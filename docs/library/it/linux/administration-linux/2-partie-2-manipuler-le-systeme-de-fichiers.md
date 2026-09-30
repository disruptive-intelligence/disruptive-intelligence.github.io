---
title: PARTIE 2 — Manipuler le système de fichiers
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 2
chapters: 7
---

En Partie 1, on observait sans rien toucher. Maintenant, on passe à l'**action** : créer, copier, déplacer, supprimer, éditer des fichiers, et comprendre comment Linux relie les fichiers entre eux et fait circuler l'information. On garde en permanence les réflexes de prudence vus en Partie 0 : sous Linux, **il n'y a pas de corbeille**, et une commande mal placée agit immédiatement.

---


## Chapitre 5 — Créer, copier, déplacer, supprimer

### Le minimum à savoir

#### Créer un fichier vide : `touch`

`touch` crée un fichier vide s'il n'existe pas (et met à jour sa date s'il existe déjà) :

```bash
touch rapport.txt        # crée un fichier vide nommé rapport.txt
touch fichier1 fichier2  # on peut en créer plusieurs d'un coup
```

C'est la façon la plus rapide de « poser » un fichier avant de le remplir.

#### Créer un dossier : `mkdir`

`mkdir` (*make directory*) crée un dossier :

```bash
mkdir projet             # crée un dossier "projet"
```

Et si tu veux créer toute une arborescence d'un coup, l'option `-p` crée les dossiers parents manquants :

```bash
mkdir -p projet/logs/2025    # crée projet, puis logs, puis 2025
```

Sans `-p`, la commande échouerait si `projet` ou `logs` n'existaient pas encore. **Le `-p` est le réflexe pour créer un chemin complet.**

#### Copier : `cp`

`cp` (*copy*) copie un fichier vers une destination. L'original reste en place :

```bash
cp rapport.txt sauvegarde.txt      # copie le fichier sous un nouveau nom
cp rapport.txt /tmp/               # copie le fichier dans le dossier /tmp
```

Pour copier un **dossier** (avec tout son contenu), il faut l'option `-r` (*recursive*) :

```bash
cp -r projet/ projet-copie/        # copie le dossier et tout ce qu'il contient
```

> **Réflexe à retenir :** sans `-r`, on ne peut pas copier un dossier. C'est aussi le `-r` qu'on retrouvera pour la suppression et les permissions : **`-r` = « et tout ce qu'il y a dedans »**.

#### Déplacer et renommer : `mv`

`mv` (*move*) sert à **deux** choses qui sont en réalité la même : déplacer, et renommer.

```bash
mv rapport.txt /tmp/               # DÉPLACE le fichier dans /tmp
mv rapport.txt bilan.txt           # RENOMME le fichier (le "déplace" vers un nouveau nom)
```

Renommer, pour Linux, c'est juste déplacer un fichier vers un nouveau nom au même endroit. Pas besoin de commande séparée.

#### Supprimer : `rm` (la commande à respecter)

`rm` (*remove*) supprime un fichier. **Définitivement. Sans corbeille. Sans confirmation.**

```bash
rm rapport.txt           # supprime le fichier (aucun retour possible)
```

Pour supprimer un **dossier** et son contenu, il faut `-r` :

```bash
rm -r projet/            # supprime le dossier et TOUT ce qu'il contient
```

Pour supprimer un dossier **vide** uniquement (plus sûr), il existe `rmdir` :

```bash
rmdir dossier-vide/      # échoue si le dossier n'est PAS vide (c'est une sécurité)
```

### Très utile en pratique

#### Le filet de sécurité : `rm -i`

L'option `-i` (*interactive*) demande **confirmation** avant chaque suppression :

```bash
rm -i rapport.txt
# rm: supprimer fichier 'rapport.txt' ? (o/n)
```

C'est un excellent réflexe quand tu débutes, ou avant une suppression importante. Tu reprends la main sur une opération irréversible.

#### Appliquer les règles d'or

Souviens-toi de la Partie 0. Avant toute suppression, le bon réflexe est :

```bash
pwd                      # 1. où suis-je vraiment ?
ls                       # 2. qu'est-ce qu'il y a ici, exactement ?
rm -i fichier-a-virer    # 3. je supprime, avec confirmation
```

Ces trois secondes de vérification t'éviteront un jour une vraie catastrophe.

#### ⚠️ `rm -rf` : la commande qui ne pardonne pas

Tu croiseras partout la combinaison `rm -rf` :

- `-r` → récursif (dossiers et contenu)
- `-f` → *force* : ne demande rien, ignore les erreurs, supprime tout

```bash
rm -rf vieux-projet/     # supprime tout, sans aucune question
```

Cette commande est puissante et **utilisée tous les jours** par les administrateurs. Mais une faute de frappe peut être dévastatrice :

```bash
rm -rf / chemin          # ❌❌❌ CATASTROPHE : l'espace après / détruit la racine
rm -rf /chemin           # ce qui était voulu (un seul argument)
```

> **La règle absolue avec `rm -rf` :** relis la ligne **avant** d'appuyer sur Entrée. Cherche les espaces parasites. Vérifie que le chemin commence bien là où tu crois. En cas de doute, remplace temporairement `rm` par `ls` pour voir *ce qui serait supprimé* — si `ls` affiche les bons fichiers, alors `rm` visera les bons fichiers.

### ❌ Erreur classique

```bash
# Copier un dossier sans -r
cp projet/ copie/        # ❌ "omitting directory" — refusé
cp -r projet/ copie/     # ✅

# Écraser un fichier sans s'en rendre compte
cp a.txt b.txt           # ❌ si b.txt existait, son contenu est PERDU
cp -i a.txt b.txt        # ✅ -i demande confirmation avant d'écraser

# Croire que rm met à la corbeille
rm important.txt         # ❌ DÉFINITIF, pas de récupération simple

# Oublier que mv écrase la destination silencieusement
mv a.txt b.txt           # si b.txt existait, il est remplacé sans prévenir
mv -i a.txt b.txt        # ✅ -i pour être prévenu

# Mauvais espace dans rm -rf
rm -rf ./ *              # ❌ le "./ *" sépare en deux : danger
rm -rf ./vieux-dossier   # ✅ un seul chemin, sans espace parasite
```

### Exercices

**Guidé :** Crée d'un seul `mkdir -p` l'arborescence `atelier/scripts/sauvegardes`. Place-toi dedans, crée trois fichiers vides avec `touch` (`a.sh`, `b.sh`, `c.sh`), puis vérifie le tout avec `ls -R atelier` (le `-R` liste récursivement).

**Autonome :** Dans le dossier `atelier`, copie `scripts/a.sh` vers `scripts/a.sh.bak` (une sauvegarde). Renomme ensuite `b.sh` en `principal.sh`. Vérifie le résultat avec `ls`. Combien de fichiers y a-t-il maintenant dans `scripts` ?

**Défi :** Crée un dossier `lab-test` avec quelques fichiers à l'intérieur. Avant de le supprimer, entraîne-toi au réflexe de sécurité : fais `ls lab-test/` pour voir ce qu'il contient, puis supprime-le entièrement avec `rm -r`. Recommence en utilisant `rm -ri` pour voir la différence (confirmation à chaque élément). Lequel te semble plus prudent quand l'enjeu est important ?

### ✅ Tu sais maintenant…

- Créer des fichiers (`touch`) et des dossiers (`mkdir`, et `mkdir -p` pour une arborescence)
- Copier avec `cp` (et `-r` pour les dossiers, `-i` pour éviter d'écraser)
- Déplacer **et** renommer avec `mv` (c'est la même opération)
- Supprimer avec `rm` — **définitivement** — et la sécurité `rmdir` pour les dossiers vides
- Te protéger avec `rm -i`, et appliquer le réflexe `pwd` → `ls` → suppression
- Pourquoi `rm -rf` est puissant **et** dangereux, et comment le manipuler sans accident

---


## Chapitre 6 — Éditer des fichiers dans le terminal

### Le minimum à savoir

#### Pourquoi éditer sans interface graphique ?

Quand tu administres un serveur, tu n'as **pas de souris ni de fenêtres** : tu es connecté en ligne de commande (on verra le SSH en Partie 5). Pour modifier un fichier de configuration, il te faut donc un éditeur qui fonctionne **dans le terminal**. C'est une compétence incontournable : la quasi-totalité du réglage d'un système Linux passe par l'édition de fichiers texte dans `/etc`.

#### `nano` : l'éditeur pour débuter

`nano` est simple, lisible, et c'est celui qu'on recommande pour commencer :

```bash
nano notes.txt           # ouvre (ou crée) le fichier dans l'éditeur
```

Une fois dans `nano`, tu tapes ton texte normalement. En bas de l'écran, une **barre d'aide** rappelle les raccourcis. Le symbole `^` y signifie la touche **`Ctrl`**. Les deux à connaître absolument :

- **`Ctrl + O`** → *enregistrer* (puis Entrée pour confirmer le nom)
- **`Ctrl + X`** → *quitter*

> **Le minimum vital dans nano :** écrire, puis `Ctrl + O` pour sauvegarder, puis `Ctrl + X` pour sortir. Avec juste ça, tu peux déjà modifier n'importe quelle configuration.

#### `vim` : survivre, au minimum

`vim` (et son ancêtre `vi`) est extrêmement puissant, mais **déroutant** au premier contact. Tu finiras peut-être par l'adorer, mais pour l'instant l'objectif est simple : **savoir en sortir sans paniquer**, car tu tomberas dessus par surprise un jour (certains systèmes l'ouvrent par défaut).

La clé : `vim` a des **modes**. Au démarrage, tu es en mode « commande » (taper du texte ne marche pas comme prévu). Le strict minimum :

- Appuie sur **`i`** → passe en mode *insertion* (là, tu peux taper du texte)
- Appuie sur **`Échap`** → reviens en mode commande
- Tape **`:wq`** puis Entrée → *write & quit* (enregistrer et quitter)
- Tape **`:q!`** puis Entrée → quitter **sans** enregistrer (la sortie de secours)

> **Si tu es coincé dans vim** et que tu veux juste partir sans rien casser : appuie sur `Échap`, puis tape `:q!` et Entrée. Retiens ce `:q!` — c'est ta porte de sortie garantie.

#### Écrire sans éditeur : `echo` et les redirections

Pour des modifications très rapides, on peut écrire dans un fichier directement depuis la ligne de commande :

```bash
echo "première ligne" > notes.txt     # > ÉCRASE le fichier avec ce texte
echo "ligne ajoutée" >> notes.txt     # >> AJOUTE à la fin sans rien effacer
```

> **Distinction capitale** (qu'on approfondira au chapitre 7) : `>` **écrase** tout le contenu existant, `>>` **ajoute** à la fin. Confondre les deux sur un fichier important est une erreur classique aux conséquences sérieuses.

### Très utile en pratique

#### Le réflexe sauvegarde-avant-modification

C'est la **troisième règle d'or** de la Partie 0, et c'est ici qu'elle prend tout son sens. **Avant de modifier un fichier de configuration, on en fait toujours une copie de sauvegarde.** Si la modification casse quelque chose, on restaure la copie et tout repart.

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. copie de sécurité (.bak)
sudo nano /etc/ssh/sshd_config                           # 2. on modifie
```

L'extension `.bak` est une convention (pour « backup ») : elle n'a rien de magique, mais elle signale clairement « ceci est une sauvegarde ». Si la modification tourne mal :

```bash
sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config    # on restaure, et on est sauvé
```

#### `sudoedit` : la bonne façon d'éditer un fichier système

Pour modifier un fichier qui appartient au système (dans `/etc`, par exemple), il faut des droits d'administrateur. On pourrait écrire `sudo nano fichier`, mais il existe **mieux** : `sudoedit`.

```bash
sudoedit /etc/ssh/sshd_config       # (équivalent : sudo -e ...)
```

`sudoedit` t'ouvre le fichier dans une **copie temporaire** avec **ton** éditeur habituel et **tes** réglages, puis réécrit le fichier original à ta place une fois que tu as fini. C'est plus propre et plus sûr que `sudo nano` : ton éditeur ne tourne pas avec les pleins pouvoirs, ce qui limite les dégâts en cas de mauvaise manipulation.

> **Bonne pratique professionnelle :** pour éditer un fichier système, préfère `sudoedit fichier` plutôt que `sudo nano fichier`. *(Pour choisir quel éditeur `sudoedit` lance, on règle la variable d'environnement `EDITOR` — un sujet du chapitre 8.)*

#### Comparer deux versions : `diff`

Après une modification, comment savoir **exactement** ce qui a changé ? `diff` compare deux fichiers et n'affiche que les **différences** :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

Le workflow complet, propre et professionnel, devient donc :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérification du changement
```

> **Très utile en sécurité :** garder un `.bak` et un `diff` permet de **prouver** ce qui a été modifié dans une configuration, et de revenir à l'état initial en cas de problème. C'est une trace précieuse lors d'un incident.

### ❌ Erreur classique

```bash
# Confondre > et >> et écraser un fichier
echo "nouvelle conf" > /etc/important.conf    # ❌ tout l'ancien contenu est PERDU
echo "ligne en plus" >> /etc/important.conf   # ✅ ajoute sans détruire

# Modifier une config système SANS sauvegarde
sudo nano /etc/ssh/sshd_config                # ❌ et si ça casse ?
sudo cp .../sshd_config .../sshd_config.bak   # ✅ toujours un .bak d'abord

# Rester bloqué dans vim et fermer brutalement le terminal
# ✅ Échap puis :q! suffit pour sortir proprement

# Croire que sudo nano = sudoedit
sudo nano /etc/fichier        # fonctionne, mais l'éditeur tourne en root
sudoedit /etc/fichier         # ✅ plus sûr : édition dans une copie temporaire

# Éditer un fichier système sans les droits
nano /etc/hosts               # ❌ "Permission denied" ou impossible d'enregistrer
sudoedit /etc/hosts           # ✅
```

### Exercices

**Guidé :** Avec `nano`, crée un fichier `~/notes-cours.txt`, écris-y trois lignes décrivant ce que tu as appris jusqu'ici, enregistre avec `Ctrl + O` et quitte avec `Ctrl + X`. Vérifie le contenu avec `cat ~/notes-cours.txt`.

**Autonome :** Crée un fichier `config-test.txt` avec quelques lignes. Fais-en une copie `.bak`. Modifie ensuite l'original (change une ligne, ajoutes-en une) avec l'éditeur de ton choix. Enfin, lance `diff config-test.txt.bak config-test.txt` et lis attentivement ce que `diff` te montre : reconnais-tu tes modifications ?

**Défi :** Ouvre volontairement un fichier avec `vim` (`vim test-vim.txt`). Passe en mode insertion avec `i`, écris une phrase, reviens en mode commande avec `Échap`, puis quitte **sans enregistrer** avec `:q!`. Recommence, mais cette fois enregistre avec `:wq`. Vérifie avec `cat` quel essai a bien été sauvegardé.

### ✅ Tu sais maintenant…

- Pourquoi l'édition en terminal est indispensable en administration
- Éditer simplement avec `nano` (sauver `Ctrl + O`, quitter `Ctrl + X`)
- **Survivre dans `vim`** : `i` pour écrire, `Échap`, puis `:wq` (enregistrer) ou `:q!` (sortie de secours)
- Écrire vite avec `echo >` (écrase) et `echo >>` (ajoute)
- Le **réflexe `.bak`** avant toute modification de configuration
- Éditer proprement un fichier système avec `sudoedit` (mieux que `sudo nano`)
- Vérifier précisément un changement avec `diff`

---


## Chapitre 7 — Liens, redirections et tuyaux

### Le minimum à savoir

#### Les trois flux : entrée, sortie, erreur

Au chapitre 4, on a utilisé le pipe `|` « pour de vrai » sans tout expliquer. Le moment est venu de comprendre **comment l'information circule** sous Linux. Chaque commande dispose de trois canaux :

- **L'entrée standard (stdin)** : ce que la commande reçoit (par défaut, ton clavier).
- **La sortie standard (stdout)** : ce que la commande produit normalement (par défaut, l'écran).
- **La sortie d'erreur (stderr)** : là où la commande envoie ses messages d'erreur (par défaut, l'écran aussi).

```
                  ┌─────────────┐
   stdin   ─────► │   COMMANDE  │ ─────►  stdout (résultat normal)
  (clavier)       │             │ ─────►  stderr (messages d'erreur)
                  └─────────────┘
```

Le point essentiel : **sortie normale et sortie d'erreur sont deux canaux séparés**, même s'ils s'affichent tous les deux à l'écran par défaut. Pouvoir les rediriger indépendamment est ce qui rend Linux si puissant pour l'automatisation.

#### Rediriger la sortie vers un fichier : `>` et `>>`

On l'a effleuré au chapitre 6, voici l'explication propre :

```bash
ls > liste.txt           # > : envoie la sortie dans le fichier (ÉCRASE l'ancien contenu)
ls >> liste.txt          # >> : AJOUTE la sortie à la fin du fichier
```

`>` redirige **stdout** vers un fichier au lieu de l'écran. C'est ainsi qu'on **enregistre** le résultat d'une commande.

> **Le piège classique, redit une fois de plus parce qu'il fait des dégâts :** `>` **écrase** sans prévenir. `commande > fichier-important` détruit le contenu du fichier. En cas de doute, utilise `>>` (ajout) ou redirige d'abord vers un fichier de test.

#### Rediriger les erreurs : `2>` et `&>`

Les erreurs voyagent sur le canal `stderr`, identifié par le numéro **`2`** :

```bash
commande 2> erreurs.txt      # envoie UNIQUEMENT les erreurs dans erreurs.txt
commande > sortie.txt 2>&1   # envoie sortie ET erreurs dans le même fichier
commande &> tout.txt         # raccourci moderne : sortie + erreurs dans tout.txt
```

Un usage très courant : **se débarrasser des erreurs** qu'on ne veut pas voir, en les envoyant vers `/dev/null` (une sorte de « trou noir » du système qui jette tout ce qu'on lui donne) :

```bash
find / -name "*.conf" 2>/dev/null    # ne montre que les résultats, pas les "Permission denied"
```

> Tu reconnais ce `2>/dev/null` ? C'est exactement ce qu'on utilisera en Partie 3 pour les recherches de fichiers SUID : on cache les nombreux messages d'erreur pour ne garder que les vrais résultats.

### Très utile en pratique

#### Le pipe `|` : maintenant tu comprends pourquoi ça marche

Le pipe relie la **sortie standard** d'une commande à l'**entrée standard** de la suivante. Ce que tu utilisais au chapitre 4 comme un simple « tuyau » est en fait une redirection de stdout vers stdin :

```bash
cat auth.log | grep "Failed" | wc -l
#   stdout ──► stdin   stdout ──► stdin
```

Chaque `|` branche la sortie de gauche sur l'entrée de droite. C'est le mécanisme qui incarne la philosophie « petits outils combinés ».

#### Voir ET enregistrer en même temps : `tee`

Parfois tu veux à la fois **voir** un résultat à l'écran **et** le **garder** dans un fichier. La commande `tee` fait les deux (comme un « T » de plomberie qui sépare un flux en deux) :

```bash
ls -l /etc | tee inventaire.txt          # affiche le résultat ET l'écrit dans inventaire.txt
ls -l /etc | tee -a inventaire.txt       # -a : ajoute au fichier au lieu de l'écraser
```

> **Très utile en pratique :** lors d'une analyse, `commande | tee rapport.txt` te permet de suivre le résultat en direct tout en conservant une trace écrite pour plus tard. Indispensable pour documenter une investigation.

#### Appliquer une commande à chaque résultat : `xargs`

`xargs` prend une liste arrivant par un pipe et la transforme en **arguments** pour une autre commande. C'est le pont entre « une liste de noms » et « une action sur chacun » :

```bash
find . -name "*.tmp" | xargs rm          # supprime tous les .tmp trouvés
```

Ici : `find` produit une liste de fichiers → `xargs` la passe à `rm` qui les supprime. C'est puissant… donc à manier avec la prudence habituelle (teste d'abord en remplaçant `rm` par `echo` pour voir ce qui serait fait).

#### Les liens symboliques : `ln -s`

Un **lien symbolique** est un « raccourci » : un petit fichier qui pointe vers un autre fichier ou dossier, parfois situé ailleurs. On le crée avec `ln -s` (*link, symbolic*) :

```bash
ln -s /var/log/syslog ~/mon-log         # crée un raccourci "mon-log" vers le vrai fichier
```

Désormais, `~/mon-log` mène au vrai `/var/log/syslog`. Si tu supprimes le lien, le fichier d'origine reste intact (tu n'effaces que le raccourci). Tu reconnaîtras un lien dans un `ls -l` à la flèche `->` qui indique sa cible.

> Il existe aussi des liens « durs » (sans `-s`), plus techniques. Pour débuter, retiens surtout le **lien symbolique** : c'est de loin le plus courant et le plus utile.

### ❌ Erreur classique

```bash
# Écraser un fichier important avec >
cat resultats.txt > resultats.txt    # ❌ peut vider le fichier ! ne redirige pas vers la source
sort resultats.txt > tries.txt       # ✅ vers un AUTRE fichier

# Oublier que les erreurs ne passent pas par le pipe normalement
commande_qui_echoue | grep "ok"      # les erreurs s'affichent quand même (elles sont sur stderr)
commande_qui_echoue 2>&1 | grep "ok" # ✅ pour filtrer aussi les erreurs

# Confondre tee et >
ls | > fichier.txt               # ❌ syntaxe cassée
ls | tee fichier.txt             # ✅ voir + enregistrer
ls > fichier.txt                 # ✅ enregistrer seulement

# Utiliser xargs avec rm sans vérifier
find . -name "*" | xargs rm      # ❌ DANGER : teste d'abord avec echo
find . -name "*.tmp" | xargs echo  # ✅ visualise ce qui serait supprimé

# Supprimer la cible en croyant supprimer le lien
rm ~/mon-log/                    # attention à ce qu'on supprime exactement
```

### Exercices

**Guidé :** Liste le contenu de `/etc` et enregistre-le dans un fichier `etc-liste.txt` avec `>`. Vérifie avec `cat etc-liste.txt`. Relance la même commande mais avec `>>` et observe que le fichier double de taille (l'ajout). Puis recommence avec `>` : le fichier est réécrit de zéro.

**Autonome :** Lance `find /etc -name "*.conf"` deux fois : une fois sans rien, une fois avec `2>/dev/null`. Compare la quantité de messages d'erreur. Ensuite, utilise `tee` pour à la fois afficher la liste des `.conf` et l'enregistrer dans `confs.txt`.

**Défi :** Crée un lien symbolique vers ton journal système quelque part dans ton dossier personnel (`ln -s`). Vérifie avec `ls -l` que la flèche `->` pointe vers la bonne cible. Lis le log à travers ton lien (`tail mon-lien`). Puis supprime **le lien** et confirme avec `ls` que le fichier d'origine, lui, existe toujours.

### ✅ Tu sais maintenant…

- Les **trois flux** : entrée (stdin), sortie (stdout), erreur (stderr) — et que sortie et erreur sont **séparées**
- Rediriger la sortie avec `>` (écrase) et `>>` (ajoute)
- Rediriger les erreurs avec `2>`, les fusionner avec `2>&1` ou `&>`, et les jeter avec `2>/dev/null`
- **Pourquoi** le pipe `|` fonctionne : il relie stdout à stdin
- Voir **et** enregistrer en même temps avec `tee`
- Appliquer une action à chaque résultat avec `xargs` (en testant d'abord avec `echo`)
- Créer un raccourci avec un **lien symbolique** (`ln -s`) et le reconnaître au `->`

---


## Chapitre 8 — Variables d'environnement et configuration du shell

### Le minimum à savoir

#### Pourquoi certaines commandes marchent « partout »

Tu as remarqué que tu peux taper `ls` depuis **n'importe quel** dossier et que ça fonctionne ? Pourtant, `ls` est un programme rangé quelque part (dans `/bin` ou `/usr/bin`). Comment le shell le retrouve-t-il sans que tu donnes son chemin complet ? La réponse tient en un mot : **les variables d'environnement**. Comprendre ce mécanisme, c'est lever l'un des derniers mystères du terminal.

#### Qu'est-ce qu'une variable d'environnement ?

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

#### Le `PATH` : la clé du mystère

`PATH` est **la** variable à comprendre. Elle contient une liste de dossiers, séparés par des `:`, dans lesquels le shell va **chercher** les programmes que tu tapes :

```bash
echo $PATH
# → /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin
```

Quand tu tapes `ls`, le shell parcourt ces dossiers **dans l'ordre** jusqu'à trouver un programme nommé `ls`. C'est pour ça que `ls` marche partout : son dossier (`/bin`) est dans le `PATH`. Et c'est aussi pourquoi une commande que tu viens d'écrire toi-même ne marche **pas** directement : son dossier n'est pas dans le `PATH`.

#### Où est ce programme ? `which` et `command -v`

Pour savoir **quel** fichier sera exécuté quand tu tapes une commande :

```bash
which ls             # → /usr/bin/ls (le chemin du programme trouvé via le PATH)
command -v ls        # → même résultat, forme plus moderne et portable
```

`command -v` fonctionne aussi avec les commandes internes au shell et les alias, là où `which` peut être limité. **Pour débuter, `which` suffit** ; garde `command -v` en tête comme la version « propre ».

### Très utile en pratique

#### Créer une variable : `export`

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

#### Ajouter un dossier au `PATH`

Imaginons que tu ranges tes propres scripts dans un dossier `~/bin`. Pour pouvoir les lancer **par leur nom** depuis partout, il faut ajouter ce dossier au `PATH` :

```bash
mkdir -p ~/bin                       # crée le dossier pour tes scripts
export PATH="$HOME/bin:$PATH"        # ajoute ~/bin EN TÊTE du PATH
```

Décortiquons `"$HOME/bin:$PATH"` : on met ton nouveau dossier, un `:`, puis **l'ancien `PATH` en entier**. C'est crucial : on **ajoute** à la liste existante, on ne la remplace pas. Oublier `:$PATH` à la fin ferait disparaître l'accès à toutes les commandes habituelles le temps de la session.

#### Les alias : des raccourcis personnels

Un **alias** est un surnom que tu donnes à une commande, souvent pour ajouter des options par défaut ou raccourcir une commande longue :

```bash
alias ll='ls -lah'           # désormais "ll" = "ls -lah"
alias ..='cd ..'             # remonter d'un dossier en tapant juste ..
alias                        # (seul) affiche tous tes alias actuels
```

> **Très utile en pratique :** les administrateurs créent souvent un alias `alias rm='rm -i'` pour que `rm` demande **toujours** confirmation. Un petit filet de sécurité permanent, dans l'esprit des règles d'or de la Partie 0.

#### Rendre tout cela permanent : `.bashrc` et `source`

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

#### Le mystère du `./script.sh` enfin résolu

Tu te demandais peut-être pourquoi, pour lancer un script à toi, on écrit `./script.sh` et pas juste `script.sh` ? Maintenant tu as la réponse : le dossier courant (`.`) **n'est pas dans le `PATH`** (pour des raisons de sécurité). Le shell ne cherche donc pas tes programmes ici. En écrivant `./script.sh`, tu donnes explicitement le chemin (« le script `script.sh`, **ici** ») au lieu de compter sur le `PATH`. Et si tu ranges tes scripts dans `~/bin` ajouté au `PATH`, tu pourras les lancer par leur nom, de partout — comme une vraie commande.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Affiche le contenu de tes variables `HOME`, `USER` et `PATH` avec `echo`. Puis utilise `which` pour trouver où se trouvent les programmes `ls`, `cat` et `grep`. Sont-ils tous dans des dossiers présents dans ton `PATH` ?

**Autonome :** Crée un dossier `~/bin`. Ajoute-le à ton `PATH` avec `export` (en n'oubliant pas `:$PATH`). Vérifie avec `echo $PATH` qu'il apparaît bien. Crée ensuite un alias temporaire `alias jrnl='tail -f /var/log/syslog'` et teste-le. *(Cet alias disparaîtra à la fermeture du terminal — c'est voulu.)*

**Défi :** Rends tes réglages permanents proprement. Fais d'abord une copie `.bak` de ton `~/.bashrc`. Ajoute-y l'export de `~/bin` dans le `PATH` et un alias `ll='ls -lah'`. Applique avec `source ~/.bashrc`, puis teste `ll`. Ouvre enfin un **nouveau** terminal et vérifie que `ll` fonctionne toujours, prouvant que le réglage est bien devenu permanent.

### 🧩 Mini-projet (Partie 2) — Atelier de configuration

Mets en œuvre toute la Partie 2 dans un atelier réaliste, **sur des fichiers de test uniquement** (pas de vrai fichier système) :

1. **Construis** une arborescence de travail avec `mkdir -p` : `atelier/{scripts,configs,sauvegardes}`.
2. **Crée** dans `configs/` un fichier `app.conf` avec quelques lignes de réglages (via `nano` ou `echo >>`).
3. **Sauvegarde** : avant toute modification, copie `app.conf` en `app.conf.bak` (le réflexe).
4. **Modifie** `app.conf` (change une valeur), puis prouve le changement avec `diff app.conf.bak app.conf`.
5. **Journalise** : avec un pipe et `tee`, enregistre la liste de tes fichiers dans `atelier/inventaire.txt` tout en l'affichant.
6. **Personnalise** : ajoute dans ton `.bashrc` (après un `.bak` !) un alias `atelier='cd ~/atelier && ls -lah'`, applique avec `source`, et teste-le.
7. **Range** : déplace tes scripts dans le dossier prévu avec `mv`, et fais le ménage des fichiers de test inutiles avec `rm -i`.

À la fin, tu auras mobilisé création, copie, déplacement, suppression prudente, édition sécurisée, redirections et configuration du shell — tout le cœur de la Partie 2.

### ✅ Tu sais maintenant…

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
