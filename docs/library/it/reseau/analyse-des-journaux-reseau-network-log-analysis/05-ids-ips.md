---
title: IDS / IPS
source: IT/04 Réseau/Journaux & investigation/Analyse des journaux réseau (Network Log Analysis).md
note: Analyse des journaux réseau (Network Log Analysis)
up:
- - Analyse des journaux réseau (Network Log Analysis)
  - index.md
---

Source : [Hack The Box Academy - Network Log Analysis](https://academy.hackthebox.com/course/preview/network-log-analysis)

## Analyse des logs IDS / IPS

- Les **IDS/IPS** complètent les contrôles réseau classiques des firewalls.
- Un firewall décide principalement selon :
    - IP ;
    - port ;
    - protocole ;
    - policy ;
    - état de connexion.
- Un IDS/IPS peut inspecter plus profondément le trafic pour identifier des patterns correspondant à des attaques.

```text
Firewall
→ "Is this communication allowed?"

IDS / IPS
→ "Does this traffic look malicious?"
```


Exemples de détection :

```text
Exploit
Port Scan
Brute Force
Code Injection
Botnet Traffic
DoS / DDoS
Malware / Trojan Activity
```


## IDS vs IPS

| Technologie | Fonction |
|---|---|
| **IDS — Intrusion Detection System** | Détecte et alerte |
| **IPS — Intrusion Prevention System** | Détecte et peut bloquer |

```text
IDS
→ Detect
→ Alert

IPS
→ Detect
→ Block / Prevent
```


Différence fondamentale :

```text
IDS
→ généralement passive / out-of-band

IPS
→ généralement inline
→ peut empêcher le trafic d'atteindre la cible
```


> IDS et IPS utilisent souvent les mêmes moteurs/signatures, mais ce ne sont pas simplement « le même produit avec une action différente » dans tous les cas : leur **positionnement réseau et leur mode de fonctionnement** peuvent également différer.

## Signatures IDS / IPS

Une **signature** définit des critères permettant de reconnaître une activité connue ou suspecte.

```text
Network Traffic
→ Signature Matching
→ Match?
├─ No  → No Alert
└─ Yes → Detect / Block
```


Une signature peut rechercher :

- séquence d’octets ;
- pattern protocolaire ;
- URI particulière ;
- header ;
- comportement réseau ;
- payload connu ;
- caractéristique d’un exploit.

### Signature Database

Les signatures sont regroupées dans une base régulièrement mise à jour.

Exemples de solutions :

```text
Snort
Suricata
```


Une règle peut être configurée pour :

```text
alert
drop
reject
```


selon :

- moteur ;
- mode IDS / IPS ;
- configuration.

## Limites des signatures

Les signatures sont particulièrement efficaces contre :

```text
Known Attacks
Known Exploits
Known Malware Patterns
```


Mais peuvent être moins efficaces contre :

- zero-days ;
- trafic fortement obfusqué ;
- protocoles chiffrés non inspectés ;
- variations d’un exploit ;
- techniques inconnues.

```text
No Signature Match
≠ Traffic Benign
```


## IDS/IPS dans le SOC

Les IDS/IPS génèrent généralement beaucoup d’événements.

Workflow :

```text
Network Traffic
→ IDS / IPS
→ Signature Trigger
→ Event
→ SIEM
→ Correlation
→ SOC Alert
```


Le SIEM peut regrouper plusieurs événements selon :

- severity ;
- category ;
- source IP ;
- destination IP ;
- fréquence ;
- période ;
- autres alertes associées.

## Corrélation de plusieurs événements

Exemple :

```text
Source IP
→ Port Scan
→ Exploit Attempt
→ Malware / C2 Activity
```


Pris séparément :

```text
Port Scan
→ reconnaissance possible
```


Mais ensemble :

```text
Port Scan
+
Exploit Signature
+
Same Source
+
Same Target
→ Much Stronger Signal
```


Le contexte et la séquence d’activité sont donc essentiels.

## Exemple de log IPS

```text
srcip=12.11.2.4
dstip=19.66.201.16
srcport=57673
dstport=53
proto=17
service="DNS"
severity="high"
action="detected"
attack="DNS.Server.Label.Buffer.Overflow"
attackid=37088
direction="incoming"
```


Interprétation initiale :

```text
12.11.2.4:57673
→ UDP/53
→ 19.66.201.16
→ DNS.Server.Label.Buffer.Overflow
→ Severity = High
→ Action = Detected
```


## Champs importants (IDS / IPS)

### Identification de l’équipement

```text
devname
→ nom du système

devid
→ identifiant du device
```


### Temps

```text
date
time
tz
```


Toujours tenir compte de la timezone lors de la reconstruction d’une timeline.

### Type d’événement

```text
type
subtype
eventtype
```


Exemple :

```text
type="utm"
subtype="ips"
eventtype="signature"
```


### Source / Destination

```text
srcip
→ Source IP

srcport
→ Source Port

dstip
→ Destination IP

dstport
→ Destination Port
```


Permet de répondre à :

```text
Who attacked?
→ Which target?
→ On which service?
```


### Pays

```text
srccountry
dstcountry
```


→ enrichment géographique.

> La géolocalisation IP est approximative et ne permet pas d’attribuer physiquement un attaquant.

### Service / Protocol

```text
proto=17
→ UDP

service="DNS"

dstport=53
```


Cela permet de vérifier si l’attaque vise un service cohérent avec la signature.

### Attack / Attack ID

```text
attack
→ nom de la signature / attaque

attackid
→ identifiant associé
```


Exemple :

```text
DNS.Server.Label.Buffer.Overflow
```


### Severity

```text
low
medium
high
critical
```


La severity permet de prioriser l’analyse.

Mais :

```text
High Severity
≠ Confirmed Compromise
```


> ⚠️ Un niveau High/Critical ne rend pas à lui seul un faux positif moins probable : la qualité d’une signature, le contexte et l’environnement cible comptent davantage que le niveau affiché.

## Action (IDS / IPS)

Champ essentiel :

```text
action
```


Exemples possibles :

```text
detected
blocked
dropped
reset
```


### `detected`

```text
action="detected"
```


→ l’IDS/IPS a détecté le trafic mais **ne l’a pas bloqué**.

### `blocked`

```text
action="blocked"
```


→ le moteur a empêché le trafic selon sa configuration.

## Détection ≠ exploitation réussie

Très important :

```text
Signature Triggered
≠ Exploit Successful
```


Si :

```text
action="detected"
```


cela signifie principalement :

```text
Suspicious Traffic Observed
→ Not Prevented by IPS
```


Cela ne prouve pas que :

```text
Target Compromised
```


Il faut vérifier :

- service réellement exposé ;
- version du logiciel ;
- vulnérabilité présente ;
- réponse du serveur ;
- logs endpoint ;
- EDR ;
- activité post-exploitation.

## Vérifier le service ciblé

Dans l’exemple :

```text
Attack:
DNS.Server.Label.Buffer.Overflow

Destination:
19.66.201.16:53
```


La signature concerne une vulnérabilité liée à un serveur DNS spécifique.

Question essentielle :

```text
What service is actually running on 19.66.201.16:53?
```


Si :

```text
Target Service
≠ Vulnerable Product
```


alors la signature peut correspondre à :

```text
Exploit Attempt
→ Not Applicable to Target
```


→ attaque probablement sans impact.

## Vulnérabilité et exposition

Workflow :

```text
IDS Alert
→ Identify Target Service
→ Identify Product / Version
→ Vulnerable?
├─ No  → Likely unsuccessful / FP context
└─ Yes → Escalate Investigation
```


Si la cible exploite précisément le produit/version vulnérable :

```text
Matching Exploit
+
Vulnerable Service
+
Traffic Reached Target
→ High Priority
```


## Direction de l’attaque

Toujours vérifier :

```text
direction
```


### Inbound

```text
Internet
→ Internal Target
```


Peut correspondre à :

- exploitation externe ;
- reconnaissance ;
- brute force ;
- scanning.

### Outbound

```text
Internal Host
→ External Destination
```


Peut correspondre à :

- malware ;
- botnet ;
- C2 ;
- exploitation sortante ;
- système interne déjà compromis.

## Analyse de la severity

La priorité ne doit pas reposer uniquement sur :

```text
severity="high"
```


Une meilleure logique :

```text
Signature Severity
+
Target Criticality
+
Service Exposure
+
Vulnerability Applicability
+
Action Taken
+
Repeated Activity
+
Other Telemetry
→ Incident Priority
```


## Signature unique vs plusieurs signatures

### Une seule signature

```text
Same Source
→ Single Signature
→ Single Target
```


Peut représenter :

- scan Internet automatique ;
- false positive ;
- tentative opportuniste ;
- attaque isolée.

### Plusieurs signatures

```text
Same Source
→ Scan
→ Exploit 1
→ Exploit 2
→ Malware Activity
```


→ signal nettement plus fort.

```text
Multiple Related Signatures
+
Same Source / Target
+
Short Time Window
→ Escalate
```


## Corrélation avec Firewall

IDS/IPS et firewall doivent être analysés ensemble.

Exemple :

```text
IPS
→ Exploit detected

Firewall
→ action=accept
```


→ le trafic a été autorisé par la policy réseau.

Autre cas :

```text
IPS
→ Exploit detected

Firewall
→ deny
```


→ tentative détectée mais trafic ensuite bloqué selon l’architecture / séquence d’inspection.

## Tentative bloquée ≠ investigation inutile

Même si :

```text
action=blocked
```


il faut parfois rechercher :

- tentatives précédentes ;
- autres destinations ciblées ;
- mêmes signatures depuis la source ;
- trafic précédemment `accept` ;
- autres IOC liés.

```text
Blocked Attack
→ Check Historical Activity
```


## Port Scan (IDS / IPS)

Pattern :

```text
One Source
→ Many Ports
→ Same Target
```


Exemple :

```text
10.0.10.5
→ :22
→ :80
→ :443
→ :445
→ :3389
```


IDS/IPS peut générer une signature de :

```text
Port Scan
```


Puis, si la source attaque un service découvert :

```text
Port Scan
→ Exploit Attempt
```


→ corrélation particulièrement importante.

## Vulnerability Scan

Pattern :

```text
One Source
→ Many Exploit Signatures
→ Multiple Services
```


Peut correspondre à :

- scanner légitime ;
- vulnerability scanner ;
- attaquant effectuant une reconnaissance automatisée.

Il faut vérifier :

```text
Is Source an Authorized Scanner?
```


## Code Injection

IDS/IPS peut détecter des patterns correspondant à :

```text
SQL Injection
Command Injection
Code Injection
```


Exemple :

```text
HTTP Request
→ Suspicious Payload
→ Signature Trigger
```


Puis corréler avec :

- WAF ;
- web server logs ;
- application logs ;
- EDR.

## Brute Force

Certaines signatures identifient :

```text
Repeated Authentication Attempts
→ Same Source
→ Same Service
```


Exemples :

```text
SSH
RDP
FTP
Web Login
```


Pour confirmer :

```text
IDS Alert
+
Authentication Logs
→ Successful / Failed Attempts
```


## DoS / DDoS

IDS/IPS peut détecter :

```text
Traffic Flood
Malformed Requests
Connection Flood
```


Pattern :

```text
Many Sources
→ Same Target
→ High Request Rate
```


→ possible DDoS.

## Trojan / Botnet

Certaines signatures détectent :

- protocoles C2 connus ;
- payloads spécifiques ;
- botnet communication ;
- malware infrastructure.

```text
Internal Host
→ Known Botnet Pattern
→ External Destination
```


→ très intéressant car cela peut indiquer un endpoint déjà compromis.

## Faux positifs

Un IDS/IPS peut produire des **False Positives**.

Causes possibles :

```text
Legitimate Application
→ matches signature pattern

Authorized Scanner
→ triggers exploit rules

Custom Protocol
→ resembles malicious traffic
```


Donc :

```text
IDS Alert
→ Evidence to Investigate
≠ Automatic Incident
```


## False Negative

L’inverse existe également :

```text
No IDS Alert
≠ No Attack
```


Raisons :

- signature inexistante ;
- trafic chiffré ;
- obfuscation ;
- packet fragmentation ;
- technique inconnue ;
- visibilité réseau insuffisante.

## Corrélation avec EDR (IDS / IPS)

Exemple :

```text
IPS
→ Exploit against HOST-A

EDR
→ powershell.exe spawned

Network
→ HOST-A contacts external IP
```


Cela permet de passer de :

```text
Exploit Attempt
```


à :

```text
Possible Successful Compromise
```


## Corrélation SOC complète

```text
IDS / IPS
→ What attack was attempted?

Firewall
→ Was traffic allowed?

Asset Inventory
→ What service/version is running?

EDR
→ What happened on the host?

Authentication Logs
→ Was access obtained?

Network / Proxy / DNS
→ What happened afterward?
```


## Exemple d’investigation (IDS / IPS)

```text
14:01
IDS
→ Port Scan detected
→ Source 12.11.2.4

14:03
IPS
→ DNS Buffer Overflow signature
→ same source
→ target 19.66.201.16:53

14:04
Firewall
→ traffic accepted

14:05
EDR
→ suspicious process spawned

14:06
Network
→ target contacts unknown external IP
```


Interprétation possible :

```text
Reconnaissance
→ Exploitation
→ Execution
→ Possible C2
```


→ priorité élevée.

## Réponse / Blocage

Bloquer l’IP attaquante peut être nécessaire.

En pratique :

```text
Malicious Source
→ Validate Context
→ Block if appropriate
```


Mais considérer :

- shared hosting ;
- NAT ;
- CDN ;
- cloud provider ;
- spoofing ;
- source compromise ;
- durée du blocage.

> Le blocage d’IP est une mesure de containment utile, mais rarement suffisante à lui seul.

## Vue d’ensemble (IDS / IPS)

```text
IDS / IPS Log
│
├─ Timestamp
├─ Source IP / Port
├─ Destination IP / Port
├─ Protocol / Service
├─ Direction
├─ Signature / Attack
├─ Attack ID
├─ Severity
└─ Action
```


Workflow SOC :

```text
IDS/IPS Alert
      ↓
Identify Source / Target
      ↓
Check Signature
      ↓
Check Direction
      ↓
Check Severity
      ↓
Was it Detected or Blocked?
      ↓
Is Target Service Vulnerable?
      ↓
Search Related Signatures
      ↓
Correlate Firewall / EDR / Logs
      ↓
Attempt or Successful Compromise?
```


Le point essentiel est de distinguer **détection d’un pattern d’attaque** et **compromission réelle**. Une signature IDS/IPS indique qu’un trafic correspond à une règle connue ; pour déterminer son impact réel, il faut vérifier **le service ciblé, sa vulnérabilité, l’action du dispositif et surtout les événements observés avant et après sur le firewall, l’endpoint et le reste du réseau**.
