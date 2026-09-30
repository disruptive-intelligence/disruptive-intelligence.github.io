---
title: 'PARTIE III — KUBERNETES : LES FONDAMENTAUX'
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 3
chapters: 7
---

-----


## Chapitre 11 — Pourquoi Kubernetes : quand Docker ne suffit plus

### Le minimum à savoir

#### Les limites de Docker seul

Docker Compose est parfait pour le développement et les petits déploiements. Mais imagine que ton application doit :

- Tourner sur **plusieurs serveurs** (pas un seul)
- **Résister à la panne** d’un serveur (si un serveur tombe, l’application continue)
- **Scaler automatiquement** (ajouter des instances quand il y a plus de trafic, en retirer quand le trafic baisse)
- Se **mettre à jour sans interruption** (rolling update — les utilisateurs ne voient pas la mise à jour)
- **Redémarrer automatiquement** un container qui plante (self-healing)

Docker Compose ne sait pas faire ça. Il gère des containers sur **une seule machine**. Pour gérer des containers sur **plusieurs machines**, il faut un **orchestrateur**. Et l’orchestrateur dominant, c’est **Kubernetes**.

#### Kubernetes en une phrase

Kubernetes (souvent abrégé **K8s** — K + 8 lettres + s) est un système qui **gère automatiquement le déploiement, le scaling et le cycle de vie de containers sur un ensemble de serveurs**.

Tu lui dis “je veux 3 instances de mon application web, toujours disponibles”, et Kubernetes s’assure que c’est le cas : il les répartit sur les serveurs disponibles, les redémarre si elles plantent, en ajoute si tu augmentes le nombre, et les met à jour sans interruption.

#### Le paradigme déclaratif

C’est le concept fondamental de Kubernetes :

- **Impératif** (Docker) : tu dis “lance ce container sur ce serveur avec ces options” — tu décris les **actions**
- **Déclaratif** (Kubernetes) : tu dis “je veux 3 instances de cette application, accessibles sur le port 80” — tu décris l’**état désiré**, et K8s se débrouille pour l’atteindre et le maintenir

```
TOI : "Je veux 3 replicas de mon_app"
         │
         ▼
KUBERNETES : vérifie en permanence
         │
    ┌────┴────┐
    │ 3 pods  │  ← État actuel = état désiré → tout va bien
    │ tournent│
    └─────────┘
         │
    Un pod plante
         │
    ┌────┴────┐
    │ 2 pods  │  ← État actuel ≠ état désiré → K8s relance un pod
    │ tournent│
    └────┬────┘
         │
    K8s crée un nouveau pod
         │
    ┌────┴────┐
    │ 3 pods  │  ← État restauré
    │ tournent│
    └─────────┘
```

> **À retenir pour un entretien :** “Kubernetes fonctionne sur un modèle déclaratif : on décrit l’état désiré dans des fichiers YAML, et Kubernetes travaille en permanence pour atteindre et maintenir cet état. Si un container plante, K8s le relance. Si un serveur tombe, K8s redéploie les containers sur les serveurs restants.”

#### Les options pour utiliser Kubernetes

|Option                         |Complexité |Usage                                            |
|-------------------------------|-----------|-------------------------------------------------|
|**minikube**                   |Très simple|Apprendre et tester sur son laptop               |
|**kind** (Kubernetes in Docker)|Simple     |CI/CD, tests automatisés                         |
|**k3s**                        |Légère     |Edge computing, Raspberry Pi, petits déploiements|
|**EKS** (AWS)                  |Managée    |Production sur AWS                               |
|**AKS** (Azure)                |Managée    |Production sur Azure                             |
|**GKE** (Google Cloud)         |Managée    |Production sur GCP                               |
|**K8s vanilla** (auto-hébergé) |Complexe   |Quand tu veux tout contrôler (rare)              |


> **Pour ce cours :** installe **minikube** pour suivre les exercices. C’est un cluster K8s complet qui tourne sur ton laptop.

```bash
# Installer minikube (Linux)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Démarrer le cluster
minikube start

# Vérifier
kubectl get nodes
```

#### Kubernetes n’est pas toujours la réponse

Kubernetes ajoute une **complexité opérationnelle significative**. Pour une petite application avec peu de trafic et une petite équipe, Docker Compose sur un seul serveur est souvent suffisant et beaucoup plus simple.

