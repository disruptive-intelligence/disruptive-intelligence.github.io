---
title: Common XDR/EDR Products
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/EDR & XDR — détection, analyse et règles.md
note: EDR & XDR — détection, analyse et règles
up:
- - EDR & XDR — détection, analyse et règles
  - index.md
---

Les solutions EDR (Endpoint Detection and Response) et XDR (Extended Detection and Response) permettent de détecter, investiguer et répondre aux cybermenaces.

- EDR : visibilité approfondie sur les endpoints.
    
- XDR : corrélation des événements provenant de plusieurs domaines de sécurité (endpoints, réseau, cloud, etc.).
    

Cette section présente cinq solutions : CrowdStrike Falcon, Cybereason, Microsoft Defender, Palo Alto Cortex XDR et SentinelOne.

## 1. CrowdStrike Falcon

CrowdStrike Falcon est une plateforme de sécurité endpoint, principalement administrée depuis une infrastructure cloud, proposant des fonctionnalités EDR et XDR.

### Fonctionnalités

- Cloud-Based Architecture : gestion centralisée et déploiement à grande échelle.
    
- Lightweight Agent : agent installé sur les endpoints pour collecter la télémétrie et appliquer les protections.
    
- Machine Learning : analyse automatisée des menaces connues et inconnues.
    
- Threat Intelligence : intégration de renseignements sur les Threat Actors et leurs TTPs.
    
- Proactive Threat Hunting : recherche et investigation des comportements suspects.
    
- Real-Time Response : actions de réponse sur les endpoints.
    

### Intérêt en Threat Hunting

CrowdStrike Falcon permet d'associer les activités endpoint à des renseignements CTI afin de mieux comprendre les comportements malveillants.

L'architecture cloud facilite la gestion centralisée, mais un agent léger ne garantit pas un impact nul sur les performances.

## 2. Cybereason

Cybereason propose des capacités EDR, EPP (Endpoint Protection Platform) et XDR.

Deux modes de déploiement :

- des possibilités de déploiement EDR/EPP on-premises ;
    
- des capacités XDR disponibles via une plateforme cloud.
    

### Operation-Centric Approach

Cybereason adopte une approche centrée sur les opérations malveillantes, plutôt que sur des alertes considérées individuellement.

Sa fonctionnalité caractéristique est Malop (Malicious Operation).

Elle permet de :

- regrouper les événements liés à une même activité malveillante ;
    
- visualiser les différents composants d'une attaque ;
    
- comprendre les relations entre les événements ;
    
- faciliter l'investigation et la réponse.
    

```
Multiple Suspicious Events
           ↓
   Malop Correlation
           ↓
  Malicious Operation
           ↓
 Investigation / Response
```


Intérêt principal : reconstituer le contexte global d'une attaque pour éviter d'investiguer chaque alerte isolément.

## 3. Microsoft Defender for Endpoint

Microsoft Defender for Endpoint (MDE) est la solution EDR de Microsoft, anciennement appelée Microsoft Defender ATP.

Elle s'appuie sur des fonctionnalités de protection endpoint, de détection comportementale et d'investigation.

### Fonctionnalités

- Endpoint Protection : prévention et détection de menaces.
    
- Behavioral Analysis & AI : identification d'activités suspectes.
    
- Threat Intelligence : exploitation des renseignements Microsoft.
    
- Incident Response : investigation et remédiation.
    
- Centralized Management : administration dans l'écosystème Microsoft Security.
    
- Advanced Hunting : recherche de comportements suspects dans la télémétrie de sécurité.
    

### EDR vs XDR chez Microsoft

⚠️ Distinction importante :

Defender ATP a évolué vers Microsoft 365 Defender. Il faut distinguer les produits :

|Produit|Fonction|
|---|---|
|Microsoft Defender for Endpoint|Protection, détection et réponse sur les endpoints — EDR|
|Microsoft Defender XDR|Corrélation et investigation entre plusieurs domaines de sécurité — XDR|

