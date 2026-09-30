---
title: Chapitre 9 — Calculer autrement
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 6
chapters: 14
---

> **Ce que ce chapitre ajoute.** Le chapitre 8 optimisait à l'intérieur du paradigme électronique numérique. Celui-ci en sort — par le support, par la représentation, ou par le mode de communication.
>
> **Une observation commune aux six entrées.** Aucune ne bute principalement sur la physique. **Toutes butent sur l'écosystème** : outils de conception, compilateurs, bibliothèques, méthodes de test, personnes formées, base installée. C'est le mécanisme le plus important de ce chapitre, et il commande la lecture de chaque fiche.

---

### ◆◆◆ Photonique intégrée

**Niveau** — composant · **Couche** — calculer, relier

**En une phrase.** Réaliser sur une puce des fonctions optiques — guider, moduler, détecter la lumière — en utilisant les procédés de la microélectronique.

**Pourquoi on en parle.** Parce qu'elle attaque le coût du déplacement des données à courte distance, et parce qu'elle est passée récemment du laboratoire à la production en volume.

**Comment ça fonctionne.** On grave dans le silicium des guides d'onde qui conduisent la lumière comme des pistes conduisent le courant. On y ajoute des modulateurs, des multiplexeurs et des détecteurs. Le silicium n'émettant pas efficacement de lumière, la source laser est généralement rapportée — c'est l'une des difficultés d'intégration du domaine.

**L'intérêt vient de trois propriétés.** La lumière ne dissipe pas dans le guide comme un courant dans un conducteur. Plusieurs longueurs d'onde peuvent coexister dans le même guide, multipliant la capacité. Et la consommation d'une liaison optique dépend peu de la distance, contrairement à une liaison électrique.

**Où vous rencontrerez le terme.** Centres de calcul · liaisons entre puces · capteurs · télécommunications · instrumentation.

**Ce que ça permet.** Remplacer des liaisons électriques par des liaisons optiques **à l'intérieur des équipements**, là où la densité et la consommation deviennent limitantes — ce qui est un déplacement récent, l'optique ayant longtemps été réservée aux longues distances.

**Ce qui bloque.** **Le seuil de conversion.** Passer de l'électronique à l'optique et revenir coûte de l'énergie et du temps. En dessous d'une certaine distance et d'un certain débit, ce coût dépasse le gain du transport optique. **C'est ce seuil qui détermine où la photonique gagne**, et il se déplace à mesure que les composants s'améliorent — c'est la grandeur à surveiller.

S'y ajoutent l'intégration de la source laser, la sensibilité en température, et l'alignement optique, qui exige des précisions submicrométriques en assemblage.

**Ce que cela implique.** La photonique **n'est pas une alternative au calcul électronique** : c'est une technologie d'interconnexion qui repousse un mur. Elle gagne progressivement du terrain vers l'intérieur des systèmes, et sa progression se mesure par une distance décroissante — celle en dessous de laquelle l'électrique reste préférable.

**À ne pas confondre avec.** **Le calcul photonique**, traité séparément : effectuer l'opération dans le domaine optique est un problème entièrement différent de transporter l'information optiquement.

**Termes voisins.** *Silicon photonics* · *optique co-packagée* désigne l'intégration au plus près du processeur.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les liaisons de centre de calcul, 🔬 émergent pour l'intégration au plus près du processeur, en industrialisation rapide.
> 🔄 **À revoir si** l'optique co-packagée devient l'architecture par défaut des accélérateurs de grande taille.

**Renvois** — Couche : calculer, relier · Convergence : énergie et calcul (40).

---

### ◆◆ Calcul photonique

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Effectuer l'opération elle-même dans le domaine optique, plutôt que de convertir en électronique pour calculer.

**Comment ça fonctionne.** Certaines opérations se prêtent naturellement à une réalisation optique. Faire passer un faisceau à travers un réseau d'éléments qui l'atténuent et le recombinent réalise, physiquement, une multiplication matricielle — à la vitesse de la lumière et sans consommation liée à l'opération elle-même.

**Ce que ça permet.** Un débit d'opérations très élevé sur des calculs réguliers, avec une consommation potentiellement très inférieure.

**Ce qui bloque.** **Les mêmes trois obstacles que le calcul analogique**, dont il est une variante physique : la **précision** est limitée et sensible aux conditions ; la **conversion** aux entrées et sorties consomme et peut annuler le gain ; et il n'existe **aucune mémoire optique** pratique, ce qui oblige à revenir dans le domaine électronique entre les étapes.

Ce dernier point est décisif : le calcul photonique excelle sur une opération isolée et perd son avantage dès qu'il faut chaîner.

**Ce que cela implique.** L'approche vise des niches où le motif de calcul est fixe, régulier et tolérant à l'imprécision. Elle ne vise pas le remplacement d'un processeur.

**À ne pas confondre avec.** **La photonique intégrée**, qui transporte. La confusion est fréquente et coûteuse : la première est déployée, le second est prospectif.

> ⏱ **État au 23/08/2026** — 🔭 prospectif, avec des démonstrateurs et quelques produits de niche.
> 🔄 **À revoir si** un système photonique démontre un avantage net sur une charge complète — et non sur une opération isolée — conversions comprises.

**Renvois** — Couche : calculer · Convergence : énergie et calcul (40).

---

### ◆◆◆ Neuromorphique

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Des architectures inspirées de l'organisation du système nerveux : calcul et mémoire colocalisés, communication par impulsions brèves, activité déclenchée par l'événement plutôt que par une horloge.

**Pourquoi on en parle.** Parce que le terme est employé pour des objets très différents, et parce que l'approche attaque simultanément les deux contraintes de la couche : le déplacement des données et l'énergie.

