---
title: Synthèse et révision
source: IT/05 Web & applications/HTTP & requêtes web.md
note: HTTP & requêtes web
up:
- - HTTP & requêtes web
  - index.md
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
