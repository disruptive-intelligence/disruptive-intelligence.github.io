---
title: Chapitre 37 — La découverte scientifique accélérée
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 12
chapters: 14
---

### ① La capacité recherchée

**Formulation courante, et son défaut.** « L'IA accélère la science » n'est pas analysable : elle ne dit ni quelle étape, ni de combien, ni à quelle condition.

**Formulation retenue.**

> **Réduire le temps et le coût du cycle hypothèse → expérience → observation → hypothèse, dans des domaines où ce cycle est le facteur limitant de la connaissance.**

**Ce que cette formulation impose.** Elle oblige à identifier **quelle étape du cycle est le goulet** dans le domaine considéré — et la réponse n'est pas la même partout. C'est ce déplacement qui est l'objet du dossier, et non l'accélération en général.

**Le récit associé.** *AI for Science*, dont la fiche du chapitre 32 signale ce qu'il masque : le rapport entre coût d'hypothèse et coût de vérification.

---

### ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Apprendre** | générer et hiérarchiser des hypothèses | modèles de fondation (11) · modèles de raisonnement (11) · agents IA (12) · données synthétiques (11) · conception de protéines (20) |
| **Fabriquer** | exécuter et mesurer sans intervention | laboratoires autonomes (20) · bioproduction (20) · métrologie avancée (18) · fabrication additive (18) |
| **Percevoir** | instrumenter, mesurer en continu | biocapteurs (7) · perception distribuée (7) |
| **Vérifier** | statut de ce qui est établi | reproductibilité et réplication (20) |

**Douze entrées mobilisées**, réparties sur quatre couches — dont une, la reproductibilité, ajoutée à l'atlas parce que ce dossier l'exigeait et que le registre initial ne la contenait pas.

---

### ③ Ce qui empêche encore

**Le raisonnement du dossier tient en une comparaison de coûts**, et il faut la poser avant les verrous.

Un cycle de découverte comporte quatre étapes : **concevoir** une hypothèse, **exécuter** l'expérience, **mesurer** le résultat, **interpréter**. L'accélération de l'une ne réduit le cycle que si elle porte sur celle qui domine.

**Ce qui a été accéléré.** La conception. Générer des hypothèses — candidats moléculaires, séquences, paramètres de procédé — est devenu rapide et peu coûteux.

**Ce qui ne l'a pas été.** L'exécution et la mesure, dans les domaines où elles impliquent de la matière, du temps biologique ou des instruments lourds. Et l'interprétation, qui dépend de personnes.

**Le verrou est donc un rapport, non une étape.** Quand générer devient quasi gratuit et que vérifier reste cher, **le système produit plus d'hypothèses qu'il ne peut en tester**. Le goulet ne se desserre pas : il se déplace et s'aggrave.

**Les verrous concrets, hiérarchisés.**

**Premier — la validation expérimentale.** Coût, durée, disponibilité d'instruments, et pour les domaines biologiques, temps de croissance et variabilité.

**Deuxième — la reproductibilité.** Un résultat non reproductible n'est pas une connaissance. Les taux de réplication varient fortement selon les disciplines, et une accélération de la production sans amélioration de la reproductibilité produit du volume.

**Troisième — la représentativité des données.** Les modèles prédictifs sont entraînés sur ce qui a été publié et mesuré, c'est-à-dire sur **les cas faciles à mesurer**. Ils prédisent donc mieux là où l'on savait déjà, et moins bien là où l'on ne savait pas.

**Quatrième — l'interprétation.** Un résultat n'est une connaissance que lorsqu'il est compris, contesté et intégré. Ces opérations dépendent de personnes et n'ont pas de mécanisme d'accélération connu.

---

### ④ Le maillon le plus en retard

**La validation expérimentale**, sans hésitation.

**L'argument.** Dans tous les domaines examinés dans l'atlas — conception de protéines, biologie synthétique, matériaux, découverte de médicaments —, la même structure apparaît : la génération de candidats est devenue rapide, et le taux de validation expérimentale des candidats proposés est soit faible, soit non publié de façon comparable.

**Le cas le plus net est celui du médicament.** L'attrition est concentrée aux étapes les plus coûteuses — les essais chez l'humain — précisément celles où la prédiction est la moins fiable. **Accélérer dix fois l'amont ne change presque rien au coût total** quand l'aval concentre l'essentiel de la dépense et du temps.

**Position par rapport à la thèse du volume.** La couche éponyme est *apprendre* ; le maillon en retard est dans *fabriquer*. **La thèse est vérifiée.**

**Une conséquence contre-intuitive, et c'est le résultat principal du dossier.**

> Dans ce régime, **la valeur marginale d'un meilleur modèle prédictif décroît, et celle d'un instrument de vérification plus rapide augmente.**

C'est l'inverse de la répartition actuelle de l'attention et des financements. **Ce n'est pas un jugement, c'est une conséquence arithmétique** : quand une étape devient dix fois moins chère et que l'autre ne bouge pas, le gain sur le cycle complet est borné par la seconde.

---

### ⑤ Quel mur domine

**Le rendement de production**, sous une forme inhabituelle : le taux d'expériences exploitables. Une plateforme qui exécute mille expériences dont cent sont analysables produit moins qu'une qui en exécute deux cents toutes exploitables — et le contrôle de ce taux est un problème de métrologie et de protocole.

**L'incertitude**, sous la forme de la reproductibilité. C'est le mur du bruit du volume 1, transposé du signal à la connaissance : **un résultat non reproductible est un signal sous le plancher de détection.**

**Un troisième mur apparaît, et il n'était pas anticipé.** Le **coût du déplacement** — non des données, mais de la matière. Une expérience physique suppose de déplacer, préparer, transférer des échantillons, et ces opérations résistent à l'automatisation pour la raison établie au chapitre 14 : ce sont des tâches de manipulation.

---

### ⑥ Ce qui est en train de changer

**La conception assistée est devenue un outil courant** dans plusieurs domaines — protéines, molécules, matériaux —, avec des accès largement ouverts.

**L'automatisation expérimentale se ferme en boucle.** Les laboratoires autonomes ne se contentent plus d'exécuter un protocole : le système choisit l'expérience suivante en fonction de ce qu'il a observé. **C'est le changement structurant**, et il porte exactement sur le maillon identifié.

**Les données produites en conditions identiques.** Un effet secondaire de l'automatisation, souvent plus précieux que la vitesse : des données comparables entre elles, ce que le travail manuel ne garantit pas.

**Ce qui n'a pas changé.** Le temps biologique. La durée des essais cliniques. Les taux de réplication. Et la disponibilité d'instruments lourds, qui reste concentrée.

---

### ⑦ Ce que la convergence débloquerait

**Un déplacement de la nature du travail scientifique.** Si le cycle se réduit d'un ordre de grandeur, la contrainte cesse d'être « combien d'expériences peut-on faire » pour devenir « quelles questions vaut-il la peine de poser ». **C'est un déplacement vers la formulation du problème.**

**Les domaines les plus concernés** sont ceux où l'espace de recherche est vaste, la validation rapide et le critère de succès mesurable : formulation de matériaux, optimisation de procédés, criblage. **Les moins concernés** sont ceux où la validation est intrinsèquement lente — clinique, écologie, sciences du climat.

**Ce qui resterait inchangé.** Les questions dont la difficulté n'est pas le nombre d'expériences mais la conceptualisation. Aucune accélération du cycle ne produit un cadre théorique.

---

### ⑧ Le verrou suivant

**La capacité d'absorption humaine.**

Si la validation s'automatise, le goulet devient le nombre de personnes capables d'interpréter, de contester et d'intégrer les résultats. **Le débit de publication, de relecture et de discussion n'a pas de mécanisme d'accélération connu**, et il est déjà décrit comme saturé.

**Une conséquence plus dérangeante.** Un système produisant des résultats plus vite qu'ils ne peuvent être vérifiés par des pairs déplace la confiance de la vérification vers la réputation de l'outil. **C'est un changement dans la manière d'établir un fait**, et il n'a pas de précédent évident.

**Et un verrou matériel.** L'automatisation expérimentale exige des installations coûteuses, ce qui concentre la capacité de découverte chez ceux qui peuvent les financer — déplacement de la structure de la recherche que le chapitre 44 traitera.

---

### ⑨ La chronologie conditionnelle

```text
① si l'automatisation expérimentale réduit d'un ordre de grandeur
   le coût et le délai d'un test dans un domaine donné
        → alors la conception de l'expérience devient le maillon limitant

② si la conception d'expérience s'automatise à son tour
        → alors l'interprétation et la validation par les pairs
          deviennent limitantes

③ si la reproductibilité ne s'améliore pas en parallèle
        → l'accélération produit du volume et non de la connaissance,
          et la confiance se déplace vers la réputation des outils

④ si la validation reste lente dans un domaine
        → l'accélération de la conception y produit un gain marginal,
          quelle que soit la qualité des modèles
```

**L'étape ③ est le cœur du dossier**, et elle doit être lue comme une conséquence de coûts et non comme un procès. L'étape ④ décrit ce qui se produit dans les domaines à validation lente — c'est-à-dire la majorité de ceux où l'enjeu est le plus élevé.

---

### ⑩ Signaux et réfutation

**Signaux de progression.**

