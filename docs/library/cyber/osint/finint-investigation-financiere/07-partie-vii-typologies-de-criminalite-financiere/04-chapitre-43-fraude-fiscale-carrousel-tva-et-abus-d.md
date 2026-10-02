---
title: Chapitre 43 — Fraude fiscale, carrousel TVA et abus de biens sociaux
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre les **principales typologies de fraude fiscale** : fraude TVA (notamment carrousel), évasion fiscale internationale, et l’**abus de biens sociaux** (ABS).

## Le concept

**Fraude fiscale** : ensemble des comportements visant à éluder l’impôt par dissimulation, fausses déclarations, montages fictifs.

**Carrousel TVA** (intracommunautaire). Exploite l’exonération de TVA sur les livraisons intracommunautaires pour générer des crédits de TVA fictifs ou pour ne pas reverser la TVA collectée. Acteurs typiques :

- **Société de défaut** (« missing trader » ou « buffer ») : collecte la TVA des clients mais disparaît avant de la reverser.
- **Société écran intermédiaire** : crée la chaîne d’opérations.
- **Société de récupération** : récupère la TVA déductible.
- **Société de revente** : termine la chaîne.

Le carrousel fait tourner les opérations entre les mêmes acteurs sur de multiples cycles.

**Évasion fiscale internationale** : planification fiscale agressive franchissant la ligne du légal :

- Treaty shopping (utilisation de conventions fiscales hors objet initial).
- Transfert de bénéfices vers juridictions à faible imposition via prix de transfert non conformes.
- Domiciliation fictive dans une juridiction à faible imposition.
- Structures hybrides (mismatch entre qualifications fiscales nationales).
- Trusts et fondations utilisés à des fins de dissimulation fiscale.

**Abus de biens sociaux (ABS)**. Délit français consistant pour le dirigeant à utiliser les biens de la société à des fins personnelles ou pour favoriser une autre société. Mécanismes : prélèvements personnels masqués, factures personnelles payées par la société, voyages perso facturés, biens immobiliers à usage privé.

## L’utilité opérationnelle

L’analyste cherche à :

- **Détecter le pattern** dans les flux (cycles, fragmentation, contreparties croisées).
- **Identifier les rôles** dans le schéma (buffer, intermédiaire, récupérateur).
- **Documenter les flux** entre la société et le dirigeant ou ses proches (ABS).
- **Quantifier le préjudice** (fiscal pour la fraude TVA, social pour l’ABS).

## Méthode — signaux carrousel TVA

- Cycles d’opérations entre les mêmes acteurs.
- Sociétés sans substance économique faisant transit de marchandise.
- Crédits de TVA disproportionnés avec activité réelle.
- Sociétés disparaissant brutalement (radiation, dissolution rapide).
- Secteurs à risque historiquement : téléphonie, électronique grand public, métaux, parfums et cosmétiques, droits d’émission CO₂, énergie renouvelable, services digitaux.

## Méthode — signaux d’évasion fiscale

- Charges de « conseil », « royalties », « management fees » à des entités liées en juridictions à faible imposition, disproportionnées.
- Prêts intragroupe sans intérêts ou à conditions anormales.
- Holding intermédiaire sans substance économique.
- Acquisitions de PI (marques, brevets) cédées à une entité offshore et reconcédées sous redevances.

## Méthode — signaux d’ABS

- Virements de la société vers comptes personnels du dirigeant sans contrepartie évidente.
- Factures de fournisseurs personnels acquittées par la société.
- Biens (véhicules, immobilier) de la société à usage manifestement privé.
- Comptes courants associés gonflés (le dirigeant a « prêté » à la société mais la société est dépendante).

## Mini-walkthrough — schéma fraude TVA simplifié

Trois sociétés A, B, C en cycle. A vend en intracommunautaire à B (exonéré TVA). B vend à C en national (TVA 20 % collectée). B disparaît avec la TVA. C revend à un client A (l’opération revient dans le pays d’origine). Crédit TVA de C illégitime ; perte fiscale = TVA non reversée par B.

Lecture FININT : pattern carrousel TVA classique. Vérification : registres (durée de vie des sociétés), comptes (TVA déclarée vs collectée), flux (cycles), liens entre A/B/C (mêmes UBO ou dirigeants partagés).

## Erreurs fréquentes

- **Confondre optimisation fiscale légale et fraude fiscale.** La frontière est juridique et factuelle.
- **Sous-estimer l’ampleur du carrousel TVA** : c’est l’une des fraudes fiscales les plus massives en UE.
- **Confondre ABS et choix de gestion contestable** : tous les choix discutables d’un dirigeant ne sont pas ABS.

## Limites

La qualification juridique de fraude fiscale et d’ABS appartient au judiciaire et à l’administration fiscale. Le FININT alimente. La coopération avec les services fiscaux nationaux (DGFiP en France) est centrale.

## Lien avec le fil rouge

> **CLEARFLOW — Évasion fiscale et ABS**
> 
> Dans le réseau Haddad, l’évasion fiscale via charges de conseil intragroupe à Chypre est *probable*. L’ABS via prélèvements personnels disproportionnés depuis les comptes des SAS françaises est *probable* à *quasi-certain* (signal récurrent dans les relevés). Pas de signal clair de carrousel TVA. La note finale recommande coopération avec la DGFiP pour qualifier les volets fiscaux.

## Points clés à retenir

- Trois familles : fraude TVA (carrousel), évasion fiscale internationale, ABS.
- Détection : flux, cycles, contreparties, substance économique.
- Coopération DGFiP / autorités fiscales étrangères centrale.
- Qualification juridique : pas du ressort du FININT seul.

-----
