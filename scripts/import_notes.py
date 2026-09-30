"""Importe les notes Obsidian (CyberSec-notes) dans la Bibliothèque du portail.

    python scripts/import_notes.py --vault ../CyberSec-notes --list      # correspondances, sans rien écrire
    python scripts/import_notes.py --vault ../CyberSec-notes --all       # publie / met à jour toutes les notes
    python scripts/import_notes.py --vault ../CyberSec-notes Cyber/01_CTI/CTI.md [autres notes…]
    python scripts/import_notes.py --vault ../CyberSec-notes IT/Culture/SQL.md --title "SQL" --to it/culture

--all est la commande de routine (« publie mes notes ») : chaque note du coffre rangée dans une rubrique
est (ré)importée, les pages dont la note source a disparu du coffre sont supprimées.
Pour chaque note :
  - rubrique déduite du dossier du coffre (Cyber/01_CTI -> cyber/cti…), ou --to dom/cat ;
  - titre = la note prévue dans data/bibliotheque.yml la plus proche du nom de fichier, ou --title ;
  - syntaxe Obsidian convertie hors du code : [[Note]] et [[#Titre]] -> vrais liens, ![[image]] et images
    locales -> copiées dans docs/library/assets/, liens locaux introuvables -> texte ;
  - titres : le titre de tête laisse la place au titre de la page, les autres « # » descendent d'un niveau ;
  - note de plus de SPLIT_AT caractères -> dossier <slug>/ : index.md (présentation + sommaire)
    et une page par partie ou chapitre ; les liens d'ancre suivent le chapitre où le titre a atterri ;
  - dépôt public : les IP de lab HackTheBox sont masquées (10.10.x.y -> 10.0.x.y, 10.129.x.y -> 10.1.x.y),
    un flag de CTF, une clé privée ou un vrai jeton empêchent l'import, puis gitleaks (s'il est installé)
    contrôle les pages écrites avec la configuration du dépôt ; au moindre constat la note est retirée.
Rien n'est commité : relire (mkdocs serve), puis committer les fichiers nommés.
"""
import argparse
import difflib
import json
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import unquote

