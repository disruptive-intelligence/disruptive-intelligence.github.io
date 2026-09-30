---
title: Chapitre 17 — Memory forensics
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

## 17.1 Workflows d'analyse concrète avec Volatility 3

Au-delà de la liste des plugins (présentée au Ch.6 pour le dump et dans le cours original), ce chapitre se concentre sur les workflows d'analyse concrets — comment l'analyste utilise les plugins en séquence pour répondre aux questions investigatives.

**Workflow 1 — Triage initial (5 minutes) :** identifier rapidement si la machine est compromise. (1) `windows.pslist` / `windows.pstree` → examiner l'arbre des processus : les processus avec des parents anormaux (svchost.exe avec explorer.exe comme parent, cmd.exe avec iexplore.exe comme parent) sont suspects. (2) `windows.netscan` → identifier les connexions réseau actives vers des destinations suspectes (IP externes non connues, ports inhabituels). (3) `windows.cmdline` → examiner les lignes de commande des processus suspects. En 5 minutes, l'analyste sait si la machine est compromise et a identifié les premiers IoC (IP C2, processus malveillant).

**Workflow 2 — Investigation de process injection (30 minutes) :** quand un processus suspect est identifié. (1) `windows.malfind` → détecter les régions mémoire avec des permissions suspectes (PAGE_EXECUTE_READWRITE — RWX — est rare pour du code légitime et typique d'injection). Attention aux faux positifs : certains programmes légitimes (JIT compilers comme .NET CLR, navigateurs web) utilisent RWX légitimement. L'analyse doit être contextuelle. (2) `windows.dlllist --pid <PID>` → lister les DLL chargées par le processus suspect — identifier les DLL inhabituelles ou non signées. (3) `windows.handles --pid <PID>` → examiner les handles ouverts (fichiers, clés de registre, mutex — un mutex nommé peut identifier une famille de malware connue). (4) `windows.procdump --pid <PID> --dump-dir output/` → extraire le binaire du processus pour analyse malware.

**Workflow 3 — Extraction de credentials (15 minutes) :** (1) `windows.hashdump` → extraire les hashes NTLM des comptes locaux depuis SAM en mémoire. (2) `windows.lsadump` → extraire les secrets LSA (mots de passe de services, clés DPAPI). (3) Recherche de strings caractéristiques de mimikatz (`sekurlsa::logonPasswords`, `sekurlsa::wdigest`) dans le dump pour déterminer si l'attaquant a utilisé mimikatz. (4) Recherche de credentials en clair dans le processus lsass avec `windows.memmap --pid <lsass_pid> --dump-dir output/` puis strings et grep.

**Workflow 4 — Analyse de rootkit (avancé) :** `windows.modules` → lister les modules kernel chargés. `windows.ssdt` → vérifier la System Service Dispatch Table pour détecter les hooks. `windows.callbacks` → lister les callbacks enregistrés (un rootkit enregistre des callbacks pour intercepter les opérations système).

## 17.2 Pagefile et hiberfil comme mémoire fossile

Quand le dump RAM n'a pas été fait à temps (la machine a été redémarrée avant l'intervention forensic), le **pagefile.sys** et le **hiberfil.sys** sont des sources de mémoire « fossile ». Le pagefile contient des pages mémoire qui ont été déplacées vers le disque — elles peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le hiberfil est un dump mémoire compressé créé lors de l'hibernation — analysable avec Volatility.

Extraction des strings du pagefile : `strings -el pagefile.sys > pagefile_strings_unicode.txt` puis recherche de patterns (URLs, IP, chemins de fichiers suspects, noms de domaine). La recherche dans le pagefile est moins structurée que l'analyse d'un dump RAM complet (pas de structure de processus), mais elle peut révéler des données critiques quand le dump RAM est indisponible.

## 17.3 YARA rules sur les dumps mémoire

Les règles YARA permettent de scanner le dump mémoire pour détecter des patterns caractéristiques de familles de malware connues. Le plugin `windows.yarascan` de Volatility exécute des règles YARA sur l'espace mémoire de chaque processus. Les sources de règles YARA : le repository `awesome-yara` sur GitHub, les règles publiées par les éditeurs CTI (Mandiant, CrowdStrike, ESET), et les règles custom créées à partir des IoC spécifiques à l'investigation.

## 17.4 Fil rouge — MUSIC BOX : la mémoire raconte tout

> **🔬 MUSIC BOX — Épisode 15**
>
> Analyse du dump RAM de WKS-RD-047 (32 Go) avec Volatility 3.
>
> **Workflow triage :** `pstree` révèle le processus suspect : `svchost.exe` (PID 7284, PPID 3412 = explorer.exe). Un svchost légitime a toujours `services.exe` comme parent — celui-ci est enfant d'explorer.exe. C'est un process hollowing : le processus svchost a été créé normalement puis son code a été remplacé en mémoire par le RAT.
>
> **Workflow injection :** `malfind` détecte une section RWX dans l'espace mémoire de PID 7284 contenant du code exécutable — confirmation de l'injection. `netscan` montre que PID 7284 maintient une connexion ESTABLISHED vers `103.xx.xx.xx:443` — le C2. `procdump` extrait le payload injecté pour analyse malware (Ch.18).
>
> **Workflow credentials :** `hashdump` extrait les hashes NTLM de 12 comptes locaux. La recherche de strings dans le processus `lsass.exe` révèle des credentials en clair pour 8 comptes AD (l'attaquant a utilisé mimikatz — les credentials wdigest sont en mémoire). Le compte `svc-backup` (Domain Admin) est parmi eux — confirmation que le credential dumping a réussi.

---
