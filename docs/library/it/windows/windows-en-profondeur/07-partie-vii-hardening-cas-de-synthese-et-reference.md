---
title: Partie VII — Hardening, cas de synthèse et référence
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 27 — Hardening Windows : P0 / P1 / P2

*Durcir, c'est réduire la surface d'attaque sans casser les usages. On procède par vagues : d'abord la visibilité et les protocoles inutiles, puis la protection des identifiants, enfin le contrôle de l'exécution. Chaque mesure passe par un pilote avant le déploiement général, et les baselines de référence (Microsoft Security Baselines, guides de l'ANSSI, CIS Benchmarks) servent de point de départ.*

### 27.1 P0 — Actions immédiates (première semaine)

| # | Mesure | Comment | Pourquoi |
|---|---|---|---|
| 1 | Ligne de commande dans les créations de processus | GPO *Audit Process Creation* + *Include command line* | Sans elle, 4688 ne dit pas ce qui a été exécuté |
| 2 | Sysmon | Configuration de référence, déployée par GPO ou Intune | Télémétrie riche (Ch.22) |
| 3 | Centralisation des journaux | WEF ou agent SIEM | Un journal local s'efface |
| 4 | LLMNR et NBT-NS désactivés | GPO *Turn off multicast name resolution* ; NetBIOS désactivé sur les interfaces | Supprime la résolution de noms par diffusion |
| 5 | SMBv1 désactivé | Fonctionnalité Windows / GPO | Protocole obsolète et vulnérable |
| 6 | Macros des documents venus d'Internet bloquées | GPO Office | Premier vecteur d'accès par hameçonnage |
| 7 | Script Block Logging PowerShell | GPO | Visibilité sur PowerShell (Ch.10) |

### 27.2 P1 — Sous trois mois

| # | Mesure | Pourquoi |
|---|---|---|
| 8 | Windows LAPS | Mot de passe administrateur local unique par machine |
| 9 | Credential Guard (matériel compatible) | Isole les secrets d'authentification de LSASS |
| 10 | LSA Protection (*RunAsPPL*) | LSASS en processus protégé |
| 11 | Signature SMB obligatoire | Empêche la réutilisation d'authentifications NTLM vers SMB |
| 12 | Règles ASR de Defender | Bloque des comportements typiques (enfants des applications Office, scripts obfusqués…) |
| 13 | BitLocker sur tout le parc | Protège les données et les ruches en cas de vol ou d'accès hors ligne |
| 14 | Protocoles anciens retirés | WDigest désactivé (vérifier `UseLogonCredential = 0`), NTLMv1 et LM refusés |

### 27.3 P2 — À six mois

| # | Mesure | Pourquoi |
|---|---|---|
| 15 | AppLocker ou WDAC, d'abord en mode audit | Seuls les programmes autorisés s'exécutent |
| 16 | HVCI (intégrité du code noyau) | Bloque les pilotes non conformes |
| 17 | Liste de blocage des pilotes vulnérables de Microsoft | Ferme l'usage de pilotes signés mais vulnérables |
| 18 | Transcription PowerShell | Complète le Script Block Logging |
| 19 | SmartScreen et propagation du Mark of the Web | Préserve la chaîne de protection des fichiers téléchargés (Ch.26) |
| 20 | Revue des points de persistance (Autoruns) | Supprimer services, tâches et clés Run inutiles |
| 21 | Règles SIEM sur les binaires système détournables | Surveiller les usages inhabituels de certutil, mshta, rundll32, regsvr32… |

### 27.4 Durcir sans casser

```text
Inventorier → choisir une baseline → tester sur un groupe pilote (mode audit quand il existe)
→ déployer par vagues → mesurer (conformité, incidents) → documenter les exceptions
```


Une exception n'est acceptable que si elle est **justifiée, limitée dans le temps, compensée** (surveillance renforcée, segmentation) et **revue** régulièrement.

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

*Ce chapitre est une fiche de référence : savoir à quoi ressemble un système sain est la condition pour repérer l'anomalie.*

### 31.1 L'arbre

```text
System (PID 4)
└── smss.exe                         ← une instance « maître », enfant de System
    ├── csrss.exe        (session 0)  ← le smss enfant se termine : parent orphelin
    ├── wininit.exe      (session 0)
    │   ├── services.exe
    │   │   └── svchost.exe -k <groupe>   (nombreuses instances)
    │   │       └── … services hébergés
    │   └── lsass.exe                 ← UNE seule instance
    ├── csrss.exe        (session 1+)
    └── winlogon.exe     (session 1+)
        └── userinit.exe → explorer.exe   ← userinit se termine : explorer orphelin
                              └── applications de l'utilisateur
```


### 31.2 La fiche par processus

| Processus | Parent attendu | Chemin | Instances | Compte | Anomalies typiques |
|---|---|---|---|---|---|
| **System** | — | (noyau) | 1 | SYSTEM | PID différent de 4 |
| **smss.exe** | System | `System32` | 1 maître (+ enfants éphémères) | SYSTEM | Autre parent, instances persistantes multiples |
| **csrss.exe** | smss.exe (orphelin) | `System32` | 2 et plus (une par session) | SYSTEM | Parent visible, autre chemin |
| **wininit.exe** | smss.exe (orphelin) | `System32` | 1 | SYSTEM | Plusieurs instances |
| **services.exe** | wininit.exe | `System32` | 1 | SYSTEM | Autre parent, autre compte |
| **svchost.exe** | services.exe | `System32` (ou `SysWOW64`) | Nombreuses | SYSTEM, LOCAL SERVICE, NETWORK SERVICE | Parent ≠ services.exe, pas d'argument `-k`, compte utilisateur, faute dans le nom (`scvhost`) |
| **lsass.exe** | wininit.exe | `System32` | **1** | SYSTEM | Deuxième instance, autre parent, autre chemin, processus enfants |
| **winlogon.exe** | smss.exe (orphelin) | `System32` | 1 par session | SYSTEM | Autre chemin |
| **explorer.exe** | userinit.exe (orphelin) | `C:\Windows` | 1 par utilisateur connecté | L'utilisateur | Autre parent, plusieurs instances pour un même utilisateur |

### 31.3 Les quatre vérifications

Pour tout processus critique : **parent**, **chemin**, **nombre d'instances**, **compte**. On y ajoute la **signature** du binaire et la **ligne de commande**. Une seule incohérence justifie un examen ; c'est leur combinaison qui qualifie la suspicion.

**Chaînes parent → enfant suspectes à connaître :**

```text
winword.exe / excel.exe / outlook.exe → powershell.exe, cmd.exe, wscript.exe, mshta.exe, rundll32.exe
navigateur → rundll32.exe, regsvr32.exe
services.exe → cmd.exe /c … (service créé pour lancer une commande)
wmiprvse.exe → powershell.exe (exécution via WMI)
```


### 31.4 Faux positifs

Windows Update, les outils de gestion (SCCM, Intune), les installeurs et certains logiciels métier produisent des parentés inhabituelles. La **baseline de l'environnement** — ce qui est normal ici — est indispensable pour que les règles de détection restent utiles.

---
