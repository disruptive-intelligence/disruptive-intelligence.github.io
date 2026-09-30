---
title: PARTIE VII — SYNTHÈSE
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 7
chapters: 7
---

-----


## Chapitre 29 — Cas de synthèse : audit de sécurité d’un environnement containerisé

### L’exercice

Un cluster Kubernetes de production avec des faiblesses volontaires. L’étudiant doit :

1. **Auditer les images :** scanner avec Trivy, vérifier les images de base, chercher les secrets dans les layers
1. **Auditer le runtime :** vérifier les users (root ?), les capabilities, le filesystem read-only, le Docker socket
1. **Auditer K8s :** kube-bench, RBAC (cluster-admin partout ?), Service Accounts, Secrets, Network Policies
1. **Produire un rapport :** matrice des risques classée P0/P1/P2, plan de remédiation, quick wins

> **📋 CONTAINER — Épisode final**
> 
> 6 mois plus tard. MedFlow tourne sur EKS. Images signées avec Cosign et scannées par Trivy dans la CI, Network Policies en default deny (seuls les flux explicitement autorisés passent), RBAC minimal (chaque développeur n’a accès qu’à son namespace), secrets dans AWS Secrets Manager via External Secrets Operator, Falco en détection runtime, monitoring Prometheus/Grafana, logs centralisés dans Loki. Un audit externe confirme la posture. Sami rédige le runbook d’exploitation et forme l’équipe dev sur les bonnes pratiques. Le CTO : “Il y a 6 mois on ne savait pas ce qu’était un Dockerfile.”

-----


## Chapitre 30 — Le métier et les perspectives

### Le minimum à savoir

#### Les métiers

|Métier                             |Focus                                           |Compétences clés                       |
|-----------------------------------|------------------------------------------------|---------------------------------------|
|**DevOps Engineer**                |Automatiser le build, test, déploiement         |CI/CD, Docker, K8s, IaC                |
|**SRE** (Site Reliability Engineer)|Fiabilité et performance en production          |Monitoring, troubleshooting, SLO/SLA   |
|**Platform Engineer**              |Construire la plateforme pour les développeurs  |K8s, abstractions, developer experience|
|**Cloud Security Engineer**        |Sécuriser les environnements cloud et containers|Hardening, audit, compliance, détection|

#### Les certifications

|Certification                                        |Organisme            |Focus                |Difficulté            |
|-----------------------------------------------------|---------------------|---------------------|----------------------|
|**CKA** (Certified Kubernetes Administrator)         |CNCF/Linux Foundation|Administration K8s   |Intermédiaire         |
|**CKAD** (Certified Kubernetes Application Developer)|CNCF/Linux Foundation|Développement sur K8s|Intermédiaire         |
|**CKS** (Certified Kubernetes Security Specialist)   |CNCF/Linux Foundation|Sécurité K8s         |Avancé (prérequis CKA)|


> **Conseil :** la CKA est la certification la plus demandée. Elle valide ta capacité à administrer un cluster K8s. La CKS est le complément sécurité — très valorisée dans les profils cyber/cloud security.

#### L’écosystème en mouvement

- **eBPF :** technologie kernel Linux qui révolutionne l’observabilité et la sécurité des containers (Cilium, Tetragon, Falco) — sans modifier les applications
- **WebAssembly (Wasm) :** alternative émergente aux containers pour certains cas d’usage — plus léger, sandboxé, portable
- **Kubernetes sans Kubernetes :** des abstractions qui masquent la complexité (AWS Fargate, Google Cloud Run, Azure Container Apps) — tu déploies des containers sans gérer le cluster

#### La veille

Les sources essentielles : le blog CNCF, KubeCon (la conférence de référence — vidéos gratuites sur YouTube), le Kubernetes security mailing list, learnk8s.io (ressources d’apprentissage), et les rapports annuels de sécurité Kubernetes (Sysdig, Datadog).

### ✅ Tu sais maintenant…

- Les métiers liés aux containers et à Kubernetes
- Les certifications de référence (CKA, CKAD, CKS)
- Les tendances technologiques (eBPF, Wasm, abstractions serverless)

