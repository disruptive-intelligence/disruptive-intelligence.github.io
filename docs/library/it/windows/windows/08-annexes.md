---
title: Annexes
source: IT/02_Windows/Windows.md
note: Windows
up:
- - Windows
  - index.md
---

---


#### Annexe A — Cheat Sheet Windows

##### Triage rapide PowerShell

```powershell
# Processus
Get-Process | Sort-Object CPU -Descending | Select -First 20
Get-WmiObject Win32_Process | Select Name, ProcessId, ParentProcessId, CommandLine

# Services
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-WmiObject Win32_Service | Where {$_.StartMode -eq 'Auto'} | Select Name, DisplayName, PathName, StartName

# Scheduled Tasks
Get-ScheduledTask | Where {$_.State -eq 'Ready'} | Select TaskName, TaskPath, State

# Connexions réseau
Get-NetTCPConnection -State Established | Select LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess

# Event Logs récents
Get-WinEvent -LogName Security -MaxEvents 50 | Where {$_.Id -in @(4624,4625,4672,4688,7045)}
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 50

# Registre - persistence
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
Get-ItemProperty 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'

# Prefetch
Get-ChildItem C:\Windows\Prefetch -Filter *.pf | Sort LastWriteTime -Descending | Select -First 20

# Drivers chargés
driverquery /v /fo csv | ConvertFrom-Csv | Sort Status
```


##### Commandes CMD essentielles

```
netstat -anob                    # Connexions avec PID et binaire
tasklist /v                      # Processus avec détails
wmic process get name,processid,parentprocessid,commandline
sc query type= service state= all   # Tous les services
schtasks /query /fo LIST /v      # Tâches planifiées détaillées
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
systeminfo                       # Info système
```


---


#### Annexe B — Matrice Artefact / Ce qu'il prouve / Outil

| Artefact | Localisation | Ce qu'il prouve | Outil | Rétention |
|----------|-------------|----------------|-------|-----------|
| Prefetch | C:\Windows\Prefetch | Programme exécuté (timestamps, run count) | PECmd | 128 fichiers max |
| Amcache | Amcache.hve | Programme installé/exécuté (hash SHA-1) | AmcacheParser | Persistant |
| ShimCache | Registre SYSTEM | Fichier rencontré par l'OS (pas forcément exécuté Win10+) | AppCompatCacheParser | Persistant |
| BAM/DAM | Registre SYSTEM | Programme exécuté par utilisateur | RECmd | ~7 jours |
| UserAssist | HKCU | Programme lancé via Explorer (ROT13) | RECmd | Persistant |
| SRUM | SRUDB.dat | Utilisation CPU/réseau par application | SrumECmd | 30-60 jours |
| $MFT | Volume NTFS | Tous les fichiers (existants + supprimés récents) | MFTECmd | Tant que non écrasé |
| $UsnJrnl | Volume NTFS | Journal des modifications fichiers | MFTECmd | Variable (taille journal) |
| LNK | %APPDATA%\Recent | Fichiers accédés (chemins, timestamps) | LECmd | Persistant |
| Jump Lists | %APPDATA%\Recent\AutomaticDestinations | Fichiers récents par application | JLECmd | Persistant |
| Shellbags | NTUSER.DAT / UsrClass.dat | Dossiers navigués (même supprimés) | ShellBagsExplorer | Persistant |
| Recycle Bin | $Recycle.Bin | Fichiers supprimés ($I = méta, $R = contenu) | RBCmd | Jusqu'à vidage |
| Zone.Identifier | ADS du fichier | Source de téléchargement (MotW) | Streams / Get-Content -Stream | Tant que fichier existe |
| Event Logs | winevt\Logs | Activité système/sécurité/application | EvtxECmd, Get-WinEvent | Taille du journal |
| Registre | SAM/SECURITY/SOFTWARE/SYSTEM/NTUSER | Configuration, persistence, secrets | RECmd, Registry Explorer | Persistant |
| Mémoire RAM | Dump mémoire | Processus, connexions, credentials, code injecté | Volatility 3 | Volatil (live uniquement) |

---


#### Annexe C — Event IDs de référence

| Event ID | Source | Description | Pertinence sécurité |
|----------|--------|-------------|-------------------|
| 4624 | Security | Logon succès | Types 2/3/7/10 — source, compte, machine |
| 4625 | Security | Logon échec | Volume = brute force/spraying |
| 4648 | Security | Explicit credentials | Mouvement latéral potentiel |
| 4672 | Security | Special privileges | Escalade potentielle |
| 4688 | Security | Process creation | Avec command line = détection #1 |
| 4698 | Security | Scheduled task créée | Persistence |
| 4720 | Security | Account created | Compte créé par attaquant ? |
| 7045 | System | Service installé | PsExec, persistence |
| 1102 | Security | Audit log cleared | Effacement de logs = alerte |
| 4104 | PowerShell | Script Block | Code PowerShell désobfusqué |
| 4103 | PowerShell | Module Logging | Appels de modules |

---


#### Annexe D — Sysmon Event IDs

| Event ID | Description | Usage détection |
|----------|-------------|----------------|
| 1 | Process Creation | Command line, parent, hash — détection n°1 |
| 3 | Network Connection | Processus → IP:port — C2, mouvement latéral |
| 6 | Driver Loaded | Hash du driver — BYOVD detection |
| 7 | Image Loaded | DLL chargée dans un processus — DLL injection |
| 8 | CreateRemoteThread | Injection de code inter-processus |
| 10 | Process Access | Accès mémoire lsass.exe — credential dumping |
| 11 | File Created | Fichier créé — payload, persistence |
| 12/13/14 | Registry events | Création/modification/renommage de clés |
| 19/20/21 | WMI events | WMI persistence — FilterToConsumerBinding |
| 22 | DNS Query | Domaines résolus par processus — C2 domain |
| 25 | Process Tampering | Image file hollowing — Process Hollowing |

