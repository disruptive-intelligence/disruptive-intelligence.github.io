---
title: Chapitre 4 — Acteurs de la menace
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE I — Fondations
  - index.md
---

typologies, motivations et convergences

## 4.1 — Catégorisation des threat actors

La catégorisation des acteurs de la menace est un exercice fondamental mais intrinsèquement imparfait. Les catégories sont des outils analytiques — pas des réalités ontologiques. Un acteur peut appartenir à plusieurs catégories simultanément, migrer d'une catégorie à l'autre, ou être instrumentalisé par un acteur d'une autre catégorie. Cette fluidité est précisément le phénomène le plus structurant du paysage 2025-2026.

Les **acteurs étatiques** (state-sponsored ou state-aligned) opèrent au service des objectifs stratégiques d'un État. Leurs motivations incluent l'espionnage stratégique (renseignement politique, militaire, économique), le prépositionnement (installation d'accès persistants dans les infrastructures critiques en prévision d'un conflit futur), la déstabilisation (attaques destructives, manipulation de l'information) et la répression transnationale (surveillance de dissidents, opposants, diasporas). Les principaux programmes étatiques documentés dans le corpus sont ceux de la Chine, de la Russie, de l'Iran et de la Corée du Nord — traités en détail dans la Partie II.

Le CERT-EU identifie, sur la période de reporting 2025, 46 ensembles d'intrusion distincts actifs contre l'UE, dont les attributions se répartissent ainsi : Russie-nexus (32%), Chine-nexus (24%), RPDC-nexus (12%), PSOA (6,7%), Iran-nexus (5,3%), Inde-nexus (4%). Environ 14,2% des activités étatiques n'ont pas pu être attribuées à un ensemble d'intrusion connu — un rappel que la visibilité est toujours partielle.

Les **acteurs cybercriminels** sont motivés par le gain financier. Leur écosystème s'est industrialisé autour du modèle Crime-as-a-Service (CaaS), avec une division du travail entre développeurs de malware, opérateurs de ransomware, courtiers en accès initial, services de blanchiment, et hébergeurs bulletproof. Le détail de cet écosystème est traité dans la Partie III.

Les **hacktivistes** sont motivés par des convictions idéologiques ou politiques. La résurgence hacktiviste 2024-2025 est étroitement liée aux conflits géopolitiques — guerre en Ukraine, conflit Israël-Hamas — et se manifeste principalement par des attaques DDoS contre les administrations publiques et les entreprises des pays perçus comme adversaires. Le CERT-EU et l'ENISA documentent que le hacktivisme représente 79% des incidents enregistrés contre l'UE en 2025, mais avec un impact opérationnel généralement limité.

Les **mercenaires cyber** (Private Sector Offensive Actors — PSOA) sont des entreprises privées qui vendent des capacités offensives à des clients gouvernementaux ou privés. Le marché du spyware commercial (NSO Group/Pegasus, Candiru, Paragon) est le segment le plus documenté, mais il existe également un marché de services d'intrusion, de surveillance et de déstabilisation. Les PSOA opèrent dans des zones grises juridiques et posent des risques spécifiques pour la société civile, les journalistes, les défenseurs des droits humains et les institutions démocratiques.

Les **insiders** — individus disposant d'un accès légitime qui l'utilisent à des fins malveillantes — constituent une catégorie distincte dont l'importance croît dans le contexte de la compétition géopolitique. Microsoft note que les États-nations recrutent de plus en plus des insiders pour accéder au renseignement, souvent via des opérations à long terme utilisant des affiliations académiques ou professionnelles comme couverture.

## 4.2 — Motivations

espionnage, gain financier, déstabilisation, prépositionnement

Les motivations des acteurs déterminent leur ciblage, leurs TTPs et leur persistance. Comprendre la motivation, c'est pouvoir prédire le comportement — au moins partiellement.

L'**espionnage stratégique** vise la collecte de renseignement politique, militaire, technologique ou économique. C'est la motivation dominante des acteurs étatiques chinois, russes et iraniens. La victimologie typique inclut les gouvernements, les institutions de défense, les centres de recherche, les télécommunications et les think tanks. L'espionnage est caractérisé par sa discrétion et sa persistance : les acteurs investissent des ressources considérables pour maintenir un accès durable sans être détectés.

Le **gain financier** est la motivation de l'écosystème cybercriminel. Il se décline en ransomware (extorsion), vol de données (revente), fraude (BEC, pig butchering), et vol de cryptomonnaies. La RPDC constitue un cas hybride où le gain financier finance directement les programmes étatiques — le ransomware et le vol de crypto servant à contourner les sanctions internationales.

La **déstabilisation** vise à perturber le fonctionnement normal d'un État, d'un secteur ou d'une société. Les attaques destructives russes contre l'Ukraine (wipers, attaques sur les infrastructures énergétiques) et leur spillover vers l'UE (cas polonais 2025) sont les manifestations les plus extrêmes. Le hacktivisme géopolitiquement aligné participe de cette logique à une échelle moindre.

Le **prépositionnement** est la motivation la plus préoccupante à moyen terme. Il consiste à installer des accès persistants dans les infrastructures critiques en prévision d'un conflit futur, sans les activer immédiatement. Le cas Volt Typhoon (Chine) est l'exemple le plus documenté : des accès dormants dans les infrastructures énergétiques, de transport et de communication américaines, prêts à être activés en cas de crise dans le détroit de Taïwan. L'ANSSI observe que les objectifs de ces prépositionnements « doivent collectivement nous alarmer ».

## 4.3 — Niveaux de sophistication et de ressources

Tous les acteurs n'ont pas les mêmes capacités. Le framework CERT-EU introduit des **niveaux d'acteurs** (threat actor levels) qui évaluent la sophistication et les ressources disponibles. Cette gradation va de l'acteur opportuniste (outils publics, pas de ciblage spécifique) à l'acteur étatique avancé (développement de zero-day, capacités de cryptanalyse, opérations multi-domaines).

En pratique, la sophistication n'est pas monolithique. Un même acteur peut utiliser des techniques très avancées (exploitation de zero-day) pour l'accès initial et des techniques banales (commandes PowerShell standard) pour le mouvement latéral. L'adoption croissante d'outils cybercriminels « commodity » par les acteurs étatiques — un phénomène documenté par l'ANSSI, le CERT-EU et Microsoft — complique cette évaluation : un acteur qui utilise des outils courants n'est pas nécessairement peu sophistiqué.

Le CSE canadien propose une analyse pertinente : le modèle CaaS a rendu les outils sophistiqués accessibles à des acteurs moins compétents, ce qui a « presque certainement contribué à l'augmentation des incidents de ransomware en abaissant les barrières techniques à l'entrée ». En d'autres termes, le niveau de sophistication de l'outil ne reflète plus le niveau de sophistication de l'opérateur.

## 4.4 — Le continuum état / cybecriminalité / hacktivisme

Le phénomène le plus structurant du paysage 2025-2026 est l'érosion des frontières entre ces catégories. Plusieurs mécanismes sont documentés.

La **convergence étatique-criminelle** prend plusieurs formes. Des acteurs étatiques utilisent des outils cybercriminels pour obscurcir l'attribution (l'ANSSI documente l'utilisation du ransomware NailoLocker combiné aux outils d'espionnage ShadowPad et PlugX). Des réseaux criminels fournissent des services aux acteurs étatiques (ransomware contre des infrastructures critiques, vol de données stratégiques) en échange de protection ou de rémunération. Europol note dans la SOCTA 2025 que les acteurs hybrides et les réseaux criminels « coopèrent pour un bénéfice mutuel, exploitant mutuellement leurs ressources, leur expertise et leur protection ».

