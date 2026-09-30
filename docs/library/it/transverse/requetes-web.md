---
title: Requêtes web
source: IT/Fiche_Web-Requests.md
---

> Fiche de révision orientée pratique cyber (HTB / eJPT / pentest débutant).

---

## 1. HTTP : principe général

### À retenir
HTTP est un protocole applicatif **client ↔ serveur**. Le client (navigateur, cURL) envoie une **requête**, le serveur traite et renvoie une **réponse** (ex. une page HTML). Port par défaut : **80** (non chiffré).

### Pourquoi c'est important en cyber
Comprendre le cycle requête/réponse est la base de tout test web. Tout ce qui passe en HTTP circule en **clair-text** et peut être intercepté (MiTM).

### Point clé à mémoriser
HTTP = client demande, serveur répond, en clair, sur le port 80.

---

## 2. URL : structure

### À retenir
```
http://admin:password@inlanefreight.com:80/dashboard.php?login=true#status
└─┬─┘ └──────┬───────┘ └────────┬────────┘└┬┘└─────┬──────┘└────┬─────┘└──┬──┘
scheme   user info           host        port    path      query string fragment
```

| Composant | Exemple | Rôle |
|---|---|---|
| **Scheme** | `http://` `https://` | Protocole utilisé |
| **User Info** | `admin:password@` | Identifiants (optionnel) |
| **Host** | `inlanefreight.com` | Nom de domaine ou IP |
| **Port** | `:80` | Port (80 HTTP / 443 HTTPS par défaut) |
| **Path** | `/dashboard.php` | Ressource ciblée (fichier/dossier) |
| **Query String** | `?login=true` | Paramètres `clé=valeur`, séparés par `&` |
| **Fragment** | `#status` | Section interne, traitée côté client |

### Point clé à mémoriser
Seuls **scheme** et **host** sont obligatoires. Le reste est optionnel.

---

## 3. HTTP Flow

