---
title: Chapitre 7 — Liens, redirections et tuyaux
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 2 — Manipuler le système de fichiers
  - index.md
---

## Le minimum à savoir

### Les trois flux : entrée, sortie, erreur

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

### Rediriger la sortie vers un fichier : `>` et `>>`

On l'a effleuré au chapitre 6, voici l'explication propre :

```bash
ls > liste.txt           # > : envoie la sortie dans le fichier (ÉCRASE l'ancien contenu)
ls >> liste.txt          # >> : AJOUTE la sortie à la fin du fichier
```


`>` redirige **stdout** vers un fichier au lieu de l'écran. C'est ainsi qu'on **enregistre** le résultat d'une commande.

> **Le piège classique, redit une fois de plus parce qu'il fait des dégâts :** `>` **écrase** sans prévenir. `commande > fichier-important` détruit le contenu du fichier. En cas de doute, utilise `>>` (ajout) ou redirige d'abord vers un fichier de test.

### Rediriger les erreurs : `2>` et `&>`

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

## Très utile en pratique

### Le pipe `|` : maintenant tu comprends pourquoi ça marche

Le pipe relie la **sortie standard** d'une commande à l'**entrée standard** de la suivante. Ce que tu utilisais au chapitre 4 comme un simple « tuyau » est en fait une redirection de stdout vers stdin :

```bash
cat auth.log | grep "Failed" | wc -l
#   stdout ──► stdin   stdout ──► stdin
```


Chaque `|` branche la sortie de gauche sur l'entrée de droite. C'est le mécanisme qui incarne la philosophie « petits outils combinés ».

### Voir ET enregistrer en même temps : `tee`

Parfois tu veux à la fois **voir** un résultat à l'écran **et** le **garder** dans un fichier. La commande `tee` fait les deux (comme un « T » de plomberie qui sépare un flux en deux) :

```bash
ls -l /etc | tee inventaire.txt          # affiche le résultat ET l'écrit dans inventaire.txt
ls -l /etc | tee -a inventaire.txt       # -a : ajoute au fichier au lieu de l'écraser
```


> **Très utile en pratique :** lors d'une analyse, `commande | tee rapport.txt` te permet de suivre le résultat en direct tout en conservant une trace écrite pour plus tard. Indispensable pour documenter une investigation.

### Appliquer une commande à chaque résultat : `xargs`

`xargs` prend une liste arrivant par un pipe et la transforme en **arguments** pour une autre commande. C'est le pont entre « une liste de noms » et « une action sur chacun » :

```bash
find . -name "*.tmp" | xargs rm          # supprime tous les .tmp trouvés
```


Ici : `find` produit une liste de fichiers → `xargs` la passe à `rm` qui les supprime. C'est puissant… donc à manier avec la prudence habituelle (teste d'abord en remplaçant `rm` par `echo` pour voir ce qui serait fait).

### Les liens symboliques : `ln -s`

Un **lien symbolique** est un « raccourci » : un petit fichier qui pointe vers un autre fichier ou dossier, parfois situé ailleurs. On le crée avec `ln -s` (*link, symbolic*) :

```bash
ln -s /var/log/syslog ~/mon-log         # crée un raccourci "mon-log" vers le vrai fichier
```


Désormais, `~/mon-log` mène au vrai `/var/log/syslog`. Si tu supprimes le lien, le fichier d'origine reste intact (tu n'effaces que le raccourci). Tu reconnaîtras un lien dans un `ls -l` à la flèche `->` qui indique sa cible.

> Il existe aussi des liens « durs » (sans `-s`), plus techniques. Pour débuter, retiens surtout le **lien symbolique** : c'est de loin le plus courant et le plus utile.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Liste le contenu de `/etc` et enregistre-le dans un fichier `etc-liste.txt` avec `>`. Vérifie avec `cat etc-liste.txt`. Relance la même commande mais avec `>>` et observe que le fichier double de taille (l'ajout). Puis recommence avec `>` : le fichier est réécrit de zéro.

**Autonome :** Lance `find /etc -name "*.conf"` deux fois : une fois sans rien, une fois avec `2>/dev/null`. Compare la quantité de messages d'erreur. Ensuite, utilise `tee` pour à la fois afficher la liste des `.conf` et l'enregistrer dans `confs.txt`.

**Défi :** Crée un lien symbolique vers ton journal système quelque part dans ton dossier personnel (`ln -s`). Vérifie avec `ls -l` que la flèche `->` pointe vers la bonne cible. Lis le log à travers ton lien (`tail mon-lien`). Puis supprime **le lien** et confirme avec `ls` que le fichier d'origine, lui, existe toujours.

## ✅ Tu sais maintenant…

- Les **trois flux** : entrée (stdin), sortie (stdout), erreur (stderr) — et que sortie et erreur sont **séparées**
- Rediriger la sortie avec `>` (écrase) et `>>` (ajoute)
- Rediriger les erreurs avec `2>`, les fusionner avec `2>&1` ou `&>`, et les jeter avec `2>/dev/null`
- **Pourquoi** le pipe `|` fonctionne : il relie stdout à stdin
- Voir **et** enregistrer en même temps avec `tee`
- Appliquer une action à chaque résultat avec `xargs` (en testant d'abord avec `echo`)
- Créer un raccourci avec un **lien symbolique** (`ln -s`) et le reconnaître au `->`

---
