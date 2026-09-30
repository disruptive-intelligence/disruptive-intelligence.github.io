---
title: Chapitre 24 — Administration en masse avec CSV
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### L'objectif : l'onboarding automatisé

C'est le projet phare de la Partie IV, et un classique du métier : **créer des dizaines de comptes AD depuis un fichier CSV** (arrivée d'une promotion, d'un service entier…). Ce chapitre assemble presque tout le cours : `Import-Csv` (Ch.9), boucles (Ch.6), fonctions (Ch.7), gestion d'erreurs (Ch.8), création AD (Ch.20), groupes (Ch.21), OU (Ch.22).

### Le flux complet

```
CSV utilisateurs
      ↓  Import-Csv
validation des données
      ↓  foreach
vérification d'existence (Get-ADUser)
      ↓
New-ADUser (-WhatIf d'abord !)
      ↓
Add-ADGroupMember (groupes)
      ↓
rapport CSV (succès / échecs)
```


### Le fichier CSV de départ

```
GivenName,Surname,SamAccountName,Department,OU,Group
Jean,Dupont,jdupont,Comptabilité,"OU=Compta,DC=lab,DC=local",GG_Compta
Alice,Martin,amartin,IT,"OU=IT,DC=lab,DC=local",GG_IT
Sophie,Bernard,sbernard,IT,"OU=IT,DC=lab,DC=local",GG_IT
```


### Lire et valider

```powershell
$utilisateurs = Import-Csv "C:\onboarding\nouveaux.csv" -Encoding UTF8

# Validation minimale : colonnes attendues présentes et non vides
foreach ($u in $utilisateurs) {
    if (-not $u.SamAccountName -or -not $u.OU) {
        Write-Warning "Ligne invalide ignorée : $($u.GivenName) $($u.Surname)"
        continue
    }
    # ... traitement ...
}
```


### `-WhatIf` : simuler avant d'agir

> **📌 La discipline `Get`/`Test` culmine ici.** Avant de créer 50 comptes pour de vrai, on **simule** avec `-WhatIf`. La plupart des cmdlets de modification (`New-ADUser`, `Set-ADUser`, `Remove-*`, `Add-ADGroupMember`…) acceptent `-WhatIf`, qui affiche ce qui *serait* fait **sans rien faire**.

```powershell
New-ADUser -Name "Test" -SamAccountName test -Path "OU=IT,DC=lab,DC=local" -WhatIf
# → "What if: Performing the operation "New-ADUser" on target "CN=Test,OU=IT,...""
```


C'est le filet de sécurité indispensable pour toute opération de masse. On lance d'abord tout le script en `-WhatIf`, on vérifie la sortie, **puis** on retire le `-WhatIf`.

## 🟡 Le script d'onboarding complet

```powershell
# Invoke-Onboarding.ps1 — Création de comptes AD en masse depuis un CSV
# SÛR PAR DÉFAUT : le script SIMULE. Il faut le lancer avec -Execute pour créer réellement.
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string]$CsvPath,
    [string]$ReportPath = "C:\onboarding\rapport_$(Get-Date -Format yyyyMMdd_HHmmss).csv",
    [switch]$Execute      # SANS ce switch, le script simule (ne crée rien)
)

Import-Module ActiveDirectory
Set-StrictMode -Version Latest

# Sûr par défaut : tant que -Execute n'est pas fourni, on force le mode simulation.
# -WhatIf:$true fait que tous les ShouldProcess n'affichent que ce qui SERAIT fait.
if (-not $Execute) {
    $WhatIfPreference = $true
    Write-Host "MODE SIMULATION (ajoute -Execute pour créer réellement les comptes)" -ForegroundColor Yellow
}

# --- Contrôles PRÉALABLES (Test avant d'agir) -------------------------------
# On vérifie l'environnement AVANT de créer le moindre compte : il serait absurde
# de créer 50 utilisateurs puis de planter au moment d'écrire le rapport.
if (-not (Test-Path $CsvPath -PathType Leaf)) {
    throw "CSV introuvable : $CsvPath"
}
$reportDir = Split-Path -Parent $ReportPath
if (-not (Test-Path $reportDir)) {
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
}

$utilisateurs = Import-Csv $CsvPath -Encoding UTF8
$resultats = [System.Collections.Generic.List[object]]::new()

# Fichier SÉPARÉ pour la remise des mots de passe initiaux (jamais dans le rapport principal).
# À protéger par ACL et à supprimer après distribution (voir note plus bas).
# On dérive son nom de celui du rapport : rapport_xxx.csv → rapport_xxx_secrets.csv
$secretsPath = Join-Path $reportDir `
    ("{0}_secrets.csv" -f [System.IO.Path]::GetFileNameWithoutExtension($ReportPath))
