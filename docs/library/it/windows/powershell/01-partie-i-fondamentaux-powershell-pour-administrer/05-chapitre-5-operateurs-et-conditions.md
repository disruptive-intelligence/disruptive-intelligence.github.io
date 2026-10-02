---
title: Chapitre 5 — Opérateurs et conditions
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Les opérateurs de comparaison

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

### Les opérateurs logiques

```powershell
$FreeGB -lt 10 -and $svc.Status -eq "Running"     # les deux vraies
$Role -eq "admin" -or $Role -eq "operator"        # au moins une
-not ($svc.Status -eq "Running")                   # négation
```


`-and`, `-or`, `-not` (Bash : `&&`, `||`, `!` ; Python : `and`, `or`, `not`).

### Manipuler le texte : opérateurs de chaînes

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

### Vérifier une existence : `Test-Path` et compagnie

Les cmdlets `Test-*` renvoient un booléen (`$true`/`$false`) — parfaites pour les conditions :

```powershell
Test-Path "C:\Scripts"                    # le dossier existe ?
Test-Path "HKLM:\SOFTWARE\MonApp"          # la clé de registre existe ?
Test-Connection SRV01 -Count 1 -Quiet      # la machine répond au ping ?
```


> **📌 Réflexe `Get`/`Test` avant d'agir :** ces cmdlets incarnent la discipline d'administration. Avant de créer un dossier, `Test-Path`. Avant de configurer une machine, `Test-Connection`. On vérifie l'état **avant** de modifier.

### Les conditions : `if` / `elseif` / `else`

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

### Un cas d'administration complet

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


### Le `switch` : choix multiples

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


## 🟡 Très utile en pratique

### Comparaisons et pipeline : la même logique

`Where-Object { $_.Status -eq "Running" }` (Ch.4) utilise exactement ces opérateurs. Un `if` teste **une** valeur ; `Where-Object` applique le même test à **chaque objet** du pipeline. Même grammaire, deux usages.

### L'opérateur ternaire `[⚡ PS7+]`

```powershell
$etat = $svc.Status -eq "Running" ? "OK" : "PROBLEME"
```


En 5.1, utilise un `if`/`else` classique.

## 🔴 Bonus

### `-match` et la variable `$Matches`

Après un `-match` réussi, `$Matches` contient les groupes capturés :

```powershell
if ("user@lab.local" -match "^(.+)@(.+)$") {
    $Matches[1]   # user
    $Matches[2]   # lab.local
}
```


Très utile pour extraire des morceaux d'un log, d'un DN, d'une adresse.

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Écris un script qui prend un `-ServiceName` et affiche en couleur : vert si Running, rouge si Stopped, jaune sinon. Utilise `switch`.

**Autonome :** Écris un script qui vérifie l'espace libre de `C:` et affiche une alerte si moins de 15 Go. Ajoute un test : si en plus le service `wuauserv` (Windows Update) tourne, suggère de le mettre en pause (message seulement).

## ✅ Tu sais maintenant...

- Les opérateurs de comparaison (`-eq`, `-lt`, `-like`, `-match`…) et logiques (`-and`, `-or`, `-not`)
- Les opérateurs et méthodes de chaîne (`-split`, `-replace`, `.Trim()`, `.Split()`…) — cruciaux pour DN, chemins, URIs
- `Test-Path` / `Test-Connection` et la discipline `Test` avant d'agir
- `if` / `elseif` / `else` et `switch` (avec motifs)

## 💬 Questions d'entretien typiques

- **Comment teste-t-on l'égalité en PowerShell ?** → `-eq` (insensible à la casse ; `-ceq` pour la casse). `==` n'existe pas ; `=` est une affectation.
- **Comment extraire le domaine de `user@lab.local` ?** → `-match "@(.+)$"` puis `$Matches[1]`, ou `.Split("@")[1]`.
- **`Where-Object` et `if`, quel rapport ?** → Même grammaire de comparaison ; `if` teste une valeur, `Where-Object` applique le test à chaque objet du pipeline.

---
