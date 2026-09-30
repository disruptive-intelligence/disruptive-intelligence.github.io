---
title: PARTIE II — LIRE DES DONNÉES
source: IT/Culture/SQL.md
note: SQL
chapter: 2
chapters: 8
---

-----


## Chapitre 5 — Première requête avec SELECT

### Le minimum à savoir

#### La requête de base : `SELECT ... FROM`

Toute lecture de données commence par `SELECT` :

```sql
SELECT * FROM readers;
```

Décomposé :

- `SELECT` → “je veux lire”
- `*` → “toutes les colonnes”
- `FROM readers` → “depuis la table `readers`”
- `;` → fin de la requête

Le résultat : toutes les lignes et toutes les colonnes de la table `readers`.

#### Sélectionner certaines colonnes

Plutôt que tout afficher, choisis les colonnes utiles :

```sql
SELECT first_name, last_name, email
FROM readers;
```

Tu obtiens uniquement le prénom, le nom et l’email — plus lisible quand la table a beaucoup de colonnes.

#### L’ordre des colonnes

L’ordre dans lequel tu listes les colonnes après `SELECT` est l’ordre dans lequel elles s’affichent :

```sql
SELECT email, last_name, first_name
FROM readers;
```

Ça affiche d’abord l’email, puis le nom, puis le prénom. Tu choisis ton ordre.

#### Le point-virgule final

En SQL, chaque requête se termine par un point-virgule `;`. C’est ce qui dit au moteur “j’ai fini, exécute”.

Dans DB Browser, tu peux te passer du `;` quand tu n’exécutes qu’une seule requête. Mais prends le réflexe — c’est obligatoire dans la plupart des outils.

#### La convention : SQL en MAJUSCULES

Par convention, on écrit les **mots-clés SQL** (`SELECT`, `FROM`, `WHERE`…) en majuscules, et les **noms de tables/colonnes** en minuscules. C’est juste une convention de lisibilité — SQL n’est pas sensible à la casse pour les mots-clés :

```sql
-- ✅ Convention recommandée (lisible)
SELECT first_name, last_name FROM readers;

-- ⚠️ Marche aussi, mais moins lisible
select first_name, last_name from readers;
```

> **📋 FIL ROUGE — Épisode 4**
> 
> La directrice demande à Nora : “Combien de lecteurs avons-nous, et qui sont-ils ?”. Nora ouvre DB Browser et tape sa toute première requête : `SELECT * FROM readers;`. Le résultat s’affiche : 15 lecteurs. Premier succès. Mais elle réalise vite qu’afficher *toutes* les colonnes est trop bavard — elle simplifie : `SELECT first_name, last_name, city FROM readers;`. Plus lisible.

### Très utile en pratique

#### `SELECT *` vs colonnes explicites

|Approche                |Quand l’utiliser                                    |
|------------------------|----------------------------------------------------|
|`SELECT *`              |Pour explorer une table, voir ce qu’elle contient   |
|`SELECT col1, col2, ...`|Pour les requêtes finales, les rapports, les exports|


> **Bonne pratique :** `SELECT *` est pratique pour explorer, mais évite-le dans les requêtes “de production”. Pourquoi ? Parce que si la table évolue (nouvelles colonnes), ton résultat change sans que tu ne contrôles rien.

### ❌ Erreur classique

```sql
-- Oublier le FROM
SELECT first_name, last_name;       -- ❌ "no such column" ou "missing FROM clause"
SELECT first_name, last_name FROM readers;  -- ✅

-- Mettre une virgule de trop
SELECT first_name, last_name, FROM readers;  -- ❌ erreur de syntaxe
SELECT first_name, last_name FROM readers;   -- ✅

-- Confondre nom de colonne et nom de table
SELECT readers FROM readers;        -- ❌ "readers" n'est pas une colonne
SELECT * FROM readers;              -- ✅
```

### 💡 Exercices

1. Affiche tous les livres (table `books`).
1. Affiche uniquement le titre et l’année de publication des livres.
1. Affiche le nom complet et la ville des lecteurs.

### ✅ Tu sais maintenant…

