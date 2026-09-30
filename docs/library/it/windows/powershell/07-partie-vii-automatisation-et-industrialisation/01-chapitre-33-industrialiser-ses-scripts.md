---
title: Chapitre 33 — Industrialiser ses scripts
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VII — Automatisation ET industrialisation
  - index.md
---

## 🟢 Le minimum à savoir

### Des scripts aux modules

Un **module** regroupe des fonctions réutilisables dans un fichier `.psm1`, qu'on importe comme les modules natifs. C'est ainsi qu'on capitalise : au lieu de copier-coller `Test-ServerHealth` dans dix scripts, on la range dans un module.

```powershell
# MonModule.psm1 — plusieurs fonctions réutilisables
function Test-ServerHealth { <# ... #> }
function Get-DiskAlert     { <# ... #> }
Export-ModuleMember -Function Test-ServerHealth, Get-DiskAlert
```


```powershell
# Utilisation
Import-Module .\MonModule.psm1
Test-ServerHealth -ComputerName SRV01
```


Un module bien rangé (dans un dossier du `$env:PSModulePath`) devient disponible partout, comme les cmdlets natives.

### Le splatting pour des appels lisibles

Rappel du Ch.3, désormais systématique dès qu'un appel a plus de 3-4 paramètres :

```powershell
$params = @{
    Name          = "svc_backup"
    Path          = "OU=Services,DC=lab,DC=local"
    AccountPassword = $pwd
    Enabled       = $true
    ChangePasswordAtLogon = $true
}
New-ADUser @params      # bien plus lisible qu'une ligne à rallonge avec des backticks
```


### Externaliser la configuration

Un bon script ne code pas ses valeurs en dur : serveurs, seuils, chemins vont dans un fichier de config (JSON, souvent) qu'on lit au démarrage :

```powershell
# config.json
# { "Serveurs": ["DC01","SRV01"], "SeuilDisqueGB": 20, "Rapport": "C:\\rapports" }

$config = Get-Content ".\config.json" -Encoding UTF8 | ConvertFrom-Json
$config.Serveurs | ForEach-Object { Test-ServerHealth -ComputerName $_ }
```


Changer un seuil ou ajouter un serveur ne demande alors plus de toucher au code — juste la config.

### Journaliser (logs)

Un script de production doit laisser une trace exploitable :

```powershell
function Write-Log {
    param([string]$Message, [ValidateSet("INFO","WARN","ERROR")][string]$Level = "INFO")
    $ligne = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') [$Level] $Message"
    $ligne | Add-Content -Path "C:\logs\script.log" -Encoding UTF8
    if ($Level -eq "ERROR") { Write-Host $ligne -ForegroundColor Red }
}

Write-Log "Début du traitement" -Level INFO
Write-Log "Serveur injoignable" -Level ERROR
```


## 🟡 Très utile en pratique

### Gérer les secrets proprement

> **⚠️ Rappel des Ch.10, 20, 30 : un secret ne s'écrit JAMAIS en clair dans un script.** Voici les mécanismes propres, du plus simple au plus robuste.

**SecureString** — pour ne pas manipuler un mot de passe en clair en mémoire :

```powershell
$pwd = Read-Host "Mot de passe" -AsSecureString      # saisie masquée
# ou, à partir d'un texte (ex : mot de passe généré), sans jamais l'écrire en dur
```


**Le module SecretManagement** — un coffre-fort pour les secrets, la vraie bonne pratique :

```powershell
Install-Module Microsoft.PowerShell.SecretManagement, Microsoft.PowerShell.SecretStore -Scope CurrentUser
Register-SecretVault -Name Coffre -ModuleName Microsoft.PowerShell.SecretStore -DefaultVault

# Stocker SANS écrire le secret sur la ligne de commande (sinon il finit dans l'historique !)
$secret = Read-Host "Valeur du secret" -AsSecureString
Set-Secret -Name "ApiToken" -SecureStringSecret $secret     # stocker (chiffré)

$token = Get-Secret -Name "ApiToken" -AsPlainText            # récupérer au moment de l'usage
```


> **⚠️ Ne mets jamais le secret en clair sur la ligne `Set-Secret`.** Écrire `Set-Secret -Secret "valeur-du-token"` place la valeur dans l'**historique** de ta console (`Get-History`, fichier `PSReadLine`) — une fuite. Saisis-le via `Read-Host -AsSecureString` (masqué, non historisé), comme ci-dessus.

Ainsi, le secret n'apparaît **jamais** dans le code source ni dans l'historique. C'est ce qu'on utilise pour les tokens d'API (Ch.30-31), les identifiants Graph applicatifs (Ch.32), les mots de passe de comptes de service.

