---
title: Cyber Threat Intelligence for Detection
source: Cyber/01 CTI & renseignement/Menace cyber/CTI pour la détection (CTI for Detection).md
note: CTI pour la détection (CTI for Detection)
up:
- - CTI pour la détection (CTI for Detection)
  - index.md
---

## Comprendre le concept de CTI

La Cyber Threat Intelligence (CTI) désigne le renseignement permettant d'identifier, comprendre et anticiper les cybermenaces afin d'améliorer les décisions de sécurité.

Elle repose sur la collecte, l'analyse et la contextualisation d'informations concernant :

- les Threat Actors : groupes, motivations, objectifs ;
    
- les TTPs : Tactics, Techniques & Procedures utilisées ;
    
- les IOCs : IP, domaines, hashes et autres indicateurs ;
    
- les vulnérabilités exploitées et les systèmes ciblés ;
    
- les campagnes et infrastructures malveillantes.
    

Données brutes ≠ Threat Intelligence : une information devient exploitable lorsqu'elle est analysée, contextualisée et reliée aux risques d'une organisation.

```
Collecte → Analyse → Contextualisation → Renseignement exploitable
                                          ↓
                            Detection / Hunting / Prevention
```


Deux objectifs majeurs :

1. Identifier les menaces potentielles : comprendre les acteurs, leurs méthodes et leurs cibles.
    
2. Identifier les vulnérabilités et risques associés : déterminer comment ces menaces pourraient affecter l'organisation.
    

La CTI permet ainsi de passer d'une approche principalement réactive à une approche davantage proactive et threat-informed.

## 1. Identification des menaces potentielles

### OSINT — Open Source Intelligence

Renseignement obtenu par la collecte et l'analyse d'informations publiquement accessibles.

Principales sources :

|Sources|Exemples|
|---|---|
|Médias numériques|Actualités, blogs, rapports de sécurité, podcasts|
|Réseaux sociaux|X/Twitter, LinkedIn, forums publics|
|Ressources académiques|Publications, conférences, recherches|
|Sources gouvernementales|Alertes officielles, bases de données publiques|
|Forums / communautés|Discussions techniques, forums spécialisés|
|Données géographiques|Cartes, informations de localisation|

Outils possibles :

- Google / Bing / DuckDuckGo : recherche avancée.
    
- Shodan / Censys : recherche d'équipements et services exposés sur Internet.
    
- Reverse Image Search / InVID : vérification et analyse de contenus visuels.
    
- Outils spécialisés de veille sur les réseaux sociaux.
    

#### Intérêt en cybersécurité

L'OSINT permet notamment de :

- identifier des infrastructures malveillantes ;
    
- rechercher des IOCs publiés ;
    
- suivre les campagnes et outils d'attaque ;
    
- découvrir des informations exposées sur son organisation ;
    
- comprendre comment un attaquant peut effectuer sa reconnaissance.
    

L'OSINT est utilisable aussi bien par les défenseurs que par les attaquants.

```
Public Information
├─ Attacker → Reconnaissance / Target Profiling
└─ Defender → Exposure Assessment / Threat Intelligence
```


⚠️ Source publique ne signifie pas information vérifiée. Il faut contrôler la provenance, la fraîcheur et la fiabilité des résultats.

### TECHINT — Technical Intelligence

Renseignement obtenu par l'analyse d'éléments techniques pour comprendre les capacités, méthodes et opérations d'un adversaire.

Dans le contexte cybersécurité :

- Malware Analysis : comportement, fonctionnalités, persistance, C2 ;
    
- Vulnerability / Exploit Analysis : vulnérabilités ciblées et méthodes d'exploitation ;
    
- Network Traffic Analysis : communications suspectes, protocoles, infrastructures ;
    
- Sandboxing : observation du comportement d'un fichier dans un environnement contrôlé ;
    
- Honeypots : systèmes leurres permettant d'observer les interactions des attaquants.
    

#### Exemple

```
Malware Sample
      ↓
Static / Dynamic Analysis
      ↓
C2 Domain + File Artifacts + Behaviors
      ↓
IOCs + TTPs
      ↓
SIEM / EDR Detection Rules
```


À citer également :

- SIGINT — Signals Intelligence : renseignement issu de signaux et communications.
    
- CNA — Computer Network Attack : Utilisé pour surveiller, analyser et prendre des contre-mesures contre les cybermenaces potentielles.
    

Précision : le SIGINT constitue une discipline de renseignement distincte pouvant fournir des données techniques. Le CNA désigne principalement des opérations offensives, pas une catégorie générale de renseignement sur les réseaux.

Le TECHINT contribue directement au Threat Hunting, au Malware Analysis, à la Detection Engineering et à l'Incident Response.

### HUMINT — Human Intelligence

Renseignement obtenu auprès de sources humaines.

Sources et méthodes évoquées :

