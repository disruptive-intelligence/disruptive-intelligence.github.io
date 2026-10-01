---
title: Chapitre 1 — Pourquoi les analyses technologiques échouent
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 1.1 Trois analyses réelles, et fausses

Commençons par des erreurs. Pas des erreurs de profanes : des erreurs commises par des organisations compétentes, informées, souvent mieux placées que nous pour savoir.

**Note de méthode.** Ce cours nomme les acteurs quand leur identité aide à comprendre une trajectoire ou permet au lecteur de vérifier par lui-même. Nommer n'est pas imputer une faute. Pour chaque cas, nous distinguons systématiquement ce qui a été annoncé, quand, ce qui était raisonnablement connaissable à ce moment-là, ce qui s'est produit, et ce que le cas ne permet pas de conclure.

### Cas A — Ford, août 2016 : un véhicule pleinement autonome en 2021

**Ce qui a été annoncé.** Le 16 août 2016, Ford publie un communiqué annonçant l'intention de mettre en service commercial en 2021 un véhicule autonome de niveau SAE 4, produit en grande série, dans un service de transport à la demande. Le communiqué précise que ce véhicule sera dépourvu de volant, de pédale d'accélérateur et de pédale de frein. Ford annonce simultanément quatre investissements ou partenariats — dont Velodyne pour le lidar et Civil Maps pour la cartographie 3D — et le doublement de ses effectifs dans la Silicon Valley. En 2017, Ford investit environ un milliard de dollars dans Argo AI, rejoint en 2019 par Volkswagen à hauteur de 2,6 milliards.

*Source primaire : communiqué Ford, 16 août 2016, « Ford Targets Fully Autonomous Vehicle for Ride Sharing in 2021 ».*

**Ce qui était raisonnablement connaissable en 2016.** Les véhicules d'essai roulaient déjà seuls sur des dizaines de milliers de kilomètres. Le coût des capteurs baissait. Les modèles de perception progressaient d'année en année. L'analyse n'était pas absurde, et Ford n'était pas isolé : plusieurs constructeurs affichaient des horizons comparables.

**Ce qui s'est produit.** Le 26 octobre 2022, Argo AI cesse ses activités faute de nouveaux investisseurs. Ford enregistre une dépréciation non monétaire avant impôt de 2,7 milliards de dollars sur sa participation, contribuant à une perte nette de 827 millions au troisième trimestre. Dans la publication des résultats, le directeur général Jim Farley constate qu'en 2017 l'entreprise anticipait une mise sur le marché large de la conduite autonome de niveau 4 en 2021, et que la situation a changé — ajoutant que des véhicules pleinement autonomes rentables et à grande échelle restent lointains.

**Et pourtant, la capacité est arrivée.** En mars 2026, Waymo annonce 500 000 trajets payants par semaine dans dix villes américaines, contre 50 000 par semaine en mai 2024 — un facteur dix en moins de deux ans — avec une flotte de l'ordre de 3 000 véhicules déclarée au régulateur américain fin 2025, et un objectif public d'un million de trajets hebdomadaires d'ici fin 2026. ⏱ *Information périssable — vérifiée en août 2026, voir Annexe I.*

**Ce que l'erreur de 2016 était réellement.** Elle ne portait ni sur la possibilité, ni même vraiment sur la date. Elle portait sur trois choses :

1. **La forme de la difficulté restante.** Passer de « fonctionne dans la grande majorité des situations » à « fonctionne dans toutes les situations, y compris celles qu'on n'a pas imaginées » n'est pas la suite de la même courbe. Nous verrons au chapitre 21 que chaque incrément de fiabilité se paie de plus en plus cher.
2. **Le modèle de déploiement.** L'annonce décrivait un véhicule produit en grande série et sans commande manuelle. Ce qui fonctionne aujourd'hui est autre chose : un déploiement ville par ville, sur des zones cartographiées finement, avec assistance à distance, et une négociation réglementaire locale à chaque nouvelle ville. La capacité s'est matérialisée sous une forme qui n'était pas celle annoncée.
3. **Le porteur.** Rien ne garantissait que celui qui annonce soit celui qui aboutit.

**Ce que ce cas ne permet pas de conclure.** Qu'annoncer 2021 était déraisonnable — c'était une hypothèse défendable avec l'information de 2016. Ni que la décision d'arrêter en 2022 était mauvaise : c'était peut-être la meilleure analyse des deux, puisqu'elle reconnaissait qu'un verrou n'était pas là où on l'avait cru. Ce cas ne dit pas non plus que la conduite autonome est « résolue » : cinq cent mille trajets hebdomadaires restent une fraction infime du transport urbain mondial.

