---
title: Chapitre 6 — Mesurer la distance, la forme et le mouvement
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute.** Le chapitre 5 traitait de ce qui se voit. Celui-ci traite de ce qui se **mesure** : à quelle distance, à quelle vitesse, dans quelle direction, et où se trouve le capteur lui-même.
>
> **Une contrainte commune à toutes les entrées.** Mesurer une distance revient à mesurer un temps — celui que met un signal à faire l'aller-retour — ou à mesurer un déphasage. La précision d'une distance est donc bornée par la précision d'une horloge, et c'est ce qui relie ce chapitre au positionnement.
>
> **Huit entrées**, dont trois traitent d'un sujet que la plupart des ouvrages omettent : que se passe-t-il quand le positionnement satellitaire n'est plus disponible.

---

## ◆◆◆ Lidar

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Un capteur qui émet de la lumière et mesure son retour pour produire une carte de distances.

**Pourquoi on en parle.** C'est le capteur emblématique de l'autonomie mobile, celui dont le coût a le plus baissé en une décennie, et celui autour duquel se cristallise un débat d'architecture — faut-il un lidar, ou une caméra suffit-elle ?

**Comment ça fonctionne.** Deux principes coexistent. Le **temps de vol** : on émet une impulsion très brève et on mesure le délai de retour ; la distance s'en déduit directement. La **modulation de fréquence continue** : on émet un signal dont la fréquence varie et on compare l'émis au reçu ; le déphasage donne la distance, et l'effet Doppler donne en prime **la vitesse radiale du point mesuré** — ce que le temps de vol ne fournit pas.

Le balayage peut être mécanique, à micro-miroirs, ou entièrement électronique. Le passage au balayage sans pièce mobile est le principal enjeu industriel de la famille, parce qu'il conditionne la durée de vie et le coût.

**Où vous rencontrerez le terme.** Véhicules autonomes · robotique mobile · cartographie et topographie · agriculture · surveillance d'infrastructures · archéologie · construction.

**Ce que ça permet.** Une mesure de distance **directe et dense**, indépendante de l'éclairement, avec une précision qui ne se dégrade pas avec la distance de la même manière qu'une estimation par vision.

**Ce qui bloque.** **Les conditions atmosphériques** : brouillard, pluie forte et poussière diffusent le faisceau et dégradent fortement la portée utile. **Les surfaces peu réfléchissantes** renvoient peu de signal. **Les interférences** entre systèmes voisins deviennent un sujet quand la densité de lidars augmente. Et **le coût**, qui a beaucoup baissé sans être négligeable.

**De quoi ça dépend.** Sources laser · détecteurs rapides · électronique de datation fine · optique de balayage · calcul pour le traitement du nuage de points.

**Ce que cela implique.** Un lidar produit une géométrie, pas une sémantique : il dit qu'il y a quelque chose à trois mètres, pas ce que c'est. Il est donc **complémentaire et non concurrent** d'une caméra — et le débat d'architecture porte en réalité sur le coût d'une redondance, pas sur la supériorité d'un capteur.

**Sûreté et sécurité.** Un capteur actif émet, donc il se signale et peut être perturbé. Ce volume traite ces phénomènes au niveau du principe et de leurs conséquences systémiques.

**À ne pas confondre avec.** **Le radar**, qui exploite des longueurs d'onde des milliers de fois plus grandes : il traverse mieux les conditions dégradées et mesure directement la vitesse, mais offre une résolution angulaire bien plus grossière à taille d'antenne raisonnable. **La stéréovision**, qui estime la distance par calcul à partir de deux images, sans rien émettre.

**Termes voisins.** *ToF* et *FMCW* désignent les deux principes, non deux produits. *Télémètre laser* désigne un dispositif à point unique, sans balayage.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Coût unitaire en baisse continue, intégration croissante en série automobile. Le balayage sans pièce mobile et la modulation de fréquence progressent ; les architectures cohabitent.
> 🔄 **À revoir si** un lidar à balayage entièrement électronique atteint une production en grande série à un coût comparable à celui d'une caméra de qualité automobile.

**Renvois** — Couche : percevoir · Courant : autonomous systems (ch. 33) · Convergences : autonomie mobile (39), robotique généraliste (36).

---

## ◆◆ Radar imageur

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Utiliser des ondes radio pour produire non plus une simple détection, mais une image ou une carte de l'environnement.

**Pourquoi on en parle.** Parce que le radar traverse ce que l'optique ne traverse pas — nuit, brouillard, pluie, poussière — et qu'il mesure directement la vitesse.

