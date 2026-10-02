---
title: Annexe E — Matrice des signaux d’alerte
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

Outil opérationnel pour reconnaître rapidement les patterns d’usage suspect.

|Catégorie                 |Signal                                                      |Niveau d’alerte|Action                                                          |
|--------------------------|------------------------------------------------------------|---------------|----------------------------------------------------------------|
|**Adresse fraîche**       |Première transaction = réception gros montant               |Élevé          |Investigation, hypothèse réception ransomware ou collecte fraude|
|**Adresse fraîche**       |Création + activité immédiate (<1h)                         |Moyen          |Vérifier contexte                                               |
|**Pattern transactionnel**|Peeling chain identifié                                     |Élevé          |Tracking étape par étape                                        |
|**Pattern transactionnel**|Consolidation de multiples sources                          |Moyen          |Possible service (exchange) ou hub                              |
|**Pattern transactionnel**|Split en multiple destinataires                             |Moyen          |Distribution post-collecte ou post-hack                         |
|**Mixers**                |Dépôt vers Tornado Cash                                     |Élevé          |Documenter, analyse statistique limitée                         |
|**Mixers**                |Dépôt vers mixer custodial                                  |Élevé          |Vérifier OFAC, documenter rupture                               |
|**Mixers**                |CoinJoin Wasabi/Samourai                                    |Moyen          |Heuristique cluster invalidée pour cette TX                     |
|**Bridges**               |Transfert via bridge cross-chain                            |Moyen          |Tracking avec outil pro nécessaire                              |
|**Privacy coins**         |Conversion vers Monero                                      |Élevé          |Rupture analytique, pivot off-chain                             |
|**Exchanges**             |Dépôt vers exchange non-KYC connu                           |Moyen-Élevé    |Identification angle limité                                     |
|**Exchanges**             |Dépôt vers exchange régulé                                  |Moyen          |Angle KYC potentiel via réquisition                             |
|**Stablecoins**           |Conversion en USDT-TRON                                     |Moyen          |Patterns blanchiment fréquent                                   |
|**Stablecoins**           |Passage en USDC                                             |Faible         |Coopération Circle rapide possible                              |
|**Sanctions**             |Adresse sur SDN list                                        |**Critique**   |Signalement obligatoire                                         |
|**Sanctions**             |Adresse interagissant avec sanctioned                       |**Critique**   |Investigation, signalement                                      |
|**Volumes**               |Transaction >100 BTC sur adresse fraîche                    |Élevé          |Investigation, possible saisie ou hack                          |
|**Volumes**               |Volumes cumulés >1 M USD                                    |Élevé          |Acteur significatif                                             |
|**Comportement**          |Multiple wallets actifs sur fenêtre courte                  |Moyen          |Possible bot ou opérateur synchronisé                           |
|**Comportement**          |Pattern temporel cohérent fuseau spécifique                 |Faible-Moyen   |Indicateur géographique probabiliste                            |
|**Comportement**          |Wallet dormant qui se réveille brutalement                  |Élevé          |Surveillance accrue, possible monétisation                      |
|**Compromission wallet**  |Drainage complet d’une adresse en quelques transactions     |Élevé          |Investigation drainer, victim potential                         |
|**Smart contract**        |Contrat non-vérifié recevant des fonds                      |Moyen          |Possible scam token / drainer                                   |
|**Smart contract**        |Approve illimité (`uint256.max`) à contrat inconnu          |Élevé          |Drapeau approval phishing                                       |
|**Pig butchering**        |Adresse de collecte multi-source (10+ victimes potentielles)|Élevé          |Investigation typologie pig butchering                          |
|**Ransomware**            |Adresse mentionnée dans ransom note publique                |Élevé          |Coordination CTI sectoriel                                      |
|**Lazarus / DPRK**        |Patterns cohérents avec Lazarus + montant significatif      |Élevé          |Escalade DGSI / FBI                                             |

-----