import yaml
from markdown.extensions.toc import slugify as toc_slugify, unique as toc_unique

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LIBRARY = DOCS / "library"
ASSETS = "library/assets"
# Dossiers du coffre -> (domaine, catégorie) de data/bibliotheque.yml
FOLDERS = {
    "Cyber/01_CTI": ("cyber", "cti"), "Cyber/02_OSINT": ("cyber", "osint"),
    "Cyber/03_Cryptographie": ("cyber", "cryptographie"), "Cyber/03_Forensic": ("cyber", "forensic"),
    "Cyber/04_Hardening": ("cyber", "hardening"), "Cyber/05_Cyberdefense": ("cyber", "cyberdefense"),
    "Cyber/10_Tools": ("cyber", "outils"), "Cyber/99_Concepts": ("cyber", "concepts"), "Cyber": ("cyber", "transverse"),
    "IT/01_Linux": ("it", "linux"), "IT/02_Windows": ("it", "windows"), "IT/03_Networking": ("it", "reseau"),
    "IT/04_Active-Directory": ("it", "active-directory"), "IT/05_Scripting_Langage-Prog": ("it", "scripting"),
    "IT/10_virtualization-containers": ("it", "conteneurs"), "IT/Culture": ("it", "culture"), "IT": ("it", "transverse"),
}
# Noms de fichier trop éloignés du titre prévu : correspondance explicite (chemin relatif au coffre).
TITLES = {
    "Cyber/01_CTI/APT_vFULL.md": "APT — version complète",
    "Cyber/01_CTI/CTI_Work.md": "CTI — travaux pratiques",
    "Cyber/01_CTI/IE.md": "Intelligence économique",
    "Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md": "Cours MCS",
    "Cyber/05_Cyberdefense/HTB_Réponse à incidents.md": "HTB — Réponse à incidents",
    "IT/02_Windows/Fiche_Windows.md": "Fiche Windows",
    "IT/02_Windows/CS_CMD.md": "CMD — cheat sheet",
    "IT/03_Networking/networking_notion.md": "Notions réseau",
    "IT/Culture/Fiche_WebApp.md": "Applications web",
}
SKIP = {"README.md"}
# Ce qui ne doit jamais atteindre le dépôt public : la note est refusée.
BLOCKING = [
    ("flag de CTF", re.compile(r"(?i)\b(?:HTB|THM|flag)\{[^}\s]{4,}\}")),
    ("clé privée", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("jeton ou clé d'API", re.compile(r"\b(?:ghp_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})\b")),
]
# Adresses des machines et du VPN HackTheBox : masquées (le reste de l'adresse garde l'exemple lisible).
LAB_IP = re.compile(r"\b10\.(10|129)\.(\d{1,3}\.\d{1,3})\b")
LAB_IP_TO = {"10": "10.0", "129": "10.1"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
SPLIT_AT = 150_000     # caractères : au-delà, la note est découpée en pages
MIN_SECTION = 2_000    # section plus courte (intertitre, « Fin du cours ») : rattachée à la précédente
MAX_PAGE = 160_000     # partie plus longue : redécoupée en ses chapitres
TOC_TITLE = re.compile(r"(?i)^(table des mati[eè]res|sommaire|table of contents)\b")
PART_TITLE = re.compile(r"(?i)^(partie|part|volume|livre)\b")
LINK_MARK = "@@"       # lien interne provisoire « @@library/…/page.md#ancre », rendu relatif page par page


def slug(text):
    text = str(text).translate(str.maketrans({"œ": "oe", "Œ": "OE", "æ": "ae", "Æ": "AE"}))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def category_of(rel):
    parts = rel.parent.as_posix()
    while parts:
        if parts in FOLDERS:
            return FOLDERS[parts]
        parts = parts.rsplit("/", 1)[0] if "/" in parts else ""
    return None


def planned(tree, dom, cat):
    for d in tree:
        if d["id"] == dom:
            for c in d.get("categories", []):
                if c["id"] == cat:
                    return c.get("notes") or []
    raise ValueError(f"catégorie inconnue dans data/bibliotheque.yml : {dom}/{cat}")


def guess_title(path, candidates):
    """Note prévue la plus proche du nom de fichier (dates, « vFULL », « ADD_ » ignorés)."""
    stem = re.sub(r"^\d{8}_|_?vFULL$|^ADD_|^Fiche_", "", path.stem)
    stem = slug(stem.replace("_", " "))
    scored = sorted(((difflib.SequenceMatcher(None, stem, slug(c)).ratio(), c) for c in candidates), reverse=True)
    return scored[0] if scored else (0, None)


def vault_notes(vault):
    """Notes du coffre rangées dans un dossier (les fichiers de la racine et README sont ignorés)."""
    return sorted(p for p in vault.rglob("*.md")
                  if ".obsidian" not in p.parts and ".git" not in p.parts and p.parent != vault and p.name not in SKIP)


def resolve(vault, rel, tree, title=None, to=None):
    """(domaine, catégorie, titre) d'une note du coffre ; ValueError si la rubrique ou le titre manquent."""
    dom, cat = to.split("/") if to else (category_of(Path(rel)) or (None, None))
    if not dom:
        raise ValueError(f"{rel} : rubrique inconnue, préciser --to domaine/catégorie")
    title = title or TITLES.get(Path(rel).as_posix())
    if not title:
        score, title = guess_title(vault / rel, planned(tree, dom, cat))
        if not title or score < 0.45:
            raise ValueError(f"{rel} : aucune note prévue ne correspond dans {dom}/{cat} "
                             f"(meilleur score {score:.2f}), préciser --title")
    return dom, cat, title


def read_note(path):
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)              # en-tête Obsidian éventuel


def is_split(text):
    return len(text) > SPLIT_AT


def note_target(dom, cat, title, split):
    """Page d'entrée d'une note publiée, relative à docs/."""
    base = f"library/{dom}/{cat}/{slug(title)}"
    return f"{base}/index.md" if split else f"{base}.md"


# ------------------------------------------------------------------ code protégé

class Shield:
    """Remplace blocs de code et code en ligne par des jetons : aucune conversion ne touche au code
    (les tests Bash « [[ -z $x ]] » ne sont pas des liens Obsidian)."""
    def __init__(self):
        self.saved = []

    def _keep(self, chunk):
        self.saved.append(chunk)
        return f"\x00{len(self.saved) - 1}\x00"

    def hide(self, text):
        out, block, fence = [], [], None
        for line in text.split("\n"):
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if fence is None and m:
                fence, block = m.group(1), [line]
            elif fence is not None:
                block.append(line)
                if line.strip().startswith(fence) and not line.strip()[len(fence):].strip():
                    out.append(self._keep("\n".join(block)))
                    fence = None
            else:
                out.append(re.sub(r"(`+)(?!`)(.+?)(?<!`)\1(?!`)", lambda m: self._keep(m.group(0)), line))
        if fence is not None:                               # bloc jamais refermé : laissé tel quel
            out.append(self._keep("\n".join(block)))
        return "\n".join(out)

    def show(self, text):
        for _ in range(3):                                   # jetons imbriqués (code dans un bloc gardé)
            if "\x00" not in text:
                break
            text = re.sub(r"\x00(\d+)\x00", lambda m: self.saved[int(m.group(1))], text)
        return text

    def plain(self, text):
        """Texte d'un titre pour les ancres : code rendu sans ses accents graves."""
        return re.sub(r"\x00(\d+)\x00", lambda m: self.saved[int(m.group(1))].strip("`"), text)


# ------------------------------------------------------------------ conversion

class Converter:
    def __init__(self, vault, tree, index=None):
        self.vault, self.tree = vault, tree
        self.index = index if index is not None else build_index(vault, tree)
        self.images = []                                    # (source, nom dans library/assets)

    def find(self, name):
        name = unquote(name).strip()
        hits = [p for p in self.vault.rglob(Path(name).name) if ".obsidian" not in p.parts and ".git" not in p.parts]
        return hits[0] if hits else None

    def asset(self, source, found):
        name = f"{slug(source.stem)}-{slug(found.stem)}{found.suffix.lower()}"
        self.images.append((found, name))
        return f"{LINK_MARK}{ASSETS}/{name}"

    def note_link(self, name):
        """Page publiée d'une note du coffre nommée dans un lien, ou None."""
        key = slug(Path(unquote(name).strip()).stem)
        return self.index.get(key)

    def convert(self, text, source, shield):
        def embed(m):
            target = m.group(1).split("|")[0].strip()
            found = self.find(target) if Path(target).suffix.lower() in IMAGE_EXT else None
            return f"![{found.stem}]({self.asset(source, found)})" if found else f"*{target}*"

        def wikilink(m):
            target, _, alias = m.group(1).partition("|")
            note, _, heading = target.partition("#")
            label = (alias or heading or note).strip()
            if not note.strip():                              # [[#Titre]] : ancre dans la note
                return f"[{label}](#{github_slug(heading)})"
            page = self.note_link(note)
            return f"[{label}]({LINK_MARK}{page})" if page else label

        def local(m):
            bang, label, target = m.group(1), m.group(2), m.group(3)
            if re.match(r"^([a-z][a-z0-9+.-]*:|#|/)", target, re.I) or target.startswith(LINK_MARK):
                return m.group(0)
            path, _, frag = target.partition("#")
            found = (source.parent / unquote(path)).resolve()
            if not found.is_file():
                found = self.find(path)
            if found and found.suffix.lower() in IMAGE_EXT:
                return f"![{label}]({self.asset(source, found)})"
            if found and found.suffix.lower() == ".md":
                page = self.note_link(found.name)
                if page:
                    return f"{bang}[{label}]({LINK_MARK}{page})"
            return label or path                              # lien local introuvable : texte

        text = re.sub(r"%%.*?%%", "", text, flags=re.S)                    # commentaires Obsidian
        text = shield.hide(text)
        text = re.sub(r"!\[\[([^\]]+)\]\]", embed, text)
        text = re.sub(r"\[\[([^\]]+)\]\]", wikilink, text)
        text = re.sub(r"(!?)\[([^\]\n]*)\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)", local, text)
        # Blocs repliables HTML (exports Notion) : leur contenu reste du Markdown (extension md_in_html)
        return re.sub(r"<details(?![^>]*\bmarkdown=)([^>]*)>", r'<details markdown="1"\1>', text)


def build_index(vault, tree):
    """slug(nom de fichier) -> page publiée, pour transformer les liens entre notes en vrais liens."""
    index = {}
    for note in vault_notes(vault):
        rel = note.relative_to(vault).as_posix()
        try:
            dom, cat, title = resolve(vault, rel, tree)
        except ValueError:
            continue
        index[slug(note.stem)] = note_target(dom, cat, title, is_split(read_note(note)))
    return index


def github_slug(text):
    """Ancre à la façon d'Obsidian / GitHub (celle des sommaires écrits à la main)."""
    text = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return text.replace(" ", "-")


def heading_text(raw, shield):
    text = shield.plain(raw)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[*_=]{1,3}", "", text).strip().rstrip("#").strip()


HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")


def normalize_headings(text):
    """Le titre de tête s'efface devant le titre de la page ; s'il reste des « # », tout descend d'un niveau."""
    lines = text.split("\n")
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first is not None and re.match(r"^# ", lines[first]):
        lines[first] = ""
    if any(re.match(r"^# ", l) for l in lines):
        lines = [("#" + l if HEADING.match(l) and not l.startswith("######") else l) for l in lines]
    return "\n".join(lines).strip("\n")


def sections(text):
    """(préambule, [(titre, texte)]) : découpe au premier niveau de titre qui compte au moins trois
    sections ; un titre isolé plus haut (« Annexes », « Fin du cours ») ouvre aussi une section."""
    lines = text.split("\n")
    levels = [len(m.group(1)) for m in map(HEADING.match, lines) if m]
    if not levels:
        return text, []
    top = next((lv for lv in range(1, 7) if levels.count(lv) >= 3), min(levels))
    pre, secs, cur = [], [], None
    for line in lines:
        m = HEADING.match(line)
        if m and len(m.group(1)) <= top:
            cur = [m.group(2), [line]]
            secs.append(cur)
        elif cur:
            cur[1].append(line)
        else:
            pre.append(line)
    return "\n".join(pre).strip("\n"), [(t, "\n".join(body)) for t, body in secs]


def group_pages(secs, shield):
    """Regroupe les sections en pages : une page par partie si la note en a, sinon une par section ;
    les sections courtes rejoignent la précédente, les parties trop longues sont redécoupées."""
    secs = [(t, b) for t, b in secs if not TOC_TITLE.match(heading_text(t, shield))]
    if not secs:
        return []
    if sum(bool(PART_TITLE.match(heading_text(t, shield))) for t, _ in secs) >= 2:
        pages = []
        for t, b in secs:
            if PART_TITLE.match(heading_text(t, shield)) or not pages:
                pages.append([(t, b)])
            else:
                pages[-1].append((t, b))
        out = []
        for page in pages:
            if sum(len(b) for _, b in page) > MAX_PAGE and len(page) > 2:
                chunk, size = [], 0
                for t, b in page:
                    if chunk and size + len(b) > MAX_PAGE // 2:
                        out.append(chunk)
                        chunk, size = [], 0
                    chunk.append((t, b))
                    size += len(b)
                out.append(chunk)
            else:
                out.append(page)
        pages = out
    else:
        pages = [[s] for s in secs]
    merged = []
    for page in pages:
        if merged and sum(len(b) for _, b in page) < MIN_SECTION:
            merged[-1] += page
        else:
            merged.append(page)
    if len(merged) > 1 and sum(len(b) for _, b in merged[0]) < MIN_SECTION:
        merged[1] = merged[0] + merged[1]
        merged.pop(0)
    return [(heading_text(page[0][0], shield), "\n\n".join(b for _, b in page)) for page in merged]


def chapter_body(body):
    """Le titre de la section devient celui de la page : sa ligne disparaît et, si la page ne regroupe
    qu'une section, ses sous-titres remontent d'un niveau (le sommaire latéral reste lisible)."""
    lines = body.split("\n")
    top = HEADING.match(lines[0])
    if not top:
        return body
    rest = lines[1:]
    level = len(top.group(1))
    if not any((m := HEADING.match(l)) and len(m.group(1)) <= level for l in rest):
        rest = [l[1:] if (m := HEADING.match(l)) and len(m.group(1)) > level else l for l in rest]
    return "\n".join(rest).strip("\n")


def anchor_map(pages, shield):
    """Pour chaque page, ancres réelles (slugify de MkDocs, doublons _1, _2…) ; renvoie
    {ancre Obsidian/GitHub ou MkDocs -> (page, ancre MkDocs)}."""
    found = {}
    for path, body in pages:
        ids = set()
        for line in body.split("\n"):
            m = HEADING.match(line)
            if not m:
                continue
            text = heading_text(m.group(2), shield)
            real = toc_unique(toc_slugify(text, "-"), ids)
            for key in (github_slug(text), real, toc_slugify(text, "-")):
                found.setdefault(key, (path, real))
    return found


def guess_anchor(frag, anchors):
    """Sommaires écrits à la main dont l'ancre abrège le titre (« #chapitre-3--biais-et-défaillances ») :
    titre qui commence par l'ancre, puis même numéro de chapitre, puis titre le plus proche."""
    keys = [k for k in anchors if k]
    hits = [k for k in keys if k.startswith(frag)]
    num = re.match(r"(chapitre|ch)-?(\d+)(?!\d)", frag)
    if not hits and num:
        hits = [k for k in keys if re.match(rf"(?:chapitre|ch)-?{num.group(2)}(?!\d)", k)]
    if not hits:
        hits = difflib.get_close_matches(frag, keys, n=1, cutoff=0.75)
    return anchors[min(hits, key=len)] if hits else None


def finish_links(body, path, anchors):
    """Liens provisoires -> relatifs à la page ; ancres -> chapitre et identifiant réels."""
    here = posixpath.dirname(path)

    def internal(m):
        target, _, frag = m.group(1).partition("#")
        rel = posixpath.relpath(target, here)
        return f"]({rel}{'#' + frag if frag else ''})"

    def anchor(m):
        frag = unquote(m.group(1))
        hit = (anchors.get(frag) or anchors.get(frag.lower()) or anchors.get(github_slug(frag.replace("-", " ")))
               or guess_anchor(frag.lower(), anchors))
        if not hit:
            return m.group(0)
        page, real = hit
        frag = f"#{real}" if real else ""
        return f"]({frag or '#'})" if page == path else f"]({posixpath.relpath(page, here)}{frag})"

    body = re.sub(r"\]\(" + LINK_MARK + r"([^)\s]+)\)", internal, body)
    return re.sub(r"\]\(#([^)\s]+)\)", anchor, body)


def front(meta):
    return "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n"


def build(vault, rel, tree, title=None, to=None, index=None):
    """Convertit une note ; renvoie (pages {chemin docs/: contenu}, images, remarques)."""
    source = vault / rel
    if not source.is_file():
        raise ValueError(f"note introuvable : {rel}")
    dom, cat, title = resolve(vault, rel, tree, title, to)
    text = read_note(source)
    problems = [f"ligne {text.count(chr(10), 0, m.start()) + 1} : {label}"
                for label, pattern in BLOCKING for m in pattern.finditer(text)]
    if problems:
        raise ValueError(f"{rel} : import refusé (dépôt public) :\n    " + "\n    ".join(problems))
    notes = []
    masked = len(LAB_IP.findall(text))
    if masked:
        text = LAB_IP.sub(lambda m: f"{LAB_IP_TO[m.group(1)]}.{m.group(2)}", text)
        notes.append(f"{masked} IP de lab masquée(s)")
    shield = Shield()
    conv = Converter(vault, tree, index)
    body = normalize_headings(conv.convert(text, source, shield))
    meta = {"title": title, "source": Path(rel).as_posix()}
    split = is_split(text)
    entry = note_target(dom, cat, title, split)       # même règle que build_index : les liens entrants tiennent
    pages, chapters, tops = [], [], {}
    if split:
        pre, secs = sections(body)
        chapters = group_pages(secs, shield)
    if len(chapters) < 2:
        chapters = []
        pages.append((entry, body))
    else:
        folder = posixpath.dirname(entry)
        width = len(str(len(chapters)))
        paths = [f"{folder}/{i:0{width}d}-{slug(t)[:60].strip('-') or 'partie'}.md" for i, (t, _) in enumerate(chapters, 1)]
        summary = "\n".join(f"{i}. [{t}]({LINK_MARK}{p})" for i, ((t, _), p) in enumerate(zip(chapters, paths), 1))
        pages.append((entry, (pre + "\n\n" if pre.strip() else "") + f"## Sommaire\n\n{summary}"))
        for p, (t, b) in zip(paths, chapters):
            pages.append((p, chapter_body(b)))
            for key in (github_slug(t), toc_slugify(t, "-")):
                tops.setdefault(key, (p, None))       # le titre du chapitre est devenu celui de la page
        notes.append(f"{len(chapters)} pages")
    anchors = {**tops, **anchor_map(pages, shield)}
    out = {}
    for i, (path, content) in enumerate(pages):
        content = shield.show(finish_links(content, path, anchors)).strip()
        if chapters and i:
            head = {"title": chapters[i - 1][0], "source": meta["source"], "note": title,
                    "chapter": i, "chapters": len(chapters)}
        else:
            head = dict(meta, **({"chapters": len(chapters)} if chapters else {}))
        out[path] = front(head) + content + "\n"
    return out, conv.images, notes


def published():
    """{source du coffre: [fichiers de docs/library]} d'après l'en-tête « source » des pages publiées."""
    found = {}
    for f in LIBRARY.rglob("*.md") if LIBRARY.exists() else []:
        m = re.match(r"---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        src = (yaml.safe_load(m.group(1)) or {}).get("source") if m else None
        if src:
            found.setdefault(src, []).append(f)
    return found


def gitleaks(files):
    """Constats de gitleaks (configuration du dépôt) sur les fichiers donnés ; None s'il est absent."""
    exe = shutil.which("gitleaks")
    if not exe or not files:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / "scan"
        for f in files:
            dest = stage / f.relative_to(ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
        report = Path(tmp) / "report.json"
        subprocess.run([exe, "dir", ".", "--config", str(ROOT / ".gitleaks.toml"), "--redact",
                        "--no-banner", "--report-format", "json", "--report-path", str(report)],
                       capture_output=True, cwd=stage)
        data = json.loads(report.read_text(encoding="utf-8") or "[]") if report.exists() else []
        return [f"{Path(x['File']).name}:{x['StartLine']} ({x['RuleID']})" for x in data]


def write_note(vault, rel, tree, title=None, to=None, index=None, existing=None):
    pages, images, notes = build(vault, rel, tree, title, to, index)
    old = (existing if existing is not None else published()).get(Path(rel).as_posix(), [])
    for f in old:                                        # version précédente (autre titre, découpage…)
        f.unlink()
        if f.parent != LIBRARY and not any(f.parent.iterdir()):
            f.parent.rmdir()
    written = []
    for path, content in pages.items():
        target = DOCS / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content.encode("utf-8"))
        written.append(target)
    for image, name in images:
        dest = DOCS / ASSETS / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(image, dest)
        written.append(dest)
    found = gitleaks([f for f in written if f.suffix == ".md"])
    if found:
        for f in written:
            if f.suffix == ".md":
                f.unlink()
        raise ValueError(f"{rel} : gitleaks refuse la publication (règle à ajouter dans .gitleaks.toml "
                         f"si c'est un exemple de cours) :\n    " + "\n    ".join(found))
    if found is None:
        notes.append("gitleaks absent : contrôle laissé au workflow de publication")
    entry = next(iter(pages))
    return entry, notes


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", type=Path, required=True, help="dossier du coffre Obsidian (CyberSec-notes)")
    ap.add_argument("--list", action="store_true", help="afficher la correspondance note -> page, sans rien écrire")
    ap.add_argument("--all", action="store_true", help="publier toutes les notes rangées du coffre et retirer les pages orphelines")
    ap.add_argument("--title", help="titre de la note (une seule note)")
    ap.add_argument("--to", help="domaine/catégorie, ex. cyber/cti (une seule note)")
    ap.add_argument("notes", nargs="*", help="chemins relatifs au coffre")
    args = ap.parse_args(argv)
    tree = yaml.safe_load((ROOT / "data/bibliotheque.yml").read_text(encoding="utf-8"))
    vault = args.vault.resolve()
    existing = published()
    if args.list:
        for note in vault_notes(vault):
            rel = note.relative_to(vault).as_posix()
            try:
                dom, cat, title = resolve(vault, rel, tree)
            except ValueError as exc:
                print(f"?  {rel}  ({str(exc).split(' : ', 1)[-1]})")
                continue
            mark = "●" if rel in existing else "○"
            cut = " · découpée" if is_split(read_note(note)) else ""
            print(f"{mark}  {rel}  ->  {dom}/{cat} · {title}{cut}")
        print("\n● publiée · ○ à publier · ? --title / --to nécessaires")
        return 0
    if (args.title or args.to) and len(args.notes) != 1:
        ap.error("--title et --to s'utilisent avec une seule note")
    if args.all and args.notes:
        ap.error("--all ou une liste de notes, pas les deux")
    todo = [n.relative_to(vault).as_posix() for n in vault_notes(vault)] if args.all else args.notes
    index = build_index(vault, tree)
    code = 0
    for rel in todo:
        try:
            entry, notes = write_note(vault, rel, tree, args.title, args.to, index, existing)
            print(f"PUBLIÉE : {rel} -> docs/{entry}" + (f"  [{', '.join(notes)}]" if notes else ""))
        except (OSError, ValueError) as exc:
            print(f"NON PUBLIÉE : {exc}", file=sys.stderr)
            code = 1
    if args.all:
        for src, files in existing.items():
            if not (vault / src).is_file():
                for f in files:
                    f.unlink()
                    if not any(f.parent.iterdir()):
                        f.parent.rmdir()
                print(f"RETIRÉE : {src} (note absente du coffre)")
    if todo:
        print("Relire les pages (mkdocs serve), puis committer les fichiers nommés.")
    return code


if __name__ == "__main__":
    sys.exit(main())
