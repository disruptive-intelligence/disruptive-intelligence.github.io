---
title: Chapitre 24 — Créer une table avec CREATE TABLE
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VI — Créer et structurer une base
  - index.md
---

## Le minimum à savoir

### La structure de base

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

### Anatomie d’une définition de colonne

```
nom_colonne    TYPE       contrainte1 contrainte2 ...
─────────────  ─────────  ───────────────────────
first_name     TEXT       NOT NULL
id             INTEGER    PRIMARY KEY
email          TEXT       UNIQUE
status         TEXT       DEFAULT 'borrowed'
```


### Supprimer une table : `DROP TABLE`

```sql
DROP TABLE readers;        -- ❌ ❌ ❌ supprime DÉFINITIVEMENT la table et toutes ses données
```


> **⚠️ Extrême prudence avec `DROP TABLE`**. Contrairement à `DELETE`, qui ne supprime que les lignes, `DROP TABLE` détruit la structure elle-même. Sans sauvegarde, c’est irréversible.

### Modifier une table existante : `ALTER TABLE`

```sql
ALTER TABLE readers ADD COLUMN birth_date TEXT;        -- ajouter une colonne
ALTER TABLE readers RENAME TO members;                  -- renommer la table
```


> **Note :** SQLite a longtemps eu un support limité de `ALTER TABLE` (pas de `DROP COLUMN` jusqu’en SQLite 3.35). C’est l’un des points où les SGBD diffèrent. Pour ce cours, on se concentre sur `CREATE TABLE`.

### `IF NOT EXISTS` : créer seulement si la table n’existe pas

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

## ❌ Erreur classique

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


## ✅ Tu sais maintenant…

- Créer une table avec `CREATE TABLE nom (colonne TYPE contrainte, ...)`
- Supprimer une table avec `DROP TABLE` (irréversible !)
- `IF NOT EXISTS` pour les scripts d’initialisation
- `ALTER TABLE` pour modifier (de manière limitée en SQLite)

-----
