---
title: PARTIE VIII — APPLICATION ET SYNTHÈSE
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 9
chapters: 9
---

*Cette partie est un atelier de synthèse : 4 cas complets qui appliquent l'intégralité de la méthodologie forensic sur des types d'incidents distincts. Chaque cas suit le processus complet : identification → préservation → acquisition → analyse → rapport.*

---

#### Chapitre 30 — Cas complet : compromission Windows avec mouvement latéral et exfiltration

Synthèse du fil rouge MUSIC BOX sous forme de cas autonome. Du spearphishing initial (J-60) au rapport final, en passant par le dump RAM, le triage KAPE, l'image disque, l'analyse mémoire (process hollowing, credentials en mémoire), l'analyse des artefacts d'exécution (Prefetch, Amcache, SRUM confirmant l'exfiltration), la détection du mouvement latéral (PsExec traces, RDP traces, SSH vers le serveur Linux), l'investigation AD (Kerberoasting, DCSync), la détection de l'anti-forensics (timestomping, log clearing), et la production du rapport pour le juge et le COMEX. La timeline unifiée de 60 jours est le livrable central.

#### Chapitre 31 — Cas complet : investigation insider threat

Un chercheur senior de NovaPharma annonce son départ pour un concurrent. Trois semaines après son départ, un audit DLP révèle : 45 Go de documentation de recherche copiée sur une clé USB personnelle dans les 10 jours précédant le départ, et un upload de 12 Go vers un compte Google Drive personnel depuis le réseau d'entreprise.

L'investigation forensic du poste (Windows 11) utilise les artefacts USB (registre USBSTOR, SetupAPI logs — identification du modèle et du numéro de série de la clé USB, dates de connexion), les ShellBags (navigation dans les dossiers de recherche confidentielle), les LNK files (fichiers ouverts depuis la clé USB), le navigateur Chrome (historique de connexion à Google Drive, volumes uploadés — confirmés par les logs proxy), et le SRUM (confirmation du volume de données transférées par Chrome vers Google Drive).

Spécificités de l'investigation insider : droit du travail (la charte informatique autorise-t-elle l'usage personnel de clés USB ?), RGPD (les données copiées contiennent-elles des données personnelles de patients d'essais cliniques ?), et procédure disciplinaire/pénale (les preuves doivent être exploitables devant les prud'hommes ET potentiellement devant le tribunal correctionnel pour vol de secrets de fabrication — article L.1227-1 du Code du travail). Le rapport est rédigé en deux versions : une pour le DRH (procédure disciplinaire) et une pour l'avocat (procédure pénale).

#### Chapitre 32 — Cas complet : investigation serveur Linux compromis

Un serveur web exposé sur Internet (Ubuntu 22.04, Apache, application PHP interne) est compromis via une vulnérabilité d'injection SQL dans l'application. L'attaquant a obtenu un shell via un webshell PHP, escaladé ses privilèges via un exploit kernel local, et déployé un cryptominer.

L'investigation Linux : logs Apache (identification de la requête d'injection SQL initiale, accès au webshell), auth.log (tentatives de su, sudo, escalade de privilèges), bash_history (commandes de l'attaquant — reconnaissance, téléchargement du cryptominer, installation du crontab de persistance), crontab (le cryptominer est relancé toutes les 5 minutes), analyse du webshell PHP (code obfusqué, capacités de commande), et analyse du binaire cryptominer (IoC, pool de mining, wallet — pour estimer les revenus de l'attaquant).

Spécificités : pas d'EDR sur le serveur (l'investigation repose entièrement sur les logs système et les artefacts du système de fichiers), logs limités (auth.log rotaîne à 4 fichiers, les logs les plus anciens sont perdus), et reconstruction à partir d'artefacts fragiles (l'attaquant a supprimé son bash_history, mais des fragments sont récupérés dans le swap par recherche de strings).

#### Chapitre 33 — Cas complet : compromission AD et identités hybrides cloud