- La structure de base : `SELECT colonnes FROM table;`
- `SELECT *` pour toutes les colonnes
- Choisir et ordonner les colonnes manuellement
- La convention : mots-clés SQL en majuscules
- Le point-virgule final

-----


## Chapitre 6 — Améliorer l’affichage : alias, DISTINCT, commentaires

### Le minimum à savoir

#### Renommer une colonne avec `AS` (alias)

Tu peux donner un nom temporaire à une colonne dans le résultat :

```sql
SELECT first_name AS prenom, last_name AS nom, email AS courriel
FROM readers;
```

Le résultat affiche les colonnes sous les noms `prenom`, `nom`, `courriel`, sans modifier la table elle-même.

> **À retenir :** un alias ne change rien dans la base — il modifie seulement l’**affichage**. C’est utile pour rendre les résultats plus lisibles, ou pour franciser un export.

Le `AS` est même optionnel — ces deux requêtes sont équivalentes :

```sql
SELECT first_name AS prenom FROM readers;
SELECT first_name prenom FROM readers;       -- même chose, mais moins lisible
```

> **Bonne pratique :** garde le `AS` pour la clarté. Tu le verras partout.

#### Éliminer les doublons avec `DISTINCT`

Sans `DISTINCT`, SQL te montre toutes les lignes — y compris les valeurs répétées :

```sql
SELECT city FROM readers;
-- Paris, Lyon, Paris, Marseille, Paris, Lyon, ... (avec doublons)
```

Avec `DISTINCT`, tu n’obtiens que les valeurs **uniques** :

```sql
SELECT DISTINCT city FROM readers;
-- Paris, Lyon, Marseille, Bordeaux, Toulouse (sans doublons)
```

C’est l’équivalent de “supprimer les doublons” dans Excel.

#### Commentaires SQL

Comme dans les autres langages, tu peux annoter ton code :

```sql
-- Ceci est un commentaire sur une ligne (deux tirets)

/* Ceci est un commentaire
   sur plusieurs lignes
   (style C) */

SELECT first_name, last_name   -- commentaire en fin de ligne
FROM readers;
```

> **Bonne pratique :** commente tes requêtes complexes. Tu te remercieras dans 6 mois quand tu reliras.

> **📋 FIL ROUGE — Épisode 5**
> 
> La directrice demande à Nora : “Dans quelles villes nos lecteurs habitent-ils ?”. Nora utilise `DISTINCT` :
> 
> ```sql
> SELECT DISTINCT city FROM readers;
> ```
> 
> Résultat : Paris, Lyon, Marseille, Bordeaux, Toulouse. 5 villes. Elle peut maintenant proposer de cibler des animations dans chacune.

### Très utile en pratique

#### `DISTINCT` sur plusieurs colonnes

`DISTINCT` s’applique à **la combinaison** de toutes les colonnes sélectionnées :

```sql
SELECT DISTINCT first_name, city FROM readers;
-- Élimine les couples (prénom, ville) en double
```

Donc deux Alice dans deux villes différentes apparaîtront **deux fois** — c’est le couple qui doit être unique.

### ❌ Erreur classique

```sql
-- Mettre AS au mauvais endroit
SELECT AS prenom first_name FROM readers;     -- ❌ AS vient APRÈS la colonne
SELECT first_name AS prenom FROM readers;      -- ✅

-- DISTINCT mal placé
SELECT first_name, DISTINCT city FROM readers; -- ❌ DISTINCT s'applique à toute la sélection
SELECT DISTINCT city FROM readers;             -- ✅
```

### ✅ Tu sais maintenant…

- Renommer une colonne dans le résultat avec `AS`
- Éliminer les doublons avec `DISTINCT`
- Commenter avec `--` ou `/* ... */`

-----


## Chapitre 7 — Filtrer avec WHERE

### Le minimum à savoir

#### Le besoin : ne pas tout afficher

Souvent, tu ne veux pas **toutes** les lignes — seulement celles qui correspondent à un critère. C’est le rôle de `WHERE` :

```sql
SELECT *
FROM readers
WHERE city = 'Paris';
```

`WHERE` filtre les lignes : seules celles où `city` vaut `'Paris'` sont retournées.

#### Les opérateurs de comparaison

