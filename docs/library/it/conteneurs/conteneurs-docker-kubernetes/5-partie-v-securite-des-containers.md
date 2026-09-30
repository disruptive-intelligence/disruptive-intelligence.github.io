---
title: PARTIE V — SÉCURITÉ DES CONTAINERS
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 5
chapters: 7
---

-----


## Chapitre 21 — Surface d’attaque des containers : comprendre les risques

### Le minimum à savoir

#### Le modèle de menaces

La sécurité des containers ne se résume pas à “scanner les images”. Il y a **6 surfaces d’attaque** à comprendre :

```
┌─────────────────────────────────────────────────┐
│                SUPPLY CHAIN                      │
│  Images malveillantes, dépendances compromises  │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              BUILD / CI/CD                       │
│  Secrets en clair, pipeline compromis            │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              RUNTIME                             │
│  Container escape, privilèges excessifs,         │
│  Docker socket exposé                            │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│           ORCHESTRATEUR (K8s)                    │
│  RBAC trop permissif, API Server exposé,         │
│  Secrets en clair dans etcd                      │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              RÉSEAU                              │
│  Pas de Network Policies → mouvement latéral     │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              DONNÉES                             │
│  Secrets, volumes, données sensibles             │
└─────────────────────────────────────────────────┘
```

#### Les 5 risques à connaître absolument

**1. Le container escape :** un attaquant sort du container pour atteindre la machine hôte. Rare mais catastrophique. Vecteurs : vulnérabilité kernel, Docker socket monté, capabilities SYS_ADMIN, hostPID/hostNetwork.

**2. Le Docker socket :** si un container a accès à `/var/run/docker.sock`, il peut créer de nouveaux containers avec des privilèges root sur l’hôte → **compromission totale de la machine**. C’est la faille la plus courante et la plus dangereuse en environnement container.

```bash
# ❌ JAMAIS en production
docker run -v /var/run/docker.sock:/var/run/docker.sock myapp
# → Ce container a un accès root sur la machine hôte
```

**3. L’exécution en root :** par défaut, les containers tournent en root (UID 0). Sans user namespace remapping ou mode rootless, cet UID 0 est le même que sur l’hôte. Les mécanismes d’isolation limitent ses pouvoirs, mais en cas de faille d’isolation ou de mauvaise configuration (capabilities excessives, volumes sensibles montés), l’impact peut être critique — jusqu’à la compromission de l’hôte.

**4. Les images non fiables :** une image Docker Hub communautaire peut contenir du code malveillant, des backdoors, des cryptominers. C’est la supply chain de l’image.

**5. Les Secrets en clair :** les Secrets K8s en base64, les variables d’environnement visibles dans `docker inspect`, les secrets dans les layers de l’image.

> **À retenir pour un entretien :** “Les principaux risques des containers sont : le container escape (sortir du container vers l’hôte), l’exécution en root, le Docker socket monté dans un container, les images non fiables (supply chain), et les secrets mal gérés. La mesure la plus impactante est de ne pas exécuter en root et de ne jamais monter le Docker socket.”

> **📋 CONTAINER — Épisode 8**
> 
> Pendant son audit, Sami découvre que le pipeline GitLab CI de MedFlow monte le Docker socket pour pouvoir construire des images Docker dans la CI. C’est une pratique courante mais dangereuse : n’importe quel job CI a un accès root sur le runner. Il remplace par kaniko (un outil de build d’images qui ne nécessite pas le Docker socket). Il découvre aussi que les secrets de production (clé API, mot de passe de la base de données) sont en clair dans les variables d’environnement GitLab CI, accessibles par tous les développeurs.

### Très utile en pratique

#### Checklist de sécurité rapide

|Risque                 |Vérification                                      |Remédiation                                        |
|-----------------------|--------------------------------------------------|---------------------------------------------------|
|Image non fiable       |D’où vient l’image ?                              |Images officielles + registry privé                |
|CVE dans l’image       |Scan Trivy/Grype                                  |Mettre à jour l’image de base                      |
|Exécution en root      |`docker inspect --format='{{.Config.User}}'`      |`USER nonroot` dans le Dockerfile                  |
|Docker socket monté    |`docker inspect` — vérifier les volumes           |Supprimer le montage                               |
|Capabilities excessives|`docker inspect --format='{{.HostConfig.CapAdd}}'`|`--cap-drop ALL --cap-add` uniquement le nécessaire|
|Secrets dans l’image   |`docker history` — vérifier les ARG/ENV           |Multi-stage build, vault externe                   |
|Secrets K8s en base64  |`kubectl get secret -o yaml`                      |Chiffrement etcd + vault externe                   |
|Pas de Network Policies|`kubectl get networkpolicies`                     |Default deny + ouverture sélective                 |
|RBAC trop permissif    |`kubectl get clusterrolebindings`                 |Principe de moindre privilège                      |
|API Server exposé      |Vérifier l’accès réseau                           |Firewall, authentification, audit logs             |

