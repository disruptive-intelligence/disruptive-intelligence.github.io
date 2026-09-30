---
title: PARTIE I — Doctrine, cadre et posture
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 2
chapters: 15
---

> **Ce que cette partie apprend.** Comprendre ce qu'est l'OSINT comme discipline professionnelle, son inscription historique et doctrinale, sa place dans l'écosystème des disciplines de renseignement, la distinction fondamentale entre donnée / information / fait / preuve / renseignement, et le cycle du renseignement appliqué.
>
> **Ce qu'elle ne couvre pas.** Le cadre juridique (Partie II), l'OPSEC opérationnelle (Partie II), la méthodologie d'enquête (Partie III), les techniques de collecte (Parties IV à VII).
>
> **Ce que vous saurez faire après cette partie.** Cadrer intellectuellement une mission OSINT, distinguer renseignement et information, situer votre travail dans l'écosystème institutionnel et doctrinal, appliquer le cycle du renseignement.

-----

### Chapitre 1 — L'OSINT comme discipline de renseignement

#### 1.1 Définition opérationnelle

L'**OSINT** (Open Source Intelligence — en français ROSO, Renseignement d'Origine Sources Ouvertes) est la discipline du renseignement qui collecte, traite, analyse et exploite de l'information accessible publiquement pour produire du renseignement actionnable. Le mot clé est « discipline » — pas une collection d'outils, pas une recherche Google améliorée, pas une accumulation de captures d'écran. C'est un processus structuré, reproductible, documenté, et orienté décision.

L'IC OSINT Strategy 2024-2026 publiée par l'ODNI américaine définit l'OSINT comme « l'intelligence dérivée de l'information accessible publiquement, qui est collectée, exploitée, et disséminée en temps opportun à un public approprié pour traiter une exigence de renseignement spécifique ». Cette définition souligne quatre dimensions cruciales : **accessibilité publique** (pas d'accès illégal), **collecte structurée** (pas de butinage), **temps opportun** (pertinence par rapport à une décision), **exigence de renseignement** (orientation par une question, pas par une curiosité).

#### 1.2 Information versus renseignement

La distinction la plus importante du métier est celle entre **information** et **renseignement**.

Une **information** est un fait brut, isolé, non qualifié : « Marc Delaunay est administrateur de Delta Consulting Ltd à Malte ».

Un **renseignement** est une information traitée, contextualisée, corrélée à d'autres sources, évaluée en fiabilité, et présentée avec un niveau de confiance explicite : « Marc Delaunay est administrateur déclaré de Delta Consulting Ltd, société maltaise au capital symbolique, dont le siège est une adresse de domiciliation partagée par 47 autres entités, et dont les flux entrants depuis TechnoVert SAS représentent 89 % du chiffre d'affaires déclaré sur les trois derniers exercices — niveau de confiance élevé, sources A1 et B2 ».

La différence n'est pas cosmétique. C'est ce qui distingue le travail d'un investigateur professionnel d'une recherche amateur, et c'est ce qui rend un livrable défendable devant un client exigeant, un magistrat, ou une contre-expertise.

#### 1.3 Trois traits structurants de l'OSINT

L'OSINT se distingue de la simple recherche par trois traits.

**Orientée par un objectif.** « Delaunay contrôle-t-il des sociétés offshore ? » est une question d'investigation. « Que sais-je sur Delaunay ? » n'en est pas une. La question d'investigation est fermée (elle admet une réponse), vérifiable (on peut tester sa véracité), et reformulable en hypothèse (on peut imaginer une réponse alternative). Sans question, il n'y a pas de critère d'arrêt et l'enquête dérive.

**Méthodologie rigoureuse.** Le cycle du renseignement (orientation, collecte, traitement, analyse, diffusion, feedback — Ch.5) appliqué de manière disciplinée. Chaque étape laisse une trace (journal, captures, hashs, cotations). Chaque décision est tracée. L'enquête est reproductible : un confrère, sur les mêmes sélecteurs et la même méthode, doit pouvoir aboutir à des conclusions comparables.

**Livrable avec un niveau de confiance explicite.** Chaque fait porte une cotation de fiabilité (Admiralty A-F/1-6 — Ch.84). Chaque conclusion est qualifiée d'un niveau de confiance (WEP — Ch.85). Chaque limite est documentée. L'analyste qui dit « je suis sûr » sans cotation ni source produit du bruit, pas du renseignement.

#### 1.4 Usages contemporains de l'OSINT

L'OSINT est mobilisée dans une variété croissante de métiers et de contextes.

**Renseignement institutionnel.** Services d'État (DGSE, DRM, DGSI, DRSD en France ; CIA, NSA, FBI aux USA ; SIS, GCHQ, MI5 au UK). L'OSINT est devenue une INT à part entière dans la doctrine alliée, fusionnée avec les autres disciplines pour produire de l'all-source intelligence. L'IC OSINT Strategy 2024-2026 reconnaît officiellement ce statut.

