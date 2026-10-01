---
title: Chapitre 12 — Méthodologie de détection
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence.md
note: Guerre informationnelle et opérations d'influence
up:
- - Guerre informationnelle et opérations d'influence
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

du signal faible à la qualification

## 12.1 Les trois niveaux de détection

La détection des opérations d'influence s'organise en trois niveaux de profondeur croissante.

Le **monitoring automatisé** constitue le premier filtre. Il repose sur des systèmes de surveillance qui détectent des anomalies quantitatives : pics de volume sur un sujet donné, création massive de comptes, émergence d'URLs vers des domaines nouveaux, ratios d'engagement incohérents. Le Datalab de VIGINUM (8 agents, docteurs et ingénieurs en sciences des données et intelligence artificielle) a développé des algorithmes spécifiques pour détecter les bots, les images probablement artificielles, les contenus proches sémantiquement (traduction, copy-pasta, reformulation automatisée) et identifier automatiquement les thématiques des contenus. En 2024, ce système a permis de détecter 259 phénomènes inauthentiques. Le monitoring automatisé produit des alertes, pas des qualifications — chaque alerte doit être triée par un analyste.

Le **triage analytique** est la qualification humaine des alertes. L'analyste évalue si le phénomène détecté correspond à une opération d'influence coordonnée ou à un phénomène organique (mobilisation authentique, buzz commercial, spam non politique). Le triage repose sur l'application des critères de qualification — VIGINUM utilise les quatre critères d'ingérence numérique étrangère comme grille de tri. Le triage est le moment le plus critique pour éviter les faux positifs : une mobilisation organique intense peut présenter des caractéristiques similaires à une opération coordonnée (publication dans des fenêtres temporelles serrées, messages similaires, hashtags communs).

L'**investigation approfondie** est déclenchée quand le triage produit une qualification « probable » ou « possible ». Elle mobilise des techniques OSINT avancées (analyse d'infrastructure, analyse de réseau, analyse narrative), potentiellement du renseignement complémentaire, et vise l'attribution technique et la cartographie complète de l'opération.

## 12.2 Le modèle de qualification VIGINUM

VIGINUM a développé un modèle de qualification structuré autour des quatre critères réglementaires d'une INE, mais enrichi de critères opérationnels qui permettent de graduer la confiance dans la qualification.

Les **critères cumulatifs** sont : un contenu manifestement inexact ou trompeur, une diffusion artificielle ou automatisée massive et délibérée, une atteinte potentielle aux intérêts fondamentaux de la Nation, et l'implication directe ou indirecte d'un acteur étranger. Les quatre critères doivent être réunis pour qualifier une INE.

En pratique, le critère d'**implication étrangère** est souvent le plus difficile à établir avec certitude. Un réseau de comptes inauthentiques diffusant des contenus trompeurs avant une élection peut être une opération étrangère ou une opération politique domestique. La distinction conditionne le périmètre d'intervention et les moyens mobilisables — VIGINUM n'est compétent que pour les ingérences étrangères, pas pour les manipulations domestiques de l'information.

## 12.3 Sources de signalement

Les signalements proviennent de sources multiples : la détection interne (monitoring automatisé), les **plateformes** (Transparency Reports, signalements proactifs — de qualité variable selon les plateformes), la **société civile** (fact-checkers, chercheurs académiques, ONG spécialisées comme EU DisinfoLab, DFRLab, Graphika), les **services de renseignement** (qui peuvent fournir des éléments classifiés corroborant l'implication étrangère), les **partenaires européens et internationaux** (EEAS, homologues nationaux), et les **signalements citoyens** (qui nécessitent un filtrage important mais constituent parfois la première alerte).

La coopération inter-agences est un facteur clé d'efficacité. Le rapport d'activité 2024 de VIGINUM souligne les échanges opérationnels avec de nombreux fournisseurs de plateformes (X, Google, YouTube, Facebook, Instagram, TikTok, Bluesky), ainsi que la coopération avec l'ARCOM, le MEAE et la Commission européenne.

## 12.4 La difficulté de qualification : faux positifs et zones grises

Les **faux positifs** sont un risque structurel de la détection. Une mobilisation citoyenne organique autour d'un événement peut présenter des caractéristiques d'une opération coordonnée : publication massive dans un temps court, messages similaires (slogans, mots d'ordre), utilisation de hashtags communs. L'analyste doit distinguer la coordination organique (des citoyens qui réagissent de manière similaire à un événement) de la coordination inauthentique (des comptes opérés par un acteur central).

Les **zones grises** sont encore plus problématiques. Un narratif amplifié par un État étranger mais aussi porté par des citoyens authentiques ne peut pas être réduit à une opération d'influence pure — il reflète aussi un débat public réel. Le cas des Gilets Jaunes est illustratif : une amplification documentée par des acteurs étrangers (notamment russes) ne signifie pas que le mouvement était une opération d'influence — il s'agissait d'un mouvement social organique dont certains narratifs ont été amplifiés de l'extérieur. La qualification doit refléter cette nuance.

## 12.5 Grammaire de la prudence attributive et niveaux de confiance

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
