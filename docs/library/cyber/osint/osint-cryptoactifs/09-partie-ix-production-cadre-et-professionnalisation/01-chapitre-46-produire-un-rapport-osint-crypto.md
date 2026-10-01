---
title: Chapitre 46 — Produire un rapport OSINT crypto
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IX — Production, cadre et professionnalisation
  - index.md
---

Le **rapport** est le livrable principal. Sa qualité détermine l’impact de l’enquête. Mauvais rapport = bonne enquête perdue. Bon rapport = enquête médiocre amplifiée. Ce chapitre couvre la méthode pour rapports professionnels.

## 46.1 Adapter à l’audience

**Différentes audiences** ont différents besoins.

**Direction / management non-technique** :

- Executive summary clair.
- Faits clés sans jargon.
- Implications business.
- Recommandations actionables.
- Graphes simples.

**Équipe technique (SOC, IR, CTI)** :

- Détails techniques.
- IoCs structurés.
- Méthodologie.
- Reproductibilité.
- Annexes complètes.

**Autorités (DGSI, TRACFIN, FBI, Europol)** :

- Faits sourcés.
- Timeline rigoureuse.
- Identifications précises avec calibration.
- Recommandations de coopération.
- Pièces à conviction structurées.

**Tribunal / procureur** :

- Faits incontestables.
- Méthodologie reproductible.
- Chain of custody documentée.
- Calibration explicite.
- Limites assumées.

**Communauté CTI / partage sectoriel** :

- Patterns anonymisés.
- IoCs.
- Threat intel utilisable.
- Préservation TLP.

Un même dossier peut produire **plusieurs rapports** adaptés (executive summary public + rapport complet TLP AMBER + annexe technique TLP RED).

## 46.2 Structure type d’un rapport OSINT crypto

**Page de garde** :

- Titre.
- Référence dossier.
- Mandant.
- Date.
- Auteur(s).
- TLP (Traffic Light Protocol).
- Version.

**Executive summary (1-2 pages)** :

- Contexte.
- Faits principaux.
- Conclusions clés.
- Recommandations.
- Limites.

**Cadrage de la mission** :

- Mandat.
- Périmètre.
- Méthodologie générale.
- Cadre légal.

**Méthodologie** :

- Outils utilisés.
- Sources.
- Méthodes appliquées.
- Calibration WEP.

**Faits et observations** :

- Timeline.
- Transactions documentées.
- Adresses identifiées.
- Patterns observés.

**Analyse** :

- Hypothèses formulées.
- Calibration.
- Recoupements.
- Identifications.

**Conclusions** :

- Synthèse.
- Niveaux de confiance.
- Implications.

**Recommandations** :

- Actions immédiates.
- Actions à moyen terme.
- Coordination requise.

**Limites** :

- Ce qui n’a pas pu être fait.
- Incertitudes.
- Évolutions possibles.

**Annexes** :

- Captures de preuves.
- Listes complètes (adresses, TXIDs).
- Graphes détaillés.
- Détails méthodologiques.
- Glossaire si nécessaire.

## 46.3 L’executive summary

Le **executive summary** est la partie la plus lue. Souvent **la seule** lue par certains décideurs. Doit donc être autonome et clair.

**Structure** :

- **Contexte** : 1-2 phrases (« Aurélien Médical, équipementier français, victime ransomware Akira mars 2026, paiement 35 BTC »).
- **Mandat** : 1 phrase (« Athéna mandaté pour tracer flux post-paiement et identifier angles d’action »).
- **Conclusions principales** : 3-5 points clés (« 75% des flux tracés », « 3 mules identifiées », « 75 000 USDT gelés », « 2 hubs blanchiment partagés Akira / Black Basta », etc.).
- **Recommandations majeures** : 3-5 points (« coordination autorités sur mules », « surveillance hubs identifiés », « renforcement défenses », etc.).
- **Limites** : 1-2 phrases honnêtes (« récupération nominale ~3,75% du paiement », « attribution civile non possible OSINT »).

