---
title: Chapitre 13 — Identifier les bénéficiaires effectifs
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Comprendre la notion de **bénéficiaire effectif (UBO)**, savoir mobiliser les registres UBO disponibles, anticiper leurs limites, et croiser pour identifier le ou les UBO réels d’une structure. C’est un objectif central du FININT, et l’un des plus difficiles dans les juridictions opaques.

## Le concept

Le **bénéficiaire effectif** (UBO — Ultimate Beneficial Owner) d’une entité est, en droit européen :

- toute personne physique qui détient ou contrôle, directement ou indirectement, plus de **25 %** du capital ou des droits de vote ;
- ou exerce un contrôle par d’autres moyens (contrat, convention de vote, droit de nomination) ;
- ou, à défaut, occupe la fonction de dirigeant principal (UBO « de dernier recours », en France parfois appelé UBO « par défaut »).

Pour les **trusts et fondations**, l’UBO inclut : le constituant (settlor), le ou les trustee(s), le ou les protecteur(s), le ou les bénéficiaire(s) (ou catégorie de bénéficiaires), et toute autre personne contrôlant le trust.

## Les registres UBO

Depuis la 4ème puis la 5ème directive AML, l’UE a imposé aux États membres de tenir des **registres des bénéficiaires effectifs**. Organisation et accès varient.

**France — Registre des bénéficiaires effectifs (RBE)** tenu par l’INPI. Toutes les entités juridiques françaises doivent déclarer leurs UBO. Accès au RBE :

- pour les autorités compétentes : sans restriction.
- pour les assujettis (banques, etc.) : dans le cadre de leurs obligations LCB-FT.
- pour le public : a été ouvert puis restreint suite à l’**arrêt CJUE du 22 novembre 2022** qui a invalidé l’accès public généralisé au motif de protection de la vie privée. La situation actuelle (2025) : accès maintenu pour les autorités, les assujettis, et certaines catégories spécifiquement justifiées (presse d’investigation sous conditions, certains professionnels). L’accès « grand public » direct est restreint. À vérifier auprès de la dernière communication de l’INPI au moment de l’enquête.

**UK — PSC (Persons with Significant Control)**. Public et gratuit via Companies House. Resté ouvert (UK hors UE depuis Brexit, donc non concerné par l’arrêt CJUE).

**Allemagne — Transparenzregister**. Accès très restreint au public depuis l’arrêt CJUE.

**Pays-Bas — UBO-register**. Idem, restreint.

**Luxembourg — Registre des bénéficiaires effectifs (RBE)**. Restreint depuis CJUE.

**Italie, Espagne, autres EU**. Situations variables, mais tendance générale au resserrement post-CJUE.

**En pratique, l’accès varie désormais fortement** selon les États membres, les catégories d’acteurs (autorités, assujettis LCB-FT, presse, chercheurs, professionnels avec intérêt légitime) et la justification d’un **intérêt légitime** à connaître l’UBO. L’analyste vérifie systématiquement l’état du droit dans chaque juridiction concernée par le dossier au moment de l’enquête.

**Pays tiers** (BVI, Cayman, Émirats, etc.) — registres existent mais accès quasi-systématiquement réservé aux autorités locales.

**AMLA et nouveau paquet AML européen (2024-2026)** : prévoit une **interconnexion européenne** des registres UBO et un encadrement plus précis de l’accès. Mise en œuvre progressive.

## L’utilité opérationnelle

L’UBO est la **clé** d’une cartographie : sans UBO, on a une coquille juridique sans sa réalité humaine.

L’analyste cherche à :

- identifier l’UBO « déclaré » officiellement dans le registre ;
- vérifier sa **plausibilité** (cet UBO a-t-il les caractéristiques pour être réellement le contrôleur — capacité financière, expérience, lien avec l’activité ?) ;
- identifier d’éventuels signes de **prête-nom** (chapitre 25) ;
- recouper avec d’autres sources (leaks, presse, registres connexes) pour confirmer ou infirmer.

