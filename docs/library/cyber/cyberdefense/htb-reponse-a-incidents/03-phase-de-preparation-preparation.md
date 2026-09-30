---
title: Phase de préparation — Preparation
source: Cyber/05_Cyberdefense/HTB_Réponse à incidents.md
note: HTB — Réponse à incidents
up:
- - HTB — Réponse à incidents
  - index.md
---

- La phase **Preparation** poursuit deux objectifs distincts :
    1. mettre en place une **capacité de gestion/réponse aux incidents** ;
    2. réduire la probabilité et l’impact des incidents grâce à des mesures préventives.

```
Preparation
├─ Incident Response Capability
└─ Preventive Security Controls
```

Les mesures préventives peuvent inclure :

- endpoint / server hardening ;
- Active Directory tiering ;
- MFA ;
- PAM — Privileged Access Management ;
- segmentation ;
- patch management ;
- logging / monitoring.

> L’équipe Incident Response n’est pas nécessairement responsable de tous ces contrôles préventifs, mais leur qualité influence directement sa capacité à gérer efficacement un incident.
## Prérequis pour la préparation
Une organisation doit disposer au minimum de :

- membres IR qualifiés ;
- compétences internes minimales même si l’IR est externalisée ;
- personnel sensibilisé et formé ;
- politiques et procédures documentées ;
- outils logiciels et matériels adaptés.

```
People
+
Processes
+
Technology
→ Incident Response Readiness
```

## Équipe de réponse aux incidents

- Les membres doivent connaître :
    - incident handling ;
    - investigation ;
    - containment ;
    - forensic basics ;
    - outils utilisés dans l’environnement.
- Certaines compétences peuvent être externalisées, mais l’organisation doit conserver suffisamment de connaissances en interne pour :
    - comprendre l’incident ;
    - coordonner les actions ;
    - prendre des décisions.

```
Internal Capability
+
External Expertise if needed
→ Effective Response
```

## Politiques & documentation
La documentation doit être **préparée avant l’incident** et maintenue à jour.
### Contacts et responsabilités
Conserver les coordonnées de :

- Incident Response Team ;
- Legal / Compliance ;
- management ;
- IT Support ;
- Communication / PR ;
- fournisseurs / prestataires ;
- ISP ;
- facilities ;
- forces de l’ordre lorsque nécessaire ;
- Incident Response provider externe.

```
Incident
→ Who must be contacted?
→ Who can authorize what?
```

L’objectif est d’éviter de chercher les responsables et coordonnées au milieu d’une crise.
### Incident Response Policy / Plan / Procedures

Il faut distinguer :
#### Policy - Politique

- Définit les règles et attentes générales de l’organisation.
#### Plan

- Définit l’organisation globale de la réponse :
    - rôles ;
    - responsabilités ;
    - communication ;
    - priorités.
#### Procedures / Playbooks

- Décrivent les actions opérationnelles à réaliser selon le type d’incident.

```
Policy
→ What / Why

Plan
→ Who / When

Procedure / Playbook
→ How
```

Exemples de playbooks :

- ransomware ;
- phishing ;
- compromised account ;
- malware ;
- data breach ;
- lost device.

### Information Sharing Policy

- Déterminer :
    - quelles informations peuvent être partagées ;
    - avec qui ;
    - à quel moment ;
    - par quelle personne autorisée.

Cela concerne notamment :

- clients ;
- partenaires ;
- vendors ;
- autorités ;
- médias

> Une communication non coordonnée pendant un incident peut créer des risques juridiques, opérationnels ou réputationnels.
## Baselines / Golden Images

- Conserver des **baselines** représentant un état normal et sain des systèmes et réseaux.

Exemples :

- services normalement actifs ;
- processus ;
- ports ;
- configurations ;
- fichiers système ;
- trafic réseau attendu.

```
Known-Good Baseline
        ↓
Current State
        ↓
Difference?
→ Potential Indicator
```


### Golden Image

- Image de référence validée servant à :
    - reconstruire un système ;
    - comparer son état ;
    - restaurer un environnement propre

> **Golden Image ≠ Backup** : elle représente une configuration de référence, pas nécessairement les données actuelles du système.
## Schémas réseau

- Les diagrammes réseau doivent être :
    - disponibles ;
    - précis ;
    - à jour.

Ils permettent de comprendre rapidement :

```
Internet
→ Firewall
→ DMZ
→ Internal Network
→ Critical Systems
```

Utiles pour :

- identifier les chemins possibles de propagation ;
- comprendre la segmentation ;
- isoler des systèmes ;
- suivre le lateral movement.
## Asset Management

