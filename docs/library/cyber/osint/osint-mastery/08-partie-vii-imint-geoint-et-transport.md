---
title: PARTIE VII — IMINT, GEOINT et transport
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 8
chapters: 15
---

> **Ce que cette partie apprend.** Analyser une image, exploiter la recherche inversée, conduire des analyses techniques (ELA, EXIF, forensiques), géolocaliser un contenu, dater par chronolocation, exploiter l'imagerie satellite, mobiliser les agents IA de géolocalisation 2026, investiguer le transport (maritime, aérien, terrestre).
>
> **Ce qu'elle ne couvre pas.** La détection des deepfakes et contenus synthétiques (Partie VIII), la production du rapport (Partie XII).
>
> **Ce que vous saurez faire après cette partie.** Conduire une investigation IMINT complète, géolocaliser une photo ou vidéo, exploiter Sentinel/Google Earth/Maxar en sources ouvertes, intégrer les agents IA de géolocalisation avec discernement, investiguer un navire/avion/véhicule.

-----

### Chapitre 45 — IMINT : analyse d'image

#### 45.1 IMINT en sources ouvertes : la discipline

L'**IMINT** (Image Intelligence) en sources ouvertes est l'une des sous-disciplines les plus matures de l'OSINT contemporaine. Bellingcat a démontré dès 2014 que des amateurs formés pouvaient produire du renseignement IMINT de qualité (enquête MH17, Skripal, conflits divers).

Une analyse d'image OSINT mature combine cinq étapes : **lecture** (que voit-on ?), **vérification de source** (d'où vient l'image ?), **vérification d'authenticité** (est-elle modifiée ?), **contextualisation** (où ? quand ? quoi ?), **corroboration** (autres sources confirment-elles ?).

#### 45.2 Lecture d'image méthodique

La **lecture méthodique** d'une image est une compétence sous-estimée. Trop d'analystes se contentent d'un coup d'œil rapide. Une lecture rigoureuse identifie :

**Plan général.**
- Cadrage (gros plan, plan moyen, large).
- Sujet principal.
- Sujets secondaires.
- Composition.

**Éléments architecturaux et urbains.**
- Bâtiments : style, époque, hauteur, matériaux.
- Mobilier urbain : panneaux, lampadaires, poubelles.
- Voirie : type de revêtement, marquages.
- Végétation : essences (révèle climat).

**Éléments humains.**
- Vêtements (style, époque, climat).
- Objets portés.
- Postures.
- Nombre de personnes.

**Éléments techniques.**
- Véhicules : marque, modèle, plaque (à pixelliser si publication).
- Technologies visibles (téléphones, écrans).

**Signaux temporels.**
- Saison (végétation, vêtements).
- Heure (lumière, ombres).
- Année / décennie (technologies, modes).

#### 45.3 Métadonnées EXIF (rappel)

Voir Ch.29 pour les métadonnées EXIF en détail.

**Pour IMINT.**
- GPS si présent → géolocalisation directe.
- Date / heure → datation.
- Appareil → corrélation cross-photos.
- Logiciel de retouche → détection de manipulation.

**Limite 2026.** Plateformes sociales suppriment EXIF à l'upload. Donc EXIF utile principalement pour fichiers transmis directement, pris du téléphone, ou téléchargés de sites brut.

#### 45.4 Pivots IMINT

Une image peut servir de sélecteur pour multiples pivots.

**Pivot visage** : reconnaissance faciale (Ch.30).

**Pivot lieu** : recherche inversée localise lieu, GEOINT confirme.

