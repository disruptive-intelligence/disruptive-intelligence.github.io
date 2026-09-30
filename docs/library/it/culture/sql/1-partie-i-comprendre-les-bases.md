---
title: PARTIE I — COMPRENDRE LES BASES
source: IT/Culture/SQL.md
note: SQL
chapter: 1
chapters: 8
---

-----


## Chapitre 1 — Pourquoi les bases de données existent

### Le minimum à savoir

#### Le problème : pourquoi pas Excel ?

Imagine que tu gères une médiathèque avec un fichier Excel. Une feuille pour les livres, une pour les lecteurs, une pour les emprunts. Au début, tout va bien. Puis, peu à peu :

- Le fichier dépasse 50 000 lignes — il devient lent à ouvrir
- Deux personnes veulent le modifier en même temps — l’une perd son travail
- Tu cherches “tous les emprunts d’Alice Martin” — il faut faire un filtre, copier-coller, recouper avec une autre feuille
- Tu écris “Allice Martin” dans une ligne et “Alice Martin” dans une autre — Excel ne sait pas que c’est la même personne
- Tu envoies le fichier par mail à un collègue, il en fait une copie, modifie sa version — laquelle est la vraie ?

C’est exactement le problème que les **bases de données** résolvent.

#### Qu’est-ce qu’une base de données ?

Une base de données est un système conçu pour :

- **Stocker** beaucoup de données de manière structurée
- **Chercher** rapidement, même dans des millions de lignes
- **Gérer** plusieurs utilisateurs en même temps sans conflits
- **Garantir** la cohérence des données (pas de doublons, pas d’incohérences)
- **Sécuriser** l’accès (qui peut lire, qui peut modifier)
- **Sauvegarder** et restaurer en cas de problème

Tu interagis avec elle via un **langage** : SQL.

#### Où trouve-t-on des bases de données ?

**Partout.** Chaque fois que tu utilises une application qui mémorise quelque chose, il y a probablement une base de données derrière :

|Application                  |Ce que la base stocke                      |
|-----------------------------|-------------------------------------------|
|Site e-commerce              |Produits, clients, commandes, paiements    |
|Réseau social                |Utilisateurs, posts, messages, likes       |
|Application bancaire         |Comptes, transactions, virements           |
|Outil RH                     |Salariés, contrats, congés, paies          |
|Système de tickets (helpdesk)|Tickets, utilisateurs, échanges            |
|SIEM (cybersécurité)         |Logs, alertes, indicateurs de compromission|
|Bibliothèque/médiathèque     |Livres, lecteurs, emprunts, retards        |

Comprendre SQL te donne accès à **toutes ces données** — c’est l’une des compétences les plus universelles en informatique.

#### Excel vs base de données : la comparaison

|Aspect            |Excel / fichier texte      |Base de données            |
|------------------|---------------------------|---------------------------|
|Volume            |Quelques milliers de lignes|Millions, milliards        |
|Recherche         |Lente, manuelle            |Rapide, structurée         |
|Multi-utilisateurs|Conflits fréquents         |Géré nativement            |
|Cohérence         |Aucune garantie            |Contraintes strictes       |
|Relations         |Difficile                  |Natif (jointures)          |
|Sécurité          |Fichier protégé ou pas     |Permissions par utilisateur|
|Sauvegarde        |Manuelle                   |Automatisable              |
|Langage           |Formules Excel             |SQL (universel)            |


> **À retenir :** Excel n’est pas mauvais — il est parfait pour de petits volumes et de l’analyse ponctuelle. Mais dès qu’il faut **stocker durablement**, **partager** et **chercher efficacement**, la base de données est l’outil adapté.

> **📋 FIL ROUGE — Épisode 1**
> 
> Premier jour de Nora à la médiathèque. La directrice lui montre l’organisation actuelle : un fichier Excel “Liste_lecteurs_2024_v17_final_def.xlsx” et une autre feuille pour les emprunts. Trois personnes ont chacune leur propre version sur leur poste. Pour savoir si Alice Martin a rendu son livre, il faut ouvrir deux fichiers et croiser à la main. Heureusement, l’ancien stagiaire informatique a laissé une **base SQLite** `bibliotheque.db` mais personne ne sait l’utiliser. C’est ce que Nora va apprendre.

### ✅ Tu sais maintenant…

