---
title: 'Chapitre 50 — Outils gratuits : registres, sanctions, presse, leaks'
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VIII — Outils, workflow et production
  - index.md
---

## Objectif du chapitre

Recenser les **outils gratuits ou freemium** utilisables en FININT pour un travail solide sans budget.

## Catalogue raisonné

**Registres d’entreprises (chapitres 11-12)** :

- France : Pappers, INPI/data.inpi.fr, Infogreffe (partiellement gratuit), BODACC.
- UK : Companies House.
- US : OpenCorporates, SEC EDGAR, registres étatiques.
- UE : BRIS via e-justice.europa.eu.
- Multi-pays : OpenCorporates (agrégateur, freemium).

**UBO et bénéficiaires effectifs (chapitre 13)** :

- France RBE : accès restreint depuis CJUE.
- UK PSC : Companies House.
- Pandora / Panama / Paradise / Pandora Papers : Offshore Leaks ICIJ.

**Sanctions et PEP** :

- OpenSanctions.org : base agrégée gratuite (sanctions OFAC, UE, ONU, OFSI, et plus).
- Site OFAC, UE consolidated list, ONU, OFSI.
- Sanctions.io : lecture libre partielle.

**Adverse media et presse** :

- Google News (avec limites).
- Médias référents accessibles en consultation gratuite.
- ICIJ Aleph (accès journalistique principalement).
- OCCRP Aleph (selon partenariats).

**Comptes annuels** :

- France : Pappers, Infogreffe.
- UK : Companies House.
- Allemagne : Bundesanzeiger.
- Belgique : Moniteur belge.

**Marchés publics** :

- BOAMP, data.gouv.fr (DECP), TED, SAM.gov, USAspending.gov.

**Patrimoine** :

- DVF (Demandes de valeurs foncières) data.gouv.fr.
- Patrim (accès via espace personnel impots.gouv.fr — limité aux usages personnels).
- Cadastre.gouv.fr.
- Bases yachts/maritime : MarineTraffic (free tier).
- Bases aéronefs : FlightAware, ADS-B Exchange.

**Visualisation gratuite** :

- Maltego (free tier, transforms limitées).
- Gephi (open source).
- Cytoscape.
- Excel/LibreOffice (graphes simples).

**Recherche d’images inverse** :

- Google Images.
- TinEye.
- Yandex.

**Archives web** :

- Web Archive (Wayback Machine).
- archive.today.

**OSINT général utile en FININT** :

- IntelTechniques (outils OSINT).
- OSINT Framework.
- Bellingcat investigations toolkit.

## Méthode — workflow gratuit type

Pour un dossier sans budget, l’enchaînement standard :

1. Pappers + INPI + Companies House + OpenCorporates → identification + cartographie initiale.
1. ICIJ Offshore Leaks → recoupement leaks.
1. OpenSanctions → screening sanctions/PEP.
1. Google + agrégateurs gratuits → adverse media.
1. DVF + cadastre + MarineTraffic → patrimoine français visible.
1. Gephi → visualisation finale.

Couvre 70-80 % d’une enquête de complexité moyenne avec un budget de 0 €.

## Erreurs fréquentes

- **Sous-estimer ce qu’on peut faire gratuitement.** Beaucoup d’analystes débutent en pensant que l’OSINT financier est inaccessible — c’est faux.
- **Surestimer la profondeur des outils gratuits.** Pour les juridictions opaques, le multi-juridictionnel intensif, l’agrégation à grande échelle, des outils professionnels sont nécessaires.

## Limites

Les outils gratuits ont des **plafonds** (nombre de requêtes, profondeur de couverture, fréquence de mise à jour). Pour des dossiers complexes ou volumineux, les outils professionnels apportent une vraie valeur ajoutée.

## Lien avec le fil rouge

> **CLEARFLOW — Phase OSINT gratuite**
> 
> Nassim utilise gratuitement Pappers, Companies House, OpenCorporates, OpenSanctions, Offshore Leaks pour le travail de cartographie initial. L’investissement dans Sayari (chapitre 51) intervient pour étendre la couverture sur les juridictions à risque où les outils gratuits sont insuffisants.

## Points clés à retenir

- Beaucoup d’OSINT financier est accessible gratuitement.
- Catalogue raisonné par usage.
- Plafond des gratuits → bascule vers professionnels selon complexité.

-----
