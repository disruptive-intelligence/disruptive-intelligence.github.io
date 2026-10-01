---
title: Chapitre 8 — Variables d'environnement et configuration du shell
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 2 — Manipuler le système de fichiers
  - index.md
---

## Le minimum à savoir

### Pourquoi certaines commandes marchent « partout »

Tu as remarqué que tu peux taper `ls` depuis **n'importe quel** dossier et que ça fonctionne ? Pourtant, `ls` est un programme rangé quelque part (dans `/bin` ou `/usr/bin`). Comment le shell le retrouve-t-il sans que tu donnes son chemin complet ? La réponse tient en un mot : **les variables d'environnement**. Comprendre ce mécanisme, c'est lever l'un des derniers mystères du terminal.

### Qu'est-ce qu'une variable d'environnement ?

Une **variable** est un nom qui stocke une valeur. Une variable d'**environnement** est une variable que le shell (et les programmes qu'il lance) peuvent consulter pour savoir « comment se comporter ». Pour lire la valeur d'une variable, on met un `$` devant son nom :

```bash
echo $HOME       # → /home/alice (ton dossier personnel)
echo $USER       # → alice       (ton nom d'utilisateur)
echo $SHELL      # → /bin/bash    (ton shell)
echo $PWD        # → le dossier courant (mis à jour à chaque cd)
```


Pour voir **toutes** les variables d'environnement d'un coup :

```bash
env              # liste toutes les variables d'environnement
printenv         # équivalent (printenv USER affiche juste celle-là)
```


| Variable | Ce qu'elle contient |
|----------|---------------------|
| `HOME` | Le chemin de ton dossier personnel |
| `USER` | Ton nom d'utilisateur |
| `SHELL` | Le shell que tu utilises |
| `PWD` | Le dossier de travail actuel |
| `PATH` | La liste des dossiers où le shell cherche les programmes *(voir ci-dessous)* |

### Le `PATH` : la clé du mystère

`PATH` est **la** variable à comprendre. Elle contient une liste de dossiers, séparés par des `:`, dans lesquels le shell va **chercher** les programmes que tu tapes :

```bash
echo $PATH
# → /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin
```


Quand tu tapes `ls`, le shell parcourt ces dossiers **dans l'ordre** jusqu'à trouver un programme nommé `ls`. C'est pour ça que `ls` marche partout : son dossier (`/bin`) est dans le `PATH`. Et c'est aussi pourquoi une commande que tu viens d'écrire toi-même ne marche **pas** directement : son dossier n'est pas dans le `PATH`.

### Où est ce programme ? `which` et `command -v`

Pour savoir **quel** fichier sera exécuté quand tu tapes une commande :

```bash
which ls             # → /usr/bin/ls (le chemin du programme trouvé via le PATH)
command -v ls        # → même résultat, forme plus moderne et portable
```


`command -v` fonctionne aussi avec les commandes internes au shell et les alias, là où `which` peut être limité. **Pour débuter, `which` suffit** ; garde `command -v` en tête comme la version « propre ».

## Très utile en pratique

### Créer une variable : `export`

Tu peux définir tes propres variables. Sans `export`, la variable n'existe que dans le shell courant ; **avec `export`**, elle devient une variable d'environnement, transmise aux programmes que tu lances :

```bash
MAVAR="bonjour"          # variable locale au shell
export MAVAR="bonjour"   # variable d'environnement (héritée par les programmes lancés)
echo $MAVAR              # → bonjour
```


Un exemple concret et utile : choisir l'éditeur que `sudoedit` (chapitre 6) va lancer :

```bash
export EDITOR=nano       # désormais sudoedit ouvrira nano
```


### Ajouter un dossier au `PATH`

Imaginons que tu ranges tes propres scripts dans un dossier `~/bin`. Pour pouvoir les lancer **par leur nom** depuis partout, il faut ajouter ce dossier au `PATH` :

```bash
mkdir -p ~/bin                       # crée le dossier pour tes scripts
export PATH="$HOME/bin:$PATH"        # ajoute ~/bin EN TÊTE du PATH
```


Décortiquons `"$HOME/bin:$PATH"` : on met ton nouveau dossier, un `:`, puis **l'ancien `PATH` en entier**. C'est crucial : on **ajoute** à la liste existante, on ne la remplace pas. Oublier `:$PATH` à la fin ferait disparaître l'accès à toutes les commandes habituelles le temps de la session.

