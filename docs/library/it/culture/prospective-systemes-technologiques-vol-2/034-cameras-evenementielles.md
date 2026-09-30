---
title: ◆◆ Caméras événementielles
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Un capteur dont chaque pixel signale indépendamment un changement de luminosité, au lieu de produire des images entières à cadence fixe.

**Pourquoi on en parle.** Parce qu'il change la nature de la donnée produite : au lieu d'un flux d'images dont la plupart sont redondantes, on obtient un flux d'événements qui ne contient que ce qui bouge.

**Comment ça fonctionne.** Chaque pixel compare en permanence la luminosité qu'il reçoit à celle de son dernier signalement. Quand l'écart dépasse un seuil, il émet un événement horodaté. Il n'y a **ni image, ni cadence, ni temps de pose** — trois notions qui disparaissent.

**Ce que ça permet.** Une résolution temporelle très fine, de l'ordre de la microseconde · une dynamique très étendue, chaque pixel s'adaptant localement · un volume de données faible sur scène statique · une consommation réduite.

**Ce qui bloque.** **L'écosystème.** Les algorithmes, les jeux de données, les outils et les compétences ont tous été construits pour des images ; presque rien ne se transpose directement. C'est un cas typique du coût de sortie d'un standard dominant. S'y ajoutent le coût du capteur et l'absence d'information sur les zones immobiles.

**Ce que cela implique.** C'est une technologie qui gagne là où la cadence ou la dynamique sont le verrou — vibration, impact, scène très contrastée, mouvement rapide — et qui perd partout ailleurs, non pour des raisons physiques mais parce que l'écosystème n'existe pas.

**À ne pas confondre avec.** **Une caméra rapide**, qui produit beaucoup d'images ordinaires. Ici, il n'y a pas d'images du tout.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Capteurs disponibles commercialement, applications industrielles de niche établies, adoption générale limitée par l'écosystème logiciel.
> 🔄 **À revoir si** des modèles d'apprentissage traitant nativement des flux d'événements atteignent des performances comparables à celles obtenues sur images sur une tâche de référence.

**Renvois** — Couche : percevoir · Convergences : robotique généraliste (36), intelligence distribuée (38).

---


## ◆ Acoustique sous-marine

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Utiliser le son pour détecter, mesurer et communiquer sous l'eau, où les ondes électromagnétiques ne se propagent pratiquement pas.

**Où vous rencontrerez le terme.** Hydrographie · pêche · offshore et énergies marines · surveillance d'infrastructures sous-marines · robotique sous-marine · applications de défense.

**Ce qui bloque.** **La vitesse du son.** Environ mille cinq cents mètres par seconde, soit deux cent mille fois plus lent que la lumière : les délais de mesure et de communication se comptent en secondes, ce qui borne toute boucle de contrôle et toute coordination. S'y ajoutent la forte dépendance aux conditions du milieu — température, salinité, profondeur courbent les trajets — et un débit de communication très faible.

**À ne pas confondre avec.** **Le radar**, inutilisable sous l'eau, et **le lidar**, dont la portée y est de quelques dizaines de mètres au mieux.

> ⏱ **État au 23/08/2026** — 🏭 déployé, domaine mature. Progression du traitement et de l'autonomie des plateformes porteuses.
> 🔄 **À revoir si** un moyen de communication sous-marine à haut débit et longue portée devient disponible — ce qui lèverait la contrainte la plus structurante du domaine.

**Renvois** — Couche : percevoir · Convergence : autonomie mobile (39).

---

---
