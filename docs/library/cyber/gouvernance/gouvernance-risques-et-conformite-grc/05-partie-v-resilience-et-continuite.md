---
title: Partie V — Résilience et continuité
source: Cyber/08 Gouvernance & résilience/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - index.md
---

*Quand ça tourne mal — comment l'organisation se prépare, réagit, et se reconstruit.*

---


## Chapitre 22 — Gestion des incidents de sécurité vue GRC

*Ce chapitre couvre le processus, les obligations, et la coordination de la gestion d'incident. La bascule vers la gestion de crise (quand l'incident dépasse la capacité de gestion normale) est traitée au Ch.22 — la distinction est structurante.*

### 22.1 Événement vs incident

Un **événement de sécurité** est un observable qui peut ou non indiquer une menace (une alerte SIEM, un email suspect signalé par un utilisateur). Un **incident de sécurité** est un événement confirmé qui a un impact sur la confidentialité, l'intégrité, ou la disponibilité des actifs. La classification par sévérité : **P1 — Critique** (impact business majeur — ransomware actif, fuite massive, compromission AD — activation cellule de crise, notification réglementaire probable), **P2 — Élevé** (impact significatif — serveur compromis, phishing réussi avec accès aux données — investigation approfondie, confinement immédiat), **P3 — Modéré** (impact limité — malware isolé sur un poste — traitement standard), **P4 — Informatif** (pas d'impact — scan détecté, tentative bloquée — documentation).

### 22.2 Le processus

