---
title: Chapitre 23 — async / await
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

`async/await` est une syntaxe plus **lisible** pour écrire de l'asynchrone. Sous le capot, ce sont toujours des promesses (chapitre 21), mais le code se lit presque comme du synchrone.

### Transformer `.then` en `await`

```javascript
// Avec .then (chapitre 22)
fetch("https://api.ipify.org?format=json")
  .then((r) => r.json())
  .then((data) => console.log(data.ip));

// Avec async/await : plus linéaire
async function afficherIp() {
  const reponse = await fetch("https://api.ipify.org?format=json");
  const data = await reponse.json();
  console.log(data.ip);
}

afficherIp();
```


Règles :

- **`await`** met en pause la fonction jusqu'à ce que la promesse soit résolue, et renvoie directement le résultat.
- **`await` ne peut s'utiliser que dans une fonction `async`.**

### Gérer les erreurs avec `try/catch`

Avec `async/await`, on revient au `try/catch` classique (chapitre 13), plus naturel que `.catch` :

```javascript
async function recupererIp() {
  try {
    const reponse = await fetch("https://api.ipify.org?format=json");
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);
    }
    const data = await reponse.json();
    return data.ip;
  } catch (erreur) {
    console.log("Erreur :", erreur.message);
    return null;
  }
}
```


## Très utile en pratique

`async/await` rend le code réseau **séquentiel et lisible**, surtout quand plusieurs étapes s'enchaînent :

```javascript
async function enrichirIp(ip) {
  try {
    const r = await fetch(`https://api.exemple.test/ip/${ip}`);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const data = await r.json();
    return { ip, score: data.score, pays: data.pays };
  } catch (e) {
    return { ip, erreur: e.message };
  }
}
```


## Exemple simple

```javascript
async function analyser() {
  const ip = "8.8.8.8";
  console.log(`Analyse de ${ip}...`);
  // (ici un await fetch réel)
  console.log("Terminé");
}

analyser();
```


## Application IT / cyber / OSINT

`async/await` est la façon recommandée d'écrire tes outils d'enrichissement d'IOC : interroger une API, attendre la réponse, la traiter, passer à la suivante — le tout lisible de haut en bas. Que ce soit côté navigateur (lookup OSINT) ou côté Node.js (scripts d'enrichissement en lot, Partie 6), c'est la syntaxe que tu utiliseras le plus. Combinée à `try/catch`, elle donne des outils robustes face aux pannes réseau.

> ### 🔍 Lecture de code inconnu
> Le couple `async`/`await` autour d'un `fetch` est le motif le plus courant d'appel réseau moderne. Le repérer te montre instantanément où le code communique avec un serveur.

## ❌ Erreur classique

```javascript
// ❌ Oublier await : on récupère la promesse, pas le résultat
async function bug() {
  const data = fetch(url);   // data est une PROMESSE, pas la réponse
  console.log(data);         // [object Promise]
}

// ✅ Avec await
async function ok() {
  const reponse = await fetch(url);
  const data = await reponse.json();   // await aussi ici !
}

// ❌ Utiliser await hors d'une fonction async
// const data = await fetch(url);   // SyntaxError (au niveau racine classique)

// ❌ Oublier le try/catch → erreur réseau non gérée
```


> **Réflexe diagnostic :** ta variable affiche `[object Promise]` ? Tu as oublié un `await`. Et souviens-toi : `reponse.json()` aussi demande un `await`.

## Exercices

**Guidé**

1. Réécris la fonction `recupererIp` du chapitre 22 en `async/await`.
2. Entoure-la d'un `try/catch`.
3. Appelle-la et affiche le résultat.

**Autonome**
Écris une fonction `async lookup(ip)` qui interroge `https://api.ipify.org?format=json` (ou une API au choix), vérifie le statut, et renvoie les données. Branche-la sur un bouton de page et affiche le résultat en `textContent`.

**Défi**
Écris une fonction `async enrichirPlusieurs(ips)` qui prend un tableau d'IP, les interroge **une par une** avec `await` dans une boucle `for...of`, accumule les résultats dans un tableau, et gère les erreurs individuellement (une IP qui échoue n'arrête pas les autres). Affiche le tableau final en JSON.

## ✅ Tu sais maintenant…

- écrire de l'asynchrone lisible avec `async`/`await` ;
- utiliser `await` (uniquement dans une fonction `async`) ;
- gérer les erreurs avec `try/catch` ;
- te souvenir que `reponse.json()` demande aussi un `await` ;
- reconnaître le motif `async fetch` dans du code.

-----
