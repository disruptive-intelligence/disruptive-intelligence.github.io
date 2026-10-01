---
title: Chapitre 4 — Installer et explorer l’environnement de lab
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie I — Comprendre les bases
  - index.md
---

## Le minimum à savoir

### Les outils que tu vas utiliser

1. **DB Browser for SQLite** : interface graphique recommandée pour débuter (gratuite, multi-plateforme)
1. **`sqlite3`** : l’outil en ligne de commande SQLite, parfois déjà installé selon le système, sinon installable séparément (paquet `sqlite3` sous Linux/Mac, téléchargeable sur sqlite.org pour Windows)
1. **Module Python `sqlite3`** : intégré nativement à Python, utile pour interroger SQLite depuis un script (voir Ch.30)

### Installer DB Browser for SQLite

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

### La base de démo : `bibliotheque.db`

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

### Premières commandes en ligne de commande SQLite

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

## ✅ Tu sais maintenant…

- Installer DB Browser for SQLite (interface graphique recommandée pour débuter)
- Créer une base SQLite à partir d’un script SQL
- La base de démo `bibliotheque.db` contient 8 tables prêtes à l’emploi
- Les méta-commandes utiles de `sqlite3` en ligne de commande (`.tables`, `.schema`, `.headers on`)

-----
