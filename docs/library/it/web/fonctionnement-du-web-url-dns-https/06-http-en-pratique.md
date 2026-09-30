---
title: HTTP en pratique
source: IT/Culture/Fiche_How-The-Web-Works.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
---

## 19. Headers HTTP importants

### À retenir
Les headers décrivent la requête/réponse. Plusieurs sont des **mines d'or** en pentest.

### Request headers (client)

- **Host** — domaine ciblé. *Cyber : certains headers comme `Host` ont un impact fort côté serveur, notamment sur les **virtual hosts**, les **reverse proxies** et les tests de **Host Header Injection**.*
- **User-Agent** — client/OS. *Cyber : falsifiable, test de filtrage.*
- **Referer** — page d'origine. *Cyber : falsifiable, ne jamais s'y fier.*
- **Accept** — types de média acceptés (`*/*` = tout).
- **Cookie** — identifiant de session côté client. *Cyber : vol = usurpation.*
- **Authorization** — token (`Basic …`, `Bearer …`). *Cyber : `Basic` = Base64 décodable.*
- **Content-Type** — type du body envoyé. *Cyber : influence l'interprétation serveur.*
- **Origin** — origine de la requête. *Cyber : central pour CORS/CSRF.*

### Response headers (serveur)

- **Server** — logiciel/version. *Cyber : fingerprinting → CVE.*
- **Set-Cookie** — pose un cookie.
- **Cache-Control** — durée de mise en cache.
- **WWW-Authenticate** — type d'auth requis.
- **Location** — cible d'une redirection (3xx).
- **Content-Type / Content-Length** — type et taille du body.

### Security headers (réponse)

- **Content-Security-Policy (CSP)** — sources autorisées. *Cyber : anti-XSS.*
- **Strict-Transport-Security (HSTS)** — force HTTPS. *Cyber : anti-downgrade/sniffing.*
- **X-Frame-Options** — anti-clickjacking.
- **Referrer-Policy** — contrôle l'envoi du Referer.
- **X-Content-Type-Options** — `nosniff`, empêche le MIME-sniffing.

### Commandes utiles

```bash
curl -I https://site.com           # headers de réponse seulement (HEAD)
curl -i https://site.com           # headers + body
curl -H 'X-Custom: valeur' URL     # header custom
```


### Point clé à mémoriser
`Server`, `Set-Cookie`, `Authorization` côté offensif ; CSP/HSTS/X-Frame-Options côté défensif.

---

## 20. Méthodes HTTP

### À retenir
La méthode dit **quelle action** le client demande sur la ressource.

### Comment ça fonctionne