**Comment ça fonctionne.** On émet une onde et on analyse l'écho. La distance vient du délai, la vitesse de l'effet Doppler, la direction de la géométrie de l'antenne. Les architectures modernes utilisent plusieurs émetteurs et récepteurs pour synthétiser une ouverture plus grande que l'antenne physique, ce qui améliore la résolution angulaire.

**Où vous rencontrerez le terme.** Automobile · aéronautique · surveillance maritime · météorologie · contrôle industriel · détection de présence.

**Ce que ça permet.** Fonctionner dans des conditions où l'optique échoue · mesurer la vitesse sans traitement · détecter à travers certains matériaux non métalliques.

**Ce qui bloque.** **La résolution angulaire**, bornée par le rapport entre longueur d'onde et taille d'antenne : c'est la contrainte structurante, et elle explique pourquoi un radar ne « voit » pas comme une caméra. S'y ajoutent les **échos parasites** et **l'encombrement du spectre**, ressource attribuée et non achetée.

**Ce que cela implique.** Radar et optique ne se remplacent pas : leurs conditions d'échec sont différentes, et c'est précisément ce qui rend leur combinaison utile — une redondance dissemblable, au sens du volume 1.

**À ne pas confondre avec.** **Le lidar**, et **le SAR**, qui est une technique particulière traitée séparément.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Généralisation en automobile ; progression de la résolution par augmentation du nombre de voies et montée en fréquence.
> 🔄 **À revoir si** des radars à haute résolution angulaire atteignent un coût de série permettant de remplacer plutôt que de compléter d'autres capteurs.

**Renvois** — Couche : percevoir · Convergence : autonomie mobile (39).

---

## ◆◆◆ SAR — ouverture synthétisée

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Obtenir la résolution d'une très grande antenne en déplaçant une petite antenne et en combinant les mesures successives.

**Pourquoi on en parle.** C'est la technique qui rend l'observation radar depuis l'espace utile — et donc la seule manière d'observer un point du globe indépendamment des nuages et de la lumière du jour.

**Comment ça fonctionne.** Le principe repose sur la contrainte du chapitre précédent : la finesse de détail dépend du rapport entre longueur d'onde et taille d'ouverture. Aux longueurs d'onde radar, obtenir une résolution fine exigerait une antenne de plusieurs centaines de mètres — impossible à embarquer.

La solution consiste à **utiliser le déplacement du porteur comme antenne**. En enregistrant l'écho depuis des positions successives et en combinant ces mesures en tenant compte de leur phase, on synthétise une ouverture équivalente à la distance parcourue. La résolution obtenue ne dépend alors plus de la taille de l'antenne réelle.

Une variante importante, l'**interférométrie**, compare deux acquisitions du même lieu à des dates différentes : la différence de phase révèle des déplacements du sol de l'ordre du centimètre, voire moins.

**Où vous rencontrerez le terme.** Observation de la Terre · surveillance maritime · suivi de déformation du sol · agriculture · gestion de catastrophes · applications de défense.

**Ce que ça permet.** Observer de nuit, à travers les nuages · mesurer des déformations millimétriques à l'échelle d'un territoire · détecter des objets en mer indépendamment de la météo · comparer deux dates avec une précision inaccessible à l'optique.

**Ce qui bloque.** **Le calcul** : la formation d'une image SAR est un traitement lourd, historiquement effectué au sol. **La puissance émise**, donc l'énergie disponible sur le satellite. **La complexité d'interprétation** : une image SAR ne ressemble pas à une photographie, et sa lecture demande une compétence spécifique — c'est un frein d'adoption souvent sous-estimé.

**De quoi ça dépend.** Stabilité de la trajectoire du porteur · référence de temps très précise · calcul · énergie · liaison de descente pour le volume de données.

**Ce que cela implique.** Le SAR est un cas où **le capteur ne produit pas l'information** : il produit une mesure dont l'information doit être extraite par calcul. C'est ce qui a longtemps limité son usage, et ce que la baisse du coût du calcul est en train de changer.

**À ne pas confondre avec.** **Le radar imageur classique**, qui n'exploite pas le déplacement du porteur. **L'imagerie optique**, dont les produits ne sont pas comparables — une image SAR ne montre pas la couleur ni la texture visuelle, mais la rugosité et les propriétés électriques des surfaces.

**Termes voisins.** *InSAR* pour l'interférométrie. *Ouverture synthétique* est la traduction directe et s'emploie.

