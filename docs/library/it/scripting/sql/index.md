---
title: SQL
source: IT/Culture/SQL.md
---

*De zéro à l’interrogation de données — Guide pour débutant absolu*

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais ouvert une base de données de sa vie.
> Tout ce dont tu as besoin, c’est un ordinateur (Windows, Mac ou Linux) et l’envie d’apprendre.

-----

### Ce que ce cours est — et ce qu’il n’est pas

Ce cours t’apprend à **comprendre et utiliser** une base de données relationnelle avec SQL.

Tu apprendras à :

- comprendre ce qu’est une base de données et pourquoi on en utilise
- lire les données d’une base avec `SELECT`
- filtrer, trier, limiter les résultats
- croiser plusieurs tables avec des jointures
- faire des statistiques (`COUNT`, `SUM`, `AVG`, `GROUP BY`)
- insérer, modifier, supprimer des données avec prudence
- créer une table simple avec ses contraintes
- comprendre les transactions et l’intégrité des données
- repérer et éviter les erreurs SQL fréquentes
- avoir les bases utiles pour le développement, la data, l’administration et la cybersécurité

Ce cours **n’est pas** :

- un cours d’administration de base de données (DBA)
- un cours de modélisation avancée (formes normales en profondeur, UML)
- un cours d’optimisation SQL (requêtes complexes, plans d’exécution avancés)
- un cours sur PostgreSQL, MySQL ou Oracle en profondeur
- un cours NoSQL (MongoDB, Redis, etc.)
- un cours offensif sur l’injection SQL (la sécurité est traitée en **défensif** uniquement)

-----

### Guide de lecture

|Section                   |Niveau           |Objectif                                           |
|--------------------------|-----------------|---------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel      |Ce qu’il faut retenir pour ne pas être perdu       |
|**Très utile en pratique**|🟡 Bon à connaître|Ce qui te rend opérationnel pour de vraies requêtes|
|**Bonus**                 |🔴 Avancé         |Pour aller plus loin — tu peux y revenir plus tard |

#### Parcours recommandés

|Parcours                      |Chapitres         |Objectif                                                                      |
|------------------------------|------------------|------------------------------------------------------------------------------|
|**🎯 Découverte / entretien**  |Ch.1-19 + Ch.32   |Comprendre SQL, savoir lire et croiser des données, être crédible en entretien|
|**🔧 Opérationnel (data, dev)**|Ch.1-26 + Ch.31-32|Savoir aussi modifier et structurer des données                               |
|**🚀 Complet**                 |Tout              |Bonnes pratiques, index, sécurité, Python — pour le terrain                   |


> **Important :** la Partie VII (Ch.27-30) est marquée **Bonus / Pour aller plus loin**. Tu peux finir le cœur du cours (Ch.1-26 + Skills Assessment) sans elle. Ces chapitres viennent enrichir ta pratique, pas la conditionner.

-----

### Glossaire — Les mots à connaître

Reviens ici chaque fois qu’un terme te semble flou.

