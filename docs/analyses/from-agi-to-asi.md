---
title: Analyse — From AGI to ASI
date: 2026-09-04
kind: analysis
theme: ia
slug: from-agi-to-asi
author: Google DeepMind
---
# Analyse — *From AGI to ASI*

> **Convention :** **[Rapport]** = contenu du document ; **[Externe]** = information issue d'une source externe datée ; **[Analyse]** = interprétation de la présente analyse.
>
> **Mise à jour : 4 septembre 2026.** La version analysée date du 30 août 2026 : il n'existe que cinq jours de recul sur cette version. Les développements « depuis publication » distinguent donc le dépôt initial du 10 juin de la v2, sans prétendre fournir une validation de long terme.

## Métadonnées

- **Titre :** *From AGI to ASI*
- **Sous-titre :** aucun.
- **Auteurs :** Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, Samuel Albanie, Adam Bales, Cole Wyeth, Stephanie Chan, Iason Gabriel, Joel Z. Leibo, Allan Dafoe, Marcus Hutter, Thore Graepel et Shane Legg.
- **Affiliations :** Google DeepMind ; University of Waterloo ; Australian National University ; University College London. Le travail de Cole Wyeth est indiqué comme réalisé chez Google DeepMind.
- **Première publication :** 10 juin 2026.
- **Version analysée :** v2, 30 août 2026 (`arXiv:2606.12683v2 [cs.AI]`).
- **Support :** rapport Google diffusé sur arXiv, identifiant 2606.12683.
- **Thème :** trajectoires de l'intelligence artificielle générale (AGI) à la superintelligence générale (ASI), freins possibles et agenda de recherche.

## Résumé exécutif

**[Rapport]** L'AGI est caractérisée informellement comme un système atteignant au moins la performance humaine médiane sur un très large ensemble de tâches cognitives. L'ASI dépasse de grands collectifs — des milliers — d'experts humains bien coordonnés, travaillant pendant des années, dans presque tous les domaines. Au-delà, l'intelligence artificielle universelle (UAI), représentée par AIXI, fournit une borne théorique incomputable, pas un plan de système réalisable.

**[Rapport]** Quatre trajectoires non exclusives pourraient progresser en parallèle et se renforcer : scaling du calcul, des modèles et des données ; évolutions ou ruptures algorithmiques ; automatisation de la R&D et amélioration récursive ; collectifs massifs d'agents. Six freins interdépendants leur sont opposés : données, ressources économiques et physiques, insuffisance du paradigme neuronal, difficulté croissante de la recherche, barrière de l'abstraction, et ralentissement délibéré/réglementaire/social.

**[Rapport]** Les auteurs ne donnent ni date d'AGI ou d'ASI, ni certitude d'explosion d'intelligence. Leur conclusion conditionnelle est qu'une fois l'AGI atteinte, un arrêt exactement au niveau humain paraît peu plausible, notamment parce qu'un logiciel peut être accéléré, copié et coordonné. Ils demandent des mesures, benchmarks post-humains, prévisions continuellement actualisées, lois d'échelle sur la récursion et les collectifs, théorie, sûreté et gouvernance.

**[Externe]** Au 4 septembre 2026, aucune source consultée ne démontre une AGI au sens du rapport, une ASI, ou une boucle autonome et soutenue d'amélioration récursive. Les données renforcent des conclusions plus modestes : le calcul à l'inférence améliore certaines tâches ; l'autonomie logicielle progresse mais reste limitée ; l'IA contribue à quelques problèmes d'optimisation de R&D sans mesure robuste de l'accélération globale ; les collectifs d'agents présentent gains, surcoûts et amplification d'erreurs selon les tâches.

**[Analyse]** La valeur du rapport est celle d'une carte de variables, non d'une prévision. Sa force est de considérer le système complet — matériel, données, inférence, recherche, agents, organisations et gouvernance. Sa faiblesse est qu'une taxonomie plausible ne fournit pas encore les probabilités, causalités et métriques permettant de départager les scénarios.

## Chronologie