**Le coût et la durée d'un cycle expérimental complet** dans un domaine donné, publiés et comparables dans le temps. **C'est le signal le plus direct et il est rarement disponible.**

**Le taux de validation expérimentale des prédictions publiées**, par classe de problème. Sa publication standardisée serait en soi un progrès méthodologique.

**L'apparition d'installations d'automatisation partagées**, accessibles au-delà de leurs propriétaires — ce qui indiquerait que la contrainte de capital se desserre.

**Un taux de réplication mesuré en progression** dans une discipline majeure, sur plusieurs années.

**Signaux non informatifs.** Le nombre de candidats générés. Le nombre de publications produites avec assistance. Les performances sur des jeux de test rétrospectifs, qui mesurent la capacité à retrouver ce qu'on sait déjà.

**Ce qui réfuterait l'analyse.**

**Le taux de validation progresse** nettement, ce qui indiquerait que la prédiction s'améliore réellement et non seulement sa quantité.

**Le coût de l'expérience baisse** d'un ordre de grandeur dans un domaine à validation historiquement lente — ce qui invaliderait l'étape ④.

**Ou bien un résultat de fond obtenu par cette voie** dans un domaine où la conceptualisation était le goulet, ce qui contredirait l'affirmation qu'aucune accélération du cycle ne produit un cadre théorique. **C'est la réfutation la plus intéressante, et elle est observable.**

---


## Bilan intermédiaire des deux premiers dossiers

### Sur la thèse du volume

| Dossier | Couche éponyme | Maillon en retard | Thèse |
|---|---|---|---|
| 36 — Robotique généraliste | agir | fiabilité de la manipulation (agir), conditionnée par les données (apprendre) | **partiellement contredite** |
| 37 — Découverte scientifique | apprendre | validation expérimentale (fabriquer) | **vérifiée** |

### Deux observations communes aux deux dossiers

**Un. Dans les deux cas, le verrou est un rapport et non une étape.** Pour la robotique, le rapport entre taux de succès et coût de traitement des échecs. Pour la découverte, le rapport entre coût de génération et coût de validation. **Ce n'est pas la performance d'un composant qui bloque, c'est un déséquilibre entre deux étapes.**

C'est une observation que ni l'atlas ni la taxonomie ne pouvaient produire, et qui justifie l'existence de cette partie.

**Deux. Dans les deux cas, le signal le plus décisif est le moins disponible.** Données d'exploitation publiées par un tiers pour la robotique ; coût et durée d'un cycle expérimental pour la découverte. **Les grandeurs qui trancheraient l'analyse ne sont pas publiées**, et c'est en soi une information sur la maturité des deux domaines.

---

---


## Chapitre 38 — L'intelligence distribuée

### ① La capacité recherchée

**Formulation courante, et son défaut.** « Mettre de l'intelligence partout » ne dit ni quelle intelligence, ni ce que « partout » coûte à exploiter.

**Formulation retenue.**

> **Percevoir, décider et agir localement, en très grand nombre, sans dépendre d'une infrastructure distante pour chaque décision — et pendant une durée compatible avec le coût d'installation.**

**Ce que cette formulation ajoute.** La dernière clause. Un dispositif installé pour cinq ans et qu'il faut visiter deux fois par an ne remplit pas la promesse, quelle que soit sa capacité de traitement. **La durée sans intervention est la variable qui décide, et elle est absente de tous les récits du domaine.**

**Le récit associé.** *Edge AI*, *IoT*, *ambient computing*. Les fiches des chapitres 32 et 34 les situent ; ce dossier analyse ce qu'ils supposent.

---

### ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Percevoir** | coût unitaire, étalonnage à grande échelle | MEMS avancés (7) · perception distribuée (7) · fibre-capteur (7) · caméras événementielles (6) |
| **Calculer** | traitement dans une enveloppe énergétique minuscule | accélérateurs (8) · calcul faible précision (8) · compute-in-memory (8) · neuromorphique (9) |
| **Apprendre** | ce qui tient dans la mémoire disponible | modèles compacts (11) · multimodalité (11) |
| **Relier** | placement du calcul, couverture, coût par message | edge/on-device/embarqué (25) · continuum (25) · réseaux non terrestres (24) |
| **Alimenter** | budget énergétique unitaire | récupération d'énergie (23) |
| **Vérifier** | confiance dans une donnée produite hors surveillance | identité machine (29) · attestation (28) · racine de confiance (28) |

**Seize entrées, six couches** — c'est la convergence la plus transversale des six.

---

### ③ Ce qui empêche encore

**Premier — l'exploitation d'un parc dispersé.** Le volume 1 l'a démontré par le calcul : un parc d'un million d'unités avec une intervention annuelle par unité représente plusieurs centaines de techniciens à temps plein. **Ni le capteur, ni le modèle, ni la liaison ne limitent — c'est l'exploitation.**

**Deuxième — la dérive silencieuse.** Un capteur qui dérive continue de produire des valeurs plausibles. À l'unité, on l'étalonne. À un million, **on ne sait pas lequel a dérivé**, et la qualité de la donnée agrégée se dégrade sans signal.

**Troisième — la mise à jour.** Un modèle déployé sur un parc se corrige au rythme du parc, avec des versions hétérogènes en service simultanément. Un dispositif alimenté par récupération d'énergie peut n'avoir aucune fenêtre de communication suffisante pour recevoir une mise à jour.

**Quatrième — la confiance dans la donnée.** Un dispositif physiquement accessible, non surveillé, peut être remplacé, déplacé ou manipulé. **Et une signature n'atteste pas la véracité** : un capteur compromis produit une donnée authentique et fausse.

---

### ④ Le maillon le plus en retard

**L'exploitation du parc — étalonnage, maintenance, mise à jour.**

**L'argument.** Les trois autres verrous se traitent par la conception : on peut concevoir un dispositif frugal, un modèle compact, une liaison économe. **L'exploitation, elle, croît linéairement avec le nombre d'unités** et ne bénéficie d'aucune économie d'échelle — c'est même l'inverse, puisque la dispersion géographique augmente le coût de chaque intervention.

**Le calcul qui le montre.** Si le coût d'exploitation annuel par unité ne descend pas sous une fraction du coût d'acquisition, un déploiement massif est économiquement impossible quelle que soit la baisse du prix du capteur. **La grandeur qui décide n'est pas le prix du dispositif mais le coût annuel de sa possession** — et elle est presque jamais publiée.

**Position par rapport à la thèse du volume.** Les couches éponymes sont *calculer* et *relier* ; le maillon en retard est **institutionnel et opérationnel**, hors de toute couche technique. **La thèse est vérifiée.**

---

### ⑤ Quel mur domine

**La défaillance silencieuse**, très nettement, et sous sa forme la plus difficile : **à grande échelle, on ne sait pas quelles unités ont dérivé**. Le mur n'est pas qu'un capteur dérive — c'est qu'on ne peut pas le savoir.

**Le rendement de production**, au sens de la proportion d'unités effectivement fonctionnelles à un instant donné. Un parc à 85 % de disponibilité produit une donnée dont la représentativité spatiale est inconnue.

---

### ⑥ Ce qui est en train de changer

**L'exécution locale de modèles est devenue possible sur des appareils ordinaires**, ce qui supprime le coût par appel et la dépendance à une liaison.

**Les architectures événementielles** — capteurs et traitement ne consommant que lorsqu'il se passe quelque chose — abaissent le budget énergétique d'un ordre de grandeur sur des données éparses.

**L'attestation au niveau du dispositif** se généralise, ce qui rend traitable la question de l'origine de la donnée.

**La couverture** s'étend par les réseaux non terrestres, ce qui ouvre les zones sans infrastructure.

**Ce qui n'a pas changé.** Le coût d'une intervention humaine sur site. Le vieillissement des capteurs. Et le fait qu'une dérive ne se signale pas.

---

### ⑦ Ce que la convergence débloquerait

**Une mesure continue là où l'on mesurait ponctuellement.** Infrastructures, agriculture, environnement, industrie, santé : le passage d'un relevé périodique à une observation permanente change la nature de ce qu'on peut détecter — les dérives lentes, les événements brefs, les corrélations spatiales.

**Une décision locale sans aller-retour.** Ce qui compte moins pour la latence que pour l'autonomie : un système qui décide seul continue de fonctionner quand la liaison tombe.

**Ce qui resterait hors de portée.** Les usages exigeant une donnée opposable — mesure réglementaire, preuve — tant que l'authenticité à la source n'est pas démontrable.

---

### ⑧ Le verrou suivant

**La confiance dans la mesure.**

Si l'exploitation s'automatise — auto-diagnostic, étalonnage croisé entre unités voisines, détection de dérive par comparaison —, le goulet devient : **que vaut une mesure produite par un dispositif non surveillé, physiquement accessible, dont la signature atteste l'origine mais jamais la véracité ?**

C'est la question du chapitre 29, et elle conditionne tous les usages où la donnée doit être opposable.

**Et un verrou de second ordre.** Un parc massif de capteurs devient une infrastructure dont d'autres systèmes dépendent sans l'avoir choisie — **exactement le mécanisme du chapitre 45**.

---

### ⑨ La chronologie conditionnelle

