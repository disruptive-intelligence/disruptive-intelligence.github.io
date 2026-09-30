---
title: Chapitre 49 — Chronolocation
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 49.1 Quand l'image a-t-elle été prise ?

La **chronolocation** (datation par analyse) consiste à déterminer **quand** une image a été prise, à partir des éléments visuels.

Cas d'usage :

- Vérifier qu'une « photo récente » n'est pas un recyclage d'image ancienne.
- Établir une timeline d'événements.
- Détecter des incohérences (image « prise à 14h » avec ombres impossibles à cette heure).

## 49.2 Indices temporels macro

**Saison.** Végétation (arbres feuillus en hiver), vêtements (manteaux, courts), météo apparente.

**Climat saisonnier régional.** Neige à Marseille en juillet = très suspect.

**Événements visibles.** Décorations Noël, drapeaux d'événement, affiches campagnes électorales.

**Année / décennie.** Technologies visibles (modèle de téléphone, de voiture), modes vestimentaires.

## 49.3 Indices temporels micro

**Heure du jour.** Lumière (matin doré, midi vertical, après-midi déclinant).

**Ombres.** Direction et longueur. Méthode shadow analysis.

## 49.4 Shadow analysis (analyse des ombres)

L'**analyse des ombres** est la technique la plus précise pour dater une photo en sources ouvertes.

**Principe.** À latitude/longitude/jour donnés, le soleil est à un endroit précis du ciel à chaque instant. Les ombres pointent dans une direction précise et ont une longueur précise.

**Inversion.** En mesurant la **direction** et la **longueur** des ombres sur une photo, et en connaissant la latitude/longitude, on peut déterminer **l'heure et la date** approximatives.

**Outils.**

**SunCalc** (suncalc.org). Calculateur position solaire. Donné une localisation et une date/heure, il affiche position solaire et direction des ombres.

**SunCalc.net** : version étendue.

**ShadowMap** (shadowmap.org) : visualisation 3D des ombres en temps réel.

**TPE — The Photographer's Ephemeris** : app payante très précise.

## 49.5 Méthodologie shadow analysis

1. **Localisation confirmée** (par GEOINT, Ch.48).
2. Mesurer **direction des ombres** sur la photo (angle par rapport à un repère cardinal connu).
3. Mesurer **longueur des ombres** par rapport à hauteur d'objets connus.
4. Sur SunCalc, **chercher** la date et l'heure correspondantes.
5. Vérifier **cohérence saisonnière** avec autres indices.
6. Trianguler.

## 49.6 Météo historique

**Cross-check météo.** Si la photo montre temps couvert / neigeux / pluvieux, vérifier la météo historique du lieu à la date supposée.

**Outils.**

- **Wolfram Alpha** : météo historique précise.
- **Weather Underground** historique.
- **Time and Date** : conditions historiques.

**Cas d'usage.** Une photo « prise à Paris le 15 juillet 2024 » montrant neige est immédiatement suspecte.

## 49.7 Métadonnées temporelles

EXIF si présent (Ch.29). Date de création du fichier.

**Limite.** Falsifiable. Ne pas se fier seul à l'EXIF.

## 49.8 Datation par technologies visibles

**Téléphones.** iPhone 15 Pro = post-septembre 2023. Galaxy S24 = post-janvier 2024.

**Logos d'entreprises.** Logo Twitter (avant juillet 2023) vs X (après) = chronolocation possible.

**Modes vestimentaires.** Plus subtil mais possible.

**Voitures.** Modèle visible permet borne « pas avant ».

## 49.9 Saisonalité végétale

**Indices.**

- Feuilles présentes / absentes / colorées.
- Floraisons spécifiques (cerisiers japonais en avril).
- Couleurs automnales.

## 49.10 Workflow chronolocation

1. Localisation confirmée.
2. Hypothèse saison / année par indices macro.
3. Shadow analysis si ombres visibles.
4. Cross-check météo si conditions visibles.
5. Validation par technologies / modes.
6. Synthèse : « photo prise entre le X et le Y avec confiance Z ».

> **MIRAGE — Épisode 12 : GEOINT et chronolocation**
>
> L'analyste examine une photo publiée par Delaunay sur LinkedIn (visible via compte d'investigation) en mai 2025 : « vue depuis la terrasse de la maison de famille ». Pas de géolocalisation EXIF (LinkedIn strippe).
>
> **Lecture.** Photo paysage, terrasse avec table en pierre, vue ouverte sur paysage rural méditerranéen : collines, oliviers, vignes au loin, cyprès. Architecture du muret : pierre sèche typique du sud de la France.
>
> **Hypothèse géographique.** Sud de la France, probablement Provence (cyprès + oliviers + pierre sèche caractéristiques).
>
> **Triangulation.** Pas de monument distinctif visible. Mais sur l'arrière-plan, une église rurale isolée avec un clocher carré.
>
> **Recherche.** Google Maps / Street View dans le triangle Provence (Drôme, Vaucluse, Bouches-du-Rhône, Var, Alpes-de-Haute-Provence). Recherche d'églises rurales isolées avec clocher carré.
>
> **Croisement avec MIRAGE 8.** Delaunay a déclaré (Pappers SCI) une propriété « La Provence Familiale ». Recherche cadastre.gouv.fr pour SCI « La Provence Familiale » avec dirigeant ou bénéficiaire Delaunay. **Hit** : SCI domiciliée à Goult (Vaucluse). Parcelle identifiée.
>
> **Vérification croisée.** Google Earth sur la parcelle Goult : terrasse correspond au cadrage de la photo LinkedIn. Église rurale à 1.2 km au sud-est, clocher carré identique à l'arrière-plan. **Géolocalisation confirmée** : maison de Delaunay à Goult, Vaucluse.
>
> **Chronolocation.** Photo publiée mai 2025 mais date de prise potentiellement antérieure. Indices : végétation luxuriante, oliviers en feuilles, ombres modérément longues (mi-journée). Saison probable : printemps ou été. Shadow analysis : ombres pointant SO-NE, environ 12-13h heure locale. SunCalc à Goult : compatible avec mois avril-septembre, heure 12h-13h GMT+2.
>
> **Synthèse.** Maison de Delaunay confirmée à Goult, Vaucluse. SCI propriétaire identifiée. Patrimoine immobilier ajouté à la fiche : Mas en Provence, estimation 1.8 M€ (valeurs locales typiques pour bien similaire).
>
> **Cotation.** A1 pour le lieu (croisement multi-sources : photo + Pappers + cadastre + Google Earth). C3 pour la chronolocation précise (large fenêtre temporelle, mais suffisant pour le rapport).

-----
