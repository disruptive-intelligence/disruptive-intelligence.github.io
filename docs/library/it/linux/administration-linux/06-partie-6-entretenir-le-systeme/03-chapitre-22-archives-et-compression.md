---
title: Chapitre 22 — Archives et compression
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 6 — Entretenir le système
  - index.md
---

## Le minimum à savoir

### Archiver ≠ compresser

Deux opérations distinctes, qu'on combine souvent :

- **Archiver**, c'est **regrouper** plusieurs fichiers et dossiers en un seul fichier (sans forcément réduire la taille). L'outil historique est `tar`, qui produit un fichier `.tar` (une « archive »).
- **Compresser**, c'est **réduire la taille** des données. Les outils courants sont `gzip` (`.gz`), et d'autres comme `xz` ou `bzip2`.

Le plus souvent, on fait les deux d'un coup : on regroupe avec `tar`, et on compresse au passage, ce qui donne un `.tar.gz` (parfois écrit `.tgz`). C'est le format d'archive le plus répandu sous Linux.

### Créer et extraire une archive : `tar`

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


## Très utile en pratique

### Compresser un fichier seul : `gzip`

Pour compresser un fichier unique (sans archive) :

```bash
gzip gros-fichier.log        # crée gros-fichier.log.gz et SUPPRIME l'original
gunzip gros-fichier.log.gz   # décompresse (récupère l'original)
zcat fichier.log.gz          # lire un fichier compressé SANS le décompresser
```


> **Très utile en pratique :** tu te souviens des logs archivés du chapitre 15 (`auth.log.2.gz`) ? C'est exactement du gzip. `zcat`, `zless` et `zgrep` permettent de **lire et chercher dans les logs compressés sans les décompresser** — précieux pour fouiller d'anciens journaux lors d'une investigation.

### Le format zip : `zip` / `unzip`

Pour échanger avec des systèmes Windows, le format `.zip` est plus universel :

```bash
zip -r archive.zip dossier/  # créer un zip d'un dossier (-r pour le contenu)
unzip archive.zip            # extraire un zip
```


`zip`/`unzip` ne sont pas toujours installés (`sudo apt install zip unzip`).

## ❌ Erreur classique

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


## Exercices

**Guidé :** Crée un dossier avec quelques fichiers. Archive-le et compresse-le en une commande : `tar -czvf sauvegarde.tar.gz mondossier/`. Observe la liste défiler (grâce au `v`). Vérifie le contenu sans extraire avec `tar -tzvf sauvegarde.tar.gz`, puis extrais-le dans un autre dossier de test.

**Autonome :** Prends un fichier texte assez gros (par exemple une copie d'un log). Compresse-le avec `gzip -k` (en gardant l'original), puis compare les tailles avec `ls -lh` : quel gain de place obtiens-tu ? Lis ensuite le fichier compressé avec `zcat` sans le décompresser.

**Défi (orientation admin/SOC) :** Prépare une « collecte » de logs comme pour une investigation. Archive et compresse en une fois le contenu de `/var/log` (ce qui est lisible) dans un fichier horodaté : `sudo tar -czvf logs-$(date +%F).tar.gz /var/log/ 2>/dev/null`. Le `$(date +%F)` insère la date du jour dans le nom (tu reverras cette technique en Bash, chapitre 26). Vérifie l'archive créée et sa taille. Pourquoi horodater le nom d'une archive de logs est-il une bonne pratique ?

## ✅ Tu sais maintenant…

- La différence entre **archiver** (regrouper, `tar`) et **compresser** (réduire, `gzip`)
- Créer une archive compressée avec `tar -czvf` et l'extraire avec `tar -xzvf` (le `f` avant le nom)
- Lister le contenu d'une archive sans extraire (`tar -tzvf`)
- Compresser un fichier seul (`gzip`, `-k` pour garder l'original)
- **Lire/chercher dans un fichier compressé** sans le décompresser (`zcat`, `zgrep`)
- Utiliser le format `.zip` (`zip -r`, `unzip`) pour l'échange avec Windows

---
