---
title: Chapitre 24 — Workflow complet d’une enquête crypto
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IV — Outils et workflow
  - index.md
---

Synthèse de toute la Partie III. Ce chapitre articule le **workflow complet** depuis la réception du mandat jusqu’à la clôture, intégrant méthodes (Partie III), outils (Ch.19-23), et discipline.

## 24.1 Phase 1 — Cadrage et réception du mandat

**Inputs** : demande client / autorité / alerte.

**Actions** :

- **Validation du mandat** : périmètre clair, objectifs réalistes, livrables explicites, délais et budget.
- **Cadre légal** : confirmation du cadre (RGPD, secret professionnel, sanctions, autorisation autorités).
- **Affectation analyste(s)** : compétences, charge de travail, conflits d’intérêt.
- **Setup technique** : environnement d’investigation, outils, accès.
- **Communication initiale** : briefing donneur d’ordre, contacts d’autorités si applicable.

**Livrable** : note de cadrage validée par toutes les parties.

## 24.2 Phase 2 — Collecte initiale

**Inputs** : indices initiaux (adresse, TXID, capture, etc. — Ch.13).

**Actions** :

- **Vérification** des indices (blockchain correcte, transaction existe, etc.).
- **Lecture initiale** : transaction, adresse principale.
- **Constitution fiche d’adresse** initiale.
- **Captures** systématiques (chain of custody).
- **Documentation** dans journal d’enquête.

**Livrable** : journal initial + fiches d’adresses initiales.

## 24.3 Phase 3 — Investigation iterative

**Inputs** : indices initiaux exploités.

**Actions** (cycle itératif, plusieurs semaines) :

- **Suivi des flux** : par étape, en suivant chaque output significatif.
- **Identification des contreparties** : nouvelles adresses, services traversés.
- **Enrichissement** : labels, OSINT externe, recoupement.
- **Hypothèses** : formulation et calibration WEP.
- **Construction du graphe** : extension progressive.
- **Documentation continue** : fiches mises à jour, journal à jour.
- **Priorisation** : quelles branches valent l’effort, lesquelles peuvent être abandonnées.

**Livrable** : graphe d’investigation en évolution, fiches multiples.

## 24.4 Phase 4 — Analyse et synthèse

**Inputs** : graphe et fiches matures.

**Actions** :

- **Identification de patterns** : ransomware, pig butchering, blanchiment, etc.
- **Attribution** : niveau et calibration.
- **Caractérisation des acteurs** : profils, méthodes, infrastructure.
- **Identification des points de coopération** : exchanges KYC, services coopérants.
- **Validation hypothèses** : croisements multiples, validation par pairs.

**Livrable** : analyse synthétique structurée.

## 24.5 Phase 5 — Production du rapport

**Inputs** : analyse complète.

**Actions** :

- **Rédaction** du rapport selon template (Annexe H).
- **Visualisations** : graphes pour rapport.
- **Captures** : annexe technique avec preuves.
- **Recommandations** : actionables et calibrées.
- **Limites** : explicites et calibrées.
- **Revue par pairs** : peer review interne.

**Livrable** : rapport final.

## 24.6 Phase 6 — Restitution et coopération

**Inputs** : rapport final.

**Actions** :

- **Briefing** : présentation orale au mandant et autorités.
- **Q&A** : réponses aux questions et clarifications.
- **Coopération** : transmission aux autorités selon TLP, support à actions ultérieures.
- **Signalement** : si infractions graves découvertes (article 40 CPP).
- **Communication** : selon TLP, partage sectoriel (ISAC) si applicable.

**Livrable** : rapport diffusé + restitutions effectuées.

## 24.7 Phase 7 — Clôture et archivage

**Inputs** : restitution effectuée.

**Actions** :

- **Archivage immutable** : tout le dossier, conformément à la chain of custody.
- **Réflexion post-mortem** : ce qui a fonctionné, ce qui pourrait être amélioré.
- **Capitalisation** : enrichissement de la base interne (labels, patterns, fiches d’acteurs).
- **Communication finale** : remerciements, retours mandant.

**Livrable** : dossier archivé + retours d’expérience.

## 24.8 Surveillance post-clôture

Selon mandat, **surveillance** des adresses identifiées peut continuer après clôture :

- Alertes automatiques sur mouvements futurs.
- Notification du mandant si évolutions significatives.
- Maintien de la base label.