|Opérateur   |Signification    |Exemple                   |
|------------|-----------------|--------------------------|
|`=`         |Égal             |`city = 'Paris'`          |
|`<>` ou `!=`|Différent        |`city <> 'Paris'`         |
|`<`         |Inférieur        |`publication_year < 2000` |
|`>`         |Supérieur        |`publication_year > 2000` |
|`<=`        |Inférieur ou égal|`publication_year <= 2000`|
|`>=`        |Supérieur ou égal|`publication_year >= 1990`|


> **Attention :** en SQL, l’égalité s’écrit avec **un seul** `=` (pas deux comme en Python ou JavaScript). Pour la différence, c’est `<>` (la forme standard) ou `!=` (acceptée par la plupart des SGBD).

#### Texte vs nombre : guillemets ou pas ?

Le **texte** se met entre **guillemets simples** `'...'`. Les **nombres** s’écrivent **sans guillemets**.

```sql
SELECT * FROM readers WHERE city = 'Paris';            -- texte → quotes
SELECT * FROM books WHERE publication_year >= 2000;    -- nombre → pas de quotes
SELECT * FROM books WHERE id = 5;                      -- nombre → pas de quotes
```

> **Important :** SQL utilise les **guillemets simples** `'...'` pour le texte. Les guillemets doubles `"..."` ont une autre signification (noms d’identifiants) — ne les utilise pas pour du texte, ou tu auras des erreurs surprenantes.

#### Les apostrophes dans le texte

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

### Très utile en pratique

#### `WHERE` sur des nombres et des dates

```sql
-- Livres publiés au 21e siècle
SELECT * FROM books WHERE publication_year >= 2000;

-- Lecteurs inscrits depuis 2025
SELECT * FROM readers WHERE registration_date >= '2025-01-01';
```

> **Note SQLite :** SQLite stocke les dates comme du **texte** au format `'YYYY-MM-DD'`. Tant que tes dates respectent ce format, les comparaisons `<`, `>`, `=` fonctionnent comme avec des nombres.

#### Filtrer sur la sortie de DB Browser

Quand tu cliques sur “Exécuter”, DB Browser affiche le résultat sous la requête. Si le résultat est long, fais défiler. Le bas de l’écran indique le nombre de lignes retournées — pratique pour vérifier qu’on a bien ce qu’on attend.

### ❌ Erreur classique

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

### 💡 Exercices

1. Affiche les livres publiés avant 1950.
1. Affiche les lecteurs habitant à Lyon.
1. Affiche les emprunts dont le statut est `'late'`.

### ✅ Tu sais maintenant…

- Filtrer les lignes avec `WHERE`
- Les opérateurs : `=`, `<>`, `!=`, `<`, `>`, `<=`, `>=`
- Texte entre guillemets simples, nombres sans guillemets
- Échapper une apostrophe en la doublant (`'L''Étranger'`)

-----


## Chapitre 8 — Conditions multiples : AND, OR, NOT

### Le minimum à savoir

#### Combiner des conditions avec `AND`

`AND` impose que **toutes** les conditions soient vraies :

```sql
SELECT *
FROM books
WHERE publication_year >= 2000
  AND category_id = 1;
```

→ Les livres publiés depuis 2000 **ET** de catégorie 1 (Roman).

#### Au moins une condition avec `OR`

`OR` accepte une ligne si **au moins une** des conditions est vraie :

```sql
SELECT *
FROM readers
WHERE city = 'Paris'
   OR city = 'Lyon';
```

→ Les lecteurs qui habitent Paris **OU** Lyon.

#### Inverser avec `NOT`

`NOT` inverse une condition :

```sql
SELECT *
FROM loans
WHERE NOT status = 'returned';
```

→ Les emprunts qui ne sont **pas** retournés (donc en cours ou en retard).

#### La priorité : parenthèses obligatoires si tu mélanges AND et OR

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

### Très utile en pratique

#### Quand `OR` est répétitif, utilise `IN` (Ch.9)

Tu verras au prochain chapitre que :

```sql
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille'
```

s’écrit plus proprement avec :

```sql
WHERE city IN ('Paris', 'Lyon', 'Marseille')
```

### ❌ Erreur classique

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

### 💡 Exercices