Kubernetes se justifie quand tu as besoin de :

- Haute disponibilité (l’application ne doit jamais tomber)
- Scaling automatique (le trafic varie)
- Déploiements sans interruption (rolling updates)
- Multi-services avec des équipes différentes (chacune déploie indépendamment)

> **📋 CONTAINER — Épisode 5 (partie 3)**
> 
> Le CTO de MedFlow veut passer en production. Docker Compose sur un seul serveur n’est pas suffisant : l’application doit être hautement disponible (données de santé), scaler pendant les pics d’utilisation (9h-12h), et se mettre à jour sans interruption. La décision est prise : EKS (Kubernetes managé sur AWS). Sami installe minikube pour prototyper la migration avant de passer sur EKS.

### Très utile en pratique

#### kubectl : l’outil de base

`kubectl` est la commande pour interagir avec un cluster Kubernetes. C’est l’équivalent de `docker` pour Docker.

```bash
# Installer kubectl
# Voir : https://kubernetes.io/docs/tasks/tools/

# Vérifier la connexion au cluster
kubectl cluster-info

# Voir les nœuds du cluster
kubectl get nodes
```

On utilisera `kubectl` en détail au chapitre 14.

#### Kubernetes managé vs auto-hébergé

En entreprise, la quasi-totalité des déploiements Kubernetes sont **managés** (EKS, AKS, GKE). Le cloud provider gère le Control Plane (API Server, etcd, Scheduler…) — tu ne gères que tes applications et la configuration. Héberger et maintenir son propre cluster K8s (vanilla) est complexe et réservé aux équipes avec une forte expertise.

### ✅ Tu sais maintenant…

- Pourquoi Kubernetes existe (les limites de Docker seul)
- Le paradigme déclaratif (état désiré vs état actuel)
- Les options pour utiliser K8s (minikube pour apprendre, managé pour la production)
- Que Kubernetes n’est pas toujours nécessaire (Docker Compose suffit souvent)

-----


## Chapitre 12 — Architecture Kubernetes : les composants du cluster

### Le minimum à savoir

#### Le cluster : la vue d’ensemble

Un cluster Kubernetes est composé de deux types de machines :

- Le **Control Plane** (plan de contrôle) : le “cerveau” qui gère le cluster
- Les **Worker Nodes** (nœuds de travail) : les machines qui font tourner les containers

```
┌─────────────────────────────────────────────────┐
│                CONTROL PLANE                     │
│                                                  │
│  ┌──────────┐ ┌──────┐ ┌───────────┐ ┌────────┐│
│  │API Server│ │ etcd │ │ Scheduler │ │Ctrl Mgr││
│  └──────────┘ └──────┘ └───────────┘ └────────┘│
└─────────────────────┬───────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────┴───┐  ┌──────┴────┐  ┌────┴──────┐
│  Node 1   │  │  Node 2   │  │  Node 3   │
│ ┌───────┐ │  │ ┌───────┐ │  │ ┌───────┐ │
│ │kubelet│ │  │ │kubelet│ │  │ │kubelet│ │
│ │Pod Pod│ │  │ │Pod Pod│ │  │ │Pod    │ │
│ │Pod    │ │  │ │Pod    │ │  │ │Pod Pod│ │
│ └───────┘ │  │ └───────┘ │  │ └───────┘ │
└───────────┘  └───────────┘  └───────────┘
    WORKER NODES
```

#### Les composants du Control Plane

|Composant             |Rôle                                                           |Analogie simple                                         |
|----------------------|---------------------------------------------------------------|--------------------------------------------------------|
|**API Server**        |Le point d’entrée unique — toutes les commandes passent par lui|La réception d’un hôtel : tout le monde passe par là    |
|**etcd**              |La base de données du cluster — stocke tout l’état             |Le registre de l’hôtel : qui est dans quelle chambre    |
|**Scheduler**         |Décide sur quel nœud placer chaque pod                         |Le concierge qui attribue les chambres                  |
|**Controller Manager**|Vérifie que l’état actuel correspond à l’état désiré           |Le responsable qualité qui vérifie que tout est en ordre|


> **Point critique :** tout passe par l’**API Server**. Quand tu tapes `kubectl get pods`, ta commande va à l’API Server. Quand le Scheduler place un pod, il parle à l’API Server. Quand un kubelet signale l’état d’un pod, il parle à l’API Server. **Contrôler l’accès à l’API Server, c’est contrôler le cluster** (voir chapitre 25 sur la sécurité).

