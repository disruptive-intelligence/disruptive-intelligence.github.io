---
title: PARTIE IV — CROISER LES TABLES
source: IT/Culture/SQL.md
note: SQL
chapter: 4
chapters: 8
---

-----


## Chapitre 15 — Comprendre les relations entre tables

### Le minimum à savoir

#### Pourquoi croiser les tables ?

Reprenons la base. Si on veut afficher “Alice a emprunté Les Misérables le 10 janvier 2025”, l’information est répartie sur **trois tables** :

```
readers              loans                       books
┌────┬────────────┐  ┌────┬───────────┬─────────┐  ┌────┬─────────────────┐
│ id │ first_name │  │ id │ reader_id │ book_id │  │ id │ title           │
├────┼────────────┤  ├────┼───────────┼─────────┤  ├────┼─────────────────┤
│ 1  │ Alice      │  │ 1  │ 1         │ 1       │  │ 1  │ Les Misérables  │
└────┴────────────┘  └────┴───────────┴─────────┘  └────┴─────────────────┘
       ↑                       ↑           ↑                  ↑
    "Alice"              "id du lecteur"  "id du livre"   "Les Misérables"
```

Pour reconstituer la phrase complète, il faut **joindre** les tables sur leurs identifiants.

C’est ce que fait `JOIN`.

#### Les types de relations

|Relation                       |Exemple                                                          |Modélisation                                |
|-------------------------------|-----------------------------------------------------------------|--------------------------------------------|
|**1-N** (un-à-plusieurs)       |Un lecteur a plusieurs emprunts                                  |Clé étrangère dans la table “côté plusieurs”|
|**N-N** (plusieurs-à-plusieurs)|Un livre a plusieurs auteurs ; un auteur a écrit plusieurs livres|Table d’**association** intermédiaire       |

#### Une relation 1-N : `readers` → `loans`

Un lecteur peut avoir plusieurs emprunts, mais un emprunt appartient à un seul lecteur.

```
readers (côté "1")              loans (côté "N")
┌────┬────────────┐              ┌────┬───────────┬─────────┐
│ id │ first_name │              │ id │ reader_id │ book_id │
├────┼────────────┤              ├────┼───────────┼─────────┤
│ 1  │ Alice      │ ←──────────  │ 1  │ 1         │ 1       │
│    │            │ ←──────────  │ 3  │ 1         │ 3       │
│    │            │ ←──────────  │ 6  │ 1         │ 6       │
│ 2  │ Karim      │ ←──────────  │ 2  │ 2         │ 2       │
└────┴────────────┘              └────┴───────────┴─────────┘
```

Alice (id=1) a 3 emprunts. Karim (id=1) en a un. La clé étrangère `reader_id` dans `loans` pointe vers `readers.id`.

#### Une relation N-N : `books` ↔ `authors`

Un livre peut avoir plusieurs auteurs (un livre coécrit), et un auteur peut avoir écrit plusieurs livres. On ne peut pas modéliser ça avec une simple clé étrangère — il faut une **table d’association**.

```
books                book_authors                  authors
┌────┬──────────┐   ┌─────────┬───────────┐       ┌────┬─────────────────┐
│ id │ title    │   │ book_id │ author_id │       │ id │ name            │
├────┼──────────┤   ├─────────┼───────────┤       ├────┼─────────────────┤
│ 1  │ Les Mis. │ ←─│ 1       │ 1         │──→    │ 1  │ Victor Hugo     │
│ 9  │ N-D Paris│ ←─│ 9       │ 1         │──→    │    │                 │
│ 2  │ 1984     │ ←─│ 2       │ 2         │──→    │ 2  │ George Orwell   │
└────┴──────────┘   └─────────┴───────────┘       └────┴─────────────────┘
```

La table `book_authors` ne contient que des **références** : “le livre 1 a pour auteur l’auteur 1”. Pas de doublons, pas d’incohérence — chaque relation est une ligne.

#### Les tables de la base `bibliotheque.db`

