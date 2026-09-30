---
title: ◆◆◆ Calcul quantique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Une machine qui exploite les propriétés quantiques de systèmes physiques pour effectuer certains calculs d'une manière inaccessible aux machines classiques.

**Pourquoi on en parle.** Parce que c'est la technologie la plus discutée et la plus mal située de cet atlas — et parce que ses effets, s'ils se matérialisent, concernent directement les infrastructures de sécurité existantes.

**Comment ça fonctionne — quatre notions suffisent.**

**Le qubit.** Un système quantique à deux états, qui peut se trouver dans une **superposition** de ces deux états : une combinaison des deux, avec des poids.

**La mesure détruit la superposition.** Quand on observe un qubit, on obtient l'un des deux états, avec une probabilité déterminée par les poids. **On ne peut pas lire une superposition.** C'est la contrainte fondamentale du domaine, et elle explique pourquoi le calcul quantique n'est pas un calcul parallèle massif : l'information est là, mais elle n'est pas directement accessible. Tout l'art consiste à organiser le calcul pour que les mauvaises réponses s'annulent entre elles et que la bonne devienne probable à la mesure.

**L'intrication.** Plusieurs qubits peuvent être corrélés de telle sorte que leur état ne se décrit pas indépendamment. C'est cette propriété, plus que la superposition seule, qui donne au calcul quantique sa puissance potentielle.

**La décohérence.** Un système quantique interagit inévitablement avec son environnement, et cette interaction détruit progressivement superposition et intrication. **C'est l'ennemi principal**, et c'est ce qui impose l'isolement extrême — températures très basses, vide, blindages — qui caractérise ces machines.

**Les familles matérielles.** Plusieurs supports physiques coexistent — circuits supraconducteurs, ions piégés, atomes neutres, photons, spins en semi-conducteur — avec des compromis différents entre vitesse d'opération, durée de cohérence, fidélité et facilité d'assemblage. **Aucune ne s'est imposée**, et c'est en soi une information sur la maturité du domaine.

**Une variante distincte.** Le **recuit quantique** est une approche différente, dédiée à des problèmes d'optimisation, et qui n'est pas un calculateur quantique universel. Les deux sont régulièrement confondus.

**Où vous rencontrerez le terme.** Sécurité et cryptographie · chimie et matériaux · optimisation · finance · programmes de recherche publics · discours stratégiques.

**Ce que ça permet — et la formulation compte.** Pour certaines familles de problèmes à structure particulière, un avantage théorique est démontré. **Il n'existe aucun avantage quantique pour un calcul quelconque.**

**Ce qui bloque.** **Le bruit.** Les qubits physiques sont fragiles et leurs opérations imparfaites ; l'accumulation d'erreurs limite la longueur des calculs réalisables. C'est l'objet de l'entrée suivante, et c'est le verrou central.

S'y ajoutent l'infrastructure de refroidissement et de contrôle, dont le volume et la consommation dépassent largement ceux de la machine elle-même ; la difficulté d'assemblage à grand nombre ; et le fait que **le nombre d'algorithmes offrant un avantage démontré reste restreint**.

**Ce que cela implique.** Ce ne sera pas un remplacement des machines classiques mais un **accélérateur ciblé**, dans des architectures où une machine classique conduit le calcul et délègue certaines étapes. Cela ne rend pas non plus calculable ce qui ne l'est pas en théorie.

**Sûreté et sécurité — le point qui vous concerne directement.** Certaines hypothèses de difficulté sur lesquelles reposent des mécanismes cryptographiques largement déployés seraient affaiblies par une machine suffisamment grande et fiable.

**La conséquence pratique ne dépend pas d'une date.** Elle dépend de **la durée pendant laquelle vos données doivent rester confidentielles** — car une donnée capturée aujourd'hui peut être déchiffrée plus tard. Et la migration cryptographique est un problème d'infrastructure et de base installée, non de logiciel : elle concerne des équipements dont certains ne seront jamais mis à jour.

**À ne pas confondre avec.** **Les capteurs quantiques** (ch. 7), dont la maturité est sans commune mesure et dont les progrès n'indiquent rien sur le calcul. **Les communications quantiques**, traitées plus bas. **Le recuit quantique**, qui n'est pas universel.

> ⏱ **État au 23/08/2026** — 🔭 prospectif. Machines disponibles en accès distant, démonstrations d'avantage sur des problèmes construits à cet effet, aucun avantage établi sur un problème d'intérêt pratique. Les feuilles de route des acteurs s'expriment désormais en qubits logiques, ce qui est un progrès de formulation.
> 🔄 **À revoir si** un avantage quantique est démontré sur un problème d'intérêt industriel, avec une machine à qubits logiques, et reproduit indépendamment.

**Renvois** — Couche : calculer · Courant : Quantum Tech (ch. 35) · Voir aussi : cryptographie post-quantique (ch. 29).

---
