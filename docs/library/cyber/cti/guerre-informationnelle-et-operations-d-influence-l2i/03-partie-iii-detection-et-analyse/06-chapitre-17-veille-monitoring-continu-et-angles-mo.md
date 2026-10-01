---
title: Chapitre 17 — Veille, monitoring continu et angles morts analytiques
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence (L2I).md
note: Guerre informationnelle et opérations d'influence (L2I)
up:
- - Guerre informationnelle et opérations d'influence (L2I)
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

## 17.1 Architecture d'un dispositif de veille informationnelle

Un dispositif de veille informationnelle complet s'organise en trois couches : les **sources** (réseaux sociaux, médias, Telegram, forums, blogs, dark web, publicités en ligne), les **outils** (agrégateurs, plateformes de monitoring social, alertes par mots-clés, crawlers, APIs), et les **flux de traitement** (collecte → enrichissement → triage → analyse → archivage).

Le dimensionnement du dispositif dépend des ressources disponibles. VIGINUM, avec 56 agents, couvre le périmètre français avec une capacité limitée de couverture internationale. L'EEAS couvre une partie du périmètre européen. Les capacités des think tanks et de la société civile complètent le dispositif mais de manière non systématique.

## 17.2 Indicateurs d'alerte

Les indicateurs d'alerte prioritaires incluent : une volumétrie anormale sur un sujet donné (pic soudain sans événement déclencheur organique), l'émergence d'un narratif nouveau sans antécédent organique (un thème apparaît simultanément sur plusieurs plateformes sans source identifiable), la synchronicité de comptes (publications dans des fenêtres temporelles anormalement serrées), des URLs vers des domaines nouveaux ou suspects, un ratio d'engagement incohérent (un contenu de faible qualité obtenant un engagement disproportionné), et des patterns linguistiques anormaux (erreurs de traduction, idiomatismes non natifs, style rédactionnel homogène sur des comptes supposément indépendants).

## 17.3 Monitoring de Telegram

Telegram est devenu l'espace central de l'amplification des opérations d'influence et un espace de coordination pour les opérateurs. Les caractéristiques de Telegram qui en font un vecteur privilégié sont : l'absence de limite de taille des canaux de diffusion (certains canaux ont des centaines de milliers d'abonnés), la fonctionnalité de forward (un contenu publié sur un canal peut être instantanément repartagé sur des dizaines d'autres), la quasi-absence de modération (avec une évolution partielle après 2024), et l'absence d'API publique de monitoring.

Le monitoring de Telegram nécessite des techniques spécifiques qui sont détaillées dans le cours OSINT Mastery (Ch.8). Les outils de monitoring incluent des solutions open source (snscrape, telethon), des solutions commerciales (Brandwatch, Meltwater, Social Links), et du monitoring manuel pour les canaux fermés ou semi-fermés.

## 17.4 Les angles morts analytiques

messageries privées et espaces non observables

L'un des ajouts les plus importants à ce cours concerne les **angles morts** de la détection — les espaces où les opérations d'influence circulent mais qui échappent à l'observation analytique.

Les **messageries privées** (WhatsApp, Signal, iMessage, messagerie privée de Facebook) constituent le principal angle mort. Les contenus de désinformation circulent massivement par partage interpersonnel — un message WhatsApp transféré de groupe en groupe peut toucher des millions de personnes sans qu'aucun analyste ne puisse l'observer. Ce phénomène a été massivement documenté pendant la pandémie de COVID-19 (la « désinfodémie ») et dans plusieurs contextes électoraux (Brésil, Inde).

**Discord** est un espace croissant d'organisation et de coordination — des serveurs Discord fermés sont utilisés pour la coordination de campagnes de brigading, de raids et de diffusion coordonnée. L'analyse est limitée par le caractère fermé des serveurs.

Les **groupes Facebook privés** sont un autre espace semi-observable — les contenus ne sont visibles que par les membres du groupe, ce qui rend le monitoring systématique impossible.

La conséquence opérationnelle est que la **diffusion observée** (sur les espaces publics — X, Telegram canaux publics, sites web) ne représente qu'une fraction de la **diffusion réelle**. La pénétration d'un narratif dans les conversations interpersonnelles — les « dark social » — est le vrai indicateur d'impact mais il est quasi impossible à mesurer.

Le praticien doit donc distinguer entre **espace observable** (où la détection et l'analyse sont possibles) et **espace d'influence réel** (qui inclut les espaces privés). Les indicateurs indirects de pénétration dans les espaces privés incluent : les captures d'écran de conversations privées qui réapparaissent dans des espaces publics, l'émergence de narratifs dans des sondages d'opinion sans source publique identifiable, et les reprises cross-platform (un narratif qui apparaît simultanément sur des plateformes non connectées, suggérant une diffusion via des espaces de transit privés).

## 17.5 Le défi du volume

Le volume de données à traiter est un défi opérationnel majeur. L'EEAS a documenté 540 incidents FIMI en 2025, impliquant 10 500 canaux et sites web. Le défi n'est pas de collecter des données mais de trier des milliers de signaux pour identifier les campagnes coordonnées dans le bruit organique. Les outils de traitement automatisé (NLP, classificateurs, détecteurs d'anomalies) sont indispensables mais produisent un volume de faux positifs qui nécessite un triage humain.

> **🔵 BROUILLARD — Épisode 6**
> L'infrastructure technique est tracée. Les trois domaines des sites de réinformation sont enregistrés chez le même registrar (Njalla, registrar connu pour son offre de confidentialité) et hébergés sur un serveur partagé chez un hébergeur identifié dans des rapports antérieurs. L'analyse Whois historique révèle qu'un des domaines a été enregistré avec une adresse email qui apparaît dans la base de données d'un rapport d'EUvsDisinfo — liée à une entité identifiée dans des opérations antérieures. L'attribution technique est posée avec une confiance modérée : les éléments d'infrastructure convergent vers un acteur documenté, mais des explications alternatives (réutilisation d'infrastructure par un acteur différent, faux flag) ne peuvent être exclues. Élise rédige la note d'analyse avec la grammaire appropriée : « Les éléments d'infrastructure identifiés sont cohérents avec les TTPs documentés du MOI X. Attribution technique : confiance modérée. Attribution stratégique : confiance faible — les éléments disponibles sont compatibles avec l'implication d'un acteur étatique Y mais ne la démontrent pas de manière autonome. »


---
