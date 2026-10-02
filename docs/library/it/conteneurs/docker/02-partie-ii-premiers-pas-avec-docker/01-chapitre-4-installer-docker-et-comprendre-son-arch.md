---
title: Chapitre 4 — Installer Docker et comprendre son architecture
source: IT/08 Conteneurs & automatisation/Conteneurs/Docker.md
note: Docker
up:
- - Docker
  - ../index.md
- - PARTIE II — Premiers pas avec Docker
  - index.md
---

## Le minimum à savoir

### Docker n'est pas « un programme », c'est trois choses

Quand tu tapes `docker run`, tu crois parler à « Docker ». En réalité, tu déclenches une **conversation entre trois composants** qu'il faut distinguer une fois pour toutes :

```
   TOI ──▶  Docker CLI  ──API──▶  Docker daemon (dockerd)  ──▶  conteneurs
            (le client)           (le moteur, tourne en root)
   "docker run nginx"             reçoit l'ordre, le réalise
```


- **Docker CLI** (`docker`) : l'**outil en ligne de commande**. C'est lui que tu tapes. Il ne fait rien lui-même : il **transmet** ta demande.
- **Docker daemon** (`dockerd`) : le **moteur**, un service qui tourne en arrière-plan. C'est lui qui **télécharge les images, crée les conteneurs, gère les réseaux et les volumes**. Il tourne avec les privilèges **root**.
- **L'API Docker** : le **canal** par lequel la CLI parle au daemon. Par défaut, ce canal est le **Docker socket** (`/var/run/docker.sock`).

L'ensemble (CLI + daemon + API) s'appelle le **Docker Engine**.

### Pourquoi cette distinction est cruciale (et pas que théorique)

Parce qu'elle explique **le premier grand réflexe de sécurité Docker** :

> Le **daemon tourne en root**. La CLI ne fait que lui passer des ordres. Donc **quiconque peut parler au daemon peut faire faire à root à peu près n'importe quoi sur la machine** — par exemple monter le disque entier de l'hôte dans un conteneur et le lire.

C'est aussi pour ça qu'on dit qu'**appartenir au groupe `docker` équivaut à avoir root** sur la machine : être dans ce groupe, c'est avoir le droit de parler au daemon. Ce n'est pas un détail d'administration, c'est une **décision de sécurité**.

> **Rappel du préambule :** Docker peut tourner en mode **rootless** pour atténuer ce point. On reste ici sur le mode classique (le plus répandu), en gardant cette nuance en tête.

### Ce dont tu as besoin

Deux choses : le **daemon** qui tourne, et la **CLI** pour lui parler. Sur Linux avec Docker Engine, les deux s'installent ensemble. Sur Docker Desktop, l'application gère le daemon (dans une VM cachée) et te fournit la CLI.

## Très utile en pratique

### Installer (vue d'ensemble)

> Comme pour tout outil, **les commandes d'installation vieillissent vite**. La **documentation officielle Docker fait foi** — suis-la pour ton système plutôt qu'un copier-coller daté. L'idée générale sur Linux : ajouter le dépôt officiel Docker, puis installer le paquet `docker-ce` (Docker Community Edition).

Après installation, **trois commandes** te confirment que tout est en place :

```bash
docker version      # versions du Client (CLI) ET du Server (daemon) : les deux doivent répondre
docker info         # vue d'ensemble : nb de conteneurs, images, driver de stockage, etc.
docker run hello-world   # le "tour complet" : pull d'une image + lancement d'un conteneur
```


### Lire `docker version` (et ce qu'il révèle)

```text
$ docker version
Client:
 Version:    27.x.x
 ...
Server: Docker Engine - Community
 Engine:
  Version:   27.x.x
  ...
```


