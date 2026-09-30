---
title: Partie VII — Programme CTI ET maturité
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - index.md
---

---


## Chapitre 30 — Construire un programme CTI en entreprise

### 30.1 Prérequis

Un programme CTI ne fonctionne pas dans le vide. Les prérequis : des logs exploitables (si le SOC n'a pas de SIEM avec des logs de qualité, la CTI ne peut pas alimenter des détections), un SOC opérationnel (la CTI tactique et technique n'a de sens que si un SOC les consomme), un RSSI qui comprend la valeur de la CTI (si la direction voit la CTI comme un « nice to have » et non comme un « must have », le budget sera le premier coupé), et une culture de la menace (les équipes IT et métier doivent accepter que l'organisation EST une cible, pas une éventualité).

### 30.2 Modèles d'organisation

**CTI intégrée au SOC :** l'analyste CTI est membre de l'équipe SOC. Avantage : boucle courte CTI → détection, connaissance intime des capacités et des gaps du SOC. Inconvénient : risque d'absorption par l'opérationnel (l'analyste passe son temps à traiter des alertes au lieu de faire de l'analyse de fond).

**CTI dédiée :** équipe séparée du SOC, avec sa propre hiérarchie. Avantage : profondeur d'analyse, capacité de travailler sur des missions de moyen/long terme (profilage, attribution, évaluation stratégique). Inconvénient : risque de déconnexion avec l'opérationnel (la CTI produit des rapports que le SOC ne lit pas).

**Modèle hybride :** équipe CTI dédiée avec un « CTI liaison » intégré au SOC pour la boucle courte. C'est le modèle le plus efficace pour les organisations de taille suffisante (3+ analystes CTI).

### 30.3 Outillage et budget

L'outillage minimal : un TIP (MISP ou OpenCTI — gratuits si auto-hébergés, ~5-20K$/an en SaaS), 1-2 feeds commerciaux prioritaires (Recorded Future ou Mandiant pour la couverture large, Intel 471 ou Flashpoint pour le dark web — 50-150K$/an chacun), et l'intégration SIEM/EDR (connecteurs STIX/TAXII). Le budget analyste est le poste principal : un analyste CTI senior coûte 50-80K€/an en France, un junior 35-50K€. Le ROI se mesure en incidents prévenus, en temps de détection réduit, et en gaps comblés — des métriques traitées au Ch.31.

---


## Chapitre 31 — Métriques et évaluation de la performance CTI

Les métriques de performance CTI sont le mécanisme qui justifie l'investissement et guide l'amélioration continue.

**Métriques de processus :** nombre de PIR adressés (sur le total des PIR actifs), temps moyen de traitement d'un rapport (de la réception à la dissémination), taux de FP des IoC injectés dans le SIEM (objectif : < 5 %), couverture des TTP pertinentes par des détections (% des techniques ATT&CK des acteurs surveillés couvertes par des règles).

**Métriques d'impact :** incidents détectés ou prévenus grâce à la CTI (le renseignement a-t-il conduit à une détection qui n'aurait pas eu lieu sans CTI ?), gaps de détection comblés (combien de nouvelles règles déployées grâce aux recommandations CTI), temps de réponse réduit (l'IR a-t-il été plus rapide grâce au contexte CTI ?), et qualité des attributions (les attributions ont-elles été confirmées ou révisées avec le temps ?).

**Métriques de maturité :** pourcentage des détections basées sur les TTP vs les IoC (plus le % TTP est élevé, plus la CTI est mature — un SOC qui ne détecte que les IoC est au bas de la Pyramid of Pain), diversité des sources (combien de catégories de sources sont couvertes — OSINT seul = immature, OSINT + commercial + interne + communautaire + dark web + technique = mature), et fréquence du feedback (le feedback loop est-il formalisé et régulier, ou inexistant ?).

---


## Chapitre 32 — Veille et intelligence continue

La veille CTI n'est pas un projet ponctuel — c'est un processus quotidien. L'organisation de la veille comprend la consultation des sources prioritaires (adaptée aux PIR — les sources qui répondent aux PIR actifs sont consultées quotidiennement, les autres hebdomadairement), le suivi des vulnérabilités exploitées ITW (CISA KEV mis à jour en continu, EPSS quotidien, alertes CERT-FR — si une CVE affectant une technologie de l'organisation est ajoutée au KEV, c'est un flash alert immédiat), la veille sectorielle (rapports qui concernent le secteur de l'organisation, les technologies utilisées, la géographie), et le suivi des acteurs surveillés (profils d'acteurs mis à jour quand de nouvelles campagnes, TTP, ou infrastructures sont identifiées). Renvoi vers le cours Dark Web pour la veille dark web.

---


## Chapitre 33 — Automatisation, outillage et place réaliste de l'IA

*Ce chapitre traite de l'automatisation et de l'IA avec pragmatisme — en distinguant ce qui est opérationnellement utile aujourd'hui, ce qui est en cours de maturation, et ce qui relève du fantasme.*

### 33.1 Ce qui peut et doit être automatisé

Le **traitement des feeds** est le candidat idéal à l'automatisation : l'ingestion de feeds STIX/TAXII, la normalisation des IoC, l'enrichissement automatisé (hash → VirusTotal, domaine → Whois/passive DNS, IP → géolocalisation/ASN), le dédoublonnage, et le scoring sont des tâches répétitives à haut volume et à faible valeur analytique — elles doivent être automatisées pour libérer du temps analyste. Les orchestrateurs (SOAR : Cortex XSOAR, Shuffle, Tines) et les connecteurs TIP → SIEM (MISP → Splunk, OpenCTI → Sentinel) font ce travail.

L'**injection des IoC** dans les systèmes de détection est automatisable (et doit l'être — un analyste qui copie-colle des IoC dans le SIEM est un gaspillage de compétence). L'**alerting** sur les mentions de l'organisation dans les sources dark web et les feeds commerciaux est automatisable. Et le **reporting automatisé** sur les métriques de processus (dashboards de couverture, volume de feeds traités, taux de FP) est automatisable.

