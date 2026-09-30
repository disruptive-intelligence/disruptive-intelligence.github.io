---
title: PARTIE 6 — Entretenir le système
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 6
chapters: 7
---

Un système qu'on administre se maintient dans le temps : installer et mettre à jour des logiciels, surveiller l'espace disque, archiver des données, et sauvegarder pour ne rien perdre. Ce sont les gestes du quotidien d'un administrateur. Tu vas réutiliser beaucoup de ce que tu sais déjà (permissions, redirections, planification) au service de la maintenance.

---


## Chapitre 20 — Gérer les paquets et logiciels

### Le minimum à savoir

#### Qu'est-ce qu'un gestionnaire de paquets ?

Sous Linux, on n'installe presque jamais un logiciel en téléchargeant un fichier sur un site web. À la place, un **gestionnaire de paquets** récupère les logiciels depuis des **dépôts** (des serveurs officiels et vérifiés), gère automatiquement leurs **dépendances** (les autres logiciels nécessaires), et permet de tout mettre à jour d'un coup. C'est plus simple, plus sûr (les paquets sont signés et vérifiés), et plus facile à maintenir.

Chaque famille de distributions a son gestionnaire :

- **Debian / Ubuntu** : `apt` (c'est celui de ce cours)
- **RHEL / CentOS / Fedora** : `dnf` (ou son ancêtre `yum`)
- **Arch** : `pacman`

#### Les commandes apt essentielles

Sur Debian/Ubuntu, tout passe par `apt`, avec une poignée de sous-commandes très régulières (toutes celles qui modifient le système demandent `sudo`) :

```bash
sudo apt update              # met à jour la LISTE des paquets disponibles
sudo apt upgrade             # installe les mises à jour des paquets déjà présents
sudo apt install nom         # installe un paquet
sudo apt remove nom          # désinstalle un paquet (garde sa configuration)
sudo apt purge nom           # désinstalle ET supprime sa configuration
apt search motclé            # cherche un paquet par mot-clé (sans sudo)
apt show nom                 # affiche les détails d'un paquet
```

> **La distinction `update` / `upgrade` est essentielle et souvent confondue :** `update` rafraîchit seulement le **catalogue** (la liste de ce qui existe et des versions), il n'installe rien. `upgrade` applique réellement les mises à jour. **On fait toujours `update` avant `upgrade`** (ou avant un `install`), pour travailler sur un catalogue à jour. C'est exactement le réflexe `sudo apt update` qu'on a introduit dès la Partie 0.

#### Mettre à jour son système

L'enchaînement de maintenance le plus courant, à faire régulièrement :

```bash
sudo apt update && sudo apt upgrade      # rafraîchit le catalogue PUIS met à jour
```

Le `&&` enchaîne les deux commandes : la seconde ne s'exécute que si la première a réussi.

> **À connaître — `apt full-upgrade` :** il existe aussi `sudo apt full-upgrade`, qui peut **installer ou supprimer** des paquets pour résoudre des mises à jour plus complexes (changements de dépendances). Pour débuter, retiens surtout `apt upgrade`. Utilise `full-upgrade` avec prudence, en **lisant bien ce qu'APT propose de supprimer** avant de confirmer.

> **Très utile en sécurité :** maintenir un système à jour fait partie des mesures défensives les plus **rentables** : beaucoup d'attaques exploitent des vulnérabilités **déjà connues et corrigées**. Un système non mis à jour laisse ces portes ouvertes. C'est le premier point de toute checklist de durcissement (chapitre 25).

### Très utile en pratique

#### Sous le capot : `dpkg`

`apt` s'appuie sur un outil de plus bas niveau, `dpkg`, qui gère les paquets individuellement. Utile surtout pour interroger ce qui est installé :

```bash
dpkg -l                      # liste TOUS les paquets installés
dpkg -l | grep nginx         # cherche si nginx est installé (pipe du chapitre 7)
dpkg -L nom                  # liste les fichiers installés par un paquet
```

#### Installer les outils de ce cours

Le moment est venu d'installer, **maintenant que tu en comprends le sens**, les outils mentionnés au fil des chapitres et regroupés dès la Partie 0. On les sépare en deux lots, ce qui clarifie leur rôle :

```bash
sudo apt update
# Lot 1 — outils d'apprentissage et d'administration
sudo apt install tree htop curl wget dnsutils traceroute net-tools rsync
# Lot 2 — outils de durcissement (on les configurera au chapitre 25)
sudo apt install ufw fail2ban
```

> **Lab vs production :** sur une machine de **lab**, tu peux installer ce lot d'un coup pour suivre le cours confortablement. Sur un **serveur réel**, installe uniquement les paquets nécessaires au besoin immédiat — chaque logiciel ajouté agrandit la surface d'attaque et la charge de maintenance. Les outils de sécurité `ufw` et `fail2ban` (lot 2) ne servent vraiment qu'une fois **configurés** : on s'en occupera au chapitre 25.

Petit rappel de ce que chacun apporte, et où on l'a croisé :

| Paquet | Outil(s) | Vu au chapitre |
|--------|----------|----------------|
| `tree` | affichage en arbre | 2 |
| `htop` | moniteur de processus | 13 |
| `curl`, `wget` | requêtes et téléchargements web | 17 |
| `dnsutils` | `dig`, `nslookup` | 17 |
| `traceroute` | chemin réseau | 17 |
| `net-tools` | `netstat`, `ifconfig` (anciens) | 17 |
| `rsync` | synchronisation/transfert | 19, 23 |
| `ufw` | pare-feu simple | 25 |
| `fail2ban` | protection contre la force brute | 25 |

> **Principe à garder :** on n'installe pas tout « au cas où » sur un vrai serveur. Sur une machine d'apprentissage, ces deux lots sont pratiques ; sur un serveur de production, on installe **uniquement le nécessaire**.

#### Faire le ménage

Avec le temps, des paquets deviennent inutiles. Pour récupérer de l'espace proprement :

```bash
sudo apt autoremove          # supprime les dépendances devenues inutiles
sudo apt clean               # vide le cache des paquets téléchargés
```

### ❌ Erreur classique

```bash
# Faire upgrade sans update d'abord
sudo apt upgrade             # ❌ travaille sur un catalogue peut-être périmé
sudo apt update && sudo apt upgrade   # ✅ catalogue à jour, puis mise à jour

# Oublier sudo
apt install htop             # ❌ "Permission denied" / "are you root?"
sudo apt install htop        # ✅

# Confondre remove et purge
sudo apt remove apache2      # garde les fichiers de config
sudo apt purge apache2       # ✅ si tu veux TOUT supprimer, config comprise

# Installer des logiciels hors des dépôts sans réfléchir
# ❌ télécharger un .deb au hasard sur Internet contourne les vérifications
# ✅ privilégier les dépôts officiels ; vérifier la source si exception

# Ignorer les mises à jour de sécurité pendant des mois
# ❌ c'est la cause n°1 d'intrusions évitables
```

### Exercices

**Guidé :** Rafraîchis le catalogue avec `sudo apt update` et lis le résumé (combien de paquets peuvent être mis à jour ?). Cherche ensuite un outil avec `apt search`, par exemple `apt search htop`, puis affiche ses détails avec `apt show htop`. Enfin, installe-le avec `sudo apt install htop` et lance-le.

**Autonome :** Liste les paquets installés avec `dpkg -l` et compte-les (`dpkg -l | wc -l`, en gardant en tête que les premières lignes sont un en-tête). Cherche si quelques outils précis sont présents : `dpkg -l | grep -E "ssh|curl|rsync"`. Lesquels sont installés ?

**Défi (orientation sécurité) :** Vérifie l'état des mises à jour de sécurité de ta machine. Lance `sudo apt update`, puis `apt list --upgradable` pour voir ce qui peut être mis à jour. Combien de paquets sont concernés ? Sur un vrai système, pourquoi appliquer ces mises à jour est-il considéré comme la mesure de sécurité prioritaire ? Applique-les avec `sudo apt upgrade`.

### ✅ Tu sais maintenant…

- Ce qu'est un **gestionnaire de paquets**, des **dépôts** et des **dépendances**
- Les familles : `apt` (Debian/Ubuntu), `dnf`/`yum` (RHEL/Fedora), `pacman` (Arch)
- Les commandes `apt` clés : `update`, `upgrade`, `install`, `remove`, `purge`, `search`, `show`
- La distinction **`update`** (catalogue) vs **`upgrade`** (vraies mises à jour), et l'enchaînement `update && upgrade`
- Que **maintenir à jour** est la mesure de sécurité la plus efficace
- Interroger les paquets installés avec `dpkg -l`
- Faire le ménage avec `autoremove` et `clean`

---


## Chapitre 21 — Stockage et espace disque

### Le minimum à savoir

#### Comprendre les niveaux : disque, partition, système de fichiers, point de montage

Le stockage sous Linux se comprend par couches, qu'il faut distinguer pour ne pas se perdre :

- Un **disque** physique (ou virtuel) : le matériel, par exemple `/dev/sda`.
- Une **partition** : une division du disque, par exemple `/dev/sda1`. Un disque peut être découpé en plusieurs partitions.
- Un **système de fichiers** : la façon dont les données sont organisées **dans** une partition (ext4, xfs…). C'est ce qui transforme un espace brut en quelque chose qui contient des fichiers.
- Un **point de montage** : l'**endroit dans l'arborescence** (chapitre 2) où ce système de fichiers devient accessible. C'est le concept clé : sous Linux, un disque n'apparaît pas comme « lecteur D: », il est **« monté »** à un endroit de l'arbre unique, par exemple `/` ou `/home` ou `/mnt/usb`.

> **L'idée à retenir :** sous Linux, on ne « voit » pas les disques séparément ; on les **rattache** (monte) à des dossiers de l'arborescence unique. Ouvrir un dossier peut donc, en réalité, accéder à un autre disque — de façon totalement transparente.

#### Voir l'espace disque : `df`

`df` (*disk free*) montre l'espace **utilisé et disponible** sur chaque système de fichiers monté :

```bash
df -h            # -h = tailles lisibles (Go, Mo) ; vue d'ensemble de l'espace
```

Chaque ligne montre un système de fichiers, sa taille, l'espace utilisé, l'espace libre, et son **point de montage**. C'est le premier réflexe quand on se demande « est-ce que mon disque est plein ? ».

#### Voir ce qui prend de la place : `du`

Là où `df` regarde les disques globalement, `du` (*disk usage*) mesure la taille **des fichiers et dossiers** :

```bash
du -sh dossier/          # -s = total (summary), -h = lisible : taille totale du dossier
du -h --max-depth=1 /var # taille de chaque sous-dossier de /var, un niveau
```

> **La confusion classique `df` vs `du` :** `df` répond « combien d'espace reste-t-il **sur le disque** ? » (vue globale, par système de fichiers). `du` répond « combien pèse **ce dossier** ? » (vue détaillée, par fichier). Quand un disque se remplit, on utilise `df` pour le **constater**, puis `du` pour **trouver le coupable**.

### Très utile en pratique

#### Trouver ce qui remplit le disque

Le combo gagnant quand `df -h` annonce un disque presque plein : descendre avec `du` pour localiser les gros dossiers, en triant (chapitre 4) :

```bash
sudo du -h --max-depth=1 / | sort -rh | head    # les plus gros dossiers à la racine
```

Ici : `du` mesure chaque dossier de premier niveau, `sort -rh` trie par taille décroissante (`-r` inverse, `-h` comprend les tailles lisibles), `head` garde le haut du classement. On répète ensuite dans le dossier coupable pour affiner. C'est l'enquête type « où est passé mon espace ? ».

#### Voir les disques et partitions : `lsblk`

`lsblk` (*list block devices*) affiche les disques et leurs partitions sous forme d'arbre — la vue « matériel » du stockage :

```bash
lsblk            # disques, partitions, tailles et points de montage
```

C'est l'outil idéal pour **observer** la structure de stockage sans rien risquer : quels disques existent, comment ils sont découpés, et où chaque partition est montée.

#### Voir précisément ce qui est monté : `findmnt`

`findmnt` affiche la liste des systèmes de fichiers montés, joliment présentée en arbre, avec leur source et leurs options :

```bash
findmnt          # arbre clair de tous les points de montage
findmnt /home    # info sur un point de montage précis
```

> **Très utile en pratique :** `lsblk` (les disques) et `findmnt` (les montages) sont tes deux outils d'**observation** du stockage. Ils ne modifient rien, et te donnent une vue complète et sûre de la situation. Prends le réflexe de les consulter **avant** toute action.

#### `/etc/fstab` : les montages permanents

Comment le système sait-il quels disques monter, et où, à chaque démarrage ? Grâce au fichier **`/etc/fstab`** (*file systems table*). Chaque ligne y décrit un système de fichiers et son point de montage permanent.

```bash
cat /etc/fstab           # lire la table des montages permanents (lecture sans risque)
```

> **À ton niveau : lire, comprendre — pas modifier.** Apprends d'abord à **lire** `/etc/fstab` pour comprendre comment ta machine est organisée. Le **modifier** est une opération sensible : une erreur peut empêcher la machine de démarrer correctement. Si tu dois un jour y toucher, applique le réflexe du chapitre 6 (copie `.bak` d'abord) et procède avec une grande prudence.

