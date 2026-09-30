---
title: 'Chapitre 12 — Énergie : produire, convertir, stocker, transporter'
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 14
chapters: 53
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * énergie et puissance sont deux grandeurs distinctes, et leur confusion est la plus coûteuse du volume ;
> * densité d'énergie et densité de puissance s'opposent presque toujours.
>
> **À reconnaître :** facteur de charge · rendement aller-retour · inertie de réseau · plasma et confinement
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

C'est le chapitre le plus transversal de la carte. L'énergie contraint le calcul, la mobilité, la production industrielle, les capteurs, le spatial et le vivant. Ce qui s'y joue réapparaîtra partout.

## 12.1 Énergie et puissance : la confusion qui coûte le plus cher

Le chapitre 5 a posé la distinction ; il faut maintenant l'installer définitivement.

**L'énergie est un stock** : ce que contient un réservoir, ce qu'une usine consomme sur une année. Elle se mesure en joules ou en wattheures.

**La puissance est un flux** : ce qui est appelé ou fourni à un instant donné. Elle se mesure en watts, et un watt vaut un joule par seconde.

**Deux systèmes de même énergie et de puissance différente n'ont rien à voir.** Une batterie de 60 kWh qu'on charge en huit heures appelle environ 7,5 kW — un raccordement domestique renforcé. La même batterie chargée en cinq minutes appelle 720 kW — l'équivalent instantané d'une centaine de logements. Même énergie, deux problèmes d'infrastructure sans rapport.

**Où cette confusion fait le plus de dégâts :**

| Formulation courante | Ce qu'elle mélange |
|---|---|
| « une centrale de 1 GW » | une puissance ; l'énergie annuelle dépend du facteur de charge |
| « un stockage de 100 MW » | une puissance ; il faut aussi savoir combien d'heures (MWh) |
| « ce site consomme 500 MW » | une puissance appelée ; la facture porte sur des MWh |
| « la batterie fait 100 kWh » | une énergie ; ne dit rien de la puissance de charge ou de décharge |

**Règle : devant tout chiffre énergétique, demandez systématiquement l'autre grandeur.** Une puissance sans durée et une énergie sans puissance sont toutes deux incomplètes.

## 12.2 Densité d'énergie et densité de puissance : le compromis universel

Deux grandeurs distinctes, et leur confusion est presque aussi coûteuse que la précédente.

**La densité d'énergie** — combien on emporte par kilogramme ou par litre. Elle détermine l'autonomie.

**La densité de puissance** — à quelle vitesse on peut la restituer ou l'absorber. Elle détermine l'accélération, la charge rapide, la capacité de pointe.

**Ces deux qualités s'opposent presque toujours.** Un dispositif optimisé pour emporter beaucoup d'énergie restitue lentement ; un dispositif optimisé pour restituer vite emporte peu. C'est pourquoi certains systèmes associent deux technologies de stockage aux rôles complémentaires.

**Les ordres de grandeur qui structurent tout le raisonnement énergétique :**

| Support | Densité d'énergie approximative | Remarque |
|---|---|---|
| Essence, kérosène | environ 12 kWh/kg | mais rendement d'usage de 25 à 40 % |
| Hydrogène (masse seule) | environ 33 kWh/kg | le réservoir domine la masse et le volume |
| Batterie lithium-ion (cellule) | environ 0,15 à 0,25 kWh/kg | rendement d'usage supérieur à 90 % |
| Batterie (module complet) | nettement moins que la cellule | structure, refroidissement, électronique |
| Volant d'inertie, supercondensateur | très faible en énergie | très élevé en puissance |

⏱ *Ordres de grandeur, à réactualiser. Les valeurs de cellules progressent ; le rapport entre familles est durable.*

**Le calcul qui explique une grande partie du monde.** Un facteur d'environ soixante en énergie massique entre un carburant liquide et une cellule lithium-ion. Corrigé des rendements d'usage — environ 30 % contre plus de 90 % —, l'écart **utile** se resserre autour d'un facteur quinze à vingt.

Ce seul résultat explique deux choses opposées :

* pourquoi l'électrification de l'automobile fonctionne : la masse de batterie nécessaire, bien que considérable, reste compatible avec un véhicule routier ;
* pourquoi l'électrification de l'aviation long-courrier est un problème d'une tout autre nature : un avion doit emporter son énergie **et se sustenter**, et un facteur quinze sur l'énergie embarquée n'est pas absorbable par la conception.

