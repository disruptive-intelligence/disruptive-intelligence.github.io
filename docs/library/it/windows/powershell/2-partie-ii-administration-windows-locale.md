---
title: PARTIE II — ADMINISTRATION WINDOWS LOCALE
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 2
chapters: 8
---

À partir d'ici, PowerShell devient réellement un outil d'administration. On applique tout ce qu'on a appris (pipeline, objets, conditions, boucles, fonctions, gestion d'erreurs) à la gestion concrète d'un poste Windows : fichiers et permissions, comptes locaux, processus et services, registre, tâches planifiées, disques et logiciels.

Le fil conducteur de cette partie : **`Get`/`Test` d'abord, puis `Set`/`New`/`Remove`**. On regarde toujours avant de modifier.

---


## Chapitre 9 — Fichiers, dossiers et permissions NTFS

### 🟢 Le minimum à savoir

#### Lister et explorer

```powershell
Get-ChildItem C:\Scripts                 # contenu d'un dossier (alias : ls, dir)
Get-ChildItem C:\Scripts -Recurse        # récursif (sous-dossiers inclus)
Get-ChildItem C:\Scripts -File           # seulement les fichiers
Get-ChildItem C:\Scripts -Directory      # seulement les dossiers
Get-ChildItem C:\Logs -Filter *.log      # filtrés par motif
Get-Item C:\Scripts\run.ps1              # UN élément précis
```

`Get-ChildItem` renvoie des objets `FileInfo`/`DirectoryInfo`. Réflexe :

```powershell
Get-ChildItem C:\Scripts | Get-Member    # propriétés : Name, FullName, Length, LastWriteTime...
```

> **📌 Réflexe `Get-Member` :** un fichier n'est pas un nom, c'est un objet riche. `Length` (taille en octets), `CreationTime`, `LastWriteTime`, `Extension`, `FullName`, `Attributes`… autant de propriétés exploitables dans un tri, un filtre, un rapport.

#### Lire et écrire du contenu

```powershell
# Lire
Get-Content C:\Logs\app.log                       # tout le fichier (comme cat)
Get-Content C:\Logs\app.log -TotalCount 10        # 10 premières lignes (head)
Get-Content C:\Logs\app.log -Tail 20              # 20 dernières lignes (tail)
Get-Content C:\Logs\app.log -Tail 20 -Wait        # suit les ajouts en direct (tail -f)

# Écrire
Set-Content C:\out.txt -Value "ligne" -Encoding UTF8    # écrase (comme >)
Add-Content C:\out.txt -Value "ajout" -Encoding UTF8    # ajoute (comme >>)
```

