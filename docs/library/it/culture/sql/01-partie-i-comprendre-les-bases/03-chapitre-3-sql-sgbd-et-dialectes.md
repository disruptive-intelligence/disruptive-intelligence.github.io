---
title: Chapitre 3 — SQL, SGBD et dialectes
source: IT/Culture/SQL.md
note: SQL
up:
- - SQL
  - ../index.md
- - Partie I — Comprendre les bases
  - index.md
---

## Le minimum à savoir

### SQL vs SGBD : la confusion classique

Beaucoup de débutants confondent **SQL** et le **moteur** de base de données. C’est comme confondre “le français” et “un livre français”.

|Concept |Définition                                                     |Exemples                                             |
|--------|---------------------------------------------------------------|-----------------------------------------------------|
|**SQL** |Le **langage** standardisé pour parler aux bases relationnelles|(un seul SQL — défini par les normes ISO)            |
|**SGBD**|Le **moteur** qui exécute le SQL                               |SQLite, PostgreSQL, MySQL/MariaDB, SQL Server, Oracle|


> **Phrase à retenir :** SQL est le langage. SQLite, PostgreSQL, MySQL ou SQL Server sont des moteurs qui comprennent ce langage avec quelques variantes.

### Les SGBD que tu rencontreras

|SGBD               |Particularité                           |Cas d’usage typique                                           |
|-------------------|----------------------------------------|--------------------------------------------------------------|
|**SQLite**         |Léger (un fichier `.db`), pas de serveur|Apps mobiles, sites web légers, prototypage, **apprentissage**|
|**PostgreSQL**     |Open source, très complet, robuste      |Applications web modernes, data, géographie                   |
|**MySQL / MariaDB**|Open source, très répandu               |Sites web (WordPress, etc.), applis classiques                |
|**SQL Server**     |Microsoft, solide en entreprise         |ERP, environnements Windows                                   |
|**Oracle**         |Historique, puissant, payant            |Grandes banques, ERP critiques                                |

**Tous comprennent le SQL standard.** Si tu sais écrire `SELECT * FROM users WHERE city = 'Paris'`, ça marche partout.

### Les dialectes : les petites différences

Chaque SGBD ajoute ses propres extensions au SQL standard. C’est ce qu’on appelle un **dialecte**.

Exemples :

|Tâche                |SQLite               |PostgreSQL            |MySQL             |
|---------------------|---------------------|----------------------|------------------|
|Concaténer du texte  |`'a' || 'b'`         |`'a' || 'b'`          |`CONCAT('a', 'b')`|
|Date du jour         |`DATE('now')`        |`CURRENT_DATE`        |`CURDATE()`       |
|Auto-incrément       |`INTEGER PRIMARY KEY`|`SERIAL` ou `IDENTITY`|`AUTO_INCREMENT`  |
|Limiter les résultats|`LIMIT 10`           |`LIMIT 10`            |`LIMIT 10`        |

**90% du SQL est identique entre tous les SGBD.** Les 10% qui varient sont les fonctions de date, l’auto-incrément, la concaténation, et quelques détails. On apprend SQLite dans ce cours, mais ce que tu apprends est transférable à 90% sur PostgreSQL ou MySQL.

### Pourquoi SQLite pour ce cours ?

Pour apprendre, SQLite est imbattable :

- **Pas de serveur** : la base est un seul fichier `.db` — tu copies, tu déplaces, tu sauvegardes facilement
- **Installation triviale** : déjà inclus dans Python, dans macOS, dans la plupart des Linux
- **Outils gratuits** : DB Browser for SQLite te donne une interface graphique en 2 minutes
- **Syntaxe SQL standard** : ce que tu apprends marchera (à 90%) sur PostgreSQL et MySQL
- **Suffisant pour de vraies applications** : SQLite est utilisé par des milliards d’apps mobiles, le navigateur Firefox, etc.

> **À retenir :** apprendre sur SQLite **n’est pas** apprendre un truc obsolète ou un jouet. C’est apprendre SQL avec l’environnement le plus simple possible. Tu transféreras 90% de ce que tu sais quand tu passeras à PostgreSQL ou MySQL.

## ✅ Tu sais maintenant…

- SQL est le **langage**, le SGBD est le **moteur**
- Les SGBD principaux : SQLite, PostgreSQL, MySQL, SQL Server, Oracle
- Les **dialectes** sont les petites variantes propres à chaque moteur
- SQLite est parfait pour apprendre — et ce que tu apprends est transférable

-----
