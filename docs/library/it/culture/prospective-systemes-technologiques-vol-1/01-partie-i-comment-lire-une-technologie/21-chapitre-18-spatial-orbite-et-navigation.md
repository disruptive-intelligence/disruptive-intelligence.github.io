---
title: Chapitre 18 — Spatial, orbite et navigation
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
> * c'est la vitesse qui coûte, pas l'altitude — et la fraction de masse utile est de quelques pour cent ;
> * positionner, c'est mesurer du temps ; une grande partie du monde numérique en dépend.
>
> **À reconnaître :** orbite basse / géostationnaire · fraction de masse utile · fauchée · revisite · durcissement
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Cette famille a une particularité : une grande partie du monde technologique en dépend sans le savoir, à travers une fonction discrète — le temps et le positionnement.

## 18.1 Pourquoi atteindre l'orbite coûte cher

**Être en orbite n'est pas être haut.** C'est se déplacer horizontalement assez vite pour que la trajectoire de chute se referme autour de la Terre. L'altitude est secondaire ; **c'est la vitesse qui coûte**, et elle est considérable — de l'ordre de plusieurs kilomètres par seconde.

**Le problème de la masse emportée.** Un lanceur doit accélérer non seulement sa charge utile, mais aussi tout l'ergol qu'il n'a pas encore brûlé. Pour aller plus vite, il faut plus d'ergol, dont la masse doit elle-même être accélérée. Cette rétroaction est exactement celle du chapitre 16.5 — la boucle masse-énergie d'un système qui emporte son énergie — dans sa forme la plus sévère.

**La conséquence est brutale et gouverne toute la conception.** La fraction de la masse au décollage qui atteint l'orbite en tant que charge utile est de l'ordre de quelques pour cent. Tout le reste est de l'ergol et de la structure. **C'est pourquoi chaque kilogramme économisé sur la structure a une valeur disproportionnée, et pourquoi l'étagement existe** : se débarrasser en vol de la structure devenue inutile.

**Ce que cela dit du coût.** L'énergie théorique nécessaire pour porter un kilogramme en orbite est modeste rapportée au prix de l'électricité. Le coût réel est sans commune mesure : il vient de la masse de matériel dépensée, de la fiabilité exigée, des cadences faibles et de l'absence d'apprentissage industriel lorsqu'on ne produit que quelques exemplaires par an. **C'est un cas d'école du chapitre 22 : la loi de Wright ne s'applique pas quand la production cumulée reste faible** — et c'est ce qui rend la question de la réutilisation et de la cadence structurante, sujet que le Volume 2 traitera.

## 18.2 Les orbites et ce qu'elles déterminent

Le choix d'orbite détermine presque tout le reste du système.

| Type d'orbite | Altitude | Latence | Couverture par satellite | Durée de vie |
|---|---|---|---|---|
| Basse | quelques centaines de km | faible | étroite : il faut une constellation | limitée : traînée résiduelle |
| Moyenne | quelques milliers à ~20 000 km | intermédiaire | large | longue |
| Géostationnaire | environ 36 000 km | élevée | très large, position fixe vue du sol | très longue |

**Les compromis à retenir :**

**Latence contre couverture.** Le chapitre 8 le rappelle : la latence est bornée par la distance. Un satellite lointain impose un aller-retour de plusieurs centaines de millisecondes ; un satellite proche en impose peu, mais ne voit qu'une petite portion de la surface et défile rapidement — il faut donc en déployer beaucoup et gérer les passages de l'un à l'autre.

**Résolution contre altitude.** Le compromis du chapitre 8 s'applique : pour une même finesse de détail, plus on est loin, plus l'ouverture optique doit être grande. Une orbite basse permet une meilleure résolution à instrument égal.

**Durée de vie.** En orbite basse, l'atmosphère résiduelle freine les satellites, qui finissent par retomber. C'est à la fois une contrainte — durée de vie courte, donc renouvellement permanent — et une propriété utile : les débris y disparaissent naturellement, ce qui n'est pas le cas plus haut.

**La congestion orbitale.** Le nombre d'objets en orbite basse augmente rapidement. Chaque collision produit des débris, qui augmentent le risque de collisions ultérieures — une boucle de rétroaction qui, poussée assez loin, rendrait certaines orbites difficilement utilisables. C'est un problème de ressource commune : l'orbite est une ressource attribuée et non extensible, comme le spectre du chapitre 13. ⏱

## 18.3 L'environnement spatial

Quatre contraintes, dont la dernière change la nature de l'ingénierie.

