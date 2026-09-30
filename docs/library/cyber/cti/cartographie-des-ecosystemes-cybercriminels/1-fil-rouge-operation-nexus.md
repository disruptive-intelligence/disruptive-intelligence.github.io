---
title: 'Fil rouge : Opération NEXUS'
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
chapter: 1
chapters: 8
---

> **Contexte narratif — ce fil rouge traverse les 28 premiers chapitres du cours.**
>
> **Mars 2026.** Samira Khaled, analyste CTI senior chez *Énergis*, un opérateur français d'infrastructures énergétiques classé OIV (Opérateur d'Importance Vitale), reçoit une alerte du SOC interne. Un sample de malware a été détecté sur un poste d'ingénierie connecté au réseau OT (Operational Technology) du site de production de Fos-sur-Mer. L'antivirus a bloqué l'exécution, mais le fichier a déjà communiqué brièvement avec un domaine C2 inconnu : `update-srv-infra[.]xyz`.
>
> Le CERT interne confirme : le binaire est un variant de ransomware déployé par un builder connu, associé à une plateforme RaaS active. Mais la cible — un réseau OT dans le secteur énergie, en pleine tension géopolitique sur l'approvisionnement européen — ne correspond pas au profil opportuniste habituel des affiliés ransomware.
>
> Samira ouvre une investigation CTI. Son objectif : cartographier l'écosystème complet derrière ce sample — de l'opérateur RaaS à l'affilié, de l'IAB qui a vendu l'accès initial au service de mixing qui blanchit les fonds, de l'hébergeur bulletproof au relais médiatique qui amplifie la pression. Et surtout : déterminer si cette attaque est purement criminelle ou si elle sert aussi des intérêts para-étatiques.
>
> Chaque chapitre enrichira cette investigation, ajoutera des pièces au graphe, et confrontera Samira à des décisions méthodologiques concrètes. Le rapport final, livré au Chapitre 28, sera une note d'analyse complète destinée à la direction générale d'Énergis, au CERT, à l'ANSSI, et potentiellement aux forces de l'ordre.

---


## PARTIE I — FONDATIONS : PENSER EN ÉCOSYSTÈME

*Avant de cartographier quoi que ce soit : comprendre pourquoi on raisonne en écosystème, avec quels outils, dans quel cadre, et avec quelle rigueur intellectuelle.*

---

### Chapitre 1 — Pourquoi raisonner en écosystème

#### 1.1 Les limites de la vision « un hacker fait tout »

La représentation dominante de la cybermenace dans les médias, dans les présentations de direction générale, et même dans certains rapports de sécurité, reste celle du hacker isolé : un individu techniquement brillant qui, seul devant son écran, compromet un système, vole des données, et disparaît. Cette image est obsolète depuis au moins quinze ans, et elle est activement nuisible à la compréhension de la menace contemporaine.

La persistance de cette représentation s'explique par trois facteurs. Premièrement, le narratif individuel est cognitivement satisfaisant : il est plus facile de concevoir un adversaire unique qu'un réseau de prestataires interconnectés. Deuxièmement, les affaires judiciaires se concluent souvent par l'arrestation d'un individu ou d'un petit groupe, ce qui renforce l'illusion d'un acteur monolithique même quand l'enquête a révélé un écosystème complet. Troisièmement, une partie de l'industrie de la cybersécurité a intérêt à simplifier la menace pour vendre des solutions « clé en main » — si le problème est un hacker, la solution est un produit.

Le problème opérationnel de cette vision est qu'elle conduit à des réponses inadaptées. Si l'analyste pense affronter un individu, il cherche à l'identifier et à le bloquer. Si l'analyste comprend qu'il affronte un écosystème, il cherche à cartographier les dépendances et à identifier les points de fragilité. La première approche est tactique et éphémère ; la seconde est stratégique et structurelle.

> **Implication pour le praticien :** Un rapport d'incident qui conclut par « le groupe X nous a attaqués » sans cartographier la chaîne d'approvisionnement (qui a fourni l'accès initial, qui a fourni le malware, qui héberge l'infrastructure, qui blanchit l'argent) est un rapport incomplet. Il répond au « qui » superficiel mais pas au « comment » structurel — et c'est le « comment » structurel qui permet d'anticiper et de prévenir.

#### 1.2 D'un acteur isolé à un marché structuré : la fragmentation des rôles

La cybercriminalité contemporaine fonctionne comme une économie de services spécialisés. Celui qui développe le ransomware ne le déploie généralement pas lui-même. Celui qui compromet le réseau de la victime n'a souvent pas écrit une ligne du malware qu'il utilise. Celui qui négocie la rançon avec la victime n'a souvent jamais touché à un clavier technique. Celui qui blanchit les cryptomonnaies n'a souvent aucune compétence en intrusion informatique.

Cette fragmentation n'est pas un accident — c'est le résultat d'une logique économique de spécialisation. Chaque rôle exige des compétences distinctes, comporte des risques différents, et génère une rémunération propre. Un développeur de ransomware peut toucher un salaire mensuel de 5 000 à 15 000 dollars sans jamais interagir avec une victime. Un affilié (celui qui déploie le ransomware) prend un risque opérationnel plus élevé mais capte 70 à 80 % de la rançon. Un Initial Access Broker (IAB) vend des accès compromis pour quelques centaines à quelques dizaines de milliers de dollars, avec un risque modéré car il n'est pas directement impliqué dans l'extorsion.

La conséquence analytique est fondamentale : « l'attaquant » n'est presque jamais une entité unique. C'est un assemblage temporaire de prestataires spécialisés qui coopèrent le temps d'une opération, chacun apportant sa compétence et facturant son service.

Le détail des rôles spécialisés (développeurs, opérateurs, affiliés, IAB, crypter services, hébergeurs, blanchisseurs, mules, négociateurs, modérateurs) est traité au Ch.17.

#### 1.3 La notion d'écosystème

Un écosystème cybercriminel n'est pas simplement un « groupe » au sens classique du terme. C'est un ensemble d'acteurs en interaction — certains stables, d'autres éphémères — qui forment un système fonctionnel plus vaste que la somme de ses parties.

Les composantes d'un écosystème typique incluent un noyau opérateur (les acteurs qui contrôlent les opérations et les décisions stratégiques), des intermédiaires (brokers d'accès, facilitateurs de communication, négociateurs), des sous-traitants techniques (développeurs de malware, fournisseurs de crypters, hébergeurs), des facilitateurs financiers (services de mixing, sociétés écrans, mules), des relais médiatiques et informationnels (leak sites, canaux Telegram, blogs de façade), des clients (les affiliés qui utilisent le service, les acheteurs de données), parfois des sponsors étatiques ou para-étatiques (voir Ch.21), et des communautés périphériques (forums, canaux de discussion, espaces de recrutement).

