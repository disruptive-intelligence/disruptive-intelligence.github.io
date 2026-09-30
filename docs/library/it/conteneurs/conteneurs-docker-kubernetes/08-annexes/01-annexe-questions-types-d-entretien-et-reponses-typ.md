---
title: Annexe — Questions types d'entretien et réponses types
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Annexes
  - index.md
---

### Questions essentielles

- **Question :** Quelle est la différence entre un container et une VM ?
  - **Réponse type :** Un container partage le kernel de l'hôte et embarque uniquement l'application et ses dépendances. Il démarre en quelques secondes et consomme très peu de ressources. Une VM embarque un OS complet avec son propre kernel, ce qui offre une isolation plus forte mais la rend beaucoup plus lourde. En résumé : le container est plus léger et plus rapide, mais l'isolation est moins forte car le kernel est partagé.

- **Question :** Qu'est-ce qu'une image Docker et comment on la construit ?
  - **Réponse type :** Une image est un template en lecture seule qui contient tout ce qu'il faut pour faire tourner une application : code, dépendances, configuration. On la construit avec un Dockerfile, un fichier texte qui décrit les étapes de construction. Chaque instruction crée une couche (layer). On utilise `docker build` pour produire l'image à partir du Dockerfile.

- **Question :** Comment sécurisez-vous une image Docker ?
  - **Réponse type :** Plusieurs bonnes pratiques : partir d'une image officielle ou minimale (slim, distroless), utiliser un multi-stage build pour ne garder que le nécessaire, ne jamais tourner en root (instruction USER), scanner les vulnérabilités avec Trivy, et ne pas embarquer de secrets dans l'image. En production, on signe les images avec Cosign et on utilise un registry privé.

- **Question :** Qu'est-ce que Kubernetes et pourquoi on l'utilise ?
  - **Réponse type :** Kubernetes est un orchestrateur de containers. Quand on a beaucoup de containers répartis sur plusieurs serveurs, Docker seul ne suffit plus pour gérer le scaling, le self-healing, les mises à jour sans coupure, et la répartition de charge. Kubernetes automatise tout ça. Il gère le cycle de vie des containers à l'échelle d'un cluster.

- **Question :** Quels sont les objets Kubernetes essentiels à connaître ?
  - **Réponse type :** Le Pod, c'est la plus petite unité — un ou plusieurs containers qui tournent ensemble. Le Deployment gère le déploiement et le scaling des Pods. Le Service donne une adresse réseau stable à un groupe de Pods. Le Namespace permet de séparer logiquement les ressources. Et les Secrets/ConfigMaps gèrent la configuration et les données sensibles.

### Questions complémentaires

- **Question :** Quels sont les principaux risques de sécurité liés aux containers ?
  - **Réponse type :** Les risques majeurs : tourner en root dans le container (un escape mène directement au root de l'hôte), utiliser des images vulnérables ou non vérifiées (supply chain), monter le Docker socket dans un container (c'est comme donner les clés de l'hôte), ne pas mettre de Network Policies (par défaut tous les Pods se parlent), et stocker des secrets en clair dans les manifests Kubernetes.

- **Question :** C'est quoi Docker Compose et dans quel cas on l'utilise ?
  - **Réponse type :** Docker Compose permet de définir et lancer plusieurs containers ensemble via un fichier YAML. Typiquement, une application avec un backend, une base de données et un cache Redis. On décrit les services, les réseaux et les volumes dans un docker-compose.yml, et un seul `docker compose up` lance tout. C'est surtout utilisé en développement et en environnement de test.

- **Question :** Comment fonctionne le RBAC dans Kubernetes ?
  - **Réponse type :** Le RBAC (Role-Based Access Control) contrôle qui peut faire quoi dans le cluster. On définit des Roles (permissions sur un namespace) ou ClusterRoles (permissions globales), puis on les lie à des utilisateurs ou des Service Accounts via des RoleBindings. Le principe c'est le moindre privilège : on ne donne que les droits strictement nécessaires.

### Questions les plus probables en entretien

1. Différence container vs VM ?
2. Comment sécuriser une image Docker ?
3. Pourquoi Kubernetes ? Quels objets essentiels ?
4. Quels risques de sécurité avec les containers ?
5. C'est quoi un Dockerfile, un Pod, un Deployment, un Service ?

### Réponses flash

- **Container vs VM** → Container = partage kernel, léger, rapide, isolation moindre. VM = OS complet, plus lourd, isolation forte.
- **Image** → Template read-only, construit via Dockerfile, chaque instruction = une layer.
- **Sécurité image** → Image minimale, multi-stage, non-root, scan Trivy, pas de secrets, signature Cosign.
- **Kubernetes** → Orchestrateur : scaling, self-healing, rolling updates, load balancing sur un cluster.
- **Objets K8s** → Pod (unité de base), Deployment (scaling/déploiement), Service (réseau stable), Namespace (isolation logique).
- **Risques sécu** → Root dans container, images vulnérables, Docker socket monté, pas de Network Policy, secrets en clair.
- **RBAC K8s** → Roles + RoleBindings, moindre privilège, pas de cluster-admin sauf admins.

---


## Conclusion

Tu as maintenant une compréhension solide de l’écosystème containers — de la théorie à la pratique, de Docker à Kubernetes, de l’utilisation à la sécurisation.

**Pour continuer à progresser :**

- Monte un lab avec minikube et déploie tes propres applications
- Passe la CKA si tu vises un poste DevOps/SRE
- Passe la CKS si tu vises un poste sécurité cloud/containers
- Suis KubeCon sur YouTube pour rester à jour
- Lis le code des Helm charts et des operators pour comprendre les patterns avancés

L’écosystème containers est vaste et en constante évolution. Ce cours t’a donné les fondations solides pour y naviguer — le reste viendra avec la pratique.
