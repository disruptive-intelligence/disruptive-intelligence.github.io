---
title: Chapitre 4 — Le cyber comme instrument de puissance étatique
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 4.1 Le modèle DIMEFIL et la place du cyber

Les analystes stratégiques classifient les instruments de puissance étatique selon le modèle **DIMEFIL** : Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement. Le cyber n’est pas une catégorie à part — il est un **instrument transverse** qui traverse tous les autres.

**Diplomatique** : attribution publique, sanctions ciblées, indictments, négociations de normes internationales (GGE, OEWG), expulsions d’opérateurs diplomatiques.

**Information** : opérations d’influence, hack-and-leak, désinformation coordonnée, contre-narratif, défense de la souveraineté informationnelle.

**Militaire** : opérations cyber offensives en soutien d’opérations conventionnelles (guerre en Ukraine), préparation du champ de bataille cyber, pré-positionnement dans les infrastructures adverses, défense cyber des systèmes militaires.

**Économique** : vol de propriété intellectuelle industrielle (espionnage économique systémique chinois), sabotage de concurrents, perturbation de chaînes d’approvisionnement.

**Financier** : cybervol pour financement étatique (DPRK), blanchiment via crypto, contournement de sanctions.

**Intelligence** : collecte cyber d’origine (SIGINT, CYBINT), pénétration de réseaux gouvernementaux adverses, collecte HUMINT facilitée par le cyber (profilage via OSINT, social engineering).

**Law Enforcement** : coopération internationale contre la cybercriminalité, extraterritorialité, saisies d’infrastructure (démantèlements Emotet, Qakbot, Hydra), exploitation judiciaire du cyber contre des menaces internes.

Chaque État dote son cyber d’une **combinaison spécifique** de ces instruments, qui reflète ses priorités et sa culture stratégique. La Russie intègre massivement le cyber dans l’information et le militaire. La Chine le concentre sur l’économique et le politique. La DPRK sur le financier. Les États-Unis sur l’intelligence, le diplomatique et le law enforcement. Israël sur le militaire et l’intelligence. Comprendre ces profils — ce que fait chaque Partie II à V — oriente l’analyse d’une cyberopération observée.

## 4.2 Doctrines comparées : vue d’ensemble

Les doctrines cyber divergent entre blocs, et même au sein de blocs. Avant d’entrer dans le détail par pays, une vue d’ensemble fixe les repères.

**Doctrine russe** : la guerre hybride (gibridnaya voyna) intègre le cyber dans un continuum information/cyber/militaire. Pas de séparation nette entre espionnage, influence et sabotage — un même service (le GRU) mène les trois. La sophistication varie selon les services (SVR ultra-furtif, GRU destructif, FSB hétérogène). La tolérance au bruit destructif est la plus élevée de tous les blocs.

**Doctrine chinoise** : le long game. Le cyber sert d’abord l’espionnage économique massif (propriété intellectuelle, rattrapage technologique) et le pré-positionnement stratégique. Pas de destructif massif documenté (à l’exception de la période Unit 61398 avant sa réorganisation post-2014). Sophistication croissante, fragmentation croissante entre services officiels (MSS, PLA) et contractors civils. Long time preference : mois et années d’attente avant d’activer les accès.

**Doctrine nord-coréenne** : le cyber comme arme économique. RGB (Reconnaissance General Bureau) mène espionnage, destruction ponctuelle (rare), et surtout vol massif (crypto, SWIFT). Unique dans son ampleur : c’est le seul État qui finance son régime et son programme d’armement par le cybervol.

**Doctrine iranienne** : rivalité régionale et surveillance interne. Cyber centré sur Israël, Golfe, dissidents. Destructif ponctuel (wipers comme substitut aux opérations conventionnelles). Social engineering très sophistiqué (APT35). Sophistication en croissance, mais en retrait par rapport aux quatre acteurs de pointe (US, Israël, Russie, Chine).

