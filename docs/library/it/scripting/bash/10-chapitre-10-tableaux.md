---
title: Chapitre 10 — Tableaux
source: IT/07 Scripting & programmation/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

> **Note :** les tableaux sont utiles, mais pas indispensables pour commencer à automatiser. Tu peux écrire beaucoup de scripts sans en avoir besoin. Ce chapitre t'équipe pour le jour où tu en auras besoin. **Si ce chapitre te semble flou au premier passage, passe au suivant et reviens-y quand tu en auras besoin dans un vrai script.**

## Le minimum à savoir

### Créer un tableau

Un tableau stocke **plusieurs valeurs** dans une seule variable. Chaque valeur a un index qui commence à 0.

```bash
fruits=("pomme" "banane" "cerise")
```


```
Index :     0         1         2
         ┌─────┐  ┌──────┐  ┌──────┐
         │pomme│  │banane│  │cerise│
         └─────┘  └──────┘  └──────┘
```


### Accéder aux éléments

```bash
fruits=("pomme" "banane" "cerise")

echo "${fruits[0]}"      # → pomme
echo "${fruits[1]}"      # → banane
echo "${fruits[@]}"      # → pomme banane cerise (tout)
echo "${#fruits[@]}"     # → 3 (le nombre d'éléments)
```


### Ajouter un élément

```bash
fruits+=("kiwi")
echo "${fruits[@]}"      # → pomme banane cerise kiwi
```


### Modifier un élément

```bash
fruits[1]="fraise"
echo "${fruits[@]}"      # → pomme fraise cerise kiwi
```


### Supprimer un élément

```bash
unset fruits[1]
echo "${fruits[@]}"      # → pomme cerise kiwi
```


### Parcourir un tableau

```bash
#!/bin/bash

fruits=("pomme" "banane" "cerise" "kiwi")

for fruit in "${fruits[@]}"; do
    echo "Fruit : $fruit"
done
```


## Très utile en pratique

### Parcourir avec les index

```bash
for i in "${!fruits[@]}"; do
    echo "Index $i : ${fruits[$i]}"
done
```


### Tableaux multi-types

Un tableau Bash peut contenir des valeurs de types différents :

```bash
infos=("Alice" 25 "Paris" "admin")

echo "Nom  : ${infos[0]}"
echo "Âge  : ${infos[1]}"
echo "Ville: ${infos[2]}"
echo "Rôle : ${infos[3]}"
```


### Récapitulatif

| Syntaxe             | Effet                 |
| ------------------- | --------------------- |
| `tab=("a" "b" "c")` | Créer un tableau      |
| `${tab[0]}`         | Accéder à l'élément 0 |
| `${tab[@]}`         | Tous les éléments     |
| `${#tab[@]}`        | Nombre d'éléments     |
| `${!tab[@]}`        | Tous les index        |
| `tab+=("d")`        | Ajouter un élément    |
| `tab[1]="x"`        | Modifier un élément   |
| `unset tab[1]`      | Supprimer un élément  |

## Bonus

### Les tableaux associatifs (dictionnaires)

Les tableaux associatifs utilisent des **clés nommées** au lieu d'index numériques. C'est comme un dictionnaire : chaque mot (clé) a une définition (valeur).

```bash
# OBLIGATOIRE : declare -A
declare -A capitales

capitales[France]="Paris"
capitales[Allemagne]="Berlin"
capitales[Espagne]="Madrid"

echo "${capitales[France]}"       # → Paris
echo "${!capitales[@]}"           # → France Allemagne Espagne (les clés)

# Parcourir
for pays in "${!capitales[@]}"; do
    echo "La capitale de $pays est ${capitales[$pays]}"
done
```


> **Prérequis :** Bash 4.0+ (`bash --version` pour vérifier). Le `declare -A` est obligatoire, sinon Bash crée un tableau indexé normal.

## ❌ Erreur classique

```bash
# Oublier les accolades et l'[@]
echo $fruits         # ❌ N'affiche que le premier élément
echo "${fruits[@]}"  # ✅ Affiche tout

# Oublier les guillemets dans une boucle
for f in ${fruits[@]}; do     # ❌ Problème si un élément contient des espaces
for f in "${fruits[@]}"; do   # ✅ Correct
```


## Exercices

**Guidé :** Crée un tableau avec 5 prénoms, puis affiche-les numérotés avec une boucle `for` et un compteur.

**Autonome :** Crée un script qui prend des noms en arguments (`$@`), les stocke dans un tableau, et les affiche triés (indice : tu peux utiliser un pipe avec `sort`).

## 🧩 Mini-projet (chapitres 9-10)

Crée un script `contacts.sh` qui :

1. Contient un tableau de noms : `noms=("Alice" "Bob" "Charlie")`
2. Contient un tableau d'emails correspondants : `emails=("alice@mail.com" "bob@mail.com" "charlie@mail.com")`
3. Affiche chaque contact sous la forme "Nom : Alice — Email : alice@mail.com"
4. Demande à l'utilisateur un numéro et affiche le contact correspondant

## ✅ Tu sais maintenant...

- Créer, modifier et parcourir un tableau indexé
- Accéder aux éléments par leur index
- Ajouter et supprimer des éléments
- (Bonus) Utiliser des tableaux associatifs

---
