---
title: Back-end, bases de données et API
source: IT/05 Web & applications/Applications web/Applications web.md
note: Applications web
up:
- - Applications web
  - index.md
---

## 19. Back-end servers

### À retenir
Le **back-end server** est le matériel + l'OS qui héberge tous les composants exécutant l'application. Il appartient à la couche d'accès aux données.

### Comment ça fonctionne
Il porte trois composants principaux : **web server**, **base de données**, **framework de développement**. S'y ajoutent souvent **WAF**, **hyperviseurs** et **conteneurs** (Docker), permettant d'isoler chaque partie. L'hébergement peut être physique, virtuel ou cloud.

Stacks courantes :

| Stack | Composants |
|---|---|
| **LAMP** | Linux, Apache, MySQL, PHP |
| **WAMP** | Windows, Apache, MySQL, PHP |
| **WINS** | Windows, IIS, .NET, SQL Server |
| **XAMPP** | Cross-platform, Apache, MySQL, PHP/Perl |

### Pourquoi c'est important en cyber
Compromettre le back-end server, c'est obtenir un **accès système** : pivot vers le réseau interne, accès aux données, aux secrets et aux services internes. C'est l'objectif final de nombreuses chaînes d'attaque web.

### Point clé à mémoriser
Le back-end server est le trophée : qui le contrôle contrôle tout ce qu'il héberge.

---

## 20. Web servers : Apache, NGINX, IIS

### À retenir
Un **web server** reçoit les requêtes HTTP/HTTPS, les **route** vers les bonnes pages/applications et renvoie les réponses. Il écoute typiquement sur les ports **80** (HTTP) et **443** (HTTPS).

### Comment ça fonctionne
Il répond avec des **codes HTTP** signalant le résultat :

| Code | Sens |
|---|---|
| 200 OK | Succès |
| 301 / 302 | Redirection (permanente / temporaire) |
| 400 | Requête mal formée |
| 401 | Non authentifié |
| 403 | Accès interdit |
| 404 | Ressource introuvable |
| 405 | Méthode non autorisée |
| 500 | Erreur serveur interne |
| 502 / 504 | Erreur / timeout de passerelle |

Principaux serveurs :

- **Apache** : le plus répandu, modulaire, souvent avec PHP (LAMP). Open source, bien documenté.
- **NGINX** : architecture asynchrone, excellent en haute concurrence ; très présent sur les sites à fort trafic.
- **IIS** : Microsoft, sur Windows Server, optimisé pour .NET et l'intégration **Active Directory** (Windows Auth).
- Autres : **Tomcat** (Java), **Node.js** (JS back-end).

### Pourquoi c'est important en cyber
Le web server est **exposé en TCP** : c'est l'un des points les plus directement attaquables (vulnérabilités publiques type Shellshock). Identifier le serveur et sa version oriente la recherche d'exploits. IIS + Windows Auth signale souvent un environnement AD.

### Commandes utiles

```bash
curl -I https://cible.example     # afficher seulement les en-têtes (serveur, codes)
curl -v https://cible.example     # détail complet de la requête/réponse
```


### Point clé à mémoriser
Le web server est la porte d'entrée HTTP exposée : l'identifier, c'est connaître la première cible et son écosystème.

---

## 21. Databases : SQL et NoSQL

### À retenir
Les bases de données **stockent et restituent** les données de l'application (contenu, comptes, fichiers). Deux grandes familles : **relationnelles (SQL)** et **non relationnelles (NoSQL)**.

### Comment ça fonctionne
**SQL (relationnel)** : données en **tables / lignes / colonnes**, reliées par des **clés** ; l'ensemble des relations forme le **schéma**. Exemples : **MySQL, MSSQL, PostgreSQL, Oracle**.

> Une clé (`id` de `users`) reliée à `user_id` de `posts` évite de dupliquer les données et permet de tout retrouver d'une requête.

