---
title: Partie IV — IMINT, GEOINT et vérification visuelle
source: Cyber/02 OSINT/Méthode & enquête/OSINT — synthèse.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

---


## Chapitre 13 — IMINT : analyse d'images et recherche inversée

La **recherche inversée** : Google Images (le plus large index), Yandex Images (supérieur pour les visages), TinEye (le plus fiable pour trouver la source originale — tri par date), Bing Visual Search, Google Lens. Les métadonnées **EXIF** : coordonnées GPS, appareil, date/heure — ExifTool. La plupart des réseaux sociaux suppriment les EXIF au upload — mais les images par email ou messagerie (WhatsApp en mode document) les conservent souvent.

L'**analyse sans EXIF** (le cas le plus fréquent) : indices visuels systématiques — enseignes (langue, marque), plaques d'immatriculation (format), végétation (espèces → climat), architecture (style → culture), signalétique routière (panneaux → pays), uniformes, conditions météo. Chaque indice est un pivot de géolocalisation.

La **vérification d'authenticité** : Error Level Analysis (ELA — les zones modifiées ont un niveau d'erreur différent — FotoForensics), cohérence des ombres (direction et longueur cohérentes ?), recherche de première occurrence (TinEye tri par date — si l'image existait avant l'événement prétendu, c'est du recyclage).

**Limites :** la recherche inversée ne fonctionne que si l'image (ou une version proche) est indexée — une photo originale non publiée ne donnera aucun résultat. L'ELA a des limites (les compressions multiples JPEG créent des artefacts qui ressemblent à des modifications). L'analyse des ombres nécessite des ombres visibles et un sol plat. **La convergence de plusieurs indices est toujours plus fiable qu'un seul test technique.**

---


## Chapitre 14 — Contenus AI-generated et deepfakes

méthodologie de vérification

*Ce chapitre est méthodologique. Les outils de détection vieillissent vite et ne sont jamais fiables seuls. La discipline de vérification, elle, reste.*

### 14.1 Le principe fondamental

**Absence de preuve de manipulation ≠ authenticité.** Un outil de détection qui dit « probablement authentique » ne PROUVE PAS l'authenticité. Un outil qui dit « probablement AI-generated » donne un indice, pas une certitude. **Un seul indice technique ne suffit jamais** — la vérification repose sur la convergence de multiples indicateurs indépendants.

### 14.2 Images synthétiques

Signaux visuels (avec la précaution qu'ils deviennent de moins en moins fiables) : mains/doigts incohérents (de moins en moins discriminant), texte dans l'image illisible, arrière-plans avec structures impossibles, symétrie excessive des visages, métadonnées absentes (les images IA n'ont pas d'EXIF caméra — mais l'absence d'EXIF n'est pas une preuve de synthèse puisque les réseaux sociaux les suppriment aussi).

La méthodologie de vérification (plus fiable que les outils seuls) : (1) recherche inversée — l'image existe-t-elle ailleurs avant la date prétendue ? (2) vérification des métadonnées, (3) ELA, (4) contexte — l'image est-elle cohérente avec d'autres sources ? (5) corroboration — d'autres sources confirment-elles le contenu ? Les outils de détection (Hive Moderation, Illuminarty, SynthID — exemples à date) sont des **aides, pas des verdicts**.

### 14.3 Deepfakes vidéo, audio et texte

Vidéo (face swap, lip sync) : clignement anormal, contour du visage flou, incohérence d'éclairage. Audio (voice cloning) : microprosodie anormale, transitions abruptes. Texte : la détection technique est la moins fiable (taux de faux positifs élevé) → vérifier les faits cités (l'IA hallucine), rechercher la première occurrence, comparer le style (stylométrie).

### 14.4 Impact sur l'investigation

Un suspect peut publier de fausses preuves AI-generated. Une campagne de désinformation peut fabriquer des « preuves » visuelles. L'analyste OSINT doit **systématiquement vérifier l'authenticité AVANT d'utiliser un contenu comme élément d'analyse** — et documenter la vérification dans le rapport avec le niveau de confiance.

> **🎯 MIRAGE — Épisode 7 :** Delaunay publie une photo « preuve » de sa présence à Genève le jour d'une transaction suspecte. Vérification : (1) recherche inversée → aucune source antérieure ni confirmante, (2) EXIF → absentes, (3) ELA → incohérences, (4) contexte → la configuration du lieu ne correspond pas (Google Street View), (5) corroboration → aucun participant ne mentionne Delaunay. Conclusion : probablement synthétique ou manipulée — cotation E5. Non utilisable comme preuve, documentée comme tentative d'alibi.

---


## Chapitre 15 — GEOINT

géolocalisation, chronolocation et OSINT spatial

La **géolocalisation par indices visuels** (méthode Bellingcat) : enseignes (langue, marque → pays/ville), plaques d'immatriculation (format → pays), signalétique routière (panneaux, marquage → normes locales), végétation (espèces → climat/région), architecture (style → culture/époque), soleil et ombres (direction → hémisphère, longueur → latitude et heure). Outils : Google Maps, Street View, Mapillary, KartaView, Sentinel Hub.

La **chronolocation** : ombres → angle du soleil → calculable via SunCalc (suncalc.org) pour un lieu et une date ; conditions météo → archives (Weather Underground, ogimet.com). L'**OSINT géospatial** : imagerie satellite (Sentinel-2 — gratuit 10m, Google Earth — historique 20+ ans, Maxar/Planet — commercial haute résolution). L'OSINT **maritime** (MarineTraffic, VesselFinder — AIS tracking, historique des routes). L'OSINT **aéronautique** (FlightRadar24, ADS-B Exchange — historique de vols ; un jet privé Paris → Malte → Chypre régulièrement = indicateur). L'OSINT **véhicules** (plaques par pays, immatriculations aéronautiques, numéros de coques).

**Limites :** la géolocalisation par indices visuels nécessite des indices visibles — une photo en intérieur sans fenêtre est quasi impossible à localiser. Google Street View ne couvre pas toutes les régions (Afrique subsaharienne, Asie centrale — couverture partielle). La chronolocation par ombres nécessite un sol plat et des ombres nettes. **Risque de sur-interprétation :** un panneau en arabe ne signifie pas « Syrie » — il peut être au Maroc, en Tunisie, en Jordanie, en Irak. La combinaison de multiples indices est la seule approche fiable.

---
