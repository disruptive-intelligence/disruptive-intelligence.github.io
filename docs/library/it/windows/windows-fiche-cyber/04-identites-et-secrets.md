---
title: Identités et secrets
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 11. SID, Access Token, ACL, ACE, DACL, SACL

### À retenir
Le cœur du modèle de sécurité Windows : **qui** agit (SID), avec **quels droits** (token), sur **quel objet** (protégé par une ACL).

### Comment ça fonctionne

**SID (Security Identifier)** : identifiant unique d'un principal de sécurité (utilisateur, groupe, machine). Généré automatiquement, il rend deux comptes au même nom distinguables.

```
S-1-5-21-674899381-4069889467-2080702030-1002
│ │ │  └──── SID domaine/machine ────┘  └─ RID
│ │ └── Identifier-authority (5 = NT Authority)
│ └──── Revision (toujours 1)
└────── "S" = SID
```

**RID (Relative ID)** : la dernière partie du SID, qui distingue un compte des autres. **RID 500 = le vrai Administrateur**, **RID 1000+ = utilisateurs normaux**.

**Access Token** : à la connexion, après vérification par LSASS, Windows crée un jeton attaché à la session. Il contient le **SID de l'utilisateur**, les **SIDs de ses groupes**, ses **privilèges** et son **niveau d'intégrité**. Ce token est hérité par les processus lancés : `explorer.exe` en transmet une copie à chaque programme ouvert.

**ACL / ACE / DACL / SACL** : chaque objet sécurisable (fichier, clé de registre, service...) possède un **Security Descriptor** contenant :

- une **DACL** (Discretionary ACL) : la liste des **ACE** (Access Control Entries), chacune disant « tel SID → Allow/Deny telles opérations ». C'est elle qui décide de l'accès.
- une **SACL** (System ACL) : définit ce qui est **audité/journalisé** (succès/échecs d'accès).

**Décision d'accès** : à chaque tentative, Windows compare le **token** du processus à la **DACL** de l'objet, et applique les ACE pour décider **Allow ou Deny**.

### Pourquoi c'est important en cyber
Comprendre cette chaîne, c'est comprendre comment Windows autorise ou refuse une action — donc où chercher des **failles de permissions** et quels comptes privilégiés repérer (via leurs SID/RID). C'est le socle de l'élévation de privilèges et de l'analyse d'accès.

### Exemple concret
Bob (token avec SID `...-1002`, groupe Users) tente d'écrire dans un fichier dont la DACL n'autorise l'écriture qu'aux Administrators. Windows compare, ne trouve pas de SID correspondant côté Allow → **accès refusé**.

### Commandes utiles

```cmd
whoami /user                # SID du compte courant
whoami /groups              # SIDs des groupes
whoami /priv                # Privilèges actifs
```


### Point clé à mémoriser
Token (qui je suis + ce que je peux) comparé à DACL (qui a droit à quoi) = décision Allow/Deny. RID 500 = vrai Administrateur.

---

## 12. SAM, LSA et LSASS

### À retenir

- **SAM** : base locale des comptes et de leurs secrets (hashes).
- **LSA** : l'autorité de sécurité qui valide identités et jetons.
- **LSASS** : le processus qui applique tout ça en mémoire.

### Comment ça fonctionne
La **SAM** (`C:\Windows\System32\config\SAM`, clé dans registre `HKLM\SAM`) stocke les comptes **locaux** et leurs hashes. Elle est **chiffrée par une clé rangée dans le fichier SYSTEM** : la SAM seule est inutilisable, il faut **SAM + SYSTEM** pour en extraire les secrets. En environnement **domaine**, les comptes sont dans Active Directory (`NTDS.dit`) ; la SAM locale ne gère alors que les comptes locaux.

La **LSA** fournit à l'authentification les identités (SID) et secrets, et valide les access tokens. **LSASS** (`lsass.exe`) est le processus qui exécute cette politique : il vérifie chaque connexion, crée les tokens et gère les changements de mot de passe.

Pour permettre le **SSO** (ne pas retaper son mot de passe), Windows garde des identifiants en mémoire dans LSASS : hashes **NTLM**, tickets **Kerberos**, et parfois mots de passe en clair sur d'anciens systèmes (**WDigest**).

### Pourquoi c'est important en cyber
LSASS est une **cible de haute valeur** : sa mémoire contient des identifiants réutilisables pour se déplacer latéralement sur le réseau. En forensic, l'accès à la SAM ou à la mémoire LSASS est un indicateur fort de compromission ; en durcissement, désactiver WDigest et protéger LSASS (Credential Guard) sont des mesures clés.

### Exemple concret
Sauvegarder les ruches pour analyse hors ligne nécessite les deux fichiers liés :

```cmd
reg save HKLM\sam sam.save
reg save HKLM\system system.save
```

Sans `system.save`, la SAM reste illisible.

### Point clé à mémoriser
Pour exploiter la SAM, il faut SAM **et** SYSTEM. LSASS garde des identifiants sensibles en mémoire.

> La SAM ne peut pas être copiée tant que Windows tourne → on passe par les **Volume Shadow Copies**.

---
