---
title: Chapitre 29 — Documents, métadonnées et traces indirectes
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 29.1 Les documents comme sélecteurs

Au-delà des sélecteurs personnels, les **documents publiés** (PDF, Word, Excel, présentations, images) contiennent fréquemment des traces exploitables : métadonnées d'auteur, chemins de fichier, versions, données EXIF. Le « document » devient un sélecteur secondaire majeur.

L'extraction de métadonnées est l'un des classiques de l'OSINT, mature et bien outillée.

## 29.2 Métadonnées PDF

Un PDF contient typiquement :

- **Auteur** (champ `Author`).
- **Logiciel de création** (`Creator`, `Producer`).
- **Date de création** et **modification**.
- **Titre**, **sujet**, **mots-clés**.
- Parfois : **chemins absolus** (« C:\Users\Marc.Delaunay\Documents\... »).

**Outils.**

- **ExifTool** (Phil Harvey) : standard de fait, CLI, multi-formats.
- **pdfinfo** (Poppler) : Linux/Mac.
- **pdfmetadata online**.
- Adobe Acrobat Pro : interface graphique.

```bash
exiftool document.pdf
# Sortie typique
File Name        : document.pdf
Author           : Marc Delaunay
Creator          : Microsoft® Word 2019
Producer         : Microsoft® Word 2019
Create Date      : 2025:03:14 09:42:18+01:00
Modify Date      : 2025:03:14 09:42:18+01:00
Title            : Rapport préliminaire Delta
```


**Pivot.** L'auteur peut révéler une identité. Le chemin peut révéler une structure d'organisation. La date peut situer un événement.

## 29.3 Métadonnées Office (Word, Excel, PowerPoint)

Office documents (.docx, .xlsx, .pptx) sont des archives ZIP. À l'intérieur, plusieurs fichiers XML contiennent des métadonnées riches.

**Métadonnées typiques.**

- Auteur (`dc:creator`).
- Dernier modificateur (`cp:lastModifiedBy`).
- Historique de versions.
- Macros (si présentes — attention sécurité).
- Liens externes (images, données).

**Méthode rapide.** Renommer en .zip, extraire `docProps/core.xml` et `docProps/app.xml`.

**Outil dédié.** **oxml** ou simplement `unzip` + lecture XML.

## 29.4 Métadonnées images : EXIF

Les **métadonnées EXIF** des photos sont l'un des sélecteurs OSINT les plus puissants quand préservées.

**EXIF typique.**

- Modèle d'appareil (iPhone 15 Pro, Canon EOS R5).
- Date et heure de prise.
- **Coordonnées GPS** (latitude, longitude, altitude).
- Paramètres techniques (ouverture, ISO, focale).
- Logiciel de retouche.
- Auteur si renseigné.
- Hash de l'image.

**Outils.**

- **ExifTool** (universel).
- **Jeffrey's Image Metadata Viewer** (en ligne).
- **Metapicz**.

**Pivot.** GPS → géolocalisation précise. Date/heure → chronolocation. Appareil → corrélation cross-photos.

**Limite 2026.** Les plateformes sociales (Facebook, Instagram, Twitter) **suppriment** systématiquement les EXIF sensibles à l'upload. Donc EXIF utile principalement pour :

- Documents PDF/Office (non strippés).
- Photos téléchargées d'un site direct (blog, site institutionnel).
- Fichiers transmis par email.
- Photos issues d'un téléphone et partagées via service brut.

## 29.5 Stripping EXIF côté investigateur

À l'inverse, l'investigateur doit **stripper systématiquement** les EXIF des captures qu'il transmet (sauf si pertinent pour preuve).

```bash
exiftool -all= image.jpg
# supprime toutes les métadonnées
```


Une capture transmise à un client avec les EXIF de votre téléphone est une fuite OPSEC.

## 29.6 Chemins absolus et noms de machine

Certains documents PDF/Office contiennent des **chemins absolus** indiquant la machine d'origine.

**Exemples révélateurs.**

- `C:\Users\Marc.Delaunay\Documents\...` → confirme l'auteur Windows.
- `/Users/m.delaunay/Desktop/...` → confirme l'auteur Mac.
- `C:\Users\jdoe\AppData\...\Word\...` → révèle un éventuel ghost writer.
- Path UNC `\\fileserver01\projets\...` → révèle l'infrastructure interne.

Ces traces sont **précieuses** pour confirmer identité, organisation, infrastructure.

## 29.7 Métadonnées des présentations

Les présentations PowerPoint / Keynote peuvent contenir :

- Auteurs successifs (multiple `lastModifiedBy`).
- Notes de présentateur cachées.
- Images intégrées avec leurs EXIF.
- Liens vers des fichiers externes (révèlent structure).

## 29.8 Documents publiés en ligne : pivots

Les documents publiés par une organisation (rapports annuels, communiqués, notices techniques) sont riches en métadonnées.

**Méthode MIRAGE.** Télécharger tous les PDFs publics de TechnoVert (rapports, communiqués, notices), extraire les métadonnées en masse :

```bash
exiftool -r *.pdf > metadata.txt
```


Identifier les auteurs récurrents : Marc Delaunay, Sophie Martin (DRH), Pierre Dubois (DG). Cohérence avec les sources publiques.

## 29.9 Watermarks invisibles et traces

Certaines organisations apposent des **watermarks invisibles** sur leurs documents : identifiant du destinataire, date d'export, etc. Détectables avec outils spécialisés.

**Cas d'usage.** Un leak interne contient un watermark unique → identification du leaker possible (côté défense).

## 29.10 OCR pour documents scannés

Beaucoup de documents publics sont des PDFs scannés non textualisés (annonces légales anciennes, jugements). L'**OCR** rend exploitable.

**Outils.**

- **Tesseract** (open source).
- **Adobe Acrobat OCR** (commercial).
- **ABBYY FineReader** (commercial, qualité supérieure).
- **OCR.space API**.

**Cas d'usage.** Recherche par mot-clé dans archives BODACC anciennes scannées.

## 29.11 Synthèse — workflow document

| Étape | Action |
|---|---|
| Collecte | Télécharger document depuis source officielle |
| Hash | SHA-256, consigné dans journal |
| Métadonnées | ExifTool, capture des champs auteur/dates/chemins |
| OCR | Si scanné, textualisation Tesseract |
| Pivot | Auteur, organisation, infrastructure révélée |
| Strip | Si transmission, supprimer EXIF pertinents |

-----
