---
title: Chapitre 28 — File Server et partages SMB
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie V — GPO et services Windows server
  - index.md
---

## 🟢 Le minimum à savoir

### Le partage de fichiers en réseau

**SMB** (Server Message Block) est le protocole de partage de fichiers de Windows. Un **partage** (share) expose un dossier du serveur sur le réseau, accessible via `\\serveur\partage`. On gère tout ça avec le module **SmbShare**.

```powershell
Get-SmbShare                          # les partages du serveur
Get-SmbShare -Name "Compta"           # un partage précis
```


> **📌 Réflexe `Get-Member` :** `Get-SmbShare | Get-Member` révèle `Name`, `Path`, `Description`, `EncryptData`. Un partage relie un **nom réseau** à un **chemin local**.

### Créer un partage `[🔑 Admin]`

```powershell
New-SmbShare -Name "Compta" -Path "C:\Partages\Compta" `
    -Description "Dossier du service Comptabilité" `
    -FullAccess "lab\Administrateurs" `
    -ChangeAccess "lab\GG_Compta" `
    -ReadAccess "lab\GG_Consultants"
```


### LE point crucial : permissions de partage vs permissions NTFS

> **⚠️ La confusion n°1 en administration de fichiers.** Il existe **deux couches de permissions** distinctes qui se cumulent, et c'est **la plus restrictive des deux qui gagne** :
>
> 1. **Permissions de partage (SMB)** : s'appliquent quand on accède via le réseau (`\\serveur\partage`). Gérées par `Grant-SmbShareAccess`. Grossières (FullAccess / ChangeAccess / ReadAccess).
> 2. **Permissions NTFS** (Ch.9, `Get-Acl`/`Set-Acl`) : s'appliquent **toujours** (réseau ET local). Fines (par fichier/dossier, nombreux droits).
>
> **L'accès effectif = l'intersection des deux.** Si le partage autorise `Change` mais que NTFS n'autorise que `Read`, l'utilisateur n'aura que `Read`. Et inversement.

```powershell
# Permissions de PARTAGE (couche SMB)
Get-SmbShareAccess -Name "Compta"
Grant-SmbShareAccess -Name "Compta" -AccountName "lab\GG_Compta" -AccessRight Change -Force

# Permissions NTFS (couche fichiers — rappel Ch.9)
Get-Acl "C:\Partages\Compta" | Select-Object -ExpandProperty Access
```


> **Une approche courante (à comprendre, pas à appliquer aveuglément) :** beaucoup d'administrateurs mettent les permissions de partage **assez larges** et gèrent la **finesse au niveau NTFS** uniquement, pour éviter de raisonner sur deux couches en parallèle. Attention toutefois : « large » ne veut pas dire `Full Control` pour tout le monde. Donner `Full Control` en partage inclut le droit de **modifier les permissions**, ce qui est excessif ; on se limite en général à `Change` pour les groupes qui écrivent, et l'on s'appuie sur NTFS pour le détail. Le point à retenir : il faut **comprendre les deux couches** pour diagnostiquer un « je ne peux pas écrire alors que j'ai les droits » — le choix de simplifier côté partage est un compromis d'exploitation, pas une règle absolue.

### Voir qui est connecté

```powershell
Get-SmbSession                        # sessions SMB ouvertes (qui est connecté ?)
Get-SmbOpenFile                       # fichiers actuellement ouverts via le réseau
```


Utile avant une maintenance (« qui utilise ce partage là maintenant ? ») ou pour diagnostiquer un fichier verrouillé.

## 🟡 Très utile en pratique

### Diagnostiquer « je n'ai pas accès »

La séquence de dépannage type, qui combine les deux couches :

```powershell
# 1. Le partage existe et quelles permissions SMB ?
Get-SmbShare -Name "Compta"
Get-SmbShareAccess -Name "Compta"

# 2. Quelles permissions NTFS sur le dossier ? (Ch.9)
(Get-Acl "C:\Partages\Compta").Access |
    Select-Object IdentityReference, FileSystemRights, AccessControlType

# 3. L'utilisateur est-il dans le bon groupe ? (Ch.21)
Get-ADGroupMember "GG_Compta" | Where-Object SamAccountName -eq "jdupont"
```


