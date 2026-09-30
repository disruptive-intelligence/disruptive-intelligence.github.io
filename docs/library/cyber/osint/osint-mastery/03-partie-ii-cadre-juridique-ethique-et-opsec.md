---
title: PARTIE II — Cadre juridique, éthique et OPSEC
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 3
chapters: 15
---

> **Ce que cette partie apprend.** Maîtriser le cadre juridique français, européen et international dans lequel opère l'analyste OSINT en 2026 ; intégrer les exigences éthiques au-delà du droit ; concevoir une OPSEC adaptée à la menace de l'enquête, y compris face aux plateformes et à l'IA ; opérer des sock puppets dans un cadre légal et déontologique.
>
> **Ce qu'elle ne couvre pas.** La méthodologie d'enquête (Partie III), les techniques de collecte (Parties IV à VII), les outils spécifiques (couverts au fil des chapitres techniques).
>
> **Ce que vous saurez faire après cette partie.** Évaluer la légalité d'une demande, identifier les risques juridiques d'une enquête, monter une infrastructure OPSEC-compatible, créer et opérer des avatars d'enquête sans franchir les limites légales et déontologiques.

-----

### Chapitre 6 — Cadre juridique français de l'investigation OSINT

#### 6.1 Le RGPD comme cadre central

Le **Règlement Général sur la Protection des Données** (RGPD, règlement UE 2016/679, entré en application le 25 mai 2018) est le cadre principal pour toute investigation OSINT en France et dans l'UE. Il s'applique dès qu'une donnée à caractère personnel est traitée, ce qui couvre quasiment toute investigation OSINT sur des personnes physiques.

**Définition d'une donnée personnelle.** Toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement. Un nom, une adresse, un email, un téléphone, une photo, un identifiant en ligne sont des données personnelles. Une adresse IP peut l'être (CNIL et CJUE l'ont confirmé).

**Principes RGPD applicables à l'OSINT.**
- **Licéité du traitement** (art. 6). Une base légale est requise : intérêt légitime de l'investigateur, exécution d'un contrat, mission d'intérêt public, etc. Pour un investigateur privé, l'intérêt légitime est la base la plus fréquente.
- **Finalité déterminée, explicite et légitime**. L'investigateur doit savoir pourquoi il collecte. Une collecte « au cas où » est non conforme.
- **Minimisation des données**. Ne collecter que ce qui est nécessaire à la finalité. Un excès de collecte est une violation.
- **Exactitude**. Les données collectées doivent être exactes et tenues à jour si elles sont conservées.
- **Limitation de la durée de conservation**. Les données ne doivent pas être conservées indéfiniment.
- **Sécurité et confidentialité**. Stockage chiffré, accès restreint, traçabilité.
- **Responsabilité (accountability)**. Capacité à démontrer la conformité.

**Droit des personnes concernées.** Droit d'accès, de rectification, d'effacement, d'opposition. Ces droits peuvent être opposés à l'investigateur dans certains cas, avec des exceptions (intérêt légitime supérieur, mission d'intérêt public, droit à l'information).

**Régimes spécifiques.** Les données sensibles (santé, opinions politiques, religion, orientation sexuelle, biométrie) bénéficient d'une protection renforcée (art. 9). Leur collecte est en principe interdite, sauf exceptions strictes.

#### 6.2 Code pénal : les infractions à connaître

Plusieurs articles du Code pénal français encadrent l'investigation et fixent les limites pénales.

**Article 226-1 — Atteinte à la vie privée.** Punit l'enregistrement ou la transmission de paroles ou d'images d'une personne dans un lieu privé, sans son consentement. Périmètre principalement physique mais peut s'appliquer à certaines captures intrusives en ligne. **1 an d'emprisonnement et 45 000 € d'amende.**

**Article 226-18 — Collecte déloyale.** Punit la collecte de données à caractère personnel par moyen frauduleux, déloyal ou illicite. C'est l'un des articles centraux pour l'OSINT : une collecte qui contourne des protections techniques, qui ruse délibérément, ou qui usurpe une qualité peut tomber sous ce coup. **5 ans d'emprisonnement et 300 000 € d'amende.**

**Article 226-19 — Conservation illicite de données sensibles.** Punit la conservation illégale de certaines catégories de données (origine raciale, opinions politiques, syndicales, religieuses, mœurs, santé). **5 ans et 300 000 €.**

**Article 226-22 — Détournement de finalité.** Punit le détournement de la finalité d'un traitement. Un investigateur qui utilise des données collectées pour une autre fin que celle annoncée tombe sous ce coup. **5 ans et 300 000 €.**

**Article 323-1 — Accès frauduleux à un STAD (Système de Traitement Automatisé de Données).** Punit l'accès ou le maintien frauduleux dans un système informatique. **3 ans et 100 000 €**, 5 ans et 150 000 € si suppression ou modification de données.

**Article 323-3-1 — Mise à disposition de programmes ou données pour accès frauduleux.** **5 ans et 150 000 €.**

**Article 433-19 — Usurpation d'identité.** **1 an et 15 000 €.**

**Articles 226-15 et suivants — Atteinte au secret des correspondances**. L'interception non autorisée de communications privées tombe ici. Risque pénal majeur en cas de tentation d'accéder à un compte.

#### 6.3 La jurisprudence Bluetouff — le cas fondateur

L'**arrêt Bluetouff** (Cour de cassation, chambre criminelle, 20 mai 2015) est l'arrêt fondamental pour comprendre la limite OSINT en France.

**Faits.** Olivier Laurelli (alias Bluetouff), journaliste et blogueur, a accédé à environ 8 Go de données internes de l'ANSES (Agence nationale de sécurité sanitaire) via une simple recherche Google. Les données étaient accessibles publiquement via une URL non protégée, mais leur accès reposait sur une défaillance de configuration. Bluetouff a téléchargé ces données.

**Décision.** La Cour de cassation a confirmé la condamnation pour **maintien frauduleux dans un système de traitement automatisé de données** (art. 323-1). Argument central : même si l'accès initial était techniquement possible sans contournement, le maintien dans le système après avoir compris qu'il s'agissait de données internes constituait un maintien frauduleux. Bluetouff a été condamné à 3 000 € d'amende.

**Conséquences pour l'OSINT.** Cet arrêt établit le principe que **« accessible n'équivaut pas à exploitable sans limite »**. Une donnée techniquement accessible peut être pénalement protégée si l'analyste comprend (ou aurait dû comprendre) qu'il s'agissait d'une donnée non destinée à la diffusion publique.

**Implication pratique.**
- Un bucket S3 mal configuré n'est pas une source OSINT légitime.
- Une page interne accessible via une URL devinée n'est pas exploitable sans précaution.
- Un dump de données apparu en ligne peut être pénalement risqué à consulter et exploiter.
- En cas de doute, **on ne consulte pas, on documente, et on signale**.

#### 6.4 Le principe « accessible ≠ public »

C'est le **corollaire pratique** de la jurisprudence Bluetouff.

Une donnée est **publique** quand :
- Elle est volontairement diffusée par son auteur (post sur un réseau social ouvert, communiqué de presse, registre légal).
- Elle est sur un site dont la diffusion est l'objet (presse, blog, page institutionnelle).
- Elle est indexée par les moteurs et reste accessible sans contournement.

Une donnée est **techniquement accessible mais non publique** quand :
- Elle a été exposée par erreur (bucket mal configuré, URL prédictible non protégée).
- Elle a été extraite d'un système compromis (leak provenant d'un piratage).
- Elle suppose un contournement technique pour y accéder (même mineur).

**Règle pratique.** En cas de doute, traiter comme non public. Ne pas consulter, ne pas exploiter, documenter et signaler le cas échéant à la CNIL ou à l'ANSSI.

#### 6.5 Mandat, finalité et proportionnalité

Trois principes opérationnels structurent l'enquête OSINT en droit français.

**Le mandat.** L'investigateur agit sur mandat (contrat avec un client, mission interne, mandat judiciaire). Le mandat encadre ce qui peut et ce qui ne peut pas être fait. Une investigation sans mandat clair est juridiquement exposée. Pour un consultant : contrat écrit, périmètre défini, finalité documentée.

