---
title: Chapitre 26 — Modélisation simple
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VI — Créer ET structurer une base
  - index.md
---

## Le minimum à savoir

### Le défi : passer d’un besoin métier à des tables

Quand on dit “je veux gérer une médiathèque”, il faut traduire ça en :

- Quelles **entités** principales ?
- Quels **attributs** pour chaque entité ?
- Quelles **relations** entre les entités ?

C’est l’exercice de **modélisation**.

### La méthode en 4 étapes

**Étape 1 — Identifier les entités principales**

Une entité = une “chose” du monde réel qu’on veut suivre.

Pour la médiathèque :

- Lecteurs
- Livres
- Auteurs
- Catégories

Chaque entité devient une **table**.

**Étape 2 — Lister les attributs de chaque entité**

Un attribut = une caractéristique. Chaque attribut devient une **colonne**.

`readers` :

- `first_name`, `last_name`, `email`, `city`, `phone`, `registration_date`

`books` :

- `title`, `publication_year`, `isbn`

**Étape 3 — Identifier les relations**

- Un livre appartient à **une** catégorie → relation 1-N → clé étrangère `category_id` dans `books`
- Un livre peut avoir **plusieurs** auteurs, et un auteur **plusieurs** livres → relation N-N → table d’association `book_authors`
- Un lecteur peut faire **plusieurs** emprunts, et un emprunt concerne **un** livre et **un** lecteur → table `loans` avec `reader_id` et `book_id`

**Étape 4 — Ajouter une clé primaire à chaque table**

Toujours `id INTEGER PRIMARY KEY`.

### Trois principes simples

1. **Chaque entité a sa table.** N’écrase pas plusieurs entités dans une seule table.
1. **Pas de répétition d’information.** Si tu te retrouves à recopier le même nom 50 fois, sépare en deux tables.
1. **Une cellule = une seule valeur.** Pas de “Hugo, Camus, Orwell” dans une cellule — utilise une table d’association.

> **À retenir :** ces trois principes correspondent à la **première forme normale (1NF)** de la théorie relationnelle. On en reste là — les formes 2NF et 3NF sont des raffinements utiles mais pas indispensables pour débuter.

### Aperçu des formes normales

|Forme|Idée                        |Exemple                                                |
|-----|----------------------------|-------------------------------------------------------|
|1NF  |Une cellule = une valeur    |Pas de “Hugo, Orwell” dans une cellule                 |
|2NF  |Une table = un sujet        |Pas mélanger lecteurs et emprunts dans la même table   |
|3NF  |Pas de dépendance transitive|Stocker `category_id` dans `books`, pas `category_name`|


> **Pour aller plus loin :** la modélisation poussée (UML, MCD, MLD, formes normales BCNF/4NF/5NF) est un sujet de cours dédié. Pour démarrer, retiens les 3 principes ci-dessus — ils couvrent 95% des cas.

> **📋 FIL ROUGE — Épisode 25**
> 
> La directrice veut ajouter le suivi des **dons de livres** par les lecteurs. Nora applique la méthode :
> 
> 1. **Entité** : un don
> 1. **Attributs** : qui a donné ? quel livre ? quand ? statut (accepté/refusé/en attente) ?
> 1. **Relations** : un don concerne un lecteur (1-N depuis `readers`) et peut concerner un livre (référence vers `books` une fois accepté)
> 
> Sa table :
> 
> ```sql
> CREATE TABLE donations (
>     id INTEGER PRIMARY KEY,
>     donor_reader_id INTEGER NOT NULL,
>     proposed_title TEXT NOT NULL,
>     book_id INTEGER,
>     donation_date TEXT NOT NULL,
>     status TEXT NOT NULL DEFAULT 'pending',
>     FOREIGN KEY (donor_reader_id) REFERENCES readers(id),
>     FOREIGN KEY (book_id) REFERENCES books(id),
>     CHECK (status IN ('pending', 'accepted', 'refused'))
> );
> ```
> 
> Le `book_id` est nullable : tant que le don n’est pas accepté, il n’y a pas de livre dans le catalogue. Modélisation propre.

## Très utile en pratique

### Quand séparer ou non ?

**Sépare** quand :

- Une entité existe **indépendamment** (un auteur existe même s’il n’a écrit qu’un livre)
- Tu vas avoir des **relations N-N** (livres ↔ auteurs)
- Tu auras des **statistiques par groupe** (livres par catégorie)

**Garde dans une seule table** quand :

- L’attribut est trivial (une simple colonne `city` dans `readers` suffit — pas besoin de table `cities`)
- Il n’y a pas de duplication problématique

### Le piège des “vraies” et “fausses” duplications

Stocker “Paris” 100 fois dans la colonne `city` de `readers` n’est **pas** une duplication problématique — c’est juste de la donnée. Mais stocker `"Paris, France"` 100 fois si tu as déjà une table `countries` avec `France` dedans, c’est un problème (3NF).

Pour démarrer, sois pragmatique : une simple colonne `city` suffit. Tu sépareras en table `cities` le jour où tu en auras besoin (statistiques, géolocalisation, multi-langue…).

## ✅ Tu sais maintenant…

- Identifier les entités, attributs et relations à partir d’un besoin métier
- Les 3 principes : une entité = une table, pas de répétition, une cellule = une valeur
- L’aperçu des formes normales (1NF, 2NF, 3NF)
- Quand séparer ou non en plusieurs tables

## 🧩 Capstone Partie VI — Mini-projet

La médiathèque veut un système d’**ateliers** payants pour les lecteurs. Chaque atelier a un titre, une description, une date, un nombre maximum de participants, un prix. Les lecteurs peuvent s’inscrire à plusieurs ateliers, et un atelier peut avoir plusieurs participants.

**Tâche :**

1. Identifie les entités, attributs et relations.
1. Crée les tables nécessaires avec contraintes.
1. Insère 3 ateliers et 5 inscriptions.
1. Écris une requête qui affiche pour chaque atelier le nombre d’inscrits actuels.

-----
