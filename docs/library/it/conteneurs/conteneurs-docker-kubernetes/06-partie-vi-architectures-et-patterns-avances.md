---
title: Partie VI — Architectures ET patterns avancés
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - index.md
---

-----


## Chapitre 27 — Microservices, patterns et anti-patterns

### Le minimum à savoir

#### Monolithe vs Microservices

|Aspect     |Monolithe                                  |Microservices                            |
|-----------|-------------------------------------------|-----------------------------------------|
|Structure  |1 application, 1 déploiement               |N services indépendants                  |
|Déploiement|Tout ou rien                               |Service par service                      |
|Scaling    |L’application entière                      |Chaque service indépendamment            |
|Complexité |Simple au début, difficile à grande échelle|Complexe dès le début (réseau, debugging)|
|Équipe     |1 équipe, 1 codebase                       |N équipes, N codebases                   |

**L’erreur classique :** migrer vers des microservices trop tôt. Si ton équipe est petite et ton application simple, un monolithe bien structuré est plus simple et plus rapide. Les microservices se justifient quand l’application est grande, l’équipe est grande, et les besoins de scaling sont différents par composant.

> **À retenir pour un entretien :** “Les microservices ne sont pas toujours la bonne réponse. Un monolithe containerisé est déjà un énorme progrès. La migration vers les microservices se justifie quand la taille de l’équipe et de l’application le nécessite.”

#### Les anti-patterns de sécurité dans les microservices

- **Confiance aveugle au trafic interne :** “les requêtes viennent de l’intérieur du cluster, donc elles sont fiables” → faux si un Pod est compromis
- **Absence d’AuthN/AuthZ inter-services :** chaque service devrait vérifier l’identité et les droits de l’appelant
- **Secrets partagés :** un secret commun à tous les services → si un service est compromis, tous les secrets fuient

### ✅ Tu sais maintenant…

- La différence entre monolithe et microservices (et quand migrer)
- Les anti-patterns de sécurité des microservices

-----


## Chapitre 28 — Multi-tenancy, scaling et production

### Le minimum à savoir

#### Le scaling automatique

|Type                               |Ce qu’il scale         |Comment                                                                |
|-----------------------------------|-----------------------|-----------------------------------------------------------------------|
|**HPA** (Horizontal Pod Autoscaler)|Le nombre de Pods      |Ajoute/retire des Pods selon la charge (CPU, mémoire, métriques custom)|
|**VPA** (Vertical Pod Autoscaler)  |Les ressources d’un Pod|Ajuste les requests/limits selon l’utilisation réelle                  |
|**Cluster Autoscaler**             |Le nombre de nœuds     |Ajoute/retire des nœuds selon les besoins de scheduling                |

```yaml
# HPA — scaler entre 3 et 10 replicas selon le CPU
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70    # Scale up si CPU > 70%
```


#### La haute disponibilité

- **PodDisruptionBudget :** garantir qu’un nombre minimum de Pods reste actif pendant les maintenances
- **Anti-affinity :** répartir les Pods sur différents nœuds (si un nœud tombe, l’application continue)
- **Multi-AZ :** répartir les nœuds sur plusieurs zones de disponibilité

### ✅ Tu sais maintenant…

- Le scaling automatique (HPA, VPA, Cluster Autoscaler)
- Les mécanismes de haute disponibilité (PDB, anti-affinity, multi-AZ)

-----