**Comment ça fonctionne.** Trois principes, qui peuvent être adoptés séparément — d'où la confusion.

**La colocalisation** : chaque unité de calcul possède sa propre mémoire locale, supprimant les transferts longue distance.

**La communication par impulsions** : les unités n'échangent pas des valeurs continues mais des impulsions brèves, dont l'information réside dans l'instant d'émission. Une unité qui n'a rien à dire ne consomme rien.

**Le fonctionnement événementiel** : il n'y a pas d'horloge globale ; l'activité se déclenche à l'arrivée d'un événement. Sur des données naturellement éparses, la consommation chute d'un ou deux ordres de grandeur.

**Ce que ça permet.** Un traitement continu à très faible consommation, particulièrement adapté aux flux d'événements — reconnaissance de motifs sur signaux, traitement de sorties de caméras événementielles, surveillance permanente sur alimentation contrainte.

**Ce qui bloque.** **L'entraînement.** Les méthodes qui ont fait le succès de l'apprentissage profond supposent des grandeurs continues et différentiables ; les impulsions ne le sont pas. On contourne par conversion depuis un réseau classique, au prix d'une partie du gain, ou par des méthodes spécifiques encore moins matures.

S'y ajoute **l'absence complète d'écosystème** : outils, formats, jeux de données, métriques et compétences ont tous été construits pour le paradigme dominant.

**Ce que cela implique.** C'est l'entrée qui illustre le mieux l'observation d'ouverture du chapitre : **le verrou n'est pas physique, il est écosystémique.** Les composants existent et fonctionnent ; ce qui manque est tout ce qui permettrait de les utiliser sans être spécialiste.

**À ne pas confondre avec.** **Les réseaux de neurones artificiels courants**, qui s'exécutent sur du matériel conventionnel et n'ont d'inspiration biologique que le nom. **Le calcul analogique**, avec lequel le neuromorphique se combine souvent sans se confondre.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Puces disponibles auprès de plusieurs acteurs, applications de niche établies en traitement de signal à très faible consommation, adoption générale absente.
> 🔄 **À revoir si** une méthode d'entraînement native atteint des performances comparables au paradigme dominant sur une tâche de référence reconnue.

**Renvois** — Couche : calculer · Convergence : intelligence distribuée (38) · Voir aussi : caméras événementielles (ch. 6).

---

### ◆◆ Calcul analogique

**Niveau** — capacité · **Couche** — calculer

**En une phrase.** Représenter une valeur par une grandeur physique continue — tension, courant, charge, conductance — et laisser la physique effectuer le calcul.

**Comment ça fonctionne.** Additionner deux courants réalise une addition, sans aucune opération logique. Le calcul devient une propriété du circuit plutôt qu'une séquence d'instructions. C'est l'approche historique, abandonnée au profit du numérique dans les années 1960 pour une raison précise.

**Cette raison est toujours valable.** Le numérique n'est pas plus fidèle que l'analogique : il est **plus stable**. En ne conservant que deux niveaux largement séparés, il recopie l'information à l'identique indéfiniment, tant que le bruit reste sous le seuil de décision. L'analogique renonce à cette protection : chaque étape ajoute du bruit, et les erreurs s'accumulent.

**Ce que ça permet.** Une efficacité énergétique très supérieure sur des opérations simples et massivement répétées.

**Ce qui bloque.** **La précision et sa non-reproductibilité.** Deux exemplaires du même circuit ne donnent pas exactement le même résultat — variations de fabrication, dérive en température, vieillissement. Cela impose un étalonnage par exemplaire, complique le test, et rend délicate toute qualification. C'est la contrainte que le volume 1 identifiait comme propre à cette famille.

**Ce que cela implique.** L'analogique revient là où **l'imprécision est tolérable et l'énergie critique** — c'est-à-dire dans une partie de l'inférence embarquée. Il ne revient pas dans le calcul exact, et cette frontière est stable.

**À ne pas confondre avec.** **La faible précision numérique**, qui est un choix reproductible et contrôlé.

> ⏱ **État au 23/08/2026** — 🔬 émergent, essentiellement sous la forme du calcul en mémoire.
> 🔄 **À revoir si** une technique d'étalonnage automatique rend les performances reproductibles à l'échelle d'une production de série.

**Renvois** — Couche : calculer.

---

### ◆ Calcul supraconducteur

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Utiliser des circuits supraconducteurs, sans résistance électrique, pour commuter à très haute fréquence en dissipant très peu.

**Ce qui bloque.** **Le refroidissement.** Ces circuits fonctionnent à quelques kelvins ; l'énergie dépensée pour les maintenir à cette température dépasse largement celle qu'ils économisent, sauf à très grande échelle. S'y ajoutent l'absence de mémoire dense compatible et un écosystème inexistant.

**À ne pas confondre avec.** **Le calcul quantique à supraconducteurs**, qui utilise des circuits similaires mais pour un tout autre principe — il s'agit ici de logique classique très rapide, pas de qubits.

> ⏱ **État au 23/08/2026** — 🔭 prospectif. Domaine de recherche ancien, applications limitées à l'instrumentation.
> 🔄 **À revoir si** la cryogénie devient de toute façon nécessaire à grande échelle pour une autre raison — le coût du refroidissement serait alors déjà payé.

**Renvois** — Couche : calculer.

---

### ◆ Architectures non von Neumann

**Niveau** — cadrage · **Couche** — calculer

**En une phrase.** Terme générique désignant toute architecture qui s'écarte de la séparation classique entre une mémoire, une unité de calcul et un flux d'instructions.

**Ce qu'il faut en savoir.** **C'est un terme fourre-tout**, défini par ce qu'il n'est pas. Il recouvre le calcul en mémoire, le neuromorphique, les architectures à flot de données et plusieurs autres approches qui n'ont en commun ni leurs principes, ni leurs verrous, ni leurs applications.

