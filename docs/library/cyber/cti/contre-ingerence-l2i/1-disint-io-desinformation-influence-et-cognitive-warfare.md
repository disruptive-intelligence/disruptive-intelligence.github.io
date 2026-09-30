---
title: DISINT / IO — Désinformation, influence et cognitive warfare
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
chapter: 1
chapters: 7
---

**Cours expert — Niveau professionnel opérationnel**
**Version 1.0 — Avril 2026**

---


## Fil rouge — Opération BROUILLARD

> **Contexte narratif.** Élise Renaud, 34 ans, analyste au sein de la cellule « Menaces informationnelles » d'un ministère européen (structure inspirée du modèle VIGINUM), est mobilisée sur une campagne d'ingérence informationnelle détectée à quatre mois d'une élection européenne. La campagne combine des comptes inauthentiques sur X et TikTok, des sites de réinformation en français et en allemand, un réseau Telegram amplifiant des narratifs polarisants, du contenu généré par IA (deepfakes audio d'un candidat, fausses images), et un hack-and-leak de documents internes d'un parti politique. L'investigation remonte progressivement vers un prestataire technique identifié dans des opérations antérieures liées à un acteur étatique.
>
> **Progression narrative** : détection initiale (signaux faibles) → qualification → cartographie du réseau → analyse des narratifs → attribution technique → coordination inter-agences → contre-mesures → retex post-électoral.

---


## PARTIE I — FONDATIONS

---

### Chapitre 1 — Qu'est-ce que la guerre informationnelle

#### 1.1 Définitions et périmètre

La guerre informationnelle désigne l'ensemble des actions offensives et défensives visant à exploiter, protéger ou dégrader l'environnement informationnel d'un adversaire — c'est-à-dire les systèmes, les contenus et les processus cognitifs par lesquels une société produit, diffuse et interprète l'information. Elle ne se limite pas à la diffusion de faux contenus : elle englobe la manipulation des perceptions, la subversion des processus de décision et l'exploitation des vulnérabilités cognitives d'une population cible.

Plusieurs terminologies coexistent, issues de traditions stratégiques différentes. L'*information warfare* anglo-saxonne renvoie historiquement à une acception large, incluant la guerre électronique, les opérations psychologiques (PSYOP), la déception militaire et les opérations sur les réseaux informatiques. Les *influence operations* (IO) se concentrent sur la dimension cognitive : modifier les attitudes, les comportements ou les décisions d'un public cible par des moyens informationnels. Les PSYOP, issues du vocabulaire militaire américain (renommées MISO — Military Information Support Operations en 2010), visent spécifiquement à influencer les émotions, attitudes et comportements d'audiences étrangères. La *propagande*, enfin, est un terme plus ancien, aujourd'hui connoté péjorativement, mais qui reste une catégorie analytique pertinente : la diffusion délibérée et systématique de messages pour influencer les opinions, qu'elle soit ouverte (propagande blanche, source identifiée) ou clandestine (propagande noire, source dissimulée ou attribuée faussement).

La convergence de ces concepts est croissante : les opérations contemporaines combinent typiquement des composantes cyber (compromission de systèmes), informationnelles (diffusion de contenus) et cognitives (exploitation de biais). Le terme de « manipulation de l'information », retenu par la France dans sa stratégie nationale de lutte (2018) et repris au niveau européen sous l'acronyme FIMI (*Foreign Information Manipulation and Interference*), a l'avantage de qualifier à la fois le contenu (inexact ou trompeur), le comportement (artificiel ou coordonné) et l'intention (porter atteinte aux intérêts fondamentaux).

#### 1.2 Le spectre de la manipulation de l'information

Toute influence n'est pas manipulation. La diplomatie publique, le plaidoyer (advocacy), le lobbying, la communication politique, le journalisme d'opinion sont des pratiques légitimes d'influence dans une société démocratique. Le problème commence quand l'influence recourt à des moyens inauthentiques (faux comptes, identités fictives, coordination clandestine), à des contenus délibérément inexacts ou trompeurs, ou quand elle implique un acteur étranger qui dissimule son rôle.

La qualification repose donc sur un faisceau de critères, pas sur le contenu seul. VIGINUM, le service français de vigilance et de protection contre les ingérences numériques étrangères, utilise quatre critères cumulatifs pour qualifier une ingérence numérique étrangère (INE) : un contenu manifestement inexact ou trompeur ; une diffusion artificielle ou automatisée, massive et délibérée ; une atteinte potentielle aux intérêts fondamentaux de la Nation ; et l'implication directe ou indirecte d'un acteur étranger. Cette grille permet de distinguer le débat public interne, même virulent, de l'ingérence caractérisée.

La « ligne grise » entre influence légitime et manipulation hostile est cependant l'un des défis structurants du domaine. Un narratif peut être factuellement exact mais présenté de manière trompeuse (sélection de faits, décontextualisation, cadrage émotionnel). Un acteur étatique peut exprimer une position officielle (légitime) tout en la faisant amplifier clandestinement par des réseaux inauthentiques (illégitime). La distinction entre propagande d'État assumée (RT, CGTN) et manipulation clandestine (Storm-1516, Doppelgänger) est analytiquement claire mais opérationnellement poreuse, car les deux se renforcent mutuellement.

#### 1.3 Mésinformation, désinformation, malinformation (MDM)

Le triptyque MDM, popularisé par le travail de Claire Wardle et Hossein Derakhshan pour le Conseil de l'Europe (2017), reste un cadre de référence utile malgré ses limites.

La **mésinformation** est la diffusion d'informations fausses sans intention de nuire : l'individu qui partage une rumeur en croyant rendre service, le média qui publie une information non vérifiée dans la précipitation. L'absence d'intention malveillante ne réduit pas l'impact : une mésinformation virale peut causer autant de dégâts qu'une désinformation planifiée.

