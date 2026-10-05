"""Importe les notes Obsidian (CyberSec-notes-v2) dans la Bibliothèque du portail.

    python scripts/import_notes.py --vault ../CyberSec-notes-v2 --list      # correspondances, sans rien écrire
    python scripts/import_notes.py --vault ../CyberSec-notes-v2 --all       # publie / met à jour toutes les notes
    python scripts/import_notes.py --vault ../CyberSec-notes-v2 "Cyber/02 OSINT/OSINT — synthèse.md" [autres…]

--all est la commande de routine (« publie mes notes ») : chaque note du coffre rangée dans une rubrique
est (ré)importée, les pages dont la note source a disparu du coffre sont supprimées.
Le coffre suit l'arborescence de data/bibliotheque.yml : Domaine/NN Rubrique[/Sous-rubrique]/Titre.md.
Pour chaque note :
  - rubrique = dossiers du coffre (libellés de data/bibliotheque.yml sans emoji ni numéro), ou --to dom/cat ;
  - titre = nom du fichier (la note prévue de même nom, « : » s'écrivant « - »), ou --title ;
  - propriétés Obsidian lues : format, provenance, niveau, objectif, prerequis, termes, rubrique ;
  - syntaxe Obsidian convertie hors du code : [[Note]] et [[#Titre]] -> vrais liens, ![[image]] et images
    locales -> copiées dans docs/library/assets/, liens locaux introuvables -> texte ;
  - titres : le titre de tête laisse la place au titre de la page, les autres « # » descendent d'un niveau ;
  - note de plus de SPLIT_AT caractères -> dossier <slug>/ : index.md (présentation + sommaire)
    et une page par partie ou chapitre ; les liens d'ancre suivent le chapitre où le titre a atterri ;
  - non publiés : mini-quiz, notes de rédaction (registre de cohérence, en-tête de maintenance, journal des
    modifications) ; l'annexe « Questions types d'entretien » part dans l'espace Révision (une page par
    rubrique, avec les notes du dossier Révision/ du coffre) ;
  - dépôt public : les IP de lab HackTheBox sont masquées (10.10.x.y -> 10.0.x.y, 10.129.x.y -> 10.1.x.y),
    un flag de CTF, une clé privée ou un vrai jeton empêchent l'import, puis gitleaks (s'il est installé)
    contrôle les pages écrites avec la configuration du dépôt ; au moindre constat la note est retirée.
Rien n'est commité : relire (mkdocs serve), puis committer les fichiers nommés.
"""
import argparse
import collections
import datetime
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
REVISION = "library/revision"     # espace Révision : une page par rubrique (questions d'entretien)
REVISION_FOLDER = "Révision"      # dossier du coffre des notes de révision autonomes
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
SPLIT_AT = 150_000       # caractères : au-delà, la note est toujours découpée en pages
SPLIT_SECTIONS_AT = 15_000   # note plus longue avec au moins trois grandes sections : une page par section
MIN_SECTION = 1_500      # page plus courte (intertitre, « Fin du cours ») : rattachée à sa voisine
MIN_CHAPTER = 300        # un vrai chapitre garde sa page, sauf s'il est vide
MIN_CHAPTER_AVG = 3_000  # chapitres plus courts en moyenne (référentiel, glossaire) : restent dans la page de leur partie
MIN_SPLIT_PARTS = 8_000  # fiche plus courte : pas de sous-pages même si elle a des parties
COURSE_AT = 120_000      # note plus longue, même sans chapitres : un cours (sinon une synthèse)
QUIZ_TITLE = re.compile(r"(?i)\bmini-?quiz\b")   # quiz de révision : gardés dans le coffre, pas publiés
# Notes de travail de la rédaction (cours écrits par tranches) : gardées dans le coffre, pas publiées
SCAFFOLD_TITLE = re.compile(r"(?i)^(registre de coh[ée]rence|en-t[êe]te de maintenance|journal des modifications)\b")
# Annexe de questions d'entretien : publiée dans l'espace Révision plutôt qu'à la fin du cours
REVISION_TITLE = re.compile(r"(?i)^annexe\s*[—–-]\s*questions types d.entretien")
TOC_TITLE = re.compile(r"(?i)^(table des mati[eè]res|sommaire|table of contents)\b")
PART_TITLE = re.compile(r"(?i)^(partie|part|volume|livre|module)\b")
CHAPTER_TITLE = re.compile(r"(?i)^(chapitre|chapter|ch\.?|le[çc]on|lesson)\s*\d")
ANNEX_TITLE = re.compile(r"(?i)^annexes?\b")
CONCLUSION_TITLE = re.compile(r"(?i)^(conclusion|fin du cours|synth[èe]se (finale|g[ée]n[ée]rale)|bilan)\b")
CHEAT_TITLE = re.compile(r"(?i)cheat.?sheet|aide-m[ée]moire")   # une fiche de rappel reste d'un seul tenant
# Mots ignorés pour reconnaître le titre de tête d'une note (« # Cours complet de scripting Bash » = « Bash »)
TITLE_NOISE = {"htb", "cours", "complet", "note", "notes", "fiche", "les", "des", "une", "pour", "dans", "avec",
               "aux", "sur", "the", "and", "version", "complete", "vfull", "synthese"}