```text
① si le coût unitaire et le budget énergétique permettent un déploiement massif
        → alors l'exploitation du parc devient limitante

② si l'exploitation s'automatise — auto-diagnostic, étalonnage croisé,
   mise à jour sans intervention
        → alors la confiance dans la mesure devient limitante

③ si l'authenticité de la mesure à la source reste indémontrable
        → les usages restent confinés à ceux qui tolèrent
          une donnée non opposable

④ si l'exploitation ne s'automatise pas
        → les déploiements plafonnent à l'échelle où
          la maintenance manuelle reste supportable
```

---

### ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** Le **coût complet d'exploitation par unité et par an**, publié par un exploitant — c'est le signal décisif. L'apparition de mécanismes d'**étalonnage croisé automatique** entre unités voisines. La normalisation d'une **attestation au niveau capteur**. Et la **durée moyenne sans intervention** observée sur un parc réel.

**Signaux non informatifs.** Le nombre d'unités déployées. Le prix unitaire du capteur. La consommation annoncée en veille. Les annonces de partenariat.

**Ce qui réfuterait l'analyse.** Les déploiements dépassent durablement le million d'unités avec un coût d'exploitation par unité en baisse — ce qui indiquerait que l'exploitation n'était pas le verrou. Ou bien les projets sont abandonnés au premier renouvellement de parc, ce qui confirmerait l'analyse par l'échec plutôt que par le blocage.

---


## Chapitre 39 — L'autonomie mobile

### ① La capacité recherchée

**Formulation retenue.**

> **Confier un déplacement à un système, dans un environnement partagé avec des humains non prévenus, sans supervision continue — et pouvoir le démontrer à un tiers.**

**La dernière clause est le dossier entier.** La capacité technique existe et fonctionne en exploitation commerciale dans un domaine restreint. **Ce qui borne l'extension n'est pas de faire, c'est de démontrer.**

---

### ② Les briques nécessaires

| Couche | Entrées d'atlas |
|---|---|
| **Percevoir** | lidar (6) · radar imageur (6) · bandes infrarouges (5) · optronique (5) · détecteurs (5) · fusion (7) · capteurs inertiels (6) · GNSS (6) · navigation sans GNSS (6) · capteurs quantiques (7) |
| **Apprendre** | modèles du monde (13) · sim-to-real (13) · automatisation-agentivité-autonomie (12) |
| **Agir** | véhicules autonomes (17) · domaine de conception opérationnelle (17) · localisation et cartographie (17) · autres modes (17) · autonomie supervisée (16) |
| **Relier** | edge/on-device (25) · réseaux non terrestres (24) · communications dégradées (24) |
| **Vérifier** | architecture de sûreté (30) · détection de sortie de domaine (30) · vérification formelle (30) · dossiers de sûreté (30) · dégradation maîtrisée (30) |

**Vingt-six entrées** — la dépendance la plus large de l'atlas, et de loin.

---

### ③ Ce qui empêche encore

**Premier — la démonstration de sûreté opposable.** On ne peut pas énumérer les situations d'un système ouvert sur le monde. La vérification exhaustive étant impossible, il faut lui substituer une argumentation acceptée par une autorité — et cette argumentation n'a pas de référentiel établi pour les systèmes apprenants.

**Deuxième — l'assurabilité.** Un assureur a besoin d'un historique de sinistres, d'une population comparable, de modes de défaillance caractérisés, d'une estimation du sinistre maximal et d'un cadre juridique stable. **Une technologie nouvelle ne fournit aucun des cinq.** Le volume 1 l'a établi : l'assurabilité est un meilleur indicateur avancé de déploiement que n'importe quelle annonce technique.

**Troisième — le ratio de supervision.** Un système supervisé à un opérateur pour un véhicule ne réduit pas le coût du travail : il le déplace. **C'est le paramètre qui décide de l'économie**, et il est presque jamais publié.

**Quatrième — l'extension du domaine d'emploi.** Chaque nouvelle ville, chaque nouveau type de voie, chaque nouvelle condition météorologique exige une validation. **L'extension se fait par négociation locale, non par effet d'échelle.**

---

### ④ Le maillon le plus en retard

**La démonstration de sûreté opposable, et son corollaire l'assurabilité.**

**L'argument.** La capacité technique est démontrée : des services commerciaux sans conducteur fonctionnent. Ce qui n'existe pas est un **référentiel permettant de démontrer, une fois, qu'un système est acceptablement sûr dans une classe de conditions** — et de transposer cette démonstration ailleurs.

**Ce qui le prouve.** L'extension se fait ville par ville. Si le verrou était la perception ou la décision, une amélioration du système permettrait une extension générale. **Le fait que l'extension soit géographique et négociée indique que le verrou est institutionnel.**

**Position par rapport à la thèse du volume.** Les couches éponymes sont *agir* et *percevoir*, qui fournissent dix-huit des vingt-six entrées. Le maillon en retard est dans *vérifier*. **La thèse est vérifiée, et c'est le cas le plus net des six.**

---

### ⑤ Quel mur domine

**La défaillance silencieuse**, sous la forme de la sortie de domaine non détectée : un système qui ne sait pas qu'il est hors de ses conditions de validation continue d'agir avec la même assurance apparente.

**L'incertitude**, au sens de l'impossibilité de vérification exhaustive — ce qui n'est pas un défaut du système mais une propriété du problème.

---

### ⑥ Ce qui est en train de changer

**L'exploitation commerciale sans conducteur existe** dans un nombre limité de villes, avec un domaine d'emploi qui s'étend progressivement. C'est un fait, et il déplace la question.

**Les architectures de sûreté** — enveloppe vérifiable entourant un système apprenant — entrent progressivement dans les référentiels sectoriels.

**La notion de domaine de conception opérationnelle** se normalise, ce qui rend les revendications comparables.

**Ce qui n'a pas changé.** Le renouvellement du parc, qui borne toute transformation à l'échelle du parc quel que soit le succès sur le flux — le volume 1 l'a chiffré. Et l'absence de référentiel transposable entre juridictions.

---

### ⑦ Ce que la convergence débloquerait

**Un transport dont le coût marginal ne comprend pas de conducteur** — ce qui change l'économie de la mobilité, de la logistique et de la desserte des zones peu denses.

**Mais borné par le parc.** Même une adoption totale sur les véhicules neufs mettrait plus d'une décennie à transformer le parc en circulation. **Le service de flotte n'a pas cette contrainte** — c'est pourquoi il précède et précédera le véhicule particulier.

---

### ⑧ Le verrou suivant

**Le renouvellement du parc et l'infrastructure de supervision.**

Si la sûreté se démontre et que l'assurabilité suit, la transformation reste bornée par deux choses : la durée de vie des véhicules en circulation — facteur cinq à dix entre part du flux et part du stock — et le **nombre d'opérateurs de supervision**, qui doit descendre sous un seuil pour que l'économie tienne.

---

### ⑨ La chronologie conditionnelle

```text
① si un référentiel de démonstration de sûreté applicable aux systèmes
   apprenants devient opposable dans une juridiction majeure
        → alors l'assurabilité devient traitable
          et le domaine d'emploi peut s'étendre par cadre et non par négociation

② si le ratio d'opérateurs de supervision descend sous un seuil économique
        → alors le renouvellement du parc devient limitant
          pour la transformation à l'échelle

③ si le référentiel n'apparaît pas
        → l'extension reste ville par ville, sans effet d'échelle,
          et l'économie reste celle d'un service local

④ si un accident majeur survient avant l'établissement du référentiel
        → durcissement des exigences, refermeture du domaine d'emploi,
          et report de plusieurs années
```

**L'étape ③ décrit l'état actuel** et doit être lue comme une trajectoire possible, non comme un échec. **L'étape ④ n'est pas une prédiction** : c'est un mécanisme établi au volume 1, et il doit figurer parce qu'il est le plus probable des facteurs de rupture.

---

### ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** La publication d'un **référentiel de certification** pour système apprenant. L'apparition d'une **offre d'assurance standardisée**. Le **ratio opérateurs par véhicule**, publié. L'extension à un **type de voie ou de condition** non couvert jusque-là.

**Signaux non informatifs.** Le nombre de kilomètres parcourus, sans le domaine d'emploi correspondant. Le nombre de villes, sans les conditions. Les levées de fonds. Les comparaisons d'accidentologie sans population de référence comparable.

**Ce qui réfuterait l'analyse.** Le nombre de domaines d'emploi cesse de croître, ce qui indiquerait un verrou technique et non institutionnel. Le ratio de supervision ne baisse pas malgré l'expérience. Ou bien un référentiel apparaît et l'extension ne suit pas — ce qui invaliderait l'identification du maillon.

---


## Chapitre 40 — Énergie et calcul

### ① La capacité recherchée

**Ce dossier ne vise pas une capacité mais une question.**

> **Qu'est-ce qui borne réellement la croissance de la capacité de calcul — et le calcul devient-il contraint par l'énergie avant de l'être par les transistors ?**

**Pourquoi ce dossier existe.** Parce que c'est la seule convergence de la partie où **les deux couches en amont de tout l'atlas se rencontrent**, et parce que la réponse détermine des décisions d'implantation, d'investissement et de politique publique.

---

### ② Les briques nécessaires

