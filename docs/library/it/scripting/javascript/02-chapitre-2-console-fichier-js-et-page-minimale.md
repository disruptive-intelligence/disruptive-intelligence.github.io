---
title: Chapitre 2 — Console, fichier .js et page minimale
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 2
chapters: 35
---

## Le minimum à savoir

La console est parfaite pour **tester**, mais on n'écrit pas un vrai programme dedans : dès qu'on recharge la page, tout disparaît. Pour conserver et réutiliser ton code, tu l'écris dans un **fichier**. Il y a deux façons d'exécuter un fichier `.js`, une pour chaque monde :

1. **Dans le navigateur**, en le reliant à une page HTML (ce chapitre).
2. **Avec Node.js**, en ligne de commande (Partie 6).

On apprend la première maintenant, pour ne pas rester coincé dans la console.

### Une page minimale en deux fichiers

Crée un dossier de travail, puis deux fichiers côte à côte.

**Fichier `index.html` :**

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Mon lab JavaScript</title>
  </head>
  <body>
    <h1>Page de test JavaScript</h1>

    <!-- On relie notre fichier JavaScript À LA FIN du body -->
    <script src="script.js"></script>
  </body>
</html>
```

**Fichier `script.js` (dans le même dossier) :**

```javascript
// Ce code s'exécute quand la page se charge
console.log("Le fichier script.js est bien chargé");
```

### Lancer la page

Double-clique sur `index.html` (ou ouvre-le depuis le navigateur). La page s'affiche avec son titre. Pour voir le message du script, ouvre la **console** (`F12`) : tu y verras `Le fichier script.js est bien chargé`.

> ### 🧭 Ce qui vient de se passer
> Le navigateur a lu `index.html`, a rencontré la balise `<script src="script.js">`, est allé chercher le fichier `script.js`, et l'a exécuté. **C'est le pont entre une page et ton code.**

### Pourquoi `<script>` à la fin du `<body>` ?

Le navigateur lit la page **de haut en bas**. Si ton script s'exécute **avant** que les éléments de la page existent, il ne les trouvera pas (tu auras des erreurs en Partie 3, sur le DOM). En plaçant `<script>` juste avant `</body>`, tu garantis que toute la page est déjà là quand ton code démarre.

## Très utile en pratique

Tu peux écrire plusieurs instructions dans `script.js`, elles s'exécutent dans l'ordre :

```javascript
console.log("Étape 1 : démarrage");
console.log("Étape 2 : analyse");
console.log("Étape 3 : terminé");
```

Modifie le fichier, **sauvegarde**, puis **recharge la page** (`F5`) : la console reflète tes changements. Ce cycle *écrire → sauvegarder → recharger → lire la console* est ta boucle de travail de base côté navigateur.

> ### 🧭 Navigateur vs Node.js
> Ici, on exécute le `.js` **via une page HTML dans le navigateur**. En Partie 6, on exécutera un `.js` **sans aucune page**, directement avec la commande `node script.js`. Même fichier `.js`, deux façons de l'exécuter — la fameuse question « où tourne mon code ? ».

## Exemple simple

`script.js` qui calcule et affiche, sans rien dans la page :

```javascript
let portHttp = 80;
let portHttps = 443;

console.log("Ports web standard :", portHttp, "et", portHttps);
```

Sortie dans la console après rechargement :

```text
Ports web standard : 80 et 443
```

## Application IT / cyber / OSINT

Savoir créer une page minimale `index.html` + `script.js` est indispensable pour :

- **tester** localement un comportement JavaScript que tu as observé ailleurs ;
- construire plus tard tes **petits outils web** (un inspecteur d'IOC, un lookup OSINT — ce sont les mini-projets à venir) ;
- comprendre la structure de base d'**absolument toutes** les pages web que tu analyseras : elles relient leur logique via des balises `<script>`.

Quand tu inspectes une page en OSINT, repérer **où** sont les balises `<script>` et **quels** fichiers `.js` elles chargent est l'une des premières choses à faire.

## ❌ Erreur classique

```html
<!-- ❌ script.js dans le <head>, avant que la page existe -->
<head>
  <script src="script.js"></script>  <!-- risque d'erreurs sur le DOM -->
</head>

<!-- ✅ script.js à la fin du <body> -->
<body>
  ...
  <script src="script.js"></script>
</body>
```

Autres pièges fréquents :

- **Mauvais chemin** : `<script src="script.js">` cherche le fichier **dans le même dossier**. S'il est ailleurs, rien ne se charge (regarde l'onglet *Réseau* ou *Console* des DevTools : tu verras un 404).
- **Oublier de sauvegarder** le fichier avant de recharger : tu vois encore l'ancien code.
- **Confondre** le contenu du fichier `.html` et du fichier `.js` : le JavaScript va dans `script.js`, pas entre les balises HTML.

> **Réflexe diagnostic :** ton script "ne fait rien" ? Ouvre la console. Si tu vois une erreur **404** sur `script.js`, c'est un problème de **chemin/nom de fichier**, pas de code.

## Exercices

**Guidé**
1. Crée un dossier `lab-js`.
2. Crée `index.html` et `script.js` comme ci-dessus.
3. Dans `script.js`, affiche trois lignes : `"Connexion"`, `"Authentification"`, `"Session ouverte"`.
4. Ouvre la page, ouvre la console (`F12`), vérifie les trois lignes.

**Autonome**
Modifie `script.js` pour afficher le résultat de `255 * 255` (le nombre d'adresses dans un /16 simplifié, à titre d'exemple de calcul). Sauvegarde, recharge, vérifie.

**Défi**
Déplace volontairement la balise `<script>` dans le `<head>`, recharge, et observe (on verra l'impact réel en Partie 3). Puis remets-la à la fin du `<body>`. Renomme ensuite `script.js` en `app.js` **sans** changer le `src` du HTML : observe l'erreur 404 dans la console, puis corrige le `src`.

## ✅ Tu sais maintenant…

- créer une page minimale `index.html` + `script.js` ;
- relier un fichier JavaScript à une page avec `<script src="...">` ;
- expliquer pourquoi on place `<script>` à la fin du `<body>` ;
- utiliser la boucle *écrire → sauvegarder → recharger → console* ;
- diagnostiquer un script qui ne se charge pas (erreur 404, mauvais chemin).

-----
