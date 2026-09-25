# Disruptive Intelligence — portail

Veille, analyses, dossiers et wiki technique (pentest, CTF, cyber), construit avec
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Lancer le wiki en local

```powershell
python -m venv .venv                          # une seule fois
.\.venv\Scripts\pip install -r requirements.txt   # une seule fois
.\.venv\Scripts\mkdocs serve
```

Puis ouvrir http://127.0.0.1:8000

## Structure

- `docs/` : contenu Markdown (la source, versionnée)
  - `veille/AAAA/MM/AAAA-MM-JJ.md`, `analyses/`, `dossiers/` : publiés par veille-agent
  - le reste : le wiki (Pentest, Bibliothèque)
- `data/ressources.yml` : ressources de la veille (thème > rubrique > liens), à éditer à la main
- `data/sources.yml` : sources suivies par veille-agent (`scripts/export_sources.py`)
- `hooks/portal.py` : génère **à chaque build** l'accueil, les pages d'index et la navigation
- `mkdocs.yml` : configuration et navigation du wiki
- `site/` : site généré (ignoré par Git)

## En-tête des contenus de veille

```yaml
---
title: "Analyse — Titre"
date: 2026-09-23
kind: analysis        # veille | analysis | dossier
theme: ia             # ia | cyber | tech | ie | geo  (analyses et dossiers)
author: Google DeepMind   # analyses
---
```

## Tester en local avec le contenu de la veille

```powershell
.\.venv\Scripts\python scripts\migrate_jekyll.py --src ..\disruptive-intelligence.github.io --dest docs
```

(Dans ce dépôt de travail, `docs/veille`, `docs/analyses` et `docs/dossiers` sont ignorés par Git.)

## Règle de sécurité

Ce dépôt est **public**. Jamais d'IP réelles de lab, flags, mots de passe, tokens
ou données de machines. Uniquement de la connaissance générique.

## Publication

Chaque push sur `main` déclenche `.github/workflows/deploy.yml` :
scan de secrets (gitleaks) → build strict → publication sur
https://disruptive-intelligence.github.io/wiki_knowledge/

## Garde-fou local

Un hook `pre-commit` (non versionné, dans `.git/hooks/`) lance `gitleaks git --staged`
et bloque tout commit contenant un secret. À réinstaller si le dépôt est recloné.
