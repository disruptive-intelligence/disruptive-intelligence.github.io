---
title: Chapitre 6 — L'administration de la preuve technologique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Ce chapitre est le plus important de la Partie I, et probablement celui dont vous vous servirez le plus souvent.

Le chapitre 5 vous a donné de quoi évaluer les affirmations qui se calculent. La plupart n'en font pas partie. Une vidéo, un benchmark, un rendement record, une feuille de route, un communiqué de résultats : rien de tout cela ne se réfute par une division. Il faut un autre instrument — la capacité à déterminer **ce qu'une preuve donnée permet réellement d'établir**.

> **P2 — Une démonstration prouve ce que son protocole permet de conclure, pas ce que son récit suggère.**

## 6.1 L'échelle des preuves

Entre « c'est possible » et « une industrie gagne de l'argent avec ça », il existe une douzaine d'échelons. Chacun est un franchissement réel, et aucun n'implique le suivant.

| Échelon | Ce qu'il établit | Ce qu'il n'établit pas |
|---|---|---|
| **Publication scientifique** | un résultat obtenu selon un protocole décrit | qu'il est reproductible ailleurs |
| **Réplication indépendante** | que le résultat ne tenait pas au laboratoire d'origine | qu'il tient hors des conditions du protocole |
| **Benchmark** | une performance sur une tâche standardisée | que la performance se transfère à la tâche réelle |
| **Prototype** | que l'objet peut exister | qu'il peut être fabriqué, ni qu'il durera |
| **Démonstrateur** | que l'objet fonctionne devant un public | dans quelles conditions, ni avec quel taux de succès |
| **Pilote** | que ça fonctionne chez un utilisateur réel, sur un périmètre limité | que ça tient à l'échelle ni dans la durée |
| **Produit** | qu'il existe une version vendable | qu'elle se vend |
| **Production série** | qu'on sait fabriquer en quantité, à un rendement donné | que c'est rentable |
| **Client payant** | qu'il existe une demande solvable | son ampleur |
| **Revenu** | l'ampleur de cette demande | la marge |
| **Marge** | que l'activité est viable | qu'elle est réplicable ailleurs |
| **Déploiement industriel** | que le système entier fonctionne | rien de plus — c'est le sommet de l'échelle |

Deux règles d'usage.

**Situer avant de discuter.** Devant une affirmation, votre premier réflexe doit être : *à quel échelon sommes-nous ?* La question est presque toujours plus informative que le contenu de l'affirmation elle-même.

**Ne jamais franchir un échelon gratuitement.** Chaque saut demande une justification. « Le prototype fonctionne, donc le produit arrivera » est un saut de cinq échelons, dont chacun a fait échouer des projets bien financés.

## 6.2 L'échelle des annonces

Parallèlement à l'échelle des preuves, il existe une échelle des **déclarations**, qui ne prouvent rien sur la technologie mais renseignent sur l'émetteur.

| Type | Ce que cela établit |
|---|---|
| Objectif annoncé | ce que l'entreprise souhaite faire |
| Feuille de route | ce qu'elle prévoit, sans engagement contractuel |
| Levée de fonds | que des investisseurs ont accepté un risque à un prix donné |
| Communiqué de presse | ce que l'entreprise veut faire savoir, et quand |
| Projection de marché | l'hypothèse d'un cabinet, généralement extrapolée |
| Résultats financiers publiés | des faits comptables, audités, opposables |

La dernière ligne est différente des autres, et c'est une astuce professionnelle utile : **les documents financiers réglementés sont beaucoup plus fiables que les communiqués de presse**, parce qu'ils engagent juridiquement leur émetteur. Le chapitre 1 en donnait un exemple — c'est dans la publication de résultats du troisième trimestre 2022, pas dans un communiqué de communication, que Ford a inscrit la dépréciation de 2,7 milliards de dollars sur Argo AI et reconnu que l'échéance de 2021 n'avait pas tenu.

> **Une annonce d'entreprise est une source légitime sur ce que l'entreprise affirme. Elle n'est pas une source sur ce qui est démontré.**

