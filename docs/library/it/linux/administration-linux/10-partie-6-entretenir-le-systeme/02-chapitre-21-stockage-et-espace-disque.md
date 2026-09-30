---
title: Chapitre 21 — Stockage et espace disque
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 6 — Entretenir le système
  - index.md
---

## Le minimum à savoir

### Comprendre les niveaux

disque, partition, système de fichiers, point de montage

Le stockage sous Linux se comprend par couches, qu'il faut distinguer pour ne pas se perdre :

- Un **disque** physique (ou virtuel) : le matériel, par exemple `/dev/sda`.
- Une **partition** : une division du disque, par exemple `/dev/sda1`. Un disque peut être découpé en plusieurs partitions.
- Un **système de fichiers** : la façon dont les données sont organisées **dans** une partition (ext4, xfs…). C'est ce qui transforme un espace brut en quelque chose qui contient des fichiers.
- Un **point de montage** : l'**endroit dans l'arborescence** (chapitre 2) où ce système de fichiers devient accessible. C'est le concept clé : sous Linux, un disque n'apparaît pas comme « lecteur D: », il est **« monté »** à un endroit de l'arbre unique, par exemple `/` ou `/home` ou `/mnt/usb`.

> **L'idée à retenir :** sous Linux, on ne « voit » pas les disques séparément ; on les **rattache** (monte) à des dossiers de l'arborescence unique. Ouvrir un dossier peut donc, en réalité, accéder à un autre disque — de façon totalement transparente.

### Voir l'espace disque : `df`

`df` (*disk free*) montre l'espace **utilisé et disponible** sur chaque système de fichiers monté :

```bash
df -h            # -h = tailles lisibles (Go, Mo) ; vue d'ensemble de l'espace
```


Chaque ligne montre un système de fichiers, sa taille, l'espace utilisé, l'espace libre, et son **point de montage**. C'est le premier réflexe quand on se demande « est-ce que mon disque est plein ? ».

### Voir ce qui prend de la place : `du`

Là où `df` regarde les disques globalement, `du` (*disk usage*) mesure la taille **des fichiers et dossiers** :

```bash
du -sh dossier/          # -s = total (summary), -h = lisible : taille totale du dossier
du -h --max-depth=1 /var # taille de chaque sous-dossier de /var, un niveau
```


> **La confusion classique `df` vs `du` :** `df` répond « combien d'espace reste-t-il **sur le disque** ? » (vue globale, par système de fichiers). `du` répond « combien pèse **ce dossier** ? » (vue détaillée, par fichier). Quand un disque se remplit, on utilise `df` pour le **constater**, puis `du` pour **trouver le coupable**.

## Très utile en pratique

### Trouver ce qui remplit le disque

Le combo gagnant quand `df -h` annonce un disque presque plein : descendre avec `du` pour localiser les gros dossiers, en triant (chapitre 4) :

```bash
sudo du -h --max-depth=1 / | sort -rh | head    # les plus gros dossiers à la racine
```


Ici : `du` mesure chaque dossier de premier niveau, `sort -rh` trie par taille décroissante (`-r` inverse, `-h` comprend les tailles lisibles), `head` garde le haut du classement. On répète ensuite dans le dossier coupable pour affiner. C'est l'enquête type « où est passé mon espace ? ».

### Voir les disques et partitions : `lsblk`

`lsblk` (*list block devices*) affiche les disques et leurs partitions sous forme d'arbre — la vue « matériel » du stockage :

```bash
lsblk            # disques, partitions, tailles et points de montage
```


C'est l'outil idéal pour **observer** la structure de stockage sans rien risquer : quels disques existent, comment ils sont découpés, et où chaque partition est montée.

### Voir précisément ce qui est monté : `findmnt`

`findmnt` affiche la liste des systèmes de fichiers montés, joliment présentée en arbre, avec leur source et leurs options :

```bash
findmnt          # arbre clair de tous les points de montage
findmnt /home    # info sur un point de montage précis
```


