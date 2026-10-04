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
import collections
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


def essentials_of(body, n=3):
    """Les premiers points de « Cinq éléments essentiels à retenir », sans balisage."""
    m = re.search(r"^## Cinq éléments essentiels[^\n]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not m:
        return []
    points = re.findall(r"^\d+\.\s+(.+)$", m.group(1), re.M)
    clean = [re.sub(r"\*\*?|\[[^\]]*\]\s*", "", p).strip() for p in points]
    return [p if len(p) <= 200 else p[:200].rsplit(" ", 1)[0] + " …" for p in clean[:n]]


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
                      kind=kind, events=[str(e) for e in meta.get("events") or []],
                      tags=[str(x) for x in meta.get("tags") or []])
            if kind == "veille":
                it["headlines"] = [re.sub(r"\s+", " ", h).strip() for h in re.findall(r"^### ▸ (.+)$", body, re.M)]
                ess = re.search(r"^!!! abstract \"L'essentiel\"\s*\n\n((?: {4}[-*] .+\n?)+)", body, re.M)
                it["essentiel"] = [l.strip()[2:] for l in ess.group(1).splitlines()] if ess else []
            else:
                it["summary"] = summary_of(body)
                it["organization"] = str(meta.get("organization") or "")
                it["doc_type"] = str(meta.get("document_type") or "")
                it["minutes"] = reading_minutes(body)
                it["essentials"] = essentials_of(body)
                it["cites"] = sorted(set(re.findall(r"analyses/([a-z0-9-]+)\.md", body)))   # dossier -> analyses
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


THEME_LEAD = {
    "ia": "Modèles, agents et course à la frontière : capacités, risques, sécurité et gouvernance de l'IA.",
    "cyber": "Incidents, menaces, renseignement et défense : ce que disent les rapports et la recherche.",
    "tech": "Les technologies qui changent l'équation : semi-conducteurs, quantique, spatial, infrastructures.",
    "geo-ie": "Rapports de force, influence et intelligence économique.",
}


def plural(n, word):
    return f"{n} {word}{'s' if n > 1 else ''}"


def analysis_who(it):
    """L'auteur, sinon l'organisation émettrice, réduite à son sigle quand il est donné entre parenthèses :
    « Agence nationale … (ANSSI) — CERT-FR » -> « ANSSI — CERT-FR »."""
    who = str(it.get("author") or it.get("organization") or "")
    return re.sub(r"^[^()]*\(([^)]+)\)\s*", r"\1 ", who).strip()


# Nature du document analysé (champ facultatif « document_type ») : aide à le lire avec le bon recul.
DOC_TYPES = {
    "rapport": ("Rapport", "Rapports", "Document d'une institution ou d'une entreprise : constats, retours d'expérience, positions."),
    "guide": ("Guide", "Guides", "Recommandations et bonnes pratiques à appliquer."),
    "recherche": ("Article de recherche", "Articles de recherche", "Publié dans une revue ou une conférence."),
    "preprint": ("Prépublication", "Prépublications", "Working paper ou preprint, sans relecture par les pairs annoncée."),
    "essai": ("Essai", "Essais", "Tribune ou essai d'auteur : une thèse argumentée, pas une étude."),
}


def doc_type_label(it):
    t = it.get("doc_type") or ""
    return DOC_TYPES[t][0] if t in DOC_TYPES else t


def type_chips(analyses):
    """Une pastille par nature de document présente ; elle filtre la liste (combinée au filtre texte)."""
    counts = collections.Counter(it.get("doc_type") for it in analyses if it.get("doc_type"))
    if not counts:
        return ""
    return ('<div class="kw-subjects kw-types">' + "".join(
        f'<button type="button" class="kw-chip" data-type="{esc(t)}" title="{esc(DOC_TYPES.get(t, ("", "", ""))[2])}">'
        f'{esc(DOC_TYPES[t][1] if counts[t] > 1 and t in DOC_TYPES else doc_type_label({"doc_type": t}))}'
        f'<span class="kw-count">{counts[t]}</span></button>' for t in DOC_TYPES if counts[t]) + "</div>")


def analysis_item(it, src):
    """Une analyse dans une grille : titre, thèse, auteur · date · durée ; data-search pour le filtre."""
    thesis = it["summary"] if len(it["summary"]) <= 170 else it["summary"][:170].rsplit(" ", 1)[0] + " …"
    search = " ".join([clean_title(it["title"]), it["summary"], analysis_who(it), it.get("organization", ""),
                       THEMES.get(it["theme"], "")] + it["tags"]).lower()
    tag = meta_line(doc_type_label(it), analysis_who(it), f'{it["date"].day} {short_month(it["date"])} {it["date"].year}',
                    f'{it["minutes"]} min')
    return (f'<div class="kw-tuto" data-search="{esc(search)}" data-type="{esc(it.get("doc_type", ""))}">'
            f'<a class="kw-tuto__title" href="{href(src, it["src"])}">{esc(clean_title(it["title"]))}</a>'
            f'<span class="kw-tuto__text">{esc(thesis)}</span><span class="kw-tuto__tag">{tag}</span></div>')


def analysis_chapter(num, key, lst, src, link=True):
    label = THEMES[key]
    title = f"[{esc(label)}]({posixpath.relpath(f'analyses/theme-{key}/index.md', posixpath.dirname(src))})" if link else esc(label)
    minutes = sum(it["minutes"] for it in lst)
    meta = plural(len(lst), "analyse") + (f" · {duration(minutes)} de lecture" if minutes else "")
    head = (f'<header class="kw-chapter__head" markdown>\n<span class="kw-chapter__num">{num:02d}</span>\n\n## {title}\n\n'
            f'<p class="kw-chapter__text">{esc(THEME_LEAD.get(key, ""))}</p>\n<span class="kw-chapter__meta">{meta}</span>\n</header>\n')
    grid = ('<div class="kw-chapter__grid">' + "".join(analysis_item(it, src) for it in lst) + "</div>\n" if lst
            else '<div class="kw-chapter__grid"><span class="kw-muted">Aucune analyse pour l\'instant : le thème est '
                 "suivi dans la veille.</span></div>\n")
    return f'\n<article class="kw-chapter" markdown>\n{head}{grid}</article>\n'


def tag_chips(analyses, limit=12):
    """Les sujets les plus fréquents ; un clic remplit le filtre de la page."""
    counts = collections.Counter(t for it in analyses for t in it["tags"])
    top = [t for t, _ in counts.most_common(limit)]
    return ('<div class="kw-subjects">' + "".join(
        f'<button type="button" class="kw-chip" data-filter="{esc(t.lower())}">{esc(t)}'
        f'<span class="kw-count">{counts[t]}</span></button>' for t in top) + "</div>") if top else ""


def analyses_filter(placeholder):
    return (f'<input class="kw-cs-search kw-an-filter" type="search" placeholder="{esc(placeholder)}" '
            'aria-label="Filtrer les analyses">')


def pages_analyses(items):
    out, src = [], "analyses/index.md"
    analyses = items["analysis"]
    minutes = sum(it["minutes"] for it in analyses)
    used = [k for k in THEMES if any(it["theme"] == k for it in analyses)]
    last = analyses[0] if analyses else None
    # une page par thème
    for key, label in THEMES.items():
        lst = [it for it in analyses if it["theme"] == key]
        if not lst:
            continue
        tsrc = f"analyses/theme-{key}/index.md"
        out.append((tsrc, f"""---
title: "{bare(label)}"
hide:
  - toc
---
<div class="kw-dom-hero kw-dom-hero--cat" markdown>
<span class="kw-eyebrow">[Analyses](../index.md)</span>

# {label}

<p class="kw-dom-lead">{esc(THEME_LEAD.get(key, ""))}</p>
<span class="kw-dom-stats">{plural(len(lst), "analyse")} · {duration(sum(it["minutes"] for it in lst))} de lecture · dernière le {fr_date(lst[0]["date"])}</span>
</div>

{analyses_filter("Filtrer : un mot, un auteur, un sujet…")}
{type_chips(lst)}{tag_chips(lst, 12)}

<div class="kw-chapter__grid kw-chapter__grid--solo kw-an-list">{"".join(analysis_item(it, tsrc) for it in lst)}</div>
"""))
    # accueil des analyses
    nav = " ".join(f'<a href="#{slug(bare(THEMES[k]))}">{esc(bare(THEMES[k]))}</a>' for k in THEMES) + (
        f' <a href="#dossiers">Dossiers</a>' if items["dossier"] else "")
    une = ""
    if last:
        ess = "".join(f"<li>{esc(p)}</li>" for p in last.get("essentials") or [])
        une = (section_bar("À la une")
               + '<div class="kw-une">'
               f'<a class="kw-une__main" href="{href(src, last["src"])}"><span class="kw-tuto__tag">{esc(bare(THEMES.get(last["theme"], "")))} · '
               f'{meta_line(doc_type_label(last), analysis_who(last))} · {last["minutes"]} min</span><span class="kw-une__title">{esc(clean_title(last["title"]))}</span>'
               f'<span class="kw-une__text">{esc(last["summary"])}</span>'
               + (f'<ol class="kw-une__points">{ess}</ol>' if ess else "")
               + f'<span class="kw-une__meta">Analyse du {fr_date(last["date"])} · Lire →</span></a>'
               '<div class="kw-une__side"><span class="kw-une__label">Analyses précédentes</span>'
               + "".join(f'<a class="kw-une__item" href="{href(src, it["src"])}"><span class="kw-une__date">'
                         f'{fr_date(it["date"])} · {esc(bare(THEMES.get(it["theme"], "")))}</span>'
                         f'<span>{esc(clean_title(it["title"]))}</span></a>' for it in analyses[1:5])
               + "</div></div>\n")
    chapters = "".join(analysis_chapter(i, key, [it for it in analyses if it["theme"] == key], src, key in used)
                       for i, key in enumerate(THEMES, 1))
    dossiers = ""
    if items["dossier"]:
        by_slug = {Path(it["src"]).stem: it for it in analyses}
        cards = ""
        for d in items["dossier"]:
            cited = [by_slug[s] for s in d.get("cites", []) if s in by_slug]
            cards += (f'<a class="kw-card kw-dossier" href="{href(src, d["src"])}"><span class="kw-card__meta">'
                      f'{meta_line(themes_label(d), fr_date(d["date"]))}</span><span class="kw-card__title">{esc(d["title"])}</span>'
                      f'<span class="kw-card__text">{esc(d.get("summary") or "Croiser les analyses pour mettre les enjeux en perspective.")}</span>'
                      + (f'<span class="kw-dossier__cites">{plural(len(cited), "analyse")} croisée{"s" if len(cited) > 1 else ""} : '
                         + " · ".join(esc(clean_title(c["title"])) for c in cited) + "</span>" if cited else "")
                      + "</a>")
        dossiers = section_bar("Les dossiers", anchor="dossiers") + (
            '<p class="kw-muted">Un dossier croise plusieurs analyses pour mettre un sujet en perspective.</p>\n'
            f'<div class="kw-libgrid">{cards}</div>\n')
    out.append((src, f"""---
title: Analyses
hide:
  - toc
---
<div class="kw-mast">
<div class="kw-mast__top"><span>{plural(len(analyses), "analyse")} · {duration(minutes)} de lecture</span><span class="kw-mast__count">{"Dernière le " + fr_date(last["date"]) if last else ""}</span></div>
<h1 class="kw-mast__title">🔎 Analyses</h1>
<p class="kw-mast__lead">La lecture critique des rapports, articles et publications qui comptent : la thèse, les arguments, les limites, et ce qu'il faut en retenir pour la veille.</p>
<div class="kw-mast__search">{analyses_filter("Filtrer les analyses : un mot, un auteur, un sujet (DGFiP, AGI, ANSSI…)")}</div>
<nav class="kw-mast__nav">{nav}</nav>
</div>
{une}{section_bar("Explorer")}<p class="kw-an-label">Par nature de document</p>{type_chips(analyses)}<p class="kw-an-label">Par sujet</p>{tag_chips(analyses)}
{section_bar("Par thème")}
<div class="kw-an-list" markdown>
{chapters}
</div>
{dossiers}"""))
    return out