**À ne pas confondre avec.** Une famille technologique. Employé dans une phrase du type « les architectures non von Neumann vont remplacer », le terme ne désigne rien de vérifiable.

**Ce qu'il vous fait manquer.** **Lequel des trois murs est attaqué.** Chaque approche vise une contrainte précise — le déplacement, l'énergie, ou la nature du problème. Le terme générique efface cette distinction, qui est la seule qui compte.

> ⏱ **État au 23/08/2026** — sans objet : cadrage et non technologie.

**Renvois** — Couche : calculer.

---


## Chapitre 10 — Le quantique

> **Ce que ce chapitre ajoute.** Les chapitres 8 et 9 traitaient de manières de calculer plus efficacement. Celui-ci traite d'une machine qui ne calcule pas de la même façon — et dont la portée est bien plus étroite, et bien plus profonde, que le discours public ne le laisse entendre.
>
> **Trois entrées seulement**, dont deux majeures. C'est délibéré : le domaine se comprend par trois objets, et le découper davantage produirait des répétitions.
>
> **Un renvoi important.** Les **capteurs quantiques** sont traités au chapitre 7, dans la couche *percevoir*. Ce n'est pas un oubli : c'est l'application de la règle des couches, et c'est la distinction la plus utile de tout le domaine.

---

### ◆◆◆ Calcul quantique

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

### ◆◆◆ Correction d'erreur quantique

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

### ◆◆ Communications quantiques

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


## Clôture de la couche B — Calculer

### Ce que les quinze entrées font apparaître

**Un. Le verrou de cette couche est presque toujours l'écosystème, pas la physique.** Sur les six entrées du chapitre 9, six butent principalement sur les outils, les compilateurs, les méthodes de test et les compétences. Une alternative doit être meilleure **d'un facteur** pour absorber ce coût — ce qui explique pourquoi elles percent d'abord dans des niches où le calcul classique est particulièrement mauvais, jamais en concurrence frontale.

**Deux. Le mur de la mémoire structure tout le chapitre 8.** Cinq entrées sur six l'attaquent : l'assemblage rapproche, la mémoire empilée élargit, le calcul en mémoire supprime le déplacement, la faible précision réduit le volume à déplacer. Seul le FPGA relève d'une autre logique. **C'est la démonstration la plus nette de l'atlas qu'une contrainte unique peut organiser un domaine entier.**

**Trois. Trois entrées de cette couche sont classées 🔭 prospectif** — calcul photonique, calcul supraconducteur, calcul quantique. C'est la proportion la plus élevée de tout l'atlas, et elle est cohérente : c'est la couche où l'on tente de sortir d'un paradigme qui fonctionne.

**Quatre. Le déplacement du goulet est observable à l'intérieur même de la couche.** La fabrication a cédé la place à l'assemblage, qui a cédé la place à la mémoire, qui cède la place à l'énergie et au refroidissement — et, à l'échelle du bâtiment, au raccordement électrique. **Le dossier 40 traitera cette chaîne complète.**

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | accélérateurs, calcul en mémoire, faible précision, neuromorphique, mémoires à forte bande passante |
| **40 — Énergie et calcul** | accélérateurs, chiplets, mémoires, calcul en mémoire, photonique intégrée, calcul photonique |

**Le dossier 40 mobilise six entrées de cette seule couche** — et son maillon en retard est pourtant le raccordement électrique, qui relève de la couche *alimenter*. **Deuxième vérification de la thèse du volume.**

---

---

---

### Couche C — Apprendre et décider

---


## Chapitre 11 — Les modèles au-delà du chatbot

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé l'échange fondamental : l'apprentissage troque de la certitude contre de la capacité. Ce chapitre traite des **objets** qui réalisent cet échange — comment ils sont construits, ce qui borne leur performance, et ce qu'ils coûtent à l'usage.
>
> **Une discipline propre à cette couche.** Aucune fiche ne nomme de modèle, d'acteur ni de score. Ce n'est pas de la prudence : c'est la condition pour que ces fiches restent valides dans trois ans. Les états sont qualitatifs, et c'est ce qui les rend durables.
>
> **Six entrées**, dont deux majeures.

---

### ◆◆◆ Modèles de fondation

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

### ◆◆◆ Modèles de raisonnement

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Des modèles qui consacrent davantage de calcul à produire une réponse, en décomposant le problème avant de conclure.

**Pourquoi on en parle.** Parce que c'est le déplacement le plus significatif de la période : le calcul est passé de l'entraînement vers l'usage — et parce que le mot « raisonnement » induit en erreur.

**Comment ça fonctionne.** Plutôt que de produire directement une réponse, le modèle génère une suite d'étapes intermédiaires, explore plusieurs pistes, revient sur certaines, puis conclut. Il consomme donc davantage à chaque requête, et cette dépense supplémentaire améliore effectivement les résultats sur des tâches à structure logique ou mathématique.

**Ce qui compte pour bien comprendre.** Ce déplacement ouvre un **arbitrage nouveau** : à performance donnée, on peut soit entraîner un modèle plus grand une fois, soit dépenser davantage à chaque appel. Le second choix est réversible et se règle par usage ; le premier est un investissement.

**Ce que ça permet.** Des résultats nettement meilleurs sur des tâches où la réponse directe échouait · un réglage du compromis qualité-coût requête par requête.

**Ce qui bloque.** **Le coût par requête**, qui devient la variable dominante d'un service très utilisé. **La latence**, une réponse longue à produire étant incompatible avec certains usages interactifs. Et **la vérification** : les étapes produites ne constituent pas une démonstration vérifiable.

