---
title: Chapitre 30 — Construire une fiche actif
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie V — Cartographier les réseaux financiers
  - index.md
---

## Objectif du chapitre

Maîtriser la **fiche actif** : livrable centré sur un bien (immobilier, financier, mobilier de valeur), structurant son identification, ses détenteurs (juridiques et effectifs), son historique d’acquisition, sa valeur estimée, et sa pertinence dans l’enquête. Modèle en annexe F.

## Le concept

Une fiche actif documente :

- **Identification** : nature du bien (immobilier, véhicule, bateau, œuvre, participation), localisation, identifiants.
- **Détenteurs** : propriétaire juridique (SCI, société, personne), UBO probable, financement.
- **Historique** : date d’acquisition, prix, mode de financement, transactions antérieures.
- **Valeur** : valorisation actuelle, source de l’estimation.
- **Pertinence** : pourquoi cet actif est dans le dossier, lien avec la personne ou la société cible.
- **Asset recovery** : susceptibilité de gel / saisie, juridiction, autorité compétente.

## Types d’actifs traités

**Immobilier** : maisons, appartements, biens commerciaux. Sources : registres fonciers (variables selon pays), Patrim France (consultation administrative), DVF (Demandes de Valeurs Foncières en France, données ouvertes), bases de données commerciales (CityScan, RealCapital), presse mondaine pour les transactions remarquables.

**Véhicules** : voitures de luxe, supercars. Registre des véhicules selon pays.

**Bateaux et yachts** : registres internationaux (Lloyd’s Register, MarineTraffic pour le tracking AIS), pavillons (souvent Malte, Cayman, Bahamas, Marshall pour les yachts).

**Aéronefs** : FAA (US), EASA (UE), pavillon de l’aéronef, traçage ADS-B (FlightAware, ADS-B Exchange).

**Participations financières** : actions, parts sociales, obligations, OPCVM, ETF.

**Œuvres d’art, objets de collection** : registres internes des maisons de ventes (Sotheby’s, Christie’s), bases académiques (Art Loss Register), provenance.

**Comptes bancaires** : pas directement « actifs » mais véhicules de détention. Existence parfois traçable via EAR/CRS pour la CRF.

**Cryptos** : adresses on-chain (renvoi vers OSINT Crypto).

## L’utilité opérationnelle

La fiche actif sert deux objectifs :

1. **Documenter le patrimoine** d’une personne ou d’un groupe — base de la reconstitution patrimoniale (chapitre 39).
1. **Préparer l’asset recovery** : gel, saisie, confiscation (chapitre 66) — l’identification précise et juridictionnellement qualifiée des actifs est la condition préalable.

## Méthode

1. **Identifier le bien** par sources ouvertes (cadastre, DVF, AIS, presse).
1. **Identifier le propriétaire juridique** : personne physique, SCI, société.
1. **Remonter jusqu’à l’UBO** quand possible.
1. **Documenter l’historique** : date d’acquisition, prix, mode (cash, prêt, virement, mixte).
1. **Estimer la valeur actuelle**.
1. **Qualifier la cohérence** : ce bien est-il cohérent avec les revenus déclarés du détenteur ?
1. **Identifier la juridiction** et l’autorité compétente pour un éventuel asset recovery.

## Mini-walkthrough — fiche actif (extrait)

```
FICHE ACTIF — APPARTEMENT PARIS 8e
Référence : CLEARFLOW/ACT/004 | v1.0 | TLP:AMBER

IDENTIFICATION
- Nature : appartement résidentiel
- Localisation : 5 rue X, Paris 8e
- Surface : ~280 m², 6e étage
- Identifiant cadastral : 75108-XXXX-XXXX

DÉTENTEUR JURIDIQUE (quasi-certain)
- SCI HADDAD INVESTISSEMENTS (France), détention 100 %
- Gérance : Mme Z (présidente d'une autre SAS du réseau, lien personnel à K. Haddad)

UBO PROBABLE
- Karim Élie Haddad, via SCI

HISTORIQUE
- Acquisition : 09/2019
- Prix d'acquisition (DVF) : 4,2 M€
- Financement : non transparent en OSINT. Pas de prêt notarié inscrit visible (vérifier hypothèques inscrites).

VALEUR ACTUELLE ESTIMÉE
- Estimation marché : 4,7 M€ (basé sur prix au m² du quartier — DVF récent)
- Source : DVF + cabinet d'estimation (à approfondir)

PERTINENCE
- Bien probablement détenu par K. Haddad via SCI.
- Cohérence avec revenus déclarés : à examiner (déclaration fiscale via réquisition).

ASSET RECOVERY
- Juridiction : France.
- Autorité compétente : AGRASC (gel/saisie/confiscation), sous procédure judiciaire.
- Réalisable si infraction qualifiée et procédure ouverte.

SOURCES
- DVF data.gouv.fr
- Registre foncier (consultation)
- Pappers (SCI)
```


## Erreurs fréquentes

- **Confondre détenteur juridique et UBO.** Une SCI détient ; l’UBO contrôle la SCI.
- **Estimer la valeur sans source.** Mention explicite de la méthode et de la source.
- **Considérer un bien comme « confiscable » sans procédure.** L’asset recovery exige un cadre judiciaire.

## Limites

L’estimation de la valeur est **indicative**. Les biens à l’étranger (Dubaï, Beyrouth, Genève) ne sont pas accessibles avec la même précision que les biens français.

## Lien avec le fil rouge

> **CLEARFLOW — Cartographie patrimoniale**
> 
> Nassim identifie 11 actifs significatifs : 3 biens immobiliers à Paris (via SCI), 1 villa à Beyrouth (présomée, à confirmer), 1 yacht enregistré sous pavillon Malte (présent dans presse), 2 véhicules de luxe immatriculés à Paris, 4 participations dans des sociétés non encore consolidées dans la cartographie. Le total estimé : environ 18 M€ pour les actifs visibles français + 6 à 12 M€ pour les actifs étrangers présumés. À comparer aux revenus déclarés français (à obtenir via DGFiP).

## Points clés à retenir

- Fiche actif : un bien, un livrable.
- Distinguer détenteur juridique et UBO.
- Estimation de valeur sourcée.
- Préparer l’éventuel asset recovery par juridiction.

-----
