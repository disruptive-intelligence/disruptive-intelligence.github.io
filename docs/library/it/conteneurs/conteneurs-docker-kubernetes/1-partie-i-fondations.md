---
title: PARTIE I — FONDATIONS
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 1
chapters: 7
---

-----


## Chapitre 1 — Pourquoi les containers : du serveur physique au container

### Le minimum à savoir

#### Le problème de départ

Imagine que tu développes une application web. Elle a besoin de Python 3.12, de PostgreSQL 15, de Redis, et de quelques bibliothèques spécifiques. Ça fonctionne sur ton ordinateur. Mais quand tu la déploies sur le serveur de production, rien ne marche : le serveur a Python 3.9, une version différente de PostgreSQL, et il manque des bibliothèques.

C’est le problème classique du **“ça marche sur ma machine”**. Les containers le résolvent.

#### L’évolution en 3 étapes

Pour comprendre les containers, il faut comprendre ce qui existait avant et pourquoi chaque étape a été inventée.

**Étape 1 — Le serveur physique (bare metal)**

Au début, chaque application tournait sur un serveur physique dédié. Un serveur = une application. Le problème : si l’application n’utilise que 10% du CPU, les 90% restants sont gaspillés. Et si tu as 20 applications, tu as besoin de 20 serveurs physiques — coûteux, lents à déployer, difficiles à maintenir.

**Étape 2 — La virtualisation (machines virtuelles)**

La virtualisation permet de faire tourner **plusieurs systèmes d’exploitation** sur un seul serveur physique. Chaque machine virtuelle (VM) a son propre OS complet, son propre kernel, ses propres ressources. Un hyperviseur (VMware, Hyper-V, KVM) gère le partage du matériel.

C’est un progrès énorme : un serveur physique peut héberger 10-20 VMs. Mais chaque VM embarque un OS complet (plusieurs Go), consomme de la RAM juste pour son kernel, et met 30 secondes à 2 minutes pour démarrer.

**Étape 3 — Les containers**

Les containers sont une forme d’isolation **sans OS complet**. Au lieu d’embarquer un kernel entier, le container **partage le kernel de la machine hôte** et n’embarque que l’application et ses dépendances.

Résultat :

- Une image container fait typiquement **50-200 Mo** au lieu de **5-20 Go** pour une VM
- Un container démarre en **quelques secondes** au lieu de minutes
- Tu peux faire tourner **des dizaines de containers** là où tu mettrais 5-10 VMs
- L’application se comporte **exactement de la même façon** partout (sur ton laptop, sur le serveur de test, en production)

#### Container vs VM : la comparaison visuelle

```
  MACHINE VIRTUELLE                    CONTAINER
┌───────────────────────┐       ┌───────────────────────┐
│  App A  │  App B      │       │  App A  │  App B      │
│─────────│─────────────│       │─────────│─────────────│
│  Libs A │  Libs B     │       │  Libs A │  Libs B     │
│─────────│─────────────│       │─────────│─────────────│
│  OS     │  OS         │       │    Container Engine   │
│ complet │ complet     │       │     (Docker)          │
│─────────│─────────────│       │───────────────────────│
│      Hyperviseur      │       │    OS hôte (1 seul)   │
│───────────────────────│       │───────────────────────│
│     Matériel (CPU,    │       │     Matériel (CPU,    │
│     RAM, disque)      │       │     RAM, disque)      │
└───────────────────────┘       └───────────────────────┘
```

La différence fondamentale : **la VM virtualise le matériel** (chaque VM croit avoir son propre ordinateur), **le container virtualise l’OS** (chaque container croit avoir son propre système, mais ils partagent le même kernel).

> **À retenir pour un entretien :** “Un container partage le kernel de la machine hôte et n’embarque que l’application et ses dépendances. C’est plus léger et plus rapide qu’une VM, mais l’isolation est moins forte car le kernel est partagé.”

#### Les 4 avantages concrets des containers