| Couche | Entrées d'atlas |
|---|---|
| **Calculer** | accélérateurs (8) · chiplets et assemblage (8) · mémoires à forte bande passante (8) · compute-in-memory (8) · calcul faible précision (8) · photonique intégrée (9) · calcul photonique (9) |
| **Alimenter** | réseaux électriques pilotés (23) · raccordement et files d'attente (23) · électronique de puissance (23) · petits réacteurs modulaires (22) |
| **Relier** | edge/on-device/embarqué (25) · continuum cloud-edge (25) |
| **Fabriquer** | semi-conducteurs à grand gap (19) · matériaux critiques (19) |

**Quinze entrées**, et la chaîne qu'elles forment est le sujet du dossier.

---

### ③ Ce qui empêche encore — la chaîne de goulets

**Ce dossier est le seul dont le verrou se lit comme une chaîne**, et le volume 1 en avait établi le mécanisme sans pouvoir l'observer sur un cas ouvert.

```text
   ① capacité de calcul par puce
        ↓  largement améliorée par la spécialisation et l'assemblage
   ② accès mémoire et bande passante
        ↓  attaqué par l'empilement, le calcul en mémoire, la faible précision
   ③ énergie consommée et densité de puissance
        ↓  attaqué par la spécialisation et les semi-conducteurs à grand gap
   ④ évacuation de la chaleur
        ↓  attaqué par le refroidissement liquide
   ⑤ raccordement électrique du site
        ↓  procédures, files d'attente, délais en années
   ⑥ fabrication d'équipements de réseau
        ↓  transformateurs, postes, lignes — carnets en années
```

**Chaque étage a été le goulet dominant, a été partiellement traité, et a révélé le suivant.** C'est le principe P8 du volume 1, observé sur une chaîne complète et documentée.

---

### ④ Le maillon le plus en retard

**Le raccordement électrique et les délais d'équipement de réseau.**

**L'argument, et il est arithmétique.** Construire un bâtiment de calcul se compte en mois ; obtenir la puissance se compte en années — sept à dix dans plusieurs marchés développés, jusqu'à une décennie dans certains pôles. **Le rapport des durées est de un à quatre.**

**Et une file d'attente n'est pas une capacité.** Sur l'ensemble des demandes de raccordement déposées aux États-Unis entre 2000 et 2019, une petite minorité avait atteint l'exploitation commerciale, l'essentiel ayant été retiré. **Confondre un carnet de projets annoncés avec une capacité future est une erreur d'échelon de preuve.**

**Ce que le dossier doit démontrer.** Une amélioration de l'efficacité par opération **ne change pas le calendrier d'un projet dont le raccordement est attendu pour dans plusieurs années**. C'est la démonstration la plus nette de tout le volume que le verrou n'est pas dans la couche où l'attention se porte.

**Position par rapport à la thèse.** Les couches éponymes sont *calculer* et *alimenter* ; le maillon en retard est **industriel et institutionnel** — procédure administrative et carnet de commandes de transformateurs. **La thèse est vérifiée.**

---

### ⑤ Quel mur domine

**La dissipation.** Un centre de calcul transforme la quasi-totalité de son électricité en chaleur — le résultat d'un calcul ne pèse rien et n'emporte aucune énergie. **La densité de puissance évacuable borne ce qu'on peut faire fonctionner**, à l'échelle de la puce comme à celle du bâtiment.

**Le coût du déplacement**, au sens de la bande passante mémoire à l'inférence : c'est l'étage ② de la chaîne, et il reste actif.

---

### ⑥ Ce qui est en train de changer

**L'assemblage avancé** est devenu le principal levier de performance, davantage que la réduction des dimensions.

**Le refroidissement liquide** se généralise, imposé par la densité de puissance par baie — ce n'est pas un raffinement mais un changement de nature de l'installation.

**Les contrats d'approvisionnement électrique dédiés** apparaissent, y compris avec des moyens de production construits pour l'usage.

**Ce qui n'a pas changé.** Les délais de raccordement. Les carnets de commandes des fabricants de transformateurs. Et l'énergie d'un accès à une mémoire externe.

---

### ⑦ Ce que la convergence débloquerait

**Rien de spectaculaire, et c'est le point.** Si le raccordement se desserrait, la capacité de calcul croîtrait au rythme de la production de composants — c'est-à-dire au rythme qu'elle aurait dû suivre.

**La conséquence intéressante est ailleurs, et elle est géographique.** Si le raccordement reste le verrou, **la localisation du calcul suit la disponibilité électrique et non la demande**. Les installations se déplacent vers les zones où la puissance est disponible et raccordable, indépendamment de la proximité des utilisateurs — sauf pour les charges sensibles à la latence, qui restent contraintes.

**C'est une prédiction de déplacement, pas de ralentissement**, et c'est ce que ce dossier apporte au-delà du volume 1.

---

### ⑧ Le verrou suivant

**La production d'équipements de réseau et la disponibilité de matériaux.**

Si les procédures s'accélèrent, le goulet devient industriel : transformateurs, postes, câbles, et les matériaux qu'ils consomment — cuivre notamment, dont l'offre minière ne répond pas avant quinze ans.

**Et un verrou de troisième ordre.** Si la capacité de réseau croît, le goulet devient la **production d'électricité pilotable disponible localement**, ce qui renvoie au chapitre 22.

---

### ⑨ La chronologie conditionnelle

```text
① si les procédures de raccordement se raccourcissent significativement
        → alors la fabrication d'équipements de réseau devient limitante

② si cette capacité industrielle croît
        → alors la production d'électricité pilotable disponible localement
          devient limitante

③ si aucun des trois ne se débloque
        → la localisation du calcul suit la disponibilité électrique,
          et non la demande

④ si l'efficacité énergétique par unité de travail utile progresse
   plus vite que la demande
        → la contrainte se desserre sans que rien ne soit débloqué
```

**L'étape ④ est la seule qui échappe à la chaîne**, et elle dépend d'un effet rebond : si le coût de l'unité de travail baisse et que la demande n'est pas saturée, l'usage augmente et absorbe le gain. **La question est celle de la saturation, et elle n'est pas tranchée.**

---

### ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** Les **délais de raccordement publiés par zone**, et leur évolution. Les **carnets de commandes des fabricants de transformateurs**. L'**efficacité énergétique par unité de travail utile** — non par opération, qui ne dit rien du système. Et les **contrats d'approvisionnement dédiés**, qui indiquent que les acteurs contournent le réseau plutôt que de l'attendre.

**Signaux non informatifs.** La puissance de calcul par puce. Les annonces de capacité en construction, qui sont des files d'attente. Les records d'efficacité sur des charges de référence.

**Ce qui réfuterait l'analyse.** Les délais de raccordement baissent nettement dans un marché majeur. La demande de calcul sature. Ou bien l'efficacité progresse assez vite pour que la demande électrique se stabilise — ce qui invaliderait la chaîne entière.

---


## Bilan des cinq premiers dossiers

| Dossier | Couche éponyme | Maillon en retard | Thèse |
|---|---|---|---|
| 36 — Robotique généraliste | agir | fiabilité de la manipulation (agir) | **partiellement contredite** |
| 37 — Découverte scientifique | apprendre | validation expérimentale (fabriquer) | vérifiée |
| 38 — Intelligence distribuée | calculer, relier | exploitation du parc (opérationnel) | vérifiée |
| 39 — Autonomie mobile | agir, percevoir | démonstration de sûreté (vérifier) | vérifiée |
| 40 — Énergie et calcul | calculer, alimenter | raccordement (industriel, institutionnel) | vérifiée |

**Quatre vérifications, une contradiction partielle.**

### Une observation que les cinq dossiers partagent

**Dans les cinq cas, le verrou est un rapport et non une étape.**

Robotique : entre taux de succès et coût de traitement des échecs. Découverte : entre coût de génération et coût de validation. Distribution : entre coût d'acquisition et coût annuel d'exploitation. Autonomie mobile : entre capacité démontrée et capacité démontrable. Énergie et calcul : entre délai de construction et délai de raccordement.

**Ce n'est jamais la performance d'un composant qui bloque, c'est un déséquilibre entre deux grandeurs.** C'est l'observation la plus solide de cette partie, et elle n'était produite ni par l'atlas ni par la taxonomie — chacun de ces documents traite des objets, jamais des rapports entre eux.

### Une seconde observation, sur les signaux

**Dans les cinq cas, le signal qui trancherait n'est pas publié.** Données d'exploitation d'une flotte robotique. Coût et durée d'un cycle expérimental. Coût annuel d'exploitation par capteur. Ratio d'opérateurs par véhicule. Délais de raccordement par zone.

**Ce sont des grandeurs d'exploitation, et elles sont systématiquement absentes du discours public**, qui porte sur les capacités. C'est en soi une information sur la maturité de ces domaines : **on communique sur ce qui progresse, pas sur ce qui borne.**

---

---


## Chapitre 41 — La biologie programmable

> **Périmètre de traitement.** Ce dossier traite mécanismes, verrous industriels, économie et gouvernance. Il ne décrit **aucun protocole, aucune méthode expérimentale, aucun paramètre de mise en œuvre** — y compris lorsque cette information est publiquement accessible. Cette règle s'applique phrase par phrase et sans exception.

---

### ① La capacité recherchée

**Formulation courante, et son défaut.** « Programmer le vivant » emprunte au logiciel une métaphore qui ne tient pas : il n'y a ni compilateur, ni exécution déterministe, ni possibilité d'arrêter le système pour l'inspecter sans le modifier.