### Cas B — L'impression 3D domestique, 2012-2014

**Ce qui a été annoncé.** Entre 2012 et 2014, un discours largement relayé annonce la fin de la production centralisée. Chris Anderson, alors rédacteur en chef de *Wired*, publie *Makers: The New Industrial Revolution* en 2012. En juin 2013, Stratasys, industriel historique de la fabrication additive, rachète MakerBot — leader des imprimantes de bureau — pour une valeur initiale d'environ 403 millions de dollars en actions, avec jusqu'à 201 millions de compléments de prix. L'analogie du micro-ondes circule alors dans la presse spécialisée : chaque foyer en aurait un, sans que tout soit fabriqué avec.

**Ce qui s'est produit.** Le marché grand public ne s'est pas matérialisé à cette échelle. Le cours de Stratasys, qui avait culminé début 2014, s'effondre les années suivantes. Pendant ce temps, la fabrication additive réussit très bien — ailleurs : aéronautique, médical, outillage, prototypage, pièces à géométrie complexe en petite série.

**L'erreur ici n'est pas d'optimisme, elle est catégorielle.** La fabrication additive est un ensemble de **procédés** — un moyen de mettre en forme de la matière. La production industrielle est un **système** : procédés, mais aussi contrôle qualité, cadence, coût unitaire, chaîne d'approvisionnement, normes, garantie, service après-vente. Annoncer que le premier remplace le second, c'est comparer une brique à un système. Le chapitre 2 est consacré à cette confusion, la plus fréquente de toutes et la plus difficile à voir sans instrument.

**Ce que ce cas ne permet pas de conclure.** Que l'impression 3D était une bulle vide. Le mécanisme était réel et il a produit une industrie ; c'est le domaine d'application annoncé qui était faux.

### Cas C — Les prévisions de photovoltaïque : l'erreur inverse

Le troisième cas est l'erreur symétrique, et on l'oublie plus volontiers.

**Ce qui s'est produit.** Pendant deux décennies, les projections de l'Agence internationale de l'énergie publiées dans le *World Energy Outlook* ont sous-estimé la croissance du photovoltaïque. Une analyse ex post des éditions de 1993 à 2022, publiée en 2025 dans *Renewable and Sustainable Energy Reviews* par Lopez, Pourjamal et Breyer (LUT University), conclut que l'agence a correctement anticipé la demande énergétique globale mais nettement sous-estimé la croissance du solaire et de l'éolien, y compris dans ses scénarios les plus volontaristes. Repère concret souvent cité : l'édition 2010 projetait environ 294 GW de capacité photovoltaïque installée en 2030 ; ce niveau était dépassé dès 2016.

**Pourquoi cette erreur.** Les modèles supposaient une baisse de coût progressive, du type de celles observées dans l'énergie conventionnelle. Ils n'intégraient pas correctement le mécanisme du chapitre 22 : pour beaucoup d'objets manufacturés, le coût baisse en fonction du **volume cumulé produit**, et non du temps écoulé. Une hypothèse de taux d'apprentissage trop faible suffit à produire, sur vingt ans, un écart d'un ordre de grandeur.

**La nuance qui compte, et qui est elle-même une leçon.** L'AIE objecte que ses scénarios ne sont pas des prévisions mais des projections conditionnelles aux politiques en vigueur : un scénario qui suppose des politiques inchangées n'a pas vocation à anticiper un changement de politique. Cette défense est partiellement recevable, et elle est exactement le genre de distinction que ce cours vous apprendra à faire au chapitre 6 : **un scénario n'est pas une prévision, et lire l'un comme l'autre est une erreur de l'utilisateur autant que du producteur**. Il reste que l'écart s'est reproduit sur presque toutes les éditions, dans le même sens, ce qu'une simple dépendance aux politiques n'explique pas entièrement.

⏱ *Chiffres de capacité et projections — information périssable, voir Annexe I.*

**Retenez la symétrie.** On peut se tromper en surestimant une trajectoire ; on peut se tromper en la sous-estimant. Le scepticisme systématique n'est pas une méthode. C'est simplement l'erreur opposée, avec une meilleure réputation.

## 1.2 Erreur 1 — Confondre les niveaux d'abstraction

Écoutez une réunion technologique et notez les objets comparés. Vous entendrez régulièrement des phrases de cette forme :

> « Entre la robotique, l'IA générative et l'edge, où faut-il investir ? »

