---
title: Annexe F — Matrice « ce que je peux conclure / ce que je ne peux pas conclure »
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

Outil de calibration. Pour chaque type d’observation, ce qui est raisonnablement concluable vs ce qui ne l’est pas en OSINT pure.

|Observation                                     |Ce que je peux conclure                                   |Ce que je ne peux PAS conclure                                       |
|------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------|
|Transaction X confirmée sur blockchain          |Le transfert a eu lieu, à ce timestamp, entre ces adresses|L’identité civile des parties                                        |
|Adresse a reçu N BTC depuis l’adresse Y         |Flux observable, contreparties identifiées                |Qui contrôle les adresses                                            |
|Cluster de N adresses constitué par heuristiques|Probable même contrôle (confiance variable)               |Contrôle absolu, identité                                            |
|Cluster labellisé « Binance » par Chainalysis   |Probable infrastructure Binance                           |Quel utilisateur final est derrière une adresse de dépôt             |
|Adresse Z est sur la SDN list OFAC              |Adresse sanctionnée — interaction = violation             |Détails non publics de la sanction                                   |
|Pattern de peeling chain observé                |Probable activité de blanchiment                          |Nature exacte de l’activité (ransomware, autre)                      |
|Adresse fraîche reçoit gros montant (35 BTC)    |Possible adresse dédiée (ransomware, achat, collecte)     |Sans contexte off-chain, type d’activité                             |
|Pattern temporel cohérent fuseau Asie           |Possible localisation opérateur en TZ X                   |Géographie certaine                                                  |
|Cluster identifié comme Akira par Chainalysis   |Probable lien avec opérations Akira                       |Quel(s) individu(s) au sein du groupe                                |
|Dépôt sur exchange régulé                       |Existence d’un compte utilisateur identifiable via KYC    |KYC sans réquisition légale                                          |
|Dépôt sur Tornado Cash                          |Anonymisation tentée, transaction observable              |Lien avec retraits ultérieurs (sauf analyse statistique probabiliste)|
|Conversion en Monero via exchange               |Existence de la conversion                                |Destination on-chain post-Monero                                     |
|Smart contract drainer identifié                |Mécanisme du vol, adresses techniques                     |Identité civile du déployeur                                         |
|Adresse créatrice d’un token rug pull           |Action du rug pull tracée                                 |Identité civile du créateur                                          |
|Hub TRON multi-source/multi-destination         |Probable service (exchange, OTC, blanchiment)             |Type exact, identité opérateur                                       |
|2 hubs identiques entre 2 enquêtes ransomware   |Probable service partagé                                  |Si même opérateur ou client commun                                   |
|Approval illimité à un contrat inconnu          |Indicateur de risque (potentiel drainer)                  |Si drainage déjà eu lieu sans regarder transferts ultérieurs         |
|Adresse Lazarus précédemment attribuée          |Cluster cohérent                                          |Tous les clusters Lazarus actuels                                    |
|Mention publique d’une adresse par chercheur    |Information à recouper                                    |Vérité absolue (vérifier la source)                                  |
|Patterns BEC + email phishing fournisseur       |Identifie schéma BEC, possible groupe russophone          |Identité des opérateurs                                              |

**Principe** : pour chaque conclusion, l’analyste s’interroge sur la **nature exacte** de ce qu’il peut affirmer. Glisser de « peut » à « ne peut pas » est trahison méthodologique.

-----
