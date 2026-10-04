---
title: "Active Directory au quotidien"
cours:
  - library/it/active-directory/active-directory/index.md
  - library/it/windows/powershell/index.md
---

# Active Directory au quotidien

Trouver un compte et son état, déverrouiller, réinitialiser, gérer les groupes ; diagnostiquer les GPO, Kerberos et les contrôleurs de domaine ; contrôles d'hygiène.

Les incontournables : `Get-ADUser` · `Search-ADAccount` · `Get-ADGroupMember` · `gpresult` · `klist` · `nltest` · `dcdiag`
{ .kw-cs-top }

Les cmdlets `*-AD*` demandent le module ActiveDirectory (RSAT sur un poste d'administration, présent sur les DC).

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

Pour comprendre : [Active Directory, ch. 3 (objets et attributs)](../../../library/it/active-directory/active-directory/01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
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

Ensuite : [forcer l'application des GPO](#forcer-lapplication-des-gpo) — Pour comprendre : [Active Directory, ch. 9 (GPO)](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/01-chapitre-9-group-policy-gpo-configuration-et-secur.md)
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

## Kerberos et contrôleurs de domaine

### Voir et purger ses tickets Kerberos

```bat title="Commande"
klist         :: tickets de la session
klist purge   :: vider le cache (nouvelle demande au prochain accès)
```

```bat title="Exemple"
klist
```

??? example "Sortie"
    ```text
    Tickets mis en cache : (2)
    #0>  Client : alice @ MERIDIAN.LOCAL
         Serveur : krbtgt/MERIDIAN.LOCAL @ MERIDIAN.LOCAL
         Type de chiffrement KerbTicket : AES-256-CTS-HMAC-SHA1-96
         Heure de fin : 02/10/2026 18:01:12
    #1>  Client : alice @ MERIDIAN.LOCAL
         Serveur : cifs/srv-fs01.meridian.local @ MERIDIAN.LOCAL
         Type de chiffrement KerbTicket : AES-256-CTS-HMAC-SHA1-96
    ```

Pour comprendre : [Active Directory, ch. 6 (Kerberos)](../../../library/it/active-directory/active-directory/02-partie-ii-authentification/03-chapitre-6-kerberos-le-flux-complet-et-les-subtili.md)
{ .kw-cs-meta }

### Diagnostiquer un échec Kerberos

```bat title="Commande"
nltest /dsgetdc:<domaine>     :: un DC est-il joignable ?
w32tm /query /status          :: écart d'horloge (5 minutes au plus)
setspn -L <compte>            :: SPN d'un compte de service
setspn -X                     :: SPN dupliqués
```

```bat title="Exemple"
setspn -L svc_sql
```

??? example "Sortie"
    ```text
    Registered ServicePrincipalNames for CN=svc_sql,OU=Services,DC=meridian,DC=local:
            MSSQLSvc/sql01.meridian.local:1433
            MSSQLSvc/sql01.meridian.local
    ```

### Vérifier la santé des contrôleurs de domaine

```bat title="Commande"
dcdiag /q                          :: n'affiche que les erreurs
repadmin /replsummary              :: état de la réplication
netdom query fsmo                  :: titulaires des rôles FSMO
```

```bat title="Exemple"
repadmin /replsummary
```

??? example "Sortie"
    ```text
    Source DSA          largest delta    fails/total %   error
     DC01-LYO               04m:12s    0 /  10    0
     DC02-LYO               03m:58s    0 /  10    0
    ```

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

### Vérifier l'âge du mot de passe de krbtgt

```powershell title="Commande"
Get-ADUser krbtgt -Properties PasswordLastSet | Select-Object PasswordLastSet
```

Un `krbtgt` jamais renouvelé depuis la création du domaine est une recommandation prioritaire (double rotation, Ch.28 du cours).

Pour comprendre : [Active Directory, ch. 10 (requêtes d'hygiène)](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/02-chapitre-10-outils-d-administration-et-requetage.md)
{ .kw-cs-meta }