#### Monter et démonter : `mount` / `umount` (avec prudence)

Pour rattacher temporairement un système de fichiers (une clé USB, un partage réseau) à un dossier, on utilise `mount` ; pour le détacher, `umount`. Ce sont des opérations **privilégiées** et **sensibles**.

```bash
sudo mount /dev/sdb1 /mnt/usb        # monte une partition sur /mnt/usb (montage temporaire)
sudo umount /mnt/usb                 # démonte proprement
```

> **⚠️ Prudence (rappel de la Partie 0) :** `mount` et `umount` figurent parmi les commandes sensibles. Démonter un disque en cours d'utilisation, ou se tromper de périphérique, peut perturber l'accès aux données ou provoquer des pertes. **Pour un débutant, on commence par observer** avec `lsblk`, `df` et `findmnt` ; on ne monte/démonte qu'en sachant exactement quel périphérique on manipule, idéalement en lab. Distinction utile : un montage par `mount` est **temporaire** (perdu au redémarrage) ; un montage **permanent** passe par `/etc/fstab`.

#### La mémoire vive : `free`

Au passage, pour la mémoire (RAM), qui n'est pas du stockage disque mais qu'on surveille de la même façon :

```bash
free -h          # mémoire totale, utilisée, libre, et swap (en tailles lisibles)
```

