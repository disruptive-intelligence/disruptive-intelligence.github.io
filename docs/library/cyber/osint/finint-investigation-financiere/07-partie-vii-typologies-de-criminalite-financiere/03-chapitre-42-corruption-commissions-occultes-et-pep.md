---
title: Chapitre 42 — Corruption, commissions occultes et PEP
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre les **schémas de corruption** transnationale : commissions occultes, pots-de-vin, rétrocommissions, et le concept de **PEP** (Personne Politiquement Exposée).

## Le concept

La **corruption** est l’obtention d’un avantage en échange d’un acte illicite par une personne en position de pouvoir. Variantes :

- **Corruption active** (celui qui offre) et **passive** (celui qui reçoit).
- **Corruption nationale** vs **transnationale** (régie par les conventions OCDE 1997, ONU Mérida 2003, loi Sapin II 2016 en France).
- **Trafic d’influence** : intermédiaire facilitant l’obtention d’un avantage.
- **Concussion** : exigence d’une rémunération non due par un agent public.
- **Prise illégale d’intérêts** : cumul d’intérêts privés et de fonctions publiques.
- **Favoritisme** : avantage indu dans la commande publique.

**PEP — Personne Politiquement Exposée.** Catégorie LCB-FT définie par la 4e/5e directive AML. Recouvre :

- Chefs d’État et de gouvernement, ministres, parlementaires.
- Membres de cours suprêmes et cours constitutionnelles.
- Membres de la haute hiérarchie militaire.
- Dirigeants de partis politiques significatifs.
- Dirigeants d’entreprises publiques significatives.
- Dirigeants d’organisations internationales.
- **Membres de la famille proche** (conjoint, parents, enfants, beaux-parents).
- **Collaborateurs étroits connus** (associés, prête-noms).

Le statut PEP ne fait pas du PEP un criminel ; il **déclenche une vigilance renforcée** (KYC renforcé, monitoring spécifique).

## Schémas typiques

- **Rétrocommissions sur marché public** : marché remporté à prix surévalué, partie reversée au décideur ou à un proche, via structure offshore.
- **Cadeaux et invitations** : voyages, séjours, biens — formes plus subtiles.
- **Pacte de corruption** : facture de « conseil » à une société écran contrôlée par le décideur ou un proche.
- **Société de couverture** : le décideur crée une société (par prête-nom) qui « facture » des prestations fictives au fournisseur bénéficiaire.
- **Trust avec bénéficiaires politiquement exposés** : fonds parqués dans un trust dont le PEP ou ses proches sont bénéficiaires.

## L’utilité opérationnelle

L’analyste cherche à :

- **Identifier le PEP** ou son entourage (PEP famille, PEP collaborateur).
- **Repérer les flux atypiques** (entrées depuis fournisseurs publics vers comptes personnels ou de proches).
- **Documenter les liens** entre décideurs et entreprises bénéficiaires.
- **Croiser avec marchés publics** (chapitre 15) et HATVP en France.

## Méthode — signaux de corruption

- Flux entrants depuis fournisseurs de la commande publique vers comptes personnels ou de proches.
- Sociétés de « conseil » dont l’activité réelle est inidentifiable, facturant des entités publiques ou semi-publiques.
- Acquisitions patrimoniales disproportionnées par des proches.
- Train de vie incohérent avec les revenus déclarés.
- Présence du décideur dans HATVP avec déclarations partielles ou contradictoires.

## Mini-walkthrough

Un haut fonctionnaire signe régulièrement des marchés publics avec une PME. Cette PME, par convention, verse 5 % de chaque marché à une « société de conseil » domiciliée à Chypre, dont l’UBO est l’oncle du fonctionnaire.

Lecture FININT : pattern de rétrocommissions probable. Vérification : marchés publics gagnés (BOAMP, DECP), flux PME → société de conseil (réquisition), UBO de la société (registre, leaks), lien familial fonctionnaire-oncle (état civil, presse, SOCMINT). Si tous les éléments se confirment, schéma *quasi-certain*.

## Erreurs fréquentes

- **Considérer toute relation PEP / entreprise comme corruption.** Beaucoup sont parfaitement légales.
- **Surinterpréter une déclaration HATVP partielle.** Peut être omission, pas nécessairement fraude.
- **Diaboliser le statut PEP** : ce n’est pas un soupçon, c’est une exigence de vigilance.

## Limites

La corruption transnationale est notoirement difficile à prouver : témoignages réticents, juridictions étrangères, secret bancaire résiduel. Les dossiers FININT débouchent souvent sur des recommandations à des autorités spécialisées (PNF, OCDE Working Group on Bribery, Interpol).

## Lien avec le fil rouge

> **CLEARFLOW — Volet corruption ivoirien**
> 
> Sur le volet du marché public ivoirien, l’hypothèse de **favoritisme avec corruption** est *possible* à *probable*. Sans coopération ivoirienne, l’établissement précis est *indéterminable*. La note finale recommande au PNF d’engager les coopérations nécessaires.

## Points clés à retenir

- Corruption : variantes nombreuses (active, passive, trafic d’influence, favoritisme).
- PEP : statut déclencheur de vigilance, pas d’accusation.
- Schémas typiques : rétrocommissions, sociétés de couverture, trusts avec bénéficiaires PEP.
- Coopération internationale souvent indispensable.

-----