**Ce que cela implique.** Ce qui est produit **ressemble** à un raisonnement sans en avoir les propriétés : le modèle peut atteindre la bonne conclusion par un chemin faux, et inversement. Les étapes intermédiaires sont une aide à la performance, pas une justification opposable — distinction décisive dès qu'une décision doit être motivée.

**À ne pas confondre avec.** **Une démonstration formelle**, vérifiable mécaniquement. **L'explicabilité** : produire des étapes n'est pas expliquer une décision.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Devenu une modalité standard, avec un réglage explicite du budget de calcul par requête chez plusieurs fournisseurs.
> 🔄 **À revoir si** les gains obtenus par allocation de calcul à l'inférence cessent de croître avec le budget alloué.

**Renvois** — Couche : apprendre et décider · Courants : modèles de raisonnement (ch. 32) · Convergence : découverte scientifique (37).

---

### ◆◆ Multimodalité

**Niveau** — capacité · **Couche** — percevoir, apprendre et décider

**En une phrase.** Traiter conjointement plusieurs types d'entrées — texte, image, son, vidéo, signaux — dans une représentation commune.

**Comment ça fonctionne.** Chaque modalité est convertie en une suite de vecteurs, puis projetée dans un espace partagé où la proximité traduit une similarité d'usage. Le modèle apprend les correspondances entre modalités à partir de données appariées — une image et sa description, un son et sa transcription.

**Ce que ça permet.** Interroger une image par du texte · relier une observation à une instruction · produire une commande à partir d'une scène — ce dernier point étant le fondement des architectures traitées au chapitre 13.

**Ce qui bloque.** **L'appariement des données.** Il faut des exemples où plusieurs modalités décrivent la même chose, et ces jeux sont bien plus rares que les corpus mono-modaux. **L'alignement temporel et spatial** quand les entrées viennent de capteurs distincts — c'est le problème de recalage de la couche *percevoir*, et c'est là que la chaîne échoue en pratique. Et le **déséquilibre** : une modalité dominante peut masquer les autres.

**Ce que cela implique.** Un système multimodal n'est pas plus fiable qu'un système mono-modal : **il hérite des défaillances de chaque capteur** et y ajoute celles de la combinaison.

**À ne pas confondre avec.** **La fusion de capteurs** (ch. 7), qui combine des mesures physiques avec un modèle d'incertitude explicite. Ici, la combinaison est apprise et son incertitude n'est pas explicitée.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour texte et image, 🔬 émergent pour l'intégration de signaux physiques hétérogènes.
> 🔄 **À revoir si** l'ajout d'une modalité issue de capteurs physiques produit un gain mesuré sur une tâche de décision en conditions réelles.

**Renvois** — Couche : percevoir, apprendre et décider · Convergence : robotique généraliste (36).

---

### ◆◆ Mémoire et contexte long

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

### ◆◆ Modèles compacts

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

### ◆◆ Données synthétiques

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


## Chapitre 12 — Agents et autonomie logicielle

> **Ce que ce chapitre ajoute.** Le chapitre 11 traitait de modèles qui produisent une réponse. Celui-ci traite de systèmes qui **entreprennent** — qui décomposent un objectif, invoquent des outils, observent le résultat et poursuivent.
>
> **Une entrée conditionne les quatre autres.** La distinction entre automatisation, agentivité et autonomie n'est pas une subtilité de vocabulaire : elle détermine ce qu'il faut prouver, ce qu'un assureur exigera, et qui répond en cas de dommage. Elle est traitée en premier.

---

### ◆◆◆ Automatisation, agentivité, autonomie

**Niveau** — cadrage analytique · **Couche** — décider

**En une phrase.** Trois régimes distincts, qui n'appellent ni les mêmes preuves, ni les mêmes garanties, ni les mêmes responsabilités — et que le vocabulaire courant confond.

**Pourquoi cette entrée existe.** Parce que c'est la distinction la plus opérationnelle de toute la couche, et qu'aucun terme du marché ne la porte.

**Les trois régimes.**

**L'automatisation.** Le système exécute une séquence définie à l'avance. Toutes les situations prévues ont une réponse spécifiée ; les autres provoquent un arrêt ou une alerte. **Ce qu'il faut prouver** : que la séquence est correcte et que les situations non prévues sont bien détectées. C'est un problème de vérification classique, et il se traite.

**L'agentivité.** Le système décompose un objectif en étapes qu'il choisit, dans un espace d'actions défini par son concepteur. Il ne sort pas de cet espace, mais l'enchaînement n'est pas prévu à l'avance. **Ce qu'il faut prouver** : que l'espace d'actions est correctement borné, et qu'aucune combinaison d'actions autorisées ne produit un effet inacceptable. **C'est beaucoup plus difficile**, parce que le nombre de combinaisons croît de façon explosive.

**L'autonomie.** Le système décide dans des situations non prévues, y compris celle de s'arrêter, de renoncer ou d'alerter. **Ce qu'il faut prouver** : qu'il reconnaît qu'il sort du domaine où son comportement a été validé — ce qui est le problème le plus difficile de la couche, et le sujet du chapitre 30.

**Où passe la frontière, en pratique.** La question à poser n'est pas « ce système est-il autonome ? » mais : **que fait-il quand il rencontre une situation à laquelle il n'a pas de réponse ?** Un système qui s'arrête est automatisé. Un système qui essaie autre chose dans son répertoire est agentique. Un système qui décide d'une action hors répertoire — y compris ne rien faire et prévenir — est autonome.

**Ce que cela implique.** Chaque régime déplace la charge de la preuve, et l'écart de coût entre les trois est considérable. **Beaucoup de produits présentés comme autonomes sont agentiques ; beaucoup de produits présentés comme agentiques sont automatisés** avec une interface en langage naturel.

