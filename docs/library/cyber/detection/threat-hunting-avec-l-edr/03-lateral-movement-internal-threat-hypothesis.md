---
title: Lateral Movement & Internal Threat Hypothesis
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting avec l'EDR.md
note: Threat hunting avec l'EDR
up:
- - Threat hunting avec l'EDR
  - index.md
---

Le Lateral Movement (mouvement latéral) désigne les activités par lesquelles un attaquant ayant obtenu un premier accès tente d'atteindre d'autres systèmes au sein du réseau interne.

En Threat Hunting, l'objectif est d'identifier les signes d'une éventuelle propagation en analysant les activités endpoint et les communications entre machines.

## 1. Threat Hunting Hypothesis

Hypothèse : un Threat Actor pourrait effectuer des mouvements latéraux sur le réseau interne afin d'accéder à d'autres systèmes ou segments réseau.

Cette approche consiste à rechercher des comportements compatibles avec cette hypothèse, même en l'absence d'alerte confirmant une compromission.

Les activités recherchées concernent principalement :

- les exécutions suspectes sur les endpoints ;
    
- les connexions inhabituelles entre machines ;
    
- les accès à de nouveaux systèmes internes ;
    
- les activités réseau potentiellement malveillantes.
    

## 2. Data Sources

Trois sources principales permettent de rechercher les signes de Lateral Movement.

|Source|Informations exploitables|
|---|---|
|EDR Logs|Processus, fichiers, exécutions suspectes et activités des endpoints|
|Network Traffic Logs|Connexions entre machines, destinations, ports et protocoles utilisés|
|IDS/IPS Logs|Alertes sur les tentatives d'attaque et les activités suspectes du réseau interne|

L'objectif est de corréler les événements observés sur les endpoints avec les communications réseau.

## 3. Threat Hunting — Analysis Steps

### Endpoint Activity Analysis

Analyser les activités des endpoints afin d'identifier les comportements potentiellement associés à une compromission.

- Process Activity : exécutions de processus inhabituels.
    
- File Activity : créations ou modifications de fichiers suspectes.
    
- Antivirus Alerts : détections de malware signalées sur les endpoints.
    
- Suspicious Code Execution : exécution de code ou de commandes potentiellement malveillantes.
    

Ces éléments peuvent révéler des actions effectuées après l'obtention d'un accès initial.

### Internal Network Analysis

Rechercher les changements inhabituels dans les communications entre les machines internes.

- Increased Connection Attempts : augmentation des tentatives de connexion entre endpoints.
    
- New Host Access : accès à des systèmes internes jamais contactés auparavant.
    
- Unexpected Protocol Usage : utilisation inhabituelle de protocoles comme SMB ou RDP.
    
- Internal Port Scanning : scans de ports sur les machines du réseau interne.
    
- Unusual Ports : communications sur des ports inattendus.
    

Les protocoles SMB et RDP ne sont pas malveillants en eux-mêmes. Leur utilisation devient suspecte lorsqu'elle ne correspond pas au comportement habituel de l'utilisateur ou de la machine.

### IDS/IPS Analysis

Examiner les alertes de sécurité réseau pour identifier :

- des tentatives d'attaque entre machines internes ;
    
- des comportements réseau anormaux ;
    
- des événements signalés par les signatures IDS/IPS ;
    
- des écarts par rapport aux patterns de communication habituels.
    

Les alertes peuvent contribuer à renforcer une hypothèse lorsqu'elles correspondent à des activités suspectes observées dans les EDR ou les logs réseau.

## 4. Correlation & Investigation

La recherche d'un mouvement latéral repose sur le rapprochement de plusieurs observations.

Exemple illustratif :

```
Endpoint A
   ↓
Suspicious Process Execution
   ↓
Unusual Internal Connection (SMB / RDP)
   ↓
Access to Previously Unseen Host B
   ↓
IDS/IPS Alert
   ↓
Potential Lateral Movement
```


L'analyste cherche notamment à déterminer :

- Source : quelle machine initie les connexions ?
    
- Destination : quels nouveaux endpoints sont contactés ?
    
- Process : quelle activité endpoint est associée aux connexions ?
    
- Protocol : SMB, RDP ou autre protocole inhabituel ?
    
- Behavior : ces connexions correspondent-elles à l'activité normale du réseau ?
    
- Alerts : des événements EDR ou IDS/IPS corroborent-ils les observations ?
    

Une connexion interne inhabituelle ne suffit pas à confirmer un Lateral Movement. Elle peut également correspondre à une opération d'administration ou de maintenance légitime.

## 5. Expected Findings

Trois grandes catégories de résultats attendus.

|Catégorie|Résultats recherchés|
|---|---|
|Endpoint Anomalies|Activités anormales de processus ou de fichiers|
|Internal Connections|Augmentation des tentatives de connexion et accès à de nouveaux appareils|
|Network Security Alerts|Alertes IDS/IPS et comportements compatibles avec des attaques internes|

Ces résultats permettent d'identifier les machines nécessitant une investigation approfondie.

## 6. Hunting Workflow

```
Hypothesis: Potential Lateral Movement
                    ↓
         Collect EDR / Network /
             IDS-IPS Logs
                    ↓
        Analyze Endpoint Activity
                    ↓
       Analyze Internal Connections
                    ↓
       Review IDS/IPS Detections
                    ↓
        Correlate Suspicious Events
                    ↓
       Validate Hunting Hypothesis
                    ↓
         Investigation / Response
```


L'objectif de cette méthodologie est de détecter une éventuelle progression d'un attaquant sur le réseau interne en corrélant la télémétrie endpoint, les communications réseau et les alertes IDS/IPS.

Le Threat Hunting permet ainsi de rechercher proactivement des mouvements latéraux potentiellement non détectés par les mécanismes de sécurité existants.
