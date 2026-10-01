---
title: 'Chapitre 22 — Sécuriser les images : de la construction au déploiement'
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie V — Sécurité des containers
  - index.md
---

## Le minimum à savoir

### Les 4 piliers de la sécurité des images

**1. Choisir la bonne base :** images officielles, versions `slim` ou `distroless`, éviter les images communautaires non vérifiées.

**2. Scanner :** Trivy, Grype, Snyk — automatisé dans le pipeline CI, bloquer les CVE critiques.

**3. Signer :** Cosign (Sigstore) — prouver que l’image vient de ta CI et n’a pas été modifiée.

**4. Contrôler l’admission :** OPA/Gatekeeper ou Kyverno — empêcher le déploiement d’images non signées ou non scannées sur le cluster K8s.

### Politique d’images en entreprise

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

## ✅ Tu sais maintenant…

- Les 4 piliers : base fiable, scan, signature, contrôle d’admission
- Le workflow de sécurité des images en entreprise

-----
