---
title: PARTIE IV — ANALYSE FORENSIC AVANCÉE
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 5
chapters: 9
---

*Le cœur technique du cours. Sept chapitres couvrant l'analyse détaillée des artefacts Windows (3 chapitres avec frontières nettes : registre/exécution, activité/mouvement latéral, Event Logs), Linux, macOS, mémoire vive, et malware.*

---

### Chapitre 12 — Windows forensics : registre et artefacts d'exécution

*Ce chapitre couvre ce que la machine « sait » sur les programmes qui ont été exécutés. Le Ch.13 couvrira l'activité utilisateur et le mouvement latéral. Le Ch.14 couvrira les Event Logs. Cette séparation évite les redites : le Prefetch apparaît ici (artefact d'exécution), les traces RDP apparaissent au Ch.13 (mouvement latéral), et les Event IDs apparaissent au Ch.14 (journaux d'audit).*

#### 12.1 Le registre Windows comme mine forensic

Le registre Windows est une base de données hiérarchique qui stocke la configuration du système et des applications. Pour le forensic, c'est la source la plus riche après les Event Logs.

Les **fichiers de ruche** (hive files) sont les fichiers physiques qui contiennent le registre. Leur localisation est fixe. **SAM** (`C:\Windows\System32\config\SAM`) contient les comptes locaux et leurs hashes NTLM — exploitable avec `secretsdump.py` ou RegRipper pour identifier les comptes créés par l'attaquant. **SYSTEM** (`C:\Windows\System32\config\SYSTEM`) contient la configuration matérielle, le nom de l'ordinateur, le fuseau horaire (critique pour la corrélation), les informations de boot, et la clé de déchiffrement (BootKey) nécessaire pour décrypter les hashes SAM. **SOFTWARE** (`C:\Windows\System32\config\SOFTWARE`) contient les logiciels installés (clé `Microsoft\Windows\CurrentVersion\Uninstall`), les profils réseau (clé `Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` — historique des réseaux WiFi et Ethernet avec dates de connexion), et les services (clé `CurrentControlSet\Services`). **NTUSER.DAT** (`C:\Users\<username>\NTUSER.DAT`) est la ruche spécifique à chaque utilisateur : elle contient les MRU (Most Recently Used — derniers fichiers ouverts), les ShellBags (navigation dans l'explorateur), les clés Run/RunOnce (persistence au login), les UserAssist (programmes exécutés via le GUI avec nombre d'exécutions et timestamps), et les Typed Paths (chemins saisis manuellement dans l'explorateur — y compris les chemins réseau UNC). **UsrClass.dat** (`C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat`) contient les associations de fichiers et les ShellBags supplémentaires (notamment pour les dossiers réseau et les drives réseau mappés).

**Outils de parsing :** **RegRipper** (Harlan Carvey) est l'outil classique d'extraction automatisée — il exécute des plugins prédéfinis sur chaque ruche et produit un rapport texte structuré. **Registry Explorer** (Eric Zimmerman) offre une interface graphique d'exploration interactive avec recherche, favoris, et export. **RECmd** (Eric Zimmerman, ligne de commande) permet l'exécution de batch files prédéfinies (comme `RECmd_Batch_MC.reb` qui extrait automatiquement tous les artefacts forensic connus de toutes les ruches collectées).

#### 12.2 Artefacts d'exécution de programmes

Ces artefacts répondent à la question centrale : quels programmes ont été exécutés sur cette machine, quand, et combien de fois ?

**Prefetch** (`C:\Windows\Prefetch\`) : Windows crée un fichier `.pf` pour chaque programme exécuté, contenant le nom de l'exécutable, les 8 dernières dates/heures d'exécution (Windows 10/11), le nombre total d'exécutions, et la liste des fichiers et répertoires chargés par le programme lors des dernières exécutions. Le Prefetch est l'artefact le plus direct et le plus fiable pour prouver l'exécution d'un programme — même si l'exécutable a été supprimé du disque, le fichier .pf persiste. Outil de parsing : **PECmd** (Eric Zimmerman) — `PECmd.exe -f "PSEXEC.EXE-AD70946C.pf" --csv output/`. Le résultat inclut le nombre d'exécutions et les 8 dernières dates.

> **Limite :** Le Prefetch est désactivé par défaut sur Windows Server (le service SysMain n'est pas démarré). Sur les serveurs, l'Amcache et le ShimCache sont les alternatives.

**Amcache** (`C:\Windows\appcompat\Programs\Amcache.hve`) : registre qui enregistre les programmes installés et exécutés avec leurs hashes SHA1 et leur chemin complet. L'Amcache est particulièrement précieux pour deux raisons : le hash SHA1 permet d'identifier formellement le binaire exécuté (vérification sur VirusTotal), et il fonctionne sur Windows Server (contrairement au Prefetch). Outil : **AmcacheParser** — `AmcacheParser.exe -f Amcache.hve --csv output/`.

**ShimCache / AppCompatCache** (stocké dans la ruche SYSTEM, clé `CurrentControlSet\Control\Session Manager\AppCompatCache`) : enregistre le chemin et le timestamp de modification de chaque programme exécuté (ou simplement parcouru dans l'explorateur sur certaines versions). Le ShimCache est persisté au shutdown — il reflète l'état au dernier redémarrage. Outil : **AppCompatCacheParser** — `AppCompatCacheParser.exe -f SYSTEM --csv output/`.

**BAM/DAM** (Background Activity Moderator / Desktop Activity Monitor, stockés dans la ruche SYSTEM, clés `ControlSet001\Services\bam\State\UserSettings\<SID>`) : enregistrent les programmes exécutés avec des timestamps UTC précis. Disponible sur Windows 10 1709+ et Server 2016+. Parsed par RegRipper ou RECmd.

**SRUM** (System Resource Usage Monitor, base SQLite `C:\Windows\System32\SRU\SRUDB.dat`) : enregistre la consommation de ressources (réseau, CPU, énergie) par processus et par utilisateur, sur 30 à 60 jours. Pour le forensic, la colonne de consommation réseau par processus est l'information la plus précieuse : elle révèle quel processus a transféré quel volume de données — excellent pour quantifier l'exfiltration même si le processus n'est plus actif. Outil : **SrumECmd** — `SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/`.

#### 12.3 Artefacts de persistance dans le registre

La persistance est le mécanisme par lequel l'attaquant s'assure que son malware survit au redémarrage de la machine. Les mécanismes basés sur le registre sont détaillés ici ; les mécanismes basés sur les services, les tâches planifiées, et d'autres vecteurs sont traités au Ch.25.

Les clés **Run/RunOnce** (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` et `HKLM\...`) lancent automatiquement un programme au login de l'utilisateur ou au démarrage de la machine. C'est le mécanisme de persistance le plus basique et le plus facilement détectable. Les clés **Winlogon** (`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, valeurs `Userinit` et `Shell`) sont détournées pour exécuter du code au login — plus subtil que Run. Les clés **Image File Execution Options** (IFEO, `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<exe>`, valeur `Debugger`) permettent de rediriger l'exécution d'un programme légitime vers un programme malveillant — très subtil.

La vérification croisée avec **Autoruns** (Sysinternals) ou Velociraptor (query `Autoruns`) est la méthode la plus fiable pour inventorier tous les points de persistance actifs sur une machine.

#### 12.4 Fil rouge — MUSIC BOX : les artefacts d'exécution

> **🔬 MUSIC BOX — Épisode 11**
>
> L'analyse des artefacts d'exécution de WKS-RD-047 avec les outils Eric Zimmerman révèle :
>
> **PECmd (Prefetch) :** `PSEXEC.EXE` — 3 exécutions, dernière le 7 mars 14h47 UTC. `RCLONE.EXE` — 12 exécutions (une par jour de J-12 à J-1), dernière le 6 mars 22h15 UTC. `CERTUTIL.EXE` — 2 exécutions à J-60 (le jour de l'infection initiale — certutil utilisé par la macro VBA pour télécharger le RAT). `MIMIKATZ.EXE` — 1 exécution à J-45 (credential dumping). Le Prefetch de `SVCHOST_7284.EXE` (le processus injecté) n'existe pas — c'est cohérent avec un process hollowing (le processus légitime svchost a été démarré normalement puis son code a été remplacé en mémoire).
>
> **AmcacheParser :** confirme les hashes SHA1 de `psexec.exe`, `rclone.exe`, et `mimikatz.exe`. Soumission sur VirusTotal : `mimikatz.exe` est identifié positivement. `rclone.exe` est le binaire officiel (non malveillant en soi — c'est un outil de synchronisation cloud légitime détourné).
>
> **SrumECmd :** `rclone.exe` a transféré 183 Go de données réseau en 12 jours. C'est la quantification de l'exfiltration, confirmant les 180 Go estimés via les logs proxy.

---

### Chapitre 13 — Windows forensics : activité utilisateur, navigateur et mouvement latéral

*Ce chapitre couvre ce que l'utilisateur (ou l'attaquant se faisant passer pour l'utilisateur) a fait sur la machine : quels fichiers ont été accédés, quels dossiers ont été navigués, quels sites ont été visités, et comment l'attaquant s'est déplacé vers d'autres machines.*

#### 13.1 Artefacts d'activité utilisateur

**ShellBags** (stockés dans NTUSER.DAT et UsrClass.dat) : enregistrent chaque dossier navigué dans l'explorateur Windows, avec les dates d'accès et les préférences d'affichage — même si le dossier a été supprimé depuis, la trace persiste dans les ShellBags. Pour le forensic, ils révèlent les répertoires explorés par l'attaquant (partages réseau, dossiers sensibles, lecteurs USB). Outil : **SBECmd** — `SBECmd.exe -d "C:\Users\JMallet" --csv output/`.

**LNK files** (raccourcis, `.lnk`, dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\`) : créés automatiquement quand un fichier est ouvert. Chaque fichier .lnk contient le chemin complet du fichier cible (y compris les chemins réseau UNC — `\\SRV-RD-01\projets\`), le volume d'origine (nom du volume, numéro de série — identifie les clés USB), les timestamps MAC du fichier cible, et la taille du fichier. Outil : **LECmd** — `LECmd.exe -d "C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent" --csv output/`.

**Jump Lists** (dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\`) : listes de fichiers récemment ouverts par application. Chaque application a son propre fichier Jump List, identifié par un AppID. Les Jump Lists contiennent les mêmes informations que les LNK files mais organisées par application. Outil : **JLECmd** — `JLECmd.exe -d "AutomaticDestinations" --csv output/`.

**UserAssist** (dans NTUSER.DAT, clé `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`) : enregistre les programmes exécutés via l'interface graphique (GUI) avec un compteur d'exécutions et le dernier timestamp. Les données sont encodées en ROT13 (obfuscation triviale, pas du chiffrement).

#### 13.2 Browser forensics

Les navigateurs web sont une source d'évidence massive et souvent sous-exploitée. Chrome, Firefox, et Edge stockent leurs données dans des bases SQLite accessibles dans le profil utilisateur.

**Chrome** (`C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\`) : `History` (historique de navigation et de téléchargements), `Cookies` (cookies de session — peuvent révéler des accès à des services cloud avec credentials volées), `Login Data` (credentials enregistrés — chiffrés avec DPAPI), `Web Data` (formulaires auto-remplies), `Preferences` (extensions installées — certaines extensions peuvent être malveillantes), `Favicons` (icônes des sites visités — preuve de visite même si l'historique a été effacé). Outil de parsing : **Hindsight** (open source) — `hindsight.py -i "C:\Users\JMallet\AppData\Local\Google\Chrome\User Data\Default" -o output/`.

**Firefox** (`C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\`) : `places.sqlite` (historique et favoris), `cookies.sqlite`, `formhistory.sqlite`, `logins.json` + `key4.db` (credentials). **Edge** (Chromium-based) utilise la même structure que Chrome mais dans un chemin différent.

L'historique de navigation peut révéler la préparation de l'attaque (l'attaquant a recherché des informations sur l'infrastructure de NovaPharma depuis le poste compromis), l'accès à des services de transfert de fichiers (mega.nz, transfer.sh), ou la consultation de forums underground.

#### 13.3 Artefacts de mouvement latéral

Le mouvement latéral est la progression de l'attaquant d'un système à un autre au sein du réseau. Chaque technique de mouvement latéral laisse des artefacts spécifiques — tant sur la machine source que sur la machine destination.

**PsExec** : sur la machine destination, PsExec crée un service temporaire `PSEXESVC` (visible dans les Event Logs : Event ID 7045 — installation de service). Le binaire `PSEXESVC.exe` est copié dans `C:\Windows\` (visible dans la MFT et potentiellement dans le Prefetch). L'Event Log Security montre une authentification réseau (4624 type 3) suivie d'un accès au partage ADMIN$ (Event ID 5140). Sur la machine source, le Prefetch de `PSEXEC.EXE` confirme l'exécution avec le timestamp.

**RDP** : les connexions RDP laissent des traces riches. Sur la machine destination : Event IDs 21/22/25 dans le canal `TerminalServices-RemoteConnectionManager` (connexion établie, réussie, reconnexion), Event ID 4624 type 10 (logon RDP) dans Security, et le **RDP Bitmap Cache** (`C:\Users\<user>\AppData\Local\Microsoft\Terminal Server Client\Cache\`) qui contient des fragments visuels de la session RDP — potentiellement des captures d'écran de ce que l'attaquant a vu. L'outil **bmc-tools** ou **rdpieces** peut reconstituer des images à partir du cache bitmap. Sur la machine source : la clé registre `HKCU\Software\Microsoft\Terminal Server Client\Default` et les fichiers `.rdp` dans le profil listent les connexions RDP récentes.

**WMI** (Windows Management Instrumentation) : l'exécution de commandes à distance via WMI est plus discrète que PsExec. Les traces : Event ID 4688 (création de processus) avec `wmiprvse.exe` comme parent sur la machine destination, et les logs WMI dans `Microsoft-Windows-WMI-Activity/Operational`.

**SMB / Accès aux partages réseau** : Event IDs 5140 (accès à un partage) et 5145 (vérification d'accès à un fichier/dossier partagé — plus granulaire, nécessite l'activation de l'audit des partages). Ces événements sont essentiels pour tracer quels fichiers l'attaquant a accédé sur les serveurs de fichiers.

**Artefacts USB** : les connexions USB sont tracées dans le registre (SYSTEM\CurrentControlSet\Enum\USBSTOR), dans les logs PnP (Event ID 20001, 20003), et dans `C:\Windows\inf\setupapi.dev.log`. Ces artefacts identifient le type de périphérique, son numéro de série, les dates de première et dernière connexion — essentiels dans les investigations d'insider threat.

#### 13.4 Fil rouge — MUSIC BOX : mouvement latéral détecté

> **🔬 MUSIC BOX — Épisode 12**
>
> L'analyse des artefacts de mouvement latéral de WKS-RD-047 révèle les connexions vers d'autres machines.
>
> **LNK files (LECmd) :** 15 fichiers .lnk pointent vers des chemins réseau `\\SRV-RD-01\projets\molecule-np427\` — l'attaquant a navigué dans les fichiers de recherche depuis le poste compromis.
>
> **RDP (registre + Event Logs) :** le registre montre une connexion RDP récente vers `SRV-RD-01` (le serveur Linux — l'accès SSH est possible via RDP Gateway ? Non — investigation complémentaire : l'attaquant a utilisé PuTTY, dont le Prefetch confirme l'exécution). Les fichiers `.rdp` du profil de l'attaquant montrent aussi une connexion vers `DC01` (le contrôleur de domaine).
>
> **PsExec :** le Prefetch confirme l'exécution de PsExec sur WKS-RD-047. Les Event Logs de DC01 (collectés au Ch.8) montrent la création du service PSEXESVC (Event ID 7045) à J-14 — c'est le moment où l'attaquant a utilisé PsExec pour exécuter le DCSync sur DC01.

---

### Chapitre 14 — Windows forensics : Event Logs et journaux d'audit

*Ce chapitre est le référentiel de l'interprétation des Event Logs Windows pour le forensic. Il ne répète pas les artefacts de registre (Ch.12) ni les artefacts d'activité utilisateur (Ch.13) — il se concentre sur ce que les journaux d'audit racontent, comment les lire, et comment les corréler.*

#### 14.1 Architecture des Event Logs Windows

Les Event Logs Windows sont stockés au format `.evtx` (XML binaire) dans `C:\Windows\System32\winevt\Logs\`. Chaque fichier correspond à un canal (channel) : `Security.evtx` (authentification, audit de sécurité — la source la plus importante pour le forensic), `System.evtx` (services, pilotes, erreurs système), `Application.evtx` (événements applicatifs), et de nombreux canaux spécialisés (`Microsoft-Windows-PowerShell/Operational`, `Microsoft-Windows-Sysmon/Operational`, `Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational`, etc.).

La **rotation** des Event Logs est configurée par taille maximale (par défaut : 20 Mo pour Security, ce qui est insuffisant pour une investigation — les événements les plus anciens sont écrasés quand le fichier est plein). Sur un DC actif avec la configuration par défaut, le Security log peut tourner en quelques heures. La recommandation forensic readiness (Ch.27) est d'augmenter la taille à 1 Go minimum et de centraliser les logs dans un SIEM.

La **collecte** et le **parsing** avec EvtxECmd (Eric Zimmerman) sont la méthode de référence : `EvtxECmd.exe -f Security.evtx --csv output/ --csvf security_parsed.csv`. Le résultat est un CSV structuré analysable dans Timeline Explorer, avec chaque Event ID parsé en colonnes exploitables.

Des outils complémentaires accélèrent l'analyse. **Chainsaw** (WithSecure, open source) applique des règles Sigma sur les Event Logs pour détecter automatiquement les patterns d'attaque. **Hayabusa** (open source, japonais) offre une détection similaire basée sur Sigma avec un focus sur la vitesse. **LogParser** (Microsoft, gratuit) permet des requêtes SQL sur les fichiers evtx.

#### 14.2 Event IDs critiques pour le forensic — interprétation détaillée

Plutôt qu'une simple liste, chaque Event ID est expliqué avec son contexte, son contenu, son interprétation forensic, et ses faux positifs.

**4624 (Successful Logon) :** enregistre chaque authentification réussie avec le type de logon. Les types pertinents pour le forensic : Type 2 (Interactive — login physique ou RDP via console), Type 3 (Network — accès à un partage réseau, authentification WMI ou PsExec), Type 7 (Unlock — déverrouillage de session), Type 10 (RemoteInteractive — RDP). L'Event 4624 contient le nom du compte, le domaine, l'adresse IP source (pour les logons réseau), et le processus d'authentification (NTLM vs Kerberos). Un 4624 Type 3 depuis une IP inconnue avec un compte de service à 3h du matin est un indicateur de mouvement latéral.

**4625 (Failed Logon) :** enregistre les échecs d'authentification. Un volume élevé de 4625 avec des comptes variés depuis une même source indique un password spraying ou un brute force. Le sous-status code précise la raison de l'échec (0xC0000064 = compte inexistant, 0xC000006A = mot de passe incorrect, 0xC0000234 = compte verrouillé).

**4648 (Logon with Explicit Credentials) :** enregistre quand un processus s'authentifie avec des credentials différentes de celles de la session en cours (runas, PsExec avec `-u`, ou pass-the-hash). C'est un indicateur fort de mouvement latéral — l'attaquant utilise des credentials volées pour accéder à d'autres machines.

**4672 (Special Privileges Assigned) :** enregistre l'attribution de privilèges administratifs lors d'un logon. Un 4672 pour un compte utilisateur standard est suspect (l'utilisateur a obtenu des droits qu'il ne devrait pas avoir).

**4688 (Process Creation) :** enregistre la création d'un processus avec le nom de l'exécutable et, si la journalisation de la ligne de commande est activée (GPO `Process Creation → Include command line`), la ligne de commande complète. C'est l'Event ID le plus riche pour le forensic d'exécution — la ligne de commande révèle exactement ce que l'attaquant a tapé. Sans l'activation de cette GPO, le 4688 est beaucoup moins informatif.

**7045 (Service Installed) :** enregistre l'installation d'un nouveau service. PsExec crée un service PSEXESVC. Les malwares installent souvent des services pour la persistence. Un 7045 avec un nom de service inhabituel, un chemin d'exécutable dans un répertoire temporaire, ou un service Type 0x10 (own process) mérite investigation.

**4698 (Scheduled Task Created) :** enregistre la création d'une tâche planifiée. Les tâches planifiées sont un mécanisme de persistence courant. Le contenu de l'événement inclut le XML de la tâche — action exécutée, déclencheur, compte utilisé.

**4769 (Kerberos Service Ticket Requested) :** avec encryption type 0x17 (RC4), c'est la signature du Kerberoasting. Un volume élevé de 4769 avec encryption RC4 depuis une seule machine indique que l'attaquant demande des TGS pour craquer les mots de passe des comptes de service. Détail au Ch.20 (AD forensics).

**1102 (Security Log Cleared) :** enregistre l'effacement du Security Event Log — ironiquement, l'acte de nettoyage produit lui-même un événement. Un 1102 est un indicateur d'anti-forensics. Si les logs sont centralisés dans un SIEM, les événements antérieurs au clearing sont préservés.

**Sysmon Event IDs** (si Sysmon est déployé) : Event 1 (Process Creation — plus détaillé que 4688, avec hash du binaire, ligne de commande complète, processus parent), Event 3 (Network Connection — quel processus se connecte à quelle IP), Event 7 (Image Loaded — DLL chargées par un processus), Event 10 (Process Access — accès à LSASS), Event 11 (File Create — fichiers créés), Event 22 (DNS Query — résolutions DNS par processus). Sysmon transforme la visibilité forensic d'une machine Windows — son déploiement est la recommandation de forensic readiness la plus impactante.

#### 14.3 Corrélation des Event Logs entre machines

Reconstituer le mouvement latéral exige de corréler les Event Logs de plusieurs machines. Sur la machine source : 4648 (logon avec credentials explicites), Prefetch de l'outil de latéralisation (PsExec, wmic). Sur la machine destination : 4624 (logon réussi, type 3 ou 10), 7045 (service installé par PsExec), 4688 (processus créé). La corrélation repose sur les timestamps (les événements doivent être proches dans le temps), les comptes (le même compte apparaît sur les deux machines), et les IP (l'IP source du 4624 sur la destination correspond à l'IP de la machine source).

#### 14.4 Fil rouge — MUSIC BOX : les Event Logs racontent l'histoire

> **🔬 MUSIC BOX — Épisode 13**
>
> L'analyse des Event Logs de DC01 (parsés avec EvtxECmd + Chainsaw) révèle la séquence de la compromission AD.
>
> J-45 : série de 4769 (Kerberos TGS) avec encryption type RC4 depuis WKS-RD-047 pour 12 comptes de service — **Kerberoasting confirmé**. Le compte `svc-backup` avait un SPN et un mot de passe faible (`NovaPharma2024!`, cracké en 2h).
>
> J-30 : 4624 type 3 depuis WKS-RD-047 avec le compte `svc-backup` (domain admin) — première utilisation du compte compromis pour le mouvement latéral.
>
> J-14 : 4662 avec les GUID de réplication (`1131f6ad-...`) depuis WKS-RD-047 — **DCSync confirmé**. Tous les hashes NTLM sont compromis.
>
> J-1, 03h42 : **1102 — Security Log cleared** sur DC01. L'attaquant a effacé le Security Log. Mais les événements antérieurs au clearing sont préservés dans le SIEM Splunk de NovaPharma — l'anti-forensics a échoué grâce à la centralisation des logs.

---

### Chapitre 15 — Linux forensics

#### 15.1 Les particularités du forensic Linux

Linux est omniprésent en serveur (web, base de données, stockage, cloud) mais ses artefacts forensic sont moins riches et moins standardisés que ceux de Windows. Il n'y a pas d'équivalent du Prefetch, de l'Amcache, ou des ShellBags. L'investigation Linux repose davantage sur les logs système, les historiques de commandes, les tâches planifiées, et l'analyse du système de fichiers ext4.

#### 15.2 Artefacts système Linux

**auth.log / secure** (`/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` sur RHEL/CentOS) : chaque authentification (login, sudo, SSH, su) est enregistrée. Les connexions SSH montrent l'IP source, le compte utilisé, et le résultat (accepté/refusé). Les commandes sudo montrent quelle commande a été exécutée par quel utilisateur.

**wtmp / btmp / lastlog** : fichiers binaires enregistrant les sessions utilisateur. `wtmp` contient les connexions réussies (lisible avec la commande `last`). `btmp` contient les tentatives échouées (lisible avec `lastb`). `lastlog` contient la dernière connexion de chaque utilisateur.

**bash_history / zsh_history** (`~/.bash_history`, `~/.zsh_history`) : historique des commandes exécutées. C'est souvent la source la plus directement exploitable — l'attaquant peut y avoir laissé ses commandes de reconnaissance, de mouvement latéral, et d'exfiltration. Le piège : l'attaquant supprime souvent son historique (`history -c`, `rm ~/.bash_history`), mais des traces peuvent persister en mémoire (dans le dump RAM), dans le swap, ou dans les secteurs non alloués du disque (le fichier supprimé peut être récupéré si le disque est un HDD).

**journald** (systemd) : le journal système de systemd, exploitable avec `journalctl`. Plus structuré que syslog, il inclut des métadonnées riches (PID, UID, unité systemd). Exportable en JSON pour l'analyse : `journalctl --since "2026-01-01" -o json > journal.json`.

**crontab et systemd timers** : les tâches planifiées sont un mécanisme de persistance courant sous Linux. Les crontab utilisateur (`crontab -l -u <user>`) et système (`/etc/crontab`, `/etc/cron.d/`) doivent être vérifiés. Les systemd timers (`.timer` + `.service` dans `/etc/systemd/system/`) sont une alternative plus moderne.

#### 15.3 Investigation serveur web et conteneurs

Les **logs Apache/Nginx** (`/var/log/apache2/access.log`, `/var/log/nginx/access.log`) sont essentiels pour l'investigation de compromission de serveur web. La détection de webshells (fichiers PHP/ASP déposés par l'attaquant pour maintenir un accès distant) passe par l'analyse des requêtes POST vers des fichiers inhabituels, l'identification de user-agents suspects, et la recherche de fichiers récemment créés dans les répertoires web.

Les **conteneurs Docker** posent des défis spécifiques : l'éphémérité des conteneurs (un conteneur détruit emporte ses données), la superposition des layers (le filesystem du conteneur est une superposition de couches en lecture seule + une couche en lecture/écriture), et l'absence de logs centralisés par défaut. L'investigation de conteneurs passe par l'examen des layers (`docker history`, `docker inspect`), des logs (`docker logs`), et des volumes montés. Sans logs externalisés vers un SIEM ou un système de log centralisé, le forensic de conteneurs est souvent impossible.

#### 15.4 Outils Linux forensics

**The Sleuth Kit / Autopsy** supporte ext4. **extundelete** et **ext4magic** permettent la récupération de fichiers supprimés sur ext4 (avec des limitations — ext4 réinitialise les pointeurs d'inode). **Plaso** (log2timeline) supporte les artefacts Linux (syslog, wtmp, bash_history, etc.). Les outils de la suite Eric Zimmerman ne sont pas disponibles nativement sous Linux (ils sont conçus pour les artefacts Windows), mais ils fonctionnent via Wine ou sur une station Windows.

#### 15.5 Fil rouge — MUSIC BOX : le serveur R&D Linux

> **🔬 MUSIC BOX — Épisode 14**
>
> L'investigation de SRV-RD-01 (Ubuntu 22.04, serveur de données R&D) révèle :
>
> **auth.log :** connexion SSH réussie depuis WKS-RD-047 (IP interne 10.xx.xx.47) avec le compte `svc-backup` à J-28, J-21, J-14, J-7, et J-1. Le compte `svc-backup` avait un authorized_key SSH ajouté par l'attaquant à J-30 — c'est le mécanisme de persistance sur le serveur Linux.
>
> **bash_history :** l'attaquant a exécuté `find /opt/research/molecule-np427 -name "*.xlsx" -o -name "*.pdf" -o -name "*.docx"` (reconnaissance des fichiers de recherche), puis `tar czf /tmp/research_backup.tar.gz /opt/research/molecule-np427/` (staging des données pour exfiltration), puis `rm -f /tmp/research_backup.tar.gz` (nettoyage après exfiltration — mais le fichier tar apparaît dans les secteurs non alloués du disque, récupérable par carving).
>
> **authorized_keys :** une clé SSH non autorisée a été ajoutée dans `/home/svc-backup/.ssh/authorized_keys` à J-30 — la clé publique est différente de celles des administrateurs légitimes. C'est le mécanisme de persistance.

---

### Chapitre 16 — macOS forensics

#### 16.1 Artefacts spécifiques macOS

macOS possède des artefacts forensic riches et spécifiques qui n'existent pas sur Windows ni Linux.

Le **Unified Logging** (introduit en macOS 10.12) est le système de journalisation le plus riche des OS modernes — il capture des milliards d'événements par jour (processus, réseau, système, applications). L'outil `log show` permet d'interroger les logs avec des filtres : `log show --predicate 'processImagePath contains "ssh"' --start "2026-01-01" --end "2026-03-08"`. L'outil `log collect` exporte les logs pour analyse offline.

Les **FSEvents** (File System Events, stockés dans `.fseventsd/` à la racine de chaque volume) enregistrent toutes les modifications du système de fichiers avec un identifiant d'événement séquentiel. Ils persistent même après suppression des fichiers — c'est l'équivalent fonctionnel du $UsnJrnl de Windows.

**KnowledgeC.db** (`~/Library/Application Support/Knowledge/KnowledgeC.db`) est une base SQLite qui enregistre l'activité utilisateur : applications ouvertes avec durée d'utilisation, activité réseau, période d'éveil de la machine, et interactions utilisateur. C'est une source forensic extrêmement riche, spécifique à macOS.

Les **Spotlight metadata** (index `.Spotlight-V100/`) contiennent les métadonnées de tous les fichiers indexés par Spotlight — même si les fichiers sont supprimés, les métadonnées peuvent persister dans l'index.

**TCC.db** (`~/Library/Application Support/com.apple.TCC/TCC.db`) enregistre les permissions d'accès aux ressources sensibles (caméra, microphone, fichiers, accessibilité). Un malware qui a obtenu l'accès à l'accessibilité ou au Full Disk Access sera visible dans TCC.db.

**LaunchAgents / LaunchDaemons** (`~/Library/LaunchAgents/`, `/Library/LaunchAgents/`, `/Library/LaunchDaemons/`) sont les mécanismes de persistance macOS — des fichiers plist qui définissent des programmes à exécuter automatiquement.

Outils macOS forensics : **mac_apt** (macOS Artifact Parsing Tool — open source, parse les artefacts spécifiques macOS), **APOLLO** (Apple Pattern of Life Lazy Output — parse KnowledgeC.db et d'autres bases de données d'activité), et **Unified Log Parser**.

---

### Chapitre 17 — Memory forensics

#### 17.1 Workflows d'analyse concrète avec Volatility 3

Au-delà de la liste des plugins (présentée au Ch.6 pour le dump et dans le cours original), ce chapitre se concentre sur les workflows d'analyse concrets — comment l'analyste utilise les plugins en séquence pour répondre aux questions investigatives.

**Workflow 1 — Triage initial (5 minutes) :** identifier rapidement si la machine est compromise. (1) `windows.pslist` / `windows.pstree` → examiner l'arbre des processus : les processus avec des parents anormaux (svchost.exe avec explorer.exe comme parent, cmd.exe avec iexplore.exe comme parent) sont suspects. (2) `windows.netscan` → identifier les connexions réseau actives vers des destinations suspectes (IP externes non connues, ports inhabituels). (3) `windows.cmdline` → examiner les lignes de commande des processus suspects. En 5 minutes, l'analyste sait si la machine est compromise et a identifié les premiers IoC (IP C2, processus malveillant).

**Workflow 2 — Investigation de process injection (30 minutes) :** quand un processus suspect est identifié. (1) `windows.malfind` → détecter les régions mémoire avec des permissions suspectes (PAGE_EXECUTE_READWRITE — RWX — est rare pour du code légitime et typique d'injection). Attention aux faux positifs : certains programmes légitimes (JIT compilers comme .NET CLR, navigateurs web) utilisent RWX légitimement. L'analyse doit être contextuelle. (2) `windows.dlllist --pid <PID>` → lister les DLL chargées par le processus suspect — identifier les DLL inhabituelles ou non signées. (3) `windows.handles --pid <PID>` → examiner les handles ouverts (fichiers, clés de registre, mutex — un mutex nommé peut identifier une famille de malware connue). (4) `windows.procdump --pid <PID> --dump-dir output/` → extraire le binaire du processus pour analyse malware.

**Workflow 3 — Extraction de credentials (15 minutes) :** (1) `windows.hashdump` → extraire les hashes NTLM des comptes locaux depuis SAM en mémoire. (2) `windows.lsadump` → extraire les secrets LSA (mots de passe de services, clés DPAPI). (3) Recherche de strings caractéristiques de mimikatz (`sekurlsa::logonPasswords`, `sekurlsa::wdigest`) dans le dump pour déterminer si l'attaquant a utilisé mimikatz. (4) Recherche de credentials en clair dans le processus lsass avec `windows.memmap --pid <lsass_pid> --dump-dir output/` puis strings et grep.

**Workflow 4 — Analyse de rootkit (avancé) :** `windows.modules` → lister les modules kernel chargés. `windows.ssdt` → vérifier la System Service Dispatch Table pour détecter les hooks. `windows.callbacks` → lister les callbacks enregistrés (un rootkit enregistre des callbacks pour intercepter les opérations système).

#### 17.2 Pagefile et hiberfil comme mémoire fossile

Quand le dump RAM n'a pas été fait à temps (la machine a été redémarrée avant l'intervention forensic), le **pagefile.sys** et le **hiberfil.sys** sont des sources de mémoire « fossile ». Le pagefile contient des pages mémoire qui ont été déplacées vers le disque — elles peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le hiberfil est un dump mémoire compressé créé lors de l'hibernation — analysable avec Volatility.

Extraction des strings du pagefile : `strings -el pagefile.sys > pagefile_strings_unicode.txt` puis recherche de patterns (URLs, IP, chemins de fichiers suspects, noms de domaine). La recherche dans le pagefile est moins structurée que l'analyse d'un dump RAM complet (pas de structure de processus), mais elle peut révéler des données critiques quand le dump RAM est indisponible.

#### 17.3 YARA rules sur les dumps mémoire

Les règles YARA permettent de scanner le dump mémoire pour détecter des patterns caractéristiques de familles de malware connues. Le plugin `windows.yarascan` de Volatility exécute des règles YARA sur l'espace mémoire de chaque processus. Les sources de règles YARA : le repository `awesome-yara` sur GitHub, les règles publiées par les éditeurs CTI (Mandiant, CrowdStrike, ESET), et les règles custom créées à partir des IoC spécifiques à l'investigation.

#### 17.4 Fil rouge — MUSIC BOX : la mémoire raconte tout

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

### Chapitre 18 — Malware forensics

#### 18.1 Positionnement

Le malware forensics dans le contexte de ce cours n'est pas du reverse engineering complet (désassemblage, décompilation, analyse du code assembleur instruction par instruction). C'est de l'analyse comportementale orientée compréhension de l'intrusion : que fait le malware (fonctionnalités), avec qui communique-t-il (C2), quelles données a-t-il volées (exfiltration), comment survit-il au reboot (persistance), et comment le détecter sur d'autres machines (IoC).

#### 18.2 Analyse statique de premier niveau

L'analyse statique examine le malware sans l'exécuter. Le **hashing** (MD5, SHA-256) permet la soumission à VirusTotal, MalwareBazaar, ou Hybrid Analysis pour vérifier si le malware est connu. L'extraction de **strings** (`strings -el malware.exe > strings_output.txt`) révèle les chaînes de caractères embarquées : URLs de C2, chemins de fichiers, clés de registre, messages d'erreur, et parfois des identifiants de campagne. L'analyse de la structure **PE** (Portable Executable, format Windows) montre les imports (quelles API Windows le malware utilise — `VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread` sont des indicateurs d'injection de processus), les sections (une section `.text` avec une entropie élevée > 7.0 suggère du packing ou du chiffrement), et les métadonnées (timestamp de compilation, éditeur de liens — le timestamp peut être falsifié mais fournit un indice). Le matching **YARA** compare l'échantillon à des règles connues pour identifier la famille.

L'analyse de **documents piégés** est une sous-spécialité de l'analyse statique. Les macros VBA dans les documents Office (Word, Excel) sont extraites et analysées avec **olevba** (oletools) sans exécuter le document. Les PDF malveillants sont analysés avec **pdf-parser** et **peepdf** (recherche de JavaScript, d'objets Flash, de liens vers des payloads). Les objets OLE embarqués dans les documents (exécutables déguisés en icônes de document) sont extraits avec **oletools**.

#### 18.3 Analyse dynamique en sandbox

L'analyse dynamique exécute le malware dans un environnement contrôlé pour observer son comportement réel. Les sandboxes en ligne (**ANY.RUN** avec interface interactive, **Joe Sandbox**, **CAPE/Cuckoo**) capturent les modifications système (fichiers créés, clés de registre modifiées, processus lancés, services installés), le trafic réseau (connexions C2, requêtes DNS, téléchargements), et les captures d'écran.

Les résultats de la sandbox sont interprétés dans le contexte de l'investigation : le C2 identifié (IP, domaine, port, protocole) est corrélé avec les logs réseau de l'organisation ; les artefacts de persistance identifiés (clé de registre, service, scheduled task) sont recherchés sur les autres machines du parc ; les IoC extraits (hash, domaines, mutex, user-agent) sont injectés dans le SIEM et l'EDR pour détecter d'autres machines compromises.

#### 18.4 Types de malware et implications forensic

Chaque type de malware pose des questions forensic différentes. Un **RAT** (Remote Access Trojan) fournit un accès distant persistant — la question est : depuis combien de temps est-il installé et quels accès ont été obtenus (keylogging, screenshot, file listing, credential dumping). Un **infostealer** (Lumma, RedLine, Vidar) exfiltre automatiquement des données spécifiques — la question est : quelles données ont été volées (credentials navigateur, cookies de session, wallets crypto, données de formulaires). Un **ransomware** chiffre les fichiers — la question est : quel périmètre a été chiffré, quelle clé a été utilisée (récupérable ?), et y a-t-il eu exfiltration avant chiffrement (double extorsion). Un **fileless malware** n'existe qu'en mémoire — la question est : le dump RAM a-t-il été fait ? (si non, le malware est potentiellement invisible au disk forensics).

#### 18.5 Extraction d'IoC et partage

Les IoC (Indicators of Compromise) sont les traces observables laissées par le malware, utilisables pour la détection sur d'autres machines et pour le partage avec la communauté. Ils incluent les hashes (SHA-256 du binaire), les domaines et IP C2, les mutex (verrous nommés — un mutex spécifique identifie souvent une famille de malware), les clés de registre modifiées, les fichiers créés (chemins, noms), les patterns réseau (beaconing interval, user-agent spécifique, JA3 hash), et les certificats TLS utilisés par le C2.

Les IoC sont partagés au format STIX/TAXII ou OpenIOC et injectés dans le SIEM et l'EDR pour scanner l'ensemble du parc. Le mapping sur la matrice MITRE ATT&CK (T1566.001 Spearphishing Attachment, T1059.001 PowerShell, T1055.012 Process Hollowing, etc.) structure les résultats pour le rapport et oriente les mesures défensives.

#### 18.6 Fil rouge — MUSIC BOX : le RAT custom

> **🔬 MUSIC BOX — Épisode 16**
>
> Le payload extrait du dump mémoire (procdump de PID 7284) est analysé.
>
> **Statique :** SHA-256 inconnu de VirusTotal — malware custom. `strings` : URL `https://103.xx.xx.xx/api/beacon`, user-agent `Mozilla/5.0 NovaPharma` (personnalisé), chemin `C:\Users\JMallet\AppData\Local\Temp\svchost_update.dat`. Structure PE : section .text avec entropie 7.2 (packé). YARA : correspondance partielle avec les signatures du groupe APT connu pour cibler l'industrie pharmaceutique européenne (cluster d'activité « PharmaGhost » selon Mandiant).
>
> **Dynamique (ANY.RUN) :** RAT custom, beacon HTTPS toutes les 30 minutes (confirmé par les logs proxy), capacités identifiées : file listing (`dir` recursif), file download, screenshot (toutes les 5 minutes), keylogger (capture des frappes clavier), credential dump (appel à `sekurlsa::logonPasswords` de mimikatz).
>
> **IoC extraits :** IP C2 `103.xx.xx.xx`, user-agent `Mozilla/5.0 NovaPharma`, mutex `Global\NP_RAT_2024`, fichier `svchost_update.dat`, clé registre `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\WindowsUpdate`. IoC injectés dans le SIEM et l'EDR → scan des 800 postes du parc. Résultat : aucune autre machine infectée.

---