**Formulation retenue.**

> **Concevoir une fonction biologique plutôt que la découvrir, puis la produire de manière reproductible et à une échelle qui la rend économiquement utile.**

**Les trois clauses sont indissociables**, et c'est le sujet du dossier. Concevoir sans produire donne des candidats qu'on ne sait pas fabriquer. Produire sans reproductibilité donne des lots dont aucun ne certifie le suivant. **La capacité n'existe que lorsque les trois tiennent ensemble.**

**Le récit associé.** *Biologie synthétique*, *BioTech*, et une part de *AI for Science*. Les fiches des chapitres 32 et 35 les situent.

---

### ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Apprendre** | prédire une fonction à partir d'une séquence | conception de protéines (20) · modèles de fondation (11) · découverte de médicaments assistée (20) |
| **Fabriquer** | écrire, assembler, produire, purifier | édition génomique (20) · biologie synthétique (20) · bioproduction (20) · laboratoires autonomes (20) · thérapies géniques et cellulaires (20) · organoïdes (20) |
| **Percevoir** | mesurer le vivant en continu | biocapteurs (7) |
| **Vérifier** | statut de ce qui est établi, et cadre | reproductibilité (20) · biosécurité (20) |

**Douze entrées, dont neuf dans un seul chapitre d'atlas** — c'est la dépendance la plus concentrée des six dossiers, et cette concentration est en elle-même un résultat.

---

### ③ Ce qui empêche encore

**Premier — la montée en échelle de la production.** Le rapport entre surface et volume change avec la taille : dans une grande cuve, l'oxygénation, le mélange et l'évacuation de la chaleur deviennent des problèmes qui n'existaient pas en fiole. **Un procédé qui fonctionne au laboratoire ne fonctionne pas mécaniquement en bioréacteur industriel** — et la purification, qui suit, domine souvent le coût.

**Deuxième — la relation entre séquence et fonction.** Prédire la forme d'une protéine à partir de sa séquence a connu des progrès considérables. **Prédire sa fonction n'a pas suivi**, parce que celle-ci dépend aussi de ses partenaires, de sa localisation, de sa concentration et de son environnement chimique. Les trois problèmes sont régulièrement présentés comme un seul succès.

**Troisième — la composabilité.** Le pari de l'ingénierie appliqué au vivant suppose qu'un élément caractérisé isolément se comporte de la même façon une fois assemblé. **Il ne le fait pas** : les composants partagent les ressources de la cellule, interagissent avec son métabolisme, et l'hôte tend à éliminer une modification coûteuse par sélection sur les générations.

**Quatrième — la variabilité et la reproductibilité.** Deux cultures conduites identiquement ne donnent pas exactement le même résultat. Cela impose un contrôle par lot bien plus lourd que pour une pièce mécanique, et cela rend la réplication d'un résultat plus difficile que dans les sciences physiques.

**Cinquième — le délai réglementaire**, dans le thérapeutique, où l'attrition est concentrée aux étapes les plus coûteuses.

---

### ④ Le maillon le plus en retard

**La capacité de bioproduction qualifiée.**

**L'argument.** Les quatre autres verrous se traitent, lentement mais réellement : la prédiction progresse, la composabilité s'améliore par la standardisation, la reproductibilité par les pratiques, le cadre par l'accumulation de précédents. **Le cinquième ne se traite pas par la recherche** : produire à l'échelle industrielle exige des installations, du capital lourd, des délais de construction en années, et **une qualification réglementaire par site et par produit**.

**Ce qui le prouve.** Si la conception s'accélère sans que cette capacité croisse, **on produit des candidats qu'on ne sait pas fabriquer**. C'est déjà observable dans le thérapeutique, où des produits autorisés rencontrent des contraintes de capacité de production.

**Un second candidat sérieux, et il faut le nommer.** Le **délai réglementaire** dans le thérapeutique. Il est plus long que la construction d'une usine, et il ne se raccourcit pas par l'investissement. **Je retiens la production comme maillon dominant** parce qu'elle borne l'ensemble du domaine — y compris les usages non thérapeutiques, qui échappent au cadre clinique — mais l'argument inverse est défendable pour le seul thérapeutique.

**Position par rapport à la thèse du volume.** La couche éponyme est *fabriquer* ; le maillon en retard y est aussi. **La thèse est partiellement contredite**, et c'était prévu au squelette : quand la couche éponyme est celle où se joue la fabrication, le verrou peut y rester.

---

### ⑤ Quel mur domine

**Le rendement de production**, au sens du rendement de lot — et il est ici plus sévère qu'ailleurs, puisque la variabilité biologique le rend intrinsèquement instable.

**L'incertitude**, sous la forme de la reproductibilité. **C'est le seul dossier des six où ce mur est structurel et non conjoncturel** : la variabilité du vivant ne se réduit pas par un meilleur procédé, elle se maîtrise par du contrôle.

---

### ⑥ Ce qui est en train de changer

**La conception assistée est devenue un outil courant**, accessible largement, ce qui a considérablement abaissé la barrière d'entrée sur la partie amont.

**L'automatisation expérimentale se ferme en boucle**, ce qui attaque le délai des cycles conception-construction-test — historiquement compté en semaines.

**Les modèles économiques du thérapeutique évoluent** sous la pression des produits administrés une fois, potentiellement curatifs, dont le financement ne s'insère pas dans les mécanismes conçus pour des traitements chroniques.

**Ce qui n'a pas changé.** Le temps biologique. La variabilité. Les délais d'essais cliniques. Le rapport entre surface et volume dans une cuve. Et la durée de construction d'une installation qualifiée.

---

### ⑦ Ce que la convergence débloquerait

**Dans le thérapeutique.** Des traitements pour des maladies aujourd'hui sans réponse, avec une trajectoire d'extension des maladies rares vers des indications plus fréquentes — ce qui suppose précisément un changement d'échelle de production.

**Hors du thérapeutique**, et c'est la partie la moins discutée. Production de molécules complexes pour la chimie, l'alimentation, les matériaux · substitution de procédés énergivores par des voies biologiques · capteurs biologiques déployés.

**Ce qui resterait hors de portée.** Les fonctions dont la prédiction dépend d'un organisme entier plutôt que d'une molécule isolée. Et tout ce qui suppose une modification héritable, qui relève de restrictions très larges et d'un débat qui n'est pas technique.

---

### ⑧ Le verrou suivant

**La disponibilité de capacité de production qualifiée devient elle-même une infrastructure rare** — capital lourd, délai long, qualification par site et par produit.

Si cette capacité croît, le goulet suivant est **la validation clinique** pour le thérapeutique, et **l'acceptabilité** pour les usages agricoles et alimentaires, où les cadres réglementaires divergent fortement entre juridictions et où le débat n'est pas technique.

**Et un verrou de troisième ordre.** La concentration de la capacité de production chez un petit nombre d'acteurs et de pays fait de la bioproduction un enjeu de dépendance au sens du chapitre 45 — mécanisme identique à celui des matériaux critiques.

---

### ⑨ La chronologie conditionnelle

```text
① si la prédiction de fonction atteint une fiabilité permettant
   de réduire significativement le criblage expérimental
        → alors la validation expérimentale devient limitante

② si les laboratoires autonomes réduisent le coût et le délai
   de cette validation
        → alors la montée en échelle de production devient limitante

③ si la capacité de bioproduction qualifiée ne croît pas
        → la conception accélérée produit des candidats
          qu'on ne sait pas fabriquer

④ si la capacité croît
        → alors la validation clinique et l'acceptabilité deviennent
          les limitants, selon les usages
```

**L'étape ③ décrit une situation déjà partiellement observable**, et c'est ce qui distingue ce dossier des cinq autres : sa chronologie n'est pas entièrement prospective.

---

### ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** Le **taux de validation expérimentale** des conceptions publiées, par classe de problème — sa publication standardisée serait en soi un progrès. Le **coût par gramme** de production biologique pour une classe de produits. Le **nombre de sites de production qualifiés** et leur capacité. Le **délai moyen d'autorisation** par catégorie de produit.

**Signaux non informatifs.** Le nombre de séquences conçues. Les performances sur des jeux de test rétrospectifs — qui mesurent la capacité à retrouver ce qu'on sait déjà. Les levées de fonds. Le nombre de publications.

**Ce qui réfuterait l'analyse.** Le coût de production biologique baisse significativement par l'expérience, ce qui indiquerait un apprentissage industriel là où le dossier n'en attend pas. Ou bien un procédé de purification générique réduit le coût de cette étape sur une classe large de produits — ce qui déplacerait le maillon. Ou encore : la capacité de production croît et le goulet ne se déplace pas vers la validation, ce qui invaliderait l'étape ④.

---


## CLÔTURE DE LA PARTIE IV

### Bilan de la thèse

L'atlas et la taxonomie avaient produit une thèse. Six dossiers l'ont testée.