Un groupe hospitalier français (3 sites, 2 000 utilisateurs, AD synchronisé avec Microsoft 365 E3 via Azure AD Connect) est victime d'une compromission qui commence par un phishing sur M365 (token volé via un kit AitM — Adversary-in-the-Middle), pivot vers l'AD on-premise (l'attaquant utilise le token pour accéder à Azure AD Connect et obtenir les credentials de synchronisation), puis Golden Ticket sur l'AD on-premise (DCSync → forge de TGT), et enfin accès aux données de santé des patients via l'application métier hospitalière.

L'investigation combine forensic cloud (UAL M365 — identification du phishing initial et du token volé, Sign-in Logs — détection du MFA bypass par le kit AitM), forensic AD (Event Logs DC — DCSync détecté via 4662, Golden Ticket détecté via anomalies Kerberos, ADTimeline — modifications d'objets), et forensic endpoint (analyse du serveur Azure AD Connect — extraction de la configuration de synchronisation et des credentials stockées par le connecteur).

Ce cas illustre la complexité croissante des investigations dans les environnements hybrides : l'attaquant pivote entre le cloud et l'on-premise en exploitant les mécanismes de synchronisation qui, par design, font le pont entre les deux mondes. L'investigation doit couvrir les deux environnements de manière intégrée, pas séparée.

---


### ANNEXES

---

#### Annexe A — Glossaire forensic

