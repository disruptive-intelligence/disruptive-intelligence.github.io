---
title: Partie I — Architecture fondamentale
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

*Comment Windows est construit, du boot au bureau — comprendre le normal pour détecter l'anormal.*

---


## Chapitre 1 — Vue d'ensemble de Windows

### 1.1 Pourquoi comprendre Windows en profondeur

En cybersécurité, Windows est partout : plus de 75 % des postes en entreprise, la quasi-totalité des environnements Active Directory, et la cible principale des malwares. On ne peut pas analyser un incident, investiguer un malware, ou hardener un poste si on ne comprend pas comment Windows fonctionne sous le capot. Ce cours n'est pas un cours d'administration classique — c'est un cours « comment Windows fonctionne réellement » avec un prisme sécurité permanent : chaque concept est relié à son exploitation ou sa défense.

### 1.2 Historique et éditions

Windows repose sur le noyau NT, conçu en 1993. La lignée : NT 3.1 → NT 4.0 → 2000 → XP → Vista → 7 → 8 → 10 → 11. Côté serveur : Server 2003 → 2008 → 2012 → 2016 → 2019 → 2022 → 2025. Le noyau est fondamentalement le même entre les versions client et serveur d'une même génération. Les éditions et leurs différences sécurité : **Home** (pas de BitLocker, pas de GPO complète, pas de domain join, pas de Credential Guard), **Pro** (BitLocker, GPO locale, domain join, Hyper-V), **Enterprise** (Credential Guard, WDAC complet, AppLocker, Defender for Endpoint complet), **Server** (rôles AD DS, AD CS, DNS, DHCP, NPS — noyau identique à la version client).

### 1.3 Architecture haut niveau : User mode vs Kernel mode

Windows sépare strictement deux niveaux d'exécution. **Ring 3 (User mode)** : les applications, les services, l'explorateur. Accès limité au matériel et à la mémoire. Un crash en user mode ne fait planter que le processus. **Ring 0 (Kernel mode)** : le noyau (ntoskrnl.exe), les drivers, le HAL. Accès total au matériel et à toute la mémoire. Un crash en kernel mode provoque un BSOD. Cette séparation est la base de la sécurité Windows : un processus utilisateur ne peut pas directement lire la mémoire d'un autre processus ou accéder au matériel — il doit passer par des appels système (syscalls) contrôlés par le noyau.

### 1.4 Composants majeurs

**ntoskrnl.exe** (noyau — scheduler, memory manager, I/O manager, Security Reference Monitor — kernel mode), **hal.dll** (Hardware Abstraction Layer — kernel), **win32k.sys** (sous-système graphique — kernel), **csrss.exe** (Client/Server Runtime — gestion des sessions, consoles — user mode), **smss.exe** (Session Manager — premier processus user mode, lance csrss et wininit), **services.exe** (Service Control Manager/SCM — gère tous les services), **lsass.exe** (Local Security Authority — authentification, tokens, credentials — la cible n°1 de Mimikatz), **svchost.exe** (héberge les services partagés — plusieurs instances, chacune avec des services spécifiques identifiés par l'argument -k), **explorer.exe** (shell Windows — bureau, barre des tâches).

Pour l'analyste SOC, connaître ces composants et leur rôle est fondamental : un processus qui n'est pas dans cette liste, ou qui se comporte différemment de son rôle attendu, est potentiellement suspect.

### 1.5 Object Manager et Security Reference Monitor

Windows gère toutes ses ressources comme des **objets** (processus, threads, fichiers, clés de registre, mutex, events, sections mémoire). L'Object Manager crée, gère et détruit ces objets. Chaque objet a un type, un nom (optionnel), un Security Descriptor (qui contrôle l'accès), et un reference count. Les **handles** sont les références qu'un processus obtient pour accéder à un objet. Le **Security Reference Monitor (SRM)** vérifie les droits à chaque création de handle : il compare le token du processus (son identité) avec la DACL de l'objet (ses permissions). Tout accès — fichier, registre, processus, réseau — passe par ce mécanisme.

### 1.6 Outils Sysinternals

La suite Sysinternals (Microsoft, gratuite) est LA boîte à outils du professionnel Windows : **Process Explorer** (processus en détail — DLLs, handles, tokens, strings, VirusTotal), **Process Monitor** (capture en temps réel de toute l'activité fichiers/registre/réseau/processus), **Autoruns** (TOUS les points de persistence — services, drivers, Run keys, tasks, COM), **TCPView** (connexions réseau par processus en temps réel), **Handle** (handles ouverts par un processus), **Strings** (chaînes d'un binaire), **Sigcheck** (vérification des signatures numériques + VirusTotal), **WinObj** (espace de noms des objets kernel), **PsExec** (exécution à distance via SMB).

### 1.7 Fil rouge — SHADOW : l'alerte

> **🔍 SHADOW — Épisode 1**
>
> Léa reçoit l'alerte CrowdStrike. Premier réflexe : vérifier l'arbre de processus. `winword.exe` (PID 4528) → `rundll32.exe` (PID 6712) — anormal. Le parent normal de rundll32 est explorer.exe ou svchost.exe, pas un processus Office. Le processus rundll32 contacte l'IP 185.220.xxx.xxx sur le port 443 — beaconing toutes les 60 secondes. Léa sait qu'elle regarde un accès initial via macro Word avec un C2 actif.

---


## Chapitre 2 — Le processus de démarrage (boot process)

