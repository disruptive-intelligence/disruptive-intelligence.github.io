---
title: Chapitre 21 — Promesses
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 21
chapters: 35
---

## Le minimum à savoir

Gérer l'asynchrone uniquement avec des callbacks devient vite illisible (callbacks imbriqués). JavaScript moderne utilise les **promesses** (*Promises*) : un objet qui représente un **résultat futur**.

Une promesse a trois états : **en attente** (pending), **tenue** (fulfilled, succès), ou **rompue** (rejected, échec).

### `.then` et `.catch`

```javascript
// uneFonctionAsync() renvoie une promesse
uneFonctionAsync()
  .then((resultat) => {
    console.log("Succès :", resultat);
  })
  .catch((erreur) => {
    console.log("Échec :", erreur);
  });
```

- **`.then(callback)`** : exécuté quand la promesse réussit, avec le résultat.
- **`.catch(callback)`** : exécuté si elle échoue, avec l'erreur.

### Illustration avec une promesse simple

```javascript
// Promise.resolve crée une promesse déjà réussie (pour l'exemple)
Promise.resolve("données reçues")
  .then((data) => console.log(data));   // "données reçues"

// Promise.reject crée une promesse en échec
Promise.reject("erreur réseau")
  .catch((err) => console.log("Attrapé :", err));   // "Attrapé : erreur réseau"
```

### Enchaîner les `.then`

Chaque `.then` peut renvoyer une valeur passée au `.then` suivant :

```javascript
Promise.resolve(5)
  .then((n) => n * 2)        // 10
  .then((n) => n + 1)        // 11
  .then((n) => console.log(n)); // 11
```

## Très utile en pratique

Les promesses sont ce que renvoie **`fetch`** (chapitre suivant). Comprendre `.then`/`.catch` te permet de lire et écrire du code réseau. Mais la syntaxe la plus agréable viendra avec `async/await` (chapitre 23), qui n'est qu'une façon plus lisible de manipuler ces mêmes promesses.

## Exemple simple

```javascript
function verifierIp(ip) {
  // Simule une vérification asynchrone qui réussit
  return Promise.resolve({ ip, malveillante: ip === "203.0.113.5" });
}

verifierIp("203.0.113.5")
  .then((res) => {
    console.log(`${res.ip} → malveillante : ${res.malveillante}`);
  });
// 203.0.113.5 → malveillante : true
```

## Application IT / cyber / OSINT

Toutes les APIs modernes s'interrogent via des promesses. Quand tu liras du code qui interroge une API de réputation, tu verras des `.then`/`.catch`. Savoir les lire — même si tu préfères écrire en `async/await` — est indispensable pour comprendre le code existant et les exemples de documentation.

## ❌ Erreur classique

```javascript
// ❌ Oublier le .catch : une erreur passe inaperçue
fetch("https://api.exemple.test/data")
  .then((r) => r.json());
  // si ça échoue, erreur silencieuse non gérée

// ✅ Toujours un .catch
fetch("https://api.exemple.test/data")
  .then((r) => r.json())
  .then((data) => console.log(data))
  .catch((err) => console.log("Erreur :", err.message));

// ❌ Oublier de renvoyer (return) dans un .then qu'on veut chaîner
Promise.resolve(5)
  .then((n) => { n * 2; })     // ne renvoie rien → le then suivant reçoit undefined
  .then((n) => console.log(n)); // undefined
```

> **Réflexe diagnostic :** une chaîne de `.then` reçoit `undefined` ? Un `.then` précédent a oublié de `return` sa valeur.

## Exercices

**Guidé**
1. Crée une promesse réussie avec `Promise.resolve("ok")` et affiche sa valeur dans un `.then`.
2. Crée une promesse en échec avec `Promise.reject("ko")` et attrape-la dans un `.catch`.

**Autonome**
Écris une fonction `chercherScore(ip)` qui renvoie `Promise.resolve(85)`. Appelle-la, et dans un `.then`, affiche `"IP à risque"` si le score `>= 80`, sinon `"IP sûre"`.

**Défi**
Enchaîne trois `.then` : le premier renvoie une IP, le deuxième la transforme en objet `{ip}`, le troisième affiche une phrase. Ajoute un `.catch` final. Observe comment la valeur circule de `.then` en `.then`.

## ✅ Tu sais maintenant…

- comprendre qu'une promesse représente un résultat futur ;
- connaître ses trois états (pending, fulfilled, rejected) ;
- gérer le succès avec `.then` et l'échec avec `.catch` ;
- enchaîner des `.then` en renvoyant des valeurs ;
- toujours prévoir un `.catch`.

-----
