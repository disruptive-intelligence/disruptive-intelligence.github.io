---
title: Chapitre 5 — FININT, OSINT financier, AML, CTI et OSINT Crypto
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie I — Comprendre le renseignement financier
  - index.md
---

## Objectif du chapitre

Positionner le FININT par rapport aux disciplines voisines, pour éviter les confusions et exploiter au mieux les complémentarités. Beaucoup de dossiers modernes mobilisent plusieurs disciplines simultanément ; un analyste qui ne sait pas où il se situe ne sait pas non plus à qui s’adresser pour ce qu’il ne fait pas lui-même.

## Le concept

Plusieurs disciplines coexistent et se recoupent :

- **AML / LCB-FT** (Anti-Money Laundering / Lutte contre le blanchiment et le financement du terrorisme) — discipline réglementaire centrée sur la **conformité** : KYC, KYB, monitoring, déclaration de soupçon, screening sanctions, gel. Elle est portée par les **assujettis** (banques, PSP, etc.) avec des obligations légales précises.
- **FININT** — discipline analytique et de **renseignement** centrée sur l’exploitation de l’information financière pour comprendre, détecter, qualifier et orienter l’action contre la criminalité économique. Pratiquée en CRF, en services d’enquête, en cabinets d’investigation, en compliance avancée.
- **OSINT financier** — sous-ensemble de l’OSINT spécialisé sur les **sources ouvertes financières et économiques** : registres, comptes annuels, presse, leaks, marchés publics, SOCMINT financier. C’est une **boîte à outils** mobilisée par le FININT.
- **CTI** (Cyber Threat Intelligence) — discipline de renseignement sur la **menace cyber** : acteurs, TTP, infrastructures, indicateurs. Lorsqu’une criminalité est cyber-financière (ransomware, BEC, hacks DeFi), CTI et FININT convergent.
- **OSINT Crypto** — discipline d’enquête **on-chain** : blockchains, transactions, wallets, mixers, bridges, DEX, privacy coins, cashout. C’est le complément naturel du FININT pour le volet crypto-actifs.

## L’utilité opérationnelle

Concrètement, dans un dossier moderne :

- **AML** détecte et signale (banque émet une DS).
- **FININT** reçoit, recoupe, analyse, qualifie et oriente (CRF produit une note).
- **OSINT financier** alimente le FININT en sources ouvertes (registres, presse, leaks).
- **CTI** alimente quand le dossier comporte un volet cyber (acteur ransomware identifié, TTP connue).
- **OSINT Crypto** alimente quand le dossier comporte une branche on-chain.

Aucune de ces disciplines n’est « supérieure » aux autres. Elles **se complètent**. Un bon analyste FININT sait *quand* solliciter une autre discipline, et *comment* exploiter ce qu’elle lui rend.

## Méthode — comment articuler les disciplines

Trois principes :

1. **Spécifier les questions adressées à chaque discipline.** Demander à un analyste OSINT Crypto *« est-ce qu’il blanchit ? »* est inopérant. Demander *« peux-tu tracer les fonds depuis cette adresse de dépôt sur l’exchange jusqu’aux destinations finales et identifier les off-ramps ? »* l’est. Le FININT pose des questions techniquement précises.
1. **Recevoir et intégrer les livrables.** Un rapport CTI, un rapport OSINT Crypto, un rapport AML interne d’une banque ne sont pas du renseignement FININT directement utilisable — ils sont des **intrants**. Le FININT les recoupe, en évalue la fiabilité, et les intègre dans une note unifiée.
1. **Documenter la chaîne d’attribution.** Quand le livrable FININT mobilise du renseignement crypto produit par un cabinet externe, le cours OSINT Crypto recommande explicitement (Chapitre 47) une calibration des sources — l’analyste FININT applique le même standard pour citer ces apports : *« L’analyse on-chain conduite par Athéna Group (rapport référencé X) conclut, avec un niveau de confiance “probable”, que les fonds atteignent un exchange non-KYC … »*.

## Mini-walkthrough — qui fait quoi dans CLEARFLOW

|Question                                                   |Discipline              |Acteur                      |
|-----------------------------------------------------------|------------------------|----------------------------|
|Les DS de banques détectent-elles la structuration ?       |AML                     |Compliance des banques      |
|Quelle est la cartographie des sociétés liées à Haddad ?   |FININT + OSINT financier|Nassim                      |
|Y a-t-il des éléments dans les Panama/Pandora Papers ?     |OSINT financier (leaks) |Nassim, ICIJ Aleph          |
|Quelle est la trajectoire des USDT envoyés sur l’exchange ?|OSINT Crypto            |Sarah Marin (Athéna)        |
|Y a-t-il un exploit cyber dans le BEC suspecté ?           |CTI                     |Service partenaire ou Athéna|
|Quel rapport final pour le PNF ?                           |FININT (intégrateur)    |Nassim                      |

C’est le FININT qui **intègre** toutes les contributions et produit le livrable final unifié. Sans intégration, on a une collection de rapports déconnectés.

## Erreurs fréquentes

- **Demander à une discipline ce qu’elle ne fait pas** — par exemple demander à un analyste OSINT Crypto une analyse des comptes annuels d’une SAS française.
- **Faire double emploi** — refaire dans le rapport FININT le détail blockchain qu’a déjà produit l’analyste crypto. Le rapport FININT renvoie, il ne refait pas.
- **Sous-utiliser l’OSINT financier** — beaucoup d’analystes FININT en CRF passent peu de temps sur les registres internationaux ou les leaks alors que les retours opérationnels y sont élevés.

## Limites

La frontière entre disciplines n’est pas toujours nette. Un analyste FININT senior maîtrise une partie de l’OSINT financier classique. Un analyste OSINT Crypto avec passé TRACFIN maîtrise une partie du FININT classique (cas Sarah Marin). C’est plus souvent une **question de profil** que de discipline pure. L’organisation prime : qui livre quoi, à qui, sous quelle responsabilité.

## Lien avec le fil rouge

> **CLEARFLOW — Architecture des coopérations**
> 
> Nassim dessine, dès le cadrage, l’architecture des coopérations : OSINT financier en interne (registres, leaks, presse), branche crypto sous-traitée à Athéna Group / Sarah Marin avec un mandat précis (« tracer USDT depuis l’exchange jusqu’aux off-ramps », pas « est-ce que c’est du blanchiment ? »), branche cyber éventuelle sous-traitée à un service partenaire si BEC se confirme, AML restant chez les banques déclarantes (Nassim ne refait pas leur monitoring). Cette architecture évite les redondances et les angles morts.

## Points clés à retenir

- AML, FININT, OSINT financier, CTI, OSINT Crypto sont **complémentaires**, pas concurrents.
- Le FININT est la discipline **intégratrice** quand un dossier mobilise plusieurs angles.
- Les questions adressées aux disciplines voisines doivent être **techniquement précises**.
- Le livrable FININT renvoie, il ne refait pas — particulièrement pour la branche crypto (renvoi systématique au cours OSINT Crypto).

-----
