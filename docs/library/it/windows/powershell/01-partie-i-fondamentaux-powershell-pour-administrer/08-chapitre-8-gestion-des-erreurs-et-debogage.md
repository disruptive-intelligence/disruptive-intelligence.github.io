---
title: Chapitre 8 — Gestion des erreurs et débogage
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Pourquoi c'est vital en administration

Un script d'administration touche à de vraies machines. S'il plante silencieusement au milieu d'une boucle sur 200 serveurs, ou s'il continue comme si de rien n'était après un échec, les dégâts peuvent être réels. Savoir **détecter, intercepter et journaliser** les erreurs est une compétence non négociable.

### Erreurs terminantes vs non-terminantes : la distinction clé

PowerShell a **deux** sortes d'erreurs, et c'est LE point à comprendre :

- **Non-terminante** : la cmdlet signale un problème mais **continue** (et le script continue). C'est le cas par défaut de la plupart des cmdlets. Exemple : `Get-Service "Absent1","Spooler"` affiche une erreur pour `Absent1` mais renvoie quand même `Spooler`.
- **Terminante** : l'exécution **s'arrête** (erreur de syntaxe, exception .NET, ou erreur non-terminante que tu as *promue* en terminante).

Le problème : un `try/catch` (voir plus bas) n'attrape **que les erreurs terminantes**. Une erreur non-terminante passe à travers le `catch` sans le déclencher. D'où la nécessité de `-ErrorAction Stop`.

### `-ErrorAction` : contrôler le comportement

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


### `try` / `catch` / `finally`

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

### Un exemple d'administration réel

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

### `$?` et `$LASTEXITCODE` : deux indicateurs à ne pas confondre

```powershell
Get-Service Spooler
$?               # $true si la DERNIÈRE commande PowerShell a réussi, $false sinon

ping SRV01
$LASTEXITCODE    # code de sortie du dernier PROGRAMME EXTERNE (ping.exe) : 0 = succès
```


- `$?` : booléen, indique le **succès de la dernière opération** — cmdlet **ou** commande native. Pour un exécutable externe, `$?` passe à `$true` si le code de sortie est `0`, `$false` sinon. Il ne dit **pas** *quel* code : juste réussi/échoué. Il se remet à jour à **chaque** commande — capture-le tout de suite.
- `$LASTEXITCODE` : entier, donne le **code de sortie exact** du dernier **programme externe** (`ping`, `robocopy`, `git`…). Convention Unix : `0` = succès, autre = erreur (et la valeur précise peut renseigner sur la cause).

> **En pratique :** `$?` = « ça a réussi, oui ou non ? » (booléen, marche pour tout) ; `$LASTEXITCODE` = « quel code exact a renvoyé l'exécutable ? » (entier, exécutables natifs seulement). Pour tester finement le résultat d'un `.exe`, préfère `$LASTEXITCODE -eq 0` plutôt que `$?`, car tu récupères la valeur exacte. Et `$?` est fugace : `Get-Service; Write-Host "x"; $?` te donne le succès du `Write-Host`, pas du `Get-Service`.

## 🟡 Très utile en pratique

### La variable `$Error`

PowerShell garde l'historique des erreurs dans `$Error` (un tableau, la plus récente en `[0]`) :

```powershell
$Error[0]                      # la dernière erreur
$Error[0].Exception.Message    # son message
$Error.Clear()                 # vider l'historique
```


Pratique pour le débogage : après un souci, `$Error[0] | Format-List *` donne tous les détails.

### Les messages de diagnostic

PowerShell a plusieurs « flux » de sortie dédiés — utilise le bon selon l'intention :

```powershell
Write-Verbose "Détail affiché avec -Verbose"      # diagnostic (nécessite CmdletBinding)
Write-Warning "Avertissement (jaune)"             # avertissement visible
Write-Error   "Erreur non-terminante"             # erreur (rouge), sans stopper
Write-Debug   "Message de débogage (-Debug)"      # débogage
```