$secrets = [System.Collections.Generic.List[object]]::new()

# Générateur de mot de passe initial, AUTONOME pour ce chapitre.
# (Le Ch.33 montrera une version industrialisée : RNG cryptographique + garantie de complexité.)
function New-InitialPassword {
    param(
        # Validation du paramètre (rappel Ch.3) : en dessous de 8 caractères, un mot de
        # passe initial n'a pas de sens face à une politique de domaine.
        [ValidateRange(8, 128)]
        [int]$Length = 16
    )
    # Pour le lab : simple et lisible. Voir Ch.33 pour la version robuste (cryptographique).
    $maj = "ABCDEFGHJKLMNPQRSTUVWXYZ"; $min = "abcdefghijkmnpqrstuvwxyz"
    $chi = "23456789"; $sym = "!@#%*-_"

    # Garantit au moins un caractère de chaque catégorie (conformité AD, cf. Ch.33).
    # ATTENTION : on travaille avec un TABLEAU de caractères, pas des additions de chars.
    # En PowerShell, [char] + [char] fait une addition NUMÉRIQUE ('A' + 'b' donne 195),
    # pas une concaténation : on assemble donc un tableau et on le -join à la fin.
    $obligatoires = @(
        $maj[(Get-Random -Maximum $maj.Length)]
        $min[(Get-Random -Maximum $min.Length)]
        $chi[(Get-Random -Maximum $chi.Length)]
        $sym[(Get-Random -Maximum $sym.Length)]
    )
    $tout  = ($maj + $min + $chi + $sym).ToCharArray()

    # Garde explicite : NE PAS écrire directement 1..($Length - 4). Si la différence
    # vaut 0, PowerShell évalue 1..0 comme la plage DESCENDANTE @(1, 0) — soit deux
    # caractères de trop. La validation du paramètre seule ne protège pas de ça.
    $reste = @()
    if ($Length -gt $obligatoires.Count) {
        $reste = 1..($Length - $obligatoires.Count) | ForEach-Object { $tout | Get-Random }
    }

    # Mélange final (sinon les 4 premiers seraient toujours Maj/Min/Chiffre/Symbole)
    -join (($obligatoires + $reste) | Sort-Object { Get-Random })
}