| Terme | Définition |
|-------|-----------|
| **ADS** | Alternate Data Stream — flux de données secondaire attaché à un fichier NTFS, invisible dans l'explorateur |
| **AFU / BFU** | After First Unlock / Before First Unlock — états d'un mobile chiffré déterminant l'accessibilité des données |
| **Amcache** | Ruche registre Windows enregistrant les programmes exécutés avec hash SHA1 |
| **Anti-forensics** | Techniques utilisées pour empêcher, ralentir ou tromper l'investigation forensic |
| **Artefact** | Trace numérique laissée par une action sur un système — exploitable pour l'investigation |
| **Autopsy** | Plateforme open source de disk forensics, interface graphique de The Sleuth Kit |
| **BAM/DAM** | Background Activity Moderator / Desktop Activity Monitor — artefacts Windows d'exécution |
| **BitLocker** | Solution de chiffrement de disque intégré à Windows |
| **Carving** | Technique de récupération de fichiers par reconnaissance de signatures dans l'espace non alloué |
| **Chain of custody** | Documentation traçant le parcours complet d'une preuve, de sa collecte à sa présentation |
| **Contradictoire** | Principe juridique garantissant que les parties puissent examiner et contester les preuves |
| **C2** | Command and Control — infrastructure de commande d'un malware |
| **DCSync** | Technique d'attaque AD simulant un DC pour récupérer les hashes de tous les comptes |
| **DFIR** | Digital Forensics and Incident Response — combinaison des deux disciplines |
| **DumpIt** | Outil d'acquisition de mémoire vive pour Windows |
| **E01** | Expert Witness Format — format d'image forensic compressé avec métadonnées intégrées |
| **Event Log** | Journal d'événements Windows (format .evtx), source primaire du forensic Windows |
| **ext4** | Système de fichiers standard de Linux |
| **Fileless malware** | Malware s'exécutant uniquement en mémoire, sans écrire de fichier sur le disque |
| **FSEvents** | Journal des modifications de système de fichiers macOS |
| **FTK Imager** | Outil gratuit d'acquisition forensic (image disque, mémoire, preview) |
| **Golden Ticket** | TGT Kerberos forgé avec le hash du krbtgt, donnant un accès illimité au domaine AD |
| **Hashing** | Calcul d'empreinte numérique (MD5, SHA-256) pour la vérification d'intégrité |
| **Hiberfil.sys** | Fichier d'hibernation Windows contenant un dump mémoire compressé |
| **HPA / DCO** | Host Protected Area / Device Configuration Overlay — zones cachées d'un disque dur |
| **Inode** | Structure de métadonnées d'un fichier dans les systèmes de fichiers Unix/Linux |
| **IoC** | Indicator of Compromise — trace observable laissée par un malware (hash, domaine, IP) |
| **JA3/JA4** | Fingerprint TLS — empreinte du client TLS pour identifier des connexions suspectes |
| **Jump Lists** | Listes de fichiers récemment ouverts par application sous Windows |
| **KAPE** | Kroll Artifact Parser and Extractor — outil de collecte automatisée d'artefacts forensic |
| **Kerberoasting** | Technique d'attaque AD consistant à craquer les mots de passe via les tickets Kerberos |
| **KnowledgeC.db** | Base SQLite macOS enregistrant l'activité utilisateur détaillée |
| **LiME** | Linux Memory Extractor — module kernel pour l'acquisition mémoire Linux |
| **LNK** | Fichier raccourci Windows contenant le chemin, le volume et les timestamps du fichier cible |
| **LOLBins** | Living Off the Land Binaries — binaires système légitimes détournés pour l'attaque |
| **MFT** | Master File Table — table maîtresse du système de fichiers NTFS |
| **NTFS** | New Technology File System — système de fichiers standard de Windows |
| **ntds.dit** | Base de données Active Directory contenant tous les objets et hashes |
| **Pagefile.sys** | Fichier d'échange Windows contenant des pages mémoire déplacées sur le disque |
| **Plaso** | Outil de création de Super Timeline à partir d'artefacts forensic multiples |
| **Prefetch** | Artefact Windows enregistrant l'historique des programmes exécutés |
| **Process hollowing** | Technique d'injection de code remplaçant le contenu d'un processus légitime |
| **RAID** | Redundant Array of Independent Disks — configuration de stockage serveur |
| **RAT** | Remote Access Trojan — malware fournissant un accès distant persistant |
| **RegRipper** | Outil d'extraction automatisée d'artefacts depuis le registre Windows |
| **Scoping** | Délimitation du périmètre d'une investigation forensic |
| **ShellBags** | Artefacts du registre Windows enregistrant la navigation dans l'explorateur |
| **ShimCache** | AppCompatCache — artefact Windows d'historique d'exécution de programmes |
| **Slack space** | Espace résiduel en fin de cluster, contenant potentiellement des fragments de fichiers |
| **SRUM** | System Resource Usage Monitor — base de données Windows de consommation de ressources par processus |
| **$STANDARD_INFORMATION** | Attribut MFT contenant les timestamps MACB du fichier (falsifiable par timestomping) |
| **$FILE_NAME** | Attribut MFT contenant un second jeu de timestamps (difficile à falsifier) |
| **Super Timeline** | Timeline unifiée intégrant tous les artefacts temporels de toutes les sources |
| **Sysmon** | System Monitor — outil Microsoft de journalisation avancée (processus, réseau, registre) |
| **Timestomping** | Modification délibérée des timestamps d'un fichier pour brouiller la timeline |
| **TRIM** | Commande SSD effaçant les secteurs marqués comme libérés — rend la récupération impossible |
| **Unified Logging** | Système de journalisation centralisé de macOS |
| **$UsnJrnl** | Update Sequence Number Journal — journal NTFS des modifications de fichiers |
| **Velociraptor** | Outil open source de collecte forensic et de threat hunting à grande échelle |
| **Volatility** | Framework open source d'analyse de mémoire vive |
| **VQL** | Velociraptor Query Language — langage de requête pour Velociraptor |
| **Write blocker** | Dispositif empêchant toute écriture sur un support de stockage pendant l'acquisition |
| **YARA** | Langage de règles pour l'identification de malware par pattern matching |

---

#### Annexe B — Cheat sheets outils

##### Acquisition disque

```bash
# dd (basique)
dd if=/dev/sdX of=/path/image.raw bs=4M status=progress

# dc3dd (avec hashing et logging)
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/log.txt

# FTK Imager (ligne de commande Linux)
ftkimager /dev/sdX /path/image --e01 --compress 6 --frag 4G --verify
```

##### Acquisition mémoire

```bash
# DumpIt (Windows — double-clic ou CLI)
DumpIt.exe /OUTPUT /path/memory.dmp

# WinPmem (Windows)
winpmem_mini_x64.exe /path/memory.raw

# LiME (Linux)
insmod lime.ko "path=/path/memory.lime format=lime"
```

##### Volatility 3

```bash
# Triage rapide
vol -f memory.raw windows.pstree
vol -f memory.raw windows.netscan
vol -f memory.raw windows.cmdline

# Investigation injection
vol -f memory.raw windows.malfind
vol -f memory.raw windows.dlllist --pid 7284

# Credentials
vol -f memory.raw windows.hashdump
vol -f memory.raw windows.lsadump

# Extraction
vol -f memory.raw windows.procdump --pid 7284 --dump-dir output/
vol -f memory.raw windows.dumpfiles --pid 7284 --dump-dir output/
```

