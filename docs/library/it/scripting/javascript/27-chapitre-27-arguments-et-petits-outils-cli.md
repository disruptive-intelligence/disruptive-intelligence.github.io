---
title: Chapitre 27 — Arguments et petits outils CLI
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 27
chapters: 35
---

## Le minimum à savoir

Un outil utile prend des **paramètres** en ligne de commande. Node expose les arguments via **`process.argv`**.

```javascript
console.log(process.argv);
```

```bash
node script.js fichier.log 5
```

```text
[
  '/usr/bin/node',       // [0] le chemin de node
  '/chemin/script.js',   // [1] le chemin du script
  'fichier.log',         // [2] premier vrai argument
  '5'                    // [3] deuxième argument
]
```

Les deux premiers éléments sont toujours node et le script. **Tes** arguments commencent à l'index **2**.

```javascript
const args = process.argv.slice(2);   // on enlève les deux premiers
const fichier = args[0];
const seuil = Number(args[1]) || 3;    // les arguments sont des CHAÎNES

console.log(`Fichier : ${fichier}, seuil : ${seuil}`);
```

> Comme pour le Web Storage, les arguments sont toujours des **chaînes** : convertis avec `Number(...)` si tu attends un nombre.

### Codes de sortie

Un outil signale son succès ou son échec par un **code de sortie** (`0` = succès, autre = erreur), utile dans les enchaînements shell.

```javascript
if (!fichier) {
  console.error("Usage : node outil.js <fichier> [seuil]");
  process.exit(1);   // sortie en erreur
}
```

## Très utile en pratique

Un outil CLI paramétrable, avec vérification des arguments :

```javascript
const fs = require("fs");

const args = process.argv.slice(2);
const fichier = args[0];

if (!fichier) {
  console.error("Usage : node compter-erreurs.js <fichier.log>");
  process.exit(1);
}

try {
  const contenu = fs.readFileSync(fichier, "utf-8");
  const lignes = contenu.split("\n");
  const erreurs = lignes.filter((l) => l.includes("FAILED")).length;
  console.log(`${erreurs} échecs trouvés dans ${fichier}`);
} catch (e) {
  console.error("Erreur :", e.message);
  process.exit(1);
}
```

```bash
node compter-erreurs.js auth.log
```

## Exemple simple

```javascript
const args = process.argv.slice(2);
const nom = args[0] || "monde";
console.log(`Bonjour, ${nom}`);
```

```bash
node salut.js analyste    # Bonjour, analyste
node salut.js             # Bonjour, monde
```

## Application IT / cyber / OSINT

Les arguments transforment un script figé en **outil réutilisable** : `node extract-ioc.js rapport.txt`, `node triage.js auth.log 5`. C'est exactement le modèle des outils du cours Python (arguments, `process.exit`). Tu peux ainsi construire une petite boîte à outils défensive en ligne de commande, chaque script faisant une tâche précise et paramétrable.

## ❌ Erreur classique

```javascript
// ❌ Oublier le slice(2) et lire node/script comme arguments
const fichier = process.argv[0];   // c'est le chemin de node !
// ✅ Tes arguments commencent à l'index 2
const fichier2 = process.argv[2];
// ou, plus clair :
const [fichier3, seuil] = process.argv.slice(2);

// ❌ Ne pas vérifier qu'un argument est fourni → undefined plus loin
// ✅ Vérifier et afficher un usage clair, puis process.exit(1)

// ❌ Traiter un argument numérique comme un nombre sans conversion
const seuil4 = process.argv[3];          // chaîne "5"
console.log(seuil4 + 1);                 // "51" !
console.log(Number(seuil4) + 1);         // 6 ✅
```

> **Réflexe diagnostic :** ton argument vaut `undefined` ? Vérifie le `slice(2)` et que tu as bien passé l'argument sur la ligne de commande.

## Exercices

**Guidé**
1. Crée un script qui affiche le premier argument passé.
2. Si aucun argument, affiche un message d'usage et `process.exit(1)`.
3. Teste avec et sans argument.

**Autonome**
Écris `compter-lignes.js <fichier>` : il lit le fichier passé en argument et affiche son nombre de lignes. Gère l'absence d'argument et le fichier manquant.

**Défi**
Écris `triage.js <fichier> [seuil]` : lit un fichier de logs, compte les échecs par IP, et affiche celles au-dessus du `seuil` (défaut 3). Tous les paramètres viennent de la ligne de commande. Renvoie `process.exit(1)` en cas d'erreur d'usage ou de fichier.

## ✅ Tu sais maintenant…

- lire les arguments avec `process.argv` (à partir de l'index 2) ;
- convertir les arguments numériques avec `Number(...)` ;
- vérifier les arguments et afficher un usage ;
- utiliser `process.exit(code)` pour signaler succès/échec ;
- construire un petit outil CLI paramétrable.

-----
