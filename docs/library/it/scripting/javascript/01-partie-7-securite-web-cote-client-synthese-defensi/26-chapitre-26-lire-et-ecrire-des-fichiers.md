---
title: Chapitre 26 — Lire et écrire des fichiers
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

C'est ici que le scripting utile commence : **manipuler des fichiers**. Node.js fournit le module **`fs`** (*file system*).

### Importer `fs`

```javascript
const fs = require("fs");
```


`require(...)` charge un module (on détaille au chapitre 28). `fs` fait partie de Node, rien à installer.

### Lire un fichier

```javascript
const fs = require("fs");

// Lecture synchrone (simple, suffisante pour des scripts)
const contenu = fs.readFileSync("logs.txt", "utf-8");
console.log(contenu);
```


`"utf-8"` indique qu'on veut du **texte** (sinon on obtient des octets bruts). `readFileSync` renvoie tout le fichier comme une grande chaîne.

### Découper en lignes

```javascript
const contenu = fs.readFileSync("logs.txt", "utf-8");
const lignes = contenu.split("\n").filter((l) => l.trim() !== "");

for (const ligne of lignes) {
  console.log("Ligne :", ligne);
}
```


C'est exactement le geste du parsing : lire le fichier, le découper en lignes (Partie 2), traiter chaque ligne.

### Écrire un fichier

```javascript
const fs = require("fs");

const rapport = "IP suspectes :\n203.0.113.5\n198.51.100.7\n";
fs.writeFileSync("rapport.txt", rapport, "utf-8");
console.log("Rapport écrit dans rapport.txt");
```


`writeFileSync` **écrase** le fichier s'il existe. Pour ajouter à la fin, utilise `fs.appendFileSync`.

### Écrire du JSON

```javascript
const donnees = { total: 42, ip_suspectes: ["203.0.113.5"] };
fs.writeFileSync("rapport.json", JSON.stringify(donnees, null, 2), "utf-8");
```


## Très utile en pratique

Le pipeline complet **lire → traiter → écrire**, cœur de l'automatisation défensive :

```javascript
const fs = require("fs");

// 1. Lire
const contenu = fs.readFileSync("auth.log", "utf-8");

// 2. Traiter : extraire les IP des lignes d'échec
const lignes = contenu.split("\n");
const ipsEchec = [];
for (const ligne of lignes) {
  if (ligne.includes("FAILED")) {
    const ips = ligne.match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g);
    if (ips) ipsEchec.push(...ips);
  }
}

// 3. Dédoublonner et écrire
const uniques = [...new Set(ipsEchec)];
fs.writeFileSync("ips_a_bloquer.txt", uniques.join("\n"), "utf-8");
console.log(`${uniques.length} IP écrites dans ips_a_bloquer.txt`);
```


## Exemple simple

```javascript
const fs = require("fs");

// Créer un fichier de test
fs.writeFileSync("test.txt", "ligne 1\nligne 2\nligne 3\n", "utf-8");

// Le relire et compter les lignes
const lignes = fs.readFileSync("test.txt", "utf-8")
  .split("\n")
  .filter((l) => l.trim() !== "");

console.log(`Le fichier contient ${lignes.length} lignes`);   // 3
```


## Application IT / cyber / OSINT

C'est **le** geste fondamental du scripting défensif, identique en logique au cours Python : lire un fichier de logs, extraire les IOC, produire une liste à bloquer ou un rapport JSON. Avec `fs` + tout ce que tu as appris (regex, `filter`, `map`, objets, JSON), tu construis de vrais outils d'analyse en local. Le mini-projet final de cette partie en fait la synthèse.

> ### 🛡️ Réflexe sécurité : prudence avec les chemins
> Ne construis jamais un chemin de fichier à partir d'une entrée non maîtrisée sans validation (risque de *path traversal*, ex. `../../etc/passwd`). Dans tes scripts personnels c'est peu risqué, mais c'est un réflexe à avoir dès qu'une entrée externe entre en jeu.

## ❌ Erreur classique

```javascript
// ❌ Oublier "utf-8" → on obtient un Buffer (octets), pas du texte
const c = fs.readFileSync("fichier.txt");
console.log(c);   // <Buffer 6c 69 67 6e ...> au lieu du texte
// ✅ Préciser l'encodage
const c2 = fs.readFileSync("fichier.txt", "utf-8");

// ❌ Lire un fichier qui n'existe pas → plantage
const x = fs.readFileSync("inexistant.txt", "utf-8");
// → Error: ENOENT: no such file or directory
// ✅ Entourer d'un try/catch
try {
  const x = fs.readFileSync("inexistant.txt", "utf-8");
} catch (e) {
  console.log("Fichier introuvable :", e.message);
}

// ❌ writeFileSync écrase tout — attention à ne pas perdre des données
```


> **Réflexe diagnostic :** `ENOENT` ? Le fichier n'existe pas (mauvais nom ou mauvais dossier). Vérifie le chemin et le dossier courant (`process.cwd()`).

## Exercices

**Guidé**

1. Écris un script qui crée un fichier `notes.txt` avec trois lignes.
2. Relis-le et affiche le nombre de lignes.
3. Ajoute une quatrième ligne avec `appendFileSync`.

**Autonome**
Crée un fichier `logs.txt` contenant quelques lignes avec des IP. Écris un script qui lit le fichier, extrait toutes les IP (regex), les dédoublonne et les écrit dans `ips.txt`.

**Défi**
Écris un script qui lit un fichier de logs, compte les échecs de connexion par IP (objet compteur), repère celles au-dessus d'un seuil, et écrit un `rapport.json` structuré. C'est le mini-projet parser de la Partie 2, mais sur un **vrai fichier**. Entoure la lecture d'un `try/catch`.

## ✅ Tu sais maintenant…

- importer `fs` avec `require` ;
- lire un fichier texte avec `readFileSync(..., "utf-8")` ;
- découper en lignes et traiter ;
- écrire avec `writeFileSync` et ajouter avec `appendFileSync` ;
- écrire du JSON dans un fichier ;
- gérer un fichier manquant avec `try/catch`.

-----
