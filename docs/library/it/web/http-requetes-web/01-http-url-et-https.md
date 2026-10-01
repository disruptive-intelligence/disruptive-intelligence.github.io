---
title: HTTP, URL et HTTPS
source: IT/05 Web & applications/HTTP & requêtes web.md
note: HTTP & requêtes web
up:
- - HTTP & requêtes web
  - index.md
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