LINK_MARK = "@@"       # lien interne provisoire « @@library/…/page.md#ancre », rendu relatif page par page


def slug(text):
    text = str(text).translate(str.maketrans({"œ": "oe", "Œ": "OE", "æ": "ae", "Æ": "AE"}))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def label_key(label):
    """Libellé du site ou dossier du coffre, comparables : « 🛰️ Détection & réponse » = « 06 Détection & réponse »."""
    return slug(re.sub(r"^\d+\s*[-_.]?\s*", "", str(label).strip()))


def category_of(rel, tree):
    """(domaine, catégorie) d'après les dossiers du coffre : Domaine/NN Rubrique/…"""
    parts = Path(rel).parts
    if len(parts) < 3:
        return None
    for d in tree:
        if label_key(d["label"]) == label_key(parts[0]):
            for c in d.get("categories", []):
                if label_key(c["label"]) == label_key(parts[1]):
                    return d["id"], c["id"]
    return None


def planned(tree, dom, cat):
    for d in tree:
        if d["id"] == dom:
            for c in d.get("categories", []):
                if c["id"] == cat:          # notes directes, ou réparties en sous-rubriques (groups)
                    return (c.get("notes") or []) + [n for g in c.get("groups") or [] for n in g.get("notes") or []]
    raise ValueError(f"catégorie inconnue dans data/bibliotheque.yml : {dom}/{cat}")


def vault_notes(vault):
    """Notes du coffre rangées dans un dossier (les fichiers de la racine et README sont ignorés)."""
    return sorted(p for p in vault.rglob("*.md")
                  if not {".obsidian", ".git", "_archives"} & set(p.parts) and p.parent != vault and p.name not in SKIP)


def is_revision(vault, rel):
    """Note de révision autonome : rangée dans Révision/ ou déclarée « format: revision »."""
    return Path(rel).parts[0] == REVISION_FOLDER or read_props(vault / rel).get("format") == "revision"


def resolve(vault, rel, tree, title=None, to=None):
    """(domaine, catégorie, titre) d'une note du coffre ; ValueError si la rubrique manque.
    Titre : la note prévue dans data/bibliotheque.yml dont le nom de fichier reprend le titre, sinon le nom
    du fichier lui-même (une nouvelle note publiée sans rien déclarer)."""
    dom, cat = to.split("/") if to else (category_of(Path(rel), tree) or (None, None))
    if not dom:
        raise ValueError(f"{rel} : rubrique inconnue (dossier hors de l'arborescence du site), préciser --to domaine/catégorie")
    if not title:
        stem = Path(rel).stem
        title = next((c for c in planned(tree, dom, cat) if slug(c) == slug(stem)), stem)
    return dom, cat, title


