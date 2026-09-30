---
title: Partie V — Identité ET authentification
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

*L'identité est le nouveau périmètre — en cloud comme on-premise, qui vous êtes détermine ce que vous pouvez faire.*

---


## Chapitre 20 — LDAP et annuaires

Un annuaire est une base de données hiérarchique optimisée pour la lecture — il stocke les utilisateurs, les groupes, les machines et les services. **LDAP** (Lightweight Directory Access Protocol — port 389, LDAPS port 636) est le protocole standard. La structure DIT (Directory Information Tree) : DC (Domain Component — dc=corp,dc=com), OU (Organizational Unit — ou=Users), CN (Common Name — cn=Alice Dupont), DN (Distinguished Name — chemin complet : cn=Alice,ou=Users,dc=corp,dc=com). Les opérations : Bind (authentification), Search (recherche), Add, Modify, Delete.

OpenLDAP vs Active Directory : OpenLDAP est un annuaire LDAP léger sous Linux. Active Directory est un annuaire enrichi sous Windows — LDAP + Kerberos + DNS + GPO (traité au Ch.21). Les risques LDAP : **anonymous bind** (connexion sans credentials → lecture complète de l'annuaire — tous les utilisateurs, groupes, attributs), **LDAP sans TLS** (port 389 — credentials en clair sur le réseau → toujours utiliser LDAPS 636 ou STARTTLS), **injection LDAP** (similaire à l'injection SQL mais sur les requêtes LDAP).

---


## Chapitre 21 — Active Directory comme socle d'infrastructure

*Ce chapitre ne redouble pas le cours AD — il traite l'AD comme brique d'infrastructure centrale dont la compréhension est indispensable même sans être spécialiste AD.*

### 21.1 Ce que l'AD fait réellement

AD n'est pas « un annuaire » — c'est le **socle de l'infrastructure Windows**. AD = **LDAP** (annuaire des utilisateurs, groupes, machines — chaque objet a des attributs, des appartenances, des permissions) + **Kerberos** (protocole d'authentification — TGT, TGS, Service Ticket ; les mots de passe ne transitent jamais sur le réseau après l'authentification initiale) + **DNS** (résolution de noms intégrée — les machines trouvent leur DC via les enregistrements SRV DNS ; si le DNS AD tombe, plus rien ne fonctionne) + **GPO** (Group Policy Objects — configuration centralisée de tous les postes et serveurs : politique de mots de passe, restriction d'exécution, mapping de lecteurs, configuration du firewall Windows, déploiement de logiciels) + **SYSVOL** (réplication des politiques et scripts de login entre les DC) + **trusts** (relations de confiance entre domaines et forêts — un trust mal configuré = un chemin d'attaque inter-domaines).

### 21.2 Le rôle des contrôleurs de domaine

Les DC (Domain Controllers) sont les serveurs les plus critiques de l'infrastructure — ils stockent **tous les comptes**, **tous les mots de passe** (sous forme de hashes NTLM), et délivrent les tickets Kerberos. Un DC compromis = le SI entier est compromis. C'est pourquoi le **tiering model** est le contrôle fondamental : **Tier 0** (DC, comptes admin domaine, AD CS, AD Connect — la zone la plus protégée), **Tier 1** (serveurs applicatifs, comptes admin serveur), **Tier 2** (postes de travail, comptes utilisateurs). La règle : un compte Tier 2 ne se connecte JAMAIS à un serveur Tier 0, et réciproquement.

### 21.3 Les dépendances de l'écosystème Windows

Exchange dépend d'AD (les boîtes mail sont des objets AD). SQL Server peut utiliser l'authentification AD (authentification intégrée Windows). Les partages de fichiers utilisent les groupes AD pour les ACL. Le VPN authentifie contre AD (via RADIUS/NPS). Les applications métier délèguent l'authentification à AD (SSO via Kerberos ou SAML). Le SIEM collecte les logs AD (Event Logs Security). **Quand AD tombe, TOUT tombe.** Un problème AD n'est jamais « un sujet annuaire » — c'est un sujet infrastructure central.

### 21.4 Les attaques qui exploitent l'AD

Vue d'ensemble (le cours AD de la bibliothèque couvre en profondeur) : **Kerberoasting** (demander des TGS pour des comptes de service et cracker les hashes offline), **AS-REP Roasting** (cibler les comptes sans pré-authentification Kerberos), **Pass-the-Hash** (utiliser le hash NTLM volé pour s'authentifier sans le mot de passe), **Golden Ticket** (forger un TGT avec le hash krbtgt → accès illimité au domaine), **Silver Ticket** (forger un Service Ticket), **DCSync** (simuler un DC pour demander la réplication des hashes de tous les comptes), **NTLM relay** (relayer une authentification NTLM vers un autre service). Pourquoi désactiver NTLM quand possible : NTLM est un protocole legacy vulnérable au relay et au pass-the-hash, Kerberos est plus sécurisé.

---


## Chapitre 22 — Authentification moderne : SSO, OAuth, SAML, OIDC

