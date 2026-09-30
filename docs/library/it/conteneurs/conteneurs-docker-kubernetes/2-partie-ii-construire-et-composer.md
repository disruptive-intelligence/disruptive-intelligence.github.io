---
title: PARTIE II — CONSTRUIRE ET COMPOSER
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 2
chapters: 7
---

-----


## Chapitre 6 — Écrire un Dockerfile : de zéro à l’image

### Le minimum à savoir

#### Qu’est-ce qu’un Dockerfile ?

Un Dockerfile est un **fichier texte** qui décrit, étape par étape, comment construire une image Docker. C’est la recette de construction de ton container. Chaque ligne est une instruction que Docker exécute dans l’ordre.

#### Le prérequis : comprendre YAML et les fichiers de configuration

Avant d’aller plus loin, un mot sur les fichiers de configuration. Docker utilise des Dockerfiles (syntaxe propre), Docker Compose utilise des fichiers YAML, et Kubernetes utilise aussi du YAML. Le YAML est un format texte structuré très lisible, basé sur l’**indentation** (comme Python). Voici un aperçu rapide :

```yaml
# Ceci est un commentaire YAML
nom: Alice
age: 25
langages:
  - Python
  - Bash
  - Go
serveur:
  host: 192.168.1.1
  port: 8080
```

Les règles essentielles du YAML : **2 espaces** pour l’indentation (pas de tabulations), les listes commencent par un tiret (`-`), les clés-valeurs sont séparées par un deux-points et un espace (`clé: valeur`). On utilisera le YAML à partir du chapitre 8 (Docker Compose) et du chapitre 14 (Kubernetes).

#### Les instructions essentielles du Dockerfile

```dockerfile
# Chaque Dockerfile commence par FROM — l'image de base
FROM python:3.12-slim

# Définir le dossier de travail dans le container
WORKDIR /app

# Copier des fichiers depuis ta machine vers le container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables d'environnement
ENV FLASK_APP=app.py

# Port que l'application écoute (documentaire — n'expose pas réellement)
EXPOSE 5000

# La commande qui se lance quand le container démarre
CMD ["python", "app.py"]
```

Détaillons chaque instruction :

|Instruction |Rôle                                                  |Exemple                   |
|------------|------------------------------------------------------|--------------------------|
|`FROM`      |Image de base (obligatoire, toujours en premier)      |`FROM python:3.12-slim`   |
|`WORKDIR`   |Définit le dossier de travail                         |`WORKDIR /app`            |
|`COPY`      |Copie des fichiers de l’hôte vers l’image             |`COPY app.py /app/`       |
|`RUN`       |Exécute une commande pendant la construction          |`RUN pip install flask`   |
|`ENV`       |Définit une variable d’environnement                  |`ENV DEBUG=false`         |
|`EXPOSE`    |Documente le port utilisé (ne l’expose pas réellement)|`EXPOSE 8080`             |
|`CMD`       |Commande par défaut au démarrage du container         |`CMD ["python", "app.py"]`|
|`ENTRYPOINT`|Point d’entrée fixe (CMD devient les arguments)       |`ENTRYPOINT ["python"]`   |

#### Construire et tester

**Étape 1 — Crée une application simple** (`app.py`) :

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello depuis un container Docker !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**Étape 2 — Crée le fichier des dépendances** (`requirements.txt`) :

```
flask==3.0.*
```

**Étape 3 — Crée le Dockerfile :**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Étape 4 — Construis l’image :**

```bash
docker build -t mon_app .
```

`-t mon_app` donne un nom (tag) à l’image. Le `.` indique que le contexte de build est le dossier actuel.

**Étape 5 — Lance le container :**

```bash
docker run -d -p 5000:5000 mon_app
```

Ouvre `http://localhost:5000` — tu vois “Hello depuis un container Docker !”

#### Le `.dockerignore`

Comme un `.gitignore`, le `.dockerignore` exclut des fichiers du contexte de build. C’est important pour la **performance** (ne pas envoyer des Go de fichiers inutiles au daemon Docker) et la **sécurité** (ne pas inclure de secrets dans l’image).

```
# .dockerignore
.git
.env
__pycache__
*.pyc
node_modules
.vscode
```

