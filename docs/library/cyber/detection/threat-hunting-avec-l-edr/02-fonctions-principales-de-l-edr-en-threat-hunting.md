---
title: Fonctions principales de l'EDR en Threat Hunting
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting avec l'EDR.md
note: Threat hunting avec l'EDR
up:
- - Threat hunting avec l'EDR
  - index.md
---

Les solutions EDR (Endpoint Detection & Response) permettent de détecter, investiguer et traiter les activités malveillantes sur les endpoints.

Dans un processus de Threat Hunting, elles fournissent la télémétrie et les capacités nécessaires pour rechercher des menaces non détectées et comprendre leur comportement.

Quatre fonctions principales :

- Threat Detection : identifier les menaces.
    
- Investigation : analyser les événements et reconstruire l'attaque.
    
- Response : contenir et neutraliser les activités malveillantes.
    
- Recovery : contribuer au rétablissement des systèmes et à la prévention de nouvelles attaques.
    

## 1. Threat Detection

### Anomaly & Behavioral Detection

Les EDR surveillent les activités des endpoints pour identifier des comportements inhabituels ou potentiellement malveillants.

Exemples :

- authentifications à des horaires inhabituels ;
    
- modifications inattendues de fichiers ;
    
- exécution de nouveaux logiciels ou processus ;
    
- activités s'écartant du comportement habituel d'un système.
    

Les mécanismes de Behavioral Analysis et d'Anomaly Detection permettent de signaler ces activités pour investigation.

Anomaly ≠ Confirmed Compromise : une activité inhabituelle peut parfaitement être légitime.

### Threat Intelligence Integration

Les EDR peuvent intégrer des renseignements CTI pour identifier des menaces connues.

Exemples d'IOCs :

- malware hashes ;
    
- adresses IP malveillantes ;
    
- domaines suspects ;
    
- autres indicateurs associés à des campagnes connues.
    

La combinaison Real-Time Monitoring + Threat Intelligence facilite la détection rapide de certaines menaces et l'intervention précoce.

## 2. Investigation

L'Investigation vise à comprendre l'origine, les méthodes et les conséquences potentielles d'une activité suspecte.

### Event Correlation & Analysis

Les EDR permettent de corréler plusieurs événements endpoint afin de reconstruire les comportements observés.

Exemples :

- création d'un processus ;
    
- modification de fichiers ;
    
- connexion réseau ;
    
- exécution de processus enfants.
    

### Digital Forensic Analysis

La télémétrie EDR peut contribuer à l'analyse forensic en fournissant des traces permettant de comprendre :

- comment l'activité a commencé ;
    
- quels processus et fichiers sont impliqués ;
    
- quelles actions ont été réalisées ;
    
- quels endpoints sont potentiellement affectés.
    

### Incident Investigation Tools

|Fonctionnalité|Utilité|
|---|---|
|Timeline Creation|Reconstituer l'ordre chronologique des événements|
|Event Correlation|Relier les activités suspectes|
|File Analysis|Examiner les fichiers potentiellement malveillants|
|Memory Analysis|Investiguer certaines activités en mémoire, selon les capacités du produit|

Exemple illustratif :

```
Suspicious Process Execution
          ↓
Unexpected File Modification
          ↓
Outbound Network Connection
          ↓
EDR Timeline & Correlation
          ↓
Threat Investigation
```


Une séquence d'événements contextualisée fournit davantage d'éléments qu'une alerte isolée.

## 3. Response

La Response regroupe les actions destinées à contenir ou neutraliser une menace identifiée.

### Incident Response & Isolation

Isolation de l'endpoint, arrêt de processus, blocage réseau, réponse automatisée : voir [les capacités de réponse d'un EDR](../edr-xdr-detection-analyse-et-regles/01-xdr-edr-introduction.md#edr-response-capabilities) (étape 3).

### Quarantine & Remediation

- Quarantine : isoler un fichier suspect ou malveillant pour empêcher son utilisation normale.
    
- Remediation : neutraliser les composants malveillants ou corriger certaines modifications provoquées par l'attaque.
    

Distinction importante : arrêter un processus ou mettre un fichier en quarantaine ne garantit pas que tous les mécanismes de persistence ou les dommages causés par l'attaquant ont été supprimés.

## 4. Recovery

La Recovery consiste à restaurer le fonctionnement normal des systèmes après un incident.

Deux activités principales.

### Backup & Restore

- Restaurer les systèmes ou données depuis des sauvegardes fiables.
    
- Réduire les interruptions opérationnelles.
    
- Vérifier que l'environnement restauré ne présente plus les éléments de compromission identifiés.
    

### Patch Application

- Identifier les vulnérabilités ou faiblesses exploitées.
    
- Appliquer les correctifs nécessaires.
    
- Réduire le risque de réexploitation.
    

⚠️ Précision technique : les EDR ne garantissent pas eux-mêmes la restauration des sauvegardes ou l'application des correctifs. Ces opérations s'appuient généralement sur des solutions de backup, de patch management et des procédures d'Incident Response distinctes. L'EDR peut fournir les informations nécessaires ou contribuer à certaines actions selon le produit.

## 5. Workflow opérationnel

```
Threat Detection
       ↓
Investigation
       ↓
Validate Threat
       ↓
Response / Containment
       ↓
Remediation
       ↓
Recovery
       ↓
Verify Endpoint Security
```


|Fonction EDR|Question pour l'analyste|
|---|---|
|Detection|Quelle activité suspecte a été détectée ?|
|Investigation|Comment s'est-elle produite et quels systèmes sont concernés ?|
|Response|Comment arrêter ou contenir la menace ?|
|Recovery|Comment rétablir un état sûr et réduire le risque de récidive ?|

Le Threat Hunting exploite particulièrement les deux premières fonctions : la détection et l'investigation. Lorsqu'une menace est confirmée, les capacités de réponse EDR peuvent ensuite soutenir les opérations d'Incident Response.

L'efficacité de l'ensemble dépend de la qualité de la télémétrie collectée, de la configuration des policies et de la validation des événements par les analystes.