-----


## ANNEXES

-----

### Annexe A — Glossaire

|Terme                     |Définition                                                                              |
|--------------------------|----------------------------------------------------------------------------------------|
|**Alpine**                |Distribution Linux ultra-légère (~5 Mo), souvent utilisée comme image de base           |
|**API Server**            |Point d’entrée unique du cluster Kubernetes — tout passe par lui                        |
|**ArgoCD**                |Outil GitOps — synchronise l’état du cluster K8s avec un repo Git                       |
|**Base64**                |Encodage (PAS chiffrement) utilisé pour les Secrets K8s                                 |
|**Bind mount**            |Montage d’un dossier de l’hôte dans un container                                        |
|**Bridge**                |Driver réseau Docker par défaut — réseau isolé                                          |
|**Capability**            |Permission granulaire du kernel Linux attribuée à un container                          |
|**cgroup**                |Control Group — mécanisme Linux de limitation des ressources (CPU, RAM)                 |
|**CKA**                   |Certified Kubernetes Administrator — certification CNCF                                 |
|**CKS**                   |Certified Kubernetes Security Specialist — certification CNCF                           |
|**ClusterIP**             |Type de Service K8s accessible uniquement à l’intérieur du cluster                      |
|**CNCF**                  |Cloud Native Computing Foundation — gouvernance de Kubernetes et des projets associés   |
|**CNI**                   |Container Network Interface — plugin réseau pour Kubernetes (Calico, Cilium)            |
|**ConfigMap**             |Objet K8s pour stocker de la configuration non sensible                                 |
|**Container escape**      |Sortie d’un container pour atteindre la machine hôte                                    |
|**containerd**            |Runtime de containers de haut niveau utilisé par Docker et K8s                          |
|**Cosign**                |Outil de signature d’images Docker (projet Sigstore)                                    |
|**CRI**                   |Container Runtime Interface — interface standard entre K8s et les runtimes              |
|**Deployment**            |Objet K8s qui gère le déploiement et le scaling d’une application                       |
|**Distroless**            |Image Docker minimale sans shell ni outils — surface d’attaque minimale                 |
|**Docker Compose**        |Outil pour gérer des applications multi-containers sur un seul hôte                     |
|**Docker Hub**            |Registry public par défaut pour les images Docker                                       |
|**Docker socket**         |`/var/run/docker.sock` — accès au daemon Docker (⚠️ donne un contrôle total)             |
|**Dockerfile**            |Fichier texte décrivant la construction d’une image Docker                              |
|**eBPF**                  |Extended Berkeley Packet Filter — technologie kernel pour l’observabilité et la sécurité|
|**EKS**                   |Elastic Kubernetes Service — K8s managé par AWS                                         |
|**etcd**                  |Base de données distribuée du cluster K8s — contient tout l’état                        |
|**Falco**                 |Outil CNCF de détection d’anomalies runtime dans les containers                         |
|**GitOps**                |Modèle où Git est la source de vérité pour l’état du cluster                            |
|**Grafana**               |Outil de dashboards pour le monitoring                                                  |
|**Grype**                 |Scanner de vulnérabilités pour les images Docker                                        |
|**Harbor**                |Registry Docker open source avec scan intégré                                           |
|**HPA**                   |Horizontal Pod Autoscaler — scaling automatique du nombre de Pods                       |
|**Ingress**               |Objet K8s qui expose des applications HTTP/HTTPS au monde extérieur                     |
|**Kaniko**                |Outil de build d’images Docker sans Docker socket                                       |
|**kubectl**               |Outil CLI pour interagir avec un cluster Kubernetes                                     |
|**kubelet**               |Agent sur chaque nœud K8s qui gère les containers localement                            |
|**Kyverno**               |Admission controller K8s pour les politiques de sécurité                                |
|**Layer**                 |Couche d’une image Docker — chaque instruction Dockerfile crée une couche               |
|**LoadBalancer**          |Type de Service K8s qui crée un load balancer cloud                                     |
|**Loki**                  |Système de centralisation de logs (Grafana Labs)                                        |
|**minikube**              |Cluster K8s local pour l’apprentissage et le développement                              |
|**mTLS**                  |Mutual TLS — chiffrement mutuel entre services                                          |
|**Multi-stage build**     |Technique Dockerfile qui sépare build et production pour réduire la taille              |
|**Namespace**             |Espace logique de séparation dans un cluster K8s                                        |
|**Network Policy**        |Règle de pare-feu entre les Pods dans K8s                                               |
|**NodePort**              |Type de Service K8s accessible via un port sur chaque nœud                              |
|**OCI**                   |Open Container Initiative — standard ouvert pour les images et runtimes                 |
|**OPA/Gatekeeper**        |Admission controller K8s pour les politiques de sécurité                                |
|**OverlayFS**             |Filesystem par couches utilisé par Docker                                               |
|**PersistentVolumeClaim** |Demande de stockage persistant dans K8s                                                 |
|**Pod**                   |Plus petite unité déployable dans K8s — contient un ou plusieurs containers             |
|**Pod Security Standards**|Niveaux de restriction de sécurité K8s (Privileged, Baseline, Restricted)               |
|**Prometheus**            |Système de monitoring et d’alerting (standard K8s)                                      |
|**RBAC**                  |Role-Based Access Control — système de permissions dans K8s                             |
|**Registry**              |Entrepôt d’images Docker (Docker Hub, Harbor, ECR, ACR)                                 |
|**ReplicaSet**            |Objet K8s qui maintient un nombre de Pods (géré par le Deployment)                      |
|**Rolling update**        |Mise à jour progressive des Pods sans interruption                                      |
|**runc**                  |Runtime de containers de bas niveau (standard OCI)                                      |
|**SBOM**                  |Software Bill of Materials — inventaire des composants d’une image                      |
|**Seccomp**               |Filtrage des appels système Linux pour les containers                                   |
|**Secret**                |Objet K8s pour stocker des données sensibles (⚠️ base64, pas chiffré)                    |
|**Service**               |Objet K8s qui donne une adresse réseau stable à un groupe de Pods                       |
|**Service Account**       |Identité d’un Pod dans K8s (avec un token API)                                          |
|**Service Mesh**          |Couche d’infrastructure pour la communication inter-services (Istio, Linkerd)           |
|**Sidecar**               |Container auxiliaire dans un Pod (ex : proxy, collecteur de logs)                       |
|**StatefulSet**           |Objet K8s pour les applications avec état (bases de données)                            |
|**StorageClass**          |Type de stockage disponible dans un cluster K8s                                         |
|**Tag**                   |Version d’une image Docker (ex : `nginx:1.25`)                                          |
|**Trivy**                 |Scanner de vulnérabilités pour les images Docker (open source)                          |
|**Volume**                |Espace de stockage persistant dans Docker ou K8s                                        |
|**Wasm**                  |WebAssembly — alternative émergente aux containers                                      |