> **📋 CONTAINER — Épisode 4 (partie 1)**
> 
> Sami écrit le Dockerfile pour l’application Django de MedFlow. Première version : image de base `python:3.12` (image complète), pas de `.dockerignore`, copie de tout le repo (y compris le `.git` de 200 Mo et le fichier `.env` avec les secrets). L’image fait 1.2 Go. Premier réflexe d’optimisation au chapitre suivant.

### Très utile en pratique

#### L’ordre des instructions : optimiser le cache

Docker met en cache chaque couche. Si une instruction n’a pas changé, Docker réutilise le cache au lieu de la reconstruire. L’astuce : **mettre les instructions qui changent le moins souvent en premier**.

```dockerfile
# ✅ BON ORDRE — les dépendances changent rarement, le code change souvent
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .              # ← Change rarement
RUN pip install --no-cache-dir -r requirements.txt   # ← Mis en cache si requirements.txt n'a pas changé
COPY . .                              # ← Change à chaque modification du code
CMD ["python", "app.py"]

# ❌ MAUVAIS ORDRE — tout est reconstruit à chaque changement de code
FROM python:3.12-slim
WORKDIR /app
COPY . .                              # ← Change à chaque modification
RUN pip install --no-cache-dir -r requirements.txt   # ← Reconstruit à chaque fois !
CMD ["python", "app.py"]
```

#### La différence CMD vs ENTRYPOINT

`CMD` est la commande par défaut, remplaçable à l’exécution. `ENTRYPOINT` est le point d’entrée fixe.

```dockerfile
# Avec CMD — la commande peut être remplacée
CMD ["python", "app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app python test.py     → exécute python test.py (remplace CMD)

# Avec ENTRYPOINT + CMD — ENTRYPOINT est fixe, CMD fournit les arguments par défaut
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app test.py            → exécute python test.py
```

Pour un débutant, utilise `CMD`. `ENTRYPOINT` est utile quand ton container est un outil en ligne de commande.

### Bonus

#### Les labels

Les labels ajoutent des métadonnées à l’image :

```dockerfile
LABEL maintainer="sami@example.com"
LABEL version="1.0"
LABEL description="Application MedFlow"
```

#### Les arguments de build (ARG)

`ARG` permet de passer des variables au moment du build (pas au runtime) :

```dockerfile
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim
```

```bash
docker build --build-arg PYTHON_VERSION=3.11 -t mon_app .
```

> **Attention sécurité :** ne passe JAMAIS de secrets via `ARG`. Les valeurs `ARG` sont visibles dans l’historique des couches (`docker history`).

### ❌ Erreur classique

```dockerfile
# Mettre COPY . . avant RUN pip install → le cache est invalidé à chaque changement de code

# Oublier --no-cache-dir dans pip install → l'image est plus grosse pour rien
RUN pip install flask                        # ❌ Conserve le cache pip dans l'image
RUN pip install --no-cache-dir flask         # ✅ Pas de cache inutile

# Utiliser ADD au lieu de COPY (sauf besoin spécifique)
ADD app.py /app/     # ❌ ADD fait des choses en plus (décompression, URL) — trop magique
COPY app.py /app/    # ✅ COPY est simple et prévisible
```

### ✅ Tu sais maintenant…

- Écrire un Dockerfile de base (`FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`)
- Construire une image avec `docker build -t nom .`
- L’importance du `.dockerignore`
- L’optimisation du cache par l’ordre des instructions

-----


## Chapitre 7 — Optimiser et durcir ses images

### Le minimum à savoir

#### Le multi-stage build

C’est LA technique d’optimisation la plus importante. L’idée : utiliser une première image pour **compiler/construire**, puis copier uniquement le résultat dans une deuxième image plus légère.

```dockerfile
# Étape 1 : construction (image lourde avec les outils de build)
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Étape 2 : production (image légère, juste le nécessaire)
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["python", "app.py"]
```

L’image finale ne contient **pas** les outils de build, pas le cache pip, pas les headers de compilation. Elle est beaucoup plus petite et a une surface d’attaque réduite.

#### L’utilisateur non-root

