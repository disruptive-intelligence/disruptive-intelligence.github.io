---
title: Chapitre 8 — Le calcul spécialisé
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte dominante : déplacer une donnée coûte plusieurs centaines de fois plus que la traiter, et cet écart s'est creusé. Ce chapitre traite des réponses apportées **à l'intérieur du paradigme électronique existant** — spécialisation, assemblage, hiérarchie mémoire, réduction de précision.
>
> Le chapitre 9 traitera des réponses qui sortent de ce paradigme, et le chapitre 10 d'une rupture d'une autre nature.
>
> **Six entrées.** Deux définissent l'économie du domaine, deux attaquent directement le mur de la mémoire, deux sont des leviers.

---

## ◆◆◆ Accélérateurs de calcul spécialisés

**Niveau** — composant · **Couche** — calculer

**En une phrase.** Des puces conçues pour exécuter très efficacement une famille restreinte d'opérations, plutôt que n'importe quel programme.

**Pourquoi on en parle.** Parce que la performance ne vient plus de la fréquence ni de la généralité, mais de la spécialisation — et que la disponibilité de ces composants est devenue une contrainte stratégique.

**Comment ça fonctionne.** Un processeur généraliste consacre l'essentiel de sa surface à décider quoi faire : prédiction de branchement, réordonnancement, hiérarchie de caches. Un accélérateur supprime cette machinerie et consacre sa surface à des unités de calcul disposées pour un motif fixe — typiquement la multiplication de matrices, opération dominante de l'apprentissage.

**Le gain vient de trois sources**, et la première est la moins évidente : la **régularité des accès mémoire**, qui permet de réutiliser une donnée chargée pour de nombreuses opérations ; le **parallélisme massif** ; et la **précision réduite**, traitée plus loin.

**Où vous rencontrerez le terme.** Centres de calcul · véhicules · téléphones · équipements industriels · instrumentation · réseaux.

**Ce que ça permet.** Exécuter des charges qui seraient économiquement impossibles autrement, pour une énergie par opération inférieure de plusieurs ordres de grandeur à celle d'un processeur généraliste sur la même tâche.

**Ce qui bloque.** **L'alimentation de la puce en données.** Un accélérateur puissant est souvent sous-utilisé parce que la mémoire ne suit pas : c'est le mur de la couche, et il commande la conception. **La spécialisation elle-même** : une puce optimisée pour un motif de calcul devient inefficace si le motif change, or les architectures logicielles évoluent plus vite que les cycles de conception matérielle, qui se comptent en années. Enfin **la chaîne d'approvisionnement**, extrêmement concentrée en fabrication comme en assemblage.

**De quoi ça dépend.** Semi-conducteurs de pointe · assemblage avancé · mémoires à forte bande passante · alimentation et refroidissement · outils de conception · écosystème logiciel.

**Ce que cela implique.** L'écosystème logiciel pèse autant que la performance. Un accélérateur supérieur sans compilateurs, bibliothèques et personnes formées reste inutilisé — c'est le coût de sortie d'un standard dominant, et il explique la persistance des positions acquises.

**Sûreté et sécurité.** Confiance dans un composant qu'on n'a pas fabriqué et qu'on ne peut inspecter sans le détruire · dépendance à une chaîne concentrée · surface d'attaque des chaînes de compilation.

**À ne pas confondre avec.** **Le processeur généraliste**, qui reste indispensable pour orchestrer. **Le FPGA**, reconfigurable et donc plus souple, mais moins efficace à motif fixe.

**Termes voisins.** *GPU*, *TPU*, *NPU*, *ASIC* désignent des points sur un continuum entre généralité et spécialisation — et non quatre familles distinctes.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Demande supérieure à l'offre sur les segments de pointe ; disponibilité soumise à des contrôles à l'exportation dans plusieurs juridictions. L'inférence représente une part croissante et parfois majoritaire des besoins.
> 🔄 **À revoir si** une architecture logicielle dominante s'écarte suffisamment du motif matriciel pour rendre inefficace la génération d'accélérateurs en place.

**Renvois** — Couche : calculer · Courants : IA générative, AI factories (ch. 32) · Convergences : énergie et calcul (40), intelligence distribuée (38).

---

## ◆◆◆ Chiplets et assemblage avancé

**Niveau** — procédé · **Couche** — calculer

**En une phrase.** Construire un composant en assemblant plusieurs petites puces plutôt qu'en fabriquant une seule grande.

**Pourquoi on en parle.** Parce que c'est devenu **le principal levier de performance** de la microélectronique, davantage que la réduction des dimensions — et parce que ce déplacement est mal connu hors du secteur.

**Comment ça fonctionne.** La raison est économique avant d'être technique. Des défauts microscopiques se répartissent au hasard sur une plaquette ; plus une puce est grande, plus elle a de chances d'en contenir un, et la proportion de puces conformes s'effondre. Doubler la surface ne double pas le coût : il peut le tripler.

**La solution consiste à découper la fonction.** On fabrique plusieurs puces plus petites — chacune avec un bon rendement, chacune éventuellement dans le procédé le mieux adapté à sa fonction — et on les assemble sur un support commun avec des liaisons très courtes et très nombreuses. On peut aussi les empiler, ce qui réduit encore les distances.