|Table         |Type                            |Lien                                                                                                                                                                        |
|--------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`categories`  |Référence (catégories de livres)|—                                                                                                                                                                           |
|`authors`     |Référence (auteurs)             |—                                                                                                                                                                           |
|`books`       |Entité principale (livres)      |`category_id` → `categories.id`                                                                                                                                             |
|`book_authors`|**Association N-N**             |`book_id` → `books.id`, `author_id` → `authors.id`                                                                                                                          |
|`readers`     |Entité principale (lecteurs)    |—                                                                                                                                                                           |
|`loans`       |Association + données (emprunts)|`reader_id` → `readers.id`, `book_id` → `books.id`                                                                                                                          |
|`staff_users` |Comptes du personnel            |—                                                                                                                                                                           |
|`login_events`|Événements de connexion         |lien logique `username` → `staff_users.username`, **non contraint volontairement** (un attaquant peut tenter avec des comptes inexistants — il faut pouvoir les journaliser)|


> **📋 FIL ROUGE — Épisode 14**
> 
> Nora dessine sur un papier le schéma de la base. Elle se rend compte que c’est presque un graphe : `readers` et `books` sont reliés par `loans`. `books` et `authors` sont reliés par `book_authors`. Cette représentation visuelle l’aide énormément — elle comprend que toutes les questions vont passer par les jointures.

### Très utile en pratique

#### Quand utiliser une table d’association ?

Si tu te poses la question “un X peut-il avoir plusieurs Y, et un Y plusieurs X ?” — si oui, c’est du N-N → table d’association.

Exemples classiques :

- Étudiants ↔ cours
- Films ↔ acteurs
- Articles ↔ tags
- Utilisateurs ↔ rôles

### ✅ Tu sais maintenant…

- Pourquoi les données sont réparties sur plusieurs tables
- La relation **1-N** : clé étrangère côté “plusieurs”
- La relation **N-N** : table d’association intermédiaire
- Le schéma complet de la base `bibliotheque.db`

-----


## Chapitre 16 — Première jointure avec INNER JOIN

### Le minimum à savoir

#### La structure d’un `INNER JOIN`

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

#### Préfixer les colonnes par le nom de table

Quand deux tables ont une colonne du même nom (par exemple `id`), il faut **préfixer** pour lever l’ambiguïté :

```sql
SELECT readers.id, loans.id     -- préfixe obligatoire si "id" existe dans les deux
FROM readers
INNER JOIN loans ON readers.id = loans.reader_id;
```

#### Les alias de table avec `AS`

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

#### Ce que fait vraiment `INNER JOIN`

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

### Très utile en pratique

#### Filtrer après une jointure

Tu peux toujours ajouter un `WHERE` :

```sql
-- Emprunts d'Alice uniquement
SELECT r.first_name, r.last_name, l.loan_date, l.status
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE r.first_name = 'Alice';
```

#### Trier après une jointure

```sql
-- Emprunts triés par date, du plus récent au plus ancien
SELECT r.last_name, l.loan_date
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
ORDER BY l.loan_date DESC;
```

### ❌ Erreur classique

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

### 💡 Exercices

1. Affiche le titre de chaque livre et le nom de sa catégorie (jointure `books` + `categories`).
1. Affiche tous les emprunts avec le nom du lecteur **et** le titre du livre (jointure `loans` + `readers` + `books`).
1. Affiche uniquement les emprunts en retard avec nom du lecteur.

### ✅ Tu sais maintenant…

- La structure : `FROM table1 INNER JOIN table2 ON condition`
- L’utilisation des alias de table (`r`, `l`, `b`…) pour la lisibilité
- `INNER JOIN` ne garde que les lignes avec correspondance dans les **deux** tables
- Combiner jointure + `WHERE` + `ORDER BY`

-----


## Chapitre 17 — LEFT JOIN et données sans correspondance

### Le minimum à savoir

#### Le besoin : trouver “ce qui manque”

`INNER JOIN` est génial quand toutes les lignes ont une correspondance. Mais que faire pour répondre à des questions comme :

- “Quels lecteurs n’ont **jamais** emprunté ?”
- “Quels livres n’ont **jamais** été empruntés ?”

Avec `INNER JOIN`, ces lignes sont **invisibles** — elles n’ont pas de match. Il faut `LEFT JOIN`.

#### `LEFT JOIN` : garder TOUTE la table de gauche

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

#### Trouver les lignes “orphelines”

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

#### `INNER JOIN` vs `LEFT JOIN` : quand utiliser quoi ?

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

### Très utile en pratique

#### Quels livres n’ont jamais été empruntés ?

```sql
SELECT b.title
FROM books AS b
LEFT JOIN loans AS l ON b.id = l.book_id
WHERE l.id IS NULL;
```

