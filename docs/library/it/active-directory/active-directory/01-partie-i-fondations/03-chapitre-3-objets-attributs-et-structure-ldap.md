---
title: Chapitre 3 — Objets, attributs et structure LDAP
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 3.1 Types d'objets

Les **utilisateurs** (classe user — compte d'une personne ou d'un service), les **ordinateurs** (classe computer — machine jointe au domaine, identifiée par le $ final : SRV-WEB01$), les **groupes** (classe group — ensemble d'objets), les **OUs** (organizationalUnit — conteneurs pour organiser et appliquer des GPO), les **GPOs** (groupPolicyContainer — politiques de configuration), et les **gMSA** (msDS-GroupManagedServiceAccount — comptes de service avec mot de passe de 240 caractères géré automatiquement par AD — la solution au Kerberoasting).

## 3.2 Attributs critiques pour la sécurité

**sAMAccountName** (nom de connexion legacy), **SID** (Security Identifier — identifiant unique S-1-5-21-..., SIDs well-known : S-1-5-21-...-500 = Administrator, -512 = Domain Admins), **memberOf** (groupes d'un objet), **adminCount** (= 1 si l'objet est ou a été membre d'un groupe privilégié — ne se réinitialise PAS automatiquement), **userAccountControl** (flags — UF_DONT_REQUIRE_PREAUTH = AS-REP Roastable, UF_TRUSTED_FOR_DELEGATION = unconstrained delegation), **ServicePrincipalName** (SPN — cible de Kerberoasting si sur un compte utilisateur), **msDS-AllowedToDelegateTo** (constrained delegation), **msDS-KeyCredentialLink** (Windows Hello / Shadow Credentials — vecteur d'attaque moderne), **pwdLastSet** (dernier changement de mot de passe), et **lastLogonTimestamp** (dernière connexion — répliqué, pas temps réel).

## 3.3 Groupes : portées et imbrication

**Domain Local** (utilisable uniquement dans le domaine local — pour les ACL sur les ressources), **Global** (membres du même domaine uniquement — pour regrouper les utilisateurs par rôle), **Universal** (membres de toute la forêt — répliqué dans le GC). Le modèle **IGDLA** (Identities → Global groups → Domain Local groups → Access — la meilleure pratique pour structurer les permissions). Les **groupes privilégiés built-in** : Domain Admins, Enterprise Admins, Schema Admins, Administrators, Backup Operators (peuvent extraire NTDS.dit), Account Operators (peuvent créer/modifier des comptes), Server Operators (accès aux DC), Print Operators, DnsAdmins (peuvent charger une DLL sur le DNS du DC → RCE sur le DC).

## 3.4 LDAP : recherche et requêtes

Le protocole LDAP (port 389 / LDAPS 636) permet d'interroger l'annuaire. La structure : **base DN** (point de départ — DC=meridian,DC=local), **scope** (base / onelevel / subtree), **filtre** ((&(objectClass=user)(adminCount=1)) — tous les comptes avec adminCount=1), **attributs retournés** (sAMAccountName, memberOf, pwdLastSet). Tout utilisateur du domaine peut énumérer l'intégralité de l'AD via LDAP — c'est par design, et c'est ce qui rend la reconnaissance si facile pour un attaquant.

## 3.5 Trusts : relations de confiance et abus inter-domaines

*Les trusts étendent la confiance au-delà du domaine — et avec elle, la surface d'attaque.*

Un **trust** est une relation de confiance entre deux domaines (ou deux forêts) qui permet aux utilisateurs d'un domaine de s'authentifier dans l'autre. Les types : **Parent-Child** (automatique dans un arbre — bidirectionnel, transitif), **Tree-Root** (entre les racines d'arbres dans une forêt — bidirectionnel, transitif), **Shortcut** (optimisation entre deux domaines d'une même forêt — bidirectionnel, transitif), **External** (entre un domaine et un domaine d'une autre forêt — unidirectionnel ou bidirectionnel, non transitif), et **Forest** (entre deux forêts — bidirectionnel, transitif au sein de chaque forêt mais le SID filtering filtre les SIDs étrangers par défaut).

Les **abus de trusts** : dans un trust intra-forêt, le **SID History** peut être exploité — un attaquant qui compromet un domaine enfant peut forger un Golden Ticket avec le SID de Enterprise Admins du domaine parent (ExtraSids attack) → compromission de toute la forêt depuis un seul domaine enfant. C'est pourquoi **la forêt est la vraie frontière de sécurité, pas le domaine**. Pour les trusts inter-forêts, le **SID filtering** est activé par défaut et filtre les SIDs étrangers — mais des configurations permissives (TrustAttributes avec TREAT_AS_EXTERNAL ou CROSS_ORGANIZATION désactivé) peuvent ouvrir des chemins d'attaque. La **Kerberos delegation** à travers les trusts est un autre vecteur : si un service dans le domaine A a une unconstrained delegation et qu'un utilisateur du domaine B s'y connecte, le TGT du domaine B est capturé.

L'audit des trusts : lister tous les trusts (Get-ADTrust -Filter *), vérifier la direction, la transitivité, le SID filtering, et les attributs de confiance. Un trust oublié vers un domaine non maintenu est un chemin d'attaque.

---
