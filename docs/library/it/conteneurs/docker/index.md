---
title: Docker
source: IT/08 Conteneurs & automatisation/Conteneurs/Docker.md
format: cours
revue: '2026-06-14'
---

*De zéro à la conteneurisation, au diagnostic et à la sécurité défensive — Guide pour débutant*

---

> **Prérequis :** des bases en Linux, terminal et réseau (IP / port / DNS). **Aucune** connaissance de Docker ni de la conteneurisation n'est supposée, ni aucun niveau développeur, DevOps ou cloud. Si tu viens de l'administration système, du réseau, du SOC, du pentest débutant ou de la cloud security junior, ce cours est fait pour toi.
> Tout ce dont tu as besoin, c'est une machine Linux (ou une **VM Linux**) capable de faire tourner Docker.

---

> **Variante de ce cours : "orienté cyber / cloud security junior".**
> Ce cours garde **tout le tronc commun opérationnel** (lancer, diagnostiquer, construire, connecter, orchestrer des conteneurs), parce qu'on ne sécurise bien que ce qu'on sait opérer. Mais il ajoute, partout, une **coloration cybersécurité défensive** : surface d'attaque, isolation, privilèges, secrets, exposition réseau, durcissement. L'esprit du cours tient en une phrase :
>
> **Docker débutant IT/cyber : savoir conteneuriser, diagnostiquer, puis sécuriser — pour préparer Kubernetes.**

---

> **Ce cours est le jumeau de mon cours Kubernetes.** Docker est la **fondation** de Kubernetes : un conteneur, une image, un runtime, un réseau de conteneurs… tout ce que tu apprends ici resservira directement quand tu passeras à l'orchestration. Le dernier chapitre construit explicitement le **pont** entre les deux.

---

### À qui s'adresse ce cours

- À un **admin Linux / réseau** qui doit comprendre et opérer des conteneurs sans devenir développeur.
- À un **analyste SOC** qui verra passer des logs, des événements et des alertes venant de conteneurs.
- À un **cloud security junior** qui doit auditer et durcir des environnements conteneurisés.
- À un **pentester débutant** qui veut comprendre la surface d'attaque des conteneurs **côté défense** d'abord.
- À toute personne curieuse qui veut un modèle mental clair de la conteneurisation avant de taper des commandes.

### Ce que ce cours n'est PAS

Pour rester pédagogique et accessible, certains sujets sont **volontairement exclus**. Ils méritent un cours à part, **après** celui-ci :

- ❌ Ce n'est **pas** un cours **Docker pour développeur fullstack** (on ne code pas d'application).
- ❌ Ce n'est **pas** un cours **DevOps expert** ni un cours **CI/CD avancé**.
- ❌ Ce n'est **pas** un cours d'**orchestration de production** (Docker Swarm en profondeur, clusters managés).
- ❌ Ce n'est **pas** un cours **cloud provider** — on reste en **lab local**.
- ❌ Ce n'est **pas** un cours d'**exploitation offensive** des conteneurs. On reste **défensif** : comprendre les risques pour les **réduire**, pas pour les exploiter.

Ces sujets peuvent venir **après**, une fois les fondamentaux acquis (voir l'annexe « Suite logique » — qui commence d'ailleurs par **Kubernetes**).

### 🎯 L'objectif final, concrètement

Pour que tu saches exactement où tu vas, à la **fin de ce cours** tu dois être capable de :

