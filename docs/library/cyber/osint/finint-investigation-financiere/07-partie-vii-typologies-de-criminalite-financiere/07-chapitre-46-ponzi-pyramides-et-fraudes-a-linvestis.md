---
title: Chapitre 46 — Ponzi, pyramides et fraudes à l’investissement
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre les **schémas de fraude à l’investissement** : Ponzi, pyramides, fausses ICO/IDO, fraudes au trading, scams crypto.

## Le concept

**Ponzi (schema)**. Le promoteur attire des investisseurs en promettant des rendements supérieurs au marché. Les « rendements » versés aux premiers investisseurs sont prélevés sur les apports des nouveaux investisseurs (et non sur une activité économique réelle). Le système s’effondre lorsque les retraits dépassent les nouveaux apports.

**Pyramide (MLM frauduleux)**. Variante : les investisseurs sont incités à recruter de nouveaux participants. Le revenu provient principalement du recrutement, pas d’un produit ou service réel.

**Fausses ICO / IDO / TGE** : émissions de tokens crypto sans projet réel, avec promesses irréalistes, abandon après collecte (« rug pull »).

**Scam pig butchering** : combinaison fraude sentimentale + fraude à l’investissement. La victime est manipulée pendant des mois par une fausse relation, puis incitée à « investir » dans une plateforme crypto qui semble fonctionner — jusqu’au retrait final impossible.

**Faux trading** : plateformes simulant un trading rentable, où la victime voit des « gains » virtuels mais ne peut pas retirer.

## L’utilité opérationnelle

Les fraudes à l’investissement représentent des pertes massives pour les victimes (souvent l’épargne d’une vie). En CRF, les signalements convergents permettent de détecter et de signaler tôt.

## Méthode — signaux

- Rendements promis très supérieurs au marché.
- Pression à recruter d’autres investisseurs (pyramide).
- Plateforme inconnue, juridiction obscure.
- Garanties auto-désignées, faux régulateurs.
- Présence de figures publiques (vraies ou usurpées) en endorsement.
- Difficulté ou refus de retrait dès qu’on dépasse certains seuils.
- Cashout difficile sur stablecoins, voire impossible.

## Mini-walkthrough — pig butchering simplifié

Une victime française rencontre sur application de rencontre un faux ami sentimental basé prétendument à Hong Kong. Après plusieurs mois, le contact recommande une « opportunité d’investissement » sur une plateforme crypto. La victime investit 50 K€ qui sont convertis en USDT, transitent par plusieurs adresses, et atteignent rapidement un exchange asiatique non-KYC. Tentative de retrait : refus pour « frais bloquants ».

Lecture FININT : pig butchering quasi-certain. Volet on-chain renvoyé à OSINT Crypto (Athéna ou équivalent). Signalement à la PHAROS et au PNF JUNALCO (cybercriminalité). Le réseau organisé derrière ces opérations est souvent identifié à terme avec coopération internationale (notamment SE Asie).

## Erreurs fréquentes

- **Sous-estimer la sophistication** des fraudes pig butchering modernes — équipes professionnelles, scripts éprouvés.
- **Blâmer la victime** : la manipulation est efficace même sur des personnes éduquées.

## Limites

Les schémas se passent souvent partiellement à l’étranger ; la coopération internationale est lente. Le volet crypto est renvoyé à OSINT Crypto pour le traitement détaillé.

## Lien avec le fil rouge

> **CLEARFLOW — Hors périmètre principal**
> 
> Le dossier Haddad ne comporte pas de volet Ponzi ou pig butchering identifié. Ce chapitre reste utile à la compréhension du contexte général des typologies modernes.

## Points clés à retenir

- Ponzi, pyramides, fausses ICO, pig butchering : schémas distincts mais structure commune.
- Rendements promis disproportionnés = signal majeur.
- Coopération internationale (notamment SE Asie) lente mais nécessaire.
- Volet crypto traité par OSINT Crypto.

-----
