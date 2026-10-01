---
title: Chapitre 17 — LEFT JOIN et données sans correspondance
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie IV — Croiser les tables
  - index.md
---

## Le minimum à savoir

### Le besoin : trouver “ce qui manque”

`INNER JOIN` est génial quand toutes les lignes ont une correspondance. Mais que faire pour répondre à des questions comme :

- “Quels lecteurs n’ont **jamais** emprunté ?”
- “Quels livres n’ont **jamais** été empruntés ?”

Avec `INNER JOIN`, ces lignes sont **invisibles** — elles n’ont pas de match. Il faut `LEFT JOIN`.

### `LEFT JOIN` : garder TOUTE la table de gauche

```sql
SELECT r.first_name, r.last_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id;
```


Le résultat contient **tous** les lecteurs — y compris ceux qui n’ont jamais emprunté. Pour ces derniers, les colonnes de `loans` sont remplies de `NULL`.

```
┌────────────┬───────────┬────────────┐
│ first_name │ last_name │ loan_date  │
├────────────┼───────────┼────────────┤
│ Alice      │ Martin    │ 2025-01-10 │
│ Alice      │ Martin    │ 2025-02-20 │   ← Alice apparaît plusieurs fois (3 emprunts)
│ Alice      │ Martin    │ 2025-04-10 │
│ Karim      │ Bernard   │ 2025-01-15 │
│ Sarah      │ Mercier   │ NULL       │   ← Sarah n'a jamais emprunté
│ Inès       │ Vincent   │ NULL       │   ← Idem
└────────────┴───────────┴────────────┘
```


### Trouver les lignes “orphelines”

C’est le cas d’usage classique : trouver les lignes de la gauche **sans correspondance** à droite. On filtre avec `WHERE ... IS NULL` :

```sql
-- Lecteurs qui n'ont JAMAIS emprunté
SELECT r.first_name, r.last_name
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.id IS NULL;
```


`l.id IS NULL` signifie “il n’y a pas eu de match dans `loans`”. Donc ce lecteur n’a pas d’emprunt.

> **C’est une technique fondamentale.** Mémorise-la — elle revient sans arrêt en SQL professionnel.

### `INNER JOIN` vs `LEFT JOIN` : quand utiliser quoi ?

|Situation                                                                    |Choix                            |
|-----------------------------------------------------------------------------|---------------------------------|
|Je veux les correspondances entre deux tables                                |`INNER JOIN`                     |
|Je veux toutes les lignes de la table principale, avec ou sans correspondance|`LEFT JOIN`                      |
|Je veux ce qui n’a pas de correspondance                                     |`LEFT JOIN` + `WHERE ... IS NULL`|


> **📋 FIL ROUGE — Épisode 16**
> 
> La directrice : “Combien de nos lecteurs n’ont jamais emprunté de livre ? On va leur faire une relance.” Nora :
> 
> ```sql
> SELECT r.first_name, r.last_name, r.email
> FROM readers AS r
> LEFT JOIN loans AS l ON r.id = l.reader_id
> WHERE l.id IS NULL;
> ```
> 
> 4 lecteurs identifiés. Avec un `INNER JOIN`, ils auraient été invisibles. C’est exactement le genre de question impossible à répondre sans maîtriser le `LEFT JOIN`.

## Très utile en pratique

### Quels livres n’ont jamais été empruntés ?

```sql
SELECT b.title
FROM books AS b
LEFT JOIN loans AS l ON b.id = l.book_id
WHERE l.id IS NULL;
```


Même technique, autre angle : la table `books` à gauche, `loans` à droite, on garde les livres sans match.

### `RIGHT JOIN` ?

Il existe aussi `RIGHT JOIN` (l’inverse de `LEFT JOIN`), mais il est rare en pratique — on inverse juste l’ordre des tables et on utilise `LEFT JOIN`. SQLite ne supporte pas `RIGHT JOIN` historiquement (ajouté en version récente). Concentre-toi sur `LEFT JOIN`.

## ❌ Erreur classique

```sql
-- Oublier WHERE ... IS NULL et croire avoir un LEFT JOIN inutile
SELECT r.first_name, l.loan_date
FROM readers r LEFT JOIN loans l ON r.id = l.reader_id;
-- → renvoie tous les emprunts ET les lecteurs sans emprunt (avec NULL)
-- → si tu voulais juste les emprunts, INNER JOIN aurait suffi

-- Mettre la condition de filtrage de la table droite dans le WHERE au lieu du ON
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.status = 'returned';
-- ⚠️ Ce WHERE filtre APRÈS la jointure, donc les lecteurs sans emprunt
--    (où l.status est NULL) sont aussi exclus → ça fait un INNER JOIN déguisé.
-- Si tu veux garder tous les lecteurs et joindre seulement leurs emprunts retournés :
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id AND l.status = 'returned';
-- ↑ la condition est dans le ON
```


## 💡 Exercices

1. Liste les livres qui n’ont jamais été empruntés.
1. Liste les auteurs qui n’ont aucun livre dans la base (jointure avec `book_authors`).
1. Pour chaque lecteur, affiche son nom et le nombre de ses emprunts (utilise `LEFT JOIN` + `COUNT` + `GROUP BY`).

## ✅ Tu sais maintenant…

- `LEFT JOIN` garde **toutes** les lignes de la table de gauche
- Les colonnes de droite sont `NULL` quand il n’y a pas de match
- La technique `LEFT JOIN ... WHERE ... IS NULL` pour trouver les lignes sans correspondance
- La différence entre `WHERE` (après jointure) et conditions dans le `ON` (pendant la jointure)

-----