### ❌ Erreur classique

```bash
# Confondre df et du
df -h dossier/           # ❌ df raisonne par système de fichiers, pas par dossier
du -sh dossier/          # ✅ du pour la taille d'un dossier
df -h                    # ✅ df pour l'espace global

# Oublier -h et lire des nombres bruts illisibles
df                       # tailles en blocs, peu parlant
df -h                    # ✅ Go/Mo lisibles

# Modifier /etc/fstab sans sauvegarde ni précaution
sudoedit /etc/fstab      # ⚠️ une erreur ici peut empêcher le boot
sudo cp /etc/fstab /etc/fstab.bak   # ✅ toujours un .bak d'abord (chapitre 6)

# Démonter un disque occupé
sudo umount /mnt/usb     # ❌ "target is busy" si un fichier y est ouvert
# ✅ ferme ce qui l'utilise, puis démonte ; observe d'abord avec findmnt

# Se tromper de périphérique avec mount
sudo mount /dev/sda /mnt # ❌ vérifie TOUJOURS avec lsblk avant de monter
```

### Exercices

**Guidé :** Affiche l'espace disque global avec `df -h`. Repère le système de fichiers monté sur `/` : quelle proportion est utilisée ? Ensuite, mesure la taille de ton dossier personnel avec `du -sh ~`. Compare : ton dossier représente-t-il une grande part de l'espace utilisé ?

