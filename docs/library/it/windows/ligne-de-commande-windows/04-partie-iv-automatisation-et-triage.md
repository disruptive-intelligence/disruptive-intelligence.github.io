---
title: Partie IV — Automatisation et triage
source: IT/02_Windows/Windows_Command-Line.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - index.md
---

-----


## Chapitre 19 — Introduction aux scripts batch (.bat)

### Le minimum à savoir

#### Qu’est-ce qu’un fichier batch ?

Un fichier `.bat` (ou `.cmd`) contient des commandes CMD exécutées dans l’ordre, comme un script Bash. C’est la forme de scripting la plus ancienne sous Windows.

#### Premier fichier batch

Crée un fichier `info.bat` avec un éditeur de texte :

```batch
@echo off
echo === Informations systeme ===
echo.
echo Utilisateur : %USERNAME%
echo Machine     : %COMPUTERNAME%
echo Date        : %DATE%
echo Heure       : %TIME%
echo.
pause
```


Double-clique sur le fichier ou lance-le avec `.\info.bat` dans le terminal.

- `@echo off` : empêche l’affichage de chaque commande avant son exécution
- `echo.` : affiche une ligne vide
- `pause` : attend que l’utilisateur appuie sur une touche

#### Variables dans un batch

```batch
@echo off
set NOM=Lea
echo Bonjour %NOM% !

set /p AGE=Quel est ton age ?
echo Tu as %AGE% ans.
```


#### Arguments

```batch
@echo off
echo Premier argument : %1
echo Deuxieme argument : %2
echo Tous les arguments : %*
```


```cmd
info.bat Alice 25
```


#### Conditions simples

```batch
@echo off
if exist "C:\Temp\fichier.txt" (
    echo Le fichier existe.
) else (
    echo Le fichier n'existe pas.
)

if "%1"=="" (
    echo Erreur : donne un argument.
    exit /b 1
)
```


#### Boucle simple

```batch
@echo off
for f
```


> **Note :** dans un fichier batch, les variables de boucle utilisent ``, les guillemets)

- Pas de gestion d’erreurs structurée
- Pas d’objets, pas de modules
- Pas de filtrage avancé
- Difficilement lisible pour les scripts complexes

**PowerShell remplace le batch pour tout ce qui dépasse 10-15 lignes.** Le batch reste utile pour les scripts de démarrage, les tâches très simples, et la compatibilité avec des environnements anciens.


-----


## Chapitre 20 — Introduction à l’automatisation PowerShell

### Le minimum à savoir

Ce chapitre est une **passerelle** vers le cours PowerShell complet de la bibliothèque. On ne fait ici qu’effleurer le scripting.

#### Commande vs script

- Une **commande** s’exécute directement dans le terminal : `Get-Process`
- Un **script** est un fichier `.ps1` qui contient plusieurs commandes

#### Premier mini-script PowerShell

Crée un fichier `rapport.ps1` :

```powershell
# rapport.ps1 — Collecte rapide d'informations
Write-Host "=== Rapport systeme ===" -ForegroundColor Cyan

Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Date        : $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Output ""

Write-Host "[Top 5 processus par CPU]" -ForegroundColor Yellow
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5 | Format-Table

Write-Host "[Services arretes]" -ForegroundColor Yellow
Get-Service | Where-Object Status -eq "Stopped" | Select-Object Name, DisplayName -First 10 | Format-Table

Write-Host "[Espace disque]" -ForegroundColor Yellow
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, @{N="Libre (Go)";E={[math]::Round($_.FreeSpace/1GB)}} | Format-Table
```


#### Exécuter le script

```powershell
.\rapport.ps1
```


Si tu obtiens une erreur sur la politique d’exécution :

```powershell
Get-ExecutionPolicy                                    # Voir la politique actuelle
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser    # Autoriser les scripts locaux
```


> **Note :** le détail de la politique d’exécution, des variables, des boucles, des fonctions, de `param()`, du pipeline d’objets en profondeur — tout ça est couvert dans le **cours PowerShell** de la bibliothèque.

#### Exporter les résultats dans un fichier

```powershell
Get-Process | Out-File process.txt
Get-Service | Export-Csv services.csv -NoTypeInformation
```



-----


## Chapitre 21 — Sécurité et triage depuis la ligne de commande

### Le minimum à savoir

#### L’objectif du triage

Le **triage** consiste à collecter rapidement des informations sur une machine pour comprendre son état — est-elle saine ? Y a-t-il des indices de compromission ? C’est la première étape d’une investigation.

#### La collecte de base

```powershell
# Identité
whoami
hostname

# Réseau
ipconfig /all
netstat -ano

# Processus
tasklist
Get-Process

# Services
Get-Service

# Utilisateurs
net user
net localgroup Administrators

# Tâches planifiées
schtasks
Get-ScheduledTask

# Événements récents
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20    # [🔑 Admin]
```


#### Vérifier un fichier suspect

```powershell
# Hash du fichier (pour comparaison avec des bases d'IOC comme VirusTotal)
Get-FileHash "C:\Temp\suspect.exe" -Algorithm SHA256

# Signature numérique (signé par un éditeur de confiance ?)
Get-AuthenticodeSignature "C:\Temp\suspect.exe"

# Métadonnées (taille, dates de création/modification)
Get-Item "C:\Temp\suspect.exe" | Select-Object Name, Length, CreationTime, LastWriteTime
```


