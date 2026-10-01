---
title: Partie II — Vulnérabilités web en profondeur
source: Cyber/05 Hardening/Sécurité applicative (AppSec).md
note: Sécurité applicative (AppSec)
up:
- - Sécurité applicative (AppSec)
  - index.md
---

*Pour chaque vulnérabilité : mécanisme, code vulnérable, exploitation, impact, code corrigé, défense en profondeur, détection, fil rouge. Chaque chapitre est conçu pour qu'un développeur comprenne non seulement comment corriger, mais pourquoi la vulnérabilité existe, comment l'attaquant l'exploite, et comment la détecter en production.*

---


## Chapitre 6 — Injection (SQL, NoSQL, OS, LDAP, templates)

### 6.1 Le mécanisme fondamental

L'injection se produit quand des données fournies par l'utilisateur sont interprétées comme du code par le système cible. La cause est toujours la même : le mélange entre données et instructions dans une même chaîne. Quand un développeur écrit `query = "SELECT * FROM users WHERE name = '" + user_input + "'"`, le contenu de user_input est inséré directement dans la requête SQL. Si l'utilisateur entre `' OR 1=1 --`, le OR 1=1 est toujours vrai, le `--` commente la suite. Le principe est identique pour toutes les injections : SQL, NoSQL, OS, LDAP, templates.

### 6.2 Injection SQL : les techniques

L'injection UNION-based (UNION SELECT pour extraire d'autres tables), error-based (les messages d'erreur contiennent les données), blind boolean-based (la page s'affiche différemment selon la condition — oui/non), blind time-based (SLEEP pour extraire bit par bit — si la réponse prend 5 secondes, le bit est 1), et stacked queries (INSERT, UPDATE, DELETE — les plus dangereuses).

### 6.3 Code vulnérable vs corrigé

La solution fondamentale : le **prepared statement** (requête paramétrée) — séparer la structure de la requête des données. En Django : l'ORM (`Patient.objects.filter(name=user_input)`) plutôt que les raw queries. En Java/JDBC : PreparedStatement avec `?`. En Node/Sequelize : méthodes de l'ORM. En PHP/PDO : prepared statements avec bindParam. La requête paramétrée garantit que l'input est TOUJOURS traité comme une donnée, jamais comme du code SQL.

Les pièges ORM : les raw queries (`cursor.execute("SELECT..." + input)`), les méthodes `extra()` et `RawSQL()` de Django, les `order_by` dynamiques (`?sort=name; DROP TABLE users`), et les filtres construits dynamiquement à partir d'entrées non validées. La règle : utiliser l'ORM partout, et quand une raw query est inévitable, utiliser des paramètres nommés.

### 6.4 Injection NoSQL, OS et SSTI

**Injection NoSQL** (MongoDB — opérateurs JSON : `{"password": {"$ne": ""}}` rend la condition toujours vraie ; protection : valider le type des entrées). **Injection de commandes OS** (`os.system("ping " + user_ip)` → injection de `; cat /etc/passwd` ; protection : `subprocess.run(["ping", user_ip])` — chaque élément est un argument, pas interprété par le shell). **SSTI** (Server-Side Template Injection — Jinja2, Twig — `{{7*7}}` renvoie 49 = SSTI confirmé ; les payloads élaborés permettent l'exécution de commandes ; protection : ne jamais insérer d'entrée utilisateur dans un template comme variable de template, utiliser le sandboxing).

### 6.5 Défense en profondeur et détection

Couche fondamentale : prepared statements. Couche supplémentaire : validation d'entrée (allowlist). Moindre privilège DB (le compte de l'application n'a pas les droits DROP ou GRANT). WAF (filet — bloque les patterns évidents mais contournable → ne doit JAMAIS être la protection principale). Détection : logs DB (requêtes anormalement longues, UNION SELECT, SLEEP), erreurs SQL dans les logs applicatifs (pic d'erreurs 500), alertes WAF, corrélation SIEM.

> **🎯 SecureHealth — injection SQL :** la recherche de patients utilise une raw query Django. L'attaquant extrait tous les comptes via UNION SELECT. Correction : migration vers l'ORM + compte DB read-only pour la recherche. Détection : alerte Splunk sur les erreurs 500 + règle WAF.

---


## Chapitre 7 — Broken Access Control, IDOR et logique métier

### 7.1 Le problème n°1 du OWASP Top 10

Le Broken Access Control est en première position depuis 2021. Le problème fondamental : l'application ne vérifie pas si l'utilisateur a le DROIT de faire ce qu'il demande. Le développeur implémente l'authentification (qui est l'utilisateur ?) mais oublie l'autorisation (a-t-il le droit d'accéder à CETTE ressource ?). Le frontend masque les boutons — mais rien n'empêche l'attaquant d'appeler directement l'endpoint API.

### 7.2 IDOR (Insecure Direct Object Reference)

L'attaquant change l'ID dans l'URL/API pour accéder aux données d'un autre utilisateur. `GET /api/patients/1234` → `GET /api/patients/1235`. Si l'API renvoie le dossier du patient 1235 sans vérifier que l'utilisateur connecté a le droit d'y accéder, c'est un IDOR. Horizontal privilege escalation (accéder aux données d'un autre utilisateur du même rôle) vs vertical (accéder à des fonctionnalités réservées à un rôle supérieur).

### 7.3 Abus de logique métier et race conditions de niveau métier

*Ce chapitre traite les race conditions au niveau métier — les abus de concurrence qui exploitent la logique fonctionnelle de l'application. Le Ch.12 traite les race conditions au niveau technique (TOCTOU, atomicité, verrouillage).*

Le **price manipulation** (modifier le prix dans la requête API avant envoi — le frontend affiche 99 €, l'attaquant envoie `"price": 1` dans le body). Le **workflow bypass** (sauter une étape de validation — l'attaquant appelle directement l'endpoint de confirmation sans passer par la vérification). Le **coupon stacking** (appliquer un coupon de réduction plusieurs fois en envoyant des requêtes concurrentes — la vérification « coupon déjà utilisé ? » est faite AVANT l'application, et 2 requêtes simultanées passent toutes les deux). Le **double-spend métier** (utiliser le même crédit/solde deux fois en exploitant le timing — 2 requêtes d'achat simultanées avec le même solde, les deux sont validées avant que le solde ne soit décrémenté). Le **negative quantity** (commander -1 article pour créditer son compte au lieu de le débiter).

### 7.4 Défense et détection

Le middleware d'autorisation systématique (ne JAMAIS faire confiance au frontend — vérifier l'ownership à chaque requête côté serveur : `if patient.owner != request.user: return 403`). Les tests d'autorisation automatisés (une suite de tests qui vérifie que chaque endpoint refuse l'accès à un utilisateur non autorisé). Pour la logique métier : la validation côté serveur de tous les paramètres critiques (prix, quantité, montant — le frontend est un affichage, le serveur est la vérité), les idempotency keys pour les opérations critiques, et la sérialisation des opérations financières (transactions DB avec isolation level approprié). Détection : alertes sur les accès à des ressources hors scope de l'utilisateur (logs d'autorisation).

> **🎯 SecureHealth — IDOR :** `GET /api/patients/1234` renvoie le dossier du patient 1234 sans vérifier que l'utilisateur connecté est le médecin traitant ou le patient lui-même. Un patient peut accéder au dossier de n'importe quel autre patient. Correction : middleware vérifiant `patient.treating_doctor == request.user OR patient.user == request.user`.

---


## Chapitre 8 — Cross-Site Scripting (XSS)

Les 3 types : **Reflected** (dans la réponse immédiate — l'URL contient le payload, la page le reflète), **Stored** (persisté en base — le payload est stocké et exécuté à chaque affichage), **DOM-based** (manipulé côté client par JavaScript sans passer par le serveur). Le mécanisme : injection de JavaScript dans le contexte du navigateur de la victime. Les impacts : vol de cookies/session (si pas HttpOnly), keylogging, phishing, redirection, defacement, crypto-mining.

Les **contextes d'injection** (chaque contexte a ses caractères dangereux) : HTML body (`<script>alert(1)</script>` → HTML encoding), attributs HTML (`" onmouseover="alert(1)` → attribute encoding), JavaScript (`'; alert(1)//` → JS encoding), CSS (`expression()`, `url()` → CSS encoding), URL (`javascript:alert(1)` → URL encoding). L'output encoding doit être **contextuel** — un encodage HTML dans un contexte JavaScript ne protège pas.

