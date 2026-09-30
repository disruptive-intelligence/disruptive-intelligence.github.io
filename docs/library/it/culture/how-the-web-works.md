---
title: How the Web Works
source: IT/Culture/Fiche_How-The-Web-Works.md
---

> Cours intermédiaire orienté cybersécurité (Hack The Box, eJPT, pentest débutant, analyse web).
> Objectif : comprendre **réellement** ce qui se passe quand on tape une URL, pas seulement mémoriser des commandes cURL.

---

## 1. Vue d'ensemble : que se passe-t-il quand on visite un site web ?

### À retenir
Visiter un site déclenche une **chaîne de couches** : on part d'un nom lisible (`example.com`) et on finit avec une page affichée. Chaque maillon peut être observé, mesuré ou attaqué.

### Comment ça fonctionne
1. L'utilisateur tape une **URL**.
2. Le navigateur **analyse l'URL** (scheme, host, port, path…).
3. Le système **résout le nom de domaine** via DNS.
4. Le client obtient une **adresse IP**.
5. Sur le réseau local, il trouve la **gateway** (ARP) pour sortir.
6. Il établit une **connexion TCP** (handshake 3 étapes).
7. Si **HTTPS** : négociation **TLS** (handshake + certificat).
8. Le navigateur envoie une **requête HTTP**.
9. Le serveur renvoie une **réponse HTTP**.
10. Le navigateur **interprète** HTML, CSS, JavaScript, images.
11. Les **cookies/session** maintiennent l'état utilisateur.

### Pourquoi c'est important en cyber
Chaque étape est un point d'observation ou d'attaque : DNS (spoofing), TCP (scan), TLS (MiTM, downgrade), HTTP (injection, vol de session). Comprendre la chaîne permet de savoir **où** se place une attaque ou une défense.

### Synthèse visuelle
```
URL → DNS → IP → ARP/gateway → TCP → TLS (si HTTPS) → HTTP request → HTTP response → cookies/session → rendu navigateur
```

### Point clé à mémoriser
Une page web n'est jamais "directe" : c'est une pile de protocoles empilés, du nom de domaine jusqu'au pixel affiché.

---

## 2. URL : structure complète

### À retenir
Une URL est l'**instruction d'accès** à une ressource. Seuls le **scheme** et le **host** sont obligatoires.

### Comment ça fonctionne
```
http://admin:password@inlanefreight.com:80/dashboard.php?login=true#status
└─┬─┘ └──────┬───────┘ └────────┬────────┘└┬┘└─────┬──────┘└────┬─────┘└──┬──┘
scheme   user info           host        port   path       query string  fragment
```

| Composant | Exemple | Rôle |
|---|---|---|
| **Scheme** | `http://` / `https://` | Protocole utilisé |
| **User Info** | `admin:password@` | Identifiants (optionnel) |
| **Host** | `inlanefreight.com` | **Cible** : nom de domaine ou IP |
| **Port** | `:80` | Port (80 HTTP / 443 HTTPS par défaut) |
| **Path** | `/dashboard.php` | **Ressource** demandée |
| **Query String** | `?login=true` | **Paramètres** `clé=valeur`, séparés par `&` |
| **Fragment** | `#status` | Section interne, **traitée côté client** |

- Le **host** sert à trouver la cible.
- Le **path** demande une ressource précise.
- La **query string** transmet des paramètres au serveur.
- Le **fragment** `#section` est géré par le navigateur et **n'est généralement pas envoyé au serveur**.

### Pourquoi c'est important en cyber
La query string est manipulable et **loggée partout** (proxys, historiques, logs serveur) → ne jamais y mettre de secret. Le user info dans l'URL (`user:pass@`) peut fuiter dans les logs.

### Point clé à mémoriser
Scheme + host = obligatoires. Le fragment reste côté client ; la query string part au serveur.

---

## 3. DNS : le répertoire d'Internet

### À retenir
Le DNS traduit un **nom lisible** (`google.com`) en **adresse IP** routable. C'est l'annuaire d'Internet : sans lui, il faudrait mémoriser des IP.

