---
title: Pare-feu
source: IT/04 Réseau/Journaux & investigation/Analyse des journaux réseau (Network Log Analysis).md
note: Analyse des journaux réseau (Network Log Analysis)
up:
- - Analyse des journaux réseau (Network Log Analysis)
  - index.md
---

Source : [Hack The Box Academy - Network Log Analysis](https://academy.hackthebox.com/course/preview/network-log-analysis)

## Analyse des logs Firewall

- Un **firewall** contrôle le trafic réseau entrant et sortant selon des règles de sécurité.
- Il peut être :
    - local à un endpoint / serveur ;
    - virtuel ;
    - physique ;
    - centralisé au périmètre du réseau.

```text
Source
→ Firewall
→ Rule Evaluation
→ Allow / Deny / Drop
→ Destination
```


Pour un SOC, les logs firewall permettent surtout de déterminer :

```text
Who communicated?
→ With whom?
→ On which port/protocol?
→ Was it allowed?
→ How much data?
→ For how long?
```


## Firewall traditionnel vs NGFW

Un firewall classique filtre principalement selon :

- source IP ;
- destination IP ;
- source/destination port ;
- protocol ;
- interface ;
- état de connexion.

Les **NGFW — Next-Generation Firewalls** ajoutent notamment une visibilité **Layer 7** :

```text
IP / Port
+
Application Identification
+
User / Content / Threat Context
```


Exemples d’applications identifiées :

```text
HTTP
HTTPS
SSH
DNS
RDP
BitTorrent
```


Cela permet par exemple de bloquer :

```text
SSH
```


même si celui-ci utilise un port autre que `22`, si le firewall reconnaît effectivement le protocole/application.

> `Port ≠ Application` : TCP/443 peut transporter HTTPS, mais également d’autres protocoles encapsulés. L’**Application Identification** cherche à reconnaître le trafic lui-même plutôt que de se fier uniquement au port.

## Champs principaux des Traffic Logs

Un log firewall contient généralement :

```text
Timestamp
Source IP / Port
Destination IP / Port
Protocol
Interfaces
Action
Policy
Bytes / Packets
Duration
NAT
```


Exemple du cours :

```text
srcip=172.14.14.26
srcport=50495
dstip=142.250.186.142
dstport=443
proto=6
action="accept"
service="HTTPS"
duration=72
sentbyte=2518
rcvdbyte=49503
```


### Date / équipement

```text
date
→ date de l'événement

time
→ heure

tz
→ timezone

devname
→ hostname du firewall

devid
→ identifiant du device
```


La **timezone** est importante pour la corrélation :

```text
Firewall
+
EDR
+
Windows Logs
+
SIEM
→ Normalize Time
→ Unified Timeline
```


### Type de log

```text
type
→ catégorie principale

subtype
→ sous-catégorie
```


Exemples :

```text
type=traffic
subtype=forward
```


Selon le produit, on peut également retrouver :

```text
VPN
Web Filter
IPS
Antivirus
System
UTM
```


### Source

```text
srcip
→ Source IP

srcname
→ Source hostname

srcport
→ Source port

srcintf
→ Source interface

srcintfrole
→ LAN / WAN / DMZ...
```


Exemple :

```text
172.14.14.26:50495
→ Source
```


### Destination

```text
dstip
→ Destination IP

dstport
→ Destination port

dstintf
→ Destination interface

dstintfrole
→ role de l'interface
```


Exemple :

```text
142.250.186.142:443
→ Destination
```


### Protocol

Dans l’exemple :

```text
proto=6
```


correspond à :

```text
IP Protocol 6
→ TCP
```


Autres valeurs classiques :

```text
6  → TCP
17 → UDP
1  → ICMP
```


### Géolocalisation

```text
srccountry
dstcountry
```


→ géolocalisation estimée des IP.

Exemple :

```text
dstcountry="United States"
```


> La géolocalisation IP reste approximative et ne constitue pas une preuve de localisation physique de l’attaquant.

Elle est surtout utile pour :

- anomalous country access ;
- policy enforcement ;
- enrichment ;
- triage.

### Action

Le champ :

```text
action
```


indique le résultat de la décision du firewall ou de la session.

Valeurs possibles selon le produit :

#### `accept`

```text
Traffic allowed
```


#### `deny`

```text
Traffic blocked
```


#### `drop`

```text
Traffic silently discarded
```


#### `close`

```text
Session closed normally
```


#### `client-rst`

```text
TCP session reset by client
```


#### `server-rst`

```text
TCP session reset by server
```


> ⚠️ La signification exacte de `deny`, `drop`, `close`, etc. est **vendor-specific**. Il ne faut pas supposer que `deny` implique toujours qu’une notification soit envoyée à la source : vérifier la documentation du firewall concerné.

### Service / Application

```text
service="HTTPS"
```


peut indiquer :

- service déduit du port ;
- application réellement identifiée ;

selon le produit et le type de log.

Il faut donc distinguer :

```text
Service / Port Mapping
≠
Application Identification
```


### NAT

Dans l’exemple :

```text
trandisp="snat"
transip=89.145.185.195
transport=50495
```


Cela indique une **Source NAT — SNAT**.

```text
Internal Host
172.14.14.26:50495
        ↓
SNAT
        ↓
89.145.185.195:50495
        ↓
Internet
```


Champs utiles :

```text
transip
→ translated IP

transport
→ translated port
```


En investigation, la conservation des informations NAT est essentielle pour relier une connexion externe à l’hôte interne réellement responsable.

### Durée et volume

```text
duration
→ durée de la session

sentbyte
→ bytes envoyés

rcvdbyte
→ bytes reçus

sentpkt
→ packets envoyés

rcvdpkt
→ packets reçus
```


Ces champs sont particulièrement utiles pour détecter :

- exfiltration ;
- downloads massifs ;
- beaconing ;
- sessions anormalement longues ;
- transferts asymétriques.

## Méthode d’analyse initiale

Commencer généralement par :

```text
Source IP
→ Destination IP
→ Destination Port
→ Protocol
→ Action
```


Puis enrichir avec :

```text
Policy
Application
NAT
Bytes
Packets
Duration
Timeline
```


Exemple :

```text
src=10.0.10.15
dst=185.x.x.x
dstport=443
action=accept
```


→ la connexion a été autorisée par le firewall.

Mais :

```text
action=accept
≠ connection necessarily malicious
≠ application necessarily succeeded
```


Il faut corréler avec la télémétrie endpoint/application.

### Filtrage pendant une investigation

Si un IOC est connu :

```text
Suspicious IP
→ Search as srcip
→ Search as dstip
```


Cela permet de répondre à :

```text
Which hosts contacted it?
Was traffic allowed?
How often?
How much data?
When?
```


## IOC Communication

Exemple :

```text
Threat Intel
→ 185.x.x.x = malicious C2

Firewall Search
→ dstip=185.x.x.x
```


Résultats possibles :

```text
HOST-A → accept
HOST-B → deny
HOST-C → accept
```


→ HOST-A et HOST-C deviennent prioritaires pour investigation.

### Corrélation Antivirus / EDR + Firewall

Exemple :

```text
Defender
→ Malware detected on HOST-A

Firewall
→ HOST-A communicated with 185.x.x.x
```


On peut alors rechercher :

```text
Which other hosts contacted 185.x.x.x?
```


```text
Firewall Logs
→ HOST-B
→ HOST-C
```


→ extension possible du **scope** de l’incident.

## Port Scanning (firewall)

Les firewall logs peuvent révéler un scan.

### Vertical Scan

```text
One Source
→ One Destination
→ Many Ports
```


Exemple :

```text
10.0.10.5
→ 10.0.10.20:22
→ 10.0.10.20:80
→ 10.0.10.20:445
→ 10.0.10.20:3389
```


→ reconnaissance des services disponibles.

### Horizontal Scan

```text
One Source
→ Many Destinations
→ Same Port
```


Exemple :

```text
10.0.10.5
→ HOST-A:445
→ HOST-B:445
→ HOST-C:445
→ HOST-D:445
```


→ recherche de systèmes exposant SMB.

## Lateral Movement (firewall)

Les communications internes inhabituelles peuvent révéler du lateral movement.

```text
Workstation
→ Server:445
→ Server:3389
→ Server:5985
```


Ports intéressants :

```text
445  → SMB
3389 → RDP
5985 → WinRM HTTP
5986 → WinRM HTTPS
22   → SSH
```


```text
Unexpected East-West Traffic
+
Administrative Protocol
+
Compromised Source
→ Possible Lateral Movement
```


### North-South vs East-West

En architecture réseau, on parle plutôt de :

```text
East-West
→ internal ↔ internal

North-South
→ internal ↔ external
```


Donc :

```text
LAN → LAN
→ East-West
→ peut correspondre à du lateral movement

LAN → WAN / WAN → LAN
→ North-South
```


`Vertical access` n’est pas le terme standard pour désigner simplement du trafic LAN↔WAN.

## Détection d’un C2 (firewall)

Exemple :

```text
HOST-A
→ 185.x.x.x:443
→ action=accept
→ every 5 minutes
```


Pattern :

```text
Same Source
+
Same Destination
+
Regular Frequency
+
Small Similar Transfers
→ Possible C2 Beaconing
```


Firewall logs + NetFlow peuvent être particulièrement utiles pour identifier cette périodicité.

## Exfiltration (firewall)

Exemple :

```text
Internal Host
→ Rare External IP
→ action=accept
→ sentbyte=4 GB
```


```text
Large Outbound Transfer
+
Rare Destination
+
Unusual Time
→ Possible Exfiltration
```


Comparer :

```text
sentbyte
vs
rcvdbyte
```


Une asymétrie importante peut fournir du contexte.

## IPS + Firewall Correlation

Scénario intéressant :

```text
IPS
→ attacker IP blocked earlier

Later...

Traffic Log
→ same IP
→ action=accept
```


Questions :

- règle modifiée ?
- autre port utilisé ?
- autre service ?
- IPS signature non déclenchée ?
- connexion réellement autorisée ?

```text
Previous Deny
→ Later Accept
→ Investigate
```


## Policy ID

Dans l’exemple :

```text
policyid=284
```


permet d’identifier quelle règle firewall a autorisé ou bloqué le trafic.

Très utile pour répondre à :

```text
Why was this traffic allowed?
```


Workflow :

```text
Suspicious Traffic
→ Policy ID
→ Review Firewall Rule
→ Too Permissive?
→ Misconfiguration?
```


## Detection Patterns SOC (firewall)

### Scan

```text
Same Source
+
Many Ports / Hosts
+
Short Time Window
→ Possible Port Scan
```


### IOC Communication

```text
Internal Host
+
Known Malicious Destination
+
action=accept
→ Investigate Endpoint
```


### Lateral Movement

```text
Compromised Host
+
New East-West Connection
+
SMB / RDP / WinRM
→ Possible Lateral Movement
```


### Exfiltration

```text
Large sentbyte
+
External Destination
+
Unusual Host
→ Possible Data Exfiltration
```


### C2

```text
Repeated Small Connections
+
Rare Destination
+
Regular Interval
→ Possible Beaconing
```


## Firewall Logs vs NetFlow

Les deux se complètent :

```text
Firewall Logs
→ Security Decision
→ Allow / Deny
→ Rule / Policy Context

NetFlow
→ Communication Metadata
→ Volume / Frequency / Relationships
```


```text
Firewall
+
NetFlow
→ Better Network Investigation
```


## Vue d’ensemble (firewall)

```text
Firewall Traffic Log
│
├─ Timestamp
├─ Source IP / Port
├─ Destination IP / Port
├─ Protocol
├─ Interfaces
├─ Application / Service
├─ Action
├─ Policy
├─ NAT
├─ Duration
├─ Bytes
└─ Packets
```


Workflow SOC :

```text
Firewall Alert / IOC
        ↓
Identify Source + Destination
        ↓
Check Port / Protocol / Application
        ↓
Check Action
        ↓
Check Policy / NAT
        ↓
Analyze Volume + Frequency
        ↓
Correlate with EDR / IPS / DNS / NetFlow
        ↓
Determine Scope & Intent
```


Le point essentiel est que les firewall logs permettent non seulement de savoir **qui a tenté de communiquer avec qui**, mais également **si le trafic a été autorisé, par quelle policy, via quel service et avec quel volume**. Ils deviennent particulièrement puissants lorsqu’ils sont corrélés avec `NetFlow`, `IPS`, `EDR`, `DNS` et les IOC connus.
