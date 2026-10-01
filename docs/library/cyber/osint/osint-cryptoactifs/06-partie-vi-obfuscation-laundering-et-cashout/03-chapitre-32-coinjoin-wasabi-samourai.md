---
title: 'Chapitre 32 — CoinJoin : Wasabi, Samourai'
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VI — Obfuscation, laundering et cashout
  - index.md
---

Le **CoinJoin** est une technique d’anonymisation Bitcoin différente des mixers custodial. Coopérative, non-custodial. Wasabi et Samourai sont les implémentations principales.

## 32.1 Principe du CoinJoin

**Idée** : multiple utilisateurs créent **collectivement une transaction** Bitcoin avec multiples inputs et outputs, sans révéler à un opérateur central qui possède quoi.

**Mécanisme simplifié** :

1. Plusieurs utilisateurs (5 à 100+ selon implémentation) coordonnent.
1. Chacun fournit des inputs (UTXO qu’il contrôle).
1. Tous signent une transaction agrégée.
1. Outputs sont mélangés : impossible de dire depuis l’extérieur quel input correspond à quel output.

**Exemple** :

- 10 utilisateurs, chacun 1 BTC en input (10 BTC total).
- Outputs : 10 × 1 BTC vers 10 nouvelles adresses.
- Heuristique du co-spend appliquée naïvement dirait : tous appartiennent à même entité. **C’est faux** dans le CoinJoin.

**Effet** : casser l’heuristique du co-spend. Chaque output, vu de l’extérieur, peut appartenir à n’importe quel input.

## 32.2 Wasabi Wallet

**Wasabi Wallet** est un wallet Bitcoin avec CoinJoin intégré. Implémentation **ZeroLink** (variante CoinJoin avec Chaumian e-cash).

**Caractéristiques** :

- Coordinator central (mais ne détient pas les fonds).
- Anonymity set fixe (~100 utilisateurs par round historiquement).
- Frais (sur le coordinator).

**Évolution** :

- Wasabi 1.0 : protocole ZeroLink pur.
- Wasabi 2.0 : WabiSabi, anonymity set plus flexible, frais plus bas.

**Réputation** : utilisé par utilisateurs privacy-conscious légitimes ET par criminels. Coordinator peut blacklister certains UTXO (controverse).

## 32.3 Samourai Wallet

**Samourai Wallet** : wallet Bitcoin alternatif, focus privacy.

**Whirlpool** : implémentation CoinJoin de Samourai. Différences :

- Anonymity set plus petit par round (5 utilisateurs).
- Mais cycles répétés pour augmenter anonymat cumulatif.
- Coordinator distinct.

**Saisie avril 2024** : opération US, fondateurs Keonne Rodriguez et William Lonergan Hill inculpés. Infrastructure saisie. Whirlpool stoppé.

**Implications** :

- Logs du coordinator récupérés permettent investigation rétroactive.
- Saisie envoie message sur acceptabilité légale des CoinJoin services, débat actif.

## 32.4 Détection de CoinJoin

**Signaux** :

**Multiple inputs et multiple outputs avec montants identiques**. Une transaction CoinJoin Wasabi typique : 100 inputs, 100 outputs de même valeur. Très distinctif.

**Coordinator address**. Wasabi prélève une fee qui va à un coordinator. Adresse identifiable.

**Patterns de timing**. Les CoinJoin ont des cycles temporels. Wasabi v2 fait des CoinJoin réguliers.

**Outils d’analyse** : KYCP.org analyse spécifiquement les CoinJoin. Détecte les transactions, calcule l’anonymity set, score la qualité du mix.

## 32.5 Limites du dé-mixage CoinJoin

**Heuristique cassée** : le co-spend dans CoinJoin n’est pas une indication d’entité commune. Outils pro **doivent détecter** les CoinJoin et **exclure** ces transactions du clustering. Reactor / TRM le font.

**Analyse possible mais limitée** :

- **Sub-mixing** : si l’anonymity set est petit (Whirlpool 5 inputs), inférence statistique partielle.
- **Toxic UTXO** : si un UTXO entré dans CoinJoin est entaché (par exemple, vient d’une adresse sanctionnée), le mélange CoinJoin ne « purifie » pas pour les autorités — les outputs gardent une « contamination » statistique.
- **Behavioral analysis** : patterns post-CoinJoin peuvent identifier l’utilisateur initial.

**Coordinator logs** : si coordinator coopère ou est saisi, logs permettent dé-mixage substantiel. Cas Samourai.

## 32.6 Wasabi vs mixers custodial

|Critère      |CoinJoin (Wasabi)                        |Mixer custodial (Tornado)                                                                 |
|-------------|-----------------------------------------|------------------------------------------------------------------------------------------|
|Custody      |Non-custodial                            |Custodial (Tornado est non-custodial via smart contract, autres mixers BTC sont custodial)|
|Risque de vol|Faible                                   |Élevé (mixers traditionnels)                                                              |
|Anonymat     |Modéré                                   |Variable                                                                                  |
|Logs         |Coordinator a logs (Wasabi)              |Variable                                                                                  |
|Légalité     |Moins claire mais usage légitime fréquent|Plus contestée                                                                            |
|Démantèlement|Wasabi continue, Samourai saisi          |Multiple démantèlements (Helix, BitcoinFog, ChipMixer, Tornado sanctionné)                |

## 32.7 Méthode d’enquête face à CoinJoin

**Étape 1 — Détecter le CoinJoin**. Outils pro indiquent. Manuellement : pattern de transaction (multiple in/out de même valeur).

**Étape 2 — Documenter**. Quelle implémentation (Wasabi v1, v2, Samourai), quel anonymity set, quel coordinator.

**Étape 3 — Continuer le tracking**. Outils pro continuent souvent à suivre la « probabilité » de chaque input vers chaque output (pas certain mais probabiliste).

**Étape 4 — Calibrer**. Confidence sur destinataires post-CoinJoin = limitée.

**Étape 5 — Coopération**. Pour cas critiques, demande au coordinator (si encore actif) ou récupération de logs post-saisie.

## 32.8 Tendances 2024-2026

**Saisie Samourai (avril 2024)** : impact majeur. Samourai était populaire. Migration vers Wasabi ou autres alternatives.

**Wasabi** : continue, mais sous pression. Coordinator en juridiction permissive pour minimiser risque. Updates régulières.

**Joinmarket** : alternative décentralisée (pas de coordinator central), moins user-friendly mais plus résiliente.

**Lightning Network** : autre approche privacy (pas CoinJoin technique, mais effet similaire — paiements off-chain limitent traçabilité on-chain).

**Pour l’enquêteur** : CoinJoin reste une **rupture analytique** sur Bitcoin, mais pas absolue. Combinaison avec autres indices et analyse temporelle / behavioral peut donner des angles.

-----
