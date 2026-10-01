---
title: Chapitre 3 — Lire le contenu des fichiers
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 1 — Survivre dans le terminal
  - index.md
---

## Le minimum à savoir

### Pourquoi lire avant d'agir

En administration, **on regarde avant de toucher**. Avant de modifier une configuration, on la lit. Avant de supprimer un fichier, on vérifie son contenu. Avant de comprendre un problème, on lit les logs. Ce chapitre te donne les outils pour **consulter** un fichier sans aucun risque de le modifier — c'est la suite logique de notre approche « lecture seule ».

### Texte ou binaire ? `file`

Tous les fichiers ne se lisent pas de la même façon. Un fichier **texte** (configuration, log, script) se lit directement. Un fichier **binaire** (image, programme) afficherait du charabia illisible si tu tentais de le lire comme du texte. Avant de lire un fichier inconnu, demande à Linux de quoi il s'agit :

```bash
file /etc/hostname       # → texte
file /bin/ls             # → exécutable (binaire)
```


> **Réflexe utile :** si une commande de lecture remplit ton écran de symboles incompréhensibles et fait « biper » le terminal, c'est probablement un fichier binaire. Ferme avec `q` ou `Ctrl + C`, et vérifie avec `file`.

### Afficher un fichier entier : `cat`

`cat` affiche tout le contenu d'un fichier d'un coup :

```bash
cat /etc/hostname        # affiche le nom de la machine
```


`cat` est parfait pour les **petits** fichiers. Mais sur un gros fichier (un log de plusieurs milliers de lignes), tout défile d'un coup et tu ne vois que la fin : peu pratique. D'où les outils suivants.

### Lire confortablement : `less`

`less` affiche un fichier **page par page**, sans tout déverser à l'écran :

```bash
less /var/log/syslog
```


Pendant que `less` est ouvert :

- **Flèches** ou **Espace** → naviguer (Espace = page suivante)
- **`/motcherché`** → rechercher un mot dans le fichier
- **`q`** → quitter (le même `q` que pour `man` — et pour cause, `man` utilise `less` !)

> **Le minimum à savoir :** pour les **petits** fichiers, `cat`. Pour les **gros** fichiers, `less`. Cette distinction simple t'évite bien des écrans qui défilent dans le vide.

### Voir le début ou la fin : `head` et `tail`

Souvent, tu ne veux que le **début** ou la **fin** d'un fichier :

```bash
head fichier.log         # les 10 premières lignes
tail fichier.log         # les 10 dernières lignes
head -n 5 fichier.log    # les 5 premières lignes
tail -n 20 fichier.log   # les 20 dernières lignes
```


`tail` est particulièrement précieux pour les logs : les événements les plus récents sont **à la fin** du fichier. Quand un problème vient de se produire, `tail` te montre tout de suite ce qui s'est passé en dernier.

## Très utile en pratique

### Suivre un log en direct : `tail -f`

Voici l'une des commandes les plus utiles de tout le cours. L'option `-f` (*follow*, « suivre ») garde le fichier ouvert et affiche **les nouvelles lignes en temps réel**, au fur et à mesure qu'elles s'ajoutent :

```bash
tail -f /var/log/syslog
```


L'écran ne se ferme pas : il attend et affiche chaque nouvel événement dès qu'il arrive. C'est exactement ce qu'on utilise pour **observer un système en train de fonctionner** : surveiller les connexions, voir un service démarrer, repérer une erreur dès qu'elle survient. Pour arrêter le suivi, appuie sur **`Ctrl + C`**.

> **Très utile en sécurité (SOC) :** `tail -f` sur un journal d'authentification permet de voir **en direct** les tentatives de connexion à une machine. C'est un réflexe d'analyste : ouvrir le log, le suivre, et regarder ce qui frappe à la porte.

### Compter : `wc`

`wc` (*word count*) compte les lignes, les mots et les caractères d'un fichier :

```bash
wc fichier.txt           # lignes, mots, caractères
wc -l fichier.txt        # uniquement le nombre de LIGNES
```


L'option `-l` est la plus utilisée : « combien de lignes ? » est une question fréquente (combien d'événements dans ce log ? combien d'utilisateurs dans ce fichier ?). On l'exploitera beaucoup au chapitre 4.

### Numéroter les lignes : `nl`

Pratique pour discuter d'un fichier ligne par ligne, ou repérer une ligne précise :

```bash
nl fichier.conf          # affiche le fichier avec un numéro devant chaque ligne
```


## ❌ Erreur classique

```bash
# Faire un "cat" sur un fichier énorme
cat /var/log/syslog      # ❌ des milliers de lignes défilent, illisible
less /var/log/syslog     # ✅ page par page

# Faire un "cat" sur un binaire
cat /bin/ls              # ❌ charabia + bips, le terminal devient bizarre
file /bin/ls             # ✅ vérifie d'abord ce que c'est

# Rester coincé dans less sans savoir en sortir
# ✅ La sortie est TOUJOURS la touche q

# Oublier le -n et passer un nombre directement
head -5 fichier          # fonctionne sur beaucoup de systèmes, mais
head -n 5 fichier        # ✅ la forme correcte et portable

# Lancer tail -f et croire que le terminal est figé
tail -f log              # il n'est pas figé, il ATTEND de nouvelles lignes
# ✅ Ctrl + C pour reprendre la main
```


> **Si ton terminal devient illisible** après avoir affiché un binaire (caractères bizarres même quand tu tapes), la commande `reset` le remet d'aplomb.

## Exercices

**Guidé :** Affiche les 3 premières lignes du fichier `/etc/passwd` avec `head`, puis ses 3 dernières lignes avec `tail`. Ensuite, compte combien de lignes contient ce fichier avec `wc -l`. Chaque ligne correspond à un compte utilisateur du système : combien y en a-t-il ?

**Autonome :** Utilise `file` sur trois éléments différents : `/etc/hostname`, `/bin/ls` et le dossier `/etc` lui-même. Note ce que `file` répond pour chacun. Lequel peux-tu lire avec `cat` sans danger ?

**Défi :** Lance `tail -f /var/log/syslog` dans ton terminal pour suivre le journal système en direct. Pendant que ça tourne, observe si de nouvelles lignes apparaissent. Au bout d'un moment, arrête proprement le suivi. *(Si `/var/log/syslog` n'existe pas sur ton système, on verra au chapitre 4 et 15 où trouver les bons journaux selon ta distribution.)*

## ✅ Tu sais maintenant…

- Que l'on **lit avant d'agir** : consulter un fichier ne le modifie jamais
- Distinguer un fichier **texte** d'un **binaire** avec `file`
- Afficher un fichier : `cat` pour les petits, `less` pour les gros (sortie : `q`)
- Voir le **début** (`head`) et la **fin** (`tail`) d'un fichier, avec `-n`
- Suivre un log **en temps réel** avec `tail -f` (et reprendre la main avec `Ctrl + C`)
- **Compter** les lignes d'un fichier avec `wc -l`
- Numéroter les lignes avec `nl`, et réparer un terminal abîmé avec `reset`

---
