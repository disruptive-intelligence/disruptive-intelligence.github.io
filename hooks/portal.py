"""Hook MkDocs : génère le portail Disruptive Intelligence à chaque build.

À partir du contenu (docs/veille, docs/analyses, docs/dossiers) et des données
(data/ressources.yml, data/sources.yml), ce hook génère EN MÉMOIRE :
  - l'accueil (index.md) ;
  - les pages d'index : veille, analyses (+ une page par thème), dossiers ;
  - les pages de ressources (un index par thème + une page par rubrique) ;
  - la navigation des onglets Veille, Analyses et Dossiers.

Rien n'est écrit sur le disque : les pages générées n'existent que dans le site
construit. Pour ajouter du contenu, il suffit de déposer un fichier Markdown
avec son en-tête au bon endroit :
  veille   : title, date, kind: veille                     -> docs/veille/AAAA/MM/AAAA-MM-JJ.md
  analyse  : title, date, kind: analysis, theme, slug, [author] -> docs/analyses/<slug>.md
  dossier  : title, date, kind: dossier, themes: [..], slug      -> docs/dossiers/<slug>.md
Le contrat (taxonomie, slug = nom du fichier) est vérifié par check_contract().
"""
import hashlib
import html
import json
import posixpath
import re
import unicodedata
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File
from mkdocs.utils.meta import get_data

# ---------------------------------------------------------------- réglages

# Taxonomie canonique, identique à celle de veille-agent (validate_editorial_publication.py).
# Analyse : `theme` (un seul, obligatoire). Dossier : `themes` (liste non vide).
THEMES = {
    "ia": "🤖 Intelligence artificielle",
    "cyber": "🛡️ Cyber",
    "tech": "💻 Tech",
    "geo-ie": "🌍 Géopolitique & IE",
}
# Rubriques des briefs -> quadrants de la page Veille
QUADS = [("cyber", "🛡️ Cyber"), ("tech", "💻 Tech"), ("geo-ie", "🌍 Géopolitique & IE"), ("ia", "🚀 IA & rupture")]
# Originaux des analyses : conservés dans le dépôt privé (lien lisible par son seul propriétaire).
PRIVATE_SOURCES = "https://github.com/H4ckeurM4n/veille-agent/blob/main/"
GROUP_FALLBACK = [("alertes-cyber", "cyber"), ("ia-rupture", "ia"), ("geopolitique-ie", "geo-ie"), ("tech", "tech")]

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

NAV_ANCHOR = "🏠 Accueil"   # les onglets générés sont insérés juste après celui-ci
LIBRARY_TAB = "📚 Bibliothèque"   # reçoit l'arborescence des notes et le Glossaire
RESSOURCES_TAB = "🧭 Ressources"   # onglet inséré juste après la Bibliothèque
RESSOURCES_SRC = "veille/ressources/index.md"   # page d'accueil des ressources (adresses inchangées)

# ---------------------------------------------------------------- utilitaires


def slug(text):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def fr_date(d):
    return f"{'1er' if d.day == 1 else d.day} {MOIS[d.month - 1]} {d.year}"


MOIS_COURTS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]


def short_month(d):
    return MOIS_COURTS[d.month - 1]


def url_of(src_uri):
    """docs/a/b.md -> a/b/   ;   a/index.md -> a/   (use_directory_urls)"""
    stem = src_uri[:-3]
    if stem == "index" or stem.endswith("/index"):
        return stem[:-5]
    return stem + "/"


def href(from_src, to_src):
    """Lien relatif entre deux pages (pour le HTML brut, que MkDocs ne réécrit pas)."""
    rel = posixpath.relpath(url_of(to_src) or ".", url_of(from_src) or ".")
    return "./" if rel == "." else rel + "/"


def esc(text):
    return html.escape(str(text), quote=True)


def clean_title(title):
    return re.sub(r"^Analyse\s*—\s*", "", str(title))


def summary_of(body, n=230):
    m = re.search(r"^## Thèse principale\s*\n+(.+?)\n\n", body, re.M | re.S)
    if not m:
        return ""
    t = re.sub(r"\*\*?|\[[^\]]*\]\s*", "", m.group(1)).replace("\n", " ").strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + " …"


def section_key(heading):
    h = heading.lower()
    if "cyber" in h and "tech &" not in h:
        return "cyber"
    if "ia &" in h or "rupture" in h:
        return "ia"
    if "géopolitique" in h or "/ ie" in h:
        return "geo-ie"
    if "tech" in h:
        return "tech"
    return None


# ---------------------------------------------------------------- lecture du contenu

STATE = {}


def check_contract(src, stem, kind, meta):
    """Garde-fou : le contenu publié doit respecter le contrat partagé avec veille-agent.
    Une violation fait échouer le build (et donc la publication)."""
    errors = []
    if kind == "analysis":
        if meta.get("theme") not in THEMES:
            errors.append(f"theme doit valoir {' | '.join(THEMES)} (reçu : {meta.get('theme')!r})")
    if kind == "dossier":
        themes = meta.get("themes")
        if not isinstance(themes, list) or not themes or len(set(themes)) != len(themes) or set(themes) - set(THEMES):
            errors.append(f"themes doit être une liste non vide et sans doublon parmi {' | '.join(THEMES)} (reçu : {themes!r})")
        if "theme" in meta:
            errors.append("un dossier utilise `themes` (liste), pas `theme`")
    if kind in ("analysis", "dossier") and meta.get("slug") != stem:
        # Les Morning Briefs ne sont pas concernés : leur nom public est dérivé de la date.
        errors.append(f"slug ({meta.get('slug')!r}) doit être identique au nom du fichier ({stem!r})")
    if errors:
        raise PluginError(f"Contrat éditorial non respecté dans docs/{src} :\n  - " + "\n  - ".join(errors))


def load_content(docs_dir):
    items = {"veille": [], "analysis": [], "dossier": []}
    for folder in ("veille", "analyses", "dossiers"):
        for f in sorted((docs_dir / folder).glob("**/*.md")) if (docs_dir / folder).exists() else []:
            body, meta = get_data(f.read_text(encoding="utf-8"))
            kind = meta.get("kind")
            if kind not in items or not meta.get("date"):
                continue
            d = meta["date"] if isinstance(meta["date"], date) else date.fromisoformat(str(meta["date"]))
            src = f.relative_to(docs_dir).as_posix()
            check_contract(src, f.stem, kind, meta)
            it = dict(src=src, title=str(meta.get("title", f.stem)), date=d, theme=meta.get("theme"),
                      themes=list(meta.get("themes") or []), author=meta.get("author"), body=body,
                      kind=kind, events=[str(e) for e in meta.get("events") or []])
            if kind == "veille":
                it["headlines"] = [re.sub(r"\s+", " ", h).strip() for h in re.findall(r"^### ▸ (.+)$", body, re.M)]
                ess = re.search(r"^!!! abstract \"L'essentiel\"\s*\n\n((?: {4}[-*] .+\n?)+)", body, re.M)
                it["essentiel"] = [l.strip()[2:] for l in ess.group(1).splitlines()] if ess else []
            else:
                it["summary"] = summary_of(body)
            items[kind].append(it)
    for lst in items.values():
        lst.sort(key=lambda x: x["date"], reverse=True)
    return items


# ---------------------------------------------------------------- sujets des briefs, fils d'actualité

THREADS_DIR = "veille/fils"
# Repère écrit par veille-agent sous chaque sujet : identité de sélection et, depuis le 28/09, fraîcheur.
MARKER = re.compile(r"^<!-- selection: (event|standalone):(\S+?)(?: freshness:(new|updated|carryover))? -->$")
FRESHNESS = {"updated": "Mise à jour", "carryover": "Suivi"}   # « new » est la norme : pas de badge
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def heading_ids(markdown):
    """Identifiants que l'extension toc donnera aux titres (même slugify, même dédoublonnage),
    dans l'ordre du document : [(niveau, texte, id)]."""
    from markdown.extensions.toc import slugify, unique
    ids, out = set(), []
    for line in markdown.splitlines():
        m = HEADING.match(line)
        if m:
            text = re.sub(r"\*\*?|`|\[([^\]]*)\]\([^)]*\)", r"\1", m.group(2))
            out.append((len(m.group(1)), text, unique(slugify(html.unescape(text), "-"), ids)))
    return out


def brief_subjects(markdown):
    """Sujets ### ▸ d'un brief : titre, ancre, rubrique, événement (repère de sélection) et « Le fait »."""
    headings = iter(heading_ids(markdown))
    lines, subjects, lane = markdown.splitlines(), [], None
    for i, line in enumerate(lines):
        if not HEADING.match(line):
            continue
        level, text, anchor = next(headings)
        if level == 2:
            lane = text
        elif level == 3 and text.startswith("▸"):
            marker = MARKER.match(lines[i + 1].strip()) if i + 1 < len(lines) else None
            fact, source = "", None
            for follow in lines[i + 1:i + 40]:
                if follow.startswith(("### ", "## ")):
                    break
                if follow.startswith("**Le fait :**"):
                    fact = follow.replace("**Le fait :**", "").strip()
                m = SOURCE_LABEL.match(follow)
                if m and source is None:
                    source = STATE.get("aliases", {}).get(m.group(2).strip(), m.group(2).strip())
            subjects.append({"title": text.lstrip("▸ ").strip(), "anchor": anchor, "lane": lane,
                             "event": marker.group(2) if marker and marker.group(1) == "event" else None,
                             "freshness": marker.group(3) if marker else None, "fact": fact,
                             "source": source, "line": i})
    return subjects


def thread_src(event_id):
    return f"{THREADS_DIR}/{event_id[:12]}.md"


def build_threads(briefs):
    """Événements suivis sur au moins deux éditions -> leur chronologie."""
    by_event = {}
    for it in sorted(briefs, key=lambda x: x["date"]):
        for s in brief_subjects(it["body"]):
            if s["event"]:
                by_event.setdefault(s["event"], []).append(dict(s, date=it["date"], src=it["src"]))
    return {e: lst for e, lst in by_event.items() if len({s["date"] for s in lst}) > 1}


def thread_title(entries):
    title = re.sub(r"^(Suivi|Mise à jour|Analyse)\s*[—–:-]\s*", "", entries[-1]["title"])
    return title[:1].upper() + title[1:]


