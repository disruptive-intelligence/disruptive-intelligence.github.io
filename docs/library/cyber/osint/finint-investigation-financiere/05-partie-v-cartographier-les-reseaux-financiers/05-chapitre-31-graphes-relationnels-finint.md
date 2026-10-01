---
title: Chapitre 31 — Graphes relationnels FININT
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Comprendre la **représentation graphique** d’un réseau financier : nœuds (personnes, entités, actifs, flux), arcs (liens typés), et les usages opérationnels de cette représentation.

## Le concept

Un graphe relationnel FININT est une représentation visuelle d’un réseau. Les **nœuds** sont des entités (personnes, sociétés, comptes, actifs, transactions). Les **arcs** (ou arêtes) sont les liens (capital, mandat, virement, propriété, etc.).

Les arcs sont typés : capital, mandat, paiement, propriété, parenté, adresse partagée. Chaque type a sa logique et son intensité.

**Outils** :

- **Maltego** : référence pour l’OSINT et le FININT, transforms multiples.
- **i2 Analyst’s Notebook** : standard du renseignement, lourd mais puissant.
- **Linkurious** : web-based, neo4j-backed, professionnel.
- **Gephi** : open source, analytique (centralités, communautés).
- **Graphistry** : web-based, GPU-accelerated, exploration interactive.
- **Neo4j** : base de données graphe sous-jacente.
- **Outils intégrés à Sayari, Orbis, Dow Jones** : graphes pré-construits sur leur référentiel.

## L’utilité opérationnelle

Le graphe permet :

- **Détection de patterns** : clusters, structures en étoile, chaînes longues, ponts.
- **Identification de nœuds centraux** : qui est le « hub » du réseau ? — souvent l’UBO réel.
- **Détection de liens cachés** : ponts entre clusters apparemment indépendants.
- **Présentation visuelle** : un graphe bien construit communique en quelques secondes ce qui exige des pages de description.

## Méthode — construire un graphe FININT

1. **Définir le périmètre** : périmètre initial (entités cibles), puis périmètres d’extension.
1. **Choisir les types de nœuds et d’arcs** :
- Nœuds : personnes, sociétés, comptes bancaires, adresses physiques, actifs significatifs, transactions clés.
- Arcs : capital (avec %), mandat (avec rôle), UBO (avec niveau de confiance), virement (avec montant et date), parenté (conjoint, enfant, fratrie), adresse partagée, employeur, contact réseau social.
1. **Charger les données** depuis les fiches (Ch.27-30) et les sources.
1. **Annoter** : libeller chaque arc avec son type, sa date, son intensité.
1. **Calculer des métriques** quand pertinent : centralité (degré, betweenness), communautés (Louvain), shortest paths.
1. **Itérer** : enrichir, déplacer, simplifier pour lisibilité.

## Mini-walkthrough — graphe CLEARFLOW (description)

Le graphe central du dossier Haddad compte ~40 nœuds (14 sociétés, 12 personnes physiques, 11 actifs, et quelques nœuds techniques de transaction). Une fois construit dans Linkurious avec les liens typés, les patterns suivants émergent visuellement :

- **Cluster français** (4 SAS + dirigeants prête-noms probables) — fortement connecté en interne, faiblement à l’extérieur sauf via 1 arc capital vers le cluster chypriote.
- **Cluster chypriote** (NEXUS HOLDINGS + trust OMEGA) — au sommet, avec arc UBO probable vers Karim Haddad.
- **Cluster émirats / asiatique** (sociétés free zone, contacts à Dubaï) — autour de M. Y (PSC des Limited UK).
- **Branche Liban** — entités libanaises, faiblement visible mais positionnée à l’origine.
- **Branche Afrique de l’Ouest** (Bénin, Côte d’Ivoire) — débouchés opérationnels.
- **Karim Haddad** au centre : nœud de plus haute centralité dans le graphe (intuition confirmée par calcul de betweenness).

Cette représentation, présentée en réunion, communique en quelques secondes ce que 30 pages de note racontent.

## Erreurs fréquentes

- **Graphe trop chargé** : illisible. Limiter à 30-50 nœuds visibles à la fois.
- **Arcs non typés** : ambiguïté.
- **Pas de date** : un lien actuel et un lien obsolète sont traités à l’identique.
- **Confondre forte connexité et causalité** : un nœud central peut être un facilitateur, pas un contrôleur.

## Limites

Le graphe **résume** ; il ne **prouve** pas. Une représentation peut renforcer une hypothèse erronée si les nœuds sont mal qualifiés. Il doit accompagner une analyse écrite, jamais la remplacer.

## Lien avec le fil rouge

> **CLEARFLOW — Le graphe en réunion de bilan**
> 
> Lors de la réunion de bilan du dossier, Nassim présente le graphe en première intention. En 2 minutes, le coordinateur et les collègues comprennent la structure du réseau, l’architecture du contrôle, et les zones d’incertitude. Le graphe accompagne la note dans le dossier transmis au PNF.

## Points clés à retenir

- Graphe = représentation, pas preuve.
- Nœuds + arcs typés + dates + niveaux de confiance.
- Outils : Maltego, i2, Linkurious, Gephi, Graphistry.
- Métriques utiles : centralité (qui est central ?), communautés (clusters ?).

-----
