---
title: Annexes
source: IT/02_Windows/Windows_Command-Line.md
note: Windows Command Line
up:
- - Windows Command Line
  - index.md
---

-----

### Annexe A — Correspondance CMD / PowerShell / Linux

|Opération             |CMD                 |PowerShell                    |Linux (Bash)       |
|----------------------|--------------------|------------------------------|-------------------|
|Qui suis-je ?         |`whoami`            |`whoami`                      |`whoami`           |
|Nom de la machine     |`hostname`          |`hostname`                    |`hostname`         |
|Où suis-je ?          |`cd`                |`Get-Location`                |`pwd`              |
|Changer de dossier    |`cd dossier`        |`Set-Location dossier`        |`cd dossier`       |
|Lister les fichiers   |`dir`               |`Get-ChildItem`               |`ls`               |
|Créer un dossier      |`mkdir`             |`New-Item -ItemType Directory`|`mkdir`            |
|Copier un fichier     |`copy`              |`Copy-Item`                   |`cp`               |
|Déplacer un fichier   |`move`              |`Move-Item`                   |`mv`               |
|Supprimer un fichier  |`del`               |`Remove-Item`                 |`rm`               |
|Lire un fichier       |`type`              |`Get-Content`                 |`cat`              |
|Écrire dans un fichier|`echo texte > f`    |`Set-Content f "texte"`       |`echo texte > f`   |
|Rechercher du texte   |`findstr`           |`Select-String`               |`grep`             |
|Configuration réseau  |`ipconfig`          |`Get-NetIPConfiguration`      |`ip addr`          |
|Ping                  |`ping`              |`Test-Connection`             |`ping`             |
|DNS                   |`nslookup`          |`Resolve-DnsName`             |`dig` / `nslookup` |
|Connexions réseau     |`netstat -ano`      |`Get-NetTCPConnection`        |`ss` / `netstat`   |
|Processus             |`tasklist`          |`Get-Process`                 |`ps aux`           |
|Tuer un processus     |`taskkill /PID`     |`Stop-Process -Id`            |`kill`             |
|Services              |`sc query`          |`Get-Service`                 |`systemctl`        |
|Utilisateurs          |`net user`          |`Get-LocalUser`               |`cat /etc/passwd`  |
|Variables d’env       |`set` / `echo %VAR%`|`$env:VAR`                    |`env` / `echo $VAR`|
|Aide                  |`commande /?`       |`Get-Help commande`           |`man commande`     |
|Effacer l’écran       |`cls`               |`Clear-Host`                  |`clear`            |

-----

### Annexe B — Les commandes CMD essentielles

```
whoami               hostname             ver                  cls
cd                   dir                  tree                 mkdir
rmdir                copy                 xcopy                robocopy
move                 ren                  del                  type
echo                 set                  where                findstr
ipconfig             ping                 tracert              pathping
nslookup             netstat              tasklist             taskkill
sc query             net user             net localgroup       schtasks
systeminfo           reg query            icacls               curl
```


-----

### Annexe C — Les cmdlets PowerShell essentielles

```
Get-Help                  Get-Command               Get-Alias
Get-Member                Get-Location              Set-Location
Get-ChildItem             New-Item                  Remove-Item
Copy-Item                 Move-Item                 Rename-Item
Get-Content               Set-Content               Add-Content
Select-String             Get-ComputerInfo          Get-CimInstance
Get-Process               Stop-Process              Get-Service
Start-Service             Stop-Service              Restart-Service
Get-LocalUser             Get-LocalGroupMember      Get-ScheduledTask
Get-WinEvent              Get-NetIPConfiguration    Test-Connection
Test-NetConnection        Resolve-DnsName           Get-NetTCPConnection
Invoke-WebRequest         Get-FileHash              Get-AuthenticodeSignature
Out-File                  Export-Csv                ConvertTo-Json
```


-----

### Annexe D — Event IDs Windows essentiels

