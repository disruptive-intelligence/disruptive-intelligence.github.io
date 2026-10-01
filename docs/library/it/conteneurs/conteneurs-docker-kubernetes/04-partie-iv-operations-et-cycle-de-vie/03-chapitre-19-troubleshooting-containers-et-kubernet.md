---
title: Chapitre 19 — Troubleshooting containers et Kubernetes
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie IV — Opérations et cycle de vie
  - index.md
---

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