- **Expliquer** ce qu'est vraiment un conteneur, et le distinguer d'une image, d'un processus et d'une VM.
- **Lancer, observer, arrêter, supprimer** un conteneur sans hésiter.
- **Diagnostiquer** un conteneur en panne avec `logs`, `exec`, `inspect`, `stats`, `events`.
- **Comprendre et choisir** des images (Docker Hub, tags, layers, digest, registries).
- **Lire et écrire** un Dockerfile simple, et le **builder** proprement (`.dockerignore`, build context).
- **Gérer** la persistance (volumes, bind mounts), la configuration (variables d'env) et le réseau.
- **Lancer une petite stack multi-services** avec Docker Compose (v2).
- **Repérer et corriger** les mauvaises configurations de sécurité les plus courantes (root, `--privileged`, Docker socket, secrets dans l'image, `latest`, bind mount large, ports exposés…).
- **Auditer** un environnement Docker mal configuré et proposer un durcissement de base.
- **Faire le pont** vers Kubernetes en sachant ce qui se transpose directement.

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici dès qu'un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Conteneur** | Un processus isolé qui embarque une application et ses dépendances |
| **Image** | Le « modèle » figé à partir duquel on lance un conteneur |
| **Layer (couche)** | Une strate empilée qui compose une image (chaque instruction en ajoute une) |
| **Tag** | Une étiquette **mobile** sur une image (ex. `nginx:1.27`) |
| **Digest** | L'empreinte **immuable** d'une image (ex. `nginx@sha256:…`) |
| **Registry** | Un dépôt d'images (Docker Hub en est un) |
| **Docker Hub** | Le registry public par défaut de Docker |
| **OCI** | Le **standard** d'images et de runtimes que respectent Docker, containerd, Kubernetes… |
| **Dockerfile** | Le fichier texte qui décrit comment construire une image |
| **Build context** | L'ensemble des fichiers envoyés au daemon pour construire une image |
| **`.dockerignore`** | Le fichier qui exclut des éléments du build context (cousin du `.gitignore`) |
| **Volume** | Un espace de stockage **géré par Docker**, persistant |
| **Bind mount** | Un montage d'un **dossier de l'hôte** directement dans le conteneur |
| **Docker Engine** | Le moteur Docker : CLI + daemon + API |
| **Docker daemon (`dockerd`)** | Le service en arrière-plan qui exécute réellement les opérations (tourne en **root**) |
| **Docker CLI** | L'outil en ligne de commande `docker` qui parle au daemon |
| **Docker socket** | Le point de communication avec le daemon (`/var/run/docker.sock`) — **très sensible** |
| **Runtime de conteneurs** | Le composant bas niveau qui lance les conteneurs (souvent **containerd**) |
| **Namespace (Linux)** | Une cloison de **visibilité** du noyau (processus, réseau, fichiers…) |
| **cgroup** | Un mécanisme du noyau qui **limite les ressources** (CPU, RAM) |
| **Port mapping** | La mise en relation d'un port du conteneur avec un port de l'hôte |
| **Docker Compose** | L'outil qui décrit et lance une **stack** de plusieurs conteneurs via un fichier |
| **`compose.yaml`** | Le fichier déclaratif d'une stack Compose |
| **Healthcheck** | Un test qui indique si un conteneur est **réellement** en bonne santé |
| **Restart policy** | La règle qui décide si/quand un conteneur redémarre tout seul |

---

### Comment penser la containerisation

Avant de taper la moindre commande, il faut comprendre **la grande idée** qui structure toute la conteneurisation. Si tu retiens une chose de ce cours, c'est celle-ci :

```
   EMPAQUETER              ISOLER                    JETER & RECRÉER
   une app + ses     →     la faire tourner    →     détruire et relancer
   dépendances dans        comme si elle était        sans douleur, à
   une unité figée         seule au monde             l'identique
```


La conteneurisation, c'est **empaqueter une application avec tout ce dont elle a besoin dans une unité isolée, reproductible et jetable.** Trois mots, trois idées à garder en tête à chaque chapitre :

1. **Isolation** — le conteneur *croit* être seul sur la machine. Il a sa propre vue des processus, des fichiers, du réseau. (C'est une illusion construite par le noyau Linux — on verra comment au Ch. 3.)
2. **Reproductibilité** — la **même image** produit le **même conteneur**, sur ta machine comme sur un serveur. C'est la fin du « ça marche sur ma machine ».
3. **Jetabilité** — un conteneur est **éphémère**. On ne le « répare » pas comme un serveur : on le **détruit et on le recrée** à partir de l'image. L'état important vit **ailleurs** (volumes).

> **Garde ce schéma en tête.** Quand un comportement de Docker te surprendra (« j'ai perdu mes données en supprimant le conteneur ?! »), la réponse viendra presque toujours de l'une de ces trois idées — ici, la **jetabilité** : un conteneur ne garde rien par défaut.

Ce modèle est le **cousin** du modèle « état désiré → réconciliation » de Kubernetes. La conteneurisation prépare le terrain ; l'orchestration ajoutera la couche au-dessus.

---

### Les 3 lunettes : Lab, Production réelle, Sécurité

Tout au long du cours, tu porteras **trois paires de lunettes**. On les pose dès maintenant pour ne jamais les confondre (mêmes lunettes que dans le cours Kubernetes, pour que tu retrouves tes repères) :

- **🧪 Lunette LAB** — ce qu'on fait sur ta machine pour **apprendre et casser sans risque**. Simplifié, local, jetable.
- **🏭 Lunette PRODUCTION RÉELLE** — ce qui changerait si de **vrais utilisateurs** dépendaient de tes conteneurs (limites de ressources, healthchecks, secrets bien gérés, images figées). Le cours **signale** ces différences sans chercher à faire de toi un ingénieur de production.
- **🛡️ Lunette SÉCURITÉ** — ce qu'un **défenseur** doit surveiller : qu'est-ce qui tourne en root, qu'est-ce qui est exposé, où sont les secrets, qu'est-ce que le conteneur partage avec l'hôte, quelle est la surface d'attaque.

Tu verras régulièrement des encadrés qui changent de lunette. Quand tu liras **🧪 Lab vs 🏭 Production réelle**, c'est qu'une chose acceptable en lab serait dangereuse en vrai. Quand tu liras **🛡️ Réflexe sécurité** ou **🔍 Réflexe diagnostic**, c'est un automatisme à acquérir.

---

### Prérequis techniques et matériel recommandé

Docker est plus léger qu'un cluster Kubernetes, mais autant cadrer l'environnement tout de suite pour éviter les frustrations.

#### Connaissances supposées (rappels inclus dans le cours)

| Domaine | Niveau attendu | Où c'est rappelé |
|---------|----------------|------------------|
| **Linux de base** | Se déplacer, éditer un fichier, lire un log | Supposé acquis |
| **Terminal** | Lancer des commandes, lire une sortie | Supposé acquis |
| **Réseau** | Comprendre IP, port, DNS (juste les bases) | Rappelé au fil du cours |
| **Processus Linux** | Savoir ce qu'est un processus, `ps` | Rappelé au **Chapitre 3** |
| **YAML** | Aucune connaissance requise | **Introduit en Partie VII (Compose)** |

> Si « IP », « port » et « processus » sont totalement flous pour toi, fais d'abord un détour par les bases Linux/réseau. Le reste, le cours te le donne.

#### Matériel recommandé

| Ressource | Minimum | Confortable |
|-----------|---------|-------------|
| **RAM** | 2 Go libres | 4 Go ou plus |
| **CPU** | 2 cœurs | 4 cœurs |
| **Disque** | 15 Go libres (les images s'accumulent vite) | 40 Go ou plus |
| **OS** | Linux, macOS, ou Windows | **Linux** (le plus simple et le plus formateur) |

#### 🧰 Docker Engine vs Docker Desktop vs VM Linux

C'est **la** décision d'environnement à comprendre avant d'installer quoi que ce soit. Selon ta machine, « installer Docker » ne veut pas dire la même chose :

| Option | Ce que c'est | Pour qui |
|--------|--------------|----------|
| **Docker Engine** (sur Linux) | Le moteur Docker **natif**, en ligne de commande | **Recommandé pour ce cours** |
| **Docker Desktop** (Windows / macOS) | Une application qui lance Docker dans une **VM cachée**, avec interface graphique | Windows/Mac, débutants visuels |
| **Docker dans une VM Linux** | Docker Engine installé dans une machine virtuelle Linux | Excellent compromis sur Windows/Mac |

> **Recommandation pédagogique :** apprends sur une **machine Linux** ou une **VM Linux** avec **Docker Engine**. Tu travailles alors avec le « vrai » Docker, sans couche d'abstraction. **Docker Desktop fonctionne très bien** aussi, mais il ajoute une VM intermédiaire qui peut compliquer le réseau et les montages de fichiers.

#### ⚠️ Limites de WSL (Windows)

Si tu es sous Windows et que tu comptes utiliser **WSL2** (souvent via Docker Desktop) :

- C'est **jouable**, et même courant en entreprise.
- Mais les **chemins de fichiers** (bind mounts), le **réseau** et les **performances disque** entre Windows et WSL sont des sources de pièges qui n'ont **rien à voir avec Docker lui-même**.
- Pour apprendre **proprement**, une **VM Linux** t'évite cette couche de complexité.

---

### ⚠️ Encadré essentiel — Commandes Docker à manipuler avec prudence

Avant d'aller plus loin, lis ceci **attentivement**. Certaines commandes Docker sont **destructrices** et n'affichent **aucune demande de confirmation**. En lab, tu peux tout casser sans risque. Mais ces réflexes te suivront sur de vraies machines, alors prends les bonnes habitudes **maintenant**.

#### Les commandes qui détruisent

```bash
docker rm -f <conteneur>      # force la suppression d'un conteneur EN MARCHE (pas de confirmation)
docker rmi <image>            # supprime une image (casse ce qui en dépend)
docker volume rm <volume>     # ☠️ supprime un volume → PERTE DE DONNÉES possible
docker volume prune           # ☠️ supprime TOUS les volumes non utilisés
docker system prune           # ☠️ supprime conteneurs arrêtés, réseaux, images pendantes, cache
docker system prune -a        # ☠️☠️ encore plus agressif : TOUTES les images non utilisées
```


#### Les pièges qui font le plus de dégâts pour un débutant

```bash
docker volume prune           # Tu crois "faire le ménage"... tu effaces des données peut-être uniques
docker system prune -a        # Lancé sur une machine partagée, tu supprimes le travail des autres
```


#### Les 3 règles d'or

> **1. Regarde AVANT de supprimer.**
> ```bash
> docker ps -a          # tous les conteneurs (même arrêtés)
> docker volume ls      # tous les volumes
> docker images         # toutes les images
> ```
> Tu vois **exactement** ce qui existe avant de décider quoi enlever.
>
> **2. Ne lance JAMAIS un `prune` à l'aveugle sur une machine partagée.**
> `prune` ne te demande pas la permission objet par objet. Sur un serveur partagé, c'est destructeur pour tout le monde.
>
> **3. Ne supprime JAMAIS un volume sans savoir quelles données il porte.**
> Un volume peut être la seule trace d'une base de données. Une fois supprimé, c'est parfois définitif.

🛡️ **Réflexe sécurité dès maintenant :** ces commandes destructrices sont aussi ce qu'un **accident** ou un **accès mal maîtrisé** peut déclencher. Et souviens-toi : **appartenir au groupe `docker` revient à avoir root sur la machine** (on y reviendra au Ch. 4). Qui peut lancer Docker peut beaucoup.

> **Note — le mode « rootless ».** Docker peut aussi tourner en **mode rootless**, où le daemon ne s'exécute pas avec les privilèges root classiques. Ce mode **réduit certains risques** (notamment en cas d'évasion), mais ajoute des **limites** et de la **complexité** (réseau, montages, certaines fonctionnalités). On le **mentionne ici** pour ne pas être trop catégorique sur « daemon Docker = root », et on le **développe en annexe** plutôt que dans le cœur du cours, pour ne pas alourdir l'apprentissage débutant.

---

### 🧨 La Boîte à risques Docker / containerisation

Voici la **carte des dangers** que tu vas apprendre à reconnaître et à neutraliser tout au long du cours. Tu n'as **pas** besoin de tout comprendre maintenant — c'est une **carte mentale** à garder sous les yeux. Chaque ligne sera traitée en détail dans le chapitre indiqué. C'est l'équivalent, pour Docker, d'une check-list d'audit défensif.

Les risques sont regroupés en **4 familles** pour les mémoriser plus facilement. **Deux d'entre eux reviennent partout dans le cours et méritent une attention spéciale : tourner en root et monter le Docker socket.**

#### Famille 1 — Privilèges (le cœur du danger Docker)

| Risque | Pourquoi c'est dangereux | Traité au |
|--------|--------------------------|-----------|
| ⭐ **Conteneur lancé en root** | En cas d'évasion ou de mauvaise config, augmente fortement le risque d'obtenir des privilèges élevés sur l'hôte | Ch. 17 / 18 |
| ⭐ **Conteneur `--privileged`** | Désactive l'essentiel des protections : quasi-accès total à l'hôte | Ch. 17 |
| ⭐ **Montage de `/var/run/docker.sock`** | Donner le socket = donner le **contrôle de toute la machine** | Ch. 17 |

#### Famille 2 — Secrets

| Risque | Pourquoi c'est dangereux | Traité au |
|--------|--------------------------|-----------|
| **Secret dans un Dockerfile / une image** | Reste dans les **layers** même « supprimé » ensuite : compromis à vie | Ch. 10 / 11 |
| **Secret en variable d'env sans réflexion** | Visible dans `inspect`, l'environnement du process, parfois les logs | Ch. 13 / 18 |

#### Famille 3 — Images

| Risque | Pourquoi c'est dangereux | Traité au |
|--------|--------------------------|-----------|
| **Image inconnue / non maintenue** | Code arbitraire qui tourne chez toi, vulnérabilités non corrigées | Ch. 8 |
| **« Officielle » prise pour « sûre »** | Une image officielle reste à versionner, mettre à jour et scanner | Ch. 8 / 19 |
| **Tag `latest` / absence de digest** | Version non maîtrisée = surface d'attaque mouvante | Ch. 9 |
| **Image trop grosse / packages inutiles** | Plus de surface d'attaque, plus de CVE potentielles | Ch. 10 / 18 |
| **Pas de `.dockerignore` / build context trop large** | Risque d'embarquer `.env`, clés, tokens dans l'image | Ch. 11 |

#### Famille 4 — Exposition & ressources

| Risque | Pourquoi c'est dangereux | Traité au |
|--------|--------------------------|-----------|
| **Ports exposés inutilement / sur `0.0.0.0`** | Service accessible depuis tout le réseau, pas juste en local | Ch. 13 |
| **Bind mount trop large (`/`, `/etc`, `/var`, `/home`)** | Le conteneur lit/écrit sur des chemins sensibles de l'hôte | Ch. 12 |
| **Volumes mal protégés** | Fuite ou altération de données | Ch. 12 |
| **Absence de limites CPU/RAM** | Un conteneur peut épuiser la machine (déni de service) | Ch. 18 |
| **Absence de `HEALTHCHECK`** | Un conteneur mort/malade passe inaperçu | Ch. 16 |

#### Et la confusion fondamentale, à dissiper en premier

| Risque | Pourquoi c'est dangereux | Traité au |
|--------|--------------------------|-----------|
| **Croire qu'un conteneur isole comme une VM** | Fausse confiance : le noyau est **partagé** avec l'hôte | Ch. 2 |

> Tu retrouveras cette boîte, **complétée et exploitée**, dans la Partie VIII et dans le capstone « audit d'un environnement Docker mal configuré ».

---

### Sur la montée en difficulté

Docker est **plus concret** que Kubernetes : tu lanceras ton premier conteneur dès la Partie II. La Partie I (conceptuelle) est donc **courte** — juste de quoi poser le vocabulaire qui piège tout le monde (VM, conteneur, image, processus) avant de mettre les mains dedans.

À partir de la Partie IV (images) et surtout de la Partie V (Dockerfile), le cours demande **plus de pratique**. Il est normal de devoir :

- Refaire un build plusieurs fois (le cache et l'ordre des instructions déroutent au début).
- Bloquer sur les volumes, le réseau ou Compose — c'est **normal**.
- Relire un chapitre à tête reposée.

> **Conseil important :** si un chapitre te paraît flou, **continue quand même**. Plusieurs notions ne s'éclairent qu'à la lumière de la suite (les images éclairent le Dockerfile, le réseau éclaire Compose). Reviens en arrière une fois que tu as vu la suite.

Ne te juge pas. **La patience compte plus que la vitesse.**

> **Et surtout :** le but n'est **pas** de mémoriser toutes les commandes Docker. C'est de comprendre le **cycle** : `image → conteneur → logs/diagnostic → données/réseau → suppression/recréation`. Une fois ce cycle clair dans ta tête, les commandes deviennent évidentes et se retrouvent dans la cheat-sheet. Apprends le **cycle**, pas la liste.

---

### Table des matières

**PARTIE 0 — PRÉAMBULE** *(tu es ici)*

**PARTIE I — COMPRENDRE LA CONTAINERISATION**

1. [Pourquoi la containerisation existe](01-partie-i-comprendre-la-containerisation/01-chapitre-1-pourquoi-la-containerisation-existe.md)
2. [VM vs conteneur, image vs conteneur, processus](01-partie-i-comprendre-la-containerisation/02-chapitre-2-vm-vs-conteneur-image-vs-conteneur-proc.md)
3. [Sous le capot : namespaces et cgroups (en clair)](01-partie-i-comprendre-la-containerisation/03-chapitre-3-sous-le-capot-namespaces-et-cgroups-en.md)

**PARTIE II — PREMIERS PAS AVEC DOCKER**

4. Installer Docker et comprendre son architecture
5. `docker run` : lancer son premier conteneur
6. Le cycle de vie d'un conteneur

**PARTIE III — OBSERVER ET DIAGNOSTIQUER UN CONTENEUR**

7. Les réflexes : logs, exec, inspect, stats, cp, events

**PARTIE IV — LES IMAGES DOCKER**

8. Images, Docker Hub et registries (et le standard OCI)
9. Tags, layers et digest

**PARTIE V — CONSTRUIRE SES PROPRES IMAGES**

10. Le Dockerfile : écrire sa première image
11. `docker build`, build context et `.dockerignore`

**PARTIE VI — DONNÉES ET RÉSEAU**

12. Volumes, bind mounts et persistance
13. Variables d'environnement et ports
14. Réseaux Docker

**PARTIE VII — ORCHESTRER EN PETIT : DOCKER COMPOSE**

15. Docker Compose (v2) : décrire une stack
16. Compose en pratique : healthchecks, restart policies, dépendances

**PARTIE VIII — SÉCURISER ET DURCIR LES CONTENEURS**

17. Les dangers fondamentaux : root, privileged, Docker socket
18. Réduire la surface : images minimales, secrets, limites
19. Scanner et maintenir ses images (`docker system df`, scan, nettoyage)

**PARTIE IX — MINI-PROJETS INTÉGRATEURS**

**PARTIE X — 🔴 BONUS — VERS KUBERNETES ET AU-DELÀ** (pont Docker → K8s, maintenance, observabilité)

**ANNEXES** (cheat-sheets commandes/Dockerfile/compose, glossaire étendu, réflexes diagnostic & sécurité, Docker socket en profondeur, suite logique)

---
---

## Sommaire

- [PARTIE I — Comprendre la containerisation](01-partie-i-comprendre-la-containerisation/index.md)
    - [Chapitre 1 — Pourquoi la containerisation existe](01-partie-i-comprendre-la-containerisation/01-chapitre-1-pourquoi-la-containerisation-existe.md)
    - [Chapitre 2 — VM vs conteneur, image vs conteneur, processus](01-partie-i-comprendre-la-containerisation/02-chapitre-2-vm-vs-conteneur-image-vs-conteneur-proc.md)
    - [Chapitre 3 — Sous le capot : namespaces et cgroups (en clair)](01-partie-i-comprendre-la-containerisation/03-chapitre-3-sous-le-capot-namespaces-et-cgroups-en.md)
- [PARTIE II — Premiers pas avec Docker](02-partie-ii-premiers-pas-avec-docker/index.md)
    - [Chapitre 4 — Installer Docker et comprendre son architecture](02-partie-ii-premiers-pas-avec-docker/01-chapitre-4-installer-docker-et-comprendre-son-arch.md)
    - [Chapitre 5 — docker run : lancer son premier conteneur](02-partie-ii-premiers-pas-avec-docker/02-chapitre-5-docker-run-lancer-son-premier-conteneur.md)
    - [Chapitre 6 — Le cycle de vie d'un conteneur](02-partie-ii-premiers-pas-avec-docker/03-chapitre-6-le-cycle-de-vie-d-un-conteneur.md)
