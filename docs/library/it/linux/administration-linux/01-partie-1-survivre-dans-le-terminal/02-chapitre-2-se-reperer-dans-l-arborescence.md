---
title: Chapitre 2 — Se repérer dans l'arborescence
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 1 — Survivre dans le terminal
  - index.md
---

## Le minimum à savoir

### Le système de fichiers est un arbre

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

### Où suis-je ? `pwd`

La toute première question quand on est perdu : **dans quel dossier suis-je ?** La commande `pwd` (*print working directory*, « affiche le dossier de travail ») répond :

```bash
pwd
# affiche par exemple : /home/alice
```


> **Réflexe à prendre dès maintenant :** quand tu ne sais plus où tu es, tape `pwd`. C'est gratuit et ça évite les catastrophes (souviens-toi de la première règle d'or : vérifier où on est avant d'agir).

### Que contient ce dossier ? `ls`

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

### Se déplacer : `cd`

`cd` (*change directory*) te déplace d'un dossier à un autre :

```bash
cd /var/log      # va dans le dossier /var/log
cd /             # va à la racine
cd ~             # va dans ton dossier personnel
cd               # (sans rien) va aussi dans ton dossier personnel
```


## Très utile en pratique

### Chemins absolus et chemins relatifs

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

### Visualiser l'arbre : `tree`

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


### Les grands dossiers de Linux (le FHS)

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

## ❌ Erreur classique

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


## Exercices

**Guidé :** Depuis ton dossier personnel (`cd ~`), rends-toi dans `/var/log` en utilisant un **chemin absolu**. Vérifie avec `pwd` que tu y es bien. Liste son contenu avec `ls -l`. Puis reviens à ton point de départ avec `cd -`.

**Autonome :** Place-toi à la racine (`cd /`). Sans jamais utiliser de chemin absolu (uniquement `cd nom`, `cd ..`, etc.), navigue jusqu'à `/usr/bin`, vérifie ta position avec `pwd`, puis remonte jusqu'à la racine uniquement avec `..`.

**Défi :** Affiche l'arborescence de `/etc` sur 2 niveaux de profondeur seulement, et compare la quantité d'informations avec un `ls` simple du même dossier. Lequel est plus lisible pour avoir une vue d'ensemble ?

## ✅ Tu sais maintenant…

- Que le système Linux est un **arbre unique** partant de la racine `/`
- Répondre à « où suis-je ? » avec `pwd` (le réflexe anti-catastrophe)
- Lister un dossier avec `ls` et ses options clés : `-l`, `-a`, `-h`, `-t`
- Te déplacer avec `cd`, et utiliser `~`, `..`, `.` et `cd -`
- La différence **fondamentale** entre chemin **absolu** (part de `/`) et **relatif** (part d'où tu es)
- Reconnaître les grands dossiers du **FHS**, en particulier `/etc` et `/var/log`
- Protéger les noms contenant des **espaces** avec des guillemets

---
