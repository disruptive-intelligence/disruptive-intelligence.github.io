---
title: ◆◆ Affichages avancés
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — interagir

**En une phrase.** Les dispositifs optiques qui délivrent une image à l'œil dans un volume et une consommation compatibles avec le port prolongé.

**Pourquoi cette entrée est déterminante.** Parce que **c'est le verrou physique de toute la première moitié du chapitre** : le confort, l'autonomie, le champ de vision et le coût des dispositifs portés sont commandés par l'affichage.

**Comment ça fonctionne.** Deux sous-ensembles. Une **source d'image**, qui doit être extrêmement lumineuse pour rester visible en superposition à la lumière du jour, et minuscule. Un **système optique** qui achemine cette image jusqu'à l'œil — typiquement un guide d'onde, plaque transparente dans laquelle la lumière se propage par réflexions avant d'être extraite devant la pupille.

**Le compromis qui borne tout.** **Champ de vision, luminosité, encombrement et rendement optique s'opposent deux à deux.** Élargir le champ de vision réduit la luminosité disponible ; améliorer le rendement complique la fabrication ; réduire l'encombrement limite le champ. **Aucune conception ne maximise les quatre**, et c'est la contrainte structurelle du domaine.

**Ce qui bloque.** **Le rendement optique**, très faible dans les guides d'onde : une fraction seulement de la lumière produite atteint l'œil, ce qui impose des sources très puissantes et donc de la consommation et de la chaleur. **Les artefacts optiques** — irisations, images fantômes — inhérents à ces architectures. Et **le coût de fabrication**, ces composants exigeant des tolérances très fines sur des surfaces étendues.

**Ce que cela implique.** **Le progrès du domaine se mesure au rendement optique et à la luminosité par watt**, non au champ de vision annoncé. C'est la grandeur à surveiller, et elle est rarement publiée.

**À ne pas confondre avec.** Les **écrans** classiques, dont les contraintes n'ont rien de commun : un écran est regardé à distance, un affichage porté est traversé.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Progrès continus sur les sources et les guides d'onde ; le compromis fondamental n'est pas levé.
> 🔄 **À revoir si** un affichage porté atteint simultanément un large champ de vision, une luminosité utilisable en extérieur et une autonomie d'une journée.

**Renvois** — Couche : interagir.

---


## ◆◆ Suivi oculaire et gestuel

**Niveau** — capacité · **Couche** — interagir, percevoir

**En une phrase.** Déterminer où l'utilisateur regarde et ce que font ses mains, pour en faire des modalités d'entrée.

**Pourquoi c'est important.** Parce que **c'est l'une des rares réponses au verrou de la couche** : capter une intention sans effort conscient ni dispositif tenu en main.

**Comment ça fonctionne.** Le suivi oculaire éclaire l'œil en infrarouge et analyse les reflets pour estimer la direction du regard. Le suivi gestuel utilise des caméras et un modèle de la main pour estimer la position des articulations.

**Ce que ça permet.** Une désignation naturelle — regarder ce qu'on veut sélectionner · une interaction sans dispositif tenu · **et une optimisation majeure du calcul** : n'afficher en haute résolution que la zone regardée, l'œil ne percevant les détails que dans une petite région centrale. Cette technique divise significativement la charge de rendu.

**Ce qui bloque.** **La désignation n'est pas la commande.** Regarder un objet ne signifie pas vouloir agir sur lui ; il faut un geste ou un signal de validation, ce qui ramène le problème initial. **La fatigue** : maintenir un geste dans le vide est épuisant sur la durée, phénomène bien documenté. **La robustesse** du suivi gestuel selon l'éclairage et les occultations. Et **la vie privée** : le regard révèle l'attention, l'intérêt et parfois l'état cognitif — c'est une donnée d'une sensibilité particulière.

**Ce que cela implique.** Ces modalités fonctionnent **en combinaison** et non isolément : regard pour désigner, geste ou voix pour confirmer. Aucune ne remplace à elle seule un dispositif de pointage.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les dispositifs portés récents.
> 🔄 **À revoir si** une modalité de confirmation sans geste ni voix atteint une fiabilité utilisable.

**Renvois** — Couche : interagir, percevoir.

---
