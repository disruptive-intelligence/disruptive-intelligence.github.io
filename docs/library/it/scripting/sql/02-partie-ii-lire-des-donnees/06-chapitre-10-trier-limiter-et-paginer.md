---
title: Chapitre 10 — Trier, limiter et paginer
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### Trier avec `ORDER BY`

Par défaut, SQL ne garantit **aucun ordre** dans les résultats. Pour trier, utilise `ORDER BY` :

```sql
-- Par ordre alphabétique sur le nom
SELECT * FROM readers ORDER BY last_name;

-- Par année de publication, du plus récent au plus ancien
SELECT * FROM books ORDER BY publication_year DESC;
```


|Mot-clé        |Effet                              |
|---------------|-----------------------------------|
|(rien) ou `ASC`|Croissant (ascending) — A→Z, 0→9   |
|`DESC`         |Décroissant (descending) — Z→A, 9→0|

### Trier sur plusieurs colonnes

Quand plusieurs lignes ont la même valeur sur la première colonne, on trie par la suivante :

```sql
-- D'abord par catégorie (alphabétique), puis par année (du plus récent)
SELECT title, category_id, publication_year
FROM books
ORDER BY category_id ASC, publication_year DESC;
```


### Limiter le nombre de résultats avec `LIMIT`

Pour ne récupérer que les N premières lignes :

```sql
-- Les 5 lecteurs inscrits le plus récemment
SELECT * FROM readers
ORDER BY registration_date DESC
LIMIT 5;
```


> **À retenir :** `LIMIT` se met **toujours à la fin** de la requête, après `ORDER BY`. Sans `ORDER BY`, `LIMIT 5` te donne 5 lignes “au hasard” — pas forcément les plus récentes.

### Paginer avec `LIMIT` + `OFFSET`

`OFFSET` saute un nombre de lignes avant de commencer :

```sql
-- Lignes 11 à 20 (saut de 10, prend 10)
SELECT * FROM readers
ORDER BY id
LIMIT 10 OFFSET 10;
```


C’est le mécanisme classique de la pagination dans une application web :

- Page 1 : `LIMIT 10 OFFSET 0`
- Page 2 : `LIMIT 10 OFFSET 10`
- Page 3 : `LIMIT 10 OFFSET 20`
- Page N : `LIMIT 10 OFFSET (N-1) * 10`

> **📋 FIL ROUGE — Épisode 9**
> 
> La directrice : “Donne-moi les 10 derniers lecteurs inscrits, on va leur envoyer un mot de bienvenue.” Nora :
> 
> ```sql
> SELECT first_name, last_name, registration_date
> FROM readers
> ORDER BY registration_date DESC
> LIMIT 10;
> ```
> 
> Parfait. Le `DESC` fait remonter les plus récents en premier, le `LIMIT 10` coupe le résultat aux 10 premiers.

## Très utile en pratique

### Trier par plusieurs critères avec sens différent

```sql
-- Par catégorie alphabétique, puis par année DÉCROISSANTE dans chaque catégorie
ORDER BY category_id ASC, publication_year DESC;
```


C’est très utile pour des rapports structurés — d’abord regroupé, puis trié finement à l’intérieur.

### Trier sur un alias

Tu peux trier sur le nom donné par `AS` :

```sql
SELECT title, 2026 - publication_year AS age_du_livre
FROM books
ORDER BY age_du_livre DESC;
```


## ❌ Erreur classique

```sql
-- LIMIT sans ORDER BY
SELECT * FROM readers LIMIT 5;
-- ❌ Te donne 5 lignes "quelconques" — pas forcément les premières/dernières
SELECT * FROM readers ORDER BY id LIMIT 5;   -- ✅ explicite l'ordre

-- ORDER BY après LIMIT
SELECT * FROM readers LIMIT 5 ORDER BY id;   -- ❌ syntaxe incorrecte
SELECT * FROM readers ORDER BY id LIMIT 5;   -- ✅ ORDER BY avant LIMIT

-- Croire que tri ASC = ordre par défaut partout
-- → C'est vrai en pratique, mais sans ORDER BY explicite, le moteur n'a aucune obligation
```


## 💡 Exercices

1. Affiche tous les livres triés par année du plus ancien au plus récent.
1. Affiche les 3 livres les plus récents.
1. Affiche les 5 lecteurs habitant à Paris, par ordre alphabétique sur le nom.
1. Affiche les pages 2 et 3 (10 lecteurs par page) triés par date d’inscription.

## ✅ Tu sais maintenant…

- Trier avec `ORDER BY col ASC` ou `ORDER BY col DESC`
- Trier sur plusieurs colonnes
- Limiter le nombre de résultats avec `LIMIT`
- Paginer avec `LIMIT` + `OFFSET`
- Toujours combiner `LIMIT` avec un `ORDER BY` explicite

-----