def related_analyses(src, items, limit=3):
    """Analyses proches : le plus de tags en commun, puis le même thème, les plus récentes d'abord."""
    me = next((it for it in items["analysis"] if it["src"] == src), None)
    if not me:
        return [], []
    mine = {t.lower() for t in me["tags"]}
    scored = sorted(((len(mine & {t.lower() for t in it["tags"]}) * 2 + (it["theme"] == me["theme"]), it["date"], it)
                     for it in items["analysis"] if it is not me), key=lambda x: (x[0], x[1]), reverse=True)
    near = [it for score, _, it in scored if score > 0][:limit]
    stem = Path(src).stem
    dossiers = [d for d in items["dossier"] if stem in d.get("cites", [])]
    return near, dossiers


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
        f'<a class="kw-chip" href="{href(src, GLOSSARY_SRC)}#{term_anchor(t["term"])}">{esc(t["term"])}</a>'
        for t in recent)

    wiki = [("📋 Cheat sheets", "Checklist avant engagement", "Préparer l'environnement, définir les variables, lancer la méthodologie.", "start/checklist.md"),
            ("📋 Cheat sheets", "Méthodologie", "Les 7 phases et le tableau port → fiche.", "methodology/index.md"),
            ("📋 Cheat sheets", "Services réseau", "Une fiche par service, nommée avec ses ports.", "services/index.md"),
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

## 📖 Glossaire & notions <span class="kw-muted">· {len(glossary)}</span>

<a class="kw-more-link" href="{href(src, GLOSSARY_SRC)}">Définitions et fiches notions →</a>

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


def library_matches(title, tags, limit=3):
    """Rubriques de la Bibliothèque dont un mot-clé (« mots » de data/bibliotheque.yml) apparaît dans le
    titre ou les mots-clés d'une analyse ou d'un dossier."""
    text = str(title) + " | " + " | ".join(str(x) for x in tags)
    out = []
    for dom in STATE.get("library", []):
        for cat in dom["categories"]:
            words = cat.get("mots") or []
            if words and re.search(r"(?<![\w-])(?:" + "|".join(re.escape(w) for w in words) + r")(?![\w-])", text, re.I):
                out.append(cat)
    return out[:limit]


def decorate_document(markdown, page):
    """Analyse ou dossier : en-tête (nature, thème, auteur, date, temps de lecture) et
    métadonnées internes repliées."""
    meta, kind = page.meta, page.meta.get("kind")
    d = meta.get("date")
    d = d if isinstance(d, date) else date.fromisoformat(str(d))
    if kind == "analysis":
        label = "Analyse · " + THEMES.get(meta.get("theme"), "") + (
            f" · {doc_type_label({'doc_type': str(meta['document_type'])})}" if meta.get("document_type") else "")
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
    rubrics = library_matches(meta.get("title", ""), meta.get("tags") or [])
    if rubrics:
        here = page.file.src_uri
        links_lib = " · ".join(f'<a href="{href(here, c["src"])}">{esc(c["label"])}</a>' for c in rubrics)
        head = head.replace("</div>\n", f'<span class="kw-doc-head__follow">Dans la Bibliothèque : {links_lib}</span></div>\n', 1)
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
    markdown = fold_section(markdown, "Sources de synthèse", "note", "Sources de synthèse")
    if kind == "analysis" and STATE.get("items"):
        here = page.file.src_uri
        near, dossiers = related_analyses(here, STATE["items"])
        if near or dossiers:
            markdown += "\n\n## À lire aussi\n\n"
            if dossiers:
                markdown += "Dans le dossier : " + " · ".join(f"[{esc(d['title'])}]({posixpath.relpath(d['src'], posixpath.dirname(here))})"
                                                       for d in dossiers) + "\n{ .kw-cs-meta }\n\n"
            if near:
                markdown += ('<div class="kw-chapter__grid kw-chapter__grid--solo">'
                             + "".join(analysis_item(it, here) for it in near) + "</div>\n")
    return markdown


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
    avec ses notes, puis la Révision, la recherche et le Glossaire."""
    nav, fiches, fiches_src = [], [], []
    for dom in library:
        cats = []
        for cat in dom["categories"]:
            if cat.get("glossaire"):                  # fiches notions : rangées sous le Glossaire, avec leur page
                fiches += [n for n in cat["notes"] if n["imported"]]
                fiches_src = fiches_src or [cat["src"]]
                continue
            # toujours une section (même vide) : une page index.md isolée deviendrait l'accueil du domaine
            cats.append({cat["label"]: [cat["src"]] + category_nav(cat)})
        nav.append({dom["label"]: [dom_src(dom)] + cats})
    glossary = [GLOSSARY_SRC] + ([{"📌 Fiches notions": fiches_src + [note_nav(n) for n in fiches]}] if fiches else [])
    # Parcours : hors du menu (cartes sur la page d'accueil de la Bibliothèque)
    return nav + revision_nav() + [{"🔎 Rechercher dans mes notes": LIBRARY_SEARCH_SRC}, {"📖 Glossaire & notions": glossary}]


def category_nav(cat):
    """Notes d'une catégorie ; celles d'une sous-rubrique (group) sous une entrée dépliable qui ouvre la page
    de la sous-rubrique (sans page, ouvrir la sous-rubrique ouvrirait sa première note). Une synthèse rangée
    sous son cours (paire) n'a pas d'entrée à elle ; les notes d'autres rubriques (liens) sont rappelées."""
    items = []
    for label, notes in grouped([n for n in cat["notes"] if not n.get("paired")]):
        entries = [note_nav(n) for n in notes]
        if label:
            entries += [link_nav(n) for n in cat["links"].get(label, [])]
        items += [{label: [group_src(cat, label)] + entries}] if label else entries
    return items + [link_nav(n) for n in cat["links"].get(None, [])]


def group_src(cat, label):
    return f"{posixpath.dirname(cat['src'])}/sous-rubriques/{slug(label)}/index.md"


def link_nav(note):
    """Note rangée dans une autre rubrique : lien vers sa page (une page ne figure qu'une fois au menu)."""
    return {nav_title(note): "/" + url_of(note["src"])}


def grouped(notes):
    """[(sous-rubrique ou None, [notes consécutives])], dans l'ordre de data/bibliotheque.yml."""
    out = []
    for n in notes:
        if out and out[-1][0] == n.get("group"):
            out[-1][1].append(n)
        else:
            out.append((n.get("group"), [n]))
    return out


def note_nav(note):
    """Note simple : un lien. Note découpée : une entrée dépliable (présentation, puis parties et chapitres).
    Cours avec synthèse : la synthèse est la première entrée du cours (« En synthèse »)."""
    pair = note.get("pair")
    if note.get("chapters") or pair:
        children = [note["src"]]
        if pair:
            children.append({"En synthèse": [pair["src"]] + [note_nav(c) for c in pair.get("chapters", [])]}
                            if pair.get("chapters") else {"En synthèse": pair["src"]})
        return {nav_title(note): children + [note_nav(c) for c in note.get("chapters", [])]}
    return {nav_title(note): note["src"]}


def nav_title(note):
    """Titre du menu, sans marque de format (voir mark_notes pour la couleur)."""
    return note["title"]


FORMAT_LABEL = {"synthese": "Synthèse", "cours": "Cours", "fiche": "Fiche notion", "aide-memoire": "Aide-mémoire",
                "atelier": "Atelier", "ressources": "Ressources", "revision": "Révision"}


def mark_notes(output, page):
    """Menu latéral : les entrées de notes de la Bibliothèque reçoivent la classe kw-note (gris clair),
    entre la rubrique (blanc) et les chapitres (lavande) : la couleur suit la profondeur, pas le format."""
    notes = STATE.get("note_urls")
    if not notes or "md-nav__link" not in output:
        return output
    here = posixpath.dirname("/" + (page.url or "").rstrip("/") + "/x")

    def tag(m):
        href = m.group(2)
        if href.startswith(("http", "#", "mailto")):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(here, href.split("#")[0])).lstrip("/").rstrip("/") + "/"
        label = html.unescape(re.sub(r"<[^>]+>", "", m.group(4).split(">", 1)[-1])).strip()
        if notes.get(target) != label:                 # une sous-rubrique repliée pointe aussi vers une note
            return m.group(0)
        return m.group(1) + ' kw-note' + m.group(3) + m.group(4) + "</a>"

    return re.sub(r'(<a href="([^"]+)" class="md-nav__link[^"]*)(")(.*?)</a>', tag, output, flags=re.S)


def title_words(title):
    noise = {"htb", "synthese", "fiche", "notions", "version", "complete", "cours", "les", "des", "and",
             "prises", "notes", "aide", "memoire", "travaux", "pratiques"}
    return {w for w in slug(title).split("-") if len(w) > 2 and w not in noise}


def link_formats(library):
    """Dans chaque catégorie, une synthèse renvoie aux cours dont le titre reprend le sien
    (« HTB — Réponse à incidents » -> « Réponse à incident ») ; le cours liste ses synthèses."""
    for dom in library:
        for cat in dom["categories"]:
            courses = [n for n in cat["notes"] if n.get("format") == "cours"]
            for n in cat["notes"]:
                if n.get("format") != "synthese" or not title_words(n["title"]):
                    continue
                words = title_words(n["title"])
                for c in courses:
                    common = words & title_words(c["title"])
                    if common and len(common) / len(words) >= 0.5:
                        n.setdefault("deeper", []).append(c)
                        c.setdefault("digests", []).append(n)


def note_pages(folder, docs_dir):
    """Pages d'une note découpée, dans l'ordre : NN-titre.md, ou NN-titre/ (partie : index.md + chapitres)."""
    out = []
    for f in sorted(folder.iterdir()):
        page = f / "index.md" if f.is_dir() else f
        if not page.is_file() or page.suffix != ".md" or (not f.is_dir() and f.name == "index.md"):
            continue
        entry = {"title": str(get_data(page.read_text(encoding="utf-8"))[1].get("title") or f.stem),
                 "src": page.relative_to(docs_dir).as_posix()}
        if f.is_dir():
            entry["chapters"] = note_pages(f, docs_dir)
        out.append(entry)
    return out


