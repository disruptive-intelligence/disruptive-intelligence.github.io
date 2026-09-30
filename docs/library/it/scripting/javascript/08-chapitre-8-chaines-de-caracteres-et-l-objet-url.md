---
title: Chapitre 8 — Chaînes de caractères et l'objet URL
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 8
chapters: 35
---

## Le minimum à savoir

Le **texte** (string) est ce que tu manipules le plus en cyber et en OSINT : logs, IP, domaines, URLs, hash. JavaScript offre de nombreuses méthodes pour le traiter.

### Propriétés et accès

```javascript
const texte = "192.168.1.1";
console.log(texte.length);     // 11  (nombre de caractères)
console.log(texte[0]);         // "1" (premier caractère)
```

> Les chaînes sont **immuables** : une méthode ne modifie jamais la chaîne d'origine, elle en **renvoie une nouvelle**. Il faut donc récupérer le résultat.

### Méthodes essentielles

```javascript
const brut = "  Admin@Example.COM  ";

console.log(brut.trim());            // "Admin@Example.COM"  (enlève les espaces aux bouts)
console.log(brut.trim().toLowerCase()); // "admin@example.com"
console.log("HELLO".toUpperCase());  // "HELLO"

const email = "admin@example.com";
console.log(email.includes("@"));    // true   (contient ?)
console.log(email.startsWith("admin")); // true
console.log(email.endsWith(".com"));    // true
console.log(email.indexOf("@"));     // 5      (position, ou -1 si absent)
console.log(email.replace("admin", "user")); // "user@example.com"
console.log(email.slice(0, 5));      // "admin" (extrait du caractère 0 à 4)
```

### `split` et `join` : découper et recoller

`split` transforme une chaîne en **tableau**, `join` fait l'inverse. Indispensables pour le parsing.

```javascript
const ligne = "8.8.8.8,google,53";
const champs = ligne.split(",");
console.log(champs);          // ["8.8.8.8", "google", "53"]
console.log(champs[0]);       // "8.8.8.8"

const ip = "192.168.1.1";
const octets = ip.split(".");
console.log(octets);          // ["192", "168", "1", "1"]
console.log(octets.length);   // 4

// join : recoller un tableau en chaîne
console.log(octets.join("-")); // "192-168-1-1"
```

### Les template strings (rappel)

```javascript
const host = "srv01";
const ip = "10.0.0.5";
console.log(`Hôte ${host} → ${ip}`);   // Hôte srv01 → 10.0.0.5
```

## Très utile en pratique : l'objet `URL`

Pour analyser une URL, **n'utilise pas `split` à la main** : c'est fragile et plein de cas particuliers. JavaScript fournit un objet natif **`URL`** qui fait le travail proprement.

```javascript
const u = new URL("https://example.com:8443/login?user=admin&lang=fr#section");

console.log(u.protocol);   // "https:"
console.log(u.hostname);   // "example.com"
console.log(u.port);       // "8443"
console.log(u.pathname);   // "/login"
console.log(u.search);     // "?user=admin&lang=fr"
console.log(u.hash);       // "#section"

// Lire les paramètres de requête proprement
console.log(u.searchParams.get("user"));  // "admin"
console.log(u.searchParams.get("lang"));   // "fr"
```

C'est bien plus fiable que de découper la chaîne soi-même : l'objet `URL` gère les ports, les paramètres, l'encodage, les cas tordus.

> ### ⚠️ À ne pas confondre : parsing manuel vs objet `URL`
> Découper une URL avec `split("/")` ou `split("?")` marche sur les cas simples mais **casse** dès qu'une URL est un peu inhabituelle. Pour extraire un domaine ou un paramètre, **utilise `new URL(...)`**. On le réutilisera avec `fetch` en Partie 5.

## Exemple simple

```javascript
function extraireDomaine(url) {
  return new URL(url).hostname;
}

console.log(extraireDomaine("https://www.example.com/path?x=1"));  // "www.example.com"
console.log(extraireDomaine("http://malveillant.test:8080/c2"));   // "malveillant.test"
```

## Application IT / cyber / OSINT

La manipulation de chaînes est le cœur de l'analyse défensive. Tu vas constamment : **normaliser** un IOC (`trim` + `toLowerCase` pour comparer des emails ou domaines sans casse), **découper** des lignes de log avec `split`, **extraire** un domaine ou un paramètre d'URL suspecte avec l'objet `URL`, **filtrer** des chaînes avec `includes` ou `startsWith`.

Exemple concret : pour comparer deux domaines en OSINT, il faut d'abord les normaliser (`"Example.COM"` et `"example.com"` sont le même domaine). Un oubli de normalisation fausse tous tes regroupements.

## ❌ Erreur classique

```javascript
// ❌ Croire qu'une méthode modifie la chaîne d'origine
let nom = "  admin  ";
nom.trim();              // renvoie "admin" mais ne modifie PAS nom
console.log(nom);        // "  admin  "  ← inchangé !

// ✅ CORRECT : récupérer le résultat
nom = nom.trim();
console.log(nom);        // "admin"

// ❌ Parser une URL à la main et se tromper
const url = "https://example.com:8443/path";
console.log(url.split("/")[2]);   // "example.com:8443"  ← le port est collé !

// ✅ CORRECT : utiliser URL
console.log(new URL(url).hostname);  // "example.com"
```

> **Réflexe diagnostic :** une transformation de texte « ne marche pas » ? Vérifie que tu **récupères** bien le résultat (`x = x.trim()`), car les chaînes sont immuables.

## Exercices

**Guidé**
1. À partir de `const brut = "  USER@Domain.COM  "`, produis la version normalisée en minuscules sans espaces.
2. Vérifie qu'elle contient `"@"`.
3. Extrais la partie après le `@` avec `split("@")`.

**Autonome**
Écris une fonction `extraireParam(url, nom)` qui renvoie la valeur d'un paramètre de requête d'une URL (utilise `new URL` et `searchParams.get`). Teste-la sur `"https://site.test/page?id=42&debug=true"` avec `"id"` puis `"debug"`.

**Défi**
À partir d'une ligne de log CSV `"2024-01-15,8.8.8.8,GET,/admin,403"`, découpe-la avec `split(",")`, et affiche une phrase lisible : `Le 2024-01-15, l'IP 8.8.8.8 a fait un GET sur /admin → 403`. Utilise une template string et les éléments du tableau.

## ✅ Tu sais maintenant…

- accéder à la longueur et aux caractères d'une chaîne ;
- comprendre que les chaînes sont immuables (récupérer le résultat) ;
- utiliser `trim`, `toLowerCase`, `toUpperCase`, `includes`, `startsWith`, `endsWith`, `replace`, `slice`, `indexOf` ;
- découper et recoller avec `split` et `join` ;
- parser une URL proprement avec `new URL(...)` et `searchParams`.

-----
