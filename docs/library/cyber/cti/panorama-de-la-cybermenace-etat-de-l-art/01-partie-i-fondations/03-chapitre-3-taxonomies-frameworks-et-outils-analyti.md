---
title: Chapitre 3 — Taxonomies, frameworks et outils analytiques
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE I — Fondations
  - index.md
---

## 3.1 — La taxonomie ENISA des menaces

La classification des menaces est le squelette structurant de tout CTL. Sans taxonomie cohérente, les données collectées ne peuvent être ni organisées, ni comparées dans le temps, ni corrélées entre sources. La taxonomie ENISA des menaces, établie en 2016 et mise à jour en 2022, est la référence européenne. Elle classe les menaces en grandes catégories : ransomware, malware, ingénierie sociale, menaces contre les données, menaces contre la disponibilité (DDoS), manipulation de l'information, attaques sur la supply chain, et menaces liées à la compromission de comptes.

L'ENISA note que cette taxonomie est actuellement en révision « pour développer un cadre plus mature et actionnable ». Cette révision est motivée par l'évolution du paysage de menace : certaines catégories se chevauchent (un ransomware est aussi un malware), certaines menaces émergentes (IA offensive, compromission de modèles) ne rentrent pas proprement dans les catégories existantes, et la granularité actuelle ne permet pas toujours une analyse opérationnelle fine.

