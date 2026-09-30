---
title: PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY
source: IT/02_Windows/Powershell.md
note: PowerShell
chapter: 4
chapters: 8
---

> **🏗️ À ce stade, on entre dans l'administration d'infrastructure Windows.** Les parties précédentes s'appliquaient à un poste isolé. Active Directory est l'annuaire central d'un **réseau d'entreprise**. Pour pratiquer cette partie, il te faut l'environnement de lab décrit en début de cours : une **VM Windows Server** promue contrôleur de domaine, ou un poste avec **RSAT** connecté à un domaine.
>
> **⚠️ Pratique sur un lab, JAMAIS en production.** À partir d'ici, les exemples **créent, modifient, désactivent et suppriment** de vrais objets d'annuaire (comptes, groupes, OU). Une erreur sur un domaine de production peut désactiver des utilisateurs réels ou casser des accès. Tous les exercices et mini-projets de cette partie sont à réaliser exclusivement sur **ton domaine de lab** (`lab.local`), sur des objets de test. Applique systématiquement la discipline du cours : `Get`/`Test` avant d'agir, `-WhatIf` avant toute opération de masse.
>
> **Ce cours reste un cours PowerShell.** On apprend ici à *piloter* AD avec PowerShell — pas à concevoir une forêt, gérer la réplication, les niveaux fonctionnels ou les approbations. Pour ça, réfère-toi à un cours Active Directory dédié. Ici, AD est le **terrain** sur lequel on applique tout ce qu'on a appris : objets, pipeline, filtrage, boucles, CSV.

---


## Chapitre 19 — Comprendre Active Directory

### 🟢 Le minimum à savoir

#### Qu'est-ce qu'Active Directory ?

**Active Directory (AD)** est l'annuaire centralisé d'un réseau Windows d'entreprise. Au lieu de gérer des comptes locaux sur chaque machine (Ch.10), on centralise **utilisateurs, ordinateurs, groupes** dans une base unique, administrée depuis les **contrôleurs de domaine**.

Concrètement, AD répond à : « qui es-tu (authentification), qu'as-tu le droit de faire (autorisation), et où es-tu rangé dans l'organisation ? ».

#### Le vocabulaire indispensable

Avant toute cmdlet, il faut ces mots — sinon les commandes n'ont pas de sens :