def pages_threads(threads):
    out, cards = [], []
    for event, entries in sorted(threads.items(), key=lambda kv: kv[1][-1]["date"], reverse=True):
        src = thread_src(event)
        days = sorted({s["date"] for s in entries})
        body = ""
        for s in entries:
            link = posixpath.relpath(s["src"], THREADS_DIR) + "#" + s["anchor"]
            body += (f"\n### {fr_date(s['date'])} · {s['lane']}\n\n**[{s['title']}]({link})**\n\n"
                     + (f"{s['fact']}\n" if s["fact"] else ""))
        title = thread_title(entries)
        docs = STATE.get("linked", {}).get(event, [])
        if docs:
            body += "\n## Pour approfondir\n\n" + "".join(
                f"- {'Analyse' if d['kind'] == 'analysis' else 'Dossier'} : "
                f"[{clean_title(d['title'])}]({posixpath.relpath(d['src'], THREADS_DIR)})\n" for d in docs)
        out.append((src, f"""# 🧵 {title}

<span class="kw-muted">Fil d'actualité · {len(days)} éditions, du {fr_date(days[0])} au {fr_date(days[-1])} ·
les faits tels que rapportés dans chaque Morning Brief, du plus ancien au plus récent.</span>
{body}"""))
        key = section_key(entries[-1]["lane"] or "") or "tech"
        cards.append((days[-1], key, f'<a class="kw-card kw-lane--{key}" href="{href(THREADS_DIR + "/index.md", src)}">'
                      f'<span class="kw-card__meta"><span class="kw-lanetag kw-lane--{key}">{LANE_TAGS.get(key, "")}</span> '
                      f'{len(days)} éditions · {span_label(days[0], days[-1])}</span>'
                      f'<span class="kw-card__title">{esc(title)}</span>'
                      f'<span class="kw-card__text">{esc(plain(entries[-1]["fact"], 170))}</span></a>'))
    out.append((f"{THREADS_DIR}/index.md", threads_index(cards)))
    return out


THREAD_ACTIVE_DAYS = 7


def span_label(first, last):
    """« 24 → 28 sept. » ou « 28 sept. → 2 oct. »"""
    if first == last:
        return f"{first.day} {short_month(first)}"
    head = f"{first.day}" if (first.month, first.year) == (last.month, last.year) else f"{first.day} {short_month(first)}"
    return f"{head} → {last.day} {short_month(last)}"


def threads_index(cards, today=None):
    """Fils actifs (nouvel élément depuis moins d'une semaine) par rubrique ; les autres, en sommeil,
    repliés par mois : la page reste courte même après des mois de veille."""
    today = today or date.today()
    active = [c for c in cards if (today - c[0]).days <= THREAD_ACTIVE_DAYS]
    dormant = [c for c in cards if (today - c[0]).days > THREAD_ACTIVE_DAYS]
    body = ""
    for key, label in (("tech", "📰 Tech"), ("ia", "🚀 IA & technologies de rupture"),
                       ("cyber", "🛡️ Cyber / CTI"), ("geo-ie", "🌍 Géopolitique / IE")):
        lst = [c[2] for c in sorted(active, key=lambda c: c[0], reverse=True) if c[1] == key]
        if lst:
            body += f'\n<p class="kw-group kw-lane--{key}">{label} <span class="kw-muted">· {len(lst)}</span></p>\n<div class="kw-cards">{"".join(lst)}</div>\n'
    if not active:
        body += '\n<span class="kw-muted">Aucun fil actif cette semaine.</span>\n'
    months = {}
    for c in sorted(dormant, key=lambda c: c[0], reverse=True):
        months.setdefault((c[0].year, c[0].month), []).append(c[2])
    if months:
        body += "\n## En sommeil\n\n<span class=\"kw-muted\">Aucun nouvel élément depuis plus d'une semaine ; classés par mois du dernier épisode.</span>\n"
        for (y, m), lst in months.items():
            body += (f'\n<details class="kw-fold"><summary>{MOIS[m - 1].capitalize()} {y} · {len(lst)} fil{"s" if len(lst) > 1 else ""}</summary>'
                     f'<div class="kw-cards">{"".join(lst)}</div></details>\n')
    return f"""---
hide:
  - toc
---
# 🧵 Fils d'actualité

Un fil se crée dès qu'un même événement revient dans deux Morning Briefs : sa page donne la chronologie des faits.
**Actifs** = un nouvel épisode depuis moins de {THREAD_ACTIVE_DAYS} jours, rangés par rubrique.
{body}"""


SOURCE_LABEL = re.compile(r"^(\*\*Sources? :\*\* \[)(.+?)( — )", re.M)
READING_LABEL = re.compile(r"^(- \*\*)(.+?)(\*\* — \[)", re.M)


def media_names(markdown):
    """Anciens briefs : l'intitulé brut du flux (« Next - Flux Complet ») devient le nom du média
    (data/sources.yml, alias). Seules les étiquettes de source sont touchées, pas le texte."""
    aliases = STATE.get("aliases", {})
    swap = lambda m: m.group(1) + aliases.get(m.group(2).strip(), m.group(2)) + m.group(3)
    return READING_LABEL.sub(swap, SOURCE_LABEL.sub(swap, markdown))


def decorate_brief(markdown, src):
    """Page d'un brief : noms des médias, sommaire repliable (téléphone) et lien vers le fil des sujets suivis."""
    markdown = media_names(markdown)
    subjects = brief_subjects(markdown)
    if len(subjects) < 5:
        return markdown
    lines = markdown.splitlines()
    threads = STATE.get("threads", {})
    for s in reversed(subjects):                       # de la fin vers le début : les numéros de ligne restent justes
        key = section_key(s["lane"] or "")
        if key:                                        # couleur de rubrique (attr_list, retiré du titre avant la toc)
            lines[s["line"]] += f" {{ .kw-subj .kw-lane--{key} }}"
        pills = ""
        if s["freshness"] in FRESHNESS:
            pills += f'<span class="kw-fresh kw-fresh--{s["freshness"]}">{FRESHNESS[s["freshness"]]}</span>'
        entries = threads.get(s["event"])
        if entries:
            days = sorted({e["date"] for e in entries})
            others = [d for d in days if d != next(e["date"] for e in entries if e["src"] == src)]
            when = ", ".join(f"{d.day} {short_month(d)}" for d in others)
            pills += (f'<span class="kw-thread">🧵 Fil d\'actualité · aussi le {esc(when)} · '
                      f'<a href="{href(src, thread_src(s["event"]))}">chronologie →</a></span>')
        for doc in STATE.get("linked", {}).get(s["event"], []):      # analyses et dossiers liés (`events`)
            pills += (f'<span class="kw-thread kw-linked">{"🔎 Analyse" if doc["kind"] == "analysis" else "🗂️ Dossier"} · '
                      f'<a href="{href(src, doc["src"])}">{esc(clean_title(doc["title"]))}</a></span>')
        if pills:
            lines.insert(s["line"] + 2, f'\n<div class="kw-subj-meta">{pills}</div>\n')
    for i, line in enumerate(lines):                   # titres de rubrique
        key = section_key(line[3:]) if line.startswith("## ") else None
        if key and any(section_key(s["lane"] or "") == key for s in subjects):
            lines[i] = line + f" {{ .kw-lane .kw-lane--{key} }}"
    toc, lane = "", None
    for s in subjects:
        if s["lane"] != lane:
            toc += ("</ol>" if lane else "") + f'<p class="kw-toc-m__lane">{esc(s["lane"])}</p><ol>'
            lane = s["lane"]
        toc += f'<li><a href="#{s["anchor"]}">{esc(s["title"])}</a></li>'
    first_h2 = next(i for i, l in enumerate(lines) if l.startswith("## "))
    lines.insert(first_h2, f'<details class="kw-toc-m"><summary>Sommaire · {len(subjects)} sujets</summary>'
                           f'{toc}</ol></details>\n')
    return "\n".join(lines)


def load_yaml(path, default):
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else default


# ---------------------------------------------------------------- composants HTML

RECENT_EDITIONS = 7        # éditions montrées dans les carrousels (celle « à la une » comprise)


def all_editions_card(from_src):
    return (f'<a class="kw-ed kw-ed--all" href="{href(from_src, "veille/index.md")}#calendrier">'
            f'<span class="kw-ed__label">Archives</span><span class="kw-ed__date">Toutes les éditions →</span>'
            f'<span class="kw-ed__more">Calendrier et archives mensuelles</span></a>')


def edition_card(it, from_src, featured=False):
    d, n = it["date"], 3 if featured else 2
    heads = "".join(f"<li>{esc(h)}</li>" for h in it["headlines"][:n])
    more = len(it["headlines"]) - n
    label = "À la une" if featured else JOURS[d.weekday()].capitalize()
    return (f'<a class="kw-ed{" kw-ed--featured" if featured else ""}" href="{href(from_src, it["src"])}">'
            f'<span class="kw-ed__label">{label}</span>'
            f'<span class="kw-ed__date">{d.day} {short_month(d)}</span>'
            f'<ul class="kw-ed__heads">{heads}</ul>'
            + (f'<span class="kw-ed__more">+ {more} autres sujets</span>' if more > 0 else "") + "</a>")


def meta_line(*parts):
    """« auteur · thème » sans séparateur orphelin quand une partie est absente (author est facultatif)."""
    return " · ".join(esc(p) for p in parts if p)


def themes_label(it):
    return " · ".join(THEMES[t] for t in it["themes"] if t in THEMES)


def analysis_card(it, from_src, with_theme=False):
    """with_theme : auteur · thème (accueil) ; sinon auteur · date (pages déjà classées par thème)."""
    second = THEMES.get(it["theme"], "") if with_theme else fr_date(it["date"])
    return (f'<a class="kw-card" href="{href(from_src, it["src"])}">'
            f'<span class="kw-card__meta">{meta_line(it["author"], second)}</span>'
            f'<span class="kw-card__title">{esc(clean_title(it["title"]))}</span>'
            f'<span class="kw-card__text">{esc(it["summary"])}</span></a>')


def carousel(cards):
    return f'<div class="kw-carousel kw-carousel--cards">{"".join(cards)}</div>'


# ---------------------------------------------------------------- pages générées

