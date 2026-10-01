---
title: Chapitre 4 — Redirections, erreurs et pipes
source: IT/07 Scripting & programmation/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Les 3 flux de données

Chaque commande travaille avec trois flux :

```
                  ┌──────────────┐
  Entrée ───────▶ │   Commande   │ ──▶ 1 = Sortie normale (stdout)
  (clavier)       │              │ ──▶ 2 = Erreurs (stderr)
                  └──────────────┘
```


| Numéro | Nom                         | Par défaut  |
| ------ | --------------------------- | ----------- |
| 0      | stdin (entrée)              | Le clavier  |
| **1**  | **stdout (sortie normale)** | **L'écran** |
| **2**  | **stderr (erreurs)**        | **L'écran** |

Les redirections permettent de **changer la destination** de ces flux.

### Rediriger la sortie vers un fichier

**Écraser avec `>` :**

```bash
echo "Bonjour" > message.txt   # Crée le fichier (ou l'écrase !)
ls /etc > liste.txt            # La liste va dans le fichier
```


**Ajouter avec `>>` :**

```bash
echo "Ligne 1" > journal.txt       # Crée le fichier
echo "Ligne 2" >> journal.txt      # Ajoute à la suite
echo "Ligne 3" >> journal.txt      # Ajoute encore
```


> **À retenir :** `>` écrase, `>>` ajoute. Confondre les deux = perdre des données.

### Rediriger les erreurs

```bash
# Les erreurs vont dans un fichier, la sortie normale s'affiche à l'écran
ls /dossier_inexistant 2> erreurs.txt

# Masquer les erreurs en les envoyant dans le "trou noir"
find / -name "mon_fichier" 2>/dev/null
```


`/dev/null` est une "poubelle" : tout ce qu'on y envoie disparaît.

### Rediriger tout (sortie + erreurs)

```bash
# Tout va dans le même fichier
./mon_script.sh > log.txt 2>&1 # > log.txt 2>&1 = "flux 1 va dans log.txt, et flux 2 suit flux 1" → tout finit dans log.txt.

# Tout dans le vide (script silencieux)
./mon_script.sh > /dev/null 2>&1
```


> **Explication de `2>&1` :** "envoie le flux 2 (erreurs) au même endroit que le flux 1 (sortie normale)".

### Les pipes `|`

Le pipe envoie la **sortie d'une commande comme entrée d'une autre**. C'est l'outil le plus puissant de Bash.

```bash
# Compter le nombre de fichiers
ls | wc -l

# Chercher un mot dans un résultat
ps aux | grep firefox

# Trier et garder les lignes uniques
cat prenoms.txt | sort | uniq
```


Chaque commande reçoit la sortie de la précédente. C'est une chaîne de traitement.

> **Note :** ces exemples sont volontairement simples pour comprendre le principe d'un pipe. Tu verras plus tard qu'en Bash, certaines alternatives sont plus robustes selon le contexte.

### La commande `tee`

`tee` permet d'**afficher ET sauvegarder** en même temps :

```bash
# Affiche à l'écran ET écrit dans log.txt
ls -la | tee log.txt

# Ajouter au fichier (au lieu d'écraser)
date | tee -a journal.log
```


## Très utile en pratique

### Rediriger l'entrée avec `<`

```bash
# Compter les lignes d'un fichier
wc -l < mon_fichier.txt

# Trier le contenu d'un fichier
sort < liste_noms.txt
```


### Enchaîner plusieurs pipes

```bash
# Les 5 plus gros fichiers
ls -lS | head -5

# Compter les fichiers .txt dans /etc
ls /etc | grep "\.txt" | wc -l
```


## Récapitulatif

| Syntaxe                     | Effet                           |
| --------------------------- | ------------------------------- |
| `commande > fichier`        | Sortie dans fichier (écrase)    |
| `commande >> fichier`       | Sortie dans fichier (ajoute)    |
| `commande 2> fichier`       | Erreurs dans fichier            |
| `commande > fichier 2>&1`   | Tout dans fichier               |
| `commande < fichier`        | Entrée depuis un fichier        |
| `cmd1 \| cmd2`              | Sortie de cmd1 → entrée de cmd2 |
| `commande \| tee fichier`   | Affiche ET sauvegarde           |
| `commande > /dev/null 2>&1` | Silence total                   |

## ❌ Erreur classique

```bash
# Confondre > et >> : tu écrases un fichier important !
echo "nouveau" > config.txt     # ❌ Tout l'ancien contenu est perdu
echo "nouveau" >> config.txt    # ✅ Ajoute à la fin

# Oublier 2> : les erreurs s'affichent en vrac et polluent la sortie
find / -name "*.log"            # ❌ Des dizaines de "Permission denied"
find / -name "*.log" 2>/dev/null  # ✅ Erreurs masquées
```


## Exercices

**Guidé :** Écris le résultat de `date` dans un fichier `log.txt` avec `>`, puis ajoute une deuxième date avec `>>`. Affiche le contenu avec `cat log.txt`.

**Autonome :** Crée un script qui compte le nombre de lignes de `/etc/passwd` en utilisant un pipe (`wc -l`), et qui utilise `tee` pour afficher le résultat ET l'écrire dans un fichier.

## 🧩 Mini-projet (chapitres 3-4)

Crée un script `rapport.sh` qui :

1. Prend un dossier en argument (vérifie qu'il est fourni)
2. Compte le nombre de fichiers dans ce dossier (`ls "$1" | wc -l`)
3. Écrit un mini-rapport dans `rapport.txt` avec la date, le dossier, et le nombre de fichiers
4. Affiche le rapport à l'écran avec `cat`

## ✅ Tu sais maintenant...

- Rediriger la sortie vers un fichier (`>`, `>>`)
- Rediriger les erreurs (`2>`, `2>&1`)
- Masquer les erreurs avec `/dev/null`
- Enchaîner des commandes avec le pipe `|`
- Afficher et sauvegarder en même temps avec `tee`

---
