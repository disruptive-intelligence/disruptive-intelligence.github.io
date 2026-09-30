---
title: Partie IV — Applications, web ET apis
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

---


## Chapitre 17 — Serveurs web, reverse proxy, WAF et CDN

Les 3 serveurs web majeurs : **Apache httpd** (configuration par fichiers .conf et .htaccess, modules mod_ssl/mod_security/mod_rewrite, logs access_log et error_log), **Nginx** (configuration déclarative, reverse proxy natif, performant en charge, logs access.log et error.log), **IIS** (Internet Information Services — intégré à Windows Server, configuration via GUI ou web.config, logs IIS dans W3SVC).

La configuration sécurisée : headers de sécurité (Strict-Transport-Security — HSTS, X-Content-Type-Options: nosniff, X-Frame-Options: DENY, Content-Security-Policy — CSP, Referrer-Policy), masquage de la version serveur (ServerTokens Prod sur Apache, server_tokens off sur Nginx), désactivation du directory listing (Options -Indexes), permissions strictes sur les fichiers web (pas de world-writable), et HTTPS obligatoire (redirect 80 → 443, Let's Encrypt + certbot pour l'automatisation).

Le **reverse proxy** est un intermédiaire entre les clients et les serveurs backend — il masque l'IP et la technologie du backend, centralise les certificats TLS, ajoute des headers de sécurité, et fournit un point unique de logging. **TLS termination** (le reverse proxy déchiffre TLS → trafic interne en clair sauf rechiffrement) et **mTLS** (authentification mutuelle — les deux côtés présentent un certificat, utilisé entre microservices et en Zero Trust).

Le **load balancer** répartit les requêtes entre serveurs backend (round-robin, least connections, IP hash, weighted) avec des health checks pour retirer les serveurs en panne. Le **WAF** (Web Application Firewall) filtre les requêtes HTTP malveillantes (ModSecurity + OWASP CRS, WAF cloud — AWS WAF, Cloudflare) — limite : ne remplace pas le secure coding, contournable par encodage/obfuscation. Le **CDN** (Cloudflare, Akamai, CloudFront) distribue le contenu géographiquement, absorbe les DDoS, et masque l'IP d'origine.

Les **logs web** comme source d'investigation : patterns suspects dans access_log — rafales de 404 (scan de répertoires), POST vers des fichiers uploadés (web shell), caractères spéciaux dans les URLs (' -- UNION <script>), user-agents d'outils de scan (sqlmap, nikto, dirsearch).

---


## Chapitre 18 — Architecture web et vulnérabilités : la vue d'ensemble

*Vue d'ensemble — le cours AppSec (futur) traitera chaque vulnérabilité en profondeur.*

L'architecture **3 tiers** : frontend (navigateur — HTML, CSS, JavaScript), backend (serveur applicatif — logique métier), base de données (stockage persistant). Les langages et frameworks : PHP (Laravel, Symfony, WordPress), Python (Django, Flask, FastAPI), Java (Spring Boot), Node.js (Express, Next.js), .NET/C# (ASP.NET Core), Go (Gin, Fiber), Ruby (Rails).

Sessions et cookies : HTTP est stateless → le serveur crée une session et envoie un cookie (Set-Cookie: session_id=abc123). Le navigateur renvoie ce cookie à chaque requête. Les flags de sécurité : **Secure** (cookie transmis uniquement en HTTPS), **HttpOnly** (cookie inaccessible au JavaScript → protection XSS), **SameSite** (strict/lax/none → protection CSRF).

**OWASP Top 10** — la référence : A01 Broken Access Control (IDOR, privesc → vérification d'autorisation systématique), A02 Cryptographic Failures (données non chiffrées → TLS partout, chiffrement au repos), A03 Injection (SQL, OS, LDAP → requêtes paramétrées), A04 Insecure Design (failles de conception → threat modeling), A05 Security Misconfiguration (config par défaut, debug activé → hardening), A06 Vulnerable Components (dépendances avec CVE → SCA), A07 Auth & Identification Failures (auth faible → MFA, rate limiting), A08 Software & Data Integrity (désérialisation, supply chain → vérification d'intégrité), A09 Logging & Monitoring Failures (pas de logs → logging de sécurité), A10 SSRF (requêtes serveur vers cible contrôlée → whitelist d'URLs).

---


## Chapitre 19 — APIs : REST, GraphQL et sécurité

**REST** (Representational State Transfer) : ressources identifiées par URL (/api/v1/users/42), verbes HTTP (GET/POST/PUT/DELETE), JSON, stateless. **GraphQL** : requêtes flexibles (le client demande exactement les champs voulus), introspection (par défaut activée → cartographie complète de l'API pour l'attaquant), risques spécifiques (requêtes imbriquées → DoS, injection). **SOAP** (Simple Object Access Protocol — XML, WSDL, legacy mais encore présent en entreprise — interfaces bancaires, ERP).

L'authentification API : **API Keys** (simple token dans le header — à protéger, à restreindre par IP/scope, à roter régulièrement), **OAuth 2.0** (authorization code flow — le standard moderne), **Bearer tokens** (JWT dans le header Authorization), **JWT** (JSON Web Token — structure header.payload.signature, signature HMAC ou RSA ; risques : alg:none → signature désactivée, secret HMAC faible → brute force, pas de vérification de la signature côté serveur, token trop longue durée de vie), **mTLS** (authentification mutuelle pour les API internes).

**OWASP API Security Top 10** : BOLA/IDOR (accès aux objets d'autres utilisateurs — la vulnérabilité API #1), Broken Authentication (auth faible sur l'API), Excessive Data Exposure (l'API renvoie plus de données que nécessaire — le client filtre au lieu du serveur), Lack of Rate Limiting (pas de throttling → brute force, DoS), Broken Function Level Authorization (accès à des fonctions admin sans vérification).

La documentation comme surface d'attaque : Swagger/OpenAPI exposé publiquement = cartographie complète de l'API pour l'attaquant (endpoints, paramètres, types, exemples).

---