Le **faketivisme** est un phénomène où des opérations étatiques se déguisent en hacktivisme. Le groupe Cyber Army of Russia Reborn (CARR), précédemment documenté comme opéré par le groupe étatique Sandworm (GRU), en est l'exemple emblématique. La revendication hacktiviste sert de couverture à des opérations qui auraient des implications géopolitiques si elles étaient ouvertement attribuées à un État.

La **convergence post-conflit** est un scénario prospectif documenté par Europol : dans un scenario post-guerre en Ukraine, les cybercriminels dirigés par des acteurs étatiques pourraient « rediriger leur expertise vers la cybercriminalité financière pure et continuer à cibler les institutions publiques, les entreprises et les individus ». Cette convergence pourrait intensifier la menace cybercriminelle en injectant des compétences étatiques dans l'écosystème criminel.

## 4.5 — Les menaces hybrides : instrumentalisation croisée

La SOCTA 2025 d'Europol consacre une analyse substantielle aux menaces hybrides — définies comme des activités menées par des acteurs étatiques qui exploitent l'écosystème criminel pour atteindre des objectifs stratégiques.

Les activités documentées incluent : les attaques ransomware contre les infrastructures critiques (qui génèrent des revenus tout en perturbant les adversaires), le vol de données stratégiques (espionnage outsourcé à des réseaux criminels), les campagnes de propagande et de désinformation (utilisant des réseaux de bots et des trolls), l'instrumentalisation des flux migratoires et du trafic de drogue (pour déstabiliser les sociétés cibles), et l'évasion de sanctions (pour renforcer les économies sanctionnées).

