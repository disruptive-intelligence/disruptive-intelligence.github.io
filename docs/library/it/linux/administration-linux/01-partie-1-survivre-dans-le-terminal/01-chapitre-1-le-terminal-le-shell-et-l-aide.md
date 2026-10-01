---
title: Chapitre 1 — Le terminal, le shell et l'aide
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 1 — Survivre dans le terminal
  - index.md
---

## Le minimum à savoir

### Terminal, shell : quelle différence ?

Quand tu ouvres une « fenêtre noire » pour taper des commandes, deux choses travaillent ensemble :

- Le **terminal**, c'est la fenêtre elle-même : l'endroit où s'affiche le texte et où tu tapes.
- Le **shell**, c'est le programme qui tourne *dans* cette fenêtre, qui **lit** ce que tu tapes et **exécute** tes commandes. Le shell le plus courant s'appelle **Bash**.

Une image simple : le terminal est le **téléphone** (l'appareil), le shell est la **personne** à l'autre bout qui comprend ce que tu dis et agit. Pour débuter, tu peux utiliser les deux mots de façon assez interchangeable ; retiens juste que c'est le shell qui « comprend » tes commandes.

### Lire le prompt (l'invite de commande)

Quand le terminal est prêt, il affiche une **invite de commande** (ou *prompt*). Elle ressemble souvent à ceci :

```
alice@serveur:~$
```


Décortiquons-la, car elle est pleine d'informations utiles :

- `alice` → ton nom d'utilisateur (qui tu es)
- `serveur` → le nom de la machine (où tu es connecté)
- `~` → le dossier où tu te trouves actuellement (`~` signifie « ton dossier personnel »)
- `$` → indique que tu es un utilisateur normal *(un `#` à la place signifierait que tu es root, le super-administrateur)*

> **Le `$` final est un repère essentiel.** Dans ce cours, quand tu vois `$` au début d'une ligne d'exemple, ça représente le prompt : tu ne tapes pas le `$`, seulement ce qui suit.

### L'anatomie d'une commande

Presque toutes les commandes suivent la même structure :

```
commande   -options   arguments
```


Exemple concret :

```bash
ls -l /home
```


- `ls` → la **commande** (ici : « lister le contenu d'un dossier »)
- `-l` → une **option** (ici : « format long », avec plus de détails). Les options modifient le comportement de la commande et commencent presque toujours par `-`.
- `/home` → l'**argument** (ici : *quel* dossier lister)

Cette structure est universelle. Dès que tu vois une commande inconnue, essaie de la découper ainsi : quelle est l'action ? quels réglages ? sur quoi ?

### Tes premières commandes

Voici quatre commandes inoffensives pour te faire la main. Elles ne modifient rien.

```bash
whoami       # affiche ton nom d'utilisateur
hostname     # affiche le nom de la machine
date         # affiche la date et l'heure
echo Bonjour # affiche le texte que tu lui donnes
```


`echo` mérite une mention : elle se contente d'**afficher** ce que tu lui passes. Ça semble inutile, mais c'est l'une des commandes les plus utilisées en pratique (pour afficher des messages, vérifier une valeur, écrire dans des fichiers plus tard…).

```bash
echo "Le terminal n'est pas si effrayant"
```


## Très utile en pratique

### Trouver de l'aide tout seul

Personne ne connaît toutes les commandes par cœur. Le vrai réflexe d'un bon administrateur, ce n'est pas de tout savoir, c'est de **savoir où chercher**. Linux embarque sa propre documentation.

**Le manuel : `man`**

```bash
man ls
```


Cela ouvre le **manuel** de la commande `ls` : description, liste des options, exemples. Tu navigues avec les flèches, et tu **quittes en appuyant sur la touche `q`** (pour *quit*). Retiens bien ce `q`, c'est la sortie de secours de beaucoup d'outils.

**L'aide rapide : `--help`**

Plus court que le manuel, souvent suffisant :

```bash
ls --help
```


Cela affiche un résumé des options directement dans le terminal, sans ouvrir de manuel.

**Chercher une commande par mot-clé : `apropos`**

Tu ne connais pas le nom de la commande, mais tu sais ce que tu veux faire ?

```bash
apropos copy     # liste les commandes liées à "copy"
```


**Savoir ce qu'est une commande : `type`**

```bash
type ls          # te dit si c'est un programme, un alias, etc.
```


### L'historique : ne retape jamais deux fois

Le shell **se souvient** de ce que tu as tapé. Deux outils t'évitent de retaper :

- La **flèche du haut (↑)** rappelle les commandes précédentes, une par une.
- La commande `history` affiche toute la liste de ce que tu as tapé.

```bash
history          # affiche l'historique numéroté de tes commandes
```


Et pour repartir d'un écran propre :

```bash
clear            # efface l'écran (l'historique, lui, reste intact)
```


> **Astuce :** la combinaison de touches `Ctrl + L` fait la même chose que `clear`, sans rien taper.

## ❌ Erreur classique

```bash
# Taper la commande pour quitter "man" au lieu d'appuyer sur q
man ls
quit             # ❌ ne fait rien d'utile, tu es toujours dans le manuel
# ✅ Appuie simplement sur la touche q

# Confondre option et argument
ls /home -l      # fonctionne souvent, mais l'ordre logique est :
ls -l /home      # ✅ options d'abord, arguments ensuite

# Oublier que Linux est sensible à la casse
Date             # ❌ commande introuvable
date             # ✅ tout en minuscules

# Croire qu'il faut taper le $ du prompt
$ whoami         # ❌ le $ représente le prompt, ne le tape pas
whoami           # ✅
```


> **La sensibilité à la casse** est une source d'erreurs constante chez les débutants. Sous Linux, `Date`, `DATE` et `date` sont trois choses différentes. La quasi-totalité des commandes sont en **minuscules**.

## Exercices

**Guidé :** Ouvre le manuel de la commande `date` avec `man date`. Cherche dans le manuel comment afficher uniquement l'année (indice : il existe un format avec `+%Y`). Quitte le manuel avec `q`, puis teste la commande que tu as trouvée.

**Autonome :** Sans utiliser Internet, trouve à quoi sert la commande `uptime` (utilise `man` ou `--help`), puis exécute-la. Que t'apprend-elle sur la machine ?

**Défi :** Utilise `apropos` pour trouver une commande qui affiche le calendrier du mois. Une fois trouvée, exécute-la, puis consulte son manuel pour afficher le calendrier de l'année entière.

## ✅ Tu sais maintenant…

- La différence entre le **terminal** (la fenêtre) et le **shell** (le programme qui exécute)
- Lire un **prompt** : qui tu es, où tu es, et si tu es root (`$` vs `#`)
- Décortiquer une commande en **commande + options + arguments**
- Afficher des informations de base : `whoami`, `hostname`, `date`, `echo`
- Te débloquer seul avec `man`, `--help`, `apropos` et `type` (et **quitter `man` avec `q`**)
- Réutiliser tes commandes avec la **flèche du haut** et `history`
- Que Linux est **sensible à la casse** : `date` ≠ `Date`

---
