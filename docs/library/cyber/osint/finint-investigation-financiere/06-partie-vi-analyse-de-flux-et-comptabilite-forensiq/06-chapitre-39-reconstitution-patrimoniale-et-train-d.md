---
title: Chapitre 39 — Reconstitution patrimoniale et train de vie
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VI — Analyse DE flux et comptabilité forensique
  - index.md
---

## Objectif du chapitre

Reconstituer le **patrimoine d’une personne** : actifs visibles, actifs présumés, train de vie observable, et confronter cette reconstitution aux revenus déclarés. C’est l’une des analyses les plus délicates et les plus stratégiques du FININT.

## Le concept

Le patrimoine d’une personne se compose :

- **Actifs immobiliers** : biens en France (DVF, Patrim) et à l’étranger.
- **Actifs financiers** : participations dans sociétés, comptes bancaires, portefeuilles.
- **Actifs mobiliers de valeur** : véhicules, bateaux, aéronefs, œuvres, bijoux, montres, instruments de collection.
- **Cryptos** : adresses on-chain — renvoi à OSINT Crypto pour l’analyse détaillée.
- **Train de vie observable** : voyages, dépenses visibles, écoles privées, événements.

La **reconstitution patrimoniale** consiste à inventorier l’ensemble, l’évaluer, et le confronter aux revenus déclarés.

## L’utilité opérationnelle

La reconstitution patrimoniale sert à :

- **Détecter un train de vie incohérent** avec les revenus officiels.
- **Préparer l’asset recovery** : identifier les biens susceptibles de gel/saisie/confiscation.
- **Étayer les soupçons** d’enrichissement illicite (corruption, fraude fiscale, etc.).
- **Mesurer le préjudice** à la collectivité (en cas d’évasion fiscale, de corruption, etc.).

## Méthode — workflow de reconstitution

1. **Lister les actifs visibles** : sources ouvertes — DVF, Patrim, registres divers, presse, SOCMINT.
1. **Identifier les actifs présumés** : signaux visibles (voyages réguliers à Dubaï = possible résidence ; voiture de luxe sur Instagram = bien à identifier ; etc.).
1. **Estimer les valeurs** : recherche prix de marché, sources spécialisées.
1. **Lister les revenus déclarés** : presse (pour les dirigeants publics), déclarations HATVP, comptes annuels des sociétés détenues, distribution de dividendes traçable.
1. **Confronter** : patrimoine identifié versus revenus déclarés. Écart ? Plausibilité d’un héritage ? Activités antérieures ?
1. **Documenter les lacunes** : actifs étrangers non vérifiés, comptes bancaires inaccessibles, etc.

## Mini-walkthrough — patrimoine Haddad

Actifs visibles français :

- 3 biens immobiliers à Paris (SCI HADDAD INVESTISSEMENTS) : valeur estimée 11 M€.
- 2 véhicules de luxe (immatriculations parisiennes) : ~280 K€.
- Total France visible : ~11,3 M€.

Actifs présumés à l’étranger :

- Villa à Beyrouth (presse libanaise, photos) : valeur estimée 3-5 M€.
- Présence à Dubaï : appartement éventuel, non confirmé (~1-3 M€ si confirmé).
- Yacht (pavillon Malte, présence dans presse mondaine) : valeur estimée 4-7 M€.
- Participations dans le groupe Haddad : valorisation complexe (probablement 8-15 M€).
- Compte bancaire suisse présumé (DS) : montant non connu.
- Total présumé : 16 à 30 M€ (très large fourchette).

Train de vie observable :

- 4-6 voyages internationaux par an (Paris-Beyrouth-Dubaï-Genève).
- Événements professionnels et caritatifs fréquents.
- Réseau social haut de gamme.

Revenus déclarés (présomé sans accès aux déclarations fiscales) :

- Activité de dirigeant de Nexus Liban SAL et NEXUS INTERNATIONAL FZ.
- Plusieurs sources de revenus non publiques.

Estimation : le patrimoine total (France + étranger) est *probable* à **25-40 M€**. La cohérence avec les revenus déclarés sur 30 ans d’activité de négoce international est *possible* — un négoce international peut générer ces patrimoines légitimement. Cependant, la fraction *attribuée à des fonds d’origine illicite* serait à qualifier, *indéterminable* sans coopération internationale et accès aux déclarations.

Hypothèse : patrimoine global cohérent avec une activité réussie ; sa **construction multi-juridictionnelle opaque** est un signal de *probable* contournement fiscal et possiblement d’autres schémas, à confirmer.

## Erreurs fréquentes

- **Sous-estimer le patrimoine étranger.** Beaucoup de patrimoines de personnes d’affaires internationales sont majoritairement à l’étranger.
- **Surinterpréter le train de vie.** Un train de vie élevé peut être financé par des sources légitimes (héritage, succès commercial réel).
- **Confondre disponibilité de l’information et absence.** Un patrimoine non visible n’est pas un patrimoine nul.

## Limites

La reconstitution patrimoniale rigoureuse exige des sources fermées : déclarations fiscales, EAR/CRS pour les comptes étrangers, coopération internationale. En OSINT seul, on aboutit à des fourchettes larges et des hypothèses calibrées.

## Lien avec le fil rouge

> **CLEARFLOW — Patrimoine et asset recovery**
> 
> Sur la base de la reconstitution, Nassim identifie 11 M€ d’actifs français saisissables en théorie (sous procédure judiciaire) et présume 16-30 M€ étrangers à confirmer. La note finale recommande au PNF d’envisager des mesures conservatoires sur les actifs français, et de solliciter la coopération internationale pour qualifier et localiser les actifs étrangers.

## Points clés à retenir

- Reconstitution = actifs immobiliers + financiers + mobiliers + crypto + train de vie.
- Sources ouvertes (DVF, Patrim, registres) + SOCMINT + leaks.
- Confronter aux revenus déclarés et à la trajectoire professionnelle.
- Préparer l’asset recovery par juridiction.

-----
