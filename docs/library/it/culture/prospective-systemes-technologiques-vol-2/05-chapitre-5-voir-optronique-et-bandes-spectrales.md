---
title: 'Chapitre 5 — Voir : optronique et bandes spectrales'
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 5
chapters: 14
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte générale — aucune mesure sans bruit, sans résolution finie, sans conditions d'observation. Ce chapitre traite de ce qui se voit par **rayonnement électromagnétique dans les bandes optiques**, c'est-à-dire de la manière dont on obtient une image sans contact.
>
> **Six entrées.** Deux définissent le domaine, trois traitent des manières de le pousser, une est là pour éviter une confusion très répandue.

---

### ◆◆◆ Optronique — *electro-optics, EO/IR*

**Niveau** — catégorie industrielle · **Couche** — percevoir

**En une phrase.** L'optronique désigne la filière des systèmes qui produisent une information exploitable à partir de rayonnement optique — du détecteur élémentaire jusqu'à l'équipement complet.

**Pourquoi on en parle.** C'est le vocabulaire dominant de la perception à distance dans l'industrie, l'aéronautique, le spatial et la défense. Vous l'entendrez plus souvent que « caméra » ou « capteur d'image », et il désigne quelque chose de plus large.

**Comment ça fonctionne.** Une chaîne optronique comporte quatre étages : une **optique** qui collecte le rayonnement et le concentre ; un **détecteur** qui le convertit en signal électrique ; une **électronique de proximité** qui amplifie, numérise et corrige ; et un **traitement** qui produit l'information utile. La performance d'ensemble est bornée par le maillon le plus faible, et rarement par le détecteur — c'est le contresens le plus fréquent du domaine.

À cela s'ajoutent, dans les équipements complets, une **stabilisation** — sans laquelle une optique à fort grossissement est inutilisable sur un porteur mobile — et parfois un **refroidissement**.

**Où vous rencontrerez le terme.** Défense et sécurité · aéronautique · spatial et observation de la Terre · contrôle industriel · systèmes de vision pour véhicules · surveillance d'infrastructures · instrumentation scientifique.

**Ce que ça permet.** Voir loin, voir dans l'obscurité, voir à travers certaines conditions dégradées, mesurer sans contact, détecter un écart de température, discriminer des matériaux.

**Ce qui bloque.** Trois choses, dans cet ordre. **Le coût de l'optique**, qui croît fortement avec le diamètre et la qualité de surface — et non le coût du détecteur, qui a beaucoup baissé. **Le refroidissement**, quand la bande l'exige : il ajoute masse, consommation, bruit mécanique et une durée de vie limitée. Et **la disponibilité de certains matériaux de détection**, dont la chaîne est étroite.

**De quoi ça dépend.** Optique de précision · matériaux de détection · microélectronique de lecture · calcul embarqué · mécanique de stabilisation · énergie.

**Ce que cela implique.** L'optronique est une filière **où l'assemblage vaut davantage que le composant**. Deux équipements à détecteur identique peuvent avoir des performances opérationnelles très différentes selon l'optique, la stabilisation et le traitement. C'est pourquoi les comparaisons par caractéristique de détecteur sont peu informatives.

**Sûreté et sécurité.** Un système optronique est un capteur : il peut être ébloui, saturé ou trompé par l'environnement, sans que rien ne distingue une saturation d'une absence de cible. Ce volume traite ces phénomènes au niveau du principe et de leurs conséquences systémiques, sans élément de mise en œuvre.

**À ne pas confondre avec.** **La vision par ordinateur**, qui est un traitement et non une chaîne de capture. **Le radar**, qui exploite des longueurs d'onde bien plus grandes et n'a ni les mêmes performances ni les mêmes limites. **La « caméra »**, qui désigne le plus souvent le seul étage de capture visible.

**Termes voisins.** *Electro-optics* et *EO/IR* dans l'usage anglophone — les trois termes sont interchangeables. *Imagerie* désigne le résultat, pas la filière.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Filière mature, en croissance tirée par l'observation, l'autonomie et la sécurité. La baisse de coût des détecteurs non refroidis a ouvert des usages civils de masse ; les segments à hautes performances restent contraints par l'optique et le refroidissement.
> 🔄 **À revoir si** un procédé de fabrication d'optiques de grande dimension à coût significativement réduit atteint la production série.

**Renvois** — Couche : percevoir · Courant : optronique (ch. 35) · Convergences : autonomie mobile (39), robotique généraliste (36).

---

### ◆◆◆ Les bandes infrarouges — *NIR, SWIR, MWIR, LWIR*

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Selon la longueur d'onde observée, on ne voit pas la même chose : dans certaines bandes on voit ce qui est éclairé, dans d'autres on voit ce qui est chaud.

**Pourquoi on en parle.** C'est la distinction la plus utile de toute la couche, et la plus mal maîtrisée. Elle explique pourquoi il existe plusieurs familles de capteurs qui semblent faire la même chose, pourquoi leurs prix diffèrent d'un facteur cent, et pourquoi aucune ne remplace les autres.