> **Bonne pratique :** ne mélange pas tes **données** (via `Write-Output`/objets) et tes **messages** (via ces flux). C'est ce qui rend un script à la fois exploitable en pipeline *et* lisible par un humain.

### `Set-StrictMode` : le filet anti-bugs

`Set-StrictMode` force PowerShell à signaler les erreurs silencieuses classiques (variable non définie, propriété inexistante) :

```powershell
Set-StrictMode -Version Latest

$Total = $Compteur + 1    # ❌ erreur claire si $Compteur n'a jamais été défini
```


Sans lui, `$Compteur` non défini vaudrait `$null` (donc `0`) et le bug passerait inaperçu. Mets-le en tête de tes scripts sérieux.

### L'aide basée sur les commentaires

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


## 🔴 Bonus

### Attraper des erreurs spécifiques

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


### Le point d'arrêt et le débogage pas-à-pas

Dans VS Code, tu peux poser des points d'arrêt (clic dans la marge, ou `Set-PSBreakpoint`) et exécuter le script pas-à-pas pour inspecter les variables. Indispensable quand un script se comporte de façon inattendue.

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Écris un script qui tente `Restart-Service -Name $ServiceName -ErrorAction Stop` dans un `try/catch` et affiche un message vert en cas de succès, rouge (avec `$_.Exception.Message`) en cas d'échec.

**Autonome :** Reprends ton script de supervision de services (Ch.6) et entoure chaque vérification d'un `try/catch` pour qu'un service inexistant n'interrompe pas la boucle. Ajoute `Set-StrictMode -Version Latest` en tête.

## 🧩 Capstone Partie I — `Get-ServerHealth.ps1`

Assemble tout ce que tu as appris dans un outil complet :

- **Paramètres** (`-ComputerName` avec tableau possible, `-MinFreeGB`) — Ch.3
- Une **fonction** `Test-ServerHealth` documentée (aide par commentaires) — Ch.7
- Un **pipeline** qui produit un PSCustomObject par serveur (nom, en ligne, espace disque, uptime, statut global) — Ch.4, Ch.6
- Des **conditions** pour déterminer le statut (OK / Alerte) — Ch.5
- Un **try/catch** par serveur pour la robustesse + `Set-StrictMode` — Ch.8
- Un **export CSV** du rapport final

C'est le premier vrai outil d'administration du cours. On le fera évoluer : disque (Ch.14), réseau (Ch.18), exécution à distance (Ch.29).

## ✅ Tu sais maintenant...

- La différence **erreur terminante / non-terminante** et pourquoi `-ErrorAction Stop` est indispensable
- `try` / `catch` / `finally` pour intercepter et nettoyer
- `$?` = succès **booléen** de la dernière opération (cmdlet **ou** natif) ; `$LASTEXITCODE` = **code numérique exact** du dernier programme natif
- `$Error`, les flux `Write-Verbose`/`Warning`/`Error`/`Debug`
- `Set-StrictMode` et l'aide par commentaires

## 💬 Questions d'entretien typiques

- **Pourquoi un `try/catch` ne capture-t-il parfois rien ?** → Parce que l'erreur est non-terminante ; il faut `-ErrorAction Stop` pour la rendre terminante.
- **Différence entre `$?` et `$LASTEXITCODE` ?** → `$?` = succès booléen de la dernière opération, cmdlet **ou** exécutable (`$true` si code 0 pour un natif) ; `$LASTEXITCODE` = code de sortie **numérique exact** du dernier exécutable externe. Pour tester finement un `.exe`, on utilise `$LASTEXITCODE`.
- **Comment éviter qu'un serveur injoignable casse une boucle sur tout un parc ?** → Mettre le traitement de chaque serveur dans un `try/catch` avec `-ErrorAction Stop`, pour isoler les échecs.
- **À quoi sert `Set-StrictMode` ?** → À transformer en erreurs les pièges silencieux (variables/propriétés inexistantes), ce qui fiabilise les scripts.

---
