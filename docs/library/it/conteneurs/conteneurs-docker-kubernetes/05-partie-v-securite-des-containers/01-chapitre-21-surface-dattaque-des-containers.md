---
title: Chapitre 21 — Surface d’attaque des containers
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

comprendre les risques

## Le minimum à savoir

### Le modèle de menaces

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


### Les 5 risques à connaître absolument

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

## Très utile en pratique

### Checklist de sécurité rapide

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

## ✅ Tu sais maintenant…

- Les 6 surfaces d’attaque des containers
- Les 5 risques à connaître (escape, Docker socket, root, images, secrets)
- La checklist de sécurité rapide

## 💬 Questions d’entretien typiques

- **Pourquoi le Docker socket est-il dangereux ?** → Le Docker socket (`/var/run/docker.sock`) permet de contrôler le daemon Docker. Si un container y a accès, il peut créer de nouveaux containers avec des privilèges root sur l’hôte — c’est une compromission totale de la machine.
- **Qu’est-ce qu’un container escape ?** → C’est quand un attaquant sort de l’isolation du container pour atteindre la machine hôte. Les vecteurs incluent des vulnérabilités kernel, des capabilities excessives (SYS_ADMIN), ou un Docker socket monté. C’est rare mais l’impact est maximal.
- **Quels sont les principaux risques de sécurité des containers ?** → Le Docker socket exposé, l’exécution en root, les images non fiables (supply chain), les secrets mal gérés (base64 dans K8s), et l’absence de segmentation réseau (Network Policies).

-----
