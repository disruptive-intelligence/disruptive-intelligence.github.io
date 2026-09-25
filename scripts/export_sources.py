"""Exporte les sources actives de veille-agent vers data/sources.yml.

Usage :
    python scripts/export_sources.py --feeds ../veille-agent/config/feeds.json

Seules les informations publiques sont exportées : nom, site, groupes.
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
    sources = [{"name": f["name"].strip(),
                "site": "{0.scheme}://{0.netloc}".format(urlparse(f["url"])),
                "groups": f.get("source_groups", [])}
               for f in feeds if f.get("enabled")]
    Path(args.out).write_text(
        "# Généré par scripts/export_sources.py — sources actives de veille-agent.\n"
        + yaml.safe_dump(sources, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"{len(sources)} sources -> {args.out}")


if __name__ == "__main__":
    main()
