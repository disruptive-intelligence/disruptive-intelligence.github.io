---
title: Chapitre 3 — Arguments et variables spéciales
source: IT/07 Scripting & programmation/Shell/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### C'est quoi un argument ?

Au lieu que le script pose des questions (avec `read`), tu peux lui **donner des infos directement** quand tu le lances :

```bash
./saluer.sh Alice
#                 ↑ c'est un argument
```


### Les paramètres positionnels

Chaque argument est stocké dans une variable numérotée :

```
./mon_script.sh  pomme   banane  cerise
       $0          $1      $2      $3
```


- `$0` → le nom du script
- `$1` → le premier argument
- `$2` → le deuxième
- `$3` → le troisième...

Exemple :

```bash
#!/bin/bash
echo "Bonjour, $1 !"
```


```bash
./saluer.sh Alice     # → Bonjour, Alice !
./saluer.sh Bob       # → Bonjour, Bob !
```


### Les variables spéciales essentielles

| Variable      | Contenu                                       |
| ------------- | --------------------------------------------- |
| `$0`          | Le nom du script                              |
| `$1`, `$2`... | Les arguments par position                    |
| `$#`          | Le **nombre** d'arguments                     |
| `$@`          | **Tous** les arguments (séparément)           |
| `$?`          | Le **code de sortie** de la dernière commande |

Exemple :

```bash
#!/bin/bash

echo "Nom du script : $0"
echo "Nombre d'arguments : $#"
echo "Tous les arguments : $@"
echo "Premier : $1"
echo "Deuxième : $2"
```


```bash
./infos.sh pomme banane cerise
```


```
Nom du script : ./infos.sh
Nombre d'arguments : 3
Tous les arguments : pomme banane cerise
Premier : pomme
Deuxième : banane
```


### Vérifier qu'un argument est fourni

Un script qui attend un argument devrait **toujours vérifier** qu'il a été donné :

```bash
#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Erreur : donne un prénom en argument !"
    echo "Utilisation : $0 <prénom>"
    exit 1
fi

echo "Bonjour, $1 !"
```


> **Explication :** `-z` teste si la chaîne est vide. Si `$1` est vide (= pas d'argument), on affiche un message d'erreur et on quitte. On verra les conditions en détail au chapitre 6.

### La variable `$?`

Chaque commande renvoie un code de sortie. `$?` contient le code de la **dernière commande** :

```bash
ls /tmp
echo $?           # → 0 (succès, le dossier existe)

ls /dossier_inexistant
echo $?           # → 2 (erreur, le dossier n'existe pas)
```


## Très utile en pratique

### Utiliser plusieurs arguments

```bash
#!/bin/bash
echo "Comparaison de $1 et $2"
echo "Taille de $1 :"
wc -c < "$1"
echo "Taille de $2 :"
wc -c < "$2"
```


> **Bonne pratique :** mets toujours `"$1"` entre guillemets (pas `$1` nu). Ça évite les problèmes si le nom de fichier contient des espaces.

### Différence entre `$@` et `$*`

```bash
./test.sh "Jean Pierre" Marie
```


- `"$@"` → préserve chaque argument : `"Jean Pierre"` et `"Marie"` (2 éléments)
- `"$*"` → fusionne tout : `"Jean Pierre Marie"` (1 seul bloc)

**Utilise `"$@"` dans la grande majorité des cas.**

## Bonus

### La variable `$$`

`$$` contient le numéro de processus (PID) du script. Utile pour créer des fichiers temporaires uniques :

```bash
fichier_temp="/tmp/script_$$.tmp"
```


### La commande `shift`

`shift` décale tous les arguments d'une position : `$2` devient `$1`, `$3` devient `$2`, etc. On l'utilisera au chapitre 8 pour parser des options avancées.

## ❌ Erreur classique

```bash
# Oublier de vérifier si l'argument existe
echo "Bonjour, $1"    # Si lancé sans argument → "Bonjour, " (chaîne vide, pas d'erreur)

# Ne pas mettre de guillemets
cat $1                 # ❌ Plante si le fichier s'appelle "mon document.txt"
cat "$1"               # ✅ Correct
```


## Exercices

**Guidé :** Crée un script `bonjour_arg.sh` qui prend un prénom en argument, vérifie qu'il est fourni, et affiche "Bonjour, [prénom] !"

**Autonome :** Crée un script `chercher.sh` qui prend un nom de fichier en argument et le cherche sur le système : `find / -iname "$1" 2>/dev/null`

## ✅ Tu sais maintenant...

- Passer des arguments à un script (`$1`, `$2`...)
- Connaître le nombre d'arguments avec `$#`
- Récupérer tous les arguments avec `$@`
- Vérifier le code de retour avec `$?`
- Vérifier qu'un argument existe avant de l'utiliser

---
