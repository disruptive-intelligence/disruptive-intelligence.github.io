---
title: Partie 1 — Vue d'ensemble et URL
source: IT/Culture/Fiche_How-The-Web-Works.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
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
