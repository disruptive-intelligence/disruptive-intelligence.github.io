---
title: Partie V — Labs, évaluation et synthèse
source: IT/02_Windows/Windows_Command-Line.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - index.md
---

-----


## Chapitre 23 — Labs progressifs

Ces labs sont conçus pour être exécutés directement dans ton terminal Windows.

### Lab 1 — Premiers pas

```cmd
whoami
hostname
ver
cd
dir
cls
```


### Lab 2 — Navigation

```cmd
cd %USERPROFILE%
dir
cd Desktop
cd ..
cd \
tree /f
```


```powershell
cd ~
Get-ChildItem
Get-ChildItem -Force
cd ..
```


### Lab 3 — Fichiers et dossiers CMD

```cmd
mkdir LabCMD
cd LabCMD
echo Bonjour Windows > test.txt
type test.txt
echo Deuxieme ligne >> test.txt
type test.txt
copy test.txt copie.txt
dir
del copie.txt
del test.txt
cd ..
rmdir LabCMD
```


### Lab 4 — Fichiers et dossiers PowerShell

```powershell
New-Item -ItemType Directory -Name "LabPS"
Set-Location LabPS
Set-Content test.txt "Bonjour PowerShell"
Get-Content test.txt
Add-Content test.txt "Deuxieme ligne"
Get-Content test.txt
Copy-Item test.txt copie.txt
Get-ChildItem
Remove-Item copie.txt
Set-Location ..
Remove-Item LabPS -Recurse
```


### Lab 5 — Variables d’environnement et PATH

```cmd
echo %USERNAME%
echo %USERPROFILE%
echo %TEMP%
echo %PATH%
where notepad
```


```powershell
$env:USERNAME
$env:USERPROFILE
$env:TEMP
$env:PATH
Get-Command notepad
```


### Lab 6 — Recherche

```cmd
mkdir LabRecherche
cd LabRecherche
echo "Tout va bien" > rapport1.txt
echo "Erreur critique" > rapport2.txt
echo "Tout va bien" > rapport3.txt
findstr "Erreur" *.txt
dir /s /b *.txt
```


```powershell
# (Reste dans le même dossier LabRecherche)
Select-String -Path *.txt -Pattern "Erreur"
Get-ChildItem -Filter *.txt
```


```cmd
REM Une fois les essais terminés, on nettoie
cd ..
rmdir /s LabRecherche
```


### Lab 7 — Réseau

```cmd
ipconfig /all
ping -n 2 8.8.8.8
ping -n 2 google.com
nslookup google.com
netstat -ano | findstr "ESTABLISHED"
```


```powershell
Test-NetConnection google.com -Port 443
Resolve-DnsName google.com
Get-NetTCPConnection | Where-Object State -eq "Established" | Select-Object -First 5
```


### Lab 8 — Processus et services

```cmd
tasklist | findstr "explorer"
```


```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10
Get-Service | Where-Object Status -eq "Running" | Measure-Object
Get-Service | Where-Object Status -eq "Stopped" | Select-Object Name -First 10
```


### Lab 9 — Utilisateurs et groupes

```cmd
whoami
net user
net localgroup
net localgroup Administrators
```


```powershell
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember Administrators
```


### Lab 10 — Tâches planifiées et registre

```powershell
Get-ScheduledTask | Select-Object TaskName, State -First 15
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
```


### Lab 11 — Journaux Windows

```powershell
Get-WinEvent -LogName System -MaxEvents 10 | Select-Object TimeCreated, LevelDisplayName, Message
Get-WinEvent -LogName Application -MaxEvents 10 | Select-Object TimeCreated, LevelDisplayName, Message
```


### Lab 12 — Mini collecte de triage

```powershell
$collecte = "$env:USERPROFILE\Collecte"
New-Item -ItemType Directory -Path $collecte -Force
Set-Location $collecte

whoami > identity.txt
hostname >> identity.txt
systeminfo > system.txt
ipconfig /all > network.txt
netstat -ano > connections.txt
tasklist > processes.txt
net user > users.txt
net localgroup Administrators > admins.txt

Get-Process | Out-File processes_ps.txt
Get-Service | Out-File services_ps.txt
Get-ScheduledTask | Out-File scheduled_tasks.txt
Get-WinEvent -LogName System -MaxEvents 20 | Out-File events_system.txt

Write-Host "Collecte terminee dans $collecte" -ForegroundColor Green
Get-ChildItem
```


