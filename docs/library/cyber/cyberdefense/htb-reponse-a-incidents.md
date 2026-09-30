---
title: HTB — Réponse à incidents
source: Cyber/05_Cyberdefense/HTB_Réponse à incidents.md
---

### Définition et portée de la gestion des incidents
- **Incident Handling — IH** désigne la capacité d’une organisation à gérer et répondre de manière structurée aux incidents de sécurité.
- Même avec des mesures préventives, une organisation doit être capable de réagir lorsqu’un incident affecte :
    - confidentialité ;
    - intégrité ;
    - disponibilité.
- Cette capacité peut être :
    - interne ;
    - externalisée auprès d’un prestataire ;
    - hybride.
- La gestion des incidents est un ensemble de procédures clairement définies pour gérer et répondre aux incidents de sécurité, permettant de : 
	- identifier ;
	- analyser ;
	- contenir ;
	- éradiquer ;
	- récupérer ;
	- documenter les incidents.
#### Cycle de vie
```
Preparation
    ↓
Detection & Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Post-Incident Activity
    ↺
```
<img src="../../assets/ir.png" alt="IR" width="550">
- Le processus est **itératif** :
    - les enseignements tirés d’un incident améliorent la préparation future.
- L’objectif final est de restaurer les opérations normales aussi rapidement et efficacement que possible.

> Un événement suspect peut devoir être traité **comme un incident jusqu’à preuve du contraire**, car sa nature réelle n’est parfois visible qu’après investigation initiale.
### Événement vs Incident
#### Événement — Event
- Un **événement** est une action qui se produit dans un système ou un réseau.

Exemples :
- Un utilisateur envoie un e-mail.
- Un clic de souris.
- Un pare-feu autorise une demande de connexion.
→ un événement n’est **pas forcément malveillant ou problématique**.
#### Incident
- Un **incident** est un événement ayant une conséquence négative.

Exemples :
- panne système ;
- accès non autorisé ;
- perte de disponibilité ;
- catastrophe naturelle ;
- panne électrique.
#### Incident de sécurité informatique
- Il n’existe pas une définition universelle unique.
- Dans le cours, un incident de sécurité est considéré comme un événement dirigé contre un système avec une intention claire de causer un préjudice.

Exemples :
- vol de données ;
- vol de fonds ;
- accès non autorisé ;
- installation de malware ;
- utilisation d’outils d’accès à distance.
```
Event
→ activité observée

Incident
→ conséquence négative

Security Incident
→ événement malveillant ou compromission nécessitant une réponse
```
### Portée de la gestion des incidents
- La gestion des incidents ne concerne pas uniquement les intrusions.
Elle couvre aussi :
- insider threat ;
- availability issues ;
- perte de propriété intellectuelle ;
- compromission de données ;
- incidents techniques ;
- incidents physiques ou environnementaux.
```
Incident Handling
≠ seulement intrusion réseau
```
### Valeur de la gestion des incidents
- Les incidents peuvent toucher :
    - quelques endpoints ;
    - un système critique ;
    - une grande partie de l’environnement.
- Une équipe spécialisée permet d’appliquer une réponse :
    - structurée ;
    - cohérente ;
    - documentée ;
    - reproductible.
Objectifs :
```
Incident
→ Investigation
→ Remediation
→ Minimize Impact
```
La réponse cherche notamment à limiter :
- vol d’informations ;
- interruption de service ;
- propagation ;
- impact métier.
### Priorisation des incidents
- Tous les incidents n’ont pas la même criticité.
Il faut évaluer :
- gravité ;
- impact ;
- nombre de systèmes concernés ;
- données touchées ;
- criticité métier ;
- urgence.
```
High Severity
→ Immediate Response
→ More Resources

Lower Severity
→ Initial Investigation
→ Confirm / Reject Incident
```
### Équipe de réponse aux incidents
- L’équipe de gestion des incidents est souvent appelée **Incident Response Team**.
- Elle peut être dirigée par :
    - SOC Manager ;
    - CISO / RSSI ;
    - CIO / DSI ;
    - prestataire tiers de confiance.
#### Incident Manager
- Coordonne les activités de réponse.
- Doit pouvoir :
    - obtenir les informations nécessaires ;
    - mobiliser d’autres équipes ;
    - suivre l’avancement ;
    - centraliser la communication.
