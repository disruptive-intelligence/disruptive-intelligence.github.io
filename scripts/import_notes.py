"""Importe des notes Obsidian (CyberSec-notes) dans la Bibliothèque du portail.

    python scripts/import_notes.py --vault ../CyberSec-notes --list
    python scripts/import_notes.py --vault ../CyberSec-notes Cyber/01_CTI/CTI.md [autres notes…]
    python scripts/import_notes.py --vault ../CyberSec-notes IT/Culture/SQL.md --title "SQL" --to it/culture

Seules les notes nommées sur la ligne de commande sont importées : rien n'est publié par défaut.
Pour chaque note :
  - rubrique déduite du dossier du coffre (Cyber/01_CTI -> cyber/cti…), ou --to dom/cat ;
  - titre = la note prévue dans data/bibliotheque.yml la plus proche du nom de fichier
    (elle remplace alors la page « Pas encore importée »), ou --title ;
  - [[Lien|alias]] -> texte, ![[image.png]] et images locales -> copiées dans docs/library/assets/ ;
  - contrôle de sécurité : un flag de CTF, une IP de lab, une clé privée ou un mot de passe
    en clair empêche l'import de cette note (le dépôt est public).
Le script écrit docs/library/<domaine>/<catégorie>/<slug>.md, sans commit : relire, puis committer.
"""
import argparse
import difflib
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
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
LEAKS = [
    ("flag de CTF", re.compile(r"(?i)\b(?:HTB|THM|flag)\{[^}\s]{4,}\}")),
    ("IP de lab HackTheBox", re.compile(r"\b10\.(?:10|129)\.\d{1,3}\.\d{1,3}\b")),
    ("clé privée", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("mot de passe en clair", re.compile(r"(?i)\b(?:password|passwd|mot de passe|pwd)\s*[:=]\s*\S{6,}")),
    ("jeton ou clé d'API", re.compile(r"\b(?:ghp_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})\b")),
]
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def slug(text):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
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


def find_in_vault(vault, name):
    hits = [p for p in vault.rglob(name) if ".obsidian" not in p.parts]
    return hits[0] if hits else None


def convert(text, source, vault, assets_rel):
    """Syntaxe Obsidian -> Markdown standard ; renvoie (texte, images à copier)."""
    images = []

    def asset(found):
        """Nom unique dans docs/library/assets : note + image, sans espace."""
        name = f"{slug(source.stem)}-{slug(found.stem)}{found.suffix.lower()}"
        images.append((found, name))
        return f"{assets_rel}/{name}"

    def embed(m):
        target = m.group(1).split("|")[0].strip()
        found = find_in_vault(vault, target) if Path(target).suffix.lower() in IMAGE_EXT else None
        if not found:
            return f"*{target}*"
        return f"![{found.stem}]({asset(found)})"

    def local_image(m):
        alt, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", target):
            return m.group(0)
        found = (source.parent / target.replace("%20", " ")).resolve()
        if not found.is_file():
            found = find_in_vault(vault, Path(target).name)
        if not found:
            return f"*{alt or target}*"
        return f"![{alt}]({asset(found)})"

    text = re.sub(r"%%.*?%%", "", text, flags=re.S)                       # commentaires Obsidian
    text = re.sub(r"!\[\[([^\]]+)\]\]", embed, text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", local_image, text)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)            # [[Note|alias]] -> alias
    text = re.sub(r"\[\[([^\]#|]+)(?:#[^\]]*)?\]\]", r"\1", text)          # [[Note]] -> Note
    return text, images


def leaks(text):
    found = []
    for label, pattern in LEAKS:
        for m in pattern.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append(f"ligne {line} : {label}")
    return found


def import_note(vault, rel, tree, title=None, to=None):
    source = vault / rel
    if not source.is_file():
        raise ValueError(f"note introuvable : {rel}")
    dom, cat = to.split("/") if to else (category_of(Path(rel)) or (None, None))
    if not dom:
        raise ValueError(f"{rel} : rubrique inconnue, préciser --to domaine/catégorie")
    title = title or TITLES.get(Path(rel).as_posix())
    if not title:
        score, title = guess_title(source, planned(tree, dom, cat))
        if not title or score < 0.45:
            raise ValueError(f"{rel} : aucune note prévue ne correspond dans {dom}/{cat} "
                             f"(meilleur score {score:.2f}), préciser --title")
    body = source.read_text(encoding="utf-8-sig")
    problems = leaks(body)
    if problems:
        raise ValueError(f"{rel} : import refusé (dépôt public) :\n    " + "\n    ".join(problems))
    folder = DOCS / "library" / dom / cat
    body, images = convert(body, source, vault, "../../assets")
    body = re.sub(r"\A---\n.*?\n---\n", "", body, flags=re.S)             # ancien en-tête éventuel
    front = yaml.safe_dump({"title": title}, allow_unicode=True, sort_keys=False)
    target = folder / f"{slug(title)}.md"
    folder.mkdir(parents=True, exist_ok=True)
    target.write_bytes(f"---\n{front}---\n\n{body.strip()}\n".encode("utf-8"))
    for image, name in images:
        (DOCS / "library/assets").mkdir(parents=True, exist_ok=True)
        shutil.copy2(image, DOCS / "library/assets" / name)
    return target, title, len(images)


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", type=Path, required=True, help="dossier du coffre Obsidian (CyberSec-notes)")
    ap.add_argument("--list", action="store_true", help="afficher la correspondance note -> page prévue, sans rien écrire")
    ap.add_argument("--title", help="titre de la note (une seule note)")
    ap.add_argument("--to", help="domaine/catégorie, ex. cyber/cti (une seule note)")
    ap.add_argument("notes", nargs="*", help="chemins relatifs au coffre")
    args = ap.parse_args(argv)
    tree = yaml.safe_load((ROOT / "data/bibliotheque.yml").read_text(encoding="utf-8"))
    vault = args.vault.resolve()
    if args.list:
        for note in sorted(p for p in vault.rglob("*.md") if ".obsidian" not in p.parts and p.parent != vault):
            rel = note.relative_to(vault)
            if note.name in SKIP:
                continue
            dom, cat = category_of(rel) or (None, None)
            if not dom:
                print(f"?  {rel.as_posix()}  (rubrique à préciser avec --to)")
                continue
            score, title = ((1.0, TITLES[rel.as_posix()]) if rel.as_posix() in TITLES
                            else guess_title(note, planned(tree, dom, cat)))
            done = (DOCS / "library" / dom / cat / f"{slug(title)}.md").is_file() if title else False
            mark = "●" if done else ("○" if title and score >= .45 else "?")
            print(f"{mark}  {rel.as_posix()}  ->  {dom}/{cat} · {title or '—'} ({score:.2f})")
        print("\n● importée · ○ correspondance trouvée · ? --title / --to nécessaires")
        return 0
    if (args.title or args.to) and len(args.notes) != 1:
        ap.error("--title et --to s'utilisent avec une seule note")
    code = 0
    for rel in args.notes:
        try:
            target, title, n = import_note(vault, rel, tree, args.title, args.to)
            print(f"IMPORTÉE : {rel} -> {target.relative_to(ROOT).as_posix()} « {title} »"
                  + (f" ({n} image(s))" if n else ""))
        except (OSError, ValueError) as exc:
            print(f"NON IMPORTÉE : {exc}", file=sys.stderr)
            code = 1
    if code == 0 and args.notes:
        print("Relire les pages (mkdocs serve), puis committer les fichiers nommés un par un.")
    return code


if __name__ == "__main__":
    sys.exit(main())