La propriété fondamentale d'un écosystème est qu'il possède des caractéristiques émergentes que ses composants individuels n'ont pas. Un affilié seul est vulnérable ; un écosystème RaaS complet est résilient. Un forum seul est une liste de messages ; un réseau de forums interconnectés est un marché avec gouvernance, réputation et mécanismes de confiance. C'est cette émergence qui rend l'approche systémique nécessaire.

> **Alerte / Piège fréquent :** La tentation de l'analyste est de traiter un écosystème comme un organigramme figé. C'est une erreur. Les écosystèmes cybercriminels sont dynamiques : les acteurs entrent et sortent, les alliances se forment et se défont, les services disparaissent et sont remplacés. La cartographie d'un écosystème est toujours un instantané daté, pas une structure permanente.

#### 1.4 La chaîne de valeur criminelle

Emprunté à l'économie industrielle (le concept de Michael Porter), la notion de chaîne de valeur appliquée à la cybercriminalité décrit la séquence d'activités par lesquelles une menace se transforme en profit. De la conception de l'outil d'attaque à la conversion en argent propre, chaque étape crée et capte de la valeur économique.

Une chaîne de valeur ransomware typique en 2025-2026 se décompose ainsi : le développement de l'outil (le ransomware, son builder, son panel de contrôle), puis l'acquisition d'un accès initial (achat auprès d'un IAB, exploitation d'une vulnérabilité, phishing), puis la compromission du réseau (élévation de privilèges, mouvement latéral, désactivation des défenses), puis l'exfiltration des données (pour la double extorsion), puis le chiffrement et la demande de rançon, puis la négociation avec la victime, puis le paiement en cryptomonnaie, puis le blanchiment (mixing, conversion, cash-out), et enfin le réinvestissement dans l'infrastructure et les opérations suivantes.

L'intérêt analytique de cette vision est double. Premièrement, elle permet d'identifier les points de concentration — les étapes où beaucoup de valeur transite par peu d'acteurs. Les services de mixing, les hébergeurs bulletproof dominants, et les quelques exchanges non coopératifs sont des points de concentration parce que de nombreux écosystèmes dépendent des mêmes prestataires à ces étapes. Deuxièmement, elle permet d'identifier les points de fragilité — les étapes où la disruption serait la plus efficace. La chaîne de valeur complète est détaillée au Ch.18.

#### 1.5 Convergence entre technique, finance, logistique, réputation et influence

Un écosystème cybercriminel n'est pas un phénomène purement technique. Il repose sur au moins cinq dimensions qui interagissent.

La **dimension technique** couvre les outils (malware, infrastructure C2, exploits), les compétences (développement, intrusion, administration système), et les plateformes (hébergement, DNS, CDN). La **dimension financière** couvre les flux de valeur (paiements de rançon, rémunérations des prestataires, blanchiment), les instruments (cryptomonnaies, sociétés écrans, mules bancaires), et les mécanismes de transaction (escrow, arbitrage). La **dimension logistique** couvre l'approvisionnement en ressources (acquisition d'accès, recrutement de mules, location d'infrastructure), la coordination opérationnelle (communication entre acteurs, gestion des affiliés), et la continuité des opérations (backup d'infrastructure, migration après disruption). La **dimension réputationnelle** couvre la confiance entre acteurs (réputation sur les forums, vouching, historique de transactions), la crédibilité de la marque (un opérateur RaaS dont les affiliés sont satisfaits attire plus d'affiliés), et la dissuasion (la réputation d'un groupe comme fiable dans le paiement de la rançon encourage les victimes futures à payer). La **dimension informationnelle et d'influence** couvre la pression médiatique sur les victimes (leak sites, menaces de publication), l'amplification via les réseaux sociaux et les médias de façade, et parfois la manipulation narrative à des fins géopolitiques.

L'analyste qui ne regarde que la dimension technique manque les trois quarts de l'écosystème. La cartographie doit intégrer ces cinq dimensions pour être complète.

#### 1.6 Fil rouge — Opération NEXUS : le point de départ

> **🔍 NEXUS — Épisode 1**
>
> Le SOC d'Énergis remonte l'alerte à 14h37. Le fichier détecté est un exécutable PE32 de 847 Ko, obfusqué, qui a tenté de résoudre le domaine `update-srv-infra[.]xyz` avant d'être bloqué par l'EDR.
>
> Le réflexe classique de la direction serait de demander : « Qui nous a attaqués ? » La réponse initiale du CERT est : « Un variant de la famille de ransomware PhantomCrypt, associée à une plateforme RaaS active. » Cette réponse est correcte mais radicalement insuffisante. Elle identifie l'outil, pas l'écosystème.
>
> Samira reformule la question : « Quel est l'écosystème derrière ce sample ? Qui l'a développé, qui l'a déployé, qui a fourni l'accès initial, qui héberge l'infrastructure, qui blanchira les fonds si une rançon est payée, et pourquoi cette cible ? » Ce sont ces questions qui guideront les 27 chapitres suivants.

---

### Chapitre 2 — Typologie des écosystèmes clandestins

#### 2.1 Écosystèmes purement cybercriminels

La première catégorie, la plus courante, est celle des écosystèmes motivés exclusivement par le profit financier. Les acteurs opèrent selon une logique de marché : ils cherchent le meilleur ratio profit/risque, changent de cibles et de méthodes en fonction des opportunités, et coopèrent avec quiconque peut apporter de la valeur sans considération idéologique ou politique.

La structure de ces écosystèmes est typiquement modulaire : les acteurs sont remplaçables, les relations sont transactionnelles, et la loyauté dépend de la rentabilité. Quand un affilié RaaS trouve une plateforme plus avantageuse (meilleur partage des revenus, meilleur outil, meilleur support), il migre. Quand un IAB est arrêté, un autre prend sa place sur le forum. Cette modularité est à la fois la force (résilience) et la faiblesse (fragilité de la confiance) de ces écosystèmes.

