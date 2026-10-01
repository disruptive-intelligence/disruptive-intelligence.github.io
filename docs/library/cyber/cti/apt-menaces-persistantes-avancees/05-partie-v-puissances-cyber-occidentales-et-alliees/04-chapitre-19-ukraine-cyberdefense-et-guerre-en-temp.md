---
title: 'Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie V — Puissances cyber occidentales et alliées
  - index.md
---

## 19.1 Contexte : la transformation 2014-2022

L’Ukraine est le **laboratoire mondial** de la cyberdéfense en temps de guerre. Sa trajectoire depuis 2014 (annexion de la Crimée, premières cyberattaques russes majeures) jusqu’à 2022 (invasion à grande échelle) et ses années de guerre ont produit un retour d’expérience unique — analysé, partagé, et étudié par toutes les agences cyber occidentales.

**Avant 2014** : l’Ukraine n’avait pas d’appareil cyber particulièrement mature. Les services de sécurité (SBU) avaient des capacités limitées. L’écosystème privé était modeste, avec une forte dépendance aux prestataires russes (historique post-soviétique).

**2014 (annexion Crimée + Donbass)** : les premières cyberattaques russes majeures en marge des opérations militaires — ciblage de la Commission électorale centrale ukrainienne en mai 2014 (tentative de manipulation des résultats de l’élection présidentielle, déjouée), BlackEnergy déployé contre le secteur énergie (avant 2015).

**2015-2021 — construction d’une posture cyber** :

- **Décembre 2015** : premier blackout cyber (BlackEnergy/KillDisk) contre trois distributeurs d’électricité. Prise de conscience nationale. Début de la coopération internationale intensive.
- **Décembre 2016** : Industroyer contre Kiev. Deuxième blackout.
- **2017** : NotPetya (supply chain M.E.Doc) — l’Ukraine absorbe le premier choc d’une cyberattaque qui deviendra mondiale.
- **2015-2022** : création et renforcement du **CERT-UA**, du **SSSCIP** (State Special Communications Service), renforcement des capacités cyber de la SBU. Coopération avec USCYBERCOM (hunt forward depuis 2018), NATO, UE.

**2022+ (invasion à grande échelle)** : l’Ukraine est devenue l’environnement de confrontation cyber le plus intense au monde. Les enseignements tirés de cette période sont étudiés partout.

## 19.2 L’appareil cyber ukrainien

**CERT-UA** (Computer Emergency Response Team of Ukraine) est le CERT national. Rattaché au SSSCIP, il conduit les réponses aux incidents cyber d’envergure nationale, publie des advisories techniques, et coordonne avec les partenaires internationaux. Le CERT-UA publie quotidiennement des alertes pendant la guerre — volume de publication parmi les plus élevés au monde.

**SSSCIP** (State Special Communications Service) est l’agence technique qui supervise la cybersécurité civile ukrainienne. Opère le CERT-UA, gère la sécurité des communications gouvernementales, et coordonne la défense des infrastructures critiques.

**SBU** (Sluzhba Bezpeky Ukrayiny — Service de sécurité d’Ukraine) est le principal service de renseignement et de sécurité. Dispose d’une branche cyber qui conduit des opérations de contre-intelligence, d’investigation cyber, et — selon certains rapports — des opérations cyber offensives ciblées.

**Ministry of Digital Transformation** : ministère dédié créé en 2019, dirigé par **Mykhailo Fedorov**. A joué un rôle central dans la coordination cyber depuis 2022 — publication de l’appel à la mobilisation de l’IT Army, coordination avec les grands fournisseurs cloud pour la migration d’urgence, communication publique internationale sur la guerre cyber.

**HUR** (Holovne Upravlinnia Rozvidky — Direction principale du renseignement, sous Ministry of Defense) conduit les opérations de renseignement militaire, y compris la dimension cyber. Certaines opérations ukrainiennes offensives publiquement revendiquées sont attribuées au HUR.

## 19.3 Coopération sans précédent avec le secteur privé et les alliés

La **coopération public-privé-international** mise en place autour de l’Ukraine est sans précédent dans l’histoire du cyber. Caractéristiques.

**Microsoft** : **Microsoft Threat Intelligence Center** (MSTIC) est en ligne avec l’Ukraine depuis 2022. Publications de dizaines de rapports publics documentant les attaques russes en temps réel, détection et neutralisation en quasi temps réel des malwares russes déployés (Microsoft a poussé des mises à jour de Defender qui ont neutralisé des wipers russes en heures). Microsoft a également migré des volumes considérables de données gouvernementales ukrainiennes vers Azure pour les protéger de frappes physiques (centres de données russes). Les rapports publics de Microsoft sur l’Ukraine sont devenus une référence de la documentation CTI.

**Google / Threat Analysis Group (TAG) et Mandiant** : **Project Shield** (protection DDoS gratuite pour les médias et les gouvernements à risque) a été massivement déployé en Ukraine. Mandiant (acquis par Google en 2022) a fourni un soutien IR continu.