**À ne pas confondre avec.** **Les niveaux d'autonomie** définis dans certains secteurs, qui décrivent le partage de tâches entre humain et machine plutôt que la nature de la décision. Les deux grilles sont utiles et ne mesurent pas la même chose.

> ⏱ **État au 23/08/2026** — cadrage, sans état de maturité. La confusion des trois régimes est répandue et s'aggrave avec la diffusion du terme « agentique ».
> 🔄 **À revoir si** un référentiel sectoriel adopte une distinction équivalente, ce qui la rendrait opposable.

**Renvois** — Couche : décider · Courants : Agentic AI, autonomous systems, machine autonomy (ch. 32-33) · Convergence : autonomie mobile (39) · Voir aussi : architecture de sûreté (ch. 30).

---

### ◆◆◆ Agents IA

**Niveau** — capacité et architecture · **Couche** — apprendre et décider, relier

**En une phrase.** Un système qui poursuit un objectif en enchaînant des appels à un modèle et des actions sur des outils extérieurs, en tenant compte des résultats obtenus.

**Pourquoi on en parle.** Parce que c'est le déplacement structurant de la période : du modèle qui répond au système qui agit.

**Comment ça fonctionne — quatre éléments.** Une **boucle** qui alterne raisonnement et action. Un **répertoire d'outils** — recherche, exécution de code, appels à des services, actions sur une interface. Une **mémoire de travail** conservant l'état de la tâche. Et un **critère d'arrêt**, qui est le plus difficile à concevoir correctement.

**Où vous rencontrerez le terme.** Développement logiciel · traitement documentaire · relation client · analyse · exploitation informatique · progressivement dans les processus métier.

**Ce que ça permet.** Déléguer une tâche entière plutôt qu'une étape · traiter des tâches dont la décomposition n'est pas connue à l'avance · agir sur des systèmes existants sans les modifier.

**Ce qui bloque.** **La propagation d'erreur.** Un système qui enchaîne dix étapes offre dix occasions de se tromper, et une erreur intermédiaire se propage **sans se signaler** — elle produit une suite d'actions cohérentes fondées sur une prémisse fausse. Le taux de succès d'une tâche complète décroît donc rapidement avec le nombre d'étapes, même quand chaque étape est très fiable.

**Le coût de vérification.** Vérifier le résultat d'un agent demande parfois autant de travail que la tâche elle-même — ce qui annule le gain.

**La surface d'action.** Un agent qui agit sur des systèmes réels peut produire des effets difficiles à défaire. La question du périmètre d'action et de sa réversibilité est une question de conception, pas de réglage.

**Ce que cela implique.** L'arbitrage central n'est pas la capacité du modèle mais **le rapport entre la valeur de la tâche déléguée et le coût de vérification du résultat**. Les usages qui réussissent sont ceux où la vérification est bon marché — parce que le résultat est testable, ou parce que l'erreur est peu coûteuse et rattrapable.

**Sûreté et sécurité.** Injection d'instructions par les contenus traités · périmètre d'action et principe de moindre privilège · traçabilité des actions · réversibilité. **Un agent hérite des droits qu'on lui confie**, et c'est une décision d'architecture, pas un paramètre.

**À ne pas confondre avec.** **L'automatisation de processus** classique, dont l'enchaînement est fixe. **Un assistant**, qui propose sans agir.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion rapide. Usages établis là où la vérification est bon marché ; adoption prudente sur les processus à conséquence, pour des raisons de vérification et non de capacité.
> 🔄 **À revoir si** le taux de succès sur des tâches à nombreuses étapes devient assez élevé pour rendre la vérification exhaustive inutile.

**Renvois** — Couche : apprendre et décider · Courant : Agentic AI (ch. 32) · Convergence : découverte scientifique (37).

---

### ◆◆ Systèmes multi-agents

**Niveau** — système · **Couche** — apprendre et décider, relier

**En une phrase.** Plusieurs agents spécialisés qui se répartissent une tâche et coordonnent leurs actions.

**Ce que ça permet.** Spécialiser chaque composant · paralléliser · isoler les droits d'accès par rôle, ce qui est un argument de sécurité au moins autant que de performance.

**Ce qui bloque.** **La coordination coûte.** Les échanges entre agents consomment du contexte, donc du calcul et de la latence ; au-delà d'un certain nombre, le coût de coordination dépasse le gain de spécialisation. **Le diagnostic** devient difficile : quand le résultat est faux, identifier quel agent a introduit l'erreur suppose une traçabilité que peu de systèmes fournissent. Et **les erreurs se renforcent** : un agent peut confirmer l'erreur d'un autre, produisant une convergence trompeuse.

**À ne pas confondre avec.** **Les essaims** (ch. 16), où la coordination est locale et sans centre. Ici, l'architecture est généralement dirigée.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Architectures répandues dans les produits, bénéfice net encore débattu au-delà de quelques agents.
> 🔄 **À revoir si** une méthode de traçabilité rend le diagnostic d'erreur aussi praticable que dans un système à agent unique.

**Renvois** — Couche : apprendre et décider, relier.

---

### ◆◆ Service autonomy

**Niveau** — capacité organisationnelle · **Couche** — décider, vérifier

**En une phrase.** La capacité d'un service à se maintenir en fonctionnement, se corriger et s'adapter sans intervention humaine de routine.

**Où vous rencontrerez le terme.** Exploitation informatique · télécommunications · industrie · services financiers · progressivement dans les processus administratifs.

**Ce que ça permet.** Réduire le délai de correction · absorber des variations de charge · libérer du temps humain pour les exceptions.

**Ce qui bloque.** **Le mode dégradé.** Un service autonome doit savoir ce qu'il fait quand il ne sait plus quoi faire — et à qui il le signale, dans quel délai. C'est la question la plus difficile et la moins traitée. S'y ajoute **la reprise en main** : un opérateur qui supervise un service fiable depuis des heures n'est pas en état de reprendre le contrôle en quelques secondes.