**Où vous rencontrerez le terme.** Processeurs et accélérateurs · mémoires · équipements réseau · progressivement dans l'embarqué.

**Ce que ça permet.** Contourner la limite de taille imposée par le rendement · combiner des procédés de générations différentes selon les besoins de chaque bloc · rapprocher la mémoire du calcul, ce qui attaque directement le mur de la couche.

**Ce qui bloque.** **Le test.** Il faut vérifier chaque puce avant assemblage, car une seule défectueuse ruine l'ensemble — et certains défauts n'apparaissent qu'après assemblage. **La thermique** : empiler des sources de chaleur réduit la surface d'évacuation par unité de puissance, ce qui est le carré-cube appliqué à la puce. **L'interopérabilité** : assembler des puces d'origines différentes suppose des interfaces normalisées, et cette normalisation est récente et incomplète.

**De quoi ça dépend.** Équipements d'assemblage de précision · substrats et interposeurs · matériaux d'interconnexion · métrologie · normes d'interface.

**Ce que cela implique.** Le goulet s'est **déplacé de la fabrication vers l'assemblage**, qui a sa propre concentration industrielle et ses propres délais. C'est un cas d'école du mécanisme du volume 1 : résoudre une contrainte ne la supprime pas, il la déplace — et le nouveau goulet n'est pas là où l'attention se portait.

**À ne pas confondre avec.** **Le multi-puce classique**, qui plaçait plusieurs composants indépendants dans un boîtier sans liaison à haute densité. Ici, l'assemblage fait partie de la conception du composant.

**Termes voisins.** *Packaging avancé*, *intégration 2.5D et 3D*, *collage hybride* désignent des techniques d'un même mouvement.

> ⏱ **État au 23/08/2026** — 🏭 déployé et en généralisation. Capacité d'assemblage avancé identifiée comme facteur limitant chez plusieurs acteurs ; normalisation des interfaces entre puces en cours.
> 🔄 **À revoir si** une norme d'interface entre puces d'origines différentes devient assez répandue pour qu'un marché de composants assemblables apparaisse.

**Renvois** — Couche : calculer · Convergence : énergie et calcul (40).

---

## ◆◆ Mémoires à forte bande passante

**Niveau** — composant · **Couche** — calculer

**En une phrase.** Des mémoires empilées et connectées très largement au processeur, conçues pour livrer beaucoup de données par seconde plutôt que pour stocker beaucoup.

**Pourquoi on en parle.** Parce que **c'est le vrai goulet de l'inférence**, et parce que leur disponibilité conditionne celle des accélérateurs.

**Comment ça fonctionne.** Plutôt que de placer la mémoire à côté du processeur et de la relier par un nombre limité de connexions, on empile plusieurs couches de mémoire et on les relie par un très grand nombre de liaisons courtes traversant les couches. La bande passante augmente d'un ordre de grandeur, et l'énergie par donnée transférée diminue.

**Ce que ça permet.** Alimenter un accélérateur assez vite pour qu'il soit effectivement utilisé — sans quoi la puissance de calcul annoncée reste théorique.

**Ce qui bloque.** **La fabrication et le rendement de l'empilement**, qui exigent un alignement de très haute précision. **Le coût**, sensiblement supérieur à celui d'une mémoire classique à capacité égale. **La thermique**, la mémoire empilée se trouvant à proximité immédiate d'une source de chaleur importante. Et **la capacité** : ces mémoires offrent moins de gigaoctets qu'une mémoire classique de même prix.

**Ce que cela implique.** Le dimensionnement d'un système d'inférence est souvent commandé par la mémoire disponible, non par la puissance de calcul — ce qui explique pourquoi la taille d'un modèle exécutable dépend d'abord de ce paramètre.

**À ne pas confondre avec.** **La mémoire vive classique**, dont l'objectif est la capacité. **Le cache**, intégré au processeur, bien plus rapide et bien plus petit.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Capacité de production identifiée comme facteur limitant de l'ensemble de la filière des accélérateurs.
> 🔄 **À revoir si** une technologie de mémoire offre simultanément la bande passante de l'empilement et la capacité de la mémoire classique.

**Renvois** — Couche : calculer · Convergences : énergie et calcul (40), intelligence distribuée (38).

---

## ◆◆◆ Calcul en mémoire

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Effectuer l'opération là où la donnée réside, au lieu de la déplacer vers une unité de calcul.

**Pourquoi on en parle.** Parce que c'est **la seule approche qui attaque frontalement la contrainte dominante de la couche** — si déplacer coûte des centaines de fois plus que traiter, la meilleure optimisation consiste à ne pas déplacer.

**Comment ça fonctionne.** Deux familles très différentes portent ce nom.

Le **calcul près de la mémoire** place des unités de calcul simples dans le composant mémoire lui-même. L'approche est modérée, compatible avec les procédés existants, et les gains sont réels sans être spectaculaires.

