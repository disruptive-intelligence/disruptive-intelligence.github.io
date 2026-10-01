---
title: Chapitre 7 — Fonctions
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Une **fonction** est un bloc de code réutilisable auquel on donne un nom. Au lieu de réécrire la même logique partout, tu l'écris une fois et tu l'appelles autant que tu veux.

```javascript
// Déclaration d'une fonction
function saluer(nom) {
  return `Bonjour, ${nom}`;
}

// Appel de la fonction
console.log(saluer("admin"));   // Bonjour, admin
console.log(saluer("analyste")); // Bonjour, analyste
```


Vocabulaire :

- **`nom`** entre parenthèses est un **paramètre** : une donnée d'entrée.
- **`return`** renvoie un résultat à celui qui a appelé la fonction.
- `"admin"` lors de l'appel est un **argument** : la valeur réelle passée.

### `return` : renvoyer vs afficher

Ne confonds pas `return` (renvoie une valeur réutilisable) et `console.log` (affiche seulement).

```javascript
function doubler(n) {
  return n * 2;        // renvoie, n'affiche rien
}

const resultat = doubler(21);   // on récupère la valeur
console.log(resultat);          // 42
```


Une fonction sans `return` renvoie `undefined`.

### Fonctions fléchées (arrow functions)

JavaScript propose une syntaxe plus courte, très fréquente dans le code moderne : la **fonction fléchée**.

```javascript
// Fonction classique
function carre(n) {
  return n * n;
}

// Même chose en fonction fléchée
const carre2 = (n) => {
  return n * n;
};

// Version ultra-courte : si le corps est un seul return, on peut tout enlever
const carre3 = (n) => n * n;

console.log(carre(5), carre2(5), carre3(5));   // 25 25 25
```


> ### ⚠️ À ne pas confondre : fonction classique vs fléchée
> Pour un débutant, **les deux font la même chose dans 95 % des cas**. La fléchée est juste plus courte. Tu la verras surtout avec `map`, `filter`, `addEventListener` (chapitres suivants). Il existe une différence subtile sur le mot-clé `this` (voir Annexe A), mais elle ne te concerne pas encore. Utilise celle qui te paraît la plus lisible.

### Paramètres par défaut

```javascript
function connexion(port = 443) {
  return `Connexion sur le port ${port}`;
}

console.log(connexion());      // Connexion sur le port 443 (valeur par défaut)
console.log(connexion(8080));  // Connexion sur le port 8080
```


## Très utile en pratique

Une fonction de test réutilisable, qui renvoie un booléen :

```javascript
function estIpPrivee(ip) {
  return ip.startsWith("10.") ||
         ip.startsWith("192.168.") ||
         ip.startsWith("172.16.");
}

console.log(estIpPrivee("192.168.1.10"));  // true
console.log(estIpPrivee("8.8.8.8"));       // false
```


Maintenant que la logique est dans une fonction, tu peux la réutiliser partout sans la réécrire.

## Exemple simple

```javascript
function classerCode(code) {
  if (code >= 200 && code < 300) return "Succès";
  if (code >= 300 && code < 400) return "Redirection";
  if (code >= 400 && code < 500) return "Erreur client";
  if (code >= 500) return "Erreur serveur";
  return "Inconnu";
}

console.log(classerCode(404));   // Erreur client
console.log(classerCode(200));   // Succès
```


## Application IT / cyber / OSINT

Les fonctions sont la base de tout outil défensif réutilisable. Tu vas écrire des fonctions comme `estIpPrivee(ip)`, `extraireDomaine(url)`, `estHashValide(h)`, `classerAlerte(event)`. Chacune encapsule une règle métier que tu réutilises dans tes parsers, tes scripts de triage et tes mini-outils OSINT. Une fonction bien nommée rend ton code **lisible** : `if (estIpPrivee(ip))` se lit comme une phrase.

> ### 🔍 Lecture de code inconnu (exercice récurrent)
> À partir de ce chapitre, prends l'habitude, face à un script JavaScript trouvé dans une page, de **repérer les fonctions** : leur nom révèle souvent l'intention du code (`sendData`, `getToken`, `validate`…). On approfondira cette compétence au chapitre 33.

## ❌ Erreur classique

```javascript
// ❌ Oublier le return : la fonction calcule mais ne renvoie rien
function additionner(a, b) {
  a + b;          // calculé mais jeté !
}
console.log(additionner(2, 3));   // undefined

// ✅ CORRECT
function additionner2(a, b) {
  return a + b;
}
console.log(additionner2(2, 3));   // 5

// ❌ Appeler une fonction sans les parenthèses
console.log(additionner2);    // affiche le code de la fonction, ne l'exécute pas !
console.log(additionner2(2, 3)); // ✅ avec parenthèses : l'exécute
```


> **Réflexe diagnostic :** ta fonction renvoie `undefined` ? Tu as très probablement oublié le `return`.

## Exercices

**Guidé**

1. Écris une fonction `estPortSecurise(port)` qui renvoie `true` si le port est 22 ou 443, sinon `false`.
2. Teste-la avec 22, 80, 443, 3389.

**Autonome**
Écris une fonction `categorieCode(code)` qui renvoie la catégorie d'un code HTTP (réutilise la logique du mini-projet du checkpoint 1, mais sous forme de fonction renvoyant une string).

**Défi**
Écris une fonction `normaliserIp(ip)` qui prend une IP éventuellement entourée d'espaces et en majuscules inutiles (ex. `"  8.8.8.8  "`), et renvoie la version nettoyée (`.trim()`). Puis écris une seconde fonction qui utilise la première **et** `estIpPrivee` pour afficher `"privée"` ou `"publique"` proprement.

## ✅ Tu sais maintenant…

- déclarer une fonction avec `function`, des paramètres et un `return` ;
- distinguer `return` (renvoie) et `console.log` (affiche) ;
- écrire une fonction fléchée et comprendre qu'elle équivaut souvent à la classique ;
- utiliser des paramètres par défaut ;
- encapsuler une règle métier dans une fonction réutilisable.

-----