**Comment ça fonctionne.** Tout corps émet un rayonnement du seul fait de sa température, et **plus il est chaud, plus ce rayonnement se déplace vers les courtes longueurs d'onde**. Un corps à température ambiante émet principalement autour de dix micromètres ; un moteur chaud dans l'infrarouge moyen ; le soleil dans le visible.

Il en découle deux manières de voir, radicalement différentes :

**Voir par réflexion** — une source éclaire la scène, les objets renvoient une partie du rayonnement. C'est le cas du visible, du proche infrarouge et du SWIR. Sans source, pas d'image.

**Voir par émission** — le capteur capte ce que les objets émettent eux-mêmes. C'est le cas du MWIR et du LWIR. **Aucun éclairage n'est nécessaire.**

| Bande | Domaine approximatif | Ce qu'on voit | Particularité |
|---|---|---|---|
| Visible | 0,4 – 0,7 µm | scène éclairée | proche de la perception humaine |
| NIR | 0,7 – 1 µm | scène faiblement éclairée | détecteurs silicium, peu coûteux |
| SWIR | 1 – 2,5 µm | réflexion, avec meilleure pénétration de brume | discrimination de matériaux, lecture à travers certains matériaux |
| MWIR | 3 – 5 µm | émission de corps chauds | fort contraste thermique, détecteurs souvent refroidis |
| LWIR | 8 – 14 µm | émission de corps à température ambiante | vision nocturne sans éclairage, détecteurs non refroidis possibles |

**L'atmosphère n'est pas transparente partout.** Certaines longueurs d'onde sont fortement absorbées par la vapeur d'eau et le dioxyde de carbone. Les bandes utilisées correspondent aux **fenêtres** où l'absorption est faible — ce n'est pas un choix technique mais une contrainte physique, et elle explique les intervalles du tableau ci-dessus.

**Où vous rencontrerez le terme.** Vision nocturne · maintenance prédictive et thermographie de bâtiment · agriculture · tri industriel · sécurité incendie · observation spatiale · véhicules · applications médicales.

**Ce que ça permet.** Voir sans éclairage · détecter un échauffement anormal avant qu'il ne soit visible · distinguer des matériaux d'apparence identique · voir partiellement à travers brume ou fumée selon la bande.

**Ce qui bloque.** **Le refroidissement**, pour les bandes moyennes : atteindre une sensibilité utile suppose souvent de descendre le détecteur à très basse température, ce qui ajoute un cryogénérateur — masse, consommation, bruit, durée de vie de quelques milliers d'heures. **La résolution**, bornée par le rapport entre longueur d'onde et diamètre d'optique : à ouverture égale, plus la longueur d'onde est grande, plus le détail accessible est grossier. Et **le coût des matériaux de détection** hors silicium.

**De quoi ça dépend.** Matériaux semi-conducteurs spécifiques à chaque bande · optiques transparentes dans la bande visée — le verre ordinaire ne l'est pas au-delà du proche infrarouge · cryogénie pour certaines applications.

**Ce que cela implique.** Un système de perception sérieux **combine plusieurs bandes**, parce qu'aucune n'est bonne partout. Et une performance annoncée n'a de sens qu'accompagnée de la bande : « voit dans le noir » peut désigner un dispositif à quelques centaines d'euros ou à plusieurs dizaines de milliers.

**À ne pas confondre avec.** **La vision nocturne par intensification**, qui amplifie la lumière résiduelle et exige donc qu'il en reste — voir l'entrée dédiée. **Le thermique et l'infrarouge en général** : tout thermique est infrarouge, tout infrarouge n'est pas thermique.

**Termes voisins.** *Imagerie thermique* désigne l'usage des bandes d'émission. *Bolométrie* désigne une technologie de détection, pas une bande.

> ⏱ **État au 23/08/2026** — 🏭 déployé, avec des maturités inégales selon les bandes. LWIR non refroidi : diffusion large, y compris grand public. SWIR : coût encore élevé, applications industrielles en croissance. MWIR refroidi : réservé aux hautes performances.
> 🔄 **À revoir si** une technologie de détection SWIR compatible avec les procédés silicium standard atteint la production série — cela déplacerait le coût de cette bande d'un ordre de grandeur.

**Renvois** — Couche : percevoir · Courant : optronique (ch. 35) · Convergences : autonomie mobile (39).

---

### ◆◆ Détecteurs refroidis et non refroidis

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Deux familles de détecteurs infrarouges, dont l'une exige d'être portée à très basse température pour fonctionner utilement.

**Pourquoi on en parle.** Cette distinction commande le prix, la masse, la consommation et la durée de vie de tout système d'imagerie thermique — et elle n'apparaît presque jamais dans les descriptions commerciales.

**Comment ça fonctionne.** Un **détecteur quantique** convertit directement les photons en porteurs de charge. Il est rapide et sensible, mais son propre bruit thermique noierait le signal à température ambiante : il faut le refroidir, souvent autour de 77 kelvins, à l'aide d'un cryogénérateur mécanique.

Un **détecteur thermique**, ou bolomètre, mesure l'échauffement d'une microstructure sous l'effet du rayonnement. Il fonctionne à température ambiante, mais il est plus lent — sa constante de temps se compte en millisecondes — et moins sensible.

