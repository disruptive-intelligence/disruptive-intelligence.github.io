---
title: Partie VI — Hardening
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

*Réduire la surface d'attaque d'AD : d'abord les mesures rapides à fort impact, puis l'authentification, puis le cœur Tier 0, et enfin la capacité à reconstruire.*

---


## Chapitre 23 — Top 10 actions de hardening et quick wins

Quand le temps et le budget manquent, on commence par les mesures qui ferment le plus de chemins pour le moins d'effort. L'ordre ci-dessous va du plus urgent au plus structurant.

| # | Action | Ce qu'elle apporte | Effort |
|---|---|---|---|
| 1 | Activer l'**Advanced Audit Policy** sur tous les DC et centraliser les journaux | Visibilité : sans elle, rien ne se détecte | Faible |
| 2 | Déployer **Windows LAPS** sur tout le parc | Supprime le mot de passe administrateur local commun | Faible à moyen |
| 3 | **Séparer** comptes d'administration et comptes bureautiques ; aucun Domain Admin sur les postes | Les secrets Tier 0 ne s'exposent plus en Tier 2 | Moyen |
| 4 | Rendre la **signature SMB** obligatoire | Empêche la réutilisation d'une authentification NTLM vers SMB | Faible (tester les équipements anciens) |
| 5 | Désactiver **LLMNR**, **NBT-NS** (et mDNS si inutile) | Supprime la résolution de noms par diffusion | Faible |
| 6 | Renouveler le mot de passe de **`krbtgt`** (deux fois, espacées) | Invalide d'éventuels tickets forgés | Faible, à planifier |
| 7 | **Auditer les ACL** et les chemins de privilèges (PingCastle, BloodHound) | Ferme les chemins invisibles vers Domain Admin | Moyen |
| 8 | Supprimer les **comptes inactifs** et les **SPN inutiles** ; passer les comptes de service en **gMSA** | Réduit la surface des comptes de service | Moyen |
| 9 | Placer les comptes Tier 0 dans **Protected Users** | Retire les mécanismes d'authentification les plus exposés | Faible (tester) |
| 10 | Durcir les **modèles de certificats AD CS** | Ferme les escalades via la PKI | Moyen |

> **Méthode.** Mesurer avant et après : un rapport PingCastle avant le chantier, un après chaque lot. Le score n'est pas un objectif en soi, mais il rend les progrès visibles pour la direction.

---


## Chapitre 24 — Hardening NTLM, Kerberos et authentification

### 24.1 Réduire NTLM progressivement

Couper NTLM d'un coup casse des applications. La démarche :

```text
1. Auditer   → GPO « Restrict NTLM : Audit … » ; événements 8001-8004 (journal NTLM)
2. Corriger  → accès par nom plutôt que par IP, SPN manquants, applications à mettre à jour
3. Documenter les exceptions restantes (liste blanche de serveurs)
4. Restreindre → « Restrict NTLM : Deny … » domaine par domaine
```


Interdire **LM et NTLMv1** (*LAN Manager authentication level* = « Send NTLMv2 response only. Refuse LM & NTLM ») est en revanche immédiat sur un parc récent.

### 24.2 Signer et lier les canaux

| Mesure | Paramètre | Protège |
|---|---|---|
| **SMB signing** | *Microsoft network server/client : Digitally sign communications (always)* | Les sessions SMB contre l'interception et la réutilisation |
| **LDAP signing** | *Domain controller : LDAP server signing requirements* = Require signing | Les échanges LDAP |
| **LDAP channel binding** | *LdapEnforceChannelBinding* = 2 (toujours) | LDAPS contre la réutilisation d'une authentification |
| **EPA** (*Extended Protection for Authentication*) | Sur IIS, AD CS Web Enrollment, ADFS | Les services web authentifiés en NTLM |

### 24.3 Durcir Kerberos

