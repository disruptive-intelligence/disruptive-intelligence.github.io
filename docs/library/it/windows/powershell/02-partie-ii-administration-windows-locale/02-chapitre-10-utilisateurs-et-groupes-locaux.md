---
title: Chapitre 10 — Utilisateurs et groupes locaux
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration Windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### Comptes locaux vs comptes de domaine

Une machine Windows a des **comptes locaux** (définis sur la machine elle-même). Dans un domaine, il existe aussi des **comptes AD** (centralisés, vus en Partie IV). Ce chapitre traite les **comptes locaux** — gérés par le module `Microsoft.PowerShell.LocalAccounts`.

> **Note :** ces cmdlets `*-LocalUser` / `*-LocalGroup` fonctionnent sur Windows 10/11 et Windows Server. Elles agissent sur la base SAM locale, pas sur l'annuaire du domaine.

### Lister les utilisateurs et groupes locaux

```powershell
Get-LocalUser                        # tous les comptes locaux
Get-LocalUser -Name Administrateur   # un compte précis
Get-LocalGroup                       # tous les groupes locaux
Get-LocalGroupMember -Group "Administrateurs"   # membres du groupe Administrateurs
```


> **📌 Réflexe `Get-Member` :** `Get-LocalUser | Get-Member` révèle `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, `SID`… Autant de propriétés pour auditer les comptes.

### Le cas d'usage n°1 : auditer les administrateurs locaux

Qui est administrateur local d'une machine ? C'est une **question de sécurité fondamentale** — trop d'admins locaux = surface d'attaque.

```powershell
Get-LocalGroupMember -Group "Administrateurs" |
    Select-Object Name, PrincipalSource, ObjectClass
```


`PrincipalSource` indique si le membre est local ou vient du domaine ; `ObjectClass` s'il s'agit d'un utilisateur ou d'un groupe.

> **Note langue :** le groupe s'appelle `Administrateurs` sur un Windows en français, `Administrators` en anglais. Pour un script portable, on peut cibler par SID : le groupe Administrateurs a toujours le SID `S-1-5-32-544`. `Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"`.

### Créer, modifier, désactiver un compte local `[🔑 Admin]`

**Discipline `Get`/`Test` avant d'agir** : on vérifie qu'un compte n'existe pas avant de le créer.

```powershell
# 1. Vérifier
if (-not (Get-LocalUser -Name "svc_backup" -ErrorAction SilentlyContinue)) {

    # 2. Créer un compte technique (mot de passe en SecureString — voir Ch.33)
    $pwd = Read-Host "Mot de passe" -AsSecureString
    New-LocalUser -Name "svc_backup" -Password $pwd `
        -FullName "Compte de sauvegarde" -Description "Service backup" `
        -PasswordNeverExpires
}

# Modifier
Set-LocalUser -Name "svc_backup" -Description "Compte technique sauvegarde"

# Désactiver / réactiver (préférable à la suppression pour garder une trace)
Disable-LocalUser -Name "svc_backup"
Enable-LocalUser  -Name "svc_backup"
```


> **Bonne pratique :** on **désactive** plutôt qu'on supprime un compte quand on n'en est pas sûr — la suppression est définitive et fait perdre le SID (donc l'historique des permissions). C'est la même logique que le « soft delete » en base de données.

### Gérer l'appartenance aux groupes `[🔑 Admin]`

```powershell
Add-LocalGroupMember    -Group "Administrateurs" -Member "svc_backup"
Remove-LocalGroupMember -Group "Administrateurs" -Member "svc_backup"
```


## 🟡 Très utile en pratique

### Auditer tous les comptes actifs

```powershell
Get-LocalUser | Where-Object Enabled |
    Select-Object Name, LastLogon, PasswordExpires |
    Sort-Object LastLogon
```


Repérer un compte activé jamais connecté, ou un mot de passe qui n'expire jamais, est un réflexe d'hygiène de sécurité.

### Produire un rapport de tous les groupes et leurs membres

```powershell
Get-LocalGroup | ForEach-Object {
    $grp = $_.Name
    Get-LocalGroupMember -Group $grp -ErrorAction SilentlyContinue | ForEach-Object {
        [PSCustomObject]@{
            Groupe = $grp
            Membre = $_.Name
            Type   = $_.ObjectClass
            Source = $_.PrincipalSource
        }
    }
} | Export-Csv C:\audit_groupes.csv -NoTypeInformation -Encoding UTF8
```


Ce pattern (boucler sur des groupes, produire des objets, exporter) est directement transposable à l'audit AD (Ch.21).

## 🔴 Bonus

### Le compte administrateur intégré

Le compte `Administrateur` (SID se terminant par `-500`) est souvent désactivé par défaut sur les postes modernes. On peut le repérer :

```powershell
Get-LocalUser | Where-Object { $_.SID -like "*-500" }
```


Un compte `-500` **activé** et renommé est un point d'attention en sécurité.

## ❌ Erreur classique

```powershell
# Cibler "Administrators" en dur sur un Windows en français
Get-LocalGroupMember -Group "Administrators"    # ❌ échoue en FR
Get-LocalGroupMember -Group "Administrateurs"   # ✅ (ou cibler par SID S-1-5-32-544)

# Supprimer un compte au lieu de le désactiver
Remove-LocalUser -Name "ancien"    # ⚠️ définitif, perte du SID
Disable-LocalUser -Name "ancien"   # ✅ réversible, garde la trace

# Créer un compte sans vérifier son existence
New-LocalUser -Name "svc"          # ❌ erreur si déjà présent
if (-not (Get-LocalUser svc -ErrorAction SilentlyContinue)) { New-LocalUser ... }   # ✅
```


## 💡 Exercices

**Guidé :** Affiche les membres du groupe Administrateurs locaux avec leur type et leur source. Cible le groupe par son SID pour être portable.

**Autonome :** Écris un script qui liste tous les comptes locaux activés dont le mot de passe n'expire jamais (`PasswordExpires -eq $null`) — un point d'audit de sécurité classique.

## 🧩 Mini-projet — Audit des comptes locaux

Crée `Get-LocalAccountAudit.ps1` qui produit un rapport CSV : tous les comptes locaux avec `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, et une colonne `EstAdmin` (True si le compte est membre du groupe Administrateurs). Réutilise `Get-LocalUser`, `Get-LocalGroupMember`, PSCustomObject et `Export-Csv`.

## ✅ Tu sais maintenant...

- La différence comptes locaux / comptes de domaine
- Lister, créer, modifier, désactiver des comptes locaux (`*-LocalUser`)
- Gérer les groupes locaux et leurs membres (`*-LocalGroup*`)
- Auditer les administrateurs locaux (par nom ou par SID, pour la portabilité)
- Préférer **désactiver** à **supprimer**

## 💬 Questions d'entretien typiques

- **Pourquoi désactiver plutôt que supprimer un compte ?** → Réversible, conserve le SID et l'historique des permissions.
- **Comment auditer les admins locaux de façon portable (FR/EN) ?** → Cibler le groupe par SID `S-1-5-32-544` plutôt que par son nom.
- **Différence compte local / compte de domaine ?** → Le compte local vit dans la base SAM de la machine ; le compte de domaine est centralisé dans Active Directory.

---