**Ce que ça permet.** Le refroidi : détection à longue portée, discrimination de faibles écarts de température, cadences élevées. Le non refroidi : imagerie thermique compacte, silencieuse, à faible consommation, et à un coût qui a permis sa diffusion massive.

**Ce qui bloque.** Pour le refroidi, le **cryogénérateur** : c'est une pièce mécanique en mouvement permanent, dont la durée de vie borne celle du système et qui produit vibrations et consommation. Pour le non refroidi, **la sensibilité et la cadence**, qui plafonnent pour des raisons physiques.

**De quoi ça dépend.** Matériaux de détection · microfabrication · cryogénie · circuits de lecture.

**À ne pas confondre avec.** La distinction **refroidi / non refroidi** n'est pas la distinction **MWIR / LWIR**, bien qu'elles se recoupent largement dans la pratique.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Le non refroidi domine en volume et continue de progresser en résolution ; le refroidi reste indispensable aux hautes performances.
> 🔄 **À revoir si** un détecteur non refroidi atteint une sensibilité et une cadence comparables à celles d'un détecteur refroidi de génération courante.

**Renvois** — Couche : percevoir · Convergence : autonomie mobile (39).

---

### ◆◆ Imagerie hyperspectrale

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Mesurer, pour chaque point d'une image, non pas trois couleurs mais des dizaines ou des centaines de bandes spectrales étroites.

**Pourquoi on en parle.** Parce que la signature spectrale d'un matériau permet de l'identifier sans contact — une capacité qui n'a aucun équivalent dans l'imagerie ordinaire.

**Comment ça fonctionne.** Le rayonnement collecté est décomposé — par un réseau, un prisme ou un filtre variable — et chaque bande est mesurée séparément. On obtient un **cube de données** : deux dimensions spatiales, une dimension spectrale. L'identification se fait en comparant la signature mesurée à des bibliothèques de référence.

**Où vous rencontrerez le terme.** Observation spatiale · agriculture de précision · tri de matériaux et recyclage · contrôle alimentaire · minéralogie · applications médicales · surveillance environnementale.

**Ce que ça permet.** Identifier un matériau, un état de maturité, un taux d'humidité, une contamination — là où une image ordinaire ne montre qu'une différence de teinte.

**Ce qui bloque.** **Le compromis fondamental** : mesurer beaucoup de bandes signifie moins de photons par bande, donc soit un temps de pose plus long, soit une résolution spatiale plus grossière, soit une optique plus grande. On ne peut pas maximiser résolution spatiale, résolution spectrale et cadence. S'y ajoutent le **volume de données** produit et le fait que **l'exploitation exige des bibliothèques de référence** propres à chaque application.

**De quoi ça dépend.** Optique de décomposition · détecteurs à faible bruit · calcul pour le traitement du cube · bases de données spectrales.

**Ce que cela implique.** L'hyperspectral est une technologie où **la donnée brute vaut peu et le modèle d'interprétation vaut beaucoup**. C'est ce qui rend son déploiement sectoriel plutôt que général.

**À ne pas confondre avec.** **Le multispectral**, qui mesure quelques bandes choisies plutôt que des centaines contiguës. La différence n'est pas de degré : le multispectral cible des signatures connues, l'hyperspectral permet d'en découvrir.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Mature en observation spatiale et en tri industriel ; en croissance en agriculture ; coût encore élevé pour les usages embarqués.
> 🔄 **À revoir si** des capteurs hyperspectraux compacts atteignent un coût compatible avec une intégration sur plateformes mobiles de masse.

**Renvois** — Couche : percevoir · Convergence : intelligence distribuée (38).

---

### ◆◆ Imagerie computationnelle

**Niveau** — capacité · **Couche** — percevoir, calculer

**En une phrase.** Concevoir conjointement l'optique et l'algorithme, de sorte que l'image finale soit reconstruite plutôt que directement captée.

**Pourquoi on en parle.** Parce qu'elle déplace une partie du coût de l'optique vers le calcul — ce qui, dans un monde où le calcul est bon marché et l'optique chère, change les architectures possibles.

**Comment ça fonctionne.** Plutôt que de former une image nette sur le détecteur, on capte une mesure volontairement encodée — par une ouverture codée, un masque, plusieurs prises de vue légèrement différentes — puis on reconstruit l'image par calcul. Le capteur ne mesure plus l'image : il mesure de quoi la reconstruire.

**Où vous rencontrerez le terme.** Photographie mobile · microscopie · imagerie médicale · observation spatiale · capteurs compacts.

**Ce que ça permet.** Réduire l'encombrement optique · dépasser certaines limites de profondeur de champ ou de dynamique · reconstruire une information de distance à partir de plusieurs prises.

**Ce qui bloque.** **La reconstruction est une inférence.** Ce qui est produit dépend d'hypothèses sur la scène ; quand ces hypothèses ne tiennent pas, l'algorithme produit une image plausible et fausse, sans le signaler. S'y ajoute le coût en calcul, qui déplace la contrainte vers l'énergie du dispositif.

