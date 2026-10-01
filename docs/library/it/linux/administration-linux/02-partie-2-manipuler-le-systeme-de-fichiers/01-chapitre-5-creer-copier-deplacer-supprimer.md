---
title: Chapitre 5 — Créer, copier, déplacer, supprimer
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 2 — Manipuler le système de fichiers
  - index.md
---

## Le minimum à savoir

### Créer un fichier vide : `touch`

`touch` crée un fichier vide s'il n'existe pas (et met à jour sa date s'il existe déjà) :

```bash
touch rapport.txt        # crée un fichier vide nommé rapport.txt
touch fichier1 fichier2  # on peut en créer plusieurs d'un coup
```


C'est la façon la plus rapide de « poser » un fichier avant de le remplir.

### Créer un dossier : `mkdir`

`mkdir` (*make directory*) crée un dossier :

```bash
mkdir projet             # crée un dossier "projet"
```


Et si tu veux créer toute une arborescence d'un coup, l'option `-p` crée les dossiers parents manquants :

```bash
mkdir -p projet/logs/2025    # crée projet, puis logs, puis 2025
```


Sans `-p`, la commande échouerait si `projet` ou `logs` n'existaient pas encore. **Le `-p` est le réflexe pour créer un chemin complet.**

### Copier : `cp`

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

### Déplacer et renommer : `mv`

`mv` (*move*) sert à **deux** choses qui sont en réalité la même : déplacer, et renommer.

```bash
mv rapport.txt /tmp/               # DÉPLACE le fichier dans /tmp
mv rapport.txt bilan.txt           # RENOMME le fichier (le "déplace" vers un nouveau nom)
```


Renommer, pour Linux, c'est juste déplacer un fichier vers un nouveau nom au même endroit. Pas besoin de commande séparée.

### Supprimer : `rm` (la commande à respecter)

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


## Très utile en pratique

### Le filet de sécurité : `rm -i`

L'option `-i` (*interactive*) demande **confirmation** avant chaque suppression :

```bash
rm -i rapport.txt
# rm: supprimer fichier 'rapport.txt' ? (o/n)
```


C'est un excellent réflexe quand tu débutes, ou avant une suppression importante. Tu reprends la main sur une opération irréversible.

### Appliquer les règles d'or

Souviens-toi de la Partie 0. Avant toute suppression, le bon réflexe est :

```bash
pwd                      # 1. où suis-je vraiment ?
ls                       # 2. qu'est-ce qu'il y a ici, exactement ?
rm -i fichier-a-virer    # 3. je supprime, avec confirmation
```


Ces trois secondes de vérification t'éviteront un jour une vraie catastrophe.

### ⚠️ `rm -rf` : la commande qui ne pardonne pas

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

## ❌ Erreur classique

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


## Exercices

**Guidé :** Crée d'un seul `mkdir -p` l'arborescence `atelier/scripts/sauvegardes`. Place-toi dedans, crée trois fichiers vides avec `touch` (`a.sh`, `b.sh`, `c.sh`), puis vérifie le tout avec `ls -R atelier` (le `-R` liste récursivement).

**Autonome :** Dans le dossier `atelier`, copie `scripts/a.sh` vers `scripts/a.sh.bak` (une sauvegarde). Renomme ensuite `b.sh` en `principal.sh`. Vérifie le résultat avec `ls`. Combien de fichiers y a-t-il maintenant dans `scripts` ?

**Défi :** Crée un dossier `lab-test` avec quelques fichiers à l'intérieur. Avant de le supprimer, entraîne-toi au réflexe de sécurité : fais `ls lab-test/` pour voir ce qu'il contient, puis supprime-le entièrement avec `rm -r`. Recommence en utilisant `rm -ri` pour voir la différence (confirmation à chaque élément). Lequel te semble plus prudent quand l'enjeu est important ?

## ✅ Tu sais maintenant…

- Créer des fichiers (`touch`) et des dossiers (`mkdir`, et `mkdir -p` pour une arborescence)
- Copier avec `cp` (et `-r` pour les dossiers, `-i` pour éviter d'écraser)
- Déplacer **et** renommer avec `mv` (c'est la même opération)
- Supprimer avec `rm` — **définitivement** — et la sécurité `rmdir` pour les dossiers vides
- Te protéger avec `rm -i`, et appliquer le réflexe `pwd` → `ls` → suppression
- Pourquoi `rm -rf` est puissant **et** dangereux, et comment le manipuler sans accident

---
