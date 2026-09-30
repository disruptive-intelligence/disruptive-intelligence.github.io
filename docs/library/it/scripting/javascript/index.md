---
title: JavaScript
source: IT/05_Scripting_Langage-Prog/JavaScript.md
format: cours
---

*De zéro aux scripts web, au DOM, aux APIs et aux bases de la sécurité web*

-----

> **Prérequis :** Aucun en développement web. Si tu as déjà touché à Linux, Bash ou Python (par exemple via les autres cours de cette collection), tu iras plus vite, mais ce n'est pas obligatoire.
>
> **Machine de lab :** un **navigateur moderne** (Firefox ou Chromium/Chrome), un **éditeur de texte** (VS Code, ou même nano), et plus tard **Node.js LTS**. Rien d'autre.
>
> **Orientation :** ce cours enseigne JavaScript en s'appuyant sur des exemples d'**administration**, de **cybersécurité défensive** (SOC, analyse de logs, OSINT, CTI), et de **sécurité web côté client**. On apprend à **comprendre** le web, **lire** du JavaScript trouvé dans une page, **manipuler** des données (JSON, URLs, IOC), **automatiser** un peu avec Node.js, et **comprendre les risques** de sécurité du navigateur. Jamais à attaquer : tous les exemples sont légitimes et défensifs.

-----

### Glossaire — Les mots à connaître

Reviens ici dès qu'un mot te semble flou. On mélange volontairement les termes JavaScript et les termes cyber, car tu vas les croiser ensemble.

| Terme | Définition simple |
| --- | --- |
| **Navigateur** | Le logiciel qui affiche les pages web (Firefox, Chrome…). Il contient un **moteur JavaScript**. |
| **Moteur JS** | La partie du navigateur (ou de Node.js) qui exécute le code JavaScript. |
| **Console** | La fenêtre des outils développeur (`F12`) où tu peux taper et exécuter du JavaScript directement. |
| **DevTools** | Les "outils développeur" du navigateur (`F12`) : console, inspecteur, réseau… |
| **Node.js** | Un programme qui permet d'exécuter du JavaScript **en dehors** du navigateur, comme un script Python. |
| **Runtime** | L'environnement qui exécute le code : le navigateur **ou** Node.js. Le même langage, deux mondes. |
| **Script** | Un fichier texte (`.js`) contenant des instructions JavaScript. |
| **Variable** | Un conteneur nommé qui stocke une valeur (texte, nombre, liste…). |
| **Type** | La nature d'une valeur : texte (`string`), nombre (`number`), vrai/faux (`boolean`)… |
| **Fonction** | Un bloc de code réutilisable auquel on donne un nom. |
| **Tableau (array)** | Une collection ordonnée de valeurs : `["a", "b", "c"]`. |
| **Objet** | Une collection de paires clé-valeur : `{ip: "1.2.3.4", port: 443}`. |
| **DOM** | *Document Object Model* : la représentation en arbre d'une page HTML, que JavaScript peut manipuler. |
| **Événement** | Une action détectable : un clic, une touche, l'envoi d'un formulaire… |
| **Callback** | Une fonction qu'on donne à exécuter "plus tard", quand quelque chose se produit. |
| **Asynchrone** | Du code qui ne s'exécute pas immédiatement dans l'ordre, typiquement en attendant le réseau. |
| **Promesse (Promise)** | Un objet qui représente un résultat **futur** (réussite ou échec). |
| **JSON** | *JavaScript Object Notation* : le format texte universel d'échange de données sur le web. |
| **API** | *Application Programming Interface* : un service accessible via le réseau auquel on envoie des requêtes. |
| **Requête HTTP** | Une demande envoyée à un serveur web (GET, POST…). |
| **`fetch`** | La fonction JavaScript moderne pour faire des requêtes HTTP. |
| **LocalStorage** | Un stockage de données persistant dans le navigateur (clé-valeur). |
| **Cookie** | Une petite donnée stockée par le navigateur, souvent envoyée automatiquement au serveur. |
| **Token** | Un jeton secret prouvant une identité ou une autorisation (à protéger absolument). |
| **XSS** | *Cross-Site Scripting* : injection de code malveillant dans une page web. |
| **DOM XSS** | Un XSS causé par du JavaScript qui insère une donnée non maîtrisée dans la page. |
| **CORS** | *Cross-Origin Resource Sharing* : la règle du **navigateur** qui encadre les requêtes vers un autre domaine. |
| **CSP** | *Content Security Policy* : un en-tête de sécurité qui limite ce qu'une page a le droit d'exécuter. |
| **IOC** | *Indicator of Compromise* : une trace d'attaque (IP, domaine, hash, URL malveillante…). |
| **OSINT** | *Open Source Intelligence* : renseignement à partir de sources publiques. |
| **SOC** | *Security Operations Center* : l'équipe qui surveille et défend un système d'information. |
| **`npm`** | Le gestionnaire de paquets de Node.js (installe des bibliothèques). |

