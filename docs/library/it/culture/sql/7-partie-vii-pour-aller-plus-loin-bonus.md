---
title: PARTIE VII — POUR ALLER PLUS LOIN — 🔴 BONUS
source: IT/Culture/SQL.md
note: SQL
chapter: 7
chapters: 8
---

> **Important :** cette partie est **bonus**. Tu peux finir le cœur du cours (Ch.1-26) et le Skills Assessment (Ch.31) sans elle. Reviens ici quand tu te sens à l’aise avec les bases — ces chapitres enrichissent la pratique mais ne la conditionnent pas.

-----


## Chapitre 27 — Bonnes pratiques SQL et vues

### Le minimum à savoir

#### Les bonnes pratiques d’écriture

Une requête lisible, c’est une requête qu’on peut **comprendre, déboguer et modifier** sans douleur. Quelques règles simples :

**1. Indenter et aérer**

```sql
-- ❌ Illisible
SELECT r.first_name,r.last_name,b.title,l.loan_date FROM loans l INNER JOIN readers r ON l.reader_id=r.id INNER JOIN books b ON l.book_id=b.id WHERE l.status='late' ORDER BY l.loan_date DESC;

-- ✅ Lisible
SELECT r.first_name, r.last_name, b.title, l.loan_date
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status = 'late'
ORDER BY l.loan_date DESC;
```

**2. Mots-clés SQL en MAJUSCULES**, noms de tables/colonnes en minuscules.

**3. Alias courts et significatifs** : `r` pour `readers`, `b` pour `books`, `l` pour `loans`.

**4. Éviter `SELECT *` dans les requêtes finales** — préfère lister les colonnes nécessaires.

**5. Commenter les requêtes complexes**

```sql
-- Lecteurs ayant emprunté plus de 3 livres en 2025
-- (utilisé pour les invitations à la soirée des grands lecteurs)
SELECT r.first_name, r.last_name, COUNT(*) AS nb_emprunts_2025
FROM readers AS r
INNER JOIN loans AS l ON r.id = l.reader_id
WHERE l.loan_date >= '2025-01-01'
GROUP BY r.id, r.first_name, r.last_name
HAVING COUNT(*) > 3;
```

**6. Toujours faire un `SELECT` avant `UPDATE` ou `DELETE`** (rappelé au Ch.21-22).

**7. Utiliser des transactions** pour les modifications importantes (Ch.23).

**8. Limiter les résultats avec `LIMIT`** quand tu explores.

#### Les vues : enregistrer une requête sous un nom

Une **vue** (view) est une requête enregistrée que tu peux utiliser comme une table. Elle ne stocke pas de données — elle exécute la requête sous-jacente à chaque appel.

```sql
-- Créer une vue
CREATE VIEW active_loans AS
SELECT r.first_name, r.last_name, b.title, l.loan_date, l.status
FROM loans AS l
INNER JOIN readers AS r ON l.reader_id = r.id
INNER JOIN books AS b ON l.book_id = b.id
WHERE l.status IN ('borrowed', 'late');

-- L'utiliser comme une table
SELECT * FROM active_loans;
SELECT * FROM active_loans WHERE status = 'late';
```

**Pourquoi c’est utile :**

- Simplifier les requêtes complexes pour les utilisateurs
- Éviter de réécrire la même jointure 50 fois
- Masquer la complexité du schéma sous-jacent

**Limites :**

- Une vue n’**accélère pas** les requêtes — c’est juste une simplification d’écriture
- Modifier les données **à travers** une vue est limité et dépend du SGBD

> **À retenir :** les vues sont un outil de **lisibilité**, pas de performance. Pour la performance, on utilise les **index** (Ch.28).

#### Supprimer une vue

```sql
DROP VIEW active_loans;
```

> **📋 FIL ROUGE — Épisode 26**
> 
> Nora se rend compte qu’elle écrit la même requête (lecteurs + livres + emprunts) dix fois par jour, légèrement adaptée à chaque fois. Elle crée une vue :
> 
> ```sql
> CREATE VIEW v_loans_full AS
> SELECT l.id, r.first_name, r.last_name, b.title, c.name AS category, l.loan_date, l.status
> FROM loans AS l
> INNER JOIN readers AS r ON l.reader_id = r.id
> INNER JOIN books AS b ON l.book_id = b.id
> INNER JOIN categories AS c ON b.category_id = c.id;
> ```
> 
> Maintenant, n’importe quelle question sur les emprunts se résume à `SELECT ... FROM v_loans_full WHERE ...`. Plus simple, plus rapide à écrire, et l’équipe peut l’utiliser sans connaître le détail des jointures.

