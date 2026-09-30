---
title: Chapitre 23 — Réponse à incident, remédiation et résilience opérationnelle
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE V — Cadres de réponse
  - index.md
---

## 23.1 — La chaîne de réponse

La réponse à incident suit un processus structuré : **détection** (identification d'un événement suspect), **qualification** (l'événement est-il un incident ? Quelle gravité ?), **containment** (limiter la propagation), **investigation** (comprendre la chaîne d'attaque), **remédiation** (éliminer la présence de l'attaquant et corriger les vulnérabilités exploitées), et **retour d'expérience** (leçons apprises, amélioration des défenses).

L'ANSSI a publié en janvier 2026 un guide « Préparer la remédiation » qui fournit un cadre structuré pour la phase de remédiation — souvent la phase la plus complexe et la plus longue. Le guide insiste sur la nécessité de **préparer la remédiation en amont** de l'incident, pas pendant la crise.

## 23.2 — La supply chain comme facteur aggravant

Les cas documentés par l'ANSSI illustrent comment la compromission d'un prestataire peut entraîner des effets en cascade sur ses clients. La remédiation dans ce contexte est considérablement plus complexe : elle implique la coordination entre organisations indépendantes, le partage d'informations sensibles (quelles données ont été exfiltrées ?), et la gestion de relations commerciales sous tension.

La **latéralisation inter-organisationnelle** — un attaquant qui pivote depuis un prestataire compromis vers les réseaux de ses clients via des interconnexions existantes — est un pattern récurrent en 2025. L'ANSSI documente des cas où les attaquants ont utilisé « les ressources internes de la première entité compromise pour forger ou utiliser des éléments crédibles permettant de mieux cibler une deuxième entité ».

## 23.3 — L'écosystème CERT/CSIRT

L'écosystème de réponse s'articule autour de plusieurs niveaux. Les CERT/CSIRT nationaux (CERT-FR en France, CERT-EU pour les institutions européennes) traitent les incidents les plus graves et produisent des alertes et advisories. Les CERT sectoriels (ISACs) partagent l'intelligence de menace au sein de secteurs spécifiques. Les CERT d'entreprise gèrent la réponse opérationnelle au niveau organisationnel.

Les réseaux de coordination incluent FIRST (Forum of Incident Response and Security Teams — réseau mondial), TF-CSIRT (réseau européen), InterCERT France (premier réseau national de CERT en France), et le réseau européen des CSIRTs sous NIS2.

## 23.4 — Construire la cyber-résilience

La cyber-résilience va au-delà de la prévention : c'est la capacité d'une organisation à **anticiper, résister, récupérer et s'adapter** face aux cyberattaques. L'approche **threat-informed defense** — défendre en fonction des menaces réelles documentées dans le CTL — est le cadre méthodologique.

Les recommandations convergentes des agences du corpus s'organisent en priorités :

**P0 — Critique** : patching des vulnérabilités activement exploitées (KEV/EUVD), MFA résistant au phishing sur tous les accès critiques, segmentation réseau IT/OT, sauvegarde hors ligne testée, plan de réponse à incident documenté et exercé.

**P1 — Important** : réduction de la surface d'attaque (désactivation des services inutiles, restriction des outils RMM), monitoring comportemental (EDR/XDR), gestion des accès privilégiés (PAM), sécurité de la supply chain (audit des prestataires, clauses contractuelles), sensibilisation ciblée (C-level, OT, supply chain).

**P2 — Structurant** : architecture zero trust, programme de threat hunting, purple teaming régulier, SBOM et gestion des dépendances, participation aux ISACs sectoriels, automatisation de la détection et de la réponse.

## 23.5 — 🔴 Fil rouge : réponse complète à l'incident

> **📌 FIL ROUGE — Épisode 23**
>
> Sophie pilote la réponse complète à l'incident EuroDefense. L'investigation, conduite avec l'appui de l'ANSSI (mobilisée en raison de la dimension espionnage étatique), confirme la présence simultanée de Qilin (ransomware) et ShadowPad (espionnage). La remédiation est complexe : l'attaquant ShadowPad a établi plusieurs points de persistance indépendants du vecteur d'accès initial du ransomware.
>
> La remédiation prend trois mois et inclut : reconstruction des serveurs compromis, changement de tous les credentials partagés avec le prestataire, segmentation réseau renforcée entre EuroDefense et ses sous-traitants, déploiement d'un monitoring renforcé (EDR sur les serveurs de contrats OTAN, IDS sur les segments OT), et notification NIS2 à l'ANSSI comme autorité compétente.
>
> Le retour d'expérience identifie trois échecs défensifs : (1) l'interconnexion réseau avec le prestataire n'était pas suffisamment segmentée, (2) aucune surveillance ne portait sur les forums underground pour les credentials des sous-traitants, (3) le serveur Exchange exposé identifié en février (Ch. 5) n'avait pas été correctement remédié. Sophie documente ces leçons dans le rapport post-incident et les intègre dans le plan de résilience.

---
