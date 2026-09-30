---
title: PARTIE IV — OPÉRATIONS ET CYCLE DE VIE
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
chapter: 4
chapters: 7
---

-----


## Chapitre 17 — CI/CD et containers : du code au déploiement

### Le minimum à savoir

#### Le pipeline containerisé

En production, personne ne fait `docker build` et `kubectl apply` manuellement. Un **pipeline CI/CD** automatise tout le processus :

```
Code pushé   →   Build de    →   Scan de     →   Push au    →   Déploiement
sur Git          l'image         sécurité        registry       sur K8s
```

Chaque étape est automatisée. Si le scan de sécurité trouve une CVE critique, le pipeline s’arrête et le déploiement n’a pas lieu.

#### Les outils CI/CD courants

|Outil             |Particularité                                 |
|------------------|----------------------------------------------|
|**GitHub Actions**|Intégré à GitHub, gratuit pour l’open source  |
|**GitLab CI**     |Intégré à GitLab, très populaire en entreprise|
|**Jenkins**       |Le vétéran, auto-hébergé, très configurable   |

#### Exemple de pipeline GitLab CI

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

#### Les secrets dans la CI/CD

> **⚠️ Piège majeur :** ne JAMAIS mettre de secrets (mots de passe, clés API, tokens) en clair dans les fichiers de pipeline, les Dockerfiles, ou les variables d’environnement du dépôt Git.

Les solutions :

- Variables protégées de la CI (GitLab CI Protected Variables, GitHub Secrets)
- Vault externe (HashiCorp Vault, AWS Secrets Manager)
- OIDC pour l’authentification au registry (pas de mot de passe stocké)

### Bonus

#### GitOps : Git comme source de vérité

Le principe GitOps : l’état du cluster Kubernetes est décrit dans un repo Git. Un outil (**ArgoCD**, **Flux**) surveille ce repo et synchronise automatiquement le cluster avec ce qui est décrit dans Git. Pour déployer, tu fais un commit dans Git — l’outil applique les changements.

Avantages : audit trail complet (chaque déploiement est un commit), rollback par revert Git, review des changements de configuration par merge request. C’est le modèle vers lequel la plupart des organisations matures convergent, mais il n’est pas indispensable pour commencer.

#### Les stratégies de déploiement avancées

|Stratégie                      |Comment                                    |Avantage                  |Inconvénient                           |
|-------------------------------|-------------------------------------------|--------------------------|---------------------------------------|
|**Rolling update** (défaut K8s)|Remplacement progressif des Pods           |Pas d’interruption        |Les deux versions coexistent brièvement|
|**Blue/Green**                 |Deux environnements complets, bascule      |Rollback instantané       |Double les ressources                  |
|**Canary**                     |Nouvelle version sur un % du trafic d’abord|Teste en production réelle|Plus complexe à configurer             |

### ✅ Tu sais maintenant…

- Le pipeline CI/CD containerisé (build → scan → push → deploy)
- Les secrets dans la CI/CD (jamais en clair)
- Le concept de GitOps (Git comme source de vérité)
- Les stratégies de déploiement (rolling, blue/green, canary)

-----


## Chapitre 18 — Monitoring, logs et observabilité

### Le minimum à savoir

#### Pourquoi centraliser les logs

Les containers sont éphémères. Quand un Pod est supprimé ou recréé, ses logs disparaissent. Sans centralisation, tu ne peux pas diagnostiquer un problème survenu il y a 30 minutes si le Pod a été recréé depuis.

**Convention containers :** les applications doivent logger sur **stdout/stderr** (pas dans des fichiers). Docker et Kubernetes captent automatiquement stdout/stderr.

```bash
# Voir les logs d'un Pod
kubectl logs mon-pod
kubectl logs -f mon-pod              # En temps réel
kubectl logs mon-pod --previous      # Logs de l'instance précédente (après un crash)
```

#### La stack de monitoring standard

Le standard de facto pour le monitoring Kubernetes :

- **Prometheus** : collecte les métriques (CPU, mémoire, latence, erreurs, métriques custom)
- **Grafana** : affiche les métriques dans des dashboards visuels
- **Loki** (ou EFK) : centralise les logs
- **AlertManager** : envoie des alertes (email, Slack, PagerDuty) quand un seuil est dépassé

#### Les métriques à surveiller

|Métrique                 |Pourquoi                                 |
|-------------------------|-----------------------------------------|
|CPU par Pod              |Détecter les surcharges                  |
|Mémoire par Pod          |Prévenir les OOMKilled                   |
|Nombre de Pods ready     |Vérifier que l’application est disponible|
|Taux d’erreurs HTTP (5xx)|Détecter les problèmes applicatifs       |
|Latence (p50, p95, p99)  |Détecter les ralentissements             |
|Restarts de Pods         |Détecter les crashs en boucle            |