- Pourquoi les fichiers Excel atteignent vite leurs limites
- Ce qu’apporte une base de données (volume, recherche, cohérence, multi-utilisateurs)
- Que SQL est le langage universel pour parler aux bases de données
- Que les bases de données sont partout — apprendre SQL ouvre l’accès à toutes les applications qui en utilisent

-----


## Chapitre 2 — Comprendre le modèle relationnel

### Le minimum à savoir

#### Les briques fondamentales

Une base de données **relationnelle** est organisée en **tables**, chacune ressemblant à un tableau structuré.

```
Table : readers
┌────┬────────────┬───────────┬──────────────────────┬────────┐
│ id │ first_name │ last_name │ email                │ city   │
├────┼────────────┼───────────┼──────────────────────┼────────┤
│ 1  │ Alice      │ Martin    │ alice@example.com    │ Paris  │
│ 2  │ Karim      │ Bernard   │ karim@example.com    │ Lyon   │
│ 3  │ Léa        │ Dubois    │ lea.dubois@mail.fr   │ Paris  │
└────┴────────────┴───────────┴──────────────────────┴────────┘
   ↑       ↑           ↑             ↑                  ↑
 colonnes (champs) — chacune a un nom et un type
```

Vocabulaire :

|Terme                  |Signification                                           |
|-----------------------|--------------------------------------------------------|
|**Table**              |Un tableau de données (`readers` = les lecteurs)        |
|**Colonne (column)**   |Un champ — une propriété (`first_name`, `email`, `city`)|
|**Ligne (row, record)**|Un enregistrement — une instance (un lecteur précis)    |
|**Valeur**             |Le contenu d’une cellule (`Alice`, `Paris`)             |


> **Note :** une table SQL ressemble à une feuille Excel, à une grande différence près — chaque colonne a un **type fixé** (texte, nombre, date…) et des **règles** qui empêchent les incohérences.

#### La clé primaire

La **clé primaire** (primary key) est une colonne qui identifie de façon **unique** chaque ligne d’une table. Souvent, c’est une colonne `id` qui contient un nombre auto-incrémenté.

```
readers
┌────┬────────────┐
│ id │ first_name │  ← id est la clé primaire
├────┼────────────┤
│ 1  │ Alice      │
│ 2  │ Karim      │
│ 3  │ Léa        │  ← chaque id est unique
└────┴────────────┘
```

Pourquoi c’est crucial ? Parce que dans la vraie vie, plusieurs personnes peuvent s’appeler “Alice Martin”. Mais l’**id** est unique. Quand tu cherches “le lecteur d’id 1”, il n’y en a qu’un — pas d’ambiguïté.

#### Plusieurs tables, et des liens entre elles

Une médiathèque ne stocke pas que des lecteurs. Elle stocke aussi des **livres** :

```
Table : books
┌────┬─────────────────────┬────────────────────┐
│ id │ title               │ category           │
├────┼─────────────────────┼────────────────────┤
│ 4  │ Les Misérables      │ Roman              │
│ 7  │ 1984                │ Roman              │
│ 12 │ Sapiens             │ Histoire           │
└────┴─────────────────────┴────────────────────┘
```

Et des **emprunts** — c’est ici que la magie du modèle relationnel opère :

```
Table : loans
┌────┬───────────┬─────────┬────────────┐
│ id │ reader_id │ book_id │ loan_date  │
├────┼───────────┼─────────┼────────────┤
│ 1  │ 1         │ 4       │ 2026-01-10 │  ← Alice (id=1) a emprunté Les Misérables (id=4)
│ 2  │ 2         │ 7       │ 2026-01-12 │  ← Karim (id=2) a emprunté 1984 (id=7)
│ 3  │ 1         │ 12      │ 2026-01-15 │  ← Alice (id=1) a aussi emprunté Sapiens (id=12)
└────┴───────────┴─────────┴────────────┘
```

Au lieu de répéter “Alice Martin” et “Les Misérables” dans chaque ligne d’emprunt, on stocke seulement les **identifiants** : `reader_id = 1` et `book_id = 4`.

#### La clé étrangère

`reader_id` dans la table `loans` est une **clé étrangère** (foreign key). Elle pointe vers la **clé primaire** `id` de la table `readers`. C’est ce qui crée la **relation** entre les deux tables.