**Le vide.** Pas de convection : la chaleur ne s'évacue que par rayonnement, ce qui est peu efficace. Le chapitre 8 avait posé les trois conditions de l'évacuation thermique ; ici, il n'en reste qu'une. **Le contrôle thermique est donc l'une des difficultés majeures de la conception d'un satellite**, ce qui surprend souvent.

**Les cycles thermiques.** Un satellite en orbite basse passe alternativement au soleil et à l'ombre, plusieurs fois par jour, avec des écarts de température considérables. Le chapitre 8 l'a établi : ce sont les cycles qui provoquent la fatigue.

**Le rayonnement.** Les particules énergétiques dégradent les matériaux et perturbent l'électronique. Un composant peut voir un bit basculer sous l'impact d'une particule — événement transitoire qui ne laisse aucune trace matérielle mais peut corrompre un calcul. D'où l'usage de composants durcis, souvent d'une génération technologique plus ancienne et volontairement moins dense, donc moins performants. **C'est un arbitrage explicite entre performance et robustesse**, et il explique pourquoi l'électronique spatiale paraît en retard.

**L'impossibilité de réparer.** C'est la contrainte qui change tout. Le chapitre 24 a établi que la disponibilité dépend autant du temps de réparation que du taux de panne ; ici, le temps de réparation est infini. **Toute la fiabilité doit donc être acquise avant le lancement**, ce qui impose des essais exhaustifs au sol, de la redondance, des marges importantes — et explique une part considérable du coût.

## 18.4 Communiquer

**Le bilan de liaison.** Établir une liaison suppose que le signal reçu se distingue du bruit — le rapport signal sur bruit du chapitre 8. Le signal s'affaiblit avec le carré de la distance ; les grandeurs disponibles pour compenser sont la puissance d'émission, la taille des antennes des deux côtés, et la réduction du débit.

**Le compromis central est donc :** débit, portée, taille d'antenne, puissance. On ne peut pas maximiser les quatre. **Un satellite lointain à petite antenne aura un débit faible**, quelle que soit la qualité de son électronique.

**Les fenêtres de visibilité.** Un satellite en orbite basse n'est visible d'une station donnée que quelques minutes par passage. Il faut donc soit multiplier les stations sol, soit relayer entre satellites, soit stocker à bord et transmettre plus tard. **La station sol est un complément au sens du chapitre 26** : elle n'appartient pas au satellite, elle coûte cher, et elle est souvent le facteur limitant réel du système.

**Les fenêtres atmosphériques du chapitre 8 s'appliquent** : certaines bandes traversent mieux l'atmosphère que d'autres, et les liaisons à très haute fréquence — y compris optiques — offrent de forts débits au prix d'une sensibilité aux nuages.

## 18.5 Observer depuis l'orbite

Quatre grandeurs, en tension permanente.

**La résolution** — la finesse du détail. Bornée par le rapport longueur d'onde sur ouverture, à l'altitude considérée.

**La revisite** — la fréquence de repassage au-dessus d'un même point. Un satellite unique en orbite basse repasse à intervalles longs ; une constellation raccourcit ce délai.

**La fauchée** — la largeur de la bande observée. Elle s'oppose à la résolution : un instrument très résolvant couvre une bande étroite.

**La bande spectrale** — le chapitre 14 l'a établi : selon la bande, on observe ce qui est éclairé, ce qui est chaud, ou ce qui est visible malgré les nuages.

**Le compromis résume tout le domaine :** résolution, revisite et fauchée s'opposent deux à deux. Améliorer les trois exige davantage de satellites, donc du coût — ce qui referme la boucle sur la section 18.1.

**La météo est une contrainte souvent oubliée.** Dans les bandes optiques, une couverture nuageuse rend l'observation impossible. Sur certaines régions, cela réduit considérablement le nombre d'images exploitables par an. Les bandes plus longues, qui traversent les nuages, offrent une résolution moindre à ouverture égale — retour au compromis du chapitre 8.

## 18.6 Positionnement, navigation et temps : la dépendance invisible

C'est le point le plus important du chapitre pour votre pratique.

**Le principe, énoncé au chapitre 14.5 :** des satellites porteurs d'horloges très stables émettent des signaux horodatés. Un récepteur compare les temps d'arrivée en provenance de plusieurs satellites et en déduit sa position. **Positionner, c'est mesurer du temps.**

**Ce qui rend cette infrastructure fragile, en trois points :**

