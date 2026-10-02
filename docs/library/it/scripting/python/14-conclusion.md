---
title: Conclusion
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - index.md
---

Tu es parti de zéro et tu disposes maintenant d'une vraie base : écrire des scripts Python clairs, structurés et **orientés défense**.

**Partie 1 — Les fondamentaux :**

- Script, variables, arguments (ch. 1-3)
- Calculs, logique, conditions (ch. 4-5)
- Chaînes, listes, boucles, fonctions, dictionnaires (ch. 6-9)
- Fichiers, CSV, JSON, erreurs, automatisation (ch. 10-12)

**Partie 2 — La cybersécurité défensive :**

- Regex et extraction d'IOC (ch. 13)
- Parsing de logs (ch. 14)
- Manipulation d'IOC (ch. 15)
- APIs et `requests` (ch. 16)
- JSON avancé CTI/SIEM (ch. 17)
- Hash avec `hashlib` (ch. 18)
- IP et réseaux avec `ipaddress` (ch. 19)
- Mini-projets défensifs (ch. 20)

**Pour continuer à progresser :**

- Écris des scripts pour tes propres besoins d'analyse — c'est la meilleure façon d'apprendre.
- `help(fonction)` dans le mode interactif reste ton meilleur ami.
- La documentation officielle [docs.python.org](https://docs.python.org) est excellente.
- Entraîne-toi sur des **logs et données de test** que tu génères toi-même, jamais sur des systèmes qui ne t'appartiennent pas.

**Prochaines étapes possibles (toujours côté défense) :**

- Approfondir les regex pour des formats de logs plus variés.
- Automatiser l'enrichissement d'IOC via plusieurs sources CTI.
- Stocker tes résultats dans une base `sqlite3` pour les requêter.
- Découvrir des bibliothèques d'analyse comme `pandas` pour de gros volumes de logs.
- Planifier tes scripts (cron) pour une surveillance continue.

**Rappel final d'éthique :** ces compétences servent à **protéger, détecter et comprendre**. N'analyse que des systèmes et des données que tu es autorisé à examiner. La cybersécurité défensive, c'est d'abord une question de responsabilité.

Bon scripting, et bonne défense !
