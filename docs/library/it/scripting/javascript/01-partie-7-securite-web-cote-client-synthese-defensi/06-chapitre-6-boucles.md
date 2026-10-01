---
title: Chapitre 6 — Boucles
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Une **boucle** répète un bloc de code. C'est essentiel pour traiter des collections : lignes de log, listes d'IP, entrées JSON.

### La boucle `for` classique

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Itération ${i}`);
}
// Itération 0, 1, 2, 3, 4
```


Trois parties entre parenthèses :

- **`let i = 0`** : initialisation (point de départ) ;
- **`i < 5`** : condition de continuation (tant qu'elle est vraie, on répète) ;
- **`i++`** : incrément (exécuté après chaque tour ; `i++` veut dire `i = i + 1`).

### La boucle `for...of` : parcourir une collection

C'est la plus lisible pour parcourir un tableau (qu'on détaillera au chapitre 10) :

```javascript
const ips = ["10.0.0.1", "8.8.8.8", "192.168.1.1"];

for (const ip of ips) {
  console.log(`IP analysée : ${ip}`);
}
```


### La boucle `while`

Répète **tant qu'**une condition est vraie. Utile quand on ne sait pas d'avance combien de tours :

```javascript
let tentatives = 0;

while (tentatives < 3) {
  console.log(`Tentative ${tentatives + 1}`);
  tentatives++;
}
```


### `break` et `continue`

```javascript
for (const ip of ["8.8.8.8", "0.0.0.0", "1.1.1.1"]) {
  if (ip === "0.0.0.0") {
    continue;   // saute CET élément, passe au suivant
  }
  if (ip === "1.1.1.1") {
    break;      // ARRÊTE complètement la boucle
  }
  console.log(`Traitée : ${ip}`);
}
// Traitée : 8.8.8.8
```


## Très utile en pratique

Compter des éléments qui remplissent une condition — un classique du parsing :

```javascript
const codes = [200, 404, 200, 500, 404, 403];
let nbErreurs = 0;

for (const code of codes) {
  if (code >= 400) {
    nbErreurs++;
  }
}

console.log(`Nombre d'erreurs : ${nbErreurs}`);   // Nombre d'erreurs : 4
```


## Exemple simple

```javascript
const ports = [22, 80, 443, 3389];

for (const port of ports) {
  const securise = port === 443 || port === 22;
  console.log(`Port ${port} → chiffré : ${securise}`);
}
```


Sortie :

```text
Port 22 → chiffré : true
Port 80 → chiffré : false
Port 443 → chiffré : true
Port 3389 → chiffré : false
```


## Application IT / cyber / OSINT

Parcourir une collection est **le geste fondamental** du scripting défensif : itérer sur les lignes d'un fichier de logs, sur une liste d'IOC, sur les entrées d'une réponse JSON d'API. Compter, filtrer, transformer pendant le parcours — c'est exactement ce que fait un parser de logs (le mini-projet de la Partie 2). En Partie 6, ces mêmes boucles s'appliqueront à des fichiers réels lus avec Node.js, et tu retrouveras la logique du cours Python.

## ❌ Erreur classique

```javascript
// ❌ Boucle infinie : on oublie de faire progresser la condition
let i = 0;
while (i < 5) {
  console.log(i);
  // on a oublié i++  → i reste 0 → boucle infinie, l'onglet se fige !
}

