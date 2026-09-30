---
title: Chapitre 31 — Métadonnées et nettoyage de fichiers
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

## 31.1 Métadonnées : ce que c’est

Les métadonnées sont les données qui décrivent les données. Souvent invisibles, presque toujours révélatrices. Elles s’agrègent silencieusement à chaque création de fichier, à chaque modification, à chaque transmission. Plus dangereuses parce que sous-estimées.

## 31.2 EXIF photo et métadonnées image étendues

Standard EXIF (Exchangeable Image File Format), embarqué dans la plupart des formats image (JPEG, TIFF, certains RAW) :

- **Coordonnées GPS** (latitude, longitude, altitude, parfois cap et vitesse au moment de la prise).
- **Date et heure** de prise, avec fuseau horaire.
- **Modèle d’appareil** et numéro de série de l’appareil (sur certains modèles haut de gamme, c’est un identifiant unique par appareil — un signal forensique fort).
- **Paramètres techniques** (ouverture, ISO, focale, exposition, balance des blancs).
- **Orientation** physique au moment de la prise (capteur gyroscopique).

**Métadonnées image étendues, souvent négligées** :

- **Profil ICC personnalisé** : si tu utilises un écran calibré ou un workflow professionnel, le profil ICC embarqué peut identifier ton matériel ou ton studio.
- **Vignettes** : mini-images embarquées dans la version finale. Si tu retouches une photo (par exemple pour caviarder un visage), la vignette peut conserver la version originale non retouchée. Plusieurs scandales journalistiques ont reposé sur cette erreur. ExifTool peut extraire les vignettes avec `exiftool -b -ThumbnailImage`.
- **XMP** (Extensible Metadata Platform) : couche métadonnées étendue, utilisée par Adobe et autres. Peut contenir auteur, copyright, historique de modifications, mots-clés ajoutés par le logiciel de gestion (Lightroom, Photo Mechanic).
- **Maker Notes** : zone propriétaire dans laquelle chaque constructeur (Canon, Nikon, Sony, Apple, Samsung) stocke des informations supplémentaires. Sur iPhone, Apple stocke des données HEIC qui incluent parfois l’orientation gyroscopique fine.
- **CRS (Camera Raw Settings)** : pour les fichiers RAW retouchés, peut révéler la version du logiciel utilisé.

**Cas réel** : John McAfee en 2012 — photo prise par un journaliste de *Vice* avec son iPhone, EXIF GPS intact, révèle au monde la localisation au Guatemala. Arrestation suivie dans les jours. Cf. Annexe 8.6.

**Cas moins connu** : plusieurs analystes d’OSINT ont géolocalisé des reportages de guerre en croisant l’angle du soleil dans la photo avec l’horodatage EXIF — sans même besoin du GPS, à condition que le téléphone n’ait pas modifié l’horloge.

## 31.3 PDF

- **Auteur**, **Producteur** (logiciel), **Créateur** (logiciel d’export), **Mots-clés**, **Sujet**.
- **Historique de révisions** : versions précédentes embarquées si non purgées.
- **Objets cachés** : commentaires invisibles, annotations, formulaires masqués.
- **XMP** (Extensible Metadata Platform) : couche métadonnées additionnelle.
- **JavaScript embarqué** : si présent, exécutable à l’ouverture.

## 31.4 Office (DOCX, XLSX, PPTX)

- **Auteur** initial et dernier modificateur.
- **Date de création**, dernière modification, dernière impression.
- **Commentaires** et suivi des modifications, parfois conservés sans en avoir conscience.
- **Texte caché** (formatage en blanc, sections masquées).
- **Vignettes** des slides PPTX.

Office propose un « Inspecter le document » qui retire la plupart, mais pas tout. Vérifier toujours après nettoyage.

## 31.5 Audio / vidéo

- **Tags ID3** sur MP3 : artiste, album, paroles, image cover.
- **Métadonnées MP4/MOV** : géolocalisation pour vidéos téléphoniques, gyroscope, codecs.
- **Traces de montage** : marqueurs invisibles laissés par certains logiciels.
- **Gyroscope iPhone vidéo** : peut révéler modèle d’iPhone exact.