def front_matter(text):
    """(propriétés, texte sans en-tête) ; un « --- » qui n'ouvre pas de vraies propriétés reste du texte."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if m:
        try:
            props = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            props = None
        if isinstance(props, dict):
            return props, text[m.end():]
        if re.match(r"^[\w-]+:", m.group(1)):          # propriétés illisibles (« : » sans guillemets) : retirées
            print(f"  propriétés Obsidian illisibles, ignorées : {m.group(1).splitlines()[0][:60]}…", file=sys.stderr)
            return {}, text[m.end():]
    return {}, text


def read_note(path):
    return front_matter(path.read_text(encoding="utf-8-sig").replace("\r\n", "\n"))[1]


def read_props(path):
    """Propriétés Obsidian (en-tête YAML) : format, provenance, niveau, objectif, prerequis, termes, rubrique."""
    return front_matter(path.read_text(encoding="utf-8-sig").replace("\r\n", "\n"))[0]


FORMAT_NAMES = ("cours", "synthese", "fiche", "aide-memoire", "atelier", "ressources", "revision")


def note_format(text, title, props, cat):
    """cours (exhaustif) | synthese (parcours condensé) | fiche (une notion) | aide-memoire | atelier |
    ressources (liens) | revision (questions). Propriété « format » de la note, sinon règle automatique."""
    if props.get("format") in FORMAT_NAMES:
        return props["format"]
    if cat == "notions":
        return "fiche"
    if CHEAT_TITLE.search(title):
        return "aide-memoire"
    if re.search(r"(?i)synth[èe]se", title):
        return "synthese"
    heads = outline(text)
    if (sum(bool(CHAPTER_TITLE.match(t)) for _, _, t in heads) >= 3
            or sum(bool(re.match(r"(?i)partie\b", t)) for _, _, t in heads) >= 2 or len(text) > COURSE_AT):
        return "cours"
    return "synthese"


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
    joined = slug(heading).replace("-", "")
    found = {w for w in words if w in set(slug(heading).split("-")) or w in joined}   # « crypto-actifs »
    common = len(words & found)                        # « Gestion des incidents » n'est pas « HTB — Réponse à incidents »
    return bool(words) and common / len(words) >= 0.5 and (common >= 2 or len(words) == 1)


def lone_h1(heads):
    """[(niveau, texte)] : le premier titre est le seul de niveau 1 de la note (hors sections non publiées) ;
    dans une note longue, c'est alors son titre, même s'il ne reprend pas ses mots (« DIGITAL FORENSICS ») ;
    une fiche courte qui s'ouvre sur « # Définitions de base » garde cette vraie section."""
    if not heads or heads[0][0] != 1:
        return False
    skip = None
    for level, text in heads[1:]:
        if skip is not None and level <= skip:
            skip = None
        if skip is None and dropped(text):
            skip = level
            continue
        if skip is None and level == 1:
            return False
    return True


def is_split(text, title=""):
    """Note publiée en plusieurs pages : très longue, cours en chapitres, ou longue et en grandes sections.
    Une cheat sheet reste d'un seul tenant (on la parcourt avec Ctrl+F)."""
    if CHEAT_TITLE.search(title):
        return False
    if len(text) > SPLIT_AT:
        return True
    heads = outline(text)
    lone = lone_h1([(lv, x) for _, lv, x in heads]) and len(text) > SPLIT_SECTIONS_AT   # cours long : son titre
    if heads and heads[0][1] == 1 and (is_title(heads[0][2], title) or lone) and not text[:text.find("#")].strip():
        heads = heads[1:]
    if sum(bool(CHAPTER_TITLE.match(t)) for _, _, t in heads) >= 3:
        return True
    if sum(bool(PART_TITLE.match(t)) for _, _, t in heads) >= 2 and len(text) > MIN_SPLIT_PARTS:
        return True                                   # fiche organisée en parties : une page par partie
    if len(text) > SPLIT_SECTIONS_AT and heads:
        levels = [lv for _, lv, _ in heads]            # même règle que sections() : premier niveau à 3 titres
        top = next((lv for lv in range(1, 7) if levels.count(lv) >= 3), min(levels))
        count = sum(lv <= top for lv in levels)
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


LIST_MARK = re.compile(r"^[ \t]*((?:[-*+]|\d+[.)])[ \t]+)(.*)$")