**Générer un mot de passe initial aléatoire** (pour l'onboarding, Ch.24). Deux exigences : un **générateur cryptographique** (`RandomNumberGenerator`, pas `Get-Random`), **et** une **composition garantie** (AD peut exiger au moins 3 catégories parmi majuscule/minuscule/chiffre/symbole). On tire donc au moins un caractère de chaque catégorie, puis on complète, puis on mélange :

```powershell
function New-RandomPassword {
    param(
        # Validation (Ch.3) : en dessous de 8, la garantie « une majuscule + une minuscule
        # + un chiffre + un symbole » deviendrait plus longue que le mot de passe demandé.
        [ValidateRange(8, 128)]
        [int]$Length = 16
    )

    # RNG cryptographique : renvoie un entier dans [0, max)
    function Get-CryptoIndex([int]$max) {
        $bytes = [byte[]]::new(4)
        $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
        try { $rng.GetBytes($bytes) } finally { $rng.Dispose() }
        # ToUInt32 (non signé) plutôt que ToInt32 + [math]::Abs() : Abs() lèverait une
        # exception sur Int32.MinValue, dont la valeur absolue n'est pas représentable.
        [int]([BitConverter]::ToUInt32($bytes, 0) % $max)
    }

    $cat = @{
        Maj = "ABCDEFGHJKLMNPQRSTUVWXYZ"
        Min = "abcdefghijkmnpqrstuvwxyz"
        Chi = "23456789"
        Sym = "!@#%*-_"
    }

    # 1. Garantir AU MOINS un caractère de chaque catégorie (conformité AD)
    $chars = foreach ($set in $cat.Values) { $set[(Get-CryptoIndex $set.Length)] }

    # 2. Compléter jusqu'à la longueur voulue depuis l'ensemble complet
    $tous = -join $cat.Values
    while ($chars.Count -lt $Length) { $chars += $tous[(Get-CryptoIndex $tous.Length)] }

    # 3. Mélanger l'ordre (sinon les 4 premiers seraient toujours Maj/Min/Chi/Sym)
    $melange = $chars | Sort-Object { Get-CryptoIndex 100000 }
    -join $melange
}
```


> **Pourquoi ces deux exigences ?** D'abord, `Get-Random` s'appuie sur un générateur pseudo-aléatoire **non cryptographique** : suffisant pour choisir un élément au hasard, mais **inadapté** aux secrets (prévisibilité théorique) — d'où `RandomNumberGenerator`. Ensuite, un simple tirage dans un pool mixte **ne garantit pas** la présence de chaque catégorie : un mot de passe pourrait, par malchance, ne contenir aucun chiffre et être **rejeté** par la politique AD. En imposant un caractère de chaque catégorie avant de compléter, on est toujours conforme.

### L'idempotence

Un script **idempotent** produit le même état final qu'on le lance une ou dix fois. C'est essentiel en automatisation : on vérifie **avant** d'agir (la discipline `Get`/`Test` de tout le cours).

```powershell
# ❌ NON idempotent : échoue au 2e passage (le compte existe déjà)
New-ADUser -Name "X" ...

# ✅ Idempotent : ne crée que si absent
if (-not (Get-ADUser -Filter "SamAccountName -eq 'x'" -ErrorAction SilentlyContinue)) {
    New-ADUser -Name "X" ...
}
```


### `-WhatIf`, `-Confirm` et `ShouldProcess`

Rappel du Ch.24, généralisé. Pour qu'une **fonction maison** supporte `-WhatIf`/`-Confirm`, on ajoute `SupportsShouldProcess` et on encadre les actions modifiantes :

```powershell
function Remove-OldUser {
    [CmdletBinding(SupportsShouldProcess)]
    param([Parameter(Mandatory)][string]$SamAccountName)

    $user = Get-ADUser -Identity $SamAccountName -ErrorAction Stop
    if ($PSCmdlet.ShouldProcess($SamAccountName, "Désactiver et déplacer")) {
        Disable-ADAccount -Identity $user
        Move-ADObject -Identity $user.DistinguishedName -TargetPath "OU=Départs,DC=lab,DC=local"
    }
}

Remove-OldUser -SamAccountName jdupont -WhatIf     # simule
Remove-OldUser -SamAccountName jdupont -Confirm    # demande confirmation
```


Tes propres outils gagnent ainsi le même filet de sécurité que les cmdlets natives — la marque d'un script professionnel.

### Robustesse : retries

Une opération réseau peut échouer temporairement. Un **retry** (nouvelle tentative) évite d'abandonner à la première erreur passagère :

```powershell
function Invoke-WithRetry {
    param([scriptblock]$Action, [int]$MaxRetries = 3, [int]$DelaySeconds = 5)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try { return & $Action }
        catch {
            if ($i -eq $MaxRetries) { throw }
            Write-Warning "Tentative $i échouée, nouvel essai dans $DelaySeconds s..."
            Start-Sleep -Seconds $DelaySeconds
        }
    }
}

Invoke-WithRetry -Action { Invoke-RestMethod -Uri "https://api.exemple.com/data" }
```


## 🔴 Bonus

### Tester ses scripts avec Pester

**Pester** est le framework de test de PowerShell. Pourquoi tester un script d'administration ? Parce qu'un script qui crée des comptes ou supprime des données **doit** se comporter comme prévu — un test attrape une régression avant qu'elle ne casse la production.

```powershell
# MonModule.Tests.ps1
Describe "New-RandomPassword" {
    It "génère un mot de passe de la longueur demandée" {
        (New-RandomPassword -Length 20).Length | Should -Be 20
    }
    It "génère des mots de passe différents à chaque appel" {
        (New-RandomPassword) | Should -Not -Be (New-RandomPassword)
    }
}
```


```powershell
Invoke-Pester .\MonModule.Tests.ps1
```


Pas besoin d'en faire un cours de CI/CD : retiens qu'on **peut** et qu'on **devrait** tester les fonctions critiques. C'est un réflexe de maturité, pas un luxe.

### Vers la CI/CD

À un niveau plus avancé, ces tests s'exécutent automatiquement à chaque modification (GitHub Actions, Azure DevOps…) et la publication des modules se fait sur un dépôt interne. C'est la suite naturelle, hors périmètre de ce cours d'introduction.

## ❌ Erreur classique

```powershell
# Secrets en clair dans le script
$token = "abc123..."     # ❌ fuite garantie si versionné → SecretManagement

# Valeurs codées en dur
$seuil = 20              # ⚠️ à externaliser en config si réutilisé
$config.SeuilDisqueGB    # ✅

# Script non idempotent lancé deux fois
New-ADUser ...           # ❌ échoue au 2e passage
if (-not (Get-ADUser ...)) { New-ADUser ... }   # ✅

# Fonction destructive sans ShouldProcess
function Remove-Stuff { Remove-ADUser ... }      # ❌ pas de -WhatIf possible
[CmdletBinding(SupportsShouldProcess)] + ShouldProcess   # ✅
```


## 💡 Exercices

**Guidé :** Transforme ta fonction `Test-CriticalServices` (Ch.11) en module `.psm1` avec `Export-ModuleMember`, importe-le et utilise-le. Ajoute une fonction `Write-Log`.

**Autonome :** Reprends `Invoke-Offboarding` (Ch.24) et rends-le pleinement professionnel : `SupportsShouldProcess` (`-WhatIf`/`-Confirm`), configuration externe (OU de départ, chemin de log en JSON), journalisation via `Write-Log`, et idempotence (ne rien faire si le compte est déjà désactivé et déplacé).

## 🧩 Capstone Partie VII — Boîte à outils d'administration

Rassemble tes meilleures fonctions dans un module `AdminToolkit.psm1` :

- `Get-ServerHealth` (Ch.8), `Test-CriticalServices` (Ch.11), `Get-DiskAlert` (Ch.14), `Get-NetworkDiagnostic` (Ch.18)
- Avec configuration externe (JSON), journalisation, gestion des secrets (SecretManagement), et `SupportsShouldProcess` sur les fonctions modifiantes
- Documente chaque fonction (aide par commentaires, Ch.8) et ajoute quelques tests Pester

C'est le livrable qui fait passer de « je sais écrire des scripts » à « je livre des outils fiables ».

## ✅ Tu sais maintenant...

- Regrouper des fonctions dans des **modules** (`.psm1`, `Export-ModuleMember`)
- Le **splatting** et la **configuration externe** (JSON) pour des scripts propres
- **Journaliser** (`Write-Log`) et gérer les **secrets** (SecureString, SecretManagement) — jamais en clair
- L'**idempotence** (`Get`/`Test` avant d'agir) et `SupportsShouldProcess` (`-WhatIf`/`-Confirm`)
- Les **retries** pour la robustesse, et l'introduction à **Pester**

## 💬 Questions d'entretien typiques

- **Comment rendre un script rejouable sans effet indésirable ?** → Le rendre idempotent : vérifier l'état avec `Get`/`Test` avant chaque action modifiante.
- **Où stocker un token ou un mot de passe de service ?** → Dans un coffre (SecretManagement) ou un SecureString — jamais en clair dans le code.
- **Comment donner `-WhatIf` à sa propre fonction ?** → `[CmdletBinding(SupportsShouldProcess)]` et encadrer les actions par `$PSCmdlet.ShouldProcess(...)`.
- **Pourquoi tester un script d'administration ?** → Parce qu'il touche à des données réelles (comptes, fichiers) ; un test (Pester) attrape une régression avant la production.

---