def walk_pages(note, trail=()):
    """(page, libellé « Note · Partie · Chapitre ») de toutes les pages d'une note."""
    label = " · ".join(trail + (note["title"],))
    yield note["src"], label
    for c in note.get("chapters", []):
        yield from walk_pages(c, trail + (note["title"],))


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
                note = {"title": title, "src": f.relative_to(docs_dir).as_posix(), "imported": True,
                        "format": meta.get("format"), "terms": meta.get("terms") or {},
                        "revision": meta.get("revision"), "revue": str(meta.get("revue") or ""),
                        "resume": str(meta.get("resume") or ""), "provenance": str(meta.get("provenance") or ""),
                        "statut": str(meta.get("statut") or "")}
                if f.name == "index.md":                    # note découpée : parties et chapitres, dans l'ordre
                    note["chapters"] = note_pages(f.parent, docs_dir)
                note["minutes"] = reading_time(note, docs_dir)
                real[slug(title)] = note
                real.setdefault(slug(stem), note)
            notes, used = [], set()
            planned = [(t, None) for t in cat.get("notes") or []] + [
                (t, g["label"]) for g in cat.get("groups") or [] for t in g.get("notes") or []]
            for title, group in planned:            # sous-rubrique (group) : menu et page de catégorie
                hit = real.get(slug(title))
                if hit:
                    notes.append(dict(hit, group=group))
                    used.add(hit["src"])
                else:
                    notes.append({"title": title, "src": f"{base}/{slug(title)}.md", "imported": False, "group": group})
            extra = {n["src"]: n for n in real.values() if n["src"] not in used}
            notes += list(extra.values())
            groups = list(dict.fromkeys(n.get("group") for n in notes))   # dans chaque sous-rubrique : cours d'abord
            notes = [n for _, _, _, n in sorted((groups.index(n.get("group")), n.get("format") != "cours", i, n)
                                                for i, n in enumerate(notes))]
            pair_up(notes)
            revision = f"{REVISION_DIR}/{cat['id']}.md"
            cats.append({"id": cat["id"], "label": cat["label"], "src": f"{base}/index.md", "notes": notes,
                         "description": cat.get("description", ""), "debut": cat.get("debut"),
                         "group_desc": {g["label"]: str(g.get("description") or "") for g in cat.get("groups") or []},
                         "glossaire": bool(cat.get("glossaire")), "mots": [str(w) for w in cat.get("mots") or []],
                         "revision": revision if (docs_dir / revision).exists() else None})
        out.append({"id": dom["id"], "label": dom["label"], "categories": cats})
    attach_links(out, tree or [])
    return out


def attach_links(library, tree):
    """« liens » de data/bibliotheque.yml (rubrique ou sous-rubrique) : notes rangées ailleurs, rappelées ici."""
    by_title = {}
    for dom in library:
        for cat in dom["categories"]:
            for n in cat["notes"]:
                if n["imported"]:
                    by_title[n["title"]] = dict(n, home=cat["label"])
    for dom, ydom in zip(library, tree):
        for cat, ycat in zip(dom["categories"], ydom.get("categories", [])):
            links = {None: [by_title[t] for t in ycat.get("liens") or [] if t in by_title]}
            for g in ycat.get("groups") or []:
                links[g["label"]] = [by_title[t] for t in g.get("liens") or [] if t in by_title]
            cat["links"] = links


WORDS_PER_MINUTE = 230


def reading_time(note, docs_dir):
    """Minutes de lecture d'une note (toutes ses pages), d'après le nombre de mots."""
    words = 0
    for src, _ in walk_pages(note):
        path = docs_dir / src
        if path.exists():
            body = get_data(path.read_text(encoding="utf-8"))[0]
            words += len(re.sub(r"```.*?```", " ", body, flags=re.S).split())
    return max(1, round(words / WORDS_PER_MINUTE))


def duration(minutes):
    """« 25 min », « 1 h », « 6 h 30 » (arrondi au quart d'heure au-delà d'une heure)."""
    if not minutes:
        return ""
    if minutes < 55:
        return f"{max(5, round(minutes / 5) * 5)} min"
    q = round(minutes / 15) * 15
    h, m = divmod(q, 60)
    return f"{h} h" + (f" {m:02d}" if m else "")


def pair_up(notes):
    """« APT — synthèse » se range sous le cours de la même rubrique dont le titre commence par « APT »."""
    for s in notes:
        m = re.match(r"^(.+?)\s+[—–-]\s+synth[èe]se$", s["title"], re.I)
        if not (m and s["imported"] and s.get("format") == "synthese"):
            continue
        key = slug(m.group(1))
        course = next((c for c in notes if c is not s and c["imported"] and c.get("format") == "cours"
                       and not c.get("pair") and slug(c["title"]).startswith(key)), None)
        if course:
            course["pair"], s["paired"] = s, course


FORMAT_PLURAL = {"cours": ("cours", "cours"), "synthese": ("synthèse", "synthèses"), "fiche": ("fiche", "fiches"),
                 "aide-memoire": ("aide-mémoire", "aide-mémoire"), "atelier": ("atelier", "ateliers"),
                 "ressources": ("liste de ressources", "listes de ressources"), "revision": ("révision", "révisions")}


def format_counts(notes):
    """« 3 cours · 2 synthèses · 1 aide-mémoire » (notes publiées seulement)."""
    counts = collections.Counter(n.get("format") for n in notes if n["imported"] and n.get("format"))
    return " · ".join(f"{counts[k]} {FORMAT_PLURAL[k][counts[k] > 1]}" for k in FORMAT_PLURAL if counts[k])


def format_pill(note):
    """Étiquette de format dans les listes : seulement pour ce qui n'est ni cours ni synthèse."""
    kind = note.get("format")
    return (f' <span class="kw-format kw-format--{kind}">{FORMAT_LABEL[kind]}</span>'
            if kind in FORMAT_LABEL and kind not in ("cours", "synthese") else "")


def starting_note(cat):
    """Note conseillée pour commencer : « debut » de la catégorie, sinon le premier cours, sinon la première note."""
    notes = [n for n in cat["notes"] if n["imported"]]
    by_title = {n["title"]: n for n in notes}
    return (by_title.get(cat.get("debut") or "") or next((n for n in notes if n.get("format") == "cours"), None)
            or (notes[0] if notes else None))


def note_line(n, src):
    """Ligne d'une note dans une page de rubrique : titre, format et durée en gris, synthèse liée ;
    pour une note rappelée depuis une autre rubrique, sa rubrique d'origine."""
    if not n["imported"]:
        return (f'<li class="is-todo"><a href="{href(src, n["src"])}">{esc(nav_title(n))}</a>'
                '<span class="kw-note-meta">à importer</span></li>')
    bits = [FORMAT_LABEL.get(n.get("format"), "").lower(), duration(n.get("minutes"))]
    meta = " · ".join(b for b in bits if b)
    pair = n.get("pair")
    if pair:
        meta += f' · <a href="{href(src, pair["src"])}">en synthèse</a> ({duration(pair.get("minutes"))})'
    if n.get("home"):
        home = re.sub(r"^\W+", "", n["home"])
        meta += f" · rangée dans {esc(home)}"
    return (f'<li class="is-done"><a href="{href(src, n["src"])}">{esc(nav_title(n))}</a>'
            f'<span class="kw-note-meta">{meta}</span></li>')


def veille_matches(words, limit=5):
    """Analyses et dossiers dont le titre ou les mots-clés citent un des mots (du plus récent au plus ancien)."""
    if not words:
        return []
    rx = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(w) for w in words) + r")(?![\w-])", re.I)
    items = STATE.get("items") or {}
    docs = sorted(items.get("analysis", []) + items.get("dossier", []), key=lambda d: d["date"], reverse=True)
    return [d for d in docs if rx.search(d["title"] + " | " + " | ".join(d.get("tags") or []))][:limit]


def veille_block(cat, src):
    hits = veille_matches(cat.get("mots"))
    if not hits:
        return ""
    lines = "".join(
        f'<li><a href="{href(src, d["src"])}">{esc(clean_title(d["title"]))}</a>'
        f'<span class="kw-note-meta">{"analyse" if d["kind"] == "analysis" else "dossier"} · '
        f'{d["date"].day} {short_month(d["date"])} {d["date"].year}</span></li>' for d in hits)
    return f'\n## Dans la veille\n\n<ul class="kw-notes kw-notes--veille">{lines}</ul>\n'


def page_group(dom, cat, label, notes):
    """Page d'une sous-rubrique : ses notes (celles rappelées d'ailleurs comprises)."""
    src = group_src(cat, label)
    desc = cat["group_desc"].get(label, "")
    body = (f"# {label}\n\n<span class=\"kw-muted\">Bibliothèque · {dom['label']} · "
            f"[{cat['label']}]({posixpath.relpath(cat['src'], posixpath.dirname(src))})</span>\n\n"
            + (f'<p class="kw-dom-lead">{esc(desc)}</p>\n\n' if desc else "")
            + '<div class="kw-chapter__grid kw-chapter__grid--solo">' + "".join(note_item(n, src) for n in notes) + "</div>\n")
    return src, body


DOMAIN_LEAD = {
    "cyber": "Comprendre la menace, enquêter en sources ouvertes, protéger, détecter et répondre — du renseignement "
             "à la gouvernance.",
    "it": "Les systèmes, réseaux, langages et infrastructures sur lesquels tout le reste repose.",
}


def bare(label):
    """Libellé sans son emoji de tête : « 🎯 CTI » -> « CTI »."""
    return re.sub(r"^\W+", "", str(label)).strip()


def dom_src(dom):
    return f"library/{dom['id']}/index.md"


def note_tag(n):
    """« cours · 1 h 30 » (+ « en cours » pour une note en rédaction)."""
    bits = [FORMAT_LABEL.get(n.get("format"), "").lower(), duration(n.get("minutes"))]
    if n.get("statut") == "en cours":
        bits.append("en cours")
    return " · ".join(b for b in bits if b)


def note_item(n, src):
    """Une note dans une grille de chapitre : titre, phrase de résumé, étiquette (format, durée, synthèse liée)."""
    if not n["imported"]:
        return (f'<div class="kw-tuto is-todo"><a class="kw-tuto__title" href="{href(src, n["src"])}">{esc(nav_title(n))}</a>'
                '<span class="kw-tuto__tag">à importer</span></div>')
    tag = note_tag(n)
    pair = n.get("pair")
    if pair:
        tag += f' · <a href="{href(src, pair["src"])}">en synthèse</a>'
    if n.get("home"):
        tag += f" · rangée dans {esc(bare(n['home']))}"
    resume = n.get("resume") or STATE.get("resumes", {}).get(n["title"], "")
    return (f'<div class="kw-tuto"><a class="kw-tuto__title" href="{href(src, n["src"])}">{esc(nav_title(n))}</a>'
            + (f'<span class="kw-tuto__text">{esc(resume)}</span>' if resume else "")
            + f'<span class="kw-tuto__tag">{tag}</span></div>')


