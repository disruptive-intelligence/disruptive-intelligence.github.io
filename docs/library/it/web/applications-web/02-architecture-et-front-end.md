---
title: Architecture et front-end
source: IT/05 Web & applications/Applications web/Applications web.md
note: Applications web
up:
- - Applications web
  - index.md
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
