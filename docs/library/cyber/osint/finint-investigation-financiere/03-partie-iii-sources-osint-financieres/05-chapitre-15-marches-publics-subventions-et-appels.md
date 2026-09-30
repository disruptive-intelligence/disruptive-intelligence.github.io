---
title: Chapitre 15 — Marchés publics, subventions et appels d’offres
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Connaître les **bases publiques de marchés publics, subventions et appels d’offres** comme source d’enquête, notamment pour les schémas de corruption (chapitre 42), de favoritisme et d’attribution douteuse.

## Le concept

Les **marchés publics** (commande publique) sont, dans de nombreuses juridictions, soumis à des obligations de **publication** : annonces préalables, attributions, contrats. Ces données ouvertes sont une mine d’information pour l’analyste FININT enquêtant sur la corruption ou les schémas adressés à l’État ou à des collectivités.

## Méthode — bases utiles par pays

**France** :

- **BOAMP** (Bulletin officiel des annonces de marchés publics) — publications obligatoires des marchés au-delà des seuils. Accès en ligne, gratuit.
- **JOUE / TED (Tenders Electronic Daily)** — équivalent UE.
- **data.gouv.fr** : datasets ouverts sur la commande publique (DECP — Données essentielles de la commande publique).
- **HATVP** (Haute Autorité pour la transparence de la vie publique) — déclarations de patrimoine et d’intérêts des responsables publics. Accès en ligne, partiellement public. **Périmètre à connaître** : toutes les fonctions publiques ne sont pas couvertes de la même manière. Le périmètre des assujettis HATVP est défini par fonctions et seuils (parlementaires, membres du gouvernement, élus locaux à partir de certains seuils, dirigeants d’organismes publics, etc.). Un élu local d’une petite commune n’est pas nécessairement couvert ; un parlementaire l’est. Vérifier la liste à jour des assujettis sur le site de la HATVP.
- **AIFE — Chorus Pro** (factures de l’État).

**UE** :

- **TED (Tenders Electronic Daily)** — toutes les annonces UE au-delà des seuils.
- **eForms** — format unifié à partir de 2024.
- **EU Funding & Tenders Portal** pour les financements européens (Horizon, FEDER, FSE, etc.).

**UK** :

- **Contracts Finder**, **Find a Tender Service**.

**US** :

- **SAM.gov** (System for Award Management) — base fédérale.
- **USAspending.gov** — dépenses fédérales.
- **State and local procurement portals**.

**Subventions** :

- France : data.gouv.fr (subventions associatives, aides aux entreprises).
- UE : Cohesion Open Data Platform.

## L’utilité opérationnelle

L’analyste cherche à identifier :

- **Marchés attribués à des sociétés du réseau** sous enquête (lien direct avec le secteur public).
- **Schémas d’attribution suspects** : faible nombre de soumissionnaires, dérogations à appel d’offres, marchés découpés sous les seuils, marchés négociés sans publicité.
- **Liens entre attributaires et décideurs** (HATVP en France pour les conflits d’intérêts).
- **Sous-traitants en cascade** dont une partie peut être des sociétés écrans.

## Mini-walkthrough

Une SARL de BTP en région française, dans un dossier de soupçon de corruption locale.

- BOAMP : la SARL a remporté 7 marchés sur 3 ans, dans 3 communes, pour un montant cumulé de 4,2 M€.
- DECP : on identifie les acheteurs publics (3 communes), les types de marchés (voirie, bâtiments scolaires).
- HATVP : le maire de la commune principale a déclaré un intérêt (ami / parent travaillant dans une société liée).
- Recoupement : on cherche dans les conseils municipaux, presse locale, des éléments confirmant ou infirmant.

Conclusion : signal de **conflit d’intérêts probable** à approfondir. Pas de qualification de corruption à ce stade — exige des éléments d’intentionnalité et de contrepartie.

## Erreurs fréquentes

- **Lire un marché public comme une preuve.** Beaucoup de marchés sont gagnés légitimement par des entreprises locales — la concentration n’est pas la preuve.
- **Ignorer les seuils.** Les marchés sous certains seuils ne sont pas publiés — l’analyse est partielle.
- **Sous-utiliser HATVP** en France — c’est une source précieuse pour les liens entre décideurs et entreprises.

## Limites

Les bases publiques ne couvrent pas tous les marchés (seuils). Elles ne disent rien des **marchés privés** (B2B), qui peuvent aussi être l’objet de corruption. La corruption se prouve par d’autres moyens (preuves d’intention, paiements traçables, témoignages).

## Lien avec le fil rouge

> **CLEARFLOW — Marché ivoirien**
> 
> Une des sociétés du réseau Haddad, NEXUS NEGOCE (Côte d’Ivoire), a remporté un marché public ivoirien de fourniture de matériel agricole en 2023 pour 3,2 M€. Source : presse économique régionale + rapport de la Chambre des comptes ivoirienne. Profil du marché : faible nombre de soumissionnaires, attributaire créé moins d’un an avant l’attribution, lien possible avec un haut fonctionnaire ivoirien (presse). Le volet ivoirien sera renvoyé en coopération internationale (Egmont avec la CRF ivoirienne) — impossible à approfondir depuis la France sans ce levier.

## Points clés à retenir

- BOAMP, TED, SAM.gov, Contracts Finder : bases ouvertes principales.
- HATVP : essentielle pour les liens décideurs / entreprises en France.
- Marchés publics ne prouvent pas la corruption : ils alimentent l’hypothèse.
- Les marchés privés et les marchés sous seuils sont des angles morts.

-----
