---
title: 'Chapitre 26 — Produire un Cyber Threat Landscape opérationnel : workflow complet'
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE VI — Prospective et mise en pratique opérationnelle
  - index.md
---

## 26.1 — Workflow de bout en bout

La production d'un CTL opérationnel suit un workflow en huit étapes : (1) cadrage (périmètre, audience, PIR), (2) plan de collecte (sources, fréquence, responsables), (3) collecte quotidienne (monitoring des sources), (4) traitement et normalisation (STIX 2.1, enrichissement), (5) analyse (identification des tendances, assessments, corrélations), (6) rédaction (structure, langage analytique, visualisations), (7) validation (revue par les pairs, approbation hiérarchique), (8) dissémination (TLP, format, canaux).

Le workflow est itératif : le feedback de l'audience (étape 9) alimente la prochaine itération du cadrage.

## 26.2 — Outils et plateformes

Les plateformes CTI constituent l'infrastructure technique de la production CTL. **MISP** (Malware Information Sharing Platform) est la plateforme de partage d'IOCs la plus déployée dans la communauté CERT, gratuite et open source. Sa force est l'interopérabilité et la communauté. Sa limite est la courbe d'apprentissage et le besoin de maintenance. **OpenCTI** est une plateforme d'analyse structurée, également open source, conçue pour la gestion du renseignement CTI au-delà du simple partage d'IOCs. **TheHive** est une plateforme de gestion d'incidents qui s'intègre avec MISP et Cortex pour l'enrichissement automatisé.

Les feeds OSINT incluent les blogs techniques des éditeurs de sécurité (Mandiant/Google TI, Microsoft MSTIC/MTAC, CrowdStrike, Recorded Future, SentinelOne), les publications des CERT nationaux (CERT-FR, CERT-EU, CISA), et les flux communautaires (AlienVault OTX, Abuse.ch). Les sources commerciales (Mandiant Advantage, Recorded Future, CrowdStrike Falcon Intelligence) apportent des données exclusives mais à un coût significatif.

## 26.3 — Rédaction du livrable

La rédaction du CTL exige un langage analytique calibré. Les assessments doivent utiliser les WEP de manière cohérente. Les sources doivent être citées ou référencées. Les niveaux de confiance doivent être explicites. Les visualisations (graphiques, matrices, heatmaps) doivent clarifier, pas décorer.

La structure type d'un CTL professionnel inclut : un executive summary (1-2 pages), une section méthodologique (périmètre, sources, limites), une analyse par catégorie de menace (acteurs étatiques, cybercrime, hacktivisme, menaces émergentes), une analyse sectorielle, des recommandations priorisées, et des annexes techniques (IOCs, TTPs, références).

## 26.4 — Maintenir un CTL vivant

Un CTL n'est pas un document figé. La fréquence de mise à jour dépend de l'audience et de la volatilité du paysage de menace : annuel pour le rapport de référence, trimestriel pour les mises à jour sectorielles, mensuel ou ad hoc pour les flash reports sur les menaces émergentes. Le versioning et la traçabilité des changements sont essentiels pour la crédibilité.

## 26.5 — Erreurs classiques et faux positifs

Les erreurs les plus fréquentes dans la production CTL incluent : le **biais de confirmation** (chercher les données qui confirment l'hypothèse initiale), le **sensationnalisme** (surévaluer les menaces spectaculaires au détriment des menaces silencieuses), les **conclusions prématurées** (attribuer trop tôt avec trop peu de données), le **cherry-picking** (sélectionner les sources qui confirment le narratif désiré), et l'**overconfidence** (présenter des assessments à faible confiance comme des certitudes).

Le garde-fou principal est la **revue par les pairs** — un analyste qui relit le travail d'un autre avec un regard critique. La culture de la contradiction constructive est un marqueur de maturité des équipes CTI.

## 26.6 — 🔴 Fil rouge : livraison du CTL v1 et bilan

> **📌 FIL ROUGE — Épisode 26**
>
> En décembre 2025, Sophie livre le CTL v1 d'EuroDefense. Le document fait 85 pages (version technique) et 12 pages (executive summary). Il couvre les 12 mois écoulés, intègre l'incident majeur traversé, et formule 15 recommandations priorisées P0/P1/P2.
>
> Bilan à 12 mois : Sophie a transformé un CERT réactif (pas de CTL, pas de méthodologie, pas de framework) en capacité d'anticipation structurée (méthodologie formalisée, sources diversifiées, framework d'analyse, livrables déclinés par audience, intégration dans la gouvernance). Elle planifie la v2 trimestrielle pour mars 2026, avec un focus sur les menaces supply chain SaaS et l'impact de l'IA générative.
>
> Le RSSI Marc Vidal : « Il y a un an, on ne savait même pas qui nous menaçait. Aujourd'hui, on a un CTL qui informe nos arbitrages budgétaires, nos audits NIS2 et nos relations avec nos sous-traitants. La prochaine étape, c'est d'intégrer cette intelligence dans nos systèmes de détection en temps réel. »

> **🎯 CAPSTONE Partie VI** : Produire un mini-CTL sectoriel (5-8 pages) pour le secteur aéronautique/défense/spatial, en format professionnel : executive summary, méthodologie, analyse par catégorie de menace (acteurs étatiques, cybercrime, menaces émergentes), 5 recommandations priorisées, et annexe IOCs/TTPs. Le CTL doit utiliser un langage analytique calibré (WEP, LCA) et citer ses sources.

---