- **1950 — [Rapport]** Turing, cité en épigraphe, formule les interrogations fondatrices.
- **Depuis environ six décennies — [Rapport]** le calcul par dollar aurait progressé d'environ 1,5×/an.
- **Depuis 2012 — [Rapport]** le calcul nécessaire pour atteindre la performance d'AlexNet sur ImageNet aurait diminué d'environ 3×/an.
- **Décennie précédant le rapport — [Rapport]** investissements matériels ≈2,5×/an, plus grands entraînements ≈4×/an ; combinés à l'efficacité algorithmique, Epoch AI estime ≈10×/an de « calcul effectif », avec forte incertitude.
- **10 juin 2026 — [Rapport]** première soumission arXiv.
- **11 juin 2026 — [Externe]** DeepMind et ses partenaires annoncent jusqu'à 10 M$ pour la sûreté multi-agents.
- **21 juillet 2026 — [Externe]** METR propose l'« expenditure horizon » pour comparer optimisation humaine et agentique à budget égal.
- **30 août 2026 — [Rapport]** v2 analysée.
- **3 septembre 2026 — [Externe]** Epoch AI révise son modèle des centres Google : calcul H100-équivalent couvert -15 % actuellement et -14 % en projection.
- **4 septembre 2026 — [Analyse]** recul insuffisant pour juger la résistance au temps de la v2.

## Thèse principale

**[Rapport]** Le niveau humain n'est probablement pas une limite naturelle : vitesse, mémoire, réplication, portabilité et partage d'expérience numériques pourraient augmenter les capacités d'une instance ou d'un collectif. Mais la transition n'est ni garantie ni nécessairement rapide : rendements décroissants, ressources, données, limites algorithmiques, expériences physiques lentes et décisions politiques peuvent la freiner.

**[Analyse]** Deux prémisses restent à établir : qu'une AGI ainsi définie soit réalisable, puis que ses avantages numériques deviennent un travail fiable, autonome, coordonné et économiquement utile. Le rapport argumente la possibilité, pas la réalisation.

## Informations et arguments importants

### Définitions et cadre

- **[Rapport] AGI minimale :** niveau approximativement humain médian sur un très large éventail cognitif, malgré un profil possiblement très irrégulier.
- **[Rapport] ASI :** supériorité générale sur de grands collectifs d'experts ; elle peut elle-même être un collectif de millions d'instances.
- **[Rapport] UAI/AIXI :** agent théorique maximisant la récompense espérée dans une classe très générale d'environnements calculables, lié à l'induction de Solomonoff et au score de Legg-Hutter ; AIXI est incomputable.
- **[Rapport] Limites :** observation imparfaite, temps réel, énergie, thermodynamique, manipulation de matière, complexité, problème de l'arrêt et incomplétude logique s'appliquent aussi à une ASI.
- **[Analyse]** « humain médian », « très large ensemble » et « presque tous les domaines » ne forment pas un protocole opérationnel ; outils, coût, délai et choix des tâches peuvent changer le classement.

### Six avantages numériques augmentant avec le calcul

La liste reste non fusionnée, conformément aux « Summary Instructions » activées par l'utilisateur.

1. **[Rapport] Vitesse d'entrée-sortie :** ingestion et production à très haut débit, sous réserve des capteurs, réseaux et actionneurs.
2. **[Rapport] Vitesse de traitement interne :** accélération séquentielle ou parallèle de la pensée, avec rendements décroissants et parties non parallélisables.
3. **[Rapport] Mémoire de travail et mémorisation :** capacité, fidélité et bande passante potentiellement très supérieures aux limites biologiques.
4. **[Rapport] Indépendance du support :** migration vers du matériel plus puissant/efficace et distribution sur des systèmes hétérogènes.
5. **[Rapport] Réplication sans perte :** copie du code et de l'état, sauvegarde, suspension, reprise et multiplication rapide d'experts.
6. **[Rapport] Partage à haut débit des expériences :** stockage, copie et rejeu ; entre instances homogènes, échange possible de signaux bruts comme des gradients.

**[Rapport]** Contrepoints : l'analogique/biologique peut être plus économe ; le physique impose conversions et latences ; débit et mémoire ne garantissent ni compréhension ni abstraction nouvelle.

### Tendances quantitatives

