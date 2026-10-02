---
title: Chapitre 17 — Formulaires et limites de la validation côté client
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Un **formulaire** regroupe des champs et un bouton d'envoi. JavaScript peut lire les valeurs, réagir à l'envoi, et **valider** la saisie.

```html
<form id="recherche">
  <input id="terme" placeholder="Terme à chercher">
  <button type="submit">Chercher</button>
</form>
<p id="sortie"></p>
<script src="script.js"></script>
```


```javascript
const form = document.querySelector("#recherche");
const terme = document.querySelector("#terme");
const sortie = document.querySelector("#sortie");

form.addEventListener("submit", (event) => {
  event.preventDefault();   // ⚠️ empêche le rechargement de la page
  const valeur = terme.value.trim();
  sortie.textContent = `Recherche : ${valeur}`;   // ✅ textContent
});
```


### `event.preventDefault()` : le réflexe formulaire

Par défaut, envoyer un formulaire **recharge la page**. Pour traiter la saisie en JavaScript sans rechargement, on appelle `event.preventDefault()` au début du callback `submit`. Sans ça, ton code semble « ne rien faire » car la page se recharge aussitôt.

### Valider une saisie

```javascript
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const valeur = terme.value.trim();

  if (valeur === "") {
    sortie.textContent = "⚠️ Le champ est vide";
    return;
  }
  if (valeur.length < 3) {
    sortie.textContent = "⚠️ Au moins 3 caractères";
    return;
  }

  sortie.textContent = `Recherche valide : ${valeur}`;
});
```


## Très utile en pratique

La validation côté client améliore l'**expérience** : retour immédiat, messages clairs, moins d'erreurs. Mais elle a une limite fondamentale, qui est une notion de sécurité majeure.

> ### 🛡️ Réflexe sécurité (MAJEUR) : la validation côté client ne protège RIEN
> La validation JavaScript dans le navigateur sert **uniquement au confort de l'utilisateur**. Elle **ne sécurise rien**, car :
>
> - l'utilisateur peut **désactiver JavaScript** ;
> - l'utilisateur peut **modifier ton code** dans les DevTools ;
> - l'utilisateur peut envoyer une requête **directement au serveur**, en contournant totalement ta page (avec `curl`, Postman, etc.).
>
> **Seule la validation côté serveur protège réellement.** C'est le risque n° 3 de la Boîte à risques. Corollaire (risque n° 8) : **masquer ou désactiver un bouton côté frontend n'interdit pas l'action** — quelqu'un peut toujours appeler l'opération directement. Le frontend, c'est l'expérience ; le serveur, c'est la sécurité.

## Exemple simple

```javascript
const form = document.querySelector("#form-ip");
const champ = document.querySelector("#champ-ip");
const sortie = document.querySelector("#sortie");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const ip = champ.value.trim();
  const valide = /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip);
  sortie.textContent = valide ? `IP acceptée : ${ip}` : "Format d'IP invalide";
});
```


## Application IT / cyber / OSINT

Cette notion est **centrale en sécurité web**. Un pentester ou un analyste SOC ne fait **jamais** confiance au frontend : il sait que toute validation, tout contrôle d'accès, toute logique implémentée uniquement côté navigateur peut être contournée. Comprendre cela te protège de l'erreur de conception la plus répandue : croire qu'un contrôle côté client est une barrière de sécurité. C'est aussi ce qui rend tant d'applications vulnérables — et ce que tu apprendras à repérer dans la suite « Web Security » de cette collection.

## ❌ Erreur classique

```javascript
// ❌ Oublier preventDefault → la page se recharge, ton code "ne fait rien"
form.addEventListener("submit", () => {
  sortie.textContent = "traité";   // disparaît aussitôt : la page recharge
});

// ✅ CORRECT
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sortie.textContent = "traité";
});

// ❌ Croire que la validation client sécurise
// if (motDePasse === "admin") { donnerAcces(); }
// ☠️ Tout est côté client : trivialement contournable. La sécurité est au serveur.
```


> **Réflexe diagnostic :** ton formulaire « clignote » ou se vide à l'envoi ? Tu as oublié `event.preventDefault()`.

## Exercices

**Guidé**

1. Crée un formulaire avec un champ et un bouton d'envoi.
2. Au `submit`, empêche le rechargement et affiche la valeur saisie.
3. Refuse les valeurs vides avec un message.

