---
title: Chapitre 19 — Comprendre Active Directory
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### Qu'est-ce qu'Active Directory ?

**Active Directory (AD)** est l'annuaire centralisé d'un réseau Windows d'entreprise. Au lieu de gérer des comptes locaux sur chaque machine (Ch.10), on centralise **utilisateurs, ordinateurs, groupes** dans une base unique, administrée depuis les **contrôleurs de domaine**.

Concrètement, AD répond à : « qui es-tu (authentification), qu'as-tu le droit de faire (autorisation), et où es-tu rangé dans l'organisation ? ».

### Le vocabulaire indispensable

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

### Le Distinguished Name (DN) : l'adresse d'un objet

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

### Le module ActiveDirectory et RSAT

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

### Vérifier son environnement AD

```powershell
Get-ADDomain                     # infos sur le domaine courant
Get-ADForest                     # infos sur la forêt
Get-ADDomainController -Discover # trouver un contrôleur de domaine
```


`Get-ADDomain` renvoie notamment le `DistinguishedName` du domaine (`DC=lab,DC=local`) et le `DNSRoot` (`lab.local`) — pratiques pour construire des recherches (Ch.23).

## 🟡 Très utile en pratique

### AD vs comptes locaux : ne pas confondre

| | Comptes **locaux** (Ch.10) | **Active Directory** |
|---|---|---|
| Cmdlets | `*-LocalUser`, `*-LocalGroup` | `*-ADUser`, `*-ADGroup` |
| Portée | Une seule machine | Tout le domaine |
| Base | SAM locale | Base AD (sur les DC) |
| Quand ? | Poste isolé, compte technique local | Réseau d'entreprise |

C'est la même logique d'administration (lister, créer, modifier, désactiver), mais à l'échelle du domaine. Tes réflexes du Ch.10 se transposent directement.

### L'objet renvoyé par `Get-ADUser`

```powershell
Get-ADUser -Identity alice.martin | Get-Member
```


> **📌 Réflexe `Get-Member` :** un objet utilisateur AD a énormément d'attributs. Mais **par défaut, `Get-ADUser` n'en renvoie qu'une poignée** (nom, SamAccountName, DN, statut). Pour obtenir les autres (email, service, dernière connexion…), il faut le paramètre `-Properties` — un point crucial qu'on détaille au Ch.23.

## 🔴 Bonus

### La structure logique vs physique

AD a une structure **logique** (domaines, OU, objets — ce qu'on manipule ici) et une structure **physique** (sites, sous-réseaux, réplication entre DC). Ce cours ne traite que la partie logique via PowerShell ; la topologie physique relève d'un cours AD dédié.

## ❌ Erreur classique

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


## 💡 Exercices

**Guidé :** Sur ton lab, exécute `Get-ADDomain` et affiche le `DNSRoot` et le `DistinguishedName` du domaine. Puis `Get-ADDomainController -Discover` pour identifier ton DC.

**Autonome :** Prends le DN d'un utilisateur (`(Get-ADUser alice.martin).DistinguishedName`) et, avec `-split ","`, extrais uniquement la première OU dans laquelle il se trouve.

## ✅ Tu sais maintenant...

- Ce qu'est AD (annuaire central) et son vocabulaire (domaine, DC, forêt, OU, objet, attribut)
- Lire et comprendre un **Distinguished Name**
- Le module **ActiveDirectory** et **RSAT** (et le piège du module absent)
- La différence comptes locaux / comptes AD
- Que `Get-ADUser` ne renvoie que quelques attributs par défaut (d'où `-Properties`)

## 💬 Questions d'entretien typiques

- **Qu'est-ce qu'un contrôleur de domaine ?** → Un serveur qui héberge la base AD et authentifie les utilisateurs du domaine.
- **Qu'est-ce qu'un DN ?** → Le Distinguished Name, l'adresse unique d'un objet dans l'arborescence AD (`CN=...,OU=...,DC=...`).
- **Pourquoi `Get-ADUser` ne montre-t-il pas l'email ?** → Par défaut il ne renvoie qu'un jeu réduit d'attributs ; il faut `-Properties mail` (ou `-Properties *`) pour les autres.
- **Où trouve-t-on les cmdlets AD sur un poste client ?** → Il faut installer RSAT, puis `Import-Module ActiveDirectory`.

---
