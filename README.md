# Disruptive Intelligence — portail

Site public **https://disruptive-intelligence.github.io/** : veille quotidienne (Morning
Intelligence Brief), analyses, dossiers, wiki Pentest, Bibliothèque, Ressources et Glossaire.
Construit avec [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/),
identité visuelle « Aurore » (sombre et claire).

Les contenus de veille sont **produits par [veille-agent](https://github.com/H4ckeurM4n/veille-agent)**
(dépôt privé) puis copiés ici ; le reste du site est écrit à la main ou généré au build.

## Lancer le site en local

```powershell
python -m venv .venv                               # une seule fois
.\.venv\Scripts\pip install -r requirements.txt    # une seule fois
.\.venv\Scripts\mkdocs serve -a 127.0.0.1:8002
```

Puis ouvrir http://127.0.0.1:8002. Après une modification de `hooks/portal.py`, relancer
`mkdocs serve` (le hook reste en mémoire). Avant un push : `mkdocs build --strict`.

## Structure

| Chemin | Rôle |
|---|---|
| `docs/veille/AAAA/MM/AAAA-MM-JJ.md` | Morning Briefs, publiés par veille-agent (ou déposés en mode secours) |
| `docs/analyses/<slug>.md`, `docs/dossiers/<slug>.md` | Analyses et dossiers, publiés par veille-agent |
| `docs/start/`, `methodology/`, `services/`… | Wiki Pentest, écrit à la main |
| `data/bibliotheque.yml` | Arborescence de la Bibliothèque (miroir des notes Obsidian, notes prévues comprises) |
| `scripts/import_notes.py` | Import des notes Obsidian dans `docs/library/` (liens, images, découpage, masquage IP, gitleaks) — testé par `tests/` |
| `data/ressources.yml` | Ressources de veille (thème > rubrique > liens), à éditer à la main |
| `data/sources.yml` | Sources suivies, générées par `scripts/export_sources.py` depuis `veille-agent/config/feeds.json` |
| `data/glossaire.yml` | Ajouts et corrections manuels du glossaire (prioritaires) |
| `data/redirects.yml` | Anciennes adresses Jekyll → nouvelles pages |
| `hooks/portal.py` | Génère **à chaque build** l'accueil, les index, la navigation, le glossaire, les fils d'actualité, les flux RSS et les redirections |
| `docs/stylesheets/extra.css` | Thème « Aurore » (variables `--kw-*`, déclinaison claire en fin de fichier) |
| `docs/javascripts/` | Masquage de la barre latérale, infobulles du glossaire |
| `overrides/` | En-tête (onglets), balises `<head>` (icônes, flux RSS), page 404 |
| `_preview/` | Maquettes de thèmes (hors site publié) |
| `site/` | Site généré (ignoré par Git) |

## Importer des notes dans la Bibliothèque

```powershell
.\.venv\Scripts\python scripts/import_notes.py --vault ..\CyberSec-notes-v2 --list      # état note -> page
.\.venv\Scripts\python scripts/import_notes.py --vault ..\CyberSec-notes-v2 --all       # routine : tout mettre à jour
.\.venv\Scripts\python scripts/import_notes.py --vault ..\CyberSec-notes-v2 "Cyber/02 OSINT/OSINT — synthèse.md"   # une note
.\.venv\Scripts\python -m unittest discover -s tests                                     # tests du convertisseur
```

Le coffre suit l'arborescence du site : `Domaine/NN Rubrique[/Sous-rubrique]/Titre.md` (dossiers nommés comme
les libellés de `data/bibliotheque.yml`, sans emoji, précédés de leur numéro d'ordre ; « : » s'écrit « - »
dans un nom de fichier). La rubrique et le titre d'une note viennent donc de son emplacement et de son nom ;
une note posée dans un dossier de rubrique est publiée sans rien déclarer. `_archives/` n'est jamais publié.

Formats (propriété Obsidian `format:`, sinon règle automatique) : **cours** (≥ 3 chapitres, parties ou
plus de 120 000 caractères), **synthèse** (le reste, ou « synthèse » dans le titre ; « X — synthèse » se range
sous le cours « X… » de sa rubrique, entrée « En synthèse »), **fiche** (rubrique Fiches notions),
**aide-mémoire** (« aide-mémoire » ou « cheat sheet » dans le titre), **ressources**, **révision**.
Autres propriétés lues : `provenance` (badge, ex. HTB Academy), `niveau`, `objectif`, `prerequis`.
Une fiche déclare ses termes (`termes: {SPF: définition…}`, valeurs entre guillemets si elles contiennent
« : ») : ils entrent au glossaire et leur infobulle, sur tout le site, mène à la fiche. Les glossaires des
cours (sections « Glossaire ») alimentent aussi le glossaire, sans infobulle.
Espace Révision : l'annexe « Questions types d'entretien » d'un cours et les notes du dossier `Révision/`
(propriété `rubrique: cyber/detection`) donnent une page par rubrique dans `docs/library/revision/`.
Non publiés : mini-quiz, registre de cohérence, en-tête de maintenance, journal des modifications.
Dans `data/bibliotheque.yml`, une rubrique liste ses notes (`notes:`) ou les répartit en sous-rubriques
(`groups:` → `label` + `notes`) ; `mots:` relie la rubrique aux analyses et dossiers de la veille.
`--all` (ré)importe chaque note rangée du coffre et retire les pages dont la note a disparu ; ensuite
`mkdocs build --strict`, puis commit des fichiers nommés (`git add docs/library/…`, jamais `git add .`).