```
   loans                                  readers
   ┌────┬───────────┬─────────┐          ┌────┬────────────┐
   │ id │ reader_id │ book_id │          │ id │ first_name │
   ├────┼───────────┼─────────┤          ├────┼────────────┤
   │ 1  │     1 ────┼─────────┼─────────→│ 1  │ Alice      │
   │ 2  │     2 ────┼─────────┼─────────→│ 2  │ Karim      │
   └────┴───────────┴─────────┘          └────┴────────────┘
            clé étrangère                       clé primaire
```

> **À retenir :** la clé primaire **identifie**, la clé étrangère **relie**. C’est le concept central du modèle relationnel — la “relation” dans “base de données relationnelle” vient de là.

#### Pourquoi séparer les données ?

Trois raisons fondamentales :

1. **Éviter les doublons** : on stocke “Alice Martin” une seule fois (dans `readers`), pas dans chaque emprunt
1. **Garantir la cohérence** : si Alice change d’email, on le modifie en un seul endroit
1. **Permettre les relations** : un lecteur peut avoir 50 emprunts sans qu’on duplique 50 fois ses informations

> **📋 FIL ROUGE — Épisode 2**
> 
> Nora ouvre la base `bibliotheque.db` et découvre 8 tables : `readers`, `books`, `authors`, `categories`, `book_authors`, `loans`, `staff_users`, `login_events`. Au début, ça l’intimide. Puis elle comprend la logique : chaque entité a sa table (lecteurs, livres, auteurs…), et les tables d’**association** comme `book_authors` ou `loans` font le lien entre elles. Le schéma devient lisible.

### Très utile en pratique

#### Les types de relations

|Relation                       |Exemple                                                                       |Comment c’est modélisé                                    |
|-------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------|
|**Un-à-plusieurs (1-N)**       |Un lecteur a plusieurs emprunts                                               |Une clé étrangère dans la table “côté plusieurs”          |
|**Plusieurs-à-plusieurs (N-N)**|Un livre peut avoir plusieurs auteurs ; un auteur peut écrire plusieurs livres|Une table d’**association** intermédiaire (`book_authors`)|
|**Un-à-un (1-1)**              |Un utilisateur a un profil détaillé                                           |Rare, géré par une clé étrangère unique                   |

On reverra tout ça en détail au Ch.15 quand on attaquera les jointures.

### ✅ Tu sais maintenant…

- Une base relationnelle est composée de **tables** (lignes + colonnes)
- La **clé primaire** identifie de façon unique chaque ligne
- La **clé étrangère** relie une table à une autre
- Les données sont **séparées** pour éviter les doublons et garantir la cohérence
- Les relations 1-N et N-N sont les patterns de base du modèle relationnel

-----


## Chapitre 3 — SQL, SGBD et dialectes

### Le minimum à savoir

#### SQL vs SGBD : la confusion classique

Beaucoup de débutants confondent **SQL** et le **moteur** de base de données. C’est comme confondre “le français” et “un livre français”.

|Concept |Définition                                                     |Exemples                                             |
|--------|---------------------------------------------------------------|-----------------------------------------------------|
|**SQL** |Le **langage** standardisé pour parler aux bases relationnelles|(un seul SQL — défini par les normes ISO)            |
|**SGBD**|Le **moteur** qui exécute le SQL                               |SQLite, PostgreSQL, MySQL/MariaDB, SQL Server, Oracle|


> **Phrase à retenir :** SQL est le langage. SQLite, PostgreSQL, MySQL ou SQL Server sont des moteurs qui comprennent ce langage avec quelques variantes.

#### Les SGBD que tu rencontreras

|SGBD               |Particularité                           |Cas d’usage typique                                           |
|-------------------|----------------------------------------|--------------------------------------------------------------|
|**SQLite**         |Léger (un fichier `.db`), pas de serveur|Apps mobiles, sites web légers, prototypage, **apprentissage**|
|**PostgreSQL**     |Open source, très complet, robuste      |Applications web modernes, data, géographie                   |
|**MySQL / MariaDB**|Open source, très répandu               |Sites web (WordPress, etc.), applis classiques                |
|**SQL Server**     |Microsoft, solide en entreprise         |ERP, environnements Windows                                   |
|**Oracle**         |Historique, puissant, payant            |Grandes banques, ERP critiques                                |

**Tous comprennent le SQL standard.** Si tu sais écrire `SELECT * FROM users WHERE city = 'Paris'`, ça marche partout.

#### Les dialectes : les petites différences

