---
title: Chapitre 15 — Modifier le DOM en sécurité (textContent vs innerHTML)
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Une fois un élément sélectionné, tu peux **modifier** son contenu, ses attributs, ses classes. Et c'est ici qu'apparaît **la première grande question de sécurité** du cours.

### Modifier le texte : `textContent`

```javascript
const titre = document.querySelector("#statut");
titre.textContent = "Analyse terminée";   // remplace le texte affiché
```


`textContent` traite ce que tu mets comme du **texte pur**. Même si la valeur contient `<script>`, ce sera affiché tel quel, jamais exécuté. **C'est sûr.**

### Modifier le HTML : `innerHTML` (à manier avec précaution)

```javascript
const zone = document.querySelector("#zone");
zone.innerHTML = "<strong>Important</strong>";   // interprété comme du HTML
```


`innerHTML` **interprète** la valeur comme du HTML. C'est puissant, mais **dangereux** si la valeur contient une donnée non maîtrisée.

> ### 🛡️ Réflexe sécurité (CRUCIAL) : `textContent` vs `innerHTML`
> C'est **le** réflexe de sécurité côté client le plus important du cours.
>
> - Pour afficher une **donnée** (surtout venant d'un utilisateur, d'une URL, d'une API) → **`textContent`**, toujours.
> - **`innerHTML`** seulement avec du HTML que **tu** contrôles entièrement, jamais avec une donnée externe.
>
> **Pourquoi ?** Si tu fais `element.innerHTML = donneeUtilisateur` et que cette donnée contient `<img src=x onerror="vol_de_cookies()">`, le navigateur **exécute** ce code. C'est une faille **XSS** (*Cross-Site Scripting*), plus précisément un **DOM XSS** quand c'est ton JavaScript qui injecte la donnée. C'est le risque n° 1 et n° 13 de la Boîte à risques.

### Démonstration de la faille (à des fins défensives)

```javascript
const saisieUtilisateur = '<img src=x onerror="alert(\'XSS\')">';
const zone = document.querySelector("#zone");

// ☠️ DANGEREUX : le code dans la saisie s'exécute
zone.innerHTML = saisieUtilisateur;   // déclenche l'alerte → faille XSS

// ✅ SÛR : la saisie est affichée comme texte, le code ne s'exécute pas
zone.textContent = saisieUtilisateur; // affiche littéralement le texte <img ...>
```


### Modifier classes et attributs

```javascript
const el = document.querySelector("#statut");

el.classList.add("alerte");        // ajoute une classe CSS
el.classList.remove("normal");     // retire une classe
el.classList.toggle("visible");    // bascule (ajoute/retire)

el.setAttribute("data-ip", "8.8.8.8");   // définir un attribut
```


## Très utile en pratique

Afficher un résultat d'analyse **en sécurité** :

```javascript
function afficherResultat(message) {
  const zone = document.querySelector("#resultat");
  zone.textContent = message;        // ✅ textContent : pas d'injection possible
  zone.classList.add("termine");
}

afficherResultat("3 IP suspectes détectées");
```


## Exemple simple

```html
<body>
  <p id="sortie">...</p>
  <script src="script.js"></script>
</body>
```


```javascript
const sortie = document.querySelector("#sortie");
const ip = "8.8.8.8";
sortie.textContent = `Dernière IP analysée : ${ip}`;
```


## Application IT / cyber / OSINT

Comprendre `textContent` vs `innerHTML` n'est pas qu'une bonne pratique : c'est **comprendre comment naît une faille web côté client**. En sécurité web défensive (la suite de cette collection), l'XSS est l'une des vulnérabilités les plus répandues. Savoir que `innerHTML` + donnée non maîtrisée = injection te permet, en tant qu'analyste, de **repérer** ce motif dangereux dans le code d'une application, et de comprendre les rapports de vulnérabilité. C'est aussi la base pour construire des outils web (inspecteur d'IOC) qui n'introduisent pas eux-mêmes de faille.

> ### 🔍 Lecture de code inconnu
> Dans un script inconnu, repère **chaque usage de `innerHTML`** : c'est un point chaud potentiel de XSS, surtout si la valeur vient d'une URL, d'un champ ou d'une API.

## ❌ Erreur classique

```javascript
// ❌ LA grande erreur : innerHTML avec une donnée utilisateur
const recherche = new URL(location.href).searchParams.get("q");
zone.innerHTML = recherche;   // ☠️ DOM XSS si q contient du HTML/JS malveillant

// ✅ CORRECT : textContent
zone.textContent = recherche;

// ❌ Utiliser eval (jamais, sous aucun prétexte)
// eval(codeUtilisateur);   // ☠️ exécution arbitraire — risque n°2

// ❌ Croire que textContent "casse" l'affichage du HTML voulu
// → si tu veux VRAIMENT du HTML que TU contrôles, innerHTML est ok ;
//   le danger est uniquement avec des données EXTERNES.
```


> **Réflexe sécurité résumé :** *donnée externe → `textContent`. HTML que je contrôle → `innerHTML` possible. Jamais d'`eval`.*

## Exercices

**Guidé**

1. Crée une page avec `<p id="sortie">`.
2. Mets-y un texte avec `textContent`.
3. Essaie ensuite `innerHTML = "<strong>Gras</strong>"` et observe la différence d'affichage.

**Autonome**
Crée une fonction `afficher(message)` qui met le message dans `#sortie` avec `textContent` et ajoute la classe `"affiche"`. Teste avec un message contenant `<b>` et vérifie qu'il s'affiche **littéralement** (preuve que c'est sûr).

**Défi**
Mets côte à côte deux zones : une qui affiche une saisie avec `innerHTML`, l'autre avec `textContent`. Passe la chaîne `"<img src=x onerror=console.log('XSS')>"`. Observe dans la console que la version `innerHTML` déclenche le code et pas la version `textContent`. Rédige en commentaire pourquoi, en deux phrases. *(But pédagogique défensif : comprendre la faille pour l'éviter.)*

## ✅ Tu sais maintenant…

- modifier le texte avec `textContent` (sûr) ;
- comprendre que `innerHTML` interprète le HTML (puissant mais risqué) ;
- expliquer le mécanisme d'un DOM XSS ;
- appliquer la règle « donnée externe → `textContent` » ;
- manipuler classes (`classList`) et attributs (`setAttribute`) ;
- proscrire `eval`.

-----