Cette question n'a pas de réponse, parce que ses termes ne sont pas du même ordre. « Robotique » désigne une famille de systèmes physiques. « IA générative » désigne une famille de capacités logicielles. « Edge » désigne une manière de répartir un traitement — un choix d'architecture, pas une technologie. Les trois peuvent coexister dans le même produit.

**Attention à ce que ce principe dit exactement.** Il n'interdit pas de faire dialoguer les niveaux — c'est même l'essentiel du travail d'analyse. *Cette brique rend-elle possible cette capacité ?* *Cette doctrine exploite-t-elle les propriétés de cette plateforme ?* sont d'excellentes questions, et tout ce cours en est fait.

Ce qui produit une conclusion mal formée, c'est de traiter des objets de niveaux différents comme des **alternatives équivalentes sur un même axe** — comme s'il fallait choisir entre eux, ou les classer. Le chapitre 2 est entièrement consacré à cette distinction.

> **P1 — Des objets de niveaux différents ne se comparent pas comme des équivalents.**

## 1.3 Erreur 2 — Confondre démonstration, produit et industrie

Une vidéo montre un robot humanoïde plier du linge. Un communiqué annonce un rendement record en laboratoire. Un article rapporte qu'un modèle a dépassé l'humain sur un test.

Chacune de ces informations est probablement exacte. Aucune ne dit ce qu'on lui fait dire.

Une démonstration établit qu'une chose est **possible dans les conditions de la démonstration**. Elle ne dit rien de la fréquence de succès, du coût, de la reproductibilité hors du laboratoire, de la possibilité de fabriquer l'objet en série, ni de l'existence d'un client. Entre « ça a marché une fois devant une caméra » et « une industrie produit cet objet et gagne de l'argent », il y a une distance considérable, et le chapitre 6 est consacré à mesurer cette distance rigoureusement.

> **P2 — Une démonstration prouve ce que son protocole permet de conclure, pas ce que son récit suggère.**

## 1.4 Erreur 3 — Confondre performance et diffusion

Le Concorde volait à Mach 2. Il a été retiré du service, et aucun successeur commercial ne l'a remplacé pendant des décennies. Le format vidéo techniquement le mieux conçu n'est pas toujours celui qui s'impose. Une pompe à chaleur est thermodynamiquement supérieure à une chaudière depuis longtemps, ce qui n'a pas suffi à la généraliser rapidement.

L'idée que la meilleure technologie gagne est une croyance confortable et empiriquement faible. Ce qui gagne, c'est ce qui est **suffisamment bon, disponible, finançable, installable, maintenable et acceptable** dans un système donné. La performance n'est qu'une des neuf conditions que nous verrons au chapitre 3, et rarement celle qui bloque.

Un lecteur venant de l'informatique connaît déjà ce phénomène sous un autre nom : la base installée. Un protocole médiocre mais universellement déployé bat un protocole élégant que personne n'implémente. C'est exactement le même mécanisme, et il vaut pour les réseaux électriques, les containers maritimes et les prises de courant.

## 1.5 Erreur 4 — Raisonner sans ordre de grandeur

Considérez cette phrase, du type de celles qu'on lit régulièrement :

> « Il suffirait de couvrir une petite partie du désert pour alimenter la planète. »

Elle est arithmétiquement défendable si l'on ne considère que la surface et l'ensoleillement. Elle devient tout autre chose dès qu'on ajoute le transport de l'électricité sur des milliers de kilomètres, le stockage nécessaire pour la nuit, les matériaux requis, l'eau de nettoyage, la maintenance dans un environnement abrasif, et le fait que l'électricité ne représente qu'une fraction de la consommation énergétique mondiale.

L'affirmation n'est pas fausse. Elle est **incomplète d'une manière qui inverse sa conclusion**. Et il ne faut pas être physicien pour le voir : il faut savoir compter en ordres de grandeur, ce qui s'apprend en un chapitre. C'est l'objet du chapitre 5.

> **P3 — Sans ordre de grandeur, il n'y a pas d'avis, seulement une impression.**

## 1.6 Erreur 5 — Produire une analyse que rien ne peut réfuter

Voici deux analyses de la même technologie.

> **A —** « L'IA va transformer en profondeur l'ensemble des métiers dans les années qui viennent. »