def page_veille(items, sources):
    src = "veille/index.md"
    briefs = items["veille"]
    # sources : rangées dans la rubrique du brief où elles sont le plus citées
    # nom cité dans un brief -> source (nom du média ou ancien intitulé du flux)
    canonical = {}
    for s in sources:
        for label in [s["name"]] + list(s.get("aliases") or []):
            canonical[label.strip()] = s["name"]
    cited = {}
    for it in briefs:
        sec = None
        for line in it["body"].splitlines():
            if line.startswith("## "):
                sec = section_key(line)
            m = re.match(r"\*\*Sources? :\*\* \[([^\]]+?) — ", line)
            if m and sec:
                c = cited.setdefault(canonical.get(m.group(1).strip(), m.group(1).strip()), {})
                c[sec] = c.get(sec, 0) + 1
    quads = {k: [] for k, _ in QUADS}
    for s in sources:
        c = cited.get(s["name"], {})
        key = max(c, key=c.get) if c else next((q for g, q in GROUP_FALLBACK if g in s.get("groups", [])), "tech")
        quads[key].append((s["name"], s["site"], sum(c.values())))
    panels = ""
    for key, label in QUADS:
        lst = sorted(quads[key], key=lambda x: (-x[2], x[0].lower()))
        li = "".join(f'<li><a href="{esc(site)}">{esc(n)}</a>'
                     + (f'<span class="kw-count">{c}</span>' if c else "") + "</li>" for n, site, c in lst)
        panels += f'<div class="kw-quad"><h3>{label} <span class="kw-muted">· {len(lst)}</span></h3><ul>{li}</ul></div>'

    editions = ""
    if briefs:
        entries = STATE.get("agenda", [])
        editions = (f'<div class="kw-editions">{edition_card(briefs[0], src, True)}'
                    f'<div class="kw-carousel">{"".join(edition_card(it, src) for it in briefs[1:RECENT_EDITIONS])}'
                    f'{all_editions_card(src)}</div></div>'
                    f'\n\n## Calendrier {{ #calendrier }}\n\n<div class="kw-dash-wrap"><div class="kw-dash">{veille_calendar(briefs, entries, src)}'
                    f'{upcoming_panel(entries, src)}{active_threads_panel(STATE.get("threads", {}), src)}</div></div>')
    return src, f"""---
hide:
  - toc
---
# 📡 Veille quotidienne

Les éditions du **Morning Intelligence Brief** : les événements retenus, leur contexte et les sources pour approfondir.

<div class="kw-tools"><a class="kw-rss kw-rss--fils" href="explorer/">🔎 Explorer</a> <a class="kw-rss kw-rss--fils" href="fils/">🧵 Fils d'actualité</a> <a class="kw-rss kw-rss--fils" href="semaines/">🗓️ Semaines</a> <a class="kw-rss kw-rss--fils" href="agenda/">📅 Agenda</a> <a class="kw-rss kw-rss--fils" href="lectures/">📚 Pile de lecture</a> <a class="kw-rss" href="feed.xml">📡 Flux RSS</a></div>

{editions}

## Sources suivies

<span class="kw-muted">{len(sources)} sources actives. Chaque source est rangée dans la rubrique où elle est le plus citée ; le chiffre = nombre de citations dans les briefs publiés.</span>

<div class="kw-quads">{panels}</div>
"""


def pages_analyses(items):
    out, body = [], ""
    for key, label in THEMES.items():
        lst = [it for it in items["analysis"] if it["theme"] == key]
        if not lst:
            body += f"\n## {label}\n\n<span class=\"kw-muted\">Aucune analyse pour l'instant.</span>\n"
            continue
        tsrc = f"analyses/theme-{key}/index.md"
        grid = "".join(analysis_card(it, tsrc) for it in lst)
        out.append((tsrc, f"---\nhide:\n  - toc\n---\n# {label}\n\n"
                          f"<span class=\"kw-muted\">{len(lst)} analyse{'s' if len(lst) > 1 else ''}</span>\n\n"
                          f'<div class="kw-cards">{grid}</div>\n'))
        body += (f"\n## {label} <span class=\"kw-muted\">· {len(lst)}</span>\n\n"
                 f'<a class="kw-more-link" href="{href("analyses/index.md", tsrc)}">Tout voir →</a>\n\n'
                 + carousel(analysis_card(it, "analyses/index.md") for it in lst) + "\n")
    out.append(("analyses/index.md", "# 🔎 Analyses\n\nUne lecture approfondie des rapports, articles et publications : "
                                     "thèse, arguments, limites et intérêt pour la veille.\n" + body))
    return out


def page_dossiers(items):
    body = ""
    for key, label in THEMES.items():
        lst = [it for it in items["dossier"] if key in it["themes"]]   # un dossier apparaît sous chacun de ses thèmes
        body += f"\n## {label}\n\n"
        body += "".join(f"- [{it['title']}]({posixpath.relpath(it['src'], 'dossiers')}) — {fr_date(it['date'])}\n"
                        for it in lst) if lst else "<span class=\"kw-muted\">Aucun dossier pour l'instant.</span>\n"
    return "dossiers/index.md", "# 🗂️ Dossiers & synthèses\n\nCroiser les analyses pour mettre les enjeux en perspective.\n" + body


def pages_ressources(themes):
    out = []
    for t in themes:
        cards = ""
        for r in t["rubriques"]:
            links = r.get("liens") or []
            rsrc = f"veille/ressources/{t['id']}/{slug(r['nom'])}.md"
            body = (f"# {r['nom']}\n\n<span class=\"kw-muted\">Ressources · {t['label']} · "
                    f"{len(links)} lien{'s' if len(links) > 1 else ''}</span>\n\n")
            if links:
                body += "| Ressource | Type | Pourquoi |\n|---|---|---|\n" + "".join(
                    f"| {('[' + l['nom'] + '](' + l['url'] + ')') if l.get('url') else l['nom']} "
                    f"| <span class=\"kw-type\">{l.get('type', '')}</span> | {l.get('pourquoi', '')} |\n" for l in links)
            else:
                body += '!!! note "À compléter"\n    Aucune ressource pour l\'instant dans cette rubrique.\n'
            out.append((rsrc, body))
            preview = " · ".join(l["nom"] for l in links[:3])
            n = f"{len(links)} ressource{'s' if len(links) > 1 else ''}" if links else "À compléter"
            cards += (f'<a class="kw-card" href="{slug(r["nom"])}/"><span class="kw-card__title">{esc(r["nom"])}</span>'
                      f'<span class="kw-card__meta">{n}</span><span class="kw-card__text">{esc(preview)}</span></a>')
        out.append((f"veille/ressources/{t['id']}/index.md",
                    f"---\nhide:\n  - toc\n---\n# {t['label']} — Ressources\n\n"
                    "Sites, pages et articles de référence, en complément des sources suivies par la veille.\n\n"
                    f'<div class="kw-wiki">{cards}</div>\n'))
    out.append(page_ressources_index(themes))
    return out


def page_ressources_index(themes):
    """Page d'accueil de l'onglet Ressources : tous les thèmes et toutes leurs rubriques."""
    src = RESSOURCES_SRC
    total = sum(len(r.get("liens") or []) for t in themes for r in t["rubriques"])
    body = ""
    for t in themes:
        base = f"veille/ressources/{t['id']}"
        n = sum(len(r.get("liens") or []) for r in t["rubriques"])
        cards = ""
        for r in t["rubriques"]:
            links = r.get("liens") or []
            count = f"{len(links)} ressource{'s' if len(links) > 1 else ''}" if links else "À compléter"
            preview = " · ".join(l["nom"] for l in links[:3])
            cards += (f'<a class="kw-card" href="{href(src, base + "/" + slug(r["nom"]) + ".md")}">'
                      f'<span class="kw-card__title">{esc(r["nom"])}</span>'
                      f'<span class="kw-card__meta">{count}</span>'
                      f'<span class="kw-card__text">{esc(preview)}</span></a>')
        body += (f"\n## {t['label']} <span class=\"kw-muted\">· {n}</span>\n\n"
                 f'<a class="kw-more-link" href="{href(src, base + "/index.md")}">Tout le thème →</a>\n\n'
                 f'<div class="kw-wiki">{cards}</div>\n')
    return src, f"""---
hide:
  - toc
---
# 🧭 Ressources

Sites, outils, formations et lectures de référence, en complément des sources suivies par la veille.
{total} ressources, {len(themes)} thèmes.

{resources_carousel(themes, src)}
{body}"""


def resources_carousel(themes, src):
    """Carrousel des thèmes de ressources : les 3 rubriques les plus fournies de chaque thème."""
    cards = ""
    for t in themes:
        rubs = t["rubriques"]
        n = sum(len(r.get("liens") or []) for r in rubs)
        top = sorted(((r["nom"], len(r.get("liens") or [])) for r in rubs if r.get("liens")), key=lambda x: -x[1])[:3]
        tops = "".join(f'<li><span>{esc(s)}</span><span class="kw-count">{c}</span></li>' for s, c in top)
        cards += (f'<a class="kw-card kw-res" href="{href(src, "veille/ressources/" + t["id"] + "/index.md")}">'
                  f'<span class="kw-res__label">{t["label"]}</span>'
                  f'<span class="kw-card__meta">{n} ressources · {len(rubs)} rubriques</span>'
                  f'<ul class="kw-res__tops">{tops}</ul></a>')
    return carousel([cards])


def essentiel_block(it, from_src):
    """Accueil : l'encadré « L'essentiel » du dernier brief, quand il existe (depuis le 29/09)."""
    if not it.get("essentiel"):
        return ""
    lis = "".join(f"<li>{esc(re.sub(r'[*`]', '', x))}</li>" for x in it["essentiel"])
    return (f'<div class="kw-essentiel"><p class="kw-essentiel__title">L\'essentiel du {it["date"].day} '
            f'{short_month(it["date"])} <a href="{href(from_src, it["src"])}">lire le brief →</a></p><ul>{lis}</ul></div>')