La **désinformation** implique une intention délibérée de tromper. Elle recouvre la création de contenus fabriqués (articles inventés, documents contrefaits, deepfakes), la manipulation de contenus existants (montages, citations hors contexte, images retouchées) et le détournement de contenus réels dans un cadre interprétatif trompeur. La désinformation est le cœur des opérations d'influence documentées dans ce cours.

La **malinformation** est la diffusion d'informations réelles mais dans un but malveillant : fuites ciblées de données privées, doxxing, publication de conversations privées hors contexte. Le hack-and-leak (Ch.9) relève typiquement de cette catégorie quand les documents publiés sont authentiques mais instrumentalisés.

**Limites du triptyque.** En pratique, la distinction est souvent floue. Les opérations sophistiquées mêlent contenus vrais et faux — une technique efficace consiste à injecter des documents falsifiés dans un corpus de vrais documents fuitées (poison pill). De plus, le triptyque ne capture pas la dimension comportementale : un contenu factuel diffusé par des milliers de comptes coordonnés inauthentiques constitue une manipulation même si le message est exact. C'est pourquoi les cadres d'analyse contemporains — DISARM (Ch.6, Annexe B), ABCDE Framework de l'EEAS, Online Operations Kill Chain de Nimmo et Hutchins — complètent la taxonomie MDM en intégrant les comportements, les acteurs et les canaux, pas seulement le contenu.

#### 1.4 Pourquoi c'est un sujet critique en 2025-2026

Plusieurs dynamiques convergent pour faire de la guerre informationnelle l'un des enjeux stratégiques majeurs de la période actuelle.

L'**IA générative** a transformé l'économie de la désinformation. Le coût marginal de production d'un contenu trompeur — texte, image, audio, vidéo — tend vers zéro. Un opérateur peut désormais produire des articles adaptés culturellement et linguistiquement dans des dizaines de langues, générer des deepfakes audio de qualité suffisante pour être crédibles, et créer des milliers de profils visuellement uniques pour les réseaux sociaux. Le rapport VIGINUM de février 2025 sur les défis de l'IA dans la lutte contre les manipulations de l'information constate toutefois que l'IA représente pour l'instant davantage une « évolution » qu'une « révolution » : elle industrialise les modes opératoires existants mais n'a pas encore engendré de modes opératoires inédits. Le verrou principal reste la diffusion et la viralité, pas la production. Cette évaluation est toutefois susceptible d'évoluer rapidement (voir Ch.27).

La **polarisation politique** dans les démocraties occidentales crée un terreau fertile pour les opérations d'influence. Les sociétés fragmentées sont plus vulnérables : les opérations n'ont pas besoin de créer des fractures, elles exploitent et amplifient celles qui existent déjà. Les sujets de polarisation — immigration, identité, coût de la vie, politique étrangère — sont systématiquement instrumentalisés par les campagnes documentées.

Le **cycle électoral mondial** est dense. Le 4e rapport EEAS sur les menaces FIMI (mars 2026) documente 540 incidents à l'échelle mondiale pour 2025, avec une intensification autour des processus électoraux. L'Ukraine reste la cible principale, suivie de la France, de la Moldavie et de l'Allemagne. En 2024, les élections européennes à elles seules avaient fait l'objet de 42 tentatives FIMI russes documentées par l'EEAS.

Les **conflits armés** sont devenus des champs de bataille informationnels majeurs. Le conflit russo-ukrainien est le cas le plus documenté de guerre informationnelle moderne, combinant propagande militaire, désinformation massive, contre-narratif stratégique et OSINT citoyenne à une échelle sans précédent. Le conflit au Proche-Orient a ajouté une dimension supplémentaire avec une guerre des images multipartite et un fact-checking sous pression opérationnelle extrême.

L'**effondrement de la confiance institutionnelle** amplifie la vulnérabilité. La défiance envers les médias, les gouvernements, les institutions scientifiques et les plateformes technologiques crée un vide que les opérations d'influence comblent. Le phénomène du « deep doubt » — un scepticisme généralisé où les citoyens ne parviennent plus à distinguer le vrai du faux — est lui-même une conséquence et un objectif des campagnes de manipulation. Le concept de « dividende du menteur » théorisé par des chercheurs de Yale illustre ce mécanisme : plus une société apprend à douter, plus il devient facile pour un menteur de nier des faits pourtant irréfutables.

#### 1.5 Articulation avec la bibliothèque

Ce cours couvre la guerre informationnelle comme phénomène stratégique, opérationnel et analytique. Il s'articule avec plusieurs autres cours de la bibliothèque sans en dépendre.

Le cours **Intelligence économique** (IE) traite de l'influence dans un prisme entreprise et souveraineté économique — les chapitres 18-22 de ce cours IE couvrent la guerre économique informationnelle, les campagnes de déstabilisation visant des entreprises, et la protection du patrimoine informationnel. Le présent cours complète cette perspective par le prisme étatique et géopolitique.

Le cours **CTI** (Cyber Threat Intelligence) traite de l'attribution technique des cyberattaques — les méthodes de suivi d'infrastructure, d'analyse de TTPs et d'attribution sont directement transposables aux opérations d'influence (Ch.13, Ch.16). Les opérations de type hack-and-leak (Ch.9) font le pont entre CTI et guerre informationnelle.

Le cours **OSINT Mastery** fournit le socle technique de détection — analyse de réseau social, analyse d'images, investigation d'infrastructure, collecte sur Telegram et plateformes fermées. Le présent cours mobilise ces techniques dans le contexte spécifique de la lutte contre les manipulations de l'information.

Le cours **APT** traite des groupes de menace persistante avancée, dont certains opèrent dans le domaine informationnel (APT28/GRU dans les opérations hack-and-leak, unité 29155 dans la coordination de Storm-1516). La convergence entre cyberespionnage et opérations d'influence est une tendance documentée.