foreach ($u in $utilisateurs) {

    $statut = "OK"; $detail = ""

    try {
        # 1. Validation des données du CSV
        if (-not $u.SamAccountName -or -not $u.OU) {
            throw "Données manquantes (SamAccountName ou OU)"
        }

        # 2. Vérifier l'existence du compte (Get avant New)
        $existe = Get-ADUser -Filter "SamAccountName -eq '$($u.SamAccountName)'" -ErrorAction SilentlyContinue
        if ($existe) { throw "Le compte existe déjà" }

        # 3. Vérifier les DÉPENDANCES AVANT de créer quoi que ce soit :
        #    une OU ou un groupe inexistant doit faire échouer AVANT la création,
        #    pas après (sinon on laisse un compte à moitié configuré).
        if (-not (Test-Path "AD:\$($u.OU)")) { throw "OU introuvable : $($u.OU)" }
        if ($u.Group -and -not (Get-ADGroup -Filter "Name -eq '$($u.Group)'" -ErrorAction SilentlyContinue)) {
            throw "Groupe introuvable : $($u.Group)"
        }

        # 4. Créer le compte. ShouldProcess respecte $WhatIfPreference :
        #    en simulation il n'exécute rien, il décrit seulement l'action.
        if ($PSCmdlet.ShouldProcess($u.SamAccountName, "Créer le compte AD")) {
            # Mot de passe initial aléatoire, généré en clair le temps de le poser sur le compte
            $pwdClair = New-InitialPassword
            $motDePasse = ConvertTo-SecureString $pwdClair -AsPlainText -Force
            New-ADUser `
                -Name "$($u.GivenName) $($u.Surname)" `
                -GivenName $u.GivenName -Surname $u.Surname `
                -SamAccountName $u.SamAccountName `
                -UserPrincipalName "$($u.SamAccountName)@lab.local" `
                -Department $u.Department `
                -Path $u.OU `
                -AccountPassword $motDePasse `
                -Enabled $true `
                -ChangePasswordAtLogon $true `
                -ErrorAction Stop

            # 5. Le compte EXISTE désormais → on enregistre IMMÉDIATEMENT son mot de passe.
            #    Si on attendait la fin, un échec à l'étape suivante ferait perdre
            #    la seule information permettant la première connexion.
            $secrets.Add([PSCustomObject]@{
                Utilisateur       = $u.SamAccountName
                MotDePasseInitial = $pwdClair
            })
            $statut = "CRÉÉ"

            # 6. Ajouter au groupe — traité À PART : un échec ici ne doit pas faire
            #    croire que le compte n'a pas été créé (il l'a été, et il est activé).
            if ($u.Group) {
                try {
                    Add-ADGroupMember -Identity $u.Group -Members $u.SamAccountName -ErrorAction Stop
                }
                catch {
                    $statut = "CRÉÉ_PARTIEL"
                    $detail = "Compte créé, mais ajout au groupe '$($u.Group)' échoué : $($_.Exception.Message)"
                }
            }
        }
        else {
            $statut = "SIMULÉ"     # ShouldProcess a refusé l'action (mode simulation)
        }
    }
    catch {
        # On n'arrive ici que si RIEN n'a été créé (validation ou New-ADUser en échec)
        $statut = "ÉCHEC"
        $detail = $_.Exception.Message
    }

    # 5. Journaliser le résultat (SANS le mot de passe)
    $resultats.Add([PSCustomObject]@{
        Utilisateur    = $u.SamAccountName
        Nom            = "$($u.GivenName) $($u.Surname)"
        OU             = $u.OU
        Groupe         = $u.Group
        Statut         = $statut
        Detail         = $detail
    })
}

# 6. Rapport principal (aucun secret dedans)
$resultats | Export-Csv $ReportPath -NoTypeInformation -Encoding UTF8
$resultats | Format-Table -AutoSize

# 6bis. Remise TEMPORAIRE des mots de passe initiaux (fichier séparé, accès restreint, à détruire)
if ($secrets.Count -gt 0) {
    $secrets | Export-Csv $secretsPath -NoTypeInformation -Encoding UTF8
    # Restreindre l'accès au SEUL créateur du fichier.
    #   /inheritance:r  → supprime les autorisations héritées du dossier parent
    #   *<SID>:(F)      → contrôle total pour ce compte, désigné par son SID
    # On cible par SID (préfixe *) et non par nom : cela lève toute ambiguïté entre
    # un compte de domaine DOMAINE\alice et un compte local alice.
    # Et (F) plutôt que (R) : le fichier doit pouvoir être SUPPRIMÉ après distribution.
    $identite = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    icacls $secretsPath /inheritance:r /grant:r "*$($identite.User.Value):(F)" | Out-Null
    Write-Host "Mots de passe initiaux : $secretsPath (À DISTRIBUER PUIS SUPPRIMER)" -ForegroundColor Yellow
}

