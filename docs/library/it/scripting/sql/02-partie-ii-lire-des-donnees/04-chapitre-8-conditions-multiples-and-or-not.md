---
title: 'Chapitre 8 — Conditions multiples : AND, OR, NOT'
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie II — Lire des données
  - index.md
---

## Le minimum à savoir

### Combiner des conditions avec `AND`

`AND` impose que **toutes** les conditions soient vraies :

```sql
SELECT *
FROM books
WHERE publication_year >= 2000
  AND category_id = 1;
```


→ Les livres publiés depuis 2000 **ET** de catégorie 1 (Roman).

### Au moins une condition avec `OR`

`OR` accepte une ligne si **au moins une** des conditions est vraie :

```sql
SELECT *
FROM readers
WHERE city = 'Paris'
   OR city = 'Lyon';
```


→ Les lecteurs qui habitent Paris **OU** Lyon.

### Inverser avec `NOT`

`NOT` inverse une condition :

```sql
SELECT *
FROM loans
WHERE NOT status = 'returned';
```


→ Les emprunts qui ne sont **pas** retournés (donc en cours ou en retard).

### La priorité : parenthèses obligatoires si tu mélanges AND et OR

`AND` est prioritaire sur `OR` (comme `*` est prioritaire sur `+` en maths). Donc cette requête :

```sql
SELECT *
FROM books
WHERE category_id = 1 OR category_id = 6 AND publication_year >= 2000;
```


est lue par SQL comme :

```sql
WHERE category_id = 1 OR (category_id = 6 AND publication_year >= 2000)
```


Ce n’est probablement pas ce que tu voulais. Pour éviter toute ambiguïté, **utilise des parenthèses** :

```sql
SELECT *
FROM books
WHERE (category_id = 1 OR category_id = 6)
  AND publication_year >= 2000;
```


> **À retenir :** dès que tu mélanges `AND` et `OR`, mets des parenthèses. Ce n’est pas du zèle — c’est la seule façon de garantir que ta requête fait ce que tu crois qu’elle fait.

> **📋 FIL ROUGE — Épisode 7**
> 
> La directrice veut une promotion : “envoie un email aux lecteurs habitant Paris ou Lyon, inscrits depuis 2024”. Nora écrit :
> 
> ```sql
> SELECT first_name, last_name, email
> FROM readers
> WHERE (city = 'Paris' OR city = 'Lyon')
>   AND registration_date >= '2024-01-01';
> ```
> 
> Elle obtient 5 lecteurs. Sans les parenthèses, elle aurait récupéré tous les Parisiens (peu importe la date) **plus** les Lyonnais inscrits depuis 2024 — résultat très différent.

## Très utile en pratique

### Quand `OR` est répétitif, utilise `IN` (Ch.9)

Tu verras au prochain chapitre que :

```sql
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille'
```


s’écrit plus proprement avec :

```sql
WHERE city IN ('Paris', 'Lyon', 'Marseille')
```


## ❌ Erreur classique

```sql
-- Oublier les parenthèses quand on mélange AND et OR
WHERE city = 'Paris' OR city = 'Lyon' AND age > 30
-- → SQL lit : WHERE city = 'Paris' OR (city = 'Lyon' AND age > 30)
-- → probablement pas ce que tu voulais
WHERE (city = 'Paris' OR city = 'Lyon') AND age > 30   -- ✅

-- Confondre AND et OR sur le sens commun
-- "lecteurs habitant à Paris ET Lyon"
WHERE city = 'Paris' AND city = 'Lyon'    -- ❌ aucune ligne ! Une ville ne peut pas valoir deux choses à la fois
WHERE city = 'Paris' OR city = 'Lyon'     -- ✅ "à Paris OU à Lyon"
```


## 💡 Exercices

1. Affiche les livres de catégorie Roman (id=1) **et** publiés avant 1950.
1. Affiche les lecteurs habitant à Paris, Lyon ou Bordeaux.
1. Affiche les emprunts qui ne sont pas en retard (`status` différent de `'late'`).

## ✅ Tu sais maintenant…

- Combiner des conditions avec `AND` (toutes vraies)
- Accepter avec `OR` (au moins une vraie)
- Inverser avec `NOT`
- Utiliser des parenthèses dès que tu mélanges `AND` et `OR`

-----
