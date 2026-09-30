---
title: Annexe I — Erreurs fréquentes d’analyse
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

Catalogue des erreurs courantes pour vigilance.

## I.1 Erreurs de lecture Bitcoin

**Confondre destinataire et change**. Voir 2 outputs et conclure 2 destinataires distincts. Cf Ch.6.

**Ignorer les frais**. Penser que `inputs - outputs ≠ 0` est une perte. Ce sont les frais.

**Mal interpréter une consolidation comme un transfer**. Une transaction interne qui regroupe 50 UTXO d’une même entité n’est pas un transfer de 50 personnes vers 1.

**Confondre adresse et personne**. Une adresse n’est pas une identité.

## I.2 Erreurs de lecture Ethereum

**Ignorer les transferts ERC-20**. Voir « Value: 0 ETH » et conclure « pas de valeur transférée ». Toujours regarder section ERC-20.

**Ignorer les internal transactions**. Pour DeFi, les flux ETH sont souvent internal.

**Confondre token contract et wallet**. L’adresse `0xdAC17...` (USDT contract) n’est pas un wallet d’utilisateur.

**Penser que `To = destinataire`**. Pour smart contract calls, `To` est le contrat, pas le destinataire final.

## I.3 Erreurs d’analyse de cluster

**Sur-attribuer par heuristique de co-spend**. CoinJoin casse cette heuristique. Vérifier que les transactions du cluster ne sont pas CoinJoin.

**Étendre un label par cluster sans précaution**. Un label sur une adresse ne s’étend pas automatiquement à tout le cluster. Vérifier la qualité du label initial.

**Confondre cluster d’exchange et cluster d’utilisateur**. Un cluster contenant une adresse de dépôt d’un exchange ne fait pas de l’utilisateur de cet exchange l’opérateur du cluster.

## I.4 Erreurs d’attribution

**Attribuer à un acteur étatique sans preuve**. Patterns sophistiqués ≠ Lazarus automatiquement.

**Identifier un individu par cluster**. Le cluster identifie un contrôle, pas une personne.

**Confondre opérateur et affilié**. Dans RaaS, l’opérateur est le développeur, l’affilié est l’attaquant. Distinct.

**Sur-attribuer un service de blanchiment à son client**. Si Akira utilise un hub TRON, ce hub n’est pas Akira. C’est un service.

## I.5 Erreurs de calibration

**Sauter les WEP**. Tous les énoncés non-évidents doivent avoir une calibration explicite.

**Inflation lexicale**. Tout devient « très probable ». Discipline.

**Confiance non-cumulative**. Une chaîne d’hypothèses cumule l’incertitude.

**Ne pas distinguer confiance de précision**. Précis ≠ certain.

## I.6 Erreurs méthodologiques

**Pas de chain of custody**. Captures non-hashées, non-archivées immutablement.

**Pas de validation croisée**. Un seul outil utilisé pour conclusions critiques.

**Pas de peer review**. Rapport produit sans relecture.

**Mauvaise gestion fuseaux horaires**. Mélange UTC et heure locale sans expliciter.

**Pas de documentation continue**. Journal d’enquête lacunaire ; reconstitution impossible.

## I.7 Erreurs de communication

**Rapport non-adapté à audience**. Trop technique pour direction, trop vague pour analystes.

**Executive summary trop long**. Doit être 1-2 pages max.

**Pas de limites assumées**. Rapport surconfiant qui s’effondre à la première vérification.

**Recommandations vagues**. « Améliorer la sécurité » au lieu de mesures SMART.

**TLP mal positionné**. Diffusion à mauvais cercle.

## I.8 Erreurs éthiques

**Conflit d’intérêt non-déclaré**. Mandat accepté sans évaluation.

**Sur-promesse au mandant**. Promesse de récupération qui ne se réalise pas.

**Manipulation par pression**. Ajustement des conclusions sous pression mandant.

**Engagement direct avec cible**. Interactions OPSEC compromises.

**Diffusion hors cercle**. Bavardage entre analystes ou avec journalistes.

## I.9 Erreurs de coopération

**Coordination tardive**. Coopération autorités initiée trop tard, fonds déjà out.

**Pas d’utilisation des canaux institutionnels**. Direct contact exchange par enquêteur privé (sans autorité) ne donne rien.

**Sous-utilisation des labels**. Ignorer ce que les outils pro savent déjà.

**Pas de partage CTI**. Ne pas alimenter ni puiser dans la communauté.

## I.10 Erreurs sur l’évolution

**Outil non mis à jour**. Utiliser une version d’outil dépassée.

**Veille déficiente**. Pas au courant des nouveaux acteurs / nouvelles techniques.

**Pas d’apprentissage post-mortem**. Mêmes erreurs répétées.

**Méthodologie figée**. Pas d’adaptation aux évolutions de l’écosystème.

-----
