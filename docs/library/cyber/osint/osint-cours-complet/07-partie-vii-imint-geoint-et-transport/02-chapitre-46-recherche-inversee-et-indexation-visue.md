---
title: Chapitre 46 — Recherche inversée et indexation visuelle
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 46.1 La recherche inversée : technique pivot

La **recherche inversée d'image** prend une image en entrée et retourne ses autres occurrences sur le web. C'est l'un des outils les plus puissants de l'IMINT moderne.

Usages :

- Identifier la source originelle d'une image (provenance).
- Détecter le recyclage d'une image dans un contexte trompeur.
- Géolocaliser via lieux identifiés ailleurs.
- Reconnaître personnes, objets, scènes.
- Vérifier l'authenticité (une « photo récente d'un événement » identifiée comme une photo de 2018 = manipulation).

## 46.2 Yandex Images : référence 2026

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

## 46.3 Google Lens et Google Images

**Google Lens** (lens.google.com). L'outil unifié Google. Identification d'objets, lieux, textes. Reverse image search.

**Google Images reverse.** Plus traditionnel, accessible via images.google.com.

**Comparaison.** Lens est plus puissant pour identifier (objets, monuments, plantes). Google Images reverse est plus exhaustif pour pages contenant l'image. Yandex souvent meilleur globalement.

## 46.4 TinEye

**TinEye** (tineye.com) est l'un des plus anciens moteurs de recherche inversée.

**Forces.**

- Excellent pour identifier l'occurrence la plus ancienne d'une image (« first seen »).
- Permet de tracer la chronologie de diffusion.
- Plugin navigateur.

**Limites.** Couverture moins exhaustive que Yandex/Google sur volumes contemporains.

## 46.5 Bing Visual Search

**Bing Visual Search** propose des fonctionnalités similaires à Google Lens, avec différences d'indexation.

**Forces.**

- Couverture Microsoft / Asie souvent meilleure.
- Bonne reconnaissance d'objets, marques.

## 46.6 Méthode multi-moteurs systématique

**Principe 2026.** Toute image importante est testée sur **au moins 3-4 moteurs** :

1. Yandex Images.
2. Google Lens.
3. TinEye.
4. Bing Visual Search.

Les résultats sont **différents**. Aucun moteur n'indexe tout. La combinaison maximise la couverture.

## 46.7 Recherche par visage versus par scène

**Recherche par visage.** PimEyes, FaceCheck (Ch.30). Spécialisée.

**Recherche par scène.** Yandex, Google Lens. Reconnaît bâtiments, paysages.

**Recherche par objet.** Google Lens excellent (téléphone modèle, voiture modèle, produits commerciaux).

**Adapter le moteur au besoin.**

## 46.8 Techniques d'amélioration

**Recadrage.** Si l'image entière ne retourne rien, recadrer une partie distinctive (visage, monument, objet rare).

**Variantes.** Tester avec et sans retouche, en versions colorisées vs N&B, à différentes résolutions.

**Filtres.** Filtrer par date, taille, type de page.

**Outils complémentaires.** RevEye (extension), Search by Image (extension multi-moteurs).

## 46.9 Limites d'indexation

**Ce qui n'est pas indexé.**

- Contenus derrière login (réseaux sociaux privés).
- Documents PDFs (parfois).
- Images dans contextes éphémères (stories supprimées).
- Sites avec robots.txt restrictif.
- Dark web.

**Implication.** Une absence de résultats ne prouve pas que l'image est « originale ». Elle peut être dans des espaces non indexés.

## 46.10 Synthèse — workflow recherche inversée

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