## 6.3 Ce qu'une vidéo de démonstration ne dit pas

La vidéo est la forme de preuve la plus persuasive et la moins informative. Elle montre qu'une chose est arrivée au moins une fois. Elle ne dit rien de la fréquence, des conditions, ni du degré d'intervention humaine.

### Cinq questions à poser à toute vidéo

1. **Combien de prises ?** Une réussite sur une prise et une réussite sur cinquante donnent la même vidéo.
2. **Quelle vitesse de lecture ?** L'accélération est courante et rarement signalée.
3. **Quel environnement ?** Préparé, cartographié, éclairé, dégagé — ou quelconque ?
4. **Quelle part d'intervention humaine ?** Téléopération, assistance à distance, opérateur hors champ.
5. **Que se passe-t-il quand ça rate ?** Une démonstration ne montre jamais son mode de défaillance, qui est pourtant l'information la plus utile.

### Cas documenté — l'événement « We, Robot », octobre 2024

**Les faits.** Lors de l'événement organisé par Tesla le 10 octobre 2024, plusieurs robots humanoïdes Optimus servaient des boissons, dansaient et conversaient avec les invités. Dans les jours qui suivent, Bloomberg, *The Verge* et d'autres rapportent que les interactions étaient largement téléopérées par des employés à distance ; l'analyste Adam Jonas, de Morgan Stanley, écrit que les robots reposaient sur de la téléopération. Selon les sources citées par Bloomberg, les prototypes marchaient de façon autonome, mais de nombreuses interactions avec le public étaient supervisées à distance. Une séquence filmée par un participant montre un robot barman reconnaissant lui-même être assisté par un humain.

**Ce que la démonstration prouvait réellement.** Que la marche autonome fonctionnait. Que la mécanique et la fluidité gestuelle étaient bonnes. Que la chaîne de téléopération fonctionnait — ce qui est un résultat d'ingénierie réel, pas rien.

**Ce qu'elle ne prouvait pas.** La manipulation autonome, la conversation autonome, ni la capacité à opérer sans opérateur humain — c'est-à-dire précisément la capacité qui déterminera l'intérêt économique de ces machines.

**Nommer n'est pas imputer une faute.** Le point pédagogique n'est pas qu'il y aurait eu tromperie. Il est que **le protocole n'était pas déclaré**. Une démonstration qui n'annonce pas ses conditions laisse le spectateur les inventer, et le spectateur les invente toujours dans le sens le plus favorable. La responsabilité de la lecture est partagée : la vôtre consiste à poser les cinq questions avant de conclure quoi que ce soit.

**Ce que ce cas ne permet pas de conclure.** Que la robotique humanoïde est une imposture. La téléopération est un échelon réel de l'échelle des preuves, et c'est même la voie par laquelle plusieurs de ces systèmes collectent les données d'entraînement qui pourraient un jour réduire le besoin de téléopération. Le cas dit seulement à quel échelon nous étions à cette date — et qu'il faut le demander.

⏱ *Événement d'octobre 2024 ; l'état de l'autonomie des systèmes humanoïdes évolue rapidement. Voir Annexe I.*

## 6.4 Benchmarks : ce qu'un score mesure

Un benchmark est une tâche standardisée servant à comparer des systèmes. Il rend possibles des progrès mesurables, et c'est un outil précieux. Il souffre d'une pathologie structurelle, connue sous le nom de **loi de Goodhart** : quand une mesure devient un objectif, elle cesse d'être une bonne mesure.

Quatre défaillances à connaître.

**La contamination.** Les données de test se retrouvent dans les données d'entraînement. Le système ne résout pas le problème : il l'a déjà vu.

**Le surajustement au benchmark.** Sans contamination directe, on peut optimiser un système pour la forme particulière des questions du test.

**La sélection de la métrique.** Sur dix métriques possibles, on rapporte celle qui est favorable. Rien n'est faux, tout est trompeur.

**L'écart de distribution.** Le test représente une distribution de cas ; la réalité en représente une autre, généralement plus large et plus désordonnée.

