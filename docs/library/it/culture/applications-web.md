---
title: Applications web
source: IT/Culture/Fiche_WebApp.md
---

> Fiche intermédiaire orientée cybersécurité (HTB, eJPT, pentest débutant).
> Objectif : **comprendre comment une application web est construite et où les failles apparaissent**, pas mémoriser une liste de vulnérabilités.

---

## 1. Vue d'ensemble : qu'est-ce qu'une application web ?

### À retenir
Une application web est une application **interactive** qui s'exécute dans un navigateur et repose sur un modèle **client/serveur**. Contrairement à un simple site, elle réagit aux actions de l'utilisateur et renvoie un contenu personnalisé.

### Comment ça fonctionne
On distingue deux moitiés :
- **Front-end (côté client)** : ce que le navigateur télécharge et exécute (HTML, CSS, JavaScript). C'est l'interface visible.
- **Back-end (côté serveur)** : la logique métier, les traitements et les données, exécutés sur un serveur distant.

Le dialogue entre les deux se fait via **HTTP/HTTPS**.

Déroulé typique d'une action :
```
Navigateur → requête HTTP → serveur web → logique applicative → base de données
           ← rendu navigateur ← réponse HTTP ←
```

### Pourquoi c'est important en cyber
Chaque flèche de ce schéma est un point d'interaction, donc une **surface d'attaque potentielle**. Comprendre où s'exécute le code (client vs serveur) détermine ce qu'un attaquant peut voir, modifier ou rejouer.

### Exemple concret
Gmail, Amazon, Google Docs, HTB Academy : toutes des applications web. Le navigateur affiche l'interface, mais l'envoi d'un mail ou le calcul d'un panier se fait côté serveur.

### Point clé à mémoriser
Le front-end **montre**, le back-end **décide**, la base de données **contient la valeur**.

---

## 2. Site web statique vs application web

### À retenir
Un **site statique (Web 1.0)** affiche le même contenu pour tout le monde et ne change qu'avec une modification manuelle du code. Une **application web dynamique (Web 2.0)** génère un contenu différent selon l'utilisateur et ses actions.

### Comment ça fonctionne
Le statique sert des fichiers fixes. Le dynamique exécute du code côté serveur (et parfois côté client) pour construire la page à la volée : session, panier, résultats de recherche, etc.

### Pourquoi c'est important en cyber
> Plus d'interactions = plus d'entrées utilisateur = plus de surface d'attaque.

Un site statique n'accepte presque aucune donnée utilisateur. Une application dynamique traite des formulaires, des paramètres et des fichiers — autant d'occasions d'injection ou de mauvaise validation.

### Point clé à mémoriser
La dynamique apporte la richesse fonctionnelle **et** le risque : chaque entrée utilisateur est une porte à tester.

---

## 3. Application web vs application native

### À retenir
Une application **web** tourne dans un navigateur, indépendamment de l'OS. Une application **native** est installée sur le système et exploite directement ses ressources.

### Comment ça fonctionne
| | Application web | Application native |
|---|---|---|
| Installation | Aucune | Requise par OS |
| Mise à jour | Centralisée (serveur) | Poussée à chaque client |
| Multi-plateforme | Oui (navigateur) | Build par plateforme |
| Performance / matériel | Limitée au navigateur | Accès complet, plus rapide |

Les applications **hybrides / PWA** mélangent les deux : code web tournant avec des capacités natives.

### Pourquoi c'est important en cyber
La mise à jour centralisée du web est un atout défensif : un correctif s'applique pour tous d'un coup. Mais l'exposition Internet permanente élargit la surface accessible à distance.

### Point clé à mémoriser
Web = accessible partout sans installation, donc attaquable partout.

---

## 4. Pourquoi les applications web sont critiques en sécurité

### À retenir
Les applications web sont **exposées sur Internet**, offrent une **large surface d'attaque** et sont souvent connectées à des **données sensibles**. Une seule faille peut servir de point d'entrée vers tout le système d'information.

### Comment ça fonctionne
- Accessibles depuis n'importe quel pays, par n'importe qui ayant un navigateur.
- Outillage automatisé d'attaque très répandu (scanners, exploits).
- Reliées à des bases de données et hébergées sur des serveurs portant d'autres ressources.
- Évoluent en permanence : un simple changement de code peut introduire une vulnérabilité critique.

### Pourquoi c'est important en cyber
Une faille web n'est presque jamais une fin en soi : c'est un **pivot**. Une SQLi exposant des emails → password spraying sur le VPN → foothold dans le réseau interne. C'est l'effet de **chaînage**.

