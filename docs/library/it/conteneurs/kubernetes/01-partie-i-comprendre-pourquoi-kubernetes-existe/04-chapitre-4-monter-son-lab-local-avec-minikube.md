---
title: Chapitre 4 — Monter son lab local avec Minikube
source: IT/08 Conteneurs & automatisation/Conteneurs/Kubernetes.md
note: Kubernetes
up:
- - Kubernetes
  - ../index.md
- - PARTIE I — Comprendre pourquoi Kubernetes existe
  - index.md
---

## Le minimum à savoir

### Pourquoi un lab local (et pas le cloud) ?

Pour apprendre, tu as besoin d'un cluster que tu peux **casser, recréer et explorer sans risque ni facture**. Un cluster cloud (EKS, GKE, AKS) coûte de l'argent, ajoute de la complexité d'accès, et te détourne de l'essentiel. **On reste en local.**

> 🧪 **Lunette LAB :** ton cluster local sera **mono-machine** (un seul node qui joue à la fois le control plane et le worker). En production, ces rôles sont sur des machines séparées et redondées. Le lab **simplifie volontairement** — c'est parfait pour apprendre, dangereux à confondre avec la prod.

> **Note pour les curieux :** Minikube est utilisé ici en **mono-node** pour la pédagogie. Il peut aussi simuler certains scénarios plus avancés (multi-node, par exemple), mais **le cours se limite volontairement au mono-node** pour ne pas mélanger *apprentissage de Kubernetes* et *complexité d'infrastructure*.

### Le choix de ce cours : Minikube

Il existe plusieurs outils pour un cluster local. **Ce cours utilise Minikube par défaut**, pour des raisons pédagogiques :

- **Mono-node simple** : un cluster « qui ressemble à un vrai » sans complexité multi-machines.
- **Commandes claires** (`minikube start`, `minikube status`, `minikube stop`).
- **Add-ons pratiques** : activer un Ingress, un dashboard, etc. en une commande (utile aux Ch. 18 et suivants).
- **Bon pour visualiser** : un tableau de bord graphique disponible si besoin.

> **Tous les exercices, manifests et commandes de ce cours sont testables avec Minikube par défaut.**

### 🧰 Encadré — Les alternatives (Kind, k3d)

Tu peux réussir le cours avec une autre solution, mais **les commandes d'environnement** (démarrage, Ingress, accès aux Services) **diffèrent**. Si tu choisis une alternative, c'est à toi d'adapter ces parties-là (le cœur Kubernetes, lui, est identique).

| Outil | Idée | Pour qui |
|-------|------|----------|
| **Minikube** | Un mini-cluster (souvent dans une VM ou un conteneur) | **Débutants — recommandé ici** |
| **Kind** | Kubernetes *in Docker* : les nodes sont des conteneurs Docker | Tester/CI, dev de Kubernetes lui-même |
| **k3d** | k3s (Kubernetes allégé) dans Docker | Clusters très légers, multi-node faciles |

> Tu **n'as pas** à les installer tous. Choisis **Minikube**, et garde les autres en tête comme alternatives.

### Le driver : comment Minikube fait tourner le cluster

Minikube a besoin d'un **driver** pour héberger le cluster (Minikube peut tourner via VM, conteneur ou bare-metal). Sur **Linux**, les deux choix les plus confortables sont :

- **`docker`** : simple si Docker est déjà installé, sans hyperviseur à gérer ni virtualisation à activer. Le cluster tourne dans un conteneur.
- **`kvm2`** : très propre si tu veux un **vrai backend VM Linux** dédié, sans dépendre de Docker.

D'autres drivers existent selon l'OS (`virtualbox`, `hyperkit`, `qemu`, `podman`…). Pour ce cours, on **privilégie `docker` pour la simplicité**, mais **`kvm2` est une excellente alternative sur Linux**.

## Très utile en pratique

### Installation (vue d'ensemble)

> Les commandes exactes dépendent de ton OS et évoluent. **Les commandes d'installation sont la partie de ce cours la plus susceptible de vieillir.** En cas de doute, la **documentation officielle Kubernetes/Minikube fait foi** — suis-la plutôt qu'un copier-coller daté. Tu as besoin de **deux** outils : `minikube` (le lab) et `kubectl` (pour parler au cluster).

Sur **Linux (x86-64)**, l'installation ressemble à ceci :

```bash
# Minikube (commande officielle actuelle, depuis GitHub)
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

# kubectl (vérifie la version stable courante sur la doc officielle)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```


> **Note de compatibilité `kubectl` ↔ cluster :** `kubectl` doit rester proche de la version du cluster — en pratique, **à plus ou moins une version mineure** du control plane. Avec Minikube en lab, la dernière version stable de `kubectl` fonctionne généralement très bien. Cette règle devient importante en **entreprise**, où le cluster peut être plus ancien que ton poste.

### Démarrer, vérifier, arrêter

```bash
minikube start                 # démarre le cluster (la première fois est la plus longue)
minikube status                # état du cluster et de ses composants
kubectl version                # versions du client kubectl et du serveur (le cluster)
kubectl cluster-info           # adresse de l'API server : la preuve que kubectl parle à une API
kubectl get nodes              # ton (unique) node doit apparaître en "Ready"
minikube stop                  # arrête le cluster sans le détruire
minikube delete                # ☠️ détruit complètement le cluster (on repart de zéro)
```


`kubectl cluster-info` est précieux pour un débutant : il affiche **l'adresse de l'API server**. C'est la confirmation visuelle que `kubectl` ne « fait pas de magie » — il **parle à une API** sur le réseau (on détaillera ce rôle central de l'API en Partie II).