- **[Rapport]** matériel ≈1,5×/an ; investissements ≈2,5×/an ; plus grands entraînements ≈4×/an ; efficacité algorithmique ≈3×/an sur AlexNet/ImageNet et jusqu'à 6×/an dans une autre étude.
- **[Rapport]** leur combinaison en ≈10×/an de calcul effectif est une estimation très incertaine, non une loi.
- **[Rapport]** illustration seulement : 1 000 instances d'AGI et 10×/an permettraient 100 millions d'instances en cinq ans, ou un million accélérées 100 fois.
- **[Rapport]** maintenir la loi de Moore mobiliserait environ 18 fois plus de chercheurs que dans les années 1970 (Bloom et al.).
- **[Externe]** la révision Epoch du 3 septembre ne réfute pas la croissance, mais illustre la dépendance des estimations aux hypothèses de ventes, déploiement, prix et puissance.

### Quatre trajectoires : description et évolution observée

#### 1. Scaling calcul–modèles–données

**[Rapport]** Davantage de calcul d'entraînement et d'inférence, de données et de capacité modèle pourrait prolonger les lois d'échelle. Ces entrées doivent être co-dimensionnées. Même si l'intelligence individuelle plafonne, réplication et accélération peuvent accroître le collectif.

**[Externe]** L'*International AI Safety Report 2026* (3 février) constate que post-entraînement et calcul à l'inférence ont produit de forts gains en mathématiques, logiciel et science, mais aussi des capacités « jagged » et un écart benchmark–réel. Après la v2, seule la révision d'infrastructure Epoch du 3 septembre apporte une donnée nouvelle ; elle ne donne pas une loi de capacité.

**[Analyse]** Voie active et la mieux documentée avant l'AGI, non démontrée jusqu'à l'ASI. Confiance élevée dans l'investissement à court terme, faible dans le maintien de 10×/an ou sa conversion générale en intelligence.

#### 2. Évolutions et ruptures de paradigme

**[Rapport]** Le paradigme associe préentraînement de transformers, post-entraînement, calcul à l'inférence, récupération, outils et échafaudages agentiques. Mémoire, récurrence, apprentissage continu, modèles du monde, planification, décision interactive, Mamba/S4 et matériel analogique/neuromorphique sont envisagés. Les ruptures véritables sont difficiles à prévoir.

**[Externe]** Aucune source consultée entre le 30 août et le 4 septembre ne constitue une rupture reconnue. Les progrès récents sont principalement des extensions du paradigme.

**[Analyse]** Évolutions continues visibles ; rupture vers l'ASI invérifiable à l'avance et catégorie difficilement falsifiable.

#### 3. Amélioration récursive

**[Rapport]** L'IA peut améliorer architectures, optimiseurs, matériel et données. Les auteurs distinguent des analogues génétiques (code/plans), culturels (données, outils, distillation) et coopératifs (spécialisation). NAS, conception de puces, FunSearch, AlphaEvolve et AI Scientists sont des formes partielles, pas une explosion démontrée.

**[Externe]** METR (21 juillet) recense des contributions crédibles — AlphaEvolve, TTT-Discover, NanoGPT — mais insiste sur biais de sélection, problèmes jouets et difficulté de convertir code ou auto-évaluations en productivité. Sur NanoGPT, son estimation préliminaire place l'horizon de dépense agentique entre 0 et 3 000 dollars après plus de 10 000 dollars d'exécution : résultat étroit.

**[Analyse]** Assistance et optimisation autonome progressent, sans boucle fermée capable de choisir, exécuter et valider toute la R&D et de maintenir des gains croissants.

#### 4. Coordination multi-agents

**[Rapport]** Des agents spécialisés pourraient former organisations, entreprises ou marchés centralisés ou distribués. Il faut relier population, organisation, tâches, communication, coût et intelligence collective.

**[Externe]** Kim et al. (9 décembre 2025), sur 180 configurations, trouvent des gains sur des tâches parallélisables mais une baisse de 39–70 % sur des tâches séquentielles ; erreurs amplifiées 17,2× dans certaines architectures indépendantes contre 4,4× en centralisé. Le financement annoncé le 11 juin 2026 cible réseaux d'agents, bancs d'essai, identité, réputation et supervision : c'est un programme, pas un résultat.

**[Analyse]** Voie plausible mais très conditionnelle. Les données contredisent la règle simple « plus d'agents = plus d'intelligence ».

