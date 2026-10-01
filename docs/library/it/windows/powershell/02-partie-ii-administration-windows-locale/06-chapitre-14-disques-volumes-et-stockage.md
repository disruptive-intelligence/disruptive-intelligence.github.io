---
title: Chapitre 14 — Disques, volumes et stockage
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration Windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### Les trois niveaux : disque, partition, volume

Le stockage Windows s'empile en trois couches, et les cmdlets suivent cette logique :

- **Disque** (`Get-Disk`) : le matériel physique (ou virtuel)
- **Partition** (`Get-Partition`) : une division d'un disque
- **Volume** (`Get-Volume`) : un système de fichiers monté, souvent avec une lettre (`C:`, `D:`)

```powershell
Get-Disk                     # les disques physiques
Get-Partition                # les partitions
Get-Volume                   # les volumes (avec espace libre !)
```


> **📌 Réflexe `Get-Member` :** `Get-Volume | Get-Member` révèle `DriveLetter`, `FileSystemLabel`, `Size`, `SizeRemaining`, `HealthStatus`. C'est `Get-Volume` qu'on utilise le plus, car il donne directement l'espace libre.

### Le cas d'usage n°1 : surveiller l'espace disque

C'est l'une des vérifications les plus fréquentes en administration. Un disque plein = services qui tombent, logs qui ne s'écrivent plus, serveur en panne.

```powershell
Get-Volume | Where-Object DriveLetter |
    Select-Object DriveLetter, FileSystemLabel,
        @{N="TailleGB";E={[math]::Round($_.Size/1GB,1)}},
        @{N="LibreGB";E={[math]::Round($_.SizeRemaining/1GB,1)}},
        @{N="Libre%";E={[math]::Round($_.SizeRemaining/$_.Size*100,1)}}
```


### Alerter sous un seuil

```powershell
$SeuilGB = 20

Get-Volume | Where-Object { $_.DriveLetter -and ($_.SizeRemaining/1GB) -lt $SeuilGB } |
    ForEach-Object {
        Write-Host "ALERTE $($_.DriveLetter): $([math]::Round($_.SizeRemaining/1GB,1)) Go libres" -ForegroundColor Red
    }
```


### `Get-PSDrive` : la vue rapide

`Get-PSDrive` donne une vue synthétique (et couvre aussi les lecteurs réseau) :

```powershell
Get-PSDrive -PSProvider FileSystem |
    Select-Object Name,
        @{N="LibreGB";E={[math]::Round($_.Free/1GB,1)}},
        @{N="UtiliséGB";E={[math]::Round($_.Used/1GB,1)}}
```


## 🟡 Très utile en pratique

### Santé des disques

```powershell
Get-Disk | Select-Object Number, FriendlyName, HealthStatus, OperationalStatus,
    @{N="TailleGB";E={[math]::Round($_.Size/1GB)}}
```


`HealthStatus` (`Healthy`/`Warning`/`Unhealthy`) est un indicateur de défaillance matérielle à surveiller.

### Intégrer l'espace disque à la fiche du poste

Souviens-toi de `Get-PosteInfo.ps1` (Ch.2). On peut maintenant y ajouter le disque :

```powershell
$c = Get-Volume -DriveLetter C
"Disque C: : $([math]::Round($c.SizeRemaining/1GB,1)) Go libres sur $([math]::Round($c.Size/1GB,1)) Go"
```


## 🔴 Bonus `[🖥️ Server]`

### Création de partitions et formatage

Sur un serveur, on peut initialiser et partitionner un nouveau disque — opérations **destructives**, à manier avec une extrême prudence :

```powershell
# Exemple (DESTRUCTIF) : initialiser le disque 1, créer une partition, formater
# Initialize-Disk -Number 1 -PartitionStyle GPT
# New-Partition -DiskNumber 1 -UseMaximumSize -AssignDriveLetter |
#     Format-Volume -FileSystem NTFS -NewFileSystemLabel "Data"
```


> **⚠️ `Format-Volume` et `Initialize-Disk` effacent les données.** Vérifie **trois fois** le numéro de disque (`Get-Disk`) avant. Une erreur de numéro formate le mauvais disque.

## ❌ Erreur classique

```powershell
# Confondre Size (octets) et affichage en Go (oubli de la division)
$v.Size            # ❌ un énorme nombre en octets
$v.Size / 1GB      # ✅ en gigaoctets

# Filtrer les volumes sans lettre (partitions système)
Get-Volume | Select DriveLetter, SizeRemaining    # ⚠️ inclut des volumes sans lettre
Get-Volume | Where-Object DriveLetter | ...        # ✅ seulement les volumes montés

# Se tromper de numéro de disque avant un formatage
Format-Volume ...    # ❌❌ vérifier Get-Disk avant, TOUJOURS
```


## 💡 Exercices

**Guidé :** Affiche tous les volumes avec lettre, leur taille, leur espace libre en Go et le pourcentage libre.

