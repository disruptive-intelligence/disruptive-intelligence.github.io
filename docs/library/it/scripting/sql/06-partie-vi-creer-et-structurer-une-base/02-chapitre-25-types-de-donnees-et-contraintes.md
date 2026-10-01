---
title: Chapitre 25 — Types de données et contraintes
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VI — Créer et structurer une base
  - index.md
---

## Le minimum à savoir

### Les types de données SQLite

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

### Les contraintes essentielles

|Contrainte                               |Effet                                      |
|-----------------------------------------|-------------------------------------------|
|`PRIMARY KEY`                            |Identifiant unique de la table             |
|`NOT NULL`                               |Valeur obligatoire (pas de NULL)           |
|`UNIQUE`                                 |Toutes les valeurs doivent être différentes|
|`DEFAULT valeur`                         |Valeur par défaut si non fournie           |
|`CHECK (condition)`                      |Règle de validation personnalisée          |
|`FOREIGN KEY (col) REFERENCES table(col)`|Clé étrangère vers une autre table         |

### Exemple complet

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

### Pourquoi les contraintes sont cruciales

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

## Très utile en pratique

### `PRIMARY KEY` composite

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

## ❌ Erreur classique

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


## 💡 Exercices

1. Crée une table `categories_v2` avec `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL UNIQUE`, et `description TEXT`.
1. Crée une table `subscriptions` (abonnements payants des lecteurs) avec `id`, `reader_id` (FK vers `readers`), `start_date`, `end_date`, `subscription_type` (avec `CHECK` sur 3 valeurs autorisées : ‘monthly’, ‘yearly’, ‘lifetime’).
1. Insère deux lignes valides dans `subscriptions`. Tente une 3e avec un type non autorisé — observe l’erreur.

## ✅ Tu sais maintenant…

- Les types SQLite : `INTEGER`, `REAL`, `TEXT`, `BLOB`
- Les contraintes : `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY`
- Les contraintes garantissent la qualité des données dès l’écriture
- `PRIMARY KEY` composite pour les tables d’association

-----
