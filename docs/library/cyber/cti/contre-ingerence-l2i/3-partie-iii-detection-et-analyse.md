---
title: PARTIE III — DÉTECTION ET ANALYSE
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
chapter: 3
chapters: 7
---

---

## Chapitre 12 — Méthodologie de détection : du signal faible à la qualification

### 12.1 Les trois niveaux de détection

La détection des opérations d'influence s'organise en trois niveaux de profondeur croissante.

Le **monitoring automatisé** constitue le premier filtre. Il repose sur des systèmes de surveillance qui détectent des anomalies quantitatives : pics de volume sur un sujet donné, création massive de comptes, émergence d'URLs vers des domaines nouveaux, ratios d'engagement incohérents. Le Datalab de VIGINUM (8 agents, docteurs et ingénieurs en sciences des données et intelligence artificielle) a développé des algorithmes spécifiques pour détecter les bots, les images probablement artificielles, les contenus proches sémantiquement (traduction, copy-pasta, reformulation automatisée) et identifier automatiquement les thématiques des contenus. En 2024, ce système a permis de détecter 259 phénomènes inauthentiques. Le monitoring automatisé produit des alertes, pas des qualifications — chaque alerte doit être triée par un analyste.

Le **triage analytique** est la qualification humaine des alertes. L'analyste évalue si le phénomène détecté correspond à une opération d'influence coordonnée ou à un phénomène organique (mobilisation authentique, buzz commercial, spam non politique). Le triage repose sur l'application des critères de qualification — VIGINUM utilise les quatre critères d'ingérence numérique étrangère comme grille de tri. Le triage est le moment le plus critique pour éviter les faux positifs : une mobilisation organique intense peut présenter des caractéristiques similaires à une opération coordonnée (publication dans des fenêtres temporelles serrées, messages similaires, hashtags communs).

L'**investigation approfondie** est déclenchée quand le triage produit une qualification « probable » ou « possible ». Elle mobilise des techniques OSINT avancées (analyse d'infrastructure, analyse de réseau, analyse narrative), potentiellement du renseignement complémentaire, et vise l'attribution technique et la cartographie complète de l'opération.

### 12.2 Le modèle de qualification VIGINUM

VIGINUM a développé un modèle de qualification structuré autour des quatre critères réglementaires d'une INE, mais enrichi de critères opérationnels qui permettent de graduer la confiance dans la qualification.

Les **critères cumulatifs** sont : un contenu manifestement inexact ou trompeur, une diffusion artificielle ou automatisée massive et délibérée, une atteinte potentielle aux intérêts fondamentaux de la Nation, et l'implication directe ou indirecte d'un acteur étranger. Les quatre critères doivent être réunis pour qualifier une INE.

En pratique, le critère d'**implication étrangère** est souvent le plus difficile à établir avec certitude. Un réseau de comptes inauthentiques diffusant des contenus trompeurs avant une élection peut être une opération étrangère ou une opération politique domestique. La distinction conditionne le périmètre d'intervention et les moyens mobilisables — VIGINUM n'est compétent que pour les ingérences étrangères, pas pour les manipulations domestiques de l'information.

### 12.3 Sources de signalement

