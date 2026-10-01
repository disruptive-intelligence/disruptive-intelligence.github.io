---
title: Annexe D — Modèle de timeline d’enquête
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Annexes
  - index.md
---

```markdown
# Timeline d'enquête — [Nom du dossier]

## Période couverte : [date début] au [date fin]

## Pré-incident
| Date UTC | Événement | Source | Notes |
|---|---|---|---|
| YYYY-MM-DD HH:MM | [événement, ex: compromission initiale] | [source forensics, log, autre] | [...] |
| ... | ... | ... | ... |

## Incident
| Date UTC | Événement | Adresse | Montant | TXID / Source |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Demande de rançon | - | - | Note ransomware |
| YYYY-MM-DD HH:MM | Paiement effectué | [adresse] | [montant] [actif] | [TXID] |
| ... | ... | ... | ... | ... |

## Post-incident — flux observés
| Date UTC | Événement | Adresses | Montant | TXID |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Premier mouvement post-paiement | [from] → [to] | [...] | [...] |
| YYYY-MM-DD HH:MM | Conversion via swap | [...] | [...] | [...] |
| YYYY-MM-DD HH:MM | Dépôt Tornado Cash | [...] | [...] | [...] |
| YYYY-MM-DD HH:MM | Dépôt sur exchange régulé | [...] | [...] | [...] |
| ... | ... | ... | ... | ... |

## Coopération et actions
| Date UTC | Action | Acteur | Résultat | Notes |
|---|---|---|---|---|
| YYYY-MM-DD | Signalement TRACFIN | [...] | Reçu | [ref] |
| YYYY-MM-DD | Coordination DGSI | [...] | Active | [ref] |
| YYYY-MM-DD | Réquisition Binance | DGSI | KYC fourni | 2 mules |
| YYYY-MM-DD | Demande gel Tether | DGSI | 30k USDT gelés | [adresses] |
| ... | ... | ... | ... | ... |

## Étapes du rapport
| Date UTC | Étape | Auteur | Notes |
|---|---|---|---|
| YYYY-MM-DD | Rapport intermédiaire 1 | [...] | TLP RED |
| YYYY-MM-DD | Briefing DGSI | [...] | [...] |
| YYYY-MM-DD | Rapport final | [...] | [...] |
| YYYY-MM-DD | Restitution mandant | [...] | [...] |
| YYYY-MM-DD | Archivage | [...] | [...] |
```


-----