|Event ID|Journal               |Signification                                          |
|--------|----------------------|-------------------------------------------------------|
|4624    |Security              |Connexion réussie                                      |
|4625    |Security              |Échec de connexion                                     |
|4648    |Security              |Connexion avec des identifiants explicites             |
|4720    |Security              |Création d’un compte utilisateur                       |
|4726    |Security              |Suppression d’un compte utilisateur                    |
|4732    |Security              |Ajout d’un membre à un groupe de sécurité              |
|4688    |Security              |Création d’un processus (si activé par GPO)            |
|7045    |System                |Installation d’un nouveau service                      |
|1102    |Security              |Journal de sécurité effacé (suspect !)                 |
|4104    |PowerShell/Operational|Script Block Logging                                   |
|400     |Windows PowerShell    |Démarrage du moteur PowerShell                         |
|6005    |System                |Démarrage du service Event Log (= la machine a démarré)|
|6006    |System                |Arrêt du service Event Log (= la machine s’est éteinte)|

-----

### Annexe E — Outils Sysinternals essentiels (aperçu)

|Outil               |Usage                                                                     |Téléchargement                                        |
|--------------------|--------------------------------------------------------------------------|------------------------------------------------------|
|**Autoruns**        |Voir TOUT ce qui se lance au démarrage (registre, services, tâches, DLLs…)|[live.sysinternals.com](https://live.sysinternals.com)|
|**Process Explorer**|Gestionnaire de tâches avancé (arborescence, DLLs, handles)               |idem                                                  |
|**TCPView**         |Connexions réseau en temps réel, par processus                            |idem                                                  |
|**PsExec**          |Exécuter des commandes sur des machines distantes                         |idem                                                  |
|**ProcMon**         |Surveiller l’activité fichier/registre/réseau d’un processus en temps réel|idem                                                  |


> **Astuce :** tous les outils Sysinternals sont accessibles sans installation via `\\live.sysinternals.com\tools\` dans l’Explorateur de fichiers.

-----

### Annexe F — Pour aller plus loin

|Thème                     |Ressource recommandée                  |
|--------------------------|---------------------------------------|
|Scripting PowerShell      |Cours PowerShell de la bibliothèque    |
|Administration Windows    |Cours Windows en profondeur            |
|Active Directory          |Cours Active Directory                 |
|Forensic Windows          |Cours Digital Forensics                |
|Réponse à incident        |Cours Réponse à incident               |
|Sysinternals en profondeur|Livre “Windows Internals” (Russinovich)|
|Infrastructure réseau     |Cours Infrastructure IT                |
|SOC / SIEM                |Cours SOC + logs Windows               |

-----


## Conclusion

Tu sais maintenant utiliser la ligne de commande Windows pour naviguer, diagnostiquer, administrer et collecter des informations. Voici ce que tu peux faire :

- **Naviguer** dans le système de fichiers et manipuler des fichiers (Ch.2-6)
- **Diagnostiquer** le réseau avec `ipconfig`, `ping`, `tracert`, `netstat` (Ch.17)
- **Inspecter** les processus, services, utilisateurs, tâches planifiées (Ch.11-14)
- **Consulter** les journaux Windows et le registre (Ch.15-16)
- **Collecter** des informations pour un triage de sécurité (Ch.21)
- **Choisir** entre CMD et PowerShell selon le contexte (Ch.9)
- **Écrire** un script batch simple et un mini-script PowerShell (Ch.19-20)

**La suite logique :**

- Le **cours PowerShell** pour apprendre à scripter et automatiser
- Le **cours Active Directory** pour administrer un domaine
- Les cours de **cybersécurité** pour utiliser ces compétences en investigation et en défense

La ligne de commande n’est pas un outil du passé — c’est l’outil le plus puissant et le plus durable de l’administration Windows. Les interfaces graphiques changent à chaque version de Windows. Les commandes, elles, restent.

Bon apprentissage !
