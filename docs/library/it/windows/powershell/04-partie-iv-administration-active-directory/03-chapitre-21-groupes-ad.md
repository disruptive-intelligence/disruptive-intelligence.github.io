---
title: Chapitre 21 — Groupes AD
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### Pourquoi les groupes sont centraux

En administration, **on n'attribue jamais un droit à un utilisateur directement** — on l'attribue à un **groupe**, et on met l'utilisateur dans le groupe. Ainsi, gérer 500 personnes revient à gérer quelques dizaines de groupes. C'est le principe **AGDLP** (on met les comptes dans des groupes, les groupes dans des ressources), fondamental en sécurité Windows.

### Chercher et lister des groupes

```powershell
Get-ADGroup -Identity "Comptables"
Get-ADGroup -Filter * | Select-Object Name, GroupScope, GroupCategory
Get-ADGroup -Filter "Name -like 'GG_*'"    # tous les groupes commençant par GG_
```


### Voir les membres d'un groupe

```powershell
Get-ADGroupMember -Identity "Comptables" |
    Select-Object Name, SamAccountName, objectClass

# Membres récursifs (y compris via des groupes imbriqués)
Get-ADGroupMember -Identity "Comptables" -Recursive
```


> **📌 Réflexe `Get-Member` :** `Get-ADGroup Comptables -Properties * | Get-Member` montre les attributs d'un groupe (`GroupScope`, `GroupCategory`, `member`, `Description`, `ManagedBy`…).

### Créer un groupe : `New-ADGroup` `[🔑 Admin]`

```powershell
New-ADGroup -Name "GG_Compta" `
    -SamAccountName "GG_Compta" `
    -GroupScope Global `
    -GroupCategory Security `
    -Path "OU=Groupes,DC=lab,DC=local" `
    -Description "Groupe global du service Comptabilité"
```


### Ajouter et retirer des membres `[🔑 Admin]`

```powershell
Add-ADGroupMember    -Identity "GG_Compta" -Members jdupont, alice.martin
Remove-ADGroupMember -Identity "GG_Compta" -Members jdupont -Confirm:$false
```


### Voir les groupes d'un utilisateur

```powershell
Get-ADPrincipalGroupMembership -Identity jdupont |
    Select-Object Name, GroupScope
```


C'est la question inverse : « de quels groupes cet utilisateur est-il membre ? » — essentielle pour comprendre ses droits.

## 🟡 Très utile en pratique

### Catégorie : Sécurité vs Distribution

- **Security** (Sécurité) : sert à attribuer des **droits** (accès à un partage, à une ressource). C'est le cas courant en administration.
- **Distribution** : sert uniquement aux **listes de diffusion mail** (Exchange), pas aux droits.

En cas de doute pour donner des permissions : c'est un groupe **Security**.

### Portée (Scope) : Domain Local, Global, Universal

La **portée** détermine qui peut être membre et où le groupe peut être utilisé. Pour un débutant, retiens la logique courante en domaine unique :

| Scope | Contient typiquement | Utilisé pour |
|-------|---------------------|--------------|
| **Global** | Des comptes du **même domaine** | Regrouper des utilisateurs par rôle/service (ex : `GG_Compta`) |
| **Domain Local** | Des groupes globaux | Attribuer un droit sur **une ressource** (ex : `DL_Partage_Compta_Modif`) |
| **Universal** | Des comptes/groupes de **toute la forêt** | Environnements multi-domaines |

> **Le modèle classique (AGDLP) :** on met les **A**ccounts dans un **G**lobal group (par rôle), ce groupe global dans un **D**omain **L**ocal group (par ressource), et c'est au Domain Local qu'on donne la **P**ermission. Ça paraît abstrait au début, mais c'est ce qui rend les droits maintenables à grande échelle. Pour un lab simple en domaine unique, on peut rester pragmatique, mais connaître ce modèle est attendu d'un administrateur.

### Auditer l'appartenance à un groupe sensible

```powershell
# Qui est Admin du domaine ? (groupe le plus sensible qui soit)
Get-ADGroupMember -Identity "Admins du domaine" -Recursive |
    Select-Object Name, SamAccountName, objectClass
```


> **Sécurité :** l'appartenance aux groupes privilégiés (`Admins du domaine` / `Domain Admins`, `Administrateurs de l'entreprise` / `Enterprise Admins`) doit être **minimale et auditée**. Chaque membre est une cible de choix pour un attaquant. Ce contrôle est un incontournable de la sécurité AD.

> **Note langue (même principe qu'au Ch.10).** Ces noms **dépendent de la langue du domaine** : `Admins du domaine` en français, `Domain Admins` en anglais. Un script qui cible ces groupes par leur nom cassera sur un annuaire dans une autre langue. Pour être portable, on cible par **SID**, dont le suffixe (le *RID*) est fixe : `-512` pour les administrateurs du domaine, `-519` pour les administrateurs de l'entreprise.
> ```powershell
> $domainSID = (Get-ADDomain).DomainSID.Value
> $admins = Get-ADGroup -Identity "$domainSID-512"    # "Admins du domaine" / "Domain Admins"
> Get-ADGroupMember -Identity $admins -Recursive | Select-Object Name, SamAccountName
> ```

## 🔴 Bonus

### Groupes imbriqués et appartenance récursive

Un groupe peut contenir d'autres groupes. `Get-ADGroupMember -Recursive` « aplatit » cette imbrication pour révéler tous les utilisateurs effectifs — indispensable pour comprendre les droits réels (un utilisateur peut être admin sans être membre *direct* du groupe admin).

## ❌ Erreur classique

```powershell
# Donner un droit à un utilisateur au lieu d'un groupe
# ❌ ingérable à l'échelle → toujours passer par un groupe

# Créer un groupe Distribution pour gérer des droits
New-ADGroup ... -GroupCategory Distribution   # ❌ ne porte pas de droits
New-ADGroup ... -GroupCategory Security        # ✅

# Oublier -Recursive et rater des membres indirects
Get-ADGroupMember "Admins du domaine"             # ⚠️ membres directs seulement
Get-ADGroupMember "Admins du domaine" -Recursive  # ✅ tous les membres effectifs
```


## 💡 Exercices

**Guidé :** Crée un groupe global de sécurité `GG_Test`, ajoute-lui deux utilisateurs, liste ses membres, puis retire-en un.

**Autonome :** Écris un script qui prend un `-GroupName` et exporte en CSV tous ses membres récursifs (Name, SamAccountName, Type). Ajoute une colonne indiquant s'il s'agit d'un membre direct ou indirect.

## ✅ Tu sais maintenant...

- Pourquoi on attribue les droits via des **groupes**, jamais aux utilisateurs directement
- Chercher, créer des groupes, gérer leurs membres (`*-ADGroup`, `*-ADGroupMember`)
- Voir les groupes d'un utilisateur (`Get-ADPrincipalGroupMembership`)
- La différence **Security** / **Distribution** et les **portées** (Global/Domain Local/Universal)
- Auditer les groupes privilégiés (avec `-Recursive`)

## 💬 Questions d'entretien typiques

- **Pourquoi attribuer les droits à des groupes plutôt qu'à des utilisateurs ?** → Maintenabilité à l'échelle : on gère quelques groupes au lieu de milliers d'attributions individuelles.
- **Security ou Distribution pour donner un accès ?** → Security ; Distribution ne sert qu'aux listes de diffusion mail.
- **Pourquoi `-Recursive` sur un groupe admin ?** → Pour révéler les membres indirects (via groupes imbriqués), donc les droits réels.

---
