---
title: PARTIE VI — CRÉER ET STRUCTURER UNE BASE
source: IT/Culture/SQL.md
note: SQL
chapter: 6
chapters: 8
---

-----


## Chapitre 24 — Créer une table avec CREATE TABLE

### Le minimum à savoir

#### La structure de base

```sql
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    city TEXT
);
```

Décodage :

- `CREATE TABLE readers` → crée une table nommée `readers`
- `(...)` → la liste des colonnes
- Pour chaque colonne : un nom, un type, et éventuellement des contraintes

#### Anatomie d’une définition de colonne

```
nom_colonne    TYPE       contrainte1 contrainte2 ...
─────────────  ─────────  ───────────────────────
first_name     TEXT       NOT NULL
id             INTEGER    PRIMARY KEY
email          TEXT       UNIQUE
status         TEXT       DEFAULT 'borrowed'
```

#### Supprimer une table : `DROP TABLE`

```sql
DROP TABLE readers;        -- ❌ ❌ ❌ supprime DÉFINITIVEMENT la table et toutes ses données
```

> **⚠️ Extrême prudence avec `DROP TABLE`**. Contrairement à `DELETE`, qui ne supprime que les lignes, `DROP TABLE` détruit la structure elle-même. Sans sauvegarde, c’est irréversible.

#### Modifier une table existante : `ALTER TABLE`

```sql
ALTER TABLE readers ADD COLUMN birth_date TEXT;        -- ajouter une colonne
ALTER TABLE readers RENAME TO members;                  -- renommer la table
```

> **Note :** SQLite a longtemps eu un support limité de `ALTER TABLE` (pas de `DROP COLUMN` jusqu’en SQLite 3.35). C’est l’un des points où les SGBD diffèrent. Pour ce cours, on se concentre sur `CREATE TABLE`.

#### `IF NOT EXISTS` : créer seulement si la table n’existe pas

```sql
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL
);
```

Pratique pour les scripts d’initialisation : si la table existe déjà, on ne tente pas de la recréer (et donc pas d’erreur).

> **📋 FIL ROUGE — Épisode 23**
> 
> La directrice veut ajouter une fonctionnalité : suivre les **événements organisés** par la médiathèque (ateliers, conférences, club de lecture). Nora crée une nouvelle table :
> 
> ```sql
> CREATE TABLE events (
>     id INTEGER PRIMARY KEY,
>     title TEXT NOT NULL,
>     event_date TEXT NOT NULL,
>     max_participants INTEGER DEFAULT 20,
>     description TEXT
> );
> ```
> 
> Une table avec sa clé primaire, des contraintes simples, et une valeur par défaut. La structure est faite — il reste à insérer des données et à l’utiliser.

### ❌ Erreur classique

```sql
-- Oublier les virgules entre colonnes
CREATE TABLE readers (
    id INTEGER PRIMARY KEY
    first_name TEXT NOT NULL              -- ❌ pas de virgule après PRIMARY KEY
);

-- Mettre une virgule en trop après la dernière colonne
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,            -- ❌ virgule de trop
);

-- Confondre DROP TABLE et DELETE
DROP TABLE readers;       -- détruit la table
DELETE FROM readers;       -- vide la table mais la garde
```

### ✅ Tu sais maintenant…

- Créer une table avec `CREATE TABLE nom (colonne TYPE contrainte, ...)`
- Supprimer une table avec `DROP TABLE` (irréversible !)
- `IF NOT EXISTS` pour les scripts d’initialisation
- `ALTER TABLE` pour modifier (de manière limitée en SQLite)

-----


## Chapitre 25 — Types de données et contraintes

### Le minimum à savoir

#### Les types de données SQLite

SQLite utilise un système de types simple, dit “à classes de stockage” :

|Type     |Contenu                                           |
|---------|--------------------------------------------------|
|`INTEGER`|Nombre entier (`5`, `-12`, `42000`)               |
|`REAL`   |Nombre décimal (`3.14`, `1.5`, `-0.001`)          |
|`TEXT`   |Chaîne de caractères (`'Bonjour'`, `'2026-05-03'`)|
|`BLOB`   |Données binaires (image, fichier — rare)          |
|`NULL`   |Absence de valeur                                 |

