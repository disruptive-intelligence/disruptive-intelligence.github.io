---
title: Chapitre 7 — Astroturfing et réseaux de comptes inauthentiques
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence et guerre informationnelle
up:
- - Contre-ingérence et guerre informationnelle
  - ../index.md
- - Partie II — Modes opératoires
  - index.md
---

## 7.1 Définition et mécanique

L'astroturfing — du nom du gazon synthétique Astroturf — désigne la création artificielle d'une apparence de mobilisation populaire spontanée. Dans le contexte des opérations d'influence, il s'agit de faire croire qu'un narratif, une pétition, un hashtag ou une cause bénéficie d'un soutien large et organique alors qu'il est porté par un réseau de comptes coordonnés inauthentiques.

Le terme de *Coordinated Inauthentic Behavior* (CIB), popularisé par Meta dans ses rapports de transparence, est devenu la terminologie de référence. Il désigne l'usage coordonné de faux comptes ou de comptes trompeurs pour manipuler le débat public. Le concept met l'accent sur le comportement (inauthenticité, coordination) plutôt que sur le contenu — ce qui permet d'éviter le piège de l'arbitrage de la vérité.

VIGINUM utilise le concept de « mode opératoire informationnel » (MOI), défini comme un ensemble de comportements, d'outils, de tactiques, techniques et procédures et de ressources adverses mis en œuvre par un acteur ou un groupe d'acteurs malveillants dans le cadre d'une ou de plusieurs opérations informationnelles numériques. Ce concept est plus large que le CIB de Meta, car il ne se limite pas aux réseaux sociaux et intègre l'ensemble de la chaîne d'influence (sites web, newsletters, médias, relais physiques).

## 7.2 Techniques de création de comptes

La création de comptes inauthentiques a considérablement évolué. Les « fermes de comptes » rudimentaires (profils avec des photos volées, des noms incohérents et un historique vide) sont de moins en moins efficaces face à la détection automatisée des plateformes. Les opérations contemporaines utilisent des techniques plus sophistiquées.

Les **comptes générés** utilisent des photos de profil créées par des générateurs d'images IA (GAN puis modèles de diffusion), des noms culturellement calibrés pour la zone cible, des biographies construites avec une apparence de crédibilité, et un historique factice de publications non controversées (photos de nourriture, commentaires sportifs, memes) avant l'activation dans une opération. La qualité des photos générées par IA a progressé au point de rendre la détection visuelle difficile — les artefacts caractéristiques des GANs (reflets asymétriques, boucles d'oreilles incohérentes, arrière-plans flous) sont de moins en moins présents dans les modèles de diffusion récents. Cependant, les détecteurs automatiques de photos générées restent des signaux exploratoires, pas des verdicts (voir Ch.15 et le cours OSINT Mastery Ch.14 pour le détail technique).

Les **comptes achetés** sur des marketplaces spécialisées offrent l'avantage d'un historique réel, d'un réseau de followers organique et d'une ancienneté qui résiste aux vérifications de surface. Le marché des comptes de réseaux sociaux anciens est actif et structuré, avec des prix variant selon la plateforme, l'ancienneté, le nombre de followers et le domaine géographique.

Les **comptes dormants réactivés** sont des comptes créés longtemps à l'avance, maintenus avec une activité minimale, puis activés au moment d'une opération. Storm-1516 a utilisé cette technique avec le compte @MattMetro, créé un an avant son utilisation opérationnelle.

## 7.3 Techniques d'amplification

L'amplification est le mécanisme par lequel un contenu initialement diffusé par un nombre limité de comptes atteint une audience massive. Plusieurs techniques sont documentées.

La **coordination temporelle** est le marqueur comportemental le plus caractéristique : les comptes publient ou partagent le même contenu dans des fenêtres temporelles serrées (typiquement 5 à 15 minutes). Cette synchronicité est un indicateur fort d'opération coordonnée, car elle est statistiquement improbable dans une diffusion organique. VIGINUM a documenté cette technique dans les opérations du Baku Initiative Group, où des comptes publiaient des messages avec les mêmes hashtags dans des fenêtres anormalement étroites.

Le **hashtag hijacking** consiste à s'emparer d'un hashtag existant (populaire ou lié à un événement en cours) pour y injecter du contenu manipulé, ou à créer un hashtag dédié et le propulser dans les tendances par la coordination de comptes inauthentiques.

L'**achat d'engagement** (likes, followers, vues, retweets) est un service commercial facilement accessible qui permet de gonfler artificiellement la visibilité et la crédibilité apparente d'un contenu ou d'un compte. Les tarifs sont dérisoires : quelques dizaines d'euros pour des milliers de likes ou de followers.

Les **publicités sponsorisées** ont été détournées pour amplifier des contenus de désinformation — l'opération Doppelgänger/RRN utilisait des publicités ciblées sur Facebook pour diriger les utilisateurs vers des clones de sites médiatiques avec des articles modifiés. Le DSA a renforcé les obligations de transparence sur les publicités politiques, mais les contournements restent possibles.

## 7.4 Plateformes spécifiques

Chaque plateforme a des caractéristiques qui influencent la manière dont les opérations s'y déploient.

**X (ex-Twitter)** reste la plateforme la plus documentée dans les rapports d'analyse, en partie parce que son API a historiquement permis une collecte et une analyse systématique des données. Le 3e rapport EEAS note que X représentait 88 % de l'activité FIMI détectée en 2024. L'évolution de la plateforme post-rachat (réduction de la modération, réintégration de comptes suspendus, modification de l'API) a modifié l'écosystème : davantage de comptes inauthentiques actifs mais aussi des restrictions d'accès aux données qui compliquent la recherche et la détection.