#### Vérifier les programmes au démarrage

```powershell
# Registre : clés Run
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# Tâches planifiées actives
Get-ScheduledTask | Where-Object State -eq "Ready" | Select-Object TaskName, TaskPath

# Services avec un chemin inhabituel
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -and $_.PathName -notlike "*System32*" -and $_.PathName -notlike "*SysWOW64*" } |
    Select-Object Name, State, PathName
```


#### Vérifier les connexions réseau suspectes

```powershell
# Connexions actives vers l'extérieur
Get-NetTCPConnection | Where-Object State -eq "Established" |
    Select-Object LocalPort, RemoteAddress, RemotePort, OwningProcess

# Identifier le processus derrière une connexion
Get-Process -Id (Get-NetTCPConnection | Where-Object RemotePort -eq 4444).OwningProcess

# Port `4444` souvent utilisé dans exemples de sécurité, mais port seul ne suffit jamais à conclure qu’une activité est malveillante. Elle fonctionne si une seule connexion correspond. Si plusieurs connexions correspondent, ou aucune, ça peut être moins propre. Préferer :

Get-NetTCPConnection | Where-Object RemotePort -eq 4444 |
ForEach-Object {
    Get-Process -Id $_.OwningProcess
}
```


#### Aperçu Sysinternals

Les **Sysinternals** sont une suite d’outils Microsoft gratuits, essentiels pour l’administration et l’investigation Windows :

|Outil               |Usage                                                                      |
|--------------------|---------------------------------------------------------------------------|
|**Autoruns**        |Voir TOUT ce qui se lance au démarrage (bien plus complet que les clés Run)|
|**Process Explorer**|Version améliorée du Gestionnaire des tâches                               |
|**TCPView**         |Voir les connexions réseau en temps réel par processus                     |
|**PsExec**          |Exécuter des commandes sur des machines distantes                          |


> **Note :** les Sysinternals sont des outils à part entière, pas des commandes PowerShell. Ils sont téléchargeables gratuitement sur [learn.microsoft.com/sysinternals](https://learn.microsoft.com/sysinternals).

> **📋 FIL ROUGE — Épisode 11**
> 
> Un fichier suspect `update_service.exe` a été trouvé sur un poste. Léa vérifie :
> 
> 1. `Get-FileHash` →  Elle vérifie le hash dans un outil de réputation ou une base IOC autorisée par son organisation. (Par exemple : Elle vérifie le hash sur VirusTotal, si la politique de l’organisation l’autorise) → 35 détections. C’est un malware.
> 2. `Get-AuthenticodeSignature` → “NotSigned”. Pas signé.
> 3. Elle vérifie les clés `Run` → le fichier est présent dans la clé de démarrage.
> 4. Elle vérifie `Get-NetTCPConnection` → le processus ouvre une connexion vers une IP étrangère sur le port 4444.
>    Conclusion : compromission confirmée. Elle isole le poste du réseau et remonte l’incident.


-----


## Chapitre 22 — PowerShell Remoting : aperçu

### Le minimum à savoir

#### Pourquoi administrer à distance ?

- 200 postes → on ne va pas se déplacer sur chaque machine
- Serveurs sans interface graphique (Server Core)
- Télétravail et intervention à distance
- Administration centralisée

#### Le principe

PowerShell Remoting (via **WinRM** — Windows Remote Management) permet d’exécuter des commandes PowerShell sur des machines distantes, comme SSH le fait sous Linux.

#### Les commandes à connaître

```powershell
# Ouvrir une session interactive sur une machine distante
Enter-PSSession -ComputerName SERVEUR01
# Tu es maintenant "sur" SERVEUR01 — les commandes s'exécutent là-bas
Exit-PSSession

# Exécuter une commande ponctuelle à distance
Invoke-Command -ComputerName SERVEUR01 -ScriptBlock { Get-Service }

# Exécuter sur PLUSIEURS machines en parallèle
Invoke-Command -ComputerName SERVEUR01, SERVEUR02, SERVEUR03 -ScriptBlock {
    hostname
    Get-CimInstance Win32_OperatingSystem | Select-Object Caption, LastBootUpTime
}
```

> **Important :** ces commandes ne fonctionnent que si PowerShell Remoting / WinRM est activé et autorisé sur la machine distante. En entreprise, cette configuration est souvent gérée par GPO ou par l’équipe infrastructure.
#### La sécurité du remoting

PowerShell Remoting s’appuie sur **WinRM** (Windows Remote Management).

- En environnement Active Directory, l’authentification se fait généralement avec **Kerberos** (le standard de sécurité Windows)
- Hors domaine, c’est **NTLM** par défaut, et il faut configurer manuellement la liste des hôtes de confiance (`TrustedHosts`)
- La communication peut passer en **HTTP** (par défaut, mais le contenu reste protégé entre machines de confiance) ou en **HTTPS** (recommandé pour les environnements sensibles, nécessite des certificats)
- Toute activité de remoting est journalisée dans les Event Logs

> **À retenir :** la configuration exacte dépend du contexte (domaine, workgroup, HTTP/HTTPS, TrustedHosts, certificats, GPO de sécurité). Dans un environnement professionnel, ces paramètres sont généralement gérés par l’équipe infrastructure.

> **Note :** la configuration avancée du remoting (JEA, CredSSP, certificats, TrustedHosts hors domaine) est un sujet d’administration avancé, couvert dans les cours d’infrastructure.


-----
