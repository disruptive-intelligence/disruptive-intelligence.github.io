---
title: 'Chapitre 24 — CORS : comprendre le blocage'
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Dès que tu feras des `fetch` dans le navigateur, tu rencontreras tôt ou tard une erreur **CORS**. Comprendre ce qu'elle signifie t'évitera des heures de confusion.

### Origine et politique same-origin

Une **origine** est le triplet `protocole + domaine + port` (ex. `https://example.com:443`). Par défaut, le navigateur applique la **politique same-origin** : une page ne peut, par défaut, lire des données que de **sa propre origine**.

### CORS : l'autorisation d'aller voir ailleurs

**CORS** (*Cross-Origin Resource Sharing*) est le mécanisme qui **assouplit** cette règle. Pour qu'une page sur `monsite.test` puisse lire les données de `api.autresite.test`, le **serveur d'`api.autresite.test`** doit explicitement l'autoriser via un en-tête de réponse :

```text
Access-Control-Allow-Origin: https://monsite.test
```


Si cet en-tête est absent ou ne correspond pas, le **navigateur bloque** la lecture et affiche une erreur CORS dans la console.

```text
Access to fetch at 'https://api.autresite.test/' from origin
'https://monsite.test' has been blocked by CORS policy
```


### Le point clé à comprendre

> ### ⚠️ À ne pas confondre : CORS n'est PAS une protection serveur
> CORS est une règle **appliquée par le navigateur**, pour protéger **l'utilisateur**. Ce n'est **pas** une sécurité côté serveur :
>
> - Un script **Node.js** (Partie 6), un outil comme `curl` ou Postman **ignorent CORS** : ils peuvent appeler l'API sans blocage. CORS ne s'applique **que dans le navigateur**.
> - Donc CORS **ne protège pas** une API contre des accès directs. Une API qui veut se protéger a besoin d'**authentification** côté serveur, pas de CORS.
>
> C'est le risque n° 7 de la Boîte à risques : croire que CORS sécurise une API. Il encadre seulement ce que **le navigateur d'un utilisateur** a le droit de lire depuis une autre origine.

## Très utile en pratique

Que faire face à une erreur CORS dans ton lab ?

