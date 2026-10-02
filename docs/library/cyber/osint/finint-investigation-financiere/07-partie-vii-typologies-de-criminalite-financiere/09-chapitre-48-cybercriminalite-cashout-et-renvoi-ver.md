---
title: Chapitre 48 — Cybercriminalité, cashout et renvoi vers OSINT Crypto
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre l’**interaction cybercriminalité / criminalité financière** : ransomware, vol de cryptos, BEC, infostealers — et savoir quand renvoyer à OSINT Crypto pour le traitement on-chain.

## Le concept

Toute cybercriminalité monétisée passe par un **cashout** : conversion des fonds illicites en valeur utilisable. Modalités :

- **Ransom en crypto** (BTC, Monero, USDT) — le plus courant.
- **Vol de fonds DeFi / exchanges** — flash loans, exploits, phishing wallet.
- **BEC** (chapitre 44) — virement fiat puis souvent conversion crypto.
- **Vente de données volées** sur darknet — paiement crypto.
- **Carding** : utilisation frauduleuse de cartes bancaires, cashout en cash, gift cards, biens.

Le cashout final passe souvent par :

- **Exchanges KYC dans juridictions à faible application** des règles.
- **P2P** (LocalBitcoins historiquement, Paxful, ou alternatives modernes).
- **Bureaux de change crypto** dans certaines villes.
- **Stablecoins** comme valeur intermédiaire avant cashout fiat.

## Articulation FININT / OSINT Crypto

C’est le sujet typique où **FININT et OSINT Crypto coopèrent** :

- **FININT** : cadre le contexte (qui est la victime, qui est probablement derrière l’attaque, quel réseau de mules, quelles coopérations avec banques et autorités, quel suivi judiciaire).
- **OSINT Crypto** : trace les fonds on-chain depuis le wallet d’attaquant jusqu’aux off-ramps (exchanges, P2P), identifie les clusters, qualifie les services traversés (mixers, bridges).

Le rapport FININT **renvoie** à OSINT Crypto pour le détail on-chain. Il ne le refait pas.

## L’utilité opérationnelle

Pour les dossiers ransomware, vol crypto, BEC majeur, fraude DeFi :

- FININT identifie victimes, impact, contexte, attribution probable (avec CTI).
- OSINT Crypto trace, identifie services, attribue.
- Coopération internationale est centrale (Europol EC3, FBI, services nationaux).

## Méthode — workflow type

1. **Signalement / DS / incident** détecté.
1. **FININT** cadre : périmètre, victime, contexte.
1. **OSINT Crypto** (Sarah Marin / Athéna Group dans le fil rouge) prend le volet on-chain.
1. **Coopération** avec exchanges pour KYC sur off-ramps via réquisition.
1. **Synthèse** intégrée dans la note FININT.

## Mini-walkthrough — ransomware sur PME

Une PME française est victime d’un ransomware. Rançon de 80 K€ demandée en USDT vers une adresse Tron. La PME paie (déconseillé, mais souvent fait).

FININT : identification de l’incident, signalement ANSSI/PHAROS, plainte, coopération avec CRF.
OSINT Crypto : traçage de l’adresse de paiement, identification du cluster (TRM Labs / Chainalysis / outils Athéna), suivi jusqu’aux off-ramps, possiblement attribution à un groupe ransomware connu.

Synthèse FININT : note de transmission au PNF JUNALCO et à Europol EC3, avec annexe technique d’OSINT Crypto, et recommandations (poursuite internationale, monitoring continu).

## Erreurs fréquentes

- **Refaire OSINT Crypto dans le FININT** : duplication, perte de temps, risque d’erreur.
- **Ignorer le lien CTI** : l’attribution à un groupe ransomware (Akira, ALPHV, LockBit, etc.) éclaire le dossier.
- **Sous-estimer l’importance du cashout** : c’est le maillon faible des cybercriminels.

## Limites

L’attribution finale d’une cybercriminalité est rarement *quasi-certaine* en pur on-chain. Elle exige souvent l’ajout d’éléments hors-chaîne (CTI, témoignages, arrestations).

## Lien avec le fil rouge

> **CLEARFLOW — Volet crypto secondaire**
> 
> Dans le dossier Haddad, les conversions USDT identifiées ne relèvent pas de ransomware mais de cashout / layering crypto opportuniste. Le volet est confié à Sarah Marin (Athéna). Son rapport on-chain est annexé à la note finale, avec renvoi explicite au cours OSINT Crypto pour les méthodes utilisées.

## Points clés à retenir

- Cybercriminalité = cashout obligatoire, souvent crypto.
- FININT cadre, OSINT Crypto trace on-chain.
- Coopération avec exchanges via réquisitions.
- Le rapport FININT renvoie à OSINT Crypto, ne refait pas.

-----
