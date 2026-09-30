---
title: Chapitre 2 — Typologie des écosystèmes clandestins
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - 'Partie I — Fondations : penser en écosystème'
  - index.md
---

## 2.1 Écosystèmes purement cybercriminels

La première catégorie, la plus courante, est celle des écosystèmes motivés exclusivement par le profit financier. Les acteurs opèrent selon une logique de marché : ils cherchent le meilleur ratio profit/risque, changent de cibles et de méthodes en fonction des opportunités, et coopèrent avec quiconque peut apporter de la valeur sans considération idéologique ou politique.

La structure de ces écosystèmes est typiquement modulaire : les acteurs sont remplaçables, les relations sont transactionnelles, et la loyauté dépend de la rentabilité. Quand un affilié RaaS trouve une plateforme plus avantageuse (meilleur partage des revenus, meilleur outil, meilleur support), il migre. Quand un IAB est arrêté, un autre prend sa place sur le forum. Cette modularité est à la fois la force (résilience) et la faiblesse (fragilité de la confiance) de ces écosystèmes.

Les exemples les plus documentés incluent les écosystèmes ransomware (LockBit, dont l'opérateur Dmitry Khoroshev a été identifié en 2024 lors de l'opération Cronos mais dont la marque a tenté un retour sous la forme LockBit 5.0 en 2025 ; Conti, fragmenté après les leaks internes de 2022 en plusieurs successeurs dont Royal/BlackSuit ; BlackCat/ALPHV, disrupted par le FBI en décembre 2023), les écosystèmes de carding (marchés de données de cartes bancaires volées, réseau de drop addresses et de mules), et les réseaux de fraude BEC (Business Email Compromise), qui reposent davantage sur l'ingénierie sociale que sur la technique pure mais qui impliquent néanmoins un écosystème de spécialistes (créateurs de comptes, spécialistes email, mules financières, blanchisseurs).

## 2.2 Écosystèmes hybrides crime/finance

La deuxième catégorie se situe à l'intersection de la cybercriminalité et de la criminalité financière traditionnelle. Ces écosystèmes combinent des compétences techniques (compromission de systèmes, manipulation de plateformes numériques) avec des mécanismes de blanchiment et de fraude financière qui impliquent le monde physique (sociétés écrans, immobilier, mules bancaires, comptes offshore).

Les cryptoscams en sont l'illustration la plus visible en 2025-2026 : de faux projets DeFi, des arnaques à l'investissement (pig butchering), ou des rug pulls de tokens frauduleux mobilisent une chaîne qui va du développeur web (qui crée le site crédible) au community manager (qui recrute les victimes via Telegram et réseaux sociaux), au gestionnaire de wallets (qui centralise les fonds), au réseau de mules et sociétés écrans (qui convertit la crypto en fiat). L'écosystème est cybercriminel par ses vecteurs d'attaque mais financier par ses objectifs et ses mécanismes de monétisation.

La frontière avec l'escroquerie financière classique est parfois ténue. Le critère distinctif est la centralité du vecteur numérique : si le cyber est le moyen principal de l'opération (pas un simple canal de communication), l'écosystème relève de cette catégorie.

## 2.3 Écosystèmes para-étatiques

La troisième catégorie est celle des acteurs qui opèrent dans une zone grise entre criminalité et intérêts étatiques. Ces écosystèmes se caractérisent par une tolérance étatique explicite ou implicite, un alignement partiel des cibles avec les intérêts géopolitiques du pays d'origine, et une porosité entre activités criminelles (lucratives) et activités alignées sur les priorités de l'État (collecte de renseignement, sabotage, influence).

Les exemples les mieux documentés sont les groupes russophones qui opèrent avec l'aval tacite des services de sécurité russes (FSB, GRU). Le mécanisme est bien connu : les autorités russes ne poursuivent pas les cybercriminels qui respectent une règle informelle — ne pas cibler la Russie ni les pays de la CEI. Cette tolérance crée un espace dans lequel les individus peuvent mener des opérations cybercriminelles lucratives tout en fournissant occasionnellement des services de renseignement à l'État. La vérification technique de cette règle est visible dans le code de nombreux ransomwares russophones, qui vérifient la langue du système d'exploitation et la disposition du clavier : si le système est configuré en russe, le ransomware ne chiffre pas et se désinstalle.

L'autre exemple majeur est celui de la Corée du Nord, où le Reconnaissance General Bureau (RGB) gère directement des unités cybercriminelles (les groupes classifiés sous l'appellation Lazarus Group par la communauté CTI) dont la mission est de générer des devises pour le régime. L'Office des Nations Unies a estimé que la Corée du Nord avait volé entre 600 millions et 1 milliard de dollars en cryptomonnaie en 2023 seule, une part significative de son financement.

