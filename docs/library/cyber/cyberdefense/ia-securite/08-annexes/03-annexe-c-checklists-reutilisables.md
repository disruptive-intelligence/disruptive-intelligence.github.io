---
title: Annexe C — Checklists réutilisables
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
up:
- - IA & sécurité
  - ../index.md
- - Annexes
  - index.md
---

## Checklist avant déploiement d’un système IA

- [ ] Threat model spécifique documenté
- [ ] Classification du système selon l’AI Act (inacceptable / haut risque / limité / minimal)
- [ ] AIPD réalisée si données personnelles traitées
- [ ] Base légale RGPD identifiée et documentée
- [ ] RBAC vectoriel implémenté et testé (si RAG)
- [ ] Sanitization des sources activée (si RAG)
- [ ] Guardrails en entrée et sortie configurés et testés
- [ ] Red teaming IA réalisé avec rapport (Garak + tests manuels)
- [ ] Seuils de fuite/hallucination mesurés et acceptables
- [ ] Human-in-the-loop implémenté pour les actions critiques (si agent)
- [ ] Allow-list d’actions configurée (si agent)
- [ ] Kill switch testé (si agent)
- [ ] Monitoring et intégration SIEM opérationnels
- [ ] DPA signé avec le fournisseur de modèle (si cloud)
- [ ] Politique d’usage IA rédigée et communiquée
- [ ] Formation des utilisateurs réalisée
- [ ] Plan de réponse à incident IA formalisé
- [ ] Décision go/no-go formelle par le RSSI

## Checklist pendant l’exploitation

- [ ] Monitoring des alertes IA (injection, fuite, action bloquée) opérationnel
- [ ] Revue périodique des logs (mensuelle minimum)
- [ ] Suivi des métriques de performance et de qualité
- [ ] Suivi des coûts
- [ ] Red teaming périodique (trimestriel minimum)
- [ ] Mise à jour des guardrails et des techniques de détection
- [ ] Revue des permissions RBAC (alignement avec l’annuaire)
- [ ] Monitoring du drift (si ML classique)
- [ ] Mise à jour des dépendances (SCA)
- [ ] Suivi de la politique d’usage (taux de shadow AI résiduel)

## Checklist en cas d’incident IA

- [ ] Activation du kill switch si nécessaire
- [ ] Confinement du composant impacté (base vectorielle, modèle, agent)
- [ ] Identification de l’incident (injection ? poisoning ? fuite ? abus ?)
- [ ] Analyse des logs pour déterminer l’étendue (quelles requêtes/réponses impactées ?)
- [ ] Identification des utilisateurs impactés
- [ ] Purge des données malveillantes (base vectorielle, source documentaire)
- [ ] Évaluation par le DPO (violation de données personnelles ? notification CNIL ?)
- [ ] Communication aux utilisateurs impactés
- [ ] Remédiation technique (correction des contrôles, re-indexation, mise à jour)
- [ ] Retex et mise à jour du threat model
- [ ] Rapport d’incident formel

-----