##### Eric Zimmerman tools

```bash
# MFT (timestamps, timestomping detection)
MFTECmd.exe -f '$MFT' --csv output/ --csvf mft.csv

# Prefetch (exécution de programmes)
PECmd.exe -d 'C:\Windows\Prefetch' --csv output/ --csvf prefetch.csv

# Amcache (programmes avec hash)
AmcacheParser.exe -f Amcache.hve --csv output/ --csvf amcache.csv

# ShimCache (historique d'exécution)
AppCompatCacheParser.exe -f SYSTEM --csv output/ --csvf shimcache.csv

# ShellBags (navigation explorateur)
SBECmd.exe -d 'C:\Users\JMallet' --csv output/ --csvf shellbags.csv

# LNK files (fichiers récents, chemins réseau)
LECmd.exe -d 'C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent' --csv output/

# Jump Lists
JLECmd.exe -d 'AutomaticDestinations' --csv output/

# Event Logs
EvtxECmd.exe -f Security.evtx --csv output/ --csvf security.csv

# Registre (batch)
RECmd.exe -d 'C:\evidence\registry' --bn RECmd_Batch_MC.reb --csv output/

# SRUM (consommation réseau)
SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/
```

##### Plaso (Super Timeline)

```bash
# Extraction
log2timeline.py --storage-file timeline.plaso image.E01

# Filtrage et export
psort.py -o l2tcsv timeline.plaso -w timeline.csv \
  "date > '2026-01-01' AND date < '2026-03-08'"
```

##### KAPE

```bash
# Triage complet
kape.exe --tsource C: --tdest E:\Output --target KapeTriage

# Collecte + parsing
kape.exe --tsource C: --tdest E:\Output --target KapeTriage \
  --mdest E:\Parsed --module !EZParser
```

##### Réseau

```bash
# Capture tcpdump
tcpdump -i eth0 -w capture.pcap -c 1000000

# Filtrage Wireshark (CLI avec tshark)
tshark -r capture.pcap -Y "ip.addr == 103.xx.xx.xx" -w filtered.pcap

# Zeek
zeek -r capture.pcap local
# Résultat : conn.log, dns.log, http.log, ssl.log, files.log
```

##### Hashing

```bash
# Double hash (Linux)
md5sum image.E01 && sha256sum image.E01

# Hash récursif (hashdeep)
hashdeep -r -c md5,sha256 /path/evidence/ > hashes.txt

# Vérification
hashdeep -r -k hashes.txt -a /path/evidence/
```

---

#### Annexe C — Artefacts Windows : référence rapide

