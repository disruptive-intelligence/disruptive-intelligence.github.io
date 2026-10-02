---
title: Chapitre 6 — Conditions, comparaisons et tests
source: IT/07 Scripting & programmation/Shell/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### La structure `if`

```bash
if [[ condition ]]; then
    # code si la condition est vraie
fi
```


> **Note :** `fi` c'est `if` à l'envers. C'est la fermeture du bloc.

Exemple simple :

```bash
#!/bin/bash

nombre=15
if [[ $nombre -gt 10 ]]; then
    echo "Le nombre est supérieur à 10"
fi
```


**Règles de syntaxe :**

- Espace après `[[` et avant `]]`
- Espace autour de l'opérateur
- `then` sur la même ligne (avec `;`) ou sur la ligne suivante

### `if...else`

```bash
#!/bin/bash

nombre=5
if [[ $nombre -gt 10 ]]; then
    echo "Supérieur à 10"
else
    echo "Inférieur ou égal à 10"
fi
```


### `if...elif...else`

```bash
#!/bin/bash

age=$1

if [[ $age -lt 13 ]]; then
    echo "Tu es un enfant."
elif [[ $age -lt 18 ]]; then
    echo "Tu es un adolescent."
elif [[ $age -lt 65 ]]; then
    echo "Tu es un adulte."
else
    echo "Tu es un senior."
fi
```


> **À retenir :** autant de `elif` que tu veux, mais un seul `else` (à la fin), et un seul `fi`.

### Les 6 tests les plus utiles

Pour débuter, ces 6 tests couvrent 90% des besoins :

| Test | Signification | Exemple |
|------|--------------|---------|
| `-f` | Le fichier existe | `[[ -f "config.txt" ]]` |
| `-d` | Le dossier existe | `[[ -d "/home" ]]` |
| `-e` | Le chemin existe (fichier ou dossier) | `[[ -e "$1" ]]` |
| `-z` | La chaîne est vide | `[[ -z "$nom" ]]` |
| `-n` | La chaîne n'est pas vide | `[[ -n "$nom" ]]` |
| `-gt` | Le nombre est supérieur | `[[ $a -gt $b ]]` |

### Exemple concret : vérifier un fichier

```bash
#!/bin/bash

fichier=$1

if [[ -z "$fichier" ]]; then
    echo "Erreur : donne un chemin en argument."
    exit 1
fi

if [[ -f "$fichier" ]]; then
    echo "$fichier est un fichier."
elif [[ -d "$fichier" ]]; then
    echo "$fichier est un dossier."
else
    echo "$fichier n'existe pas."
fi
```


### Combiner des conditions

```bash
#!/bin/bash

age=$1
nom=$2

# ET : les deux doivent être vraies
if [[ $age -ge 18 && "$nom" == "Alice" ]]; then
    echo "Alice est majeure."
fi

# OU : au moins une doit être vraie
if [[ $age -lt 10 || $age -gt 80 ]]; then
    echo "Âge extrême."
fi
```


## Très utile en pratique

### Les conditions imbriquées

Tu peux mettre un `if` dans un autre `if` :

```bash
#!/bin/bash

temperature=$1

if [[ $temperature -gt 0 ]]; then
    if [[ $temperature -lt 15 ]]; then
        echo "Il fait frais."
    elif [[ $temperature -lt 25 ]]; then
        echo "Il fait bon."
    else
        echo "Il fait chaud."
    fi
else
    echo "Il gèle !"
fi
```


> **Conseil :** si tes conditions imbriquées dépassent 2-3 niveaux, c'est signe qu'il faut simplifier.

### `[ ]` vs `[[ ]]` — ce qu'il faut savoir

Dans ce cours, on utilise `[[ ]]` (la syntaxe moderne). Mais tu verras souvent `[ ]` dans des scripts existants sur internet. C'est l'ancienne syntaxe. Elle fonctionne, mais elle est plus fragile (elle plante si une variable est vide et non protégée par des guillemets).

```bash
# Avec [ ] — risqué si $nom est vide
[ $nom = "Alice" ]     # ❌ Erreur si $nom est vide

# Avec [[ ]] — pas de problème
[[ $nom == "Alice" ]]  # ✅ Fonctionne même si $nom est vide
```


**Règle simple :** utilise `[[ ]]` dans tes scripts. Si tu vois `[ ]` ailleurs, sache que c'est l'équivalent en plus ancien.

## ❌ Erreur classique

```bash
# Oublier then
if [[ $a -gt 5 ]]      # ❌ Erreur : "then" manquant
    echo "Grand"
fi

# Oublier les espaces
if [[$a -gt 5]]; then   # ❌ Erreur : pas d'espace
if [[ $a -gt 5 ]]; then # ✅ Correct

# Utiliser > pour comparer des nombres
if [[ $a > $b ]]; then      # ⚠️ Compare comme du TEXTE, pas des nombres
if [[ $a -gt $b ]]; then    # ✅ Compare comme des NOMBRES

# Oublier fi
if [[ $a -gt 5 ]]; then
    echo "Grand"
                             # ❌ Erreur : fi manquant
```


## Exercices

**Guidé :** Crée un script `meteo.sh` qui prend une température en argument et affiche "Il gèle" (< 0), "Froid" (0-15), "Bon" (15-25), ou "Chaud" (> 25).

**Autonome :** Crée un script `verifier.sh` qui prend un chemin en argument et dit si c'est un fichier, un dossier, ou si ça n'existe pas. Pense à vérifier que l'argument est fourni.

## 🧩 Mini-projet (chapitres 5-6)

Crée un script `acces.sh` qui :

1. Prend un chemin de fichier en argument
2. Vérifie qu'il existe (`-e`)
3. Si c'est un fichier (`-f`), affiche s'il est lisible (`-r`), modifiable (`-w`) et exécutable (`-x`)
4. Si c'est un dossier (`-d`), compte le nombre d'éléments qu'il contient (`ls "$1" | wc -l`)

## ✅ Tu sais maintenant...

- Écrire des conditions avec `if / elif / else / fi`
- Utiliser `[[ ]]` pour les tests
- Tester des fichiers (`-f`, `-d`, `-e`)
- Combiner des conditions avec `&&` et `||`
- La différence entre `[[ ]]` (moderne) et `[ ]` (ancien)

---
