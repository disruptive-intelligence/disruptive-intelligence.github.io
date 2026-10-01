---
title: Chapitre 37 — Détecter anomalies comptables et signaux faibles
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse de flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Connaître les **anomalies comptables typiques** et les **signaux faibles** qui orientent vers une enquête approfondie : ventes fictives, charges fictives, prêts intragroupe sans contrepartie, ajustements de fin d’exercice douteux.

## Le concept

Une anomalie comptable est un poste, un mouvement ou une présentation qui s’écarte de ce qu’on attendrait pour une entreprise du secteur et de la taille concernée. Elle peut être :

- **Innocente** : choix méthodologique légitime, particularité sectorielle.
- **Suspecte** : indice d’un schéma à investiguer.
- **Frauduleuse** : preuve, après recoupement, d’une falsification.

L’analyste FININT cherche d’abord à identifier la suspicion, pas à conclure à la fraude.

## Familles d’anomalies courantes

**Côté revenus** :

- **Ventes fictives** : factures sans contrepartie réelle (marchandise, prestation). Détectables par : créances clients qui ne se règlent pas, croissance disproportionnée du CA, ventes à des clients sans existence vérifiable, marges anormalement élevées.
- **Cut-off** : décalage de la reconnaissance du revenu pour gonfler l’exercice (revenu reconnu en année N alors qu’il aurait dû l’être en N+1, ou inversement).
- **Vente fictive de stocks** entre entités liées pour gonfler les ventes.
- **Subventions non rapportées au bon exercice**.

**Côté charges** :

- **Charges fictives** : factures payées à des fournisseurs fictifs ou à des sociétés liées sans contrepartie réelle. Vecteur classique d’abus de biens sociaux (ABS — chapitre 43).
- **Charges de conseil** disproportionnées à des entités liées (signal d’évasion de bénéfices).
- **Voyages et frais de représentation** disproportionnés à l’activité.
- **Sous-traitance massive** sans personnel ni équipement chez le sous-traitant (chaîne fictive).

**Côté bilan** :

- **Créances clients gonflées** : créances qui restent en bilan sans recouvrement (cachent une absence de revenu réel).
- **Stocks invraisemblables** : volumes ou valeurs sans rapport avec l’activité.
- **Provisions douteuses** : sur-provisionnement ou sous-provisionnement pour modeler le résultat.
- **Prêts intragroupe** : si faits sans intérêts, sans documentation, sans remboursement, signal de transfert occulte de valeur.
- **Compte courant d’associé** anormalement gros (le dirigeant a prêté ou retiré beaucoup).

**Présentation et publication** :

- **Comptes publiés en retard récurrent**.
- **Confidentialité demandée alors que la société dépasse les seuils**.
- **Changement de cabinet de CAC** sans justification claire.
- **Réserves dans le rapport du CAC**.

## L’utilité opérationnelle

Détecter les anomalies oriente :

- La typologie probable du schéma (ABS, fraude fiscale, évasion, blanchiment).
- Les pièces à demander en réquisition (factures sous-jacentes, contrats, ordres de virement).
- Les acteurs à profiler (commissaire aux comptes, expert-comptable, dirigeants).

## Méthode — protocole de détection

1. **Comparer les ratios** sectoriels et historiques.
1. **Examiner les postes principaux** ligne par ligne pour les postes représentant > 5 % du total.
1. **Lire systématiquement l’annexe**.
1. **Identifier les conventions réglementées** (transactions avec parties liées).
1. **Confronter avec les flux observables** (relevés bancaires).
1. **Documenter les signaux** dans la fiche société (chapitre 28).

## Mini-walkthrough — anomalies NEXUS TRADING

- Charges de conseil à NEXUS HOLDINGS LTD CY = 140 K€ sur l’exercice. Disproportionné pour une SAS de 12,4 M€ de CA avec un seul dirigeant. Convention réglementée à l’origine ? Service réel rendu ? *Probable* signal de transfert de bénéfices vers la juridiction chypriote.
- Créances clients = 280 K€, soit ~30 jours de CA. Niveau normal pour le négoce. Pas d’anomalie ici.
- Compte courant associé NEXUS HOLDINGS CY = 52 K€. Faible niveau, pas alarmant.
- Stocks = 0 €. Cohérent avec intermédiation pure.

Signal principal : **les charges de conseil**. *Probable* mécanisme d’évasion de bénéfices vers la holding chypriote, à investiguer (substance des prestations, contrats sous-jacents).

## Erreurs fréquentes

- **Considérer une anomalie comme une preuve.** L’anomalie est un signal d’investigation, pas une preuve.
- **Ignorer la perspective sectorielle.** Certaines anomalies apparentes sont des pratiques sectorielles courantes.
- **Ne pas chercher l’explication légitime** avant de conclure à la fraude.

## Limites

Le détecteur d’anomalies suppose une connaissance sectorielle ; sans elle, l’analyste risque d’attribuer une anomalie là où il n’y en a pas, ou inversement.

## Lien avec le fil rouge

> **CLEARFLOW — Signaux comptables consolidés**
> 
> Sur l’ensemble du réseau Haddad, Nassim recense 8 anomalies comptables convergentes : charges de conseil intragroupe disproportionnées (3 SAS), prêts intragroupe sans intérêts (5 entités), créances clients structurellement non recouvrées (1 SAS), absence systématique de stocks pour entités déclarées en négoce (4 SAS). Cumulés, ces signaux constituent un faisceau convergent de *probable* schéma d’évasion de bénéfices et de transferts intragroupe non justifiés économiquement.

## Points clés à retenir

- Anomalies = signaux d’investigation, jamais preuves seules.
- Familles : ventes fictives, charges fictives, postes de bilan douteux, présentation.
- Comparaison sectorielle + cohérence avec flux = clés.
- Conventions réglementées et annexe sont des mines d’information.

-----
