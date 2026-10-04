---
title: 'Approfondir : modèle de sécurité et secrets'
source: IT/02 Windows/Comprendre Windows/Windows — fiche cyber.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 7. Modèle de sécurité Windows

### 7.1 Security principal

Un **security principal** est une entité à laquelle Windows peut attribuer des droits.

Exemples :

- utilisateur ;
- groupe ;
- ordinateur ;
- service ;
- domaine.

Chaque security principal possède un identifiant unique : le **SID**.

---

### 7.2 SID — Security Identifier

Un **SID** identifie de façon unique un utilisateur, groupe, ordinateur, domaine ou service.

Windows ne se base pas sur le nom affiché mais sur le SID.

Voir son SID :

```cmd
whoami /user
```


Voir ses groupes :

```cmd
whoami /groups
```


Lister les comptes locaux et leurs SID :

```cmd
wmic useraccount get name,sid
```


---

### 7.3 Structure d’un SID

Exemple :

```text
S-1-5-21-674899381-4069889467-2080702030-1002
```


Décomposition :

```text
S-1-5-21-674899381-4069889467-2080702030-1002
^ ^ ^ ^-----------------------------------^ ^^^^
| | |             SID machine/domaine       RID
| | +-- Authority : 5 = NT Authority
| +---- Revision : toujours 1
+------ S = SID
```


|Partie|Signification|
|---|---|
|`S`|Indique qu’il s’agit d’un SID.|
|`1`|Niveau de révision. Toujours 1.|
|`5`|Identifier Authority. `5` = NT Authority.|
|`21-...`|SID de la machine ou du domaine.|
|`1002`|RID : identifiant relatif du compte.|

RID connus :

|RID|Signification|
|---|---|
|`500`|Administrateur local intégré.|
|`501`|Invité.|
|`512`|Domain Admins, en domaine AD.|
|`513`|Domain Users, en domaine AD.|
|`1000+`|Utilisateurs créés ensuite.|

---

### 7.4 Access token

Lorsqu’un utilisateur s’authentifie, Windows crée un **access token**.

Ce token contient notamment :

- SID de l’utilisateur ;
- SID des groupes ;
- privilèges ;
- niveau d’intégrité ;
- type de logon ;
- éventuels restricted SIDs.

Ensuite, les processus lancés par l’utilisateur héritent généralement de ce token.

Exemple :

```text
Utilisateur se connecte
   ↓
LSASS valide l’identité
   ↓
Windows crée un token
   ↓
explorer.exe reçoit le token
   ↓
Les programmes lancés depuis explorer.exe héritent du token
```


Quand un processus veut accéder à un fichier, une clé registre ou un service, Windows compare :

```text
Token du processus ↔ DACL de l’objet demandé
```


Puis Windows décide :

```text
Accès autorisé ou refusé
```


---

### 7.5 Privilèges Windows

Voir ses privilèges :

```cmd
whoami /priv
```


Exemples :

|Privilège|Intérêt|
|---|---|
|`SeDebugPrivilege`|Permet de déboguer ou ouvrir d’autres processus. Sensible pour LSASS.|
|`SeImpersonatePrivilege`|Permet l’impersonation. Souvent important en privesc Windows.|
|`SeBackupPrivilege`|Permet de lire certains fichiers malgré les ACL.|
|`SeRestorePrivilege`|Permet d’écrire/restaurer certains fichiers.|
|`SeShutdownPrivilege`|Permet d’arrêter le système.|
|`SeTakeOwnershipPrivilege`|Permet de prendre possession d’un objet.|

---

### 7.6 Integrity Levels

Windows utilise des niveaux d’intégrité pour limiter ce qu’un processus peut faire.

|Niveau|Exemple|
|---|---|
|`Low`|Navigateur en mode sandbox, processus très limité.|
|`Medium`|Processus utilisateur standard.|
|`High`|Processus administrateur élevé.|
|`System`|Processus système.|

Voir son niveau d’intégrité :

```cmd
whoami /groups
```


Chercher la ligne :