Les signalements proviennent de sources multiples : la détection interne (monitoring automatisé), les **plateformes** (Transparency Reports, signalements proactifs — de qualité variable selon les plateformes), la **société civile** (fact-checkers, chercheurs académiques, ONG spécialisées comme EU DisinfoLab, DFRLab, Graphika), les **services de renseignement** (qui peuvent fournir des éléments classifiés corroborant l'implication étrangère), les **partenaires européens et internationaux** (EEAS, homologues nationaux), et les **signalements citoyens** (qui nécessitent un filtrage important mais constituent parfois la première alerte).

La coopération inter-agences est un facteur clé d'efficacité. Le rapport d'activité 2024 de VIGINUM souligne les échanges opérationnels avec de nombreux fournisseurs de plateformes (X, Google, YouTube, Facebook, Instagram, TikTok, Bluesky), ainsi que la coopération avec l'ARCOM, le MEAE et la Commission européenne.

### 12.4 La difficulté de qualification : faux positifs et zones grises

Les **faux positifs** sont un risque structurel de la détection. Une mobilisation citoyenne organique autour d'un événement peut présenter des caractéristiques d'une opération coordonnée : publication massive dans un temps court, messages similaires (slogans, mots d'ordre), utilisation de hashtags communs. L'analyste doit distinguer la coordination organique (des citoyens qui réagissent de manière similaire à un événement) de la coordination inauthentique (des comptes opérés par un acteur central).

Les **zones grises** sont encore plus problématiques. Un narratif amplifié par un État étranger mais aussi porté par des citoyens authentiques ne peut pas être réduit à une opération d'influence pure — il reflète aussi un débat public réel. Le cas des Gilets Jaunes est illustratif : une amplification documentée par des acteurs étrangers (notamment russes) ne signifie pas que le mouvement était une opération d'influence — il s'agissait d'un mouvement social organique dont certains narratifs ont été amplifiés de l'extérieur. La qualification doit refléter cette nuance.

### 12.5 Grammaire de la prudence attributive et niveaux de confiance

L'un des risques majeurs du domaine est la **sur-attribution** — voir une main étrangère derrière tout phénomène informationnel suspect. Le risque inverse, la **sous-qualification**, existe aussi mais ses conséquences sont généralement moins dommageables.

La prudence attributive repose sur une grammaire explicite de niveaux de confiance qui doit être systématiquement utilisée dans les analyses et les rapports. Cette grammaire distingue plusieurs niveaux.

L'**indicateur** est un élément observable isolé (un compte a été créé récemment, une URL pointe vers un domaine nouveau). Un indicateur ne prouve rien en soi — il oriente l'investigation.

Le **signal faible** est un indicateur qui, dans un contexte donné, suggère une hypothèse. Plusieurs signaux faibles convergents renforcent l'hypothèse mais ne la démontrent pas.

Le **faisceau d'indices** est un ensemble de signaux convergents, suffisamment cohérents pour qualifier une hypothèse comme « plausible » ou « probable ». C'est le niveau à partir duquel une investigation approfondie est justifiée.

L'**hypothèse analytique** est une interprétation structurée des indices disponibles. Elle doit être formulée comme une hypothèse (« les éléments disponibles sont cohérents avec une opération coordonnée impliquant un acteur étranger ») et non comme un fait établi.

L'**attribution technique** est l'identification des moyens techniques utilisés (infrastructure, comptes, outils). Elle peut être solide sans que l'attribution stratégique (qui a commandité ?) soit établie.

L'**attribution publique** est une décision politique, pas seulement technique — elle dépend du niveau de confiance, du contexte diplomatique, et de l'évaluation des conséquences de la publication (Ch.16).

Les **niveaux de confiance** doivent être systématiquement explicités : **confiance faible** (les éléments sont compatibles avec l'hypothèse mais des explications alternatives sont plausibles), **confiance modérée** (les éléments convergent vers l'hypothèse mais certains éléments manquent ou sont ambigus), **haute confiance** (les éléments convergent de manière robuste, les explications alternatives sont peu plausibles). Le vocabulaire de restitution doit refléter ces niveaux : « plausible », « cohérent avec », « compatible avec », « probable », « vraisemblable », « non démontré mais cohérent avec les TTPs de... », « incompatible avec l'hypothèse de... ».

Le rapport VIGINUM sur Storm-1516 illustre cette rigueur : « Si l'impact réel du mode opératoire sur le débat public numérique demeure difficile à estimer, VIGINUM observe que de nombreux narratifs propagés via le MOI ont atteint une visibilité très importante en ligne. »

---

## Chapitre 13 — Analyse de réseau : cartographier les opérations coordonnées

### 13.1 Social Network Analysis appliquée aux opérations d'influence

L'analyse de réseau social (SNA — *Social Network Analysis*) est la méthode clé pour cartographier les opérations coordonnées. Elle consiste à construire un graphe d'interactions (qui retweet qui, qui partage les mêmes URLs, qui mentionne qui, qui suit qui) et à analyser sa structure pour identifier des clusters de coordination.

Les métriques classiques de la SNA sont directement exploitables : la **centralité** (quels comptes sont au centre du réseau de diffusion — les amplificateurs clés), la **densité** (un réseau inauthentique est typiquement plus dense qu'un réseau organique — les faux comptes interagissent davantage entre eux), les **communautés** (identification de clusters de comptes qui interagissent préférentiellement entre eux — technique de Louvain, Leiden), et les **bridges** (comptes qui relient le réseau inauthentique à des communautés authentiques — les points de passage du fringe au mainstream).

Dans le cadre d'une opération d'influence, l'analyse de réseau vise à répondre à trois questions : le réseau présente-t-il des caractéristiques de coordination inauthentique (synchronicité, densité, homogénéité) ? Quel est le noyau central (les comptes « amplificateurs » qui structurent la diffusion) ? Quels sont les points de contact avec les communautés organiques (les « bridges » par lesquels le narratif pénètre le débat authentique) ?

### 13.2 Analyse temporelle

L'analyse temporelle est souvent le marqueur le plus discriminant. La détection de synchronicité — publications à quelques minutes d'intervalle dans des fenêtres anormalement serrées — est un indicateur fort de coordination. L'analyse des horaires d'activité peut révéler des incohérences avec le fuseau horaire affiché (un réseau de comptes prétendument français publiant aux horaires de bureau de Moscou). Les pics de volume coordonnés, superposés à la timeline des événements, permettent de reconstituer le cycle opérationnel de l'opération.

### 13.3 Analyse d'infrastructure

L'analyse technique des URLs partagées et des domaines associés mobilise les mêmes techniques que l'OSINT technique classique. L'analyse Whois (historique et actuelle), le reverse IP, les certificats SSL, l'analyse de l'hébergeur, les records DNS, et l'analyse des patterns d'enregistrement (même registrar, mêmes données de contact, même serveur) permettent d'identifier l'infrastructure sous-jacente.

Le rapport VIGINUM sur Storm-1516 illustre cette approche : les opérateurs de CopyCop utilisent des services d'anonymisation de Cloudflare, des hébergeurs peu discriminants, et des templates WordPress quasi systématiquement différents pour gêner la détection. Malgré ces précautions, l'analyse d'infrastructure a permis d'identifier des liens entre les différents sites du réseau.

La doctrine OpenCTI de VIGINUM documente l'utilisation d'observables spécifiques (adresses email, adresses IP, médias, URLs, noms de domaine) pour tracer l'infrastructure des opérations informationnelles et les relier à des acteurs identifiés.

### 13.4 Outils

Le paysage d'outils pour l'analyse de réseau a significativement évolué entre 2023 et 2026, principalement du fait des restrictions d'accès aux données des plateformes.

**Gephi** reste la référence open source pour la visualisation et l'analyse de graphes — gratuit, puissant, mais avec une courbe d'apprentissage significative et des limites de performance sur les très grands graphes. **NodeXL** (Microsoft Excel plugin) est adapté pour des analyses de taille modérée avec une interface plus accessible. **Graphistry** offre des capacités de visualisation GPU-accelerée pour les graphes massifs. **Maltego** est utilisé pour l'enrichissement et la visualisation des données d'investigation.

**CrowdTangle**, l'outil de Meta pour le suivi de la diffusion sur Facebook et Instagram, a été fermé en août 2024 et remplacé par la **Meta Content Library** — dont l'accès est restreint aux chercheurs qualifiés et dont les fonctionnalités sont plus limitées. Cette fermeture a significativement dégradé les capacités de monitoring pour l'ensemble de la communauté.

**Botometer** (Indiana University) évalue la probabilité qu'un compte Twitter/X soit un bot — mais ses performances sont connues pour être limitées (taux de faux positifs et faux négatifs significatifs) et il ne doit jamais être utilisé comme verdict autonome.

Les **APIs des plateformes** sont de plus en plus restreintes. L'API de X (ex-Twitter) est devenue payante et coûteuse depuis 2023, ce qui a sévèrement limité les capacités de recherche académique et opérationnelle. Le DSA impose un accès aux données pour les chercheurs agréés, mais la mise en œuvre effective reste lente et difficile.

### 13.5 Visualisation et restitution

La présentation des résultats d'analyse de réseau à un décideur non technique est un enjeu opérationnel majeur. Un graphe de réseau brut est incompréhensible pour un non-spécialiste. La restitution doit inclure : un graphe simplifié et annoté (avec les clusters identifiés, les nœuds centraux étiquetés, les connexions clés mises en évidence), une description narrative du réseau (taille, structure, comportements caractéristiques), les indicateurs quantitatifs clés (nombre de comptes, volume de publications, engagement total, fenêtres temporelles), et les conclusions avec niveaux de confiance.

> **🔵 BROUILLARD — Épisode 5**
> La cartographie du réseau est complète. Élise et son équipe ont reconstitué un graphe de relations impliquant plus de 200 comptes X, 50 comptes Facebook, 12 canaux Telegram, 3 sites web de réinformation et une newsletter. L'analyse de réseau identifie un cluster central de 30 comptes « amplificateurs » qui structurent la diffusion — ces comptes sont les premiers à partager les contenus publiés sur les sites de réinformation et les canaux Telegram, et les autres comptes du réseau les retweet dans des fenêtres de 5 à 15 minutes. L'analyse temporelle confirme la coordination : les pics d'activité sont systématiquement synchronisés, avec des horaires d'activité concentrés entre 8h et 17h UTC+3 (Moscou). L'infrastructure des trois sites web est tracée via Whois et reverse IP. Le rapport visuel — graphe annoté, timeline, tableau d'indicateurs — est préparé pour le briefing hebdomadaire.

---

## Chapitre 14 — Analyse narrative, sémantique et évaluation d'impact

### 14.1 Qu'est-ce qu'un narratif

Un narratif n'est pas un message — c'est un **cadre interprétatif**. Il combine un récit (des événements ordonnés dans le temps), des acteurs (protagonistes, antagonistes, victimes), des valeurs (ce qui est bien, ce qui est mal), une charge émotionnelle, et souvent un appel implicite ou explicite à l'action. Le même fait peut être cadré par des narratifs opposés : « la France aide ses alliés africains » vs « la France perpétue une domination néocoloniale ». Le cadre interprétatif détermine la manière dont les faits sont perçus et mémorisés — c'est pourquoi les opérations d'influence investissent massivement dans la construction narrative.

La **distinction entre un narratif et un message** est opérationnellement importante. Un message est un contenu ponctuel (un tweet, un article, une vidéo). Un narratif est une structure persistante qui transcende les messages individuels et leur donne un sens. Une opération d'influence diffuse des centaines de messages, mais ils s'inscrivent typiquement dans un petit nombre de narratifs stratégiques (3 à 5 pour une opération majeure). L'analyse doit identifier les narratifs sous-jacents, pas seulement les messages.

### 14.2 Analyse des narratifs déployés

L'analyse narrative consiste à identifier les **thèmes dominants** (immigration, corruption, politique étrangère, sécurité), les **frames** utilisés (le cadrage interprétatif — « menace » vs « opportunité », « eux » vs « nous »), les **mots-clés stratégiques** et les **oppositions binaires construites**. Storm-1516 déploie typiquement des narratifs autour de deux axes principaux : la décrédibilisation de l'Ukraine et de ses dirigeants (accusations de corruption, de détournement de l'aide occidentale) et le ciblage de personnalités et processus électoraux occidentaux (fausses accusations, deepfakes, contenus anxiogènes liés à l'immigration et au terrorisme).

Le framework DISARM identifie des techniques narratives spécifiques : « Exploiter des récits existants » (T0003) — capitaliser sur des préoccupations réelles plutôt que créer des narratifs de toutes pièces, « Développer des récits contradictoires » (T0004) — polariser en proposant des versions antagonistes, « Exploiter des théories conspirationnistes » (T0022) — s'appuyer sur des communautés complotistes existantes.

### 14.3 La co-optation de narratifs existants et la chaîne fringe → mainstream

L'une des techniques les plus efficaces — et les plus difficiles à détecter — consiste à ne pas créer un narratif ex nihilo mais à **amplifier et orienter des préoccupations réelles**. Un narratif sur le coût de la vie, l'insécurité ou l'immigration n'est pas faux en soi — il reflète des préoccupations authentiques. L'opération d'influence le prend, l'amplifie, le polarise et l'oriente vers une conclusion politique spécifique (méfiance envers les institutions, rejet de l'UE, opposition à l'aide à l'Ukraine).

La **chaîne de passage du fringe au mainstream** est un mécanisme central qui mérite d'être explicitement décrit. Un narratif injecté dans l'espace informationnel parcourt typiquement les étapes suivantes :

1. **Injection** dans un espace marginal (canal Telegram, forum anonyme, faux site d'information)
2. **Reprise par des relais idéologiques** — influenceurs militants, blogs d'opinion, médias alternatifs qui trouvent le narratif utile à leur cause. Ces relais ne sont pas nécessairement partie prenante de l'opération — ils sont souvent sincères mais manipulés
3. **Amplification par des influenceurs semi-authentiques** — personnalités publiques avec une audience significative qui reprennent le narratif par conviction, opportunisme ou simple inattention
4. **Couverture par des médias alternatifs ou pseudo-médias** sous une forme journalistique
5. **Entrée dans le débat mainstream** — soit par la couverture médiatique (même pour contester le narratif), soit par la reprise par des personnalités politiques

À chaque étape, le narratif gagne en crédibilité perçue et perd la trace de son origine. Le « narrative laundering » est analogue au blanchiment d'argent — le contenu « sale » (injection clandestine) est progressivement blanchi par des intermédiaires qui lui confèrent une légitimité apparente.

### 14.4 Analyse sémantique computationnelle

Le NLP (*Natural Language Processing*) appliqué à l'analyse de campagne permet de traiter des volumes de données inaccessibles à l'analyse humaine. Les techniques mobilisées incluent le *topic modeling* (identification automatique des thèmes dominants dans un corpus), le *sentiment analysis* (mesure de la polarité émotionnelle des contenus), l'*entity extraction* (identification des personnes, organisations et lieux mentionnés), et la détection de duplications sémantiques.

VIGINUM a développé et publié sous licence libre la bibliothèque **D3lta**, qui permet de détecter les duplications massives de contenus en distinguant le copy-pasta (forte proximité graphique et sémantique), la reformulation (forte proximité sémantique, moindre proximité graphique, même langue), et la traduction (forte proximité sémantique, moindre proximité graphique, langue différente). Cet outil est directement opérationnel pour identifier les campagnes d'amplification coordonnée.

Les **LLM** sont de plus en plus utilisés comme outils d'analyse (pas de détection) — pour classifier des contenus, identifier des thèmes, résumer de grands volumes de données, et explorer des patterns. Leur utilisation comme outil analytique est prometteuse mais doit intégrer les biais des modèles et ne pas se substituer au jugement humain.

### 14.5 Évaluation d'impact : portée, pénétration et effet réel

L'évaluation de l'impact réel d'une opération d'influence est l'un des défis analytiques les plus difficiles du domaine. Trop d'analyses confondent **visibilité** (combien de personnes ont vu le contenu), **engagement** (combien ont interagi), **pénétration narrative** (combien l'ont intégré dans leur vision du monde) et **effet comportemental** (combien ont modifié leur vote, leur opinion ou leur action).

La **portée** (nombre de vues, d'impressions) est la métrique la plus facile à mesurer mais la moins significative. Un contenu vu par des millions de personnes n'a pas nécessairement modifié la perception de quiconque.

L'**engagement** (likes, partages, commentaires) est un indicateur intermédiaire qui mesure l'activation émotionnelle mais pas la conviction. Un contenu peut être massivement commenté par des personnes qui le contestent.

La **pénétration narrative** — le fait qu'un narratif injecté soit repris et intégré par des communautés authentiques — est un indicateur plus significatif. La transition d'un narratif de l'espace des comptes inauthentiques vers des conversations organiques est un seuil critique. VIGINUM note que des narratifs de Storm-1516 ont atteint « une visibilité très importante en ligne » et ont été « repris, de manière inconsciente ou opportuniste, par des personnalités et des représentants politiques de premier plan ».

Le **déplacement d'agenda** — le fait qu'un narratif injecté modifie les priorités du débat public — est un indicateur de niveau stratégique. Les chercheurs de Clemson University ont estimé que sur X, un narratif de Storm-1516 représentait 35 % des posts contenant un mot-clé spécifique dans les 48 heures suivant sa primo-diffusion — ce qui constitue un déplacement d'agenda documenté.

Le **changement de comportement** (vote, décision, action) est l'impact ultime mais il est quasi impossible à prouver par l'analyse seule. La corrélation entre exposition à une campagne de désinformation et changement de vote ne peut pas être établie avec certitude — trop de facteurs confondants interviennent. Le rapport VIGINUM reconnaît explicitement que « l'impact réel du mode opératoire sur le débat public numérique demeure difficile à estimer ».

La **Breakout Scale** de Ben Nimmo (Brookings, 2020) et l'**Impact-Risk Index** de EU DisinfoLab (2022) sont des cadres méthodologiques pour évaluer l'impact des opérations d'influence, mais ils restent des outils exploratoires, pas des mesures définitives.

Le praticien doit intégrer cette incertitude structurelle : il est possible de documenter rigoureusement une opération, ses mécanismes et sa portée, mais l'affirmation de son « impact » sur les opinions ou les votes reste une évaluation probabiliste, jamais une démonstration.

---

## Chapitre 15 — Détection de contenu synthétique et manipulé

### 15.1 Images et vidéos

La détection de manipulation d'images repose sur un arsenal de techniques complémentaires. Le **reverse image search** (Google Images, TinEye, Yandex Images) permet d'identifier si une image a été publiée auparavant dans un autre contexte — c'est souvent le moyen le plus efficace de détecter un contenu détourné (image réelle dans un contexte faux). L'**analyse de métadonnées EXIF** (données embarquées dans le fichier image — appareil, date, coordonnées GPS, logiciel d'édition) peut révéler des modifications, mais les métadonnées sont facilement supprimées ou modifiées. L'**Error Level Analysis** (ELA) détecte les différences de compression JPEG qui peuvent indiquer une retouche, mais cette technique produit de nombreux faux positifs et nécessite une interprétation experte. La **détection d'artefacts IA** — artefacts caractéristiques des modèles génératifs (mains mal formées, textes incohérents, reflets asymétriques, textures répétitives) — est de moins en moins fiable à mesure que les modèles s'améliorent.

### 15.2 Audio

L'analyse forensique audio est un domaine spécialisé. L'**analyse spectrale** permet d'identifier des artefacts de synthèse vocale (discontinuités spectrales, patterns de fréquence anormaux, transitions non naturelles). La **comparaison avec des échantillons authentiques** permet d'évaluer si une voix synthétique correspond à une voix réelle connue. Les détecteurs automatiques de synthèse vocale ont des performances variables et ne constituent pas un verdict — le rapport VIGINUM sur Storm-1516 documente explicitement un cas où le détecteur automatique donnait un résultat « incertain » alors que l'expert humain identifiait des artefacts spectraux.

### 15.3 Texte

Les détecteurs de texte généré par IA (GPTZero, Originality.ai, Copyleaks, et al.) méritent une attention particulière en raison de leur utilisation croissante — et des risques d'interprétation abusive de leurs résultats. Les performances de ces outils sont médiocres sur les textes courts (moins de 200 mots), fortement sensibles aux paraphrases et au post-editing humain, et présentent des taux de faux positifs significatifs (des textes humains classés comme « IA »). Un détecteur de texte IA ne doit jamais être utilisé comme preuve autonome — il produit un signal qui doit être corroboré par d'autres éléments.

### 15.4 La course aux armements détection/génération

La dynamique fondamentale est celle d'une course aux armements : chaque amélioration de la détection est contournée par la génération suivante. Les watermarks sont supprimés, les artefacts corrigés, les patterns de détection contournés. Cette dynamique a une implication opérationnelle directe : les outils de détection ont une durée de vie limitée et doivent être constamment mis à jour. L'investissement dans les capacités de détection est un coût récurrent, pas un investissement ponctuel.

### 15.5 Principe fondamental : la détection comme signal, jamais comme preuve

Ce principe est si important qu'il mérite d'être explicitement posé : **la détection automatique de contenu synthétique est un signal exploratoire, jamais une preuve**. La corroboration multi-méthode est obligatoire. Un contenu ne peut être qualifié de « synthétique » ou de « manipulé » que sur la base d'une convergence de signaux : résultat de détecteurs automatiques + analyse humaine experte + vérification contextuelle + analyse de la chaîne de diffusion + cohérence avec les TTPs connus. Tout rapport présentant un résultat de détecteur comme un verdict est méthodologiquement défaillant.

---

## Chapitre 16 — Attribution des opérations d'influence

### 16.1 Niveaux d'attribution

L'attribution est un processus en couches. L'**attribution technique** identifie l'infrastructure et les moyens utilisés : domaines, serveurs, comptes, outils, patterns techniques. Elle repose sur des éléments objectivables et vérifiables. L'**attribution opérationnelle** identifie les personnes ou entités qui ont conduit l'opération. Elle s'appuie sur l'attribution technique enrichie d'éléments d'investigation (liens entre infrastructure et entités identifiées, fuites, erreurs de sécurité opérationnelle). L'**attribution stratégique** identifie le commanditaire — l'État ou l'organisation qui a ordonné et financé l'opération. C'est le niveau le plus difficile à atteindre car le commanditaire est généralement séparé de l'exécutant par une chaîne de proxies.

Le rapport VIGINUM sur Storm-1516 illustre ces trois niveaux : l'attribution technique est solide (infrastructure CopyCop, comptes X et Telegram, patterns de diffusion documentés), l'attribution opérationnelle est étayée (implication de John Mark Dougan documentée, liens avec la FCI et la BJA), l'attribution stratégique pointe vers le GRU et le CEG mais avec des niveaux de confiance différenciés (« VIGINUM a par ailleurs pu obtenir des informations supplémentaires sur Youry Khorochenky, un potentiel officier de l'unité 29155 du GRU accusé publiquement d'avoir financé et coordonné le mode opératoire »).

### 16.2 Méthodes d'attribution

L'OSINT sur l'infrastructure (domaines, hébergement, certificats, Whois historique) est la base de l'attribution technique. L'**analyse linguistique** peut fournir des indices : erreurs de traduction spécifiques, idiomatismes caractéristiques, horaires d'activité. L'**analyse des TTPs** permet de comparer le mode opératoire avec des opérations précédemment attribuées — un acteur a tendance à réutiliser les mêmes outils, les mêmes techniques et les mêmes patterns, ce qui constitue une « signature opérationnelle ». Le renseignement complémentaire (HUMINT, SIGINT) peut fournir des éléments décisifs mais reste hors du périmètre de l'analyste civil.

VIGINUM a développé une doctrine d'utilisation d'OpenCTI (plateforme open source de threat intelligence) pour structurer le suivi des modes opératoires informationnels, en modélisant les acteurs, les campagnes, les infrastructures, les narratifs, les observables et leurs relations dans un format STIX interopérable. Cette approche systématique permet de capitaliser sur les investigations successives et de renforcer progressivement l'attribution.

### 16.3 Limites et biais d'attribution

Le **false flag** — un acteur A se faisant passer pour un acteur B — est un risque structurel. Planter des indices techniques pointant vers un acteur connu est techniquement possible et a été documenté. La prudence dans l'attribution est une nécessité méthodologique, pas une faiblesse.

Le **biais d'attribution** est un risque cognitif : on attribue plus facilement une opération à un adversaire connu. Si un analyste surveille principalement les opérations russes, il risque d'interpréter tout signal comme d'origine russe. La diversification des hypothèses et la recherche active d'explications alternatives sont des pratiques de rigueur essentielles.

La dimension **diplomatique** influence le timing et le contenu de l'attribution publique. Une attribution techniquement solide peut être retardée ou modulée pour des raisons politiques — ce qui crée une tension entre l'exigence technique de l'analyste et les considérations stratégiques du décideur.

### 16.4 La chaîne attribution → décision → action

L'attribution n'est pas une fin en soi — elle alimente une chaîne de décision. Une fois l'attribution posée et le niveau de confiance évalué, les options incluent : le signalement au politique (briefing interministériel), la notification aux plateformes (pour obtenir des takedowns), la publication (attribution publique — naming and shaming), l'action diplomatique (protestations, sanctions), la coopération avec les partenaires (partage de renseignement), et dans certains cas, des actions judiciaires.

Le choix de la réponse dépend du niveau de confiance dans l'attribution, du contexte diplomatique, de l'impact estimé de l'opération, et de l'évaluation des conséquences de chaque option de réponse. L'analyste documente et recommande — le décideur arbitre.

---

## Chapitre 17 — Veille, monitoring continu et angles morts analytiques

### 17.1 Architecture d'un dispositif de veille informationnelle

Un dispositif de veille informationnelle complet s'organise en trois couches : les **sources** (réseaux sociaux, médias, Telegram, forums, blogs, dark web, publicités en ligne), les **outils** (agrégateurs, plateformes de monitoring social, alertes par mots-clés, crawlers, APIs), et les **flux de traitement** (collecte → enrichissement → triage → analyse → archivage).

Le dimensionnement du dispositif dépend des ressources disponibles. VIGINUM, avec 56 agents, couvre le périmètre français avec une capacité limitée de couverture internationale. L'EEAS couvre une partie du périmètre européen. Les capacités des think tanks et de la société civile complètent le dispositif mais de manière non systématique.

### 17.2 Indicateurs d'alerte

Les indicateurs d'alerte prioritaires incluent : une volumétrie anormale sur un sujet donné (pic soudain sans événement déclencheur organique), l'émergence d'un narratif nouveau sans antécédent organique (un thème apparaît simultanément sur plusieurs plateformes sans source identifiable), la synchronicité de comptes (publications dans des fenêtres temporelles anormalement serrées), des URLs vers des domaines nouveaux ou suspects, un ratio d'engagement incohérent (un contenu de faible qualité obtenant un engagement disproportionné), et des patterns linguistiques anormaux (erreurs de traduction, idiomatismes non natifs, style rédactionnel homogène sur des comptes supposément indépendants).

### 17.3 Monitoring de Telegram

Telegram est devenu l'espace central de l'amplification des opérations d'influence et un espace de coordination pour les opérateurs. Les caractéristiques de Telegram qui en font un vecteur privilégié sont : l'absence de limite de taille des canaux de diffusion (certains canaux ont des centaines de milliers d'abonnés), la fonctionnalité de forward (un contenu publié sur un canal peut être instantanément repartagé sur des dizaines d'autres), la quasi-absence de modération (avec une évolution partielle après 2024), et l'absence d'API publique de monitoring.

Le monitoring de Telegram nécessite des techniques spécifiques qui sont détaillées dans le cours OSINT Mastery (Ch.8). Les outils de monitoring incluent des solutions open source (snscrape, telethon), des solutions commerciales (Brandwatch, Meltwater, Social Links), et du monitoring manuel pour les canaux fermés ou semi-fermés.

### 17.4 Les angles morts analytiques : messageries privées et espaces non observables

L'un des ajouts les plus importants à ce cours concerne les **angles morts** de la détection — les espaces où les opérations d'influence circulent mais qui échappent à l'observation analytique.

Les **messageries privées** (WhatsApp, Signal, iMessage, messagerie privée de Facebook) constituent le principal angle mort. Les contenus de désinformation circulent massivement par partage interpersonnel — un message WhatsApp transféré de groupe en groupe peut toucher des millions de personnes sans qu'aucun analyste ne puisse l'observer. Ce phénomène a été massivement documenté pendant la pandémie de COVID-19 (la « désinfodémie ») et dans plusieurs contextes électoraux (Brésil, Inde).

**Discord** est un espace croissant d'organisation et de coordination — des serveurs Discord fermés sont utilisés pour la coordination de campagnes de brigading, de raids et de diffusion coordonnée. L'analyse est limitée par le caractère fermé des serveurs.

Les **groupes Facebook privés** sont un autre espace semi-observable — les contenus ne sont visibles que par les membres du groupe, ce qui rend le monitoring systématique impossible.

La conséquence opérationnelle est que la **diffusion observée** (sur les espaces publics — X, Telegram canaux publics, sites web) ne représente qu'une fraction de la **diffusion réelle**. La pénétration d'un narratif dans les conversations interpersonnelles — les « dark social » — est le vrai indicateur d'impact mais il est quasi impossible à mesurer.

Le praticien doit donc distinguer entre **espace observable** (où la détection et l'analyse sont possibles) et **espace d'influence réel** (qui inclut les espaces privés). Les indicateurs indirects de pénétration dans les espaces privés incluent : les captures d'écran de conversations privées qui réapparaissent dans des espaces publics, l'émergence de narratifs dans des sondages d'opinion sans source publique identifiable, et les reprises cross-platform (un narratif qui apparaît simultanément sur des plateformes non connectées, suggérant une diffusion via des espaces de transit privés).

### 17.5 Le défi du volume

Le volume de données à traiter est un défi opérationnel majeur. L'EEAS a documenté 540 incidents FIMI en 2025, impliquant 10 500 canaux et sites web. Le défi n'est pas de collecter des données mais de trier des milliers de signaux pour identifier les campagnes coordonnées dans le bruit organique. Les outils de traitement automatisé (NLP, classificateurs, détecteurs d'anomalies) sont indispensables mais produisent un volume de faux positifs qui nécessite un triage humain.

> **🔵 BROUILLARD — Épisode 6**
> L'infrastructure technique est tracée. Les trois domaines des sites de réinformation sont enregistrés chez le même registrar (Njalla, registrar connu pour son offre de confidentialité) et hébergés sur un serveur partagé chez un hébergeur identifié dans des rapports antérieurs. L'analyse Whois historique révèle qu'un des domaines a été enregistré avec une adresse email qui apparaît dans la base de données d'un rapport d'EUvsDisinfo — liée à une entité identifiée dans des opérations antérieures. L'attribution technique est posée avec une confiance modérée : les éléments d'infrastructure convergent vers un acteur documenté, mais des explications alternatives (réutilisation d'infrastructure par un acteur différent, faux flag) ne peuvent être exclues. Élise rédige la note d'analyse avec la grammaire appropriée : « Les éléments d'infrastructure identifiés sont cohérents avec les TTPs documentés du MOI X. Attribution technique : confiance modérée. Attribution stratégique : confiance faible — les éléments disponibles sont compatibles avec l'implication d'un acteur étatique Y mais ne la démontrent pas de manière autonome. »


---