### Comment ça fonctionne
Le DNS opère sur la **couche 7 (Application)**, sur le **port 53 (UDP et TCP)**. **UDP** est utilisé pour la majorité des requêtes DNS classiques. **TCP** est utilisé pour les réponses volumineuses, certains cas de fallback, **DNSSEC** et les **transferts de zone**.

Vocabulaire :
- **Nom de domaine** : `tryhackme.com`
- **Sous-domaine / hostname** : `admin.tryhackme.com`
- **Adresse IP** : la destination réelle (`104.26.10.229`)

### Pourquoi c'est important en cyber
Le DNS est souvent la **première fuite d'information** : même en HTTPS, une requête DNS en clair révèle les sites visités. C'est aussi une surface d'attaque (spoofing, cache poisoning — voir §7).

### Exemple concret
Taper `google.com` ne sert à rien tant qu'on n'a pas son IP. Le navigateur ne sait pas joindre un nom : il joint une IP.

### Point clé à mémoriser
DNS = nom → IP, couche application, port 53 UDP/TCP. Pas d'IP = pas de communication.

---

## 4. Résolution DNS : le chemin complet

### À retenir
La résolution suit un ordre précis, du **plus local au plus global**, en s'arrêtant dès qu'une réponse est trouvée.

### Comment ça fonctionne
Le client vérifie d'abord ses **mécanismes locaux de résolution** : cache navigateur, cache OS et fichier hosts, **selon la configuration du système** (l'ordre exact peut varier selon l'OS, le navigateur et la config).

```
cache local / hosts → resolver (FAI/public) → cache resolver → root (.) → TLD (.com) → authoritative → réponse IP
```

1. **Mécanismes locaux** (cache navigateur, cache OS, fichier hosts) : si l'IP y est, c'est fini.
2. **Fichier hosts** (`/etc/hosts` sous Linux) : entrée statique `IP   domaine`, prioritaire quand elle existe.
3. **Resolver récursif** : serveur DNS configuré (FAI ou public comme `8.8.8.8`, `1.1.1.1`). S'il a la réponse en cache, il la renvoie.
4. **Serveurs racines (.)** : indiquent quel serveur TLD gère l'extension (`.com`).
5. **Serveurs TLD (.com)** : indiquent le serveur **autoritaire** du domaine.
6. **Serveur autoritaire** : détient les enregistrements DNS réels et renvoie l'IP.
7. L'IP remonte la chaîne, est **mise en cache** (avec son **TTL**), puis transmise au client.

Le **TTL** (en secondes) définit combien de temps l'enregistrement reste en cache avant d'être re-demandé.

### Pourquoi c'est important en cyber
- `/etc/hosts` permet de **forcer une résolution locale** (viser un lab HTB, bypasser un DNS).
- **Correction importante** : `8.8.8.8` et `1.1.1.1` sont des **résolveurs publics**, pas automatiquement du DNS chiffré. Le chiffrement dépend de **DoH** (DNS over HTTPS) ou **DoT** (DNS over TLS), qui doivent être activés explicitement.

### Commandes utiles
```bash
nslookup google.com          # résolution simple
dig google.com               # détaillée (records, TTL)
cat /etc/hosts               # entrées statiques locales
```

### Point clé à mémoriser
cache → hosts → resolver → root → TLD → authoritative → IP. DNS public ≠ DNS chiffré.

---

## 5. Hiérarchie DNS

### À retenir
Le DNS est un **arbre**, de la racine vers les feuilles.

### Comment ça fonctionne
| Couche | Description |
|---|---|
| **Root servers (.)** | Sommet de la hiérarchie. Gérés sous l'égide de l'ICANN. **13 ensembles logiques** (a→m), mais **distribués mondialement via anycast** : une même IP est routée vers le serveur physique le plus proche. |
| **TLD** | `.com`, `.org`, `.net`, codes pays `.fr`, `.uk` |
| **Second-level domain** | `tryhackme` dans `tryhackme.com` |
| **Sous-domaine / hostname** | `admin.tryhackme.com` — découpe en zones plus spécifiques |
| **Serveur autoritaire** | Détient la vérité (les records) pour un domaine donné |