**ESET** (Bratislava, Slovaquie) : ESET a une présence historique en Ukraine. La collaboration CERT-UA/ESET a permis la **détection et neutralisation d’Industroyer2** en avril 2022 — l’une des opérations défensives les plus remarquables de la guerre cyber. ESET publie régulièrement des analyses techniques détaillées des malwares russes déployés en Ukraine.

**Amazon Web Services** : migration d’urgence de données gouvernementales ukrainiennes vers AWS dans les premiers jours de l’invasion. Les datacenters ukrainiens étant des cibles potentielles de frappes physiques, la migration cloud a été une mesure de résilience essentielle.

**Starlink (SpaceX)** : connectivité satellitaire critique. Starlink a été déployé massivement en Ukraine dès février 2022, fournissant une connectivité résiliente aux forces armées, aux services publics, et aux civils dans les zones sans infrastructure télécom. Le rôle de Starlink est à double tranchant : dépendance stratégique envers un opérateur privé (SpaceX/Elon Musk) dont les décisions individuelles (limitation de l’usage au-dessus de la Crimée, par exemple) ont pu affecter les opérations militaires.

**Cloudflare** : protection DDoS, services de sécurité web.

**USCYBERCOM hunt forward** : équipes américaines déployées dans les réseaux ukrainiens depuis 2018, intensifiées massivement depuis 2022. Détection de menaces, partage en temps réel, remontée des TTP russes observées aux défenseurs occidentaux.

**Autres alliés européens** : CERT-EU, ANSSI (France), BSI (Allemagne), NCSC (UK), CERT-LT (Lituanie) — contributions techniques et analytiques. L’Estonie a joué un rôle particulier comme « voix cyber » européenne vis-à-vis de l’Ukraine (mémoire de l’attaque de 2007 contre l’Estonie).

Ce modèle de coopération public-privé-international a produit :

- Une **visibilité sans précédent** sur les TTP d’un acteur étatique (la Russie) dans un conflit réel.
- Une **vitesse de détection et de neutralisation** que l’Ukraine seule n’aurait pas pu atteindre.
- Un **laboratoire** pour les techniques défensives modernes, utilisable par tous les alliés.

## 19.4 Les opérations offensives ukrainiennes

Les opérations cyber offensives ukrainiennes sont documentées publiquement de manière fragmentaire. Plusieurs catégories :

**Opérations du HUR (renseignement militaire)** : cyber-sabotages contre des systèmes logistiques russes, compromission de caméras de surveillance russes (pour exfiltrer des flux vidéo révélant des mouvements militaires), compromission de systèmes de communication militaire russe, ciblage d’officiels russes.

**Opérations revendiquées publiquement** :

- **Compromission de banques russes** : plusieurs fuites de données de grandes banques russes revendiquées par des acteurs proches des services ukrainiens.
- **Hack de Rosaviatsiya** (régulateur aéronautique russe) : fuite de documents en 2022.
- **Opérations contre les médias d’État russes** : défacements ponctuels, interruptions de diffusion.

**Opérations en coordination avec l’IT Army** : certaines opérations de l’IT Army of Ukraine (voir 19.5) ont été publiquement reconnues par des responsables ukrainiens, suggérant une coordination informelle entre services et volontaires.

## 19.5 IT Army of Ukraine : zone grise hacktivisme/opération militaire

L’**IT Army of Ukraine** est un mouvement de volontaires cyber internationaux lancé publiquement par **Mykhailo Fedorov** (ministre de la Transformation numérique) via Telegram le 26 février 2022, deux jours après l’invasion.

**Modus operandi** : le canal Telegram de l’IT Army publie des listes de cibles russes (sites gouvernementaux, entreprises, médias) et appelle les volontaires à conduire des actions (DDoS principalement, parfois hacking plus sophistiqué). Le nombre de membres a dépassé 300 000 au plus haut. Une variété d’outils automatisés a été mise à disposition (scripts DDoS, plugins navigateur).

**Activités** :

- **DDoS massif** : sites gouvernementaux russes, banques, médias d’État, plateformes de service public.
- **Défacements** : sites russes compromis avec messages pro-ukrainiens.
- **Fuites de données** : publication de données russes exfiltrées par des membres plus sophistiqués.

**Zone grise** : l’IT Army illustre la difficulté contemporaine de classifier les opérations cyber.

- **Coordonnée par l’État** (via Fedorov) ? — oui, publiquement.
- **Composée de volontaires indépendants** ? — oui, majoritairement.
- **Hacktivisme ou opération militaire** ? — la question est juridiquement ouverte. Les membres de l’IT Army ne sont pas des combattants légalement (pas d’uniforme, pas d’incorporation militaire), mais ils conduisent des opérations coordonnées par l’État dans un conflit armé.
- **Cadre juridique** ? — les actions de l’IT Army constituent dans la plupart des juridictions des infractions cyber. Les participants prennent des risques juridiques réels selon leur pays de résidence.