1. **Portabilité** : le container fonctionne partout de la même façon — sur ton laptop, sur le serveur de test, en production, chez un collègue. Plus jamais “ça marche sur ma machine”.
1. **Reproductibilité** : l’image container décrit exactement ce qui est installé. Pas de configuration manuelle, pas de “j’ai oublié d’installer cette bibliothèque”. Si l’image est la même, le résultat est le même.
1. **Isolation** : chaque container a son propre filesystem, ses propres processus, son propre réseau. L’application A dans son container ne peut pas interférer avec l’application B dans un autre container.
1. **Densité** : un serveur qui fait tourner 5 VMs peut faire tourner 50 containers. Les containers consomment beaucoup moins de ressources.

#### Ce que les containers ne sont PAS

C’est important de le dire dès le départ :

- **Les containers ne sont PAS des VMs.** L’isolation est moins forte (kernel partagé). Une vulnérabilité dans le kernel affecte tous les containers de la machine.
- **Les containers ne sont PAS magiquement sécurisés.** Un container mal configuré (exécuté en root, avec trop de permissions, avec des secrets dans l’image) est une vulnérabilité.
- **Les containers ne remplacent PAS la virtualisation dans tous les cas.** Pour une isolation forte (multi-tenant, environnements hostiles), une VM reste plus sûre.
- **Les containers ne simplifient PAS tout.** Ils ajoutent une couche de complexité (réseau, stockage, orchestration). Le bénéfice vient quand cette complexité est maîtrisée.

> **📋 CONTAINER — Épisode 1**
> 
> Sami rejoint l’équipe MedFlow. L’application tourne sur 3 VMs : une pour Django (le serveur web), une pour PostgreSQL (la base de données), une pour Redis + Celery (le cache et les tâches en arrière-plan). Chaque VM est configurée manuellement par un administrateur système. Le dernier déploiement a cassé la production : la version de Python sur la VM de staging (3.11) n’était pas la même qu’en production (3.9). Le CTO demande à Sami d’accompagner la migration vers des containers. Objectif : “que l’application se comporte exactement pareil partout.”

### Très utile en pratique

#### Les cas d’usage concrets

**Développement local reproductible :** au lieu d’installer PostgreSQL, Redis, Elasticsearch sur ton laptop (et de gérer les versions, les conflits, le nettoyage), tu lances des containers. Un `docker compose up` et tout ton environnement de développement est prêt. Un `docker compose down` et tout disparaît proprement.

**CI/CD (intégration et déploiement continus) :** les pipelines de test et de déploiement utilisent des containers pour garantir un environnement identique à chaque exécution. Les tests passent dans un container → on construit l’image de production → on la déploie.

**Microservices :** au lieu d’une grosse application monolithique, on découpe en services indépendants, chacun dans son container. Chaque service peut être développé, déployé et mis à l’échelle indépendamment.

**Labs de sécurité et pentest :** les containers sont parfaits pour lancer rapidement des environnements d’entraînement (DVWA, Juice Shop, Metasploitable) sans polluer ta machine.

#### Container vs VM : le tableau comparatif

|Critère    |Machine Virtuelle                       |Container                 |
|-----------|----------------------------------------|--------------------------|
|Isolation  |Forte (kernel séparé)                   |Moyenne (kernel partagé)  |
|Taille     |5-20 Go                                 |50-500 Mo                 |
|Démarrage  |30s - 2 min                             |1-5 secondes              |
|Densité    |5-20 par serveur                        |50-200 par serveur        |
|OS embarqué|OS complet                              |Juste les libs nécessaires|
|Portabilité|Moyenne (format VMware, Hyper-V…)       |Excellente (standard OCI) |
|Performance|Légère perte (virtualisation matérielle)|Quasi native              |
|Sécurité   |Plus forte par défaut                   |Nécessite du hardening    |

### Bonus

#### Un peu d’histoire