**Ce que cela implique.** Ce n'est pas une absence d'équipe mais un **déplacement du travail** : de l'exécution vers la conception des règles, la supervision des exceptions et l'analyse d'incidents. Les compétences requises augmentent en niveau et diminuent en volume — ce qui est une transformation d'organisation, pas un projet technique.

**À ne pas confondre avec.** **L'automatisation d'exploitation**, qui exécute des procédures définies sans décider.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Déployé sur des périmètres restreints et bien caractérisés ; extension limitée par la question du mode dégradé.
> 🔄 **À revoir si** un référentiel d'exploitation intègre des exigences explicites de comportement en mode dégradé pour les services autonomes.

**Renvois** — Couche : décider, vérifier · Courant : service autonomy (ch. 33) · Voir aussi : dégradation maîtrisée (ch. 30).

---

### ◆◆ Opérations autonomes

**Niveau** — doctrine · **Couche** — décider

**En une phrase.** L'application de l'automatisation décisionnelle à l'exploitation d'infrastructures — détection, diagnostic, correction.

**Ce que ça permet.** Détecter des anomalies dans des volumes de signaux qu'aucune équipe ne peut surveiller · corriger des incidents connus sans intervention · anticiper des défaillances par l'observation de dérives.

**Ce qui bloque.** **Le comportement en incident majeur.** Un système qui se répare seul en régime courant peut **aggraver** un incident systémique en propageant des reconfigurations. C'est le mode de défaillance qui compte, et il est difficile à tester puisqu'il ne se produit que rarement. S'y ajoute la difficulté de distinguer une anomalie d'un changement légitime.

**Ce que cela implique.** L'autonomie d'exploitation est **plus sûre sur les incidents fréquents et plus risquée sur les incidents rares** — exactement l'inverse de l'intuition, et cohérent avec ce que le volume 1 a établi sur les queues de distribution.

**À ne pas confondre avec.** **La supervision**, qui observe et alerte sans agir.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour la détection, 🔬 émergent pour la correction automatique sur périmètre critique.
> 🔄 **À revoir si** un mécanisme de limitation de propagation devient une pratique standard, rendant traitable le risque d'aggravation.

**Renvois** — Couche : décider · Courant : autonomous networks (ch. 34).

---


## Chapitre 13 — Apprendre le monde physique

> **Ce que ce chapitre ajoute.** Les chapitres 11 et 12 traitaient de systèmes agissant sur de l'information. Celui-ci traite de systèmes qui produisent **des commandes destinées à des actionneurs** — et cela change la nature des contraintes.
>
> **Trois différences avec le monde logiciel.** Une erreur n'est pas toujours rattrapable. Les données ne se collectent pas en ligne mais s'acquièrent une interaction à la fois. Et le monde ne se réinitialise pas.
>
> **Sept entrées.** C'est le chapitre le plus directement lié au dossier de convergence 36.

---

### ◆◆◆ Modèles du monde

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Un modèle qui apprend à prédire l'évolution d'un environnement, de sorte qu'un système puisse anticiper les conséquences d'une action avant de l'exécuter.

**Pourquoi on en parle.** Parce que c'est la réponse proposée au problème de coût des données physiques : si un système peut simuler intérieurement les conséquences de ses actions, il peut apprendre sans agir.

**Comment ça fonctionne.** Le modèle est entraîné à prédire l'état suivant à partir de l'état courant et de l'action envisagée. Une fois cette prédiction assez fiable, le système peut **dérouler mentalement** plusieurs séquences d'actions et choisir celle dont le résultat prédit est le meilleur — sans les exécuter.

**Ce que ça permet.** Réduire le nombre d'interactions réelles nécessaires · anticiper au lieu de réagir · évaluer une action risquée sans la tenter.

**Ce qui bloque.** **L'accumulation d'erreur de prédiction.** Chaque pas prédit introduit une erreur, et prédire loin revient à composer ces erreurs : au-delà de quelques pas, la prédiction diverge. L'horizon utile est donc court, et l'étendre est le sujet actif.

**La physique du contact** est particulièrement difficile à prédire : au moment où deux objets se touchent, la dynamique change brutalement et de faibles écarts de position produisent des résultats très différents.

**Et une difficulté de fond** : le modèle prédit ce qu'il a observé. Face à une situation inhabituelle, il produit une prédiction plausible et fausse — sans le signaler.

**Ce que cela implique.** Un modèle du monde ne supprime pas le besoin de données réelles : **il l'exporte vers la validation**. Il faut vérifier que les prédictions correspondent au réel, ce qui exige d'agir dans le réel.

**À ne pas confondre avec.** **Un simulateur physique**, construit à partir d'équations connues et non appris. **Un jumeau numérique** (ch. 34), qui est synchronisé sur un système existant et n'a pas vocation à généraliser.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Résultats convaincants sur horizon court et environnements maîtrisés ; extension à des environnements ouverts non établie.
> 🔄 **À revoir si** un modèle du monde permet un apprentissage de manipulation en environnement varié avec un volume d'interactions réelles réduit d'un ordre de grandeur.

**Renvois** — Couche : apprendre et décider · Courants : Physical AI, embodied AI (ch. 33) · Convergences : robotique généraliste (36), autonomie mobile (39).

---

### ◆◆◆ VLA — Vision-Language-Action

**Niveau** — architecture · **Couche** — percevoir, apprendre et décider, agir

**En une phrase.** Une architecture qui prend en entrée une observation visuelle et une instruction en langage, et produit directement une commande motrice.

**Pourquoi on en parle.** Parce que c'est **l'objet technique concret derrière le cadrage « Physical AI »** — et parce que le terme circule largement sans que son contenu soit clair.