-----

### Annexe B — Cheat sheets

#### Commandes Docker essentielles

```bash
# Images
docker build -t nom:tag .          # Construire
docker images                       # Lister
docker pull nom:tag                 # Télécharger
docker rmi nom:tag                  # Supprimer

# Containers
docker run -d --name X -p H:C img  # Lancer
docker ps / docker ps -a            # Lister
docker stop X / docker rm X         # Arrêter / Supprimer
docker logs X / docker logs -f X    # Logs
docker exec -it X bash              # Shell dans le container
docker inspect X                    # Détails

# Nettoyage
docker system prune                 # Tout nettoyer
```

#### Commandes kubectl essentielles

```bash
# Lecture
kubectl get pods/deploy/svc/all     # Lister
kubectl describe pod X              # Détails + événements
kubectl logs X / kubectl logs -f X  # Logs

# Interaction
kubectl exec -it X -- bash          # Shell dans le Pod
kubectl port-forward X 8080:80      # Accès local

# Déploiement
kubectl apply -f manifest.yaml      # Appliquer
kubectl delete -f manifest.yaml     # Supprimer
kubectl scale deploy X --replicas=N # Scaler
kubectl rollout undo deploy X       # Rollback
```

-----

### Annexe C — Tableau d’outils de référence

|Catégorie         |Outil            |Gratuit/Payant|Usage                                   |Limites                       |
|------------------|-----------------|--------------|----------------------------------------|------------------------------|
|Build             |Docker           |Gratuit (CE)  |Construction d’images                   |Daemon en root                |
|Build sans socket |Kaniko           |Gratuit       |Build en CI sans Docker socket          |Plus lent                     |
|Alternative Docker|Podman           |Gratuit       |Containers sans daemon root             |Écosystème plus petit         |
|Scan images       |Trivy            |Gratuit       |Scan CVE images + IaC + SBOM            |Faux positifs possibles       |
|Scan images       |Grype            |Gratuit       |Scan CVE images                         |Moins de features que Trivy   |
|Scan images       |Snyk Container   |Freemium      |Scan + monitoring continu               |Plan gratuit limité           |
|Signature         |Cosign (Sigstore)|Gratuit       |Signature et vérification d’images      |Nécessite une PKI ou Fulcio   |
|SBOM              |Syft             |Gratuit       |Génération de SBOM                      |—                             |
|Registry          |Harbor           |Gratuit       |Registry privé avec scan intégré        |Auto-hébergé (maintenance)    |
|Registry          |Docker Hub       |Freemium      |Registry public                         |Pull rate limit               |
|Orchestration     |Kubernetes       |Gratuit       |Orchestration de containers             |Complexité opérationnelle     |
|K8s local         |minikube         |Gratuit       |Cluster K8s local                       |Un seul nœud                  |
|K8s managé        |EKS/AKS/GKE      |Payant        |K8s en production                       |Coût cloud                    |
|Monitoring        |Prometheus       |Gratuit       |Métriques et alertes                    |Stockage long terme limité    |
|Dashboards        |Grafana          |Gratuit (OSS) |Visualisation                           |—                             |
|Logs              |Loki             |Gratuit       |Centralisation des logs                 |Moins riche qu’Elasticsearch  |
|Détection runtime |Falco            |Gratuit       |Détection d’anomalies containers        |Règles à maintenir            |
|Détection eBPF    |Tetragon         |Gratuit       |Observabilité et sécurité kernel        |Récent, écosystème jeune      |
|Audit K8s         |kube-bench       |Gratuit       |CIS Kubernetes Benchmark                |Audit ponctuel                |
|Admission         |Kyverno          |Gratuit       |Politiques de sécurité K8s              |—                             |
|Admission         |OPA/Gatekeeper   |Gratuit       |Politiques de sécurité K8s (Rego)       |Langage Rego à apprendre      |
|GitOps            |ArgoCD           |Gratuit       |Synchronisation Git → K8s               |Configuration initiale        |
|Service Mesh      |Istio            |Gratuit       |mTLS, observabilité, routing            |Complexe, overhead performance|
|CLI K8s           |k9s              |Gratuit       |Terminal interactif K8s                 |—                             |
|Lint Dockerfile   |Hadolint         |Gratuit       |Vérification bonnes pratiques Dockerfile|—                             |

