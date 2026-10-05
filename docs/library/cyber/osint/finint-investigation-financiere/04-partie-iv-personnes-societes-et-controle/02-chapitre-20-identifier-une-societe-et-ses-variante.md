---
title: Chapitre 20 — Identifier une société et ses variantes internationales
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Maîtriser l’identification d’une **personne morale** : variantes orthographiques, sociétés de même nom dans plusieurs juridictions, sociétés homonymes, identifiants officiels permettant de stabiliser la référence.

## Le concept

L’identification d’une société repose essentiellement sur son **identifiant officiel** dans la juridiction de son siège :

- **France** : SIREN (9 chiffres) ou SIRET (14 chiffres = SIREN + identifiant établissement).
- **UE** : EUID (European Unique Identifier) émergent ; chaque pays a son identifiant national (Numéro KvK aux Pays-Bas, Numéro d’entreprise belge, etc.).
- **UK** : Company Number (8 caractères : 2 lettres + 6 chiffres pour Scottish, sinon 8 chiffres).
- **US** : EIN (Employer Identification Number) au niveau fédéral, mais pas universel. Plus utile : numéro d’enregistrement de l’État (Delaware, etc.).
- **LEI** (Legal Entity Identifier) : code ISO 17442 à 20 caractères, attribué aux entités opérant sur les marchés financiers. Base mondiale [GLEIF](https://www.gleif.org/). Particulièrement utile pour les institutions financières et les contreparties cotées.
- **DUNS Number** : identifiant Dun & Bradstreet, utilisé largement dans la commande publique et l’évaluation de risque.
- **VAT Number** : numéro de TVA intracommunautaire (UE), vérifiable via VIES.

L’identifiant officiel est **clé** : il lève l’ambiguïté entre sociétés de même nom dans plusieurs juridictions.

## Les pièges classiques

**Sociétés homonymes inter-juridictions** : « NEXUS TRADING » peut exister en France, en UK, à Chypre et à Dubaï — entités juridiques distinctes, parfois liées, parfois non. Toujours préciser la juridiction et l’identifiant.

**Variantes orthographiques** : « NEXUS TRADING SAS » vs « Nexus Trading » vs « N. Trading SAS » — le registre officiel a une dénomination exacte qui prévaut.

**Sociétés rebaptisées** : une société peut changer de dénomination plusieurs fois. L’identifiant SIREN/Company Number reste, mais la recherche par nom historique peut manquer la cible.

**Sociétés fusionnées / absorbées** : une société absorbée disparaît juridiquement ; son identifiant aussi. Continuité économique parfois trompeuse.

**Groupes vs filiales** : « TOTAL » peut désigner TotalEnergies SE, TotalEnergies Marketing France SAS, TotalEnergies E&P, etc. Préciser l’entité concernée.

**Marques vs sociétés** : une marque commerciale (« Apple ») peut correspondre à plusieurs sociétés juridiques (Apple Inc., Apple Operations International, Apple Sales International, etc.).

## Méthode — protocole d’identification

1. **Recueillir tous les attributs** : dénomination, juridiction (pays + ville si possible), secteur d’activité, dirigeants connus, adresse.
1. **Recherche dans le registre national** (chapitres 11-12).
1. **Vérifier l’identifiant officiel** : SIREN / Company Number / autre.
1. **Vérifier l’historique** : changements de dénomination, fusions, transferts de siège.
1. **Identifier les entités liées** : filiales, sociétés sœurs, holding mère.
1. **Documenter** : fiche identification précise (annexe D).

## Mini-walkthrough

Cible : « NEXUS HOLDINGS », mentionnée dans une DS comme contrepartie d’un flux de 1,2 M€ provenant de Chypre.

- Recherche initiale : Pappers, Companies House, OpenCorporates → 14 résultats sociétés contenant « Nexus » dans le nom, dans 9 juridictions.
- Affinage avec le contexte (Chypre + 2019 + dirigeant connu) : 2 candidats.
    - NEXUS HOLDINGS LTD (Chypre, registered 2019, directeur M. Y) → match probable.
    - NEXUS HOLDINGS LIMITED (BVI, registered 2010, directeurs trustees professionnels) → exclu (différents directeurs et antériorité).
- Identifiant officiel : Cyprus Company Registration Number HE-XXXXXX.
- Historique : pas de changement de dénomination depuis création.
- Entités liées : la société est associée majoritaire d’une SAS française et d’une LLC US — graphe à étendre.

## Erreurs fréquentes

- **Confondre des sociétés de même nom dans des juridictions différentes** — c’est l’erreur n°1 dans les enquêtes multi-juridictionnelles.
- **Oublier de tester les translittérations** — « Sergei » vs « Sergey », « Loutchnikov » vs « Luchnikov ».
- **Confondre groupe et filiale** — un dossier sur « TOTAL » sans préciser l’entité juridique est ininterprétable.
- **Confondre dénomination commerciale et dénomination sociale** — la marque ne suffit pas.

## Limites

Dans les juridictions opaques (BVI, Cayman, Panama, etc.), les recherches par nom peuvent ne pas être publiques. L’analyste s’appuie alors sur leaks (chapitre 18), agrégateurs et coopération internationale.

## Lien avec le fil rouge

> **CLEARFLOW — Stabiliser les 14 entités**
> 
> Sur les 14 sociétés du réseau Haddad mentionnées dans les DS, Nassim stabilise chaque identification par juridiction et identifiant officiel. Une particularité émerge : 3 sociétés portent un nom proche (« Nexus Trading », « Nexus Holdings », « Nexus International ») mais sont dans 3 juridictions différentes (France, Chypre, Émirats). L’analyse confirme qu’elles sont liées (sociétés affiliées contrôlées par le même réseau), mais ce sont des entités juridiques distinctes — distinction à maintenir dans tout livrable pour éviter les amalgames.

## Points clés à retenir

- L’identifiant officiel (SIREN, Company Number, LEI) prime sur le nom.
- Tester systématiquement les variantes orthographiques et les translittérations.
- Distinguer sociétés homonymes, groupes, filiales et marques.
- Documenter l’historique (changements de dénomination, fusions).

-----