Le **calcul dans la mémoire** au sens strict utilise les propriétés physiques du réseau de cellules pour réaliser l'opération. Dans une matrice de cellules dont chacune stocke une valeur sous forme de conductance, appliquer des tensions en entrée produit, par simple addition de courants, le résultat d'une multiplication matricielle — **en une seule opération physique, sans qu'aucune donnée ne circule**. Le gain énergétique potentiel est d'un ou deux ordres de grandeur.

**Ce qui bloque.** **La précision.** L'approche stricte est analogique : la valeur stockée est une grandeur physique, donc bruitée, dérivant avec la température et variant d'une cellule à l'autre. **La précision atteignable est limitée et, surtout, elle n'est pas reproductible d'un exemplaire à l'autre** — ce qui pose des problèmes de conception, de test et de qualification que le numérique n'a pas.

S'y ajoutent la conversion entre analogique et numérique aux frontières du bloc, qui consomme et peut annuler le gain ; l'endurance en écriture des cellules ; et l'absence d'écosystème de conception.

**Ce que cela implique.** L'approche convient aux calculs **tolérants à une précision modeste** — ce qui inclut une partie des traitements d'apprentissage, où une précision réduite dégrade peu les résultats. Elle ne convient pas au calcul exact.

**À ne pas confondre avec.** **Le cache**, qui rapproche la donnée sans changer le lieu du calcul. **Le neuromorphique**, qui partage la colocalisation mais s'en distingue par le mode de communication.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrateurs et premiers composants commerciaux sur des niches ; adoption générale limitée par la précision et l'écosystème.
> 🔄 **À revoir si** un composant de calcul en mémoire atteint une précision suffisante pour une charge d'inférence courante, avec des performances reproductibles d'un exemplaire à l'autre.

**Renvois** — Couche : calculer · Convergences : énergie et calcul (40), intelligence distribuée (38) · Voir aussi : calcul analogique (ch. 9).

---

## ◆◆ Calcul à faible précision

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Représenter les nombres sur moins de bits, ce qui réduit simultanément l'énergie, la mémoire et le temps de transfert.

**Pourquoi on en parle.** Parce que c'est le levier d'efficacité le plus employé et le moins spectaculaire — il n'exige aucune rupture technologique et produit des gains d'un facteur significatif.

**Comment ça fonctionne.** Une multiplication sur des nombres courts coûte beaucoup moins d'énergie qu'une multiplication sur des nombres longs, et le gain est plus que proportionnel. Surtout, **la donnée occupe moins de place et se transfère plus vite** — ce qui attaque la contrainte dominante de la couche.

L'observation qui a rendu la technique possible est empirique : sur de nombreuses charges d'apprentissage, réduire la précision dégrade peu la qualité du résultat, à condition de traiter correctement les valeurs extrêmes.

**Ce que ça permet.** Exécuter un modèle plus grand dans la même mémoire · réduire l'énergie par requête · rendre possible l'exécution sur des appareils contraints.

**Ce qui bloque.** **La dégradation n'est pas uniforme** : certaines tâches y sont sensibles, et l'effet peut être invisible sur les tests courants tout en apparaissant sur des cas rares. C'est une forme de défaillance silencieuse : le système continue de produire des résultats plausibles avec une qualité légèrement dégradée que rien ne signale. S'y ajoute la prolifération de formats, qui fragmente l'écosystème.

**À ne pas confondre avec.** **Le calcul analogique**, dont l'imprécision est physique et non choisie. Ici, la précision est réduite délibérément et reste parfaitement reproductible.

> ⏱ **État au 23/08/2026** — 🏭 déployé, pratique standard. Les formats très courts sont supportés nativement par les accélérateurs récents.
> 🔄 **À revoir si** une méthode d'évaluation devient standard pour mesurer la dégradation induite sur les cas rares — ce qui rendrait l'arbitrage explicite plutôt qu'empirique.

**Renvois** — Couche : calculer · Convergence : intelligence distribuée (38).

---

## ◆ FPGA

**Niveau** — composant · **Couche** — calculer

**En une phrase.** Un circuit dont la fonction logique est configurée après fabrication, et reconfigurable ensuite.

**Où vous rencontrerez le terme.** Télécommunications · instrumentation · industrie · aéronautique et spatial · prototypage · traitement de signal à faible latence.

**Ce que ça permet.** Une latence très faible et déterministe · l'adaptation à un protocole ou à un traitement qui évolue · la production en petite série sans le coût d'un circuit dédié.

**Ce qui bloque.** **Le coût de développement.** Concevoir pour un FPGA relève de la conception matérielle et non de la programmation ; les compétences sont rares et les cycles longs. À grande série, un circuit dédié est plus efficace et moins cher.

**À ne pas confondre avec.** **L'ASIC**, figé mais optimal. **Le processeur**, programmable au sens logiciel. Le FPGA occupe une position intermédiaire : plus souple qu'un ASIC, plus efficace qu'un processeur, plus difficile à mettre en œuvre que les deux.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie mature. Concurrencé par les accélérateurs spécialisés sur les charges régulières, conservé pour la latence et l'adaptabilité.
> 🔄 **À revoir si** les outils de conception réduisent significativement le coût d'entrée en compétence.

**Renvois** — Couche : calculer.

---
