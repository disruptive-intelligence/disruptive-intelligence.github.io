---
title: "Kerberos, DC et comptes de service"
---

# Kerberos, DC et comptes de service

Créer un gMSA ; voir et purger ses tickets Kerberos, diagnostiquer un échec ; trouver les contrôleurs de domaine, leurs rôles et leur santé.

Les incontournables : `New-ADServiceAccount` · `klist` · `nltest` · `netdom query fsmo` · `dcdiag`
{ .kw-cs-top }

## Comptes de service

### Créer un compte de service géré (gMSA)

```powershell title="Commande"
Add-KdsRootKey -EffectiveImmediately        # une seule fois par forêt ; utilisable après réplication (jusqu'à 10 h)
New-ADServiceAccount -Name <gmsa> -DNSHostName <gmsa>.<domaine> -PrincipalsAllowedToRetrieveManagedPassword "<groupe de serveurs>"
Install-ADServiceAccount -Identity <gmsa>   # sur chaque serveur du groupe
Test-ADServiceAccount -Identity <gmsa>      # True : le serveur sait récupérer le mot de passe
```

```powershell title="Exemple"
New-ADServiceAccount -Name gmsa-sql -DNSHostName gmsa-sql.meridian.local -PrincipalsAllowedToRetrieveManagedPassword "GS-Serveurs-SQL"
Test-ADServiceAccount -Identity gmsa-sql    # sur SQL01, après Install-ADServiceAccount
```

??? example "Sortie"
    ```text
    True
    ```

Dans le service, le compte s'écrit `MERIDIAN\gmsa-sql$`, mot de passe laissé vide : AD le génère (240 octets) et le renouvelle tous les 30 jours. Le serveur doit être membre du groupe autorisé (redémarrage après l'ajout).

Pour comprendre : [Active Directory, ch. 3 (gMSA)](../../../../library/it/active-directory/active-directory/01-partie-i-fondations/03-chapitre-3-objets-attributs-et-structure-ldap.md)
{ .kw-cs-meta }

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

Pour comprendre : [Active Directory, ch. 6 (Kerberos)](../../../../library/it/active-directory/active-directory/02-partie-ii-authentification/03-chapitre-6-kerberos-le-flux-complet-et-les-subtili.md)
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

### Trouver les contrôleurs de domaine et leurs rôles

```powershell title="Commande"
Get-ADDomainController -Filter * | Select-Object Name, Site, IPv4Address, IsGlobalCatalog, OperationMasterRoles
```

```powershell title="Exemple"
Get-ADDomainController -Filter * | Select-Object Name, Site, IsGlobalCatalog, OperationMasterRoles
```

??? example "Sortie"
    ```text
    Name     Site IsGlobalCatalog OperationMasterRoles
    ----     ---- --------------- --------------------
    DC01-LYO Lyon            True {SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster, InfrastructureMaster}
    DC02-LYO Lyon            True {}
    ```

```bat title="Exemple 2"
nltest /dclist:meridian.local
```

Les postes, eux, trouvent les DC dans le DNS (enregistrements SRV) : voir [résoudre un nom](../../fondamentaux/reseau.md#resoudre-un-nom).

Pour comprendre : [Active Directory, ch. 2 (FSMO, Global Catalog)](../../../../library/it/active-directory/active-directory/01-partie-i-fondations/02-chapitre-2-architecture-et-composants.md)
{ .kw-cs-meta }

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

## Vue d'ensemble

| Rôle FSMO | Portée | Rôle |
|---|---|---|
| Schema Master | Forêt | Seul à pouvoir modifier le schéma |
| Domain Naming Master | Forêt | Ajout et suppression de domaines |
| RID Master | Domaine | Distribue les blocs de RID qui composent les SID |
| PDC Emulator | Domaine | Heure de référence, changements de mot de passe, verrouillages |
| Infrastructure Master | Domaine | Références vers les objets d'autres domaines |

| Échec Kerberos | Vérification |
|---|---|
| Aucun DC joignable | `nltest /dsgetdc:<domaine>` |
| Horloge décalée (plus de 5 minutes) | `w32tm /query /status` |
| SPN absent ou dupliqué | `setspn -L <compte>` · `setspn -X` |
| Ticket périmé ou faux | `klist` · `klist purge` |
| Santé et réplication des DC | `dcdiag /q` · `repadmin /replsummary` |
