---
title: Partie VI — Cloud, containers et architectures modernes
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

*L'infrastructure moderne — ce qui remplace progressivement le datacenter on-premise.*

---


## Chapitre 25 — Cloud : modèles, architecture et responsabilité partagée

Les 3 modèles : **IaaS** (le provider gère hardware/réseau/virtualisation, vous gérez OS/middleware/app/données — AWS EC2, Azure VM, GCP Compute), **PaaS** (le provider gère aussi OS/middleware/runtime, vous gérez app/données — Heroku, Azure App Service), **SaaS** (le provider gère tout, vous gérez la configuration et les données — Office 365, Salesforce, Slack). Le **Shared Responsibility Model** est la source n°1 de confusion : le provider est responsable de la sécurité DU cloud (infrastructure), vous êtes responsable de la sécurité DANS le cloud (configuration, accès, données). La majorité des brèches cloud viennent de mauvaises configurations (S3 buckets publics, IAM trop permissif, security groups ouverts).

Les concepts cloud transversaux : régions et zones de disponibilité (résilience géographique), VPC/VNet (réseau virtuel isolé — votre réseau privé dans le cloud), security groups/NSG (filtrage réseau cloud — l'équivalent du firewall), stockage objet (S3/Azure Blob/GCS). L'architecture cloud type (VPC multi-tiers : subnet public → load balancer → subnet privé → application → subnet privé → base de données, NAT gateway pour le trafic sortant, bastion cloud pour l'administration).

Les **erreurs de configuration** les plus courantes : S3 bucket public (données exposées sur Internet), security group 0.0.0.0/0 sur SSH (le serveur est accessible depuis n'importe où), IAM trop permissif (AdministratorAccess pour tout le monde), logs non activés (CloudTrail/Activity Log désactivés → aucune traçabilité), et chiffrement désactivé (données au repos en clair).

---


## Chapitre 26 — Sécurité cloud : services natifs et bonnes pratiques

Les services de sécurité natifs : **AWS** (GuardDuty — détection de menaces, Security Hub — posture, Config — conformité, CloudTrail — audit API, KMS — gestion des clés, IAM Access Analyzer — permissions excessives), **Azure** (Defender for Cloud — posture et détection, Sentinel — SIEM cloud-native, Key Vault — secrets et clés, Azure Policy — conformité), **GCP** (Security Command Center — posture, Cloud KMS — clés, VPC Service Controls — périmètre de données).

Le **CSPM** (Cloud Security Posture Management) vérifie automatiquement les configurations cloud contre les benchmarks (CIS, propriétaire) — détecte les S3 publics, les security groups ouverts, les IAM excessifs, les logs désactivés. La gestion des secrets (Key Vault, KMS, Secret Manager — ne jamais stocker de secrets dans le code, les variables d'environnement en clair, ou les fichiers Terraform). L'**IaC sécurisée** : Terraform state files contiennent des secrets → backend distant chiffré obligatoire (S3 + KMS, Azure Blob + encryption) ; scanning IaC (tfsec, checkov — détectent les erreurs de configuration avant le déploiement). Le cloud logging (CloudTrail, Azure Activity Log, GCP Cloud Audit Logs — les logs qu'il faut absolument activer et centraliser vers le SIEM).

---


## Chapitre 27 — Containers : Docker, Kubernetes et sécurité

*Traitement « socle » — les concepts et les risques fondamentaux, pas un cours DevSecOps complet.*

**Docker** : une image est un template read-only (construit depuis un Dockerfile), un container est une instance en exécution d'une image. Le registry (Docker Hub, registries privés — Harbor, GitLab Registry) stocke les images. La sécurité des images : utiliser des images officielles, scanner les vulnérabilités (Trivy, Snyk, Clair), et le risque de supply chain d'images (une image Docker Hub malveillante donne accès à tout ce que le container peut atteindre). L'isolation container vs VM : le container partage le kernel hôte → l'isolation est moins forte qu'une VM (namespaces et cgroups vs virtualisation matérielle). Le container escape est rare mais possible. Bonnes pratiques : utilisateur non-root dans le container, read-only filesystem, pas de capabilities inutiles, secrets via volume sécurisé (pas dans l'image), réseau isolé, registry privé. Le **Docker socket** (/var/run/docker.sock) : si le socket est monté dans un container → l'attaquant peut créer des containers avec des privilèges complets sur l'hôte → full host compromise.

**Kubernetes** : pods (la plus petite unité — 1+ containers), deployments (gestion du cycle de vie des pods), services (exposition réseau des pods), namespaces (isolation logique), ConfigMaps (configuration), Secrets (données sensibles — encodées en base64, PAS chiffrées par défaut → utiliser un KMS externe), Ingress (exposition HTTP/HTTPS externe). La sécurité K8s : **RBAC** (Role-Based Access Control — le mécanisme d'autorisation ; risque : cluster-admin attribué à tout le monde), **Network Policies** (segmentation réseau entre pods — par défaut, tous les pods peuvent communiquer entre eux), **Pod Security Standards** (baseline/restricted — restreindre les capabilities, forcer le non-root). Les risques majeurs : API server exposé sur Internet sans authentification, RBAC trop permissif, secrets en clair dans les ConfigMaps, images non vérifiées, et mouvement latéral entre pods (sans Network Policies, compromettre un pod = accéder à tous les pods du cluster). Le **service mesh** (Istio, Linkerd) ajoute le mTLS automatique entre tous les services, le rate limiting, et l'observabilité — couche d'infrastructure sécurité pour les microservices.

---


## Chapitre 28 — Architectures modernes

microservices, serverless et CI/CD

Les **microservices** : l'application est découpée en N services indépendants qui communiquent via API REST, gRPC, ou message queues. Chaque service a sa propre base de données et son propre cycle de déploiement. Avantage : scalabilité, résilience, agilité. Risque : surface d'attaque multipliée — chaque microservice est un point d'entrée potentiel, la communication inter-services doit être authentifiée et chiffrée.

Les **message brokers** : RabbitMQ (queue de messages AMQP — tâches asynchrones, découplage), Apache Kafka (streaming d'événements — big data, SIEM, événements temps réel), AWS SQS/Azure Service Bus (queues managées cloud). Risque : broker sans authentification ou avec des permissions trop larges → lecture/injection de messages.

Le **serverless** (AWS Lambda, Azure Functions, GCP Cloud Functions) : le développeur écrit une fonction, le provider gère tout le reste. Risques : permissions IAM trop larges sur les fonctions, injection dans les paramètres, secrets en variables d'environnement visibles dans la console.

Le **pipeline CI/CD** (Continuous Integration/Continuous Deployment) : GitHub Actions, GitLab CI, Jenkins, ArgoCD. Le pipeline compile, teste, et déploie le code automatiquement. C'est une **cible critique** : il a accès au code source, aux secrets de déploiement, et peut exécuter du code arbitraire. Supply chain attack via CI/CD : compromettre le pipeline = compromettre l'application en production (cf. cours APT — SolarWinds, 3CX).

**Git et sécurité** : les repos Git contiennent parfois des secrets commités par erreur (clés API, mots de passe, tokens). L'historique Git conserve tout — même un secret supprimé dans un commit ultérieur est récupérable (git log, git diff). Outils de détection : truffleHog, gitleaks, git-secrets.

---
