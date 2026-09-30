---
title: Chapitre 22 — fetch et requêtes HTTP
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 22
chapters: 35
---

## Le minimum à savoir

**`fetch`** est la fonction moderne pour faire des requêtes HTTP : récupérer des données d'un serveur ou d'une API. Elle renvoie une **promesse**.

### Une requête GET de base

```javascript
fetch("https://api.exemple.test/ip/8.8.8.8")
  .then((reponse) => reponse.json())   // convertir la réponse en objet (JSON)
  .then((donnees) => console.log(donnees))
  .catch((erreur) => console.log("Erreur réseau :", erreur.message));
```

Deux étapes :
1. `fetch(url)` renvoie une promesse de **réponse**.
2. `reponse.json()` lit le corps et le parse en objet JavaScript (renvoie elle aussi une promesse).

### Vérifier le statut HTTP

`fetch` ne considère **pas** un code 404 ou 500 comme une erreur (la promesse réussit quand même). Il faut vérifier `reponse.ok` ou `reponse.status` soi-même.

```javascript
fetch("https://api.exemple.test/data")
  .then((reponse) => {
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);   // 404, 500...
    }
    return reponse.json();
  })
  .then((data) => console.log(data))
  .catch((err) => console.log("Problème :", err.message));
```

- **`reponse.ok`** : `true` si le statut est 200-299.
- **`reponse.status`** : le code numérique (200, 404, 500…).

> ### 🛡️ Réflexe sécurité : toujours gérer l'échec réseau
> Une requête peut échouer : serveur injoignable, timeout, 500, hors-ligne. **Sans `.catch` (ou `try/catch`), ton appli casse silencieusement ou affiche des données incohérentes.** C'est le risque n° 11 de la Boîte à risques. Et n'injecte **jamais** la réponse via `innerHTML` (risque XSS) : utilise `textContent` (chapitre 15).

## Très utile en pratique

> ### 🧭 Navigateur vs Node.js : `fetch` n'est pas identique partout
> `fetch` existe **dans le navigateur** ET **dans Node.js moderne** (Node 18+). Le code se ressemble, mais **le contexte diffère** :
>
> - **Dans le navigateur**, `fetch` est soumis à **CORS** (chapitre suivant) : le navigateur peut **bloquer** une requête vers un autre domaine. C'est une règle **du navigateur**.
> - **Dans un script Node.js classique**, il **n'y a pas de navigateur, donc pas de CORS** : `fetch` vers n'importe quel domaine n'est pas bloqué de la même façon.
>
> Conséquence pratique : un `fetch` qui « marche » dans un script Node peut être **bloqué par CORS** dans le navigateur, et inversement. Quand tu vois une erreur CORS, c'est que tu es **dans le navigateur**. On détaille au chapitre 24.

## Exemple simple

Récupérer son IP publique via une API (l'exemple `ipify` renvoie `{"ip": "..."}`) :

```javascript
fetch("https://api.ipify.org?format=json")
  .then((r) => r.json())
  .then((data) => {
    console.log("Mon IP publique :", data.ip);
  })
  .catch((err) => console.log("Impossible de récupérer l'IP :", err.message));
```

## Application IT / cyber / OSINT

`fetch` est la porte vers toutes les **APIs de cybersécurité** : réputation d'IP, résolution de domaines, threat intelligence, enrichissement d'IOC. Le geste type est : `fetch` une API → vérifier le statut → `.json()` → traiter avec `filter`/`map` → afficher en `textContent`. C'est le cœur du mini-projet « lookup OSINT » de cette partie. La gestion d'erreurs réseau (`.catch`) n'est pas optionnelle : les services externes sont parfois lents, en panne, ou limités en débit.

> ### 🔍 Lecture de code inconnu
> Repérer les appels `fetch` (ou `XMLHttpRequest`) dans un script inconnu te révèle **avec quels serveurs il communique** et **quelles données il envoie/reçoit**. C'est souvent l'information la plus importante pour comprendre le comportement réseau d'une page.

## ❌ Erreur classique

```javascript
// ❌ Oublier .json() et utiliser la réponse brute
fetch(url).then((r) => console.log(r.ip));   // undefined ! r est la réponse, pas les données

// ✅ Lire le corps avec .json()
fetch(url).then((r) => r.json()).then((data) => console.log(data.ip));

// ❌ Croire que fetch rejette sur 404/500
fetch("https://site.test/page-inexistante")
  .then((r) => r.json())   // s'exécute même sur un 404 ! r.ok serait false
  .catch(...);             // ne se déclenche PAS pour un 404

// ✅ Vérifier r.ok soi-même
fetch(url).then((r) => {
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
});
```

> **Réflexe diagnostic :** `fetch` « réussit » mais tes données sont vides/fausses ? Vérifie que tu appelles bien `.json()`, et que tu testes `r.ok` (un 404 passe le `.then` sans déclencher `.catch`).

## Exercices

**Guidé**
1. Fais un `fetch` vers `https://api.ipify.org?format=json`.
2. Convertis en JSON avec `.json()`.
3. Affiche l'IP. Ajoute un `.catch` qui affiche l'erreur.

**Autonome**
Écris une fonction `recupererIp()` qui fait le `fetch` ci-dessus et affiche l'IP dans un élément `#resultat` de la page avec `textContent` (pas `innerHTML`). Branche-la sur un bouton.

**Défi**
Écris une fonction `requeteSafe(url)` qui fait un `fetch`, vérifie `r.ok` (sinon `throw`), renvoie le JSON, et gère toute erreur dans un `.catch` en affichant un message propre. Teste-la avec une URL valide et une URL volontairement cassée.

## ✅ Tu sais maintenant…

- faire une requête GET avec `fetch` ;
- lire le corps avec `.json()` ;
- vérifier `reponse.ok` et `reponse.status` ;
- gérer l'échec réseau avec `.catch` ;
- comprendre que `fetch` diffère navigateur vs Node.js (CORS) ;
- ne jamais injecter une réponse via `innerHTML`.

-----
