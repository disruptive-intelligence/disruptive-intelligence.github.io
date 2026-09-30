---
title: PARTIE I — FONDAMENTAUX POWERSHELL POUR ADMINISTRER WINDOWS
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 1
chapters: 8
---

Cette partie pose les fondations du langage. Mais dès le premier chapitre, on manipule de vraies commandes d'administration Windows : l'idée n'est pas d'apprendre des concepts abstraits, c'est d'apprendre PowerShell **en regardant ce qui se passe sur une vraie machine**.

---


## Chapitre 1 — PowerShell dans l'écosystème Windows

### 🟢 Le minimum à savoir

#### Qu'est-ce que PowerShell ?

PowerShell est **trois choses à la fois** :

1. **Un terminal (un shell)** — tu tapes des commandes, il les exécute
2. **Un langage de scripting** — tu écris des scripts pour automatiser
3. **Un outil d'administration Windows** — tu pilotes services, processus, utilisateurs, registre, réseau, Active Directory…

C'est ce troisième point qui nous intéresse le plus. Tout ce que tu peux faire dans les interfaces graphiques de Windows (le Gestionnaire des tâches, les Services, l'Observateur d'événements, la console AD…), tu peux le faire en PowerShell — plus vite, de façon reproductible, et surtout **automatisable** et applicable à **des centaines de machines à la fois**.

#### Un aperçu de ce qu'on va pouvoir faire

Avant même d'apprendre la syntaxe, tape ces commandes pour voir la puissance de l'outil. Ne cherche pas encore à tout comprendre — c'est une bande-annonce :

```powershell
Get-Service                     # Tous les services Windows et leur état
Get-Process                     # Tous les programmes en cours d'exécution
Get-ComputerInfo                # Une fiche complète de la machine
Get-CimInstance Win32_OperatingSystem   # Infos sur le système d'exploitation
Get-NetIPAddress                # Les adresses IP de la machine
```

Chacune de ces commandes t'a renvoyé des informations structurées. C'est le cœur de PowerShell, et on va apprendre à l'exploiter méthodiquement.

#### La convention Verbe-Nom

Toutes les commandes PowerShell (les **cmdlets**) suivent le même pattern : **`Verbe-Nom`**.

| Verbe | Signification | Exemples d'administration |
|-------|--------------|--------------------------|
| `Get` | Obtenir, lire | `Get-Service`, `Get-Process`, `Get-ADUser` |
| `Set` | Modifier, configurer | `Set-Service`, `Set-ADUser` |
| `New` | Créer | `New-LocalUser`, `New-ADUser`, `New-Item` |
| `Remove` | Supprimer | `Remove-Item`, `Remove-ADUser` |
| `Start` / `Stop` | Démarrer / arrêter | `Start-Service`, `Stop-Process` |
| `Restart` | Redémarrer | `Restart-Service`, `Restart-Computer` |
| `Test` | Vérifier | `Test-Path`, `Test-Connection`, `Test-NetConnection` |
| `Enable` / `Disable` | Activer / désactiver | `Enable-ADAccount`, `Disable-LocalUser` |

C'est la grande force de PowerShell : la convention est **prédictible**. Tu ne connais pas la commande pour lister les services ? Essaie `Get-Service`. Pour en arrêter un ? `Stop-Service`. Pour changer sa configuration ? `Set-Service`. Ça marche presque toujours.

> **Comparaison avec Bash :** en Bash, les noms sont courts et souvent cryptiques (`ls`, `ps`, `grep`, `awk`). En PowerShell, ils sont longs mais explicites. C'est plus verbeux à taper, mais tu **devines** la commande au lieu de la mémoriser — un énorme avantage quand tu débutes.

> **La discipline `Get` d'abord :** remarque que la moitié des verbes ci-dessus ne font que **lire** (`Get`, `Test`). C'est voulu. En administration, on regarde toujours avant de modifier. On y reviendra sans cesse.

#### Les 3 commandes pour tout découvrir

Ces trois cmdlets sont ta porte d'entrée vers tout le reste de PowerShell. Retiens-les avant tout :

```powershell
# 1. TROUVER une commande
Get-Command *Service*        # Toutes les cmdlets contenant "Service"
Get-Command -Verb Get        # Toutes les cmdlets qui commencent par "Get"
Get-Command -Noun ADUser     # Toutes les cmdlets qui agissent sur "ADUser"

# 2. COMPRENDRE une commande
Get-Help Get-Service                 # L'aide
Get-Help Get-Service -Examples       # Des exemples concrets (le plus utile !)
Get-Help Get-Service -Online         # L'aide complète dans le navigateur

# 3. EXPLORER ce qu'une commande retourne
Get-Service | Get-Member     # Les propriétés et méthodes d'un objet "service"
```

