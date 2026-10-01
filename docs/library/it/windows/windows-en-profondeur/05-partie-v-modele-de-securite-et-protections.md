---
title: Partie V — Modèle de sécurité et protections
source: IT/02 Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 17 — Modèle de sécurité, intégrité et mitigations mémoire

### 17.1 Le Security Reference Monitor

Le SRM vérifie chaque accès : il compare le **token d'accès** du processus (SID de l'utilisateur, SIDs des groupes, privilèges) avec la **DACL** de l'objet (liste d'ACE Allow/Deny). Les tokens sont créés au logon et ne changent pas pendant la session. L'**impersonation** (un thread adopte temporairement l'identité d'un autre utilisateur — niveaux : Anonymous, Identification, Impersonation, Delegation).

### 17.2 Mandatory Integrity Control (MIC)

Niveaux d'intégrité : Untrusted, Low (navigateur sandboxé), Medium (processus utilisateur standard), High (processus élevé/admin), System (services), Protected Process. Un processus ne peut PAS écrire dans un objet d'intégrité supérieure — un processus Medium ne peut pas modifier un objet High.

### 17.3 UAC (User Account Control)

Un admin a deux tokens : un Medium (filtré) et un High (élevé). L'élévation demande le consentement (prompt UAC). Le **bypass UAC** obtient le token High sans le prompt — techniques : fodhelper.exe, eventvwr.exe (auto-elevation via registre), COM elevation moniker. Détection : Sysmon 1 avec les binaires d'auto-elevation comme parent + modification de registre Sysmon 13.

### 17.4 Mitigations mémoire et code

*Les protections modernes qui rendent l'exploitation de vulnérabilités et l'injection de code plus difficiles.*