> **Très utile en pratique :** `lsblk` (les disques) et `findmnt` (les montages) sont tes deux outils d'**observation** du stockage. Ils ne modifient rien, et te donnent une vue complète et sûre de la situation. Prends le réflexe de les consulter **avant** toute action.

### `/etc/fstab` : les montages permanents

Comment le système sait-il quels disques monter, et où, à chaque démarrage ? Grâce au fichier **`/etc/fstab`** (*file systems table*). Chaque ligne y décrit un système de fichiers et son point de montage permanent.

```bash
cat /etc/fstab           # lire la table des montages permanents (lecture sans risque)
```


> **À ton niveau : lire, comprendre — pas modifier.** Apprends d'abord à **lire** `/etc/fstab` pour comprendre comment ta machine est organisée. Le **modifier** est une opération sensible : une erreur peut empêcher la machine de démarrer correctement. Si tu dois un jour y toucher, applique le réflexe du chapitre 6 (copie `.bak` d'abord) et procède avec une grande prudence.

### Monter et démonter : `mount` / `umount` (avec prudence)

Pour rattacher temporairement un système de fichiers (une clé USB, un partage réseau) à un dossier, on utilise `mount` ; pour le détacher, `umount`. Ce sont des opérations **privilégiées** et **sensibles**.

```bash
sudo mount /dev/sdb1 /mnt/usb        # monte une partition sur /mnt/usb (montage temporaire)
sudo umount /mnt/usb                 # démonte proprement
```


> **⚠️ Prudence (rappel de la Partie 0) :** `mount` et `umount` figurent parmi les commandes sensibles. Démonter un disque en cours d'utilisation, ou se tromper de périphérique, peut perturber l'accès aux données ou provoquer des pertes. **Pour un débutant, on commence par observer** avec `lsblk`, `df` et `findmnt` ; on ne monte/démonte qu'en sachant exactement quel périphérique on manipule, idéalement en lab. Distinction utile : un montage par `mount` est **temporaire** (perdu au redémarrage) ; un montage **permanent** passe par `/etc/fstab`.

### La mémoire vive : `free`

Au passage, pour la mémoire (RAM), qui n'est pas du stockage disque mais qu'on surveille de la même façon :

```bash
free -h          # mémoire totale, utilisée, libre, et swap (en tailles lisibles)
```


## ❌ Erreur classique

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


## Exercices

**Guidé :** Affiche l'espace disque global avec `df -h`. Repère le système de fichiers monté sur `/` : quelle proportion est utilisée ? Ensuite, mesure la taille de ton dossier personnel avec `du -sh ~`. Compare : ton dossier représente-t-il une grande part de l'espace utilisé ?

**Autonome :** Observe la structure de stockage de ta machine avec `lsblk`, puis avec `findmnt`. Combien de disques/partitions vois-tu ? Où est monté chacun ? Enfin, lis `/etc/fstab` avec `cat` et essaie de faire le lien entre ce fichier et ce que `findmnt` t'a montré.

**Défi :** Mène l'enquête « où est passé mon espace ? ». Pars de `df -h` pour repérer le système de fichiers le plus rempli. Puis, avec `sudo du -h --max-depth=1 / | sort -rh | head`, identifie les plus gros dossiers à la racine. Descends d'un niveau dans le coupable et répète, jusqu'à localiser précisément ce qui occupe le plus d'espace. Quel dossier as-tu trouvé ?

## ✅ Tu sais maintenant…

- Distinguer **disque**, **partition**, **système de fichiers** et **point de montage**
- Que Linux **monte** les disques dans son arborescence unique (pas de « lecteur D: »)
- Voir l'espace global avec `df -h` et la taille des dossiers avec `du -sh`
- La distinction **`df`** (espace du disque) vs **`du`** (taille d'un dossier), et l'enquête `du | sort -rh | head`
- **Observer** le stockage sans risque avec `lsblk` (disques) et `findmnt` (montages)
- Lire `/etc/fstab` pour comprendre les montages permanents (sans le modifier à la légère)
- Que `mount`/`umount` sont **sensibles** : on observe d'abord, on agit en connaissant le périphérique
- Surveiller la mémoire avec `free -h`

---