**Doctrine américaine** : defend forward / persistent engagement. Agir en continu dans les réseaux adverses pour dégrader leurs capacités, pas seulement défendre. Cyber intégré au renseignement (NSA), au militaire (USCYBERCOM), et au law enforcement (FBI). Usage massif du droit et de l’attribution publique comme instrument diplomatique.

**Doctrine israélienne** : préemption et supériorité technologique. Cyber comme espace d’action permanent, pas réponse à agression. Intégration militaire-renseignement-privé unique. Exportation des capacités via le marché commercial (NSO, Intellexa, Candiru).

**Doctrine britannique** : disruption coordonnée avec les Five Eyes. Modèle NCSC de protection nationale influent. National Cyber Force (2020) pour les opérations offensives dédiées.

**Doctrine française** : lutte informatique offensive / défensive / d’influence (LIO/LID/L2I), officialisée en 2019. Cadre clair, capacités croissantes, ambition d’autonomie stratégique.

Ces doctrines ne sont pas hermétiques — elles évoluent, elles s’influencent (la doctrine russe de guerre hybride a inspiré certaines réflexions chinoises ; le defend forward américain a influencé le Royaume-Uni et l’Australie). Mais elles fixent des répères durables qui permettent d’interpréter une cyberopération observée.

## 4.3 Le cyberespace comme 5ème domaine

Depuis le sommet OTAN de Varsovie (2016), le cyberespace est reconnu comme le **5ème domaine d’opérations**, après la terre, la mer, l’air et l’espace. Cette reconnaissance formalise ce qui était déjà une réalité opérationnelle depuis 2007-2010 : le cyber est un espace de confrontation militaire.

Les particularités du cyberespace comme domaine :

**Asymétrie** : un petit État peut infliger des dommages significatifs à un grand. La DPRK, avec un PIB de 30 milliards de dollars, a réalisé des vols crypto dépassant ses exportations légales. L’Iran et la Russie ont infligé des pertes industrielles se chiffrant en milliards à des économies bien plus importantes.

**Déni plausible** : l’attribution est techniquement difficile et politiquement coûteuse. Un État peut mener une opération cyber et nier publiquement pendant des années. Cette caractéristique favorise les opérations dans la zone grise (en dessous du seuil du conflit armé).

**Zone grise** : le cyber permet d’agir en dessous du seuil traditionnel du conflit armé. Des actions qui, dans le monde physique, appelleraient une réponse militaire (sabotage d’une centrale, espionnage d’un état-major) sont courantes dans le cyber avec des réponses politiques/diplomatiques seulement.

**Vitesse** : une action cyber peut se dérouler en minutes ou en heures ; une réponse diplomatique coordonnée prend des mois. Cette asymétrie temporelle favorise l’attaquant.

**Continuum** : les frontières entre espionnage, pré-positionnement, sabotage et guerre sont floues. Un même accès peut servir à l’espionnage aujourd’hui et au sabotage demain. La reconnaissance de Volt Typhoon comme pré-positionnement implique que la Chine est **déjà** en phase de préparation militaire dans les réseaux américains — sans avoir franchi aucun seuil traditionnel.

**Dual-use** : les outils cyber sont massivement dual-use. Un outil légitime de pentest (Cobalt Strike, Metasploit, Empire) est utilisé par des opérateurs autorisés et par des attaquants. Un outil comme BloodHound est utilisé par les red teams défensives et par les APT. Cette caractéristique complique la régulation export et l’attribution.

## 4.4 Ce que les APT révèlent des intentions étatiques

La lecture géopolitique des campagnes APT est une compétence à part entière. Elle consiste à inférer les priorités stratégiques d’un État à partir des cibles qu’il attaque.

**Victimologie comme signal** : si une APT attribuable à la Chine cible systématiquement des chercheurs en semiconducteurs, on peut inférer la priorité au rattrapage technologique dans ce domaine. Si elle cible la diaspora ouïghoure, on peut inférer la priorité au contrôle politique interne projeté à l’étranger. Si APT35 (Iran) cible des chercheurs spécialisés sur le nucléaire iranien, on peut inférer la priorité à la contre-surveillance du programme national.

