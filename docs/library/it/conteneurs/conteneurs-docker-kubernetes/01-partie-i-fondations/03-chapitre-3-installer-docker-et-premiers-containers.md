---
title: Chapitre 3 — Installer Docker et premiers containers
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### Installer Docker

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

### Vérifier l’installation

```bash
docker version
```


Tu devrais voir deux sections : **Client** et **Server**. Si le Server ne répond pas, le daemon Docker n’est pas démarré (`sudo systemctl start docker`).

```bash
docker info
```


Affiche des informations sur l’installation : nombre de containers, nombre d’images, version du kernel, driver de stockage, etc.

### Ton premier container

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

### Les commandes essentielles

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

### Explorer un container interactif

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

### Exposer un port

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

## Très utile en pratique

### Nommer ses containers

```bash
docker run -d --name mon_nginx -p 8080:80 nginx
docker stop mon_nginx
docker start mon_nginx
docker logs mon_nginx
```


Beaucoup plus pratique que d’utiliser l’ID hexadécimal (`a3f2b1c9d8e7...`).

### Le cycle de vie complet

```
docker create  →  docker start  →  docker stop  →  docker rm
   (créé)           (en cours)       (arrêté)       (supprimé)

  ou directement :
docker run  =  docker create + docker start
```


Un container arrêté **existe encore** (tu peux le voir avec `docker ps -a`, le redémarrer avec `docker start`). Il ne disparaît que quand tu le supprimes (`docker rm`).

### Le nettoyage

Les containers arrêtés et les images téléchargées s’accumulent. Pour nettoyer :

```bash
# Supprimer tous les containers arrêtés
docker container prune

# Supprimer toutes les images non utilisées
docker image prune

# Tout nettoyer d'un coup (containers arrêtés + images non utilisées + réseaux + cache)
docker system prune
```


### Le flag `--rm` : containers jetables

```bash
docker run --rm -it ubuntu bash
```


Le `--rm` supprime automatiquement le container quand il s’arrête. Parfait pour les utilisations ponctuelles (tester une commande, lancer un outil, explorer).

## Bonus

### Voir les ressources consommées

```bash
docker stats
```


Affiche en temps réel le CPU, la mémoire, le réseau et le disque de chaque container — l’équivalent d’un `top` pour les containers.

### Inspecter un container en détail

```bash
docker inspect mon_nginx
```


Renvoie un JSON détaillé avec toute la configuration du container : réseau (adresse IP), volumes, variables d’environnement, état, etc. Utile pour le troubleshooting.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Lance un container Nginx en arrière-plan, expose-le sur le port 8080, vérifie dans ton navigateur, regarde les logs, puis arrête-le et supprime-le.

**Autonome :** Lance un container `python:3.12` en mode interactif (`-it`), tape `python3` à l’intérieur, exécute `print("Hello from a container!")`, puis quitte. Observe que le container s’arrête quand tu quittes.

## ✅ Tu sais maintenant…

- Installer Docker et vérifier l’installation
- Lancer un container avec `docker run`
- Les flags essentiels : `-d` (détaché), `-it` (interactif), `-p` (port), `--name` (nom), `--rm` (jetable)
- Le cycle de vie : run → stop → rm (ou start pour redémarrer)
- Que les containers sont éphémères — les données disparaissent à la suppression
- Les commandes de base : `docker ps`, `docker logs`, `docker exec`, `docker stop`, `docker rm`

-----