-----

### Comment penser JavaScript

Avant d'écrire la moindre ligne, comprends la logique de base. Comme tout langage, JavaScript suit le schéma :

```text
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le code    →  Ce que le code
  code reçoit      fait avec            produit / affiche / modifie
```


En contexte web et cyber, ce schéma est partout :

```text
  Du texte     →   On extrait les    →  Une liste d'IP
  de logs          IP avec une regex    dédoublonnées
```


```text
  Un clic      →   On lit un champ   →  On affiche un résultat
  utilisateur      et on le traite      dans la page (en sécurité)
```


Il n'y a que 5 briques de base, comme dans n'importe quel langage :

1. **Recevoir** des données (saisie, fichier, réponse d'API…).
2. **Stocker** dans des variables.
3. **Tester** si quelque chose est vrai ou faux (conditions).
4. **Répéter** une action (boucles).
5. **Afficher ou enregistrer** un résultat (console, page, fichier).

Mais JavaScript ajoute **une question fondatrice** que Python et Bash n'ont pas :

> ### 🧭 La question à se poser AVANT tout : « Où tourne mon code ? »
>
> JavaScript vit dans **deux mondes différents** :
>
> - **Le navigateur** : ton code peut manipuler la page (DOM), réagir aux clics, faire des requêtes web — mais il **n'a pas accès** aux fichiers de ta machine.
> - **Node.js** : ton code peut lire/écrire des fichiers, prendre des arguments — mais il **n'y a pas de page**, pas de DOM, pas de bouton.
>
> Beaucoup d'erreurs de débutant viennent d'une confusion entre ces deux mondes (« pourquoi `document` ne marche pas dans Node ? », « pourquoi je ne peux pas ouvrir un fichier dans le navigateur ? »). **Garde cette question en tête à chaque chapitre.** Le cours te le rappellera avec des encadrés « Navigateur vs Node.js ».

-----

### La grande différence avec Python et Bash

Si tu viens des cours Bash ou Python de cette collection, trois choses vont changer.

**1. JavaScript est né dans le navigateur.** Bash pilote le système, Python est généraliste, mais JavaScript a d'abord été conçu pour **rendre les pages web vivantes**. C'est sa force et son contexte naturel. Node.js est venu **après** pour l'amener hors du navigateur.

**2. JavaScript est asynchrone et événementiel.** En Python, ton script s'exécute ligne par ligne, du début à la fin. En JavaScript navigateur, ton code **attend des événements** (un clic, une réponse réseau) et y réagit. C'est un changement de mentalité qu'on introduira en douceur (Partie 5).

**3. Côté navigateur, JavaScript ne contrôle pas le système.** Un script Python peut lire `/etc/passwd`. Un JavaScript dans une page web **ne peut pas lire librement** les fichiers de ta machine : il peut seulement accéder à un fichier si l'utilisateur le **sélectionne explicitement** via un champ prévu pour cela (par exemple un `<input type="file">`). Le navigateur impose cette limite par sécurité. Elle est **volontaire** et tu vas apprendre à raisonner avec.

Pont rapide pour les profils Python : ce que tu appelais `print()` devient `console.log()`, une `liste` devient un `array`, un `dictionnaire` devient un `objet`, et `json` est intégré nativement. Tu n'es pas en terrain totalement inconnu.

-----

### 🧨 Boîte à risques JavaScript / Web

> **À lire maintenant, même sans tout comprendre.** Ce tableau est le **fil rouge sécurité** du cours. Chaque ligne est une mauvaise pratique fréquente, et chaque ligne sera traitée en profondeur dans le chapitre indiqué. Reviens-y régulièrement : à la fin du cours, tu dois comprendre **pourquoi** chacune est dangereuse.

| # | Mauvaise pratique | Pourquoi c'est risqué (en une phrase) | Vu au chapitre |
| --- | --- | --- | --- |
| 1 | `innerHTML` avec une donnée non maîtrisée | Permet d'injecter du code dans la page → **XSS / DOM XSS**. | Ch. 15, 30 |
| 2 | Utiliser `eval` | Exécute du texte comme du code → exécution arbitraire. | Ch. 13, 30 |
| 3 | Croire que la validation **côté client** suffit | Le navigateur est modifiable : seule la validation **serveur** protège. | Ch. 17 |
| 4 | Stocker un **secret/token dans LocalStorage** | Lisible par tout JS de la page → volé via XSS. | Ch. 18, 30 |
| 5 | **Exposer un token** côté navigateur | Tout ce qui est côté client est visible par l'utilisateur. | Ch. 18, 32 |
| 6 | Confondre **cookie / sessionStorage / LocalStorage** | Mauvais choix de stockage → fuite ou perte de données. | Ch. 18, 19 |
| 7 | Mal comprendre **CORS** | On croit à tort que c'est une protection serveur (c'est une règle navigateur). | Ch. 24, 31 |
| 8 | Croire qu'un **bouton masqué** protège une action | Cacher en frontend ≠ interdire ; l'action reste appelable. | Ch. 17, 32 |
| 9 | **Dépendances npm** non maîtrisées | Code tiers exécuté chez toi → risque supply chain. | Ch. 29 |
| 10 | **Copier-coller du code inconnu** | Tu exécutes quelque chose que tu ne comprends pas. | Ch. 29, 30 |
| 11 | Ne pas gérer les **erreurs réseau** (`fetch`) | L'appli casse ou se comporte mal à la moindre panne. | Ch. 22, 23 |
| 12 | Manipuler du **JSON sans validation** | Une donnée inattendue fait planter ou trompe ton code. | Ch. 12 |
| 13 | Afficher directement une **donnée utilisateur** dans le DOM | Vecteur direct de XSS si non échappée. | Ch. 15, 30 |
| 14 | Confondre `==` et `===` | Comparaisons surprenantes dues à la conversion implicite. | Ch. 4 |
| 15 | Confondre `null` et `undefined` | Tests faux, bugs silencieux. | Ch. 3 |
| 16 | Cookie sans `HttpOnly` / `Secure` / `SameSite` | Cookie vulnérable au vol ou à l'envoi non sécurisé. | Ch. 19, 31 |
| 17 | Croire que le JS navigateur protège une **logique sensible** | Tout le code client est lisible et modifiable. | Ch. 32 |