Microsoft 365 Defender est l'ancienne appellation de Microsoft Defender XDR.

L'intérêt de l'écosystème Microsoft réside notamment dans l'intégration des activités endpoint avec d'autres signaux de sécurité, selon les produits et licences déployés.

## 4. Palo Alto Networks Cortex XDR

Cortex XDR est une plateforme de détection et de réponse étendues développée par Palo Alto Networks.

Elle se distingue par sa capacité à analyser des événements provenant de plusieurs domaines de sécurité.

### Fonctionnalités

- Multi-Source Integration : combinaison de données endpoint, réseau, cloud et autres sources compatibles.
    
- Advanced Analytics : analyse de grands volumes de télémétrie.
    
- AI / Machine Learning : identification de comportements suspects.
    
- Threat Correlation : corrélation entre les différentes étapes d'une attaque.
    
- Continuous Monitoring : surveillance et investigation des menaces.
    
- Automated Response : actions de réponse selon les intégrations disponibles.
    

### Intérêt en Threat Hunting

Cortex XDR permet de relier une activité suspecte détectée sur un endpoint à d'autres événements réseau ou cloud.

Son principal avantage est la Cross-Domain Visibility, qui facilite l'analyse d'attaques complexes dépassant un seul endpoint.

## 5. SentinelOne

SentinelOne est une plateforme de sécurité proposant des capacités EDR et XDR, avec un accent sur l'automatisation et l'analyse comportementale.

### Fonctionnalités

- Static & Behavioral Analysis : combinaison de méthodes statiques et comportementales.
    
- AI / Machine Learning : détection automatisée des menaces.
    
- Automated Response : intervention et remédiation selon la configuration.
    
- Attack Mapping : visualisation des événements et des chaînes d'attaque.
    
- Incident Investigation : compréhension de l'origine et des conséquences d'une attaque.
    
- Third-Party Integrations : connexion avec d'autres solutions de sécurité.
    

### Intérêt en Threat Hunting

SentinelOne aide les analystes à comprendre la progression d'une activité malveillante grâce à la visualisation des événements liés à une attaque.

Les fonctionnalités d'automatisation contribuent à réduire les tâches répétitives et à accélérer certaines réponses.

## 6. Comparaison des solutions

|Solution|Orientation|Élément caractéristique présenté|
|---|---|---|
|CrowdStrike Falcon|EDR / XDR|Cloud, Threat Intelligence et Threat Hunting|
|Cybereason|EDR / XDR|Analyse Operation-Centric et Malop|
|Microsoft Defender for Endpoint|EDR|Intégration Microsoft et Advanced Hunting|
|Microsoft Defender XDR|XDR|Corrélation des signaux de sécurité Microsoft|
|Palo Alto Cortex XDR|XDR|Analyse et corrélation multi-sources|
|SentinelOne|EDR / XDR|Analyse comportementale, automatisation et Attack Mapping|

Les cinq solutions partagent de nombreuses fonctionnalités : collecte de télémétrie, détection comportementale, Threat Intelligence, investigation et réponse.

Leur différenciation repose surtout sur l'architecture, les intégrations, les méthodes d'analyse, les possibilités de déploiement et les fonctionnalités disponibles selon les licences.

## 7. Application en Threat Hunting

Exemple : un endpoint exécute un processus inhabituel qui communique avec une infrastructure suspecte.

```
Suspicious Process
        ↓
EDR Telemetry
        ↓
Process Tree / File & Network Activity
        ↓
Threat Intelligence Enrichment
        ↓
Cross-Source Correlation (XDR)
        ↓
Attack Investigation
        ↓
Response / Detection Improvement
```


L'EDR permet principalement de comprendre ce qui s'est produit sur l'endpoint. Le XDR étend l'investigation en reliant ces activités aux événements provenant des autres domaines de sécurité intégrés.

Point de vigilance : aucune de ces plateformes ne garantit la détection de toutes les attaques ou zero-days. Leur efficacité dépend de la télémétrie collectée, des capacités activées et des investigations réalisées par les analystes.
