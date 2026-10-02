---
title: Chapitre 25 — Découverte de Node.js
source: IT/07 Scripting & programmation/Langages/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Jusqu'ici, ton JavaScript tournait dans le **navigateur**. **Node.js** permet d'exécuter du JavaScript **directement sur ta machine**, comme un script Python ou Bash. C'est le moment où JavaScript devient un outil d'**automatisation**.

### Installer Node.js LTS

**Linux :**

```bash
# Vérifie si Node est déjà installé
node --version

# Sinon, installe via le gestionnaire de paquets (Debian/Ubuntu)
sudo apt update && sudo apt install nodejs npm

# Ou, recommandé, via nvm pour avoir la version LTS récente
# (voir https://github.com/nvm-sh/nvm)
```


**Mac :** `brew install node`, ou l'installeur depuis le site officiel.

**Windows :** l'installeur **LTS** depuis le site officiel de Node.js.

> Choisis toujours la version **LTS** (*Long Term Support*) : c'est la version stable recommandée. Vérifie avec `node --version` (tu devrais voir `v20.x`, `v22.x` ou plus récent).

### Exécuter un fichier

Crée un fichier `script.js` :

```javascript
console.log("Bonjour depuis Node.js");
console.log("2 + 2 =", 2 + 2);
```


Lance-le dans le terminal :

```bash
node script.js
```


Sortie :

```text
Bonjour depuis Node.js
2 + 2 = 4
```


**Aucune page, aucun navigateur** : le code s'exécute directement. C'est exactement le modèle du cours Python, mais en JavaScript.

### Le REPL (mode interactif)

Tape simplement `node` sans argument pour ouvrir un mode interactif (comme la console Python) :

```bash
node
> 2 + 2
4
> "8.8.8.8".split(".")
[ '8', '8', '8', '8' ]
> .exit
```


## Très utile en pratique

> ### 🧭 Navigateur vs Node.js : le récapitulatif
> | | Navigateur | Node.js |
> | --- | --- | --- |
> | **DOM / `document`** | ✅ oui | ❌ non |
> | **`window`, `alert`** | ✅ oui | ❌ non |
> | **Accès aux fichiers** | ❌ non (sauf input file) | ✅ oui (`fs`) |
> | **Arguments CLI** | ❌ non | ✅ oui (`process.argv`) |
> | **CORS sur `fetch`** | ✅ appliqué | ❌ ignoré |
> | **Lancement** | via une page HTML | `node script.js` |
>
> Même langage, capacités différentes. Si un code utilise `document`, il est **navigateur**. S'il utilise `fs` ou `process`, il est **Node.js**.

## Exemple simple

`info.js` :

```javascript
const ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"];

for (const ip of ips) {
  const privee = ip.startsWith("192.168.");
  console.log(`${ip} → ${privee ? "privée" : "publique"}`);
}
```


```bash
node info.js
```


Tout ton savoir des Parties 1-2 (variables, boucles, fonctions, tableaux, objets, JSON, regex) fonctionne **à l'identique** dans Node.js. Seuls le DOM et les événements navigateur n'existent pas.

## Application IT / cyber / OSINT

Node.js est là où JavaScript rejoint le **scripting d'automatisation** que tu connais peut-être de Python : lire des fichiers de logs, parser des données, interroger des APIs en lot, produire des rapports. Tu peux écrire un outil CLI qui prend un fichier en entrée, extrait les IOC, et sort un rapport JSON — sans aucun navigateur. C'est le terrain des chapitres suivants.

## ❌ Erreur classique

```javascript
// ❌ Utiliser du code navigateur dans Node
document.querySelector("#x");   // ReferenceError: document is not defined
alert("test");                  // ReferenceError: alert is not defined

// ✅ Dans Node, on utilise console.log, fs, process... (chapitres suivants)
```


> **Réflexe diagnostic :** `document is not defined` ou `window is not defined` dans Node ? Tu exécutes du code **navigateur** dans Node. Ces objets n'existent que dans le navigateur.

## Exercices

**Guidé**

1. Installe Node.js LTS, vérifie avec `node --version`.
2. Crée `hello.js` qui affiche un message et un calcul.
3. Lance-le avec `node hello.js`.

**Autonome**
Crée un script Node qui contient un tableau d'IP et affiche pour chacune si elle est privée ou publique (réutilise ta fonction `estIpPrivee`).

**Défi**
Dans le REPL Node (`node`), expérimente : `[1,2,3].map(n => n*2)`, `JSON.stringify({a:1})`, `"a.b.c".split(".")`. Vérifie que tout ce que tu as appris fonctionne identiquement. Puis `.exit`.

## ✅ Tu sais maintenant…

- installer Node.js LTS et vérifier la version ;
- exécuter un fichier avec `node script.js` ;
- utiliser le REPL interactif ;
- distinguer ce qui existe en Node vs navigateur ;
- diagnostiquer un `document is not defined`.

-----