> **🔵 BROUILLARD — Épisode 1**
> Élise Renaud reçoit un signalement automatique un lundi matin : le système de monitoring a détecté 47 comptes X créés en moins de 72 heures, partageant les mêmes URLs vers trois sites web se présentant comme des médias d'actualité alternative en français. Les noms de domaine sont enregistrés depuis moins de deux semaines. Les comptes ont des biographies construites, des photos de profil variées, et ont commencé à publier du contenu non politique avant de pivoter vers des narratifs polarisants sur l'immigration et la politique étrangère européenne. Premier réflexe d'Élise : s'agit-il d'un faux positif — une campagne marketing mal calibrée, un réseau de spam commercial — ou des signaux précurseurs d'une opération coordonnée ? Elle ouvre une fiche de triage et lance les premières vérifications : ancienneté des comptes, cohérence des photos de profil, analyse des URLs partagées, horaires de publication.

---

### Chapitre 2 — Histoire des opérations d'influence : de la propagande classique au numérique

#### 2.1 Les racines : de la propagande de guerre aux opérations actives soviétiques

Les opérations d'influence ne sont pas un phénomène numérique. La propagande de guerre organisée à l'échelle industrielle apparaît dès la Première Guerre mondiale, avec les Commissions Creel aux États-Unis et le War Propaganda Bureau britannique (Wellington House). Les affiches, tracts, films et articles de presse sont déjà calibrés pour cibler des émotions spécifiques — la colère, la peur, le patriotisme — et modifier les comportements d'une population.

Pendant la Seconde Guerre mondiale, la propagande devient une arme stratégique assumée. Le ministère de la Propagande du Reich (Goebbels), la BBC comme outil de guerre psychologique, la Voice of America : chaque belligérant investit massivement dans la capacité d'influencer les perceptions de l'ennemi, des neutres et de sa propre population.

La Guerre froide marque l'âge d'or des opérations d'influence institutionnalisées. L'Union soviétique développe une doctrine explicite de *dezinformatsiya* (désinformation) au sein du KGB, département A puis service A de la Première direction principale. Les « mesures actives » (*aktivnye meropriyatia*) englobent un spectre large : désinformation médiatique, agents d'influence, organisations de front, contrefaçons de documents officiels, campagnes de subversion. L'opération INFEKTION (1983-1987), qui visait à faire croire que le virus du SIDA avait été créé par le Pentagone dans un laboratoire de Fort Detrick, est l'une des plus documentées : lancée par un article planté dans un journal indien, elle a été reprise par des médias dans plus de 80 pays avant d'être retracée au KGB. Côté occidental, la CIA mène ses propres opérations d'influence — financement de médias, de syndicats et d'organisations culturelles (Congrès pour la liberté de la culture), opérations de déstabilisation politique — avec des méthodes comparables.

Ce qui change avec le numérique n'est pas la nature des opérations mais leur échelle, leur coût et la difficulté d'attribution. Les mécanismes psychologiques exploités restent fondamentalement les mêmes (Ch.4).

#### 2.2 Le tournant numérique : des forums aux réseaux sociaux

L'avènement d'Internet puis des réseaux sociaux a transformé la guerre informationnelle en supprimant trois verrous historiques.

Le premier verrou supprimé est celui de l'**accès à la diffusion**. Pendant des décennies, la capacité de toucher une audience de masse était réservée aux États, aux grands médias et aux organisations disposant d'infrastructures de diffusion (antennes, presses, réseaux de distribution). Les réseaux sociaux ont démocratisé cette capacité : n'importe quel acteur peut désormais publier un contenu potentiellement viral, sans intermédiaire éditorial, sans investissement lourd, et depuis n'importe quel point du globe.

Le deuxième verrou est celui du **coût**. Une opération d'influence qui aurait nécessité des dizaines d'agents, des couvertures médiatiques plantées dans plusieurs pays et des mois de préparation peut désormais être conduite par une équipe réduite avec des comptes créés en quelques heures. L'Internet Research Agency (IRA) de Saint-Pétersbourg, avec un budget mensuel estimé à 1,25 million de dollars en 2016, a touché des dizaines de millions d'Américains via Facebook et Instagram. Le rapport coût/impact est sans équivalent dans le spectre des opérations hybrides.

Le troisième verrou est celui de l'**attribution**. Les opérations traditionnelles laissaient des traces — agents identifiables, circuits de financement, chaînes de commandement. Les opérations numériques peuvent être conduites derrière des couches d'anonymisation (VPN, proxies, registrars anonymes, cryptomonnaies), avec des identités fictives et des infrastructures éphémères. L'attribution technique est possible mais coûteuse en temps et en expertise, et l'attribution publique est une décision politique, pas seulement technique (Ch.16).

#### 2.3 Les opérations fondatrices de l'ère moderne

Plusieurs opérations ont structuré la compréhension contemporaine de la guerre informationnelle numérique.

L'**opération IRA/GRU autour de l'élection américaine de 2016** est fondatrice à plusieurs titres. Elle combine pour la première fois à grande échelle deux volets habituellement distincts : une opération d'influence sociale (IRA — création de faux comptes, de groupes Facebook, de publicités ciblées, organisation de manifestations réelles via des personnages fictifs) et une opération cyber (GRU/APT28 — compromission du DNC et de John Podesta, exfiltration d'emails, publication via DCLeaks, Guccifer 2.0 et WikiLeaks). L'étude détaillée de cette opération fait l'objet du Ch.23.

Les **Macron Leaks** de 2017, survenues 48 heures avant le second tour de l'élection présidentielle française, illustrent le hack-and-leak dans un contexte électoral européen. La publication de 20 000 emails et documents internes de la campagne d'Emmanuel Macron, enrichis de quelques documents falsifiés, visait à reproduire le schéma de 2016. L'opération a été contenue par plusieurs facteurs : le timing (la période de réserve électorale limitait l'amplification médiatique), la préparation de la campagne Macron (qui avait anticipé le risque) et la réaction des autorités françaises.