### Cas documenté — GSM1k, 2024

**Le protocole.** En mai 2024, une équipe de Scale AI publie *A Careful Examination of Large Language Model Performance on Grade School Arithmetic* (arXiv:2405.00332). L'idée est simple et élégante : GSM8k, benchmark de référence pour l'arithmétique de niveau primaire, circule sur Internet depuis des années et peut donc avoir fui dans les corpus d'entraînement. Les auteurs font écrire à la main un nouveau jeu de problèmes, GSM1k, calibré pour être équivalent à GSM8k sur tout ce qui est mesurable : taux de résolution humain, nombre d'étapes, ordre de grandeur des réponses, longueur des énoncés. Si un modèle sait faire de l'arithmétique, les deux scores doivent coïncider.

**Le résultat.** Pour plusieurs familles de modèles, ils ne coïncident pas : les auteurs observent des écarts allant jusqu'à environ 13 points de pourcentage, avec un surajustement systématique dans certaines familles à presque toutes les tailles de modèle. D'autres modèles, notamment parmi les plus performants de l'époque, ne montrent pas d'écart significatif. Les auteurs relèvent en outre une corrélation positive entre la propension d'un modèle à régénérer verbatim des énoncés de GSM8k et l'ampleur de sa chute sur GSM1k — signature d'une mémorisation au moins partielle.

**Les trois nuances qui font la valeur de ce cas.** D'abord, les auteurs notent explicitement qu'un modèle surajusté **reste capable de raisonner** : le score était surévalué, pas fictif. Ensuite, la contamination n'explique pas tout l'écart. Enfin — et c'est le point le plus important — les modèles les plus performants ne montrant pas d'écart, il serait faux d'en conclure que « les benchmarks ne valent rien ».

**Ce que ce cas enseigne vraiment.** Non pas que les scores mentent, mais que **la seule manière de savoir ce qu'un score mesure est de construire un ensemble de contrôle** — ce que presque personne ne fait pour la plupart des benchmarks cités. En l'absence de contrôle, un score est une information, pas une preuve.

**La question à poser désormais devant tout score :** *sur quelle distribution, et qu'est-ce qui garantit que le système ne l'a pas déjà vue ?*

## 6.5 Rendement de laboratoire, rendement de production

C'est l'écart le plus systématique de toute l'industrie, et il vaut bien au-delà de l'électronique.

Un record de laboratoire est obtenu sur un exemplaire unique, souvent de très petite surface, fabriqué par des experts, mesuré dans des conditions idéales, sans contrainte de coût ni de durée de vie. Un produit industriel est fabriqué en série, sur grande surface, par des opérateurs, avec des tolérances, un budget et une garantie.

Trois écarts se combinent.

**L'effet de surface.** Les rendements record de cellules photovoltaïques sont certifiés sur des surfaces très petites. Passer à un module de plusieurs mètres carrés fait apparaître les inhomogénéités, les pertes de connexion et les défauts locaux. L'écart entre rendement de cellule record et rendement de module commercial est structurel et se compte en plusieurs points. ⏱

**Le rendement de fabrication.** En microélectronique, le nombre de puces fonctionnelles par plaquette gouverne l'économie entière. Une même conception peut être rentable à un rendement de 80 % et ruineuse à 40 %. Ce paramètre n'apparaît dans aucune annonce technique, et c'est souvent lui qui décide qui gagne.

**La durée de vie.** Un dispositif peut atteindre un excellent rendement initial et se dégrader trop vite pour être commercialisable. C'est aujourd'hui le principal verrou de plusieurs familles de matériaux photovoltaïques émergents : la performance est démontrée, la stabilité ne l'est pas. Nous y reviendrons au chapitre 21, puis dans la famille énergie de la Partie II.

**La question à poser devant tout record :** *sur quelle surface, pendant combien de temps, avec quel rendement de fabrication ?*

## 6.6 Le calendrier glissant

Les calendriers de projets techniques dérivent, et cette dérive est structurelle plutôt qu'accidentelle. Trois mécanismes concourent.

