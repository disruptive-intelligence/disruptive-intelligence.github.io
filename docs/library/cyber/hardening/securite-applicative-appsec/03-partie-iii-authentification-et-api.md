---
title: Partie III — Authentification et API
source: Cyber/05 Hardening/Sécurité applicative (AppSec).md
note: Sécurité applicative (AppSec)
up:
- - Sécurité applicative (AppSec)
  - index.md
---

---


## Chapitre 13 — Authentification, sessions et identité moderne

L'authentification locale : stockage des mots de passe (bcrypt/Argon2 — JAMAIS de hash simple), politique de mot de passe NIST 2024 (longueur > complexité, blocklist de mots de passe compromis — HIBP API, pas de rotation forcée sans raison). Les **sessions** : session ID côté serveur (stocké en cookie HttpOnly, Secure, SameSite — le serveur maintient l'état) vs JWT côté client (le token contient les claims, signé par le serveur — stateless mais révocation difficile). Session fixation, session hijacking, invalidation (le logout doit détruire la session côté serveur, pas seulement supprimer le cookie côté client).

Le **MFA** : TOTP (Google Authenticator, Authy — basé sur le temps), WebAuthn/passkeys (clé cryptographique liée au device — la direction de l'industrie en 2025), push notification. Les SMS sont déconseillés comme second facteur (interception via SIM swapping, SS7 attacks).

**OAuth 2.1 et OpenID Connect** : le standard d'authentification déléguée. Authorization Code + PKCE pour les SPA et les mobiles (PKCE empêche l'interception du code d'autorisation). Les erreurs courantes : redirect URI ouvertes (l'attaquant redirige le token vers son serveur), token leakage via le header Referer, state/nonce manquants (permet le CSRF sur le flux OAuth), client credentials exposées dans le frontend JavaScript (le client_secret ne doit JAMAIS être dans le frontend).

Les **passkeys/WebAuthn** : authentification sans mot de passe par clé cryptographique — résistant au phishing (la clé est liée au domaine), au credential stuffing, et au brute force. La prise en charge est native dans les navigateurs et les OS modernes (Chrome, Safari, Windows Hello).

L'authentification pour les **microservices** : mTLS (mutual TLS — les services s'authentifient mutuellement par certificat), service mesh (Istio/Linkerd — mTLS automatique), et JWT inter-services (un token signé qui porte l'identité et les droits du service appelant).

---


## Chapitre 14 — Sécurité des APIs

Les spécificités : pas d'interface utilisateur → pas de « frontend qui cache les boutons » → chaque endpoint doit être sécurisé indépendamment.

**REST API security** : authentification (API keys, Bearer tokens, OAuth 2.0), autorisation (RBAC/ABAC — middleware systématique, ne jamais vérifier les droits uniquement dans le contrôleur), validation des entrées (schéma JSON strict — rejeter tout ce qui n'est pas conforme au schéma, limites de taille), rate limiting (par IP, par token, par endpoint — Protection from Automated Threats), pagination (TOUJOURS une limite de résultats par page — un endpoint sans pagination permet à l'attaquant de dump toute la base), versioning (ne pas exposer d'anciennes versions non maintenues). Le **mass assignment** (l'attaquant envoie des champs non prévus — `{"role": "admin"}` — qui sont appliqués si le framework les accepte automatiquement ; protection : allowlist de champs modifiables — `serializer.validated_data` plutôt que `request.data` directement).

**GraphQL security** : introspection désactivée en production (sinon l'attaquant obtient le schéma complet), query depth/complexity limiting (une requête récursive `{user {friends {friends {friends...}}}}` peut OOM le serveur), batching attacks (envoyer des centaines de requêtes en un seul batch), et autorisation par résolveur (pas par type — vérifier les droits à chaque résolveur, pas seulement au niveau du type).

**gRPC et WebSocket security** : authentification par token/certificat, validation des messages (protobuf pour gRPC, schéma pour WebSocket), timeouts.

L'**API Gateway** comme point de contrôle centralisé (authentification, rate limiting, logging, transformation — Kong, AWS API Gateway, Traefik).

---


## Chapitre 15 — Security Misconfiguration et composants vulnérables

### 15.1 Security Misconfiguration

*Les erreurs de configuration — le terreau le plus fertile des vulnérabilités, parce qu'il ne nécessite aucune compétence d'exploitation sophistiquée.*

Les configurations dangereuses : debug activé en production (stack traces avec variables d'environnement — `DEBUG=True` en Django, `error_reporting(E_ALL)` en PHP), headers par défaut révélant la technologie (`Server: Apache/2.4.41`, `X-Powered-By: Express`), directory listing activé (l'arborescence du serveur est visible), credentials par défaut non changées (admin/admin, root/root — les scanners automatisés les testent systématiquement), CORS permissif (`Access-Control-Allow-Origin: *` avec credentials — n'importe quel site peut faire des requêtes authentifiées), et permissions cloud trop larges (buckets S3 publics, security groups ouverts sur `0.0.0.0/0`, rôles IAM avec `*:*`).

La défense : checklists de configuration par environnement (dev, staging, production — chaque environnement a sa checklist), infrastructure as code (Terraform, CloudFormation — la configuration est versionnée, revue, et reproductible), et hardening guides (CIS Benchmarks par technologie).

### 15.2 Composants vulnérables

*Les dépendances avec des CVE connues — la majorité du code d'une application est du code tiers.*

Une application Python typique a 50-200 dépendances directes et transitives. Chaque dépendance est du code tiers, maintenu par des tiers, avec ses propres vulnérabilités. Les outils de **SCA** (Software Composition Analysis) scannent les dépendances en continu : pip-audit (Python), npm audit (Node.js), Snyk (multi-langage), Dependabot (GitHub — PR automatiques de mise à jour), Trivy (conteneurs + dépendances). Le workflow : scan → alerte sur CVE → triage (vrai positif ? exploitable dans notre contexte ?) → mise à jour ou mitigation → vérification → clôture. Les exceptions (vulnérabilité acceptée temporairement) doivent être documentées avec justification et date de revue.

La gestion des **headers de sécurité** (CSP, HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy — une checklist à vérifier sur chaque déploiement ; les outils comme securityheaders.com fournissent un scan instantané).

---