**Pivot objet** : un objet rare visible peut être identifié (modèle de voiture précis, logo d'entreprise, uniforme militaire).

**Pivot scène** : un contexte (manifestation, événement) identifié.

**Pivot timestamp** : datation précise via éléments visuels.

**Pivot infrastructure visuelle** : type de signalétique révèle pays (signalisation routière diffère par pays).

#### 45.5 Outils de lecture assistée

**Google Lens.** Identifier objets, lieux, textes dans l'image. Souvent surprenant.

**Bing Visual Search.** Alternative.

**Yandex Images.** Reverse + identification souvent supérieure pour scènes.

**LLMs multimodaux (Claude, GPT-4V, Gemini)**. En 2026, les LLMs peuvent décrire une image en détail, identifier des éléments. **Avec vérification** : leur identification est sujette à hallucinations.

#### 45.6 Composition technique d'une image

**Résolution.** Image 4K vs 480p révèle source (téléphone récent vs vieille caméra de surveillance).

**Compression.** JPEG répété dégrade : si une image est manifestement très compressée, elle a été partagée de nombreuses fois.

**Rapport d'aspect.** 16:9 (cinéma), 4:3 (TV ancienne), 9:16 (téléphone vertical), 1:1 (Instagram classique).

**Noise et grain.** ISO élevé en condition basse lumière, qualité d'optique.

#### 45.7 Authenticité préliminaire

Avant analyse approfondie, signaux rapides d'authenticité.

**Signaux suspects.**
- Mains, doigts, oreilles, dents anormaux → IA générée (Ch.53).
- Ombres incohérentes → composite ou manipulation.
- Pixellisation locale → masquage / inserts.
- Cohérence physique des objets, gravité.

#### 45.8 Cas particulier des screenshots

Un **screenshot** (capture d'écran) est un type d'image fréquent en OSINT.

**Authenticité.**
- Vérifier la cohérence d'interface (bonne version de l'app, date affichée plausible).
- Vérifier polices, éléments d'UI (vrais ou refaits ?).
- Recherche inversée pour autres apparitions.

**Limites.** Un screenshot est aisément fabricable. Cotation prudente, corroboration recommandée.

#### 45.9 Workflow analyse d'image type

1. **Capture et préservation** : SingleFile, hash, EXIF préservé si possible.
2. **Lecture méthodique** : éléments identifiés.
3. **Métadonnées EXIF** : ExifTool.
4. **Recherche inversée** (Ch.46).
5. **Analyse technique** (Ch.47).
6. **Géolocalisation** (Ch.48).
7. **Chronolocation** (Ch.49).
8. **Synthèse cotée**.

#### 45.10 Pièges classiques

- **Confiance excessive en EXIF** : peut être falsifié.
- **Saut à conclusion** : un détail mal interprété produit hypothèse erronée.
- **Biais culturel** : un Occidental lit mal une scène asiatique faute de référentiel.
- **Image hors contexte** : prêchant des conclusions à partir d'un cadrage restreint.
- **Confiance LLM** : une description LLM hallucinée acceptée comme analyse.

> **Principe IMINT.** Lire avant de conclure. Une image qui semble révéler X mérite la même rigueur qu'un témoignage oral : examen méthodique, corroboration, cotation.

-----

### Chapitre 46 — Recherche inversée et indexation visuelle

#### 46.1 La recherche inversée : technique pivot

La **recherche inversée d'image** prend une image en entrée et retourne ses autres occurrences sur le web. C'est l'un des outils les plus puissants de l'IMINT moderne.

Usages :
- Identifier la source originelle d'une image (provenance).
- Détecter le recyclage d'une image dans un contexte trompeur.
- Géolocaliser via lieux identifiés ailleurs.
- Reconnaître personnes, objets, scènes.
- Vérifier l'authenticité (une « photo récente d'un événement » identifiée comme une photo de 2018 = manipulation).

#### 46.2 Yandex Images : référence 2026

**Yandex Images** est régulièrement classé comme le meilleur moteur de recherche inversée pour 2026.

**Forces.**
- Indexation différente (couvre des sources que Google ignore).
- Reconnaissance de visages, scènes, objets.
- Bien meilleur sur images modifiées légèrement (recadrage, légère retouche).
- Excellence sur populations slaves et CEI.

**Méthode.**
- yandex.com/images → glisser-déposer l'image.
- Filtres : par taille, par couleur, par site.
- Examen méthodique des résultats.

#### 46.3 Google Lens et Google Images

**Google Lens** (lens.google.com). L'outil unifié Google. Identification d'objets, lieux, textes. Reverse image search.

**Google Images reverse.** Plus traditionnel, accessible via images.google.com.

**Comparaison.** Lens est plus puissant pour identifier (objets, monuments, plantes). Google Images reverse est plus exhaustif pour pages contenant l'image. Yandex souvent meilleur globalement.

#### 46.4 TinEye

**TinEye** (tineye.com) est l'un des plus anciens moteurs de recherche inversée.

**Forces.**
- Excellent pour identifier l'occurrence la plus ancienne d'une image (« first seen »).
- Permet de tracer la chronologie de diffusion.
- Plugin navigateur.

**Limites.** Couverture moins exhaustive que Yandex/Google sur volumes contemporains.

#### 46.5 Bing Visual Search

**Bing Visual Search** propose des fonctionnalités similaires à Google Lens, avec différences d'indexation.

**Forces.**
- Couverture Microsoft / Asie souvent meilleure.
- Bonne reconnaissance d'objets, marques.

#### 46.6 Méthode multi-moteurs systématique

**Principe 2026.** Toute image importante est testée sur **au moins 3-4 moteurs** :

1. Yandex Images.
2. Google Lens.
3. TinEye.
4. Bing Visual Search.

