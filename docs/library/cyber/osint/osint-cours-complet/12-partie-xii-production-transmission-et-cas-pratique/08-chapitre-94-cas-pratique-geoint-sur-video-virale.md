---
title: 'Chapitre 94 — Cas pratique : GEOINT sur vidéo virale'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 94.1 Présentation du cas

Une vidéo virale circule sur X et Telegram, montrant un convoi militaire dans un environnement non identifié. La vidéo est présentée comme « preuve d'incursion en territoire X ». L'analyste OSINT doit :

- Vérifier l'authenticité de la vidéo.
- Géolocaliser le lieu.
- Chronolocaliser la date de prise.
- Identifier les véhicules visibles.
- Évaluer la cohérence avec le narratif présenté.

## 94.2 Étape 1 — Préservation

**Action.** Download via `yt-dlp` (avec X) ou capture manuelle (Telegram).

```bash
yt-dlp https://x.com/[user]/status/[id]
```


**Préservation.** Hash SHA-256, capture HTML de la page de partage, conservation des métadonnées disponibles.

## 94.3 Étape 2 — Lecture méthodique

**Inventaire visuel.**

- Convoi de 6 véhicules militaires.
- Visibles : 2 chars (type à identifier), 3 véhicules de transport, 1 camion.
- Insignes au sol partiellement visibles.
- Paysage : terrain plat semi-aride, végétation rare, ligne d'horizon dégagée.
- Route asphaltée mais dégradée.
- Lampadaires de type est-européen.
- Ciel : ensoleillé, ombres modérées.
- Pas de panneaux routiers lisibles.

**Audio.** Bruits moteur + voix off en langue à identifier.

## 94.4 Étape 3 — Authenticité technique

**Détection IA.**

- Sensity AI : 12 % « likely real ».
- FakeCatcher : signal physiologique cohérent.
- Pas de signaux visuels d'IA générative (cohérence frame par frame).

**Recherche inversée des frames clés.** Yandex + Google Lens : aucune occurrence antérieure à la date de publication. Pas de recyclage d'ancienne vidéo identifié.

**Conclusion préliminaire.** Probable authenticité. Cotation B2 (cohérence technique, sans certificat C2PA).

## 94.5 Étape 4 — Identification des véhicules

**Chars.** Comparaison avec catalogues OSINT militaires : forme de la tourelle, position du canon, profil général.

**Hypothèses :**

- T-72B3 (Russie / soviétique).
- T-90 (Russie moderne).

**Affinement par détails.** Système de protection KMT-5/8 visible : compatible T-72B3 modernisé.

**Outils.**

- Janes Defense Equipment.
- Oryx Spioenkop (suivi pertes équipement Ukraine).
- ARES Database.

## 94.6 Étape 5 — Géolocalisation

**Indices.**

- Terrain semi-aride.
- Lampadaires est-européens.
- Climat compatible Europe de l'Est / Asie centrale.
- Pas de végétation tropicale.

**Hypothèses initiales.** Sud Ukraine, Crimée, Russie sud, Kazakhstan, Asie centrale.

**Triangulation visuelle.** Identification d'un détail : une pylône électrique distinctive avec configuration spécifique visible en arrière-plan, et une station-service abandonnée à droite.

**Recherche.** Google Earth sur les régions hypothétiques, à proximité de routes principales avec terrain plat semi-aride. Mapillary pour Street View communautaire.

**Hit.** Identification de la station-service abandonnée sur Google Earth (image satellite 2024) le long d'une route en Ukraine sud (région Kherson). Vérification : pylône électrique correspondant.

**Conclusion.** Géolocalisation : route P-58, Ukraine, oblast Kherson, secteur précis identifié (coordonnées GPS X,Y). Cotation : A1.

## 94.7 Étape 6 — Chronolocation

**Indices.**

- Saison : végétation sèche, vêtements légers visibles → été ou début automne.
- Ombres : modérées, soleil bas à droite → matin ou fin d'après-midi.

**Shadow analysis.** SunCalc sur coordonnées identifiées : ombres compatibles avec **10h30-11h30 heure locale**, période **juillet-août**.

**Cross-météo.** Wolfram Alpha sur région et période : pas de précipitation, ciel dégagé. Cohérent avec vidéo.

