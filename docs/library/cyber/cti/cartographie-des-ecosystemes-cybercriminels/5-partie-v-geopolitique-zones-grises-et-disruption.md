---
title: PARTIE V — GÉOPOLITIQUE, ZONES GRISES ET DISRUPTION
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
chapter: 5
chapters: 8
---

*Sortir de la vision purement criminelle pour comprendre les liens entre cybercriminalité, intérêts étatiques, et les stratégies pour désorganiser les écosystèmes.*

---

## Chapitre 21 — Zones grises entre criminalité, influence et para-étatique

### 21.1 Tolérance étatique

La tolérance étatique est le mécanisme central de la zone grise. Certains États ne poursuivent pas les cybercriminels opérant depuis leur territoire, tant que ceux-ci respectent une règle implicite : ne pas cibler le pays d'origine ni ses alliés proches.

Le cas russe est le mieux documenté. Les groupes de ransomware russophones intègrent des vérifications dans leur code (langue du système, disposition du clavier, géolocalisation IP) pour éviter de chiffrer des machines dans les pays de la CEI. Cette « règle du forum » (ne pas travailler « dans la CEI ») est explicitement mentionnée dans les termes et conditions des programmes RaaS et dans les règles des forums russophones majeurs. En échange de cette non-agression, les autorités russes ferment les yeux. Quand les forces de l'ordre occidentales demandent la coopération de la Russie pour arrêter des cybercriminels, la réponse est généralement nulle — sauf dans de rares cas médiatisés servant un intérêt diplomatique ponctuel.

### 21.2 Sous-traitance implicite et proxys

Le modèle de sous-traitance implicite fonctionne sans contrat ni ordre explicite. Un service de renseignement peut « signaler » à un cybercriminel connu qu'une cible spécifique serait intéressante, sans lui donner d'ordre formel. Le cybercriminel comprend que cibler cette cible lui vaudra une protection accrue. Le résultat est un alignement stratégique sans chaîne de commandement traçable.

Ce modèle est analytiquement redoutable parce qu'il ne laisse pas les traces habituelles d'un commandement étatique (ordres, communications, infrastructure partagée). Le seul indice est l'alignement des cibles et du timing avec les intérêts géopolitiques — un signal faible, pas une preuve.

### 21.3 Acteurs hybrides

Certains individus ou groupes combinent explicitement activité criminelle (pour le profit) et activité alignée sur les intérêts étatiques (pour la protection). Le profil type : un hacker compétent qui fait du ransomware la semaine (pour gagner sa vie) et de la collecte de renseignement ou du sabotage occasionnellement (pour maintenir la bienveillance du FSB). La porosité entre les deux activités est totale : les mêmes outils, les mêmes compétences, les mêmes infrastructures servent les deux objectifs.

### 21.4 Porosité entre collecte, sabotage, influence et enrichissement

