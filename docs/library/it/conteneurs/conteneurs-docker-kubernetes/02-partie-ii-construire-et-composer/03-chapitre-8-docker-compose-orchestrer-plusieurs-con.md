---
title: 'Chapitre 8 — Docker Compose : orchestrer plusieurs containers'
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie II — Construire et composer
  - index.md
---

## Le minimum à savoir

### Le problème

Au chapitre 5, on a lancé 3 containers avec 3 commandes `docker run` séparées. Chaque commande a une douzaine de flags (-d, -p, -v, -e, –name, –network). C’est ingérable dès que l’application a plus de 2 services. Et si tu dois partager la configuration avec un collègue, il doit retaper les mêmes commandes.

**Docker Compose** résout ça : tu décris toute ta stack dans **un seul fichier YAML**, et tu la lances avec **une seule commande**.

### Le fichier `docker-compose.yml`

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db/medflow
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=medflow

  redis:
    image: redis:7

volumes:
  pgdata:
```


Ce fichier remplace les 3 commandes `docker run` du chapitre 5. Docker Compose crée automatiquement un réseau dédié et y connecte tous les services.

### Les commandes Compose

```bash
# Lancer toute la stack en arrière-plan
docker compose up -d

# Voir l'état des services
docker compose ps

# Voir les logs de tous les services
docker compose logs

# Voir les logs d'un service spécifique
docker compose logs web

# Arrêter et supprimer tout (containers + réseau, mais PAS les volumes)
docker compose down

# Arrêter et supprimer tout Y COMPRIS les volumes (⚠️ données perdues)
docker compose down -v

# Reconstruire les images après un changement de Dockerfile
docker compose build
docker compose up -d --build    # build + relance en une commande
```


> **Note :** la commande est `docker compose` (avec un espace, pas un tiret). L’ancienne syntaxe `docker-compose` (avec un tiret) est dépréciée.

### Décortiquer le fichier

```yaml
services:           # La liste des containers à lancer
  web:              # Nom du service (= nom du container sur le réseau)
    build: .        # Construit l'image depuis le Dockerfile dans le dossier courant
    # OU
    image: nginx:1.25   # Utilise une image existante
    
    ports:
      - "8000:8000"     # Mapping de port hôte:container
    
    volumes:
      - ./code:/app     # Bind mount (développement)
      - data:/var/lib/data   # Volume nommé (persistance)
    
    environment:        # Variables d'environnement
      - DEBUG=true
      - DB_HOST=db
    
    depends_on:         # Ce service démarre après db et redis
      - db
      - redis

volumes:            # Déclaration des volumes nommés
  data:
```


> **`depends_on` :** attention, `depends_on` garantit l’**ordre de démarrage** des containers, mais PAS que le service est prêt. PostgreSQL peut être démarré (le container tourne) mais pas encore prêt à accepter des connexions (le serveur SQL n’a pas fini de s’initialiser). En production, l’application doit gérer les retries de connexion.

> **📋 CONTAINER — Épisode 5 (partie 1)**
> 
> Sami écrit le `docker-compose.yml` de MedFlow : Django (build depuis le Dockerfile) + PostgreSQL (image officielle, volume persistant) + Redis (image officielle, pas de volume) + Celery (même image que Django, commande différente) + Nginx (reverse proxy). Un `docker compose up -d` et toute la stack tourne. Le nouveau développeur qui arrive fait un `git clone` + `docker compose up -d` et a tout l’environnement de développement en 2 minutes.

## Très utile en pratique

### Un Compose complet pour MedFlow

```yaml
services:
  web:
    build: .
    command: gunicorn medflow.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./src:/app
      - static:/app/static
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
      - REDIS_URL=redis://redis:6379
      - SECRET_KEY=dev-secret-key-change-in-prod
    depends_on:
      - db
      - redis

  celery:
    build: .
    command: celery -A medflow worker --loglevel=info
    volumes:
      - ./src:/app
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=medflow
    ports:
      - "127.0.0.1:5432:5432"

  redis:
    image: redis:7-alpine

  nginx:
    image: nginx:1.25
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - static:/app/static:ro
    depends_on:
      - web

volumes:
  pgdata:
  static:
```


### Les fichiers `.env` pour les variables

Au lieu de mettre les variables en clair dans le YAML :

```bash
# Fichier .env (à la racine, à côté de docker-compose.yml)
POSTGRES_PASSWORD=secret
DATABASE_URL=postgresql://postgres:secret@db:5432/medflow
SECRET_KEY=ma-cle-secrete
```


```yaml
# docker-compose.yml
services:
  web:
    build: .
    env_file:
      - .env
```


> **Sécurité :** le fichier `.env` doit être dans le `.gitignore` — ne jamais commiter des secrets dans Git.

### Exécuter des commandes dans un service

```bash
# Ouvrir un shell dans le container web
docker compose exec web bash

# Lancer une migration Django
docker compose exec web python manage.py migrate

# Créer un superuser
docker compose exec web python manage.py createsuperuser
```


## Bonus

### Les profils (pour les services optionnels)

```yaml
services:
  web:
    build: .
    # ...
  
  debug:
    image: busybox
    profiles:
      - debug
    command: sleep infinity
```


```bash
docker compose up -d              # Lance web uniquement
docker compose --profile debug up -d   # Lance web + debug
```


### Health checks dans Compose

```yaml
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
  
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy    # Attend que db soit VRAIMENT prête
```


## ❌ Erreur classique

```yaml
# Oublier de déclarer les volumes nommés
services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
# ❌ Erreur : volume "pgdata" non déclaré
# Il faut ajouter :
volumes:
  pgdata:

# Indentation YAML incorrecte
services:
web:           # ❌ Il manque 2 espaces d'indentation
    image: nginx

services:
  web:         # ✅ Correct
    image: nginx

# Utiliser docker-compose (avec tiret) au lieu de docker compose (avec espace)
docker-compose up    # ⚠️ Ancienne syntaxe, dépréciée
docker compose up    # ✅ Syntaxe actuelle
```


## ✅ Tu sais maintenant…

- Décrire une stack multi-containers dans un fichier `docker-compose.yml`
- Les commandes : `up -d`, `down`, `logs`, `exec`, `build`, `ps`
- Les options clés : `build`, `image`, `ports`, `volumes`, `environment`, `depends_on`
- Utiliser un fichier `.env` pour les variables sensibles

-----