> **Réflexe à graver dès aujourd'hui :** *tout ce qui tourne dans le navigateur est sous le contrôle de l'utilisateur.* Le frontend sert à l'expérience, **jamais** à la sécurité.

-----

### Table des matières


#### Partie 0 — Ouverture
*(Glossaire, Comment penser JavaScript, différence avec Python/Bash, Boîte à risques — ci-dessus.)*


#### Partie 1 — Fondamentaux du langage

*(dans la console et un premier fichier)*

1. Découverte de JavaScript et premier code
2. Console, fichier `.js` et page minimale
3. Variables et types
4. Opérateurs, comparaisons et logique
5. Conditions
6. Boucles


#### Partie 2 — Structurer les données et le code

7. Fonctions
8. Chaînes de caractères et l'objet `URL`
9. Regex simples pour OSINT / SOC *(chapitre court)*
10. Tableaux et méthodes utiles (`map`, `filter`, `find`…)
11. Objets
12. JSON
13. Erreurs, exceptions et débogage


#### Partie 3 — JavaScript dans le navigateur : DOM et événements

14. Le DOM : comprendre et sélectionner
15. Modifier le DOM en sécurité (`textContent` vs `innerHTML`)
16. Événements
17. Formulaires et limites de la validation côté client


#### Partie 4 — Stockage navigateur et sécurité des données client