def page_home(items, themes, glossary):
    src = "index.md"
    briefs, analyses, dossiers = items["veille"], items["analysis"], items["dossier"]
    une = ""
    if briefs:
        une += edition_card(briefs[0], src, True)
    if analyses:
        a = analyses[0]
        une += (f'<a class="kw-card" href="{href(src, a["src"])}"><span class="kw-ed__label">Dernière analyse</span>'
                f'<span class="kw-card__meta">{meta_line(a["author"], THEMES.get(a["theme"], ""))}</span>'
                f'<span class="kw-card__title">{esc(clean_title(a["title"]))}</span>'
                f'<span class="kw-card__text">{esc(a["summary"])}</span></a>')
    if dossiers:
        d = dossiers[0]
        une += (f'<a class="kw-card" href="{href(src, d["src"])}"><span class="kw-ed__label">Dernier dossier</span>'
                f'<span class="kw-card__meta">{meta_line(themes_label(d), fr_date(d["date"]))}</span>'
                f'<span class="kw-card__title">{esc(d["title"])}</span>'
                f'<span class="kw-card__text">Croiser les analyses pour mettre les enjeux en perspective.</span></a>')

    total = sum(len(r.get("liens") or []) for t in themes for r in t["rubriques"])
    # Glossaire : les termes les plus récents (ordre des briefs), en pastilles vers la lettre du glossaire
    recent = sorted(glossary, key=lambda t: max((it["date"] for it in t["seen"]), default=date.min), reverse=True)[:14]
    chips = "".join(
        f'<a class="kw-chip" href="{href(src, GLOSSARY_SRC)}#{letter_anchor(t["term"])}">{esc(t["term"])}</a>'
        for t in recent)

    wiki = [("⚔️ Pentest", "Checklist avant engagement", "Préparer l'environnement, définir les variables, lancer la méthodologie.", "start/checklist.md"),
            ("⚔️ Pentest", "Méthodologie", "Les 7 phases et le tableau port → fiche.", "methodology/index.md"),
            ("⚔️ Pentest", "Services réseau", "Une fiche par service, nommée avec ses ports.", "services/index.md"),
            ("📚 Bibliothèque", "Notes de cours", "Cyber et IT : synthèses pour apprendre et réviser.", "library/index.md")]
    wiki_cards = "".join(f'<a class="kw-card" href="{href(src, s)}"><span class="kw-ed__label">{a}</span>'
                         f'<span class="kw-card__title">{b}</span><span class="kw-card__text">{c}</span></a>'
                         for a, b, c, s in wiki)

    return src, f"""---
hide:
  - navigation
  - toc
---
<div class="kw-hero" markdown>

# Disruptive Intelligence

<p class="kw-hero__tagline"><strong>Tech · IA · Cyber · Géopolitique</strong> — veille quotidienne, analyses et base de connaissances.</p>

</div>

## À la une

<div class="kw-une">{une}</div>
{essentiel_block(briefs[0], src) if briefs else ""}

## 📡 Veille récente

<a class="kw-more-link" href="veille/">Toutes les éditions →</a>

<div class="kw-carousel">{"".join(edition_card(it, src) for it in briefs[1:RECENT_EDITIONS])}{all_editions_card(src)}</div>

## 🔎 Analyses récentes

<a class="kw-more-link" href="analyses/">Toutes les analyses →</a>

{carousel(analysis_card(it, src, with_theme=True) for it in analyses[:6])}

## 🧭 Ressources <span class="kw-muted">· {total}</span>

{resources_carousel(themes, src)}

## 📖 Glossaire <span class="kw-muted">· {len(glossary)}</span>

<a class="kw-more-link" href="{href(src, GLOSSARY_SRC)}">Tout le glossaire →</a>

<div class="kw-chips">{chips}</div>

## 📚 Le wiki

<div class="kw-wiki">{wiki_cards}</div>
"""


# ---------------------------------------------------------------- veille : explorer, lectures, agenda, semaines

LANE_TAGS = {"tech": "Tech", "ia": "IA & rupture", "cyber": "Cyber", "geo-ie": "Géopolitique"}
EXPLORER_SRC = "veille/explorer.md"
READING_SRC = "veille/lectures.md"
AGENDA_SRC = "veille/agenda.md"
WEEKS_DIR = "veille/semaines"
READING_ENTRY = re.compile(r"^[-*]\s+\*\*(.+?)\*\*\s+—\s+\[(.+?)\]\((\S+?)\)\.?\s*(.*)$")
FR_DATE = re.compile(r"\b(1er|\d{1,2})\s+(" + "|".join(MOIS) + r")(?:\s+(\d{4}))?", re.I)


def all_subjects(briefs):
    """Tous les sujets de toutes les éditions, du plus récent au plus ancien."""
    return [dict(s, date=it["date"], src=it["src"], key=section_key(s["lane"] or ""))
            for it in briefs for s in brief_subjects(it["body"])]


def section_body(body, heading):
    m = re.search(r"^## " + heading + r"\s*\n(.*?)(?=^## |^\*Lecture|\Z)", body, re.M | re.S)
    return m.group(1) if m else ""


def explorer_data(briefs):
    """assets/veille-sujets.json : tous les sujets, lus par l'Explorer (affichage paginé côté navigateur)."""
    rows = []
    for s in all_subjects(briefs):
        fact = re.sub(r"\*\*?|`|\[([^\]]*)\]\([^)]*\)", r"\1", s["fact"])
        rows.append({"d": s["date"].isoformat(), "l": s["key"] or "", "f": s["freshness"] or "",
                     "t": s["title"], "u": url_of(s["src"]) + "#" + s["anchor"], "s": s["source"] or "",
                     "x": fact if len(fact) <= 260 else fact[:260].rsplit(" ", 1)[0] + " …"})
    return "assets/veille-sujets.json", json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


def page_explorer(briefs):
    subjects = sum(len(brief_subjects(it["body"])) for it in briefs)
    options = "".join(f'<option value="{k}">{v}</option>' for k, v in LANE_TAGS.items())
    return EXPLORER_SRC, f"""---
hide:
  - toc
---
# 🔎 Explorer la veille

<span class="kw-muted">{subjects} sujets dans {len(briefs)} éditions, affichés 50 par page, du plus récent au plus ancien.
Filtrer par mot (acteur, pays, technologie, média), période, rubrique ou statut.</span>

<div class="kw-explorer" id="kw-explorer" data-src="assets/veille-sujets.json">
<div class="kw-explorer__bar">
<input type="search" class="kw-explorer__q" placeholder="Rechercher : Anthropic, Ukraine, ransomware…" aria-label="Rechercher dans les sujets">
<select class="kw-explorer__period" aria-label="Période"><option value="">Toute la période</option><option value="7">7 derniers jours</option><option value="30">30 derniers jours</option><option value="90">3 derniers mois</option></select>
<select class="kw-explorer__lane" aria-label="Rubrique"><option value="">Toutes les rubriques</option>{options}</select>
<select class="kw-explorer__fresh" aria-label="Statut"><option value="">Tous les statuts</option><option value="new">Nouveaux</option><option value="updated">Mises à jour</option><option value="carryover">Suivis</option></select>
<span class="kw-explorer__count kw-muted"></span>
</div>
<p class="kw-legend"><strong>Nouveau</strong> : premier traitement du sujet · <strong>Mise à jour</strong> : sujet déjà traité, avec un fait nouveau ce jour-là ·
<strong>Suivi</strong> : sujet déjà traité, rappelé sans fait nouveau (échéance, enjeu toujours actuel).</p>
<table class="kw-explorer__table"><thead><tr><th>Date</th><th>Rubrique</th><th>Sujet</th><th>Source</th></tr></thead><tbody></tbody></table>
<nav class="kw-pager" aria-label="Pages de résultats"></nav>
<noscript>L'Explorer a besoin de JavaScript ; les éditions restent accessibles depuis la page Veille.</noscript>
</div>
"""


READING_DAYS_PER_PAGE = 5


def page_readings(briefs):
    src = READING_SRC
    groups, total = "", 0
    for it in briefs:
        entries = [READING_ENTRY.match(l.strip()) for l in section_body(it["body"], "📚 Reading list").splitlines()]
        entries = [e for e in entries if e]
        if not entries:
            continue
        total += len(entries)
        items = "".join(
            f'<li class="kw-read" data-url="{esc(e.group(3))}"><label><input type="checkbox" class="kw-read__box" '
            f'aria-label="Marquer comme lu"></label><div><a href="{esc(e.group(3))}">{esc(e.group(2).strip("«» "))}</a>'
            f'<span class="kw-read__meta">{esc(STATE.get("aliases", {}).get(e.group(1).strip(), e.group(1).strip()))}</span>'
            f'<span class="kw-read__why">{esc(re.sub(r"[*`]", "", e.group(4)))}</span></div></li>'
            for e in entries)
        groups += (f'<section class="kw-read__group"><p class="kw-read__day">{JOURS[it["date"].weekday()].capitalize()} '
                   f'{fr_date(it["date"])} <a class="kw-read__brief" href="{href(src, it["src"])}">le brief →</a></p>'
                   f'<ul class="kw-reads">{items}</ul></section>')
    return src, f"""---
hide:
  - toc
---
# 📚 Pile de lecture

<span class="kw-muted">{total} lectures approfondies recommandées par les Morning Briefs, {READING_DAYS_PER_PAGE} éditions par page.
Cocher une lecture la marque comme lue sur cet appareil.</span>

<div class="kw-readings" id="kw-readings" data-per-page="{READING_DAYS_PER_PAGE}">
<p class="kw-readings__bar"><label><input type="checkbox" class="kw-read__hide"> Masquer les lectures faites</label>
<span class="kw-readings__count kw-muted"></span></p>
{groups}
<nav class="kw-pager" aria-label="Pages de lectures"></nav>
</div>
"""


def milestone_date(text, edition):
    """« 1er octobre », « mercredi 30 septembre 2026 » -> date ; l'année manquante suit l'édition."""
    m = FR_DATE.search(text)
    if not m:
        return None
    day = 1 if m.group(1) == "1er" else int(m.group(1))
    month = MOIS.index(m.group(2).lower()) + 1
    year = int(m.group(3)) if m.group(3) else edition.year + (1 if month < edition.month - 6 else 0)
    try:
        return date(year, month, day)
    except ValueError:
        return None


def agenda_entries(briefs):
    """Jalons datés des sections « À surveiller » : [(date, texte, brief)], sans doublon."""
    seen, out = set(), []
    for it in briefs:
        for line in section_body(it["body"], "À surveiller").splitlines():
            line = line.strip()
            if not line.startswith(("- ", "* ")):
                continue
            head = re.match(r"^[-*]\s+\*\*(.+?)\s*:?\*\*\s*:?\s*(.*)$", line)
            when = milestone_date(head.group(1) if head else line, it["date"])
            if not when:
                continue
            text = head.group(2) if head and milestone_date(head.group(1), it["date"]) else line[2:]
            if (when, text[:60]) not in seen:
                seen.add((when, text[:60]))
                out.append((when, text, it))
    return sorted(out, key=lambda e: e[0])


