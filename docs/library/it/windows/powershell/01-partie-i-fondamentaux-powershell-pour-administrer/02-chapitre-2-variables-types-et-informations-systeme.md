---
title: Chapitre 2 — Variables, types et informations système
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable est un **conteneur nommé**. En PowerShell, le nom commence **toujours** par `$` — à la création comme à l'utilisation :

```powershell
$Prenom = "Alice"
$Age = 25
$EstAdmin = $true
```


> **Comparaison :** en Bash, `$` seulement à l'utilisation (`prenom="Alice"` puis `echo $prenom`). En Python, jamais de `$`. En PowerShell, **toujours** `$`.

Les petits exemples abstraits comme ci-dessus servent à poser une première idée. Mais on va vite les relier à Windows — c'est là que PowerShell devient concret :

```powershell
$Utilisateur = $env:USERNAME
$Machine     = $env:COMPUTERNAME
$OS          = Get-CimInstance Win32_OperatingSystem

Write-Output "Connecté en tant que $Utilisateur sur $Machine"
Write-Output "Système : $($OS.Caption)"
```


Ici, `$OS` ne contient pas un simple texte : c'est un **objet** riche décrivant le système, dont on lira les propriétés (`.Caption`, `.Version`, `.LastBootUpTime`…). On explore comment au Ch.4.

### Les types de données

PowerShell détecte le type automatiquement, mais tu peux le forcer :

| Type | Notation | Exemple |
|------|----------|---------|
| Texte | `[string]` | `"SRV01"` |
| Entier | `[int]` | `25` |
| Décimal | `[double]` | `1.75` |
| Booléen | `[bool]` | `$true`, `$false` |
| Date | `[datetime]` | `Get-Date` |

```powershell
# Vérifier le type d'une variable
$Machine.GetType().Name          # String
(Get-Date).GetType().Name        # DateTime

# Forcer une conversion
[int]$Nombre = "42"              # le texte "42" devient l'entier 42
```


Forcer le type est utile en administration : quand tu attends un nombre de jours, un seuil d'espace disque, etc., tu veux un `[int]`, pas du texte.

### Afficher : `Write-Output` vs `Write-Host`

```powershell
Write-Output "Bonjour"    # Envoie dans le pipeline (capturable, redirigeable)
Write-Host   "Bonjour"    # Écrit directement à l'écran
```


La différence concrète :

```powershell
$r = Write-Output "Hello"
$r                         # → "Hello" (capturé)

$r = Write-Host "Hello"    # "Hello" s'affiche, mais...
$r                         # → (vide, rien n'a été capturé)
```