La séquence complète : (1) **Firmware UEFI** (POST, initialisation matérielle, recherche périphérique bootable), (2) **bootmgr** (lit le BCD, affiche le menu de boot), (3) **winload.exe** (charge ntoskrnl.exe, le HAL, les drivers boot-start, et le registre SYSTEM), (4) **ntoskrnl.exe** (initialise le noyau, lance smss.exe), (5) **smss.exe** (crée les sessions, lance csrss.exe + wininit.exe en session 0, csrss.exe + winlogon.exe en session 1), (6) **wininit.exe** (lance services.exe + lsass.exe), (7) **services.exe** (démarre tous les services auto-start), (8) **winlogon.exe** (écran de logon), (9) **explorer.exe** (après authentification — bureau, shell utilisateur).

**UEFI vs BIOS legacy** (GPT vs MBR, Secure Boot). Le **Secure Boot** vérifie la signature de chaque composant de boot — protection contre les bootkits. Le **Measured Boot + TPM** enregistre les mesures d'intégrité dans les PCR du TPM — attestation à distance. Le **BCD** (Boot Configuration Data — bcdedit.exe).

La **persistence pré-OS** : bootkits (TDL4, Rovnix, **BlackLotus** — UEFI bootkit 2023 qui contourne Secure Boot), drivers boot-start, implants firmware (LoJax/APT28, CosmicStrand — persistent même après réinstallation OS), modification BCD. Un malware pré-OS est quasi invisible pour l'EDR (qui s'exécute après le boot). La **persistence post-boot** : services auto-start, drivers, scheduled tasks, Run/RunOnce registre, Winlogon, startup folders — visible mais noyée dans le légitime → Autoruns les liste toutes.

---


## Chapitre 3 — Noyau, mémoire et drivers

La séparation user/kernel appliquée par le processeur (rings x86). Le **syscall** : quand un programme appelle CreateFile(), la requête traverse ntdll.dll (user mode) → syscall → ntoskrnl.exe (kernel mode) → I/O Manager → driver → disque. L'**espace d'adressage virtuel** (128 To sur x64 — partie basse = user space propre à chaque processus, partie haute = kernel space partagé — isolation mémoire). La **mémoire virtuelle** (pages 4 Ko, page tables, pagefile.sys — peut contenir des credentials et du code malveillant → artefact forensic, working set).

Le noyau **ntoskrnl.exe** (Scheduler — threads sur les cœurs CPU, Memory Manager — mémoire virtuelle et pagefile, I/O Manager — entrées/sorties via drivers, Object Manager — tous les objets kernel, Security Reference Monitor — vérifie les droits). Les **drivers** (kernel mode ring 0, accès total — un driver malveillant = contrôle complet du système ; **driver signing obligatoire** sauf en mode test ; **HVCI** — Hypervisor-Protected Code Integrity — bloque les drivers non signés même avec admin, basé sur VBS — Virtualization-Based Security). Les **mini-filter drivers** (interception des opérations I/O — c'est ainsi que les antivirus scannent les fichiers en temps réel et que les EDR surveillent l'activité disque).

---


## Chapitre 4 — Système de fichiers NTFS

NTFS est le système de fichiers de Windows — journal, permissions, compression, chiffrement EFS. La **MFT** (Master File Table) contient un enregistrement par fichier/dossier, même supprimé récemment → artefact forensic majeur (MFTECmd — Eric Zimmerman). Les **timestamps MACB** (Modified, Accessed, Changed, Birth) existent en 2 copies : $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le noyau) — les attaquants modifient $SI mais pas $FN → l'analyse comparée détecte le **timestomping**.

Les **Alternate Data Streams** (ADS — données cachées dans un flux alternatif du même fichier). Le plus important : **Zone.Identifier** = le **Mark of the Web (MotW)** — quand un fichier est téléchargé depuis Internet ou reçu par email, Windows écrit la source dans un ADS Zone.Identifier. Ce MotW déclenche toute la chaîne de protection : SmartScreen → Office Protected View → restrictions de macros → ASR rules (Ch.26). Les malwares stockent parfois du code dans des ADS pour le dissimuler.

Le **$UsnJrnl** (journal des modifications — création, suppression, renommage — artefact forensic pour la timeline). Les permissions NTFS (ACL sur les fichiers et dossiers, héritage, droits effectifs). L'EFS (Encrypting File System — chiffrement par fichier, clé de l'utilisateur).

---


## Chapitre 5 — Registre Windows, hives et persistence

Le registre est la base de données hiérarchique de configuration de Windows. Les **hives** : **SAM** (comptes locaux — hashes NTLM), **SECURITY** (secrets LSA — mots de passe de services, clés de chiffrement), **SOFTWARE** (configuration des applications et de l'OS), **SYSTEM** (configuration hardware, services, drivers — contient la boot key qui déchiffre SAM), **NTUSER.DAT** (par utilisateur — configuration personnelle, persistence par utilisateur).

Les **clés de persistence** — les emplacements où un malware s'inscrit pour survivre au redémarrage : **Run/RunOnce** (HKLM et HKCU — exécution au logon), **Services** (HKLM\SYSTEM\CurrentControlSet\Services — exécution par SCM), **Winlogon Shell/Userinit** (détournement du processus de logon), **AppInit_DLLs** (DLL chargée dans tout processus qui charge user32.dll — vecteur d'injection global), **IFEO** (Image File Execution Options — permet de rediriger l'exécution d'un exe vers un autre = hijack), **COM Objects CLSID** (détournement de l'appel COM vers une DLL malveillante — COM Hijacking), **Boot Execute** (programmes exécutés par smss.exe au boot — rare mais très discret).

Le registre comme source forensic : la dernière modification d'une clé = timestamp exploitable. Outils : RECmd, Registry Explorer (Eric Zimmerman). Les protections : clés protégées par ACL, WRP (Windows Resource Protection).

---