**Ce que cela implique.** **La distinction entre mesure et inférence devient opérationnelle.** Dans une chaîne computationnelle, une partie de ce que vous voyez a été acquise et une partie a été reconstruite. Pour un usage esthétique, la distinction importe peu ; pour une mesure, une preuve ou une décision automatique, elle est décisive.

**À ne pas confondre avec.** **Le post-traitement d'image**, qui améliore une image déjà formée. Ici, l'optique elle-même est conçue pour ne pas former d'image.

> ⏱ **État au 23/08/2026** — 🏭 déployé en photographie grand public, 🔬 émergent en instrumentation.
> 🔄 **À revoir si** une exigence réglementaire ou probatoire impose de distinguer, dans une image, ce qui est mesuré de ce qui est reconstruit.

**Renvois** — Couche : percevoir, calculer · Convergence : intelligence distribuée (38).

---

### ◆ Intensification d'image

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Amplifier la lumière résiduelle d'une scène nocturne pour la rendre visible.

**Où vous rencontrerez le terme.** Vision nocturne · sécurité · applications de défense · astronomie amateur.

**Ce qui bloque.** **Il faut qu'il reste de la lumière.** Un intensificateur ne crée rien : il amplifie des photons existants. Dans l'obscurité totale, il ne voit rien — contrairement à un imageur thermique.

**À ne pas confondre avec.** **L'imagerie thermique.** C'est la confusion la plus fréquente du chapitre : les deux sont appelés « vision nocturne » et reposent sur des principes opposés. L'un amplifie la lumière réfléchie, l'autre capte l'émission propre des objets. L'un est aveuglé par une source vive, l'autre non ; l'un ne voit rien sans lumière, l'autre voit un corps chaud dans le noir absolu.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie mature. Progressivement concurrencée par les capteurs à très faible bruit en bandes visible et proche infrarouge.
> 🔄 **À revoir si** des capteurs numériques à faible bruit atteignent des performances équivalentes à un coût et une consommation comparables.

**Renvois** — Couche : percevoir.

---


## Chapitre 6 — Mesurer la distance, la forme et le mouvement

> **Ce que ce chapitre ajoute.** Le chapitre 5 traitait de ce qui se voit. Celui-ci traite de ce qui se **mesure** : à quelle distance, à quelle vitesse, dans quelle direction, et où se trouve le capteur lui-même.
>
> **Une contrainte commune à toutes les entrées.** Mesurer une distance revient à mesurer un temps — celui que met un signal à faire l'aller-retour — ou à mesurer un déphasage. La précision d'une distance est donc bornée par la précision d'une horloge, et c'est ce qui relie ce chapitre au positionnement.
>
> **Huit entrées**, dont trois traitent d'un sujet que la plupart des ouvrages omettent : que se passe-t-il quand le positionnement satellitaire n'est plus disponible.

---

### ◆◆◆ Lidar

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

### ◆◆ Radar imageur

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

### ◆◆◆ SAR — ouverture synthétisée

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

### ◆◆ Capteurs inertiels

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

### ◆◆ GNSS et positionnement par satellite

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

### ◆◆◆ Navigation sans référence satellitaire

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

### ◆◆ Caméras événementielles

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

### ◆ Acoustique sous-marine

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


## Chapitre 7 — Percevoir autrement

> **Ce que ce chapitre ajoute.** Les chapitres 5 et 6 traitaient de ce qui se voit et de ce qui se mesure par ondes électromagnétiques. Celui-ci traite de tout le reste : les grandeurs physiques, chimiques et biologiques qu'on convertit en information par d'autres moyens.
>
> **Un fil conducteur.** La plupart de ces entrées partagent une propriété : elles mesurent des signaux **très faibles**, à la limite de ce que le bruit permet. C'est ce qui explique leur coût, leur encombrement, et le fait que plusieurs d'entre elles n'aient quitté le laboratoire que récemment.
>
> **Huit entrées**, dont une majeure — les capteurs quantiques — et une qui n'est pas un capteur au sens habituel : la perception distribuée, qui est un fait d'architecture.

---

### ◆◆◆ Capteurs quantiques

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Des capteurs qui exploitent des propriétés quantiques de la matière ou de la lumière pour mesurer avec une sensibilité et une stabilité inaccessibles autrement.

**Pourquoi on en parle.** Parce que c'est **la branche des technologies quantiques la plus proche du déploiement réel** — et parce qu'elle est systématiquement confondue avec le calcul quantique, dont la maturité est sans commune mesure.

**Comment ça fonctionne.** Le principe commun est d'utiliser un système quantique comme instrument de mesure, plutôt que comme unité de calcul. Un atome, un défaut cristallin ou un nuage d'atomes refroidis possède des niveaux d'énergie extrêmement stables et prévisibles ; une perturbation extérieure — champ magnétique, accélération, gravité, température — modifie ces niveaux d'une manière que l'on peut mesurer très précisément.

**L'avantage décisif n'est pas seulement la sensibilité : c'est l'absence de dérive.** Un capteur classique se déforme, vieillit et doit être réétalonné par comparaison à une référence. Un capteur quantique se réfère à des constantes physiques : il **est** sa propre référence. Cela supprime le problème que le chapitre 6 a identifié comme le plus dangereux de la couche.