-----

### Annexe D — Templates opérationnels

#### Dockerfile de production (Python)

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --no-log-init --shell /bin/false appuser
COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app.wsgi:application"]
```

#### Network Policy — Default Deny

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

#### Checklist de sécurité container

- [ ] Images officielles ou registry privé uniquement
- [ ] Scan Trivy : 0 CVE critique/haute
- [ ] Image signée avec Cosign
- [ ] Utilisateur non-root (`USER` dans Dockerfile, `runAsNonRoot` dans K8s)
- [ ] Capabilities : `drop ALL`, ajouter uniquement le nécessaire
- [ ] Filesystem read-only (`readOnlyRootFilesystem: true`)
- [ ] Secrets dans un vault externe (pas en base64 dans K8s)
- [ ] Network Policies en default deny
- [ ] RBAC : moindre privilège (pas de cluster-admin sauf admins)
- [ ] Service Account : `automountServiceAccountToken: false` sauf besoin
- [ ] Resource requests et limits définis
- [ ] Probes liveness et readiness configurées
- [ ] Logs centralisés (pas dans le container)
- [ ] Monitoring et alertes actifs (Prometheus)
- [ ] Détection runtime (Falco)
- [ ] API Server non exposé sur Internet
- [ ] Audit logs K8s activés

-----

### Annexe E — Ressources et formation

#### Labs gratuits

|Ressource                                       |Usage                                       |
|------------------------------------------------|--------------------------------------------|
|**Killercoda** (killercoda.com)                 |Exercices K8s interactifs dans le navigateur|
|**Play with Docker** (labs.play-with-docker.com)|Lab Docker en ligne gratuit                 |
|**Play with K8s** (labs.play-with-k8s.com)      |Lab K8s en ligne gratuit                    |
|**KodeKloud**                                   |Cours et labs K8s (certains gratuits)       |

#### Certifications

|Certification|Prérequis             |Format                 |Coût (~)|
|-------------|----------------------|-----------------------|--------|
|CKA          |Expérience K8s basique|Pratique (2h, terminal)|~395 USD|
|CKAD         |Expérience K8s basique|Pratique (2h, terminal)|~395 USD|
|CKS          |CKA valide            |Pratique (2h, terminal)|~395 USD|

#### Livres

- *Kubernetes Up & Running* (Hightower, Burns, Beda) — la référence pour démarrer
- *Container Security* (Liz Rice) — excellent pour le volet sécurité

#### Conférences

- **KubeCon + CloudNativeCon** — la conférence de référence (vidéos gratuites sur YouTube)
- **Docker Con** — conférence Docker

-----

### Annexe F — Hardening checklist par priorité

#### P0 — Quick wins (immédiat)

- Utilisateur non-root dans tous les containers
- Scanner toutes les images avec Trivy
- Supprimer les montages de Docker socket
- Ne pas utiliser `latest` en production
- Mettre des resource limits sur tous les Pods

#### P1 — Fondations (1-3 mois)

- Registry privé avec scan intégré
- Network Policies (default deny)
- RBAC minimal (supprimer les cluster-admin inutiles)
- Secrets dans un vault externe
- Monitoring et alertes (Prometheus + Grafana)
- Logs centralisés

#### P2 — Hardening avancé (3-6 mois)

- Signature d’images (Cosign) + admission controller
- Pod Security Standards (Restricted)
- Seccomp profiles
- Détection runtime (Falco)
- Audit logs K8s
- Service mesh (mTLS inter-services)

-----

### Annexe G — Mapping de la bibliothèque

|Thématique                                       |Cours principal   |Ce cours                                        |
|-------------------------------------------------|------------------|------------------------------------------------|
|Infrastructure IT (virtualisation, réseau, cloud)|**Cours Infra IT**|Fondations (Ch.1-2), réseau (Ch.5, 24)          |
|Sécurité applicative (vulnérabilités, DevSecOps) |**Cours AppSec**  |Images (Ch.7, 22), pipeline (Ch.17)             |
|Détection SOC                                    |**Cours SOC**     |Logs containers → SIEM (Ch.18, 26)              |
|Incident Response                                |**Cours IR**      |Forensic container (Ch.26)                      |
|Digital Forensic                                 |**Cours Forensic**|Analyse de layers, capture d’état (Ch.26)       |
|CTI                                              |**Cours CTI**     |Supply chain d’images comme vecteur (Ch.9, 22)  |
|Active Directory                                 |**Cours AD**      |Containers dans les environnements AD (contexte)|
|Linux (scripting Bash)                           |**Cours Bash**    |Namespaces, cgroups, kernel (Ch.2)              |
|Python (scripting)                               |**Cours Python**  |Dockerfile Python, automatisation (Ch.6, 12)    |

-----


## Annexe — Questions types d'entretien et réponses types

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