- **AES uniquement** : désactiver RC4 (et DES) pour les comptes et les DC une fois l'inventaire fait ; les comptes de service doivent annoncer AES ;
- **Pré-authentification** obligatoire sur tous les comptes ;
- **Délégation** : aucune délégation non contrainte hors DC ; préférer la délégation contrainte, bien bornée ; cocher « compte sensible et ne peut pas être délégué » sur les comptes privilégiés ;
- **Comptes de service** : gMSA partout où c'est possible, sinon mots de passe longs (25 caractères et plus) et renouvelés ;
- **`krbtgt`** : rotation régulière (par exemple annuelle) et après tout départ d'administrateur ou incident.

### 24.4 Protected Users

Le groupe **Protected Users** applique des restrictions non configurables à ses membres :

| Restriction | Effet |
|---|---|
| Pas de NTLM | Authentification uniquement en Kerberos |
| Pas de DES ni RC4 dans Kerberos | AES obligatoire |
| Pas de délégation | Le compte ne peut pas être délégué |
| TGT de 4 heures, non renouvelable au-delà | Réduit la durée d'utilité d'un ticket |
| Pas de mise en cache des identifiants | Pas de connexion hors ligne avec ces comptes |

À réserver aux comptes humains privilégiés, après test : il ne convient ni aux comptes de service ni aux comptes d'ordinateur.

### 24.5 Protéger les secrets en mémoire

| Mesure | Principe | Limite |
|---|---|---|
| **Credential Guard** | Isole les secrets d'authentification de LSASS dans un environnement protégé par l'hyperviseur (VBS) | Ne protège pas les identifiants mis en cache ni la SAM ; nécessite du matériel compatible |
| **LSA Protection** (*RunAsPPL*) | LSASS tourne en processus protégé : les processus non protégés ne peuvent plus lire sa mémoire | Moins fort que Credential Guard, mais plus compatible |
| **WDigest désactivé** | Plus de mot de passe réversible en mémoire | Défaut depuis Windows 8.1 / 2012 R2 : à vérifier |
| **Cache réduit** | *Interactive logon : Number of previous logons to cache* bas sur les serveurs | Gêne les postes nomades si trop bas |

### 24.6 Politiques de mots de passe

La politique du domaine (GPO liée au domaine) fixe le socle ; les **FGPP** (*Fine-Grained Password Policies*), appliquées à des groupes, permettent des exigences plus fortes pour les administrateurs et les comptes de service. Les recommandations actuelles privilégient la **longueur** (phrases de passe), le **blocage des mots de passe connus ou compromis** et le **MFA** pour les accès sensibles, plutôt que des changements fréquents imposés.

---


## Chapitre 25 — Hardening AD CS, GPO et Tier 0

### 25.1 AD CS

| Mesure | Détail |
|---|---|
| Auditer les modèles de certificats | Outils d'audit PKI (PingCastle, Locksmith, Certipy en mode inventaire) |
| Interdire au demandeur de choisir le sujet | Sauf besoin documenté, avec approbation d'un gestionnaire |
| Restreindre les droits d'inscription | Pas d'inscription pour *Domain Users* ou *Authenticated Users* sur les modèles d'authentification |
| Proscrire « Any Purpose » et les modèles de sous-CA non maîtrisés | Usages limités au besoin |
| Sécuriser les permissions des modèles et de la CA | Modification réservée au Tier 0 |
| Web Enrollment en HTTPS avec EPA, ou désactivé | Ferme la réutilisation d'authentification NTLM vers la CA |
| CA racine hors ligne | La clé racine n'est jamais exposée |
| Journaliser et centraliser | Émissions (4886/4887), modifications de modèles |

La CA et ses serveurs sont **Tier 0** : quiconque contrôle la CA peut émettre des certificats d'authentification pour n'importe quel compte.

### 25.2 GPO