def chapter(num, title_md, text, meta, notes, src):
    """Un chapitre : numéro, titre, phrase et compte à gauche ; les notes en grille à droite."""
    head = (f'<header class="kw-chapter__head" markdown>\n<span class="kw-chapter__num">{num:02d}</span>\n\n'
            f"## {title_md}\n\n" + (f'<p class="kw-chapter__text">{esc(text)}</p>\n' if text else "")
            + (f'<span class="kw-chapter__meta">{meta}</span>\n' if meta else "") + "</header>\n")
    grid = '<div class="kw-chapter__grid">' + "".join(note_item(n, src) for n in notes) + "</div>\n"
    return f'\n<article class="kw-chapter" markdown>\n{head}{grid}</article>\n'


def lib_stats(notes):
    """« 10 cours · 2 synthèses · 38 h de lecture »."""
    counts = format_counts(notes)
    minutes = sum(n.get("minutes") or 0 for n in notes if n["imported"])
    return " · ".join(b for b in (counts, f"{duration(minutes)} de lecture" if minutes else "") if b)


def last_update(notes):
    dates = [n.get("revue") for n in notes if n.get("revue")]
    return fr_date(date.fromisoformat(max(dates))) if dates else ""


def page_domain(dom, library):
    """Page d'un domaine (Cyber, IT) : en-tête, sommaire, notes pour commencer, parcours, puis une rubrique par
    chapitre (cours en grille), et pour finir les autres portes d'entrée."""
    src = dom_src(dom)
    cats = [c for c in dom["categories"] if not c.get("glossaire")]
    notes = [n for c in cats for n in c["notes"]]
    stats = lib_stats(notes)
    update = last_update(notes)
    toc = " ".join(f'<a href="#{slug(bare(c["label"]))}">{esc(bare(c["label"]))}</a>' for c in cats)
    starts = [(c, starting_note(c)) for c in cats]
    starts = [(c, n) for c, n in starts if n][:6]
    first = "".join(
        f'<a class="kw-start" href="{href(src, n["src"])}"><span class="kw-start__num">{i:02d}</span>'
        f'<span class="kw-start__body"><span class="kw-start__title">{esc(nav_title(n))}</span>'
        f'<span class="kw-start__text">{esc(n.get("resume") or STATE.get("resumes", {}).get(n["title"], ""))}</span></span>'
        f'<span class="kw-start__cat">{esc(bare(c["label"]))}</span></a>'
        for i, (c, n) in enumerate(starts, 1))
    parcours = [p for p in STATE.get("parcours", []) if p.get("domaine") == dom["id"]]
    body = f"""---
title: "{bare(dom['label'])}"
hide:
  - toc
---
<div class="kw-dom-hero" markdown>
<span class="kw-eyebrow">Bibliothèque</span>

# {dom['label']}

<p class="kw-dom-lead">{esc(DOMAIN_LEAD.get(dom['id'], ''))}</p>
<span class="kw-dom-stats">{stats}{' · mis à jour le ' + update if update else ''}</span>
</div>

<nav class="kw-dom-toc"><span>Sommaire</span>{toc}</nav>

<span class="kw-eyebrow">Pour commencer</span>

## Une note par rubrique

<div class="kw-starts">{first}</div>
"""
    if parcours:
        body += ('\n<span class="kw-eyebrow">Parcours</span>\n\n## Apprendre dans le bon ordre\n\n'
                 + parcours_cards(src, parcours) + "\n")
    body += '\n<span class="kw-eyebrow">La bibliothèque</span>\n\n## Toutes les rubriques\n'
    for i, cat in enumerate(cats, 1):
        listed = [n for n in cat["notes"] if not n.get("paired")]
        body += chapter(i, f"[{esc(cat['label'])}]({posixpath.relpath(cat['src'], posixpath.dirname(src))})",
                        cat.get("description"), lib_stats(cat["notes"]), listed, src)
    others = [d for d in library if d is not dom]
    body += ('\n<span class="kw-eyebrow">Aller plus loin</span>\n\n## Ailleurs sur le site\n\n<div class="kw-libgrid">'
             + "".join(f'<a class="kw-card" href="{href(src, dom_src(d))}"><span class="kw-card__title">{esc(d["label"])}</span>'
                       f'<span class="kw-card__text">{esc(DOMAIN_LEAD.get(d["id"], ""))}</span></a>' for d in others)
             + f'<a class="kw-card" href="{href(src, "cheatsheets/index.md")}"><span class="kw-card__title">📋 Cheat sheets</span>'
               '<span class="kw-card__text">La commande et un exemple qui marche, quand on est sur le poste.</span></a>'
             + f'<a class="kw-card" href="{href(src, GLOSSARY_SRC)}"><span class="kw-card__title">📖 Glossaire & notions</span>'
               '<span class="kw-card__text">Les définitions et les fiches notions, de A à Z.</span></a>'
             + "</div>\n")
    return src, body


def pages_library(library):
    out = [page_domain(dom, library) for dom in library]
    for dom in library:
        for cat in dom["categories"]:
            src = cat["src"]
            update = last_update(cat["notes"])
            stats = lib_stats(cat["notes"])
            body = (f'---\ntitle: "{bare(cat["label"])}"\n---\n<div class="kw-dom-hero kw-dom-hero--cat" markdown>\n'
                    f'<span class="kw-eyebrow">[Bibliothèque · {esc(bare(dom["label"]))}]'
                    f'({posixpath.relpath(dom_src(dom), posixpath.dirname(src))})</span>\n\n# {cat["label"]}\n\n')
            if cat.get("description"):
                body += f'<p class="kw-dom-lead">{esc(cat["description"])}</p>\n'
            body += (f'<span class="kw-dom-stats">{stats}{" · mis à jour le " + update if update else ""}</span>\n'
                     "</div>\n\n")
            listed = [n for n in cat["notes"] if not n.get("paired")]
            if listed:
                groups = grouped(listed)
                for i, (label, notes) in enumerate(groups, 1):
                    notes = notes + cat["links"].get(label, []) if label else notes
                    if label:
                        title = f"[{esc(label)}]({posixpath.relpath(group_src(cat, label), posixpath.dirname(src))})"
                        body += chapter(i, title, cat["group_desc"].get(label, ""), lib_stats(notes), notes, src)
                        out.append(page_group(dom, cat, label, notes))
                    else:
                        body += '<div class="kw-chapter__grid kw-chapter__grid--solo">' + "".join(note_item(n, src) for n in notes) + "</div>\n\n"
            else:
                body += "Pas encore de cours dans cette rubrique.\n\n"
            if cat["links"].get(None):
                body += ("\n## Voir aussi\n\n" + '<div class="kw-chapter__grid kw-chapter__grid--solo">'
                         + "".join(note_item(n, src) for n in cat["links"][None]) + "</div>\n\n")
            if cat.get("revision"):
                body += (f'<a class="kw-more-link kw-more-link--inline" href="{href(src, cat["revision"])}">'
                         "📝 Réviser : questions d'entretien de la rubrique →</a>\n\n")
            body += veille_block(cat, src)
            out.append((src, body))
            for n in cat["notes"]:
                if not n["imported"]:
                    out.append((n["src"],
                                f"# {n['title']}\n\n<span class=\"kw-muted\">Bibliothèque · {dom['label']} · "
                                f"[{cat['label']}](index.md)</span>\n\n"
                                '!!! note "Pas encore importée"\n'
                                "    Cette note existe dans mes notes Obsidian et sera publiée ici après relecture.\n"))
    return out


def library_card(cat, src):
    """Carte de rubrique : titre, phrase de périmètre, formats présents et point de départ."""
    start = starting_note(cat)
    counts = format_counts(cat["notes"])
    return (f'<div class="kw-card kw-libcard"><a class="kw-libcard__title" href="{href(src, cat["src"])}">{esc(cat["label"])}</a>'
            + (f'<span class="kw-card__text">{esc(cat["description"])}</span>' if cat.get("description") else "")
            + (f'<span class="kw-card__meta">{counts}</span>' if counts else "")
            + (f'<a class="kw-libcard__start" href="{href(src, start["src"])}">Commencer par : {esc(start["title"])} →</a>'
               if start else "")
            + "</div>")


WEEKDAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def section_bar(label, anchor=None):
    """Titre de section façon journal : filet de couleur, libellé en capitales, trait jusqu'au bord."""
    ident = f' id="{anchor}"' if anchor else ""
    return f'\n<div class="kw-bar"{ident}><span>{esc(label)}</span></div>\n'


