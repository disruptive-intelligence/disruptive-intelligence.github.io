---
title: Chapitre 9 — Registries et gestion des images
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie II — Construire et composer
  - index.md
---

## Le minimum à savoir

### Qu’est-ce qu’un registry ?

Un registry est un **entrepôt d’images Docker**. C’est là que les images sont stockées, versionnées et distribuées. Le registry le plus connu est **Docker Hub**, mais en entreprise, on utilise un **registry privé**.

### Pourquoi un registry privé ?

- **Sécurité :** tu contrôles ce qui entre et sort — pas d’images communautaires non vérifiées
- **Confidentialité :** tes images d’application ne sont pas publiques
- **Performance :** pas de pull rate limit, le registry est sur ton réseau
- **Conformité :** certaines réglementations exigent que les artefacts logiciels soient hébergés en interne

### Les options de registries privés

|Registry                               |Type                    |Particularité                                          |
|---------------------------------------|------------------------|-------------------------------------------------------|
|**Docker Hub** (plan payant)           |Cloud public            |Le plus connu, repos privés possibles                  |
|**Harbor**                             |Self-hosted, open source|Scan de vulnérabilités intégré (Trivy), signature, RBAC|
|**GitLab Container Registry**          |Intégré à GitLab        |Gratuit si tu utilises GitLab CI                       |
|**AWS ECR**                            |Cloud AWS               |Intégré à EKS, scan natif                              |
|**Azure ACR**                          |Cloud Azure             |Intégré à AKS                                          |
|**GCP Artifact Registry**              |Cloud GCP               |Intégré à GKE                                          |
|**GitHub Container Registry** (ghcr.io)|Cloud GitHub            |Intégré à GitHub Actions                               |

### Pousser une image vers un registry

```bash
# 1. Se connecter au registry
docker login registry.example.com

# 2. Tagger l'image avec le nom complet du registry
docker tag mon_app:latest registry.example.com/mon_equipe/mon_app:1.0.0

# 3. Pousser
docker push registry.example.com/mon_equipe/mon_app:1.0.0
```


Le format du nom d’une image complète :

```
registry.example.com / mon_equipe / mon_app : 1.0.0
       ↑                   ↑          ↑        ↑
    registry          namespace     image     tag
```


### La stratégie de tags

**Ne jamais utiliser `latest` en production.** Le tag `latest` change à chaque push — tu ne sais pas quelle version tourne.

Stratégies recommandées :

|Stratégie         |Exemple             |Usage               |
|------------------|--------------------|--------------------|
|Version sémantique|`mon_app:1.2.3`     |Releases officielles|
|SHA du commit Git |`mon_app:a3f2b1c`   |Chaque build CI     |
|Date              |`mon_app:2025-04-07`|Builds quotidiens   |


> **À retenir pour un entretien :** “En production, on utilise des tags de version spécifiques, jamais `latest`. Ça garantit que le déploiement est déterministe — on sait exactement quelle version tourne.”

## Très utile en pratique

### La supply chain des images

C’est un sujet de sécurité critique : **d’où viennent tes images ?**

Les risques :

- **Typosquatting :** une image `ngimx` (au lieu de `nginx`) qui contient du code malveillant
- **Image compromise :** une image communautaire légitime dont l’auteur a été compromis ou est malveillant
- **Image obsolète :** une image avec des CVE connues non corrigées

Les protections :

- N’utiliser que des images **officielles** ou **vérifiées** (badge sur Docker Hub)
- Scanner toutes les images avec **Trivy/Grype** avant déploiement
- Utiliser un **registry privé** qui met en cache les images officielles
- **Signer** les images avec **Cosign** (projet Sigstore) et vérifier les signatures avant déploiement

### Cosign : signer et vérifier les images

```bash
# Installer cosign
# (voir https://docs.sigstore.dev/cosign/installation/)

# Signer une image
cosign sign registry.example.com/mon_app:1.0.0

# Vérifier la signature
cosign verify registry.example.com/mon_app:1.0.0
```


En combinant signature + admission controller K8s (voir chapitre 22), tu peux empêcher le déploiement de toute image non signée.

## Bonus

### Le SBOM (Software Bill of Materials)

Un SBOM est l’**inventaire complet** de tous les composants logiciels d’une image (packages système, bibliothèques, dépendances). C’est l’équivalent d’une liste d’ingrédients pour une image Docker.

```bash
# Générer un SBOM avec Syft
syft mon_app:latest

# Docker a un SBOM intégré
docker sbom mon_app:latest
```


Quand une CVE critique est annoncée (type Log4Shell), le SBOM te permet de savoir instantanément quels containers sont affectés.

## ✅ Tu sais maintenant…

- Ce qu’est un registry et pourquoi utiliser un registry privé
- Pousser une image vers un registry (`tag` + `push`)
- La stratégie de tags (jamais `latest` en production)
- Les risques de supply chain des images et les protections (scan, signature, SBOM)

-----
