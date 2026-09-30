---
title: Chapitre 5 — Outils et méthodologie de cartographie
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - 'Partie I — Fondations : penser en écosystème'
  - index.md
---

## 5.1 Maltego — le graphe relationnel automatisé

Maltego est la plateforme de référence pour la cartographie relationnelle en CTI et OSINT. Développé par Maltego Technologies GmbH (Munich), il est utilisé aussi bien par les équipes CTI d'entreprise que par les forces de l'ordre et les services de renseignement.

**Fonctionnement.** Maltego repose sur un concept central : les transforms. Une transform est un module de requête qui prend une entité en entrée (un domaine, une IP, un email, un pseudo, un hash de malware) et produit des entités liées en sortie (les sous-domaines d'un domaine, les IP associées, les autres domaines enregistrés avec le même email, etc.). L'analyste construit son graphe en enchaînant les transforms : il entre un point de départ, lance les transforms pertinentes, et le graphe s'enrichit automatiquement.

Les transforms disponibles dépendent des data partners intégrés : Maltego propose en standard des transforms pour DNS, WHOIS, Shodan, VirusTotal, Have I Been Pwned, et de nombreuses autres sources. Des transforms spécialisées sont disponibles pour des sources premium (DomainTools, Recorded Future, Censys, BuiltWith, etc.). En 2025-2026, Maltego a élargi sa plateforme vers un modèle intégré : Maltego Graph (le graphe desktop classique et sa version navigateur), Maltego Search (OSINT rapide), Maltego Monitor (surveillance de réseaux sociaux), et Maltego Evidence (collecte et préservation de preuves numériques).

**Tarification.** Le plan Basic est gratuit mais limité (200 crédits mensuels, accès restreint aux transforms). Le plan Entry est orienté individuel. Le plan Professional coûte environ 6 600 dollars/an et donne accès à l'ensemble des transforms commerciales et aux fonctionnalités collaboratives. Le plan Organization (tarif sur devis) est destiné aux équipes et intègre des fonctionnalités d'entreprise. Pour les forces de l'ordre et les entités gouvernementales, un plan Basic+ gratuit est disponible sur demande avec une adresse email officielle.

**Forces :** automatisation de l'enrichissement, visualisation immédiate du graphe, écosystème de transforms extensible, collaboration entre analystes, intégration avec de nombreuses sources de données.

**Limites :** les résultats des transforms sont bruts et nécessitent une validation humaine systématique (un transform peut retourner des faux positifs ou des données obsolètes), les transforms premium sont coûteuses (chaque data partner a sa propre tarification), la qualité du résultat dépend directement de la qualité des sources interrogées, et le graphe peut devenir rapidement illisible avec trop d'entités sans nettoyage régulier.

> **Bonne pratique :** Ne jamais lancer toutes les transforms d'un coup sur une entité (le « Run All Transforms » est le piège du débutant). Choisir les transforms pertinentes en fonction de la question analytique. Valider chaque résultat avant de pivoter dessus. Un graphe Maltego est un outil exploratoire, pas un verdict.

## 5.2 Gephi — l'analyse de réseau avancée

Gephi est un logiciel open source d'analyse et de visualisation de réseaux, particulièrement adapté aux grands jeux de données que Maltego gère difficilement.

**Quand utiliser Gephi plutôt que Maltego :** lorsque le graphe dépasse plusieurs centaines de nœuds et que l'analyse visuelle dans Maltego devient confuse, lorsque l'objectif est de calculer des métriques de réseau formelles (centralité, betweenness, détection de communautés, densité), ou lorsque l'analyste veut produire des visualisations publication-ready avec un contrôle fin sur le layout et le style.

**Fonctionnement.** Gephi importe des données structurées (fichiers CSV de nœuds et d'arêtes, fichiers GEXF, GraphML, ou export depuis Maltego) et permet d'appliquer des algorithmes de layout (ForceAtlas2 est le plus courant pour les réseaux sociaux et criminels, Yifan Hu pour les très grands graphes), de calculer des métriques (degree centrality pour les hubs, betweenness centrality pour les brokers, modularity pour la détection de communautés), et de filtrer visuellement (par attribut, par métrique, par composante connectée).

**Forces :** gratuit et open source, puissant sur les grands graphes (des dizaines de milliers de nœuds), calcul de métriques statistiques, visualisation sophistiquée.

**Limites :** pas d'enrichissement automatique (contrairement à Maltego, Gephi ne va pas chercher de données — il analyse des données déjà collectées), courbe d'apprentissage non négligeable, interface moins intuitive que Maltego pour l'investigation interactive, développement ralenti ces dernières années (la communauté reste active mais les mises à jour majeures sont rares).

## 5.3 Obsidian et i2 Analyst's Notebook — la structuration de la connaissance

**Obsidian** est un outil de notes liées (knowledge graph) de plus en plus utilisé par les analystes CTI pour structurer leur investigation en cours de route. Chaque note est un fichier Markdown, les notes se lient entre elles par des liens wiki, et le graphe de connaissances qui en résulte permet de naviguer visuellement entre les entités, les observations, et les hypothèses.

L'avantage d'Obsidian pour l'investigation CTI est la flexibilité : l'analyste peut créer une note par entité (une note pour kr0n0s_ops, une pour l'hébergeur moldave, une pour le wallet Bitcoin), ajouter des métadonnées (tags, dates, niveaux de confiance), et relier les notes au fil de l'investigation. Le graphe Obsidian sert de « mémoire structurée » de l'investigation — complémentaire au graphe Maltego qui est l'outil d'exploration. Obsidian est gratuit pour un usage personnel, avec un abonnement pour la synchronisation et les fonctionnalités collaboratives.

**i2 Analyst's Notebook** (IBM) est la référence historique dans les forces de l'ordre et les services de renseignement pour la production analytique formelle. Il permet de construire des graphes relationnels, des chronologies, et des analyses de flux financiers avec un formalisme rigoureux et une production de rapports « court-ready » (acceptables comme pièces dans une procédure judiciaire). L'outil est commercial et son coût est significatif (plusieurs milliers d'euros par licence), ce qui le réserve principalement aux organisations institutionnelles.

**Alternatives et compléments :** yEd (gratuit, pour des graphes simples et des organigrammes), draw.io/diagrams.net (gratuit, en ligne, pour des schémas rapides), Miro ou Excalidraw (pour le brainstorming visuel collaboratif), et les notebooks Jupyter avec NetworkX (pour l'analyse programmatique en Python).

## 5.4 Outils blockchain

L'analyse des flux financiers en cryptomonnaie est une composante essentielle de la cartographie d'écosystèmes criminels. Les outils se répartissent en deux catégories : les outils gratuits ou à faible coût accessibles aux analystes, et les plateformes professionnelles utilisées par les forces de l'ordre et les institutions financières.

**Outils accessibles.** OXT.me est un explorateur Bitcoin avancé et gratuit qui permet de visualiser les transactions, les clusters d'adresses, et les flux. Il est particulièrement utile pour le traçage initial d'un wallet Bitcoin. Etherscan (Ethereum) et les explorateurs équivalents pour d'autres chaînes (Polygonscan, BSCScan, Solscan) permettent de suivre les transactions sur leurs blockchains respectives. Arkham Intelligence propose une plateforme de surveillance blockchain avec des fonctionnalités d'attribution (identification des wallets associés à des entités connues) avec un modèle freemium.

**Plateformes professionnelles.** Chainalysis Reactor est la plateforme dominante, utilisée par plus de 800 agences gouvernementales dans environ 70 pays. Elle offre une base d'attribution couvrant plus de 5 milliards de clusters d'adresses, un traçage cross-chain (27+ blockchains, 300+ bridges et DEX, mixing/demixing), et des fonctionnalités d'investigation graphique avancées. Le coût est significatif (plusieurs dizaines de milliers de dollars/an) et la plateforme est principalement accessible aux institutions. TRM Labs, Elliptic, et Crystal Intelligence (anciennement Crystal Blockchain, acquis par Tether/Bitfinex en 2025) sont les principaux concurrents, chacun avec des spécialisations différentes (TRM sur la forensics réglementaire, Elliptic sur la conformité AML, Crystal sur l'analyse investigative avec un focus Europe de l'Est).

**Limites communes.** Tous ces outils reposent sur des heuristiques de clustering qui ont des limites connues (voir Ch.10 sur les objets financiers). Le traçage cross-chain (quand les fonds passent d'une blockchain à une autre via un bridge ou un DEX) est encore imparfait. Les privacy coins (Monero en premier lieu) restent largement résistantes au traçage, bien que des progrès aient été réalisés. Les résultats doivent toujours être considérés comme des indicateurs, pas comme des preuves — l'attribution finale nécessite des données off-chain (données KYC des exchanges obtenues par réquisition judiciaire).

## 5.5 Outils OSINT applicables

Sans reproduire le contenu d'un cours OSINT dédié, il est utile de rappeler les techniques OSINT spécifiquement pertinentes pour la cartographie d'écosystèmes cybercriminels.

**WHOIS historique** (DomainTools, SecurityTrails, WhoisXMLAPI) : les données WHOIS courantes sont presque toujours masquées, mais les données historiques peuvent révéler des erreurs OPSEC passées — un email réel, un nom, une organisation. **Certificate Transparency** (crt.sh, Censys) : les certificats SSL/TLS émis pour un domaine sont publics et historisés. Ils peuvent révéler des sous-domaines cachés, des certificats wildcard partagés entre domaines, et des patterns d'infrastructure. **Recherche de pseudos** (Sherlock, Namechk, WhatsMyName) : vérifier si un pseudo apparaît sur d'autres plateformes (réseaux sociaux, GitHub, forums). **Bases de données de breaches** (DeHashed, IntelX, Snusbase) : vérifier si un email ou un pseudo apparaît dans des fuites de données, ce qui peut révéler des mots de passe (utiles pour comprendre les habitudes de l'acteur), des adresses IP de connexion, des données personnelles. **Shodan/Censys** : scanner les IP identifiées pour trouver des services exposés (panels C2, interfaces d'administration, services mal configurés). **Google Dorks** : recherches avancées sur le web visible pour trouver des fichiers, des configurations, ou des pages liées à l'infrastructure identifiée.

## 5.6 Workflow type — le processus en 7 étapes

L'expérience de terrain permet de formaliser un workflow récurrent de cartographie d'écosystème, en 7 étapes séquentielles mais itératives (l'analyste revient souvent en arrière).

**Étape 1 — Point d'entrée.** L'investigation commence par un artefact concret : un IoC (hash, domaine, IP), un pseudo, un wallet, un rapport de threat intel, une plainte client. Ce point d'entrée détermine la direction initiale de l'exploration.

**Étape 2 — Enrichissement automatique.** L'analyste utilise Maltego (ou des outils équivalents) pour enrichir automatiquement le point d'entrée : résolution DNS, WHOIS, reverse IP, Certificate Transparency, VirusTotal, etc. Cette étape produit un graphe brut avec de nombreux nœuds non qualifiés.

**Étape 3 — Pivot manuel.** L'analyste examine les résultats de l'enrichissement, identifie les nœuds les plus prometteurs, et effectue des recherches manuelles ciblées : recherche du pseudo sur les forums et Telegram, analyse du wallet sur les explorateurs blockchain, vérification de l'email dans les bases de breaches.

**Étape 4 — Structuration.** Les données collectées sont structurées : les entités sont typées et nommées, les relations sont qualifiées (type, force, confiance), les métadonnées de source sont ajoutées. Le journal de collecte est mis à jour.

**Étape 5 — Corrélation.** L'analyste cherche les liens entre les entités identifiées : même infrastructure partagée, même pseudo réutilisé, même wallet recevant des fonds, même pattern temporel. C'est l'étape la plus critique et la plus exposée aux faux positifs (voir Ch.12).

**Étape 6 — Interprétation.** L'analyste formule des hypothèses sur la structure et le fonctionnement de l'écosystème, en distinguant faits, estimations, et suppositions. Les hypothèses concurrentes sont documentées. Les niveaux de confiance sont attribués.

**Étape 7 — Rapport.** Les résultats sont formalisés dans une note d'analyse adaptée au destinataire (CERT, direction, autorités). Le graphe est simplifié pour la communication. Les recommandations sont formulées. Le processus de production du rapport est détaillé au Ch.28.

## 5.7 Fil rouge — NEXUS : initialisation du graphe

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
