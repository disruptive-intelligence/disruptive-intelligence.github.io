---
title: ◆◆ Mémoire et contexte long
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Permettre à un modèle de tenir compte d'une grande quantité d'information fournie au moment de l'usage, ou de conserver une trace entre les échanges.

**Pourquoi on en parle.** Parce que c'est la limite que rencontrent en premier tous les usages professionnels — et parce que deux mécanismes très différents sont désignés par le même mot.

**Comment ça fonctionne — deux mécanismes distincts.**

**Le contexte** est ce qu'on fournit au modèle à chaque appel. Il est volatil : rien n'en subsiste après l'échange. L'étendre coûte cher, parce que le mécanisme qui met chaque élément en relation avec les autres implique un nombre de comparaisons croissant **avec le carré** de la longueur. Doubler le contexte quadruple ce coût — contrainte structurelle, et non réglage.

**La mémoire externe** consiste à stocker de l'information à l'extérieur du modèle et à en réinjecter les fragments pertinents au moment utile. Ce n'est pas une propriété du modèle mais une **architecture**, et sa qualité dépend entièrement de la pertinence de la récupération.

**Ce qui bloque.** Pour le contexte : le coût, la latence, et le fait qu'**une information présente dans un très long contexte n'est pas nécessairement utilisée** — la performance dépend de sa position et de sa saillance. Pour la mémoire externe : la récupération, qui devient le maillon déterminant, et la gestion de l'obsolescence — que faire d'une information mémorisée devenue fausse.

**Ce que cela implique.** Un modèle **n'a pas de mémoire persistante par construction** ; ce qu'il a appris est figé à l'entraînement. Tout ce qui ressemble à de la mémoire est un dispositif extérieur, avec ses propres modes de défaillance.

**À ne pas confondre avec.** **L'apprentissage**, qui modifie les paramètres. Fournir une information en contexte ne l'apprend pas.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Contextes très étendus disponibles ; l'exploitation effective de leur totalité reste inégale selon les tâches.
> 🔄 **À revoir si** un mécanisme dont le coût croît linéairement avec la longueur atteint les performances du mécanisme quadratique sur les tâches courantes.

**Renvois** — Couche : apprendre et décider · Convergence : intelligence distribuée (38).

---


## ◆◆ Modèles compacts

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Obtenir un comportement utile avec un modèle assez petit pour tenir dans la mémoire d'un appareil ordinaire.

**Pourquoi on en parle.** Parce que c'est la condition de l'exécution locale — donc de la latence faible, du coût par appel nul et de l'indépendance vis-à-vis d'un réseau.

**Comment ça fonctionne — trois techniques, souvent combinées.** La **distillation** entraîne un petit modèle à reproduire le comportement d'un grand. La **quantification** réduit la précision des paramètres, ce qui divise l'empreinte mémoire. Le **mélange d'experts** n'active qu'une fraction des paramètres à chaque requête, ce qui réduit le calcul sans réduire la taille totale.

**Ce que ça permet.** Exécuter sur un téléphone, un véhicule, un équipement industriel · supprimer le coût par requête · traiter des données qui ne doivent pas quitter l'appareil.

**Ce qui bloque.** **La dégradation n'est pas uniforme.** Un modèle compact peut égaler un grand modèle sur les tâches courantes et s'effondrer sur les cas rares — sans que les tests usuels le révèlent. C'est une défaillance silencieuse. S'y ajoutent la **mémoire disponible**, qui est la contrainte dimensionnante bien avant la puissance de calcul, et la **mise à jour** d'un parc déployé.

**À ne pas confondre avec.** **Un modèle simplement plus petit**, entraîné directement à cette taille : les performances diffèrent nettement, la distillation transférant une partie du comportement du grand modèle.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Exécution locale disponible sur des appareils courants ; l'écart avec les modèles distants persiste sur les tâches complexes.
> 🔄 **À revoir si** un modèle exécutable localement atteint, sur une tâche professionnelle de référence, la performance d'un modèle distant de génération courante.

**Renvois** — Couche : apprendre et décider · Convergence : intelligence distribuée (38).

---


## ◆◆ Données synthétiques

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Entraîner un modèle sur des données produites par un autre modèle ou par simulation, plutôt que collectées.

**Ce que ça permet.** Compléter des cas rares mal représentés · produire des données là où la collecte est coûteuse, dangereuse ou juridiquement contrainte · générer des variations contrôlées pour éprouver la robustesse.

**Ce qui bloque.** **La dérive de distribution.** Un modèle entraîné majoritairement sur les productions d'un autre hérite de ses biais et de ses angles morts, et peut s'écarter progressivement du réel sans que rien ne le signale. La question ouverte est celle de la proportion acceptable, et elle n'est pas tranchée. S'y ajoute la **validation** : vérifier qu'une donnée synthétique est représentative suppose de disposer de données réelles — ce qui est précisément ce qui manquait.

**Ce que cela implique.** Les données synthétiques fonctionnent bien là où **un modèle physique fiable existe** — simulation d'un capteur, d'un mécanisme, d'un environnement. Elles fonctionnent mal là où la richesse du réel est précisément ce qu'on ne sait pas modéliser.

**À ne pas confondre avec.** **L'augmentation de données**, qui transforme des données réelles sans en créer de nouvelles.

> ⏱ **État au 23/08/2026** — 🏭 déployé, pratique courante, avec des proportions et des méthodes variables selon les domaines.
> 🔄 **À revoir si** une méthode de mesure de la dérive de distribution devient assez fiable pour être utilisée comme critère de qualité opposable.

**Renvois** — Couche : apprendre et décider · Convergences : robotique généraliste (36), découverte scientifique (37).

---