> **B —** « Si le coût d'inférence par tâche continue de baisser d'un facteur dix tous les deux ans, et si les modèles atteignent une fiabilité suffisante pour être utilisés sans relecture systématique sur des tâches à conséquence, alors les gains de productivité deviendront mesurables dans les statistiques sectorielles. Si le coût plafonne ou si la fiabilité reste insuffisante pour supprimer la relecture, l'adoption restera confinée aux tâches à faible enjeu. »

L'analyse A est agréable, consensuelle et inutile. Aucune observation future ne peut l'invalider : quoi qu'il arrive, elle aura eu raison. L'analyse B est plus longue, plus prudente et infiniment plus utile, parce qu'elle **dit ce qu'il faut regarder** et **ce qui la ferait tomber**.

Une analyse qu'aucune observation ne peut contredire n'est pas une analyse prudente. C'est une opinion déguisée en analyse.

> **P10 — Une analyse qu'aucune observation ne peut réfuter est une opinion, pas une analyse.**

Ce principe gouvernera tout le cours, et il sera votre principal outil de défense contre le bruit technologique. Il a une contrepartie exigeante : il vous oblige à formuler vos propres analyses de manière à pouvoir avoir tort. C'est inconfortable et c'est le prix de la rigueur.

## 1.7 Ce que ce cours propose à la place

Les cinq erreurs ci-dessus ont un point commun : aucune ne vient d'un manque de connaissances techniques. Elles viennent d'une **absence d'instruments de lecture**. On peut connaître parfaitement le fonctionnement d'une batterie et commettre les cinq.

Ce cours vous donne donc, dans l'ordre :

| Instrument | Chapitre | Contre quelle erreur |
|---|---|---|
| L'échelle d'abstraction | 2 | Erreur 1 |
| Les neuf conditions de diffusion | 3 | Erreur 3 |
| Les quatre questions | 4 | Erreur 5 |
| Les ordres de grandeur | 5 | Erreur 4 |
| L'administration de la preuve | 6 | Erreur 2 |
| Le statut des lois et modèles | 7 | Toutes |

Puis une carte des grandes familles technologiques (Partie II), les mécanismes qui déterminent la diffusion (Partie III), une confrontation de la méthode à des trajectoires historiques dont nous connaissons l'issue (Partie IV), et enfin un protocole pour aborder seul un domaine que vous ne connaissez pas (Partie V).

### Une remarque à l'intention du lecteur venant de l'informatique et de la cybersécurité

Vous arrivez avec un avantage réel et un angle mort.

L'avantage : vous manipulez déjà quotidiennement des modèles mentaux qui se transfèrent remarquablement bien à d'autres domaines. La **dépendance** — savoir que si ce composant tombe, quatorze autres tombent avec lui. L'**abstraction en couches** — savoir qu'on peut raisonner à un niveau sans connaître le niveau inférieur, et savoir aussi que les abstractions fuient. La **latence** et la **bande passante** comme deux grandeurs distinctes qu'on confond. Le **scaling** — savoir que ce qui marche pour dix utilisateurs ne marche pas mécaniquement pour dix millions. La **résilience** et le mode dégradé. La **dette technique** — savoir qu'un choix ancien continue de coûter longtemps après avoir été oublié.

Ces modèles sont puissants et ils vous serviront dans tout ce cours. Nous les réutiliserons explicitement.

L'angle mort : ils viennent d'un domaine où **copier coûte presque zéro**, où le déploiement est instantané, où un correctif se pousse en production en quelques minutes, et où la matière n'intervient pas. Ce n'est pas le cas général. Dans la plupart des domaines que nous allons traverser, produire le millième exemplaire coûte à peu près autant que le centième, un correctif implique de rappeler des objets physiques, une usine se construit en années, et une erreur de conception se paie en tonnes de matière. Une partie du travail de ce cours consistera à vous montrer **où vos modèles se transfèrent et où ils cessent de fonctionner**.

Vous ne serez pas relégué : la cybersécurité apparaîtra systématiquement, comme conséquence, dans chaque famille technologique. Mais elle apparaîtra à sa place réelle, qui est celle d'une implication majeure et non d'un centre.

🎓 **À ce stade, vous savez…**

* nommer cinq erreurs d'analyse récurrentes et les reconnaître dans un discours ;
* expliquer pourquoi le scepticisme systématique est une erreur symétrique de l'enthousiasme ;
* distinguer une analyse réfutable d'une analyse qui ne peut pas avoir tort ;
* dire pourquoi votre expérience informatique est un point d'appui et non une clé universelle.

**Ce que vous ne savez pas encore :** comment classer proprement les objets dont on vous parle, ce qui est l'objet du chapitre suivant.

---
