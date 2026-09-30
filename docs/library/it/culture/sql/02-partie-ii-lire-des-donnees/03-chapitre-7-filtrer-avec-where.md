---
title: Chapitre 7 — Filtrer avec WHERE
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### Le besoin : ne pas tout afficher

Souvent, tu ne veux pas **toutes** les lignes — seulement celles qui correspondent à un critère. C’est le rôle de `WHERE` :

```sql
SELECT *
FROM readers
WHERE city = 'Paris';
```


`WHERE` filtre les lignes : seules celles où `city` vaut `'Paris'` sont retournées.

### Les opérateurs de comparaison

|Opérateur   |Signification    |Exemple                   |
|------------|-----------------|--------------------------|
|`=`         |Égal             |`city = 'Paris'`          |
|`<>` ou `!=`|Différent        |`city <> 'Paris'`         |
|`<`         |Inférieur        |`publication_year < 2000` |
|`>`         |Supérieur        |`publication_year > 2000` |
|`<=`        |Inférieur ou égal|`publication_year <= 2000`|
|`>=`        |Supérieur ou égal|`publication_year >= 1990`|


> **Attention :** en SQL, l’égalité s’écrit avec **un seul** `=` (pas deux comme en Python ou JavaScript). Pour la différence, c’est `<>` (la forme standard) ou `!=` (acceptée par la plupart des SGBD).

### Texte vs nombre : guillemets ou pas ?

Le **texte** se met entre **guillemets simples** `'...'`. Les **nombres** s’écrivent **sans guillemets**.

```sql
SELECT * FROM readers WHERE city = 'Paris';            -- texte → quotes
SELECT * FROM books WHERE publication_year >= 2000;    -- nombre → pas de quotes
SELECT * FROM books WHERE id = 5;                      -- nombre → pas de quotes
```


> **Important :** SQL utilise les **guillemets simples** `'...'` pour le texte. Les guillemets doubles `"..."` ont une autre signification (noms d’identifiants) — ne les utilise pas pour du texte, ou tu auras des erreurs surprenantes.

### Les apostrophes dans le texte

Si ton texte contient une apostrophe, double-la :

```sql
SELECT * FROM books WHERE title = 'L''Étranger';
--                                  ↑↑
--                            apostrophe doublée
```


C’est la façon standard d’échapper une apostrophe en SQL.

> **📋 FIL ROUGE — Épisode 6**
> 
> La directrice demande : “Combien de lecteurs habitent à Paris ?”. Nora tape :
> 
> ```sql
> SELECT * FROM readers WHERE city = 'Paris';
> ```
> 
> Elle compte 5 lignes dans le résultat. Pour automatiser le compte, elle préfigure ce qu’elle apprendra au Ch.12 — `COUNT()`. Mais pour l’instant, voir la liste lui suffit.

## Très utile en pratique

### `WHERE` sur des nombres et des dates

```sql
-- Livres publiés au 21e siècle
SELECT * FROM books WHERE publication_year >= 2000;

-- Lecteurs inscrits depuis 2025
SELECT * FROM readers WHERE registration_date >= '2025-01-01';
```


> **Note SQLite :** SQLite stocke les dates comme du **texte** au format `'YYYY-MM-DD'`. Tant que tes dates respectent ce format, les comparaisons `<`, `>`, `=` fonctionnent comme avec des nombres.

### Filtrer sur la sortie de DB Browser

Quand tu cliques sur “Exécuter”, DB Browser affiche le résultat sous la requête. Si le résultat est long, fais défiler. Le bas de l’écran indique le nombre de lignes retournées — pratique pour vérifier qu’on a bien ce qu’on attend.

## ❌ Erreur classique

```sql
-- Utiliser == au lieu de =
SELECT * FROM readers WHERE city == 'Paris';   -- ❌ Pas standard
SELECT * FROM readers WHERE city = 'Paris';    -- ✅

-- Mettre des nombres entre quotes (ça marche, mais c'est mauvaise pratique)
SELECT * FROM books WHERE id = '5';            -- ⚠️ Fonctionne mais sale
SELECT * FROM books WHERE id = 5;              -- ✅

-- Oublier les quotes pour le texte
SELECT * FROM readers WHERE city = Paris;      -- ❌ "no such column: Paris"
SELECT * FROM readers WHERE city = 'Paris';    -- ✅

-- Utiliser des guillemets doubles pour le texte
SELECT * FROM readers WHERE city = "Paris";    -- ⚠️ peut donner des résultats inattendus
SELECT * FROM readers WHERE city = 'Paris';    -- ✅
```


## 💡 Exercices

1. Affiche les livres publiés avant 1950.
1. Affiche les lecteurs habitant à Lyon.
1. Affiche les emprunts dont le statut est `'late'`.

## ✅ Tu sais maintenant…

- Filtrer les lignes avec `WHERE`
- Les opérateurs : `=`, `<>`, `!=`, `<`, `>`, `<=`, `>=`
- Texte entre guillemets simples, nombres sans guillemets
- Échapper une apostrophe en la doublant (`'L''Étranger'`)

-----
