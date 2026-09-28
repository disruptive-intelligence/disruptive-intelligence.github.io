"""Exporte les sources actives de veille-agent vers data/sources.yml.

Usage :
    python scripts/export_sources.py --feeds ../veille-agent/config/feeds.json

Seules les informations publiques sont exportées : nom du média, site, groupes, alias.
(À terme, veille-agent pourra écrire ce fichier lui-même à chaque publication.)
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

import yaml


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--feeds", required=True)
    ap.add_argument("--out", default=Path(__file__).parent.parent / "data" / "sources.yml")
    args = ap.parse_args()

    feeds = json.loads(Path(args.feeds).read_text(encoding="utf-8"))["feeds"]
    # Une source par média (display_name) ; les intitulés bruts des flux restent en alias,
    # car les anciens briefs les citent encore.
    by_name = {}
    for f in feeds:
        if not f.get("enabled"):
            continue
        name = (f.get("display_name") or f["name"]).strip()
        s = by_name.setdefault(name, {"name": name,
                                      "site": "{0.scheme}://{0.netloc}".format(urlparse(f["url"])),
                                      "groups": [], "aliases": []})
        s["groups"] += [g for g in f.get("source_groups", []) if g not in s["groups"]]
        if f["name"].strip() != name and f["name"].strip() not in s["aliases"]:
            s["aliases"].append(f["name"].strip())
    sources = [{k: v for k, v in s.items() if v or k != "aliases"} for s in by_name.values()]
    Path(args.out).write_bytes((
        "# Généré par scripts/export_sources.py — sources actives de veille-agent.\n"
        + yaml.safe_dump(sources, allow_unicode=True, sort_keys=False)).encode("utf-8"))   # LF, comme le dépôt
    print(f"{len(sources)} sources -> {args.out}")


if __name__ == "__main__":
    main()