### ✅ Tu sais maintenant…

- Les bonnes pratiques d’écriture (indentation, majuscules, alias, commentaires)
- Les vues comme requêtes enregistrées (`CREATE VIEW`, `DROP VIEW`)
- Les vues simplifient l’écriture mais n’accélèrent pas les requêtes

-----


## Chapitre 28 — Index et performance : introduction

### Le minimum à savoir

#### Pourquoi une requête est-elle parfois lente ?

Quand tu écris `SELECT * FROM readers WHERE email = 'alice@example.com'`, le moteur doit parcourir **toutes les lignes** de la table pour trouver celles qui correspondent. Sur 15 lignes, c’est instantané. Sur 10 millions, c’est très lent.

**L’index** est la solution.

#### L’analogie du livre

Imagine un livre de 1000 pages. Tu cherches le mot “transaction”.

- **Sans index** : tu parcours toutes les pages une par une.
- **Avec un index** (à la fin du livre) : tu vas directement à la page indiquée.

Un **index SQL** fonctionne pareil — c’est une structure annexe qui pointe rapidement vers les lignes contenant une certaine valeur.

#### Créer un index

```sql
CREATE INDEX idx_readers_email
ON readers(email);
```

Décodage :

- `CREATE INDEX idx_readers_email` → un index nommé (par convention : `idx_table_colonne`)
- `ON readers(email)` → sur la colonne `email` de la table `readers`

Maintenant, `SELECT * FROM readers WHERE email = 'alice@example.com'` est ultra-rapide même avec des millions de lignes.

#### Les colonnes naturellement indexées

|Colonne                   |Indexée par défaut ?         |
|--------------------------|-----------------------------|
|`PRIMARY KEY`             |✅ Oui, automatiquement       |
|`UNIQUE`                  |✅ Oui, automatiquement       |
|Colonne avec `FOREIGN KEY`|❌ Non, à indexer manuellement|
|Colonnes ordinaires       |❌ Non                        |


> **À retenir :** les clés primaires et `UNIQUE` sont déjà indexées. Pour le reste — surtout les clés étrangères et les colonnes souvent filtrées — il faut créer l’index manuellement.

#### Quand créer un index ?

**Bonnes raisons :**

- Une colonne est souvent dans le `WHERE`
- Une colonne est souvent dans les conditions `JOIN ... ON`
- Une colonne est souvent dans `ORDER BY`

**Mauvaises raisons :**

- “Au cas où” → un index a un coût (voir ci-dessous)
- Indexer toutes les colonnes → ralentit énormément les écritures

#### Le coût d’un index

Un index a deux coûts :

1. **Espace disque** : l’index est une structure annexe qui prend de la place
1. **Ralentissement des écritures** : à chaque `INSERT`/`UPDATE`/`DELETE`, l’index doit être mis à jour

Sur les bases en lecture quasi-exclusive, indexer généreusement. Sur les bases en écriture intensive, indexer parcimonieusement. C’est un arbitrage classique.

#### Mention : `EXPLAIN QUERY PLAN`

SQLite (et tous les SGBD) ont une commande pour voir comment une requête sera exécutée :

```sql
EXPLAIN QUERY PLAN
SELECT * FROM readers WHERE email = 'alice@example.com';
```

Le résultat te dit si l’index est utilisé. C’est utile pour le debug de performance, mais c’est un sujet plus avancé — on le mentionne ici, on n’en fait pas plus.

> **📋 FIL ROUGE — Épisode 27**
> 
> La base est encore petite, mais Nora anticipe sa croissance. Elle ajoute deux index sur les colonnes les plus filtrées :
> 
> ```sql
> CREATE INDEX idx_loans_reader_id ON loans(reader_id);
> CREATE INDEX idx_loans_book_id ON loans(book_id);
> ```
> 
> Désormais, les jointures `loans` ↔ `readers` et `loans` ↔ `books` seront rapides même avec 100 000 emprunts.

### ❌ Erreur classique

```sql
-- Croire qu'indexer tout est gratuit
-- → Sur une table avec 50 colonnes, tu ne crées pas 50 index !
-- → Indexer ce qui est *réellement* utilisé dans WHERE / JOIN / ORDER BY

-- Oublier d'indexer une FOREIGN KEY
-- → Les jointures sur cette colonne seront lentes
-- → Toujours indexer les FK que tu joindras

-- Croire qu'un index sur (a, b) accélère un WHERE b = ...
-- → Un index composite est ordonné — il accélère a, ou (a, b), mais pas b seul
```

