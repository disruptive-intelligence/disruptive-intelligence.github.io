---
title: 'Chapitre 19 — Calcul non classique : socle conceptuel minimal'
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * chaque approche attaque un mur physique précis — aucune n'attaque tous les murs ;
> * sortir du calcul classique coûte la totalité d'un écosystème, ce qui exige un gain d'un facteur, pas de quelques pourcents.
>
> **À reconnaître :** qubit physique / logique · décohérence · seuil de conversion électron-photon · calcul en mémoire
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

**Avertissement au lecteur.** Ce chapitre est volontairement bref, et il s'arrête là où les autres continuent. Aucune des approches présentées ici n'a de trajectoire close : ce sont des sujets dont l'issue est ouverte, et l'analyse de trajectoires ouvertes appartient au second volume. Ce chapitre pose le vocabulaire et les mécanismes, pour que vous puissiez lire ces sujets sans les confondre. Il ne comporte ni comparaison d'acteurs, ni projection de calendrier, ni affirmation de suprématie.

## 19.1 Pourquoi chercher autre chose

Trois murs, tous rencontrés dans les chapitres précédents, motivent la recherche d'alternatives au calcul électronique classique.

**Le mur de la mémoire** (chapitre 9) : déplacer une donnée coûte plusieurs centaines de fois plus que la traiter, et cet écart s'est creusé.

**Le mur de l'énergie** (chapitre 10) : la densité de puissance limite ce qu'on peut faire fonctionner simultanément, et l'évacuation thermique borne le reste.

**La nature des problèmes.** Certains problèmes se prêtent mal à une exécution séquentielle d'opérations élémentaires, quelle que soit la vitesse de la machine.

Les approches qui suivent attaquent chacune l'un de ces murs. Aucune ne les attaque tous.

## 19.2 Le quantique

**Le principe, en quatre notions.**

**Le qubit.** Un système quantique à deux états qui, contrairement à un bit, peut se trouver dans une **superposition** de ces deux états — une combinaison des deux, avec des poids.

**La mesure détruit la superposition.** Lorsqu'on observe un qubit, on obtient l'un des deux états, avec une probabilité déterminée par les poids. **On ne peut pas lire une superposition.** C'est la contrainte fondamentale du domaine, et elle explique pourquoi le calcul quantique n'est pas simplement un calcul parallèle massif : l'information est là, mais elle n'est pas directement accessible.

**L'intrication.** Plusieurs qubits peuvent être corrélés de telle façon que leur état ne se décrit pas indépendamment. C'est cette propriété, plus que la superposition seule, qui donne au calcul quantique sa puissance potentielle.

**La décohérence.** Un système quantique interagit inévitablement avec son environnement, et cette interaction détruit progressivement la superposition et l'intrication. **La décohérence est l'ennemi principal**, et elle impose l'isolement extrême — températures très basses, blindages, vide — qui caractérise ces machines.

**Qubit physique et qubit logique — la distinction essentielle.** Les qubits physiques sont bruités et fragiles. Pour effectuer un calcul long, il faut corriger les erreurs en permanence. Les schémas de correction connus consistent à encoder l'information d'un qubit **logique** — fiable — sur un grand nombre de qubits **physiques**, avec un facteur de multiplication considérable.

**Conséquence directe pour votre lecture.** Un nombre de qubits annoncé ne signifie rien s'il ne précise pas de quel type de qubits il s'agit, avec quel taux d'erreur et quelle durée de cohérence. C'est un cas typique du chapitre 6 : une métrique unique, impressionnante, qui n'établit pas ce qu'on lui fait dire. **La question à poser est : physiques ou logiques, avec quel taux d'erreur ?**

## 19.3 Ce que le quantique ne fera pas

Section nécessaire, parce que les attentes diffuses sur ce sujet sont considérables.

**Ce n'est pas un accélérateur général.** Il n'existe pas d'avantage quantique pour un calcul quelconque. Les gains théoriques connus concernent des familles de problèmes précises, à structure particulière. Pour l'immense majorité des tâches informatiques courantes, une machine quantique n'apporterait rien.

**Cela ne remplacera pas les machines classiques.** Les usages envisagés sont des accélérations ciblées, dans des architectures où une machine classique conduit le calcul et délègue certaines étapes.

**Cela ne rend pas tout calculable.** Ce qui est impossible en théorie de la calculabilité le reste.

**Le point qui concerne directement votre domaine.** Certaines hypothèses de difficulté sur lesquelles reposent des mécanismes cryptographiques largement déployés seraient affaiblies par une machine quantique suffisamment grande et fiable. Le chapitre 9 a posé le raisonnement complet : la sécurité repose sur des hypothèses, une hypothèse peut tomber, et la migration cryptographique est un problème d'infrastructure et de base installée, non de logiciel. **La conséquence pratique ne dépend donc pas d'une date : elle dépend de la durée pendant laquelle vos données doivent rester confidentielles**, puisqu'une donnée capturée aujourd'hui peut être déchiffrée plus tard.

## 19.4 La photonique

**Pourquoi la lumière.** Elle se propage vite, ne dissipe pas dans le milieu de propagation comme le fait un courant dans un conducteur, et permet de faire coexister plusieurs canaux dans le même support en utilisant des longueurs d'onde différentes.