$crees    = ($resultats | Where-Object Statut -eq "CRÉÉ").Count
$partiels = ($resultats | Where-Object Statut -eq "CRÉÉ_PARTIEL").Count
$simules  = ($resultats | Where-Object Statut -eq "SIMULÉ").Count
$ko       = ($resultats | Where-Object Statut -eq "ÉCHEC").Count
Write-Host "`nTerminé : $crees créé(s), $partiels partiel(s), $simules simulé(s), $ko échec(s). Rapport : $ReportPath" -ForegroundColor Cyan
if ($partiels -gt 0) {
    Write-Host "⚠️  $partiels compte(s) créé(s) mais incomplet(s) — voir la colonne Detail du rapport." -ForegroundColor Yellow
}
```


**Utilisation :**

```powershell
# 1. D'ABORD simuler — c'est le comportement PAR DÉFAUT (rien n'est créé)
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv

# 2. Vérifier la sortie (colonne Statut = SIMULÉ), PUIS exécuter réellement
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv -Execute
```


> **⚠️ Sûr par défaut — le point le plus important de ce script.** Sans `-Execute`, le script **simule** (grâce à `$WhatIfPreference = $true` qui force tous les `ShouldProcess` en mode simulation) : la colonne `Statut` affiche `SIMULÉ` et **aucun compte n'est créé**. Il faut explicitement ajouter `-Execute` pour créer réellement. C'est exactement la philosophie du cours : on observe et on simule avant d'agir. (Tu peux aussi toujours ajouter `-WhatIf` manuellement, qui a le même effet.)

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré.

> **Note sur le mot de passe initial.** Le script est **autonome** : il définit sa propre fonction `New-InitialPassword` (pas de dépendance à un chapitre ultérieur), qui garantit au moins un caractère de chaque catégorie (majuscule, minuscule, chiffre, symbole) pour respecter la politique de complexité AD. Chaque compte reçoit un mot de passe **unique**. Ces mots de passe sont écrits dans un **fichier séparé** (`…secrets.csv`), **jamais dans le rapport principal**, avec un accès **restreint** (`icacls`) : c'est une **remise temporaire à accès restreint** — à distribuer aux utilisateurs, **puis à détruire**. Sans ça, on créerait des comptes… dont personne ne connaît le mot de passe pour la première connexion. (Le terme **stockage sécurisé** est réservé au coffre du Ch.33 : un CSV protégé par ACL n'en est pas un.)

> **🎯 Le vrai sujet d'administration : l'état « partiellement créé ».** Une opération en masse enchaîne plusieurs actions par utilisateur (créer le compte, l'ajouter à un groupe, …). Que se passe-t-il si la **deuxième** échoue ? Le compte existe déjà, activé, mais incomplet. Deux erreurs classiques :
> - Marquer l'utilisateur `ÉCHEC` : faux, et trompeur — au prochain lancement le script dira « le compte existe déjà », et personne ne saura qu'il faut finir le travail.
> - Perdre le mot de passe initial parce qu'on ne l'enregistrait qu'à la toute fin.
>
> Le script traite les deux : il **valide les dépendances (OU, groupe) AVANT** de créer quoi que ce soit — c'est le plus efficace, la plupart des échecs disparaissent —, il **enregistre le mot de passe dès que le compte existe**, et il isole l'ajout au groupe dans son propre `try/catch` pour produire un statut `CRÉÉ_PARTIEL` explicite. On préfère ici un **état honnête et rattrapable** à un rollback automatique (supprimer le compte qu'on vient de créer), plus risqué et plus complexe.
>
> **➡️ Renvoi Ch.33 :** cette gestion reste rudimentaire (fichier à accès restreint). Le Ch.33 l'industrialise : générateur **cryptographique** (`RandomNumberGenerator` plutôt que `Get-Random`) et surtout stockage des secrets dans un **coffre** (SecretManagement/SecretStore) plutôt qu'un fichier plat.

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré, et remise sécurisée des secrets.

## 🔴 Bonus

### Générer un SamAccountName automatiquement

Si le CSV ne fournit pas le `SamAccountName`, on le construit (rappel des méthodes de chaîne, Ch.5) :

```powershell
$sam = ($u.GivenName.Substring(0,1) + $u.Surname).ToLower() -replace '[^a-z]', ''
# Jean Dupont → "jdupont"
```


### Gérer les doublons de SamAccountName

Deux « Jean Dupont » donneraient le même `jdupont`. On teste et on incrémente :

```powershell
$base = $sam; $i = 1
while (Get-ADUser -Filter "SamAccountName -eq '$sam'" -ErrorAction SilentlyContinue) {
    $sam = "$base$i"; $i++
}
```


## ❌ Erreur classique

```powershell
# Bien comprendre le mode par défaut : SANS -Execute, le script SIMULE
.\Invoke-Onboarding.ps1 -CsvPath x.csv             # ✅ SIMULATION (rien n'est créé)
# Le point réellement sensible, c'est l'exécution :
.\Invoke-Onboarding.ps1 -CsvPath x.csv -Execute    # ⚠️ crée réellement les comptes
# → toujours avoir relu la sortie de la simulation AVANT d'ajouter -Execute