| Dossier | Couche éponyme | Maillon en retard | Nature du verrou | Thèse |
|---|---|---|---|---|
| 36 — Robotique généraliste | agir | fiabilité de la manipulation | technique | **contredite** |
| 37 — Découverte scientifique | apprendre | validation expérimentale | industriel | vérifiée |
| 38 — Intelligence distribuée | calculer, relier | exploitation du parc | opérationnel | vérifiée |
| 39 — Autonomie mobile | agir, percevoir | démonstration de sûreté | institutionnel | vérifiée |
| 40 — Énergie et calcul | calculer, alimenter | raccordement électrique | industriel et institutionnel | vérifiée |
| 41 — Biologie programmable | fabriquer | capacité de production | industriel | **contredite** |

**Quatre vérifications, deux contradictions — et les deux contradictions s'expliquent par la même règle.**

### La thèse, dans sa formulation corrigée

Voici ce que les six dossiers autorisent à affirmer, et rien de plus :

> **Dans la majorité des convergences, le maillon le plus en retard se situe hors de la couche qui donne son nom au phénomène — et le plus souvent dans une contrainte industrielle, opérationnelle ou institutionnelle.**
>
> **L'exception est identifiable à l'avance : quand la couche éponyme est celle où se joue la fabrication ou le contact physique, le verrou peut y rester.**

**Pourquoi cette formulation vaut mieux que l'originale.** Elle est **réfutable** — on peut lui opposer un cas. Elle est **prédictive** — elle dit à l'avance dans quels cas s'attendre à l'exception. Et elle est **vérifiée sur son corpus** sans avoir été arrondie.

Une thèse vérifiée quatre fois sur six dont les exceptions s'expliquent vaut mieux qu'une thèse assénée. **C'est l'application de P10 du volume 1 à un résultat de ce volume.**

---

### Trois observations que seuls les six dossiers réunis produisent

#### Un — Le verrou est un rapport, jamais une étape

**Dans les six cas sans exception**, ce qui bloque n'est pas la performance d'un composant mais un déséquilibre entre deux grandeurs.

| Dossier | Le rapport qui bloque |
|---|---|
| 36 | taux de succès contre coût de traitement des échecs |
| 37 | coût de génération contre coût de validation |
| 38 | coût d'acquisition contre coût annuel d'exploitation |
| 39 | capacité démontrée contre capacité démontrable |
| 40 | délai de construction contre délai de raccordement |
| 41 | vitesse de conception contre capacité de production |

**C'est le résultat le plus solide de cette partie**, et il a une conséquence méthodologique directe : **devant toute annonce de convergence, chercher les deux grandeurs dont le rapport décide** — et non le composant le plus avancé.

Ni l'atlas ni la taxonomie ne pouvaient produire ce constat : l'un traite des objets, l'autre des mots. **Les rapports entre objets n'apparaissent qu'en les faisant travailler ensemble.**

#### Deux — Le signal qui trancherait n'est jamais publié

Données d'exploitation d'une flotte robotique · coût et durée d'un cycle expérimental · coût annuel d'exploitation par capteur · ratio d'opérateurs par véhicule · délais de raccordement par zone · taux de validation expérimentale.

**Ce sont toutes des grandeurs d'exploitation**, et elles sont systématiquement absentes du discours public — qui porte sur les capacités.

**Ce n'est pas une dissimulation, c'est une propriété de ce qui se communique.** On publie ce qui progresse, pas ce qui borne. Et ce qui borne relève de l'exploitation, c'est-à-dire du travail le moins visible.

**Conséquence pour votre veille**, et le chapitre 46 y reviendra : **les signaux les plus informatifs viennent des exploitants, pas des concepteurs.** Un rapport d'exploitation, un carnet de commandes de transformateurs, un délai de raccordement publié valent davantage que dix annonces de performance.

#### Trois — Cinq verrous sur six sont hors de la technique

Un seul dossier — la robotique généraliste — a un maillon en retard proprement technique. Les cinq autres butent sur l'industriel, l'opérationnel ou l'institutionnel.

**C'est cohérent avec les deux résultats obtenus plus tôt dans ce volume** : sur 45 termes de la taxonomie, 34 masquaient une contrainte non physique ; sur 162 entrées d'atlas, la contrainte dominante était technique dans une minorité de cas.

**Trois découpages, trois unités d'analyse, un même constat — un résultat convergent, non une preuve indépendante.** Ce n'est plus une impression : c'est un résultat, et il commande la manière de lire toute annonce technologique.

---

### Ce que cette partie ne dit pas

**Aucune date.** Aucun des six dossiers ne comporte de calendrier, et cette absence est délibérée. Ce qu'ils produisent — des seuils, des ordres, des signaux, des réfutations — reste valide quand les échéances glissent, ce qu'aucune date ne permet.

**Aucun classement.** Les six convergences ne sont pas comparées entre elles par importance ou par proximité. Ce serait une hiérarchie de valeurs déguisée en analyse.

**Aucun pronostic.** Les chronologies conditionnelles disent ce qui devrait devenir vrai, pas ce qui deviendra vrai. **La différence est la seule chose que ce volume peut honnêtement offrir**, et elle est plus utile qu'une prédiction : elle dit quoi surveiller.

---

### Passage à la Partie V

Les six dossiers ont répondu à : **que se passe-t-il si ces capacités convergent ?**

La partie suivante pose une autre question : **que devient le système lorsqu'une capacité se diffuse effectivement ?** Non pas ce qu'elle permet, mais **quels goulets se déplacent, quelles dépendances se constituent, et ce qui ne change pas.**

Quatre chapitres, dont le dernier traite d'un phénomène que le volume 1 avait identifié comme un angle mort de sa propre méthode : **les dépendances que personne n'a décidées.**

---

---


## Ouverture de la Partie V

L'atlas décrivait des objets. Les convergences décrivaient ce qui se produit quand plusieurs deviennent simultanément suffisants.

Cette partie pose la question suivante : **que devient le système lorsqu'une capacité se diffuse effectivement ?**

### Ce que cette partie fait, et ne fait pas

**Elle ne prédit pas d'impacts.** « Les impacts futurs de l'IA » n'est pas une question analysable : elle n'a ni périmètre, ni seuil, ni condition de vérification.

**Elle analyse des déplacements de contrainte.** Quand une capacité devient abondante, ce qui était rare cesse de l'être — et autre chose devient rare. **La question est de savoir quoi.**

### La discipline commune aux quatre chapitres

Chacun traite, dans cet ordre :

**① Ce qui devient abondant** — la capacité dont le coût s'effondre.
**② Ce qui devient rare** — le nouveau goulet.
**③ Ce qui ne change pas** — et pourquoi, ce qui est souvent la partie la plus utile.
**④ Le rythme imposé** — renouvellement de parc, formation, cadre.
**⑤ Les positions en présence** — exposées avec leurs hypothèses, sans arbitrage.
**⑥ Ce qu'il faudrait observer** — pour trancher, ou pour changer d'avis.

**Le mouvement ③ est le plus important.** Une transformation se caractérise autant par ce qu'elle laisse intact que par ce qu'elle modifie — et l'attention se porte spontanément sur le second.

### Neutralité

Les quatre chapitres portent sur des sujets contestés. Ce volume expose les positions sérieuses avec leurs hypothèses, indique ce qui ferait évoluer chacune, et **ne tranche pas** — parce que trancher supposerait des arbitrages de valeurs qui n'appartiennent pas à un livre technique.

Il distingue en revanche systématiquement : **consensus solide · débat scientifique ouvert · incertitude · récit spéculatif.**

---


## Chapitre 42 — Quand produire du plausible devient presque gratuit

### ① Ce qui devient abondant

**La production de contenu vraisemblable** — texte, image, son, vidéo, code, données — dont le coût marginal tend vers celui du calcul consommé.

**Ce n'est pas la première fois qu'un coût de production s'effondre.** L'imprimerie, la photographie, la reprographie, la publication en ligne ont chacune produit un effondrement comparable. **Ce qui change ici est que la production devient indépendante de la compétence** : il ne faut plus savoir écrire, dessiner ou filmer pour produire quelque chose de plausible.

**Précision nécessaire.** Plausible ne signifie ni vrai, ni bon, ni utile. **C'est le coût de production du vraisemblable qui s'effondre**, pas celui de la qualité — et cette distinction commande tout le chapitre.

---

### ② Ce qui devient rare

**La vérification.**

**Le mécanisme, et il est asymétrique.** Produire une affirmation plausible coûte désormais presque rien. La vérifier coûte ce qu'elle a toujours coûté — parfois davantage, puisqu'il faut d'abord établir qu'il y a lieu de vérifier. **L'écart entre les deux coûts s'est creusé de plusieurs ordres de grandeur en quelques années.**

**Trois conséquences directes.**

**Le coût de l'attention devient dominant.** Trier ce qui mérite d'être lu, écouté ou examiné consomme un temps qui ne baisse pas. Quand l'offre de contenu croît sans limite et que le temps disponible reste fixe, **la contrainte se déplace vers la sélection**.

**La provenance prend de la valeur.** Si l'on ne peut pas vérifier le contenu, on vérifie son origine — d'où l'importance des dispositifs du chapitre 29. **Mais cette bascule a un prix** : elle transfère la confiance du contenu vers l'émetteur, donc vers la réputation, donc vers des acteurs établis.

**La charge de la preuve se déplace.** Quand tout peut être fabriqué, l'absence de preuve d'authenticité devient un argument — et le chapitre 29 a établi l'asymétrie décisive : **les systèmes de provenance permettent d'affirmer une origine, jamais de nier une origine.** Un contenu authentique sans métadonnées est indiscernable d'un contenu fabriqué.