**La finalité.** Toute collecte a une finalité. L'utilisation des données pour une finalité autre que celle annoncée tombe sous l'art. 226-22 (détournement de finalité). Si la finalité initiale était la due diligence M&A, on ne peut pas réutiliser les données pour une investigation pénale sans une nouvelle base légale.

**La proportionnalité.** La collecte doit être proportionnée à la finalité. Si l'objectif est de vérifier l'existence d'une société écran, on ne collecte pas l'intégralité du profil familial du dirigeant. La sur-collecte est une violation RGPD.

#### 6.6 OSINT pour les LEA versus le secteur privé

Les **services d'État et autorités judiciaires** ont des pouvoirs que le secteur privé n'a pas :
- Réquisitions judiciaires (accès aux données opérateurs, plateformes).
- Interceptions légales (cadre loi renseignement, art. 100 et suivants CPP).
- Perquisitions et saisies.
- Accès à des bases protégées (FOVeS, FIJAIT, etc.).

Les **investigateurs privés** doivent rester strictement dans le périmètre OSINT (accessible publiquement, sans contournement). La tentation d'utiliser des moyens « gris » (bases de données illégalement constituées, paiement de tipsters internes, accès via leaks) expose à des sanctions pénales.

#### 6.7 Cas particulier : les leaks

Le statut juridique des **données fuitées** (leaks, dumps) est complexe.

**Pour les LEA.** Peuvent généralement utiliser les leaks comme sources d'orientation. Cadre judiciaire balise l'usage.

**Pour les journalistes.** Liberté de presse et intérêt public sont des protections fortes. Les ICIJ, OCCRP, médias d'investigation utilisent massivement les leaks (Panama, Pandora, Cyprus Confidential). Risque pénal limité dans un cadre journalistique sérieux.

**Pour les analystes privés non-journalistes.** Zone grise. Consulter un leak public reste généralement toléré. **Exploiter** un leak (intégrer ses données dans un rapport, le commercialiser) est juridiquement plus risqué — particulièrement si les données proviennent d'un piratage avéré.

**Règle pratique.** En l'absence de mandat judiciaire ou de qualité journalistique reconnue, prudence maximale sur l'exploitation des leaks. Documenter l'origine, ne pas reproduire les données, citer les analyses publiées par les sources autorisées (ICIJ notamment) plutôt que d'accéder aux dumps bruts.

#### 6.8 Recours en cas d'incident

Si l'investigateur est sollicité par la personne ciblée (droit d'accès, droit d'effacement, plainte) :