**Le signal reçu est extrêmement faible.** Il provient d'émetteurs distants de milliers de kilomètres et arrive au sol à un niveau très bas — en dessous du bruit ambiant dans certaines conditions. Il est donc facilement perturbable, y compris involontairement.

**Il n'est pas authentifié dans ses formes civiles historiques.** Le chapitre 9 a établi la distinction : un signal peut être reçu correctement sans que rien n'atteste son origine.

**La dépendance est bien plus large que la navigation.** Réseaux de télécommunications, transactions financières, réseaux électriques, journaux d'événements, protocoles de sécurité : beaucoup de systèmes tirent leur référence de temps de cette source. **Une grande partie des infrastructures numériques dépend donc d'un signal spatial faible.**

**Le mode de défaillance est celui du chapitre 14.** En cas de perte du signal, les systèmes ne s'arrêtent pas tous : certains basculent sur une référence interne et **dérivent lentement**, d'autres continuent avec une position ou un temps faux. La dégradation est progressive, hétérogène et silencieuse — la pire combinaison pour un diagnostic.

**Les parades**, énoncées au niveau du principe : disposer d'une référence de temps locale de bonne stabilité, utiliser plusieurs constellations indépendantes, croiser avec des sources non spatiales, et surveiller la vraisemblance des mesures. Ce cours n'entre pas dans les techniques de perturbation ni de leurre, conformément à la règle de double usage.

## 18.7 Ce que cela implique

**Le passage à l'échelle.** Le spatial illustre à l'inverse le chapitre 22 : longtemps, la production restait de quelques unités par an, sans apprentissage industriel possible. Ce qui change une trajectoire dans ce domaine n'est donc pas d'abord une percée technique mais **un changement de régime de production** — cadence, réutilisation, standardisation. Le Volume 2 analysera cette trajectoire ouverte ; ce volume vous en donne le critère.

**Dépendances.** Cette famille dépend des matériaux, de l'électronique durcie, des lanceurs, des stations sol et d'attributions internationales — fréquences et positions orbitales. Et une part importante du monde numérique dépend d'elle pour le temps.

**Implication cyber.** Deux points, traités au niveau du principe : la **dépendance mondiale à un signal faible et historiquement non authentifié**, dont les conséquences systémiques sont considérables ; et le fait que les segments sol et les liaisons de commande constituent des systèmes informatiques classiques, avec les surfaces d'attaque correspondantes, mais dont la compromission a des conséquences physiques irréversibles au sens du chapitre 16.

## 🧪 Lab 7 — Que peut-on mesurer, et à quel prix
**Objectif.** Appliquer le compromis spectral et le triangle d'arbitrage à un besoin réel.
**Durée.** 75 minutes. **Difficulté.** 3/3. **Prérequis.** Chapitres 8, 13, 14, 18.
**Contexte.** Un besoin d'observation vous est décrit — un phénomène à détecter, une zone, une fréquence de mise à jour souhaitée, des conditions météorologiques locales. Aucune solution n'est proposée.

**Travail demandé.**
(a) Déterminer si le phénomène doit être observé par réflexion ou par émission, et en déduire la ou les bandes candidates.
(b) Dire ce que la météo locale élimine ou impose.
(c) Poser le compromis résolution / revisite / fauchée et dire lequel des trois doit être sacrifié compte tenu du besoin.
(d) Situer la solution sur l'échelle d'abstraction : brique, plateforme ou système ?
(e) Identifier deux modes de défaillance silencieuse de la chaîne de mesure envisagée.

**Livrable.** Une page, plus un tableau des compromis.

**Éléments attendus.** En (a), le raisonnement compte plus que la conclusion. En (c), la bonne réponse dépend du besoin et doit être justifiée par lui — une copie qui maximise les trois n'a pas compris le chapitre 14.2. En (d), la réponse attendue est « système » : un besoin d'observation récurrent suppose une chaîne complète, et non un capteur. En (e), au moins une des deux défaillances doit porter sur l'étalonnage ou la dérive, non sur une panne franche.

---

🎓 **À ce stade, vous savez…** expliquer pourquoi c'est la vitesse et non l'altitude qui coûte, et ce qu'implique la fraction de masse utile ; choisir une orbite en fonction du compromis latence-couverture-résolution ; nommer les quatre contraintes de l'environnement spatial et dire pourquoi l'irréparabilité change l'ingénierie ; poser un bilan de liaison en termes de compromis ; opposer résolution, revisite et fauchée ; expliquer pourquoi positionner c'est mesurer le temps, et pourquoi cette dépendance est fragile et large.

---
