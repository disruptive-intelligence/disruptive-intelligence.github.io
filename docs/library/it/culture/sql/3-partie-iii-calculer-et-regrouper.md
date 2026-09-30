---
title: PARTIE III — CALCULER ET REGROUPER
source: IT/Culture/SQL.md
note: SQL
chapter: 3
chapters: 8
---

-----


## Chapitre 11 — Fonctions et calculs simples

### Le minimum à savoir

#### Calculs dans `SELECT`

Tu peux faire des calculs directement dans la sélection :

```sql
SELECT title, publication_year, 2026 - publication_year AS age_du_livre
FROM books;
```

Le résultat ajoute une colonne calculée `age_du_livre`. Cette colonne n’existe pas dans la table — elle est calculée à la volée pour le résultat.

#### Concaténation de texte

En SQLite (et PostgreSQL), on concatène avec `||` :

```sql
SELECT first_name || ' ' || last_name AS full_name
FROM readers;
```

→ `'Alice' || ' ' || 'Martin'` = `'Alice Martin'`

> **Note dialecte :** MySQL utilise `CONCAT(a, b, c)` au lieu de `||`. SQLite et PostgreSQL utilisent `||`. C’est l’un des points où les dialectes diffèrent.

#### Fonctions de texte essentielles

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

#### Fonctions de date (SQLite)

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

### Très utile en pratique

#### Combiner texte et calculs

```sql
SELECT first_name || ' ' || last_name || ' (inscrit en ' || strftime('%Y', registration_date) || ')' AS description
FROM readers;
-- → 'Alice Martin (inscrit en 2023)', 'Karim Bernard (inscrit en 2023)', ...
```

C’est le même principe qu’une f-string Python, en SQL.

### ❌ Erreur classique

```sql
-- Confondre la chaîne 'NULL' et la valeur NULL
SELECT 'a' || NULL || 'b';      -- → NULL (toute opération avec NULL donne NULL)
-- Pour gérer ça, utilise COALESCE :
SELECT 'a' || COALESCE(NULL, '') || 'b';   -- → 'ab' (COALESCE remplace NULL par '')

-- Utiliser CONCAT en SQLite
SELECT CONCAT(first_name, ' ', last_name) FROM readers;   -- ❌ pas en SQLite/PostgreSQL
SELECT first_name || ' ' || last_name FROM readers;        -- ✅
```

### 💡 Exercices

1. Affiche le nom complet de chaque lecteur (prénom + espace + nom).
1. Affiche les titres des livres en majuscules.
1. Affiche, pour chaque emprunt, l’année de l’emprunt extraite avec `strftime`.

### ✅ Tu sais maintenant…

- Faire des calculs dans `SELECT` (`2026 - year`, etc.)
- Concaténer du texte avec `||` (SQLite/PostgreSQL)
- Les fonctions de texte : `UPPER`, `LOWER`, `LENGTH`, `TRIM`, `SUBSTR`
- Les fonctions de date SQLite : `DATE('now')`, `strftime()`, `julianday()`
- `COALESCE(x, valeur_par_défaut)` pour gérer les `NULL`

-----


## Chapitre 12 — Fonctions d’agrégation

### Le minimum à savoir

#### Le concept : compter, additionner, calculer une moyenne

Les **fonctions d’agrégation** réduisent plusieurs lignes en une seule valeur. Les 5 essentielles :

|Fonction        |Effet                                          |
|----------------|-----------------------------------------------|
|`COUNT(*)`      |Compte les lignes                              |
|`COUNT(colonne)`|Compte les valeurs **non nulles** d’une colonne|
|`SUM(colonne)`  |Additionne les valeurs                         |
|`AVG(colonne)`  |Moyenne                                        |
|`MIN(colonne)`  |Plus petite valeur                             |
|`MAX(colonne)`  |Plus grande valeur                             |

#### Compter

```sql
-- Combien de lecteurs au total ?
SELECT COUNT(*) FROM readers;
-- → 15

-- Combien de lecteurs ont un email renseigné ?
SELECT COUNT(email) FROM readers;
-- → 14 (un lecteur a NULL dans email)
```

