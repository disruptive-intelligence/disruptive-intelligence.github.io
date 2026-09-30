---
title: 'Chapitre 12 — Windows forensics : registre et artefacts d''exécution'
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

*Ce chapitre couvre ce que la machine « sait » sur les programmes qui ont été exécutés. Le Ch.13 couvrira l'activité utilisateur et le mouvement latéral. Le Ch.14 couvrira les Event Logs. Cette séparation évite les redites : le Prefetch apparaît ici (artefact d'exécution), les traces RDP apparaissent au Ch.13 (mouvement latéral), et les Event IDs apparaissent au Ch.14 (journaux d'audit).*

## 12.1 Le registre Windows comme mine forensic

Le registre Windows est une base de données hiérarchique qui stocke la configuration du système et des applications. Pour le forensic, c'est la source la plus riche après les Event Logs.

Les **fichiers de ruche** (hive files) sont les fichiers physiques qui contiennent le registre. Leur localisation est fixe. **SAM** (`C:\Windows\System32\config\SAM`) contient les comptes locaux et leurs hashes NTLM — exploitable avec `secretsdump.py` ou RegRipper pour identifier les comptes créés par l'attaquant. **SYSTEM** (`C:\Windows\System32\config\SYSTEM`) contient la configuration matérielle, le nom de l'ordinateur, le fuseau horaire (critique pour la corrélation), les informations de boot, et la clé de déchiffrement (BootKey) nécessaire pour décrypter les hashes SAM. **SOFTWARE** (`C:\Windows\System32\config\SOFTWARE`) contient les logiciels installés (clé `Microsoft\Windows\CurrentVersion\Uninstall`), les profils réseau (clé `Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` — historique des réseaux WiFi et Ethernet avec dates de connexion), et les services (clé `CurrentControlSet\Services`). **NTUSER.DAT** (`C:\Users\<username>\NTUSER.DAT`) est la ruche spécifique à chaque utilisateur : elle contient les MRU (Most Recently Used — derniers fichiers ouverts), les ShellBags (navigation dans l'explorateur), les clés Run/RunOnce (persistence au login), les UserAssist (programmes exécutés via le GUI avec nombre d'exécutions et timestamps), et les Typed Paths (chemins saisis manuellement dans l'explorateur — y compris les chemins réseau UNC). **UsrClass.dat** (`C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat`) contient les associations de fichiers et les ShellBags supplémentaires (notamment pour les dossiers réseau et les drives réseau mappés).

**Outils de parsing :** **RegRipper** (Harlan Carvey) est l'outil classique d'extraction automatisée — il exécute des plugins prédéfinis sur chaque ruche et produit un rapport texte structuré. **Registry Explorer** (Eric Zimmerman) offre une interface graphique d'exploration interactive avec recherche, favoris, et export. **RECmd** (Eric Zimmerman, ligne de commande) permet l'exécution de batch files prédéfinies (comme `RECmd_Batch_MC.reb` qui extrait automatiquement tous les artefacts forensic connus de toutes les ruches collectées).

## 12.2 Artefacts d'exécution de programmes

Ces artefacts répondent à la question centrale : quels programmes ont été exécutés sur cette machine, quand, et combien de fois ?

**Prefetch** (`C:\Windows\Prefetch\`) : Windows crée un fichier `.pf` pour chaque programme exécuté, contenant le nom de l'exécutable, les 8 dernières dates/heures d'exécution (Windows 10/11), le nombre total d'exécutions, et la liste des fichiers et répertoires chargés par le programme lors des dernières exécutions. Le Prefetch est l'artefact le plus direct et le plus fiable pour prouver l'exécution d'un programme — même si l'exécutable a été supprimé du disque, le fichier .pf persiste. Outil de parsing : **PECmd** (Eric Zimmerman) — `PECmd.exe -f "PSEXEC.EXE-AD70946C.pf" --csv output/`. Le résultat inclut le nombre d'exécutions et les 8 dernières dates.

> **Limite :** Le Prefetch est désactivé par défaut sur Windows Server (le service SysMain n'est pas démarré). Sur les serveurs, l'Amcache et le ShimCache sont les alternatives.

**Amcache** (`C:\Windows\appcompat\Programs\Amcache.hve`) : registre qui enregistre les programmes installés et exécutés avec leurs hashes SHA1 et leur chemin complet. L'Amcache est particulièrement précieux pour deux raisons : le hash SHA1 permet d'identifier formellement le binaire exécuté (vérification sur VirusTotal), et il fonctionne sur Windows Server (contrairement au Prefetch). Outil : **AmcacheParser** — `AmcacheParser.exe -f Amcache.hve --csv output/`.

**ShimCache / AppCompatCache** (stocké dans la ruche SYSTEM, clé `CurrentControlSet\Control\Session Manager\AppCompatCache`) : enregistre le chemin et le timestamp de modification de chaque programme exécuté (ou simplement parcouru dans l'explorateur sur certaines versions). Le ShimCache est persisté au shutdown — il reflète l'état au dernier redémarrage. Outil : **AppCompatCacheParser** — `AppCompatCacheParser.exe -f SYSTEM --csv output/`.

**BAM/DAM** (Background Activity Moderator / Desktop Activity Monitor, stockés dans la ruche SYSTEM, clés `ControlSet001\Services\bam\State\UserSettings\<SID>`) : enregistrent les programmes exécutés avec des timestamps UTC précis. Disponible sur Windows 10 1709+ et Server 2016+. Parsed par RegRipper ou RECmd.

**SRUM** (System Resource Usage Monitor, base SQLite `C:\Windows\System32\SRU\SRUDB.dat`) : enregistre la consommation de ressources (réseau, CPU, énergie) par processus et par utilisateur, sur 30 à 60 jours. Pour le forensic, la colonne de consommation réseau par processus est l'information la plus précieuse : elle révèle quel processus a transféré quel volume de données — excellent pour quantifier l'exfiltration même si le processus n'est plus actif. Outil : **SrumECmd** — `SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/`.

## 12.3 Artefacts de persistance dans le registre

La persistance est le mécanisme par lequel l'attaquant s'assure que son malware survit au redémarrage de la machine. Les mécanismes basés sur le registre sont détaillés ici ; les mécanismes basés sur les services, les tâches planifiées, et d'autres vecteurs sont traités au Ch.25.

Les clés **Run/RunOnce** (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` et `HKLM\...`) lancent automatiquement un programme au login de l'utilisateur ou au démarrage de la machine. C'est le mécanisme de persistance le plus basique et le plus facilement détectable. Les clés **Winlogon** (`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, valeurs `Userinit` et `Shell`) sont détournées pour exécuter du code au login — plus subtil que Run. Les clés **Image File Execution Options** (IFEO, `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<exe>`, valeur `Debugger`) permettent de rediriger l'exécution d'un programme légitime vers un programme malveillant — très subtil.

La vérification croisée avec **Autoruns** (Sysinternals) ou Velociraptor (query `Autoruns`) est la méthode la plus fiable pour inventorier tous les points de persistance actifs sur une machine.

## 12.4 Fil rouge — MUSIC BOX : les artefacts d'exécution

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
