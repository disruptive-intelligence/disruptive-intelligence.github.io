---
title: 'Outils : cURL et DevTools'
source: IT/05 Web & applications/HTTP & requêtes web.md
note: HTTP & requêtes web
up:
- - HTTP & requêtes web
  - index.md
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