def page_library_index(library, themes, glossary_count):
    """Accueil de la Bibliothèque : bandeau (date, compteurs, recherche, rubriques), note à la une et dernières
    mises à jour, parcours en cartes à étapes, un bloc par domaine avec ses rubriques numérotées, outils."""
    src = "library/index.md"
    all_notes = [n for d in library for c in d["categories"] for n in c["notes"] if n["imported"]]
    hours = round(sum(n.get("minutes") or 0 for n in all_notes) / 60)
    today = date.today()
    cat_of = {n["src"]: c for d in library for c in d["categories"] for n in c["notes"]}
    recent = sorted((n for n in all_notes if n.get("revue")), key=lambda n: (n["revue"], n.get("minutes") or 0), reverse=True)
    resume = lambda n: n.get("resume") or STATE.get("resumes", {}).get(n["title"], "")
    nav = " ".join(f'<a href="{href(src, dom_src(d))}">{esc(bare(d["label"]))}</a>' for d in library) + (
        f' <a href="#parcours">Parcours</a> <a href="{href(src, GLOSSARY_SRC)}">Glossaire</a>'
        + (f' <a href="{href(src, REVISION_INDEX)}">Révision</a>' if STATE.get("revisions") else "")
        + f' <a href="{href(src, "cheatsheets/index.md")}">Cheat sheets</a>')
    masthead = (
        '<div class="kw-mast">'
        f'<div class="kw-mast__top"><span>{WEEKDAYS[today.weekday()].capitalize()} {fr_date(today)}</span>'
        f'<span class="kw-mast__count">{len(all_notes)} notes en ligne · {hours} h de lecture</span></div>'
        '<h1 class="kw-mast__title">📚 Bibliothèque</h1>'
        '<p class="kw-mast__lead">Le savoir de référence : mes cours, synthèses et fiches, repris d\'Obsidian au fil de '
        "l'eau. La veille raconte ce qui <b>se passe</b> ; la Bibliothèque garde ce qui <b>dure</b>.</p>"
        f'<form class="kw-mast__search" action="{href(src, LIBRARY_SEARCH_SRC)}" method="get">'
        '<input type="search" name="mots" placeholder="Chercher dans le texte de toutes les notes : kerberoasting, nmap -sV, Lazarus…" '
        'aria-label="Chercher dans les notes"><button type="submit">Rechercher</button></form>'
        f'<nav class="kw-mast__nav">{nav}</nav></div>')
    une = ""
    if recent:
        f0, rest = recent[0], recent[1:4]
        cat = cat_of.get(f0["src"])
        une = (section_bar("À la une")
               + '<div class="kw-une">'
               f'<a class="kw-une__main" href="{href(src, f0["src"])}"><span class="kw-tuto__tag">{esc(bare(cat["label"])) if cat else ""} · '
               f'{note_tag(f0)}</span><span class="kw-une__title">{esc(nav_title(f0))}</span>'
               f'<span class="kw-une__text">{esc(resume(f0))}</span>'
               f'<span class="kw-une__meta">Mis à jour le {fr_date(date.fromisoformat(f0["revue"]))} · Lire →</span></a>'
               '<div class="kw-une__side"><span class="kw-une__label">Récemment mis à jour</span>'
               + "".join(f'<a class="kw-une__item" href="{href(src, n["src"])}"><span class="kw-une__date">'
                         f'{fr_date(date.fromisoformat(n["revue"]))}</span><span>{esc(nav_title(n))}</span></a>' for n in rest)
               + "</div></div>\n")
    colors = ["#ed4d5a", "#8f9bff", "#e0b12a", "#4fc3a1", "#c77dff", "#5ab0ff"]
    paths = "".join(
        f'<div class="kw-course" style="--kw-course: {colors[i % len(colors)]}">'
        f'<span class="kw-course__tag">Parcours · {len(p["etapes"])} étapes</span>'
        f'<a class="kw-course__title" href="{href(src, p["src"])}">{esc(p["titre"])}</a>'
        f'<span class="kw-course__text">{esc(p["description"])}</span><ol class="kw-course__steps">'
        + "".join(f'<li><a href="{href(src, s["note"]["src"])}">{esc(s["note"]["title"])}</a></li>' for s in p["etapes"][:9])
        + "</ol>"
        + (f'<span class="kw-course__more">+ {len(p["etapes"]) - 9} étape{"s" if len(p["etapes"]) > 10 else ""}</span>'
           if len(p["etapes"]) > 9 else "")
        + f'<a class="kw-course__cta" href="{href(src, p["etapes"][0]["note"]["src"])}">Commencer →</a></div>'
        for i, p in enumerate(p for p in STATE.get("parcours", []) if p["etapes"]))
    doms = ""
    for d in library:
        cats = [c for c in d["categories"] if not c.get("glossaire")]
        notes = [n for c in cats for n in c["notes"]]
        rubs = "".join(
            f'<a class="kw-domblock__rub" href="{href(src, c["src"])}"><span class="kw-domblock__num">{i:02d}</span>'
            f'<span class="kw-domblock__name">{esc(c["label"])}</span>'
            f'<span class="kw-domblock__desc">{esc(c.get("description", ""))}</span>'
            f'<span class="kw-tuto__tag">{format_counts(c["notes"]) or "à venir"}</span></a>'
            for i, c in enumerate(cats, 1))
        doms += (section_bar(bare(d["label"]), anchor=d["id"])
                 + '<div class="kw-domblock"><div class="kw-domblock__intro">'
                 f'<a class="kw-domblock__title" href="{href(src, dom_src(d))}">{esc(d["label"])}</a>'
                 f'<p>{esc(DOMAIN_LEAD.get(d["id"], ""))}</p><span class="kw-dom-stats">{lib_stats(notes)}</span>'
                 f'<a class="kw-domblock__cta" href="{href(src, dom_src(d))}">Explorer {esc(bare(d["label"]))} →</a></div>'
                 f'<div class="kw-domblock__rubs">{rubs}</div></div>\n')
    fiches = [n for d in library for c in d["categories"] if c.get("glossaire") for n in c["notes"] if n["imported"]]
    return src, f"""---
title: Bibliothèque
hide:
  - toc
---
{masthead}
{une}{doms}{section_bar("Apprendre dans le bon ordre", anchor="parcours")}
<div class="kw-courses">{paths}</div>
{section_bar("Les outils")}
<div class="kw-libgrid">
<a class="kw-card" href="{href(src, LIBRARY_SEARCH_SRC)}"><span class="kw-card__title">🔎 Rechercher dans mes notes</span><span class="kw-card__text">Texte intégral des {len(all_notes)} notes publiées : un mot, une commande, un acteur.</span></a>
<a class="kw-card" href="{href(src, GLOSSARY_SRC)}"><span class="kw-card__title">📖 Glossaire & notions</span><span class="kw-card__text">{glossary_count} définitions de A à Z et {len(fiches)} fiches notions pour aller à l'essentiel.</span></a>
{revision_card(src)}
<a class="kw-card" href="{href(src, "cheatsheets/index.md")}"><span class="kw-card__title">📋 Cheat sheets</span><span class="kw-card__text">La commande et un exemple qui marche, quand on est sur le poste.</span></a>
</div>

<span class="kw-muted">Les liens externes sélectionnés (outils, sites, lectures) sont rangés à part, dans l'onglet [🧭 Ressources]({posixpath.relpath(RESSOURCES_SRC, "library")}).</span>
"""


# ---------------------------------------------------------------- parcours

PARCOURS_SRC = "library/parcours/index.md"


def load_parcours(root, library):
    """data/parcours.yml : parcours d'apprentissage, étapes = titres de notes publiées."""
    notes = {n["title"]: n for d in library for c in d["categories"] for n in c["notes"] if n["imported"]}
    out = []
    for p in load_yaml(root / "data" / "parcours.yml", []) or []:
        steps = [dict(s, note=notes[s["note"]]) for s in p.get("etapes") or [] if s.get("note") in notes]
        out.append({"id": p["id"], "titre": p["titre"], "description": p.get("description", ""), "domaine": p.get("domaine"),
                    "src": f"library/parcours/{p['id']}.md", "etapes": steps})
    return out


def parcours_cards(src, parcours=None):
    """Cartes de parcours : titre, phrase, puis les premières étapes numérotées."""
    def steps(p):
        shown = p["etapes"][:4]
        more = len(p["etapes"]) - len(shown)
        return ('<span class="kw-path__steps">' + "".join(
            f'<span class="kw-path__step"><b>{i:02d}</b> {esc(s["note"]["title"])}</span>' for i, s in enumerate(shown, 1))
            + (f'<span class="kw-path__step kw-path__more">+ {more} étapes</span>' if more > 0 else "") + "</span>")
    return ('<div class="kw-libgrid kw-libgrid--paths">' + "".join(
        f'<a class="kw-card kw-path" href="{href(src, p["src"])}"><span class="kw-card__title">{esc(p["titre"])}</span>'
        f'<span class="kw-card__text">{esc(p["description"])}</span>{steps(p)}</a>'
        for p in (STATE.get("parcours", []) if parcours is None else parcours))
        + "</div>")


def pages_parcours():
    out, parcours = [], STATE.get("parcours", [])
    if not parcours:
        return out
    out.append((PARCOURS_SRC, "# 🎓 Parcours\n\nDes chemins de lecture dans la Bibliothèque, du plus accessible au plus "
                "approfondi. Chaque étape renvoie à une note ; à chacun d'aller plus loin dans les cours.\n\n"
                + parcours_cards(PARCOURS_SRC) + "\n"))
    for p in parcours:
        total = sum(s["note"].get("minutes") or 0 for s in p["etapes"])
        steps = "".join(
            f'<li class="kw-steps__item"><span class="kw-steps__num">{i:02d}</span><div class="kw-steps__body">'
            f'<a class="kw-steps__title" href="{href(p["src"], s["note"]["src"])}">{esc(s["note"]["title"])}</a>'
            + (f'<span class="kw-steps__why">{esc(s["pourquoi"])}</span>' if s.get("pourquoi") else "")
            + f'<span class="kw-tuto__tag">{note_tag(s["note"])}</span></div></li>'
            for i, s in enumerate(p["etapes"], 1))
        out.append((p["src"], f"# {p['titre']}\n\n<span class=\"kw-muted\">[🎓 Parcours](index.md)</span>\n\n"
                    f"{esc(p['description'])}\n\n"
                    f'<span class="kw-dom-stats">{len(p["etapes"])} étapes'
                    + (f" · {duration(total)} de lecture en tout" if total else "") + "</span>\n\n"
                    f'<ol class="kw-steps">{steps}</ol>\n'))
    return out


# ---------------------------------------------------------------- cheat sheets

CS_DIR = "cheatsheets"
CS_NEEDS = f"{CS_DIR}/besoins.md"
CS_TAB = "📋 Cheat sheets"
REPRISE = re.compile(r"^!\[\[([^\]#]+)#([^\]]+)\]\]\s*$", re.M)
MD_LINK = re.compile(r"\]\(([^)\s]+)\)")


def cs_pages(docs_dir):
    """{src: (titre, texte, méta)} des pages de l'onglet Cheat sheets."""
    out = {}
    for f in sorted((docs_dir / CS_DIR).rglob("*.md")) if (docs_dir / CS_DIR).exists() else []:
        body, meta = get_data(f.read_text(encoding="utf-8"))
        src = f.relative_to(docs_dir).as_posix()
        h1 = re.search(r"^# (.+)$", body, re.M)
        out[src] = (str(meta.get("title") or (h1.group(1) if h1 else f.stem)), body, meta)
    return out


def cs_entries(body):
    """[(groupe H2, besoin H3)] d'une fiche, hors blocs de code."""
    out, group, fence = [], "", False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        if fence:
            continue
        m = HEADING.match(line)
        if m and len(m.group(1)) == 2:
            group = m.group(2)
        elif m and len(m.group(1)) == 3:
            out.append((group, m.group(2)))
    return out


def cs_trail(src, pages):
    """« Linux › Fondamentaux › Processus et services » d'après les pages d'index des dossiers parents."""
    parts, path = [], posixpath.dirname(src)
    while path and path != CS_DIR:
        idx = f"{path}/index.md"
        if idx in pages and idx != src:
            parts.insert(0, pages[idx][0])
        path = posixpath.dirname(path)
    return parts + ([pages[src][0]] if not src.endswith("/index.md") else [])


def nav_srcs(nav):
    """Pages de la navigation, dans l'ordre du menu."""
    out = []
    for e in nav or []:
        if isinstance(e, str):
            out.append(e)
        elif isinstance(e, dict):
            for v in e.values():
                out += nav_srcs(v) if isinstance(v, list) else ([v] if isinstance(v, str) else [])
    return out


CS_COMMANDS = f"{CS_DIR}/commandes.md"
CS_EQUIV = f"{CS_DIR}/linux-windows.md"
CS_CODE = re.compile(r'^```(\w+)\s+title="(Commande|Exemple|Exemple 2)"\s*$')
CMD_SPLIT = re.compile(r"\|\||\||&&|;|\$\(|`|-exec\s|\bxargs\s")
CMD_NAME = re.compile(r"^[a-z][a-z0-9._-]*$")