1. Affiche les livres de catégorie Roman (id=1) **et** publiés avant 1950.
1. Affiche les lecteurs habitant à Paris, Lyon ou Bordeaux.
1. Affiche les emprunts qui ne sont pas en retard (`status` différent de `'late'`).

### ✅ Tu sais maintenant…

- Combiner des conditions avec `AND` (toutes vraies)
- Accepter avec `OR` (au moins une vraie)
- Inverser avec `NOT`
- Utiliser des parenthèses dès que tu mélanges `AND` et `OR`

-----


## Chapitre 9 — Filtres utiles : LIKE, IN, BETWEEN, NULL

### Le minimum à savoir

#### Recherche par motif avec `LIKE`

`LIKE` permet de chercher un motif dans du texte. Deux caractères spéciaux :

|Caractère|Signification                                      |
|---------|---------------------------------------------------|
|`%`      |N’importe quelle séquence de caractères (même vide)|
|`_`      |Exactement un caractère                            |

Exemples :

```sql
-- Tous les livres dont le titre contient "Harry"
SELECT * FROM books WHERE title LIKE '%Harry%';

-- Tous les emails se terminant par "@example.com"
SELECT * FROM readers WHERE email LIKE '%@example.com';

-- Tous les noms commençant par "Mar"
SELECT * FROM readers WHERE last_name LIKE 'Mar%';

-- Mots de 4 lettres commençant par "L"
SELECT * FROM books WHERE title LIKE 'L___';
```

> **Note :** par défaut, `LIKE` est **insensible à la casse** dans SQLite (`'PARIS'` = `'Paris'`). Dans PostgreSQL, c’est sensible — utilise `ILIKE` pour insensibiliser.

#### Liste de valeurs avec `IN`

Plus propre que des `OR` à répétition :

```sql
-- Avec OR (verbeux)
SELECT * FROM readers
WHERE city = 'Paris' OR city = 'Lyon' OR city = 'Marseille';

-- Avec IN (concis)
SELECT * FROM readers
WHERE city IN ('Paris', 'Lyon', 'Marseille');
```

L’inverse existe aussi : `NOT IN` :

```sql
SELECT * FROM readers
WHERE city NOT IN ('Paris', 'Lyon');
-- → toutes les villes SAUF Paris et Lyon
```

#### Plage de valeurs avec `BETWEEN`

```sql
-- Livres publiés entre 1990 et 2000 (inclus)
SELECT * FROM books
WHERE publication_year BETWEEN 1990 AND 2000;
```

`BETWEEN a AND b` est **inclusif** des deux bornes. C’est équivalent à :

```sql
WHERE publication_year >= 1990 AND publication_year <= 2000
```

#### Le cas particulier : `NULL`

`NULL` représente l’**absence de valeur**. Ce n’est ni `0`, ni la chaîne vide `''` — c’est “rien”.

**Important :** on ne peut **pas** comparer `NULL` avec `=` :

```sql
SELECT * FROM readers WHERE phone = NULL;        -- ❌ ne renvoie jamais rien
SELECT * FROM readers WHERE phone IS NULL;       -- ✅ correct

SELECT * FROM readers WHERE phone IS NOT NULL;   -- ✅ ceux qui ont un téléphone
```

> **À retenir :** `NULL` n’est égal à rien — pas même à lui-même. Utilise toujours `IS NULL` ou `IS NOT NULL`. C’est l’une des erreurs les plus fréquentes en SQL.

> **📋 FIL ROUGE — Épisode 8**
> 
> La directrice : “Combien de lecteurs n’ont pas de téléphone enregistré ? Il faut leur demander à leur prochaine visite.” Nora :
> 
> ```sql
> SELECT first_name, last_name FROM readers WHERE phone IS NULL;
> ```
> 
> 4 lecteurs. Elle imprime la liste. Si elle avait écrit `WHERE phone = NULL`, elle aurait obtenu 0 résultats — et conclu à tort que tous les lecteurs ont un téléphone.

### Très utile en pratique

#### `LIKE` avec recherche multilingue

`LIKE '%harry%'` est insensible à la casse en SQLite par défaut, mais peut ne pas trouver `'Harry'` dans certains environnements. Pour être sûr :

