---
title: Chapitre 10 — Le quantique
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute.** Les chapitres 8 et 9 traitaient de manières de calculer plus efficacement. Celui-ci traite d'une machine qui ne calcule pas de la même façon — et dont la portée est bien plus étroite, et bien plus profonde, que le discours public ne le laisse entendre.
>
> **Trois entrées seulement**, dont deux majeures. C'est délibéré : le domaine se comprend par trois objets, et le découper davantage produirait des répétitions.
>
> **Un renvoi important.** Les **capteurs quantiques** sont traités au chapitre 7, dans la couche *percevoir*. Ce n'est pas un oubli : c'est l'application de la règle des couches, et c'est la distinction la plus utile de tout le domaine.

---

## ◆◆◆ Calcul quantique

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

## ◆◆◆ Correction d'erreur quantique

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Encoder l'information d'un qubit fiable sur un grand nombre de qubits fragiles, de manière à détecter et corriger les erreurs en cours de calcul.

**Pourquoi on en parle.** Parce que **c'est la seule voie connue vers un calcul quantique utile**, et parce que la distinction qu'elle introduit — qubit physique contre qubit logique — est celle qui manque à presque tout décompte public.

**Comment ça fonctionne.** On ne peut pas copier un état quantique pour le comparer — la mesure le détruirait. La correction repose donc sur un mécanisme indirect : on répartit l'information sur plusieurs qubits physiques et on mesure des **combinaisons** de ces qubits, choisies pour révéler qu'une erreur s'est produite et où, **sans révéler l'information elle-même**.

**Le seuil.** La correction n'aide que si les erreurs sont assez rares au départ. En dessous d'un certain taux d'erreur des opérations élémentaires, ajouter des qubits réduit le taux d'erreur logique ; au-dessus, cela l'augmente. Franchir ce seuil a été le résultat majeur de la période récente.

**Le rapport entre physique et logique.** Il dépend du schéma de correction retenu, du taux d'erreur des qubits et de la longueur du calcul visé. **Ce volume ne le chiffre pas**, pour une raison assumée : le rapport évolue avec les schémas, et un chiffre le figerait. Ce qui compte est la question à poser.

**La question à poser, désormais.** Devant tout décompte de qubits : **physiques ou logiques, avec quel taux d'erreur, et pour quelle durée de calcul ?** Un décompte non qualifié n'est pas une information.

**Ce qui bloque.** **Le coût en qubits physiques**, considérable. **La rapidité de la correction**, qui doit s'effectuer plus vite que les erreurs n'apparaissent, ce qui impose une électronique de contrôle très rapide fonctionnant à proximité de la machine. Et **l'échelle** : passer de quelques qubits logiques à un nombre utile suppose un assemblage dont la complexité croît fortement.

**Ce que cela implique.** Toute annonce de progrès quantique doit être lue à travers cette entrée. Un doublement du nombre de qubits physiques sans amélioration du taux d'erreur peut ne représenter **aucun progrès vers l'utilité**.

**À ne pas confondre avec.** **L'atténuation d'erreur**, qui corrige statistiquement les résultats après coup, sans corriger le calcul lui-même. Elle permet d'exploiter des machines bruitées pour certaines tâches, mais ne s'étend pas aux calculs longs.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Franchissement du seuil démontré sur de petits systèmes ; premiers qubits logiques opérationnels en nombre très limité. Le passage à l'échelle est le sujet actif.
> 🔄 **À revoir si** un système démontre plusieurs dizaines de qubits logiques exploitables simultanément avec une durée de calcul utile.

**Renvois** — Couche : calculer.

---

## ◆◆ Communications quantiques

**Niveau** — capacité · **Couche** — relier, vérifier

**En une phrase.** Utiliser des propriétés quantiques pour transmettre de l'information de manière dont la sécurité repose sur la physique plutôt que sur une hypothèse calculatoire.

**Comment ça fonctionne.** L'application principale est la **distribution quantique de clés**. Deux parties échangent des états quantiques ; toute tentative d'interception les perturbe de façon détectable. Les parties comparent un échantillon, détectent une éventuelle écoute et, en son absence, disposent d'une clé partagée dont la confidentialité repose sur les lois physiques.

**Ce qui bloque.** **La distance.** Les signaux s'atténuent et **on ne peut pas amplifier un état quantique** — un répéteur classique le détruirait. La portée est donc limitée à quelques centaines de kilomètres en fibre, ce qui impose soit des relais de confiance, qui affaiblissent la garantie, soit des liaisons satellitaires, soit des répéteurs quantiques encore expérimentaux.

S'y ajoutent le **débit**, faible, et le fait que **cela ne résout qu'un problème** : l'échange de clés. L'authentification, l'intégrité et la signature restent à assurer par d'autres moyens.

**Ce que cela implique.** La distribution quantique de clés et la cryptographie post-quantique sont deux réponses au même risque, de natures différentes : l'une repose sur la physique et exige du matériel dédié, l'autre repose sur de nouvelles hypothèses mathématiques et se déploie logiciellement.

**Les positions publiques des autorités nationales de sécurité convergent davantage qu'on ne le dit, et c'est un point de vocabulaire à tenir.** Une prise de position commune de plusieurs agences européennes — dont les agences française, allemande, néerlandaise et suédoise — conclut que la technologie actuelle ne convient qu'à des usages de niche et que la cryptographie post-quantique et les clés symétriques prépartagées doivent être les solutions principales. Les agences américaine et britannique vont plus loin et ne soutiennent pas son emploi pour leurs systèmes gouvernementaux ou de sécurité nationale tant que ses limites ne sont pas levées.

**Trois arguments reviennent dans tous ces textes**, et ils sont techniques et non doctrinaux : la distribution quantique de clés **n'assure pas l'authentification**, qui reste à fournir par de la cryptographie classique ou post-quantique ; elle exige un **matériel spécialisé** et des liaisons dédiées, là où la seconde est une mise à jour logicielle ; et les **relais de confiance** réintroduisent une hypothèse de confiance physique que la garantie théorique prétendait supprimer.

**Ce que ce désaccord n'est pas.** Un débat sur la physique, qui n'est pas contestée. **C'est un désaccord sur le rapport entre le bénéfice et le coût d'infrastructure** — exactement la forme de verrou décrite au chapitre 3, et la raison pour laquelle des politiques publiques de soutien à des infrastructures de communication quantique coexistent sans contradiction avec ces réserves techniques.

**À ne pas confondre avec.** **Le calcul quantique**, dont c'est un domaine entièrement distinct. **La cryptographie post-quantique** (ch. 29), qui n'a rien de quantique — c'est de la cryptographie classique résistante à un attaquant quantique.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Liaisons opérationnelles sur des périmètres restreints et démonstrations satellitaires ; répéteurs quantiques en recherche.
> 🔄 **À revoir si** un répéteur quantique fonctionnel permet une liaison longue distance sans relais de confiance.

**Renvois** — Couche : relier, vérifier · Voir aussi : cryptographie post-quantique (ch. 29).

---
