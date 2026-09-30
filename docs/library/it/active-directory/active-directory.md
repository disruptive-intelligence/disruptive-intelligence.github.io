---
title: Active Directory
source: IT/04_Active-Directory/Active_Directory.md
---

*Comprendre • Attaquer • Défendre • Répondre*

**Cours complet — 32 chapitres • 7 parties • 7 annexes**

*Architecture • Kerberos/NTLM • AD CS • BloodHound • Attaques • Détection • Hardening • IR • Hybrid*

---

### Table des matières

- [Fil rouge : Opération KERBEROS](#fil-rouge-operation-kerberos)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - [Ch.1 — Active Directory : pourquoi c'est partout et pourquoi c'est la cible n°1](#chapitre-1-active-directory-pourquoi-cest-partout-et-pourquoi-cest-la-cible-n1)
  - [Ch.2 — Architecture et composants](#chapitre-2-architecture-et-composants)
  - [Ch.3 — Objets, attributs et structure LDAP](#chapitre-3-objets-attributs-et-structure-ldap)
  - [Ch.4 — Autorisations, ACL, trusts et modèle de sécurité](#chapitre-4-autorisations-acl-et-modele-de-securite)
- **PARTIE II — AUTHENTIFICATION (Ch.5-8)**
  - [Ch.5 — NTLM : le protocole legacy qui refuse de mourir](#chapitre-5-ntlm-le-protocole-legacy-qui-refuse-de-mourir)
  - [Ch.6 — Kerberos : le flux complet et les subtilités](#chapitre-6-kerberos-le-flux-complet-et-les-subtilites)
  - [Ch.7 — Où sont stockés les secrets et comment ils sont volés](#chapitre-7-ou-sont-stockes-les-secrets-et-comment-ils-sont-voles)
  - [Ch.8 — AD CS : PKI interne, certificats et surface d'attaque](#chapitre-8-ad-cs-pki-interne-certificats-et-surface-dattaque)
- **PARTIE III — ADMINISTRATION ET CONTRÔLE (Ch.9-12)**
  - [Ch.9 — Group Policy (GPO) : configuration et sécurité](#chapitre-9-group-policy-gpo-configuration-et-securite)
  - [Ch.10 — Outils d'administration et requêtage](#chapitre-10-outils-dadministration-et-requetage)
  - [Ch.11 — Tiering model et séparation des privilèges](#chapitre-11-tiering-model-et-separation-des-privileges)
  - [Ch.12 — Journalisation et audit AD](#chapitre-12-journalisation-et-audit-ad)
- **PARTIE IV — ATTAQUES AD (Ch.13-18)**
  - [Ch.13 — Reconnaissance et énumération](#chapitre-13-reconnaissance-et-enumeration)
  - [Ch.14 — BloodHound et analyse de chemins d'attaque](#chapitre-14-bloodhound-et-analyse-de-chemins-dattaque)
  - [Ch.15 — Credential attacks : Kerberoasting, relay et coercion](#chapitre-15-credential-attacks-kerberoasting-as-rep-relay-et-coercion)
  - [Ch.16 — Mouvement latéral, escalade et ACL abuse](#chapitre-16-mouvement-lateral-escalade-et-acl-abuse)
  - [Ch.17 — Persistence : Golden Ticket, Shadow Credentials et au-delà](#chapitre-17-persistence-golden-ticket-shadow-credentials-et-au-dela)
  - [Ch.18 — Kill chain AD typique : du phishing au Domain Admin](#chapitre-18-kill-chain-ad-typique-du-phishing-au-domain-admin)
- **PARTIE V — DÉTECTION (Ch.19-22)**
  - [Ch.19 — Minimum Viable Visibility : la télémétrie indispensable](#chapitre-19-minimum-viable-visibility-la-telemetrie-indispensable)
  - [Ch.20 — Détecter les attaques AD dans le SIEM](#chapitre-20-detecter-les-attaques-ad-dans-le-siem)
  - [Ch.21 — Deception et honey objects](#chapitre-21-deception-et-honey-objects)
  - [Ch.22 — Règles SIEM et corrélation avancée](#chapitre-22-regles-siem-et-correlation-avancee)
- **PARTIE VI — HARDENING (Ch.23-26)**
  - [Ch.23 — Top 10 actions de hardening et quick wins](#chapitre-23-top-10-actions-de-hardening-et-quick-wins)
  - [Ch.24 — Hardening NTLM, Kerberos et authentification](#chapitre-24-hardening-ntlm-kerberos-et-authentification)
  - [Ch.25 — Hardening AD CS, GPO et Tier 0](#chapitre-25-hardening-ad-cs-gpo-et-tier-0)
  - [Ch.26 — Backup, restore et résilience AD](#chapitre-26-backup-restore-et-resilience-ad)
- **PARTIE VII — INCIDENT RESPONSE, HYBRID IDENTITY ET SYNTHÈSE (Ch.27-32)**
  - [Ch.27 — Incident Response AD : méthodologie](#chapitre-27-incident-response-ad-methodologie)
  - [Ch.28 — Containment, nettoyage et rotation krbtgt](#chapitre-28-containment-nettoyage-et-rotation-krbtgt)
  - [Ch.29 — Rebuild vs Clean et retour à la normale](#chapitre-29-rebuild-vs-clean-et-retour-a-la-normale)
  - [Ch.30 — Entra ID / Hybrid : architecture et synchronisation](#chapitre-30-entra-id-hybrid-architecture-et-synchronisation)
  - [Ch.31 — Attaques et défense du cloud identity](#chapitre-31-attaques-et-defense-du-cloud-identity)
  - [Ch.32 — Cas de synthèse : rapport de pentest AD complet](#chapitre-32-cas-de-synthese-rapport-de-pentest-ad-complet)
- **ANNEXES**

---

### Fil rouge : Opération KERBEROS

> **Contexte narratif — ce fil rouge alterne entre perspective offensive et défensive tout au long du cours.**
>
> **Thomas Granier**, consultant senior en sécurité offensive chez **RedForge** (cabinet de pentest et réponse à incident, 30 personnes), est mandaté pour un **test d'intrusion interne** sur l'AD de **Meridian Pharma** — laboratoire pharmaceutique européen, 4 200 collaborateurs, 3 sites (siège Lyon, usine Strasbourg, R&D Genève), forêt AD mono-domaine (meridian.local), ~120 serveurs, ~3 500 postes, hybrid AD avec Entra ID (Azure AD Connect, PHS), AD CS déployé (PKI interne pour les certificats machines et VPN), 2 DC physiques au siège + 1 RODC sur le site de Genève.
>
> Thomas démarre avec un accès réseau standard (poste utilisateur joint au domaine, compte sans privilèges). Objectif : atteindre le Domain Admin, documenter chaque étape, et produire le rapport de pentest avec recommandations priorisées.
>
> En parallèle, la **Blue Team** de Meridian (SOC interne, 3 analystes) a pour mission de détecter l'intrusion et de pratiquer la réponse à incident.

---

### PARTIE I — FONDATIONS

*Comprendre AD, son architecture, ses objets, ses protocoles et son modèle de sécurité.*

---

#### Chapitre 1 — Active Directory : pourquoi c'est partout et pourquoi c'est la cible n°1

Active Directory est un service d'annuaire Microsoft utilisé pour centraliser la gestion des identités, groupes, ordinateurs et ressources dans un environnement Windows.
##### 1.1 Le problème que résout Active Directory

Imaginez une entreprise de 5 000 employés. Chaque employé a un PC, un compte email, des accès à des partages réseau, des applications métier. Sans système centralisé, il faudrait créer et gérer chaque compte sur chaque machine individuellement. Active Directory résout ce problème : c'est un service d'annuaire centralisé qui stocke et gère toutes les identités (utilisateurs, ordinateurs, services) et les politiques de sécurité d'une organisation. Un employé se connecte une fois avec son compte AD, et il accède à tout ce à quoi il a droit : c'est le Single Sign-On (SSO). AD est développé par Microsoft et intégré à Windows Server depuis 2000. Il est présent dans plus de 90 % des entreprises dans le monde.

##### 1.2 Pourquoi AD est « les clés du royaume »

Compromettre AD signifie : accès à tout (tous les comptes, tous les mots de passe hashés, toutes les machines, toutes les données), persistence durable (un attaquant qui contrôle AD peut créer des backdoors quasi invisibles — Golden Ticket, Golden Certificate), et contrôle de l'entreprise (déployer du code sur toutes les machines via GPO, modifier les politiques de sécurité, exfiltrer des données). Les composants AD (DC, comptes admins) sont classés **Tier 0** — le niveau de criticité le plus élevé. Les compromissions AD sont au cœur de la majorité des attaques majeures (ransomwares, APT).

##### 1.3 AD DS vs Entra ID (ex-Azure AD)

AD DS (on-premises) utilise LDAP, Kerberos, NTLM et DNS, avec une structure hiérarchique (forêt → domaines → OUs) et des GPO. Entra ID (cloud) utilise OAuth 2.0, OIDC et SAML, avec un tenant plat et Conditional Access/Intune. La majorité des entreprises sont en **mode hybride** : AD DS on-prem synchronisé avec Entra ID. Ce cours couvre AD DS en profondeur (Parties I-VI) et l'hybride/Entra ID dans la Partie VII.

##### 1.4 Fil rouge — KERBEROS : la mission

> **🔴 KERBEROS — Épisode 1**
>
> Thomas reçoit le périmètre : forêt mono-domaine meridian.local, 2 DC physiques (DC01-LYO, DC02-LYO) + 1 RODC (RODC-GVA à Genève — site R&D avec 300 utilisateurs), AD CS déployé (CA subordonnée YOURCA-CA), Azure AD Connect vers Entra ID (PHS). Objectif : Domain Admin. Contrainte : ne pas perturber la production (usine connectée). Thomas se connecte au poste utilisateur avec le compte t.granier@meridian.local — aucun privilège.

---

#### Chapitre 2 — Architecture et composants

##### 2.1 Domaine, arbre, forêt

L'architecture AD est hiérarchique. Le **domaine** est l'unité de base (ex : meridian.local) — tous les objets partagent la même base AD, les mêmes politiques, les mêmes administrateurs. L'**arbre** (Tree) est une hiérarchie de domaines partageant un namespace contigu (ex : meridian.local → eu.meridian.local). La **forêt** (Forest) est l'ensemble de domaines partageant un schéma commun et des relations de confiance — c'est la **frontière de sécurité ultime** d'AD (en théorie — en pratique, des attaques cross-forêt existent via les trusts, cf. Ch.4).

##### 2.2 Le contrôleur de domaine (DC)

Le DC est le serveur le plus critique de l'infrastructure. Il héberge : le **NTDS.dit** (base de données AD — tous les objets, tous les attributs, y compris les hashes de mots de passe), le **service LDAP** (requêtes d'annuaire — ports 389/636), le **service Kerberos / KDC** (authentification — port 88), le **DNS intégré** (résolution de noms — port 53), et le **partage SYSVOL** (réplication des GPO et scripts de logon entre DC). En production, minimum 2 DC pour la redondance. Un DC compromis = AD compromis = entreprise compromise.

##### 2.3 Le RODC (Read-Only Domain Controller)

Le RODC est un DC en lecture seule déployé sur les sites distants où la sécurité physique est moindre. Il contient une copie partielle de la base AD — par défaut, il ne cache que les mots de passe des comptes autorisés par la **Password Replication Policy** (PRP). Si le RODC est compromis, seuls les mots de passe cachés localement sont exposés (pas ceux des comptes admin, pas le krbtgt du domaine — le RODC utilise son propre krbtgt, le krbtgt_XXXXX). Les idées reçues : « le RODC est sûr donc on peut le mettre n'importe où » est faux — un RODC mal configuré (PRP trop large, admin local compromis) expose des comptes. La PRP doit être auditée régulièrement.

##### 2.4 Réplication et sites

La réplication propage les modifications entre DC. **Intra-site** : réplication rapide (secondes), déclenchée par notification. **Inter-sites** : réplication planifiée (toutes les 15-180 min). Les **sites** représentent les emplacements physiques (siège, usine, R&D) associés à des subnets IP — les clients contactent le DC le plus proche de leur site. **DFSR** (Distributed File System Replication) réplique SYSVOL entre les DC.

##### 2.5 Rôles FSMO

Cinq rôles spéciaux (Flexible Single Master Operations) sont attribués à des DC spécifiques : **Schema Master** (forêt — modifications du schéma), **Domain Naming Master** (forêt — ajout/suppression de domaines), **PDC Emulator** (domaine — le plus critique au quotidien : source de temps, changements de MdP immédiats, verrouillage de comptes), **RID Master** (domaine — attribue les blocs de RID pour les SID), **Infrastructure Master** (domaine — résout les références cross-domaine).

##### 2.6 Global Catalog, schéma, DNS et NTP

Le **Global Catalog** est un DC qui contient une copie partielle de TOUS les objets de TOUTE la forêt — indispensable pour les recherches multi-domaines et le login (vérification des groupes universels). Le **schéma** définit les types d'objets et attributs — unique pour toute la forêt, modifications irréversibles (Schema Admins = groupe très privilégié). **DNS** est critique : AD dépend fondamentalement de DNS — les enregistrements SRV (_ldap._tcp.dc._msdcs.meridian.local) permettent aux machines de trouver les DC. Sans DNS, plus d'authentification. **NTP** : Kerberos a une tolérance de 5 minutes entre l'horloge client et le DC — le PDC Emulator est la source de temps de référence.

##### 2.7 Ports et flux AD

Le tableau de référence : DNS 53, Kerberos 88, RPC Endpoint Mapper 135, LDAP 389, SMB 445 (SYSVOL, GPO), Kerberos kpasswd 464, LDAPS 636, GC 3268/3269, WinRM 5985/5986, ADWS 9389, RPC dynamiques 49152+. Comprendre les flux = comprendre la segmentation nécessaire.

---

#### Chapitre 3 — Objets, attributs et structure LDAP

##### 3.1 Types d'objets

Les **utilisateurs** (classe user — compte d'une personne ou d'un service), les **ordinateurs** (classe computer — machine jointe au domaine, identifiée par le $ final : SRV-WEB01$), les **groupes** (classe group — ensemble d'objets), les **OUs** (organizationalUnit — conteneurs pour organiser et appliquer des GPO), les **GPOs** (groupPolicyContainer — politiques de configuration), et les **gMSA** (msDS-GroupManagedServiceAccount — comptes de service avec mot de passe de 240 caractères géré automatiquement par AD — la solution au Kerberoasting).

##### 3.2 Attributs critiques pour la sécurité

**sAMAccountName** (nom de connexion legacy), **SID** (Security Identifier — identifiant unique S-1-5-21-..., SIDs well-known : S-1-5-21-...-500 = Administrator, -512 = Domain Admins), **memberOf** (groupes d'un objet), **adminCount** (= 1 si l'objet est ou a été membre d'un groupe privilégié — ne se réinitialise PAS automatiquement), **userAccountControl** (flags — UF_DONT_REQUIRE_PREAUTH = AS-REP Roastable, UF_TRUSTED_FOR_DELEGATION = unconstrained delegation), **ServicePrincipalName** (SPN — cible de Kerberoasting si sur un compte utilisateur), **msDS-AllowedToDelegateTo** (constrained delegation), **msDS-KeyCredentialLink** (Windows Hello / Shadow Credentials — vecteur d'attaque moderne), **pwdLastSet** (dernier changement de mot de passe), et **lastLogonTimestamp** (dernière connexion — répliqué, pas temps réel).

##### 3.3 Groupes : portées et imbrication

**Domain Local** (utilisable uniquement dans le domaine local — pour les ACL sur les ressources), **Global** (membres du même domaine uniquement — pour regrouper les utilisateurs par rôle), **Universal** (membres de toute la forêt — répliqué dans le GC). Le modèle **IGDLA** (Identities → Global groups → Domain Local groups → Access — la meilleure pratique pour structurer les permissions). Les **groupes privilégiés built-in** : Domain Admins, Enterprise Admins, Schema Admins, Administrators, Backup Operators (peuvent extraire NTDS.dit), Account Operators (peuvent créer/modifier des comptes), Server Operators (accès aux DC), Print Operators, DnsAdmins (peuvent charger une DLL sur le DNS du DC → RCE sur le DC).

##### 3.4 LDAP : recherche et requêtes

Le protocole LDAP (port 389 / LDAPS 636) permet d'interroger l'annuaire. La structure : **base DN** (point de départ — DC=meridian,DC=local), **scope** (base / onelevel / subtree), **filtre** ((&(objectClass=user)(adminCount=1)) — tous les comptes avec adminCount=1), **attributs retournés** (sAMAccountName, memberOf, pwdLastSet). Tout utilisateur du domaine peut énumérer l'intégralité de l'AD via LDAP — c'est par design, et c'est ce qui rend la reconnaissance si facile pour un attaquant.

##### 3.5 Trusts : relations de confiance et abus inter-domaines

*Les trusts étendent la confiance au-delà du domaine — et avec elle, la surface d'attaque.*

Un **trust** est une relation de confiance entre deux domaines (ou deux forêts) qui permet aux utilisateurs d'un domaine de s'authentifier dans l'autre. Les types : **Parent-Child** (automatique dans un arbre — bidirectionnel, transitif), **Tree-Root** (entre les racines d'arbres dans une forêt — bidirectionnel, transitif), **Shortcut** (optimisation entre deux domaines d'une même forêt — bidirectionnel, transitif), **External** (entre un domaine et un domaine d'une autre forêt — unidirectionnel ou bidirectionnel, non transitif), et **Forest** (entre deux forêts — bidirectionnel, transitif au sein de chaque forêt mais le SID filtering filtre les SIDs étrangers par défaut).

Les **abus de trusts** : dans un trust intra-forêt, le **SID History** peut être exploité — un attaquant qui compromet un domaine enfant peut forger un Golden Ticket avec le SID de Enterprise Admins du domaine parent (ExtraSids attack) → compromission de toute la forêt depuis un seul domaine enfant. C'est pourquoi **la forêt est la vraie frontière de sécurité, pas le domaine**. Pour les trusts inter-forêts, le **SID filtering** est activé par défaut et filtre les SIDs étrangers — mais des configurations permissives (TrustAttributes avec TREAT_AS_EXTERNAL ou CROSS_ORGANIZATION désactivé) peuvent ouvrir des chemins d'attaque. La **Kerberos delegation** à travers les trusts est un autre vecteur : si un service dans le domaine A a une unconstrained delegation et qu'un utilisateur du domaine B s'y connecte, le TGT du domaine B est capturé.

L'audit des trusts : lister tous les trusts (Get-ADTrust -Filter *), vérifier la direction, la transitivité, le SID filtering, et les attributs de confiance. Un trust oublié vers un domaine non maintenu est un chemin d'attaque.

---

#### Chapitre 4 — Autorisations, ACL et modèle de sécurité

Tout objet dans AD possède un **Security Descriptor** composé de : l'**Owner** (propriétaire — peut modifier les ACL), la **DACL** (liste d'ACE qui définissent qui a le droit de faire quoi sur l'objet), et la **SACL** (liste d'ACE qui définissent ce qui est audité — génère les Event Logs).

Les **ACE** (Access Control Entries) sont de type Allow ou Deny, avec des droits standard (Read, Write, Delete) et des droits étendus spécifiques à AD. Les **droits dangereux** : **GenericAll** (contrôle total — modifier l'objet, réinitialiser le mot de passe, s'ajouter aux groupes), **GenericWrite** (modifier les attributs — notamment ServicePrincipalName pour un targeted Kerberoasting, ou msDS-KeyCredentialLink pour Shadow Credentials), **WriteDACL** (modifier les permissions de l'objet — s'accorder GenericAll), **WriteOwner** (prendre la propriété → puis modifier les ACL), **ForceChangePassword** (réinitialiser le mot de passe sans connaître l'ancien), **Self** (s'ajouter soi-même à un groupe), **Extended Rights DS-Replication-Get-Changes + DS-Replication-Get-Changes-All** (DCSync).

L'**héritage** des ACL : les ACL se propagent dans l'arborescence — une ACL permissive sur une OU s'applique à tous les objets en dessous. **AdminSDHolder** : le processus SDProp réapplique les ACL d'AdminSDHolder sur tous les objets avec adminCount=1 toutes les 60 minutes — un attaquant qui modifie les ACL d'AdminSDHolder obtient un accès persistant à tous les comptes privilégiés (persistence — Ch.17).

---

### PARTIE II — AUTHENTIFICATION

*Le cœur d'AD — les protocoles qui authentifient les utilisateurs et les services.*

---

#### Chapitre 5 — NTLM : le protocole legacy qui refuse de mourir

Le challenge/response NTLM en 4 étapes : négociation (le client demande une connexion), challenge (le serveur envoie un nombre aléatoire), response (le client chiffre le challenge avec le hash de son mot de passe), et vérification (le serveur transmet au DC qui vérifie). **NTLMv1** est cryptographiquement cassable en minutes. **NTLMv2** est plus résistant mais reste vulnérable au relay. Les faiblesses structurelles : pas d'authentification mutuelle (le client ne vérifie pas le serveur → relay possible), hash = clé (Pass-the-Hash), et le hash transite sur le réseau (capture via Responder).

Pourquoi NTLM persiste : accès par IP au lieu du nom DNS, applications legacy, machines non jointes au domaine, certains proxy. Le **Net-NTLMv2 hash** est le hash capturé sur le réseau — crackable offline si le mot de passe est faible, relayable vers d'autres services. Le poisoning **LLMNR/NBT-NS/mDNS** : quand un client ne résout pas un nom via DNS, il tombe en fallback sur des protocoles broadcast (LLMNR port 5355, NBT-NS port 137) — un attaquant avec Responder répond à ces requêtes et capture les hashes NTLM des clients.

> **🔴 KERBEROS — Épisode 2**
>
> Thomas lance Responder sur le VLAN utilisateurs de Meridian. En 15 minutes, il capture 4 hashes Net-NTLMv2 — dont celui de m.laurent (responsable qualité) dont le mot de passe (Pharma2024!) cède en 8 secondes avec hashcat. LLMNR et NBT-NS sont actifs sur tout le parc.

---

#### Chapitre 6 — Kerberos : le flux complet et les subtilités

Le principe fondamental : les mots de passe ne transitent jamais sur le réseau — système de tickets chiffrés. Les **5 étapes** : AS-REQ (le client envoie son identité + timestamp chiffré par son hash = pré-authentification), AS-REP (le KDC vérifie et renvoie un TGT chiffré par la clé krbtgt — le client ne peut pas lire le TGT mais peut le présenter), TGS-REQ (le client présente le TGT et demande un ticket de service pour un SPN), TGS-REP (le KDC renvoie un TGS chiffré par la clé du compte de service cible), AP-REQ (le client présente le TGS au serveur cible qui le déchiffre avec sa propre clé).

Les composants : **KDC** (Key Distribution Center — hébergé sur chaque DC), **TGT** (valide 10h, renouvelable 7j, chiffré par krbtgt), **TGS** (spécifique à un service/SPN, chiffré par le hash du compte de service), **PAC** (Privilege Attribute Certificate — contient le SID de l'utilisateur et ses groupes, inclus dans le ticket), **pré-authentification** (empêche de demander des TGT sans connaître le mot de passe — si désactivée : AS-REP Roasting).

Les **SPN** (Service Principal Name) : identifient un service de manière unique (format service/hostname:port — MSSQLSvc/sql01.meridian.local:1433). Tout utilisateur du domaine peut demander un ticket pour n'importe quel SPN. Si le ticket est chiffré avec le hash d'un compte de service dont le mot de passe est faible → crack offline = **Kerberoasting**.

La **délégation Kerberos** : **Unconstrained** (le service reçoit le TGT complet de l'utilisateur → très dangereux, l'attaquant qui compromet le service récupère tous les TGT des utilisateurs qui s'y connectent), **Constrained** (S4U2Proxy — le service ne peut déléguer que vers des services listés dans msDS-AllowedToDelegateTo), **RBCD** (Resource-Based Constrained Delegation — c'est la ressource cible qui définit qui peut déléguer vers elle via msDS-AllowedToActOnBehalfOfOtherIdentity → abus si l'attaquant contrôle un compte machine).

Le **compte krbtgt** chiffre tous les TGT. Compromettre son hash = forger n'importe quel TGT = **Golden Ticket**. Si le krbtgt n'a jamais été roté (vérifier : Get-ADUser krbtgt -Properties PasswordLastSet), c'est un red flag majeur.

---

#### Chapitre 7 — Où sont stockés les secrets et comment ils sont volés

Le **NTDS.dit** (base AD sur les DC — hashes NTLM de TOUS les comptes, historique de MdP ; extraction = compromission totale ; méthodes : ntdsutil, Volume Shadow Copy, DCSync). La **SAM** (Security Account Manager — hashes des comptes locaux sur chaque machine ; extraction : reg save, secretsdump ; risque : même mot de passe admin local partout → LAPS est la solution). Les **LSA Secrets** (registre — mots de passe de comptes de service, clés de chiffrement, mot de passe machine ; accessibles avec SYSTEM). La **mémoire lsass.exe** (tickets Kerberos, hashes NTLM, parfois mots de passe en clair — Mimikatz, Pypykatz, comsvcs.dll MiniDump ; protection : Credential Guard, PPL/RunAsPPL). Les **Group Policy Preferences** (cpassword — mots de passe chiffrés en AES-256 avec une clé publiée par Microsoft → déchiffrement trivial ; corrigé par MS14-025 mais les GPP historiques restent souvent en place).

---

#### Chapitre 8 — AD CS : PKI interne, certificats et surface d'attaque

*AD CS est devenu l'un des vecteurs d'attaque les plus exploités — les vulnérabilités ESC transforment une PKI interne en machine à fabriquer des Domain Admin.*

L'architecture AD CS : CA racine (idéalement hors ligne), CA subordonnée (en ligne, émet les certificats), templates de certificats (définissent ce que le certificat autorise et qui peut le demander), enrollment (demande automatique ou manuelle), et auto-enrollment (les machines reçoivent automatiquement leurs certificats). Usages légitimes : certificats machines pour 802.1X, certificats VPN, certificats SSL internes, authentification par certificat (PKINIT/smart card).

Les **vulnérabilités ESC** (Escalation via Certificate Services — documentées par SpecterOps) : **ESC1** (le template permet au demandeur de spécifier un SAN arbitraire → demander un certificat au nom d'un Domain Admin ; conditions : Client Authentication + CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT + permissions d'enrollment pour les utilisateurs), **ESC2** (le template permet « Any Purpose » ou « SubCA » → certificat utilisable pour tout), **ESC3** (un agent d'enrollment peut demander des certificats au nom d'autres utilisateurs), **ESC4** (les ACL du template sont trop permissives → un utilisateur peut modifier le template pour le rendre ESC1), **ESC6** (le flag EDITF_ATTRIBUTESUBJECTALTNAME2 est activé sur la CA → tout template devient ESC1), **ESC7** (un utilisateur a le droit ManageCA → peut activer le flag ESC6), **ESC8** (le web enrollment est en HTTP sans EPA → NTLM relay vers le web enrollment → certificat au nom de n'importe qui).

Outils : **Certify** (C# — énumération et exploitation), **Certipy** (Python — énumération, exploitation, et extraction de certificats). Hardening AD CS : auditer les templates (Invoke-PKIAudit, Certipy find), supprimer les SAN libres (CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT), restreindre les permissions d'enrollment, désactiver « Any Purpose », activer HTTPS + EPA sur le web enrollment, et surveiller les enrollments (Event 4887).

> **🔴 KERBEROS — Épisode 3**
>
> Thomas lance Certipy contre Meridian : `certipy find -u t.granier@meridian.local -p '...' -dc-ip 10.0.1.10`. Résultat : ESC1 sur le template « VPN-User » — Client Authentication activé, CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT activé, et l'enrollment est autorisé pour « Authenticated Users ». Thomas demande un certificat avec le SAN de l'admin DA admin.ssi@meridian.local. Le certificat est émis en 3 secondes. Il utilise PKINIT pour obtenir un TGT de Domain Admin. L'ensemble de l'attaque a pris 90 secondes depuis la découverte du template vulnérable. La Blue Team n'a rien vu — les logs AD CS n'étaient pas centralisés vers le SIEM.

---

### PARTIE III — ADMINISTRATION ET CONTRÔLE

---

#### Chapitre 9 — Group Policy (GPO) : configuration et sécurité

Les GPO sont des ensembles de paramètres appliqués aux utilisateurs et machines d'une OU. L'ordre d'application : **LSDOU** (Local → Site → Domain → OU — le dernier appliqué gagne, sauf « Enforced »). Le filtrage de sécurité (appliquer une GPO uniquement à certains groupes). Les GPO de sécurité essentielles : politique de mots de passe (longueur, complexité, historique, verrouillage), audit policy (Advanced Audit Policy — activer les bons Event IDs), restriction d'exécution (AppLocker/WDAC), Windows Firewall, PowerShell logging (Script Block + Module Logging).

Les GPO comme vecteur d'attaque : un attaquant qui a WriteDACL sur une GPO peut ajouter un scheduled task ou un script de login → exécution de code sur toutes les machines de l'OU liée. SYSVOL contient les GPO (\\domain\SYSVOL\domain\Policies\{GUID}) et NETLOGON contient les scripts de login — les deux sont accessibles en lecture par tous les utilisateurs du domaine.

---

#### Chapitre 10 — Outils d'administration et requêtage

Les outils natifs (ADUC, GPMC, DNS Manager, AD Sites and Services). **PowerShell AD module** (Get-ADUser, Get-ADGroup, Get-ADComputer, Get-ADObject, Set-ADUser — les cmdlets essentielles). Les requêtes LDAP pour l'audit sécurité : comptes inactifs > 90j, mots de passe qui n'expirent jamais, comptes avec SPN (surface Kerberoasting), comptes sans pré-auth (AS-REP Roasting), unconstrained delegation, comptes avec adminCount=1. Les outils d'audit : **PingCastle** (score de maturité AD — 0 à 100, avec recommandations priorisées), **BloodHound** (analyse de chemins d'attaque — traité en profondeur au Ch.14), **Purple Knight** (audit Semperis), **ADRecon** (collecte structurée d'informations AD).

---

#### Chapitre 11 — Tiering model et séparation des privilèges

Le principe : séparer les environnements en tiers de criticité pour empêcher le mouvement latéral vertical. **Tier 0** (DC, comptes Domain Admin, Enterprise Admin, AD CS, Azure AD Connect — zone la plus protégée : isolation réseau, PAW obligatoire, aucun accès internet, monitoring maximal). **Tier 1** (serveurs membres, comptes admin serveur — les admins Tier 1 ne se connectent JAMAIS à un DC ni à un poste Tier 2). **Tier 2** (postes de travail, comptes utilisateurs).

La **PAW** (Privileged Access Workstation — poste durci dédié à l'administration, sans internet, sans email, sans navigation). **LAPS** (Local Administrator Password Solution — mot de passe admin local unique et roté sur chaque machine, stocké dans AD). La réalité du terrain : le tiering complet est difficile — commencer par protéger le Tier 0 (séparer les comptes DA, interdire les connexions DA sur les postes, déployer LAPS).

---

#### Chapitre 12 — Journalisation et audit AD

L'**Advanced Audit Policy** à activer sur tous les DC (Account Logon, Logon/Logoff, Object Access, DS Access, Policy Change, Account Management). Les **Event IDs critiques** : 4624 (logon succès), 4625 (logon échec), 4648 (explicit credentials), 4672 (special privileges), 4720 (account created), 4728/4732/4756 (member added to group), 4769 (TGS request), 4768 (TGT request), 5136 (directory object modified), 4662 (directory service access), 4887 (certificate enrollment). **Sysmon** sur les DC (Event 1 process creation, 3 network connection, 10 process access → lsass.exe, 13 registry). **PowerShell logging** (Script Block — Event 4104, Module Logging). La **centralisation** (WEF ou agent SIEM — les logs locaux sont effacés par l'attaquant). Le volume (des milliers d'événements/heure par DC — filtrage et priorisation essentiels).

---

### PARTIE IV — ATTAQUES AD

*Comprendre comment AD est attaqué pour mieux défendre — chaque technique avec mécanisme, outils, preuves et détection.*

---

#### Chapitre 13 — Reconnaissance et énumération

Tout utilisateur du domaine peut énumérer l'intégralité de l'AD via LDAP. Les outils : **BloodHound/SharpHound** (collecte et analyse de chemins d'attaque — traité en détail au Ch.14), **ADRecon** (collecte structurée), **PowerView** (énumération PowerShell — Get-DomainUser, Get-DomainGroup, Get-DomainComputer, Find-LocalAdminAccess), **ldapsearch** (requêtes LDAP depuis Linux), **Enum4linux** (énumération SMB/RPC).

Ce que l'attaquant cherche en priorité : comptes avec SPN → Kerberoasting surface, comptes sans pré-auth → AS-REP Roasting, comptes avec unconstrained delegation → cible de coercion, groupes privilégiés et leurs membres (Domain Admins, Enterprise Admins — combien de DA ? des comptes de service DA ?), ACLs permissives sur les objets critiques (GenericAll, WriteDACL), GPOs modifiables, trusts entre domaines/forêts, machines avec des sessions admin actives (Find-DomainUserLocation), et le RODC (PRP — quels comptes sont cachés ?).

> **🔴 KERBEROS — Épisode 4**
>
> Thomas lance SharpHound en mode « All » — en 90 secondes, il a le graphe complet de Meridian : 47 chemins vers Domain Admin, 12 comptes avec SPN dont 8 avec des mots de passe > 3 ans, 1 serveur avec unconstrained delegation (SRV-PRINT01), et le RODC de Genève dont la PRP inclut 45 comptes — dont 3 comptes de service Tier 1.

---

#### Chapitre 14 — BloodHound et analyse de chemins d'attaque

*L'outil qui a transformé la sécurité AD — il rend visible ce qui était invisible.*

Le concept : modéliser l'AD comme un graphe (les nœuds = objets AD, les arêtes = relations/droits) et trouver les chemins du compte compromis au Domain Admin. La collecte **SharpHound** (modes : Default — sessions + groupes + ACLs, All — tout, DCOnly — uniquement les données du DC ; les données collectées : sessions actives, appartenances aux groupes, ACLs, trusts, SPNs, délégation). L'analyse : **shortest paths** vers Domain Admin, shortest paths depuis les comptes « owned », **nœuds de convergence** (les objets par lesquels passent le plus de chemins — les couper ferme le plus de chemins), et les droits dangereux visualisés (GenericAll, WriteDACL, ForceChangePassword, AddMember, ReadLAPSPassword).

L'**utilisation défensive** : lancer BloodHound sur son propre AD pour identifier les chemins AVANT l'attaquant, supprimer les ACLs inutiles, couper les chemins critiques (remédier un seul nœud de convergence peut fermer 30 chemins), et valider après remédiation. **BloodHound CE** (Community Edition — version moderne, interface web, API, stockage Neo4j). Fil rouge : Thomas analyse le graphe de Meridian — un chemin passe par svc_monitoring (compte de service avec GenericWrite sur le groupe « IT-Admins » qui a WriteDACL sur le DC). La Blue Team n'avait jamais vu ce chemin.

---

#### Chapitre 15 — Credential attacks : Kerberoasting, AS-REP, relay et coercion

**Kerberoasting** : tout utilisateur demande un TGS pour un SPN → le ticket est chiffré avec le hash du compte de service → crack offline (hashcat -m 13100, john). Cible : comptes de service avec SPN et mot de passe faible. Outils : Rubeus kerberoast, GetUserSPNs.py. Défense : gMSA (mot de passe 240 caractères roté automatiquement), AES au lieu de RC4, comptes de service avec mots de passe forts (25+ caractères).

**AS-REP Roasting** : comptes avec DONT_REQUIRE_PREAUTH → l'AS-REP contient des données chiffrées avec le hash du compte → crack offline. Outils : Rubeus asreproast, GetNPUsers.py. Défense : activer la pré-auth sur tous les comptes (aucune raison de la désactiver sauf cas exceptionnel documenté).

**Password Spraying** : tester 1-2 mots de passe communs contre tous les comptes — sous le seuil de verrouillage. Outils : Spray, DomainPasswordSpray. Détection : 4625 en volume, 4771 KDC_ERR_PREAUTH_FAILED.

**NTLM Relay** : intercepter une authentification NTLM et la relayer vers un autre service — l'attaquant agit au nom de la victime. Chaîne typique : coercion ou Responder → ntlmrelayx → cible (LDAP pour DCSync/RBCD abuse, AD CS web enrollment pour ESC8, SMB pour exécution de code). Les **coercions** (forcer une machine à s'authentifier vers l'attaquant) : **PetitPotam** (abus EFS RPC — le DC s'authentifie vers l'attaquant → relay vers LDAP → DCSync), **PrinterBug/SpoolSample** (abus du spooler d'impression), **DFSCoerce** (abus DFS). Les coercions de DC sont les plus dangereuses. Défenses : SMB signing obligatoire, LDAP signing + channel binding, EPA sur IIS et AD CS, désactiver le spooler sur les DC, patcher PetitPotam.

---

#### Chapitre 16 — Mouvement latéral, escalade et ACL abuse

**Pass-the-Hash** (utiliser un hash NTLM volé pour s'authentifier — fonctionne car NTLM ne vérifie pas le mot de passe mais le hash ; outils : Mimikatz sekurlsa::pth, Impacket psexec/wmiexec/smbexec ; détection : 4624 logon type 3/9 avec processus inhabituel). **Pass-the-Ticket** (utiliser un ticket Kerberos volé ; outils : Mimikatz sekurlsa::tickets, Rubeus). **Overpass-the-Hash** (convertir un hash NTLM en ticket Kerberos — plus discret).

**ACL Abuse** : GenericAll sur un utilisateur → réinitialiser son mot de passe, GenericAll sur un groupe → s'ajouter comme membre, WriteDACL → modifier les ACL pour s'accorder des droits, WriteOwner → prendre la propriété, ForceChangePassword → changer le mot de passe, AddSelf/AddMember → s'ajouter à un groupe, GenericWrite sur un compte → modifier le SPN (targeted Kerberoasting) ou modifier msDS-KeyCredentialLink (Shadow Credentials — voir ci-dessous). Outils : PowerView (Add-DomainObjectAcl), BloodHound (visualisation), Impacket dacledit. Détection : Event 5136 sur objets sensibles, 4662.

**Shadow Credentials** : l'attaquant qui a GenericWrite ou WriteDACL sur un compte utilisateur ou machine peut modifier l'attribut **msDS-KeyCredentialLink** pour ajouter une clé publique qu'il contrôle. Ensuite, il utilise PKINIT pour s'authentifier en tant que ce compte sans connaître son mot de passe — en obtenant un TGT via le certificat associé à la clé. L'attaque est puissante car elle ne modifie pas le mot de passe du compte (moins de bruit), elle fonctionne avec PKINIT (Kerberos, pas NTLM), et elle est persistante tant que la clé n'est pas supprimée de l'attribut. Outils : **Whisker** (C# — ajout de la clé), **pywhisker** (Python), puis **Rubeus** (obtention du TGT via PKINIT). Pré-requis : AD CS déployé avec au moins un DC qui supporte PKINIT, et GenericWrite/WriteDACL sur le compte cible. Détection : Event 5136 sur l'attribut msDS-KeyCredentialLink, Event 4768 avec certificat (pré-auth type 16). Défense : auditer les modifications de msDS-KeyCredentialLink, restreindre les ACL (qui a GenericWrite sur les comptes critiques ?), monitorer les authentifications PKINIT depuis des sources inhabituelles.

Les techniques d'exécution à distance : PsExec (crée un service temporaire — Event 7045), WMI (Event 4688 + wmiprvse.exe), WinRM/PowerShell Remoting (Event 4624 logon type 3 + 4688 wsmprovhost.exe), DCOM, schtasks (tâche planifiée à distance). Chaque technique a un profil de détection différent.

---

#### Chapitre 17 — Persistence : Golden Ticket, Shadow Credentials et au-delà

**Golden Ticket** (forger un TGT avec le hash krbtgt → accès illimité, durée arbitraire ; fonctionne même après reset de tous les mots de passe — tant que krbtgt n'est pas roté ; détection : TGT avec durée anormale, SID inexistant, absence d'AS-REQ correspondant). **Silver Ticket** (forger un Service Ticket avec le hash d'un compte de service → accès au service ciblé sans passer par le KDC ; plus discret — pas de TGS-REQ ; détection : PAC validation, ticket sans TGS-REQ). **DCSync** (simuler un DC pour demander la réplication des hashes — droits requis : DS-Replication-Get-Changes + DS-Replication-Get-Changes-All ; outils : Mimikatz lsadump::dcsync, Impacket secretsdump ; détection : Event 4662 avec droits de réplication depuis une machine non-DC = alerte critique).

**Shadow Credentials comme persistence** : l'attaquant qui a déjà compromis un compte DA peut ajouter une clé dans msDS-KeyCredentialLink d'un compte machine (DC par exemple) et maintenir un accès persistant via PKINIT, même après rotation du mot de passe du compte. Combiné avec un UnPAC-the-Hash (obtenir le hash NTLM du compte via le TGT PKINIT), cette persistence survit aux rotations de mots de passe classiques.

**Golden Certificate** (compromettre la clé privée de la CA → forger des certificats pour n'importe quel utilisateur → persistence tant que la CA n'est pas reconstruite ; c'est la persistence la plus durable — la clé privée de la CA a une durée de vie de 5-20 ans). **AdminSDHolder Persistence** (modifier les ACL d'AdminSDHolder → SDProp réapplique automatiquement les ACL sur tous les comptes adminCount=1 toutes les 60 min). **Skeleton Key** (injection dans lsass sur le DC — mot de passe « maître » pour tous les comptes ; survit au reboot uniquement si persistance via patch). **DCShadow** (enregistrer un faux DC pour pousser des modifications via la réplication — extrêmement discret ; détection : objets nTDSDSA inhabituels).

---

#### Chapitre 18 — Kill chain AD typique : du phishing au Domain Admin

Scénario réaliste complet en 8 étapes : (1) Phishing → accès initial (C2), (2) Reconnaissance AD (SharpHound — 47 chemins vers DA), (3) Kerberoasting du compte svc_backup (mot de passe : Backup2019!), (4) Mouvement latéral (WMI vers SRV-APP01 avec les credentials svc_backup — admin local), (5) Credential dumping (Mimikatz sur SRV-APP01 → hash de bob.admin — Domain Admin qui avait une session active sur ce serveur Tier 1 — violation de tiering), (6) Pass-the-Hash vers le DC avec le hash de bob.admin, (7) DCSync (extraction de tous les hashes y compris krbtgt), (8) Golden Ticket + Golden Certificate pour la persistence.

Mapping MITRE ATT&CK complet. Temps réel observé : quelques heures dans un environnement peu durci — 30 minutes dans les cas les plus rapides. Où la défense aurait pu stopper la chaîne : gMSA pour svc_backup (Kerberoasting impossible), LAPS (admin local unique par machine), Credential Guard (Mimikatz bloqué), tiering (bob.admin ne devrait pas avoir de session Tier 1), détection DCSync (Event 4662), rotation krbtgt (invalide le Golden Ticket), audit AD CS (Golden Certificate détecté).

Fil rouge : Thomas réalise 2 kill chains sur Meridian — chemin 1 (classique : Kerberoasting → PtH → DCSync) et chemin 2 (AD CS : ESC1 → certificat DA → PKINIT → TGT DA). La Blue Team détecte le chemin 1 (alert sur le Kerberoasting — volume anormal de 4769 RC4) mais manque le chemin 2 (logs AD CS non centralisés).

---

### PARTIE V — DÉTECTION

---

#### Chapitre 19 — Minimum Viable Visibility : la télémétrie indispensable

Les 10 sources à activer et centraliser (par priorité) : (1) Security logs sur tous les DC (Advanced Audit Policy), (2) Directory Service Changes (Event 5136), (3) PowerShell ScriptBlock Logging + Module Logging, (4) Sysmon sur DC et Tier 0/1, (5) LDAP query logging (Event 1644), (6) Logs Kerberos détaillés (4768/4769/4771), (7) WEF ou agent SIEM vers centralisation, (8) EDR sur DC et PAW, (9) Logs AD CS (enrollment, modifications templates — Event 4887), (10) DNS query logging sur les DC DNS-intégrés. Sans cette télémétrie, même le meilleur SOC est aveugle sur AD.

---

#### Chapitre 20 — Détecter les attaques AD dans le SIEM

Pour chaque technique, le triptyque : signal compatible + corrélation nécessaire + faux positifs courants. **Kerberoasting** (4769 RC4 en volume → vérifier la baseline du compte, l'encryption demandée). **AS-REP Roasting** (4768 sans pré-auth → lister les comptes DONT_REQUIRE_PREAUTH). **DCSync** (4662 avec droits de réplication depuis non-DC = alerte critique → vérifier : la machine source est-elle un DC connu ?). **Pass-the-Hash** (4624 logon type 3/9 avec processus source inhabituel → violation de tiering ?). **Golden Ticket** (TGT avec durée anormale, SID inexistant, absence d'AS-REQ). **Modifications ACL suspectes** (5136 sur objets sensibles — AdminSDHolder, GPOs, comptes DA). **Accès lsass** (Sysmon Event 10 ProcessAccess ciblant lsass.exe → processus source légitime ou suspect ?). **Password Spraying** (4625 en volume, 4771). **AD CS abuse** (4887 — enrollment avec SAN inhabituel, template sensible). **Shadow Credentials** (5136 sur msDS-KeyCredentialLink → qui a modifié cet attribut ? depuis quelle machine ?).

Un Event ID = un indice, pas une preuve. Chaque signal doit être évalué avec son contexte et comparé à une baseline.

---

#### Chapitre 21 — Deception et honey objects

**Honey accounts** (comptes factices avec des attributs attractifs — adminCount=1, SPN, vieux mot de passe → toute interaction = alerte, zéro faux positif). **Honey SPNs** (SPNs factices sur des comptes pièges → Kerberoasting détecté immédiatement). **Honey tokens** (credentials factices sur des machines — fichiers, registre, mémoire → credential dumping détecté). **Canary files** (fichiers pièges sur des partages → énumération/exfiltration détectée). L'avantage de la deception : zéro faux positif — si un honey object est touché, c'est forcément suspect.

> **🔵 KERBEROS — Épisode 5 (Blue Team)**
>
> La Blue Team de Meridian n'avait pas déployé de honey objects. Après le pentest de Thomas, elle déploie : 1 honey account « svc_legacy » avec adminCount=1 et un SPN attractif (MSSQLSvc/legacy-db.meridian.local), 2 canary files « salaries_2025.xlsx » et « passwords.xlsx » sur un partage accessible, et des honey tokens (credentials factices) dans le registre du serveur SRV-APP01. Au prochain test, le premier Kerberoasting sur svc_legacy déclenche une alerte immédiate.

---

#### Chapitre 22 — Règles SIEM et corrélation avancée

Les règles de corrélation multi-événements : **Kerberoasting avancé** (4769 RC4 + volume > seuil + pas dans la baseline = alerte haute), **mouvement latéral via tiering** (4624 logon type 3/10 + compte admin + machine Tier 2 + destination Tier 0 = violation de tiering = alerte critique), **persistence** (5136 modification AdminSDHolder/GPO + hors fenêtre de maintenance + compte non autorisé = alerte haute), **AD CS abuse** (4887 enrollment + template sensible + SAN ≠ demandeur = alerte critique), **Shadow Credentials** (5136 msDS-KeyCredentialLink + compte non attendu = alerte haute).

Réduction des faux positifs : baseline essentielle (whitelister les comptes de service légitimes, documenter les comportements attendus, tuner progressivement). Les **règles Sigma** (format portable de détection — convertibles en Splunk SPL, ELK KQL, Sentinel KQL — la communauté maintient un large set de règles AD).

---

### PARTIE VI — HARDENING

---

#### Chapitre 23 — Top 10 actions de hardening et quick wins

Par où commencer quand le temps et le budget sont limités. Les 10 actions par impact décroissant : (1) Activer Advanced Audit Policy sur tous les DC (visibilité), (2) Déployer LAPS sur tout le parc (supprime le PtH via admin local), (3) Séparer les comptes admin/user (pas de DA sur les postes), (4) Activer SMB signing obligatoire (bloque le relay), (5) Désactiver LLMNR et NBT-NS (bloque le poisoning Responder), (6) Rotater le krbtgt (double rotation — invalide tout Golden Ticket), (7) Auditer les ACLs avec BloodHound (identifier et couper les chemins), (8) Supprimer les comptes inactifs et SPNs inutiles (réduire la surface), (9) Activer Protected Users pour les comptes Tier 0 (protection renforcée), (10) Durcir les templates AD CS (bloquer ESC1-ESC8).

---

#### Chapitre 24 — Hardening NTLM, Kerberos et authentification

Désactivation progressive de NTLM (audit d'abord : Network security: Restrict NTLM: Audit pour identifier les applications qui utilisent NTLM → corriger ou documenter les exceptions → puis restreindre par GPO). SMB signing obligatoire (GPO : Microsoft network server/client: Digitally sign communications always). LDAP signing et channel binding (bloque le relay LDAP — LDAP server signing requirements = Require signing). EPA (Extended Protection for Authentication — IIS, AD CS web enrollment). **Protected Users** (les membres ne peuvent pas : utiliser NTLM, être délégués, cacher les credentials, utiliser DES/RC4 pour Kerberos, avoir des TGT > 4h). **Credential Guard** (isolation de lsass dans un environnement virtuel via Hyper-V — empêche Mimikatz). PPL/RunAsPPL (protège lsass contre les injections — moins contraignant que Credential Guard mais contournable). FGPP (Fine-Grained Password Policy — politique différenciée : mots de passe longs pour les comptes de service, MFA pour les admins).

---

#### Chapitre 25 — Hardening AD CS, GPO et Tier 0

**AD CS hardening** : auditer les templates (Certipy find, Invoke-PKIAudit — supprimer les SAN libres, restreindre enrollment, désactiver « Any Purpose »), activer HTTPS + EPA sur le web enrollment, CA racine hors ligne, surveiller les enrollments (Event 4887 centralisé), et auditer msDS-KeyCredentialLink (Shadow Credentials). **GPO hardening** : restreindre qui peut créer/modifier les GPO, auditer les modifications (5136), verrouiller les GPO critiques. **Tier 0 hardening** : DC sans accès internet, sans agent superflu, sans logiciel tiers, pas de compte de service non-gMSA, VLAN dédié, PAW obligatoire, monitoring maximal. **RODC hardening** : PRP minimale (seuls les comptes strictement nécessaires), pas de comptes privilégiés dans la PRP, auditer régulièrement les comptes cachés, surveiller les tentatives de réplication depuis le RODC.

> **🔴 KERBEROS — Épisode 6**
>
> Thomas teste le RODC de Genève. La PRP inclut 45 comptes dont 3 comptes de service Tier 1 — c'est trop large. Il compromet le RODC (accès physique simulé — le RODC est dans un local technique sans contrôle d'accès) et extrait les hashes des 45 comptes cachés. Parmi eux, svc_monitoring a GenericWrite sur un groupe IT — un chemin vers l'escalade. Le RODC, censé limiter l'exposition, a été configuré trop permissivement et devient un vecteur d'attaque. Recommandation : PRP réduite aux comptes strictement nécessaires pour le site (utilisateurs de Genève uniquement, pas de comptes de service Tier 1), et sécurisation physique du local.

---

#### Chapitre 26 — Backup, restore et résilience AD

Pourquoi les backups AD sont critiques (un AD compromis sans backup sain = reconstruction from scratch = semaines d'arrêt). Les méthodes : **System State backup** (NTDS.dit, registre, SYSVOL, boot files — via Windows Server Backup, Veeam, ou outil spécialisé). La récupération : **authoritative restore** (restaurer un objet supprimé en le marquant comme autoritaire → la réplication le propage), **non-authoritative restore** (restaurer un DC et le laisser se re-synchroniser avec les autres DC), **bare metal restore** (reconstruire un DC from scratch à partir du backup). La **Corbeille AD** (Active Directory Recycle Bin — récupération d'objets supprimés pendant la durée de rétention — à activer impérativement). Les tests de restauration (tester régulièrement — la première fois ne doit PAS être le jour de l'incident). La réplication comme résilience (2 DC minimum, sur des sites différents).

---

### PARTIE VII — INCIDENT RESPONSE, HYBRID IDENTITY ET SYNTHÈSE

---

#### Chapitre 27 — Incident Response AD : méthodologie

Le scénario type (« l'EDR a détecté Mimikatz sur un serveur, l'attaquant semble avoir des credentials DA, des modifications ACL suspectes ont été détectées »). Le **triage** : quels comptes compromis ? (logs 4624, 4648, 4672), quels systèmes touchés ? (DC, serveurs, postes — signes de mouvement latéral ?), le Tier 0 est-il compromis ? (si un DC ou un DA est touché → scope maximal), depuis quand ? (date de première activité suspecte), y a-t-il de la persistence ? (Golden Ticket, ACL modifiées, GPO modifiées, comptes créés, certificats AD CS émis, Shadow Credentials ajoutées). Règle d'or : supposer le pire et vérifier.

---

#### Chapitre 28 — Containment, nettoyage et rotation krbtgt

Le **containment** : isoler les systèmes compromis (couper le réseau, ne PAS éteindre — préserver la mémoire), désactiver les comptes compromis (pas supprimer), révoquer les sessions (klist purge ou rotation krbtgt si Golden Ticket suspecté), bloquer les IOCs, protéger les backups. La **rotation krbtgt** (double rotation espacée : 1ère rotation → attendre 10-12h → 2ème rotation → l'ancien hash est complètement invalidé ; ne PAS faire les deux simultanément — casse toutes les sessions).

Le **nettoyage de persistence** : comptes créés (4720 → supprimer), ACLs modifiées (comparer avec baseline → révoquer), GPOs modifiées (5136 → restaurer), SPNs ajoutés (supprimer), AdminSDHolder (nettoyer les ACEs), certificats AD CS (révoquer les certificats suspects), DCShadow (vérifier les objets nTDSDSA), Shadow Credentials (vérifier msDS-KeyCredentialLink sur les comptes sensibles — supprimer les clés non légitimes), Scheduled Tasks/Services (vérifier sur chaque DC et serveur touché).

---

#### Chapitre 29 — Rebuild vs Clean et retour à la normale

Les critères : scope limité + durée courte + backups sains → clean ; Tier 0 compromis + durée longue/inconnue + pas de backup → rebuild. Le processus de rebuild (nouveaux DC, nouvelle forêt, migration — long et douloureux mais parfois nécessaire). La validation post-incident (PingCastle/BloodHound — chemins fermés ?, scanner les comptes à risque, vérifier les ACLs, confirmer la rotation krbtgt, vérifier les templates AD CS, auditer msDS-KeyCredentialLink). Le retex (timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné/échoué, actions d'amélioration).

---

#### Chapitre 30 — Entra ID / Hybrid : architecture et synchronisation

**Entra ID** (ex-Azure AD) : tenant plat (pas de forêt/domaine), protocoles OAuth 2.0/OIDC/SAML, Conditional Access au lieu de GPO, Intune au lieu de SCCM. La synchronisation **Azure AD Connect / Entra Connect** : 3 méthodes. **PHS** (Password Hash Sync — les hashes sont synchronisés vers le cloud ; le plus courant ; risque : si Entra ID est compromis, les hashes sont exposés). **PTA** (Pass-Through Auth — l'auth cloud est validée en temps réel par un agent on-prem ; l'agent PTA est Tier 0). **Federation/ADFS** (un serveur ADFS émet des tokens pour le cloud ; ADFS est Tier 0 — si compromis : Golden SAML).

**Azure AD Connect = Tier 0** — le serveur a accès aux credentials de TOUS les comptes synchronisés. Isolation, pas d'internet, accès restreint, monitoring. Les erreurs courantes : serveur AD Connect non isolé, pas dans le Tier 0, sans EDR, synchronisation de comptes DA vers le cloud, pas de filtering (tous les comptes synchronisés y compris les comptes de service).

---

#### Chapitre 31 — Attaques et défense du cloud identity

Les attaques hybrid/cloud : **Token theft** (voler un access/refresh token → accès aux applications cloud sans MFA), **PRT theft** (Primary Refresh Token — le « TGT du cloud » ; vol via Mimikatz, ROADtools → SSO complet à toutes les apps Entra ID), **Consent phishing** (tromper un utilisateur pour autoriser une app malveillante → lecture emails, fichiers via Graph API), **Golden SAML** (forger des tokens SAML avec le certificat de signing ADFS → accès à toutes les apps fédérées — APT29/SolarWinds), **Azure AD backdoors** (service principals, credentials sur des apps, rôles persistants).

**Conditional Access Policies** (MFA obligatoire pour tous les admins, bloquer les connexions depuis des pays inhabituels, exiger un appareil conforme Intune, bloquer les protocoles legacy — SMTP auth, POP3, IMAP). **PIM** (Privileged Identity Management — activation temporaire JIT des rôles admin, approbation, justification, audit complet). Logs et détection cloud (Sign-in logs, Audit logs, Risky sign-ins — Entra ID Protection, Provisioning logs, MS Sentinel/Defender).

---

#### Chapitre 32 — Cas de synthèse : rapport de pentest AD complet

Synthèse du fil rouge KERBEROS. Le rapport de pentest de Thomas sur Meridian Pharma.

**Résumé exécutif** (pour la direction — score PingCastle : 73/100, Domain Admin atteint en 4 heures par 2 chemins indépendants, recommandations critiques : 5 actions P0 pour réduire le risque de 80 %).

**Findings classés par criticité :**

**Critique :** ESC1 sur template VPN-User (Domain Admin en 90 secondes via AD CS), krbtgt jamais roté depuis 7 ans, 3 comptes DA avec sessions actives sur des serveurs Tier 1 (violation de tiering), Azure AD Connect non isolé avec accès internet, RODC Genève avec PRP trop large (45 comptes dont 3 comptes de service Tier 1).

**Élevé :** 12 comptes de service avec SPN et mot de passe > 3 ans (Kerberoasting surface), LLMNR/NBT-NS actifs (4 hashes capturés en 15 min), pas de Credential Guard (Mimikatz fonctionnel), pas de SMB signing (relay possible), svc_monitoring avec GenericWrite sur le groupe IT-Admins → chemin vers DA via ACL abuse.

**Moyen :** 47 comptes inactifs > 180 jours, 3 GPO modifiables par des utilisateurs non privilégiés, NTLM non restreint, pas de honey objects, logs AD CS non centralisés (la kill chain AD CS est passée inaperçue), msDS-KeyCredentialLink non monitoré.

**Kill chains documentées :** Chemin 1 (Responder → hash capture → Kerberoasting svc_backup → mouvement latéral SRV-APP01 → credential dumping → PtH vers DC → DCSync). Chemin 2 (Certipy ESC1 → certificat DA → PKINIT → TGT DA → DCSync). Chemin 3 (RODC Genève → PRP trop large → hash svc_monitoring → GenericWrite → ACL abuse → DA).

**Recommandations priorisées :** P0 immédiat (corriger ESC1, rotater krbtgt double rotation, séparer les comptes DA des serveurs Tier 1, isoler Azure AD Connect, réduire la PRP du RODC), P1 3 mois (déployer LAPS, gMSA pour les comptes de service, désactiver LLMNR/NBT-NS, SMB signing, centraliser les logs AD CS, monitorer msDS-KeyCredentialLink), P2 6 mois (Credential Guard sur les serveurs Tier 0/1, tiering complet, déployer honey objects, restreindre NTLM, audit ACL complet et remédiation BloodHound). Risques résiduels acceptés : 2 applications legacy nécessitant NTLM (compensatoire : monitoring renforcé + segmentation).

---

### ANNEXES

---

#### Annexe A — Cheat Sheet AD

##### Commandes PowerShell AD essentielles

```powershell
# --- UTILISATEURS ---
Get-ADUser -Identity alice -Properties *                    # Tout sur un user
Get-ADUser -Filter {Enabled -eq $true} -Properties lastLogonTimestamp  # Users actifs
Get-ADUser -Filter {adminCount -eq 1}                       # Comptes avec adminCount=1
Search-ADAccount -LockedOut                                  # Comptes verrouillés
Search-ADAccount -PasswordNeverExpires                       # MdP n'expire jamais
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00     # Inactifs 90j
Get-ADUser krbtgt -Properties PasswordLastSet                # Dernière rotation krbtgt

# --- GROUPES ---
Get-ADGroupMember -Identity 'Domain Admins' -Recursive       # Membres DA (récursif)
Get-ADPrincipalGroupMembership -Identity alice               # Groupes d'un user
Get-ADGroup -Filter {adminCount -eq 1}                       # Groupes privilégiés

# --- SPN (Kerberoasting surface) ---
Get-ADUser -Filter {ServicePrincipalName -ne '$null'} -Properties ServicePrincipalName

# --- DELEGATION ---
Get-ADComputer -Filter {TrustedForDelegation -eq $true}      # Unconstrained
Get-ADComputer -Filter {msDS-AllowedToDelegateTo -ne '$null'} # Constrained

# --- TRUSTS ---
Get-ADTrust -Filter *                                        # Tous les trusts

# --- PRE-AUTH (AS-REP Roasting surface) ---
Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true}

# --- SHADOW CREDENTIALS ---
Get-ADUser -Filter {msDS-KeyCredentialLink -ne '$null'} -Properties msDS-KeyCredentialLink

# --- GPO ---
Get-GPO -All | Select DisplayName, ModificationTime
Get-GPResultantSetOfPolicy -ReportType Html -Path gpo.html

# --- RODC PRP ---
Get-ADDomainControllerPasswordReplicationPolicy -Identity RODC-GVA
```

##### Requêtes LDAP courantes

```
# Tous les utilisateurs avec adminCount=1
(&(objectClass=user)(adminCount=1))

# Comptes avec SPN (Kerberoasting)
(&(objectClass=user)(servicePrincipalName=*)(!(objectClass=computer)))

# Comptes sans pré-auth (AS-REP Roasting)
(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))

# Unconstrained delegation
(&(objectClass=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))

# Comptes avec msDS-KeyCredentialLink (Shadow Credentials)
(&(objectClass=user)(msDS-KeyCredentialLink=*))
```

---

#### Annexe B — Matrice Attaque / Détection / Remédiation

| Technique | Event IDs | Outils offensifs | Signal de détection | Faux positifs | Remédiation |
|-----------|-----------|-----------------|---------------------|---------------|-------------|
| Kerberoasting | 4769 | Rubeus, GetUserSPNs.py | Volume 4769 RC4 depuis un même compte | Monitoring légitime | gMSA, AES, MdP forts |
| AS-REP Roasting | 4768 | Rubeus, GetNPUsers.py | 4768 sans pré-auth | Comptes legacy | Activer pré-auth |
| Password Spraying | 4625, 4771 | Spray, DomainPasswordSpray | Volume 4625 même MdP | Oublis utilisateurs | Verrouillage, MFA |
| NTLM Relay | 4624 | ntlmrelayx, Responder | 4624 depuis source inhabituelle | Services légitimes | SMB/LDAP signing |
| PetitPotam | 4624 | PetitPotam.py | Auth DC vers machine non-DC | — | Patch, disable EFS RPC |
| Pass-the-Hash | 4624 (type 3/9) | Mimikatz, Impacket | Logon avec processus inhabituel | Admin légitime | Credential Guard, LAPS |
| DCSync | 4662 | Mimikatz, secretsdump | 4662 replication depuis non-DC | Backup légitime | Auditer droits replic. |
| Golden Ticket | — | Mimikatz | TGT durée anormale, SID inexistant | — | Rotation krbtgt |
| Silver Ticket | — | Mimikatz | Ticket sans TGS-REQ | — | PAC validation |
| Shadow Credentials | 5136 | Whisker, pywhisker | 5136 sur msDS-KeyCredentialLink | Windows Hello | Auditer ACLs, monitoring |
| ESC1 (AD CS) | 4887 | Certipy, Certify | Enrollment avec SAN ≠ demandeur | — | Supprimer SAN libre |
| ACL Abuse | 5136, 4662 | PowerView, BloodHound | Modification ACL sur objets sensibles | Admin changements | Audit BloodHound |
| AdminSDHolder | 5136 | PowerView | Modification AdminSDHolder | — | Monitoring dédié |
| DCShadow | 5137 | Mimikatz | Objet nTDSDSA inhabituel | — | Monitoring CN=Config |

---

#### Annexe C — Event IDs critiques AD

| Event ID | Source | Description | Pertinence sécurité |
|----------|--------|-------------|-------------------|
| 4624 | Security | Logon succès | Type 3/9/10 = réseau/credentials, source inhabituelle = PtH |
| 4625 | Security | Logon échec | Volume = brute force/spraying |
| 4648 | Security | Explicit credentials | Utilisation de credentials différentes = mouvement latéral |
| 4662 | Security | Directory service access | Droits de réplication depuis non-DC = DCSync |
| 4672 | Security | Special privileges assigned | Nouveaux privilèges = escalade potentielle |
| 4720 | Security | Account created | Compte créé par l'attaquant ? |
| 4728/4732/4756 | Security | Member added to group | Ajout à un groupe privilégié = alerte |
| 4768 | Security | TGT request | Sans pré-auth = AS-REP Roasting |
| 4769 | Security | TGS request | RC4 en volume = Kerberoasting |
| 4771 | Security | Kerberos pre-auth failed | Volume = spraying |
| 4887 | Security | Certificate enrollment | SAN inhabituel = ESC1 abuse |
| 5136 | Security | Directory object modified | AdminSDHolder, GPO, ACL, msDS-KeyCredentialLink |
| 5137 | Security | Directory object created | Objet nTDSDSA = DCShadow |
| 7045 | System | Service installed | PsExec crée un service temporaire |
| 1 | Sysmon | Process creation | Mimikatz, Rubeus, SharpHound, PsExec |
| 3 | Sysmon | Network connection | C2 beaconing, mouvement latéral |
| 10 | Sysmon | Process access | lsass.exe access = credential dumping |
| 4104 | PowerShell | Script Block | PowerShell offensif = PowerView, etc. |

---

#### Annexe D — Lab AD : monter son environnement de test

**Infrastructure minimale** : 1 VM Windows Server 2022 (DC01 — DC + DNS + AD CS), 1 VM Windows Server 2022 (SRV01 — serveur membre), 1 VM Windows 10/11 (PC01 — poste joint au domaine), 1 VM Kali Linux (attaquant). Total : ~16 Go RAM, 100 Go disque. Hyperviseur : VirtualBox, VMware Workstation, ou Proxmox.

**Configuration AD** : Promouvoir DC01 en DC (Install-WindowsFeature AD-Domain-Services + Install-ADDSForest), créer des OUs (IT, Finance, HR), créer des utilisateurs (dont au moins 1 DA, 1 compte de service avec SPN, 1 compte sans pré-auth), créer des groupes, joindre SRV01 et PC01 au domaine, déployer AD CS (Install-WindowsFeature ADCS-Cert-Authority + Install-AdcsCertificationAuthority), créer un template vulnérable ESC1, et configurer un trust (optionnel — 2ème forêt).

**Outils à installer** : Mimikatz, Rubeus, SharpHound/BloodHound CE, Certipy, Responder, Impacket, PowerView, PingCastle, Sysmon (avec config SwiftOnSecurity).

---

#### Annexe E — MITRE ATT&CK mapping AD

| Tactique | Techniques AD clés | Sub-techniques |
|----------|-------------------|---------------|
| Reconnaissance | T1087 Account Discovery | .002 Domain Account |
| | T1069 Permission Groups Discovery | .002 Domain Groups |
| Credential Access | T1558 Steal or Forge Kerberos Tickets | .003 Kerberoasting, .001 Golden Ticket |
| | T1003 OS Credential Dumping | .001 LSASS Memory, .003 NTDS, .006 DCSync |
| | T1557 Adversary-in-the-Middle | .001 LLMNR/NBT-NS Poisoning |
| Lateral Movement | T1550 Use Alternate Authentication | .002 Pass the Hash, .003 Pass the Ticket |
| | T1021 Remote Services | .002 SMB, .006 WinRM |
| Persistence | T1098 Account Manipulation | .xxx Shadow Credentials |
| | T1484 Domain Policy Modification | .001 Group Policy Modification |
| Privilege Escalation | T1078 Valid Accounts | .002 Domain Accounts |
| | T1134 Access Token Manipulation | |
| Defense Evasion | T1207 Rogue Domain Controller | DCShadow |

---

#### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Active Directory (ce cours) | **Ce cours (AD)** | — |
| Infrastructure IT | **Cours Infra** | AD (Ch.21 Infra — AD comme socle, vue d'ensemble) |
| Détection SOC | **Cours SOC** | AD (Ch.19-22 — détection AD spécifique, Event IDs) |
| Incident Response | **Cours IR** | AD (Ch.27-29 — IR spécifique AD, rotation krbtgt, rebuild) |
| APT | **Cours APT** | AD (Ch.18 kill chain — APT29 Golden SAML, Ch.31 cloud attacks) |
| Windows en profondeur | **Cours Windows** | AD (Ch.5-7 — NTLM/Kerberos/lsass, complémentaire) |
| GRC | **Cours GRC** | AD (Ch.11 tiering — le tiering est une mesure de gouvernance) |
| CTI | **Cours CTI** | AD (Ch.14 BloodHound — même logique d'analyse de graphe) |

---

#### Annexe G — Glossaire et ressources

##### Glossaire (sélection)

| Terme | Définition |
|-------|-----------|
| **ACE** | Access Control Entry — entrée de contrôle d'accès |
| **ACL** | Access Control List — liste de contrôle d'accès (DACL/SACL) |
| **AdminSDHolder** | Objet dont les ACL sont propagées aux comptes privilégiés |
| **AS-REP** | Authentication Service Reply — réponse du KDC avec le TGT |
| **BloodHound** | Outil d'analyse de chemins d'attaque AD par graphe |
| **Credential Guard** | Isolation de lsass via Hyper-V contre Mimikatz |
| **DCSync** | Simulation de réplication DC pour extraire les hashes |
| **DFSR** | Distributed File System Replication — réplication SYSVOL |
| **ESC1-ESC8** | Escalation via Certificate Services — vulnérabilités AD CS |
| **FGPP** | Fine-Grained Password Policy — politique MdP différenciée |
| **FSMO** | Flexible Single Master Operations — rôles spéciaux DC |
| **GC** | Global Catalog — DC avec copie partielle de toute la forêt |
| **gMSA** | Group Managed Service Account — compte de service sécurisé |
| **Golden Ticket** | TGT forgé avec le hash krbtgt → accès illimité |
| **GPO** | Group Policy Object — politique de configuration/sécurité |
| **KDC** | Key Distribution Center — service Kerberos sur le DC |
| **Kerberoasting** | Crack offline de tickets de service (TGS) |
| **krbtgt** | Compte qui chiffre tous les TGT — cible n°1 |
| **LAPS** | Local Administrator Password Solution |
| **NTDS.dit** | Base de données AD (hashes de tous les comptes) |
| **NTLM** | NT LAN Manager — protocole d'authentification legacy |
| **OU** | Organizational Unit — conteneur d'objets AD |
| **PAC** | Privilege Attribute Certificate — SID + groupes dans le ticket |
| **PAW** | Privileged Access Workstation — poste admin durci |
| **PKINIT** | Authentification Kerberos par certificat |
| **PRP** | Password Replication Policy — politique du RODC |
| **PRT** | Primary Refresh Token — « TGT du cloud » |
| **RBCD** | Resource-Based Constrained Delegation |
| **RODC** | Read-Only Domain Controller |
| **SDProp** | Processus qui propage les ACL d'AdminSDHolder |
| **Shadow Credentials** | Abus de msDS-KeyCredentialLink via PKINIT |
| **SID** | Security Identifier — identifiant unique d'un objet |
| **Silver Ticket** | Service Ticket forgé avec le hash du compte de service |
| **SPN** | Service Principal Name — identifie un service Kerberos |
| **SYSVOL** | Partage répliqué entre DC (GPO, scripts) |
| **TGT / TGS** | Ticket Granting Ticket / Ticket Granting Service |
| **Trust** | Relation de confiance entre domaines/forêts |

##### Ressources

| Ressource | Type | Focus |
|-----------|------|-------|
| harmj0y (blog) | Blog | Recherche offensive AD — BloodHound, Kerberos, AD CS |
| adsecurity.org (Sean Metcalf) | Blog | Défense AD — détection, hardening |
| thehacker.recipes | Wiki | Techniques d'attaque AD pas-à-pas |
| ired.team | Blog | Red team techniques avec exemples |
| SpecterOps (blog) | Blog | AD CS (ESC), BloodHound, recherche |
| The DFIR Report | Blog | Intrusions réelles analysées |
| PingCastle | Outil | Audit de maturité AD |
| BloodHound CE | Outil | Analyse de chemins d'attaque |

##### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| CRTP (Certified Red Team Professional) | Altered Security | Attaque AD |
| CRTE (Certified Red Team Expert) | Altered Security | Attaque AD avancé + forêts |
| SANS SEC560 | SANS | Pentest réseau + AD |
| SANS SEC566 | SANS | Hardening AD |
| HTB CPTS | HackTheBox | Pentest avancé (incluant AD) |
| HTB Dante/Offshore/Zephyr | HackTheBox | Pro Labs AD |

---

---

## Annexe — Questions types d'entretien et réponses types

### Questions essentielles

- **Question :** Qu'est-ce qu'Active Directory et pourquoi c'est la cible principale des attaquants ?
  - **Réponse type :** Active Directory est l'annuaire centralisé de Microsoft qui gère les identités, les authentifications et les politiques de sécurité dans plus de 90 % des entreprises. C'est la cible n°1 parce que compromettre AD donne accès à tout : tous les comptes, toutes les machines, toutes les données. Les composants AD — les contrôleurs de domaine, le krbtgt, les comptes Domain Admin — sont classés Tier 0, le niveau de criticité le plus élevé.

- **Question :** Expliquez le fonctionnement de Kerberos en quelques étapes.
  - **Réponse type :** L'utilisateur s'authentifie auprès du KDC (le DC) et obtient un TGT — c'est le ticket qui prouve son identité. Ensuite, quand il veut accéder à un service, il présente son TGT au KDC qui lui délivre un TGS (ticket de service) pour ce service précis. Le service valide le ticket et autorise l'accès. Tout repose sur le secret du compte krbtgt, qui chiffre les TGT. Si un attaquant obtient ce hash, il peut forger des Golden Tickets — des TGT illimités.

- **Question :** Qu'est-ce que le Kerberoasting et comment s'en protéger ?
  - **Réponse type :** Le Kerberoasting exploite le fait que tout utilisateur du domaine peut demander un ticket de service (TGS) pour n'importe quel SPN. Ce ticket est chiffré avec le hash du compte de service — si le mot de passe est faible, on le cracke en offline. La défense principale c'est d'utiliser des gMSA (Group Managed Service Accounts), qui ont des mots de passe de 240 caractères rotés automatiquement. Sinon, il faut des mots de passe de 25+ caractères sur les comptes de service et forcer l'AES au lieu de RC4.

- **Question :** Qu'est-ce que le tiering model et pourquoi c'est important ?
  - **Réponse type :** Le tiering sépare l'environnement en trois niveaux : Tier 0 pour les DC et comptes Domain Admin, Tier 1 pour les serveurs, Tier 2 pour les postes utilisateurs. L'idée c'est d'empêcher le mouvement latéral vertical — un admin ne doit jamais utiliser un compte Tier 0 pour se connecter à une machine Tier 1 ou 2. Si un attaquant compromet un poste et qu'un DA a une session active dessus, il récupère le hash et c'est terminé. Le tiering casse cette chaîne.

- **Question :** Quelles sont les premières mesures de hardening AD que vous recommanderiez ?
  - **Réponse type :** Je commencerais par : activer l'Advanced Audit Policy sur tous les DC pour avoir de la visibilité, déployer LAPS pour avoir un mot de passe admin local unique par machine, séparer les comptes admin et utilisateur, activer le SMB signing obligatoire pour bloquer le relay NTLM, et désactiver LLMNR et NBT-NS pour empêcher le poisoning. Ce sont des quick wins à fort impact.

### Questions complémentaires

- **Question :** Comment fonctionne BloodHound et quel est son intérêt ?
  - **Réponse type :** BloodHound modélise l'AD comme un graphe : les objets sont des nœuds, les relations et droits sont des arêtes. Il collecte les données avec SharpHound et permet de visualiser les chemins d'attaque vers Domain Admin. C'est aussi un outil défensif : en le lançant sur son propre AD, on identifie les chemins avant l'attaquant et on peut couper les nœuds de convergence — un seul nœud corrigé peut fermer des dizaines de chemins.

- **Question :** Qu'est-ce qu'un DCSync et comment le détecter ?
  - **Réponse type :** Un DCSync simule un contrôleur de domaine pour demander la réplication des hashes via le protocole de réplication AD. L'attaquant a besoin des droits DS-Replication-Get-Changes et DS-Replication-Get-Changes-All. Côté détection, c'est l'Event ID 4662 avec des droits de réplication depuis une machine qui n'est PAS un DC — ça doit être une alerte critique.

- **Question :** En cas de compromission AD avec suspicion de Golden Ticket, que faites-vous ?
  - **Réponse type :** La priorité c'est la double rotation du krbtgt : une première rotation, on attend 10-12 heures, puis la deuxième. Ça invalide tous les Golden Tickets existants. Il ne faut pas faire les deux rotations en même temps, sinon on casse toutes les sessions Kerberos légitimes. En parallèle, on isole les systèmes compromis sans les éteindre pour préserver la mémoire, et on cherche les autres mécanismes de persistence.

- **Question :** Quels sont les avantages de la deception (honey objects) dans un environnement AD ?
  - **Réponse type :** L'intérêt principal c'est le zéro faux positif. On crée des comptes pièges avec des attributs attractifs — un adminCount=1, un SPN, un vieux mot de passe — et toute interaction avec ces objets est forcément suspecte. Par exemple, un honey SPN déclenche une alerte immédiate dès qu'un attaquant fait du Kerberoasting. C'est une couche de détection très efficace et simple à mettre en place.

### Questions les plus probables en entretien

1. C'est quoi AD et pourquoi c'est critique ?
2. Expliquez Kerberos en quelques étapes.
3. Kerberoasting : principe et défense ?
4. Tiering model : c'est quoi et pourquoi ?
5. Top 5 mesures de hardening AD ?
6. DCSync : c'est quoi, comment détecter ?
7. BloodHound : utilité offensive et défensive ?

### Réponses flash

- **AD** → Annuaire centralisé Microsoft, SSO, 90 % des entreprises, cible n°1 (accès total si compromis).
- **Kerberos** → Client → TGT (via krbtgt) → TGS (via SPN) → accès service. Secret = hash krbtgt.
- **Kerberoasting** → Demande TGS pour SPN → crack offline. Défense = gMSA, mots de passe 25+ chars, AES.
- **Tiering** → Tier 0 (DC/DA), Tier 1 (serveurs), Tier 2 (postes). Jamais de connexion cross-tier.
- **Hardening quick wins** → Audit Policy, LAPS, séparation comptes, SMB signing, désactiver LLMNR.
- **DCSync** → Fausse réplication pour extraire hashes. Détection = 4662 depuis non-DC.
- **Golden Ticket** → TGT forgé avec hash krbtgt. Remédiation = double rotation krbtgt espacée de 10-12h.
- **BloodHound** → Graphe AD, chemins vers DA, nœuds de convergence. Offensif ET défensif.

---

> **Note de clôture**
>
> Ce cours a été conçu comme LA référence Active Directory de la bibliothèque — la ressource complète pour comprendre, attaquer, défendre et répondre à incident sur AD.
>
> L'opération KERBEROS illustre une réalité que tout professionnel cyber constate sur le terrain : la majorité des compromissions AD exploitent des fondamentaux négligés. Un compte de service avec un SPN et un mot de passe de 5 ans. Un template AD CS avec le SAN libre. Un Domain Admin qui a une session active sur un serveur Tier 1. Un krbtgt jamais roté depuis la création du domaine. Un RODC avec une PRP trop large. Un LLMNR actif. Ce ne sont pas des vulnérabilités exotiques — ce sont des configurations par défaut que personne n'a durcies.
>
> Le cours assume deux convictions. Première : comprendre l'attaque est le prérequis pour défendre efficacement — chaque technique offensive est présentée avec son mécanisme, ses outils, ses preuves, ET sa détection et sa remédiation. Deuxième : aucune mesure seule ne suffit — c'est la défense en profondeur (hardening + détection + deception + IR) qui protège AD. Un Golden Ticket est forgeable, mais si le krbtgt est roté régulièrement, les sessions sont monitorées, et les honey accounts sont en place, l'attaquant est détecté avant d'atteindre son objectif.
>
> *Comprendre le mécanisme • Exploiter la faiblesse • Détecter le signal • Durcir la configuration • Répondre à l'incident — avec méthode et profondeur.*
