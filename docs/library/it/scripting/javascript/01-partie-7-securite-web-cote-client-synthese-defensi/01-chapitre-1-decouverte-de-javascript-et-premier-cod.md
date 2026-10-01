---
title: Chapitre 1 — Découverte de JavaScript et premier code
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

### À quoi sert JavaScript ?

Une page web repose sur trois langages, et il est essentiel de ne pas les confondre :

| Langage | Rôle | Analogie |
| --- | --- | --- |
| **HTML** | La **structure** : titres, paragraphes, boutons, champs. | Le squelette |
| **CSS** | Le **style** : couleurs, tailles, positions. | L'habillage |
| **JavaScript** | Le **comportement** : réactions aux clics, calculs, requêtes réseau, modifications dynamiques. | Les muscles et le cerveau |

> ### ⚠️ À ne pas confondre : HTML vs CSS vs JavaScript
> HTML décrit *ce qui est là*. CSS décrit *à quoi ça ressemble*. JavaScript décrit *ce qui se passe quand*. Sans JavaScript, une page est figée : elle s'affiche mais ne **réagit** à rien.

JavaScript est aujourd'hui l'un des langages les plus répandus au monde, précisément parce qu'il tourne dans **tous** les navigateurs. Pour un profil IT/cyber, le savoir-lire est un atout direct : en OSINT comme en analyse, tu rencontreras du JavaScript dans presque toutes les pages que tu inspectes.

### Navigateur vs Node.js : la distinction fondatrice

Le **même** langage JavaScript s'exécute dans deux environnements :

- **Dans le navigateur** : pour rendre les pages vivantes. C'est ici qu'on commence, car **tu n'as rien à installer**.
- **Dans Node.js** : pour écrire des scripts comme en Python. On y viendra en Partie 6.

On commence par le navigateur parce que le retour est **immédiat** : tu tapes du code, tu vois le résultat à la seconde.

### Ouvrir la console (ton premier outil)

Tout navigateur moderne contient une **console JavaScript** intégrée. C'est ton bac à sable.

1. Ouvre ton navigateur sur une page quelconque (même une page blanche `about:blank`).
2. Appuie sur **`F12`** (ou clic droit → *Inspecter*).
3. Clique sur l'onglet **Console**.

Tu vois une invite où tu peux taper du JavaScript. Écris ceci et appuie sur Entrée :

```javascript
console.log("Bonjour depuis JavaScript");
```


Résultat affiché dans la console :

```text
Bonjour depuis JavaScript
```


Félicitations, tu viens d'exécuter du JavaScript. `console.log()` est l'équivalent du `print()` de Python : il **affiche** quelque chose dans la console.

### Commentaires

Comme dans tout langage, on annote son code. JavaScript ignore les commentaires à l'exécution.

```javascript
// Ceci est un commentaire sur une seule ligne

/*
   Ceci est un commentaire
   sur plusieurs lignes
*/

console.log("Le code, lui, s'exécute"); // commentaire en fin de ligne
```


## Très utile en pratique

Tu peux faire des calculs directement dans la console — pratique pour une vérification rapide :

```javascript
console.log(443 + 80);      // 523
console.log(1024 * 8);      // 8192
console.log("a".repeat(10)); // aaaaaaaaaa
```


Tu peux aussi enchaîner plusieurs valeurs dans un seul `console.log`, séparées par des virgules :

```javascript
console.log("Statut :", 200, "OK");
// Statut : 200 OK
```


> ### 💡 À éviter dès le début : `alert()`
> Tu verras souvent `alert("message")` dans de vieux tutoriels. Ça ouvre une boîte de dialogue bloquante. On l'évite : `console.log()` est plus propre, ne bloque pas, et reflète mieux les pratiques réelles.

## Exemple simple

Inspecter une donnée et la transformer, entièrement dans la console :

```javascript
// Une URL trouvée dans une page
let url = "https://Example.COM/login?user=admin";

// On l'affiche
console.log("URL brute :", url);

// On la normalise en minuscules
console.log("Normalisée :", url.toLowerCase());
```


Sortie console :

```text
URL brute : https://Example.COM/login?user=admin
Normalisée : https://example.com/login?user=admin
```


## Application IT / cyber / OSINT

La console du navigateur est **le premier réflexe d'inspection** d'une page web. En OSINT et en analyse défensive, elle te permet de :

- lire les **variables JavaScript** qu'une page expose (parfois des données sensibles oubliées là) ;
- tester rapidement une transformation de texte sur un IOC ;
- comprendre **comment** une page se comporte avant de l'analyser plus en profondeur.

Concrètement, dès qu'une page web t'intrigue, ouvrir `F12` → Console est souvent ta première action. Ce cours t'apprend à comprendre ce que tu y vois.

## ❌ Erreur classique

```javascript
// ❌ Oublier les guillemets autour d'un texte
console.log(Bonjour);
// → ReferenceError: Bonjour is not defined
// JavaScript croit que "Bonjour" est le nom d'une variable !

// ✅ CORRECT : un texte va entre guillemets
console.log("Bonjour");

// ❌ Confondre la console du navigateur et un terminal
ls
// → la console n'est PAS un shell : "ls" n'existe pas en JavaScript
```


> **Réflexe diagnostic :** un message `ReferenceError: X is not defined` signifie presque toujours que tu as écrit un mot **sans guillemets** alors que c'était du texte, ou que tu utilises une variable qui n'existe pas encore.

## Exercices

**Guidé**

1. Ouvre la console (`F12`).
2. Affiche ton prénom avec `console.log`.
3. Affiche le résultat de `65535 - 1024`.
4. Affiche, en une seule instruction : le texte `"Port :"` suivi du nombre `443`.

**Autonome**
Dans la console, écris du code qui affiche la version en minuscules du texte `"ADMIN@Example.COM"`. *(Indice : `.toLowerCase()`.)*

**Défi**
Trouve, dans la console, comment afficher le **nombre de caractères** du texte `"https://example.com"`. *(Indice : les chaînes ont une propriété `.length`. On l'écrit sans parenthèses : `texte.length`.)*

## ✅ Tu sais maintenant…

- expliquer la différence entre HTML, CSS et JavaScript ;
- distinguer JavaScript **navigateur** et JavaScript **Node.js** ;
- ouvrir la console DevTools avec `F12` ;
- afficher des valeurs avec `console.log()` ;
- écrire des commentaires ;
- reconnaître une `ReferenceError` due à des guillemets manquants.

-----
