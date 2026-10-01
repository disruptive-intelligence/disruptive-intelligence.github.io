---
title: Chapitre 13 — Les processus
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 4 — La machine vivante
  - index.md
---

## Le minimum à savoir

### Programme vs processus

Un **programme** est un fichier sur le disque (le binaire `/usr/bin/firefox`, par exemple) : inerte, il ne fait rien. Quand tu le lances, le système en crée une copie active en mémoire : c'est un **processus**. Un même programme peut donner naissance à plusieurs processus en même temps (plusieurs fenêtres d'un éditeur, par exemple). Retiens la formule : **un processus est un programme en cours d'exécution**.

### Chaque processus a un numéro : le PID

Le système identifie chaque processus par un numéro unique, le **PID** (*Process ID*). C'est par ce numéro qu'on agit sur un processus (pour l'observer, le mettre en pause, l'arrêter). Chaque processus connaît aussi son « parent » (le processus qui l'a lancé), identifié par le **PPID** (*Parent PID*). Tous les processus descendent ainsi d'un ancêtre commun lancé au démarrage de la machine.

### Voir les processus : `ps`

`ps` (*process status*) liste les processus. La combinaison la plus utile est `ps aux`, qui montre **tous** les processus de **tous** les utilisateurs :

```bash
ps aux                   # tous les processus, avec utilisateur, PID, CPU, mémoire…
ps aux | grep firefox    # ne garder que les lignes liées à firefox (pipe du chapitre 7)
```


Les colonnes importantes : `USER` (qui l'a lancé), `PID` (son numéro), `%CPU` et `%MEM` (ce qu'il consomme), et la commande elle-même. Le `ps aux | grep ...` est un réflexe quotidien : « ce programme tourne-t-il, et sous quel PID ? ».

### Voir en temps réel : `top` et `htop`

`ps` donne une photo à un instant donné. Pour observer l'activité **en continu**, on utilise `top` (toujours présent) :

```bash
top                      # tableau de bord temps réel ; on quitte avec q
```


`top` affiche, rafraîchies en direct, la charge du système et les processus les plus gourmands. On le quitte avec `q` (comme `man` et `less`).

`htop` est une version plus colorée et plus lisible, qu'on installe au besoin (réflexe de la Partie 0) :

```bash
sudo apt install htop
htop                     # version améliorée et navigable de top
```


> **Très utile en pratique :** quand une machine devient lente, le premier geste est `top` ou `htop` pour voir **quel processus dévore le CPU ou la mémoire**. C'est le point de départ de presque tout diagnostic de performance (on y reviendra au chapitre 24).

## Très utile en pratique

### Arrêter un processus : les signaux et `kill`

Pour demander à un processus de s'arrêter, on lui envoie un **signal** avec `kill`, en lui donnant son PID :

```bash
kill 4821                # envoie le signal par défaut (TERM) : demande polie d'arrêt
kill -9 4821             # envoie KILL : arrêt FORCÉ, sans condition
```


Deux signaux à connaître :

- **TERM** (le défaut) : « termine-toi proprement ». Le processus peut sauvegarder et fermer correctement. **C'est celui qu'on essaie en premier.**
- **KILL** (`-9`) : « arrête-toi immédiatement », sans possibilité de se préparer. Brutal, à réserver aux processus qui ne répondent plus.

> **Le bon ordre :** toujours essayer `kill PID` (poli) d'abord. Ne passer à `kill -9 PID` que si le processus refuse de s'arrêter. Le `-9` est un dernier recours, pas la solution par défaut : il peut laisser des fichiers à moitié écrits ou des données perdues.

Pour arrêter tous les processus d'un même nom :

```bash
killall firefox          # arrête tous les processus nommés "firefox"
```


### Premier plan, arrière-plan : `&`, `jobs`, `fg`, `bg`

Quand tu lances une commande longue, elle occupe ton terminal jusqu'à la fin. Tu peux la lancer **en arrière-plan** avec `&` pour récupérer la main :

```bash
une-longue-commande &    # lance en arrière-plan, le terminal reste libre
jobs                     # liste les tâches lancées depuis ce terminal
fg                       # ramène une tâche au premier plan (foreground)
```


Tu peux aussi suspendre une commande en cours avec `Ctrl + Z`, puis la relancer en arrière-plan avec `bg` ou au premier plan avec `fg`. Pour débuter, l'essentiel est `&` (lancer en fond) et `Ctrl + C` (interrompre la commande au premier plan).

### La priorité : `nice` (notion)

Chaque processus a une priorité qui influence sa part de temps processeur. On peut lancer un programme avec une priorité réduite (pour qu'il ne ralentisse pas le reste) avec `nice`. À ton niveau, retiens simplement que ça **existe** : on peut rendre un processus « plus poli » envers les autres.

## ❌ Erreur classique

```bash
# Dégainer kill -9 d'emblée
kill -9 4821             # ❌ brutal, risque de perte de données
kill 4821                # ✅ d'abord la demande propre (TERM)

# Se tromper de PID et arrêter le mauvais processus
kill 1                   # ❌❌ PID 1 = le processus maître du système, NE JAMAIS toucher
ps aux | grep le-bon-nom # ✅ vérifie le PID AVANT d'agir

# Confondre le nom et le PID
kill firefox             # ❌ kill attend un numéro, pas un nom
killall firefox          # ✅ killall travaille par nom
kill 4821                # ✅ kill travaille par PID

# Croire que fermer le terminal arrête un processus en arrière-plan
commande &               # selon les cas, peut continuer après fermeture du terminal
```


> **Ne touche jamais au PID 1.** C'est le tout premier processus, l'ancêtre de tous les autres (souvent `systemd`, voir chapitre suivant). L'arrêter reviendrait à éteindre brutalement le système.

## Exercices

**Guidé :** Lance `top`, observe quelques secondes quel processus consomme le plus de CPU et de mémoire, puis quitte avec `q`. Ensuite, avec `ps aux | grep bash`, retrouve le PID de ton propre shell. Compare-le à ce qu'affiche la variable spéciale `echo $$` (qui donne le PID du shell courant) : est-ce le même ?

**Autonome :** Lance une commande qui tourne longtemps en arrière-plan, par exemple `sleep 300 &` (attend 300 secondes sans rien faire). Liste-la avec `jobs`, retrouve son PID avec `ps aux | grep sleep`, puis arrête-la proprement avec `kill <PID>`. Vérifie avec `jobs` ou `ps` qu'elle a bien disparu.

**Défi (orientation sécurité) :** Lance `ps aux` et parcours la liste des processus. Pour chacun, demande-toi : est-ce que je reconnais ce programme et l'utilisateur qui le lance ? Sur une vraie machine, un analyste cherche ici un processus au **nom inhabituel**, lancé depuis un **emplacement suspect** (comme `/tmp`), ou consommant des ressources anormales. Repère le processus avec le plus gros `%CPU` et identifie de quel programme il s'agit : est-il légitime ?

## ✅ Tu sais maintenant…

- La différence entre **programme** (fichier inerte) et **processus** (programme en exécution)
- Que chaque processus a un **PID** (et un **PPID**, son parent)
- Lister les processus avec `ps aux` (souvent suivi de `| grep`)
- Observer l'activité **en temps réel** avec `top` et `htop` (sortie : `q`)
- Arrêter un processus avec `kill PID` (poli) puis `kill -9 PID` (forcé, en dernier recours), et `killall nom`
- Gérer l'arrière-plan avec `&`, `jobs`, `fg`, et interrompre avec `Ctrl + C`
- Qu'on ne touche **jamais** au PID 1, et qu'un processus suspect se repère par son nom, son origine et sa consommation

---