### Pourquoi c'est important en cyber
Comprendre la hiérarchie aide à l'**énumération de sous-domaines** (surface d'attaque) et à comprendre où une zone est réellement gérée (qui contrôle quoi).

### Point clé à mémoriser
13 ensembles racines logiques, démultipliés par anycast. La hiérarchie : root → TLD → domaine → sous-domaine.

---

## 6. Types d'enregistrements DNS

### À retenir
Un domaine porte plusieurs **records**, chacun avec un rôle précis.

### Comment ça fonctionne
| Record | Rôle | Intérêt cyber |
|---|---|---|
| **A** | Nom → **IPv4** | Cible principale d'un host |
| **AAAA** | Nom → **IPv6** | Souvent oublié dans les scans → angle mort |
| **CNAME** | Alias vers un autre nom (`store.tryhackme.com` → `shop.shopify.com`) | Révèle l'infra/les services tiers utilisés |
| **MX** | Serveurs **mail** du domaine (`alt1.aspmx.l.google.com`) | Identifier le fournisseur mail, cibler le phishing |
| **TXT** | Texte libre : **SPF / DKIM / validations** | Révèle la posture anti-spoofing mail |
| **NS** | Serveurs de **noms autoritaires** du domaine | Identifier qui héberge la zone DNS |

### Pourquoi c'est important en cyber
L'énumération DNS (records A/AAAA/CNAME/MX/TXT/NS) est une étape clé de la **reconnaissance** : elle cartographie l'infrastructure sans toucher la cible directement.

### Commandes utiles
```bash
dig tryhackme.com MX
dig tryhackme.com TXT
dig tryhackme.com NS
```

### Point clé à mémoriser
A/AAAA = IP, CNAME = alias, MX = mail, TXT = SPF/DKIM, NS = serveurs autoritaires.

---

## 7. DNS et sécurité

### À retenir
Le DNS, par défaut **en clair**, est une cible et une fuite.

### Comment ça fonctionne
- **DNS spoofing** : sur un réseau local, un attaquant répond **avant** le vrai serveur DNS, en se faisant passer pour la cible (« l'IP de la banque, c'est ma machine »).
- **Cache poisoning** : empoisonner le cache d'un resolver pour rediriger durablement des victimes.
- **Typosquatting** : enregistrer `gooogle.com` pour piéger les fautes de frappe.
- **Énumération de sous-domaines** : découvrir `admin.`, `dev.`, `vpn.`… → surface d'attaque.
- **Fuite d'information** : le DNS en clair révèle les domaines visités même en HTTPS.

### Pourquoi c'est important en cyber
Le DNS est un point faible classique en MiTM et en reconnaissance. La parade : **DoH/DoT** chiffrent la requête DNS.

À noter : même avec HTTPS + DNS chiffré, le domaine peut encore fuiter via le **SNI** du handshake TLS (voir §18).

### Point clé à mémoriser
DNS en clair = fuite + spoofing. DoH/DoT chiffrent, mais HTTPS seul ne masque pas toujours le domaine.

---

## 8. Avant HTTP : réseau, IP, ARP, gateway et encapsulation

### À retenir
HTTP ne flotte pas dans le vide : il repose sur **plusieurs couches réseau** en dessous.

