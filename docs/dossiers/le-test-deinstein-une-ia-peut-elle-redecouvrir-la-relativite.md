---
title: "Le test d’Einstein : une IA peut-elle redécouvrir la relativité ?"
date: 2026-10-10
kind: dossier
themes:
- ia
slug: le-test-deinstein-une-ia-peut-elle-redecouvrir-la-relativite
tags:
- test d'Einstein
- AGI
- LLM historiques
- découverte scientifique
- abduction
- évaluation
---
# Le test d’Einstein : une IA peut-elle redécouvrir la relativité ?

Date de rédaction : 2026-10-10

## Sources de synthèse

- **[S1]** Michael Hla, [*Machina Mirabilis*](https://michaelhla.com/blog/machina-mirabilis.html), billet-rapport, mars 2026.
- **[S2]** Michael Hla, [dépôt GitHub `gpt1900`](https://github.com/michaelhla/gpt1900) : prompts d’évaluation, générations, registre des points de contrôle et rapport technique archivé du 5 octobre 2026 (`docs/gpt1900.pdf`) ; fiches des modèles et jeux de données liés sur [Hugging Face](https://huggingface.co/collections/mhla/gpt-1900).
- **[S3]** Philip Ball, [« The Einstein test: what happens when AI tries to rediscover relativity? »](https://www.nature.com/articles/d41586-026-02804-x), *Nature* 657, 338-340, 9 septembre 2026, corrigé le 14 septembre.
- **[S4]** OfficeChai, [compte rendu de l’intervention de Demis Hassabis à l’India AI Summit](https://officechai.com/ai/a-test-of-agi-could-be-if-a-system-trained-till-1911-data-could-discover-general-relativity-google-deepmind-ceo-demis-hassabis/), 20 février 2026.
- **[S5]** Crypto Briefing, [« DeepMind’s Hassabis proposes Einstein test »](https://cryptobriefing.com/deepmind-hassabis-agi-einstein-test/), 14 juin 2026.
- **[S6]** Owain Evans, [*Vintage Large Language Models*](https://owainevans.github.io/talk-transcript.html), transcription d’un exposé, décembre 2024.
- **[S7]** OfficeChai, [synthèse de l’expérience de Hla](https://officechai.com/ai/someone-built-an-llm-to-test-out-demis-hassabis-agi-definition-of-pre-1900-science-discovering-relativity/), 3 avril 2026.
- **[S8]** D. Benrimoh, D. Harel, N. Mikus, P. Stone et A. Rosenfeld, [« The Einstein Test: A Test of AI’s Ability to Generate Transformative Science »](https://cacm.acm.org/opinion/the-einstein-test-a-test-of-ais-ability-to-generate-transformative-science/), *Communications of the ACM* 69(5), p. 49-50, en ligne le 2 avril 2026.
- **[S9]** Tom Zahavy, [« Position: LLMs can’t jump »](https://icml.cc/virtual/2026/poster/67091), papier de position présenté à ICML 2026 (poster du 9 juillet 2026) ; version déposée sur PhilSci-Archive le 27 janvier 2026.
- **[A1]** [`analyses/from-agi-to-asi.md`](../analyses/from-agi-to-asi.md), analyse interne du rapport de Google DeepMind, pour la « barrière de l’abstraction ».

**Périmètre.** Ce dossier part d’un corpus de huit liens transmis par l’utilisateur, complété par le papier de Zahavy, souvent cité mais non lié dans ce corpus. Les sources ont été lues directement le 10 octobre 2026 : l’article de *Nature* jusqu’à la limite de son accès libre, qui coupe la fin du texte, et le dépôt de Hla jusqu’aux fichiers de résultats. La section finale « État de l’art et regards extérieurs » ajoute des recherches complémentaires, chacune liée et datée.

**Convention.** Les identifiants [S1] à [S9] renvoient aux sources ci-dessus. *Inférence du dossier* signale un rapprochement ou une conclusion qui n’est pas attribuable aux auteurs.

## Repères pour comprendre le dossier

Le corpus mêle trois choses qu’il faut séparer pour le lire correctement. La première est une **idée de test** : entraîner une IA sur le savoir disponible avant une grande découverte, puis voir si elle la refait. Demis Hassabis l’a popularisée, mais d’autres l’ont formulée en même temps, et la formulation varie selon les interventions. La deuxième est une **expérience** : celle de Michael Hla, chercheur indépendant, qui a réellement entraîné un petit modèle sur des textes antérieurs à 1900 et l’a interrogé sur quatre problèmes de physique. La troisième est un **débat théorique** : les modèles de langage peuvent-ils produire le « saut » conceptuel d’un Einstein, ou seulement recombiner l’existant ? Le test sert d’horizon, l’expérience de banc d’essai, le débat de grille de lecture. Il faut aussi garder en tête la physique en jeu : la relativité restreinte (1905), la relativité générale (1915) et les débuts de la théorie quantique (1900-1905) ne posent pas le même degré de difficulté, et la date de coupure choisie change entièrement ce qui reste à découvrir.

- **Test d’Einstein** — Protocole d’évaluation proposé pour mesurer si une IA peut produire une découverte scientifique transformatrice : on la prive de tout savoir postérieur à une date, puis on vérifie si elle reconstruit la percée historique. Le nom est employé par Hassabis, par Benrimoh et al. [S8] et par *Nature* [S3], avec des contenus différents.
- **LLM historique ou « vintage »** — Modèle de langage entraîné à partir de zéro sur des textes publiés avant une date donnée. Le terme vient de l’exposé d’Owain Evans [S6] ; on parle aussi de modèle « verrouillé dans le temps » (*time-locked*).
- **Date de coupure (*cutoff*)** — Limite au-delà de laquelle aucun texte n’entre dans les données d’entraînement. Elle est nominale : les métadonnées de date sont souvent fausses ou absentes.
- **Fuite temporelle (contamination)** — Présence, dans les données ou la supervision, d’informations postérieures à la coupure : préface moderne d’un livre ancien, note de bas de page, ou connaissances apportées par un modèle moderne utilisé pendant l’entraînement.
- **Pré-entraînement, mi-entraînement, affinage supervisé (SFT)** — Les étapes successives de la fabrication d’un modèle : apprentissage généraliste sur un grand corpus, spécialisation sur un corpus ciblé (ici des traités de physique), puis apprentissage à répondre à des consignes à partir de paires question-réponse.
- **Apprentissage par renforcement avec juge LLM** — Le modèle est récompensé selon la note qu’un autre modèle de langage, plus puissant, attribue à ses réponses. Chez Hla, ce juge est un modèle moderne (Claude Sonnet 4), ce qui pose directement la question de la fuite.
- **Piratage de la récompense (*reward hacking*)** — Stratégie par laquelle un modèle maximise sa note sans accomplir la tâche visée, par exemple en énumérant toutes les conclusions possibles pour être sûr de citer la bonne.
- **Induction, déduction, abduction** — Trois formes de raisonnement distinguées par le philosophe C. S. Peirce : généraliser à partir de cas, tirer des conséquences de règles posées, inventer une hypothèse explicative pour un fait surprenant. Zahavy situe le « saut » d’Einstein dans l’abduction [S9].
- **Catastrophe ultraviolette** — Prédiction de la physique classique selon laquelle un corps chaud rayonnerait une énergie infinie aux hautes fréquences ; Planck la lève en 1900 en supposant que l’énergie s’échange par paquets.
- **Effet photoélectrique** — Émission d’électrons par un métal éclairé ; son seuil en fréquence, inexplicable par une onde continue, conduit Einstein en 1905 à l’hypothèse des quanta de lumière.
- **Principe d’équivalence** — Idée qu’un champ de gravitation et une accélération sont localement indiscernables ; Einstein la formule en 1907 et en fait la porte d’entrée de la relativité générale.
- **Changement de paradigme** — Notion de Thomas Kuhn désignant un bouleversement du cadre dans lequel une discipline pose ses questions, par opposition à la « science normale » qui résout des problèmes à l’intérieur du cadre.

## Résumé exécutif

En février 2026, à l’India AI Summit de New Delhi, Demis Hassabis a proposé de juger l’intelligence artificielle générale à un critère simple à énoncer : entraîner un système sur le savoir disponible en 1911 et voir s’il retrouve la relativité générale, comme Einstein en 1915 [S3, S4]. L’idée n’était ni nouvelle ni isolée. Owain Evans avait décrit dès décembre 2024 les usages possibles de modèles entraînés sur des données anciennes [S6] ; une tribune de *Communications of the ACM* proposait au même moment un protocole complet sous le même nom [S8] ; et un chercheur de Google DeepMind, Tom Zahavy, expliquait en janvier pourquoi, selon lui, les modèles de langage actuels échoueraient [S9].

Un mois après Hassabis, Michael Hla a tenté l’expérience avec les moyens d’un particulier : un modèle de 3,3 milliards de paramètres, environ 22 milliards de tokens de textes antérieurs à 1900, une spécialisation sur 2 600 traités de physique, puis un affinage et un renforcement guidés par des modèles modernes [S1]. Sur huit questions posées sous forme d’observations et d’hypothèses classiques à réfuter, le modèle produit quelques réponses frappantes, comme une lumière qui se « brise » en impulsions distinctes pour l’effet photoélectrique. Mais ses notes moyennes restent proches de 1,25 sur 5, ses meilleures réponses proviennent de points de contrôle différents, et Hla lui-même conclut à une imitation plausible plutôt qu’à une intuition physique [S1, S2]. La documentation de ses modèles révèle en outre que la spécialisation en physique du meilleur d’entre eux a été étendue à des textes allant jusqu’en 1905, dont Planck et Lorentz, ce que le billet ne dit pas [S2].

La lecture croisée du corpus fait apparaître que le test d’Einstein est aujourd’hui **plus utile comme programme de recherche que comme critère d’AGI**. Les obstacles pratiques sont massifs : données anciennes rares et bruitées, fuites temporelles difficiles à éliminer, supervision moderne presque inévitable, et surtout des énoncés de test qui, rédigés avec le recul, mâchent une partie du travail de découverte. Les autres modèles historiques sortis en 2026 (Talkie, Ranke-4B, TypewriterLM, Bart) confirment ces difficultés plus qu’ils ne les résolvent [S3].

Pour la veille, le sujet compte à deux titres. Il fournit un vocabulaire et un protocole pour évaluer les annonces de « découverte » par l’IA, qui se multiplient en 2026. Il ouvre aussi un champ nouveau, celui des modèles historiques, dont les usages en prévision, en histoire et en évaluation dépassent largement la seule question d’Einstein.

## Chronologie

L’histoire du test d’Einstein se lit sur deux échelles : celle de la physique de 1887 à 1919, qui fixe ce qu’une IA aurait à redécouvrir, et celle du débat sur l’IA de 2024 à 2026.

**La physique en jeu**

- **1887** — L’expérience de Michelson et Morley ne détecte aucun mouvement de la Terre par rapport à l’éther supposé porter la lumière.
- **1894** — Michelson laisse entendre que les grandes lois de la physique sont connues et que les progrès se joueront dans les décimales ; Hla ouvre son récit sur ce discours [S1].
- **Décembre 1900** — Planck introduit l’hypothèse des quanta d’énergie pour expliquer le rayonnement du corps noir.
- **1905** — « Année miraculeuse » d’Einstein : quanta de lumière et effet photoélectrique, relativité restreinte, équivalence masse-énergie.
- **1907** — Einstein formule le principe d’équivalence, sa « pensée la plus heureuse » : un observateur en chute libre ne sent pas son poids.
- **1911** — À Prague, Einstein prédit que la gravitation dévie la lumière, avec une valeur de 0,83 seconde d’arc, moitié de la valeur correcte.
- **1912-1913** — Avec le mathématicien Marcel Grossmann, Einstein adopte la géométrie riemannienne ; première théorie, dite *Entwurf*, encore fautive.
- **Novembre 1915** — Équations du champ de la relativité générale ; explication de l’avance du périhélie de Mercure.
- **1919** — L’éclipse observée par Eddington confirme la déviation de la lumière prédite en 1915.

**Le débat sur l’IA**

- **Décembre 2024** — Owain Evans (Truthful AI, Berkeley) présente les « vintage LLMs » et leurs usages, dont la redécouverte scientifique [S3, S6].
- **Avril 2025** — Dans *Time*, Hassabis évoque un test : retrouver la relativité générale avec les seules informations dont disposait Einstein.
- **Septembre 2025** — À l’All-In Summit, Hassabis formule une variante : coupure en 1901, cible la relativité restreinte.
- **14 décembre 2025** — L’Université de Zurich annonce Ranke-4B, famille de modèles historiques (coupures de 1913 à 1946).
- **27 janvier 2026** — Tom Zahavy dépose « LLMs can’t jump » [S9].
- **Février 2026** — India AI Summit : Hassabis propose la version 1911-relativité générale [S3, S4].
- **Mars 2026** — Michael Hla publie *Machina Mirabilis* et le modèle GPT-1900 [S1, S2].
- **2 avril 2026** — Tribune de Benrimoh et al. dans *Communications of the ACM* [S8].
- **27 avril 2026** — Sortie de Talkie-1930, modèle de 13 milliards de paramètres (Radford, Levine, Duvenaud).
- **9 juillet 2026** — Présentation de la position de Zahavy à ICML 2026 [S9].
- **30 juillet 2026** — Prépublication de Shalyt, Regev, Soljačić et Kaminer, « Can AI follow in Einstein’s footsteps? » [S3].
- **9 septembre 2026** — Article de Philip Ball dans *Nature*, qui donne au sujet sa visibilité scientifique [S3].
- **5 octobre 2026** — Hla prépare une édition archivée de son rapport technique, sans relecture par les pairs ni DOI à cette date [S2].

## Thèse principale

Le corpus converge vers un constat sobre : aucun système n’a passé le test d’Einstein, et la seule tentative publique, modeste par construction, montre surtout ce qui rend ce test difficile à réaliser honnêtement. La question qu’il pose reste pourtant féconde, parce qu’elle oblige à distinguer ce que l’IA sait déjà faire en science (prédire, optimiser, démontrer à l’intérieur d’un cadre) de ce qu’elle ne fait pas encore (inventer le cadre).

Ce dossier défend une lecture en trois temps. Le test est d’abord un **critère philosophiquement solide mais opérationnellement fragile** : tout dépend de la date de coupure, de la propreté du corpus et de la façon dont on pose la question. L’expérience de Hla est ensuite un **résultat négatif instructif**, plus probant sur les obstacles que sur les capacités. Enfin, le débat sur l’abduction déplace la question : le goulet n’est peut-être pas de produire une bonne idée parmi d’autres, mais de **savoir laquelle retenir** et de la rendre vérifiable.

## Informations et arguments importants

### Un test, plusieurs formulations

Le « test d’Einstein » n’a pas d’énoncé canonique. Chaque source le formule à sa manière, et ces écarts ne sont pas de détail : ils changent la difficulté de l’épreuve et ce qu’un succès prouverait.

- **La version de Hassabis.** À New Delhi, Hassabis parle d’entraîner un système avec une coupure « en 1911, par exemple » et de voir s’il produit la relativité générale ; il y voit le vrai test d’une AGI complète, hors de portée des systèmes actuels mais possible dans quelques années [S4]. Le contexte est sa critique d’une intelligence « en dents de scie » (*jagged*) : des modèles capables d’une médaille d’or aux Olympiades de mathématiques mais fragiles sur des problèmes plus simples reformulés [S4]. Crypto Briefing reprend en juin la même idée en mentionnant des coupures en 1901 ou en 1911 et des estimations d’AGI vers 2030 [S5]. Ces variations reflètent des interventions successives, pas une erreur de transcription (voir la vérification plus bas).
- **Le protocole de *Communications of the ACM*.** Benrimoh, Harel, Mikus, Stone et Rosenfeld proposent un test structuré [S8]. Un comité d’experts choisit une percée que l’équipe candidate ne connaît pas ; le système reçoit un corpus soigneusement purgé de tout savoir postérieur ; on lui pose les problèmes ouverts de l’époque sans « main qui guide », c’est-à-dire sans souligner les indices dont on sait aujourd’hui qu’ils étaient décisifs ; une équipe d’experts joue le rôle d’assistant de recherche et fournit les résultats des expériences demandées, si elles étaient réalisables à l’époque ; la réponse finale est vérifiée formellement. Les auteurs ajoutent une version prospective : un système qui aurait réussi le test rétrospectif serait mis au défi de produire une percée nouvelle. Ils reconnaissent que la purge du corpus est le point le plus difficile.
- **La version théorique de Zahavy.** Pour Zahavy, la relativité générale est le cas d’école d’une découverte faite avec très peu de données : ce qui compte n’est pas de dériver les équations à partir du principe d’équivalence, mais d’inventer ce principe [S9]. Son test implicite porte donc sur l’abduction, pas sur la capacité de calcul.

*Inférence du dossier :* ces trois versions ne mesurent pas la même chose. La version de Hassabis teste une connaissance générale ; celle de *CACM* teste une démarche de recherche complète, avec choix des expériences ; celle de Zahavy teste un seul moment, le saut vers un nouveau principe. Une expérience comme celle de Hla, qui fournit au modèle les observations et parfois le principe, ne relève d’aucune des trois au sens strict.

### *Machina Mirabilis* : l’expérience de Michael Hla

Hla présente son projet comme une tentative de mettre la proposition de Hassabis à l’épreuve, avec un objectif volontairement modeste : il s’attend à un échec sur la plupart des tâches, mais espère quelques signes d’intuition, par exemple l’idée que la lumière transporte l’énergie par quantités discrètes [S1]. Le projet a duré environ un mois, avec un budget individuel dont le montant n’est pas donné.

**Les données.** Le corpus de pré-entraînement provient de trois jeux de données publics hébergés sur Hugging Face : *Institutional Books* (livres numérisés de la bibliothèque de Harvard), les livres de la British Library et les journaux américains *American Stories*. Après filtrage, il reste environ **22 milliards de tokens** [S1]. Le filtrage est délibérément agressif : tri par année déclarée et par qualité de reconnaissance optique (OCR), suppression de tout document mentionnant Einstein, la relativité ou la mécanique quantique, retrait des préfaces et notes modernes, et filtre statistique sur la probabilité moyenne des tokens pour écarter le bruit d’OCR et les textes répétitifs. Hla signale lui-même une alerte : la préface d’un traducteur de Boltzmann citait Einstein et la relativité, ce qu’il a jugé sans conséquence [S1].

**Le modèle et son entraînement.** Le modèle est un transformeur de **3,3 milliards de paramètres**, construit à partir de *nanochat*, le code d’entraînement minimaliste d’Andrej Karpathy [S1]. Quatre étapes se succèdent :

1. **Pré-entraînement** sur le corpus historique. Sur l’indicateur CORE, moyenne de tests de compréhension courants, le modèle obtient 0,140 avec une coupure en 1900, contre 0,260 pour le même code entraîné sur des données web modernes (FineWeb-Edu) ; il reste en dessous de GPT-2 [S1].
2. **Mi-entraînement** sur environ **290 millions de tokens** tirés de plus de 2 600 ouvrages et revues de physique antérieurs à 1900 (Maxwell, Newton, Faraday…), issus du projet Gutenberg, de Wikisource et d’Internet Archive [S1]. Hla y voit la dernière étape exempte d’influence moderne. La documentation publiée avec les modèles nuance cette borne : le registre des points de contrôle fait passer la version v11 par un mi-entraînement « étendu » (`physicssft-expanded`), et la fiche Hugging Face du jeu de données de physique indique qu’il a été élargi à une coupure en 1905, avec Planck (1901) et Lorentz (1904) [S2]. Ce point est discuté dans les limites.
3. **Affinage sur consignes** avec environ **53 000 paires** (30 millions de tokens), générées par un modèle moderne à partir d’extraits du corpus, puis filtrées pour écarter les formulations tournées vers l’avenir [S1].
4. **Renforcement « par contradiction »** : un modèle moderne extrait d’un extrait de physique une idée, la reformule en contradiction à résoudre, et Claude Sonnet 4 note la réponse sur la forme, la cohérence et la justesse [S1]. Pour la version v11, le registre indique 284 problèmes et 24 passes [S2].

Hla documente honnêtement ses échecs de méthode : échantillonnage « par puissance » qui tourne en boucle, renforcement par auto-certitude qui s’effondre, renforcement sur des exercices de mathématiques ou de physique vérifiables qui ne transfère pas [S1].

**L’évaluation.** Huit questions couvrent quatre problèmes : la catastrophe ultraviolette, l’effet photoélectrique, la relativité restreinte (poursuivre un rayon lumineux, approcher la vitesse de la lumière, simultanéité du train et des éclairs, Michelson-Morley) et la relativité générale (lumière dans un ascenseur accéléré, équivalence de la chute libre) [S2]. Chaque question donne des observations, puis souvent une liste d’hypothèses classiques ; le modèle doit dire laquelle est fausse et pourquoi. Dans le billet, Hla qualifie ses évaluations d’impressionnistes (*vibes based*) [S1]. Le dépôt contient pourtant une notation : un juge Claude Sonnet 4 attribue une note de 0 à 5 selon une grille propre à chaque tâche [S2]. Le rapport archivé reproduit quelques lignes de ces résultats :

| Point de contrôle v11 | Effet photoélectrique | Ascenseur et lumière | Moyenne sur 8 tâches |
|---|---|---|---|
| Étape 560 | 2 / 5 | 2 / 5 | 1,25 / 5 |
| Étape 630 | 3 / 5 | 3 / 5 | 1,25 / 5 |
| Étape 735 | 2 / 5 | 2 / 5 | 1,25 / 5 |
| Étape 770 | 4 / 5 | 1 / 5 | 1,125 / 5 |

*Source : rapport technique archivé, tableau 2, un échantillon par tâche et par point de contrôle [S2].*

**Les résultats.** La meilleure réponse sur l’effet photoélectrique (4/5) rejette l’idée d’une onde continue et décrit une lumière qui se divise en impulsions distinctes, chacune livrant une quantité d’énergie définie, sans délai, selon la fréquence [S2]. Sur l’ascenseur, le modèle conclut à l’équivalence de l’accélération et de la gravitation, mais l’explique par une tension dans un milieu, raisonnement qui rappelle l’éther du XIXe siècle plus que la courbure de l’espace-temps [S1, S2]. Reformuler les questions ou retirer les hypothèses classiques ne change guère les conclusions [S1]. Le rapport archivé précise toutefois que la variante sans hypothèses (moyennes de 1,04 à 1,58 selon le point de contrôle, sur trois échantillons par tâche) n’est pas une comparaison contrôlée [S2].

**Les échecs.** Le dépôt réunit une « galerie des échecs » : analogies avec les machines à vapeur, les rivières ou la roue d’une calèche, glissements vers la métaphysique de l’âme, formules répétées à l’identique, et piratage de la récompense, le modèle énumérant toutes les conclusions possibles pour satisfaire le juge [S1, S2]. Hla note aussi que des traces de raisonnement distillées d’un autre modèle avaient l’air plausibles mais récitaient des absurdités [S1].

**La conclusion de l’auteur.** Hla juge l’explication la plus probable peu flatteuse : le modèle produit des mots plausibles sans représentation interne du monde à partir de laquelle raisonner [S1, S3]. Il refuse cependant d’en conclure que l’approche des modèles de langage est condamnée : taille, données et méthode sont des facteurs de confusion, et un modèle de pointe entraîné sous les mêmes contraintes pourrait faire beaucoup mieux [S1]. Son essai final distingue une intelligence « d’exécution », celle des modèles actuels, d’une intelligence d’introspection et de goût, et plaide pour le duo humain-machine [S1].

### Les autres modèles historiques de 2026

L’expérience de Hla s’inscrit dans une vague. *Nature* mentionne plusieurs équipes ayant construit des modèles « vintage » cette année, avec un constat commun : ces premiers essais révèlent davantage les limites de l’IA actuelle que ses forces [S3]. La liste communautaire *awesome-vintage-llms* recense les principaux :

| Modèle | Coupure | Taille | Équipe | Particularité |
|---|---|---|---|---|
| [MonadGPT](https://huggingface.co/Pclanglais/MonadGPT) (2023) | XVe-XVIIe s. | 7 Md | P.-C. Langlais | Affinage d’un modèle moderne, pas un entraînement à zéro |
| [TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM) | Londres 1800-1875 | jusqu’à 1,2 Md | H. Grigorian | Précurseur remercié par Hla |
| [Ranke-4B](https://github.com/DGoettlich/history-llms) | 1913 à 1946 | 4 Md | Univ. de Zurich et de Cologne | Coupures historiques ; publication annoncée, encore partielle |
| [GPT-1900](https://huggingface.co/collections/mhla/gpt-1900) | 1900 | 3,3 Md | M. Hla | Seul modèle dédié au test d’Einstein |
| [Talkie-1930](https://talkie-lm.com/introducing-talkie) | 1930 | 13 Md | A. Radford, N. Levine, D. Duvenaud | 260 Md de tokens ; « jumeau » moderne pour comparer |
| [TypewriterLM](https://arxiv.org/abs/2606.02991) | 1913 | 7,24 Md | X. Luo et al. | Article accepté à EMNLP 2026 ; banc d’essai HISTORY-EVENT |
| [Bartholomew (Bart)](https://unboundedlab.com/blog/bart) | 1930 | 2,82 Md | Unbounded Labs | Environ 800 $ de calcul ; reprend le filtre de Hla |

Deux enseignements ressortent de ces projets. Le premier est que **la fuite temporelle est la règle**. L’équipe de Talkie rapporte qu’une version de 7 milliards de paramètres connaissait la présidence de Roosevelt et le New Deal, et que le modèle de 13 milliards évoque encore la Seconde Guerre mondiale et l’ONU ; Nick Levine résume dans *Nature* qu’interrogé sur les années 1950, le modèle répond souvent « par accident » [S3]. Le second est que **les données anciennes coûtent cher en qualité** : Talkie estime qu’un texte issu d’OCR classique n’apporte qu’environ 30 % de l’efficacité d’apprentissage d’une transcription humaine. Ranke-4B résume l’ambition réaliste du domaine par une formule de Daniel Göttlich : chercher non le génie, mais des « étincelles de génie » [S3].

### Le saut, l’abduction et le tri des idées

Le cœur théorique du corpus est le papier de Zahavy [S9], que *Nature* présente comme la description la plus détaillée du test [S3]. Zahavy part du schéma de la découverte qu’Einstein décrivait à son ami Maurice Solovine : de l’expérience sensible, un saut intuitif mène aux axiomes, d’où l’on déduit des conséquences testables. Selon lui, l’IA générative maîtrise l’induction, progresse vite en déduction, mais n’a pas de mécanisme pour l’abduction créatrice, celle qui invente une cause pour un phénomène singulier. La relativité générale illustre le problème : peu de données, pas de signal d’erreur clair (l’anomalie de Mercure était attribuée à une planète hypothétique, Vulcain), et un principe tiré d’une expérience de pensée incarnée, la chute libre. Zahavy propose comme remède des modèles du monde physiquement cohérents et multimodaux, dans lesquels un agent pourrait mener des expériences simulées.

*Nature* élargit le débat avec trois voix [S3]. Sendhil Mullainathan (MIT) rappelle une expérience de 2025 : un modèle entraîné sur des orbites planétaires simulées n’a jamais retrouvé la loi de la gravitation de Newton, mais une loi différente, et fausse, pour chaque système. Ido Kaminer (Technion) juge une percée de type relativité accessible à l’IA, à condition de repenser certains principes de ses modèles. Jacob Andreas (MIT) déplace la question : rien n’empêche un modèle de produire la relativité générale parmi beaucoup de théories fausses ; la difficulté est de reconnaître la bonne, ce qu’on sait faire en mathématiques, où chaque étape se vérifie, mais pas en physique théorique.

*Inférence du dossier :* l’argument d’Andreas éclaire l’expérience de Hla. Le meilleur résultat sur l’effet photoélectrique vient d’un point de contrôle, celui sur l’ascenseur d’un autre ; choisir *a posteriori* la bonne réponse parmi les échantillons revient à confier au chercheur le tri que le test voulait attribuer à la machine. C’est aussi ce que l’analyse interne [*From AGI to ASI*](../analyses/from-agi-to-asi.md) appelle la « barrière de l’abstraction » : l’automatisation progresse dans les tâches vérifiables, beaucoup moins dans la formation de concepts nouveaux [A1].

## Convergences et divergences

Malgré leurs différences de nature (déclarations, expérience, tribune, papier de position, journalisme), les sources s’accordent sur trois points. Aucun système actuel ne passe le test, et Hassabis le dit lui-même [S4]. La propreté du corpus est la difficulté pratique centrale, que la tribune de *CACM* nomme explicitement [S8] et que l’expérience de Hla puis Talkie illustrent [S1, S3]. Enfin, réussir un test rétrospectif ne garantirait pas une capacité de découverte prospective, même si *CACM* y voit un indice [S8].

| Question | Positions | Lecture du dossier |
|---|---|---|
| Le test mesure-t-il l’AGI ? | Hassabis : oui, c’en serait la vraie preuve [S4]. *CACM* : il mesure la capacité de science transformatrice, plus étroite [S8]. Crypto Briefing oppose ce seuil aux définitions économiques de l’AGI, plus basses [S5]. | Le test vise une capacité rare, même chez l’humain ; en faire le critère de l’AGI place la barre au niveau d’Einstein, pas de l’humain ordinaire. |
| Les LLM peuvent-ils faire le saut ? | Zahavy : non, faute d’abduction ancrée dans l’expérience [S9]. Kaminer : oui, avec d’autres principes de conception [S3]. Andreas : la génération n’est pas l’obstacle, la sélection l’est [S3]. Hla : la question reste ouverte à plus grande échelle [S1]. | Désaccord réel sur le mécanisme manquant ; il ne pourra être tranché que par une expérience à grande échelle et proprement contrôlée. |
| Que prouve GPT-1900 ? | Hla : quelques signes, pas d’intuition robuste [S1]. OfficeChai : des réponses proches de Planck et d’Einstein, mais une imitation plausible [S7]. *Nature* : échec dans la plupart des cas, malgré des « coups de pouce » [S3]. | Accord sur l’essentiel ; les comptes rendus de presse mettent davantage en avant les réussites que les moyennes. |
| Faut-il fournir les observations ? | Hla les fournit, avec les hypothèses classiques à réfuter [S1]. *CACM* exige que la machine demande elle-même les expériences, sans indices rétrospectifs [S8]. | Différence de protocole décisive : l’expérience de Hla teste l’explication d’anomalies déjà isolées, pas leur découverte. |

## Points particulièrement intéressants pour la veille

- **Les annonces de « découverte » par l’IA.** Le corpus fournit une grille pour les lire : qui a choisi le problème, qui a fourni les données, combien d’essais ont été faits, qui a trié les résultats et comment ils ont été vérifiés. *Inférence pour la veille :* appliquer ces cinq questions aux communiqués de laboratoires, notamment lorsque *Nature* cite une réfutation d’une conjecture d’Erdős par un modèle d’OpenAI en mai 2026 comme une avancée conceptuelle réelle mais construite sur des idées existantes [S3].
- **L’émergence d’un champ des modèles historiques.** Sept modèles au moins existent, avec des équipes universitaires (Zurich et Cologne pour Ranke-4B, les auteurs de TypewriterLM), un ancien d’OpenAI (Alec Radford) et des indépendants. *Inférence pour la veille :* suivre la publication effective des données et des poids de Ranke-4B, la version de Talkie de niveau GPT-3 annoncée, et les premiers usages en histoire et en sciences sociales.
- **La prévision comme débouché.** Evans propose de tester des modèles arrêtés en 2019 sur les événements suivants [S6] ; Nick Levine envisage de poser à son modèle de 1930 des questions de marché prédictif [S3]. *Inférence pour la veille :* les modèles à coupure contrôlée deviennent un outil d’évaluation sans contamination, utile bien au-delà de la physique.
- **La supervision par des modèles modernes.** Hla, Talkie et sans doute Ranke-4B utilisent des modèles actuels pour affiner ou juger leurs modèles anciens. *Inférence pour la veille :* toute revendication de « pureté » temporelle doit préciser ce qui se passe après le pré-entraînement.
- **Le coût d’entrée très bas.** GPT-1900 tient dans un projet individuel d’un mois ; Bart revendique environ 800 dollars de calcul. *Inférence pour la veille :* les expériences de ce type vont se multiplier, avec une qualité très inégale ; la vérification des protocoles comptera plus que le nombre de modèles.

## Faits, opinions et interprétations

### Faits rapportés par les sources

Les faits les mieux établis concernent l’expérience de Hla, documentée par ses propres fichiers : un modèle de **3,3 milliards de paramètres**, environ **22 milliards de tokens** de textes antérieurs à 1900, 290 millions de tokens de physique, 53 000 paires d’instructions, un juge Claude Sonnet 4, huit questions et des notes moyennes autour de **1,25 sur 5** pour les meilleurs points de contrôle [S1, S2]. Le rapport archivé du 5 octobre 2026 n’a fait l’objet d’aucune relecture par les pairs et n’a pas de DOI [S2]. Les fiches Hugging Face du projet établissent par ailleurs que la chaîne du modèle v11 passe par des données de physique étendues à 1905 [S2]. La proposition de Hassabis à l’India AI Summit en février 2026, avec une coupure en 1911, est attestée par deux sources indépendantes [S3, S4]. La tribune de *CACM* est publiée dans le numéro de mai 2026, signée par cinq chercheurs dont David Harel et Peter Stone [S8].

### Opinions et positions des auteurs

Hassabis juge le test décisif pour l’AGI et hors de portée actuelle [S4]. Zahavy soutient que les modèles de langage ne peuvent pas faire le saut abductif et que des modèles du monde seraient nécessaires [S9]. Les auteurs de *CACM* présentent leur test comme un critère clair et falsifiable, préférable selon eux aux bancs d’essai comme ARC-AGI ou *Humanity’s Last Exam* [S8]. Hla, enfin, défend une position nuancée : son modèle « dit des mots », mais peu importe si ces mots font avancer les tâches ; il plaide pour le couple humain-machine [S1].

### Interprétations et inférences

L’interprétation la plus discutable du corpus est celle qui présente les réponses de GPT-1900 comme des « aperçus d’intuition » [S1, S3]. Une réponse notée 4/5 sur l’effet photoélectrique, choisie parmi des centaines, à partir d’un énoncé qui liste déjà le seuil en fréquence et l’absence de délai, est compatible avec une recombinaison habile des notions de vibration et de seuil présentes dans la physique de la fin du XIXe siècle, voire avec une reprise de Planck si les données étendues à 1905 ont bien servi. *Inférence du dossier :* le résultat le plus solide de l’expérience est négatif, et il porte autant sur la méthode que sur le modèle ; il montre qu’un test d’Einstein crédible exige une échelle, une propreté de données et un protocole d’évaluation qui dépassent de loin ce qu’un projet individuel peut réunir.

## Limites et points à vérifier

1. **Un corpus dominé par une seule expérience.** Hla est la seule tentative publique explicitement consacrée au test, et les articles d’OfficeChai et de *Nature* reprennent ses propres résultats [S3, S7]. Ces reprises ne constituent pas des confirmations indépendantes ; aucune réplication par une autre équipe n’est documentée.
2. **Une coupure de 1900 qui n’est peut-être pas celle du meilleur modèle.** Le billet décrit un mi-entraînement sur des textes antérieurs à 1900 [S1]. Or la fiche Hugging Face du jeu de données de physique (`mhla/gpt1900-physics-clm`) le dit « étendu à une coupure en 1905 », avec Planck 1901, Lorentz 1904 et Rutherford, et désigne le modèle v11 comme issu de ces données ; la fiche du modèle d’instructions parle aussi de textes de physique antérieurs à 1905 [S2]. Si c’est exact, le modèle qui « retrouve » des paquets d’énergie a lu l’hypothèse des quanta de Planck, et celui qui raisonne sur Michelson-Morley a lu les transformations de Lorentz. Ni le billet ni le rapport archivé ne lèvent cette contradiction ; elle suffit à suspendre toute lecture des meilleurs résultats comme redécouverte.
3. **Une supervision moderne qui brouille la frontière temporelle.** Les paires d’instructions sont produites par un modèle moderne, les problèmes de renforcement aussi, et le juge est Claude Sonnet 4 [S1, S2]. Le rapport archivé reconnaît que le savoir moderne peut entrer par les données et par la récompense ; aucune mesure n’en estime l’ampleur.
4. **Des énoncés qui contiennent une partie de la réponse.** La question de l’ascenseur affirme déjà que l’accélération et la gravitation sont localement équivalentes, c’est-à-dire l’intuition de 1907 qu’Einstein mit des années à exploiter [S2]. Le modèle doit en tirer la conséquence, pas l’inventer.
5. **Une sélection des meilleurs résultats.** Les réponses mises en avant proviennent de points de contrôle différents, à température élevée, avec un échantillon par tâche [S2]. Le rapport archivé prévient que retenir le maximum par tâche surestime la capacité de n’importe quel modèle pris isolément.
6. **Une évaluation par un seul juge automatique.** Les notes de 0 à 5 viennent de Claude Sonnet 4, sans validation par des physiciens ni vérification mathématique [S2]. Le juge peut récompenser une formulation proche de la réponse attendue sans mécanisme physique correct.
7. **Des chiffres de calcul non réconciliés.** Hla annonce un rapport de 11 tokens par paramètre, alors que 22 milliards de tokens pour 3,3 milliards de paramètres donnent environ 6,7 ; le rapport archivé laisse la question ouverte, ce qui laisse supposer plusieurs passes sur les données sans le préciser [S1, S2].
8. **Une question de fond non tranchée.** Ni l’échec de GPT-1900 ni le papier de Zahavy ne démontrent qu’un modèle de langage à grande échelle échouerait ; Hla le souligne lui-même [S1]. Le corpus ne permet de conclure ni dans un sens ni dans l’autre.

## Sources et références du corpus

Le corpus est déséquilibré mais complémentaire. Les sources primaires (le billet et le dépôt de Hla, la tribune de *CACM*, l’exposé d’Evans, le papier de Zahavy) portent l’essentiel du raisonnement ; les trois articles de presse en ligne (OfficeChai deux fois, Crypto Briefing) ne servent qu’à dater et situer les déclarations de Hassabis ; l’article de *Nature* joue un rôle de pivot, puisqu’il relie le test, l’expérience de Hla, les autres modèles historiques et le débat théorique, avec des citations de chercheurs absents du reste du corpus. Les références déterminantes citées par ces sources sont la vidéo et les diapositives de l’exposé d’Evans, les jeux de données *Institutional Books* et *American Stories*, le code *nanochat*, et les travaux de Vafa, Mullainathan et collègues sur les modèles du monde.

- **[S1] Hla, *Machina Mirabilis*** — Source primaire principale : méthode, résultats commentés, échecs et essai sur l’AGI. Mobilisée pour toute la description de l’expérience.
- **[S2] Dépôt `gpt1900` et rapport archivé** — Prompts, notes du juge, générations complètes, galerie d’échecs, et une relecture critique par l’auteur lui-même (5 octobre 2026). Mobilisé pour le tableau des notes et plusieurs limites.
- **[S3] Ball, *Nature*** — Mise en contexte la plus large : Evans, Zahavy, Mullainathan, Kaminer, Andreas, Talkie, Ranke-4B. Une correction du 14 septembre porte sur les détails de publication du papier de Zahavy.
- **[S4] OfficeChai, février 2026** — Seule source détaillée sur l’intervention de Hassabis à New Delhi.
- **[S5] Crypto Briefing, juin 2026** — Reprise tardive, utile pour les variantes de coupure et le contraste avec les définitions économiques de l’AGI ; non signée.
- **[S6] Evans, *Vintage Large Language Models*** — Texte fondateur du champ : usages (prévision, invention, histoire), obstacles (fuite, rareté des données, coût) et pistes (données synthétiques, fourches chronologiques).
- **[S7] OfficeChai, avril 2026** — Résumé fidèle de l’expérience de Hla, sans réaction extérieure.
- **[S8] Benrimoh et al., *CACM*** — Seul protocole complet du test, avec version rétrospective et prospective.
- **[S9] Zahavy, « LLMs can’t jump »** — Cadre théorique de l’abduction ; lu à travers sa présentation ICML et sa couverture par *Nature* et *The Decoder*.
- **[A1] [From AGI to ASI](../analyses/from-agi-to-asi.md)** — Analyse interne du rapport de Genewein et al. (Google DeepMind) ; mobilisée pour la « barrière de l’abstraction » et l’état de la R&D automatisée.

## Cinq éléments essentiels à retenir

1. Le **test d’Einstein** consiste à priver une IA de tout savoir postérieur à une date, puis à voir si elle reconstruit une grande découverte ; Hassabis l’a popularisé en février 2026, mais sa formulation varie et *CACM* en propose un protocole plus exigeant.
2. **GPT-1900**, seule tentative publique, est un modèle de 3,3 milliards de paramètres entraîné sur 22 milliards de tokens antérieurs à 1900 ; ses meilleures réponses évoquent les quanta de lumière ou l’équivalence, mais ses notes moyennes restent proches de 1,25 sur 5.
3. Les obstacles sont surtout **méthodologiques** : fuites temporelles (le meilleur modèle de Hla a vu des textes de physique jusqu’en 1905), supervision par des modèles modernes, énoncés qui contiennent une partie de la réponse et sélection des meilleurs échantillons.
4. Le débat théorique oppose ceux qui jugent l’**abduction** hors de portée des modèles de langage (Zahavy) et ceux qui placent le vrai goulet dans le **tri** des idées produites (Andreas).
5. Au-delà d’Einstein, les **modèles historiques** forment un champ nouveau (Talkie, Ranke-4B, TypewriterLM, Bart) dont les usages en prévision, en histoire et en évaluation sans contamination méritent d’être suivis.

## État de l’art et regards extérieurs

Recherches effectuées le 2026-10-10. Ces constats complètent le corpus sans modifier les sections précédentes.

### Travaux de référence

- **Langley, Simon, Bradshaw et Zytkow, *Scientific Discovery: Computational Explorations of the Creative Processes* (MIT Press, 1987).** Le programme BACON y « redécouvrait » la troisième loi de Kepler ou la loi d’Ohm à partir de données numériques. C’est le premier test d’Einstein avant la lettre, avec la même limite que celle relevée par Zahavy : les variables pertinentes étaient choisies par les chercheurs, et la machine cherchait une relation, pas un cadre.
- **Schmidt et Lipson, [« Distilling Free-Form Natural Laws from Experimental Data »](https://doi.org/10.1126/science.1165893), *Science*, 3 avril 2009, et Udrescu et Tegmark, [« AI Feynman »](https://doi.org/10.1126/sciadv.aay2631), *Science Advances*, 15 avril 2020.** La régression symbolique retrouve des lois physiques à partir de mesures. Ces travaux montrent ce que l’IA sait faire depuis longtemps, extraire une équation de données abondantes, et donc ce que le test d’Einstein cherche au-delà.
- **Vafa, Chang, Rambachan et Mullainathan, [« What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models »](https://arxiv.org/abs/2507.06952), ICML 2025.** C’est l’expérience citée par Mullainathan dans *Nature* : des modèles entraînés sur des trajectoires d’orbites prédisent bien mais n’adoptent pas la mécanique newtonienne lorsqu’on les adapte à de nouvelles tâches. Le travail donne une base empirique à l’idée qu’une bonne prédiction ne prouve pas un modèle du monde.
- **Thomas Kuhn, *La Structure des révolutions scientifiques* (1962).** Toute la discussion sur le « saut » repose sur sa distinction entre science normale et changement de paradigme. *Nature* la mobilise explicitement [S3].

### Compléments sur le sujet

Le corpus traite la relativité générale comme un bloc et la date de coupure comme un détail technique. L’histoire des sciences montre au contraire que le choix de la date fixe presque à lui seul la difficulté du test, et que l’IA produit déjà des résultats scientifiques réels, mais d’une autre nature.

**En 1911, l’essentiel du chemin était fait.** Le principe d’équivalence date de l’article de synthèse d’Einstein de 1907, et l’article de Prague de 1911 en tire déjà une prédiction quantitative de la déviation de la lumière par le Soleil, 0,83 seconde d’arc, moitié de la valeur de 1915 ([Wikipédia, « History of general relativity »](https://en.wikipedia.org/wiki/History_of_general_relativity), consulté le 10 octobre 2026). Les outils mathématiques existaient aussi : la géométrie de Riemann (1854) et le calcul différentiel absolu de Ricci-Curbastro et Levi-Civita, publié au tournant de 1900. Une coupure fin 1911 qui inclurait les articles d’Einstein lui-même laisserait donc à la machine le travail de 1912-1915 (choix de la géométrie, équations du champ, périhélie de Mercure), considérable mais différent de l’invention du principe. Une coupure en 1906, au contraire, exigerait l’intuition de 1907. *Ce point n’est discuté dans aucune source du corpus.*

**La relativité restreinte était « dans l’air ».** Lorentz avait publié ses transformations en 1904, Poincaré avait formulé le principe de relativité et corrigé ces transformations en 1905 ([Wikipédia, « History of special relativity »](https://en.wikipedia.org/wiki/History_of_special_relativity), consulté le 10 octobre 2026). La variante 1901-relativité restreinte que Hassabis a évoquée à l’All-In Summit en septembre 2025 ([36Kr, 15 septembre 2025](https://eu.36kr.com/en/p/3467136046601605)) est donc un test plus faible : plusieurs physiciens y étaient presque parvenus. Le test le plus discriminant reste celui d’un saut que personne d’autre n’approchait, ce qui était davantage le cas de la relativité générale.

**L’IA fait déjà de la science, mais à l’intérieur des cadres.** La prépublication de Shalyt, Regev, Soljačić et Kaminer ([arXiv:2607.27794](https://arxiv.org/abs/2607.27794), 30 juillet 2026) observe que l’IA en physique a suivi le chemin inverse de l’histoire humaine : des premiers travaux de découverte d’équations aux grands prédicteurs comme AlphaFold ou GraphCast, très précis mais pauvres en théorie. Les auteurs identifient la compétence manquante : poser les bonnes questions, inventer des principes directeurs (symétrie, simplicité) et concevoir les tests qui pourraient réfuter une théorie. Le co-scientifique de Google, cité par la tribune de *CACM*, a proposé en 2025 une hypothèse de transfert de gènes bactériens qui recoupait des résultats non publiés de l’équipe de José Penadés [S8] : c’est un test d’Einstein en miniature, mais sur une hypothèse à portée locale, pas un changement de paradigme.

**Les modèles historiques servent d’abord les sciences humaines.** Underwood, Nelson et Wilkens ont montré qu’un modèle moderne, même affiné, ne restitue pas fidèlement le style d’une époque et qu’un pré-entraînement sur des textes d’époque serait sans doute nécessaire pour simuler des points de vue historiques ([arXiv:2505.00030](https://arxiv.org/abs/2505.00030), 28 avril 2025). L’historien Benjamin Breen y voit l’amorce d’un nouveau champ humaniste ([Res Obscura, 29 avril 2026](https://resobscura.substack.com/t/ai)). Ranke-4B revendique explicitement cet usage, avec un avertissement : ses modèles reproduisent le racisme, l’antisémitisme et la misogynie de leurs sources, et ne reflètent que la parole publiée, plus instruite et plus dominante que l’opinion réelle ([DGoettlich/history-llms](https://github.com/DGoettlich/history-llms), 14 décembre 2025).

**Mesurer la surprise plutôt que la découverte.** Talkie propose une autre manière d’utiliser les coupures : mesurer à quel point les événements postérieurs « surprennent » le modèle. Sur environ 5 000 événements, la surprise augmente après 1930, surtout pour les années 1950 et 1960, puis plafonne ([talkie-lm.com, avril 2026](https://talkie-lm.com/introducing-talkie)). Bart retrouve le même profil pour GPT-1900 autour de 1900 ([Unbounded Labs, 22 août 2026](https://unboundedlab.com/blog/bart)). Evans suggérait déjà de mesurer ainsi à quel point la relativité restreinte était imprévisible avant 1905 [S6]. *Inférence du dossier :* cet usage, plus modeste, pourrait livrer des résultats quantitatifs bien avant qu’un modèle ne passe le test d’Einstein.

### Vérification des affirmations du corpus

| Affirmation | Verdict | Source de la vérification |
|---|---|---|
| Hassabis a proposé le test à l’India AI Summit, en février 2026, avec une coupure en 1911 | **Confirmé** | *Nature* [S3] et OfficeChai [S4] |
| Le test d’Einstein est une proposition de Hassabis | **Nuancé** | Formulations antérieures dans *Time* ([Perrigo, 15 avril 2025](https://time.com/7277608/demis-hassabis-interview-time100-2025/)), chez Thomas Wolf ([« The Einstein AI model », 2025](https://thomwolf.io/blog/scientific-ai.html)) et dans *CACM* [S8] |
| Il n’existe pas de papier relu par les pairs sur l’expérience de Hla | **Confirmé** | Note d’archivage du dépôt, 5 octobre 2026 : ni relecture ni DOI [S2] |
| Le modèle de Hla a 3,3 milliards de paramètres et 22 milliards de tokens | **Confirmé** | Billet et rapport archivé [S1, S2] |
| Le modèle ne connaît que des textes antérieurs à 1900 | **Nuancé** | Vrai pour le pré-entraînement ; la fiche [`mhla/gpt1900-physics-clm`](https://huggingface.co/datasets/mhla/gpt1900-physics-clm) décrit des données de physique étendues à 1905 (Planck 1901, Lorentz 1904), en amont du modèle v11 |
| Rapport de 11 tokens par paramètre | **Non établi** | Le rapport archivé relève l’incohérence avec 22/3,3 ≈ 6,7 [S2] |
| Le modèle s’approche des modèles classiques sur les tests généraux | **Contredit** | Score CORE de 0,140 contre 0,260 pour l’équivalent moderne, sous GPT-2 [S1] ; GPT-1900 d34 est aussi sous Bart sur Vintage CORE ([Unbounded Labs](https://unboundedlab.com/blog/bart)) |
| L’exposé d’Owain Evans date de 2024 | **Confirmé** | Décembre 2024 selon *Nature* [S3] ; citation BibTeX 2024 [S6] |
| « LLMs can’t jump » est un papier de Tom Zahavy (Google DeepMind) | **Confirmé** | Programme ICML 2026 ([poster 67091](https://icml.cc/virtual/2026/poster/67091)) ; *Nature* corrige le 14 septembre les détails de sa publication [S3] |
| GPT-1900 est utilisé par d’autres travaux de recherche | **Confirmé** | TypewriterLM l’évalue comme point de comparaison selon le registre de citations de Hla [S2] ; Bart le compare et reprend son filtre ([Unbounded Labs](https://unboundedlab.com/blog/bart)) |

### Contrepoints et critiques

- **Balani et Panda, [« LLMs Don’t Pay for the Jump »](https://arxiv.org/abs/2608.14397), 14 août 2026.** Les auteurs contestent le remède de Zahavy : le saut de Planck vers E = hν ne doit rien à une simulation incarnée, il vient d’une conséquence mathématique inacceptable de la théorie classique, une énergie infinie. Selon eux, ce qui manque aux modèles est un mécanisme qui rende l’erreur coûteuse au point de forcer la révision. La thèse est stimulante mais spéculative, appuyée sur des mesures d’entropie de sortie plus que sur une expérience de découverte.
- **Le dilemme de la taille du corpus.** Un commentaire publié sous la tribune de *CACM* (28 juin 2026) relève qu’une IA a accès à beaucoup plus de textes qu’Einstein n’en a lu : un corpus trop large favorise la machine, un corpus trop étroit oblige à choisir les textes, donc à indiquer la piste. La tribune elle-même ne règle pas ce point [S8].
- **Thomas Wolf, [« The Einstein AI model »](https://thomwolf.io/blog/scientific-ai.html), 2025.** Le cofondateur de Hugging Face prédit plutôt un « pays de béni-oui-oui sur des serveurs » qu’un pays de génies : les modèles, comme les bons élèves, excellent à répondre aux questions connues mais ne remettent pas en cause leurs prémisses. Il propose des bancs d’essai qui récompensent les questions non évidentes, ce qui rejoint le protocole de *CACM*.
- **Le pragmatisme de Hla lui-même.** Dans son essai, Hla défend un « test du canard » : si des boucles automatisées produisent et vérifient des hypothèses utiles, peu importe qu’elles « disent seulement des mots » [S1]. C’est un contrepoint direct à la lecture de Zahavy, qui fait de la nature du raisonnement un critère.

### Évolutions depuis la publication

Le corpus s’étale de décembre 2024 à septembre 2026, et le sujet a beaucoup bougé pendant cette période. Côté modèles, Talkie-1930 est sorti le 27 avril 2026 avec un modèle de niveau GPT-3 annoncé, TypewriterLM a été accepté à EMNLP 2026 (version 2 du 2 octobre 2026, [arXiv:2606.02991](https://arxiv.org/abs/2606.02991)), et Bart a été publié le 22 août 2026. Ranke-4B reste annoncé : ses dépôts de données et d’entraînement sont toujours marqués « à venir » au 10 octobre 2026. Côté Hla, une édition archivée du rapport technique a été préparée le 5 octobre 2026 ; elle n’ajoute aucune expérience, mais durcit le ton des limites et propose un protocole de réplication (manifestes de corpus, empreintes, graines aléatoires, problèmes réservés et enregistrés à l’avance, validation par des experts en aveugle) [S2]. Côté débat, la prépublication de Kaminer et collègues (30 juillet) et la réponse de Balani et Panda (14 août) prolongent la discussion ouverte par Zahavy.

### Cadre juridique et éthique

- **Domaine public américain.** Talkie justifie sa coupure fin 1930 par l’entrée des œuvres de cette année dans le domaine public aux États-Unis au 1er janvier 2026 ([talkie-lm.com](https://talkie-lm.com/introducing-talkie)) ; les coupures historiques facilitent donc des corpus juridiquement sûrs, ce qui explique en partie l’essor du champ.
- **Contenus discriminatoires.** Les modèles historiques reproduisent les préjugés de leurs sources ; Ranke-4B l’assume comme objet d’étude et prévoit un accès académique encadré, Hla publie une version « sûre » de son modèle d’instructions dont les jugements moraux d’époque ont été retirés ([Hugging Face, mhla](https://huggingface.co/collections/mhla/gpt-1900)).

### Pour aller plus loin

- [awesome-vintage-llms](https://github.com/entanglr/awesome-vintage-llms) — Liste communautaire à jour des modèles historiques, articles, jeux de données et discussions.
- [Galerie des échecs de GPT-1900](https://github.com/michaelhla/gpt1900/blob/master/results/gallery_of_funny_failures.md) — Les réponses ratées les plus parlantes, plus instructives que les réussites.
- [Démonstration GPT-1900](https://gpt1900.com/) et [conversation avec Talkie](https://talkie-lm.com/chat) — Pour interroger soi-même un modèle de 1900 ou de 1930.
- [Exposé d’Owain Evans en vidéo](https://www.youtube.com/watch?v=AA4ophKBK58) — L’intervention qui a nommé le champ, avec ses diapositives.
- [*The Decoder* sur le papier de Zahavy](https://the-decoder.com/language-models-cant-spark-scientific-revolutions-but-world-models-might/) (30 juillet 2026) — Présentation accessible de l’argument de l’abduction et des modèles du monde.
- [Dossier « Autonomie des systèmes d’IA, risques et mécanismes de contrôle »](autonomie-des-systemes-dia-risques-et-mecanismes-de-controle.md) — Pour l’autre versant du débat sur la R&D automatisée : la maîtrise des agents.
