---
title: Docker
source: IT/10_virtualization-containers/Docker.md
---

### De zéro à la conteneurisation, au diagnostic et à la sécurité défensive — Guide pour débutant

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

1. [Pourquoi la containerisation existe](#chapitre-1-pourquoi-la-containerisation-existe)
2. [VM vs conteneur, image vs conteneur, processus](#chapitre-2-vm-vs-conteneur-image-vs-conteneur-processus)
3. [Sous le capot : namespaces et cgroups (en clair)](#chapitre-3-sous-le-capot-namespaces-et-cgroups-en-clair)

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

## PARTIE I — COMPRENDRE LA CONTAINERISATION

> Dans toute cette partie, on **manipule très peu**. On installe juste de quoi vérifier, et surtout on construit le **modèle mental** et le vocabulaire. Résiste à l'envie de « faire » : ici, on **comprend**. La pratique arrive vite, dès la Partie II.

---

## Chapitre 1 — Pourquoi la containerisation existe

### Le minimum à savoir

#### Pourquoi commencer par « le problème » ?

Beaucoup de gens apprennent Docker en tapant des commandes qu'ils ne comprennent pas. Résultat : ils savent *faire* des choses, mais paniquent dès que ça casse. On va éviter ça. **La conteneurisation est une réponse à des problèmes très concrets.** Si tu comprends les problèmes, les solutions deviennent évidentes.

#### Le cauchemar du « ça marche sur ma machine »

Imagine la scène, vécue par tous les admins du monde :

- Un développeur te livre une application. **« Chez moi, ça marche. »**
- Tu l'installes sur le serveur. Ça **plante**. Mauvaise version de Python. Bibliothèque manquante. Variable d'environnement absente.
- Tu passes l'après-midi à reproduire « son » environnement à la main. Tu finis par y arriver.
- Trois mois plus tard, nouveau serveur. **Tout est à refaire.** Et tu as oublié la moitié des bricolages.

Ce problème a un nom : l'**enfer des dépendances**. Une application ne tourne pas toute seule — elle dépend d'un langage, de bibliothèques, de fichiers de config, de versions précises. Si l'environnement diffère **un peu**, tout casse.

#### L'idée libératrice

Et si, au lieu de réinstaller l'environnement à chaque fois, on **empaquetait l'application AVEC son environnement** dans une boîte unique, qu'on pourrait déplacer telle quelle ?

> C'est **exactement** l'idée de la conteneurisation. Le conteneur embarque l'application **et** ses dépendances. La même boîte tourne **à l'identique** sur ton portable, sur le serveur de test et sur le serveur de production. Fini le « ça marche sur ma machine » : **ça marche partout pareil, parce que c'est la même boîte.**

#### La définition simple

> **Conteneuriser, c'est emballer une application avec tout ce dont elle a besoin pour tourner, dans une unité standardisée, isolée et reproductible — qu'on peut lancer, déplacer et détruire facilement.**

Docker est l'outil qui a rendu cette idée **simple et populaire**. Ce n'est pas le seul, mais c'est la référence par laquelle on apprend.

### Très utile en pratique

Tu n'as **rien à taper** dans ce chapitre — c'est du cadrage mental. Mais voici la traduction directe des corvées d'admin en **promesses de la conteneurisation** :

| Corvée d'admin classique | Ce que la conteneurisation apporte |
|--------------------------|-------------------------------------|
| Réinstaller l'environnement sur chaque serveur | **Reproductibilité** : la même image partout |
| « Ça marche chez moi, pas chez toi » | **Cohérence** : même boîte = même comportement |
| Peur de casser le serveur en testant | **Jetabilité** : on lance, on teste, on jette |
| Conflits entre deux applis sur le même serveur | **Isolation** : chacune dans sa boîte |
| Déploiement long et manuel | **Rapidité** : démarrage quasi instantané |

### Application admin / cyber

- **Côté admin système :** la conteneurisation remplace une pile de procédures d'installation manuelles et fragiles par des **images reproductibles**. Ce que tu sais déjà en Linux n'est **pas perdu** — un conteneur, c'est du Linux, on le verra au Ch. 3.
- **Côté SOC / cyber :** un environnement **reproductible** est un environnement **auditable**. Si tu sais exactement ce qu'il y a dans une image, tu sais ce qui tourne. À l'inverse, un serveur bricolé à la main pendant des années est une **boîte noire** dont personne ne connaît le contenu réel — un cauchemar pour la sécurité.

🛡️ **Réflexe sécurité (à garder pour tout le cours) :** « reproductible » et « maîtrisé » vont ensemble. Chaque fois qu'une image est claire, minimale et figée, elle est aussi plus facile à **défendre et auditer**. On reviendra sans cesse sur ce lien.

### ❌ Erreur classique

> **Croire que la conteneurisation sert juste à « gagner du temps de déploiement ».**

C'est un effet, pas le cœur. Le vrai apport, c'est la **reproductibilité** et l'**isolation** : savoir que ce qui tourne en production est **exactement** ce que tu as testé et audité. Pour un profil cyber, c'est ça qui compte : un environnement reproductible est un environnement sur lequel on peut **raisonner**.

### Exercices

**Guidé :** Sur une feuille (ou un fichier texte), raconte une situation réelle (vécue ou imaginée) de **« ça marche sur ma machine »** : une appli, un script ou un outil qui marchait quelque part et pas ailleurs. Identifie **précisément** ce qui différait (version, bibliothèque, config, OS). Tu viens de nommer le problème que Docker résout.

**Autonome :** Reprends le tableau « corvée → promesse ». Pour **3 lignes**, écris une phrase qui relie la promesse à **ton métier** (admin, SOC, réseau…). Exemple : « Isolation → je peux faire tourner deux outils incompatibles sans qu'ils se gênent. »

**Défi :** En une demi-page, explique à un collègue **non technique** ce qu'apporte la conteneurisation, **sans utiliser** les mots « conteneur », « image » ou « Docker ». Utilise une analogie (un conteneur maritime standardisé, un plat préparé sous vide qu'on réchauffe à l'identique partout…). Si tu y arrives, tu as compris le **pourquoi**.

### ✅ Tu sais maintenant…

- **Pourquoi** la conteneurisation existe : résoudre l'enfer des dépendances et le « ça marche sur ma machine ».
- Que l'idée centrale est d'**empaqueter l'app avec son environnement** dans une unité reproductible.
- Les grandes promesses : **reproductibilité, cohérence, isolation, jetabilité, rapidité**.
- Que Docker est l'**outil de référence** qui a popularisé cette idée.
- Que **reproductible = auditable**, un point clé pour la sécurité.

---

## Chapitre 2 — VM vs conteneur, image vs conteneur, processus

### Le minimum à savoir

#### Les 4 mots que tout le monde confond

Ce chapitre pose le vocabulaire qui piège **tous** les débutants. Prends ton temps ici : si ces 4 mots sont clairs, tout le reste du cours coule.

#### Image vs conteneur

- Une **image** est un **modèle figé** : l'application + ses dépendances, empaquetées. C'est un fichier inerte, comme un plan ou une recette.
- Un **conteneur** est une **instance en cours d'exécution** de cette image. C'est le plan **devenu réalité** qui tourne.

> Analogie : l'**image** est la recette, le **conteneur** est le plat cuisiné. Avec une seule recette, tu peux cuisiner **plusieurs** plats identiques. De même, une image peut lancer **plusieurs** conteneurs identiques.

```
   IMAGE (figée)                CONTENEURS (qui tournent)
   nginx:1.27       ───run──▶   conteneur web-1
                    ───run──▶   conteneur web-2
                    ───run──▶   conteneur web-3
```

#### Un conteneur EST un processus

Voici le point que personne ne te dit assez tôt : **un conteneur n'est pas une « petite machine ». C'est un processus** (ou un petit groupe de processus) qui tourne sur ton hôte, mais **isolé** pour qu'il croie être seul. Tu peux d'ailleurs le **voir** dans la liste des processus de la machine hôte (on le fera au Ch. 3).

#### LE point clé : un conteneur n'est PAS une VM

C'est **la** distinction à intégrer, surtout côté sécurité :

| | Machine virtuelle (VM) | Conteneur |
|---|------------------------|-----------|
| Contient | Un OS complet (son propre noyau) | Juste l'appli + ses dépendances |
| Noyau | **Le sien**, isolé | **Celui de l'hôte**, partagé |
| Taille | Gigaoctets | Mégaoctets |
| Démarrage | Dizaines de secondes | Quasi instantané |
| Isolation | **Forte** (noyau séparé) | **Plus légère** (noyau partagé) |

```
   MACHINES VIRTUELLES                CONTENEURS
   ┌─────────┐ ┌─────────┐            ┌─────────┐ ┌─────────┐
   │  App A  │ │  App B  │            │  App A  │ │  App B  │
   │ OS + 🐧 │ │ OS + 🐧 │            │  deps   │ │  deps   │
   │ (noyau) │ │ (noyau) │            └─────────┘ └─────────┘
   └─────────┘ └─────────┘            ┌───────────────────────┐
   ┌───────────────────────┐         │   🐧 NOYAU PARTAGÉ    │
   │     Hyperviseur       │         │   (un seul, l'hôte)   │
   └───────────────────────┘         └───────────────────────┘
   Chaque VM = son noyau              Tous les conteneurs = même noyau
```

> **Le conteneur partage le noyau de la machine hôte.** Il ne transporte pas son propre système d'exploitation complet. C'est ce qui le rend léger et rapide… **et c'est aussi sa principale limite de sécurité.**

### Très utile en pratique

Garde cette grille de lecture, tu t'en serviras tout le cours :

- On **construit** ou on **télécharge** une **image**.
- On **lance** un **conteneur** à partir d'une image.
- Le conteneur est un **processus isolé**, pas une machine.
- Plusieurs conteneurs **partagent le noyau** de l'hôte.

### Application admin / cyber

- **Côté admin :** comprendre qu'un conteneur est « juste » un processus isolé démystifie tout. Pas de magie : des mécanismes Linux que tu connais déjà en partie (processus, droits, réseau).
- **Côté SOC / cyber :** parce que **le noyau est partagé**, la surface d'attaque d'un conteneur **inclut l'hôte**. Une faille du noyau exploitée depuis un conteneur peut, dans le pire des cas, toucher la machine entière et les autres conteneurs.

En sécurité, on parle de **« container escape »** (évasion de conteneur) lorsqu'une compromission **sort du conteneur** pour atteindre l'hôte ou ses voisins. Ce cours **n'enseigne pas** ces techniques (on reste défensif), mais tu dois comprendre **pourquoi** les mauvaises configurations (conteneur en root, `--privileged`, montages dangereux) **augmentent** ce risque. Tout l'objectif du durcissement (Partie VIII) sera de rendre une telle évasion la plus difficile possible.

🛡️ **Réflexe sécurité :** « conteneur » ne veut **pas** dire « isolé comme une VM ». Quand tu évalues le risque d'un conteneur compromis, pense toujours : *qu'est-ce qu'il partage avec l'hôte et avec ses voisins ?* C'est **la** question défensive de tout le cours.

### ❌ Erreur classique

> **Traiter un conteneur comme une mini-VM jetable et « forcément sûre ».**

Beaucoup de débutants supposent qu'un conteneur compromis « reste dans sa boîte ». La réalité est plus nuancée : l'isolation est **réelle mais plus fine** qu'une VM. Un conteneur mal configuré (privilégié, en root, avec des montages dangereux) **affaiblit** cette barrière. Le réflexe correct : *un conteneur est isolé par défaut, mais cette isolation se mérite et peut être affaiblie par une mauvaise config*.

### Exercices

**Guidé :** Avec tes propres mots, écris la différence entre une **image** et un **conteneur** en **une seule phrase** qui contient les mots « recette » et « plat ». Puis fais la même chose pour **VM vs conteneur** avec le mot « noyau ». Ces deux phrases sont ton ancrage pour tout le cours.

**Autonome :** Dessine (à la main, c'est très bien) deux schémas : à gauche, trois VM ; à droite, trois conteneurs. Fais clairement apparaître **où se trouve le noyau** dans chaque cas. Tu dois « voir » pourquoi le conteneur est plus léger.

**Défi :** Rédige **3 différences concrètes** entre VM et conteneur, et pour chacune une **conséquence de sécurité**. Exemple de départ : « Le conteneur partage le noyau de l'hôte → une faille noyau peut permettre une évasion vers l'hôte. » C'est exactement le type de raisonnement attendu d'un profil cyber.

### ✅ Tu sais maintenant…

- La différence **image** (modèle figé) vs **conteneur** (instance qui tourne).
- Qu'un conteneur **est un processus isolé**, pas une machine.
- La distinction fondamentale **conteneur vs VM** : le **noyau partagé**.
- Pourquoi le noyau partagé rend le conteneur **léger** mais étend sa **surface d'attaque** à l'hôte.
- La notion défensive de **container escape** et le réflexe « qu'est-ce qui est partagé avec l'hôte ? ».

---

## Chapitre 3 — Sous le capot : namespaces et cgroups (en clair)

### Le minimum à savoir

#### Pourquoi ouvrir le capot ?

Au Ch. 2, on a dit qu'un conteneur est « un processus isolé ». Mais **isolé comment ?** Comprendre ça, ce n'est pas de la curiosité : c'est ce qui te permettra plus tard de comprendre **pourquoi** `--privileged` est dangereux, ou **pourquoi** un conteneur sans limites peut faire tomber une machine. Deux mécanismes du noyau Linux font tout le travail : les **namespaces** et les **cgroups**.

> Attention au piège de vocabulaire : ces **namespaces Linux** n'ont **rien à voir** avec les *namespaces de Kubernetes* (qui sont une autre notion, vue dans le cours K8s). Même mot, concepts différents.

#### Les namespaces : des cloisons de visibilité

Un **namespace** Linux limite **ce qu'un processus peut voir**. Le noyau peut donner à un conteneur :

- sa propre **vue des processus** (il ne voit pas ceux des autres conteneurs ni de l'hôte) ;
- son propre **système de fichiers** (ses fichiers à lui) ;
- sa propre **vue réseau** (sa configuration, ses interfaces) ;
- son propre **nom d'hôte**, ses propres utilisateurs, etc.

> Image mentale : les namespaces, ce sont les **cloisons** qui font croire au conteneur qu'il est seul dans l'appartement, alors qu'il partage l'immeuble (le noyau) avec d'autres.

#### Les cgroups : des limites de ressources

Un **cgroup** (*control group*) limite **ce qu'un processus peut consommer** : combien de **CPU**, combien de **mémoire**. Sans cgroup, un conteneur pourrait dévorer **toute** la RAM de la machine et faire tomber les voisins.

> Image mentale : si les namespaces sont les cloisons, les cgroups sont les **compteurs** (électricité, eau) qui empêchent un locataire de tout consommer.

#### La grande révélation

> **L'isolation d'un conteneur n'est pas magique. C'est du Linux : des namespaces pour cloisonner la visibilité, des cgroups pour limiter les ressources.** Docker ne fait qu'orchestrer ces mécanismes du noyau pour toi.

Et la conséquence directe, côté sécurité : **affaiblir ces mécanismes affaiblit l'isolation**. C'est exactement ce que font les mauvaises configs qu'on verra en Partie VIII.

### Très utile en pratique

On peut **voir** qu'un conteneur n'est qu'un processus de l'hôte. L'idée de la manip (qu'on rejouera après avoir installé Docker au Ch. 4) :

```bash
# Dans un terminal : lancer un conteneur qui tourne
docker run -d --name demo nginx:1.27

# Depuis l'HÔTE : retrouver le(s) processus du conteneur
ps -ef | grep nginx        # le processus nginx du conteneur apparaît côté hôte !
```

Le processus du conteneur est **bien là, sur l'hôte** — simplement isolé par des namespaces. C'est la preuve concrète que « conteneur = processus isolé », pas « petite machine ».

### Application admin / cyber

- **Côté admin :** savoir que namespaces + cgroups = l'isolation t'aide à **diagnostiquer**. Un conteneur qui « voit trop » ou « consomme trop » est presque toujours un problème de namespace ou de cgroup mal réglé.
- **Côté SOC / cyber :** c'est **la clé** pour comprendre les risques de la Partie VIII :
  - 🛡️ **`--privileged`** **casse des cloisons** (namespaces) et redonne au conteneur un accès large à l'hôte.
  - 🛡️ **Absence de cgroup / de limites** = pas de garde-fou de ressources = un conteneur (ou un attaquant qui le contrôle) peut provoquer un **déni de service** sur la machine.

🔍 **Réflexe diagnostic :** quand un conteneur a un comportement « trop puissant » (il voit l'hôte, accède à des périphériques, consomme sans limite), pose-toi la question : *quelles cloisons ont été abaissées ?* La réponse est presque toujours dans les options de lancement.

### ❌ Erreur classique

> **Penser que « le conteneur est isolé » est une garantie binaire, vraie ou fausse.**

L'isolation est **graduée**. Un conteneur par défaut est raisonnablement cloisonné. Mais chaque option qui « ouvre » quelque chose (`--privileged`, montage de chemins hôte, partage de namespaces) **réduit** l'isolation d'un cran. Le réflexe correct : penser l'isolation comme un **curseur**, pas comme un interrupteur.

### Exercices

**Guidé :** Avec tes mots, complète ces deux phrases : « Les namespaces servent à _______ » et « Les cgroups servent à _______ ». Puis donne, pour chacun, **un exemple de ce qui se passe mal** si on les affaiblit ou les retire. (Indices : voir trop / consommer trop.)

**Autonome :** Reprends l'image de l'immeuble (cloisons = namespaces, compteurs = cgroups). Étends-la : qu'est-ce que représenterait, dans cette analogie, le fait de donner à un locataire **la clé de la chaufferie de l'immeuble** ? Relie ta réponse à l'idée de `--privileged` ou de Docker socket. (C'est un teaser de la Partie VIII.)

**Défi :** Sans encore l'exécuter si tu n'as pas Docker, **écris la séquence de commandes** qui permettrait de prouver qu'un conteneur nginx est visible comme un processus sur l'hôte. Explique en une phrase **pourquoi** c'est possible (indice : noyau partagé + namespaces). Tu rejoueras cette manip pour de vrai après le Ch. 4.

### ✅ Tu sais maintenant…

- Que l'isolation d'un conteneur repose sur deux mécanismes du **noyau Linux** : **namespaces** et **cgroups**.
- Que les **namespaces** cloisonnent la **visibilité** (processus, fichiers, réseau…).
- Que les **cgroups** limitent les **ressources** (CPU, RAM).
- Que ces **namespaces Linux** ≠ les **namespaces Kubernetes** (piège de vocabulaire).
- Que l'isolation est **graduée** : l'affaiblir (privilèges, montages) augmente la surface d'attaque.
- Pourquoi un conteneur est **visible comme un processus** sur l'hôte.

---

### 🚩 Checkpoint — Fin de la Partie I

C'est le moment de vérifier tes **fondations**. Avant de mettre les mains dans Docker, tu dois pouvoir :

- [ ] Expliquer en une phrase **pourquoi la conteneurisation existe** (enfer des dépendances, « ça marche sur ma machine »).
- [ ] Énoncer le modèle mental **isolation / reproductibilité / jetabilité** avec tes propres mots.
- [ ] Expliquer la différence **image vs conteneur** (recette vs plat).
- [ ] Expliquer pourquoi **un conteneur est un processus isolé**, pas une machine.
- [ ] Expliquer pourquoi **un conteneur n'est pas une VM** (noyau partagé) et la **conséquence de sécurité** (container escape).
- [ ] Dire à quoi servent les **namespaces** (cloisonner la visibilité) et les **cgroups** (limiter les ressources).
- [ ] Comprendre que l'isolation est **graduée** et qu'une mauvaise config peut l'affaiblir.

> **Si tu coches tout, tu as le socle mental.** La Partie II va te faire **installer Docker** et **lancer tes premiers conteneurs** — enfin de la pratique. On commencera par comprendre *qui parle à qui* (CLI, daemon, socket), parce que c'est là que se cache le premier grand réflexe de sécurité Docker : **le daemon tourne en root**.

---
---
---

## PARTIE II — PREMIERS PAS AVEC DOCKER

> Enfin de la pratique. On installe Docker, on comprend **qui parle à qui**, puis on lance, observe et arrête nos premiers conteneurs. Garde le cycle en tête : `image → conteneur → diagnostic → suppression/recréation`.

---

## Chapitre 4 — Installer Docker et comprendre son architecture

### Le minimum à savoir

#### Docker n'est pas « un programme », c'est trois choses

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

#### Pourquoi cette distinction est cruciale (et pas que théorique)

Parce qu'elle explique **le premier grand réflexe de sécurité Docker** :

> Le **daemon tourne en root**. La CLI ne fait que lui passer des ordres. Donc **quiconque peut parler au daemon peut faire faire à root à peu près n'importe quoi sur la machine** — par exemple monter le disque entier de l'hôte dans un conteneur et le lire.

C'est aussi pour ça qu'on dit qu'**appartenir au groupe `docker` équivaut à avoir root** sur la machine : être dans ce groupe, c'est avoir le droit de parler au daemon. Ce n'est pas un détail d'administration, c'est une **décision de sécurité**.

> **Rappel du préambule :** Docker peut tourner en mode **rootless** pour atténuer ce point. On reste ici sur le mode classique (le plus répandu), en gardant cette nuance en tête.

#### Ce dont tu as besoin

Deux choses : le **daemon** qui tourne, et la **CLI** pour lui parler. Sur Linux avec Docker Engine, les deux s'installent ensemble. Sur Docker Desktop, l'application gère le daemon (dans une VM cachée) et te fournit la CLI.

### Très utile en pratique

#### Installer (vue d'ensemble)

> Comme pour tout outil, **les commandes d'installation vieillissent vite**. La **documentation officielle Docker fait foi** — suis-la pour ton système plutôt qu'un copier-coller daté. L'idée générale sur Linux : ajouter le dépôt officiel Docker, puis installer le paquet `docker-ce` (Docker Community Edition).

Après installation, **trois commandes** te confirment que tout est en place :

```bash
docker version      # versions du Client (CLI) ET du Server (daemon) : les deux doivent répondre
docker info         # vue d'ensemble : nb de conteneurs, images, driver de stockage, etc.
docker run hello-world   # le "tour complet" : pull d'une image + lancement d'un conteneur
```

#### Lire `docker version` (et ce qu'il révèle)

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

#### Le premier conteneur : `hello-world`

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

### Application admin / cyber

- **Côté admin :** `docker info` est ta **fiche d'identité** de l'installation : version, nombre de conteneurs/images, **driver de stockage**, dossier de données. C'est le premier endroit où regarder pour comprendre une machine Docker que tu découvres.
- **Côté SOC / cyber :** la séparation CLI/daemon/socket **est** le modèle de menace de Docker. Retiens trois choses :
  - 🛡️ Le **daemon = root**. Le compromettre ou détourner le socket, c'est compromettre l'hôte.
  - 🛡️ Le **groupe `docker` = root de fait**. Qui tu ajoutes à ce groupe est une **décision de sécurité**, pas de confort.
  - 🛡️ Le **socket `/var/run/docker.sock`** est l'objet le plus sensible de tout l'écosystème. On verra au Ch. 17 pourquoi le **monter dans un conteneur** est l'une des pires erreurs possibles.

🔍 **Réflexe diagnostic :** devant une machine Docker inconnue, commence par `docker version` (le daemon répond-il ?) et `docker info` (qu'y a-t-il dessus ?). Ces deux commandes te disent l'essentiel avant même de lister quoi que ce soit.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Installe Docker pour ton système (en suivant la doc officielle), puis lance la séquence `docker version`, `docker info`, `docker run hello-world`. Tu dois voir **les deux blocs** Client/Server répondre, puis le message « Hello from Docker! ». Si tu tombes sur « cannot connect to the Docker daemon », relie l'erreur aux deux causes ci-dessus et note la commande qui a résolu le problème.

**Autonome :** Lance `docker info` et repère **trois informations** : le nombre de conteneurs, le nombre d'images, et le **dossier racine de Docker** (*Docker Root Dir*). Écris en une phrase pourquoi un analyste qui découvre une machine voudrait connaître ces trois éléments.

**Défi :** Explique, avec tes propres mots et en 4-5 lignes, **pourquoi `sudo docker run -v /:/hôte ...` est si dangereux**. Indice : relie le fait que **le daemon tourne en root** au fait qu'on lui demande de **monter la racine de l'hôte** dans un conteneur. Tu n'as pas besoin de l'exécuter — c'est un exercice de **modèle de menace**, à rapprocher du Ch. 17.

### ✅ Tu sais maintenant…

- Que Docker = **CLI** (le client) + **daemon `dockerd`** (le moteur, en root) + **API/socket** (le canal).
- Que l'ensemble s'appelle le **Docker Engine**.
- Vérifier une installation avec `docker version`, `docker info`, `docker run hello-world`.
- Lire les deux blocs **Client/Server** et diagnostiquer « cannot connect to the daemon ».
- Que **le daemon tourne en root** et que le **groupe `docker` ≈ root** : un point de sécurité fondateur.
- Que le **socket Docker** est l'objet le plus sensible de l'écosystème (suite au Ch. 17).

---

## Chapitre 5 — `docker run` : lancer son premier conteneur

### Le minimum à savoir

#### La commande centrale, décortiquée

`docker run` est la commande que tu taperas le plus. Elle fait **deux choses d'un coup** : elle **crée** un conteneur à partir d'une image, puis elle le **démarre**. Voici son anatomie :

```
docker run [options]   IMAGE        [commande]
           ▲           ▲            ▲
           comment     à partir de  quoi exécuter dans
           le lancer   quelle image le conteneur (optionnel)
```

Exemple minimal :

```bash
docker run nginx        # lance un conteneur à partir de l'image nginx
```

Si l'image `nginx` n'est pas en local, Docker la **télécharge** d'abord (comme pour `hello-world`), puis lance le conteneur.

#### Les options que tu utiliseras tout le temps

| Option | Rôle | Sans elle… |
|--------|------|------------|
| `-d` (*detached*) | Lance en **arrière-plan**, te rend la main | Le terminal reste « bloqué » par le conteneur |
| `-it` | Mode **interactif** + terminal (pour entrer dans le conteneur) | Pas de shell interactif |
| `--name <nom>` | Donne un **nom** lisible au conteneur | Docker en génère un aléatoire (ex. `nostalgic_tesla`) |
| `--rm` | **Supprime** le conteneur dès qu'il s'arrête | Le conteneur arrêté traîne dans `docker ps -a` |
| `-p <hôte>:<conteneur>` | **Publie** un port (vu au Ch. 13) | Le service n'est pas joignable depuis l'hôte |

#### Deux façons de lancer, deux usages

**Détaché (`-d`) — pour un service qui tourne en fond :**

```bash
docker run -d --name web nginx
# Docker affiche un long identifiant et te rend la main.
```

**Interactif (`-it`) — pour entrer dans un conteneur et explorer :**

```bash
docker run -it --name labo ubuntu bash
# Tu te retrouves DANS un shell Ubuntu, isolé.
root@a1b2c3:/#  ls
root@a1b2c3:/#  exit      # quitter le shell → le conteneur s'arrête
```

> Le mode interactif est parfait pour **comprendre** : tu es « dans » le conteneur, tu vois son système de fichiers, tu constates qu'il est isolé. Quand tu fais `exit`, le processus principal (`bash`) se termine… et **le conteneur s'arrête avec lui**. Cette dernière phrase est la clé du chapitre suivant.

### Très utile en pratique

```bash
# Un serveur web en arrière-plan, nommé, avec un port publié
docker run -d --name web -p 8080:80 nginx
# → ouvre http://localhost:8080 dans un navigateur : la page nginx s'affiche

# Un conteneur jetable pour tester une commande, supprimé automatiquement
docker run --rm -it alpine sh
/ # echo "je teste, puis je disparais"
/ # exit        # grâce à --rm, le conteneur ne laisse aucune trace
```

`--rm` est ton meilleur ami en lab : il évite l'accumulation de conteneurs arrêtés. Pour un **service** que tu veux garder, ne le mets pas ; pour un **test jetable**, mets-le.

### Application admin / cyber

- **Côté admin :** `docker run` remplace tout un rituel (installer, configurer, démarrer un service) par **une ligne reproductible**. Lancer ≠ installer : tu ne « salis » pas la machine hôte, tout vit dans le conteneur.
- **Côté SOC / cyber :** chaque option de `run` est une **décision de surface d'attaque**. Quelques réflexes posés ici, détaillés plus loin :
  - 🛡️ `-p 8080:80` **publie un port** : ce qui était interne devient **joignable**. À ne faire qu'en conscience (Ch. 13).
  - 🛡️ `-v` / `--mount` **monte des chemins de l'hôte** : puissant et risqué (Ch. 12).
  - 🛡️ `--privileged`, `--user`, `--network host` : changent radicalement l'isolation (Ch. 17).

🔍 **Réflexe diagnostic :** quand un conteneur « ne se comporte pas comme prévu », la cause est souvent **dans les options de `run`** (mauvais port publié, image inattendue, commande surchargée). Relis la ligne `run` avant d'aller chercher plus loin.

### ❌ Erreur classique

> **Oublier `-d` et croire que « le terminal a planté ».**

Quand tu lances `docker run nginx` **sans** `-d`, le conteneur tourne au **premier plan** : ton terminal affiche les logs de nginx et **ne te rend pas la main**. Beaucoup de débutants pensent que c'est figé et ferment tout. En réalité, le conteneur **fonctionne**. Deux réflexes : soit lancer en arrière-plan avec `-d`, soit ouvrir un **second terminal** pour observer. (Et `Ctrl+C` arrête le conteneur au premier plan.)

### Exercices

**Guidé :** Lance `docker run -d --name web -p 8080:80 nginx`, puis ouvre `http://localhost:8080`. Tu dois voir la page d'accueil de nginx. Tu viens de publier un service conteneurisé et d'y accéder depuis l'hôte. Laisse-le tourner, on s'en sert au chapitre suivant.

**Autonome :** Lance un conteneur **interactif** Ubuntu (`docker run -it --name labo ubuntu bash`). Une fois dedans, crée un fichier (`touch /tmp/test`), liste-le, puis `exit`. Relance ensuite `docker run -it ubuntu bash` (nouveau conteneur) et vérifie que `/tmp/test` **n'existe pas**. Explique en une phrase ce que ça démontre sur la **jetabilité** et l'**isolation**.

**Défi :** Trouve la différence concrète entre ces deux commandes en les lançant : `docker run --rm alpine echo coucou` et `docker run alpine echo coucou`. Puis fais `docker ps -a`. Combien de conteneurs `alpine` arrêtés vois-tu, et **pourquoi** ? Tu viens d'observer l'effet de `--rm` — un réflexe d'hygiène essentiel.

### ✅ Tu sais maintenant…

- Que `docker run` **crée puis démarre** un conteneur à partir d'une image.
- L'anatomie `docker run [options] IMAGE [commande]`.
- Les options clés : `-d`, `-it`, `--name`, `--rm`, `-p`.
- La différence entre lancer en **arrière-plan** (service) et en **interactif** (exploration).
- Que quitter le processus principal **arrête le conteneur** (clé du Ch. 6).
- Que chaque option de `run` est une **décision de surface d'attaque**.

---

## Chapitre 6 — Le cycle de vie d'un conteneur

### Le minimum à savoir

#### Un conteneur a des états, comme un processus

Un conteneur n'est pas « allumé ou éteint ». Il traverse une **suite d'états** qu'il faut savoir lire, car c'est la base de tout diagnostic :

```
   docker run
       │
       ▼
   [Created] ──start──▶ [Running] ──stop──▶ [Exited/Stopped]
                            │                      │
                         (le process               └──start──▶ [Running]
                          principal                │
                          se termine)              └──rm──▶ [Supprimé] (n'existe plus)
                            │
                            ▼
                        [Exited]
```

- **Created** : le conteneur existe mais n'a pas démarré (rare en pratique, créé sans lancer).
- **Running** : il tourne, son processus principal est actif.
- **Exited / Stopped** : il s'est arrêté — soit parce qu'on l'a stoppé, soit parce que **son processus principal s'est terminé**.
- **Supprimé** : retiré de la machine (`rm`). Il n'apparaît plus nulle part.

#### LE point qui déroute tous les débutants

> **Un conteneur vit tant que son processus principal vit.** Quand ce processus se termine, le conteneur passe en **Exited**. Ce n'est **pas** une panne : c'est le comportement normal.

C'est pour ça que `docker run hello-world` « disparaît » : son unique tâche (afficher un message) finit, donc le conteneur finit. Et c'est pour ça qu'un `docker run -it ubuntu bash` s'arrête quand tu fais `exit` : tu as terminé le processus `bash`.

#### Voir les conteneurs : `ps` et `ps -a`

```bash
docker ps        # conteneurs EN COURS (Running) uniquement
docker ps -a     # TOUS les conteneurs, y compris les Exited
```

> **Piège classique :** `docker ps` ne montre **pas** les conteneurs arrêtés. Si « ton conteneur a disparu », il est probablement juste **Exited** — `docker ps -a` le retrouve.

### Très utile en pratique

```bash
docker ps -a                    # voir l'état de tous les conteneurs

docker stop web                 # arrêt propre (laisse le temps au process de finir)
docker start web                # redémarre un conteneur arrêté (il garde son nom et sa config)
docker restart web              # stop + start enchaînés

docker rm web                   # supprime un conteneur ARRÊTÉ
docker rm -f web                # ☠️ force la suppression même s'il TOURNE (pas de confirmation)
```

Lire la sortie de `docker ps -a` :

```text
CONTAINER ID   IMAGE     COMMAND                  STATUS                     NAMES
a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   Up 3 minutes               web
f6e5d4c3b2a1   ubuntu    "bash"                   Exited (0) 2 minutes ago   labo
```

La colonne **STATUS** est ta boussole : `Up …` = Running, `Exited (0) …` = arrêté proprement (code 0 = succès), `Exited (1) …` ou un autre code = arrêté sur **erreur** (un indice de diagnostic, qu'on exploitera au Ch. 7).

### Application admin / cyber

- **Côté admin :** la distinction `stop` (arrêt propre) / `rm` (suppression) / `rm -f` (suppression forcée) est exactement parallèle à ce que tu connais avec les services et processus Linux. `stop` envoie un signal d'arrêt poli ; au-delà d'un délai, le conteneur est arrêté plus fermement.
- **Côté SOC / cyber :** savoir lister **tous** les conteneurs (`-a`), y compris arrêtés, est un **réflexe d'investigation**. Un conteneur **Exited** peut être la trace d'une activité passée (un outil lancé puis arrêté). Le **code de sortie** (`Exited (N)`) et l'**ancienneté** racontent une histoire.

🔍 **Réflexe diagnostic :** un conteneur « qui ne marche pas » est presque toujours dans un de ces deux cas : soit il est **Exited** (et le code de sortie + les logs disent pourquoi — Ch. 7), soit il **redémarre en boucle** (mauvaise config). `docker ps -a` est **toujours** ta première commande.

### ❌ Erreur classique

> **Croire qu'un conteneur Exited est « cassé », alors qu'il a simplement fini son travail.**

Le cas le plus fréquent : on lance une image qui exécute une tâche courte (un script, une commande) et on s'étonne qu'« elle ne reste pas allumée ». Mais un conteneur **n'a pas vocation à rester en vie sans raison** : si son processus principal se termine avec succès (`Exited (0)`), tout va bien. Le réflexe correct : lire le **STATUS** et le **code de sortie** avant de parler de panne. Un `Exited (0)` n'est pas un problème ; un `Exited (1)` mérite un coup d'œil aux logs.

### Exercices

**Guidé :** Reprends ton conteneur `web` (nginx) du Ch. 5. Lance `docker ps` (il apparaît), puis `docker stop web` et `docker ps` (il a disparu de la liste). Maintenant `docker ps -a` : il est là, en **Exited**. Fais `docker start web`, vérifie qu'il est de nouveau **Up**. Tu viens de parcourir le cycle Running → Stopped → Running.

**Autonome :** Lance `docker run --name court alpine echo "fini"`. Observe qu'il s'arrête immédiatement. Avec `docker ps -a`, lis son **STATUS** : quel code de sortie ? Que signifie-t-il ? Puis nettoie avec `docker rm court`. Écris en une phrase pourquoi ce conteneur « ne reste pas allumé ».

**Défi :** Crée volontairement un conteneur qui s'arrête sur **erreur** : `docker run --name casse alpine sh -c "exit 3"`. Lis son STATUS avec `docker ps -a` : tu dois voir `Exited (3)`. Explique en quoi ce **code de sortie non nul** est un **indice de diagnostic** précieux, et fais le lien avec ce qu'on va apprendre au chapitre suivant (logs, inspect). Nettoie ensuite avec `docker rm casse`.

### ✅ Tu sais maintenant…

- Les états d'un conteneur : **Created → Running → Exited → (Supprimé)**.
- Que **le conteneur vit tant que son processus principal vit** (et qu'un arrêt n'est pas forcément une panne).
- La différence cruciale entre `docker ps` (Running) et `docker ps -a` (**tous**).
- Les commandes du cycle de vie : `stop`, `start`, `restart`, `rm`, `rm -f`.
- Lire la colonne **STATUS** et le **code de sortie** comme premiers indices de diagnostic.
- Que lister **tous** les conteneurs est un réflexe d'investigation côté SOC.

---

### 🚩 Checkpoint — Fin de la Partie II

Tu as maintenant **les mains dans Docker**. Avant de passer au diagnostic approfondi, tu dois pouvoir :

- [ ] Expliquer l'architecture **CLI → daemon → conteneurs** et le rôle du **socket**.
- [ ] Dire pourquoi **le daemon = root** et **le groupe `docker` ≈ root**.
- [ ] Vérifier une installation (`docker version`, `docker info`, `hello-world`) et diagnostiquer « cannot connect to the daemon ».
- [ ] Lancer un conteneur en **arrière-plan** (`-d`) et en **interactif** (`-it`), le **nommer**, **publier un port**, utiliser `--rm`.
- [ ] Lire les états d'un conteneur et la colonne **STATUS** (`docker ps` vs `docker ps -a`).
- [ ] Utiliser `stop`, `start`, `restart`, `rm`, et savoir que `rm -f` ne demande **aucune confirmation**.
- [ ] Comprendre qu'un conteneur **Exited (0)** n'est pas une panne.

> **🧩 Mini-projet — « Lancer, observer, nettoyer ».**
> 1. Lance **trois** conteneurs : un nginx nommé `web` en arrière-plan avec port publié, un `alpine` interactif que tu explores puis quittes, et un conteneur jetable avec `--rm`.
> 2. Avec `docker ps -a`, dresse l'inventaire : lesquels sont **Up**, lesquels **Exited**, lequel a **disparu** (et pourquoi).
> 3. Arrête proprement `web`, puis **nettoie** tout ce qui traîne (`stop` puis `rm`), en faisant **systématiquement un `docker ps -a` avant chaque `rm`** pour vérifier ce que tu supprimes.
> Objectif : intégrer le cycle complet **lancer → observer → arrêter → nettoyer**, avec le bon réflexe « regarder avant de supprimer ».

> **La suite :** en Partie III, on installe les **réflexes de diagnostic** — `logs`, `exec`, `inspect`, `stats`, `cp`, `events` — pour ne plus jamais être bloqué devant un conteneur qui « ne marche pas ». C'est ce qui te rend vraiment **autonome**.

---