| Méthode | Usage normal | Intérêt / risque pentest |
|---|---|---|
| **GET** | Lire une ressource (params dans l'URL) | Params visibles et loggés |
| **HEAD** | Comme GET, **headers seulement** | Reconnaissance (version), vérifier un lien |
| **POST** | Envoyer des données (body) | Login, upload |
| **PUT** | Créer/remplacer une ressource | **Danger** : upload malveillant si non sécurisé |
| **DELETE** | Supprimer une ressource | **Danger** : DoS / suppression critique |
| **OPTIONS** | Lister les méthodes acceptées | Énumération des méthodes autorisées |
| **PATCH** | Modifier partiellement | Update d'API |
| **TRACE** | Echo de la requête reçue | Risque de **Cross-Site Tracing** (XSS) |
| **CONNECT** | Établir un **tunnel** | Souvent via proxy (HTTPS) |

### Pourquoi c'est important en cyber
Les apps modernes utilisent surtout GET/POST, mais les **API REST/CRUD** exposent PUT/DELETE/PATCH. Une méthode dangereuse exposée **sans contrôle d'accès** = vulnérabilité critique.

### Commandes utiles

```bash
curl -X OPTIONS -i http://SERVER/   # quelles méthodes sont acceptées ?
```


### Point clé à mémoriser
PUT/DELETE mal sécurisées = upload ou suppression. TRACE = risque XSS. CONNECT = tunnel proxy.

---

## 21. Codes de statut HTTP

### À retenir
Les codes se rangent par **familles** : 1xx info, 2xx succès, 3xx redirection, 4xx erreur **client**, 5xx erreur **serveur**.

### Comment ça fonctionne

| Code | Signification | Intérêt cyber |
|---|---|---|
| **200 OK** | Succès, ressource renvoyée | — |
| **201 Created** | Ressource créée (POST/PUT) | Confirme une écriture réussie |
| **204 No Content** | Succès sans body | API silencieuse |
| **301 / 302** | Redirection permanente / temporaire | HTTP→HTTPS, post-login |
| **400 Bad Request** | Requête malformée | — |
| **401 Unauthorized** | **Authentification requise** | Zone protégée |
| **403 Forbidden** | **Accès refusé** : le serveur comprend la requête mais refuse l'accès, que l'utilisateur soit authentifié ou non | Souvent vu en bypass/WAF |
| **404 Not Found** | Ressource inexistante | Énumération fichiers/dossiers |
| **405 Method Not Allowed** | Méthode refusée | Indice sur les méthodes acceptées |
| **500 Internal Server Error** | Erreur serveur | **Fuite d'info** (stack traces) |

Clarification : **401** = authentification requise ; **403** = le serveur comprend la requête mais **refuse l'accès**, que l'utilisateur soit authentifié ou non ; **404** = n'existe pas ; **500** = le serveur a planté.

### Pourquoi c'est important en cyber
Les codes **guident l'énumération** : 401/403 révèlent des zones protégées, 404 sert au fuzzing de chemins, 500 peut fuiter des traces internes.

### Point clé à mémoriser
4xx = faute du client, 5xx = faute du serveur. 401 ≠ 403.

---

## 22. Cookies et sessions

### À retenir
Les cookies redonnent un **état** à un protocole HTTP **sans état**.

### Comment ça fonctionne

- **Set-Cookie** (réponse) : le serveur pose un cookie après login.
- **Cookie** (requête) : le client le **renvoie à chaque requête**.
- **PHPSESSID** : identifiant de session PHP typique.
- Le cookie est **stocké côté client**, mais référence souvent une **session maintenue côté serveur**.
- Attributs de sécurité : **Secure** (HTTPS only), **HttpOnly** (inaccessible au JS → anti-vol XSS), **SameSite** (anti-CSRF).

**Correction** : un cookie n'est pas « stocké côté serveur ». Il vit côté client ; c'est la **session** qu'il pointe qui peut être côté serveur.

### Pourquoi c'est important en cyber
Un **cookie de session valide = preuve d'identité** : souvent suffisant pour être authentifié **sans login**. Le voler (via XSS par ex.) = **usurpation de session**.

### Commandes utiles

```bash
curl -b 'PHPSESSID=xxxxxxxx' http://SERVER/   # envoyer un cookie de session
```


### Point clé à mémoriser
Cookie = côté client, session = côté serveur. Cookie de session volé = compte compromis. HttpOnly/Secure/SameSite limitent les dégâts.

---

## 23. Authentification web

### À retenir
Distinguer **authentification** (qui es-tu ?) et **autorisation** (as-tu le droit ?).

### Comment ça fonctionne

- **Basic Auth** : `Authorization: Basic <base64(user:pass)>`. Ex. `YWRtaW46YWRtaW4=` = `admin:admin`. **Encodé, pas chiffré.**
- **Bearer token / JWT** : `Authorization: Bearer <token>` — jeton signé, stocké côté client.
- **Cookie de session** : alternative la plus courante (voir §22).

### Pourquoi c'est important en cyber
Le **Basic Auth en Base64 est trivial à décoder** → jamais sécurisé sans HTTPS. Un JWT mal signé/validé est une faille classique.

### Commandes utiles

```bash
echo 'YWRtaW46YWRtaW4=' | base64 -d        # admin:admin
curl -u admin:admin http://SERVER/         # Basic Auth
curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://SERVER/
```


### Point clé à mémoriser
Authentification ≠ autorisation. Basic Auth = Base64 décodable, acceptable **seulement** sur HTTPS.

---

## 24. GET, POST et données envoyées

### À retenir
**GET** met les paramètres **dans l'URL** ; **POST** les met **dans le body**.

### Comment ça fonctionne

- **GET** : `search.php?q=london`. Visible dans **logs, historique, proxys** → jamais de secret dans l'URL.
- **POST** : données dans le body. Types courants :
  - `application/x-www-form-urlencoded` (formulaire classique)
  - `application/json` (API)
  - `multipart/form-data` (upload de fichiers)
- Avantages POST : moins de logs, accepte le binaire, plus de volume (l'URL est limitée à ~2000 caractères).

**Nuance** : POST n'est pas « secret » — le body peut être **loggé** par l'appli, un proxy ou un WAF.

### Pourquoi c'est important en cyber
Forger un POST manuellement permet de tester l'auth et les fonctions **sans le front-end**. Sans le bon `Content-Type`, le serveur **n'interprète pas** correctement un body JSON.

### Commandes utiles

```bash
curl -X POST -d 'username=admin&password=admin' http://SERVER/
curl -X POST -d '{"search":"london"}' -H 'Content-Type: application/json' http://SERVER/search.php
```


### Point clé à mémoriser
GET = params dans l'URL (loggés). POST = body, mais loggable aussi. JSON → `Content-Type: application/json` obligatoire.

---

## 25. API CRUD / REST

### À retenir
Une API CRUD associe une **opération** à une **méthode HTTP** sur une **ressource** (`/api.php/city/london`).

### Comment ça fonctionne

| Opération | Méthode | Effet |
|---|---|---|
| **Create** | POST | Ajoute une entrée |
| **Read** | GET | Lit une entrée |
| **Update** | PUT (ou PATCH) | Modifie une entrée |
| **Delete** | DELETE | Supprime une entrée |

`PUT` remplace toute l'entrée, `PATCH` modifie partiellement. `OPTIONS` indique les méthodes acceptées. L'auth passe par cookie ou header (JWT).

### Pourquoi c'est important en cyber
Une API qui autorise PUT/DELETE **sans contrôle d'accès** = faille critique. Risque **IDOR/BOLA** : un utilisateur accède à une ressource qui ne lui appartient pas en changeant un identifiant (`/city/london` → `/city/secret`).

### Commandes utiles

```bash
curl -s http://SERVER/api.php/city/london | jq          # Read (JSON formaté)
curl -X POST http://SERVER/api.php/city/ \
     -d '{"city_name":"HTB_City","country_name":"HTB"}' \
     -H 'Content-Type: application/json'                # Create
curl -X PUT http://SERVER/api.php/city/london \
     -d '{"city_name":"New_City","country_name":"HTB"}' \
     -H 'Content-Type: application/json'                # Update
curl -X DELETE http://SERVER/api.php/city/New_City      # Delete
```


### Point clé à mémoriser
CRUD = POST/GET/PUT/DELETE. Sans contrôle d'accès → faille (IDOR/BOLA).

---

## 26. cURL : lire et forger des requêtes

### À retenir
cURL est l'outil de base pour **fabriquer manuellement** n'importe quelle requête HTTP.

### Commandes utiles

```bash
curl URL                                  # GET simple
curl -v URL                               # requête + réponse complètes (verbose)
curl -I URL                               # headers seulement (HEAD)
curl -i URL                               # headers + body
curl -H 'Header: valeur' URL              # header custom (répétable)
curl -A 'Mozilla/5.0' URL                 # change le User-Agent
curl -u user:pass URL                     # Basic Auth
curl -b 'PHPSESSID=xxx' URL               # envoyer un cookie
curl -d 'a=1&b=2' -X POST URL             # POST form
curl -X POST -d '{"k":"v"}' -H 'Content-Type: application/json' URL   # POST JSON
curl -L URL                               # suivre les redirections
curl -k URL                               # ignorer le certificat TLS (LAB)
curl -s URL | jq                          # JSON propre
curl -X OPTIONS -i http://SERVER/         # méthodes acceptées
```


### Point clé à mémoriser
`-v` pour tout voir, `-H` pour forger, `-d` pour POSTer, `-b` pour les cookies, `-L` pour les redirections.

---

## 27. DevTools navigateur

### À retenir
**F12** / **Ctrl+Shift+I** → onglet **Network** = cœur de l'analyse web.

### Comment ça fonctionne

- Voir toutes les **requêtes** (statut, méthode, URL).
- Lire les **headers** (request + response, bouton **Raw**).
- Voir les **paramètres / payload** GET et POST.
- **Cookies / Storage** : inspecter et modifier les cookies.
- **Copy → Copy as cURL** : rejouer la requête au terminal.
- **Copy → Copy as Fetch** : rejouer en JS dans la console.

### Pourquoi c'est important en cyber
Permet de comprendre comment l'app dialogue avec son **backend**, et de **rejouer/modifier** une requête sans passer par l'UI — bien plus rapide pour tester.

### Point clé à mémoriser
Network + Copy as cURL = rejouer n'importe quelle requête en quelques secondes.

---
