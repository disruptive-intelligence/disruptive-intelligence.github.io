---
title: Annexe J — 5 mini-cas synthétiques d’entraînement
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

Cinq cas réduits à pratiquer la méthode. Pas de solutions « officielles » — l’analyste reproduit le raisonnement.

## J.1 Mini-cas 1 — Suspicion de pig butchering

**Énoncé** : un client privé contacte le cabinet. Sa cousine, 60 ans, a perdu ~80 000 USD sur une plateforme « MetaInvest Pro » sur 5 mois. Elle fournit 12 TXIDs USDT-TRON, captures de l’app, et conversation Instagram avec « Alex », son contact qui l’a introduite.

**Questions à se poser** :

1. Quels sont vos premiers indices à investiguer ?
1. Quelle est votre méthode pour confirmer le pattern de pig butchering ?
1. Quels outils utilisez-vous principalement ?
1. Comment caractérisez-vous le cluster opérateur ?
1. Quelles sont les actions recommandables pour la cousine ?
1. Quels sont les WEP que vous appliqueriez à vos conclusions ?

**Pistes** : Tronscan pour vérification, Chainalysis pour cluster, recherche reverse image sur photos « Alex », identification d’autres victimes via adresse de collecte, signalement Chainabuse, plainte avec rapport.

## J.2 Mini-cas 2 — Hack DeFi modeste

**Énoncé** : un protocole DeFi sur Ethereum (« YieldFarm v2 ») a été exploité en mai 2026. ~3 M USD drainés. L’équipe vous mandate (4 semaines, 30 k EUR) pour investigation et soutien à coopération avec autorités.

**Questions** :

1. Quelle est votre méthodologie de Phase 1 ?
1. Comment identifiez-vous l’attaquant on-chain ?
1. Comment suivez-vous les fonds post-hack ?
1. Quels patterns d’obfuscation anticipez-vous ?
1. Quelle attribution est possible / pas possible ?
1. Quelles coopérations activez-vous ?

**Pistes** : analyse transaction d’exploit sur Phalcon / Etherscan, identification adresse attaquant, suivi vers Tornado Cash probable, identification de bridges, coordination avec Etherscan pour labels, signalement à OFAC si patterns DPRK.

## J.3 Mini-cas 3 — Compromission wallet personnel

**Énoncé** : vous êtes mandaté par un trader crypto français individuel. Son wallet a été drainé le matin (12 ETH + tokens valant ~50 k EUR). Il a signé une transaction sur un site de mint NFT découvert via Twitter.

**Questions** :

1. Quelles sont vos premières actions techniques ?
1. Comment identifiez-vous la mécanique du drain ?
1. Quel est le drainer-as-a-service utilisé probablement ?
1. Suivez-vous les fonds drainés ?
1. Quelles recommandations d’urgence donnez-vous au trader ?
1. Quelles actions de récupération sont raisonnables ?

**Pistes** : lecture des transactions de drain, identification de l’approval, identification du drainer (via patterns), suivi via Tornado Cash probable, recommandation revoke.cash sur tous les wallets, plainte, alerte communauté.

## J.4 Mini-cas 4 — Suspect business email compromise

**Énoncé** : une PME française a payé 200 000 EUR en USDT-Ethereum à une adresse sur instructions présumées de son fournisseur (qui a été compromis par BEC). Le fournisseur réel n’a jamais demandé ce paiement. La PME mandate (3 semaines, 25 k EUR).

**Questions** :

1. Quelles méthodes pour vérifier le BEC vs autre fraude ?
1. Comment tracez-vous les fonds USDT-Ethereum ?
1. Quels patterns post-réception attendez-vous ?
1. Quels sont les angles de coopération potentiels ?
1. Quelles probabilités de récupération calibrer ?

**Pistes** : analyse email frauduleux off-chain, lecture transaction USDT, suivi via swap / bridge probables, identification d’exchanges régulés en aval, coordination autorités françaises + nationales du fournisseur.

## J.5 Mini-cas 5 — Tentative d’enquête sur paiement Monero

**Énoncé** : une organisation française a payé 28 XMR à un opérateur ransomware « XYZware ». Elle vous demande « de tracer ces XMR autant que possible ». Quel mandat acceptez-vous ?

**Questions** :

1. Quelle réponse réaliste donnez-vous au mandant initial ?
1. Si mandat alternatif, quel cadrage proposez-vous ?
1. Que pouvez-vous faire on-chain ?
1. Que pouvez-vous faire off-chain ?
1. Quelle calibration de promesses faites-vous ?
1. Quelles coopérations sont pertinentes ?

**Pistes** : refus du mandat « tracking XMR » ; proposition mandat caractérisation profil acteur + analyse off-chain + coordination CTI sectoriel ; reconnaissance honnête des limites Monero ; pivot vers angles indirects.

-----

> **Fin des annexes. Fin du cours.**
> 
> L’analyste qui a parcouru le cours OSINT Crypto en intégralité et fait les mini-cas dispose d’une formation **substantielle** au métier de crypto-forensique. La maîtrise opérationnelle vient ensuite avec l’expérience — premiers cas réels, mentoring, mises en situation, veille continue.
> 
> L’écosystème évolue rapidement. La méthodologie de fond (rigueur, calibration, coopération, éthique) reste stable. Les outils, typologies, et patterns spécifiques évoluent.
> 
> Bonne investigation.

-----

**Document complet — OSINT Crypto, Athéna Group, 2026.**
