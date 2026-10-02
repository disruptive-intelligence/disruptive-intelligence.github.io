---
title: Synthèse finale & cheat-sheets
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - index.md
---

## Ce que tu as construit

Tu es parti de zéro et tu disposes maintenant d'un socle JavaScript **orienté IT / cyber / OSINT** :

```text
Console navigateur + fichiers
→ langage de base (variables, conditions, boucles)
→ données et code (fonctions, chaînes, URL, regex, tableaux, objets, JSON, erreurs)
→ DOM et événements (en sécurité)
→ stockage navigateur (et ses pièges)
→ HTTP / async / fetch / CORS
→ Node.js (fichiers, CLI, modules, npm)
→ sécurité web côté client (XSS, CSP, client non fiable, lecture de code)
```


## Les 10 principes à retenir

1. **« Où tourne mon code ? »** Navigateur (DOM, pas de fichiers) ou Node.js (fichiers, pas de DOM). Toujours se poser la question.
2. **`const` par défaut, `let` si ça change, jamais `var`.**
3. **Toujours `===`, jamais `==`.** Comparaison honnête, pas de conversion surprise.
4. **Les chaînes sont immuables** : récupère le résultat (`x = x.trim()`).
5. **`filter`/`map`/`find` + tableaux d'objets** = le geste central du traitement de données.
6. **`JSON.parse` pour lire, `JSON.stringify` pour écrire** ; toujours dans un `try/catch`, jamais d'`eval`.
7. **`textContent`, pas `innerHTML`** pour une donnée externe. C'est la défense n° 1 du XSS.
8. **Jamais de secret côté client** (ni LocalStorage, ni JS). Les secrets restent au serveur.
9. **La validation client = confort ; la sécurité = serveur.** Le client n'est jamais de confiance.
10. **Gère toujours l'échec** (réseau, fichier, parsing) avec `try/catch` ou `.catch`.

-----

## Cheat-sheet — Syntaxe de base

```javascript
// Variables
const x = 10;          // constante
let y = "texte";       // variable

// Types
typeof valeur;         // "string" | "number" | "boolean" | "undefined" | "object"

// Template string
`Valeur : ${x}`;

// Comparaison (toujours stricte)
a === b;   a !== b;   a > b;   a >= b;

// Logique
a && b;    a || b;    !a;

// Condition
if (cond) { } else if (cond2) { } else { }
const r = cond ? "oui" : "non";          // ternaire

// Boucles
for (let i = 0; i < n; i++) { }
for (const el of tableau) { }
while (cond) { }
```


## Cheat-sheet — Chaînes

```javascript
s.length;                 s[0];
s.trim();                 s.toLowerCase();   s.toUpperCase();
s.includes("x");          s.startsWith("x"); s.endsWith("x");
s.indexOf("x");           s.replace("a","b"); s.slice(0, 5);
s.split(",");             ["a","b"].join("-");

// URL
const u = new URL("https://h.test:8443/p?q=1");
u.hostname; u.pathname; u.searchParams.get("q");

// Regex (extraction d'IOC)
texte.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g) || [];
/motif/.test(texte);
```


## Cheat-sheet — Tableaux et objets

```javascript
// Tableaux
arr.push(x);   arr.pop();   arr.length;   arr.includes(x);
arr.filter(el => cond);     // sous-ensemble (tableau)
arr.map(el => transforme);  // transformation (tableau)
arr.find(el => cond);       // premier élément (ou undefined)
[...new Set(arr)];          // dédoublonner

// Objets
const o = { ip: "8.8.8.8", code: 403 };
o.ip;   o["ip"];   o.nouvelle = 1;   delete o.code;
Object.keys(o); Object.values(o); Object.entries(o);
const { ip, code } = o;     // déstructuration
o.peutEtreAbsent?.x;        // accès optionnel

// JSON
const obj = JSON.parse(texte);                 // lire
const txt = JSON.stringify(obj, null, 2);      // écrire (indenté)
```