Les mêmes infrastructures, compétences et acteurs peuvent servir alternativement ou simultanément à la collecte de renseignement (espionnage), au sabotage (destruction de données, perturbation d'infrastructures), à l'influence (désinformation, pression médiatique), et à l'enrichissement (ransomware, fraude). Le cas nord-coréen illustre parfaitement cette polyvalence : le Lazarus Group (RGB) mène des opérations de cyber-espionnage, des attaques destructrices (Sony Pictures 2014, WannaCry 2017), des vols de crypto à grande échelle (Ronin Bridge 2022 — 625 M$), et des opérations de fraude (faux profils LinkedIn de développeurs pour infiltrer des entreprises tech).

### 21.5 Fil rouge — NEXUS : la dimension géopolitique

> **🔍 NEXUS — Épisode 20**
>
> Samira rassemble les éléments qui alimentent l'hypothèse H2 (instrumentalisation para-étatique).
>
> **Pour H2 :** ciblage d'un OIV énergie en période de tension diplomatique, coordination médiatique inhabituelle pour un affilié opportuniste, spécialisation de l'IAB ghost_access sur l'industrie européenne, flux financier (faible confiance) vers un wallet para-étatique, narratifs du blog de façade alignés avec la propagande d'État.
>
> **Contre H2 :** pas de preuve de commandement étatique direct, le secteur énergie est lucratif et attire les affiliés purement criminels, la coordination médiatique pourrait refléter une sophistication individuelle plutôt qu'une directive étatique, le lien financier est indirect et potentiellement artéfactuel.
>
> **Conclusion analytique :** « Les indices disponibles sont compatibles avec une instrumentalisation para-étatique (H2) mais ne permettent pas de la confirmer avec un niveau de confiance suffisant. L'hypothèse la plus parcimonieuse reste H1 (affilié purement criminel ciblant un secteur lucratif). La dimension para-étatique est maintenue comme hypothèse alternative crédible, à explorer par des investigations complémentaires (notamment : analyse approfondie du profil de ghost_access, réquisitions sur les comptes Telegram pour identifier les échanges privés, et analyse du wallet para-étatique par un service spécialisé). »

---

## Chapitre 22 — Stratégies de disruption

### 22.1 Le « et alors ? » de la cartographie

Une cartographie d'écosystème qui reste descriptive est un exercice intellectuel intéressant mais pas opérationnel. La question « et alors ? » est : à quoi sert cette cartographie concrètement ? La réponse est l'identification des points de fragilité exploitables pour la disruption.

La cartographie révèle les dépendances critiques (quels nœuds sont indispensables), les points de concentration (quels nœuds servent beaucoup d'acteurs), et les liens de confiance (quelles relations maintiennent la cohésion). Ces trois informations permettent de concevoir des stratégies de disruption ciblées.

### 22.2 Disruption technique

La disruption technique vise l'infrastructure. Elle comprend la saisie d'infrastructure (takedown de serveurs C2, de leak sites, de forums — nécessite la coopération judiciaire internationale), l'infiltration de communications (les autorités ont lu les messages internes de Conti pendant des mois avant la disruption ; l'opération Cronos a compromis l'infrastructure LockBit et collecté « une vaste quantité d'intelligence »), et l'injection de méfiance (publier des données suggérant que le forum est compromis par les forces de l'ordre, provoquant la panique et la migration désorganisée).

L'efficacité de la disruption technique dépend de la centralisation de l'écosystème visé. Un écosystème centralisé (type APT étatique avec infrastructure dédiée) est vulnérable : la saisie de l'infrastructure paralyse les opérations. Un écosystème décentralisé (type affiliés utilisant des services mutualisés) est résilient : les acteurs migrent rapidement vers des alternatives.

### 22.3 Disruption financière