> 🧰 **Solution de secours — `kubectl` pas encore installé ?** Minikube embarque sa propre version de `kubectl`, utilisable via :
> ```bash
> minikube kubectl -- get nodes
> ```
> Dans ce cours, on installe quand même `kubectl` **directement**, car c'est le **réflexe professionnel** (et c'est la commande que tu utiliseras partout ailleurs).

Choisir explicitement un driver :

```bash
minikube start --driver=docker        # si tu as Docker
minikube start --driver=virtualbox    # si tu préfères une VM
```


### À quoi ressemble un démarrage réussi

```text
$ minikube start
😄  minikube v1.x.x on Ubuntu 22.04
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes ...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster
```


```text
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   45s   v1.x.x
```


> Vois ce **`Ready`** ? C'est ton premier signe de vie. Le node est prêt à accueillir des applis. On les déploiera en Partie III.

## Application admin / cyber

- **Côté admin :** `minikube start` te donne, en une commande, ce qui prendrait des heures à monter à la main (control plane configuré, réseau interne, stockage de base). C'est **le** terrain d'entraînement.
- **Côté SOC / cyber :** un lab local est aussi le bon endroit pour **rejouer des mauvaises configurations en sécurité**. Tout au long du cours, tu vas **créer volontairement** des situations risquées (Secret en clair, droits trop larges) pour apprendre à les **repérer et corriger** — chose impensable sur un vrai cluster de production.

🛡️ **Réflexe sécurité :** quand `kubectl version` ou `kubectl get nodes` répond, c'est que **ton kubectl est connecté à un cluster**. Cette connexion repose sur le fichier **kubeconfig** (souvent `~/.kube/config`). Retiens dès maintenant : **ce fichier contient des identifiants d'accès au cluster**. On le traitera comme une clé sensible au Ch. 8.

## ❌ Erreur classique

> **Lancer `minikube start` sans ressources suffisantes — puis croire que « Kubernetes est cassé ».**

Si la RAM ou le CPU manquent, le démarrage échoue ou le node reste `NotReady`, et le débutant accuse Kubernetes. Le réflexe correct : vérifier les **prérequis matériel** (section du préambule), lire le **message d'erreur** de `minikube start` (il est souvent explicite), et au besoin allouer plus de ressources :

```bash
minikube start --cpus=2 --memory=2200      # ajuste selon ta machine
```


Autres pièges fréquents : oublier d'installer **kubectl** (tu as le lab mais pas l'outil pour lui parler), ou être sous **WSL** sans Docker Desktop correctement configuré (voir « Limites de WSL » du préambule).

## Exercices

**Guidé :** Installe `minikube` et `kubectl` pour ton système, puis lance la séquence : `minikube start`, `minikube status`, `kubectl get nodes`. Tu dois voir **un node `Ready`**. Si ça échoue, **lis le message d'erreur** et relie-le aux prérequis (RAM, CPU, driver, Docker). Note la commande qui a fini par marcher.

**Autonome :** Démarre le cluster, puis `minikube stop`, puis `minikube start` à nouveau. Observe que **redémarrer** est plus rapide que **créer**. Ensuite, sans paniquer, fais `minikube delete` puis `minikube start` : tu viens de **détruire et recréer** ton lab. Cette aisance à repartir de zéro est exactement ce qui rend un lab **rassurant**.

**Défi :** Trouve **où se trouve ton fichier kubeconfig** sur ta machine (indice : `~/.kube/config` est l'emplacement par défaut) et **ouvre-le** pour l'observer (sans le modifier). Repère qu'il contient l'**adresse du cluster** et des **données d'authentification**. Ne le partage jamais. Tu viens de voir, en vrai, le fichier qui te donne les **clés du cluster** — on en reparlera sérieusement au Ch. 8.

## ✅ Tu sais maintenant…

- **Pourquoi** un lab local plutôt que le cloud pour apprendre (gratuit, jetable, sans risque).
- Pourquoi ce cours choisit **Minikube** comme environnement principal, et l'existence de **Kind/k3d** comme alternatives.
- Ce qu'est un **driver** Minikube (`docker` vs VM) et comment en choisir un.
- Démarrer, vérifier et arrêter ton cluster : `minikube start/status/stop/delete`, `kubectl get nodes`.
- Reconnaître un node **`Ready`** comme premier signe de vie.
- Que la connexion au cluster repose sur le **kubeconfig**, un fichier **sensible** à protéger.

---

## 🚩 Checkpoint — Fin de la Partie I

C'est le moment de vérifier tes **fondations**. Avant de passer à l'anatomie du cluster, tu dois pouvoir :

- [ ] Expliquer en une phrase **pourquoi Kubernetes existe** (orchestration, automatisation de corvées d'admin à grande échelle).
- [ ] Citer au moins **4 promesses** de Kubernetes (self-healing, scaling, scheduling, rolling update, rollback, adresses stables).
- [ ] Énoncer le modèle mental **« état désiré → réconciliation → état réel »** avec tes propres mots.
- [ ] Expliquer la différence **image vs conteneur**.
- [ ] Expliquer pourquoi **un conteneur n'est pas une VM** (noyau partagé) et la **conséquence de sécurité** associée.
- [ ] Dire pourquoi **Docker et Kubernetes ne sont pas concurrents**.
- [ ] Avoir un cluster **Minikube qui démarre**, avec un node **`Ready`** confirmé par `kubectl get nodes`.
- [ ] Savoir que le **kubeconfig** contient des identifiants d'accès au cluster.

> **Si tu coches tout, tu as le socle mental ET le terrain de jeu.** La Partie II va te faire **visiter** ce cluster de l'intérieur — sans rien y construire encore — pour que tu saches *qui fait quoi* avant de commander quoi que ce soit. C'est là que `kube-system` et les premiers **namespaces** entrent en scène.

---
