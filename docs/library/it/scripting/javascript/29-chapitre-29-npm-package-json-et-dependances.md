---
title: Chapitre 29 — npm, package.json et dépendances
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 29
chapters: 35
---

## Le minimum à savoir

**`npm`** (*Node Package Manager*) est l'outil qui installe des **bibliothèques** (paquets) écrites par d'autres. Il est installé avec Node.

### Initialiser un projet

```bash
mkdir mon-outil && cd mon-outil
npm init -y          # crée un package.json par défaut
```

Cela crée **`package.json`**, le fichier qui décrit ton projet et ses dépendances :

```json
{
  "name": "mon-outil",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {}
}
```

### Installer un paquet

```bash
npm install nom-du-paquet
```

Cela : télécharge le paquet dans **`node_modules/`**, et l'ajoute aux `dependencies` de `package.json`. Tu l'utilises ensuite avec `require`.

### Scripts npm

Le champ `scripts` de `package.json` définit des commandes pratiques :

```json
"scripts": {
  "start": "node index.js",
  "triage": "node cli.js auth.log"
}
```

```bash
npm run triage     # exécute "node cli.js auth.log"
```

### `package.json` vs `package-lock.json`

- **`package.json`** : la liste de ce que tu veux (tes dépendances déclarées).
- **`package-lock.json`** : les versions **exactes** réellement installées (généré par npm). À conserver pour des installs reproductibles.

## Très utile en pratique : la sécurité des dépendances

> ### 🛡️ Réflexe sécurité (MAJEUR) : dépendances et supply chain
> Installer un paquet npm, c'est **exécuter du code écrit par des inconnus** sur ta machine. C'est puissant, mais c'est une vraie **surface d'attaque** (risques n° 9 et n° 10 de la Boîte à risques). Réflexes :
>
> - **N'installe que ce dont tu as besoin.** Chaque dépendance ajoute du code (et ses propres sous-dépendances).
> - **Vérifie ce que tu installes** : nom exact (attention au *typosquatting* — un paquet au nom presque identique à un paquet connu), popularité, maintenance récente.
> - **Lance `npm audit`** : il signale les vulnérabilités connues dans tes dépendances.
> - **Ne copie-colle jamais une commande `npm install` venue d'une source douteuse** sans comprendre ce qu'elle installe.
> - **Commits le `package-lock.json`** pour des installations reproductibles et traçables.
>
> Les attaques par chaîne d'approvisionnement (un paquet populaire compromis ou un paquet malveillant au nom trompeur) sont une menace réelle. La connaissance de ce risque fait partie du socle défensif.

## Exemple simple

```bash
npm init -y
npm install chalk        # un paquet qui colore le texte du terminal
```

```javascript
// index.js
const chalk = require("chalk");
console.log(chalk.red("⚠️ Alerte"));
console.log(chalk.green("✅ OK"));
```

```bash
node index.js
```

## Application IT / cyber / OSINT

`npm` ouvre l'accès à un immense écosystème utile : parsing avancé, clients d'API, manipulation de données. Mais pour un profil cyber, la **dimension sécurité** prime : comprendre la **supply chain** npm, savoir qu'une dépendance est du code exécuté chez toi, utiliser `npm audit`, et se méfier du *typosquatting* sont des compétences directement transférables à l'analyse de risques d'un projet. Beaucoup d'incidents réels viennent d'une dépendance compromise.

> ### 🔍 Lecture de code inconnu
> Face à un projet inconnu, lis **`package.json`** en premier : ses dépendances révèlent ce que le projet fait et avec quoi. Une dépendance obscure, très récente ou au nom proche d'un paquet connu mérite un examen attentif.

## ❌ Erreur classique

```text
# ❌ Installer un paquet sans vérifier son nom (typosquatting)
npm install crossenv        # ⚠️ faux paquet imitant "cross-env" (cas réel malveillant)

# ❌ Copier une commande npm install d'un tutoriel douteux sans la comprendre

# ❌ Ignorer les avertissements de npm audit
npm audit                   # ✅ lis et traite les vulnérabilités signalées

# ❌ Versionner node_modules (inutile, énorme) — on versionne package.json + lock
```

> **Réflexe diagnostic :** un `require("paquet")` échoue avec `Cannot find module` ? Le paquet n'est pas installé (`npm install paquet`) ou tu n'es pas dans le bon dossier (celui qui contient `node_modules` et `package.json`).

## Exercices

**Guidé**
1. Crée un dossier, lance `npm init -y`, observe le `package.json`.
2. Ajoute un script `"start": "node index.js"`.
3. Crée `index.js` et lance-le avec `npm start`.

**Autonome**
Initialise un projet, installe un petit paquet utilitaire de ton choix (par ex. de coloration ou de date), et écris un `index.js` qui l'utilise. Observe l'apparition de `node_modules` et la mise à jour de `package.json`.

**Défi**
Dans un projet avec quelques dépendances, lance `npm audit` et lis le rapport. Rédige (en commentaire ou dans un fichier) un court mémo : qu'est-ce que le typosquatting, pourquoi `package-lock.json` est important, et trois réflexes pour réduire le risque lié aux dépendances.