### ✅ Tu sais maintenant…

- Un index accélère les recherches comme l’index d’un livre
- Les `PRIMARY KEY` et `UNIQUE` sont auto-indexées
- Les `FOREIGN KEY` ne le sont **pas** par défaut — à indexer manuellement
- Un index a un coût (espace + écritures)
- `EXPLAIN QUERY PLAN` permet de vérifier l’utilisation des index

-----


## Chapitre 29 — Sécurité et SQL injection : aperçu défensif

> **Cadre de ce chapitre :** les exemples ci-dessous servent uniquement à comprendre le mécanisme de la vulnérabilité pour mieux s’en protéger. Ils ne doivent être testés que dans un environnement de lab personnel (ta propre base SQLite). Tester l’injection SQL sur un système qui ne t’appartient pas est illégal.

### Le minimum à savoir

#### Le problème : entrée utilisateur + concaténation

Imagine une application web qui cherche un livre par titre. L’utilisateur tape `Harry Potter` dans un formulaire, et le code construit une requête comme ça :

```python
# Code DANGEREUX (à NE PAS faire)
recherche = "Harry Potter"
requete = "SELECT * FROM books WHERE title = '" + recherche + "'"
```

La requête devient : `SELECT * FROM books WHERE title = 'Harry Potter'`. Tout va bien.

**Mais que se passe-t-il si l’utilisateur tape :**

```
' OR '1'='1
```

La requête devient : `SELECT * FROM books WHERE title = '' OR '1'='1'`. Comme `'1'='1'` est toujours vrai, **tous les livres sont retournés**. C’est l’**injection SQL** la plus simple.

Pire encore, avec une entrée comme :

```
'; DROP TABLE books; --
```

La requête devient : `SELECT * FROM books WHERE title = ''; DROP TABLE books; --'`. Le `;` clôt la première requête, le `DROP TABLE` détruit la table, et le `--` commente le reste. **La table `books` disparaît.**

#### Pourquoi c’est dangereux ?

L’injection SQL permet à un attaquant de :

- **Lire** des données qu’il ne devrait pas voir (mots de passe, données privées)
- **Modifier** des données (s’élever en admin, fausser des comptes)
- **Supprimer** des tables entières
- **Exécuter** des commandes selon le SGBD

C’est l’une des vulnérabilités web les plus anciennes et les plus répandues — encore aujourd’hui dans le top 10 OWASP.

#### La solution : les requêtes préparées

Au lieu de **concaténer** l’entrée utilisateur, on utilise des **paramètres** (placeholders). Le moteur SQL traite l’entrée comme une **valeur**, jamais comme du code.

```python
# Code SÛR (à faire)
recherche = "Harry Potter"
cursor.execute(
    "SELECT * FROM books WHERE title = ?",
    (recherche,)
)
```

Le `?` est un placeholder. La valeur passée comme tuple `(recherche,)` est traitée comme une chaîne, **pas interprétée comme du SQL**. Même si l’utilisateur tape `' OR '1'='1`, la chaîne complète est cherchée comme titre — aucune injection possible.

> **À retenir :** **ne concatène jamais d’entrée utilisateur dans une requête SQL**. Utilise toujours les paramètres de ton driver (`?` en SQLite, `%s` en PostgreSQL Python, `?` ou `:name` ailleurs). C’est la règle n°1 de la sécurité SQL.

#### Les autres bonnes pratiques

**Le principe de moindre privilège** : un compte applicatif ne devrait avoir que les permissions strictement nécessaires. Le compte qui sert le site web n’a pas besoin de pouvoir `DROP TABLE` ou `CREATE USER`.

**La validation côté application** : vérifier le format de l’entrée (un email ressemble-t-il à un email ? une date est-elle valide ?) avant de la passer à SQL. C’est une couche de défense supplémentaire.

**La journalisation** : enregistrer les requêtes (ou au moins celles qui échouent) permet de détecter une attaque en cours. C’est ce que fait la table `login_events` dans notre base.