18. LocalStorage et SessionStorage
19. Cookies et les limites de JavaScript


#### Partie 5 — Le web dynamique : requêtes HTTP et asynchrone

20. Comprendre l'asynchrone
21. Promesses
22. `fetch` et requêtes HTTP
23. `async` / `await`
24. CORS : comprendre le blocage


#### Partie 6 — Node.js : automatiser et scripter hors navigateur

25. Découverte de Node.js
26. Lire et écrire des fichiers
27. Arguments et petits outils CLI
28. Modules
29. `npm`, `package.json` et dépendances

## Sommaire

- [Partie 7 — Sécurité web côté client : synthèse défensive](01-partie-7-securite-web-cote-client-synthese-defensi/index.md)
    - [Chapitre 1 — Découverte de JavaScript et premier code](01-partie-7-securite-web-cote-client-synthese-defensi/01-chapitre-1-decouverte-de-javascript-et-premier-cod.md)
    - [Chapitre 2 — Console, fichier .js et page minimale](01-partie-7-securite-web-cote-client-synthese-defensi/02-chapitre-2-console-fichier-js-et-page-minimale.md)
    - [Chapitre 3 — Variables et types](01-partie-7-securite-web-cote-client-synthese-defensi/03-chapitre-3-variables-et-types.md)
    - [Chapitre 4 — Opérateurs, comparaisons et logique](01-partie-7-securite-web-cote-client-synthese-defensi/04-chapitre-4-operateurs-comparaisons-et-logique.md)
    - [Chapitre 5 — Conditions](01-partie-7-securite-web-cote-client-synthese-defensi/05-chapitre-5-conditions.md)
    - [Chapitre 6 — Boucles](01-partie-7-securite-web-cote-client-synthese-defensi/06-chapitre-6-boucles.md)
    - [Chapitre 7 — Fonctions](01-partie-7-securite-web-cote-client-synthese-defensi/07-chapitre-7-fonctions.md)
    - [Chapitre 8 — Chaînes de caractères et l'objet URL](01-partie-7-securite-web-cote-client-synthese-defensi/08-chapitre-8-chaines-de-caracteres-et-l-objet-url.md)
    - [Chapitre 9 — Regex simples pour OSINT / SOC](01-partie-7-securite-web-cote-client-synthese-defensi/09-chapitre-9-regex-simples-pour-osint-soc.md)
    - [Chapitre 10 — Tableaux et méthodes utiles](01-partie-7-securite-web-cote-client-synthese-defensi/10-chapitre-10-tableaux-et-methodes-utiles.md)
    - [Chapitre 11 — Objets](01-partie-7-securite-web-cote-client-synthese-defensi/11-chapitre-11-objets.md)
    - [Chapitre 12 — JSON](01-partie-7-securite-web-cote-client-synthese-defensi/12-chapitre-12-json.md)
    - [Chapitre 13 — Erreurs, exceptions et débogage](01-partie-7-securite-web-cote-client-synthese-defensi/13-chapitre-13-erreurs-exceptions-et-debogage.md)
    - [Chapitre 14 — Le DOM : comprendre et sélectionner](01-partie-7-securite-web-cote-client-synthese-defensi/14-chapitre-14-le-dom-comprendre-et-selectionner.md)
    - [Chapitre 15 — Modifier le DOM en sécurité (textContent vs innerHTML)](01-partie-7-securite-web-cote-client-synthese-defensi/15-chapitre-15-modifier-le-dom-en-securite-textconten.md)
    - [Chapitre 16 — Événements](01-partie-7-securite-web-cote-client-synthese-defensi/16-chapitre-16-evenements.md)
    - [Chapitre 17 — Formulaires et limites de la validation côté client](01-partie-7-securite-web-cote-client-synthese-defensi/17-chapitre-17-formulaires-et-limites-de-la-validatio.md)
    - [Chapitre 18 — LocalStorage et SessionStorage](01-partie-7-securite-web-cote-client-synthese-defensi/18-chapitre-18-localstorage-et-sessionstorage.md)
    - [Chapitre 19 — Cookies et les limites de JavaScript](01-partie-7-securite-web-cote-client-synthese-defensi/19-chapitre-19-cookies-et-les-limites-de-javascript.md)
    - [Chapitre 20 — Comprendre l'asynchrone](01-partie-7-securite-web-cote-client-synthese-defensi/20-chapitre-20-comprendre-l-asynchrone.md)
    - [Chapitre 21 — Promesses](01-partie-7-securite-web-cote-client-synthese-defensi/21-chapitre-21-promesses.md)
    - [Chapitre 22 — fetch et requêtes HTTP](01-partie-7-securite-web-cote-client-synthese-defensi/22-chapitre-22-fetch-et-requetes-http.md)
    - [Chapitre 23 — async / await](01-partie-7-securite-web-cote-client-synthese-defensi/23-chapitre-23-async-await.md)
    - [Chapitre 24 — CORS : comprendre le blocage](01-partie-7-securite-web-cote-client-synthese-defensi/24-chapitre-24-cors-comprendre-le-blocage.md)
    - [Chapitre 25 — Découverte de Node.js](01-partie-7-securite-web-cote-client-synthese-defensi/25-chapitre-25-decouverte-de-node-js.md)
    - [Chapitre 26 — Lire et écrire des fichiers](01-partie-7-securite-web-cote-client-synthese-defensi/26-chapitre-26-lire-et-ecrire-des-fichiers.md)
    - [Chapitre 27 — Arguments et petits outils CLI](01-partie-7-securite-web-cote-client-synthese-defensi/27-chapitre-27-arguments-et-petits-outils-cli.md)
    - [Chapitre 28 — Modules](01-partie-7-securite-web-cote-client-synthese-defensi/28-chapitre-28-modules.md)
    - [Chapitre 29 — npm, package.json et dépendances](01-partie-7-securite-web-cote-client-synthese-defensi/29-chapitre-29-npm-package-json-et-dependances.md)
    - [Chapitre 30 — XSS et DOM XSS expliqués](01-partie-7-securite-web-cote-client-synthese-defensi/30-chapitre-30-xss-et-dom-xss-expliques.md)
    - [Chapitre 31 — CSP, en-têtes et défenses navigateur](01-partie-7-securite-web-cote-client-synthese-defensi/31-chapitre-31-csp-en-tetes-et-defenses-navigateur.md)
    - [Chapitre 32 — Le réflexe fondamental](01-partie-7-securite-web-cote-client-synthese-defensi/32-chapitre-32-le-reflexe-fondamental.md)
    - [Chapitre 33 — Lire un script JavaScript inconnu](01-partie-7-securite-web-cote-client-synthese-defensi/33-chapitre-33-lire-un-script-javascript-inconnu.md)
- [Synthèse finale & cheat-sheets](02-synthese-finale-cheat-sheets.md)
- [Annexes](03-annexes.md)