**Autonome :** Écris un script `-SeuilGB` (défaut 20) qui liste les volumes sous le seuil et renvoie un PSCustomObject par volume concerné (Lecteur, LibreGB, Pourcent). Exporte en CSV si au moins un volume est en alerte.

---

## Rôles, fonctionnalités et logiciels

Cette section clôt la Partie II en abordant l'inventaire du logiciel installé — côté client comme côté serveur.

### Rôles et fonctionnalités Windows Server `[🖥️ Server]`

Sur **Windows Server**, les capacités s'ajoutent sous forme de **rôles** (AD DS, DNS, DHCP, File Server…) et **fonctionnalités**. On les gère avec le module `ServerManager` :

```powershell
Get-WindowsFeature                                   # tout, avec l'état Installed/Available
Get-WindowsFeature | Where-Object Installed          # ce qui est installé
Install-WindowsFeature -Name DNS -IncludeManagementTools    # installer le rôle DNS  [🔑 Admin]
```


> **Important :** `Get-WindowsFeature` / `Install-WindowsFeature` n'existent **que sur Windows Server**, pas sur Windows 10/11. C'est ainsi qu'on installe les rôles qu'on administrera en Parties IV et V (AD, DNS, DHCP…).

### Fonctionnalités sur Windows 10/11

Côté **client**, l'équivalent passe par d'autres cmdlets :

```powershell
Get-WindowsOptionalFeature -Online                          # fonctionnalités optionnelles
Get-WindowsOptionalFeature -Online -FeatureName *Hyper-V*   # rechercher
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All   # activer  [🔑 Admin]
```


C'est ainsi qu'on active, par exemple, Hyper-V ou le client OpenSSH sur un poste.

### Inventorier les logiciels installés — SANS `Win32_Product`

Question fréquente : « quels logiciels sont installés ? ». La tentation est d'utiliser `Get-CimInstance Win32_Product`. **À éviter absolument.**

> **⚠️ Ne JAMAIS utiliser `Win32_Product` pour un inventaire.** Interroger cette classe déclenche, pour **chaque** logiciel MSI, une vérification de cohérence (une réparation à blanc) — c'est **lent** et surtout ça peut générer des milliers d'événements et **relancer des installations**. C'est un piège classique qui a causé de vrais incidents en production.

La bonne méthode : lire les clés de désinstallation du registre.

```powershell
$chemins = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

Get-ItemProperty $chemins -ErrorAction SilentlyContinue |
    Where-Object DisplayName |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Sort-Object DisplayName
```


Cette approche est **rapide et sûre** pour inventorier les applications **desktop enregistrées au niveau machine**, en 32 comme en 64 bits (grâce à `WOW6432Node`). C'est celle qu'utilisent les vrais outils d'inventaire.

> **Ce qu'elle ne couvre pas.** Deux angles morts à connaître : les logiciels installés **par utilisateur** (clé `HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*`, à ajouter si besoin), et les applications **AppX/MSIX** (applications du Microsoft Store et applications modernes), qui ont leur propre mécanisme d'inventaire :
> ```powershell
> Get-AppxPackage | Select-Object Name, Version, PackageFullName
> ```
> Un inventaire réellement exhaustif combine donc les clés `Uninstall` (machine + utilisateur) et `Get-AppxPackage`.

## ✅ Tu sais maintenant...

- Les trois couches disque / partition / volume et leurs cmdlets
- Surveiller l'espace disque et alerter sous un seuil (le cas d'usage n°1)
- Vérifier la santé des disques (`HealthStatus`)
- Installer des rôles/fonctionnalités (`Install-WindowsFeature` sur **Server** uniquement)
- Inventorier les logiciels **via le registre**, jamais avec `Win32_Product`

## 💬 Questions d'entretien typiques

- **Comment vérifier l'espace disque libre ?** → `Get-Volume` (propriété `SizeRemaining`) ou `Get-PSDrive`, avec un calcul en Go.
- **Pourquoi éviter `Win32_Product` ?** → Son interrogation déclenche une vérification/réparation de chaque MSI : lent et potentiellement perturbant. On lit plutôt les clés `Uninstall` du registre.
- **Où installe-t-on un rôle comme DNS ou AD DS ?** → Sur Windows Server, avec `Install-WindowsFeature` (indisponible sur les clients).

## 🧩 Capstone Partie II — Boîte à outils du poste local

Assemble un script `Get-LocalHealthReport.ps1` qui produit un rapport complet du poste, en réutilisant toute la Partie II :

- Infos système (Ch.2) et espace disque (Ch.14)
- Services critiques et leur conformité (Ch.11)
- Comptes administrateurs locaux (Ch.10)
- Tâches planifiées non-Microsoft (Ch.13)
- Le tout structuré en PSCustomObject, exporté en CSV, avec un résumé coloré à l'écran, et robuste aux erreurs (`try/catch`, Ch.8)

C'est la version « poste local » de l'outil que tu enrichiras avec le réseau (Partie III) puis l'exécution distante (Partie VI).

---
