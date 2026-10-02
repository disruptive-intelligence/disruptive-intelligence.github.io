---
title: Authentification et Autorisation sous Windows
source: Cyber/05 Hardening/Systèmes/Sécurité système Windows.md
note: Sécurité système Windows
up:
- - Sécurité système Windows
  - index.md
---

```
Authentication → Qui es-tu ?
Authorization  → Qu'as-tu le droit de faire ?
```


- **Authentication** vérifie l’identité d’un utilisateur, d’un ordinateur ou d’un service.
- **Authorization** détermine ensuite les ressources et actions auxquelles cette identité a droit.
## Authentification

- L'authentification est le processus de vérification de l'identité d'un utilisateur.
- Windows peut utiliser plusieurs méthodes :
	- username/password ;
	- smart card ;
	- biométrie ;
	- certificats ;
	- MFA.
- Dans un environnement Active Directory, les protocoles les plus importants sont surtout **Kerberos** et **NTLM**.
### Kerberos

- Protocole d’authentification principal dans un **domaine Active Directory**.
- Repose sur un **KDC — Key Distribution Center**, généralement fourni par les Domain Controllers.
- Lorsqu'un utilisateur se connecte au système pour la première fois, il reçoit un « ticket » du KDC. Ce ticket est utilisé pour vérifier l'identité de l'utilisateur pendant une certaine période. Le protocole Kerberos offre une authentification rapide et sécurisée et prend en charge l'authentification entre les services sur le réseau.
- Utilise des **tickets** plutôt que de retransmettre constamment le password.

```
User
 ↓
KDC
 ↓
Ticket
 ↓
Service
```

Principe simplifié :

```
Login
→ obtention d'un TGT
→ demande d'un Service Ticket
→ accès au service
```

#### Clock Synchronization

- Kerberos dépend fortement du temps.

```
Client Time ≈ Domain Controller Time
```

Une différence d’horloge trop importante peut provoquer des erreurs d’authentification.
→ utiliser une synchronisation temporelle fiable.
#### SPN — Service Principal Name

- Identifie une instance de service dans Active Directory.
- Doit être :
    - correctement configuré ;
    - associé au bon compte ;
    - unique.

Exemple :

```
HTTP/webserver.domain.local
MSSQLSvc/sql01.domain.local
```

-> Une mauvaise configuration des SPN peut empêcher Kerberos et provoquer un fallback vers NTLM.
#### Chiffrement

- Privilégier les algorithmes modernes comme **AES**.
- Éviter les mécanismes historiques comme DES lorsqu’ils sont encore présents dans un environnement legacy.
### NTLM — NT LAN Manager

- Protocole plus ancien que Kerberos.
- NTLM hache les informations d'identification de l'utilisateur et utilise ces hachages (hashes) pour l'authentification.
- Souvent utilisé lorsque Kerberos ne peut pas fonctionner :
    - système hors domaine ;
    - accès par IP dans certains contextes ;
    - legacy systems ;
    - mauvaise configuration Kerberos.

```
Kerberos indisponible
→ NTLM fallback possible
```

NTLM utilise un mécanisme **challenge-response** dérivé du secret utilisateur.

> Il ne transmet normalement pas directement le password sur le réseau.
#### NTLMv1 vs NTLMv2

```
NTLMv1 → ancien / faible
NTLMv2 → plus robuste
```

Bonnes pratiques :

- désactiver NTLMv1 ;
- utiliser NTLMv2 si NTLM reste nécessaire ;
- réduire progressivement l’utilisation de NTLM ;
- préférer Kerberos dans AD.
### Digest Authentication

- Mécanisme historique utilisé notamment avec certains services HTTP.
- Fonctionne via un mécanisme challenge-response basé sur un digest plutôt qu’en envoyant directement le password.

> Historiquement, Digest est fortement associé à **MD5**, aujourd’hui considéré comme faible. C’est donc surtout un mécanisme legacy.
### Basic Authentication

- Envoie les credentials sous une forme **Base64**, qui n’est pas un chiffrement.

```
username:password
→ Base64
→ facilement décodable
```

Donc :

```
Basic sans TLS
→ credentials exposés

Basic + HTTPS/TLS
→ transport chiffré
```

> Dire que Basic envoie « en clair » est conceptuellement correct du point de vue sécurité : Base64 n’offre aucune confidentialité.
### Carte à puce - Smart Card Authentication