### Les alias : des raccourcis personnels

Un **alias** est un surnom que tu donnes à une commande, souvent pour ajouter des options par défaut ou raccourcir une commande longue :

```bash
alias ll='ls -lah'           # désormais "ll" = "ls -lah"
alias ..='cd ..'             # remonter d'un dossier en tapant juste ..
alias                        # (seul) affiche tous tes alias actuels
```


> **Très utile en pratique :** les administrateurs créent souvent un alias `alias rm='rm -i'` pour que `rm` demande **toujours** confirmation. Un petit filet de sécurité permanent, dans l'esprit des règles d'or de la Partie 0.

### Rendre tout cela permanent : `.bashrc` et `source`

Voici le point essentiel : **tout ce qu'on vient de faire (variables, PATH, alias) disparaît quand tu fermes le terminal.** Chaque nouveau terminal repart à zéro. Pour rendre tes réglages **permanents**, on les écrit dans un fichier que le shell lit **automatiquement à chaque démarrage** : `~/.bashrc`.

C'est un fichier caché (il commence par un `.`, souviens-toi de `ls -a`) dans ton dossier personnel. On l'édite comme n'importe quel fichier — avec le réflexe `.bak` du chapitre 6 :

```bash
cp ~/.bashrc ~/.bashrc.bak           # 1. sauvegarde, toujours
nano ~/.bashrc                       # 2. on ajoute nos lignes à la fin :
                                     #    export PATH="$HOME/bin:$PATH"
                                     #    alias ll='ls -lah'
                                     #    alias rm='rm -i'
```


Mais attention : modifier `.bashrc` ne change **rien** dans le terminal déjà ouvert, puisqu'il n'est lu qu'au démarrage. Pour appliquer tes changements **immédiatement**, sans rouvrir de terminal, on utilise `source` :

```bash
source ~/.bashrc         # relit le fichier et applique les changements ici et maintenant
```


> **Le concept à retenir :** `.bashrc` est lu **automatiquement** au lancement de chaque shell. `source ~/.bashrc` le relit **manuellement** dans le terminal courant. On écrit ses réglages une fois dans `.bashrc`, puis on `source` pour les tester sans redémarrer.

### Le mystère du `./script.sh` enfin résolu

Tu te demandais peut-être pourquoi, pour lancer un script à toi, on écrit `./script.sh` et pas juste `script.sh` ? Maintenant tu as la réponse : le dossier courant (`.`) **n'est pas dans le `PATH`** (pour des raisons de sécurité). Le shell ne cherche donc pas tes programmes ici. En écrivant `./script.sh`, tu donnes explicitement le chemin (« le script `script.sh`, **ici** ») au lieu de compter sur le `PATH`. Et si tu ranges tes scripts dans `~/bin` ajouté au `PATH`, tu pourras les lancer par leur nom, de partout — comme une vraie commande.

## ❌ Erreur classique

```bash
# Oublier le $ pour LIRE une variable
echo PATH         # ❌ affiche littéralement le mot "PATH"
echo $PATH        # ✅ affiche le contenu de la variable

# Mettre un $ pour DÉFINIR une variable
$MAVAR="x"        # ❌ erreur de syntaxe
MAVAR="x"         # ✅ pas de $ à la définition, seulement à la lecture

# Mettre des espaces autour du =
MAVAR = "x"       # ❌ le shell croit à une commande "MAVAR"
MAVAR="x"         # ✅ pas d'espaces autour du =

# ÉCRASER le PATH au lieu d'y ajouter
export PATH="$HOME/bin"          # ❌❌ catastrophe : plus aucune commande ne marche
export PATH="$HOME/bin:$PATH"    # ✅ on ajoute, on garde l'ancien

# Modifier .bashrc et s'étonner que rien ne change
nano ~/.bashrc                   # modification faite...
# ❌ ...mais pas appliquée dans ce terminal
source ~/.bashrc                 # ✅ relit et applique maintenant
```


> **Si tu casses ton `PATH`** pendant une session (plus aucune commande ne répond), pas de panique : ferme et rouvre le terminal. Comme `.bashrc` n'avait pas été modifié, tu repars sur un `PATH` sain. C'est exactement pour ça qu'on garde un `.bashrc.bak`.

