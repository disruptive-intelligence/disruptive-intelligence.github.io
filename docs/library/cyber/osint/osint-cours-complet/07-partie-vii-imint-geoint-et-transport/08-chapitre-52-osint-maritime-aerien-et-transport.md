---
title: Chapitre 52 — OSINT maritime, aérien et transport
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 52.1 Le transport comme terrain OSINT

Le **transport** (maritime, aérien, terrestre) est un terrain OSINT spécifique avec ses propres sources, outils et méthodes. Il intéresse :

- **Sanctions** : suivre les navires contournant les embargos.
- **Criminalité organisée** : trafics maritimes.
- **Journalisme** : enquêtes sur trafics, asset tracking.
- **Investigation corporate** : flotte d'une société.
- **Conflits** : mouvements d'armement.

## 52.2 Maritime — AIS et MarineTraffic

**AIS** (Automatic Identification System). Système obligatoire pour navires > 300 tonneaux internationaux. Émet position, vitesse, cap, identité.

**Sources publiques AIS.**

**MarineTraffic** (marinetraffic.com). Le plus populaire. Couverture mondiale. Recherche par navire, port, route.

**VesselFinder** (vesselfinder.com). Alternative. Données historiques mieux gérées dans certaines versions.

**FleetMon**, **MyShipTracking**. Alternatives.

**Capacités.**

- Position actuelle d'un navire.
- Historique de positions (selon abonnement).
- Détails navire : propriétaire (souvent caché derrière sociétés écrans), pavillon, IMO, MMSI.
- Photos.
- Routes historiques.

## 52.3 Investigation navire

**Pivots maritime.**

**IMO Number.** Identifiant unique permanent (lié à la coque, pas au pavillon). Suivi cross-pavillons.

**MMSI.** Identifiant lié à la station radio.

**Pavillon.** Pays d'enregistrement. Pavillons de complaisance (Libéria, Panama, Marshall Islands, Saint-Vincent) signaux faibles.

**Propriétaire et opérateur.** Souvent différents. Souvent sociétés écrans.

**Cargaisons.** Bills of lading parfois publics, manifestes douaniers.

**Outils complémentaires.**

- **Equasis** (equasis.org) : portail multi-sources pour navires (registres, accidents, inspections).
- **Lloyd's List Intelligence** (payant).
- **IHS Markit / S&P Global Maritime** (payant).
- **Shipfinder**, **VesselTracker**.

## 52.4 Pavillons et registres

**Registres principaux.**

- **Pavillon traditionnels** : Royaume-Uni, France, Allemagne, Norvège.
- **Pavillons de complaisance** : Panama, Libéria, Marshall Islands.
- **Pavillons à risque** : pavillons utilisés pour contourner sanctions (Iran, Russie, Corée du Nord récemment via diverses juridictions).

## 52.5 Sanctions maritimes et dark fleet

Depuis 2022, une **dark fleet** russe et iranienne s'est développée pour contourner les sanctions : navires vieillissants, pavillons opaques, transferts de cargaison en mer, AIS éteint.

**Investigations OSINT majeures 2022-2026.**

- Suivi des pétroliers russes contournant le price cap.
- Documentation des ship-to-ship transferts.
- Identification des opérateurs réels via sociétés écrans.

**Outils spécialisés.**

- **Tankertrackers.com** : focus pétrolier.
- **Lloyd's List Intelligence**.
- **Windward AI** (CTI maritime).
- **Pole Star** (sanctions screening maritime).

## 52.6 Aérien — ADS-B

**ADS-B** (Automatic Dependent Surveillance-Broadcast). Système d'identification aérienne. Émet position, vitesse, altitude, identité.

**Sources publiques ADS-B.**

**Flightradar24** (flightradar24.com). Populaire, freemium. Beaucoup d'aéronefs militaires masqués.

**ADS-B Exchange** (adsbexchange.com). **Référence OSINT** : ne filtre pas, montre tous les avions trackés (y compris militaires, présidentiels). Communauté de récepteurs amateurs.

**FlightAware**, **RadarBox**, **Plane Finder**. Alternatives.

## 52.7 Investigation avion

**Pivots aérien.**

**Immatriculation.** Format pays-spécifique (F- France, N- US, D- Allemagne, G- UK). Identifiable visuellement.

**ICAO 24-bit code.** Identifiant technique unique.

**Tail number / registration.** Plaque sur l'aéronef.

**Outils complémentaires.**

- **planespotters.net** : photos d'aéronefs identifiés.
- **JetPhotos** : community photos.
- **Aviation Safety Network**.
- Registres nationaux : FAA (US), CAA (UK), DGAC (FR).

## 52.8 Cas d'usage aérien

**Jets privés et oligarques.** Investigation des déplacements de personnalités via leurs jets privés. Communauté @JetTracker, @ElonJet (avant suspension X).

**Vols de renseignement / militaires.** Suivi des avions de reconnaissance OTAN, US, Russie via ADS-B Exchange.

**Itinéraires diplomatiques.** Déplacements d'avions gouvernementaux.

**Compagnies de fret.** Suivi de livraisons d'armement par avion-cargo.

## 52.9 Terrestre — trains, camions, véhicules

Le terrestre est plus opaque que maritime et aérien (pas d'équivalent AIS / ADS-B mondial).

**Trains.**

- **Live Trains** sites par pays (Trainsdvfr en France, RailwayLive UK).
- Information opérateurs.
- Twitter / X des enthousiastes ferroviaires (rail community publie observations).

**Camions et fret.**

- **TruckTraffic** et équivalents : limité, souvent commercial.
- Plateformes de fret (DeliveryGuru, etc.).
- Caméras autoroute publiques (Sytadin pour Paris).

**Véhicules.**

- Caméras de surveillance publiques (où légalement accessible).
- Photos de capture (parking, accidents, événements publics).
- Plaques d'immatriculation : recherche limitée légalement (variable par pays — en France, recherche directe interdite hors LEA).

## 52.10 Cas d'usage transport

**Sanctions.** Suivi du contournement (tankers, fret).

**Criminalité organisée.** Trafics de stupéfiants (maritime, aérien notamment Caraïbes / Méditerranée).

**Conflits armés.** Mouvements d'armement.

**Enquête sur déplacements personnels (avec déontologie).** Limité par RGPD.

**Investigation corporate.** Flotte de transport d'une société (logistique, supply chain).

## 52.11 Synthèse — boîte à outils transport

| Domaine | Outil principal | Niveau accès |
|---|---|---|
| Maritime | MarineTraffic + ADS-B Exchange | Freemium, premium étendu |
| Maritime forensic | Equasis + Lloyd's List | Mixte |
| Aérien standard | Flightradar24 | Freemium |
| Aérien militaire / non-filtré | ADS-B Exchange | Gratuit |
| Photos aéronefs | planespotters.net | Gratuit |
| Terrestre | Live Trains, Twitter/X observers | Gratuit |
| Plaques | Limité, juridiction-dépendant | Souvent restreint |

Pour les enquêtes avancées (sanctions maritimes complexes, traffic flow analysis), partenariat avec acteurs spécialisés (Windward, Tankertrackers) ou agence (Lloyd's, IHS Markit).

-----
