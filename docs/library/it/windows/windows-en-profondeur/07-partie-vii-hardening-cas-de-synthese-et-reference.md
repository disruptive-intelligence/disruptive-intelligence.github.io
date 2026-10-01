---
title: Partie VII — Hardening, cas de synthèse et référence
source: IT/02 Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 27 — Hardening Windows : P0 / P1 / P2

### 27.1 P0 — Actions immédiates (semaine 1)

(1) Activer le command line logging (GPO Audit Process Creation + Include command line — sans ça, les Event 4688 sont aveugles). (2) Déployer Sysmon avec la config SwiftOnSecurity. (3) Centraliser les logs (WEF ou agent SIEM — les logs locaux sont effacés par l'attaquant). (4) Désactiver LLMNR + NBT-NS (GPO — bloque le poisoning Responder). (5) Désactiver SMBv1 (GPO — bloque EternalBlue). (6) Bloquer les macros Office dans les documents provenant d'Internet (GPO — la mesure anti-phishing la plus efficace). (7) Activer Script Block Logging PowerShell (GPO — la détection PowerShell n°1).

### 27.2 P1 — Actions sous 3 mois

(8) Déployer LAPS (mot de passe admin local unique par machine). (9) Activer Credential Guard sur les machines compatibles (Enterprise, VBS capable). (10) Activer RunAsPPL sur lsass (GPO — protection contre le dump mémoire). (11) Activer SMB signing obligatoire (GPO — bloque le relay NTLM). (12) Configurer les ASR rules (Defender — bloquer les processus enfants de Office, bloquer les appels Win32 depuis macros). (13) Activer BitLocker sur tout le parc (protection offline). (14) Désactiver les protocoles legacy (WDigest — vérifier UseLogonCredential=0, NTLMv1 — désactiver).

### 27.3 P2 — Actions à moyen terme (6 mois)

(15) Configurer AppLocker ou WDAC (contrôle d'exécution — seuls les binaires autorisés s'exécutent). (16) Activer HVCI (blocage des drivers non signés — protection BYOVD partielle). (17) Déployer la Microsoft Vulnerable Driver Blocklist. (18) Activer Transcription Logging PowerShell (complément au Script Block). (19) Configurer les restrictions de contenu exécutable téléchargeable (GPO + SmartScreen). (20) Auditer et supprimer les points de persistence inutiles (Autoruns — services, tâches, clés Run non nécessaires). (21) Mettre en place le monitoring des LOLBins (règles SIEM sur certutil, mshta, rundll32, regsvr32, bitsadmin avec command lines suspectes).

---


## Chapitre 28 — Cas complet : investigation malware fileless (synthèse SHADOW)

Synthèse du fil rouge. L'investigation complète de Léa sur l'incident Valtec Industries.

**Phase 1 — Alerte et triage :** CrowdStrike détecte rundll32.exe enfant de winword.exe contactant une IP C2. Léa vérifie l'arbre (anormal — Ch.6), la command line (Sysmon 1 — rundll32 charge une DLL depuis %TEMP%), les connexions (Sysmon 3 — beaconing 60s vers 185.220.xxx.xxx:443).

**Phase 2 — Vecteur initial :** document Word piégé reçu par email. Zone.Identifier confirme la source (pièce jointe Outlook). La macro VBA (Event 4104 Script Block) : certutil télécharge une DLL → rundll32 l'exécute → injection en mémoire. La chaîne MotW→SmartScreen→Protected View a été contournée : le document était dans une archive .zip qui n'a pas préservé le MotW → Protected View ne s'est pas activé → la macro s'est exécutée directement. Les macros n'étaient pas bloquées par GPO (la mesure P0 n°6 aurait empêché l'attaque).

**Phase 3 — Payload et évasion :** la DLL utilise du Process Hollowing (Sysmon 25 — ProcessTampering) pour injecter du code dans svchost.exe. Le svchost creux contacte le C2 via HTTPS (Sysmon 3 + 22 DNS query). Un second stage est téléchargé via BITS. AMSI a été bypassé (patching amsi.dll — visible dans Script Block Logging Event 4104). Le payload n'a jamais touché le disque après l'injection (fileless — Ch.26).

**Phase 4 — Persistence :** scheduled task « WindowsUpdateCheck » (Event 4698), clé Run HKCU (Sysmon 13), WMI Event Subscription (Sysmon 19/20/21) — 3 mécanismes de persistence redondants.

**Phase 5 — Mouvement latéral :** dump lsass via comsvcs.dll (Sysmon 10 — accès lsass par rundll32 + comsvcs.dll en command line — un LOLBin classique). Credentials de l'admin IT récupérées (pas de Credential Guard — la mesure P1 n°9 aurait bloqué). WMI vers SRV-FILE01 (Event 4624 type 3 + 4688 wmiprvse.exe). PsExec vers SRV-APP02 (Event 7045 — PSEXESVC). DCSync depuis SRV-APP02 (Event 4662 — droits de réplication depuis non-DC → alerte critique).

**Timeline :** 09:12 email → 09:15 macro → 09:15 DLL téléchargée (certutil) → 09:16 process hollowing svchost → 09:17 C2 → 09:18 persistence (×3) → 09:25 dump lsass → 09:30 WMI latéral → 09:35 PsExec → 09:42 DCSync. **30 minutes du phishing au Domain Admin.**

