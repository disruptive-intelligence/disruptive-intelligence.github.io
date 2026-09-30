---
title: Outils logiciels & matériels
source: Cyber/05_Cyberdefense/HTB_Réponse à incidents.md
note: HTB — Réponse à incidents
up:
- - HTB — Réponse à incidents
  - index.md
---

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