**Autonome :** Observe la structure de stockage de ta machine avec `lsblk`, puis avec `findmnt`. Combien de disques/partitions vois-tu ? Où est monté chacun ? Enfin, lis `/etc/fstab` avec `cat` et essaie de faire le lien entre ce fichier et ce que `findmnt` t'a montré.

**Défi :** Mène l'enquête « où est passé mon espace ? ». Pars de `df -h` pour repérer le système de fichiers le plus rempli. Puis, avec `sudo du -h --max-depth=1 / | sort -rh | head`, identifie les plus gros dossiers à la racine. Descends d'un niveau dans le coupable et répète, jusqu'à localiser précisément ce qui occupe le plus d'espace. Quel dossier as-tu trouvé ?

### ✅ Tu sais maintenant…

- Distinguer **disque**, **partition**, **système de fichiers** et **point de montage**
- Que Linux **monte** les disques dans son arborescence unique (pas de « lecteur D: »)
- Voir l'espace global avec `df -h` et la taille des dossiers avec `du -sh`
- La distinction **`df`** (espace du disque) vs **`du`** (taille d'un dossier), et l'enquête `du | sort -rh | head`
- **Observer** le stockage sans risque avec `lsblk` (disques) et `findmnt` (montages)
- Lire `/etc/fstab` pour comprendre les montages permanents (sans le modifier à la légère)
- Que `mount`/`umount` sont **sensibles** : on observe d'abord, on agit en connaissant le périphérique
- Surveiller la mémoire avec `free -h`

---


## Chapitre 22 — Archives et compression

### Le minimum à savoir

#### Archiver ≠ compresser

Deux opérations distinctes, qu'on combine souvent :

- **Archiver**, c'est **regrouper** plusieurs fichiers et dossiers en un seul fichier (sans forcément réduire la taille). L'outil historique est `tar`, qui produit un fichier `.tar` (une « archive »).
- **Compresser**, c'est **réduire la taille** des données. Les outils courants sont `gzip` (`.gz`), et d'autres comme `xz` ou `bzip2`.

Le plus souvent, on fait les deux d'un coup : on regroupe avec `tar`, et on compresse au passage, ce qui donne un `.tar.gz` (parfois écrit `.tgz`). C'est le format d'archive le plus répandu sous Linux.

#### Créer et extraire une archive : `tar`

`tar` a une réputation de syntaxe intimidante, mais deux combinaisons couvrent presque tout :

```bash
tar -czvf archive.tar.gz dossier/    # CRÉER une archive compressée d'un dossier
tar -xzvf archive.tar.gz             # EXTRAIRE une archive compressée
```

Décortiquons les options (les mêmes lettres dans les deux cas, sauf la première) :

- `c` = *create* (créer) / `x` = *extract* (extraire)
- `z` = compresser/décompresser avec gzip
- `v` = *verbose* (affiche les fichiers traités)
- `f` = *file* (le nom du fichier d'archive suit) — **toujours en dernier**, juste avant le nom

> **Moyen mnémotechnique :** pour **créer**, pense « **c**reate **z**ip **v**erbose **f**ile » → `czvf`. Pour **extraire**, remplace le `c` par `x` → `xzvf`. Avec ces deux-là, tu gères l'immense majorité des archives. Le `f` est toujours collé au nom de l'archive.

Pour juste **regarder** le contenu d'une archive sans l'extraire :

```bash
tar -tzvf archive.tar.gz             # t = list (lister le contenu)
```

### Très utile en pratique

#### Compresser un fichier seul : `gzip`

Pour compresser un fichier unique (sans archive) :

```bash
gzip gros-fichier.log        # crée gros-fichier.log.gz et SUPPRIME l'original
gunzip gros-fichier.log.gz   # décompresse (récupère l'original)
zcat fichier.log.gz          # lire un fichier compressé SANS le décompresser
```

> **Très utile en pratique :** tu te souviens des logs archivés du chapitre 15 (`auth.log.2.gz`) ? C'est exactement du gzip. `zcat`, `zless` et `zgrep` permettent de **lire et chercher dans les logs compressés sans les décompresser** — précieux pour fouiller d'anciens journaux lors d'une investigation.

#### Le format zip : `zip` / `unzip`

Pour échanger avec des systèmes Windows, le format `.zip` est plus universel :

```bash
zip -r archive.zip dossier/  # créer un zip d'un dossier (-r pour le contenu)
unzip archive.zip            # extraire un zip
```

`zip`/`unzip` ne sont pas toujours installés (`sudo apt install zip unzip`).

### ❌ Erreur classique

```bash
# Mettre le nom de l'archive au mauvais endroit (f doit précéder le nom)
tar -cfzv dossier/ archive.tar.gz    # ❌ ordre des options cassé
tar -czvf archive.tar.gz dossier/    # ✅ f juste avant le nom de l'archive

# Extraire sans savoir où ça va se déverser
tar -xzvf archive.tar.gz             # extrait dans le dossier COURANT
pwd                                  # ✅ vérifie où tu es avant d'extraire

# Oublier que gzip supprime l'original
gzip rapport.log                     # rapport.log disparaît, devient rapport.log.gz
gzip -k rapport.log                  # ✅ -k garde l'original (keep)

# Décompresser un gros log juste pour le lire
gunzip auth.log.1.gz                 # ❌ inutile et encombrant
zcat auth.log.1.gz | grep "Failed"   # ✅ lire/chercher sans décompresser
```

### Exercices

**Guidé :** Crée un dossier avec quelques fichiers. Archive-le et compresse-le en une commande : `tar -czvf sauvegarde.tar.gz mondossier/`. Observe la liste défiler (grâce au `v`). Vérifie le contenu sans extraire avec `tar -tzvf sauvegarde.tar.gz`, puis extrais-le dans un autre dossier de test.

**Autonome :** Prends un fichier texte assez gros (par exemple une copie d'un log). Compresse-le avec `gzip -k` (en gardant l'original), puis compare les tailles avec `ls -lh` : quel gain de place obtiens-tu ? Lis ensuite le fichier compressé avec `zcat` sans le décompresser.

**Défi (orientation admin/SOC) :** Prépare une « collecte » de logs comme pour une investigation. Archive et compresse en une fois le contenu de `/var/log` (ce qui est lisible) dans un fichier horodaté : `sudo tar -czvf logs-$(date +%F).tar.gz /var/log/ 2>/dev/null`. Le `$(date +%F)` insère la date du jour dans le nom (tu reverras cette technique en Bash, chapitre 26). Vérifie l'archive créée et sa taille. Pourquoi horodater le nom d'une archive de logs est-il une bonne pratique ?

### ✅ Tu sais maintenant…

- La différence entre **archiver** (regrouper, `tar`) et **compresser** (réduire, `gzip`)
- Créer une archive compressée avec `tar -czvf` et l'extraire avec `tar -xzvf` (le `f` avant le nom)
- Lister le contenu d'une archive sans extraire (`tar -tzvf`)
- Compresser un fichier seul (`gzip`, `-k` pour garder l'original)
- **Lire/chercher dans un fichier compressé** sans le décompresser (`zcat`, `zgrep`)
- Utiliser le format `.zip` (`zip -r`, `unzip`) pour l'échange avec Windows

---


## Chapitre 23 — Sauvegardes

### Le minimum à savoir

#### Pourquoi sauvegarder : la question n'est pas « si » mais « quand »

Un disque tombe en panne, un fichier est supprimé par erreur (`rm`, chapitre 5 !), une attaque chiffre les données… Tôt ou tard, **on perd des données**. La seule protection est la **sauvegarde** : une copie, ailleurs, qu'on peut restaurer. Ce n'est pas optionnel en administration ; c'est une responsabilité fondamentale.

#### La règle 3-2-1

La référence en matière de sauvegarde tient en trois chiffres :

- **3** copies des données (l'originale + 2 sauvegardes)
- **2** supports différents (par exemple disque interne + disque externe)
- **1** copie hors site (ailleurs physiquement, pour survivre à un incendie, un vol, une attaque)

Pour débuter, retiens l'esprit : **une sauvegarde sur le même disque que l'original ne protège de presque rien.** Une vraie sauvegarde est ailleurs.

#### Sauvegarde complète vs incrémentale

- Une sauvegarde **complète** copie tout, à chaque fois : simple, mais lourde et lente.
- Une sauvegarde **incrémentale** ne copie que ce qui a **changé** depuis la dernière fois : rapide et économe. C'est exactement ce que fait `rsync` (chapitre 19), ce qui en fait un excellent outil de sauvegarde.

### Très utile en pratique

#### Sauvegarder avec `rsync`

`rsync` (vu au chapitre 19) est idéal : il ne copie que les changements, préserve les attributs, et fonctionne aussi bien en local que vers une machine distante.

```bash
# Sauvegarde locale vers un disque externe monté
rsync -av --delete ~/documents/ /mnt/backup/documents/

# Sauvegarde vers un serveur distant (à travers SSH, chapitre 18)
rsync -av ~/documents/ alice@serveur:/sauvegardes/documents/
```

L'option `--delete` rend la sauvegarde **identique** à la source (elle supprime côté sauvegarde ce qui a disparu côté source). Puissante, donc à manier avec soin :

> **⚠️ Prudence avec `--delete` :** combinée à une erreur de chemin, elle peut supprimer des fichiers de ta sauvegarde. **Teste toujours avec `--dry-run` d'abord** (chapitre 19) : `rsync -av --delete --dry-run ...`. C'est le même réflexe de prudence qui traverse tout le cours.

#### Sauvegarder avec `tar` (archive datée)

Pour une sauvegarde ponctuelle sous forme d'archive unique (facile à stocker et à dater) :

```bash
tar -czvf backup-$(date +%F).tar.gz ~/documents/    # archive horodatée du jour
```

Le `$(date +%F)` insère la date (format `2025-01-10`) dans le nom : tu obtiens un historique clair de tes sauvegardes.

#### Planifier les sauvegardes

Une sauvegarde n'a de valeur que si elle est **régulière**. On combine donc ce chapitre avec la planification du chapitre 16. Un petit script de sauvegarde, déposé en cron, et la machine se sauvegarde toute seule chaque nuit :

```bash
# Exemple de ligne crontab : sauvegarde chaque jour à 2h30
30 2 * * * /home/alice/scripts/sauvegarde.sh
```

> Souviens-toi du piège du chapitre 16 : dans un script planifié, utilise des **chemins absolus**, car cron s'exécute dans un environnement minimal.

#### Le point le plus oublié : tester la restauration

**Une sauvegarde qu'on n'a jamais testée n'est pas une sauvegarde.** Beaucoup découvrent, le jour fatidique, que leurs sauvegardes étaient vides, corrompues ou incomplètes. Le réflexe professionnel : **restaurer régulièrement** un fichier au hasard pour vérifier que ça fonctionne.

```bash
# Vérifier qu'on peut bien extraire une archive de sauvegarde
tar -tzvf backup-2025-01-10.tar.gz | head     # le contenu est-il bien là ?
# Puis tester une vraie extraction dans un dossier temporaire
mkdir /tmp/test-restore && tar -xzvf backup-2025-01-10.tar.gz -C /tmp/test-restore
```

> **Très utile en sécurité :** face à une attaque par rançongiciel (qui chiffre les données), des sauvegardes **hors ligne, testées et régulières** sont souvent la seule façon de tout récupérer sans céder. C'est une pièce maîtresse de la résilience défensive.

### ❌ Erreur classique

```bash
# Sauvegarder sur le même disque que l'original
rsync -av ~/data/ /autre-dossier-du-meme-disque/   # ❌ le disque meurt = tout est perdu
rsync -av ~/data/ /mnt/disque-externe/             # ✅ support différent

# Utiliser --delete sans simuler
rsync -av --delete ~/data/ /mnt/backup/            # ❌ une erreur de chemin = perte
rsync -av --delete --dry-run ~/data/ /mnt/backup/  # ✅ simuler d'abord

# Ne jamais tester la restauration
# ❌ découvrir le jour J que la sauvegarde était inutilisable
tar -tzvf backup.tar.gz                            # ✅ vérifier régulièrement

# Croire qu'une copie unique suffit
# ❌ une seule copie n'est pas une stratégie : pense 3-2-1
```

### Exercices

**Guidé :** Crée un dossier `~/precieux/` avec quelques fichiers. Réalise une première sauvegarde complète vers un autre dossier avec `rsync -av ~/precieux/ ~/sauvegarde-precieux/`. Modifie ensuite un fichier de `~/precieux/`, relance le même `rsync`, et observe : seul le fichier modifié est transféré (c'est l'aspect incrémental).

**Autonome :** Crée une archive de sauvegarde horodatée de ton dossier `~/precieux/` avec `tar -czvf backup-$(date +%F).tar.gz ~/precieux/`. Vérifie son contenu sans l'extraire. Puis **teste la restauration** : extrais l'archive dans `/tmp/restore-test/` et confirme que tes fichiers sont bien là, intacts.

**Défi :** Conçois (sur le papier ou en vrai script) une stratégie de sauvegarde complète appliquant la règle 3-2-1 pour un dossier important. Décris : quoi sauvegarder, vers où (deux supports, une copie distante), à quelle fréquence (et comment la planifier avec cron), et comment tu vérifierais régulièrement que les sauvegardes sont restaurables. Tu mobilises ici rsync, tar, SSH et cron — toute la Partie 6.

### ✅ Tu sais maintenant…

- Pourquoi sauvegarder est une **responsabilité fondamentale**, pas une option
- La règle **3-2-1** (3 copies, 2 supports, 1 hors site)
- La différence entre sauvegarde **complète** et **incrémentale**
- Sauvegarder avec `rsync` (incrémental, local ou distant) et la prudence du `--delete` + `--dry-run`
- Créer des archives **horodatées** avec `tar` et `$(date +%F)`
- **Planifier** les sauvegardes avec cron (chemins absolus)
- Que **tester la restauration** est indispensable, et le rôle des sauvegardes contre les rançongiciels

---

> **🏁 CHECKPOINT 6 — Fin de la Partie 6**
>
> Tu sais maintenant **entretenir un système sur la durée** : installer et tenir les logiciels à jour, surveiller l'espace disque et la mémoire, archiver des données, et mettre en place des sauvegardes fiables et testées. Ce sont les gestes qui maintiennent une machine en bonne santé année après année.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - mettre à jour ton système proprement, et expliquer `update` vs `upgrade` ?
> - constater un disque plein avec `df`, puis trouver le coupable avec `du` ?
> - observer la structure de stockage avec `lsblk` et `findmnt` sans rien risquer ?
> - créer et extraire une archive `.tar.gz` ?
> - mettre en place une sauvegarde `rsync` incrémentale et tester sa restauration ?
>
> Si oui, tu sais faire vivre un système dans le temps. Il ne reste qu'à tout réunir : diagnostiquer, sécuriser et automatiser. Place à la **Partie 7 — Diagnostiquer, sécuriser, automatiser**, la synthèse appliquée du cours.

---

---
---
