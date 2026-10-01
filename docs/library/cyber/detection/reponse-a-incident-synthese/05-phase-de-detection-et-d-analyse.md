---
title: Phase de détection et d'analyse
source: Cyber/06 Détection & réponse/Réponse à incident — synthèse.md
note: Réponse à incident — synthèse
up:
- - Réponse à incident — synthèse
  - index.md
---

- La phase **Detection & Analysis** consiste à :
    - détecter les événements potentiellement malveillants ;
    - déterminer s’ils constituent réellement un incident ;
    - établir leur contexte ;
    - mesurer leur portée et leur gravité ;
    - commencer à reconstruire la chronologie de l’attaque.

```
Telemetry / Alert
→ Detection
→ Initial Triage
→ Context
→ Analysis
→ Incident Confirmed / Rejected
```

## Sources de détection
Un incident peut être détecté depuis plusieurs sources.
### Utilisateur / employé

- Un utilisateur remarque un comportement anormal :
    - pop-up inhabituel ;
    - fichier suspect ;
    - connexion étrange ;
    - comportement système anormal ;
    - email de phishing.

```
User
→ Suspicious Activity
→ Report
→ SOC / IR
```

### Outils de sécurité
Alertes provenant de :

- EDR ;
- AV ;
- IDS / IPS ;
- firewall ;
- SIEM ;
- email security ;
- application logs ;
- IAM / authentication systems.

```
Telemetry
→ Detection Rule
→ Alert
→ Analyst
```

> **Alert ≠ Incident** : une alerte est un signal nécessitant analyse et contextualisation.
### Threat Hunting

- Recherche **proactive** de comportements suspects qui n’ont pas forcément déclenché d’alerte.

```
Hypothesis
→ Search Telemetry
→ Suspicious Behavior
→ Investigation
```

Exemple :

```
"Un attaquant pourrait utiliser LSASS dumping"

→ rechercher T1003.001
→ process access
→ memory dump
→ suspicious tool execution
```

### Notification externe
Un tiers peut signaler une compromission :

- fournisseur ;
- partenaire ;
- CERT / CSIRT ;
- researcher ;
- law enforcement ;
- MSSP ;
- Threat Intelligence provider.

```
Third Party
→ IOC / Evidence
→ Internal Investigation
```

## Détection en profondeur
La détection doit être répartie sur plusieurs couches.

```
Internet
   ↓
Perimeter
   ↓
Internal Network
   ↓
Endpoint
   ↓
Application
```

### Périmètre réseau
Outils :

- firewall ;
- Internet-facing IDS / IPS ;
- DMZ monitoring ;
- proxy ;
- secure web gateway.

Permet notamment de détecter :

- reconnaissance ;
- exploitation externe ;
- connexions vers C2 ;
- trafic entrant/sortant inhabituel.
### Réseau interne
Outils :

- Pare-feu locaux ;
- IDS / NIDS ;
- network monitoring ;
- flow monitoring.

Objectifs :

- détecter lateral movement ;
- communications inhabituelles ;
- scans internes ;
- SMB / RDP suspects ;
- mouvements entre segments.
### Endpoint
Outils :

- AV ;
- EDR ;
- HIDS ;
- OS logs.

Permet de détecter :

- process suspects ;
- persistence ;
- credential dumping ;
- malware ;
- PowerShell abuse ;
- modifications système.
### Application
Sources : Principalement les journaux :

- application logs ;
- service logs ;
- database logs ;
- web server logs ;
- authentication logs.

Permet notamment d’identifier :

- abus de comptes ;
- injection ;
- accès anormal ;
- modifications non autorisées ;
- exploitation applicative.
## Enquête initiale — Initial Triage

- Lorsqu’un événement suspect est détecté, il faut d’abord **établir le contexte** avant de déclencher une réponse à incident à grande échelle.

```
Alert
→ Contextualize
→ Validate
→ Scope
→ Prioritize
```

-> Une information isolée peut être trompeuse.
Exemple :

```
Admin account
→ login to 10.0.10.15
→ 03:00
```

Sans contexte :

- quel système correspond à cette IP ?
- quel timezone ?
- utilisateur légitime ?
- maintenance planifiée ?
- source habituelle ?
- MFA validée ?
- activité associée ?

→ impossible de conclure correctement.
## Informations à collecter initialement
### Informations générales
Documenter :

- date / heure du signalement ;
- personne ayant détecté ou signalé l’incident ;
- méthode de détection ;
- type d’incident présumé.

Exemples :

```
Phishing
Malware
Account Compromise
Data Breach
System Outage
Unauthorized Access
```

### Systèmes impactés
Pour chaque système :

- hostname ;
- IP address ;
- OS ;
- physical / logical location ;
- owner ;
- fonction métier ;
- criticality ;
- état actuel ;
- utilisateurs ayant accédé au système.

```
Asset
├─ Hostname
├─ IP
├─ OS
├─ Owner
├─ Business Function
├─ Criticality
└─ Current State
```

### Activité observée
Documenter :

- actions effectuées ;
- comptes impliqués ;
- connexions ;
- changements réalisés ;
- activité encore en cours ou arrêtée.

```
Suspicious Activity
→ Still Active?
├─ Yes → containment may become urgent
└─ No  → preserve and investigate
```

### Malware
Si un malware est impliqué, collecter :

- date / heure de détection ;
- famille / type si connu ;
- systèmes impactés ;
- fichiers associés ;
- copies des samples ;
- hashes ;
- network indicators ;
- autres artefacts forensiques.

Exemples :

```
SHA-256
Filename
Path
IP
Domain
URL
Process
Registry Key
```

> Les samples doivent être manipulés dans un environnement adapté et isolé.
## Contexte métier

