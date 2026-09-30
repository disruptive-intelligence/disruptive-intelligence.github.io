---
title: Chapitre 35 — Reconstituer des flux financiers
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse DE flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Passer de la lecture d’un compte isolé à la **reconstitution d’un schéma multi-comptes** — suivre l’argent à travers plusieurs banques, plusieurs juridictions, plusieurs entités, pour comprendre l’organisation d’ensemble.

## Le concept

La reconstitution de flux consiste à **enchaîner les opérations** pour montrer le parcours de la valeur. Elle peut se faire dans deux directions :

- **Forward tracing** : partant d’une opération initiale, suivre où va l’argent.
- **Backward tracing** : partant d’une opération finale, remonter à l’origine.

Idéalement, les deux sont combinées pour valider mutuellement les chaînes.

## L’utilité opérationnelle

Reconstituer les flux permet :

- Identifier l’**origine probable** des fonds (infraction prédécesseur en blanchiment).
- Identifier la **destination finale** (UBO bénéficiaire, intégration dans l’économie légale).
- Identifier les **points de passage critiques** (banques, juridictions, sociétés).
- Identifier les **techniques de layering** (fractionnement, complexification, conversion).
- Quantifier le volume total et le ventiler.

## Méthode — workflow

1. **Identifier les comptes accessibles** : DS, réquisitions, EAR/CRS pour les comptes étrangers (en CRF).
1. **Construire un tableau de flux** : pour chaque opération, donneur, bénéficiaire, montant, devise, date, libellé, rail.
1. **Identifier les liens entre opérations** : opération A débite le compte 1 vers le compte 2, opération B (1-3 jours après) débite le compte 2 vers le compte 3, etc.
1. **Constituer des séquences** : chaîne d’opérations chronologiquement et économiquement liées.
1. **Construire le graphe de flux** : nœuds = comptes (ou entités), arcs = flux pondérés par montant.
1. **Calculer les agrégats** : total entré, total sorti, perte en route (différence = frais ou paiements masqués).

## Walkthrough — séquence de transit

```
Schéma observé (sur 14 mois)

Société Y (Émirats) ──[3,8 M€ via 18 SWIFT MT103]──> SAS A (France)
SAS A (France) ──[3,2 M€ via 24 SCT vers]──> Sociétés liées du groupe
SAS A (France) ──[420 K€ via SCT Inst]──> Comptes personnels (M. X et liés)
SAS A (France) ──[300 K€ via 5 SWIFT MT103]──> Banque privée Suisse (compte K. Haddad présumé)

Détail temporel : entrées concentrées en début de mois, sorties dans les 7 jours.
```


Lecture FININT : le profil est compatible avec un **schéma de transit avec rétention de marge minimale** et **dilution dans le réseau** + **prélèvements personnels**. Le solde net de la SAS reste faible (~100 K€), cohérent avec un compte de passage.

Hypothèses : TBML (probable), corruption avec rétrocommissions (possible), simple optimisation fiscale agressive (peu probable seul à expliquer le schéma).

## Erreurs fréquentes

- **Ne suivre qu’un sens.** Toujours combiner forward et backward.
- **Ignorer les frais bancaires** : ils peuvent expliquer une partie de la perte en route.
- **Confondre transit et accumulation** : un compte peut être les deux selon les périodes.
- **Sur-attribuer une intention.** Un schéma de transit peut être légitime (intermédiation commerciale réelle).

## Limites

La reconstitution exige l’accès aux relevés détaillés de **chaque compte** dans la chaîne. Sans coopération internationale, des maillons restent inaccessibles, donc des hypothèses non confirmées.

## Lien avec le fil rouge

> **CLEARFLOW — Reconstitution globale**
> 
> Nassim, après 5 semaines, produit une cartographie des flux du dossier Haddad : sur 18 mois, ~22 M€ entrants dans le réseau (origine multi-juridictionnelle), ~16 M€ sortants vers l’étranger, ~6 M€ stationnés ou consommés (dépenses, immobilier, autres). Sur les 22 M€ entrants, l’origine reste partiellement floue : ~12 M€ proviennent de sociétés du même groupe (transit interne sans origine externe identifiée pour cette portion), ~10 M€ proviennent de tiers commerciaux dont la réalité économique reste à confirmer (TBML probable). C’est cette analyse qui structure la note finale.

## Points clés à retenir

- Forward + backward tracing combinés.
- Tableau de flux structuré, graphe de flux pondéré.
- Quantifier les totaux et les pertes en route.
- Identifier les techniques de layering.

-----
