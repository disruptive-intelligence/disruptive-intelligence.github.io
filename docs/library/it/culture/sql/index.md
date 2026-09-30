---
title: SQL
source: IT/Culture/SQL.md
chapters: 8
---

### De zéro à l’interrogation de données — Guide pour débutant absolu

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

1. [Pourquoi les bases de données existent](1-partie-i-comprendre-les-bases.md#chapitre-1-pourquoi-les-bases-de-donnees-existent)
1. [Comprendre le modèle relationnel](1-partie-i-comprendre-les-bases.md#chapitre-2-comprendre-le-modele-relationnel)
1. [SQL, SGBD et dialectes](1-partie-i-comprendre-les-bases.md#chapitre-3-sql-sgbd-et-dialectes)
1. [Installer et explorer l’environnement de lab](1-partie-i-comprendre-les-bases.md#chapitre-4-installer-et-explorer-lenvironnement-de-lab)

**PARTIE II — LIRE DES DONNÉES (Ch.5-10)**

1. [Première requête avec SELECT](2-partie-ii-lire-des-donnees.md#chapitre-5-premiere-requete-avec-select)
1. [Améliorer l’affichage : alias, DISTINCT, commentaires](2-partie-ii-lire-des-donnees.md#chapitre-6-ameliorer-laffichage-alias-distinct-commentaires)
1. [Filtrer avec WHERE](2-partie-ii-lire-des-donnees.md#chapitre-7-filtrer-avec-where)
1. [Conditions multiples : AND, OR, NOT](2-partie-ii-lire-des-donnees.md#chapitre-8-conditions-multiples-and-or-not)
1. [Filtres utiles : LIKE, IN, BETWEEN, NULL](2-partie-ii-lire-des-donnees.md#chapitre-9-filtres-utiles-like-in-between-null)
1. [Trier, limiter et paginer](2-partie-ii-lire-des-donnees.md#chapitre-10-trier-limiter-et-paginer)

**PARTIE III — CALCULER ET REGROUPER (Ch.11-14)**

1. [Fonctions et calculs simples](3-partie-iii-calculer-et-regrouper.md#chapitre-11-fonctions-et-calculs-simples)
1. [Fonctions d’agrégation](3-partie-iii-calculer-et-regrouper.md#chapitre-12-fonctions-dagregation)
1. [Regrouper avec GROUP BY](3-partie-iii-calculer-et-regrouper.md#chapitre-13-regrouper-avec-group-by)
1. [Filtrer les groupes avec HAVING](3-partie-iii-calculer-et-regrouper.md#chapitre-14-filtrer-les-groupes-avec-having)

**PARTIE IV — CROISER LES TABLES (Ch.15-19)**

1. [Comprendre les relations entre tables](4-partie-iv-croiser-les-tables.md#chapitre-15-comprendre-les-relations-entre-tables)
1. [Première jointure avec INNER JOIN](4-partie-iv-croiser-les-tables.md#chapitre-16-premiere-jointure-avec-inner-join)
1. [LEFT JOIN et données sans correspondance](4-partie-iv-croiser-les-tables.md#chapitre-17-left-join-et-donnees-sans-correspondance)
1. [Jointures sur plusieurs tables](4-partie-iv-croiser-les-tables.md#chapitre-18-jointures-sur-plusieurs-tables)
1. [Pièges classiques des jointures](4-partie-iv-croiser-les-tables.md#chapitre-19-pieges-classiques-des-jointures)

**PARTIE V — MODIFIER LES DONNÉES (Ch.20-23)**

1. [Ajouter des données avec INSERT](5-partie-v-modifier-les-donnees.md#chapitre-20-ajouter-des-donnees-avec-insert)
1. [Modifier avec UPDATE](5-partie-v-modifier-les-donnees.md#chapitre-21-modifier-avec-update)
1. [Supprimer avec DELETE](5-partie-v-modifier-les-donnees.md#chapitre-22-supprimer-avec-delete)
1. [Transactions : BEGIN, COMMIT, ROLLBACK](5-partie-v-modifier-les-donnees.md#chapitre-23-transactions-begin-commit-rollback)

**PARTIE VI — CRÉER ET STRUCTURER UNE BASE (Ch.24-26)**

1. [Créer une table avec CREATE TABLE](6-partie-vi-creer-et-structurer-une-base.md#chapitre-24-creer-une-table-avec-create-table)
1. [Types de données et contraintes](6-partie-vi-creer-et-structurer-une-base.md#chapitre-25-types-de-donnees-et-contraintes)
1. [Modélisation simple](6-partie-vi-creer-et-structurer-une-base.md#chapitre-26-modelisation-simple)

**PARTIE VII — POUR ALLER PLUS LOIN (Ch.27-30) — 🔴 BONUS**

1. [Bonnes pratiques SQL et vues](7-partie-vii-pour-aller-plus-loin-bonus.md#chapitre-27-bonnes-pratiques-sql-et-vues)
1. [Index et performance : introduction](7-partie-vii-pour-aller-plus-loin-bonus.md#chapitre-28-index-et-performance-introduction)
1. [Sécurité et SQL injection : aperçu défensif](7-partie-vii-pour-aller-plus-loin-bonus.md#chapitre-29-securite-et-sql-injection-apercu-defensif)
1. [SQL depuis Python : passerelle](7-partie-vii-pour-aller-plus-loin-bonus.md#chapitre-30-sql-depuis-python-passerelle)

**PARTIE VIII — SYNTHÈSE (Ch.31-32)**

1. [Skills Assessment — Évaluation finale](8-partie-viii-synthese.md#chapitre-31-skills-assessment-evaluation-finale)
1. [Synthèse et boîte à outils SQL](8-partie-viii-synthese.md#chapitre-32-synthese-et-boite-a-outils-sql)

**ANNEXES**

-----

## Sommaire

1. [PARTIE I — COMPRENDRE LES BASES](1-partie-i-comprendre-les-bases.md)
2. [PARTIE II — LIRE DES DONNÉES](2-partie-ii-lire-des-donnees.md)
3. [PARTIE III — CALCULER ET REGROUPER](3-partie-iii-calculer-et-regrouper.md)
4. [PARTIE IV — CROISER LES TABLES](4-partie-iv-croiser-les-tables.md)
5. [PARTIE V — MODIFIER LES DONNÉES](5-partie-v-modifier-les-donnees.md)
6. [PARTIE VI — CRÉER ET STRUCTURER UNE BASE](6-partie-vi-creer-et-structurer-une-base.md)
7. [PARTIE VII — POUR ALLER PLUS LOIN — 🔴 BONUS](7-partie-vii-pour-aller-plus-loin-bonus.md)
8. [PARTIE VIII — SYNTHÈSE](8-partie-viii-synthese.md)
