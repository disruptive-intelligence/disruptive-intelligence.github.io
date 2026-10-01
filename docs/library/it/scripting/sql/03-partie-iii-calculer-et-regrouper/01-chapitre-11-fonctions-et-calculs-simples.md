---
title: Chapitre 11 — Fonctions et calculs simples
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie III — Calculer et regrouper
  - index.md
---

## Le minimum à savoir

### Calculs dans `SELECT`

Tu peux faire des calculs directement dans la sélection :

```sql
SELECT title, publication_year, 2026 - publication_year AS age_du_livre
FROM books;
```


Le résultat ajoute une colonne calculée `age_du_livre`. Cette colonne n’existe pas dans la table — elle est calculée à la volée pour le résultat.

### Concaténation de texte

En SQLite (et PostgreSQL), on concatène avec `||` :

```sql
SELECT first_name || ' ' || last_name AS full_name
FROM readers;
```


→ `'Alice' || ' ' || 'Martin'` = `'Alice Martin'`

> **Note dialecte :** MySQL utilise `CONCAT(a, b, c)` au lieu de `||`. SQLite et PostgreSQL utilisent `||`. C’est l’un des points où les dialectes diffèrent.

### Fonctions de texte essentielles

|Fonction             |Effet               |Exemple                            |
|---------------------|--------------------|-----------------------------------|
|`UPPER(s)`           |Majuscules          |`UPPER('alice')` → `'ALICE'`       |
|`LOWER(s)`           |Minuscules          |`LOWER('ALICE')` → `'alice'`       |
|`LENGTH(s)`          |Longueur            |`LENGTH('Alice')` → `5`            |
|`TRIM(s)`            |Supprime espaces    |`TRIM('  abc  ')` → `'abc'`        |
|`SUBSTR(s, début, n)`|Extrait n caractères|`SUBSTR('Bonjour', 1, 3)` → `'Bon'`|

```sql
SELECT UPPER(title) AS titre_majuscules, LENGTH(title) AS longueur
FROM books;
```


### Fonctions de date (SQLite)

SQLite stocke les dates comme du texte au format `'YYYY-MM-DD'`. Quelques fonctions utiles :

```sql
-- Date du jour
SELECT DATE('now');                        -- → '2026-05-03'

-- Extraire une partie d'une date
SELECT strftime('%Y', loan_date) AS annee FROM loans;     -- → '2025', '2025', ...
SELECT strftime('%m', loan_date) AS mois  FROM loans;     -- → '01', '02', ...
SELECT strftime('%Y-%m', loan_date) AS annee_mois FROM loans; -- → '2025-01', ...

-- Nombre de jours depuis une date
SELECT julianday('now') - julianday(loan_date) AS jours_depuis_emprunt
FROM loans;
```


> **Note dialecte :** chaque SGBD a ses propres fonctions de date. PostgreSQL utilise `EXTRACT(YEAR FROM date)`, MySQL utilise `YEAR(date)`. SQLite utilise `strftime()`. Quand tu changes de SGBD, c’est l’un des points à adapter.

> **📋 FIL ROUGE — Épisode 10**
> 
> La directrice : “Affiche-moi le nom complet de chaque lecteur en majuscules pour les badges.” Nora :
> 
> ```sql
> SELECT UPPER(first_name || ' ' || last_name) AS nom_badge
> FROM readers
> ORDER BY last_name;
> ```
> 
> Génial — la concaténation et `UPPER()` font tout en une seule requête.

## Très utile en pratique

### Combiner texte et calculs

```sql
SELECT first_name || ' ' || last_name || ' (inscrit en ' || strftime('%Y', registration_date) || ')' AS description
FROM readers;
-- → 'Alice Martin (inscrit en 2023)', 'Karim Bernard (inscrit en 2023)', ...
```


C’est le même principe qu’une f-string Python, en SQL.

## ❌ Erreur classique

```sql
-- Confondre la chaîne 'NULL' et la valeur NULL
SELECT 'a' || NULL || 'b';      -- → NULL (toute opération avec NULL donne NULL)
-- Pour gérer ça, utilise COALESCE :
SELECT 'a' || COALESCE(NULL, '') || 'b';   -- → 'ab' (COALESCE remplace NULL par '')

-- Utiliser CONCAT en SQLite
SELECT CONCAT(first_name, ' ', last_name) FROM readers;   -- ❌ pas en SQLite/PostgreSQL
SELECT first_name || ' ' || last_name FROM readers;        -- ✅
```


## 💡 Exercices

1. Affiche le nom complet de chaque lecteur (prénom + espace + nom).
1. Affiche les titres des livres en majuscules.
1. Affiche, pour chaque emprunt, l’année de l’emprunt extraite avec `strftime`.

## ✅ Tu sais maintenant…

- Faire des calculs dans `SELECT` (`2026 - year`, etc.)
- Concaténer du texte avec `||` (SQLite/PostgreSQL)
- Les fonctions de texte : `UPPER`, `LOWER`, `LENGTH`, `TRIM`, `SUBSTR`
- Les fonctions de date SQLite : `DATE('now')`, `strftime()`, `julianday()`
- `COALESCE(x, valeur_par_défaut)` pour gérer les `NULL`

-----