> ⏱ **État au 23/08/2026** — 🏭 déployé, en forte croissance. La multiplication des constellations à petits satellites a réduit le coût d'accès et augmenté la fréquence de revisite ; le traitement à bord progresse.
> 🔄 **À revoir si** la formation d'images SAR devient couramment embarquée, ce qui supprimerait la contrainte de descente de données brutes.

**Renvois** — Couche : percevoir · Courant : SpaceTech (ch. 35) · Convergence : intelligence distribuée (38).

---

## ◆◆ Capteurs inertiels

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Mesurer ses propres accélérations et rotations, pour en déduire son déplacement sans aucune référence extérieure.

**Pourquoi on en parle.** Parce que c'est le seul moyen de continuer à savoir où l'on est quand toute référence externe disparaît — et parce que ce moyen se dégrade inexorablement.

**Comment ça fonctionne.** Des accéléromètres mesurent les accélérations selon trois axes, des gyromètres les vitesses de rotation. En intégrant ces mesures dans le temps, on estime vitesse puis position.

**La difficulté est dans l'intégration.** Chaque petite erreur de mesure s'accumule : une erreur d'accélération devient une erreur de vitesse qui croît linéairement, puis une erreur de position qui croît quadratiquement. **Une centrale inertielle ne se trompe pas de plus en plus vite : elle se trompe de plus en plus, et de manière accélérée.**

**Où vous rencontrerez le terme.** Téléphones · véhicules · aéronautique · robotique · plateformes stabilisées · forage · sous-marin.

**Ce que ça permet.** Une navigation totalement autonome, insensible au brouillage, disponible en intérieur, sous l'eau et sous terre — **pendant un temps limité**.

**Ce qui bloque.** **La dérive.** L'écart entre les classes de performance couvre plusieurs ordres de grandeur. La grandeur usuelle est la **stabilité de biais du gyromètre**, exprimée en degrés par heure : de l'ordre de la dizaine à la centaine de degrés par heure pour un capteur de grande diffusion, de l'ordre de l'unité au dixième de degré par heure pour un capteur dit tactique, et en deçà du centième pour un équipement de navigation de haut de gamme — au prix d'un coût, d'une masse et d'un volume sans commune mesure.

**Trois précautions de lecture, et elles comptent plus que les chiffres.** Les noms de classes — grand public, industriel, tactique, navigation — sont des **conventions commerciales sans définition normative**, et leurs bornes varient d'un fournisseur à l'autre. La stabilité de biais *en fonctionnement* n'est pas la **répétabilité au démarrage**, souvent bien plus mauvaise et rarement mise en avant. Et une bonne stabilité de biais ne borne pas seule la dérive : la marche aléatoire angulaire et la sensibilité thermique y contribuent autant. **Un chiffre unique de dérive, sans le protocole qui l'a produit, n'est pas une information exploitable** — c'est le cas d'école du chapitre 4.

**Ce que cela implique.** L'inertiel est presque toujours **couplé** à une source de recalage périodique. Cette architecture — un système précis à court terme associé à un système stable à long terme — est un motif que l'on retrouve dans de nombreux domaines de la mesure.

**À ne pas confondre avec.** **Le positionnement satellitaire**, qui est une référence externe. Les deux sont complémentaires et non substituables.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Les capteurs microfabriqués ont diffusé massivement à bas coût ; les technologies de haute performance restent coûteuses et soumises à contrôle à l'exportation dans certaines classes.
> 🔄 **À revoir si** une technologie de gyromètre de haute performance devient fabricable par les procédés de la microélectronique de masse.

**Renvois** — Couche : percevoir · Convergences : autonomie mobile (39), robotique généraliste (36).

---

## ◆◆ GNSS et positionnement par satellite

**Niveau** — infrastructure · **Couche** — percevoir, relier

**En une phrase.** Déterminer sa position en mesurant le temps de propagation de signaux émis par plusieurs satellites.

**Pourquoi on en parle.** Parce qu'une part considérable du monde technologique en dépend — et pas seulement pour se déplacer.

**Comment ça fonctionne.** Chaque satellite émet en continu un signal horodaté par une horloge très stable. Un récepteur qui reçoit plusieurs de ces signaux compare leurs temps d'arrivée et en déduit sa distance à chaque satellite, donc sa position. **Positionner, c'est fondamentalement mesurer du temps** — et le récepteur obtient donc, en prime, une référence temporelle d'une précision inaccessible autrement.

**Où vous rencontrerez le terme.** Navigation · logistique · agriculture de précision · construction · **synchronisation des réseaux de télécommunications** · **horodatage de transactions** · **corrélation d'événements de sécurité** · réseaux électriques.