**Renseignement militaire et théâtre.** Suivi des conflits (Ukraine depuis 2022 a été un cas d'école), targeting, évaluation des dommages, identification de violations du droit international. Le **B2RS** (Bataillon de Réserve en Renseignement Spécialisé) créé en France illustre l'institutionnalisation de l'OSINT militaire chez les réservistes.

**Investigation judiciaire et police.** OSINT mobilisée par les services d'enquête (Section de Recherches gendarmerie, OCLCTIC, JIRS, C3N en France ; FBI Cyber, NCA en UK) pour l'investigation pénale ; par les magistrats instructeurs comme source d'orientation ; par les douanes (DNRED en France) pour les enquêtes fiscales et de trafic.

**Conformité, AML/CFT, KYC.** Banques, sociétés de gestion, assurances, courtiers, mobilisent l'OSINT pour le KYC (Know Your Customer), le KYB (Know Your Business), la due diligence renforcée sur les PEP, l'adverse media screening. Renforcement réglementaire avec **MiCA**, **AMLD**, **Travel Rule**.

**Cyber Threat Intelligence.** Identification d'infrastructures adverses, attribution prudente, monitoring de leak sites et forums, surveillance de la surface d'attaque. L'OSINT est l'une des sources majeures de la CTI, aux côtés de l'analyse interne et des feeds commerciaux.

**Due diligence et intelligence économique.** Vérification de partenaires commerciaux, M&A, supply chain (la **CSDDD** européenne 2024 impose un devoir de vigilance qui mobilise massivement l'OSINT), investigation de fraude interne, lutte contre la contrefaçon.

**Journalisme d'investigation.** Bellingcat est devenue la référence mondiale. ICIJ et OCCRP mobilisent l'OSINT pour leurs enquêtes (Panama, Pandora, FinCEN, Cyprus Confidential). Le journalisme d'investigation contemporain est profondément OSINT-augmenté.

**Recherche académique et droits humains.** Documentation de crimes de guerre, identification de victimes de pédocriminalité (programmes Europol *Stop Child Abuse — Trace an Object*), monitoring de violations des droits humains, recherche en sciences sociales.

**Executive protection.** Identification des menaces sur dirigeants, vérification d'environnement avant un déplacement, monitoring des fuites d'informations personnelles, gestion de réputation.

**Recherche citoyenne encadrée.** Trace Labs (CTF humanitaires de recherche de personnes disparues), Bellingcat Discord, projets de recherche participative. L'OSINT citoyenne est devenue une force réelle.

#### 1.5 L'OSINT comme discipline professionnelle

L'OSINT est devenue **un métier**. En 2026, il existe des intitulés de postes dédiés (analyste OSINT, investigateur OSINT, OSINT specialist), des certifications reconnues (GIAC GOSI, TCM PORP, IntelTechniques OSIP), des cursus universitaires, des associations professionnelles (OSMOSIS, AFCOSINT en France). Les rémunérations et les responsabilités se sont structurées.

Cette professionnalisation s'accompagne d'une **exigence déontologique croissante**. L'analyste OSINT n'est plus un curieux solitaire derrière son écran : il est un professionnel responsable, tenu à des standards de méthode, de traçabilité, de proportionnalité, de respect des personnes. Le cours forme à cette posture professionnelle, pas à une virtuosité technique sans cadre.

#### 1.6 OSINT et cycle du renseignement : aperçu

Le cycle du renseignement (Ch.5 pour le détail) structure toute investigation. Six phases : **orientation** (formuler la question), **collecte** (mobiliser les sources), **traitement** (nettoyer, organiser), **analyse** (corréler, tester les hypothèses, coter), **diffusion** (produire le livrable), **feedback** (le commanditaire réagit, on rebondit). Ce cycle n'est pas strictement séquentiel : les phases se chevauchent, on revient en arrière, on itère. Mais la discipline du cycle prévient les deux pièges classiques : la collecte qui ne mène à rien (pas d'orientation claire) et le rapport bâclé (pas d'analyse structurée).

#### 1.7 Ce que l'OSINT n'est pas

L'OSINT n'est pas du **HUMINT déguisé**. L'investigateur ne se fait pas passer pour qui il n'est pas auprès de sources humaines (sauf cadre LEA précis). Le sock puppet sert à observer, pas à manipuler activement.

L'OSINT n'est pas du **SIGINT**. L'investigateur n'intercepte aucune communication. Toute interception est réservée aux services autorisés.

L'OSINT n'est pas du **hacking**. Toute exploitation d'accès non autorisé sort du cadre OSINT et bascule dans l'illégal (Code pénal art. 323-1).

L'OSINT n'est pas une **garantie de vérité**. C'est une production de renseignement coté sous incertitude, à partir de sources accessibles mais potentiellement biaisées, manipulées ou incomplètes. La rigueur méthodologique est ce qui distingue le renseignement du bruit, pas une magie qui ferait surgir la vérité.

-----

### Chapitre 2 — Histoire et doctrine OSINT 2024-2026

#### 2.1 Brève histoire

L'OSINT n'est pas née avec Internet. Pendant la Seconde Guerre mondiale, les Alliés analysaient quotidiennement la presse allemande, les émissions radio, les bulletins officiels pour reconstituer l'état des forces de l'Axe. Le **FBIS** (Foreign Broadcast Information Service, créé en 1941) est l'ancêtre direct des structures OSINT contemporaines. Pendant la Guerre froide, l'analyse de presse étrangère, de revues techniques, de bulletins officiels a fourni une part significative du renseignement disponible.

L'irruption d'Internet à la fin des années 1990 et la généralisation du web 2.0 dans les années 2000 ont transformé l'OSINT. La masse de données accessibles publiquement a explosé. Les techniques se sont diversifiées : SOCMINT (réseaux sociaux), IMINT en sources ouvertes (Google Earth en 2005), GEOINT citoyen (méthode Bellingcat à partir de 2014), DARKINT (à mesure que Tor s'est structuré).

La **guerre en Ukraine depuis 2022** a marqué une rupture doctrinale. L'OSINT citoyenne et professionnelle a livré, en temps quasi-réel, du renseignement de qualité sur les mouvements de troupes russes, l'attribution des crimes de guerre, la documentation des violations du droit international. Bellingcat, le **Conflict Intelligence Team**, **Oryx** (tracking des pertes matérielles), **GeoConfirmed**, des centaines de comptes individuels ont composé un écosystème de renseignement parallèle, parfois plus rapide et plus précis que les sources classifiées.

Cette guerre a aussi montré les **limites** : surconsommation d'informations partielles, bulles de filtrage des observateurs, manipulation de l'OSINT par les belligérants (faux comptes, faux documents, deepfakes), risque de surinterprétation. L'OSINT n'est pas une garantie de vérité, c'est un outil — et comme tout outil, il peut être retourné.

#### 2.2 L'IC OSINT Strategy 2024-2026 (États-Unis)

L'**ODNI** (Office of the Director of National Intelligence) et la **CIA** ont publié en mars 2024 la première stratégie OSINT formelle de la communauté du renseignement américaine. Elle structure quatre piliers.

**Innovation et adoption technologique.** Investir massivement dans l'IA, le ML, l'automatisation, les knowledge graphs. Réduire le temps entre collecte et exploitation. Intégrer l'OSINT avec les autres INTs.

**Workforce et compétences.** Former et retenir une force de travail OSINT spécialisée. Reconnaître l'OSINT comme discipline professionnelle à part entière. Développer des parcours de carrière.

**Data sharing et collection management.** Standardiser les pratiques. Partager les ressources entre agences. Coordonner les acquisitions de données commerciales (CAI — Commercially Available Information).

**Allies and partners.** Renforcer la coopération avec les alliés (Five Eyes, OTAN, partenaires européens). Partager les méthodologies, les données et les leçons apprises.

Cette stratégie reconnaît officiellement l'OSINT comme INT structurante et lui donne un statut institutionnel comparable au HUMINT, SIGINT, IMINT historiques. Elle est citée comme document de référence par les services alliés.

#### 2.3 La doctrine française émergente

La France a longtemps été en retard sur l'OSINT institutionnelle. Cette situation a basculé entre 2023 et 2026.

**Création du B2RS** (Bataillon de Réserve en Renseignement Spécialisé) — annoncée en 2024, opérationnel en 2025. Unité de réservistes spécialisée dans la collecte et l'analyse OSINT au profit du **Centre de Renseignement Terre** (CRT). Compagnies à Strasbourg, Paris, Toulouse selon les sources publiques. Symboliquement majeure : la France assume publiquement l'utilité opérationnelle de l'OSINT citoyenne formée, intégrée dans la défense nationale.

**Intégration au Commandement de l'Action dans la Profondeur et du Renseignement (CAPR)**. Le B2RS est rattaché à cette structure qui centralise drones, renseignement humain, et OSINT. L'OSINT n'est plus marginale, elle est un capteur parmi les autres.

**Services d'État.** DGSE, DRM, DGSI, DRSD ont structuré des cellules OSINT. La **DNRED** (douanes) mobilise l'OSINT pour les enquêtes de trafic. Le **C3N** (Centre de lutte contre les criminalités numériques de la gendarmerie) intègre l'OSINT dans ses méthodes.

**Création de VIGINUM** (Service de vigilance et protection contre les ingérences numériques étrangères) — rattaché au SGDSN, opérationnel depuis 2021, monté en puissance 2022-2026. Mission officielle : détecter et caractériser les phénomènes inauthentiques, comportements anormaux ou coordonnés affectant le débat public numérique. VIGINUM publie des rapports techniques (notamment sur l'opération **Doppelgänger** russe) qui sont devenus une référence.

**Forum InCyber** (anciennement Forum International de la Cybersécurité, FIC). Journée OSINT annuelle. Communauté professionnelle française structurée.

#### 2.4 La doctrine alliée et OTAN

**Royaume-Uni.** Le **RUSI** (Royal United Services Institute) a publié en 2023 « The Future of Open Source Intelligence for UK National Security », un papier de référence sur l'intégration PAI/OSINT au renseignement national britannique. Le **GCHQ**, **MI5**, **MI6**, **NCA** mobilisent largement l'OSINT.

**OTAN.** L'OSINT est désormais intégrée dans la doctrine de renseignement de l'Alliance, avec des manuels dédiés (NATO OSINT Handbook, NATO OSINT Reader). L'OTAN organise des exercices d'OSINT inter-alliés.

**ICRC** (Croix-Rouge internationale). A publié en 2023 le papier « Deploying OSINT in Armed Conflict Settings: Law, Ethics, and the Need for a New Theory of Harm » qui pose les questions juridiques et éthiques de l'usage de l'OSINT en conflit armé.

**Australie.** L'**ONI** (Office of National Intelligence) et l'**ASIO** intègrent l'OSINT. Le **chef de l'ASIO Mike Burgess** a publiquement averti en 2024-2025 sur l'usage de l'IA et des données ouvertes par les services étrangers contre le personnel de défense australien.

**Allemagne, Pays-Bas, Pays nordiques.** Structures OSINT établies, intégrées aux services civils et militaires.

#### 2.5 Acteurs civils et journalistiques de référence

**Bellingcat.** Fondée par Eliot Higgins en 2014. Référence mondiale du journalisme d'investigation OSINT. Méthodologie publique, formations, communauté Discord, archives de cas. Investigations majeures : MH17, Skripal, Navalny, Soleimani.

**ICIJ** (International Consortium of Investigative Journalists). Coordination des grandes enquêtes mondiales : Offshore Leaks, Panama Papers (2016), Paradise (2017), Pandora (2021), Pandora Papers, FinCEN Files (2020), Cyprus Confidential (2023), Pandora Papers continuations.

**OCCRP** (Organized Crime and Corruption Reporting Project). Centré sur la criminalité organisée transnationale et la corruption. Plateforme **Aleph** d'accès journalistique à des données publiques agrégées.

**EU DisinfoLab.** ONG bruxelloise spécialisée dans la détection et l'analyse des opérations d'influence. Référence sur l'opération **Indian Chronicles** (2019-2020, 750 faux médias en 116 pays).

**Stanford Internet Observatory.** Recherche académique sur les opérations d'influence numérique. Référence sur Spamouflage (Chine), IRA (Russie), opérations diverses.

**Graphika.** Société américaine d'analyse de réseaux sociaux et d'opérations d'influence. Rapports publics réguliers.

#### 2.6 La communauté OSINT francophone

**OSINT-FR.** Communauté en ligne (Discord, Twitter/X, conférences). Hébergement de **OSINT-CON** annuel.

**Forum InCyber** (ex-FIC). Lille, janvier. Journée OSINT dédiée.

**OSMOSIS Association.** Communauté professionnelle internationale (présence francophone). Conférences annuelles.

**Universités.** Plusieurs universités françaises offrent désormais des modules OSINT (sciences politiques, écoles de journalisme, formations en cybersécurité).

**Acteurs privés français.** Cabinets de due diligence, cellules OSINT internes de grands groupes, sociétés spécialisées.

#### 2.7 Tendances doctrinales 2026

Quelques tendances structurantes pour les années à venir.

**Fusion all-source.** L'OSINT s'intègre dans des architectures de renseignement « all-source » où elle est fusionnée avec les autres INTs. La frontière entre OSINT et autres disciplines s'estompe partiellement.

**Automatisation et agentic AI.** Les agents autonomes deviennent des outils standards (Ch.67). L'analyste devient orchestrateur d'agents, pas exécutant manuel.

**Encadrement éthique et légal renforcé.** L'**AI Act** européen, les régulations sur les données biométriques, l'évolution jurisprudentielle sur l'usage des leaks et stealer logs imposent un cadrage juridique de plus en plus exigeant.

**Professionnalisation et certification.** Les certifications se structurent. Les formations universitaires se développent. La discipline gagne en reconnaissance.

**Tension entre fragmentation et concentration.** Les plateformes se ferment (X, Meta, LinkedIn). Mais simultanément, de nouvelles plateformes émergent (Bluesky, Mastodon, Threads). L'écosystème se fragmente, augmentant la complexité de la collecte.

**Course IA défensive vs offensive.** L'IA permet à la fois de mieux investiguer et de mieux mentir. L'analyste doit maîtriser les deux faces.

-----

### Chapitre 3 — Disciplines connexes du renseignement

#### 3.1 Pourquoi distinguer les INTs

L'OSINT s'inscrit dans un écosystème de disciplines de renseignement, chacune avec ses sources, ses méthodes et ses contraintes légales. Il est utile de les distinguer pour comprendre ce que l'OSINT couvre, ce qu'elle ne couvre pas, et comment elle s'articule avec les autres.

#### 3.2 HUMINT — Human Intelligence

Renseignement issu de **sources humaines** : entretiens, informateurs, élicitation, infiltration.

**Cadre légal.** Légal s'il est transparent (un journaliste interviewant une source, un investigateur posant une question dans un cadre professionnel normal). Devient illégal si l'investigateur usurpe une identité, exerce une pression, ou manipule la source pour obtenir l'information.

**Articulation avec l'OSINT.** Le HUMINT n'est pas dans le périmètre de l'OSINT, mais certaines pratiques sont voisines : l'élicitation passive en ligne, l'observation de conversations publiques, l'interaction avec une source via un compte d'investigation déclaré. La frontière entre OSINT défensif et HUMINT actif est fine — quand l'investigateur interagit avec une source plutôt que de l'observer, il bascule en HUMINT et le cadre juridique change.

**Pour le privé.** Les enquêteurs privés agréés peuvent faire du HUMINT déclaré (entretiens, démarches). Les analystes OSINT non agréés doivent se limiter à l'observation et aux interactions transparentes.

#### 3.3 SIGINT — Signal Intelligence

**Interception de communications électroniques** (radio, téléphone, mail, données).

**Cadre légal.** Strictement réservé aux services d'État autorisés. En France, encadré par la loi renseignement de 2015 et ses évolutions. Aucun investigateur privé ne peut faire du SIGINT légalement. L'interception non autorisée est lourdement sanctionnée pénalement.

**Articulation avec l'OSINT.** Aucun chevauchement légitime pour le privé. Pour les services d'État, le SIGINT est fusionné avec l'OSINT dans des architectures all-source.

#### 3.4 IMINT — Image Intelligence

Renseignement par l'**imagerie**.

**Sous-types.**
- IMINT classifié : imagerie satellite haute résolution militaire (KH-11, Pléiades militaires). Réservé aux services.
- IMINT en sources ouvertes : imagerie satellite Sentinel (Copernicus européen), Google Earth, Maxar (commercial, partiellement public), Planet Labs, photos publiées en ligne. Accessible à l'OSINT.

**Articulation.** L'IMINT en sources ouvertes est une composante de l'OSINT (couverte en Partie VII). Les Bellingcat, GeoConfirmed et autres font massivement de l'IMINT-OSINT.

#### 3.5 GEOINT — Geospatial Intelligence

Combine **imagerie, cartographie, et données géolocalisées** pour produire du renseignement spatial.

**Méthodes.** Géolocalisation (où ?), chronolocation (quand ?), analyse temporelle d'imagerie satellite, analyse de signature spatiale. La méthode Bellingcat est un GEOINT en sources ouvertes pur.

**Articulation.** L'un des sous-domaines les plus matures de l'OSINT contemporaine. Couvert en Partie VII (Ch.48-52). L'arrivée des agents IA spécialisés en géolocalisation (GeoSpy, GeoSeer) en 2025-2026 transforme la pratique.

#### 3.6 SOCMINT — Social Media Intelligence

Renseignement issu des **réseaux sociaux**.

**Importance.** C'est aujourd'hui l'un des plus gros volumes de l'OSINT, à la fois parce que les personnes publient massivement leur vie en ligne et parce que les réseaux sociaux sont devenus des plateformes opérationnelles pour la criminalité (recrutement de mules, marché de fraude, coordination), l'extrémisme, l'influence et la fraude.

**Articulation.** Sous-domaine majeur de l'OSINT, couvert en Partie V (Ch.31-35). Souvent fusionné avec l'IMINT (photos publiées) et l'OSINT classique (pivots vers domaines, emails).

#### 3.7 FININT — Financial Intelligence

**Renseignement financier**.

**Sous-types.**
- FININT institutionnel : déclarations de soupçon, accès aux flux bancaires, levée du secret bancaire. Réservé aux Cellules de Renseignement Financier (TRACFIN en France, FinCEN aux USA).
- FININT en sources ouvertes : registres d'entreprises, comptes publiés, listes de sanctions, Pandora Papers, presse financière. Accessible à l'OSINT.

**Articulation.** L'OSINT financier est couvert en vue maître dans le présent cours (Ch.70-71, 77). Pour la profondeur métier (UBO complexes, schémas de blanchiment, comptabilité forensique, AML/CFT), **renvoi vers FININT vFULL**.

#### 3.8 DARKINT — Dark Web Intelligence

Renseignement issu du **dark web** — forums clandestins, marketplaces, leak sites.

**Cadre.** La consultation est légale (à condition de ne pas accéder à des contenus pénalement répréhensibles : CSAM, terrorisme). L'interaction est réservée à un cadre professionnel strict ou aux LEA. Aucun analyste OSINT privé ne devrait acheter sur une marketplace dark web.

**Articulation.** Vue opérationnelle dans le présent cours (Ch.44). Pour la profondeur (écosystèmes, IA criminelle, opérations LEA), **renvoi vers Dark Web vFULL**.

#### 3.9 CYBINT — Cyber Intelligence (et CTI)

Renseignement sur les **menaces et acteurs cyber**.

**Articulation.** CTI (Cyber Threat Intelligence) est un sous-domaine professionnalisé. L'OSINT est l'une de ses sources majeures (forums, leak sites, infrastructure adverse). Couvert dans le présent cours en Ch.74-75. Pour la profondeur, **renvoi vers cours CTI dédié**.

#### 3.10 MASINT, TECHINT, OSINT corporate

**MASINT** (Measurement and Signature Intelligence). Renseignement par signatures techniques (acoustique, radar, infrarouge). Très spécialisé, principalement militaire. Hors périmètre OSINT.

**TECHINT** (Technical Intelligence). Renseignement technique sur les capacités adverses (matériel, équipement, technologie). Une partie en sources ouvertes (manuels, brochures, salons, dépôts de brevets) est accessible à l'OSINT.

**OSINT corporate / Business Intelligence.** Sous-domaine de l'OSINT appliqué à la due diligence, l'intelligence économique, le M&A. Couvert dans le présent cours en Partie VI et Ch.77.

#### 3.11 Récapitulatif et frontières

| Discipline | Source | Cadre légal privé | Couverture OSINT Mastery |
|---|---|---|---|
| **HUMINT** | Sources humaines | Limité (transparence) | Hors périmètre |
| **SIGINT** | Communications interceptées | Interdit | Hors périmètre |
| **IMINT** | Imagerie | Sources ouvertes seules | Partie VII |
| **GEOINT** | Géospatial | Sources ouvertes | Partie VII |
| **SOCMINT** | Réseaux sociaux | Conditionné | Partie V |
| **FININT** | Financier | Sources ouvertes seules | Ch.70-71, 77 + FININT vFULL |
| **DARKINT** | Dark web | Consultation OK, interaction limitée | Ch.44 + Dark Web vFULL |
| **CYBINT / CTI** | Cyber | Sources ouvertes + feeds | Ch.74-75 + CTI vFULL |
| **MASINT** | Signatures techniques | Inaccessible privé | Hors périmètre |

L'OSINT englobe ou recoupe l'IMINT en sources ouvertes, le GEOINT, le SOCMINT, la part ouverte du FININT, le DARKINT en consultation, le CYBINT en sources publiques. Une investigation OSINT typique combine plusieurs de ces sous-disciplines. Le cours les enseigne de manière intégrée.

-----

### Chapitre 4 — Donnée, information, indice, fait, preuve, hypothèse, renseignement

#### 4.1 Pourquoi ce chapitre est central

C'est le **chapitre pivot** du cours. La distinction rigoureuse entre donnée brute, information contextualisée, indice, faisceau d'indices, hypothèse, fait établi, preuve, et renseignement actionnable est ce qui sépare un analyste professionnel d'un curieux. Confondre ces niveaux est l'erreur la plus fréquente — et la plus coûteuse — de l'analyste débutant.

Un investigateur qui présente une hypothèse comme un fait commet une faute professionnelle. Un investigateur qui prend un indice unique pour une preuve produit du bruit. Un investigateur qui présente une donnée brute non contextualisée comme du renseignement actionnable trompe son commanditaire. Maîtriser ces distinctions est la condition de la crédibilité du métier.

#### 4.2 Donnée brute

Une **donnée brute** est un élément informationnel non contextualisé, isolé, sans qualification ni interprétation.

**Exemples.**
- `192.168.1.42` est une adresse IP. C'est une donnée brute.
- `m.delaunay@technovert.fr` est une adresse email. C'est une donnée brute.
- Une photographie de profil sur LinkedIn. C'est une donnée brute.
- Un timestamp `2025-09-12T14:32:00Z`. C'est une donnée brute.

Une donnée brute en elle-même **ne dit rien**. Elle n'a pas de valeur opérationnelle sans contextualisation. Le travail de l'analyste commence quand la donnée brute devient information.

#### 4.3 Information

Une **information** est une donnée brute **contextualisée** : on sait d'où elle vient, à quoi elle se rapporte, dans quel contexte elle a été produite.

**Exemples.**
- « L'adresse email `m.delaunay@technovert.fr` figure dans le pied de page d'un communiqué de presse TechnoVert du 12 mars 2024, attribuée à Marc Delaunay, DAF. » C'est une information.
- « La photographie X publiée sur le profil LinkedIn de Marc Delaunay le 8 janvier 2025 montre une silhouette en costume sombre devant un fond uni. » C'est une information.
- « Le timestamp 2025-09-12T14:32:00Z apparaît dans les métadonnées EXIF d'une photo téléversée sur Facebook par le compte M.Delaunay. » C'est une information.

Une information **dit quelque chose** mais ne suffit pas à conclure. Elle peut être vraie, fausse, partielle, manipulée. Elle attend d'être qualifiée.

#### 4.4 Indice

Un **indice** est une information qui **oriente une hypothèse**.

**Exemples.**
- « L'email `m.delaunay@technovert.fr` apparaît également dans le WHOIS du domaine `delta-consulting.eu`. » C'est un indice : il oriente l'hypothèse que Delaunay est lié à Delta Consulting.
- « La photographie de profil LinkedIn de Marc Delaunay a un score Hive Moderation de 78 % "likely AI-generated". » C'est un indice : il oriente l'hypothèse que la photo est synthétique.

Un indice **n'établit pas un fait**. Il oriente, il suggère, il appelle vérification. Un indice isolé ne suffit pas. Un faisceau d'indices convergents peut établir un fait.

#### 4.5 Faisceau d'indices

Un **faisceau d'indices** est un ensemble d'indices convergents pointant vers la même conclusion.

**Exemple.**
- Indice 1 : email `m.delaunay@technovert.fr` dans WHOIS de `delta-consulting.eu`.
- Indice 2 : Marc Delaunay enregistré comme director unique de Delta Consulting Ltd auprès du Companies Registry maltais.
- Indice 3 : adresse de domiciliation Delta Consulting partagée avec 46 autres entités identifiées par un même registered agent.
- Indice 4 : flux entrant de TechnoVert SAS vers Delta Consulting documenté dans une fuite de comptes maltais (Cyprus Confidential).

Le faisceau **converge** vers la conclusion : Delaunay contrôle Delta Consulting et a organisé des flux entre TechnoVert et cette société. Aucun indice isolé ne le prouverait. Ensemble, ils établissent un fait avec un niveau de confiance élevé.

#### 4.6 Fait établi

Un **fait** est un élément établi par au moins deux sources indépendantes, cotées, et corroborantes.

**Critères.**
- Deux sources minimum.
- Sources **indépendantes** (un article qui en cite un autre n'est pas une seconde source — c'est la même source recyclée).
- Sources **cotées** (fiabilité connue, traçabilité documentée).
- **Corroboration** : les sources disent la même chose sur le même objet.

**Exemple.**
- Fait : « Delaunay est administrateur de Delta Consulting Ltd à Malte. »
- Sources : Companies Registry maltais (A1) + acte notarié reproduit dans Cyprus Confidential (B2).
- Conclusion : fait établi avec niveau de confiance élevé.

Un fait est **opposable**. Il peut être versé dans un rapport, défendu en audition, contre-expertisé. Il porte sa cotation.

#### 4.7 Hypothèse

Une **hypothèse** est une explication candidate des faits.

**Exemples (hypothèses concurrentes sur Delaunay).**
- H1 : Delaunay détourne sciemment des fonds de TechnoVert vers Delta Consulting pour son enrichissement personnel.
- H2 : Delaunay opère une optimisation fiscale agressive mais légale, pour compte de TechnoVert.
- H3 : Delaunay est administrateur nominee, contrôlé par un tiers, et n'a pas de bénéfice direct.

Une hypothèse n'est ni vraie ni fausse a priori. Elle est **testée** contre les faits (méthode ACH — Ch.79). La meilleure hypothèse n'est pas celle qui confirme nos préjugés, c'est celle qui résiste à la réfutation.

#### 4.8 Preuve

Une **preuve** est un fait qui établit la véracité d'une hypothèse au-delà du raisonnable.

L'OSINT produit **rarement des preuves au sens judiciaire**. Elle produit du renseignement coté qui oriente l'enquête judiciaire ou la décision opérationnelle. La preuve, au sens pénal, suppose une procédure (perquisition, audition, expertise judiciaire) que l'analyste OSINT ne maîtrise pas.

Cette limite est centrale. L'analyste OSINT qui présente ses conclusions comme des « preuves » trompe son commanditaire et expose le dossier. La formulation correcte est : « éléments compatibles avec », « faisceau d'indices convergents vers », « niveau de confiance élevé que… » — pas « preuve de ».

#### 4.9 Renseignement actionnable

Le **renseignement** est un fait ou un ensemble de faits contextualisés, analysés, cotés, et présentés avec un niveau de confiance explicite à un commanditaire en vue d'une **décision**.

**Caractéristiques.**
- **Pertinent** par rapport à la question du commanditaire.
- **Coté** (fiabilité, niveau de confiance).
- **Tracé** (sources documentées).
- **Honnête** sur ses limites.
- **Actionnable** : il oriente une décision.

C'est le **livrable final** du métier. Un renseignement de qualité peut tenir en une page (note flash) ou s'étendre sur 80 pages (rapport complet) — l'important est qu'il respecte les critères ci-dessus.

#### 4.10 Risque de surinterprétation

L'erreur classique : passer trop vite d'un indice à un fait, d'un fait à une preuve, d'une preuve à un verdict. Cette surinterprétation est le piège constant.

**Réflexes pour s'en protéger.**
- Demander systématiquement : ai-je le niveau d'évidence suffisant pour cette affirmation ?
- Formuler en niveau intermédiaire si nécessaire : « plusieurs éléments suggèrent que… », plutôt que « il est établi que… ».
- Appliquer l'ACH (Ch.79) : ai-je testé les hypothèses alternatives ?
- Cotation systématique (Ch.84) : chaque fait porte sa fiabilité.
- Revue par pair : un confrère relit avec un œil frais.
- Délai de réflexion : laisser dormir le rapport 24-48h avant de l'envoyer.

#### 4.11 Synthèse opérationnelle

| Niveau | Caractéristique | Exemple |
|---|---|---|
| Donnée brute | Élément isolé non contextualisé | `m.delaunay@technovert.fr` |
| Information | Donnée contextualisée | Email cité dans communiqué TechnoVert |
| Indice | Information orientant une hypothèse | Email apparaît aussi dans WHOIS Delta Consulting |
| Faisceau d'indices | Plusieurs indices convergents | Email + registre + nominee + fuite |
| Fait | Établi par 2+ sources indépendantes cotées | Delaunay administrateur Delta (A1+B2) |
| Hypothèse | Explication candidate testable | Delaunay détourne des fonds |
| Preuve | Fait établissant véracité d'hypothèse | Rare en OSINT pur |
| Renseignement | Faits analysés, cotés, livrés pour décision | Rapport complet ou note flash |

> **Principe directeur.** Quand vous écrivez un rapport, demandez-vous pour chaque affirmation : à quel niveau suis-je ? Suis-je au niveau d'évidence requis pour ce que j'affirme ? Si non, reformulez en niveau inférieur. La discipline du niveau est la première protection contre la surinterprétation.

-----

### Chapitre 5 — Cycle du renseignement appliqué à l'OSINT

#### 5.1 Origine et utilité du cycle

Le **cycle du renseignement** est le cadre méthodologique qui structure toute production de renseignement, quelle que soit la discipline (HUMINT, SIGINT, OSINT, all-source). Il a été formalisé par les services occidentaux dans les années 1940-1950 et reste la référence doctrinale, malgré ses limites (le « cycle » n'est en réalité jamais strictement séquentiel).

Son utilité, appliquée à l'OSINT, est triple : il **prévient les deux pièges classiques** (collecte qui ne mène à rien faute d'orientation, rapport bâclé faute d'analyse), il **structure la communication** avec le commanditaire (chaque étape est lisible), et il **rend l'enquête reproductible** (un confrère peut reprendre à n'importe quelle étape).

#### 5.2 Phase 1 — Orientation

L'**orientation** est la phase la plus importante et la plus négligée. C'est ici que se forme la **question de renseignement**.

**Activités.**
- Réception et compréhension de la demande du commanditaire.
- Reformulation en questions de renseignement (intelligence requirements).
- Identification des sélecteurs initiaux.
- Définition du périmètre et des limites.
- Évaluation des risques juridiques et éthiques.
- Validation du mandat.
- Fixation des critères d'arrêt (quand l'enquête est-elle suffisante ?).

**Erreurs classiques.**
- Lancer la collecte sans questions claires.
- Accepter un mandat trop large (« faire le tour de tout ce qu'on sait sur X »).
- Ne pas reformuler la demande avec le commanditaire.
- Ne pas définir le périmètre, ce qui mène à la dérive d'enquête.
- Sous-estimer les risques juridiques.

L'orientation prend typiquement **5-15 % du temps total** d'une enquête. C'est peu en temps, beaucoup en impact. Une orientation bâclée invalide tout ce qui suit.

#### 5.3 Phase 2 — Collecte

La **collecte** est la mobilisation des sources pour répondre aux questions.

**Activités.**
- Identification des sources prioritaires.
- Mise en place de l'OPSEC.
- Exécution de la collecte (recherches, captures, requêtes API).
- Documentation systématique dans le journal d'enquête.
- Préservation (Hunchly, SingleFile, hashing).
- Premier tri de pertinence.

**Erreurs classiques.**
- Collecter au hasard, sans hiérarchie de sources.
- Ne pas documenter chaque action.
- Capturer trop ou trop peu.
- Oublier d'archiver les sources fragiles (réseaux sociaux, articles éphémères).
- Sous-estimer les restrictions plateformes en 2026 (Ch.24).

La collecte prend **30-50 % du temps**. C'est la phase la plus chronophage. Une collecte structurée alimente une analyse fluide ; une collecte chaotique paralyse tout ce qui suit.

#### 5.4 Phase 3 — Traitement

Le **traitement** est la mise en forme des données collectées pour les rendre exploitables.

**Activités.**
- Nettoyage (suppression des doublons, des éléments hors périmètre).
- Organisation (vault Obsidian structuré, taxonomie d'entités).
- Indexation (référencement des éléments, codes de suivi).
- Déduplication (fusion d'entités, résolution d'identités — Ch.82).
- Conversion (PDF, OCR, transcription audio/vidéo si nécessaire).
- Traduction (LLMs comme assistants — Ch.61).
- Préparation du matériau pour l'analyse.

**Erreurs classiques.**
- Sauter le traitement (« je vais analyser au fil de l'eau »).
- Conserver tout en vrac sans structuration.
- Confondre traitement et analyse.

Le traitement prend **10-20 % du temps**. Il est invisible dans le livrable final mais indispensable.

#### 5.5 Phase 4 — Analyse

L'**analyse** est la transformation du matériau collecté et traité en renseignement.

**Activités.**
- Corrélation des éléments (graphes, timelines, matrices source/information).
- Formulation d'hypothèses concurrentes.
- Application de l'**ACH** (Analysis of Competing Hypotheses — Ch.79).
- Test contre les évidences (quelles hypothèses sont compatibles ? Lesquelles sont infirmées ?).
- Cotation de chaque fait (Admiralty — Ch.84).
- Évaluation des biais cognitifs (Ch.80).
- Raisonnement adversaire (Ch.81).
- Formulation des conclusions en niveau de confiance (WEP — Ch.85).

**Erreurs classiques.**
- Sauter à l'hypothèse confortable sans test.
- Confondre indices et faits (Ch.4).
- Confirmer ce qu'on cherche (biais de confirmation).
- Surinterpréter (chercher une preuve dans un indice).
- Mal coter (cotation par confort, pas par méthode).

L'analyse prend **20-30 % du temps**. C'est la phase qui fait la valeur du métier. Une analyse rigoureuse distingue le renseignement du bruit.

#### 5.6 Phase 5 — Diffusion

La **diffusion** est la production et la transmission du livrable au commanditaire.

**Activités.**
- Rédaction du rapport (note courte ou rapport complet).
- Production des annexes (graphes, timelines, fiches entités).
- Revue par pair (si possible).
- Choix du canal de transmission (TLP, sécurité).
- Transmission effective.
- Briefing oral si demandé.

**Erreurs classiques.**
- Rédiger à chaud, dans l'enthousiasme de la découverte.
- Ne pas faire revoir le rapport.
- Excéder le vocabulaire calibré.
- Diffuser par canal non sécurisé.
- Oublier la classification TLP.

La diffusion prend **10-20 % du temps**. C'est la phase la plus visible — c'est le seul moment où le commanditaire voit votre travail.

#### 5.7 Phase 6 — Feedback

Le **feedback** est le retour du commanditaire et l'itération de l'enquête.

**Activités.**
- Réception du retour du commanditaire (questions, demandes de précision, nouvelles pistes).
- Identification des questions ouvertes.
- Planification éventuelle d'une seconde itération.
- Veille post-rapport (Ch.92).
- Capitalisation interne (leçons apprises, modèles réutilisables).

**Erreurs classiques.**
- Considérer l'enquête terminée à la diffusion.
- Ne pas solliciter de retour structuré.
- Ne pas mettre en place la veille post-rapport.
- Ne pas capitaliser pour les enquêtes futures.

#### 5.8 Le cycle n'est pas linéaire

En pratique, les phases **se chevauchent et se rétroactivent**.

- L'orientation est souvent affinée pendant la collecte (on découvre que la question initiale était mal posée).
- La collecte se poursuit pendant l'analyse (on identifie de nouveaux sélecteurs à explorer).
- L'analyse peut renvoyer à de la collecte complémentaire.
- La diffusion peut générer un feedback qui relance un nouveau cycle.

Le cycle est donc un **cycle en spirale** : on monte en compréhension à chaque itération. Une enquête complexe peut comporter 3-5 itérations du cycle. La discipline du cycle prévient le chaos, mais elle n'impose pas une rigidité contre-productive.

#### 5.9 Adaptation aux contextes urgents

Dans certains contextes (urgence opérationnelle, crise, breaking news), le cycle est **compressé**. Une note flash en 4 heures suit toujours les six phases, mais chacune ne dure que 30-45 minutes. Le risque est de sacrifier l'analyse au profit de la vitesse. La discipline reste : même en urgence, on cote, on trace, on documente les limites.

#### 5.10 Le cycle et l'IA

L'**arrivée de l'IA en 2025-2026** transforme partiellement le cycle.

- **Collecte automatisée** : agents qui collectent en continu (Ch.67).
- **Traitement assisté** : LLMs pour extraction d'entités, traduction, classification.
- **Analyse augmentée** : LLMs pour synthèse de corpus, génération d'hypothèses (à valider).
- **Diffusion accélérée** : aide à la rédaction.

Mais le cœur du cycle — formulation de la question, jugement, cotation, formulation calibrée, décision éthique — **reste humain**. L'analyste devient orchestrateur d'agents, pas exécutant manuel. C'est ce que la Partie IX du cours développe.

-----