// ❌ Confondre for...of (valeurs) et for...in (clés/index)
const arr = ["a", "b", "c"];
for (const x of arr) console.log(x);   // a, b, c   ← les VALEURS (ce qu'on veut)
for (const x in arr) console.log(x);   // 0, 1, 2   ← les INDEX (souvent pas voulu)
```


> ### ⚠️ À ne pas confondre : `for...of` vs `for...in`
> - **`for...of`** parcourt les **valeurs** d'un tableau → c'est ce que tu veux 95 % du temps.
> - **`for...in`** parcourt les **clés/index** → réservé aux objets, piégeux sur les tableaux.
>
> Règle de débutant : sur un tableau, utilise **`for...of`**.

> **Réflexe diagnostic :** ton onglet se fige ? Tu as probablement une **boucle infinie** : vérifie que la condition finit par devenir fausse (compteur incrémenté, etc.). Ferme l'onglet pour reprendre la main.

## Exercices

**Guidé**

1. Crée `const codes = [200, 301, 404, 500, 200]`.
2. Avec `for...of`, affiche chaque code et s'il s'agit d'une erreur (`>= 400`).
3. Compte le nombre total d'erreurs et affiche-le à la fin.

**Autonome**
À partir d'un tableau d'IP `["10.0.0.1", "8.8.8.8", "192.168.0.5", "1.1.1.1"]`, parcours-le et affiche pour chacune `"privée"` ou `"publique"` (réutilise ta logique du chapitre 5).

**Défi**
Parcours les nombres de 1 à 50. Pour chaque multiple de 5 (`n % 5 === 0`), affiche le nombre. Utilise `continue` pour sauter les autres. Compte combien tu en as affichés et vérifie le total.

## ✅ Tu sais maintenant…

- écrire une boucle `for` classique (init ; condition ; incrément) ;
- parcourir une collection avec `for...of` ;
- utiliser `while` quand le nombre de tours est inconnu ;
- contrôler le flux avec `break` et `continue` ;
- éviter les boucles infinies et le piège `for...in` sur un tableau.

-----

## 🧩 Mini-projet — Classificateur de codes HTTP (chapitres 1 à 6)

Rassemble tout ce que tu as appris dans la Partie 1. Crée un fichier `classificateur.js` relié à une page `index.html` (chapitre 2), ou teste directement en console.

**Objectif :** à partir d'une liste de codes HTTP, afficher pour chacun sa catégorie, et un récapitulatif du nombre d'erreurs.

```javascript
// classificateur.js
const codes = [200, 301, 404, 403, 500, 200, 503, 204];

let nbSucces = 0;
let nbRedirections = 0;
let nbErreursClient = 0;
let nbErreursServeur = 0;

for (const code of codes) {
  let categorie;

  if (code >= 200 && code < 300) {
    categorie = "Succès";
    nbSucces++;
  } else if (code >= 300 && code < 400) {
    categorie = "Redirection";
    nbRedirections++;
  } else if (code >= 400 && code < 500) {
    categorie = "Erreur client";
    nbErreursClient++;
  } else if (code >= 500 && code < 600) {
    categorie = "Erreur serveur";
    nbErreursServeur++;
  } else {
    categorie = "Inconnu";
  }

  console.log(`${code} → ${categorie}`);
}

console.log("---");
console.log(`Succès : ${nbSucces}`);
console.log(`Redirections : ${nbRedirections}`);
console.log(`Erreurs client : ${nbErreursClient}`);
console.log(`Erreurs serveur : ${nbErreursServeur}`);

const totalErreurs = nbErreursClient + nbErreursServeur;
console.log(`⚠️ Total erreurs : ${totalErreurs}`);
```


Sortie attendue :

```text
200 → Succès
301 → Redirection
404 → Erreur client
403 → Erreur client
500 → Erreur serveur
200 → Succès
503 → Erreur serveur
204 → Succès
---
Succès : 3
Redirections : 1
Erreurs client : 2
Erreurs serveur : 2
⚠️ Total erreurs : 4
```


**Pour aller plus loin (optionnel) :** ajoute un code « bizarre » comme `999` et vérifie qu'il tombe dans `"Inconnu"`. Change la liste et observe le récapitulatif s'adapter.

Ce mini-projet mobilise : variables (`const`/`let`), types, comparaisons strictes (`===`, `>=`), conditions (`if/else if/else`), boucle (`for...of`), compteurs, et template strings. C'est exactement la mécanique d'un **premier outil de triage**.

-----

## ✅ CHECKPOINT 1 — Tu maîtrises le langage de base

Avant de passer à la Partie 2, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer la différence HTML / CSS / JavaScript et navigateur / Node.js ;
- [ ] ouvrir la console et exécuter du JavaScript ;
- [ ] créer une page minimale `index.html` + `script.js` reliés ;
- [ ] déclarer des variables avec `const`/`let` et nommer les types de base ;
- [ ] écrire une template string ;
- [ ] utiliser `===` plutôt que `==` et expliquer pourquoi ;
- [ ] citer les valeurs falsy ;
- [ ] écrire un `if/else if/else`, un ternaire, un `switch` ;
- [ ] écrire une boucle `for...of` et compter des éléments sous condition ;
- [ ] réaliser le mini-projet classificateur de codes HTTP.

Si un point te résiste, reviens au chapitre concerné avant de continuer. La Partie 2 (fonctions, tableaux, objets, JSON) s'appuie entièrement sur ces fondations.

-----

*Fin de la Partie 1. La Partie 2 — « Structurer les données et le code » sera rédigée après ta validation de ce premier bloc.*

-----
