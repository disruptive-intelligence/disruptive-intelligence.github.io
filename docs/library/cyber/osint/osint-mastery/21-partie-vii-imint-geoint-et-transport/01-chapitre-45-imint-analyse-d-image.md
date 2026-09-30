---
title: 'Chapitre 45 — IMINT : analyse d''image'
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 45.1 IMINT en sources ouvertes : la discipline

L'**IMINT** (Image Intelligence) en sources ouvertes est l'une des sous-disciplines les plus matures de l'OSINT contemporaine. Bellingcat a démontré dès 2014 que des amateurs formés pouvaient produire du renseignement IMINT de qualité (enquête MH17, Skripal, conflits divers).

Une analyse d'image OSINT mature combine cinq étapes : **lecture** (que voit-on ?), **vérification de source** (d'où vient l'image ?), **vérification d'authenticité** (est-elle modifiée ?), **contextualisation** (où ? quand ? quoi ?), **corroboration** (autres sources confirment-elles ?).

## 45.2 Lecture d'image méthodique

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

## 45.3 Métadonnées EXIF (rappel)

Voir Ch.29 pour les métadonnées EXIF en détail.

**Pour IMINT.**

- GPS si présent → géolocalisation directe.
- Date / heure → datation.
- Appareil → corrélation cross-photos.
- Logiciel de retouche → détection de manipulation.

**Limite 2026.** Plateformes sociales suppriment EXIF à l'upload. Donc EXIF utile principalement pour fichiers transmis directement, pris du téléphone, ou téléchargés de sites brut.

## 45.4 Pivots IMINT

Une image peut servir de sélecteur pour multiples pivots.

**Pivot visage** : reconnaissance faciale (Ch.30).

**Pivot lieu** : recherche inversée localise lieu, GEOINT confirme.

**Pivot objet** : un objet rare visible peut être identifié (modèle de voiture précis, logo d'entreprise, uniforme militaire).

**Pivot scène** : un contexte (manifestation, événement) identifié.

**Pivot timestamp** : datation précise via éléments visuels.

**Pivot infrastructure visuelle** : type de signalétique révèle pays (signalisation routière diffère par pays).

## 45.5 Outils de lecture assistée

**Google Lens.** Identifier objets, lieux, textes dans l'image. Souvent surprenant.

**Bing Visual Search.** Alternative.

**Yandex Images.** Reverse + identification souvent supérieure pour scènes.

**LLMs multimodaux (Claude, GPT-4V, Gemini)**. En 2026, les LLMs peuvent décrire une image en détail, identifier des éléments. **Avec vérification** : leur identification est sujette à hallucinations.

## 45.6 Composition technique d'une image

**Résolution.** Image 4K vs 480p révèle source (téléphone récent vs vieille caméra de surveillance).

**Compression.** JPEG répété dégrade : si une image est manifestement très compressée, elle a été partagée de nombreuses fois.

**Rapport d'aspect.** 16:9 (cinéma), 4:3 (TV ancienne), 9:16 (téléphone vertical), 1:1 (Instagram classique).

**Noise et grain.** ISO élevé en condition basse lumière, qualité d'optique.

## 45.7 Authenticité préliminaire

Avant analyse approfondie, signaux rapides d'authenticité.

**Signaux suspects.**

- Mains, doigts, oreilles, dents anormaux → IA générée (Ch.53).
- Ombres incohérentes → composite ou manipulation.
- Pixellisation locale → masquage / inserts.
- Cohérence physique des objets, gravité.

## 45.8 Cas particulier des screenshots

Un **screenshot** (capture d'écran) est un type d'image fréquent en OSINT.

**Authenticité.**

- Vérifier la cohérence d'interface (bonne version de l'app, date affichée plausible).
- Vérifier polices, éléments d'UI (vrais ou refaits ?).
- Recherche inversée pour autres apparitions.

**Limites.** Un screenshot est aisément fabricable. Cotation prudente, corroboration recommandée.

## 45.9 Workflow analyse d'image type

1. **Capture et préservation** : SingleFile, hash, EXIF préservé si possible.
2. **Lecture méthodique** : éléments identifiés.
3. **Métadonnées EXIF** : ExifTool.
4. **Recherche inversée** (Ch.46).
5. **Analyse technique** (Ch.47).
6. **Géolocalisation** (Ch.48).
7. **Chronolocation** (Ch.49).
8. **Synthèse cotée**.

## 45.10 Pièges classiques

- **Confiance excessive en EXIF** : peut être falsifié.
- **Saut à conclusion** : un détail mal interprété produit hypothèse erronée.
- **Biais culturel** : un Occidental lit mal une scène asiatique faute de référentiel.
- **Image hors contexte** : prêchant des conclusions à partir d'un cadrage restreint.
- **Confiance LLM** : une description LLM hallucinée acceptée comme analyse.

> **Principe IMINT.** Lire avant de conclure. Une image qui semble révéler X mérite la même rigueur qu'un témoignage oral : examen méthodique, corroboration, cotation.

-----
