---
title: Chapitre 11 — Déboguer et écrire des scripts propres
source: IT/07 Scripting & programmation/Shell/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Les `echo` de débogage

La méthode la plus simple : ajouter des `echo` pour voir les valeurs en cours de route :

```bash
#!/bin/bash

fichier=$1
echo "[DEBUG] fichier = '$fichier'"

if [[ -f "$fichier" ]]; then
    echo "[DEBUG] Le fichier existe"
    nb_lignes=$(wc -l < "$fichier")
    echo "[DEBUG] nb_lignes = '$nb_lignes'"
fi
```


> **Astuce :** utilise le préfixe `[DEBUG]` pour retrouver facilement tes messages et les supprimer une fois le bug corrigé.

> Utiliser `echo` pour voir ce que contient une variable ou pour suivre l'exécution d'un script, c'est une méthode **normale**, simple, et utilisée par tout le monde — même les développeurs expérimentés. Ce n'est pas du bricolage, c'est du débogage.

### Lire un message d'erreur

Les messages d'erreur de Bash suivent ce format :

```
./mon_script.sh: line 12: commande: command not found
```


- `./mon_script.sh` → quel fichier
- `line 12` → quelle ligne
- `command not found` → quel problème

### Le mode trace avec `bash -x`

`-x` affiche chaque commande **avant** de l'exécuter, avec les variables remplacées par leurs valeurs :

```bash
bash -x mon_script.sh
```


Tu peux aussi l'activer/désactiver dans le script :

```bash
#!/bin/bash
set -x          # Active la trace
echo "Ceci sera tracé"
nombre=$((5 + 3))
set +x          # Désactive la trace
echo "Ceci ne sera plus tracé"
```


Sortie :

```
+ echo 'Ceci sera tracé'
Ceci sera tracé
+ nombre=8
+ set +x
Ceci ne sera plus tracé
```


### Les 5 erreurs de débutant les plus fréquentes

| Erreur                   | Message                   | Solution                                       |
| ------------------------ | ------------------------- | ---------------------------------------------- |
| Espaces autour de `=`    | `command not found`       | `var="valeur"` (pas d'espace)                  |
| `then` ou `fi` oublié    | `syntax error`            | Vérifie chaque `if` a son `then` et son `fi`   |
| `do` ou `done` oublié    | `syntax error`            | Vérifie chaque boucle a son `do` et son `done` |
| Guillemets oubliés       | `unary operator expected` | Mets `"$var"` au lieu de `$var`                |
| `-eq` confondu avec `==` | Résultat inattendu        | `-eq` pour nombres, `==` pour texte            |

## Très utile en pratique

### Vérifier les arguments en début de script

```bash
#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Erreur : argument manquant" >&2
    echo "Utilisation : $0 <fichier>" >&2
    exit 1
fi
```


> **Note :** `>&2` envoie le message vers stderr (la sortie d'erreur). C'est la bonne pratique pour les messages d'erreur.

### Noms de variables descriptifs

```bash
# ❌ Incompréhensible
a=5
b="txt"

# ✅ Clair
nombre_fichiers=5
extension="txt"
```


### Structurer avec des fonctions

```bash
# ❌ Script monolithique de 200 lignes

# ✅ Script structuré
verifier_arguments() { ... }
traiter_fichier() { ... }
generer_rapport() { ... }

verifier_arguments "$@"
traiter_fichier "$1"
generer_rapport
```


### Commenter ton code

```bash
#!/bin/bash
# Ce script sauvegarde les fichiers de configuration
# Usage : ./backup.sh <dossier_destination>
```


### Toujours mettre les variables entre guillemets

```bash
cat $fichier       # ❌ Dangereux si $fichier contient des espaces
cat "$fichier"     # ✅ Sûr
```


## Bonus

### `set -e` : arrêt sur erreur

Par défaut, Bash continue même quand une commande échoue. `set -e` change ça :

```bash
#!/bin/bash
set -e

echo "Étape 1"
cd /dossier_inexistant     # ← Erreur ! Le script s'arrête ici
echo "Étape 2"             # ← Jamais exécuté
```


C'est utile pour les scripts importants, mais attention : ça peut aussi arrêter le script sur des erreurs "attendues". Utilise-le quand tu maîtrises bien ton script.

### `set -u` : erreur si variable non définie

```bash
#!/bin/bash
set -u

echo "Mon nom est $nom"    # ← Erreur ! $nom n'est pas défini
```


### La combinaison `set -euo pipefail`

Beaucoup de développeurs expérimentés utilisent :

```bash
#!/bin/bash
set -euo pipefail
```


- `-e` : arrêt sur erreur
- `-u` : erreur si variable non définie
- `-o pipefail` : un pipe échoue si n'importe quelle commande du pipe échoue

C'est un filet de sécurité puissant, mais à utiliser quand tu es à l'aise avec les bases. Ne te force pas à le mettre dans tes premiers scripts.

## ❌ Erreur classique

```bash
# Laisser des echo [DEBUG] dans le script final
echo "[DEBUG] valeur = $x"    # ← Pense à les supprimer !

# Ne pas tester le script avec des cas limites
./script.sh ""                # Que se passe-t-il avec un argument vide ?
./script.sh "fichier avec espaces.txt"   # Et avec des espaces ?
```


## Exercices

**Guidé :** Prends un de tes scripts précédents et lance-le avec `bash -x`. Observe les lignes précédées de `+`.

**Autonome :** Crée un script volontairement bugué (variable mal nommée, `fi` manquant, variable vide...) et corrige les erreurs en lisant les messages d'erreur.

## ✅ Tu sais maintenant...

- Déboguer avec `echo [DEBUG]` et `bash -x`
- Lire et comprendre les messages d'erreur
- Les 5 erreurs les plus fréquentes
- Les bonnes pratiques : guillemets, noms clairs, commentaires, fonctions
- (Bonus) `set -e`, `set -u`, `set -euo pipefail`

---
