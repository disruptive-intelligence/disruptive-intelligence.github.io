---
title: Chapitre 13 — Erreurs, exceptions et débogage
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Une **erreur** (ou exception) interrompt l'exécution. Apprendre à les **lire** est une compétence centrale : une erreur n'est pas un échec, c'est une information.

### Les types d'erreurs courants

| Type | Cause typique |
| --- | --- |
| **`SyntaxError`** | Code mal écrit (parenthèse manquante, JSON invalide). |
| **`ReferenceError`** | Utilisation d'une variable qui n'existe pas. |
| **`TypeError`** | Opération sur un type qui ne le permet pas (ex. appeler une méthode sur `undefined`). |

```javascript
console.log(inconnu);        // ReferenceError: inconnu is not defined

const x = null;
console.log(x.length);       // TypeError: Cannot read properties of null
```


### Lire une erreur (la stack trace)

Une erreur affiche un **message** et une **pile d'appels** (stack trace) : la liste des fonctions traversées, la plus récente en haut. Lis toujours :

1. **le type** d'erreur (TypeError, ReferenceError…) ;
2. **le message** (que s'est-il passé ?) ;
3. **la ligne** indiquée (où ?).

> ### 🧭 Réflexe diagnostic : méthode de lecture d'une erreur
> 1. **Type + message** te disent *quoi*. `Cannot read properties of undefined (reading 'x')` = tu accèdes à `.x` sur quelque chose qui vaut `undefined`.
> 2. **La première ligne de la stack** te dit *où*, dans ton code.
> 3. **Reproduis et isole** : ajoute un `console.log` juste avant la ligne fautive pour voir la vraie valeur.

### `try/catch` : gérer une erreur sans planter

```javascript
try {
  const obj = JSON.parse("{ cassé }");   // va échouer
  console.log(obj.ip);
} catch (erreur) {
  console.log("JSON invalide, on continue proprement :", erreur.message);
}

console.log("Le programme continue");   // s'exécute quand même
```


Structure : on **tente** (`try`) une opération risquée ; si elle échoue, on **attrape** l'erreur (`catch`) au lieu de planter. Optionnellement, `finally` s'exécute toujours, succès ou échec.

### Déclencher sa propre erreur avec `throw`

```javascript
function analyserCode(code) {
  if (typeof code !== "number") {
    throw new Error("Le code doit être un nombre");
  }
  return code >= 400 ? "erreur" : "ok";
}

try {
  analyserCode("404");   // string au lieu de number
} catch (e) {
  console.log("Problème :", e.message);   // Problème : Le code doit être un nombre
}
```


## Très utile en pratique

Le `try/catch` est **indispensable** autour de tout ce qui peut échouer : parsing JSON, requêtes réseau (Partie 5), lecture de fichiers (Partie 6).

```javascript
function parserSafe(texte) {
  try {
    return JSON.parse(texte);
  } catch {
    return null;   // au lieu de planter, on renvoie null
  }
}

console.log(parserSafe('{"ok": true}'));   // { ok: true }
console.log(parserSafe("cassé"));          // null
```


## Exemple simple

```javascript
const entrees = ['{"ip":"8.8.8.8"}', 'cassé', '{"ip":"1.1.1.1"}'];

for (const entree of entrees) {
  try {
    const obj = JSON.parse(entree);
    console.log("OK :", obj.ip);
  } catch {
    console.log("Ignoré (JSON invalide) :", entree);
  }
}
```


Sortie :

```text
OK : 8.8.8.8
Ignoré (JSON invalide) : cassé
OK : 1.1.1.1
```


Une seule entrée cassée n'arrête plus tout le traitement — crucial pour parser un fichier réel où une ligne peut être corrompue.

## Application IT / cyber / OSINT

En analyse défensive, tu traites des données **imparfaites** : logs avec des lignes corrompues, réponses d'API qui échouent, fichiers partiels. Sans gestion d'erreurs, ton script s'arrête à la première anomalie et tu perds tout le reste. Avec `try/catch`, tu **isoles** les échecs et tu continues : tu parses les 9 999 lignes valides en ignorant proprement la ligne cassée. C'est la différence entre un script fragile et un outil robuste. La gestion des erreurs réseau (`fetch`) — risque n° 11 de la Boîte à risques — repose sur ces réflexes.

## ❌ Erreur classique

```javascript
// ❌ Ne pas gérer une opération risquée → tout s'arrête
const lignes = ['{"a":1}', 'cassé', '{"b":2}'];
for (const l of lignes) {
  const obj = JSON.parse(l);   // plante sur "cassé", la boucle s'arrête !
  console.log(obj);
}

// ✅ CORRECT : try/catch dans la boucle
for (const l of lignes) {
  try {
    console.log(JSON.parse(l));
  } catch {
    console.log("ligne ignorée");
  }
}

// ❌ Attraper l'erreur et l'ignorer en silence (catch vide sans log)
// → tu masques des problèmes réels. Logue au moins quelque chose.
```


> **Réflexe diagnostic :** ne crains pas les erreurs rouges dans la console — **lis-les**. 90 % du débogage, c'est lire le type, le message et la ligne, puis ajouter un `console.log` au bon endroit.

## Exercices

**Guidé (lecture d'erreurs)**
Pour chaque ligne, **prédis** le type d'erreur avant d'exécuter, puis vérifie :

```javascript
console.log(maVariable);        // ?
const o = null; o.x;            // ?
JSON.parse("{ pas du json }");  // ?
```


**Autonome**
Écris une fonction `diviser(a, b)` qui `throw` une erreur si `b === 0`, sinon renvoie `a / b`. Appelle-la dans un `try/catch` avec `b = 0` et affiche le message d'erreur proprement.

**Défi**
Tu reçois un tableau de chaînes censées être du JSON, mais certaines sont cassées. Écris une boucle qui parse chaque entrée avec `try/catch`, accumule les objets valides dans un tableau `valides` et compte les invalides. Affiche : `X entrées valides, Y ignorées`. C'est exactement le squelette d'un parser de logs robuste.

## ✅ Tu sais maintenant…

- reconnaître `SyntaxError`, `ReferenceError`, `TypeError` ;
- lire une erreur (type, message, ligne) et appliquer une méthode de diagnostic ;
- gérer une opération risquée avec `try/catch/finally` ;
- déclencher une erreur avec `throw new Error(...)` ;
- écrire du code robuste qui continue malgré une donnée cassée.

-----

## 🧩 Mini-projet — Parser de logs et extracteur d'IOC (chapitres 7 à 13)

Rassemble toute la Partie 2. Crée `parser.js` (à tester en console ou dans une page).

**Objectif :** à partir d'un bloc de logs bruts, extraire les IP, compter les échecs de connexion par IP, repérer les IP qui dépassent un seuil (détection de brute-force simple), et produire un rapport JSON.

```javascript
// parser.js

// Des logs bruts (simulés). En Partie 6, on les lira depuis un vrai fichier.
const logsBruts = `
2024-01-15 10:00:01 203.0.113.5 login FAILED
2024-01-15 10:00:02 203.0.113.5 login FAILED
2024-01-15 10:00:03 8.8.8.8 login OK
2024-01-15 10:00:04 203.0.113.5 login FAILED
2024-01-15 10:00:05 ligne corrompue ???
2024-01-15 10:00:06 1.1.1.1 login FAILED
2024-01-15 10:00:07 203.0.113.5 login FAILED
`;

const SEUIL = 3;

// 1. Découper en lignes, enlever les lignes vides
const lignes = logsBruts
  .split("\n")
  .map((l) => l.trim())
  .filter((l) => l.length > 0);

// 2. Parser chaque ligne en objet, en ignorant les lignes invalides
const evenements = [];
for (const ligne of lignes) {
  try {
    const champs = ligne.split(" ");
    // champs : [date, heure, ip, action, statut]
    const ip = champs[2];
    const action = champs[3];
    const statut = champs[4];

    // Validation simple : l'IP doit ressembler à une IPv4
    if (!/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
      throw new Error("IP invalide");
    }

    evenements.push({ ip, action, statut });
  } catch {
    console.log(`⚠️ Ligne ignorée : ${ligne}`);
  }
}

// 3. Garder seulement les échecs de login
const echecs = evenements.filter(
  (e) => e.action === "login" && e.statut === "FAILED"
);

// 4. Compter les échecs par IP
const compteur = {};
for (const e of echecs) {
  compteur[e.ip] = (compteur[e.ip] || 0) + 1;
}

// 5. Repérer les IP au-dessus du seuil
const suspectes = Object.entries(compteur)
  .filter(([ip, n]) => n >= SEUIL)
  .map(([ip, n]) => ({ ip, echecs: n }));

// 6. Produire un rapport JSON
const rapport = {
  total_evenements: evenements.length,
  total_echecs: echecs.length,
  ip_suspectes: suspectes
};

console.log("--- RAPPORT ---");
console.log(JSON.stringify(rapport, null, 2));
```


Sortie attendue :

```text
⚠️ Ligne ignorée : 2024-01-15 10:00:05 ligne corrompue ???
--- RAPPORT ---
{
  "total_evenements": 6,
  "total_echecs": 4,
  "ip_suspectes": [
    {
      "ip": "203.0.113.5",
      "echecs": 4
    }
  ]
}
```


Ce mini-projet mobilise **toute la Partie 2** : fonctions, chaînes (`split`, `trim`), regex (validation IP), tableaux (`map`, `filter`), objets (compteur, `Object.entries`), JSON (`stringify`), et gestion d'erreurs (`try/catch` pour la ligne corrompue). C'est un vrai **détecteur de brute-force** miniature, et le pendant JavaScript du parser de logs du cours Python.

**Pour aller plus loin :** ajoute des lignes pour `1.1.1.1` afin qu'elle dépasse aussi le seuil, et vérifie qu'elle apparaît dans `ip_suspectes`.

-----

## ✅ CHECKPOINT 2 — Tu sais structurer données et code

Avant la Partie 3, assure-toi de pouvoir, **sans regarder** :

- [ ] écrire une fonction (classique et fléchée) avec `return` ;
- [ ] manipuler des chaînes (`trim`, `toLowerCase`, `split`, `includes`…) ;
- [ ] parser une URL avec `new URL(...)` ;
- [ ] extraire des IOC d'un texte avec une regex simple et le drapeau `g` ;
- [ ] filtrer/transformer un tableau avec `filter`, `map`, `find` ;
- [ ] modéliser des données avec des objets et des tableaux d'objets ;
- [ ] lire et produire du JSON avec `JSON.parse` / `JSON.stringify` ;
- [ ] gérer une erreur avec `try/catch` et écrire du code robuste ;
- [ ] réaliser le mini-projet parser de logs.

Tu disposes maintenant de **tout le langage**. La Partie 3 quitte la pure logique pour faire vivre une page web : le DOM et les événements.


-----
