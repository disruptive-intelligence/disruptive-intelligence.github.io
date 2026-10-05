---
title: "OU, ordinateurs et GPO"
---

# OU, ordinateurs et GPO

Ranger les objets dans les OU, lister les ordinateurs, lire un mot de passe LAPS ; voir, forcer et lister les GPO.

Les incontournables : `Get-ADComputer` · `Move-ADObject` · `Get-LapsADPassword` · `gpresult` · `gpupdate`
{ .kw-cs-top }

## OU et ordinateurs

### Voir l'OU d'un objet et l'y déplacer

```powershell title="Commande"
Get-ADComputer <machine> | Select-Object DistinguishedName                  # l'OU se lit dans le DN
Move-ADObject -Identity "<DN de l'objet>" -TargetPath "<DN de l'OU>"
```

```powershell title="Exemple"
Get-ADComputer PC-COMPTA-07 | Select-Object DistinguishedName
Get-ADComputer PC-COMPTA-07 | Move-ADObject -TargetPath "OU=Postes,OU=Lyon,DC=meridian,DC=local"
```

??? example "Sortie"
    ```text
    DistinguishedName
    -----------------
    CN=PC-COMPTA-07,CN=Computers,DC=meridian,DC=local
    ```

```bat title="Exemple 2"
redircmp "OU=Postes,OU=Lyon,DC=meridian,DC=local"   :: les machines jointes ensuite arrivent dans cette OU
```

`CN=Computers` et `CN=Users` sont des conteneurs, pas des OU : on ne peut pas y lier de GPO.

