---
title: 'Chapitre 4 — Images Docker : comprendre, chercher, utiliser'
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### Image vs container

L’**image** est le plan de construction. Le **container** est l’instance en cours d’exécution.

```
Image (template)          Container (instance)
┌──────────────┐          ┌──────────────┐
│ Python 3.12  │  ──►     │ Python 3.12  │  ← en cours d'exécution
│ + Flask      │  ──►     │ + Flask      │  ← avec sa couche d'écriture
│ + mon app    │  ──►     │ + mon app    │  ← processus actifs
└──────────────┘          └──────────────┘
   (lecture seule)          (vivant, éphémère)
```


Une image peut générer **plusieurs containers** identiques, comme un moule peut produire plusieurs gâteaux.

### Docker Hub : le “GitHub des images”

[Docker Hub](https://hub.docker.com) est le registry public par défaut. Quand tu fais `docker run nginx`, Docker télécharge l’image `nginx` depuis Docker Hub.

Il existe deux types d’images sur Docker Hub :

- **Images officielles** : maintenues par Docker et/ou les éditeurs (nginx, postgres, python, ubuntu…). Elles ont un badge “Official Image” et sont régulièrement mises à jour et scannées. C’est ce qu’il faut utiliser.
- **Images communautaires** : publiées par n’importe qui (`utilisateur/nom_image`). **Attention** : n’importe qui peut publier une image sur Docker Hub. Une image communautaire peut contenir du code malveillant, des CVE non corrigées, ou des backdoors. En environnement professionnel, on n’utilise que des images officielles ou des images d’un registry privé.

### Les tags : choisir la version

Chaque image a des **tags** qui identifient une version :

```bash
docker run python:3.12        # Python 3.12 (version spécifique)
docker run python:3.12-slim   # Version allégée (moins de packages système)
docker run python:3.12-alpine # Version ultra-légère (basée sur Alpine Linux)
docker run python:latest      # La dernière version (⚠️ change au fil du temps !)
docker run python              # Équivalent de python:latest
```


> **Règle importante :** ne jamais utiliser `latest` en production. Le tag `latest` change quand une nouvelle version est publiée. Ton container pourrait se comporter différemment d’un jour à l’autre. Utilise toujours un tag de version spécifique (`python:3.12`, `postgres:16`, `nginx:1.25`).

### Les variantes d’images

|Variante            |Taille typique|Contenu                                     |Usage                                             |
|--------------------|--------------|--------------------------------------------|--------------------------------------------------|
|`python:3.12`       |~900 Mo       |OS Debian complet + Python + outils de build|Développement, CI                                 |
|`python:3.12-slim`  |~150 Mo       |Debian minimal + Python                     |Production (bon compromis)                        |
|`python:3.12-alpine`|~50 Mo        |Alpine Linux + Python                       |Quand la taille compte (attention : compatibilité)|
|**distroless**      |~20 Mo        |Juste le runtime, pas de shell              |Production sécurisée                              |


> **Conseil pour débuter :** commence avec les images `slim`. Elles offrent un bon compromis entre taille raisonnable et compatibilité. Les images `alpine` sont plus petites mais peuvent causer des problèmes de compatibilité (musl vs glibc). Les images distroless sont pour la production durcie — pas de shell, pas d’outils de debug, surface d’attaque minimale.

### Gérer les images localement

```bash
# Télécharger une image sans lancer de container
docker pull nginx:1.25

# Lister les images sur ta machine
docker images

# Supprimer une image
docker rmi nginx:1.25

# Voir la taille de toutes les images
docker images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}"
```


### Les couches d’une image

```bash
# Voir les couches et les instructions qui les ont créées
docker history python:3.12-slim
```


Chaque ligne correspond à une couche. Tu peux voir la taille de chaque couche et l’instruction Dockerfile qui l’a créée. C’est utile pour comprendre pourquoi une image est grosse.

## Très utile en pratique

### Inspecter une image avant de l’utiliser

```bash
# Voir les métadonnées complètes
docker inspect python:3.12-slim

# Voir le user par défaut, les ports exposés, les variables d'environnement
docker inspect --format='{{.Config.User}}' python:3.12-slim
docker inspect --format='{{.Config.ExposedPorts}}' nginx:1.25
```


C’est le réflexe d’audit : avant de lancer une image en production, inspecte-la. Quel utilisateur ? Quels ports ? Quelles variables d’environnement par défaut ?

### Chercher des images

```bash
# Chercher sur Docker Hub depuis le terminal
docker search postgres

# Filtrer les images officielles
docker search --filter is-official=true postgres
```


En pratique, la recherche sur le site web Docker Hub est plus pratique (tu vois la documentation, les tags disponibles, les instructions d’utilisation).

### Sauvegarder et charger des images (hors ligne)

```bash
# Exporter une image dans un fichier
docker save nginx:1.25 -o nginx.tar

# Importer une image depuis un fichier
docker load -i nginx.tar
```


Utile pour transférer des images vers des machines sans accès Internet.

## Bonus

### Comprendre le pull rate limit de Docker Hub

Docker Hub limite le nombre de téléchargements d’images :

- Utilisateur anonyme : 100 pulls par 6 heures
- Utilisateur authentifié (gratuit) : 200 pulls par 6 heures
- Abonnement payant : illimité

En CI/CD, ces limites sont vite atteintes. C’est une des raisons pour lesquelles les entreprises utilisent un **registry privé** qui met en cache les images officielles (voir chapitre 9).

### Les images multi-architectures

Une même image peut contenir des variantes pour différentes architectures CPU (amd64, arm64). Quand tu fais `docker pull nginx`, Docker télécharge automatiquement la variante correspondant à ton architecture. C’est transparent, mais c’est important si tu développes sur un Mac avec puce Apple (arm64) et que tu déploies sur un serveur x86_64 (amd64).

## ❌ Erreur classique

```bash
# Utiliser "latest" en production
docker run myapp:latest    # ❌ "latest" peut changer à tout moment
docker run myapp:1.5.2     # ✅ Version fixée et prévisible

# Utiliser une image communautaire non vérifiée en production
docker run random_user/mysteriousapp    # ❌ Qui a construit ça ? Qu'est-ce qu'il y a dedans ?
docker run library/nginx:1.25           # ✅ Image officielle

# Accumuler des images sans nettoyer
docker images              # ← 50 images, 30 Go de disque
docker image prune -a      # ← Supprime les images non utilisées
```


## ✅ Tu sais maintenant…

- La différence entre image (template) et container (instance)
- Docker Hub et les images officielles vs communautaires
- Les tags et pourquoi ne pas utiliser `latest`
- Les variantes d’images (full, slim, alpine, distroless)
- Gérer les images localement (pull, images, rmi, history, inspect)

-----
