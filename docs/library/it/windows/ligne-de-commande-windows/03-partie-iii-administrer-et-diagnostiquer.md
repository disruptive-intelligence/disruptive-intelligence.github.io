---
title: Partie III — Administrer et diagnostiquer
source: IT/02_Windows/Windows_Command-Line.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - index.md
---

-----


## Chapitre 9 — CMD vs PowerShell : comprendre la différence

### Le minimum à savoir

#### CMD : historique, simple, orienté texte

CMD traite tout comme du **texte brut**. Quand tu fais `tasklist`, le résultat est un bloc de texte formaté. Pour en extraire une information, tu dois chercher des mots dans ce texte avec `findstr` — comme chercher un mot dans un livre.

```cmd
tasklist | findstr chrome
```


#### PowerShell : moderne, orienté objets

PowerShell traite tout comme des **objets structurés**. Quand tu fais `Get-Process`, chaque processus est un objet avec des propriétés nommées (`Name`, `Id`, `CPU`, `WorkingSet64`…). Tu accèdes directement aux propriétés — pas besoin de parser du texte.

```powershell
Get-Process chrome
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5
```


#### La comparaison concrète

**La même tâche : trouver les 5 processus les plus gourmands en CPU.**

CMD :

```cmd
REM Pas de commande simple pour trier par CPU en CMD
REM Il faudrait exporter, parser avec des outils externes...
tasklist /v
```


PowerShell :

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5
```


#### Quand utiliser CMD ?

- Commandes réseau classiques (`ipconfig`, `ping`, `tracert`, `netstat`)
- Dépannage rapide sur n’importe quel Windows
- Scripts batch (.bat) existants
- Compatibilité avec des environnements anciens
- Quand tu veux une réponse rapide sans charger PowerShell

#### Quand utiliser PowerShell ?

- Administration moderne (processus, services, utilisateurs, registre)
- Filtrage et tri avancés (`Where-Object`, `Sort-Object`, `Select-Object`)
- Export structuré (CSV, JSON)
- Automatisation et scripting
- Collecte d’informations système
- Tout ce qui nécessite de traiter des données de manière structurée

#### La règle simple

> **En pratique :** utilise CMD pour les commandes réseau classiques et les tâches ponctuelles rapides. Utilise PowerShell pour tout ce qui nécessite de filtrer, trier, exporter ou automatiser.


-----


## Chapitre 10 — Informations système et diagnostic de base

### Le minimum à savoir

#### Identifier la machine

```cmd
REM CMD
whoami                       REM Utilisateur actuel (DOMAINE\utilisateur)
hostname                     REM Nom de la machine
ver                          REM Version de Windows (courte)
systeminfo                   REM Informations détaillées (OS, RAM, patchs, boot time...)
```


```powershell
# PowerShell
whoami
hostname
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsArchitecture
```


#### `systeminfo` en détail

`systeminfo` est une mine d’or — elle affiche en une seule commande :

- Le nom et la version de l’OS
- La date d’installation
- La date du dernier démarrage (uptime)
- La mémoire totale et disponible
- Les cartes réseau
- Les correctifs (hotfixes) installés

```cmd
systeminfo
systeminfo | findstr /i "boot"       REM Depuis quand la machine tourne-t-elle ?
systeminfo | findstr /i "hotfix"     REM Quels patchs sont installés ?
```


#### Informations système via PowerShell (CIM)

PowerShell accède à des informations système détaillées via **CIM** (Common Information Model) :

```powershell
# Informations sur le système d'exploitation
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, LastBootUpTime

# Informations sur le matériel
Get-CimInstance Win32_ComputerSystem | Select-Object Name, Manufacturer, Model, TotalPhysicalMemory

