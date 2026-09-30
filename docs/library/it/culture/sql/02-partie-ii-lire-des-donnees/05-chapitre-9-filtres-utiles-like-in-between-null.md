---
title: 'Chapitre 9 — Filtres utiles : LIKE, IN, BETWEEN, NULL'
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### Recherche par motif avec `LIKE`

`LIKE` permet de chercher un motif dans du texte. Deux caractères spéciaux :

|Caractère|Signification                                      |
|---------|---------------------------------------------------|
|`%`      |N’importe quelle séquence de caractères (même vide)|
|`_`      |Exactement un caractère                            |

Exemples :

```sql
-- Tous les livres dont le titre contient "Harry"
SELECT * FROM books WHERE title LIKE '%Harry%';

-- Tous les emails se terminant par "@example.com"
SELECT * FROM readers WHERE email LIKE '%@example.com';

-- Tous les noms commençant par "Mar"
SELECT * FROM readers WHERE last_name LIKE 'Mar%';

-- Mots de 4 lettres commençant par "L"
SELECT * FROM books WHERE title LIKE 'L___';
```


> **Note :** par défaut, `LIKE` est **insensible à la casse** dans SQLite (`'PARIS'` = `'Paris'`). Dans PostgreSQL, c’est sensible — utilise `ILIKE` pour insensibiliser.

### Liste de valeurs avec `IN`

Plus propre que des `OR` à répétition :

```sql
-- Avec OR (verbeux)
SELECT * FROM readers
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille';

-- Avec IN (concis)
SELECT * FROM readers
WHERE city IN ('Paris', 'Lyon', 'Marseille');
```


L’inverse existe aussi : `NOT IN` :

```sql
SELECT * FROM readers
WHERE city NOT IN ('Paris', 'Lyon');
-- → toutes les villes SAUF Paris et Lyon
```


### Plage de valeurs avec `BETWEEN`

```sql
-- Livres publiés entre 1990 et 2000 (inclus)
SELECT * FROM books
WHERE publication_year BETWEEN 1990 AND 2000;
```


`BETWEEN a AND b` est **inclusif** des deux bornes. C’est équivalent à :

```sql
WHERE publication_year >= 1990 AND publication_year <= 2000
```


### Le cas particulier : `NULL`

`NULL` représente l’**absence de valeur**. Ce n’est ni `0`, ni la chaîne vide `''` — c’est “rien”.

**Important :** on ne peut **pas** comparer `NULL` avec `=` :

```sql
SELECT * FROM readers WHERE phone = NULL;        -- ❌ ne renvoie jamais rien
SELECT * FROM readers WHERE phone IS NULL;       -- ✅ correct

SELECT * FROM readers WHERE phone IS NOT NULL;   -- ✅ ceux qui ont un téléphone
```


> **À retenir :** `NULL` n’est égal à rien — pas même à lui-même. Utilise toujours `IS NULL` ou `IS NOT NULL`. C’est l’une des erreurs les plus fréquentes en SQL.

> **📋 FIL ROUGE — Épisode 8**
> 
> La directrice : “Combien de lecteurs n’ont pas de téléphone enregistré ? Il faut leur demander à leur prochaine visite.” Nora :
> 
> ```sql
> SELECT first_name, last_name FROM readers WHERE phone IS NULL;
> ```
> 
> 4 lecteurs. Elle imprime la liste. Si elle avait écrit `WHERE phone = NULL`, elle aurait obtenu 0 résultats — et conclu à tort que tous les lecteurs ont un téléphone.

## Très utile en pratique

### `LIKE` avec recherche multilingue

`LIKE '%harry%'` est insensible à la casse en SQLite par défaut, mais peut ne pas trouver `'Harry'` dans certains environnements. Pour être sûr :

```sql
SELECT * FROM books WHERE LOWER(title) LIKE '%harry%';
```


`LOWER()` met le texte en minuscules — la comparaison devient garantie insensible à la casse.

### `NULL` et opérations

Toute opération impliquant `NULL` produit `NULL` :

```sql
SELECT 5 + NULL;    -- → NULL
SELECT 'a' || NULL; -- → NULL
```


C’est pour ça que `WHERE col = NULL` ne marche pas : `col = NULL` produit `NULL`, pas `TRUE` — et `WHERE` ne garde que les `TRUE`.

## ❌ Erreur classique

```sql
-- Comparer NULL avec =
WHERE phone = NULL;          -- ❌ ne renvoie rien
WHERE phone IS NULL;         -- ✅

-- Confondre chaîne vide et NULL
WHERE email = '';            -- ne trouve QUE les emails vides (chaîne de longueur 0)
WHERE email IS NULL;         -- trouve les emails non renseignés (rien du tout)

-- Les deux peuvent coexister dans une base mal nettoyée :
-- email = '' (vide) ≠ email IS NULL (absent)
```


## 💡 Exercices

1. Affiche les livres dont le titre contient “Potter”.
1. Affiche les lecteurs habitant à Paris, Lyon **ou** Bordeaux (avec `IN`).
1. Affiche les livres publiés entre 1900 et 1950 (avec `BETWEEN`).
1. Affiche les lecteurs qui n’ont pas d’email.

## ✅ Tu sais maintenant…

- `LIKE '%motif%'` pour chercher un motif dans du texte
- `IN (...)` pour une liste de valeurs
- `BETWEEN a AND b` pour une plage (inclusive)
- `IS NULL` / `IS NOT NULL` pour les valeurs absentes
- `NULL` ≠ chaîne vide `''` ≠ zéro `0`

-----