### Exemple concret
Une SQLi sur un portail authentifié via Active Directory permet souvent d'extraire les emails (= identifiants AD), puis de tenter un password spray contre le webmail ou le VPN.

### Point clé à mémoriser
Une faille web compromet rarement *que* l'application : elle ouvre la route vers le reste du SI.

---

## 5. Logique générale d'un pentest web

### À retenir
Pentester une application web ne consiste pas à balancer des payloads au hasard, mais à **comprendre l'application** avant de l'attaquer.

### Comment ça fonctionne
Démarche type (inspirée de l'**OWASP Web Security Testing Guide**) :
1. Analyser le front-end (HTML, CSS, JS) à la recherche de données exposées et d'endpoints.
2. Observer le trafic HTTP entre navigateur et serveur.
3. Identifier la stack technique (serveur web, framework, versions).
4. Tester en **non authentifié**.
5. Tester en **authentifié**.
6. Comparer les **rôles** (user vs admin) pour repérer les défauts de contrôle d'accès.
7. Chercher les vulnérabilités sur chaque entrée.

### Pourquoi c'est important en cyber
La majorité des failles intéressantes (IDOR, broken access control, escalade de privilèges) ne se voient qu'en comparant les comportements selon le contexte d'authentification.

### Point clé à mémoriser
Comprendre l'application > envoyer des payloads. La compréhension dirige les payloads.

---

## 6. Architecture web : les trois couches (Three Tier)

### À retenir
Une application web s'organise en trois couches : **présentation**, **application** et **données**.

### Comment ça fonctionne
| Couche | Rôle | Technologies | Risques cyber |
|---|---|---|---|
| **Presentation Layer** | Interface utilisateur | HTML, CSS, JS | XSS, HTML injection, données exposées |
| **Application Layer** | Logique métier, droits, traitements | Framework back-end | Injections, broken access control, logique métier cassée |
| **Data Layer** | Stockage et accès aux données | SQL/NoSQL, fichiers | SQLi, NoSQLi, fuite de données, droits trop larges |

Synthèse du flux : `front-end → application layer → data layer`.

### Pourquoi c'est important en cyber
Localiser une faille dans la bonne couche oriente l'exploitation **et** la remédiation. Une faille de présentation (XSS) frappe l'utilisateur ; une faille de la couche application (injection) peut compromettre le serveur.

### Point clé à mémoriser
Trois couches = trois familles de risques. Savoir où l'on est dit quoi tester.

---

## 7. Modèles d'infrastructure web

### À retenir
La façon dont les serveurs et bases sont répartis influence directement l'**impact d'une compromission** et la **redondance**.

### Comment ça fonctionne

**Client-Server** — Un serveur héberge l'application et la distribue aux clients (navigateurs). C'est le socle de tous les autres modèles.

**One Server** — Tout (application + base) sur un seul serveur.
- *Avantage* : simple à déployer.
- *Risque* : « tous les œufs dans le même panier ». Une faille = tout compromis ; le serveur tombe = tout indisponible.

**Many Servers – One Database** — Plusieurs serveurs applicatifs, une base isolée sur son propre serveur.
- *Avantage* : **segmentation**. Un serveur web compromis n'expose pas directement la base, et inversement.
- *Risque* : la base reste un point de convergence ; il faut limiter les accès au strict nécessaire.

**Many Servers – Many Databases** — Chaque application a sa propre base (parfois sur des serveurs distincts).
- *Avantage* : meilleure segmentation + **redondance** (bascule sur backup).
- *Risque* : plus complexe (load balancers), mais l'un des meilleurs choix sécurité.

**Microservices** — Application découpée en petits services indépendants, communicant entre eux (souvent stateless).

**Serverless** — Le code tourne dans des conteneurs gérés par un cloud (AWS, GCP, Azure) ; aucune gestion de serveur côté développeur.

### Pourquoi c'est important en cyber
La segmentation **limite la propagation** d'une compromission. Après avoir pris le contrôle d'un serveur, ne pas trouver la base indique souvent qu'elle est isolée ailleurs — information précieuse pour le pivot.

### Point clé à mémoriser
Plus l'architecture est segmentée, plus une faille est **contenue**. Le « one server » amplifie l'impact ; le « many/many » l'amortit.

---

## 8. Composants d'une application web

### À retenir
Au-delà des modèles, toute application se décompose en composants identifiables, chacun avec son rôle et son risque.

### Comment ça fonctionne
| Composant | Rôle | Risque cyber |
|---|---|---|
| **Client** | Navigateur, exécute le front-end | Tout y est visible et modifiable |
| **Server** | Matériel + OS hôte | Compromission = accès système, pivot |
| **Web server** | Reçoit/route les requêtes HTTP | Exposé en TCP, vulnérabilités publiques |
| **Application logic** | Cœur fonctionnel | Injections, logique métier cassée |
| **Database** | Stockage des données | SQLi/NoSQLi, fuite de données |
| **Microservices** | Fonctions isolées | Communication inter-services à sécuriser |
| **3rd-party integrations** | Services externes | Confiance excessive, dépendances vulnérables |
| **Serverless functions** | Fonctions cloud à la demande | Mauvaise config des permissions cloud |

### Pourquoi c'est important en cyber
Cartographier ces composants, c'est dresser la **carte des cibles**. Chaque composant a sa propre catégorie de failles.

### Point clé à mémoriser
Connaître les composants = savoir quoi énumérer et quoi attaquer.

---

## 9. Front-end vs back-end

### À retenir
Le **front-end** est tout ce que le navigateur reçoit et exécute. Le **back-end** est la logique et les données côté serveur. Le **full stack** désigne la maîtrise des deux.

### Comment ça fonctionne
Le front-end est livré au client : HTML, CSS, JS sont **téléchargés** et tournent dans le navigateur. Le back-end (code source, framework, base) reste sur le serveur et n'est pas accessible par défaut.

### Pourquoi c'est important en cyber
> Tout ce qui est côté client est **visible, modifiable et rejouable**.

Conséquence directe : la sécurité critique (authentification, autorisation, validation des données) **doit** être imposée côté serveur. Un contrôle uniquement front-end se contourne en désactivant le JS ou en envoyant la requête à la main (curl, Burp).

### Exemple concret
Un bouton « Admin » caché en CSS reste accessible : l'endpoint existe côté serveur. Cacher ≠ protéger.

### Point clé à mémoriser
Côté client = suggestion. Côté serveur = décision. Ne jamais faire confiance au front-end.

---

## 10. Front-end : HTML, CSS, JavaScript

### À retenir
Le front-end repose sur le **trio** : HTML (structure), CSS (style), JavaScript (comportement), interprétés par le navigateur.

### Comment ça fonctionne
- **HTML** : squelette de la page (titres, formulaires, images).
- **CSS** : apparence (couleurs, mise en page, animations).
- **JavaScript** : interactivité (réactions, requêtes, mise à jour dynamique).

Frameworks JS courants : **Angular, React, Vue, jQuery** — ils accélèrent le développement d'interfaces dynamiques.

### Pourquoi c'est important en cyber
Le code front-end est **lisible par tous**. On y cherche : endpoints/API cachés, commentaires révélateurs, credentials de test, clés exposées, et on y identifie les vecteurs **XSS / DOM**.

### Point clé à mémoriser
Le front-end est un livre ouvert : la première lecture d'une cible commence là.

---

## 11. HTML, DOM et URL encoding

### À retenir
Le HTML structure la page sous forme d'**arbre** d'éléments. Le **DOM** est la représentation programmable de cet arbre, manipulable par JavaScript. L'**URL encoding** permet de transporter des caractères spéciaux dans une URL.

### Comment ça fonctionne
- Chaque élément est une balise ouvrante/fermante (`<p>...</p>`), pouvant porter un `id` ou une `class` (utilisés par CSS et JS pour cibler l'élément).
- Le **DOM** (Document Object Model) expose la page comme des objets : `document.head`, `document.getElementById(...)`. JavaScript lit et modifie ces objets en temps réel.
- L'**URL encoding** (percent-encoding) remplace les caractères hors ASCII par `%` suivi de deux chiffres hexadécimaux.

| Caractère | Encodage |
|---|---|
| espace | `%20` |
| `"` | `%22` |
| `#` | `%23` |
| `&` | `%26` |
| `'` | `%27` |

### Pourquoi c'est important en cyber
Comprendre le DOM est indispensable pour le **DOM XSS** et l'**HTML injection** : on manipule ou crée des éléments. Maîtriser l'URL encoding permet de lire et construire des **payloads encodés** qui passent les filtres ou traversent une URL.

### Exemple concret
Une apostrophe `'` encodée en `%27` reste interprétée comme une apostrophe par le serveur — utile pour tester une injection à travers un paramètre d'URL.

### Point clé à mémoriser
Le DOM est la cible du JS (et des attaques client) ; l'encodage est la grammaire des payloads dans les URL.

---

## 12. CSS

### À retenir
Le CSS contrôle **l'apparence**, pas la sécurité. Il définit le style des éléments via des sélecteurs (`body`, `h1`, classes, id).

### Comment ça fonctionne
Syntaxe : `sélecteur { propriété : valeur; }`. Des frameworks (**Bootstrap, SASS, Foundation, Bulma, Pure**) fournissent des styles prêts à l'emploi.

### Pourquoi c'est important en cyber
Le CSS peut **masquer** des éléments (`display:none`), mais ces éléments existent toujours dans le DOM et leurs endpoints restent appelables. Une interface peut aussi être détournée visuellement (faux formulaire superposé).

### Point clé à mémoriser
Cacher un élément en CSS n'est **jamais** une mesure de sécurité.

---

## 13. JavaScript

### À retenir
JavaScript pilote le **comportement** côté navigateur. Il existe aussi côté back-end via **Node.js**.

### Comment ça fonctionne
- Inline : `<script> ... </script>`.
- Externe : `<script src="./script.js"></script>`.
- Manipule le DOM, met à jour la page en temps réel.
- Effectue des requêtes vers le back-end via **AJAX / fetch**.
- S'appuie sur des frameworks (Angular, React, Vue, jQuery).

### Pourquoi c'est important en cyber
Les fichiers JS révèlent souvent les **endpoints/API** de l'application. La logique côté client est **modifiable**. C'est aussi le terrain du **XSS / DOM XSS**, et on y trouve parfois des **secrets exposés** (clés, tokens).

### Exemple concret
`grep`er les fichiers `.js` d'une cible pour extraire les chemins d'API (`/api/v1/users`, `/admin/...`) révèle des fonctionnalités non visibles dans l'interface.

### Point clé à mémoriser
Le JS est une mine d'endpoints et un terrain d'exécution côté victime. À lire systématiquement.

---

## 14. Exposition de données sensibles côté front-end

### À retenir
Le **Sensitive Data Exposure** désigne des données sensibles laissées en clair dans le code visible côté client.

### Comment ça fonctionne
Outils d'inspection : **View Source** (Ctrl+U), **DevTools** (onglets Network, Sources, Storage/Cookies), proxy **Burp Suite**.
On y trouve : commentaires HTML oubliés, scripts JS, endpoints cachés, **credentials de test**, **clés API**, liens internes.

### Pourquoi c'est important en cyber
C'est le premier réflexe d'audit : chercher les **« low-hanging fruits »**. Un commentaire oublié contenant des identifiants peut suffire à entrer.

### Exemple concret
```html
<!-- TODO: remove test credentials test:test -->
```
Un commentaire de développeur non supprimé pouvant exposer des identifiants encore valides.

### Prévention
Ne **jamais** mettre de secret côté client ; relire le code visible ; supprimer commentaires et liens inutiles ; minifier/obfusquer le JS pour limiter l'exposition.

### Point clé à mémoriser
Tout ce qui est dans le code client est public. Lire le source avant tout le reste.

---

## 15. HTML Injection

### À retenir
L'**HTML injection** survient quand une entrée utilisateur non filtrée est affichée comme du **HTML** plutôt que comme du texte.

### Comment ça fonctionne
Si l'application insère l'entrée directement dans la page (par ex. via `innerHTML`) sans nettoyage, le navigateur **interprète** le HTML soumis au lieu de l'afficher littéralement. La donnée peut venir directement du front-end ou être récupérée depuis la base (commentaire stocké).

### Pourquoi c'est important en cyber
Impacts : **défacement** de page, insertion de **faux formulaire** de connexion (phishing), modification visuelle trompeuse. C'est souvent la porte d'entrée vers le **XSS**.

### Exemple concret
Un champ « nom » réaffiché tel quel : soumettre une balise `<style>` modifiant l'arrière-plan suffit à prouver que l'entrée est interprétée comme HTML.

### Prévention
Validation, sanitization, **output encoding** (afficher comme texte), éviter `innerHTML` avec une entrée utilisateur.

### Point clé à mémoriser
Si une entrée s'affiche comme du code et non comme du texte, le contrôle d'affichage est cassé.

---

## 16. Cross-Site Scripting (XSS)

### À retenir
Le **XSS** injecte du **JavaScript** exécuté dans le navigateur de la victime. C'est une HTML injection poussée à l'exécution de code client.

### Comment ça fonctionne
| Type | Déclenchement |
|---|---|
| **Reflected** | L'entrée est renvoyée immédiatement (résultat de recherche, message d'erreur) |
| **Stored** | L'entrée est stockée en base puis réaffichée (post, commentaire) — touche plusieurs victimes |
| **DOM** | L'entrée est écrite directement dans un objet du DOM par du JS côté client |

### Pourquoi c'est important en cyber
Impacts : **vol de session** (cookies), actions effectuées au nom de la victime, et — si la victime est admin — compromission de comptes à privilèges pouvant mener au serveur.

### Exemple concret
Un payload affichant `document.cookie` dans une alerte prouve qu'on peut lire le cookie de session de la victime — première étape vers son vol.

### Prévention
**Output encoding**, sanitization, **CSP** (Content Security Policy), cookies **HttpOnly**, éviter les *DOM sinks* dangereux, validation côté serveur. Les navigateurs modernes bloquent une partie des exécutions automatiques, mais ce n'est pas suffisant.

### Point clé à mémoriser
HTML injection = injecter du HTML. XSS = injecter du JS exécuté chez la victime.

---

## 17. Cross-Site Request Forgery (CSRF)

### À retenir
Le **CSRF** abuse de la **session active** d'une victime pour exécuter une action **non voulue** en son nom.

### Comment ça fonctionne
Le navigateur joint **automatiquement** les cookies d'authentification à chaque requête vers le site. Si un attaquant force la victime authentifiée à envoyer une requête (via un lien, une image, ou un XSS), l'action s'exécute avec les droits de la victime.

### Pourquoi c'est important en cyber
Permet de modifier un mot de passe, d'effectuer une action sensible, ou — en visant un admin — d'obtenir des accès privilégiés. Le CSRF s'appuie souvent sur un XSS pour porter le payload.

### Exemple concret
Un commentaire piégé charge un script qui rejoue la procédure de changement de mot de passe de l'application. La victime, connectée, change son mot de passe à son insu vers une valeur connue de l'attaquant.

### Prévention
**Token anti-CSRF** unique par session/requête, attribut cookie **SameSite** (Strict/Lax), vérification **Origin/Referer**, et confirmation (ou ressaisie du mot de passe) pour les actions sensibles. Ces défenses sont des **couches**, pas des garanties absolues.

### Point clé à mémoriser
CSRF = faire agir le navigateur de la victime à son insu, en exploitant ses cookies automatiquement envoyés.

---

## 18. Validation, sanitization et output encoding

### À retenir
Trois contrôles complémentaires sur les entrées/sorties utilisateur :
- **Validation** : vérifier que l'entrée correspond au format attendu (un email ressemble à un email).
- **Sanitization** : supprimer/neutraliser les caractères dangereux avant stockage ou affichage.
- **Output encoding** : afficher la donnée comme **texte** et non comme du code.

### Comment ça fonctionne
Validation et sanitization s'appliquent à l'entrée ; l'output encoding s'applique à la sortie, au moment du rendu. Les trois ensemble bloquent HTML injection et XSS même si une couche est contournée.

### Pourquoi c'est important en cyber
Le contrôle **côté client** sert l'expérience utilisateur (UX) ; il se contourne trivialement. La sécurité réelle se joue **côté serveur**, et idéalement aussi à l'affichage.

### Point clé à mémoriser
Valider l'entrée, nettoyer la donnée, encoder la sortie — et toujours imposer la décision côté serveur.

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

## 24. Vulnérabilités web courantes

### À retenir
La plupart des failles web sont des **conséquences** de mauvaises décisions dans les couches précédentes (validation absente, contrôle d'accès oublié, requêtes concaténées).

### Comment ça fonctionne (vue d'ensemble)
| Vulnérabilité | Principe | Impact | Prévention (haut niveau) |
|---|---|---|---|
| **Broken Authentication** | Contourner l'authentification | Connexion sans identifiants valides | Auth robuste côté serveur |
| **Broken Access Control** | Accéder à ce qui est interdit | Accès admin, données d'autrui | Contrôle d'accès serveur sur chaque ressource |
| **Malicious File Upload** | Uploader un script exécutable | RCE sur le serveur | Valider type/contenu, stockage non exécutable |
| **File Inclusion** | Inclure un fichier non prévu | Lecture de code, RCE | Pas d'inclusion basée sur entrée utilisateur |
| **Command Injection** | Injecter une commande OS | Exécution sur le serveur | Ne pas passer d'entrée à des commandes système |
| **SQL Injection** | Injecter du SQL | Lecture/écriture base, RCE | Requêtes paramétrées |
| **IDOR / BOLA** | Manipuler un identifiant d'objet | Accès aux ressources d'autrui | Vérifier l'appartenance côté serveur |
| **Security Misconfiguration** | Réglage par défaut/erroné | Exposition variée | Durcissement, revue de config |
| **Vulnerable/Outdated Components** | Composant connu vulnérable | Exploit public | Mise à jour, inventaire des dépendances |

### Pourquoi c'est important en cyber
Comprendre **d'où vient** chaque faille (quelle couche, quelle décision) permet de la détecter, de l'expliquer au client et de proposer une remédiation structurelle.

### Point clé à mémoriser
Une vulnérabilité n'est pas un accident isolé : c'est le symptôme d'une couche mal conçue.

---

## 25. Broken Authentication vs Broken Access Control

### À retenir
Deux notions à ne **jamais confondre** :
- **Authentification** = « **Qui es-tu ?** » (prouver son identité).
- **Autorisation / contrôle d'accès** = « **As-tu le droit ?** » (vérifier les permissions).

### Comment ça fonctionne
- **Broken Authentication** : on contourne la vérification d'identité — login sans identifiants valides, devenir un autre utilisateur.
- **Broken Access Control** : on est authentifié, mais on accède à des ressources/fonctions interdites pour son rôle.

### Pourquoi c'est important en cyber
Ce sont parmi les failles **les plus fréquentes et les plus graves**. Le contrôle d'accès doit être vérifié **côté serveur sur chaque ressource**, pas déduit de l'interface affichée.

### Exemple concret
- Bypass de login via un champ email piégé.
- `roleid` modifiable à l'inscription (`roleid=3` → `roleid=0`) pour s'auto-attribuer un rôle admin.
- Accès direct à `/admin` sans en avoir le droit.
- Modifier `/user/701/edit-profile` en `/user/702/edit-profile` pour éditer le profil d'autrui (IDOR).

### Point clé à mémoriser
Authentification ≠ autorisation. Être connecté ne signifie pas avoir le droit.

---

## 26. File Upload, File Inclusion, Command Injection, SQL Injection

### À retenir
Quatre failles back-end critiques qui partagent une cause commune : **une entrée utilisateur traitée sans contrôle**.

### Comment ça fonctionne
- **Malicious File Upload** : l'application accepte un fichier sans valider type/contenu → upload d'un script (ex. `.php`) → exécution sur le serveur. Les contrôles faibles (extension seule) se contournent (ex. `shell.php.jpg`).
- **File Inclusion** : l'application inclut un fichier dont le chemin dépend de l'entrée utilisateur → lecture de code source, voire RCE.
- **Command Injection** : l'entrée est intégrée dans une commande OS → l'attaquant ajoute sa propre commande (ex. `| commande`) exécutée sur le serveur.
- **SQL Injection** : l'entrée est concaténée dans une requête SQL → l'attaquant modifie la logique de la requête (auth bypass, extraction de données, parfois RCE).

### Pourquoi c'est important en cyber
Ces failles mènent souvent **directement à l'exécution de code** ou à la **compromission de la base**, donc au contrôle du serveur. Ce sont des cibles prioritaires en pentest.

### Prévention (haut niveau)
- Upload : valider type **et** contenu, stocker hors zone exécutable.
- Inclusion : ne jamais baser un chemin d'inclusion sur l'entrée utilisateur.
- Command Injection : éviter d'appeler l'OS avec une entrée ; sinon, échappement strict / API dédiées.
- SQLi : **requêtes paramétrées** (préparées), jamais de concaténation.

> Objectif ici : **comprendre** le mécanisme et l'impact, pas exécuter une exploitation détaillée.

### Point clé à mémoriser
Entrée utilisateur + traitement non contrôlé (fichier, inclusion, commande, requête) = porte vers le serveur.

---

## 27. OWASP Top 10

### À retenir
Le classement de référence des risques web les plus critiques. À connaître comme grille de lecture.

### Liste (version moderne)
1. **Broken Access Control** — accès à des ressources interdites (ex. `/user/702`).
2. **Cryptographic Failures** — chiffrement absent/faible (ex. mots de passe en clair).
3. **Injection** — SQLi, command injection, etc. (entrée non filtrée).
4. **Insecure Design** — faille de conception, pas seulement de code (ex. pas de RBAC prévu).
5. **Security Misconfiguration** — réglages par défaut/erronés (ex. page d'admin exposée).
6. **Vulnerable and Outdated Components** — composant vulnérable connu (ex. plugin non patché).
7. **Identification and Authentication Failures** — authentification cassée (ex. bypass de login).
8. **Software and Data Integrity Failures** — mise à jour/dépendance non vérifiée (ex. pipeline compromis).
9. **Security Logging and Monitoring Failures** — pas de détection (ex. intrusion non journalisée).
10. **Server-Side Request Forgery (SSRF)** — forcer le serveur à émettre des requêtes (ex. accès à un service interne).

### Pourquoi c'est important en cyber
C'est le langage commun du pentest web : savoir classer une faille dans l'OWASP Top 10 structure le rapport et la priorisation.

### Point clé à mémoriser
L'OWASP Top 10 est une **grille de lecture**, pas un substitut à la compréhension de l'architecture.

---

## 28. Public vulnerabilities, CVE et CVSS

### À retenir
Les vulnérabilités publiques sont répertoriées par **CVE** et notées par **CVSS**. Identifier la **version** d'un composant est la première étape pour chercher un exploit.

### Comment ça fonctionne
- **CVE** (Common Vulnerabilities and Exposures) : identifiant unique d'une vulnérabilité connue.
- **NVD** (National Vulnerability Database) : fournit les scores CVSS de base.
- Sources d'exploits : **Exploit-DB**, **Rapid7 DB**, **GitHub advisories**.
- **CVSS** (Common Vulnerability Scoring System) : score de **0 à 10** basé sur des métriques **Base**, **Temporal**, **Environmental** (le NVD ne fournit que la Base).

Sévérité CVSS v3 :
| Sévérité | Score |
|---|---|
| None | 0.0 |
| Low | 0.1–3.9 |
| Medium | 4.0–6.9 |
| High | 7.0–8.9 |
| Critical | 9.0–10.0 |

### Pourquoi c'est important en cyber
Premier réflexe sur une application connue : **identifier le composant et sa version**, puis chercher un exploit public (priorité aux scores 8–10 ou menant à la RCE). À étendre aux composants externes (plugins, dépendances) et au serveur web lui-même (ex. Shellshock).

### Point clé à mémoriser
Pas de version identifiée = pas de recherche d'exploit efficace. Toujours commencer par l'empreinte (fingerprinting).

---

## 29. Méthodologie de lecture d'une application web

### À retenir
Une démarche reproductible pour cartographier puis tester une application, du visible vers le profond.

### Démarche
1. Identifier les **pages visibles**.
2. Observer le **trafic** (DevTools Network / Burp).
3. Lire le **code source** (View Source).
4. Identifier les **scripts JavaScript**.
5. Repérer les **endpoints / API**.
6. Identifier **stack et versions**.
7. Tester en **non authentifié**.
8. Tester en **authentifié**.
9. **Comparer les rôles** (user vs admin).
10. Tester les **entrées utilisateur**.
11. Vérifier l'**upload** de fichiers.
12. Vérifier le **contrôle d'accès**.
13. Examiner les **erreurs** 401 / 403 / 404 / 500.
14. **Documenter** proprement.

### Pourquoi c'est important en cyber
Une méthodologie évite les oublis (un rôle non testé, un endpoint JS ignoré) et rend l'audit reproductible et présentable au client.

### Point clé à mémoriser
Du visible vers le profond, du non authentifié vers l'authentifié, en comparant toujours les rôles.

---

## 30. Synthèse mentale

### Flux complet
```
Utilisateur → navigateur → front-end (HTML/CSS/JS)
           → requêtes HTTP/HTTPS
           → web server → application layer (validation / auth / droits)
           → database / services / API
           → réponse → rendu navigateur
```

### Synthèse sécurité
- Le **front-end est visible** (et modifiable, rejouable).
- Le **back-end décide** (c'est là qu'on impose auth, droits et validation).
- La **database contient la valeur**.
- L'**architecture** (segmentation, redondance) **limite ou amplifie** l'impact d'une compromission.

### Point clé à mémoriser
Front-end = ce qu'on voit. Back-end = ce qui décide. Database = ce qui vaut. Architecture = ce qui contient ou propage.

---

## 31. Commandes et réflexes utiles

### Ligne de commande
```bash
curl -I  https://cible        # en-têtes seuls (serveur, codes, redirections)
curl -v  https://cible        # détail complet requête/réponse
curl -s  https://cible        # mode silencieux (sortie propre)
curl -X OPTIONS -i https://cible/api/   # méthodes HTTP autorisées
curl -s https://cible/api/x | jq        # parser une réponse JSON
```

### Navigateur (DevTools)
- **View Source** (Ctrl+U) : commentaires, liens, scripts.
- **Network** : requêtes réelles, endpoints, en-têtes.
- **Sources** : fichiers JS, logique client.
- **Storage / Cookies** : cookies de session, tokens, flags (HttpOnly, SameSite).

### Réflexe
- `grep` les fichiers `.js` pour extraire les endpoints/API cachés.

### Point clé à mémoriser
curl pour le serveur, DevTools pour le client : deux angles d'observation complémentaires.

---

## 32. Erreurs fréquentes à éviter

- Faire **confiance au front-end** pour la sécurité.
- Stocker des **secrets dans le JS**.
- **Cacher** un bouton (CSS) au lieu de protéger la fonction côté serveur.
- Valider **uniquement côté client**.
- **Confondre authentification et autorisation**.
- **Exposer les versions** des composants.
- **Oublier de tester les rôles**.
- Accepter des **uploads sans contrôle** de type/contenu.
- **Concaténer** des entrées utilisateur dans une requête SQL.
- Croire qu'un **WAF remplace** du code sécurisé.
- Tester **uniquement sans compte** (ignorer le périmètre authentifié).
- **Ne pas lire les scripts JS**.

### Point clé à mémoriser
La plupart de ces erreurs reviennent à **faire confiance au client** ou à **confondre cacher et protéger**.

---

## 33. Résumé ultra-court (pour entretien)

> Une application web suit un modèle client/serveur : le **front-end** (HTML/CSS/JS) s'exécute dans le navigateur et est entièrement visible et modifiable, tandis que le **back-end** (web server, logique applicative, base de données) traite les requêtes HTTP et prend toutes les décisions de sécurité. La règle fondamentale est qu'on ne fait **jamais confiance au client** : authentification, autorisation et validation doivent être imposées côté serveur. Les vulnérabilités (XSS, SQLi, broken access control, IDOR, command injection…) ne sont pas des accidents isolés mais les **conséquences** d'une mauvaise décision dans une couche — entrée non filtrée, contrôle d'accès oublié, requête concaténée. L'**architecture** (segmentation, redondance) détermine ensuite si une compromission reste contenue ou se propage à tout le SI.

---

## 34. Mini quiz

1. **Quelle est la différence fondamentale entre front-end et back-end ?**
   Le front-end s'exécute dans le navigateur (visible et modifiable) ; le back-end s'exécute sur le serveur et prend les décisions de sécurité.

2. **Pourquoi ne faut-il jamais faire confiance au front-end ?**
   Tout ce qui est côté client est visible, modifiable et rejouable (JS désactivable, requêtes forgeables via curl/Burp).

3. **Que signifie « Web 2.0 » par rapport à « Web 1.0 » ?**
   Contenu dynamique et personnalisé (Web 2.0) vs pages statiques identiques pour tous (Web 1.0).

4. **Quelles sont les trois couches de la Three Tier Architecture ?**
   Presentation Layer, Application Layer, Data Layer.

5. **Quel modèle d'infrastructure est le plus risqué et pourquoi ?**
   « One Server » : tout sur un même serveur, donc une faille ou une panne compromet tout (œufs dans le même panier).

6. **Quel est l'intérêt sécurité de la segmentation (many servers / one database) ?**
   Un composant compromis n'expose pas directement les autres ; l'impact est contenu.

7. **Différence entre authentification et autorisation ?**
   Authentification = « qui es-tu ? » ; autorisation = « as-tu le droit ? ».

8. **Qu'est-ce qu'un IDOR ?**
   Manipuler un identifiant d'objet (ex. `/user/701` → `/user/702`) pour accéder aux ressources d'autrui faute de contrôle d'accès serveur.

9. **Différence entre HTML injection et XSS ?**
   HTML injection = injecter du HTML interprété ; XSS = injecter du JavaScript exécuté chez la victime.

10. **Cite les trois types de XSS.**
    Reflected, Stored, DOM.

11. **Comment fonctionne une attaque CSRF ?**
    Elle abuse de la session active : le navigateur joint automatiquement les cookies, exécutant une action non voulue au nom de la victime.

12. **Trois défenses contre le CSRF ?**
    Token anti-CSRF, attribut cookie SameSite, vérification Origin/Referer (et ressaisie du mot de passe pour actions sensibles).

13. **Différence entre validation, sanitization et output encoding ?**
    Validation = vérifier le format ; sanitization = nettoyer les caractères dangereux ; output encoding = afficher comme texte et non comme code.

14. **Quels ports écoutent typiquement les web servers ?**
    80 (HTTP) et 443 (HTTPS).

15. **Que signalent les codes HTTP 401 et 403 ?**
    401 = non authentifié ; 403 = authentifié mais accès interdit.

16. **Pourquoi IIS est-il un indice intéressant en pentest ?**
    Il tourne sur Windows Server et s'intègre à Active Directory, suggérant un environnement AD.

17. **Différence entre base SQL et NoSQL ?**
    SQL = tables/lignes/colonnes avec schéma et relations ; NoSQL = sans schéma fixe, flexible (clé-valeur, document, etc.).

18. **Pourquoi la concaténation d'entrée utilisateur dans une requête SQL est-elle dangereuse ?**
    Elle permet une SQL injection : l'attaquant modifie la logique de la requête.

19. **Que faut-il identifier en premier pour chercher un exploit public ?**
    La version du composant (web app, framework, plugin, serveur).

20. **Que mesure le score CVSS et sur quelle échelle ?**
    La sévérité d'une vulnérabilité, de 0 à 10 (Critical = 9.0–10.0 en v3).