**Trois familles à connaître.** Les **horloges** atomiques, qui fournissent une référence temporelle ; les **magnétomètres** et gravimètres, qui mesurent des champs très faibles ; et les **capteurs inertiels** quantiques, qui mesurent accélération et rotation par interférométrie atomique.

**Où vous rencontrerez le terme.** Métrologie et étalonnage · prospection géophysique · imagerie médicale fonctionnelle · navigation en environnement dégradé · surveillance de sous-sol et d'ouvrages · synchronisation de réseaux.

**Ce que ça permet.** Mesurer sans dérive · détecter des variations de densité du sous-sol depuis la surface · fournir une référence de temps locale de très haute stabilité · à terme, une navigation inertielle dont la dérive serait d'un ordre de grandeur inférieure.

**Ce qui bloque.** **L'encombrement et l'environnement de fonctionnement.** Beaucoup de ces dispositifs exigent un vide poussé, un refroidissement, un blindage magnétique ou une immobilité relative — conditions difficiles à réunir sur un porteur mobile, qui est précisément là où ils seraient les plus utiles. S'y ajoutent le coût, la consommation, et la disponibilité de composants optiques et laser spécialisés.

**De quoi ça dépend.** Sources laser stabilisées · optique de précision · vide et cryogénie selon les familles · blindage · électronique de contrôle · matériaux à défauts contrôlés.

**Ce que cela implique.** Le verrou de cette famille est **la miniaturisation, pas la physique**. La capacité est démontrée ; ce qui reste à franchir est industriel. C'est une situation différente de celle du calcul quantique, où des questions de principe restent ouvertes — et c'est exactement pourquoi les réunir sous un même mot induit en erreur.

**Sûreté et sécurité.** Une référence de temps locale de haute stabilité réduit la dépendance à une source externe. C'est traité au niveau du principe ; ce volume ne décrit aucune technique de perturbation ni de contre-mesure.

**À ne pas confondre avec.** **Le calcul quantique**, dont ces capteurs ne partagent ni la maturité, ni les verrous, ni les applications. Un progrès en capteurs quantiques n'indique **rien** sur le calcul quantique — c'est le coût direct de la catégorie *Quantum Tech* signalé au chapitre 35.

**Termes voisins.** *Quantum sensing* dans l'usage anglophone. *Métrologie quantique* insiste sur l'aspect référence.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des segments 🏭 déployés. Les horloges atomiques sont une technologie mature en usage opérationnel. Magnétométrie et gravimétrie sont en déploiement dans des applications spécialisées. Les capteurs inertiels quantiques restent en démonstration ou en pré-série, avec un enjeu de miniaturisation.
> 🔄 **À revoir si** un capteur inertiel quantique atteint un volume et une consommation compatibles avec une intégration sur porteur mobile standard.

**Renvois** — Couche : percevoir · Courants : Quantum Tech (ch. 35), Deep Tech (ch. 35) · Convergence : autonomie mobile (39) · Voir aussi : calcul quantique (ch. 10), pour la distinction.

---

### ◆◆ Biocapteurs

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Des capteurs qui utilisent un élément biologique — enzyme, anticorps, brin d'ADN, cellule — pour reconnaître spécifiquement une molécule cible et convertir cette reconnaissance en signal mesurable.

**Pourquoi on en parle.** Parce qu'ils déplacent la mesure biologique du laboratoire vers le lieu où la question se pose : au chevet du patient, dans un cours d'eau, sur une ligne de production.

**Comment ça fonctionne.** Deux étages. Un **élément de reconnaissance** biologique se lie sélectivement à la molécule recherchée. Un **transducteur** convertit cet événement de liaison en signal — variation de courant, de masse, de couleur, de fluorescence. La sélectivité vient du biologique ; la sensibilité vient du transducteur.

**Où vous rencontrerez le terme.** Diagnostic médical décentralisé · surveillance de glycémie · contrôle alimentaire · qualité de l'eau · sécurité industrielle · recherche.

**Ce que ça permet.** Une mesure spécifique sans laboratoire, sans préparation lourde et parfois en continu — ce dernier point étant celui qui change le plus les usages.

**Ce qui bloque.** **La stabilité de l'élément biologique.** Une enzyme ou un anticorps se dégrade avec le temps, la température et l'usage : la durée de vie utile est souvent le facteur limitant, davantage que la sensibilité. S'y ajoutent **l'encrassement** en milieu réel — protéines et cellules se déposent sur la surface et modifient la réponse — et la difficulté d'obtenir une mesure quantitative stable plutôt qu'une simple détection.

**De quoi ça dépend.** Biologie moléculaire · microfabrication · électronique à faible bruit · chimie de surface.

**Ce que cela implique.** Un biocapteur en service dérive, et sa dérive ne se signale pas. En usage ponctuel, on utilise des consommables à usage unique ; en usage continu, il faut une stratégie de recalage — le problème central de la couche, sous une forme biologique.