### ✅ Tu sais maintenant…

- Les 6 surfaces d’attaque des containers
- Les 5 risques à connaître (escape, Docker socket, root, images, secrets)
- La checklist de sécurité rapide

### 💬 Questions d’entretien typiques

- **Pourquoi le Docker socket est-il dangereux ?** → Le Docker socket (`/var/run/docker.sock`) permet de contrôler le daemon Docker. Si un container y a accès, il peut créer de nouveaux containers avec des privilèges root sur l’hôte — c’est une compromission totale de la machine.
- **Qu’est-ce qu’un container escape ?** → C’est quand un attaquant sort de l’isolation du container pour atteindre la machine hôte. Les vecteurs incluent des vulnérabilités kernel, des capabilities excessives (SYS_ADMIN), ou un Docker socket monté. C’est rare mais l’impact est maximal.
- **Quels sont les principaux risques de sécurité des containers ?** → Le Docker socket exposé, l’exécution en root, les images non fiables (supply chain), les secrets mal gérés (base64 dans K8s), et l’absence de segmentation réseau (Network Policies).

-----


## Chapitre 22 — Sécuriser les images : de la construction au déploiement

### Le minimum à savoir

#### Les 4 piliers de la sécurité des images

**1. Choisir la bonne base :** images officielles, versions `slim` ou `distroless`, éviter les images communautaires non vérifiées.

**2. Scanner :** Trivy, Grype, Snyk — automatisé dans le pipeline CI, bloquer les CVE critiques.

**3. Signer :** Cosign (Sigstore) — prouver que l’image vient de ta CI et n’a pas été modifiée.

**4. Contrôler l’admission :** OPA/Gatekeeper ou Kyverno — empêcher le déploiement d’images non signées ou non scannées sur le cluster K8s.

#### Politique d’images en entreprise

```
Développeur construit  →  CI scanne  →  CI signe  →  Push au   →  K8s vérifie
l'image                   avec Trivy    avec Cosign   registry     la signature
                              ↓                                      ↓
                        CVE critique ?                        Signature valide ?
                              ↓                                      ↓
                          OUI → BLOQUÉ                       NON → REFUSÉ
                          NON → OK                           OUI → DÉPLOYÉ
```

> **📋 CONTAINER — Épisode 9 (partie 1)**
> 
> Sami met en place la politique d’images MedFlow : registry privé Harbor, scan Trivy dans la CI (0 CVE critical/high pour passer), signature Cosign, et un admission webhook Kyverno qui refuse toute image non signée. Un développeur essaie de déployer une image Docker Hub → refusé. Sami lui explique le workflow : “on ne bloque pas le travail, on fournit les images validées.”

### ✅ Tu sais maintenant…

- Les 4 piliers : base fiable, scan, signature, contrôle d’admission
- Le workflow de sécurité des images en entreprise

-----


## Chapitre 23 — Sécuriser le runtime : isolation et contrôle d’exécution

### Le minimum à savoir

#### Les 4 mesures essentielles

**1. Utilisateur non-root :** `USER nonroot` dans le Dockerfile, `runAsNonRoot: true` dans le Pod spec K8s.

**2. Capabilities minimales :** `--cap-drop ALL` puis `--cap-add` uniquement ce qui est nécessaire. En K8s : Pod Security Standards.

**3. Read-only filesystem :** `readOnlyRootFilesystem: true` dans le Pod spec — le container ne peut rien écrire sur son filesystem (sauf les volumes montés).

**4. Pod Security Standards (K8s) :** trois niveaux — Privileged (aucune restriction), Baseline (restrictions minimales), Restricted (hardening strict).