---

### ③ Ce qui ne change pas

**Le coût de l'établissement d'un fait.** Vérifier qu'un événement a eu lieu, qu'une mesure est exacte, qu'un témoignage est fiable suppose un travail qui n'a pas été affecté. **L'abondance de contenu ne produit aucune abondance de faits établis** — et c'est ce qui explique que le rapport entre les deux se dégrade.

**Le fonctionnement des institutions de vérification.** Tribunaux, expertises, audits, revues par les pairs, procédures administratives : leur rythme est fixé par des exigences de procédure et par la disponibilité de personnes compétentes. **Ils ne s'accélèrent pas, ce qui les rend structurellement débordables.**

**La confiance interpersonnelle.** Ce que quelqu'un tient d'une personne qu'il connaît n'est pas affecté. **Une conséquence intéressante en découle** : la valeur relative des canaux personnels et fermés augmente à mesure que les canaux ouverts deviennent moins discriminables.

**Et la difficulté des questions.** Aucune abondance de production ne rend un problème moins difficile. Un contenu plausible sur une question ouverte reste un contenu sur une question ouverte.

---

### ④ Le rythme imposé

**Rapide du côté de la production**, dont l'adoption ne dépend d'aucune infrastructure lourde ni d'aucun renouvellement de parc — c'est le domaine de cet ouvrage où le déploiement est le plus rapide.

**Lent du côté de la vérification.** Les dispositifs de provenance dépendent d'une couverture : appareils de capture, logiciels d'édition, plateformes de diffusion doivent tous les implémenter. **C'est un problème de standard et de complément**, avec le calendrier correspondant — plusieurs années au minimum.

**Très lent du côté institutionnel.** Les règles de preuve, les procédures d'expertise et les cadres juridiques évoluent sur des décennies.

**L'écart entre ces trois rythmes est le sujet du chapitre.** Ce n'est pas la capacité qui produit l'effet, c'est le décalage.

---

### ⑤ Les positions en présence

**Trois lectures coexistent**, et elles reposent sur des hypothèses différentes qu'il vaut mieux nommer.

**La première tient que l'effet sera absorbé.** Argument : chaque effondrement antérieur du coût de production — imprimerie, photographie, publication en ligne — a été suivi d'une adaptation des pratiques et des institutions. **Hypothèse sous-jacente** : le rythme d'adaptation est comparable à celui des transitions précédentes.

**La deuxième tient que l'asymétrie est nouvelle.** Argument : les effondrements antérieurs réduisaient le coût de diffusion, celui-ci réduit le coût de fabrication du vraisemblable — ce qui n'a pas de précédent. **Hypothèse sous-jacente** : la vérification ne peut pas être automatisée au même rythme que la production.

**La troisième tient que le problème se déplacera vers la confiance institutionnelle.** Argument : si le contenu ne peut être vérifié, la société se réorganisera autour de sources autorisées. **Hypothèse sous-jacente** : ces sources existent et sont jugées crédibles — ce qui est précisément contesté dans plusieurs pays.

**Ce que ce volume constate.** Les trois hypothèses sont testables, et aucune n'est encore tranchée. **Ce qui n'est pas contesté** : l'asymétrie entre coût de production et coût de vérification s'est creusée, et les dispositifs de provenance ne peuvent affirmer une origine que lorsqu'ils sont présents.

---

### ⑥ Ce qu'il faudrait observer

**La couverture des dispositifs de provenance** dans le parc d'appareils de capture et sur les plateformes de diffusion. **C'est la grandeur la plus directe** et elle est mesurable.

**L'évolution des règles de preuve** dans les procédures juridiques et administratives : à partir de quand un contenu non attesté cesse-t-il d'être recevable ?

**Le coût de l'attention**, mesurable indirectement par le temps consacré à la sélection dans les usages professionnels.

**Et un contre-signal** : si des méthodes de vérification automatisée atteignaient une fiabilité durable, l'asymétrie se réduirait. **Le volume 1 rappelle la prudence** — la détection de contenus synthétiques se dégrade à mesure que les générateurs progressent, ce qui en fait une course et non une solution.

---


## Chapitre 43 — Quand les machines agissent dans le monde

### ① Ce qui devient abondant

**La capacité d'exécuter des actions physiques sans intervention humaine continue** — manipulation, déplacement, inspection, maintenance — sur des tâches dont la variété augmente.

**Précision nécessaire.** Cette abondance est **conditionnelle et partielle** : le dossier 36 a établi que le maillon en retard est la fiabilité, et le dossier 39 que l'extension est bornée par la démonstration de sûreté. **Ce chapitre analyse ce qui se produirait si ces verrous cédaient**, et il le dit.

---

### ② Ce qui devient rare

**Trois choses, et la première n'est pas celle qu'on attend.**

**La maintenance et les compétences de terrain.** Le dossier 36 l'a établi : le nombre de personnes capables d'entretenir des machines borne le déploiement bien avant la capacité de production. **Former un technicien qualifié se compte en années**, et cette contrainte ne bénéficie d'aucun effet d'échelle.

**La responsabilité identifiable.** Quand une action physique cause un dommage, il faut établir qui répond. Les régimes classiques répartissent entre fabricant, exploitant et utilisateur, et supposent qu'on puisse établir ce qui s'est passé et qui a décidé. **Un système qui décide brouille les deux** — et l'incertitude juridique bloque le déploiement même quand tout le reste fonctionne, parce qu'elle empêche de contracter.

**La coordination entre humains et machines partageant un espace.** Ce n'est pas un problème de sécurité mais d'organisation : qui a la priorité, comment on signale une intention, ce qui se passe quand les deux se bloquent mutuellement.

---

### ③ Ce qui ne change pas

**Le renouvellement des installations.** Un site industriel s'équipe au rythme de ses investissements, et un site moyen fait cohabiter des équipements de plusieurs décennies. **Une capacité disponible ne s'installe pas plus vite que le cycle d'investissement.**

**La structure des coûts d'exploitation.** Le chapitre 15 l'a établi : le coût total de possession d'une flotte est dominé par la maintenance, non par l'acquisition. **Automatiser déplace le coût du travail direct vers le travail de maintenance et de supervision** — il ne le supprime pas.

**La difficulté de la manipulation.** Les quatre raisons du chapitre 14 sont physiques : le contact change la dynamique, il faut contrôler des forces, les objets diffèrent, certaines erreurs sont irréversibles. **Aucune ne se résout par le calcul.**

**Et le fait que l'environnement décide.** La difficulté suit le degré de structuration du lieu, pas la sophistication de la machine — c'est le résultat le plus net de la couche *agir*, et il ne bouge pas.

---

### ④ Le rythme imposé

**Le cycle d'investissement industriel** — quinze à trente ans pour un équipement de production.

**La formation** — années pour un technicien, décennie pour l'expérience qui permet de traiter les cas non standard.

**Le cadre** — certification, responsabilité, assurance, dont le dossier 39 a montré qu'ils sont le maillon en retard.

**Et une temporalité propre à ce chapitre : l'apprentissage organisationnel.** Une organisation qui intègre des machines autonomes doit réviser ses processus, ses métiers et ses responsabilités. **Le volume 1 l'a établi sur un autre cas** : une capacité installée sans réorganisation ne produit aucun gain mesurable.

---

### ⑤ Les positions en présence

Le sujet est contesté et les positions reposent sur des hypothèses distinctes.

**Sur l'ampleur de la substitution du travail.** Une position tient que l'automatisation physique substituera des tâches plutôt que des métiers, comme les vagues précédentes — hypothèse : la variété des tâches d'un métier reste supérieure à ce qu'une machine peut couvrir. Une autre tient que le seuil de variété franchi change la nature de la substitution — hypothèse : la généralité rend la décomposition en tâches moins protectrice.

**Sur la vitesse.** Une position insiste sur les contraintes physiques, de maintenance et de cadre — celles que ce chapitre expose. Une autre observe que ces contraintes ont été surmontées dans d'autres domaines et que leur invocation a souvent été un argument de sous-anticipation.

**Ce que ce volume constate, et il faut être précis.** Les contraintes exposées ici — maintenance, responsabilité, renouvellement, formation — **sont observables et chiffrables**. Leur ampleur ne fait pas débat ; ce qui fait débat est la vitesse à laquelle elles seront levées. **Ce n'est pas la même chose qu'un désaccord sur les faits.**

Et une observation de méthode : **les deux positions se réclament du volume 1.** L'une invoque le mur de la fiabilité et le renouvellement du parc ; l'autre invoque le scepticisme automatique et les erreurs de sous-anticipation. **Les deux ont raison sur leur mécanisme** — ce qui indique que la question n'est pas tranchable par la méthode seule.

---

### ⑥ Ce qu'il faudrait observer

**Le ratio d'opérateurs par machine**, publié par des exploitants. **C'est le signal décisif de ce chapitre** — il détermine si l'automatisation réduit le coût du travail ou le déplace.

**Le nombre de techniciens formés** par an dans les filières concernées, comparé au parc déployé.

**L'apparition d'une offre d'assurance** couvrant l'exploitation de machines autonomes en environnement partagé.

