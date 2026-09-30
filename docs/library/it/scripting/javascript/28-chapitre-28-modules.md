---
title: Chapitre 28 — Modules
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 28
chapters: 35
---

## Le minimum à savoir

Quand un projet grandit, on **découpe** le code en plusieurs fichiers réutilisables : les **modules**. Node a deux systèmes ; on apprend le plus simple d'abord.

### CommonJS : `require` et `module.exports`

C'est le système historique de Node, omniprésent.

**Fichier `outils.js` (le module qui exporte) :**

```javascript
function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

function extraireIps(texte) {
  return texte.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g) || [];
}

// On exporte ce qu'on veut rendre disponible
module.exports = { estIpPrivee, extraireIps };
```

**Fichier `main.js` (qui importe) :**

```javascript
const { estIpPrivee, extraireIps } = require("./outils");

console.log(estIpPrivee("192.168.1.1"));   // true
console.log(extraireIps("vu 8.8.8.8 et 1.1.1.1"));   // ["8.8.8.8", "1.1.1.1"]
```

Note le `./` devant `outils` : il indique un fichier **local** (par opposition à un module installé).

### Les modules intégrés

`fs` (chapitre 26) est un module intégré : `require("fs")` sans `./`. Node en fournit beaucoup (`path`, `crypto`, `os`…).

### Mention : les ES Modules (`import`)

Le JavaScript moderne a une autre syntaxe, **les ES Modules**, que tu as déjà vue côté navigateur dans certains contextes :

```javascript
// Syntaxe ES Modules (import/export)
import { estIpPrivee } from "./outils.js";
export function maFonction() { }
```

> ### ⚠️ À ne pas confondre : `require` vs `import` vs `<script>`
> - **`require(...)` / `module.exports`** : CommonJS, le système classique de Node. Commence par là.
> - **`import` / `export`** : ES Modules, syntaxe moderne (navigateur, et Node avec configuration). Tu la verras beaucoup.
> - **`<script src="...">`** : la façon de charger du JS dans une **page HTML** (Partie 1), sans rapport avec les modules Node.
>
> Pour débuter en Node, **CommonJS (`require`) est le plus simple**. On reste dessus dans ce cours.

## Très utile en pratique

Séparer la logique réutilisable (un module `outils.js`) des scripts qui l'utilisent rend ton code **propre et testable**. Tu écris tes fonctions d'analyse une fois, tu les importes dans plusieurs outils.

## Exemple simple

`math.js` :

```javascript
function doubler(n) { return n * 2; }
module.exports = { doubler };
```

`app.js` :

```javascript
const { doubler } = require("./math");
console.log(doubler(21));   // 42
```

```bash
node app.js
```

## Application IT / cyber / OSINT

Au fur et à mesure que ta boîte à outils défensive grandit, les modules te permettent de **factoriser** : un module `ioc.js` avec tes fonctions d'extraction/validation d'IP, domaines, hash, importé par tous tes outils de parsing et de triage. C'est ainsi qu'on construit une bibliothèque personnelle réutilisable, exactement comme on importe ses propres modules en Python.

> ### 🔍 Lecture de code inconnu
> Les `require`/`import` en tête d'un fichier révèlent **ses dépendances** : quels modules internes et quels paquets externes il utilise. C'est la première chose à lire pour comprendre la surface d'un script — et repérer une dépendance suspecte (chapitre suivant).

## ❌ Erreur classique

```javascript
// ❌ Oublier le ./ pour un fichier local
const o = require("outils");    // cherche un MODULE INSTALLÉ "outils" → erreur
const o2 = require("./outils"); // ✅ fichier local

// ❌ Oublier d'exporter ce qu'on veut importer
// dans outils.js : pas de module.exports → require renvoie {} vide

// ❌ Mélanger require et import sans configuration adaptée
// → "Cannot use import statement outside a module"
//   Pour débuter, reste sur require (CommonJS).
```

> **Réflexe diagnostic :** `Cannot find module './outils'` ? Vérifie le chemin (`./`, l'extension, le dossier). `undefined` à l'import ? Tu as oublié le `module.exports`.

## Exercices

**Guidé**
1. Crée `outils.js` avec une fonction `estIpPrivee` exportée.
2. Crée `main.js` qui l'importe et l'utilise.
3. Lance `node main.js`.

**Autonome**
Crée un module `ioc.js` qui exporte `extraireIps(texte)` et `extraireEmails(texte)`. Importe-le dans un script qui lit un fichier et affiche les IOC trouvés.

**Défi**
Réorganise ton parser de logs (Partie 2 / chapitre 26) en deux fichiers : un module `analyse.js` (fonctions de parsing et de comptage) et un `cli.js` (lecture du fichier en argument, appel des fonctions, écriture du rapport). C'est une vraie structure d'outil.

## ✅ Tu sais maintenant…

- découper le code en modules ;
- exporter avec `module.exports` et importer avec `require("./fichier")` ;
- distinguer module local (`./`) et module intégré/installé ;
- distinguer `require`, `import` et `<script>` ;
- factoriser une bibliothèque de fonctions réutilisables.

-----
