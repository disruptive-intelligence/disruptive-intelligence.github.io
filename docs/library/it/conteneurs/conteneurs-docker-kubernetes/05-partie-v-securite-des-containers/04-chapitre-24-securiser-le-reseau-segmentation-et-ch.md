---
title: 'Chapitre 24 — Sécuriser le réseau : segmentation et chiffrement'
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

## Le minimum à savoir

### Le réseau K8s par défaut est PLAT

Par défaut dans Kubernetes, **tous les Pods peuvent communiquer avec tous les Pods**, dans tous les namespaces. C’est exactement comme un réseau d’entreprise sans aucune segmentation — si un attaquant compromet un Pod, il peut atteindre tous les autres.

### Network Policies : le pare-feu de K8s

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

### Le service mesh (avancé)

Pour aller plus loin : un **service mesh** (Istio, Linkerd) ajoute automatiquement le **mTLS** (chiffrement mutuel) entre tous les services. Chaque communication inter-Pod est chiffrée sans modification du code applicatif.

## ✅ Tu sais maintenant…

- Le réseau K8s est plat par défaut (pas de segmentation)
- Les Network Policies pour segmenter (default deny + règles explicites)
- Le service mesh pour le chiffrement inter-services (mTLS)

-----