## Cheat-sheet — DOM (navigateur)

```javascript
const el  = document.querySelector("#id");      // premier
const els = document.querySelectorAll(".cls");  // tous

el.textContent = "sûr";        // ✅ affichage de données
el.innerHTML = "<b>contrôlé</b>"; // ⚠️ jamais avec une donnée externe
el.classList.add("x"); el.classList.toggle("y");
el.setAttribute("data-ip", "8.8.8.8");

const n = document.createElement("li");
n.textContent = valeur; parent.appendChild(n);   // insertion sûre

// Événements
el.addEventListener("click", () => { });
form.addEventListener("submit", (e) => { e.preventDefault(); });
champ.value;   // contenu d'un input
```


## Cheat-sheet — fetch / async

```javascript
// async / await (recommandé)
async function go() {
  try {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const data = await r.json();
    return data;
  } catch (e) {
    console.log("Erreur :", e.message);
  }
}

// Promesses (.then)
fetch(url)
  .then(r => r.json())
  .then(data => { })
  .catch(err => { });
```


## Cheat-sheet — Node.js

```javascript
// Fichiers
const fs = require("fs");
const txt = fs.readFileSync("f.txt", "utf-8");
fs.writeFileSync("out.txt", contenu, "utf-8");
fs.appendFileSync("out.txt", suite, "utf-8");

// Arguments CLI
const args = process.argv.slice(2);   // tes arguments
process.exit(1);                       // code de sortie

// Modules (CommonJS)
module.exports = { maFonction };           // dans outils.js
const { maFonction } = require("./outils"); // ailleurs

// npm
// npm init -y    npm install paquet    npm audit    npm run script
```


-----

## Cheat-sheet SÉCURITÉ — Boîte à risques (version imprimable)

> À garder sous les yeux. Chaque ligne : le risque, la règle, le chapitre.

| Risque | La règle défensive | Ch. |
| --- | --- | --- |
| `innerHTML` + donnée externe | Utilise **`textContent`** (ou `createElement` + `textContent`). | 15, 30 |
| `eval` / `new Function` | **Jamais.** `JSON.parse` pour le JSON. | 13, 30 |
| Validation seulement côté client | **Valide au serveur** ; le client est du confort. | 17, 32 |
| Token/secret en LocalStorage | **Jamais de secret côté client.** Session via cookie `HttpOnly`. | 18, 30 |
| Token exposé dans le JS | Les secrets/clés restent **au serveur**. | 18, 32 |
| Mauvais choix de stockage | Cookie (session) / Session (temporaire) / Local (préférences). | 18, 19 |
| CORS pris pour une sécurité serveur | CORS protège l'**utilisateur** ; sécurise l'API par **auth serveur**. | 24, 31 |
| Bouton masqué = contrôle d'accès | Cacher ≠ interdire ; **autorise au serveur**. | 17, 32 |
| Dépendance npm non vérifiée | `npm audit`, vérifie le nom (typosquatting), `package-lock`. | 29 |
| Copier-coller / exécuter du code inconnu | **Lis, n'exécute pas.** Analyse statique. | 29, 33 |
| Erreurs réseau non gérées | `try/catch` ou `.catch` sur **tout** `fetch`. | 22, 23 |
| JSON non validé | `JSON.parse` en `try/catch` + vérifie la structure. | 12 |
| Donnée utilisateur affichée brute | **`textContent`** systématique. | 15, 30 |
| `==` au lieu de `===` | **Toujours `===` / `!==`.** | 4 |
| `null` vs `undefined` | Teste explicitement ; comprends la différence. | 3 |
| Cookie sans `HttpOnly`/`Secure`/`SameSite` | Pose les trois sur les cookies de session (côté serveur). | 19, 31 |
| Logique sensible côté frontend | **Le client n'est jamais de confiance.** | 32 |

**La phrase à retenir :** *le frontend, c'est l'expérience ; le serveur, c'est la sécurité.*

-----
