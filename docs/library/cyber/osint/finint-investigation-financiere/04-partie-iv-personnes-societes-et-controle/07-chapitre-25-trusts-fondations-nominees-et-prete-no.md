---
title: Chapitre 25 — Trusts, fondations, nominees et prête-noms
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Maîtriser les **structures de détention indirecte** : trusts, fondations privées, nominees, prête-noms — leurs mécanismes, leurs usages légitimes, leur exploitation dans l’opacification, et leur lecture en enquête FININT.

## Le concept

**Trust** (common law). Une relation juridique tripartite :

- **Settlor** (constituant) : la personne qui apporte les actifs au trust.
- **Trustee** : la personne (physique ou morale, souvent un trust company) qui détient et gère légalement les actifs au profit des bénéficiaires.
- **Bénéficiaires** : personnes (nommées ou non) qui jouissent des actifs (revenus ou capital, selon les termes).
- **Protecteur** (parfois) : tiers chargé de surveiller le trustee et/ou de modifier le trust.

**Types de trusts** :

- **Trust révocable** : le settlor peut révoquer et récupérer les actifs. Faible opacification ; les actifs restent attribuables.
- **Trust irrévocable** : le settlor ne peut plus récupérer. Opacification renforcée ; mais le settlor est généralement listé.
- **Trust discrétionnaire** : le trustee a un pouvoir discrétionnaire sur la distribution. Souvent utilisé pour des montages opaques (qui sont les bénéficiaires effectifs ? le trustee décide).
- **Trust avec lettre de souhait** : le settlor laisse une « letter of wishes » non contraignante au trustee — outil d’opacification fréquent.

**Juridictions de trust** : UK, US, BVI, Cayman, Bahamas, Jersey, Guernsey, Île de Man, Singapour, Hong Kong, Suisse (admis depuis 2007 sous certaines conditions), New Zealand.

**Fondation privée** (droit continental). Entité juridique distincte. Mécanisme similaire au trust mais juridiquement différent :

- **Fondateur** : apporte les actifs.
- **Conseil de fondation** : gère.
- **Bénéficiaires** : reçoivent.

**Juridictions de fondations privées** : Liechtenstein (Stiftung), Panama, Pays-Bas (Stichting), Autriche, Suisse, certaines juridictions caribéennes.

**Nominee**. Prête-nom **officiel**, déclaré comme tel. Mécanisme courant en common law (nominee director, nominee shareholder). Le nominee détient au nom d’un bénéficiaire qu’il représente. La relation est formalisée par un contrat (declaration of trust, nominee agreement).

**Prête-nom (en droit continental)**. Personne qui apparaît officiellement comme dirigeant ou associé sans l’être réellement. À la différence du nominee, la relation est **dissimulée** dans la plupart des juridictions de droit continental. En France, le prête-nom est illicite quand il vise à frauder.

## L’utilité opérationnelle

L’analyste doit savoir :

- **Identifier la présence** d’une telle structure dans une chaîne de contrôle (chapitre 23).
- **Comprendre les rôles** : qui est settlor / fondateur / trustee / bénéficiaire.
- **Identifier les UBO réels** : selon les directives AML, ce sont (pour les trusts) le settlor, les trustees, les protecteurs, les bénéficiaires identifiés ou la classe, et toute personne contrôlant.
- **Détecter les prête-noms** : signaux d’incohérence entre profil et fonction.

## Méthode — analyser une structure de détention indirecte

1. **Récupérer les actes** quand accessibles (trust deed, statuts de fondation) — souvent indisponibles en sources ouvertes, possibles en leaks (Pandora particulièrement riche).
1. **Identifier les acteurs déclarés** : settlor, trustee, bénéficiaires, protecteurs.
1. **Profiler chacun** : le trustee est-il un cabinet professionnel ? Quels autres trusts gère-t-il ? Le settlor est-il visible publiquement ?
1. **Croiser avec leaks et presse** : Pandora et Paradise Papers contiennent souvent les éléments de trusts non publics.
1. **Identifier les bénéficiaires** : nommés ou catégorie ? Si « famille X », identifier les membres.
1. **Calibrer** : qui contrôle réellement ? Réversibilité ? Liens visibles entre settlor et bénéficiaires ?

