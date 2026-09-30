---
title: 'Chapitre 48 — GEOINT : géolocaliser un contenu'
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 48.1 La méthode Bellingcat comme référence

La **géolocalisation OSINT** consiste à déterminer le lieu où une image, une vidéo, ou un événement a eu lieu, en analysant les éléments visibles. La **méthode Bellingcat** est devenue la référence : exploiter chaque indice visuel jusqu'à identification précise.

Pour une investigation Ukraine, un journaliste Bellingcat peut géolocaliser une vidéo de combat dans un rayon de 10 mètres en quelques heures, en partant de zéro. Cette compétence est apprenable et structurée.

## 48.2 Méthodologie en étapes

**Étape 1 — Lecture des indices.** Que voit-on qui peut localiser ?

- Architecture (style, matériaux, époque).
- Signalétique (panneaux routiers, plaques de rue, enseignes).
- Langue visible.
- Végétation et climat.
- Topographie (relief, plat, montagne).
- Infrastructure (lignes électriques, réseau routier).
- Marqueurs culturels.

**Étape 2 — Hypothèses géographiques.** Quel pays / région ?

**Étape 3 — Recherches ciblées.** Avec hypothèse, raffiner.

**Étape 4 — Confrontation cartographique.** Comparer aux outils cartographiques.

**Étape 5 — Confirmation.** Trianguler plusieurs indices.

## 48.3 Indices visuels par catégorie

**Architecture.**

- Style régional (architecture haussmannienne = Paris, style colonial = Asie ex-coloniale).
- Toitures (tuiles méditerranéennes, ardoise du Nord, taule en pays chauds).
- Matériaux (brique rouge UK, calcaire Sud France).
- Étage moyens (densité urbaine).

**Signalétique routière.**

- Forme et couleur des panneaux (variable par pays).
- Police de caractère (DIN allemand, Transport UK, Caractères français).
- Marquages au sol (lignes continues vs discontinues, couleur).

**Plaques d'immatriculation.**

- Format (EU avec drapeau, US avec état, asiatique avec caractères).
- Couleurs distinctives.

**Plaques de rue et enseignes.**

- Langue.
- Conventions de nomenclature.

**Mobilier urbain.**

- Lampadaires (designs distinctifs).
- Bornes, poubelles, abribus.
- Téléphones publics (de plus en plus rares).

**Végétation.**

- Essences révélant climat (palmiers = tropical, conifères = nord).
- Saisonnalité.

**Lignes électriques.**

- Poteaux bois vs béton.
- Configuration des câbles.

## 48.4 Outils cartographiques principaux

**Google Maps** et **Google Earth (Pro)**. Imagerie satellite historique, Street View, mesures.

**OpenStreetMap** (osm.org). Cartographie collaborative. Données structurées.

**Overpass Turbo** (overpass-turbo.eu). Recherche dans OSM par tags. Ex : « toutes les stations-service Total dans un rayon de 5 km ».

**Mapillary** (mapillary.com, racheté Meta) : Street View collaboratif, mondial.

**KartaView** (anciennement OpenStreetCam) : alternative open source à Street View.

**Wikimapia** : couches contributives sur points d'intérêt.

## 48.5 Méthode triangulation visuelle

Pour une géolocalisation précise :

1. **Hypothèse initiale** (pays, région).
2. Identifier **2-3 points de repère** visibles dans l'image (immeuble distinctif, intersection, monument).
3. Sur Google Maps / Street View, **rechercher** ces points de repère dans la région supposée.
4. Vérifier que la **configuration relative** correspond (les 3 points doivent être dans la bonne disposition).
5. **Confirmer** par angles, lumière, ombres.

## 48.6 Cas d'usage Bellingcat

Bellingcat a publié de nombreuses méthodologies. Par exemple, l'investigation du **MH17** (Bellingcat 2015-2018) a utilisé des dizaines de géolocalisations pour suivre le mouvement du convoi BUK russe en Ukraine.

Méthode type : prendre des photos / vidéos publiées sur les réseaux sociaux par les habitants locaux, géolocaliser chacune, reconstituer l'itinéraire.

## 48.7 Sources d'images à géolocaliser

**Images d'une cible.** Photos publiées sur les réseaux sociaux pour révéler lieu de résidence, lieu de travail, déplacements.

**Vidéos virales d'événements.** Manifestations, incidents, conflits.

**Photos de prise en otage / preuve de vie.** Sources humanitaires.

**Imagerie satellite à valider.** Confrontation avec image terrestre.

## 48.8 Limites

**Images génériques.** Une chambre d'hôtel anonyme, une rue résidentielle banale peut résister à la géolocalisation.

**Images modifiées.** Recadrage, retouches peuvent éliminer les indices clés.

**Images intérieures.** Beaucoup d'indices manquent (pas de paysage).

**Images de nuit.** Indices visuels limités.

**Images très anciennes.** Le lieu a pu changer (démolition, construction).

## 48.9 LLMs multimodaux pour géolocalisation

Les **LLMs multimodaux** (GPT-4V, Claude, Gemini) peuvent suggérer des géolocalisations à partir d'images en 2026.

**Capacités 2026.**

- Identification de monuments connus.
- Reconnaissance de styles architecturaux.
- Suggestions de pays/villes basées sur indices visuels.

**Limites.**

- Hallucinations fréquentes.
- Précision variable.
- À utiliser comme **assistant**, jamais comme conclusion.

## 48.10 Synthèse — workflow géolocalisation

| Étape | Action |
|---|---|
| Lecture | Inventaire des indices visuels |
| Hypothèse | Pays / région supposée |
| Recherche | Google Maps / OSM / Mapillary |
| Triangulation | 2-3 points de repère |
| Confirmation | Cohérence relative |
| Documentation | Captures avec coordonnées GPS |
| Cotation | Niveau de confiance |

-----
