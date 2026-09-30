---
title: Chapitre 3 — Paramètres et scripts administrables
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux powershell pour administrer windows
  - index.md
---

## 🟢 Le minimum à savoir

### Le problème : rendre un script réutilisable

Un script qui ne fait qu'une chose figée a peu de valeur. Un bon script d'administration prend des **paramètres** : le nom du serveur à vérifier, le service à redémarrer, le seuil d'alerte… C'est ce qui le rend réutilisable et **automatisable**.

### La méthode simple : `$args`

`$args` est un tableau contenant les arguments passés au script :

```powershell
# verifier.ps1
Write-Output "Service demandé : $($args[0])"
```


```powershell
.\verifier.ps1 Spooler       # → Service demandé : Spooler
```


C'est rudimentaire : pas de noms, pas de types, pas de valeurs par défaut. On s'en sert rarement dans un vrai script.

### La méthode recommandée : `param()`

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

### Des noms de paramètres qui parlent

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


### Paramètres obligatoires

```powershell
param(
    [Parameter(Mandatory)]
    [string]$ServiceName
)
```


Si l'utilisateur oublie `-ServiceName`, PowerShell le lui **demande** automatiquement au lancement — pas de plantage.

### Les paramètres `[switch]` (drapeaux)

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


## 🟡 Très utile en pratique

### La validation des paramètres

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

### Le splatting : passer les paramètres via une hashtable

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

## 🔴 Bonus

### `CmdletBinding` et paramètres communs

En ajoutant `[CmdletBinding()]` au-dessus du `param()`, ton script gagne gratuitement plusieurs **paramètres communs** : `-Verbose`, `-Debug`, `-ErrorAction`… En revanche, `-WhatIf` et `-Confirm` **ne sont pas** ajoutés par le seul `[CmdletBinding()]` : ils nécessitent `[CmdletBinding(SupportsShouldProcess)]` et un appel à `ShouldProcess` (détaillé au Ch.33). On approfondit `[CmdletBinding()]` au Ch.7 (fonctions).

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Écris `Test-ServicePresent.ps1` avec un paramètre obligatoire `-ServiceName`. Le script affiche si le service existe (`Get-Service -Name $ServiceName -ErrorAction SilentlyContinue`) et son statut.

**Autonome :** Ajoute un paramètre `-Start` de type `[switch]`. Si présent et que le service est arrêté, le script le démarre. (On verra les conditions `if` au Ch.5 — ici, un simple `if ($Start) { ... }` suffit.)

## ✅ Tu sais maintenant...

- Passer des arguments (`$args`) et, mieux, déclarer des paramètres avec `param()`
- Rendre un paramètre obligatoire, typé, avec valeur par défaut
- Les `[switch]` et la validation (`ValidateSet`, `ValidateRange`…)
- Pourquoi les paramètres rendent un script **automatisable**
- Le splatting pour les appels à nombreux paramètres

## 💬 Questions d'entretien typiques

- **Pourquoi `param()` plutôt que `$args` ?** → Paramètres nommés, typés, validés, avec valeurs par défaut et tab-complétion. Plus robuste et automatisable.
- **Comment forcer un paramètre à faire partie d'une liste de valeurs ?** → `[ValidateSet("a","b","c")]`, qui rejette les autres valeurs et active l'autocomplétion.
- **Qu'est-ce que le splatting ?** → Passer les paramètres d'une cmdlet via une hashtable projetée avec `@`, pour la lisibilité et la construction dynamique d'appels.

---
