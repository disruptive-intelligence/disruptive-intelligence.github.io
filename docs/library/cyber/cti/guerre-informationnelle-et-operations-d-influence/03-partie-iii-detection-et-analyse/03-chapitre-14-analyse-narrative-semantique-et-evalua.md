---
title: Chapitre 14 — Analyse narrative, sémantique et évaluation d'impact
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence.md
note: Guerre informationnelle et opérations d'influence
up:
- - Guerre informationnelle et opérations d'influence
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

## 14.1 Qu'est-ce qu'un narratif

Un narratif n'est pas un message — c'est un **cadre interprétatif**. Il combine un récit (des événements ordonnés dans le temps), des acteurs (protagonistes, antagonistes, victimes), des valeurs (ce qui est bien, ce qui est mal), une charge émotionnelle, et souvent un appel implicite ou explicite à l'action. Le même fait peut être cadré par des narratifs opposés : « la France aide ses alliés africains » vs « la France perpétue une domination néocoloniale ». Le cadre interprétatif détermine la manière dont les faits sont perçus et mémorisés — c'est pourquoi les opérations d'influence investissent massivement dans la construction narrative.

La **distinction entre un narratif et un message** est opérationnellement importante. Un message est un contenu ponctuel (un tweet, un article, une vidéo). Un narratif est une structure persistante qui transcende les messages individuels et leur donne un sens. Une opération d'influence diffuse des centaines de messages, mais ils s'inscrivent typiquement dans un petit nombre de narratifs stratégiques (3 à 5 pour une opération majeure). L'analyse doit identifier les narratifs sous-jacents, pas seulement les messages.

## 14.2 Analyse des narratifs déployés

L'analyse narrative consiste à identifier les **thèmes dominants** (immigration, corruption, politique étrangère, sécurité), les **frames** utilisés (le cadrage interprétatif — « menace » vs « opportunité », « eux » vs « nous »), les **mots-clés stratégiques** et les **oppositions binaires construites**. Storm-1516 déploie typiquement des narratifs autour de deux axes principaux : la décrédibilisation de l'Ukraine et de ses dirigeants (accusations de corruption, de détournement de l'aide occidentale) et le ciblage de personnalités et processus électoraux occidentaux (fausses accusations, deepfakes, contenus anxiogènes liés à l'immigration et au terrorisme).

Le framework DISARM identifie des techniques narratives spécifiques : « Exploiter des récits existants » (T0003) — capitaliser sur des préoccupations réelles plutôt que créer des narratifs de toutes pièces, « Développer des récits contradictoires » (T0004) — polariser en proposant des versions antagonistes, « Exploiter des théories conspirationnistes » (T0022) — s'appuyer sur des communautés complotistes existantes.

## 14.3 La co-optation de narratifs existants et la chaîne fringe → mainstream