**Comment ça fonctionne.** Le principe est de traiter la commande motrice comme une modalité de sortie parmi d'autres. Le modèle reçoit une image et une instruction, les projette dans une représentation commune, et produit une séquence d'actions — positions articulaires, déplacements, ouvertures de préhenseur — de la même manière qu'un modèle de langage produit une suite de mots.

**Ce que cela change.** Auparavant, un robot enchaînait des modules séparés : perception, puis planification, puis contrôle. Chaque interface entre modules était un endroit où l'information se perdait. Une architecture VLA **supprime ces interfaces** en apprenant la correspondance de bout en bout — c'est le pari, et c'est aussi ce qui rend le comportement difficile à analyser quand il échoue.

**Où vous rencontrerez le terme.** Robotique · humanoïdes · manipulation · publications et communications sur la Physical AI.

**Ce que ça permet.** Exécuter une instruction formulée en langage naturel sur une tâche non spécifiquement programmée · transférer partiellement une compétence d'un objet à un objet similaire · réduire le travail d'ingénierie par tâche.

**Ce qui bloque.** **Les données.** Il faut des exemples associant observation, instruction et action réelle, et ils s'acquièrent une démonstration à la fois — par téléopération, le plus souvent. Il n'existe aucun équivalent physique d'un corpus textuel collecté en ligne, et **c'est le verrou central**.

**Le transfert entre plateformes.** Les données collectées sur un robot ne se transposent pas directement sur un autre, dont la géométrie et la dynamique diffèrent. Cela fragmente l'effort de collecte.

**La fiabilité.** Les taux de succès démontrés sur des tâches variées restent très en dessous de ce qu'exige une exploitation sans surveillance, et l'écart se creuse quand l'environnement s'écarte des conditions d'entraînement.

**Ce que cela implique.** Un VLA est **une architecture, pas un robot** — c'est la confusion à éviter absolument. Et sa progression se mesure moins par les démonstrations que par deux grandeurs : le volume de données d'interaction disponible et le degré de transfert entre plateformes.

**À ne pas confondre avec.** **Un modèle vision-langage**, qui décrit une scène sans produire d'action. **Un humanoïde** (ch. 15), qui est une plateforme. **Physical AI** (ch. 33), qui est un cadrage englobant.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrations nombreuses sur des tâches variées en environnement maîtrisé ; efforts de constitution de jeux de données partagés entre laboratoires et industriels ; pas de déploiement autonome en exploitation.
> 🔄 **À revoir si** un jeu de données d'interaction physique partagé entre plusieurs plateformes atteint une taille permettant un transfert mesurable d'une plateforme à une autre.

**Renvois** — Couche : percevoir, apprendre, agir · Courants : Physical AI, embodied AI (ch. 33) · Convergence : robotique généraliste (36).

---

### ◆◆ Embodied AI

**Niveau** — cadrage · **Couche** — percevoir, apprendre, agir

**En une phrase.** La thèse selon laquelle un système apprenant doté d'un corps et interagissant avec un environnement acquiert des capacités qu'un système traitant uniquement des données ne peut acquérir.

**Ce qu'il faut en savoir.** C'est **une hypothèse scientifique avant d'être une catégorie de produits**, et elle a une histoire académique de plusieurs décennies. Son intérêt pratique est de rappeler que certaines compétences — anticiper une conséquence physique, adapter une force, comprendre une occlusion — s'apprennent difficilement sans agir.

**Ce qui bloque.** **Le coût de l'incarnation.** Apprendre par interaction suppose du matériel, du temps réel, de l'usure et des erreurs coûteuses. C'est ce qui rend le domaine lent comparé à l'apprentissage sur données.

**À ne pas confondre avec.** **Humanoïde.** Un bras fixe, un drone, un véhicule sont des systèmes incarnés. **C'est la confusion la plus fréquente du domaine**, et elle conduit à surestimer l'importance de la forme.

> ⏱ **État au 23/08/2026** — cadrage, avec des travaux actifs. Les résultats les plus solides restent obtenus en environnement contraint.
> 🔄 **À revoir si** un apprentissage par interaction produit une capacité qu'aucun apprentissage sur données n'a permis d'obtenir, de façon reproductible.

**Renvois** — Couche : percevoir, apprendre, agir.

---

### ◆◆ Apprentissage par imitation

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Apprendre une tâche en reproduisant des démonstrations effectuées par un opérateur humain.

**Comment ça fonctionne.** Un opérateur exécute la tâche, souvent par téléopération, pendant que le système enregistre observations et actions. Le modèle apprend ensuite à produire l'action associée à chaque observation.

**Ce que ça permet.** Acquérir une compétence sans la spécifier · exploiter le savoir-faire d'un opérateur qui ne saurait pas l'expliciter · démarrer un apprentissage sans définir de fonction de récompense.

**Ce qui bloque.** **La dérive.** Le système apprend à agir dans les situations que l'humain a rencontrées ; dès qu'il s'en écarte un peu, il se retrouve dans des situations non démontrées, où il agit mal, ce qui l'en écarte davantage. **L'erreur s'auto-amplifie**, et c'est le problème structurel de la méthode.

S'y ajoutent le **coût de collecte** — une démonstration à la fois — et le fait que les démonstrations humaines contiennent des corrections implicites difficiles à reproduire.

**Ce que cela implique.** C'est **la source principale des données physiques** aujourd'hui, et donc le facteur limitant des architectures du chapitre. La téléopération n'est pas un pis-aller : c'est l'infrastructure de collecte.

**À ne pas confondre avec.** **L'apprentissage par renforcement**, qui apprend par essai et récompense sans démonstration.