## 24.9 Discipline transversale

À chaque phase, principes communs :

**Documentation continue** : journal à jour, fiches actualisées, captures faites.

**Calibration WEP systématique** : pas d’affirmation sans niveau de confiance.

**Validation croisée** : multiple sources, multiple outils.

**Communication claire** : points d’étape réguliers avec mandant.

**Discipline éthique** : pas d’interaction directe avec wallets cibles, respect du périmètre, pas de prolifération.

**Adaptation** : le workflow est un guide, pas un dogme. Chaque enquête a ses spécificités.

## 24.10 Indicateurs de qualité

Pour évaluer la qualité d’une enquête crypto :

**Couverture** : pourcentage des flux pertinents tracés.

**Calibration** : niveaux de confiance bien justifiés et cohérents.

**Reproductibilité** : un autre analyste peut-il refaire l’analyse à partir des mêmes données ?

**Actionnabilité** : les recommandations sont-elles concrètes et exploitables ?

**Honnêteté** : les limites sont-elles documentées clairement ?

**Délai** : respect des échéances mandat.

**Coût** : budget respecté.

**Satisfaction mandant** : feedback du donneur d’ordre.

## 24.11 Fil rouge — MIXSHADOW : workflow complet

> **🔗 MIXSHADOW — Épisode 16 : bilan workflow**
> 
> À 8 semaines de mission, Sarah a parcouru le workflow complet :
> 
> - **Cadrage** (semaine 1) : note validée par DGSI + Aurélien Médical + Athéna.
> - **Collecte initiale** (semaines 1-2) : indices initiaux exploités, fiche Akira receive établie.
> - **Investigation** (semaines 2-7) : 250 adresses identifiées, 4 chaînes (Bitcoin, Ethereum, TRON, Solana mineur), graphe complet construit.
> - **Analyse** (semaine 6-7) : patterns Akira caractérisés, attribution calibrée, points de coopération identifiés.
> - **Rapport** (semaine 7-8) : rédaction, visualisations, peer review interne, validation directeur Athéna.
> - **Restitution** (semaine 8) : briefing DGSI + Aurélien Médical, transmission Europol via DGSI.
> - **Clôture** (semaine 8) : archivage immutable, retours mandant.
> 
> **Bilan honnête** :
> 
> ✅ **Réussites** :
> 
> - Cartographie complète des flux Akira post-paiement.
> - Identification de **2 hubs de blanchiment** non précédemment documentés (alimentent la base TRM Labs et Chainalysis).
> - **6 adresses TRON** principales transmises à Tether via DGSI pour évaluation de gel.
> - Pattern de blanchiment Akira **documenté** (template réutilisable pour d’autres victimes).
> - Insight sur **service de blanchiment partagé** Akira / Black Basta — alimente dossier transversal.
> - **3 adresses identifiées comme déposées sur Binance** — coopération Binance via DGSI permet identification utilisateur du compte (mais résultat non communiqué à Athéna).
> 
> ⚠️ **Limites** :
> 
> - **Pas de récupération** des fonds.
> - **Attribution civile** non possible en OSINT — relevait des autorités.
> - **Tornado Cash** : analyse statistique des sorties n’a pas permis attribution claire des retraits correspondants.
> - **Plusieurs branches** n’ont pas été suivies en profondeur (priorisation imposée par budget).
> 
> 📊 **Métriques** :
> 
> - Durée : 8 semaines.
> - Charge : Sarah 80% temps + 1 junior 50% temps.
> - Budget : ~80 k EUR (incluant outils, peer review, livrables).
> - Couverture estimée : ~75% des flux Akira post-paiement Aurélien Médical.
> - Calibration : tous les éléments du rapport ont WEP explicite.
> 
> Sarah note pour le retour d’expérience interne Athéna :
> 
> - **Outils pro** (Chainalysis + TRM) ont apporté gain majeur de temps et couverture.
> - **Coordination DGSI** a permis ouvertures (Tether, Binance) impossibles en OSINT pur.
> - **Workflow structuré** a rendu l’enquête lisible et le rapport crédible.
> - **Limites honnêtes** ont préservé la crédibilité d’Athéna (vs un rapport sur-promesses qui se serait effondré à la première vérification).
> 
> Le dossier MIXSHADOW est archivé. Les insights alimentent les enquêtes futures Athéna.

-----