**IOCs et recommandations :** hash DLL, IP C2, domaine DNS, clés de registre, noms de scheduled tasks. Recommandations priorisées : P0 — bloquer macros Internet (GPO), centraliser les logs AD CS ; P1 — Credential Guard, LAPS, ASR rules Office ; P2 — WDAC, HVCI. Le MotW bypass via archive .zip est le vecteur critique — recommandation : configurer la politique d'archivage pour propager le MotW (fonctionnalité Windows 11 22H2+).

---


## Chapitre 29 — Cas complet : analyse d'un ransomware pré-détonation

Un fichier suspect intercepté par l'email gateway. Léa analyse en sandbox. **Analyse statique** (PE : entropy élevée = packing UPX, imports suspects — CryptEncrypt, FindFirstFileW, GetLogicalDriveStrings → probable ransomware, strings : note de rançon en anglais, extensions ciblées .docx .xlsx .pdf .pst, commande vssadmin delete shadows). **Analyse dynamique** en sandbox (dépackage UPX → imports réels visibles, exécution : création de mutex GlobalRansomLock, énumération des drives, chiffrement AES-256 fichier par fichier avec renommage en .locked, suppression des shadow copies via vssadmin, dépose de la note de rançon README_UNLOCK.txt dans chaque dossier). **Artefacts générés** : Sysmon 1 (process creation avec vssadmin delete shadows en child), Sysmon 11 (création de README_UNLOCK.txt dans de multiples dossiers — pattern détectable), Sysmon 13 (modification du registre — désactivation de la restauration système), Event 7045 (service créé pour la persistence). Le cas enseigne l'analyse PE (Ch.8), les mécanismes d'exécution (Ch.7), et comment construire des règles de détection avant la détonation.

---


## Chapitre 30 — Cas complet : investigation mémoire avec Volatility

Un dump mémoire (RAM) réalisé sur une machine suspecte. Léa utilise **Volatility 3** : **windows.pslist** (lister les processus — un svchost.exe avec un PPID suspect, PID 8240, parent services.exe mais image path anormal), **windows.psscan** (scan des structures EPROCESS en mémoire — détecte les processus cachés/unlinkés par un rootkit — un processus invisible dans pslist mais présent dans psscan = rootkit), **windows.netscan** (connexions réseau — une connexion vers l'IP C2 depuis le PID 8240, confirmant le svchost creux), **windows.malfind** (sections mémoire RWX dans le svchost — code injecté détecté, signature de shellcode), **windows.cmdline** (commandes des processus — le svchost n'a pas d'argument -k attendu), **windows.hashdump** (hashes SAM), **windows.lsadump** (tickets Kerberos en mémoire). Le cas enseigne l'analyse mémoire comme compétence forensic complémentaire à l'analyse disque.

---


## Chapitre 31 — Arbre de processus normal Windows

la référence de détection

*Ce chapitre est une référence — l'arbre de processus normal est le fondement de la détection basée sur le comportement.*

L'arbre complet avec, pour chaque processus : le parent attendu, le chemin attendu, le nombre d'instances attendu, l'utilisateur attendu, les arguments attendus, et les anomalies qui signalent une compromission.

**System** (PID 4, pas de parent, kernel mode, toujours présent — anomalie : PID ≠ 4). **smss.exe** (parent : System, chemin : %SystemRoot%\System32, 1 instance enfant de System — anomalie : parent ≠ System, chemin ≠ System32, instances multiples enfants de System). **csrss.exe** (parent : smss.exe devenu orphelin car smss se termine, chemin : System32, 2+ instances — anomalie : parent visible autre que smss orphelin). **wininit.exe** (parent : smss.exe orphelin, chemin : System32, 1 instance — anomalie : parent ≠ smss orphelin, instances multiples). **services.exe** (parent : wininit.exe, chemin : System32, 1 instance, utilisateur : SYSTEM — anomalie : parent ≠ wininit.exe, instances multiples, utilisateur ≠ SYSTEM). **svchost.exe** (parent : services.exe, chemin : System32, multiples instances, utilisateur : SYSTEM/LOCAL SERVICE/NETWORK SERVICE, **arguments : -k [nom_groupe]** — anomalies critiques : parent ≠ services.exe, chemin ≠ System32, pas d'argument -k, argument -k inhabituel, utilisateur ≠ SYSTEM/LOCAL/NETWORK SERVICE). **lsass.exe** (parent : wininit.exe, chemin : System32, **1 seule instance**, utilisateur : SYSTEM — anomalies critiques : parent ≠ wininit.exe, chemin ≠ System32, **2 instances = la seconde est probablement malveillante**, utilisateur ≠ SYSTEM). **winlogon.exe** (parent : smss.exe orphelin, chemin : System32, 1+ instances par session — anomalie : chemin ≠ System32). **explorer.exe** (parent : userinit.exe devenu orphelin, chemin : %SystemRoot%, 1 instance par session utilisateur — anomalie : parent autre que userinit orphelin, instances multiples pour un même utilisateur).

Les **cas courants de faux positifs** : Windows Update peut lancer des processus avec des parentés inhabituelles, les outils de management (SCCM, Intune) peuvent créer des processus enfants de services atypiques, et certains logiciels tiers légitimes ont des arbres de processus non standard → la baseline de l'environnement est indispensable pour réduire les faux positifs.

---