def cs_entry_commands(body, known=()):
    """[(groupe, besoin, commandes de la forme neutre, commandes vues seulement dans les exemples)] :
    le premier mot de chaque segment de ligne (sudo écarté), dans les blocs bash « Commande » et
    « Exemple » de chaque besoin. Hors forme neutre, seuls les noms connus (data/commandes.yml) comptent :
    une ligne de configuration dans un exemple ne devient pas une commande."""
    out, group, need, block, fence = [], "", None, None, False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            m = CS_CODE.match(line.strip()) if not fence else None
            block = (m.group(2) if m.group(1) == "bash" else None) if m else None
            fence = not fence
            continue
        if fence:
            if block and need is not None and not line.lstrip().startswith("#"):
                code = re.sub(r"\s#\s.*$", "", line)
                for seg in CMD_SPLIT.split(code):
                    words = [w for w in seg.strip().lstrip("(!").split() if not re.match(r"^\w+=", w)]
                    if words and words[0] == "sudo" and len(words) > 1 and not words[1].startswith("-"):
                        words = words[1:]
                    name = words[0] if words else ""
                    if CMD_NAME.match(name):
                        (out[-1][2] if block == "Commande" else out[-1][3]).append(name)
            continue
        m = HEADING.match(line)
        if m and len(m.group(1)) == 2:
            group, need = m.group(2), None
        elif m and len(m.group(1)) == 3:
            need = m.group(2)
            out.append((group, need, [], []))
    res = []
    for g, n, prim, sec in out:
        prim = list(dict.fromkeys(prim))
        sec = [c for c in dict.fromkeys(sec) if c not in prim and c in known]
        res.append((g, n, prim, sec))
    return res


def cs_command_index(pages, order, known):
    """{commande: {"main": [(besoin, src)], "also": [(besoin, src)]}} sur les fiches de l'onglet,
    dans l'ordre du menu ; les fiches commande (méta « commande ») n'y participent pas."""
    srcs = [s for s in order if s in pages] + [s for s in pages if s not in order]
    index = {}
    for src in srcs:
        if pages[src][2].get("commande"):
            continue
        for _, need, prim, sec in cs_entry_commands(pages[src][1], known):
            for key, names in (("main", prim), ("also", sec)):
                for name in names:
                    index.setdefault(name, {"main": [], "also": []})[key].append((need, src))
    return index


def cs_command_fiches(pages):
    """{commande: src} des fiches commande (méta « commande »)."""
    return {str(m["commande"]): src for src, (_, _, m) in pages.items() if m.get("commande")}


def win_cmds(info, key):
    """Équivalent(s) Windows d'une commande (data/commandes.yml : texte ou liste), en code."""
    v = info.get(key)
    return [f"`{x}`" for x in (v if isinstance(v, list) else [v] if v else [])]


def cs_need_link(need, src, base):
    from markdown.extensions.toc import slugify as toc_slugify
    return f"[{esc(need)}]({posixpath.relpath(src, posixpath.dirname(base))}#{toc_slugify(need, '-')})"


def page_cs_needs(pages, order, known=()):
    """« Que veux-tu faire ? » : tous les besoins de toutes les fiches, avec un filtre (qui trouve aussi
    une commande : chaque besoin porte ses commandes)."""
    known_srcs = [s for s in order if s in pages] + [s for s in pages if s not in order]
    body = ""
    for src in known_srcs:
        title, text, meta = pages[src]
        if meta.get("commande"):
            continue
        lines = []
        if meta.get("besoin"):
            lines.append(f'- [{esc(meta["besoin"])}]({posixpath.relpath(src, CS_DIR)})')
        for g, n, prim, sec in cs_entry_commands(text, known):
            chips = " ".join(f"<code>{esc(c)}</code>" for c in prim)
            lines.append(f"- {cs_need_link(n, src, CS_NEEDS)}"
                         + (f' <span class="kw-note-meta">{esc(g)}</span>' if g else "")
                         + (f' <span class="kw-cs-cmds">{chips}</span>' if chips else "")
                         + (f' <span class="kw-cs-hidden">{esc(" ".join(sec))}</span>' if sec else ""))
        if lines:
            body += f'\n<div class="kw-cs-needgroup" markdown>\n\n## {" › ".join(cs_trail(src, pages))}\n\n' + "\n".join(lines) + "\n\n</div>\n"
    total = body.count("\n- [")
    return CS_NEEDS, f"""---
hide:
  - toc
---
# 🔎 Que veux-tu faire ?

Tous les besoins de toutes les cheat sheets ({total}). Tape un mot ou une commande : `pid`, `hosts`, `port`,
`cron`, `tail`, `ss`… Pour partir d'une commande : [🔤 Par commande](commandes.md).

<input class="kw-cs-search" type="search" placeholder="Filtrer les besoins ou les commandes…" aria-label="Filtrer les besoins" data-scope=".kw-cs-needgroup">
{body}"""


def page_cs_commands(pages, order, data):
    """« Par commande » : chaque commande des fiches, de A à Z — ce qu'elle fait, les besoins où elle sert
    (forme neutre, puis exemples), sa fiche détaillée et son équivalent Windows."""
    index = cs_command_index(pages, order, data)
    fiches = cs_command_fiches(pages)
    here = CS_COMMANDS
    body, letters = "", []
    for name in sorted(index, key=lambda n: n.lower()):
        letter = name[0].upper()
        if letter not in letters:
            letters.append(letter)
            body += f"\n## {letter}\n"
        info = data.get(name) or {}
        uses = index[name]
        head = f"**`{name}`**"
        if info.get("fait"):
            head += f" — {esc(info['fait'])}"
        if name in fiches:
            head += f" · [fiche détaillée]({posixpath.relpath(fiches[name], CS_DIR)})"
        lines = [f"- {cs_need_link(n, s, here)} <span class=\"kw-note-meta\">{esc(pages[s][0])}</span>"
                 for n, s in uses["main"]]
        if uses["also"]:
            lines.append('- <span class="kw-muted">en exemple :</span> '
                         + " · ".join(cs_need_link(n, s, here) for n, s in uses["also"]))
        win = win_cmds(info, "cmd") + win_cmds(info, "powershell")
        if win:
            lines.append(f'- <span class="kw-muted">Windows :</span> {" · ".join(win)}')
        body += (f'\n<div class="kw-cs-cmd" id="cmd-{slug(name)}" markdown>\n\n{head}\n{{ .kw-cs-cmdname }}\n\n'
                 + "\n".join(lines) + "\n\n</div>\n")
    nav = " ".join(f"[{l}](#{l.lower()})" for l in letters)
    return here, f"""---
hide:
  - toc
---
# 🔤 Par commande

Les {len(index)} commandes des cheat sheets, de A à Z : ce qu'elles font, les besoins où elles servent,
leur équivalent Windows. Tape une commande ou un mot : `tail`, `ss`, `journal`… Pour partir d'un besoin :
[🔎 Que veux-tu faire ?](besoins.md).

<input class="kw-cs-search" type="search" placeholder="Filtrer les commandes…" aria-label="Filtrer les commandes" data-scope=".kw-cs-cmd">

{nav}
{{ .kw-cs-letters }}
{body}"""


