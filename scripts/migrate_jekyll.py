"""Migre le contenu Jekyll de la veille vers la structure MkDocs du portail.

Usage :
    python scripts/migrate_jekyll.py --src ../disruptive-intelligence.github.io --dest docs

- Briefs    : veille/AAAA/MM/AAAAMMJJ_*.md -> docs/veille/AAAA/MM/AAAA-MM-JJ.md
- Analyses  : analyses/*.md                -> docs/analyses/<slug-du-titre>.md
- Dossiers  : dossiers/*.md                -> docs/dossiers/<slug-du-titre>.md

Le front matter est normalisé (title, date, kind, theme, author) à partir de
scripts/migration_metadata.yml. Les balises Liquid de Jekyll sont converties
en liens Markdown classiques. Le dépôt source n'est jamais modifié.
"""
import argparse
import re
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def split_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def dest_path(meta, src):
    kind, date = meta["kind"], meta["date"]
    if kind == "veille":
        return Path("veille") / f"{date:%Y}" / f"{date:%m}" / f"{date:%Y-%m-%d}.md"
    title = re.sub(r"^Analyse\s*—\s*", "", str(meta["title"]))
    folder = "analyses" if kind == "analysis" else "dossiers"
    return Path(folder) / f"{slug(title)}.md"


def convert_liquid(body, own_dest, path_map):
    """{% assign aN = site.pages | where: 'path', 'X.md' %} + {{ aN.url }} -> lien relatif."""
    assigns = dict(re.findall(r"{%\s*assign (\w+) = site\.pages \| where: 'path', '([^']+)'.*?%}", body))
    for var, src_path in assigns.items():
        target = path_map.get(src_path)
        link = Path("../" * (len(own_dest.parts) - 1)) / target if target else "#"
        body = re.sub(r"{{\s*" + var + r"\.url \| relative_url\s*}}", Path(link).as_posix(), body)
    body = re.sub(r"{%.*?%}\n?", "", body)
    body = re.sub(r"{{\s*'/'\s*\|\s*relative_url\s*}}", "../index.md", body)
    return re.sub(r"{{.*?}}", "", body)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--src", required=True, help="dépôt Jekyll de la veille")
    ap.add_argument("--dest", required=True, help="dossier docs/ du portail")
    ap.add_argument("--metadata", default=HERE / "migration_metadata.yml")
    ap.add_argument("--redirects", help="fichier YAML des redirections à compléter (ex. data/redirects.yml)")
    args = ap.parse_args()

    src, dest = Path(args.src), Path(args.dest)
    extra = yaml.safe_load(Path(args.metadata).read_text(encoding="utf-8"))

    sources = sorted([*src.glob("veille/**/*.md"), *src.glob("analyses/*.md"), *src.glob("dossiers/*.md")])
    entries = []
    for f in sources:
        if f.name == "index.md":
            continue
        meta, body = split_front_matter(f.read_text(encoding="utf-8"))
        if meta.get("kind") not in ("veille", "analysis", "dossier"):
            continue
        meta.update(extra.get(f.name, {}))
        entries.append((f, meta, body, dest_path(meta, f)))

    path_map = {f.relative_to(src).as_posix(): d.as_posix() for f, _, _, d in entries}

    # Anciennes adresses Jekyll (page.md -> page.html) -> nouveaux fichiers, pour les redirections
    if args.redirects:
        old = {}
        if Path(args.redirects).exists():
            old = yaml.safe_load(Path(args.redirects).read_text(encoding="utf-8")) or {}
        old.update({p[:-3] + ".html": d for p, d in path_map.items()})
        Path(args.redirects).parent.mkdir(parents=True, exist_ok=True)
        Path(args.redirects).write_text(
            "# Anciennes adresses du site Jekyll -> page du portail (redirections générées par hooks/portal.py)\n"
            + yaml.safe_dump(dict(sorted(old.items())), allow_unicode=True, width=300), encoding="utf-8")
        print(f"{len(old)} redirections -> {args.redirects}")
    for f, meta, body, d in entries:
        fm = {k: meta[k] for k in ("title", "date", "kind", "theme", "author") if k in meta}
        out = dest / d
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n"
                       + convert_liquid(body, d, path_map), encoding="utf-8", newline="\n")
        print(f"{f.relative_to(src).as_posix():70} -> {d.as_posix()}")
    print(f"{len(entries)} fichiers migrés.")


if __name__ == "__main__":
    main()