Les containers ne sont pas une invention récente. Les premières formes d’isolation de processus datent de `chroot` (1979) sous Unix. Puis sont venus les FreeBSD Jails (2000), Solaris Zones (2004), et LXC (Linux Containers, 2008). **Docker** (2013) a démocratisé le concept en le rendant simple d’utilisation avec un format d’image standardisé et un écosystème d’outils. Docker n’a pas inventé les containers — il les a rendus accessibles.

Aujourd’hui, le standard est **OCI** (Open Container Initiative) — un format ouvert pour les images et les runtimes de containers, indépendant de Docker. Kubernetes utilise `containerd` (un runtime OCI) plutôt que Docker directement.

#### Le standard OCI en bref

L’OCI définit deux choses : un format d’image (comment une image est construite et distribuée) et un runtime (comment un container est exécuté). Docker, Podman, containerd — tous respectent le standard OCI. Une image construite avec Docker fonctionne avec Podman et vice versa.

### ❌ Erreur classique

```
# Croire que container = VM légère
→ Non. Le modèle d'isolation est fondamentalement différent (kernel partagé vs séparé).

# Croire que les containers sont sécurisés par défaut
→ Non. Un container en root avec le Docker socket monté est MOINS sécurisé qu'une VM.

# Vouloir mettre "tout en containers" sans réflexion
→ Une base de données de production avec de fortes contraintes de performance et de
  persistance n'est pas toujours le meilleur candidat pour la containerisation.
```

### ✅ Tu sais maintenant…

- La différence entre serveur physique, VM et container
- Pourquoi les containers existent (portabilité, reproductibilité, isolation, densité)
- Que les containers partagent le kernel de la machine hôte (conséquence en sécurité)
- Ce que les containers ne sont PAS (pas des VMs, pas magiquement sécurisés)

### 💬 Questions d’entretien typiques

- **Quelle est la différence entre un container et une machine virtuelle ?** → Le container partage le kernel de l’hôte et isole au niveau de l’OS (namespaces), la VM virtualise le matériel avec un kernel séparé. Le container est plus léger et rapide, la VM offre une isolation plus forte.
- **Quels sont les avantages des containers ?** → Portabilité, reproductibilité, isolation des dépendances, densité (plus de containers que de VMs par serveur), démarrage rapide.
- **Les containers sont-ils sécurisés ?** → Pas par défaut. L’isolation repose sur des mécanismes logiciels (namespaces, cgroups), pas sur une séparation matérielle. Un container mal configuré (root, Docker socket monté) peut être moins sécurisé qu’une VM.

-----


## Chapitre 2 — L’architecture container : comment ça marche sous le capot

### Le minimum à savoir

#### Pourquoi comprendre “le dessous”

Tu n’as pas besoin de maîtriser les mécanismes internes du kernel Linux pour utiliser Docker. Mais comprendre les grandes lignes te permet de :

- répondre aux questions techniques en entretien (“comment fonctionne l’isolation d’un container ?”)
- comprendre pourquoi certaines configurations sont dangereuses
- diagnostiquer les problèmes quand ça ne fonctionne pas

#### L’isolation par les namespaces

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

#### Le contrôle des ressources par les cgroups

Les **cgroups** (control groups) limitent les ressources qu’un container peut consommer :

- **CPU** : “ce container ne peut pas utiliser plus de 50% du CPU”
- **Mémoire** : “ce container ne peut pas utiliser plus de 512 Mo de RAM”
- **I/O disque** : “ce container ne peut pas saturer le disque”

Sans cgroups, un container pourrait monopoliser toutes les ressources de la machine et faire tomber les autres containers. Les cgroups sont le mécanisme de “fair play” entre containers.

> **Conséquence pratique :** quand un container dépasse sa limite mémoire, le kernel le tue brutalement (OOMKilled — Out Of Memory Killed). C’est un comportement normal, pas un bug — c’est la protection qui fonctionne. On verra comment diagnostiquer ça au chapitre 19.

#### Le filesystem par couches (layers)

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

#### Le kernel partagé : la conséquence en sécurité

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

#### Les composants de l’écosystème Docker

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