**Longueur** : 1 à 2 pages **maximum**. Deux pages = strict maximum. Une page si possible.

**Style** : phrases courtes, factuelles, sans jargon. Si le destinataire (CEO, journaliste) ne comprend pas l’executive summary, le rapport est raté.

## 46.4 Calibration WEP dans le rapport

Chaque hypothèse / conclusion doit avoir un **WEP explicite**.

**Formulations recommandées** :

- « **Quasi-certain** (>95%) que [observation] » — réservé aux faits directement observés.
- « **Très probable** (80-95%) que [hypothèse] basé sur [éléments de preuve] »
- « **Probable** (60-80%) que [hypothèse] »
- « **Possible** (40-60%) que [hypothèse], en concurrence avec [alternatives] »
- « **Peu probable** (15-40%) que [hypothèse alternative] »

**Erreur classique** : oublier WEP, ce qui fait passer hypothèses comme certitudes. Tous les énoncés non-évidents doivent être qualifiés.

## 46.5 Visualisations dans le rapport

Cf Ch.21. En synthèse :

**Pour rapport exécutif** : 1-3 graphes simples, niveau 3-4.

**Pour rapport opérationnel** : 3-7 graphes intermédiaires.

**Pour annexes techniques** : graphes détaillés.

**Tableaux** : timeline, listes d’adresses, mules identifiées. Toujours préférer tableaux propres à listes en prose pour données structurées.

## 46.6 Recommandations

Les recommandations doivent être **SMART** :

- **Spécifiques** : pas « renforcer la sécurité » mais « déployer EDR sur 100% des postes Windows utilisateurs ».
- **Mesurables** : objectifs quantifiables.
- **Atteignables** : réalistes pour le contexte du mandant.
- **Pertinentes** : adressent les enjeux identifiés.
- **Temporellement définies** : avec délai.

**Hiérarchisation** :

- **Actions immédiates** (jours / semaines).
- **Actions à moyen terme** (mois).
- **Actions à long terme** (programme durable).

**Adaptation à audience** :

- Recommandations à victime : pratiques, opérationnelles.
- Recommandations à autorités : coopération, coordination.
- Recommandations à communauté : threat sharing, defensive measures.

## 46.7 Annexes structurées

**Annexes typiques** :

**A — Liste exhaustive d’adresses identifiées** : tableau avec adresse, blockchain, label, niveau de confiance, source.

**B — Liste des transactions documentées** : tableau avec TXID, date, montant, source, destinataire.

**C — Captures d’écran** : avec hashes SHA-256.

**D — Graphes détaillés** : niveau 1 / 2.

**E — Méthodologie détaillée** : protocoles, outils, validations.

**F — Glossaire** : termes techniques expliqués (utile si rapport lu par non-spécialistes).

**G — IoCs structurés** : pour partage CTI (format STIX/TAXII si possible).

## 46.8 Revue qualité avant livraison

Avant transmission, **peer review** systématique :

- Un pair lit le rapport entier.
- Vérifie cohérence, calibration, faits.
- Suggère améliorations.
- Validation directeur si projet sensible.

**Checklist qualité** :

- [ ] Executive summary autonome et clair.
- [ ] Tous WEP explicites.
- [ ] Captures référencées en annexes avec hashes.
- [ ] Timeline cohérente UTC.
- [ ] Recommandations SMART.
- [ ] Limites assumées explicitement.
- [ ] Pas de jargon inexpliqué.
- [ ] Cohérence terminologique.
- [ ] Graphes lisibles avec légende.
- [ ] Cadre légal respecté.
- [ ] TLP correctement positionné.

## 46.9 Le rapport vivant

Pour enquêtes longues, **rapport intermédiaire** + rapport final, avec versionning. Conserve traçabilité de l’évolution analytique.

Pour surveillance continue, **rapports périodiques** (mensuels, trimestriels) selon mandat.

-----