> **Règle :** dans un script, produis tes **données** avec `Write-Output` (ou simplement en laissant l'objet « tomber » dans le pipeline). Réserve `Write-Host` aux **messages destinés à l'humain** (état, couleurs) — jamais aux données que tu voudras réutiliser.

> **Note version :** longtemps, `Write-Host` a eu mauvaise réputation car son texte « disparaissait » (impossible à capturer/rediriger). Depuis PowerShell 5+, `Write-Host` écrit en réalité dans un flux dédié (*Information stream*) et peut être capturé via `6>`. En pratique la règle ne change pas : **données → `Write-Output`, messages → `Write-Host`**.

### L'interpolation de chaînes

Guillemets **doubles** → les variables sont interprétées. Guillemets **simples** → texte littéral.

```powershell
$Machine = "SRV01"
Write-Output "Serveur : $Machine"     # → Serveur : SRV01
Write-Output 'Serveur : $Machine'     # → Serveur : $Machine
```


Pour insérer une **propriété** ou une **expression**, encadre avec `$(...)` :

```powershell
Write-Output "OS : $($OS.Caption)"
Write-Output "Uptime calculé le $(Get-Date)"
```


> **Piège classique :** `"$OS.Caption"` affiche l'objet suivi du texte `.Caption` — pas ce que tu veux. Il faut `"$($OS.Caption)"`. Retiens : dès qu'il y a un point (une propriété) ou un calcul, encadre avec `$(...)`.

### Saisie utilisateur avec `Read-Host`

```powershell
$NomServeur = Read-Host "Nom du serveur à vérifier"
Write-Output "Vérification de $NomServeur..."
```


Par défaut, `Read-Host` renvoie **du texte** (une chaîne). Si tu attends un nombre, convertis :

```powershell
[int]$Seuil = Read-Host "Seuil d'espace disque libre (Go)"
```


> **Une exception au « texte » :** avec l'option `-AsSecureString`, `Read-Host` masque la saisie et renvoie un **`SecureString`**, pas une chaîne. C'est la façon correcte de demander un mot de passe — on la retrouvera aux Ch.10, 20 et 33.

> **Bonne pratique d'admin :** `Read-Host` rend un script **interactif**, donc **non automatisable**. Pour un vrai script d'administration, on préfère les **paramètres** (Ch.3), qui permettent de lancer le script sans intervention humaine. On garde `Read-Host` pour les confirmations ponctuelles.

### Les variables automatiques utiles

```powershell
$true / $false / $null       # Booléens et absence de valeur
$HOME                        # Dossier personnel
$PWD                         # Dossier courant
$PSVersionTable              # Version de PowerShell (.PSVersion)
$env:USERNAME                # Utilisateur courant
$env:COMPUTERNAME            # Nom de la machine
$env:USERPROFILE             # Profil utilisateur
$?                           # La dernière commande a-t-elle réussi ? (True/False)
$LASTEXITCODE                # Code de sortie du dernier programme externe
```


Les variables `$env:` exposent les **variables d'environnement** Windows — équivalent de `$USER`, `$HOME` en Bash. On y accède aussi via le PSDrive `Env:` (`Get-ChildItem Env:`), qu'on verra au Ch.12.

## 🟡 Très utile en pratique

### `Write-Host` en couleurs (pour les messages d'état)

```powershell
Write-Host "Service actif"   -ForegroundColor Green
Write-Host "Service arrêté"  -ForegroundColor Red
Write-Host "Attention"       -ForegroundColor Yellow
```


Idéal pour un rapport lisible à l'écran — mais rappelle-toi : ce sont des messages, pas des données.

### Interroger le système avec `Get-CimInstance`

`Get-CimInstance` est **la** porte d'entrée vers les informations système (via la couche CIM/WMI de Windows). Il renvoie des objets riches :

```powershell
# Système d'exploitation
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, LastBootUpTime

# Matériel
Get-CimInstance Win32_ComputerSystem |
    Select-Object Manufacturer, Model, TotalPhysicalMemory

# Calculer l'uptime (depuis le dernier démarrage)
$os = Get-CimInstance Win32_OperatingSystem
(Get-Date) - $os.LastBootUpTime
```


> **📌 Réflexe `Get-Member` :** tu ne sais pas quelles propriétés existent ? `Get-CimInstance Win32_OperatingSystem | Get-Member` te les liste toutes. C'est **toujours** la bonne première étape face à un objet inconnu.

> **Note version :** `Get-CimInstance` (moderne) remplace l'ancien `Get-WmiObject`. **`Get-WmiObject` n'existe plus du tout dans PowerShell 7** — utilise `Get-CimInstance` partout, il fonctionne en 5.1 comme en 7.

## 🔴 Bonus

### Les méthodes .NET

Chaque objet PowerShell est un objet .NET. Tu peux appeler des méthodes .NET directement :

```powershell
[math]::Round(3.14159, 2)               # 3.14
[math]::Round($os.FreePhysicalMemory/1MB, 2)
[System.Environment]::OSVersion         # Version de l'OS
```


Pas indispensable pour débuter, mais c'est ce qui donne à PowerShell sa profondeur.

## ❌ Erreur classique

```powershell
# Oublier le $
Machine = "SRV01"        # ❌
$Machine = "SRV01"       # ✅

# Interpoler une propriété sans $()
"OS : $OS.Caption"       # ❌ affiche l'objet puis ".Caption"
"OS : $($OS.Caption)"    # ✅

# Oublier de convertir une saisie numérique
$Seuil = Read-Host "Seuil"
$Seuil + 1               # ❌ concaténation de texte ("101" au lieu de 11)
[int]$Seuil = Read-Host "Seuil"   # ✅
```


## 💡 Exercices

**Guidé :** Crée `fiche.ps1` qui stocke `$env:COMPUTERNAME`, `$env:USERNAME` et `Get-Date` dans des variables, puis les affiche proprement.

**Autonome :** Récupère l'objet `Get-CimInstance Win32_OperatingSystem` dans une variable `$os` et affiche sa version (`.Version`) et sa date de dernier démarrage (`.LastBootUpTime`) via l'interpolation `$(...)`.

## 🧩 Mini-projet — Fiche d'identité du poste

Crée `Get-PosteInfo.ps1` qui affiche une fiche claire :

```
=== Fiche du poste ===
Machine     : <COMPUTERNAME>
Utilisateur : <USERNAME>
OS          : <Caption> <Version>
RAM totale  : <Go>
PowerShell  : <version>
Démarré le  : <LastBootUpTime>
```


Utilise `$env:`, `Get-CimInstance Win32_OperatingSystem` et `Win32_ComputerSystem`, `$PSVersionTable.PSVersion`, l'interpolation `$(...)` et `Write-Host` en couleurs pour le titre. (On étoffera cette fiche au fil du cours — disque au Ch.14, IP au Ch.15.)

## ✅ Tu sais maintenant...

- Créer une variable avec `$`, forcer un type
- La différence `Write-Output` (données) / `Write-Host` (messages)
- L'interpolation, et le piège `$($objet.Propriété)`
- Lire une saisie avec `Read-Host` — et pourquoi les paramètres sont préférables
- Les variables automatiques (`$env:`, `$?`, `$LASTEXITCODE`…)
- Interroger le système avec `Get-CimInstance` (et que `Get-WmiObject` est mort en PS7)

## 💬 Questions d'entretien typiques

- **`Write-Output` ou `Write-Host` pour un résultat réutilisable ?** → `Write-Output` : il va dans le pipeline et peut être capturé. `Write-Host` sert aux messages destinés à l'humain.
- **Comment récupérer la version de l'OS d'une machine ?** → `Get-CimInstance Win32_OperatingSystem` puis lire `.Caption` / `.Version`. `Get-WmiObject` est l'ancêtre, absent de PowerShell 7.
- **Pourquoi préférer des paramètres à `Read-Host` ?** → Pour rendre le script automatisable (planifiable, appelable en masse) au lieu d'exiger une saisie humaine.

---