## Méthode — démarche en 4 étapes

1. **Récupérer la déclaration UBO officielle** quand accessible (RBE France pour les autorités/assujettis, PSC UK public, etc.).
1. **Vérifier la cohérence** : profil, nationalité, adresse, antécédents. Un UBO de 22 ans déclaré contrôleur d’un groupe à 50 M€ de CA est invraisemblable.
1. **Croiser** avec : autres mandats déclarés, presse, leaks, réseaux sociaux, registres connexes.
1. **Calibrer la confiance** : UBO déclaré = *possible* ; UBO confirmé par recoupement = *probable* ; UBO confirmé par documents indépendants (réquisitions, EAR) = *quasi-certain*.

## Mini-walkthrough

Cible : OMEGA HOLDINGS LTD (Chypre).

- Recherche RBE chypriote : restreint depuis CJUE.
- Companies House équivalent chypriote : directors visibles, UBO non.
- Sayari (licence) : indique un UBO possible, M. Y, basé à Beyrouth, avec un lien sur trois autres sociétés méditerranéennes.
- Recherche dans Pandora Papers (Aleph ICIJ) : OMEGA HOLDINGS apparaît, avec un settlor d’un trust chypriote. Le settlor est *distinct* de M. Y. **Hypothèse : M. Y est le directeur déclaré, mais le settlor du trust contrôle in fine** — UBO probable = settlor.
- Vérification du settlor : presse libanaise antérieure, fonctions dans des sociétés liées au commerce régional. Profil cohérent.
- Calibration : UBO probable = settlor (Karim Haddad ou personne associée), niveau de confiance *probable* sur la base du recoupement Pandora.
- Lacune : la liste exacte des bénéficiaires du trust est inaccessible — il faudrait Egmont avec Mokas ou MROS selon l’évolution.

## Erreurs fréquentes

- **Croire l’UBO déclaré sans vérification.** Beaucoup d’UBO déclarés sont des prête-noms.
- **Conclure à un prête-nom sans preuve.** Inversement, ce n’est pas parce que l’UBO déclaré paraît modeste qu’il est nécessairement un prête-nom.
- **Ignorer le contrôle indirect.** Un UBO peut contrôler par convention, par usufruit, par contrat de gestion — pas seulement par % de capital.
- **Mélanger l’UBO d’une société et l’UBO d’un compte bancaire.** Ce ne sont pas toujours les mêmes (un compte peut être au nom d’une personne mandataire de la société, ou d’un fiduciaire).

## Limites

L’identification de l’UBO réel d’une structure complexe **multi-juridictionnelle** opaque exige souvent : des leaks, des coopérations internationales, des réquisitions auprès de banques, et parfois reste **indéterminable** par le seul OSINT.

## Lien avec le fil rouge

> **CLEARFLOW — Identification UBO progressive**
> 
> Pour les 4 SAS françaises : UBO déclarés au RBE = personnes physiques résidant en France. Pour 2 d’entre elles, l’UBO déclaré est un retraité français de 78 ans avec un patrimoine modeste — **alarme prête-nom probable**. Pour les Limited UK : PSC = M. Y (libanais, basé à Dubaï). Pour OMEGA Chypre : UBO déclaré = trustee professionnel (couverture). Pour la LLC Delaware : aucun UBO accessible (depuis l’interim final rule FinCEN de mars 2025, les LLC domestiques US sont exemptées de déclaration BOI à FinCEN). Conclusion : *probable* que Karim Haddad est l’UBO réel d’une partie significative du réseau, sous prête-noms et trustees, mais l’identification *quasi-certaine* exigerait coopération internationale et réquisitions.

## Points clés à retenir

- UBO = personne physique qui détient/contrôle ultimement, seuils 25 % en UE (capital ou droits de vote).
- Registres UBO : accès restreint en UE depuis CJUE 2022. UK PSC reste public.
- Croiser systématiquement déclaration / cohérence / recoupements / leaks.
- L’UBO réel d’une structure complexe peut être *indéterminable* sans coopération.

-----