```sql
SELECT * FROM books WHERE LOWER(title) LIKE '%harry%';
```

`LOWER()` met le texte en minuscules — la comparaison devient garantie insensible à la casse.

#### `NULL` et opérations

Toute opération impliquant `NULL` produit `NULL` :

```sql
SELECT 5 + NULL;    -- → NULL
SELECT 'a' || NULL; -- → NULL
```

C’est pour ça que `WHERE col = NULL` ne marche pas : `col = NULL` produit `NULL`, pas `TRUE` — et `WHERE` ne garde que les `TRUE`.

### ❌ Erreur classique

```sql
-- Comparer NULL avec =
WHERE phone = NULL;          -- ❌ ne renvoie rien
WHERE phone IS NULL;         -- ✅

-- Confondre chaîne vide et NULL
WHERE email = '';            -- ne trouve QUE les emails vides (chaîne de longueur 0)
WHERE email IS NULL;         -- trouve les emails non renseignés (rien du tout)

-- Les deux peuvent coexister dans une base mal nettoyée :
-- email = '' (vide) ≠ email IS NULL (absent)
```

### 💡 Exercices

1. Affiche les livres dont le titre contient “Potter”.
1. Affiche les lecteurs habitant à Paris, Lyon **ou** Bordeaux (avec `IN`).
1. Affiche les livres publiés entre 1900 et 1950 (avec `BETWEEN`).
1. Affiche les lecteurs qui n’ont pas d’email.

### ✅ Tu sais maintenant…

- `LIKE '%motif%'` pour chercher un motif dans du texte
- `IN (...)` pour une liste de valeurs
- `BETWEEN a AND b` pour une plage (inclusive)
- `IS NULL` / `IS NOT NULL` pour les valeurs absentes
- `NULL` ≠ chaîne vide `''` ≠ zéro `0`

-----


## Chapitre 10 — Trier, limiter et paginer

### Le minimum à savoir

#### Trier avec `ORDER BY`

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

#### Trier sur plusieurs colonnes

Quand plusieurs lignes ont la même valeur sur la première colonne, on trie par la suivante :

```sql
-- D'abord par catégorie (alphabétique), puis par année (du plus récent)
SELECT title, category_id, publication_year
FROM books
ORDER BY category_id ASC, publication_year DESC;
```

#### Limiter le nombre de résultats avec `LIMIT`

Pour ne récupérer que les N premières lignes :

```sql
-- Les 5 lecteurs inscrits le plus récemment
SELECT * FROM readers
ORDER BY registration_date DESC
LIMIT 5;
```

> **À retenir :** `LIMIT` se met **toujours à la fin** de la requête, après `ORDER BY`. Sans `ORDER BY`, `LIMIT 5` te donne 5 lignes “au hasard” — pas forcément les plus récentes.

#### Paginer avec `LIMIT` + `OFFSET`

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

### Très utile en pratique

#### Trier par plusieurs critères avec sens différent

```sql
-- Par catégorie alphabétique, puis par année DÉCROISSANTE dans chaque catégorie
ORDER BY category_id ASC, publication_year DESC;
```

C’est très utile pour des rapports structurés — d’abord regroupé, puis trié finement à l’intérieur.

#### Trier sur un alias

Tu peux trier sur le nom donné par `AS` :

```sql
SELECT title, 2026 - publication_year AS age_du_livre
FROM books
ORDER BY age_du_livre DESC;
```

### ❌ Erreur classique

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

### 💡 Exercices

1. Affiche tous les livres triés par année du plus ancien au plus récent.
1. Affiche les 3 livres les plus récents.
1. Affiche les 5 lecteurs habitant à Paris, par ordre alphabétique sur le nom.
1. Affiche les pages 2 et 3 (10 lecteurs par page) triés par date d’inscription.

### ✅ Tu sais maintenant…

- Trier avec `ORDER BY col ASC` ou `ORDER BY col DESC`
- Trier sur plusieurs colonnes
- Limiter le nombre de résultats avec `LIMIT`
- Paginer avec `LIMIT` + `OFFSET`
- Toujours combiner `LIMIT` avec un `ORDER BY` explicite

-----