- Disposer d’un inventaire central des assets :

```
Hostname
IP
OS
Owner
Location
Criticality
Role
Software
```

Sans inventaire fiable :

```
Unknown Asset
→ difficult to investigate
→ difficult to contain
```

L’asset inventory est donc directement utile à l’Incident Response.
## Comptes privilégiés dédiés à l’IR

- Prévoir des comptes avec les privilèges nécessaires pour intervenir sur les systèmes critiques.
- Ils ne devraient pas être utilisés en permanence.

Approche recommandée :

```
Incident confirmed
→ Enable IR Privileged Account
→ Perform actions
→ Disable account
→ Rotate credentials
```

Avantages :

- réduction de l’exposition permanente ;
- meilleure traçabilité ;
- accès disponible rapidement en cas d’urgence.

> Cela s’apparente à une approche **Just-In-Time / Break Glass**, à condition que l’usage soit strictement contrôlé et audité.
## Capacité d’achat d’urgence

- Un incident peut nécessiter rapidement :
    - stockage supplémentaire ;
    - forensic tools ;
    - licences ;
    - consultants ;
    - matériel.

Prévoir une procédure permettant un achat rapide jusqu’à un certain montant.

```
Incident
→ Need Tool Now
→ Emergency Procurement
→ No multi-week approval delay
```

## Cheat Sheets / Runbooks

- Préparer des aide-mémoires opérationnels pour :
    - acquisition disque ;
    - memory capture ;
    - live response ;
    - log collection ;
    - triage ;
    - IOC search ;
    - forensic analysis.

Objectif :

```
Stressful Incident
→ Standardized Checklist
→ Less Error
```

## Legal & Compliance
Certains incidents peuvent nécessiter :

- notification réglementaire ;
- communication clients ;
- notification partenaires ;
- coordination avec les autorités ;
- conservation spécifique des preuves.

Les exigences dépendent notamment :

- du type de données ;
- de la juridiction ;
- du secteur ;
- de la localisation de l’organisation et des personnes concernées.

> ⚠️ Le cours simplifie le RGPD : une violation de données personnelles susceptible d’engendrer un risque doit généralement être notifiée à **l’autorité de contrôle compétente**, pas automatiquement aux forces de l’ordre. Des obligations supplémentaires peuvent exister selon le contexte.

→ Legal / Compliance doit donc être impliqué **avant l’incident**, pas découvert au moment de la crise.
## Documentation pendant l’incident

 - La documentation ne doit pas seulement exister avant l’incident : elle doit être maintenue **pendant toute l’investigation**. 
 - Faire une main courante.

Pour chaque action :

```
Timestamp
Who
What
Where
Why
How
Result
```

Exemple :

```
02:31
SOC Analyst
→ isolated HOST-42 from network
→ EDR isolation
→ successful
```


### Questions fondamentales

```
Who?
What?
When?
Where?
Why?
How?
```

- Cette timeline aide pour :
    - investigation ;
    - coordination ;
    - forensic reporting ;
    - legal/compliance ;
    - lessons learned.

> Les actions de l’équipe IR elles-mêmes doivent être documentées, car elles peuvent modifier l’état du système ou des preuves.
## Outils logiciels & matériels

- L’équipe IR doit disposer des outils nécessaires **avant** qu’un incident ne survienne.
### Forensic Workstation

- Poste dédié à :
    - forensic imaging ;
    - memory analysis ;
    - log analysis ;
    - malware analysis ;
    - processing evidence.

```
Evidence
→ Dedicated Forensic Workstation
→ Analysis
```

- Il doit être isolé et traité comme un environnement potentiellement dangereux.

> Le cours évoque la désactivation de l’antivirus parce que des échantillons malveillants peuvent être manipulés. Cela doit se faire sur une **workstation/lab isolé**, pas sur un poste connecté normalement au réseau de production.
### Disk Forensics
Prévoir :

- forensic imaging tools ;
- disques de stockage dédiés ;
- write blockers.
#### Write Blocker

- Empêche la modification du support original pendant l’acquisition.

```
Original Disk
→ Write Blocker
→ Forensic Workstation
→ Forensic Image
```

Objectif :

- préserver l’intégrité de la preuve.
### Memory Forensics
Prévoir des outils pour :

```
RAM
→ Capture
→ Memory Dump
→ Analysis
```

La mémoire peut révéler :

- processes ;
- network connections ;
- loaded modules ;
- injected code ;
- credentials/secrets temporaires ;
- malware fileless.
### Live Response

- Acquisition d’informations sur une machine encore active.

Exemples :