- restreindre la création, la modification et la liaison de GPO (onglet *Délégation* de GPMC) ;
- traiter comme Tier 0 les GPO liées aux DC et à la racine du domaine ;
- auditer les modifications (5136 sur les objets GPO, versions dans SYSVOL) ;
- aucun secret dans SYSVOL ni NETLOGON.

### 25.3 Le Tier 0

| Mesure | Pourquoi |
|---|---|
| DC sans accès Internet, sans navigation, sans logiciel tiers superflu | Réduire les points d'entrée |
| Administration uniquement depuis des PAW | Ne pas exposer les secrets Tier 0 |
| Réseau d'administration dédié, flux filtrés vers les DC | Limiter qui peut parler aux DC |
| Comptes de service des DC en gMSA | Pas de mot de passe statique |
| Hyperviseurs, sauvegardes et consoles qui touchent les DC classés Tier 0 | Ce qui contrôle un DC est un DC |
| Surveillance maximale (EDR, journaux, changements d'objets) | Détecter vite |
| Groupes privilégiés quasiment vides ; accès temporaire si possible | Moins de comptes, moins d'exposition |

### 25.4 RODC

- PRP minimale : seuls les utilisateurs et postes du site ;
- **aucun compte privilégié** dans la liste autorisée (le groupe *Denied RODC Password Replication Group* doit contenir les groupes Tier 0) ;
- revue régulière des comptes réellement mis en cache ;
- sécurité physique du local.

> **🔴 KERBEROS — Épisode 6**
>
> Thomas examine le RODC de Genève. La PRP autorise 45 comptes, dont 3 comptes de service Tier 1 — beaucoup trop. Le RODC est installé dans un local technique sans contrôle d'accès : un accès physique simulé suffit à exposer les secrets mis en cache. L'un de ces comptes de service dispose de droits d'écriture sur un groupe IT, premier maillon d'un chemin vers l'administration du domaine. Le RODC, censé limiter l'exposition, l'aggrave. Recommandations : PRP réduite aux utilisateurs de Genève, comptes de service exclus, local sécurisé.

---


## Chapitre 26 — Backup, restore et résilience AD

### 26.1 Pourquoi c'est critique

Un AD compromis ou détruit (rançongiciel) sans sauvegarde saine impose une reconstruction complète : des semaines d'arrêt. La sauvegarde de l'AD est donc un actif **Tier 0** : elle contient NTDS.dit, c'est-à-dire les secrets de tous les comptes.

### 26.2 Ce qu'on sauvegarde

La **sauvegarde de l'état du système** (*System State*) d'au moins deux DC par domaine : NTDS.dit, registre, SYSVOL, fichiers de démarrage, base de la CA si le DC l'héberge. Outils : Windows Server Backup, ou une solution du marché compatible AD.

### 26.3 Les modes de restauration

| Mode | Usage |
|---|---|
| **Non autoritaire** | Restaurer un DC, qui se resynchronise ensuite avec les autres |
| **Autoritaire** | Restaurer des objets supprimés et les marquer comme faisant foi pour que la réplication les propage |
| **Corbeille AD** (*Recycle Bin*) | Récupérer un objet supprimé avec tous ses attributs, sans restauration ; **à activer** (irréversible, sans inconvénient) |
| **Restauration de forêt** | Reconstruire toute la forêt après une compromission ou une destruction totale |

### 26.4 Les règles de résilience

- au moins **deux DC par domaine**, sur des sites différents ;
- sauvegardes **hors ligne ou immuables**, isolées du domaine qu'elles protègent ;
- accès aux sauvegardes réservé au Tier 0, et journalisé ;
- **tests de restauration** réguliers dans un environnement isolé : la première restauration ne doit pas avoir lieu le jour de l'incident ;
- un **plan de restauration de forêt** écrit (ordre des opérations, DC de départ, rotation des secrets) ;
- la réplication n'est pas une sauvegarde : une suppression ou une corruption se réplique aussi.

---