Pour comprendre : [Active Directory, ch. 3 (objets et OU)](../../../../library/it/active-directory/active-directory/01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
{ .kw-cs-meta }

### Supprimer une OU protégée

```powershell title="Commande"
Get-ADObject -SearchBase "<DN de l'OU>" -Filter * | Select-Object Name, ObjectClass   # ce qu'elle contient
Set-ADOrganizationalUnit -Identity "<DN de l'OU>" -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity "<DN de l'OU>" -Recursive
```

```powershell title="Exemple"
Set-ADOrganizationalUnit -Identity "OU=Stagiaires,OU=Lyon,DC=meridian,DC=local" -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity "OU=Stagiaires,OU=Lyon,DC=meridian,DC=local" -Recursive -Confirm:$false
```

!!! warning "Attention"
    `-Recursive` supprime aussi tout ce que l'OU contient (comptes, machines, sous-OU). Sans la corbeille AD, la restauration passe par une sauvegarde.

### Lister les ordinateurs du domaine et leur système

```powershell title="Commande"
Get-ADComputer -Filter * -Properties OperatingSystem, LastLogonDate | Select-Object Name, OperatingSystem, LastLogonDate
```

```powershell title="Exemple"
Get-ADComputer -Filter 'OperatingSystem -like "*Server*"' -Properties OperatingSystem, LastLogonDate |
    Sort-Object Name | Select-Object Name, OperatingSystem, LastLogonDate
```

??? example "Sortie"
    ```text
    Name     OperatingSystem              LastLogonDate
    ----     ---------------              -------------
    DC01-LYO Windows Server 2022 Standard 03/10/2026 22:14:05
    DC02-LYO Windows Server 2022 Standard 03/10/2026 21:58:40
    SRV-FS01 Windows Server 2019 Standard 03/10/2026 19:02:11
    ```

```powershell title="Exemple 2"
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -ComputersOnly | Select-Object Name, LastLogonDate   # machines disparues
```

### Lire le mot de passe LAPS d'un poste

```powershell title="Commande"
Get-LapsADPassword -Identity <machine> -AsPlainText              # Windows LAPS
Set-LapsADPasswordExpirationTime -Identity <machine>             # le faire renouveler après usage
```

```powershell title="Exemple"
Get-LapsADPassword -Identity PC-COMPTA-07 -AsPlainText | Select-Object ComputerName, Account, Password, ExpirationTimestamp
```

??? example "Sortie"
    ```text
    ComputerName        : PC-COMPTA-07
    Account             : Administrator
    Password            : ••••••••••••••••
    ExpirationTimestamp : 02/11/2026 09:30:12
    ```

```powershell title="Exemple 2"
Get-ADComputer PC-COMPTA-07 -Properties ms-Mcs-AdmPwd | Select-Object Name, ms-Mcs-AdmPwd   # ancien LAPS
```

Seuls les groupes délégués peuvent lire ce mot de passe : la liste de ces groupes fait partie de l'audit des droits.

Pour comprendre : [Active Directory, ch. 11 (LAPS)](../../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md)
{ .kw-cs-meta }

## GPO

### Voir les GPO appliquées à un poste et à un utilisateur

```bat title="Commande"
gpresult /r                      :: résumé : GPO appliquées et refusées
gpresult /h <rapport.html> /f    :: rapport détaillé
```

```bat title="Exemple"
gpresult /r /scope computer
```

??? example "Sortie"
    ```text
    Objets Stratégie de groupe appliqués
    -------------------------------------
        Sécurité - Postes de travail
        Default Domain Policy
    Les GPO suivants n'ont pas été appliqués car ils ont été filtrés
    -------------------------------------
        Serveurs - Durcissement
            Filtrage :  Refusé (Sécurité)
    ```

Ensuite : [forcer l'application des GPO](#forcer-lapplication-des-gpo) — Pour comprendre : [Active Directory, ch. 9 (GPO)](../../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/01-chapitre-9-group-policy-gpo-configuration-et-secur.md)
{ .kw-cs-meta }

### Forcer l'application des GPO

```bat title="Commande"
gpupdate /force
```

```powershell title="Exemple"
Invoke-GPUpdate -Computer PC-COMPTA-07 -Force   # à distance (module GroupPolicy)
```

### Lister les GPO et leurs dates de modification

```powershell title="Commande"
Get-GPO -All | Sort-Object ModificationTime -Descending | Select-Object DisplayName, ModificationTime
```

```powershell title="Exemple"
Get-GPO -All | Sort-Object ModificationTime -Descending | Select-Object -First 3 DisplayName, ModificationTime
```

??? example "Sortie"
    ```text
    DisplayName                  ModificationTime
    -----------                  ----------------
    Sécurité - Postes de travail 01/10/2026 18:22:10
    Default Domain Policy        12/09/2026 10:05:44
    RDP policy                   02/06/2026 14:31:09
    ```

## Vue d'ensemble

| Besoin | Commande | À retenir |
|---|---|---|
| OU d'un objet, déplacement | `Get-ADComputer` / `Get-ADUser` · `Move-ADObject` | L'OU se lit dans le `DistinguishedName` |
| Supprimer une OU protégée | `Set-ADOrganizationalUnit -ProtectedFromAccidentalDeletion $false` · `Remove-ADOrganizationalUnit -Recursive` | Vérifier d'abord son contenu |
| Ordinateurs et leur système | `Get-ADComputer -Properties OperatingSystem, LastLogonDate` | Postes inactifs, systèmes obsolètes |
| Mot de passe LAPS | `Get-LapsADPassword -AsPlainText` · `Set-LapsADPasswordExpirationTime` | Le faire renouveler après usage |
| GPO appliquées | `gpresult /r` · `gpresult /h <rapport.html>` | Appliquées et refusées |
| Forcer l'application | `gpupdate /force` | — |
| GPO modifiées récemment | `Get-GPO -All | Sort-Object ModificationTime` | Changement inattendu = à vérifier |

Ordre d'application des GPO : **local → site → domaine → OU** (de la plus haute à la plus proche) ; en cas de conflit, la dernière appliquée l'emporte, sauf GPO « appliquée » (enforced) ou héritage bloqué.
