---
title: Synthèse et révision
source: IT/05 Web & applications/Le web/Fonctionnement du web - URL, DNS, HTTPS.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
---

## 28. Points de vigilance cyber

| Sujet | Risque |
|---|---|
| **HTTP en clair** | Credentials/données interceptables (MiTM, Wi-Fi public) |
| **DNS non chiffré** | Fuite des sites visités, base du spoofing |
| **DNS spoofing** | Redirection vers une machine attaquante |
| **Certificat invalide** | Authenticité non prouvée → MiTM possible |
| **`curl -k` hors lab** | Validation désactivée → MiTM |
| **Basic Auth sans HTTPS** | Base64 sniffé et décodé instantanément |
| **Cookies de session** | Vol = usurpation (XSS) |
| **Secrets dans la query string** | Fuite via logs/historique/proxy |
| **Headers manipulables** | `User-Agent`/`Referer` falsifiables → jamais s'y fier |
| **Méthodes dangereuses** | PUT/DELETE exposées → upload/suppression |
| **API sans contrôle d'accès** | Lecture/écriture/suppression libres (IDOR/BOLA) |
| **Fuite d'info** | Header `Server` (→ CVE), erreurs 5xx (stack traces) |

---

## 29. Synthèse mentale

```text
HTTP :
URL → DNS → IP → ARP/gateway → TCP:80 → HTTP request en clair → HTTP response en clair → rendu navigateur
```


```text
HTTPS :
URL → DNS → IP → ARP/gateway → TCP:443 → TLS handshake → tunnel chiffré → HTTP request chiffrée → HTTP response chiffrée → rendu navigateur
```


> **La différence clé** : en HTTP, la requête part directement après TCP ; en HTTPS, une couche TLS est négociée **avant** d'envoyer la requête HTTP.

Vue détaillée de bout en bout :

```
URL
 └─ DNS  ──────────── nom → IP (cache → hosts → resolver → root → TLD → authoritative)
     └─ ARP/gateway ── trouver la MAC du routeur, sortir du réseau local
         └─ TCP ────── handshake SYN / SYN-ACK / ACK
             └─ TLS ── (si HTTPS) ClientHello → certificat → clé de session → symétrique
                 └─ HTTP request ── méthode + path + headers (+ body)
                     └─ serveur traite
                         └─ HTTP response ── code + headers + body
                             └─ cookies/session ── maintien de l'état
                                 └─ navigateur ── rend HTML/CSS/JS (+ requêtes secondaires)
```


---

## 30. Commandes à connaître par cœur

```bash
# DNS
nslookup google.com
dig google.com MX

# HTTP / cURL
curl URL
curl -v URL
curl -I URL
curl -H 'Header: val' URL
curl -X POST -d 'a=1&b=2' URL
curl -b 'PHPSESSID=xxx' URL
curl -k URL                 # lab uniquement
curl -s URL | jq
```


---

## 31. Erreurs fréquentes à éviter

- Croire que **HTTPS cache tout** (le DNS/SNI peut révéler le domaine).
- Croire que **DNS public = DNS chiffré** (il faut DoH/DoT).
- Utiliser **`-k` hors lab** (désactive la validation → MiTM).
- Croire que **Basic Auth chiffre** (c'est du Base64).
- Oublier **`Content-Type: application/json`** en POSTant du JSON.
- Oublier le **cookie de session** (`-b`) → on retombe sur le login.
- Confondre **401** (authentification requise) et **403** (interdit).
- Mettre des **secrets dans l'URL** (loggés partout).
- Croire que **POST ne peut pas être loggé**.
- Oublier que le **fragment `#section`** reste côté client.
- Croire que **HTTPS est un protocole totalement différent** de HTTP : c'est **HTTP encapsulé dans TLS**.
- Croire que le **certificat sert à chiffrer directement** tout le trafic : il sert surtout à **authentifier le serveur** et à permettre l'établissement sécurisé d'un secret partagé.
- Croire que **`curl -k` désactive le chiffrement** : il désactive surtout la **validation du certificat** (la connexion reste chiffrée).
- Croire que **403 signifie toujours « connecté mais pas autorisé »** : cela signifie surtout **« accès refusé »**, authentifié ou non.

---

## 32. Résumé ultra-court pour entretien

> Quand on tape une URL, le navigateur l'analyse, puis résout le nom via **DNS** (cache → hosts → resolver → root → TLD → autoritaire) pour obtenir une **IP**. Sur le réseau local, **ARP** trouve la gateway, puis un **handshake TCP** (SYN/SYN-ACK/ACK) ouvre la connexion. En **HTTPS**, un **handshake TLS** vérifie le certificat du serveur et établit une **clé de session** (asymétrique pour s'installer, symétrique pour la suite). Le navigateur envoie alors une **requête HTTP** (méthode + path + headers + body), le serveur répond (code + headers + body). Les **cookies/sessions** maintiennent l'état d'un protocole sans état, et le navigateur **rend** le HTML/CSS/JS. Côté sécurité : HTTP est en clair, le DNS peut fuiter même en HTTPS, Basic Auth n'est que du Base64, un cookie de session volé = usurpation, et une API sans contrôle d'accès = faille critique.

> **Distinction HTTP / HTTPS** : en HTTP, après la résolution DNS et le handshake TCP sur le port 80, le navigateur envoie directement une requête HTTP en clair. En HTTPS, après DNS et TCP sur le port 443, le navigateur réalise d'abord un **handshake TLS** : il vérifie le certificat du serveur, établit un secret partagé, puis envoie la requête HTTP dans un **tunnel chiffré**. HTTPS n'est donc **pas un autre protocole applicatif** : c'est HTTP protégé par TLS.

---