## Exercices

**Guidé :** Affiche le contenu de tes variables `HOME`, `USER` et `PATH` avec `echo`. Puis utilise `which` pour trouver où se trouvent les programmes `ls`, `cat` et `grep`. Sont-ils tous dans des dossiers présents dans ton `PATH` ?

**Autonome :** Crée un dossier `~/bin`. Ajoute-le à ton `PATH` avec `export` (en n'oubliant pas `:$PATH`). Vérifie avec `echo $PATH` qu'il apparaît bien. Crée ensuite un alias temporaire `alias jrnl='tail -f /var/log/syslog'` et teste-le. *(Cet alias disparaîtra à la fermeture du terminal — c'est voulu.)*

**Défi :** Rends tes réglages permanents proprement. Fais d'abord une copie `.bak` de ton `~/.bashrc`. Ajoute-y l'export de `~/bin` dans le `PATH` et un alias `ll='ls -lah'`. Applique avec `source ~/.bashrc`, puis teste `ll`. Ouvre enfin un **nouveau** terminal et vérifie que `ll` fonctionne toujours, prouvant que le réglage est bien devenu permanent.

## 🧩 Mini-projet (Partie 2) — Atelier de configuration

Mets en œuvre toute la Partie 2 dans un atelier réaliste, **sur des fichiers de test uniquement** (pas de vrai fichier système) :

1. **Construis** une arborescence de travail avec `mkdir -p` : `atelier/{scripts,configs,sauvegardes}`.
2. **Crée** dans `configs/` un fichier `app.conf` avec quelques lignes de réglages (via `nano` ou `echo >>`).
3. **Sauvegarde** : avant toute modification, copie `app.conf` en `app.conf.bak` (le réflexe).
4. **Modifie** `app.conf` (change une valeur), puis prouve le changement avec `diff app.conf.bak app.conf`.
5. **Journalise** : avec un pipe et `tee`, enregistre la liste de tes fichiers dans `atelier/inventaire.txt` tout en l'affichant.
6. **Personnalise** : ajoute dans ton `.bashrc` (après un `.bak` !) un alias `atelier='cd ~/atelier && ls -lah'`, applique avec `source`, et teste-le.
7. **Range** : déplace tes scripts dans le dossier prévu avec `mv`, et fais le ménage des fichiers de test inutiles avec `rm -i`.

À la fin, tu auras mobilisé création, copie, déplacement, suppression prudente, édition sécurisée, redirections et configuration du shell — tout le cœur de la Partie 2.

## ✅ Tu sais maintenant…

- Ce qu'est une **variable d'environnement** et comment la lire (`$NOM`, `env`, `printenv`)
- Le rôle des variables clés : `HOME`, `USER`, `SHELL`, `PWD`
- **Pourquoi** les commandes marchent partout grâce au `PATH`, et comment l'inspecter
- Localiser un programme avec `which` et `command -v`
- Créer des variables avec `export`, et **ajouter** un dossier au `PATH` sans l'écraser
- Créer des raccourcis avec `alias` (dont le filet de sécurité `rm -i`)
- Rendre tes réglages **permanents** dans `.bashrc` et les appliquer avec `source`
- **Pourquoi** on tape `./script.sh` (le `.` n'est pas dans le `PATH`)

---

> **🏁 CHECKPOINT 2 — Fin de la Partie 2**
>
> Tu es passé de l'observation à l'**action** : tu sais créer, organiser, éditer et supprimer des fichiers en toute prudence, faire circuler l'information entre les commandes, et façonner ton propre environnement de travail.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - créer une arborescence complète en une commande, puis la supprimer prudemment ?
> - modifier un fichier de configuration en gardant une sauvegarde et en vérifiant le changement avec `diff` ?
> - sortir de `vim` sans paniquer ?
> - expliquer la différence entre `>`, `>>` et `|` ?
> - dire pourquoi `ls` marche partout, et ajouter ton propre dossier au `PATH` de façon permanente ?
>
> Si oui, tu maîtrises les fondations pratiques de Linux. Place à la **Partie 3 — Qui a le droit de quoi**, le cœur conceptuel de l'administration et de la sécurité : permissions, utilisateurs, groupes et `sudo`.

---

---
---
