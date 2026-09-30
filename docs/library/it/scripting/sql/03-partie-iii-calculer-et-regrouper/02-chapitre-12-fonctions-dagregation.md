---
title: Chapitre 12 — Fonctions d’agrégation
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie III — Calculer ET regrouper
  - index.md
---

## Le minimum à savoir

### Le concept : compter, additionner, calculer une moyenne

Les **fonctions d’agrégation** réduisent plusieurs lignes en une seule valeur. Les 5 essentielles :

|Fonction        |Effet                                          |
|----------------|-----------------------------------------------|
|`COUNT(*)`      |Compte les lignes                              |
|`COUNT(colonne)`|Compte les valeurs **non nulles** d’une colonne|
|`SUM(colonne)`  |Additionne les valeurs                         |
|`AVG(colonne)`  |Moyenne                                        |
|`MIN(colonne)`  |Plus petite valeur                             |
|`MAX(colonne)`  |Plus grande valeur                             |

### Compter

```sql
-- Combien de lecteurs au total ?
SELECT COUNT(*) FROM readers;
-- → 15

-- Combien de lecteurs ont un email renseigné ?
SELECT COUNT(email) FROM readers;
-- → 14 (un lecteur a NULL dans email)
```


> **À retenir :** `COUNT(*)` compte **toutes les lignes**. `COUNT(colonne)` compte **uniquement les lignes où la colonne n’est pas NULL**. Cette distinction est l’une des subtilités les plus importantes du SQL.

### Additionner et moyenner

```sql
-- Année moyenne de publication
SELECT AVG(publication_year) FROM books;
-- → ~1973.5

-- Année du livre le plus ancien et du plus récent
SELECT MIN(publication_year), MAX(publication_year) FROM books;
-- → 1831, 2018
```


### Combiner plusieurs agrégations

```sql
SELECT
    COUNT(*) AS nb_livres,
    MIN(publication_year) AS plus_ancien,
    MAX(publication_year) AS plus_recent,
    AVG(publication_year) AS annee_moyenne
FROM books;
```


→ Une ligne, quatre statistiques.

### Compter avec condition

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

## Très utile en pratique

### Arrondir une moyenne

```sql
SELECT ROUND(AVG(publication_year), 0) AS annee_moyenne FROM books;
-- → 1974 (au lieu de 1973.5)
```


### `COUNT(DISTINCT col)`

Compter les valeurs **uniques** d’une colonne :

```sql
SELECT COUNT(DISTINCT city) FROM readers;
-- → 5 (le nombre de villes distinctes)
```


C’est très utile pour des analyses : combien de catégories, combien d’utilisateurs uniques, combien de pays différents…

## ❌ Erreur classique

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


## 💡 Exercices

1. Combien de livres dans la table `books` ?
1. Quel est le livre le plus ancien (année) et le plus récent ?
1. Combien de catégories distinctes existent dans `books` ?
1. Quelle est l’année moyenne de publication ? Arrondis-la.

## ✅ Tu sais maintenant…

- Les 5 agrégations : `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- La différence cruciale : `COUNT(*)` (toutes les lignes) vs `COUNT(colonne)` (sans les NULL)
- `COUNT(DISTINCT col)` pour les valeurs uniques
- Combiner agrégations et `WHERE` pour des stats filtrées

-----