Chaque SGBD ajoute ses propres extensions au SQL standard. C’est ce qu’on appelle un **dialecte**.

Exemples :

|Tâche                |SQLite               |PostgreSQL            |MySQL             |
|---------------------|---------------------|----------------------|------------------|
|Concaténer du texte  |`'a' || 'b'`         |`'a' || 'b'`          |`CONCAT('a', 'b')`|
|Date du jour         |`DATE('now')`        |`CURRENT_DATE`        |`CURDATE()`       |
|Auto-incrément       |`INTEGER PRIMARY KEY`|`SERIAL` ou `IDENTITY`|`AUTO_INCREMENT`  |
|Limiter les résultats|`LIMIT 10`           |`LIMIT 10`            |`LIMIT 10`        |

**90% du SQL est identique entre tous les SGBD.** Les 10% qui varient sont les fonctions de date, l’auto-incrément, la concaténation, et quelques détails. On apprend SQLite dans ce cours, mais ce que tu apprends est transférable à 90% sur PostgreSQL ou MySQL.

#### Pourquoi SQLite pour ce cours ?

Pour apprendre, SQLite est imbattable :

- **Pas de serveur** : la base est un seul fichier `.db` — tu copies, tu déplaces, tu sauvegardes facilement
- **Installation triviale** : déjà inclus dans Python, dans macOS, dans la plupart des Linux
- **Outils gratuits** : DB Browser for SQLite te donne une interface graphique en 2 minutes
- **Syntaxe SQL standard** : ce que tu apprends marchera (à 90%) sur PostgreSQL et MySQL
- **Suffisant pour de vraies applications** : SQLite est utilisé par des milliards d’apps mobiles, le navigateur Firefox, etc.

> **À retenir :** apprendre sur SQLite **n’est pas** apprendre un truc obsolète ou un jouet. C’est apprendre SQL avec l’environnement le plus simple possible. Tu transféreras 90% de ce que tu sais quand tu passeras à PostgreSQL ou MySQL.

### ✅ Tu sais maintenant…

- SQL est le **langage**, le SGBD est le **moteur**
- Les SGBD principaux : SQLite, PostgreSQL, MySQL, SQL Server, Oracle
- Les **dialectes** sont les petites variantes propres à chaque moteur
- SQLite est parfait pour apprendre — et ce que tu apprends est transférable

-----


## Chapitre 4 — Installer et explorer l’environnement de lab

### Le minimum à savoir

#### Les outils que tu vas utiliser

1. **DB Browser for SQLite** : interface graphique recommandée pour débuter (gratuite, multi-plateforme)
1. **`sqlite3`** : l’outil en ligne de commande SQLite, parfois déjà installé selon le système, sinon installable séparément (paquet `sqlite3` sous Linux/Mac, téléchargeable sur sqlite.org pour Windows)
1. **Module Python `sqlite3`** : intégré nativement à Python, utile pour interroger SQLite depuis un script (voir Ch.30)

#### Installer DB Browser for SQLite

C’est l’outil que je te recommande pour démarrer. Tu ouvres ta base, tu vois les tables, tu cliques pour explorer, tu écris tes requêtes dans une fenêtre dédiée.

**Téléchargement :** <https://sqlitebrowser.org> (gratuit, open source, Windows/Mac/Linux)

**Installation :**

- **Windows** : télécharge le `.msi`, double-clic, suivant-suivant-terminer
- **Mac** : télécharge le `.dmg`, glisse dans Applications
- **Linux (Ubuntu/Debian)** : `sudo apt install sqlitebrowser`

Une fois installé, lance l’application. Tu vois 4 onglets en haut :

- **Structure de la base** (les tables, les colonnes, les contraintes)
- **Parcourir les données** (visualiser et éditer les lignes)
- **Modifier les pragmas** (paramètres avancés — on s’en fiche pour l’instant)
- **Exécuter le SQL** (où tu vas passer 95% de ton temps)

#### La base de démo : `bibliotheque.db`

Pour pratiquer, il te faut une base remplie de données. Voici le **script SQL complet** qui crée la base “bibliothèque” qu’on utilisera tout au long du cours.

**Marche à suivre :**

1. Ouvre DB Browser for SQLite
1. Clique sur **“Nouvelle base de données”** → enregistre-la sous `bibliotheque.db`
1. Va dans l’onglet **“Exécuter le SQL”**
1. Colle l’intégralité du script ci-dessous
1. Clique sur le bouton ▶ (“Exécuter”)
1. Dans le menu : **Fichier → Enregistrer les changements**

