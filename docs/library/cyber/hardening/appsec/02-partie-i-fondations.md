---
title: Partie I — Fondations
source: IT/03_Networking/AppSec.md
note: AppSec
up:
- - AppSec
  - index.md
---

*Comprendre le terrain avant d'attaquer ou de défendre — HTTP, le navigateur, les référentiels OWASP, et la modélisation des menaces.*

---


## Chapitre 1 — Pourquoi la sécurité applicative

Le constat : la majorité des compromissions sont applicatives (Verizon DBIR, année après année). Les firewalls protègent le périmètre réseau, les EDR détectent les malwares — mais quand un attaquant exploite une injection SQL ou un IDOR via HTTPS sur le port 443, il passe comme du trafic légitime. L'application est devenue le périmètre.

AppSec ≠ pentest (diagnostic à un instant T) ≠ infra security (serveurs, réseau) ≠ DevOps (automatisation du déploiement). L'AppSec s'intègre dans le cycle de développement pour prévenir les vulnérabilités à la source, les détecter en continu, les identifier en production, et réduire systématiquement la surface d'attaque applicative.

Le coût de la vulnérabilité (courbe shift-left : design 1x → développement 5-10x → test 15-30x → production 30-100x → breach 100-1000x). La surface d'attaque moderne (SPA React → API REST → microservices → bases de données → services cloud → webhooks → SDK tiers — chaque endpoint, chaque formulaire, chaque upload, chaque dépendance npm est un point d'entrée potentiel). L'attaquant pense en graphe (tous les états possibles de l'application), le développeur pense en fonctionnalité (le happy path).

> **🎯 SecureHealth — M0 :** le pentest tombe. 14 vulnérabilités, 3 critiques. Le CTO convoque une réunion de crise. « On ne peut plus ignorer la sécurité. »

---


## Chapitre 2 — Architecture web et surface d'attaque

