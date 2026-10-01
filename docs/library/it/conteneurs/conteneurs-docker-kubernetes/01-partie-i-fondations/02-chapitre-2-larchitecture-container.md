---
title: Chapitre 2 — L’architecture container
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie I — Fondations
  - index.md
---

comment ça marche sous le capot

## Le minimum à savoir

### Pourquoi comprendre “le dessous”

Tu n’as pas besoin de maîtriser les mécanismes internes du kernel Linux pour utiliser Docker. Mais comprendre les grandes lignes te permet de :

- répondre aux questions techniques en entretien (“comment fonctionne l’isolation d’un container ?”)
- comprendre pourquoi certaines configurations sont dangereuses
- diagnostiquer les problèmes quand ça ne fonctionne pas

### L’isolation par les namespaces

Les **namespaces** sont le mécanisme du kernel Linux qui donne à chaque container l’illusion d’avoir son propre système. Chaque namespace isole un aspect :

|Namespace|Ce qu’il isole                  |Effet concret                                                                            |
|---------|--------------------------------|-----------------------------------------------------------------------------------------|
|**PID**  |Les processus                   |Le container ne voit que ses propres processus (pas ceux de l’hôte)                      |
|**NET**  |Le réseau                       |Le container a sa propre interface réseau, sa propre IP                                  |
|**MNT**  |Le filesystem                   |Le container a son propre système de fichiers                                            |
|**UTS**  |Le hostname                     |Le container a son propre nom de machine                                                 |
|**IPC**  |La communication inter-processus|Les processus du container ne peuvent pas communiquer avec ceux d’un autre               |
|**USER** |Les utilisateurs                |L’utilisateur “root” dans le container peut être un utilisateur non privilégié sur l’hôte|

Concrètement, quand tu lances un container et que tu fais `ps aux` dedans, tu ne vois que les processus du container. L’hôte, lui, voit tous les processus de tous les containers. C’est une illusion, pas une séparation matérielle — et c’est la raison pour laquelle l’isolation est plus faible qu’une VM.

> **À retenir pour un entretien :** “L’isolation des containers repose sur les namespaces Linux, qui donnent à chaque container l’illusion d’avoir son propre système. Mais contrairement à une VM, il n’y a pas de séparation matérielle — c’est une isolation logicielle au niveau du kernel.”

### Le contrôle des ressources par les cgroups

Les **cgroups** (control groups) limitent les ressources qu’un container peut consommer :

- **CPU** : “ce container ne peut pas utiliser plus de 50% du CPU”
- **Mémoire** : “ce container ne peut pas utiliser plus de 512 Mo de RAM”
- **I/O disque** : “ce container ne peut pas saturer le disque”

Sans cgroups, un container pourrait monopoliser toutes les ressources de la machine et faire tomber les autres containers. Les cgroups sont le mécanisme de “fair play” entre containers.

> **Conséquence pratique :** quand un container dépasse sa limite mémoire, le kernel le tue brutalement (OOMKilled — Out Of Memory Killed). C’est un comportement normal, pas un bug — c’est la protection qui fonctionne. On verra comment diagnostiquer ça au chapitre 19.

### Le filesystem par couches (layers)

Les images Docker sont construites en **couches** superposées (layers). Chaque instruction dans le Dockerfile (on verra ça au chapitre 6) crée une couche :

```
┌─────────────────────────────────┐
│ Couche 4 : COPY app.py          │  ← Ton code (petite couche)
│─────────────────────────────────│
│ Couche 3 : RUN pip install      │  ← Tes dépendances
│─────────────────────────────────│
│ Couche 2 : RUN apt-get update   │  ← Les mises à jour système
│─────────────────────────────────│
│ Couche 1 : FROM python:3.12     │  ← L'image de base (la plus grosse)
└─────────────────────────────────┘
```


Chaque couche est **en lecture seule**. Quand le container tourne, une couche supplémentaire **en écriture** est ajoutée au-dessus. Quand le container est détruit, cette couche d’écriture disparaît — c’est pourquoi les données non persistées sont perdues.

**L’avantage :** si deux images utilisent la même couche de base (`python:3.12`), cette couche n’est stockée qu’une seule fois sur le disque. C’est un gain de place considérable.

> **À retenir :** les couches sont en lecture seule et partagées entre images. Le container ajoute une couche d’écriture temporaire qui disparaît quand le container est supprimé. C’est pour ça qu’on utilise des **volumes** pour les données qu’on veut garder (chapitre 5).

### Le kernel partagé : la conséquence en sécurité

C’est **le** point à comprendre en profondeur :

```
Container A    Container B    Container C
    │              │              │
    └──────────────┼──────────────┘
                   │
           Kernel Linux (partagé)
                   │
             Matériel (CPU, RAM)
```


Tous les containers utilisent le **même kernel** que la machine hôte. Conséquences :