- communautés et réseaux spécialisés ;
- Ingénierie sociale :` Une technique de collecte d'informations ou d'obtention d'un accès à un réseau en manipulant des individus cibles.
- `Informations d'initié :` Collecte d'informations auprès d'une source qui fournit des informations de l'intérieur de l'organisation ou de son entourage proche.

    
- échanges avec des experts ou informateurs ;
    
- renseignements provenant de personnes internes à une organisation ;
    
- observation de discussions sur des forums ou marchés clandestins ;
    
- interactions humaines et techniques d'ingénierie sociale.
    

Il peut fournir des informations sur :

- les intentions et motivations d'un Threat Actor ;
    
- les campagnes en préparation ;
    
- les outils ou techniques envisagés ;
    
- certaines faiblesses organisationnelles.
    

Distinction importante :

- Lire un forum public → généralement OSINT.
    
- Obtenir directement des informations auprès d'une personne → HUMINT.
    

Le deep/dark web n'est donc pas automatiquement du HUMINT : cela dépend de la méthode de collecte.

L'ingénierie sociale peut servir à collecter du renseignement, mais constitue aussi une technique d'attaque. Son utilisation dans un cadre défensif doit respecter les autorisations et règles applicables.

### Synthèse des sources

|Source|Nature|Exemple de résultat|
|---|---|---|
|OSINT|Informations accessibles publiquement|Rapport sur une campagne APT|
|TECHINT|Analyse technique|Comportement d'un malware, C2, IOC|
|HUMINT|Informations issues de sources humaines|Renseignements sur les intentions d'un acteur|

Ces disciplines sont complémentaires : une même investigation CTI peut combiner plusieurs sources.

## 2. Identification des vulnérabilités

### Vulnerability Scanners

La partie **Identification des menaces potentielles** nous permet de savoir ce qu'il est possible de connaitre de nous-même depuis l'extérieur, il est primordial de savoir également ce qu'il en est depuis l'intérieur.

Les scanners de vulnérabilités permettent d'identifier les faiblesses potentielles des systèmes, applications et équipements.

Ils facilitent notamment :

- la découverte de composants vulnérables ;
- l'identification de logiciels obsolètes ;
- la détection de certaines mauvaises configurations ;
- la comparaison avec des vulnérabilités publiées ;
- le suivi de l'exposition dans le temps.

Les vulnérabilités publiques peuvent être suivies à travers les références CVE — Common Vulnerabilities and Exposures.

Mais :

- CVE = identifiant d'une vulnérabilité connue.
    
- CVSS = mesure de sévérité technique.
    
- Exploitabilité réelle = dépend du contexte, du produit, de sa configuration et de son exposition.
    

Un scanner ne détecte pas toutes les vulnérabilités et peut produire des false positives / false negatives. Les résultats nécessitent une validation.

### Apport de la CTI à la Vulnerability Management

La CTI permet de distinguer :

- une vulnérabilité simplement connue ;
    
- une vulnérabilité activement exploitée par des Threat Actors ;
    
- une vulnérabilité ciblant des technologies présentes dans l'organisation.
    

La priorisation devient alors plus pertinente :

```
Vulnerability Scan
+
Threat Intelligence
+
Asset Criticality / Exposure
→ Risk-Based Prioritization
```


Une vulnérabilité activement exploitée sur un système exposé et critique peut nécessiter une correction prioritaire, même si son CVSS n'est pas le plus élevé.

CTI et Vulnerability Management sont complémentaires : la première apporte le contexte de menace, la seconde identifie et traite les faiblesses de l'environnement.

## 3. Threat Intelligence Reports

Les rapports sur les menaces sont publiés notamment par :

- chercheurs en sécurité ;
    
- éditeurs de solutions de cybersécurité ;
    
- équipes CTI ;
    
- organismes gouvernementaux ;
    
- prestataires spécialisés.
    

Ils peuvent aussi être produits spécifiquement pour une organisation ou un secteur.

### Contenu d'un Threat Report

Un rapport peut détailler :

- Threat Actor : groupe ou acteur concerné ;
    
- Motivation : espionnage, gain financier, sabotage ;
    
- Targeting : secteurs, pays, technologies ciblés ;
    
- TTPs : méthodes d'intrusion et de post-exploitation ;
    
- Tools / Malware : logiciels et outils employés ;
    
- Vulnerabilities : faiblesses ciblées ou exploitées ;
    
- IOCs : artefacts techniques observés ;
    
- Detections / Mitigations : moyens de détection et mesures défensives.
    

### Utilisation opérationnelle

```
Threat Report
      ↓
Extract IOCs / TTPs
      ↓
Check Relevance to Organization
      ↓
Hunt Historical Logs
      ↓
Create / Improve Detections
      ↓
Validate & Monitor
```


Les rapports permettent donc de :

- anticiper des attaques ;
    
- prioriser le patch management ;
    
