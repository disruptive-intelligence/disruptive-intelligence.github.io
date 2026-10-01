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

# Libellés avec emoji, dossiers du coffre numérotés : « IT/07 Scripting/ » = « ⌨️ Scripting »
TREE = [{"id": "it", "label": "💻 IT", "categories": [
    {"id": "scripting", "label": "⌨️ Scripting", "notes": ["Bash", "Python"]},
    {"id": "culture", "label": "🧠 Culture", "notes": ["SQL"]}]}]
SCRIPTING, CULTURE = "IT/07 Scripting", "IT/09 Culture"


class VaultCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / SCRIPTING).mkdir(parents=True)
        (self.vault / CULTURE).mkdir(parents=True)
        self.write(f"{CULTURE}/SQL.md", "# SQL\n\nDu SQL.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        (self.vault / rel).parent.mkdir(parents=True, exist_ok=True)
        (self.vault / rel).write_text(text, encoding="utf-8")
        return rel

    def build(self, rel, text):
        self.write(rel, text)
        pages, _, notes = imp.build(self.vault, rel, TREE)
        return pages, notes


class VaultLayoutTests(VaultCase):
    def test_category_from_folders_and_title_from_file_name(self):
        self.assertEqual(imp.resolve(self.vault, f"{SCRIPTING}/Bash.md", TREE), ("it", "scripting", "Bash"))
        self.assertEqual(imp.resolve(self.vault, f"{SCRIPTING}/Sous-rubrique/Python.md", TREE),
                         ("it", "scripting", "Python"))
        # note pas encore déclarée dans data/bibliotheque.yml : titre = nom du fichier
        self.assertEqual(imp.resolve(self.vault, f"{CULTURE}/Shell - pipes et filtres.md", TREE),
                         ("it", "culture", "Shell - pipes et filtres"))
        with self.assertRaises(ValueError):
            imp.resolve(self.vault, "Autre/Note.md", TREE)

    def test_archives_and_root_files_not_listed(self):
        self.write("_archives/Vieille note.md", "# Vieille\n")
        self.write("README.md", "# Coffre\n")
        names = [p.name for p in imp.vault_notes(self.vault)]
        self.assertNotIn("Vieille note.md", names)
        self.assertNotIn("README.md", names)

    def test_stray_rule_is_not_front_matter(self):
        text = "---\n\n# Annexe\n\n- **Question :** quoi ?\n\n---\n\nSuite.\n"
        self.assertEqual(imp.front_matter(text), ({}, text))
        props, body = imp.front_matter("---\nformat: fiche\n---\n# Titre\n")
        self.assertEqual((props, body), ({"format": "fiche"}, "# Titre\n"))


class ConversionTests(VaultCase):
    def test_code_keeps_double_brackets(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "# Bash\n\nVoir [[SQL|la note SQL]] et `[[ -n $a ]]`.\n\n"
                              "```bash\nif [[ -z \"$1\" ]]; then exit 1; fi\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn('if [[ -z "$1" ]]; then', body)
        self.assertIn("`[[ -n $a ]]`", body)
        self.assertIn("[la note SQL](../culture/sql.md)", body)

    def test_unknown_wikilink_and_local_link_become_text(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", "# Bash\n\n[[Note absente]] et [fichier](annexe.pdf).\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("Note absente et fichier.", body)

    def test_lab_ip_masked_and_flag_refused(self):
        pages, notes = self.build(f"{SCRIPTING}/Bash.md",
                                  "# Bash\n\n```\nmount 10.129.12.17:/home ~/nfs\nping 10.10.5.112\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("10.1.12.17", body)
        self.assertIn("10.0.5.112", body)
        self.assertNotIn("10.129.", body)
        self.assertIn("2 IP de lab masquée(s)", notes)
        self.write(f"{SCRIPTING}/Python.md", "# Python\n\nHTB{un_vrai_flag}\n")
        with self.assertRaises(ValueError):
            imp.build(self.vault, f"{SCRIPTING}/Python.md", TREE)

    def test_headings_title_dropped_and_demoted(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "# Bash\n\nIntro\n\n# Partie 1\n\n## Détail\n\n```\n# commentaire\n```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertNotIn("\n# Bash", body)
        self.assertIn("## Partie 1", body)
        self.assertIn("### Détail", body)
        self.assertIn("# commentaire", body)            # le code n'est pas un titre

    def test_manual_toc_anchor_follows_mkdocs_slug(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "# Bash\n\n- [Ch.1](#chapitre-1--découverte)\n- [Ch.2](#chapitre-2--boucles-et-tests)\n\n"
                              "## Chapitre 1 — Découverte de Bash\n\ntexte\n\n## Chapitre 2 — Boucles et tests\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("(#chapitre-1-decouverte-de-bash)", body)
        self.assertIn("(#chapitre-2-boucles-et-tests)", body)

    def test_details_blocks_keep_markdown(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "# Bash\n\n<details>\n<summary>Réseau</summary>\n\n> citation\n\n</details>\n")
        self.assertIn('<details markdown="1">', pages["library/it/scripting/bash.md"])


class HeadingTests(VaultCase):
    def test_first_heading_kept_when_not_the_note_title(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", "# Définitions de base\n\nTexte.\n\n## Concept\n\nSuite.\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("## Définitions de base", body)   # vraie section (fiche HTB), pas un titre de note
        self.assertIn("### Concept", body)

    def test_lone_top_heading_of_a_long_note_is_its_title(self):
        long = "".join(f"## Section {i}\n\n{'mot ' * 1000}\n\n" for i in range(1, 6))
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", f"# NETWORKING\n\n{long}")
        self.assertNotIn("NETWORKING", "".join(pages.values()))

    def test_course_title_dropped_and_subtitle_becomes_lead(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "# Cours complet de scripting Bash\n\n## De zéro à l'automatisation\n\n"
                              "Prérequis : aucun.\n\n## Glossaire\n\nmots\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertNotIn("Cours complet", body)
        self.assertIn("*De zéro à l'automatisation*", body)
        self.assertIn("## Glossaire", body)

    def test_sentence_headings_are_shortened_and_levels_rebased(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "### Kill chain\n\n#### 1. Reconnaissance : But de l'attaquant : collecter des infos "
                              "publiques sur la cible avant l'attaque\n\ntexte\n\n"
                              "#### Network/Host artifacts (ex : clés de registre, chemins, mutex, patterns réseau)\n\n"
                              "#### Chapitre 34 — Cas complet : profilage et attribution d'un cluster inconnu (MERIDIAN)\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("## Kill chain", body)
        self.assertIn("### 1. Reconnaissance\n\nBut de l'attaquant : collecter", body)
        self.assertIn("### Network/Host artifacts\n\n*(ex : clés de registre", body)
        self.assertIn("### Chapitre 34 — Cas complet : profilage et attribution", body)   # début trop vague : gardé entier

    def test_all_caps_titles_recased(self):
        acronyms = imp.acronyms_of("Le SOC et la CTI. ET voilà.")
        self.assertEqual(imp.tidy_title("PARTIE IV — PROFILAGE D'ACTEUR ET ATTRIBUTION", acronyms),
                         "Partie IV — Profilage d'acteur et attribution")
        self.assertEqual(imp.tidy_title("PARTIE V — CTI OPÉRATIONNELLE : DE L'INTELLIGENCE À L'ACTION", acronyms),
                         "Partie V — CTI opérationnelle : de l'intelligence à l'action")
        self.assertEqual(imp.tidy_title("PARTIE IV — CORÉE DU NORD, IRAN ET AUTRES ACTEURS", acronyms),
                         "Partie IV — Corée du Nord, Iran et autres acteurs")
        self.assertEqual(imp.tidy_title("PARTIE II — ADMINISTRATION WINDOWS LOCALE", acronyms),
                         "Partie II — Administration Windows locale")

    def test_lists_code_and_html_images_are_spaced_and_converted(self):
        (self.vault / "assets").mkdir()
        (self.vault / "assets/iam.png").write_bytes(b"\x89PNG")
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "## IAAA\n**IAAA** regroupe :\n- **Identification** ;\n- **Authentication**.\n"
                              '<img src="../../assets/iam.png" alt="IAM" width="550">\nExemples :\n- username ;\n'
                              "```\nUser\n```\n> citation\n- étape\n    ```bash\n    ls\n    ```\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("regroupe :\n\n- **Identification**", body)
        self.assertIn('![IAM](../../assets/bash-iam.png){ width="550" }', body)
        self.assertIn("Exemples :\n\n- username ;\n\n```\nUser\n```\n\n> citation", body)
        self.assertIn("- étape\n    ```bash\n    ls\n    ```", body)       # code d'une liste : indentation gardée

    def test_format_automatic_and_fiche_terms(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", "## DNS\n\ntexte\n")
        self.assertIn("format: synthese", pages["library/it/scripting/bash.md"])
        course = "".join(f"## Chapitre {i} — Sujet\n\n{'mot ' * 900}\n\n" for i in range(1, 4))
        pages, _ = self.build(f"{SCRIPTING}/Python.md", course)
        self.assertIn("format: cours", pages["library/it/scripting/python/index.md"])
        pages, _ = self.build(f"{CULTURE}/SQL.md", "---\nformat: fiche\ntermes:\n  SQL: Langage de requête.\n---\n# SQL\n\nTexte.\n")
        page = pages["library/it/culture/sql.md"]
        self.assertIn("format: fiche", page)
        self.assertIn("terms:\n  SQL: Langage de requête.", page)
        self.assertNotIn("termes:", page.split("---", 2)[2])            # propriétés Obsidian : pas dans le texte

    def test_heading_gaps_closed(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", "## A\n\n#### A1\n\n#### A2\n\n### A3\n\n## B\n\n##### B1\n")
        body = pages["library/it/scripting/bash.md"]
        self.assertIn("## A\n\n### A1\n\n### A2\n\n### A3\n\n## B\n\n### B1", body)

    def test_provenance_formats_and_optional_properties(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              "---\nformat: atelier\nprovenance: HTB Academy\nniveau: débutant\n"
                              "objectif: écrire un premier script\n---\n## Variables\n\ntexte\n")
        page = pages["library/it/scripting/bash.md"]
        for expected in ("format: atelier", "provenance: HTB Academy", "niveau: débutant",
                         "objectif: écrire un premier script", "revue: '20"):
            self.assertIn(expected, page)


class SplitTests(VaultCase):
    FILLER = "Lorem ipsum dolor sit amet. " * 130

    def course(self):
        f = self.FILLER
        return ("# SQL et bases de données\n\n## Prérequis\n\nAucun.\n\n## Fil rouge : Opération Nexus\n\n"
                f"{f}\n\n## Table des matières\n\n- [Filtrer](#chapitre-3--filtrer-avec-where)\n\n"
                f"## PARTIE I — Bases\n\nIntro de la partie.\n\n### Chapitre 1 — Pourquoi\n\n{f}\n\n"
                f"### Chapitre 2 — Modèle\n\n#### Détail\n\n```sql\n{'SELECT nom, prenom FROM clients;' * 100}\n```\n\n"
                f"## PARTIE II — Lire\n\n### Chapitre 3 — Filtrer avec WHERE\n\nVoir [le début](#chapitre-1--pourquoi).\n\n{f}\n\n"
                f"## Annexe A — Glossaire\n\n{f}\n\n## Annexe B — Ressources\n\n{f}\n")

    def test_course_parts_chapters_and_annexes(self):
        pages, notes = self.build(f"{CULTURE}/SQL.md", self.course())
        paths = [p.replace("library/it/culture/sql/", "") for p in pages]
        self.assertEqual(paths, ["index.md",
                                 "01-partie-i-bases/index.md",
                                 "01-partie-i-bases/01-chapitre-1-pourquoi.md",
                                 "01-partie-i-bases/02-chapitre-2-modele.md",
                                 "02-partie-ii-lire/index.md",
                                 "02-partie-ii-lire/01-chapitre-3-filtrer-avec-where.md",
                                 "03-annexes/index.md",
                                 "03-annexes/01-annexe-a-glossaire.md",
                                 "03-annexes/02-annexe-b-ressources.md"])
        index = pages["library/it/culture/sql/index.md"]
        self.assertIn("## Prérequis", index)                  # présentation : prérequis, fil rouge
        self.assertIn("## Fil rouge : Opération Nexus", index)
        self.assertNotIn("Table des matières", index)         # remplacée par le sommaire
        self.assertIn("- [PARTIE I — Bases](01-partie-i-bases/index.md)\n"
                      "    - [Chapitre 1 — Pourquoi](01-partie-i-bases/01-chapitre-1-pourquoi.md)", index)
        part = pages["library/it/culture/sql/01-partie-i-bases/index.md"]
        self.assertIn("Intro de la partie.", part)
        self.assertIn("## Dans cette partie", part)
        chapter = pages["library/it/culture/sql/02-partie-ii-lire/01-chapitre-3-filtrer-avec-where.md"]
        self.assertIn("(../01-partie-i-bases/01-chapitre-1-pourquoi.md)", chapter)
        self.assertIn("- - SQL\n  - ../index.md\n- - PARTIE II — Lire\n  - index.md", chapter)   # fil d'Ariane
        self.assertNotIn("## Chapitre 3", chapter)             # le titre est devenu celui de la page
        short = pages["library/it/culture/sql/01-partie-i-bases/02-chapitre-2-modele.md"]
        self.assertIn("## Détail", short)                      # chapitre court (presque que du code) gardé

    def test_intermediate_review_stays_in_its_part(self):
        f = self.FILLER
        text = ("# Partie I — Bases\n\n" + "".join(f"# Chapitre {i} — Sujet {i}\n\n{f}\n\n" for i in (1, 2))
                + f"# Bilan intermédiaire\n\n{f}\n\n# Chapitre 3 — Sujet 3\n\n{f}\n\n# Partie II — Suite\n\n"
                + f"# Chapitre 4 — Sujet 4\n\n{f}\n\n# Conclusion\n\n{f}\n")
        pages, _ = self.build(f"{CULTURE}/SQL.md", text)
        self.assertIn("library/it/culture/sql/01-partie-i-bases/04-chapitre-3-sujet-3.md", pages)

    def test_cheat_sheet_stays_one_page(self):
        text = "".join(f"## Chapitre {i} — Commandes\n\n{self.FILLER}\n\n" for i in range(1, 5))
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", text)
        self.assertEqual(len(pages), 5)                         # cours : présentation + 4 chapitres
        pages, _ = self.build(f"{SCRIPTING}/Python — cheat sheet.md", text)
        self.assertEqual(len(pages), 1)

    def test_parts_split_small_sections_not_and_quiz_and_scaffold_dropped(self):
        f = "texte " * 350
        sections = "".join(f"## {i}. Sujet {i}\n\n{f}\n\n" for i in range(1, 7))
        pages, _ = self.build(f"{SCRIPTING}/Bash.md",
                              f"# Partie 1 — DNS\n\n{sections}# Partie 2 — HTTP\n\n{sections}"
                              "## 33. Mini-quiz (15 questions)\n\nQ1 ?\n\n"
                              "## Registre de cohérence — fin de T1\n\nRenvois vers des chapitres non rédigés.\n")
        self.assertEqual([p.rsplit("/", 1)[-1] for p in pages], ["index.md", "01-partie-1-dns.md", "02-partie-2-http.md"])
        self.assertNotIn("Mini-quiz", "".join(pages.values()))
        self.assertNotIn("Registre de cohérence", "".join(pages.values()))
        small = "".join(f"## {i}. Point {i}\n\n{'mot ' * 250}\n\n" for i in range(1, 30))   # 29 × ~1 000 car.
        pages, _ = self.build(f"{SCRIPTING}/Python.md", small)
        self.assertEqual(list(pages), ["library/it/scripting/python.md"])            # fiche : une page

    def test_split_entry_matches_link_index(self):
        self.write(f"{CULTURE}/SQL.md", self.course())
        index = imp.build_index(self.vault, TREE)
        self.assertEqual(index["sql"], "library/it/culture/sql/index.md")


class RevisionTests(VaultCase):
    ANNEX = ("# Annexe — Questions types d'entretien et réponses types\n\n## Questions essentielles\n\n"
             "- **Question :** Pourquoi `set -e` ?\n  - **Réponse type :** Pour s'arrêter à la première erreur.\n")

    def test_interview_annex_leaves_the_course_for_the_revision_space(self):
        pages, _ = self.build(f"{SCRIPTING}/Bash.md", f"# Bash\n\n## Variables\n\ntexte\n\n{self.ANNEX}")
        page = pages["library/it/scripting/bash.md"]
        self.assertNotIn("Questions types", page)
        self.assertIn("revision: library/revision/scripting.md", page)
        self.write(f"{CULTURE}/Mémo.md", "---\nformat: revision\n---\n# Mémo\n\n## Réseau\n\n- **Question :** DNS ?\n")
        self.write("Révision/Cryptographie — questions.md",
                   "---\nformat: revision\nrubrique: it/scripting\n---\n" + self.ANNEX.replace("set -e", "AES"))
        self.assertTrue(imp.is_revision(self.vault, f"{CULTURE}/Mémo.md"))
        groups = imp.revision_sources(self.vault, TREE, {})
        self.assertEqual([s[1] for s in groups[("it", "scripting")]], ["Bash", "Cryptographie — questions"])
        self.assertIn((None, "Mémo"), groups)
        with tempfile.TemporaryDirectory() as docs, mock.patch.object(imp, "DOCS", Path(docs)), \
                mock.patch.object(imp, "gitleaks", lambda files: []):
            imp.write_revisions(self.vault, TREE, {})
            page = (Path(docs) / "library/revision/scripting.md").read_text(encoding="utf-8")
        self.assertIn("title: Révision — Scripting", page)
        self.assertIn("## Bash\n\n*D'après le cours [Bash](../it/scripting/bash.md)*", page)
        self.assertIn("### Questions essentielles", page)
        self.assertIn("`set -e`", page)
        self.assertIn("## Cryptographie — questions", page)


if __name__ == "__main__":
    unittest.main()
