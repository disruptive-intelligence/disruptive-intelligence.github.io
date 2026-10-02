---
title: Chapitre 13 — Les objets Kubernetes essentiels
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

## Le minimum à savoir

### Le Pod

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

### Le Deployment

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

### Le Service

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

### Le Namespace

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

### ConfigMap et Secret

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

## Très utile en pratique

### Les labels et sélecteurs : le mécanisme de liaison

Les **labels** sont des paires clé-valeur attachées aux objets. Les **sélecteurs** permettent de sélectionner des objets par leurs labels. C’est le mécanisme qui lie un Service à ses Pods, un Deployment à ses Pods, etc.

```yaml
# Le Deployment crée des Pods avec le label app: web
# Le Service sélectionne les Pods avec le label app: web
# → Le Service route le trafic vers les bons Pods
```


Si les labels ne correspondent pas entre le Deployment, les Pods et le Service, rien ne fonctionne. C’est la cause n°1 de troubleshooting en K8s pour les débutants.

### Utiliser les ConfigMaps et Secrets dans un Pod

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


## ✅ Tu sais maintenant…

- Le Pod (unité de base, rarement utilisé seul)
- Le Deployment (gère les Pods : replicas, rolling updates, self-healing)
- Le Service (donne une adresse stable à un groupe de Pods)
- Le Namespace (séparation logique, pas une frontière de sécurité en soi)
- Les ConfigMaps et Secrets (configuration et données sensibles — Secrets en base64, pas chiffrés !)
- Les labels et sélecteurs (le mécanisme qui lie tout ensemble)

## 💬 Questions d’entretien typiques

- **Pourquoi un Service est-il nécessaire si les Pods existent déjà ?** → Les Pods sont éphémères et changent d’adresse IP à chaque recréation. Le Service fournit une adresse stable et un nom DNS qui pointe toujours vers les bons Pods, via le mécanisme de labels/sélecteurs.
- **Quelle est la différence entre un Deployment et un Pod ?** → On ne déploie pas de Pods seuls en production. Un Deployment gère un groupe de Pods identiques : il assure le nombre de replicas demandé, redémarre les Pods qui plantent, et gère les mises à jour sans interruption (rolling update).
- **Les Secrets Kubernetes sont-ils sécurisés ?** → Non par défaut. Ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC appropriés peut les lire. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe.

-----