Défense en profondeur : output encoding contextuel (la fondation) + CSP stricte avec nonces (défense en profondeur — même si un XSS passe l'encoding, la CSP bloque l'exécution du script) + HttpOnly cookies (le XSS ne peut pas voler le cookie de session) + input validation (couche supplémentaire). Détection : violations CSP loggées (Content-Security-Policy-Report-Only puis enforcement), patterns XSS dans les logs WAF.

---


## Chapitre 9 — Cryptographic Failures

Le stockage des mots de passe : **bcrypt, scrypt, Argon2** — JAMAIS MD5/SHA1/SHA256 sans sel et sans itérations (un hash SHA256 se brute-force en secondes avec hashcat ; bcrypt avec un work factor de 12 prend des jours). Le **chiffrement des données** : AES-256-GCM pour le symétrique (le mode GCM fournit confidentialité + intégrité + authentification), RSA-2048+ ou ECC pour l'asymétrique. Les modes à éviter : ECB (chaque bloc est chiffré indépendamment → les patterns sont visibles).

La **gestion des clés** : rotation régulière, séparation des environnements (la clé de dev n'est pas la clé de prod), KMS (AWS KMS, HashiCorp Vault — les clés ne sont JAMAIS dans le code source). Le TLS (TLS 1.2 minimum, TLS 1.3 recommandé, cipher suites fortes, HSTS avec preload). Les erreurs courantes : secrets en clair dans le code, certificats auto-signés en production, algorithmes obsolètes (DES, RC4, MD5), sel fixe ou absent pour les mots de passe, clés privées dans les repos Git.

---


## Chapitre 10 — CSRF, clickjacking et attaques côté client

Le **CSRF** (Cross-Site Request Forgery — forcer le navigateur de la victime à envoyer une requête authentifiée vers un site vulnérable). Les protections : CSRF tokens (synchronizer pattern — un token unique par session, vérifié à chaque requête mutante), double submit cookie, et SameSite cookies (SameSite=Lax par défaut dans les navigateurs modernes réduit considérablement le risque CSRF — la majorité des formulaires cross-origin sont bloqués).

Le **clickjacking** (iframe invisible qui trompe l'utilisateur pour qu'il clique sur un bouton caché). Protection : X-Frame-Options: DENY ou CSP frame-ancestors 'none'. Les attaques côté client modernes : DOM clobbering (collision de noms entre les éléments du DOM et les variables JavaScript), prototype pollution (modifier Object.prototype pour injecter des propriétés dans tous les objets), postMessage abuse (messages cross-origin non validés).

---


## Chapitre 11 — Server-Side Request Forgery (SSRF)

Le mécanisme : l'attaquant fait envoyer des requêtes par le serveur vers des destinations non prévues — réseau interne, cloud metadata, services internes. L'**impact cloud** : accès au metadata endpoint AWS `169.254.169.254` → credentials IAM temporaires → compromission du compte cloud (le scénario Capital One 2019). Les techniques de bypass : encodage IP (décimal `2130706433` = 127.0.0.1, hexadécimal `0x7f000001`, IPv6 `::1`), DNS rebinding (le domaine résout vers l'IP interne après la validation), redirections (l'URL passe la validation mais redirige vers une cible interne).

Les défenses : allowlist de destinations autorisées (la seule protection fiable — si l'application doit accéder à un service externe, lister explicitement les URLs autorisées), blocage des IP internes et metadata (169.254.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), résolution DNS contrôlée (résoudre le DNS AVANT de vérifier l'IP — bloque le DNS rebinding), segmentation réseau (le service qui fait des requêtes sortantes n'a pas accès au réseau interne), et IMDSv2 sur AWS (nécessite un token pour accéder au metadata endpoint — bloque les SSRF simples).

> **🎯 SecureHealth — SSRF :** un nouveau microservice de génération de rapports PDF accepte une URL template. L'attaquant envoie `http://169.254.169.254/latest/meta-data/iam/security-credentials/` → récupère les credentials IAM. Correction : allowlist de templates internes + blocage des IP privées + migration vers IMDSv2.

---


## Chapitre 12 — File Upload, désérialisation et race conditions techniques

### 12.1 File Upload

Les attaques : webshell upload (un fichier PHP/ASPX uploadé et exécuté par le serveur web), path traversal dans le filename (`../../etc/cron.d/backdoor`), bypass de validation (extension double `shell.php.jpg`, magic bytes manipulés, Content-Type forgé). Les défenses : validation côté serveur (type MIME vérifié par le contenu, pas par l'extension ou le Content-Type), renommage aléatoire (UUID — le nom original n'est jamais utilisé), stockage hors du webroot (ou mieux : S3 avec des URLs pré-signées), scan antimalware, Content-Disposition: attachment (force le téléchargement, pas l'exécution).

### 12.2 Désérialisation

Les objets sérialisés exécutent du code au moment de la désérialisation — Java (`ObjectInputStream`), PHP (`unserialize()`), Python (`pickle.loads()`). Si les données sérialisées proviennent de l'utilisateur, l'attaquant peut injecter un objet qui exécute du code à la désérialisation. La règle : ne JAMAIS désérialiser des données non fiables. Alternatives : JSON (pas d'exécution de code), Protocol Buffers, MessagePack.

### 12.3 Race conditions techniques

*Ce chapitre traite les race conditions au niveau technique — les problèmes de concurrence dans le code et le système. Le Ch.7 traite les abus de concurrence au niveau logique métier (coupon stacking, double-spend fonctionnel).*

Le **TOCTOU** (Time of Check to Time of Use — le système vérifie une condition, puis agit sur cette condition, mais entre les deux un autre processus a modifié l'état. Exemple : vérifier qu'un fichier existe, puis le lire — entre la vérification et la lecture, le fichier a été remplacé par un lien symbolique vers /etc/shadow). Le **file write race** (deux processus écrivent le même fichier simultanément — corruption de données ou écrasement). Les **transactions non atomiques** (une opération en base de données qui devrait être atomique est implémentée en plusieurs requêtes séparées — entre les requêtes, un autre processus modifie les données).

Les défenses : **verrous** (mutexes, file locking — sérialiser les accès concurrents), **transactions atomiques** (BEGIN TRANSACTION / COMMIT — la base de données garantit l'atomicité), **isolation levels** (SERIALIZABLE pour les opérations critiques — empêche les lectures fantômes), **idempotency keys** (une clé unique par opération — si la même requête est envoyée deux fois, elle n'est exécutée qu'une fois), et **compare-and-swap** (vérifier que la valeur n'a pas changé entre la lecture et l'écriture).

---
