---
title: Chapitre 30 — Reconnaissance faciale et image-to-person
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 30.1 Une technologie puissante et controversée

La **reconnaissance faciale** est l'une des technologies OSINT les plus puissantes et **les plus encadrées** en 2026. L'AI Act européen restreint son usage privé. Le RGPD la classe comme donnée biométrique sensible. Plusieurs juridictions interdisent ou limitent ses outils commerciaux.

L'analyste OSINT doit maîtriser la technique tout en respectant un cadre légal strict.

## 30.2 Comment ça fonctionne

La reconnaissance faciale convertit un visage en **vecteur biométrique** (embedding) — une représentation numérique des caractéristiques faciales. Comparer deux visages = comparer leurs vecteurs.

Les outils OSINT de reconnaissance faciale fonctionnent en :

1. Indexant des milliards de photos du web public.
2. Extrayant les vecteurs faciaux.
3. Permettant une recherche : photo query → photos similaires dans l'index.

## 30.3 PimEyes : le standard controversé

**PimEyes** (pimeyes.com) est l'outil de reconnaissance faciale le plus connu.

**Capacités.**

- Indexation massive du web public.
- Recherche par photo.
- Identification de visages dans des photos, articles, blogs.

**Restrictions.**

- Tarification payante ($14.99-$299/mois).
- AI Act et RGPD : usage restreint en UE.
- PimEyes a introduit un système d'opt-out pour les personnes (à demande).

**Précautions OSINT.**

- Usage strictement professionnel et documenté.
- Base légale RGPD requise (intérêt légitime documenté).
- Pas de recherche « pour curiosité ».
- Documentation des résultats dans le journal.

## 30.4 FaceCheck.ID et alternatives

**FaceCheck.ID** : outil concurrent, indexation différente. Parfois meilleur pour certaines populations géographiques.

**Search4Faces, FindClone** : moteurs russes, couverture forte pour la CEI.

**Clearview AI** : usage réservé aux LEA, non accessible au privé.

**Yandex Images** : reverse image incluant recherche faciale fonctionnelle (sans biométrie explicite).

**Google Lens** : recherche par image, parfois identifie des personnalités publiques.

## 30.5 Limites de la reconnaissance faciale

**Faux positifs.**

- Photos à basse qualité ou angle défavorable génèrent des matches fragiles.
- Jumeaux ou ressemblances fortes peuvent confondre.
- Maquillage, vieillissement, lunettes peuvent perturber.

**Faux négatifs.**

- Photos très anciennes peuvent ne pas matcher avec photos récentes.
- Pose extrême peut empêcher reconnaissance.

**Biais.**

- Les modèles sont historiquement moins performants sur certaines populations (visages noirs, asiatiques, féminins) — biais d'entraînement documentés.
- L'analyste doit en tenir compte dans la cotation de ses résultats.

## 30.6 Méthodologie : règles de prudence

**Règle 1 — Faux positifs.** Un match unique sur PimEyes n'est **jamais** une identification définitive. Cotation maximum « hypothèse à corroborer ».

**Règle 2 — Corroboration multi-sources.** Un match doit être confirmé par cross-recherche (nom retrouvé sur source citée, profil correspondant, etc.).

**Règle 3 — Pas de conclusion « C'est elle/lui ».** Formulation : « la recherche faciale a renvoyé une correspondance avec X, à confirmer par cross-vérification… ».

**Règle 4 — Pas pour identifier des inconnus.** L'usage est pour confirmer/contextualiser une identité **déjà supposée**, pas pour partir de zéro sur un inconnu.

**Règle 5 — Documentation rigoureuse.** Captures de recherche horodatées, hashes, sources.

## 30.7 Photos générées par IA : nouveau défi

En 2026, les photos générées par IA (StyleGAN, Stable Diffusion, Midjourney, Flux) sont **omniprésentes** sur les réseaux sociaux. Un avatar peut être un visage 100 % synthétique.

**Détection.**

- **Hive Moderation** : score « AI-generated ».
- **Sensity AI** : détection de deepfakes.
- **Optic AI or Not** : interface simple.
- **Intel FakeCatcher** : analyse physiologique.

**Signaux visuels.**

- Asymétries faciales subtiles.
- Pupilles incohérentes (StyleGAN classique).
- Mains, oreilles, dents souvent défectueuses.
- Arrière-plan flou ou incohérent.
- Cheveux qui « fondent » au niveau du contour.

**Implication.** Avant toute recherche faciale, vérifier si la photo source n'est pas synthétique. Une recherche sur une photo IA produit du bruit.

## 30.8 Image-to-person : workflow complet

Pour identifier une personne à partir d'une photo :

1. **Vérification authenticité.** Hive Moderation, ELA, recherche inversée pour origine.
2. **Recherche inversée multi-moteurs.** Yandex (en priorité), Google Lens, TinEye, Bing Visual.
3. **Recherche faciale dédiée.** PimEyes, FaceCheck (si cadre légal OK).
4. **Cross-recherche des hits.** Vérifier les pages mentionnant la photo : nom, contexte, cohérence.
5. **Corroboration multi-sources.** Pas de conclusion sur un seul hit.
6. **Documentation.** Captures, sources, cotation prudente.

## 30.9 Limites légales en UE

L'**AI Act** classe la reconnaissance faciale comme **risque élevé** voire **inacceptable** selon usage.

**Inacceptable (interdit).** Identification biométrique en temps réel dans l'espace public (sauf exceptions strictes terrorisme).

**Risque élevé.** Identification biométrique différée. Soumis à conformité stricte.

**Pour OSINT privé.** Zone grise. L'usage de PimEyes pour due diligence est généralement toléré mais doit reposer sur une base légale claire (intérêt légitime documenté).

**Recommandation.** Documenter explicitement dans le SOR la finalité, la base légale, la proportionnalité. En cas de doute, consulter un avocat.

## 30.10 Synthèse — usage prudent en 2026

| Cas | Recommandation |
|---|---|
| Confirmer une identité déjà supposée | OK avec corroboration |
| Identifier un inconnu à partir d'une photo | À éviter sauf cadre LEA |
| Verification photo profil = vraie personne | OK |
| Recherche dans cadre de stalking suspect | Refus mandat |
| Photo source potentiellement IA | Vérifier authenticité d'abord |
| Documentation | Toujours : capture, source, cotation prudente |

-----
