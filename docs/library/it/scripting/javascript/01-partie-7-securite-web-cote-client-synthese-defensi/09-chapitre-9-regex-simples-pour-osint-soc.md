---
title: Chapitre 9 — Regex simples pour OSINT / SOC
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

> **Chapitre court.** On reste volontairement sur les bases. Les regex avancées (groupes nommés, lookahead…) ne sont pas nécessaires ici. L'objectif : savoir **extraire** des IOC d'un texte.

## Le minimum à savoir

Une **expression régulière** (regex) est un motif qui décrit une forme de texte. En JavaScript, une regex s'écrit entre slashes : `/motif/`.

```javascript
const texte = "Connexion depuis 8.8.8.8 vers le port 443";

// Tester si un motif existe
console.log(/\d+/.test(texte));   // true  (contient au moins un chiffre)
```


### Les briques de base

| Motif | Signifie | Exemple |
| --- | --- | --- |
| `\d` | un chiffre (0-9) | `\d\d\d` → 3 chiffres |
| `\w` | un caractère de mot (lettre, chiffre, `_`) | |
| `.` | n'importe quel caractère | |
| `+` | « un ou plusieurs » du motif précédent | `\d+` → 1+ chiffres |
| `*` | « zéro ou plusieurs » | |
| `{n}` | exactement n fois | `\d{1,3}` → 1 à 3 chiffres |
| `[abc]` | un caractère parmi a, b, c | `[0-9]` = `\d` |
| `\.` | un vrai point (échappé) | dans une IP |
| `g` | drapeau « global » : toutes les occurrences | `/\d+/g` |
| `i` | drapeau « insensible à la casse » | |

### Extraire avec `match`

```javascript
const log = "IP source 192.168.1.10, IP dest 8.8.8.8";

// Motif simplifié d'IPv4 : 1 à 3 chiffres, un point, ... 4 fois
const motifIp = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

const ips = log.match(motifIp);
console.log(ips);   // ["192.168.1.10", "8.8.8.8"]
```


Sans le drapeau `g`, `match` ne renvoie que la **première** occurrence. Avec `g`, il renvoie **toutes** les occurrences dans un tableau (ou `null` si aucune).

## Très utile en pratique : motifs d'IOC courants

```javascript
// IPv4 (version simple, suffisante pour extraire d'un texte)
const reIp = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

// Email (version simple)
const reEmail = /[\w.+-]+@[\w-]+\.[\w.-]+/g;

// Hash MD5 (32 caractères hexadécimaux)
const reMd5 = /\b[a-f0-9]{32}\b/gi;

// Hash SHA-256 (64 caractères hexadécimaux)
const reSha256 = /\b[a-f0-9]{64}\b/gi;
```


> Ces motifs sont **volontairement simples** : ils servent à **extraire des candidats** d'un texte, pas à valider strictement. Une validation rigoureuse (IP entre 0 et 255, etc.) se fait ensuite avec des conditions ou des objets dédiés.

## Exemple simple

```javascript
const rapport = `
Alerte: connexion de admin@corp.test
depuis 203.0.113.45 et 8.8.8.8
fichier suspect: d41d8cd98f00b204e9800998ecf8427e
`;

const ips = rapport.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g);
const emails = rapport.match(/[\w.+-]+@[\w-]+\.[\w.-]+/g);
const md5 = rapport.match(/\b[a-f0-9]{32}\b/gi);

console.log("IPs :", ips);       // ["203.0.113.45", "8.8.8.8"]
console.log("Emails :", emails); // ["admin@corp.test"]
console.log("MD5 :", md5);       // ["d41d8cd98f00b204e9800998ecf8427e"]
```


## Application IT / cyber / OSINT

C'est exactement le geste d'un analyste : **extraire les IOC** d'un bloc de texte (rapport, log, email d'alerte). En quelques lignes, tu récupères toutes les IP, emails et hash d'un document. Combiné aux méthodes de tableaux du chapitre suivant (dédoublonnage avec un `Set`, filtrage), tu obtiens un mini-extracteur d'IOC — un classique du cours Python, transposé en JavaScript.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, une regex révèle souvent **ce que le code cherche** : un motif d'email, de carte bancaire, de token. Repérer les regex t'aide à comprendre l'intention.

## ❌ Erreur classique

```javascript
// ❌ Oublier le drapeau g : on ne récupère que la première occurrence
const log = "8.8.8.8 et 1.1.1.1";
console.log(log.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/));   // ["8.8.8.8", ...] une seule

// ✅ Avec g : toutes
console.log(log.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g));  // ["8.8.8.8", "1.1.1.1"]

// ❌ Oublier d'échapper le point : . veut dire "n'importe quel caractère"
console.log(/8.8.8.8/.test("8X8X8X8"));   // true  ← pas ce qu'on veut !

// ✅ Échapper avec \.
console.log(/8\.8\.8\.8/.test("8X8X8X8")); // false
```


> **Réflexe diagnostic :** `match` renvoie `null` ? Le motif ne correspond à rien. Teste ton motif progressivement, et vérifie le drapeau `g`.

## Exercices

**Guidé**

1. À partir du texte `"erreurs sur 10.0.0.1 et 10.0.0.2 et 8.8.8.8"`, extrais toutes les IP avec une regex et le drapeau `g`.
2. Affiche le tableau et son `.length`.

**Autonome**
Écris une fonction `extraireEmails(texte)` qui renvoie tous les emails d'un texte (ou un tableau vide si aucun — attention, `match` renvoie `null`, pense à gérer ce cas avec `|| []`).

**Défi**
À partir d'un texte mêlant MD5 (32 hex) et SHA-256 (64 hex), extrais séparément les deux types de hash avec deux regex distinctes, et affiche combien il y en a de chaque. *(Indice : `\b...\b` et la longueur exacte avec `{32}` ou `{64}`.)*

## ✅ Tu sais maintenant…

- écrire une regex simple entre `/.../` ;
- utiliser `\d`, `\w`, `.`, `+`, `{n}`, `[...]`, et échapper avec `\.` ;
- tester avec `.test()` et extraire avec `.match()` ;
- utiliser les drapeaux `g` (global) et `i` (insensible à la casse) ;
- extraire des IOC simples (IP, emails, hash) d'un texte.

-----
