---
title: 'Chapitre 14 — Le DOM : comprendre et sélectionner'
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 14
chapters: 35
---

## Le minimum à savoir

Jusqu'ici, on a affiché dans la **console**. Maintenant, on va modifier la **page** elle-même. Pour cela, il faut comprendre le **DOM**.

### Qu'est-ce que le DOM ?

Quand le navigateur charge une page HTML, il la transforme en un **arbre d'objets** manipulable par JavaScript : le **DOM** (*Document Object Model*). Chaque balise HTML devient un **nœud** dans cet arbre.

```html
<body>
  <h1>Titre</h1>
  <p>Paragraphe</p>
</body>
```

devient, dans le DOM, un arbre :

```text
document
  └── body
        ├── h1  ("Titre")
        └── p   ("Paragraphe")
```

JavaScript accède à cet arbre via l'objet global **`document`**. Modifier le DOM = modifier ce que l'utilisateur voit, **en direct**, sans recharger la page.

> ### 🧭 Navigateur vs Node.js
> Le DOM et l'objet `document` **n'existent que dans le navigateur**. Dans Node.js (Partie 6), il n'y a pas de page : `document` n'existe pas. C'est l'une des différences les plus importantes entre les deux mondes. Si tu vois `document is not defined`, tu es probablement en train d'exécuter du code navigateur dans Node.

### Sélectionner des éléments

Pour modifier un élément, il faut d'abord l'**attraper**. La méthode moderne est **`querySelector`**, qui utilise la syntaxe des sélecteurs CSS.

```html
<h1 id="titre">Page de test</h1>
<p class="info">Premier paragraphe</p>
<p class="info">Deuxième paragraphe</p>
```

```javascript
// Par id (avec #)
const titre = document.querySelector("#titre");

// Par classe (avec .)
const premierInfo = document.querySelector(".info");   // le PREMIER trouvé

// Tous les éléments correspondants
const tousLesInfos = document.querySelectorAll(".info");   // une liste

// Par balise
const premierP = document.querySelector("p");
```

- **`querySelector`** renvoie le **premier** élément correspondant (ou `null` si aucun).
- **`querySelectorAll`** renvoie **tous** les éléments (une liste qu'on peut parcourir avec `for...of`).

```javascript
const infos = document.querySelectorAll(".info");
console.log(infos.length);   // 2

for (const p of infos) {
  console.log(p.textContent);   // "Premier paragraphe", puis "Deuxième paragraphe"
}
```

## Très utile en pratique

Lire le contenu et les attributs d'un élément :

```javascript
const lien = document.querySelector("a");
console.log(lien.textContent);        // le texte du lien
console.log(lien.getAttribute("href")); // l'URL du lien
```

## Exemple simple

Page `index.html` :

```html
<body>
  <h1 id="statut">En attente</h1>
  <script src="script.js"></script>
</body>
```

`script.js` :

```javascript
const titre = document.querySelector("#statut");
console.log("Texte actuel :", titre.textContent);   // "En attente"
```

## Application IT / cyber / OSINT

Comprendre le DOM est **fondamental** pour analyser une page web. En OSINT, tu inspectes le DOM (onglet *Éléments* des DevTools) pour voir la structure réelle d'une page, repérer des données cachées, des champs, des liens. `querySelectorAll("a")` dans la console te liste tous les liens d'une page — un geste de reconnaissance classique. Comprendre comment JavaScript lit et modifie le DOM est aussi le préalable indispensable pour comprendre les failles XSS (chapitre suivant et Partie 7).

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, les appels à `querySelector` / `getElementById` te montrent **quels éléments de la page le code manipule**. C'est une piste directe sur son comportement.

## ❌ Erreur classique

```javascript
// ❌ Sélectionner un élément qui n'existe pas encore (script dans le <head>)
// → querySelector renvoie null
const titre = document.querySelector("#statut");
console.log(titre.textContent);   // ❌ TypeError: Cannot read properties of null

// ✅ Placer le <script> à la fin du <body> (rappel chapitre 2)
//    ou vérifier que l'élément existe

// ❌ Oublier le # ou le . dans le sélecteur
document.querySelector("statut");    // cherche une balise <statut> → null
document.querySelector("#statut");   // ✅ cherche l'id "statut"
```

> **Réflexe diagnostic :** `Cannot read properties of null` après un `querySelector` ? Soit le sélecteur est faux (oubli de `#`/`.`), soit l'élément n'existe pas encore (script trop tôt). Vérifie la position du `<script>` et l'orthographe du sélecteur.

## Exercices

**Guidé**
1. Crée une page avec un `<h1 id="titre">` et deux `<p class="ligne">`.
2. Dans `script.js`, sélectionne le titre et affiche son `textContent`.
3. Sélectionne tous les `.ligne` et affiche combien il y en a.

**Autonome**
Ajoute trois `<a href="...">` à ta page. Dans la console, écris du code qui liste tous les `href` de la page (sélectionne tous les `a`, parcours-les, affiche `getAttribute("href")`).

**Défi**
Sur n'importe quelle page web réelle, ouvre la console et compte le nombre de liens (`document.querySelectorAll("a").length`), puis affiche les 5 premiers `href`. C'est un mini-geste de reconnaissance OSINT.

## ✅ Tu sais maintenant…

- expliquer ce qu'est le DOM (l'arbre d'objets d'une page) ;
- comprendre que `document` n'existe que dans le navigateur ;
- sélectionner avec `querySelector` (premier) et `querySelectorAll` (tous) ;
- utiliser les sélecteurs CSS (`#id`, `.classe`, `balise`) ;
- lire `textContent` et les attributs ;
- diagnostiquer un `null` après sélection.

-----
