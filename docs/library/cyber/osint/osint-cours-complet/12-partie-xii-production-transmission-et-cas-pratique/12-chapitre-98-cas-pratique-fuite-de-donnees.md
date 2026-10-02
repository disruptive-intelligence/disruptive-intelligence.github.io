---
title: 'Chapitre 98 — Cas pratique : fuite de données'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 98.1 Présentation du cas

Une organisation découvre via veille externe qu'une fuite de données semble la concerner : un dump apparu sur un forum cybercriminel, prétendant contenir des emails internes. Le RSSI mandate l'analyste OSINT pour :

- Confirmer ou infirmer la fuite.
- Évaluer le volume et la sensibilité.
- Identifier la source probable.
- Documenter pour action légale et notification CNIL (RGPD).

## 98.2 Étape 1 — Préservation et accès

**OPSEC stricte.** Compte d'investigation sur forum cybercriminel (compte mature, OPSEC robuste).

**Capture.** Hunchly du post de vente. Capture du sample si fourni.

**Hash** systématique.

## 98.3 Étape 2 — Vérification

**Sample analysis.** Le vendeur fournit un sample de 10 emails. Examination :

- Format cohérent avec format internes de l'organisation.
- Adresses email correspondent aux conventions internes.
- Sujets cohérents avec l'activité.
- Métadonnées cohérentes (timestamps plausibles, expéditeurs vérifiables sur LinkedIn).

**Conclusion préliminaire.** Sample probablement authentique. Fuite confirmée (B2).

## 98.4 Étape 3 — Estimation du volume

**Selon le post de vente.** ~50 000 emails. Période couverte : janvier-décembre 2025.

**Tarif demandé.** 25 000 $ en BTC.

**Cohérence.** Cohérent avec dump de boîte email exploitée ou avec un leak structuré (employé compromis).

## 98.5 Étape 4 — Source probable

**Hypothèses.**

| H | Source |
|---|---|
| H1 | Compte email d'un employé compromis (phishing, stealer log) |
| H2 | Accès serveur interne (intrusion réseau) |
| H3 | Insider |
| H4 | Fournisseur cloud compromis |

**Indices.**

- Vérification Hudson Rock / SpyCloud sur domaines emails de l'organisation : plusieurs employés ont machines compromises par stealer logs récents.
- Recherche dans canaux Telegram de vente stealer logs : un dump récent contient credentials de l'organisation, dont accounts cloud.

**Conclusion préliminaire.** H1 et H4 plausibles. Possiblement combinaison.

## 98.6 Étape 5 — Attribution

**Posteur.** Username `cyberseller22` sur le forum.

**Recherche cross-plateformes.** `cyberseller22` actif sur 3 forums. Historique : vente régulière de dumps. Pas de signature étatique.

**Conclusion attribution.** Acteur criminel privé (broker). Pas opération étatique apparente. Pas attribution précise possible en OSINT.

## 98.7 Étape 6 — Action

**Immédiat.**

- Notification CNIL (RGPD art. 33) : sous 72 heures de la confirmation de la fuite.
- Préservation des pièces (hash + captures Hunchly).
- Communication interne (RSSI + direction).
- Audit interne (qui est compromis ? quels emails ont fuité ?).
- Réinitialisation des accès des comptes compromis.
- Notification des personnes concernées si données personnelles (RGPD art. 34).

**Court terme.**

- Plainte pénale (intrusion, vol de données, recel).
- Recherche éventuelle d'acquisition contrôlée du dump (zone juridique : à valider avec avocats).
- Veille proactive pour d'autres apparitions.

## 98.8 Étape 7 — Production

**Rapport RSSI.**

> **BLUF.** Une fuite de données a été identifiée sur forum cybercriminel, contenant probablement ~50 000 emails internes 2025. Cotation : B2 (sample vérifié, volume non confirmé). Source probable : compromission de comptes employés via infostealers. Risques : exposition de données commerciales, fuite RGPD, opportunités d'extorsion. **Recommandations : notification CNIL immédiate, réinitialisation comptes compromis, audit, communication maîtrisée.**

## 98.9 Étape 8 — Suite

**Veille post-rapport.**

- Surveillance des autres forums.
- Surveillance des canaux Telegram pour publications progressives.
- Alertes en cas de leak public.

## 98.10 Pédagogie

Ce cas illustre :

- OSINT pour CTI défensive.
- Workflow notification CNIL.
- Identification source via stealer logs (Hudson Rock).
- Cadre légal RGPD strict.
- Coordination avec RSSI / RGPD / avocats.

-----
