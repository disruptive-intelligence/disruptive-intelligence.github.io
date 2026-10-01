---
title: Chapitre 12 — Le registre Windows
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration Windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### Qu'est-ce que le registre ?

Le registre est la **base de données de configuration** de Windows. On y trouve les réglages du système, des logiciels, des associations de fichiers, des politiques de sécurité, et — ce qui intéressera la Partie VIII — des mécanismes de démarrage automatique.

PowerShell traite le registre **comme un système de fichiers** : mêmes cmdlets que pour les dossiers.

### Les ruches principales

```powershell
Get-PSDrive -PSProvider Registry    # les "lecteurs" du registre
```


| Ruche | Abréviation | Contenu |
|-------|-------------|---------|
| `HKEY_CURRENT_USER` | `HKCU:` | Configuration de l'utilisateur **courant** |
| `HKEY_LOCAL_MACHINE` | `HKLM:` | Configuration de la **machine** (nécessite `[🔑 Admin]` pour écrire) |

### Lire le registre

```powershell
# Parcourir comme un dossier
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion"

# Lire TOUTES les valeurs d'une clé
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"

# Lire UNE valeur précise
Get-ItemPropertyValue "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName
```


> **📌 Réflexe `Test-Path` :** avant de lire ou d'écrire, `Test-Path "HKLM:\SOFTWARE\MonApp"` évite les erreurs sur une clé absente.

### Le concept de PSDrive : une abstraction unifiée

Le registre est un exemple de **PSDrive** — PowerShell présente plusieurs systèmes comme des « lecteurs » navigables avec les **mêmes** cmdlets (`Get-ChildItem`, `Get-ItemProperty`…) :

| PSDrive | Contenu |
|---------|---------|
| `C:`, `D:` | Système de fichiers |
| `HKCU:`, `HKLM:` | Registre |
| `Env:` | Variables d'environnement |
| `Cert:` | Certificats |
| `Variable:` | Variables PowerShell |

```powershell
Get-ChildItem Env:                       # toutes les variables d'environnement
Get-ChildItem Cert:\CurrentUser\My       # tes certificats personnels
```


C'est une idée puissante : apprendre `Get-ChildItem` une fois, l'utiliser partout.

### Modifier le registre `[🔑 Admin pour HKLM]`

**Discipline `Test`/`Get` avant `Set`/`New`** — et prudence maximale :

```powershell
# Créer une clé (si absente)
if (-not (Test-Path "HKCU:\Software\MonApp")) {
    New-Item -Path "HKCU:\Software\MonApp" -Force
}

# Créer une valeur avec son type explicite
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "dark" -PropertyType String
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Version" -Value 2 -PropertyType DWord

# Modifier une valeur existante
Set-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "light"

# Supprimer
Remove-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme"
Remove-Item -Path "HKCU:\Software\MonApp" -Recurse
```


Les types de valeurs courants : `String`, `DWord` (entier 32 bits), `QWord` (64 bits), `Binary`, `ExpandString`, `MultiString`.

> **⚠️ Le registre est critique — prudence maximale.** Une mauvaise modification de `HKLM:` peut empêcher Windows de démarrer. Règles de survie : travaille d'abord dans `HKCU:` (moins dangereux), **sauvegarde** la clé avant modification (`reg export`), et ne touche à `HKLM:` que si tu sais exactement ce que tu fais. `New-ItemProperty` pour créer (avec `-PropertyType`), `Set-ItemProperty` pour modifier.

## 🟡 Très utile en pratique

### Sauvegarder avant de modifier

```powershell
# Exporter une clé avant de la toucher (via l'outil reg.exe)
reg export "HKLM\SOFTWARE\MonApp" "C:\backup\MonApp.reg" /y
```


C'est le `Get`/backup avant `Set` appliqué au registre. Indispensable en production.

### Lire une information de configuration système

```powershell
# Version précise de Windows depuis le registre
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild
```


## 🔴 Bonus

### Les clés de démarrage automatique

Certaines clés lancent des programmes au démarrage — utile à connaître pour l'admin, essentiel pour la sécurité (persistance de malware, Ch.34) :

```powershell
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
```


> **Renvoi croisé :** on réutilise exactement ces clés `Run`/`RunOnce` au **Ch.34** pour le triage de persistance. Ici on les lit comme configuration ; là-bas on les analyse comme indicateur de compromission.

## ❌ Erreur classique

```powershell
# Écrire dans HKLM sans droits admin
Set-ItemProperty "HKLM:\..." -Name X -Value 1     # ❌ Accès refusé
# → console en administrateur

# Confondre New-ItemProperty (créer) et Set-ItemProperty (modifier)
Set-ItemProperty "HKCU:\Software\MonApp" -Name Nouveau -Value 1   # crée quand même,
# mais sans contrôle du type → préférer New-ItemProperty -PropertyType pour créer

# Modifier le registre sans sauvegarde
Set-ItemProperty "HKLM:\..."                       # ❌ sans filet
reg export "HKLM\..." backup.reg /y ; Set-ItemProperty ...   # ✅
```


## 💡 Exercices

**Guidé :** Lis et affiche `ProductName`, `DisplayVersion` et `CurrentBuild` depuis `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion`.

**Autonome :** Écris un script qui crée une clé `HKCU:\Software\MonLab`, y ajoute une valeur `String` et une valeur `DWord`, les relit pour vérifier, puis supprime la clé entière. Encadre chaque étape d'un `Test-Path`.

## ✅ Tu sais maintenant...

- Ce qu'est le registre et ses ruches (`HKCU:`, `HKLM:`)
- Le lire (`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`)
- Le modifier (`New-ItemProperty` pour créer avec type, `Set-ItemProperty` pour modifier)
- Le concept unificateur de **PSDrive** (fichiers, registre, Env:, Cert:…)
- La prudence : `HKCU:` d'abord, sauvegarde avant `HKLM:`

## 💬 Questions d'entretien typiques

- **Comment PowerShell voit-il le registre ?** → Comme un système de fichiers (un PSDrive), navigable avec `Get-ChildItem`, `Get-ItemProperty`…
- **Différence `HKCU:` / `HKLM:` ?** → `HKCU:` = config de l'utilisateur courant ; `HKLM:` = config machine, écriture réservée aux administrateurs.
- **`New-ItemProperty` ou `Set-ItemProperty` ?** → `New-ItemProperty` pour créer une valeur (avec `-PropertyType`), `Set-ItemProperty` pour en modifier une existante.

---
