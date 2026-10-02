---
title: Chapitre 10 — Tableaux et méthodes utiles
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Un **tableau** (array) est une collection ordonnée de valeurs.

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"];

console.log(ips[0]);        // "8.8.8.8"  (premier, index 0)
console.log(ips.length);    // 3
console.log(ips[ips.length - 1]); // "192.168.1.1" (dernier)
```


### Ajouter et retirer

```javascript
const liste = [];
liste.push("a");       // ajoute à la fin → ["a"]
liste.push("b");       // ["a", "b"]
liste.pop();           // retire le dernier → ["a"]
console.log(liste);    // ["a"]
```


### Parcourir (rappel)

```javascript
const ports = [22, 80, 443];
for (const port of ports) {
  console.log(port);
}
```


## Très utile en pratique : `map`, `filter`, `find`

Ces trois méthodes transforment un tableau sans boucle explicite. **Elles sont au cœur du JavaScript moderne.** Chacune prend une fonction (souvent fléchée) appliquée à chaque élément.

### `filter` — garder seulement certains éléments

```javascript
const codes = [200, 404, 301, 500, 403];

const erreurs = codes.filter((code) => code >= 400);
console.log(erreurs);   // [404, 500, 403]
```


Lecture : « garde les éléments pour lesquels la fonction renvoie `true` ».

### `map` — transformer chaque élément

```javascript
const ips = ["8.8.8.8", "1.1.1.1"];

const enMajuscules = ips.map((ip) => `IP: ${ip}`);
console.log(enMajuscules);   // ["IP: 8.8.8.8", "IP: 1.1.1.1"]
```


Lecture : « renvoie un nouveau tableau où chaque élément est transformé ».

### `find` — trouver le premier qui correspond

```javascript
const codes = [200, 404, 500];

const premiereErreur = codes.find((code) => code >= 400);
console.log(premiereErreur);   // 404  (le premier, pas tous)
```


`find` renvoie l'**élément** (ou `undefined` si aucun). À ne pas confondre avec `filter` qui renvoie un **tableau**.

### `includes` — l'élément est-il présent ?

```javascript
const ipsBloquees = ["8.8.8.8", "1.1.1.1"];
console.log(ipsBloquees.includes("8.8.8.8"));   // true
console.log(ipsBloquees.includes("9.9.9.9"));   // false
```


### Enchaîner les méthodes

La vraie puissance vient de l'enchaînement :

```javascript
const codes = [200, 404, 301, 500, 403, 502];

const messagesErreurs = codes
  .filter((c) => c >= 400)        // garde les erreurs → [404, 500, 403, 502]
  .map((c) => `Erreur ${c}`);     // transforme → ["Erreur 404", ...]

console.log(messagesErreurs);
// ["Erreur 404", "Erreur 500", "Erreur 403", "Erreur 502"]
```


### Dédoublonner avec `Set`

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "8.8.8.8", "8.8.8.8"];
const uniques = [...new Set(ips)];
console.log(uniques);   // ["8.8.8.8", "1.1.1.1"]
```


## Exemple simple

```javascript
const ips = ["10.0.0.1", "8.8.8.8", "192.168.1.5", "1.1.1.1"];

function estIpPrivee(ip) {
  return ip.startsWith("10.") || ip.startsWith("192.168.") || ip.startsWith("172.16.");
}

const publiques = ips.filter((ip) => !estIpPrivee(ip));
console.log("IP publiques :", publiques);   // ["8.8.8.8", "1.1.1.1"]
```


## Application IT / cyber / OSINT

`filter`, `map`, `find` et `Set` sont **exactement** les outils du traitement d'IOC. Filtrer les IP publiques d'une liste, transformer une liste d'IP en lignes de règles de blocage, dédoublonner des domaines, trouver la première entrée suspecte : tout cela tient en quelques lignes lisibles. C'est le pendant JavaScript des list comprehensions de Python. Le mini-projet parser de logs en fin de partie repose entièrement sur ces méthodes.

## ❌ Erreur classique

```javascript
// ❌ Oublier de récupérer le résultat (map/filter renvoient un NOUVEAU tableau)
const codes = [200, 404];
codes.filter((c) => c >= 400);    // résultat jeté !
console.log(codes);               // [200, 404]  ← inchangé

// ✅ CORRECT
const erreurs = codes.filter((c) => c >= 400);

// ❌ Confondre find (un élément) et filter (un tableau)
const codes2 = [200, 404, 500];
console.log(codes2.find((c) => c >= 400));    // 404  (un seul)
console.log(codes2.filter((c) => c >= 400));  // [404, 500] (tableau)

// ❌ Accéder à un index qui n'existe pas
const arr = ["a"];
console.log(arr[5]);   // undefined (pas d'erreur, mais piège silencieux)
```


> ### ⚠️ À ne pas confondre : `find` vs `filter`
> - **`find`** renvoie **le premier élément** correspondant (ou `undefined`).
> - **`filter`** renvoie **un tableau** de tous les éléments correspondants (éventuellement vide).

> **Réflexe diagnostic :** ton `map`/`filter` « ne fait rien » ? Tu as oublié de **récupérer** le tableau renvoyé. Ces méthodes ne modifient pas l'original.

## Exercices

**Guidé**

1. Crée `const codes = [200, 404, 200, 500, 403, 200]`.
2. Avec `filter`, garde uniquement les codes `>= 400`.
3. Avec `map`, transforme-les en `"Erreur XXX"`.
4. Affiche le résultat et son `.length`.

**Autonome**
À partir d'une liste d'IP contenant des doublons et un mélange privé/public, produis un tableau des IP **publiques uniques** (combine `filter` et `Set`).

**Défi**
À partir d'un tableau de lignes de log `["8.8.8.8 200", "1.1.1.1 404", "8.8.8.8 500"]`, extrais avec `map` un tableau d'objets `{ip, code}` (utilise `split(" ")`), puis avec `filter` garde ceux dont le code `>= 400`. Affiche le résultat. *(On verra les objets en détail au chapitre suivant — ici, devine la syntaxe `{ip: ..., code: ...}`.)*

## ✅ Tu sais maintenant…

- créer, indexer et mesurer un tableau ;
- ajouter/retirer avec `push`/`pop` ;
- filtrer avec `filter`, transformer avec `map`, trouver avec `find` ;
- tester la présence avec `includes` ;
- enchaîner les méthodes et dédoublonner avec `Set` ;
- distinguer `find` (un élément) de `filter` (un tableau).


-----
