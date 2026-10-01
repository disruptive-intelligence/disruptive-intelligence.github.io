---
title: Chapitre 4 — Chercher, filtrer et transformer du texte
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 1 — Survivre dans le terminal
  - index.md
---

## Le minimum à savoir

### L'idée : filtrer un flux

Au chapitre précédent, on **affichait** des fichiers. Maintenant, on va **chercher** dedans et n'en garder que l'utile. C'est une compétence centrale : un fichier de logs peut contenir des dizaines de milliers de lignes, et tu n'en cherches souvent qu'une poignée. L'art de l'administrateur, c'est de **réduire le bruit pour ne voir que le signal**.

### Chercher un texte : `grep`

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

### Trouver des fichiers : `find`

`grep` cherche **dans** les fichiers. `find` cherche **les fichiers eux-mêmes**, par leur nom, leur date, leur taille… Elle parcourt l'arborescence à partir d'un dossier de départ :

```bash
find /etc -name "*.conf"         # tous les fichiers .conf sous /etc
find /home -name "rapport.txt"   # le fichier nommé rapport.txt sous /home
find . -name "*.log"             # tous les .log à partir d'ici (.)
```


La structure de `find` est : `find <où chercher> <critère>`. Le critère le plus courant est `-name` (par nom). L'astérisque `*` signifie « n'importe quelle suite de caractères » : `*.conf` veut dire « tout ce qui se termine par `.conf` ».

### Une alternative rapide : `locate`

`locate` cherche dans une base de données préconstruite, donc c'est **très rapide**, mais la base n'est pas toujours à jour ni installée par défaut :

```bash
locate hostname              # trouve très vite les chemins contenant "hostname"
```


> `find` est toujours fiable (il regarde le système réel, en direct) mais plus lent. `locate` est instantané mais peut rater un fichier récent. Pour débuter, **privilégie `find`** : il ne ment jamais.

## Très utile en pratique

### Le tuyau (pipe) `|` : enchaîner les commandes

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

### Trier et dédoublonner : `sort` et `uniq`

```bash
sort fichier.txt             # trie les lignes par ordre alphabétique
sort -n fichier.txt          # -n : trie numériquement (1, 2, 10) et non (1, 10, 2)
uniq fichier.txt             # supprime les doublons CONSÉCUTIFS
```


> **Le duo classique :** `uniq` ne supprime que les doublons **qui se suivent**. Il faut donc presque toujours trier **avant** : `sort | uniq`. Encore mieux, `sort | uniq -c` trie, dédoublonne **et compte** combien de fois chaque ligne apparaît — extrêmement utile pour répondre à « quelle valeur revient le plus souvent ? ».

### Extraire une colonne : `cut`

Beaucoup de fichiers système sont organisés en colonnes séparées par un caractère. `cut` extrait la colonne qui t'intéresse :

```bash
cut -d: -f1 /etc/passwd      # -d: séparateur ":"   -f1 : 1re colonne
```


Le fichier `/etc/passwd` sépare ses champs par des `:`. La première colonne est le **nom d'utilisateur**. Cette commande liste donc tous les comptes du système. (`-d` = *delimiter*, le séparateur ; `-f` = *field*, le numéro de colonne.)

### Transformer du texte : `tr`, `sed`, `awk` (initiation)

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

## Où sont les logs d'authentification ?

Plusieurs exercices de ce chapitre utilisent un journal d'authentification (les tentatives de connexion). **Son emplacement dépend de ta distribution :**

- Sur **Debian / Ubuntu** : `/var/log/auth.log`
- Sur **RHEL / CentOS / Fedora** : `/var/log/secure`
- Sur **tout système moderne avec systemd** : la méthode la plus fiable est `journalctl` (on l'étudiera en détail au **chapitre 15**)

> Si un fichier d'exemple n'existe pas chez toi, ce n'est pas une erreur de ta part : c'est juste que ta distribution range ses logs ailleurs. Adapte le chemin, ou note que `journalctl` sera la solution universelle vue plus tard.

## ❌ Erreur classique

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

## Exercices

**Guidé :** Dans `/etc/passwd`, affiche uniquement la liste des noms d'utilisateurs (1re colonne), triée par ordre alphabétique. Indice : combine `cut` (avec le séparateur `:`) et `sort` à l'aide d'un pipe.

**Autonome :** Toujours dans `/etc/passwd`, compte combien de comptes existent sur le système de deux façons différentes : avec `wc -l`, puis avec `grep -c ""`. Obtiens-tu le même nombre ? *(C'est normal, les deux comptent les lignes.)*

**Défi (orientation sécurité) :** Sur ton journal d'authentification (`/var/log/auth.log`, ou `/var/log/secure`, selon ta distribution), construis une chaîne de commandes qui :

1. extrait les lignes contenant « Failed password » (avec `grep`),
2. isole l'adresse IP source de chaque tentative (avec `awk`, en repérant la bonne colonne),
3. trie ces IP, les dédoublonne et **compte** combien de fois chacune apparaît (avec `sort` et `uniq -c`).

Tu obtiendras la liste des adresses ayant tenté le plus de connexions échouées — exactement le réflexe d'un analyste SOC face à une attaque par force brute. *(Si le fichier n'existe pas, garde la logique de la chaîne en tête : on la réutilisera avec `journalctl` au chapitre 15.)*

## 🧩 Mini-projet (Partie 1) — Ta première enquête

Mets bout à bout tout ce que tu viens d'apprendre dans une petite investigation. Sur ta machine :

1. **Repère-toi** : place-toi dans `/var/log` et liste son contenu trié par date de modification (`ls -lt`). Quels sont les journaux modifiés le plus récemment ?
2. **Lis** : choisis un fichier de log lisible, affiche ses 20 dernières lignes (`tail`), puis suis-le un instant en direct (`tail -f`, puis `Ctrl + C`).
3. **Cherche** : dans ce log, compte combien de lignes contiennent le mot « error » ou « failed » (insensible à la casse, avec `grep -ic`).
4. **Transforme** : si le log contient des lignes structurées, extrais une colonne intéressante (heure, service…) avec `awk` ou `cut`, et identifie la valeur la plus fréquente avec `sort | uniq -c | sort -n`.
5. **Conclus** : en deux phrases, qu'as-tu appris sur l'activité récente de ta machine ?

Ce mini-projet n'utilise **que** des commandes de lecture et de filtrage : tu mènes une vraie enquête sans rien modifier. C'est l'essence du travail défensif.

## ✅ Tu sais maintenant…

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