Pour le praticien, les menaces hybrides posent un défi fondamental : elles ne rentrent dans aucune case proprement. Elles ne sont ni purement étatiques (ce qui permettrait une réponse diplomatique), ni purement criminelles (ce qui permettrait une réponse judiciaire). Elles exploitent précisément cette ambiguïté pour maximiser leur impact tout en minimisant les conséquences pour le commanditaire.

## 4.6 — Limites de la catégorisation : attribution et manipulation

L'ANSSI résume le défi en une phrase : « S'il a toujours été complexe d'imputer une attaque informatique à un mode opératoire ou à un groupe d'attaquants, il est aujourd'hui également difficile de détecter et de faire sens de leurs traces dissimulées dans la complexité générale des environnements numériques. »

L'attribution est un processus analytique qui combine des indicateurs techniques (infrastructure, malware, TTPs), comportementaux (ciblage, timing, persistance) et contextuels (géopolitique, motivation, intérêt). Aucun indicateur n'est suffisant à lui seul. Les faux drapeaux sont courants : un acteur peut délibérément utiliser les outils ou l'infrastructure d'un autre pour brouiller l'attribution.

La réutilisation d'outillage complique encore l'analyse. Quand un acteur étatique utilise des outils cybercriminels disponibles publiquement, la présence de ces outils dans un incident n'est plus un indicateur d'attribution. La convergence des TTPs entre catégories d'acteurs rend les distinctions analytiques plus difficiles à maintenir.

> **⚠️ Garde-fou analytique** : ne jamais présenter une attribution comme un fait établi sans expliciter le niveau de confiance et les éléments qui la soutiennent. L'attribution est toujours un assessment — une conclusion analytique fondée sur des preuves, pas une vérité absolue. Le vocabulaire doit refléter cette nuance : « attribué avec une confiance modérée à un ensemble d'intrusion Russia-nexus » est correct. « L'attaque a été menée par la Russie » est une assertion qui dépasse le cadre de l'analyse technique.

## 4.7 — 🔴 Fil rouge : Sophie cartographie les acteurs pertinents

> **📌 FIL ROUGE — Épisode 4**
>
> Sophie commence la cartographie des acteurs pertinents pour EuroDefense. Elle identifie quatre profils de menace prioritaires :
>
> 1. **Espionnage étatique chinois** (priorité haute) : EuroDefense développe des systèmes de défense avancés et des composants satellites. Les groupes Mustang Panda et APT41 ont un historique de ciblage du secteur aéronautique et de défense européen.
> 2. **Espionnage étatique russe** (priorité haute) : en tant que fournisseur OTAN, EuroDefense est dans le périmètre de ciblage du GRU (APT28) et du SVR (APT29). Le contexte Ukraine amplifie la menace.
> 3. **Ransomware / supply chain** (priorité haute) : la dépendance à 200+ sous-traitants crée une surface d'attaque étendue. Les groupes Qilin et Akira ciblent activement l'industrie européenne.
> 4. **RPDC** (priorité moyenne) : Lazarus cible le secteur défense via des offres d'emploi fictives. La branche spatiale d'EuroDefense est potentiellement visée pour le vol de technologie.
>
> Sophie note un angle mort : la filiale en Malaisie, qui partage un réseau avec des partenaires locaux dont la posture de sécurité est inconnue. C'est un risque de supply chain géographique qui n'apparaît dans aucun rapport public.

---
