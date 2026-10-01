---
title: Partager et évaluer le renseignement
source: Cyber/01 CTI & renseignement/Méthodes d'analyse/Modèles d'analyse de la menace.md
note: Modèles d'analyse de la menace
up:
- - Modèles d'analyse de la menace
  - index.md
---

## TLP

- **TLP:RED** : Réservé aux participants directs (yeux/oreilles uniquement). Pas de partage.
- **TLP:AMBER** : Partage limité au sein de l'organisation et avec les clients.
- **TLP:AMBER+STRICT** : Partage limité à l'organisation uniquement.
- **TLP:GREEN** : Partage avec la communauté (partenaires, secteur).
- **TLP:CLEAR** : Public (pas de restriction).


## L'évaluation de la confiance (Admiralty Code / NATO System)

En CTI, une info n'est jamais fiable à 100%. Tu dois ajouter comment noter tes sources.

- **Fiabilité de la source (A à F)** : De "A - Complètement fiable" à "F - Impossible à évaluer".
- **Crédibilité de l'information (1 à 6)** : De "1 - Confirmée par d'autres sources" à "6 - Impossible à évaluer".
- _Exemple :_ Une info classée **A1** est un fait avéré venant d'une source sûre. Une info **E5** est une rumeur improbable.


## Biais cognitif

|   |   |   |   |
|---|---|---|---|
|**Biais**|**Définition**|**Exemple**|**Contre-mesure**|
|**Biais de confirmation**|Chercher uniquement les preuves qui valident notre hypothèse de départ.|"Je suis sûr que c'est APT28, donc je cherche seulement des IP russes."|**ACH (Analysis of Competing Hypotheses) :** Essayer activement de prouver que son hypothèse est fausse.|
|**Biais de récence**|Donner plus d'importance aux informations reçues récemment.|"On a vu 3 attaques de ransomware hier, donc cette alerte est forcément un ransomware."|Regarder les statistiques historiques sur 12 mois.|
|**Effet de groupe**|S'aligner sur l'opinion de la majorité ou du chef sans critique.|"Si le Senior Analyst dit que c'est bénin, je ne vérifie pas."|Encourager l'avocat du diable ("Red Teaming" des idées).|