Pour le praticien, la taxonomie est un outil — pas une fin en soi. L'important est de choisir une taxonomie, de l'appliquer de manière cohérente, et de documenter les écarts lorsque les données ne rentrent pas proprement dans les catégories. La comparabilité dans le temps (pouvoir comparer le CTL de cette année avec celui de l'année dernière) exige une stabilité taxonomique que les révisions fréquentes peuvent compromettre.

Le CERT-EU a développé sa propre taxonomie des catégories de menace dans son framework CTI, organisée en plusieurs niveaux. Au niveau le plus élevé, les « threat domains » distinguent le cyberespionnage et prépositionnement, le cybercrime, le hacktivisme, les opérations d'information, et les activités opportunistes. Cette distinction par finalité (plutôt que par technique) est particulièrement pertinente pour la communication avec les décideurs, qui raisonnent en termes de motivations et d'impacts plutôt que de vecteurs techniques.

## 3.2 — Le framework CTI du CERT-EU

Le Cyber Threat Intelligence Framework du CERT-EU, publié en 2025, mérite une attention particulière car il définit les standards analytiques et opérationnels utilisés pour classifier, évaluer et prioriser les activités malveillantes pertinentes pour les institutions de l'Union.

Le concept central est celui de **Malicious Activity of Interest (MAI)** — une activité malveillante qui satisfait les critères de pertinence pour les constituants du CERT-EU et leur écosystème. Le MAI est l'unité de base de l'analyse : chaque activité malveillante observée est qualifiée (ou non) comme MAI, puis classifiée, évaluée et priorisée selon le framework.

Le framework introduit plusieurs dimensions structurantes. Les **niveaux de menace** (threat levels) évaluent la gravité de la menace sur une échelle définie. Les **niveaux d'acteurs** (threat actor levels) évaluent la sophistication et les ressources de l'acteur. Le **scoring** combine ces dimensions pour prioriser la réponse. L'ensemble est conçu pour permettre la « Full-Spectrum Adversary Approach » — une approche de défense informée par la menace qui couvre à la fois les dimensions stratégiques et techniques.

Le framework définit également les secteurs d'intérêt, alignés sur les secteurs NIS2 (énergie, transport, finance, santé, etc.) plus des secteurs additionnels pertinents pour les institutions de l'UE (diplomatie, défense, administration parlementaire, droits fondamentaux, etc.). Cette liste sectorielle structure l'analyse et la classification des MAI.

> **💡 Implication opérationnelle** : le framework CERT-EU est un excellent modèle pour toute organisation souhaitant formaliser sa propre approche CTI. Ses principes — MAI comme unité de base, scoring multi-dimensionnel, secteurs d'intérêt définis, niveaux de confiance explicites — sont transposables à n'importe quel contexte.

## 3.3 — MITRE ATT&CK comme grille structurante des TTPs

MITRE ATT&CK est une base de connaissances des tactiques et techniques adverses fondée sur des observations réelles. Organisée en matrices (Enterprise, Mobile, ICS), elle structure les TTPs en tactiques (le « pourquoi » — l'objectif tactique de l'attaquant) et en techniques (le « comment » — les moyens utilisés pour atteindre cet objectif).

La force d'ATT&CK réside dans sa granularité et sa factualité : chaque technique est documentée avec des exemples réels, des procédures de détection et des mesures de mitigation. Cela en fait un outil de travail quotidien pour les analystes CTI, les detection engineers et les red teamers.

Dans le contexte d'un CTL, ATT&CK sert de grille de structuration des TTPs observés. Plutôt que de décrire les techniques d'un acteur dans un texte libre, l'analyste les mappe sur les techniques ATT&CK, ce qui permet la comparaison entre acteurs, la traçabilité dans le temps, et l'opérationnalisation dans les règles de détection.

Les limites d'ATT&CK doivent être connues. Le framework décrit le « quoi » mais pas le « comment exact » — deux acteurs peuvent utiliser la même technique ATT&CK de manière très différente. Le framework est principalement centré sur l'Enterprise IT et couvre moins bien les environnements OT, cloud-natif et spatial — même si les matrices ICS et Cloud existent. Enfin, ATT&CK est un framework descriptif, pas prédictif : il dit ce que les attaquants ont fait, pas ce qu'ils feront.

Pour le secteur spatial, des adaptations spécifiques existent : le framework SPARTA (Space Attack Research & Tactic Analysis) de l'Aerospace Corporation et le ESA SPACE-SHIELD, tous deux basés sur MITRE ATT&CK mais adaptés au domaine spatial.

## 3.4 — STIX 2.1 et TAXII : représentation et échange normalisés

STIX (Structured Threat Information eXpression) est le standard de représentation de la CTI développé par l'OASIS CTI Technical Committee. Publié comme standard OASIS en 2021, STIX 2.1 est un langage (et une ontologie) qui décrit les cyber-menaces et les observables associés de manière cohérente et machine-readable.

STIX 2.1 intègre d'autres frameworks : les TTPs sont structurées selon MITRE ATT&CK, les indicateurs techniques sont enrichis par des observables standardisés, et les relations entre entités (acteur → utilise → malware → cible → secteur) sont formalisées dans un graphe exploitable programmatiquement.

TAXII (Trusted Automated Exchange of Intelligence Information) est le mécanisme de transport associé à STIX. Il définit comment les données STIX sont échangées entre systèmes — typiquement via des serveurs TAXII qui exposent des collections de données auxquelles les consommateurs peuvent s'abonner.

Pour le praticien, STIX/TAXII est le format de référence pour toute CTI machine-readable. Les plateformes CTI (MISP, OpenCTI) supportent nativement STIX 2.1, et les feeds commerciaux sont de plus en plus disponibles dans ce format. Le bénéfice principal est l'interopérabilité : des données STIX produites par un CERT national peuvent être consommées automatiquement par les systèmes de détection d'une entreprise, sans intervention humaine.

## 3.5 — Cyber Kill Chain, Diamond Model : complémentarités et limites

La **Cyber Kill Chain** (Lockheed Martin) modélise l'attaque comme une séquence de phases : reconnaissance, armement, livraison, exploitation, installation, commande et contrôle, actions sur objectif. Son intérêt est la linéarité : elle permet de visualiser une attaque comme un processus séquentiel et d'identifier les points d'interception possibles à chaque étape. Sa limite est justement cette linéarité : les attaques modernes sont rarement séquentielles et impliquent souvent des itérations, des pivots et des retours en arrière.

Le **Diamond Model** (Caltagirone, Pendergast, Betz) modélise l'intrusion comme un losange à quatre sommets : adversaire, capacité, infrastructure, victime. Chaque intrusion est décrite par la relation entre ces quatre éléments. L'intérêt du Diamond Model est sa capacité à modéliser les relations entre acteurs et à structurer l'analyse d'attribution. Sa limite est son abstraction : il décrit la structure d'une intrusion mais pas sa dynamique.

Ces frameworks sont complémentaires avec MITRE ATT&CK. La Kill Chain donne la vision séquentielle, le Diamond Model donne la vision relationnelle, et ATT&CK donne la vision granulaire des techniques. Un analyste CTI expérimenté utilise les trois, en fonction du besoin analytique.

## 3.6 — L'EUVD : un nouvel outil de coordination pan-européen (2025)

L'European Union Vulnerability Database (EUVD), lancée en 2025, est un nouvel outil de coordination pan-européen pour la gestion des vulnérabilités. Complémentaire du catalogue KEV (Known Exploited Vulnerabilities) de la CISA américaine et du système CVE du NIST, l'EUVD vise à fournir une perspective européenne sur les vulnérabilités exploitées, en intégrant les signalements des CERT nationaux européens et les obligations de notification prévues par NIS2 et le CRA.

Pour le praticien, l'EUVD s'inscrit dans un écosystème de gestion des vulnérabilités qui inclut : le CVE (identification), le CVSS (scoring de sévérité), l'EPSS (probabilité d'exploitation), le KEV CISA (confirmation d'exploitation active), et désormais l'EUVD (perspective européenne). L'articulation entre ces outils est un enjeu opérationnel : prioriser les vulnérabilités en combinant leur sévérité technique (CVSS), leur probabilité d'exploitation (EPSS) et leur exploitation confirmée (KEV/EUVD) est significativement plus efficace qu'un simple classement par score CVSS.

## 3.7 — 🔴 Fil rouge : Sophie choisit ses frameworks

> **📌 FIL ROUGE — Épisode 3**
>
> Sophie doit arbitrer entre couverture et exploitabilité. Elle présente à son équipe CERT le choix des frameworks pour le CTL d'EuroDefense :
>
> — **Taxonomie** : taxonomie ENISA adaptée au périmètre EuroDefense, avec ajout de catégories spatiales issues du Space Threat Landscape 2025.
> — **Structuration des TTPs** : MITRE ATT&CK (Enterprise + ICS), complété par SPARTA pour les systèmes spatiaux.
> — **Scoring de confiance** : code Admiralty avec le seuil CERT-EU (A1, A2, B1, B2 uniquement).
> — **Classification des acteurs** : niveaux d'acteurs du framework CERT-EU.
> — **Représentation machine-readable** : STIX 2.1, partagé via l'instance MISP interne.
>
> Un analyste junior demande : « Pourquoi ne pas utiliser aussi le Diamond Model ? ». Sophie répond que le Diamond Model sera utilisé ponctuellement pour l'analyse d'attribution, mais que le structurer comme grille systématique pour l'ensemble du CTL serait trop lourd pour la taille de l'équipe. « On choisit ses batailles. L'important, c'est la cohérence, pas l'exhaustivité des frameworks. »

---
