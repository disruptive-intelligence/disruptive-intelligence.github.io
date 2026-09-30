---
title: Chapitre 10 — Capstone Partie II
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie II — Construire ET composer
  - index.md
---

containeriser une application complète

Cet exercice intègre tout ce que tu as appris dans les chapitres 6 à 9.

## L’exercice

**Objectif :** containeriser une application web multi-composants et la déployer avec Docker Compose.

**L’application :** un blog simple avec :

- Un **backend** Python/Flask (ou Django) qui sert l’API
- Une **base de données** PostgreSQL
- Un **cache** Redis
- Un **reverse proxy** Nginx

**Les étapes :**

1. **Écrire le Dockerfile** pour le backend :
- Image de base `slim`
- Multi-stage build
- Utilisateur non-root
- `.dockerignore` complet
1. **Écrire le `docker-compose.yml`** :
- 4 services (backend, db, redis, nginx)
- Volume persistant pour PostgreSQL
- Bind mount pour le code source (développement)
- Fichier `.env` pour les variables sensibles
- Réseau nommé
- Health check sur PostgreSQL
1. **Scanner l’image** avec Trivy
1. **Documenter** : un `README.md` avec les instructions de démarrage

**Checklist de validation :**

|Critère                                                           |Vérifié ?|
|------------------------------------------------------------------|---------|
|L’image backend fait moins de 200 Mo                              |         |
|Le scan Trivy ne montre aucune CVE critique                       |         |
|L’application tourne avec un utilisateur non-root                 |         |
|Les données PostgreSQL survivent à un `docker compose down` + `up`|         |
|Les secrets ne sont pas dans le Dockerfile ni dans le YAML        |         |
|Le `.dockerignore` exclut `.git`, `.env`, `__pycache__`           |         |
|`docker compose up -d` lance tout en une commande                 |         |
|L’application est accessible sur `http://localhost`               |         |


> **📋 CONTAINER — Épisode 5 (partie 2)**
> 
> Sami livre la stack Docker Compose de MedFlow. Résultat : image de production 180 Mo (vs 1.2 Go au départ), scan Trivy propre, utilisateur non-root, secrets dans un `.env` hors du repo Git. Le nouveau développeur qui rejoint l’équipe clone le repo et fait `docker compose up -d` — tout l’environnement de développement est prêt en 2 minutes. Le CTO est convaincu. Prochaine étape : Kubernetes pour la production.

## ✅ Tu sais maintenant…

- Containeriser une application multi-composants de A à Z
- Appliquer les bonnes pratiques : multi-stage, non-root, scan, secrets externalisés
- Documenter pour que n’importe qui puisse lancer la stack

-----
