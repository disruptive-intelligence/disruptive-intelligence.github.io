---
title: Chapitre 47 — Analyse technique d'image
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 47.1 Au-delà de la lecture : la forensique d'image

Quand une image est suspecte ou critique pour une enquête, l'**analyse technique** (forensique d'image) peut révéler manipulations, retouches, incohérences invisibles à l'œil nu.

L'analyse technique ne remplace pas la lecture méthodique — elle la complète. Et elle a des **limites** : un faux bien fait peut résister à toutes les analyses classiques.

## 47.2 ExifTool : la pierre angulaire

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

## 47.3 ELA — Error Level Analysis

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

## 47.4 Clone detection

La **détection de clone** identifie les zones d'une image qui sont des copies internes (tampon de clone, copies pour masquer).

**Outils.**

- **Forensically** (clone detection).
- **JPEGsnoop**.

**Cas d'usage.** Une photo de foule où des manifestants ont été dupliqués pour amplifier l'apparence de masse.

## 47.5 Analyse de luminosité, gradient, bruit

D'autres analyses techniques :

**Luminance gradient.** Met en évidence les bordures et différences d'éclairage.

**Noise analysis.** Le bruit (grain) doit être cohérent dans toute l'image. Des zones avec un bruit différent suggèrent insertion.

**JPEG ghosts.** Compression JPEG répétée laisse des « fantômes ». L'analyse révèle si des zones ont été insérées depuis une source compressée différemment.

**Outils.** Forensically intègre la plupart.

## 47.6 Analyse spectrale

L'**analyse spectrale** examine les fréquences de l'image (transformée de Fourier).

**Cas d'usage avancé.** Détection de watermarks invisibles, de patterns d'IA, d'inserts subtils.

**Outils.**

- ImageMagick avec FFT.
- Python (scipy.fft).

## 47.7 Détection IA générée (Ch.30 et Ch.56 développent)

Outils spécifiques :

- **Hive Moderation**.
- **Optic AI or Not**.
- **Sensity AI**.
- **Intel FakeCatcher**.

À utiliser systématiquement sur images suspectes en 2026.

## 47.8 Vidéo : analyse frame par frame

Pour vidéos suspectes :

1. Extraction des frames clés (ffmpeg).
2. Analyse de chaque frame comme image.
3. Recherche d'incohérences entre frames consécutives.
4. Détection deepfake spécifique (Ch.56).

```bash
ffmpeg -i video.mp4 -vf "select=eq(pict_type\,I)" -vsync vfr frame_%04d.png
```


## 47.9 Limites de l'analyse technique

**Faux positifs.** Une image authentique peut « ELA suspect » pour raisons techniques (recompression réseau social).

**Faux négatifs.** Un faux sophistiqué peut résister.

**Course offensive/défensive.** Les outils de génération IA et les outils de détection évoluent en parallèle.

**Implication.** L'analyse technique est **un indice**, pas une preuve. Cotation prudente.

## 47.10 Méthodologie type

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