Pour les **dates**, SQLite n’a pas de type dédié — on utilise `TEXT` au format `'YYYY-MM-DD'` ou `'YYYY-MM-DD HH:MM:SS'`. C’est suffisant pour 99% des cas.

> **Note :** PostgreSQL et MySQL ont des types plus stricts (`VARCHAR(50)`, `DATE`, `TIMESTAMP`, `BOOLEAN`…). En SQLite, c’est plus laxiste — un peu comme Python par rapport à C. Tu reverras les vrais types fixes quand tu passeras à un autre SGBD.

#### Les contraintes essentielles

|Contrainte                               |Effet                                      |
|-----------------------------------------|-------------------------------------------|
|`PRIMARY KEY`                            |Identifiant unique de la table             |
|`NOT NULL`                               |Valeur obligatoire (pas de NULL)           |
|`UNIQUE`                                 |Toutes les valeurs doivent être différentes|
|`DEFAULT valeur`                         |Valeur par défaut si non fournie           |
|`CHECK (condition)`                      |Règle de validation personnalisée          |
|`FOREIGN KEY (col) REFERENCES table(col)`|Clé étrangère vers une autre table         |

#### Exemple complet

```sql
CREATE TABLE loans (
    id INTEGER PRIMARY KEY,
    reader_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL DEFAULT 'borrowed',
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (status IN ('borrowed', 'returned', 'late'))
);
```

Ce que ça garantit :

- `id` : identifiant unique automatique
- `reader_id`, `book_id`, `loan_date` : ne peuvent pas être `NULL`
- `return_date` : peut être `NULL` (pour les emprunts en cours)
- `status` : si non fourni, vaut `'borrowed'` ; et ne peut être que `'borrowed'`, `'returned'` ou `'late'` (grâce au `CHECK`)
- Les `reader_id` et `book_id` doivent exister respectivement dans `readers.id` et `books.id`

#### Pourquoi les contraintes sont cruciales

Sans contraintes, ta base se remplit de données incohérentes :

- Des emprunts qui pointent vers des lecteurs qui n’existent pas
- Des `status` avec des valeurs comme `'lost'`, `'pending'`, `'???'`, `''`, `NULL`…
- Des emails dupliqués sur 12 utilisateurs différents
- Des dates au format `'15/03/2025'` mélangées avec `'2025-03-15'`

Les contraintes forcent la qualité dès l’**écriture** — c’est beaucoup mieux que de nettoyer après coup.

> **À retenir :** chaque fois que tu crées une table, demande-toi pour chaque colonne : peut-elle être vide ? Doit-elle être unique ? Y a-t-il une valeur par défaut sensée ? Y a-t-il un lien vers une autre table ?

> **📋 FIL ROUGE — Épisode 24**
> 
> La directrice veut ajouter un système de réservation. Nora conçoit la table avec contraintes :
> 
> ```sql
> CREATE TABLE reservations (
>     id INTEGER PRIMARY KEY,
>     reader_id INTEGER NOT NULL,
>     book_id INTEGER NOT NULL,
>     reservation_date TEXT NOT NULL DEFAULT (DATE('now')),
>     status TEXT NOT NULL DEFAULT 'pending',
>     FOREIGN KEY (reader_id) REFERENCES readers(id),
>     FOREIGN KEY (book_id) REFERENCES books(id),
>     CHECK (status IN ('pending', 'fulfilled', 'cancelled'))
> );
> ```
> 
> Cette table est **autoprotégée** : impossible d’insérer un statut farfelu, impossible de réserver pour un lecteur qui n’existe pas. La qualité des données est garantie par la structure.

### Très utile en pratique

#### `PRIMARY KEY` composite

Pour une table d’association comme `book_authors`, la clé primaire combine deux colonnes :

```sql
CREATE TABLE book_authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),     -- combinaison unique
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
```

Un même couple `(book_id, author_id)` ne peut pas apparaître deux fois — pas de doublon possible.

### ❌ Erreur classique