**À ne pas confondre avec.** **Les capteurs chimiques**, qui reposent sur une réaction physico-chimique sans élément biologique : moins sélectifs, mais bien plus stables dans le temps.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour quelques applications de masse, 🔬 émergent pour la mesure continue multi-analytes.
> 🔄 **À revoir si** un élément de reconnaissance non biologique atteint la sélectivité d'un anticorps avec la stabilité d'un capteur physique.

**Renvois** — Couche : percevoir · Courant : HealthTech (ch. 35) · Convergences : découverte scientifique (37), biologie programmable (41).

---

### ◆ Capteurs chimiques

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Détecter la présence et la concentration de composés par une interaction physico-chimique avec un matériau sensible.

**Où vous rencontrerez le terme.** Sécurité industrielle · qualité de l'air · agroalimentaire · détection de fuites · contrôle de procédés · applications de sécurité civile.

**Ce qui bloque.** **La sélectivité.** Un capteur chimique répond souvent à plusieurs composés à la fois, ce qui produit des fausses alarmes ou masque la cible. La parade consiste à combiner plusieurs capteurs peu sélectifs et à traiter la signature d'ensemble — c'est le principe du « nez électronique » —, ce qui déplace la difficulté vers l'étalonnage et vers la constitution de bases de référence.

**À ne pas confondre avec.** **Les biocapteurs**, plus sélectifs et moins stables. **La spectrométrie**, qui identifie par analyse spectrale plutôt que par interaction chimique, avec une sélectivité supérieure et un encombrement sans commune mesure.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Progrès continus sur la miniaturisation et sur le traitement de signatures multi-capteurs.
> 🔄 **À revoir si** un capteur miniature atteint une sélectivité comparable à celle d'un instrument de laboratoire.

**Renvois** — Couche : percevoir.

---

### ◆ MEMS avancés

**Niveau** — composant · **Couche** — percevoir, agir

**En une phrase.** Des structures mécaniques microscopiques fabriquées par les procédés de la microélectronique, servant à mesurer ou à actionner.

**Pourquoi on en parle.** Parce qu'ils sont omniprésents et invisibles : accéléromètres, gyromètres, microphones, capteurs de pression, micro-miroirs de projection ou de balayage laser. Presque toute mesure physique embarquée passe par eux.

**Ce que ça permet.** Une mesure physique à un coût unitaire de quelques dizaines de centimes, dans un volume de quelques millimètres cubes — c'est ce qui a rendu possible l'instrumentation de masse.

**Ce qui bloque.** **La performance plafonne** pour des raisons d'échelle : plus une structure est petite, plus elle est sensible aux effets de surface et au bruit thermique. C'est pourquoi les instruments de haute performance ne sont pas des MEMS agrandis mais des dispositifs de conception entièrement différente. S'y ajoute la sensibilité aux contraintes mécaniques du boîtier, qui provoque une dérive difficile à distinguer d'un signal réel.

**À ne pas confondre avec.** **Les capteurs de haute performance** de même fonction : un gyromètre MEMS et un gyromètre optique portent le même nom de fonction et sont séparés par plusieurs ordres de grandeur de performance et de prix.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie de masse mature.
> 🔄 **À revoir si** un procédé compatible avec la microfabrication de masse atteint des performances aujourd'hui réservées aux technologies non-MEMS.

**Renvois** — Couche : percevoir, agir · Convergence : intelligence distribuée (38).

---

### ◆◆ Peau électronique et perception tactile

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Doter une machine d'une sensibilité au contact : force, pression, glissement, texture, température.

**Pourquoi on en parle.** Parce que c'est **le verrou identifié de la manipulation robotique**, et l'un des rares cas où l'absence d'un sens explique directement l'échec d'une capacité.

**Comment ça fonctionne.** Plusieurs principes coexistent : mesure de la déformation d'un matériau conducteur, variation de capacité, mesure optique de la déformation d'une membrane souple, ou capteurs de force intégrés aux articulations. Les approches optiques donnent une richesse d'information remarquable — on peut y lire la texture et le début de glissement — au prix d'un encombrement et d'un besoin de calcul.

**Ce que ça permet.** Saisir un objet dont on ignore la masse et la rigidité · détecter le glissement avant la chute · adapter la force à l'objet · manipuler sans vision, ce que l'humain fait en permanence.

**Ce qui bloque.** **La durabilité.** Un capteur tactile est, par construction, la partie qui frotte, qui reçoit les chocs et qui s'use. Une peau qui se dégrade produit des mesures fausses sans le signaler. S'y ajoutent le **câblage** — connecter des milliers de points sur une surface souple et mobile est un problème mécanique difficile — et l'absence de standard, qui empêche de mutualiser les données entre plateformes.

**Ce que cela implique.** C'est une capacité où **le verrou n'est pas la sensibilité mais la tenue dans le temps**. Les démonstrations sont convaincantes ; les déploiements butent sur le nombre d'heures de fonctionnement.

**À ne pas confondre avec.** **Les capteurs de force articulaires**, qui mesurent l'effort global d'un membre et non le contact local — ils ne détectent pas le glissement.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Nombreuses démonstrations, quelques intégrations industrielles, pas de solution dominante.
> 🔄 **À revoir si** une peau tactile démontre plusieurs milliers d'heures de fonctionnement sans dérive significative sur une plateforme en exploitation.