**Une différence supplémentaire, souvent oubliée.** Un avion à carburant s'allège en volant ; un avion à batteries atterrit avec la masse du décollage. Cela change le dimensionnement du train d'atterrissage et de la structure — un exemple de contrainte qui n'apparaît pas dans la comparaison de densités.

## 12.3 Produire : les grandes filières et ce qui les contraint

L'objectif ici n'est pas d'être exhaustif ni de comparer les filières entre elles, mais d'identifier **ce qui contraint chacune**.

| Filière | Principe | Contrainte dominante |
|---|---|---|
| Thermique à combustion | brûler pour chauffer, détendre, entraîner | rendement borné par les températures ; combustible ; émissions |
| Nucléaire de fission | chaleur d'une réaction nucléaire | capital, durée de construction, cadre, déchets, acceptabilité |
| Hydraulique | énergie de l'eau en mouvement | sites disponibles, acceptabilité, hydrologie |
| Éolien | énergie du vent | intermittence, facteur de charge, foncier, réseau |
| Solaire photovoltaïque | conversion directe du rayonnement | intermittence, surface, stockage associé |
| Géothermie | chaleur du sous-sol | géologie locale, forage |

**Toutes les filières thermiques partagent la contrainte du chapitre 8** : la fraction de chaleur convertible en travail dépend de l'écart de température. C'est ce qui borne leurs rendements, indépendamment de la source de chaleur.

### Réaction nucléaire : le socle conceptuel

Deux mécanismes distincts, souvent confondus dans le vocabulaire courant.

**La fission** consiste à casser des noyaux lourds. Le processus libère des neutrons, qui peuvent provoquer d'autres fissions : c'est la réaction en chaîne, et l'enjeu du pilotage est de la maintenir stable. La technologie est industrialisée depuis des décennies ; ses difficultés sont de coût, de construction, de gestion des déchets et d'acceptabilité — c'est-à-dire des conditions ④, ⑥ et ⑧, non des conditions ① ou ②.

**La fusion** consiste à réunir des noyaux légers. C'est le mécanisme qui alimente les étoiles, et il libère davantage d'énergie par unité de masse. Sa difficulté est d'une autre nature : pour que les noyaux fusionnent, il faut vaincre leur répulsion électrique, donc les porter à des températures extrêmes — de l'ordre de la centaine de millions de degrés.

**À ces températures, la matière est un plasma** : un état où les électrons ne sont plus liés aux noyaux, et où l'ensemble est électriquement conducteur et sensible aux champs magnétiques. Aucun matériau ne peut le contenir par contact — il refroidirait le plasma et se détruirait. Il faut donc le **confiner** autrement, principalement par champs magnétiques, ou par compression très brève.

**Les difficultés qui en découlent, et il faut les nommer précisément** : maintenir le plasma stable assez longtemps ; obtenir plus d'énergie que celle injectée, en comptant l'ensemble de l'installation et non le seul plasma ; et tenir des matériaux soumis à un flux de neutrons intense pendant des années. Cette dernière contrainte est une contrainte de matériaux au sens du chapitre 11, et elle est souvent sous-estimée dans les discussions publiques.

**Où se situe la difficulté, en langage de ce cours.** Pour la fusion, la condition ① est acquise — le principe est établi — et la condition ② est atteinte dans certaines configurations. Les conditions ③ à ⑥ sont ouvertes. C'est exactement le type de situation que le Volume 2 analysera ; ce volume-ci vous donne le vocabulaire et s'arrête là.

⏱ *L'état d'avancement des programmes de fusion évolue ; ce paragraphe est écrit pour rester valide indépendamment.*

## 12.4 Convertir : les rendements se multiplient

Le chapitre 8 a établi le principe. Voici les rendements typiques à retenir.

| Conversion | Rendement approximatif |
|---|---|
| Électrique → mécanique (moteur) | 85 à 95 % |
| Mécanique → électrique (générateur) | 90 % et plus |
| Chimique → thermique → mécanique (moteur thermique) | 25 à 45 % |
| Électrique → chimique → électrique (batterie, aller-retour) | 85 à 95 % |
| Électrique → hydrogène (électrolyse) | 60 à 75 % |
| Hydrogène → électrique (pile à combustible) | 45 à 60 % |
| Conversion de tension (électronique de puissance) | 95 à 99 % |

⏱ *Ordres de grandeur variables selon technologies et conditions.*

**Deux enseignements.**

