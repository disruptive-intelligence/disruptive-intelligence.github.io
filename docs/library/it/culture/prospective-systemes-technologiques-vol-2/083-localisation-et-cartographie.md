---
title: ◆◆ Localisation et cartographie
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — percevoir, décider

**En une phrase.** Se situer précisément dans un environnement, et construire ou maintenir la représentation qui permet de le faire.

**Comment ça fonctionne — deux approches complémentaires.**

**La cartographie préétablie.** On relève au préalable l'environnement avec une précision élevée, et le véhicule s'y localise en comparant ce qu'il perçoit à cette carte. Précision excellente, mais **la carte doit être maintenue** : travaux, marquages effacés, signalisation modifiée. C'est un coût d'exploitation continu, et c'est ce qui limite l'extension géographique.

**La cartographie et localisation simultanées.** Le système construit sa carte en se déplaçant, tout en s'y localisant. Aucune préparation nécessaire, mais la position obtenue est relative et dérive — sauf recalage sur une référence externe.

**Ce qui bloque.** **Le coût de maintien de la carte**, qui croît avec la surface couverte et qui est le facteur limitant réel de l'extension. **La dérive** pour l'approche sans carte. **Les environnements peu texturés ou répétitifs**, où la localisation visuelle échoue — couloirs identiques, tunnels, champs.

**Ce que cela implique.** Le choix entre les deux approches est un arbitrage entre **coût de préparation** et **précision garantie**. C'est un cas où le verrou est logistique — qui relève la carte, à quelle fréquence, et qui paie — plutôt que technique.

**À ne pas confondre avec.** **Le positionnement par satellite** (ch. 6), qui donne une position absolue mais insuffisamment précise et indisponible en intérieur, en tunnel ou en environnement urbain dense.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Le maintien de cartographies fines à grande échelle reste un coût significatif et un frein à l'extension géographique.
> 🔄 **À revoir si** un système atteint des performances de localisation suffisantes sans cartographie préétablie dans un environnement urbain dense.

**Renvois** — Couche : percevoir, décider · Convergence : autonomie mobile (39).

---


## Clôture de la couche D — Agir


### Ce que les vingt et une entrées font apparaître

**Un. La difficulté suit l'environnement, pas la machine.** Le classement du chapitre 14 le rendait visible ; les chapitres 16 et 17 le confirment. Une même capacité — se déplacer, saisir, décider — change de difficulté d'un ordre de grandeur selon que l'environnement est préparé, semi-structuré, ouvert mais réservé, ou partagé avec des humains non prévenus. **C'est la variable dominante de toute la couche, et elle n'apparaît dans aucune fiche technique.**

**Deux. Le verrou est institutionnel dans huit entrées sur vingt et une.** Drones — autorisation du vol hors vue. Véhicules autonomes — démonstration de sûreté et assurabilité. Maritime — droit international. Aérien — certification. Ferroviaire — infrastructure et financement. Robotique médicale — preuve clinique et autorisation. Essaims — vérifiabilité du comportement. Autonomie supervisée — responsabilité. **Dans aucun de ces cas la capacité technique n'est le facteur limitant.**

**Trois. Le ratio d'opérateurs par machine est la grandeur économique cachée de la couche.** Elle apparaît en téléopération, en autonomie supervisée, en véhicules autonomes et en systèmes maritimes. Elle décide de la rentabilité de tout déploiement, et elle est presque jamais publiée. **Si une seule grandeur devait être surveillée dans ce domaine, ce serait celle-là.**

**Quatre. La défaillance silencieuse d'origine mécanique complète le relevé du volume.** Jeu de réducteur, usure de préhenseur, dérive de structure : trois formes d'une même chose — une machine précise selon ses capteurs et imprécise en réalité, parce que la déformation se situe en aval de la mesure.


### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **36 — Robotique généraliste** | robotique industrielle, robots mobiles, manipulation, locomotion, souple, humanoïde, actionneurs, mains, téléopération |
| **39 — Autonomie mobile** | drones, terrestres, maritimes, essaims, autonomie supervisée, véhicules autonomes, domaine d'emploi, autres modes, localisation |

**Neuf entrées pour chacun des deux dossiers.** La couche D est la plus directement mobilisée de l'atlas — et c'est la seule dont les entrées se répartissent presque exclusivement entre deux dossiers, sans dispersion.


### Vérification de la thèse du volume

Le dossier 39 mobilise neuf entrées de cette couche et dix de la couche *percevoir*, soit dix-neuf sur les trente-six entrées attendues par l'ensemble des dossiers. **Et son maillon en retard est ailleurs** : dans la démonstration de sûreté, qui relève de la couche *vérifier*.

Le dossier 36 mobilise neuf entrées de cette couche et huit de la couche *apprendre*. **Son maillon en retard est partagé** entre la fiabilité de la manipulation — couche *agir* — et les données physiques — couche *apprendre*. C'est la contradiction partielle relevée au squelette, et elle se confirme.

**Bilan intermédiaire : deux vérifications, une contradiction partielle.** La formulation affaiblie proposée au squelette tient.

---

---

---


### Couche E — Fabriquer

---
