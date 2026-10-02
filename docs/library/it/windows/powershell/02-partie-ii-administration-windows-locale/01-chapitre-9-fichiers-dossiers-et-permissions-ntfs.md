---
title: Chapitre 9 — Fichiers, dossiers et permissions NTFS
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration Windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### Lister et explorer

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

### Lire et écrire du contenu

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

### Manipuler les chemins

```powershell
Join-Path C:\Scripts "logs\run.log"       # construit "C:\Scripts\logs\run.log"
Split-Path C:\Scripts\run.ps1 -Leaf        # "run.ps1"
Split-Path C:\Scripts\run.ps1 -Parent      # "C:\Scripts"
Test-Path C:\Scripts                        # le chemin existe ? (True/False)
Test-Path C:\Scripts -PathType Container    # est-ce un dossier ?
```


> **Bonne pratique :** construis toujours tes chemins avec `Join-Path` plutôt qu'en collant des chaînes avec `\`. Ça évite les doubles `\\` ou les séparateurs manquants, et reste correct quel que soit le contexte.

### Créer, copier, déplacer, supprimer

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

## 🟡 Très utile en pratique

### CSV et JSON natifs (rappel et approfondissement)

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

### Les permissions NTFS : `Get-Acl` / `Set-Acl`

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

## 🔴 Bonus

### Rechercher dans des fichiers : `Select-String`

L'équivalent de `grep` :

```powershell
Select-String -Path C:\Logs\*.log -Pattern "ERROR"          # lignes contenant ERROR
Select-String -Path C:\Logs\*.log -Pattern "fail" -Context 2  # avec 2 lignes de contexte
```


Renvoie des objets `MatchInfo` (fichier, numéro de ligne, ligne) — donc filtrables et exploitables.

### Prendre possession d'un dossier

Si tu n'as plus accès à un dossier, `takeown` (exécutable) puis `Set-Acl` permettent de reprendre la main — opération sensible, réservée aux cas de récupération, en `[🔑 Admin]`.

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Écris un script qui liste les fichiers d'un dossier (paramètre `-Path`) de plus de 100 Mo, triés par taille décroissante, avec nom et taille en Mo (propriété calculée).

**Autonome :** Écris un script qui affiche les ACE d'un dossier (`-Path`) sous forme de tableau lisible : qui (`IdentityReference`), quel droit (`FileSystemRights`), Allow/Deny, hérité ou non.

## 🧩 Mini-projet — Inventaire de dossier

Crée `Get-FolderReport.ps1` (paramètre `-Path`, `-OutputPath`) qui parcourt un dossier, produit un PSCustomObject par fichier (Nom, Extension, TailleMo, ModifieLe), exporte en CSV, et affiche un résumé (nombre de fichiers, taille totale, plus gros fichier). Réutilise pipeline, propriétés calculées, `Measure-Object` et `Export-Csv`.

## ✅ Tu sais maintenant...

- Explorer et manipuler fichiers/dossiers (`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`)
- Construire des chemins proprement (`Join-Path`, `Split-Path`, `Test-Path`)
- **Toujours** préciser `-Encoding UTF8` (piège 5.1 vs 7)
- Lire et exporter CSV/JSON nativement
- Lire les permissions NTFS avec `Get-Acl` (ACL, ACE, Allow/Deny, héritage, propriétaire) et la prudence requise pour `Set-Acl`

## 💬 Questions d'entretien typiques

- **Pourquoi toujours mettre `-Encoding UTF8` ?** → Parce que le défaut varie (5.1 ≠ 7) et casse les accents ; UTF-8 explicite rend le résultat portable.
- **Qu'est-ce qu'une ACE ?** → Une entrée d'ACL : un couple (identité, droit) en Allow ou Deny, hérité ou explicite.
- **Comment modifier des permissions sans risque ?** → Sauvegarder l'ACL (`Get-Acl | Export-Clixml`), travailler par groupes, tester sur un bac à sable, puis `Set-Acl`.

---