> **📌 Réflexe transversal — `Get-Member` :** `Get-Service | Get-Member` te montre **tout** ce que contient un objet service : ses propriétés (`Name`, `Status`, `StartType`…) et ses méthodes (`.Start()`, `.Stop()`…). Chaque fois que ce cours introduira un nouvel objet (un utilisateur AD, une tâche planifiée, une réponse d'API…), le réflexe sera le même : le passer dans `Get-Member` pour l'explorer. On ne mémorise pas PowerShell, on l'explore.

> **Première utilisation de l'aide :** PowerShell peut te proposer de télécharger les fichiers d'aide détaillés. Lance une fois `Update-Help -ErrorAction SilentlyContinue` (nécessite Internet et, selon la version, des droits admin). Sans ça, `Get-Help` reste minimal.

#### Windows PowerShell 5.1 vs PowerShell 7

Il existe **deux** versions qui coexistent, et c'est important de le comprendre :

| | Windows PowerShell **5.1** | PowerShell **7+** |
|---|---|---|
| Exécutable | `powershell.exe` | `pwsh.exe` |
| Installé par défaut sur Windows ? | ✅ Oui | ❌ Non (à installer) |
| Multi-plateforme (Linux/Mac) ? | ❌ Non | ✅ Oui |
| Basé sur | .NET Framework | .NET (Core) |
| Modules AD, GPO, DNS Server… | ✅ Oui (via RSAT) | ✅ Oui (compatibilité) |

**Pour ce cours :** Windows PowerShell 5.1, déjà présent sur ton Windows, suffit pour la quasi-totalité du contenu. C'est aussi souvent la seule version disponible sur les serveurs en production. Les points spécifiques à PowerShell 7 sont signalés `[⚡ PS7+]`.

> **Où télécharger PowerShell 7 :** sur le dépôt officiel [github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell). Utile surtout si tu veux les nouveautés du langage ou travailler aussi sous Linux/Mac.

#### PowerShell vs CMD

Windows a un autre shell historique, **CMD** (l'Invite de commandes). Ce sont deux outils différents :

- **CMD** manipule du **texte brut** et a un jeu de commandes limité (`dir`, `copy`, `ipconfig`…)
- **PowerShell** manipule des **objets** et a des milliers de cmdlets structurées

Beaucoup de commandes CMD et d'exécutables classiques (`ipconfig`, `ping`, `whoami`) fonctionnent aussi depuis PowerShell — mais l'inverse est faux : les cmdlets PowerShell ne fonctionnent pas dans CMD.

#### Ouvrir PowerShell (et en administrateur)

- Menu Démarrer → tape "PowerShell" → **Windows PowerShell**
- Pour les opérations d'administration : **clic droit → Exécuter en tant qu'administrateur**
- Recommandé : **Windows Terminal** (depuis le Microsoft Store), qui regroupe PowerShell, CMD et WSL dans une fenêtre à onglets

> **🔑 Quand faut-il être administrateur ?** Lire est souvent possible sans privilèges (`Get-Service`, `Get-Process`). **Modifier** le système (arrêter un service, écrire dans `HKLM:`, lire le journal Security) nécessite en général une console élevée. Chaque fois que c'est le cas, ce cours l'indique avec `[🔑 Admin]`. Pour vérifier rapidement si ta console est élevée, une astuce : `net session` renvoie une erreur "Accès refusé" si tu n'es **pas** administrateur.

#### Ton premier script

Crée un dossier de travail et un fichier `poste.ps1` :

```powershell
# poste.ps1 — Premières infos sur la machine
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Date        : $(Get-Date)"
```

Pour le lancer :

```powershell
.\poste.ps1
```

Le `.\` devant le nom dit à PowerShell « exécute le script du dossier courant » (comme `./` en Bash). C'est une mesure de sécurité : PowerShell ne lance pas un script juste parce qu'on tape son nom.

Tu obtiens probablement une **erreur rouge** parlant de politique d'exécution. C'est le prochain point.

#### La politique d'exécution (Execution Policy)

Par défaut, Windows bloque l'exécution des scripts `.ps1`. Pour l'autoriser :

```powershell
# Voir la politique actuelle
Get-ExecutionPolicy

# Autoriser les scripts locaux pour ton compte utilisateur
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

| Politique | Effet |
|-----------|-------|
| `Restricted` | Aucun script ne s'exécute (défaut sur les clients Windows) |
| `RemoteSigned` | Les scripts locaux fonctionnent ; ceux téléchargés doivent être signés |
| `Unrestricted` / `Bypass` | Tout passe (à éviter) |

> **⚠️ Point technique important — l'Execution Policy n'est PAS une barrière de sécurité.** C'est un **garde-fou anti-erreur**, pas une protection contre un attaquant. Elle empêche un double-clic accidentel de lancer un script, mais elle se contourne trivialement — par exemple `powershell -ExecutionPolicy Bypass -File script.ps1`, ou en copiant-collant le contenu du script dans la console. Ne compte jamais dessus pour te protéger d'un code malveillant. Les vraies protections d'exécution (contrôle applicatif App Control/WDAC ou AppLocker, qui déclenche le Constrained Language Mode, et signature de code) sont vues en Partie VIII. Retiens : `RemoteSigned` en `CurrentUser` est le bon réglage **de confort** pour apprendre. En entreprise, cette politique est généralement imposée par GPO.

#### Les commentaires

```powershell
# Commentaire sur une ligne

<#
Commentaire
sur plusieurs lignes
#>

Write-Output "Ceci s'affiche"   # Commentaire en fin de ligne
```

### 🟡 Très utile en pratique

#### Les alias : passerelle avec Bash et CMD

PowerShell fournit des raccourcis (**alias**) pour les commandes courantes :

| Tu tapes | PowerShell exécute | Équivalent Bash |
|----------|-------------------|-----------------|
| `ls` / `dir` | `Get-ChildItem` | `ls` |
| `cd` | `Set-Location` | `cd` |
| `cat` / `type` | `Get-Content` | `cat` |
| `cp` | `Copy-Item` | `cp` |
| `rm` / `del` | `Remove-Item` | `rm` |
| `cls` | `Clear-Host` | `clear` |

Pratiques pour taper vite dans la console. **Mais dans un script, utilise toujours les noms complets** (`Get-ChildItem` plutôt que `ls`) : c'est plus lisible et portable.

> **Attention :** ces alias appellent des cmdlets PowerShell, pas les vraies commandes Linux. `ls -la` ne fonctionne pas ; l'équivalent est `Get-ChildItem -Force`.

#### Un éditeur : VS Code

Pour écrire des scripts confortablement, installe **Visual Studio Code** avec l'extension **PowerShell** (gratuit, multi-plateforme). Il offre coloration, autocomplétion et débogage. L'ancien **PowerShell ISE** (intégré à Windows) fonctionne aussi mais n'est plus développé.

#### La tab-complétion

Tape le début d'une cmdlet et appuie sur `Tab` : PowerShell complète. Ça marche aussi sur les paramètres (`Get-Service -N` + Tab → `-Name`). Indispensable et anti-fautes de frappe.

### 🔴 Bonus

#### Le profil PowerShell

Le profil est un script qui s'exécute à chaque ouverture de PowerShell (comme le `.bashrc` de Bash). Utile pour définir des raccourcis ou des fonctions perso :

```powershell
$PROFILE            # Le chemin de ton profil
notepad $PROFILE    # L'éditer
```

#### PowerShell Gallery

Le dépôt public de modules ([powershellgallery.com](https://www.powershellgallery.com/)), équivalent de PyPI ou npm :

```powershell
Install-Module -Name <NomDuModule> -Scope CurrentUser
```

### ❌ Erreur classique

```powershell
# Croire que l'Execution Policy sécurise le système
# → NON : c'est un garde-fou anti-erreur, contournable trivialement

# Oublier le .\ devant un script
poste.ps1        # ❌ "terme non reconnu"
.\poste.ps1      # ✅

# Utiliser les options Linux avec les alias
ls -la           # ❌
Get-ChildItem -Force   # ✅

# Confondre PowerShell et CMD
# Les cmdlets (Get-Service…) ne fonctionnent PAS dans CMD
```

### 💡 Exercices

**Guidé :** Ouvre PowerShell, lance `Get-Command -Verb Get | Measure-Object` pour compter combien de cmdlets `Get-*` existent sur ta machine. Puis `Get-Command -Noun Service` pour voir toutes les commandes liées aux services.

**Autonome :** Utilise `Get-Help` pour trouver comment lister uniquement les services *arrêtés* avec `Get-Service`. (Indice : `Get-Help Get-Service -Examples`.)

### ✅ Tu sais maintenant...

- Ce qu'est PowerShell (shell + langage + outil d'administration)
- La convention `Verbe-Nom` et pourquoi elle rend PowerShell prédictible
- Le trio `Get-Command` / `Get-Help` / `Get-Member` pour tout découvrir
- Le réflexe `Get-Member` pour explorer n'importe quel objet
- La différence 5.1 vs 7, PowerShell vs CMD
- Exécuter un script et régler l'Execution Policy — **en sachant qu'elle n'est pas une sécurité**

### 💬 Questions d'entretien typiques

- **Qu'est-ce qu'une cmdlet ?** → Une commande native PowerShell nommée `Verbe-Nom`, qui retourne des objets (pas du texte).
- **Comment découvrir une commande inconnue ?** → `Get-Command` pour la trouver, `Get-Help -Examples` pour l'utiliser, `Get-Member` pour explorer ce qu'elle retourne.
- **L'Execution Policy protège-t-elle des malwares ?** → Non. C'est un garde-fou anti-exécution accidentelle, contournable trivialement (`-ExecutionPolicy Bypass`, copier-coller…). Les vraies protections sont le contrôle applicatif (App Control/WDAC ou AppLocker) qui déclenche le Constrained Language Mode, plus la signature.
- **Différence Windows PowerShell 5.1 / PowerShell 7 ?** → 5.1 est intégré à Windows, basé sur .NET Framework, Windows uniquement. 7 est à installer, basé sur .NET, multi-plateforme.

---


## Chapitre 2 — Variables, types et informations système

### 🟢 Le minimum à savoir

#### Qu'est-ce qu'une variable ?

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

#### Les types de données

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

#### Afficher : `Write-Output` vs `Write-Host`

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

#### L'interpolation de chaînes

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

#### Saisie utilisateur avec `Read-Host`

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

#### Les variables automatiques utiles

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

### 🟡 Très utile en pratique

#### `Write-Host` en couleurs (pour les messages d'état)

```powershell
Write-Host "Service actif"   -ForegroundColor Green
Write-Host "Service arrêté"  -ForegroundColor Red
Write-Host "Attention"       -ForegroundColor Yellow
```

Idéal pour un rapport lisible à l'écran — mais rappelle-toi : ce sont des messages, pas des données.

#### Interroger le système avec `Get-CimInstance`

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

### 🔴 Bonus

#### Les méthodes .NET

Chaque objet PowerShell est un objet .NET. Tu peux appeler des méthodes .NET directement :

```powershell
[math]::Round(3.14159, 2)               # 3.14
[math]::Round($os.FreePhysicalMemory/1MB, 2)
[System.Environment]::OSVersion         # Version de l'OS
```

Pas indispensable pour débuter, mais c'est ce qui donne à PowerShell sa profondeur.

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Crée `fiche.ps1` qui stocke `$env:COMPUTERNAME`, `$env:USERNAME` et `Get-Date` dans des variables, puis les affiche proprement.

**Autonome :** Récupère l'objet `Get-CimInstance Win32_OperatingSystem` dans une variable `$os` et affiche sa version (`.Version`) et sa date de dernier démarrage (`.LastBootUpTime`) via l'interpolation `$(...)`.

### 🧩 Mini-projet — Fiche d'identité du poste

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

### ✅ Tu sais maintenant...

- Créer une variable avec `$`, forcer un type
- La différence `Write-Output` (données) / `Write-Host` (messages)
- L'interpolation, et le piège `$($objet.Propriété)`
- Lire une saisie avec `Read-Host` — et pourquoi les paramètres sont préférables
- Les variables automatiques (`$env:`, `$?`, `$LASTEXITCODE`…)
- Interroger le système avec `Get-CimInstance` (et que `Get-WmiObject` est mort en PS7)

### 💬 Questions d'entretien typiques

- **`Write-Output` ou `Write-Host` pour un résultat réutilisable ?** → `Write-Output` : il va dans le pipeline et peut être capturé. `Write-Host` sert aux messages destinés à l'humain.
- **Comment récupérer la version de l'OS d'une machine ?** → `Get-CimInstance Win32_OperatingSystem` puis lire `.Caption` / `.Version`. `Get-WmiObject` est l'ancêtre, absent de PowerShell 7.
- **Pourquoi préférer des paramètres à `Read-Host` ?** → Pour rendre le script automatisable (planifiable, appelable en masse) au lieu d'exiger une saisie humaine.

---


## Chapitre 3 — Paramètres et scripts administrables

### 🟢 Le minimum à savoir

#### Le problème : rendre un script réutilisable

Un script qui ne fait qu'une chose figée a peu de valeur. Un bon script d'administration prend des **paramètres** : le nom du serveur à vérifier, le service à redémarrer, le seuil d'alerte… C'est ce qui le rend réutilisable et **automatisable**.

#### La méthode simple : `$args`

`$args` est un tableau contenant les arguments passés au script :

```powershell
# verifier.ps1
Write-Output "Service demandé : $($args[0])"
```

```powershell
.\verifier.ps1 Spooler       # → Service demandé : Spooler
```

C'est rudimentaire : pas de noms, pas de types, pas de valeurs par défaut. On s'en sert rarement dans un vrai script.

#### La méthode recommandée : `param()`

`param()` déclare des paramètres **nommés, typés, validés**. C'est la façon professionnelle :

```powershell
# Get-ServiceStatus.ps1 — interroge le service SUR LA MACHINE LOCALE
param(
    [Parameter(Mandatory)]
    [string]$ServiceName,

    [switch]$IncludeStartType     # afficher aussi le type de démarrage
)

$svc = Get-Service -Name $ServiceName
if ($IncludeStartType) {
    Write-Output "$($svc.Name) : $($svc.Status) (démarrage : $($svc.StartType))"
} else {
    Write-Output "$($svc.Name) : $($svc.Status)"
}
```

```powershell
.\Get-ServiceStatus.ps1 -ServiceName Spooler
.\Get-ServiceStatus.ps1 -ServiceName wuauserv -IncludeStartType
```

> **[⚡ PS7+]** `$svc.StartType` est utilisé ici pour garder l'exemple simple. Sous **Windows PowerShell 5.1**, cette propriété peut être vide : utilise alors `Get-CimInstance Win32_Service` et sa propriété `StartMode`. Cette différence est expliquée au **Ch.4** puis appliquée au **Ch.11** — si tu travailles en 5.1, garde-la en tête dès maintenant.

> **Pourquoi pas de `-ComputerName` ici ?** Ce serait trompeur : `Get-Service` s'exécute **en local**. Ajouter un paramètre `-ComputerName` qui n'interroge pas vraiment la machine distante afficherait « le service de SRV01 est Running » alors qu'on a lu **ton poste**. Pour interroger réellement une machine distante, on utilise le **Remoting** (`Invoke-Command`, Ch.29) — et non un paramètre cosmétique. (Note : `Get-Service -ComputerName` existait en Windows PowerShell 5.1 mais **a été retiré de PowerShell 7** ; le remoting est désormais la voie recommandée.)

Les avantages de `param()`, décisifs en administration :

- Les paramètres ont des **noms** (`-ServiceName`) — pas besoin de retenir l'ordre
- On impose un **type** (`[string]`, `[int]`) — les erreurs sont attrapées tôt
- On définit des **valeurs par défaut**
- On rend un paramètre **obligatoire** (`[Parameter(Mandatory)]`)
- La **tab-complétion** fonctionne sur les noms

> **`param()` doit être la toute première instruction** du script (hors commentaires). Sinon, erreur.

> **Comparaison :** en Bash, tu gères `$1`, `$2` et des `shift` manuels ; en Python, `sys.argv` ou `argparse`. `param()` fait tout ça nativement, proprement.

#### Des noms de paramètres qui parlent

En administration, on retrouve toujours les mêmes noms de paramètres. Adopte-les, c'est la convention :

```powershell
param(
    [string]$ComputerName,     # la machine cible
    [string]$ServiceName,      # un service
    [string]$UserName,         # un utilisateur
    [string]$Path,             # un chemin
    [string]$OutputPath,       # où écrire un rapport
    [int]$ThresholdGB,         # un seuil
    [switch]$Force             # forcer sans confirmation
)
```

#### Paramètres obligatoires

```powershell
param(
    [Parameter(Mandatory)]
    [string]$ServiceName
)
```

Si l'utilisateur oublie `-ServiceName`, PowerShell le lui **demande** automatiquement au lancement — pas de plantage.

#### Les paramètres `[switch]` (drapeaux)

Un `[switch]` est un interrupteur : présent = `$true`, absent = `$false`.

```powershell
param(
    [string]$ServiceName,
    [switch]$Restart
)

$svc = Get-Service -Name $ServiceName
Write-Output "$($svc.Name) : $($svc.Status)"

if ($Restart) {
    Restart-Service -Name $ServiceName
    Write-Output "Service redémarré."
}
```

```powershell
.\svc.ps1 -ServiceName Spooler            # affiche seulement
.\svc.ps1 -ServiceName Spooler -Restart   # affiche ET redémarre
```

### 🟡 Très utile en pratique

#### La validation des paramètres

PowerShell peut valider automatiquement les valeurs **avant** que le script ne s'exécute :

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ServiceName,

    [ValidateRange(1, 100)]
    [int]$ThresholdGB = 10,

    [ValidateSet("Running", "Stopped", "All")]
    [string]$Filter = "All"
)
```

- `ValidateNotNullOrEmpty` : refuse une valeur vide
- `ValidateRange(1,100)` : impose un intervalle
- `ValidateSet(...)` : n'autorise qu'une liste de valeurs (et active la tab-complétion dessus !)

C'est un gain énorme : les mauvaises entrées sont rejetées avec un message clair, avant de casser quoi que ce soit.

#### Le splatting : passer les paramètres via une hashtable

Quand une commande a beaucoup de paramètres, on peut les regrouper dans une hashtable et la « projeter » avec `@` :

```powershell
$params = @{
    Name        = "wuauserv"
    ErrorAction = "Stop"
}
Get-Service @params
```

Plus lisible qu'une longue ligne, et pratique pour construire des appels dynamiquement. On y reviendra en Partie VII (industrialisation).

> **Note :** on n'a volontairement pas mis de `ComputerName` dans ce splat — `Get-Service -ComputerName` n'existe plus en PowerShell 7 (voir plus haut). Pour cibler une machine distante, on splatterait plutôt un appel `Invoke-Command` (Ch.29).

### 🔴 Bonus

#### `CmdletBinding` et paramètres communs

En ajoutant `[CmdletBinding()]` au-dessus du `param()`, ton script gagne gratuitement plusieurs **paramètres communs** : `-Verbose`, `-Debug`, `-ErrorAction`… En revanche, `-WhatIf` et `-Confirm` **ne sont pas** ajoutés par le seul `[CmdletBinding()]` : ils nécessitent `[CmdletBinding(SupportsShouldProcess)]` et un appel à `ShouldProcess` (détaillé au Ch.33). On approfondit `[CmdletBinding()]` au Ch.7 (fonctions).

### ❌ Erreur classique

```powershell
# param() pas en première position
Write-Output "Début"
param([string]$Nom)      # ❌ doit être la première instruction

# Oublier la virgule entre paramètres
param(
    [string]$Nom
    [int]$Age            # ❌ virgule manquante après $Nom
)

# Appeler avec la syntaxe C# (parenthèses + virgules)
Get-ServiceStatus("Spooler")           # ❌
.\Get-ServiceStatus.ps1 -ServiceName Spooler   # ✅
```

### 💡 Exercices

**Guidé :** Écris `Test-ServicePresent.ps1` avec un paramètre obligatoire `-ServiceName`. Le script affiche si le service existe (`Get-Service -Name $ServiceName -ErrorAction SilentlyContinue`) et son statut.

**Autonome :** Ajoute un paramètre `-Start` de type `[switch]`. Si présent et que le service est arrêté, le script le démarre. (On verra les conditions `if` au Ch.5 — ici, un simple `if ($Start) { ... }` suffit.)

### ✅ Tu sais maintenant...

- Passer des arguments (`$args`) et, mieux, déclarer des paramètres avec `param()`
- Rendre un paramètre obligatoire, typé, avec valeur par défaut
- Les `[switch]` et la validation (`ValidateSet`, `ValidateRange`…)
- Pourquoi les paramètres rendent un script **automatisable**
- Le splatting pour les appels à nombreux paramètres

### 💬 Questions d'entretien typiques

- **Pourquoi `param()` plutôt que `$args` ?** → Paramètres nommés, typés, validés, avec valeurs par défaut et tab-complétion. Plus robuste et automatisable.
- **Comment forcer un paramètre à faire partie d'une liste de valeurs ?** → `[ValidateSet("a","b","c")]`, qui rejette les autres valeurs et active l'autocomplétion.
- **Qu'est-ce que le splatting ?** → Passer les paramètres d'une cmdlet via une hashtable projetée avec `@`, pour la lisibilité et la construction dynamique d'appels.

---


## Chapitre 4 — Le pipeline et les objets

### 🟢 Le minimum à savoir

#### Pourquoi ce chapitre est LE plus important

Si tu ne retiens qu'une chose de tout le cours, retiens ceci : **en PowerShell, le pipeline transporte des objets, pas du texte.** C'est ce qui le rend radicalement différent de Bash, et c'est ce qui rend l'administration Windows si efficace.

#### Le pipeline : texte (Bash) vs objets (PowerShell)

**En Bash** : `ps aux | grep firefox | awk '{print $2}'`
- `ps` produit du **texte** ; `grep` filtre des lignes de texte ; `awk` découpe la 2ᵉ colonne de texte. Si le format d'affichage change, tout casse.

**En PowerShell** : `Get-Process firefox | Select-Object Id`
- `Get-Process` produit des **objets processus** ; chaque objet a des propriétés (`Name`, `Id`, `CPU`, `WorkingSet64`…) ; `Select-Object` lit directement la propriété `Id`. Aucun texte à découper, rien ne casse.

> **À garder en tête tout le cours :** les pipelines Unix manipulent des flux de texte ; le pipeline PowerShell manipule des **propriétés d'objets**. C'est la différence fondamentale.

#### Voir les objets en action

```powershell
$svc = Get-Service -Name Spooler

$svc.Name            # Spooler
$svc.Status          # Running (ou Stopped)
$svc.StartType       # Automatic / Manual / Disabled
$svc.DisplayName     # "Spouleur d'impression"
```

`$svc` n'est pas du texte : c'est un objet service, dont on lit les propriétés avec un point `.`.

> **⚠️ Compatibilité 5.1 — propriété `StartType`.** La propriété `StartType` sur l'objet renvoyé par `Get-Service` a été **ajoutée à PowerShell 6+**. En **Windows PowerShell 5.1**, `(Get-Service Spooler).StartType` peut être vide. Les exemples de ce cours qui utilisent `$svc.StartType` supposent donc PowerShell 7 (le plus courant aujourd'hui). **Pour obtenir le type de démarrage de façon portable 5.1 ET 7**, passe par CIM (que le cours détaille au Ch.11) :
> ```powershell
> Get-CimInstance Win32_Service -Filter "Name='Spooler'" |
>     Select-Object Name, State, StartMode    # StartMode = Auto / Manual / Disabled
> ```
> Retiens cette équivalence : `Get-Service`.`StartType` (PS7) ↔ `Win32_Service`.`StartMode` (5.1 et 7). On la réutilisera.

#### `Get-Member` : LA commande pour explorer

C'est le réflexe central de PowerShell. `Get-Member` révèle **tout** ce que contient un objet :

```powershell
Get-Service | Get-Member
```

La sortie liste :
- les **propriétés** (les informations : `Name`, `Status`, `StartType`…)
- les **méthodes** (les actions : `Start()`, `Stop()`, `Restart()`…)

> **📌 Réflexe transversal.** Tu récupères un objet inconnu ? Passe-le dans `Get-Member`. Ce cours te le rappellera à chaque nouvel objet : service, utilisateur AD, tâche planifiée, réponse d'API… La démarche est toujours la même. C'est le meilleur réflexe PowerShell qui soit.

#### Les 5 cmdlets du pipeline

| Cmdlet | Rôle | Analogie Bash |
|--------|------|--------------|
| `Where-Object` | **Filtrer** les objets selon une condition | `grep` |
| `Select-Object` | **Choisir** des propriétés (ou les N premiers) | `cut` / `awk` |
| `Sort-Object` | **Trier** par une propriété | `sort` |
| `Measure-Object` | **Compter**, additionner, moyenner | `wc` |
| `ForEach-Object` | **Agir** sur chaque objet | boucle `for` |

#### Filtrer avec `Where-Object`

```powershell
# Les services en cours d'exécution
Get-Service | Where-Object { $_.Status -eq "Running" }

# Les services démarrés automatiquement mais actuellement arrêtés (anomalie !)
Get-Service | Where-Object { $_.StartType -eq "Automatic" -and $_.Status -eq "Stopped" }

# Les processus consommant plus de 200 Mo
Get-Process | Where-Object { $_.WorkingSet64 -gt 200MB }
```

`$_` représente **l'objet courant** qui traverse le pipeline. On le retrouvera partout.

> **Syntaxe simplifiée (PowerShell 3+) :** pour un test simple, on peut écrire `Get-Service | Where-Object Status -eq "Running"` (sans accolades ni `$_`). Les deux formes coexistent ; les accolades restent nécessaires pour les conditions composées.

#### Sélectionner avec `Select-Object`

```powershell
Get-Service | Select-Object Name, Status, StartType    # certaines propriétés
Get-Process | Select-Object -First 5                    # les 5 premiers
Get-Process | Select-Object Name, Id -Last 3            # les 3 derniers
```

#### Trier avec `Sort-Object`

```powershell
# Les 10 processus les plus gourmands en mémoire
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id -First 10
```

#### Compter et calculer avec `Measure-Object`

```powershell
(Get-Service).Count                              # nombre de services (rapide)
Get-Process | Measure-Object WorkingSet64 -Sum   # mémoire totale utilisée
```

#### Agir avec `ForEach-Object`

```powershell
# Afficher un message pour chaque service arrêté
Get-Service | Where-Object Status -eq "Stopped" | ForEach-Object {
    Write-Output "Arrêté : $($_.Name)"
}
```

#### Un pipeline complet, réaliste

Les 10 processus les plus gourmands, avec la RAM en Mo (propriété **calculée**) :

```powershell
Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{ Name = "RAM(Mo)"; Expression = { [math]::Round($_.WorkingSet64/1MB) } } |
    Select-Object -First 10
```

La syntaxe `@{ Name = "..."; Expression = { ... } }` crée une colonne calculée à la volée. On l'écrit souvent en abrégé `@{ N=...; E={...} }`.

### 🟡 Très utile en pratique

#### Exporter les résultats (et le piège `Format-Table`)

Comme le pipeline transporte des objets, on peut les exporter directement — proprement :

```powershell
Get-Service | Select-Object Name, Status, StartType |
    Export-Csv -Path "services.csv" -NoTypeInformation -Encoding UTF8

Get-Process | Select-Object Name, Id, CPU |
    ConvertTo-Json | Set-Content "process.json" -Encoding UTF8
```

> **⚠️ Règle importante — `Format-*` en toute fin de pipeline uniquement.** Les cmdlets `Format-Table`, `Format-List`, `Format-Wide` transforment tes objets en **instructions d'affichage** : après elles, ce ne sont plus des données exploitables. Ne mets **jamais** un `Format-Table` avant un `Export-Csv`, un `Where-Object` ou un traitement — tu obtiendrais un CSV illisible rempli d'objets de formatage. `Format-*` sert **seulement** à présenter à l'écran, en tout dernier.
>
> ```powershell
> Get-Service | Format-Table | Export-Csv out.csv   # ❌ CSV corrompu
> Get-Service | Export-Csv out.csv -NoTypeInformation  # ✅ export propre
> Get-Service | Format-Table -AutoSize                  # ✅ affichage écran, en dernier
> ```

#### `Out-GridView` : une fenêtre interactive `[🪟 Windows]`

```powershell
Get-Service | Out-GridView    # tableau graphique triable/filtrable
```

### 🔴 Bonus

#### Les propriétés calculées, plus loin

On peut enchaîner plusieurs propriétés calculées pour bâtir un rapport sur mesure — on s'en servira beaucoup pour les inventaires (Ch.14) et les rapports AD (Ch.24).

### ❌ Erreur classique

```powershell
# Oublier $_ dans Where-Object (forme avec accolades)
Get-Service | Where-Object { Status -eq "Running" }     # ❌
Get-Service | Where-Object { $_.Status -eq "Running" }  # ✅

# Mettre Format-Table avant un traitement
Get-Process | Format-Table | Where-Object CPU -gt 10    # ❌ ne filtre plus rien d'utile
Get-Process | Where-Object CPU -gt 10 | Format-Table    # ✅

# Croire que "rien à l'écran" = "rien retourné"
$x = Get-Service    # rien ne s'affiche, mais $x contient tous les services
```

### 💡 Exercices

**Guidé :** Liste les services arrêtés dont le démarrage est `Automatic` (une anomalie fréquente), triés par nom, et affiche `Name` + `DisplayName`.

**Autonome :** Affiche les 5 processus les plus gourmands en mémoire avec une colonne calculée « RAM(Mo) », puis exporte le résultat complet (tous les processus, pas seulement 5) en CSV.

### 🧩 Mini-projet — Top consommateurs

Crée `Get-TopProcess.ps1` avec un paramètre `-Count` (défaut 10) qui affiche les N processus les plus gourmands en mémoire (nom, PID, RAM en Mo via propriété calculée) **et** affiche en vert le total de RAM consommée par ces N processus. Réutilise `param()` (Ch.3), le pipeline, la propriété calculée et `Measure-Object`.

### ✅ Tu sais maintenant...

- Le pipeline transporte des **objets**, pas du texte
- `$_` = l'objet courant ; `Get-Member` = le réflexe d'exploration
- `Where-Object` / `Select-Object` / `Sort-Object` / `Measure-Object` / `ForEach-Object`
- Les propriétés calculées `@{N=...;E={...}}`
- Exporter en CSV/JSON, et **ne jamais** mettre `Format-*` avant un traitement

### 💬 Questions d'entretien typiques

- **Quelle est LA différence entre le pipeline Bash et PowerShell ?** → Bash transporte du texte à parser ; PowerShell transporte des objets dont on lit les propriétés directement.
- **Que fait `Get-Member` ?** → Il révèle les propriétés et méthodes d'un objet. C'est l'outil pour explorer tout objet inconnu.
- **Pourquoi ne pas mettre `Format-Table` au milieu d'un pipeline ?** → Il convertit les objets en instructions d'affichage : plus rien n'est exploitable ensuite (filtrage, export). `Format-*` va en tout dernier, pour l'écran uniquement.

---


## Chapitre 5 — Opérateurs et conditions

### 🟢 Le minimum à savoir

#### Les opérateurs de comparaison

PowerShell utilise des opérateurs avec tiret (comme Bash), **pas** les symboles `<` `>` `==` (réservés à d'autres usages) :

| Opérateur | Signification | Exemple |
|-----------|--------------|---------|
| `-eq` | Égal | `$_.Status -eq "Running"` |
| `-ne` | Différent | `$_.Status -ne "Stopped"` |
| `-gt` / `-ge` | Supérieur / ou égal | `$_.WorkingSet64 -gt 200MB` |
| `-lt` / `-le` | Inférieur / ou égal | `$FreeGB -lt 10` |
| `-like` | Correspond à un motif (`*`, `?`) | `$_.Name -like "Win*"` |
| `-match` | Correspond à une regex | `$_.Name -match "^svc"` |
| `-contains` / `-in` | Appartenance à une collection | `$Critiques -contains $_.Name` |

> **Comparaison :** PowerShell `-eq` / `-lt` / `-gt` ≈ Bash `-eq` / `-lt` / `-gt`. Python utilise `==` / `<` / `>`. En PowerShell, `<` et `>` servent à la **redirection** — d'où les opérateurs à tiret.

> **Insensible à la casse par défaut :** `"SPOOLER" -eq "spooler"` renvoie `$true`. Pour forcer la casse, préfixe par `c` : `-ceq`, `-clike`, `-cmatch`.

#### Les opérateurs logiques

```powershell
$FreeGB -lt 10 -and $svc.Status -eq "Running"     # les deux vraies
$Role -eq "admin" -or $Role -eq "operator"        # au moins une
-not ($svc.Status -eq "Running")                   # négation
```

`-and`, `-or`, `-not` (Bash : `&&`, `||`, `!` ; Python : `and`, `or`, `not`).

#### Manipuler le texte : opérateurs de chaînes

En administration, on manipule sans cesse du texte : noms de machines, chemins, DN Active Directory, noms DNS, URIs, valeurs de registre. Ces opérateurs sont indispensables :

```powershell
# -like : motifs simples avec * et ?
"SRV-DC01" -like "SRV-*"                 # True

# -match : expressions régulières
"user@lab.local" -match "@(.+)$"         # True ; $Matches[1] = "lab.local"

# -replace : remplacer (avec regex)
"lab\alice" -replace "^lab\\", ""        # "alice"

# -split / -join : découper / recoller
"DC01,SRV01,CLIENT01" -split ","         # tableau de 3 éléments
@("a","b","c") -join " | "               # "a | b | c"
```

Et les **méthodes** de chaîne (rappel : ce sont des objets `[string]`) :

```powershell
$dn = "CN=Alice Martin,OU=IT,DC=lab,DC=local"
$dn.Length                                # longueur
$dn.ToUpper() / $dn.ToLower()             # casse
$dn.Trim()                                # enlève les espaces aux extrémités
$dn.Replace("lab", "corp")                # remplacement simple (sans regex)
$dn.Split(",")                            # découpe → tableau
$dn.StartsWith("CN=")                     # True
$dn.Substring(0, 8)                       # "CN=Alice"
```

> **Pourquoi c'est crucial :** au Ch.20, un DN (Distinguished Name) AD ressemble à `CN=Alice,OU=IT,DC=lab,DC=local`. Savoir le découper avec `.Split(",")` ou `-match` te permettra d'en extraire l'OU, le nom, le domaine. Ces opérations de chaînes reviennent partout : parser un chemin, isoler un nom d'utilisateur, construire une URI d'API.

#### Vérifier une existence : `Test-Path` et compagnie

Les cmdlets `Test-*` renvoient un booléen (`$true`/`$false`) — parfaites pour les conditions :

```powershell
Test-Path "C:\Scripts"                    # le dossier existe ?
Test-Path "HKLM:\SOFTWARE\MonApp"          # la clé de registre existe ?
Test-Connection SRV01 -Count 1 -Quiet      # la machine répond au ping ?
```

> **📌 Réflexe `Get`/`Test` avant d'agir :** ces cmdlets incarnent la discipline d'administration. Avant de créer un dossier, `Test-Path`. Avant de configurer une machine, `Test-Connection`. On vérifie l'état **avant** de modifier.

#### Les conditions : `if` / `elseif` / `else`

```powershell
$svc = Get-Service -Name Spooler

if ($svc.Status -eq "Running") {
    Write-Host "Le spouleur tourne." -ForegroundColor Green
}
elseif ($svc.Status -eq "Stopped") {
    Write-Host "Le spouleur est arrêté." -ForegroundColor Red
}
else {
    Write-Host "État : $($svc.Status)" -ForegroundColor Yellow
}
```

Syntaxe : condition entre **parenthèses** `()`, bloc entre **accolades** `{}`. Pas de `then`, pas de `fi`. C'est `elseif` en un seul mot.

#### Un cas d'administration complet

```powershell
# Vérifier l'espace disque et réagir
$free = (Get-PSDrive C).Free / 1GB

if ($free -lt 10) {
    Write-Host "ALERTE : seulement $([math]::Round($free,1)) Go libres sur C:" -ForegroundColor Red
}
else {
    Write-Host "Espace OK : $([math]::Round($free,1)) Go libres" -ForegroundColor Green
}
```

#### Le `switch` : choix multiples

Quand on teste une même valeur contre plusieurs cas, `switch` est plus lisible qu'une cascade de `if` :

```powershell
$svc = Get-Service -Name Spooler

switch ($svc.Status) {
    "Running" { Write-Host "Actif" -ForegroundColor Green }
    "Stopped" { Write-Host "Arrêté" -ForegroundColor Red }
    default   { Write-Host "État : $($svc.Status)" -ForegroundColor Yellow }
}
```

Le `switch` PowerShell gère aussi les motifs :

```powershell
switch -Wildcard ($fichier) {
    "*.log" { "Journal" }
    "*.csv" { "Données" }
    default { "Autre" }
}
```

### 🟡 Très utile en pratique

#### Comparaisons et pipeline : la même logique

`Where-Object { $_.Status -eq "Running" }` (Ch.4) utilise exactement ces opérateurs. Un `if` teste **une** valeur ; `Where-Object` applique le même test à **chaque objet** du pipeline. Même grammaire, deux usages.

#### L'opérateur ternaire `[⚡ PS7+]`

```powershell
$etat = $svc.Status -eq "Running" ? "OK" : "PROBLEME"
```

En 5.1, utilise un `if`/`else` classique.

### 🔴 Bonus

#### `-match` et la variable `$Matches`

Après un `-match` réussi, `$Matches` contient les groupes capturés :

```powershell
if ("user@lab.local" -match "^(.+)@(.+)$") {
    $Matches[1]   # user
    $Matches[2]   # lab.local
}
```

Très utile pour extraire des morceaux d'un log, d'un DN, d'une adresse.

### ❌ Erreur classique

```powershell
# Utiliser == ou > au lieu des opérateurs à tiret
if ($age == 18) { }      # ❌ == n'existe pas
if ($a > $b) { }         # ❌ > redirige vers un fichier !
if ($age -eq 18) { }     # ✅
if ($a -gt $b) { }       # ✅

# Confondre = (affectation) et -eq (comparaison)
if ($status = "Running") { }    # ❌ affectation, toujours vrai
if ($status -eq "Running") { }  # ✅

# Oublier les parenthèses ou accolades
if $svc.Status -eq "Running" { }   # ❌ parenthèses obligatoires
```

### 💡 Exercices

**Guidé :** Écris un script qui prend un `-ServiceName` et affiche en couleur : vert si Running, rouge si Stopped, jaune sinon. Utilise `switch`.

**Autonome :** Écris un script qui vérifie l'espace libre de `C:` et affiche une alerte si moins de 15 Go. Ajoute un test : si en plus le service `wuauserv` (Windows Update) tourne, suggère de le mettre en pause (message seulement).

### ✅ Tu sais maintenant...

- Les opérateurs de comparaison (`-eq`, `-lt`, `-like`, `-match`…) et logiques (`-and`, `-or`, `-not`)
- Les opérateurs et méthodes de chaîne (`-split`, `-replace`, `.Trim()`, `.Split()`…) — cruciaux pour DN, chemins, URIs
- `Test-Path` / `Test-Connection` et la discipline `Test` avant d'agir
- `if` / `elseif` / `else` et `switch` (avec motifs)

### 💬 Questions d'entretien typiques

- **Comment teste-t-on l'égalité en PowerShell ?** → `-eq` (insensible à la casse ; `-ceq` pour la casse). `==` n'existe pas ; `=` est une affectation.
- **Comment extraire le domaine de `user@lab.local` ?** → `-match "@(.+)$"` puis `$Matches[1]`, ou `.Split("@")[1]`.
- **`Where-Object` et `if`, quel rapport ?** → Même grammaire de comparaison ; `if` teste une valeur, `Where-Object` applique le test à chaque objet du pipeline.

---


## Chapitre 6 — Collections, hashtables et boucles

### 🟢 Le minimum à savoir

#### Les tableaux (arrays)

Un tableau regroupe plusieurs valeurs. En administration, c'est typiquement **une liste de machines** :

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

$Serveurs[0]           # DC01 (premier)
$Serveurs[-1]          # SRV-WEB01 (dernier)
$Serveurs.Count        # 3
$Serveurs += "SRV02"   # ajoute (crée un nouveau tableau — lent en boucle serrée)
$Serveurs -contains "DC01"    # True
```

#### Les hashtables (dictionnaires clé-valeur)

Une hashtable associe des **clés** à des **valeurs** :

```powershell
$Seuils = @{
    DisqueGB = 10
    RAMPourcent = 90
    Uptime = 30
}

$Seuils["DisqueGB"]        # 10
$Seuils.RAMPourcent        # 90 (syntaxe avec point)
$Seuils["Uptime"] = 45     # modifier
$Seuils.ContainsKey("DisqueGB")   # True
```

On les retrouve partout : configuration, `-FilterHashtable` pour les logs (Ch.34), splatting (Ch.3), corps JSON d'API (Ch.31).

> **Comparaison :** `@{ Clé = "Valeur" }` en PowerShell ≈ dictionnaire Python `{ "clé": "valeur" }` ≈ tableau associatif Bash `declare -A`.

#### Le PSCustomObject : construire des objets pour tes rapports

C'est **l'outil clé** pour produire des rapports d'administration propres. Tu fabriques un objet avec les propriétés que tu veux :

```powershell
$rapport = [PSCustomObject]@{
    Serveur   = "SRV01"
    Statut    = "OK"
    EspaceGB  = 42
    Verifie   = Get-Date
}

$rapport.Serveur          # SRV01
```

L'intérêt : un tableau de PSCustomObject s'exporte directement en CSV/JSON, s'affiche en table, se filtre… C'est ainsi qu'on produit des inventaires (Ch.14), des rapports AD (Ch.24), des états de parc.

```powershell
$parc = @(
    [PSCustomObject]@{ Serveur = "DC01";  Role = "AD";     RAM_GB = 16 }
    [PSCustomObject]@{ Serveur = "SRV01"; Role = "Files";  RAM_GB = 8 }
)
$parc | Format-Table -AutoSize        # affichage
$parc | Export-Csv parc.csv -NoTypeInformation -Encoding UTF8   # export
```

#### Les boucles

**`foreach`** — parcourir une collection (le cas le plus courant en admin) :

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

foreach ($s in $Serveurs) {
    if (Test-Connection $s -Count 1 -Quiet) {
        Write-Host "$s répond" -ForegroundColor Green
    } else {
        Write-Host "$s NE répond PAS" -ForegroundColor Red
    }
}
```

**`for`** — quand tu as besoin d'un compteur :

```powershell
for ($i = 1; $i -le 5; $i++) {
    Write-Output "Tentative $i"
}
```

**`while`** / **`do...while`** / **`do...until`** — tant qu'une condition tient :

```powershell
# Attendre qu'un service démarre (avec sécurité anti-boucle infinie)
$essais = 0
do {
    Start-Sleep -Seconds 2
    $svc = Get-Service -Name Spooler
    $essais++
} while ($svc.Status -ne "Running" -and $essais -lt 10)
```

**`break`** sort de la boucle, **`continue`** passe à l'itération suivante.

#### `foreach` (mot-clé) vs `ForEach-Object` (pipeline)

```powershell
# foreach : la collection est déjà en mémoire
$services = Get-Service
foreach ($s in $services) { $s.Name }

# ForEach-Object : traite les objets au fil du pipeline (économe en mémoire)
Get-Service | ForEach-Object { $_.Name }
```

Les deux existent, choisis selon le contexte. En pipeline, c'est `ForEach-Object` (avec `$_`).

### 🟡 Très utile en pratique

#### Construire un rapport de parc

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

$resultats = foreach ($s in $Serveurs) {
    $enLigne = Test-Connection $s -Count 1 -Quiet
    [PSCustomObject]@{
        Serveur = $s
        EnLigne = $enLigne
        Teste   = Get-Date -Format "HH:mm:ss"
    }
}

$resultats | Format-Table -AutoSize
```

Remarque : la boucle `foreach` **produit** des objets qu'on capture dans `$resultats`. C'est un pattern fondamental pour les inventaires.

#### Performance : `+=` sur un gros tableau

`$tab += $x` recrée tout le tableau à chaque ajout — lent sur des milliers d'éléments. Alternative :

```powershell
$liste = [System.Collections.Generic.List[object]]::new()
$liste.Add($x)
```

Pour débuter, `+=` suffit sur de petits volumes ; retiens juste que ça ne passe pas à l'échelle.

### 🔴 Bonus

#### Parcours parallèle `[⚡ PS7+]`

PowerShell 7 permet `ForEach-Object -Parallel` pour traiter plusieurs machines en même temps :

```powershell
$Serveurs | ForEach-Object -Parallel { Test-Connection $_ -Count 1 -Quiet } -ThrottleLimit 5
```

Puissant pour l'inventaire d'un grand parc — on en reparle en Partie VI.

### ❌ Erreur classique

```powershell
# Confondre foreach (mot-clé) et ForEach-Object (pipeline)
Get-Service | foreach ($s in ...) { }      # ❌
Get-Service | ForEach-Object { $_.Name }   # ✅

# Boucle potentiellement infinie sans garde-fou
do { ... } while ($svc.Status -ne "Running")   # ❌ si le service ne démarre jamais
# ✅ ajoute un compteur d'essais maximum

# Indexer une hashtable comme un tableau
$Seuils[0]              # ❌ 0 n'est pas une clé
$Seuils["DisqueGB"]     # ✅
```

### 💡 Exercices

**Guidé :** Crée un tableau de 3 noms de services critiques (`"Spooler"`, `"wuauserv"`, `"EventLog"`). Parcours-le avec `foreach` et affiche l'état de chacun en couleur.

**Autonome :** Transforme le résultat précédent en tableau de PSCustomObject (`Service`, `Statut`, `DemarrageAuto`) et exporte-le en CSV.

### 🧩 Mini-projet — Supervision de services critiques

Crée `Test-CriticalServices.ps1` qui : prend un paramètre `-Services` (tableau, avec une valeur par défaut de 3-4 services), parcourt la liste, construit un PSCustomObject par service (Nom, Statut, TypeDémarrage, Conforme), affiche le tout en table, et exporte en CSV. Réutilise `param()` (Ch.3), le pipeline (Ch.4), les conditions (Ch.5) et les collections (Ch.6). *(Pour le type de démarrage portable en 5.1 comme en 7, tu utiliseras `Get-CimInstance Win32_Service` et sa propriété `StartMode` — détaillé au Ch.11.)*

### ✅ Tu sais maintenant...

- Créer et manipuler tableaux (`@()`) et hashtables (`@{}`)
- Fabriquer des **PSCustomObject** pour des rapports propres
- Les boucles `foreach` / `for` / `while` / `do` et `break`/`continue`
- La différence `foreach` (mot-clé) vs `ForEach-Object` (pipeline)
- Produire un tableau d'objets depuis une boucle (pattern d'inventaire)

### 💬 Questions d'entretien typiques

- **Comment produire un rapport structuré exportable en CSV ?** → Construire des `[PSCustomObject]` (une propriété par colonne), les collecter dans un tableau, puis `Export-Csv`.
- **`foreach` ou `ForEach-Object` ?** → `foreach` quand la collection est en mémoire ; `ForEach-Object` dans un pipeline (plus économe, utilise `$_`).
- **Pourquoi `$tab += $x` est déconseillé en masse ?** → Il recrée le tableau à chaque ajout ; sur de gros volumes, on utilise une `List[object]`.

---


## Chapitre 7 — Fonctions et scripts structurés

### 🟢 Le minimum à savoir

#### Pourquoi des fonctions ?

Jusqu'ici, tes scripts étaient linéaires. Dès qu'une logique se répète (vérifier un service, tester une machine, produire une ligne de rapport), on la range dans une **fonction** : un bloc nommé, réutilisable, testable. C'est le premier pas vers des outils d'administration propres.

#### Définir et appeler une fonction

```powershell
function Get-Uptime {
    $os = Get-CimInstance Win32_OperatingSystem
    (Get-Date) - $os.LastBootUpTime
}

Get-Uptime        # appel : on écrit juste son nom
```

> **Convention :** nomme tes fonctions en `Verbe-Nom`, comme les cmdlets (`Get-Uptime`, `Test-ServerHealth`). Utilise des verbes approuvés (liste : `Get-Verb`). Ça rend tes fonctions cohérentes avec l'écosystème PowerShell.

#### Paramètres de fonction

C'est le **même `param()`** que pour les scripts (Ch.3) — une fonction est un mini-script :

```powershell
function Test-ServiceRunning {
    param(
        [Parameter(Mandatory)]
        [string]$ServiceName
    )

    $svc = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
    $svc -and $svc.Status -eq "Running"
}

Test-ServiceRunning -ServiceName Spooler    # → True ou False
```

#### Le return implicite : LE piège à comprendre

**En PowerShell, tout ce qui n'est pas capturé ou redirigé est automatiquement renvoyé.** Pas besoin de `return` pour renvoyer une valeur — mais attention aux sorties parasites.

```powershell
function Get-Somme {
    param([int]$A, [int]$B)
    $A + $B          # renvoyé automatiquement, sans return
}

$r = Get-Somme -A 10 -B 25     # → 35
```

Le piège : si la fonction produit **d'autres** sorties, elles sont aussi renvoyées :

```powershell
function Get-SommeBuggee {
    param([int]$A, [int]$B)
    Write-Output "Calcul en cours..."   # ← renvoyé AUSSI !
    $A + $B
}

$r = Get-SommeBuggee -A 10 -B 25
$r    # → un TABLEAU @("Calcul en cours...", 35), pas 35 !
```

**La solution :** pour les messages de diagnostic, utilise `Write-Verbose` (affiché seulement si l'appelant passe `-Verbose`), qui nécessite `[CmdletBinding()]` :

```powershell
function Get-SommeCorrecte {
    [CmdletBinding()]
    param([int]$A, [int]$B)
    Write-Verbose "Calcul en cours..."   # n'entre PAS dans la sortie
    $A + $B                               # seule vraie valeur renvoyée
}

$r = Get-SommeCorrecte -A 10 -B 25            # → 35
$r = Get-SommeCorrecte -A 10 -B 25 -Verbose   # affiche le message, renvoie 35
```

> **Comparaison :** en Python, seul `return` renvoie. En PowerShell, **tout** ce qui « tombe » dans le pipeline est renvoyé. C'est puissant (une fonction peut émettre un flux d'objets) mais il faut garder ses fonctions « propres » : une fonction renvoie des **données**, ses messages passent par `Write-Verbose`/`Write-Host`.

#### `return` existe (mais ne fait pas ce que tu crois)

`return` renvoie une valeur **et** quitte la fonction. Il sert surtout à sortir tôt :

```powershell
function Get-AccountState {
    param([int]$FailedLogons)
    if ($FailedLogons -ge 5) { return "À verrouiller" }
    if ($FailedLogons -ge 1) { return "À surveiller" }
    "OK"
}
```

`return "x"` équivaut à « émettre `x` puis stopper ». Il ne « fabrique » pas la sortie à lui seul — la ligne `"OK"` sans `return` renvoie tout autant.

#### La portée des variables (scope)

Les variables créées dans une fonction sont **locales** — elles n'affectent pas l'extérieur :

```powershell
$Cible = "Global"

function Set-Cible {
    $Cible = "Local"        # crée une variable LOCALE
    Write-Output "Dans la fonction : $Cible"    # Local
}

Set-Cible
Write-Output "Après : $Cible"                   # Global (inchangé)
```

Pour lire une variable du script parent, PowerShell « remonte » les portées automatiquement en **lecture**. Mais pour **modifier** une variable parente, il faudrait `$script:Cible` ou `$global:Cible` — à **éviter**. La bonne pratique : une fonction reçoit ce dont elle a besoin par **paramètres** et **renvoie** un résultat. Pas d'effets de bord cachés.

### 🟡 Très utile en pratique

#### `[CmdletBinding()]` : transformer une fonction en outil pro

Ajouter `[CmdletBinding()]` au-dessus du `param()` donne gratuitement à ta fonction les **paramètres communs** : `-Verbose`, `-Debug`, `-ErrorAction`, et (avec un peu plus de code) `-WhatIf`/`-Confirm` (voir Ch.33).

```powershell
function Test-ServerHealth {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$ComputerName,
        [int]$MinFreeGB = 10
    )

    Write-Verbose "Vérification de $ComputerName..."

    $online = Test-Connection $ComputerName -Count 1 -Quiet

    [PSCustomObject]@{
        Serveur = $ComputerName
        EnLigne = $online
        Verifie = Get-Date -Format "yyyy-MM-dd HH:mm"
    }
}

Test-ServerHealth -ComputerName SRV01 -Verbose
```

Remarque le pattern clé : la fonction **renvoie un PSCustomObject**. Elle ne l'affiche pas, elle le produit — l'appelant décide ensuite d'afficher, filtrer, exporter.

#### Placer ses fonctions dans un script

Un script d'administration typique définit ses fonctions en haut, puis les orchestre en bas :

```powershell
# ServerHealth.ps1
param(
    [string[]]$Servers = @("DC01", "SRV01")
)

function Test-ServerHealth {
    [CmdletBinding()]
    param([string]$ComputerName)
    [PSCustomObject]@{
        Serveur = $ComputerName
        EnLigne = Test-Connection $ComputerName -Count 1 -Quiet
    }
}

# Orchestration
$Servers | ForEach-Object { Test-ServerHealth -ComputerName $_ } |
    Format-Table -AutoSize
```

### 🔴 Bonus

#### `begin` / `process` / `end` : accepter le pipeline

Une fonction avancée peut traiter des objets reçus **par le pipeline** grâce à un paramètre marqué `ValueFromPipeline` et un bloc `process` :

```powershell
function Get-ServiceReport {
    [CmdletBinding()]
    param(
        [Parameter(ValueFromPipeline)]
        [System.ServiceProcess.ServiceController]$Service
    )
    process {
        [PSCustomObject]@{
            Nom    = $Service.Name
            Statut = $Service.Status
        }
    }
}

Get-Service | Get-ServiceReport    # la fonction reçoit chaque service via le pipeline
```

C'est ce qui rend une fonction « native » au pipeline PowerShell. À creuser plus tard.

### ❌ Erreur classique

```powershell
# Return implicite pollué par .Add()
function Build-List {
    $l = @()
    $l.Add("x")          # ❌ .Add() sur un tableau renvoie... et échoue souvent
}
# → utiliser une vraie liste et absorber les sorties parasites
$l = [System.Collections.Generic.List[object]]::new()
$l.Add("x")              # ok, ne pollue pas

# Appeler une fonction à la C#
Test-ServiceRunning("Spooler")          # ❌ un seul argument (un tableau)
Test-ServiceRunning -ServiceName Spooler   # ✅

# Modifier une variable globale depuis une fonction
function Set-Flag { $global:Flag = $true }   # ❌ effet de bord caché
# → renvoyer une valeur et la capturer à l'extérieur
```

### 💡 Exercices

**Guidé :** Écris une fonction `Test-DiskSpace` qui prend `-Drive` (ex : `"C"`) et `-MinFreeGB` (défaut 10), et renvoie un PSCustomObject `{ Lecteur; LibreGB; Conforme }`.

**Autonome :** Écris `Get-ServiceStatus` qui accepte plusieurs noms de services et renvoie un PSCustomObject par service. Appelle-la puis exporte le résultat en CSV.

### ✅ Tu sais maintenant...

- Définir des fonctions `Verbe-Nom` avec `param()`
- Le **return implicite** et comment garder une fonction propre (`Write-Verbose`)
- La portée locale des variables et pourquoi éviter les variables globales
- `[CmdletBinding()]` pour des fonctions avec paramètres communs
- Le pattern « une fonction renvoie des objets, elle ne les affiche pas »

### 💬 Questions d'entretien typiques

- **Comment une fonction PowerShell renvoie-t-elle une valeur ?** → Tout ce qui n'est pas capturé/redirigé est renvoyé ; `return` sert surtout à sortir tôt.
- **Pourquoi `Write-Verbose` plutôt que `Write-Output` pour un message ?** → `Write-Output` polluerait la valeur de retour ; `Write-Verbose` ne s'affiche qu'avec `-Verbose` et n'entre pas dans la sortie.
- **À quoi sert `[CmdletBinding()]` ?** → À obtenir les paramètres communs (`-Verbose`, `-ErrorAction`, support de `-WhatIf`…) et faire de la fonction un outil « avancé ».

---


## Chapitre 8 — Gestion des erreurs et débogage

### 🟢 Le minimum à savoir

#### Pourquoi c'est vital en administration

Un script d'administration touche à de vraies machines. S'il plante silencieusement au milieu d'une boucle sur 200 serveurs, ou s'il continue comme si de rien n'était après un échec, les dégâts peuvent être réels. Savoir **détecter, intercepter et journaliser** les erreurs est une compétence non négociable.

#### Erreurs terminantes vs non-terminantes : la distinction clé

PowerShell a **deux** sortes d'erreurs, et c'est LE point à comprendre :

- **Non-terminante** : la cmdlet signale un problème mais **continue** (et le script continue). C'est le cas par défaut de la plupart des cmdlets. Exemple : `Get-Service "Absent1","Spooler"` affiche une erreur pour `Absent1` mais renvoie quand même `Spooler`.
- **Terminante** : l'exécution **s'arrête** (erreur de syntaxe, exception .NET, ou erreur non-terminante que tu as *promue* en terminante).

Le problème : un `try/catch` (voir plus bas) n'attrape **que les erreurs terminantes**. Une erreur non-terminante passe à travers le `catch` sans le déclencher. D'où la nécessité de `-ErrorAction Stop`.

#### `-ErrorAction` : contrôler le comportement

Chaque cmdlet accepte `-ErrorAction`, qui décide quoi faire en cas d'erreur :

| Valeur | Effet |
|--------|-------|
| `Continue` | (défaut) Affiche l'erreur et continue |
| `Stop` | **Transforme l'erreur en terminante** (indispensable pour `try/catch`) |
| `SilentlyContinue` | Ignore l'erreur silencieusement et continue |
| `Ignore` | Ignore sans même enregistrer l'erreur dans `$Error` |

```powershell
Get-Service "Absent" -ErrorAction SilentlyContinue   # pas de rouge à l'écran
Get-Service "Absent" -ErrorAction Stop               # lève une erreur terminante
```

#### `try` / `catch` / `finally`

C'est le mécanisme d'interception. **Rappel : il faut `-ErrorAction Stop` pour que `catch` attrape une erreur de cmdlet.**

```powershell
try {
    $svc = Get-Service -Name "ServiceInexistant" -ErrorAction Stop
    Restart-Service -Name $svc.Name -ErrorAction Stop
    Write-Host "Service redémarré." -ForegroundColor Green
}
catch {
    Write-Host "Échec : $($_.Exception.Message)" -ForegroundColor Red
}
finally {
    Write-Host "Vérification terminée."   # s'exécute TOUJOURS
}
```

- `try` : le code qui peut échouer
- `catch` : ce qu'on fait en cas d'erreur (`$_` contient l'objet erreur ; `$_.Exception.Message` le message)
- `finally` : s'exécute dans tous les cas (nettoyage, fermeture de session…) — optionnel

> **Comparaison :** `try/catch/finally` existe quasi à l'identique en Python et dans beaucoup de langages. La spécificité PowerShell, c'est le `-ErrorAction Stop` à ne pas oublier.

#### Un exemple d'administration réel

```powershell
$Serveurs = @("DC01", "SRV-ABSENT", "SRV01")

foreach ($s in $Serveurs) {
    try {
        $os = Get-CimInstance Win32_OperatingSystem -ComputerName $s -ErrorAction Stop
        Write-Host "$s OK — démarré le $($os.LastBootUpTime)" -ForegroundColor Green
    }
    catch {
        Write-Host "$s injoignable : $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

Grâce au `try/catch` **dans** la boucle, un serveur injoignable n'interrompt pas le traitement des autres. C'est le pattern d'or de l'administration de parc.

#### `$?` et `$LASTEXITCODE` : deux indicateurs à ne pas confondre

```powershell
Get-Service Spooler
$?               # $true si la DERNIÈRE commande PowerShell a réussi, $false sinon

ping SRV01
$LASTEXITCODE    # code de sortie du dernier PROGRAMME EXTERNE (ping.exe) : 0 = succès
```

- `$?` : booléen, indique le **succès de la dernière opération** — cmdlet **ou** commande native. Pour un exécutable externe, `$?` passe à `$true` si le code de sortie est `0`, `$false` sinon. Il ne dit **pas** *quel* code : juste réussi/échoué. Il se remet à jour à **chaque** commande — capture-le tout de suite.
- `$LASTEXITCODE` : entier, donne le **code de sortie exact** du dernier **programme externe** (`ping`, `robocopy`, `git`…). Convention Unix : `0` = succès, autre = erreur (et la valeur précise peut renseigner sur la cause).

> **En pratique :** `$?` = « ça a réussi, oui ou non ? » (booléen, marche pour tout) ; `$LASTEXITCODE` = « quel code exact a renvoyé l'exécutable ? » (entier, exécutables natifs seulement). Pour tester finement le résultat d'un `.exe`, préfère `$LASTEXITCODE -eq 0` plutôt que `$?`, car tu récupères la valeur exacte. Et `$?` est fugace : `Get-Service; Write-Host "x"; $?` te donne le succès du `Write-Host`, pas du `Get-Service`.

### 🟡 Très utile en pratique

#### La variable `$Error`

PowerShell garde l'historique des erreurs dans `$Error` (un tableau, la plus récente en `[0]`) :

```powershell
$Error[0]                      # la dernière erreur
$Error[0].Exception.Message    # son message
$Error.Clear()                 # vider l'historique
```

Pratique pour le débogage : après un souci, `$Error[0] | Format-List *` donne tous les détails.

#### Les messages de diagnostic

PowerShell a plusieurs « flux » de sortie dédiés — utilise le bon selon l'intention :

```powershell
Write-Verbose "Détail affiché avec -Verbose"      # diagnostic (nécessite CmdletBinding)
Write-Warning "Avertissement (jaune)"             # avertissement visible
Write-Error   "Erreur non-terminante"             # erreur (rouge), sans stopper
Write-Debug   "Message de débogage (-Debug)"      # débogage
```

> **Bonne pratique :** ne mélange pas tes **données** (via `Write-Output`/objets) et tes **messages** (via ces flux). C'est ce qui rend un script à la fois exploitable en pipeline *et* lisible par un humain.

#### `Set-StrictMode` : le filet anti-bugs

`Set-StrictMode` force PowerShell à signaler les erreurs silencieuses classiques (variable non définie, propriété inexistante) :

```powershell
Set-StrictMode -Version Latest

$Total = $Compteur + 1    # ❌ erreur claire si $Compteur n'a jamais été défini
```

Sans lui, `$Compteur` non défini vaudrait `$null` (donc `0`) et le bug passerait inaperçu. Mets-le en tête de tes scripts sérieux.

#### L'aide basée sur les commentaires

Documente tes fonctions/scripts avec un bloc spécial — `Get-Help` le lira :

```powershell
function Test-ServerHealth {
<#
.SYNOPSIS
    Vérifie l'état de santé d'un serveur.
.PARAMETER ComputerName
    Le nom du serveur à vérifier.
.EXAMPLE
    Test-ServerHealth -ComputerName SRV01
#>
    [CmdletBinding()]
    param([string]$ComputerName)
    # ...
}

Get-Help Test-ServerHealth -Examples    # affiche ta doc
```

### 🔴 Bonus

#### Attraper des erreurs spécifiques

`catch` peut cibler un type d'exception précis, pour réagir différemment selon la cause :

```powershell
try {
    Get-Content "C:\introuvable.txt" -ErrorAction Stop
}
catch [System.IO.FileNotFoundException] {
    Write-Warning "Fichier absent."
}
catch {
    Write-Warning "Autre erreur : $($_.Exception.Message)"
}
```

#### Le point d'arrêt et le débogage pas-à-pas

Dans VS Code, tu peux poser des points d'arrêt (clic dans la marge, ou `Set-PSBreakpoint`) et exécuter le script pas-à-pas pour inspecter les variables. Indispensable quand un script se comporte de façon inattendue.

### ❌ Erreur classique

```powershell
# try/catch SANS -ErrorAction Stop → le catch ne se déclenche pas
try { Get-Service "Absent" }               # ❌ erreur non-terminante, catch ignoré
catch { "attrapé" }
try { Get-Service "Absent" -ErrorAction Stop }   # ✅ catch fonctionne
catch { "attrapé" }

# Choisir le bon indicateur après un .exe
ping SRV01; if (-not $?) { }               # ⚠️ marche, mais moins informatif (pas le code exact)
ping SRV01; if ($LASTEXITCODE -ne 0) { }   # ✅ code exact du programme externe

# Vérifier $? trop tard
Get-Service Spooler
Write-Host "ok"
$?                                          # ❌ reflète Write-Host, pas Get-Service
```

### 💡 Exercices

**Guidé :** Écris un script qui tente `Restart-Service -Name $ServiceName -ErrorAction Stop` dans un `try/catch` et affiche un message vert en cas de succès, rouge (avec `$_.Exception.Message`) en cas d'échec.

**Autonome :** Reprends ton script de supervision de services (Ch.6) et entoure chaque vérification d'un `try/catch` pour qu'un service inexistant n'interrompe pas la boucle. Ajoute `Set-StrictMode -Version Latest` en tête.

### 🧩 Capstone Partie I — `Get-ServerHealth.ps1`

Assemble tout ce que tu as appris dans un outil complet :

- **Paramètres** (`-ComputerName` avec tableau possible, `-MinFreeGB`) — Ch.3
- Une **fonction** `Test-ServerHealth` documentée (aide par commentaires) — Ch.7
- Un **pipeline** qui produit un PSCustomObject par serveur (nom, en ligne, espace disque, uptime, statut global) — Ch.4, Ch.6
- Des **conditions** pour déterminer le statut (OK / Alerte) — Ch.5
- Un **try/catch** par serveur pour la robustesse + `Set-StrictMode` — Ch.8
- Un **export CSV** du rapport final

C'est le premier vrai outil d'administration du cours. On le fera évoluer : disque (Ch.14), réseau (Ch.18), exécution à distance (Ch.29).

### ✅ Tu sais maintenant...

- La différence **erreur terminante / non-terminante** et pourquoi `-ErrorAction Stop` est indispensable
- `try` / `catch` / `finally` pour intercepter et nettoyer
- `$?` = succès **booléen** de la dernière opération (cmdlet **ou** natif) ; `$LASTEXITCODE` = **code numérique exact** du dernier programme natif
- `$Error`, les flux `Write-Verbose`/`Warning`/`Error`/`Debug`
- `Set-StrictMode` et l'aide par commentaires

### 💬 Questions d'entretien typiques

- **Pourquoi un `try/catch` ne capture-t-il parfois rien ?** → Parce que l'erreur est non-terminante ; il faut `-ErrorAction Stop` pour la rendre terminante.
- **Différence entre `$?` et `$LASTEXITCODE` ?** → `$?` = succès booléen de la dernière opération, cmdlet **ou** exécutable (`$true` si code 0 pour un natif) ; `$LASTEXITCODE` = code de sortie **numérique exact** du dernier exécutable externe. Pour tester finement un `.exe`, on utilise `$LASTEXITCODE`.
- **Comment éviter qu'un serveur injoignable casse une boucle sur tout un parc ?** → Mettre le traitement de chaque serveur dans un `try/catch` avec `-ErrorAction Stop`, pour isoler les échecs.
- **À quoi sert `Set-StrictMode` ?** → À transformer en erreurs les pièges silencieux (variables/propriétés inexistantes), ce qui fiabilise les scripts.

---
