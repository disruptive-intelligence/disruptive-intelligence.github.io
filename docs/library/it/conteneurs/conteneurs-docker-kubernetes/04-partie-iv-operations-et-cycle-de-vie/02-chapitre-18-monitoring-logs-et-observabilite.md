---
title: Chapitre 18 — Monitoring, logs et observabilité
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie IV — Opérations ET cycle de vie
  - index.md
---

## Le minimum à savoir

### Pourquoi centraliser les logs

Les containers sont éphémères. Quand un Pod est supprimé ou recréé, ses logs disparaissent. Sans centralisation, tu ne peux pas diagnostiquer un problème survenu il y a 30 minutes si le Pod a été recréé depuis.

**Convention containers :** les applications doivent logger sur **stdout/stderr** (pas dans des fichiers). Docker et Kubernetes captent automatiquement stdout/stderr.

```bash
# Voir les logs d'un Pod
kubectl logs mon-pod
kubectl logs -f mon-pod              # En temps réel
kubectl logs mon-pod --previous      # Logs de l'instance précédente (après un crash)
```


### La stack de monitoring standard

Le standard de facto pour le monitoring Kubernetes :

- **Prometheus** : collecte les métriques (CPU, mémoire, latence, erreurs, métriques custom)
- **Grafana** : affiche les métriques dans des dashboards visuels
- **Loki** (ou EFK) : centralise les logs
- **AlertManager** : envoie des alertes (email, Slack, PagerDuty) quand un seuil est dépassé

### Les métriques à surveiller

|Métrique                 |Pourquoi                                 |
|-------------------------|-----------------------------------------|
|CPU par Pod              |Détecter les surcharges                  |
|Mémoire par Pod          |Prévenir les OOMKilled                   |
|Nombre de Pods ready     |Vérifier que l’application est disponible|
|Taux d’erreurs HTTP (5xx)|Détecter les problèmes applicatifs       |
|Latence (p50, p95, p99)  |Détecter les ralentissements             |
|Restarts de Pods         |Détecter les crashs en boucle            |

### Les outils du quotidien

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

## ✅ Tu sais maintenant…

- Pourquoi centraliser les logs (éphémérité des containers)
- La stack Prometheus + Grafana pour le monitoring
- Les métriques clés à surveiller
- Les outils du quotidien (kubectl top, k9s, Dashboard — avec précaution)

-----