**Renvois** — Couche : percevoir · Convergence : robotique généraliste (36).

---

### ◆◆ La fibre optique comme capteur

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Utiliser une fibre optique déjà installée, non pour transmettre, mais pour mesurer ce qui se passe tout au long de son parcours.

**Pourquoi on en parle.** Parce que c'est un cas remarquable de **détournement d'une infrastructure existante en instrument** — et parce que cela transforme des dizaines de kilomètres de câble en un capteur continu.

**Comment ça fonctionne.** On injecte une impulsion lumineuse dans la fibre et on analyse la lumière rétrodiffusée par les imperfections du verre. Une vibration, une déformation ou un changement de température modifie localement cette rétrodiffusion. En mesurant le délai de retour, on localise l'événement le long de la fibre — le principe est celui du chapitre 6, appliqué à l'intérieur d'un câble.

**Où vous rencontrerez le terme.** Surveillance de pipelines · sécurité périmétrique · suivi de puits · surveillance ferroviaire · ouvrages d'art · sismologie · surveillance de câbles sous-marins.

**Ce que ça permet.** Un capteur **continu et non ponctuel** sur des dizaines de kilomètres, sans alimentation ni électronique le long du parcours, et souvent sur une fibre déjà posée.

**Ce qui bloque.** **L'interprétation.** Le système produit un volume considérable de signaux dont l'exploitation exige de distinguer un événement pertinent d'un bruit ambiant — travaux, trafic, météo. C'est un problème de classification, et il conditionne l'utilité entière du dispositif. S'y ajoutent le coût de l'interrogateur et la difficulté de localiser précisément un événement en trois dimensions.

**Ce que cela implique.** C'est un exemple net d'une technologie dont **le verrou n'est pas dans le capteur mais dans le traitement**, et dont l'infrastructure était déjà là. Le déploiement dépend donc du coût du calcul et de la disponibilité de données annotées, non de la physique.

**À ne pas confondre avec.** **Les réseaux de Bragg**, qui utilisent des fibres spécialement gravées pour mesurer en des points définis — mesure ponctuelle et précise, contre mesure continue et statistique.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans plusieurs secteurs industriels, en croissance.
> 🔄 **À revoir si** l'interrogateur descend à un coût permettant l'équipement systématique de réseaux de télécommunications existants.

**Renvois** — Couche : percevoir · Convergence : intelligence distribuée (38).

---

### ◆ Détection radiologique

**Niveau** — famille · **Couche** — percevoir

**En une phrase.** Détecter et caractériser des rayonnements ionisants, pour la sûreté, la sécurité, la médecine ou la science.

**Où vous rencontrerez le terme.** Sûreté nucléaire · imagerie médicale · contrôle non destructif · sécurité portuaire et frontalière · instrumentation spatiale · géologie.

**Ce qui bloque.** **La distinction entre détecter et identifier.** Détecter un rayonnement est relativement simple ; déterminer quel isotope l'émet exige une résolution spectrale que seuls certains détecteurs offrent, souvent au prix d'un refroidissement. S'y ajoute le compromis entre sensibilité et encombrement : un détecteur sensible est un détecteur volumineux, parce qu'il faut de la matière pour arrêter le rayonnement.

**À ne pas confondre avec.** **La dosimétrie**, qui mesure une exposition cumulée pour la protection des personnes, et non la présence instantanée d'une source.

> ⏱ **État au 23/08/2026** — 🏭 déployé, domaine mature. Progrès sur les détecteurs à semi-conducteurs fonctionnant sans refroidissement.
> 🔄 **À revoir si** un détecteur à résolution spectrale fonctionnant à température ambiante atteint un coût de série.

**Renvois** — Couche : percevoir.

---

### ◆◆ Perception distribuée

**Niveau** — système · **Couche** — percevoir, relier

**En une phrase.** Construire une représentation partagée à partir de nombreux capteurs répartis, plutôt qu'à partir d'un capteur unique performant.

**Pourquoi on en parle.** Parce que c'est un changement d'architecture et non de technologie : **la question devient combien de capteurs médiocres valent un capteur excellent, et à quelles conditions**.

**Comment ça fonctionne.** Chaque nœud produit une observation partielle, datée et localisée. Un traitement — centralisé ou réparti — combine ces observations en une représentation commune. Trois problèmes se posent, et ils sont les mêmes que ceux de la fusion de capteurs, à une échelle supérieure : **le recalage** — ramener toutes les mesures à une référence spatiale et temporelle commune ; **le désaccord** — que faire quand deux nœuds disent des choses différentes ; et **la corrélation des erreurs** — le gain de la combinaison suppose l'indépendance, que le brouillard, l'éblouissement ou une panne d'alimentation commune détruisent.

**Où vous rencontrerez le terme.** Véhicules communicants · surveillance d'infrastructures · agriculture · défense · robotique en flotte · villes instrumentées.

