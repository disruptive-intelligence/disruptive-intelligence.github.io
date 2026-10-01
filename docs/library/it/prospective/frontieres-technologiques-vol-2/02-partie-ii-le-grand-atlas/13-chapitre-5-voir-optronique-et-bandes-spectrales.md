---
title: 'Chapitre 5 — Voir : optronique et bandes spectrales'
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte générale — aucune mesure sans bruit, sans résolution finie, sans conditions d'observation. Ce chapitre traite de ce qui se voit par **rayonnement électromagnétique dans les bandes optiques**, c'est-à-dire de la manière dont on obtient une image sans contact.
>
> **Six entrées.** Deux définissent le domaine, trois traitent des manières de le pousser, une est là pour éviter une confusion très répandue.

---

## ◆◆◆ Optronique — *electro-optics, EO/IR*

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

## ◆◆◆ Les bandes infrarouges — *NIR, SWIR, MWIR, LWIR*

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

## ◆◆ Détecteurs refroidis et non refroidis

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

## ◆◆ Imagerie hyperspectrale

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

## ◆◆ Imagerie computationnelle

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

## ◆ Intensification d'image

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Amplifier la lumière résiduelle d'une scène nocturne pour la rendre visible.

**Où vous rencontrerez le terme.** Vision nocturne · sécurité · applications de défense · astronomie amateur.

**Ce qui bloque.** **Il faut qu'il reste de la lumière.** Un intensificateur ne crée rien : il amplifie des photons existants. Dans l'obscurité totale, il ne voit rien — contrairement à un imageur thermique.

**À ne pas confondre avec.** **L'imagerie thermique.** C'est la confusion la plus fréquente du chapitre : les deux sont appelés « vision nocturne » et reposent sur des principes opposés. L'un amplifie la lumière réfléchie, l'autre capte l'émission propre des objets. L'un est aveuglé par une source vive, l'autre non ; l'un ne voit rien sans lumière, l'autre voit un corps chaud dans le noir absolu.

> ⏱ **État au 23/08/2026** — 🏭 déployé, technologie mature. Progressivement concurrencée par les capteurs à très faible bruit en bandes visible et proche infrarouge.
> 🔄 **À revoir si** des capteurs numériques à faible bruit atteignent des performances équivalentes à un coût et une consommation comparables.

**Renvois** — Couche : percevoir.

---
