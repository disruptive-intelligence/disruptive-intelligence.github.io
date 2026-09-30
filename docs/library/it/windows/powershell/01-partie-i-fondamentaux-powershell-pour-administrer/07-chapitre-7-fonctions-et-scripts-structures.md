---
title: Chapitre 7 — Fonctions et scripts structurés
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux powershell pour administrer windows
  - index.md
---

## 🟢 Le minimum à savoir

### Pourquoi des fonctions ?

Jusqu'ici, tes scripts étaient linéaires. Dès qu'une logique se répète (vérifier un service, tester une machine, produire une ligne de rapport), on la range dans une **fonction** : un bloc nommé, réutilisable, testable. C'est le premier pas vers des outils d'administration propres.

### Définir et appeler une fonction

```powershell
function Get-Uptime {
    $os = Get-CimInstance Win32_OperatingSystem
    (Get-Date) - $os.LastBootUpTime
}

Get-Uptime        # appel : on écrit juste son nom
```


> **Convention :** nomme tes fonctions en `Verbe-Nom`, comme les cmdlets (`Get-Uptime`, `Test-ServerHealth`). Utilise des verbes approuvés (liste : `Get-Verb`). Ça rend tes fonctions cohérentes avec l'écosystème PowerShell.

### Paramètres de fonction

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


### Le return implicite : LE piège à comprendre

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

### `return` existe (mais ne fait pas ce que tu crois)

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

### La portée des variables (scope)

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

## 🟡 Très utile en pratique

### `[CmdletBinding()]` : transformer une fonction en outil pro

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

### Placer ses fonctions dans un script

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


## 🔴 Bonus

### `begin` / `process` / `end` : accepter le pipeline

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

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Écris une fonction `Test-DiskSpace` qui prend `-Drive` (ex : `"C"`) et `-MinFreeGB` (défaut 10), et renvoie un PSCustomObject `{ Lecteur; LibreGB; Conforme }`.

**Autonome :** Écris `Get-ServiceStatus` qui accepte plusieurs noms de services et renvoie un PSCustomObject par service. Appelle-la puis exporte le résultat en CSV.

## ✅ Tu sais maintenant...

- Définir des fonctions `Verbe-Nom` avec `param()`
- Le **return implicite** et comment garder une fonction propre (`Write-Verbose`)
- La portée locale des variables et pourquoi éviter les variables globales
- `[CmdletBinding()]` pour des fonctions avec paramètres communs
- Le pattern « une fonction renvoie des objets, elle ne les affiche pas »

## 💬 Questions d'entretien typiques

- **Comment une fonction PowerShell renvoie-t-elle une valeur ?** → Tout ce qui n'est pas capturé/redirigé est renvoyé ; `return` sert surtout à sortir tôt.
- **Pourquoi `Write-Verbose` plutôt que `Write-Output` pour un message ?** → `Write-Output` polluerait la valeur de retour ; `Write-Verbose` ne s'affiche qu'avec `-Verbose` et n'entre pas dans la sortie.
- **À quoi sert `[CmdletBinding()]` ?** → À obtenir les paramètres communs (`-Verbose`, `-ErrorAction`, support de `-WhatIf`…) et faire de la fonction un outil « avancé ».

---