> **Point critique :** **etcd** contient l’intégralité de l’état du cluster, y compris les Secrets. Si etcd est compromis, tout le cluster est compromis. En production, etcd doit être chiffré, sauvegardé, et accessible uniquement au Control Plane.

#### Les composants des Worker Nodes

|Composant            |Rôle                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------|
|**kubelet**          |L’agent sur chaque nœud — reçoit les instructions de l’API Server et gère les containers localement|
|**kube-proxy**       |Gère le réseau — route le trafic vers les bons pods                                                |
|**Container runtime**|Exécute les containers (containerd)                                                                |

#### Le flux simplifié

```
1. Tu écris un manifest YAML qui dit "je veux 3 replicas de mon_app"
2. Tu tapes : kubectl apply -f manifest.yaml
3. kubectl envoie le manifest à l'API Server
4. L'API Server stocke l'état désiré dans etcd
5. Le Controller Manager détecte : "l'état désiré dit 3 pods, l'état actuel dit 0"
6. Le Scheduler choisit sur quels nœuds placer les 3 pods
7. Les kubelets des nœuds choisis créent les containers
8. Le Controller Manager vérifie en continu que 3 pods tournent
```

### Très utile en pratique

#### Kubernetes managé : ce que le cloud gère pour toi

Avec EKS, AKS ou GKE, le **Control Plane est géré par le cloud provider**. Tu ne vois pas les machines qui font tourner l’API Server, etcd, le Scheduler. Tu ne les maintiens pas, tu ne les patches pas. Tu ne gères que les Worker Nodes (et même ceux-là peuvent être managés avec des node pools auto-scalés).

C’est un avantage énorme : maintenir un Control Plane K8s est un travail à plein temps. Avec un service managé, tu te concentres sur tes applications.

#### Inspecter le cluster

```bash
# Voir les nœuds
kubectl get nodes

# Voir les composants du Control Plane
kubectl get componentstatuses    # ou kubectl get cs

# Voir tout dans tous les namespaces
kubectl get all --all-namespaces
```

### Bonus

#### La haute disponibilité du Control Plane

En production, le Control Plane doit être en haute disponibilité : **3 nœuds etcd minimum** (consensus par Raft), **API Server répliqué** derrière un load balancer. Les services managés (EKS, AKS, GKE) gèrent ça automatiquement — c’est l’un des avantages principaux.

### ✅ Tu sais maintenant…

- L’architecture Control Plane + Worker Nodes
- Le rôle de chaque composant (API Server, etcd, Scheduler, Controller Manager, kubelet)
- Que tout passe par l’API Server (implications en sécurité)
- Que etcd est la base de données la plus critique du cluster
- La différence entre K8s auto-hébergé et managé

-----


## Chapitre 13 — Les objets Kubernetes essentiels

### Le minimum à savoir

#### Le Pod

Le **Pod** est la plus petite unité déployable dans Kubernetes. Un Pod contient **un ou plusieurs containers** qui partagent le même réseau et le même stockage.

En pratique, un Pod contient presque toujours **un seul container**. Les cas multi-containers (sidecar pattern) sont avancés.

```yaml
# Un Pod simple (on ne déploie presque jamais un Pod seul en production)
apiVersion: v1
kind: Pod
metadata:
  name: mon-pod
spec:
  containers:
  - name: mon-app
    image: nginx:1.25
    ports:
    - containerPort: 80
```

> **Règle :** on ne déploie presque **jamais** un Pod directement. On utilise un **Deployment** qui gère les Pods pour nous (scaling, updates, self-healing). Le Pod seul est utile pour comprendre le concept, pas pour la production.

#### Le Deployment

Le **Deployment** est l’objet qu’on utilise pour déployer une application. Il gère un ensemble de Pods identiques (les **replicas**) et s’assure qu’ils sont toujours au nombre demandé.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3          # Je veux 3 instances de mon application
  selector:
    matchLabels:
      app: web         # Ce Deployment gère les Pods avec le label "app: web"
  template:
    metadata:
      labels:
        app: web       # Les Pods créés auront ce label
    spec:
      containers:
      - name: web
        image: mon_app:1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:            # Ressources minimales demandées
            memory: "128Mi"
            cpu: "100m"
          limits:              # Ressources maximales autorisées
            memory: "256Mi"
            cpu: "500m"
