---
title: Couche C — Apprendre et décider
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

*Chapitres 11 à 13 — 18 entrées*

> ### La question
> **Comment produire un comportement utile pour une tâche que personne ne sait spécifier ?**
>
> ### Ce que la couche recouvre
> Modèles de fondation · raisonnement · mémoire et contexte · modèles compacts · agents et systèmes multi-agents · autonomie logicielle · modèles du monde · architectures reliant perception, langage et action · apprentissage par imitation et par renforcement · transfert de la simulation au réel.
>
> ### La grande contrainte
> **L'apprentissage échange de la certitude contre de la capacité.** On obtient un comportement sur des tâches qu'on ne savait pas décrire ; on perd la possibilité de démontrer ce que le système fera. On peut mesurer sa performance sur un échantillon ; on ne peut pas prouver son comportement sur une entrée non testée. Tout ce qui suit dans cette couche découle de cet échange.
>
> ### La contrainte physique de la couche
> Le déplacement des données. À l'inférence, ce n'est pas la puissance de calcul qui limite le plus souvent, mais la bande passante mémoire — ce qui explique le mouvement vers l'exécution locale et vers les modèles compacts.
>
> ### Dépend de
> Calcul, énergie, données, et de compétences rares.
>
> ### Permet
> Perception interprétée, décision, action autonome, découverte scientifique assistée, conception générative.
>
> ### ⏱ Ce qui a le plus bougé en cinq ans
> Le passage du modèle unique au système composé d'appels, d'outils et de mémoire externe. L'allocation de calcul au moment de l'inférence plutôt qu'au seul entraînement. L'apparition d'architectures reliant directement observation, instruction et commande motrice. Et l'exécution locale devenue possible sur des appareils ordinaires.
>
> ### 🧱 Ce qui n'a pas bougé
> **Hors de sa distribution d'entraînement, un modèle produit une sortie plausible sans que rien n'alerte.** C'est le même mode de défaillance qu'un capteur dérivé, et aucune des avancées de la période ne l'a supprimé. N'ont pas bougé non plus : la dépendance à la qualité des données, le coût quadratique de la mise en relation d'éléments dans une séquence, et l'absence de garantie démontrable.
>
> ### 🎯 Le piège de lecture dominant
> **Confondre une capacité démontrée sur une tâche avec une capacité générale.** Un système excellent sur une distribution de cas peut être inutilisable sur une autre, et l'écart n'est visible que si quelqu'un a construit un jeu de contrôle. Devant tout score, demandez sur quelle distribution — et ce qui garantit que le système ne l'a pas déjà vue.

🖼 **SCHÉMA — carte de la couche apprendre et décider.** Trois bandes horizontales superposées : *ce qu'on sait spécifier* (règles, contrôle classique), *ce qu'on apprend* (modèles de fondation, imitation, renforcement), *ce qu'on ne sait ni spécifier ni démontrer* (comportement hors distribution). Placer les entrées de la couche dans la bande correspondante. À droite, un axe vertical unique : *certitude démontrable*, décroissant de haut en bas. Légende : *on descend cet axe pour gagner de la capacité ; c'est un échange, pas un progrès gratuit.*

---