def page_cs_equivalents(pages, order, data):
    """« Linux ↔ Windows » : pour chaque fiche Linux, ses commandes et leurs équivalents CMD et PowerShell
    (data/commandes.yml)."""
    index = cs_command_index(pages, order, data)
    fiches = cs_command_fiches(pages)
    srcs = [s for s in order if s in pages and s.startswith(f"{CS_DIR}/linux/") and not pages[s][2].get("commande")]
    first = {}
    for name, uses in index.items():
        for _, src in uses["main"] + uses["also"]:
            if src in srcs:
                first.setdefault(name, src)
                break
    body = ""
    for src in srcs:
        names = sorted((n for n, s in first.items()
                        if s == src and ((data.get(n) or {}).get("cmd") or (data.get(n) or {}).get("powershell"))),
                       key=str.lower)
        if not names:
            continue
        rows = []
        for n in names:
            info = data[n]
            linux = f"[`{esc(n)}`]({posixpath.relpath(fiches[n], CS_DIR)})" if n in fiches else f"`{esc(n)}`"
            rows.append(f"| {linux} | {esc(info.get('fait', ''))} | "
                        + " | ".join("<br>".join(win_cmds(info, k)) or "—" for k in ("cmd", "powershell")) + " |")
        body += (f"\n## [{esc(pages[src][0])}]({posixpath.relpath(src, CS_DIR)})\n\n"
                 "| Linux | Ce qu'elle fait | CMD | PowerShell |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
    return CS_EQUIV, f"""---
title: Linux ↔ Windows
---
# 🔁 Linux ↔ Windows

La commande Linux que je connais, et son équivalent sous Windows : en invite de commandes (CMD) et en
PowerShell. Rangé comme les fiches Linux. Les commandes CMD (`ping`, `ipconfig`, `netstat`…) marchent
aussi dans PowerShell ; « — » : pas d'équivalent direct.

!!! tip "Lire ce tableau"
    Les équivalents rendent le même service, pas forcément avec les mêmes options ni la même sortie.
    PowerShell renvoie des objets : on filtre avec `Where-Object` et on choisit les colonnes avec
    `Select-Object`, là où Linux enchaîne `grep`, `cut` et `awk`.
{body}"""


def decorate_command_fiche(markdown, page, config):
    """Fiche commande : les besoins où elle sert et son équivalent Windows, ajoutés à la fin."""
    name = str(page.meta["commande"])
    pages = STATE.get("cs_pages", {})
    data = STATE.get("commands", {})
    uses = STATE.get("cs_index", {}).get(name, {"main": [], "also": []})
    src = page.file.src_uri
    out = ""
    if uses["main"] or uses["also"]:
        out += "\n\n## Où elle sert dans les cheat sheets\n\n" + "\n".join(
            f"- {cs_need_link(n, s, src)} <span class=\"kw-note-meta\">{esc(pages[s][0])}</span>" for n, s in uses["main"])
        if uses["also"]:
            out += "\n- <span class=\"kw-muted\">en exemple :</span> " + " · ".join(cs_need_link(n, s, src) for n, s in uses["also"])
    info = data.get(name) or {}
    win = [(label, win_cmds(info, k)) for k, label in (("cmd", "CMD"), ("powershell", "PowerShell")) if info.get(k)]
    if win:
        out += "\n\n## Sous Windows\n\n" + "\n".join(f"- {label} : {' · '.join(v)}" for label, v in win)
        out += f"\n\nTous les équivalents : [Linux ↔ Windows]({posixpath.relpath(CS_EQUIV, posixpath.dirname(src))})."
    return markdown + out


def expand_reprises(markdown, src, docs_dir):
    """`![[cheatsheets/…/fiche#Besoin]]` sur une ligne seule : l'entrée de la fiche d'origine, reprise
    telle quelle (liens recalculés), avec « Repris de … »."""
    from markdown.extensions.toc import slugify as toc_slugify
    here = posixpath.dirname(src)

    def one(m):
        target = m.group(1).strip()
        target = target if target.endswith(".md") else target + ".md"
        title = m.group(2).strip()
        path = Path(docs_dir) / target
        if not path.exists():
            raise PluginError(f"{src} : reprise introuvable « {m.group(0).strip()} »")
        body, meta = get_data(path.read_text(encoding="utf-8"))
        lines, start, fence = body.split("\n"), None, False
        for i, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                fence = not fence
            h = None if fence else HEADING.match(line)
            if start is None and h and len(h.group(1)) == 3 and h.group(2) == title:
                start = i
            elif start is not None and h and len(h.group(1)) <= 3:
                lines = lines[start:i]
                break
        else:
            lines = lines[start:] if start is not None else None
        if not lines:
            raise PluginError(f"{src} : besoin « {title} » absent de {target}")
        there = posixpath.dirname(target)

        def relink(lk):
            dest = lk.group(1)
            if re.match(r"^[a-z]+:", dest):
                return lk.group(0)
            path_, _, frag = dest.partition("#")
            full = target if not path_ else posixpath.normpath(posixpath.join(there, path_))
            return f"]({posixpath.relpath(full, here)}{'#' + frag if frag else ''})"

        block = MD_LINK.sub(relink, "\n".join(lines).strip())
        head, _, rest = block.partition("\n")
        origin = " › ".join(cs_trail(target, STATE.get("cs_pages", {}))) or str(meta.get("title") or "")
        return (f"{head}\n\nRepris de [{origin}]({posixpath.relpath(target, here)}#{toc_slugify(title, '-')})\n"
                f"{{ .kw-cs-repris }}\n{rest}")

    return REPRISE.sub(one, markdown)


def decorate_cheatsheet(markdown, page, config):
    src = page.file.src_uri
    markdown = expand_reprises(markdown, src, config.docs_dir)
    model = page.meta.get("modele")
    if model:
        path = Path(config.docs_dir) / posixpath.dirname(src) / str(model)
        text = re.sub(r"\A---\n.*?\n---\n", "", path.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"^(#{1,5}) ", r"#\1 ", text, flags=re.M)          # sous le titre de la page
        name = re.sub(r"\.txt$", ".md", str(model))
        markdown += (f'\n\n[Télécharger le modèle ({name})]({model}){{ .md-button .md-button--primary download="{name}" }}\n\n'
                     f"## Aperçu du modèle\n\n{text}")
    return markdown


def cheatsheet_links(pages):
    """Cours de la Bibliothèque -> cheat sheets qui s'y rattachent (méta « cours » des fiches) ;
    au-delà de trois fiches pour un cours, un lien vers leur rubrique commune."""
    by_course = {}
    for src, (title, _, meta) in pages.items():
        for c in meta.get("cours") or []:
            by_course.setdefault(str(c), []).append((title, src))
    out = {}
    for course, sheets in by_course.items():
        if len(sheets) > 3:
            common = posixpath.commonpath([posixpath.dirname(s) for _, s in sheets])
            while f"{common}/index.md" not in pages and "/" in common:
                common = posixpath.dirname(common)
            idx = f"{common}/index.md"
            sheets = [(f"cheat sheets {pages[idx][0]}", idx)] if idx in pages else sheets[:3]
        out[course] = sheets
    return out


# ---------------------------------------------------------------- révision

REVISION_DIR = "library/revision"
REVISION_INDEX = f"{REVISION_DIR}/index.md"


def load_revisions(docs_dir, library):
    """Pages de l'espace Révision écrites par scripts/import_notes.py, dans l'ordre des rubriques."""
    order = [f"{d['id']}/{c['id']}" for d in library for c in d["categories"]]
    out = []
    for f in sorted((docs_dir / REVISION_DIR).glob("*.md")) if (docs_dir / REVISION_DIR).exists() else []:
        if f.name == "index.md":
            continue
        body, meta = get_data(f.read_text(encoding="utf-8"))
        rubric = str(meta.get("revision") or "transverse")
        out.append({"title": str(meta.get("title") or f.stem), "src": f.relative_to(docs_dir).as_posix(),
                    "rubric": rubric, "domain": str(meta.get("domaine") or "") or "Transverse",
                    "questions": len(re.findall(r"\*\*Question\s*:\*\*", body)),
                    "label": re.sub(r"^Révision — ", "", str(meta.get("title") or f.stem))})
    return sorted(out, key=lambda r: order.index(r["rubric"]) if r["rubric"] in order else len(order))


def revision_nav():
    revisions = STATE.get("revisions") or []
    if not revisions:
        return []
    by_domain = {}
    for r in revisions:
        by_domain.setdefault(r["domain"], []).append({r["label"]: r["src"]})
    return [{"📝 Révision": [REVISION_INDEX] + [{d: entries} for d, entries in by_domain.items()]}]


def revision_card(src):
    revisions = STATE.get("revisions") or []
    if not revisions:
        return ""
    total = sum(r["questions"] for r in revisions)
    return (f'<a class="kw-card" href="{href(src, REVISION_INDEX)}"><span class="kw-card__title">📝 Révision</span>'
            f'<span class="kw-card__text">{total} questions d\'entretien et leurs réponses types, '
            f'rangées en {len(revisions)} domaines.</span></a>')


def page_revision_index():
    revisions = STATE.get("revisions") or []
    by_domain = {}
    for r in revisions:
        by_domain.setdefault(r["domain"], []).append(r)
    body = ""
    for domain, lst in by_domain.items():
        body += f"\n## {domain}\n\n" + '<ul class="kw-notes">' + "".join(
            f'<li class="is-done"><a href="{posixpath.relpath(r["src"], REVISION_DIR)}">{esc(r["label"])}</a>'
            f'<span class="kw-note-meta">{r["questions"]} questions</span></li>' for r in lst) + "</ul>\n"
    return REVISION_INDEX, f"""# 📝 Révision

Les questions types d'entretien de mes cours, avec une réponse courte à savoir dire à voix haute.
Elles restent écrites dans les cours (annexe « Questions types d'entretien ») et sont regroupées ici par
domaine ; chaque page renvoie au cours d'origine.
{body}"""


def decorate_revision(markdown, page):
    here = page.file.src_uri
    rel = lambda src: posixpath.relpath(src, posixpath.dirname(here))
    domain = page.meta.get("domaine") or "Transverse"
    head = (f'<span class="kw-muted">[📚 Bibliothèque]({rel("library/index.md")}) · '
            f'[📝 Révision]({rel(REVISION_INDEX)}) · {esc(domain)}</span>')
    rubric = str(page.meta.get("revision") or "")
    cat = next((c for d in STATE.get("library", []) for c in d["categories"]
                if f"{d['id']}/{c['id']}" == rubric), None)
    if cat:
        head += f'<br><span class="kw-muted">Rubrique : [{esc(cat["label"])}]({rel(cat["src"])})</span>'
    return head + "\n\n" + markdown


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
                    labels.update((url_of(src), label) for src, label in walk_pages(n))
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


def term_anchor(term):
    """Ancre propre à chaque terme du glossaire (#g-defense-en-profondeur) : les liens mènent à la définition."""
    return "g-" + (slug(term) or "terme")


def first_sentence(text):
    """Première phrase = définition générale ; la suite est le contexte propre au brief."""
    m = re.search(r"^(.+?[.!?])(?=\s+[A-ZÀ-ÖØ-Þ«\"(])", text.strip())
    return (m.group(1) if m else text).strip()


SOURCE_CONTEXT = re.compile(r"(?i)\b(?:le|du|ce|au) (?:document|rapport|brief)\b|\bles auteurs\b|\bl'auteur\b"
                            r"|\bici\b|\bde l'article\b|\bnotion centrale\b|^c'est\b|\bfuite\b|\bl'attaquant a\b")


def standalone(definition):
    """Définition autonome : sans renvoi de page « (p. 29) », sans « Explication ajoutée », sans les
    propositions qui parlent du document source plutôt que de la notion (« le rapport souligne… »)."""
    text = re.sub(r"\s*\([^()]*\b(?:p\.|pages?|note)\s?\d[^()]*\)", "", definition)
    text = re.sub(r"\s*\(?\*?(?:Explication|Définition) ajoutée\b.*$", "", text, flags=re.S | re.I)
    text = re.sub(r"(?i)^pour (?:l'auteur|les auteurs),\s*", "", text)
    text = re.sub(r",[^,;.]*\bici\b[^,;.]*", "", text)                  # « …, chargé ici d'un audit »
    parts = [p for p in re.split(r"\s*;\s*", text) if p and not SOURCE_CONTEXT.search(p)]
    text = " ; ".join(parts).strip() if parts else text.strip()
    text = re.sub(r"\s*\.(\s*\.)+$", ".", text[:1].upper() + text[1:] if text else text)
    return text if text.endswith((".", "!", "?", "»", ")")) or not text else text + "."


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
            t = terms.setdefault(key, {"term": e.group(1).strip(), "definition": standalone(first_sentence(definition)),
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


def add_fiche_terms(glossary, library):
    """Termes déclarés par les fiches notions de la Bibliothèque (propriété « termes » dans Obsidian) :
    entrée du glossaire créée si besoin (définition de la fiche), avec « Voir la fiche → » ;
    une définition manuelle (data/glossaire.yml) reste prioritaire."""
    by_key = {slug(t["term"]) or t["term"].casefold(): t for t in glossary}
    for dom in library:
        for cat in dom["categories"]:
            for n in cat["notes"]:
                for term, definition in (n.get("terms") or {}).items():
                    t = by_key.setdefault(slug(term) or term.casefold(),
                                          {"term": term, "definition": "", "seen": [], "see": None})
                    if not t.get("manual"):                  # la fiche prime sur la définition d'un brief
                        t["definition"] = str(definition).strip()
                    t["see"] = t.get("see") or n["src"]
    return sorted(by_key.values(), key=lambda t: slug(t["term"]) or t["term"].casefold())


GLOSS_HEADING = re.compile(r"(?i)glossaire")
TABLE_ROW = re.compile(r"^\|\s*\**([^|*]+?)\**\s*\|\s*([^|]+?)\s*\|")
BOLD_LINE = re.compile(r"^(?:[-*]\s+)?\*\*([^*]{2,80}?)\*\*\s*(\([^)]{0,120}\))?\s*(?:[—–:]|\.(?=\s))?\s*(\S.*)$")
SECTION_REF = re.compile(r"\s*(?:\(?\s*§\s*[\d.]+(?:\s*[,;et]+\s*§?\s*[\d.]+)*\s*\)?)\.?\s*$")


def course_terms(library, docs_dir):
    """Termes des glossaires des cours (sections « Glossaire » des pages publiées) :
    {clé: {"term", "definition", "courses": [(titre du cours, page#ancre)]}}, dans l'ordre de la Bibliothèque."""
    from markdown.extensions.toc import slugify as toc_slugify
    found = {}
    for dom in library:
        for cat in dom["categories"]:
            if cat.get("glossaire"):
                continue
            for note in cat["notes"]:
                if not note["imported"]:
                    continue
                for src, _ in walk_pages(note):
                    path = docs_dir / src
                    if not path.exists():
                        continue
                    body, meta = get_data(path.read_text(encoding="utf-8"))
                    lines = body.split("\n")
                    starts = [(0, 0, "")] if GLOSS_HEADING.search(str(meta.get("title") or "")) else []
                    for i, line in enumerate(lines):
                        h = HEADING.match(line)
                        if h and GLOSS_HEADING.search(h.group(2)):
                            text = re.sub(r"[*_`]", "", h.group(2)).strip()
                            starts.append((i + 1, len(h.group(1)), "#" + toc_slugify(text, "-")))
                    for start, level, anchor in starts:
                        for term, definition in glossary_rows(lines[start:], level):
                            entry = found.setdefault(slug(term), {"term": term, "definition": definition, "courses": []})
                            if all(c[0] != note["title"] for c in entry["courses"]):
                                entry["courses"].append((note["title"], f"{src}{anchor}"))
    return found


def glossary_rows(lines, level):
    """(terme, définition) d'une section de glossaire : tableau « Terme | Définition », lignes
    « **Terme** — définition » ou puces « - **Terme** : définition » ; s'arrête au titre suivant."""
    table_ok = None
    for row in lines:
        hh = HEADING.match(row)
        if hh and level and len(hh.group(1)) <= level:
            return
        if row.startswith("|"):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if table_ok is None:                          # en-tête : « Terme | Définition »
                table_ok = len(cells) >= 2 and re.search(r"(?i)définition", cells[1]) is not None
                continue
            if not table_ok or set(cells[0]) <= set("-: ") or len(cells) < 2:
                continue
            term, definition = re.sub(r"[*`]", "", cells[0]).strip(), cells[1]
        else:
            table_ok = None
            m = BOLD_LINE.match(row.strip())
            if not m:
                continue
            term = m.group(1).strip().rstrip(".:").strip()
            definition = ((m.group(2) or "") + " " + m.group(3)).strip()
        definition = SECTION_REF.sub("", definition.strip()).strip()
        if (len(term) < 2 or len(definition) < 12 or re.fullmatch(r"[A-Z]", term)
                or re.search(r"(?i)\bce glossaire\b", definition)):
            continue
        yield term, definition


def add_course_terms(glossary, library, docs_dir):
    """Ajoute au glossaire les définitions des cours ; un terme déjà défini (briefs, analyses, fiches,
    ajouts manuels) garde sa définition et gagne « Dans les cours »."""
    by_key = {slug(t["term"]) or t["term"].casefold(): t for t in glossary}
    for key, entry in course_terms(library, docs_dir).items():
        t = by_key.get(key)
        if t is None:
            t = by_key[key] = {"term": entry["term"], "definition": entry["definition"], "seen": [], "see": None,
                               "course_only": True}
        t["courses"] = entry["courses"]
    return sorted(by_key.values(), key=lambda t: slug(t["term"]) or t["term"].casefold())


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
            courses = t.get("courses") or []
            if courses:
                extras.append("Dans les cours : " + ", ".join(
                    f"[{esc(name)}]({posixpath.relpath(target.split('#')[0], 'library')}"
                    f"{'#' + target.split('#', 1)[1] if '#' in target else ''})" for name, target in courses[:6])
                    + (f" (+{len(courses) - 6})" if len(courses) > 6 else ""))
            body += (f"<span class=\"kw-anchor\" id=\"{term_anchor(t['term'])}\"></span>**{t['term']}**\n:   "
                     f"{t['definition'] or '<span class=\"kw-muted\">Définition à compléter.</span>'}")
            body += (f"<br><span class=\"kw-muted\">{' · '.join(extras)}</span>" if extras else "") + "\n\n"
    fiches = [n for d in STATE.get("library", []) for c in d["categories"] if c.get("glossaire")
              for n in c["notes"] if n["imported"]]
    chips = "".join(f'<a class="kw-chip" href="{href(src, n["src"])}">{esc(n["title"])}</a>' for n in fiches)
    return src, f"""# 📖 Glossaire & notions

Trois niveaux de lecture : la **définition** (ici, et au survol de tout terme souligné en pointillé sur le site),
la **fiche notion** quand une notion mérite l'essentiel en une page, puis les **cours** pour approfondir.
Les définitions viennent du Lexique des Morning Briefs, des repères des analyses, des fiches notions et
des glossaires de mes cours ; « Dans les cours » mène à la définition dans le cours.
{len(glossary)} définitions, {len(fiches)} fiches.

## 📌 Fiches notions

<div class="kw-chips">{chips}</div>

## Définitions de A à Z

{index}
{body}"""


def glossary_data(glossary):
    """assets/glossary.json : lu par javascripts/glossary-tooltips.js pour les infobulles."""
    url = url_of(GLOSSARY_SRC)
    def plain(text):                                   # l'infobulle affiche du texte brut
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
        return re.sub(r"\*+|`", "", text).strip()
    def link(t):                                       # terme d'une fiche notion : l'infobulle y mène
        see = str(t.get("see") or "")
        return url_of(see) if see.startswith("library/") else f"{url}#{term_anchor(t['term'])}"
    # infobulles : briefs, analyses, fiches et ajouts manuels ; les termes venus des seuls glossaires de cours
    # restent sur la page Glossaire (des centaines de mots courants souligneraient tout le site)
    data = [{"t": t["term"], "d": plain(t["definition"]), "u": link(t)}
            for t in glossary if t["definition"] and len(t["term"]) >= 2 and not t.get("course_only")]
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
    STATE["items"] = items
    library = load_library(docs_dir, load_yaml(root / "data" / "bibliotheque.yml", []))
    link_formats(library)
    STATE["library"] = library
    STATE["notes_by_src"] = {n["src"]: n for d in library for c in d["categories"] for n in c["notes"]}
    STATE["note_urls"] = {url_of(src): n["title"] for src, n in STATE["notes_by_src"].items() if n["imported"]}
    STATE["revisions"] = load_revisions(docs_dir, library)
    glossary = add_fiche_terms(glossary, library)
    glossary = add_course_terms(glossary, library, docs_dir)
    STATE["resumes"] = {str(k): str(v) for k, v in (load_yaml(root / "data" / "resumes.yml", {}) or {}).items()}
    STATE["parcours"] = load_parcours(root, library)

    pages = [page_home(items, themes, glossary), page_veille(items, sources), page_dossiers(items)]
    pages += pages_analyses(items) + pages_ressources(themes) + [page_glossary(glossary)]
    pages += pages_library(library) + [page_library_index(library, themes, len(glossary)), page_library_search(library)]
    pages += pages_parcours()
    STATE["cs_pages"] = cs_pages(docs_dir)
    STATE["cs_links"] = cheatsheet_links(STATE["cs_pages"])
    cs_tab = next((e[CS_TAB] for e in (config.nav or []) if isinstance(e, dict) and CS_TAB in e), [])
    commands = load_yaml(root / "data" / "commandes.yml", {}) or {}
    STATE["commands"] = commands
    cs_order = nav_srcs(cs_tab)
    STATE["cs_index"] = cs_command_index(STATE["cs_pages"], cs_order, commands)
    pages += [page_cs_needs(STATE["cs_pages"], cs_order, commands),
              page_cs_commands(STATE["cs_pages"], cs_order, commands),
              page_cs_equivalents(STATE["cs_pages"], cs_order, commands)]
    if STATE["revisions"]:
        pages.append(page_revision_index())
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
    return mark_notes(output, page)


def on_page_markdown(markdown, page, config, files):
    """Briefs : sommaire, fils, fraîcheur. Analyses et dossiers : en-tête et métadonnées repliées."""
    src = page.file.src_uri
    if src.startswith("veille/") and re.match(r"veille/\d{4}/\d{2}/", src):
        return decorate_brief(markdown, src)
    if re.fullmatch(r"(analyses|dossiers)/[^/]+\.md", src) and page.meta.get("kind") in ("analysis", "dossier"):
        return decorate_document(markdown, page)
    if src.startswith("library/") and page.meta.get("source"):
        return decorate_note(markdown, page)
    if src.startswith(CS_DIR + "/"):
        if page.meta.get("commande"):
            markdown = decorate_command_fiche(markdown, page, config)
        return decorate_cheatsheet(markdown, page, config)
    if src.startswith(REVISION_DIR + "/") and page.meta.get("revision"):
        return decorate_revision(markdown, page)
    return markdown


def decorate_note(markdown, page):
    """Notes de la Bibliothèque : fil (domaine · catégorie · note · partie), d'après l'en-tête « up »
    écrit par scripts/import_notes.py (liens relatifs à la page) ; en page d'entrée, une ligne
    format · provenance · mise à jour · liens cours/synthèse, puis niveau / objectif / prérequis s'ils existent."""
    here = page.file.src_uri
    parts = here.split("/")
    dom = next((d for d in STATE.get("library", []) if d["id"] == parts[1]), None)
    cat = next((c for c in dom["categories"] if c["id"] == parts[2]), None) if dom else None

    def rel(src):
        return posixpath.relpath(src, posixpath.dirname(here))

    crumbs = [f"[📚 Bibliothèque]({rel('library/index.md')})"]
    if cat and cat.get("glossaire"):
        crumbs.append(f"[📖 Glossaire & notions]({rel(GLOSSARY_SRC)})")
    elif dom and cat:
        crumbs.append(f"{esc(dom['label'])} · [{esc(cat['label'])}]({rel(cat['src'])})")
    for label, path in page.meta.get("up") or []:
        crumbs.append(f"[{esc(label)}]({path})")
    head = f'<span class="kw-muted">{" · ".join(crumbs)}</span>'
    note = STATE.get("notes_by_src", {}).get(here)    # page d'entrée d'une note
    if note:
        meta = page.meta
        links = lambda notes: " · ".join(f"[{esc(n['title'])}]({rel(n['src'])})" for n in notes)
        kind = note.get("format")
        bits = [f'<span class="kw-format kw-format--{kind}">{FORMAT_LABEL[kind]}</span>'] if kind in FORMAT_LABEL else []
        if meta.get("provenance"):
            bits.append(f'<span class="kw-format kw-format--source">{esc(meta["provenance"])}</span>')
        if meta.get("statut") == "en cours":
            bits.append('<span class="kw-format kw-format--wip">✍️ en cours de rédaction</span>')
        line = " ".join(bits)
        if meta.get("revue"):
            line += f" mis à jour le {fr_date(date.fromisoformat(str(meta['revue'])))}"
        if note.get("minutes") and kind != "fiche":
            line += f" · {duration(note['minutes'])} de lecture"
        if note.get("pair"):
            line += f" · en synthèse : {links([note['pair']])} ({duration(note['pair'].get('minutes'))})"
        elif note.get("paired"):
            line += f" · synthèse du cours {links([note['paired']])} ({duration(note['paired'].get('minutes'))})"
        elif note.get("deeper"):
            line += f" · pour approfondir : {links(note['deeper'])}"
        elif note.get("digests"):
            line += f" · en synthèse : {links(note['digests'])}"
        elif note.get("terms"):
            line += " · " + ", ".join(esc(t) for t in note["terms"])
        if meta.get("revision"):
            line += f" · [📝 questions de révision]({rel(str(meta['revision']))})"
        memo = STATE.get("cs_links", {}).get(here)
        if memo:
            line += " · 📋 mémo terrain : " + ", ".join(f"[{esc(t)}]({rel(s)})" for t, s in memo)
        head += f'<br><span class="kw-muted">{line}</span>'
        about = [f"**{label} :** {esc(meta[key])}" for key, label in
                 (("niveau", "Niveau"), ("objectif", "Objectif"), ("prerequis", "Prérequis")) if meta.get(key)]
        if about:
            head += '<br><span class="kw-muted">' + " · ".join(about) + "</span>"
    return head + "\n\n" + markdown


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
