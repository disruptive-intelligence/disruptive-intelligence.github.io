---
title: Couche d — Agir
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

*Chapitres 14 à 17 — 21 entrées*

> ### La question
> **Comment une machine modifie-t-elle le monde physique de façon contrôlée, répétable et sûre ?**
>
> ### Ce que la couche recouvre
> Robotique industrielle et mobile · manipulation et préhension · locomotion · humanoïdes · actionneurs · téléopération · systèmes sans équipage aériens, terrestres et maritimes · essaims · mobilité autonome.
>
> ### La grande contrainte
> **Un système mobile emporte son énergie, et cette énergie a une masse qu'il faut déplacer.** Ajouter de la capacité ajoute de la masse ; déplacer cette masse consomme de l'énergie ; il en faut donc davantage. Le gain d'autonomie est moins que proportionnel, et il existe un point au-delà duquel ajouter de la batterie n'apporte presque plus rien. Cette boucle borne toute la couche.
>
> ### La seconde contrainte, la plus sous-estimée
> **Manipuler est structurellement plus difficile que se déplacer.** Le contact change brutalement la dynamique ; il faut contrôler des forces et non seulement des positions ; les objets diffèrent alors qu'ils se ressemblent ; et certaines erreurs sont irréversibles. Le verrou de cette couche n'est pas la perception.
>
> ### Dépend de
> Percevoir, apprendre et décider, alimenter — et de matériaux, de mécanique de précision, d'électronique de puissance.
>
> ### Permet
> Automatisation physique, inspection, logistique, agriculture, chirurgie, exploration, présence en environnement inaccessible.
>
> ### ⏱ Ce qui a le plus bougé en cinq ans
> Le coût et la disponibilité des plateformes, notamment aériennes et quadrupèdes. La collecte massive de données de démonstration par téléopération. L'arrivée d'architectures d'apprentissage reliant directement perception et commande. Et l'entrée en service de flottes de véhicules autonomes payants dans un petit nombre de villes.
>
> ### 🧱 Ce qui n'a pas bougé
> La densité de puissance des actionneurs. Le compromis entre couple, vitesse et précision. Le jeu mécanique qui apparaît avec l'usure et qui rend un système imprécis alors que ses capteurs le disent précis. Et **l'écart entre une démonstration réussie et une fiabilité exploitable**, qui reste de plusieurs ordres de grandeur.
>
> ### 🎯 Le piège de lecture dominant
> **Confondre démonstration contrôlée et autonomie générale.** C'est la couche où les démonstrations sont les plus spectaculaires et les moins informatives. Cinq questions les remettent à leur place : combien de prises, à quelle vitesse de lecture, dans quel environnement, avec quelle part de téléopération, et que se passe-t-il quand ça rate.

🖼 **SCHÉMA — carte de la couche agir.** Une boucle fermée à quatre nœuds — percevoir, décider, actionner, se maintenir — avec les entrées de la couche disposées sur le nœud qu'elles servent. Marquer d'un trait épais le segment *actionner → se maintenir*, qui porte le verrou dominant : la fiabilité en environnement non structuré. En bas, deux échelles parallèles et décalées : *taux de succès en démonstration* et *taux de succès exploitable*, séparées de plusieurs ordres de grandeur. Légende : *c'est l'écart entre les deux échelles qui décide, pas la position sur la première.*

---