- Utilise une **carte à puce** contenant des éléments cryptographiques, associée généralement à un PIN.

```
Something you have → Smart Card
+
Something you know → PIN
```

Bonnes pratiques :

- protéger le PIN ;
- protéger physiquement la carte ;
- contrôler les lecteurs ;
- révoquer rapidement une carte perdue.
### Authentification basée sur les certificats

- Cette méthode utilise des certificats numériques (digital certificates) et est souvent utilisée en conjonction avec une Infrastructure à Clé Publique.
- L'identité d'un utilisateur est vérifiée via un certificat numérique signé par une autorité de certification (certificate authority) et détenu par l'utilisateur.
### Comparaison rapide

|Méthode|Usage|
|---|---|
|**Kerberos**|Authentification principale en Active Directory|
|**NTLM**|Legacy / fallback|
|**Digest**|Mécanisme ancien, notamment HTTP|
|**Basic**|Simple, doit être protégé par TLS|
|**Smart Card**|Authentification forte avec carte + PIN|
|**Certificate**|Authentification basée PKI|
## Autorisation — Authorization

- Une fois l’utilisateur authentifié, Windows doit déterminer ce qu’il peut faire.
- Lors de la connexion, Windows construit un **Access Token / Security Token** contenant notamment :
	- SID de l’utilisateur ;
	- SIDs des groupes ;
	- privilèges ;
	- informations de sécurité.

```
Authenticated User
→ Access Token
→ Groups + Privileges
→ Authorization Decisions
```

- Une partie importante de l'autorisation Windows est l'utilisation des Listes de Contrôle d'Accès (Access Control Lists - ACL) et des Entrées de Contrôle d'Accès (Access Control Entries - ACE).
	- ACL déterminent le type d'accès qu'un utilisateur ou un groupe a sur un objet (par exemple, un fichier, un dossier ou une clé de registre) ;
	- ACE sont des entrées individuelles dans les ACL et déterminent comment un utilisateur ou un groupe particulier peut accéder à un objet.
### SID — Security Identifier

- Windows identifie les utilisateurs et groupes principalement avec leur **SID**, pas simplement leur nom.
- Exemple conceptuel :

```
S-1-5-21-...
```


```
Username → lisible par l'humain
SID      → identité réellement utilisée par Windows
```

### ACL — Access Control List

- Une **ACL** définit les règles de contrôle d’accès associées à un objet.
- Une ACL répertorie les utilisateurs et les groupes qui ont la permission d'accéder à l'objet.
- Chaque entrée est appelée une ACE et détermine comment un utilisateur ou un groupe particulier peut accéder à l'objet.
- Objets possibles :
	- fichier ;
	- dossier ;
	- registry key ;
	- printer ;
	- service ;
	- autr

```
Object
→ ACL
→ ACE
→ Allow / Deny / Audit
```

### ACE — Access Control Entry

- Chaque entrée d’une ACL est une **ACE**.
- Une ACE associe généralement :

```
User / Group
+
Permission
+
Allow / Deny
```

Exemple :

```
Finance Group
→ Read + Write
→ ALLOW
```

### DACL et SACL

- Complément important :
- Une Security Descriptor Windows peut notamment contenir :
#### DACL — Discretionary ACL

- Définit **qui peut faire quoi** sur l’objet.

```
Alice → Read  → Allow
Bob   → Write → Deny
```

#### SACL — System ACL

- Définit **quels accès doivent être audités**.

```
Failed Write
→ generate Security Event
```


```
DACL → authorization
SACL → auditing
```

### Permissions NTFS
Permissions classiques :

|Permission|Fonction|
|---|---|
|**Full Control**|Tous les droits + modification des permissions|
|**Modify**|Lire, écrire, modifier, supprimer|
|**Read & Execute**|Lire et exécuter|
|**List Folder Contents**|Voir le contenu d’un dossier|
|**Read**|Lire|
|**Write**|Créer/modifier certaines données|
### Stratégie de groupe (GPO)
Les **GPO** peuvent compléter le contrôle d’accès en imposant des règles aux utilisateurs et ordinateurs :

- User Rights Assignment ;
- restrictions système ;
- sécurité ;
- application control ;
- firewall ;
- restrictions de connexion.

```
GPO
→ configure les règles

ACL
→ contrôle l'accès à un objet précis
```


> Une GPO et une ACL ne remplissent donc pas exactement le même rôle.