**Script `bibliotheque.sql`** (le code complet est aussi disponible en Annexe H) :

```sql
-- =============================================================
-- Base de démo : médiathèque municipale
-- =============================================================
-- Ce script est idempotent : tu peux le ré-exécuter, il se nettoie tout seul.

-- 1. Désactiver temporairement les FK pour pouvoir DROP dans n'importe quel ordre
PRAGMA foreign_keys = OFF;

-- 2. Supprimer les tables si elles existent déjà (ordre inverse des dépendances)
DROP TABLE IF EXISTS login_events;
DROP TABLE IF EXISTS staff_users;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS book_authors;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS readers;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS categories;

-- 3. Réactiver les FK pour qu'elles soient vraiment appliquées
PRAGMA foreign_keys = ON;

-- =============================================================
-- Création des tables
-- =============================================================

-- Catégories de livres
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO categories (id, name) VALUES
    (1, 'Roman'),
    (2, 'Histoire'),
    (3, 'Science'),
    (4, 'Bande dessinée'),
    (5, 'Jeunesse'),
    (6, 'Polar');

-- Auteurs
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

INSERT INTO authors (id, name, country) VALUES
    (1, 'Victor Hugo', 'France'),
    (2, 'George Orwell', 'Royaume-Uni'),
    (3, 'Yuval Noah Harari', 'Israël'),
    (4, 'J.K. Rowling', 'Royaume-Uni'),
    (5, 'Albert Camus', 'France'),
    (6, 'Stephen King', 'États-Unis'),
    (7, 'Agatha Christie', 'Royaume-Uni'),
    (8, 'Hergé', 'Belgique'),
    (9, 'Claire Morel', 'France'),
    (10, 'Marc Dumas', 'France'),
    (11, 'Mary Shelley', 'Royaume-Uni');     -- auteur sans livre dans la base

-- Livres
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    category_id INTEGER,
    publication_year INTEGER,
    isbn TEXT UNIQUE,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO books (id, title, category_id, publication_year, isbn) VALUES
    (1, 'Les Misérables', 1, 1862, '978-2-07-040922-8'),
    (2, '1984', 1, 1949, '978-0-452-28423-4'),
    (3, 'Sapiens', 2, 2011, '978-0-06-231609-7'),
    (4, 'Harry Potter à l''école des sorciers', 5, 1997, '978-2-07-054127-9'),
    (5, 'L''Étranger', 1, 1942, '978-2-07-036002-4'),
    (6, 'Ça', 6, 1986, '978-2-253-15124-5'),
    (7, 'Le Crime de l''Orient-Express', 6, 1934, '978-2-253-00642-2'),
    (8, 'Tintin au Tibet', 4, 1960, '978-2-203-00120-3'),
    (9, 'Notre-Dame de Paris', 1, 1831, '978-2-07-040909-9'),
    (10, 'Animal Farm', 1, 1945, '978-0-452-28424-1'),
    (11, 'Harry Potter et la Chambre des Secrets', 5, 1998, '978-2-07-054128-6'),
    (12, 'La Peste', 1, 1947, '978-2-07-036042-0'),
    (13, 'Shining', 6, 1977, '978-2-253-15127-6'),
    (14, 'Dix petits nègres', 6, 1939, '978-2-253-00643-9'),
    (15, 'Histoire d''un pays sans nom', 2, 2018, '978-2-07-014123-7');

-- Table d'association livres ↔ auteurs (relation N-N)
CREATE TABLE book_authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

INSERT INTO book_authors (book_id, author_id) VALUES
    (1, 1), (9, 1),                  -- Hugo
    (2, 2), (10, 2),                  -- Orwell
    (3, 3),                            -- Harari
    (4, 4), (11, 4),                  -- Rowling
    (5, 5), (12, 5),                  -- Camus
    (6, 6), (13, 6),                  -- King
    (7, 7), (14, 7),                  -- Christie
    (8, 8),                            -- Hergé
    (15, 9), (15, 10);                 -- Histoire d'un pays sans nom : coécrit Morel + Dumas

-- Lecteurs
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    city TEXT,
    phone TEXT,
    registration_date TEXT NOT NULL
);

INSERT INTO readers (id, first_name, last_name, email, city, phone, registration_date) VALUES
    (1, 'Alice', 'Martin', 'alice.martin@example.com', 'Paris', '0612345678', '2023-03-15'),
    (2, 'Karim', 'Bernard', 'karim.bernard@example.com', 'Lyon', '0698765432', '2023-04-02'),
    (3, 'Léa', 'Dubois', 'lea.dubois@example.com', 'Paris', NULL, '2023-05-10'),
    (4, 'Thomas', 'Petit', 'thomas.petit@example.com', 'Marseille', '0623456789', '2023-06-21'),
    (5, 'Sophie', 'Leroy', 'sophie.leroy@example.com', 'Paris', '0634567890', '2023-09-05'),
    (6, 'Mehdi', 'Garcia', 'mehdi.garcia@example.com', 'Lyon', NULL, '2024-01-12'),
    (7, 'Camille', 'Rousseau', 'camille.rousseau@example.com', 'Bordeaux', '0645678901', '2024-02-28'),
    (8, 'Hugo', 'Moreau', 'hugo.moreau@example.com', 'Paris', '0656789012', '2024-04-15'),
    (9, 'Yasmine', 'Lefevre', 'yasmine.lefevre@example.com', 'Marseille', NULL, '2024-07-03'),
    (10, 'Alice', 'Martin', 'alice.martin@example.com', 'Toulouse', '0667890123', '2024-09-18'),
    (11, 'Pierre', 'Roux', 'pierre.roux@example.com', 'Lyon', '0678901234', '2024-11-22'),
    (12, 'Inès', 'Vincent', NULL, 'Paris', '0689012345', '2025-01-08'),
    (13, 'David', 'Fournier', 'david.fournier@example.com', 'Bordeaux', NULL, '2025-02-14'),
    (14, 'Sarah', 'Mercier', 'sarah.mercier@example.com', 'Paris', '0690123456', '2025-04-30'),
    (15, 'Lucas', 'Blanc', 'lucas.blanc@example.com', 'Toulouse', '0601234567', '2025-08-11');

-- Emprunts
CREATE TABLE loans (
    id INTEGER PRIMARY KEY,
    reader_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL DEFAULT 'borrowed',
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (status IN ('borrowed', 'returned', 'late'))
);

INSERT INTO loans (id, reader_id, book_id, loan_date, return_date, status) VALUES
    (1, 1, 1, '2025-01-10', '2025-01-25', 'returned'),
    (2, 2, 2, '2025-01-15', '2025-02-05', 'returned'),
    (3, 1, 3, '2025-02-20', '2025-03-10', 'returned'),
    (4, 3, 4, '2025-03-01', NULL, 'late'),
    (5, 4, 5, '2025-03-15', '2025-04-02', 'returned'),
    (6, 1, 6, '2025-04-10', NULL, 'borrowed'),
    (7, 5, 7, '2025-04-22', '2025-05-12', 'returned'),
    (8, 2, 8, '2025-05-05', NULL, 'late'),
    (9, 6, 9, '2025-05-18', '2025-06-08', 'returned'),
    (10, 7, 10, '2025-06-01', '2025-06-22', 'returned'),
    (11, 1, 11, '2025-06-15', '2025-07-05', 'returned'),
    (12, 8, 12, '2025-07-10', NULL, 'borrowed'),
    (13, 3, 13, '2025-07-25', NULL, 'late'),
    (14, 9, 14, '2025-08-12', '2025-09-01', 'returned'),
    (15, 4, 15, '2025-08-30', NULL, 'borrowed'),
    (16, 5, 1, '2025-09-15', '2025-10-05', 'returned'),
    (17, 1, 2, '2025-10-02', NULL, 'borrowed'),
    (18, 11, 3, '2025-10-18', NULL, 'borrowed'),
    (19, 13, 6, '2025-11-05', NULL, 'borrowed'),
    (20, 1, 4, '2025-11-20', NULL, 'late');

-- Comptes du personnel (pour l'angle cyber)
CREATE TABLE staff_users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
);

INSERT INTO staff_users (id, username, full_name, role, is_active, created_at) VALUES
    (1, 'nora.benali', 'Nora Benali', 'admin', 1, '2025-01-15'),
    (2, 'jean.dupont', 'Jean Dupont', 'staff', 1, '2023-09-01'),
    (3, 'sophie.morel', 'Sophie Morel', 'staff', 1, '2024-03-12'),
    (4, 'olivier.bernard', 'Olivier Bernard', 'staff', 0, '2022-06-20'),
    (5, 'admin', 'Admin Initial', 'admin', 1, '2022-01-01');

-- Journal de connexions au système interne
CREATE TABLE login_events (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    event_time TEXT NOT NULL,
    success INTEGER NOT NULL,
    ip_address TEXT
);

INSERT INTO login_events (id, username, event_time, success, ip_address) VALUES
    (1, 'nora.benali', '2025-11-20 08:32:15', 1, '192.168.1.42'),
    (2, 'jean.dupont', '2025-11-20 09:01:43', 1, '192.168.1.51'),
    (3, 'sophie.morel', '2025-11-20 09:15:02', 1, '192.168.1.55'),
    (4, 'admin', '2025-11-20 23:14:01', 0, '203.0.113.42'),
    (5, 'admin', '2025-11-20 23:14:08', 0, '203.0.113.42'),
    (6, 'admin', '2025-11-20 23:14:14', 0, '203.0.113.42'),
    (7, 'admin', '2025-11-20 23:14:19', 0, '203.0.113.42'),
    (8, 'admin', '2025-11-20 23:14:25', 0, '203.0.113.42'),
    (9, 'admin', '2025-11-20 23:14:31', 0, '203.0.113.42'),
    (10, 'admin', '2025-11-20 23:14:37', 0, '203.0.113.42'),
    (11, 'admin', '2025-11-20 23:14:42', 0, '203.0.113.42'),
    (12, 'admin', '2025-11-20 23:14:48', 0, '203.0.113.42'),
    (13, 'admin', '2025-11-20 23:14:54', 0, '203.0.113.42'),
    (14, 'admin', '2025-11-20 23:15:01', 1, '203.0.113.42'),
    (15, 'nora.benali', '2025-11-21 08:28:55', 1, '192.168.1.42'),
    (16, 'jean.dupont', '2025-11-21 08:55:12', 1, '192.168.1.51'),
    (17, 'olivier.bernard', '2025-11-21 14:32:09', 0, '198.51.100.7');
```