Les exemples les plus documentés incluent les écosystèmes ransomware (LockBit, dont l'opérateur Dmitry Khoroshev a été identifié en 2024 lors de l'opération Cronos mais dont la marque a tenté un retour sous la forme LockBit 5.0 en 2025 ; Conti, fragmenté après les leaks internes de 2022 en plusieurs successeurs dont Royal/BlackSuit ; BlackCat/ALPHV, disrupted par le FBI en décembre 2023), les écosystèmes de carding (marchés de données de cartes bancaires volées, réseau de drop addresses et de mules), et les réseaux de fraude BEC (Business Email Compromise), qui reposent davantage sur l'ingénierie sociale que sur la technique pure mais qui impliquent néanmoins un écosystème de spécialistes (créateurs de comptes, spécialistes email, mules financières, blanchisseurs).

#### 2.2 Écosystèmes hybrides crime/finance

La deuxième catégorie se situe à l'intersection de la cybercriminalité et de la criminalité financière traditionnelle. Ces écosystèmes combinent des compétences techniques (compromission de systèmes, manipulation de plateformes numériques) avec des mécanismes de blanchiment et de fraude financière qui impliquent le monde physique (sociétés écrans, immobilier, mules bancaires, comptes offshore).

Les cryptoscams en sont l'illustration la plus visible en 2025-2026 : de faux projets DeFi, des arnaques à l'investissement (pig butchering), ou des rug pulls de tokens frauduleux mobilisent une chaîne qui va du développeur web (qui crée le site crédible) au community manager (qui recrute les victimes via Telegram et réseaux sociaux), au gestionnaire de wallets (qui centralise les fonds), au réseau de mules et sociétés écrans (qui convertit la crypto en fiat). L'écosystème est cybercriminel par ses vecteurs d'attaque mais financier par ses objectifs et ses mécanismes de monétisation.

La frontière avec l'escroquerie financière classique est parfois ténue. Le critère distinctif est la centralité du vecteur numérique : si le cyber est le moyen principal de l'opération (pas un simple canal de communication), l'écosystème relève de cette catégorie.

#### 2.3 Écosystèmes para-étatiques

La troisième catégorie est celle des acteurs qui opèrent dans une zone grise entre criminalité et intérêts étatiques. Ces écosystèmes se caractérisent par une tolérance étatique explicite ou implicite, un alignement partiel des cibles avec les intérêts géopolitiques du pays d'origine, et une porosité entre activités criminelles (lucratives) et activités alignées sur les priorités de l'État (collecte de renseignement, sabotage, influence).

Les exemples les mieux documentés sont les groupes russophones qui opèrent avec l'aval tacite des services de sécurité russes (FSB, GRU). Le mécanisme est bien connu : les autorités russes ne poursuivent pas les cybercriminels qui respectent une règle informelle — ne pas cibler la Russie ni les pays de la CEI. Cette tolérance crée un espace dans lequel les individus peuvent mener des opérations cybercriminelles lucratives tout en fournissant occasionnellement des services de renseignement à l'État. La vérification technique de cette règle est visible dans le code de nombreux ransomwares russophones, qui vérifient la langue du système d'exploitation et la disposition du clavier : si le système est configuré en russe, le ransomware ne chiffre pas et se désinstalle.

L'autre exemple majeur est celui de la Corée du Nord, où le Reconnaissance General Bureau (RGB) gère directement des unités cybercriminelles (les groupes classifiés sous l'appellation Lazarus Group par la communauté CTI) dont la mission est de générer des devises pour le régime. L'Office des Nations Unies a estimé que la Corée du Nord avait volé entre 600 millions et 1 milliard de dollars en cryptomonnaie en 2023 seule, une part significative de son financement.

La dimension para-étatique est approfondie au Ch.21.

#### 2.4 Écosystèmes d'influence et de manipulation informationnelle

La quatrième catégorie concerne les écosystèmes de désinformation coordonnée qui mobilisent des infrastructures techniques et des logiques économiques comparables à celles de la cybercriminalité « classique ».

Un écosystème de désinformation typique comprend des commanditaires (un État, un parti politique, une entreprise), des prestataires (des sociétés de « PR » de façade, des fermes de trolls, des développeurs de bots), des infrastructures techniques (fermes de comptes, réseaux de faux médias, serveurs d'automatisation), des marchés de services (achat de followers, achat de likes, achat de faux avis), et des flux financiers souvent opaques (paiements via crypto, sociétés écrans, intermédiaires multiples).

Le point de convergence avec les autres catégories est que ces écosystèmes utilisent les mêmes forums, les mêmes prestataires techniques (hébergeurs bulletproof, registrars complaisants), les mêmes mécanismes financiers (sociétés écrans, paiements crypto), et parfois les mêmes acteurs humains (un spécialiste qui fait du SEO black hat le matin et de l'amplification de désinformation l'après-midi). Le Ch.32 traite en détail un cas d'étude d'opération d'influence coordonnée.

#### 2.5 Structures internes : centralisé, modulaire, opportuniste, distribué

Au-delà de la motivation, les écosystèmes se distinguent par leur structure organisationnelle interne, et cette structure détermine leur résilience et leur vulnérabilité.

Un écosystème **centralisé** est hiérarchique : un chef ou un noyau dirigeant prend les décisions, les subordonnés exécutent. C'est le modèle des groupes APT étatiques classiques (type APT28/Fancy Bear du GRU russe). L'avantage est la coordination ; la faiblesse est le point de défaillance unique — si le noyau est compromis, l'ensemble est paralysé.

Un écosystème **fédéré** fonctionne comme une franchise : un opérateur central fournit la marque, l'outil et l'infrastructure, des affiliés autonomes mènent les opérations. Le modèle RaaS est l'archétype. L'avantage est la scalabilité ; la faiblesse est que la compromission de l'opérateur central (comme lors de l'opération Cronos contre LockBit en février 2024) affecte tous les affiliés, mais les affiliés peuvent migrer vers un autre opérateur.

Un écosystème **modulaire** se compose de prestataires indépendants qui se combinent au besoin. Il n'y a pas de chef ni de marque commune — les acteurs se trouvent sur les forums, échangent des services, et se séparent après l'opération. L'avantage est la résilience extrême (aucun point de défaillance unique) ; la faiblesse est la difficulté de coordination et le risque d'arnaque entre acteurs (voir Ch.19 sur la confiance).

Un écosystème **opportuniste** est un rassemblement temporaire autour d'une opportunité spécifique (une vulnérabilité 0-day qui vient d'être publiée, un événement géopolitique qui crée des cibles). Les acteurs coopèrent le temps d'exploiter l'opportunité, puis se dispersent. Ce modèle est fréquent dans les premières heures suivant la publication d'une vulnérabilité critique.

