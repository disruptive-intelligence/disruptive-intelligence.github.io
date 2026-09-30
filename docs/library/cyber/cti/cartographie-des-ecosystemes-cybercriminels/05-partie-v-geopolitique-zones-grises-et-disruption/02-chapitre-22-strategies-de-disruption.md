---
title: Chapitre 22 — Stratégies de disruption
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie V — Géopolitique, zones grises ET disruption
  - index.md
---

## 22.1 Le « et alors ? » de la cartographie

Une cartographie d'écosystème qui reste descriptive est un exercice intellectuel intéressant mais pas opérationnel. La question « et alors ? » est : à quoi sert cette cartographie concrètement ? La réponse est l'identification des points de fragilité exploitables pour la disruption.

La cartographie révèle les dépendances critiques (quels nœuds sont indispensables), les points de concentration (quels nœuds servent beaucoup d'acteurs), et les liens de confiance (quelles relations maintiennent la cohésion). Ces trois informations permettent de concevoir des stratégies de disruption ciblées.

## 22.2 Disruption technique

La disruption technique vise l'infrastructure. Elle comprend la saisie d'infrastructure (takedown de serveurs C2, de leak sites, de forums — nécessite la coopération judiciaire internationale), l'infiltration de communications (les autorités ont lu les messages internes de Conti pendant des mois avant la disruption ; l'opération Cronos a compromis l'infrastructure LockBit et collecté « une vaste quantité d'intelligence »), et l'injection de méfiance (publier des données suggérant que le forum est compromis par les forces de l'ordre, provoquant la panique et la migration désorganisée).

L'efficacité de la disruption technique dépend de la centralisation de l'écosystème visé. Un écosystème centralisé (type APT étatique avec infrastructure dédiée) est vulnérable : la saisie de l'infrastructure paralyse les opérations. Un écosystème décentralisé (type affiliés utilisant des services mutualisés) est résilient : les acteurs migrent rapidement vers des alternatives.

## 22.3 Disruption financière

La disruption financière vise les flux de valeur. La saisie de wallets crypto (le FBI a récupéré environ 2,3 millions de dollars de la rançon Colonial Pipeline en 2021), les sanctions contre les services de mixing (Tornado Cash sanctionné par l'OFAC en 2022, Chipmixer saisi en 2023, Sinbad saisi en 2023), les sanctions contre les exchanges non coopératifs, le gel des comptes des sociétés écrans, et le ciblage des réseaux de mules sont les principales tactiques.

## 22.4 Disruption humaine

L'arrestation d'acteurs clés a un impact proportionnel à leur centralité dans l'écosystème. Arrêter un affilié remplaçable a un impact limité. Arrêter l'opérateur central a un impact majeur. La cartographie permet précisément de distinguer les deux — d'où son utilité opérationnelle.

Le retournement d'informateurs et la coopération de certains acteurs arrêtés permettent d'obtenir des informations de l'intérieur de l'écosystème. Les programmes de récompense (le Département d'État américain offre jusqu'à 10-15 millions de dollars pour des informations sur les leaders de groupes de ransomware majeurs) sont des incitations puissantes.

## 22.5 Disruption de la confiance

La forme de disruption la plus dévastatrice et la plus sous-estimée. La publication des échanges internes de Conti (Conti Leaks, février-mars 2022) a détruit la confiance entre les membres et provoqué l'effondrement du groupe plus efficacement qu'aucune opération technique. La révélation de l'identité réelle de LockBitSupp (Dmitry Khoroshev, mai 2024) a sapé la crédibilité de la marque et contribué au bannissement de ses forums majeurs.

La méfiance est l'arme la plus puissante contre un écosystème basé sur la confiance. Si les acteurs soupçonnent que leur forum est infiltré, que leur opérateur partage des informations avec les forces de l'ordre, ou que leurs communications sont surveillées, la coopération devient impossible — et l'écosystème se désintègre.

## 22.6 Fil rouge — NEXUS : recommandations de disruption

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