**NoSQL (non relationnel)** : pas de schéma fixe, très flexible et scalable. Quatre modèles : **clé-valeur, document, wide-column, graph**. Exemples : **MongoDB** (document, JSON), **Elasticsearch** (recherche), **Cassandra** (wide-column), **Redis**, **Neo4j** (graph).

### Pourquoi c'est important en cyber
C'est là que réside la **valeur** (identifiants, données personnelles). Risques : **SQL injection**, **NoSQL injection**, fuite de données, requêtes mal construites. Bonne pratique : **droits minimaux** pour le compte applicatif (n'accéder qu'aux données nécessaires).

### Exemple concret
Concaténer une entrée utilisateur dans une requête :

```php
$query = "select * from users where name like '%$searchInput%'";
```

Sans filtrage, `$searchInput` peut injecter une requête SQL arbitraire.

### Point clé à mémoriser
La base contient la valeur ; toute requête construite à partir d'entrée utilisateur non filtrée est un risque d'injection.

---

## 22. Frameworks de développement

### À retenir
Un **framework** fournit une base structurée (routes, contrôleurs, intégration DB) pour développer rapidement la logique applicative sans tout réécrire.

### Comment ça fonctionne
Le framework gère le routage des requêtes, organise le code (logique métier / contrôleurs / accès données) et propose parfois des protections intégrées (anti-CSRF, échappement automatique des templates).

| Framework | Langage | Utilisé par |
|---|---|---|
| **Laravel** | PHP | Startups, PME |
| **Express** | Node.js | PayPal, Uber, IBM |
| **Django** | Python | Google, Instagram, Mozilla |
| **Rails** | Ruby | GitHub, Twitch, Airbnb |
| **ASP.NET** | C# | Environnements Microsoft |
| **Spring** | Java | Applications d'entreprise |

### Pourquoi c'est important en cyber
Risques : **version vulnérable** du framework, **mauvaise configuration**, dépendances/plugins faillibles, **réglages par défaut** dangereux. Les protections intégrées n'aident que si elles sont activées et bien utilisées.

### Point clé à mémoriser
Le framework accélère le développement **et** hérite ses propres CVE : identifier le framework et sa version est un réflexe d'audit.

---

## 23. APIs web

### À retenir
Une **API** est une interface permettant à des composants (front/back, ou applications tierces) d'échanger des données et de déclencher des fonctions back-end.

### Comment ça fonctionne
Le front-end appelle l'API avec une entrée ; le back-end traite et renvoie une réponse (souvent **JSON**) que le front-end affiche.

**Paramètres de requête** :

- **GET** : paramètres dans l'URL — `/search.php?item=apples`.
- **POST** : paramètres dans le corps de la requête.

**Standards** :

- **SOAP** : échange en **XML**, adapté aux données structurées/stateful, mais verbeux.
- **REST** : données via le **chemin d'URL** (`/users/1`), réponses généralement en **JSON** ; modulaire et scalable.

Méthodes REST :

| Méthode | Action |
|---|---|
| GET | Lire |
| POST | Créer |
| PUT | Remplacer (idempotent) |
| PATCH | Modifier partiellement |
| DELETE | Supprimer |

### Pourquoi c'est important en cyber
Surfaces classiques : **IDOR / BOLA** (changer un id dans l'URL pour accéder aux données d'autrui), **manque d'authentification** sur un endpoint, **sur-exposition de données** dans les réponses JSON, **endpoints cachés** trouvés dans le JS, **méthodes dangereuses** (PUT/DELETE laissées ouvertes).

### Exemple concret
`GET /user/701` qui renvoie le profil 701 : tester `GET /user/702` révèle un IDOR si l'accès n'est pas contrôlé côté serveur.

### Commandes utiles

```bash
curl -X OPTIONS -i https://cible/api/   # méthodes autorisées
curl -s https://cible/api/users | jq    # réponse JSON lisible
```


### Point clé à mémoriser
Une API expose la logique back-end : tester l'auth, les id (IDOR) et les méthodes est central.

---