```

Le Deployment crée automatiquement un **ReplicaSet** (qui gère les replicas) qui crée les **Pods**. La chaîne est : Deployment → ReplicaSet → Pods.

> **À retenir pour un entretien :** “Un Deployment gère le cycle de vie d’un groupe de Pods identiques. Si un Pod plante, le Deployment en recrée un. Pour une mise à jour, le Deployment fait un rolling update : il crée les nouveaux Pods un par un et supprime les anciens progressivement, sans interruption de service.”

#### Le Service

Les Pods sont **éphémères** : ils peuvent être recréés avec une adresse IP différente à tout moment (crash, mise à jour, scaling). Le **Service** donne une **adresse stable** à un groupe de Pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web           # Ce Service cible les Pods avec le label "app: web"
  ports:
  - port: 80           # Le port du Service
    targetPort: 8000   # Le port du container dans le Pod
  type: ClusterIP      # Accessible uniquement à l'intérieur du cluster
```

Les types de Service :

|Type            |Accessible depuis                                  |Usage                       |
|----------------|---------------------------------------------------|----------------------------|
|**ClusterIP**   |Intérieur du cluster uniquement                    |Communication entre services|
|**NodePort**    |Extérieur via un port sur chaque nœud (30000-32767)|Tests, petits déploiements  |
|**LoadBalancer**|Extérieur via un load balancer cloud               |Production (EKS, AKS, GKE)  |

Le service discovery fonctionne par **DNS** : dans le cluster, `web-service` résout automatiquement vers les Pods avec le label `app: web`. Comme le réseau Docker nommé, mais à l’échelle du cluster.

#### Le Namespace

Un **Namespace** est un espace logique qui sépare les ressources dans le cluster. C’est comme des dossiers sur ton ordinateur.

```bash
kubectl get namespaces
# NAME              STATUS   AGE
# default           Active   1d
# kube-system       Active   1d    ← les composants internes de K8s
# kube-public       Active   1d
```

```bash
# Créer un namespace
kubectl create namespace staging

# Déployer dans un namespace
kubectl apply -f deployment.yaml -n staging

# Voir les ressources d'un namespace
kubectl get pods -n staging
```

Usages : séparer les environnements (dev, staging, prod), séparer les équipes, appliquer des quotas de ressources par namespace.

> **Point important :** un Namespace n’est **pas** une frontière de sécurité en soi. Sans Network Policies (chapitre 24), les Pods de namespaces différents peuvent communiquer entre eux.

#### ConfigMap et Secret

**ConfigMap** : stocker de la configuration non sensible (URLs, paramètres, fichiers de configuration).

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "db-service"
  LOG_LEVEL: "info"
```

**Secret** : stocker des données sensibles (mots de passe, clés API, certificats).

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  DATABASE_PASSWORD: c2VjcmV0    # ← "secret" encodé en base64
```

> **⚠️ Piège fondamental :** les Secrets Kubernetes sont encodés en **base64**, PAS chiffrés. `echo "c2VjcmV0" | base64 -d` donne “secret” en clair. Toute identité disposant des droits RBAC adéquats (ou tout accès à etcd insuffisamment protégé) peut les lire. En production, il faut chiffrer etcd au repos et/ou utiliser un gestionnaire de secrets externe (HashiCorp Vault, AWS Secrets Manager). On verra ça au chapitre 25.

> **À retenir pour un entretien :** “Les Secrets Kubernetes sont en base64, pas chiffrés. C’est une fausse sécurité. En production, il faut du chiffrement au repos (encryption at rest dans etcd) et idéalement un vault externe.”

### Très utile en pratique

#### Les labels et sélecteurs : le mécanisme de liaison

Les **labels** sont des paires clé-valeur attachées aux objets. Les **sélecteurs** permettent de sélectionner des objets par leurs labels. C’est le mécanisme qui lie un Service à ses Pods, un Deployment à ses Pods, etc.

```yaml
# Le Deployment crée des Pods avec le label app: web
# Le Service sélectionne les Pods avec le label app: web
# → Le Service route le trafic vers les bons Pods
```

