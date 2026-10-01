---
title: 'Chapitre 25 — Sécuriser Kubernetes : RBAC, Secrets et API Server'
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

## Le minimum à savoir

### Le RBAC (Role-Based Access Control)

Le RBAC contrôle **qui peut faire quoi** dans le cluster.

|Objet                 |Portée         |Rôle                                               |
|----------------------|---------------|---------------------------------------------------|
|**Role**              |Un namespace   |Permissions dans un namespace                      |
|**ClusterRole**       |Tout le cluster|Permissions globales                               |
|**RoleBinding**       |Un namespace   |Lie un utilisateur/service account à un Role       |
|**ClusterRoleBinding**|Tout le cluster|Lie un utilisateur/service account à un ClusterRole|

```yaml
# Un Role qui permet de lire les Pods dans le namespace "staging"
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: staging
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```


> **⚠️ Le piège :** le ClusterRoleBinding `cluster-admin` donne **tous les droits sur tout le cluster**. C’est souvent attribué par défaut à tous les développeurs par commodité — c’est l’équivalent de donner root à tout le monde.

> **À retenir pour un entretien :** “Le RBAC dans Kubernetes fonctionne par le principe de moindre privilège : chaque utilisateur et chaque service account ne doit avoir que les permissions strictement nécessaires. Le cluster-admin ne devrait être attribué qu’aux administrateurs du cluster.”

### Les Service Accounts

Chaque Pod a un **Service Account** (SA) qui lui donne des droits sur l’API K8s. Par défaut :

- Un SA `default` est automatiquement créé dans chaque namespace
- Le token du SA est automatiquement monté dans chaque Pod
- Ce token permet d’appeler l’API Server depuis le Pod

**Le risque :** si un attaquant compromet un Pod avec un SA trop permissif, il peut utiliser le token pour lire des Secrets, créer des Pods, ou même prendre le contrôle du cluster.

**La remédiation :**

```yaml
spec:
  automountServiceAccountToken: false   # Ne pas monter le token automatiquement
```


### Les Secrets : le vrai problème

Rappel : les Secrets K8s sont en **base64, pas chiffrés**. Les remédiations :

1. **Chiffrement au repos :** configurer le chiffrement d’etcd (EncryptionConfiguration) pour que les Secrets soient chiffrés sur disque
1. **Vault externe :** utiliser HashiCorp Vault, AWS Secrets Manager, ou Azure Key Vault via External Secrets Operator — les secrets ne sont jamais stockés dans K8s
1. **Rotation :** les secrets doivent pouvoir être changés sans redéploiement

### L’API Server : le point de contrôle

L’API Server est le point d’entrée unique du cluster. Le sécuriser est prioritaire :

- **Ne jamais l’exposer sur Internet** sans authentification
- **Audit logs :** activer les logs d’audit pour tracer qui fait quoi
- **Authentification :** OIDC (SSO), certificats clients — pas de tokens statiques

### Les outils d’audit

```bash
# kube-bench — vérifie le cluster contre le CIS Kubernetes Benchmark
docker run --rm -v /etc:/node/etc -v /var:/node/var aquasec/kube-bench

# kubeaudit — audite les manifests et les configurations
kubeaudit all
```


> **📋 CONTAINER — Épisode 9 (partie 2)**
> 
> Audit de sécurité du cluster EKS de MedFlow. Résultats : 3 service accounts avec `cluster-admin` (dont 2 inutiles), pas de Network Policies, Secrets en base64 sans chiffrement etcd, audit logs désactivés. Plan de remédiation : réduire les RBAC au strict nécessaire, activer les Network Policies (default deny), migrer les secrets vers AWS Secrets Manager via External Secrets Operator, activer les audit logs.

## ✅ Tu sais maintenant…

- Le RBAC (Role, ClusterRole, RoleBinding — moindre privilège)
- Les Service Accounts et leurs risques (token monté par défaut)
- Les Secrets K8s (base64, pas chiffrés — vault externe recommandé)
- La sécurité de l’API Server (pas d’exposition Internet, audit logs)
- Les outils d’audit (kube-bench, kubeaudit)

## 💬 Questions d’entretien typiques

- **Comment fonctionne le RBAC dans Kubernetes ?** → K8s utilise des Roles (permissions dans un namespace) et ClusterRoles (permissions globales), liés à des utilisateurs ou Service Accounts via des Bindings. Le principe est le moindre privilège — chaque identité ne doit avoir que les droits strictement nécessaires.
- **Pourquoi les Secrets Kubernetes ne sont-ils pas suffisants seuls ?** → Parce qu’ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC adéquats ou tout accès à etcd insuffisamment protégé peut les lire en clair. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe (HashiCorp Vault, AWS Secrets Manager).
- **Qu’est-ce qu’un Service Account et pourquoi est-ce un risque ?** → Chaque Pod a un Service Account avec un token API monté automatiquement. Si un attaquant compromet le Pod et que le SA a des droits excessifs, il peut utiliser le token pour interagir avec l’API Server (lire des Secrets, créer des Pods, etc.). La remédiation : désactiver le montage automatique du token et appliquer le moindre privilège.

-----