**Et la profondeur des déploiements** : un exploitant qui passe de dix à mille machines apprend quelque chose qu'aucune démonstration ne montre — **c'est là que se lit le franchissement du seuil de fiabilité**.

**Signaux non informatifs.** Le nombre de machines livrées. Les démonstrations, quelle que soit leur variété. Les annonces de production en série, qui sont des objectifs.

---

---


## Chapitre 44 — Quand observer devient permanent et bon marché

### ① Ce qui devient abondant

**L'observation exploitable** — c'est-à-dire non pas la captation, mais la captation **suivie d'une lecture**.

**La distinction est tout le chapitre.** Enregistrer est bon marché depuis longtemps : les caméras, les journaux d'accès, les images satellitaires, les relevés de capteurs s'accumulent depuis des décennies. **Le coût dominant a longtemps été celui du regard plutôt que celui du capteur** — quelqu'un devait regarder, comparer, indexer. Une archive que personne n'examine n'a d'effet sur rien.

**C'est ce coût-là qui s'effondre.** L'interprétation automatique de flux — images, sons, séquences, mesures — transforme des archives dormantes en matière consultable. Le chapitre 42 traitait de l'effondrement du coût de production du vraisemblable ; **celui-ci traite de l'effondrement symétrique du coût de lecture du réel.**

**Trois mouvements le rendent possible en même temps**, et aucun ne suffit seul : des capteurs issus des chaînes grand public, dont le prix suit des volumes qui ne sont pas les leurs ; des porteurs accessibles, dont les constellations en orbite basse sont le cas le plus visible ; et une capacité d'interprétation générique, qui n'exige plus un modèle par cas d'usage.

**Précision nécessaire.** Observer davantage ne signifie pas savoir davantage. **Une détection n'est pas un fait**, et le mouvement ③ y revient — c'est le point où ce chapitre se sépare le plus nettement de son récit.

---

### ② Ce qui devient rare

**La non-observation par défaut.**

**Le mécanisme, et il est simple.** Ce qui n'était pas observé ne l'était pas par décision, mais par coût : personne n'avait les moyens de regarder partout, tout le temps, ni de relire trois ans d'enregistrements pour y chercher une occurrence. **Cette protection n'était pas un droit, c'était une contrainte économique** — et elle disparaît sans qu'aucune règle n'ait changé.

**La conséquence la moins intuitive est rétroactive.** Ce qui a été capté hier devient lisible aujourd'hui. Une collecte décidée à une époque où son exploitation était impraticable produit ses effets des années plus tard, sans nouvelle décision.

**La qualification devient le goulet.** Une détection automatique est une hypothèse assortie d'un taux d'erreur, souvent inconnu hors du domaine où elle a été évaluée — l'entrée *détection de sortie de domaine* du chapitre 30 en donne le mécanisme. **Transformer une détection en élément opposable suppose un étalonnage, une traçabilité, une contradiction possible** : c'est un travail humain et procédural qui n'a pas changé de coût.

**Et la position d'observateur indépendant devient rare.** Observer à grande échelle suppose un parc, un porteur, du calcul et de la donnée d'entraînement — donc du capital fixe. **La capacité d'observation se concentre chez ceux qui peuvent financer l'installation**, et le dossier 37 a établi que le même mécanisme joue sur l'observation scientifique instrumentée : ce qui devient rare n'est pas l'information, c'est **la capacité de produire une observation qu'on ne tient de personne.**

> **Note de traitement dual.** Le déplacement décrit ici concerne aussi les usages de défense, où il porte le nom d'*économie de l'attrition* : lorsque détecter et engager des plateformes consommables devient peu coûteux, le rapport entre le coût de ce qui est engagé et le coût de ce qu'il oblige à protéger se déforme. **Ce volume traite ce point au niveau économique, industriel, doctrinal et de gouvernance uniquement**, conformément à la règle appliquée aux chapitres 16 et 17, et ne fournit aucun élément d'emploi.

---

### ③ Ce qui ne change pas

**La physique de la mesure.** Un capteur reste borné par la distance, l'ouverture, l'atmosphère, l'occultation et le compromis entre champ et résolution — le chapitre 5 l'a établi bande par bande. **Aucune quantité d'interprétation ne fait voir ce qui n'a pas été capté**, et le SAR, qui traverse la couverture nuageuse, n'échappe pas à ses propres limites.

**La couverture reste un budget.** Observer en continu suppose de l'énergie, de la bande passante, du stockage et — depuis l'espace — des créneaux de revisite fixés par l'orbite. **L'observation permanente est une propriété locale, jamais globale** : elle est obtenue là où on a payé pour l'obtenir.

**Le coût d'établissement d'un fait**, déjà rencontré au chapitre 42 et inchangé ici sous une autre forme. Une observation n'est pas une preuve : il faut établir qu'elle porte sur ce qu'on croit, qu'elle n'a pas été altérée, qu'elle est reproductible. **L'abondance d'observations ne produit aucune abondance de faits établis.**

**Le nombre d'alertes traitables par jour.** Une détection sans destinataire capable d'agir ne produit rien. **Le maillon humain en aval se met beaucoup moins bien à l'échelle que la détection**, et la Partie IV a montré que le coût complet d'exploitation par capteur, non le prix du capteur, décide des déploiements.

**Et l'impossibilité d'observer une intention.** On observe des comportements. L'écart entre ce qui est observé et ce qui est inféré ne se réduit par aucun progrès de capteur — **c'est une limite de nature, pas de performance.**

---

### ④ Le rythme imposé

**Immédiat du côté de l'exploitation.** Améliorer l'interprétation peut s'appuyer sur un parc existant, sans chantier ni déploiement nouveau : cela s'applique aux flux déjà collectés, et rétroactivement aux archives. **C'est la temporalité la plus rapide de toute la Partie V.**

**Moyen du côté du parc.** Les capteurs se renouvellent au rythme des équipements qui les portent. Le spatial fait exception dans un sens inattendu : la durée de vie courte des satellites en orbite basse rend le renouvellement **plus** rapide que celui des infrastructures terrestres.

**Lent du côté du cadre.** Recevabilité d'une détection automatique, régimes de conservation, obligations de journalisation : ces règles évoluent par jurisprudence et par crise, sur des décennies.

**L'asymétrie propre à ce chapitre est la rétroactivité.** Dans les autres transformations de cette partie, une capacité nouvelle agit sur l'avenir. Ici, **elle agit aussi sur le passé déjà enregistré** — ce qui rend toute décision de collecte plus engageante qu'elle n'en a l'air au moment où elle est prise.

---

### ⑤ Les positions en présence

**Sur la vie privée, trois positions sérieuses**, et leurs hypothèses ne sont pas du même ordre.

**Réguler l'usage plutôt que la collecte.** Argument : interdire la collecte est inapplicable et prive d'usages légitimes ; ce qui compte est ce qu'on en fait. **Hypothèse sous-jacente** : l'usage est auditable *a posteriori*, donc l'auditabilité technique existe et l'auditeur a les moyens.

**Réguler la collecte elle-même.** Argument : une donnée conservée finit par être exploitée, et la rétroactivité rend l'engagement d'usage non tenable dans la durée. **Hypothèse sous-jacente** : la limitation à la source est vérifiable, ce qui est plus facile pour un parc déclaré que pour un capteur diffus.

**Tenir que la régulation nationale est structurellement insuffisante.** Argument : l'observation depuis l'espace ignore les frontières et l'exploitation peut être délocalisée. **Hypothèse sous-jacente** : les points de contrôle utiles sont l'accès au marché et l'accès à la donnée, non l'acte d'observer.

**Sur l'effet en matière de sécurité**, le débat est empirique et le niveau de preuve est déséquilibré — il faut le dire plutôt que de fabriquer une symétrie. **Que le coût de l'observation ait chuté est documenté et mesurable.** Que l'observation généralisée réduise le risque ne l'est pas : les évaluations disponibles sont contextuelles, difficilement transférables, et les effets de déplacement y sont mal capturés.

**Sur le versant doctrinal**, une position tient que la transparence du champ d'observation renforce ce qui défend, puisque détecter précède tout ; une autre tient qu'elle avantage ce qui est nombreux et peu coûteux, puisque ce qui est vu doit être protégé et que la protection est chère. **Les deux se réclament du même constat** — l'observation devient bon marché — et divergent sur la grandeur qui décide, ce qui est la signature d'un désaccord de rythme et non de fait.

---

### ⑥ Ce qu'il faudrait observer

**Le coût complet d'exploitation par capteur et par an**, publié par un exploitant. **C'est le signal décisif** — la Partie IV avait déjà noté qu'il n'est presque jamais publié.

**La part des flux réellement exploités automatiquement**, à distinguer de la part collectée : c'est le seul indicateur qui mesure l'abondance décrite au mouvement ①.

**La recevabilité d'une détection automatique** comme élément de preuve dans les procédures, et les conditions posées à cette recevabilité — étalonnage, journalisation, contradiction.

**L'accès commercial à de l'imagerie récente** pour des acteurs sans capacité propre : la diffusion se lit là, bien mieux que dans les résolutions annoncées.

**Signaux non informatifs.** La résolution annoncée d'un capteur ou d'un satellite. Le nombre de satellites lancés. Les performances de détection sur jeux de données publics, dont le chapitre 30 a montré qu'elles ne prédisent pas le comportement hors domaine.

---