Les résultats sont **différents**. Aucun moteur n'indexe tout. La combinaison maximise la couverture.

#### 46.7 Recherche par visage versus par scène

**Recherche par visage.** PimEyes, FaceCheck (Ch.30). Spécialisée.

**Recherche par scène.** Yandex, Google Lens. Reconnaît bâtiments, paysages.

**Recherche par objet.** Google Lens excellent (téléphone modèle, voiture modèle, produits commerciaux).

**Adapter le moteur au besoin.**

#### 46.8 Techniques d'amélioration

**Recadrage.** Si l'image entière ne retourne rien, recadrer une partie distinctive (visage, monument, objet rare).

**Variantes.** Tester avec et sans retouche, en versions colorisées vs N&B, à différentes résolutions.

**Filtres.** Filtrer par date, taille, type de page.

**Outils complémentaires.** RevEye (extension), Search by Image (extension multi-moteurs).

#### 46.9 Limites d'indexation

**Ce qui n'est pas indexé.**
- Contenus derrière login (réseaux sociaux privés).
- Documents PDFs (parfois).
- Images dans contextes éphémères (stories supprimées).
- Sites avec robots.txt restrictif.
- Dark web.

**Implication.** Une absence de résultats ne prouve pas que l'image est « originale ». Elle peut être dans des espaces non indexés.

#### 46.10 Synthèse — workflow recherche inversée

| Étape | Action |
|---|---|
| Préparation | Image extracted, hash calculé, copie locale |
| Multi-moteurs | Yandex + Google Lens + TinEye + Bing |
| Recadrages | Tester crops si nécessaire |
| Examen résultats | Sources primaires identifiées |
| Provenance | Source la plus ancienne (TinEye « first seen ») |
| Documentation | Captures avec timestamps |
| Synthèse | Cotation et hypothèses |

-----

### Chapitre 47 — Analyse technique d'image

#### 47.1 Au-delà de la lecture : la forensique d'image

Quand une image est suspecte ou critique pour une enquête, l'**analyse technique** (forensique d'image) peut révéler manipulations, retouches, incohérences invisibles à l'œil nu.

L'analyse technique ne remplace pas la lecture méthodique — elle la complète. Et elle a des **limites** : un faux bien fait peut résister à toutes les analyses classiques.

#### 47.2 ExifTool : la pierre angulaire

**ExifTool** (Phil Harvey) est l'outil standard pour métadonnées d'images.

**Capacités.**
- Lecture de toutes les métadonnées (EXIF, IPTC, XMP).
- Multi-formats (JPEG, PNG, TIFF, RAW, vidéo).
- Détection d'incohérences (timestamp modifié, logiciel inattendu).

**Indicateurs suspects.**
- Champ `Software` indiquant Photoshop : retouche probable.
- Date `Modify` ≠ date `Create` : modification.
- Géolocation absente alors qu'on attendrait : strippée.
- Profil ICC ou paramètres inhabituels pour le device déclaré.

#### 47.3 ELA — Error Level Analysis

L'**ELA** (Analyse de niveau d'erreur) compare la compression locale d'une image. Les zones modifiées (re-compressées) ressortent différemment.

**Outils.**
- **FotoForensics** (fotoforensics.com) : interface web simple.
- **Forensically** (29a.ch/photo-forensics) : suite d'outils ELA + clone detection + autres.
- **GIMP** + plugin ELA.

**Méthode.**
1. Upload de l'image.
2. Examen visuel ELA : les zones uniformes ressortent différemment.
3. Comparaison régions suspectes vs régions a priori intactes.

**Limites.**
- ELA est **indicatif**, pas définitif.
- Images très compressées (réseaux sociaux multiples uploads) : ELA bruité, peu lisible.
- Sophistication des manipulations modernes peut tromper ELA.

#### 47.4 Clone detection

La **détection de clone** identifie les zones d'une image qui sont des copies internes (tampon de clone, copies pour masquer).

**Outils.**
- **Forensically** (clone detection).
- **JPEGsnoop**.

**Cas d'usage.** Une photo de foule où des manifestants ont été dupliqués pour amplifier l'apparence de masse.

#### 47.5 Analyse de luminosité, gradient, bruit

D'autres analyses techniques :

**Luminance gradient.** Met en évidence les bordures et différences d'éclairage.

**Noise analysis.** Le bruit (grain) doit être cohérent dans toute l'image. Des zones avec un bruit différent suggèrent insertion.

**JPEG ghosts.** Compression JPEG répétée laisse des « fantômes ». L'analyse révèle si des zones ont été insérées depuis une source compressée différemment.

**Outils.** Forensically intègre la plupart.