**La dernière ligne explique pourquoi l'électronique de puissance du chapitre 10 est stratégique.** Un composant présent dans presque toutes les chaînes, dont chaque point de rendement se multiplie avec tous les autres.

**Les chaînes longues sont pénalisées structurellement.** Le calcul du chapitre 8 le montrait : une chaîne à trois ou quatre conversions perd la moitié ou davantage. Toute proposition impliquant plusieurs conversions successives doit être évaluée sur son rendement **cumulé**, jamais sur celui de son meilleur maillon.

## 12.5 Stocker

**Le stockage est une conversion**, avec un rendement à l'aller et un au retour. C'est pourquoi on parle de rendement aller-retour.

| Famille | Principe | Densité d'énergie | Durée typique | Limite |
|---|---|---|---|---|
| Électrochimique | réaction réversible | moyenne | minutes à heures | cyclage, matériaux, température |
| Mécanique (pompage, volant) | énergie potentielle ou cinétique | faible | heures à jours | sites disponibles, encombrement |
| Thermique | chaleur stockée | variable | heures à mois | ne restitue que de la chaleur |
| Chimique (hydrogène, carburants) | molécule énergétique | élevée | mois | rendement aller-retour faible |

### Électrochimie : le principe, et ce qu'il implique

Une batterie déplace des ions d'une électrode à l'autre à travers un électrolyte, tandis que les électrons empruntent le circuit extérieur — c'est ce déplacement d'électrons qui constitue le courant utile. La charge inverse le processus.

**Ce qui limite une batterie, dans l'ordre d'importance pratique :**

* **les interfaces** — c'est aux frontières entre électrodes et électrolyte que se produisent la plupart des dégradations ;
* **le cyclage** — chaque cycle dégrade légèrement, et la durée de vie se compte en cycles, exactement comme la fatigue du chapitre 8 ;
* **la température** — le froid réduit temporairement les performances, la chaleur accélère durablement la dégradation ;
* **la puissance de charge** — charger vite dégrade davantage, ce qui est un arbitrage direct entre confort d'usage et durée de vie ;
* **l'emballement thermique** — le cas de panne fondateur du chapitre 8, dans sa forme la plus concrète : une dégradation locale échauffe, l'échauffement accélère la dégradation, et la boucle peut devenir incontrôlable.

**Ce qui explique pourquoi la sécurité d'un pack est un problème de conception système** et non de chimie seule : il faut détecter, isoler, refroidir, et éviter la propagation d'une cellule à ses voisines.

**La règle du chapitre 8 s'applique ici aussi** : ce qui vaut pour une cellule ne vaut pas pour un pack. Le passage de la cellule au module puis au pack ajoute structure, refroidissement, électronique de surveillance et connectique — et réduit la densité d'énergie effective de façon significative. **Comparer une densité de cellule à un besoin de véhicule est une erreur de niveau**, au sens du chapitre 2.

## 12.6 Le réseau électrique : un équilibre permanent

Point essentiel et mal connu : **le réseau électrique ne stocke rien**. À chaque instant, la production doit égaler la consommation, aux pertes près.

**La fréquence est la variable de survie.** Si la production dépasse la consommation, la fréquence monte ; si elle est inférieure, la fréquence baisse. Un écart trop important déclenche des protections, qui déconnectent des équipements, ce qui aggrave le déséquilibre. C'est un mécanisme d'effondrement en cascade.

**L'inertie amortit les écarts.** Les grandes masses tournantes des alternateurs classiques stockent de l'énergie cinétique et ralentissent la variation de fréquence, laissant le temps aux régulations d'agir. Les sources connectées par électronique de puissance ne fournissent pas naturellement cette inertie — elles peuvent l'émuler, mais c'est une fonction à concevoir et non une propriété physique offerte. **C'est un exemple où résoudre un problème — produire de l'électricité autrement — en révèle un autre qui n'existait pas.** Chapitre 32.

**La congestion.** L'électricité produite doit pouvoir être acheminée. Une capacité de production installée là où le réseau ne peut pas évacuer l'énergie est en partie inutilisable. Le chapitre 26 a montré ce que coûte le raccordement ; c'est le même sujet vu de l'autre côté.

**Cas de panne.** Une perte de production importante fait chuter la fréquence ; les protections déconnectent des charges et des producteurs ; chaque déconnexion modifie l'équilibre et peut en déclencher d'autres. L'ensemble peut se propager en quelques secondes — bien plus vite qu'aucune intervention humaine. Le redémarrage complet d'un réseau effondré est une opération longue et délicate, car il faut réalimenter progressivement en maintenant l'équilibre à chaque étape.