### Six freins croisés avec les quatre trajectoires

| Frein | Scaling | Paradigmes | Récursion | Collectifs |
|---|---|---|---|---|
| **1. Mur des données** | Direct et fort : modèles croissants demandent données nouvelles ; synthèse, recherche à l'inférence, autojeu, simulation et interaction peuvent le déplacer. | Une meilleure efficacité en données peut le contourner ; le manque de données peut aussi masquer un paradigme. | Auto-génération/distillation peuvent améliorer, mais une boucle naïve peut dégénérer ; le vérificateur est crucial. | Les interactions génèrent des données, mais aussi erreurs corrélées et productions sans ancrage. |
| **2. Demande économique et ressources** | Capital, puces, énergie, eau, sites, matériaux, mémoire et interconnexions : impact potentiellement majeur. | Une rupture efficace relâche la contrainte ; son industrialisation peut exiger une pile coûteuse. | Entraînements, matériel et expériences physiques freinent même une R&D cognitive automatisée. | Multiplier instances et communications coûte ; les gains doivent dépasser coordination et bureaucratie. |
| **3. Paradigme neuronal insuffisant** | Bloquant si davantage d'échelle donne seulement des rendements décroissants. | C'est la voie compensatrice ; des IA sous-AGI peuvent aider la recherche. | Un chercheur artificiel trop fragile ne ferme pas la boucle, mais peut l'accélérer partiellement. | Diversité/vote compensent certaines erreurs, pas une faiblesse systématique commune. |
| **4. Recherche plus difficile** | Ralentit les gains d'efficacité nécessaires au scaling. | Frein majeur aux idées radicales et à leur reconnaissance. | Des chercheurs artificiels peuvent compenser ; rendements décroissants et expériences restent. | Parallélisme/spécialisation aident seulement si le problème est décomposable. |
| **5. Barrière de l'abstraction** | Le scaling sur produits humains pourrait plafonner conceptuellement malgré vitesse et volume. | Apprentissage incarné/interactif ou rupture pourrait l'attaquer. | La boucle recombinerait des concepts existants ; l'expérimentation ancrée impose du temps réel. | Contournement collectif possible sans création de nouvelles primitives individuelles. |
| **6. Ralentissement délibéré** | Plafonds, licences, évaluations, coûts ou moratoires retardent l'échelle. | Peut réorienter vers sûreté/efficacité ou bloquer le déploiement. | Restreindre calcul, code, expériences et autonomie peut casser la boucle. | Peut encadrer identité, transactions et population ; compétition et arbitrage peuvent l'affaiblir. |

**[Rapport]** Savoir si chaque frein est temporaire ou durable dépend de l'efficacité de ses contrepoids à mesure que les capacités évoluent : c'est une question ouverte.

### Réévaluation des freins au 4 septembre 2026

| Frein | Importance actuelle estimée | Justification |
|---|---|---|
| **Données** | **Moyenne à élevée pour le préentraînement naïf ; indéterminée globalement** | **[Externe]** déplacement des gains vers post-entraînement/inférence. **[Analyse]** adaptation au mur, pas disparition ; synthèse vérifiée prometteuse surtout lorsqu'un vérificateur fiable existe. |
| **Économie/ressources** | **Élevée comme friction, non établie comme plafond** | **[Externe]** investissements massifs et inventaires Epoch révisables. **[Analyse]** énergie, réseau, construction et coûts sont matériels ; retours et efficacité empêchent de conclure au plafond. |
| **Paradigme neuronal** | **Indéterminée** | **[Externe]** gains continus mais hallucinations, autonomie fragile et échecs simples. Ni suffisance vers l'ASI ni impossibilité démontrée. |
| **Recherche plus difficile** | **Moyenne** | **[Externe]** contributions utiles, mais METR ne trouve pas encore de mesure robuste de la productivité totale. |
| **Barrière de l'abstraction** | **Indéterminée ; preuve faible** | Aucun test consensuel n'isole la création de primitives nouvelles ; importance potentiellement majeure si vraie. |
| **Ralentissement délibéré** | **Moyenne, très contextuelle** | **[Externe]** davantage de cadres volontaires et quelques obligations ; incitations concurrentielles et limites des garde-fous persistent. |

