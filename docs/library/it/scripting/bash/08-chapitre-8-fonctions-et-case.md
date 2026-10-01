---
title: Chapitre 8 — Fonctions et case
source: IT/07 Scripting & programmation/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'une fonction ?

Une fonction, c'est un **bloc de code réutilisable** auquel tu donnes un nom. Au lieu de copier-coller les mêmes lignes, tu les mets dans une fonction et tu l'appelles par son nom.

### Définir et appeler une fonction

```bash
#!/bin/bash

# 1. Définir la fonction
saluer() {
    echo "Salut, bienvenue !"
}

# 2. L'appeler (juste son nom, sans parenthèses)
saluer
saluer
```


```
Salut, bienvenue !
Salut, bienvenue !
```


> **Règle :** la définition doit apparaître **AVANT** l'appel dans le script.

### Passer des arguments à une fonction

À l'intérieur de la fonction, `$1`, `$2`... sont les arguments **de la fonction** (pas du script) :

```bash
#!/bin/bash

saluer() {
    echo "Bonjour, $1 ! Tu as $2 ans."
}

saluer "Alice" 25
saluer "Bob" 30
```


```
Bonjour, Alice ! Tu as 25 ans.
Bonjour, Bob ! Tu as 30 ans.
```


### Récupérer le résultat d'une fonction

En Bash, une fonction renvoie un résultat en l'affichant avec `echo`. On le récupère avec `$(...)` :

```bash
#!/bin/bash

addition() {
    echo $(( $1 + $2 ))
}

resultat=$(addition 15 27)
echo "La somme est : $resultat"
```


> **À retenir :** `return` ne sert PAS à renvoyer une chaîne ou un nombre. Il sert uniquement à donner un code de succès (0) ou d'erreur (1). Pour renvoyer un résultat, utilise `echo` + `$(...)`.

### Le `case` : choix multiples propres

Le `case` teste **une variable** contre plusieurs valeurs possibles. C'est plus lisible que des enchaînements de `elif` :

```bash
#!/bin/bash

case $1 in
    oui|o|yes|y)
        echo "Tu as dit oui." ;;
    non|n|no)
        echo "Tu as dit non." ;;
    *)
        echo "Réponse non reconnue." ;;
esac
```


> **Notes :**
> - `esac` c'est `case` à l'envers (fermeture du bloc)
> - Chaque bloc se termine par `;;`
> - `*` est le cas par défaut (si rien d'autre ne correspond)
> - `|` sépare plusieurs patterns pour le même bloc

## Très utile en pratique

### Fonctions + case = script avec des options

```bash
#!/bin/bash

afficher_aide() {
    echo "Utilisation : $0 [option]"
    echo "  -l    Lister les fichiers"
    echo "  -d    Afficher la date"
    echo "  -h    Afficher cette aide"
}

case $1 in
    -l) ls -la ;;
    -d) date ;;
    -h) afficher_aide ;;
    "")
        echo "Erreur : aucune option fournie."
        afficher_aide
        exit 1 ;;
    *)
        echo "Option '$1' inconnue."
        afficher_aide
        exit 1 ;;
esac
```


```bash
./outil.sh -l      # Liste les fichiers
./outil.sh -d      # Affiche la date
./outil.sh -h      # Affiche l'aide
./outil.sh -z      # "Option '-z' inconnue."
```


### Variables locales

Par défaut, les variables dans une fonction sont **globales**. Pour les limiter à la fonction, utilise `local` :

```bash
#!/bin/bash

nom="Global"

modifier() {
    local nom="Local"
    echo "Dans la fonction : $nom"
}

echo "Avant : $nom"    # → Global
modifier               # → Local
echo "Après : $nom"    # → Global (pas affecté)
```


> **Bonne pratique :** utilise toujours `local` pour les variables internes d'une fonction.

### Valeurs par défaut pour les arguments

`${1:-"valeur"}` signifie : utilise `$1` s'il existe, sinon prends `"valeur"`.

```bash
saluer() {
    local nom=${1:-"Inconnu"}
    echo "Bonjour, $nom !"
}

saluer "Alice"    # → Bonjour, Alice !
saluer            # → Bonjour, Inconnu !
```


### Le code de retour d'une fonction (`return`)

```bash
fichier_existe() {
    if [[ -f "$1" ]]; then
        return 0    # Succès
    else
        return 1    # Échec
    fi
}

if fichier_existe "/etc/passwd"; then
    echo "Le fichier existe."
else
    echo "Le fichier n'existe pas."
fi
```


## Bonus

### Menu interactif avec `select`

`select` crée automatiquement un menu numéroté :

```bash
#!/bin/bash

echo "Que veux-tu faire ?"
select choix in "Lister les fichiers" "Afficher la date" "Quitter"; do
    case $choix in
        "Lister les fichiers") ls ;;
        "Afficher la date") date ;;
        "Quitter") echo "Au revoir." ; break ;;
        *) echo "Choix invalide." ;;
    esac
done
```


### Parser des arguments nommés avec `shift`

Pour les scripts avec des flags comme `-n 42 -s "texte"` :

```bash
#!/bin/bash

while [[ $# -gt 0 ]]; do
    case $1 in
        -n) nombre="$2" ; shift 2 ;;
        -s) texte="$2" ; shift 2 ;;
        -h) echo "Aide : $0 -n <nombre> -s <texte>" ; exit 0 ;;
        *) echo "Option inconnue : $1" ; exit 1 ;;
    esac
done

echo "Nombre : $nombre"
echo "Texte : $texte"
```


> **Note :** `shift` décale les arguments : l'ancien `$2` devient `$1`. `shift 2` décale de 2 positions. C'est comme ça qu'on "consomme" les flags un par un.

## ❌ Erreur classique

```bash
# Croire que return renvoie une chaîne
ma_fonction() {
    return "Hello"     # ❌ return ne prend qu'un nombre (0-255)
}

# Il faut utiliser echo :
ma_fonction() {
    echo "Hello"       # ✅ On capture avec $(ma_fonction)
}

# Appeler une fonction avec des parenthèses
saluer()               # ❌ Les parenthèses sont pour la DÉFINITION
saluer                 # ✅ Pour appeler, juste le nom
```


## Exercices

**Guidé :** Crée une fonction `maximum` qui prend deux nombres et affiche le plus grand. Teste-la avec `echo "Le max est $(maximum 10 25)"`.

**Autonome :** Crée un script `outil.sh` avec les options `-l` (lister les fichiers), `-d` (afficher la date), `-u` (afficher l'utilisateur) en utilisant `case` et des fonctions.
1
## 🧩 Mini-projet (chapitres 7-8)

Crée un script `gestion.sh` qui :

1. Propose un menu avec `case` : 1) Lister les fichiers .txt, 2) Compter les lignes d'un fichier, 3) Quitter
2. Chaque option appelle une fonction dédiée
3. La boucle `while true` permet de revenir au menu après chaque action
4. L'option "Quitter" utilise `break` pour sortir

## ✅ Tu sais maintenant...

- Définir, appeler et passer des arguments à une fonction
- Récupérer un résultat avec `echo` + `$(...)` (et non avec `return`)
- Utiliser `case` pour des choix multiples propres
- Protéger les variables internes avec `local`

---
