---
title: Chapitre 5 — Réseau, volumes et persistance
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### Le réseau Docker

Par défaut, Docker crée un réseau virtuel isolé. Les containers sur le même réseau peuvent communiquer entre eux par leur **nom** (DNS interne). Les containers sur des réseaux différents ne peuvent pas se voir.

```bash
# Créer un réseau
docker network create mon_reseau

# Lancer deux containers sur le même réseau
docker run -d --name web --network mon_reseau nginx
docker run -d --name db --network mon_reseau postgres:16 -e POSTGRES_PASSWORD=secret

# Depuis le container "web", on peut joindre "db" par son nom
docker exec web ping db    # ← "db" est résolu en adresse IP automatiquement
```


> **Pourquoi c’est important :** quand ton application Django doit se connecter à PostgreSQL, tu n’as pas besoin de connaître l’adresse IP du container PostgreSQL (elle change à chaque fois). Tu utilises simplement le **nom du container** comme hostname (`db` dans l’exemple ci-dessus). Docker résout le nom en adresse IP automatiquement.

### L’exposition de ports (rappel et approfondissement)

```bash
docker run -d -p 8080:80 nginx
#              ↑      ↑
#           hôte    container
```


Sans `-p`, le container est isolé du réseau de la machine hôte. Le port est accessible à l’intérieur du réseau Docker, mais pas depuis ton navigateur ou depuis l’extérieur.

Avec `-p 8080:80`, le port 80 du container est accessible via le port 8080 de la machine hôte.

> **Sécurité :** par défaut, `-p 8080:80` expose le port sur **toutes les interfaces réseau** de la machine (0.0.0.0). Pour limiter à localhost uniquement : `-p 127.0.0.1:8080:80`.

### Les volumes : la persistance des données

Les containers sont **éphémères** : quand un container est supprimé, tout ce qu’il contenait disparaît. C’est un problème pour les bases de données, les fichiers uploadés, les logs.

La solution : les **volumes**. Un volume est un espace de stockage qui existe **en dehors du container** et qui survit à sa destruction.

```bash
# Créer un volume nommé
docker volume create mes_donnees

# Lancer un container avec le volume monté
docker run -d --name ma_db \
  -v mes_donnees:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:16
```


`-v mes_donnees:/var/lib/postgresql/data` signifie : “monte le volume `mes_donnees` dans le dossier `/var/lib/postgresql/data` du container”. PostgreSQL stocke ses données dans ce dossier — elles sont maintenant persistées dans le volume.

Si tu supprimes le container et en crées un nouveau avec le même volume, les données sont toujours là :

```bash
docker rm -f ma_db    # Supprime le container
docker run -d --name ma_db_v2 \
  -v mes_donnees:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:16
# ← Les données de l'ancienne base sont toujours là !
```


### Les 3 types de montages

|Type            |Syntaxe                            |Usage                                                                        |
|----------------|-----------------------------------|-----------------------------------------------------------------------------|
|**Volume nommé**|`-v mon_volume:/chemin`            |Données de production (bases de données, fichiers uploadés) — géré par Docker|
|**Bind mount**  |`-v /chemin/hôte:/chemin/container`|Développement (monter ton code source dans le container)                     |
|**tmpfs**       |`--tmpfs /chemin`                  |Données temporaires en mémoire uniquement                                    |

```bash
# Volume nommé (production)
docker run -v pgdata:/var/lib/postgresql/data postgres:16

# Bind mount (développement — ton code est synchronisé en temps réel)
docker run -v $(pwd)/mon_app:/app python:3.12

# tmpfs (données sensibles temporaires — jamais écrites sur disque)
docker run --tmpfs /tmp myapp
```


> **À retenir :** utilise des **volumes nommés** pour les données de production et des **bind mounts** pour le développement (voir ton code modifié en direct dans le container).

### Les variables d’environnement

Les variables d’environnement sont le mécanisme standard pour configurer un container sans modifier l’image :

```bash
docker run -d \
  -e POSTGRES_USER=medflow \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=patients \
  postgres:16
```


Chaque image a ses propres variables d’environnement documentées sur Docker Hub. PostgreSQL utilise `POSTGRES_PASSWORD`, MySQL utilise `MYSQL_ROOT_PASSWORD`, etc.

> **Attention sécurité :** passer des mots de passe en clair avec `-e` les rend visibles dans `docker inspect` et dans l’historique des commandes. En production, on utilise des secrets (voir chapitres 8 et 25). Pour le développement et l’apprentissage, `-e` suffit.

