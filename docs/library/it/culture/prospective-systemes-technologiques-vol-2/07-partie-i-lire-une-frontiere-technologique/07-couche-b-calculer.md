---
title: Couche b — Calculer
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

*Chapitres 8 à 10 — 15 entrées*

> ### La question
> **Comment exécute-t-on davantage d'opérations utiles pour une énergie et un coût donnés ?**
>
> ### Ce que la couche recouvre
> Accélérateurs spécialisés · assemblage et intégration des puces · hiérarchie mémoire · calcul en mémoire · photonique · neuromorphique et analogique · calcul quantique et sa correction d'erreur.
>
> ### La grande contrainte
> **Déplacer une donnée coûte plusieurs centaines de fois plus que la traiter, et cet écart s'est creusé.** Le calcul est devenu beaucoup moins cher ; le déplacement des données presque pas. Toute l'architecture des machines modernes découle de ce rapport, et toutes les approches alternatives de cette couche l'attaquent d'une manière ou d'une autre.
>
> ### La seconde contrainte, qui domine à l'échelle du système
> **Tout finit en chaleur.** Un calculateur transforme la quasi-totalité de son électricité en chaleur — le résultat d'un calcul ne pèse rien et n'emporte aucune énergie. La densité de puissance évacuable borne donc ce qu'on peut faire fonctionner simultanément, à l'échelle de la puce comme à celle du bâtiment.
>
> ### Dépend de
> Semi-conducteurs, matériaux, énergie, refroidissement, chaînes d'approvisionnement très concentrées.
>
> ### Permet
> Tout le reste. C'est, avec l'énergie, la couche la plus en amont de l'atlas.
>
> ### ⏱ Ce qui a le plus bougé en cinq ans
> L'assemblage avancé et l'intégration en trois dimensions, devenus le principal levier de performance. La bande passante mémoire, désormais reconnue comme le goulet dominant de l'inférence. L'arrivée à maturité industrielle de l'optique co-packagée. Et la formulation d'objectifs chiffrés en qubits logiques plutôt qu'en qubits physiques.
>
> ### 🧱 Ce qui n'a pas bougé
> La hiérarchie mémoire et ses raisons d'être. Le coût énergétique d'un accès à une mémoire externe. Le fait que la précision analogique n'est pas reproductible d'un exemplaire à l'autre. Et le coût de sortir de l'écosystème dominant — outils, chaînes, compétences, base installée — qui exige qu'une alternative soit meilleure d'un facteur, pas de quelques pourcents.
>
> ### 🎯 Le piège de lecture dominant
> **Confondre un progrès sur un benchmark avec un progrès du système complet.** Une puce deux fois plus rapide ne produit pas un système deux fois plus rapide si le goulet est ailleurs — dans la mémoire, dans le refroidissement, ou dans le raccordement électrique du bâtiment. Devant toute annonce de performance, demandez sur quelle grandeur elle porte et laquelle limite réellement.

🖼 **SCHÉMA — la chaîne de goulets du calcul.** Six étages empilés : capacité par puce, accès mémoire, énergie et densité de puissance, évacuation thermique, raccordement électrique, délais de fabrication des équipements de réseau. Griser les étages franchis, marquer l'étage dominant. Légende : *améliorer un étage ne change rien tant qu'un étage inférieur borne.*

---