Même technique, autre angle : la table `books` à gauche, `loans` à droite, on garde les livres sans match.

#### `RIGHT JOIN` ?

Il existe aussi `RIGHT JOIN` (l’inverse de `LEFT JOIN`), mais il est rare en pratique — on inverse juste l’ordre des tables et on utilise `LEFT JOIN`. SQLite ne supporte pas `RIGHT JOIN` historiquement (ajouté en version récente). Concentre-toi sur `LEFT JOIN`.

### ❌ Erreur classique

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

### 💡 Exercices

1. Liste les livres qui n’ont jamais été empruntés.
1. Liste les auteurs qui n’ont aucun livre dans la base (jointure avec `book_authors`).
1. Pour chaque lecteur, affiche son nom et le nombre de ses emprunts (utilise `LEFT JOIN` + `COUNT` + `GROUP BY`).

### ✅ Tu sais maintenant…

- `LEFT JOIN` garde **toutes** les lignes de la table de gauche
- Les colonnes de droite sont `NULL` quand il n’y a pas de match
- La technique `LEFT JOIN ... WHERE ... IS NULL` pour trouver les lignes sans correspondance
- La différence entre `WHERE` (après jointure) et conditions dans le `ON` (pendant la jointure)

-----


## Chapitre 18 — Jointures sur plusieurs tables

### Le minimum à savoir

#### Joindre 3 tables (ou plus)

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

#### Joindre via une table d’association (relation N-N)

Pour afficher chaque livre avec son ou ses auteurs, il faut passer par `book_authors` :

```sql
SELECT b.title, a.name AS author_name
FROM books AS b
INNER JOIN book_authors AS ba ON b.id = ba.book_id
INNER JOIN authors AS a ON ba.author_id = a.id;
```

Si un livre a deux auteurs, il apparaîtra **deux fois** dans le résultat — une fois par auteur. C’est le comportement normal du `JOIN`.

#### L’ordre des jointures

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

### Très utile en pratique

#### Mélanger `INNER` et `LEFT`

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

### ❌ Erreur classique

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

### 💡 Exercices

1. Affiche tous les emprunts avec le nom du lecteur, le titre du livre et le statut.
1. Affiche tous les livres avec leur(s) auteur(s) — un livre peut apparaître plusieurs fois s’il a plusieurs auteurs.
1. Affiche pour chaque emprunt en retard : le nom du lecteur, le titre du livre et la catégorie.

### ✅ Tu sais maintenant…

- Chaîner plusieurs `JOIN` (`INNER JOIN ... INNER JOIN ...`)
- Utiliser une table d’association pour les relations N-N
- Mélanger `INNER` et `LEFT JOIN` selon le besoin
- Toujours utiliser des alias quand tu as plus de 2 tables

-----


## Chapitre 19 — Pièges classiques des jointures

### Le minimum à savoir

Les jointures sont la partie la plus piégeuse de SQL. Ce chapitre regroupe les erreurs typiques — celles qui font que ta requête “marche” mais te donne des résultats faux. **C’est probablement le chapitre le plus important du cours pour éviter les bugs en production.**

#### Piège n°1 : la jointure cartésienne

Si tu oublies la condition `ON`, ou si tu utilises l’ancienne syntaxe avec une virgule, tu obtiens un **produit cartésien** : chaque ligne de la première table est combinée avec **toutes** les lignes de la seconde.

```sql
-- Syntaxe ancienne, dangereuse
SELECT * FROM readers, loans;
-- → 15 lecteurs × 20 emprunts = 300 lignes !
-- → Toutes les combinaisons, sans aucun lien logique
```

15 × 20 = 300 lignes au lieu de 20. Avec 100 000 utilisateurs et 1 000 000 commandes, tu fais exploser la base.

> **À retenir :** **n’utilise jamais la syntaxe avec virgule** pour joindre deux tables. Toujours `INNER JOIN ... ON ...`. C’est une cause classique de “ma requête prend des heures et plante” en production.

#### Piège n°2 : oublier la condition `ON`

Avec la syntaxe `JOIN` moderne, oublier le `ON` est une erreur de syntaxe (le moteur la refuse). Mais si tu utilises l’ancienne syntaxe ou si tu omets une partie de la condition, tu retombes sur un produit cartésien.

