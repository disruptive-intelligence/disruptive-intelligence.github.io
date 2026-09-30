---
title: Chapitre 7 — Optimiser et durcir ses images
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie II — Construire ET composer
  - index.md
---

## Le minimum à savoir

### Le multi-stage build

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

### L’utilisateur non-root

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

### Scanner ses images

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

## Très utile en pratique

### Choisir la bonne image de base

|Image de base              |Taille |Surface d’attaque        |Compatibilité   |Usage recommandé            |
|---------------------------|-------|-------------------------|----------------|----------------------------|
|`python:3.12`              |~900 Mo|Large (Debian complète)  |Excellente      |Dev, CI, debug              |
|`python:3.12-slim`         |~150 Mo|Moyenne                  |Très bonne      |**Production (recommandé)** |
|`python:3.12-alpine`       |~50 Mo |Petite                   |Attention (musl)|Quand la taille est critique|
|`gcr.io/distroless/python3`|~20 Mo |Minimale (pas de shell !)|Limitée         |Production durcie           |


> **Conseil :** commence avec `slim`. C’est le meilleur compromis pour la plupart des cas. Alpine peut causer des problèmes de compatibilité avec certaines bibliothèques Python (car Alpine utilise `musl` au lieu de `glibc`). Distroless est le choix le plus sécurisé mais rend le debugging très difficile (pas de shell dans le container).

### Regrouper les RUN et nettoyer

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

### Le read-only filesystem

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run mon_app
```


Toute tentative d’écriture sur le filesystem (sauf `/tmp` et `/run`) échoue. C’est une protection forte contre les attaquants qui déposent des fichiers (webshells, outils) après une compromission.

## Bonus

### Hadolint : le linter de Dockerfile

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```


Hadolint analyse ton Dockerfile et signale les mauvaises pratiques (utiliser `latest`, ne pas fixer les versions des packages, ne pas nettoyer le cache apt, etc.).

### Le Dockerfile de production type

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


## ✅ Tu sais maintenant…

- Le multi-stage build pour réduire la taille des images
- L’importance de l’utilisateur non-root (`USER` dans le Dockerfile)
- Scanner les images avec Trivy
- Choisir la bonne image de base (slim vs alpine vs distroless)
- Les bonnes pratiques : regrouper les RUN, nettoyer le cache, `.dockerignore`

## 💬 Questions d’entretien typiques

- **Pourquoi ne pas utiliser le tag `latest` en production ?** → Parce que `latest` change à chaque push. Le déploiement n’est plus déterministe — on ne sait pas quelle version tourne réellement. On utilise des tags de version spécifiques.
- **Qu’est-ce qu’un multi-stage build ?** → Une technique Dockerfile qui utilise une première image pour compiler/construire, puis copie uniquement le résultat dans une image finale légère. L’image de production ne contient pas les outils de build.
- **Pourquoi ne pas exécuter en root dans un container ?** → Si un attaquant exploite une faille, il est root dans le container. Avec un user non-root, l’impact est limité. C’est la mesure de sécurité la plus simple et la plus impactante.

-----