**L'estimation par la partie connue.** On estime le temps d'après les tâches qu'on sait identifier. Les tâches qu'on ne sait pas encore identifier sont, par construction, absentes de l'estimation.

**Le premier exemplaire.** Un objet fabriqué pour la première fois révèle des problèmes que la conception ne pouvait pas contenir. Plus l'objet est nouveau, plus cet effet est fort.

**L'asymétrie des incitations.** Annoncer une date lointaine coûte immédiatement — financement, attention, moral des équipes. Le coût du glissement, lui, est différé.

### Cas documenté — le calendrier d'ITER

**Les faits.** Le projet ITER, réacteur expérimental de fusion en construction à Cadarache, visait un « premier plasma » en 2025 selon la référence de 2016. En juin 2024, l'organisation soumet à son conseil une nouvelle référence, adoptée comme référence de travail. Le nouveau calendrier prévoit le début des opérations de recherche en 2034, la pleine énergie magnétique en 2036 — soit trois ans de retard sur la référence de 2016 — et le début de la phase deutérium-tritium en 2039, soit quatre ans de retard. Le directeur général Pietro Barabaschi cite la pandémie, des problèmes de qualité — notamment des non-conformités géométriques sur des secteurs de la chambre à vide et une corrosion sous contrainte dans des circuits de refroidissement des écrans thermiques — et une planification initialement trop optimiste pour un objet de première espèce. Le surcoût annoncé est de l'ordre de 5 milliards d'euros.

**La nuance méthodologique, qui est le vrai enseignement.** L'organisation souligne que les deux calendriers ne sont pas directement comparables : le « premier plasma » de 2025 correspondait à une machine très allégée, alors que le début d'opérations de 2034 correspond à une machine beaucoup plus complète, incluant divertor et blanket. Comparer les deux dates comme si elles désignaient le même événement produit un chiffre de retard trompeur.

**Ce que vous devez en retenir.** Devant tout glissement de calendrier, la première question n'est pas « de combien ? » mais **« la définition du jalon a-t-elle changé ? »**. Un jalon redéfini est une information différente d'un jalon manqué, et les deux se ressemblent beaucoup dans un communiqué.

⏱ *Calendrier ITER — référence 2024, vérifiée en août 2026. Voir Annexe I.*

## 6.7 Lire une source pour ce qu'elle peut établir

Aucune source n'est bonne ou mauvaise dans l'absolu. Chacune peut établir certaines choses et pas d'autres.

| Source | Bonne pour établir | Mauvaise pour établir |
|---|---|---|
| Article scientifique à comité de lecture | un résultat sous protocole | sa généralisation, sa maturité industrielle |
| Norme ou standard officiel | ce qui est exigible, exigé, mesuré | ce qui est effectivement pratiqué |
| Document réglementaire ou financier | des faits opposables juridiquement | l'intention future |
| Documentation technique constructeur | ce que le produit est censé faire | ses limites réelles |
| Communiqué d'entreprise | ce que l'entreprise affirme et veut faire savoir | l'état technique indépendant |
| Rapport d'agence publique | des données agrégées, une méthodologie explicite | des projections, lues comme des prévisions |
| Cabinet d'analyse privé | l'état d'une perception de marché | des faits techniques |
| Presse spécialisée | l'existence d'un événement, des recoupements | le détail technique de première main |

Deux habitudes valent tout un chapitre.

**Remonter d'un cran.** Un article de presse qui rapporte une étude : allez à l'étude. Une étude qui cite un chiffre : allez à la source du chiffre. Cette remontée prend deux minutes et surprend souvent.

**Chercher qui bénéficie de l'affirmation.** Ce n'est pas un argument — un acteur intéressé peut dire vrai. C'est une indication du niveau de vérification à appliquer.

## 6.8 Le sceptique automatique se trompe aussi

Ce chapitre vous a donné des instruments pour douter. Il faut donc en donner un pour ne pas douter à tort, car l'erreur symétrique existe et coûte aussi cher.