| Terme | Ce que c'est |
|-------|-------------|
| **Domaine** | L'unité d'administration AD (ex : `lab.local`). Regroupe des objets partageant une base de sécurité commune |
| **Contrôleur de domaine (DC)** | Un serveur qui héberge la base AD et authentifie les utilisateurs |
| **Forêt** | L'ensemble de tous les domaines liés (le conteneur le plus haut) |
| **Objet** | Toute entité d'AD : un utilisateur, un ordinateur, un groupe… |
| **Utilisateur** | Un compte de connexion (`alice.martin`) |
| **Ordinateur** | Un compte machine (chaque PC/serveur membre du domaine en a un) |
| **Groupe** | Un ensemble d'utilisateurs/ordinateurs, pour attribuer des droits en bloc |
| **OU (Unité d'organisation)** | Un « dossier » qui range les objets (ex : `OU=IT`, `OU=Compta`). Sert à organiser **et** à cibler les GPO |
| **Attribut** | Une propriété d'un objet (nom, email, service, date de dernière connexion…) |

#### Le Distinguished Name (DN) : l'adresse d'un objet

Chaque objet AD a une **adresse unique**, son **DN** (Distinguished Name), qui décrit son emplacement dans l'arborescence, de l'objet jusqu'au domaine :

```
CN=Alice Martin,OU=IT,OU=Utilisateurs,DC=lab,DC=local
│                │     │              │
│                │     │              └─ le domaine lab.local (DC = Domain Component)
│                │     └─ rangé dans l'OU Utilisateurs
│                └─ puis dans l'OU IT
└─ l'objet lui-même (CN = Common Name)
```

On **lit** un DN de gauche (l'objet) à droite (le domaine). Tu n'as pas à le mémoriser ou le taper à la main : les cmdlets te le renvoient, et tu peux le **découper** avec les techniques de chaînes du Ch.5 (`-split ","`, `-match`) pour en extraire l'OU ou le domaine.

> **Rappel Ch.5 :** `"CN=Alice,OU=IT,DC=lab,DC=local" -split "," ` te donne un tableau `["CN=Alice", "OU=IT", "DC=lab", "DC=local"]`. C'est exactement là que les opérations de chaînes deviennent concrètes.

#### Le module ActiveDirectory et RSAT

Les cmdlets AD (`Get-ADUser`, `New-ADUser`…) viennent du module **ActiveDirectory**, qui n'est **pas** présent partout :

- Sur un **contrôleur de domaine** : présent d'office.
- Sur un **Windows Server membre** : via le rôle/outils AD.
- Sur un **Windows 10/11** : via **RSAT** (Remote Server Administration Tools), à installer.

```powershell
# Installer RSAT AD sur Windows 10/11                      [🔑 Admin]
Add-WindowsCapability -Online -Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"

# Charger le module
Import-Module ActiveDirectory

# Vérifier qu'il est disponible
Get-Module -ListAvailable ActiveDirectory
```

> **⚠️ Si `Get-ADUser` renvoie « terme non reconnu » :** le module n'est pas installé. Sur un poste client, installe RSAT (ci-dessus). C'est LE piège du débutant qui tape `Get-ADUser` sur son Windows 11 personnel sans domaine — comme prévenu en début de cours.

#### Vérifier son environnement AD

```powershell
Get-ADDomain                     # infos sur le domaine courant
Get-ADForest                     # infos sur la forêt
Get-ADDomainController -Discover # trouver un contrôleur de domaine
```

`Get-ADDomain` renvoie notamment le `DistinguishedName` du domaine (`DC=lab,DC=local`) et le `DNSRoot` (`lab.local`) — pratiques pour construire des recherches (Ch.23).

### 🟡 Très utile en pratique

#### AD vs comptes locaux : ne pas confondre

| | Comptes **locaux** (Ch.10) | **Active Directory** |
|---|---|---|
| Cmdlets | `*-LocalUser`, `*-LocalGroup` | `*-ADUser`, `*-ADGroup` |
| Portée | Une seule machine | Tout le domaine |
| Base | SAM locale | Base AD (sur les DC) |
| Quand ? | Poste isolé, compte technique local | Réseau d'entreprise |

C'est la même logique d'administration (lister, créer, modifier, désactiver), mais à l'échelle du domaine. Tes réflexes du Ch.10 se transposent directement.

#### L'objet renvoyé par `Get-ADUser`

```powershell
Get-ADUser -Identity alice.martin | Get-Member
```

> **📌 Réflexe `Get-Member` :** un objet utilisateur AD a énormément d'attributs. Mais **par défaut, `Get-ADUser` n'en renvoie qu'une poignée** (nom, SamAccountName, DN, statut). Pour obtenir les autres (email, service, dernière connexion…), il faut le paramètre `-Properties` — un point crucial qu'on détaille au Ch.23.

### 🔴 Bonus

#### La structure logique vs physique

AD a une structure **logique** (domaines, OU, objets — ce qu'on manipule ici) et une structure **physique** (sites, sous-réseaux, réplication entre DC). Ce cours ne traite que la partie logique via PowerShell ; la topologie physique relève d'un cours AD dédié.

### ❌ Erreur classique

```powershell
# Taper une cmdlet AD sans le module / sans domaine
Get-ADUser alice        # ❌ "terme non reconnu" si RSAT absent
Import-Module ActiveDirectory   # (après avoir installé RSAT)

# Croire qu'un compte local et un compte AD sont la même chose
Get-LocalUser alice     # compte LOCAL de la machine
Get-ADUser alice        # compte du DOMAINE — objets différents !

# Vouloir taper un DN à la main sans erreur
# → laisse les cmdlets te le fournir, découpe-le avec -split (Ch.5)
```

### 💡 Exercices

**Guidé :** Sur ton lab, exécute `Get-ADDomain` et affiche le `DNSRoot` et le `DistinguishedName` du domaine. Puis `Get-ADDomainController -Discover` pour identifier ton DC.

**Autonome :** Prends le DN d'un utilisateur (`(Get-ADUser alice.martin).DistinguishedName`) et, avec `-split ","`, extrais uniquement la première OU dans laquelle il se trouve.

### ✅ Tu sais maintenant...

- Ce qu'est AD (annuaire central) et son vocabulaire (domaine, DC, forêt, OU, objet, attribut)
- Lire et comprendre un **Distinguished Name**
- Le module **ActiveDirectory** et **RSAT** (et le piège du module absent)
- La différence comptes locaux / comptes AD
- Que `Get-ADUser` ne renvoie que quelques attributs par défaut (d'où `-Properties`)

### 💬 Questions d'entretien typiques

- **Qu'est-ce qu'un contrôleur de domaine ?** → Un serveur qui héberge la base AD et authentifie les utilisateurs du domaine.
- **Qu'est-ce qu'un DN ?** → Le Distinguished Name, l'adresse unique d'un objet dans l'arborescence AD (`CN=...,OU=...,DC=...`).
- **Pourquoi `Get-ADUser` ne montre-t-il pas l'email ?** → Par défaut il ne renvoie qu'un jeu réduit d'attributs ; il faut `-Properties mail` (ou `-Properties *`) pour les autres.
- **Où trouve-t-on les cmdlets AD sur un poste client ?** → Il faut installer RSAT, puis `Import-Module ActiveDirectory`.

---


## Chapitre 20 — Utilisateurs AD

### 🟢 Le minimum à savoir

#### Chercher un utilisateur : `Get-ADUser`

```powershell
# Par identité (SamAccountName, DN, SID, GUID)
Get-ADUser -Identity alice.martin

# Avec des attributs supplémentaires (rappel Ch.19 : sinon jeu réduit)
Get-ADUser -Identity alice.martin -Properties mail, Department, LastLogonDate

# Tous les utilisateurs (filtre obligatoire — voir Ch.23)
Get-ADUser -Filter *
```

Les attributs par défaut : `Name`, `SamAccountName`, `DistinguishedName`, `Enabled`, `UserPrincipalName`, `SID`, `GivenName`, `Surname`. Tout le reste (`mail`, `Department`, `Title`, `LastLogonDate`, `Manager`…) nécessite `-Properties`.

> **📌 Réflexe `Get-Member` :** `Get-ADUser alice.martin -Properties * | Get-Member` liste **tous** les attributs disponibles pour un utilisateur. Fais-le une fois pour découvrir ce que tu peux exploiter (souvent 100+ attributs).

#### Créer un utilisateur : `New-ADUser` `[🔑 Admin]`

**Discipline `Get` avant `New`** : on vérifie que le compte n'existe pas.

```powershell
if (-not (Get-ADUser -Filter "SamAccountName -eq 'jdupont'" -ErrorAction SilentlyContinue)) {

    $motDePasse = Read-Host "Mot de passe initial" -AsSecureString

    New-ADUser `
        -Name "Jean Dupont" `
        -GivenName "Jean" -Surname "Dupont" `
        -SamAccountName "jdupont" `
        -UserPrincipalName "jdupont@lab.local" `
        -Path "OU=IT,DC=lab,DC=local" `
        -AccountPassword $motDePasse `
        -Enabled $true `
        -ChangePasswordAtLogon $true
}
```

Points clés :
- `-SamAccountName` : l'identifiant de connexion (format court, `jdupont`)
- `-UserPrincipalName` : l'identifiant moderne (format email, `jdupont@lab.local`)
- `-Path` : le DN de l'OU où créer le compte
- `-AccountPassword` : un **SecureString** (jamais en clair — voir Ch.33)
- `-Enabled $true` : sinon le compte est créé désactivé
- `-ChangePasswordAtLogon $true` : bonne pratique pour un mot de passe initial

#### Modifier un utilisateur : `Set-ADUser` `[🔑 Admin]`

```powershell
Set-ADUser -Identity jdupont -EmailAddress "jean.dupont@lab.local" -Department "Informatique"
Set-ADUser -Identity jdupont -Title "Technicien" -Office "Bâtiment A"
```

#### Activer, désactiver, déverrouiller `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity jdupont      # désactiver (départ, suspension)
Enable-ADAccount  -Identity jdupont      # réactiver
Unlock-ADAccount  -Identity jdupont      # déverrouiller (après trop d'essais de mot de passe)
```

> **Verrouillé ≠ désactivé :** un compte **verrouillé** l'a été automatiquement (trop de mauvais mots de passe) — on le **déverrouille**. Un compte **désactivé** l'a été manuellement (départ…) — on le **réactive**. Deux situations différentes.

#### Réinitialiser un mot de passe `[🔑 Admin]`

```powershell
$nouveau = Read-Host "Nouveau mot de passe" -AsSecureString
Set-ADAccountPassword -Identity jdupont -NewPassword $nouveau -Reset
Set-ADUser -Identity jdupont -ChangePasswordAtLogon $true    # forcer le changement
```

#### Supprimer un utilisateur `[🔑 Admin]`

```powershell
Remove-ADUser -Identity jdupont -Confirm:$false
```

> **Bonne pratique (rappel Ch.10) :** on préfère souvent **désactiver et déplacer** un compte (départ d'un employé) plutôt que le supprimer d'emblée — pour conserver l'historique et pouvoir restaurer. La suppression vient après une période de rétention.

### 🟡 Très utile en pratique

#### Identifier les comptes à problème

```powershell
# Comptes désactivés
Get-ADUser -Filter "Enabled -eq '$false'" | Select-Object Name, SamAccountName

# Comptes verrouillés
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName

# Comptes dont le mot de passe n'expire jamais (point d'audit)
Get-ADUser -Filter "PasswordNeverExpires -eq '$true'" -Properties PasswordNeverExpires |
    Select-Object Name, SamAccountName
```

`Search-ADAccount` est un raccourci pratique pour les cas courants (`-LockedOut`, `-AccountDisabled`, `-AccountInactive`, `-PasswordExpired`).

#### La discipline Get → Set en action

```powershell
# 1. Regarder l'état actuel
Get-ADUser jdupont -Properties Department, Title | Select Department, Title

# 2. Modifier en connaissance de cause
Set-ADUser jdupont -Department "Support" -Title "Technicien N2"

# 3. Vérifier
Get-ADUser jdupont -Properties Department, Title | Select Department, Title
```

Ce triptyque lire → modifier → vérifier est la marque d'un administrateur rigoureux.

### 🔴 Bonus

#### Comptes inactifs depuis X jours

```powershell
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly |
    Select-Object Name, SamAccountName, LastLogonDate
```

> **⚠️ Nuance importante sur `LastLogonDate` :** cet attribut dérive de `lastLogonTimestamp`, qui n'est répliqué entre contrôleurs de domaine que périodiquement (par défaut avec une marge d'environ 9-14 jours). Il est donc **approximatif** : parfait pour repérer des comptes « globalement inactifs depuis des mois », mais **pas** pour savoir la dernière connexion exacte à la minute. Pour une précision fine, il faudrait interroger l'attribut `lastLogon` (non répliqué) sur **chaque** DC — beaucoup plus lourd. Pour l'audit courant, `LastLogonDate` suffit, en gardant sa marge d'erreur en tête.

### ❌ Erreur classique

```powershell
# Créer un compte sans -Enabled → compte inutilisable (désactivé)
New-ADUser -Name "X" -SamAccountName x -AccountPassword $p   # ⚠️ créé désactivé
New-ADUser ... -Enabled $true                                 # ✅

# Passer le mot de passe en clair
-AccountPassword "P@ssw0rd"          # ❌ refusé (attend un SecureString)
-AccountPassword (Read-Host -AsSecureString)   # ✅

# Confondre verrouillé et désactivé
Enable-ADAccount jdupont    # ❌ ne déverrouille pas un compte verrouillé
Unlock-ADAccount jdupont    # ✅ pour un compte verrouillé

# Se fier à LastLogonDate à la minute près
# → attribut approximatif (réplication différée)
```

### 💡 Exercices

**Guidé :** Affiche le nom, l'email et le service (`Department`) de `alice.martin` (pense à `-Properties`). Puis modifie son `Title` et vérifie le changement.

**Autonome :** Écris une fonction `New-LabUser` qui prend `-GivenName`, `-Surname` et `-OU`, construit le `SamAccountName` (première lettre du prénom + nom, en minuscules, via les méthodes de chaîne du Ch.5), vérifie l'absence du compte, puis le crée activé avec changement de mot de passe à la première connexion.

### ✅ Tu sais maintenant...

- Chercher (`Get-ADUser`, avec `-Properties`), créer (`New-ADUser`), modifier (`Set-ADUser`)
- Activer/désactiver (`Enable`/`Disable-ADAccount`), déverrouiller (`Unlock-ADAccount`)
- Réinitialiser un mot de passe (`Set-ADAccountPassword -Reset`)
- Repérer les comptes à problème (`Search-ADAccount`)
- La nuance sur `LastLogonDate` (approximatif, réplication différée)

### 💬 Questions d'entretien typiques

- **Différence entre un compte verrouillé et désactivé ?** → Verrouillé = automatique (trop de mauvais mots de passe), on déverrouille ; désactivé = manuel, on réactive.
- **Pourquoi un `New-ADUser` donne-t-il un compte inutilisable ?** → Souvent l'oubli de `-Enabled $true` (créé désactivé par défaut).
- **Peut-on se fier à `LastLogonDate` à la minute ?** → Non : dérivé de `lastLogonTimestamp`, répliqué avec une marge de plusieurs jours ; bon pour l'inactivité globale, pas pour l'exactitude.
- **Comment passer un mot de passe à `New-ADUser` ?** → Via un `SecureString` (`-AsSecureString`), jamais en clair.

---


## Chapitre 21 — Groupes AD

### 🟢 Le minimum à savoir

#### Pourquoi les groupes sont centraux

En administration, **on n'attribue jamais un droit à un utilisateur directement** — on l'attribue à un **groupe**, et on met l'utilisateur dans le groupe. Ainsi, gérer 500 personnes revient à gérer quelques dizaines de groupes. C'est le principe **AGDLP** (on met les comptes dans des groupes, les groupes dans des ressources), fondamental en sécurité Windows.

#### Chercher et lister des groupes

```powershell
Get-ADGroup -Identity "Comptables"
Get-ADGroup -Filter * | Select-Object Name, GroupScope, GroupCategory
Get-ADGroup -Filter "Name -like 'GG_*'"    # tous les groupes commençant par GG_
```

#### Voir les membres d'un groupe

```powershell
Get-ADGroupMember -Identity "Comptables" |
    Select-Object Name, SamAccountName, objectClass

# Membres récursifs (y compris via des groupes imbriqués)
Get-ADGroupMember -Identity "Comptables" -Recursive
```

> **📌 Réflexe `Get-Member` :** `Get-ADGroup Comptables -Properties * | Get-Member` montre les attributs d'un groupe (`GroupScope`, `GroupCategory`, `member`, `Description`, `ManagedBy`…).

#### Créer un groupe : `New-ADGroup` `[🔑 Admin]`

```powershell
New-ADGroup -Name "GG_Compta" `
    -SamAccountName "GG_Compta" `
    -GroupScope Global `
    -GroupCategory Security `
    -Path "OU=Groupes,DC=lab,DC=local" `
    -Description "Groupe global du service Comptabilité"
```

#### Ajouter et retirer des membres `[🔑 Admin]`

```powershell
Add-ADGroupMember    -Identity "GG_Compta" -Members jdupont, alice.martin
Remove-ADGroupMember -Identity "GG_Compta" -Members jdupont -Confirm:$false
```

#### Voir les groupes d'un utilisateur

```powershell
Get-ADPrincipalGroupMembership -Identity jdupont |
    Select-Object Name, GroupScope
```

C'est la question inverse : « de quels groupes cet utilisateur est-il membre ? » — essentielle pour comprendre ses droits.

### 🟡 Très utile en pratique

#### Catégorie : Sécurité vs Distribution

- **Security** (Sécurité) : sert à attribuer des **droits** (accès à un partage, à une ressource). C'est le cas courant en administration.
- **Distribution** : sert uniquement aux **listes de diffusion mail** (Exchange), pas aux droits.

En cas de doute pour donner des permissions : c'est un groupe **Security**.

#### Portée (Scope) : Domain Local, Global, Universal

La **portée** détermine qui peut être membre et où le groupe peut être utilisé. Pour un débutant, retiens la logique courante en domaine unique :

| Scope | Contient typiquement | Utilisé pour |
|-------|---------------------|--------------|
| **Global** | Des comptes du **même domaine** | Regrouper des utilisateurs par rôle/service (ex : `GG_Compta`) |
| **Domain Local** | Des groupes globaux | Attribuer un droit sur **une ressource** (ex : `DL_Partage_Compta_Modif`) |
| **Universal** | Des comptes/groupes de **toute la forêt** | Environnements multi-domaines |

> **Le modèle classique (AGDLP) :** on met les **A**ccounts dans un **G**lobal group (par rôle), ce groupe global dans un **D**omain **L**ocal group (par ressource), et c'est au Domain Local qu'on donne la **P**ermission. Ça paraît abstrait au début, mais c'est ce qui rend les droits maintenables à grande échelle. Pour un lab simple en domaine unique, on peut rester pragmatique, mais connaître ce modèle est attendu d'un administrateur.

#### Auditer l'appartenance à un groupe sensible

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

### 🔴 Bonus

#### Groupes imbriqués et appartenance récursive

Un groupe peut contenir d'autres groupes. `Get-ADGroupMember -Recursive` « aplatit » cette imbrication pour révéler tous les utilisateurs effectifs — indispensable pour comprendre les droits réels (un utilisateur peut être admin sans être membre *direct* du groupe admin).

### ❌ Erreur classique

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

### 💡 Exercices

**Guidé :** Crée un groupe global de sécurité `GG_Test`, ajoute-lui deux utilisateurs, liste ses membres, puis retire-en un.

**Autonome :** Écris un script qui prend un `-GroupName` et exporte en CSV tous ses membres récursifs (Name, SamAccountName, Type). Ajoute une colonne indiquant s'il s'agit d'un membre direct ou indirect.

### ✅ Tu sais maintenant...

- Pourquoi on attribue les droits via des **groupes**, jamais aux utilisateurs directement
- Chercher, créer des groupes, gérer leurs membres (`*-ADGroup`, `*-ADGroupMember`)
- Voir les groupes d'un utilisateur (`Get-ADPrincipalGroupMembership`)
- La différence **Security** / **Distribution** et les **portées** (Global/Domain Local/Universal)
- Auditer les groupes privilégiés (avec `-Recursive`)

### 💬 Questions d'entretien typiques

- **Pourquoi attribuer les droits à des groupes plutôt qu'à des utilisateurs ?** → Maintenabilité à l'échelle : on gère quelques groupes au lieu de milliers d'attributions individuelles.
- **Security ou Distribution pour donner un accès ?** → Security ; Distribution ne sert qu'aux listes de diffusion mail.
- **Pourquoi `-Recursive` sur un groupe admin ?** → Pour révéler les membres indirects (via groupes imbriqués), donc les droits réels.

---


## Chapitre 22 — Ordinateurs et unités d'organisation

### 🟢 Le minimum à savoir

#### Les comptes ordinateurs

Chaque machine jointe au domaine possède un **compte ordinateur** dans AD — comme les utilisateurs, mais pour les machines. On les gère avec `*-ADComputer`.

```powershell
Get-ADComputer -Identity "CLIENT01"
Get-ADComputer -Filter * | Select-Object Name, Enabled, OperatingSystem

# Avec des attributs utiles
Get-ADComputer -Filter * -Properties OperatingSystem, LastLogonDate |
    Select-Object Name, OperatingSystem, LastLogonDate
```

> **📌 Réflexe `Get-Member` :** `Get-ADComputer CLIENT01 -Properties * | Get-Member` révèle `OperatingSystem`, `OperatingSystemVersion`, `LastLogonDate`, `IPv4Address`, `Enabled`, `DistinguishedName`.

#### Le cas d'usage : inventaire du parc machines

```powershell
# Inventaire des OS présents dans le domaine
Get-ADComputer -Filter * -Properties OperatingSystem |
    Group-Object OperatingSystem |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```

`Group-Object` regroupe les machines par OS et les compte — un inventaire instantané, très parlant pour repérer des OS obsolètes (ex : Windows 7 encore présent).

#### Repérer les machines obsolètes ou inactives

```powershell
# Ordinateurs inactifs depuis 90 jours (rappel : LastLogonDate approximatif, Ch.20)
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -ComputersOnly |
    Select-Object Name, LastLogonDate
```

#### Désactiver / supprimer un compte ordinateur `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity "CLIENT01$"          # noter le $ pour un compte machine
Remove-ADComputer -Identity "CLIENT01" -Confirm:$false
```

> **Note :** le nom de compte machine se termine par `$` (ex : `CLIENT01$`). `Get-ADComputer` accepte le nom sans `$`, mais certaines opérations bas niveau l'exigent.

### 🟡 Les unités d'organisation (OU)

#### À quoi servent les OU

Une **OU** (Organizational Unit) est un conteneur qui **range** les objets AD. Elle a deux rôles majeurs :

1. **Organiser** : ranger les objets par service, site, type (`OU=IT`, `OU=Compta`, `OU=Serveurs`)
2. **Cibler les GPO** : on lie une stratégie de groupe à une OU pour l'appliquer à tous ses objets (Ch.25)

Ce deuxième rôle est fondamental : la structure d'OU **conditionne** l'application des GPO.

#### Lister et créer des OU `[🔑 Admin]`

```powershell
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName

New-ADOrganizationalUnit -Name "Comptabilité" -Path "OU=Services,DC=lab,DC=local"
```

> **Bonne pratique :** par défaut, une OU créée avec PowerShell est **protégée contre la suppression accidentelle** (`ProtectedFromAccidentalDeletion = $true`). C'est voulu : ça évite d'effacer d'un coup une OU pleine d'objets. Pour supprimer une OU, il faut d'abord retirer cette protection.

#### Déplacer un objet : `Move-ADObject` `[🔑 Admin]`

Déplacer un objet le range dans une autre OU — et donc change les GPO qui s'y appliquent :

```powershell
# Déplacer un utilisateur vers l'OU Comptabilité
$dn = (Get-ADUser jdupont).DistinguishedName
Move-ADObject -Identity $dn -TargetPath "OU=Comptabilité,OU=Services,DC=lab,DC=local"
```

> **Cas concret (départ d'un employé) :** on désactive le compte, puis on le **déplace** vers une OU « Départs » (souvent liée à une GPO restrictive). Déplacer + désactiver plutôt que supprimer, c'est la procédure propre.

### 🔴 Bonus

#### Retirer la protection avant suppression d'une OU

```powershell
Set-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" `
    -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" -Confirm:$false
```

### ❌ Erreur classique

```powershell
# Essayer de supprimer une OU protégée directement
Remove-ADOrganizationalUnit "OU=X,..."    # ❌ échoue si protégée
# → retirer d'abord ProtectedFromAccidentalDeletion (voir bonus)

# Oublier que déplacer un objet change les GPO appliquées
Move-ADObject ...    # ⚠️ conséquence : nouvelles stratégies, nouveaux droits

# Confondre le conteneur "Computers" (par défaut) et une vraie OU
# Les objets du conteneur CN=Computers ne reçoivent pas les GPO liées aux OU
```

### 💡 Exercices

**Guidé :** Fais l'inventaire des systèmes d'exploitation des ordinateurs du domaine avec `Group-Object`. Identifie le plus répandu.

**Autonome :** Crée une OU `OU=Test`, crée un utilisateur dedans, déplace-le vers une autre OU avec `Move-ADObject`, vérifie son nouveau DN, puis nettoie (retire la protection et supprime l'OU).

### ✅ Tu sais maintenant...

- Gérer les comptes ordinateurs (`*-ADComputer`) et inventorier le parc (`Group-Object` par OS)
- Repérer machines obsolètes/inactives
- Le rôle double des **OU** (organiser + cibler les GPO)
- Créer des OU, déplacer des objets (`Move-ADObject`) et l'impact sur les GPO
- La protection contre la suppression accidentelle

### 💬 Questions d'entretien typiques

- **À quoi sert une OU ?** → Ranger les objets AD et servir de cible aux GPO (la structure d'OU conditionne les stratégies appliquées).
- **Que se passe-t-il quand on déplace un objet d'OU ?** → Il reçoit les GPO liées à sa nouvelle OU — ses stratégies et droits peuvent changer.
- **Comment inventorier les OS du parc ?** → `Get-ADComputer -Properties OperatingSystem | Group-Object OperatingSystem`.
- **Pourquoi une OU ne se supprime-t-elle pas directement ?** → Protection contre la suppression accidentelle activée par défaut ; il faut la retirer d'abord.

---


## Chapitre 23 — Recherche et filtrage AD

### 🟢 Le minimum à savoir

#### Pourquoi ce chapitre est important

Un annuaire d'entreprise contient des milliers d'objets. Savoir **filtrer efficacement** est ce qui sépare un script qui met 10 minutes (et surcharge le DC) d'un script instantané. La clé : filtrer **côté serveur** avec `-Filter`, pas côté client avec `Where-Object`.

#### `-Filter` : le filtrage côté serveur

`-Filter` envoie la condition au contrôleur de domaine, qui ne renvoie **que** les objets correspondants. C'est rapide et économe.

```powershell
# Utilisateurs activés
Get-ADUser -Filter "Enabled -eq '$true'"

# Utilisateurs d'un service
Get-ADUser -Filter "Department -eq 'Comptabilité'" -Properties Department

# Recherche par motif
Get-ADUser -Filter "Surname -like 'Dup*'"

# Combiner des conditions
Get-ADUser -Filter "Enabled -eq '$true' -and Department -eq 'IT'" -Properties Department
```

> **Syntaxe du `-Filter` :** elle ressemble aux opérateurs PowerShell (`-eq`, `-like`, `-and`) mais s'écrit **entre guillemets** et suit des règles propres à AD. Les attributs utilisés dans le filtre doivent exister dans AD (ex : `Surname`, pas `Nom`).

#### `-Filter` vs `Where-Object` : la différence cruciale

```powershell
# ❌ LENT : récupère TOUS les utilisateurs, puis filtre côté client
Get-ADUser -Filter * -Properties Department | Where-Object { $_.Department -eq "IT" }

# ✅ RAPIDE : le DC ne renvoie que les utilisateurs IT
Get-ADUser -Filter "Department -eq 'IT'" -Properties Department
```

> **Règle d'or :** filtre **toujours** au plus près de la source. `-Filter` (côté serveur) d'abord ; `Where-Object` (côté client) seulement pour ce que `-Filter` ne sait pas faire (calculs complexes, propriétés dérivées). Sur un annuaire de 50 000 objets, la différence est spectaculaire.

#### `-SearchBase` : limiter la recherche à une OU

```powershell
# Ne chercher que dans l'OU IT
Get-ADUser -Filter * -SearchBase "OU=IT,DC=lab,DC=local"

# Combiner filtre et périmètre
Get-ADUser -Filter "Enabled -eq '$true'" -SearchBase "OU=Comptabilité,DC=lab,DC=local"
```

`-SearchBase` restreint la recherche à une branche de l'arbre — plus rapide et plus ciblé. `-SearchScope` affine (`Base`, `OneLevel`, `Subtree`).

#### `-Properties` : récupérer les bons attributs

Rappel (Ch.19-20) : par défaut, seul un jeu réduit d'attributs revient. `-Properties` charge ceux dont tu as besoin :

```powershell
Get-ADUser -Filter * -Properties mail, Department, LastLogonDate |
    Select-Object Name, mail, Department, LastLogonDate
```

> **Performance :** ne demande que les attributs nécessaires. `-Properties *` charge **tout** (100+ attributs par objet) — pratique pour explorer un seul objet, mais coûteux sur une recherche de masse. En production, liste explicitement les attributs voulus.

### 🟡 Très utile en pratique

#### Un rapport ciblé et performant

```powershell
# Comptes IT activés, avec leurs infos clés — filtré et projeté proprement
Get-ADUser -Filter "Enabled -eq '$true'" `
           -SearchBase "OU=IT,DC=lab,DC=local" `
           -Properties mail, Title, LastLogonDate |
    Select-Object Name, SamAccountName, mail, Title, LastLogonDate |
    Sort-Object Name |
    Export-Csv "C:\rapports\users_IT.csv" -NoTypeInformation -Encoding UTF8
```

Ce pipeline combine `-Filter` (serveur), `-SearchBase` (périmètre), `-Properties` (attributs), `Select-Object` (projection) et `Export-Csv` — le schéma type d'un rapport AD.

#### Compter par catégorie

```powershell
# Répartition des utilisateurs par service
Get-ADUser -Filter * -Properties Department |
    Group-Object Department |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```

### 🔴 Bonus

#### `Get-ADObject` : chercher tous types d'objets

Quand on ne sait pas si l'objet est un utilisateur, un groupe ou un ordinateur, `Get-ADObject` cherche par-delà les types :

```powershell
Get-ADObject -Filter "Name -like 'SRV*'" |
    Select-Object Name, ObjectClass, DistinguishedName
```

#### Filtres LDAP

Pour des recherches très pointues, `-LDAPFilter` accepte la syntaxe LDAP native :

```powershell
Get-ADUser -LDAPFilter "(&(objectCategory=user)(!(mail=*)))"    # utilisateurs sans email
```

Puissant mais plus aride — à réserver aux cas que `-Filter` ne couvre pas.

### ❌ Erreur classique

```powershell
# Tout ramener puis filtrer côté client (lent, surcharge le DC)
Get-ADUser -Filter * | Where-Object { $_.Department -eq "IT" }   # ❌
Get-ADUser -Filter "Department -eq 'IT'"                          # ✅

# Filtrer sur un attribut non chargé
Get-ADUser -Filter * | Where-Object { $_.mail -like "*@lab*" }    # ❌ mail non chargé → vide
Get-ADUser -Filter "mail -like '*@lab*'" -Properties mail         # ✅

# Utiliser -Properties * en masse
Get-ADUser -Filter * -Properties *    # ⚠️ très lourd sur un gros annuaire
Get-ADUser -Filter * -Properties mail, Department   # ✅ juste le nécessaire
```

### 💡 Exercices

**Guidé :** Liste les utilisateurs activés de l'OU IT avec leur email et leur `Title`, triés par nom, en utilisant `-Filter`, `-SearchBase` et `-Properties`.

**Autonome :** Produis un rapport CSV de la répartition des utilisateurs par service (`Department`), avec le compte par service, trié du plus grand au plus petit.

### ✅ Tu sais maintenant...

- Filtrer **côté serveur** avec `-Filter` (et pourquoi c'est bien plus rapide que `Where-Object`)
- Restreindre le périmètre avec `-SearchBase` / `-SearchScope`
- Charger les bons attributs avec `-Properties` (sans abuser de `*`)
- Construire des rapports AD performants (filtre → périmètre → attributs → projection → export)

### 💬 Questions d'entretien typiques

- **`-Filter` ou `Where-Object` en AD ?** → `-Filter` (côté serveur) chaque fois que possible : le DC ne renvoie que le nécessaire. `Where-Object` seulement pour ce que `-Filter` ne peut pas exprimer.
- **Pourquoi un attribut apparaît-il vide alors qu'il existe ?** → Il n'a pas été chargé ; il faut `-Properties <attribut>`.
- **À quoi sert `-SearchBase` ?** → Limiter la recherche à une OU précise, pour la rapidité et le ciblage.

---


## Chapitre 24 — Administration en masse avec CSV

### 🟢 Le minimum à savoir

#### L'objectif : l'onboarding automatisé

C'est le projet phare de la Partie IV, et un classique du métier : **créer des dizaines de comptes AD depuis un fichier CSV** (arrivée d'une promotion, d'un service entier…). Ce chapitre assemble presque tout le cours : `Import-Csv` (Ch.9), boucles (Ch.6), fonctions (Ch.7), gestion d'erreurs (Ch.8), création AD (Ch.20), groupes (Ch.21), OU (Ch.22).

#### Le flux complet

```
CSV utilisateurs
      ↓  Import-Csv
validation des données
      ↓  foreach
vérification d'existence (Get-ADUser)
      ↓
New-ADUser (-WhatIf d'abord !)
      ↓
Add-ADGroupMember (groupes)
      ↓
rapport CSV (succès / échecs)
```

#### Le fichier CSV de départ

```
GivenName,Surname,SamAccountName,Department,OU,Group
Jean,Dupont,jdupont,Comptabilité,"OU=Compta,DC=lab,DC=local",GG_Compta
Alice,Martin,amartin,IT,"OU=IT,DC=lab,DC=local",GG_IT
Sophie,Bernard,sbernard,IT,"OU=IT,DC=lab,DC=local",GG_IT
```

#### Lire et valider

```powershell
$utilisateurs = Import-Csv "C:\onboarding\nouveaux.csv" -Encoding UTF8

# Validation minimale : colonnes attendues présentes et non vides
foreach ($u in $utilisateurs) {
    if (-not $u.SamAccountName -or -not $u.OU) {
        Write-Warning "Ligne invalide ignorée : $($u.GivenName) $($u.Surname)"
        continue
    }
    # ... traitement ...
}
```

#### `-WhatIf` : simuler avant d'agir

> **📌 La discipline `Get`/`Test` culmine ici.** Avant de créer 50 comptes pour de vrai, on **simule** avec `-WhatIf`. La plupart des cmdlets de modification (`New-ADUser`, `Set-ADUser`, `Remove-*`, `Add-ADGroupMember`…) acceptent `-WhatIf`, qui affiche ce qui *serait* fait **sans rien faire**.

```powershell
New-ADUser -Name "Test" -SamAccountName test -Path "OU=IT,DC=lab,DC=local" -WhatIf
# → "What if: Performing the operation "New-ADUser" on target "CN=Test,OU=IT,...""
```

C'est le filet de sécurité indispensable pour toute opération de masse. On lance d'abord tout le script en `-WhatIf`, on vérifie la sortie, **puis** on retire le `-WhatIf`.

### 🟡 Le script d'onboarding complet

```powershell
# Invoke-Onboarding.ps1 — Création de comptes AD en masse depuis un CSV
# SÛR PAR DÉFAUT : le script SIMULE. Il faut le lancer avec -Execute pour créer réellement.
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [string]$CsvPath,
    [string]$ReportPath = "C:\onboarding\rapport_$(Get-Date -Format yyyyMMdd_HHmmss).csv",
    [switch]$Execute      # SANS ce switch, le script simule (ne crée rien)
)

Import-Module ActiveDirectory
Set-StrictMode -Version Latest

# Sûr par défaut : tant que -Execute n'est pas fourni, on force le mode simulation.
# -WhatIf:$true fait que tous les ShouldProcess n'affichent que ce qui SERAIT fait.
if (-not $Execute) {
    $WhatIfPreference = $true
    Write-Host "MODE SIMULATION (ajoute -Execute pour créer réellement les comptes)" -ForegroundColor Yellow
}

# --- Contrôles PRÉALABLES (Test avant d'agir) -------------------------------
# On vérifie l'environnement AVANT de créer le moindre compte : il serait absurde
# de créer 50 utilisateurs puis de planter au moment d'écrire le rapport.
if (-not (Test-Path $CsvPath -PathType Leaf)) {
    throw "CSV introuvable : $CsvPath"
}
$reportDir = Split-Path -Parent $ReportPath
if (-not (Test-Path $reportDir)) {
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
}

$utilisateurs = Import-Csv $CsvPath -Encoding UTF8
$resultats = [System.Collections.Generic.List[object]]::new()

# Fichier SÉPARÉ pour la remise des mots de passe initiaux (jamais dans le rapport principal).
# À protéger par ACL et à supprimer après distribution (voir note plus bas).
# On dérive son nom de celui du rapport : rapport_xxx.csv → rapport_xxx_secrets.csv
$secretsPath = Join-Path $reportDir `
    ("{0}_secrets.csv" -f [System.IO.Path]::GetFileNameWithoutExtension($ReportPath))
$secrets = [System.Collections.Generic.List[object]]::new()

# Générateur de mot de passe initial, AUTONOME pour ce chapitre.
# (Le Ch.33 montrera une version industrialisée : RNG cryptographique + garantie de complexité.)
function New-InitialPassword {
    param(
        # Validation du paramètre (rappel Ch.3) : en dessous de 8 caractères, un mot de
        # passe initial n'a pas de sens face à une politique de domaine.
        [ValidateRange(8, 128)]
        [int]$Length = 16
    )
    # Pour le lab : simple et lisible. Voir Ch.33 pour la version robuste (cryptographique).
    $maj = "ABCDEFGHJKLMNPQRSTUVWXYZ"; $min = "abcdefghijkmnpqrstuvwxyz"
    $chi = "23456789"; $sym = "!@#%*-_"

    # Garantit au moins un caractère de chaque catégorie (conformité AD, cf. Ch.33).
    # ATTENTION : on travaille avec un TABLEAU de caractères, pas des additions de chars.
    # En PowerShell, [char] + [char] fait une addition NUMÉRIQUE ('A' + 'b' donne 195),
    # pas une concaténation : on assemble donc un tableau et on le -join à la fin.
    $obligatoires = @(
        $maj[(Get-Random -Maximum $maj.Length)]
        $min[(Get-Random -Maximum $min.Length)]
        $chi[(Get-Random -Maximum $chi.Length)]
        $sym[(Get-Random -Maximum $sym.Length)]
    )
    $tout  = ($maj + $min + $chi + $sym).ToCharArray()

    # Garde explicite : NE PAS écrire directement 1..($Length - 4). Si la différence
    # vaut 0, PowerShell évalue 1..0 comme la plage DESCENDANTE @(1, 0) — soit deux
    # caractères de trop. La validation du paramètre seule ne protège pas de ça.
    $reste = @()
    if ($Length -gt $obligatoires.Count) {
        $reste = 1..($Length - $obligatoires.Count) | ForEach-Object { $tout | Get-Random }
    }

    # Mélange final (sinon les 4 premiers seraient toujours Maj/Min/Chiffre/Symbole)
    -join (($obligatoires + $reste) | Sort-Object { Get-Random })
}

foreach ($u in $utilisateurs) {

    $statut = "OK"; $detail = ""

    try {
        # 1. Validation des données du CSV
        if (-not $u.SamAccountName -or -not $u.OU) {
            throw "Données manquantes (SamAccountName ou OU)"
        }

        # 2. Vérifier l'existence du compte (Get avant New)
        $existe = Get-ADUser -Filter "SamAccountName -eq '$($u.SamAccountName)'" -ErrorAction SilentlyContinue
        if ($existe) { throw "Le compte existe déjà" }

        # 3. Vérifier les DÉPENDANCES AVANT de créer quoi que ce soit :
        #    une OU ou un groupe inexistant doit faire échouer AVANT la création,
        #    pas après (sinon on laisse un compte à moitié configuré).
        if (-not (Test-Path "AD:\$($u.OU)")) { throw "OU introuvable : $($u.OU)" }
        if ($u.Group -and -not (Get-ADGroup -Filter "Name -eq '$($u.Group)'" -ErrorAction SilentlyContinue)) {
            throw "Groupe introuvable : $($u.Group)"
        }

        # 4. Créer le compte. ShouldProcess respecte $WhatIfPreference :
        #    en simulation il n'exécute rien, il décrit seulement l'action.
        if ($PSCmdlet.ShouldProcess($u.SamAccountName, "Créer le compte AD")) {
            # Mot de passe initial aléatoire, généré en clair le temps de le poser sur le compte
            $pwdClair = New-InitialPassword
            $motDePasse = ConvertTo-SecureString $pwdClair -AsPlainText -Force
            New-ADUser `
                -Name "$($u.GivenName) $($u.Surname)" `
                -GivenName $u.GivenName -Surname $u.Surname `
                -SamAccountName $u.SamAccountName `
                -UserPrincipalName "$($u.SamAccountName)@lab.local" `
                -Department $u.Department `
                -Path $u.OU `
                -AccountPassword $motDePasse `
                -Enabled $true `
                -ChangePasswordAtLogon $true `
                -ErrorAction Stop

            # 5. Le compte EXISTE désormais → on enregistre IMMÉDIATEMENT son mot de passe.
            #    Si on attendait la fin, un échec à l'étape suivante ferait perdre
            #    la seule information permettant la première connexion.
            $secrets.Add([PSCustomObject]@{
                Utilisateur       = $u.SamAccountName
                MotDePasseInitial = $pwdClair
            })
            $statut = "CRÉÉ"

            # 6. Ajouter au groupe — traité À PART : un échec ici ne doit pas faire
            #    croire que le compte n'a pas été créé (il l'a été, et il est activé).
            if ($u.Group) {
                try {
                    Add-ADGroupMember -Identity $u.Group -Members $u.SamAccountName -ErrorAction Stop
                }
                catch {
                    $statut = "CRÉÉ_PARTIEL"
                    $detail = "Compte créé, mais ajout au groupe '$($u.Group)' échoué : $($_.Exception.Message)"
                }
            }
        }
        else {
            $statut = "SIMULÉ"     # ShouldProcess a refusé l'action (mode simulation)
        }
    }
    catch {
        # On n'arrive ici que si RIEN n'a été créé (validation ou New-ADUser en échec)
        $statut = "ÉCHEC"
        $detail = $_.Exception.Message
    }

    # 5. Journaliser le résultat (SANS le mot de passe)
    $resultats.Add([PSCustomObject]@{
        Utilisateur    = $u.SamAccountName
        Nom            = "$($u.GivenName) $($u.Surname)"
        OU             = $u.OU
        Groupe         = $u.Group
        Statut         = $statut
        Detail         = $detail
    })
}

# 6. Rapport principal (aucun secret dedans)
$resultats | Export-Csv $ReportPath -NoTypeInformation -Encoding UTF8
$resultats | Format-Table -AutoSize

# 6bis. Remise TEMPORAIRE des mots de passe initiaux (fichier séparé, accès restreint, à détruire)
if ($secrets.Count -gt 0) {
    $secrets | Export-Csv $secretsPath -NoTypeInformation -Encoding UTF8
    # Restreindre l'accès au SEUL créateur du fichier.
    #   /inheritance:r  → supprime les autorisations héritées du dossier parent
    #   *<SID>:(F)      → contrôle total pour ce compte, désigné par son SID
    # On cible par SID (préfixe *) et non par nom : cela lève toute ambiguïté entre
    # un compte de domaine DOMAINE\alice et un compte local alice.
    # Et (F) plutôt que (R) : le fichier doit pouvoir être SUPPRIMÉ après distribution.
    $identite = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    icacls $secretsPath /inheritance:r /grant:r "*$($identite.User.Value):(F)" | Out-Null
    Write-Host "Mots de passe initiaux : $secretsPath (À DISTRIBUER PUIS SUPPRIMER)" -ForegroundColor Yellow
}

$crees    = ($resultats | Where-Object Statut -eq "CRÉÉ").Count
$partiels = ($resultats | Where-Object Statut -eq "CRÉÉ_PARTIEL").Count
$simules  = ($resultats | Where-Object Statut -eq "SIMULÉ").Count
$ko       = ($resultats | Where-Object Statut -eq "ÉCHEC").Count
Write-Host "`nTerminé : $crees créé(s), $partiels partiel(s), $simules simulé(s), $ko échec(s). Rapport : $ReportPath" -ForegroundColor Cyan
if ($partiels -gt 0) {
    Write-Host "⚠️  $partiels compte(s) créé(s) mais incomplet(s) — voir la colonne Detail du rapport." -ForegroundColor Yellow
}
```

**Utilisation :**

```powershell
# 1. D'ABORD simuler — c'est le comportement PAR DÉFAUT (rien n'est créé)
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv

# 2. Vérifier la sortie (colonne Statut = SIMULÉ), PUIS exécuter réellement
.\Invoke-Onboarding.ps1 -CsvPath .\nouveaux.csv -Execute
```

> **⚠️ Sûr par défaut — le point le plus important de ce script.** Sans `-Execute`, le script **simule** (grâce à `$WhatIfPreference = $true` qui force tous les `ShouldProcess` en mode simulation) : la colonne `Statut` affiche `SIMULÉ` et **aucun compte n'est créé**. Il faut explicitement ajouter `-Execute` pour créer réellement. C'est exactement la philosophie du cours : on observe et on simule avant d'agir. (Tu peux aussi toujours ajouter `-WhatIf` manuellement, qui a le même effet.)

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré.

> **Note sur le mot de passe initial.** Le script est **autonome** : il définit sa propre fonction `New-InitialPassword` (pas de dépendance à un chapitre ultérieur), qui garantit au moins un caractère de chaque catégorie (majuscule, minuscule, chiffre, symbole) pour respecter la politique de complexité AD. Chaque compte reçoit un mot de passe **unique**. Ces mots de passe sont écrits dans un **fichier séparé** (`…secrets.csv`), **jamais dans le rapport principal**, avec un accès **restreint** (`icacls`) : c'est une **remise temporaire à accès restreint** — à distribuer aux utilisateurs, **puis à détruire**. Sans ça, on créerait des comptes… dont personne ne connaît le mot de passe pour la première connexion. (Le terme **stockage sécurisé** est réservé au coffre du Ch.33 : un CSV protégé par ACL n'en est pas un.)

> **🎯 Le vrai sujet d'administration : l'état « partiellement créé ».** Une opération en masse enchaîne plusieurs actions par utilisateur (créer le compte, l'ajouter à un groupe, …). Que se passe-t-il si la **deuxième** échoue ? Le compte existe déjà, activé, mais incomplet. Deux erreurs classiques :
> - Marquer l'utilisateur `ÉCHEC` : faux, et trompeur — au prochain lancement le script dira « le compte existe déjà », et personne ne saura qu'il faut finir le travail.
> - Perdre le mot de passe initial parce qu'on ne l'enregistrait qu'à la toute fin.
>
> Le script traite les deux : il **valide les dépendances (OU, groupe) AVANT** de créer quoi que ce soit — c'est le plus efficace, la plupart des échecs disparaissent —, il **enregistre le mot de passe dès que le compte existe**, et il isole l'ajout au groupe dans son propre `try/catch` pour produire un statut `CRÉÉ_PARTIEL` explicite. On préfère ici un **état honnête et rattrapable** à un rollback automatique (supprimer le compte qu'on vient de créer), plus risqué et plus complexe.
>
> **➡️ Renvoi Ch.33 :** cette gestion reste rudimentaire (fichier à accès restreint). Le Ch.33 l'industrialise : générateur **cryptographique** (`RandomNumberGenerator` plutôt que `Get-Random`) et surtout stockage des secrets dans un **coffre** (SecretManagement/SecretStore) plutôt qu'un fichier plat.

Ce script incarne tout le cours : paramètres, `CmdletBinding`/`ShouldProcess`, `Import-Csv`, boucle, validation, `try/catch`, `Get` avant `New`, création AD, groupes, liste d'objets, rapport CSV, résumé coloré, et remise sécurisée des secrets.

### 🔴 Bonus

#### Générer un SamAccountName automatiquement

Si le CSV ne fournit pas le `SamAccountName`, on le construit (rappel des méthodes de chaîne, Ch.5) :

```powershell
$sam = ($u.GivenName.Substring(0,1) + $u.Surname).ToLower() -replace '[^a-z]', ''
# Jean Dupont → "jdupont"
```

#### Gérer les doublons de SamAccountName

Deux « Jean Dupont » donneraient le même `jdupont`. On teste et on incrémente :

```powershell
$base = $sam; $i = 1
while (Get-ADUser -Filter "SamAccountName -eq '$sam'" -ErrorAction SilentlyContinue) {
    $sam = "$base$i"; $i++
}
```

### ❌ Erreur classique

```powershell
# Bien comprendre le mode par défaut : SANS -Execute, le script SIMULE
.\Invoke-Onboarding.ps1 -CsvPath x.csv             # ✅ SIMULATION (rien n'est créé)
# Le point réellement sensible, c'est l'exécution :
.\Invoke-Onboarding.ps1 -CsvPath x.csv -Execute    # ⚠️ crée réellement les comptes
# → toujours avoir relu la sortie de la simulation AVANT d'ajouter -Execute

# Pas de try/catch → une ligne en erreur arrête tout le lot
foreach ($u in $users) { New-ADUser ... }   # ❌ un échec = tout s'arrête
# ✅ try/catch par utilisateur : on isole les échecs, on continue

# Pas de rapport → impossible de savoir ce qui a réussi/échoué
# ✅ toujours produire un rapport CSV succès/échecs

# Encodage CSV oublié → prénoms accentués cassés
Import-Csv x.csv                    # ⚠️
Import-Csv x.csv -Encoding UTF8     # ✅
```

### 💡 Exercices

**Guidé :** Crée un petit CSV de 3 utilisateurs et lance le script d'onboarding **sans `-Execute`** (mode simulation par défaut). Vérifie que la colonne `Statut` affiche `SIMULÉ` et qu'aucun compte n'est créé. Relance ensuite avec `-Execute` (sur ton lab uniquement).

**Autonome :** Ajoute au script une colonne CSV `Title` et fais en sorte qu'elle soit appliquée (`-Title`). Ajoute aussi la génération automatique du `SamAccountName` avec gestion des doublons (bonus ci-dessus).

### 🧩 Capstone Partie IV — Suite d'onboarding/offboarding

Construis deux scripts complémentaires :

1. **`Invoke-Onboarding.ps1`** (ci-dessus) : création en masse depuis CSV, avec `-WhatIf`, gestion d'erreurs par ligne, et rapport.
2. **`Invoke-Offboarding.ps1`** : pour une liste de `SamAccountName`, **désactive** le compte, le **déplace** vers `OU=Départs`, retire ses groupes, et produit un rapport. Applique la discipline `Get` avant modification et `-WhatIf`.

Ensemble, ils forment un vrai outil de gestion du cycle de vie des comptes — le genre de livrable attendu d'un administrateur junior.

### ✅ Tu sais maintenant...

- Automatiser la création de comptes AD depuis un CSV (`Import-Csv` + boucle + `New-ADUser`)
- **Simuler avec `-WhatIf`** avant toute opération de masse (la discipline poussée à son maximum)
- Isoler les erreurs par ligne (`try/catch`) pour ne pas casser tout le lot
- Produire un rapport de succès/échecs
- Assembler tout le cours dans un livrable professionnel

### 💬 Questions d'entretien typiques

- **Comment créer 100 comptes AD depuis un fichier ?** → `Import-Csv`, une boucle `foreach`, `New-ADUser` par ligne, avec validation, `try/catch` et rapport.
- **Pourquoi `-WhatIf` est-il crucial en masse ?** → Il simule l'opération sans l'exécuter : on vérifie ce qui *serait* fait avant de le faire réellement.
- **Comment éviter qu'une ligne en erreur arrête tout ?** → Encadrer chaque itération d'un `try/catch` pour isoler l'échec et poursuivre le lot.

---