> **À retenir :** `COUNT(*)` compte **toutes les lignes**. `COUNT(colonne)` compte **uniquement les lignes où la colonne n’est pas NULL**. Cette distinction est l’une des subtilités les plus importantes du SQL.

#### Additionner et moyenner

```sql
-- Année moyenne de publication
SELECT AVG(publication_year) FROM books;
-- → ~1973.5

-- Année du livre le plus ancien et du plus récent
SELECT MIN(publication_year), MAX(publication_year) FROM books;
-- → 1831, 2018
```

#### Combiner plusieurs agrégations

```sql
SELECT
    COUNT(*) AS nb_livres,
    MIN(publication_year) AS plus_ancien,
    MAX(publication_year) AS plus_recent,
    AVG(publication_year) AS annee_moyenne
FROM books;
```

→ Une ligne, quatre statistiques.

#### Compter avec condition

Tu peux combiner `COUNT(*)` et `WHERE` :

```sql
-- Combien de lecteurs habitent à Paris ?
SELECT COUNT(*) FROM readers WHERE city = 'Paris';
-- → 5
```

> **📋 FIL ROUGE — Épisode 11**
> 
> La directrice prépare le rapport annuel : “Donne-moi les chiffres clés.” Nora :
> 
> ```sql
> SELECT
>     COUNT(*) AS nb_lecteurs,
>     COUNT(email) AS nb_avec_email,
>     COUNT(phone) AS nb_avec_phone
> FROM readers;
> ```
> 
> Résultat : 15 lecteurs, 14 ont un email, 11 ont un téléphone. Sans `COUNT(colonne)` qui exclut les `NULL`, elle aurait dû faire trois requêtes séparées.

### Très utile en pratique

#### Arrondir une moyenne

```sql
SELECT ROUND(AVG(publication_year), 0) AS annee_moyenne FROM books;
-- → 1974 (au lieu de 1973.5)
```

#### `COUNT(DISTINCT col)`

Compter les valeurs **uniques** d’une colonne :

```sql
SELECT COUNT(DISTINCT city) FROM readers;
-- → 5 (le nombre de villes distinctes)
```

C’est très utile pour des analyses : combien de catégories, combien d’utilisateurs uniques, combien de pays différents…

### ❌ Erreur classique

```sql
-- Confondre COUNT(*) et COUNT(colonne)
SELECT COUNT(*) FROM readers;        -- 15 (toutes les lignes)
SELECT COUNT(email) FROM readers;    -- 14 (sans les NULL)
SELECT COUNT(phone) FROM readers;    -- 11 (sans les NULL)

-- Mélanger agrégation et colonne brute SANS GROUP BY
SELECT first_name, COUNT(*) FROM readers;    -- ❌ erreur ou résultat absurde
-- → on verra GROUP BY au prochain chapitre

-- Compter avec MAX au lieu de COUNT
SELECT MAX(id) FROM readers;
-- → renvoie l'id le plus grand, pas le nombre de lecteurs !
```

### 💡 Exercices

1. Combien de livres dans la table `books` ?
1. Quel est le livre le plus ancien (année) et le plus récent ?
1. Combien de catégories distinctes existent dans `books` ?
1. Quelle est l’année moyenne de publication ? Arrondis-la.

### ✅ Tu sais maintenant…

