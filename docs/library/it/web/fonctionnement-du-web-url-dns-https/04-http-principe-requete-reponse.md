---
title: 'HTTP : principe, requête, réponse'
source: IT/05 Web & applications/Le web/Fonctionnement du web - URL, DNS, HTTPS.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
---

## 10. HTTP : principe général

### À retenir
HTTP (**HyperText Transfer Protocol**) est un protocole applicatif **client ↔ serveur** : le client demande, le serveur répond. **Sans état** par défaut, **port 80**, données **en clair**.

### Comment ça fonctionne
Le client envoie une **requête** (méthode + ressource), le serveur renvoie une **réponse** (code + contenu). Chaque requête est indépendante : HTTP ne « se souvient » de rien — d'où le besoin de cookies/sessions (voir §22).

### Pourquoi c'est important en cyber
HTTP **ne chiffre rien**. En capture réseau, **tout** est lisible : credentials, cookies, paramètres, contenu. Un Wi-Fi public + HTTP = capture triviale (MiTM).

### Comment ça fonctionne — déroulé HTTP simple

1. L'utilisateur tape une URL en `http://`.
2. Le navigateur extrait le host, le path et éventuellement les paramètres.
3. Le système résout le nom de domaine en adresse IP via **DNS**.
4. Le client ouvre une **connexion TCP** vers le serveur sur le **port 80**.
5. Le navigateur construit une **requête HTTP** : méthode, path, version, headers, body éventuel.
6. Le serveur web reçoit la requête sur le **port 80**.
7. Le serveur identifie le site demandé grâce au header **`Host`**.
8. Le serveur cherche la **ressource** demandée : fichier HTML, endpoint API, image, etc.
9. Le serveur renvoie une **réponse HTTP** : code de statut, headers, body.
10. Le navigateur lit la réponse, **interprète** le contenu et déclenche éventuellement d'autres requêtes (CSS, JS, images, API).

```text
URL HTTP → DNS → TCP:80 → HTTP request → serveur web → HTTP response → navigateur
```


- En HTTP, **tout est en clair**.
- Headers, cookies, paramètres et body peuvent être **lus en capture réseau**.
- HTTP est **sans état** : les cookies/sessions servent à maintenir une identité entre plusieurs requêtes.

### Point clé à mémoriser
HTTP = client demande / serveur répond, en clair, sans état, sur le port 80.

---

## 11. Requête HTTP

### À retenir
Structure : **request line** (méthode + path + version), puis **headers**, une **ligne vide**, et un **body** éventuel.

### Comment ça fonctionne

```
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/
```

- `GET / HTTP/1.1` → méthode + ressource ciblée + version du protocole.
- `Host:` → quel site (un serveur peut en héberger plusieurs).
- `User-Agent:` → identité du client (navigateur, OS).
- `Referer:` → page d'origine de la requête.

| Champ | Exemple | Rôle |
|---|---|---|
| Méthode | `GET` | Action demandée |
| Path | `/users/login.html` | Ressource ciblée |
| Version | `HTTP/1.1` | Version du protocole |

### Pourquoi c'est important en cyber
Tous ces headers sont **forgeables** (cURL, Burp). On peut usurper un User-Agent, falsifier un Referer, viser un virtual host via Host.

### Point clé à mémoriser
Ligne 1 = méthode + path + version. Puis headers, ligne vide, body éventuel.

---

## 12. Réponse HTTP

### À retenir
Structure : **status line** (version + code), puis **headers**, et le **body** (HTML, CSS, JS, JSON, image, PDF…).

### Comment ça fonctionne

```
HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98

<html>
  <head><title>TryHackMe</title></head>
  <body>Welcome To TryHackMe.com</body>
</html>
```


### Pourquoi c'est important en cyber
Le header `Server:` fuit la version du logiciel → **fingerprinting** et recherche de **CVE**. Le body n'est pas que du HTML : une API renvoie souvent du JSON exploitable directement.

### Point clé à mémoriser
Ligne 1 = version + code de statut. Le body peut être HTML, JSON, fichiers…

---

## 13. HTML, CSS, JavaScript : ce que le navigateur rend

### À retenir
Le navigateur reçoit des ressources et les **interprète** : HTML pour la **structure**, CSS pour le **style**, JavaScript pour le **comportement dynamique**.

### Comment ça fonctionne
Une page moderne déclenche **plusieurs requêtes supplémentaires** (CSS, JS, images, polices, appels API). Le HTML de base :

```html
<!DOCTYPE html>        <!-- déclare un document HTML -->
<html>                 <!-- élément racine -->
  <head>               <!-- métadonnées (titre, liens) -->
    <title>...</title>
  </head>
  <body>               <!-- contenu affiché -->
    <h1>Titre</h1>     <!-- grand titre -->
    <p>Paragraphe</p>  <!-- paragraphe -->
  </body>
</html>
```


### Pourquoi c'est important en cyber
Le JavaScript côté client est lisible et analysable (endpoints cachés, clés exposées, logique d'auth). C'est aussi le terrain du **XSS**. Chaque requête secondaire est une cible potentielle.

### Point clé à mémoriser
HTML = structure, CSS = style, JS = comportement. Une page = souvent des dizaines de requêtes.

---
