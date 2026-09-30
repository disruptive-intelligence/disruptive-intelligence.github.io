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
import collections
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
    "Cyber/10_Tools": ("cyber", "outils"), "Cyber/99_Concepts": ("cyber", "concepts"), "Cyber": ("cyber", "concepts"),
    "IT/01_Linux": ("it", "linux"), "IT/02_Windows": ("it", "windows"), "IT/03_Networking": ("it", "reseau"),
    "IT/04_Active-Directory": ("it", "active-directory"), "IT/05_Scripting_Langage-Prog": ("it", "scripting"),
    "IT/10_virtualization-containers": ("it", "conteneurs"), "IT/Culture": ("it", "culture"), "IT": ("it", "infrastructure"),
}
# Notes rangées sur le site ailleurs que leur dossier du coffre (le coffre Obsidian n'est pas réorganisé).
PLACES = {
    "Cyber/99_Concepts/Analyste_SOC.md": ("cyber", "cyberdefense"),
    "Cyber/99_Concepts/HTB_Attack Surface Management.md": ("cyber", "cyberdefense"),
    "Cyber/99_Concepts/VirusTotal.md": ("cyber", "outils"),
    "Cyber/HUMINT_Social_Engineering.md": ("cyber", "osint"),
    "Cyber/OPSEC_Privacy.md": ("cyber", "cti"),
    "Cyber/Red_Teaming.md": ("cyber", "cti"),
    "IT/02_Windows/HTB_Windows System Sécurity.md": ("cyber", "hardening"),
    "IT/03_Networking/AppSec.md": ("cyber", "hardening"),
    "IT/03_Networking/Infrastructure_IT.md": ("it", "infrastructure"),
    "IT/Culture/Materiel_informatique-connectique-andco.md": ("it", "infrastructure"),
    "IT/Culture/Fiche_How-The-Web-Works.md": ("it", "web"),
    "IT/Culture/Fiche_WebApp.md": ("it", "web"),
    "IT/Fiche_Web-Requests.md": ("it", "web"),
    "IT/Culture/SQL.md": ("it", "scripting"),
    "IT/Culture/Assembleur.md": ("it", "scripting"),
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
    "IT/Culture/Fiche_How-The-Web-Works.md": "Fonctionnement du web : URL, DNS, HTTPS",
    "IT/Fiche_Web-Requests.md": "HTTP & requêtes web",
}
SKIP = {"README.md"}
# Documents du coffre qui ne sont pas des notes personnelles : jamais publiés (--all retire leur page).
EXCLUDED = {
    "Cyber/01_CTI/CERT-EU-Cyber-Threat-Intelligence-Framework.md",   # cadre publié par le CERT-EU
}
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
SPLIT_AT = 150_000       # caractères : au-delà, la note est toujours découpée en pages
SPLIT_SECTIONS_AT = 20_000   # note plus longue avec au moins trois grandes sections : une page par section
MIN_SECTION = 2_000      # page plus courte (intertitre, « Fin du cours ») : rattachée à sa voisine
MIN_CHAPTER = 300        # un vrai chapitre garde sa page, sauf s'il est vide
MIN_CHAPTER_AVG = 3_000  # chapitres plus courts en moyenne (référentiel, glossaire) : restent dans la page de leur partie
MIN_SPLIT_PARTS = 8_000  # fiche plus courte : pas de sous-pages même si elle a des parties
QUIZ_TITLE = re.compile(r"(?i)\bmini-?quiz\b")   # quiz de révision : gardés dans le coffre, pas publiés
TOC_TITLE = re.compile(r"(?i)^(table des mati[eè]res|sommaire|table of contents)\b")
PART_TITLE = re.compile(r"(?i)^(partie|part|volume|livre|module)\b")
CHAPTER_TITLE = re.compile(r"(?i)^(chapitre|chapter|ch\.?|le[çc]on|lesson)\s*\d")
ANNEX_TITLE = re.compile(r"(?i)^annexes?\b")
CONCLUSION_TITLE = re.compile(r"(?i)^(conclusion|fin du cours|synth[èe]se (finale|g[ée]n[ée]rale)|bilan)\b")
CHEAT_TITLE = re.compile(r"(?i)cheat.?sheet|aide-m[ée]moire")   # une fiche de rappel reste d'un seul tenant
# Mots ignorés pour reconnaître le titre de tête d'une note (« # Cours complet de scripting Bash » = « Bash »)
TITLE_NOISE = {"htb", "cours", "complet", "note", "notes", "fiche", "les", "des", "une", "pour", "dans", "avec",
               "aux", "sur", "the", "and", "version", "vfull", "synthese"}
