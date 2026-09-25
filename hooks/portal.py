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
import html
import posixpath
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

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
GROUP_FALLBACK = [("alertes-cyber", "cyber"), ("geopolitique-ie", "geo-ie"), ("tech", "tech")]

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

NAV_ANCHOR = "🏠 Accueil"   # les onglets générés sont insérés juste après celui-ci
LIBRARY_TAB = "📚 Bibliothèque"   # reçoit les sections Ressources et Glossaire

# ---------------------------------------------------------------- utilitaires


def slug(text):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def fr_date(d):
    return f"{d.day} {MOIS[d.month - 1]} {d.year}"


def short_month(d):
    m = MOIS[d.month - 1]
    return m if len(m) <= 4 else m[:4] + "."


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
                      themes=list(meta.get("themes") or []), author=meta.get("author"), body=body)
            if kind == "veille":
                it["headlines"] = [re.sub(r"\s+", " ", h).strip() for h in re.findall(r"^### ▸ (.+)$", body, re.M)]
            else:
                it["summary"] = summary_of(body)
            items[kind].append(it)
    for lst in items.values():
        lst.sort(key=lambda x: x["date"], reverse=True)
    return items


def load_yaml(path, default):
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else default


# ---------------------------------------------------------------- composants HTML

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
    cited = {}
    for it in briefs:
        sec = None
        for line in it["body"].splitlines():
            if line.startswith("## "):
                sec = section_key(line)
            m = re.match(r"\*\*Sources? :\*\* \[([^\]]+?) — ", line)
            if m and sec:
                c = cited.setdefault(m.group(1).strip(), {})
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
        editions = (f'<div class="kw-editions">{edition_card(briefs[0], src, True)}'
                    f'<div class="kw-carousel">{"".join(edition_card(it, src) for it in briefs[1:])}</div></div>')
    return src, f"""---
hide:
  - toc
---
# 📡 Veille quotidienne

Les éditions du **Morning Intelligence Brief** : les événements retenus, leur contexte et les sources pour approfondir.

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
    return out


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

**Tech · IA · Cyber · Géopolitique** — veille quotidienne, analyses approfondies et base de connaissances technique.

</div>

## À la une

<div class="kw-une">{une}</div>

## 📡 Veille récente

<a class="kw-more-link" href="veille/">Toutes les éditions →</a>

<div class="kw-carousel">{"".join(edition_card(it, src) for it in briefs[1:8])}</div>

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


# ---------------------------------------------------------------- navigation

def build_nav(items, themes):
    veille = ["veille/index.md",
              {"🧭 Ressources": [{t["label"]: [f"veille/ressources/{t['id']}/index.md"]
                                 + [{r["nom"]: f"veille/ressources/{t['id']}/{slug(r['nom'])}.md"} for r in t["rubriques"]]}
                                for t in themes]}]
    months = {}
    for it in items["veille"]:
        months.setdefault(f"{MOIS[it['date'].month - 1].capitalize()} {it['date'].year}", []).append(
            {f"{it['date'].day:02d} {short_month(it['date'])} — Morning Brief": it["src"]})
    if months:
        veille.append({"🗓️ Archives": [{m: lst} for m, lst in months.items()]})

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
    """Onglet Bibliothèque : un en-tête par domaine (Cyber, IT), une entrée par catégorie
    (dépliable quand des notes sont importées), puis le Glossaire."""
    nav = []
    for dom in library:
        cats = []
        for cat in dom["categories"]:
            if cat["imported"]:
                cats.append({cat["label"]: [cat["src"]] + [{n["title"]: n["src"]} for n in cat["imported"]]})
            else:
                cats.append({cat["label"]: cat["src"]})
        nav.append({dom["label"]: cats})
    return nav + [{"📖 Glossaire": [GLOSSARY_SRC]}]


# ---------------------------------------------------------------- bibliothèque

def load_library(docs_dir, tree):
    """Associe l'arborescence (data/bibliotheque.yml) aux notes réellement présentes dans docs/library/."""
    out = []
    for dom in tree or []:
        cats = []
        for cat in dom.get("categories", []):
            folder = docs_dir / "library" / dom["id"] / cat["id"]
            imported = []
            for f in sorted(folder.glob("*.md")) if folder.exists() else []:
                if f.name == "index.md":
                    continue
                body, meta = get_data(f.read_text(encoding="utf-8"))
                h1 = re.search(r"^# (.+)$", body, re.M)
                imported.append({"title": str(meta.get("title") or (h1.group(1) if h1 else f.stem)).strip(),
                                 "src": f.relative_to(docs_dir).as_posix()})
            done = {slug(n["title"]) for n in imported}
            cats.append({"id": cat["id"], "label": cat["label"], "src": f"library/{dom['id']}/{cat['id']}/index.md",
                         "imported": imported, "todo": [n for n in cat.get("notes") or [] if slug(n) not in done]})
        out.append({"id": dom["id"], "label": dom["label"], "categories": cats})
    return out


