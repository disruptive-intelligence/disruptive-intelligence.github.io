---
title: Annexes
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - index.md
---

> Les annexes cadrent **quand et pourquoi** s'intéresser à ces sujets, sans les enseigner en détail. Ils sont **hors du cœur** de ce cours : maîtrise d'abord JS natif, DOM, fetch, JSON, Node.js et la sécurité côté client. Reviens-y ensuite, selon tes besoins.

## Annexe A — `var`, hoisting, `this`, prototypes

Les coins historiques et avancés du langage, utiles surtout pour **lire du vieux code** ou comprendre certaines bizarreries.

- **`var`** : l'ancienne déclaration de variable. Sa portée est la **fonction** (pas le bloc), ce qui crée des surprises. **À éviter à l'écriture** ; à connaître pour lire du code ancien. Préfère `const`/`let`.
- **Hoisting** : JavaScript « remonte » les déclarations en haut de leur portée. Avec `var`, une variable peut exister (valant `undefined`) avant sa ligne de déclaration. Avec `const`/`let`, l'accès avant déclaration lève une erreur (comportement plus sain).
- **`this`** : un mot-clé dont la valeur **dépend de la façon dont une fonction est appelée**. Source classique de confusion. Les fonctions fléchées ne créent pas leur propre `this` (elles héritent de l'englobant), ce qui simplifie souvent les choses. À approfondir le jour où tu écris des objets/classes complexes.
- **Prototypes** : le mécanisme d'héritage historique de JavaScript (avant la syntaxe `class`). Comprendre les prototypes éclaire le fonctionnement profond du langage, mais n'est pas nécessaire pour les usages de ce cours.

**Quand t'y intéresser :** quand tu lis du code legacy, ou quand une bizarrerie de `this`/hoisting te bloque.

## Annexe B — TypeScript

**TypeScript** est un sur-ensemble de JavaScript qui ajoute un **typage statique** : tu annotes les types (`let port: number = 443`), et un compilateur vérifie la cohérence **avant** l'exécution.

- **Pourquoi ça existe :** attraper des erreurs de type à l'écriture plutôt qu'à l'exécution, et documenter le code. Très répandu dans les projets professionnels d'envergure.
- **Pourquoi hors cœur ici :** pour comprendre le web, lire du JS, scripter en Node et raisonner sécurité, **JavaScript natif suffit**. TypeScript ajoute une couche d'outillage qui n'apporte rien aux objectifs de ce cours pour un débutant.
- **Quand t'y mettre :** quand tu rejoins un projet qui l'utilise, ou quand tes scripts grossissent au point que le typage devient un confort.

## Annexe C — Frameworks front (React, Vue, Angular, Next.js)

Les **frameworks** structurent les grandes applications web (interfaces complexes, composants réutilisables, gestion d'état).

- **React, Vue, Angular** : trois approches pour construire des interfaces riches. **Next.js** est un framework bâti sur React, ajoutant rendu serveur et routage.
- **Pourquoi hors cœur ici :** ils supposent une bonne maîtrise de JavaScript natif, du DOM et de l'asynchrone — exactement ce que ce cours construit. Apprendre un framework **avant** ces bases mène à du code qu'on copie sans comprendre.
- **Lien cyber :** côté défensif, tu rencontreras des applications en React/Vue. Savoir lire du JS et comprendre le DOM (ce cours) t'aide à les analyser, même sans maîtriser le framework. Beaucoup de failles (dont le XSS) se raisonnent au niveau JavaScript/DOM, sous le framework.
- **Quand t'y mettre :** après être à l'aise avec tout ce cours, si tu veux construire des interfaces conséquentes.

## Annexe D — Outillage moderne (Vite, bundlers)

Les projets front utilisent des outils de **build** : un **bundler** (Vite, esbuild, webpack…) regroupe et optimise les fichiers JavaScript pour la production.

- **À quoi ça sert :** rassembler de nombreux modules en quelques fichiers optimisés, gérer les dépendances, recharger à chaud pendant le développement.
- **Pourquoi hors cœur ici :** ce cours fonctionne avec un simple `index.html` + `script.js` et avec `node script.js` — aucun bundler nécessaire pour apprendre. L'outillage s'ajoute quand le projet grandit.
- **Quand t'y intéresser :** quand tu travailles sur une application avec un framework, ou quand tu vois un `vite.config` / `webpack.config` dans un projet à analyser.

## Annexe E — Express / backend

**Express** est un framework Node.js minimaliste pour écrire des **serveurs web** et des **APIs**.

- **Le lien avec la sécurité :** c'est **côté serveur** que se joue la vraie sécurité (chapitre 32). Express illustre où vivent la **validation qui fait foi**, l'**authentification**, les **autorisations**, et où l'on pose les **en-têtes de sécurité** et les **cookies `HttpOnly`** (chapitre 31).
- **Pourquoi hors cœur ici :** ce cours est orienté **JavaScript côté client + scripting Node**. Le développement backend complet est un sujet à part entière.
- **Quand t'y mettre :** quand tu veux comprendre l'autre moitié du web (le serveur), ou construire toi-même une petite API. Comprendre le backend renforce énormément le réflexe « le client n'est jamais de confiance ».

## Annexe F — Pont vers la suite cyber

Ce cours est une **brique** d'un parcours plus large. Voici où il mène, en cohérence avec la collection (`Bash / Python → JavaScript → Web Security → Docker / Kubernetes`).

- **Web Security (la suite directe).** Tu as les fondations pour aborder sérieusement la sécurité web : XSS (chapitres 15, 30), CSP et en-têtes (31), cookies et sessions (19), CORS (24), le principe du client non fiable (32), la lecture de code (33). La suite approfondit ces vulnérabilités et en ajoute (injection, CSRF, contrôle d'accès…), **toujours dans un cadre légal et défensif**.
- **Bug bounty débutant.** Avec la lecture de JavaScript (chapitre 33), l'analyse des requêtes (`fetch`, DevTools Réseau), la compréhension du DOM et des en-têtes, tu as la base pour commencer à explorer des programmes légitimes. Insiste sur le **cadre** : uniquement sur les périmètres autorisés, avec les règles du programme.
- **OSINT tooling.** Node.js (Partie 6) te permet d'écrire tes propres outils : extracteurs d'IOC, clients d'APIs de threat intel, parsers de données publiques, enrichissement en lot. Tu réutilises directement regex, `fetch`, JSON, `fs` et modules.
- **Vers le backend et l'infra.** Express (annexe E) puis la conteneurisation (cours Docker/Kubernetes de la collection) complètent la vision : du client au serveur, puis au déploiement.

**Prochaine étape recommandée :** consolide ce cours par les mini-projets, puis enchaîne sur **Web Security**, où tout ce que tu as appris côté client prend tout son sens — du point de vue de la défense.

-----

*Fin du cours. Tu sais désormais comprendre le web, lire et écrire du JavaScript, manipuler des données, automatiser avec Node.js, et raisonner sécurité côté client. La suite, c'est la pratique : reprends les mini-projets, adapte-les à tes propres données, et garde la Boîte à risques sous les yeux.*