```sql
-- Oublier NOT NULL sur une colonne qui ne devrait jamais être vide
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT          -- ⚠️ peut être NULL → un user sans email passe
);

-- Oublier UNIQUE sur une colonne qui devrait l'être
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL  -- ⚠️ deux users peuvent avoir le même email
);
-- ✅
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);

-- Oublier la FOREIGN KEY (alors la cohérence n'est pas garantie)
CREATE TABLE loans (
    reader_id INTEGER       -- ⚠️ peut pointer vers un id inexistant
);
```

### 💡 Exercices

1. Crée une table `categories_v2` avec `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL UNIQUE`, et `description TEXT`.
1. Crée une table `subscriptions` (abonnements payants des lecteurs) avec `id`, `reader_id` (FK vers `readers`), `start_date`, `end_date`, `subscription_type` (avec `CHECK` sur 3 valeurs autorisées : ‘monthly’, ‘yearly’, ‘lifetime’).
1. Insère deux lignes valides dans `subscriptions`. Tente une 3e avec un type non autorisé — observe l’erreur.

### ✅ Tu sais maintenant…

- Les types SQLite : `INTEGER`, `REAL`, `TEXT`, `BLOB`
- Les contraintes : `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY`
- Les contraintes garantissent la qualité des données dès l’écriture
- `PRIMARY KEY` composite pour les tables d’association

-----


## Chapitre 26 — Modélisation simple

### Le minimum à savoir

#### Le défi : passer d’un besoin métier à des tables

Quand on dit “je veux gérer une médiathèque”, il faut traduire ça en :

- Quelles **entités** principales ?
- Quels **attributs** pour chaque entité ?
- Quelles **relations** entre les entités ?

C’est l’exercice de **modélisation**.

#### La méthode en 4 étapes

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

#### Trois principes simples

1. **Chaque entité a sa table.** N’écrase pas plusieurs entités dans une seule table.
1. **Pas de répétition d’information.** Si tu te retrouves à recopier le même nom 50 fois, sépare en deux tables.
1. **Une cellule = une seule valeur.** Pas de “Hugo, Camus, Orwell” dans une cellule — utilise une table d’association.

> **À retenir :** ces trois principes correspondent à la **première forme normale (1NF)** de la théorie relationnelle. On en reste là — les formes 2NF et 3NF sont des raffinements utiles mais pas indispensables pour débuter.

#### Aperçu des formes normales

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

### Très utile en pratique

#### Quand séparer ou non ?

**Sépare** quand :

- Une entité existe **indépendamment** (un auteur existe même s’il n’a écrit qu’un livre)
- Tu vas avoir des **relations N-N** (livres ↔ auteurs)
- Tu auras des **statistiques par groupe** (livres par catégorie)

**Garde dans une seule table** quand :

- L’attribut est trivial (une simple colonne `city` dans `readers` suffit — pas besoin de table `cities`)
- Il n’y a pas de duplication problématique

#### Le piège des “vraies” et “fausses” duplications

Stocker “Paris” 100 fois dans la colonne `city` de `readers` n’est **pas** une duplication problématique — c’est juste de la donnée. Mais stocker `"Paris, France"` 100 fois si tu as déjà une table `countries` avec `France` dedans, c’est un problème (3NF).

Pour démarrer, sois pragmatique : une simple colonne `city` suffit. Tu sépareras en table `cities` le jour où tu en auras besoin (statistiques, géolocalisation, multi-langue…).

### ✅ Tu sais maintenant…

- Identifier les entités, attributs et relations à partir d’un besoin métier
- Les 3 principes : une entité = une table, pas de répétition, une cellule = une valeur
- L’aperçu des formes normales (1NF, 2NF, 3NF)
- Quand séparer ou non en plusieurs tables

### 🧩 Capstone Partie VI — Mini-projet

La médiathèque veut un système d’**ateliers** payants pour les lecteurs. Chaque atelier a un titre, une description, une date, un nombre maximum de participants, un prix. Les lecteurs peuvent s’inscrire à plusieurs ateliers, et un atelier peut avoir plusieurs participants.

**Tâche :**

1. Identifie les entités, attributs et relations.
1. Crée les tables nécessaires avec contraintes.
1. Insère 3 ateliers et 5 inscriptions.
1. Écris une requête qui affiche pour chaque atelier le nombre d’inscrits actuels.

-----
