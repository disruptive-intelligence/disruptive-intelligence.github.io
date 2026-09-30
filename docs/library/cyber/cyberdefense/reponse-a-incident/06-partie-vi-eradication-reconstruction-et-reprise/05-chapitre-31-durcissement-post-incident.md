---
title: Chapitre 31 — Durcissement post-incident
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction ET reprise
  - index.md
---

## 31.1 Quick wins (premières semaines)

Les quick wins sont les mesures de durcissement à impact élevé et à déploiement rapide, directement inspirées des failles exploitées pendant l'incident. Segmentation IT/OT renforcée avec pare-feu dédié (pas juste un VLAN taggé — un pare-feu physique entre le réseau IT et le réseau OT, avec filtrage applicatif). MFA obligatoire sur tous les accès externes (VPN, Microsoft 365, portails web) y compris les accès prestataires (la faille GestPaie ne se reproduira pas). LAPS (Local Administrator Password Solution) activé sur tout le parc Windows (mots de passe admin locaux uniques et rotatifs). PowerShell script block logging activé sur TOUS les postes (pas seulement les serveurs). Sauvegardes migrées vers un système immuable (stockage cloud avec MFA delete protection et versioning). Comptes break glass créés et stockés en coffre-fort physique. PingCastle exécuté mensuellement avec suivi du score.

## 31.2 Plan structurel (mois suivants)

Les mesures structurelles nécessitent un investissement plus significatif. Tiering model AD (Tier 0 pour les DC et l'infrastructure de sécurité, Tier 1 pour les serveurs, Tier 2 pour les postes de travail — avec des comptes admin dédiés par tier, jamais réutilisés entre tiers). PAW (Privileged Access Workstations) pour les administrateurs Tier 0 (des postes dédiés, durcis, non utilisés pour la navigation ou la messagerie). Déploiement NDR pour la visibilité réseau. Upgrade licence M365 vers E5 (rétention UAL étendue). Sysmon déployé sur l'ensemble du parc Windows. Programme d'exercices de crise annuel avec la direction. Revue contractuelle des prestataires (clause MFA obligatoire pour les accès au SI).

---
