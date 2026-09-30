---
title: Annexe B — Checklists opérationnelles
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

## Checklist des 30 premières minutes

- [ ] Confirmer le vrai positif (exclure faux positif, maintenance planifiée)
- [ ] Identifier les systèmes visiblement impactés
- [ ] Évaluer la sévérité initiale (P1-P4)
- [ ] Augmenter le logging sur les systèmes suspects
- [ ] Sauvegarder les logs actuels (avant rotation)
- [ ] Activer la capture réseau si possible
- [ ] NE PAS redémarrer, NE PAS nettoyer, NE PAS modifier
- [ ] Escalader vers l'IR lead selon la chaîne d'escalade
- [ ] Ouvrir le canal de communication sécurisé (hors SI)
- [ ] Documenter les actions dans le journal d'incident

## Checklist de confinement

- [ ] Décision de confinement validée par le RSSI ou l'IR lead
- [ ] Collecte forensic (RAM + triage) effectuée AVANT l'isolation
- [ ] Isolation réseau exécutée (EDR containment / VLAN / ACL pare-feu)
- [ ] Comptes compromis désactivés
- [ ] Tokens et sessions révoqués (M365, VPN, SSO)
- [ ] Sauvegardes protégées (déconnexion si sur le même réseau)
- [ ] Accès tiers compromis désactivés
- [ ] Communication au SOC : surveillance renforcée sur les IoC identifiés
- [ ] SitRep mis à jour avec le périmètre de confinement

## Checklist de collecte forensic

- [ ] Acquisition mémoire (DumpIt/WinPmem) — AVANT tout redémarrage
- [ ] Hash SHA256 calculé immédiatement après acquisition
- [ ] Triage KAPE ou Velociraptor (artefacts Windows/Linux)
- [ ] Image disque si nécessaire (FTK Imager / dd)
- [ ] Chaîne de custody documentée (formulaire complété)
- [ ] Stockage sécurisé de la preuve (hors SI compromis)
- [ ] Sample malware isolé pour analyse (sandbox)

## Checklist de validation post-éradication

- [ ] Scan EDR complet sur 100 % du parc
- [ ] Aucune tâche planifiée malveillante résiduelle
- [ ] Aucun service non répertorié
- [ ] Aucun compte non autorisé dans les groupes privilégiés
- [ ] Aucune GPO non légitime
- [ ] Aucune règle de forwarding email non légitime
- [ ] Aucun flux réseau vers les C2 identifiés
- [ ] Audit AD (PingCastle / Purple Knight) passé
- [ ] Threat hunting ciblé en cours (4 semaines minimum)

## Checklist de clôture

- [ ] Éradication validée (surveillance post sans alerte)
- [ ] Tous les systèmes en production
- [ ] Notifications effectuées (ANSSI, CNIL, assureur)
- [ ] Plainte déposée
- [ ] Rapport d'incident final livré
- [ ] Actions résiduelles attribuées avec responsables et échéances
- [ ] RETEX planifié (J+14 à J+28 après clôture)
- [ ] Journal d'incident archivé

---