Le processus suit le modèle NIST SP 800-61 : **détection** (SOC, utilisateurs, tiers — cf. cours SOC), **qualification** (VP/FP, sévérité, périmètre — le RSSI qualifie P1/P2, le SOC qualifie P3/P4), **confinement** (isoler les machines, bloquer les comptes, bloquer les IoC — cf. cours SOC Ch.23), **éradication** (supprimer la menace, patcher la vulnérabilité, réinitialiser les credentials), **récupération** (restaurer les services, vérifier l'intégrité), et **retex** (post-mortem sans blame — timeline, ce qui a fonctionné, ce qui a échoué, actions correctives → alimente le registre des risques).

### 22.3 Obligations de notification

| Réglementation | Délai | Destinataire | Contenu |
|---------------|-------|-------------|---------|
| RGPD | 72h | CNIL + personnes si risque élevé | Nature, données, conséquences, mesures |
| NIS 2 | 24h / 72h / 1 mois | ANSSI | Alerte précoce / notification / rapport final |
| DORA | Selon classification | Régulateur financier | Incident TIC majeur |
| PCI-DSS | Immédiat | Brands, banque acquéreuse | Compromission données CB |
| OIV/SIIV | Sans délai | ANSSI | Incident sur un SIIV |

### 22.4 La coordination GRC-SOC-IR

Le RSSI coordonne (vision globale, arbitrage, communication direction), le SOC détecte et investigue (cf. cours SOC), l'IR remédie (cf. cours IR), le DPO notifie la CNIL si données personnelles, le juridique qualifie les obligations, et la COM communique (interne et externe). Le RSSI ne fait pas tout — il orchestre.

---


## Chapitre 23 — Continuité (PCA) et reprise (PRA)

Les concepts : **PCA** (Plan de Continuité d'Activité — comment continuer à fonctionner pendant la crise), **PRA** (Plan de Reprise d'Activité — comment revenir à la normale après la crise), **BIA** (Business Impact Analysis — quels processus sont critiques), **RPO** (Recovery Point Objective — combien de données peut-on perdre ? → dimensionne les sauvegardes), **RTO** (Recovery Time Objective — en combien de temps doit-on redémarrer ? → dimensionne l'infrastructure de reprise).

Le **BIA en pratique** : identifier les processus critiques AVEC les métiers (pas avec l'IT seul — les métiers savent ce qui est vital pour le business), évaluer l'impact à 1h, 4h, 24h, 48h, 1 semaine (financier, réputationnel, réglementaire, humain), identifier les dépendances (SI, prestataires, personnes), et définir les RPO/RTO par processus.

Les **stratégies de continuité** : sauvegardes 3-2-1 + immutables (3 copies, 2 supports, 1 hors site, anti-ransomware — RPO : heures à 24h, RTO : heures à jours, coût : faible à moyen), haute disponibilité (redondance, clustering, failover — RPO : quasi 0, RTO : minutes, coût : élevé), site de repli cold/warm/hot (du local vide au prêt à fonctionner — RPO/RTO et coût croissants), et Cloud DRaaS (réplication cloud, basculement automatisé). Les **tests** : test de restauration (semestriel minimum — « testez vos sauvegardes : la question n'est pas SI elles ne marchent pas, mais QUAND vous le découvrirez »), tabletop (simulation en salle, annuel), et exercice technique (basculement réel site de repli, annuel pour les processus critiques).

---


## Chapitre 24 — Gestion de crise cyber

*La gestion de crise commence là où la gestion d'incident s'arrête. Un incident P1 qui dépasse la capacité de gestion normale (SOC débordé, impact business majeur, médias, clients impactés) bascule en crise. La bascule est le moment clé — elle doit être formalisée (seuil défini, pas de débat le jour J).*

### 24.1 L'organisation de crise

La **cellule de crise** est pré-constituée (pas improvisée le jour J) : DG (décisions stratégiques — payer ou non la rançon, communiquer ou non), RSSI (coordinateur technique — pilote la réponse, fait le lien entre technique et direction), Direction COM (communication interne, externe, médias — ce qui est dit et ce qui ne l'est pas), Juridique/DPO (notifications réglementaires, qualification juridique, plainte), Technique/IR/SOC (investigation, confinement, éradication — cf. cours IR). La **salle de crise** utilise des outils HORS du SI compromis (téléphones personnels, messagerie externe, visio dédiée, tableaux physiques). Les moyens de communication sont testés en amont.

### 24.2 La communication de crise

4 audiences : les **collaborateurs** (ce qui se passe, quoi faire/ne pas faire, point de contact — « ne redémarrez pas vos postes, n'envoyez pas d'emails, utilisez vos téléphones personnels »), les **clients/partenaires** (impact sur les services, mesures prises, calendrier de reprise — « nos services sont temporairement indisponibles, nous travaillons à la résolution »), les **régulateurs** (notification formelle CNIL/ANSSI selon les délais réglementaires — Ch.20), et les **médias** (communiqué factuel, pas de spéculation, pas de détails techniques — « nous avons détecté un incident de sécurité, nos équipes sont mobilisées »). Principes : transparence dosée, ne pas mentir, ne pas spéculer, communiquer ce qu'on sait et ce qu'on fait. Les templates sont préparés à l'avance et adaptés le jour J.

### 24.3 L'exercice de crise

Scénario réaliste (ransomware vendredi soir, fuite de données, compromission d'un fournisseur critique). Participants : direction + équipes clés. Injections d'événements toutes les 15-30 min (le scénario évolue — « les médias appellent », « un client menace de rompre le contrat », « les sauvegardes ne fonctionnent pas »). Décisions à prendre et communication à produire. Retex : ce qui a fonctionné, les blocages, les améliorations.

---


## Chapitre 25 — Assurance cyber et transfert de risque

L'assurance cyber comme option de traitement du risque résiduel. Le marché (acteurs, couvertures types — interruption d'activité, frais de réponse à incident, notification des personnes, responsabilité civile, cyber-extorsion, frais juridiques). Les prérequis des assureurs (MFA obligatoire, EDR déployé, sauvegardes immutables testées, plan IR formalisé, segmentation — les assureurs imposent un socle de sécurité minimum qui est devenu un standard de facto). Les exclusions (actes de guerre — clause Lloyds 2023, amendes réglementaires, perte de données non chiffrées, incidents antérieurs — lire les petites lignes). Le processus (questionnaire, audit de souscription, tarification, couverture). L'articulation avec la gestion des risques (l'assurance couvre le risque financier résiduel APRÈS la réduction — pas un substitut aux contrôles ; un assureur qui couvre une organisation sans MFA n'existe plus). Fil rouge : Néoforma souscrit une assurance cyber — le questionnaire assureur révèle 3 non-conformités.

---
