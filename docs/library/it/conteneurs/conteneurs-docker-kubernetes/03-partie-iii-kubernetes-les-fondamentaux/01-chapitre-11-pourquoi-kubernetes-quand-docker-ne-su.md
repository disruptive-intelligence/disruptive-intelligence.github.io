---
title: 'Chapitre 11 — Pourquoi Kubernetes : quand Docker ne suffit plus'
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

## Le minimum à savoir

### Les limites de Docker seul

Docker Compose est parfait pour le développement et les petits déploiements. Mais imagine que ton application doit :

- Tourner sur **plusieurs serveurs** (pas un seul)
- **Résister à la panne** d’un serveur (si un serveur tombe, l’application continue)
- **Scaler automatiquement** (ajouter des instances quand il y a plus de trafic, en retirer quand le trafic baisse)
- Se **mettre à jour sans interruption** (rolling update — les utilisateurs ne voient pas la mise à jour)
- **Redémarrer automatiquement** un container qui plante (self-healing)

Docker Compose ne sait pas faire ça. Il gère des containers sur **une seule machine**. Pour gérer des containers sur **plusieurs machines**, il faut un **orchestrateur**. Et l’orchestrateur dominant, c’est **Kubernetes**.

### Kubernetes en une phrase

Kubernetes (souvent abrégé **K8s** — K + 8 lettres + s) est un système qui **gère automatiquement le déploiement, le scaling et le cycle de vie de containers sur un ensemble de serveurs**.

Tu lui dis “je veux 3 instances de mon application web, toujours disponibles”, et Kubernetes s’assure que c’est le cas : il les répartit sur les serveurs disponibles, les redémarre si elles plantent, en ajoute si tu augmentes le nombre, et les met à jour sans interruption.

### Le paradigme déclaratif

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

### Les options pour utiliser Kubernetes

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


### Kubernetes n’est pas toujours la réponse

Kubernetes ajoute une **complexité opérationnelle significative**. Pour une petite application avec peu de trafic et une petite équipe, Docker Compose sur un seul serveur est souvent suffisant et beaucoup plus simple.

Kubernetes se justifie quand tu as besoin de :

- Haute disponibilité (l’application ne doit jamais tomber)
- Scaling automatique (le trafic varie)
- Déploiements sans interruption (rolling updates)
- Multi-services avec des équipes différentes (chacune déploie indépendamment)

> **📋 CONTAINER — Épisode 5 (partie 3)**
> 
> Le CTO de MedFlow veut passer en production. Docker Compose sur un seul serveur n’est pas suffisant : l’application doit être hautement disponible (données de santé), scaler pendant les pics d’utilisation (9h-12h), et se mettre à jour sans interruption. La décision est prise : EKS (Kubernetes managé sur AWS). Sami installe minikube pour prototyper la migration avant de passer sur EKS.

## Très utile en pratique

### kubectl : l’outil de base

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

### Kubernetes managé vs auto-hébergé

En entreprise, la quasi-totalité des déploiements Kubernetes sont **managés** (EKS, AKS, GKE). Le cloud provider gère le Control Plane (API Server, etcd, Scheduler…) — tu ne gères que tes applications et la configuration. Héberger et maintenir son propre cluster K8s (vanilla) est complexe et réservé aux équipes avec une forte expertise.

## ✅ Tu sais maintenant…

- Pourquoi Kubernetes existe (les limites de Docker seul)
- Le paradigme déclaratif (état désiré vs état actuel)
- Les options pour utiliser K8s (minikube pour apprendre, managé pour la production)
- Que Kubernetes n’est pas toujours nécessaire (Docker Compose suffit souvent)

-----
