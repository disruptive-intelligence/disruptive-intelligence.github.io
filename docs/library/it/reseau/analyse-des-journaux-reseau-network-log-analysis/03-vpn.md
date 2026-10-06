---
title: VPN
source: IT/04 Réseau/Journaux & investigation/Analyse des journaux réseau (Network Log Analysis).md
note: Analyse des journaux réseau (Network Log Analysis)
up:
- - Analyse des journaux réseau (Network Log Analysis)
  - index.md
---

Source : [Hack The Box Academy - Network Log Analysis](https://academy.hackthebox.com/course/preview/network-log-analysis)

## Analyse des logs VPN

- Un **VPN — Virtual Private Network** permet à un utilisateur distant d’accéder à un réseau auquel il n’est pas physiquement connecté.
- En entreprise, il est principalement utilisé pour fournir un **remote access** sécurisé aux ressources internes.

```text
Remote User
→ Internet
→ VPN Gateway
→ Internal Network
```


Comme le service VPN est généralement exposé sur Internet, il constitue une **surface d’attaque** importante.

Pour un SOC, les logs VPN permettent surtout de répondre à :

```text
Who connected?
→ From which IP?
→ Using which account?
→ Was authentication successful?
→ Which internal VPN IP was assigned?
→ What happened afterward?
```


## Déploiement d’un VPN

Deux architectures courantes :

```text
VPN
│
├─ Integrated into Firewall
│
└─ Dedicated VPN Appliance
```


Les logs peuvent donc provenir :

- du firewall ;
- d’un concentrateur VPN dédié ;
- d’un service VPN cloud selon l’architecture.

## Exemple de VPN Log

```text
date=2022-05-21
time=14:06:38
devname="FG500"
type="event"
subtype="vpn"
logdesc="SSL VPN tunnel up"
action="tunnel-up"
tunneltype="ssl-web"
remip=13.29.5.4
user="letsdefend-user"
reason="login successfully"
msg="SSL tunnel established"
```


Interprétation :

```text
Remote IP:
13.29.5.4

User:
letsdefend-user

VPN Type:
SSL VPN

Action:
Tunnel established

Result:
Login successful
```


## Champs principaux (VPN)

### Temps

```text
date
→ date de l'événement

time
→ heure

eventtime
→ timestamp précis

tz
→ timezone
```


La timezone est importante pour corréler les événements VPN avec :

- authentication logs ;
- firewall ;
- EDR ;
- proxy ;
- SIEM.

### Équipement

```text
devname
→ hostname du device

devid
→ identifiant de l'équipement
```


### Type de log

```text
type
→ catégorie principale

subtype
→ sous-catégorie
```


Exemple :

```text
type="event"
subtype="vpn"
```


→ événement VPN généré par le firewall.

### Description / Action

```text
logdesc
→ description de l'événement

action
→ action effectuée
```


Exemple :

```text
logdesc="SSL VPN tunnel up"

action="tunnel-up"
```


→ le tunnel VPN a été établi.

### Tunnel Type

```text
tunneltype
```


peut identifier le type de VPN.

Exemples :

```text
SSL VPN
IPsec VPN
```


Dans le log :

```text
tunneltype="ssl-web"
```


→ connexion **SSL-VPN**.

### Remote IP — `remip`

```text
remip
→ IP publique ayant initié la connexion VPN
```


Exemple :

```text
remip=13.29.5.4
```


C’est une information essentielle pour déterminer :

- origine réseau de la connexion ;
- pays approximatif ;
- réputation de l’IP ;
- autres comptes utilisant cette IP ;
- historique de connexion.

### User

```text
user
→ compte authentifié
```


Exemple :

```text
user="letsdefend-user"
```


L’un des premiers axes d’analyse consiste donc à corréler :

```text
User
+
Remote IP
+
Timestamp
+
Authentication Result
```


### Résultat de l’authentification

Champs possibles :

```text
reason
msg
action
```


Dans l’exemple :

```text
reason="login successfully"

msg="SSL tunnel established"
```


→ authentification réussie et tunnel créé.

Les trois éléments les plus importants à vérifier sont donc :

```text
Source IP
Username
Success / Failure
```


## Tunnel IP

Après une connexion VPN réussie, le système peut attribuer une adresse IP interne au client :

```text
Remote IP
13.29.5.4
        ↓
VPN Authentication
        ↓
Assigned VPN IP
"tunnelip"
        ↓
Internal Network Traffic
```


Cette adresse peut apparaître :

- dans le même événement ;
- dans un événement suivant.

### `remip` vs `tunnelip`

Très important :

```text
remip
→ Public / external IP of VPN client

tunnelip
→ Internal IP assigned inside VPN
```


Exemple conceptuel :

```text
Internet:
13.29.5.4
    ↓
VPN Gateway
    ↓
Assigned:
10.20.30.15
```


Ensuite, les communications internes peuvent apparaître comme :

```text
srcip=10.20.30.15
```


dans les logs firewall.

### Corrélation VPN → Firewall

Workflow :

```text
VPN Log
remip=13.29.5.4
user=letsdefend-user
tunnelip=10.20.30.15
        ↓
Firewall Traffic Logs
srcip=10.20.30.15
        ↓
Internal Activity
```


Cela permet de suivre :

```text
External User
→ VPN Session
→ Assigned IP
→ Internal Network Activity
```


### SSL-VPN et HTTPS

Dans le scénario du cours, les traffic logs associés à la connexion initiale peuvent montrer :

```text
service=HTTPS
```


car le VPN utilisé est de type :

```text
SSL-VPN
```


Donc :

```text
Remote Client
→ HTTPS / TLS
→ VPN Gateway
```


## Analyse d’une connexion VPN

Workflow de base :

```text
VPN Event
      ↓
Identify User
      ↓
Identify Remote IP
      ↓
Check Success / Failure
      ↓
Identify Tunnel IP
      ↓
Search Firewall Activity
      ↓
Analyze Internal Access
```


### Phishing + Credentials compromis

Scénario du cours :

```text
Phishing Email
→ User enters credentials
→ Credentials stolen
```


Une étape essentielle consiste ensuite à rechercher si ces credentials ont été utilisés sur les services exposés :

```text
VPN
Email
Cloud Services
Other External Portals
```


Pour le VPN :

```text
Compromised User
→ Search VPN Logs
→ Successful Connections?
→ From Which IP?
→ From Which Country?
→ Was It Really the User?
```


### Connexion VPN suspecte

Exemple :

```text
User:
jdoe

Normal:
France

Observed:
Successful VPN Login
from unusual foreign IP
```


→ activité à investiguer.

Mais :

```text
Different Country
≠ automatically compromised
```


Il faut considérer :

- voyage ;
- corporate VPN / proxy ;
- mobile carrier ;
- cloud egress ;
- changement légitime d’emplacement.

## Brute Force VPN

Pattern :

```text
Same Source IP
→ user1 FAIL
→ user2 FAIL
→ user3 FAIL
→ user4 FAIL
```


ou :

```text
Same User
→ FAIL
→ FAIL
→ FAIL
→ FAIL
```


Peut indiquer :

```text
Password Guessing
Brute Force
Password Spraying
```


### Brute Force vs Password Spraying

```text
Brute Force
→ Many passwords
→ One / few accounts
```


```text
Password Spraying
→ One / few passwords
→ Many accounts
```


Les logs VPN sont particulièrement utiles pour détecter les deux.

### Échec puis succès

Pattern important :

```text
14:00 → Login failed
14:01 → Login failed
14:02 → Login failed
14:03 → Login successful
```


Si la source IP et le compte sont identiques :

```text
Repeated Failures
+
Successful Login
→ Possible Credential Compromise
```


### Multiple Users from Same IP

Exemple :

```text
185.x.x.x
→ userA
→ userB
→ userC
→ userD
```


sur une courte période.

Peut indiquer :

- password spraying ;
- credential stuffing ;
- infrastructure d’attaquant.

### Same User from Multiple IPs

Exemple :

```text
user=jdoe

10:00 → France
10:03 → United States
```


Peut être intéressant pour détecter une anomalie géographique.

```text
Same Account
+
Distant Locations
+
Short Time Window
→ Suspicious
```


Cela peut être rapproché d’un concept de :

```text
Impossible Travel
```


> Note technique : la géolocalisation IP reste approximative ; VPN commerciaux, proxies et réseaux mobiles peuvent produire des anomalies apparentes.

## Connexions hors horaires habituels

Exemple :

```text
Normal:
08:00–18:00

Observed:
VPN Login at 03:17
```


Peut être intéressant surtout si combiné à :

```text
Unusual Time
+
Unusual IP
+
Sensitive Account
→ Higher Suspicion
```


## Connexions hors pays autorisés

Certaines organisations limitent ou surveillent les pays depuis lesquels le VPN doit être accessible.

```text
Expected:
France / Germany

Observed:
Unexpected Country
```


→ investigation.

Le pays seul reste un signal de contexte, pas une preuve.

## Successful vs Unsuccessful VPN Access

### Failed

```text
Authentication Failure
```


Peut indiquer :

- mot de passe incorrect ;
- compte invalide ;
- brute force ;
- password spraying.

### Successful

```text
Authentication Success
```


Permet d’établir qu’un compte a effectivement obtenu une session VPN.

Mais :

```text
Successful Authentication
≠ Legitimate User
```


Un attaquant utilisant des credentials valides apparaîtra également comme une authentification réussie.

### VPN + MFA

Lorsqu’un VPN utilise MFA, une investigation doit idéalement vérifier :

```text
Password Authentication
+
MFA Result
+
Remote IP
+
Device Context
```


Une connexion réussie après phishing peut indiquer :

- credentials compromis ;
- MFA approuvé frauduleusement ;
- session/token compromis selon l’architecture.

## Corrélation après une connexion suspecte

Une fois le `tunnelip` identifié :

```text
VPN
→ user=jdoe
→ tunnelip=10.0.50.25
```


rechercher :

```text
Firewall
→ 10.0.50.25 → Servers

Authentication
→ account logons

EDR
→ endpoint activity

IDS/IPS
→ suspicious internal connections
```


### Exemple de lateral movement après VPN

```text
02:03
VPN Login
→ user=jdoe
→ tunnelip=10.0.50.25

02:06
10.0.50.25
→ Server-A:445

02:08
10.0.50.25
→ Server-B:3389

02:10
10.0.50.25
→ Server-C:5985
```


Peut suggérer :

```text
Compromised VPN Account
→ Internal Reconnaissance
→ Possible Lateral Movement
```


### Ports particulièrement intéressants

Après une connexion VPN suspecte :

```text
445   → SMB
3389  → RDP
5985  → WinRM HTTP
5986  → WinRM HTTPS
22    → SSH
```


De nouvelles connexions vers plusieurs systèmes internes peuvent être prioritaires.

## VPN + IOC / Threat Intelligence

La `remip` peut être enrichie avec :

- réputation ;
- IOC feeds ;
- ASN ;
- hosting provider ;
- TOR / proxy information.

```text
Successful VPN Login
+
Known Malicious Remote IP
→ High Priority
```


Mais :

```text
Bad IP Reputation
≠ proof account is compromised
```


→ toujours corréler.

## Patterns SOC importants (VPN)

### Brute Force

```text
Same User
+
Many Failures
+
Short Time Window
→ Possible Brute Force
```


### Password Spraying

```text
Same Source IP
+
Many Accounts
+
Few Attempts per Account
→ Possible Password Spraying
```


### Failed → Successful

```text
Many Failures
+
Same Source/User
+
Success
→ Possible Account Compromise
```


### Unusual Geography

```text
Successful Login
+
Unexpected Country
→ Investigate
```


### Unusual Time

```text
Successful Login
+
Outside Normal Hours
→ Investigate
```


### Suspicious Internal Activity

```text
VPN Login
+
New Tunnel IP
+
SMB / RDP / WinRM to Many Hosts
→ Possible Compromise / Lateral Movement
```


## Vue d’ensemble (VPN)

```text
VPN Log
│
├─ Timestamp
├─ VPN Device
├─ Remote IP (`remip`)
├─ Username
├─ Authentication Result
├─ Tunnel Type
├─ Assigned IP (`tunnelip`)
├─ Action
└─ Status Message
```


Workflow SOC :

```text
VPN Event
      ↓
Identify User
      ↓
Check Remote IP
      ↓
Success or Failure?
      ↓
Check Location / Reputation / Time
      ↓
Identify Tunnel IP
      ↓
Search Internal Traffic
      ↓
Correlate Firewall / IDS / EDR / Auth
      ↓
Legitimate Remote Access or Compromise?
```


Le point essentiel est de relier **l’identité externe de la connexion** (`user + remip`) à **l’identité réseau utilisée à l’intérieur du VPN** (`tunnelip`). C’est cette corrélation qui permet de suivre une session distante depuis son authentification jusqu’aux accès internes effectués après l’établissement du tunnel.
