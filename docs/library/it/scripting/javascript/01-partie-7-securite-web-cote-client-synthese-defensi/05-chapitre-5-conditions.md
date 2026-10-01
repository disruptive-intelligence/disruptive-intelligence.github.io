---
title: Chapitre 5 — Conditions
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Une **condition** fait prendre une décision au code : exécuter un bloc **seulement si** quelque chose est vrai.

```javascript
const code = 404;

if (code === 200) {
  console.log("Succès");
} else if (code >= 400 && code < 500) {
  console.log("Erreur côté client");
} else if (code >= 500) {
  console.log("Erreur côté serveur");
} else {
  console.log("Autre code");
}
// Affiche : Erreur côté client
```


Structure :

- **`if (condition) { ... }`** : exécute le bloc si la condition est vraie.
- **`else if (autre) { ... }`** : testé seulement si les précédents sont faux.
- **`else { ... }`** : exécuté si rien d'autre n'a matché.

### Le ternaire : un `if/else` compact

Pour choisir entre **deux** valeurs, le ternaire est pratique :

```javascript
const code = 200;
const message = code === 200 ? "OK" : "Pas OK";
console.log(message);   // OK
```


Lecture : `condition ? valeurSiVrai : valeurSiFaux`.

### `switch` : tester une valeur contre plusieurs cas

Quand on compare **une même variable** à de nombreuses valeurs, `switch` est plus lisible :

```javascript
const methode = "POST";

switch (methode) {
  case "GET":
    console.log("Lecture de données");
    break;
  case "POST":
    console.log("Envoi de données");
    break;
  case "DELETE":
    console.log("Suppression");
    break;
  default:
    console.log("Méthode non gérée");
}
// Affiche : Envoi de données
```


> **N'oublie pas `break`** à la fin de chaque `case`, sinon l'exécution « déborde » sur le cas suivant (comportement rarement voulu).

## Très utile en pratique

Tester proprement `null` / `undefined` (rappel du chapitre 3) :

```javascript
let donnee;   // undefined

if (donnee === undefined) {
  console.log("Aucune donnée reçue");
}

// Astuce courante : tester l'absence de valeur "utile"
if (!donnee) {
  console.log("Donnée vide, nulle ou absente");
}
```


## Exemple simple

```javascript
const tentatives = 7;
const seuil = 5;

if (tentatives > seuil) {
  console.log(`⚠️ Alerte : ${tentatives} tentatives (seuil : ${seuil})`);
} else {
  console.log("Activité normale");
}
// ⚠️ Alerte : 7 tentatives (seuil : 5)
```


## Application IT / cyber / OSINT

Toute la logique de **triage** d'un SOC est faite de conditions. Classer un code HTTP, décider si une IP est privée ou publique, déclencher une alerte au-delà d'un seuil, router un événement selon sa méthode HTTP : ce sont des `if/else` et des `switch`. Plus tu écris des conditions claires, plus ta logique de détection est lisible et maintenable.

## ❌ Erreur classique

```javascript
// ❌ Un seul = (affectation) au lieu de === (comparaison)
let actif = false;
if (actif = true) {       // ⚠️ assigne true, puis teste true → toujours vrai !
  console.log("Toujours exécuté, bug silencieux");
}

// ✅ CORRECT : comparaison stricte
if (actif === true) { ... }

// ❌ Oublier le break dans un switch
switch (x) {
  case 1:
    console.log("un");   // sans break, "deux" s'affiche aussi
  case 2:
    console.log("deux");
}
```


> **Réflexe diagnostic :** une condition « toujours vraie » sans raison ? Vérifie que tu as bien `===` et non un seul `=` (qui est une **affectation**, pas une comparaison).

## Exercices

**Guidé**

1. Crée `const code = 503`.
2. Avec `if / else if / else`, affiche `"client"` pour 4xx, `"serveur"` pour 5xx, `"autre"` sinon.
3. Vérifie avec `code = 404` puis `code = 200`.

**Autonome**
Écris un `switch` sur une variable `protocole` (`"HTTP"`, `"HTTPS"`, `"SSH"`, `"RDP"`) qui affiche le port standard correspondant (80, 443, 22, 3389), et un message par défaut pour les autres.

**Défi**
Écris une fonction de classification d'IP **sans fonction encore** (juste avec des conditions, on fera les fonctions au chapitre suivant) : à partir d'une `const ip = "192.168.1.10"`, affiche `"privée"` si elle commence par `"192.168."`, `"10."`, ou `"172.16."`, sinon `"publique"`. *(Indice : `ip.startsWith("192.168.")`.)*

## ✅ Tu sais maintenant…

- écrire des `if` / `else if` / `else` ;
- utiliser le ternaire pour choisir entre deux valeurs ;
- utiliser `switch` avec `break` et `default` ;
- tester l'absence de valeur (`undefined`, falsy) ;
- éviter le piège du `=` (affectation) au lieu de `===` (comparaison).

-----