#### Les outils du quotidien

```bash
# Voir les ressources consommées par les Pods
kubectl top pods
kubectl top nodes

# Le dashboard Kubernetes (interface web)
kubectl proxy
# → http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

# k9s — le terminal interactif pour K8s (très recommandé)
# Installer : https://k9scli.io/
k9s
```

> **⚠️ Sécurité :** le Kubernetes Dashboard exposé sans authentification est une vulnérabilité critique. Des clusters de production ont été compromis parce que le Dashboard était accessible sur Internet sans mot de passe. Toujours protéger par RBAC et authentification.

### ✅ Tu sais maintenant…

- Pourquoi centraliser les logs (éphémérité des containers)
- La stack Prometheus + Grafana pour le monitoring
- Les métriques clés à surveiller
- Les outils du quotidien (kubectl top, k9s, Dashboard — avec précaution)

-----


## Chapitre 19 — Troubleshooting containers et Kubernetes

### Le minimum à savoir

#### La démarche systématique

Quand un Pod ne fonctionne pas, suis cette démarche :

```
1. kubectl get pods           → Quel est l'état du Pod ? (Running, CrashLoopBackOff, Pending, Error)
2. kubectl describe pod X     → Quels événements ? Quelles erreurs ?
3. kubectl logs X             → Que dit l'application ?
4. kubectl exec -it X -- sh   → Explorer l'intérieur du container
```

#### Les états de Pod et leur signification

|État                |Signification                           |Action                                                      |
|--------------------|----------------------------------------|------------------------------------------------------------|
|**Running**         |Le Pod tourne                           |OK (mais vérifier les logs quand même)                      |
|**Pending**         |Le Pod attend d’être placé sur un nœud  |Vérifier les ressources disponibles, les taints/tolerations |
|**CrashLoopBackOff**|Le container plante en boucle           |`kubectl logs` pour voir l’erreur, `kubectl logs --previous`|
|**ImagePullBackOff**|L’image ne peut pas être téléchargée    |Vérifier le nom de l’image, les credentials du registry     |
|**OOMKilled**       |Le container a dépassé sa limite mémoire|Augmenter les limits ou optimiser l’application             |
|**Error**           |Le container s’est terminé en erreur    |`kubectl logs`                                              |
|**Terminating**     |Le Pod est en cours de suppression      |Vérifier les finalizers, les PVC                            |

#### Les problèmes les plus courants

**1. CrashLoopBackOff :**

```bash
kubectl logs mon-pod                  # Voir pourquoi ça plante
kubectl logs mon-pod --previous       # Logs de l'instance précédente
kubectl describe pod mon-pod          # Section "Events" en bas
```

**2. Le Service ne route pas le trafic :**

```bash
kubectl describe service web-service  # Vérifier "Endpoints" — si vide, les labels ne matchent pas
kubectl get endpoints web-service     # Doit lister les IPs des Pods
```

**3. Le Pod reste en Pending :**

```bash
kubectl describe pod mon-pod          # Section "Events" — souvent "Insufficient cpu/memory"
kubectl get nodes                     # Vérifier la capacité des nœuds
```

**4. OOMKilled :**

```bash
kubectl describe pod mon-pod          # "Last State: Terminated, Reason: OOMKilled"
# → Augmenter la limit mémoire ou optimiser l'application
```

> **📋 CONTAINER — Épisode 7**
> 
> Incident en staging : les pods Django redémarrent en boucle (CrashLoopBackOff). `kubectl describe pod` montre un OOMKilled — la limite mémoire est à 256 Mi, l’application en consomme 400 Mi sous charge. Sami augmente les limits à 512 Mi, ajoute des alertes Prometheus sur la consommation mémoire (alerte à 80% de la limit), et documente le seuil. L’incident est résolu en 15 minutes grâce à la démarche systématique.

### ✅ Tu sais maintenant…

- La démarche de troubleshooting (get → describe → logs → exec)
- Les états de Pod et leur signification
- Les problèmes les plus courants et comment les résoudre

-----


## Chapitre 20 — Capstone Partie IV : pipeline CI/CD et monitoring

Exercice intégrateur : mettre en place un pipeline CI/CD simplifié (build → scan Trivy → push → deploy sur minikube), ajouter un monitoring basique (kubectl top + alertes manuelles), et simuler un incident (OOMKilled) pour le diagnostiquer.

-----
