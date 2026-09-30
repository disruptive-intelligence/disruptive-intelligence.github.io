---
title: Chapitre 30 — XSS et DOM XSS expliqués
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Le **XSS** (*Cross-Site Scripting*) est l'une des vulnérabilités web les plus répandues. On l'a effleuré au chapitre 15 ; on le pose ici clairement, **à des fins défensives** : comprendre la faille pour l'éviter et la reconnaître.

### Le principe

Un XSS survient quand une page web **insère une donnée non maîtrisée** (venant d'un utilisateur, d'une URL, d'une API) **dans le HTML de la page**, de telle sorte que cette donnée est **interprétée comme du code** plutôt que comme du texte. L'attaquant fait alors exécuter **son** JavaScript dans le navigateur de la victime.

```javascript
// La donnée vient de l'utilisateur (ici, d'un paramètre d'URL)
const recherche = new URL(location.href).searchParams.get("q");

// ☠️ FAILLE : innerHTML interprète la donnée comme du HTML
document.querySelector("#resultat").innerHTML = `Résultats pour : ${recherche}`;
```


Si l'URL est `...?q=<img src=x onerror="...">`, le code dans `onerror` **s'exécute**. L'attaquant peut alors voler des cookies (s'ils ne sont pas `HttpOnly`), lire le LocalStorage, agir au nom de la victime, etc.

### Les grandes familles de XSS

| Type | Où la donnée malveillante transite |
| --- | --- |
| **XSS réfléchi** | dans la requête (URL, formulaire) ; renvoyée immédiatement par le serveur dans la page. |
| **XSS stocké** | enregistrée côté serveur (ex. un commentaire), puis affichée à d'autres victimes. |
| **DOM XSS** | entièrement côté client : c'est **ton JavaScript** qui insère la donnée dans le DOM (cas ci-dessus). |

Le **DOM XSS** est celui qui te concerne le plus directement quand tu écris du JavaScript : il ne dépend pas du serveur, mais de la façon dont **ton code** manipule le DOM.

## Très utile en pratique : les défenses

> ### 🛡️ Réflexe sécurité : éviter le XSS côté client
> 1. **Affiche les données avec `textContent`, jamais `innerHTML`** (chapitre 15). C'est la défense n° 1 du DOM XSS. `textContent` n'interprète jamais le contenu comme du code.
> 2. **N'utilise jamais `eval`** ni équivalents (`new Function`, `setTimeout("code en string")`). `eval` exécute du texte comme du code : risque n° 2 de la Boîte à risques.
> 3. **Méfie-toi des sources de données non maîtrisées** : paramètres d'URL (`location`, `searchParams`), champs de formulaire, réponses d'API, `postMessage`, `document.referrer`.
> 4. **Si tu dois vraiment produire du HTML**, échappe la donnée ou utilise une bibliothèque d'assainissement reconnue — mais pour un débutant, la règle simple « `textContent` » suffit dans l'immense majorité des cas.

### Démonstration défensive (les deux versions côte à côte)

```javascript
const donnee = '<img src=x onerror="console.log(\'code exécuté\')">';

// ☠️ VULNÉRABLE : le code de la donnée s'exécute
zoneA.innerHTML = donnee;

// ✅ SÛR : la donnée est affichée littéralement, jamais exécutée
zoneB.textContent = donnee;
```


## Exemple simple

```javascript
// Affichage sûr d'un paramètre d'URL
const terme = new URL(location.href).searchParams.get("q") || "";
document.querySelector("#titre").textContent = `Recherche : ${terme}`;
// Même si q contient du HTML, il s'affiche comme texte. Pas de XSS.
```


## Application IT / cyber / OSINT

Le XSS est au cœur de la sécurité web. Pour un profil défensif :

- **En revue de code**, tu repères les `innerHTML`, `eval`, et l'insertion de données non maîtrisées : ce sont les points chauds.
- **En analyse**, comprendre le XSS t'aide à lire les rapports de vulnérabilité et à évaluer la gravité d'une faille.
- **En tant que développeur d'outils**, tu construis des interfaces (comme l'inspecteur d'IOC) qui n'introduisent pas elles-mêmes de faille.

C'est aussi la porte d'entrée vers la suite « Web Security » de la collection, où le XSS est étudié en profondeur (toujours dans un cadre légal et défensif).

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, le trio **`innerHTML` + donnée externe + absence d'échappement** est le motif de DOM XSS à repérer en priorité. De même, tout `eval` est un signal d'alarme.

## ❌ Erreur classique

```javascript
// ❌ Insérer une donnée externe via innerHTML
el.innerHTML = donneeApi.nom;          // ☠️ XSS si nom contient du HTML/JS

// ✅ textContent
el.textContent = donneeApi.nom;

// ❌ Construire du HTML "à la main" avec des données
el.innerHTML = "<p>" + saisie + "</p>"; // ☠️ même problème

// ✅ Créer les éléments et remplir le texte
const p = document.createElement("p");
p.textContent = saisie;                 // ✅
el.appendChild(p);
```


> **Réflexe diagnostic :** dès que tu écris `.innerHTML =`, demande-toi : « cette valeur peut-elle contenir une donnée que je ne contrôle pas ? » Si oui → `textContent` ou création d'éléments.

## Exercices

**Guidé**

1. Crée une page qui lit le paramètre `?q=` de l'URL et l'affiche avec `textContent`.
2. Teste avec `?q=bonjour`, puis `?q=<b>test</b>` : observe qu'il s'affiche littéralement (sûr).

**Autonome**
Reprends ton inspecteur d'IOC (Partie 3). Vérifie qu'aucune donnée n'est insérée via `innerHTML`. Documente en commentaire pourquoi chaque insertion est sûre.

**Défi**
Crée une mini-démo pédagogique à deux zones : l'une affiche une saisie via `innerHTML`, l'autre via `textContent`. Passe une charge utile inoffensive (`<img src=x onerror=console.log('demo')>`) et observe dans la console que seule la version `innerHTML` l'exécute. Rédige une explication de 3 lignes du mécanisme et de la défense. *(But strictement défensif et pédagogique.)*

## ✅ Tu sais maintenant…

- expliquer le principe du XSS (donnée interprétée comme code) ;
- distinguer XSS réfléchi, stocké et DOM XSS ;
- appliquer la défense n° 1 : `textContent` plutôt qu'`innerHTML` ;
- proscrire `eval` et identifier les sources non maîtrisées ;
- repérer le motif de DOM XSS dans du code.

-----
