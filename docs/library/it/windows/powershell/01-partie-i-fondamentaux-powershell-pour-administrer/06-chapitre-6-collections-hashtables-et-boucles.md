---
title: Chapitre 6 — Collections, hashtables et boucles
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Les tableaux (arrays)

Un tableau regroupe plusieurs valeurs. En administration, c'est typiquement **une liste de machines** :

```powershell
$Serveurs = @("DC01", "SRV01", "SRV-WEB01")

$Serveurs[0]           # DC01 (premier)
$Serveurs[-1]          # SRV-WEB01 (dernier)
$Serveurs.Count        # 3
$Serveurs += "SRV02"   # ajoute (crée un nouveau tableau — lent en boucle serrée)
$Serveurs -contains "DC01"    # True
```


### Les hashtables (dictionnaires clé-valeur)

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

### Le PSCustomObject : construire des objets pour tes rapports

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


### Les boucles

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

### `foreach` (mot-clé) vs `ForEach-Object` (pipeline)

```powershell
# foreach : la collection est déjà en mémoire
$services = Get-Service
foreach ($s in $services) { $s.Name }

# ForEach-Object : traite les objets au fil du pipeline (économe en mémoire)
Get-Service | ForEach-Object { $_.Name }
```


Les deux existent, choisis selon le contexte. En pipeline, c'est `ForEach-Object` (avec `$_`).

## 🟡 Très utile en pratique

### Construire un rapport de parc

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

### Performance : `+=` sur un gros tableau

`$tab += $x` recrée tout le tableau à chaque ajout — lent sur des milliers d'éléments. Alternative :

```powershell
$liste = [System.Collections.Generic.List[object]]::new()
$liste.Add($x)
```


Pour débuter, `+=` suffit sur de petits volumes ; retiens juste que ça ne passe pas à l'échelle.

## 🔴 Bonus

### Parcours parallèle `[⚡ PS7+]`

PowerShell 7 permet `ForEach-Object -Parallel` pour traiter plusieurs machines en même temps :

```powershell
$Serveurs | ForEach-Object -Parallel { Test-Connection $_ -Count 1 -Quiet } -ThrottleLimit 5
```


Puissant pour l'inventaire d'un grand parc — on en reparle en Partie VI.

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Crée un tableau de 3 noms de services critiques (`"Spooler"`, `"wuauserv"`, `"EventLog"`). Parcours-le avec `foreach` et affiche l'état de chacun en couleur.

**Autonome :** Transforme le résultat précédent en tableau de PSCustomObject (`Service`, `Statut`, `DemarrageAuto`) et exporte-le en CSV.

## 🧩 Mini-projet — Supervision de services critiques

Crée `Test-CriticalServices.ps1` qui : prend un paramètre `-Services` (tableau, avec une valeur par défaut de 3-4 services), parcourt la liste, construit un PSCustomObject par service (Nom, Statut, TypeDémarrage, Conforme), affiche le tout en table, et exporte en CSV. Réutilise `param()` (Ch.3), le pipeline (Ch.4), les conditions (Ch.5) et les collections (Ch.6). *(Pour le type de démarrage portable en 5.1 comme en 7, tu utiliseras `Get-CimInstance Win32_Service` et sa propriété `StartMode` — détaillé au Ch.11.)*

## ✅ Tu sais maintenant...

- Créer et manipuler tableaux (`@()`) et hashtables (`@{}`)
- Fabriquer des **PSCustomObject** pour des rapports propres
- Les boucles `foreach` / `for` / `while` / `do` et `break`/`continue`
- La différence `foreach` (mot-clé) vs `ForEach-Object` (pipeline)
- Produire un tableau d'objets depuis une boucle (pattern d'inventaire)

## 💬 Questions d'entretien typiques

- **Comment produire un rapport structuré exportable en CSV ?** → Construire des `[PSCustomObject]` (une propriété par colonne), les collecter dans un tableau, puis `Export-Csv`.
- **`foreach` ou `ForEach-Object` ?** → `foreach` quand la collection est en mémoire ; `ForEach-Object` dans un pipeline (plus économe, utilise `$_`).
- **Pourquoi `$tab += $x` est déconseillé en masse ?** → Il recrée le tableau à chaque ajout ; sur de gros volumes, on utilise une `List[object]`.

---