Si les labels ne correspondent pas entre le Deployment, les Pods et le Service, rien ne fonctionne. C’est la cause n°1 de troubleshooting en K8s pour les débutants.

#### Utiliser les ConfigMaps et Secrets dans un Pod

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: mon_app:1.0.0
        envFrom:
        - configMapRef:
            name: app-config      # Toutes les clés du ConfigMap deviennent des variables d'env
        - secretRef:
            name: app-secrets     # Toutes les clés du Secret deviennent des variables d'env
```

### ✅ Tu sais maintenant…

- Le Pod (unité de base, rarement utilisé seul)
- Le Deployment (gère les Pods : replicas, rolling updates, self-healing)
- Le Service (donne une adresse stable à un groupe de Pods)
- Le Namespace (séparation logique, pas une frontière de sécurité en soi)
- Les ConfigMaps et Secrets (configuration et données sensibles — Secrets en base64, pas chiffrés !)
- Les labels et sélecteurs (le mécanisme qui lie tout ensemble)

### 💬 Questions d’entretien typiques

- **Pourquoi un Service est-il nécessaire si les Pods existent déjà ?** → Les Pods sont éphémères et changent d’adresse IP à chaque recréation. Le Service fournit une adresse stable et un nom DNS qui pointe toujours vers les bons Pods, via le mécanisme de labels/sélecteurs.
- **Quelle est la différence entre un Deployment et un Pod ?** → On ne déploie pas de Pods seuls en production. Un Deployment gère un groupe de Pods identiques : il assure le nombre de replicas demandé, redémarre les Pods qui plantent, et gère les mises à jour sans interruption (rolling update).
- **Les Secrets Kubernetes sont-ils sécurisés ?** → Non par défaut. Ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC appropriés peut les lire. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe.

-----


## Chapitre 14 — Déployer sur Kubernetes : kubectl et les manifests

### Le minimum à savoir

#### Les commandes kubectl essentielles

```bash
# --- LECTURE ---
kubectl get pods                     # Lister les Pods
kubectl get deployments              # Lister les Deployments
kubectl get services                 # Lister les Services
kubectl get all                      # Tout lister

# --- DÉTAILS ---
kubectl describe pod mon-pod         # Détails complets d'un Pod (événements, état, erreurs)
kubectl logs mon-pod                 # Logs du container dans le Pod
kubectl logs -f mon-pod              # Logs en temps réel (follow)

# --- INTERACTION ---
kubectl exec -it mon-pod -- bash     # Shell dans le container
kubectl port-forward mon-pod 8080:80 # Accès local au port 80 du Pod

# --- DÉPLOIEMENT ---
kubectl apply -f manifest.yaml       # Appliquer un manifest (créer ou mettre à jour)
kubectl delete -f manifest.yaml      # Supprimer les ressources décrites dans le manifest

# --- SCALING ---
kubectl scale deployment web --replicas=5   # Passer à 5 instances
```

#### Déployer pas à pas

**1. Crée le manifest du Deployment** (`deployment.yaml`) :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:1.25
        ports:
        - containerPort: 80
```

**2. Crée le manifest du Service** (`service.yaml`) :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
  type: NodePort
```

**3. Applique les manifests :**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

**4. Vérifie :**

```bash
kubectl get pods              # 3 pods en Running
kubectl get services          # Le service avec son NodePort
kubectl describe deployment web   # Détails du Deployment
```

**5. Teste :**

```bash
# Avec minikube
minikube service web-service --url
# Ouvre l'URL dans ton navigateur
```

#### Le rolling update

Pour mettre à jour l’application, modifie l’image dans le manifest et réapplique :

```bash
# Modifier l'image dans deployment.yaml : image: nginx:1.26
kubectl apply -f deployment.yaml

# Observer le rolling update en temps réel
kubectl rollout status deployment web

# Historique des déploiements
kubectl rollout history deployment web

