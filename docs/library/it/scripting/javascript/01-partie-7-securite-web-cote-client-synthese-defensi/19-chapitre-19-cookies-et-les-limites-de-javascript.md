---
title: Chapitre 19 — Cookies et les limites de JavaScript
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Un **cookie** est une petite donnée stockée par le navigateur, avec une particularité majeure : il est **envoyé automatiquement au serveur** à chaque requête vers le site. C'est historiquement le mécanisme des **sessions** (rester connecté).

### Lire et écrire des cookies en JavaScript

```javascript
// Lire tous les cookies accessibles à JS (une seule chaîne)
console.log(document.cookie);   // "theme=sombre; langue=fr"

// Écrire un cookie
document.cookie = "theme=sombre; path=/";
```


L'API `document.cookie` est rudimentaire (tout est dans une seule chaîne à découper soi-même). C'est volontaire : **les cookies sérieux ne sont pas censés être gérés par JavaScript**.

### Les attributs de sécurité essentiels

Un cookie peut porter des attributs qui changent radicalement sa sécurité. Ils sont posés par le **serveur** (via l'en-tête `Set-Cookie`), pas par JavaScript.

| Attribut | Effet | Pourquoi c'est important |
| --- | --- | --- |
| **`HttpOnly`** | le cookie est **invisible** à JavaScript (`document.cookie` ne le voit pas) | protège contre le vol par XSS |
| **`Secure`** | envoyé **uniquement en HTTPS** | empêche l'interception en clair |
| **`SameSite`** | limite l'envoi vers d'autres sites (`Strict`, `Lax`, `None`) | protège contre le CSRF |

```text
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict
```


## Très utile en pratique

> ### 🛡️ Réflexe sécurité : pourquoi `HttpOnly` est une bonne chose
> Quand un cookie de session est **`HttpOnly`**, JavaScript **ne peut pas le lire**. C'est exactement ce qu'on veut : même si la page subit un XSS, l'attaquant ne peut pas voler le cookie de session via `document.cookie`. C'est pour cela qu'on préfère un **cookie `HttpOnly`** à un token en LocalStorage (chapitre 18) pour l'authentification.
>
> Un cookie de session **sans** `HttpOnly`, `Secure` et `SameSite` est vulnérable (vol par XSS, interception, CSRF). C'est le risque n° 16 de la Boîte à risques.

## Exemple simple

```javascript
// Poser un cookie de préférence (non sensible) côté client
document.cookie = "affichage=compact; path=/; SameSite=Lax";

// Lire et chercher une valeur
function lireCookie(nom) {
  const paires = document.cookie.split("; ");
  for (const paire of paires) {
    const [cle, valeur] = paire.split("=");
    if (cle === nom) return valeur;
  }
  return null;
}

console.log(lireCookie("affichage"));   // "compact"
```


## Application IT / cyber / OSINT

Comprendre les cookies et leurs attributs est **central en sécurité web défensive**. En analyse, tu inspectes les en-têtes `Set-Cookie` d'une application (onglet *Réseau* des DevTools) pour vérifier la présence de `HttpOnly`, `Secure`, `SameSite` : leur **absence** est une faiblesse notable, souvent relevée dans les audits. Comprendre que JavaScript **ne doit pas** voir le cookie de session t'aide à raisonner sur le vol de session et le XSS. C'est un sujet que tu approfondiras dans la suite « Web Security ».

> ### 🔍 Lecture de code inconnu
> Un script qui lit ou écrit `document.cookie` mérite attention : que manipule-t-il ? Un cookie sensible géré en JavaScript (au lieu de `HttpOnly` côté serveur) est un signal de conception risquée.

## ❌ Erreur classique

```javascript
// ❌ Croire que document.cookie voit TOUS les cookies
console.log(document.cookie);
// → ne montre PAS les cookies HttpOnly (et c'est voulu, pour la sécurité)

// ☠️ Gérer une session sensible via document.cookie en JS
document.cookie = "session=" + token;   // sans HttpOnly → volable par XSS

// ❌ Confondre où se posent les attributs de sécurité
// HttpOnly / Secure / SameSite des cookies de session = posés par le SERVEUR,
// pas par JavaScript. JS ne peut pas rendre un cookie HttpOnly.
```


> **Réflexe diagnostic :** un cookie « n'apparaît pas » dans `document.cookie` ? Il est probablement `HttpOnly` — invisible à JavaScript par conception. Regarde l'onglet *Application* → *Cookies* des DevTools pour le voir.

## Exercices

**Guidé**

1. Pose un cookie de préférence non sensible avec `document.cookie`.
2. Relis tous les cookies avec `document.cookie`.
3. Écris une fonction `lireCookie(nom)` qui extrait une valeur précise.

**Autonome**
Sur une application web réelle où tu es connecté (la tienne ou un service de test), ouvre DevTools → *Application* → *Cookies*, et repère quels cookies ont `HttpOnly`, `Secure`, `SameSite`. Note lesquels sont invisibles dans `document.cookie` (les `HttpOnly`).

**Défi**
Rédige (en commentaires dans un fichier) un mini-mémo défensif : pour un cookie de session, quels attributs poser et pourquoi, et pourquoi LocalStorage est un mauvais endroit pour un token. Appuie-toi sur les chapitres 18 et 19.

## ✅ Tu sais maintenant…

- comprendre qu'un cookie est envoyé automatiquement au serveur ;
- lire/écrire des cookies non sensibles avec `document.cookie` ;
- expliquer `HttpOnly`, `Secure`, `SameSite` ;
- comprendre pourquoi un cookie de session `HttpOnly` est invisible à JS (et pourquoi c'est bien) ;
- raisonner sur le choix cookie vs LocalStorage pour un token.

-----

## ✅ CHECKPOINT 4 — Tu sais où (ne pas) stocker des données côté client

Avant la Partie 5, assure-toi de pouvoir, **sans regarder** :

- [ ] utiliser `localStorage` / `sessionStorage` (écrire, lire, supprimer) ;
- [ ] stocker un objet via JSON ;
- [ ] expliquer pourquoi un token ne va jamais en LocalStorage ;
- [ ] distinguer cookie / sessionStorage / LocalStorage ;
- [ ] expliquer `HttpOnly`, `Secure`, `SameSite` ;
- [ ] comprendre pourquoi un cookie de session `HttpOnly` est invisible à JS.

Tu maîtrises le stockage client et ses pièges. La Partie 5 ouvre le web dynamique : faire parler ta page au réseau, avec l'asynchrone et `fetch`.


-----