- **Conversion** (hors code : `[[ -z $x ]]` en Bash reste intact) : `[[Note]]` et `[[#Titre]]` deviennent de vrais
  liens, les ancres des sommaires écrits à la main suivent le titre réel, images copiées dans
  `docs/library/assets/`, blocs `<details>` rendus en Markdown, surlignage `==…==` et schémas Mermaid.
- **Découpage** : au-delà de 150 000 caractères, la note devient un dossier `<slug>/` (présentation + sommaire
  dans `index.md`, une page par partie ou chapitre) ; le menu l'affiche comme une entrée dépliable.
- **Dépôt public** : IP de lab HackTheBox masquées (10.10.x.y → 10.0.x.y, 10.129.x.y → 10.1.x.y) ; flag, clé
  privée ou vrai jeton = note refusée ; puis gitleaks (s'il est installé) contrôle les pages écrites avec
  `.gitleaks.toml`. Un exemple de cours factice signalé par gitleaks s'ajoute à l'allowlist « Bibliothèque ».
- **Recherche** : l'index global de Material (rechargé à chaque page) ne garde des notes que titres et
  intertitres ; leur texte intégral part dans `search/bibliotheque.json`, lu par la page
  « 🔎 Rechercher dans mes notes » (`/library/recherche/?mots=…`).

## Ce que le hook génère

- **Accueil, pages Veille / Analyses / Dossiers / Ressources / Bibliothèque** et leur navigation,
  à partir des en-têtes des fichiers : aucune liste à tenir à la main.
- **Glossaire** : entrées `- **Terme** — définition` (ou `- **Terme :** définition`) des sections
  « Lexique du jour » des briefs et « Repères pour comprendre le document » des analyses, complétées
  par `data/glossaire.yml`. Sur tout le site, la première occurrence d'un terme est soulignée et
  affiche sa définition au survol ou au toucher (`assets/glossary.json`).
- **Fils d'actualité** (`veille/fils/`) : chaque sujet d'un brief porte un repère
  `<!-- selection: event:evt-… -->` écrit par veille-agent ; dès qu'un même événement apparaît dans
  deux éditions, il reçoit une page chronologique et une pastille « Fil d'actualité » sous le sujet.
- **Sommaire repliable** des 20 sujets en tête de chaque brief (téléphone).
- **Outils de veille** (`veille/`) : Explorer (tous les sujets, filtrables), Pile de lecture (reading
  lists, cases « lu » locales), Agenda (jalons datés d'« À surveiller »), Semaines (sujets par rubrique),
  calendrier des éditions ; badges de fraîcheur, couleurs de rubrique, encadré « L'essentiel ».
- **Analyses et dossiers** : en-tête (nature, thème, auteur, date, durée), métadonnées repliées, et
  liens avec la veille quand l'en-tête déclare `events`.
- **Flux RSS** à contenu complet : `feed.xml` (tout) et `veille/feed.xml` (briefs).
- **Contrôle du contrat éditorial** : un contenu hors contrat fait échouer le build.

## En-tête des contenus de veille (contrat partagé avec veille-agent)

```yaml
---
title: "Morning Intelligence Brief — 28 septembre 2026"
date: 2026-09-28
kind: veille                 # veille | analysis | dossier
---
```

- **Analyse** : `kind: analysis`, `theme` (un seul : `ia | cyber | tech | geo-ie`), `slug` persistant
  identique au nom du fichier ; `author`, `organization`, `tags` facultatifs.
- **Dossier** : `kind: dossier`, `themes` (liste parmi `ia | cyber | tech | geo-ie`), `slug`.
- **Brief** : nom de fichier dérivé de la date, `docs/veille/AAAA/MM/AAAA-MM-JJ.md`.

## Publication

Chaque push sur `main` déclenche `.github/workflows/deploy.yml` : scan de secrets (gitleaks) →
`mkdocs build --strict` → déploiement GitHub Pages sur https://disruptive-intelligence.github.io/.
Retour arrière possible : l'étiquette `jekyll-final` pointe sur le dernier état Jekyll.

## Règles de sécurité

Ce dépôt est **public**. Jamais d'IP réelles de lab, flags, mots de passe, tokens ou données de
machines ; uniquement de la connaissance générique. Le workflow de publication scanne tout
l'historique avec gitleaks (`.gitleaks.toml` : règles par défaut + flags de CTF et IP de lab
HackTheBox, seule exception : `docs/start/conventions.md`) et refuse de déployer en cas de fuite.