- enrichir les règles SIEM/EDR ;
    
- orienter les investigations et le Threat Hunting ;
    
- partager des connaissances entre équipes.
    

Attention à l'attribution : un rapport associant un outil ou une infrastructure à un groupe ne prouve pas que toute activité présentant cet indicateur provient de ce groupe.

## 4. Plateformes de partage d'informations

Ces plateformes facilitent la collecte, la centralisation, l'enrichissement et le partage du renseignement entre organisations.

### MISP — Malware Information Sharing Platform

Plateforme open source de gestion et de partage de Threat Intelligence.

Elle permet notamment :

- de stocker et organiser les indicateurs ;
    
- de relier des artefacts à des événements/campagnes ;
    
- d'enrichir les renseignements ;
    
- de partager des informations ;
    
- d'automatiser certains échanges avec les outils de sécurité.
    

### FS-ISAC — Financial Services Information Sharing and Analysis Center

Organisation de partage de renseignements dédiée au secteur financier.

Objectif : améliorer la connaissance des menaces et la coordination entre institutions financières.

### OTX — Open Threat Exchange

Plateforme communautaire de Threat Intelligence associée à AlienVault.

Elle permet de consulter et partager des indicateurs et informations sur les menaces, notamment sous forme de collections appelées pulses.

### STIX et TAXII

Deux standards complémentaires :

|Standard|Fonction|
|---|---|
|STIX — Structured Threat Information Expression|Format/modèle structuré pour représenter la Threat Intelligence|
|TAXII — Trusted Automated Exchange of Intelligence Information|Protocole/API pour échanger de la Threat Intelligence|

```
STIX  → WHAT information is represented
TAXII → HOW that information is exchanged
```


Exemple de données représentables avec STIX :

- Threat Actors ;
    
- malware ;
    
- indicators ;
    
- attack patterns ;
    
- relationships entre ces objets.
    

### Avantages des plateformes

- Automation : collecte, enrichissement et diffusion en partageant automatiquement les indicateurs de menace.
    
- Standardization / Normalisation : formats standards sont généralement utilisés pour partager les informations (STIX / TAXII) échanges structurés entre différents outils de manière cohérente et compatible.
    
- Collaboration : mutualisation des observations, certaines plateformes permettent aux utilisateurs de travailler en collaboration de sorte que la communauté ait une perspective plus large sur les menaces.
    
- Customization : filtrage par secteur, technologie ou menace.
    
- Confidentialité et anonymat : contrôle de la diffusion des informations sensibles.
    

Complément utile : TLP — Traffic Light Protocol. Il sert à préciser les limites de partage d'une information sensible (par exemple `TLP:RED`, `TLP:AMBER`, `TLP:GREEN`, `TLP:CLEAR`).

### Qualité du renseignement

Un feed contenant de nombreux IOCs n'est pas nécessairement un bon feed.

Critères à examiner :

- fiabilité de la source ;
    
- fraîcheur des indicateurs ;
    
- niveau de confiance ;
    
- contexte associé ;
    
- pertinence pour l'organisation ;
    
- taux de false positives.
    

Un IOC peut rapidement devenir obsolète : IP réattribuée, domaine abandonné, infrastructure partagée, etc.

Il faut donc éviter de transformer automatiquement tous les indicateurs reçus en règles de blocage sans validation.

## 5. CTI appliquée à la détection

Dans le cadre de Cyber Threat Intelligence for Detection, l'objectif n'est pas simplement d'accumuler du renseignement, mais de le rendre exploitable dans les opérations de défense.

### Niveaux de Threat Intelligence

|Niveau|Contenu|Utilisation|
|---|---|---|
|Strategic|Tendances, motivations, impacts métier|Direction, stratégie de sécurité|
|Operational|Campagnes, objectifs, modes opératoires|Préparation et réponse aux menaces|
|Tactical|TTPs et comportements adverses|Threat Hunting, Detection Engineering|
|Technical|IP, domaines, hashes et autres artefacts|Corrélation SIEM, EDR, IOC matching|

Classification complémentaire utile pour organiser le renseignement selon ses consommateurs et ses cas d'usage.

### IOC vs TTP dans la détection

IOC-based Detection

```
Known Malicious Domain
→ Match in DNS Logs
→ Alert / Investigation
```


- rapide à déployer ;
    
- utile pour le retro-hunting ;
    
- mais souvent facile à contourner en changeant l'infrastructure.
    

TTP-based Detection

```
Unusual Process Execution
+
Credential Access Behavior
+
Unexpected Network Communication
→ Behavioral Detection
```


- nécessite davantage de contexte ;
    
- généralement plus durable face aux changements d'IOCs.
    

Le renseignement le plus utile est celui qui permet de prendre une décision concrète :

identifier une menace pertinente → rechercher ses traces → développer une détection → valider son efficacité → maintenir cette détection dans le temps.
