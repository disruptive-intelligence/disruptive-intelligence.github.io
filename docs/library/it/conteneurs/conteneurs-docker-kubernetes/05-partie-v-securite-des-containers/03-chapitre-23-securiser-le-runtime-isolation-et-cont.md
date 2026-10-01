---
title: 'Chapitre 23 — Sécuriser le runtime : isolation et contrôle d’exécution'
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

## Le minimum à savoir

### Les 4 mesures essentielles

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

## Très utile en pratique

### Falco : la détection runtime

**Falco** (CNCF) surveille les containers en temps réel et détecte les comportements anormaux :

- Un shell est lancé dans un container de production
- Un processus lit `/etc/shadow`
- Une connexion réseau sortante vers une IP suspecte
- Un fichier est écrit dans `/usr/bin/`

C’est l’IDS (système de détection d’intrusion) pour les containers.

### Docker rootless et user namespace remapping

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

## ✅ Tu sais maintenant…

- Les 4 mesures de hardening runtime (non-root, capabilities, read-only, PSS)
- Falco pour la détection d’anomalies en runtime
- Docker rootless et user namespace remapping comme couches de défense supplémentaires

## 💬 Questions d’entretien typiques

- **Comment sécuriser le runtime d’un container ?** → Exécuter en non-root (USER dans le Dockerfile + runAsNonRoot dans K8s), supprimer toutes les capabilities (cap-drop ALL), filesystem read-only, et appliquer les Pod Security Standards restricted.
- **Qu’est-ce que le user namespace remapping ?** → C’est un mécanisme qui mappe le UID 0 (root) du container vers un UID non privilégié sur l’hôte. Même si un attaquant devient root dans le container, il est un utilisateur sans privilège sur la machine hôte.
- **Quelle est la différence entre Docker classique et Docker rootless ?** → En Docker classique, le daemon tourne en root — un accès au Docker socket donne l’équivalent de root sur l’hôte. En rootless, le daemon tourne sans root, ce qui réduit l’impact d’une compromission du daemon.

-----