|Terme               |Définition simple                                                                              |
|--------------------|-----------------------------------------------------------------------------------------------|
|**Base de données** |Un système organisé de stockage et de gestion de données                                       |
|**SGBD**            |Système de Gestion de Base de Données — le moteur qui exécute SQL (SQLite, PostgreSQL, MySQL…) |
|**SQL**             |Le langage standard pour interroger et manipuler des bases de données relationnelles           |
|**Table**           |Un tableau de données — l’équivalent d’une feuille Excel structurée                            |
|**Ligne (row)**     |Un enregistrement dans une table (un livre, un lecteur, un emprunt)                            |
|**Colonne (column)**|Un champ dans une table (le titre d’un livre, la ville d’un lecteur)                           |
|**Schéma**          |La structure de la base : quelles tables, quelles colonnes, quels types                        |
|**Clé primaire**    |Une colonne qui identifie de manière unique chaque ligne d’une table                           |
|**Clé étrangère**   |Une colonne qui pointe vers la clé primaire d’une autre table — crée une relation              |
|**Relation**        |Le lien entre deux tables (un emprunt est lié à un lecteur et à un livre)                      |
|**Requête**         |Une instruction SQL qu’on envoie à la base (ex : `SELECT * FROM books`)                        |
|**NULL**            |L’absence de valeur (différent de zéro et de chaîne vide)                                      |
|**Jointure (JOIN)** |Une opération qui combine les données de plusieurs tables                                      |
|**Agrégation**      |Un calcul sur un groupe de lignes (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)                        |
|**Transaction**     |Un ensemble de modifications qu’on valide ou qu’on annule en bloc                              |
|**Index**           |Une structure qui accélère les recherches sur une colonne                                      |
|**Vue**             |Une requête enregistrée qu’on utilise comme une table                                          |
|**Contrainte**      |Une règle imposée à une colonne (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`)                 |
|**Dialecte SQL**    |Une variante de SQL propre à un SGBD (la syntaxe varie un peu entre SQLite, PostgreSQL, MySQL…)|
|**Injection SQL**   |Une attaque qui consiste à injecter du SQL malveillant via une entrée utilisateur mal protégée |

-----

### Comment penser une requête SQL

Avant d’écrire la moindre ligne de SQL, il faut comprendre la logique de base. **Toute requête SQL répond à une question :**

```
   QUESTION                  REQUÊTE                  RÉSULTAT
   "Quels lecteurs       →   SELECT * FROM      →     Une liste
    habitent à Paris ?"      readers WHERE            de lignes
                             city = 'Paris';
```


Concrètement, **6 grandes opérations** suffisent à résoudre 90% des questions :

1. **Choisir** une table (`FROM`)
1. **Choisir** des colonnes (`SELECT`)
1. **Filtrer** les lignes (`WHERE`)
1. **Croiser** plusieurs tables (`JOIN`)
1. **Regrouper** pour calculer (`GROUP BY` + `COUNT`/`SUM`/`AVG`)
1. **Trier et limiter** (`ORDER BY` + `LIMIT`)

Tout le reste est de la nuance ou de la combinaison de ces 6 briques. Garde ça en tête à chaque chapitre.

-----

### Fil rouge : Nora à la médiathèque

> **Contexte narratif**
> 
> **Nora**, 28 ans, vient d’être recrutée à la médiathèque municipale de Saint-Cloud. Son poste est hybride : agent d’accueil, responsable des données, et “personne qui sait gérer l’informatique” pour la petite équipe. La médiathèque a une base de données SQLite qui stocke les livres, les auteurs, les lecteurs, les emprunts, les comptes du personnel, et un journal de connexions.
> 
> Personne avant elle ne savait écrire de requêtes SQL. Le directeur veut maintenant des **statistiques régulières** : combien de lecteurs sont actifs, quels livres sont les plus empruntés, quels lecteurs ont des retards récurrents, quels emails sont en double dans la base, et — plus inquiétant — y a-t-il des tentatives de connexion suspectes sur les comptes du personnel ?
> 
> Nora va apprendre SQL chapitre par chapitre, et chaque épisode du fil rouge correspond à une vraie demande qu’elle reçoit dans son travail.

-----

### Table des matières

**PARTIE I — COMPRENDRE LES BASES (Ch.1-4)**

1. [Pourquoi les bases de données existent](01-partie-i-comprendre-les-bases/01-chapitre-1-pourquoi-les-bases-de-donnees-existent.md)
1. [Comprendre le modèle relationnel](01-partie-i-comprendre-les-bases/02-chapitre-2-comprendre-le-modele-relationnel.md)
1. [SQL, SGBD et dialectes](01-partie-i-comprendre-les-bases/03-chapitre-3-sql-sgbd-et-dialectes.md)
1. [Installer et explorer l’environnement de lab](01-partie-i-comprendre-les-bases/04-chapitre-4-installer-et-explorer-lenvironnement-de.md)

**PARTIE II — LIRE DES DONNÉES (Ch.5-10)**

1. [Première requête avec SELECT](02-partie-ii-lire-des-donnees/01-chapitre-5-premiere-requete-avec-select.md)
1. [Améliorer l’affichage : alias, DISTINCT, commentaires](02-partie-ii-lire-des-donnees/02-chapitre-6-ameliorer-laffichage-alias-distinct-com.md)
1. [Filtrer avec WHERE](02-partie-ii-lire-des-donnees/03-chapitre-7-filtrer-avec-where.md)
1. [Conditions multiples : AND, OR, NOT](02-partie-ii-lire-des-donnees/04-chapitre-8-conditions-multiples-and-or-not.md)
1. [Filtres utiles : LIKE, IN, BETWEEN, NULL](02-partie-ii-lire-des-donnees/05-chapitre-9-filtres-utiles-like-in-between-null.md)
1. [Trier, limiter et paginer](02-partie-ii-lire-des-donnees/06-chapitre-10-trier-limiter-et-paginer.md)

**PARTIE III — CALCULER ET REGROUPER (Ch.11-14)**

1. [Fonctions et calculs simples](03-partie-iii-calculer-et-regrouper/01-chapitre-11-fonctions-et-calculs-simples.md)
1. [Fonctions d’agrégation](03-partie-iii-calculer-et-regrouper/02-chapitre-12-fonctions-dagregation.md)
1. [Regrouper avec GROUP BY](03-partie-iii-calculer-et-regrouper/03-chapitre-13-regrouper-avec-group-by.md)
1. [Filtrer les groupes avec HAVING](03-partie-iii-calculer-et-regrouper/04-chapitre-14-filtrer-les-groupes-avec-having.md)

**PARTIE IV — CROISER LES TABLES (Ch.15-19)**

1. [Comprendre les relations entre tables](04-partie-iv-croiser-les-tables/01-chapitre-15-comprendre-les-relations-entre-tables.md)
1. [Première jointure avec INNER JOIN](04-partie-iv-croiser-les-tables/02-chapitre-16-premiere-jointure-avec-inner-join.md)
1. [LEFT JOIN et données sans correspondance](04-partie-iv-croiser-les-tables/03-chapitre-17-left-join-et-donnees-sans-correspondan.md)
1. [Jointures sur plusieurs tables](04-partie-iv-croiser-les-tables/04-chapitre-18-jointures-sur-plusieurs-tables.md)
1. [Pièges classiques des jointures](04-partie-iv-croiser-les-tables/05-chapitre-19-pieges-classiques-des-jointures.md)

**PARTIE V — MODIFIER LES DONNÉES (Ch.20-23)**

1. [Ajouter des données avec INSERT](05-partie-v-modifier-les-donnees/01-chapitre-20-ajouter-des-donnees-avec-insert.md)
1. [Modifier avec UPDATE](05-partie-v-modifier-les-donnees/02-chapitre-21-modifier-avec-update.md)
1. [Supprimer avec DELETE](05-partie-v-modifier-les-donnees/03-chapitre-22-supprimer-avec-delete.md)
1. [Transactions : BEGIN, COMMIT, ROLLBACK](05-partie-v-modifier-les-donnees/04-chapitre-23-transactions-begin-commit-rollback.md)

**PARTIE VI — CRÉER ET STRUCTURER UNE BASE (Ch.24-26)**

1. [Créer une table avec CREATE TABLE](06-partie-vi-creer-et-structurer-une-base/01-chapitre-24-creer-une-table-avec-create-table.md)
1. [Types de données et contraintes](06-partie-vi-creer-et-structurer-une-base/02-chapitre-25-types-de-donnees-et-contraintes.md)
1. [Modélisation simple](06-partie-vi-creer-et-structurer-une-base/03-chapitre-26-modelisation-simple.md)

**PARTIE VII — POUR ALLER PLUS LOIN (Ch.27-30) — 🔴 BONUS**

1. [Bonnes pratiques SQL et vues](07-partie-vii-pour-aller-plus-loin-bonus/01-chapitre-27-bonnes-pratiques-sql-et-vues.md)
1. [Index et performance : introduction](07-partie-vii-pour-aller-plus-loin-bonus/02-chapitre-28-index-et-performance-introduction.md)
1. [Sécurité et SQL injection : aperçu défensif](07-partie-vii-pour-aller-plus-loin-bonus/03-chapitre-29-securite-et-sql-injection-apercu-defen.md)
1. [SQL depuis Python : passerelle](07-partie-vii-pour-aller-plus-loin-bonus/04-chapitre-30-sql-depuis-python-passerelle.md)

**PARTIE VIII — SYNTHÈSE (Ch.31-32)**

1. [Skills Assessment — Évaluation finale](08-partie-viii-synthese/01-chapitre-31-skills-assessment-evaluation-finale.md)
1. [Synthèse et boîte à outils SQL](08-partie-viii-synthese/02-chapitre-32-synthese-et-boite-a-outils-sql.md)

**ANNEXES**

-----

## Sommaire

- [Partie I — Comprendre les bases](01-partie-i-comprendre-les-bases/index.md)
    - [Chapitre 1 — Pourquoi les bases de données existent](01-partie-i-comprendre-les-bases/01-chapitre-1-pourquoi-les-bases-de-donnees-existent.md)
    - [Chapitre 2 — Comprendre le modèle relationnel](01-partie-i-comprendre-les-bases/02-chapitre-2-comprendre-le-modele-relationnel.md)
    - [Chapitre 3 — SQL, SGBD et dialectes](01-partie-i-comprendre-les-bases/03-chapitre-3-sql-sgbd-et-dialectes.md)
    - [Chapitre 4 — Installer et explorer l’environnement de lab](01-partie-i-comprendre-les-bases/04-chapitre-4-installer-et-explorer-lenvironnement-de.md)
- [Partie II — Lire des données](02-partie-ii-lire-des-donnees/index.md)
    - [Chapitre 5 — Première requête avec SELECT](02-partie-ii-lire-des-donnees/01-chapitre-5-premiere-requete-avec-select.md)
    - [Chapitre 6 — Améliorer l’affichage : alias, DISTINCT, commentaires](02-partie-ii-lire-des-donnees/02-chapitre-6-ameliorer-laffichage-alias-distinct-com.md)
    - [Chapitre 7 — Filtrer avec WHERE](02-partie-ii-lire-des-donnees/03-chapitre-7-filtrer-avec-where.md)
    - [Chapitre 8 — Conditions multiples : AND, OR, NOT](02-partie-ii-lire-des-donnees/04-chapitre-8-conditions-multiples-and-or-not.md)
    - [Chapitre 9 — Filtres utiles : LIKE, IN, BETWEEN, NULL](02-partie-ii-lire-des-donnees/05-chapitre-9-filtres-utiles-like-in-between-null.md)
    - [Chapitre 10 — Trier, limiter et paginer](02-partie-ii-lire-des-donnees/06-chapitre-10-trier-limiter-et-paginer.md)
- [Partie III — Calculer ET regrouper](03-partie-iii-calculer-et-regrouper/index.md)
    - [Chapitre 11 — Fonctions et calculs simples](03-partie-iii-calculer-et-regrouper/01-chapitre-11-fonctions-et-calculs-simples.md)
    - [Chapitre 12 — Fonctions d’agrégation](03-partie-iii-calculer-et-regrouper/02-chapitre-12-fonctions-dagregation.md)
    - [Chapitre 13 — Regrouper avec GROUP BY](03-partie-iii-calculer-et-regrouper/03-chapitre-13-regrouper-avec-group-by.md)
    - [Chapitre 14 — Filtrer les groupes avec HAVING](03-partie-iii-calculer-et-regrouper/04-chapitre-14-filtrer-les-groupes-avec-having.md)
- [Partie IV — Croiser les tables](04-partie-iv-croiser-les-tables/index.md)
    - [Chapitre 15 — Comprendre les relations entre tables](04-partie-iv-croiser-les-tables/01-chapitre-15-comprendre-les-relations-entre-tables.md)
    - [Chapitre 16 — Première jointure avec INNER JOIN](04-partie-iv-croiser-les-tables/02-chapitre-16-premiere-jointure-avec-inner-join.md)
    - [Chapitre 17 — LEFT JOIN et données sans correspondance](04-partie-iv-croiser-les-tables/03-chapitre-17-left-join-et-donnees-sans-correspondan.md)
    - [Chapitre 18 — Jointures sur plusieurs tables](04-partie-iv-croiser-les-tables/04-chapitre-18-jointures-sur-plusieurs-tables.md)
    - [Chapitre 19 — Pièges classiques des jointures](04-partie-iv-croiser-les-tables/05-chapitre-19-pieges-classiques-des-jointures.md)
- [Partie V — Modifier les données](05-partie-v-modifier-les-donnees/index.md)
    - [Chapitre 20 — Ajouter des données avec INSERT](05-partie-v-modifier-les-donnees/01-chapitre-20-ajouter-des-donnees-avec-insert.md)
    - [Chapitre 21 — Modifier avec UPDATE](05-partie-v-modifier-les-donnees/02-chapitre-21-modifier-avec-update.md)
    - [Chapitre 22 — Supprimer avec DELETE](05-partie-v-modifier-les-donnees/03-chapitre-22-supprimer-avec-delete.md)
    - [Chapitre 23 — Transactions : BEGIN, COMMIT, ROLLBACK](05-partie-v-modifier-les-donnees/04-chapitre-23-transactions-begin-commit-rollback.md)
- [Partie VI — Créer ET structurer une base](06-partie-vi-creer-et-structurer-une-base/index.md)
    - [Chapitre 24 — Créer une table avec CREATE TABLE](06-partie-vi-creer-et-structurer-une-base/01-chapitre-24-creer-une-table-avec-create-table.md)
    - [Chapitre 25 — Types de données et contraintes](06-partie-vi-creer-et-structurer-une-base/02-chapitre-25-types-de-donnees-et-contraintes.md)
    - [Chapitre 26 — Modélisation simple](06-partie-vi-creer-et-structurer-une-base/03-chapitre-26-modelisation-simple.md)
- [Partie VII — Pour aller plus loin — 🔴 Bonus](07-partie-vii-pour-aller-plus-loin-bonus/index.md)
    - [Chapitre 27 — Bonnes pratiques SQL et vues](07-partie-vii-pour-aller-plus-loin-bonus/01-chapitre-27-bonnes-pratiques-sql-et-vues.md)
    - [Chapitre 28 — Index et performance : introduction](07-partie-vii-pour-aller-plus-loin-bonus/02-chapitre-28-index-et-performance-introduction.md)
    - [Chapitre 29 — Sécurité et SQL injection : aperçu défensif](07-partie-vii-pour-aller-plus-loin-bonus/03-chapitre-29-securite-et-sql-injection-apercu-defen.md)
    - [Chapitre 30 — SQL depuis Python : passerelle](07-partie-vii-pour-aller-plus-loin-bonus/04-chapitre-30-sql-depuis-python-passerelle.md)
- [Partie VIII — Synthèse](08-partie-viii-synthese/index.md)
    - [Chapitre 31 — Skills Assessment — Évaluation finale](08-partie-viii-synthese/01-chapitre-31-skills-assessment-evaluation-finale.md)
    - [Chapitre 32 — Synthèse et boîte à outils SQL](08-partie-viii-synthese/02-chapitre-32-synthese-et-boite-a-outils-sql.md)
- [Annexes](09-annexes.md)