#### 47.6 Analyse spectrale

L'**analyse spectrale** examine les fréquences de l'image (transformée de Fourier).

**Cas d'usage avancé.** Détection de watermarks invisibles, de patterns d'IA, d'inserts subtils.

**Outils.**
- ImageMagick avec FFT.
- Python (scipy.fft).

#### 47.7 Détection IA générée (Ch.30 et Ch.56 développent)

Outils spécifiques :
- **Hive Moderation**.
- **Optic AI or Not**.
- **Sensity AI**.
- **Intel FakeCatcher**.

À utiliser systématiquement sur images suspectes en 2026.

#### 47.8 Vidéo : analyse frame par frame

Pour vidéos suspectes :

1. Extraction des frames clés (ffmpeg).
2. Analyse de chaque frame comme image.
3. Recherche d'incohérences entre frames consécutives.
4. Détection deepfake spécifique (Ch.56).

```bash
ffmpeg -i video.mp4 -vf "select=eq(pict_type\,I)" -vsync vfr frame_%04d.png
```

#### 47.9 Limites de l'analyse technique

**Faux positifs.** Une image authentique peut « ELA suspect » pour raisons techniques (recompression réseau social).

**Faux négatifs.** Un faux sophistiqué peut résister.

**Course offensive/défensive.** Les outils de génération IA et les outils de détection évoluent en parallèle.

**Implication.** L'analyse technique est **un indice**, pas une preuve. Cotation prudente.

#### 47.10 Méthodologie type

Pour une image suspecte :

1. EXIF (ExifTool).
2. Hash et préservation.
3. ELA (Forensically / FotoForensics).
4. Clone detection.
5. Analyse spectrale si nécessaire.
6. Détection IA (Hive, Optic).
7. Recherche inversée (Ch.46).
8. Synthèse cotée.

> **MIRAGE — Épisode 11 : Image suspecte et vérification**
>
> L'analyste examine les **trois fausses photographies** de « soirées professionnelles » destinées à fabriquer un narratif d'inconduite contre Berthier (mentionnées dans le mandat MIRAGE).
>
> **Image 1.** Photo prétendument « Antoine Berthier lors d'une soirée privée 2024 », publiée sur `info-finance-eu.com` le 14 mars 2026.
>
> **Lecture méthodique.** Pièce sombre, plusieurs personnes en arrière-plan flou, sujet central tenant une coupe. Style propre (résolution 1920×1280). Aucun élément architectural distinctif visible.
>
> **EXIF.** Strippé (capture web). Pas d'information directe.
>
> **Recherche inversée Yandex.** Hit critique : l'image principale (sans le visage de Berthier visiblement remplacé) apparaît sur **Unsplash**, photo stock libre, photographe Mark Adriane, datée 2021, intitulée « party scene ». La photo originale est une image stock générique.
>
> **Analyse comparative.** Vérification visuelle du visage de Berthier : superposé sur la photo stock. Comparaison avec photo profil LinkedIn de Berthier : ressemblance forte mais avec léger lissage caractéristique d'une opération de face swap.
>
> **Hive Moderation** sur la zone du visage : score « likely manipulated 67 % ». Cohérent.
>
> **ELA Forensically.** Zone du visage de Berthier ressort différemment du reste : compression locale incohérente. Forte présomption de manipulation.
>
> **Conclusion image 1.** Photo composite : fond Unsplash 2021 + face swap du visage de Berthier. Cotation A1 (sources techniques convergentes + source originale identifiée). **Élément majeur du dossier** : démonstration formelle qu'au moins une « photo Berthier » est entièrement fabriquée.
>
> **Images 2 et 3.** Analyses similaires révèlent même pattern (deux autres fonds Unsplash / Pexels + face swaps). Cluster de fabrication.
>
> **Implication enquête.** La preuve que ces photos sont fabriquées renforce massivement le dossier de diffamation organisée. Couplée à la vidéo deepfake de Berthier (MIRAGE 16) et au cluster désinformation, elle dessine une campagne sophistiquée.

-----

### Chapitre 48 — GEOINT : géolocaliser un contenu

#### 48.1 La méthode Bellingcat comme référence

La **géolocalisation OSINT** consiste à déterminer le lieu où une image, une vidéo, ou un événement a eu lieu, en analysant les éléments visibles. La **méthode Bellingcat** est devenue la référence : exploiter chaque indice visuel jusqu'à identification précise.

Pour une investigation Ukraine, un journaliste Bellingcat peut géolocaliser une vidéo de combat dans un rayon de 10 mètres en quelques heures, en partant de zéro. Cette compétence est apprenable et structurée.

#### 48.2 Méthodologie en étapes

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

