---
title: Chapitre 18 — LocalStorage et SessionStorage
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Le navigateur offre un moyen de **stocker des données** côté client, qui survivent au rechargement de la page : le **Web Storage**. Il en existe deux variantes.

### LocalStorage : persistant

```javascript
// Écrire (toujours des chaînes de caractères)
localStorage.setItem("derniere_ip", "8.8.8.8");

// Lire
const ip = localStorage.getItem("derniere_ip");
console.log(ip);   // "8.8.8.8"

// Supprimer une clé
localStorage.removeItem("derniere_ip");

// Tout effacer
localStorage.clear();
```


`localStorage` **persiste** même après fermeture du navigateur. Les données restent jusqu'à suppression explicite.

### SessionStorage : temporaire

Même API, mais les données disparaissent à la **fermeture de l'onglet**.

```javascript
sessionStorage.setItem("etape", "2");
console.log(sessionStorage.getItem("etape"));   // "2"
```


### Stocker des objets : passer par JSON

Le Web Storage ne stocke **que des chaînes**. Pour un objet, on sérialise en JSON (Partie 2).

```javascript
const prefs = { theme: "sombre", langue: "fr" };

// Écrire un objet
localStorage.setItem("prefs", JSON.stringify(prefs));

// Relire et reconvertir
const lu = JSON.parse(localStorage.getItem("prefs"));
console.log(lu.theme);   // "sombre"
```


## Très utile en pratique

Mémoriser une préférence d'interface entre deux visites :

```javascript
// Au chargement : restaurer la préférence
const theme = localStorage.getItem("theme") || "clair";
console.log(`Thème : ${theme}`);

// Sur action utilisateur : sauvegarder
function changerTheme(nouveau) {
  localStorage.setItem("theme", nouveau);
}
```


## Exemple simple

```javascript
// Compter les visites de la page
let visites = Number(localStorage.getItem("visites") || 0);
visites++;
localStorage.setItem("visites", visites);
console.log(`Visite n° ${visites}`);
```


(Le `Number(...)` reconvertit la chaîne stockée en nombre.)

## Application IT / cyber / OSINT

Le Web Storage est utile pour des **préférences** ou un **état non sensible** dans tes petits outils web (thème, dernier terme recherché, historique local d'analyse). Mais il est surtout important de connaître ses **limites de sécurité**, car c'est une source fréquente de vulnérabilités dans les applications réelles que tu analyseras.

> ### 🛡️ Réflexe sécurité (MAJEUR) : jamais de secret dans LocalStorage
> **Ne stocke JAMAIS de token, mot de passe, clé d'API ou donnée sensible dans LocalStorage ou SessionStorage.** Raison : **tout JavaScript exécuté sur la page peut les lire** (`localStorage.getItem(...)`). Donc si la page subit une **faille XSS** (chapitre 15), l'attaquant lit instantanément tout ton LocalStorage et **vole les tokens**. C'est les risques n° 4 et n° 5 de la Boîte à risques.
>
> Pour l'authentification, les jetons de session sérieux sont gérés via des **cookies `HttpOnly`** (chapitre suivant), justement **inaccessibles** à JavaScript.

> ### ⚠️ À ne pas confondre : cookie / sessionStorage / LocalStorage
> | | LocalStorage | SessionStorage | Cookie |
> | --- | --- | --- | --- |
> | **Durée** | jusqu'à suppression | fermeture de l'onglet | configurable |
> | **Envoyé au serveur ?** | non | non | **oui, automatiquement** |
> | **Lisible par JS ?** | oui | oui | oui, **sauf si `HttpOnly`** |
> | **Usage typique** | préférences | état temporaire | session / authentification |
>
> C'est le risque n° 6 : choisir le mauvais mécanisme mène à des fuites ou des pertes.

## ❌ Erreur classique

```javascript
// ☠️ LA faute grave : stocker un token côté client
localStorage.setItem("auth_token", "eyJhbGci...");   // volé au premier XSS

// ❌ Oublier que tout est chaîne
localStorage.setItem("compteur", 5);
const c = localStorage.getItem("compteur");
console.log(c + 1);        // "51" (concaténation de chaînes !)
console.log(Number(c) + 1); // 6  ✅ reconvertir en nombre

// ❌ Stocker un objet sans JSON
localStorage.setItem("user", { nom: "admin" });
console.log(localStorage.getItem("user"));   // "[object Object]" — données perdues !
// ✅ JSON.stringify à l'écriture, JSON.parse à la lecture
```


> **Réflexe diagnostic :** une valeur stockée se comporte « comme du texte » (concaténée au lieu d'additionnée) ? Normal : le Web Storage ne stocke que des chaînes. Reconvertis avec `Number(...)` ou `JSON.parse(...)`.

## Exercices

**Guidé**

1. Stocke ton nom dans `localStorage` sous la clé `"nom"`.
2. Relis-le et affiche-le.
3. Recharge la page : vérifie qu'il est toujours là. Supprime-le avec `removeItem`.

**Autonome**
Stocke un objet de préférences `{theme, langue}` en JSON. Relis-le, change le thème, resauvegarde. Vérifie après rechargement.

**Défi**
Implémente un compteur de visites persistant ET un mini-historique : à chaque visite, ajoute l'horodatage (`new Date().toISOString()`) dans un tableau stocké en JSON dans `localStorage`. Affiche les 5 dernières visites. Réfléchis (commentaire) : pourquoi ne mettrais-tu **jamais** un token de session ici ?

## ✅ Tu sais maintenant…

- écrire/lire/supprimer avec `localStorage` et `sessionStorage` ;
- distinguer persistant (Local) et temporaire (Session) ;
- stocker des objets via `JSON.stringify`/`JSON.parse` ;
- expliquer pourquoi un secret ne doit jamais y être stocké ;
- distinguer cookie / sessionStorage / LocalStorage.

-----