LINK_MARK = "@@"       # lien interne provisoire « @@library/…/page.md#ancre », rendu relatif page par page


def slug(text):
    text = str(text).translate(str.maketrans({"œ": "oe", "Œ": "OE", "æ": "ae", "Æ": "AE"}))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def category_of(rel):
    if Path(rel).as_posix() in PLACES:
        return PLACES[Path(rel).as_posix()]
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
                  if not {".obsidian", ".git", "_archives"} & set(p.parts) and p.parent != vault and p.name not in SKIP
                  and p.relative_to(vault).as_posix() not in EXCLUDED)


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


HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")


def outline(text):
    """[(numéro de ligne, niveau, texte)] des titres hors blocs de code."""
    out, fence = [], None
    for i, line in enumerate(text.split("\n")):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif line.strip().startswith(fence):
                fence = None
            continue
        h = HEADING.match(line) if fence is None else None
        if h:
            out.append((i, len(h.group(1)), clean_heading(h.group(2))))
    return out


def clean_heading(text):
    """Texte lisible d'un titre : « ## ## Titre » (coquille), gras, liens et « # » finaux retirés."""
    text = re.sub(r"^(#+\s*)+", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[*_=]{1,3}", "", text).strip().rstrip("#").strip()


def is_title(heading, title):
    """Le titre de tête reprend-il le titre de la note ? (sinon c'est une vraie section, à garder)"""
    words = {w for w in slug(title).split("-") if len(w) > 2 and w not in TITLE_NOISE}
    found = set(slug(heading).split("-"))
    return bool(words) and len(words & found) / len(words) >= 0.5


def is_split(text, title=""):
    """Note publiée en plusieurs pages : très longue, cours en chapitres, ou longue et en grandes sections.
    Une cheat sheet reste d'un seul tenant (on la parcourt avec Ctrl+F)."""
    if CHEAT_TITLE.search(title):
        return False
    if len(text) > SPLIT_AT:
        return True
    heads = outline(text)
    if heads and heads[0][1] == 1 and is_title(heads[0][2], title) and not text[:text.find("#")].strip():
        heads = heads[1:]
    if sum(bool(CHAPTER_TITLE.match(t)) for _, _, t in heads) >= 3:
        return True
    if sum(bool(PART_TITLE.match(t)) for _, _, t in heads) >= 2 and len(text) > MIN_SPLIT_PARTS:
        return True                                   # fiche organisée en parties : une page par partie
    if len(text) > SPLIT_SECTIONS_AT and heads:
        top = min(lv for _, lv, _ in heads)
        count = sum(lv == top for _, lv, _ in heads)
        # une suite de petites sections numérotées (fiche) reste d'un seul tenant
        return count >= 3 and len(text) / count >= MIN_CHAPTER_AVG
    return False


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
        self.blocks = set()                                  # jetons de blocs de code (une ligne à eux seuls)

    def _keep(self, chunk, block=False):
        self.saved.append(chunk)
        token = f"\x00{len(self.saved) - 1}\x00"
        if block:
            self.blocks.add(token)
        return token

    def hide(self, text):
        out, block, fence, indent = [], [], None, ""
        for line in text.split("\n"):
            m = re.match(r"^(\s*)(`{3,}|~{3,})", line)
            if fence is None and m:                          # l'indentation reste devant le jeton (code
                indent, fence, block = m.group(1), m.group(2), [line[len(m.group(1)):]]   # dans une liste)
            elif fence is not None:
                block.append(line)
                if line.strip().startswith(fence) and not line.strip()[len(fence):].strip():
                    out.append(indent + self._keep("\n".join(block), block=True))
                    fence = None
            else:
                out.append(re.sub(r"(`+)(?!`)(.+?)(?<!`)\1(?!`)", lambda m: self._keep(m.group(0)), line))
        if fence is not None:                               # bloc jamais refermé : laissé tel quel
            out.append(indent + self._keep("\n".join(block), block=True))
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

LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def space_blocks(text, shield):
    """Obsidian accepte une liste, une citation, un tableau ou un bloc de code collés au paragraphe qui
    précède ; MkDocs en ferait du texte en ligne (« …d'accès : - Identification ; - Authentication »).
    Ajoute la ligne vide manquante (texte déjà protégé : les blocs de code sont des jetons)."""
    def kind(line):
        s = line.strip()
        if not s:
            return "blank"
        if s in shield.blocks:
            return "code"
        if LIST_ITEM.match(line):
            return "list"
        if s.startswith(">"):
            return "quote"
        if s.startswith("|"):
            return "table"
        if HEADING.match(line):
            return "heading"
        return "text"

    out, prev = [], "blank"
    for line in text.split("\n"):
        k = kind(line)
        indented = line[:1] in (" ", "\t")
        if prev != "blank" and out:
            if (k in ("list", "quote", "table") and prev != k and not (indented and prev == "list")) \
                    or (k == "code" and not (indented and prev == "list")) \
                    or (prev == "code" and not indented) \
                    or (k == "text" and not indented and prev in ("list", "table")):
                out.append("")
        out.append(line)
        prev = k if not (indented and prev == "list" and k in ("text", "code")) else "list"
    return "\n".join(out)

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
            if target.startswith("attachment:"):              # image d'un export Notion, absente du coffre
                return ""
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

        def html_image(m):
            """<img src="../../assets/x.png" width="550"> -> image Markdown (copiée, largeur gardée)."""
            attrs = dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', m.group(0)))
            src = attrs.get("src", "")
            if not src or re.match(r"^[a-z]+:", src, re.I):
                return m.group(0)
            found = (source.parent / unquote(src)).resolve()
            if not found.is_file():
                found = self.find(src)
            if not found or found.suffix.lower() not in IMAGE_EXT:
                return f"*{attrs.get('alt') or Path(src).stem}*"
            width = f'{{ width="{attrs["width"]}" }}' if attrs.get("width", "").isdigit() else ""
            return f"![{attrs.get('alt', '')}]({self.asset(source, found)}){width}"

        text = re.sub(r"%%.*?%%", "", text, flags=re.S)                    # commentaires Obsidian
        text = shield.hide(text)
        text = re.sub(r"!\[\[([^\]]+)\]\]", embed, text)
        text = re.sub(r"\[\[([^\]]+)\]\]", wikilink, text)
        text = re.sub(r"<img\s[^>]*>", html_image, text)
        text = re.sub(r"(!?)\[([^\]\n]*)\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)", local, text)
        # Blocs repliables HTML (exports Notion) : leur contenu reste du Markdown (extension md_in_html)
        text = re.sub(r"<details(?![^>]*\bmarkdown=)([^>]*)>", r'<details markdown="1"\1>', text)
        return space_blocks(text, shield)


def build_index(vault, tree):
    """slug(nom de fichier) -> page publiée, pour transformer les liens entre notes en vrais liens."""
    index = {}
    for note in vault_notes(vault):
        rel = note.relative_to(vault).as_posix()
        try:
            dom, cat, title = resolve(vault, rel, tree)
        except ValueError:
            continue
        index[slug(note.stem)] = note_target(dom, cat, title, is_split(read_note(note), title))
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


def split_heading(text):
    """Titre-phrase -> (titre court, accroche) : « 1. Reconnaissance : But de l'attaquant… » ou
    « Network/Host artifacts (ex : clés de registre, chemins…) » ; un titre court reste tel quel."""
    if len(text) <= 70:
        return text, ""
    for m in re.finditer(r"\s:\s", text):
        before = text[:m.start()]
        if 3 <= len(before) <= 60 and before.count("(") == before.count(")"):
            return before.strip(), text[m.end():].strip()
    m = re.match(r"^(.{3,60}?)\s*\((.{25,})\)\s*$", text)
    if m:
        return m.group(1).strip(), f"*({m.group(2).strip()})*"
    return text, ""


def rebase(lines, top=2):
    """Décale tous les titres pour que le plus haut soit de niveau `top` (sous le titre de la page)."""
    levels = [len(m.group(1)) for m in map(HEADING.match, lines) if m]
    shift = (min(levels) - top) if levels else 0
    if not shift:
        return lines
    return [f"{'#' * max(1, min(6, len(m.group(1)) - shift))} {m.group(2)}" if (m := HEADING.match(l)) else l
            for l in lines]


def normalize_headings(text, title, shield):
    """Titres d'aplomb : le titre de tête qui reprend celui de la note s'efface (la page a le sien) et le
    sous-titre qui le suit devient une accroche ; « ## ## » corrigé, titres-phrases coupés ;
    le plus haut niveau présent devient ## ."""
    lines = text.split("\n")
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    m = re.match(r"^#[ \t]+(.+)$", lines[first]) if first is not None else None
    if m and is_title(heading_text(m.group(1), shield), title):
        lines[first] = ""
        heads = [(i, len(h.group(1)), h.group(2)) for i, l in enumerate(lines) if (h := HEADING.match(l))]
        nxt = next((i for i in range(first + 1, len(lines)) if lines[i].strip()), None)
        sub = heading_text(heads[0][2], shield) if heads else ""
        if heads and heads[0][0] == nxt and kind_of(sub) == "other" and len(sub.split()) >= 4 \
                and (len(heads) == 1 or heads[1][1] <= heads[0][1]):
            lines[nxt] = f"*{heading_text(heads[0][2], shield)}*"       # sous-titre du cours -> accroche
    out = []
    for line in lines:
        h = HEADING.match(line)
        if not h:
            out.append(line)
            continue
        head, lead = split_heading(re.sub(r"^(#+\s*)+", "", h.group(2)))
        out.append(f"{h.group(1)} {head}")
        if lead:
            out += ["", lead]
    return "\n".join(rebase(out)).strip("\n")


def drop_quizzes(body, shield):
    """Sections « Mini-quiz » retirées de la page publiée (elles restent dans la note Obsidian)."""
    out, skip = [], None
    for line in body.split("\n"):
        m = HEADING.match(line)
        if m and skip is not None and len(m.group(1)) <= skip:
            skip = None
        if m and skip is None and QUIZ_TITLE.search(heading_text(m.group(2), shield)):
            skip = len(m.group(1))
        if skip is None:
            out.append(line)
    return "\n".join(out).rstrip("\n")


def kind_of(text):
    for kind, pattern in (("toc", TOC_TITLE), ("part", PART_TITLE), ("chapter", CHAPTER_TITLE),
                          ("annex", ANNEX_TITLE), ("end", CONCLUSION_TITLE)):
        if pattern.match(text):
            return kind
    return "other"


def structure(body, shield, sections_only=False):
    """Plan d'une note normalisée : (présentation, [nœuds]) ; nœud = {"title", "lines", "children"}.
    - cours à parties : une partie = une entrée (page d'introduction) et une page par chapitre ;
    - cours à chapitres : une page par chapitre ;
    - sinon (sections_only) : une page par grande section.
    Ce qui précède le premier chapitre (prérequis, fil rouge, glossaire…) va dans la présentation ;
    les annexes sont regroupées ; le sommaire écrit à la main disparaît (la présentation a le sien)."""
    lines = body.split("\n")
    heads = [(i, len(m.group(1)), heading_text(m.group(2), shield)) for i, l in enumerate(lines)
             if (m := HEADING.match(l))]
    if not heads:
        return body, []
    kinds = [kind_of(t) for _, _, t in heads]
    chapters = [lv for (_, lv, _), k in zip(heads, kinds) if k == "chapter"]
    mode = "sections" if sections_only or len(chapters) < 2 else "chapters"
    chap_lv = (collections.Counter(chapters).most_common(1)[0][0] if mode == "chapters"
               else min(lv for _, lv, _ in heads))

    def holds_chapters(k):
        """Le titre n°k ouvre-t-il un groupe qui contient des chapitres ?"""
        lv = heads[k][1]
        for j in range(k + 1, len(heads)):
            if heads[j][1] <= lv and kinds[j] != "chapter":
                return False
            if kinds[j] == "chapter":
                return True
        return False

    pre, nodes, group, current, started = [], [], None, None, mode == "sections"
    bounds = {i: (lv, kind) for (i, lv, _), kind in zip(heads, kinds) if lv <= chap_lv or kind == "part"}
    skipping = False
    for i, line in enumerate(lines):
        if i in bounds:
            lv, kind = bounds[i]
            title = heading_text(HEADING.match(line).group(2), shield)
            k = next(n for n, h in enumerate(heads) if h[0] == i)
            skipping = False
            if kind == "toc" and not started:
                skipping, current = True, None
                continue
            if kind == "annex" and mode == "chapters":
                if re.fullmatch(r"(?i)annexes?\W*", title):           # « ANNEXES » ouvre le groupe
                    group = current = {"title": title, "lines": [line], "children": []}
                    nodes.append(group)
                else:                                                  # « Annexe A — … » : une page
                    if not group or not ANNEX_TITLE.match(group["title"]):
                        group = {"title": "Annexes", "lines": [], "children": []}
                        nodes.append(group)
                    current = {"title": title, "lines": [line], "children": []}
                    group["children"].append(current)
                started = True
                continue
            if kind == "part" or (lv < chap_lv and kind != "end"):
                if mode == "chapters" and not holds_chapters(k) and kind != "part":
                    if not started:
                        pre.append(line)
                        current = None
                        continue
                    current = {"title": title, "lines": [line], "children": []}
                    nodes.append(current)
                    group = None
                    continue
                group = current = {"title": title, "lines": [line], "children": []}
                nodes.append(group)
                started = True
                continue
            if kind == "end" and started:
                group, current = None, {"title": title, "lines": [line], "children": []}
                nodes.append(current)
                continue
            if kind == "chapter" or started:
                current = {"title": title, "lines": [line], "children": []}
                (group["children"] if group else nodes).append(current)
                started = True
                continue
            pre.append(line)
            current = None
            continue
        if skipping:
            continue
        (current["lines"] if current else pre).append(line)
    nodes = merge_small(nodes, pre, shield)
    acronyms = acronyms_of(body)

    def tidy(siblings):
        for node in siblings:
            node["title"] = tidy_title(node["title"], acronyms)
            tidy(node["children"])

    tidy(nodes)
    return "\n".join(pre).strip("\n"), nodes


def acronyms_of(text):
    """Sigles de la note (OSINT, CTI, NEXUS…) : mots en capitales dans des lignes qui ne le sont pas."""
    found = set()
    for line in text.split("\n"):
        letters = [c for c in line if c.isalpha()]
        if letters and sum(c.isupper() for c in letters) / len(letters) < 0.6:
            found.update(re.findall(r"\b[A-ZÀ-Ý][A-ZÀ-Ý0-9]+\b", line))
    return found


def tidy_title(title, acronyms):
    """« PARTIE I — FONDATIONS : PENSER EN ÉCOSYSTÈME » -> « Partie I — Fondations : penser en écosystème »
    (titres tout en capitales seulement ; sigles et chiffres romains gardés)."""
    letters = [c for c in title if c.isalpha()]
    if len(letters) < 6 or sum(c.isupper() for c in letters) / len(letters) < 0.9:
        return title
    out, start = [], True
    for token in re.split(r"(\W+)", title):
        if not token or not token[0].isalnum():
            out.append(token)
            if re.search(r"[—–.]", token):          # après « : », minuscule (usage français)
                start = True
            continue
        if token in acronyms or re.fullmatch(r"[IVXLC]+", token) or any(c.isdigit() for c in token):
            word = token
        else:
            word = token.lower()
        out.append(word[:1].upper() + word[1:] if start else word)
        start = False
    return "".join(out)


def size(node, shield):
    """Taille réelle (code compris) d'une page et de ses sous-pages."""
    return (len(shield.show("\n".join(node["lines"][1:])).strip())
            + sum(size(c, shield) for c in node["children"]))


def merge_small(nodes, pre, shield):
    """Pages minuscules (intertitre seul, « Fin du cours ») rattachées à leur voisine précédente ;
    un groupe sans chapitre devient une simple page."""
    out = []
    for node in nodes:
        node["children"] = merge_small(node["children"], node["lines"], shield)
        kids = node["children"]
        if kids and sum(size(c, shield) for c in kids) / len(kids) < MIN_CHAPTER_AVG:
            for c in kids:                                   # fiches de référentiel : la partie tient en une page
                node["lines"] += [""] + c["lines"]
            node["children"] = []
        chapter = kind_of(node["title"]) in ("chapter", "annex", "part")
        if node["children"] or size(node, shield) >= (MIN_CHAPTER if chapter else MIN_SECTION):
            out.append(node)
            continue
        host = out[-1] if out else None
        while host and host["children"]:
            host = host["children"][-1]
        if host:
            host["lines"] += [""] + node["lines"]
        else:
            pre += [""] + node["lines"]
    return out


def page_lines(node):
    """Corps d'une page : son titre devient celui de la page, le reste remonte sous lui."""
    return rebase(node["lines"][1:] if node["lines"] and HEADING.match(node["lines"][0]) else node["lines"])


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
    if not hits:                                        # titre-phrase raccourci à l'import
        longest = max((k for k in keys if len(k) >= 8 and frag.startswith(k)), key=len, default=None)
        hits = [longest] if longest else []
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
    body = drop_quizzes(normalize_headings(conv.convert(text, source, shield), title, shield), shield)
    meta = {"title": title, "source": Path(rel).as_posix()}
    split = is_split(text, title)
    entry = note_target(dom, cat, title, split)       # même règle que build_index : les liens entrants tiennent
    pages, tops, nodes = [], {}, []
    if split:
        pre, nodes = structure(body, shield)
        if len(nodes) < 2 and not any(n["children"] for n in nodes):
            pre, nodes = structure(body, shield, sections_only=True)
    if not split or not nodes:
        pages.append((entry, body, meta))
    else:
        folder = posixpath.dirname(entry)

        def place(siblings, where, up):
            """Chemins des pages : NN-titre.md, ou NN-titre/index.md pour une partie et ses chapitres."""
            width = max(2, len(str(len(siblings))))
            for i, node in enumerate(siblings, 1):
                name = f"{i:0{width}d}-{slug(node['title'])[:50].strip('-') or 'page'}"
                if node["children"]:
                    node["path"] = f"{where}/{name}/index.md"
                    place(node["children"], f"{where}/{name}", up + [node])
                else:
                    node["path"] = f"{where}/{name}.md"
                node["up"] = up

        def summary(siblings, depth=0):
            return "\n".join("    " * depth + f"- [{n['title']}]({LINK_MARK}{n['path']})"
                             + ("\n" + summary(n["children"], depth + 1) if n["children"] else "")
                             for n in siblings)

        def emit(siblings):
            for node in siblings:
                here = posixpath.dirname(node["path"])
                up = [[title, posixpath.relpath(entry, here)]] + [
                    [p["title"], posixpath.relpath(p["path"], here)] for p in node["up"]]
                content = "\n".join(page_lines(node)).strip("\n")
                if node["children"]:
                    content += f"\n\n## Dans cette partie\n\n{summary(node['children'])}"
                pages.append((node["path"], content, {"title": node["title"], "source": meta["source"],
                                                      "note": title, "up": up}))
                for key in (github_slug(node["title"]), toc_slugify(node["title"], "-")):
                    tops.setdefault(key, (node["path"], None))   # titre devenu celui de la page
                emit(node["children"])

        place(nodes, folder, [])
        pages.append((entry, (pre + "\n\n" if pre.strip() else "") + f"## Sommaire\n\n{summary(nodes)}", meta))
        emit(nodes)
        notes.append(f"{len(pages) - 1} pages")
    anchors = {**tops, **anchor_map([(p, c) for p, c, _ in pages], shield)}
    out = {}
    for path, content, head in pages:
        out[path] = front(head) + shield.show(finish_links(content, path, anchors)).strip() + "\n"
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


def remove_pages(files):
    """Supprime des pages publiées et les dossiers (note découpée, partie) restés vides."""
    for f in files:
        if f.exists():
            f.unlink()
        folder = f.parent
        while folder != LIBRARY and folder.exists() and not any(folder.iterdir()):
            folder.rmdir()
            folder = folder.parent


def write_note(vault, rel, tree, title=None, to=None, index=None, existing=None):
    pages, images, notes = build(vault, rel, tree, title, to, index)
    old = (existing if existing is not None else published()).get(Path(rel).as_posix(), [])
    remove_pages(old)                                    # version précédente (autre titre, découpage…)
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
            cut = " · découpée" if is_split(read_note(note), title) else ""
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
    if args.all:                  # d'abord : une note fusionnée peut reprendre le titre (et les pages) d'une archivée
        for src, files in existing.items():
            if not (vault / src).is_file() or src in EXCLUDED:
                remove_pages(files)
                print(f"RETIRÉE : {src} (note absente du coffre ou exclue)")
    for rel in todo:
        try:
            entry, notes = write_note(vault, rel, tree, args.title, args.to, index, existing)
            print(f"PUBLIÉE : {rel} -> docs/{entry}" + (f"  [{', '.join(notes)}]" if notes else ""))
        except (OSError, ValueError) as exc:
            print(f"NON PUBLIÉE : {exc}", file=sys.stderr)
            code = 1
    if args.all:
        used = {m for f in LIBRARY.rglob("*.md") for m in re.findall(r"assets/([^)\s\"]+)", f.read_text(encoding="utf-8"))}
        for image in (LIBRARY / "assets").glob("*") if (LIBRARY / "assets").exists() else []:
            if image.name not in used:                   # image qu'aucune page n'utilise plus
                image.unlink()
                print(f"IMAGE RETIRÉE : {image.name}")
    if todo:
        print("Relire les pages (mkdocs serve), puis committer les fichiers nommés.")
    return code


if __name__ == "__main__":
    sys.exit(main())
