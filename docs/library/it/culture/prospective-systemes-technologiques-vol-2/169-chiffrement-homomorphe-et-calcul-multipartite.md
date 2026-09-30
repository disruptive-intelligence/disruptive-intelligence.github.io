---
title: ◆◆ Chiffrement homomorphe et calcul multipartite
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Calculer sur des données sans les déchiffrer, ou faire calculer plusieurs parties sur leurs données respectives sans qu'aucune ne révèle les siennes.

**Comment ça fonctionne.** Le **chiffrement homomorphe** permet d'effectuer des opérations sur des données chiffrées, le résultat déchiffré étant celui qu'on aurait obtenu sur les données en clair. Le **calcul multipartite** répartit le calcul entre plusieurs participants de telle sorte qu'aucun ne dispose d'assez d'information pour reconstituer les entrées des autres.

**Ce que ça permet.** Confier un traitement sans confier les données · croiser des jeux de données entre organisations qui ne peuvent pas les partager · établir une statistique sur une population sans exposer les individus.

**Ce qui bloque.** **Le coût en calcul**, encore très supérieur au traitement en clair — plusieurs ordres de grandeur selon les opérations, malgré des progrès continus. **La complexité de mise en œuvre**, qui exige une expertise rare. Et **la concurrence des enclaves** (ch. 28), qui offrent une garantie de nature différente — matérielle plutôt que mathématique — à un coût de performance bien inférieur.

**Ce que cela implique.** Ces techniques ont une garantie **plus forte** que les enclaves, puisqu'elles ne supposent aucune confiance dans un fabricant. Elles ont un coût bien supérieur. **L'arbitrage se joue sur le degré de confiance que l'on accepte de déplacer**, et non sur la performance seule.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des déploiements sur des cas où la sensibilité justifie le coût.
> 🔄 **À revoir si** le surcoût de calcul descend sous un ordre de grandeur pour des opérations courantes.

**Renvois** — Couche : vérifier, calculer.

---