- Les 5 agrégations : `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- La différence cruciale : `COUNT(*)` (toutes les lignes) vs `COUNT(colonne)` (sans les NULL)
- `COUNT(DISTINCT col)` pour les valeurs uniques
- Combiner agrégations et `WHERE` pour des stats filtrées

-----


## Chapitre 13 — Regrouper avec GROUP BY

### Le minimum à savoir

#### Le besoin : statistiques par catégorie

Au chapitre précédent, on a fait `COUNT(*)` sur toute la table. Mais souvent, tu veux des **statistiques par groupe** : combien de livres par catégorie ? Combien d’emprunts par lecteur ?

C’est le rôle de `GROUP BY`.

#### La structure : `GROUP BY` + agrégation

```sql
SELECT category_id, COUNT(*) AS nb_livres
FROM books
GROUP BY category_id;
```

Résultat (exemple) :

|category_id |nb_livres|
|------------|---------|
|1 (Roman)   |6        |
|2 (Histoire)|2        |
|4 (BD)      |1        |
|5 (Jeunesse)|2        |
|6 (Polar)   |4        |

→ Une ligne par catégorie, avec le nombre de livres dans chacune.

#### La règle d’or

Avec `GROUP BY`, **chaque colonne du `SELECT` doit être** :

- soit dans le `GROUP BY`,
- soit utilisée dans une fonction d’agrégation (`COUNT`, `SUM`, etc.).

Cette requête est correcte :

```sql
SELECT category_id, COUNT(*)
FROM books
GROUP BY category_id;
```

Celle-ci ne l’est pas (`title` n’est ni groupée ni agrégée) :

```sql
SELECT title, category_id, COUNT(*)    -- ❌
FROM books
GROUP BY category_id;
```

> **À retenir :** quand tu groupes, tu ne peux afficher que ce qui est constant dans le groupe (les colonnes du `GROUP BY`) ou un calcul sur le groupe (une agrégation). Sinon, ça n’a pas de sens — quelle valeur de `title` afficher pour la catégorie qui en contient 6 ?

#### Combiner plusieurs agrégations

```sql
SELECT category_id,
       COUNT(*) AS nb_livres,
       MIN(publication_year) AS plus_ancien,
       MAX(publication_year) AS plus_recent
FROM books
GROUP BY category_id;
```

Pour chaque catégorie : le nombre, le plus ancien, le plus récent.

#### Grouper sur plusieurs colonnes

```sql
-- Nombre d'emprunts par lecteur ET par statut
SELECT reader_id, status, COUNT(*) AS nb
FROM loans
GROUP BY reader_id, status;
```

Tu obtiens une ligne par couple (reader_id, status). C’est utile pour des analyses croisées.

> **📋 FIL ROUGE — Épisode 12**
> 
> La directrice : “Combien de livres a-t-on dans chaque catégorie ? On va voir si on est équilibrés.” Nora :
> 
> ```sql
> SELECT category_id, COUNT(*) AS nb_livres
> FROM books
> GROUP BY category_id
> ORDER BY nb_livres DESC;
> ```
> 
> 6 romans, 4 polars, 2 histoires, 2 jeunesse, 1 BD. La directrice constate qu’il manque cruellement de BD et de livres jeunesse — un nouvel achat est planifié.

### Très utile en pratique

#### Grouper + filtrer + trier

Tu peux combiner `WHERE`, `GROUP BY` et `ORDER BY` :

```sql
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
WHERE loan_date >= '2025-01-01'         -- filtre AVANT le groupage
GROUP BY reader_id
ORDER BY nb_emprunts DESC;              -- trier les groupes
```

L’ordre est : `WHERE` filtre les lignes, puis `GROUP BY` regroupe ce qui reste, puis `ORDER BY` trie le résultat.

### ❌ Erreur classique

```sql
-- Mettre une colonne non-groupée dans le SELECT
SELECT first_name, COUNT(*)
FROM readers
GROUP BY city;     -- ❌ first_name n'est ni groupé ni agrégé
                   --    SQLite renvoie une valeur arbitraire (silencieusement)
                   --    PostgreSQL renvoie une erreur claire

-- Oublier le GROUP BY
SELECT category_id, COUNT(*) FROM books;     -- ❌ résultat bizarre
SELECT category_id, COUNT(*) FROM books GROUP BY category_id;   -- ✅
```

### 💡 Exercices

1. Combien de lecteurs habitent dans chaque ville (`city`) ?
1. Combien d’emprunts pour chaque lecteur (`reader_id`) ? Trie par nombre décroissant.
1. Pour chaque catégorie, combien de livres et quelle année moyenne de publication ?

### ✅ Tu sais maintenant…

- `GROUP BY col` regroupe les lignes par la valeur de `col`
- Chaque colonne du `SELECT` doit être soit dans `GROUP BY`, soit dans une agrégation
- Combiner `GROUP BY` avec `WHERE` (avant) et `ORDER BY` (après)
- Grouper sur plusieurs colonnes pour des analyses croisées

-----


## Chapitre 14 — Filtrer les groupes avec HAVING

### Le minimum à savoir

#### Le problème : filtrer après agrégation

`WHERE` filtre les **lignes** avant le regroupement. Mais que faire si tu veux filtrer les **groupes** après calcul ?

Exemple : “Quels lecteurs ont emprunté 3 livres ou plus ?”

Tu ne peux pas écrire `WHERE COUNT(*) >= 3` — `COUNT(*)` n’existe qu’après agrégation. Il faut une autre clause : `HAVING`.

#### `WHERE` vs `HAVING`

```sql
-- ❌ Ne marche pas : COUNT(*) n'est pas connu au moment du WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3
GROUP BY reader_id;