| Artefact | Localisation | Outil de parsing | Ce qu'il révèle | Limites |
|----------|-------------|-----------------|-----------------|---------|
| MFT | `$MFT` (racine NTFS) | MFTECmd | Tous les fichiers avec timestamps $SI et $FN, détection timestomping | Volume massif (millions d'entrées) |
| $UsnJrnl | `$Extend\$UsnJrnl:$J` | MFTECmd | Modifications de fichiers (création, suppression, renommage) avec compte utilisateur | Taille limitée, rotation |
| Prefetch | `C:\Windows\Prefetch\` | PECmd | Programmes exécutés (8 dernières dates, nb exécutions) | Désactivé sur Windows Server |
| Amcache | `C:\Windows\appcompat\Programs\Amcache.hve` | AmcacheParser | Programmes avec hash SHA1 | Pas de compteur d'exécutions |
| ShimCache | Registre SYSTEM (AppCompatCache) | AppCompatCacheParser | Programmes exécutés avec timestamp | Persisté au shutdown uniquement |
| BAM/DAM | Registre SYSTEM (bam\State) | RegRipper, RECmd | Programmes exécutés avec timestamp UTC précis | Win10 1709+ / Server 2016+ |
| SRUM | `C:\Windows\System32\SRU\SRUDB.dat` | SrumECmd | Consommation réseau/CPU par processus (30-60 jours) | Base SQLite, rotation |
| Registre Run | NTUSER.DAT / SOFTWARE | RegRipper, RECmd | Persistence (programmes au démarrage) | L'attaquant peut nettoyer |
| UserAssist | NTUSER.DAT | RegRipper | Programmes exécutés via GUI (compteur + timestamp) | Encodé ROT13, GUI uniquement |
| ShellBags | NTUSER.DAT + UsrClass.dat | SBECmd | Dossiers navigués dans l'explorateur | Pas le contenu des fichiers |
| LNK files | `\Recent\` | LECmd | Fichiers ouverts, chemins réseau, volumes USB | Limité aux fichiers ouverts via GUI |
| Jump Lists | `\Recent\AutomaticDestinations\` | JLECmd | Fichiers récents par application | Rotation selon le nb d'entrées |
| Event Logs | `C:\Windows\System32\winevt\Logs\` | EvtxECmd, Chainsaw | Authentification, processus, services, PowerShell | Rotation (taille par défaut : 20 Mo) |
| Browser (Chrome) | `\AppData\Local\Google\Chrome\User Data\Default\` | Hindsight | Historique, cookies, downloads, passwords | Base SQLite, effaçable |
| RDP Bitmap Cache | `\AppData\Local\Microsoft\Terminal Server Client\Cache\` | bmc-tools, rdpieces | Fragments visuels de sessions RDP | Images partielles |
| Sysmon | `Microsoft-Windows-Sysmon/Operational.evtx` | EvtxECmd | Processus avec hash, connexions réseau, DLL | Nécessite déploiement préalable |

---

#### Annexe D — Artefacts Linux et macOS : référence rapide

##### Linux

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| auth.log / secure | `/var/log/auth.log` ou `/var/log/secure` | grep, Plaso | Authentifications SSH, sudo, su |
| wtmp / btmp | `/var/log/wtmp`, `/var/log/btmp` | `last`, `lastb` | Sessions utilisateur (réussies / échouées) |
| lastlog | `/var/log/lastlog` | `lastlog` | Dernière connexion de chaque utilisateur |
| bash_history | `~/.bash_history` | cat, Plaso | Commandes exécutées (si non supprimé) |
| journald | `/var/log/journal/` | `journalctl` | Journal système structuré (systemd) |
| crontab | `/var/spool/cron/`, `/etc/crontab`, `/etc/cron.d/` | cat | Tâches planifiées (persistance) |
| SSH authorized_keys | `~/.ssh/authorized_keys` | cat | Clés SSH autorisées (persistance) |
| Apache/Nginx logs | `/var/log/apache2/`, `/var/log/nginx/` | grep, GoAccess | Requêtes web (détection webshell, injection) |

##### macOS

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| Unified Logging | `/var/db/diagnostics/` | `log show`, Unified Log Parser | Tout : processus, réseau, système, apps |
| FSEvents | `.fseventsd/` (racine volume) | FSEventsParser, mac_apt | Modifications du système de fichiers |
| KnowledgeC.db | `~/Library/Application Support/Knowledge/` | APOLLO, mac_apt | Activité utilisateur (apps, durée, réseau) |
| Spotlight metadata | `.Spotlight-V100/` | mdls, mac_apt | Métadonnées de tous les fichiers indexés |
| TCC.db | `~/Library/Application Support/com.apple.TCC/` | sqlite3 | Permissions d'accès (caméra, micro, fichiers) |
| LaunchAgents/Daemons | `~/Library/LaunchAgents/`, `/Library/LaunchDaemons/` | plutil | Persistence (programmes au démarrage) |
| Keychain | `~/Library/Keychains/` | security (CLI) | Credentials stockés (avec autorisation) |
| Safari | `~/Library/Safari/` | mac_apt, Autopsy | Historique, downloads, tabs ouvertes |

---

#### Annexe E — Templates

##### Formulaire de chaîne de custody

```
CHAÎNE DE CUSTODY — PIÈCE N° [XX]

Affaire : [Nom de l'affaire / Nom de code]
Description de la pièce : [Type de support, modèle, numéro de série]
État à la collecte : [Allumé/éteint, état physique, connexions]

COLLECTE
  Date/Heure : [JJ/MM/AAAA HH:MM:SS, fuseau horaire]
  Collecté par : [Nom, qualité, organisme]
  Méthode : [Outil utilisé, version, paramètres]
  Hash MD5 : [________________________]
  Hash SHA-256 : [________________________]
  Lieu de stockage : [Coffre, numéro de casier]

TRANSFERTS
  | Date | De | À | Motif | Signature |
  |------|-----|-----|-------|-----------|
  | | | | | |

ANALYSES
  | Date | Analyste | Action | Outil | Hash vérifié ? |
  |------|----------|--------|-------|----------------|
  | | | | | |

Signature du responsable : _____________ Date : _____________
```

##### Template rapport forensic (structure)

```
RAPPORT D'INVESTIGATION FORENSIC
[CONFIDENTIEL — DIFFUSION RESTREINTE]

1. RÉSUMÉ EXÉCUTIF (1-2 pages)
   - Contexte, mandat, conclusions principales, impact, recommandations

2. CADRE DE L'INVESTIGATION
   - Mandataire, périmètre, questions investigatives
   - Méthodologie, outils (noms, versions), environnement d'analyse

3. CHRONOLOGIE DES OPÉRATIONS
   - Acquisitions réalisées (avec hash et chaîne de custody)
   - Analyses menées (séquence chronologique)

4. FAITS CONSTATÉS
   - Chaque constatation : source, date, description, niveau de confiance
   - Distinction explicite : fait / déduction / hypothèse

5. ANALYSE ET INTERPRÉTATION
   - Timeline de l'intrusion
   - Mapping MITRE ATT&CK
   - Hypothèses concurrentes et test

6. CONCLUSIONS
   - Réponses aux questions investigatives
   - Niveaux de confiance explicites
   - Ce qui n'a pas pu être déterminé (angles morts)

7. RECOMMANDATIONS
   - Mesures correctives et préventives
   - Suggestions pour la procédure judiciaire (si applicable)

ANNEXES
  A. IoC complets (hash, domaines, IP, artefacts)
  B. Timeline détaillée
  C. Captures d'écran annotées
  D. Chaîne de custody de chaque pièce
  E. Configuration de l'environnement d'analyse
```

---

#### Annexe F — Ressources et certifications

##### Certifications (à jour 2025-2026)

| Certification | Organisme | Focus | Cours associé |
|--------------|-----------|-------|---------------|
| GCFE (Forensic Examiner) | SANS/GIAC | Windows forensics fondamental | FOR500 |
| GCFA (Forensic Analyst) | SANS/GIAC | Forensics avancé, threat hunting | FOR508 |
| GNFA (Network Forensic Analyst) | SANS/GIAC | Network forensics | FOR572 |
| GASF (Advanced Smartphone Forensics) | SANS/GIAC | Mobile forensics | FOR585 |
| GREM (Reverse Engineering Malware) | SANS/GIAC | Malware analysis | FOR610 |
| EnCE (EnCase Certified Examiner) | OpenText | EnCase forensics | Formation éditeur |
| ACE (AccessData Certified Examiner) | Exterro | FTK forensics | Formation éditeur |
| CHFI (Computer Hacking Forensic Investigator) | EC-Council | Forensics général | Programme EC-Council |
| CCFP (Certified Cyber Forensics Professional) | ISC² | Forensics management | Auto-formation + examen |

##### Formations SANS de référence

| Code | Titre | Focus |
|------|-------|-------|
| FOR500 | Windows Forensic Analysis | Artefacts Windows, registre, timeline |
| FOR508 | Advanced Incident Response, Threat Hunting, and Digital Forensics | IR + forensics avancé, memory forensics |
| FOR518 | Mac and iOS Forensic Analysis and Incident Response | macOS et iOS |
| FOR572 | Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response | Network forensics |
| FOR578 | Cyber Threat Intelligence | CTI appliqué au forensic |
| FOR585 | Smartphone Forensic Analysis In-Depth | Mobile forensics |
| FOR610 | Reverse-Engineering Malware | Malware analysis avancé |

##### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| DFRWS (Digital Forensic Research Workshop) | Conférence | Recherche académique en forensic |
| OSDFCon (Open Source Digital Forensics) | Conférence | Forensic open source (Autopsy, Sleuth Kit) |
| Magnet User Summit | Conférence | Forensic commercial (Magnet AXIOM) |
| SANS DFIR Summit | Conférence/Webcasts | Présentations pratiques DFIR |
| The DFIR Report | Blog | Rapports d'intrusion détaillés, pas à pas |
| 13Cubed (YouTube) | Vidéos | Tutoriels forensic pratiques |
| SANS DFIR Blog | Blog | Articles techniques et cas d'étude |
| Forensic Focus | Communauté | Articles, forums, offres d'emploi |
| r/digitalforensics | Reddit | Communauté, questions, ressources |
| FIRST | Communauté | Forum international des CERT/CSIRT |
| InterCERT France | Communauté | Association des CERT français |

##### Ouvrages de référence

| Titre | Auteur(s) | Sujet |
|-------|-----------|-------|
| *The Art of Memory Forensics* | Hale Ligh, Case, Levy, Walters | Analyse mémoire avec Volatility |
| *File System Forensic Analysis* | Brian Carrier | Systèmes de fichiers (NTFS, ext, FAT) |
| *Incident Response & Computer Forensics* | Luttgens, Pepe, Mandia | IR + forensic intégré |
| *Digital Forensics with Kali Linux* | Parasram | Forensic pratique avec Kali |
| *Practical Malware Analysis* | Sikorski, Honig | Analyse de malware (statique + dynamique) |
| *Windows Forensic Analysis* (SANS courseware) | Rob Lee | Artefacts Windows en profondeur |
| *Network Forensics* | Davidoff, Ham | Analyse réseau forensic |

---

---


## Annexe — Questions types d'entretien et réponses types


### Questions essentielles

- **Question :** Quelle est la différence entre le forensic judiciaire et le triage DFIR ?
  - **Réponse type :** Le forensic judiciaire vise à produire des preuves recevables devant un tribunal — l'exhaustivité et la chaîne de custody priment. Le triage DFIR vise à comprendre rapidement ce qui se passe pour contenir la menace — la rapidité prime. En pratique, les deux s'articulent : on commence souvent en triage et on bascule en judiciaire si les constatations le justifient. C'est pour ça qu'il faut respecter les bonnes pratiques de préservation dès le début, même en triage — on ne sait jamais si l'affaire finira devant un juge.

- **Question :** Qu'est-ce que la chaîne de custody et pourquoi c'est critique ?
  - **Réponse type :** La chaîne de custody trace chaque manipulation d'une preuve : qui l'a collectée, quand, comment, où elle a été stockée, qui y a eu accès. C'est ce qui garantit l'intégrité et la recevabilité de la preuve en justice. Si la chaîne est rompue — par exemple une image disque non hashée ou un scellé mal documenté —, la partie adverse peut contester la preuve et le juge peut la rejeter.

- **Question :** Qu'est-ce que l'ordre de volatilité et comment l'appliquez-vous ?
  - **Réponse type :** L'ordre de volatilité dicte la priorité de collecte : on commence par ce qui disparaît le plus vite. La mémoire RAM est la plus volatile — elle contient les processus en cours, les clés de chiffrement, les connexions réseau, et elle disparaît au redémarrage. Ensuite les logs système, le cache, les fichiers temporaires, puis le disque dur. En pratique : d'abord le dump RAM (DumpIt), puis le triage KAPE pour les artefacts, puis l'image disque complète. Et surtout, ne jamais éteindre une machine avant d'avoir capturé la mémoire.

- **Question :** Quels sont les principaux artefacts Windows que vous analysez ?
  - **Réponse type :** Pour l'exécution : le Prefetch (programmes exécutés avec dates), l'Amcache et le ShimCache (historique d'exécution avec hash), les Event Logs (4688 création de processus, Sysmon). Pour l'activité utilisateur : les ShellBags (navigation explorateur), les Jump Lists (fichiers récents par application), les fichiers LNK (raccourcis avec chemins et dates). Pour la persistence : les clés Run/RunOnce du registre, les services, les tâches planifiées. La MFT pour la timeline de tous les fichiers. Les outils Eric Zimmerman (MFTECmd, PECmd, AmcacheParser) sont la référence pour parser tout ça.

- **Question :** Comment détectez-vous le timestomping ?
  - **Réponse type :** Le timestomping consiste à modifier les timestamps des fichiers pour masquer l'activité. Sous NTFS, il y a deux jeux de timestamps : $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le kernel). Si les deux divergent — par exemple si $SI montre une date ancienne mais $FN montre une date récente — c'est un signe de manipulation. MFTECmd extrait les deux et la comparaison est immédiate.


### Questions complémentaires

- **Question :** Quels outils utilisez-vous pour le triage rapide ?
  - **Réponse type :** KAPE (Kroll Artifact Parser and Extractor) pour la collecte et le parsing automatisé des artefacts Windows — en quelques minutes il collecte les Event Logs, le registre, le Prefetch, la MFT, l'Amcache, les historiques navigateur. Velociraptor pour la collecte à distance sur un parc entier via des requêtes VQL. FTK Imager pour l'acquisition disque en format E01 avec write blocker. Et DumpIt pour le dump mémoire.

- **Question :** C'est quoi l'analyse mémoire et pourquoi c'est indispensable ?
  - **Réponse type :** L'analyse mémoire capture l'état instantané du système : les processus en cours, les connexions réseau, les DLLs chargées, les credentials en clair, et le code des malwares fileless qui n'existent qu'en RAM. L'outil de référence c'est Volatility 3. On peut identifier un processus injecté (svchost.exe avec un parent anormal), extraire les clés de chiffrement d'un ransomware, ou trouver un RAT qui ne touche jamais le disque. Sans dump mémoire, on perd toute cette information au redémarrage.


### Questions les plus probables en entretien

1. Forensic judiciaire vs triage DFIR ?
2. Chaîne de custody : pourquoi c'est critique ?
3. Ordre de volatilité : RAM en premier ?
4. Artefacts Windows clés ?
5. Comment détecter le timestomping ?
6. Outils de triage et d'acquisition ?


### Réponses flash

- **Forensic vs triage** → Judiciaire = exhaustivité, preuve recevable, chaîne de custody. DFIR = rapidité, contenir la menace. Les deux s'articulent.
- **Chaîne de custody** → Qui, quand, comment, où. Hash (MD5 + SHA-256). Rupture = preuve contestable.
- **Volatilité** → RAM → cache → logs → fichiers temp → disque. D'abord DumpIt, puis KAPE, puis image disque.
- **Artefacts Windows** → Prefetch, Amcache, ShimCache (exécution). ShellBags, LNK, Jump Lists (activité). Run keys, services, tasks (persistence). MFT (timeline).
- **Timestomping** → Comparer $STANDARD_INFORMATION vs $FILE_NAME dans la MFT. Divergence = manipulation.
- **Outils** → KAPE (triage), Velociraptor (collecte à distance), FTK Imager (image E01), DumpIt (RAM), Volatility 3 (analyse mémoire), Eric Zimmerman tools (parsing).

---


> **Note de clôture**
>
> Ce cours a été conçu pour former à l'investigation numérique comme discipline scientifique complète — de l'acquisition rigoureuse des preuves à la production d'un rapport défendable devant un tribunal, en passant par l'analyse technique approfondie des artefacts sur tous les types de systèmes.
>
> L'investigation MUSIC BOX qui traverse les 29 premiers chapitres illustre la réalité du terrain : l'analyste forensic ne se contente pas d'extraire des artefacts d'une machine — il reconstitue une histoire de 60 jours de compromission, il corrèle des sources hétérogènes (endpoint, réseau, AD, cloud), il détecte les tentatives d'anti-forensics de l'attaquant, il raisonne par hypothèses en gérant ses propres biais, et il produit un rapport qui sera lu par un juge ET par un CEO.
>
> La compétence forensic ne se résume pas à la maîtrise des outils — c'est une posture intellectuelle : rigueur, doute méthodique, transparence des conclusions, et humilité face à la complexité du réel. Les outils évoluent (Volatility 4 remplacera peut-être Volatility 3, de nouveaux artefacts apparaîtront avec chaque version de Windows), mais la posture reste.
>
> *Acquisition • Analyse • Preuve • Rapport — avec rigueur et objectivité.*