**Timing comme signal** : les campagnes cyber suivent souvent les évolutions politiques et militaires. Le ciblage intensifié de l’Ukraine par les groupes russes post-2022, les campagnes iraniennes post-assassinat Soleimani (2020), le ciblage chinois des think tanks Taïwan lors des élections présidentielles sont des signaux doctrinaires lisibles.

**Escalation comme signal** : le passage de l’espionnage au destructif marque une escalade. Le passage du destructif ciblé au destructif mass-market (NotPetya) marque un seuil. Le pré-positionnement massif dans les infras critiques étrangères (Volt Typhoon) marque une préparation stratégique.

**Silence comme signal** : l’absence prolongée d’activité d’un groupe très actif peut signaler une réorganisation interne, un changement de mandat, ou la préparation d’une opération majeure à venir. APT10 a eu des périodes silencieuses corrélées à des réorganisations du MSS chinois.

Pour l’analyste APT, ces signaux doivent être lus prudemment. Les biais de confirmation, les fausses corrélations, et la manipulation délibérée (false flags) peuvent tromper. La règle : une hypothèse géopolitique doit être étayée par plusieurs signaux indépendants et confrontée à des hypothèses alternatives (ACH — voir Ch.24).

## 4.5 Fil rouge — BLACKOUT Épisode 2

> **⚡ BLACKOUT — Épisode 2 : pourquoi un opérateur énergie ?**
> 
> Le CERT élargit le cadrage de l’analyse. La question « qui attaque ? » ne peut pas être répondue sans d’abord répondre à « pourquoi cette cible ? »
> 
> **Profil de la victime** : opérateur de distribution d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), classement OIV en France (arrêté sectoriel énergie), entité essentielle NIS 2. Infrastructure de supervision SCADA reliée à plusieurs dizaines de postes de transformation haute tension. Pas de position publique politique marquée ; pas de contentieux notable avec des acteurs étatiques ; pas de rôle spécifique dans le soutien à l’Ukraine (au-delà de la solidarité européenne générale).
> 
> **Secteur d’activité** : l’énergie est un secteur **stratégique structurel**. Les cibles énergie sont attaquées par :
> 
> - **La Russie (Sandworm)** : doctrine de guerre hybride, ciblage énergie documenté depuis 2015 en Ukraine, extension à l’Europe dans le contexte du conflit ukrainien. Objectif : démonstration de capacité, pré-positionnement pour sabotage en cas d’escalade.
> - **La Chine (Volt Typhoon et clusters similaires)** : doctrine de pré-positionnement stratégique, ciblage énergie documenté aux US et dans le Pacifique (Guam), extension possible à l’Europe dans le contexte Taïwan. Objectif : capacité de dissuasion / représailles.
> - **L’Iran (groupes IRGC)** : ciblage énergie dans le contexte régional, moins présent en Europe. Objectif : démonstration de portée régionale, parfois représailles pour sanctions.
> - **Les cybercriminels** : énergie = cible à fort ROI pour ransomware (Colonial Pipeline 2021 a démontré que les opérateurs paient vite). Mais ici, pas de ransomware — élimine cette hypothèse.
> - **Les hacktivistes** : possible si le contexte politique le justifie. Ici, pas de signal hacktiviste évident — élimine cette hypothèse (pour l’instant).
> 
> **Diagnostic intermédiaire** : le profil cible + l’absence d’intention monétaire + la patience opérationnelle + le positionnement OT orientent vers **une APT étatique en phase de pré-positionnement**. Les candidats principaux sont **Sandworm (Russie)** et **Volt Typhoon ou cluster chinois similaire**. L’Iran est moins probable pour des raisons géographiques et doctrinaires. Les autres acteurs étatiques sont possibles mais improbables a priori.
> 
> Le CERT verrouille ce cadrage dans son journal d’investigation et passe au profilage détaillé des TTP, pour les confronter aux profils connus des candidats (Parties II à V du cours).

-----