**SSO** (Single Sign-On — s'authentifier une fois, accéder à tout) : avantage UX et sécurité (un seul mot de passe fort + MFA plutôt que 15 mots de passe faibles), risque (si le SSO est compromis, tout est compromis).

**SAML** (Security Assertion Markup Language — protocole de SSO XML, créé pour l'entreprise) : l'IdP (Identity Provider — AD FS, Okta, Azure AD) authentifie l'utilisateur et génère une assertion SAML (un document XML signé contenant l'identité et les attributs). Le SP (Service Provider — l'application) vérifie l'assertion et accorde l'accès. L'attaque **GoldenSAML** (forger des assertions SAML en compromettant la clé de signature de l'IdP → accès à tous les SP sans authentification — utilisé par APT29 dans SolarWinds, cf. cours APT Ch.29).

**OAuth 2.0** (framework d'autorisation — le standard moderne pour les APIs) : l'authorization code flow (le plus sécurisé — redirection vers l'IdP, code d'autorisation, échange contre un token), l'implicit flow (déprécié — le token est directement dans l'URL), le client credentials flow (entre services, pas d'utilisateur). Tokens (access token — durée de vie courte, refresh token — durée de vie longue pour renouveler l'access token). Scopes (permissions granulaires).

**OpenID Connect** (OIDC — couche d'authentification au-dessus d'OAuth 2.0) : ajoute l'ID Token (un JWT qui contient l'identité de l'utilisateur) et le UserInfo endpoint. C'est le standard moderne pour le SSO web.

**JWT** (JSON Web Token — token autoportant signé) : structure header.payload.signature (chaque partie en base64). Le header contient l'algorithme de signature (HS256, RS256). Le payload contient les claims (sub, iss, exp, iat, rôles). La signature garantit l'intégrité. Risques : alg:none (l'attaquant met « none » comme algorithme → la signature n'est pas vérifiée), secret HMAC faible (brute force du secret → forgeage de tokens), pas de vérification côté serveur, et token avec une durée de vie trop longue.

---


## Chapitre 23 — IAM cloud : Azure AD/Entra ID, AWS IAM, GCP IAM

*L'IAM cloud est le terrain de jeu des APT modernes — Volt Typhoon, APT29 compromettent l'identité cloud.*

**Azure AD / Entra ID** : tenants (l'organisation), utilisateurs, groupes, applications enregistrées, rôles (Global Admin — le plus puissant, équivalent Domain Admin en cloud), Conditional Access (politiques d'accès contextuelles — autoriser/bloquer selon l'appareil, la localisation, le risque), et PIM (Privileged Identity Management — activation temporaire des rôles admin, just-in-time access).

**AWS IAM** : users, groups, roles, policies (documents JSON qui définissent les permissions). Le principe du moindre privilège : chaque entité a uniquement les permissions nécessaires. Les erreurs courantes : politique AdministratorAccess sur tous les utilisateurs, access keys (credentials programmatiques) en clair dans le code source, pas de MFA sur le compte root.

**GCP IAM** : service accounts, roles (predefined/custom), bindings (liaison role → identité → ressource).

L'**identité comme nouveau périmètre** : en cloud, il n'y a pas de firewall au sens traditionnel — l'identité EST le contrôle d'accès. Le token est la clé — token theft (vol de token OAuth/SAML), OAuth abuse (application malveillante demandant des scopes excessifs), et MFA bypass (AitM — Adversary-in-the-Middle, intercepte le token post-MFA) sont les vecteurs d'attaque cloud dominants. Le **monitoring identity** est indispensable : Azure AD sign-in logs (connexions, risques détectés), CloudTrail (toutes les actions API AWS), et les anomalies (connexion depuis un pays inhabituel, token utilisé depuis 2 IP simultanément).

---


## Chapitre 24 — MFA, gestion des mots de passe et facteurs d'authentification

Les **3 facteurs** : ce que je sais (mot de passe, PIN), ce que j'ai (téléphone/TOTP, clé physique FIDO2/YubiKey, badge), ce que je suis (empreinte, reconnaissance faciale). Le MFA combine au moins 2 facteurs différents. Quels comptes : TOUS les comptes admin (P0), tous les accès distants (VPN, RDP), tous les accès cloud, et idéalement tous les utilisateurs. Quels types : **FIDO2/clés physiques** (résistantes au phishing — le gold standard pour les admins), **push/TOTP** (acceptable pour les utilisateurs standard), SMS (le plus faible — SIM swapping — à éviter).

Les **attaques anti-MFA** : MFA fatigue/prompt bombing (envoyer des dizaines de notifications push jusqu'à ce que l'utilisateur accepte par lassitude), AitM (Adversary-in-the-Middle — proxy qui intercepte le token de session après l'authentification MFA → contourne le MFA car le token est volé post-authentification), SIM swapping (transfert du numéro de téléphone vers une SIM contrôlée par l'attaquant → interception des SMS OTP), et vol de token post-MFA (le MFA protège l'authentification, pas le token de session résultant).

La **politique de mots de passe** : longueur > complexité (les recommandations NIST 2024 privilégient 12+ caractères sans exigence de caractères spéciaux — un mot de passe long est plus résistant qu'un mot de passe court et complexe), gestionnaire de mots de passe (un mot de passe unique et fort par service), interdiction de réutilisation (vérification contre les bases de mots de passe compromis — Have I Been Pwned), et pas de rotation obligatoire si MFA est en place (la rotation forcée pousse les utilisateurs à choisir des mots de passe plus faibles et prévisibles).

---