**TikTok** est un terrain d'opération croissant en raison de son algorithme de recommandation particulièrement puissant — un contenu peut devenir viral sans que le compte auteur n'ait de base d'abonnés significative. Cette caractéristique rend TikTok vulnérable à l'amplification organique involontaire de contenus manipulés. En revanche, l'accès aux données pour les chercheurs reste très limité et la modération opaque, ce qui complique l'analyse.

**Telegram** est devenu l'espace central de l'amplification et de la coordination des opérations d'influence. La quasi-absence de modération (avec une inflexion partielle après l'arrestation de Pavel Durov en août 2024), l'absence d'API publique exploitable, et la possibilité de créer des canaux de diffusion unidirectionnels avec un nombre illimité d'abonnés en font un vecteur privilégié. Le rapport VIGINUM sur Storm-1516 documente l'utilisation de chaînes Telegram pour la diffusion des narratifs vers les audiences russophones et internationales.

**Facebook/Instagram (Meta)** reste important pour le ciblage de communautés via les groupes fermés et la publicité ciblée. Meta publie des rapports CIB réguliers et a développé les capacités de détection les plus avancées parmi les plateformes, mais le volume de contenus rend la modération exhaustive impossible.

## 7.5 Limites et contre-mesures

Les plateformes détectent et suppriment régulièrement des réseaux de CIB — les *takedowns* sont documentés dans les rapports de transparence. Cependant, la reconstitution des réseaux après suppression est rapide et peu coûteuse. Un réseau de comptes supprimé sur X peut être remplacé en quelques jours. Le déplacement vers des plateformes moins modérées (Telegram, Rumble, Odysee, VKontakte) est une réponse classique aux takedowns.

La coopération entre VIGINUM et les plateformes, bien que renforcée en 2024, reste « objectivement en-deçà des attentes légitimes » selon le rapport d'activité de VIGINUM, notamment sur l'accès aux APIs nécessaires à l'identification des ingérences.

> **🔵 BROUILLARD — Épisode 3**
> L'analyse approfondie des 47 comptes initiaux révèle un réseau plus étendu. Parmi les comptes identifiés, 38 ont des photos de profil présentant des caractéristiques compatibles avec une génération par IA — mais l'analyse est nuancée : les détecteurs automatiques (Is It AI, Hive Moderation) donnent des résultats contradictoires sur certains profils. L'analyse manuelle identifie des artefacts subtils (texture de l'arrière-plan, incohérence de la ligne des cheveux) sur la majorité des images. Neuf comptes sont des comptes anciens avec un changement de nom récent — probablement achetés. En élargissant la recherche par analyse de réseau (qui retweet qui, qui partage les mêmes URLs), le réseau s'étend à plus de 200 comptes sur X, 50 comptes Facebook, 12 canaux Telegram, et 3 sites web de réinformation avec une newsletter commune. Élise documente les indicateurs d'opération dans sa fiche d'analyse.

---