Pour la doctrine internationale, l’IT Army pose des questions nouvelles — que ni le droit humanitaire international, ni le droit de la cybersécurité n’ont pleinement résolues. Voir Ch.26 pour les implications sur la responsabilité étatique.

## 19.6 Retour d’expérience technique : résilience sous feu

Plusieurs enseignements techniques majeurs de la guerre cyber en Ukraine.

**Résilience par la décentralisation** : les infrastructures ukrainiennes critiques ont été décentralisées (géographiquement et architecturalement). Un datacenter bombardé, un point de connectivité détruit n’interrompent pas l’ensemble — la redondance est la norme. Cette leçon est directement applicable à la préparation européenne.

**Migration cloud d’urgence** : la migration vers les clouds publics (AWS, Azure) des données gouvernementales critiques a été une mesure de résilience majeure. Préserve les données face aux frappes physiques, permet l’accès depuis n’importe où.

**Backup hors ligne et récupération rapide** : les multiples wipers russes ont imposé une discipline de backup rigoureuse. Les organisations ukrainiennes qui ont survécu aux wipers sont celles qui avaient des backups hors ligne régulièrement testés. Cette leçon est universelle.

**Détection rapide et réponse coordonnée** : la neutralisation d’Industroyer2 en quelques heures illustre ce qu’une collaboration CERT-UA/ESET bien rodée peut accomplir. La **rapidité** est un paramètre critique en cyberdéfense — la différence entre réponse en heures vs en jours peut être la différence entre incident contenu et catastrophe.

**Connectivité résiliente** : Starlink et les technologies satellitaires sont désormais des éléments stratégiques de la planification de résilience cyber.

## 19.7 Efficacité relative des cyberattaques dans un conflit cinétique

L’observation empirique la plus intéressante de la guerre cyber en Ukraine : le **cyber seul ne gagne pas une guerre**. Malgré l’intensité massive des cyberopérations russes, aucune n’a produit d’effet décisif sur le cours de la guerre conventionnelle.

**Pourquoi** :

- **Les blackouts cyber sont temporaires** : les blackouts de 2022 (réussis partiellement) ont été réparés en **heures à jours**, grâce à l’expérience accumulée depuis 2015 et aux équipes bien rodées. L’impact humain/militaire a été bien inférieur à celui d’une frappe physique équivalente.
- **Les frappes physiques sont plus efficaces pour les effets voulus** : lorsque la Russie a voulu détruire l’infrastructure énergétique ukrainienne de façon durable, elle a utilisé des missiles de croisière (hiver 2022-2023), pas des cyberattaques. Les missiles détruisent physiquement, les cyberattaques produisent des pannes de durée limitée.
- **La résilience peut être construite** : face à la menace cyber anticipée, l’Ukraine a construit une résilience qui a massivement limité l’impact effectif.

**Leçons pour les défenseurs européens** :

- **Anticiper** : le cyber sera un composant des conflits futurs, pas le composant central.
- **Construire la résilience** : backups, décentralisation, cloud, exercices.
- **Investir dans la coopération internationale** : le modèle Ukraine-alliés doit être reproductible.
- **Ne pas sur-investir dans la défense cyber au détriment de la défense conventionnelle** : le cyber complète, il ne remplace pas.

## 19.8 Implications pour l’Europe

L’expérience ukrainienne informe directement la préparation cyber européenne. Plusieurs implications opérationnelles.

**Pour les OIV et entités essentielles NIS 2** :

- Les infrastructures critiques européennes sont des cibles crédibles de pré-positionnement ou d’attaque directe dans un scénario d’escalade.
- La résilience sous bombardement (cinétique) doit être intégrée à la planification cyber — pas seulement la défense contre le cyber isolé.
- Les exercices cyber doivent inclure des scénarios de conflit composé (cyber + cinétique + économique).

**Pour les CERT nationaux et CSIRT sectoriels** :

- Le modèle de partage en temps réel (CERT-UA avec Microsoft, ESET, alliés) est à cultiver.
- Les relations préalables avec les vendors CTI majeurs sont indispensables — ne pas les construire pendant la crise.
- Les advisories CERT-UA sont une ressource permanente à intégrer aux workflows.

**Pour les agences nationales (ANSSI, BSI, NCSC)** :

- La coopération avec les pays de première ligne (États baltes, Pologne, Roumanie) est stratégique.
- Le soutien à l’Ukraine (partage de renseignement, assistance technique) nourrit en retour les capacités européennes.

**Pour l’UE** :

- **EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence — inspiré en partie de l’expérience ukrainienne.
- La coordination continue avec l’Ukraine reste une priorité stratégique.

Pour l’analyste cyber travaillant sur la menace russe contre l’Europe, la référence méthodologique est : « comment les mêmes TTP observées en Ukraine s’appliqueraient-elles à mon organisation si le conflit escaladait ? ». Cette approche traduit les enseignements ukrainiens en préparation concrète.

-----