> ⏱ **État au 23/08/2026** — 🏭 déployé en recherche et en pré-industrialisation, méthode dominante pour la manipulation.
> 🔄 **À revoir si** une méthode de collecte permet d'acquérir des démonstrations à un coût significativement inférieur à la téléopération individuelle.

**Renvois** — Convergence : robotique généraliste (36) · Voir aussi : téléopération (ch. 15).

---

### ◆◆ Apprentissage par renforcement

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Apprendre par essais successifs, guidé par un signal de récompense qui indique si le résultat est meilleur ou moins bon.

**Ce que ça permet.** Découvrir des stratégies qu'aucun humain n'aurait démontrées · optimiser un comportement selon un critère explicite · s'améliorer au-delà de la performance des démonstrations.

**Ce qui bloque.** **La conception de la récompense.** Le système optimise exactement ce qu'on mesure, ce qui n'est jamais exactement ce qu'on veut — et il trouve des moyens inattendus de maximiser la mesure sans atteindre l'objectif. **Le nombre d'essais** : en environnement physique, les essais coûtent du temps, de l'usure et parfois du matériel, ce qui pousse à apprendre en simulation. Et **la sécurité pendant l'apprentissage**, qui interdit l'exploration libre sur un système réel.

**Ce que cela implique.** En robotique, le renforcement s'emploie presque toujours **en simulation puis transféré**, ce qui déplace la difficulté vers l'entrée suivante.

**À ne pas confondre avec.** **L'ajustement sur préférences** utilisé pour les modèles de langage, qui emploie des techniques voisines pour un problème différent.

> ⏱ **État au 23/08/2026** — 🏭 déployé, méthode établie. Emploi en environnement physique généralement médié par la simulation.
> 🔄 **À revoir si** un apprentissage direct sur système physique devient praticable en toute sécurité et en un nombre d'essais raisonnable.

**Renvois** — Couche : apprendre et décider.

---

### ◆◆◆ Sim-to-real

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

### ◆◆ Modèles de fondation robotiques

**Niveau** — plateforme · **Couche** — apprendre et décider, agir

**En une phrase.** Un modèle pré-entraîné sur de larges volumes de données d'interaction physique, destiné à être adapté à des plateformes et des tâches variées.

**Ce que ça permet.** Mutualiser l'effort de collecte entre acteurs · réduire le travail d'adaptation par plateforme · faire bénéficier une tâche nouvelle de compétences acquises ailleurs.

**Ce qui bloque.** **L'hétérogénéité des plateformes.** Contrairement au texte, où un corpus est universel, les données physiques sont liées à une géométrie, une dynamique et un jeu de capteurs. Constituer un socle transférable suppose d'abstraire ces différences — et c'est un problème ouvert.

S'y ajoute la **taille des données disponibles**, sans commune mesure avec celle des corpus textuels.

**Ce que cela implique.** Si ce socle se constitue, il déplace le verrou du dossier 36 : la collecte cesserait d'être refaite par chaque acteur. **C'est le signal le plus important à surveiller dans toute cette couche.**

**À ne pas confondre avec.** **Un VLA**, qui est une architecture. Un modèle de fondation robotique peut employer une architecture VLA, ou une autre.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Plusieurs initiatives de mutualisation de données entre laboratoires et industriels ; transfert entre plateformes partiel.
> 🔄 **À revoir si** un modèle pré-entraîné sur données mutualisées surpasse, sur une plateforme donnée, un modèle entraîné uniquement sur les données de cette plateforme.

**Renvois** — Convergence : robotique généraliste (36).

---


## Clôture de la couche C — Apprendre et décider

### Ce que les dix-huit entrées font apparaître

**Un. Le verrou de cette couche s'est déplacé de la capacité vers la vérification.** Sur dix-huit entrées, onze ont pour verrou principal non pas ce que le système sait faire, mais **le coût de vérifier ce qu'il a produit** — propagation d'erreur des agents, dégradation non uniforme des modèles compacts, dérive des données synthétiques, prédiction plausible et fausse d'un modèle du monde. Ce n'est pas une limite de performance : c'est une limite d'exploitabilité.

**Deux. Les données physiques sont le facteur limitant du chapitre 13, et rien d'autre.** Cinq entrées sur sept y renvoient. C'est cohérent avec l'hypothèse du squelette de convergence, et cela confirme que le dossier 36 doit trancher entre fiabilité et données — les deux étant liés par la même contrainte.

**Trois. Aucune entrée de cette couche n'est classée ◆ de reconnaissance.** C'est la seule couche de l'atlas dans ce cas. Toutes les notions y sont soit majeures, soit standard — signe que le domaine n'a pas encore produit de périphérie, ce qui est un indicateur de jeunesse plutôt que d'importance.

**Quatre. La distinction automatisation / agentivité / autonomie est la fiche la plus opérationnelle de tout l'atlas jusqu'ici.** Elle ne décrit aucune technologie et détermine ce qu'il faut prouver, ce qu'un assureur exigera, et qui répond en cas de dommage.

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **36 — Robotique généraliste** | modèles du monde, VLA, imitation, renforcement, sim-to-real, modèles robotiques, multimodalité, données synthétiques |
| **37 — Découverte scientifique** | modèles de fondation, raisonnement, agents, données synthétiques |
| **38 — Intelligence distribuée** | modèles compacts, contexte, multimodalité |
| **39 — Autonomie mobile** | modèles du monde, sim-to-real, automatisation/agentivité/autonomie |
| **41 — Biologie programmable** | modèles de fondation |

**Le dossier 36 mobilise huit entrées de cette couche**, davantage que de la couche *agir* elle-même. C'est un résultat inattendu : la convergence dite « robotique » dépend plus fortement de l'apprentissage que de la mécanique — ce qui nuance, sans l'annuler, la contradiction partielle relevée au squelette.

---

---

---

### Couche D — Agir

---
