---
title: Annexe H — Matrice “ce que je peux conclure / ce que je ne peux pas conclure”
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Annexes
  - index.md
---

*Aide-mémoire pour calibrer rigoureusement les conclusions selon les sources mobilisées et les éléments disponibles.*

|À partir de…                           |Je peux conclure (avec niveau WEP)                                                                                      |Je ne peux pas conclure                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
|Registre du commerce + UBO RBE         |Mandats officiels (quasi-certain), UBO déclaré (quasi-certain), structure de capital (quasi-certain)                    |UBO réel si contrôle indirect, intention frauduleuse, substance économique                 |
|Comptes annuels publiés                |Profil financier (quasi-certain sous réserve de fiabilité comptable), ratios sectoriels (probable)                      |Réalité des transactions, ABS, fraude comptable sans expertise forensique                  |
|Adverse media (presse, ONG)            |Présence de soupçons publics (quasi-certain), réputation publique (quasi-certain)                                       |Culpabilité, faits non confirmés                                                           |
|Leaks (Pandora, Panama, etc.)          |Existence de structure offshore (quasi-certain si leak authentifié), settlor / bénéficiaires déclarés (quasi-certain)   |Finalité illicite sans recoupements, mise à jour post-leak                                 |
|Relevé bancaire                        |Flux observés (quasi-certain), patterns (probable), typologie compatible (probable au mieux)                            |Origine illicite des fonds sans infraction prédécesseur, intention, identification UBO réel|
|Analyse de réseau / graphe             |Liens formels (quasi-certain), centralités (quasi-certain), clusters (probable)                                         |Contrôle effectif, causalité, intention                                                    |
|Sanctions / PEP screening              |Présence sur listes (quasi-certain), statut PEP (quasi-certain)                                                         |Culpabilité, lien actif avec opérations sanctionnées                                       |
|OSINT crypto (Sarah Marin / partenaire)|Flux on-chain (quasi-certain), services traversés (probable à quasi-certain), identification cluster (probable)         |Identification individuelle de l’attaquant, attribution finale                             |
|Reconstitution patrimoniale            |Patrimoine identifié visible (quasi-certain), train de vie observable (probable)                                        |Cohérence avec revenus déclarés sans accès fiscal, patrimoine total réel                   |
|DS reçues en CRF                       |Faits déclarés par assujetti (quasi-certain), motifs de suspicion de l’assujetti (quasi-certain)                        |Réalité de l’infraction, qualification définitive                                          |
|Coopérations CRF étrangères (Egmont)   |Informations transmises (quasi-certain dans la limite de la coopération), faits confirmés par partenaire (quasi-certain)|Faits non couverts par la coopération, opacité juridictionnelle persistante                |

**Règle générale** : ce qu’on observe peut être *quasi-certain* ; ce qu’on déduit peut être *probable* à *très probable* avec recoupements ; ce qu’on attribue (intention, contrôle réel, infraction prédécesseur) est presque toujours *probable* au mieux, sauf documentation très solide.

-----