#### 48.3 Indices visuels par catégorie

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

#### 48.4 Outils cartographiques principaux

**Google Maps** et **Google Earth (Pro)**. Imagerie satellite historique, Street View, mesures.

**OpenStreetMap** (osm.org). Cartographie collaborative. Données structurées.

**Overpass Turbo** (overpass-turbo.eu). Recherche dans OSM par tags. Ex : « toutes les stations-service Total dans un rayon de 5 km ».

**Mapillary** (mapillary.com, racheté Meta) : Street View collaboratif, mondial.

**KartaView** (anciennement OpenStreetCam) : alternative open source à Street View.

**Wikimapia** : couches contributives sur points d'intérêt.

#### 48.5 Méthode triangulation visuelle

Pour une géolocalisation précise :

1. **Hypothèse initiale** (pays, région).
2. Identifier **2-3 points de repère** visibles dans l'image (immeuble distinctif, intersection, monument).
3. Sur Google Maps / Street View, **rechercher** ces points de repère dans la région supposée.
4. Vérifier que la **configuration relative** correspond (les 3 points doivent être dans la bonne disposition).
5. **Confirmer** par angles, lumière, ombres.

#### 48.6 Cas d'usage Bellingcat

Bellingcat a publié de nombreuses méthodologies. Par exemple, l'investigation du **MH17** (Bellingcat 2015-2018) a utilisé des dizaines de géolocalisations pour suivre le mouvement du convoi BUK russe en Ukraine.

Méthode type : prendre des photos / vidéos publiées sur les réseaux sociaux par les habitants locaux, géolocaliser chacune, reconstituer l'itinéraire.

#### 48.7 Sources d'images à géolocaliser

**Images d'une cible.** Photos publiées sur les réseaux sociaux pour révéler lieu de résidence, lieu de travail, déplacements.

**Vidéos virales d'événements.** Manifestations, incidents, conflits.

**Photos de prise en otage / preuve de vie.** Sources humanitaires.

**Imagerie satellite à valider.** Confrontation avec image terrestre.

#### 48.8 Limites

**Images génériques.** Une chambre d'hôtel anonyme, une rue résidentielle banale peut résister à la géolocalisation.

**Images modifiées.** Recadrage, retouches peuvent éliminer les indices clés.

**Images intérieures.** Beaucoup d'indices manquent (pas de paysage).

**Images de nuit.** Indices visuels limités.

**Images très anciennes.** Le lieu a pu changer (démolition, construction).

#### 48.9 LLMs multimodaux pour géolocalisation

Les **LLMs multimodaux** (GPT-4V, Claude, Gemini) peuvent suggérer des géolocalisations à partir d'images en 2026.

**Capacités 2026.**
- Identification de monuments connus.
- Reconnaissance de styles architecturaux.
- Suggestions de pays/villes basées sur indices visuels.

**Limites.**
- Hallucinations fréquentes.
- Précision variable.
- À utiliser comme **assistant**, jamais comme conclusion.

#### 48.10 Synthèse — workflow géolocalisation

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

### Chapitre 49 — Chronolocation

#### 49.1 Quand l'image a-t-elle été prise ?

La **chronolocation** (datation par analyse) consiste à déterminer **quand** une image a été prise, à partir des éléments visuels.

Cas d'usage :
- Vérifier qu'une « photo récente » n'est pas un recyclage d'image ancienne.
- Établir une timeline d'événements.
- Détecter des incohérences (image « prise à 14h » avec ombres impossibles à cette heure).

#### 49.2 Indices temporels macro

**Saison.** Végétation (arbres feuillus en hiver), vêtements (manteaux, courts), météo apparente.

**Climat saisonnier régional.** Neige à Marseille en juillet = très suspect.

**Événements visibles.** Décorations Noël, drapeaux d'événement, affiches campagnes électorales.

**Année / décennie.** Technologies visibles (modèle de téléphone, de voiture), modes vestimentaires.

#### 49.3 Indices temporels micro

**Heure du jour.** Lumière (matin doré, midi vertical, après-midi déclinant).

**Ombres.** Direction et longueur. Méthode shadow analysis.

#### 49.4 Shadow analysis (analyse des ombres)

L'**analyse des ombres** est la technique la plus précise pour dater une photo en sources ouvertes.

**Principe.** À latitude/longitude/jour donnés, le soleil est à un endroit précis du ciel à chaque instant. Les ombres pointent dans une direction précise et ont une longueur précise.

**Inversion.** En mesurant la **direction** et la **longueur** des ombres sur une photo, et en connaissant la latitude/longitude, on peut déterminer **l'heure et la date** approximatives.

**Outils.**

