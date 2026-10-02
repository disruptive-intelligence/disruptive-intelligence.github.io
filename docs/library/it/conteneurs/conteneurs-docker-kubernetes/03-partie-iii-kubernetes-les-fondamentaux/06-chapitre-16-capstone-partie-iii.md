---
title: Chapitre 16 — Capstone Partie III
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - 'Partie III — Kubernetes : les fondamentaux'
  - index.md
---

déployer une application sur Kubernetes

## L’exercice

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

## ✅ Tu sais maintenant…

- Déployer une application multi-composants sur Kubernetes
- Combiner Deployment, Service, ConfigMap, Secret, PVC, Ingress
- Vérifier, diagnostiquer et mettre à jour un déploiement K8s

-----
