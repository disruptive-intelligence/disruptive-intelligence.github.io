---
title: Anatomie d'un échange HTTP
source: IT/Fiche_Web-Requests.md
note: HTTP & requêtes web
up:
- - HTTP & requêtes web
  - index.md
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