**Ce que ça permet.** Une position et un temps, gratuitement, partout, avec un récepteur devenu négligeable en coût et en taille.

**Ce qui bloque.** **Le signal reçu est extrêmement faible.** Il provient d'émetteurs distants de milliers de kilomètres et arrive au sol à un niveau très bas — il est donc facilement perturbable, y compris involontairement. Il ne fonctionne pas en intérieur, sous l'eau, sous terre, et mal en environnement urbain dense où les réflexions produisent des erreurs. Enfin, **les signaux civils historiques ne sont pas authentifiés** : rien dans le signal n'atteste son origine.

**Ce que cela implique.** C'est l'exemple le plus net de ce que le chapitre 2 appelle une **infrastructure** : un système dont d'innombrables autres dépendent sans le posséder, sans l'avoir choisi et souvent sans le savoir. La dépendance la plus critique n'est pas la navigation — c'est **le temps**.

**Sûreté et sécurité.** En cas de perte du signal, les systèmes ne s'arrêtent pas tous : certains basculent sur une référence interne et **dérivent lentement**, d'autres continuent avec une position ou un temps faux. La dégradation est progressive, hétérogène et silencieuse — la pire combinaison pour un diagnostic. Les parades relèvent du principe : référence de temps locale de bonne stabilité, constellations multiples, croisement avec des sources non spatiales, contrôle de vraisemblance.

**À ne pas confondre avec.** **« GPS »**, qui désigne l'une des constellations et s'emploie abusivement comme nom générique. **Les systèmes d'augmentation**, qui améliorent la précision par des corrections transmises séparément.

> ⏱ **État au 23/08/2026** — 🏭 déployé, infrastructure critique. Plusieurs constellations opérationnelles ; l'authentification des signaux civils progresse mais le parc de récepteurs déployés ne l'exploite pas.
> 🔄 **À revoir si** une part significative du parc de récepteurs critiques bascule sur des signaux authentifiés — ou si une source de temps alternative de précision comparable devient largement disponible.

**Renvois** — Couche : percevoir, relier · Convergences : autonomie mobile (39), intelligence distribuée (38) · Voir aussi : chapitre 45 — les dépendances que personne n'a décidées.

---

## ◆◆◆ Navigation sans référence satellitaire

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Savoir où l'on se trouve quand le positionnement par satellite est indisponible, dégradé ou non fiable.

**Pourquoi on en parle.** Parce que la dépendance décrite à l'entrée précédente est massive, largement invisible, et que sa remise en cause est devenue un sujet d'ingénierie sérieux dans de nombreux domaines civils.

**Comment ça fonctionne.** Cinq familles de méthodes, souvent combinées.

**L'inertiel**, traité plus haut : autonome, mais dérivant.

**L'odométrie visuelle** : estimer son déplacement en suivant le mouvement apparent de points caractéristiques dans des images successives. Précise à court terme, dépendante de la texture de l'environnement et de l'éclairement, et dérivant elle aussi.

**L'appariement de terrain** : comparer ce que l'on perçoit — relief, image, signature magnétique, profondeur — à une carte de référence embarquée. Ne dérive pas, mais exige une carte, à jour, du territoire survolé ou parcouru.

**La navigation par signaux d'opportunité** : exploiter des émissions non destinées à la navigation — télécommunications, diffusion — dont la position des émetteurs est connue.

**La navigation céleste**, retrouvée avec l'automatisation : mesurer la position d'astres, ce qui est insensible à toute perturbation terrestre mais exige une visibilité du ciel et une référence de temps.

**Où vous rencontrerez le terme.** Aéronautique · maritime et sous-marin · robotique en intérieur · milieu souterrain · agriculture sous couvert · applications de défense.

**Ce que ça permet.** Poursuivre une mission en environnement dégradé · fonctionner là où le signal n'a jamais été disponible · détecter une incohérence entre sources et donc **repérer un positionnement erroné**, ce qui est parfois plus important que de s'en passer.

**Ce qui bloque.** **Aucune méthode n'est bonne partout.** L'inertiel dérive, la visuelle dépend de la scène, l'appariement dépend d'une carte, les signaux d'opportunité dépendent d'une infrastructure tierce. La combinaison est donc la règle — mais **elle ajoute ses propres modes de défaillance** : recalage entre sources, arbitrage en cas de désaccord, et corrélation des erreurs quand deux sources sont affectées par la même cause.