```
Incident Manager
→ Coordination
→ Communication
→ Tracking
→ Decision Support
```
- Il agit comme **point de communication unique** pendant l’incident.
## Exemples de causes d’incidents réels

### Fuites d'identifiants - Credentials compromis
#### Rançongiciel contre Colonial Pipeline 
- Le Colonial Pipeline, un important système d'oléoducs américain, a été victime d'une attaque par rançongiciel (ransomware).
- Cette [attaque](https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack) provenait d'un MDP personnel d'un employé qui avait été compromis, probablement trouvé sur le dark web, plutôt que d'une attaque directe sur le réseau de l'entreprise.
- Les attaquants ont accédé aux systèmes de l'entreprise en utilisant un mot de passe compromis pour un compte VPN inactif, qui n'avait pas la MFA activée.
```
- Compromission d’un compte VPN.
- Password compromis.
- Compte inactif.
- MFA non activée.

Compromised Password
+
No MFA
→ VPN Access
→ Incident
```
### Identifiants faibles / par défaut
#### Botnet Mirai (2016)
- Botnet Mirai scan d’équipements IoT utilisant des identifiants d'usine ou par défaut
- Les appareils compromis sont intégrés dans un botnet DDoS massif.
- La cause première était que les appareils étaient livrés avec des identifiants par défaut non modifiés.
#### Incident LogicMonitor (2023)
- Certains comptes clients avait été fournis avec des MDP par défaut faibles.
- Les clients concernés ont subi des incidents de rançongiciel consécutifs ou des accès non autorisés.
- Conséquences :
    - accès non autorisé ;
    - ransomware pour certains clients.
### Logiciels obsolètes / systèmes non patchés
#### Fuite de données d'Equifax — 2017
- Exploitation d'une vuln Apache Struts (CVE-2017-5638) dans l'application web d'Equifax.
- Le correctif était disponible mais n’avait pas été appliqué à temps.
- Résultat :
    - fuite massive de données personnelles.
    - Cette faille a exposé les données personnelles d'environ 143 à 147 millions de personnes, entraînant des conséquences réglementaires et juridiques majeures.
#### WannaCry — 2017
- Ransomware avec propagation de type worm en utilisant l'exploit SMB EternalBlue.
- Exploit :
```
EternalBlue
→ SMB
→ MS17-010
```
- Plus de 200 000 systèmes affectés dans plus de 150 pays.
- Cet incident était dû à des systèmes Windows non corrigés, bien que le correctif MS17-010 ait été disponible avant l'épidémie.
### Menace interne - Insider Threat
#### CCash App / Block Inc. (Divulgation en 2021 ; Avis public en 2022)
- Un ancien employé a accédé aux informations personnelles de millions d'utilisateurs de Cash App.
- Environ 8,2 millions de clients actuels et anciens ont été potentiellement touchés, ce qui a entraîné un examen réglementaire et des règlements.
- Cause principale :
    - abus d’un accès légitime ;
    - contrôles internes insuffisants ;
    - monitoring insuffisant.
```
Legitimate Access
→ Misuse
→ Data Exposure
```
### Phishing / Social Engineering
- Le phishing peut servir à :
    - voler des credentials ;
    - délivrer un malware ;
    - obtenir un foothold ;
    - faciliter la fraude.
#### Attaque par hameçonnage du Département de l'Intérieur des États-Unis
- Les attaquants ont utilisé une technique de "evil twin" pour inciter les individus à se connecter à un faux Wi-Fi, permettant aux pirates de voler des identifiants et d'accéder au réseau
- Cet incident a révélé un manque d'infrastructure de réseau sans fil sécurisée et des mesures de sécurité insuffisantes, notamment une authentification utilisateur faible et des tests de réseau inadéquats.
#### Twitter — 2020
- Compromission de comptes à forte visibilité pour promouvoir une arnaque au bitcoin.
 - Accès aux outils d'administration de Twitter, leur permettant de modifier les comptes et de publier directement des tweets.