> **📋 FIL ROUGE — Épisode 28**
> 
> Nora regarde la table `login_events` et constate quelque chose d’étrange :
> 
> ```sql
> SELECT username,
>        COUNT(*) AS nb_tentatives,
>        SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS echecs
> FROM login_events
> GROUP BY username
> ORDER BY echecs DESC;
> ```
> 
> Le compte `admin` a **10 échecs** suivis d’une **réussite**, tous depuis l’IP `203.0.113.42`. C’est le pattern typique d’une attaque par **brute-force réussie**. Nora alerte la directrice et bloque immédiatement le compte. Un audit est déclenché.
> 
> *Sans la journalisation des connexions et la capacité d’analyse SQL, cette attaque serait passée inaperçue.*

### Très utile en pratique

#### Détecter une attaque par brute-force

```sql
-- Comptes ayant subi plus de 5 échecs en moins de 10 minutes
SELECT username, ip_address, COUNT(*) AS nb_echecs,
       MIN(event_time) AS premier, MAX(event_time) AS dernier
FROM login_events
WHERE success = 0
GROUP BY username, ip_address
HAVING COUNT(*) >= 5
   AND julianday(MAX(event_time)) - julianday(MIN(event_time)) < 0.007;     -- ~10 min
```

C’est une requête de détection typique en cybersécurité. Le SQL est un outil **central** pour analyser les logs.

### ❌ Erreur classique

```python
# La concaténation, l'erreur n°1
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")    # ❌ injection possible

# Les f-strings ne protègent PAS — c'est juste de la concaténation déguisée
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")         # ❌ même problème

# La bonne approche : paramètres
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))        # ✅
```

### ✅ Tu sais maintenant…

- L’injection SQL exploite la concaténation d’entrées utilisateur
- Les requêtes préparées (paramètres `?`) protègent automatiquement
- Le principe de moindre privilège pour les comptes applicatifs
- La détection d’attaques via l’analyse des logs (le SQL est l’outil central)

-----


## Chapitre 30 — SQL depuis Python : passerelle

### Le minimum à savoir

Ce chapitre est volontairement court. Son but : **te donner le pont** entre ton cours Python et ton cours SQL. Tu sauras ouvrir une base, faire une requête, lire les résultats — c’est tout ce qu’il faut pour démarrer.

#### Le module `sqlite3`

Python intègre nativement le support de SQLite via le module `sqlite3` — pas besoin d’installer quoi que ce soit.

#### Le pattern minimal en 5 lignes

```python
import sqlite3

# 1. Se connecter à la base
conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# 2. Exécuter une requête
cursor.execute("SELECT first_name, last_name FROM readers WHERE city = 'Paris'")

# 3. Lire les résultats
for row in cursor.fetchall():
    print(row)

# 4. Fermer la connexion
conn.close()
```

Décodage :

- `connect()` ouvre la base (le fichier `.db`)
- `cursor()` crée un curseur — l’objet qui exécute les requêtes
- `execute()` lance une requête SQL
- `fetchall()` récupère toutes les lignes
- `close()` ferme proprement

#### Avec paramètres : la bonne pratique

**Toujours** utiliser les paramètres (`?` en SQLite) plutôt que la concaténation :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# Variable issue d'une entrée utilisateur (par exemple)
ville = "Paris"

# ❌ JAMAIS faire ça
# cursor.execute(f"SELECT * FROM readers WHERE city = '{ville}'")

# ✅ Toujours faire ça
cursor.execute(
    "SELECT first_name, last_name FROM readers WHERE city = ?",
    (ville,)            # tuple — n'oublie pas la virgule pour 1 seul paramètre
)

for row in cursor.fetchall():
    print(row)

conn.close()
```

> **À retenir :** la sécurité SQL en Python tient en une règle. **Ne jamais concaténer.** Toujours utiliser `?` et un tuple. Cette règle te protège de 99% des injections SQL.

#### Insérer, modifier, supprimer : `commit()` obligatoire

Pour les modifications, il faut explicitement valider avec `conn.commit()` :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
cursor = conn.cursor()

# Insérer une ligne
cursor.execute(
    "INSERT INTO readers (first_name, last_name, registration_date) VALUES (?, ?, ?)",
    ("Marie", "Lefort", "2026-05-03")
)

conn.commit()           # ← VALIDER les modifications
conn.close()
```

Sans `commit()`, les modifications sont perdues à la fermeture. C’est l’équivalent du `COMMIT` SQL qu’on a vu au Ch.23.

#### Le `with` : commit/rollback automatique

Python permet d’utiliser `with` pour gérer automatiquement les transactions sur une connexion SQLite :