Vois les **deux** blocs ? **Client** = la CLI, **Server** = le daemon. Si le bloc *Server* manque ou renvoie une erreur du type « cannot connect to the Docker daemon », c'est que **le daemon ne tourne pas** ou que **tu n'as pas le droit de lui parler** — deux pannes classiques (voir l'erreur classique plus bas).

### Le premier conteneur : `hello-world`

```bash
docker run hello-world
```


```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world      ← l'image n'était pas là, Docker la télécharge
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```


En une commande, tu viens de vivre **tout le cycle** : Docker a cherché l'image en local, ne l'a pas trouvée, l'a **téléchargée** depuis Docker Hub, puis a **lancé un conteneur** à partir d'elle. Le conteneur a affiché son message, puis s'est **terminé**. C'est la conteneurisation en miniature.

## Application admin / cyber

- **Côté admin :** `docker info` est ta **fiche d'identité** de l'installation : version, nombre de conteneurs/images, **driver de stockage**, dossier de données. C'est le premier endroit où regarder pour comprendre une machine Docker que tu découvres.
- **Côté SOC / cyber :** la séparation CLI/daemon/socket **est** le modèle de menace de Docker. Retiens trois choses :
  - 🛡️ Le **daemon = root**. Le compromettre ou détourner le socket, c'est compromettre l'hôte.
  - 🛡️ Le **groupe `docker` = root de fait**. Qui tu ajoutes à ce groupe est une **décision de sécurité**, pas de confort.
  - 🛡️ Le **socket `/var/run/docker.sock`** est l'objet le plus sensible de tout l'écosystème. On verra au Ch. 17 pourquoi le **monter dans un conteneur** est l'une des pires erreurs possibles.

🔍 **Réflexe diagnostic :** devant une machine Docker inconnue, commence par `docker version` (le daemon répond-il ?) et `docker info` (qu'y a-t-il dessus ?). Ces deux commandes te disent l'essentiel avant même de lister quoi que ce soit.

## ❌ Erreur classique

> **« Cannot connect to the Docker daemon » — et conclure que Docker est cassé.**

C'est **la** panne d'installation la plus fréquente. Deux causes, deux réflexes :

1. **Le daemon ne tourne pas.** Sur Linux, il faut démarrer le service :
   ```bash
   sudo systemctl start docker      # démarrer le daemon maintenant
   sudo systemctl enable docker     # le démarrer automatiquement au boot
   ```
2. **Tu n'as pas le droit de parler au daemon.** Ton utilisateur n'est pas dans le groupe `docker`, donc seul `sudo docker ...` fonctionne. On peut ajouter l'utilisateur au groupe :
   ```bash
   sudo usermod -aG docker $USER    # puis se déconnecter/reconnecter
   ```
   > ⚠️ **Mais souviens-toi de ce que ça signifie :** rejoindre le groupe `docker`, c'est s'octroyer un **équivalent root**. En lab perso, c'est commode. Sur une machine partagée ou sensible, c'est une décision à prendre **en conscience**.

## Exercices

**Guidé :** Installe Docker pour ton système (en suivant la doc officielle), puis lance la séquence `docker version`, `docker info`, `docker run hello-world`. Tu dois voir **les deux blocs** Client/Server répondre, puis le message « Hello from Docker! ». Si tu tombes sur « cannot connect to the Docker daemon », relie l'erreur aux deux causes ci-dessus et note la commande qui a résolu le problème.

**Autonome :** Lance `docker info` et repère **trois informations** : le nombre de conteneurs, le nombre d'images, et le **dossier racine de Docker** (*Docker Root Dir*). Écris en une phrase pourquoi un analyste qui découvre une machine voudrait connaître ces trois éléments.

**Défi :** Explique, avec tes propres mots et en 4-5 lignes, **pourquoi `sudo docker run -v /:/hôte ...` est si dangereux**. Indice : relie le fait que **le daemon tourne en root** au fait qu'on lui demande de **monter la racine de l'hôte** dans un conteneur. Tu n'as pas besoin de l'exécuter — c'est un exercice de **modèle de menace**, à rapprocher du Ch. 17.

## ✅ Tu sais maintenant…

- Que Docker = **CLI** (le client) + **daemon `dockerd`** (le moteur, en root) + **API/socket** (le canal).
- Que l'ensemble s'appelle le **Docker Engine**.
- Vérifier une installation avec `docker version`, `docker info`, `docker run hello-world`.
- Lire les deux blocs **Client/Server** et diagnostiquer « cannot connect to the daemon ».
- Que **le daemon tourne en root** et que le **groupe `docker` ≈ root** : un point de sécurité fondateur.
- Que le **socket Docker** est l'objet le plus sensible de l'écosystème (suite au Ch. 17).

---
