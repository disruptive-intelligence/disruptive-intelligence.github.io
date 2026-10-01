---
title: Chapitre 19 — Pièges classiques des jointures
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie IV — Croiser les tables
  - index.md
---

## Le minimum à savoir

Les jointures sont la partie la plus piégeuse de SQL. Ce chapitre regroupe les erreurs typiques — celles qui font que ta requête “marche” mais te donne des résultats faux. **C’est probablement le chapitre le plus important du cours pour éviter les bugs en production.**

### Piège n°1 : la jointure cartésienne

Si tu oublies la condition `ON`, ou si tu utilises l’ancienne syntaxe avec une virgule, tu obtiens un **produit cartésien** : chaque ligne de la première table est combinée avec **toutes** les lignes de la seconde.

```sql
-- Syntaxe ancienne, dangereuse
SELECT * FROM readers, loans;
-- → 15 lecteurs × 20 emprunts = 300 lignes !
-- → Toutes les combinaisons, sans aucun lien logique
```


15 × 20 = 300 lignes au lieu de 20. Avec 100 000 utilisateurs et 1 000 000 commandes, tu fais exploser la base.

> **À retenir :** **n’utilise jamais la syntaxe avec virgule** pour joindre deux tables. Toujours `INNER JOIN ... ON ...`. C’est une cause classique de “ma requête prend des heures et plante” en production.

### Piège n°2 : oublier la condition `ON`

Avec la syntaxe `JOIN` moderne, oublier le `ON` est une erreur de syntaxe (le moteur la refuse). Mais si tu utilises l’ancienne syntaxe ou si tu omets une partie de la condition, tu retombes sur un produit cartésien.

```sql
-- Erreur subtile : la condition n'est pas complète
SELECT * FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id
INNER JOIN authors a ON 1 = 1;        -- ❌ "1 = 1" est toujours vrai
-- → produit cartésien sur la jointure des auteurs !
```


### Piège n°3 : les doublons après jointure

Si tu fais une jointure sur une table N-N (comme `book_authors`), un livre avec 2 auteurs apparaîtra **2 fois**. Si tu calcules `COUNT(*)`, tu sur-compteras.

```sql
-- Combien de livres ?
SELECT COUNT(*) FROM books;
-- → 15

-- Combien de livres après jointure avec auteurs ?
SELECT COUNT(*) FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id;
-- → 16 (un livre est compté 2 fois car il a 2 auteurs co-écrits)
```


**Solution :** utilise `COUNT(DISTINCT b.id)` au lieu de `COUNT(*)` :

```sql
SELECT COUNT(DISTINCT b.id) FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id;
-- → 15
```


### Piège n°4 : confondre `WHERE` et condition de jointure

Vu au Ch.17 : mettre une condition sur la table de droite dans `WHERE` (au lieu de `ON`) transforme un `LEFT JOIN` en `INNER JOIN` déguisé.

```sql
-- ❌ Le WHERE exclut les lecteurs sans emprunt — pas l'effet voulu
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.status = 'returned';

-- ✅ Mettre la condition dans le ON pour vraiment garder tous les lecteurs
SELECT r.first_name, l.loan_date
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id AND l.status = 'returned';
```


### Piège n°5 : choisir le mauvais type de jointure

|Question                                     |Bon type                             |
|---------------------------------------------|-------------------------------------|
|“Quels lecteurs ont emprunté ?”              |`INNER JOIN` (correspondances)       |
|“Liste tous les lecteurs avec leurs emprunts”|`LEFT JOIN` (tous, même sans emprunt)|
|“Quels lecteurs n’ont jamais emprunté ?”     |`LEFT JOIN ... WHERE ... IS NULL`    |

Si tu utilises `INNER JOIN` pour la 2e ou 3e question, tu **excluras silencieusement** des données sans t’en rendre compte. Toujours te poser la question “qu’est-ce qui se passe pour les lignes sans correspondance ?”.

> **📋 FIL ROUGE — Épisode 18**
> 
> Nora avait livré un rapport “Combien de livres dans la base”, après l’avoir joint à `book_authors` pour avoir aussi les auteurs. Résultat : 16 livres. La directrice s’étonne — la fois précédente, il y en avait 15. Nora cherche, comprend que le livre coécrit est compté 2 fois, et corrige avec `COUNT(DISTINCT b.id)`. Petit incident, gros enseignement.

## Très utile en pratique

### Vérifier après chaque jointure

Quand tu écris une jointure complexe, **vérifie le nombre de lignes** :

```sql
-- D'abord, compte les lignes de la table principale
SELECT COUNT(*) FROM loans;     -- 20

-- Puis le résultat après jointure : tu dois avoir 20 lignes (ou plus si N-N)
SELECT COUNT(*) FROM loans l
INNER JOIN readers r ON l.reader_id = r.id;    -- doit aussi être 20
```


Si tu as plus, tu as probablement un produit cartésien ou un doublon. Si tu as moins, tu as exclu des lignes (peut-être à tort).

## ❌ Erreur classique (synthèse)

|Erreur                                |Symptôme                             |Solution                                              |
|--------------------------------------|-------------------------------------|------------------------------------------------------|
|Syntaxe virgule sans condition        |Beaucoup trop de lignes              |Utiliser `INNER JOIN ... ON ...`                      |
|`INNER` au lieu de `LEFT`             |Lignes manquantes                    |Vérifier qui doit être dans le résultat               |
|Condition dans `WHERE` au lieu de `ON`|`LEFT JOIN` se comporte comme `INNER`|Mettre les conditions sur la table droite dans le `ON`|
|`COUNT(*)` après jointure N-N         |Surcomptage                          |Utiliser `COUNT(DISTINCT col)`                        |
|Mauvaise condition `ON`               |Résultats absurdes                   |Relire et vérifier les `id`                           |

## 💡 Exercices

1. Combien y a-t-il de **livres distincts** parmi les emprunts (jointure `loans` + `books`) ?
1. Trouve les lecteurs qui ont au moins un emprunt en retard, sans doublons (utilise `DISTINCT`).
1. Vérifie : combien de lignes y a-t-il dans `book_authors` ? Combien de livres distincts ? Pourquoi la différence ?

## ✅ Tu sais maintenant…

- Le produit cartésien et comment l’éviter
- Les doublons après jointure N-N (utilise `COUNT(DISTINCT)`)
- La différence cruciale entre condition dans `ON` et dans `WHERE`
- Comment vérifier qu’une jointure ne casse pas les données
- Les 5 grands pièges et comment les détecter

## 🧩 Capstone Partie IV — Mini-projet

Crée un rapport “activité de la médiathèque” avec :

1. Le top 5 des lecteurs les plus actifs (nom + nombre d’emprunts).
1. La liste des livres jamais empruntés.
1. Le nombre d’emprunts par catégorie de livre.
1. La liste des lecteurs avec leurs emprunts en retard (s’ils en ont).

Utilise les jointures, agrégations et `LEFT JOIN ... IS NULL` selon les questions.

-----