Par défaut, les processus dans un container tournent en **root**. C’est dangereux : si un attaquant exploite une faille dans l’application, il est root dans le container (UID 0). Sans user namespace remapping ni mode rootless, cet UID 0 correspond à celui de l’hôte. Les mécanismes d’isolation (namespaces, capabilities) limitent ce que ce root peut faire, mais en cas de faille d’isolation ou de mauvaise configuration, l’impact peut devenir critique.

```dockerfile
FROM python:3.12-slim
WORKDIR /app

# Créer un utilisateur non-root
RUN useradd --create-home --shell /bin/bash appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Basculer vers l'utilisateur non-root
USER appuser

# L'application écoute sur un port > 1024 (les ports < 1024 nécessitent root)
EXPOSE 8000
CMD ["python", "app.py"]
```

> **À retenir pour un entretien :** “En production, les containers ne doivent jamais tourner en root. On crée un utilisateur dédié dans le Dockerfile avec `USER`. C’est la mesure de sécurité la plus impactante et la plus simple à mettre en place.”

#### Scanner ses images

Les images Docker contiennent des packages système et des bibliothèques qui peuvent avoir des **vulnérabilités connues** (CVE). Un scanner analyse l’image et liste les CVE trouvées.

```bash
# Installer Trivy (le scanner open source le plus populaire)
# Sur Linux :
sudo apt-get install trivy
# Ou via Docker lui-même :
docker run --rm aquasec/trivy image python:3.12-slim

# Scanner une image
trivy image mon_app:latest
```

Le scan va lister les CVE par sévérité (CRITICAL, HIGH, MEDIUM, LOW). L’objectif n’est pas d’avoir 0 CVE (c’est souvent impossible — les images de base ont des CVE dans les bibliothèques système), mais de n’avoir aucune CVE **critique ou haute** exploitable.

> **Point important :** un scan est un **signal**, pas un verdict. Une CVE dans une bibliothèque que ton application n’utilise pas n’est pas un risque réel. Mais une CVE critique dans OpenSSL sur une image exposée à Internet est un problème urgent.

> **📋 CONTAINER — Épisode 4 (partie 2)**
> 
> Sami optimise le Dockerfile de MedFlow. Image de base `python:3.12` (1.2 Go, 147 CVE) → multi-stage build avec `python:3.12-slim` (180 Mo, 12 CVE en low/medium), utilisateur non-root, `.dockerignore` qui exclut `.git`, `.env`, et `__pycache__`. Le scan Trivy est ajouté au pipeline GitLab CI : le build échoue si une CVE critique est détectée.

### Très utile en pratique

#### Choisir la bonne image de base

|Image de base              |Taille |Surface d’attaque        |Compatibilité   |Usage recommandé            |
|---------------------------|-------|-------------------------|----------------|----------------------------|
|`python:3.12`              |~900 Mo|Large (Debian complète)  |Excellente      |Dev, CI, debug              |
|`python:3.12-slim`         |~150 Mo|Moyenne                  |Très bonne      |**Production (recommandé)** |
|`python:3.12-alpine`       |~50 Mo |Petite                   |Attention (musl)|Quand la taille est critique|
|`gcr.io/distroless/python3`|~20 Mo |Minimale (pas de shell !)|Limitée         |Production durcie           |


> **Conseil :** commence avec `slim`. C’est le meilleur compromis pour la plupart des cas. Alpine peut causer des problèmes de compatibilité avec certaines bibliothèques Python (car Alpine utilise `musl` au lieu de `glibc`). Distroless est le choix le plus sécurisé mais rend le debugging très difficile (pas de shell dans le container).

#### Regrouper les RUN et nettoyer

```dockerfile
# ❌ 3 couches inutilement séparées
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*

# ✅ 1 seule couche, nettoyée
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
```

Le `rm -rf /var/lib/apt/lists/*` supprime le cache apt — inutile dans l’image finale. Chaque `RUN` crée une couche, et chaque couche ajoute à la taille de l’image.

#### Le read-only filesystem

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run mon_app
```

Toute tentative d’écriture sur le filesystem (sauf `/tmp` et `/run`) échoue. C’est une protection forte contre les attaquants qui déposent des fichiers (webshells, outils) après une compromission.

### Bonus

#### Hadolint : le linter de Dockerfile

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

Hadolint analyse ton Dockerfile et signale les mauvaises pratiques (utiliser `latest`, ne pas fixer les versions des packages, ne pas nettoyer le cache apt, etc.).

#### Le Dockerfile de production type

```dockerfile
# --- Stage 1 : Build ---
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Stage 2 : Production ---
FROM python:3.12-slim
WORKDIR /app

