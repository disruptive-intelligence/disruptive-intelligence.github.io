---
title: Chapitre 20 — Utilisateurs AD
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### Chercher un utilisateur : `Get-ADUser`

```powershell
# Par identité (SamAccountName, DN, SID, GUID)
Get-ADUser -Identity alice.martin

# Avec des attributs supplémentaires (rappel Ch.19 : sinon jeu réduit)
Get-ADUser -Identity alice.martin -Properties mail, Department, LastLogonDate

# Tous les utilisateurs (filtre obligatoire — voir Ch.23)
Get-ADUser -Filter *
```


Les attributs par défaut : `Name`, `SamAccountName`, `DistinguishedName`, `Enabled`, `UserPrincipalName`, `SID`, `GivenName`, `Surname`. Tout le reste (`mail`, `Department`, `Title`, `LastLogonDate`, `Manager`…) nécessite `-Properties`.

> **📌 Réflexe `Get-Member` :** `Get-ADUser alice.martin -Properties * | Get-Member` liste **tous** les attributs disponibles pour un utilisateur. Fais-le une fois pour découvrir ce que tu peux exploiter (souvent 100+ attributs).

### Créer un utilisateur : `New-ADUser` `[🔑 Admin]`

**Discipline `Get` avant `New`** : on vérifie que le compte n'existe pas.

```powershell
if (-not (Get-ADUser -Filter "SamAccountName -eq 'jdupont'" -ErrorAction SilentlyContinue)) {

    $motDePasse = Read-Host "Mot de passe initial" -AsSecureString

    New-ADUser `
        -Name "Jean Dupont" `
        -GivenName "Jean" -Surname "Dupont" `
        -SamAccountName "jdupont" `
        -UserPrincipalName "jdupont@lab.local" `
        -Path "OU=IT,DC=lab,DC=local" `
        -AccountPassword $motDePasse `
        -Enabled $true `
        -ChangePasswordAtLogon $true
}
```


Points clés :

- `-SamAccountName` : l'identifiant de connexion (format court, `jdupont`)
- `-UserPrincipalName` : l'identifiant moderne (format email, `jdupont@lab.local`)
- `-Path` : le DN de l'OU où créer le compte
- `-AccountPassword` : un **SecureString** (jamais en clair — voir Ch.33)
- `-Enabled $true` : sinon le compte est créé désactivé
- `-ChangePasswordAtLogon $true` : bonne pratique pour un mot de passe initial

### Modifier un utilisateur : `Set-ADUser` `[🔑 Admin]`

```powershell
Set-ADUser -Identity jdupont -EmailAddress "jean.dupont@lab.local" -Department "Informatique"
Set-ADUser -Identity jdupont -Title "Technicien" -Office "Bâtiment A"
```


### Activer, désactiver, déverrouiller `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity jdupont      # désactiver (départ, suspension)
Enable-ADAccount  -Identity jdupont      # réactiver
Unlock-ADAccount  -Identity jdupont      # déverrouiller (après trop d'essais de mot de passe)
```


> **Verrouillé ≠ désactivé :** un compte **verrouillé** l'a été automatiquement (trop de mauvais mots de passe) — on le **déverrouille**. Un compte **désactivé** l'a été manuellement (départ…) — on le **réactive**. Deux situations différentes.

### Réinitialiser un mot de passe `[🔑 Admin]`

```powershell
$nouveau = Read-Host "Nouveau mot de passe" -AsSecureString
Set-ADAccountPassword -Identity jdupont -NewPassword $nouveau -Reset
Set-ADUser -Identity jdupont -ChangePasswordAtLogon $true    # forcer le changement
```


### Supprimer un utilisateur `[🔑 Admin]`

```powershell
Remove-ADUser -Identity jdupont -Confirm:$false
```


> **Bonne pratique (rappel Ch.10) :** on préfère souvent **désactiver et déplacer** un compte (départ d'un employé) plutôt que le supprimer d'emblée — pour conserver l'historique et pouvoir restaurer. La suppression vient après une période de rétention.

## 🟡 Très utile en pratique

### Identifier les comptes à problème

```powershell
# Comptes désactivés
Get-ADUser -Filter "Enabled -eq '$false'" | Select-Object Name, SamAccountName

# Comptes verrouillés
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName

# Comptes dont le mot de passe n'expire jamais (point d'audit)
Get-ADUser -Filter "PasswordNeverExpires -eq '$true'" -Properties PasswordNeverExpires |
    Select-Object Name, SamAccountName
```


`Search-ADAccount` est un raccourci pratique pour les cas courants (`-LockedOut`, `-AccountDisabled`, `-AccountInactive`, `-PasswordExpired`).

### La discipline Get → Set en action

```powershell
# 1. Regarder l'état actuel
Get-ADUser jdupont -Properties Department, Title | Select Department, Title

# 2. Modifier en connaissance de cause
Set-ADUser jdupont -Department "Support" -Title "Technicien N2"

# 3. Vérifier
Get-ADUser jdupont -Properties Department, Title | Select Department, Title
```


Ce triptyque lire → modifier → vérifier est la marque d'un administrateur rigoureux.

## 🔴 Bonus

### Comptes inactifs depuis X jours

```powershell
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly |
    Select-Object Name, SamAccountName, LastLogonDate
```


> **⚠️ Nuance importante sur `LastLogonDate` :** cet attribut dérive de `lastLogonTimestamp`, qui n'est répliqué entre contrôleurs de domaine que périodiquement (par défaut avec une marge d'environ 9-14 jours). Il est donc **approximatif** : parfait pour repérer des comptes « globalement inactifs depuis des mois », mais **pas** pour savoir la dernière connexion exacte à la minute. Pour une précision fine, il faudrait interroger l'attribut `lastLogon` (non répliqué) sur **chaque** DC — beaucoup plus lourd. Pour l'audit courant, `LastLogonDate` suffit, en gardant sa marge d'erreur en tête.

## ❌ Erreur classique

```powershell
# Créer un compte sans -Enabled → compte inutilisable (désactivé)
New-ADUser -Name "X" -SamAccountName x -AccountPassword $p   # ⚠️ créé désactivé
New-ADUser ... -Enabled $true                                 # ✅

# Passer le mot de passe en clair
-AccountPassword "P@ssw0rd"          # ❌ refusé (attend un SecureString)
-AccountPassword (Read-Host -AsSecureString)   # ✅

# Confondre verrouillé et désactivé
Enable-ADAccount jdupont    # ❌ ne déverrouille pas un compte verrouillé
Unlock-ADAccount jdupont    # ✅ pour un compte verrouillé

# Se fier à LastLogonDate à la minute près
# → attribut approximatif (réplication différée)
```


## 💡 Exercices

**Guidé :** Affiche le nom, l'email et le service (`Department`) de `alice.martin` (pense à `-Properties`). Puis modifie son `Title` et vérifie le changement.

**Autonome :** Écris une fonction `New-LabUser` qui prend `-GivenName`, `-Surname` et `-OU`, construit le `SamAccountName` (première lettre du prénom + nom, en minuscules, via les méthodes de chaîne du Ch.5), vérifie l'absence du compte, puis le crée activé avec changement de mot de passe à la première connexion.

## ✅ Tu sais maintenant...

- Chercher (`Get-ADUser`, avec `-Properties`), créer (`New-ADUser`), modifier (`Set-ADUser`)
- Activer/désactiver (`Enable`/`Disable-ADAccount`), déverrouiller (`Unlock-ADAccount`)
- Réinitialiser un mot de passe (`Set-ADAccountPassword -Reset`)
- Repérer les comptes à problème (`Search-ADAccount`)
- La nuance sur `LastLogonDate` (approximatif, réplication différée)

## 💬 Questions d'entretien typiques

- **Différence entre un compte verrouillé et désactivé ?** → Verrouillé = automatique (trop de mauvais mots de passe), on déverrouille ; désactivé = manuel, on réactive.
- **Pourquoi un `New-ADUser` donne-t-il un compte inutilisable ?** → Souvent l'oubli de `-Enabled $true` (créé désactivé par défaut).
- **Peut-on se fier à `LastLogonDate` à la minute ?** → Non : dérivé de `lastLogonTimestamp`, répliqué avec une marge de plusieurs jours ; bon pour l'inactivité globale, pas pour l'exactitude.
- **Comment passer un mot de passe à `New-ADUser` ?** → Via un `SecureString` (`-AsSecureString`), jamais en clair.

---