- **Utiliser une API qui autorise le cross-origin** (beaucoup d'APIs publiques renvoient `Access-Control-Allow-Origin: *`).
- **Faire la requête depuis Node.js** au lieu du navigateur (pas de CORS) — souvent la meilleure option pour un outil d'analyse.
- Comprendre que tu **ne peux pas** « forcer » le navigateur à ignorer CORS depuis ton JavaScript : c'est le serveur distant qui décide.

## Exemple simple

```javascript
// Dans le NAVIGATEUR : peut être bloqué par CORS si l'API ne l'autorise pas
async function tester() {
  try {
    const r = await fetch("https://api.autresite.test/data");
    const data = await r.json();
    console.log(data);
  } catch (e) {
    // Une erreur CORS se manifeste souvent comme un échec de fetch ici
    console.log("Échec (possiblement CORS) :", e.message);
  }
}
```


## Application IT / cyber / OSINT

CORS est un sujet **clé en sécurité web**. Côté défensif, tu dois comprendre :

- qu'une **mauvaise configuration CORS** (par exemple `Access-Control-Allow-Origin: *` sur une API qui renvoie des données sensibles avec credentials) est une **faiblesse** réelle, relevée dans les audits ;
- que CORS protège l'utilisateur, **pas** le serveur — donc qu'on ne « contourne » pas une sécurité serveur en jouant avec CORS ;
- que pour tes **outils OSINT**, faire les requêtes depuis Node.js évite le problème entièrement.

Cette compréhension t'évite le contresens le plus fréquent des débutants en sécurité web, et prépare la suite « Web Security » de la collection.

## ❌ Erreur classique

```javascript
// ❌ Croire que c'est un bug de ton code
// → l'erreur CORS ne vient PAS d'une faute dans ton JavaScript :
//   c'est le serveur distant qui n'autorise pas ton origine.

// ❌ Croire que CORS protège l'API
// → un curl/Node atteint l'API quand même. CORS ≠ authentification.

// ❌ Chercher à "désactiver CORS" en JavaScript
// → impossible côté page : c'est le navigateur + le serveur distant qui décident.
```


> **Réflexe diagnostic :** erreur `blocked by CORS policy` ? Ce n'est pas ton code qui est faux : le serveur distant n'autorise pas ton origine. Soit l'API n'est pas faite pour un appel navigateur cross-origin, soit fais la requête depuis Node.js.

## Exercices

**Guidé**

1. Depuis une page locale, fais un `fetch` vers une API publique qui autorise CORS (ex. `https://api.ipify.org?format=json`) : ça marche.
2. Lis l'onglet *Réseau* des DevTools et repère l'en-tête `Access-Control-Allow-Origin` dans la réponse.

**Autonome**
Explique (en commentaires) pourquoi le même `fetch` pourrait échouer vers une autre API qui n'autorise pas le cross-origin, alors qu'il fonctionnerait depuis un script Node.js.

**Défi**
Rédige un mini-mémo défensif : qu'est-ce qu'une configuration CORS trop permissive, pourquoi `Access-Control-Allow-Origin: *` combiné à des données sensibles est risqué, et pourquoi CORS ne remplace jamais l'authentification serveur.

## ✅ Tu sais maintenant…

- définir une origine (protocole + domaine + port) ;
- expliquer la politique same-origin et le rôle de CORS ;
- comprendre que CORS est une règle **navigateur**, pas une sécurité serveur ;
- savoir qu'un script Node.js / curl ignore CORS ;
- diagnostiquer et contourner légitimement une erreur CORS dans ton lab.

-----

## 🧩 Mini-projet — Lookup OSINT dans le navigateur (chapitres 20 à 24)

Une page qui interroge une API publique et affiche le résultat **en sécurité**, avec gestion d'erreurs.

`index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
  <head><meta charset="UTF-8"><title>Lookup OSINT</title></head>
  <body>
    <h1>Mon IP publique</h1>
    <button id="lookup">Récupérer mon IP</button>
    <p id="resultat">—</p>
    <script src="script.js"></script>
  </body>
</html>
```


`script.js` :

```javascript
const bouton = document.querySelector("#lookup");
const resultat = document.querySelector("#resultat");

async function recupererIp() {
  resultat.textContent = "Chargement...";
  try {
    const reponse = await fetch("https://api.ipify.org?format=json");
    if (!reponse.ok) {
      throw new Error(`HTTP ${reponse.status}`);
    }
    const data = await reponse.json();
    // ✅ textContent : aucune injection possible même si la réponse était piégée
    resultat.textContent = `Votre IP publique : ${data.ip}`;
  } catch (erreur) {
    resultat.textContent = `Erreur : ${erreur.message}`;
  }
}

bouton.addEventListener("click", recupererIp);
```


**Ce que tu obtiens :** un bouton qui interroge une API réelle, affiche un état de chargement, le résultat en `textContent`, et un message d'erreur propre en cas de panne réseau. Tout y est : `async/await`, vérification du statut, `try/catch`, affichage sécurisé, événement.

Ce mini-projet mobilise toute la Partie 5 (asynchrone, `fetch`, `async/await`, gestion d'erreurs) plus le DOM et les événements (Partie 3) et le réflexe `textContent` (sécurité).

**Pour aller plus loin :** ajoute un champ pour saisir une IP et interroge une API de géolocalisation/réputation qui autorise CORS ; affiche pays et score. Pense à gérer le cas où l'API échoue ou est bloquée par CORS.

-----

## ✅ CHECKPOINT 5 — Tu sais faire parler une page au réseau

Avant la Partie 6, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer synchrone vs asynchrone et le « plus tard » ;
- [ ] lire une chaîne de `.then`/`.catch` ;
- [ ] faire un `fetch`, lire `.json()`, vérifier `reponse.ok` ;
- [ ] écrire la même chose en `async`/`await` avec `try/catch` ;
- [ ] expliquer que `fetch` diffère navigateur vs Node.js (CORS) ;
- [ ] expliquer ce qu'est CORS et pourquoi ce n'est pas une sécurité serveur ;
- [ ] réaliser le mini-projet lookup OSINT.

Tu sais interroger le web côté navigateur. La Partie 6 quitte le navigateur pour Node.js : enfin le scripting d'automatisation, proche de Python.


-----
