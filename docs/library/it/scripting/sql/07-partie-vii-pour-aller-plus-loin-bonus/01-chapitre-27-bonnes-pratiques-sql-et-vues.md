---
title: Chapitre 27 — Bonnes pratiques SQL et vues
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VII — Pour aller plus loin — 🔴 Bonus
  - index.md
---

## Le minimum à savoir

### Les bonnes pratiques d’écriture

Une requête lisible, c’est une requête qu’on peut **comprendre, déboguer et modifier** sans douleur. Quelques règles simples :

**1. Indenter et aérer**

```sql
-- ❌ Illisible
SELECT r.first_name,r.last_name,b.title,l.loan_date FROM loans l INNER JOIN readers r ON l.reader_id=r.id INNER JOIN books b ON l.book_id=b.id WHERE l.status='late' ORDER BY l.loan_date DESC;

-- ✅ Lisible
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status = 'late'
ORDER BY l.loan_date DESC;
```


**2. Mots-clés SQL en MAJUSCULES**, noms de tables/colonnes en minuscules.

**3. Alias courts et significatifs** : `r` pour `readers`, `b` pour `books`, `l` pour `loans`.

**4. Éviter `SELECT *` dans les requêtes finales** — préfère lister les colonnes nécessaires.

**5. Commenter les requêtes complexes**

```sql
-- Lecteurs ayant emprunté plus de 3 livres en 2025
-- (utilisé pour les invitations à la soirée des grands lecteurs)
SELECT r.first_name, r.last_name, COUNT(*) AS nb_emprunts_2025
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE l.loan_date >= '2025-01-01'
GROUP BY r.id, r.first_name, r.last_name
HAVING COUNT(*) > 3;
```


**6. Toujours faire un `SELECT` avant `UPDATE` ou `DELETE`** (rappelé au Ch.21-22).

**7. Utiliser des transactions** pour les modifications importantes (Ch.23).

**8. Limiter les résultats avec `LIMIT`** quand tu explores.

### Les vues : enregistrer une requête sous un nom

Une **vue** (view) est une requête enregistrée que tu peux utiliser comme une table. Elle ne stocke pas de données — elle exécute la requête sous-jacente à chaque appel.

```sql
-- Créer une vue
CREATE VIEW active_loans AS
SELECT r.first_name, r.last_name, b.title, l.loan_date, l.status
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status IN ('borrowed', 'late');

-- L'utiliser comme une table
SELECT * FROM active_loans;
SELECT * FROM active_loans WHERE status = 'late';
```


**Pourquoi c’est utile :**

- Simplifier les requêtes complexes pour les utilisateurs
- Éviter de réécrire la même jointure 50 fois
- Masquer la complexité du schéma sous-jacent

**Limites :**

- Une vue n’**accélère pas** les requêtes — c’est juste une simplification d’écriture
- Modifier les données **à travers** une vue est limité et dépend du SGBD

> **À retenir :** les vues sont un outil de **lisibilité**, pas de performance. Pour la performance, on utilise les **index** (Ch.28).

### Supprimer une vue

```sql
DROP VIEW active_loans;
```


> **📋 FIL ROUGE — Épisode 26**
> 
> Nora se rend compte qu’elle écrit la même requête (lecteurs + livres + emprunts) dix fois par jour, légèrement adaptée à chaque fois. Elle crée une vue :
> 
> ```sql
> CREATE VIEW v_loans_full AS
> SELECT l.id, r.first_name, r.last_name, b.title, c.name AS category, l.loan_date, l.status
> FROM loans AS l
> INNER JOIN readers AS r ON l.reader_id = r.id
> INNER JOIN books AS b ON l.book_id = b.id
> INNER JOIN categories AS c ON b.category_id = c.id;
> ```
> 
> Maintenant, n’importe quelle question sur les emprunts se résume à `SELECT ... FROM v_loans_full WHERE ...`. Plus simple, plus rapide à écrire, et l’équipe peut l’utiliser sans connaître le détail des jointures.

## ✅ Tu sais maintenant…

- Les bonnes pratiques d’écriture (indentation, majuscules, alias, commentaires)
- Les vues comme requêtes enregistrées (`CREATE VIEW`, `DROP VIEW`)
- Les vues simplifient l’écriture mais n’accélèrent pas les requêtes

-----