def plain(text, n=None):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*`]", "", text).strip()
    return text if n is None or len(text) <= n else text[:n].rsplit(" ", 1)[0] + " …"


def page_agenda(briefs, today=None):
    src = AGENDA_SRC
    today = today or date.today()
    entries = STATE.get("agenda") or agenda_entries(briefs)
    upcoming = [e for e in entries if e[0] >= today]
    past = [e for e in reversed(entries) if e[0] < today and (today - e[0]).days <= 45]

    def render(lst):
        return "".join(f'<li id="j-{w.isoformat()}"><span class="kw-agenda__date">{JOURS[w.weekday()]} {fr_date(w)}</span>'
                       f'<span class="kw-agenda__text">{esc(plain(t))}</span>'
                       f'<a class="kw-agenda__brief" href="{href(src, it["src"])}">brief du {it["date"].day} {short_month(it["date"])}</a></li>'
                       for w, t, it in lst)
    cal = agenda_calendar(entries, src, today)
    return src, f"""---
hide:
  - toc
---
# 📅 Agenda

Les jalons datés relevés dans la section « À surveiller » des Morning Briefs.

<div class="kw-dash-wrap"><div class="kw-dash kw-dash--2">{cal}{upcoming_panel(entries, src, today, 8)}</div></div>

## À venir

{f'<ul class="kw-agenda">{render(upcoming)}</ul>' if upcoming else '<span class="kw-muted">Aucun jalon à venir pour l’instant.</span>'}

## Passés (45 derniers jours)

{f'<ul class="kw-agenda kw-agenda--past">{render(past)}</ul>' if past else '<span class="kw-muted">Aucun jalon passé récent.</span>'}
"""


def iso_week(d):
    y, w, _ = d.isocalendar()
    return f"{y}-s{w:02d}"


def week_span(monday):
    sunday = monday + timedelta(days=6)
    if monday.month == sunday.month:
        return f"{monday.day}–{sunday.day} {short_month(sunday)}"
    return f"{monday.day} {short_month(monday)} – {sunday.day} {short_month(sunday)}"


def plural(n, word):
    return f"{n} {word}{'s' if n > 1 else ''}"


def pages_weeks(briefs, threads):
    """Une page par semaine : les sujets de la semaine par rubrique, un événement une seule fois.
    L'index range les semaines par mois ; seuls les deux mois les plus récents sont dépliés."""
    by_week = {}
    for s in all_subjects(briefs):
        by_week.setdefault(iso_week(s["date"]), []).append(s)
    out, rows = [], []
    for week, subjects in sorted(by_week.items(), reverse=True):
        src = f"{WEEKS_DIR}/{week}.md"
        days = sorted({s["date"] for s in subjects})
        monday = days[0] - timedelta(days=days[0].weekday())
        sunday = monday + timedelta(days=6)
        body = ""
        for key, label in (("tech", "📰 Tech"), ("ia", "🚀 IA & technologies de rupture"),
                           ("cyber", "🛡️ Cyber / CTI"), ("geo-ie", "🌍 Géopolitique / IE")):
            groups = {}
            for s in sorted((s for s in subjects if s["key"] == key), key=lambda s: s["date"]):
                groups.setdefault(s["event"] or (s["src"], s["anchor"]), []).append(s)
            if not groups:
                continue
            body += f"\n## {label} {{ .kw-lane .kw-lane--{key} }}\n\n"
            for entries in sorted(groups.values(), key=lambda g: g[-1]["date"], reverse=True):
                last = entries[-1]
                when = ", ".join(f"[{e['date'].day} {short_month(e['date'])}]({posixpath.relpath(e['src'], WEEKS_DIR)}#{e['anchor']})"
                                 for e in entries)
                thread = (f" · [🧵 fil]({posixpath.relpath(thread_src(last['event']), WEEKS_DIR)})"
                          if last["event"] in threads else "")
                body += f"- **{last['title']}** — {when}" + (f" · {last['source']}" if last["source"] else "") + thread + "\n"
        n_subjects = len({s["event"] or s["anchor"] for s in subjects})
        title = f"Semaine du {monday.day}{' ' + MOIS[monday.month - 1] if monday.month != sunday.month else ''} au {fr_date(sunday)}"
        out.append((src, f"# 🗓️ {title}\n\n<span class=\"kw-muted\">{plural(len(days), 'édition')} · {n_subjects} sujets distincts. "
                         f"Un sujet repris plusieurs jours n'apparaît qu'une fois, avec ses dates.</span>\n{body}"))
        rows.append((monday, src, len(days), n_subjects))
    months = {}
    for monday, s, d, n in rows:
        months.setdefault((monday.year, monday.month), []).append(
            f'<a class="kw-week" href="{href(WEEKS_DIR + "/index.md", s)}"><span class="kw-week__no">S{monday.isocalendar()[1]}</span>'
            f'<span class="kw-week__span">{week_span(monday)}</span>'
            f'<span class="kw-week__meta">{plural(d, "édition")} · {n} sujets</span></a>')
    body = ""
    for i, ((y, m), lst) in enumerate(months.items()):
        block = f'<div class="kw-weeks">{"".join(lst)}</div>'
        body += (f'\n<p class="kw-group">{MOIS[m - 1].capitalize()} {y}</p>\n{block}\n' if i < 2 else
                 f'\n<details class="kw-fold"><summary>{MOIS[m - 1].capitalize()} {y} · {plural(len(lst), "semaine")}</summary>{block}</details>\n')
    out.append((f"{WEEKS_DIR}/index.md", f"---\nhide:\n  - toc\n---\n# 🗓️ Semaines\n\nLa veille relue à l'échelle de la semaine : "
                                         f"tous les sujets par rubrique, sans doublon. Une semaine commence le lundi.\n{body}"))
    return out


# ---------------------------------------------------------------- calendriers

def month_calendar(marks, months, default, from_src, title, cid, today=None):
    """Calendriers mensuels feuilletables (‹ ›) : marks = {date: (lien, info-bulle, classe)}.
    Sans JavaScript, tous les mois restent affichés les uns sous les autres."""
    today = today or date.today()
    panels = ""
    for y, m in months:
        first = date(y, m, 1)
        nxt = date(y + (m == 12), m % 12 + 1, 1)
        cells = "".join(f'<span class="kw-cal__head">{j[:1].upper()}</span>' for j in JOURS)
        cells += '<span class="kw-cal__pad"></span>' * first.weekday()
        d, n = first, 0
        while d < nxt:
            mark = marks.get(d)
            cls = " is-today" if d == today else ""
            if mark:
                n += 1
                cells += (f'<a class="kw-cal__day {mark[2]}{cls}" href="{mark[0]}" title="{esc(mark[1])}">{d.day}</a>')
            else:
                cells += f'<span class="kw-cal__day{cls}">{d.day}</span>'
            d += timedelta(days=1)
        panels += (f'<div class="kw-cal__month" data-month="{y}-{m:02d}"{" data-default" if (y, m) == default else ""}>'
                   f'<p class="kw-cal__mtitle">{MOIS[m - 1].capitalize()} {y}</p><div class="kw-cal__grid">{cells}</div></div>')
    return (f'<div class="kw-cal" id="{cid}"><div class="kw-cal__nav"><button type="button" class="kw-cal__prev" aria-label="Mois précédent">‹</button>'
            f'<span class="kw-cal__title">{title}</span>'
            f'<button type="button" class="kw-cal__next" aria-label="Mois suivant">›</button></div>{panels}</div>')


def month_range(first, last):
    out, (y, m) = [], (first.year, first.month)
    while (y, m) <= (last.year, last.month):
        out.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def veille_calendar(briefs, entries, from_src, today=None):
    """Un seul calendrier : jours d'édition (rouge, lien vers le brief) et jalons de l'agenda
    (point ambre ; case ambre quand aucun brief n'est paru ce jour-là)."""
    today = today or date.today()
    events = {}
    for when, text, _ in entries:
        events.setdefault(when, []).append(plain(text, 80))
    marks = {it["date"]: (href(from_src, it["src"]), f"Morning Brief du {fr_date(it['date'])}", "is-on")
             for it in briefs}
    for when, texts in events.items():
        tip = "À surveiller : " + " · ".join(texts)
        if when in marks:
            link, title, cls = marks[when]
            marks[when] = (link, f"{title} — {tip}", cls + " has-event")
        else:
            marks[when] = (href(from_src, AGENDA_SRC) + f"#j-{when.isoformat()}", tip,
                           "is-event" + (" is-past" if when < today else ""))
    if not marks:
        return ""
    months = month_range(min(list(marks) + [today]), max(list(marks) + [today]))
    html = month_calendar(marks, months, (today.year, today.month), from_src,
                          "📡 Éditions et jalons", "kw-cal-veille", today)
    legend = ('<p class="kw-cal__legend"><span class="kw-dot kw-dot--brief"></span>brief '
              '<span class="kw-dot kw-dot--event"></span>jalon à surveiller</p>')
    return html[:-len("</div>")] + legend + "</div>"


def active_threads_panel(threads, from_src, today=None, n=5):
    """Les fils qui bougent : dernier épisode depuis moins d'une semaine, le plus récent d'abord."""
    today = today or date.today()
    live = sorted(((entries[-1]["date"], event, entries) for event, entries in threads.items()
                   if (today - entries[-1]["date"]).days <= THREAD_ACTIVE_DAYS), key=lambda x: x[0], reverse=True)[:n]
    items = ""
    for _, event, entries in live:
        key = section_key(entries[-1]["lane"] or "") or "tech"
        days = sorted({e["date"] for e in entries})
        items += (f'<li><a href="{href(from_src, thread_src(event))}"><span class="kw-up__date kw-up__date--lane kw-lane--{key}">'
                  f'{span_label(days[0], days[-1])}</span><span class="kw-up__text">{esc(plain(thread_title(entries), 90))}'
                  f' <span class="kw-muted">· {len(days)} éd.</span></span></a></li>')
    return (f'<div class="kw-up"><p class="kw-up__title">🧵 Fils actifs <a href="{href(from_src, THREADS_DIR + "/index.md")}">tous les fils →</a></p>'
            + (f'<ul>{items}</ul>' if items else '<p class="kw-muted">Aucun fil actif cette semaine.</p>') + "</div>")


def editions_calendar(briefs, from_src):
    if not briefs:
        return ""
    marks = {it["date"]: (href(from_src, it["src"]), f"Morning Brief du {fr_date(it['date'])}", "is-on")
             for it in briefs}
    last = max(marks)
    return month_calendar(marks, month_range(min(marks), last), (last.year, last.month), from_src,
                          "📡 Éditions", "kw-cal-editions")


def agenda_calendar(entries, from_src, today=None):
    today = today or date.today()
    marks = {}
    for when, text, _ in entries:
        link = href(from_src, AGENDA_SRC) + f"#j-{when.isoformat()}"
        prev = marks.get(when)
        marks[when] = (link, (prev[1] + " · " if prev else "") + plain(text, 90),
                       "is-event" + (" is-past" if when < today else ""))
    first = min([today] + list(marks))
    last = max([today + timedelta(days=31)] + list(marks))
    return month_calendar(marks, month_range(first, last), (today.year, today.month), from_src,
                          "📅 Agenda", "kw-cal-agenda", today)


def upcoming_panel(entries, from_src, today=None, n=5):
    today = today or date.today()
    nxt = [e for e in entries if e[0] >= today][:n]
    items = "".join(f'<li><a href="{href(from_src, AGENDA_SRC)}#j-{w.isoformat()}"><span class="kw-up__date">'
                    f'{JOURS[w.weekday()][:3]}. {w.day} {short_month(w)}</span><span class="kw-up__text">{esc(plain(t, 110))}</span></a></li>'
                    for w, t, _ in nxt)
    return (f'<div class="kw-up"><p class="kw-up__title">⏳ À venir <a href="{href(from_src, AGENDA_SRC)}">agenda complet →</a></p>'
            + (f'<ul>{items}</ul>' if items else '<p class="kw-muted">Aucun jalon daté à venir dans les derniers briefs.</p>') + "</div>")


# ---------------------------------------------------------------- analyses et dossiers : en-tête

def reading_minutes(markdown):
    words = len(re.sub(r"\]\([^)]*\)|<[^>]+>|[#*`>|-]", " ", markdown).split())
    return max(1, round(words / 200))


