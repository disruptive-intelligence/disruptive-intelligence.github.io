---
title: 'Chapitre 17 — CI/CD et containers : du code au déploiement'
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie IV — Opérations ET cycle de vie
  - index.md
---

## Le minimum à savoir

### Le pipeline containerisé

En production, personne ne fait `docker build` et `kubectl apply` manuellement. Un **pipeline CI/CD** automatise tout le processus :

```
Code pushé   →   Build de    →   Scan de     →   Push au    →   Déploiement
sur Git          l'image         sécurité        registry       sur K8s
```


Chaque étape est automatisée. Si le scan de sécurité trouve une CVE critique, le pipeline s’arrête et le déploiement n’a pas lieu.

### Les outils CI/CD courants

|Outil             |Particularité                                 |
|------------------|----------------------------------------------|
|**GitHub Actions**|Intégré à GitHub, gratuit pour l’open source  |
|**GitLab CI**     |Intégré à GitLab, très populaire en entreprise|
|**Jenkins**       |Le vétéran, auto-hébergé, très configurable   |

### Exemple de pipeline GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - scan
  - deploy

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

scan:
  stage: scan
  script:
    - trivy image --exit-code 1 --severity CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy:
  stage: deploy
  script:
    - kubectl set image deployment/web web=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main
```


### Les secrets dans la CI/CD

> **⚠️ Piège majeur :** ne JAMAIS mettre de secrets (mots de passe, clés API, tokens) en clair dans les fichiers de pipeline, les Dockerfiles, ou les variables d’environnement du dépôt Git.

Les solutions :

- Variables protégées de la CI (GitLab CI Protected Variables, GitHub Secrets)
- Vault externe (HashiCorp Vault, AWS Secrets Manager)
- OIDC pour l’authentification au registry (pas de mot de passe stocké)

## Bonus

### GitOps : Git comme source de vérité

Le principe GitOps : l’état du cluster Kubernetes est décrit dans un repo Git. Un outil (**ArgoCD**, **Flux**) surveille ce repo et synchronise automatiquement le cluster avec ce qui est décrit dans Git. Pour déployer, tu fais un commit dans Git — l’outil applique les changements.

Avantages : audit trail complet (chaque déploiement est un commit), rollback par revert Git, review des changements de configuration par merge request. C’est le modèle vers lequel la plupart des organisations matures convergent, mais il n’est pas indispensable pour commencer.

### Les stratégies de déploiement avancées

|Stratégie                      |Comment                                    |Avantage                  |Inconvénient                           |
|-------------------------------|-------------------------------------------|--------------------------|---------------------------------------|
|**Rolling update** (défaut K8s)|Remplacement progressif des Pods           |Pas d’interruption        |Les deux versions coexistent brièvement|
|**Blue/Green**                 |Deux environnements complets, bascule      |Rollback instantané       |Double les ressources                  |
|**Canary**                     |Nouvelle version sur un % du trafic d’abord|Teste en production réelle|Plus complexe à configurer             |

## ✅ Tu sais maintenant…

- Le pipeline CI/CD containerisé (build → scan → push → deploy)
- Les secrets dans la CI/CD (jamais en clair)
- Le concept de GitOps (Git comme source de vérité)
- Les stratégies de déploiement (rolling, blue/green, canary)

-----
