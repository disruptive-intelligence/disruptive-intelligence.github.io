---
title: Chapitre 32 — Synthèse et boîte à outils SQL
source: IT/07 Scripting & programmation/Langages/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VIII — Synthèse
  - index.md
---

## L’ordre d’écriture d’une requête

Quand tu écris une requête, l’ordre est :

```sql
SELECT     -- 1. Quelles colonnes ?
FROM       -- 2. Quelle table ?
JOIN       -- 3. Quelles tables croiser ?
WHERE      -- 4. Quelles lignes filtrer (avant agrégation) ?
GROUP BY   -- 5. Comment regrouper ?
HAVING     -- 6. Quels groupes garder ?
ORDER BY   -- 7. Comment trier ?
LIMIT      -- 8. Combien de lignes ?
```


## L’ordre logique d’exécution (interne)

Le moteur SQL **n’exécute pas** les clauses dans l’ordre où tu les écris. Il les exécute dans cet ordre logique :

```
FROM / JOIN  →  WHERE  →  GROUP BY  →  HAVING  →  SELECT  →  ORDER BY  →  LIMIT
```


C’est important à comprendre pour deux raisons :

1. Les **alias définis dans `SELECT`** ne peuvent pas être utilisés dans `WHERE` (le `WHERE` est exécuté avant le `SELECT`). Mais ils peuvent être utilisés dans `ORDER BY`.
1. `WHERE` filtre **avant** agrégation, `HAVING` filtre **après**. C’est ce qu’on a vu au Ch.14.

> **À retenir :** ce n’est pas exactement l’ordre d’exécution interne du moteur (qui peut optimiser), mais c’est le **modèle mental** correct pour comprendre ce qui se passe.

## Les commandes SQL essentielles

```
-- Lecture
SELECT, FROM, WHERE, AND, OR, NOT
DISTINCT, AS
LIKE, IN, BETWEEN, IS NULL, IS NOT NULL
ORDER BY, ASC, DESC, LIMIT, OFFSET

-- Calcul et regroupement
COUNT, SUM, AVG, MIN, MAX
GROUP BY, HAVING

-- Jointures
INNER JOIN, LEFT JOIN, ON

-- Modification
INSERT INTO ... VALUES
UPDATE ... SET ... WHERE
DELETE FROM ... WHERE

-- Transactions
BEGIN, COMMIT, ROLLBACK

-- Structure
CREATE TABLE, DROP TABLE, ALTER TABLE
CREATE INDEX, CREATE VIEW
PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT
```


## Les erreurs fréquentes (synthèse)

|Erreur                       |Symptôme                      |Solution                                |
|-----------------------------|------------------------------|----------------------------------------|
|Oublier `WHERE` dans `UPDATE`|Toute la table modifiée       |Faire un `SELECT` avant                 |
|Oublier `WHERE` dans `DELETE`|Toute la table vidée          |Faire un `SELECT` avant + transaction   |
|`WHERE col = NULL`           |Aucun résultat                |Utiliser `IS NULL`                      |
|Confondre `WHERE` et `HAVING`|Erreur “aggregate not allowed”|`WHERE` avant agrégation, `HAVING` après|
|`SELECT *` après jointure    |Doublons silencieux           |`COUNT(DISTINCT)` ou colonnes explicites|
|Oublier `ON`                 |Produit cartésien             |Toujours `INNER JOIN ... ON ...`        |
|Concatener entrée utilisateur|Injection SQL                 |Utiliser `?` et paramètres              |

## Quand utiliser quelle clause ?

```
J'ai besoin de…                          Outil
────────────────────────────────────     ──────────────
Lire des lignes                          SELECT
Filtrer ces lignes                       WHERE
Combiner deux tables                     INNER JOIN
Garder les lignes même sans match        LEFT JOIN
Trouver "ce qui n'a pas de match"        LEFT JOIN ... WHERE ... IS NULL
Compter par catégorie                    GROUP BY + COUNT(*)
Filtrer ces groupes                      HAVING
Trier le résultat                        ORDER BY
Limiter le nombre de lignes              LIMIT
Pagination                               LIMIT + OFFSET
Recherche par motif                      LIKE '%motif%'
Plage de valeurs                         BETWEEN a AND b
Liste de valeurs                         IN (...)
Valeur absente                           IS NULL
Modifier des données                     UPDATE ... WHERE + SELECT préalable
Supprimer des données                    DELETE ... WHERE + SELECT préalable + transaction
Sécuriser un bloc de modifications       BEGIN ... COMMIT (ou ROLLBACK)
Accélérer une recherche                  CREATE INDEX
Simplifier des requêtes complexes        CREATE VIEW
```


## La suite logique

|Cours                                         |Quand le faire                                       |
|----------------------------------------------|-----------------------------------------------------|
|**PostgreSQL** ou **MySQL**                   |Pour passer à un SGBD professionnel (web, entreprise)|
|**Modélisation avancée**                      |Quand tu conçois des bases de plus de 10 tables      |
|**Performance et optimisation**               |Quand les requêtes deviennent lentes                 |
|**NoSQL** (MongoDB, Redis)                    |Pour comprendre les alternatives au relationnel      |
|**Data Engineering** (Spark, dbt)             |Pour le big data et les pipelines analytiques        |
|**Sécurité offensive** (SQL injection avancée)|Si tu vas vers le pentest                            |

-----
