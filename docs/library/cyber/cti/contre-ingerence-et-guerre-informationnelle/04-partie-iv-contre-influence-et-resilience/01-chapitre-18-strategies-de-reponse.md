---
title: Chapitre 18 — Stratégies de réponse
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence et guerre informationnelle
up:
- - Contre-ingérence et guerre informationnelle
  - ../index.md
- - Partie IV — Contre-influence et résilience
  - index.md
---

le spectre des options opérationnelles

## 18.1 L'inaction calculée

Ne pas répondre est parfois la meilleure réponse. L'**effet Streisand** — une réponse qui amplifie la visibilité du contenu qu'elle cherche à contrer — est un risque réel. Un narratif confiné à des espaces marginaux (Telegram, forums) peut devenir mainstream si un gouvernement ou une institution y répond publiquement. L'évaluation du risque d'amplification involontaire doit précéder toute décision de réponse.

Les critères de décision incluent : le contenu a-t-il dépassé les espaces marginaux ? Atteint-il des audiences organiques authentiques ? Est-il repris par des médias mainstream ? Le narratif est-il susceptible de pénétrer le débat public sans intervention ? La réponse institutionnelle risque-t-elle d'amplifier plus qu'elle ne contient ? Si le narratif reste confiné et en déclin, l'inaction surveillée est souvent la stratégie optimale.

## 18.2 Le debunking : déconstruction factuelle

Le debunking — la correction factuelle d'une fausse information après sa diffusion — est l'outil le plus instinctif mais pas nécessairement le plus efficace. Son efficacité est limitée sur les audiences déjà convaincues (le biais de confirmation rend la correction inopérante) mais réelle sur les audiences indécises (celles qui n'ont pas encore formé une opinion arrêtée).

Les bonnes pratiques issues de la recherche (Lewandowsky et al., 2020) : commencer par le fait correct (pas par le mythe à réfuter), fournir une explication alternative (pourquoi l'information est fausse et quelle est la réalité), utiliser un format clair et visuel, et ne pas sur-exposer le contenu faux en le répétant excessivement.

L'**état de la recherche 2025** sur l'effet backfire (la correction renforce la croyance) est nuancé : cet effet est moins fréquent que ne le suggérait la littérature initiale de Nyhan et Reifler (2010), mais le *continued influence effect* (persistance de la croyance corrigée) reste documenté. Le debunking fonctionne, mais ses effets sont modestes et temporaires.

## 18.3 Le prebunking : inoculation

Le prebunking est la stratégie la plus prometteuse identifiée par la recherche. Le principe est l'inoculation — préexposer les audiences aux techniques de manipulation pour renforcer leur résistance cognitive avant l'attaque. Les travaux de Cambridge (van der Linden, Roozenbeek) ont montré que cette approche réduit significativement la susceptibilité aux contenus manipulés. Google/Jigsaw a déployé des campagnes de prebunking vidéo sur YouTube en Europe de l'Est (Pologne, République tchèque, Slovaquie) avec des résultats mesurables en termes de capacité à identifier les techniques de manipulation.

L'avantage du prebunking sur le debunking est qu'il cible les **techniques** (cadrage émotionnel, fausse autorité, faux consensus) plutôt que les **contenus** spécifiques, ce qui le rend résistant à l'évolution des narratifs. Sa limite est qu'il suppose une action proactive, avant l'attaque, ce qui nécessite une anticipation stratégique.

## 18.4 La contre-narrative

La contre-narrative va au-delà de la correction factuelle : elle propose un récit alternatif cohérent qui remplace le narratif hostile. La bataille n'est pas seulement factuelle — elle est narrative. Un fait isolé ne bat pas un récit ; seul un récit alternatif peut battre un récit.

La construction d'une contre-narrative efficace suppose d'identifier les besoins psychologiques que le narratif hostile satisfait (besoin de sens, d'identité, de justice) et de proposer un récit qui satisfait ces mêmes besoins de manière plus constructive. C'est un exercice difficile qui relève autant de la communication stratégique que de l'analyse (voir Ch.19 pour la doctrine de communication).

## 18.5 L'action sur l'infrastructure

Le signalement aux plateformes pour obtenir des takedowns de comptes et de contenus est l'action la plus directe. Son efficacité est réelle mais limitée dans le temps : les réseaux se reconstituent rapidement après suppression, migrent vers des plateformes moins modérées, ou adaptent leurs TTPs pour contourner la détection. Le rapport d'activité 2024 de VIGINUM documente comment le partage d'éléments techniques avec les plateformes « a parfois conduit à des actions proactives de modération » mais note que « le niveau de coopération avec certains fournisseurs de plateformes reste objectivement en-deçà des attentes ».

Les **sanctions** sur les entités impliquées dans les opérations d'influence sont un levier de plus en plus utilisé. En 2024-2025, l'UE a sanctionné plusieurs entités liées aux opérations FIMI russes, dont la Social Design Agency, Tigerweb et John Mark Dougan. Le 4e rapport EEAS formalise un « FIMI Deterrence Playbook » qui vise à rendre les opérations plus coûteuses et plus risquées pour les opérateurs en ciblant les intermédiaires, les proxies et les fournisseurs de services.

## 18.6 KPIs défensifs : mesurer l'efficacité de la réponse

Comment savoir si la réponse a fonctionné ? Les KPIs défensifs incluent : la **baisse de la viralité** du contenu ciblé (déclin des impressions et de l'engagement après l'intervention), le **ralentissement de la propagation** (allongement du temps entre la primo-diffusion et l'atteinte d'audiences organiques), la **non-entrée dans le mainstream** (le narratif reste confiné aux espaces marginaux), la **latence de réaction** (le temps entre la détection et la première action est un indicateur de performance opérationnelle), et la **coordination institutionnelle** (le nombre d'acteurs mobilisés et le temps de coordination entre les agences).

Ces KPIs doivent être suivis dans le temps pour évaluer l'évolution des capacités défensives, pas seulement évalués au cas par cas.

## 18.7 Exercices et red teaming informationnel

Un acteur institutionnel ne fait pas que détecter — il se prépare. Les exercices de type tabletop et les simulations de red teaming informationnel permettent de tester les processus de détection, de qualification, de décision et de réponse dans des conditions contrôlées.

Les scénarios types incluent : la simulation d'une fuite de documents sensibles (hack-and-leak), la diffusion d'un deepfake de dirigeant, la montée d'un narratif hostile avant un scrutin, et l'activation d'un réseau de comptes inauthentiques ciblant une institution. Chaque exercice doit inclure un cycle complet : détection → qualification → analyse → recommandation → décision → action → retex.

Ces exercices sont particulièrement utiles pour identifier les failles de coordination interinstitutionnelle, les délais de réaction excessifs, les lacunes de communication, et les divergences d'appréciation entre les analystes et les décideurs.

---