-- ✅ Correct : HAVING filtre les groupes après agrégation
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;
```

> **À retenir :** `WHERE` filtre les **lignes** (avant `GROUP BY`). `HAVING` filtre les **groupes** (après `GROUP BY`). Tu peux utiliser les deux dans la même requête — ils ne servent pas à la même chose.

#### L’exemple combiné

```sql
-- Lecteurs ayant eu plus de 2 emprunts en retard
SELECT reader_id, COUNT(*) AS nb_retards
FROM loans
WHERE status = 'late'                  -- ← filtre les lignes "en retard"
GROUP BY reader_id
HAVING COUNT(*) >= 2;                  -- ← garde les lecteurs avec ≥ 2 retards
```

L’ordre logique :

1. `WHERE status = 'late'` → on ne garde que les emprunts en retard
1. `GROUP BY reader_id` → on regroupe par lecteur
1. `HAVING COUNT(*) >= 2` → on garde les groupes ayant au moins 2 retards

> **📋 FIL ROUGE — Épisode 13**
> 
> La directrice : “Identifie les lecteurs qui ont plus d’un retard. On va leur envoyer un rappel.” Nora :
> 
> ```sql
> SELECT reader_id, COUNT(*) AS nb_retards
> FROM loans
> WHERE status = 'late'
> GROUP BY reader_id
> HAVING COUNT(*) >= 2;
> ```
> 
> Elle identifie les “récidivistes”. Sans `HAVING`, elle aurait obtenu tous les lecteurs avec leur nombre de retards (y compris ceux qui en ont 1) — `HAVING` lui permet de cibler spécifiquement les problématiques.

### Très utile en pratique

#### Le tableau récapitulatif

|Clause  |Filtre quoi ?       |Quand ?         |Peut utiliser des agrégations ?|
|--------|--------------------|----------------|-------------------------------|
|`WHERE` |Lignes individuelles|Avant `GROUP BY`|❌ Non                          |
|`HAVING`|Groupes             |Après `GROUP BY`|✅ Oui                          |

#### Sans `GROUP BY` ?

`HAVING` peut techniquement s’utiliser sans `GROUP BY` (la table est alors traitée comme un seul groupe), mais c’est rare. Le cas standard est `GROUP BY ... HAVING ...`.

### ❌ Erreur classique

```sql
-- Mettre une condition d'agrégation dans WHERE
SELECT reader_id, COUNT(*)
FROM loans
WHERE COUNT(*) >= 3      -- ❌ COUNT(*) n'existe pas à ce stade
GROUP BY reader_id;

-- ✅ Correct
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING COUNT(*) >= 3;

-- Mettre une condition simple dans HAVING (techniquement possible mais inefficace)
SELECT reader_id, COUNT(*)
FROM loans
GROUP BY reader_id
HAVING reader_id = 1;     -- ⚠️ ça marche, mais c'est plus efficace dans WHERE

-- ✅ Plus efficace
SELECT reader_id, COUNT(*)
FROM loans
WHERE reader_id = 1
GROUP BY reader_id;
```

### 💡 Exercices

1. Quelles villes ont au moins 3 lecteurs ?
1. Quels livres ont été empruntés au moins 2 fois ?
1. Quels lecteurs ont au moins 2 emprunts encore en cours (`status = 'borrowed'`) ?

### ✅ Tu sais maintenant…

- `WHERE` filtre les lignes (avant `GROUP BY`)
- `HAVING` filtre les groupes (après `GROUP BY`)
- `HAVING` peut utiliser des fonctions d’agrégation, `WHERE` non
- Combiner les deux dans une même requête est non seulement possible mais recommandé pour les conditions appropriées

-----
