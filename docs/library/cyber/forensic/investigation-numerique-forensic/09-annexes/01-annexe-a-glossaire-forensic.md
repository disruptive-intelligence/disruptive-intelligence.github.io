---
title: Annexe A — Glossaire forensic
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Annexes
  - index.md
---

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
