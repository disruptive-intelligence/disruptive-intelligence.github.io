---
title: Chapitre 2 — Variables, affichage et saisie utilisateur
source: IT/05_Scripting_Langage-Prog/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable, c'est un **conteneur avec une étiquette**. L'étiquette c'est le nom, et à l'intérieur il y a une valeur.

```
┌─────────────────┐
│  prenom = Alice  │   ← "prenom" est le nom, "Alice" est la valeur
└─────────────────┘
```


### Créer et afficher une variable

```bash
#!/bin/bash

prenom="Alice"
echo "Bonjour, $prenom !"
```


Résultat : `Bonjour, Alice !`

**Règle critique : PAS d'espace autour du `=`**

```bash
# ✅ CORRECT
prenom="Alice"

# ❌ FAUX — Bash croit que "prenom" est une commande
prenom = "Alice"
```


Pour accéder au contenu d'une variable, on met `$` devant son nom. Sans le `$`, Bash affiche le texte brut :

```bash
echo "Bonjour, $prenom"     # → Bonjour, Alice
echo "Bonjour, prenom"      # → Bonjour, prenom
```


> **Bonne pratique :** écris `"$prenom"` (avec guillemets) plutôt que `$prenom` nu. Ça évite des problèmes si la valeur contient des espaces. Prends ce réflexe dès maintenant.

### La forme avec accolades `${variable}`

Les accolades servent à éviter les ambiguïtés :

```bash
animal="chat"
echo "J'ai 3 ${animal}s"    # → J'ai 3 chats
echo "J'ai 3 $animals"      # → J'ai 3  (Bash cherche la variable "animals" qui n'existe pas)
```


### Modifier une variable

Tu peux changer la valeur à tout moment :

```bash
#!/bin/bash
humeur="content"
echo "Je suis $humeur"

humeur="fatigué"
echo "Maintenant je suis $humeur"
```


### Guillemets simples vs doubles

```bash
prenom="Alice"

echo "Bonjour, $prenom"    # Guillemets doubles → Bash remplace la variable
# → Bonjour, Alice

echo 'Bonjour, $prenom'    # Guillemets simples → tout est affiché tel quel
# → Bonjour, $prenom
```


> **À retenir :**
> - **Guillemets doubles `" "`** → Bash interprète les variables
> - **Guillemets simples `' '`** → tout est littéral, aucune interprétation

### Lire une saisie utilisateur avec `read`

La commande `read` demande à l'utilisateur de taper quelque chose :

```bash
#!/bin/bash

read -p "Ton prénom : " prenom
read -p "Ton âge : " age
echo "Tu es $prenom et tu as $age ans."
```


Exécution :

```
Ton prénom : Alice
Ton âge : 25
Tu es Alice et tu as 25 ans.
```


`-p` permet de mettre le message et la saisie sur la même ligne. C'est la forme la plus pratique.

## Très utile en pratique

### La substitution de commande

Tu peux **stocker le résultat d'une commande** dans une variable avec `$(commande)` :

```bash
#!/bin/bash

aujourdhui=$(date)
echo "Nous sommes le : $aujourdhui"

utilisateur=$(whoami)
echo "Connecté en tant que : $utilisateur"

nb_fichiers=$(ls | wc -l)
echo "Il y a $nb_fichiers éléments dans ce dossier"
```


> **À retenir :** `$(commande)` exécute la commande et renvoie son résultat. C'est l'une des fonctionnalités les plus puissantes de Bash.

### Les variables d'environnement

Ton système contient des variables déjà définies :

```bash
echo "Utilisateur : $USER"
echo "Dossier personnel : $HOME"
echo "Shell actuel : $SHELL"
echo "Dossier actuel : $PWD"
```


### Variables en lecture seule

Pour qu'une variable ne puisse jamais être modifiée :

```bash
readonly PI=3.14159
PI=3.0    # → Erreur ! bash: PI: readonly variable
```


## Bonus

### Note sur les "types" en Bash

En Bash, une variable contient surtout du texte. Même les nombres sont manipulés comme du texte, sauf quand tu fais du calcul (chapitre 5). Il n'y a pas de système de types strict comme dans d'autres langages. Ne te préoccupe pas de ça pour l'instant.

### Autres options de `read`

```bash
read -p "Mot de passe : " -s motdepasse    # -s : saisie invisible
read -p "Choix rapide : " -t 5 choix        # -t 5 : timeout de 5 secondes
```


## ❌ Erreur classique

```bash
prenom = "Alice"     # ❌ Espaces autour du = → Bash croit que "prenom" est une commande
prenom="Alice"       # ✅ Correct

echo $prenom         # ⚠️ Fonctionne, mais risqué si la valeur contient des espaces
echo "$prenom"       # ✅ Toujours préférer cette forme
```


## Exercices

**Guidé :** Crée un script `presentation.sh` qui demande le prénom et l'âge avec `read -p`, puis affiche "Tu es [prénom] et tu as [âge] ans."

**Autonome :** Crée un script `machine.sh` qui affiche le nom de l'utilisateur, la date et le nom de la machine (`hostname`) en utilisant la substitution de commande `$(...)`.

## 🧩 Mini-projet (chapitres 1-2)

Crée un script `bienvenue.sh` qui :

1. Affiche "Bienvenue sur cette machine !"
2. Affiche la date du jour (avec substitution de commande)
3. Demande le prénom de l'utilisateur
4. Affiche "Bonjour [prénom], connecté en tant que [whoami]"

## ✅ Tu sais maintenant...

- Créer une variable et l'afficher avec `$`
- La différence entre guillemets simples et doubles
- Lire une saisie utilisateur avec `read -p`
- Stocker le résultat d'une commande avec `$(commande)`

---