## ✅ Tu sais maintenant…

- initialiser un projet avec `npm init` et lire `package.json` ;
- installer un paquet avec `npm install` et l'utiliser via `require` ;
- définir et lancer des scripts npm ;
- distinguer `package.json` et `package-lock.json` ;
- appliquer les réflexes de sécurité supply chain (`npm audit`, typosquatting, prudence).

-----

## 🧩 Mini-projet — Outil CLI Node « log-triage » (chapitres 25 à 29)

La synthèse de la Partie 6 : un vrai outil en ligne de commande, structuré en module + CLI, qui lit un fichier de logs et produit un rapport.

**Structure du projet :**

```text
log-triage/
├── package.json
├── analyse.js     (module : fonctions de parsing)
└── triage.js      (CLI : lecture fichier + rapport)
```

`analyse.js` :

```javascript
// Module de fonctions réutilisables

function parserLignes(contenu) {
  const lignes = contenu.split("\n").map((l) => l.trim()).filter((l) => l !== "");
  const evenements = [];
  for (const ligne of lignes) {
    try {
      const champs = ligne.split(" ");
      const ip = champs[2];
      const statut = champs[4];
      if (!/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(ip)) {
        throw new Error("IP invalide");
      }
      evenements.push({ ip, statut });
    } catch {
      // ligne ignorée silencieusement (on pourrait logger)
    }
  }
  return evenements;
}

function compterEchecsParIp(evenements) {
  const compteur = {};
  for (const e of evenements) {
    if (e.statut === "FAILED") {
      compteur[e.ip] = (compteur[e.ip] || 0) + 1;
    }
  }
  return compteur;
}

function ipsSuspectes(compteur, seuil) {
  return Object.entries(compteur)
    .filter(([ip, n]) => n >= seuil)
    .map(([ip, n]) => ({ ip, echecs: n }));
}

module.exports = { parserLignes, compterEchecsParIp, ipsSuspectes };
```

`triage.js` :

```javascript
const fs = require("fs");
const { parserLignes, compterEchecsParIp, ipsSuspectes } = require("./analyse");

// Arguments CLI
const args = process.argv.slice(2);
const fichier = args[0];
const seuil = Number(args[1]) || 3;

if (!fichier) {
  console.error("Usage : node triage.js <fichier.log> [seuil]");
  process.exit(1);
}

try {
  const contenu = fs.readFileSync(fichier, "utf-8");
  const evenements = parserLignes(contenu);
  const compteur = compterEchecsParIp(evenements);
  const suspectes = ipsSuspectes(compteur, seuil);

  const rapport = {
    fichier,
    seuil,
    total_evenements: evenements.length,
    ip_suspectes: suspectes
  };

  // Afficher ET sauvegarder
  console.log(JSON.stringify(rapport, null, 2));
  fs.writeFileSync("rapport.json", JSON.stringify(rapport, null, 2), "utf-8");
  console.log("\n✅ Rapport écrit dans rapport.json");

  // Code de sortie : 2 si des IP suspectes (utile en script shell)
  process.exit(suspectes.length > 0 ? 2 : 0);
} catch (e) {
  console.error("Erreur :", e.message);
  process.exit(1);
}
```

**Crée un fichier `auth.log` de test :**

```text
2024-01-15 10:00:01 203.0.113.5 login FAILED
2024-01-15 10:00:02 203.0.113.5 login FAILED
2024-01-15 10:00:03 8.8.8.8 login OK
2024-01-15 10:00:04 203.0.113.5 login FAILED
2024-01-15 10:00:05 203.0.113.5 login FAILED
```

**Lance :**

```bash
node triage.js auth.log 3
```

Ce mini-projet est le **pendant JavaScript complet** du parser de logs du cours Python : module réutilisable (`require`/`module.exports`), CLI avec arguments (`process.argv`), lecture de fichier (`fs`), parsing (regex, `split`, objets, `filter`/`map`), production de rapport JSON, gestion d'erreurs (`try/catch`), et code de sortie. Tu disposes maintenant d'un vrai outil d'automatisation défensive.

-----

## ✅ CHECKPOINT 6 — Tu sais écrire de vrais petits outils

Avant la Partie 7, assure-toi de pouvoir, **sans regarder** :

- [ ] exécuter un script avec `node` et utiliser le REPL ;
- [ ] distinguer capacités navigateur vs Node.js ;
- [ ] lire/écrire des fichiers avec `fs` (et gérer `ENOENT`) ;
- [ ] lire des arguments avec `process.argv` et `process.exit` ;
- [ ] découper en modules (`require`/`module.exports`) ;
- [ ] utiliser `npm`, `package.json`, et appliquer les réflexes supply chain ;
- [ ] réaliser le mini-projet CLI log-triage.

Tu sais automatiser en local. La Partie 7 rassemble et approfondit la **sécurité web côté client** semée tout au long du cours.


-----