---


#### Annexe E — LOLBins : binaires détournables et détection

| LOLBin | Usage légitime | Usage offensif | Command line suspecte | Détection |
|--------|---------------|---------------|----------------------|-----------|
| certutil | Gestion de certificats | Téléchargement + décodage | -urlcache -split -f http:// | Sysmon 1 + 3 |
| mshta | Exécution HTA | Exécution de script distant | mshta http://... ou vbscript: | Sysmon 1 + 3 |
| rundll32 | Appel de fonctions DLL | Exécution de payload DLL | DLL dans %TEMP% ou URL | Sysmon 1 + 7 |
| regsvr32 | Enregistrement COM | Squiblydoo — script distant | /s /n /u /i:http://... | Sysmon 1 + 3 |
| bitsadmin | Transferts en arrière-plan | Téléchargement discret | /transfer /download http:// | Event BITS + Sysmon 1 |
| wmic | Administration WMI | Exécution à distance | process call create | Sysmon 1, 4688 |
| cmstp | Profils CM | Bypass UAC + exécution | /ni /s [fichier .inf] | Sysmon 1 |
| msiexec | Installation MSI | Exécution depuis URL | /q /i http://... | Sysmon 1 + 3 |
| powershell | Scripting/admin | Download + execute | -enc, IEX, -nop -w hidden | Event 4104 + Sysmon 1 |

---


#### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Windows internals (ce cours) | **Ce cours (Windows)** | — |
| Active Directory | **Cours AD** | Windows (Ch.11-12 credentials, Ch.18 authentification) |
| Détection SOC | **Cours SOC** | Windows (Ch.21-22 Event Logs/Sysmon, Ch.31 arbre de processus) |
| Incident Response | **Cours IR** | Windows (Ch.23-25 artefacts forensic, Ch.28 investigation complète) |
| Infrastructure IT | **Cours Infra** | Windows (Ch.7 Infra — vue d'ensemble OS) |
| APT | **Cours APT** | Windows (Ch.9 injection, Ch.17 persistence, Ch.20 EDR evasion) |
| Digital Forensic | **Cours Forensic** | Windows (Ch.23-24 artefacts, Ch.25 méthodologie, Ch.30 Volatility) |

---


#### Annexe G — Glossaire, ressources et lab

##### Glossaire (sélection)

| Terme | Définition |
|-------|-----------|
| **ACL / DACL / SACL** | Access Control List / Discretionary / System — permissions et audit |
| **ADS** | Alternate Data Stream — données cachées dans un flux NTFS |
| **AMSI** | Anti-Malware Scan Interface — scan du code avant exécution |
| **ASLR** | Address Space Layout Randomization — randomisation des adresses |
| **ASR** | Attack Surface Reduction — règles Defender bloquant des comportements |
| **BYOVD** | Bring Your Own Vulnerable Driver — driver légitime vulnérable pour accès kernel |
| **CFG** | Control Flow Guard — vérification des appels de fonctions indirects |
| **Credential Guard** | Isolation des credentials via VBS/hyperviseur |
| **DEP** | Data Execution Prevention — bloque l'exécution dans les pages données |
| **DPAPI** | Data Protection API — chiffrement des secrets utilisateur |
| **ETW** | Event Tracing for Windows — mécanisme de trace universel |
| **HVCI** | Hypervisor-Protected Code Integrity — intégrité du code kernel |
| **IFEO** | Image File Execution Options — hijack d'exécutable via registre |
| **LOLBin** | Living-off-the-Land Binary — binaire légitime détourné |
| **MFT** | Master File Table — index de tous les fichiers NTFS |
| **MotW** | Mark of the Web — marquage des fichiers téléchargés |
| **PE** | Portable Executable — format des binaires Windows |
| **PPL** | Protected Process Light — protection de lsass |
| **SRM** | Security Reference Monitor — vérifie les droits d'accès |
| **VBS** | Virtualization-Based Security — isolation via hyperviseur |
| **WDAC** | Windows Defender Application Control — contrôle d'exécution kernel |

##### Ressources

| Ressource | Type | Focus |
|-----------|------|-------|
| Windows Internals (Russinovich) | Livre | LA référence sur les internals Windows |
| SANS FOR500 (Windows Forensic Analysis) | Formation | Investigation forensic Windows |
| SANS FOR508 (Advanced IR & Threat Hunting) | Formation | IR avancé et threat hunting |
| 13Cubed (YouTube) | Vidéos | Forensic Windows pratique |
| Eric Zimmerman Tools | Outils | Suite complète de parsing d'artefacts |
| KAPE | Outil | Collecte + parsing automatisé |
| Velociraptor | Outil | Triage à distance à l'échelle |
| Volatility 3 | Outil | Analyse mémoire |
| CyberDefenders | Plateforme | Challenges forensic Blue Team |
| HackTheBox Sherlocks | Plateforme | Challenges forensic/IR |
| lolbas-project.github.io | Référence | Catalogue complet des LOLBins |
| SwiftOnSecurity/sysmon-config | Config | Baseline Sysmon communautaire |

##### Lab

Infrastructure minimale : 1 VM Windows 11 Pro (ou Enterprise si disponible), Sysmon installé avec config SwiftOnSecurity, outils Sysinternals (Process Explorer, Process Monitor, Autoruns, TCPView), suite Eric Zimmerman, KAPE, Volatility 3, Python 3. Optionnel : Flare VM (distribution Windows pré-configurée pour l'analyse de malwares — outils de reverse, debuggers, sandbox).

---

---


## Annexe — Questions types d'entretien et réponses types
