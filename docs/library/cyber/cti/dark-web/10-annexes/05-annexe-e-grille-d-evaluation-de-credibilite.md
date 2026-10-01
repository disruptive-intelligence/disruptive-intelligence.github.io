---
title: Annexe E — Grille d'évaluation de crédibilité
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Annexes
  - index.md
---

Outil pour évaluer rapidement la crédibilité d'une annonce de breach, vente de données, ou autre contenu dark web.

## E.1 Grille produit / annonce

| Critère | Indicateurs positifs (crédibilité ↑) | Indicateurs négatifs (crédibilité ↓) |
|---|---|---|
| **Vendeur — ancienneté** | Compte 12+ mois, posts réguliers | Compte récent (<3 mois), peu d'activité |
| **Vendeur — réputation** | 100+ transactions, feedback 95%+ | Pas de transactions visibles, pas de vouching |
| **Vendeur — signature** | PGP stable, signée systématiquement | Pas de PGP, ou clé récente/changée |
| **Forum** | Forum sérieux à vouching (XSS, Exploit) | Forum public ou low-end |
| **Description** | Spécifique, technique, cohérente | Générique, vague, exagérée |
| **Volumétrie** | Cohérente avec ce qui est plausible | Disproportionnée (« 100 To en exclusivité ») |
| **Échantillons** | Disponibles, vérifiables | Refusés, vagues, ou demandant paiement |
| **Prix** | Cohérent avec marché (voir Ch.14) | Anormalement bas (scam) ou absurde |
| **Méthode contact** | Standard (XMPP, forum) | Telegram nouveau, email gratuit douteux |
| **Métadonnées échantillons** | Cohérentes avec organisation présumée | Vagues, génériques, ou contradictoires |
| **Timing** | Cohérent avec compromission documentable | Timing improbable (avant événement déclencheur) |
| **Markers internes** | Présents (noms internes, codes spécifiques) | Absents ou contredits |
| **Cohérence cross-source** | Corroboration sur autres canaux | Source unique, non-corroboré |

## E.2 Scoring rapide

Scoring informel : pour chaque critère, +1 (positif), 0 (neutre/incertain), -1 (négatif). Sommer.

- **+8 et plus** : très probablement authentique. Investigation approfondie justifiée.
- **+3 à +7** : probablement authentique avec réserves. Investigation prudente.
- **0 à +2** : ambigu. Recherche supplémentaire avant conclusion.
- **-3 à -1** : probablement scam ou recyclage. Faible priorité.
- **-4 et moins** : très probablement fake/scam. Classer.

Le scoring est un **outil d'orientation**, pas une vérité. Une investigation peut justifier d'un cas avec score modeste si certains critères sont déterminants (par exemple : marker interne unique = suffit à confirmer authenticité même si autres critères neutres).

## E.3 Grille acteur (pseudonyme)

Pour évaluer la crédibilité d'un acteur observé (vendeur, IAB, opérateur).

| Critère | Évaluation |
|---|---|
| Ancienneté du compte | Mois / années |
| Volume de posts | Nombre, fréquence |
| Activité par catégorie | Quels types de produits/services |
| Transactions confirmées | Nombre, montants, types |
| Feedback / ratings | Distribution positive/négative |
| Vouching | Qui vouche, quels niveaux |
| Présence multi-forum | Quels forums, cohérence |
| PGP | Stable ? Reconnue cross-platform ? |
| Style linguistique | Cohérence, langue maternelle apparente |
| Wallet crypto | Activité, cluster, exchanges |
| Disputes | Litiges historiques, résolutions |

Sortie : profil structuré du vendeur en 1-2 pages, base de tout dossier d'investigation sur cet acteur.

## E.4 Pièges classiques à vérifier

- **Recyclage** : la donnée vient-elle d'un breach antérieur connu ? Vérifier HIBP, DeHashed.
- **Composition factice** : assemblage de plusieurs breaches anciens présenté comme nouveau ?
- **Watermark / honeypot** : la donnée contient-elle des markers qui pourraient identifier les acheteurs ou les diffuseurs ?
- **False flag** : le profil de l'acteur est-il cohérent ou semble-t-il « designed » pour pointer vers une autre attribution ?
- **Pression temporelle artificielle** : le vendeur impose-t-il « offre 24h » pour empêcher due diligence ?
- **Prix incohérent** : trop bas (scam) ou trop élevé sans justification ?

---