```text
Mandatory Label\Medium Mandatory Level
Mandatory Label\High Mandatory Level
```


---

## 8. ACL, ACE, DACL, SACL

### 8.1 Objet sécurisable

Dans Windows, beaucoup d’objets peuvent avoir des permissions :

- fichier ;
- dossier ;
- clé de registre ;
- service ;
- tâche planifiée ;
- processus ;
- thread ;
- imprimante ;
- partage réseau.

Ces objets possèdent un **Security Descriptor**.

---

### 8.2 Security Descriptor

Un **Security Descriptor** décrit la sécurité d’un objet.

Il contient notamment :

- **Owner** : propriétaire ;
- **Primary Group** : groupe principal ;
- **DACL** : qui a le droit de faire quoi ;
- **SACL** : quoi auditer/journaliser.

---

### 8.3 ACL / ACE / DACL / SACL

|Terme|Définition|Rôle|
|---|---|---|
|**ACE**|Access Control Entry|Une règle : tel SID a tel droit en Allow ou Deny.|
|**ACL**|Access Control List|Liste d’ACE.|
|**DACL**|Discretionary ACL|Liste des autorisations/refus d’accès.|
|**SACL**|System ACL|Liste des accès à auditer/journaliser.|

Exemple mental :

```text
Security Descriptor
├── Owner
├── Group
├── DACL
│   ├── ACE : Alice peut lire
│   ├── ACE : Bob peut écrire
│   └── ACE : Users ne peuvent pas modifier
└── SACL
    └── Auditer les échecs d’écriture
```


---

### 8.4 Access check

Quand un processus veut accéder à un objet :

```text
1. Le processus présente son token.
2. Windows lit la DACL de l’objet.
3. Windows compare les SID du token avec les ACE de la DACL.
4. Windows autorise ou refuse l’accès.
```


Schéma :

```text
Processus
  ↓ token : SID user + groupes + privilèges
Objet demandé
  ↓ DACL : ACE Allow/Deny
Décision
  ↓
Access granted / Access denied
```


---

## 9. SAM, LSA et secrets locaux

### 9.1 SAM — Security Accounts Manager

La **SAM** est la base locale des comptes Windows.

Elle contient notamment :

- comptes utilisateurs locaux ;
- groupes locaux ;
- SID ;
- informations nécessaires à l’authentification locale ;
- secrets comme les hashes de mots de passe.

Sur disque, la ruche SAM est ici :

```text
C:\Windows\System32\config\SAM
```


Dans le registre :

```text
HKLM\SAM
```


---

### 9.2 SAM et SYSTEM

Les secrets de la SAM sont protégés.

Pour exploiter ou analyser hors ligne la SAM dans un lab autorisé, on a souvent besoin de :

```text
SAM + SYSTEM
```


Pourquoi ?

- `SAM` contient les comptes et hashes.
- `SYSTEM` contient notamment des éléments nécessaires au déchiffrement local.

Ruches intéressantes :

|Ruche|Contenu|
|---|---|
|`SAM`|Comptes locaux et hashes.|
|`SYSTEM`|Configuration système, clés nécessaires à certains secrets.|
|`SECURITY`|Secrets LSA, informations sensibles locales.|

---

### 9.3 Extraire les ruches en lab

Commande possible en contexte administrateur/lab :

```cmd
reg save HKLM\SAM sam.save
reg save HKLM\SYSTEM system.save
reg save HKLM\SECURITY security.save
```


Note : il n’est généralement pas possible de copier directement `C:\Windows\System32\config\SAM` pendant que Windows tourne, car le fichier est verrouillé.

---

### 9.4 SAM en domaine Active Directory

Sur une machine jointe à un domaine :

- les comptes locaux restent dans la SAM locale ;
- les comptes de domaine sont stockés côté Active Directory ;
- la base AD principale est `NTDS.dit` sur les contrôleurs de domaine.

À retenir :

```text
Compte local → SAM locale
Compte domaine → Active Directory / NTDS.dit
```


---