def pages_library(library):
    out = []
    for dom in library:
        for cat in dom["categories"]:
            body = f"# {cat['label']}\n\n<span class=\"kw-muted\">Bibliothèque · {dom['label']}</span>\n\n"
            if cat["imported"]:
                body += "## Notes\n\n" + "".join(
                    f"- [{n['title']}]({posixpath.relpath(n['src'], posixpath.dirname(cat['src']))})\n"
                    for n in cat["imported"]) + "\n"
            if cat["todo"]:
                body += ("## À importer depuis Obsidian\n\n<ul class=\"kw-todo\">"
                         + "".join(f"<li>{esc(n)}</li>" for n in cat["todo"]) + "</ul>\n")
            if not cat["imported"] and not cat["todo"]:
                body += '!!! note "Catégorie vide"\n    Aucune note pour l\'instant.\n'
            out.append((cat["src"], body))
    return out


def page_library_index(library, themes, glossary_count):
    src = "library/index.md"
    doms = ""
    for dom in library:
        cards = "".join(
            f'<a class="kw-card" href="{href(src, c["src"])}"><span class="kw-card__title">{esc(c["label"])}</span>'
            f'<span class="kw-card__meta">{len(c["imported"])} importée{"s" if len(c["imported"]) > 1 else ""}'
            f' · {len(c["todo"])} à importer</span></a>' for c in dom["categories"])
        doms += f"\n## {dom['label']}\n\n<div class=\"kw-wiki\">{cards}</div>\n"
    return src, f"""---
hide:
  - toc
---
# 📚 Bibliothèque

Le **savoir de référence** : mes notes de compréhension, reprises d'Obsidian au fil de l'eau, les ressources
et le glossaire. Veille, Analyses et Dossiers racontent ce qui **se passe** ; la Bibliothèque garde ce qui **dure**.

## 🧭 Ressources

{resources_carousel(themes, src)}

## 📖 Glossaire

<a class="kw-card kw-card--wide" href="{href(src, GLOSSARY_SRC)}"><span class="kw-card__title">{glossary_count} notions de A à Z</span><span class="kw-card__text">Alimenté automatiquement par le « Lexique du jour » des Morning Briefs, complété à la main.</span></a>
{doms}"""


# ---------------------------------------------------------------- glossaire

GLOSSARY_SRC = "library/glossaire.md"
LEXIQUE_ENTRY = re.compile(r"^- \*\*(.+?)\*\*\s+[—–-]\s+(.+)$")


def letter_anchor(term):
    """Ancre de la lettre du glossaire où se trouve le terme (#a, #b… ou #autres)."""
    c = slug(term)[:1]
    return c if c.isalpha() else "autres"


def first_sentence(text):
    """Première phrase = définition générale ; la suite est le contexte propre au brief."""
    m = re.search(r"^(.+?[.!?])(?=\s+[A-ZÀ-ÖØ-Þ«\"(])", text.strip())
    return (m.group(1) if m else text).strip()


def build_glossary(items, manual):
    """Termes des « Lexique du jour » des briefs (du plus récent au plus ancien), complétés
    et corrigés par data/glossaire.yml, prioritaire."""
    terms = {}
    for it in items["veille"]:                                   # déjà triés du plus récent au plus ancien
        m = re.search(r"^## Lexique du jour\s*\n(.*?)(?=^## |^\*Lecture|\Z)", it["body"], re.M | re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            e = LEXIQUE_ENTRY.match(line.strip())
            if not e:
                continue
            key = slug(e.group(1)) or e.group(1).casefold()
            t = terms.setdefault(key, {"term": e.group(1).strip(), "definition": first_sentence(e.group(2)),
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
            body += f"**{t['term']}**\n:   {t['definition'] or '<span class=\"kw-muted\">Définition à compléter.</span>'}"
            body += (f"<br><span class=\"kw-muted\">{' · '.join(extras)}</span>" if extras else "") + "\n\n"
    return src, f"""# 📖 Glossaire

Les notions expliquées dans le **Lexique du jour** des Morning Briefs, rassemblées automatiquement,
complétées par des ajouts manuels (`data/glossaire.yml`). {len(glossary)} termes.

{index}
{body}"""


# ---------------------------------------------------------------- hooks MkDocs

def on_config(config):
    root = Path(config.config_file_path).parent
    docs_dir = Path(config.docs_dir)
    items = load_content(docs_dir)
    themes = load_yaml(root / "data" / "ressources.yml", [])
    sources = load_yaml(root / "data" / "sources.yml", [])

    glossary = build_glossary(items, load_yaml(root / "data" / "glossaire.yml", []))
    library = load_library(docs_dir, load_yaml(root / "data" / "bibliotheque.yml", []))

    pages = [page_home(items, themes, glossary), page_veille(items, sources), page_dossiers(items)]
    pages += pages_analyses(items) + pages_ressources(themes) + [page_glossary(glossary)]
    pages += pages_library(library) + [page_library_index(library, themes, len(glossary))]
    STATE["pages"] = pages

    nav = list(config.nav or [])
    pos = next((i + 1 for i, e in enumerate(nav) if isinstance(e, dict) and NAV_ANCHOR in e), 0)
    nav = nav[:pos] + build_nav(items, themes) + nav[pos:]
    for i, e in enumerate(nav):                  # Ressources + Glossaire rejoignent l'onglet Bibliothèque
        if isinstance(e, dict) and LIBRARY_TAB in e:
            children = e[LIBRARY_TAB] if isinstance(e[LIBRARY_TAB], list) else [e[LIBRARY_TAB]]
            nav[i] = {LIBRARY_TAB: list(children) + library_nav(library)}
    config.nav = nav
    return config


def on_post_build(config):
    """Redirections : chaque ancienne adresse Jekyll devient une petite page qui renvoie vers la nouvelle."""
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
