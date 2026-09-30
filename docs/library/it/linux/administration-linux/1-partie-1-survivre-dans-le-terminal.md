---
title: PARTIE 1 — Survivre dans le terminal
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 1
chapters: 7
---

Avant de pouvoir administrer quoi que ce soit, il faut savoir **exister** dans le terminal : comprendre ce qu'on voit, se déplacer, lire des fichiers et y chercher de l'information — le tout **sans rien casser**. Cette première partie est volontairement « en lecture seule » : on observe, on explore, on s'oriente. On apprendra à modifier les choses dans la Partie 2, une fois qu'on sera à l'aise.

---


## Chapitre 1 — Le terminal, le shell et l'aide

### Le minimum à savoir

#### Terminal, shell : quelle différence ?

Quand tu ouvres une « fenêtre noire » pour taper des commandes, deux choses travaillent ensemble :

- Le **terminal**, c'est la fenêtre elle-même : l'endroit où s'affiche le texte et où tu tapes.
- Le **shell**, c'est le programme qui tourne *dans* cette fenêtre, qui **lit** ce que tu tapes et **exécute** tes commandes. Le shell le plus courant s'appelle **Bash**.

Une image simple : le terminal est le **téléphone** (l'appareil), le shell est la **personne** à l'autre bout qui comprend ce que tu dis et agit. Pour débuter, tu peux utiliser les deux mots de façon assez interchangeable ; retiens juste que c'est le shell qui « comprend » tes commandes.

#### Lire le prompt (l'invite de commande)

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

#### L'anatomie d'une commande

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

#### Tes premières commandes

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

### Très utile en pratique

#### Trouver de l'aide tout seul

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

#### L'historique : ne retape jamais deux fois

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

### ❌ Erreur classique

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

### Exercices

**Guidé :** Ouvre le manuel de la commande `date` avec `man date`. Cherche dans le manuel comment afficher uniquement l'année (indice : il existe un format avec `+%Y`). Quitte le manuel avec `q`, puis teste la commande que tu as trouvée.

**Autonome :** Sans utiliser Internet, trouve à quoi sert la commande `uptime` (utilise `man` ou `--help`), puis exécute-la. Que t'apprend-elle sur la machine ?

**Défi :** Utilise `apropos` pour trouver une commande qui affiche le calendrier du mois. Une fois trouvée, exécute-la, puis consulte son manuel pour afficher le calendrier de l'année entière.

### ✅ Tu sais maintenant…

- La différence entre le **terminal** (la fenêtre) et le **shell** (le programme qui exécute)
- Lire un **prompt** : qui tu es, où tu es, et si tu es root (`$` vs `#`)
- Décortiquer une commande en **commande + options + arguments**
- Afficher des informations de base : `whoami`, `hostname`, `date`, `echo`
- Te débloquer seul avec `man`, `--help`, `apropos` et `type` (et **quitter `man` avec `q`**)
- Réutiliser tes commandes avec la **flèche du haut** et `history`
- Que Linux est **sensible à la casse** : `date` ≠ `Date`

---


## Chapitre 2 — Se repérer dans l'arborescence

### Le minimum à savoir

#### Le système de fichiers est un arbre

Sous Windows, tu as plusieurs « disques » (`C:`, `D:`…). Sous Linux, c'est différent : **tout part d'un point unique**, appelé la **racine**, notée `/` (une simple barre oblique). À partir de cette racine, les dossiers se ramifient comme les branches d'un arbre.

```
/                        ← la racine : le sommet de tout
├── home/                ← les dossiers personnels des utilisateurs
│   └── alice/           ← le dossier personnel d'alice
├── etc/                 ← les fichiers de configuration du système
├── var/                 ← les données variables (logs, etc.)
│   └── log/             ← les journaux du système
├── bin/                 ← les programmes (commandes) de base
└── tmp/                 ← les fichiers temporaires
```

Tout fichier, où qu'il soit, descend de cette racine `/`. Il n'y a pas de second arbre : un seul, qui contient tout.

#### Où suis-je ? `pwd`

La toute première question quand on est perdu : **dans quel dossier suis-je ?** La commande `pwd` (*print working directory*, « affiche le dossier de travail ») répond :

```bash
pwd
# affiche par exemple : /home/alice
```

> **Réflexe à prendre dès maintenant :** quand tu ne sais plus où tu es, tape `pwd`. C'est gratuit et ça évite les catastrophes (souviens-toi de la première règle d'or : vérifier où on est avant d'agir).

#### Que contient ce dossier ? `ls`

`ls` (*list*) liste le contenu du dossier courant :

```bash
ls
```

Cette commande devient bien plus puissante avec ses options :

```bash
ls -l      # format "long" : permissions, propriétaire, taille, date
ls -a      # affiche TOUT, y compris les fichiers cachés (qui commencent par .)
ls -h      # tailles "lisibles" (Ko, Mo, Go) — à combiner avec -l
ls -t      # trie par date de modification (plus récent en premier)
```

On peut **combiner les options** :

```bash
ls -lah    # format long + fichiers cachés + tailles lisibles
```

> **Les fichiers cachés** ne sont pas « secrets » : ce sont simplement des fichiers dont le nom commence par un point (`.bashrc`, `.ssh`…). Linux les masque par défaut pour ne pas encombrer l'affichage. On en croisera beaucoup ; `ls -a` est le moyen de les voir.

#### Se déplacer : `cd`

`cd` (*change directory*) te déplace d'un dossier à un autre :

```bash
cd /var/log      # va dans le dossier /var/log
cd /             # va à la racine
cd ~             # va dans ton dossier personnel
cd               # (sans rien) va aussi dans ton dossier personnel
```

### Très utile en pratique

#### Chemins absolus et chemins relatifs

C'est **le** concept à maîtriser dans ce chapitre. Il y a deux façons d'indiquer où se trouve un fichier.

**Le chemin absolu** part toujours de la racine `/`. C'est une adresse complète, qui marche **depuis n'importe où** :

```bash
cd /home/alice/documents     # adresse complète, sans ambiguïté
```

**Le chemin relatif** part de là où tu te trouves *en ce moment*. Plus court, mais il dépend de ta position actuelle :

```bash
cd documents     # va dans le dossier "documents" situé ICI
```

Pour t'y retrouver, deux raccourcis essentiels :

- `.` → le dossier **courant** (là où tu es)
- `..` → le dossier **parent** (juste au-dessus)

```bash
cd ..            # remonte d'un niveau
cd ../..         # remonte de deux niveaux
cd ./scripts     # va dans "scripts", ici (le ./ est souvent optionnel)
```

Et deux raccourcis bien pratiques :

- `~` → ton dossier personnel (`/home/alice`)
- `cd -` → revient au **dossier précédent** (comme un bouton « retour »)

```bash
cd /var/log
cd -             # retourne là où tu étais juste avant
```

> **Image mentale :** un chemin absolu, c'est donner ton adresse postale complète (pays, ville, rue, numéro). Un chemin relatif, c'est dire « la deuxième porte à gauche » — ça ne marche que si on sait d'où tu pars.

#### Visualiser l'arbre : `tree`

La commande `tree` affiche les dossiers sous forme d'arbre, ce qui est très parlant :

```bash
tree
```

Elle n'est pas toujours installée. Si tu obtiens « command not found », installe-la (tu te souviens du réflexe de la Partie 0) :

```bash
sudo apt update
sudo apt install tree
```

Pour ne pas être noyé, limite la profondeur affichée :

```bash
tree -L 2        # n'affiche que 2 niveaux de profondeur
```

#### Les grands dossiers de Linux (le FHS)

Linux range ses fichiers selon une norme appelée **FHS** (*Filesystem Hierarchy Standard*). Tu n'as pas à tout retenir, mais reconnaître ces dossiers t'aidera énormément :

| Dossier | Ce qu'il contient |
|---------|-------------------|
| `/` | La racine : le point de départ de tout |
| `/home` | Les dossiers personnels des utilisateurs (`/home/alice`…) |
| `/root` | Le dossier personnel de l'administrateur root (attention, différent de `/`) |
| `/etc` | Les fichiers de **configuration** du système (« et cetera ») |
| `/var` | Les données qui **varient** : surtout les **logs** dans `/var/log` |
| `/bin`, `/usr/bin` | Les **programmes** (les commandes que tu tapes y vivent) |
| `/tmp` | Les fichiers **temporaires** (effacés au redémarrage) |
| `/dev` | Les **périphériques** (disques, etc.) — souviens-toi : « tout est fichier » |

> **Très utile en sécurité :** `/etc` (configurations) et `/var/log` (journaux) sont les deux dossiers que tu visiteras le plus souvent en administration et en analyse de sécurité. Note-les dès maintenant.

### ❌ Erreur classique

```bash
# Oublier où on est et lancer une commande au mauvais endroit
ls               # ❓ et si tu n'es pas dans le bon dossier ?
pwd              # ✅ vérifie TOUJOURS d'abord

# Confondre / au début (racine) et / au milieu (séparateur)
cd /home/alice   # le premier / = racine, les autres = séparateurs

# Croire que "cd .." peut dépasser la racine
cd /
cd ..            # reste à la racine : on ne peut pas remonter plus haut

# Taper le chemin avec une mauvaise casse
cd /Home/Alice   # ❌ introuvable
cd /home/alice   # ✅

# Mettre un espace dans un nom sans le protéger
cd Mes Documents     # ❌ Linux croit à deux arguments
cd "Mes Documents"   # ✅ entre guillemets
cd Mes\ Documents    # ✅ ou en échappant l'espace
```

### Exercices

**Guidé :** Depuis ton dossier personnel (`cd ~`), rends-toi dans `/var/log` en utilisant un **chemin absolu**. Vérifie avec `pwd` que tu y es bien. Liste son contenu avec `ls -l`. Puis reviens à ton point de départ avec `cd -`.

**Autonome :** Place-toi à la racine (`cd /`). Sans jamais utiliser de chemin absolu (uniquement `cd nom`, `cd ..`, etc.), navigue jusqu'à `/usr/bin`, vérifie ta position avec `pwd`, puis remonte jusqu'à la racine uniquement avec `..`.

**Défi :** Affiche l'arborescence de `/etc` sur 2 niveaux de profondeur seulement, et compare la quantité d'informations avec un `ls` simple du même dossier. Lequel est plus lisible pour avoir une vue d'ensemble ?

### ✅ Tu sais maintenant…

- Que le système Linux est un **arbre unique** partant de la racine `/`
- Répondre à « où suis-je ? » avec `pwd` (le réflexe anti-catastrophe)
- Lister un dossier avec `ls` et ses options clés : `-l`, `-a`, `-h`, `-t`
- Te déplacer avec `cd`, et utiliser `~`, `..`, `.` et `cd -`
- La différence **fondamentale** entre chemin **absolu** (part de `/`) et **relatif** (part d'où tu es)
- Reconnaître les grands dossiers du **FHS**, en particulier `/etc` et `/var/log`
- Protéger les noms contenant des **espaces** avec des guillemets

---


## Chapitre 3 — Lire le contenu des fichiers

### Le minimum à savoir

#### Pourquoi lire avant d'agir

En administration, **on regarde avant de toucher**. Avant de modifier une configuration, on la lit. Avant de supprimer un fichier, on vérifie son contenu. Avant de comprendre un problème, on lit les logs. Ce chapitre te donne les outils pour **consulter** un fichier sans aucun risque de le modifier — c'est la suite logique de notre approche « lecture seule ».

#### Texte ou binaire ? `file`

Tous les fichiers ne se lisent pas de la même façon. Un fichier **texte** (configuration, log, script) se lit directement. Un fichier **binaire** (image, programme) afficherait du charabia illisible si tu tentais de le lire comme du texte. Avant de lire un fichier inconnu, demande à Linux de quoi il s'agit :

```bash
file /etc/hostname       # → texte
file /bin/ls             # → exécutable (binaire)
```

> **Réflexe utile :** si une commande de lecture remplit ton écran de symboles incompréhensibles et fait « biper » le terminal, c'est probablement un fichier binaire. Ferme avec `q` ou `Ctrl + C`, et vérifie avec `file`.

#### Afficher un fichier entier : `cat`

`cat` affiche tout le contenu d'un fichier d'un coup :

```bash
cat /etc/hostname        # affiche le nom de la machine
```

`cat` est parfait pour les **petits** fichiers. Mais sur un gros fichier (un log de plusieurs milliers de lignes), tout défile d'un coup et tu ne vois que la fin : peu pratique. D'où les outils suivants.

#### Lire confortablement : `less`

`less` affiche un fichier **page par page**, sans tout déverser à l'écran :

```bash
less /var/log/syslog
```

Pendant que `less` est ouvert :

- **Flèches** ou **Espace** → naviguer (Espace = page suivante)
- **`/motcherché`** → rechercher un mot dans le fichier
- **`q`** → quitter (le même `q` que pour `man` — et pour cause, `man` utilise `less` !)

> **Le minimum à savoir :** pour les **petits** fichiers, `cat`. Pour les **gros** fichiers, `less`. Cette distinction simple t'évite bien des écrans qui défilent dans le vide.

#### Voir le début ou la fin : `head` et `tail`

Souvent, tu ne veux que le **début** ou la **fin** d'un fichier :

```bash
head fichier.log         # les 10 premières lignes
tail fichier.log         # les 10 dernières lignes
head -n 5 fichier.log    # les 5 premières lignes
tail -n 20 fichier.log   # les 20 dernières lignes
```

`tail` est particulièrement précieux pour les logs : les événements les plus récents sont **à la fin** du fichier. Quand un problème vient de se produire, `tail` te montre tout de suite ce qui s'est passé en dernier.

### Très utile en pratique

#### Suivre un log en direct : `tail -f`

Voici l'une des commandes les plus utiles de tout le cours. L'option `-f` (*follow*, « suivre ») garde le fichier ouvert et affiche **les nouvelles lignes en temps réel**, au fur et à mesure qu'elles s'ajoutent :

```bash
tail -f /var/log/syslog
```

L'écran ne se ferme pas : il attend et affiche chaque nouvel événement dès qu'il arrive. C'est exactement ce qu'on utilise pour **observer un système en train de fonctionner** : surveiller les connexions, voir un service démarrer, repérer une erreur dès qu'elle survient. Pour arrêter le suivi, appuie sur **`Ctrl + C`**.

> **Très utile en sécurité (SOC) :** `tail -f` sur un journal d'authentification permet de voir **en direct** les tentatives de connexion à une machine. C'est un réflexe d'analyste : ouvrir le log, le suivre, et regarder ce qui frappe à la porte.

#### Compter : `wc`

`wc` (*word count*) compte les lignes, les mots et les caractères d'un fichier :

```bash
wc fichier.txt           # lignes, mots, caractères
wc -l fichier.txt        # uniquement le nombre de LIGNES
```

L'option `-l` est la plus utilisée : « combien de lignes ? » est une question fréquente (combien d'événements dans ce log ? combien d'utilisateurs dans ce fichier ?). On l'exploitera beaucoup au chapitre 4.

#### Numéroter les lignes : `nl`

Pratique pour discuter d'un fichier ligne par ligne, ou repérer une ligne précise :

```bash
nl fichier.conf          # affiche le fichier avec un numéro devant chaque ligne
```

### ❌ Erreur classique

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

### Exercices

**Guidé :** Affiche les 3 premières lignes du fichier `/etc/passwd` avec `head`, puis ses 3 dernières lignes avec `tail`. Ensuite, compte combien de lignes contient ce fichier avec `wc -l`. Chaque ligne correspond à un compte utilisateur du système : combien y en a-t-il ?

**Autonome :** Utilise `file` sur trois éléments différents : `/etc/hostname`, `/bin/ls` et le dossier `/etc` lui-même. Note ce que `file` répond pour chacun. Lequel peux-tu lire avec `cat` sans danger ?

**Défi :** Lance `tail -f /var/log/syslog` dans ton terminal pour suivre le journal système en direct. Pendant que ça tourne, observe si de nouvelles lignes apparaissent. Au bout d'un moment, arrête proprement le suivi. *(Si `/var/log/syslog` n'existe pas sur ton système, on verra au chapitre 4 et 15 où trouver les bons journaux selon ta distribution.)*

### ✅ Tu sais maintenant…

- Que l'on **lit avant d'agir** : consulter un fichier ne le modifie jamais
- Distinguer un fichier **texte** d'un **binaire** avec `file`
- Afficher un fichier : `cat` pour les petits, `less` pour les gros (sortie : `q`)
- Voir le **début** (`head`) et la **fin** (`tail`) d'un fichier, avec `-n`
- Suivre un log **en temps réel** avec `tail -f` (et reprendre la main avec `Ctrl + C`)
- **Compter** les lignes d'un fichier avec `wc -l`
- Numéroter les lignes avec `nl`, et réparer un terminal abîmé avec `reset`

---


## Chapitre 4 — Chercher, filtrer et transformer du texte

### Le minimum à savoir

#### L'idée : filtrer un flux

Au chapitre précédent, on **affichait** des fichiers. Maintenant, on va **chercher** dedans et n'en garder que l'utile. C'est une compétence centrale : un fichier de logs peut contenir des dizaines de milliers de lignes, et tu n'en cherches souvent qu'une poignée. L'art de l'administrateur, c'est de **réduire le bruit pour ne voir que le signal**.

#### Chercher un texte : `grep`

`grep` est sans doute la commande la plus utilisée de tout l'univers Linux. Elle cherche un motif dans un fichier et n'affiche **que les lignes qui le contiennent** :

```bash
grep "erreur" fichier.log        # affiche les lignes contenant "erreur"
```

Ses options indispensables :

```bash
grep -i "erreur" fichier.log     # -i : ignore la casse (Erreur, ERREUR, erreur)
grep -n "erreur" fichier.log     # -n : affiche le numéro de chaque ligne trouvée
grep -v "erreur" fichier.log     # -v : INVERSE — lignes qui NE contiennent PAS le mot
grep -c "erreur" fichier.log     # -c : COMPTE le nombre de lignes correspondantes
grep -r "erreur" /etc/           # -r : cherche RÉCURSIVEMENT dans tout un dossier
```

> **Le minimum à savoir :** `grep "ce que je cherche" dans-quel-fichier`. Avec juste ça et les options `-i`, `-n`, `-v`, `-c`, tu réponds déjà à l'immense majorité des besoins de recherche.

#### Trouver des fichiers : `find`

`grep` cherche **dans** les fichiers. `find` cherche **les fichiers eux-mêmes**, par leur nom, leur date, leur taille… Elle parcourt l'arborescence à partir d'un dossier de départ :

```bash
find /etc -name "*.conf"         # tous les fichiers .conf sous /etc
find /home -name "rapport.txt"   # le fichier nommé rapport.txt sous /home
find . -name "*.log"             # tous les .log à partir d'ici (.)
```

La structure de `find` est : `find <où chercher> <critère>`. Le critère le plus courant est `-name` (par nom). L'astérisque `*` signifie « n'importe quelle suite de caractères » : `*.conf` veut dire « tout ce qui se termine par `.conf` ».

#### Une alternative rapide : `locate`

`locate` cherche dans une base de données préconstruite, donc c'est **très rapide**, mais la base n'est pas toujours à jour ni installée par défaut :

```bash
locate hostname              # trouve très vite les chemins contenant "hostname"
```

> `find` est toujours fiable (il regarde le système réel, en direct) mais plus lent. `locate` est instantané mais peut rater un fichier récent. Pour débuter, **privilégie `find`** : il ne ment jamais.

### Très utile en pratique

#### Le tuyau (pipe) `|` : enchaîner les commandes

Voici l'idée la plus puissante de la Partie 1. Le caractère `|` (appelé *pipe*, ou « tuyau ») prend la **sortie** d'une commande et l'envoie comme **entrée** à la commande suivante. On enchaîne ainsi de petits outils pour répondre à une question précise :

```bash
cat fichier.log | grep "erreur"      # affiche le fichier, PUIS n'en garde que les erreurs
```

C'est exactement la philosophie « petits outils combinés » vue en Partie 0, rendue concrète. On peut chaîner plusieurs pipes :

```bash
cat fichier.log | grep "erreur" | wc -l    # COMBIEN de lignes contiennent "erreur" ?
```

Ici : on lit le fichier → on garde les erreurs → on les compte. Trois outils simples, une réponse précise.

> **Note importante :** ici, on utilise les pipes de façon **pratique**, comme un tuyau qui relie des commandes — c'est suffisant pour ce chapitre. Le fonctionnement complet des flux (entrée, sortie, sortie d'erreur, redirections vers des fichiers) sera expliqué proprement au **chapitre 7**. Pour l'instant, retiens juste : `|` envoie le résultat de gauche vers la commande de droite.

