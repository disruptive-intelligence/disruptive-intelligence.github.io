---
title: "Utilisateurs et groupes"
cours:
  - library/it/windows/powershell/index.md
---

# Utilisateurs et groupes

Créer, modifier, désactiver ou supprimer des comptes et des groupes locaux ; réinitialiser un mot de passe ; ajouter à un groupe.

Les incontournables : `Get-LocalUser` · `New-LocalUser` · `Disable-LocalUser` · `Add-LocalGroupMember` · `net user`
{ .kw-cs-top }

Toutes ces commandes demandent une console administrateur. Pour les comptes du domaine, voir la fiche [Active Directory](active-directory/index.md).

## Comptes

### Lister les comptes locaux

```powershell title="Commande"
Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordLastSet
```

```powershell title="Exemple"
Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordLastSet
```

??? example "Sortie"
    ```text
    Name               Enabled LastLogon           PasswordLastSet
    ----               ------- ---------           ---------------
    Administrateur       False                     12/03/2026 10:02:11
    alice-local           True 30/09/2026 17:44:02 02/09/2026 08:10:47
    DefaultAccount       False
    Invité               False
    WDAGUtilityAccount   False                     12/03/2026 10:05:33
    ```

```bat title="Exemple 2"
net user
net user alice-local   :: détail d'un compte : groupes, dernière connexion, expiration
```

### Créer un compte local

```powershell title="Commande"
New-LocalUser -Name <nom> -Password (Read-Host -AsSecureString "Mot de passe") -FullName "<nom complet>"
```

```powershell title="Exemple"
New-LocalUser -Name tech-maint -Password (Read-Host -AsSecureString "Mot de passe") -FullName "Compte de maintenance" -PasswordNeverExpires:$false
```

??? example "Sortie"
    ```text
    Name       Enabled Description
    ----       ------- -----------
    tech-maint True
    ```

### Réinitialiser un mot de passe

```powershell title="Commande"
Set-LocalUser -Name <nom> -Password (Read-Host -AsSecureString "Nouveau mot de passe")
```

```powershell title="Exemple"
Set-LocalUser -Name tech-maint -Password (Read-Host -AsSecureString "Nouveau mot de passe")
```

```bat title="Exemple 2"
net user tech-maint *   :: demande le mot de passe sans l'afficher
```

!!! warning "Attention"
    Ne jamais écrire un mot de passe en clair dans une commande : il reste dans l'historique PowerShell et dans les journaux (4104).

### Désactiver, réactiver ou supprimer un compte

```powershell title="Commande"
Disable-LocalUser -Name <nom>
Enable-LocalUser -Name <nom>
Remove-LocalUser -Name <nom>
```

```powershell title="Exemple"
Disable-LocalUser -Name tech-maint
```

```bat title="Exemple 2"
net user tech-maint /active:no
```

En réponse à incident : **désactiver** plutôt que supprimer, pour garder le compte (et son SID) le temps de l'enquête.

## Groupes

### Ajouter ou retirer un membre d'un groupe local

```powershell title="Commande"
Add-LocalGroupMember -Group <groupe> -Member <compte>
Remove-LocalGroupMember -Group <groupe> -Member <compte>
```

```powershell title="Exemple"
Add-LocalGroupMember -SID S-1-5-32-555 -Member tech-maint   # Utilisateurs du Bureau à distance, quelle que soit la langue
```

```bat title="Exemple 2"
net localgroup "Utilisateurs du Bureau à distance" tech-maint /add
```

| SID | Groupe local |
|---|---|
| S-1-5-32-544 | Administrateurs |
| S-1-5-32-545 | Utilisateurs |
| S-1-5-32-551 | Opérateurs de sauvegarde |
| S-1-5-32-555 | Utilisateurs du Bureau à distance |
| S-1-5-32-580 | Utilisateurs de gestion à distance (WinRM) |

### Créer un groupe local

```powershell title="Commande"
New-LocalGroup -Name <groupe> -Description "<description>"
```

```powershell title="Exemple"
New-LocalGroup -Name LG-Lecture-Logs -Description "Lecture des journaux applicatifs"
```

Pour comprendre : [PowerShell, ch. 10 (utilisateurs et groupes locaux)](../../../library/it/windows/powershell/02-partie-ii-administration-windows-locale/02-chapitre-10-utilisateurs-et-groupes-locaux.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Action | Compte local (PowerShell) | Avec `net` | Compte de domaine |
|---|---|---|---|
| Lister | `Get-LocalUser` | `net user` | `Get-ADUser -Filter *` |
| Créer | `New-LocalUser` | `net user <nom> * /add` | `New-ADUser` |
| Réinitialiser le mot de passe | `Set-LocalUser -Password` | `net user <nom> *` | `Set-ADAccountPassword -Reset` |
| Désactiver / réactiver | `Disable-LocalUser` · `Enable-LocalUser` | `net user <nom> /active:no` | `Disable-ADAccount` · `Enable-ADAccount` |
| Supprimer | `Remove-LocalUser` | `net user <nom> /delete` | `Remove-ADUser` |
| Ajouter à un groupe | `Add-LocalGroupMember` | `net localgroup <groupe> <compte> /add` | `Add-ADGroupMember` |
| Retirer d'un groupe | `Remove-LocalGroupMember` | `net localgroup <groupe> <compte> /delete` | `Remove-ADGroupMember` |
| Créer un groupe | `New-LocalGroup` | `net localgroup <groupe> /add` | `New-ADGroup` |