**SunCalc** (suncalc.org). Calculateur position solaire. Donné une localisation et une date/heure, il affiche position solaire et direction des ombres.

**SunCalc.net** : version étendue.

**ShadowMap** (shadowmap.org) : visualisation 3D des ombres en temps réel.

**TPE — The Photographer's Ephemeris** : app payante très précise.

#### 49.5 Méthodologie shadow analysis

1. **Localisation confirmée** (par GEOINT, Ch.48).
2. Mesurer **direction des ombres** sur la photo (angle par rapport à un repère cardinal connu).
3. Mesurer **longueur des ombres** par rapport à hauteur d'objets connus.
4. Sur SunCalc, **chercher** la date et l'heure correspondantes.
5. Vérifier **cohérence saisonnière** avec autres indices.
6. Trianguler.

#### 49.6 Météo historique

**Cross-check météo.** Si la photo montre temps couvert / neigeux / pluvieux, vérifier la météo historique du lieu à la date supposée.

**Outils.**
- **Wolfram Alpha** : météo historique précise.
- **Weather Underground** historique.
- **Time and Date** : conditions historiques.

**Cas d'usage.** Une photo « prise à Paris le 15 juillet 2024 » montrant neige est immédiatement suspecte.

#### 49.7 Métadonnées temporelles

EXIF si présent (Ch.29). Date de création du fichier.

**Limite.** Falsifiable. Ne pas se fier seul à l'EXIF.

#### 49.8 Datation par technologies visibles

**Téléphones.** iPhone 15 Pro = post-septembre 2023. Galaxy S24 = post-janvier 2024.

**Logos d'entreprises.** Logo Twitter (avant juillet 2023) vs X (après) = chronolocation possible.

**Modes vestimentaires.** Plus subtil mais possible.

**Voitures.** Modèle visible permet borne « pas avant ».

#### 49.9 Saisonalité végétale

**Indices.**
- Feuilles présentes / absentes / colorées.
- Floraisons spécifiques (cerisiers japonais en avril).
- Couleurs automnales.

#### 49.10 Workflow chronolocation

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

### Chapitre 50 — OSINT spatial et imagerie satellite

#### 50.1 L'imagerie satellite en sources ouvertes

L'**imagerie satellite** était historiquement réservée aux services d'État. Depuis Google Earth (2005) et la démocratisation des satellites commerciaux, elle est devenue accessible aux investigateurs OSINT.

En 2026, l'imagerie satellite OSINT est mature pour : suivi de chantiers, surveillance de sites industriels, documentation de conflits, agriculture, environnement.

#### 50.2 Google Earth Pro

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

#### 50.3 Sentinel Hub (Copernicus)

**Sentinel Hub** (sentinel-hub.com) donne accès à l'imagerie **Sentinel** du programme européen **Copernicus**.

**Sentinel-2.** Résolution 10m. **Mises à jour très fréquentes (5 jours)** sur l'ensemble de la planète. Idéal pour surveillance continue.

**Sentinel-1.** Imagerie radar (SAR). Pénètre nuages. Utile en zones tropicales.

**Avantages.** Gratuit, mises à jour rapides, scriptable.

**Limites.** 10m de résolution : on voit les bâtiments, pas les personnes ou véhicules individuels.

#### 50.4 Planet Labs

**Planet Labs** opère une constellation de **petits satellites** offrant imagerie quotidienne mondiale à résolution ~3-5m.

**Tarification.** Très chère pour usage commercial. Programmes éducationnels et research accessibles à conditions.

**Cas d'usage.** Suivi quasi-quotidien d'un site.

#### 50.5 Maxar Technologies

**Maxar** (anciennement DigitalGlobe). Imagerie **très haute résolution** (30 cm). Source principale de Google Earth pour zones urbaines.

**Limites.** Accès commercial très cher. Certaines images disponibles via partenaires (services presse, ONG).

#### 50.6 SkySat (Planet)

**SkySat** (Planet) : satellites haute résolution sur tasking.

#### 50.7 Sources gratuites supplémentaires

**USGS Earth Explorer** : archive historique Landsat (libre).

**NASA Worldview** : imagerie quotidienne MODIS/VIIRS (basse résolution mais quotidien).

**Bhuvan** (Inde), **Roscosmos** : sources nationales.

#### 50.8 Méthodes d'analyse satellite

**Comparaison temporelle.** Avant/après pour identifier changements.

**Pattern recognition.** Identifier types de bâtiments (industriel, militaire, agricole).

**Mesures.** Distances, surfaces, hauteurs (via ombres).

**Détection d'activité.** Véhicules présents, modifications de terrain.

#### 50.9 Cas d'usage OSINT

