---
title: Chapitre 10 — Structure et dynamiques de l'écosystème cybercriminel
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - 'PARTIE III — L''écosystème cybercriminel : une industrie de la menace'
  - index.md
---

## 10.1 — Le modèle Crime-as-a-Service (CaaS)

L'écosystème cybercriminel contemporain fonctionne comme une **économie de services industrialisée**. Le modèle Crime-as-a-Service (CaaS) permet à des acteurs ayant des compétences limitées de mener des attaques sophistiquées en achetant ou louant les capacités nécessaires auprès de fournisseurs spécialisés. Ce modèle, documenté de manière convergente par Europol (IOCTA/SOCTA 2025), l'ASD, le CSE canadien et Microsoft, est le facteur structurant principal de la menace cybercriminelle.

L'ASD détaille les services de l'écosystème CaaS : le **courtage d'accès initial** (vente de credentials et d'accès réseau), le **développement de ransomware** (programmes RaaS avec portail web et service client), le **crypting** (services d'obfuscation de malware pour contourner la détection), l'**hébergement bulletproof** (infrastructure réseau résistante aux takedowns), et le **blanchiment de cryptomonnaies** (services de mixing et de tumbling).

Le CSE canadien évalue que « la popularité continue du RaaS contribue presque certainement à l'augmentation des incidents de ransomware en abaissant les barrières techniques à l'entrée ». En d'autres termes, le CaaS démocratise la cybercriminalité : un acteur sans compétence technique peut acheter un accès initial sur un forum, louer un programme ransomware, et lancer une attaque contre une cible — tout en partageant les revenus avec les fournisseurs de chaque service.

## 10.2 — La chaîne de valeur criminelle

La chaîne de valeur cybercriminelle peut être décomposée en maillons spécialisés, chacun opéré par des acteurs distincts qui interagissent via des marketplaces et des forums.

Les **développeurs de malware** créent les outils — ransomware, infostealers, loaders, backdoors. Ils vendent leurs produits via des programmes RaaS/MaaS (Malware-as-a-Service) ou directement sur des forums. Les **opérateurs d'infrastructure** fournissent les hébergements bulletproof, les domaines résistants aux takedowns et les réseaux de proxy. Les **courtiers en accès initial (IAB)** vendent des accès déjà établis dans les réseaux de victimes. Les **affiliés ransomware** achètent ces accès et déploient le ransomware. Les **services de blanchiment** convertissent les cryptomonnaies extorquées en fonds utilisables.

Europol souligne que l'accès aux systèmes compromis est devenu « une marchandise dans l'économie CaaS, avec des accès vendus en gros ou aux enchères sur des forums du dark web ». Une victime compromise peut être soumise à « plusieurs cyberattaques simultanées ou consécutives » par différents acteurs ayant acheté l'accès au même vendeur.

## 10.3 — Forums, marketplaces et messageries chiffrées

L'infrastructure du marché noir cybercriminel a évolué sous la pression des forces de l'ordre. Les grands forums centralisés (comme les défunts Genesis Market ou BreachForums dans sa première incarnation) ont cédé du terrain aux **messageries chiffrées de bout en bout (E2EE)**. Europol note que les applications de communication chiffrées sont « de plus en plus utilisées pour négocier, faire la promotion et effectuer des transactions commerciales concernant des données piratées ».

Cette migration vers les messageries E2EE pose un défi majeur pour les forces de l'ordre : le chiffrement empêche l'interception des communications, et la nature éphémère des conversations complique la collecte de preuves. Le démantèlement de la plateforme Ghost en septembre 2024 illustre les efforts internationaux pour contrer ces canaux de communication criminels.

Les courtiers en données « font connaître leur activité sur plusieurs plateformes afin de diversifier leurs opérations et d'accroître leur résilience face aux opérations répressives » — une stratégie de multi-plateforme qui complique les takedowns.

## 10.4 — Les données volées comme marchandise centrale

L'IOCTA 2025 d'Europol est titré « Steal, Deal and Repeat » — voler, vendre, recommencer — une formulation qui résume l'économie des données volées. Les données compromises sont « très précieuses pour un vaste éventail d'acteurs criminels, qui les exploitent comme une marchandise à part entière, mais également comme un bien à acquérir à d'autres fins, y compris d'autres activités criminelles ».

Les données volées alimentent l'ensemble de l'écosystème : les credentials volées par les infostealers sont vendues aux IAB, qui les revendent aux affiliés ransomware. Les données personnelles volées lors de data breaches sont utilisées pour des fraudes d'identité, du phishing ciblé, ou de l'extorsion directe des victimes. L'ENISA documente que 68,6% des intrusions enregistrées ont conduit à des data breaches publiées sur des forums cybercriminels.

## 10.5 — Fragmentation post-disruptions

Le paysage cybercriminel a été significativement perturbé par les opérations de law enforcement en 2024-2025. Les takedowns de LockBit (février 2024), ALPHV/BlackCat (décembre 2023) et Hive (janvier 2023) ont éliminé ou dégradé les groupes ransomware les plus prolifiques. L'opération Endgame (mai 2025) a ciblé les botnets et droppers qui servent d'infrastructure commune à de nombreuses opérations.

L'effet net est paradoxal : les grandes opérations de disruption ont **fragmenté** l'écosystème plutôt que de le réduire. L'ENISA observe qu'« une transition dans l'écosystème ransomware a été observée, marquée par une fragmentation continue, conduisant à l'émergence de nouvelles variants et de nouveaux programmes RaaS ». 82 variants de ransomware ont été déployées contre l'UE sur la période de reporting — un nombre significativement plus élevé que lorsque quelques groupes dominants centralisaient le marché.

Europol note que « le paysage de la cybercriminalité est devenu plus fragmenté, avec des durées de vie plus courtes pour les marketplaces et les groupes ransomware, rendant l'attribution des acteurs de la menace plus difficile ».

## 10.6 — Recrutement et rajeunissement

Europol et le CSE documentent un phénomène préoccupant : le recrutement de jeunes adultes et d'adolescents techniquement compétents par les réseaux cybercriminels. La SOCTA 2025 note que « la récession économique, l'instabilité géopolitique et le creusement des inégalités mondiales ont augmenté les incitations pour les individus à s'engager dans la cybercriminalité financièrement motivée. Les adolescents et jeunes adultes techniquement compétents sont particulièrement susceptibles au recrutement par les réseaux criminels. »

Ce rajeunissement a des implications pour la réponse : les outils de disruption conçus pour démanteler des organisations criminelles structurées sont moins efficaces contre des individus isolés ou des petits groupes éphémères.

## 10.7 — 🔴 Fil rouge : credentials en vente sur un forum

> **📌 FIL ROUGE — Épisode 10**
>
> En juin 2025, un analyste de l'équipe de Sophie repère sur un forum underground une annonce vendant des accès VPN à une « entreprise européenne aéronautique ». Le prix demandé : 15 000 dollars en Bitcoin. L'annonce inclut une capture d'écran montrant un portail VPN — et le logo est celui d'un sous-traitant de niveau 2 d'EuroDefense.
>
> Sophie évalue : l'accès a probablement été obtenu via un infostealer (les credentials VPN sont le type d'accès le plus fréquemment vendu par les IAB). Si un affilié ransomware achète cet accès, l'attaque peut se matérialiser en jours. Plus préoccupant : ce sous-traitant a une interconnexion réseau avec le SI d'EuroDefense pour la gestion de projets conjoints.
>
> Elle déclenche une procédure d'urgence : notification du sous-traitant, reset des credentials partagées, audit des connexions entre le sous-traitant et le réseau EuroDefense, et surveillance renforcée des flux entre les deux réseaux. Elle note dans son CTL en cours de rédaction : « La supply chain IT constitue le vecteur de risque principal pour EuroDefense — non pas parce que nos propres défenses sont faibles, mais parce que nos sous-traitants sont le maillon le plus exposé. »

---
