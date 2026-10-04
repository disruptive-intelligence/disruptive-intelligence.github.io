---
title: Chapitre 7 — Où sont stockés les secrets et comment ils sont volés
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie II — Authentification
  - index.md
---

Comprendre **où vit chaque secret** est la clé pour savoir ce qu'une compromission expose et comment s'en protéger. Un principe d'abord : **un compte local ≠ un compte de domaine**. Les comptes locaux d'une machine sont dans sa **SAM** locale ; les comptes du domaine sont dans **NTDS.dit**, sur les contrôleurs de domaine.

```text
Compte local    → SAM locale (sur chaque machine)
Compte domaine  → NTDS.dit (sur les DC)
```


| Emplacement | Contenu | Ce qu'il faut pour l'exploiter | Protection |
|---|---|---|---|
| **SAM** (`HKLM\SAM`, `C:\Windows\System32\config\SAM`) | Comptes **locaux** et leurs hashes | SAM **+** SYSTEM (la SAM est chiffrée par une clé rangée dans SYSTEM) | LAPS (mot de passe admin local unique par poste), réduction des admins locaux |
| **SYSTEM** (`config\SYSTEM`) | Clé de déchiffrement des secrets locaux, config, services | — | — |
| **SECURITY** (`config\SECURITY`) | **LSA Secrets** : mots de passe de comptes de service, clé machine, secrets DPAPI | SECURITY + SYSTEM, privilèges SYSTEM | Rotation des comptes de service, moindre privilège |
| **NTDS.dit** (sur les DC) | Hashes NTLM de **tous** les comptes du domaine + historique | Accès DC (sauvegarde, snapshot) ou droits de réplication (DCSync) | Tiering, protection des sauvegardes, surveillance de la réplication |
| **Mémoire de `lsass.exe`** | Tickets Kerberos, hashes NTLM, parfois mot de passe en clair (WDigest) des **sessions actives** | Droits d'administrateur/SYSTEM sur la machine (`SeDebugPrivilege`) | Credential Guard, LSA Protection (RunAsPPL), EDR, désactivation de WDigest |

**Pourquoi SAM seule ne suffit pas.** La ruche SAM est chiffrée par une clé (la *SysKey*/bootkey) rangée dans la ruche SYSTEM. On ne peut donc rien en tirer sans les **deux** fichiers. De plus, ces fichiers sont verrouillés quand Windows tourne : on passe par un cliché instantané (Volume Shadow Copy) ou un export registre pour en obtenir une copie au repos.

**Pourquoi LSASS est une cible de choix.** Pour assurer le SSO (ne pas retaper son mot de passe à chaque service), Windows garde en mémoire, dans LSASS, des éléments d'authentification des sessions ouvertes : tickets Kerberos, hashes NTLM, et sur les anciens systèmes mal configurés, des mots de passe en clair (WDigest). C'est pourquoi un accès en lecture à la mémoire de LSASS est un signal d'alerte fort, et que Credential Guard (isolation par virtualisation) et RunAsPPL (LSASS en processus protégé) existent.

> **Dump SAM vs dump LSASS — à bien distinguer.** La SAM concerne les comptes **locaux stockés sur disque** (hashes au repos). LSASS est un **processus actif** qui contient les secrets des **sessions en cours** (tickets, clés). Sources, contenus et protections sont donc différents.

Les **autres sources** à connaître : les **Group Policy Preferences** historiques (attribut `cpassword` chiffré avec une clé publiée par Microsoft → corrigé par MS14-025 mais souvent encore présent dans SYSVOL), les **identifiants de domaine mis en cache** (permettent d'ouvrir une session hors connexion même sans DC joignable), et le **`pagefile.sys`** / crash dumps (fragments de mémoire). Outils d'extraction cités dans les cours : `ntdsutil`, `reg save`, `secretsdump`, `Mimikatz`, `Pypykatz`.

---