**Vérification conflits.** Bellingcat utilise massivement Sentinel et Maxar pour confirmer mouvements de troupes en Ukraine.

**Surveillance industrielle.** Évolution d'un site (cas Iran nuclear : suivi sites enrichissement).

**Documentation crimes de guerre.** Identification de bombardements, mouvements de population.

**Environnement.** Déforestation, pollutions, exploitations illégales.

**Investigation corporate.** Vérifier l'activité réelle d'un site industriel déclaré.

#### 50.10 Limites OSINT satellite

**Résolution.** 10m Sentinel : pas de détails fins.

**Couverture nuageuse.** Limite l'optique (sauf SAR).

**Latence.** Mises à jour pas toujours en temps réel.

**Coût haute résolution.** Maxar / Planet hors de portée du budget OSINT individuel.

**Analyse expertise.** Lire une image satellite demande expertise.

-----

### Chapitre 51 — GEOINT assisté par IA

#### 51.1 La rupture 2024-2026

L'**IA appliquée à la géolocalisation** a connu une rupture majeure en 2024-2026. Des outils comme **GeoSpy** (et son successeur **GeoSeer**) ont démontré la capacité d'agents IA à géolocaliser des photos à partir d'indices visuels avec une précision impressionnante — parfois meilleure qu'un analyste humain en temps record.

Cette rupture transforme la pratique GEOINT. L'analyste 2026 ne fait plus de géolocalisation purement manuelle : il **collabore avec des agents IA** spécialisés.

#### 51.2 GeoSpy et GeoSeer

**GeoSpy** (geospy.ai). Premier outil grand public, lancé en 2023, devenu très populaire.

**Capacités.**
- Upload de photo, retour de géolocalisation suggérée.
- Estimation de probabilité par région.
- Multi-suggestions hierarchized.

**Forces.**
- Rapide (résultat en secondes).
- Souvent précis sur monuments / scènes distinctives.
- Bon sur grandes villes occidentales.

**Limites.**
- Hallucinations possibles.
- Moins bon sur zones rurales / pays sous-représentés dans l'entraînement.
- Précision variable.

**GeoSeer**, **PicArta**, autres : alternatives concurrentes.

#### 51.3 Architecture multi-agents

Les outils 2026 utilisent souvent une **architecture multi-agents** :

- **Agent vision** : décrit l'image.
- **Agent géographique** : émet hypothèses régionales.
- **Agent cross-vérificateur** : confronte aux bases cartographiques.
- **Agent synthèse** : produit suggestion finale + confiance.

Cette architecture permet une **traçabilité** partielle : on peut voir quelles hypothèses ont été émises et lesquelles ont été éliminées.

#### 51.4 LLMs multimodaux : usage géolocalisation

**GPT-4V** (OpenAI), **Claude** (Anthropic), **Gemini** (Google). Tous peuvent recevoir une image et produire description + suggestions de localisation.

**Méthode.** Prompt structuré demandant : description méthodique, hypothèses de localisation, raisonnement.

**Exemple de prompt.**
```
Tu es un expert OSINT spécialisé en géolocalisation. Analyse cette image :
1. Inventorie les éléments visuels suggérant une localisation
2. Émets 3 hypothèses de localisation avec probabilité
3. Justifie ton raisonnement
4. Indique les vérifications à mener pour confirmer
```

#### 51.5 Limites et risques

**Hallucinations.** Un LLM peut inventer une localisation plausible mais fausse.

**Biais d'entraînement.** Surreprésentation de certaines régions.

**Confidentialité.** Upload d'image vers cloud (OpenAI, Anthropic, Google) = fuite d'intent OSINT.

**Sur-confiance.** L'analyste qui accepte la suggestion IA sans vérification produit du bruit.

#### 51.6 Workflow GEOINT augmenté

Le workflow recommandé 2026 :

1. **Lecture méthodique humaine** (Ch.48).
2. **Suggestion IA** (GeoSpy / LLM multimodal) — comme **hypothèse de départ**.
3. **Vérification manuelle** sur Google Maps / Street View / Mapillary.
4. **Triangulation** classique.
5. **Confirmation** ou rejet.

L'IA accélère ; elle ne remplace pas.

#### 51.7 OPSEC : upload d'images suspectes

**Si l'image est sensible**, ne pas l'uploader vers services cloud publics :
- Utiliser LLMs locaux (Ollama avec modèles multimodaux : LLaVA, Qwen-VL).
- GeoSpy a une version self-hosted limited.
- Préférer méthode manuelle pour très sensible.

#### 51.8 Reconnaissance de scène par IA