La disruption financière vise les flux de valeur. La saisie de wallets crypto (le FBI a récupéré environ 2,3 millions de dollars de la rançon Colonial Pipeline en 2021), les sanctions contre les services de mixing (Tornado Cash sanctionné par l'OFAC en 2022, Chipmixer saisi en 2023, Sinbad saisi en 2023), les sanctions contre les exchanges non coopératifs, le gel des comptes des sociétés écrans, et le ciblage des réseaux de mules sont les principales tactiques.

### 22.4 Disruption humaine

L'arrestation d'acteurs clés a un impact proportionnel à leur centralité dans l'écosystème. Arrêter un affilié remplaçable a un impact limité. Arrêter l'opérateur central a un impact majeur. La cartographie permet précisément de distinguer les deux — d'où son utilité opérationnelle.

Le retournement d'informateurs et la coopération de certains acteurs arrêtés permettent d'obtenir des informations de l'intérieur de l'écosystème. Les programmes de récompense (le Département d'État américain offre jusqu'à 10-15 millions de dollars pour des informations sur les leaders de groupes de ransomware majeurs) sont des incitations puissantes.

### 22.5 Disruption de la confiance

La forme de disruption la plus dévastatrice et la plus sous-estimée. La publication des échanges internes de Conti (Conti Leaks, février-mars 2022) a détruit la confiance entre les membres et provoqué l'effondrement du groupe plus efficacement qu'aucune opération technique. La révélation de l'identité réelle de LockBitSupp (Dmitry Khoroshev, mai 2024) a sapé la crédibilité de la marque et contribué au bannissement de ses forums majeurs.

La méfiance est l'arme la plus puissante contre un écosystème basé sur la confiance. Si les acteurs soupçonnent que leur forum est infiltré, que leur opérateur partage des informations avec les forces de l'ordre, ou que leurs communications sont surveillées, la coopération devient impossible — et l'écosystème se désintègre.

### 22.6 Fil rouge — NEXUS : recommandations de disruption

> **🔍 NEXUS — Épisode 21**
>
> L'analyse de l'écosystème identifie 3 points de fragilité exploitables.
>
> **Point 1 : L'hébergeur moldave.** Il héberge le C2, le panel PhantomCrypt, le blog de façade, et 15+ autres domaines malveillants. Sa déconnexion (par coopération judiciaire avec la Moldavie, pression sur le fournisseur d'upstream connectivity, ou notification au registrar) impacterait simultanément PhantomCrypt et d'autres opérations. Impact estimé : élevé. Faisabilité : modérée (la Moldavie coopère inégalement mais a un intérêt à démontrer sa bonne volonté européenne).
>
> **Point 2 : L'exchange Dubaï.** C'est le principal point de cash-out (65 % des flux). Une coopération judiciaire avec les EAU (via canal Interpol ou bilatéral) permettrait le gel des comptes et l'identification des titulaires. Impact estimé : élevé sur la chaîne financière. Faisabilité : difficile (la coopération des EAU est lente et politiquement sensible).
>
> **Point 3 : L'IAB ghost_access.** Il est le fournisseur d'accès de 5+ affiliés RaaS identifiés. Son arrestation tarirait l'approvisionnement en accès pour une partie significative de l'écosystème PhantomCrypt. Impact estimé : modéré (les affiliés trouveraient un autre IAB, mais avec un délai). Faisabilité : dépend de l'identification et de la localisation de l'acteur.

---

## Chapitre 23 — Les facteurs macro

### 23.1 Pression policière internationale

L'intensification de la coopération internationale en matière de cybercriminalité (Europol, FBI, NCA, Joint Cybercrime Action Taskforce) a produit des résultats significatifs en 2023-2025, mais l'impact global reste limité par la vitesse de reconstitution des écosystèmes.

### 23.2 Sanctions et régulations crypto

Le cadre réglementaire des cryptomonnaies s'est considérablement durci. Le règlement MiCA (Markets in Crypto-Assets) de l'Union européenne, entré en application en 2024-2025, impose des obligations KYC/AML renforcées aux fournisseurs de services d'actifs virtuels (VASP). Les sanctions OFAC contre les services de mixing (Tornado Cash, Chipmixer, Sinbad, Blender.io) et contre des exchanges non coopératifs ont réduit les options de blanchiment — mais ont aussi accéléré l'innovation des acteurs (migration vers des protocoles décentralisés, bridges, privacy coins).

### 23.3 Fermetures de forums et migrations

Les fermetures de forums (par saisie policière ou exit scam de l'administrateur) provoquent des migrations massives qui réorganisent l'écosystème. Chaque migration est une période de vulnérabilité : les acteurs perdent temporairement leur capital réputationnel, les communications sont désorganisées, et les nouveaux espaces ne bénéficient pas immédiatement des mécanismes de gouvernance matures des forums précédents.

### 23.4 Tolérance étatique variable et géopolitique

La tolérance étatique envers la cybercriminalité varie en fonction du contexte géopolitique. Les tensions entre la Russie et l'Occident depuis 2022 (invasion de l'Ukraine) ont renforcé la tolérance russe envers les groupes ciblant l'Occident. Inversement, les rapprochements diplomatiques ponctuels peuvent conduire à des arrestations médiatisées (comme les arrestations REvil en Russie en janvier 2022, peu avant l'invasion — interprétées comme un signal diplomatique plutôt que comme un changement de politique structurel).

---