> **Bonne pratique :** Lors de la cartographie d'un écosystème, l'une des premières questions analytiques à se poser est : « Quelle est la structure interne ? » La réponse conditionne l'évaluation de la résilience et oriente la stratégie de disruption (voir Ch.22).

#### 2.6 Fil rouge — NEXUS : premier indice de classification

> **🔍 NEXUS — Épisode 2**
>
> L'analyse préliminaire du sample donne des premiers éléments de classification. Le malware est un variant de PhantomCrypt, une plateforme RaaS active depuis 18 mois. C'est donc un écosystème fédéré — un opérateur fournit l'outil, un affilié l'a déployé.
>
> Mais deux éléments troublent Samira. Premièrement, la cible : le réseau OT d'un opérateur d'importance vitale du secteur énergie. Les affiliés RaaS opportunistes préfèrent généralement des cibles plus faciles — cabinets d'avocats, PME industrielles, collectivités locales — car le rapport effort/risque est meilleur. Cibler un OIV attire l'attention des autorités et de l'ANSSI, ce que les cybercriminels purement financiers cherchent à éviter. Deuxièmement, le timing : l'attaque survient en pleine période de tension diplomatique sur les contrats gaziers européens, un contexte dans lequel la déstabilisation d'un opérateur énergétique français pourrait servir des intérêts géopolitiques.
>
> Samira note dans son journal d'analyse : « Hypothèse de travail initiale : écosystème RaaS (structure fédérée, motivation financière probable), mais la cible et le timing suggèrent une possible dimension para-étatique. Maintenir les deux hypothèses. Confiance : faible à ce stade. »

---

### Chapitre 3 — Lecture systémique d'un environnement clandestin

#### 3.1 Penser en graphe, pas en silos

L'erreur la plus courante de l'analyste débutant est de traiter chaque indice isolément. Un domaine C2, pris seul, est un indicateur de compromission (IoC) — utile pour la détection, mais pauvre en renseignement. Un pseudo vu sur un forum, pris seul, est un identifiant — utile pour le suivi, mais pauvre en contexte. Un wallet Bitcoin, pris seul, est une adresse — utile pour le traçage, mais pauvre en attribution.

La valeur analytique apparaît quand on relie ces éléments. Quand le domaine C2 pointe vers une IP hébergée chez un fournisseur connu pour son bulletproof hosting, que cette même IP héberge un blog anonyme qui relaie des revendications de ransomware, que le certificat SSL du domaine est un wildcard partagé avec trois autres domaines associés à des campagnes précédentes, que l'enregistrement WHOIS historique du domaine révèle un email ProtonMail, que cet email a été compromis dans un breach et est associé à un pseudo actif sur un forum underground, que ce pseudo a recommandé un service de mixing sur un canal Telegram — alors un écosystème commence à apparaître.

Penser en graphe signifie que chaque nouvel indice n'est pas évalué pour ce qu'il « est » mais pour ce qu'il « relie ». L'analyste ne collecte pas des données — il construit des connexions. Chaque entité est un nœud dans un graphe, et chaque connexion identifiée est une arête qui enrichit la compréhension de l'ensemble.

#### 3.2 Nœuds, liens, flux et dépendances

Le vocabulaire de base de l'analyse de réseau, emprunté à la théorie des graphes et à l'analyse de réseau social (Social Network Analysis, SNA), doit être maîtrisé par l'analyste.

Un **nœud** (ou sommet) est une entité dans le graphe. Les nœuds peuvent être des personnes (identifiées ou pseudonymisées), des organisations (groupes, sociétés écrans, forums), des objets techniques (domaines, IP, serveurs, malware, certificats), des objets financiers (wallets, comptes bancaires, sociétés), ou des espaces (forums, canaux Telegram, leak sites). Chaque nœud a des attributs : type, nom, date de découverte, source, niveau de confiance.

Un **lien** (ou arête) est une relation entre deux nœuds. Les liens sont typés (technique, financier, identitaire, social, temporel — détail au Ch.11) et qualifiés (force, direction, confiance). Un lien peut être directionnel (A paie B) ou bidirectionnel (A et B communiquent). La qualification des liens est le cœur de la rigueur analytique — voir Ch.11 et Ch.12.

Un **flux** est un mouvement entre nœuds. Les flux peuvent être financiers (transfert de crypto), informationnels (transmission de données volées, communication d'instructions), ou matériels (livraison d'accès, déploiement de malware). L'analyse des flux révèle la dynamique de l'écosystème : qui fournit quoi à qui, dans quel ordre, à quel volume.

Une **dépendance** est un lien critique dont la rupture affecterait le fonctionnement de l'écosystème. Si un affilié dépend d'un seul IAB pour ses accès initiaux, la relation affilié-IAB est une dépendance. Si un opérateur RaaS dépend d'un seul hébergeur bulletproof pour son infrastructure, cette relation est une dépendance critique. L'identification des dépendances est l'objectif ultime de la cartographie, car elles révèlent les points de fragilité exploitables pour la disruption (Ch.22).

#### 3.3 Intermédiaires critiques et points de concentration

Tous les nœuds d'un graphe n'ont pas la même importance structurelle. La théorie des réseaux distingue deux types de nœuds particulièrement significatifs.

Les **hubs** sont des nœuds très connectés — ils ont un grand nombre de liens directs avec d'autres nœuds. Un hébergeur bulletproof qui sert 50 groupes différents est un hub. Un forum avec 10 000 membres actifs est un hub. Les hubs sont importants parce que leur suppression déconnecte beaucoup de nœuds simultanément. Mais ils ne sont pas nécessairement les plus intéressants analytiquement, car leur rôle est souvent passif (ils fournissent un service sans contrôler les opérations).

Les **brokers** (ou intermédiaires de ponts) sont des nœuds qui connectent des communautés qui seraient sinon séparées. Un acteur qui est à la fois actif sur un forum anglophone de carding et sur un forum russophone de ransomware est un broker : il relie deux communautés. Un IAB qui vend des accès à des affiliés de trois plateformes RaaS différentes est un broker : il relie trois écosystèmes. La métrique formelle est la betweenness centrality — le nombre de chemins les plus courts entre paires de nœuds qui passent par un nœud donné.

Les brokers sont souvent les cibles les plus intéressantes pour la disruption, car leur suppression fragmente le réseau en communautés isolées qui ne peuvent plus coopérer.

> **Bonne pratique :** Lors de la construction d'un graphe dans Maltego ou Gephi (voir Ch.5), calculer systématiquement les métriques de centralité (degree, betweenness, closeness) pour identifier les hubs et les brokers. Ne pas se fier à l'impression visuelle seule — un nœud visuellement central dans le layout n'est pas forcément structurellement central.