# Revenir en arrière (rollback)
kubectl rollout undo deployment web
```

Kubernetes crée les nouveaux Pods un par un et supprime les anciens progressivement. À aucun moment l’application n’est indisponible.

> **📋 CONTAINER — Épisode 6**
> 
> Sami déploie la stack MedFlow sur minikube. Django tourne dans un Deployment (3 replicas), PostgreSQL dans un StatefulSet avec PVC (on verra ça au chapitre 15), Redis dans un Deployment. Un Service de type ClusterIP expose chaque composant en interne. Il fait un rolling update de Django en changeant la version de l’image — les 3 pods sont remplacés un par un sans interruption.

### Très utile en pratique

#### Mettre plusieurs objets dans un seul fichier

Tu peux séparer les manifests par `---` dans un seul fichier :

```yaml
# stack.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  # ...
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  # ...
```

```bash
kubectl apply -f stack.yaml    # Applique tous les objets d'un coup
```

#### Dry run : tester sans appliquer

```bash
kubectl apply -f manifest.yaml --dry-run=client   # Vérifie la syntaxe sans rien créer
kubectl diff -f manifest.yaml                       # Montre ce qui changerait
```

### Bonus

#### Helm et Kustomize : gérer les manifests dans la vraie vie

En production, personne ne gère des dizaines de fichiers YAML à la main. Deux outils dominent :

**Helm** est un “gestionnaire de packages” pour Kubernetes. Il regroupe tous les manifests d’une application dans un **chart** (un package) avec des variables personnalisables. Au lieu de modifier les YAML un par un, tu changes les variables dans un fichier `values.yaml`.

```bash
# Installer une application avec Helm
helm install mon-app bitnami/postgresql --set auth.postgresPassword=secret

# Lister les installations
helm list

# Mettre à jour
helm upgrade mon-app bitnami/postgresql --set auth.postgresPassword=newsecret
```

**Kustomize** est une approche plus légère : tu gardes tes manifests YAML standards et tu crées des **overlays** (surcouches) pour chaque environnement (dev, staging, prod) sans dupliquer les fichiers.

```bash
# Appliquer avec un overlay
kubectl apply -k overlays/production/
```

Tu n’as pas besoin de maîtriser ces outils pour débuter, mais sache qu’ils existent : dans un vrai environnement K8s, tu les rencontreras systématiquement.

### ❌ Erreur classique

```bash
# Labels qui ne correspondent pas entre Deployment et Service
# → Le Service ne trouve pas les Pods → pas de trafic routé
# Vérifier : kubectl describe service web-service → Endpoints doit montrer des IPs

# Oublier le containerPort
# → Le Pod tourne mais le trafic n'arrive pas

# Confondre kubectl apply et kubectl create
kubectl create -f manifest.yaml    # Crée — échoue si ça existe déjà
kubectl apply -f manifest.yaml     # Crée OU met à jour — idempotent ← Préfère celui-ci
```

### ✅ Tu sais maintenant…

- Les commandes kubectl essentielles (get, describe, logs, exec, apply, delete)
- Écrire et appliquer des manifests YAML
- Le rolling update et le rollback
- Le port-forward pour tester localement

-----


## Chapitre 15 — Stockage, Ingress et configuration avancée

### Le minimum à savoir

#### Le stockage persistant

Les Pods sont éphémères — comme les containers Docker. Pour les données qui doivent persister (bases de données), Kubernetes utilise un système de stockage en 3 couches :

- **PersistentVolume (PV)** : un espace de stockage provisionné (un disque EBS sur AWS, un disque Azure, un partage NFS)
- **PersistentVolumeClaim (PVC)** : une “demande” de stockage faite par un Pod (“je veux 10 Go de stockage”)
- **StorageClass** : le type de stockage disponible (SSD rapide, HDD pas cher, etc.)

```yaml
# PVC : le Pod demande du stockage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data
spec:
  accessModes:
    - ReadWriteOnce       # Un seul Pod peut écrire à la fois
  resources:
    requests:
      storage: 10Gi       # 10 Go demandés
```

Le PVC est ensuite monté dans le Pod :

```yaml
spec:
  containers:
  - name: db
    image: postgres:16
    volumeMounts:
    - name: data
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: db-data
```

#### Le StatefulSet (pour les bases de données)

Le **StatefulSet** est l’objet K8s conçu pour les applications avec état (bases de données, systèmes distribués). Contrairement au Deployment :

- Chaque Pod a un **nom stable** (db-0, db-1, db-2 au lieu de noms aléatoires)
- Chaque Pod a son **propre volume persistant**
- Les Pods sont créés et supprimés **dans l’ordre** (important pour les réplications)

#### L’Ingress : exposer à l’extérieur

Un Service de type `ClusterIP` n’est accessible que depuis l’intérieur du cluster. Pour exposer une application sur Internet avec un nom de domaine et du HTTPS, on utilise un **Ingress** :

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: app.medflow.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
  tls:
  - hosts:
    - app.medflow.com
    secretName: tls-cert       # Certificat TLS dans un Secret
```