### À retenir
1. L'utilisateur saisit le domaine (`inlanefreight.com`).
2. **Résolution DNS** : le domaine est traduit en IP (le navigateur consulte d'abord `/etc/hosts`).
3. Le navigateur envoie un **GET /** sur le port 80.
4. Le serveur renvoie une **réponse HTTP** (ex. `200 OK` + `index.html`).
5. Le navigateur **rend** la page.

### Pourquoi c'est important en cyber
`/etc/hosts` permet de forcer une résolution DNS locale (utile pour viser un lab ou bypasser le DNS). Format : `IP   domaine`.

### Point clé à mémoriser
Pas d'IP = pas de communication. Le DNS traduit toujours le domaine avant la requête.

---

## 4. HTTPS

### À retenir
HTTPS = HTTP **chiffré** via TLS. Port **443**. Même si le trafic est intercepté, les données restent illisibles (un seul flux chiffré).

- **HTTP** : tout en clair (identifiants visibles dans Wireshark).
- **HTTPS** : handshake TLS + échange de certificats → chiffrement.
- Visiter un site HTTP qui force HTTPS → redirection **301** vers le port 443, puis handshake TLS.

### Pourquoi c'est important en cyber
HTTP expose les credentials sur le réseau (Wi-Fi public = capture facile). Même en HTTPS, un **DNS en clair** peut révéler les sites visités → utiliser DNS chiffré (8.8.8.8, 1.1.1.1) ou VPN. Attention aux **HTTP downgrade attacks** (MiTM).

### Commandes utiles
```bash
curl -k https://inlanefreight.com   # ignore les erreurs de certificat (labs/SSL invalide)
```

### Point clé à mémoriser
HTTPS chiffre tout sur le port 443. `-k` ignore le certificat (à n'utiliser qu'en lab).

---

## 5. Requête HTTP

### À retenir
Première ligne = **Méthode + Path + Version**, suivie des **headers**, puis d'un **body** éventuel.

```
GET /users/login.html HTTP/1.1
Host: inlanefreight.com
User-Agent: Mozilla/5.0
Cookie: PHPSESSID=c4ggt4jull9obt7aupa55o8vbf
```

| Champ | Exemple | Rôle |
|---|---|---|
| Méthode | `GET` | Action à effectuer |
| Path | `/users/login.html` | Ressource ciblée |
| Version | `HTTP/1.1` | Version du protocole |

### Point clé à mémoriser
Ligne 1 = méthode + chemin + version. Puis headers, puis body éventuel.

---

## 6. Réponse HTTP

### À retenir
Première ligne = **Version + Code de statut**, suivie des **headers**, puis du **body** (HTML, JSON, image, PDF…).

```
HTTP/1.1 200 OK
Server: Apache/2.4.41
Set-Cookie: PHPSESSID=m4u64rqlpfthrvvb12ai9voqgf
Content-Type: text/html; charset=UTF-8
```

### Point clé à mémoriser
Ligne 1 = version + code. Le body peut être bien plus que du HTML (JSON, fichiers).

---

## 7. Headers HTTP importants

> **Définition courte + intérêt cyber** pour chaque header.

### Request headers (envoyés par le client)
- **Host** — domaine/IP ciblé. *Cyber : un même serveur héberge plusieurs sites → cible d'énumération (virtual hosts).*
- **User-Agent** — décrit le client (navigateur, OS). *Cyber : manipulable, utile pour usurper un client ou tester du filtrage.*
- **Referer** — d'où vient la requête. *Cyber : facilement falsifiable, ne jamais s'y fier pour la sécurité.*
- **Accept** — types de média acceptés (`*/*` = tout).
- **Cookie** — `nom=valeur`, identifiant de session côté client. *Cyber : vol de cookie = vol de session.*
- **Authorization** — token d'authentification (`Basic …`, `Bearer …`). *Cyber : `Basic` = Base64 décodable.*

### Response headers (envoyés par le serveur)
- **Server** — logiciel/version du serveur (ex. `Apache/2.2.14`). *Cyber : fuite d'info → fingerprinting et recherche de CVE.*
- **Set-Cookie** — pose un cookie côté client.
- **WWW-Authenticate** — type d'auth requis (ex. `Basic realm="..."`).

### Entity headers (décrivent le contenu)
- **Content-Type** — type de la ressource (`text/html`, `application/json`). *Cyber : crucial, influence l'interprétation de l'input par le serveur.*
- **Content-Length** — taille du body.
- **Content-Encoding** — compression (ex. `gzip`).

### Security headers (réponse)
- **Content-Security-Policy (CSP)** — sources autorisées. *Cyber : protège contre le XSS.*
- **Strict-Transport-Security (HSTS)** — force HTTPS. *Cyber : empêche le sniffing / downgrade.*
- **Referrer-Policy** — contrôle l'envoi du Referer. *Cyber : évite la fuite d'URLs sensibles.*

### Commandes utiles
```bash
curl -I https://site.com          # HEAD : affiche seulement les headers de réponse
curl -i https://site.com          # affiche headers + body
curl -H 'Header: valeur' URL      # envoyer un header custom
```

### Point clé à mémoriser
Les headers `Server`, `Set-Cookie` et `Authorization` sont des mines d'or en pentest.

---

## 8. Méthodes HTTP

### À retenir

| Méthode | Rôle | Intérêt / Risque en pentest |
|---|---|---|
| **GET** | Lire une ressource (params dans l'URL) | Params visibles/loggés |
| **POST** | Envoyer des données (body) | Login, upload de fichiers |
| **HEAD** | Comme GET mais sans body | Vérifier la taille avant de télécharger |
| **PUT** | Créer une ressource | **Danger** : upload de fichier malveillant si non sécurisé |
| **DELETE** | Supprimer une ressource | **Danger** : DoS / suppression de fichiers critiques |
| **OPTIONS** | Liste les méthodes acceptées | Énumération des méthodes autorisées |
| **PATCH** | Modifier partiellement une ressource | Update d'API |

### Pourquoi c'est important en cyber
Les apps modernes utilisent surtout **GET** et **POST**, mais les **REST/CRUD APIs** exposent aussi **PUT/DELETE**. Une méthode dangereuse exposée sans contrôle = vulnérabilité critique.

### Point clé à mémoriser
PUT et DELETE mal sécurisées = upload malveillant ou suppression de données.

---

## 9. Codes de statut HTTP

### À retenir — les familles
- **1xx** : informationnel
- **2xx** : succès
- **3xx** : redirection
- **4xx** : erreur **client**
- **5xx** : erreur **serveur**

### Codes utiles
| Code | Signification | Intérêt cyber |
|---|---|---|
| **200 OK** | Succès, ressource renvoyée | — |
| **301 / 302** | Redirection (permanente / temporaire) | Ex. redirection HTTP→HTTPS ou post-login |
| **400 Bad Request** | Requête malformée | — |
| **401 Unauthorized** | Authentification requise | Indique une zone protégée |
| **403 Forbidden** | Accès interdit (ou input malveillant détecté) | Souvent vu lors de bypass |
| **404 Not Found** | Ressource inexistante | Énumération de fichiers/dossiers |
| **500 Internal Server Error** | Erreur serveur | **Fuite d'info** possible (stack traces) |

### Point clé à mémoriser
4xx = ta faute (client), 5xx = sa faute (serveur). Les 401/403/404/500 guident l'énumération.

---

## 10. cURL : commandes essentielles

| Commande | Explication |
|---|---|
| `curl URL` | Requête GET simple |
| `curl -O URL` | Télécharge dans un fichier (nom distant) |
| `curl -s URL` | Mode silencieux (pas de barre de progression) |
| `curl -I URL` | Affiche seulement les headers (HEAD) |
| `curl -i URL` | Affiche headers + body |
| `curl -v URL` | Mode verbose (requête + réponse complètes) |
| `curl -k URL` | Ignore le certificat TLS |
| `curl -H 'Header: val' URL` | Envoie un header custom (répétable) |
| `curl -A 'Mozilla/5.0' URL` | Change le User-Agent |
| `curl -u admin:admin URL` | Basic Auth |
| `curl -X POST -d 'a=1&b=2' URL` | Requête POST avec données |
| `curl -X POST -d '{"k":"v"}' -H 'Content-Type: application/json' URL` | POST JSON |
| `curl -b 'PHPSESSID=xxx' URL` | Envoie un cookie |
| `curl -L URL` | Suit les redirections |

### Point clé à mémoriser
`-v` pour tout voir, `-H` pour forger des headers, `-d` pour POSTer, `-b` pour les cookies.

---

## 11. DevTools navigateur

### À retenir
Ouvrir avec **F12** ou **Ctrl+Shift+I**. Onglet **Network** = cœur de l'analyse web.

- Voir toutes les **requêtes** (statut, méthode, URL, path).
- Lire les **headers** (request + response, bouton **Raw** pour le brut).
- Voir les **paramètres GET/POST** (onglet Request → Raw).
- **Copy → Copy as cURL** : rejouer la requête dans le terminal.
- **Copy → Copy as Fetch** : rejouer en JS dans la console.
- Onglet **Cookies / Storage** : inspecter et modifier les cookies.

### Pourquoi c'est important en cyber
Permet de comprendre comment l'app communique avec son backend, et de **rejouer/modifier** des requêtes directement (test plus rapide que via l'UI).

### Point clé à mémoriser
Network + Copy as cURL = rejouer n'importe quelle requête en quelques secondes.

---

## 12. GET et paramètres

### À retenir
Les paramètres GET sont **dans l'URL** : `search.php?search=london`. Un seul `?`, plusieurs params séparés par `&`.

```bash
curl 'http://SERVER/search.php?search=le' -H 'Authorization: Basic YWRtaW46YWRtaW4='
```

### Pourquoi c'est important en cyber
Repérer la page réelle interrogée par une fonction (ex. une recherche appelle `search.php`) permet de l'attaquer directement, souvent en récupérant du JSON brut.

### Point clé à mémoriser
GET = paramètres visibles dans l'URL → faciles à manipuler et à logger.

---

## 13. POST, formulaires et JSON

### À retenir
POST place les données dans le **body** (pas dans l'URL).

**3 avantages du POST :** moins de logs, moins d'encodage (accepte le binaire), plus de données possibles (l'URL est limitée à ~2000 caractères).

```bash
# Formulaire classique
curl -X POST -d 'username=admin&password=admin' http://SERVER/

# Données JSON (header Content-Type obligatoire)
curl -X POST -d '{"search":"london"}' \
     -H 'Content-Type: application/json' \
     -b 'PHPSESSID=xxx' http://SERVER/search.php
```

### Pourquoi c'est important en cyber
Savoir forger manuellement un POST (login, JSON) permet de tester l'auth et les fonctions sans passer par le front-end. Sans le bon `Content-Type`, le serveur n'interprète pas correctement le body.

### Point clé à mémoriser
POST = données dans le body. Pour du JSON : `-H 'Content-Type: application/json'` est indispensable.

---

## 14. Cookies et authentification

### À retenir
- **Set-Cookie** (réponse) : le serveur pose un cookie après login.
- **Cookie** (requête) : le client le renvoie à chaque requête.
- **PHPSESSID** : identifiant de session PHP typique.
- Un **cookie valide = preuve de session** → souvent suffisant pour être authentifié sans login.
- **Cookie** : stocké côté client **et** serveur. **Authorization (token/JWT)** : stocké uniquement côté client.
- **Basic Auth** : `Authorization: Basic <base64(user:pass)>` → ex. `YWRtaW46YWRtaW4=` = `admin:admin`. **Encodé, pas chiffré.**

```bash
curl -u admin:admin http://SERVER/                 # Basic Auth
curl http://admin:admin@SERVER/                    # via l'URL
curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://SERVER/   # header manuel
curl -b 'PHPSESSID=xxx' http://SERVER/             # cookie de session
```

### Pourquoi c'est important en cyber
Voler ou rejouer un cookie de session permet d'usurper un utilisateur (cf. XSS). Le Basic Auth en Base64 est trivial à décoder → jamais sécurisé sans HTTPS.

### Point clé à mémoriser
`Basic <base64>` se décode en une commande. Un cookie de session volé = compte compromis.

---

## 15. API CRUD

### À retenir
Une API CRUD associe une **opération** à une **méthode HTTP** sur une ressource (`/api.php/city/london`).

| Opération | Méthode HTTP | Effet |
|---|---|---|
| **Create** | POST | Ajoute une entrée |
| **Read** | GET | Lit une entrée |
| **Update** | PUT (ou PATCH) | Modifie une entrée |
| **Delete** | DELETE | Supprime une entrée |

> `PUT` = remplace toute l'entrée, `PATCH` = modification partielle. `OPTIONS` indique laquelle est acceptée.

### Commandes utiles
```bash
# Read (jq formate le JSON)
curl -s http://SERVER/api.php/city/london | jq

# Create
curl -X POST http://SERVER/api.php/city/ \
     -d '{"city_name":"HTB_City","country_name":"HTB"}' \
     -H 'Content-Type: application/json'

# Update
curl -X PUT http://SERVER/api.php/city/london \
     -d '{"city_name":"New_HTB_City","country_name":"HTB"}' \
     -H 'Content-Type: application/json'

# Delete
curl -X DELETE http://SERVER/api.php/city/New_HTB_City
```

### Pourquoi c'est important en cyber
Une API qui autorise PUT/DELETE **sans contrôle d'accès** = vulnérabilité critique (n'importe qui modifie/supprime des données). L'auth se fait via cookie ou header (JWT).

### Point clé à mémoriser
CRUD = POST/GET/PUT/DELETE. Sans contrôle d'accès, c'est une faille.

---

## 16. Points de vigilance cyber

| Sujet | Risque |
|---|---|
| **HTTP en clair** | Credentials et données interceptables (MiTM, Wi-Fi public) |
| **Cookies de session** | Vol = usurpation de session (XSS) |
| **Headers manipulables** | `User-Agent`, `Referer` falsifiables → ne jamais s'y fier pour la sécurité |
| **Basic Auth en Base64** | Encodé ≠ chiffré, décodable instantanément |
| **Méthodes dangereuses** | PUT/DELETE exposées sans contrôle → upload/suppression |
| **API sans contrôle d'accès** | Lecture/écriture/suppression libre de données |
| **Fuite d'info** | Header `Server` (version → CVE), erreurs **5xx** (stack traces) |

---

## ⭐ Commandes cURL à connaître par cœur

```bash
curl URL                                    # GET simple
curl -v URL                                 # requête + réponse complètes
curl -I URL                                 # headers seulement (HEAD)
curl -k URL                                 # ignore le certificat TLS
curl -H 'Header: valeur' URL                # header custom
curl -A 'Mozilla/5.0' URL                   # change le User-Agent
curl -u user:pass URL                       # Basic Auth
curl -X POST -d 'a=1&b=2' URL               # POST form
curl -X POST -d '{"k":"v"}' -H 'Content-Type: application/json' URL   # POST JSON
curl -b 'PHPSESSID=xxx' URL                 # cookie
curl -L URL                                 # suivre les redirections
curl -s URL | jq                            # JSON propre
```

---

## ⚠️ Erreurs fréquentes à éviter

- Oublier `-H 'Content-Type: application/json'` en POSTant du JSON.
- Confondre **301/302** (redirection) avec une erreur → utiliser `-L`.
- Croire que **Basic Auth** est sécurisé (c'est du Base64).
- Confondre **4xx** (client) et **5xx** (serveur).
- Oublier le cookie de session (`-b`) → on retombe sur le login.
- Se fier aux headers `Referer` / `User-Agent` côté serveur (falsifiables).
- Utiliser `-k` en production (uniquement pour les labs).

---

## 🎯 Résumé ultra-court pour entretien

> HTTP est un protocole client/serveur en clair (port 80) ; HTTPS le chiffre via TLS (port 443). Une requête = méthode + path + version + headers + body éventuel ; une réponse = version + code de statut + headers + body. Les méthodes clés sont GET (params dans l'URL), POST (données dans le body), et PUT/DELETE pour les APIs CRUD. Les codes : 2xx succès, 3xx redirection, 4xx erreur client, 5xx erreur serveur. Côté sécurité : cookies de session (vol = usurpation), Basic Auth en Base64 (décodable), headers manipulables, et APIs sans contrôle d'accès. cURL et les DevTools (onglet Network) permettent de forger et rejouer n'importe quelle requête.

---

## 🧠 Mini-quiz (10 questions)

1. **Quel est le port par défaut de HTTP ? De HTTPS ?**
2. **Quels sont les deux composants obligatoires d'une URL ?**
3. **Quelle est la différence entre 4xx et 5xx ?**
4. **Que signifie le code 401 ? Et 403 ?**
5. **Où sont placés les paramètres en GET ? En POST ?**
6. **Quel header est indispensable pour POSTer du JSON ?**
7. **Comment décoder une valeur `Authorization: Basic` ?**
8. **À quoi sert le flag `-k` de cURL ?**
9. **Quelle méthode HTTP correspond à l'opération "Update" en CRUD ?**
10. **Pourquoi un cookie de session volé est-il dangereux ?**

<details markdown="1">
<summary>Réponses</summary>

1. HTTP = **80**, HTTPS = **443**.
2. Le **scheme** et le **host**.
3. **4xx** = erreur côté **client** (mauvaise requête), **5xx** = erreur côté **serveur**.
4. **401** = authentification requise ; **403** = accès interdit (droits insuffisants ou input malveillant détecté).
5. GET = dans l'**URL** (query string) ; POST = dans le **body**.
6. `Content-Type: application/json`.
7. C'est du **Base64** : `echo 'YWRtaW46YWRtaW4=' | base64 -d` → `admin:admin`.
8. **Ignorer le certificat TLS** (utile en lab / certificat invalide).
9. **PUT** (ou **PATCH** pour une modification partielle).
10. Il prouve la session → permet d'**usurper l'utilisateur** sans connaître son mot de passe.

</details>
