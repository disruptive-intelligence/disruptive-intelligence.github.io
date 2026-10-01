---
title: Chapitre 4 — Le pipeline et les objets
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Pourquoi ce chapitre est LE plus important

Si tu ne retiens qu'une chose de tout le cours, retiens ceci : **en PowerShell, le pipeline transporte des objets, pas du texte.** C'est ce qui le rend radicalement différent de Bash, et c'est ce qui rend l'administration Windows si efficace.

### Le pipeline : texte (Bash) vs objets (PowerShell)

**En Bash** : `ps aux | grep firefox | awk '{print $2}'`

- `ps` produit du **texte** ; `grep` filtre des lignes de texte ; `awk` découpe la 2ᵉ colonne de texte. Si le format d'affichage change, tout casse.

**En PowerShell** : `Get-Process firefox | Select-Object Id`

- `Get-Process` produit des **objets processus** ; chaque objet a des propriétés (`Name`, `Id`, `CPU`, `WorkingSet64`…) ; `Select-Object` lit directement la propriété `Id`. Aucun texte à découper, rien ne casse.

> **À garder en tête tout le cours :** les pipelines Unix manipulent des flux de texte ; le pipeline PowerShell manipule des **propriétés d'objets**. C'est la différence fondamentale.

### Voir les objets en action

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

### `Get-Member` : LA commande pour explorer

C'est le réflexe central de PowerShell. `Get-Member` révèle **tout** ce que contient un objet :

```powershell
Get-Service | Get-Member
```


La sortie liste :

- les **propriétés** (les informations : `Name`, `Status`, `StartType`…)
- les **méthodes** (les actions : `Start()`, `Stop()`, `Restart()`…)

> **📌 Réflexe transversal.** Tu récupères un objet inconnu ? Passe-le dans `Get-Member`. Ce cours te le rappellera à chaque nouvel objet : service, utilisateur AD, tâche planifiée, réponse d'API… La démarche est toujours la même. C'est le meilleur réflexe PowerShell qui soit.

### Les 5 cmdlets du pipeline

| Cmdlet | Rôle | Analogie Bash |
|--------|------|--------------|
| `Where-Object` | **Filtrer** les objets selon une condition | `grep` |
| `Select-Object` | **Choisir** des propriétés (ou les N premiers) | `cut` / `awk` |
| `Sort-Object` | **Trier** par une propriété | `sort` |
| `Measure-Object` | **Compter**, additionner, moyenner | `wc` |
| `ForEach-Object` | **Agir** sur chaque objet | boucle `for` |

### Filtrer avec `Where-Object`

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

### Sélectionner avec `Select-Object`

```powershell
Get-Service | Select-Object Name, Status, StartType    # certaines propriétés
Get-Process | Select-Object -First 5                    # les 5 premiers
Get-Process | Select-Object Name, Id -Last 3            # les 3 derniers
```


### Trier avec `Sort-Object`

```powershell
# Les 10 processus les plus gourmands en mémoire
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id -First 10
```


### Compter et calculer avec `Measure-Object`

```powershell
(Get-Service).Count                              # nombre de services (rapide)
Get-Process | Measure-Object WorkingSet64 -Sum   # mémoire totale utilisée
```


### Agir avec `ForEach-Object`

```powershell
# Afficher un message pour chaque service arrêté
Get-Service | Where-Object Status -eq "Stopped" | ForEach-Object {
    Write-Output "Arrêté : $($_.Name)"
}
```


### Un pipeline complet, réaliste

Les 10 processus les plus gourmands, avec la RAM en Mo (propriété **calculée**) :

```powershell
Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{ Name = "RAM(Mo)"; Expression = { [math]::Round($_.WorkingSet64/1MB) } } |
    Select-Object -First 10
```


La syntaxe `@{ Name = "..."; Expression = { ... } }` crée une colonne calculée à la volée. On l'écrit souvent en abrégé `@{ N=...; E={...} }`.

## 🟡 Très utile en pratique

### Exporter les résultats (et le piège `Format-Table`)

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

### `Out-GridView` : une fenêtre interactive `[🪟 Windows]`

```powershell
Get-Service | Out-GridView    # tableau graphique triable/filtrable
```


## 🔴 Bonus

### Les propriétés calculées, plus loin

On peut enchaîner plusieurs propriétés calculées pour bâtir un rapport sur mesure — on s'en servira beaucoup pour les inventaires (Ch.14) et les rapports AD (Ch.24).

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Liste les services arrêtés dont le démarrage est `Automatic` (une anomalie fréquente), triés par nom, et affiche `Name` + `DisplayName`.

**Autonome :** Affiche les 5 processus les plus gourmands en mémoire avec une colonne calculée « RAM(Mo) », puis exporte le résultat complet (tous les processus, pas seulement 5) en CSV.

## 🧩 Mini-projet — Top consommateurs

Crée `Get-TopProcess.ps1` avec un paramètre `-Count` (défaut 10) qui affiche les N processus les plus gourmands en mémoire (nom, PID, RAM en Mo via propriété calculée) **et** affiche en vert le total de RAM consommée par ces N processus. Réutilise `param()` (Ch.3), le pipeline, la propriété calculée et `Measure-Object`.

## ✅ Tu sais maintenant...

- Le pipeline transporte des **objets**, pas du texte
- `$_` = l'objet courant ; `Get-Member` = le réflexe d'exploration
- `Where-Object` / `Select-Object` / `Sort-Object` / `Measure-Object` / `ForEach-Object`
- Les propriétés calculées `@{N=...;E={...}}`
- Exporter en CSV/JSON, et **ne jamais** mettre `Format-*` avant un traitement

## 💬 Questions d'entretien typiques

- **Quelle est LA différence entre le pipeline Bash et PowerShell ?** → Bash transporte du texte à parser ; PowerShell transporte des objets dont on lit les propriétés directement.
- **Que fait `Get-Member` ?** → Il révèle les propriétés et méthodes d'un objet. C'est l'outil pour explorer tout objet inconnu.
- **Pourquoi ne pas mettre `Format-Table` au milieu d'un pipeline ?** → Il convertit les objets en instructions d'affichage : plus rien n'est exploitable ensuite (filtrage, export). `Format-*` va en tout dernier, pour l'écran uniquement.

---