- Répondre dans les délais RGPD (1 mois en général).
- Documenter la base légale du traitement.
- Évaluer si l'opposition de la personne doit être suivie ou si l'intérêt légitime prévaut (notamment dans le cadre d'investigations en cours).
- En cas de doute, consulter un avocat spécialisé.

#### 6.9 La CNIL comme acteur

La **CNIL** (Commission nationale de l'informatique et des libertés) est l'autorité de contrôle française. Elle peut :
- Contrôler les pratiques (sur plainte ou d'office).
- Sanctionner (jusqu'à 4 % du chiffre d'affaires mondial pour les violations RGPD majeures).
- Publier des recommandations et guidelines (à suivre).

Pour les professionnels de l'OSINT, la CNIL n'a pas publié de doctrine sectorielle complète, mais ses recommandations générales sur le RGPD s'appliquent. En cas de doute, consulter le **registre des activités de traitement** de l'organisation et désigner un DPO si l'activité OSINT est significative.

#### 6.10 Synthèse — les 10 réflexes juridiques

1. Vérifier la base légale RGPD du traitement.
2. Documenter la finalité de la collecte.
3. Minimiser la collecte aux données nécessaires.
4. Respecter le principe « accessible ≠ public ».
5. Refuser tout contournement technique (pas de Bluetouff 2).
6. Documenter le mandat (client + finalité + périmètre).
7. Protéger les données collectées (chiffrement, accès restreint).
8. Encadrer la durée de conservation.
9. Préparer les réponses aux droits des personnes concernées.
10. Consulter un avocat en cas de doute, ne pas improviser.

-----

### Chapitre 7 — Cadre européen et international 2024-2026

#### 7.1 Vue d'ensemble

Le cadre juridique européen et international de l'OSINT a évolué de manière substantielle entre 2024 et 2026. Quatre textes structurent désormais la pratique : le **Digital Services Act** (DSA), l'**AI Act**, la **Corporate Sustainability Due Diligence Directive** (CSDDD), et le renforcement des **sanctions internationales**. Côté UK, la **Failure to Prevent Fraud Offence** entre en vigueur en septembre 2025 et change la donne pour la diligence corporate.

#### 7.2 Digital Services Act (DSA)

Le **DSA** (règlement UE 2022/2065, applicable depuis février 2024 pour les très grandes plateformes, août 2024 pour les autres) encadre les plateformes en ligne dans l'UE.

**Apports pour l'OSINT.**
- Obligations de transparence des plateformes (rapports de modération, registres publicitaires).
- Création d'archives publiques (DSA Transparency Database, X Community Notes).
- Désignation des **VLOPs** (Very Large Online Platforms) : Meta, X, TikTok, YouTube, etc., soumises aux obligations les plus strictes.
- Encadrement de la publicité ciblée, traçabilité.
- Possibilité de **dark patterns** restreinte.
- **Accès chercheurs** : les VLOPs doivent fournir un accès aux données aux chercheurs agréés (art. 40), avec des conditions strictes.

**Implication OSINT.** Les archives DSA fournissent une source nouvelle pour l'investigation des opérations d'influence (publicités politiques notamment) et de la modération. L'accès chercheur peut être mobilisé pour des projets académiques agréés.

#### 7.3 AI Act (Règlement UE 2024/1689)

Entré en vigueur le **1er août 2024**, applicable progressivement entre 2025 et 2027. C'est le premier cadre réglementaire complet sur l'IA au monde.

**Architecture par risques.**
- **Risque inacceptable** (interdits) : social scoring, manipulation comportementale subliminale, identification biométrique en temps réel dans l'espace public (avec exceptions très encadrées).
- **Risque élevé** : usages en justice, RH, éducation, infrastructures critiques, biométrie. Obligations strictes (conformité, documentation, supervision humaine, robustesse).
- **Risque limité** : transparence (deepfakes étiquetés, chatbots identifiés).
- **Risque minimal** : libre.

**Apports pour l'OSINT.**
- **Identification de contenus IA** (art. 50) : les fournisseurs de modèles d'IA générative doivent permettre de marquer les contenus générés. Standard **C2PA** retenu de facto.
- **Encadrement de la reconnaissance faciale** : usage privé restreint. PimEyes et équivalents naviguent dans une zone grise.
- **Modèles à usage général** (GPAI) : transparence sur l'entraînement, droit d'auteur, sécurité.
- **Sanctions** : jusqu'à 7 % du chiffre d'affaires mondial pour les violations majeures.

**Implication OSINT.** L'AI Act renforce les obligations de transparence des contenus IA et donne un cadre aux outils de détection. Il restreint les usages les plus invasifs de la reconnaissance faciale par les acteurs privés. L'OSINT doit s'adapter : si vous utilisez des outils de reconnaissance faciale, vérifiez leur conformité AI Act.

#### 7.4 Corporate Sustainability Due Diligence Directive (CSDDD)

La **CSDDD** (directive UE 2024/1760, entrée en vigueur le 25 juillet 2024, transposition nationale à venir) impose un **devoir de vigilance** aux grandes entreprises sur leur chaîne d'approvisionnement, en matière de droits humains et d'environnement.

**Périmètre.**
- Grandes entreprises UE (>1000 employés, >450 M€ CA mondial).
- Grandes entreprises hors UE actives dans l'UE (seuils similaires).

**Obligations.**
- Identification des risques humains et environnementaux dans la chaîne d'activité.
- Prévention et atténuation.
- Reporting et communication.
- Mesures de remédiation.

**Implication OSINT.** La CSDDD fait de l'OSINT un **outil opérationnel obligatoire** pour les directions juridiques, achats et conformité des grandes entreprises. Cartographie des fournisseurs, due diligence renforcée sur les sous-traitants, monitoring continu deviennent des cas d'usage massifs. Le marché de l'OSINT corporate explose en parallèle.

#### 7.5 Sanctions internationales (OFAC, UE, UK, ONU)

Le régime de sanctions s'est considérablement renforcé depuis 2022 (invasion russe de l'Ukraine, sanctions Iran, Corée du Nord, Belarus).

**OFAC** (Office of Foreign Assets Control, US Treasury). Liste **SDN** (Specially Designated Nationals). Extraterritorialité forte (toute transaction touchant le dollar US ou impliquant une entité US peut tomber sous coupe OFAC). Sanctions secondaires : un acteur non-US qui transige avec une entité sanctionnée peut être lui-même sanctionné.

**UE**. Sanctions UE coordonnées via le SEAE. Listes consolidées publiées par la Commission. Effet direct dans tous les États membres.

**UK** post-Brexit. **OFSI** (Office of Financial Sanctions Implementation, HM Treasury). Liste consolidée UK.

**ONU**. Sanctions ONU obligatoires pour tous les États membres. Liste publique.

**Implication OSINT.** Le screening sanctions est devenu un cas d'usage massif. Outils : **OpenSanctions** (gratuit, multi-listes), WorldCheck (payant), Dow Jones Sanctions, Sayari, **Pappers** intègre une partie. La couverture doit être multi-listes et multi-juridictions.

#### 7.6 Failure to Prevent Fraud Offence (UK)

L'**Economic Crime and Corporate Transparency Act 2023** crée une nouvelle infraction au Royaume-Uni : **failure to prevent fraud**, entrée en vigueur le 1er septembre 2025.

**Principe.** Une grande organisation est pénalement responsable si une personne associée (employé, agent, prestataire) commet une fraude pour son bénéfice, sauf si elle peut démontrer qu'elle avait mis en place des **« reasonable prevention procedures »**.

**Périmètre.**
- Organisations >250 employés OU >36 M£ CA OU >18 M£ actifs.
- Couvre fraudes diverses : false accounting, fraud by false representation, fraud by failing to disclose, etc.

**Implication OSINT.** Les entreprises UK et leurs partenaires investissent massivement dans la due diligence préventive. L'OSINT corporate, supply chain, et adverse media devient un outil de mise en conformité.

#### 7.7 Régime américain (vue d'ensemble)

**Premier amendement** : protection forte de la liberté d'expression, plus permissif pour l'OSINT que le cadre européen.

**CCPA / CPRA** (Californie). Cadre privacy comparable au RGPD pour les résidents californiens, applicable aux entreprises traitant leurs données.

**State laws diverses** : Virginie, Colorado, Connecticut, Utah, Texas — patchwork de législations état par état.

**Federal**. Pas de loi privacy fédérale équivalente RGPD. **HIPAA** pour la santé, **GLBA** pour le financier, **COPPA** pour les enfants.

**FCRA** (Fair Credit Reporting Act). Encadre les rapports d'enquête commerciaux. Applicable à certaines pratiques OSINT corporate.

**FOIA** (Freedom of Information Act). Levier OSINT majeur côté US : demandes d'accès à l'information publique des agences fédérales.

#### 7.8 Régime UK post-Brexit

**UK GDPR** (Data Protection Act 2018 + UK GDPR). Très proche du RGPD européen, avec quelques divergences mineures.

**RIPA** (Regulation of Investigatory Powers Act). Encadre la surveillance.

**ICO** (Information Commissioner's Office). Autorité de contrôle.

**Failure to Prevent Fraud** (supra).

#### 7.9 Pays sensibles et juridictions à risque

Certaines juridictions présentent des risques particuliers pour l'OSINT.

**Chine, Russie, Iran, Corée du Nord.** Cadre juridique restrictif. Sanctions occidentales. Investigation depuis l'extérieur reste possible mais sur place quasiment impossible.

**Allemagne.** Forte protection vie privée, jurisprudence stricte sur la photographie de personnes, BDSG. Plus exigeant que le standard RGPD européen sur certains points.

**Suisse**. Hors UE mais cadre privacy équivalent (LPD révisée 2023). Régime spécifique pour les données financières (secret bancaire allégé mais existant).

**Émirats, Singapour, autres hubs financiers.** Régulations en construction, parfois moins strictes que l'UE.

#### 7.10 MiCA et Travel Rule (cadre crypto)

Le règlement **MiCA** (Markets in Crypto-Assets, applicable progressivement depuis 2024) impose un cadre prudentiel aux **VASPs** (Virtual Asset Service Providers) dans l'UE. Implications OSINT : meilleure visibilité des exchanges régulés, durcissement KYC, traçabilité accrue.

La **Travel Rule** (FATF Recommendation 16, transposée en UE) impose que les VASPs échangent des informations sur l'émetteur et le destinataire pour les transferts crypto au-dessus de certains seuils. Implications OSINT : exchanges régulés disposent de plus d'informations sur leurs utilisateurs, ce qui peut être mobilisé en réquisition judiciaire.

*(Pour le détail, renvoi vers le cours OSINT Crypto vFULL.)*

#### 7.11 Synthèse — boussole juridique 2026

| Texte | Juridiction | Applicable | Implication OSINT principale |
|---|---|---|---|
| RGPD | UE | 2018 | Cadre principal collecte données personnelles |
| DSA | UE | 2024 | Transparence plateformes, accès chercheurs |
| AI Act | UE | 2024-2027 | Encadrement IA, marquage contenus, restriction reconnaissance faciale |
| CSDDD | UE | 2024+ | Due diligence supply chain obligatoire |
| MiCA | UE | 2024 | Cadre VASPs crypto |
| CCPA/CPRA | Californie | 2020+ | Privacy résidents Californie |
| Failure to Prevent Fraud | UK | 09/2025 | Due diligence préventive obligatoire |
| Sanctions OFAC | US extraterritorial | Continu | Screening multi-juridictions |
| FOIA | US | 1966 | Levier d'accès information publique |

L'analyste OSINT travaillant à l'échelle internationale doit maîtriser ces régimes croisés. En cas de doute juridique, consultation avocat spécialisé n'est pas optionnelle.

-----

### Chapitre 8 — Éthique, déontologie et responsabilité de l'analyste

#### 8.1 Pourquoi l'éthique au-delà du droit

Le droit pose un plancher, pas un plafond. Un comportement légal peut être profondément non-éthique. L'investigateur OSINT a une responsabilité **déontologique** qui dépasse la conformité juridique stricte.

Trois raisons concrètes.

**Premièrement, l'OSINT touche aux personnes.** Une note d'analyse mal calibrée, une diffusion non maîtrisée, un soupçon présenté comme preuve peuvent causer des dommages réels : licenciement injuste, divorce, atteinte à la réputation, suicide. L'analyste qui produit du renseignement engage une responsabilité morale qu'aucun mandat n'efface.

**Deuxièmement, la légitimité collective de la discipline.** L'OSINT est une discipline jeune. Sa crédibilité dépend de la rigueur éthique de ses praticiens. Un dérapage individuel (doxxing public, harcèlement) entache toute la profession. L'éthique est aussi une question de soutenabilité collective.

**Troisièmement, l'analyste lui-même.** L'OSINT expose à des contenus difficiles (violence, abus, harcèlement, désinformation). Une posture éthique structurée protège la santé mentale du praticien et la qualité de son travail dans la durée.

#### 8.2 Les principes fondamentaux

**Proportionnalité.** L'intensité de l'investigation doit être proportionnée à l'enjeu. On n'utilise pas la reconnaissance faciale, le scrapping massif et l'analyse stylométrique pour vérifier une réservation de restaurant. La proportionnalité est aussi un principe juridique (RGPD) — c'est ici un principe éthique structurant.

**Minimisation.** Collecter le strict nécessaire à la finalité. Le RGPD l'impose ; l'éthique le renforce. Toute collecte excédentaire est une intrusion dans la vie privée sans justification.

**Nécessité.** L'investigation doit être nécessaire. Si l'objectif peut être atteint par une voie moins intrusive (entretien direct, consultation officielle), elle doit être privilégiée. L'OSINT n'est pas la première option par défaut.

**Finalité.** Toute collecte a une fin déterminée. La réutilisation des données pour une finalité autre est une trahison du commanditaire et de la personne ciblée.

**Loyauté.** Les méthodes doivent être loyales : pas d'usurpation agressive d'identité, pas de manipulation, pas de pièges techniques. La transparence par défaut, l'opacité par exception justifiée.

**Respect des personnes.** La personne ciblée a une dignité. Elle reste un sujet, pas un objet d'enquête. Le langage du rapport, la formulation des conclusions, le partage des données respectent cette dignité.

#### 8.3 Ce qui est éthiquement interdit

Certaines pratiques sont **hors-jeu**, même si elles peuvent être techniquement réalisables et juridiquement ambiguës.

**Doxxing public.** La publication d'informations personnelles d'une personne dans le but de lui nuire, l'exposer à du harcèlement, ou orchestrer une vengeance est interdite. Les forums de doxxing (Kiwi Farms et successeurs) ne sont pas des sources OSINT légitimes — ce sont des dispositifs de harcèlement.

**Harcèlement et stalking.** L'utilisation des compétences OSINT pour suivre, harceler, intimider une personne (ex-conjoint, ex-collègue, manifestant, journaliste) est interdite. Si vous êtes sollicité pour une investigation qui ressemble à du stalking déguisé, vous refusez.

**Surveillance abusive.** Le monitoring permanent d'une personne sans base légale (ex-conjoint, voisin, manifestant) est interdit. Le RGPD l'interdit, l'éthique le renforce.

**Manipulation active de sources.** Créer une fausse situation pour faire parler quelqu'un (faux profil de recruteur pour faire candidater, faux profil amoureux pour faire confier, faux investisseur pour faire diligenter) bascule en HUMINT manipulé et sort du cadre OSINT légitime.

**Violations volontaires des CGU.** Le scraping massif en violation explicite des CGU peut, dans certains pays, exposer pénalement. L'éthique recommande la modération et le respect des CGU autant que possible.

**Diffusion non maîtrisée.** Le partage de données collectées hors du périmètre du mandat (commentaire sur Twitter, brief informel à un confrère, fuite à un journaliste) est une faute professionnelle.

#### 8.4 Le doxxing : zone particulièrement sensible

Le **doxxing** mérite un traitement spécifique tant l'incidence est forte.

**Définition.** Publication d'informations personnelles d'une personne (adresse, téléphone, employeur, famille) dans le but de l'exposer, généralement à des fins d'intimidation, vengeance, ou mobilisation hostile.

**Le doxxing est interdit éthiquement et souvent pénalement.**

**Distinction importante.** Un rapport OSINT remis à un commanditaire légitime n'est pas un doxxing — c'est un livrable confidentiel. Le doxxing commence à la **diffusion non maîtrisée à un public hostile**.

**Réflexes.**
- Toujours sécuriser la diffusion du livrable.
- Ne jamais publier d'éléments identifiants sans nécessité.
- En cas de communication publique (presse, conférence), anonymiser systématiquement les exemples.
- Refuser les demandes ambiguës qui ressemblent à de la commande de doxxing.

#### 8.5 Cas particulier : les contenus sensibles

L'OSINT expose à des contenus difficiles : violence, abus, terrorisme, harcèlement. Trois cas méritent une attention particulière.

**CSAM (Child Sexual Abuse Material).** Le matériel pédopornographique est pénalement gravissime. Aucune justification (recherche, enquête, curiosité) n'autorise un analyste OSINT privé à le consulter ou le télécharger. **Si vous découvrez du CSAM** : ne pas télécharger, ne pas faire de capture, signaler immédiatement à **Pharos** (en France), **INHOPE** (international), **NCMEC** (US). Les services de police judiciaire ont les habilitations pour traiter, pas vous.

**Contenus terroristes / extrémistes.** Idem. Signalement Pharos. Pas de stockage local. Pas de partage.

**Contenus traumatiques (violence, accidents, morts).** Pour les besoins d'investigation, peut être nécessaire de visionner. Précautions : limiter le temps d'exposition, ne pas stocker plus que nécessaire, débriefer avec collègue, considérer suivi psychologique si exposition fréquente (cf. infra).

#### 8.6 Hygiène mentale de l'analyste

L'OSINT prolongé expose à un **stress traumatique secondaire**. Les investigateurs spécialisés CSAM, conflit armé, désinformation politique vivent un coût psychologique réel.

**Réflexes recommandés.**
- Limiter le temps d'exposition aux contenus difficiles (séances cadrées, pauses).
- Ne pas travailler seul sur des sujets lourds — équipe, débrief, soutien.
- Hygiène de séparation pro/perso : VM dédiée, horaires, espace physique séparé.
- Reconnaître les signaux d'alerte (insomnie, ruminations, irritabilité, cynisme).
- Accepter le suivi psychologique si nécessaire — c'est une marque de professionnalisme, pas de faiblesse.

Les grandes organisations OSINT (Bellingcat, ICIJ) ont structuré un soutien psychologique pour leurs équipes. Le free-lance doit s'auto-organiser une équivalence.

#### 8.7 Conflits d'intérêts

L'investigateur OSINT peut être confronté à des conflits d'intérêts.

**Cas typiques.**
- Investigation sur un acteur économique concurrent d'un autre client.
- Investigation sur un proche, un ami, un collègue.
- Investigation commanditée par un client dont la finalité réelle vous semble suspecte.

**Réflexes.**
- Déclarer le conflit dès qu'il apparaît.
- Refuser le mandat ou solliciter accord explicite du commanditaire.
- Tenir un registre interne des conflits potentiels.

#### 8.8 Secret professionnel et confidentialité

Les données collectées et les livrables produits sont confidentiels. L'analyste est tenu au secret.

**Pratiques.**
- Stockage chiffré, accès restreint.
- Pas de partage non autorisé, même informel.
- Destruction sécurisée à l'expiration de la durée de conservation.
- Non-divulgation des clients (sauf cas où l'investigation est rendue publique par eux).
- Vigilance sur les conversations en lieu public, dans les transports.

#### 8.9 Quand refuser une mission

Quelques signaux qui doivent conduire à refuser une mission.

- Mandat flou ou refusé par écrit.
- Finalité réelle suspecte (« je veux des éléments sur mon ex », « je veux faire pression »).
- Demande de doxxing déguisée.
- Demande d'accès à des données non publiques (paie pour un leak, accès à un compte).
- Cible vulnérable (mineur, lanceur d'alerte, opposant politique sous régime hostile).
- Délais ou budgets manifestement insuffisants pour une investigation sérieuse.
- Manque de transparence du commanditaire sur sa propre identité.

Refuser une mission est parfois la décision la plus professionnelle. La capacité à dire non protège le métier.

#### 8.10 Vers une déontologie professionnelle structurée

L'OSINT n'a pas encore d'ordre professionnel équivalent au Barreau ou à l'Ordre des médecins. Plusieurs associations posent des chartes (OSMOSIS, AFCOSINT, Bellingcat Code of Conduct). Le mouvement vers une professionnalisation déontologique structurée est en cours en 2026. À titre individuel, adopter une charte éthique écrite, la publier le cas échéant, s'y conformer est un signal de sérieux.

-----

### Chapitre 9 — OPSEC de l'investigateur OSINT

#### 9.1 Pourquoi l'OPSEC

L'**OPSEC** (Operations Security, sécurité opérationnelle) est la discipline qui protège l'investigation et l'investigateur. Trois enjeux concrets.

**Protéger la mission.** Une cible qui détecte qu'elle est observée peut effacer ses traces, fuir, mettre en place des contre-mesures, ou alerter ses complices. L'OPSEC empêche la cible de remarquer l'investigation.

**Protéger l'investigateur.** Certaines cibles ont les moyens de retourner l'investigation contre l'enquêteur (criminels organisés, services étrangers, acteurs étatiques hostiles, harceleurs sophistiqués). L'OPSEC protège l'identité, le foyer, la famille, l'employeur de l'investigateur.

**Protéger les données.** Les données collectées sont sensibles (RGPD, contractuel, déontologique). Une fuite expose le commanditaire et la cible. L'OPSEC sécurise le stockage et la transmission.

#### 9.2 Threat model — le concept central

L'OPSEC n'est pas une checklist universelle, c'est une **adaptation à la menace**. Le **threat model** est l'évaluation structurée de qui pourrait s'intéresser à votre investigation et avec quelles capacités.

**Questions du threat model.**
- Qui est la cible ? Quelles sont ses capacités techniques et financières ?
- A-t-elle des complices ? Quelles sont leurs capacités ?
- Y a-t-il des tiers (services d'État hostiles, groupes criminels) susceptibles d'intervenir ?
- Quelle est la valeur potentielle de la cible (qu'a-t-elle à perdre) ?
- Quels sont les vecteurs d'attaque réalistes contre l'investigateur ?
- Quelle est la durée de l'exposition ?

Un threat model rigoureux fait la différence entre une OPSEC adaptée et une OPSEC théâtrale (trop lourde pour rien) ou une OPSEC insuffisante (légère face à une menace réelle).

#### 9.3 Catégories de menace

Quatre catégories types, à adapter à chaque cas.

**Cibles ordinaires.** Personne physique sans compétences techniques particulières, sans moyens financiers extraordinaires, sans réseau de complices. OPSEC légère suffit : navigateur dédié, VPN, comptes d'investigation. Délaunay du fil rouge MIRAGE rentre en partie dans cette catégorie initiale — mais sa compétence technique de DAF le rend plus sensible que la moyenne.

**Cibles sensibles.** Personnes avec ressources techniques (RSSI, ingénieurs sécurité), financières (chefs d'entreprise, fortunés), ou en position de pouvoir (élus, magistrats). OPSEC renforcée : VM dédiée, séparation stricte, OPSEC plateforme par plateforme.

**Cibles criminelles.** Organisations criminelles structurées, particulièrement crime organisé (mafia, cartels), groupes cybercriminels professionnels. Capacité à retourner l'investigation, à corrompre, à intimider. OPSEC forte : VM dédiée par enquête, Whonix, séparation infrastructure physique, anonymisation maximale.

**Cibles étatiques.** Services de renseignement étrangers, gouvernements hostiles, agences cyber étatiques. Capacités SIGINT, accès aux opérateurs télécom, capacité à monitorer Internet à grande échelle. OPSEC maximale : Tails sur clé USB, jamais de connexion depuis l'infrastructure habituelle, infrastructure dédiée et jetable. **Si vous êtes confronté à cette menace sans formation spécifique, vous transférez le dossier à un partenaire qualifié.**

#### 9.4 Infrastructure d'investigation : VM, VPN, Tor

**Machine virtuelle (VM) dédiée par enquête** est le standard.

Avantages : isolation complète, possibilité de snapshot avant action sensible, destruction propre après mission, séparation entre identité d'investigateur et identité personnelle.

Outils : **VirtualBox** (gratuit, robuste), **VMware Workstation** (payant, plus performant), **QEMU/KVM** (Linux natif). Configuration recommandée : 4-8 Go RAM, 50-100 Go disque chiffré, snapshots à chaque étape clé.

**Systèmes d'exploitation.**
- **Ubuntu 24.04 LTS** : VM principale, bon compromis fonctionnalité/sécurité.
- **Tails** : Linux live amnésique sur clé USB, à utiliser pour les missions ponctuelles sensibles. Routage Tor par défaut.
- **Whonix** : architecture deux VM (Gateway Tor + Workstation), isolation forte. Pour les enquêtes nécessitant Tor de manière soutenue.
- **Qubes OS** : isolation par compartiments (qubes). Très robuste mais courbe d'apprentissage. Pour analystes avancés.

**VPN.**
- VPN **non corporate, sans logs vérifiés** par audit tiers (Mullvad, IVPN, Proton VPN avec parcimonie).
- Paiement anonyme si possible (crypto, espèces).
- Jamais le VPN personnel (qui peut remonter à l'identité civile).
- Vigilance sur les VPN gratuits — souvent compromis ou financés par exploitation des données utilisateurs.

**Tor.**
- Pour les cas de menace élevée.
- Tor Browser, **jamais d'identification personnelle** dans une session Tor.
- Performances dégradées (acceptable pour investigation, pas pour usage quotidien).
- Conscience des limites : Tor protège l'anonymat de connexion, pas le contenu si on s'identifie une fois connecté.

#### 9.5 Navigateurs et empreinte

**Profil navigateur dédié.** Firefox ou Chromium avec profil isolé, jamais le profil personnel.

**Extensions sécurité.**
- **uBlock Origin** (blocage tracking).
- **NoScript** (contrôle JavaScript, à manier avec discernement).
- **Cookie AutoDelete** (purge des cookies à chaque session).
- **Privacy Badger** (anti-tracking heuristique).
- **CanvasBlocker** (lutte fingerprinting canvas).

**Empreinte navigateur (browser fingerprinting).** Au-delà des cookies, les sites identifient les visiteurs par la combinaison de paramètres (résolution, fonts, plugins, GPU, configuration audio). Tests : **AmIUnique**, **Cover Your Tracks** (EFF). En 2026, la déanonymisation par fingerprinting est mature — un profil unique vous identifie même sans cookie.

**Réflexes.**
- Profil minimaliste (peu d'extensions, configuration standard).
- Désactivation du WebRTC (peut révéler l'IP réelle même sous VPN).
- DNS chiffré (DoH ou DoT).
- Désactivation du géolocalisation, microphone, caméra par défaut.

#### 9.6 DNS chiffré et fuites

Les requêtes DNS classiques sont visibles par votre FAI ou par un attaquant sur le réseau. Le DNS chiffré (**DoH** — DNS over HTTPS, ou **DoT** — DNS over TLS) le prévient.

**Configurations recommandées.**
- Cloudflare 1.1.1.1 (rapide, audit-friendly).
- Quad9 9.9.9.9 (filtrage malware par défaut).
- NextDNS (configurable, payant raisonnable).
- DNS auto-hébergé pour analystes avancés.

**Test de fuite.** `dnsleaktest.com`, `ipleak.net`. Vérifier régulièrement.

#### 9.7 Stockage chiffré

Les données d'investigation doivent être chiffrées **au repos** et **en transit**.

**Au repos.**
- Disque chiffré complet : **LUKS** (Linux), **BitLocker** (Windows Pro), **FileVault** (macOS).
- Conteneurs chiffrés pour archives sensibles : **VeraCrypt** (multi-OS).
- Cloud chiffré côté client : **Cryptomator**, **Boxcryptor** (avant import dans cloud).
- Pas de stockage en clair, jamais.

**En transit.**
- Email chiffré : **PGP** via Thunderbird+Enigmail ou via **ProtonMail**.
- Messagerie chiffrée pour collaboration : **Signal** (à privilégier), **Wire**, **Element/Matrix**.
- Pas de transmission par WhatsApp pour sujets sensibles (chiffrement E2E mais propriété Meta).

**Gestion des clés.**
- Mot de passe maître robuste (gestionnaire type **Bitwarden**, **KeePassXC**).
- 2FA matériel pour les accès sensibles (clé YubiKey).
- Sauvegarde sécurisée des clés (coffre-fort, partage Shamir si critique).

#### 9.8 Cloisonnement strict

Le **cloisonnement** entre identité personnelle, identité professionnelle générale, et identité d'investigation est central.

**Règles.**
- VM d'investigation **jamais** synchronisée avec compte cloud personnel.
- Email d'investigation **jamais** lié au téléphone personnel.
- Téléphone d'investigation séparé physiquement (SIM dédiée, IMEI distinct).
- Pas de copie-coller entre VM d'investigation et machine hôte (clipboard est un vecteur de fuite).
- Pas de USB partagée.
- Compte bancaire dédié pour les abonnements professionnels OSINT (DeHashed, PimEyes, etc.).

#### 9.9 Téléphones d'investigation

Pour les investigations qui nécessitent une présence mobile (vérification compte SMS, app store country-specific, géolocalisation cible) :

- Téléphone **physiquement séparé** du téléphone personnel (idéalement modèle différent).
- **SIM prépayée** acquise en espèces (selon législation locale).
- **IMEI distinct** (ne pas réutiliser un ancien téléphone personnel).
- Profil système d'investigation, pas de comptes personnels.
- Géolocalisation désactivée par défaut, activée à la demande.
- Mode avion entre missions.
- Reset complet entre enquêtes critiques.

Légalité de la SIM prépayée : variable selon pays. En France, la SIM prépayée est désormais soumise à identification (loi sur les communications). Vérifier la conformité locale.

#### 9.10 Gestion des mots de passe et 2FA

- **Gestionnaire de mots de passe** dédié (KeePassXC local, ou Bitwarden self-hosted pour les sensibles).
- Mots de passe **uniques par compte**, générés (16+ caractères aléatoires).
- **2FA matériel** pour les comptes critiques (YubiKey, Nitrokey).
- **2FA SMS à éviter** (SIM swapping possible).
- **Codes de récupération** stockés chiffrés.

#### 9.11 Comptes d'investigation

Les comptes utilisés pour observer les plateformes (LinkedIn, X, Telegram) sont des **comptes d'investigation**, pas des comptes personnels. Pour leur création, voir Ch.11 (sock puppets).

**Règles minimales.**
- Email d'investigation (ProtonMail, Tutanota, ou domaine dédié).
- Téléphone d'investigation pour confirmation SMS si demandée.
- Pas d'informations personnelles dans la bio.
- Activité de maturation (quelques posts neutres, abonnements neutres) avant utilisation pour investigation.
- Cloisonnement strict entre comptes par investigation si menace élevée.

#### 9.12 Erreurs classiques

Quelques erreurs récurrentes à éviter.

- LinkedIn d'investigation connecté au vrai téléphone (qui voit votre profil personnel via les contacts).
- VPN d'investigation et VPN personnel sur la même IP (corrélation possible).
- Métadonnées EXIF non purgées dans les captures envoyées au client.
- Copier-coller entre VM d'investigation et machine hôte (clipboard sync).
- Capture d'écran de l'investigation incluant la barre de tâches avec compte personnel.
- Réutilisation d'un username déjà utilisé personnellement.
- Posting via compte d'investigation depuis le wifi domestique sans VPN.
- Activation de la géolocalisation par défaut sur le téléphone d'investigation.

#### 9.13 OPSEC parfaite n'existe pas

Aucune OPSEC n'est parfaite. L'objectif n'est pas l'invisibilité totale (théorique) mais la **réduction du risque à un niveau acceptable** pour la mission.

L'analyste qui surévalue sa sécurité (« je suis intracable ») est presque aussi dangereux que celui qui la néglige. Le premier prend des risques en croyant être invisible. La modestie OPSEC est une vertu.

#### 9.14 OPSEC en équipe

Quand l'investigation se fait en équipe, l'OPSEC est le maillon faible.

**Pratiques.**
- Outils collaboratifs chiffrés (Signal, Wire, Element).
- Pas de partage de captures via canaux non chiffrés.
- Définir clairement qui voit quoi.
- Briefing OPSEC en début de mission.
- Debriefing en fin de mission (qu'est-ce qui a fuité, quoi corriger).

#### 9.15 Synthèse — OPSEC par niveau

| Niveau menace | Infrastructure | Réseau | Téléphone | Stockage |
|---|---|---|---|---|
| **Ordinaire** | Profil navigateur dédié | VPN | Optionnel | Disque chiffré |
| **Sensible** | VM dédiée | VPN + DNS chiffré | Recommandé | Conteneur VeraCrypt par enquête |
| **Criminelle** | VM Whonix | VPN + Tor | Téléphone dédié SIM prépayée | Conteneur séparé + backup chiffré |
| **Étatique** | Tails clé USB | Tor seul, jamais VPN commercial | Téléphone jetable | Pas de stockage local longue durée |

Le chapitre suivant traite spécifiquement de l'OPSEC face aux plateformes et à l'IA — un sujet 2026 majeur.

-----

### Chapitre 10 — OPSEC face aux plateformes et à l'IA

#### 10.1 Pourquoi un chapitre spécifique en 2026

L'OPSEC technique du chapitre précédent (VM, VPN, Tor, chiffrement) reste nécessaire mais n'est plus suffisante. En 2026, deux ruptures redéfinissent ce qu'observer en ligne signifie : les **plateformes infusées d'IA** disposent de capacités d'inférence comportementale qui dépassent largement le fingerprinting technique, et les **outils OSINT que nous utilisons** (LLMs commerciaux, agents, SaaS) constituent eux-mêmes un vecteur de fuite d'intention. L'analyste qui maîtrise l'OPSEC classique mais ignore ces deux dimensions opère avec un faux sentiment de sécurité.

#### 10.2 Empreinte comportementale au-delà du fingerprinting

Le fingerprinting technique (canvas, fonts, GPU, audio) identifie un navigateur. L'**empreinte comportementale** identifie une personne. Elle s'appuie sur des signaux que la plupart des outils OPSEC ne couvrent pas.

**Signaux comportementaux.**
- **Cadence de navigation** : vitesse de lecture, temps moyen par page, schémas de défilement.
- **Fuseau horaire d'activité** : heures de connexion, jours de la semaine.
- **Lexique de recherche** : choix de mots-clés, langue maternelle, niveau de spécialisation.
- **Patterns de pivots** : un investigateur navigue de façon caractéristique (recherche entité → registre → réseau social → archive).
- **Frappe clavier** : timing entre frappes (keystroke dynamics), reconstruction possible.
- **Mouvement souris** : trajectoires, micro-pauses, hover patterns.
- **Pile applicative** : combinaison de plugins, paramètres, langue système.

Une plateforme grand public ne réunit pas tous ces signaux par défaut. Une plateforme commerciale OSINT, un site spécialisé, un outil SaaS peuvent en collecter beaucoup. Et un acteur étatique disposant d'une intercept réseau peut reconstituer une grande partie. La menace n'est pas hypothétique : les services de renseignement étrangers traquent activement les analystes OSINT alliés selon plusieurs avertissements publics récents (avertissement du chef de l'ASIO australienne Mike Burgess en 2024-2025 sur la collecte étrangère ciblant le personnel de défense via les sources ouvertes et les services d'IA).

**Contre-mesures.**
- Varier sa cadence (ne pas être identifiable à un schéma temporel).
- Ne pas utiliser les mêmes patterns de navigation entre identités.
- Si la menace est élevée, automatiser via outils (Playwright, requêtes API) qui produisent une signature neutre — au prix d'une perte de finesse.

#### 10.3 Fuite d'intention via les outils d'investigation

Les outils OSINT modernes communiquent avec leurs serveurs. Chaque requête révèle ce que vous cherchez.

**Vecteurs typiques.**
- **APIs OSINT commerciales** (Shodan, DeHashed, IntelX, Hunter) : le fournisseur sait ce que vous cherchez, par horodatage et IP. Logs conservés.
- **LLMs commerciaux** (ChatGPT, Claude, Gemini) : le contenu de vos prompts est conservé selon les conditions du fournisseur. Vos prompts d'investigation révèlent vos cibles, vos hypothèses, votre méthode.
- **Outils SaaS OSINT** (Maltego cloud, Hunchly cloud, plateformes commerciales) : centralisation des données d'enquête chez le fournisseur.
- **Reverse image cloud** : votre image cible est envoyée au serveur de recherche, indexée potentiellement.
- **Outils de géolocalisation IA** (GeoSpy, GeoSeer) : votre image cible est envoyée et conservée.

**Le risque réel.** Une compromission, une réquisition judiciaire, une faille, ou simplement un employé indiscret du fournisseur peut exposer l'ensemble de vos investigations. Pour des cibles étatiques avec capacités SIGINT, l'observation directe du trafic est possible.

#### 10.4 Prompts vers LLMs : un sujet sous-estimé

Les LLMs commerciaux sont devenus des outils de recherche au quotidien. Leur utilisation dans un cadre OSINT mérite une attention spécifique.

**Risques.**
- **Conservation des prompts** : OpenAI, Anthropic, Google conservent les prompts (durées variables, politiques évoluant). En cas de réquisition judiciaire dans le pays du fournisseur, ces données peuvent être accessibles.
- **Apprentissage potentiel** : selon les politiques (variables et évolutives), certaines plateformes utilisent les prompts pour entraîner les modèles, ce qui peut faire ressurgir des éléments d'enquête dans des réponses ultérieures.
- **Profilage du compte** : le fournisseur peut profiler votre usage et inférer votre activité professionnelle.
- **Erreurs de saisie** : copier-coller d'un dossier contenant des données sensibles, fuite involontaire.

**Bonnes pratiques.**
- **Anonymiser les prompts** : ne pas inclure de noms réels, d'identifiants, de données personnelles si évitable. Utiliser des placeholders (« la cible », « l'individu A »).
- **Compte d'investigation dédié** : pas le compte personnel professionnel, pas le compte client.
- **Privilégier les modèles avec opt-out** : OpenAI Enterprise, Anthropic Claude avec opt-out, Mistral hébergé en UE.
- **LLMs locaux** pour les sujets sensibles (Ch.65) : Ollama, LM Studio, vLLM auto-hébergé.
- **Cloisonner les contextes** : ne pas mélanger plusieurs investigations dans la même session.

#### 10.5 Graphes de comportement et inférence des plateformes

Les grandes plateformes (Meta, Google, LinkedIn) construisent en interne des **graphes de comportement** qui peuvent corréler des comptes apparemment distincts.

**Signaux corrélatifs.**
- IP partagée (même VPN, même bureau).
- Empreinte navigateur similaire.
- Plages horaires identiques.
- Contacts communs (LinkedIn « personnes que vous pourriez connaître » est une fuite OPSEC majeure : il révèle les contacts implicites entre vos comptes).
- Géolocalisation téléphonique (si app activée).
- Carte de crédit, méthode de paiement.
- Adresse mail de récupération.

**Implication.** Vos comptes d'investigation peuvent être liés entre eux par la plateforme, et liés à votre identité personnelle, même sans erreur explicite de votre part. La défense est de **séparer physiquement** : IP différente, navigateur différent, téléphone différent, fenêtre temporelle différente.

#### 10.6 Risque spécifique des agents autonomes

L'utilisation d'agents autonomes (Ch.67) en OSINT 2026 introduit un risque OPSEC nouveau.

**L'agent est une projection de l'investigateur.** Son schéma de comportement, ses pivots, ses choix de sources peuvent former une signature identifiable par les plateformes adverses. Un agent qui requête Shodan, puis Censys, puis crt.sh dans la même séquence pour un même domaine porte une signature distinctive.

**Risques spécifiques.**
- Agents qui interagissent avec des plateformes adverses (réponses qui peuvent influencer l'agent — *prompt injection* en environnement adversariale).
- Agents qui consultent un dump et le téléchargent inadvertamment (exposition pénale).
- Agents qui requêtent des API au-delà des CGU.
- Agents qui exposent leurs prompts en logs.

**Mesures.**
- Audit des agents : qui appelle quoi, quand, avec quels paramètres.
- Validation humaine systématique avant action sensible.
- Logs locaux des actions d'agents (pas dans le cloud).
- Mode dégradé en environnement adverse (humain au volant).

#### 10.7 Détection de l'investigation par la cible

Une cible compétente peut détecter qu'elle est investiguée.

**Signaux côté cible.**
- **Recherches Google** : un dirigeant qui surveille « son nom » avec Google Alerts voit les nouvelles indexations.
- **Visites LinkedIn** : LinkedIn notifie qui consulte un profil (sauf mode privé, qui implique une perte de fonctionnalité d'investigation).
- **Notifications Twitter/X** : les retweets, likes, mentions remontent.
- **Audit des connexions** : les comptes consultés via une connexion suspecte sont signalés.
- **Honeypots** : la cible elle-même peut déposer des fichiers piégés (canary tokens) ou des liens piégés.

**Contre-mesures.**
- Mode privé LinkedIn (ou compte premium pour le voir).
- Pas d'interaction (pas de like, pas de retweet, pas de réponse).
- Connexion via VPN constante.
- Pas de téléchargement de fichiers d'origine suspecte sans isolation.
- Vigilance sur les liens cliqués dans les emails ou messages.

#### 10.8 Counter-OSINT : la cible se défend

Les cibles aguerries pratiquent du **counter-OSINT** pour détecter et tromper les investigations.

**Méthodes typiques.**
- **Honeypot social** : profil dormant qui attire les curieux et les identifie.
- **Désinformation contrôlée** : informations fausses semées pour identifier les fuites.
- **Monitoring des consultations** : alertes sur les accès à leur profil, leurs documents partagés.
- **Identités secondaires** : compte public propre, activité réelle ailleurs.
- **Faux indices** : fausses pistes plantées pour égarer les enquêteurs.

**Implication.** L'analyste OSINT doit considérer que ses propres observations peuvent être manipulées. C'est l'objet du raisonnement adversaire (Ch.81).

#### 10.9 Knowledge graphs locaux comme protection

Conserver l'enquête **localement** plutôt que dans un SaaS cloud limite la surface d'exposition. Le knowledge graph local (Ch.66) est l'illustration : graphe d'entités et de faits stocké chez l'investigateur, sans synchronisation cloud.

**Bénéfices OPSEC.**
- Pas de fuite d'intent vers un fournisseur tiers.
- Pas d'historique d'enquête centralisé hors de votre contrôle.
- Souveraineté complète sur les données.
- Possibilité de chiffrer entièrement.

**Coûts.**
- Pas de partage facilité avec une équipe distribuée (à compenser par chiffrement E2E).
- Pas de hosted intelligence (LLMs locaux moins puissants que les cloud).
- Maintenance technique.

Pour les sujets de haute sensibilité, le local est la règle.

#### 10.10 Synthèse — boussole OPSEC 2026

| Vecteur de fuite | Mesure |
|---|---|
| Fingerprinting navigateur | Profil minimaliste, extensions standard, test fingerprint |
| Logs APIs OSINT commerciales | Compte d'investigation, anonymisation requêtes |
| Prompts LLMs cloud | LLMs locaux pour sensibles, anonymisation, opt-out |
| Graphes corrélatifs plateformes | Séparation IP, téléphone, mail, contacts |
| Agents autonomes | Audit, validation humaine, logs locaux |
| Détection par la cible | Mode privé, pas d'interaction, VPN constant |
| Counter-OSINT cible | Raisonnement adversaire, croisement sources |
| Centralisation cloud | Knowledge graph local pour sensibles |

> **Principe directeur 2026.** Plus votre boîte à outils OSINT est puissante, plus elle est observable. La maîtrise consiste à choisir consciemment quel outil pour quel niveau de sensibilité — pas à utiliser l'outil le plus puissant par défaut.

-----

### Chapitre 11 — Sock puppets, avatars et identités d'enquête

#### 11.1 Définition et cadre

Un **sock puppet** (ou avatar, ou identité d'enquête) est un compte créé et opéré par l'analyste qui n'est pas son identité personnelle. Son usage est central dans l'OSINT moderne : sans avatar, l'accès à de nombreuses plateformes (LinkedIn, Telegram, X, Discord, forums) est impossible ou révèle immédiatement l'identité réelle de l'investigateur.

L'avatar est un outil **professionnel**, pas une fausse identité criminelle. Sa création et son usage respectent un cadre éthique et juridique strict. Mal manié, il bascule en infraction d'usurpation d'identité (art. 433-19 CP en France) ou en pratique HUMINT non-déclarée potentiellement frauduleuse.

#### 11.2 Typologies d'avatars

**Avatar passif d'observation.** Compte qui n'interagit pas, n'écrit pas, ne contacte personne. Il sert uniquement à voir des contenus accessibles aux comptes connectés mais pas aux visiteurs non identifiés (groupes Facebook privés au sens « visible aux membres », posts LinkedIn nécessitant connexion). C'est l'usage le plus défensif et le moins juridiquement exposé.

**Avatar actif d'observation.** Compte qui interagit légèrement (likes, joindre des groupes ouverts, suivre des comptes publics) pour s'intégrer dans un écosystème observable. Plus exposé juridiquement, à manier avec rigueur.

**Avatar d'élicitation.** Compte qui contacte activement des sources pour les faire parler. **Sortie du périmètre OSINT pur**, bascule en HUMINT. Légitime dans certains cadres (LEA, journalisme avec déontologie stricte) mais exigeant : suppose mandat, suppose limites éthiques, suppose qu'on accepte la responsabilité de manipuler une personne.

**Avatar honeypot.** Compte qui attire des cibles (faux profil amoureux, faux profil candidat, faux profil journaliste). Très exposé juridiquement et éthiquement. À réserver à des cadres LEA strictement encadrés ou à des journalistes avec déontologie publiée.

Pour le présent cours, l'usage par défaut est l'avatar **passif** ou **actif léger**. Les autres usages sortent du cadre OSINT standard.

#### 11.3 Légitimité juridique de l'avatar

L'usage d'un avatar reste légitime tant que :
- Il **n'usurpe pas une identité réelle existante** (pas de copie d'une personne réelle).
- Il **n'usurpe pas une qualité protégée** (pas de prétention à être avocat, médecin, policier, journaliste accrédité si on ne l'est pas).
- Il **ne sert pas à commettre une infraction** (escroquerie, harcèlement, atteinte à la vie privée caractérisée).
- Il **respecte les CGU** de la plateforme, ou les violations restent mineures et déontologiquement justifiées.

Sortir de ces limites, c'est entrer en zone pénale ou déontologique fragile. La jurisprudence française reste en évolution sur ces sujets.

#### 11.4 Création d'un avatar : éléments constitutifs

Construire un avatar crédible est un travail. Six éléments doivent être cohérents.

**Identité fictive.** Un nom plausible mais non-existant (vérifier qu'il ne correspond pas à une personne réelle identifiable). Générateurs comme **Fake Name Generator** peuvent aider mais il faut vérifier l'unicité. Idéalement, créer un nom plausible pour la juridiction de l'enquête.

**Email dédié.** Adresse créée sur un service privacy-friendly (ProtonMail, Tutanota) ou sur un domaine que vous contrôlez. **Jamais lié au téléphone personnel**.

**Téléphone d'investigation.** Pour les plateformes qui exigent SMS de confirmation. Voir Ch.9 sur la séparation physique.

**Photo de profil.** Trois options :
- **Photo générée par IA** (ThisPersonDoesNotExist et successeurs). Avantage : aucune personne réelle. Inconvénient : les outils de détection IA s'améliorent et certaines plateformes flaguent les photos GAN-classiques.
- **Photo achetée banque image** (Adobe Stock, modèles consentants). Légalité OK si licence respectée, mais risque qu'elle apparaisse ailleurs (recherche inversée par la cible).
- **Photo générée par IA récente** (Midjourney, Flux) avec personnage stylisé. Compromis raisonnable, attention à la détection.

**Bio et histoire.** Cohérence avec l'identité (ville, parcours, profession, intérêts). Pas de vérité personnelle dedans (pas de vraie école, pas de vrai employeur). Suffisamment générique pour ne pas alerter, suffisamment spécifique pour être crédible.

**Réseau social initial.** Quelques posts neutres (paysages, citations, articles partagés), quelques abonnements à des comptes publics neutres. Avatar nu = avatar suspect.

#### 11.5 Maturation

Un avatar **fraîchement créé** est suspect. Les plateformes (LinkedIn particulièrement) flaguent les comptes neufs. La maturation consiste à laisser l'avatar **prendre de l'âge** avant utilisation opérationnelle.

**Cadence type.**
- **Mois 1** : créer, compléter profil, 5-10 abonnements neutres, 2-3 posts généraux.
- **Mois 2-3** : poursuivre l'activité légère, abonnements progressifs, quelques interactions (likes sur contenus généraux), pas d'interaction avec cibles potentielles.
- **Mois 4-6** : avatar utilisable pour observation passive. Activité maintenue régulièrement.
- **Mois 6+** : avatar mature, utilisable plus largement (toujours dans le cadre passif/actif léger).

**Implication.** Si vous avez besoin d'avatars opérationnels, vous devez les créer **bien avant** d'en avoir besoin. Un cabinet professionnel maintient un parc d'avatars matures à différents stades.

#### 11.6 Cohérence sur la durée

Un avatar bien conçu est trahi par les erreurs de cohérence sur la durée.

**Pièges classiques.**
- **Fuseau horaire incohérent** : avatar « basé à Lyon » qui poste à 3h du matin systématiquement.
- **Lexique trahissant** : l'avatar prétendument anglophone qui utilise des tournures françaises (et inversement).
- **Photo profil unique** : avatar qui n'a jamais d'autre photo, jamais de selfie circonstancié.
- **Activité saisonnière incohérente** : vacances supposées au Pérou en décembre, post de neige à Toulouse le même jour.
- **Inactivité prolongée** : six mois sans activité, puis usage soudain pour l'enquête (signal fort).
- **Réseau corrélé** : tous les avatars d'investigation suivent les mêmes comptes (clustering détectable).

#### 11.7 Journal interne des avatars

Pour les cabinets et investigateurs maintenant plusieurs avatars, un **journal interne** est indispensable.

**Champs minimaux.**
- Nom de l'avatar.
- Date de création.
- Plateformes opérées.
- Email associé.
- Téléphone associé.
- IP/VPN utilisés.
- Historique d'activité (cadence, posts, abonnements).
- Enquêtes pour lesquelles utilisé.
- État actuel (actif, dormant, brûlé).
- Date de prochaine action de maintien.

Ce journal est **lui-même hautement sensible** : il révèle l'écosystème complet d'investigation. Stockage chiffré, accès strictement restreint.

#### 11.8 Risque d'usurpation et erreurs classiques

**Erreurs récurrentes à éviter.**
- Avatar avec photo de personne réelle (recherche inversée → usurpation).
- Avatar qui se prétend journaliste, avocat, ou policier sans l'être (usurpation de qualité).
- Avatar utilisé pour escroquerie, harcèlement, doxxing (sortie pénale).
- Avatar dont l'email récupère vers l'adresse personnelle.
- Avatar dont le téléphone est le téléphone personnel.
- Avatar dont le numéro de carte bancaire est lié à l'investigateur.
- Avatar accédé depuis le même IP que les autres avatars (clustering plateforme).
- Avatar qui contacte des personnes vulnérables (mineurs, victimes).
- Plusieurs avatars qui se suivent entre eux pour créer une illusion de réseau (détectable).

#### 11.9 Durée de vie et renouvellement

Un avatar n'est pas éternel.

**Causes de fin de vie.**
- **Brûlage** : cible le détecte ou suspecte.
- **Suspension plateforme** : LinkedIn, X suspendent régulièrement les comptes flagués.
- **Compromission OPSEC** : l'email associé est leaké, le téléphone est doxxé.
- **Fin d'enquête** : avatar dédié à une affaire, fermé à la conclusion.
- **Obsolescence** : photo, bio devenue trop vintage.

**Cycle.** Maintenir un parc d'avatars en pipeline : 30 % en maturation, 50 % opérationnels, 20 % en fin de vie / archivage.

#### 11.10 Avatars en équipe et partage

Si une équipe partage un avatar, l'OPSEC se complique.

**Pratiques.**
- Accès via VPN dédié partagé.
- Mot de passe centralisé chiffré.
- Journal de qui a utilisé quand.
- Pas d'usage simultané (sessions parallèles peuvent flaguer le compte).
- Cohérence comportementale : un membre type a-t-il une cadence ? Tous les utilisateurs doivent s'y conformer.

#### 11.11 Avatar et IA : tendance 2026

Les outils de génération IA permettent désormais de créer des avatars avec :
- Photos cohérentes série complète (visage identique sous différents angles, à différents âges, dans différents contextes).
- Posts générés par LLM (à condition de garder une cohérence de style).
- Vidéos courtes deepfake (très risqué juridiquement et déontologiquement, à éviter pour OSINT pur).

**Mais simultanément**, les plateformes développent des détecteurs IA. La course est en cours. L'avatar « 100 % IA » est de plus en plus détectable. Le compromis raisonnable en 2026 : photo générée par IA + bio rédigée par humain (ou LLM avec révision humaine forte) + activité humaine réelle.

#### 11.12 Synthèse

| Élément | Bonne pratique |
|---|---|
| Identité | Plausible, non-existante vérifiée, jamais usurpation |
| Email | ProtonMail/Tutanota dédié, jamais lié au personnel |
| Téléphone | Téléphone d'investigation séparé |
| Photo | Génération IA récente OU stock licencié, jamais personne réelle |
| Bio | Cohérente, générique, pas de vérité personnelle |
| Maturation | 3-6 mois avant usage opérationnel |
| Activité | Régulière, neutre, cohérente fuseau horaire/lexique |
| Cloisonnement | IP séparée des autres avatars, VPN dédié si possible |
| Journal | Interne, chiffré, accès restreint |
| Cycle | Pipeline maturation → opérationnel → fin de vie |

L'avatar mature est un actif. Le maintenir demande du temps et de la rigueur. Le compromettre, c'est griller un investissement et potentiellement une enquête.

-----
