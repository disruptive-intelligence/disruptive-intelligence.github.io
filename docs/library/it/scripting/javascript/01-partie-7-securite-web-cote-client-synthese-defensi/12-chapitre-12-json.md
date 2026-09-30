---
title: Chapitre 12 — JSON
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

**JSON** (*JavaScript Object Notation*) est le format texte universel d'échange de données sur le web. Toutes les APIs, presque tous les fichiers de configuration et de logs structurés l'utilisent. Sa syntaxe ressemble à un objet JavaScript, avec des règles strictes.

```json
{
  "ip": "8.8.8.8",
  "ports": [80, 443],
  "actif": true,
  "tags": null
}
```


Règles du JSON (plus strictes qu'un objet JS) :

- les **clés** sont toujours entre **guillemets doubles** ;
- les **chaînes** utilisent des guillemets **doubles** (jamais simples) ;
- pas de virgule après le dernier élément ;
- valeurs autorisées : string, number, boolean, `null`, objet, tableau.

### Convertir entre JSON et objet JavaScript

Deux fonctions, à ne jamais confondre :

```javascript
// JSON.parse : texte JSON → objet JavaScript (pour LIRE une réponse d'API)
const texteJson = '{"ip": "8.8.8.8", "code": 403}';
const obj = JSON.parse(texteJson);
console.log(obj.ip);     // "8.8.8.8"
console.log(obj.code);   // 403

// JSON.stringify : objet JavaScript → texte JSON (pour ENVOYER ou SAUVEGARDER)
const event = { ip: "1.1.1.1", code: 500 };
const json = JSON.stringify(event);
console.log(json);       // '{"ip":"1.1.1.1","code":500}'

// Version lisible (indentée)
console.log(JSON.stringify(event, null, 2));
```


Moyen mnémotechnique : **parse** = « lire » (entrant), **stringify** = « écrire » (sortant).

## Très utile en pratique

Lire une réponse d'API simulée (un tableau d'objets, structure ultra-courante) :

```javascript
const reponseApi = '[{"ip":"8.8.8.8","score":10},{"ip":"1.1.1.1","score":85}]';

const donnees = JSON.parse(reponseApi);

// On peut maintenant utiliser filter/map du chapitre 10
const malveillantes = donnees.filter((d) => d.score >= 80);
console.log(malveillantes);   // [{ip: "1.1.1.1", score: 85}]
```


## Exemple simple

```javascript
const alerte = {
  ip: "203.0.113.9",
  type: "brute-force",
  tentatives: 42
};

// Sauvegarder en JSON lisible
const json = JSON.stringify(alerte, null, 2);
console.log(json);
```


Sortie :

```text
{
  "ip": "203.0.113.9",
  "type": "brute-force",
  "tentatives": 42
}
```


## Application IT / cyber / OSINT

JSON est **omniprésent** en cyber : toutes les APIs de threat intelligence (VirusTotal, AbuseIPDB…), les SIEM, les exports de logs structurés parlent JSON. Le geste central est : `fetch` une API (Partie 5) → `JSON.parse` la réponse → `filter`/`map` les résultats → afficher ou sauvegarder. Tu vas le répéter constamment. Savoir lire et produire du JSON proprement est une compétence quotidienne d'analyste.

> ### 🛡️ Réflexe sécurité : ne jamais faire confiance à du JSON non validé
> Une réponse JSON vient souvent d'une source externe. **Trois précautions :**
> 1. **Entoure `JSON.parse` d'un `try/catch`** (chapitre suivant) : un JSON malformé fait planter ton code.
> 2. **Vérifie la structure** avant de l'utiliser : la clé attendue existe-t-elle ? Est-ce bien un tableau ?
> 3. **N'utilise JAMAIS `eval`** pour parser du JSON. `eval` exécute le texte comme du code → exécution arbitraire si la donnée est piégée. C'est le risque n° 2 de la Boîte à risques. `JSON.parse` est le seul bon outil.

## ❌ Erreur classique

```javascript
// ❌ JSON malformé → plantage
const mauvais = "{ip: '8.8.8.8'}";   // clés sans guillemets doubles, guillemets simples
JSON.parse(mauvais);   // ❌ SyntaxError: Unexpected token i in JSON

// ✅ JSON valide
const bon = '{"ip": "8.8.8.8"}';
console.log(JSON.parse(bon).ip);   // "8.8.8.8"

// ❌ Confondre l'objet et sa version texte
const obj = { a: 1 };
console.log(obj.a);              // 1 (objet)
const txt = JSON.stringify(obj);
console.log(txt.a);              // undefined (txt est une CHAÎNE, pas un objet !)

// ❌ Utiliser eval pour parser (DANGER)
// eval(texteJson);   // ☠️ JAMAIS — exécution de code arbitraire
```


> **Réflexe diagnostic :** `SyntaxError ... in JSON` ? Ton texte n'est pas du JSON valide. Vérifie les guillemets **doubles** sur les clés et les chaînes, et l'absence de virgule finale.

## Exercices

**Guidé**

1. Crée un objet `{ ip, code, date }`.
2. Convertis-le en JSON lisible avec `JSON.stringify(obj, null, 2)`.
3. Reconvertis ce JSON en objet avec `JSON.parse` et affiche `obj.ip`.

**Autonome**
À partir de la chaîne JSON `'[{"domaine":"a.test","score":20},{"domaine":"b.test","score":90}]'`, parse-la et garde les domaines de score `>= 80`. Affiche-les.

**Défi**
Écris une fonction `parserSafe(texte)` qui tente `JSON.parse` dans un `try/catch` (regarde le chapitre suivant si besoin) et renvoie l'objet, ou `null` si le JSON est invalide — sans planter. Teste-la avec un JSON valide et un JSON cassé.

## ✅ Tu sais maintenant…

- reconnaître la syntaxe stricte du JSON ;
- convertir texte → objet avec `JSON.parse` (lire) ;
- convertir objet → texte avec `JSON.stringify` (écrire), version indentée ;
- traiter une réponse JSON avec `filter`/`map` ;
- appliquer les réflexes sécurité : `try/catch`, validation de structure, jamais d'`eval`.

-----
