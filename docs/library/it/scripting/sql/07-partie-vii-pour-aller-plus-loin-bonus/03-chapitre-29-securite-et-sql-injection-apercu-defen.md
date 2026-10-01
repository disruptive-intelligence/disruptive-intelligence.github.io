---
title: 'Chapitre 29 — Sécurité et SQL injection : aperçu défensif'
source: IT/07 Scripting & programmation/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VII — Pour aller plus loin — 🔴 Bonus
  - index.md
---

> **Cadre de ce chapitre :** les exemples ci-dessous servent uniquement à comprendre le mécanisme de la vulnérabilité pour mieux s’en protéger. Ils ne doivent être testés que dans un environnement de lab personnel (ta propre base SQLite). Tester l’injection SQL sur un système qui ne t’appartient pas est illégal.

## Le minimum à savoir

### Le problème : entrée utilisateur + concaténation

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

### Pourquoi c’est dangereux ?

L’injection SQL permet à un attaquant de :

- **Lire** des données qu’il ne devrait pas voir (mots de passe, données privées)
- **Modifier** des données (s’élever en admin, fausser des comptes)
- **Supprimer** des tables entières
- **Exécuter** des commandes selon le SGBD

C’est l’une des vulnérabilités web les plus anciennes et les plus répandues — encore aujourd’hui dans le top 10 OWASP.

### La solution : les requêtes préparées

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

### Les autres bonnes pratiques

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

## Très utile en pratique

### Détecter une attaque par brute-force

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

## ❌ Erreur classique

```python
# La concaténation, l'erreur n°1
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")    # ❌ injection possible

# Les f-strings ne protègent PAS — c'est juste de la concaténation déguisée
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")         # ❌ même problème

# La bonne approche : paramètres
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))        # ✅
```


## ✅ Tu sais maintenant…

- L’injection SQL exploite la concaténation d’entrées utilisateur
- Les requêtes préparées (paramètres `?`) protègent automatiquement
- Le principe de moindre privilège pour les comptes applicatifs
- La détection d’attaques via l’analyse des logs (le SQL est l’outil central)

-----
