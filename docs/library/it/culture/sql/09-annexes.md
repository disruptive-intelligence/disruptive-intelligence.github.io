---
title: Annexes
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - index.md
---

-----

### Annexe A — Glossaire complet

|Terme                          |Définition                                                                                |
|-------------------------------|------------------------------------------------------------------------------------------|
|**ACID**                       |Propriétés des transactions : Atomicité, Cohérence, Isolation, Durabilité                 |
|**Agrégation**                 |Fonction qui calcule une valeur unique sur un groupe (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)|
|**Alias**                      |Nom temporaire donné à une colonne ou une table avec `AS`                                 |
|**Base de données**            |Système organisé de stockage et de gestion de données                                     |
|**Clé étrangère (FOREIGN KEY)**|Colonne qui pointe vers la clé primaire d’une autre table                                 |
|**Clé primaire (PRIMARY KEY)** |Colonne(s) qui identifie(nt) de façon unique chaque ligne                                 |
|**Colonne**                    |Champ d’une table (équivalent : attribut, propriété)                                      |
|**Contrainte**                 |Règle imposée à une colonne (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`)                |
|**Cursor (curseur)**           |Objet qui exécute des requêtes en Python (et autres langages)                             |
|**DDL**                        |Data Definition Language : `CREATE`, `ALTER`, `DROP`                                      |
|**DML**                        |Data Manipulation Language : `SELECT`, `INSERT`, `UPDATE`, `DELETE`                       |
|**Dialecte**                   |Variante de SQL propre à un SGBD                                                          |
|**Entité**                     |Concept du monde réel modélisé en table                                                   |
|**Index**                      |Structure annexe qui accélère les recherches                                              |
|**Injection SQL**              |Attaque exploitant la concaténation d’entrée utilisateur                                  |
|**Jointure (JOIN)**            |Opération qui combine les données de plusieurs tables                                     |
|**Ligne (row)**                |Enregistrement dans une table                                                             |
|**NULL**                       |Absence de valeur (différent de zéro et de chaîne vide)                                   |
|**OFFSET**                     |Saut d’un nombre de lignes pour la pagination                                             |
|**Paramètre (placeholder)**    |`?` ou `:nom` dans une requête, remplacé par une valeur sécurisée                         |
|**Relation**                   |Lien entre deux tables (1-N ou N-N)                                                       |
|**Requête**                    |Instruction SQL envoyée au moteur                                                         |
|**Requête préparée**           |Requête avec paramètres, protégée contre l’injection                                      |
|**Schéma**                     |Structure de la base : tables, colonnes, contraintes                                      |
|**SGBD**                       |Système de Gestion de Base de Données (SQLite, PostgreSQL, MySQL…)                        |
|**SQL**                        |Structured Query Language — le langage standard                                           |
|**SQLite**                     |SGBD léger, embarqué, basé sur un fichier                                                 |
|**Table**                      |Tableau structuré de données                                                              |
|**Table d’association**        |Table intermédiaire pour modéliser une relation N-N                                       |
|**Transaction**                |Bloc de modifications validable (`COMMIT`) ou annulable (`ROLLBACK`)                      |
|**Vue (VIEW)**                 |Requête enregistrée utilisable comme une table                                            |

-----

### Annexe B — Commandes SQL essentielles

#### Lecture

```sql
SELECT col1, col2 FROM table;
SELECT * FROM table;
SELECT DISTINCT col FROM table;
SELECT col AS alias FROM table;

-- Filtrage
WHERE col = valeur
WHERE col <> valeur, !=
WHERE col > / < / >= / <=
WHERE col LIKE '%motif%'
WHERE col IN (val1, val2, val3)
WHERE col BETWEEN a AND b
WHERE col IS NULL / IS NOT NULL
WHERE cond1 AND cond2
WHERE cond1 OR cond2
WHERE NOT cond

-- Tri et limite
ORDER BY col ASC / DESC
LIMIT n
LIMIT n OFFSET m
```


#### Agrégation

```sql
SELECT COUNT(*) FROM table;
SELECT COUNT(col) FROM table;        -- exclut les NULL
SELECT COUNT(DISTINCT col) FROM table;
SELECT SUM(col), AVG(col), MIN(col), MAX(col) FROM table;

GROUP BY col
HAVING agrégation cond
```


#### Jointures

```sql
FROM table1 INNER JOIN table2 ON table1.col = table2.col
FROM table1 LEFT JOIN table2 ON ...
-- Pour trouver les "orphelins" :
FROM t1 LEFT JOIN t2 ON ... WHERE t2.id IS NULL
```


#### Modification

```sql
INSERT INTO table (col1, col2) VALUES (val1, val2);
INSERT INTO table (col1, col2) VALUES (a, b), (c, d), (e, f);

UPDATE table SET col = val WHERE cond;          -- TOUJOURS avec WHERE
DELETE FROM table WHERE cond;                    -- TOUJOURS avec WHERE
```


#### Transactions

```sql
BEGIN;
-- modifications
COMMIT;     -- ou ROLLBACK;
```


#### Structure

```sql
CREATE TABLE nom (
    id INTEGER PRIMARY KEY,
    col TEXT NOT NULL,
    autre TEXT UNIQUE,
    valeur INTEGER DEFAULT 0,
    FOREIGN KEY (col) REFERENCES autre_table(id),
    CHECK (cond)
);

DROP TABLE nom;
ALTER TABLE nom ADD COLUMN col TYPE;

CREATE INDEX idx_nom ON table(col);
DROP INDEX idx_nom;

CREATE VIEW vue AS SELECT ...;
DROP VIEW vue;
```


-----

### Annexe C — Fonctions SQLite utiles

#### Texte

```sql
UPPER('alice')              -- 'ALICE'
LOWER('ALICE')              -- 'alice'
LENGTH('Alice')             -- 5
TRIM('  abc  ')             -- 'abc'
SUBSTR('Bonjour', 1, 3)     -- 'Bon'
REPLACE('abc', 'b', 'B')    -- 'aBc'

-- Concaténation (SQLite/PostgreSQL)
'a' || 'b'                  -- 'ab'
COALESCE(NULL, 'défaut')    -- 'défaut' (si premier est NULL)
```


#### Dates

```sql
DATE('now')                 -- date du jour : '2026-05-03'
DATETIME('now')             -- date + heure
strftime('%Y', date)        -- année
strftime('%Y-%m', date)     -- année-mois
strftime('%H:%M', heure)    -- heure-minute
julianday('now')            -- nombre de jours depuis le 24 nov 4714 av. J.-C.
julianday('now') - julianday(date)    -- différence en jours
DATE('now', '-7 days')      -- il y a 7 jours
DATE('now', '+1 month')     -- dans 1 mois
```


#### Numériques

```sql
ABS(x)                       -- valeur absolue
ROUND(3.14159, 2)            -- 3.14
MAX(a, b)                    -- max de 2 valeurs (différent de l'agrégation MAX !)
MIN(a, b)                    -- idem pour min
RANDOM()                     -- nombre aléatoire
```


#### Conditionnel

```sql
CASE
    WHEN cond1 THEN val1
    WHEN cond2 THEN val2
    ELSE valeur_par_defaut
END

COALESCE(col1, col2, 'défaut')   -- premier non-NULL
NULLIF(col, valeur)              -- NULL si col = valeur, sinon col
```


-----

### Annexe D — Différences SQLite / PostgreSQL / MySQL

|Tâche                       |SQLite                |PostgreSQL                    |MySQL                       |
|----------------------------|----------------------|------------------------------|----------------------------|
|Auto-incrément              |`INTEGER PRIMARY KEY` |`SERIAL` ou `IDENTITY`        |`AUTO_INCREMENT`            |
|Concaténation               |`'a' || 'b'`          |`'a' || 'b'`                  |`CONCAT('a', 'b')`          |
|Date du jour                |`DATE('now')`         |`CURRENT_DATE`                |`CURDATE()`                 |
|Extraire année              |`strftime('%Y', date)`|`EXTRACT(YEAR FROM date)`     |`YEAR(date)`                |
|Booléen                     |`INTEGER` (0/1)       |`BOOLEAN` natif               |`BOOLEAN` (alias de TINYINT)|
|Texte limité                |`TEXT` (illimité)     |`VARCHAR(50)`                 |`VARCHAR(50)`               |
|Insensible à la casse (LIKE)|par défaut            |`ILIKE`                       |par défaut                  |
|`LIMIT` + `OFFSET`          |`LIMIT 10 OFFSET 20`  |idem (et `OFFSET 20 LIMIT 10`)|idem                        |
|Méta-commandes              |`.tables`, `.schema`  |`\dt`, `\d`                   |`SHOW TABLES`, `DESCRIBE`   |


> **À retenir :** 90% du SQL est identique. Les 10% qui varient concernent surtout : auto-incrément, fonctions de date, concaténation, et certaines fonctions de texte. Quand tu changes de SGBD, c’est ce que tu adaptes.

-----

### Annexe E — Pièges classiques

|Piège                                   |Exemple incorrect                    |Correction                                                        |
|----------------------------------------|-------------------------------------|------------------------------------------------------------------|
|Oublier `WHERE` dans `UPDATE`           |`UPDATE readers SET city = 'Paris';` |`UPDATE readers SET city = 'Paris' WHERE id = 1;`                 |
|Oublier `WHERE` dans `DELETE`           |`DELETE FROM readers;`               |`DELETE FROM readers WHERE id = 1;`                               |
|Confondre `NULL` et chaîne vide         |`WHERE col = ''`                     |`WHERE col = ''` (chaîne vide) **ou** `WHERE col IS NULL` (absent)|
|`= NULL` au lieu de `IS NULL`           |`WHERE col = NULL`                   |`WHERE col IS NULL`                                               |
|`WHERE` agrégation                      |`WHERE COUNT(*) > 5`                 |`HAVING COUNT(*) > 5`                                             |
|`COUNT(col)` ne compte pas les NULL     |`COUNT(email)` peut être < `COUNT(*)`|C’est normal, c’est même utile                                    |
|Jointure sans `ON`                      |`SELECT * FROM a, b`                 |`SELECT * FROM a INNER JOIN b ON a.id = b.a_id`                   |
|Doublons après JOIN N-N                 |`COUNT(*)` après `JOIN book_authors` |`COUNT(DISTINCT b.id)`                                            |
|`SELECT *` partout                      |Risqué, perd en clarté               |Lister les colonnes explicitement                                 |
|Pas de transaction sur opération risquée|`UPDATE` massif sans `BEGIN`         |`BEGIN; UPDATE...; COMMIT;`                                       |
|Concatener entrée utilisateur           |`... + user_input + ...`             |`... ? ...` avec paramètres                                       |

-----

### Annexe F — Requêtes types (et solutions du Skills Assessment)

#### Solutions du Ch.31

**Q1 — Combien y a-t-il de lecteurs ?**

```sql
SELECT COUNT(*) FROM readers;
```


**Q2 — Les 10 derniers lecteurs inscrits**

```sql
SELECT first_name, last_name, registration_date
FROM readers
ORDER BY registration_date DESC
LIMIT 10;
```


**Q3 — Livres jamais empruntés**

```sql
SELECT b.title
FROM books AS b
LEFT JOIN loans AS l ON b.id = l.book_id
WHERE l.id IS NULL;
```


**Q4 — Top 5 lecteurs**

```sql
SELECT r.first_name, r.last_name, COUNT(*) AS nb
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
GROUP BY r.id, r.first_name, r.last_name
ORDER BY nb DESC
LIMIT 5;
```


**Q5 — Lecteurs avec emprunts en retard**

```sql
SELECT r.first_name, r.last_name, b.title
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status = 'late';
```


**Q6 — Livres par catégorie**

```sql
SELECT c.name, COUNT(*) AS nb
FROM books AS b
INNER JOIN categories AS c ON b.category_id = c.id
GROUP BY c.name
ORDER BY nb DESC;
```


**Q7 — Auteur le plus emprunté**

```sql
SELECT a.name, COUNT(*) AS nb_emprunts
FROM authors AS a
INNER JOIN book_authors AS ba ON a.id = ba.author_id
INNER JOIN books AS b ON ba.book_id = b.id
INNER JOIN loans AS l ON b.id = l.book_id
GROUP BY a.id, a.name
ORDER BY nb_emprunts DESC
LIMIT 1;
```


**Q8 — Lecteurs n’ayant jamais emprunté**

```sql
SELECT r.first_name, r.last_name
FROM readers AS r
LEFT JOIN loans AS l ON r.id = l.reader_id
WHERE l.id IS NULL;
```


**Q9 — Emails en double**

```sql
SELECT email, COUNT(*) AS nb
FROM readers
WHERE email IS NOT NULL
GROUP BY email
HAVING nb > 1;
```


**Q10 — Comptes avec le plus d’échecs**

```sql
-- Version avec jointure : affiche aussi les comptes à 0 échec (rapport plus complet)
SELECT s.username, s.full_name, COUNT(le.id) AS nb_echecs
FROM staff_users AS s
LEFT JOIN login_events AS le
       ON s.username = le.username
      AND le.success = 0
GROUP BY s.id, s.username, s.full_name
ORDER BY nb_echecs DESC;

-- Version sans jointure : ne liste que les comptes ayant au moins un échec
-- (et inclut aussi les tentatives sur des comptes inexistants)
SELECT username, COUNT(*) AS nb_echecs
FROM login_events
WHERE success = 0
GROUP BY username
ORDER BY nb_echecs DESC;
```


> **Pourquoi deux versions ?** La première donne un rapport propre pour la directrice (tous les comptes connus, avec leur compteur d’échecs même à zéro). La seconde sert à l’analyse cyber pure — elle révèle aussi les tentatives sur des comptes **qui n’existent pas** dans `staff_users` (typique d’un attaquant qui essaie des noms d’utilisateurs au hasard).

**Q11 — Livres empruntés au moins 2 fois**

```sql
SELECT b.title, COUNT(*) AS nb
FROM books AS b
INNER JOIN loans AS l ON b.id = l.book_id
GROUP BY b.id, b.title
HAVING nb >= 2;
```


**Q12 — Activité d’Alice (id=1)**

```sql
SELECT
    r.first_name || ' ' || r.last_name AS lecteur,
    COUNT(*) AS total,
    SUM(CASE WHEN l.status = 'returned' THEN 1 ELSE 0 END) AS retournes,
    SUM(CASE WHEN l.status = 'borrowed' THEN 1 ELSE 0 END) AS en_cours,
    SUM(CASE WHEN l.status = 'late' THEN 1 ELSE 0 END) AS en_retard
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE r.id = 1
GROUP BY r.id, r.first_name, r.last_name;
```


-----

### Annexe G — SQL pour la cybersécurité

Le SQL est un outil **central** en cybersécurité défensive — pour analyser les logs, détecter les anomalies, comprendre le comportement utilisateur. Voici quelques patterns utiles.

#### Détecter une attaque par brute-force

```sql
-- Comptes ayant subi 5+ échecs depuis la même IP
SELECT username, ip_address, COUNT(*) AS nb_echecs,
       MIN(event_time) AS premier, MAX(event_time) AS dernier
FROM login_events
WHERE success = 0
GROUP BY username, ip_address
HAVING nb_echecs >= 5
ORDER BY nb_echecs DESC;
```


#### Repérer un pattern brute-force réussi

```sql
-- Comptes avec beaucoup d'échecs ET au moins une réussite depuis la même IP
SELECT username, ip_address,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs,
       SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) AS nb_succes
FROM login_events
GROUP BY username, ip_address
HAVING nb_echecs >= 5 AND nb_succes >= 1;
```


#### Détecter les comptes inactifs (à désactiver)

```sql
-- Comptes du personnel sans connexion depuis 90 jours
SELECT s.username, s.full_name, MAX(le.event_time) AS derniere_connexion
FROM staff_users AS s
LEFT JOIN login_events AS le ON s.username = le.username AND le.success = 1
GROUP BY s.id
HAVING derniere_connexion IS NULL
   OR julianday('now') - julianday(derniere_connexion) > 90;
```


#### Connexions à des heures inhabituelles

```sql
-- Connexions réussies entre 22h et 6h (potentiellement suspect)
SELECT username, event_time, ip_address
FROM login_events
WHERE success = 1
  AND (CAST(strftime('%H', event_time) AS INTEGER) >= 22
       OR CAST(strftime('%H', event_time) AS INTEGER) < 6);
```


#### Détection d’utilisateur dupliqué (compte fantôme)

```sql
-- Lecteurs avec le même nom complet (et donc potentiellement doublonnés)
SELECT first_name, last_name, COUNT(*) AS nb
FROM readers
GROUP BY first_name, last_name
HAVING nb > 1;
```


#### Compter les événements par fenêtre temporelle

```sql
-- Nombre de connexions par jour
SELECT DATE(event_time) AS jour, COUNT(*) AS nb_evenements,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs
FROM login_events
GROUP BY DATE(event_time)
ORDER BY jour DESC;
```


> **Ouverture :** ces requêtes sont la base de tout système de **SIEM** (Security Information and Event Management). Les outils comme Splunk, Elastic SIEM, ou QRadar utilisent du SQL (ou des langages similaires) pour détecter les anomalies en temps réel.

-----

### Annexe H — Script de la base de démo

Le script complet pour recréer la base `bibliotheque.db` est celui présenté au **Chapitre 4**. Tu peux le copier-coller dans DB Browser → “Exécuter le SQL”, puis sauvegarder.

**Rappel des 8 tables :**

1. `categories` — 6 catégories de livres
1. `authors` — 11 auteurs (dont 1 sans livre dans la base, pour les exercices `LEFT JOIN`)
1. `books` — 15 livres
1. `book_authors` — table d’association N-N (16 lignes ; un livre coécrit par 2 auteurs, pour illustrer le piège des doublons)
1. `readers` — 15 lecteurs (avec deux Alice Martin partageant le même email et 4 sans téléphone)
1. `loans` — 20 emprunts (mix returned, borrowed, late)
1. `staff_users` — 5 comptes du personnel (1 inactif, 1 compte ‘admin’ dangereux)
1. `login_events` — 17 événements (avec une attaque brute-force réussie sur ‘admin’ : 10 échecs + 1 succès)

-----


## Conclusion

Tu maîtrises maintenant les fondamentaux de SQL et des bases de données relationnelles :

- **Comprendre** ce qu’est une base, comment elle est structurée (Ch.1-4)
- **Lire** des données avec `SELECT`, filtrer, trier, limiter (Ch.5-10)
- **Calculer** et regrouper avec les agrégations (Ch.11-14)
- **Croiser** les tables avec les jointures (Ch.15-19)
- **Modifier** les données avec prudence — `INSERT`, `UPDATE`, `DELETE`, transactions (Ch.20-23)
- **Créer** une table avec contraintes (Ch.24-26)
- **Bonus** : bonnes pratiques, vues, index, sécurité, Python (Ch.27-30)

**La progression naturelle :**

- Pratique sur des bases plus grandes (Kaggle, datasets publics)
- Passe à PostgreSQL pour un environnement professionnel
- Apprends la modélisation poussée pour concevoir des bases de 20+ tables
- Explore le data engineering (Spark, dbt, Airflow)
- Va voir le NoSQL pour comprendre les alternatives

**Le SQL est l’une des compétences les plus durables en informatique.** Le langage a 50 ans, il sera encore là dans 30. Tu viens d’investir dans une compétence qui ne se démode pas.

Bon voyage dans le monde des données !
