---
title: 'Chapitre 101 — Cas pratique : triage financier / crypto'
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 101.1 Présentation du cas

Un cabinet d'avocats mandate l'analyste pour triage initial sur une affaire impliquant flux crypto suspects entre plusieurs entités. Objectif : déterminer si l'affaire mérite expertise crypto forensique professionnelle, ou si elle se limite à un triage simple.

## 101.2 Étape 1 — Cadrage

**Sujet.** Société française « EuroTrade » suspecte des flux crypto vers entités opaques. Plainte du DAF.

**Périmètre.** Triage initial en sources ouvertes pour orienter la suite.

**Bornes.** Pas d'analyse on-chain profonde (renvoi cours OSINT Crypto vFULL si nécessaire).

## 101.3 Étape 2 — Sociétés impliquées

**EuroTrade SAS (France).** Pappers : société de trading B2B, CA 23 M€.

**Partenaire 1 : Glacier Capital Ltd (BVI).** OpenCorporates : société BVI, données très limitées.

**Partenaire 2 : SkyChain DMCC (UAE).** Limited public info.

## 101.4 Étape 3 — Flux observables

**Indicateurs.**

- Comptes EuroTrade montrent ligne « services financiers internationaux » de 4.2 M€ sur 2024-2025.
- Pas de détail public.

**Hypothèse.** Ces flux peuvent transiter en crypto.

## 101.5 Étape 4 — Pivots crypto en surface

**Recherche.** EuroTrade publiquement enregistrée sur exchange crypto ? Pas de mention publique.

**Wallets connus.** EuroTrade a-t-elle wallet public connu (Etherscan ENS, mention site web) ? Non identifiable.

**SkyChain DMCC.** Dubai-based, mention dans rapports d'analyses sectorielles comme intermédiaire crypto-fiat.

**Glacier Capital BVI.** Aucune empreinte crypto identifiable en surface.

## 101.6 Étape 5 — Limites du triage

**Constat.** En surface, peu d'éléments pour conclure. Les flux crypto, s'ils existent, transitent par adresses non publiquement liées aux sociétés en source ouverte.

**Pour aller plus loin.** Nécessaire :

- Identification de wallets via réquisitions exchanges (compétence judiciaire).
- Clustering on-chain par cabinet spécialisé (Chainalysis, TRM, Elliptic).
- Cross-référence avec adresses sanctionnées.
- Analyse des bridges utilisés (cross-chain).

**Renvoi.** Cours OSINT Crypto vFULL pour l'expertise approfondie. Recommandation au cabinet d'avocats : faire intervenir cabinet spécialisé crypto forensique.

## 101.7 Étape 6 — Production

**Note de triage.**

> **BLUF.** Le triage OSINT initial sur EuroTrade et ses partenaires Glacier Capital (BVI) et SkyChain (UAE) ne permet pas de caractériser publiquement les flux crypto suspectés. Les éléments visibles (ligne comptable « services financiers internationaux » de 4.2 M€) sont cohérents avec hypothèse de flux opaques, sans démonstration directe en source ouverte. **Recommandation : expertise crypto forensique professionnelle pour clustering on-chain et identification des wallets ; coordination procédure pénale pour réquisitions exchanges.**

## 101.8 Pédagogie

Ce cas illustre :

- Triage initial OSINT crypto.
- Identification rapide des limites du master.
- Renvoi explicite vers cours spécialisé.
- Recommandation actionnable proportionnée.
- Honnêteté méthodologique : ne pas sur-affirmer ce qu'on ne peut pas voir.

## 101.9 Élargissement — variantes de triage crypto

**Variante 1 — Wallet identifié publiquement.** L'entité a publié son adresse ENS ou wallet en clair. Triage : Etherscan, historique transactions, contreparties. Pivots possibles si DeFi avec adresses labellisées.

**Variante 2 — Stealer log avec credentials exchange.** Email cible apparaît dans stealer log avec accès Binance / Coinbase. Triage : confirmation usage exchange, hypothèses sur volumes (sans accès au compte). Escalade : exchange réquisition.

**Variante 3 — Donation publique à organisation.** L'entité a fait donation crypto à organisation (publique sur Etherscan). Pivot : identité publique → wallet. Réutilisation du wallet pour autres flux.

**Variante 4 — Rug pull / scam identification.** Investigation d'un projet crypto frauduleux. Identification des wallets fondateurs, suivi du cashout, identification des plateformes utilisées. Souvent traçable sur quelques étapes avant mixer.

**Variante 5 — Sanctions evasion via crypto.** Investigation sur entité sanctionnée. Recherche d'adresses publiques (OFAC SDN crypto list). Suivi des contournements (mixers, bridges, P2P).

## 101.10 Méthodologie triage spécifique sanctions

Pour vérification rapide :

1. **Liste OFAC** : OFAC SDN crypto addresses list à jour (mise à jour fréquente).
2. **Chainalysis Sanctions Screening** (gratuit pour adresses individuelles).
3. **TRM Labs Public** (limité gratuit).
4. **Cross-recherche** : adresses associées (clusters connus).

**Limites.** L'OSINT pur ne peut pas garantir absence de sanction (adresses nouvelles, clustering avancé requis). Pour conformité institutionnelle, outils payants nécessaires (Chainalysis KYT, TRM, Elliptic Lens).

## 101.11 Coordination OSINT crypto + classique

Le cas typique mobilise OSINT classique ET crypto :

**OSINT classique.** Identifie entités, sociétés, contextes, indices de flux.

**OSINT crypto.** Identifie adresses, patterns on-chain, sanctions.

**Coordination.**

- Pivots email/username → adresse crypto via réseaux sociaux ou ENS.
- Pivots crypto → email/identité via leaks ou KYC d'exchange (judiciaire).
- Pattern d'ensemble (offshore + crypto + désinformation) en cohérence.

Pour MIRAGE : le compte Binance personnel de Delaunay identifié via stealer log (OSINT classique) ouvre le pivot crypto. La profondeur (clustering on-chain, attribution wallets) renvoie cours OSINT Crypto vFULL.

-----
