---
title: XDR/EDR Introduction
source: Cyber/06 Détection & réponse/Threat hunting/EDR & XDR — détection, analyse et règles.md
note: EDR & XDR — détection, analyse et règles
up:
- - EDR & XDR — détection, analyse et règles
  - index.md
---

Les solutions EDR (Endpoint Detection and Response) et XDR (Extended Detection and Response) permettent de détecter, investiguer et répondre aux cybermenaces.

La différence principale concerne leur périmètre de visibilité :

- EDR : surveillance et protection des endpoints (postes de travail, serveurs et autres terminaux compatibles).
    
- XDR : corrélation des événements provenant de plusieurs domaines de sécurité : endpoints, réseau, cloud et autres sources.
    

L'objectif commun est d'améliorer la détection des attaques, de faciliter les investigations et d'accélérer l'Incident Response.

## 1. EDR — Endpoint Detection and Response

Un EDR surveille les activités des endpoints afin d'identifier des comportements suspects, d'analyser les incidents et de déclencher des actions de réponse.

### Fonctionnalités principales

|Fonctionnalité|Description|
|---|---|
|Real-Time Monitoring|Surveillance continue des activités endpoint|
|File & Process Monitoring|Surveillance des fichiers, processus et activités système|
|Behavioral Analysis|Identification de comportements inhabituels ou malveillants|
|Malware Detection|Détection et isolation de malwares|
|IOC Detection|Recherche d'indicateurs connus : hashes, IP, domaines, etc.|
|Event Log Analysis|Analyse des événements système et de sécurité|
|Threat Intelligence Integration|Enrichissement des détections avec des renseignements CTI|
|Machine Learning|Analyse automatisée pour identifier certaines menaces|
|Incident Investigation|Reconstruction des activités et des chaînes d'attaque|
|Response Capabilities|Actions de confinement et de remédiation|
|Network Monitoring|Visibilité sur certaines connexions réseau associées aux endpoints|
|Data Protection & Encryption|Fonctionnalités complémentaires de protection des données selon la solution|

### EDR — Detection & Investigation

L'EDR observe notamment :

- les processus exécutés et leurs relations parent/enfant ;
    
- les fichiers créés ou modifiés ;
    
- les activités suspectes ;
    
- les connexions réseau initiées par les processus ;
    
- les événements de sécurité disponibles.
    

Exemple d'investigation :

```
Suspicious Process
        ↓
EDR Detection
        ↓
Process Tree / File Activity
        ↓
Network Connections / IOCs
        ↓
Analyst Investigation
        ↓
Response if Necessary
```


Le Behavioral Analysis est particulièrement utile pour identifier une application effectuant des opérations inhabituelles, même sans correspondance avec un hash malveillant connu.

### EDR — Response Capabilities

Selon les fonctionnalités de la solution :

- Host Isolation : isoler un endpoint du réseau pour limiter une éventuelle propagation.
    
- Process Termination : arrêter un processus malveillant.
    
- File Quarantine : mettre un fichier en quarantaine.
    
- Remediation : neutraliser ou supprimer certains artefacts malveillants.
    
- Network Blocking : bloquer certaines communications lorsque cette capacité est disponible.
    
- Remote Investigation : approfondir l'analyse à distance.
    
- Automated Response : déclencher des actions prédéfinies selon les détections et policies.
    

Certaines actions peuvent être exécutées automatiquement ; d'autres nécessitent une intervention ou une validation humaine.
    

Précision : l'EDR ne garantit pas une visibilité complète sur tous les événements d'un système. La télémétrie et les capacités de réponse dépendent de l'agent, du système d'exploitation et de la configuration.

## 2. XDR — Extended Detection and Response

Le XDR étend les capacités de détection et de réponse en intégrant plusieurs sources de sécurité dans une analyse commune.

Contrairement à un EDR centré sur les endpoints, il vise une visibilité transversale sur les différentes étapes d'une attaque.

### Fonctionnalités principales