## Agenda de recherche et progrès pertinents

1. **Freins et scaling — [Rapport]** Mesurer données synthétiques/interactives, expérience tierce, conversion calcul→intelligence, rentabilité, difficulté de recherche, goulet incarné et abstraction. **[Externe/Analyse]** Epoch et le rapport international améliorent l'observation, sans résoudre les freins.
2. **Prévision quantitative — [Rapport]** Coupler coût/FLOP, efficacité, calcul, capacités et macroéconomie ; ensembles de modèles, seuils, mises à jour et intervalles. **[Externe]** séries Epoch et horizons METR (8 mai 2026). **[Analyse]** le lien benchmark→productivité→intelligence reste faible.
3. **Benchmarks post-humains — [Rapport]** Compétitions/cooperations, setter–solver, compression générale, productivité indirecte, distinction saut qualitatif/saturation. **[Externe]** horizons temporel et de dépense de METR ; l'évaluation internationale souligne l'écart au réel. Aucun benchmark consensuel d'ASI.
4. **Récursion — [Rapport]** Lois par mécanisme, test-time search, curation, distillation, vérificateurs, contribution aux algorithmes/matériel et productivité scientifique. **[Externe]** l'expenditure horizon répond au besoin de comparaison à coût égal, mais NanoGPT peut surestimer la R&D réelle.
5. **Multi-agents — [Rapport]** Délégation, décomposition, organisations, comparaison population/modèle, alignement de groupe, résilience épistémique humain–ASI. **[Externe]** Kim et al. quantifient coordination et erreurs ; l'appel de juin institutionnalise la sûreté. Pas de loi universelle.
6. **Fondements — [Rapport]** Approximer AIXI sous budget, relier compression/décision/complexité, expliquer les capacités irrégulières et modéliser les systèmes myopes/non agentiques. **[Externe/Analyse]** aucun travail consulté ne ferme l'écart théorie–pratique.
7. **Sûreté et société — [Rapport]** Mise en œuvre du ralentissement, alignement individuel/collectif, buts instrumentaux, normes scientifiques sous surproduction et transfert travail→capital. **[Externe]** le rapport international documente risques, limites des garde-fous et résilience ; la sûreté conditionne l'usage de l'IA pour la R&D.

## Points particulièrement intéressants pour la veille

- **[Analyse] Calcul effectif :** suivre séparément matériel, capital et logiciel avec hypothèses et incertitudes auditables.
- **[Analyse] Inference scaling–distillation :** vérifier si les traces améliorées deviennent des données fiables sans contamination.
- **[Analyse] R&D réelle :** mesurer coût, horizon, intervention humaine, nouveauté et validation, pas seulement volume de code.
- **[Analyse] Agent supplémentaire :** ventiler les gains par parallélisme, topologie, communication, erreurs corrélées et supervision.
- **[Analyse] Benchmark post-humain :** contrôler fuite, entraînement sur le test et écart au réel.
- **[Analyse] Goulet incarné :** distinguer les domaines à vérification numérique rapide de l'expérimentation physique lente.
- **[Analyse] Gouvernance endogène :** investissements, concentration du calcul, normes, incidents et concurrence sont couplés à la technique.
- **[Analyse] Transformations successives :** surveiller les inflexions sectorielles plutôt qu'un unique « moment AGI ».

## Faits, opinions et interprétations

### Faits rapportés par la source

- Quatre trajectoires et six freins, non exhaustifs ; trajectoires parallèles et effets composés.
- Distinction entre AGI humaine médiane, ASI supérieure à des collectifs et UAI/AIXI incomputable.
- Tendances historiques quantitatives présentées avec prudence, sans calendrier fiable.
- AlphaZero, AlphaEvolve et AI Scientists sont des mécanismes partiels, non des AGI/ASI.
- L'hypothèse d'un alignement suffisamment résolu est explicitement qualifiée de lourde et non garantie.
- La section « Summary Instructions », activée par l'utilisateur, demande définitions, six avantages, quatre voies, tous les freins et interactions, agenda, actualisation et critiques.

### Informations externes

