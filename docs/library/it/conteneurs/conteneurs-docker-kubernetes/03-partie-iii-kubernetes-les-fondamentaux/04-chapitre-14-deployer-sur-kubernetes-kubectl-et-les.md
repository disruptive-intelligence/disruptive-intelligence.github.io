---
title: 'Chapitre 14 — Déployer sur Kubernetes : kubectl et les manifests'
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

## Le minimum à savoir

### Les commandes kubectl essentielles

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


### Déployer pas à pas

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


### Le rolling update

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

## Très utile en pratique

### Mettre plusieurs objets dans un seul fichier

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


### Dry run : tester sans appliquer

```bash
kubectl apply -f manifest.yaml --dry-run=client   # Vérifie la syntaxe sans rien créer
kubectl diff -f manifest.yaml                       # Montre ce qui changerait
```


## Bonus

### Helm et Kustomize : gérer les manifests dans la vraie vie

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

## ❌ Erreur classique

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


## ✅ Tu sais maintenant…

- Les commandes kubectl essentielles (get, describe, logs, exec, apply, delete)
- Écrire et appliquer des manifests YAML
- Le rolling update et le rollback
- Le port-forward pour tester localement

-----
