---
title: Chapitre 15 — Stockage, Ingress et configuration avancée
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

## Le minimum à savoir

### Le stockage persistant

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


### Le StatefulSet (pour les bases de données)

Le **StatefulSet** est l’objet K8s conçu pour les applications avec état (bases de données, systèmes distribués). Contrairement au Deployment :

- Chaque Pod a un **nom stable** (db-0, db-1, db-2 au lieu de noms aléatoires)
- Chaque Pod a son **propre volume persistant**
- Les Pods sont créés et supprimés **dans l’ordre** (important pour les réplications)

### L’Ingress : exposer à l’extérieur

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

### Les probes : le self-healing en action

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

### Resource requests et limits

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

## ✅ Tu sais maintenant…

- Le stockage persistant (PV, PVC, StorageClass)
- Le StatefulSet pour les applications avec état
- L’Ingress pour exposer des applications sur Internet
- Les probes pour le self-healing (liveness, readiness, startup)
- Les resource requests et limits

-----
