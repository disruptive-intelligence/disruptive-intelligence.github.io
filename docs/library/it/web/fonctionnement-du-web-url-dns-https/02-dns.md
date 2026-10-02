---
title: DNS
source: IT/05 Web & applications/Le web/Fonctionnement du web - URL, DNS, HTTPS.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
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