# Pas de try/catch → une ligne en erreur arrête tout le lot
foreach ($u in $users) { New-ADUser ... }   # ❌ un échec = tout s'arrête
# ✅ try/catch par utilisateur : on isole les échecs, on continue

# Pas de rapport → impossible de savoir ce qui a réussi/échoué
# ✅ toujours produire un rapport CSV succès/échecs

# Encodage CSV oublié → prénoms accentués cassés
Import-Csv x.csv                    # ⚠️
Import-Csv x.csv -Encoding UTF8     # ✅
```


## 💡 Exercices

**Guidé :** Crée un petit CSV de 3 utilisateurs et lance le script d'onboarding **sans `-Execute`** (mode simulation par défaut). Vérifie que la colonne `Statut` affiche `SIMULÉ` et qu'aucun compte n'est créé. Relance ensuite avec `-Execute` (sur ton lab uniquement).

**Autonome :** Ajoute au script une colonne CSV `Title` et fais en sorte qu'elle soit appliquée (`-Title`). Ajoute aussi la génération automatique du `SamAccountName` avec gestion des doublons (bonus ci-dessus).

## 🧩 Capstone Partie IV — Suite d'onboarding/offboarding

Construis deux scripts complémentaires :

1. **`Invoke-Onboarding.ps1`** (ci-dessus) : création en masse depuis CSV, avec `-WhatIf`, gestion d'erreurs par ligne, et rapport.
2. **`Invoke-Offboarding.ps1`** : pour une liste de `SamAccountName`, **désactive** le compte, le **déplace** vers `OU=Départs`, retire ses groupes, et produit un rapport. Applique la discipline `Get` avant modification et `-WhatIf`.

Ensemble, ils forment un vrai outil de gestion du cycle de vie des comptes — le genre de livrable attendu d'un administrateur junior.

## ✅ Tu sais maintenant...

- Automatiser la création de comptes AD depuis un CSV (`Import-Csv` + boucle + `New-ADUser`)
- **Simuler avec `-WhatIf`** avant toute opération de masse (la discipline poussée à son maximum)
- Isoler les erreurs par ligne (`try/catch`) pour ne pas casser tout le lot
- Produire un rapport de succès/échecs
- Assembler tout le cours dans un livrable professionnel

## 💬 Questions d'entretien typiques

- **Comment créer 100 comptes AD depuis un fichier ?** → `Import-Csv`, une boucle `foreach`, `New-ADUser` par ligne, avec validation, `try/catch` et rapport.
- **Pourquoi `-WhatIf` est-il crucial en masse ?** → Il simule l'opération sans l'exécuter : on vérifie ce qui *serait* fait avant de le faire réellement.
- **Comment éviter qu'une ligne en erreur arrête tout ?** → Encadrer chaque itération d'un `try/catch` pour isoler l'échec et poursuivre le lot.

---
