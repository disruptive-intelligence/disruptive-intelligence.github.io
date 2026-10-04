---
title: Chapitre 1 — Active Directory
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie I — Fondations
  - index.md
---

pourquoi c'est partout et pourquoi c'est la cible n°1

Active Directory (AD) est le service d'annuaire de Microsoft. Il centralise la gestion des **identités** (utilisateurs, comptes de service), des **machines**, des **groupes** et des **politiques de sécurité** d'un réseau Windows dans un référentiel unique.

## 1.1 Le problème que résout Active Directory

Imaginez une entreprise de 5 000 employés : chacun a un poste, une messagerie, des accès à des partages et à des applications métier. Sans annuaire, il faudrait créer chaque compte sur chaque machine et maintenir des milliers de mots de passe dispersés. AD remplace ce modèle par une gestion centralisée :

| Sans AD (groupe de travail) | Avec AD (domaine) |
|---|---|
| Un compte local par machine, dans la SAM de chaque poste | Un compte unique, stocké sur les contrôleurs de domaine |
| Mots de passe et droits gérés poste par poste | Politiques appliquées à tout le parc par GPO |
| Aucune vue d'ensemble des accès | Groupes et droits centralisés, auditables |
| L'utilisateur se réauthentifie pour chaque ressource | **Single Sign-On** : une connexion, accès à tout ce qui est autorisé |

AD est intégré à Windows Server depuis 2000 et reste le socle d'identité de la très grande majorité des entreprises.

## 1.2 Ce que contient l'annuaire

L'annuaire est un catalogue d'**objets**, chacun décrit par des **attributs** :

- **Utilisateurs** — des *security principals* (toute entité qui peut s'authentifier et recevoir des droits). Ils représentent des personnes ou des **comptes de service** (IIS, MSSQL…) qui ont besoin d'une identité pour fonctionner.
- **Ordinateurs** — toute machine qui rejoint le domaine reçoit un objet ordinateur, lui aussi security principal, avec son propre compte et mot de passe. Son nom de compte est le nom de la machine suivi d'un `$` (`DC01$`).
- **Groupes de sécurité** — ils regroupent des identités pour leur attribuer des droits sur des ressources.
- **Unités d'organisation (OU)** — des conteneurs qui rangent les objets, servent à **appliquer des GPO** et à **déléguer l'administration**.

> **OU ou groupe ?** Une OU sert à *organiser et administrer* (GPO, délégation) : un objet n'est que dans une seule OU. Un groupe sert à *donner des droits* : un utilisateur peut être dans plusieurs groupes. Placer un utilisateur dans l'OU « RH » ne lui donne aucun droit sur les partages RH.

## 1.3 Pourquoi AD est « les clés du royaume »

Contrôler AD, c'est contrôler l'entreprise :

- **accès à tout** — tous les comptes, les secrets de tous les mots de passe, toutes les machines jointes ;
- **pouvoir de configuration** — une GPO modifiée s'applique à des milliers de postes ;
- **persistance** — un attaquant qui maîtrise AD peut se maintenir durablement, de façon très discrète.

C'est pourquoi les contrôleurs de domaine, les comptes d'administration du domaine et tout ce qui peut les contrôler sont classés **Tier 0**, le niveau de criticité le plus élevé (Ch.11). La compromission d'AD est l'étape centrale de la plupart des attaques majeures, rançongiciels en tête.

## 1.4 AD DS et Entra ID (ex-Azure AD)

| | **AD DS** (on-premises) | **Entra ID** (cloud) |
|---|---|---|
| Protocoles | LDAP, Kerberos, NTLM, DNS | OAuth 2.0, OpenID Connect, SAML |
| Structure | Hiérarchique : forêt → domaines → OU | Tenant plat |
| Configuration | GPO | Conditional Access, Intune |
| Cas d'usage | Postes, serveurs, applications internes | Applications SaaS, Microsoft 365 |

La plupart des entreprises sont en **mode hybride** : AD DS synchronisé avec Entra ID. Ce cours traite AD DS en profondeur (Parties I à VI) et l'hybride dans la Partie VII.

## 1.5 Fil rouge — KERBEROS : la mission

> **🔴 KERBEROS — Épisode 1**
>
> Thomas reçoit le périmètre : forêt mono-domaine meridian.local, 2 DC physiques (DC01-LYO, DC02-LYO) + 1 RODC (RODC-GVA à Genève — site R&D avec 300 utilisateurs), AD CS déployé (CA subordonnée), Azure AD Connect vers Entra ID (PHS). Objectif : Domain Admin. Contrainte : ne pas perturber la production (usine connectée). Thomas se connecte au poste utilisateur avec le compte t.granier@meridian.local — aucun privilège.

---
