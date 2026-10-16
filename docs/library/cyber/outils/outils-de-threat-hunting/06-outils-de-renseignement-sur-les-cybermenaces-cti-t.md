---
title: Outils de renseignement sur les cybermenaces — CTI Tools
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les Cyber Threat Intelligence (CTI) Tools permettent de collecter, enrichir, analyser et partager des renseignements sur les cybermenaces.

En Threat Hunting, ils fournissent le contexte nécessaire pour orienter les recherches vers les menaces pertinentes pour une organisation.

Objectifs :

- Identifier les Threat Actors, leurs motivations et leurs TTPs.
    
- Collecter et enrichir des IOCs.
    
- Identifier les campagnes et infrastructures malveillantes.
    
- Orienter les hypothèses de Threat Hunting.
    
- Améliorer la détection, la prévention et l'Incident Response.
    

## 1. Threat Data Collection & Enrichment

### Collecte de données

Les outils CTI collectent des renseignements provenant de plusieurs sources :

|Source|Informations obtenues|
|---|---|
|OSINT|Rapports publics, recherches, informations accessibles publiquement|
|Commercial Threat Feeds|IOCs et renseignements fournis par des prestataires spécialisés|
|Dark Web Monitoring|Fuites de données, credentials compromis, discussions de Threat Actors|
|ISACs|Renseignements partagés entre organisations d'un même secteur|

L'utilisation de sources variées permet d'obtenir une vision plus complète du paysage des menaces.

### Data Enrichment

L'enrichissement consiste à ajouter du contexte aux données collectées pour les rendre exploitables.

Exemple :

```
Suspicious IP Address
       ↓
CTI Enrichment
       ↓
Known C2 Infrastructure
Associated Malware / Campaign
Previous Observations
       ↓
Threat Hunting Investigation
```


L'analyste peut alors déterminer si l'IOC mérite d'être recherché dans son environnement.

Précision : l'association d'une IP à une campagne ou à un malware n'est pas nécessairement définitive. Elle dépend de la fiabilité et de la fraîcheur du renseignement.

## 2. Threat Analysis & Correlation

Les plateformes CTI analysent et corrèlent les informations provenant de différentes sources.

Elles contribuent à identifier :

- les relations entre IOCs, malwares et Threat Actors ;
    
- les méthodes et vecteurs d'attaque utilisés ;
    
- les campagnes et infrastructures associées ;
    
- les risques potentiels pour l'organisation.
    

### Utilisation en Threat Hunting

Un rapport CTI révèle qu'un groupe utilise une technique spécifique de persistence.

```
CTI Report
    ↓
Identify Threat Actor TTPs
    ↓
Search Internal Telemetry
    ↓
Investigate Suspicious Activity
    ↓
Improve Detection Rules
```


La CTI permet ainsi de passer d'une information externe à une recherche ciblée dans les logs internes.

## 3. Threat Intelligence Sharing

Le Threat Intelligence Sharing consiste à distribuer les renseignements aux équipes et organisations concernées.

Objectifs :

- Accélérer la diffusion des informations sur les menaces.
    
- Faciliter la collaboration entre équipes de sécurité.
    
- Partager les IOCs et TTPs observés.
    
- Améliorer la coordination des actions défensives.
    

Les renseignements peuvent être transmis au :

- SOC : amélioration du monitoring et des détections.
    
- Threat Hunting Team : préparation de nouveaux hunts.
    
- Incident Response Team : enrichissement des investigations.
    
- Security Management : priorisation des risques.
    

Complément technique : les standards STIX et TAXII peuvent faciliter la représentation et l'échange automatisé de Threat Intelligence. Leur utilisation dépend des plateformes et intégrations disponibles.

Les informations partagées doivent conserver leur contexte, leur niveau de confiance et leurs restrictions de diffusion.

## 4. Proactive Defense & Threat Prediction

Les outils CTI permettent d'anticiper certaines menaces à partir des activités observées des Threat Actors.

Applications :

- Early Warning : identification précoce de menaces émergentes.
    
- Threat Forecasting : estimation des attaques ou campagnes susceptibles de cibler l'organisation.
    
- Risk Prioritization : priorisation des menaces pertinentes.
    
- Proactive Detection : développement de règles avant l'observation d'une attaque interne.
    

Exemple :

Une campagne cible activement une vulnérabilité présente dans un logiciel utilisé par l'organisation.

La CTI peut aider à :

1. Identifier la campagne et les techniques utilisées.
    
2. Vérifier si les systèmes concernés sont exposés.
    
3. Prioriser les mesures de protection.
    
4. Rechercher d'éventuelles traces d'exploitation.
    

Attention : la CTI ne permet pas de prédire avec certitude les futures attaques. Elle fournit des éléments permettant d'évaluer des scénarios de menace plausibles.

## 5. Incident Response & Continuous Improvement

Lors d'un incident, les renseignements CTI peuvent aider les analystes à :

- identifier les IOCs associés à l'attaque ;
    
- comprendre les techniques et outils employés ;
    
- rechercher d'autres systèmes potentiellement compromis ;
    
- orienter les investigations ;
    
- améliorer les mesures de détection et de prévention.
    

Après l'incident, les nouveaux IOCs et TTPs découverts peuvent enrichir les connaissances CTI et les futurs hunts.

La CTI fournit le renseignement : les actions de containment, eradication et recovery sont réalisées par les équipes et outils de réponse appropriés.

## 6. Exemples de CTI Tools

|Outil|Fonctionnalités principales|Contribution au Threat Hunting|
|---|---|---|
|Recorded Future|Collecte multi-sources, analyse des menaces et diffusion du renseignement|Identification de campagnes, IOCs et menaces pertinentes|
|ThreatConnect|Centralisation, corrélation, analyse et partage de Threat Intelligence|Enrichissement des investigations, collaboration et soutien à l'Incident Response|

### Recorded Future

Plateforme CTI permettant notamment de :

- collecter des informations provenant de diverses sources ;
    
- analyser et contextualiser les menaces ;
    
- fournir des renseignements aux équipes de sécurité ;
    
- orienter les investigations proactives.
    

### ThreatConnect

Plateforme de Threat Intelligence facilitant :

- l'agrégation de renseignements ;
    
- la corrélation d'informations issues de plusieurs sources ;
    
- le partage et la collaboration ;
    
- l'exploitation des renseignements pendant les investigations.
    

Ces outils poursuivent des objectifs similaires, avec des fonctionnalités et intégrations pouvant varier selon les offres.

## 7. Intégration de la CTI au Threat Hunting

```
OSINT / Dark Web / ISACs / Threat Feeds
                   ↓
              CTI Platform
                   ↓
       Collection & Enrichment
                   ↓
        Analysis & Correlation
                   ↓
         Actionable Intelligence
                   ↓
         Threat Hunting / SOC
                   ↓
          SIEM / EDR Searches
                   ↓
       Investigation & Validation
                   ↓
       Detection Improvement / IR
```


|Composant|Rôle|
|---|---|
|CTI Platform|Comprendre quelles menaces et techniques rechercher|
|SIEM|Rechercher et corréler les événements internes|
|EDR|Investiguer les comportements sur les endpoints|
|Threat Hunter|Tester les hypothèses et valider les résultats|

La distinction essentielle est que la CTI apporte le contexte externe sur les menaces, tandis que le Threat Hunting exploite ce renseignement pour rechercher des traces concrètes dans l'environnement de l'organisation.

Une information CTI n'est donc véritablement exploitable que lorsqu'elle est pertinente, contextualisée et transformée en actions défensives.