def fold_section(markdown, heading, admonition, title):
    """Replie une section « ## heading » dans un bloc dépliable (hors table des matières)."""
    m = re.search(r"^## " + re.escape(heading) + r"\s*\n(.*?)(?=^## |\Z)", markdown, re.M | re.S)
    if not m:
        return markdown
    body = "\n".join(("    " + l) if l.strip() else "" for l in m.group(1).strip("\n").splitlines())
    return markdown[:m.start()] + f'??? {admonition} "{title}"\n\n{body}\n\n' + markdown[m.end():]


def decorate_document(markdown, page):
    """Analyse ou dossier : en-tête (nature, thème, auteur, date, temps de lecture) et
    métadonnées internes repliées."""
    meta, kind = page.meta, page.meta.get("kind")
    d = meta.get("date")
    d = d if isinstance(d, date) else date.fromisoformat(str(d))
    if kind == "analysis":
        label = "Analyse · " + THEMES.get(meta.get("theme"), "")
        who = meta_line(meta.get("author"), meta.get("organization"))
    else:
        label = "Dossier · " + " · ".join(THEMES[t] for t in meta.get("themes") or [] if t in THEMES)
        who = ""
    tags = "".join(f'<span class="kw-chip kw-chip--static">{esc(t)}</span>' for t in meta.get("tags") or [])
    head = (f'<div class="kw-doc-head"><span class="kw-doc-head__kind">{label}</span>'
            f'<span class="kw-doc-head__meta">{meta_line(who, fr_date(d), f"{reading_minutes(markdown)} min de lecture")}</span>'
            + (f'<span class="kw-doc-head__tags">{tags}</span>' if tags else "") + "</div>\n")
    follow = []                                        # événements de la veille éclairés par le document
    for event in meta.get("events") or []:
        mentions = STATE.get("mentions", {}).get(str(event), [])
        if str(event) in STATE.get("threads", {}):
            follow.append(f'<a href="{href(page.file.src_uri, thread_src(str(event)))}">🧵 {esc(thread_title(STATE["threads"][str(event)]))}</a>')
        elif mentions:
            m = mentions[-1]
            follow.append(f'<a href="{href(page.file.src_uri, m["src"])}#{m["anchor"]}">📡 {esc(m["title"])} '
                          f'({m["date"].day} {short_month(m["date"])})</a>')
    if follow:
        head = head.replace("</div>\n", f'<span class="kw-doc-head__follow">Dans la veille : {" · ".join(follow)}</span></div>\n', 1)
    # Document original : lien public (source_url) et/ou fichier du dépôt privé (source_file).
    # Le portail n'héberge jamais le document lui-même.
    links = ""
    if meta.get("source_url"):
        links += (f'<a class="kw-doc-btn" href="{esc(meta["source_url"])}" rel="noopener">📄 Document original</a>')
    if meta.get("source_file"):
        links += (f'<a class="kw-doc-btn kw-doc-btn--private" href="{PRIVATE_SOURCES}{quote(str(meta["source_file"]))}" '
                  f'rel="noopener" title="Fichier conservé dans le dépôt privé veille-agent (accès réservé)">🔒 Original (privé)</a>')
    if links:
        head = head.replace("</div>\n", f'<span class="kw-doc-head__links">{links}</span></div>\n', 1)
    markdown = re.sub(r"^# (?:Analyse\s*—\s*)?(.+)$", lambda m: f"# {m.group(1)}\n\n{head}", markdown, count=1, flags=re.M)
    markdown = fold_section(markdown, "Métadonnées", "info", "Fiche technique du document")
    return fold_section(markdown, "Sources de synthèse", "note", "Sources de synthèse")


# ---------------------------------------------------------------- navigation

NAV_ITEMS = 3


def nav_label(text, n=46):
    text = re.sub(r"\s+", " ", str(text)).strip()
    return text if len(text) <= n else text[:n].rsplit(" ", 1)[0] + " …"


def latest_readings(briefs):
    """[(titre, url)] des reading lists, de la plus récente à la plus ancienne."""
    return [(e.group(2).strip("«» "), e.group(3)) for it in briefs
            for e in (READING_ENTRY.match(l.strip()) for l in section_body(it["body"], "📚 Reading list").splitlines()) if e]


def build_nav(items, themes, threads=None):
    # Fils et semaines : seule leur page d'index figure dans le menu (pages individuelles hors
    # navigation, voir not_in_nav dans mkdocs.yml) pour que la barre latérale reste courte.
    # Chaque outil montre ses trois derniers éléments (fils récents, semaines, prochains jalons,
    # dernières lectures) : le menu reste court quel que soit l'historique.
    today = date.today()
    recent_threads = sorted((threads or {}).items(), key=lambda kv: kv[1][-1]["date"], reverse=True)[:NAV_ITEMS]
    upcoming = [e for e in STATE.get("agenda", []) if e[0] >= today][:NAV_ITEMS]
    weeks = sorted({iso_week(it["date"]): it["date"] for it in items["veille"]}.items(), reverse=True)[:NAV_ITEMS]
    readings = latest_readings(items["veille"])[:NAV_ITEMS]
    veille = ["veille/index.md", {"🔎 Explorer": EXPLORER_SRC},
              {"🧵 Fils d'actualité": [f"{THREADS_DIR}/index.md"]
               + [{nav_label(thread_title(e)): thread_src(ev)} for ev, e in recent_threads]},
              {"🗓️ Semaines": [f"{WEEKS_DIR}/index.md"]
               + [{f"S{d.isocalendar()[1]} · {week_span(d - timedelta(days=d.weekday()))}": f"{WEEKS_DIR}/{w}.md"}
                  for w, d in weeks]},
              {"📅 Agenda": [AGENDA_SRC]
               + [{nav_label(f"{'1er' if w.day == 1 else w.day} {short_month(w)} · {plain(t)}"): f"/{url_of(AGENDA_SRC)}#j-{w.isoformat()}"}
                  for w, t, _ in upcoming]},
              {"📚 Pile de lecture": [READING_SRC] + [{nav_label(title): url} for title, url in readings]}]
    months = {}
    for it in items["veille"]:
        months.setdefault(f"{MOIS[it['date'].month - 1].capitalize()} {it['date'].year}", []).append(
            {f"{it['date'].day:02d} {short_month(it['date'])} — Morning Brief": it["src"]})
    if months:
        veille.append({"🗄️ Archives": [{m: lst} for m, lst in months.items()]})

    analyses = ["analyses/index.md"]
    for key, label in THEMES.items():
        lst = [it for it in items["analysis"] if it["theme"] == key]
        if lst:
            analyses.append({label: [f"analyses/theme-{key}/index.md"]
                             + [{clean_title(it["title"]): it["src"]} for it in lst]})

    dossiers = ["dossiers/index.md"]
    for key, label in THEMES.items():
        lst = [it for it in items["dossier"] if key in it["themes"]]
        if lst:
            dossiers.append({label: [{it["title"]: it["src"]} for it in lst]})

    return [{"📡 Veille": veille}, {"🔎 Analyses": analyses}, {"🗂️ Dossiers": dossiers}]


def library_nav(library):
    """Onglet Bibliothèque : un en-tête par domaine (Cyber, IT), une entrée dépliable (») par catégorie
    avec ses notes, puis le Glossaire."""
    nav = []
    for dom in library:
        nav.append({dom["label"]: [{cat["label"]: [cat["src"]] + [note_nav(n) for n in cat["notes"]]}
                                   if cat["notes"] else {cat["label"]: cat["src"]}
                                   for cat in dom["categories"]]})
    return nav + [{"🔎 Rechercher dans mes notes": LIBRARY_SEARCH_SRC}, {"📖 Glossaire": [GLOSSARY_SRC]}]


def note_nav(note):
    """Note simple : un lien. Note découpée : une entrée dépliable, présentation puis chapitres."""
    if note.get("chapters"):
        return {note["title"]: [note["src"]] + [{c["title"]: c["src"]} for c in note["chapters"]]}
    return {note["title"]: note["src"]}


# ---------------------------------------------------------------- bibliothèque

def load_library(docs_dir, tree):
    """Associe l'arborescence (data/bibliotheque.yml) aux notes présentes dans docs/library/<domaine>/<catégorie>/.
    Chaque note prévue et pas encore importée reçoit une page d'attente générée, pour rester cliquable ;
    la vraie note la remplace dès qu'elle est déposée (reconnue par son titre ou son nom de fichier)."""
    out = []
    for dom in tree or []:
        cats = []
        for cat in dom.get("categories", []):
            base = f"library/{dom['id']}/{cat['id']}"
            folder = docs_dir / base
            real = {}
            found = (sorted(folder.glob("*.md")) + sorted(folder.glob("*/index.md"))) if folder.exists() else []
            for f in found:
                if f.name == "index.md" and f.parent == folder:
                    continue
                body, meta = get_data(f.read_text(encoding="utf-8"))
                h1 = re.search(r"^# (.+)$", body, re.M)
                stem = f.parent.name if f.name == "index.md" else f.stem
                title = str(meta.get("title") or (h1.group(1) if h1 else stem)).strip()
                note = {"title": title, "src": f.relative_to(docs_dir).as_posix(), "imported": True}
                if f.name == "index.md":                    # note découpée : ses chapitres, dans l'ordre
                    note["chapters"] = [{"title": str(get_data(c.read_text(encoding="utf-8"))[1].get("title") or c.stem),
                                         "src": c.relative_to(docs_dir).as_posix()}
                                        for c in sorted(f.parent.glob("*.md")) if c.name != "index.md"]
                real[slug(title)] = note
                real.setdefault(slug(stem), note)
            notes, used = [], set()
            for title in cat.get("notes") or []:
                hit = real.get(slug(title))
                if hit:
                    notes.append(hit)
                    used.add(hit["src"])
                else:
                    notes.append({"title": title, "src": f"{base}/{slug(title)}.md", "imported": False})
            extra = {n["src"]: n for n in real.values() if n["src"] not in used}
            notes += list(extra.values())
            cats.append({"id": cat["id"], "label": cat["label"], "src": f"{base}/index.md", "notes": notes})
        out.append({"id": dom["id"], "label": dom["label"], "categories": cats})
    return out


