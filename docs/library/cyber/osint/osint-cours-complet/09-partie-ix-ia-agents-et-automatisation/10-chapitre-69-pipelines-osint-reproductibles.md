---
title: Chapitre 69 — Pipelines OSINT reproductibles
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 69.1 Du script ad hoc au pipeline

L'analyste débutant écrit des scripts ad hoc. L'analyste mature construit des **pipelines reproductibles** : workflows structurés, versionnés, documentés, ré-exécutables.

Bénéfices :

- Reproductibilité (un confrère ré-exécute).
- Capitalisation (modèles réutilisables).
- Auditabilité.
- Qualité (tests, validation).

## 69.2 Architecture pipeline type

**Étapes typiques pour pipeline OSINT.**

1. **Collecte** : APIs, scraping, captures.
2. **Stockage brut** : données collectées préservées.
3. **Nettoyage / structuration** : déduplication, formatting.
4. **Enrichissement** : croisements, pivots.
5. **Analyse** : agrégations, statistiques, patterns.
6. **Visualisation** : graphes, dashboards.
7. **Production** : génération de rapports.

Chaque étape : input, traitement, output, log.

## 69.3 Outils

**Scrapy.** Framework Python pour scraping structuré. Production-ready.

**Apache Airflow.** Orchestration de workflows. Standard data engineering.

**dbt** (Data Build Tool). Transformations SQL versionnées.

**Snakemake.** Workflow management bioinformatique-style.

**Jupyter Notebook.** Pour investigation interactive avec narrative.

**Pandas.** Standard data manipulation.

**Polars** : alternative pandas moderne, plus rapide.

**NetworkX.** Graphes.

**RapidFuzz.** Entity resolution / fuzzy matching.

## 69.4 Entity resolution

Le **entity resolution** (résolution d'entités) consiste à fusionner les références à la même entité dans différents documents.

**Cas.**

- « Marc Delaunay » et « M. Delaunay » et « Mr. Marc H. Delaunay » → même entité.
- « TechnoVert SAS » et « Technovert » et « TechnoVert France » → même entité.

**Outils.**

- **RapidFuzz** : fuzzy matching strings.
- **dedupe.io** (Python library) : entity resolution structurée.
- **Splink** : pour grands volumes.

## 69.5 Pipeline exemple : monitoring de domaines

**Objectif.** Monitorer 50 domaines suspects pour changements.

**Pipeline.**

```
Étape 1 — Collecte (quotidienne)
  - Pour chaque domaine : WHOIS, DNS records, certificats, contenu page.
  - Stockage : SQLite local + captures Hunchly.

Étape 2 — Comparaison
  - Diff avec snapshot précédent.
  - Détection des changements.

Étape 3 — Alerte
  - Si changement significatif : email/Signal/Slack à analyste.

Étape 4 — Rapport hebdomadaire
  - Synthèse des changements de la semaine.
  - Visualisations.
```


**Implémentation.** Python + cron + SQLite + Hunchly.

## 69.6 Versioning et Git

**Tout pipeline est versionné en Git local.**

**Discipline.**

- Commits réguliers.
- Messages explicites.
- Branches par fonctionnalité.
- Tags par versions stables.
- Backup chiffré du repo.

## 69.7 Tests et qualité

**Unit tests** sur fonctions critiques.

**Integration tests** sur pipelines end-to-end (avec données test).

**Validation continue** : pipeline qui échoue silencieusement = pipeline dangereux.

## 69.8 Documentation

**README** par projet.

**Notebooks documentés** (Markdown intercalé avec code).

**Modèles de prompts** versionnés.

## 69.9 Pipeline MIRAGE type

Pour MIRAGE, plusieurs pipelines :

**Pipeline 1 : Enrichissement entités.**

- Input : liste d'entités identifiées.
- Pour chaque entité : recherches automatisées (WHOIS, Sherlock, Hunter, Pappers).
- Output : fiches entités structurées.

**Pipeline 2 : Monitoring cluster désinformation.**

- Input : liste de comptes coordonnés identifiés.
- Quotidien : capture nouveaux posts, archivage, alerte si activité.

**Pipeline 3 : Synthèse rapport.**

- Input : graphe entités + journal d'enquête.
- Output : draft rapport markdown.

## 69.10 Synthèse — maturation de l'analyste

| Niveau analyste | Approche |
|---|---|
| Débutant | Outils manuels |
| Intermédiaire | Scripts ad hoc |
| Avancé | Pipelines reproductibles versionnés |
| Expert | Agents + knowledge graphs + automation structurée |

L'objectif n'est pas d'automatiser pour automatiser, mais de **scaler** la rigueur méthodologique. Une enquête bien automatisée est plus rigoureuse, plus rapide, plus défendable qu'une enquête manuelle.

> **Principe Partie IX.** L'IA et l'automatisation transforment **comment** on conduit l'OSINT, pas **ce qu'est** l'OSINT. La discipline méthodologique, la cotation, la formulation calibrée, la responsabilité humaine restent les piliers. L'IA accélère et augmente — mais elle s'inscrit dans le même cadre éthique et professionnel.

-----