L'une des techniques les plus efficaces — et les plus difficiles à détecter — consiste à ne pas créer un narratif ex nihilo mais à **amplifier et orienter des préoccupations réelles**. Un narratif sur le coût de la vie, l'insécurité ou l'immigration n'est pas faux en soi — il reflète des préoccupations authentiques. L'opération d'influence le prend, l'amplifie, le polarise et l'oriente vers une conclusion politique spécifique (méfiance envers les institutions, rejet de l'UE, opposition à l'aide à l'Ukraine).

La **chaîne de passage du fringe au mainstream** est un mécanisme central qui mérite d'être explicitement décrit. Un narratif injecté dans l'espace informationnel parcourt typiquement les étapes suivantes :

1. **Injection** dans un espace marginal (canal Telegram, forum anonyme, faux site d'information)
2. **Reprise par des relais idéologiques** — influenceurs militants, blogs d'opinion, médias alternatifs qui trouvent le narratif utile à leur cause. Ces relais ne sont pas nécessairement partie prenante de l'opération — ils sont souvent sincères mais manipulés
3. **Amplification par des influenceurs semi-authentiques** — personnalités publiques avec une audience significative qui reprennent le narratif par conviction, opportunisme ou simple inattention
4. **Couverture par des médias alternatifs ou pseudo-médias** sous une forme journalistique
5. **Entrée dans le débat mainstream** — soit par la couverture médiatique (même pour contester le narratif), soit par la reprise par des personnalités politiques

À chaque étape, le narratif gagne en crédibilité perçue et perd la trace de son origine. Le « narrative laundering » est analogue au blanchiment d'argent — le contenu « sale » (injection clandestine) est progressivement blanchi par des intermédiaires qui lui confèrent une légitimité apparente.

## 14.4 Analyse sémantique computationnelle

Le NLP (*Natural Language Processing*) appliqué à l'analyse de campagne permet de traiter des volumes de données inaccessibles à l'analyse humaine. Les techniques mobilisées incluent le *topic modeling* (identification automatique des thèmes dominants dans un corpus), le *sentiment analysis* (mesure de la polarité émotionnelle des contenus), l'*entity extraction* (identification des personnes, organisations et lieux mentionnés), et la détection de duplications sémantiques.

VIGINUM a développé et publié sous licence libre la bibliothèque **D3lta**, qui permet de détecter les duplications massives de contenus en distinguant le copy-pasta (forte proximité graphique et sémantique), la reformulation (forte proximité sémantique, moindre proximité graphique, même langue), et la traduction (forte proximité sémantique, moindre proximité graphique, langue différente). Cet outil est directement opérationnel pour identifier les campagnes d'amplification coordonnée.

Les **LLM** sont de plus en plus utilisés comme outils d'analyse (pas de détection) — pour classifier des contenus, identifier des thèmes, résumer de grands volumes de données, et explorer des patterns. Leur utilisation comme outil analytique est prometteuse mais doit intégrer les biais des modèles et ne pas se substituer au jugement humain.

## 14.5 Évaluation d'impact : portée, pénétration et effet réel

L'évaluation de l'impact réel d'une opération d'influence est l'un des défis analytiques les plus difficiles du domaine. Trop d'analyses confondent **visibilité** (combien de personnes ont vu le contenu), **engagement** (combien ont interagi), **pénétration narrative** (combien l'ont intégré dans leur vision du monde) et **effet comportemental** (combien ont modifié leur vote, leur opinion ou leur action).

La **portée** (nombre de vues, d'impressions) est la métrique la plus facile à mesurer mais la moins significative. Un contenu vu par des millions de personnes n'a pas nécessairement modifié la perception de quiconque.

L'**engagement** (likes, partages, commentaires) est un indicateur intermédiaire qui mesure l'activation émotionnelle mais pas la conviction. Un contenu peut être massivement commenté par des personnes qui le contestent.

La **pénétration narrative** — le fait qu'un narratif injecté soit repris et intégré par des communautés authentiques — est un indicateur plus significatif. La transition d'un narratif de l'espace des comptes inauthentiques vers des conversations organiques est un seuil critique. VIGINUM note que des narratifs de Storm-1516 ont atteint « une visibilité très importante en ligne » et ont été « repris, de manière inconsciente ou opportuniste, par des personnalités et des représentants politiques de premier plan ».

Le **déplacement d'agenda** — le fait qu'un narratif injecté modifie les priorités du débat public — est un indicateur de niveau stratégique. Les chercheurs de Clemson University ont estimé que sur X, un narratif de Storm-1516 représentait 35 % des posts contenant un mot-clé spécifique dans les 48 heures suivant sa primo-diffusion — ce qui constitue un déplacement d'agenda documenté.

Le **changement de comportement** (vote, décision, action) est l'impact ultime mais il est quasi impossible à prouver par l'analyse seule. La corrélation entre exposition à une campagne de désinformation et changement de vote ne peut pas être établie avec certitude — trop de facteurs confondants interviennent. Le rapport VIGINUM reconnaît explicitement que « l'impact réel du mode opératoire sur le débat public numérique demeure difficile à estimer ».

La **Breakout Scale** de Ben Nimmo (Brookings, 2020) et l'**Impact-Risk Index** de EU DisinfoLab (2022) sont des cadres méthodologiques pour évaluer l'impact des opérations d'influence, mais ils restent des outils exploratoires, pas des mesures définitives.

Le praticien doit intégrer cette incertitude structurelle : il est possible de documenter rigoureusement une opération, ses mécanismes et sa portée, mais l'affirmation de son « impact » sur les opinions ou les votes reste une évaluation probabiliste, jamais une démonstration.

---
