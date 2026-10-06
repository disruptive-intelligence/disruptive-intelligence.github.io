---
title: Chapitre 11 — HTTP et le fonctionnement du web
source: IT/04 Réseau/Comprendre le réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie III — Services et protocoles applicatifs
  - index.md
---

## 11.1 L'URL

Une **URL** décrit comment atteindre une ressource :

```text
https://user:pass@www.example.com:443/dossier/page.php?id=42#section
└─┬─┘   └───┬───┘ └──────┬──────┘└┬┘└──────┬──────────┘└──┬─┘└──┬──┘
schéma  identifiants    hôte    port     chemin        requête fragment
```


## 11.2 Requête et réponse

**HTTP** définit le dialogue entre un client (navigateur) et un serveur web. Une requête minimale tient en une ligne (`GET / HTTP/1.1`) ; les en-têtes suivent :

```http
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 Firefox/129.0
Referer: https://example.com/
```


```http
HTTP/1.1 200 OK
Server: nginx/1.25.3
Date: Thu, 02 Oct 2026 09:34:03 GMT
Content-Type: text/html
Content-Length: 98

<html>
<head><title>Example</title></head>
<body>Bienvenue</body>
</html>
```


## 11.3 Les méthodes

| Méthode | Rôle | Remarque d'analyste |
|---|---|---|
| **GET** | Lire une ressource | Les paramètres sont dans l'URL (donc dans les journaux) |
| **HEAD** | Comme GET, sans le corps | Reconnaissance : version du serveur, lien mort |
| **POST** | Envoyer des données (formulaire, connexion) | Les données sont dans le corps |
| **PUT** | Créer ou remplacer une ressource à une URI précise | Rarement attendu sur un site public |
| **DELETE** | Supprimer une ressource | Suspect s'il apparaît sur un serveur public |
| **OPTIONS** | Lister les méthodes acceptées | Souvent émis par des scanners |
| **TRACE** | Renvoyer la requête reçue (écho) | À désactiver |
| **CONNECT** | Ouvrir un tunnel via un proxy | Utilisé pour HTTPS à travers un proxy explicite |

## 11.4 Les codes de réponse

| Plage | Famille | Codes fréquents |
|---|---|---|
| **1xx** | Information | 101 Switching Protocols (WebSocket) |
| **2xx** | Succès | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirection | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | Erreur du client | 400 Bad Request, 401 Unauthorized (authentification requise), **403 Forbidden** (la ressource existe mais l'accès est refusé), 404 Not Found, 429 Too Many Requests |
| **5xx** | Erreur du serveur | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

## 11.5 Les en-têtes et les cookies

| En-tête | Sens | Rôle |
|---|---|---|
| `Host` | Requête | Choisit le site parmi ceux hébergés sur le même serveur |
| `User-Agent` | Requête | Navigateur et version |
| `Content-Length` | Les deux | Taille du corps |
| `Cookie` | Requête | Renvoie les cookies reçus |
| `Set-Cookie` | Réponse | Dépose un cookie |
| `Cache-Control` | Réponse | Durée de mise en cache |
| `Content-Type` | Réponse | Type du contenu (HTML, JSON, PDF…) |
| `Location` | Réponse | Cible d'une redirection |

HTTP est **sans état** : chaque requête est indépendante. Le **cookie** — petite donnée déposée par `Set-Cookie` et renvoyée à chaque requête — permet au serveur de reconnaître la session, les préférences ou une visite antérieure. Un cookie de session vaut une authentification : d'où les attributs `Secure` (HTTPS seulement), `HttpOnly` (inaccessible au JavaScript) et `SameSite`.

## 11.6 Ce que le serveur renvoie : HTML, CSS, JavaScript

Le serveur renvoie une page **HTML** (la structure), stylée par du **CSS** et animée par du **JavaScript** exécuté dans le navigateur.

![Structure d'une page HTML](../../../../assets/reseau-image-27.png)

| Balise | Rôle |
|---|---|
| `<!DOCTYPE html>` | Déclare un document HTML5 |
| `<html>` | Élément racine |
| `<head>` | Métadonnées (titre, encodage, scripts, styles) |
| `<body>` | Contenu affiché |
| `<h1>` … `<h6>` | Titres |
| `<p>` | Paragraphe |

Le détail de HTTP et des applications web est traité dans les cours *Fonctionnement du web* et *HTTP & requêtes web*.

---
