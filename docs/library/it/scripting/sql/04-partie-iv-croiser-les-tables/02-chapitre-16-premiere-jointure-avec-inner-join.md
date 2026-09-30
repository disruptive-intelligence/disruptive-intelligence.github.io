---
title: Chapitre 16 — Première jointure avec INNER JOIN
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie IV — Croiser les tables
  - index.md
---

## Le minimum à savoir

### La structure d’un `INNER JOIN`

```sql
SELECT readers.first_name, readers.last_name, loans.loan_date
FROM readers
INNER JOIN loans ON readers.id = loans.reader_id;
```


Décodage :

- `FROM readers` → table principale
- `INNER JOIN loans` → joins avec la table `loans`
- `ON readers.id = loans.reader_id` → la condition de jointure (la clé)

Le résultat : une ligne par couple (lecteur, emprunt) qui matche.

### Préfixer les colonnes par le nom de table

Quand deux tables ont une colonne du même nom (par exemple `id`), il faut **préfixer** pour lever l’ambiguïté :

```sql
SELECT readers.id, loans.id     -- préfixe obligatoire si "id" existe dans les deux
FROM readers
INNER JOIN loans ON readers.id = loans.reader_id;
```


### Les alias de table avec `AS`

Pour ne pas répéter `readers.` et `loans.` partout, on utilise des **alias courts** :

```sql
SELECT r.first_name, r.last_name, l.loan_date
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id;
```


`r` = `readers`, `l` = `loans`. Beaucoup plus lisible quand la requête grossit. Comme pour les colonnes, le `AS` est optionnel :

```sql
FROM readers r INNER JOIN loans l ON r.id = l.reader_id    -- équivalent
```


### Ce que fait vraiment `INNER JOIN`

`INNER JOIN` ne garde que les lignes qui ont une **correspondance dans les deux tables**.

Si Alice a 3 emprunts, on aura 3 lignes pour Alice dans le résultat (une par emprunt).
Si Sarah a 0 emprunt, **elle n’apparaîtra pas** dans le résultat (pas de match dans `loans`).

C’est important : `INNER JOIN` peut **filtrer implicitement** les lignes sans correspondance. Si tu veux les garder, c’est `LEFT JOIN` (Ch.17).

> **📋 FIL ROUGE — Épisode 15**
> 
> La directrice : “Donne-moi la liste des emprunts avec le nom du lecteur, pas juste son id.” Nora :
> 
> ```sql
> SELECT r.first_name, r.last_name, l.loan_date, l.status
> FROM readers AS r
> INNER JOIN loans AS l ON r.id = l.reader_id
> ORDER BY l.loan_date DESC;
> ```
> 
> Le résultat affiche les emprunts récents avec les noms — beaucoup plus exploitable que des `reader_id`.

## Très utile en pratique

### Filtrer après une jointure

Tu peux toujours ajouter un `WHERE` :

```sql
-- Emprunts d'Alice uniquement
SELECT r.first_name, r.last_name, l.loan_date, l.status
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE r.first_name = 'Alice';
```


### Trier après une jointure

```sql
-- Emprunts triés par date, du plus récent au plus ancien
SELECT r.last_name, l.loan_date
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
ORDER BY l.loan_date DESC;
```


## ❌ Erreur classique

```sql
-- Oublier le ON
SELECT * FROM readers INNER JOIN loans;
-- ❌ syntaxe incorrecte (manque ON), ou pire : produit cartésien

-- Oublier de préfixer une colonne ambiguë
SELECT id FROM readers INNER JOIN loans ON readers.id = loans.reader_id;
-- ❌ "ambiguous column: id"
SELECT readers.id FROM readers INNER JOIN loans ON readers.id = loans.reader_id;
-- ✅
```


## 💡 Exercices

1. Affiche le titre de chaque livre et le nom de sa catégorie (jointure `books` + `categories`).
1. Affiche tous les emprunts avec le nom du lecteur **et** le titre du livre (jointure `loans` + `readers` + `books`).
1. Affiche uniquement les emprunts en retard avec nom du lecteur.

## ✅ Tu sais maintenant…

- La structure : `FROM table1 INNER JOIN table2 ON condition`
- L’utilisation des alias de table (`r`, `l`, `b`…) pour la lisibilité
- `INNER JOIN` ne garde que les lignes avec correspondance dans les **deux** tables
- Combiner jointure + `WHERE` + `ORDER BY`

-----