- Dépôt arXiv du 10 juin et fiche DeepMind du 12 juin 2026.
- Rapport international du 3 février 2026 : progrès rapides mais irréguliers, test-time scaling et écart d'évaluation.
- METR, 8 mai et 21 juillet : autonomie temporelle et optimisation à coût égal, avec limites explicites.
- Kim et al., 9 décembre 2025 : rendements multi-agents dépendants des tâches/topologies.
- DeepMind et partenaires, 11 juin 2026 : financement de sûreté multi-agents.
- Epoch AI, 3 septembre 2026 : révision des estimations de calcul Google.

### Opinions des auteurs

- L'AGI serait devenue un objectif concret de la prochaine décennie pour de grandes organisations.
- Si l'AGI est atteignable, un arrêt exactement au niveau humain paraît peu plausible.
- Une accélération persistante ne peut être exclue ; préparation mondiale et interdisciplinaire nécessaire.
- Mesure et prévision devraient devenir une discipline institutionnelle importante.
- AIXI est le cadre théorique le mieux compris pour une limite de l'intelligence générale.

### Interprétations et inférences

- **[Analyse]** Les voies sont les composants d'un même système : scaling fournit les ressources, algorithmes l'efficacité, récursion le feedback, collectifs le parallélisme.
- **[Analyse]** Les données soutiennent surtout un progrès pré-AGI par composition, pas le passage AGI→ASI.
- **[Analyse]** Passer de « copiable/rapide » à « fiable/autonome/productif » exige plusieurs démonstrations distinctes.
- **[Analyse]** La gouvernance est contrainte, mécanisme de direction et produit de la concentration, pas seulement un frein externe.
- **[Analyse]** Cinq jours après la v2, le résultat honnête est une ligne de base datée, non un verdict.

## Limites, critiques et points à vérifier

### Limites reconnues par le rapport

- Travail prospectif, listes incomplètes, incertitude extrême, pas de calendrier.
- Définitions informelles sans test complet.
- AIXI incomputable et éloigné de l'ingénierie.
- ≈10×/an obtenu par combinaison de grandeurs incertaines ; extrapolation fragile.
- Pas de lois empiriques établies pour récursion ou collectifs.
- Barrière de l'abstraction hypothétique.
- Conséquences sociales largement hors champ et alignement supposé suffisamment résolu.

### Critiques et réserves externes

Il est trop tôt pour identifier des lacunes **largement acceptées propres au rapport** : deux mois et demi depuis le dépôt initial, cinq jours depuis la v2, et aucune littérature de consensus dédiée trouvée. Les réserves suivantes sont attribuées.

- **[Externe — consensus plus large]** L'*International AI Safety Report 2026* souligne capacités irrégulières et écart benchmark–réel, ce qui fragilise un seuil AGI agrégé et toute projection benchmark→productivité.
- **[Externe — résultat empirique]** Kim et al. montrent que les collectifs peuvent dégrader les tâches séquentielles et amplifier les erreurs : la réplication doit être conditionnée par décomposabilité et corrélation des échecs.
- **[Externe — réserve méthodologique]** METR avertit que tâches jouets, déclarations de productivité et succès sélectionnés ne mesurent pas l'accélération de la R&D frontière.
- **[Externe — critique non consensuelle]** Soto², *The Blind Spot of DeepMind's ASI Report* (1er juillet 2026), reproche au rapport de sous-traiter la position de DeepMind, la concentration du calcul, le caractère endogène de la gouvernance et l'interaction entre trajectoires.

### Omissions ou angles morts déduits

- **[Analyse] Mesure :** choix des tâches, outils, temps et coûts changent les seuils AGI/ASI.
- **[Analyse] Capacité→impact :** adoption, intégration, confiance, responsabilité et institutions déterminent la productivité.
- **[Analyse] Concentration :** contrôle des puces, centres, données et plateformes peut empêcher la réplication supposée.
- **[Analyse] Cybersécurité :** agents massifs augmentent surface d'attaque, compromission d'outils et risques systémiques.
- **[Analyse] Économie politique :** distribution du pouvoir, revenus et accès au calcul est peu analysée.
- **[Analyse] Objectifs multiples :** conflits entre agents, organisations, États et humains peuvent empêcher une agence collective cohérente.
- **[Analyse] Ruptures :** « paradigme imprévisible » est une catégorie peu falsifiable.
- **[Analyse] Double comptage :** efficacité, R&D automatisée et calcul peuvent refléter des causes liées ; leur multiplication peut surestimer le calcul effectif.
- **[Analyse] Position institutionnelle :** l'affiliation à un laboratoire frontière n'invalide pas l'étude, mais impose triangulation et transparence.

