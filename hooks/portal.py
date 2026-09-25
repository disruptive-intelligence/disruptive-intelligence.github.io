"""Hook MkDocs : génère le portail Disruptive Intelligence à chaque build.

À partir du contenu (docs/veille, docs/analyses, docs/dossiers) et des données
(data/ressources.yml, data/sources.yml), ce hook génère EN MÉMOIRE :
  - l'accueil (index.md) ;
  - les pages d'index : veille, analyses (+ une page par thème), dossiers ;
  - les pages de ressources (un index par thème + une page par rubrique) ;
  - la navigation des onglets Veille, Analyses et Dossiers.

Rien n'est écrit sur le disque : les pages générées n'existent que dans le site
construit. Pour ajouter du contenu, il suffit de déposer un fichier Markdown
avec son en-tête (title, date, kind, theme, author) au bon endroit.
"""
import html
import posixpath
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml
from mkdocs.structure.files import File
from mkdocs.utils.meta import get_data

# ---------------------------------------------------------------- réglages

THEMES = {  # clé du front matter `theme:` -> libellé
    "ia": "🤖 Intelligence artificielle",
    "cyber": "🛡️ Cyber",
    "tech": "💻 Tech",
    "ie": "📈 Intelligence économique",
    "geo": "🌍 Géopolitique",
}
# Rubriques des briefs -> quadrants de la page Veille
QUADS = [("cyber", "🛡️ Cyber"), ("tech", "💻 Tech"), ("ie", "🌍 Géopolitique & IE"), ("ia", "🚀 IA & rupture")]
GROUP_FALLBACK = [("alertes-cyber", "cyber"), ("geopolitique-ie", "ie"), ("tech", "tech")]

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

NAV_ANCHOR = "🏠 Accueil"   # les onglets générés sont insérés juste après celui-ci

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
        return "ie"
    if "tech" in h:
        return "tech"
    return None


# ---------------------------------------------------------------- lecture du contenu

STATE = {}


def load_content(docs_dir):
    items = {"veille": [], "analysis": [], "dossier": []}
    for folder in ("veille", "analyses", "dossiers"):
        for f in sorted((docs_dir / folder).glob("**/*.md")) if (docs_dir / folder).exists() else []:
            body, meta = get_data(f.read_text(encoding="utf-8"))
            kind = meta.get("kind")
            if kind not in items or not meta.get("date"):
                continue
            d = meta["date"] if isinstance(meta["date"], date) else date.fromisoformat(str(meta["date"]))
            it = dict(src=f.relative_to(docs_dir).as_posix(), title=str(meta.get("title", f.stem)),
                      date=d, theme=meta.get("theme"), author=meta.get("author", "—"), body=body)
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


def analysis_card(it, from_src, with_theme=False):
    """with_theme : auteur · thème (accueil) ; sinon auteur · date (pages déjà classées par thème)."""
    second = THEMES.get(it["theme"], "") if with_theme else fr_date(it["date"])
    return (f'<a class="kw-card" href="{href(from_src, it["src"])}">'
            f'<span class="kw-card__meta">{esc(it["author"])} · {second}</span>'
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
        lst = [it for it in items["dossier"] if it["theme"] == key]
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


def page_home(items, themes):
    src = "index.md"
    briefs, analyses, dossiers = items["veille"], items["analysis"], items["dossier"]
    une = ""
    if briefs:
        une += edition_card(briefs[0], src, True)
    if analyses:
        a = analyses[0]
        une += (f'<a class="kw-card" href="{href(src, a["src"])}"><span class="kw-ed__label">Dernière analyse</span>'
                f'<span class="kw-card__meta">{esc(a["author"])} · {THEMES.get(a["theme"], "")}</span>'
                f'<span class="kw-card__title">{esc(clean_title(a["title"]))}</span>'
                f'<span class="kw-card__text">{esc(a["summary"])}</span></a>')
    if dossiers:
        d = dossiers[0]
        une += (f'<a class="kw-card" href="{href(src, d["src"])}"><span class="kw-ed__label">Dernier dossier</span>'
                f'<span class="kw-card__meta">{THEMES.get(d["theme"], "")} · {fr_date(d["date"])}</span>'
                f'<span class="kw-card__title">{esc(d["title"])}</span>'
                f'<span class="kw-card__text">Croiser les analyses pour mettre les enjeux en perspective.</span></a>')

    res_cards, total = "", 0
    for t in themes:
        rubs = t["rubriques"]
        n = sum(len(r.get("liens") or []) for r in rubs)
        total += n
        top = sorted(((r["nom"], len(r.get("liens") or [])) for r in rubs if r.get("liens")), key=lambda x: -x[1])[:3]
        tops = "".join(f'<li><span>{esc(s)}</span><span class="kw-count">{c}</span></li>' for s, c in top)
        res_cards += (f'<a class="kw-card kw-res" href="{href(src, "veille/ressources/" + t["id"] + "/index.md")}">'
                      f'<span class="kw-res__label">{t["label"]}</span>'
                      f'<span class="kw-card__meta">{n} ressources · {len(rubs)} rubriques</span>'
                      f'<ul class="kw-res__tops">{tops}</ul></a>')

    wiki = [("⚔️ Pentest", "Checklist avant engagement", "Préparer l'environnement, définir les variables, lancer la méthodologie.", "start/checklist.md"),
            ("⚔️ Pentest", "Méthodologie", "Les 7 phases et le tableau port → fiche.", "methodology/index.md"),
            ("⚔️ Pentest", "Services réseau", "Une fiche par service, nommée avec ses ports.", "services/index.md"),
            ("📚 Bibliothèque", "Notes de cours", "Synthèses pour apprendre et réviser.", "library/index.md")]
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

{carousel([res_cards])}

## 📚 Le wiki

<div class="kw-wiki">{wiki_cards}</div>
"""


# ---------------------------------------------------------------- navigation

def build_nav(items, themes):
    veille = ["veille/index.md",
              {"📚 Ressources": [{t["label"]: [f"veille/ressources/{t['id']}/index.md"]
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
        lst = [it for it in items["dossier"] if it["theme"] == key]
        if lst:
            dossiers.append({label: [{it["title"]: it["src"]} for it in lst]})

    return [{"📡 Veille": veille}, {"🔎 Analyses": analyses}, {"🗂️ Dossiers": dossiers}]


# ---------------------------------------------------------------- hooks MkDocs

def on_config(config):
    root = Path(config.config_file_path).parent
    docs_dir = Path(config.docs_dir)
    items = load_content(docs_dir)
    themes = load_yaml(root / "data" / "ressources.yml", [])
    sources = load_yaml(root / "data" / "sources.yml", [])

    pages = [page_home(items, themes), page_veille(items, sources), page_dossiers(items)]
    pages += pages_analyses(items) + pages_ressources(themes)
    STATE["pages"] = pages

    nav = list(config.nav or [])
    pos = next((i + 1 for i, e in enumerate(nav) if isinstance(e, dict) and NAV_ANCHOR in e), 0)
    config.nav = nav[:pos] + build_nav(items, themes) + nav[pos:]
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