1. **Performance :** c’est pour ça que les containers sont rapides — pas de virtualisation du matériel.
1. **Compatibilité :** tu ne peux pas faire tourner un container Windows sur un hôte Linux (sauf via une VM intermédiaire, comme Docker Desktop sur Mac/Windows).
1. **Sécurité :** une vulnérabilité dans le kernel affecte **tous les containers** de la machine. C’est la raison principale pour laquelle l’isolation est plus faible qu’une VM.

### Les composants de l’écosystème Docker

Quand tu utilises Docker, plusieurs composants collaborent :

```
  Toi
   │
   ▼
Docker CLI  ────►  Docker Daemon  ────►  containerd  ────►  runc  ────►  Container
(docker run)       (dockerd)              (gestion)         (exécution)
```


- **Docker CLI** : la commande `docker` que tu tapes dans le terminal
- **Docker Daemon** (`dockerd`) : le service qui tourne en arrière-plan et gère tout
- **containerd** : le runtime de haut niveau qui gère le cycle de vie des containers
- **runc** : le runtime de bas niveau qui crée effectivement le container (namespaces, cgroups)

Tu n’as pas besoin de connaître ces détails pour utiliser Docker au quotidien. Mais savoir que le Docker daemon tourne en **root** et que le socket Docker (`/var/run/docker.sock`) donne un accès total au daemon est crucial pour la sécurité (on y reviendra au chapitre 21).

## Très utile en pratique

### OverlayFS : le filesystem en couches concrètement

Le filesystem utilisé par Docker (sur la plupart des distributions Linux) s’appelle **OverlayFS**. Il superpose les couches de l’image et rend le tout transparent pour l’application dans le container.

```bash
# Voir les couches d'une image
docker inspect --format='{{.RootFS.Layers}}' python:3.12-slim
```


Chaque couche est identifiée par un hash SHA256. Si tu modifies une seule ligne de ton Dockerfile, seules les couches à partir de cette ligne sont reconstruites — c’est le **cache de build**, et c’est un gain de temps considérable.

### Les capabilities Linux

En plus des namespaces et des cgroups, Linux a un système de **capabilities** — des permissions granulaires qui décomposent les pouvoirs du root. Au lieu de donner “tous les droits” (root classique), on peut donner des droits spécifiques :

|Capability        |Droit accordé                                |
|------------------|---------------------------------------------|
|`NET_BIND_SERVICE`|Écouter sur les ports < 1024                 |
|`NET_RAW`         |Utiliser des sockets raw (ping, tcpdump)     |
|`SYS_ADMIN`       |Presque tout — la “super capability” à éviter|
|`SYS_PTRACE`      |Tracer les processus (débogage)              |
|`DAC_OVERRIDE`    |Ignorer les permissions de fichiers          |

Docker donne un ensemble de capabilities par défaut à chaque container. En sécurité, le principe est de **supprimer toutes les capabilities** (`--cap-drop ALL`) puis d’ajouter uniquement celles dont l’application a besoin (`--cap-add NET_BIND_SERVICE`). On verra ça en détail au chapitre 23.

## Bonus

### Alternatives à Docker : Podman

**Podman** est une alternative à Docker qui fonctionne **sans daemon** (pas de processus root en arrière-plan) et peut exécuter des containers **sans privilèges root** (rootless). Les commandes sont les mêmes (`podman run` au lieu de `docker run`). C’est un choix de plus en plus courant dans les environnements où la sécurité est une priorité (RHEL, Fedora).

### Les runtimes alternatifs

- **gVisor** (Google) : un kernel “sandbox” qui intercepte les appels système du container — isolation plus forte que les namespaces classiques, avec un coût en performance
- **Kata Containers** : des containers qui tournent dans des micro-VMs — l’isolation d’une VM avec l’expérience utilisateur d’un container
- **Firecracker** (AWS) : des micro-VMs ultra-légères (démarrage en 125ms) utilisées par AWS Lambda et Fargate

Ces alternatives existent pour les cas où l’isolation standard des containers n’est pas suffisante (environnements multi-tenant, clouds publics).

## ❌ Erreur classique

```
# Croire que "isolation par namespaces" = "aussi sécurisé qu'une VM"
→ Les namespaces sont une isolation logicielle, pas matérielle.
  Une vulnérabilité kernel peut permettre un "container escape".

# Ignorer les cgroups (ne pas mettre de limites de ressources)
→ Un container sans limite mémoire peut consommer toute la RAM de l'hôte
  et faire tomber les autres containers.

# Confondre "root dans le container" et "root sur l'hôte"
→ Par défaut, root dans le container correspond à l'UID 0 sur l'hôte (si le
  remapping n'est pas activé). L'isolation par namespaces et capabilities le
  limite, mais en cas de faille d'isolation ou de mauvaise configuration,
  l'impact peut devenir critique.
```


## ✅ Tu sais maintenant…

- Les namespaces isolent les processus, le réseau et le filesystem de chaque container
- Les cgroups limitent les ressources (CPU, mémoire)
- Le filesystem fonctionne par couches en lecture seule + une couche d’écriture temporaire
- Le kernel est partagé entre tous les containers et la machine hôte
- Pourquoi cette architecture a des implications en sécurité

-----