#### Trier et dédoublonner : `sort` et `uniq`

```bash
sort fichier.txt             # trie les lignes par ordre alphabétique
sort -n fichier.txt          # -n : trie numériquement (1, 2, 10) et non (1, 10, 2)
uniq fichier.txt             # supprime les doublons CONSÉCUTIFS
```

> **Le duo classique :** `uniq` ne supprime que les doublons **qui se suivent**. Il faut donc presque toujours trier **avant** : `sort | uniq`. Encore mieux, `sort | uniq -c` trie, dédoublonne **et compte** combien de fois chaque ligne apparaît — extrêmement utile pour répondre à « quelle valeur revient le plus souvent ? ».

#### Extraire une colonne : `cut`

Beaucoup de fichiers système sont organisés en colonnes séparées par un caractère. `cut` extrait la colonne qui t'intéresse :

```bash
cut -d: -f1 /etc/passwd      # -d: séparateur ":"   -f1 : 1re colonne
```

Le fichier `/etc/passwd` sépare ses champs par des `:`. La première colonne est le **nom d'utilisateur**. Cette commande liste donc tous les comptes du système. (`-d` = *delimiter*, le séparateur ; `-f` = *field*, le numéro de colonne.)

#### Transformer du texte : `tr`, `sed`, `awk` (initiation)

