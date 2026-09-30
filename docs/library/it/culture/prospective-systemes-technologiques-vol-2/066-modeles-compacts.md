---
title: ◆◆ Modèles compacts
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
