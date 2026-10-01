---
title: Annexe M — Registre de sources
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - ANNEXES
  - index.md
---

> ⏱ **Annexe versionnée — dernière vérification : 2 août 2026.**
> Niveau : `T` texte juridique · `D` documentation officielle · `N` norme ou standard · `S` source secondaire.

**[S-01]** — Projet ATT&CK (MITRE) — *notes de version v18 et v19*
Niveau `D` · Vérifié le 02/08/2026 · Utilisé au §1.8, §18.6, annexe H.
*Fait retenu* : la version 19, publiée le 28 avril 2026, scinde la tactique historique *Defense Evasion* en deux tactiques distinctes — *Stealth*, conservant l'identifiant TA0005, et *Defense Impairment*, TA0112. Volumétrie Entreprise : 15 tactiques, 222 techniques, 475 sous-techniques. La version 18, d'octobre 2025, avait introduit les objets *Detection Strategies* et *Analytics*. Une table de correspondance a été publiée pour le remappage.

**[S-02]** — Projet ATT&CK — *entrées documentant l'emploi de modèles de langage par des attaquants*
Niveau `D` · Vérifié le 02/08/2026 · Utilisé au §1.8, §10.7.
*Fait retenu* : des entrées de campagne et de logiciel documentent l'emploi de modèles de langage en opération, décrivant à la fois des opérations largement automatisées et un maliciel interrogeant un modèle en cours d'exécution.
⚠️ **Note de transparence** : l'un de ces cas concerne un usage détourné de Claude, l'assistant développé par Anthropic — l'organisation qui m'a créé. Ce cours le traite à partir des sources publiques, comme les autres.

**[S-03]** — Analyses juridiques concordantes sur le régime américain de partage d'indicateurs de 2015
Niveau `S` · Vérifié le 02/08/2026 · Utilisé au §1.8, §20.4, annexe F.3.
*Faits retenus* : le régime a expiré le 30 septembre 2025 · une première prolongation l'a porté au 30 janvier 2026 · une seconde au 30 septembre 2026 · aucune modification de fond n'a été apportée · pendant la période de vacance, le partage a continué avec une exposition juridique réévaluée par les participants.
⚠️ **Décision engageante** : à prendre sur le texte lui-même et sur avis juridique, jamais sur ces analyses.

**[S-04]** — OASIS — *STIX 2.1 et TAXII 2.1*
Niveau `N` · Vérifié le 02/08/2026 · Utilisé au §36.2, annexe E.2.
*Fait retenu* : standards OASIS stables depuis 2021.


## M.1 Ce qui n'est pas sourcé, et l'est assumé

Les éléments suivants relèvent d'une **doctrine proposée par ce cours**, non d'une exigence externe. Ils sont à adapter et à faire approuver :

| Élément | Où |
|---|---|
| L'échelle de probabilité en sept expressions et ses fourchettes | §9.3 |
| L'échelle de confiance en trois niveaux | §9.4 |
| Les quatre conditions d'une alerte justifiée | §27.1 |
| Le repère de 2 à 6 alertes par an | §27.2 |
| Les cinq tests d'évaluation d'un fournisseur | §22.3 |
| Le budget de 3 h/semaine en petite organisation | §39.1 |
| Les délais du workflow | Annexe J.3 |
| Le critère de production d'une fiche post-incident | §23.7 |
| Le modèle de maturité en six niveaux | Annexe K.4 |

⚠️ **Le principe** : mieux vaut une doctrine interne assumée qu'une valeur présentée comme une norme externe qu'elle n'est pas.


## M.2 À revérifier en priorité

| Priorité | Source | Motif |
|---|---|---|
| **1** | [S-03] | Échéance à huit semaines de la rédaction |
| **2** | [S-01] | Les référentiels évoluent structurellement, et pas seulement par ajout |
| **3** | [S-02] | Domaine en évolution rapide, forte couverture médiatique |
| 4 | [S-04] | Stable, revérification annuelle suffisante |

---