Le chapitre 1 en a montré un exemple : la sous-estimation persistante du photovoltaïque par des institutions sérieuses. Le mécanisme de l'erreur sceptique est identifiable :

* **la généralisation depuis les échecs passés** — « on nous a déjà promis ça » est vrai et ne prouve rien ;
* **la confusion entre difficile et impossible** ;
* **le refus du changement de régime** — une régularité observée pendant vingt ans peut cesser, dans les deux sens ;
* **le confort social du scepticisme** : il coûte moins cher d'avoir tort en doutant qu'en croyant, ce qui n'a rien à voir avec la vérité.

**Le test pratique.** Après avoir formulé un doute, appliquez-lui la quatrième question du chapitre 4 : *qu'est-ce qui me ferait changer d'avis ?* Si votre scepticisme ne produit aucun signal observable qui le contredirait, ce n'est pas une analyse — c'est une posture.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « C'est en production chez un client » | pilote, périmètre restreint | combien d'utilisateurs, depuis combien de temps, avec quel taux d'incident ? |
| « On a un record mondial » | mesure certifiée en conditions idéales | sur quelle surface, quelle durée, avec quel rendement de fabrication ? |
| « Le modèle atteint 95 % » | score sur un benchmark public | sur quelle distribution, et vérifiée comment contre la contamination ? |
| « Notre feuille de route prévoit » | intention non contractuelle | quel jalon a déjà glissé, et sa définition a-t-elle changé ? |
| « Ils ont levé 200 millions » | des investisseurs ont pris un risque | qu'est-ce que cela prouve sur la technologie ? |
| « C'est déjà déployé » | ambigu de plusieurs échelons | déployé au sens pilote, série, ou industriel ? |

🧪 **Lab 4 — Décomposition d'annonce**

**Objectif.** Situer une affirmation technologique sur l'échelle des preuves et reformuler ce qui est réellement établi.
**Durée.** 75 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitres 2, 4, 6.
**Contexte.** Un dossier vous est fourni sur une même technologie : un communiqué d'entreprise, une vidéo de démonstration, un article de presse spécialisée, un extrait de publication scientifique et un extrait de document financier.
**Travail demandé.**
(a) Situer chaque pièce sur l'échelle des preuves ou sur l'échelle des annonces.
(b) Pour la vidéo, répondre aux cinq questions de 6.3 — en notant explicitement celles auxquelles la vidéo ne permet pas de répondre.
(c) Établir ce que le dossier permet d'affirmer, en trois phrases maximum, sans aucun terme de niveau récit.
(d) Lister ce que le dossier ne permet pas de trancher, et pour chaque point, dire quelle pièce manquante le trancherait.
(e) Identifier la pièce la plus fiable du dossier et justifier.
**Livrable.** Une page. La partie (d) est la plus importante.
**Compétences validées.** Situation sur l'échelle, lecture différenciée des sources, formulation de ce qui reste indéterminé, désignation de la preuve manquante.
**Éléments attendus.** En (e), la réponse attendue est généralement le document financier ou l'extrait scientifique, non le communiqué ni la vidéo — mais une copie qui argumente l'inverse de façon défendable est valable. L'erreur la plus fréquente est en (c) : la plupart des premières tentatives écrivent trois phrases qui reprennent le communiqué en le nuançant, au lieu d'énoncer ce que les pièces établissent conjointement. Une copie forte produit en (d) une liste plus longue qu'en (c) — c'est normal et c'est le signe d'une lecture honnête.

🎓 **À ce stade, vous savez…**

* situer une affirmation sur les douze échelons de l'échelle des preuves ;
* distinguer une preuve d'une annonce, et savoir ce que chacune établit ;
* interroger une vidéo de démonstration sur son protocole ;
* demander à un score de benchmark sa distribution et son ensemble de contrôle ;
* distinguer rendement de laboratoire, rendement de fabrication et durée de vie ;
* lire un glissement de calendrier en vérifiant d'abord si le jalon a été redéfini ;
* appliquer à votre propre scepticisme la même exigence de réfutabilité qu'à l'enthousiasme d'autrui.

---