#### 3.4 Fonctions visibles et fonctions cachées

Chaque entité dans un écosystème remplit des fonctions manifestes (visibles, déclarées) et des fonctions latentes (cachées, implicites).

Un forum underground est manifestement une place de marché — les utilisateurs y achètent et vendent des services et des données. Mais un forum remplit aussi des fonctions latentes essentielles. C'est un espace de recrutement (les acteurs compétents se font remarquer par leurs contributions et sont approchés pour des opérations). C'est un filtre de sélection (le système de vouching, les fees d'entrée, et les règles de la communauté filtrent les « amateurs » et les agents infiltrés). C'est un mécanisme de réputation (l'historique des transactions et les ratings sont le « CV » d'un acteur). C'est un espace de gouvernance (les modérateurs arbitrent les litiges, les admins fixent les règles, les sanctions collectives punissent les tricheurs).

L'analyste qui ne voit que la fonction marchande d'un forum sous-estime dramatiquement son importance dans l'écosystème. Supprimer un forum ne supprime pas seulement une place de marché — cela détruit un capital social, un système de réputation, et un mécanisme de confiance qui avaient mis des années à se construire. C'est pourquoi les takedowns de forums ont un impact si profond, même quand les acteurs migrent rapidement vers des alternatives (le capital social ne migre pas automatiquement).

#### 3.5 Résilience et adaptation

Un écosystème bien structuré survit à la perte de certains de ses nœuds. Si un forum ferme, l'activité migre vers un autre. Si un affilié est arrêté, un autre prend sa place. Si un service de mixing est saisi, un concurrent émerge. Cette propriété — la capacité du système à maintenir sa fonction malgré la perte de composants — est la résilience.

La résilience d'un écosystème dépend de plusieurs facteurs. La **redondance** : y a-t-il plusieurs nœuds capables de remplir la même fonction ? Si l'écosystème dispose de plusieurs hébergeurs bulletproof alternatifs, il survit à la perte de l'un d'eux. La **substituabilité des acteurs** : les rôles sont-ils suffisamment standardisés pour qu'un acteur puisse être remplacé par un autre ? Dans un modèle RaaS, les affiliés sont hautement substituables. La **décentralisation** : le contrôle et la prise de décision sont-ils distribués ? Un écosystème modulaire sans noyau central est plus résilient qu'un écosystème centralisé. La **rapidité de reconstitution** : combien de temps faut-il pour reconstruire un composant perdu ? L'opération Cronos contre LockBit en février 2024 a saisi l'infrastructure, identifié l'administrateur, et banni la marque des forums majeurs — pourtant, l'opérateur a tenté de reconstruire sous LockBit 4.0 puis LockBit 5.0, cette dernière version ayant été détectée en attaque active dès septembre 2025 par Check Point Research.

Évaluer la résilience est essentiel pour estimer l'impact d'une action de disruption (Ch.22) : une action qui supprime un nœud substituable a un impact temporaire ; une action qui supprime un nœud critique non redondant a un impact structurel.

#### 3.6 Fil rouge — NEXUS : le domaine C2 comme point d'entrée

> **🔍 NEXUS — Épisode 3**
>
> Samira commence par le point d'entrée le plus concret : le domaine C2 `update-srv-infra[.]xyz`. Elle interroge les bases de données de renseignement.
>
> Le **WHOIS actuel** est masqué par un service de privacy (résultat attendu — les acteurs ne laissent plus de données WHOIS exploitables depuis des années). Le **WHOIS historique** (via DomainTools) révèle que le domaine a été enregistré 6 mois plus tôt, et qu'un enregistrement intermédiaire — probablement une erreur OPSEC du registrant — mentionne l'email `kr0n0s-ops@proton.me`.
>
> Le **reverse DNS** montre que l'IP associée au domaine (185.234.xx.xx) est hébergée par un fournisseur VPS basé en Moldavie, connu dans les rapports CTI pour sa tolérance envers les contenus malveillants — un hébergeur bulletproof. Le **reverse IP** (via SecurityTrails) révèle que cette même adresse héberge 4 autres domaines. L'un d'eux, `phantom-news[.]press`, ressemble à un blog.
>
> Ce n'est pas un nœud isolé — c'est un point d'entrée dans un graphe. Samira commence à dessiner : le domaine C2, l'IP, l'hébergeur, l'email ProtonMail, et les domaines co-localisés. Cinq nœuds, quatre liens. Le graphe est encore embryonnaire. Mais la méthode est en place.

---

### Chapitre 4 — Cadre juridique, éthique et posture de travail

#### 4.1 Ce que l'analyste a le droit de faire — et ce qu'il n'a pas le droit de faire

Le cadre juridique de l'investigation CTI en France (et plus largement en Europe) est souvent mal compris par les praticiens, ce qui conduit soit à une paralysie excessive (« on ne peut rien faire sans mandat ») soit à des prises de risque inconsidérées (« c'est de l'OSINT, donc c'est légal »).