def nest_lists(text, shield):
    """Obsidian imbrique une sous-liste décalée de 2 espaces ; Python-Markdown en veut 4 et l'aplatit
    sinon (« Task Scheduler permet : » puis ses sous-points au même niveau, en une longue liste).
    Réindente : chaque niveau à 4 espaces de son parent ; les suites d'une puce (texte, tableau, bloc
    de code) suivent leur puce."""
    def shift(token, delta):                                 # lignes internes d'un bloc de code gardé
        i = int(token.strip("\x00"))
        lines = shield.saved[i].split("\n")
        pad = " " * max(delta, 0)
        shield.saved[i] = "\n".join(lines[:1] + [pad + l[min(-delta, len(l) - len(l.lstrip(" "))):]
                                                 if delta < 0 else pad + l for l in lines[1:]])

    out, stack, blank = [], [], True                         # stack : (colonne du texte source, retrait cible)
    for line in text.split("\n"):
        body = line.lstrip(" \t")
        if not body:
            out.append(line)
            blank = True
            continue
        col = len(line[:len(line) - len(body)].expandtabs(4))
        m = LIST_MARK.match(line)
        if HEADING.match(line) or (col == 0 and not m and blank):
            stack = []                                       # titre, ou paragraphe après une ligne vide : fin de liste
        while stack and col < stack[-1][0]:
            stack.pop()
        if m and (stack or col < 4):
            dst = stack[-1][1] if stack else 0
            stack.append((col + len(m.group(1).expandtabs(4)), dst + 4))
            line = " " * dst + body
        elif stack and col:
            extra = col - stack[-1][0]                       # 1 à 3 espaces de plus : même suite de puce
            dst = stack[-1][1] + (extra if extra >= 4 else 0)
            if body.strip() in shield.blocks and dst != col:
                shift(body.strip(), dst - col)
            line = " " * dst + body
        out.append(line)
        blank = False
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
        def width_of(label):
            """« légende|400 » (largeur Obsidian) -> (« légende », '{ width="400" }')."""
            text, _, size = label.rpartition("|")
            return (text.strip(), f'{{ width="{size.strip()}" }}') if text and size.strip().isdigit() else (label, "")

        def embed(m):
            target, _, size = m.group(1).partition("|")
            target = target.strip()
            found = self.find(target) if Path(target).suffix.lower() in IMAGE_EXT else None
            width = f'{{ width="{size.strip()}" }}' if size.strip().isdigit() else ""
            return f"![{found.stem}]({self.asset(source, found)}){width}" if found else f"*{target}*"

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
                label, width = width_of(label)
                return f"![{label}]({self.asset(source, found)}){width}"
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
        return nest_lists(space_blocks(text, shield), shield)


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


# Début de titre trop vague pour servir seul (« Chapitre 34 — Cas complet : profilage… ») : titre gardé entier
GENERIC_LEAD = re.compile(r"(?i)^(?:(?:chapitre|chapter|ch\.?)\s*\d+\s*[—–-]\s*)?(?:cas(?: complet| pratique| de synthèse)?"
                          r"|étude de cas|exercice|lab|atelier|synthèse|exemple)\s*\d*$")


def split_heading(text):
    """Titre-phrase -> (titre court, accroche) : « 1. Reconnaissance : But de l'attaquant… » ou
    « Network/Host artifacts (ex : clés de registre, chemins…) » ; un titre court reste tel quel, comme
    celui dont le début ne dit rien seul (« Cas complet : … »)."""
    if len(text) <= 70:
        return text, ""
    for m in re.finditer(r"\s:\s", text):
        before = text[:m.start()]
        if GENERIC_LEAD.match(before.strip()):
            return text, ""
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
    every = [(len(h.group(1)), heading_text(h.group(2), shield)) for l in lines if (h := HEADING.match(l))]
    if m and (is_title(heading_text(m.group(1), shield), title) or (lone_h1(every) and len(text) > SPLIT_SECTIONS_AT)):
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
    return "\n".join(close_gaps(rebase(out))).strip("\n")


def close_gaps(lines):
    """Sauts de niveau (## suivi de ####, habitude des exports Notion) : chaque titre descend d'un
    seul cran sous son parent, pour une table des matières bien emboîtée."""
    stack, out = [], []                               # (niveau d'origine, niveau publié)
    for line in lines:
        m = HEADING.match(line)
        if not m:
            out.append(line)
            continue
        level = len(m.group(1))
        while stack and stack[-1][0] >= level:
            stack.pop()
        new = min(level, stack[-1][1] + 1) if stack else level
        stack.append((level, new))
        out.append(f"{'#' * new} {m.group(2)}")
    return out


def dropped(heading):
    """Section non publiée avec la note : mini-quiz, note de rédaction, annexe de questions d'entretien."""
    return bool(QUIZ_TITLE.search(heading) or SCAFFOLD_TITLE.match(heading) or REVISION_TITLE.match(heading))