**Ce que ça permet.** Voir au-delà de l'horizon d'un capteur unique · disposer de plusieurs points de vue sur le même objet · maintenir une observation quand un nœud est occulté ou défaillant · réduire le coût unitaire au prix du nombre.

**Ce qui bloque.** **La datation.** Combiner des observations suppose de savoir précisément quand chacune a été prise ; une erreur de datation produit une erreur de fusion qui ressemble à une erreur de mesure. Cela renvoie directement à la dépendance temporelle décrite au chapitre 6. S'y ajoutent la bande passante, l'énergie des nœuds, et **la confiance** : un nœud compromis injecte des observations authentiques et fausses.

**Ce que cela implique.** La perception distribuée **ajoute ses propres modes de défaillance** — elle n'additionne pas seulement des qualités. Une fusion bien réglée produit une estimation plus précise et une incertitude annoncée plus faible ; si cette incertitude est sous-estimée, le système devient confiant à tort, ce qui est plus dangereux qu'un système incertain.

**À ne pas confondre avec.** **La fusion de capteurs** sur une même plateforme, où le recalage est un problème de conception résolu une fois. Ici, les nœuds sont indépendants, mobiles, de qualités inégales et parfois non fiables.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Déployée dans des périmètres maîtrisés ; l'extension à des nœuds hétérogènes et non contrôlés reste le sujet ouvert.
> 🔄 **À revoir si** un mécanisme d'attestation au niveau du capteur devient déployable à grande échelle, ce qui rendrait traitable la question de la confiance entre nœuds.

**Renvois** — Couche : percevoir, relier · Convergences : intelligence distribuée (38), découverte scientifique (37) · Voir aussi : identité machine (ch. 29).

---


## Clôture de la couche A — Percevoir

### Ce que les vingt-deux entrées font apparaître

**Un.** La couche compte **peu de verrous physiques et beaucoup de verrous d'exploitation**. Sur vingt-deux entrées, quatre seulement butent sur une limite de principe — résolution bornée par la longueur d'onde, plancher de bruit, vitesse du son, dérive inertielle. Les dix-huit autres butent sur le coût, la durabilité, l'étalonnage, l'interprétation ou l'écosystème.

**Deux.** **La dérive est le fil rouge de toute la couche.** Elle apparaît sous six noms différents : dérive inertielle, dérive de biocapteur, usure de peau tactile, encrassement de capteur chimique, contrainte mécanique sur MEMS, désynchronisation d'un nœud distribué. C'est le même phénomène — la relation entre grandeur physique et signal se déforme lentement — et il produit toujours la même conséquence : **des valeurs plausibles et fausses, sans alerte**.

**Trois.** **Le traitement a absorbé une part croissante de la performance.** Imagerie computationnelle, SAR, fibre-capteur, perception distribuée, nez électronique : dans cinq entrées au moins, ce qui limite n'est plus le capteur mais l'algorithme et la donnée de référence. Cela déplace le verrou de la couche *percevoir* vers la couche *calculer* — et c'est un déplacement que la carte de couche n'avait pas anticipé.

**Quatre.** **Deux entrées de cette couche sont des infrastructures**, au sens strict du chapitre 2 : le positionnement satellitaire et, dans une moindre mesure, les réseaux de fibre détournés en capteurs. Toutes deux figurent au dossier du chapitre 45.

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **36 — Robotique généraliste** | peau électronique, fusion, lidar, inertiel, caméras événementielles |
| **37 — Découverte scientifique** | biocapteurs, perception distribuée |
| **38 — Intelligence distribuée** | MEMS, perception distribuée, fibre-capteur, hyperspectral, imagerie computationnelle, SAR, caméras événementielles |
| **39 — Autonomie mobile** | optronique, bandes IR, détecteurs, lidar, radar, inertiel, GNSS, navigation sans GNSS, capteurs quantiques, acoustique |
| **41 — Biologie programmable** | biocapteurs |

**Le dossier 39 mobilise dix entrées de cette seule couche.** C'est cohérent avec le squelette : l'autonomie mobile est la convergence la plus dépendante de la perception — et pourtant son maillon en retard est ailleurs, dans la démonstration de sûreté. **C'est le premier test interne de la thèse du volume.**

---

---

---

### Couche B — Calculer

---


## Chapitre 8 — Le calcul spécialisé

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte dominante : déplacer une donnée coûte plusieurs centaines de fois plus que la traiter, et cet écart s'est creusé. Ce chapitre traite des réponses apportées **à l'intérieur du paradigme électronique existant** — spécialisation, assemblage, hiérarchie mémoire, réduction de précision.
>
> Le chapitre 9 traitera des réponses qui sortent de ce paradigme, et le chapitre 10 d'une rupture d'une autre nature.
>
> **Six entrées.** Deux définissent l'économie du domaine, deux attaquent directement le mur de la mémoire, deux sont des leviers.

---

### ◆◆◆ Accélérateurs de calcul spécialisés

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

### ◆◆◆ Chiplets et assemblage avancé

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

### ◆◆ Mémoires à forte bande passante

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

### ◆◆◆ Calcul en mémoire

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

### ◆◆ Calcul à faible précision

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

### ◆ FPGA

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
