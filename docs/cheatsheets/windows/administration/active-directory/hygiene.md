---
title: "Contrôles d'hygiène"
---

# Contrôles d'hygiène

Comptes inactifs, mots de passe qui n'expirent jamais, comptes privilégiés, comptes porteurs d'un SPN, âge du mot de passe de krbtgt.

Les incontournables : `Search-ADAccount -AccountInactive` · `Get-ADUser -Filter` · `Get-ADGroupMember -Recursive`
{ .kw-cs-top }

## Contrôles d'hygiène

### Trouver les comptes inactifs

```powershell title="Commande"
Search-ADAccount -AccountInactive -TimeSpan <jours>.00:00:00 -UsersOnly | Where-Object Enabled
```

```powershell title="Exemple"
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly | Where-Object Enabled | Measure-Object | Select-Object Count
```

### Trouver les mots de passe qui n'expirent jamais

```powershell title="Commande"
Get-ADUser -Filter 'PasswordNeverExpires -eq $true -and Enabled -eq $true' -Properties PasswordLastSet | Select-Object SamAccountName, PasswordLastSet
```

### Lister les comptes privilégiés (actuels et anciens)

```powershell title="Commande"
Get-ADUser -Filter 'adminCount -eq 1' -Properties adminCount, LastLogonDate | Select-Object SamAccountName, Enabled, LastLogonDate
```

`adminCount = 1` reste sur les anciens membres des groupes protégés : les comptes qui ne sont plus privilégiés doivent être nettoyés (Ch.4 du cours).

### Inventorier les comptes utilisateurs qui portent un SPN

```powershell title="Commande"
Get-ADUser -Filter 'servicePrincipalName -like "*"' -Properties servicePrincipalName, PasswordLastSet, adminCount |
    Where-Object SamAccountName -ne 'krbtgt' |
    Select-Object SamAccountName, PasswordLastSet, adminCount, @{n='SPN';e={$_.servicePrincipalName -join ', '}}
```

Chaque compte de la liste doit avoir un mot de passe long et renouvelé, aucun privilège superflu (`adminCount` à 1 = à revoir en priorité), ou devenir un gMSA. Un SPN qui ne sert plus se retire avec `setspn -D <SPN> <compte>`.

Ensuite : [créer un gMSA](kerberos-dc.md#creer-un-compte-de-service-gere-gmsa) — Pour comprendre : [Active Directory, ch. 3 (attributs critiques)](../../../../library/it/active-directory/active-directory/01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
{ .kw-cs-meta }

### Vérifier l'âge du mot de passe de krbtgt

```powershell title="Commande"
Get-ADUser krbtgt -Properties PasswordLastSet | Select-Object PasswordLastSet
```

Un `krbtgt` jamais renouvelé depuis la création du domaine est une recommandation prioritaire (double rotation, Ch.28 du cours).

Pour comprendre : [Active Directory, ch. 10 (requêtes d'hygiène)](../../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/02-chapitre-10-outils-d-administration-et-requetage.md)
{ .kw-cs-meta }