def pages_library(library):
    out = []
    for dom in library:
        for cat in dom["categories"]:
            done = sum(n["imported"] for n in cat["notes"])
            total = len(cat["notes"])
            body = (f"# {cat['label']}\n\n<span class=\"kw-muted\">Bibliothèque · {dom['label']} · "
                    f"{done}/{total} importée{'s' if done > 1 else ''}</span>\n\n")
            if cat["notes"]:
                body += ('<ul class="kw-notes">' + "".join(
                    f'<li class="{"is-done" if n["imported"] else "is-todo"}">'
                    f'<a href="{href(cat["src"], n["src"])}">{esc(n["title"])}</a></li>' for n in cat["notes"])
                    + "</ul>\n\n<span class=\"kw-muted\">● importée · ○ à importer depuis Obsidian</span>\n")
            else:
                body += '!!! note "Catégorie vide"\n    Aucune note pour l\'instant.\n'
            out.append((cat["src"], body))
            for n in cat["notes"]:
                if not n["imported"]:
                    out.append((n["src"],
                                f"# {n['title']}\n\n<span class=\"kw-muted\">Bibliothèque · {dom['label']} · "
                                f"[{cat['label']}](index.md)</span>\n\n"
                                '!!! note "Pas encore importée"\n'
                                "    Cette note existe dans mes notes Obsidian et sera publiée ici après relecture.\n"))
    return out


def library_card(cat, src, max_notes=8):
    """Carte d'une catégorie, sur le modèle des cartes Ressources : titre, compteur, puis une ligne
    cliquable par note (pastille pleine = importée, vide = à importer)."""
    rows = "".join(
        f'<li><a href="{href(src, n["src"])}"><span>{esc(n["title"])}</span>'
        f'<span class="kw-lib__dot{" is-done" if n["imported"] else ""}"></span></a></li>'
        for n in cat["notes"][:max_notes])
    more = len(cat["notes"]) - max_notes
    if more > 0:
        rows += f'<li class="kw-lib__more"><a href="{href(src, cat["src"])}">+ {more} autre{"s" if more > 1 else ""} →</a></li>'
    if not rows:
        rows = '<li class="kw-lib__empty">Catégorie vide pour l\'instant</li>'
    done, total = sum(n["imported"] for n in cat["notes"]), len(cat["notes"])
    return (f'<div class="kw-card kw-res kw-lib"><a class="kw-res__label" href="{href(src, cat["src"])}">{esc(cat["label"])}</a>'
            f'<span class="kw-card__meta">{total} note{"s" if total > 1 else ""} · {done} importée{"s" if done > 1 else ""}</span>'
            f'<ul class="kw-res__tops kw-lib__notes">{rows}</ul></div>')


def page_library_index(library, themes, glossary_count):
    src = "library/index.md"
    doms = "".join(f"\n## {dom['label']}\n\n<div class=\"kw-dom kw-dom--{dom['id']}\">"
                   + carousel(library_card(c, src) for c in dom["categories"]) + "</div>\n"
                   for dom in library)
    return src, f"""---
hide:
  - toc
---
# 📚 Bibliothèque

Le **savoir de référence** : mes notes de compréhension, reprises d'Obsidian au fil de l'eau, les ressources
et le glossaire. Veille, Analyses et Dossiers racontent ce qui **se passe** ; la Bibliothèque garde ce qui **dure**.

<a class="kw-card kw-card--wide" href="{href(src, LIBRARY_SEARCH_SRC)}"><span class="kw-card__title">🔎 Rechercher dans mes notes</span><span class="kw-card__text">Texte intégral des {sum(n["imported"] for d in library for c in d["categories"] for n in c["notes"])} notes publiées : un mot, une commande, un acteur.</span></a>
{doms}
## 🧭 Ressources

{resources_carousel(themes, src)}

## 📖 Glossaire

<a class="kw-card kw-card--wide" href="{href(src, GLOSSARY_SRC)}"><span class="kw-card__title">{glossary_count} notions de A à Z</span><span class="kw-card__text">Alimenté automatiquement par le « Lexique du jour » des Morning Briefs, complété à la main.</span></a>
"""


LIBRARY_SEARCH_SRC = "library/recherche.md"
LIBRARY_SEARCH_DATA = "search/bibliotheque.json"


def page_library_search(library):
    notes = sum(n["imported"] for d in library for c in d["categories"] for n in c["notes"])
    return LIBRARY_SEARCH_SRC, f"""---
hide:
  - toc
search:
  exclude: true
---
# 🔎 Rechercher dans mes notes

<span class="kw-muted">Texte intégral des {notes} notes publiées. Tous les mots saisis doivent figurer dans la section ;
un mot trouvé dans le titre la fait remonter. La recherche du site (en haut) ne connaît que les titres des notes.</span>

<div class="kw-explorer kw-libsearch" id="kw-libsearch" data-src="{LIBRARY_SEARCH_DATA}">
<div class="kw-explorer__bar">
<input type="search" class="kw-explorer__q" placeholder="Rechercher : kerberoasting, nmap -sV, Lazarus…" aria-label="Rechercher dans les notes" autofocus>
<span class="kw-explorer__count kw-muted"></span>
</div>
<ol class="kw-libsearch__hits"></ol>
<nav class="kw-pager" aria-label="Pages de résultats"></nav>
<noscript>La recherche a besoin de JavaScript ; les notes restent accessibles depuis la Bibliothèque.</noscript>
</div>
"""


def split_search_index(config):
    """Le texte des notes de la Bibliothèque (plusieurs dizaines de Mo) sort de l'index de recherche global,
    que Material recharge à chaque page : il n'y garde que ses titres et intertitres, et le texte intégral
    part dans search/bibliotheque.json, lu seulement par la page « Rechercher dans mes notes »."""
    path = Path(config.site_dir) / "search" / "search_index.json"
    if not path.exists():
        return
    labels = {}
    for dom in STATE.get("library", []):
        for cat in dom["categories"]:
            for n in cat["notes"]:
                if n["imported"]:
                    labels[url_of(n["src"])] = n["title"]
                    for c in n.get("chapters", []):
                        labels[url_of(c["src"])] = f"{n['title']} · {c['title']}"
    data = json.loads(path.read_text(encoding="utf-8"))
    notes, kept, pages = [], [], {}
    for doc in data.get("docs", []):
        page = doc["location"].split("#")[0]
        if page not in labels:
            kept.append(doc)
            continue
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", doc.get("text") or ""))).strip()
        if text:                                          # texte brut : balises de l'index Material retirées
            notes.append([doc["location"], html.unescape(doc["title"]), labels[page], text])
        if "#" not in doc["location"]:                   # une entrée par page : son titre, ses intertitres en texte
            pages[page] = dict(doc, text="")
            kept.append(pages[page])
        elif page in pages and doc["title"]:
            pages[page]["text"] += (" · " if pages[page]["text"] else "") + doc["title"]
    data["docs"] = kept
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (path.parent / "bibliotheque.json").write_text(json.dumps(notes, ensure_ascii=False, separators=(",", ":")),
                                                   encoding="utf-8")


# ---------------------------------------------------------------- glossaire

GLOSSARY_SRC = "library/glossaire.md"
# Accepte « - **Terme** — déf. », « - **Terme :** déf. », « - **Terme** : déf. » (formats vus dans les briefs)
LEXIQUE_ENTRY = re.compile(r"^[-*]\s+\*\*([^*]+?)\s*:?\s*\*\*\s*(?:[—–:-]\s*)?(\S.*)$")


def letter_anchor(term):
    """Ancre de la lettre du glossaire où se trouve le terme (#a, #b… ou #autres)."""
    c = slug(term)[:1]
    return c if c.isalpha() else "autres"


def first_sentence(text):
    """Première phrase = définition générale ; la suite est le contexte propre au brief."""
    m = re.search(r"^(.+?[.!?])(?=\s+[A-ZÀ-ÖØ-Þ«\"(])", text.strip())
    return (m.group(1) if m else text).strip()


