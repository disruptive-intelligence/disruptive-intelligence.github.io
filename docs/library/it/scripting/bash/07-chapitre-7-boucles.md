---
title: Chapitre 7 — Boucles
source: IT/07 Scripting & programmation/Shell/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### À quoi servent les boucles ?

Les boucles répètent des actions. Tu dois renommer 200 fichiers ? Vérifier 50 serveurs ? Tu n'écris pas 200 commandes : tu écris une boucle.

Il y a deux façons de penser :

- **`for`** = répéter sur une **liste** d'éléments
- **`while`** = répéter **tant qu'une condition** est vraie

### La boucle `for`

**Parcourir une liste de mots :**

```bash
#!/bin/bash

for fruit in pomme banane cerise; do
    echo "J'aime la $fruit"
done
```


```
J'aime la pomme
J'aime la banane
J'aime la cerise
```


**Parcourir une plage de nombres :**

```bash
for i in {1..5}; do
    echo "Tour numéro $i"
done
```


**Parcourir des fichiers (le cas le plus courant) :**

```bash
#!/bin/bash

for fichier in *.txt; do
    echo "Traitement de $fichier"
done
```


> **À retenir :** `for fichier in *.txt` parcourt tous les fichiers `.txt` du dossier actuel. C'est la façon propre et sûre de parcourir des fichiers.

**Parcourir avec un pas :**

```bash
# Compter de 2 en 2
for i in {0..10..2}; do
    echo $i
done
# → 0, 2, 4, 6, 8, 10
```


### La boucle `while`

```bash
#!/bin/bash

compteur=1
while [[ $compteur -le 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done
```


```
Compteur : 1
Compteur : 2
Compteur : 3
Compteur : 4
Compteur : 5
```


> **Attention :** si tu oublies `((compteur++))`, la boucle tourne **à l'infini** ! Appuie sur `Ctrl+C` pour l'arrêter.

**Lire un fichier ligne par ligne :**

```bash
#!/bin/bash

while read -r ligne; do
    echo "Lu : $ligne"
done < mon_fichier.txt
```


> **Note :** `-r` empêche `read` d'interpréter les caractères spéciaux comme `\`. C'est une bonne pratique.

### `break` et `continue`

**`break`** — sortir de la boucle :

```bash
for i in {1..10}; do
    if [[ $i -eq 6 ]]; then
        echo "Stop à $i"
        break
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 3, 4, 5 puis "Stop à 6"
```


**`continue`** — sauter au tour suivant :

```bash
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 4, 5 (le 3 est sauté)
```


## Très utile en pratique

### Le `for` style C (pour les plages dynamiques)

La syntaxe `{1..5}` ne fonctionne pas avec des variables. Pour ça :

```bash
#!/bin/bash

limite=$1
for (( i=1; i<=limite; i++ )); do
    echo "Tour $i"
done
```


### Les boucles imbriquées

```bash
#!/bin/bash

for i in {1..3}; do
    for j in {1..3}; do
        echo "i=$i, j=$j"
    done
done
```


### Attention aux boucles infinies

```bash
# ❌ BOUCLE INFINIE — le compteur ne change jamais
compteur=1
while [[ $compteur -le 5 ]]; do
    echo $compteur
    # Oubli de ((compteur++)) !
done
```


Si ça t'arrive : **Ctrl+C** pour arrêter.

**Boucle infinie volontaire** (parfois utile) :

```bash
while true; do
    echo "En attente..."
    sleep 5
done
```


## Bonus

### La boucle `until`

`until` est l'inverse de `while` : elle boucle tant que la condition est **fausse** :

```bash
compteur=1
until [[ $compteur -gt 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done
```


En pratique, `while` est beaucoup plus courant. `until` est juste une autre façon d'écrire certaines boucles.

## 🔧 Quand ça plante : déboguer une boucle

Ajoute des `echo` temporaires pour voir ce qui se passe :

```bash
for fichier in *.txt; do
    echo "[DEBUG] fichier = '$fichier'"    # ← ajoute ça
    # ... le reste du code
done
```


Si tu ne vois aucun `[DEBUG]`, c'est que la boucle ne s'exécute pas (peut-être qu'il n'y a aucun `.txt` dans le dossier).

## ❌ Erreur classique

```bash
# Oublier do
for i in {1..5};        # ❌ "do" manquant
    echo $i
done

# Oublier done
for i in {1..5}; do
    echo $i
                        # ❌ "done" manquant

# Boucle infinie par oubli d'incrément
while [[ $n -le 10 ]]; do
    echo $n
    # ← Il faut ((n++)) ici !
done
```


## Exercices

**Guidé :** Crée un script qui affiche les nombres de 1 à 10, un par ligne. Utilise une boucle `for` avec `{1..10}`.

**Autonome :** Crée un script qui lit un fichier texte ligne par ligne et affiche chaque ligne précédée de son numéro (indice : utilise un compteur avec `((numero++))`).

**Défi :** Crée un script qui affiche la table de multiplication d'un nombre donné en argument (de 1 à 10).

## ✅ Tu sais maintenant...

- Parcourir une liste ou des fichiers avec `for`
- Répéter tant qu'une condition est vraie avec `while`
- Lire un fichier ligne par ligne
- Contrôler une boucle avec `break` et `continue`
- Éviter et arrêter les boucles infinies

---
