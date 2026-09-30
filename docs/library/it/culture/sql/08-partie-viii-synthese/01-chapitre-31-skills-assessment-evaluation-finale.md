---
title: Chapitre 31 — Skills Assessment — Évaluation finale
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie VIII — Synthèse
  - index.md
---

## Objectif

Tu vas exploiter une base **inconnue à toi** (mais que tu as construite au Ch.4) — la base `bibliotheque.db`. Réponds aux 12 questions ci-dessous en écrivant les requêtes SQL correspondantes.

**Cette évaluation valide :**

- Lecture de données (Ch.5-10)
- Calculs et agrégations (Ch.11-14)
- Jointures (Ch.15-19)
- Modifications avec sécurité (Ch.20-23)
- Compréhension du modèle (Ch.2, 15)
- Détection d’anomalies (angle cyber)

## Préparation

```sql
-- Vérifier que la base est bien chargée
.tables
-- Doit lister : authors, book_authors, books, categories, loans, login_events, readers, staff_users
```


## Les 12 questions

**1. Combien y a-t-il de lecteurs au total ?**

<details markdown="1">
<summary>💡 Indice</summary>

Une simple agrégation `COUNT(*)` sur la table `readers`.

</details>

-----

**2. Quels sont les 10 derniers lecteurs inscrits ? (nom, prénom, date d’inscription)**

<details markdown="1">
<summary>💡 Indice</summary>

`ORDER BY registration_date DESC` + `LIMIT 10`.

</details>

-----

**3. Quels livres n’ont jamais été empruntés ?**

<details markdown="1">
<summary>💡 Indice</summary>

`LEFT JOIN` entre `books` et `loans`, puis `WHERE l.id IS NULL`.

</details>

-----

**4. Quels sont les 5 lecteurs ayant le plus emprunté ? (nom + nombre d’emprunts)**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `readers` + `loans`, `GROUP BY` sur le lecteur, `ORDER BY COUNT(*) DESC LIMIT 5`.

</details>

-----

**5. Quels lecteurs ont des emprunts en retard ? (nom + titre du livre)**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `readers` + `loans` + `books`, `WHERE l.status = 'late'`.

</details>

-----

**6. Combien de livres existe-t-il par catégorie ? (catégorie + nombre, trié)**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `books` + `categories`, `GROUP BY c.name`, `ORDER BY COUNT(*) DESC`.

</details>

-----

**7. Quel(s) auteur(s) est/sont le(s) plus emprunté(s) ?**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `loans` + `books` + `book_authors` + `authors`, `GROUP BY` sur l’auteur, trier par nombre.

</details>

-----

**8. Quels lecteurs n’ont jamais emprunté ?**

<details markdown="1">
<summary>💡 Indice</summary>

Comme la question 3, mais cette fois `LEFT JOIN` depuis `readers`.

</details>

-----

**9. Quels emails de lecteurs sont en double dans la base ?**

<details markdown="1">
<summary>💡 Indice</summary>

`GROUP BY email` puis `HAVING COUNT(*) > 1`.

</details>

-----

**10. Quels comptes du personnel ont eu le plus d’échecs de connexion ? (cyber)**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `staff_users` + `login_events`, `WHERE success = 0`, `GROUP BY` sur l’utilisateur.

</details>

-----

**11. Quels livres ont été empruntés au moins 2 fois ?**

<details markdown="1">
<summary>💡 Indice</summary>

Jointure `books` + `loans`, `GROUP BY` sur le livre, `HAVING COUNT(*) >= 2`.

</details>

-----

**12. Question synthèse : écris une requête qui résume l’activité d’**Alice Martin** (id=1) — combien d’emprunts au total, combien retournés, combien en cours, combien en retard.**

<details markdown="1">
<summary>💡 Indice</summary>

Une seule requête avec plusieurs `COUNT` conditionnels :

```sql
COUNT(*) AS total,
COUNT(CASE WHEN status = 'returned' THEN 1 END) AS retournes,
...
```


</details>

## Bonus cyber : la tentative de brute-force

Regarde la table `login_events` : tu y verras **10 échecs** sur le compte `admin` depuis l’IP `203.0.113.42`, suivis d’**1 réussite** depuis la même IP. C’est le pattern typique d’une attaque par brute-force qui a réussi.

Écris une requête simple qui détecte un compte ayant subi beaucoup d’échecs **et** au moins une réussite depuis la même IP :

```sql
SELECT username, ip_address,
       COUNT(*) AS nb_total,
       SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) AS nb_echecs,
       SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) AS nb_succes
FROM login_events
GROUP BY username, ip_address
HAVING nb_echecs >= 5 AND nb_succes >= 1;
```


> **Limite de cette requête :** elle détecte **beaucoup d’échecs + au moins une réussite** depuis la même IP, mais ne prouve pas formellement que les échecs sont consécutifs ni que la réussite vient *après*. Pour cela, il faudrait des fonctions de fenêtre (window functions) — un sujet plus avancé. En pratique, cette requête simple suffit comme **premier signal d’alerte** : un analyste reprendra ensuite manuellement les événements triés par date pour confirmer.

## Solutions

Les solutions complètes sont disponibles dans l’**Annexe F — Requêtes types**. Mais essaie d’abord par toi-même !

-----