# Créer un utilisateur non-root
RUN useradd --create-home --no-log-init --shell /bin/false appuser

# Copier les dépendances depuis le stage de build
COPY --from=builder /install /usr/local

# Copier le code
COPY --chown=appuser:appuser . .

# Basculer vers l'utilisateur non-root
USER appuser

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

### ✅ Tu sais maintenant…

- Le multi-stage build pour réduire la taille des images
- L’importance de l’utilisateur non-root (`USER` dans le Dockerfile)
- Scanner les images avec Trivy
- Choisir la bonne image de base (slim vs alpine vs distroless)
- Les bonnes pratiques : regrouper les RUN, nettoyer le cache, `.dockerignore`

### 💬 Questions d’entretien typiques

- **Pourquoi ne pas utiliser le tag `latest` en production ?** → Parce que `latest` change à chaque push. Le déploiement n’est plus déterministe — on ne sait pas quelle version tourne réellement. On utilise des tags de version spécifiques.
- **Qu’est-ce qu’un multi-stage build ?** → Une technique Dockerfile qui utilise une première image pour compiler/construire, puis copie uniquement le résultat dans une image finale légère. L’image de production ne contient pas les outils de build.
- **Pourquoi ne pas exécuter en root dans un container ?** → Si un attaquant exploite une faille, il est root dans le container. Avec un user non-root, l’impact est limité. C’est la mesure de sécurité la plus simple et la plus impactante.

-----


## Chapitre 8 — Docker Compose : orchestrer plusieurs containers

### Le minimum à savoir

#### Le problème

Au chapitre 5, on a lancé 3 containers avec 3 commandes `docker run` séparées. Chaque commande a une douzaine de flags (-d, -p, -v, -e, –name, –network). C’est ingérable dès que l’application a plus de 2 services. Et si tu dois partager la configuration avec un collègue, il doit retaper les mêmes commandes.

**Docker Compose** résout ça : tu décris toute ta stack dans **un seul fichier YAML**, et tu la lances avec **une seule commande**.

#### Le fichier `docker-compose.yml`

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

#### Les commandes Compose

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

#### Décortiquer le fichier

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

### Très utile en pratique

#### Un Compose complet pour MedFlow

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

#### Les fichiers `.env` pour les variables

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

#### Exécuter des commandes dans un service

```bash
# Ouvrir un shell dans le container web
docker compose exec web bash

# Lancer une migration Django
docker compose exec web python manage.py migrate

# Créer un superuser
docker compose exec web python manage.py createsuperuser
```

### Bonus

#### Les profils (pour les services optionnels)

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

#### Health checks dans Compose

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

### ❌ Erreur classique

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

### ✅ Tu sais maintenant…

- Décrire une stack multi-containers dans un fichier `docker-compose.yml`
- Les commandes : `up -d`, `down`, `logs`, `exec`, `build`, `ps`
- Les options clés : `build`, `image`, `ports`, `volumes`, `environment`, `depends_on`
- Utiliser un fichier `.env` pour les variables sensibles

-----


## Chapitre 9 — Registries et gestion des images

### Le minimum à savoir

#### Qu’est-ce qu’un registry ?

Un registry est un **entrepôt d’images Docker**. C’est là que les images sont stockées, versionnées et distribuées. Le registry le plus connu est **Docker Hub**, mais en entreprise, on utilise un **registry privé**.

#### Pourquoi un registry privé ?

- **Sécurité :** tu contrôles ce qui entre et sort — pas d’images communautaires non vérifiées
- **Confidentialité :** tes images d’application ne sont pas publiques
- **Performance :** pas de pull rate limit, le registry est sur ton réseau
- **Conformité :** certaines réglementations exigent que les artefacts logiciels soient hébergés en interne

#### Les options de registries privés