> **⚠️ Encodage — un piège selon la version.** En **Windows PowerShell 5.1**, l'encodage par défaut de `Set-Content`/`Out-File` n'est pas UTF-8 (c'est souvent de l'ANSI ou de l'UTF-16), ce qui casse les accents dans d'autres outils. En **PowerShell 7**, le défaut est l'UTF-8 (sans BOM). Pour être tranquille et **portable entre versions**, précise **toujours** `-Encoding UTF8`.

#### Manipuler les chemins

```powershell
Join-Path C:\Scripts "logs\run.log"       # construit "C:\Scripts\logs\run.log"
Split-Path C:\Scripts\run.ps1 -Leaf        # "run.ps1"
Split-Path C:\Scripts\run.ps1 -Parent      # "C:\Scripts"
Test-Path C:\Scripts                        # le chemin existe ? (True/False)
Test-Path C:\Scripts -PathType Container    # est-ce un dossier ?
```

> **Bonne pratique :** construis toujours tes chemins avec `Join-Path` plutôt qu'en collant des chaînes avec `\`. Ça évite les doubles `\\` ou les séparateurs manquants, et reste correct quel que soit le contexte.

#### Créer, copier, déplacer, supprimer

```powershell
New-Item -ItemType Directory -Path C:\Scripts\archive -Force    # créer un dossier
New-Item -ItemType File -Path C:\Scripts\notes.txt             # créer un fichier
Copy-Item C:\a.txt C:\backup\a.txt                             # copier
Copy-Item C:\src\* C:\dst\ -Recurse                            # copier récursif
Move-Item C:\a.txt C:\archive\a.txt                            # déplacer / renommer
Remove-Item C:\vieux.txt                                       # supprimer
Remove-Item C:\vieuxdossier -Recurse -Force                    # supprimer un dossier
```

> **📌 `Test` avant d'agir :** `if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst }` — on vérifie l'existence avant de créer. Et `Remove-Item -Recurse -Force` est **irréversible** : pas de corbeille. Vérifie toujours ton chemin avant.

### 🟡 Très utile en pratique

#### CSV et JSON natifs (rappel et approfondissement)

On l'a vu au Ch.4 : PowerShell lit le CSV comme des **objets** et le JSON aussi. C'est un atout majeur pour l'administration.

```powershell
# CSV → objets (chaque ligne devient un objet avec des propriétés nommées)
$users = Import-Csv C:\users.csv -Encoding UTF8
$users | Where-Object { $_.Ville -eq "Paris" }

# objets → CSV
Get-Service | Select-Object Name, Status |
    Export-Csv C:\services.csv -NoTypeInformation -Encoding UTF8

# JSON
$config = Get-Content C:\config.json -Encoding UTF8 | ConvertFrom-Json
$config.ServerName
@{ Server = "SRV01"; Port = 8080 } | ConvertTo-Json | Set-Content C:\config.json -Encoding UTF8
```

On réutilisera intensivement `Import-Csv` pour créer des utilisateurs AD en masse (Ch.24).

#### Les permissions NTFS : `Get-Acl` / `Set-Acl`

Sur un volume NTFS, chaque fichier et dossier porte une **ACL** (Access Control List) — la liste de qui a le droit de faire quoi. Comprendre les ACL est fondamental en administration Windows.

Le vocabulaire minimal :

- **ACL** : la liste complète des permissions d'un objet
- **ACE** (Access Control Entry) : une entrée de cette liste — « tel utilisateur/groupe a tel droit, en Allow ou en Deny »
- **Allow / Deny** : autoriser ou refuser (un `Deny` l'emporte sur un `Allow`)
- **Héritage** : par défaut, un fichier hérite des permissions de son dossier parent
- **Propriétaire (Owner)** : le compte propriétaire de l'objet, qui peut toujours modifier ses permissions

```powershell
# LIRE les permissions d'un dossier
$acl = Get-Acl C:\Partages\Compta
$acl.Owner                       # le propriétaire
$acl.Access                      # la liste des ACE

# Afficher proprement qui a quoi
(Get-Acl C:\Partages\Compta).Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType, IsInherited
```

> **📌 Réflexe `Get-Member` :** `(Get-Acl C:\Partages\Compta).Access | Get-Member` te montre les propriétés d'une ACE (`IdentityReference` = qui, `FileSystemRights` = quel droit, `AccessControlType` = Allow/Deny, `IsInherited` = hérité ou explicite).

Modifier une ACL est plus délicat (on manipule des objets .NET). Le schéma général — **toujours en lisant l'ACL d'abord, en la modifiant, puis en la réappliquant** :

```powershell
$acl = Get-Acl C:\Partages\Compta                              # 1. lire
$regle = New-Object System.Security.AccessControl.FileSystemAccessRule(
    "lab\Comptables", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.AddAccessRule($regle)                                     # 2. modifier en mémoire
Set-Acl -Path C:\Partages\Compta -AclObject $acl              # 3. réappliquer   [🔑 Admin]
```

> **⚠️ Prudence extrême avec `Set-Acl`.** Une mauvaise manipulation d'ACL peut verrouiller un dossier pour tout le monde (y compris toi) ou, à l'inverse, l'ouvrir trop largement. Règles de survie : **lis et sauvegarde l'ACL existante avant** (`Get-Acl ... | Export-Clixml sauvegarde.xml`), teste sur un dossier bac à sable, et privilégie la gestion des droits via des **groupes** plutôt que des utilisateurs individuels. On reverra la distinction **permissions NTFS vs permissions de partage SMB** au Ch.28 — ce sont deux couches différentes qui se combinent.

### 🔴 Bonus

#### Rechercher dans des fichiers : `Select-String`

L'équivalent de `grep` :

```powershell
Select-String -Path C:\Logs\*.log -Pattern "ERROR"          # lignes contenant ERROR
Select-String -Path C:\Logs\*.log -Pattern "fail" -Context 2  # avec 2 lignes de contexte
```

Renvoie des objets `MatchInfo` (fichier, numéro de ligne, ligne) — donc filtrables et exploitables.

#### Prendre possession d'un dossier

Si tu n'as plus accès à un dossier, `takeown` (exécutable) puis `Set-Acl` permettent de reprendre la main — opération sensible, réservée aux cas de récupération, en `[🔑 Admin]`.

### ❌ Erreur classique

```powershell
# Oublier -Encoding UTF8 (accents cassés, surtout en 5.1)
Set-Content out.txt -Value "éàü"                   # ⚠️ selon la version
Set-Content out.txt -Value "éàü" -Encoding UTF8    # ✅

# Coller des chemins à la main
$p = "C:\Scripts" + "\" + $nom                     # ⚠️ fragile
$p = Join-Path C:\Scripts $nom                     # ✅

# Supprimer sans vérifier (pas de corbeille !)
Remove-Item C:\Data -Recurse -Force                # ❌ irréversible si mauvais chemin
if (Test-Path C:\Data) { Remove-Item C:\Data -Recurse -Force -WhatIf }   # ✅ teste d'abord

# Modifier une ACL sans l'avoir sauvegardée
Set-Acl ...                                        # ❌ sans filet
Get-Acl C:\D | Export-Clixml backup.xml; Set-Acl ...   # ✅
```

### 💡 Exercices

**Guidé :** Écris un script qui liste les fichiers d'un dossier (paramètre `-Path`) de plus de 100 Mo, triés par taille décroissante, avec nom et taille en Mo (propriété calculée).

**Autonome :** Écris un script qui affiche les ACE d'un dossier (`-Path`) sous forme de tableau lisible : qui (`IdentityReference`), quel droit (`FileSystemRights`), Allow/Deny, hérité ou non.

### 🧩 Mini-projet — Inventaire de dossier

Crée `Get-FolderReport.ps1` (paramètre `-Path`, `-OutputPath`) qui parcourt un dossier, produit un PSCustomObject par fichier (Nom, Extension, TailleMo, ModifieLe), exporte en CSV, et affiche un résumé (nombre de fichiers, taille totale, plus gros fichier). Réutilise pipeline, propriétés calculées, `Measure-Object` et `Export-Csv`.

### ✅ Tu sais maintenant...

- Explorer et manipuler fichiers/dossiers (`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`)
- Construire des chemins proprement (`Join-Path`, `Split-Path`, `Test-Path`)
- **Toujours** préciser `-Encoding UTF8` (piège 5.1 vs 7)
- Lire et exporter CSV/JSON nativement
- Lire les permissions NTFS avec `Get-Acl` (ACL, ACE, Allow/Deny, héritage, propriétaire) et la prudence requise pour `Set-Acl`

### 💬 Questions d'entretien typiques

- **Pourquoi toujours mettre `-Encoding UTF8` ?** → Parce que le défaut varie (5.1 ≠ 7) et casse les accents ; UTF-8 explicite rend le résultat portable.
- **Qu'est-ce qu'une ACE ?** → Une entrée d'ACL : un couple (identité, droit) en Allow ou Deny, hérité ou explicite.
- **Comment modifier des permissions sans risque ?** → Sauvegarder l'ACL (`Get-Acl | Export-Clixml`), travailler par groupes, tester sur un bac à sable, puis `Set-Acl`.

---


## Chapitre 10 — Utilisateurs et groupes locaux

### 🟢 Le minimum à savoir

#### Comptes locaux vs comptes de domaine

Une machine Windows a des **comptes locaux** (définis sur la machine elle-même). Dans un domaine, il existe aussi des **comptes AD** (centralisés, vus en Partie IV). Ce chapitre traite les **comptes locaux** — gérés par le module `Microsoft.PowerShell.LocalAccounts`.

> **Note :** ces cmdlets `*-LocalUser` / `*-LocalGroup` fonctionnent sur Windows 10/11 et Windows Server. Elles agissent sur la base SAM locale, pas sur l'annuaire du domaine.

#### Lister les utilisateurs et groupes locaux

```powershell
Get-LocalUser                        # tous les comptes locaux
Get-LocalUser -Name Administrateur   # un compte précis
Get-LocalGroup                       # tous les groupes locaux
Get-LocalGroupMember -Group "Administrateurs"   # membres du groupe Administrateurs
```

> **📌 Réflexe `Get-Member` :** `Get-LocalUser | Get-Member` révèle `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, `SID`… Autant de propriétés pour auditer les comptes.

#### Le cas d'usage n°1 : auditer les administrateurs locaux

Qui est administrateur local d'une machine ? C'est une **question de sécurité fondamentale** — trop d'admins locaux = surface d'attaque.

```powershell
Get-LocalGroupMember -Group "Administrateurs" |
    Select-Object Name, PrincipalSource, ObjectClass
```

`PrincipalSource` indique si le membre est local ou vient du domaine ; `ObjectClass` s'il s'agit d'un utilisateur ou d'un groupe.

> **Note langue :** le groupe s'appelle `Administrateurs` sur un Windows en français, `Administrators` en anglais. Pour un script portable, on peut cibler par SID : le groupe Administrateurs a toujours le SID `S-1-5-32-544`. `Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"`.

#### Créer, modifier, désactiver un compte local `[🔑 Admin]`

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

#### Gérer l'appartenance aux groupes `[🔑 Admin]`

```powershell
Add-LocalGroupMember    -Group "Administrateurs" -Member "svc_backup"
Remove-LocalGroupMember -Group "Administrateurs" -Member "svc_backup"
```

### 🟡 Très utile en pratique

#### Auditer tous les comptes actifs

```powershell
Get-LocalUser | Where-Object Enabled |
    Select-Object Name, LastLogon, PasswordExpires |
    Sort-Object LastLogon
```

Repérer un compte activé jamais connecté, ou un mot de passe qui n'expire jamais, est un réflexe d'hygiène de sécurité.

#### Produire un rapport de tous les groupes et leurs membres

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

### 🔴 Bonus

#### Le compte administrateur intégré

Le compte `Administrateur` (SID se terminant par `-500`) est souvent désactivé par défaut sur les postes modernes. On peut le repérer :

```powershell
Get-LocalUser | Where-Object { $_.SID -like "*-500" }
```

Un compte `-500` **activé** et renommé est un point d'attention en sécurité.

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Affiche les membres du groupe Administrateurs locaux avec leur type et leur source. Cible le groupe par son SID pour être portable.

**Autonome :** Écris un script qui liste tous les comptes locaux activés dont le mot de passe n'expire jamais (`PasswordExpires -eq $null`) — un point d'audit de sécurité classique.

### 🧩 Mini-projet — Audit des comptes locaux

Crée `Get-LocalAccountAudit.ps1` qui produit un rapport CSV : tous les comptes locaux avec `Name`, `Enabled`, `LastLogon`, `PasswordExpires`, et une colonne `EstAdmin` (True si le compte est membre du groupe Administrateurs). Réutilise `Get-LocalUser`, `Get-LocalGroupMember`, PSCustomObject et `Export-Csv`.

### ✅ Tu sais maintenant...

- La différence comptes locaux / comptes de domaine
- Lister, créer, modifier, désactiver des comptes locaux (`*-LocalUser`)
- Gérer les groupes locaux et leurs membres (`*-LocalGroup*`)
- Auditer les administrateurs locaux (par nom ou par SID, pour la portabilité)
- Préférer **désactiver** à **supprimer**

### 💬 Questions d'entretien typiques

- **Pourquoi désactiver plutôt que supprimer un compte ?** → Réversible, conserve le SID et l'historique des permissions.
- **Comment auditer les admins locaux de façon portable (FR/EN) ?** → Cibler le groupe par SID `S-1-5-32-544` plutôt que par son nom.
- **Différence compte local / compte de domaine ?** → Le compte local vit dans la base SAM de la machine ; le compte de domaine est centralisé dans Active Directory.

---


## Chapitre 11 — Processus et services

### 🟢 Le minimum à savoir

#### Processus vs services : la distinction

- Un **processus** est un programme en cours d'exécution (une instance de `chrome.exe`, `notepad.exe`…). Il a un **PID** (identifiant numérique).
- Un **service** est un programme qui tourne en **arrière-plan**, souvent sans interface, géré par Windows (démarrage automatique, redémarrage en cas d'échec…). Le pare-feu, Windows Update, le spouleur d'impression sont des services.

Un service, quand il tourne, s'exécute *via* un ou plusieurs processus — mais on les gère avec des cmdlets différentes.

#### Gérer les processus

```powershell
Get-Process                          # tous les processus
Get-Process -Name chrome             # par nom
Get-Process -Id 1234                 # par PID

# Les 5 plus gros consommateurs de mémoire
Get-Process | Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{N="RAM(Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 5

# Lancer / arrêter
Start-Process notepad
Start-Process "C:\outil.exe" -ArgumentList "/silent"
Stop-Process -Name notepad
Stop-Process -Id 1234 -Force
```

> **📌 Réflexe `Get-Member` :** `Get-Process | Get-Member` révèle `Id`, `Name`, `CPU`, `WorkingSet64` (mémoire), `Path`, `StartTime`, et des méthodes comme `.Kill()`. Un processus est un objet riche — on peut trier, filtrer, corréler.

> **⚠️ `Stop-Process` est brutal :** il tue le processus sans sauvegarde (comme `kill -9`). Vérifie le PID/nom avant. Certains processus système protégés nécessitent `[🔑 Admin]`.

#### Gérer les services

```powershell
Get-Service                           # tous les services
Get-Service -Name wuauserv            # un service précis (Windows Update)
Get-Service | Where-Object Status -eq "Running"    # ceux qui tournent

# Contrôler un service                                   [🔑 Admin]
Start-Service   -Name wuauserv
Stop-Service    -Name wuauserv
Restart-Service -Name wuauserv

# Changer le type de démarrage                           [🔑 Admin]
Set-Service -Name wuauserv -StartupType Automatic   # Automatic / Manual / Disabled
```

Les propriétés clés d'un service : `Name`, `DisplayName`, `Status` (Running/Stopped), `StartType` (Automatic/Manual/Disabled), `DependentServices`, `ServicesDependedOn`.

#### Le point à investiguer : Automatic + Stopped

Un service configuré en démarrage **automatique** mais actuellement **arrêté** est un **point à investiguer** — pas nécessairement une panne :

```powershell
# Version portable 5.1 et 7 via CIM (StartMode = "Auto" pour les services automatiques)
Get-CimInstance Win32_Service |
    Where-Object { $_.StartMode -eq "Auto" -and $_.State -eq "Stopped" } |
    Select-Object Name, DisplayName, StartMode, State
```

> **⚠️ Nuance importante — « Automatic + Stopped » n'est pas toujours une anomalie.** Windows gère des services **déclenchés par événement** (*trigger-start*) : un service peut être configuré en automatique (ou automatique-différé), démarrer quand un événement survient, puis **s'arrêter légitimement** quand il n'a plus de travail. Le voir `Stopped` à un instant donné peut être parfaitement normal. Microsoft recommande même ce modèle *trigger-start* dans certains scénarios.
>
> La bonne façon de raisonner la **conformité** n'est donc pas « tout service Automatic doit être Running », mais : **comparer l'état observé à une baseline attendue** (la liste des services qui, chez toi, *doivent* tourner en permanence). Un service critique attendu en fonctionnement continu et trouvé arrêté = à investiguer ; un service *trigger-start* arrêté = souvent normal.

C'est un contrôle de santé que tout administrateur fait régulièrement — en gardant cette nuance à l'esprit.

#### Les dépendances de services

Certains services en requièrent d'autres. Le savoir évite les mauvaises surprises quand on en arrête un :

```powershell
(Get-Service -Name wuauserv).ServicesDependedOn    # ce dont dépend Windows Update
(Get-Service -Name rpcss).DependentServices         # ce qui dépend de RPCSS
```

> **Piège :** arrêter un service dont dépendent d'autres services les arrête aussi (avec `-Force`) ou échoue (sans). Toujours vérifier `DependentServices` avant un `Stop-Service`.

### 🟡 Très utile en pratique

#### `Get-Service` vs `Get-CimInstance Win32_Service`

`Get-Service` est simple mais limité. Pour obtenir le **compte de service**, le **chemin de l'exécutable** ou le **PID**, on passe par CIM :

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName, PathName |
    Where-Object { $_.StartName -notlike "*LocalSystem*" }
```

`StartName` (le compte sous lequel tourne le service) et `PathName` (le binaire) sont essentiels en administration **et** en sécurité — un service tournant depuis un chemin inhabituel est suspect (on approfondit au Ch.34).

#### Un contrôle de santé de services critiques

```powershell
function Test-CriticalServices {
    [CmdletBinding()]
    param([string[]]$Services = @("wuauserv","WinDefend","EventLog","Spooler"))

    foreach ($nom in $Services) {
        $svc = Get-Service -Name $nom -ErrorAction SilentlyContinue
        # StartMode via CIM = portable 5.1 et 7 (contrairement à $svc.StartType, PS7 seulement)
        $cim = Get-CimInstance Win32_Service -Filter "Name='$nom'" -ErrorAction SilentlyContinue
        [PSCustomObject]@{
            Service   = $nom
            Present   = [bool]$svc
            Statut    = if ($svc) { $svc.Status } else { "ABSENT" }
            Demarrage = if ($cim) { $cim.StartMode } else { "-" }   # Auto / Manual / Disabled
        }
    }
}

Test-CriticalServices | Format-Table -AutoSize
```

Ce petit outil réunit fonctions (Ch.7), gestion d'absence (Ch.8), collections (Ch.6) et PSCustomObject. Il utilise `Win32_Service`.`StartMode` pour rester portable entre Windows PowerShell 5.1 et PowerShell 7.

### 🔴 Bonus

#### Processus et leur ligne de commande complète

La ligne de commande exacte d'un processus (arguments inclus) est précieuse pour le diagnostic :

```powershell
Get-CimInstance Win32_Process -Filter "Name = 'powershell.exe'" |
    Select-Object ProcessId, CommandLine
```

Un `powershell.exe` lancé avec des arguments encodés en base64 est un signal d'alerte (Ch.34).

### ❌ Erreur classique

```powershell
# Arrêter un service sans vérifier ses dépendances
Stop-Service RPCSS            # ❌ échoue ou casse une cascade de services
(Get-Service RPCSS).DependentServices   # ✅ vérifier d'abord

# Utiliser Get-Service quand on a besoin du chemin/compte du service
Get-Service wuauserv | Select-Object Path    # ❌ pas de propriété Path
Get-CimInstance Win32_Service -Filter "Name='wuauserv'" | Select PathName, StartName  # ✅

# Tuer un processus par nom alors que plusieurs instances tournent
Stop-Process -Name chrome     # ⚠️ tue TOUTES les instances de Chrome
```

### 💡 Exercices

**Guidé :** Affiche les services en démarrage automatique actuellement arrêtés, triés par nom.

**Autonome :** Écris un script qui prend un `-ServiceName`, vérifie ses dépendances (`ServicesDependedOn`), et n'affiche un message de redémarrage possible que si toutes ses dépendances sont `Running`.

### 🧩 Mini-projet — Rapport de services critiques

Étends `Test-CriticalServices` : la conformité se juge **par rapport à une baseline** que tu définis (les services qui, chez toi, doivent tourner en permanence). Ajoute une colonne `Conforme` (True si un service **attendu en fonctionnement** est bien `Running`), affiche en couleur les non-conformes, et exporte le rapport complet en CSV horodaté (`services_$(Get-Date -Format yyyyMMdd).csv`). Note que « Automatic + Stopped » seul ne suffit pas à conclure : compare à ta liste attendue.

### ✅ Tu sais maintenant...

- La différence processus / service
- Gérer les processus (`Get/Start/Stop-Process`) et les services (`Get/Start/Stop/Restart/Set-Service`)
- Repérer le point à investiguer « Automatic + Stopped » — en le comparant à une baseline (pas une anomalie automatique, à cause des services *trigger-start*)
- Vérifier les dépendances avant d'arrêter un service
- Passer par `Win32_Service` pour le compte et le chemin d'un service

### 💬 Questions d'entretien typiques

- **Différence entre un processus et un service ?** → Un processus est un programme en cours ; un service tourne en arrière-plan sous le contrôle du gestionnaire de services (démarrage auto, resilience).
- **Comment obtenir le chemin du binaire d'un service ?** → `Get-CimInstance Win32_Service` (propriété `PathName`), car `Get-Service` ne l'expose pas.
- **Quel contrôle de santé faire sur les services ?** → Comparer l'état à une baseline : les services *attendus en fonctionnement continu* doivent être `Running`. « Automatic + Stopped » est un point à investiguer, mais pas une anomalie en soi (services *trigger-start*).

---


## Chapitre 12 — Le registre Windows

### 🟢 Le minimum à savoir

#### Qu'est-ce que le registre ?

Le registre est la **base de données de configuration** de Windows. On y trouve les réglages du système, des logiciels, des associations de fichiers, des politiques de sécurité, et — ce qui intéressera la Partie VIII — des mécanismes de démarrage automatique.

PowerShell traite le registre **comme un système de fichiers** : mêmes cmdlets que pour les dossiers.

#### Les ruches principales

```powershell
Get-PSDrive -PSProvider Registry    # les "lecteurs" du registre
```

| Ruche | Abréviation | Contenu |
|-------|-------------|---------|
| `HKEY_CURRENT_USER` | `HKCU:` | Configuration de l'utilisateur **courant** |
| `HKEY_LOCAL_MACHINE` | `HKLM:` | Configuration de la **machine** (nécessite `[🔑 Admin]` pour écrire) |

#### Lire le registre

```powershell
# Parcourir comme un dossier
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion"

# Lire TOUTES les valeurs d'une clé
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"

# Lire UNE valeur précise
Get-ItemPropertyValue "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName
```

> **📌 Réflexe `Test-Path` :** avant de lire ou d'écrire, `Test-Path "HKLM:\SOFTWARE\MonApp"` évite les erreurs sur une clé absente.

#### Le concept de PSDrive : une abstraction unifiée

Le registre est un exemple de **PSDrive** — PowerShell présente plusieurs systèmes comme des « lecteurs » navigables avec les **mêmes** cmdlets (`Get-ChildItem`, `Get-ItemProperty`…) :

| PSDrive | Contenu |
|---------|---------|
| `C:`, `D:` | Système de fichiers |
| `HKCU:`, `HKLM:` | Registre |
| `Env:` | Variables d'environnement |
| `Cert:` | Certificats |
| `Variable:` | Variables PowerShell |

```powershell
Get-ChildItem Env:                       # toutes les variables d'environnement
Get-ChildItem Cert:\CurrentUser\My       # tes certificats personnels
```

C'est une idée puissante : apprendre `Get-ChildItem` une fois, l'utiliser partout.

#### Modifier le registre `[🔑 Admin pour HKLM]`

**Discipline `Test`/`Get` avant `Set`/`New`** — et prudence maximale :

```powershell
# Créer une clé (si absente)
if (-not (Test-Path "HKCU:\Software\MonApp")) {
    New-Item -Path "HKCU:\Software\MonApp" -Force
}

# Créer une valeur avec son type explicite
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "dark" -PropertyType String
New-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Version" -Value 2 -PropertyType DWord

# Modifier une valeur existante
Set-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme" -Value "light"

# Supprimer
Remove-ItemProperty -Path "HKCU:\Software\MonApp" -Name "Theme"
Remove-Item -Path "HKCU:\Software\MonApp" -Recurse
```

Les types de valeurs courants : `String`, `DWord` (entier 32 bits), `QWord` (64 bits), `Binary`, `ExpandString`, `MultiString`.

> **⚠️ Le registre est critique — prudence maximale.** Une mauvaise modification de `HKLM:` peut empêcher Windows de démarrer. Règles de survie : travaille d'abord dans `HKCU:` (moins dangereux), **sauvegarde** la clé avant modification (`reg export`), et ne touche à `HKLM:` que si tu sais exactement ce que tu fais. `New-ItemProperty` pour créer (avec `-PropertyType`), `Set-ItemProperty` pour modifier.

### 🟡 Très utile en pratique

#### Sauvegarder avant de modifier

```powershell
# Exporter une clé avant de la toucher (via l'outil reg.exe)
reg export "HKLM\SOFTWARE\MonApp" "C:\backup\MonApp.reg" /y
```

C'est le `Get`/backup avant `Set` appliqué au registre. Indispensable en production.

#### Lire une information de configuration système

```powershell
# Version précise de Windows depuis le registre
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild
```

### 🔴 Bonus

#### Les clés de démarrage automatique

Certaines clés lancent des programmes au démarrage — utile à connaître pour l'admin, essentiel pour la sécurité (persistance de malware, Ch.34) :

```powershell
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
```

> **Renvoi croisé :** on réutilise exactement ces clés `Run`/`RunOnce` au **Ch.34** pour le triage de persistance. Ici on les lit comme configuration ; là-bas on les analyse comme indicateur de compromission.

### ❌ Erreur classique

```powershell
# Écrire dans HKLM sans droits admin
Set-ItemProperty "HKLM:\..." -Name X -Value 1     # ❌ Accès refusé
# → console en administrateur

# Confondre New-ItemProperty (créer) et Set-ItemProperty (modifier)
Set-ItemProperty "HKCU:\Software\MonApp" -Name Nouveau -Value 1   # crée quand même,
# mais sans contrôle du type → préférer New-ItemProperty -PropertyType pour créer

# Modifier le registre sans sauvegarde
Set-ItemProperty "HKLM:\..."                       # ❌ sans filet
reg export "HKLM\..." backup.reg /y ; Set-ItemProperty ...   # ✅
```

### 💡 Exercices

**Guidé :** Lis et affiche `ProductName`, `DisplayVersion` et `CurrentBuild` depuis `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion`.

**Autonome :** Écris un script qui crée une clé `HKCU:\Software\MonLab`, y ajoute une valeur `String` et une valeur `DWord`, les relit pour vérifier, puis supprime la clé entière. Encadre chaque étape d'un `Test-Path`.

### ✅ Tu sais maintenant...

- Ce qu'est le registre et ses ruches (`HKCU:`, `HKLM:`)
- Le lire (`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`)
- Le modifier (`New-ItemProperty` pour créer avec type, `Set-ItemProperty` pour modifier)
- Le concept unificateur de **PSDrive** (fichiers, registre, Env:, Cert:…)
- La prudence : `HKCU:` d'abord, sauvegarde avant `HKLM:`

### 💬 Questions d'entretien typiques

- **Comment PowerShell voit-il le registre ?** → Comme un système de fichiers (un PSDrive), navigable avec `Get-ChildItem`, `Get-ItemProperty`…
- **Différence `HKCU:` / `HKLM:` ?** → `HKCU:` = config de l'utilisateur courant ; `HKLM:` = config machine, écriture réservée aux administrateurs.
- **`New-ItemProperty` ou `Set-ItemProperty` ?** → `New-ItemProperty` pour créer une valeur (avec `-PropertyType`), `Set-ItemProperty` pour en modifier une existante.

---


## Chapitre 13 — Tâches planifiées

### 🟢 Le minimum à savoir

#### À quoi ça sert

Une **tâche planifiée** exécute un programme ou un script automatiquement : à heure fixe, au démarrage, à la connexion d'un utilisateur, ou sur événement. C'est l'équivalent Windows de `cron` sous Linux — et c'est ainsi qu'on **automatise** l'exécution de ses scripts PowerShell (sauvegardes, rapports, nettoyages).

#### Lister et inspecter les tâches

```powershell
Get-ScheduledTask                                   # toutes les tâches
Get-ScheduledTask -TaskName "MaTache"               # une tâche
Get-ScheduledTask | Where-Object State -eq "Ready"  # les tâches actives

# Infos d'exécution (dernier/prochain lancement, dernier résultat)
Get-ScheduledTask -TaskName "MaTache" | Get-ScheduledTaskInfo
```

> **📌 Réflexe `Get-Member` :** `Get-ScheduledTask | Get-Member` montre `TaskName`, `TaskPath`, `State`, `Actions`, `Triggers`, `Principal`. Une tâche est un objet composé : elle contient des **actions** (quoi exécuter) et des **déclencheurs** (quand).

#### Les 4 briques d'une tâche

Créer une tâche, c'est assembler quatre éléments :

1. **Action** — quoi exécuter (`New-ScheduledTaskAction`)
2. **Déclencheur (trigger)** — quand (`New-ScheduledTaskTrigger`)
3. **Principal** — sous quel compte et avec quels privilèges (`New-ScheduledTaskPrincipal`)
4. **Enregistrement** — assembler et créer (`Register-ScheduledTask`)

#### Créer une tâche planifiée `[🔑 Admin]`

```powershell
# 1. Action : lancer un script PowerShell
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -File C:\Scripts\backup.ps1"

# 2. Déclencheur : tous les jours à 2h du matin
$trigger = New-ScheduledTaskTrigger -Daily -At "02:00"

# 3. Principal : exécuter en tant que SYSTEM, avec privilèges élevés
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

# 4. Enregistrer
Register-ScheduledTask -TaskName "BackupQuotidien" `
    -Action $action -Trigger $trigger -Principal $principal `
    -Description "Sauvegarde quotidienne à 2h"
```

> **Note sur l'argument :** pour lancer un script `.ps1`, on exécute `powershell.exe` (ou `pwsh.exe` en PS7) avec `-File`. `-NoProfile` (ignore le profil, pour un environnement prévisible) est une bonne habitude.
>
> **⚠️ À propos de `-ExecutionPolicy Bypass` :** on voit souvent `-ExecutionPolicy Bypass` ajouté ici par réflexe. **Ne l'utilise pas systématiquement.** Rappel du Ch.1 : l'Execution Policy n'est pas une frontière de sécurité, mais l'ajouter aveuglément dans chaque tâche est une mauvaise habitude qui banalise le contournement. La bonne approche : le script tourne sous une **policy correctement configurée** (souvent `RemoteSigned` imposée par GPO) ou, mieux, il est **signé** (Ch.35). Réserve `Bypass` à un choix **volontaire et justifié** dans un contexte contrôlé — pas à une recette copiée-collée partout.

#### Supprimer une tâche

```powershell
Unregister-ScheduledTask -TaskName "BackupQuotidien" -Confirm:$false
```

### 🟡 Très utile en pratique

#### Comprendre le contexte d'exécution

Une tâche s'exécute sous un **compte** avec un **niveau de privilège** — deux points cruciaux :

- **Le compte** (`-UserId`) : `SYSTEM` (tout-puissant local), un compte de service dédié, ou un utilisateur. Détermine les droits **et** l'accès réseau.
- **Le niveau** (`-RunLevel`) : `Limited` (normal) ou `Highest` (élevé). Un script qui touche à `HKLM:` ou aux services a besoin de `Highest`.
- **« Exécuter même si l'utilisateur n'est pas connecté »** : implique de stocker des identifiants — sujet sécurité (Ch.33).

> **Réflexe sécurité :** une tâche planifiée tournant en `SYSTEM` qui lance un script modifiable par tous est une porte d'entrée classique pour l'élévation de privilèges. On y revient au Ch.34 (triage de persistance) : les tâches planifiées sont un mécanisme de persistance très utilisé.

#### Différents types de déclencheurs

```powershell
New-ScheduledTaskTrigger -Daily -At "02:00"                  # quotidien
New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At "8am"  # hebdomadaire
New-ScheduledTaskTrigger -AtStartup                          # au démarrage machine
New-ScheduledTaskTrigger -AtLogOn                            # à la connexion
```

### 🔴 Bonus

#### Auditer les tâches non standard

```powershell
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, TaskPath, State,
        @{N="Action";E={$_.Actions.Execute}}
```

Filtrer les tâches hors `\Microsoft\*` fait ressortir celles ajoutées par des logiciels ou des humains — un bon point de départ pour un audit (et pour du triage de sécurité, Ch.34).

### ❌ Erreur classique

```powershell
# Ajouter -ExecutionPolicy Bypass par réflexe dans CHAQUE tâche
-Argument "-NoProfile -ExecutionPolicy Bypass -File C:\s.ps1"   # ⚠️ mauvaise habitude
# ✅ compter sur une policy correcte (GPO) ou un script signé ; Bypass = choix justifié seulement

# Créer une tâche SYSTEM lançant un script world-writable
# ❌ risque d'élévation de privilèges — protéger les ACL du script (Ch.9)

# Chemins relatifs dans une tâche
-Argument "-File .\backup.ps1"     # ❌ le dossier courant n'est pas garanti
-Argument "-File C:\Scripts\backup.ps1"   # ✅ chemin absolu
```

### 💡 Exercices

**Guidé :** Liste les tâches planifiées actives (`State -eq "Ready"`) qui ne sont pas dans `\Microsoft\`, avec leur nom et l'exécutable lancé.

**Autonome :** Crée une tâche `RapportHebdo` qui lance un script PowerShell tous les lundis à 8h, puis vérifie sa création avec `Get-ScheduledTaskInfo`, puis supprime-la.

### ✅ Tu sais maintenant...

- Le rôle des tâches planifiées (automatiser ses scripts, équivalent `cron`)
- Lister et inspecter (`Get-ScheduledTask`, `Get-ScheduledTaskInfo`)
- Les 4 briques : action, déclencheur, principal, enregistrement
- L'importance du **contexte d'exécution** (compte + niveau de privilège)
- Le lien avec la sécurité (persistance, à revoir Ch.34)

### 💬 Questions d'entretien typiques

- **Comment automatiser l'exécution quotidienne d'un script PowerShell ?** → Une tâche planifiée avec une action `powershell.exe -File ...` et un déclencheur `-Daily`.
- **Pourquoi le compte d'exécution d'une tâche est-il sensible ?** → Il détermine les privilèges ; une tâche `SYSTEM` lançant un script modifiable par tous permet une élévation de privilèges.
- **Équivalent de `cron` sous Windows ?** → Le Planificateur de tâches, piloté par les cmdlets `*-ScheduledTask*`.

---


## Chapitre 14 — Disques, volumes et stockage

### 🟢 Le minimum à savoir

#### Les trois niveaux : disque, partition, volume

Le stockage Windows s'empile en trois couches, et les cmdlets suivent cette logique :

- **Disque** (`Get-Disk`) : le matériel physique (ou virtuel)
- **Partition** (`Get-Partition`) : une division d'un disque
- **Volume** (`Get-Volume`) : un système de fichiers monté, souvent avec une lettre (`C:`, `D:`)

```powershell
Get-Disk                     # les disques physiques
Get-Partition                # les partitions
Get-Volume                   # les volumes (avec espace libre !)
```

> **📌 Réflexe `Get-Member` :** `Get-Volume | Get-Member` révèle `DriveLetter`, `FileSystemLabel`, `Size`, `SizeRemaining`, `HealthStatus`. C'est `Get-Volume` qu'on utilise le plus, car il donne directement l'espace libre.

#### Le cas d'usage n°1 : surveiller l'espace disque

C'est l'une des vérifications les plus fréquentes en administration. Un disque plein = services qui tombent, logs qui ne s'écrivent plus, serveur en panne.

```powershell
Get-Volume | Where-Object DriveLetter |
    Select-Object DriveLetter, FileSystemLabel,
        @{N="TailleGB";E={[math]::Round($_.Size/1GB,1)}},
        @{N="LibreGB";E={[math]::Round($_.SizeRemaining/1GB,1)}},
        @{N="Libre%";E={[math]::Round($_.SizeRemaining/$_.Size*100,1)}}
```

#### Alerter sous un seuil

```powershell
$SeuilGB = 20

Get-Volume | Where-Object { $_.DriveLetter -and ($_.SizeRemaining/1GB) -lt $SeuilGB } |
    ForEach-Object {
        Write-Host "ALERTE $($_.DriveLetter): $([math]::Round($_.SizeRemaining/1GB,1)) Go libres" -ForegroundColor Red
    }
```

#### `Get-PSDrive` : la vue rapide

`Get-PSDrive` donne une vue synthétique (et couvre aussi les lecteurs réseau) :

```powershell
Get-PSDrive -PSProvider FileSystem |
    Select-Object Name,
        @{N="LibreGB";E={[math]::Round($_.Free/1GB,1)}},
        @{N="UtiliséGB";E={[math]::Round($_.Used/1GB,1)}}
```

### 🟡 Très utile en pratique

#### Santé des disques

```powershell
Get-Disk | Select-Object Number, FriendlyName, HealthStatus, OperationalStatus,
    @{N="TailleGB";E={[math]::Round($_.Size/1GB)}}
```

`HealthStatus` (`Healthy`/`Warning`/`Unhealthy`) est un indicateur de défaillance matérielle à surveiller.

#### Intégrer l'espace disque à la fiche du poste

Souviens-toi de `Get-PosteInfo.ps1` (Ch.2). On peut maintenant y ajouter le disque :

```powershell
$c = Get-Volume -DriveLetter C
"Disque C: : $([math]::Round($c.SizeRemaining/1GB,1)) Go libres sur $([math]::Round($c.Size/1GB,1)) Go"
```

### 🔴 Bonus `[🖥️ Server]`

#### Création de partitions et formatage

Sur un serveur, on peut initialiser et partitionner un nouveau disque — opérations **destructives**, à manier avec une extrême prudence :

```powershell
# Exemple (DESTRUCTIF) : initialiser le disque 1, créer une partition, formater
# Initialize-Disk -Number 1 -PartitionStyle GPT
# New-Partition -DiskNumber 1 -UseMaximumSize -AssignDriveLetter |
#     Format-Volume -FileSystem NTFS -NewFileSystemLabel "Data"
```

> **⚠️ `Format-Volume` et `Initialize-Disk` effacent les données.** Vérifie **trois fois** le numéro de disque (`Get-Disk`) avant. Une erreur de numéro formate le mauvais disque.

### ❌ Erreur classique

```powershell
# Confondre Size (octets) et affichage en Go (oubli de la division)
$v.Size            # ❌ un énorme nombre en octets
$v.Size / 1GB      # ✅ en gigaoctets

# Filtrer les volumes sans lettre (partitions système)
Get-Volume | Select DriveLetter, SizeRemaining    # ⚠️ inclut des volumes sans lettre
Get-Volume | Where-Object DriveLetter | ...        # ✅ seulement les volumes montés

# Se tromper de numéro de disque avant un formatage
Format-Volume ...    # ❌❌ vérifier Get-Disk avant, TOUJOURS
```

### 💡 Exercices

**Guidé :** Affiche tous les volumes avec lettre, leur taille, leur espace libre en Go et le pourcentage libre.

**Autonome :** Écris un script `-SeuilGB` (défaut 20) qui liste les volumes sous le seuil et renvoie un PSCustomObject par volume concerné (Lecteur, LibreGB, Pourcent). Exporte en CSV si au moins un volume est en alerte.

---

### Rôles, fonctionnalités et logiciels

Cette section clôt la Partie II en abordant l'inventaire du logiciel installé — côté client comme côté serveur.

#### Rôles et fonctionnalités Windows Server `[🖥️ Server]`

Sur **Windows Server**, les capacités s'ajoutent sous forme de **rôles** (AD DS, DNS, DHCP, File Server…) et **fonctionnalités**. On les gère avec le module `ServerManager` :

```powershell
Get-WindowsFeature                                   # tout, avec l'état Installed/Available
Get-WindowsFeature | Where-Object Installed          # ce qui est installé
Install-WindowsFeature -Name DNS -IncludeManagementTools    # installer le rôle DNS  [🔑 Admin]
```

> **Important :** `Get-WindowsFeature` / `Install-WindowsFeature` n'existent **que sur Windows Server**, pas sur Windows 10/11. C'est ainsi qu'on installe les rôles qu'on administrera en Parties IV et V (AD, DNS, DHCP…).

#### Fonctionnalités sur Windows 10/11

Côté **client**, l'équivalent passe par d'autres cmdlets :

```powershell
Get-WindowsOptionalFeature -Online                          # fonctionnalités optionnelles
Get-WindowsOptionalFeature -Online -FeatureName *Hyper-V*   # rechercher
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All   # activer  [🔑 Admin]
```

C'est ainsi qu'on active, par exemple, Hyper-V ou le client OpenSSH sur un poste.

#### Inventorier les logiciels installés — SANS `Win32_Product`

Question fréquente : « quels logiciels sont installés ? ». La tentation est d'utiliser `Get-CimInstance Win32_Product`. **À éviter absolument.**

> **⚠️ Ne JAMAIS utiliser `Win32_Product` pour un inventaire.** Interroger cette classe déclenche, pour **chaque** logiciel MSI, une vérification de cohérence (une réparation à blanc) — c'est **lent** et surtout ça peut générer des milliers d'événements et **relancer des installations**. C'est un piège classique qui a causé de vrais incidents en production.

La bonne méthode : lire les clés de désinstallation du registre.

```powershell
$chemins = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*",
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
)

Get-ItemProperty $chemins -ErrorAction SilentlyContinue |
    Where-Object DisplayName |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Sort-Object DisplayName
```

Cette approche est **rapide et sûre** pour inventorier les applications **desktop enregistrées au niveau machine**, en 32 comme en 64 bits (grâce à `WOW6432Node`). C'est celle qu'utilisent les vrais outils d'inventaire.

> **Ce qu'elle ne couvre pas.** Deux angles morts à connaître : les logiciels installés **par utilisateur** (clé `HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*`, à ajouter si besoin), et les applications **AppX/MSIX** (applications du Microsoft Store et applications modernes), qui ont leur propre mécanisme d'inventaire :
> ```powershell
> Get-AppxPackage | Select-Object Name, Version, PackageFullName
> ```
> Un inventaire réellement exhaustif combine donc les clés `Uninstall` (machine + utilisateur) et `Get-AppxPackage`.

### ✅ Tu sais maintenant...

- Les trois couches disque / partition / volume et leurs cmdlets
- Surveiller l'espace disque et alerter sous un seuil (le cas d'usage n°1)
- Vérifier la santé des disques (`HealthStatus`)
- Installer des rôles/fonctionnalités (`Install-WindowsFeature` sur **Server** uniquement)
- Inventorier les logiciels **via le registre**, jamais avec `Win32_Product`

### 💬 Questions d'entretien typiques

- **Comment vérifier l'espace disque libre ?** → `Get-Volume` (propriété `SizeRemaining`) ou `Get-PSDrive`, avec un calcul en Go.
- **Pourquoi éviter `Win32_Product` ?** → Son interrogation déclenche une vérification/réparation de chaque MSI : lent et potentiellement perturbant. On lit plutôt les clés `Uninstall` du registre.
- **Où installe-t-on un rôle comme DNS ou AD DS ?** → Sur Windows Server, avec `Install-WindowsFeature` (indisponible sur les clients).

### 🧩 Capstone Partie II — Boîte à outils du poste local

Assemble un script `Get-LocalHealthReport.ps1` qui produit un rapport complet du poste, en réutilisant toute la Partie II :

- Infos système (Ch.2) et espace disque (Ch.14)
- Services critiques et leur conformité (Ch.11)
- Comptes administrateurs locaux (Ch.10)
- Tâches planifiées non-Microsoft (Ch.13)
- Le tout structuré en PSCustomObject, exporté en CSV, avec un résumé coloré à l'écran, et robuste aux erreurs (`try/catch`, Ch.8)

C'est la version « poste local » de l'outil que tu enrichiras avec le réseau (Partie III) puis l'exécution distante (Partie VI).

---