> **📋 CONTAINER — Épisode 3**
> 
> Sami crée un réseau Docker dédié pour MedFlow, lance PostgreSQL avec un volume persistant, Redis sans volume (le cache est éphémère par nature), et connecte l’application Django aux deux services par leur nom DNS interne. Premier stack fonctionnel en local — Django parle à PostgreSQL via `db:5432` et à Redis via `redis:6379`, sans adresses IP en dur.

## Très utile en pratique

### Les drivers réseau Docker

|Driver   |Description                                                      |Usage                                        |
|---------|-----------------------------------------------------------------|---------------------------------------------|
|`bridge` |Réseau isolé par défaut                                          |Le plus courant — containers sur un même hôte|
|`host`   |Pas d’isolation réseau (le container utilise le réseau de l’hôte)|Performance maximale, mais pas d’isolation   |
|`none`   |Pas de réseau                                                    |Containers qui n’ont pas besoin de réseau    |
|`overlay`|Réseau multi-hôtes                                               |Docker Swarm / environnements multi-serveurs |

```bash
# Le réseau bridge par défaut
docker run -d nginx    # ← Utilise le bridge par défaut

# Un réseau bridge nommé (recommandé)
docker network create mon_app
docker run -d --network mon_app --name web nginx
docker run -d --network mon_app --name api myapp
# web et api peuvent se joindre par nom
```


> **Bonne pratique :** crée toujours un réseau nommé pour tes applications. Le réseau bridge par défaut ne supporte pas la résolution DNS par nom de container.

### Gérer les volumes

```bash
# Lister les volumes
docker volume ls

# Inspecter un volume (voir où il est stocké sur l'hôte)
docker volume inspect mes_donnees

# Supprimer un volume (⚠️ les données sont perdues !)
docker volume rm mes_donnees

# Supprimer les volumes non utilisés
docker volume prune
```


### Cas pratique complet : stack minimale

```bash
# Créer le réseau
docker network create medflow

# Lancer PostgreSQL avec persistance
docker run -d --name db \
  --network medflow \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=medflow \
  postgres:16

# Lancer Redis (cache — pas besoin de volume)
docker run -d --name redis \
  --network medflow \
  redis:7

# Lancer l'application (en bind mount pour le dev)
docker run -d --name web \
  --network medflow \
  -p 8000:8000 \
  -v $(pwd):/app \
  -e DATABASE_URL=postgresql://postgres:secret@db/medflow \
  -e REDIS_URL=redis://redis:6379 \
  python:3.12 python /app/manage.py runserver 0.0.0.0:8000
```


C’est fonctionnel, mais gérer 3 commandes `docker run` manuellement est ingérable dès que la stack grossit. C’est exactement le problème que Docker Compose résout (chapitre 8).

## Bonus

### Inspecter le réseau

```bash
# Voir les containers connectés à un réseau
docker network inspect medflow

# Depuis l'intérieur d'un container, voir la config réseau
docker exec web cat /etc/hosts
docker exec web ip addr
```


### Le read-only filesystem

Tu peux lancer un container avec un filesystem en **lecture seule** pour réduire la surface d’attaque :

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run nginx
```


L’application ne peut rien écrire sauf dans `/tmp` et `/run` (montés en tmpfs, en mémoire). Un attaquant qui compromet l’application ne peut pas déposer de fichier sur le disque.

## ❌ Erreur classique

```bash
# Oublier le volume sur la base de données
docker run -d postgres:16      # ❌ Les données disparaîtront à la suppression

# Utiliser le réseau bridge par défaut et s'attendre à la résolution DNS
docker run -d --name web nginx
docker run -d --name db postgres:16
docker exec web ping db        # ❌ Ne fonctionne PAS sur le bridge par défaut
# → Crée un réseau nommé !

# Exposer un port sur toutes les interfaces
docker run -d -p 5432:5432 postgres:16    # ❌ PostgreSQL accessible depuis Internet !
docker run -d -p 127.0.0.1:5432:5432 postgres:16   # ✅ Uniquement en local
```


## 🧩 Mini-projet (chapitres 3-5)

Crée une stack “blog” minimale :

1. Un container **PostgreSQL** avec un volume persistant et un mot de passe configuré
1. Un container **Nginx** qui sert une page HTML (montée en bind mount depuis ton hôte)
1. Les deux containers sur un **réseau nommé**
1. Nginx accessible sur le port 8080 de ton hôte
1. Vérifie que les données PostgreSQL survivent à un `docker rm` + recréation du container

## ✅ Tu sais maintenant…

- Créer un réseau Docker et y connecter des containers
- Exposer un port avec `-p hôte:container`
- Persister des données avec les volumes (et la différence volume nommé vs bind mount)
- Configurer un container avec les variables d’environnement (`-e`)
- Pourquoi ne pas utiliser le réseau bridge par défaut

-----
