---
title: PARTIE 4 — La machine vivante
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 4
chapters: 7
---

Jusqu'ici, tu manipulais des fichiers « au repos ». Maintenant, on regarde le système **en train de fonctionner** : les programmes qui tournent (processus), ceux qui tournent en permanence (services), ce que la machine raconte sur elle-même (logs), et comment lui faire faire des choses automatiquement dans le temps (tâches planifiées). C'est le passage de « gérer des fichiers » à « administrer une machine vivante ».

---


## Chapitre 13 — Les processus

### Le minimum à savoir

#### Programme vs processus

Un **programme** est un fichier sur le disque (le binaire `/usr/bin/firefox`, par exemple) : inerte, il ne fait rien. Quand tu le lances, le système en crée une copie active en mémoire : c'est un **processus**. Un même programme peut donner naissance à plusieurs processus en même temps (plusieurs fenêtres d'un éditeur, par exemple). Retiens la formule : **un processus est un programme en cours d'exécution**.

#### Chaque processus a un numéro : le PID

Le système identifie chaque processus par un numéro unique, le **PID** (*Process ID*). C'est par ce numéro qu'on agit sur un processus (pour l'observer, le mettre en pause, l'arrêter). Chaque processus connaît aussi son « parent » (le processus qui l'a lancé), identifié par le **PPID** (*Parent PID*). Tous les processus descendent ainsi d'un ancêtre commun lancé au démarrage de la machine.

#### Voir les processus : `ps`

`ps` (*process status*) liste les processus. La combinaison la plus utile est `ps aux`, qui montre **tous** les processus de **tous** les utilisateurs :

```bash
ps aux                   # tous les processus, avec utilisateur, PID, CPU, mémoire…
ps aux | grep firefox    # ne garder que les lignes liées à firefox (pipe du chapitre 7)
```

Les colonnes importantes : `USER` (qui l'a lancé), `PID` (son numéro), `%CPU` et `%MEM` (ce qu'il consomme), et la commande elle-même. Le `ps aux | grep ...` est un réflexe quotidien : « ce programme tourne-t-il, et sous quel PID ? ».

#### Voir en temps réel : `top` et `htop`

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

### Très utile en pratique

#### Arrêter un processus : les signaux et `kill`

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

#### Premier plan, arrière-plan : `&`, `jobs`, `fg`, `bg`

Quand tu lances une commande longue, elle occupe ton terminal jusqu'à la fin. Tu peux la lancer **en arrière-plan** avec `&` pour récupérer la main :

```bash
une-longue-commande &    # lance en arrière-plan, le terminal reste libre
jobs                     # liste les tâches lancées depuis ce terminal
fg                       # ramène une tâche au premier plan (foreground)
```

Tu peux aussi suspendre une commande en cours avec `Ctrl + Z`, puis la relancer en arrière-plan avec `bg` ou au premier plan avec `fg`. Pour débuter, l'essentiel est `&` (lancer en fond) et `Ctrl + C` (interrompre la commande au premier plan).

#### La priorité : `nice` (notion)

Chaque processus a une priorité qui influence sa part de temps processeur. On peut lancer un programme avec une priorité réduite (pour qu'il ne ralentisse pas le reste) avec `nice`. À ton niveau, retiens simplement que ça **existe** : on peut rendre un processus « plus poli » envers les autres.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Lance `top`, observe quelques secondes quel processus consomme le plus de CPU et de mémoire, puis quitte avec `q`. Ensuite, avec `ps aux | grep bash`, retrouve le PID de ton propre shell. Compare-le à ce qu'affiche la variable spéciale `echo $$` (qui donne le PID du shell courant) : est-ce le même ?

**Autonome :** Lance une commande qui tourne longtemps en arrière-plan, par exemple `sleep 300 &` (attend 300 secondes sans rien faire). Liste-la avec `jobs`, retrouve son PID avec `ps aux | grep sleep`, puis arrête-la proprement avec `kill <PID>`. Vérifie avec `jobs` ou `ps` qu'elle a bien disparu.

**Défi (orientation sécurité) :** Lance `ps aux` et parcours la liste des processus. Pour chacun, demande-toi : est-ce que je reconnais ce programme et l'utilisateur qui le lance ? Sur une vraie machine, un analyste cherche ici un processus au **nom inhabituel**, lancé depuis un **emplacement suspect** (comme `/tmp`), ou consommant des ressources anormales. Repère le processus avec le plus gros `%CPU` et identifie de quel programme il s'agit : est-il légitime ?

### ✅ Tu sais maintenant…

- La différence entre **programme** (fichier inerte) et **processus** (programme en exécution)
- Que chaque processus a un **PID** (et un **PPID**, son parent)
- Lister les processus avec `ps aux` (souvent suivi de `| grep`)
- Observer l'activité **en temps réel** avec `top` et `htop` (sortie : `q`)
- Arrêter un processus avec `kill PID` (poli) puis `kill -9 PID` (forcé, en dernier recours), et `killall nom`
- Gérer l'arrière-plan avec `&`, `jobs`, `fg`, et interrompre avec `Ctrl + C`
- Qu'on ne touche **jamais** au PID 1, et qu'un processus suspect se repère par son nom, son origine et sa consommation

---


## Chapitre 14 — Les services avec systemd

### Le minimum à savoir

#### Qu'est-ce qu'un service (ou démon) ?

Certains programmes ne sont pas faits pour être lancés à la main puis fermés : ils doivent tourner **en permanence**, en arrière-plan, prêts à répondre à tout moment. C'est le cas d'un serveur web, d'une base de données, ou du **serveur SSH** qui attend les connexions distantes. Ces programmes de fond s'appellent des **services**, ou **démons** (*daemons*). Leur nom se termine souvent par un `d` : `sshd` (SSH daemon), `cron`, etc.

#### systemd : le chef d'orchestre

Au démarrage de la machine, quelque chose doit lancer tous ces services dans le bon ordre, les surveiller, les redémarrer s'ils tombent. Sur la quasi-totalité des distributions modernes, ce rôle est tenu par **systemd**. C'est lui le fameux **PID 1** du chapitre précédent : le tout premier processus, ancêtre de tous les autres. systemd gère des unités appelées **units**, dont les plus courantes sont les services (`.service`).

#### Piloter un service : `systemctl`

L'outil unique pour gérer les services est `systemctl`. Sa logique est simple et régulière :

```bash
systemctl status ssh         # quel est l'état du service SSH ? (actif ? en erreur ?)
sudo systemctl start ssh     # démarre le service
sudo systemctl stop ssh      # arrête le service
sudo systemctl restart ssh   # redémarre (stop puis start)
sudo systemctl reload ssh    # recharge la config sans interrompre le service
```

La commande la plus utile au quotidien est `status` : elle te dit si le service tourne, depuis quand, et affiche ses dernières lignes de journal — précieux pour comprendre un problème.

> **Le minimum à savoir :** `systemctl status nom-du-service` pour diagnostiquer, `start`/`stop`/`restart` pour agir. Les actions qui modifient l'état (start, stop, restart) demandent `sudo` ; consulter le `status` est souvent possible sans.

#### Démarrage automatique : `enable` et `disable`

Démarrer un service avec `start` ne le relance **pas** au prochain redémarrage de la machine. Pour qu'un service se lance **automatiquement au boot**, il faut l'**activer** :

```bash
sudo systemctl enable ssh    # SSH démarrera automatiquement à chaque démarrage
sudo systemctl disable ssh   # SSH ne démarrera plus automatiquement
sudo systemctl enable --now ssh   # active ET démarre tout de suite
```

> **Distinction essentielle :** `start` agit **maintenant** (jusqu'au prochain reboot), `enable` agit **au démarrage** (de façon permanente). On les confond souvent. Un service qu'on veut voir tourner durablement doit être à la fois **démarré** et **activé** — d'où le pratique `enable --now`.

### Très utile en pratique

#### Lister et explorer les services

```bash
systemctl list-units --type=service          # tous les services actuellement chargés
systemctl list-units --type=service --state=running   # uniquement ceux qui tournent
systemctl list-unit-files --type=service     # tous les services installés et leur statut
```

> **Très utile en sécurité :** lister les services actifs revient à dresser l'inventaire de ce qui **tourne** — donc de ce qui pourrait être attaqué. Un service inattendu, ou activé sans raison, mérite qu'on s'y intéresse. C'est aussi la base du durcissement (chapitre 25) : **désactiver les services inutiles réduit la surface d'attaque**.

#### Lire le journal d'un service

Quand un service refuse de démarrer, son journal explique pourquoi. `systemctl status` en donne un aperçu, mais on accède au journal complet avec `journalctl` (le chapitre 15 lui est consacré) :

```bash
systemctl status nginx       # aperçu de l'état + dernières lignes de log
journalctl -u nginx          # le journal complet du service nginx
```

Ce duo `status` + `journalctl -u` est la base du diagnostic d'un service défaillant : on regarde l'état, puis on lit ce que le service a écrit avant de tomber.

### ❌ Erreur classique

```bash
# Confondre start et enable
sudo systemctl start ssh     # démarre maintenant... mais pas après reboot
sudo systemctl enable ssh    # ✅ pour qu'il revienne au démarrage
sudo systemctl enable --now ssh  # ✅ les deux d'un coup

# Oublier sudo pour les actions
systemctl restart ssh        # ❌ "Permission denied" / demande d'authentification
sudo systemctl restart ssh   # ✅

# Se tromper de nom de service
systemctl status sshd        # selon la distro, le service s'appelle "ssh" ou "sshd"
systemctl status ssh         # ✅ sur Debian/Ubuntu c'est souvent "ssh"

# Modifier une config de service et oublier de recharger
sudoedit /etc/ssh/sshd_config   # modification faite...
# ❌ ...mais le service tourne encore avec l'ancienne config
sudo systemctl restart ssh      # ✅ recharge la nouvelle config
```

### Exercices

**Guidé :** Affiche l'état du service SSH avec `systemctl status ssh` (ou `sshd` selon ta distribution). Est-il `active (running)` ? Est-il `enabled` (démarrage auto) ? Lis attentivement les dernières lignes affichées : que t'apprennent-elles sur le service ?

**Autonome :** Liste tous les services en cours d'exécution avec `systemctl list-units --type=service --state=running`. Combien y en a-t-il ? Parcours la liste : reconnais-tu le rôle de quelques-uns (réseau, journalisation, planification…) ?

**Défi (en lab) :** Sur une machine de test, choisis un service non critique, note son état avec `systemctl status`, arrête-le avec `sudo systemctl stop`, vérifie qu'il est bien `inactive`, puis redémarre-le et confirme qu'il est de nouveau `active`. **Ne fais jamais cela sur le service SSH d'une machine à laquelle tu es connecté à distance** — tu couperais ta propre connexion (on en reparlera au chapitre 17).

### ✅ Tu sais maintenant…

- Ce qu'est un **service / démon** : un programme qui tourne en permanence en arrière-plan
- Que **systemd** orchestre les services et qu'il est le **PID 1**
- Piloter un service avec `systemctl` : `status`, `start`, `stop`, `restart`, `reload`
- La différence cruciale entre `start` (maintenant) et `enable` (au démarrage), et le raccourci `enable --now`
- Lister les services actifs (`list-units`) et pourquoi c'est un enjeu de surface d'attaque
- Diagnostiquer un service défaillant avec `status` puis `journalctl -u`

---


## Chapitre 15 — Les logs et journaux

### Le minimum à savoir

#### Pourquoi les logs sont la matière première de la sécurité

Un système Linux **raconte en permanence ce qu'il fait** : connexions, erreurs, démarrages de services, tentatives d'accès refusées… Ces enregistrements sont les **logs** (journaux). Pour un administrateur, ils répondent à « pourquoi ça ne marche pas ? ». Pour un analyste sécurité, ils répondent à « que s'est-il passé, qui, quand ? ». **Sans logs, pas d'investigation possible.** Savoir où ils sont et comment les lire est une compétence centrale, en admin comme en SOC.

#### Deux mondes : fichiers texte et journal systemd

Il existe historiquement **deux façons** de stocker les logs, et tu rencontreras les deux :

1. **Les fichiers texte dans `/var/log`** : la méthode classique. Chaque service y écrit son journal, et on les lit avec les outils du chapitre 3-4 (`cat`, `less`, `tail`, `grep`).
2. **Le journal systemd** : centralisé, structuré, interrogeable avec une seule commande, `journalctl`. C'est la méthode moderne, présente sur tous les systèmes systemd.

#### Explorer `/var/log`

```bash
ls -lt /var/log              # liste les journaux, les plus récents en premier
sudo less /var/log/syslog    # journal général du système (Debian/Ubuntu)
sudo tail -f /var/log/syslog # suivre le journal système en direct (chapitre 3)
```

Quelques fichiers courants : `syslog` (journal général), les logs d'authentification, et des dossiers propres à certains services.

#### Où sont les logs d'authentification ? (rappel essentiel)

Comme annoncé au chapitre 4, l'emplacement du journal d'authentification **dépend de la distribution** :

- **Debian / Ubuntu** : `/var/log/auth.log`
- **RHEL / CentOS / Fedora** : `/var/log/secure`
- **Tout système systemd** : `journalctl` est la méthode **la plus fiable et universelle** (voir ci-dessous)

> Ne sois pas surpris si `/var/log/auth.log` n'existe pas chez toi : c'est que ta distribution range ses logs ailleurs, ou s'appuie entièrement sur le journal systemd. Dans le doute, `journalctl` fonctionne partout où systemd est présent.

### Très utile en pratique

#### `journalctl` : le journal unifié

`journalctl` interroge le journal systemd. C'est l'outil le plus puissant de ce chapitre :

```bash
journalctl                       # tout le journal (long ; navigue comme less, quitte avec q)
journalctl -e                    # saute directement à la fin (événements récents)
journalctl -u ssh                # uniquement les messages du service ssh
journalctl -f                    # suit le journal EN DIRECT (comme tail -f)
journalctl --since "today"       # depuis aujourd'hui
journalctl --since "1 hour ago"  # depuis une heure
journalctl -p err                # uniquement les messages de niveau "erreur" et plus grave
```

Les options à retenir en priorité : **`-u`** (filtrer par service), **`-f`** (suivre en direct), **`--since`** (filtrer par date). Combinées, elles répondent à des questions précises :

```bash
journalctl -u ssh --since "today"     # toutes les activités SSH d'aujourd'hui
```

> **Très utile en sécurité (SOC) :** `journalctl -u ssh -f` permet de **suivre en direct les tentatives de connexion SSH**. Couplé au `grep` du chapitre 4, c'est la base de la détection d'une attaque par force brute : on isole les échecs d'authentification, on compte les IP sources, on identifie celles qui frappent le plus.

#### `dmesg` : les messages du noyau

À côté des logs de services, il existe un journal particulier : celui du **noyau** (le kernel), accessible avec `dmesg`. Il enregistre tout ce qui touche au **matériel et au bas niveau** :

```bash
sudo dmesg               # messages du noyau
sudo dmesg | tail        # les plus récents
sudo dmesg -T            # avec des dates lisibles (-T = timestamps humains)
```

`dmesg` est l'outil de référence pour les problèmes **matériels** :

- erreurs de **disque** (secteurs défectueux, déconnexions)
- branchement/débranchement de **périphériques USB**
- problèmes de **pilotes (drivers)**
- messages d'erreur du **noyau** lui-même

> **Réflexe :** quand un disque se comporte mal, qu'une clé USB n'est pas reconnue, ou qu'un matériel pose problème, `dmesg -T | tail` est souvent le moyen le plus rapide de voir ce que le noyau a constaté. On le réutilisera dans la démarche de diagnostic du chapitre 24.

#### La rotation des logs : `logrotate` (notion)

Les logs grandissent sans cesse. Pour qu'ils ne remplissent pas le disque, un mécanisme appelé **rotation** archive et compresse régulièrement les anciens journaux, et supprime les plus vieux. C'est géré automatiquement par **`logrotate`**. Pour débuter, retiens simplement que ça **existe** : c'est pourquoi tu verras des fichiers comme `auth.log.1`, `auth.log.2.gz` — ce sont d'anciens journaux archivés. Tu n'as rien à configurer maintenant.

### ❌ Erreur classique

```bash
# Lire un gros log avec cat
cat /var/log/syslog          # ❌ des milliers de lignes défilent
sudo less /var/log/syslog    # ✅ page par page
journalctl -u ssh -e         # ✅ ou cibler directement le service

# Oublier sudo pour les logs sensibles
cat /var/log/auth.log        # ❌ souvent "Permission denied"
sudo cat /var/log/auth.log   # ✅ les logs d'auth sont protégés

# Chercher auth.log là où il n'existe pas
cat /var/log/auth.log        # ❌ absent sur RHEL/Fedora
sudo cat /var/log/secure     # ✅ sur RHEL/CentOS/Fedora
journalctl -u sshd           # ✅ méthode universelle (systemd)

# Croire que dmesg ne sert qu'au démarrage
dmesg                        # ❌ besoin de sudo sur beaucoup de systèmes
sudo dmesg -T | tail         # ✅ utile à tout moment pour le matériel
```

### Exercices

**Guidé :** Affiche les événements système d'aujourd'hui avec `journalctl --since "today"` (navigue, puis quitte avec `q`). Ensuite, cible un service précis avec `journalctl -u ssh` (ou un autre service actif chez toi vu au chapitre 14). Que t'apprend son journal ?

**Autonome :** Utilise `sudo dmesg -T | tail -20` pour voir les 20 derniers messages du noyau. Repères-tu des mentions de matériel (disque, USB, réseau) ? Si tu peux brancher/débrancher une clé USB, relance la commande juste après : vois-tu apparaître l'événement ?

**Défi (orientation SOC) :** Reprends la logique de détection de force brute du chapitre 4, mais avec le journal moderne. Avec `journalctl`, isole les tentatives d'authentification SSH échouées (cherche « Failed » dans le journal de SSH), puis, à l'aide des pipes et de `awk`/`grep`/`sort`/`uniq -c` (chapitre 4), identifie les adresses IP qui reviennent le plus souvent. Tu obtiens la même analyse qu'avec `auth.log`, mais d'une façon qui fonctionne sur **n'importe quel** système systemd.

### ✅ Tu sais maintenant…

- Pourquoi les logs sont **la matière première** de l'administration et de la sécurité
- Les deux mondes : **fichiers texte dans `/var/log`** et **journal systemd**
- Explorer `/var/log` avec `ls -lt`, `less`, `tail -f`
- Que les logs d'auth sont dans `auth.log` (Debian/Ubuntu), `secure` (RHEL/Fedora) ou via `journalctl` (universel)
- Interroger le journal avec `journalctl` et ses options clés `-u`, `-f`, `--since`, `-p`
- Lire les messages **matériels et noyau** avec `dmesg` (et `dmesg -T`)
- Que la **rotation** (`logrotate`) archive automatiquement les vieux journaux

---


## Chapitre 16 — Tâches planifiées

### Le minimum à savoir

#### Pourquoi automatiser dans le temps

Beaucoup de tâches d'administration doivent se répéter : sauvegarder chaque nuit, nettoyer des fichiers temporaires chaque semaine, vérifier l'espace disque tous les matins. Plutôt que de les lancer à la main, on les **planifie** : le système les exécute tout seul, à l'heure dite, que tu sois là ou non. C'est l'un des grands intérêts d'un serveur, qui tourne en continu.

#### cron : le planificateur classique

L'outil historique et universel est **cron**. Chaque utilisateur dispose de sa propre table de tâches planifiées, la **crontab**, qu'on édite ainsi :

```bash
crontab -e               # éditer SA table de tâches planifiées
crontab -l               # afficher SA table actuelle
```

La première fois, `crontab -e` te demande quel éditeur utiliser (choisis `nano` si tu hésites).

#### Lire la syntaxe cron : cinq champs

Chaque ligne de la crontab décrit **quand** lancer **quoi**, avec cinq champs de temps suivis de la commande :

```
┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, dimanche = 0 ou 7)
│ │ │ │ │
* * * * *  commande-à-exécuter
```

Une `*` signifie « toutes les valeurs ». Quelques exemples parlants :

```bash
0 8 * * *    /chemin/script.sh      # tous les jours à 8h00
30 2 * * 0   /chemin/backup.sh      # chaque dimanche à 2h30
*/15 * * * * /chemin/check.sh       # toutes les 15 minutes
0 0 1 * *    /chemin/mensuel.sh     # le 1er de chaque mois à minuit
```

> **Le minimum à savoir :** les deux premiers champs (minute, heure) suffisent pour l'immense majorité des besoins : « tous les jours à telle heure ». Pour le reste, on met des `*`. En cas de doute sur une expression, des aides en ligne existent pour traduire une ligne cron en langage clair.

### Très utile en pratique

#### Les dossiers cron du système

À côté de la crontab personnelle, le système propose des dossiers où **déposer un script** pour qu'il s'exécute à une fréquence donnée, sans même écrire de ligne cron :

```bash
ls /etc/cron.daily/      # scripts exécutés chaque jour
ls /etc/cron.weekly/     # chaque semaine
ls /etc/cron.hourly/     # chaque heure
```

Déposer un script exécutable (chapitre 9 : `chmod +x`) dans `/etc/cron.daily/` suffit à le faire tourner quotidiennement. Pratique et lisible.

#### Une exécution unique : `at`

Là où cron **répète**, `at` exécute une commande **une seule fois**, à un moment futur :

```bash
echo "commande" | at 22:00       # lance la commande à 22h, une seule fois
at now + 1 hour                  # planifie pour dans une heure (mode interactif)
```

`at` n'est pas toujours installé ; au besoin, `sudo apt install at`.

#### Les timers systemd (notion)

systemd propose une alternative moderne à cron : les **timers** (`.timer`). Ils sont plus puissants (meilleure journalisation via `journalctl`, gestion des tâches manquées…) mais plus verbeux à écrire. Pour débuter, retiens qu'ils **existent** et qu'on les rencontre de plus en plus ; cron reste parfaitement valable et plus simple pour commencer.

> **Orientation cyber / sécurité :** les tâches planifiées sont à double tranchant. Côté défense, elles automatisent la surveillance et les sauvegardes. Côté attaque, elles sont un **mécanisme de persistance** classique : un intrus ajoute une tâche cron pour relancer son code régulièrement. Lors d'un audit, **inspecter les crontabs** (`crontab -l`, les fichiers dans `/etc/cron.*` et `/var/spool/cron/`) fait partie des réflexes pour repérer une persistance suspecte.

### ❌ Erreur classique

```bash
# Éditer la crontab à la main au mauvais endroit
nano /var/spool/cron/...      # ❌ ne pas éditer directement les fichiers internes
crontab -e                    # ✅ toujours passer par crontab -e

# Utiliser un chemin relatif dans une tâche cron
0 8 * * * script.sh           # ❌ cron ne sait pas où il est ; PATH minimal
0 8 * * * /home/alice/script.sh   # ✅ TOUJOURS un chemin absolu

# Oublier de rendre le script exécutable
0 8 * * * /home/alice/backup.sh   # ❌ échoue si pas de droit x
chmod +x /home/alice/backup.sh    # ✅ (chapitre 9)

# Croire que la tâche tourne alors que la machine est éteinte
# cron a besoin que la machine soit ALLUMÉE à l'heure prévue
```

> **Le piège du chemin et de l'environnement :** une tâche cron s'exécute dans un environnement **minimal** (un `PATH` réduit, pas tes alias du chapitre 8). Une commande qui marche dans ton terminal peut échouer en cron si elle dépend de ton environnement. La parade : **utiliser des chemins absolus** partout dans tes scripts planifiés.

### Exercices

**Guidé :** Ouvre ta crontab avec `crontab -e` (choisis `nano` si on te le demande). Ajoute une ligne qui écrit la date dans un fichier toutes les minutes, à des fins de test : `* * * * * date >> /home/alice/cron-test.log` (**remplace `alice` par ton vrai nom d'utilisateur** — on met un chemin absolu, conformément à la règle ci-dessus). Enregistre, attends deux-trois minutes, puis lis `cron-test.log` : vois-tu plusieurs horodatages s'accumuler ? Retire ensuite la ligne avec `crontab -e` pour ne pas polluer.

**Autonome :** Écris en langage clair ce que feraient ces lignes cron, puis vérifie ton interprétation : `0 6 * * 1`, `*/10 * * * *`, `0 0 * * 0`. À quelle fréquence chacune s'exécute-t-elle ?

**Défi (orientation sécurité) :** Fais l'inventaire des tâches planifiées de ta machine. Affiche ta crontab (`crontab -l`), liste le contenu des dossiers `/etc/cron.daily/`, `/etc/cron.hourly/`, et regarde s'il existe des crontabs système (`cat /etc/crontab`). Sur une vraie investigation, pourquoi serait-il important de connaître **toutes** les tâches planifiées d'une machine ? Que chercherait un analyste là-dedans ?

### ✅ Tu sais maintenant…

- Pourquoi on **planifie** des tâches répétitives (sauvegardes, nettoyages, vérifications)
- Éditer et lire ta planification avec `crontab -e` et `crontab -l`
- Lire la **syntaxe cron** à cinq champs (minute, heure, jour, mois, jour de semaine)
- Déposer un script dans `/etc/cron.daily/` (et `.weekly`, `.hourly`)
- Planifier une exécution **unique** avec `at`, et que les **timers systemd** existent
- Le piège des **chemins relatifs** en cron (toujours des chemins absolus)
- Que les tâches planifiées sont un **mécanisme de persistance** à auditer en sécurité

---

> **🏁 CHECKPOINT 4 — Fin de la Partie 4**
>
> Tu sais désormais **piloter une machine en fonctionnement** : observer et contrôler les processus, gérer les services qui tournent en permanence, lire ce que le système raconte dans ses journaux, et automatiser des tâches dans le temps.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - retrouver le PID d'un programme et l'arrêter proprement (puis de force si besoin) ?
> - vérifier si un service tourne, le redémarrer, et le faire démarrer automatiquement au boot ?
> - expliquer la différence entre `systemctl start` et `systemctl enable` ?
> - suivre en direct les tentatives de connexion SSH avec `journalctl` ?
> - utiliser `dmesg` pour diagnostiquer un souci matériel ?
> - planifier un script pour qu'il tourne tous les jours à heure fixe ?
>
> Si oui, tu administres une machine vivante. Il est temps de l'**ouvrir sur le monde** : place à la **Partie 5 — Linux en réseau**.

---

---
---
