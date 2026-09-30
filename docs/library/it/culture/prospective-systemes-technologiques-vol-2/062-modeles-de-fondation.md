---
title: ◆◆◆ Modèles de fondation
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — plateforme · **Couche** — apprendre et décider

**En une phrase.** Un modèle entraîné à très grande échelle sur des données larges, destiné à être adapté à de nombreuses tâches plutôt qu'à une seule.

**Pourquoi on en parle.** Parce que c'est l'objet autour duquel s'est réorganisée toute une industrie — et parce que le terme désigne simultanément une manière d'entraîner et un rapport de dépendance.

**Comment ça fonctionne.** L'entraînement se fait en deux temps. Une phase de **pré-entraînement** expose le modèle à un très grand volume de données avec un objectif simple — prédire ce qui manque —, ce qui lui fait acquérir des régularités générales. Une phase d'**adaptation** l'oriente ensuite vers des usages, par apprentissage supervisé sur des exemples choisis puis par ajustement sur des préférences exprimées.

**Ce qui a rendu cette approche dominante** est une observation empirique : la performance s'améliore de façon régulière quand on augmente conjointement la taille du modèle, le volume de données et la quantité de calcul. **Cette régularité est empirique, pas une loi.** Elle décrit ce qui a été observé sur une plage donnée ; elle ne garantit ni sa poursuite, ni l'apparition d'une capacité donnée à un niveau donné, et elle porte sur des mesures agrégées qui masquent des comportements très variables tâche par tâche.

**Où vous rencontrerez le terme.** Partout — et c'est le problème : il désigne selon le contexte un objet technique, un produit, ou un fournisseur.

**Ce que ça permet.** Obtenir un comportement utile sur une tâche sans disposer d'un jeu de données propre à cette tâche — ce qui a supprimé la principale barrière d'entrée de l'apprentissage automatique.

**Ce qui bloque.** **La densité des données.** Un modèle est bon là où ses données sont denses ; l'adaptation en aval ne crée pas de compétence là où le socle n'en avait pas. **Le coût d'entraînement**, qui concentre l'activité chez un petit nombre d'acteurs capables de l'engager. Et **l'absence de garantie** : on mesure une performance sur un échantillon, on ne démontre pas un comportement.

**De quoi ça dépend.** Accélérateurs · énergie · données et droits associés · compétences rares · infrastructure d'entraînement.

**Ce que cela implique.** Construire sur un socle qu'on n'a pas entraîné, dont on ne connaît pas les données et qui peut changer de comportement à chaque version est **une dépendance au sens strict** — au même titre qu'une dépendance à un fournisseur unique de composant. Elle est rarement traitée comme telle.

**Sûreté et sécurité.** Intégrité des données d'entraînement · dépendance à un fournisseur tiers non auditable · reproductibilité d'un comportement entre deux versions.

**À ne pas confondre avec.** **Un produit**, qui inclut une interface, une politique d'usage et une infrastructure. **Un modèle spécialisé**, entraîné pour une tâche unique et qui la surpasse souvent.

**Termes voisins.** *LLM* désigne la sous-famille textuelle. *Frontier model* désigne une catégorie réglementaire, non technique.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Écart croissant entre les modèles les plus grands et les modèles compacts sur les tâches courantes ; concentration persistante de la capacité d'entraînement.
> 🔄 **À revoir si** l'augmentation conjointe de la taille, des données et du calcul cesse de produire des gains mesurables sur des tâches d'intérêt pratique.

**Renvois** — Couche : apprendre et décider · Courants : IA générative, Frontier AI (ch. 32) · Convergences : découverte scientifique (37), biologie programmable (41).

---