Ce diagnostic croise SMB (ce chapitre), NTFS (Ch.9) et les groupes AD (Ch.21) — une vraie synthèse d'administration.

### Fermer une session ou un fichier bloqué

```powershell
# Fermer un fichier ouvert (avant maintenance) — force la fermeture côté serveur
Close-SmbOpenFile -FileId <id> -Force

# Fermer une session
Close-SmbSession -SessionId <id> -Force
```


## 🔴 Bonus

### Partages administratifs cachés

Windows crée des partages cachés (suffixés `$` : `C$`, `ADMIN$`) réservés aux administrateurs. Ils n'apparaissent pas en navigation réseau mais sont accessibles via `\\serveur\C$` :

```powershell
Get-SmbShare | Where-Object Name -like "*$"    # les partages administratifs
```


> **Sécurité :** ces partages administratifs sont utiles pour l'administration distante, mais aussi exploités par les attaquants pour se déplacer latéralement. Leur usage est surveillé en sécurité (Ch.34).

## ❌ Erreur classique

```powershell
# Ne raisonner que sur une seule couche de permissions
# ❌ "j'ai mis Full en partage mais l'utilisateur ne peut pas écrire"
# → vérifier AUSSI les permissions NTFS (l'intersection gagne)

# Créer un partage sans restreindre l'accès
New-SmbShare -Name "X" -Path "C:\X" -FullAccess "Tout le monde"   # ❌ trop ouvert
New-SmbShare -Name "X" -Path "C:\X" -ChangeAccess "lab\GG_X"       # ✅ par groupe

# Supprimer un partage occupé sans prévenir
Remove-SmbShare -Name "Compta"    # ⚠️ vérifier Get-SmbSession avant
```


## 💡 Exercices

**Guidé :** Liste les partages du serveur (hors partages administratifs `$`), avec leur chemin et leur description. Affiche les permissions SMB de l'un d'eux.

**Autonome :** Écris un script qui, pour un partage donné, affiche côte à côte ses permissions SMB (`Get-SmbShareAccess`) et NTFS (`Get-Acl`), pour visualiser les deux couches d'un coup.

## 🧩 Capstone Partie V — Rapport d'infrastructure

Construis `Get-InfraReport.ps1` (à exécuter sur le serveur) qui produit un état des lieux :

- Les GPO du domaine et leurs liens (Ch.25)
- Les zones DNS et le nombre d'enregistrements A (Ch.26)
- Les scopes DHCP et leur taux d'utilisation (Ch.27)
- Les partages SMB et leurs permissions (Ch.28)
- Le tout en sections claires, exporté en CSV (un fichier par domaine) ou en rapport HTML

C'est le type de livrable qu'un administrateur produit pour documenter une infrastructure.

## ✅ Tu sais maintenant...

- Créer et gérer des partages SMB (`*-SmbShare`)
- **La distinction cruciale permissions de partage (SMB) vs NTFS**, et que la plus restrictive gagne
- Voir les sessions et fichiers ouverts (`Get-SmbSession`, `Get-SmbOpenFile`)
- Diagnostiquer un problème d'accès en croisant SMB, NTFS et groupes AD
- Les partages administratifs cachés (`C$`, `ADMIN$`)

## 💬 Questions d'entretien typiques

- **Quelle est la différence entre permissions de partage et NTFS ?** → Le partage (SMB) ne s'applique qu'en accès réseau et reste grossier ; NTFS s'applique toujours et est fin. L'accès effectif est l'intersection (la plus restrictive gagne).
- **Un utilisateur a Full en partage mais ne peut pas écrire, pourquoi ?** → Les permissions NTFS sont probablement plus restrictives ; c'est l'intersection qui compte.
- **Comment savoir qui utilise un partage avant une maintenance ?** → `Get-SmbSession` et `Get-SmbOpenFile`.

---
