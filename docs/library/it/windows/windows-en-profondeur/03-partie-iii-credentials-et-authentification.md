---
title: Partie III — Credentials et authentification
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

*Où sont les secrets, comment ils sont volés, et comment les protéger.*

---


## Chapitre 11 — Stockage des credentials : SAM, SYSTEM, LSASS, DPAPI

### 11.1 Où vit chaque secret

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

### 11.2 Les autres sources de secrets

Au-delà de SAM, NTDS.dit et LSASS (tableau ci-dessus), quatre sources reviennent dans toutes les investigations :

| Source | Où | Ce qu'elle contient | Point d'attention |
|---|---|---|---|
| **LSA Secrets** | `HKLM\SECURITY\Policy\Secrets` | Mots de passe des comptes de service, mot de passe du compte machine, clés de chiffrement | Lisibles par SYSTEM : un service qui tourne sous un compte de domaine y laisse son mot de passe |
| **DPAPI** (*Data Protection API*) | Master keys dans `%APPDATA%\Microsoft\Protect\` | Secrets chiffrés pour l'utilisateur : mots de passe des navigateurs, Wi-Fi, Credential Manager | La master key dérive du mot de passe de l'utilisateur ; la clé de sauvegarde du domaine, sur les DC, ouvre toutes les master keys du domaine |
| **DCC2** (*Domain Cached Credentials*) | `HKLM\SECURITY\Cache` | Une empreinte des derniers comptes de domaine connectés (10 par défaut), pour ouvrir une session sans DC | Plus lente à casser qu'un hash NTLM mais pas impossible ; réduire le nombre en cache sur les serveurs |
| **GPP** (*Group Policy Preferences*) | `SYSVOL` | Anciens mots de passe (`cpassword`) chiffrés avec une clé publiée par Microsoft | Corrigé par MS14-025, mais les anciens fichiers restent souvent dans SYSVOL : les chercher et les supprimer |

---


## Chapitre 12 — Extraction de credentials

techniques SAM/SYSTEM/LSASS et détection

### 12.1 Les sources visées et leurs traces

L'extraction **SAM + SYSTEM** : reg save (commande native — admin local, Event 4688 command line), Volume Shadow Copy (plus discrète), backup wbadmin (offline), accès physique/Live USB (hors OS), Mimikatz lsadump::sam (détecté par EDR/AV). L'extraction **NTDS.dit** : ntdsutil, VSS, DCSync (renvoi cours AD). Le **dump mémoire LSASS** — 7 techniques avec traces et détection : Task Manager (Sysmon 10, fichier .dmp), comsvcs.dll (LoLBin — rundll32 comsvcs.dll,MiniDump, Sysmon 10 + 4688), procdump (Sysmon 10), Mimikatz sekurlsa::logonpasswords (signature AV, behavior EDR), nanodump/dumpert (contournement EDR — plus difficile à détecter), duplication de handle (subtil), et SSP injection (DLL chargée dans lsass — Sysmon 7). Ce qu'on trouve dans un dump LSASS : hashes NTLM (toujours sauf Credential Guard), tickets Kerberos (si session domaine), MdP en clair (si WDigest activé — UseLogonCredential=1), clés DPAPI master keys. Les LSA Secrets (secretsdump, Mimikatz lsadump::secrets — mots de passe de services en clair). Le DPAPI (master key déchiffrée avec le hash NTLM → accès Chrome/WiFi/Vault). Les DCC2 (secretsdump, Mimikatz lsadump::cache).

### 12.2 La détection

| Source | Ce qu'elle révèle |
|---|---|
| Sysmon 10 sur `lsass.exe` | Un processus inhabituel ouvre la mémoire de LSASS |
| 4688 / Sysmon 1 | Une ligne de commande `reg save` visant SAM, SYSTEM ou SECURITY |
| 7036 + 4688 | Un cliché instantané (VSS) créé hors des sauvegardes prévues |
| Sysmon 7 | Une DLL inattendue chargée dans LSASS |
| Sysmon 13 | Une modification de la liste des SSP dans le registre |
| 4662 | Une réplication d'annuaire demandée par une machine qui n'est pas un DC (DCSync, cours AD) |

Les protections qui ferment ces sources sont au chapitre suivant.

---


## Chapitre 13 — Protections des identifiants et hardening

*Chaque mesure protège une source de secrets précise (Ch.11) : aucune ne les couvre toutes, d'où la nécessité de les combiner.*

### 13.1 Les protections et ce qu'elles couvrent

| Mesure | Principe | Protège | Ne protège pas |
|---|---|---|---|
| **Credential Guard** | Les secrets d'authentification de LSASS sont déplacés dans un environnement isolé par l'hyperviseur (VBS) | Empreintes NTLM et tickets Kerberos de domaine en mémoire | SAM, secrets LSA, identifiants mis en cache |
| **LSA Protection** (*RunAsPPL*) | LSASS tourne en processus protégé : un processus non protégé, même administrateur, ne peut plus lire sa mémoire | Mémoire de LSASS | Contournable depuis le noyau |
| **WDigest désactivé** | `UseLogonCredential = 0` (défaut depuis 8.1 / 2012 R2) | Plus de mot de passe réversible en mémoire | — |
| **LAPS** | Mot de passe administrateur local unique et renouvelé par machine | Réutilisation du compte local sur tout le parc | Comptes de domaine |
| **Remote Credential Guard** / *Restricted Admin* | Les identifiants ne sont pas déposés sur le serveur RDP de destination | Exposition sur le serveur administré | Le poste d'origine |
| **Protected Users** (groupe AD) | Pas de NTLM, de délégation, de cache, de DES/RC4 pour ses membres | Comptes privilégiés | Comptes de service |
| **Cache réduit** | GPO *Number of previous logons to cache* = 0 à 2 sur les serveurs | Identifiants de domaine mis en cache | Postes nomades (à garder raisonnable) |
| **BitLocker** | Chiffrement du disque | SAM, SYSTEM, NTDS.dit hors ligne (vol, démarrage sur un autre système) | Machine allumée et déverrouillée |

### 13.2 VBS, VSM et Credential Guard

```text
Hyperviseur
├── VTL0 : Windows « normal » (noyau, LSASS, applications, et un éventuel attaquant administrateur)
└── VTL1 : mode sécurisé (VSM) — LSA isolée (LSAIso.exe) qui détient les secrets
```


LSASS ne garde plus que des références ; les secrets restent dans VTL1, inaccessibles depuis VTL0, même avec les droits SYSTEM. C'est la protection la plus forte de la liste, à condition d'un matériel compatible (virtualisation, Secure Boot, TPM recommandé).

### 13.3 Vérifier l'état

```powershell
# Credential Guard / VBS : services de sécurité configurés et actifs
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard |
    Select-Object SecurityServicesConfigured, SecurityServicesRunning

# LSA Protection
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name RunAsPPL -ErrorAction SilentlyContinue

# WDigest
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest -Name UseLogonCredential -ErrorAction SilentlyContinue
```


`SecurityServicesRunning` contient `1` quand Credential Guard est actif. L'outil *msinfo32* affiche la même information (section « Sécurité basée sur la virtualisation »).

---