## 31.6 Yellow dots : tracking imprimantes

**Cas Reality Winner, 2017** : analyste NSA, fuite d’un document classifié au média The Intercept. Le document est scanné et publié. Sur l’impression : des **micro-points jaunes** quasi invisibles à l’œil nu, formant un code dérivé de la **machine spécifique**, **date** et **heure** d’impression. Le FBI remonte à l’imprimante de la NSA, à l’heure d’impression, à Reality Winner. Arrestation en quelques jours.

**Mécanisme** : la quasi-totalité des imprimantes couleur professionnelles intègrent depuis les années 2000 un système de marquage forensique. Les patterns varient selon le constructeur, mais le principe est universel. Non documenté par les constructeurs, mais documenté par EFF (« Machine Identification Code »).

**Défense** :

- Pour publication anonyme : ne pas imprimer.
- Si impression nécessaire : imprimer dans des lieux multiples non identifiables, ou utiliser des imprimantes sans MIC (rares).
- Pour transmission de document scanné : ré-imprimer après scan via une voie qui retire les artefacts (re-générer le PDF depuis le contenu, jamais re-scanner).

## 31.7 Outils de nettoyage

- **MAT2** : Metadata Anonymisation Toolkit v2 (Tails inclut). Multi-format, automatique. `mat2 fichier.jpg` nettoie en place.
- **ExifTool** : référence pour lire et écrire métadonnées. Plus puissant, plus complexe. `exiftool -all= fichier.jpg`.
- **« Inspecter le document »** (Word, PowerPoint, Excel) : intégré, bon mais incomplet.
- **Acrobat Pro « Suppression d’informations cachées »** : payant mais efficace sur PDF.

## 31.8 Dangerzone

Cf. Ch 16. Méthode différente : reconversion complète du PDF dans un conteneur isolé, qui produit un PDF *nettoyé par reconstruction*. Plus radical que MAT2 (qui retire les métadonnées sur le fichier existant) parce qu’il *recrée* le fichier à partir de l’image rendue. Aucun objet caché, aucun JavaScript, aucune révision n’y survit.

## 31.9 Zed!

Cf. Ch 12. Conteneur chiffré auto-extractible, secteur public francophone. Utile pour transmettre un dossier complet à un correspondant non technique en environnement français.

## 31.10 Redaction destructive vs masquage

Pour caviarder un nom dans un PDF :

- **Mauvaise méthode** : rectangle noir par-dessus le texte dans Acrobat → le texte est toujours là, sous le rectangle. Copier-coller révèle.
- **Bonne méthode** : redaction destructive (Acrobat Pro propose, ou re-générer le PDF depuis source). Le texte est physiquement supprimé.

**Cas réel** : documents Manning publiés par Le Monde et The Guardian — premières versions avec caviardage non destructif, noms révélés par copier-coller. Correctifs et leçons apprises depuis.

## 31.11 Workflow avant publication

1. Travailler dans un environnement isolé si document sensible.
1. Avant export final : passer par Dangerzone (PDF) ou MAT2 (autres formats).
1. Vérifier visuellement : ouvrir le résultat dans un visualiseur différent, examiner les métadonnées.
1. Tester copier-coller du contenu : ce qui ne devrait pas y être ne doit pas y être.
1. Vérifier les vignettes embarquées.
1. **Ne jamais publier directement depuis le logiciel de création**.

## 31.12 *Fil rouge* — Léa nettoie un PDF et découvre un nom

Léa s’apprête à publier un document de l’enquête. Avant publication, application du workflow :

- Ouverture du PDF dans ExifTool : champ XMP « Author » contient le nom de la source. Erreur d’export.
- Vérification visuelle : tout est OK sur l’image.
- Vérification métadonnées : `exiftool -all` → champ « Producer » indique « Microsoft Word 2019 - Bureau de [nom de la source dans son administration] ». Si publié, identifie la source.
- Action : reconstruction via Dangerzone, vérification, publication.

Sans cette étape, la source aurait pu être identifiée par n’importe quel lecteur attentif.

-----