# Espace disque
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, @{N="Taille (Go)";E={[math]::Round($_.Size/1GB)}}, @{N="Libre (Go)";E={[math]::Round($_.FreeSpace/1GB)}}
```


> **Note :** `Get-CimInstance` remplace l’ancien `Get-WmiObject` (qui fonctionne encore mais est déprécié). CIM est la méthode moderne pour interroger le système.

#### Espace disque avec CMD

```cmd
wmic logicaldisk get name,size,freespace
```


> **⚠️ wmic est déprécié.** Microsoft a marqué `wmic` comme obsolète depuis Windows 10 21H1 / Windows Server 21H1, et il peut ne pas être disponible sur certaines versions récentes de Windows 11. Il reste utile à connaître pour lire d’anciens scripts, mais pour tout nouveau travail, utilise PowerShell avec `Get-CimInstance` (méthode moderne, supportée et plus puissante).

> **📋 FIL ROUGE — Épisode 6**
> 
> Le responsable IT demande un état des lieux rapide du serveur de fichiers. Léa lance `systeminfo` et note : Windows Server 2022, 32 Go de RAM, uptime de 45 jours, 12 hotfixes installés. Elle vérifie l’espace disque avec `Get-CimInstance Win32_LogicalDisk` : il reste 15 Go libres sur 500 — c’est peut-être la cause des problèmes.


-----


## Chapitre 11 — Processus

### Le minimum à savoir

#### Qu’est-ce qu’un processus ?

Un **processus** est un programme en cours d’exécution. Chaque fois que tu ouvres Chrome, Word, ou même le terminal, Windows crée un processus avec un numéro unique (le **PID** — Process ID).

#### Lister les processus

```cmd
REM CMD
tasklist                             REM Liste tous les processus
tasklist | findstr chrome            REM Filtrer par nom
```


```powershell
# PowerShell
Get-Process                          # Liste tous les processus
Get-Process chrome                   # Filtrer par nom
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id, @{N="RAM (Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 10
```


#### Arrêter un processus

```cmd
REM CMD
taskkill /PID 1234                   REM Arrêter par PID
taskkill /IM notepad.exe             REM Arrêter par nom
taskkill /PID 1234 /F                REM Forcer l'arrêt (/F = force)
```


```powershell
# PowerShell
Stop-Process -Id 1234                # Arrêter par PID
Stop-Process -Name notepad           # Arrêter par nom
```


> **⚠️ Attention :** arrêter un processus système peut rendre la machine instable. Ne tue que les processus que tu connais.

#### Point sécurité

Un processus peut être suspect si :

- Il a un nom inhabituel ou qui ressemble à un processus légitime (ex : `svchost.exe` dans un dossier autre que `System32`)
- Il consomme anormalement le CPU ou la RAM
- Il est lancé depuis un chemin inhabituel (`C:\Temp\`, `%APPDATA%\...`)
- Il ouvre des connexions réseau vers des adresses inconnues

> **Attention :** un chemin hors `System32` n’est pas automatiquement suspect. C’est seulement un indice à croiser avec le nom du processus, sa signature, son comportement réseau et son contexte.

```powershell
# Voir le chemin de l'exécutable d'un processus
Get-Process | Select-Object Name, Id, Path | Where-Object Path -notlike "*System32*"
```


> **📋 FIL ROUGE — Épisode 7**
> 
> Un poste est anormalement lent. Léa lance `tasklist` puis `Get-Process | Sort-Object CPU -Descending`. Un processus `update_service.exe` consomme 95% du CPU depuis `C:\Users\dupont\AppData\Local\Temp`. Suspect. Elle vérifie qu’il ne correspond à aucun logiciel connu, note le PID, et le tue avec `taskkill /PID 4567 /F`.


-----


## Chapitre 12 — Services Windows

### Le minimum à savoir

#### Qu’est-ce qu’un service ?

Un **service** est un programme qui tourne en arrière-plan, souvent sans fenêtre visible. Windows en a des dizaines : le pare-feu, Windows Update, le spooler d’impression, le DNS client, etc.

#### Lister les services

```cmd
REM CMD
sc query                             REM Services en cours d'exécution
sc query state= all                  REM Tous les services (attention : espace avant "all")
```


```powershell
# PowerShell
Get-Service                          # Tous les services
Get-Service | Where-Object Status -eq "Running"    # En cours d'exécution
Get-Service | Where-Object Status -eq "Stopped"    # Arrêtés
Get-Service -Name "wuauserv"         # Un service spécifique (Windows Update)
```


#### Démarrer / arrêter un service

```cmd
REM CMD                                              [🔑 Admin]
net start wuauserv                   REM Démarrer Windows Update
net stop wuauserv                    REM Arrêter Windows Update
```


```powershell
# PowerShell                                         [🔑 Admin]
Start-Service -Name wuauserv
Stop-Service -Name wuauserv
Restart-Service -Name wuauserv
```


#### Mode de démarrage

```powershell
# Voir le mode de démarrage d'un service              [🔑 Admin]
Get-Service wuauserv | Select-Object Name, Status, StartType

# Modifier (avec prudence)
Set-Service -Name wuauserv -StartupType Manual
```


#### Point sécurité

Les services sont importants en cybersécurité pour détecter :

- Un service inconnu qui tourne
- Un service récemment installé (Event ID 7045)
- Un mécanisme de **persistance** (un malware qui s’installe comme service pour redémarrer automatiquement)

> **📋 FIL ROUGE — Épisode 8**
> 
> Le spooler d’impression est arrêté — les utilisateurs ne peuvent plus imprimer. Léa vérifie avec `Get-Service Spooler`, constate qu’il est “Stopped”, le redémarre avec `Start-Service Spooler`, et vérifie qu’il passe bien en “Running”.


-----


## Chapitre 13 — Utilisateurs et groupes locaux

### Le minimum à savoir

#### Identifier l’utilisateur actuel

```cmd
whoami                               REM Affiche DOMAINE\utilisateur ou MACHINE\utilisateur
```


#### Lister les utilisateurs locaux

```cmd
REM CMD
net user                             REM Liste les comptes locaux
net user alice                       REM Détails d'un compte (dernière connexion, expiration...)
```


```powershell
# PowerShell
Get-LocalUser                        # Liste les comptes locaux
Get-LocalUser -Name "alice"          # Détails d'un compte
```


#### Lister les groupes locaux

```cmd
REM CMD
net localgroup                       REM Liste les groupes
net localgroup Administrators        REM Membres du groupe Administrators
```


```powershell
# PowerShell
Get-LocalGroup                       # Liste les groupes
Get-LocalGroupMember Administrators  # Qui est administrateur ?
```


> **Pourquoi c’est important :** savoir qui est dans le groupe **Administrators** est une question de sécurité fondamentale. Trop de comptes admin = surface d’attaque trop large.

#### Actions de modification (aperçu)

La création d’utilisateurs (`New-LocalUser`), l’ajout à des groupes (`Add-LocalGroupMember`), et la suppression sont des opérations d’administration qui nécessitent des droits élevés et de la prudence. Elles sont couvertes en détail dans les cours d’administration Windows et Active Directory.


-----


## Chapitre 14 — Tâches planifiées

### Le minimum à savoir

#### Qu’est-ce qu’une tâche planifiée ?

Une **tâche planifiée** (scheduled task) est une action programmée pour s’exécuter automatiquement :

- Au démarrage de la machine
- À la connexion d’un utilisateur
- À une heure précise (tous les jours à 2h du matin)
- Selon un événement (quand un log spécifique apparaît)

#### Pourquoi c’est important ?

- **Administration :** sauvegardes automatiques, maintenance, nettoyage
- **Sécurité :** les tâches planifiées sont un **mécanisme de persistance** classique — un malware peut créer une tâche pour se relancer au démarrage

#### Lister les tâches

```cmd
REM CMD
schtasks                             REM Liste toutes les tâches planifiées
schtasks /query /tn "NomDeLaTache"   REM Détails d'une tâche spécifique
```


```powershell
# PowerShell
Get-ScheduledTask                    # Toutes les tâches
Get-ScheduledTask | Select-Object TaskName, State -First 20
Get-ScheduledTask | Where-Object State -eq "Ready"    # Tâches actives
```


> **Astuce sécurité :** une tâche planifiée qui exécute un programme depuis `C:\Temp`, `%APPDATA%` ou un chemin inhabituel mérite une vérification.

> **Note :** la création et la suppression de tâches planifiées (`Register-ScheduledTask`, `Unregister-ScheduledTask`) sont des opérations d’administration couvertes dans le cours PowerShell.


-----


## Chapitre 15 — Le registre Windows

### Le minimum à savoir

#### Qu’est-ce que le registre ?

Le **registre Windows** est une base de données hiérarchique qui stocke la configuration de Windows, des applications et des utilisateurs. Tout y est : les paramètres d’affichage, les programmes au démarrage, les associations de fichiers, les politiques de sécurité…

#### Les ruches principales

|Ruche              |Abréviation|Contenu                                                    |
|-------------------|-----------|-----------------------------------------------------------|
|HKEY_LOCAL_MACHINE |`HKLM`     |Configuration de la machine (matériel, logiciels, services)|
|HKEY_CURRENT_USER  |`HKCU`     |Configuration de l’utilisateur connecté                    |
|HKEY_CLASSES_ROOT  |`HKCR`     |Associations de fichiers                                   |
|HKEY_USERS         |`HKU`      |Tous les profils utilisateurs                              |
|HKEY_CURRENT_CONFIG|`HKCC`     |Configuration matérielle actuelle                          |

#### L’éditeur graphique

```cmd
regedit                              REM Ouvre l'éditeur de registre (GUI)
```


#### Lire le registre avec CMD

```cmd
reg query HKCU                       REM Lister les sous-clés de HKCU
reg query "HKCU\Software"            REM Naviguer dans Software
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"    REM Programmes au démarrage
```


#### Lire le registre avec PowerShell

PowerShell traite le registre comme un système de fichiers (un PSDrive) :

```powershell
Get-ChildItem HKCU:\                 # Naviguer dans HKCU
Get-ChildItem HKCU:\Software         # Sous-clés de Software

# Les programmes qui se lancent au démarrage de l'utilisateur
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Les programmes qui se lancent au démarrage de la machine      [🔑 Admin]
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
```


> **Point sécurité :** les clés `Run` et `RunOnce` dans le registre sont l’un des mécanismes de persistance les plus courants. Un programme listé ici se lance automatiquement à chaque connexion ou démarrage.

#### Précaution

> **⚠️ Dans ce cours, on apprend à LIRE le registre.** La modification du registre peut casser une configuration Windows si elle est mal faite. La modification est un sujet d’administration avancé.


-----


## Chapitre 16 — Journaux Windows (Event Logs)

### Le minimum à savoir

#### Qu’est-ce qu’un journal d’événements ?

Windows enregistre en permanence ce qui se passe sur la machine dans des **journaux** (Event Logs). C’est l’équivalent des logs sous Linux. Chaque événement a un **Event ID** — un numéro qui identifie le type d’événement.

#### Les journaux principaux

|Journal                                     |Contenu                                                         |
|--------------------------------------------|----------------------------------------------------------------|
|**System**                                  |Événements système (services, drivers, démarrage)               |
|**Application**                             |Événements des applications                                     |
|**Security**                                |Connexions, déconnexions, accès aux ressources (nécessite admin)|
|**Windows PowerShell**                      |Activité PowerShell classique                                   |
|**Microsoft-Windows-PowerShell/Operational**|Activité PowerShell détaillée (Script Block Logging)            |

#### Lire les événements

```powershell
# Les 20 derniers événements du journal System
Get-WinEvent -LogName System -MaxEvents 20

# Les 20 derniers du journal Application
Get-WinEvent -LogName Application -MaxEvents 20

# Les 20 derniers du journal Security                           [🔑 Admin]
Get-WinEvent -LogName Security -MaxEvents 20

# Lister tous les journaux disponibles
Get-WinEvent -ListLog * | Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending -First 20
```


> **⚠️ Important :** toujours utiliser `-MaxEvents` pour limiter le nombre de résultats. Sans ça, PowerShell tente de charger TOUT le journal — ce qui peut être très long.

#### Filtrer les événements

```powershell
# Les erreurs parmi les 50 derniers événements du journal System
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object LevelDisplayName -eq "Error"

# Vraiment filtrer sur les dernières 24 heures (méthode efficace avec FilterHashtable)
Get-WinEvent -FilterHashtable @{
    LogName   = "System"
    Level     = 2                          # 2 = Error
    StartTime = (Get-Date).AddDays(-1)
}

# Filtrer par Event ID
Get-WinEvent -FilterHashtable @{LogName="Security"; Id=4625} -MaxEvents 10    # Échecs de connexion
```


> **Bonne pratique :** `-FilterHashtable` filtre **côté serveur** (au niveau du moteur d’événements Windows), bien plus performant que de tout récupérer puis filtrer avec `Where-Object`. Sur un journal volumineux, la différence peut être de plusieurs minutes. Microsoft recommande systématiquement cette approche pour `Get-WinEvent`.

> **Les niveaux d’événements (`Level`) :** `1` = Critical, `2` = Error, `3` = Warning, `4` = Information, `5` = Verbose.

#### Les Event IDs à connaître

|Event ID|Journal               |Signification                                     |
|--------|----------------------|--------------------------------------------------|
|4624    |Security              |Connexion réussie                                 |
|4625    |Security              |Échec de connexion                                |
|4720    |Security              |Création d’un compte utilisateur                  |
|7045    |System                |Installation d’un nouveau service                 |
|1102    |Security              |Journal de sécurité effacé (suspect !)            |
|4104    |PowerShell/Operational|Script Block Logging (contenu d’un script exécuté)|


> **📋 FIL ROUGE — Épisode 9**
> 
> Suspicion d’activité anormale sur un poste. Léa consulte les logs de sécurité : `Get-WinEvent -FilterHashtable @{LogName="Security"; Id=4625} -MaxEvents 20`. Elle trouve 47 échecs de connexion en 10 minutes sur le compte “admin” — c’est une tentative de brute-force. Elle note l’adresse IP source et remonte l’information à l’équipe sécurité.


-----


## Chapitre 17 — Réseau avec CMD et PowerShell

### Le minimum à savoir

C’est le chapitre le plus utilisé au quotidien. Les commandes réseau sont la raison n°1 pour laquelle beaucoup de gens ouvrent un terminal.

#### Configuration IP

```cmd
REM CMD
ipconfig                             REM Résumé (IP, masque, passerelle)
ipconfig /all                        REM Détail complet (DNS, DHCP, MAC...)
```


```powershell
# PowerShell
Get-NetIPAddress | Where-Object AddressFamily -eq "IPv4"
Get-NetIPConfiguration               # Configuration complète
Get-NetAdapter                       # Cartes réseau
```


#### Tester la connectivité

```cmd
REM CMD
ping 8.8.8.8                         REM Tester la connexion à une IP
ping google.com                      REM Tester la résolution DNS + la connexion
ping -n 1 8.8.8.8                    REM Un seul ping (par défaut : 4)
```


```powershell
# PowerShell
Test-Connection google.com           # Ping en objets
Test-Connection 8.8.8.8 -Count 1    # Un seul ping
```


#### Résolution DNS

```cmd
REM CMD
nslookup google.com                  REM Interroger le DNS
ipconfig /displaydns                 REM Voir le cache DNS local
ipconfig /flushdns                   REM Vider le cache DNS
```


```powershell
# PowerShell
Resolve-DnsName google.com
Get-DnsClientCache                   # Cache DNS
Clear-DnsClientCache                 # Vider le cache
```


#### Chemin réseau

```cmd
REM CMD
tracert google.com                   REM Tracer le chemin réseau
pathping google.com                  REM Ping + tracert combinés (plus lent, plus complet)
```


```powershell
# PowerShell
Test-NetConnection google.com -TraceRoute
```


#### Tester un port spécifique

```powershell
Test-NetConnection google.com -Port 443         # Le port 443 (HTTPS) est-il ouvert ?
Test-NetConnection serveur01 -Port 3389         # Le port RDP est-il accessible ?
```


#### Connexions actives

```cmd
REM CMD
netstat -ano                         REM Connexions actives avec PID
netstat -an                          REM Connexions sans résolution DNS (plus rapide)
```


```powershell
# PowerShell
Get-NetTCPConnection                 # Toutes les connexions TCP
Get-NetTCPConnection | Where-Object State -eq "Established"    # Connexions actives
```


#### Relier un port à un processus

```cmd
REM CMD : en deux étapes
netstat -ano                         REM 1. Trouver le PID qui utilise le port
tasklist | findstr 1234              REM 2. Trouver le nom du processus
```


```powershell
# PowerShell : en une seule commande
Get-NetTCPConnection | Select-Object LocalPort, RemoteAddress, State, OwningProcess |
    Where-Object LocalPort -eq 8080
Get-Process -Id 1234                 # Identifier le processus par son PID
```


#### Renouveler la configuration DHCP

```cmd
ipconfig /release                    REM Libérer l'adresse IP
ipconfig /renew                      REM Obtenir une nouvelle adresse
```


#### Pare-feu Windows (aperçu)

```powershell
# Voir les règles de pare-feu
Get-NetFirewallRule | Select-Object DisplayName, Direction, Action, Enabled -First 20
```


> **Note :** la création et la modification de règles de pare-feu (`New-NetFirewallRule`, etc.) sont des opérations d’administration avancées.

> **📋 FIL ROUGE — Épisode 10**
> 
> Le poste de l’utilisateur ne se connecte plus au réseau. Léa diagnostique pas à pas :
> 
> 1. `ipconfig` → l’IP est en 169.254.x.x (APIPA — pas de DHCP)
> 1. `ipconfig /renew` → timeout, pas de réponse du serveur DHCP
> 1. `ping 192.168.1.1` (passerelle) → pas de réponse
> 1. Vérification physique : le câble réseau était débranché. Problème résolu.


-----


## Chapitre 18 — Interagir avec le Web depuis la CLI

### Le minimum à savoir

#### Pourquoi interagir avec le web ?

- Tester l’accès à un site
- Télécharger un fichier
- Vérifier qu’un service web répond
- Diagnostiquer un problème de proxy ou de connectivité HTTPS

#### Avec `curl`

Windows 10/11 inclut `curl.exe`. Mais attention au piège : dans **Windows PowerShell 5.1**, `curl` (sans le `.exe`) est interprété comme un alias de `Invoke-WebRequest` — pas le vrai outil curl. Pour appeler explicitement le vrai `curl`, utilise toujours `curl.exe` :

```cmd
curl.exe https://example.com                           REM Récupérer le contenu d'une page
curl.exe -o page.html https://example.com              REM Télécharger dans un fichier
curl.exe -I https://example.com                        REM Voir les en-têtes HTTP seulement
```


> **Note :** dans PowerShell 7+, l’alias `curl` a été supprimé pour éviter cette confusion — `curl` y appelle bien le vrai `curl.exe`. Mais par sécurité, prends le réflexe d’écrire `curl.exe` partout.

#### Avec PowerShell

```powershell
Invoke-WebRequest https://example.com                  # Récupérer une page web
Invoke-WebRequest https://example.com -OutFile page.html   # Télécharger
(Invoke-WebRequest https://example.com).StatusCode     # Code HTTP (200 = OK)
```


#### Les codes HTTP à connaître

|Code     |Signification    |
|---------|-----------------|
|200      |OK — tout va bien|
|301 / 302|Redirection      |
|403      |Accès interdit   |
|404      |Page non trouvée |
|500      |Erreur serveur   |


-----