def drop_sections(body, shield):
    """Retire de la page publiée les sections non publiées (elles restent dans la note Obsidian)."""
    out, skip = [], None
    for line in body.split("\n"):
        m = HEADING.match(line)
        if m and skip is not None and len(m.group(1)) <= skip:
            skip = None
        if m and skip is None and dropped(heading_text(m.group(2), shield)):
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
    levels = [lv for _, lv, _ in heads]
    chap_lv = (collections.Counter(chapters).most_common(1)[0][0] if mode == "chapters"      # sinon : premier
               else next((lv for lv in range(1, 7) if levels.count(lv) >= 3), min(levels)))   # niveau à 3 titres

    def chapters_follow(k):
        """Un bilan suivi d'autres chapitres avant la partie suivante est intermédiaire : il reste dans sa partie."""
        for j in range(k + 1, len(heads)):
            if kinds[j] == "chapter":
                return True
            if kinds[j] in ("part", "annex") and heads[j][1] <= heads[k][1]:
                return False
        return False

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
    # Parties : seulement au niveau principal (un sommaire écrit à la main répète « ### Partie V — … »)
    part_lv = min((lv for (_, lv, _), k in zip(heads, kinds) if k == "part"), default=0)
    bounds = {i: (lv, kind) for (i, lv, _), kind in zip(heads, kinds)
              if lv <= chap_lv or (kind == "part" and lv <= part_lv)}
    skipping = None                                   # niveau du sommaire manuel en cours d'omission
    for i, line in enumerate(lines):
        h = HEADING.match(line)
        if skipping is not None and h and len(h.group(1)) > skipping:
            continue                                  # titres internes du sommaire : omis avec lui
        if i in bounds:
            lv, kind = bounds[i]
            title = heading_text(h.group(2), shield)
            k = next(n for n, x in enumerate(heads) if x[0] == i)
            skipping = None
            if kind == "toc" and not started:
                skipping, current = lv, None
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
            if kind == "end" and started and not chapters_follow(k):
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
        if skipping is not None:
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
            found.update(w for w in re.findall(r"\b[A-ZÀ-Ý][A-ZÀ-Ý0-9]+\b", line) if w.lower() not in SMALL_WORDS)
    return found


# Mots français jamais pris pour des sigles (« Profilage d'acteur ET attribution »)
SMALL_WORDS = {"et", "ou", "de", "du", "des", "la", "le", "les", "un", "une", "en", "au", "aux", "a", "à", "pour",
               "par", "sur", "sous", "sans", "avec", "dans", "pas", "ne", "que", "qui", "quoi", "ce", "ces", "son",
               "sa", "ses", "leur", "leurs", "avant", "après", "apres", "comme", "vers", "entre", "mais", "donc",
               "quand", "est", "sont", "plus", "moins", "tout", "tous", "chez", "contre", "depuis", "selon"}
ELIDED = {"l", "d", "j", "n", "s", "c", "qu", "jusqu", "lorsqu", "puisqu"}   # L'…, D'…, QU'…
# Noms propres et sigles écrits en minuscules par la remise en casse (« administration windows locale »)
PROPER = {"windows": "Windows", "linux": "Linux", "powershell": "PowerShell", "docker": "Docker",
          "kubernetes": "Kubernetes", "ansible": "Ansible", "python": "Python", "javascript": "JavaScript",
          "bash": "Bash", "sql": "SQL", "iran": "Iran", "chine": "Chine", "russie": "Russie", "europe": "Europe",
          "france": "France", "internet": "Internet", "microsoft": "Microsoft", "mitre": "MITRE",
          "api": "API", "apis": "API", "ot": "OT", "ia": "IA", "dprk": "DPRK", "osint": "OSINT",
          "cti": "CTI", "ie": "IE", "soc": "SOC", "grc": "GRC", "mcs": "MCS", "ssi": "SSI",
          "tcp": "TCP", "ip": "IP", "dns": "DNS", "http": "HTTP", "https": "HTTPS", "vpn": "VPN", "gpo": "GPO",
          "ntfs": "NTFS", "smb": "SMB", "dhcp": "DHCP", "ssh": "SSH", "uac": "UAC", "edr": "EDR", "siem": "SIEM",
          "devsecops": "DevSecOps", "ics": "ICS", "rgpd": "RGPD", "nis2": "NIS2"}
PROPER_PHRASES = [(re.compile(r"\bcorée du nord\b", re.I), "Corée du Nord")]


