---
title: 'Annexe C — Artefacts Windows : référence rapide'
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Annexes
  - index.md
---

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
