---
title: 'Chapitre 40 — Blanchiment : placement, empilement, intégration'
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies DE criminalité financière
  - index.md
---

## Objectif du chapitre

Maîtriser le **cadre conceptuel** du blanchiment de capitaux : trois phases (placement, empilement, intégration), typologies courantes, signaux de détection. C’est la matrice de référence pour la majorité des dossiers FININT.

## Le concept

Le **blanchiment de capitaux** est l’opération par laquelle une personne dissimule l’origine illicite de fonds pour les introduire dans l’économie légale.

Le modèle classique en **trois phases** (popularisé par le GAFI dans les années 1990, encore utile pédagogiquement même s’il simplifie la réalité) :

**1. Placement.** Introduire les fonds illicites dans le système financier. Mécanismes : dépôts en espèces (souvent fractionnés sous les seuils — *structuration* ou *smurfing*), achats en cash de biens revendables, conversions en cryptos, infiltration dans des activités à forte composante cash (restauration, hôtellerie, salons de coiffure, lavages auto, bars-tabacs). C’est la phase la plus risquée pour le blanchisseur car la plus visible.

**2. Empilement (layering).** Multiplier les opérations et les juridictions pour brouiller la traçabilité. Mécanismes : virements multiples entre sociétés écrans, conversions de devises, allers-retours bancaires, fragmentation par plusieurs PSP, layering crypto via mixers ou bridges, transit par des juridictions à secret bancaire. Le but : créer une distance entre l’origine et la destination.

**3. Intégration.** Réinjecter les fonds blanchis dans l’économie légale sous une forme apparemment légitime : achat immobilier, acquisition d’entreprises, investissements dans des actifs financiers, achats de luxe.

## Évolution moderne du modèle

Le modèle trois phases simplifie la réalité 2020+. Les schémas modernes :

- **Combinent rapidement** placement et layering (BEC + fintechs + crypto en quelques heures).
- **Intègrent la crypto** comme rail de placement et de layering (renvoi OSINT Crypto).
- **S’appuient sur des structures juridiques** (sociétés écrans, trusts) plus que sur les espèces.
- **Exploitent les jeux d’argent en ligne** comme couche.
- **Utilisent les marchés de l’art, des NFT, des cartes de collection** comme moyens d’intégration.

## L’utilité opérationnelle

L’analyste cherche à :

- **Identifier la phase** dans laquelle se situe une opération observée.
- **Reconstituer la chaîne** : retrouver le placement initial à partir des indices de layering ou d’intégration.
- **Qualifier l’infraction prédécesseur** (qu’est-ce qui a généré les fonds : trafic, fraude, corruption ?).

## Méthode — signaux par phase

**Placement** : dépôts d’espèces fréquents et fractionnés, activité incohérente avec le compte, achats en cash de biens revendables, onboarding rapide sur PSP/EME avec activité immédiate inhabituelle.

**Layering** : cascades de virements en cycle court, multiplication des juridictions sans rationale, conversions multiples de devises, transferts en cascade entre fintechs, sorties crypto avec mixers ou bridges.

**Intégration** : acquisitions immobilières disproportionnées, investissements dans des sociétés sans expérience préalable, acquisitions d’œuvres d’art à prix élevés, importations de biens de luxe, donations à des organismes avec retours indirects.

## Mini-walkthrough — schéma observable

Un trafiquant accumule 1 M€ en espèces. **Placement** : dépôts par 10-50 mules de 5-9 K€ chacun en plusieurs agences. **Layering** : virements vers une SAS écran, puis société émirate, conversion USDT, transferts entre exchanges, reconversion en EUR sur fintech. **Intégration** : achat d’un appartement à Paris via SCI.

L’analyste qui intervient à un point quelconque doit reconstituer en amont et en aval pour identifier infraction prédécesseur et bénéficiaire final.

## Erreurs fréquentes

- **Considérer toute opération inhabituelle comme blanchiment.** Beaucoup ont des explications légitimes.
- **Ignorer la phase d’intégration** : c’est souvent la plus visible et la plus exploitable judiciairement.
- **Sous-estimer le rôle des assujettis non bancaires** : notaires, avocats, marchands d’art, agents immobiliers, casinos.

## Limites

La qualification *« blanchiment »* est une qualification juridique qui exige une **infraction prédécesseur** établie. En FININT, on parle de **schéma compatible avec un blanchiment** et l’on transmet à l’autorité compétente.

## Lien avec le fil rouge

> **CLEARFLOW — Phases observables**
> 
> Dans le dossier Haddad, les phases sont mélangées. Le **placement** apparaît marginal (peu de cash visible). Le **layering** est central (transit multi-juridictionnel via sociétés écrans). L’**intégration** apparaît dans les acquisitions immobilières françaises et présumées étrangères. L’infraction prédécesseur n’est pas clairement établie ; les hypothèses retenues : corruption autour des marchés ouest-africains (probable), évasion fiscale et fraudes diverses (possible).

## Points clés à retenir

- Modèle GAFI : placement → layering → intégration.
- Évolution moderne : phases mélangées, accélérées, intégrant crypto.
- L’analyste identifie la phase et reconstitue en amont/aval.
- Qualification juridique de blanchiment exige l’infraction prédécesseur.

-----