**DEP** (Data Execution Prevention — empêche l'exécution de code dans les pages mémoire marquées « données » — le shellcode classique dans le heap ne peut plus s'exécuter directement). **ASLR** (Address Space Layout Randomization — randomise les adresses de chargement des DLLs et de l'exécutable — l'attaquant ne peut plus prédire les adresses pour ses gadgets ROP). **CFG** (Control Flow Guard — vérifie que les appels de fonctions indirects ciblent des adresses valides — protection contre le détournement du flux d'exécution). **CET** (Control-flow Enforcement Technology — Intel hardware, shadow stack — détecte la corruption de la pile par les exploits ROP/JOP). **ACG** (Arbitrary Code Guard — empêche un processus de générer du code dynamique — bloque la modification de pages mémoire en exécutable après allocation). **CIG** (Code Integrity Guard — empêche le chargement de DLLs non signées par Microsoft). **HVCI** (Hypervisor-Protected Code Integrity — utilise l'hyperviseur pour vérifier l'intégrité du code kernel — empêche le chargement de drivers non signés même avec admin ; fait partie de **VBS** — Virtualization-Based Security).

Ces mitigations se cumulent en couches — un exploit moderne doit contourner DEP (ROP), ASLR (info leak), CFG (appels indirects vérifiés), CET (shadow stack), et potentiellement HVCI. Chaque couche rend l'exploitation plus coûteuse pour l'attaquant.

---


## Chapitre 18 — Authentification locale et domaine

L'authentification locale : winlogon.exe → LogonUI → lsass.exe → SAM. L'authentification domaine : winlogon.exe → lsass.exe → Kerberos ou NTLM vers le DC (renvoi cours AD Ch.5-6). La **LSA** (Local Security Authority — le sous-système qui orchestre l'authentification ; les Security Packages — Negotiate, Kerberos, NTLM, WDigest, CredSSP ; un **SSP malveillant** peut être injecté dans lsass pour capturer les credentials — enregistrement via la clé registre Security Packages, détection : Sysmon 13 + 7). L'authentification par certificat (smart card, Windows Hello — PKINIT). Le **Credential Provider** (l'interface entre le logon screen et la LSA — les credential providers custom sont un vecteur de persistence rare mais discret).

---


## Chapitre 19 — Privilèges, élévation et contrôle d'exécution

Les **privilèges Windows** critiques : **SeDebugPrivilege** (accéder à la mémoire de tout processus → Mimikatz), **SeImpersonatePrivilege** (impersonation → Potato attacks), **SeBackupPrivilege** (lire tout fichier y compris SAM/NTDS.dit), **SeRestorePrivilege** (écrire tout fichier), **SeTcbPrivilege** (agir comme le système), **SeLoadDriverPrivilege** (charger un driver kernel). L'**élévation de privilèges** Potato (exploitent SeImpersonatePrivilege pour obtenir SYSTEM via la coercion NTLM interne — PrintSpoofer, GodPotato, JuicyPotato, SweetPotato ; détection : 4672 avec SeImpersonatePrivilege + processus inhabituel).

Le **contrôle d'exécution** : **AppLocker** (règles par path, hash, publisher → contournable mais ralentit l'attaquant — bypass via LOLBins, DLL side-loading), **WDAC** (Windows Defender Application Control — plus robuste, basé sur la politique code integrity du kernel, plus difficile à contourner que AppLocker), **SRP** (Software Restriction Policies — legacy, remplacé par AppLocker/WDAC).

---


## Chapitre 20 — Détection moderne : AMSI, ETW, EDR et BYOVD

### 20.1 AMSI (Anti-Malware Scan Interface)

AMSI est l'interface qui permet à PowerShell, VBA, JavaScript, .NET, et WSH de soumettre le code au moteur antimalware AVANT exécution. Quand un script PowerShell s'exécute, chaque bloc de code est passé à AMSI → l'AV le scanne → autorisation ou blocage. Les attaquants **patachent amsi.dll en mémoire** pour désactiver le scan (le champ amsiInitFailed est mis à $true, ou les instructions de AmsiScanBuffer sont remplacées par un retour immédiat). Détection : Script Block Logging (Event 4104) capture le code APRÈS le bypass AMSI (le bypass est lui-même loggé), ETW peut détecter le patching.

### 20.2 ETW (Event Tracing for Windows)

ETW est le mécanisme de trace universel de Windows. Les **providers** ETW génèrent des événements. Les **consumers** consomment ces événements — Event Logs, Sysmon, et les EDR sont des consumers ETW. Le provider **Microsoft-Windows-Threat-Intelligence** est utilisé par les EDR pour détecter les injections de code (il enregistre les opérations sur la mémoire de processus distants — WriteProcessMemory, NtMapViewOfSection). Les attaquants avancés **désactivent ou contournent les providers ETW** (patching des structures ETW en mémoire, NtTraceControl abuse). Détection : monitoring de la configuration ETW (Event 11 Sysmon sur les fichiers ETW, vérification de l'intégrité des providers).

### 20.3 EDR (Endpoint Detection and Response)

Comment les EDR fonctionnent : **hooking user mode** (les EDR remplacent les premières instructions des fonctions ntdll.dll par un JMP vers leur DLL de monitoring → chaque appel API suspect est intercepté et analysé), **callbacks kernel** (PsSetCreateProcessNotifyRoutine, PsSetLoadImageNotifyRoutine — le driver EDR est notifié à chaque création de processus et chargement d'image), **ETW consumption** (le driver EDR consomme les événements du provider Threat-Intelligence), **minifilter drivers** (interception des opérations I/O pour scanner les fichiers). Comment les EDR sont contournés : **unhooking** (restaurer les bytes originaux de ntdll.dll pour supprimer les hooks EDR), **syscalls directs** (sauter ntdll.dll entièrement → les hooks ne sont jamais traversés), **BYOVD** (voir ci-dessous), et **ETW patching** (désactiver les providers ETW qui alimentent l'EDR).

### 20.4 BYOVD (Bring Your Own Vulnerable Driver)

*Une technique moderne majeure qui mérite une attention particulière.*

Le **BYOVD** consiste à charger un driver légitime mais vulnérable (un ancien driver signé par un éditeur reconnu — Dell, Intel, HP, Realtek — qui contient une vulnérabilité connue) pour obtenir un accès kernel. Une fois en kernel mode, l'attaquant peut : désactiver l'EDR (tuer le processus EDR, désactiver les callbacks kernel, supprimer les hooks), désactiver la protection de lsass (accéder à la mémoire de lsass même avec RunAsPPL), et charger un rootkit. Le driver est légitime et signé → il passe le driver signing enforcement. Exemples : gdrv.sys (Gigabyte), procexp.sys (Process Explorer — le driver du propre outil Sysinternals a été abusé), dbutil_2_3.sys (Dell).

La défense : **HVCI** (Hypervisor-Protected Code Integrity — vérifie l'intégrité du code kernel et peut bloquer les drivers vulnérables connus), les **Microsoft Vulnerable Driver Blocklist** (liste de drivers vulnérables bloqués par Windows), **WDAC** avec blocage de drivers spécifiques, et le monitoring (Event 7045 chargement de driver, Sysmon 6 — DriverLoaded — hash du driver → comparaison avec la liste des drivers vulnérables connus).

---