- running processes ;
- users ;
- network connections ;
- logged-on sessions ;
- services ;
- volatile data.

```
Running System
→ Live Response
→ Volatile Evidence
```

> Certaines informations disparaissent après extinction : il faut donc décider avec prudence entre **live acquisition** et arrêt du système.

### Log Analysis
Prévoir des outils capables d’analyser :

- Windows Event Logs ;
- firewall logs ;
- EDR ;
- authentication logs ;
- application logs ;
- proxy / DNS ;
- SIEM.

```
Multiple Log Sources
→ Timeline / Correlation
→ Incident Reconstruction
```

### Network Capture & Analysis
Outils nécessaires pour :

- packet capture ;
- PCAP analysis ;
- flow analysis ;
- protocol analysis.

```
Network Traffic
→ PCAP / Flow
→ Analysis
→ C2 / Exfiltration / Lateral Movement
```

### IOC Management
Disposer d’une capacité à :

1. créer/enrichir des IOC ;
2. rechercher ces IOC dans tout l’environnement.

Exemples :

```
Hash
IP
Domain
URL
Filename
Registry Key
```


```
IOC identified on HOST-A
→ Search enterprise-wide
→ HOST-B / HOST-C also affected?
```


→ essentiel pour déterminer le **scope** réel de l’incident.
## Chain of Custody — Chaîne de possession

- Les preuves doivent être traçables depuis leur collecte jusqu’à leur stockage/analyse.

Documenter notamment :

```
Evidence ID
→ Collected by
→ Date / Time
→ Location
→ Transfer
→ Storage
→ Analyst
```

Objectifs :

- intégrité ;
- traçabilité ;
- admissibilité éventuelle ;
- démontrer qui a manipulé la preuve.
## Ticketing / Case Management

- Utiliser un système de suivi pour centraliser :

```
Incident
├─ Alerts
├─ Evidence
├─ Actions
├─ Timeline
├─ Owners
└─ Status
```

Cela facilite :

- coordination ;
- handover ;
- documentation ;
- reporting.
## Jump Bag

- Ensemble de matériel et outils **préparés à l’avance**, disponibles immédiatement en cas d’incident.

Peut contenir :

- forensic drives ;
- write blockers ;
- câbles ;
- network switch ;
- adaptateurs ;
- outils matériels ;
- software/media ;
- chain-of-custody forms ;
- alimentation.

```
Incident occurs
→ Grab Jump Bag
→ Respond immediately
```

Sans préparation :

```
Incident
→ Search for cables/tools/drives
→ Delay
→ Evidence / containment opportunity lost
```

## Infrastructure indépendante

- Un point particulièrement important : certains outils IR doivent être **indépendants de l’environnement potentiellement compromis**.

Cela concerne notamment :

- incident management ;
- documentation ;
- communication ;
- stockage de certaines informations critiques.

```
Corporate Domain
→ Assume Compromised

IR Infrastructure
→ Separate / Secure
```

Pourquoi ?

- AD peut être compromis ;
- email peut être lu ;
- file shares peuvent être indisponibles ;
- collaboration tools peuvent être contrôlés ;
- credentials internes peuvent être compromis.
### Out-of-Band Communication
Pendant un incident grave :

```
Do not assume:
Corporate Email = Safe
Teams/Slack = Safe
AD = Safe
```


Prévoir un canal **Out-of-Band — OOB** :

- comptes séparés ;
- infrastructure distincte ;
- téléphone sécurisé ;
- plateforme de communication indépendante.

```
Compromised Environment
      X
IR Communication Channel
```


> Principe : **Assume Breach**. Si le domaine entier est compromis, l’attaquant ne doit pas pouvoir observer les communications et décisions de l’équipe de réponse.
### Vue d'ensemble

```
Preparation
│
├─ People
│  ├─ IR Team
│  └─ Trained Staff
│
├─ Processes
│  ├─ Policies
│  ├─ Plans
│  ├─ Playbooks
│  ├─ Legal / Compliance
│  └─ Reporting
│
├─ Knowledge
│  ├─ Asset Inventory
│  ├─ Network Diagrams
│  └─ Baselines / Golden Images
│
├─ Tools
│  ├─ Forensic Workstation
│  ├─ Disk / Memory Tools
│  ├─ Network Tools
│  ├─ IOC Search
│  └─ Jump Bag
│
└─ Resilience
   ├─ Independent IR Platform
   └─ Out-of-Band Communications
```

- Le point central de la phase **Preparation** est d’éviter de découvrir pendant l’incident qu’il manque les **personnes, procédures, accès, outils, informations ou moyens de communication** nécessaires pour y répondre.