### Points à vérifier dans le temps

- Part de R&D réellement automatisée et taux d'intervention humaine.
- Multi-agents sous budget fixe sur tâches longues, séquentielles et réelles.
- Qualité marginale des données après plusieurs cycles génération–vérification–distillation.
- Coût complet : calcul, énergie, mémoire, réseau, eau, construction, délais et amortissement.
- Tests distinguant recombinaison et création de concepts depuis des données sensorielles.
- Validité externe des horizons METR.
- Effets réels des règles, incidents et dynamiques internationales sur le rythme.

## Sources et références

### Document analysé

- Genewein et al., *From AGI to ASI*, **10 juin 2026**, v2 **30 août 2026** : <https://arxiv.org/abs/2606.12683>.
- Google DeepMind, fiche du **12 juin 2026** : <https://deepmind.google/research/publications/239142/>.

### Sources externes consultées

- *International AI Safety Report 2026*, **3 février 2026** : <https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026>.
- METR, *Task-Completion Time Horizons*, mise à jour **8 mai 2026** : <https://metr.org/time-horizons/>.
- Google DeepMind et partenaires, *Investing in multi-agent AI safety research*, **11 juin 2026** : <https://deepmind.google/blog/investing-in-multi-agent-ai-safety-research/>.
- METR, *Expenditure Horizon*, **21 juillet 2026** : <https://metr.org/blog/2026-07-21-expenditure-horizon/>.
- Kim et al., *Towards a Science of Scaling Agent Systems*, **9 décembre 2025** : <https://arxiv.org/abs/2512.08296>.
- Epoch AI, *AI Data Centers Updates*, révision du **3 septembre 2026** : <https://epoch.ai/data/ai-data-centers/updates>.
- Soto², *The Blind Spot of DeepMind's ASI Report*, **1er juillet 2026** : <https://scybernethics.org/the-blind-spot-of-deepminds-asi-report/>.

### Références structurantes mentionnées dans le rapport

- **Fondements :** Turing, Wiener, Good, Solomonoff, Legg, Hutter, AIXI, Bostrom, Chalmers, Russell.
- **Mesure/prévision :** Epoch AI, GATE, METR, Aschenbrenner, Davidson et al., Ho et al., Kaplan et al., Bloom et al., rapports internationaux de sûreté.
- **Systèmes :** transformers, Chinchilla, MoE, Mamba, S4, AlphaGo/Zero/Star, Adaptive Agent, FunSearch, AlphaEvolve, AI Scientists.
- **Évaluations :** ImageNet, GPQA, SWE-bench, FrontierMath, SuperARC, Dynabench, setter–solver et multi-agents.
- **Gouvernance/économie :** règlement UE 2024/1689, EO 14110, Déclaration de Bletchley, Acemoglu–Restrepo, Agrawal–Brynjolfsson–Korinek, Narayanan–Kapoor.

Cette sélection ne remplace pas la bibliographie complète.

## Cinq éléments essentiels à retenir

1. **[Rapport]** AGI = environ humain médian sur un large ensemble ; ASI = supérieure à de grands collectifs sur presque tous les domaines : seuils informels.
2. **[Rapport]** Scaling, paradigmes, récursion et collectifs sont quatre voies parallèles et cumulables.
3. **[Rapport/Analyse]** Les six avantages numériques rendent un dépassement plausible, mais copie et vitesse ne garantissent ni fiabilité, autonomie, coordination ou productivité.
4. **[Externe]** Les progrès observés portent sur inférence, autonomie limitée, optimisation assistée et multi-agents ; aucun ne prouve AGI, ASI ou récursion soutenue.
5. **[Analyse]** Ressources, données et coordination sont aujourd'hui les freins les plus tangibles ; suffisance du paradigme et abstraction restent indéterminées, et le recul sur la v2 est trop court pour un verdict.