**Où c'est déjà gagné.** Pour la transmission sur toute distance significative, la fibre optique a remplacé le cuivre depuis longtemps — chapitre 13. Ce n'est pas un sujet ouvert : c'est une technologie déployée.

**Où c'est ouvert.** L'utilisation de la lumière pour le calcul lui-même, ou pour les liaisons courtes à l'intérieur des machines et entre puces.

**La difficulté centrale : la conversion.** L'information calculée est électronique ; la transporter optiquement suppose de convertir électron vers photon, puis photon vers électron. Chaque conversion coûte de l'énergie et du temps. **En dessous d'une certaine distance et d'un certain débit, le coût des conversions dépasse le gain du transport.** C'est ce seuil qui détermine où la photonique gagne, et il se déplace à mesure que les composants s'améliorent.

**Ce qui rend le sujet intéressant.** Le mur de la mémoire est un problème de déplacement de données. La photonique attaque directement ce déplacement. Le Volume 2 examinera si et où le seuil bascule.

## 19.5 Neuromorphique et analogique

**Le principe commun.** Plutôt que de représenter des nombres par des symboles binaires et de les manipuler par des opérations logiques, on utilise une grandeur physique continue — une tension, un courant, une charge — pour représenter directement la valeur, et on laisse la physique effectuer le calcul.

**Le gain potentiel.** Certaines opérations qui demandent de nombreuses étapes en numérique se font en une seule opération physique, avec une consommation très inférieure.

**Le problème central : la précision.** Le chapitre 9 l'a annoncé. Une grandeur physique est bruitée, elle dérive avec la température, elle varie d'un composant à l'autre. Le numérique s'affranchit de ces défauts en ne conservant que deux niveaux, largement séparés. **L'analogique renonce à cette protection.** La précision atteignable est donc limitée, et surtout **elle n'est pas reproductible d'un exemplaire à l'autre** — ce qui pose des problèmes de conception, de test et de qualification que le chapitre 24 vous permet d'évaluer.

**Où cela peut convenir.** Aux calculs tolérants à une précision modeste — ce qui inclut une partie des traitements d'apprentissage, où l'on a constaté qu'une précision réduite dégrade peu les résultats.

**Le neuromorphique** désigne des architectures inspirées de l'organisation du système nerveux : traitement distribué, communication par événements brefs plutôt que par valeurs continues, mémoire et calcul colocalisés. Son intérêt principal, pour ce cours, est qu'il attaque simultanément le mur de la mémoire et celui de l'énergie.

## 19.6 Le calcul en mémoire

**Le raisonnement est direct.** Si déplacer une donnée coûte plusieurs centaines de fois plus que la traiter, alors la meilleure optimisation consiste à ne pas la déplacer. On cherche donc à effectuer l'opération là où la donnée est stockée.

**Ce que cela suppose.** Des dispositifs de mémoire capables de participer au calcul, ce qui relève souvent des approches analogiques de la section précédente, avec leurs limites de précision.

**Pourquoi c'est structurellement intéressant.** C'est la seule des approches présentées ici qui attaque directement le goulet identifié au chapitre 9 comme le plus contraignant aujourd'hui. Que ce soit une raison suffisante pour qu'elle s'impose est une question de trajectoire — et donc du Volume 2.

## 19.7 Ce que ces approches partagent

**Le vrai obstacle n'est pas la physique.** Il est dans ce que le chapitre 27 a nommé.

Le calcul électronique classique bénéficie de décennies d'accumulation : des chaînes de fabrication amorties, des outils de conception matures, des langages, des compilateurs, des bibliothèques, des millions de personnes formées, des méthodes de test, des normes. **Une approche alternative n'a rien de tout cela**, et doit le reconstruire.

> **Résout / coûte.** Sortir du calcul électronique classique : *résout* un mur physique spécifique · *coûte* la totalité de l'écosystème — fabrication, outils de conception, logiciel, compétences, méthodes de test, et la base installée de tout ce qui existe déjà.

**Ce que cela signifie pour l'analyse.** Une alternative doit être meilleure **d'un facteur**, pas de quelques pourcents, pour absorber ce coût — c'est exactement la quatrième porte de sortie du chapitre 27.6. C'est pourquoi ces approches percent d'abord, quand elles percent, dans des **niches où le calcul classique est particulièrement mauvais**, plutôt qu'en concurrence frontale. C'est la troisième porte : le nouveau segment.

**Ce que vous devez savoir faire maintenant.** Devant une annonce concernant l'une de ces approches, poser les quatre questions du chapitre 4 et, en particulier : de quel goulet spécifique s'agit-il, quel est le facteur d'amélioration réel sur ce goulet, quelle est la précision ou la fiabilité obtenue, et quel écosystème existe déjà. Le Volume 2 fera ce travail ; vous en avez ici les instruments.

🎓 **À ce stade, vous savez…** nommer les trois murs qui motivent la recherche d'alternatives ; définir qubit, superposition, mesure, intrication et décohérence ; distinguer qubit physique et logique et refuser un décompte non qualifié ; énoncer ce que le quantique ne fera pas et formuler correctement l'enjeu cryptographique ; identifier le seuil de conversion qui détermine où la photonique gagne ; expliquer le compromis précision-énergie de l'analogique ; dire pourquoi le calcul en mémoire attaque le goulet le plus contraignant ; et évaluer ce que coûte de sortir d'un écosystème dominant.

---

---

---
