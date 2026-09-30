---
title: Annexe C — Modèle de fiche transaction
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

```markdown
# Fiche transaction — [TXID abrégé]

## Identification
- **TXID complet** : [hash 64 caractères]
- **Blockchain** : [Bitcoin / Ethereum / etc.]
- **Block height** : [N]
- **Timestamp** : YYYY-MM-DD HH:MM:SS UTC
- **Confirmations** (au moment de la consultation) : [N]
- **Status** : [Success / Failed (Ethereum)]

## Détails
- **From / Inputs** :
  - [adresse 1] : [montant]
  - [adresse 2] : [montant]
  - **Total inputs** : [montant]
- **To / Outputs** :
  - [adresse 1] : [montant]  ← [destinataire / change ?]
  - [adresse 2] : [montant]  ← [destinataire / change ?]
  - **Total outputs** : [montant]
- **Frais** : [montant]
- **Actif transféré** : [BTC / ETH / USDT / autre]
- **Si Ethereum** :
  - **Value (ETH natif)** : [montant]
  - **ERC-20 transfers** (si applicable) : [from, to, amount, token]
  - **Internal transactions** (si applicable)
  - **Gas used / Gas price**

## Lecture
- **Pattern observé** : [transfer simple / peeling / consolidation / split / etc.]
- **Contexte enquête** : [pertinence pour le dossier]

## Hypothèses
- **Hypothèse sur la nature** : [description avec WEP]
- **Hypothèse sur les destinataires** : [destinataire vs change pour Bitcoin]

## Captures
- **Page d'explorateur** : [chemin, hash SHA-256]
- **Page outil pro** : [chemin, hash SHA-256]

## Connexions
- **Adresses impliquées** : [liens vers fiches d'adresses]
- **Transactions liées** : [TXID prédécesseurs / successeurs significatifs]

## Statut
- **Statut** : [Documentée / Pertinente / Clôturée]
- **Date d'analyse** : YYYY-MM-DD UTC
```


-----