> **Astuce :** ce script est aussi en **Annexe H** à la fin du cours, prêt à être copié-collé.

> **⚠️ Important — SQLite et les clés étrangères :** par défaut, SQLite **n’applique pas automatiquement** les contraintes `FOREIGN KEY` dans toutes les sessions. Il faut les activer explicitement avec `PRAGMA foreign_keys = ON;` au début de chaque session. Le script de la base le fait déjà, mais si tu ouvres une nouvelle session SQLite (par exemple via `sqlite3 bibliotheque.db` en ligne de commande), pense à ré-exécuter `PRAGMA foreign_keys = ON;` avant tes manipulations. Sinon, certaines erreurs de clé étrangère que tu attends (par exemple aux Ch.22 sur `DELETE`) ne se produiront pas.

#### Premières commandes en ligne de commande SQLite

Si tu préfères le terminal, ouvre un terminal et lance :

```bash
sqlite3 bibliotheque.db
```

Tu obtiens un prompt `sqlite>`. Quelques commandes utiles (les “méta-commandes” commencent par un point) :

```
.tables                 -- Liste les tables
.schema                 -- Affiche la structure de toutes les tables
.schema readers         -- Affiche la structure de la table readers
.headers on             -- Affiche les noms de colonnes dans les résultats
.mode column            -- Affichage en colonnes alignées (plus lisible)
.quit                   -- Quitter sqlite3
```

Puis tu peux taper du SQL directement :

```sql
SELECT * FROM readers LIMIT 5;
```

> **📋 FIL ROUGE — Épisode 3**
> 
> Nora installe DB Browser, ouvre `bibliotheque.db`, et explore la structure. Elle découvre que la base contient bien tout ce dont elle a besoin : 8 tables, des données réalistes, et même un journal de connexions. Elle clique sur “Parcourir les données” pour voir les premières lignes — déjà, elle commence à comprendre la logique. Maintenant, il faut apprendre à interroger.

### ✅ Tu sais maintenant…

- Installer DB Browser for SQLite (interface graphique recommandée pour débuter)
- Créer une base SQLite à partir d’un script SQL
- La base de démo `bibliotheque.db` contient 8 tables prêtes à l’emploi
- Les méta-commandes utiles de `sqlite3` en ligne de commande (`.tables`, `.schema`, `.headers on`)

-----