Ces trois outils **transforment** le texte. On les introduit ici pour des cas **simples** : ils te seront indispensables pour traiter des logs. *(Leurs usages avancés dépassent le cadre d'un cours débutant et sont laissés en annexe.)*

**`tr`** — remplace ou supprime des caractères :

```bash
echo "BONJOUR" | tr 'A-Z' 'a-z'      # → bonjour (met tout en minuscules)
```

**`sed`** — remplace un motif par un autre (substitution) :

```bash
sed 's/ancien/nouveau/g' fichier.txt    # remplace "ancien" par "nouveau" partout
```

La syntaxe `s/.../.../g` se lit : *substitute* (remplacer) `s/ce-qu-on-cherche/ce-qu-on-met/g`, le `g` final signifiant « partout sur la ligne » (*global*).

**`awk`** — extrait une colonne, façon `cut` mais plus souple :

```bash
awk '{print $1}' fichier.txt             # affiche la 1re colonne (séparée par espaces)
awk -F: '{print $1}' /etc/passwd         # -F: change le séparateur en ":"
```

`$1` désigne la première colonne, `$2` la deuxième, etc. C'est parfait pour isoler une information précise dans une ligne de log.

> **Pour débuter, retiens juste ces quatre formes :** `tr 'A-Z' 'a-z'` (changer la casse), `sed 's/x/y/g'` (remplacer), `awk '{print $1}'` (extraire une colonne par espaces), `awk -F: '{print $1}'` (extraire une colonne par un autre séparateur). C'est largement suffisant pour traiter des logs au niveau débutant.

### Où sont les logs d'authentification ?

Plusieurs exercices de ce chapitre utilisent un journal d'authentification (les tentatives de connexion). **Son emplacement dépend de ta distribution :**

- Sur **Debian / Ubuntu** : `/var/log/auth.log`
- Sur **RHEL / CentOS / Fedora** : `/var/log/secure`
- Sur **tout système moderne avec systemd** : la méthode la plus fiable est `journalctl` (on l'étudiera en détail au **chapitre 15**)

> Si un fichier d'exemple n'existe pas chez toi, ce n'est pas une erreur de ta part : c'est juste que ta distribution range ses logs ailleurs. Adapte le chemin, ou note que `journalctl` sera la solution universelle vue plus tard.

### ❌ Erreur classique

```bash
# Oublier les guillemets quand le motif contient un espace
grep Failed password auth.log    # ❌ cherche "Failed" dans les fichiers "password" et "auth.log"
grep "Failed password" auth.log  # ✅ le motif entier entre guillemets

# Utiliser uniq sans trier avant
uniq fichier.txt                 # ❌ rate les doublons non consécutifs
sort fichier.txt | uniq          # ✅ trier d'abord

# Trier des nombres sans -n
sort fichier.txt                 # ❌ ordre alphabétique : 1, 10, 2, 20, 3
sort -n fichier.txt              # ✅ ordre numérique : 1, 2, 3, 10, 20

# Se tromper de sens avec grep -v
grep -v "ok" log                 # garde les lignes SANS "ok" (inversion) — voulu ?

# Confondre find et grep
find /etc -name "erreur"         # cherche un FICHIER nommé "erreur"
grep -r "erreur" /etc            # cherche le TEXTE "erreur" DANS les fichiers
```

> **La confusion `find` vs `grep`** est l'une des plus fréquentes. Mémo : `find` cherche **des fichiers** (par leur nom), `grep` cherche **du texte** (dans les fichiers).

### Exercices

**Guidé :** Dans `/etc/passwd`, affiche uniquement la liste des noms d'utilisateurs (1re colonne), triée par ordre alphabétique. Indice : combine `cut` (avec le séparateur `:`) et `sort` à l'aide d'un pipe.

**Autonome :** Toujours dans `/etc/passwd`, compte combien de comptes existent sur le système de deux façons différentes : avec `wc -l`, puis avec `grep -c ""`. Obtiens-tu le même nombre ? *(C'est normal, les deux comptent les lignes.)*

**Défi (orientation sécurité) :** Sur ton journal d'authentification (`/var/log/auth.log`, ou `/var/log/secure`, selon ta distribution), construis une chaîne de commandes qui :
1. extrait les lignes contenant « Failed password » (avec `grep`),
2. isole l'adresse IP source de chaque tentative (avec `awk`, en repérant la bonne colonne),
3. trie ces IP, les dédoublonne et **compte** combien de fois chacune apparaît (avec `sort` et `uniq -c`).

Tu obtiendras la liste des adresses ayant tenté le plus de connexions échouées — exactement le réflexe d'un analyste SOC face à une attaque par force brute. *(Si le fichier n'existe pas, garde la logique de la chaîne en tête : on la réutilisera avec `journalctl` au chapitre 15.)*

### 🧩 Mini-projet (Partie 1) — Ta première enquête

Mets bout à bout tout ce que tu viens d'apprendre dans une petite investigation. Sur ta machine :

1. **Repère-toi** : place-toi dans `/var/log` et liste son contenu trié par date de modification (`ls -lt`). Quels sont les journaux modifiés le plus récemment ?
2. **Lis** : choisis un fichier de log lisible, affiche ses 20 dernières lignes (`tail`), puis suis-le un instant en direct (`tail -f`, puis `Ctrl + C`).
3. **Cherche** : dans ce log, compte combien de lignes contiennent le mot « error » ou « failed » (insensible à la casse, avec `grep -ic`).
4. **Transforme** : si le log contient des lignes structurées, extrais une colonne intéressante (heure, service…) avec `awk` ou `cut`, et identifie la valeur la plus fréquente avec `sort | uniq -c | sort -n`.
5. **Conclus** : en deux phrases, qu'as-tu appris sur l'activité récente de ta machine ?

Ce mini-projet n'utilise **que** des commandes de lecture et de filtrage : tu mènes une vraie enquête sans rien modifier. C'est l'essence du travail défensif.

### ✅ Tu sais maintenant…

- **Filtrer un flux** pour ne garder que l'information utile
- Chercher du texte avec `grep` et ses options clés : `-i`, `-n`, `-v`, `-c`, `-r`
- Trouver des fichiers avec `find` (par nom), et la différence avec `grep`
- Enchaîner des commandes avec le **pipe** `|` (vu ici en pratique ; détaillé au ch. 7)
- Trier et dédoublonner avec `sort` et le duo `sort | uniq -c`
- Extraire une colonne avec `cut`, et transformer du texte avec `tr`, `sed`, `awk` (cas simples)
- Que l'emplacement des **logs d'auth** dépend de la distribution (`auth.log` / `secure` / `journalctl`)
- Mener une **enquête de lecture seule** sur les journaux de ta machine

---

> **🏁 CHECKPOINT 1 — Fin de la Partie 1**
>
> Tu sais désormais **survivre et te repérer** dans un système Linux sans aucun risque : te déplacer, lire, chercher et filtrer de l'information. C'est la fondation de tout le reste.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - expliquer la différence entre un chemin absolu et un chemin relatif ?
> - retrouver un fichier dont tu connais le nom, n'importe où sous `/etc` ?
> - suivre un log en temps réel, puis reprendre la main ?
> - compter combien de fois un mot apparaît dans un fichier ?
> - extraire la première colonne de `/etc/passwd` et la trier ?
>
> Si tu réponds oui à tout, tu es prêt pour la **Partie 2 — Manipuler le système de fichiers**, où l'on passera enfin de la lecture à l'action : créer, copier, déplacer, éditer — avec les bons réflexes de prudence.

---

---
---
