---
title: ◆◆◆ Navigation sans référence satellitaire
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Savoir où l'on se trouve quand le positionnement par satellite est indisponible, dégradé ou non fiable.

**Pourquoi on en parle.** Parce que la dépendance décrite à l'entrée précédente est massive, largement invisible, et que sa remise en cause est devenue un sujet d'ingénierie sérieux dans de nombreux domaines civils.

**Comment ça fonctionne.** Cinq familles de méthodes, souvent combinées.

**L'inertiel**, traité plus haut : autonome, mais dérivant.

**L'odométrie visuelle** : estimer son déplacement en suivant le mouvement apparent de points caractéristiques dans des images successives. Précise à court terme, dépendante de la texture de l'environnement et de l'éclairement, et dérivant elle aussi.

**L'appariement de terrain** : comparer ce que l'on perçoit — relief, image, signature magnétique, profondeur — à une carte de référence embarquée. Ne dérive pas, mais exige une carte, à jour, du territoire survolé ou parcouru.

**La navigation par signaux d'opportunité** : exploiter des émissions non destinées à la navigation — télécommunications, diffusion — dont la position des émetteurs est connue.

**La navigation céleste**, retrouvée avec l'automatisation : mesurer la position d'astres, ce qui est insensible à toute perturbation terrestre mais exige une visibilité du ciel et une référence de temps.

**Où vous rencontrerez le terme.** Aéronautique · maritime et sous-marin · robotique en intérieur · milieu souterrain · agriculture sous couvert · applications de défense.

**Ce que ça permet.** Poursuivre une mission en environnement dégradé · fonctionner là où le signal n'a jamais été disponible · détecter une incohérence entre sources et donc **repérer un positionnement erroné**, ce qui est parfois plus important que de s'en passer.

**Ce qui bloque.** **Aucune méthode n'est bonne partout.** L'inertiel dérive, la visuelle dépend de la scène, l'appariement dépend d'une carte, les signaux d'opportunité dépendent d'une infrastructure tierce. La combinaison est donc la règle — mais **elle ajoute ses propres modes de défaillance** : recalage entre sources, arbitrage en cas de désaccord, et corrélation des erreurs quand deux sources sont affectées par la même cause.

**De quoi ça dépend.** Capteurs inertiels · imagerie · cartes de référence · calcul embarqué · référence de temps locale.

**Ce que cela implique.** Ce domaine illustre un mécanisme général : **une dépendance devient visible au moment où elle devient contestable.** Le positionnement satellitaire était une commodité gratuite ; il est traité comme une infrastructure dont il faut prévoir l'indisponibilité.

**Sûreté et sécurité.** Traitement au niveau du principe et des conséquences systémiques uniquement : ce volume ne décrit aucune technique de perturbation ni aucune contre-mesure opérationnelle.

**À ne pas confondre avec.** **Le SLAM**, qui construit une carte tout en s'y localisant, sans référence absolue — il fournit une position relative, pas une position dans un repère global.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Composants matures pris séparément ; l'intégration robuste et certifiable est le sujet actif, avec une demande en forte croissance.
> 🔄 **À revoir si** un référentiel de certification impose une capacité de navigation de secours dans un secteur civil réglementé — ce qui transformerait un sujet d'ingénierie en obligation de conception.

**Renvois** — Couche : percevoir · Convergences : autonomie mobile (39) · Voir aussi : chapitre 45.

---