```sql
-- Erreur subtile : la condition n'est pas complète
SELECT * FROM books b
INNER JOIN book_authors ba ON b.id = ba.book_id
INNER JOIN authors a ON 1 = 1;        -- ❌ "1 = 1" est toujours vrai
-- → produit cartésien sur la jointure des auteurs !
```

#### Piège n°3 : les doublons après jointure

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

#### Piège n°4 : confondre `WHERE` et condition de jointure

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

#### Piège n°5 : choisir le mauvais type de jointure

|Question                                     |Bon type                             |
|---------------------------------------------|-------------------------------------|
|“Quels lecteurs ont emprunté ?”              |`INNER JOIN` (correspondances)       |
|“Liste tous les lecteurs avec leurs emprunts”|`LEFT JOIN` (tous, même sans emprunt)|
|“Quels lecteurs n’ont jamais emprunté ?”     |`LEFT JOIN ... WHERE ... IS NULL`    |

Si tu utilises `INNER JOIN` pour la 2e ou 3e question, tu **excluras silencieusement** des données sans t’en rendre compte. Toujours te poser la question “qu’est-ce qui se passe pour les lignes sans correspondance ?”.

> **📋 FIL ROUGE — Épisode 18**
> 
> Nora avait livré un rapport “Combien de livres dans la base”, après l’avoir joint à `book_authors` pour avoir aussi les auteurs. Résultat : 16 livres. La directrice s’étonne — la fois précédente, il y en avait 15. Nora cherche, comprend que le livre coécrit est compté 2 fois, et corrige avec `COUNT(DISTINCT b.id)`. Petit incident, gros enseignement.

### Très utile en pratique

#### Vérifier après chaque jointure

Quand tu écris une jointure complexe, **vérifie le nombre de lignes** :

```sql
-- D'abord, compte les lignes de la table principale
SELECT COUNT(*) FROM loans;     -- 20

-- Puis le résultat après jointure : tu dois avoir 20 lignes (ou plus si N-N)
SELECT COUNT(*) FROM loans l
INNER JOIN readers r ON l.reader_id = r.id;    -- doit aussi être 20
```

Si tu as plus, tu as probablement un produit cartésien ou un doublon. Si tu as moins, tu as exclu des lignes (peut-être à tort).

### ❌ Erreur classique (synthèse)

|Erreur                                |Symptôme                             |Solution                                              |
|--------------------------------------|-------------------------------------|------------------------------------------------------|
|Syntaxe virgule sans condition        |Beaucoup trop de lignes              |Utiliser `INNER JOIN ... ON ...`                      |
|`INNER` au lieu de `LEFT`             |Lignes manquantes                    |Vérifier qui doit être dans le résultat               |
|Condition dans `WHERE` au lieu de `ON`|`LEFT JOIN` se comporte comme `INNER`|Mettre les conditions sur la table droite dans le `ON`|
|`COUNT(*)` après jointure N-N         |Surcomptage                          |Utiliser `COUNT(DISTINCT col)`                        |
|Mauvaise condition `ON`               |Résultats absurdes                   |Relire et vérifier les `id`                           |

### 💡 Exercices

1. Combien y a-t-il de **livres distincts** parmi les emprunts (jointure `loans` + `books`) ?
1. Trouve les lecteurs qui ont au moins un emprunt en retard, sans doublons (utilise `DISTINCT`).
1. Vérifie : combien de lignes y a-t-il dans `book_authors` ? Combien de livres distincts ? Pourquoi la différence ?

### ✅ Tu sais maintenant…

- Le produit cartésien et comment l’éviter
- Les doublons après jointure N-N (utilise `COUNT(DISTINCT)`)
- La différence cruciale entre condition dans `ON` et dans `WHERE`
- Comment vérifier qu’une jointure ne casse pas les données
- Les 5 grands pièges et comment les détecter

### 🧩 Capstone Partie IV — Mini-projet

Crée un rapport “activité de la médiathèque” avec :

1. Le top 5 des lecteurs les plus actifs (nom + nombre d’emprunts).
1. La liste des livres jamais empruntés.
1. Le nombre d’emprunts par catégorie de livre.
1. La liste des lecteurs avec leurs emprunts en retard (s’ils en ont).

Utilise les jointures, agrégations et `LEFT JOIN ... IS NULL` selon les questions.

-----
