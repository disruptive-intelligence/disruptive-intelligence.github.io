---
title: 'Partie 4 — Envoyer des données : GET, POST, cookies, API'
source: IT/Fiche_Web-Requests.md
note: HTTP & requêtes web
up:
- - HTTP & requêtes web
  - index.md
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
