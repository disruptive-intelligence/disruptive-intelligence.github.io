---
title: "Comptes et groupes"
---

# Comptes et groupes

Tout savoir sur un compte, le déverrouiller, réinitialiser son mot de passe, le désactiver, le créer ; gérer les membres des groupes.

Les incontournables : `Get-ADUser` · `Search-ADAccount` · `Unlock-ADAccount` · `Get-ADGroupMember` · `Add-ADGroupMember`
{ .kw-cs-top }

## Comptes

### Tout savoir sur un compte

```powershell title="Commande"
Get-ADUser <identifiant> -Properties *
```

```powershell title="Exemple"
Get-ADUser m.laurent -Properties Enabled, LockedOut, LastLogonDate, PasswordLastSet, PasswordNeverExpires, MemberOf |
    Select-Object SamAccountName, Enabled, LockedOut, LastLogonDate, PasswordLastSet, PasswordNeverExpires, @{n='Groupes';e={($_.MemberOf | ForEach-Object { ($_ -split ',')[0] -replace 'CN=' }) -join ', '}}
```

??? example "Sortie"
    ```text
    SamAccountName       : m.laurent
    Enabled              : True
    LockedOut            : False
    LastLogonDate        : 02/10/2026 08:03:41
    PasswordLastSet      : 15/07/2026 09:12:05
    PasswordNeverExpires : False
    Groupes              : GG-Qualite, GG-Lyon, VPN-Users
    ```

```bat title="Exemple 2"
net user m.laurent /domain
```

Pour comprendre : [Active Directory, ch. 3 (objets et attributs)](../../../../library/it/active-directory/active-directory/01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
{ .kw-cs-meta }

### Trouver les comptes verrouillés et les déverrouiller

```powershell title="Commande"
Search-ADAccount -LockedOut | Select-Object SamAccountName, LastLogonDate
Unlock-ADAccount -Identity <compte>
```

```powershell title="Exemple"
Search-ADAccount -LockedOut | Select-Object SamAccountName, LastLogonDate
```

??? example "Sortie"
    ```text
    SamAccountName LastLogonDate
    -------------- -------------
    j.petit        01/10/2026 17:52:10
    ```

D'où vient le verrouillage ? Sur le DC qui détient le rôle PDC Emulator, l'événement **4740** indique la machine à l'origine (*Caller Computer Name*).

### Réinitialiser un mot de passe

```powershell title="Commande"
Set-ADAccountPassword -Identity <compte> -Reset -NewPassword (Read-Host -AsSecureString "Nouveau mot de passe")
Set-ADUser -Identity <compte> -ChangePasswordAtLogon $true
```

```powershell title="Exemple"
Set-ADAccountPassword -Identity j.petit -Reset -NewPassword (Read-Host -AsSecureString "Nouveau mot de passe")
Set-ADUser -Identity j.petit -ChangePasswordAtLogon $true
```

### Désactiver un compte

```powershell title="Commande"
Disable-ADAccount -Identity <compte>
```

```powershell title="Exemple"
Disable-ADAccount -Identity j.petit
Get-ADUser j.petit | Select-Object SamAccountName, Enabled
```

### Créer un compte

```powershell title="Commande"
New-ADUser -Name "<Prénom Nom>" -SamAccountName <identifiant> -UserPrincipalName <identifiant>@<domaine> `
    -Path "<DN de l'OU>" -AccountPassword (Read-Host -AsSecureString "Mot de passe initial") `
    -Enabled $true -ChangePasswordAtLogon $true
```

```powershell title="Exemple"
New-ADUser -Name "Sarah Benali" -GivenName Sarah -Surname Benali -SamAccountName s.benali `
    -UserPrincipalName s.benali@meridian.local -Path "OU=Utilisateurs,OU=Lyon,DC=meridian,DC=local" `
    -AccountPassword (Read-Host -AsSecureString "Mot de passe initial") -Enabled $true -ChangePasswordAtLogon $true
```

Le mot de passe est saisi au clavier, jamais écrit dans la commande. Sans `-Path`, le compte arrive dans le conteneur `Users`, où aucune GPO d'OU ne s'applique.

## Groupes

### Voir les membres d'un groupe, imbrications comprises

```powershell title="Commande"
Get-ADGroupMember -Identity "<groupe>" -Recursive | Select-Object SamAccountName, objectClass
```

```powershell title="Exemple"
Get-ADGroupMember -Identity "Domain Admins" -Recursive | Select-Object SamAccountName, objectClass
```

??? example "Sortie"
    ```text
    SamAccountName objectClass
    -------------- -----------
    Administrator  user
    adm.martin.t0  user
    ```

Le nombre de membres des groupes privilégiés doit être minimal ; un compte de service dans Domain Admins est une anomalie.

### Voir les groupes d'un compte

```powershell title="Commande"
Get-ADPrincipalGroupMembership -Identity <compte> | Select-Object Name
```

```bat title="Exemple"
whoami /groups   :: pour le compte connecté, y compris les groupes imbriqués
```

### Ajouter ou retirer un membre

```powershell title="Commande"
Add-ADGroupMember -Identity "<groupe>" -Members <compte>
Remove-ADGroupMember -Identity "<groupe>" -Members <compte> -Confirm:$false
```

```powershell title="Exemple"
Add-ADGroupMember -Identity "GG-Compta" -Members j.petit
```

L'utilisateur doit rouvrir sa session (nouveau jeton) pour que le changement s'applique.

## Vue d'ensemble

| Besoin | Cmdlet | Propriétés utiles |
|---|---|---|
| Tout savoir sur un compte | `Get-ADUser <compte> -Properties *` | `Enabled`, `LockedOut`, `LastLogonDate`, `PasswordLastSet`, `MemberOf` |
| Comptes verrouillés | `Search-ADAccount -LockedOut` · `Unlock-ADAccount` | `LockedOut` |
| Réinitialiser un mot de passe | `Set-ADAccountPassword -Reset` | Puis `-ChangePasswordAtLogon $true` |
| Désactiver | `Disable-ADAccount` | `Enabled` |
| Créer | `New-ADUser` | `-Path` (OU), `-Enabled`, `-ChangePasswordAtLogon` |
| Membres d'un groupe | `Get-ADGroupMember -Recursive` | Imbrications comprises |
| Groupes d'un compte | `Get-ADPrincipalGroupMembership` | `Name` |
| Ajouter, retirer un membre | `Add-ADGroupMember` · `Remove-ADGroupMember` | — |
