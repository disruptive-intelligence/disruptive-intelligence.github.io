---
title: Chapitre 50 — OSINT spatial et imagerie satellite
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 50.1 L'imagerie satellite en sources ouvertes

L'**imagerie satellite** était historiquement réservée aux services d'État. Depuis Google Earth (2005) et la démocratisation des satellites commerciaux, elle est devenue accessible aux investigateurs OSINT.

En 2026, l'imagerie satellite OSINT est mature pour : suivi de chantiers, surveillance de sites industriels, documentation de conflits, agriculture, environnement.

## 50.2 Google Earth Pro

**Google Earth Pro** (gratuit depuis 2015). Mine standard.

**Forces.**

- Imagerie haute résolution mondiale (variable par zone).
- Historique d'images (slider temporel).
- Mesure de distances, surfaces.
- Annotations, KML.
- Visualisation 3D (Google Earth).

**Limites.**

- Fréquence de mise à jour variable.
- Source Google (couverture inégale).
- Pas d'images très récentes en général (latence semaines / mois).

## 50.3 Sentinel Hub (Copernicus)

**Sentinel Hub** (sentinel-hub.com) donne accès à l'imagerie **Sentinel** du programme européen **Copernicus**.

**Sentinel-2.** Résolution 10m. **Mises à jour très fréquentes (5 jours)** sur l'ensemble de la planète. Idéal pour surveillance continue.

**Sentinel-1.** Imagerie radar (SAR). Pénètre nuages. Utile en zones tropicales.

**Avantages.** Gratuit, mises à jour rapides, scriptable.

**Limites.** 10m de résolution : on voit les bâtiments, pas les personnes ou véhicules individuels.

## 50.4 Planet Labs

**Planet Labs** opère une constellation de **petits satellites** offrant imagerie quotidienne mondiale à résolution ~3-5m.

**Tarification.** Très chère pour usage commercial. Programmes éducationnels et research accessibles à conditions.

**Cas d'usage.** Suivi quasi-quotidien d'un site.

## 50.5 Maxar Technologies

**Maxar** (anciennement DigitalGlobe). Imagerie **très haute résolution** (30 cm). Source principale de Google Earth pour zones urbaines.

**Limites.** Accès commercial très cher. Certaines images disponibles via partenaires (services presse, ONG).

## 50.6 SkySat (Planet)

**SkySat** (Planet) : satellites haute résolution sur tasking.

## 50.7 Sources gratuites supplémentaires

**USGS Earth Explorer** : archive historique Landsat (libre).

**NASA Worldview** : imagerie quotidienne MODIS/VIIRS (basse résolution mais quotidien).

**Bhuvan** (Inde), **Roscosmos** : sources nationales.

## 50.8 Méthodes d'analyse satellite

**Comparaison temporelle.** Avant/après pour identifier changements.

**Pattern recognition.** Identifier types de bâtiments (industriel, militaire, agricole).

**Mesures.** Distances, surfaces, hauteurs (via ombres).

**Détection d'activité.** Véhicules présents, modifications de terrain.

## 50.9 Cas d'usage OSINT

**Vérification conflits.** Bellingcat utilise massivement Sentinel et Maxar pour confirmer mouvements de troupes en Ukraine.

**Surveillance industrielle.** Évolution d'un site (cas Iran nuclear : suivi sites enrichissement).

**Documentation crimes de guerre.** Identification de bombardements, mouvements de population.

**Environnement.** Déforestation, pollutions, exploitations illégales.

**Investigation corporate.** Vérifier l'activité réelle d'un site industriel déclaré.

## 50.10 Limites OSINT satellite

**Résolution.** 10m Sentinel : pas de détails fins.

**Couverture nuageuse.** Limite l'optique (sauf SAR).

**Latence.** Mises à jour pas toujours en temps réel.

**Coût haute résolution.** Maxar / Planet hors de portée du budget OSINT individuel.

**Analyse expertise.** Lire une image satellite demande expertise.

-----