L’Ingress a besoin d’un **Ingress Controller** installé dans le cluster (nginx-ingress, traefik, HAProxy). C’est le composant qui lit les règles Ingress et configure le reverse proxy.

#### Les probes : le self-healing en action

Les probes sont des vérifications automatiques de santé :

```yaml
spec:
  containers:
  - name: web
    image: mon_app:1.0.0
    livenessProbe:              # Le container est-il vivant ?
      httpGet:
        path: /health
        port: 8000
      periodSeconds: 10
    readinessProbe:             # Le container est-il prêt à recevoir du trafic ?
      httpGet:
        path: /ready
        port: 8000
      initialDelaySeconds: 5
```

|Probe        |Question                                |Si elle échoue                                     |
|-------------|----------------------------------------|---------------------------------------------------|
|**Liveness** |“Le container est-il vivant ?”          |K8s le **redémarre**                               |
|**Readiness**|“Le container est-il prêt ?”            |K8s **retire** le Pod du Service (plus de trafic)  |
|**Startup**  |“Le container a-t-il fini de démarrer ?”|K8s **attend** avant de vérifier liveness/readiness|

#### Resource requests et limits

```yaml
resources:
  requests:          # "Je voudrais au minimum..."
    memory: "128Mi"
    cpu: "100m"      # 100 millicores = 0.1 CPU
  limits:            # "Je ne dois pas dépasser..."
    memory: "256Mi"
    cpu: "500m"      # 500 millicores = 0.5 CPU
```

- **Requests** : ce que le Scheduler utilise pour décider sur quel nœud placer le Pod. Si le nœud n’a pas assez de ressources “disponibles” (en requests), le Pod n’y sera pas placé.
- **Limits** : le maximum que le container peut consommer. Si le container dépasse la limite mémoire → **OOMKilled**. S’il dépasse la limite CPU → **throttling** (ralentissement).

> **Bonne pratique :** mets toujours des requests et des limits. Sans limits, un container peut consommer toutes les ressources du nœud et impacter les autres Pods.

### ✅ Tu sais maintenant…

- Le stockage persistant (PV, PVC, StorageClass)
- Le StatefulSet pour les applications avec état
- L’Ingress pour exposer des applications sur Internet
- Les probes pour le self-healing (liveness, readiness, startup)
- Les resource requests et limits

-----


## Chapitre 16 — Capstone Partie III : déployer une application sur Kubernetes

### L’exercice

**Objectif :** déployer la stack MedFlow sur un cluster Kubernetes de lab (minikube/kind).

**Les composants :**

1. **Django** : Deployment (3 replicas) + Service ClusterIP + probes liveness/readiness
1. **PostgreSQL** : StatefulSet + PVC (10 Gi) + Service ClusterIP
1. **Redis** : Deployment (1 replica) + Service ClusterIP
1. **Ingress** : expose Django sur un hostname local

**Les étapes :**

1. Écrire les manifests YAML pour chaque composant
1. Créer un ConfigMap pour les variables non sensibles
1. Créer un Secret pour le mot de passe de la base de données
1. Déployer avec `kubectl apply -f`
1. Vérifier que tout tourne (`kubectl get all`, `kubectl logs`)
1. Simuler un crash : `kubectl delete pod` → observer le self-healing
1. Faire un rolling update en changeant la version de l’image
1. Faire un rollback

**Checklist :**

|Critère                                             |Vérifié ?|
|----------------------------------------------------|---------|
|3 replicas Django tournent                          |         |
|PostgreSQL a un volume persistant                   |         |
|Les probes liveness/readiness sont configurées      |         |
|Les resource requests et limits sont définies       |         |
|Les secrets ne sont pas en clair dans les manifests |         |
|Le self-healing fonctionne (delete pod → recréation)|         |
|Le rolling update fonctionne sans interruption      |         |

### ✅ Tu sais maintenant…

- Déployer une application multi-composants sur Kubernetes
- Combiner Deployment, Service, ConfigMap, Secret, PVC, Ingress
- Vérifier, diagnostiquer et mettre à jour un déploiement K8s

-----