La dimension para-étatique est approfondie au Ch.21.

## 2.4 Écosystèmes d'influence et de manipulation informationnelle

La quatrième catégorie concerne les écosystèmes de désinformation coordonnée qui mobilisent des infrastructures techniques et des logiques économiques comparables à celles de la cybercriminalité « classique ».

Un écosystème de désinformation typique comprend des commanditaires (un État, un parti politique, une entreprise), des prestataires (des sociétés de « PR » de façade, des fermes de trolls, des développeurs de bots), des infrastructures techniques (fermes de comptes, réseaux de faux médias, serveurs d'automatisation), des marchés de services (achat de followers, achat de likes, achat de faux avis), et des flux financiers souvent opaques (paiements via crypto, sociétés écrans, intermédiaires multiples).

Le point de convergence avec les autres catégories est que ces écosystèmes utilisent les mêmes forums, les mêmes prestataires techniques (hébergeurs bulletproof, registrars complaisants), les mêmes mécanismes financiers (sociétés écrans, paiements crypto), et parfois les mêmes acteurs humains (un spécialiste qui fait du SEO black hat le matin et de l'amplification de désinformation l'après-midi). Le Ch.32 traite en détail un cas d'étude d'opération d'influence coordonnée.

## 2.5 Structures internes

centralisé, modulaire, opportuniste, distribué

Au-delà de la motivation, les écosystèmes se distinguent par leur structure organisationnelle interne, et cette structure détermine leur résilience et leur vulnérabilité.

Un écosystème **centralisé** est hiérarchique : un chef ou un noyau dirigeant prend les décisions, les subordonnés exécutent. C'est le modèle des groupes APT étatiques classiques (type APT28/Fancy Bear du GRU russe). L'avantage est la coordination ; la faiblesse est le point de défaillance unique — si le noyau est compromis, l'ensemble est paralysé.

Un écosystème **fédéré** fonctionne comme une franchise : un opérateur central fournit la marque, l'outil et l'infrastructure, des affiliés autonomes mènent les opérations. Le modèle RaaS est l'archétype. L'avantage est la scalabilité ; la faiblesse est que la compromission de l'opérateur central (comme lors de l'opération Cronos contre LockBit en février 2024) affecte tous les affiliés, mais les affiliés peuvent migrer vers un autre opérateur.

Un écosystème **modulaire** se compose de prestataires indépendants qui se combinent au besoin. Il n'y a pas de chef ni de marque commune — les acteurs se trouvent sur les forums, échangent des services, et se séparent après l'opération. L'avantage est la résilience extrême (aucun point de défaillance unique) ; la faiblesse est la difficulté de coordination et le risque d'arnaque entre acteurs (voir Ch.19 sur la confiance).

Un écosystème **opportuniste** est un rassemblement temporaire autour d'une opportunité spécifique (une vulnérabilité 0-day qui vient d'être publiée, un événement géopolitique qui crée des cibles). Les acteurs coopèrent le temps d'exploiter l'opportunité, puis se dispersent. Ce modèle est fréquent dans les premières heures suivant la publication d'une vulnérabilité critique.

> **Bonne pratique :** Lors de la cartographie d'un écosystème, l'une des premières questions analytiques à se poser est : « Quelle est la structure interne ? » La réponse conditionne l'évaluation de la résilience et oriente la stratégie de disruption (voir Ch.22).

## 2.6 Fil rouge — NEXUS : premier indice de classification

> **🔍 NEXUS — Épisode 2**
>
> L'analyse préliminaire du sample donne des premiers éléments de classification. Le malware est un variant de PhantomCrypt, une plateforme RaaS active depuis 18 mois. C'est donc un écosystème fédéré — un opérateur fournit l'outil, un affilié l'a déployé.
>
> Mais deux éléments troublent Samira. Premièrement, la cible : le réseau OT d'un opérateur d'importance vitale du secteur énergie. Les affiliés RaaS opportunistes préfèrent généralement des cibles plus faciles — cabinets d'avocats, PME industrielles, collectivités locales — car le rapport effort/risque est meilleur. Cibler un OIV attire l'attention des autorités et de l'ANSSI, ce que les cybercriminels purement financiers cherchent à éviter. Deuxièmement, le timing : l'attaque survient en pleine période de tension diplomatique sur les contrats gaziers européens, un contexte dans lequel la déstabilisation d'un opérateur énergétique français pourrait servir des intérêts géopolitiques.
>
> Samira note dans son journal d'analyse : « Hypothèse de travail initiale : écosystème RaaS (structure fédérée, motivation financière probable), mais la cible et le timing suggèrent une possible dimension para-étatique. Maintenir les deux hypothèses. Confiance : faible à ce stade. »

---