def tidy_title(title, acronyms):
    """« PARTIE I — FONDATIONS : PENSER EN ÉCOSYSTÈME » -> « Partie I — Fondations : penser en écosystème »
    (titres tout en capitales seulement ; sigles, chiffres romains et noms propres gardés)."""
    letters = [c for c in title if c.isalpha()]
    if len(letters) < 6 or sum(c.isupper() for c in letters) / len(letters) < 0.9:
        return title
    tokens = re.split(r"(\W+)", title)
    out, start = [], True
    for i, token in enumerate(tokens):
        if not token or not token[0].isalnum():
            out.append(token)
            if re.search(r"[—–.]", token):          # après « : », minuscule (usage français)
                start = True
            continue
        low = token.lower()
        after = tokens[i + 1] if i + 1 < len(tokens) else ""
        if low in ELIDED and after[:1] in ("'", "’"):
            word = low                                # « L'intelligence », pas « L » (chiffre romain)
        elif low in PROPER:
            word = PROPER[low]
        elif low in SMALL_WORDS:
            word = low
        elif token in acronyms or re.fullmatch(r"[IVXLC]+", token) or any(c.isdigit() for c in token):
            word = token
        else:
            word = low
        out.append(word[:1].upper() + word[1:] if start else word)
        start = False
    text = "".join(out)
    for rx, fixed in PROPER_PHRASES:
        text = rx.sub(fixed, text)
    return text


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
    body = drop_sections(normalize_headings(conv.convert(text, source, shield), title, shield), shield)
    meta = {"title": title, "source": Path(rel).as_posix()}
    props = read_props(source)
    kind = note_format(text, title, props, cat)
    if kind:
        meta["format"] = kind
    if props.get("provenance"):                        # badge : HTB Academy, L2I…
        meta["provenance"] = str(props["provenance"])
    if props.get("resume"):                            # une phrase : pages de domaine et de rubrique
        meta["resume"] = str(props["resume"]).strip()
    if str(props.get("statut") or "").strip().lower() in ("en cours", "brouillon"):   # note encore en rédaction
        meta["statut"] = "en cours"
    meta["revue"] = datetime.date.fromtimestamp(source.stat().st_mtime).isoformat()   # dernière modification
    for key in ("niveau", "objectif", "prerequis"):    # propriétés Obsidian facultatives, affichées si présentes
        if props.get(key):
            meta[key] = str(props[key])
    if revision_section(text):                         # questions d'entretien : page de révision de la rubrique
        meta["revision"] = revision_page(dom, cat)
    if isinstance(props.get("termes"), dict):          # fiche notion : termes du glossaire (terme: définition)
        meta["terms"] = {str(k): str(v) for k, v in props["termes"].items()}
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


# ------------------------------------------------------------------ espace Révision

def revision_section(text):
    """Annexe « Questions types d'entretien » d'une note (titre compris), ou None."""
    heads = outline(text)
    lines = text.split("\n")
    for k, (i, level, title) in enumerate(heads):
        if REVISION_TITLE.match(title):
            end = next((j for j, lv, _ in heads[k + 1:] if lv <= level), len(lines))
            return "\n".join(lines[i:end]).strip("\n")
    return None


def revision_page(dom, cat):
    return f"{REVISION}/{cat}.md" if cat else f"{REVISION}/{dom}.md"


def category_label(tree, dom, cat):
    for d in tree:
        for c in d.get("categories", []) if d["id"] == dom else []:
            if c["id"] == cat:
                return re.sub(r"^\W+", "", c["label"]).strip(), re.sub(r"^\W+", "", d["label"]).strip()
    return None, None


def revision_sources(vault, tree, index):
    """{(domaine, catégorie) ou (None, sujet): [(note du coffre, titre, page du cours ou None, texte)]}
    — annexes des cours, puis notes autonomes du dossier Révision/ (propriété « rubrique »)."""
    groups = {}
    for note in vault_notes(vault):
        rel = note.relative_to(vault).as_posix()
        text = read_note(note)
        if is_revision(vault, rel):
            rubric = str(read_props(note).get("rubrique") or "")
            key = tuple(rubric.split("/", 1)) if "/" in rubric else (None, note.stem)
            groups.setdefault(key, []).append((rel, note.stem, None, text))
            continue
        section = revision_section(text)
        if not section:
            continue
        try:
            dom, cat, title = resolve(vault, rel, tree)
        except ValueError:
            continue
        course = note_target(dom, cat, title, is_split(text, title))
        groups.setdefault((dom, cat), []).insert(0, (rel, title, course, section))
    return groups