### 33.2 Ce que les LLM apportent concrètement

*(et ce qu'ils n'apportent pas)*

Les LLM (GPT-4, Claude, modèles open source) sont des outils utiles pour l'analyste CTI dans des cas d'usage précis et encadrés. Le **résumé de rapports** : un LLM peut résumer un rapport de 30 pages en 1 page — gain de temps significatif pour la veille quotidienne, à condition que l'analyste vérifie le résumé (les hallucinations existent). La **traduction** : les rapports en chinois, russe, farsi, ou coréen sont directement pertinents pour la CTI — un LLM traduit avec une qualité largement suffisante pour le triage (la traduction finale pour un livrable formel doit être vérifiée par un humain). L'**extraction structurée d'IoC** : extraire les hash, domaines, IP, et techniques ATT&CK d'un rapport narratif vers un format structuré (STIX) est un cas d'usage productif. L'**aide à la rédaction** : un LLM peut aider à structurer un premier jet de note analytique — que l'analyste revoit, corrige, et complète.

Ce que les LLM **n'apportent PAS** (et ne doivent pas être utilisés pour) : l'**analyse structurée** (l'ACH, le Key Assumptions Check, et les TAS sont des processus de raisonnement humain qui nécessitent le jugement, l'expérience, et la connaissance du contexte — un LLM qui remplit une matrice ACH produit un résultat plausible mais potentiellement faux, sans que l'erreur soit détectable), l'**attribution** (un LLM qui « attribue » une campagne à un acteur se base sur des corrélations statistiques dans ses données d'entraînement, pas sur une analyse d'évidences — c'est de la pseudo-analyse dangereusement convaincante), la **formulation de niveaux de confiance** (un LLM ne sait pas ce qu'il ne sait pas — il ne peut pas évaluer honnêtement l'incertitude de ses conclusions), et la **détection des biais** (un LLM n'a pas conscience de ses propres biais de données — il les reproduit silencieusement).

### 33.3 Le risque de la « CTI industrialisée »

L'automatisation poussée à l'extrême crée un risque : la CTI qui produit en volume (des dizaines de rapports par semaine, des milliers d'IoC par jour) mais sans profondeur analytique. Les rapports sont « plausibles » (le LLM écrit bien, les mots sont les bons, les structures sont correctes) mais creux (pas d'analyse réelle, pas d'hypothèses testées, pas de niveaux de confiance calibrés, pas de valeur ajoutée au-delà de ce que le consommateur aurait pu lire lui-même dans les sources). La CTI industrialisée sans analyse est du bruit déguisé en renseignement — et elle est pire que l'absence de CTI, car elle crée une fausse confiance.

La règle : automatiser le traitement (volume, répétitif, faible valeur analytique), assister la production (résumés, traductions, extraction), mais ne jamais automatiser l'analyse (raisonnement, jugement, confiance).

---
