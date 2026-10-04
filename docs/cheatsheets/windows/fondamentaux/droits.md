---
title: "Droits et identités"
cours:
  - library/it/windows/windows-en-profondeur/index.md
  - library/it/windows/powershell/index.md
  - library/it/active-directory/active-directory/index.md
---

# Droits et identités

Savoir qui je suis (SID, groupes, privilèges, niveau d'intégrité), lire et modifier les permissions NTFS, repérer les permissions trop larges, savoir qui est administrateur.

Les incontournables : `whoami /all` · `icacls` · `Get-Acl` · `Get-LocalGroupMember` · `net localgroup`
{ .kw-cs-top }

## Identité

### Voir mon SID, mes groupes et mes privilèges

```bat title="Commande"
whoami /user     :: SID
whoami /groups   :: groupes et niveau d'intégrité
whoami /priv     :: privilèges du jeton
```

```bat title="Exemple"
whoami /priv
```

??? example "Sortie"
    ```text
    Nom de privilège              Description                                   État
    ============================= ============================================= =========
    SeShutdownPrivilege           Arrêter le système                            Désactivé
    SeChangeNotifyPrivilege       Contourner la vérification de parcours        Activé
    SeUndockPrivilege             Retirer l'ordinateur de la station d'accueil  Désactivé
    SeIncreaseWorkingSetPrivilege Augmenter une plage de travail de processus   Désactivé
    SeTimeZonePrivilege           Changer le fuseau horaire                     Désactivé
    ```

Un utilisateur standard n'a que ces privilèges. `SeDebugPrivilege`, `SeBackupPrivilege`, `SeImpersonatePrivilege` ou `SeTakeOwnershipPrivilege` signalent un compte puissant.

Pour comprendre : [Windows en profondeur, ch. 17 (jeton et notions centrales)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/01-chapitre-17-modele-de-securite-integrite-et-mitiga.md)
{ .kw-cs-meta }

### Savoir si la session est élevée (UAC)

```bat title="Commande"
whoami /groups | findstr /i "Mandatory"   :: niveau d'intégrité du jeton
```

```bat title="Exemple"
whoami /groups | findstr /i "Mandatory Label"
```

??? example "Sortie"
    ```text
    Étiquette obligatoire\Niveau obligatoire moyen   Étiquette   S-1-16-8192
    ```

| SID | Niveau | Signification |
|---|---|---|
| S-1-16-4096 | Faible | Processus bac à sable (navigateur) |
| S-1-16-8192 | Moyen | Session standard, ou administrateur non élevé |
| S-1-16-12288 | Élevé | « Exécuter en tant qu'administrateur » |
| S-1-16-16384 | Système | Services SYSTEM |

### Trouver le SID d'un compte, ou le compte d'un SID

```powershell title="Commande"
(New-Object System.Security.Principal.NTAccount('<DOMAINE\compte>')).Translate([System.Security.Principal.SecurityIdentifier]).Value
(New-Object System.Security.Principal.SecurityIdentifier('<SID>')).Translate([System.Security.Principal.NTAccount]).Value
```

```powershell title="Exemple"
(New-Object System.Security.Principal.SecurityIdentifier('S-1-5-32-544')).Translate([System.Security.Principal.NTAccount]).Value
```

??? example "Sortie"
    ```text
    BUILTIN\Administrateurs
    ```

```powershell title="Exemple 2"
Get-LocalUser | Select-Object Name, SID, Enabled   # comptes locaux et leurs SID
```

### Savoir qui est administrateur de la machine

```powershell title="Commande"
Get-LocalGroupMember -Group Administrateurs   # « Administrators » sur un Windows anglais
```

```powershell title="Exemple"
Get-LocalGroupMember -SID S-1-5-32-544   # par SID : indépendant de la langue
```

??? example "Sortie"
    ```text
    ObjectClass Name                        PrincipalSource
    ----------- ----                        ---------------
    Utilisateur PC-COMPTA-07\Administrateur Local
    Groupe      MERIDIAN\Admins du domaine  ActiveDirectory
    Groupe      MERIDIAN\GG-Support-Postes  ActiveDirectory
    ```

```bat title="Exemple 2"
net localgroup Administrateurs
```

## Permissions NTFS

### Lire les permissions d'un fichier ou d'un dossier

```bat title="Commande"
icacls <chemin>
```

```bat title="Exemple"
icacls "C:\Program Files\Updater"
```

??? example "Sortie"
    ```text
    C:\Program Files\Updater NT AUTHORITY\SYSTEM:(OI)(CI)(F)
                             BUILTIN\Administrateurs:(OI)(CI)(F)
                             BUILTIN\Utilisateurs:(OI)(CI)(M)
                             BUILTIN\Utilisateurs:(OI)(CI)(RX)
    ```

Ici, `Utilisateurs:(M)` sur un dossier de programme est une anomalie : tout utilisateur peut remplacer les fichiers.

| Droit | Signification | Héritage | Signification |
|---|---|---|---|
| `F` | Contrôle total | `(OI)` | Hérité par les fichiers |
| `M` | Modification | `(CI)` | Hérité par les sous-dossiers |
| `RX` | Lecture et exécution | `(IO)` | Seulement pour les enfants |
| `R` / `W` | Lecture / écriture | `(I)` | ACE héritée du parent |
| `D` | Suppression | `(NP)` | Ne descend que d'un niveau |

```powershell title="Exemple 2"
(Get-Acl "C:\Program Files\Updater").Access | Select-Object IdentityReference, FileSystemRights, AccessControlType, IsInherited
```

Pour comprendre : [Windows en profondeur, ch. 4 (permissions NTFS)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/04-chapitre-4-le-systeme-de-fichiers-ntfs.md)
{ .kw-cs-meta }

### Repérer les permissions trop larges

```powershell title="Commande"
Get-ChildItem <dossier> -Recurse -Directory -ErrorAction SilentlyContinue | ForEach-Object {
  $p = $_.FullName
  (Get-Acl $p).Access | Where-Object { $_.IdentityReference -match 'Everyone|Tout le monde|Utilisateurs|Users|Utilisateurs authentifiés|Authenticated Users' -and
      $_.FileSystemRights -match 'FullControl|Modify|Write' -and $_.AccessControlType -eq 'Allow' } |
    Select-Object @{n='Dossier';e={$p}}, IdentityReference, FileSystemRights }
```

```powershell title="Exemple"
# Même boucle sur C:\Program Files et C:\Program Files (x86)
```

??? example "Sortie"
    ```text
    Dossier                    IdentityReference    FileSystemRights
    -------                    -----------------    ----------------
    C:\Program Files\Updater   BUILTIN\Utilisateurs Modify, Synchronize
    ```

### Accorder ou retirer un droit

```bat title="Commande"
icacls <chemin> /grant <compte>:<droits>       :: ex. (OI)(CI)M pour dossier + contenu
icacls <chemin> /remove <compte>
icacls <chemin> /inheritance:d                 :: couper l'héritage en copiant les ACE
```

```bat title="Exemple"
icacls D:\Partages\Compta /grant "MERIDIAN\GG-Compta":(OI)(CI)M
icacls "C:\Program Files\Updater" /remove "BUILTIN\Utilisateurs"
```

??? example "Sortie"
    ```text
    fichier traité : D:\Partages\Compta
    1 fichiers correctement traités ; échec du traitement de 0 fichiers
    ```

!!! warning "Attention"
    Avant de modifier, sauvegarder les ACL : `icacls <chemin> /save acl.txt /t` (restauration : `icacls <parent> /restore acl.txt`). Donner les droits à des groupes, jamais à des comptes nominatifs.

### Prendre possession d'un fichier

```bat title="Commande"
takeown /f <chemin> [/r /d o]   :: devenir propriétaire (console administrateur)
```

```bat title="Exemple"
takeown /f D:\Archives\ancien-projet /r /d o
```

!!! warning "Attention"
    Opération d'administration : à tracer, et à réserver aux cas où l'ancien propriétaire n'existe plus.