- La même compromission technique peut avoir une criticité très différente selon l’asset.

```
Compromised Intern Laptop
≠
Compromised CEO Laptop
≠
Compromised Domain Controller
```

Il faut donc toujours corréler :

```
Technical Impact
+
Asset Criticality
+
Business Impact
→ Incident Priority
```

## Construction de la timeline

- Dès l’enquête initiale, commencer une **chronologie de l’incident**.

Objectif :

- organiser les événements ;
- comprendre la progression de l’attaque ;
- corréler différentes sources ;
- identifier ce qui s’est produit avant/après un événement donné.

```
Evidence
→ Normalize Timestamps
→ Sort Chronologically
→ Build Timeline
```

### Structure minimale

|Date|Time|Hostname|Event|Data Source|
|---|---|---|---|---|
|09/09/2021|13:31 CET|SQLServer01|Mimikatz detected|Antivirus|

La timeline doit enregistrer notamment :

- authentifications ;
- process execution ;
- network connections ;
- file downloads ;
- account creation ;
- privilege changes ;
- lateral movement ;
- persistence ;
- exfiltration.
### Ordre de découverte ≠ ordre des événements

- Pendant l’enquête :

```
Evidence discovered
→ pas forcément dans l'ordre réel
```

Exemple :

```
Aujourd'hui :
Payload found on HOST-B

Puis :
Logs reveal same payload existed 2 weeks earlier on HOST-A
```


Après reconstruction :

```
HOST-A compromise
→ 2 weeks later
→ HOST-B compromise
```

-> La timeline permet donc de replacer chaque preuve dans son **contexte temporel réel**.
## Synchronisation temporelle
Pour construire une timeline fiable, vérifier :

- timezone ;
- UTC vs local time ;
- clock drift ;
- NTP ;
- format des timestamps.

```
Source A → UTC
Source B → CET
Source C → local time

→ Normalize
→ Unified Timeline
```

> Une mauvaise normalisation temporelle peut donner une fausse représentation de la séquence d’attaque.
## Gravité et étendue de l’incident

- Après le triage initial, déterminer :

```
Severity
→ How bad is it?

Scope
→ How far has it spread?
```

### Questions essentielles
#### Impact

- Quel est l’impact de l’exploitation ?
- Confidentialité affectée ?
- Intégrité ?
- Disponibilité ?
- Impact métier ?
#### Conditions d’exploitation

- Quelles conditions sont nécessaires ?
- Authentification requise ?
- Privileges requis ?
- Interaction utilisateur ?
- Accès réseau préalable ?

```
Exploitability
→ prerequisites?
→ complexity?
→ privileges?
```

#### Assets critiques

- Des systèmes business-critical peuvent-ils être affectés ?

Exemples :

- Domain Controller ;
- database ;
- ERP ;
- production systems ;
- backup infrastructure ;
- privileged accounts.
#### Remédiation

- Existe-t-il :
    - patch ;
    - workaround ;
    - IOC ;
    - mitigation ;
    - configuration fix ?
#### Scope

- Combien de systèmes sont touchés ?

```
1 endpoint
≠
50 endpoints
≠
Entire domain
```

→ plus le scope est large, plus l’incident doit être escaladé.
#### Exploitation active

- L’exploit est-il utilisé **in the wild** ?
- Existe-t-il des campagnes connues ?
- La vulnérabilité est-elle activement exploitée ?
#### Wormable

- Le mécanisme peut-il se propager automatiquement ?

```
Compromise Host A
→ automatically exploit Host B
→ Host C
→ Host D
```

-> Une capacité **wormable** peut transformer très rapidement un incident local en incident majeur.
## Priorisation

- La priorité peut être représentée conceptuellement par :

```
Severity
+
Scope
+
Asset Criticality
+
Exploitability
+
Business Impact
→ Incident Priority
```

Exemple :

```
Domain Controller
+
Credential Dumping
+
Active Adversary
+
Multiple Hosts
→ Critical Incident
```

## Confidentialité de l’incident

- Les informations liées à un incident doivent être diffusées selon le principe :

```
Need to Know
```


Pourquoi ?

- un insider peut être impliqué ;
- l’attaquant peut surveiller les communications ;
- des données sensibles peuvent être concernées ;
- implications juridiques ;
- communication publique à contrôler ;
- risque réputationnel.

```
Incident Information
→ Only Authorized Personnel
```

## Communication
La communication doit être coordonnée avec :

- Incident Manager ;
- management ;
- Legal ;
- Compliance ;
- Communication / PR.

```
IR Team
→ Incident Manager
→ Legal / Management
→ Authorized External Communication
```


> Les analystes ne doivent pas communiquer directement et spontanément aux clients, médias ou tiers sur un incident sensible.
## Attentes de l’enquête
Au début de l’investigation, définir :

- type d’incident supposé ;
- sources de preuves disponibles ;
- scope initial ;
- objectifs ;
- durée approximative ;
- limites de l’analyse.

```
Investigation
├─ What do we know?
├─ What evidence exists?
├─ What do we need to prove?
├─ What is the scope?
└─ What are our limitations?
```

Ces éléments peuvent évoluer avec l’apparition de nouvelles preuves.
## Reporting continu
Pendant l’incident, maintenir les parties concernées informées de :

- nouvelles découvertes ;
- changement de scope ;
- évolution de la gravité ;
- actions réalisées ;
- risques persistants ;
- prochaines étapes.

```
Investigation
→ Findings
→ Update Stakeholders
→ Adjust Response
```

Le point central de cette phase est de **transformer une alerte ou un signal brut en incident contextualisé, priorisé et documenté**, avec une compréhension initiale fiable de sa chronologie, de son impact et de son étendue.