**Détecter un prête-nom (signaux probabilistes)** :

- **Profil incohérent** : retraité de 80 ans dirigeant 7 SAS de négoce.
- **Absence d’expérience visible** dans le secteur.
- **Réseau personnel pauvre** sur LinkedIn et réseaux sociaux par rapport aux mandats officiels.
- **Domiciliation à l’adresse de la société** ou d’un cabinet de domiciliation.
- **Multi-mandats** dans des secteurs sans cohérence.
- **Rotation rapide** des mandats (entrées et sorties multiples).
- **Lien capillaire avec un autre acteur** identifié comme contrôleur réel possible.

Aucun de ces signaux ne suffit. **Plusieurs convergents** justifient le qualificatif *probable* prête-nom — jamais *quasi-certain* sans éléments documentaires (témoignages, actes contestés, aveux).

## Mini-walkthrough — OMEGA HOLDINGS TRUST

- Identification dans Pandora Papers (chapitre 18) : trust chypriote constitué en 2019.
- **Settlor** : Karim Élie Haddad, identifié.
- **Trustee** : Cabinet Pancyprian Trustees Ltd (Chypre) — cabinet professionnel, identifié comme administrateur de plusieurs centaines de trusts dans Pandora.
- **Bénéficiaires** : « the family of the settlor » — formulation vague, à étendre.
- **Protecteur** : non identifié dans les documents disponibles.
- Type : trust irrévocable, mais avec letter of wishes mentionnée dans le trust deed (les souhaits du settlor sont à respecter par le trustee).

Lecture FININT : structure typique d’un trust patrimonial à finalité d’opacification du contrôle. Le settlor est identifié *quasi-certain* (leak Pandora). Le contrôle effectif est *probable* chez le settlor (letter of wishes), avec autonomie nominale du trustee. Les bénéficiaires (famille Haddad) restent à identifier précisément — recherche presse et OSINT sur l’entourage familial.

## Erreurs fréquentes

- **Considérer tout trust comme illégal.** Les trusts sont des outils juridiques largement utilisés et légitimes, notamment en droit anglo-saxon (planification successorale, protection des incapables, donations conditionnelles, etc.).
- **Considérer tout prête-nom comme volontaire.** Certaines personnes peuvent être *abusées* (mules, identités usurpées).
- **Confondre nominee et prête-nom illicite.** Le nominee anglo-saxon est légal s’il est correctement déclaré.

## Limites

La structure interne d’un trust ou d’une fondation est généralement **non publique** en l’absence de leak. La coopération internationale est nécessaire pour obtenir le trust deed, la liste des bénéficiaires, les distributions effectuées.

## Lien avec le fil rouge

> **CLEARFLOW — Trust et prête-noms**
> 
> Nassim consolide : OMEGA TRUST = structure de contrôle ultime du réseau Haddad, settlor identifié, contrôle effectif probable. En parallèle, Monsieur X et 3 autres mandataires français sont *probables* prête-noms (profils convergents avec multi-mandats, cabinet de domiciliation, absence d’expérience sectorielle). Mme Z, présidente d’une SAS, n’est pas *probable* prête-nom — son profil est différent et un recoupement avec le réseau personnel de Haddad (presse libanaise antérieure) montre un lien amical. Hypothèse Mme Z : présidente nominale avec lien personnel à Haddad, sans qualification certaine de prête-nom. Calibration *possible*.

## Points clés à retenir

- Trust : settlor + trustee + bénéficiaires + (protecteur). Fondation : fondateur + conseil + bénéficiaires.
- Tous les rôles sont, selon la 4e/5e directive AML, à considérer comme UBO.
- Prête-noms : détecter par convergence de signaux faibles, jamais sur un seul indice.
- Sources : leaks (Pandora particulièrement), coopération internationale.

-----