Les **activités légales sans restriction** pour un analyste CTI d'entreprise incluent la consultation de sources ouvertes indexées par les moteurs de recherche, la consultation de registres publics (WHOIS historique, registres d'entreprises, cadastre, brevets), l'analyse de données techniques partagées par la communauté CTI (rapports, IoC, samples soumis à des sandboxes publiques), l'analyse de la blockchain publique (Bitcoin, Ethereum — les transactions sont par design publiques et pseudonymisées), la consultation de bases de données de breaches accessibles via des services légaux (DeHashed, Have I Been Pwned, IntelX — la légalité de la consultation est établie, l'exploitation opérationnelle des données personnelles est encadrée par le RGPD), et l'observation passive du dark web (consulter un forum sans interaction).

Les **activités encadrées nécessitant une attention particulière** incluent l'exploitation de données à caractère personnel issues de breaches (autorisée dans le cadre de la réponse à incident de l'entreprise, mais les données doivent être traitées conformément au RGPD : finalité légitime, proportionnalité, durée de conservation limitée, information du DPO), la collecte de données depuis des canaux Telegram ou Discord (la consultation est légale, mais la collecte automatisée massive peut poser des questions sous l'angle du RGPD et de la loi Informatique et Libertés), et la communication d'IoC ou de résultats d'investigation aux forces de l'ordre ou à l'ANSSI (non seulement légale mais encouragée — l'article L.2321-1 du Code de la défense donne à l'ANSSI un rôle de coordination).

Les **activités illégales** incluent toute interaction active avec des acteurs criminels (même sous une fausse identité, sans cadre judiciaire, cela constitue potentiellement une provocation ou une complicité), toute intrusion dans un système informatique tiers, même celui d'un attaquant (le « hack back » est illégal en France — article 323-1 du Code pénal), l'achat de services criminels (même « pour tester » — acheter un accès sur un forum pour vérifier sa validité est une infraction), et l'utilisation de logiciels d'interception de communications (hors cadre judiciaire ou autorisation légale spécifique).

> **Alerte :** La frontière entre observation passive et interaction active est parfois floue. Créer un compte sur un forum pour lire des messages est généralement considéré comme de l'observation passive. Poster un message, même anodin, pour établir une couverture est une interaction active qui sort du cadre légal de l'analyste privé.

#### 4.2 Responsabilité analytique

Une cartographie d'écosystème qui nomme des personnes ou des organisations crée un risque juridique et éthique que l'analyste doit anticiper.

Nommer un acteur comme « membre d'un écosystème criminel » dans un rapport interne ou partagé avec des partenaires, sans un niveau de preuve suffisant, est potentiellement diffamatoire (article 29 de la loi du 29 juillet 1881). Même dans un contexte de réponse à incident, l'analyste doit distinguer rigoureusement entre ce qui est établi (le pseudo kr0n0s_ops est actif sur le forum X et revendique Y), ce qui est probable (les indices convergents suggèrent que kr0n0s_ops et le compte GitHub Z sont contrôlés par la même personne), et ce qui est hypothétique (il est possible que cette personne opère depuis la Russie sur la base du fuseau horaire d'activité).

Le rapport d'analyse doit toujours expliciter ses niveaux de confiance (voir Ch.13) et ne jamais présenter une hypothèse comme un fait. Cette discipline n'est pas seulement une précaution juridique — c'est une exigence de qualité analytique. Un rapport qui mélange faits et hypothèses sans les distinguer est un mauvais rapport, indépendamment des conséquences juridiques.

#### 4.3 Neutralité et rigueur

L'analyste CTI n'est pas un enquêteur judiciaire (il ne prouve pas la culpabilité), il n'est pas un journaliste (il ne publie pas), et il n'est pas un militant (il ne dénonce pas). Il produit du renseignement analytique destiné à informer une décision.

Sa valeur repose sur sa rigueur et sa prudence, pas sur le caractère spectaculaire de ses conclusions. Un rapport qui dit « nous avons identifié un écosystème de 12 acteurs avec un niveau de confiance modéré, et nous recommandons 3 investigations complémentaires pour renforcer l'attribution » est plus utile qu'un rapport qui dit « le groupe X, probablement sponsorisé par l'État Y, nous a ciblé dans le cadre de la stratégie Z » — si le second ne repose pas sur un faisceau d'indices suffisant.

La neutralité implique aussi de ne pas surinterpréter dans le sens qui plairait au commanditaire. Si la direction espère que l'attaque est « étatique » (parce que cela renforce le discours politique), l'analyste ne doit pas forcer les conclusions dans cette direction. Si les données pointent vers un affilié opportuniste, c'est cette conclusion qu'il faut présenter, avec les nuances nécessaires.

#### 4.4 Conservation des sources et traçabilité du raisonnement

Chaque connexion dans la cartographie doit être traçable : quelle source, quelle date de consultation, quel outil utilisé, quel niveau de confiance attribué, et quel raisonnement a conduit à l'établissement du lien.

Un graphe non sourcé est un graphe inexploitable. Si un collègue reprend l'analyse six mois plus tard, ou si le rapport est transmis aux forces de l'ordre, ou si une décision stratégique est prise sur la base de la cartographie, il faut pouvoir remonter à l'origine de chaque assertion.

En pratique, cela signifie maintenir un journal de collecte (un document chronologique qui enregistre chaque recherche, chaque requête, chaque résultat, chaque décision analytique) et annoter chaque nœud et chaque lien du graphe avec ses métadonnées de source. Les outils comme Obsidian (notes liées) et Maltego (métadonnées sur les entités) permettent cette traçabilité. Le workflow opérationnel est détaillé au Ch.25.

#### 4.5 Fil rouge — NEXUS : cadrage de l'investigation

> **🔍 NEXUS — Épisode 4**
>
> Samira cadre formellement l'investigation avant de plonger plus loin.
>
> **Cadre juridique :** L'investigation s'inscrit dans la réponse à incident de l'entreprise. Énergis est victime d'une tentative d'attaque par ransomware. L'analyste CTI est légitime à mener des recherches en source ouverte pour comprendre la menace, informer la direction, et préparer le dépôt de plainte.
>
> **Limites :** Samira peut consulter les forums (sans interagir), analyser la blockchain publique, interroger les bases de données CTI et OSINT. Elle ne peut pas créer de faux profils, interagir avec les acteurs, ni tenter d'accéder aux systèmes des attaquants. Pour les données nécessitant des réquisitions (identité derrière un compte Telegram, titulaire d'un compte crypto sur un exchange KYC, logs de connexion de l'hébergeur), il faudra articuler avec les forces de l'ordre après le dépôt de plainte.
>
> **DPO :** Samira informe le DPO d'Énergis que l'investigation CTI impliquera le traitement de données personnelles (pseudos, emails, éventuellement identités réelles si identifiées). Le traitement est légitime au titre de l'intérêt vital de l'entreprise (article 6.1.f du RGPD), avec conservation limitée à la durée de l'investigation et de la procédure judiciaire.

---

### Chapitre 5 — Outils et méthodologie de cartographie

#### 5.1 Maltego — le graphe relationnel automatisé

Maltego est la plateforme de référence pour la cartographie relationnelle en CTI et OSINT. Développé par Maltego Technologies GmbH (Munich), il est utilisé aussi bien par les équipes CTI d'entreprise que par les forces de l'ordre et les services de renseignement.

**Fonctionnement.** Maltego repose sur un concept central : les transforms. Une transform est un module de requête qui prend une entité en entrée (un domaine, une IP, un email, un pseudo, un hash de malware) et produit des entités liées en sortie (les sous-domaines d'un domaine, les IP associées, les autres domaines enregistrés avec le même email, etc.). L'analyste construit son graphe en enchaînant les transforms : il entre un point de départ, lance les transforms pertinentes, et le graphe s'enrichit automatiquement.

Les transforms disponibles dépendent des data partners intégrés : Maltego propose en standard des transforms pour DNS, WHOIS, Shodan, VirusTotal, Have I Been Pwned, et de nombreuses autres sources. Des transforms spécialisées sont disponibles pour des sources premium (DomainTools, Recorded Future, Censys, BuiltWith, etc.). En 2025-2026, Maltego a élargi sa plateforme vers un modèle intégré : Maltego Graph (le graphe desktop classique et sa version navigateur), Maltego Search (OSINT rapide), Maltego Monitor (surveillance de réseaux sociaux), et Maltego Evidence (collecte et préservation de preuves numériques).

**Tarification.** Le plan Basic est gratuit mais limité (200 crédits mensuels, accès restreint aux transforms). Le plan Entry est orienté individuel. Le plan Professional coûte environ 6 600 dollars/an et donne accès à l'ensemble des transforms commerciales et aux fonctionnalités collaboratives. Le plan Organization (tarif sur devis) est destiné aux équipes et intègre des fonctionnalités d'entreprise. Pour les forces de l'ordre et les entités gouvernementales, un plan Basic+ gratuit est disponible sur demande avec une adresse email officielle.

**Forces :** automatisation de l'enrichissement, visualisation immédiate du graphe, écosystème de transforms extensible, collaboration entre analystes, intégration avec de nombreuses sources de données.

**Limites :** les résultats des transforms sont bruts et nécessitent une validation humaine systématique (un transform peut retourner des faux positifs ou des données obsolètes), les transforms premium sont coûteuses (chaque data partner a sa propre tarification), la qualité du résultat dépend directement de la qualité des sources interrogées, et le graphe peut devenir rapidement illisible avec trop d'entités sans nettoyage régulier.

> **Bonne pratique :** Ne jamais lancer toutes les transforms d'un coup sur une entité (le « Run All Transforms » est le piège du débutant). Choisir les transforms pertinentes en fonction de la question analytique. Valider chaque résultat avant de pivoter dessus. Un graphe Maltego est un outil exploratoire, pas un verdict.

#### 5.2 Gephi — l'analyse de réseau avancée

Gephi est un logiciel open source d'analyse et de visualisation de réseaux, particulièrement adapté aux grands jeux de données que Maltego gère difficilement.

**Quand utiliser Gephi plutôt que Maltego :** lorsque le graphe dépasse plusieurs centaines de nœuds et que l'analyse visuelle dans Maltego devient confuse, lorsque l'objectif est de calculer des métriques de réseau formelles (centralité, betweenness, détection de communautés, densité), ou lorsque l'analyste veut produire des visualisations publication-ready avec un contrôle fin sur le layout et le style.

**Fonctionnement.** Gephi importe des données structurées (fichiers CSV de nœuds et d'arêtes, fichiers GEXF, GraphML, ou export depuis Maltego) et permet d'appliquer des algorithmes de layout (ForceAtlas2 est le plus courant pour les réseaux sociaux et criminels, Yifan Hu pour les très grands graphes), de calculer des métriques (degree centrality pour les hubs, betweenness centrality pour les brokers, modularity pour la détection de communautés), et de filtrer visuellement (par attribut, par métrique, par composante connectée).

**Forces :** gratuit et open source, puissant sur les grands graphes (des dizaines de milliers de nœuds), calcul de métriques statistiques, visualisation sophistiquée.

**Limites :** pas d'enrichissement automatique (contrairement à Maltego, Gephi ne va pas chercher de données — il analyse des données déjà collectées), courbe d'apprentissage non négligeable, interface moins intuitive que Maltego pour l'investigation interactive, développement ralenti ces dernières années (la communauté reste active mais les mises à jour majeures sont rares).

#### 5.3 Obsidian et i2 Analyst's Notebook — la structuration de la connaissance

**Obsidian** est un outil de notes liées (knowledge graph) de plus en plus utilisé par les analystes CTI pour structurer leur investigation en cours de route. Chaque note est un fichier Markdown, les notes se lient entre elles par des liens wiki, et le graphe de connaissances qui en résulte permet de naviguer visuellement entre les entités, les observations, et les hypothèses.

L'avantage d'Obsidian pour l'investigation CTI est la flexibilité : l'analyste peut créer une note par entité (une note pour kr0n0s_ops, une pour l'hébergeur moldave, une pour le wallet Bitcoin), ajouter des métadonnées (tags, dates, niveaux de confiance), et relier les notes au fil de l'investigation. Le graphe Obsidian sert de « mémoire structurée » de l'investigation — complémentaire au graphe Maltego qui est l'outil d'exploration. Obsidian est gratuit pour un usage personnel, avec un abonnement pour la synchronisation et les fonctionnalités collaboratives.

**i2 Analyst's Notebook** (IBM) est la référence historique dans les forces de l'ordre et les services de renseignement pour la production analytique formelle. Il permet de construire des graphes relationnels, des chronologies, et des analyses de flux financiers avec un formalisme rigoureux et une production de rapports « court-ready » (acceptables comme pièces dans une procédure judiciaire). L'outil est commercial et son coût est significatif (plusieurs milliers d'euros par licence), ce qui le réserve principalement aux organisations institutionnelles.

**Alternatives et compléments :** yEd (gratuit, pour des graphes simples et des organigrammes), draw.io/diagrams.net (gratuit, en ligne, pour des schémas rapides), Miro ou Excalidraw (pour le brainstorming visuel collaboratif), et les notebooks Jupyter avec NetworkX (pour l'analyse programmatique en Python).

#### 5.4 Outils blockchain

L'analyse des flux financiers en cryptomonnaie est une composante essentielle de la cartographie d'écosystèmes criminels. Les outils se répartissent en deux catégories : les outils gratuits ou à faible coût accessibles aux analystes, et les plateformes professionnelles utilisées par les forces de l'ordre et les institutions financières.

**Outils accessibles.** OXT.me est un explorateur Bitcoin avancé et gratuit qui permet de visualiser les transactions, les clusters d'adresses, et les flux. Il est particulièrement utile pour le traçage initial d'un wallet Bitcoin. Etherscan (Ethereum) et les explorateurs équivalents pour d'autres chaînes (Polygonscan, BSCScan, Solscan) permettent de suivre les transactions sur leurs blockchains respectives. Arkham Intelligence propose une plateforme de surveillance blockchain avec des fonctionnalités d'attribution (identification des wallets associés à des entités connues) avec un modèle freemium.

**Plateformes professionnelles.** Chainalysis Reactor est la plateforme dominante, utilisée par plus de 800 agences gouvernementales dans environ 70 pays. Elle offre une base d'attribution couvrant plus de 5 milliards de clusters d'adresses, un traçage cross-chain (27+ blockchains, 300+ bridges et DEX, mixing/demixing), et des fonctionnalités d'investigation graphique avancées. Le coût est significatif (plusieurs dizaines de milliers de dollars/an) et la plateforme est principalement accessible aux institutions. TRM Labs, Elliptic, et Crystal Intelligence (anciennement Crystal Blockchain, acquis par Tether/Bitfinex en 2025) sont les principaux concurrents, chacun avec des spécialisations différentes (TRM sur la forensics réglementaire, Elliptic sur la conformité AML, Crystal sur l'analyse investigative avec un focus Europe de l'Est).

**Limites communes.** Tous ces outils reposent sur des heuristiques de clustering qui ont des limites connues (voir Ch.10 sur les objets financiers). Le traçage cross-chain (quand les fonds passent d'une blockchain à une autre via un bridge ou un DEX) est encore imparfait. Les privacy coins (Monero en premier lieu) restent largement résistantes au traçage, bien que des progrès aient été réalisés. Les résultats doivent toujours être considérés comme des indicateurs, pas comme des preuves — l'attribution finale nécessite des données off-chain (données KYC des exchanges obtenues par réquisition judiciaire).

#### 5.5 Outils OSINT applicables

Sans reproduire le contenu d'un cours OSINT dédié, il est utile de rappeler les techniques OSINT spécifiquement pertinentes pour la cartographie d'écosystèmes cybercriminels.

**WHOIS historique** (DomainTools, SecurityTrails, WhoisXMLAPI) : les données WHOIS courantes sont presque toujours masquées, mais les données historiques peuvent révéler des erreurs OPSEC passées — un email réel, un nom, une organisation. **Certificate Transparency** (crt.sh, Censys) : les certificats SSL/TLS émis pour un domaine sont publics et historisés. Ils peuvent révéler des sous-domaines cachés, des certificats wildcard partagés entre domaines, et des patterns d'infrastructure. **Recherche de pseudos** (Sherlock, Namechk, WhatsMyName) : vérifier si un pseudo apparaît sur d'autres plateformes (réseaux sociaux, GitHub, forums). **Bases de données de breaches** (DeHashed, IntelX, Snusbase) : vérifier si un email ou un pseudo apparaît dans des fuites de données, ce qui peut révéler des mots de passe (utiles pour comprendre les habitudes de l'acteur), des adresses IP de connexion, des données personnelles. **Shodan/Censys** : scanner les IP identifiées pour trouver des services exposés (panels C2, interfaces d'administration, services mal configurés). **Google Dorks** : recherches avancées sur le web visible pour trouver des fichiers, des configurations, ou des pages liées à l'infrastructure identifiée.

#### 5.6 Workflow type — le processus en 7 étapes

L'expérience de terrain permet de formaliser un workflow récurrent de cartographie d'écosystème, en 7 étapes séquentielles mais itératives (l'analyste revient souvent en arrière).

**Étape 1 — Point d'entrée.** L'investigation commence par un artefact concret : un IoC (hash, domaine, IP), un pseudo, un wallet, un rapport de threat intel, une plainte client. Ce point d'entrée détermine la direction initiale de l'exploration.

**Étape 2 — Enrichissement automatique.** L'analyste utilise Maltego (ou des outils équivalents) pour enrichir automatiquement le point d'entrée : résolution DNS, WHOIS, reverse IP, Certificate Transparency, VirusTotal, etc. Cette étape produit un graphe brut avec de nombreux nœuds non qualifiés.

**Étape 3 — Pivot manuel.** L'analyste examine les résultats de l'enrichissement, identifie les nœuds les plus prometteurs, et effectue des recherches manuelles ciblées : recherche du pseudo sur les forums et Telegram, analyse du wallet sur les explorateurs blockchain, vérification de l'email dans les bases de breaches.

**Étape 4 — Structuration.** Les données collectées sont structurées : les entités sont typées et nommées, les relations sont qualifiées (type, force, confiance), les métadonnées de source sont ajoutées. Le journal de collecte est mis à jour.

**Étape 5 — Corrélation.** L'analyste cherche les liens entre les entités identifiées : même infrastructure partagée, même pseudo réutilisé, même wallet recevant des fonds, même pattern temporel. C'est l'étape la plus critique et la plus exposée aux faux positifs (voir Ch.12).

**Étape 6 — Interprétation.** L'analyste formule des hypothèses sur la structure et le fonctionnement de l'écosystème, en distinguant faits, estimations, et suppositions. Les hypothèses concurrentes sont documentées. Les niveaux de confiance sont attribués.

**Étape 7 — Rapport.** Les résultats sont formalisés dans une note d'analyse adaptée au destinataire (CERT, direction, autorités). Le graphe est simplifié pour la communication. Les recommandations sont formulées. Le processus de production du rapport est détaillé au Ch.28.

#### 5.7 Fil rouge — NEXUS : initialisation du graphe

> **🔍 NEXUS — Épisode 5**
>
> Samira initialise son graphe Maltego avec trois points d'entrée : le domaine C2 `update-srv-infra[.]xyz`, l'IP associée `185.234.xx.xx`, et le hash SHA256 du sample de malware.
>
> Elle lance les transforms ciblés (pas de « Run All »). Les résultats :
> - **DNS/Reverse IP :** 4 domaines supplémentaires sur la même IP, dont `phantom-news[.]press` (un blog), `phcrypt-panel[.]xyz` (un sous-domaine évoquant un panel de contrôle), et deux domaines apparemment inactifs.
> - **Certificate Transparency (crt.sh) :** un certificat wildcard `*.phantom-infra[.]xyz` couvre le domaine C2 et le panel. Ce certificat partagé est un lien technique fort — voir Ch.11.
> - **WHOIS historique (DomainTools) :** l'email `kr0n0s-ops@proton.me` apparaît sur un snapshot WHOIS vieux de 4 mois pour le domaine C2. C'est une erreur OPSEC classique : le registrant a utilisé un service de privacy par la suite, mais l'historique conserve la trace.
> - **VirusTotal :** le hash du malware est associé à 3 autres domaines C2 dans des rapports communautaires, tous liés à la famille PhantomCrypt.
>
> Le graphe compte maintenant 12 nœuds et 15 arêtes. Samira passe au pivot manuel : elle recherche l'email `kr0n0s-ops@proton.me` dans DeHashed.
>
> **Résultat :** l'email apparaît dans une breach d'un forum underground (XSS) datant de 2023. Le compte associé utilise le pseudo `kr0n0s_ops`. La piste identitaire est ouverte.

---