|Fonctionnalité|Description|
|---|---|
|Multi-Source Integration|Agrégation des données endpoint, réseau, cloud et autres sources|
|Threat Correlation|Corrélation d'événements provenant de plusieurs environnements|
|Automated Detection|Identification automatisée de certaines menaces, notamment via IA/ML|
|Threat Chain Analysis|Reconstruction des étapes et relations d'une attaque|
|Automated Response|Actions automatisées selon les règles et intégrations disponibles|
|Threat Intelligence Integration|Utilisation des IOCs, TTPs et renseignements externes|
|Incident Management|Centralisation et analyse des incidents de sécurité|
|Reporting|Rapports sur les incidents, menaces et résultats des investigations|

### XDR — Cross-Domain Correlation

L'intérêt principal du XDR est de relier des événements qui pourraient paraître peu significatifs lorsqu'ils sont examinés séparément.

Exemple illustratif :

```
Endpoint → Suspicious PowerShell Execution
                         +
Network  → Connection to Malicious Domain
                         +
Cloud    → Unusual Account Activity
                         ↓
                  XDR Correlation
                         ↓
              Related Security Incident
                         ↓
               Investigation / Response
```


Chaque événement peut avoir une explication légitime. Leur corrélation fournit davantage de contexte pour examiner une éventuelle chaîne d'attaque.

### Threat Chain Analysis

Le XDR permet de reconstruire les relations entre différents événements afin de mieux comprendre :

- comment une attaque a commencé ;
    
- quels systèmes ou comptes sont concernés ;
    
- comment elle s'est propagée ;
    
- quelles actions ont été réalisées ;
    
- quelles mesures de réponse sont nécessaires.
    

### Automated Detection & Response

Le XDR peut utiliser des analyses comportementales, de l'IA et du Machine Learning pour identifier des menaces.

Il peut également faciliter ou automatiser certaines actions de réponse.

Attention : une détection automatisée ne constitue pas une preuve définitive de compromission. De même, les capacités de réponse automatique dépendent des intégrations, licences et politiques configurées.

## 3. EDR vs XDR

|Critère|EDR|XDR|
|---|---|---|
|Périmètre|Endpoints|Plusieurs domaines de sécurité|
|Sources principales|Processus, fichiers, événements endpoint|Endpoints, réseau, cloud, logs de sécurité|
|Détection|Malware, IOCs, comportements endpoint|Détections et corrélations multi-sources|
|Investigation|Activités d'une ou plusieurs machines|Chaîne d'attaque à travers plusieurs environnements|
|Threat Intelligence|Intégration possible|Intégration possible|
|Response|Actions principalement sur les endpoints|Actions potentiellement coordonnées entre plusieurs outils|
|Objectif|Visibilité et réponse endpoint|Visibilité et réponse étendues|

### Exemple : compromission d'un endpoint

Avec un EDR : l'analyste peut rechercher le processus malveillant, sa command line, les fichiers manipulés et les connexions réseau initiées.

Avec un XDR : l'analyste peut également corréler cette activité avec d'autres sources intégrées, par exemple des événements réseau ou cloud, afin d'identifier une éventuelle propagation.

L'EDR apporte donc une visibilité approfondie sur les endpoints, tandis que le XDR cherche à fournir une vision plus globale de l'incident.

## 4. Application au Threat Hunting

Les deux approches contribuent aux investigations proactives.

|Activité|Apport EDR / XDR|
|---|---|
|IOC-Based Hunting|Recherche de hashes, IP et domaines suspects|
|Behavioral Hunting|Analyse des processus et comportements inhabituels|
|Threat Chain Investigation|Reconstruction des activités liées à une attaque|
|Incident Scoping|Identification des systèmes et comptes potentiellement affectés|
|Detection Improvement|Exploitation des résultats pour améliorer les détections|

Distinction essentielle : un XDR n'est pas simplement un EDR disposant de davantage d'alertes. Son intérêt repose sur la corrélation de plusieurs sources de sécurité, tandis que l'EDR reste spécialisé dans la télémétrie et la réponse sur les endpoints.

Ces solutions sont complémentaires : la qualité de leurs détections dépend de la visibilité disponible, de la qualité des données et de leur configuration.
