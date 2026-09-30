---
title: Chapitre 1 — Active Directory
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie I — Fondations
  - index.md
---

pourquoi c'est partout et pourquoi c'est la cible n°1

Active Directory est un service d'annuaire Microsoft utilisé pour centraliser la gestion des identités, groupes, ordinateurs et ressources dans un environnement Windows.
## 1.1 Le problème que résout Active Directory

Imaginez une entreprise de 5 000 employés. Chaque employé a un PC, un compte email, des accès à des partages réseau, des applications métier. Sans système centralisé, il faudrait créer et gérer chaque compte sur chaque machine individuellement. Active Directory résout ce problème : c'est un service d'annuaire centralisé qui stocke et gère toutes les identités (utilisateurs, ordinateurs, services) et les politiques de sécurité d'une organisation. Un employé se connecte une fois avec son compte AD, et il accède à tout ce à quoi il a droit : c'est le Single Sign-On (SSO). AD est développé par Microsoft et intégré à Windows Server depuis 2000. Il est présent dans plus de 90 % des entreprises dans le monde.

## 1.2 Pourquoi AD est « les clés du royaume »

Compromettre AD signifie : accès à tout (tous les comptes, tous les mots de passe hashés, toutes les machines, toutes les données), persistence durable (un attaquant qui contrôle AD peut créer des backdoors quasi invisibles — Golden Ticket, Golden Certificate), et contrôle de l'entreprise (déployer du code sur toutes les machines via GPO, modifier les politiques de sécurité, exfiltrer des données). Les composants AD (DC, comptes admins) sont classés **Tier 0** — le niveau de criticité le plus élevé. Les compromissions AD sont au cœur de la majorité des attaques majeures (ransomwares, APT).

## 1.3 AD DS vs Entra ID (ex-Azure AD)

AD DS (on-premises) utilise LDAP, Kerberos, NTLM et DNS, avec une structure hiérarchique (forêt → domaines → OUs) et des GPO. Entra ID (cloud) utilise OAuth 2.0, OIDC et SAML, avec un tenant plat et Conditional Access/Intune. La majorité des entreprises sont en **mode hybride** : AD DS on-prem synchronisé avec Entra ID. Ce cours couvre AD DS en profondeur (Parties I-VI) et l'hybride/Entra ID dans la Partie VII.

## 1.4 Fil rouge — KERBEROS : la mission

> **🔴 KERBEROS — Épisode 1**
>
> Thomas reçoit le périmètre : forêt mono-domaine meridian.local, 2 DC physiques (DC01-LYO, DC02-LYO) + 1 RODC (RODC-GVA à Genève — site R&D avec 300 utilisateurs), AD CS déployé (CA subordonnée YOURCA-CA), Azure AD Connect vers Entra ID (PHS). Objectif : Domain Admin. Contrainte : ne pas perturber la production (usine connectée). Thomas se connecte au poste utilisateur avec le compte t.granier@meridian.local — aucun privilège.

---