Le modèle client-serveur. **HTTP en profondeur** : méthodes (GET, POST, PUT, DELETE, PATCH, OPTIONS), URL cible, headers (Host, Content-Type, Authorization, Cookie, User-Agent), corps. La réponse : status codes (200, 301, 403, 404, 500), headers (Set-Cookie, Content-Security-Policy, CORS), corps. Chaque élément est manipulable par l'attaquant. **HTTPS/TLS** : TLS 1.2 minimum, 1.3 recommandé. Ce que TLS protège (confidentialité et intégrité en transit) et ce qu'il ne protège PAS (les vulnérabilités de l'application — une injection SQL transite parfaitement en HTTPS). **URLs, routes, paramètres** : path (IDOR, path traversal), query string (injection, XSS), fragment (DOM-based XSS).

Les **architectures modernes** : monolithe (surface limitée, vulnérabilités concentrées), microservices (surface multipliée — chaque service est un point d'entrée, mais isolation possible), SPA + API (le frontend est du code dans le navigateur de l'utilisateur — non fiable par définition, le backend est la seule source de vérité), BFF (Backend For Frontend — proxy entre SPA et APIs), API Gateway (centralise auth, rate limiting, routage). Le reverse proxy (Nginx, Traefik — terminaison TLS, headers de sécurité), le load balancer, le CDN (Cloudflare, CloudFront). Les erreurs de configuration : IP spoofing via X-Forwarded-For, host header injection, cache poisoning.

La cartographie de la surface d'attaque : formulaires (injection, XSS), endpoints API (IDOR, auth bypass, mass assignment), uploads (webshell), webhooks (SSRF), WebSockets (injection, auth bypass), headers HTTP (host injection, CRLF).

> **🎯 SecureHealth — cartographie :** SPA React (Vercel) → API Django REST Framework (EC2/ALB) → PostgreSQL (RDS) → S3 (documents médicaux). Services tiers : Stripe, SendGrid, Twilio. 47 endpoints API, 3 formulaires, 1 upload, 1 webhook Stripe, 1 WebSocket notifications.

---


## Chapitre 3 — Le modèle de sécurité du navigateur

Le navigateur comme sandbox — il exécute du code JavaScript de n'importe quel site. La **Same-Origin Policy** (SOP — le fondement : un script d'un origin ne peut pas accéder aux données d'un autre origin ; un origin = scheme + host + port). Le **CORS** (Cross-Origin Resource Sharing — mécanisme qui assouplit la SOP de manière contrôlée ; les erreurs de configuration CORS — Access-Control-Allow-Origin: * avec credentials = vulnérabilité). La **CSP** (Content Security Policy — header qui contrôle quelles ressources le navigateur peut charger ; défense en profondeur contre le XSS ; une CSP stricte avec nonces est la meilleure protection complémentaire).

Les **cookies** (HttpOnly — non accessible par JavaScript → protège contre le vol par XSS, Secure — uniquement en HTTPS, SameSite — Lax par défaut dans les navigateurs modernes → protection CSRF, Domain/Path — scope). Les **headers de sécurité** : X-Content-Type-Options: nosniff, X-Frame-Options: DENY (anti-clickjacking), Strict-Transport-Security (HSTS — force HTTPS), Referrer-Policy, Permissions-Policy.

---


## Chapitre 4 — OWASP Top 10 (2025), API Top 10, ASVS et Top 10 LLM

L'**OWASP Top 10 2025** comme référentiel de base (les 10 catégories avec les changements par rapport à 2021). L'**OWASP API Security Top 10 2023** (vulnérabilités spécifiques aux APIs — BOLA/Broken Object Level Authorization, Broken Authentication, BOPLA/Broken Object Property Level Authorization, Unrestricted Resource Consumption, BFLA/Broken Function Level Authorization, SSRF, Security Misconfiguration, Lack of Protection from Automated Threats, Improper Inventory Management, Unsafe Consumption of APIs). L'**OWASP ASVS** (Application Security Verification Standard — 3 niveaux : L1 standard, L2 défensif, L3 critique — la feuille de route concrète pour atteindre un niveau de sécurité cible). L'**OWASP Top 10 for LLM Applications** (prompt injection, insecure output handling, training data poisoning, model DoS, supply chain, sensitive information disclosure, insecure plugin design, excessive agency, overreliance, model theft).

L'articulation : le Top 10 est le diagnostic, l'ASVS est la feuille de route, le Top 10 API est le focus pour les architectures modernes, le Top 10 LLM couvre le nouveau terrain IA.

---


## Chapitre 5 — Modélisation des menaces (Threat Modeling)

Le threat modeling identifie les risques de sécurité au moment de la conception — le shift-left ultime. **STRIDE** appliqué (Spoofing — un attaquant forge un JWT, Tampering — modification du prix dans la requête, Repudiation — pas de logs d'audit, Information Disclosure — stack trace en production, Denial of Service — requête sans pagination, Elevation of Privilege — mass assignment role=admin). Les **DFD** (Data Flow Diagrams — entités externes, processus, data stores, flux, trust boundaries — chaque trust boundary est un point où la validation et l'authentification doivent être appliquées). DREAD (scoring) et alternatives.

Threat modeling en pratique : atelier collaboratif 1-2h avec l'équipe de développement, au début de chaque fonctionnalité significative. Attack trees et abuse cases. Les limites : identifie les failles de design, pas les bugs d'implémentation — ne remplace pas les tests.

> **🎯 SecureHealth — threat modeling :** partage de dossier patient avec un médecin externe. DFD : médecin → SPA → API /share → PostgreSQL → SendGrid. Trust boundaries identifiées. STRIDE : Spoofing (vérification identité médecin ?), Information Disclosure (lien de partage devinable ?), Elevation of Privilege (accès à d'autres dossiers ?). 7 menaces identifiées, 3 critiques, mitigations intégrées au backlog avant le code.

---
