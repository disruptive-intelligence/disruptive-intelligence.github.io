---
title: 'Chapitre 12 — Architecture Kubernetes : les composants du cluster'
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

## Le minimum à savoir

### Le cluster : la vue d’ensemble

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


### Les composants du Control Plane

|Composant             |Rôle                                                           |Analogie simple                                         |
|----------------------|---------------------------------------------------------------|--------------------------------------------------------|
|**API Server**        |Le point d’entrée unique — toutes les commandes passent par lui|La réception d’un hôtel : tout le monde passe par là    |
|**etcd**              |La base de données du cluster — stocke tout l’état             |Le registre de l’hôtel : qui est dans quelle chambre    |
|**Scheduler**         |Décide sur quel nœud placer chaque pod                         |Le concierge qui attribue les chambres                  |
|**Controller Manager**|Vérifie que l’état actuel correspond à l’état désiré           |Le responsable qualité qui vérifie que tout est en ordre|


> **Point critique :** tout passe par l’**API Server**. Quand tu tapes `kubectl get pods`, ta commande va à l’API Server. Quand le Scheduler place un pod, il parle à l’API Server. Quand un kubelet signale l’état d’un pod, il parle à l’API Server. **Contrôler l’accès à l’API Server, c’est contrôler le cluster** (voir chapitre 25 sur la sécurité).

> **Point critique :** **etcd** contient l’intégralité de l’état du cluster, y compris les Secrets. Si etcd est compromis, tout le cluster est compromis. En production, etcd doit être chiffré, sauvegardé, et accessible uniquement au Control Plane.

### Les composants des Worker Nodes

|Composant            |Rôle                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------|
|**kubelet**          |L’agent sur chaque nœud — reçoit les instructions de l’API Server et gère les containers localement|
|**kube-proxy**       |Gère le réseau — route le trafic vers les bons pods                                                |
|**Container runtime**|Exécute les containers (containerd)                                                                |

### Le flux simplifié

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


## Très utile en pratique

### Kubernetes managé : ce que le cloud gère pour toi

Avec EKS, AKS ou GKE, le **Control Plane est géré par le cloud provider**. Tu ne vois pas les machines qui font tourner l’API Server, etcd, le Scheduler. Tu ne les maintiens pas, tu ne les patches pas. Tu ne gères que les Worker Nodes (et même ceux-là peuvent être managés avec des node pools auto-scalés).

C’est un avantage énorme : maintenir un Control Plane K8s est un travail à plein temps. Avec un service managé, tu te concentres sur tes applications.

### Inspecter le cluster

```bash
# Voir les nœuds
kubectl get nodes

# Voir les composants du Control Plane
kubectl get componentstatuses    # ou kubectl get cs

# Voir tout dans tous les namespaces
kubectl get all --all-namespaces
```


## Bonus

### La haute disponibilité du Control Plane

En production, le Control Plane doit être en haute disponibilité : **3 nœuds etcd minimum** (consensus par Raft), **API Server répliqué** derrière un load balancer. Les services managés (EKS, AKS, GKE) gèrent ça automatiquement — c’est l’un des avantages principaux.

## ✅ Tu sais maintenant…

- L’architecture Control Plane + Worker Nodes
- Le rôle de chaque composant (API Server, etcd, Scheduler, Controller Manager, kubelet)
- Que tout passe par l’API Server (implications en sécurité)
- Que etcd est la base de données la plus critique du cluster
- La différence entre K8s auto-hébergé et managé

-----
