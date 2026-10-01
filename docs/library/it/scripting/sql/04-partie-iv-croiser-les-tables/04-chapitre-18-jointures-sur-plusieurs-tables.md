---
title: Chapitre 18 — Jointures sur plusieurs tables
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie IV — Croiser les tables
  - index.md
---

## Le minimum à savoir

### Joindre 3 tables (ou plus)

On peut chaîner plusieurs `JOIN`. Exemple : afficher les emprunts avec **le nom du lecteur ET le titre du livre**.

```sql
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id;
```


Décodage :

- On part de `loans` (la table centrale)
- On joint `readers` pour récupérer les noms
- On joint `books` pour récupérer les titres

Chaque ligne du résultat combine les 3 informations.

### Joindre via une table d’association (relation N-N)

Pour afficher chaque livre avec son ou ses auteurs, il faut passer par `book_authors` :

```sql
SELECT b.title, a.name AS author_name
FROM books AS b
INNER JOIN book_authors AS ba ON b.id = ba.book_id
INNER JOIN authors AS a ON ba.author_id = a.id;
```


Si un livre a deux auteurs, il apparaîtra **deux fois** dans le résultat — une fois par auteur. C’est le comportement normal du `JOIN`.

### L’ordre des jointures

L’ordre dans lequel tu chaînes les `JOIN` n’a généralement pas d’impact sur le résultat (tant que les conditions sont correctes). Mais il a un impact sur la **lisibilité** :

```sql
-- Lisible : on part de la table "centrale" et on attache les références
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id

-- Aussi correct, mais moins naturel
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
INNER JOIN books AS b ON l.book_id = b.id
```


> **À retenir :** part de la table qui te semble centrale dans la question, puis attache les autres une par une.

> **📋 FIL ROUGE — Épisode 17**
> 
> La directrice : “Donne-moi un export complet : pour chaque emprunt, qui a emprunté, quel livre, quelle catégorie, quand.” Nora chaîne 4 jointures :
> 
> ```sql
> SELECT r.first_name, r.last_name, b.title, c.name AS categorie, l.loan_date
> FROM loans AS l
> INNER JOIN readers AS r ON l.reader_id = r.id
> INNER JOIN books AS b ON l.book_id = b.id
> INNER JOIN categories AS c ON b.category_id = c.id
> ORDER BY l.loan_date DESC;
> ```
> 
> Un seul résultat, toutes les informations utiles, prêt à exporter en CSV depuis DB Browser.

## Très utile en pratique

### Mélanger `INNER` et `LEFT`

Tu peux mélanger les types de jointures dans la même requête :

```sql
-- Tous les lecteurs, avec leurs emprunts (s'ils en ont) et le titre du livre
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
LEFT JOIN books AS b ON l.book_id = b.id
ORDER BY r.last_name;
```


Le `LEFT JOIN loans` garde tous les lecteurs. Le second `LEFT JOIN books` est important : si la première jointure renvoie `NULL` (lecteur sans emprunt), un `INNER JOIN` à `books` exclurait cette ligne. Le `LEFT JOIN` la garde.

## ❌ Erreur classique

```sql
-- Mélanger les conditions ON et WHERE de manière confuse
FROM readers r INNER JOIN loans l ON r.id = l.book_id    -- ❌ erreur de logique
                                          ↑↑↑↑
                                  devrait être l.reader_id

-- Le moteur ne renverra pas d'erreur — il fera la mauvaise jointure et tu obtiendras
-- des résultats absurdes. Toujours vérifier les conditions ON.

-- Alias incohérents
FROM loans AS l INNER JOIN readers AS r ON loans.reader_id = readers.id
-- ⚠️ Tu as défini les alias l et r, utilise-les :
ON l.reader_id = r.id    -- ✅
```


## 💡 Exercices

1. Affiche tous les emprunts avec le nom du lecteur, le titre du livre et le statut.
1. Affiche tous les livres avec leur(s) auteur(s) — un livre peut apparaître plusieurs fois s’il a plusieurs auteurs.
1. Affiche pour chaque emprunt en retard : le nom du lecteur, le titre du livre et la catégorie.

## ✅ Tu sais maintenant…

- Chaîner plusieurs `JOIN` (`INNER JOIN ... INNER JOIN ...`)
- Utiliser une table d’association pour les relations N-N
- Mélanger `INNER` et `LEFT JOIN` selon le besoin
- Toujours utiliser des alias quand tu as plus de 2 tables

-----
