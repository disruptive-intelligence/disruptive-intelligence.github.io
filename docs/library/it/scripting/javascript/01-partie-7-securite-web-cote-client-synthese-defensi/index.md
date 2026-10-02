---
title: 'Partie 7 — Sécurité web côté client : synthèse défensive'
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
---

30. XSS et DOM XSS expliqués
31. CSP, en-têtes et défenses navigateur
32. Le réflexe fondamental : le client n'est jamais de confiance
33. Lire un script JavaScript inconnu

## Synthèse finale & cheat-sheets

## Annexes

- A — `var`, hoisting, `this`, prototypes
- B — TypeScript
- C — Frameworks front (React, Vue, Angular, Next.js)
- D — Outillage moderne (Vite, bundlers)
- E — Express / backend
- F — Pont vers la suite cyber (Web Security, bug bounty débutant, OSINT tooling)

-----

## Dans cette partie

- [Chapitre 1 — Découverte de JavaScript et premier code](01-chapitre-1-decouverte-de-javascript-et-premier-cod.md)
- [Chapitre 2 — Console, fichier .js et page minimale](02-chapitre-2-console-fichier-js-et-page-minimale.md)
- [Chapitre 3 — Variables et types](03-chapitre-3-variables-et-types.md)
- [Chapitre 4 — Opérateurs, comparaisons et logique](04-chapitre-4-operateurs-comparaisons-et-logique.md)
- [Chapitre 5 — Conditions](05-chapitre-5-conditions.md)
- [Chapitre 6 — Boucles](06-chapitre-6-boucles.md)
- [Chapitre 7 — Fonctions](07-chapitre-7-fonctions.md)
- [Chapitre 8 — Chaînes de caractères et l'objet URL](08-chapitre-8-chaines-de-caracteres-et-l-objet-url.md)
- [Chapitre 9 — Regex simples pour OSINT / SOC](09-chapitre-9-regex-simples-pour-osint-soc.md)
- [Chapitre 10 — Tableaux et méthodes utiles](10-chapitre-10-tableaux-et-methodes-utiles.md)
- [Chapitre 11 — Objets](11-chapitre-11-objets.md)
- [Chapitre 12 — JSON](12-chapitre-12-json.md)
- [Chapitre 13 — Erreurs, exceptions et débogage](13-chapitre-13-erreurs-exceptions-et-debogage.md)
- [Chapitre 14 — Le DOM : comprendre et sélectionner](14-chapitre-14-le-dom-comprendre-et-selectionner.md)
- [Chapitre 15 — Modifier le DOM en sécurité (textContent vs innerHTML)](15-chapitre-15-modifier-le-dom-en-securite-textconten.md)
- [Chapitre 16 — Événements](16-chapitre-16-evenements.md)
- [Chapitre 17 — Formulaires et limites de la validation côté client](17-chapitre-17-formulaires-et-limites-de-la-validatio.md)
- [Chapitre 18 — LocalStorage et SessionStorage](18-chapitre-18-localstorage-et-sessionstorage.md)
- [Chapitre 19 — Cookies et les limites de JavaScript](19-chapitre-19-cookies-et-les-limites-de-javascript.md)
- [Chapitre 20 — Comprendre l'asynchrone](20-chapitre-20-comprendre-l-asynchrone.md)
- [Chapitre 21 — Promesses](21-chapitre-21-promesses.md)
- [Chapitre 22 — fetch et requêtes HTTP](22-chapitre-22-fetch-et-requetes-http.md)
- [Chapitre 23 — async / await](23-chapitre-23-async-await.md)
- [Chapitre 24 — CORS : comprendre le blocage](24-chapitre-24-cors-comprendre-le-blocage.md)
- [Chapitre 25 — Découverte de Node.js](25-chapitre-25-decouverte-de-node-js.md)
- [Chapitre 26 — Lire et écrire des fichiers](26-chapitre-26-lire-et-ecrire-des-fichiers.md)
- [Chapitre 27 — Arguments et petits outils CLI](27-chapitre-27-arguments-et-petits-outils-cli.md)
- [Chapitre 28 — Modules](28-chapitre-28-modules.md)
- [Chapitre 29 — npm, package.json et dépendances](29-chapitre-29-npm-package-json-et-dependances.md)
- [Chapitre 30 — XSS et DOM XSS expliqués](30-chapitre-30-xss-et-dom-xss-expliques.md)
- [Chapitre 31 — CSP, en-têtes et défenses navigateur](31-chapitre-31-csp-en-tetes-et-defenses-navigateur.md)
- [Chapitre 32 — Le réflexe fondamental](32-chapitre-32-le-reflexe-fondamental.md)
- [Chapitre 33 — Lire un script JavaScript inconnu](33-chapitre-33-lire-un-script-javascript-inconnu.md)
