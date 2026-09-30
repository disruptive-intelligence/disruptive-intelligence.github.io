---
title: Chapitre 13 — Regrouper avec GROUP BY
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie III — Calculer ET regrouper
  - index.md
---

## Le minimum à savoir

### Le besoin : statistiques par catégorie

Au chapitre précédent, on a fait `COUNT(*)` sur toute la table. Mais souvent, tu veux des **statistiques par groupe** : combien de livres par catégorie ? Combien d’emprunts par lecteur ?

C’est le rôle de `GROUP BY`.

### La structure : `GROUP BY` + agrégation

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

### La règle d’or

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

### Combiner plusieurs agrégations

```sql
SELECT category_id,
       COUNT(*) AS nb_livres,
       MIN(publication_year) AS plus_ancien,
       MAX(publication_year) AS plus_recent
FROM books
GROUP BY category_id;
```


Pour chaque catégorie : le nombre, le plus ancien, le plus récent.

### Grouper sur plusieurs colonnes

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

## Très utile en pratique

### Grouper + filtrer + trier

Tu peux combiner `WHERE`, `GROUP BY` et `ORDER BY` :

```sql
SELECT reader_id, COUNT(*) AS nb_emprunts
FROM loans
WHERE loan_date >= '2025-01-01'         -- filtre AVANT le groupage
GROUP BY reader_id
ORDER BY nb_emprunts DESC;              -- trier les groupes
```


L’ordre est : `WHERE` filtre les lignes, puis `GROUP BY` regroupe ce qui reste, puis `ORDER BY` trie le résultat.

## ❌ Erreur classique

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


## 💡 Exercices

1. Combien de lecteurs habitent dans chaque ville (`city`) ?
1. Combien d’emprunts pour chaque lecteur (`reader_id`) ? Trie par nombre décroissant.
1. Pour chaque catégorie, combien de livres et quelle année moyenne de publication ?

## ✅ Tu sais maintenant…

- `GROUP BY col` regroupe les lignes par la valeur de `col`
- Chaque colonne du `SELECT` doit être soit dans `GROUP BY`, soit dans une agrégation
- Combiner `GROUP BY` avec `WHERE` (avant) et `ORDER BY` (après)
- Grouper sur plusieurs colonnes pour des analyses croisées

-----