```yaml
# Pod spec durci
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
  containers:
  - name: web
    image: mon_app:1.0.0
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

> **À retenir pour un entretien :** “Pour sécuriser le runtime, les mesures essentielles sont : exécuter en non-root, supprimer toutes les capabilities Linux sauf celles nécessaires, monter le filesystem en lecture seule, et appliquer les Pod Security Standards restricted.”

### Très utile en pratique

#### Falco : la détection runtime

**Falco** (CNCF) surveille les containers en temps réel et détecte les comportements anormaux :

- Un shell est lancé dans un container de production
- Un processus lit `/etc/shadow`
- Une connexion réseau sortante vers une IP suspecte
- Un fichier est écrit dans `/usr/bin/`

C’est l’IDS (système de détection d’intrusion) pour les containers.

#### Docker rootless et user namespace remapping

Au-delà du `USER nonroot` dans le Dockerfile, deux mécanismes renforcent l’isolation au niveau de l’hôte :

**Docker en mode rootless** : le daemon Docker lui-même tourne sans root. L’avantage est fondamental : même une faille dans le daemon Docker ne donne pas root sur l’hôte. Docker rootless est supporté depuis Docker 20.10+ mais nécessite une configuration spécifique. **Podman** fonctionne nativement en rootless.

**User namespace remapping** : le UID 0 (root) dans le container est mappé vers un UID non privilégié sur l’hôte (par exemple 100000). Même si un attaquant est root dans le container, il est un utilisateur sans privilège sur l’hôte. C’est une couche de défense en profondeur. Configuration dans `/etc/docker/daemon.json` :

```json
{
  "userns-remap": "default"
}
```

> **En résumé :** `USER nonroot` dans le Dockerfile empêche l’application de tourner en root dans le container. Le user namespace remapping empêche root dans le container d’être root sur l’hôte. Docker rootless empêche le daemon lui-même de tourner en root. Ce sont 3 couches de défense complémentaires.

Ces mécanismes ne sont pas magiques — ils ont des contraintes (compatibilité avec certains volumes, certains réseaux, performance). Mais pour les environnements où la sécurité est une priorité, ils réduisent significativement le risque de container escape.

### ✅ Tu sais maintenant…

- Les 4 mesures de hardening runtime (non-root, capabilities, read-only, PSS)
- Falco pour la détection d’anomalies en runtime
- Docker rootless et user namespace remapping comme couches de défense supplémentaires

### 💬 Questions d’entretien typiques

- **Comment sécuriser le runtime d’un container ?** → Exécuter en non-root (USER dans le Dockerfile + runAsNonRoot dans K8s), supprimer toutes les capabilities (cap-drop ALL), filesystem read-only, et appliquer les Pod Security Standards restricted.
- **Qu’est-ce que le user namespace remapping ?** → C’est un mécanisme qui mappe le UID 0 (root) du container vers un UID non privilégié sur l’hôte. Même si un attaquant devient root dans le container, il est un utilisateur sans privilège sur la machine hôte.
- **Quelle est la différence entre Docker classique et Docker rootless ?** → En Docker classique, le daemon tourne en root — un accès au Docker socket donne l’équivalent de root sur l’hôte. En rootless, le daemon tourne sans root, ce qui réduit l’impact d’une compromission du daemon.

-----


## Chapitre 24 — Sécuriser le réseau : segmentation et chiffrement

### Le minimum à savoir

#### Le réseau K8s par défaut est PLAT

Par défaut dans Kubernetes, **tous les Pods peuvent communiquer avec tous les Pods**, dans tous les namespaces. C’est exactement comme un réseau d’entreprise sans aucune segmentation — si un attaquant compromet un Pod, il peut atteindre tous les autres.

#### Network Policies : le pare-feu de K8s

Les **Network Policies** sont les règles de firewall de Kubernetes. Elles contrôlent quels Pods peuvent communiquer entre eux.

```yaml
# Default deny — RIEN ne communique sauf ce qui est explicitement autorisé
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}      # S'applique à TOUS les pods du namespace
  policyTypes:
  - Ingress
  - Egress
```

```yaml
# Autoriser le trafic web → db uniquement
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-to-db
spec:
  podSelector:
    matchLabels:
      app: db
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: web
    ports:
    - port: 5432
```

> **Important :** les Network Policies ne fonctionnent que si le CNI (Container Network Interface) du cluster les supporte. **Calico** et **Cilium** les supportent. Le CNI par défaut de certains services managés ne les supporte pas toujours — vérifie.

#### Le service mesh (avancé)

Pour aller plus loin : un **service mesh** (Istio, Linkerd) ajoute automatiquement le **mTLS** (chiffrement mutuel) entre tous les services. Chaque communication inter-Pod est chiffrée sans modification du code applicatif.

### ✅ Tu sais maintenant…

- Le réseau K8s est plat par défaut (pas de segmentation)
- Les Network Policies pour segmenter (default deny + règles explicites)
- Le service mesh pour le chiffrement inter-services (mTLS)

-----


## Chapitre 25 — Sécuriser Kubernetes : RBAC, Secrets et API Server

### Le minimum à savoir

#### Le RBAC (Role-Based Access Control)

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

#### Les Service Accounts

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

#### Les Secrets : le vrai problème

Rappel : les Secrets K8s sont en **base64, pas chiffrés**. Les remédiations :

1. **Chiffrement au repos :** configurer le chiffrement d’etcd (EncryptionConfiguration) pour que les Secrets soient chiffrés sur disque
1. **Vault externe :** utiliser HashiCorp Vault, AWS Secrets Manager, ou Azure Key Vault via External Secrets Operator — les secrets ne sont jamais stockés dans K8s
1. **Rotation :** les secrets doivent pouvoir être changés sans redéploiement

#### L’API Server : le point de contrôle

L’API Server est le point d’entrée unique du cluster. Le sécuriser est prioritaire :

- **Ne jamais l’exposer sur Internet** sans authentification
- **Audit logs :** activer les logs d’audit pour tracer qui fait quoi
- **Authentification :** OIDC (SSO), certificats clients — pas de tokens statiques

#### Les outils d’audit

```bash
# kube-bench — vérifie le cluster contre le CIS Kubernetes Benchmark
docker run --rm -v /etc:/node/etc -v /var:/node/var aquasec/kube-bench