## 12.7 Facteur de charge, intermittence, coût système

**Le facteur de charge n'est pas un rendement.** Confusion fréquente et lourde de conséquences.

* Le **rendement** est la fraction de l'énergie entrante convertie en énergie utile.
* Le **facteur de charge** est la fraction de sa puissance nominale qu'une installation produit en moyenne sur l'année.

Une installation peut avoir un excellent rendement de conversion et un facteur de charge faible, simplement parce que sa ressource n'est pas disponible en permanence.

**Conséquence directe :** comparer des puissances installées sans comparer les facteurs de charge est dépourvu de sens. Un gigawatt d'une filière à facteur de charge élevé et un gigawatt d'une filière à facteur de charge faible ne produisent pas la même énergie annuelle, et l'écart peut être d'un facteur trois ou quatre.

**Intermittence et variabilité.** Une source variable impose au système de compenser : par du stockage, par des moyens pilotables, par de la flexibilité de la demande, ou par du réseau permettant de mutualiser sur une grande zone. Chacune de ces réponses a un coût, qui n'apparaît pas dans le coût de production de la source elle-même.

**D'où la notion de coût système**, introduite au chapitre 22 : le coût pertinent inclut ce que l'insertion d'une source impose au reste du système. **C'est le seul niveau auquel des filières différentes sont comparables**, et c'est aussi le niveau le plus difficile à établir — raison pour laquelle les comparaisons publiques se font rarement à ce niveau.

**Neutralité.** Les débats sur le mix énergétique sont légitimes et vifs. Ce cours ne prend pas position. Il affirme deux choses plus étroites : les comparaisons doivent se faire à périmètre identique, et une puissance installée n'est pas une énergie produite.

## 12.8 Chaleur et refroidissement

Le chapitre 8 l'a établi : tout finit en chaleur, et l'évacuer devient plus difficile à mesure qu'on grandit.

**Trois conséquences pratiques traversent tout le volume :**

**Le refroidissement consomme de l'énergie.** Un système de refroidissement est lui-même un consommateur, ce qui dégrade le rendement global et ajoute une boucle à surveiller.

**La chaleur résiduelle a une valeur qui dépend de sa température.** Une chaleur à quelques centaines de degrés est valorisable industriellement ; une chaleur à trente ou quarante degrés ne l'est presque pas, et sa valorisation suppose un besoin situé à proximité immédiate. C'est pourquoi la récupération de chaleur des installations informatiques est possible mais contrainte par la géographie.

**L'évacuation limite la densité.** Le chapitre 10 l'a montré à l'échelle de la puce ; le chapitre 13 le montrera à l'échelle du bâtiment. C'est la même contrainte à trois échelles.

## 12.9 Ce que cela implique

**Le passage à l'échelle.** L'énergie est le domaine où le facteur mille est le plus impitoyable : les quantités se comptent en ressources nationales, les infrastructures en décennies, et les décisions engagent des durées de vie de quarante ans ou davantage.

**Dépendances.** Cette famille dépend des matériaux et de la fabrication, de l'électronique de puissance, des chaînes d'approvisionnement minérales, du foncier et des autorisations. Tout le reste dépend d'elle — c'est la famille la plus en amont de la carte.

**Implication cyber.** Le pilotage des réseaux et des installations de production repose sur des systèmes numériques dont une défaillance produit des conséquences physiques immédiates et étendues. C'est le cas le plus net du volume où le logiciel agit directement sur le monde, et où les modèles de menace du système d'information ne suffisent pas — thème repris au chapitre 16.

🎓 **À ce stade, vous savez…**

* distinguer énergie et puissance et demander systématiquement la grandeur manquante ;
* opposer densité d'énergie et densité de puissance et expliquer pourquoi elles s'opposent ;
* calculer l'écart utile entre carburant et batterie et en déduire ce qui s'électrifie et ce qui résiste ;
* décrire fission et fusion, le plasma et le confinement, et situer chacune sur les neuf conditions ;
* multiplier des rendements de chaîne et refuser une évaluation sur le meilleur maillon ;
* nommer ce qui limite une batterie et pourquoi la sécurité d'un pack est un problème système ;
* expliquer l'équilibre permanent du réseau, le rôle de l'inertie et le mécanisme d'effondrement ;
* distinguer facteur de charge et rendement, et exiger une comparaison à coût système.

---

---

---
