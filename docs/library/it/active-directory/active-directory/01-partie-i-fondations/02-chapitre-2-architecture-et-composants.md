---
title: Chapitre 2 — Architecture et composants
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 2.1 Domaine, arbre, forêt

L'architecture AD est hiérarchique. Le **domaine** est l'unité de base (ex : meridian.local) — tous les objets partagent la même base AD, les mêmes politiques, les mêmes administrateurs. L'**arbre** (Tree) est une hiérarchie de domaines partageant un namespace contigu (ex : meridian.local → eu.meridian.local). La **forêt** (Forest) est l'ensemble de domaines partageant un schéma commun et des relations de confiance — c'est la **frontière de sécurité ultime** d'AD (en théorie — en pratique, des attaques cross-forêt existent via les trusts, cf. Ch.4).

## 2.2 Le contrôleur de domaine (DC)

Le DC est le serveur le plus critique de l'infrastructure. Il héberge : le **NTDS.dit** (base de données AD — tous les objets, tous les attributs, y compris les hashes de mots de passe), le **service LDAP** (requêtes d'annuaire — ports 389/636), le **service Kerberos / KDC** (authentification — port 88), le **DNS intégré** (résolution de noms — port 53), et le **partage SYSVOL** (réplication des GPO et scripts de logon entre DC). En production, minimum 2 DC pour la redondance. Un DC compromis = AD compromis = entreprise compromise.

## 2.3 Le RODC (Read-Only Domain Controller)

Le RODC est un DC en lecture seule déployé sur les sites distants où la sécurité physique est moindre. Il contient une copie partielle de la base AD — par défaut, il ne cache que les mots de passe des comptes autorisés par la **Password Replication Policy** (PRP). Si le RODC est compromis, seuls les mots de passe cachés localement sont exposés (pas ceux des comptes admin, pas le krbtgt du domaine — le RODC utilise son propre krbtgt, le krbtgt_XXXXX). Les idées reçues : « le RODC est sûr donc on peut le mettre n'importe où » est faux — un RODC mal configuré (PRP trop large, admin local compromis) expose des comptes. La PRP doit être auditée régulièrement.

## 2.4 Réplication et sites

La réplication propage les modifications entre DC. **Intra-site** : réplication rapide (secondes), déclenchée par notification. **Inter-sites** : réplication planifiée (toutes les 15-180 min). Les **sites** représentent les emplacements physiques (siège, usine, R&D) associés à des subnets IP — les clients contactent le DC le plus proche de leur site. **DFSR** (Distributed File System Replication) réplique SYSVOL entre les DC.

## 2.5 Rôles FSMO

Cinq rôles spéciaux (Flexible Single Master Operations) sont attribués à des DC spécifiques : **Schema Master** (forêt — modifications du schéma), **Domain Naming Master** (forêt — ajout/suppression de domaines), **PDC Emulator** (domaine — le plus critique au quotidien : source de temps, changements de MdP immédiats, verrouillage de comptes), **RID Master** (domaine — attribue les blocs de RID pour les SID), **Infrastructure Master** (domaine — résout les références cross-domaine).

## 2.6 Global Catalog, schéma, DNS et NTP

Le **Global Catalog** est un DC qui contient une copie partielle de TOUS les objets de TOUTE la forêt — indispensable pour les recherches multi-domaines et le login (vérification des groupes universels). Le **schéma** définit les types d'objets et attributs — unique pour toute la forêt, modifications irréversibles (Schema Admins = groupe très privilégié). **DNS** est critique : AD dépend fondamentalement de DNS — les enregistrements SRV (_ldap._tcp.dc._msdcs.meridian.local) permettent aux machines de trouver les DC. Sans DNS, plus d'authentification. **NTP** : Kerberos a une tolérance de 5 minutes entre l'horloge client et le DC — le PDC Emulator est la source de temps de référence.

## 2.7 Ports et flux AD

Le tableau de référence : DNS 53, Kerberos 88, RPC Endpoint Mapper 135, LDAP 389, SMB 445 (SYSVOL, GPO), Kerberos kpasswd 464, LDAPS 636, GC 3268/3269, WinRM 5985/5986, ADWS 9389, RPC dynamiques 49152+. Comprendre les flux = comprendre la segmentation nécessaire.

---
