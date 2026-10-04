---
title: Chapitre 10 — Outils d'administration et requêtage
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie III — Administration et contrôle
  - index.md
---

## 10.1 Les consoles natives

| Outil | Usage |
|---|---|
| **ADUC** (`dsa.msc`) | Utilisateurs, groupes, ordinateurs, OU, délégation |
| **ADAC** (Centre d'administration AD) | Interface moderne, corbeille AD, FGPP |
| **GPMC** (`gpmc.msc`) | Stratégies de groupe |
| **AD Sites and Services** (`dssite.msc`) | Sites, sous-réseaux, réplication |
| **AD Domains and Trusts** (`domain.msc`) | Trusts, niveaux fonctionnels |
| **DNS Manager** (`dnsmgmt.msc`) | Zones DNS intégrées |

Ces consoles s'installent sur un poste d'administration avec **RSAT** ; on n'administre pas en ouvrant une session sur le DC.

## 10.2 Le module PowerShell ActiveDirectory

| Cmdlet | Usage |
|---|---|
| `Get-ADUser` / `Set-ADUser` / `New-ADUser` | Comptes utilisateurs |
| `Get-ADGroup` / `Get-ADGroupMember` / `Add-ADGroupMember` | Groupes |
| `Get-ADComputer` | Ordinateurs |
| `Get-ADOrganizationalUnit` | OU |
| `Get-ADObject` | Tout objet, avec filtre LDAP |
| `Search-ADAccount` | Comptes inactifs, verrouillés, expirés |
| `Get-ADDomain` / `Get-ADForest` | Informations de domaine et de forêt |

Le module passe par **ADWS** (port 9389). La syntaxe de filtre utilise `-Filter` (syntaxe PowerShell) ou `-LDAPFilter` (syntaxe LDAP).

## 10.3 LDAP : la langue de l'annuaire

Une requête LDAP comporte :

| Élément | Rôle | Exemple |
|---|---|---|
| **Base DN** | Point de départ | `OU=Lyon,DC=meridian,DC=local` |
| **Scope** | Profondeur : `base`, `onelevel`, `subtree` | `subtree` |
| **Filtre** | Critères, en notation préfixée | `(&(objectClass=user)(adminCount=1))` |
| **Attributs** | Ce qu'on veut récupérer | `sAMAccountName, memberOf` |

Par défaut, **tout utilisateur authentifié peut lire l'essentiel de l'annuaire**. C'est nécessaire au fonctionnement (trouver un collègue, résoudre un groupe) et cela signifie qu'un simple compte du domaine voit la structure, les groupes et les attributs non confidentiels de tous les objets. La sécurité d'AD ne peut donc pas reposer sur le secret de sa configuration.

## 10.4 Requêtes d'hygiène

Les requêtes que tout administrateur devrait lancer régulièrement :

| Contrôle | Pourquoi |
|---|---|
| Comptes inactifs depuis plus de 90 jours | Identités abandonnées, toujours valides |
| Mots de passe qui n'expirent jamais | Secrets figés |
| Comptes utilisateurs portant un SPN | Comptes de service exposés à une attaque hors ligne (Ch.15) |
| Comptes sans pré-authentification Kerberos | Même risque (Ch.15) |
| Machines et comptes en délégation non contrainte | Exposition d'identités (Ch.6) |
| Comptes avec `adminCount = 1` | Inventaire des comptes privilégiés, actuels et anciens |
| Membres (récursifs) des groupes privilégiés | Le nombre de Domain Admins doit être minimal |
| Date du dernier changement de mot de passe de `krbtgt` | Doit être renouvelé régulièrement (Ch.28) |

Les commandes correspondantes sont regroupées dans l'Annexe A.

## 10.5 Outils d'audit

| Outil | Apport |
|---|---|
| **PingCastle** | Score de risque AD et recommandations priorisées ; rapport lisible par la direction |
| **Purple Knight** (Semperis) | Indicateurs d'exposition et de compromission |
| **BloodHound** | Graphe des relations et des chemins de privilèges (Ch.14) |
| **ADRecon** | Inventaire structuré exporté en tableur |

---
