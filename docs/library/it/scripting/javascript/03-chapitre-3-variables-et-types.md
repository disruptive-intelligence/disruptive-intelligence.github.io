---
title: Chapitre 3 — Variables et types
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 3
chapters: 35
---

## Le minimum à savoir

Une **variable** est un conteneur nommé qui stocke une valeur. En JavaScript moderne, on en déclare avec **`let`** ou **`const`**.

```javascript
let utilisateur = "admin";   // peut changer plus tard
const port = 443;            // ne changera jamais
```

- **`let`** : une variable dont la valeur **peut** changer.
- **`const`** : une variable dont la valeur **ne doit pas** changer (constante).

```javascript
let statut = "actif";
statut = "inactif";   // ✅ autorisé avec let

const PORT = 443;
PORT = 8443;          // ❌ TypeError: Assignment to constant variable.
```

> ### ⚠️ Évite `var` au début
> Tu croiseras `var` dans du vieux code. Il a un comportement de portée déroutant (voir Annexe A). **Règle simple pour débuter :** utilise `const` par défaut, et `let` seulement si la valeur doit changer. N'utilise pas `var`.

### Les types de valeurs

Une valeur a une **nature** : son **type**. Les types de base à connaître :

| Type | Exemple | Description |
| --- | --- | --- |
| **string** | `"1.2.3.4"` | Du texte, entre guillemets. |
| **number** | `443`, `3.14` | Un nombre (entier ou décimal, pas de distinction). |
| **boolean** | `true`, `false` | Vrai ou faux. |
| **null** | `null` | Une absence de valeur **volontaire**. |
| **undefined** | `undefined` | Une valeur **non encore définie**. |
| **object** | `{ip: "1.2.3.4"}` | Une structure clé-valeur (chapitre 11). |
| **array** | `["a", "b"]` | Une liste ordonnée (chapitre 10). Techniquement un type d'objet. |

Pour connaître le type d'une valeur, utilise `typeof` :

```javascript
console.log(typeof "1.2.3.4");  // "string"
console.log(typeof 443);        // "number"
console.log(typeof true);       // "boolean"
console.log(typeof undefined);  // "undefined"
console.log(typeof null);       // "object"  ← bizarrerie historique, à connaître
```

### Les guillemets et les template strings

Le texte (string) peut s'écrire avec des guillemets doubles `"..."`, simples `'...'`, ou des **backticks** `` `...` ``. Les backticks sont les plus utiles : ils permettent d'**insérer des variables** directement avec `${...}`.

```javascript
const ip = "10.0.0.5";
const port = 22;

// ❌ Concaténation pénible avec +
console.log("Connexion à " + ip + " sur le port " + port);

// ✅ Template string : bien plus lisible
console.log(`Connexion à ${ip} sur le port ${port}`);
```

Les deux affichent : `Connexion à 10.0.0.5 sur le port 22`.

## Très utile en pratique

Stocker des données d'analyse dans des variables bien typées rend le code clair :

```javascript
const ip = "192.168.1.50";       // string
const port = 3389;               // number
const estChiffre = false;        // boolean
const protocole = "RDP";         // string

console.log(`Service détecté : ${protocole} sur ${ip}:${port} (chiffré : ${estChiffre})`);
// Service détecté : RDP sur 192.168.1.50:3389 (chiffré : false)
```

## Exemple simple

```javascript
let nbTentatives = 0;       // un compteur, amené à changer → let
const seuilAlerte = 5;      // un seuil fixe → const

nbTentatives = nbTentatives + 1;   // une tentative
nbTentatives = nbTentatives + 1;   // une autre

console.log(`Tentatives : ${nbTentatives} / seuil : ${seuilAlerte}`);
// Tentatives : 2 / seuil : 5
```

## Application IT / cyber / OSINT

En analyse défensive, tu modélises constamment des observations sous forme de variables typées : une **IP** est une string, un **port** un number, un **flag** « malveillant » un boolean. Bien typer dès le départ évite des comparaisons absurdes (par exemple comparer un port écrit en texte `"443"` avec un nombre `443` — un piège qu'on dissèque au chapitre 4).

Le réflexe `typeof` est aussi un outil de **diagnostic** : quand une donnée venue d'une API ne se comporte pas comme prévu, vérifier `typeof maValeur` révèle souvent qu'un nombre est en fait une string.

## ❌ Erreur classique

```javascript
// ❌ Réassigner une const
const x = 10;
x = 20;
// → TypeError: Assignment to constant variable.

// ❌ Utiliser une variable avant de la déclarer
console.log(y);   // ReferenceError (avec let/const)
let y = 5;

// ❌ Confondre null et undefined
let a;            // déclarée mais sans valeur → undefined
let b = null;     // valeur "vide" volontaire → null
console.log(a);   // undefined
console.log(b);   // null
```

> ### ⚠️ À ne pas confondre : `null` vs `undefined`
> - **`undefined`** : « cette variable existe mais on ne lui a **jamais** donné de valeur ». C'est l'état par défaut.
> - **`null`** : « on a **volontairement** mis une valeur vide ici ». C'est un choix du développeur.
>
> Confondre les deux mène à des tests faux. C'est le risque n° 15 de la Boîte à risques. On verra comment les tester proprement au chapitre suivant.

## Exercices

**Guidé**
1. Déclare une `const ip` valant `"172.16.0.1"`.
2. Déclare un `let compteur` valant `0`.
3. Incrémente `compteur` deux fois.
4. Affiche, avec une template string : `IP 172.16.0.1 vue 2 fois`.

**Autonome**
Crée trois variables décrivant un service réseau (nom du service en string, port en number, ouvert en boolean) et affiche une phrase récapitulative avec une template string. Affiche aussi le `typeof` de chacune.

**Défi**
Sans exécuter le code, **prédis** ce qu'affiche `typeof null`, `typeof []`, et `typeof "443"`. Puis vérifie dans la console. Note ce qui te surprend — on expliquera ces subtilités au fil du cours.

## ✅ Tu sais maintenant…

- déclarer des variables avec `const` et `let`, et éviter `var` ;
- choisir `const` par défaut et `let` si la valeur change ;
- nommer les types de base : string, number, boolean, null, undefined, object, array ;
- utiliser `typeof` pour inspecter un type ;
- écrire des template strings avec `` `${...}` `` ;
- distinguer `null` (vide volontaire) et `undefined` (jamais défini).

-----