### Très utile en pratique

#### OverlayFS : le filesystem en couches concrètement

Le filesystem utilisé par Docker (sur la plupart des distributions Linux) s’appelle **OverlayFS**. Il superpose les couches de l’image et rend le tout transparent pour l’application dans le container.

```bash
# Voir les couches d'une image
docker inspect --format='{{.RootFS.Layers}}' python:3.12-slim
```

Chaque couche est identifiée par un hash SHA256. Si tu modifies une seule ligne de ton Dockerfile, seules les couches à partir de cette ligne sont reconstruites — c’est le **cache de build**, et c’est un gain de temps considérable.

#### Les capabilities Linux

En plus des namespaces et des cgroups, Linux a un système de **capabilities** — des permissions granulaires qui décomposent les pouvoirs du root. Au lieu de donner “tous les droits” (root classique), on peut donner des droits spécifiques :

|Capability        |Droit accordé                                |
|------------------|---------------------------------------------|
|`NET_BIND_SERVICE`|Écouter sur les ports < 1024                 |
|`NET_RAW`         |Utiliser des sockets raw (ping, tcpdump)     |
|`SYS_ADMIN`       |Presque tout — la “super capability” à éviter|
|`SYS_PTRACE`      |Tracer les processus (débogage)              |
|`DAC_OVERRIDE`    |Ignorer les permissions de fichiers          |

Docker donne un ensemble de capabilities par défaut à chaque container. En sécurité, le principe est de **supprimer toutes les capabilities** (`--cap-drop ALL`) puis d’ajouter uniquement celles dont l’application a besoin (`--cap-add NET_BIND_SERVICE`). On verra ça en détail au chapitre 23.

### Bonus

#### Alternatives à Docker : Podman

**Podman** est une alternative à Docker qui fonctionne **sans daemon** (pas de processus root en arrière-plan) et peut exécuter des containers **sans privilèges root** (rootless). Les commandes sont les mêmes (`podman run` au lieu de `docker run`). C’est un choix de plus en plus courant dans les environnements où la sécurité est une priorité (RHEL, Fedora).

#### Les runtimes alternatifs

- **gVisor** (Google) : un kernel “sandbox” qui intercepte les appels système du container — isolation plus forte que les namespaces classiques, avec un coût en performance
- **Kata Containers** : des containers qui tournent dans des micro-VMs — l’isolation d’une VM avec l’expérience utilisateur d’un container
- **Firecracker** (AWS) : des micro-VMs ultra-légères (démarrage en 125ms) utilisées par AWS Lambda et Fargate

Ces alternatives existent pour les cas où l’isolation standard des containers n’est pas suffisante (environnements multi-tenant, clouds publics).

### ❌ Erreur classique

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

### ✅ Tu sais maintenant…

- Les namespaces isolent les processus, le réseau et le filesystem de chaque container
- Les cgroups limitent les ressources (CPU, mémoire)
- Le filesystem fonctionne par couches en lecture seule + une couche d’écriture temporaire
- Le kernel est partagé entre tous les containers et la machine hôte
- Pourquoi cette architecture a des implications en sécurité

-----


## Chapitre 3 — Installer Docker et premiers containers

### Le minimum à savoir

#### Installer Docker

**Linux (Ubuntu/Debian) :**

```bash
# 1. Supprimer les anciennes versions éventuelles
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2. Installer les prérequis
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

# 3. Ajouter le dépôt officiel Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Installer Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# 5. Ajouter ton utilisateur au groupe docker (pour ne pas taper sudo à chaque fois)
sudo usermod -aG docker $USER
# ⚠️ Déconnecte-toi et reconnecte-toi pour que ça prenne effet
```

> **Important :** utilise le dépôt **officiel Docker**, pas le paquet `docker.io` de ta distribution. Le paquet de la distribution est souvent une version ancienne.