> **Pourquoi `$env:USERPROFILE` plutôt que `C:\Temp` ?** Sur certains postes verrouillés, un utilisateur standard n’a pas le droit d’écrire à la racine de `C:\`. Utiliser le profil utilisateur (`C:\Users\TonNom\`) garantit que le lab fonctionne partout, sans droits admin.

-----


## Chapitre 24 — Skills Assessment — Évaluation finale

### Objectif

Tu dois être capable de créer un dossier de collecte et d’y stocker les résultats de commandes qui répondent aux questions ci-dessous.

### Consignes

```powershell
# Crée le dossier de collecte (dans ton profil utilisateur, pas besoin d'admin)
$assessment = "$env:USERPROFILE\WindowsCLI-Assessment"
New-Item -ItemType Directory -Path $assessment -Force
Set-Location $assessment
```


Utilise les commandes que tu as apprises pour répondre à chaque question et stocke les résultats dans des fichiers.

### Questions

1. **Quel utilisateur est connecté ?** Quel est son nom complet (DOMAINE\utilisateur ou MACHINE\utilisateur) ?
1. **Quel est le nom de la machine ?**
1. **Quelle est l’adresse IP de la machine ?** Quelle est sa passerelle par défaut ?
1. **Quels processus sont actifs ?** Lequel consomme le plus de CPU ?
1. **Quels services sont présents ?** Combien sont en cours d’exécution, combien sont arrêtés ?
1. **Quels utilisateurs locaux existent ?**
1. **Qui est administrateur local ?**
1. **Quelles tâches planifiées existent ?** Y en a-t-il dans un état inhabituel ?
1. **Quels événements système récents sont visibles ?** Y a-t-il des erreurs ?
1. **Quelle est la différence fondamentale entre CMD et PowerShell ?** (Réponse écrite, pas une commande.)

### Exemple de collecte attendue

```powershell
whoami > identity.txt
hostname >> identity.txt
systeminfo > system.txt
ipconfig /all > network.txt
tasklist > processes.txt
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10 | Out-File top_cpu.txt
Get-Service | Out-File services.txt
(Get-Service | Where-Object Status -eq "Running" | Measure-Object).Count | Out-File services_count.txt
net user > users.txt
net localgroup Administrators > admins.txt
Get-ScheduledTask | Out-File scheduled_tasks.txt
Get-WinEvent -LogName System -MaxEvents 30 | Out-File events_system.txt
Get-WinEvent -LogName System -MaxEvents 30 | Where-Object LevelDisplayName -eq "Error" | Out-File events_errors.txt
```


-----


## Chapitre 25 — Synthèse et boîte à outils du praticien

### Quand utiliser CMD ?

- Dépannage réseau rapide (`ipconfig`, `ping`, `tracert`, `netstat`)
- Compatibilité avec des environnements anciens
- Scripts batch existants
- Tâches très simples et ponctuelles

### Quand utiliser PowerShell ?

- Administration moderne (processus, services, utilisateurs, registre)
- Filtrage et tri avancés (`Where-Object`, `Sort-Object`, `Select-Object`)
- Export structuré (CSV, JSON)
- Collecte d’informations système (`Get-CimInstance`)
- Consultation des journaux (`Get-WinEvent`)
- Triage et investigation de sécurité
- Automatisation et scripting (→ cours PowerShell)

### Les prochaines étapes

|Cours de la bibliothèque       |Ce qu’il apporte                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------|
|**Cours PowerShell**           |Scripting avancé : variables, boucles, fonctions, param(), pipeline d’objets, automatisation|
|**Cours Active Directory**     |Administration d’un domaine Windows avec PowerShell                                         |
|**Cours Infrastructure IT**    |Architecture réseau, serveurs, virtualisation                                               |
|**Cours Windows en profondeur**|Internals Windows, sécurité, hardening                                                      |
|**Cours Digital Forensics**    |Investigation numérique (dont forensic Windows)                                             |
|**Cours Réponse à incident**   |Gestion d’un incident de sécurité de bout en bout                                           |

-----