### Comment ça fonctionne
1. Le navigateur **génère** la requête HTTP.
2. Elle est **encapsulée** dans TCP (port 80 ou 443), lui-même dans un paquet IP portant l'**IP destination**.
3. Sur le **réseau local**, la machine utilise **ARP** pour trouver l'**adresse MAC de la gateway** (le routeur).
4. La trame part vers le routeur, qui **transfère** le paquet selon l'IP destination.
5. Les routeurs intermédiaires **font suivre** de proche en proche.
6. Le serveur reçoit le paquet et l'oriente vers le **port applicatif** (80/443).
7. La réponse revient vers le **port source temporaire** du client (choisi aléatoirement par l'OS).

### Pourquoi c'est important en cyber
ARP est lui-même attaquable (**ARP spoofing** → MiTM local). Comprendre l'encapsulation explique pourquoi une capture réseau voit des couches empilées (Ethernet → IP → TCP → HTTP).

### Point clé à mémoriser
HTTP s'appuie sur IP + ARP + routage. Le client écoute sur un port temporaire ; le serveur, sur 80/443.

---

## 9. TCP : établir la connexion

### À retenir
HTTP et HTTPS utilisent classiquement **TCP**, qui garantit une connexion fiable avant tout échange applicatif.

### Comment ça fonctionne
- **HTTP = port 80**, **HTTPS = port 443**.
- Le client utilise un **port source temporaire** (éphémère).
- **Handshake TCP en 3 étapes** :

```
Client  ──── SYN ───▶  Serveur
Client  ◀── SYN-ACK ─  Serveur
Client  ──── ACK ───▶  Serveur
```

Après ce handshake, les **données applicatives** (HTTP, ou TLS si HTTPS) peuvent circuler.

### Pourquoi c'est important en cyber
Le handshake TCP est la base du **scan de ports** (un SYN-ACK = port ouvert). Comprendre l'état de connexion aide à lire Wireshark et à interpréter les scans Nmap.

### Point clé à mémoriser
SYN → SYN-ACK → ACK, puis les données circulent. Port 80 HTTP, 443 HTTPS, port source client temporaire.

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

## 14. HTTPS : HTTP dans TLS

### À retenir
HTTPS = HTTP **encapsulé dans TLS**. Port **443**. Le contenu HTTP devient **illisible** sur le réseau.

### Comment ça fonctionne
Avant tout échange HTTP, un **handshake TLS** établit un tunnel chiffré (voir §16). Ensuite, les requêtes/réponses HTTP circulent **à l'intérieur** de ce tunnel. Dans Wireshark, on ne voit plus du HTTP mais du **« TLS Application Data »** (illisible sans la clé).

### Pourquoi c'est important en cyber
HTTPS apporte trois garanties : **confidentialité** (chiffré), **intégrité** (non altéré), **authentification du serveur** (certificat). Un site HTTP qui force HTTPS renvoie souvent une **redirection 301** vers le port 443, suivie du handshake.

### Commandes utiles
```bash
curl -k https://site.local   # désactive la validation du certificat TLS — LAB UNIQUEMENT
```
> `-k` désactive la **validation du certificat TLS** (la connexion reste chiffrée). À utiliser uniquement en lab ou environnement maîtrisé, **jamais en production**.

### Point clé à mémoriser
HTTPS = HTTP dans TLS, port 443. Sur le réseau, on ne voit que du « Application Data » chiffré.

---

## 15. TLS : certificats et chaîne de confiance

### À retenir
Un **certificat TLS** prouve que la **clé publique** appartient bien au domaine demandé.

### Comment ça fonctionne
- Le serveur possède une **clé privée** (secrète) et une **clé publique** (distribuée dans le certificat).
- Le certificat est au format **X.509**.
- Émission : l'admin génère une **CSR** (Certificate Signing Request) → la soumet à une **Autorité de Certification (CA)** → la CA vérifie et **signe** le certificat.
- Le navigateur fait confiance à un certificat si sa CA fait partie des **autorités de confiance** installées (chaîne de confiance).
- Un **certificat autosigné** chiffre, mais **ne prouve pas l'authenticité** (aucun tiers ne le valide) → le navigateur affiche une alerte.

### Pourquoi c'est important en cyber
La chaîne de confiance est ce qui empêche un attaquant de se faire passer pour la banque. Un certificat invalide = **problème d'authenticité**, signal d'un possible MiTM. Let's Encrypt fournit des certificats signés gratuits.

### Point clé à mémoriser
Le certificat lie une clé publique à un domaine, validé par une CA de confiance. Autosigné = chiffré mais non authentifié.

---

## 16. TLS handshake : le process simplifié

### À retenir
Le handshake établit la confiance et un **secret partagé**, puis bascule en chiffrement rapide.

### Comment ça fonctionne
1. **ClientHello** : le client annonce les versions TLS (1.2/1.3) et suites cryptographiques supportées.
2. **ServerHello** : le serveur choisit les paramètres.
3. Le serveur envoie son **certificat** (X.509).
4. Le client **vérifie** : domaine, date de validité, signature, CA de confiance.
5. **Échange de clés** : le client et le serveur établissent un **secret partagé** via un **échange de clés éphémère** (Diffie-Hellman / **ECDHE**), **sans transmettre directement** la clé de session sur le réseau. La clé publique du certificat sert surtout à **authentifier le serveur**.
6. Dérivation d'une **clé de session** symétrique commune à partir de ce secret.
7. **Passage au chiffrement symétrique** (rapide).
8. Les requêtes HTTP circulent ensuite **dans le tunnel TLS**.

### Métaphore
L'**asymétrique** (lent) sert à **établir la confiance et à négocier le secret** ; le **symétrique** (rapide) chiffre ensuite toute la conversation. *Cette métaphore aide à comprendre l'idée générale, même si TLS moderne (notamment **TLS 1.3**) utilise des mécanismes d'échange de clés éphémères plus avancés que le simple « chiffrer une clé avec la clé publique ».*

### Pourquoi c'est important en cyber
Comprendre le handshake explique les attaques de **downgrade** (forcer une version faible) et l'intérêt de TLS 1.3. La vérification du certificat est l'étape qu'un MiTM cherche à contourner.

### Point clé à mémoriser
ClientHello → ServerHello → certificat → vérification → échange de clés → clé de session → symétrique.

---

## 16 bis. Déroulé complet d'une requête HTTPS

### Comment ça fonctionne — déroulé HTTPS
1. L'utilisateur tape une URL en `https://`.
2. Le navigateur extrait le host, le path et le **port implicite 443**.
3. Le système résout le nom de domaine en adresse IP via **DNS**.
4. Le client ouvre une **connexion TCP** vers le serveur sur le **port 443**.
5. Avant d'envoyer la requête HTTP, le client démarre un **handshake TLS**.
6. Le client envoie un **`ClientHello`** (versions TLS + suites cryptographiques supportées).
7. Le serveur répond par un **`ServerHello`** et choisit les paramètres TLS.
8. Le serveur envoie son **certificat TLS**.
9. Le navigateur **vérifie le certificat** : nom de domaine, date de validité, signature, autorité de certification.
10. Le client et le serveur établissent un **secret partagé / une clé de session** via l'échange de clés.
11. Une fois le **tunnel TLS** établi, le navigateur envoie la **requête HTTP à l'intérieur du tunnel chiffré**.
12. Le serveur traite la requête et renvoie une **réponse HTTP elle aussi chiffrée** dans TLS.
13. Le navigateur **déchiffre** la réponse, interprète HTML/CSS/JS et déclenche d'autres requêtes si nécessaire.

```text
URL HTTPS → DNS → TCP:443 → TLS handshake → tunnel chiffré → HTTP request → HTTP response → navigateur
```

À retenir :
- HTTPS **ne remplace pas** HTTP : il **encapsule** HTTP dans TLS.
- Le contenu HTTP est **chiffré** : path, headers, cookies, body, réponse.
- Certaines **métadonnées peuvent encore fuiter** : DNS, IP destination, parfois **SNI** selon la configuration.
- Un **certificat invalide** = l'**authenticité du serveur n'est pas garantie**.
- `curl -k` **chiffre toujours** la connexion, mais **désactive la vérification d'identité** du serveur → MiTM possible.

---

## 17. Chiffrement asymétrique vs symétrique

### À retenir
HTTPS **combine** les deux : asymétrique pour s'installer, symétrique pour travailler.

### Comment ça fonctionne
- **Asymétrique** : une **clé publique** et une **clé privée** liées mathématiquement. Selon l'algorithme, elles peuvent servir à **chiffrer/déchiffrer**, **signer/vérifier** ou **authentifier un échange de clés**. Sûr mais **lent**.
- **Symétrique** : **une même clé** chiffre et déchiffre. **Rapide**, mais il faut d'abord partager la clé en sécurité.

Mécanisme (métaphore historique du cadenas) :
1. Le serveur prouve son identité via son **certificat** (clé publique signée par une CA).
2. Le client et le serveur **négocient un secret partagé** via un échange de clés éphémère.
3. Les deux dérivent la **même clé symétrique** → toute la suite passe en symétrique (ex. AES).

*Cette image aide à saisir l'idée, mais TLS moderne (TLS 1.3) n'envoie pas une clé enfermée dans un cadenas : il établit le secret par **Diffie-Hellman éphémère (ECDHE)**, sans jamais transmettre la clé de session.*

### Pourquoi c'est important en cyber
L'asymétrique résout le **problème d'échange de clé** sur un réseau hostile. C'est exactement ce que fait HTTPS au début de chaque session.

### Point clé à mémoriser
Asymétrique = établir la session (lent, sûr). Symétrique = échanger les données (rapide). HTTPS fait les deux.

---

## 18. HTTPS et limites de sécurité

### À retenir
HTTPS chiffre le **contenu**, pas forcément toutes les **métadonnées**.

### Comment ça fonctionne
- Le **DNS** peut rester **visible** s'il n'est pas chiffré (DoH/DoT).
- Le **SNI** (Server Name Indication) du handshake peut exposer le domaine demandé selon la version/config TLS.
- Un **certificat invalide** = problème d'**authenticité**, même si un chiffrement existe.
- `curl -k https://site.local` **ignore la validation** du certificat (la connexion reste chiffrée) → ouvre la porte au **MiTM** (à réserver aux labs).
- **HSTS** (Strict-Transport-Security) force HTTPS et limite les **downgrade attacks**.

### Pourquoi c'est important en cyber
« HTTPS = tout est caché » est une **erreur courante**. Un analyste peut déduire les sites visités via DNS/SNI même sans déchiffrer le contenu.

### Point clé à mémoriser
HTTPS protège le contenu, pas toujours le domaine (DNS/SNI). `-k` = MiTM possible. HSTS = anti-downgrade.

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

## 33. Mini-quiz (15 questions)

1. Quels sont les deux seuls composants **obligatoires** d'une URL ?
2. Le fragment `#section` est-il envoyé au serveur ?
3. Sur quel port et quels protocoles de transport fonctionne le DNS ?
4. Dans quel ordre se fait la résolution DNS (cite les 4 grandes étapes après le cache) ?
5. `8.8.8.8` fournit-il automatiquement un DNS chiffré ?
6. À quoi sert ARP avant l'envoi du paquet ?
7. Décris le handshake TCP en 3 étapes.
8. Quels ports pour HTTP et HTTPS ?
9. Quelles sont les trois garanties apportées par HTTPS ?
10. Dans le handshake TLS, l'asymétrique sert à quoi, le symétrique à quoi ?
11. Un certificat autosigné chiffre-t-il ? Prouve-t-il l'authenticité ?
12. Différence entre **401** et **403** ?
13. Où sont les paramètres en GET ? En POST ?
14. Un cookie est-il stocké côté client ou serveur ? Et la session ?
15. Pourquoi une API autorisant DELETE sans contrôle d'accès est-elle dangereuse ?

<details markdown="1">
<summary>Réponses</summary>

1. Le **scheme** et le **host**.
2. Non, il est traité **côté client**.
3. Port **53**, en **UDP et TCP**.
4. cache → hosts → resolver → **root → TLD → authoritative → réponse IP**.
5. Non : c'est un **résolveur public**, pas chiffré sans **DoH/DoT**.
6. Trouver l'**adresse MAC de la gateway** (routeur) pour sortir du réseau local.
7. **SYN** → **SYN-ACK** → **ACK**.
8. HTTP = **80**, HTTPS = **443**.
9. **Confidentialité**, **intégrité**, **authentification du serveur**.
10. Asymétrique = **établir la confiance et échanger le secret** ; symétrique = **chiffrer rapidement la session**.
11. Oui il **chiffre**, mais il **ne prouve pas** l'authenticité (pas de CA tierce).
12. **401** = authentification requise ; **403** = authentifié mais accès interdit.
13. GET = dans l'**URL** (query string) ; POST = dans le **body**.
14. Le **cookie** est côté client ; la **session** qu'il référence peut être côté serveur.
15. N'importe qui peut **supprimer des données** (DoS / perte de données critiques), surtout avec une faille **IDOR/BOLA**.

</details>
