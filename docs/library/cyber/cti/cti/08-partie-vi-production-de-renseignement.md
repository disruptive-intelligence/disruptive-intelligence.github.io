---
title: Partie VI — Production de renseignement
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - index.md
---

*La partie la plus opérationnelle : comment écrire les livrables CTI — du flash alert au rapport stratégique annuel.*

---


## Chapitre 26 — Les produits CTI : formats, audiences, temporalités

Cartographie complète des livrables CTI. Le **flash alert** (urgence — 0-day exploitée, campagne active ciblant l'organisation, fuite de données confirmée) : 1 page maximum, faits + impact + actions immédiates, diffusion sous 1-2 heures, audience : toute l'équipe sécurité. Le **daily/weekly brief** (résumé des menaces pertinentes de la période) : 1-2 pages, tendances + incidents notables + CVE exploitées + IoC pertinents, audience : SOC manager, RSSI. La **note tactique** (analyse de TTP avec détections) : 3-5 pages, mapping ATT&CK + procédures spécifiques + règles Sigma + recommandations de hunting, audience : analystes SOC, hunters, ingénieurs de détection. Le **rapport de campagne** (analyse approfondie d'une campagne) : 10-20 pages, acteur + TTP + IoC + victimologie + timeline + attribution + recommandations, audience : équipe sécurité, pairs communautaires. Le **profil d'acteur** (dossier complet) : document vivant, 15-30 pages, toutes les composantes du Ch.15, audience : référence long terme, communauté. Le **rapport stratégique** (évaluation de menace sectorielle) : 5-10 pages, tendances + acteurs + risques + recommandations business, audience : RSSI, direction, board. L'**évaluation de risque basée sur la menace** : 5-10 pages, menaces concrètes × exposition × recommandations priorisées, audience : RSSI, risk managers.

---


## Chapitre 27 — Rédiger une note analytique CTI

### 27.1 La structure

**Résumé exécutif** (5 lignes maximum) : conclusion principale + niveau de confiance + implication + action recommandée. C'est souvent le seul élément lu par le décideur — il doit être autonome. Exemple : « Nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU (Sandworm). L'acteur cible systématiquement les opérateurs d'énergie européens avec un objectif de pré-positionnement dans les réseaux SCADA. Nous recommandons le déploiement des détections jointes en annexe et un audit de segmentation IT/OT dans les 30 jours. »

**Contexte :** pourquoi cette note, quel événement déclencheur, quel PIR adressé, quelles sources consultées, et quelles limitations (qu'est-ce que l'analyste n'a PAS pu vérifier).

**Faits observés :** chaque fait avec sa source et son évaluation de fiabilité (cotation Admiralty). La distinction fait/déduction est explicite.

**Analyse :** hypothèses testées (ACH ou équivalent), corrélations multi-sources, raisonnement explicite (pas juste les conclusions — le chemin qui y mène). Le lecteur doit pouvoir évaluer la qualité du raisonnement, pas seulement la conclusion.

**Conclusions :** avec niveaux de confiance explicites pour chaque affirmation clé. Les inconnues sont documentées.

**Implications et recommandations :** actions priorisées — techniques (IoC, détections Sigma, hunts), organisationnelles (posture, audit, formation), et stratégiques (communication, notification, budget).

**Annexes :** IoC complets (format STIX si possible), mapping ATT&CK, captures d'écran horodatées, références des sources.

### 27.2 La discipline rédactionnelle

Phrases courtes (une idée par phrase). Pas de jargon non défini (chaque acronyme est développé à sa première occurrence). Chaque affirmation est sourcée (entre parenthèses ou en note). Chaque conclusion est qualifiée par un niveau de confiance. Le test de la note : si le résumé exécutif est lu seul, donne-t-il au décideur ce dont il a besoin pour agir ? Si la réponse est non, le résumé doit être réécrit.

---


## Chapitre 28 — Rédiger un profil d'acteur et cartographier une campagne

### 28.1 Le profil d'acteur comme document vivant

Un profil d'acteur n'est pas un rapport ponctuel — c'est un document vivant mis à jour à chaque nouvelle information. La structure est celle du Ch.15 (identité, sponsor, objectifs, victimologie, TTP, outils, infrastructure, campagnes, évolution). Chaque section est datée et sourcée. Les mises à jour sont versionnées (v1.0 lors de la création, v1.1 après enrichissement communautaire, v2.0 après attribution révisée). Le profil est stocké dans le TIP (OpenCTI) avec les relations vers les IoC, les campagnes, et les malwares associés.

### 28.2 Le rapport de campagne

Le rapport de campagne reconstitue et documente une série d'incidents liés. La timeline (de la première activité observée à la dernière — avec les lacunes explicites), le mapping des victimes (qui a été touché, dans quel ordre, avec quel vecteur — la victimologie est le cœur du rapport), l'infrastructure (domaines, IP, certificats — et leur évolution dans le temps), les TTP (cohérence ou variations entre incidents), et l'attribution (avec son niveau de confiance et ses limitations). Le rapport de campagne est le livrable de référence pour la communauté — il est partagé via l'ISAC ou en TLP:GREEN/AMBER pour que d'autres organisations puissent se protéger.

---


## Chapitre 29 — Étude critique de livrables CTI

*Ce chapitre examine des exemples de livrables CTI — bons et mauvais — pour développer le sens critique rédactionnel de l'analyste.*

### 29.1 Ce qui fait un bon rapport CTI

Un bon rapport CTI : pose une question de renseignement claire (pas « voici ce qu'on a trouvé » mais « voici la réponse à votre question »), distingue explicitement les faits, les déductions, et les hypothèses, qualifie chaque conclusion par un niveau de confiance, source chaque affirmation, présente les hypothèses alternatives testées (pas juste la conclusion retenue — le lecteur doit voir que les alternatives ont été considérées), documente les limitations et les inconnues, et formule des recommandations actionnables (pas « soyez vigilants » mais « déployez la règle Sigma suivante sur les postes d'ingénieurs OT »).

### 29.2 Les erreurs rédactionnelles les plus fréquentes

**L'affirmation sans niveau de confiance :** « UNC-VOLT est un groupe du GRU. » → pas de qualification. Devrait être : « Nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU, basé sur... ». **La confusion IoC = renseignement :** un rapport qui liste 200 hash sans contexte n'est pas du renseignement — c'est un dump de données. **Le résumé qui ne résume pas :** un résumé exécutif de 2 pages avec du jargon technique n'est pas un résumé. **L'attribution sur un seul indice :** « un domaine C2 est hébergé sur le même ASN qu'une campagne Sandworm précédente → donc c'est Sandworm » — un ASN est partagé par des milliers de clients, ce n'est pas un indice d'attribution. **Le rapport alarmiste sans évidences :** « MENACE CRITIQUE — votre organisation est ciblée par un APT étatique » basé sur un post de forum non vérifié.

### 29.3 Exercice d'analyse critique

Le chapitre présente 3 extraits de rapports CTI (anonymisés, inspirés de rapports réels) que l'analyste doit critiquer : identifier les forces (sources multiples, niveaux de confiance explicites, hypothèses alternatives), les faiblesses (affirmations non sourcées, sauts logiques, attribution excessive), et les améliorations possibles. Cet exercice développe le sens critique qui distingue l'analyste consommateur passif de rapports (il lit et transmet) de l'analyste producteur actif de renseignement (il évalue, critique, et produit mieux).

---
