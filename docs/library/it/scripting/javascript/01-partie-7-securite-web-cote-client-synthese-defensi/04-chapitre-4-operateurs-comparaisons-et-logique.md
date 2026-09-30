---
title: Chapitre 4 — Opérateurs, comparaisons et logique
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

### Opérateurs arithmétiques

```javascript
console.log(10 + 3);   // 13
console.log(10 - 3);   // 7
console.log(10 * 3);   // 30
console.log(10 / 3);   // 3.333...
console.log(10 % 3);   // 1   (modulo : le reste de la division)
```


Le **modulo** `%` est utile en cyber : tester la parité, faire des regroupements, vérifier des multiples.

### Comparaisons : le point critique `==` vs `===`

JavaScript a **deux** opérateurs d'égalité, et c'est l'une des sources de bugs les plus fréquentes.

- **`===`** (égalité **stricte**) : compare la valeur **ET** le type. **C'est celui qu'on utilise.**
- **`==`** (égalité **lâche**) : compare les valeurs en **convertissant** les types au passage. Source de surprises.

```javascript
console.log(443 === 443);     // true
console.log(443 === "443");   // false  ← number vs string : types différents
console.log(443 == "443");    // true   ← == convertit "443" en nombre : piège !

console.log(0 == false);      // true   ← conversion surprenante
console.log("" == false);     // true   ← idem
console.log(null == undefined); // true ← idem
```


> ### ⚠️ À ne pas confondre : `==` vs `===`
> **Règle absolue pour débuter : utilise toujours `===` et `!==`.** Ils sont prévisibles. `==` fait des conversions implicites qui mènent à des comparaisons fausses sans erreur visible. C'est le risque n° 14 de la Boîte à risques.
>
> Mêmes opérateurs pour l'inégalité : `!==` (strict, à utiliser) vs `!=` (lâche, à éviter).

Autres comparaisons (sans piège, elles) :

```javascript
console.log(500 > 400);    // true
console.log(200 < 400);    // true
console.log(443 >= 443);   // true
console.log(80 <= 79);     // false
```


### Truthy et falsy

Dans un contexte booléen (un `if`, par exemple), chaque valeur est considérée comme **vraie** (truthy) ou **fausse** (falsy). Les valeurs **falsy** à connaître par cœur :

```text
false       0       ""  (chaîne vide)
null        undefined       NaN  (Not a Number)
```


**Tout le reste est truthy**, y compris `"0"` (chaîne contenant zéro), `"false"` (le texte), `[]` (tableau vide) et `{}` (objet vide).

> **`NaN`** signifie *Not a Number* : c'est le résultat d'un calcul numérique impossible ou invalide, par exemple `Number("abc")` ou `0 / 0`. C'est une valeur de type `number` qui représente paradoxalement « pas un nombre valide ».

```javascript
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean("0"));      // true  ← une chaîne non vide est truthy !
console.log(Boolean([]));       // true  ← surprenant mais vrai
```


### Opérateurs logiques

```javascript
//  &&  (ET) : vrai si LES DEUX sont vrais
console.log(true && true);    // true
console.log(true && false);   // false

//  ||  (OU) : vrai si AU MOINS UN est vrai
console.log(false || true);   // true

//  !   (NON) : inverse
console.log(!true);           // false
```


## Très utile en pratique

Combiner comparaisons et logique pour décrire une règle :

```javascript
const codeHttp = 503;

// Est-ce une erreur serveur ? (codes 500 à 599)
const estErreurServeur = codeHttp >= 500 && codeHttp <= 599;
console.log(`Erreur serveur : ${estErreurServeur}`);   // Erreur serveur : true
```


## Exemple simple

```javascript
const port = 22;
const estPortConnu = port === 22 || port === 80 || port === 443;
console.log(`Port bien connu : ${estPortConnu}`);   // true
```


## Application IT / cyber / OSINT

Le triage défensif repose entièrement sur des comparaisons et de la logique : « ce code HTTP est-il une erreur ? », « ce port est-il dans ma liste à surveiller ? », « cette tentative dépasse-t-elle le seuil **ET** vient-elle d'une IP externe ? ».

Le piège `==` vs `===` est particulièrement vicieux ici. Une donnée venue d'une API ou d'un log arrive souvent en **string**. Comparer `"443" == 443` renvoie `true` par conversion, ce qui peut masquer un vrai problème de typage. En utilisant **toujours `===`**, tu forces une comparaison honnête et tu repères les incohérences de type au lieu de les ignorer.

## ❌ Erreur classique

```javascript
// ❌ Utiliser == et se faire piéger par la conversion
if ("0" == false) {
  console.log("Ceci s'affiche... mais on ne s'y attendait pas !");
}

// ✅ Avec ===, le piège disparaît
console.log("0" === false);   // false (logique : string vs boolean)

// ❌ Croire qu'un tableau vide est falsy
if ([]) {
  console.log("Un tableau vide est TRUTHY"); // s'affiche !
}
```


> **Réflexe diagnostic :** une condition se comporte « bizarrement » (s'exécute alors qu'elle ne devrait pas) ? Soupçonne en premier un `==` au lieu de `===`, ou une valeur truthy/falsy inattendue. Affiche la valeur avec `console.log` et son `typeof`.

## Exercices

**Guidé**

1. Crée `const code = 404`.
2. Calcule un booléen `estErreurClient` vrai si `code` est entre 400 et 499.
3. Affiche-le.
4. Refais le test avec `code = 200` et vérifie qu'il vaut `false`.

**Autonome**
Écris une expression booléenne qui vaut `true` si un `port` est **soit** 80 **soit** 443, **et** qu'une variable `estPublic` vaut `true`. Teste avec plusieurs valeurs.

**Défi**
Sans exécuter, prédis le résultat de chaque ligne, puis vérifie :

```javascript
console.log(1 == "1");
console.log(1 === "1");
console.log(null == undefined);
console.log(null === undefined);
console.log(Boolean("false"));
```

Explique en une phrase, pour chaque, pourquoi `==` et `===` diffèrent (ou non).

## ✅ Tu sais maintenant…

- utiliser les opérateurs arithmétiques, dont le modulo `%` ;
- distinguer `==` (lâche, à éviter) et `===` (strict, à utiliser), de même pour `!=` / `!==` ;
- citer les valeurs falsy (`false`, `0`, `""`, `null`, `undefined`, `NaN`) ;
- combiner des conditions avec `&&`, `||`, `!` ;
- diagnostiquer une condition au comportement surprenant.

-----
