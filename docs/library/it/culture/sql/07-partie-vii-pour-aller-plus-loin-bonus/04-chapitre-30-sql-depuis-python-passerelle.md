---
title: 'Chapitre 30 — SQL depuis Python : passerelle'
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VII — Pour aller plus loin — 🔴 Bonus
  - index.md
---

## Le minimum à savoir

Ce chapitre est volontairement court. Son but : **te donner le pont** entre ton cours Python et ton cours SQL. Tu sauras ouvrir une base, faire une requête, lire les résultats — c’est tout ce qu’il faut pour démarrer.

### Le module `sqlite3`

Python intègre nativement le support de SQLite via le module `sqlite3` — pas besoin d’installer quoi que ce soit.

### Le pattern minimal en 5 lignes

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

### Avec paramètres : la bonne pratique

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

### Insérer, modifier, supprimer : `commit()` obligatoire

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

### Le `with` : commit/rollback automatique

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

## Très utile en pratique

### `fetchall()`, `fetchone()`, `fetchmany(n)`

|Méthode       |Renvoie                                   |
|--------------|------------------------------------------|
|`fetchall()`  |Toutes les lignes (liste de tuples)       |
|`fetchone()`  |Une seule ligne (tuple), ou `None` si vide|
|`fetchmany(n)`|Les n prochaines lignes                   |

Pour des requêtes qui ne renvoient qu’une valeur (comme `COUNT(*)`), `fetchone()[0]` est idéal.

### Le résultat sous forme de dictionnaire

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

## ❌ Erreur classique

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


## ✅ Tu sais maintenant…

- Le pattern minimal `sqlite3` en Python : `connect`, `cursor`, `execute`, `fetchall`, `close`
- Toujours utiliser `?` et un tuple, jamais la concaténation
- `commit()` obligatoire pour les modifications
- `with conn:` gère automatiquement le commit/rollback, mais **ne ferme pas** la connexion
- `conn.close()` (souvent dans un `finally`) ferme explicitement la connexion
- C’est ta passerelle vers le cours Python complet

-----