Les **campagnes africaines** de la galaxie Prigozhin/Wagner, actives depuis 2018-2019 en Centrafrique, au Mali, au Burkina Faso, à Madagascar et dans d'autres pays, illustrent le modèle « influence + présence militaire ». Les opérations informationnelles y sont indissociables d'un projet géopolitique et économique — légitimer la présence de mercenaires, décrédibiliser la France et les partenaires occidentaux, construire un récit de libération « néocoloniale ». Ces opérations sont aujourd'hui poursuivies sous de nouvelles formes par le Corps africain et des structures comme African Initiative (Ch.24, Ch.26).

#### 2.4 L'évolution 2020-2026 : professionnalisation, industrialisation, IA

La période 2020-2026 est marquée par plusieurs tendances lourdes.

La **professionnalisation** des opérations se traduit par des chaînes de diffusion de plus en plus complexes. Le mode opératoire Storm-1516, documenté par VIGINUM dans un rapport technique de mai 2025, illustre cette évolution : la chaîne opérationnelle passe par une phase de planification (conception de narratifs, recrutement d'acteurs, génération de deepfakes), une primo-diffusion via des comptes jetables ou rémunérés, un blanchiment par des médias étrangers rémunérés ou des comptes de réseaux sociaux, et une amplification par un réseau d'influenceurs, de chaînes Telegram et de MOI connexes (CopyCop, Lakhta). Cette complexité rend la détection et l'attribution plus difficiles.

La **sous-traitance** et la privatisation de l'influence se développent. Des entreprises privées offrent des services d'influence-as-a-service : Team Jorge (Israël, révélé en 2023), l'Archimedes Group, et d'autres acteurs moins documentés proposent des opérations clés en main à des clients étatiques ou privés. Le modèle économique est celui du mercenariat informationnel — un client passe commande, un prestataire exécute, l'attribution est fragmentée.

L'**IA générative** est intégrée dans les modes opératoires à partir de 2023-2024. Storm-1516 utilise des deepfakes vidéo et audio générés par IA pour mettre en scène de faux témoignages et de faux enregistrements. Les réseaux de type Doppelgänger/RRN utilisent des LLM pour produire et traduire des articles de propagande à grande échelle. Cependant, comme le souligne le rapport VIGINUM sur l'IA et la menace informationnelle, le recours à l'IA ne résout pas le défi principal des opérations : assurer la diffusion et la viralité des contenus, qui reste le principal facteur limitant.

#### 2.5 Leçons historiques : ce qui a changé et ce qui reste constant

Ce qui a **changé** : l'échelle (des dizaines de millions de personnes touchées à faible coût), la vitesse (une opération peut se déployer en heures), le coût (marginal), l'attribution (beaucoup plus difficile), et la multiplicité des acteurs (non plus réservée aux superpuissances).

Ce qui reste **constant** : la cible est toujours le cerveau humain, avec ses biais cognitifs, ses émotions et ses vulnérabilités sociales (Ch.4). Les mécanismes fondamentaux — exploiter la peur et la colère, polariser les groupes sociaux, éroder la confiance dans les institutions, créer la confusion — sont les mêmes que ceux utilisés par le KGB ou la propagande de guerre classique. Les technologies changent, les leviers psychologiques non.

---

### Chapitre 3 — Les acteurs de la guerre informationnelle

#### 3.1 Acteurs étatiques : doctrines par bloc

**Russie.** La Russie est l'acteur étatique le plus documenté et le plus actif dans le domaine des opérations d'influence numériques. Sa doctrine s'inscrit dans le concept de « guerre hybride » et de « contrôle réflexif » (*reflexivnoe upravlenie*) — l'idée que l'on peut amener un adversaire à prendre de lui-même la décision souhaitée par le manipulateur, en contrôlant les informations dont il dispose. L'appareil d'influence russe est composite : le GRU (renseignement militaire) gère les opérations cyber-influence les plus offensives (APT28, unité 29155 liée à Storm-1516), le SVR (renseignement extérieur) aurait repris le contrôle du projet Lakhta après la mort de Prigozhin, le FSB intervient sur le volet intérieur et de contre-espionnage, et une constellation d'acteurs para-étatiques et privés (anciens réseaux Prigozhin, think tanks comme le Centre d'expertise géopolitique, médias d'État comme RT et Sputnik) assurent la diffusion. Le 4e rapport EEAS (mars 2026) attribue 29 % des incidents FIMI documentés à la Russie, sachant que cette proportion ne reflète que les incidents détectés et attribués.

**Chine.** La stratégie informationnelle chinoise est structurellement différente. La Chine poursuit un objectif de « puissance discursive » (*huayuquan*) — la capacité de façonner les termes du débat international en sa faveur. La diplomatie du « loup guerrier » (*wolf warrior diplomacy*), la stratégie du Front uni (*United Front Work Department*) et le réseau médiatique transnational (CGTN, Xinhua, China Daily) constituent les piliers ouverts. Côté clandestin, les opérations documentées — Spamouflage/Dragonbridge — se caractérisent par un volume massif mais une sophistication souvent limitée, avec un impact réel faible sur les audiences occidentales. Toutefois, le 4e rapport EEAS note une montée en compétences, avec un recours croissant à l'IA pour générer des contenus. La Chine cible prioritairement le continent indo-pacifique, les diasporas chinoises, et les institutions internationales. Le rapport EEAS attribue 6 % des incidents FIMI détectés à la Chine — un chiffre probablement sous-estimé du fait des différences de couverture analytique.

**Iran.** L'Iran conduit des opérations d'influence numérique ciblant principalement les audiences du Moyen-Orient, les diasporas iraniennes et, de manière plus limitée, les audiences occidentales. Le modèle inclut des campagnes d'amplification de narratifs anti-israéliens, la création de faux médias en anglais, et des opérations de hack-and-leak ciblées. Le dispositif est moins documenté que celui de la Russie ou de la Chine mais ses capacités sont en développement.

**DPRK (Corée du Nord).** La capacité d'influence numérique de la Corée du Nord est essentiellement tournée vers la propagande interne et le contrôle informationnel de la population. Ses capacités d'influence externe sont limitées mais ses capacités cyber offensives (Lazarus Group) pourraient être utilisées dans des opérations de type hack-and-leak.

#### 3.2 Acteurs para-étatiques et proxies

Le recours à des proxies permet aux États de nier leur implication (plausible deniability) tout en poursuivant leurs objectifs d'influence. La constellation Prigozhin illustre parfaitement ce modèle : l'Internet Research Agency (IRA, rebaptisée plusieurs fois), la société de consulting Concord, et les entités associées à la SMP Wagner ont conduit des opérations d'influence pour le compte de l'État russe tout en maintenant une façade de dénégation. Après la mort de Prigozhin en août 2023, cet appareil a été restructuré : le SVR aurait repris le contrôle du projet Lakhta, les activités militaires sont passées sous la tutelle du GRU via le Corps africain, et de nouvelles structures médiatiques comme African Initiative ont émergé pour poursuivre le volet informationnel en Afrique.

Les **think tanks instrumentalisés** constituent un autre vecteur para-étatique. Le Centre d'expertise géopolitique (CEG), think tank moscovite, est publiquement accusé par le gouvernement américain d'avoir coordonné et financé les opérations de Storm-1516 en lien avec le GRU. Ce type de structure offre une couverture académique ou analytique à des activités d'influence étatique.

Les **médias d'État à vocation internationale** (RT, Sputnik, CGTN, Press TV) fonctionnent comme un système de « blanchiment de narratifs ». Un contenu initialement produit par une opération clandestine peut être repris par un média d'État qui lui confère une apparence de légitimité journalistique, puis être cité par d'autres médias, progressant ainsi dans la chaîne de crédibilité. Le rapport VIGINUM sur Storm-1516 documente comment les narratifs du MOI sont systématiquement amplifiés par des médias d'État russes et des médias liés aux services de renseignement russes (FSB, GRU, SVR).

#### 3.3 Acteurs privés : l'industrie de l'influence-as-a-service

Un marché privé de la désinformation s'est structuré. L'affaire Team Jorge, révélée en 2023 par un consortium de journalistes, a mis au jour une entreprise israélienne proposant des services complets de manipulation électorale : création de faux comptes, diffusion de narratifs, manipulation de sondages en ligne, piratage de comptes de messagerie. Tal Hanan, le dirigeant identifié, affirmait avoir ciblé des processus électoraux dans plus de 30 pays.

Le modèle **Cambridge Analytica** (2014-2018) a montré comment les données personnelles pouvaient être exploitées pour du micro-targeting politique — même si l'efficacité réelle de l'opération reste débattue académiquement. Au-delà de Cambridge Analytica elle-même (dissoute en 2018), le modèle économique de l'exploitation de données pour l'influence ciblée persiste et s'est diversifié.

Des **agences de relations publiques** et des cabinets de conseil en communication proposent des services d'influence qui, sans être illégaux, peuvent s'approcher de la manipulation informationnelle quand ils recourent à des comptes inauthentiques, à des articles sponsorisés non déclarés, ou à des campagnes d'astroturfing.

L'implication pour le praticien est directe : l'attribution d'une opération d'influence ne se résume pas à identifier un État. La chaîne de commandement peut passer par des prestataires privés, des réseaux de proxies, des influenceurs rémunérés et des relais idéologiques sincères. La cartographie de ces acteurs est un enjeu opérationnel majeur (Ch.13, Ch.16).

#### 3.4 Acteurs non étatiques idéologiques

Tous les acteurs de la guerre informationnelle ne sont pas étatiques ou para-étatiques. Des mouvements idéologiques décentralisés conduisent leurs propres opérations d'influence, parfois avec une efficacité supérieure à celle d'acteurs étatiques.

Le phénomène **QAnon** (2017-présent) illustre la dynamique d'un mouvement complotiste décentralisé, né sur des forums anonymes, qui a acquis une audience massive et une réelle influence politique sans structure hiérarchique identifiable. Les mouvements **identitaires** européens et américains utilisent des techniques de coordination en ligne (brigading, memes, hashtag campaigns) sophistiquées. Le **complotisme organisé** autour de la pandémie de COVID-19 a montré la capacité de communautés décentralisées à produire et diffuser de la désinformation à une échelle industrielle.

L'enjeu analytique est que ces acteurs non étatiques peuvent être instrumentalisés par des acteurs étatiques — un État peut amplifier un narratif complotiste existant sans l'avoir créé, rendant la détection et l'attribution plus complexes. La distinction entre amplification opportuniste et activation délibérée est souvent impossible à trancher de manière certaine.

#### 3.5 La convergence : quand les catégories se brouillent

La tendance majeure de la période 2022-2026 est le brouillage des catégories. Des hacktivistes sont instrumentalisés par des services de renseignement. Des influenceurs sont rémunérés sans nécessairement connaître la source de financement. Des acteurs sincèrement convaincus relaient des narratifs initialement injectés par une opération d'influence. Le rapport VIGINUM sur Storm-1516 documente comment les narratifs du MOI sont « parfois repris, de manière inconsciente ou opportuniste, par des personnalités et des représentants politiques de premier plan ».

Cette convergence complique considérablement l'analyse. L'identification d'un réseau coordonné inauthentique ne signifie pas que tous les acteurs qui partagent les mêmes narratifs sont partie prenante de l'opération. La distinction entre amplification coordonnée (inauthentique) et engagement organique (authentique) est l'un des défis méthodologiques majeurs de la détection (Ch.12).

---

### Chapitre 4 — Fondements psychologiques et cognitifs

#### 4.1 Biais cognitifs exploités dans les opérations d'influence

Les opérations d'influence ne fonctionnent pas en convainquant des esprits rationnels par des arguments — elles exploitent les raccourcis cognitifs que le cerveau humain utilise pour traiter l'information en situation d'incertitude ou de surcharge.

Le **biais de confirmation** est le mécanisme le plus systématiquement exploité. Les individus recherchent, interprètent et mémorisent préférentiellement les informations qui confirment leurs croyances existantes. Une opération d'influence ne crée presque jamais une conviction ex nihilo — elle renforce, polarise et radicalise des prédispositions existantes. Un narratif anti-immigration aura un impact maximal sur une audience déjà préoccupée par l'immigration, pas sur une audience neutre. C'est pourquoi les opérations sophistiquées commencent par une phase de reconnaissance de l'environnement informationnel cible pour identifier les fractures exploitables (Ch.6).

L'**effet de vérité illusoire** (*illusory truth effect*) est un levier puissant : la simple répétition d'une affirmation augmente sa crédibilité perçue, indépendamment de sa véracité. Des études expérimentales (Hasher, Goldstein et Toppino, 1977 ; Pennycook et al., 2018) ont démontré que des affirmations fausses étiquetées comme telles sont jugées plus vraies après exposition répétée. Ce mécanisme est directement exploité par les campagnes de flooding — inonder l'espace informationnel avec le même narratif via des centaines de comptes coordonnés pour créer une impression de consensus.

Le **biais d'ancrage** fait que la première information reçue sur un sujet a un poids disproportionné dans le jugement ultérieur. C'est pourquoi le timing de publication est une arme : injecter un narratif avant que les faits ne soient établis (pendant un événement en cours, avant la publication d'un rapport officiel) permet de « cadrer » l'interprétation pour l'ensemble de la couverture médiatique qui suivra.

Le **biais de disponibilité** conduit à surestimer la probabilité d'événements facilement remémorables. En amplifiant massivement des faits divers liés à l'immigration, au terrorisme ou à la criminalité, une opération d'influence peut modifier la perception du risque d'une population entière sans modifier la réalité statistique sous-jacente.

Le **biais de groupe** (*in-group bias*) est exploité par les stratégies de polarisation « nous contre eux ». La construction d'identités de groupe antagonistes — patriotes vs mondialistes, peuple vs élites, nationaux vs migrants — est un mécanisme classique des opérations d'influence, qui exploite le besoin humain d'appartenance sociale.

#### 4.2 Émotions comme vecteur : colère et peur

La recherche sur la viralité des contenus en ligne converge sur un constat : les contenus émotionnels surpassent les contenus factuels en termes de partage et d'engagement. Les émotions à forte activation — la colère, l'indignation, la peur, l'enthousiasme — génèrent plus d'interactions que les émotions à faible activation — la tristesse, la satisfaction. Les études de Berger et Milkman (2012) sur le partage d'articles du New York Times ont montré que la colère et l'anxiété sont les émotions les plus fortement corrélées à la viralité.

Les algorithmes de recommandation des plateformes amplifient ce mécanisme. Conçus pour optimiser l'engagement (temps passé, interactions), ils tendent à favoriser les contenus qui suscitent des réactions émotionnelles fortes. Un contenu polarisant qui génère de l'indignation sera davantage recommandé qu'une analyse nuancée — non par malveillance algorithmique mais par optimisation mathématique d'une fonction d'engagement. Ce phénomène crée une convergence d'intérêts involontaire entre les plateformes (qui maximisent l'engagement) et les opérations d'influence (qui maximisent l'impact émotionnel).

Les opérations documentées exploitent systématiquement ce levier. Storm-1516, par exemple, produit des deepfakes et de faux témoignages conçus pour susciter l'indignation — fausses accusations d'agression sexuelle contre des personnalités politiques, vidéos de menaces terroristes attribuées au Hamas avant les JOP 2024, fausses preuves de corruption de dirigeants ukrainiens. Le mécanisme est le même à chaque fois : un contenu émotionnellement chargé est plus susceptible d'être partagé impulsivement, avant vérification.

#### 4.3 Théories psychosociales mobilisées

Plusieurs cadres théoriques éclairent les mécanismes d'influence à l'échelle collective.

Les **principes de persuasion de Cialdini** (réciprocité, engagement, preuve sociale, autorité, sympathie, rareté) sont mobilisés de manière opérationnelle dans les campagnes d'influence. La preuve sociale — « tout le monde en parle » — est créée artificiellement par l'astroturfing (Ch.7). L'autorité est empruntée en citant des experts fictifs ou en attribuant faussement des propos à des personnalités. La rareté est exploitée par les opérations de « contenu exclusif » et de fausses fuites.

La **dissonance cognitive** (Festinger, 1957) explique pourquoi les individus résistent au debunking : corriger une croyance fausse crée un inconfort psychologique que l'individu résout souvent en rejetant la correction plutôt qu'en modifiant sa croyance. Ce mécanisme est une contrainte fondamentale de la contre-influence (Ch.18) — le debunking factuel a une efficacité limitée sur les personnes déjà convaincues.

La **spirale du silence** (Noelle-Neumann, 1974) décrit comment les individus qui perçoivent leur opinion comme minoritaire tendent à se taire, ce qui renforce l'impression que l'opinion opposée est majoritaire. Les opérations de flooding exploitent ce mécanisme : en créant une masse artificielle de messages portant un narratif, elles peuvent faire taire les voix modérées ou dissidentes.

Les concepts de **chambres d'écho** et de **bulles de filtre** (Pariser, 2011) décrivent les mécanismes de fragmentation informationnelle. Ces concepts sont pertinents mais doivent être nuancés : la recherche récente suggère que l'exposition à des contenus partisans est plus le résultat de choix actifs des utilisateurs que de la seule algorithmique, et que les bulles de filtre sont moins hermétiques que ne le suggérait Pariser.

#### 4.4 Le concept de cognitive warfare (OTAN)

Depuis 2020, l'OTAN a développé le concept de *cognitive warfare* — la guerre cognitive — qui positionne le cerveau humain comme un « domaine opérationnel » au même titre que les domaines terrestre, maritime, aérien, spatial et cyber. L'Innovation Hub de l'OTAN (Norfolk) et le Hub for the South (Naples) ont produit plusieurs rapports cadrant cette doctrine émergente.

Le concept de guerre cognitive va au-delà de la désinformation traditionnelle. Il inclut la manipulation des processus cognitifs eux-mêmes — pas seulement des contenus informationnels mais des mécanismes de raisonnement, de décision et de perception. Les vecteurs envisagés incluent les neurosciences appliquées, les interfaces homme-machine, les technologies de réalité augmentée/virtuelle et les manipulations comportementales à grande échelle via les plateformes numériques.

**Limites du concept.** La notion de cognitive warfare est pertinente comme cadre prospectif mais doit être maniée avec précaution. Le risque est de surestimer les capacités réelles des acteurs — la manipulation cognitive de masse reste techniquement difficile et ses effets sont incertains. Le concept peut aussi devenir un fourre-tout qui dilue la spécificité des différentes formes d'influence. En pratique, les opérations documentées en 2025-2026 relèvent encore largement de la propagande classique numérisée, pas de la manipulation neurocognitive avancée.

#### 4.5 Résilience cognitive : mécanismes de défense

La recherche sur les défenses cognitives contre la désinformation s'est considérablement développée depuis 2018.

Le **prebunking** — préexposer les individus aux techniques de manipulation pour renforcer leur immunité cognitive — est la piste la plus prometteuse. Les travaux de Sander van der Linden et Jon Roozenbeek (Cambridge) ont montré qu'une exposition préalable aux techniques de désinformation (via des jeux sérieux comme « Bad News » ou « Go Viral ! ») réduit significativement la susceptibilité aux contenus manipulés. Google/Jigsaw a déployé des campagnes de prebunking vidéo sur YouTube en Europe de l'Est avec des résultats encourageants. Le prebunking agit en ciblant les techniques (cadrage trompeur, appel émotionnel, fausse autorité) plutôt que les contenus spécifiques, ce qui le rend plus robuste face à l'évolution des narratifs.

Le **debunking** (correction factuelle a posteriori) reste nécessaire mais son efficacité est structurellement limitée. Le « Debunking Handbook » (Lewandowsky et al., 2020) synthétise les bonnes pratiques : répéter le fait correct (pas le mythe), fournir une explication alternative, utiliser des visuels clairs, et éviter l'effet backfire en ne renforçant pas l'exposition au contenu faux. L'effet backfire lui-même — la correction renforce la croyance fausse — est plus rare que ne le suggérait la littérature initiale, mais le « continued influence effect » (persistance de la croyance corrigée) reste documenté.

La **littératie médiatique** — la capacité à évaluer les sources, identifier les biais, comprendre les algorithmes et vérifier les informations — est un levier de résilience à long terme. Les modèles nordiques (Finlande, Estonie) qui intègrent cette éducation dès le primaire montrent des résultats positifs (Ch.21). Cependant, la littératie médiatique a ses limites : elle protège contre les manipulations grossières mais pas nécessairement contre les opérations sophistiquées qui exploitent des informations réelles dans un cadre trompeur.

---

### Chapitre 5 — Cadre juridique et institutionnel

#### 5.1 La liberté d'expression comme contrainte structurante

Le paradoxe fondamental de la lutte contre la désinformation dans les démocraties est que la liberté d'expression — valeur constitutive de l'ordre démocratique — protège aussi le droit de dire des choses fausses. La Déclaration universelle des droits de l'homme (art. 19), la Convention européenne des droits de l'homme (art. 10), le Premier Amendement américain : tous ces textes consacrent une protection forte de la liberté d'expression, y compris pour les opinions fausses, choquantes ou polémiques.

Toute politique de lutte contre la désinformation doit donc naviguer dans cet espace contraint : agir contre la manipulation sans instituer de censure. La distinction opérante n'est généralement pas entre « vrai » et « faux » mais entre comportements authentiques (légitime, même si le contenu est faux) et comportements inauthentiques coordonnés (illégitime, indépendamment du contenu). C'est pourquoi VIGINUM se concentre sur les comportements (diffusion artificielle, coordination inauthentique, implication étrangère) et non sur la véracité des contenus en eux-mêmes.

#### 5.2 Cadre français

Le dispositif français de lutte contre les manipulations de l'information repose sur plusieurs piliers.

**VIGINUM** (Service de vigilance et de protection contre les ingérences numériques étrangères), créé par décret du 13 juillet 2021 et rattaché au Secrétariat général de la défense et de la sécurité nationale (SGDSN), est la pierre angulaire du dispositif. Sa mission est de détecter et caractériser les opérations d'ingérence numérique étrangère en analysant les contenus publiquement accessibles sur les plateformes en ligne. Le service est autorisé à opérer un traitement automatisé de données à caractère personnel par décret du 7 décembre 2021, dans un cadre juridique strict — durée de conservation limitée, supervision par un comité éthique et scientifique. En 2024, VIGINUM comptait 56 agents (moyenne d'âge 33 ans, 24 recrutements dans l'année), et avait détecté 259 phénomènes inauthentiques dont 174 liés à une ingérence numérique étrangère, sur 11 modes opératoires suivis. Le service fonctionne selon une approche fondée sur des critères techniques objectivables, non sur la nature des contenus diffusés — ce qui le distingue d'un organe de censure.

La **loi du 22 décembre 2018 relative à la lutte contre la manipulation de l'information** a créé un cadre pour lutter contre les « fausses informations » en période électorale, permettant la saisine du juge des référés pour faire cesser la diffusion de fausses informations susceptibles d'altérer la sincérité d'un scrutin. Son utilisation effective a été très limitée — la procédure est lourde et le périmètre étroit.

L'**ARCOM** (Autorité de régulation de la communication audiovisuelle et numérique, ex-CSA fusionné avec Hadopi en 2022) régule les contenus audiovisuels et supervise les obligations de transparence des plateformes au titre du DSA.

Le **COMCYBER** (Commandement de la cyberdéfense) et sa composante L2I (Lutte informatique d'influence) opèrent dans le champ militaire — la capacité d'influence offensive de la France en opérations extérieures. Ce volet est distinct de la mission de VIGINUM (défensif et sur le territoire national) et relève du ministère des Armées.

La **DGSI** intervient sur le volet ingérence au titre de la protection du secret de la défense nationale et de la contre-ingérence. La coordination entre ces acteurs est assurée par le SGDSN au niveau interministériel.

#### 5.3 Cadre européen

Le **Digital Services Act** (DSA), en application depuis février 2024 pour les très grandes plateformes et depuis février 2025 pour l'ensemble des services numériques, est le cadre réglementaire le plus structurant. Il impose aux plateformes de réaliser des évaluations des risques systémiques — y compris les risques liés à la manipulation de l'information — et de prendre des mesures d'atténuation proportionnées. Il crée un droit d'accès aux données pour les chercheurs agréés, et impose des obligations de transparence sur la publicité politique et le fonctionnement algorithmique. En pratique, l'application effective du DSA sur la question de la désinformation reste un chantier en cours — les plateformes résistent à certaines obligations d'accès aux données, et l'asymétrie de moyens entre les régulateurs et les plateformes est considérable.

Le **Code de pratique européen renforcé contre la désinformation** (2022) est un engagement volontaire des plateformes qui, combiné au DSA, tend à devenir un cadre de co-régulation. Il prévoit des obligations de transparence sur la publicité politique, des mesures contre les comptes inauthentiques, et un accès facilité aux données pour les chercheurs.

L'**EEAS** (Service européen pour l'action extérieure) et sa division StratCom constituent le bras analytique et opérationnel de l'UE dans la lutte contre les FIMI. La task force East StratCom (créée en 2015) et le projet EUvsDisinfo assurent la veille et la publication de bases de données de cas de désinformation. L'EEAS publie depuis 2023 des rapports annuels sur les menaces FIMI qui constituent des références opérationnelles majeures — le 4e rapport (mars 2026) introduit un « FIMI Deterrence Playbook » marquant un passage d'une posture défensive à une logique de dissuasion active.

#### 5.4 Cadre international

Au niveau international, les normes restent essentiellement déclaratoires. Le processus **UN GGE** (Groupe d'experts gouvernementaux) sur le comportement responsable des États dans le cyberespace a produit des normes de comportement qui incluent la non-interférence dans les processus électoraux, mais leur caractère contraignant est faible et leur application dans le domaine informationnel est contestée.

Le **processus de Tallinn** (NATO CCDCOE) a principalement porté sur le droit international applicable au cyberespace, mais le Tallinn Manual 2.0 (2017) aborde partiellement l'application du droit international aux opérations d'influence, notamment au regard du principe de non-intervention dans les affaires intérieures des États. L'application de ce principe aux opérations informationnelles reste juridiquement controversée — le seuil de coercition requis est rarement atteint par des campagnes de désinformation seules.

L'**Appel de Paris** pour la confiance et la sécurité dans le cyberespace (2018) est un engagement politique de 80+ États et de centaines d'entreprises et organisations en faveur d'un cyberespace sûr, mais sans mécanisme contraignant.

#### 5.5 Limites du droit : la désinformation n'est pas toujours illégale

Le praticien doit intégrer une réalité juridique fondamentale : la plupart des activités constitutives d'une opération d'influence ne sont pas, prises isolément, illégales. Créer un faux compte n'est pas un délit pénal dans la plupart des juridictions — c'est une violation des conditions d'utilisation d'une plateforme privée. Publier une information fausse n'est pas un délit en soi — sauf dans des contextes très spécifiques (diffamation, injure, incitation à la haine, faux en écriture publique, manipulation de cours boursiers). Amplifier un narratif n'est pas illégal — même si les moyens utilisés sont inauthentiques.

La qualification juridique dépend du contexte : une même action peut être une ingérence étrangère (périmètre VIGINUM), un débat démocratique interne (hors périmètre), une satire protégée par la liberté d'expression, ou une erreur de bonne foi. La distinction entre ces catégories est souvent l'enjeu central de la qualification (Ch.12).

Les sanctions disponibles sont principalement extra-judiciaires : signalement aux plateformes (qui appliquent leurs conditions d'utilisation), attribution publique (naming and shaming), sanctions diplomatiques (régime de sanctions UE contre les entités impliquées dans les FIMI — Social Design Agency, Tigerweb, John Mark Dougan sanctionnés en 2024-2025), et, dans certains cas, poursuites pénales pour des infractions connexes (piratage informatique, atteinte au secret de la défense, blanchiment).

> **🔵 BROUILLARD — Épisode 2**
> Élise doit qualifier le phénomène détecté. La question est cruciale : s'agit-il d'une ingérence numérique étrangère — ce qui entre dans le périmètre de sa cellule et permet de mobiliser certains moyens d'investigation — ou d'un débat interne amplifié, qui relèverait d'autres services ou de la seule responsabilité des plateformes ? Les quatre critères sont passés en revue : le contenu est-il manifestement inexact ou trompeur ? Les premiers articles identifiés mélangent des faits réels (chiffres d'immigration) avec des interprétations trompeuses et des affirmations non sourcées — zone grise. La diffusion est-elle artificielle ? Les 47 comptes montrent des indices de coordination (fenêtres temporelles serrées, URLs identiques, création quasi simultanée) — signal fort. Y a-t-il atteinte aux intérêts fondamentaux ? Les narratifs ciblent directement le processus électoral — potentiellement. Y a-t-il implication étrangère ? Pas encore démontré — c'est l'objet de l'investigation. Élise ouvre une fiche d'analyse en « hypothèse INE » et lance les investigations techniques sur l'infrastructure des sites web.


---
