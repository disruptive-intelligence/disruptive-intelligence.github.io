---
title: Chapitre 11 — Objets
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Un **objet** regroupe des données sous forme de paires **clé-valeur**. C'est l'outil idéal pour représenter une « chose » avec plusieurs caractéristiques.

```javascript
const evenement = {
  ip: "8.8.8.8",
  utilisateur: "admin",
  code: 403,
  date: "2024-01-15"
};

// Accès par point
console.log(evenement.ip);     // "8.8.8.8"
console.log(evenement.code);   // 403

// Accès par crochets (utile si la clé est dans une variable)
const cle = "utilisateur";
console.log(evenement[cle]);   // "admin"
```


### Modifier, ajouter, supprimer

```javascript
const alerte = { niveau: "info", source: "firewall" };

alerte.niveau = "critique";        // modifier
alerte.horodatage = "12:30:00";    // ajouter une nouvelle clé
delete alerte.source;              // supprimer

console.log(alerte);   // { niveau: "critique", horodatage: "12:30:00" }
```


### Parcourir un objet

```javascript
const service = { nom: "RDP", port: 3389, chiffre: false };

console.log(Object.keys(service));    // ["nom", "port", "chiffre"]
console.log(Object.values(service));  // ["RDP", 3389, false]

// Parcourir clés + valeurs
for (const [cle, valeur] of Object.entries(service)) {
  console.log(`${cle} : ${valeur}`);
}
// nom : RDP
// port : 3389
// chiffre : false
```


### Objets imbriqués et tableaux d'objets

C'est ainsi que se structurent les données réelles (et le JSON, chapitre suivant) :

```javascript
// Un tableau d'objets : LA structure la plus courante en cyber
const alertes = [
  { ip: "8.8.8.8", code: 403 },
  { ip: "1.1.1.1", code: 500 },
  { ip: "9.9.9.9", code: 200 }
];

console.log(alertes[0].ip);   // "8.8.8.8"

// Combiné avec filter/map du chapitre 10
const erreurs = alertes.filter((a) => a.code >= 400);
console.log(erreurs);   // [{ip: "8.8.8.8", code: 403}, {ip: "1.1.1.1", code: 500}]
```


### Déstructuration (raccourci pratique)

```javascript
const event = { ip: "8.8.8.8", code: 403 };
const { ip, code } = event;   // extrait ip et code en variables
console.log(ip, code);        // "8.8.8.8" 403
```


## Très utile en pratique

Modéliser une observation défensive comme objet, puis traiter une collection :

```javascript
const logs = [
  { ip: "203.0.113.5", action: "login", succes: false },
  { ip: "203.0.113.5", action: "login", succes: false },
  { ip: "8.8.8.8",     action: "login", succes: true }
];

// Combien d'échecs de connexion ?
const echecs = logs.filter((l) => l.action === "login" && l.succes === false);
console.log(`Échecs de connexion : ${echecs.length}`);   // 2
```


## Exemple simple

```javascript
function decrireService(service) {
  return `${service.nom} sur le port ${service.port} (chiffré : ${service.chiffre})`;
}

const ssh = { nom: "SSH", port: 22, chiffre: true };
console.log(decrireService(ssh));   // SSH sur le port 22 (chiffré : true)
```


## Application IT / cyber / OSINT

L'objet est la **brique de modélisation** de toute donnée structurée en sécurité : un événement de log, une alerte SOC, un IOC enrichi (`{valeur, type, source, score}`), une entrée de threat intel. Et surtout : un **tableau d'objets** est exactement ce que renvoient les APIs (sous forme JSON, chapitre suivant). Maîtriser « tableau d'objets + `filter`/`map` » te donne le geste central de l'analyse de données défensive.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, les objets révèlent **la structure des données** manipulées. Un objet `{ token, userId, sessionId }` t'apprend beaucoup sur ce que le code gère, et donc sur ce qui pourrait fuiter.

## ❌ Erreur classique

```javascript
// ❌ Accéder à une clé qui n'existe pas
const event = { ip: "8.8.8.8" };
console.log(event.code);          // undefined (pas d'erreur)
console.log(event.code.toString()); // ❌ TypeError: Cannot read properties of undefined

// ✅ Vérifier avant, ou utiliser l'accès optionnel
console.log(event.code?.toString()); // undefined (le ?. évite le crash)

// ❌ Confondre point et crochets quand la clé est dynamique
const cle = "ip";
console.log(event.cle);    // undefined (cherche une clé littérale "cle" !)
console.log(event[cle]);   // "8.8.8.8"  ✅
```


> **Réflexe diagnostic :** `Cannot read properties of undefined` signifie que tu accèdes à une propriété sur quelque chose qui vaut `undefined`. Affiche l'objet avec `console.log` pour voir sa vraie structure, et utilise `?.` pour les accès incertains.

## Exercices

**Guidé**

1. Crée un objet `alerte` avec les clés `ip`, `code`, `date`.
2. Affiche chaque valeur avec une template string.
3. Ajoute une clé `traitee` valant `false`, puis passe-la à `true`.

**Autonome**
Crée un tableau de 4 objets `{ip, code}`. Avec `filter`, garde les erreurs (`code >= 400`). Avec `map`, transforme-les en chaînes `"IP X → code Y"`. Affiche le résultat.

**Défi**
À partir d'un tableau d'objets log `{ip, succes}`, compte le nombre d'échecs **par IP** et stocke le résultat dans un objet compteur `{ "203.0.113.5": 2, ... }`. *(Indice : parcours avec `for...of`, et fais `compteur[ip] = (compteur[ip] || 0) + 1`.)* C'est un vrai geste de détection de brute-force.

## ✅ Tu sais maintenant…

- créer un objet et accéder à ses valeurs par `.` et `[]` ;
- modifier, ajouter, supprimer des clés ;
- parcourir avec `Object.keys`, `values`, `entries` ;
- manipuler des tableaux d'objets avec `filter`/`map` ;
- déstructurer et utiliser l'accès optionnel `?.`.

-----