# kubeaudit — audite les manifests et les configurations
kubeaudit all
```

> **📋 CONTAINER — Épisode 9 (partie 2)**
> 
> Audit de sécurité du cluster EKS de MedFlow. Résultats : 3 service accounts avec `cluster-admin` (dont 2 inutiles), pas de Network Policies, Secrets en base64 sans chiffrement etcd, audit logs désactivés. Plan de remédiation : réduire les RBAC au strict nécessaire, activer les Network Policies (default deny), migrer les secrets vers AWS Secrets Manager via External Secrets Operator, activer les audit logs.

### ✅ Tu sais maintenant…

- Le RBAC (Role, ClusterRole, RoleBinding — moindre privilège)
- Les Service Accounts et leurs risques (token monté par défaut)
- Les Secrets K8s (base64, pas chiffrés — vault externe recommandé)
- La sécurité de l’API Server (pas d’exposition Internet, audit logs)
- Les outils d’audit (kube-bench, kubeaudit)

### 💬 Questions d’entretien typiques

- **Comment fonctionne le RBAC dans Kubernetes ?** → K8s utilise des Roles (permissions dans un namespace) et ClusterRoles (permissions globales), liés à des utilisateurs ou Service Accounts via des Bindings. Le principe est le moindre privilège — chaque identité ne doit avoir que les droits strictement nécessaires.
- **Pourquoi les Secrets Kubernetes ne sont-ils pas suffisants seuls ?** → Parce qu’ils sont encodés en base64, pas chiffrés. Toute identité avec les droits RBAC adéquats ou tout accès à etcd insuffisamment protégé peut les lire en clair. En production, il faut chiffrer etcd au repos et/ou utiliser un vault externe (HashiCorp Vault, AWS Secrets Manager).
- **Qu’est-ce qu’un Service Account et pourquoi est-ce un risque ?** → Chaque Pod a un Service Account avec un token API monté automatiquement. Si un attaquant compromet le Pod et que le SA a des droits excessifs, il peut utiliser le token pour interagir avec l’API Server (lire des Secrets, créer des Pods, etc.). La remédiation : désactiver le montage automatique du token et appliquer le moindre privilège.

-----


## Chapitre 26 — Détection et réponse aux incidents dans les containers

### Le minimum à savoir

#### Le défi de l’éphémérité

Les containers meurent et renaissent en permanence. Un container compromis peut être détruit et recréé par K8s en quelques secondes — **les preuves disparaissent**. Sans externalisation des logs et des métriques, le forensic est impossible.

#### La détection runtime

**Falco** (CNCF) est l’outil de référence pour la détection d’anomalies dans les containers :

```yaml
# Exemples de règles Falco
- rule: Terminal shell in container
  desc: Détecte l'ouverture d'un shell dans un container
  condition: container and proc.name in (bash, sh, zsh)
  output: "Shell ouvert dans le container (user=%user.name container=%container.name)"
  priority: WARNING
```

#### La réponse

1. **Isoler :** appliquer une Network Policy deny all sur le Pod compromis (coupure réseau immédiate)
1. **Capturer :** sauvegarder l’état du container avant sa destruction (`kubectl cp`, export des logs, snapshot du volume)
1. **Analyser :** examiner les logs K8s, les audit logs de l’API Server, les alertes Falco, corréler avec les logs applicatifs centralisés
1. **Remédier :** corriger la vulnérabilité, mettre à jour l’image, renforcer les politiques

#### Les indicateurs de compromission (IoC) spécifiques aux containers

- Processus non attendu dans le container (shell, wget, curl, netcat)
- Connexions réseau sortantes vers des IPs/domaines inconnus
- Écriture dans des répertoires système (`/usr/bin`, `/etc`)
- Tentative de montage de volumes non autorisés
- Utilisation de capabilities inhabituelles
- Appels API K8s depuis un Pod applicatif

### ✅ Tu sais maintenant…

- Le défi de l’éphémérité pour le forensic
- Falco pour la détection runtime
- La démarche de réponse (isoler → capturer → analyser → remédier)
- Les IoC spécifiques aux containers

-----
