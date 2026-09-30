"""Tests de scripts/import_notes.py (conversion Obsidian -> Bibliothèque).

    .venv/Scripts/python -m unittest discover -s tests
"""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import import_notes as imp  # noqa: E402

TREE = [{"id": "it", "label": "IT", "categories": [
    {"id": "scripting", "label": "Scripting", "notes": ["Bash", "Python"]},
    {"id": "culture", "label": "Culture", "notes": ["SQL"]}]}]


class VaultCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / "IT/05_Scripting_Langage-Prog").mkdir(parents=True)
        (self.vault / "IT/Culture").mkdir(parents=True)
        self.write("IT/Culture/SQL.md", "# SQL\n\nDu SQL.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        (self.vault / rel).write_text(text, encoding="utf-8")
        return rel

    def build(self, rel, text):
        self.write(rel, text)
        pages, _, notes = imp.build(self.vault, rel, TREE)
        return pages, notes


class ConversionTests(VaultCase):
    def test_code_keeps_double_brackets(self):
        pages, _ = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                              "# Bash\n\nVoir [[SQL|la note SQL]] et `[[ -n $a ]]`.\n\n"
                              "```bash\nif [[ -z \"$1\" ]]; then exit 1; fi\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn('if [[ -z "$1" ]]; then', body)
        self.assertIn("`[[ -n $a ]]`", body)
        self.assertIn("[la note SQL](../culture/sql.md)", body)

    def test_unknown_wikilink_and_local_link_become_text(self):
        pages, _ = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                              "# Bash\n\n[[Note absente]] et [fichier](annexe.pdf).\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("Note absente et fichier.", body)

    def test_lab_ip_masked_and_flag_refused(self):
        pages, notes = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                                  "# Bash\n\n```\nmount 10.129.12.17:/home ~/nfs\nping 10.10.5.112\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("10.1.12.17", body)
        self.assertIn("10.0.5.112", body)
        self.assertNotIn("10.129.", body)
        self.assertIn("2 IP de lab masquée(s)", notes)
        self.write("IT/05_Scripting_Langage-Prog/Python.md", "# Python\n\nHTB{un_vrai_flag}\n")
        with self.assertRaises(ValueError):
            imp.build(self.vault, "IT/05_Scripting_Langage-Prog/Python.md", TREE)

    def test_headings_title_dropped_and_demoted(self):
        pages, _ = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                              "# Bash\n\nIntro\n\n# Partie 1\n\n## Détail\n\n```\n# commentaire\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertNotIn("\n# Bash", body)
        self.assertIn("## Partie 1", body)
        self.assertIn("### Détail", body)
        self.assertIn("# commentaire", body)            # le code n'est pas un titre

    def test_manual_toc_anchor_follows_mkdocs_slug(self):
        pages, _ = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                              "# Bash\n\n- [Ch.1](#chapitre-1--découverte)\n- [Ch.2](#chapitre-2--boucles-et-tests)\n\n"
                              "## Chapitre 1 — Découverte de Bash\n\ntexte\n\n## Chapitre 2 — Boucles et tests\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("(#chapitre-1-decouverte-de-bash)", body)
        self.assertIn("(#chapitre-2-boucles-et-tests)", body)

    def test_details_blocks_keep_markdown(self):
        pages, _ = self.build("IT/05_Scripting_Langage-Prog/Bash.md",
                              "# Bash\n\n<details>\n<summary>Réseau</summary>\n\n> citation\n\n</details>\n")
        self.assertIn('<details markdown="1">', pages["library/it/scripting/bash.md"])


class SplitTests(VaultCase):
    def test_long_note_split_by_parts_with_cross_page_anchors(self):
        filler = "Lorem ipsum dolor sit amet. " * 200
        text = ("# SQL\n\nPrésentation.\n\n## Table des matières\n\n- [Filtrer](#chapitre-3--filtrer-avec-where)\n\n"
                f"# PARTIE I — Bases\n\n{filler}\n\n# Chapitre 1 — Pourquoi\n\n{filler}\n\n"
                f"# Chapitre 2 — Modèle\n\n{filler}\n\n# PARTIE II — Lire\n\n{filler}\n\n"
                f"# Chapitre 3 — Filtrer avec WHERE\n\nVoir [le début](#chapitre-1--pourquoi).\n\n{filler}\n")
        with mock.patch.object(imp, "SPLIT_AT", 1000), mock.patch.object(imp, "MIN_SECTION", 100):
            pages, notes = self.build("IT/Culture/SQL.md", text)
        paths = list(pages)
        self.assertEqual(paths[0], "library/it/culture/sql/index.md")
        self.assertEqual(len(paths), 3)                  # présentation + 2 parties
        self.assertIn("2 pages", notes)
        index, part1, part2 = (pages[p] for p in paths)
        self.assertIn("## Sommaire", index)
        self.assertIn("(2-partie-ii-lire.md#chapitre-3-filtrer-avec-where)", index)   # sommaire manuel suivi
        self.assertIn("title: PARTIE II — Lire", part2)
        self.assertIn("chapter: 2", part2)
        self.assertIn("(1-partie-i-bases.md#chapitre-1-pourquoi)", part2)

    def test_many_small_chapters_one_page_each(self):
        filler = "texte " * 600
        text = "# Python\n\n" + "".join(f"# Chapitre {i} — Sujet {i}\n\n{filler}\n\n" for i in range(1, 6))
        with mock.patch.object(imp, "SPLIT_AT", 1000):
            pages, _ = self.build("IT/05_Scripting_Langage-Prog/Python.md", text)
        self.assertEqual(len(pages), 6)
        chapter = pages["library/it/scripting/python/1-chapitre-1-sujet-1.md"]
        self.assertNotIn("## Chapitre 1", chapter)      # le titre de section est devenu celui de la page

    def test_split_entry_matches_link_index(self):
        with mock.patch.object(imp, "SPLIT_AT", 10):
            index = imp.build_index(self.vault, TREE)
        self.assertEqual(index["sql"], "library/it/culture/sql/index.md")


if __name__ == "__main__":
    unittest.main()