**Autonome**
Crée un formulaire qui valide un email côté client (présence de `@` et d'un `.`) et affiche « valide » ou « invalide ». Ajoute **en commentaire** une phrase rappelant que cette validation ne remplace pas celle du serveur.

**Défi**
Crée un formulaire « ajouter une IP à surveiller » : il valide le format IPv4, refuse les doublons (garde les IP dans un tableau JavaScript), et affiche la liste à jour avec `textContent`. Réfléchis : qu'est-ce qui empêcherait quelqu'un de contourner ta validation ? (Réponse en commentaire : rien, côté client — d'où la nécessité du serveur.)

## ✅ Tu sais maintenant…

- lire les champs d'un formulaire et réagir au `submit` ;
- empêcher le rechargement avec `event.preventDefault()` ;
- valider une saisie côté client pour le confort ;
- expliquer pourquoi la validation client ne sécurise rien ;
- expliquer pourquoi masquer un bouton ne protège pas une action.

-----

## 🧩 Mini-projet — Inspecteur d'IOC dans une page (chapitres 14 à 17)

Rassemble la Partie 3. Une page où l'on colle du texte et qui en extrait les IOC, affichés **en sécurité**.

`index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
  <head><meta charset="UTF-8"><title>Inspecteur d'IOC</title></head>
  <body>
    <h1>Inspecteur d'IOC</h1>
    <textarea id="entree" rows="8" cols="60" placeholder="Collez un texte (logs, rapport...)"></textarea>
    <br>
    <button id="analyser">Analyser</button>
    <h2>IP trouvées</h2>
    <ul id="liste-ip"></ul>
    <h2>Résumé</h2>
    <p id="resume"></p>
    <script src="script.js"></script>
  </body>
</html>
```


`script.js` :

```javascript
const entree = document.querySelector("#entree");
const bouton = document.querySelector("#analyser");
const listeIp = document.querySelector("#liste-ip");
const resume = document.querySelector("#resume");

const RE_IP = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g;

bouton.addEventListener("click", () => {
  const texte = entree.value;

  // Extraire et dédoublonner les IP
  const ipsTrouvees = texte.match(RE_IP) || [];
  const ipsUniques = [...new Set(ipsTrouvees)];

  // Vider la liste précédente
  listeIp.textContent = "";

  // Afficher chaque IP EN SÉCURITÉ (textContent, jamais innerHTML)
  for (const ip of ipsUniques) {
    const li = document.createElement("li");
    li.textContent = ip;          // ✅ textContent : pas d'injection possible
    listeIp.appendChild(li);
  }

  // Résumé
  resume.textContent =
    `${ipsTrouvees.length} IP au total, ${ipsUniques.length} uniques.`;
});
```


**Ce que tu obtiens :** colle un bloc de logs, clique « Analyser », et la page liste les IP uniques + un résumé. Chaque IP est insérée avec `textContent` et `createElement` — **jamais** `innerHTML` —, ce qui rend l'outil immunisé contre une injection même si le texte collé contient du HTML piégé.

Ce mini-projet mobilise : DOM (`querySelector`, `createElement`, `appendChild`), `textContent` (réflexe sécurité), événements (`click`), regex et `Set` (Partie 2). C'est un vrai petit outil d'analyste, construit proprement.

**Pour aller plus loin :** ajoute l'extraction des emails et des hash (deuxièmes regex), avec leurs propres listes.

-----

## ✅ CHECKPOINT 3 — Tu sais manipuler une page et tu connais le réflexe XSS

Avant la Partie 4, assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer ce qu'est le DOM et sélectionner avec `querySelector` ;
- [ ] modifier le contenu avec `textContent` et savoir pourquoi pas `innerHTML` sur des données externes ;
- [ ] expliquer le mécanisme d'un DOM XSS ;
- [ ] manipuler classes et attributs ;
- [ ] réagir à un événement avec `addEventListener` ;
- [ ] gérer un formulaire avec `event.preventDefault()` ;
- [ ] expliquer pourquoi la validation client ne sécurise rien ;
- [ ] réaliser le mini-projet inspecteur d'IOC.

Tu sais faire vivre une page **en sécurité**. La Partie 4 aborde le stockage de données dans le navigateur — et les pièges de sécurité associés.


-----