> **Note sécurité :** ajouter ton utilisateur au groupe `docker` lui donne **l’équivalent des droits root** sur la machine (car le Docker daemon tourne en root). C’est pratique pour le développement, mais en production, l’accès au groupe docker doit être restreint. Si la sécurité est une priorité, sache que deux alternatives existent : **Docker en mode rootless** (le daemon tourne sans root — configuration spécifique) et **Podman** (un outil compatible Docker qui fonctionne nativement sans daemon root). Pour ce cours, on utilise Docker classique — c’est le plus répandu et le plus simple pour apprendre.

**Mac / Windows :** installe [Docker Desktop](https://www.docker.com/products/docker-desktop/) — c’est une application graphique qui installe tout. Sur Mac et Windows, Docker tourne en réalité dans une VM Linux cachée (car les containers Linux ont besoin d’un kernel Linux).

#### Vérifier l’installation

```bash
docker version
```

Tu devrais voir deux sections : **Client** et **Server**. Si le Server ne répond pas, le daemon Docker n’est pas démarré (`sudo systemctl start docker`).

```bash
docker info
```

Affiche des informations sur l’installation : nombre de containers, nombre d’images, version du kernel, driver de stockage, etc.

#### Ton premier container

```bash
docker run hello-world
```

Que se passe-t-il ? Décortiquons :

1. Docker cherche l’image `hello-world` en local → elle n’existe pas
1. Docker la **télécharge** (pull) depuis Docker Hub
1. Docker **crée** un container à partir de cette image
1. Docker **exécute** le programme dans le container (qui affiche un message)
1. Le programme se termine → le container **s’arrête**

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Félicitations, tu as lancé ton premier container !

#### Les commandes essentielles

```bash
# Lancer un container
docker run nginx                  # Lance un serveur web Nginx

# Lancer en arrière-plan (mode détaché)
docker run -d nginx               # Le -d "détache" : le container tourne en fond

# Voir les containers en cours d'exécution
docker ps

# Voir TOUS les containers (y compris les arrêtés)
docker ps -a

# Arrêter un container
docker stop <id_ou_nom>

# Supprimer un container arrêté
docker rm <id_ou_nom>

# Voir les logs d'un container
docker logs <id_ou_nom>

# Exécuter une commande dans un container en cours d'exécution
docker exec -it <id_ou_nom> bash
```

> **Le flag `-it` :** `-i` = interactif (garde l’entrée standard ouverte), `-t` = terminal (alloue un pseudo-terminal). Combinés, ils te permettent d’entrer “dans” le container et de taper des commandes comme si tu étais sur une machine.

#### Explorer un container interactif

```bash
docker run -it ubuntu bash
```

Tu es maintenant “dans” un container Ubuntu. Tu peux explorer :

```bash
ls /                  # Le filesystem du container (pas celui de ton hôte !)
cat /etc/os-release   # C'est bien Ubuntu
ps aux                # Très peu de processus (juste bash et ps)
whoami                # root (par défaut — on verra pourquoi c'est un problème)
exit                  # Quitter le container (il s'arrête)
```

> **Point crucial :** quand tu quittes le container, tout ce que tu as fait dedans **disparaît**. Si tu as créé un fichier, il est perdu. Le container est **éphémère** par nature. C’est un concept fondamental : les containers naissent, vivent et meurent — les données qui doivent survivre doivent être dans un **volume** (chapitre 5).

#### Exposer un port

Par défaut, un container est isolé du réseau de la machine hôte. Pour accéder à un service qui tourne dans un container depuis ton navigateur, tu dois **mapper un port** :

```bash
docker run -d -p 8080:80 nginx
```

`-p 8080:80` signifie : “le port 8080 de ma machine → le port 80 du container”. Tu peux maintenant ouvrir `http://localhost:8080` dans ton navigateur et voir la page par défaut de Nginx.

```
Port machine hôte     Port container
      8080       →        80
```

> **📋 CONTAINER — Épisode 2**
> 
> Sami installe Docker sur sa machine de travail et lance son premier container PostgreSQL :
> 
> ```bash
> docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=secret postgres:16
> ```
> 
> Il s’y connecte avec `psql` et crée une table. Puis il arrête le container (`docker stop`), le relance (`docker start`), et constate que ses données sont toujours là. Mais quand il **supprime** le container (`docker rm`) et en crée un nouveau, les données ont disparu. Il comprend la différence entre arrêter et supprimer, et pourquoi il faut un volume.

### Très utile en pratique

#### Nommer ses containers

```bash
docker run -d --name mon_nginx -p 8080:80 nginx
docker stop mon_nginx
docker start mon_nginx
docker logs mon_nginx
```

Beaucoup plus pratique que d’utiliser l’ID hexadécimal (`a3f2b1c9d8e7...`).

#### Le cycle de vie complet

```
docker create  →  docker start  →  docker stop  →  docker rm
   (créé)           (en cours)       (arrêté)       (supprimé)

  ou directement :
docker run  =  docker create + docker start
```

Un container arrêté **existe encore** (tu peux le voir avec `docker ps -a`, le redémarrer avec `docker start`). Il ne disparaît que quand tu le supprimes (`docker rm`).

#### Le nettoyage

Les containers arrêtés et les images téléchargées s’accumulent. Pour nettoyer :

```bash
# Supprimer tous les containers arrêtés
docker container prune

# Supprimer toutes les images non utilisées
docker image prune

# Tout nettoyer d'un coup (containers arrêtés + images non utilisées + réseaux + cache)
docker system prune
```

#### Le flag `--rm` : containers jetables

```bash
docker run --rm -it ubuntu bash
```

Le `--rm` supprime automatiquement le container quand il s’arrête. Parfait pour les utilisations ponctuelles (tester une commande, lancer un outil, explorer).

### Bonus

#### Voir les ressources consommées

```bash
docker stats
```

Affiche en temps réel le CPU, la mémoire, le réseau et le disque de chaque container — l’équivalent d’un `top` pour les containers.

#### Inspecter un container en détail

```bash
docker inspect mon_nginx
```

Renvoie un JSON détaillé avec toute la configuration du container : réseau (adresse IP), volumes, variables d’environnement, état, etc. Utile pour le troubleshooting.

### ❌ Erreur classique

```bash
# Oublier -d (le terminal est bloqué)
docker run nginx         # ← Ton terminal est pris. Ctrl+C pour arrêter.
docker run -d nginx      # ← Tourne en arrière-plan, ton terminal est libre.

# Oublier -p (le service n'est pas accessible)
docker run -d nginx      # ← Nginx tourne mais tu ne peux pas y accéder
docker run -d -p 8080:80 nginx   # ← Accessible sur localhost:8080

# Confondre stop et rm
docker stop mon_container   # ← Le container existe encore (arrêté)
docker rm mon_container     # ← Le container est supprimé définitivement

# Confondre le port hôte et le port container
docker run -d -p 80:8080 nginx   # ← Inverse ! C'est hôte:container
docker run -d -p 8080:80 nginx   # ← Correct : port 8080 de l'hôte → port 80 du container
```

### Exercices

**Guidé :** Lance un container Nginx en arrière-plan, expose-le sur le port 8080, vérifie dans ton navigateur, regarde les logs, puis arrête-le et supprime-le.

**Autonome :** Lance un container `python:3.12` en mode interactif (`-it`), tape `python3` à l’intérieur, exécute `print("Hello from a container!")`, puis quitte. Observe que le container s’arrête quand tu quittes.

### ✅ Tu sais maintenant…

- Installer Docker et vérifier l’installation
- Lancer un container avec `docker run`
- Les flags essentiels : `-d` (détaché), `-it` (interactif), `-p` (port), `--name` (nom), `--rm` (jetable)
- Le cycle de vie : run → stop → rm (ou start pour redémarrer)
- Que les containers sont éphémères — les données disparaissent à la suppression
- Les commandes de base : `docker ps`, `docker logs`, `docker exec`, `docker stop`, `docker rm`

-----


## Chapitre 4 — Images Docker : comprendre, chercher, utiliser

### Le minimum à savoir

#### Image vs container

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

#### Docker Hub : le “GitHub des images”

[Docker Hub](https://hub.docker.com) est le registry public par défaut. Quand tu fais `docker run nginx`, Docker télécharge l’image `nginx` depuis Docker Hub.

Il existe deux types d’images sur Docker Hub :

- **Images officielles** : maintenues par Docker et/ou les éditeurs (nginx, postgres, python, ubuntu…). Elles ont un badge “Official Image” et sont régulièrement mises à jour et scannées. C’est ce qu’il faut utiliser.
- **Images communautaires** : publiées par n’importe qui (`utilisateur/nom_image`). **Attention** : n’importe qui peut publier une image sur Docker Hub. Une image communautaire peut contenir du code malveillant, des CVE non corrigées, ou des backdoors. En environnement professionnel, on n’utilise que des images officielles ou des images d’un registry privé.

#### Les tags : choisir la version

Chaque image a des **tags** qui identifient une version :

```bash
docker run python:3.12        # Python 3.12 (version spécifique)
docker run python:3.12-slim   # Version allégée (moins de packages système)
docker run python:3.12-alpine # Version ultra-légère (basée sur Alpine Linux)
docker run python:latest      # La dernière version (⚠️ change au fil du temps !)
docker run python              # Équivalent de python:latest
```

> **Règle importante :** ne jamais utiliser `latest` en production. Le tag `latest` change quand une nouvelle version est publiée. Ton container pourrait se comporter différemment d’un jour à l’autre. Utilise toujours un tag de version spécifique (`python:3.12`, `postgres:16`, `nginx:1.25`).

#### Les variantes d’images

|Variante            |Taille typique|Contenu                                     |Usage                                             |
|--------------------|--------------|--------------------------------------------|--------------------------------------------------|
|`python:3.12`       |~900 Mo       |OS Debian complet + Python + outils de build|Développement, CI                                 |
|`python:3.12-slim`  |~150 Mo       |Debian minimal + Python                     |Production (bon compromis)                        |
|`python:3.12-alpine`|~50 Mo        |Alpine Linux + Python                       |Quand la taille compte (attention : compatibilité)|
|**distroless**      |~20 Mo        |Juste le runtime, pas de shell              |Production sécurisée                              |


> **Conseil pour débuter :** commence avec les images `slim`. Elles offrent un bon compromis entre taille raisonnable et compatibilité. Les images `alpine` sont plus petites mais peuvent causer des problèmes de compatibilité (musl vs glibc). Les images distroless sont pour la production durcie — pas de shell, pas d’outils de debug, surface d’attaque minimale.

#### Gérer les images localement

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

#### Les couches d’une image

```bash
# Voir les couches et les instructions qui les ont créées
docker history python:3.12-slim
```

Chaque ligne correspond à une couche. Tu peux voir la taille de chaque couche et l’instruction Dockerfile qui l’a créée. C’est utile pour comprendre pourquoi une image est grosse.

### Très utile en pratique

#### Inspecter une image avant de l’utiliser

```bash
# Voir les métadonnées complètes
docker inspect python:3.12-slim

# Voir le user par défaut, les ports exposés, les variables d'environnement
docker inspect --format='{{.Config.User}}' python:3.12-slim
docker inspect --format='{{.Config.ExposedPorts}}' nginx:1.25
```

C’est le réflexe d’audit : avant de lancer une image en production, inspecte-la. Quel utilisateur ? Quels ports ? Quelles variables d’environnement par défaut ?

#### Chercher des images

```bash
# Chercher sur Docker Hub depuis le terminal
docker search postgres

# Filtrer les images officielles
docker search --filter is-official=true postgres
```

En pratique, la recherche sur le site web Docker Hub est plus pratique (tu vois la documentation, les tags disponibles, les instructions d’utilisation).

#### Sauvegarder et charger des images (hors ligne)

```bash
# Exporter une image dans un fichier
docker save nginx:1.25 -o nginx.tar

# Importer une image depuis un fichier
docker load -i nginx.tar
```

Utile pour transférer des images vers des machines sans accès Internet.

### Bonus

#### Comprendre le pull rate limit de Docker Hub

Docker Hub limite le nombre de téléchargements d’images :

- Utilisateur anonyme : 100 pulls par 6 heures
- Utilisateur authentifié (gratuit) : 200 pulls par 6 heures
- Abonnement payant : illimité

En CI/CD, ces limites sont vite atteintes. C’est une des raisons pour lesquelles les entreprises utilisent un **registry privé** qui met en cache les images officielles (voir chapitre 9).

#### Les images multi-architectures

Une même image peut contenir des variantes pour différentes architectures CPU (amd64, arm64). Quand tu fais `docker pull nginx`, Docker télécharge automatiquement la variante correspondant à ton architecture. C’est transparent, mais c’est important si tu développes sur un Mac avec puce Apple (arm64) et que tu déploies sur un serveur x86_64 (amd64).

### ❌ Erreur classique

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

### ✅ Tu sais maintenant…

- La différence entre image (template) et container (instance)
- Docker Hub et les images officielles vs communautaires
- Les tags et pourquoi ne pas utiliser `latest`
- Les variantes d’images (full, slim, alpine, distroless)
- Gérer les images localement (pull, images, rmi, history, inspect)

-----


## Chapitre 5 — Réseau, volumes et persistance

### Le minimum à savoir

#### Le réseau Docker

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

#### L’exposition de ports (rappel et approfondissement)

```bash
docker run -d -p 8080:80 nginx
#              ↑      ↑
#           hôte    container
```

Sans `-p`, le container est isolé du réseau de la machine hôte. Le port est accessible à l’intérieur du réseau Docker, mais pas depuis ton navigateur ou depuis l’extérieur.

Avec `-p 8080:80`, le port 80 du container est accessible via le port 8080 de la machine hôte.

> **Sécurité :** par défaut, `-p 8080:80` expose le port sur **toutes les interfaces réseau** de la machine (0.0.0.0). Pour limiter à localhost uniquement : `-p 127.0.0.1:8080:80`.

#### Les volumes : la persistance des données

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

#### Les 3 types de montages

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

#### Les variables d’environnement

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

### Très utile en pratique

#### Les drivers réseau Docker

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

#### Gérer les volumes

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

#### Cas pratique complet : stack minimale

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

### Bonus

#### Inspecter le réseau

```bash
# Voir les containers connectés à un réseau
docker network inspect medflow

# Depuis l'intérieur d'un container, voir la config réseau
docker exec web cat /etc/hosts
docker exec web ip addr
```

#### Le read-only filesystem

Tu peux lancer un container avec un filesystem en **lecture seule** pour réduire la surface d’attaque :

```bash
docker run --read-only --tmpfs /tmp --tmpfs /run nginx
```

L’application ne peut rien écrire sauf dans `/tmp` et `/run` (montés en tmpfs, en mémoire). Un attaquant qui compromet l’application ne peut pas déposer de fichier sur le disque.

### ❌ Erreur classique

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

### 🧩 Mini-projet (chapitres 3-5)

Crée une stack “blog” minimale :

1. Un container **PostgreSQL** avec un volume persistant et un mot de passe configuré
1. Un container **Nginx** qui sert une page HTML (montée en bind mount depuis ton hôte)
1. Les deux containers sur un **réseau nommé**
1. Nginx accessible sur le port 8080 de ton hôte
1. Vérifie que les données PostgreSQL survivent à un `docker rm` + recréation du container

### ✅ Tu sais maintenant…

- Créer un réseau Docker et y connecter des containers
- Exposer un port avec `-p hôte:container`
- Persister des données avec les volumes (et la différence volume nommé vs bind mount)
- Configurer un container avec les variables d’environnement (`-e`)
- Pourquoi ne pas utiliser le réseau bridge par défaut

-----
