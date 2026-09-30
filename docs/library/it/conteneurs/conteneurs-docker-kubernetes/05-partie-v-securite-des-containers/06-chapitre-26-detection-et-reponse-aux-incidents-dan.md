---
title: Chapitre 26 — Détection et réponse aux incidents dans les containers
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

## Le minimum à savoir

### Le défi de l’éphémérité

Les containers meurent et renaissent en permanence. Un container compromis peut être détruit et recréé par K8s en quelques secondes — **les preuves disparaissent**. Sans externalisation des logs et des métriques, le forensic est impossible.

### La détection runtime

**Falco** (CNCF) est l’outil de référence pour la détection d’anomalies dans les containers :

```yaml
# Exemples de règles Falco
- rule: Terminal shell in container
  desc: Détecte l'ouverture d'un shell dans un container
  condition: container and proc.name in (bash, sh, zsh)
  output: "Shell ouvert dans le container (user=%user.name container=%container.name)"
  priority: WARNING
```


### La réponse

1. **Isoler :** appliquer une Network Policy deny all sur le Pod compromis (coupure réseau immédiate)
1. **Capturer :** sauvegarder l’état du container avant sa destruction (`kubectl cp`, export des logs, snapshot du volume)
1. **Analyser :** examiner les logs K8s, les audit logs de l’API Server, les alertes Falco, corréler avec les logs applicatifs centralisés
1. **Remédier :** corriger la vulnérabilité, mettre à jour l’image, renforcer les politiques

### Les indicateurs de compromission (IoC) spécifiques aux containers

- Processus non attendu dans le container (shell, wget, curl, netcat)
- Connexions réseau sortantes vers des IPs/domaines inconnus
- Écriture dans des répertoires système (`/usr/bin`, `/etc`)
- Tentative de montage de volumes non autorisés
- Utilisation de capabilities inhabituelles
- Appels API K8s depuis un Pod applicatif

## ✅ Tu sais maintenant…

- Le défi de l’éphémérité pour le forensic
- Falco pour la détection runtime
- La démarche de réponse (isoler → capturer → analyser → remédier)
- Les IoC spécifiques aux containers

-----
