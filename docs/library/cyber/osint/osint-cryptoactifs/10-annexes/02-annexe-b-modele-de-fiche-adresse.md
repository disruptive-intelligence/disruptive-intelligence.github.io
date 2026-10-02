---
title: Annexe B — Modèle de fiche adresse
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

```markdown
# Fiche adresse — [Identifiant abrégé interne]

## Identification
- **Adresse complète** : [adresse exacte 26-62 caractères selon blockchain]
- **Blockchain** : [Bitcoin / Ethereum / TRON / Solana / autre]
- **Type d'adresse** : [P2PKH / P2SH / SegWit (P2WPKH/P2WSH) / Taproot / EOA / Smart Contract / autre]
- **Identifiant interne enquête** : [INVESTIGATION-XXX-YYY]
- **Date de création de la fiche** : YYYY-MM-DD UTC

## Activité observable
- **Première transaction** : YYYY-MM-DD HH:MM UTC, TXID: [...]
- **Dernière transaction** : YYYY-MM-DD HH:MM UTC, TXID: [...]
- **Nombre total de transactions** : [N entrantes / N sortantes]
- **Solde actuel** : [montant] [actif] (au YYYY-MM-DD HH:MM UTC)
- **Volume cumulé entrant** : [montant par actif]
- **Volume cumulé sortant** : [montant par actif]
- **Périodes d'activité notables** : [bursts, dormances]

## Contreparties principales
| Adresse | Direction | Volume cumulé | Actif | Notes |
|---|---|---|---|---|
| [...] | reçu | [...] | [...] | [...] |
| [...] | envoyé | [...] | [...] | [...] |

## Cluster
- **Cluster Chainalysis ID** : [...]
- **Cluster TRM ID** : [...]
- **Adresses connues du cluster** : [N]
- **Label cluster** : [...]
- **Confiance cluster** : [high/medium/low/none]

## Labels
- **Etherscan / Tronscan / Mempool** : [labels visibles]
- **Chainalysis** : [label, confiance]
- **TRM Labs** : [label, confiance]
- **Elliptic** : [label, confiance]
- **OFAC SDN** : [oui/non, date sanction si oui]
- **Sanctions UE** : [oui/non]
- **Mentions OSINT** : [Twitter, presse, forums — sources et dates]

## Hypothèses
- **Hypothèse principale** : [description]
- **WEP** : [Quasi-certain / Très probable / Probable / Possible / Peu probable / Très peu probable]
- **Justification** : [synthèse des éléments soutenant]
- **Hypothèses alternatives** : [autres explications avec WEP]
- **Contre-éléments** : [observations qui pourraient nuancer]
- **Évolution attendue** : [si X est observé, alors évolution du WEP vers Y]

## Captures et sources
- **Captures d'explorateur** : 
  - Mempool/Etherscan/Tronscan : [chemin fichier], hash SHA-256: [...]
  - Outil pro (Reactor/TRM) : [chemin fichier], hash SHA-256: [...]
- **Sources externes** : [URL, date consultation, hash si applicable]
- **Cross-checks effectués** : [outils, dates]

## Statut enquête
- **Statut** : [Active / Surveillance / Clôturée]
- **Priorité** : [Haute / Moyenne / Basse]
- **Investigateur principal** : [nom]
- **Liens vers fiches connexes** : [autres adresses du graphe]
- **Mises à jour** : [historique versionné]

## Actions
- **Actions effectuées** : [liste avec dates]
- **Actions à mener** : [priorisées]
- **Coopération externe** : [autorités contactées, dates, retours]
```


-----
