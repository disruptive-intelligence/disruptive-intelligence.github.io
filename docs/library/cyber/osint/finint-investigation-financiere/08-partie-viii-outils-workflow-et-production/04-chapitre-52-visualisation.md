---
title: Chapitre 52 — Visualisation
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VIII — Outils, workflow et production
  - index.md
---

Maltego, i2, Linkurious, Gephi, Graphistry

## Objectif du chapitre

Maîtriser les **outils de visualisation** pour construire des graphes relationnels FININT exploitables.

## Catalogue raisonné

**Maltego** : standard OSINT depuis 15+ ans. Forces : transforms multiples (intégrations natives avec dizaines de sources), modélisation de graphes, exploration interactive. Versions : Community (gratuite, limitée), Pro, Enterprise.

**i2 Analyst’s Notebook (IBM)** : standard du renseignement institutionnel et police. Forces : analyse de cas complexes, modèles temporels, intégration avec bases policières. Lourd à prendre en main mais très puissant. Coût élevé.

**Linkurious Enterprise** : plateforme web-based, backend Neo4j. Forces : exploration interactive grands graphes, collaboration multi-utilisateurs, audit. Adopté par certaines CRF et banques.

**Gephi** : open source, orienté analyse de données (centralités, communautés, layout). Excellent pour les graphes statiques de présentation.

**Graphistry** : web-based, accélération GPU pour très grands graphes. Forces : performance, exploration interactive, intégration analytique.

**Cytoscape** : open source, à l’origine biologique, utilisable pour réseaux financiers.

**Neo4j** : base de données graphe utilisée comme backend de plusieurs outils. Requêtes Cypher pour l’analyse.

**Excel / Power BI** : pour les analyses simples ou les présentations exécutives. Sous-estimé par les analystes techniques.

## Méthode — choix d’outil par contexte

- **Exploration interactive, peu de nœuds (< 100)** : Maltego.
- **Cas complexe institutionnel, intégration policière** : i2.
- **Très grand graphe (1000+)** : Linkurious ou Graphistry.
- **Présentation finale propre** : Gephi (export image), Linkurious.
- **Analyse de centralités, communautés** : Gephi.
- **Public exécutif, simple** : Excel / PowerBI.

## L’utilité opérationnelle

Le bon outil :

- **Accélère** la construction du graphe.
- **Permet la calculation** des métriques (centralité, communautés).
- **Communique** efficacement le résultat.

Le mauvais outil :

- **Ralentit** le travail (limites de performance).
- **Cache** la complexité (graphe illisible).
- **Trompe** par mauvais layout.

## Erreurs fréquentes

- **Penser que la visualisation prouve quelque chose.** Elle illustre.
- **Surcharger** le graphe : 200 nœuds visibles = illisible.
- **Ne pas annoter** les arcs et les nœuds : ambiguïté.

## Limites

Aucun outil ne fait l’analyse — l’analyste pose les bonnes questions et interprète.

## Lien avec le fil rouge

> **CLEARFLOW — Linkurious pour le dossier**
> 
> Le dossier Haddad, avec ~40 nœuds principaux, est construit dans Linkurious (licence du service). Maltego sert pour l’exploration initiale, Gephi pour le graphe final présentable. Le travail visualisation prend environ 1 jour cumulé.

## Points clés à retenir

- Maltego (OSINT standard), i2 (institutionnel), Linkurious (web grand graphe), Gephi (analyse + présentation), Graphistry (GPU).
- Choix par contexte.
- La visualisation illustre, ne prouve pas.

-----