```python
import sqlite3

conn = sqlite3.connect("bibliotheque.db")
try:
    with conn:                    # ← gère le commit/rollback automatique
        cursor = conn.cursor()
        cursor.execute("INSERT INTO readers (first_name, last_name, registration_date) VALUES (?, ?, ?)",
                       ("Marie", "Lefort", "2026-05-03"))
        # Si tout va bien à la sortie du with → COMMIT automatique
        # Si une exception est levée → ROLLBACK automatique
finally:
    conn.close()                  # fermeture explicite
```

> **⚠️ Attention à un piège fréquent :** avec `sqlite3`, le bloc `with` **ne ferme pas** la connexion — il gère seulement la transaction (commit en cas de succès, rollback en cas d’erreur). Pour fermer proprement, il faut un `conn.close()` explicite (typiquement dans un `finally`, ou en utilisant `contextlib.closing`).

Pour avoir une vraie fermeture automatique, on peut combiner avec `contextlib.closing` :

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect("bibliotheque.db")) as conn:
    with conn:                    # transaction (commit/rollback)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM readers")
        for row in cursor.fetchall():
            print(row)
# Ici la connexion est fermée automatiquement
```

Pour démarrer, retiens simplement : **`with conn:` gère la transaction, `conn.close()` ferme la connexion**. Les deux sont à connaître.

> **📋 FIL ROUGE — Épisode 29**
> 
> Nora veut automatiser un rapport quotidien. Plutôt que d’ouvrir DB Browser chaque matin, elle écrit un petit script Python :
> 
> ```python
> import sqlite3
> 
> conn = sqlite3.connect("bibliotheque.db")
> try:
>     cursor = conn.cursor()
> 
>     cursor.execute("SELECT COUNT(*) FROM loans WHERE status = 'late'")
>     nb_retards = cursor.fetchone()[0]
> 
>     cursor.execute("SELECT COUNT(*) FROM readers")
>     nb_lecteurs = cursor.fetchone()[0]
> 
>     print(f"Rapport du jour : {nb_lecteurs} lecteurs, {nb_retards} emprunts en retard")
> finally:
>     conn.close()
> ```
> 
> Quelques lignes — et le script peut être lancé chaque matin par une tâche planifiée. C’est exactement la passerelle entre SQL et Python qu’elle cherchait.

### Très utile en pratique

#### `fetchall()`, `fetchone()`, `fetchmany(n)`

|Méthode       |Renvoie                                   |
|--------------|------------------------------------------|
|`fetchall()`  |Toutes les lignes (liste de tuples)       |
|`fetchone()`  |Une seule ligne (tuple), ou `None` si vide|
|`fetchmany(n)`|Les n prochaines lignes                   |

Pour des requêtes qui ne renvoient qu’une valeur (comme `COUNT(*)`), `fetchone()[0]` est idéal.

#### Le résultat sous forme de dictionnaire

Par défaut, les lignes sont des **tuples** (`row[0]`, `row[1]`…). Pour les avoir comme dictionnaires (`row['first_name']`) :

```python
conn = sqlite3.connect("bibliotheque.db")
conn.row_factory = sqlite3.Row     # ← active le mode "dict-like"
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name FROM readers")
for row in cursor.fetchall():
    print(row['first_name'], row['last_name'])
```

Plus lisible quand tu as beaucoup de colonnes.

### ❌ Erreur classique

```python
# Oublier le commit après une modification
cursor.execute("INSERT INTO readers ...")
# pas de commit → perdu

# Concaténation au lieu de paramètres
cursor.execute(f"SELECT * FROM readers WHERE id = {user_id}")    # ❌ injection
cursor.execute("SELECT * FROM readers WHERE id = ?", (user_id,)) # ✅

# Oublier la virgule dans le tuple à 1 élément
cursor.execute("SELECT * FROM readers WHERE id = ?", (1))     # ❌ "1" n'est pas un tuple
cursor.execute("SELECT * FROM readers WHERE id = ?", (1,))    # ✅ tuple à 1 élément
```

### ✅ Tu sais maintenant…

- Le pattern minimal `sqlite3` en Python : `connect`, `cursor`, `execute`, `fetchall`, `close`
- Toujours utiliser `?` et un tuple, jamais la concaténation
- `commit()` obligatoire pour les modifications
- `with conn:` gère automatiquement le commit/rollback, mais **ne ferme pas** la connexion
- `conn.close()` (souvent dans un `finally`) ferme explicitement la connexion
- C’est ta passerelle vers le cours Python complet

-----
