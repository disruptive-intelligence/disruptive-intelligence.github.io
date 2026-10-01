---
title: Chapitre 16 — Événements
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Jusqu'ici, ton code s'exécutait une fois, au chargement. Le web est **interactif** : on veut réagir aux **événements** (clic, frappe, envoi de formulaire). C'est le cœur du modèle JavaScript navigateur.

### `addEventListener`

On attache une fonction à un élément, qui s'exécutera quand l'événement se produit.

```html
<button id="lancer">Lancer l'analyse</button>
<script src="script.js"></script>
```


```javascript
const bouton = document.querySelector("#lancer");

bouton.addEventListener("click", () => {
  console.log("Bouton cliqué !");
});
```


Structure : `element.addEventListener("nom_evenement", fonction)`. La fonction (souvent fléchée) s'appelle un **callback** : elle est exécutée « plus tard », quand l'événement arrive.

### Événements courants

| Événement | Déclenché quand… |
| --- | --- |
| `click` | on clique sur l'élément |
| `input` | le contenu d'un champ change (à chaque frappe) |
| `submit` | un formulaire est envoyé |
| `keydown` | une touche est pressée |
| `change` | un champ perd le focus après modification |

### L'objet `event`

Le callback reçoit un objet `event` décrivant ce qui s'est passé :

```javascript
const champ = document.querySelector("#recherche");

champ.addEventListener("input", (event) => {
  console.log("Valeur actuelle :", event.target.value);
});
```


`event.target` est l'élément concerné ; `.value` est le contenu d'un champ.

## Très utile en pratique

Réagir à un clic en modifiant la page (en sécurité avec `textContent`) :

```html
<input id="ip" placeholder="Entrez une IP">
<button id="verifier">Vérifier</button>
<p id="resultat"></p>
<script src="script.js"></script>
```


```javascript
const champ = document.querySelector("#ip");
const bouton = document.querySelector("#verifier");
const resultat = document.querySelector("#resultat");

function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

bouton.addEventListener("click", () => {
  const ip = champ.value.trim();
  const type = estIpPrivee(ip) ? "privée" : "publique";
  resultat.textContent = `${ip} → ${type}`;   // ✅ textContent
});
```


## Exemple simple

```javascript
const bouton = document.querySelector("#compteur");
let clics = 0;

bouton.addEventListener("click", () => {
  clics++;
  console.log(`Clics : ${clics}`);
});
```


## Application IT / cyber / OSINT

Les événements rendent tes **petits outils web** interactifs : un champ où coller du texte, un bouton qui lance l'extraction d'IOC, un résultat qui s'affiche. Les mini-projets « inspecteur d'IOC » et « lookup OSINT » (Parties 3 et 5) reposent dessus. Comprendre les événements, c'est aussi comprendre comment une page réagit aux actions — utile pour analyser le comportement d'une application web. En sécurité, c'est souvent sur un `submit` ou un `input` que se branchent validations (et failles).

> ### 🔍 Lecture de code inconnu
> Repérer les `addEventListener` dans un script inconnu te dit **à quelles actions le code réagit** (clics, envois de formulaire) et **ce qu'il déclenche** (souvent un appel réseau, chapitre 22).

## ❌ Erreur classique

```javascript
// ❌ Appeler la fonction au lieu de la passer
bouton.addEventListener("click", maFonction());   // ❌ () exécute TOUT DE SUITE
bouton.addEventListener("click", maFonction);      // ✅ on passe la fonction
bouton.addEventListener("click", () => maFonction()); // ✅ ou via une flèche

// ❌ Attacher l'événement avant que l'élément existe (script trop tôt)
// → bouton vaut null → addEventListener plante. Place le script en fin de body.

// ❌ Oublier .value et manipuler le champ lui-même
const v = champ;          // l'élément
const v2 = champ.value;   // ✅ le contenu texte du champ
```


> **Réflexe diagnostic :** ton bouton « ne réagit pas » ? Vérifie : le sélecteur est-il bon (pas `null`) ? Le script est-il bien à la fin du `<body>` ? As-tu passé la **fonction** (sans `()`) et non son résultat ?

## Exercices

**Guidé**

1. Crée un bouton et un `<p id="msg">`.
2. Au clic, mets `"Cliqué !"` dans le `<p>` avec `textContent`.
3. Ajoute un compteur de clics affiché dans le `<p>`.

**Autonome**
Crée un champ de saisie et un `<p>`. À chaque frappe (`input`), affiche en direct le nombre de caractères saisis dans le `<p>`.

**Défi**
Crée un mini-vérificateur : un champ pour une URL, un bouton « Extraire le domaine ». Au clic, utilise `new URL(champ.value)` (dans un `try/catch` car l'URL peut être invalide) et affiche le domaine avec `textContent`, ou un message d'erreur si l'URL est invalide.

## ✅ Tu sais maintenant…

- attacher un comportement avec `addEventListener("event", callback)` ;
- reconnaître `click`, `input`, `submit`, `keydown`, `change` ;
- lire l'objet `event` et `event.target.value` ;
- récupérer le contenu d'un champ avec `.value` ;
- passer une fonction sans l'exécuter (pas de `()`) ;
- diagnostiquer un événement qui ne se déclenche pas.

-----
