---
title: Chapitre 16 — Attribution des opérations d'influence
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
up:
- - Contre-ingérence (L2I)
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

## 16.1 Niveaux d'attribution

L'attribution est un processus en couches. L'**attribution technique** identifie l'infrastructure et les moyens utilisés : domaines, serveurs, comptes, outils, patterns techniques. Elle repose sur des éléments objectivables et vérifiables. L'**attribution opérationnelle** identifie les personnes ou entités qui ont conduit l'opération. Elle s'appuie sur l'attribution technique enrichie d'éléments d'investigation (liens entre infrastructure et entités identifiées, fuites, erreurs de sécurité opérationnelle). L'**attribution stratégique** identifie le commanditaire — l'État ou l'organisation qui a ordonné et financé l'opération. C'est le niveau le plus difficile à atteindre car le commanditaire est généralement séparé de l'exécutant par une chaîne de proxies.

Le rapport VIGINUM sur Storm-1516 illustre ces trois niveaux : l'attribution technique est solide (infrastructure CopyCop, comptes X et Telegram, patterns de diffusion documentés), l'attribution opérationnelle est étayée (implication de John Mark Dougan documentée, liens avec la FCI et la BJA), l'attribution stratégique pointe vers le GRU et le CEG mais avec des niveaux de confiance différenciés (« VIGINUM a par ailleurs pu obtenir des informations supplémentaires sur Youry Khorochenky, un potentiel officier de l'unité 29155 du GRU accusé publiquement d'avoir financé et coordonné le mode opératoire »).

## 16.2 Méthodes d'attribution

L'OSINT sur l'infrastructure (domaines, hébergement, certificats, Whois historique) est la base de l'attribution technique. L'**analyse linguistique** peut fournir des indices : erreurs de traduction spécifiques, idiomatismes caractéristiques, horaires d'activité. L'**analyse des TTPs** permet de comparer le mode opératoire avec des opérations précédemment attribuées — un acteur a tendance à réutiliser les mêmes outils, les mêmes techniques et les mêmes patterns, ce qui constitue une « signature opérationnelle ». Le renseignement complémentaire (HUMINT, SIGINT) peut fournir des éléments décisifs mais reste hors du périmètre de l'analyste civil.

VIGINUM a développé une doctrine d'utilisation d'OpenCTI (plateforme open source de threat intelligence) pour structurer le suivi des modes opératoires informationnels, en modélisant les acteurs, les campagnes, les infrastructures, les narratifs, les observables et leurs relations dans un format STIX interopérable. Cette approche systématique permet de capitaliser sur les investigations successives et de renforcer progressivement l'attribution.

## 16.3 Limites et biais d'attribution

Le **false flag** — un acteur A se faisant passer pour un acteur B — est un risque structurel. Planter des indices techniques pointant vers un acteur connu est techniquement possible et a été documenté. La prudence dans l'attribution est une nécessité méthodologique, pas une faiblesse.

Le **biais d'attribution** est un risque cognitif : on attribue plus facilement une opération à un adversaire connu. Si un analyste surveille principalement les opérations russes, il risque d'interpréter tout signal comme d'origine russe. La diversification des hypothèses et la recherche active d'explications alternatives sont des pratiques de rigueur essentielles.

La dimension **diplomatique** influence le timing et le contenu de l'attribution publique. Une attribution techniquement solide peut être retardée ou modulée pour des raisons politiques — ce qui crée une tension entre l'exigence technique de l'analyste et les considérations stratégiques du décideur.

## 16.4 La chaîne attribution → décision → action

L'attribution n'est pas une fin en soi — elle alimente une chaîne de décision. Une fois l'attribution posée et le niveau de confiance évalué, les options incluent : le signalement au politique (briefing interministériel), la notification aux plateformes (pour obtenir des takedowns), la publication (attribution publique — naming and shaming), l'action diplomatique (protestations, sanctions), la coopération avec les partenaires (partage de renseignement), et dans certains cas, des actions judiciaires.

Le choix de la réponse dépend du niveau de confiance dans l'attribution, du contexte diplomatique, de l'impact estimé de l'opération, et de l'évaluation des conséquences de chaque option de réponse. L'analyste documente et recommande — le décideur arbitre.

---
