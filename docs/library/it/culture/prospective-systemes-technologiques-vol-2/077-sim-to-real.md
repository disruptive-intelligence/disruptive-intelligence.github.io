---
title: ◆◆◆ Sim-to-real
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Entraîner un système en simulation, puis transférer le comportement appris sur un système physique.

**Pourquoi on en parle.** Parce que c'est **la réponse principale au coût des données physiques** — et parce que l'écart entre simulation et réel est le verrou qui décide de son efficacité.

**Comment ça fonctionne.** On entraîne dans un simulateur, où les essais sont rapides, parallélisables, sans usure et sans risque. Puis on transfère.

**Le problème est l'écart de réalité.** Aucune simulation ne reproduit exactement les frottements, les jeux, les déformations, les délais de capteur et les propriétés des matériaux. Un comportement optimal en simulation exploite souvent des particularités du simulateur qui n'existent pas dans le monde.

**La parade principale est la randomisation.** Plutôt que de simuler précisément, on fait varier aléatoirement les paramètres — masses, frottements, éclairages, délais — pendant l'entraînement. Le système apprend alors un comportement qui fonctionne sur toute une famille de mondes possibles, dont le monde réel fait partie. **On renonce à l'exactitude pour obtenir de la robustesse** — c'est un compromis, et il coûte en performance de pointe.

**Ce que ça permet.** Réduire massivement le besoin d'interactions réelles · explorer des situations dangereuses sans risque · paralléliser l'apprentissage.

**Ce qui bloque.** **La physique du contact**, mal simulée : c'est là que l'écart est le plus grand, et c'est précisément ce dont la manipulation dépend. **La perception** : les images simulées diffèrent des images réelles de façon subtile. Et **la validation**, qui exige de toute façon des essais réels.

**Ce que cela implique.** Le transfert fonctionne bien pour la locomotion et le déplacement, où la physique est dominée par des effets bien modélisés. Il fonctionne mal pour la manipulation fine. **C'est cohérent avec le fait que manipuler soit plus difficile que se déplacer** — et cela indique où le progrès compte.

**À ne pas confondre avec.** **La simulation d'ingénierie**, qui vise la fidélité pour dimensionner. Ici, la fidélité n'est pas l'objectif : la robustesse l'est.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour la locomotion, 🔬 émergent pour la manipulation.
> 🔄 **À revoir si** un simulateur de contact atteint une fidélité permettant un transfert direct de comportements de manipulation fine sans réglage sur le système réel.

**Renvois** — Couche : apprendre et décider · Convergences : robotique généraliste (36), autonomie mobile (39).

---