**De quoi ça dépend.** Capteurs inertiels · imagerie · cartes de référence · calcul embarqué · référence de temps locale.

**Ce que cela implique.** Ce domaine illustre un mécanisme général : **une dépendance devient visible au moment où elle devient contestable.** Le positionnement satellitaire était une commodité gratuite ; il est traité comme une infrastructure dont il faut prévoir l'indisponibilité.

**Sûreté et sécurité.** Traitement au niveau du principe et des conséquences systémiques uniquement : ce volume ne décrit aucune technique de perturbation ni aucune contre-mesure opérationnelle.

**À ne pas confondre avec.** **Le SLAM**, qui construit une carte tout en s'y localisant, sans référence absolue — il fournit une position relative, pas une position dans un repère global.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Composants matures pris séparément ; l'intégration robuste et certifiable est le sujet actif, avec une demande en forte croissance.
> 🔄 **À revoir si** un référentiel de certification impose une capacité de navigation de secours dans un secteur civil réglementé — ce qui transformerait un sujet d'ingénierie en obligation de conception.

**Renvois** — Couche : percevoir · Convergences : autonomie mobile (39) · Voir aussi : chapitre 45.

---

## ◆◆ Caméras événementielles

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Un capteur dont chaque pixel signale indépendamment un changement de luminosité, au lieu de produire des images entières à cadence fixe.

**Pourquoi on en parle.** Parce qu'il change la nature de la donnée produite : au lieu d'un flux d'images dont la plupart sont redondantes, on obtient un flux d'événements qui ne contient que ce qui bouge.

**Comment ça fonctionne.** Chaque pixel compare en permanence la luminosité qu'il reçoit à celle de son dernier signalement. Quand l'écart dépasse un seuil, il émet un événement horodaté. Il n'y a **ni image, ni cadence, ni temps de pose** — trois notions qui disparaissent.

**Ce que ça permet.** Une résolution temporelle très fine, de l'ordre de la microseconde · une dynamique très étendue, chaque pixel s'adaptant localement · un volume de données faible sur scène statique · une consommation réduite.

**Ce qui bloque.** **L'écosystème.** Les algorithmes, les jeux de données, les outils et les compétences ont tous été construits pour des images ; presque rien ne se transpose directement. C'est un cas typique du coût de sortie d'un standard dominant. S'y ajoutent le coût du capteur et l'absence d'information sur les zones immobiles.

**Ce que cela implique.** C'est une technologie qui gagne là où la cadence ou la dynamique sont le verrou — vibration, impact, scène très contrastée, mouvement rapide — et qui perd partout ailleurs, non pour des raisons physiques mais parce que l'écosystème n'existe pas.

**À ne pas confondre avec.** **Une caméra rapide**, qui produit beaucoup d'images ordinaires. Ici, il n'y a pas d'images du tout.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Capteurs disponibles commercialement, applications industrielles de niche établies, adoption générale limitée par l'écosystème logiciel.
> 🔄 **À revoir si** des modèles d'apprentissage traitant nativement des flux d'événements atteignent des performances comparables à celles obtenues sur images sur une tâche de référence.

**Renvois** — Couche : percevoir · Convergences : robotique généraliste (36), intelligence distribuée (38).

---

## ◆ Acoustique sous-marine

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Utiliser le son pour détecter, mesurer et communiquer sous l'eau, où les ondes électromagnétiques ne se propagent pratiquement pas.

**Où vous rencontrerez le terme.** Hydrographie · pêche · offshore et énergies marines · surveillance d'infrastructures sous-marines · robotique sous-marine · applications de défense.

**Ce qui bloque.** **La vitesse du son.** Environ mille cinq cents mètres par seconde, soit deux cent mille fois plus lent que la lumière : les délais de mesure et de communication se comptent en secondes, ce qui borne toute boucle de contrôle et toute coordination. S'y ajoutent la forte dépendance aux conditions du milieu — température, salinité, profondeur courbent les trajets — et un débit de communication très faible.

**À ne pas confondre avec.** **Le radar**, inutilisable sous l'eau, et **le lidar**, dont la portée y est de quelques dizaines de mètres au mieux.

> ⏱ **État au 23/08/2026** — 🏭 déployé, domaine mature. Progression du traitement et de l'autonomie des plateformes porteuses.
> 🔄 **À revoir si** un moyen de communication sous-marine à haut débit et longue portée devient disponible — ce qui lèverait la contrainte la plus structurante du domaine.

**Renvois** — Couche : percevoir · Convergence : autonomie mobile (39).

---

---
