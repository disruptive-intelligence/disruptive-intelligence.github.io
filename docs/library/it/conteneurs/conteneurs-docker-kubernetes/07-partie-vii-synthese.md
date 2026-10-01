---
title: Partie VII — Synthèse
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - index.md
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