|Registry                               |Type                    |Particularité                                          |
|---------------------------------------|------------------------|-------------------------------------------------------|
|**Docker Hub** (plan payant)           |Cloud public            |Le plus connu, repos privés possibles                  |
|**Harbor**                             |Self-hosted, open source|Scan de vulnérabilités intégré (Trivy), signature, RBAC|
|**GitLab Container Registry**          |Intégré à GitLab        |Gratuit si tu utilises GitLab CI                       |
|**AWS ECR**                            |Cloud AWS               |Intégré à EKS, scan natif                              |
|**Azure ACR**                          |Cloud Azure             |Intégré à AKS                                          |
|**GCP Artifact Registry**              |Cloud GCP               |Intégré à GKE                                          |
|**GitHub Container Registry** (ghcr.io)|Cloud GitHub            |Intégré à GitHub Actions                               |

#### Pousser une image vers un registry

```bash
# 1. Se connecter au registry
docker login registry.example.com

# 2. Tagger l'image avec le nom complet du registry
docker tag mon_app:latest registry.example.com/mon_equipe/mon_app:1.0.0

# 3. Pousser
docker push registry.example.com/mon_equipe/mon_app:1.0.0
```

Le format du nom d’une image complète :

```
registry.example.com / mon_equipe / mon_app : 1.0.0
       ↑                   ↑          ↑        ↑
    registry          namespace     image     tag
```

#### La stratégie de tags

**Ne jamais utiliser `latest` en production.** Le tag `latest` change à chaque push — tu ne sais pas quelle version tourne.

Stratégies recommandées :

|Stratégie         |Exemple             |Usage               |
|------------------|--------------------|--------------------|
|Version sémantique|`mon_app:1.2.3`     |Releases officielles|
|SHA du commit Git |`mon_app:a3f2b1c`   |Chaque build CI     |
|Date              |`mon_app:2025-04-07`|Builds quotidiens   |


> **À retenir pour un entretien :** “En production, on utilise des tags de version spécifiques, jamais `latest`. Ça garantit que le déploiement est déterministe — on sait exactement quelle version tourne.”

### Très utile en pratique

#### La supply chain des images

C’est un sujet de sécurité critique : **d’où viennent tes images ?**

Les risques :

- **Typosquatting :** une image `ngimx` (au lieu de `nginx`) qui contient du code malveillant
- **Image compromise :** une image communautaire légitime dont l’auteur a été compromis ou est malveillant
- **Image obsolète :** une image avec des CVE connues non corrigées

Les protections :

- N’utiliser que des images **officielles** ou **vérifiées** (badge sur Docker Hub)
- Scanner toutes les images avec **Trivy/Grype** avant déploiement
- Utiliser un **registry privé** qui met en cache les images officielles
- **Signer** les images avec **Cosign** (projet Sigstore) et vérifier les signatures avant déploiement

#### Cosign : signer et vérifier les images

```bash
# Installer cosign
# (voir https://docs.sigstore.dev/cosign/installation/)

# Signer une image
cosign sign registry.example.com/mon_app:1.0.0

# Vérifier la signature
cosign verify registry.example.com/mon_app:1.0.0
```

En combinant signature + admission controller K8s (voir chapitre 22), tu peux empêcher le déploiement de toute image non signée.

### Bonus

#### Le SBOM (Software Bill of Materials)

Un SBOM est l’**inventaire complet** de tous les composants logiciels d’une image (packages système, bibliothèques, dépendances). C’est l’équivalent d’une liste d’ingrédients pour une image Docker.

```bash
# Générer un SBOM avec Syft
syft mon_app:latest

# Docker a un SBOM intégré
docker sbom mon_app:latest
```

Quand une CVE critique est annoncée (type Log4Shell), le SBOM te permet de savoir instantanément quels containers sont affectés.

### ✅ Tu sais maintenant…

- Ce qu’est un registry et pourquoi utiliser un registry privé
- Pousser une image vers un registry (`tag` + `push`)
- La stratégie de tags (jamais `latest` en production)
- Les risques de supply chain des images et les protections (scan, signature, SBOM)

-----


## Chapitre 10 — Capstone Partie II : containeriser une application complète

Cet exercice intègre tout ce que tu as appris dans les chapitres 6 à 9.

### L’exercice

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

### ✅ Tu sais maintenant…

- Containeriser une application multi-composants de A à Z
- Appliquer les bonnes pratiques : multi-stage, non-root, scan, secrets externalisés
- Documenter pour que n’importe qui puisse lancer la stack

-----