Au-delà de la géolocalisation, les LLMs multimodaux excellent à :
- **Identifier monuments** (Eiffel Tower, Sagrada Familia).
- **Identifier types d'architecture régionale**.
- **Reconnaître activités** (manifestation, marché).
- **Décrire** finement.

Tous à utiliser comme suggestions, à valider.

#### 51.9 Cas d'usage avancés

**Investigation de conflits.** Géolocalisation rapide de centaines de vidéos virales.

**Réfugiés et migrations.** Documentation de mouvements.

**Sites industriels.** Identification du contexte géographique d'une photo intérieure.

**Investigation criminelle.** Localisation d'images de crimes (kidnapping, traite humaine).

#### 51.10 Synthèse 2026

| Capacité | Outils | Niveau de confiance |
|---|---|---|
| Géoloc rapide tentative | GeoSpy | Hypothèse, à vérifier |
| Description fine image | GPT-4V / Claude / Gemini | À vérifier |
| Identification monuments | Google Lens + LLM | Souvent fiable |
| Géoloc rurale précise | Méthode manuelle Bellingcat | Standard |
| Confirmation | Google Maps / Street View / OSM | Fiable |

> **Principe 2026.** L'IA est devenue un copilote GEOINT puissant. Mais le pilote reste l'analyste humain qui valide chaque suggestion contre des sources cartographiques canoniques.

-----

### Chapitre 52 — OSINT maritime, aérien et transport

#### 52.1 Le transport comme terrain OSINT

Le **transport** (maritime, aérien, terrestre) est un terrain OSINT spécifique avec ses propres sources, outils et méthodes. Il intéresse :
- **Sanctions** : suivre les navires contournant les embargos.
- **Criminalité organisée** : trafics maritimes.
- **Journalisme** : enquêtes sur trafics, asset tracking.
- **Investigation corporate** : flotte d'une société.
- **Conflits** : mouvements d'armement.

#### 52.2 Maritime — AIS et MarineTraffic

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

#### 52.3 Investigation navire

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

#### 52.4 Pavillons et registres

**Registres principaux.**
- **Pavillon traditionnels** : Royaume-Uni, France, Allemagne, Norvège.
- **Pavillons de complaisance** : Panama, Libéria, Marshall Islands.
- **Pavillons à risque** : pavillons utilisés pour contourner sanctions (Iran, Russie, Corée du Nord récemment via diverses juridictions).

#### 52.5 Sanctions maritimes et dark fleet

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

#### 52.6 Aérien — ADS-B

**ADS-B** (Automatic Dependent Surveillance-Broadcast). Système d'identification aérienne. Émet position, vitesse, altitude, identité.

**Sources publiques ADS-B.**

**Flightradar24** (flightradar24.com). Populaire, freemium. Beaucoup d'aéronefs militaires masqués.

**ADS-B Exchange** (adsbexchange.com). **Référence OSINT** : ne filtre pas, montre tous les avions trackés (y compris militaires, présidentiels). Communauté de récepteurs amateurs.

**FlightAware**, **RadarBox**, **Plane Finder**. Alternatives.

#### 52.7 Investigation avion

**Pivots aérien.**

**Immatriculation.** Format pays-spécifique (F- France, N- US, D- Allemagne, G- UK). Identifiable visuellement.

**ICAO 24-bit code.** Identifiant technique unique.

**Tail number / registration.** Plaque sur l'aéronef.

**Outils complémentaires.**
- **planespotters.net** : photos d'aéronefs identifiés.
- **JetPhotos** : community photos.
- **Aviation Safety Network**.
- Registres nationaux : FAA (US), CAA (UK), DGAC (FR).

#### 52.8 Cas d'usage aérien

**Jets privés et oligarques.** Investigation des déplacements de personnalités via leurs jets privés. Communauté @JetTracker, @ElonJet (avant suspension X).

**Vols de renseignement / militaires.** Suivi des avions de reconnaissance OTAN, US, Russie via ADS-B Exchange.

**Itinéraires diplomatiques.** Déplacements d'avions gouvernementaux.

**Compagnies de fret.** Suivi de livraisons d'armement par avion-cargo.

#### 52.9 Terrestre — trains, camions, véhicules

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

#### 52.10 Cas d'usage transport

**Sanctions.** Suivi du contournement (tankers, fret).

**Criminalité organisée.** Trafics de stupéfiants (maritime, aérien notamment Caraïbes / Méditerranée).

**Conflits armés.** Mouvements d'armement.

**Enquête sur déplacements personnels (avec déontologie).** Limité par RGPD.

**Investigation corporate.** Flotte de transport d'une société (logistique, supply chain).

#### 52.11 Synthèse — boîte à outils transport

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
