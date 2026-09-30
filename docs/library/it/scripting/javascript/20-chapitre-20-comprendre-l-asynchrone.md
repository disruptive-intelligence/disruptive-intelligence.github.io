---
title: Chapitre 20 — Comprendre l'asynchrone
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 20
chapters: 35
---

## Le minimum à savoir

C'est **le concept le plus important et le plus déroutant** de JavaScript. On l'aborde en douceur, avec l'idée avant la syntaxe.

### Synchrone vs asynchrone

Jusqu'ici, ton code s'exécutait **dans l'ordre, ligne par ligne** : c'est **synchrone**.

```javascript
console.log("1");
console.log("2");
console.log("3");
// affiche 1, 2, 3 dans l'ordre
```

Mais certaines opérations prennent du **temps** : interroger un serveur, lire un fichier, attendre. JavaScript ne **bloque pas** en les attendant — il continue, et traite le résultat **plus tard**. C'est **asynchrone**.

```javascript
console.log("Début");

setTimeout(() => {
  console.log("Plus tard (après 1 seconde)");
}, 1000);

console.log("Fin");

// Affiche :
// Début
// Fin
// Plus tard (après 1 seconde)   ← arrive APRÈS, même si écrit avant "Fin" dans le code !
```

`setTimeout(fonction, ms)` exécute la fonction **après** un délai, sans bloquer le reste. C'est l'illustration la plus simple du « plus tard ».

### Le callback : « fais ça quand ce sera prêt »

La fonction qu'on donne à `setTimeout` (ou à `addEventListener`) est un **callback** : du code à exécuter quand un événement futur se produit. Tu en as déjà utilisé avec les événements (chapitre 16). L'asynchrone généralise cette idée à tout ce qui « prend du temps ».

> ### ⚠️ À ne pas confondre : ordre d'écriture vs ordre d'exécution
> En asynchrone, **l'ordre des lignes dans ton code n'est pas l'ordre d'exécution**. Ce qui est « différé » (réseau, `setTimeout`) s'exécute après le code synchrone qui suit. C'est la source n° 1 de confusion des débutants. Garde en tête : *le réseau et les timers arrivent « plus tard »*.

## Très utile en pratique

Pourquoi c'est nécessaire : imagine que demander une page au serveur prenne 2 secondes. Si JavaScript **bloquait** pendant ces 2 secondes, toute la page se figerait (boutons inertes, scroll bloqué). L'asynchrone permet à l'interface de **rester réactive** pendant que la requête voyage. C'est indispensable pour le web.

## Exemple simple

```javascript
console.log("Lancement de l'analyse...");

setTimeout(() => {
  console.log("Analyse terminée (résultat reçu)");
}, 2000);

console.log("L'interface reste utilisable pendant l'attente");
```

## Application IT / cyber / OSINT

Toute interaction réseau est asynchrone : interroger une API de threat intel, télécharger une liste d'IOC, vérifier une réputation d'IP. Comprendre l'asynchrone est le préalable indispensable à `fetch` (chapitre 22). Sans ce modèle mental, le code réseau paraît « se comporter dans le désordre ». Avec lui, tu écris des outils qui interrogent des services distants sans figer l'interface.

## ❌ Erreur classique

```javascript
// ❌ Croire qu'on récupère un résultat asynchrone tout de suite
let resultat;
setTimeout(() => { resultat = "données"; }, 1000);
console.log(resultat);   // undefined ! (le callback n'a pas encore tourné)

// ✅ Utiliser le résultat DANS le callback, là où il est disponible
setTimeout(() => {
  const resultat = "données";
  console.log(resultat);   // "données"
}, 1000);
```

> **Réflexe diagnostic :** une variable est `undefined` juste après une opération asynchrone ? Normal : le résultat n'est pas encore là. Il faut le traiter **dans** le callback (ou avec `await`, chapitre 23), pas sur la ligne suivante.

## Exercices

**Guidé**
1. Affiche `"A"`, puis programme un `setTimeout` de 1 s qui affiche `"C"`, puis affiche `"B"` après le `setTimeout`.
2. Prédis l'ordre d'affichage avant d'exécuter, puis vérifie (A, B, C).

**Autonome**
Programme trois `setTimeout` à 500 ms, 1000 ms et 1500 ms qui affichent `"étape 1/2/3"`. Vérifie qu'ils s'affichent dans l'ordre des délais.

**Défi**
Sans utiliser de variable globale, écris une fonction `simulerRequete(callback)` qui, après 1 s (`setTimeout`), appelle `callback` avec un objet `{ip: "8.8.8.8", score: 10}`. Appelle-la et affiche le score **dans** le callback. Tu viens de reproduire le schéma d'une requête asynchrone.

## ✅ Tu sais maintenant…

- distinguer code synchrone et asynchrone ;
- comprendre que certaines opérations s'exécutent « plus tard » ;
- utiliser `setTimeout` pour illustrer le différé ;
- comprendre le rôle d'un callback ;
- distinguer ordre d'écriture et ordre d'exécution.

-----