def build_glossary(items, manual):
    """Termes des « Lexique du jour » des briefs et des mini-glossaires des analyses
    (« Repères pour comprendre le document »), du plus récent au plus ancien, complétés
    et corrigés par data/glossaire.yml, prioritaire."""
    terms = {}
    sources = sorted(items["veille"] + items["analysis"], key=lambda x: x["date"], reverse=True)
    for it in sources:
        m = re.search(r"^## (?:Lexique du jour|Repères pour comprendre le document)\s*\n(.*?)(?=^## |^\*Lecture|\Z)",
                      it["body"], re.M | re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            e = LEXIQUE_ENTRY.match(line.strip())
            if not e:
                continue
            key = slug(e.group(1)) or e.group(1).casefold()
            definition = e.group(2).strip()
            definition = definition[:1].upper() + definition[1:]
            t = terms.setdefault(key, {"term": e.group(1).strip(), "definition": first_sentence(definition),
                                       "seen": [], "see": None})
            t["seen"].append(it)
    for entry in manual or []:
        name = str(entry.get("terme", "")).strip()
        if not name:
            continue
        t = terms.setdefault(slug(name) or name.casefold(), {"term": name, "definition": "", "seen": [], "see": None})
        t["term"] = name
        if entry.get("definition"):
            t["definition"] = str(entry["definition"]).strip()
        t["see"] = entry.get("voir")
        t["manual"] = True
    return sorted(terms.values(), key=lambda t: slug(t["term"]) or t["term"].casefold())


def seen_label(it):
    """Lien « Vu dans » : la date pour un brief, le titre court pour une analyse."""
    if it["src"].startswith("veille/"):
        return f"{it['date'].day} {short_month(it['date'])}"
    title = clean_title(it["title"])
    return "analyse « " + (title if len(title) <= 40 else title[:40].rsplit(" ", 1)[0] + " … ") + " »"


def page_glossary(glossary):
    src = GLOSSARY_SRC
    by_letter = {}
    for t in glossary:
        first = (slug(t["term"])[:1] or "#").upper()
        by_letter.setdefault(first if first.isalpha() else "#", []).append(t)
    index = " · ".join(f"[{l}](#{l.lower() if l != '#' else 'autres'})" for l in by_letter)
    body = ""
    for letter, lst in by_letter.items():
        anchor = letter.lower() if letter != "#" else "autres"
        body += f"\n## {letter if letter != '#' else 'Autres'} {{ #{anchor} }}\n\n"
        for t in lst:
            extras = []
            if t.get("see"):
                extras.append(f"[Voir la fiche →]({posixpath.relpath(t['see'], 'library')})")
            seen = list({it["src"]: it for it in t["seen"]}.values())[:6]   # du plus récent au plus ancien
            if seen:
                extras.append("Vu dans : " + ", ".join(
                    f"[{seen_label(it)}]({posixpath.relpath(it['src'], 'library')})" for it in seen))
            body += f"**{t['term']}**\n:   {t['definition'] or '<span class=\"kw-muted\">Définition à compléter.</span>'}"
            body += (f"<br><span class=\"kw-muted\">{' · '.join(extras)}</span>" if extras else "") + "\n\n"
    return src, f"""# 📖 Glossaire

Les notions expliquées dans le **Lexique du jour** des Morning Briefs et dans les repères des analyses,
rassemblées automatiquement, complétées par des ajouts manuels (`data/glossaire.yml`). {len(glossary)} termes.
Partout sur le site, un terme souligné en pointillé affiche sa définition au survol ou au toucher.

{index}
{body}"""


def glossary_data(glossary):
    """assets/glossary.json : lu par javascripts/glossary-tooltips.js pour les infobulles."""
    url = url_of(GLOSSARY_SRC)
    def plain(text):                                   # l'infobulle affiche du texte brut
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
        return re.sub(r"\*+|`", "", text).strip()
    data = [{"t": t["term"], "d": plain(t["definition"]), "u": f"{url}#{letter_anchor(t['term'])}"}
            for t in glossary if t["definition"] and len(t["term"]) >= 2]
    return "assets/glossary.json", json.dumps(data, ensure_ascii=False, separators=(",", ":"))


# ---------------------------------------------------------------- flux RSS

FEED_SIZE = 20


def rfc822(d):
    """Date de parution à 7 h (heure de Paris) au format RSS."""
    moment = datetime(d.year, d.month, d.day, 7, 0)
    try:
        from zoneinfo import ZoneInfo
        moment = moment.replace(tzinfo=ZoneInfo("Europe/Paris"))
    except Exception:                                  # pas de base de fuseaux : UTC
        moment = moment.replace(tzinfo=timezone.utc)
    return format_datetime(moment)


def absolute_links(fragment, page_url):
    """Les lecteurs RSS n'ont pas de page de référence : liens et images en adresses absolues."""
    return re.sub(r'(href|src)="(?![a-z]+:|#)([^"]*)"',
                  lambda m: f'{m.group(1)}="{urljoin(page_url, m.group(2))}"', fragment)


def write_feed(path, title, description, entries, config):
    site = config.site_url.rstrip("/") + "/"
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>',
           f"<title>{esc(title)}</title><link>{site}</link><description>{esc(description)}</description>",
           f'<language>fr</language><atom:link href="{site}{path}" rel="self" type="application/rss+xml"/>']
    for it in entries[:FEED_SIZE]:
        link = site + url_of(it["src"])
        body = STATE["html"].get(it["src"], "")
        label = {"analysis": "Analyse", "dossier": "Dossier"}.get(it["kind"])
        name = clean_title(it["title"])
        xml.append(f"<item><title>{esc(f'{label} — {name}' if label else name)}</title><link>{link}</link>"
                   f'<guid isPermaLink="true">{link}</guid><pubDate>{rfc822(it["date"])}</pubDate>'
                   f"<description><![CDATA[{absolute_links(body, link).replace(']]>', ']]&gt;')}]]></description></item>")
    xml.append("</channel></rss>")
    out = Path(config.site_dir) / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(xml), encoding="utf-8")


def write_feeds(config):
    items = STATE.get("items")
    if not items or not config.site_url:
        return
    tagged = [dict(it, kind=kind) for kind in ("veille", "analysis", "dossier") for it in items[kind]]
    everything = sorted(tagged, key=lambda x: x["date"], reverse=True)
    write_feed("feed.xml", "Disruptive Intelligence",
               "Morning Intelligence Brief, analyses et dossiers : Tech · IA · Cyber · Géopolitique.", everything, config)
    write_feed("veille/feed.xml", "Disruptive Intelligence — Morning Intelligence Brief",
               "La veille quotidienne, une édition par jour.", [it for it in everything if it["kind"] == "veille"], config)


# ---------------------------------------------------------------- hooks MkDocs

def on_config(config):
    root = Path(config.config_file_path).parent
    docs_dir = Path(config.docs_dir)
    items = load_content(docs_dir)
    themes = load_yaml(root / "data" / "ressources.yml", [])
    sources = load_yaml(root / "data" / "sources.yml", [])
    STATE["aliases"] = {a.strip(): s["name"] for s in sources for a in s.get("aliases") or []}

    glossary = build_glossary(items, load_yaml(root / "data" / "glossaire.yml", []))
    threads = STATE["threads"] = build_threads(items["veille"])
    STATE["agenda"] = agenda_entries(items["veille"])
    STATE["linked"], STATE["mentions"] = {}, {}         # analyses/dossiers <-> événements de la veille
    for doc in sorted(items["analysis"] + items["dossier"], key=lambda x: x["date"], reverse=True):
        for event in doc["events"]:
            STATE["linked"].setdefault(event, []).append(doc)
    for s in sorted(all_subjects(items["veille"]), key=lambda s: s["date"]):
        if s["event"]:
            STATE["mentions"].setdefault(s["event"], []).append(s)
    library = load_library(docs_dir, load_yaml(root / "data" / "bibliotheque.yml", []))
    STATE["library"] = library

    pages = [page_home(items, themes, glossary), page_veille(items, sources), page_dossiers(items)]
    pages += pages_analyses(items) + pages_ressources(themes) + [page_glossary(glossary)]
    pages += pages_library(library) + [page_library_index(library, themes, len(glossary)), page_library_search(library)]
    pages.append(glossary_data(glossary))
    pages += pages_threads(threads)
    pages += pages_weeks(items["veille"], threads)
    pages += [page_explorer(items["veille"]), explorer_data(items["veille"]),
              page_readings(items["veille"]), page_agenda(items["veille"])]
    STATE["pages"] = pages
    STATE["items"] = items
    STATE["html"] = {}
    STATE["digests"] = {}

    nav = list(config.nav or [])
    pos = next((i + 1 for i, e in enumerate(nav) if isinstance(e, dict) and NAV_ANCHOR in e), 0)
    nav = nav[:pos] + build_nav(items, themes, threads) + nav[pos:]
    for i, e in enumerate(nav):                  # arborescence + Glossaire dans l'onglet Bibliothèque,
        if isinstance(e, dict) and LIBRARY_TAB in e:   # puis l'onglet Ressources juste après
            children = e[LIBRARY_TAB] if isinstance(e[LIBRARY_TAB], list) else [e[LIBRARY_TAB]]
            nav[i] = {LIBRARY_TAB: list(children) + library_nav(library)}
            nav.insert(i + 1, {RESSOURCES_TAB: [RESSOURCES_SRC] + [
                {t["label"]: [f"veille/ressources/{t['id']}/index.md"]
                 + [{r["nom"]: f"veille/ressources/{t['id']}/{slug(r['nom'])}.md"} for r in t["rubriques"]]}
                for t in themes]})
            break
    config.nav = nav
    return config


def on_post_page(output, page, config):
    """Anti-cache : ajoute l'empreinte du fichier aux styles et scripts du site (extra.css?v=…),
    pour que chaque nouvelle version soit rechargée par les navigateurs."""
    digests = STATE.setdefault("digests", {})          # calculées une fois par build, pas à chaque page
    for asset in list(config.extra_css or []) + [str(s) for s in (config.extra_javascript or [])]:
        if asset not in digests:
            path = Path(config.docs_dir) / asset
            digests[asset] = hashlib.sha1(path.read_bytes()).hexdigest()[:10] if path.exists() else None
        if digests[asset]:
            output = output.replace(f'{asset}"', f'{asset}?v={digests[asset]}"')
    return output


def on_page_markdown(markdown, page, config, files):
    """Briefs : sommaire, fils, fraîcheur. Analyses et dossiers : en-tête et métadonnées repliées."""
    src = page.file.src_uri
    if src.startswith("veille/") and re.match(r"veille/\d{4}/\d{2}/", src):
        return decorate_brief(markdown, src)
    if re.fullmatch(r"(analyses|dossiers)/[^/]+\.md", src) and page.meta.get("kind") in ("analysis", "dossier"):
        return decorate_document(markdown, page)
    if src.startswith("library/") and page.meta.get("source"):
        return decorate_note(markdown, page)
    return markdown


def decorate_note(markdown, page):
    """Notes de la Bibliothèque : fil (domaine · catégorie · note) et, pour un chapitre, sa place dans la note."""
    here = page.file.src_uri
    parts = here.split("/")
    dom = next((d for d in STATE.get("library", []) if d["id"] == parts[1]), None)
    cat = next((c for c in dom["categories"] if c["id"] == parts[2]), None) if dom else None

    def rel(src):
        return posixpath.relpath(src, posixpath.dirname(here))

    crumbs = [f"[📚 Bibliothèque]({rel('library/index.md')})"]
    if dom and cat:
        crumbs.append(f"{esc(dom['label'])} · [{esc(cat['label'])}]({rel(cat['src'])})")
    if page.meta.get("chapter"):
        crumbs.append(f"[{esc(page.meta.get('note', ''))}](index.md) · "
                      f"chapitre {page.meta['chapter']}/{page.meta.get('chapters')}")
    return f'<span class="kw-muted">{" · ".join(crumbs)}</span>\n\n' + markdown


def on_page_content(html, page, config, files):
    """Garde le HTML rendu des briefs, analyses et dossiers pour le contenu des flux RSS."""
    if page.file.src_uri.startswith(("veille/", "analyses/", "dossiers/")) and "html" in STATE:
        STATE["html"][page.file.src_uri] = html
    return html


def on_post_build(config):
    """Flux RSS, puis redirections : chaque ancienne adresse Jekyll devient une petite page
    qui renvoie vers la nouvelle."""
    write_feeds(config)
    split_search_index(config)
    redirects = load_yaml(Path(config.config_file_path).parent / "data" / "redirects.yml", {}) or {}
    base = "/" + urlparse(config.site_url or "/").path.strip("/")
    base = base.rstrip("/") + "/"
    for old, new_src in redirects.items():
        target = base + url_of(new_src)
        out = Path(config.site_dir) / old
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Redirection</title>'
            f'<link rel="canonical" href="{esc(target)}"><meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={esc(target)}"></head>'
            f'<body><a href="{esc(target)}">Cette page a déménagé.</a></body></html>', encoding="utf-8")


def on_files(files, config):
    for src_uri, content in STATE.get("pages", []):
        existing = files.get_file_from_path(src_uri)
        if existing:
            files.remove(existing)
        files.append(File.generated(config, src_uri, content=content))
    return files