def revision_body(vault, rel, text, tree, index, path, depth):
    """Questions d'une source, converties comme une note ; leur titre de tête disparaît (la page en a un)."""
    found = [label for label, pattern in BLOCKING for _ in pattern.finditer(text)]
    if found:
        raise ValueError(f"{rel} : révision refusée (dépôt public) : {', '.join(found)}")
    text = LAB_IP.sub(lambda m: f"{LAB_IP_TO[m.group(1)]}.{m.group(2)}", text)
    shield = Shield()
    conv = Converter(vault, tree, index)
    lines = conv.convert(text, vault / rel, shield).split("\n")
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first is not None and HEADING.match(lines[first]):
        lines = lines[first + 1:]
    body = "\n".join(close_gaps(rebase(lines, top=depth))).strip("\n")
    return shield.show(finish_links(body, path, {})), conv.images


def write_revisions(vault, tree, index):
    """Pages de l'espace Révision (une par rubrique, plus une par note autonome sans rubrique) ;
    les pages devenues sans source sont supprimées. Renvoie [(page, remarques)]."""
    folder = DOCS / REVISION
    old = set(folder.glob("*.md")) if folder.exists() else set()
    written, report = [], []
    for (dom, cat), sources in sorted(revision_sources(vault, tree, index).items(), key=lambda kv: str(kv[0])):
        label, domain = category_label(tree, dom, cat) if dom else (None, None)
        title = f"Révision — {label}" if label else sources[0][1]
        path = revision_page(dom, cat) if dom else f"{REVISION}/{slug(cat)}.md"
        many = len(sources) > 1
        parts, images = [], []
        for rel, name, course, text in sources:
            name = re.sub(r"\s*[—–-]\s*questions de r[ée]vision$", "", name)     # « Threat hunting — questions de révision »
            body, imgs = revision_body(vault, rel, text, tree, index, path, 3 if many else 2)
            images += imgs
            origin = (f"*D'après le cours [{name}]({posixpath.relpath(course, posixpath.dirname(path))})*"
                      if course else "")
            parts.append((f"## {name}\n\n" if many else "") + (origin + "\n\n" if origin else "") + body)
        meta = {"title": title, "revision": f"{dom}/{cat}" if dom else "transverse",
                "domaine": domain or "", "sources": [s[0] for s in sources]}
        target = DOCS / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((front(meta) + "\n\n".join(parts).strip() + "\n").encode("utf-8"))
        for image, name in images:
            dest = DOCS / ASSETS / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(image, dest)
        written.append(target)
        report.append((path, f"{len(sources)} source(s)"))
    found = gitleaks(written)
    if found:
        for f in written:
            f.unlink()
        raise ValueError("gitleaks refuse les pages de révision :\n    " + "\n    ".join(found))
    for f in old - set(written):
        f.unlink()
        report.append((f.relative_to(DOCS).as_posix(), "retirée"))
    return report


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
            if is_revision(vault, rel):
                print(f"R  {rel}  ->  espace Révision")
                continue
            try:
                dom, cat, title = resolve(vault, rel, tree)
            except ValueError as exc:
                print(f"?  {rel}  ({str(exc).split(' : ', 1)[-1]})")
                continue
            mark = "●" if rel in existing else "○"
            cut = " · découpée" if is_split(read_note(note), title) else ""
            print(f"{mark}  {rel}  ->  {dom}/{cat} · {title}{cut}")
        print("\n● publiée · ○ à publier · R révision · ? --title / --to nécessaires")
        return 0
    if (args.title or args.to) and len(args.notes) != 1:
        ap.error("--title et --to s'utilisent avec une seule note")
    if args.all and args.notes:
        ap.error("--all ou une liste de notes, pas les deux")
    todo = [n.relative_to(vault).as_posix() for n in vault_notes(vault)] if args.all else args.notes
    todo = [rel for rel in todo if not is_revision(vault, rel)]      # publiées dans l'espace Révision
    index = build_index(vault, tree)
    code = 0
    if args.all:                  # d'abord : une note fusionnée peut reprendre le titre (et les pages) d'une archivée
        for src, files in existing.items():
            if not (vault / src).is_file() or is_revision(vault, src):
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
    try:
        for page, note in write_revisions(vault, tree, index):
            print(f"RÉVISION : docs/{page}  [{note}]")
    except ValueError as exc:
        print(f"NON PUBLIÉE : {exc}", file=sys.stderr)
        code = 1
    if todo:
        print("Relire les pages (mkdocs serve), puis committer les fichiers nommés.")
    return code


if __name__ == "__main__":
    sys.exit(main())