**Affinement.** Le compte X publie la vidéo le 18 août 2024. Cohérence : prise probable la veille ou jour même.

**Conclusion.** Date probable : entre le 15 et 18 août 2024, plage horaire 10h30-11h30. Cotation : B2.

## 94.8 Étape 7 — Cohérence avec narratif

**Narratif accompagnant.** « Convoi russe entrant en région X ».

**Vérification.**

- Géolocalisation Ukraine sud, oblast Kherson : zone effectivement contestée à cette période.
- Chars compatibles T-72B3 modernisés : équipement Russe utilisé sur ce théâtre.
- Insignes au sol : à examiner avec experts militaires.

**Cohérence.** Globalement compatible avec narratif. Mais subtilité : direction du convoi, identification des marquages spécifiques (régiment) demandent expertise militaire complémentaire.

## 94.9 Synthèse cas

**Conclusion globale.** La vidéo est probablement authentique (B2-A1 selon dimensions), géolocalisée en Ukraine sud (A1), datée août 2024 (B2). Le narratif d'accompagnement (convoi russe en région) est compatible avec les éléments observés, sans qu'une identification précise du régiment russe ou de la mission opérationnelle puisse être conduite en OSINT pur.

**Production.** Note courte (Ch.87) au commanditaire avec captures référencées, coordonnées GPS, hypothèses identifiées, limites mentionnées.

## 94.10 Pédagogie

Ce cas illustre :

- Authentification multi-couches (technique + recherche inversée + cohérence).
- Géolocalisation par méthode Bellingcat.
- Chronolocation par shadow analysis.
- Identification d'équipements (limites OSINT pur, expertise militaire).
- Honnêteté méthodologique sur les limites.

## 94.11 Variantes du cas

**Variante 1 — Vidéo recyclée d'un autre conflit.** L'analyse de recherche inversée révèle que la vidéo a déjà été publiée antérieurement dans un autre contexte. Manipulation : recyclage avec narratif trompeur. Cas fréquent sur réseaux sociaux après chaque crise.

**Variante 2 — Vidéo générée par IA.** Veo, Sora, Runway peuvent produire vidéos militaires plausibles. Détection : Sensity, Intel FakeCatcher, signaux visuels (cohérence physique des objets, fumée, mouvements).

**Variante 3 — Vidéo authentique mais hors contexte.** Vidéo réelle prise il y a 2 ans, présentée comme récente. Détection : chronolocation par shadow analysis + cross-référence événements.

**Variante 4 — Vidéo composite (morceaux assemblés).** Plusieurs vidéos authentiques montées pour créer narratif faux. Détection : analyse frame par frame, ruptures de continuité, EXIF résiduels.

## 94.12 Workflow GEOINT vidéo type

1. **Préservation** : yt-dlp, hash, capture page partage.
2. **Lecture méthodique** : inventaire visuels et audio.
3. **Authenticité technique** : EXIF, ELA frames clés, détection IA (Sensity, FakeCatcher).
4. **Recherche inversée** : frames clés sur Yandex / Google Lens / TinEye.
5. **Identification éléments** : véhicules, uniformes, signalétique.
6. **Géolocalisation** : triangulation Google Earth / OSM / Mapillary.
7. **Chronolocation** : shadow analysis + cross-météo + saison.
8. **Cohérence narratif** : confrontation au récit.
9. **Cotation et limites** : prudente, expertise complémentaire si pièce centrale.

## 94.13 Cas de référence Bellingcat

**MH17 (2014-2018).** Géolocalisation par Bellingcat de chaque étape du convoi BUK russe à travers Ukraine. Méthode reproductible documentée.

**Skripal (2018).** Identification des deux agents GRU par cross-recherche photos, voyages, identité.

**Khashoggi (2018-2019).** Reconstitution des mouvements de l'équipe saoudienne à Istanbul.

**Ukraine (2022-2026).** Volume massif de géolocalisations, suivi des conflits avec rigueur.

**Soudan (2023-2026).** Documentation des massacres et conflits via OSINT collaborative.

Ces cas constituent le **corpus pédagogique** de référence. Étude recommandée pour formation.

-----