- Social engineering contre des employés.
### Supply Chain Attack
#### SolarWinds Orion — 2020
- Compromission, par acteurs étatiques, de l’environnement de build/publication.
- Backdoor ajoutée aux updates Orion.
- Distribution à des milliers de clients de la mise à jour compromise à de nombreux clients.
- Cela a provoqué un espionnage et un accès non autorisé à grande échelle dans les secteurs gouvernemental et privé
```
Vendor Compromise
→ Malicious Update
→ Customers Install Update
→ Widespread Access
```
## Rapports d’incident
- Un rapport d’incident doit documenter les événements de manière **chronologique et séquentielle**.
- Il peut être aligné sur :
	- Cyber Kill Chain ;
	- MITRE ATT&CK.
- Exemple de rapport : 
	- DFIR Labs : https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/
	- La plateforme DFIR Labs contient de nombreux autres rapports d'incident. : https://thedfirreport.com/
	- Cybereason : https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf
Exemple de progression :
```
Initial Access
→ Execution
→ Persistence
→ Privilege Escalation
→ Lateral Movement
→ Exfiltration
→ Impact
```
### Rapports spécifiques à un incident
- Se concentre sur **un incident particulier**.
- Décrit notamment :
    - comment l’attaquant est entré ;
    - quelles actions ont été réalisées ;
    - comment l’incident a été détecté ;
    - quels systèmes ont été affectés ;
    - quel impact a été observé.
```
One Incident
→ Detailed Timeline
→ Technical Findings
→ Lessons Learned
```
#### Rapports globaux sur la réponse aux incidents
- Agrège les données issues de nombreux incidents.
- Objectifs :
    - identifier les tendances ;
    - observer les TTP récurrentes ;
    - repérer les menaces émergentes ;
    - produire des statistiques ;
    - proposer des recommandations générales.
```
Many Incidents
→ Aggregate Data
→ Trends
→ Threat Landscape
```
- Par exemple rapport de l'Unit 42 :
	- https://www.paloaltonetworks.com/engage/unit42-2025-global-incident-response-report
## Scénario (fictif) d'incident
- Le module utilise un scénario fictif autour de **Insight Nexus**, entreprise manipulant des données concurrentielles sensibles.
- Deux threat actors distincts opèrent simultanément dans son environnement.
### Premier acteur de menace
- Après une mise à jour, les administrateurs n’avaient pas modifié les credentials par défaut.
Point d’entrée :
```
ManageEngine ADManager Plus
→ Internet-facing
→ default credentials admin/admin
```
Progression :
```
Default Credentials
→ Initial Access
→ Reconnaissance
→ User / Machine Enumeration
→ Privileged AD Account Creation
→ Pivot
→ Exposed RDP
→ Increased Control
→ GPO Abuse
→ MSI Deployment
→ Spyware on Multiple Endpoints
```
Ce scénario illustre plusieurs faiblesses combinées :
- default credentials ;
- service Internet-facing ;
- création de comptes privilégiés ;
- mauvaise configuration RDP ;
- abuse de GPO ;
- déploiement de malware à grande échelle.
## Phase de préparation — Preparation

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

---

### Prérequis pour la préparation

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

---

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

---

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

---

### Incident Response Policy / Plan / Procedures

Il faut distinguer :

#### Policy

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

---

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
- médias.

> Une communication non coordonnée pendant un incident peut créer des risques juridiques, opérationnels ou réputationnels.

---

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

#### Golden Image

- Image de référence validée servant à :
    - reconstruire un système ;
    - comparer son état ;
    - restaurer un environnement propre.

> **Golden Image ≠ Backup** : elle représente une configuration de référence, pas nécessairement les données actuelles du système.

---

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

---

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

---

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

---

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

---

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

---

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

---

## Documentation pendant l’incident

La documentation ne doit pas seulement exister avant l’incident : elle doit être maintenue **pendant toute l’investigation**.

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

#### Questions fondamentales

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

---

## Outils logiciels & matériels

L’équipe IR doit disposer des outils nécessaires **avant** qu’un incident ne survienne.

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## Infrastructure indépendante

Un point particulièrement important : certains outils IR doivent être **indépendants de l’environnement potentiellement compromis**.

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

---

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

---

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

Le point central de la phase **Preparation** est d’éviter de découvrir pendant l’incident qu’il manque les **personnes, procédures, accès, outils, informations ou moyens de communication** nécessaires pour y répondre.
