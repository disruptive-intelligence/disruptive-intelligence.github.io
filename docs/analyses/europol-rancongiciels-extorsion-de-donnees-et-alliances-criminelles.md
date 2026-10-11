---
title: "Europol : rançongiciels, extorsion de données et alliances criminelles"
date: 2026-10-11
kind: analysis
theme: "cyber"
slug: "europol-rancongiciels-extorsion-de-donnees-et-alliances-criminelles"
organization: "Europol"
source_file: "inbox/Transcript-how-ransomware-is-evolving.pdf"
source_url: "https://www.europol.europa.eu/media-press/europol-podcast/episode-25-how-ransomware-is-evolving"
rubriques:
  - "cyber-menaces-cti"
  - "justice-enquete"
tags:
  - "rançongiciels"
  - "extorsion de données"
  - "cybercriminalité organisée"
  - "DDoS"
---

# Europol : rançongiciels, extorsion de données et alliances criminelles

## Métadonnées

- **Titre original :** *How ransomware is evolving – Episode 3, Season 4*.
- **Auteur et intervenants :** transcription officielle du podcast Europol ; entretien animé par Gabby avec Michaël De Laet, chef d'équipe au Centre européen de lutte contre la cybercriminalité (EC3). La transcription ne donne pas le nom complet de l'animatrice (p. 1-2).
- **Date de publication :** non indiquée dans le PDF. La discussion évoque le rapport IOCTA 2026 et des observations de 2025-2026 (p. 1-3).
- **Support et méthode :** transcription éditée d'une session d'experts en direct, sur douze pages ; elle avertit que la transcription automatisée peut contenir des erreurs (p. 1, 12).
- **Original :** `inbox/Transcript-how-ransomware-is-evolving.pdf`. La page officielle de l'épisode, vérifiée séparément dans l'état de l'art, est indiquée dans le lien « Original » du portail.
- **Thématique principale :** transformation de l'économie du rançongiciel, méthodes d'extorsion et réponse policière.

## Repères pour comprendre le document

L'entretien mêle une présentation des groupes de rançongiciels à des questions sur les attaques par déni de service, l'intelligence artificielle et le travail d'Europol. Pour le lire, il faut distinguer la **technique d'attaque**, le **modèle commercial** qui la rend accessible et la **revendication publique** d'un groupe. Ces trois niveaux ne mesurent pas la même chose : une marque peut changer sans que ses opérateurs changent, et une revendication n'établit pas à elle seule une victime ou une perte. Les définitions ci-dessous reformulent le vocabulaire employé dans l'entretien ; elles servent d'aide à la lecture, pas de constat statistique indépendant (p. 2-7).

- **Rançongiciel** — attaque associant une demande de paiement à l'indisponibilité de systèmes ou à la menace de divulguer des données volées.
- **Exfiltration** — sortie non autorisée de données d'un système ; l'extorsion peut ensuite porter sur leur publication, même sans chiffrement.
- **RaaS (*ransomware-as-a-service*)** — modèle dans lequel un opérateur fournit un outil ou une infrastructure à des affiliés qui mènent des attaques et partagent les recettes.
- **Affilié** — acteur utilisant le service d'un opérateur de rançongiciel pour trouver et attaquer des victimes ; ses compétences et résultats varient.
- **Courtier d'accès / *infostealer*** — dans le contexte de l'entretien, service ou logiciel permettant d'obtenir des identifiants utiles à une intrusion ; le document évoque surtout le vol d'identifiants par *infostealers*.
- **Mouvement latéral** — progression d'un système compromis vers d'autres ressources du réseau, souvent pour atteindre des données ou des droits d'administration.
- **Indicateur de compromission** — trace technique, comme une adresse IP, une empreinte de fichier ou un transfert anormal, pouvant aider à détecter une activité malveillante.
- **DDoS** — saturation d'un service par un grand nombre de requêtes, destinée à le rendre indisponible ; elle ne suppose pas en elle-même un vol de données.
- **Attribution** — rapprochement d'une activité avec des acteurs ; l'emploi d'une marque, d'un outil ou d'un pseudonyme commun ne suffit pas à établir l'identité des personnes.
- **IOCTA** — évaluation annuelle d'Europol sur la criminalité organisée sur Internet, qui sert de cadre à cette série d'entretiens.

## Résumé exécutif

Dans cet épisode, **Europol décrit le rançongiciel comme un écosystème de services et de groupes**, dont les formes vont des plateformes ouvertes aux équipes fermées. Michaël De Laet explique que les sauvegardes et les défenses contre le chiffrement ont poussé certains attaquants vers le vol de données, parfois sans tentative de chiffrement. Le nom public d'un groupe est devenu moins stable ; l'intervenant dit que **120 marques** ont été citées dans des messages reçus par Europol « l'année dernière », sans y voir 120 équipes nouvelles (p. 2-4, 8-10).

La coopération entre acteurs est l'autre fil conducteur. L'entretien présente les compétences complémentaires attribuées à Scattered Spider, Lapsus$ et ShinyHunters, les services proposés par DragonForce et les liens plus diffus de la communauté *The Com*. Il élargit ensuite la discussion aux DDoS à motivation politique, illustrés par l'opération Eastwood contre NoName057(16). Ces rapprochements sont ceux de l'intervenant ; la transcription n'expose ni dossiers d'enquête ni méthode d'attribution permettant de les vérifier indépendamment (p. 4-7).

Pour la veille, la conclusion utile est opérationnelle : **suivre les accès, les données sorties, les intermédiaires et les personnes derrière les marques**, sans confondre disparition d'un site de fuite et fin d'une activité. L'entretien signale aussi les sollicitations d'employés contre rémunération et l'intérêt d'une coopération entre enquêteurs, États et entreprises privées. Il donne toutefois très peu de séries chiffrées, de dénominateurs ou d'indicateurs de résultat ; ses projections sur l'IA et les paiements de rançon restent des positions ou hypothèses à tester (p. 2-12).

## Chronologie

La séquence compte ici parce qu'elle explique le déplacement du levier d'extorsion et situe les opérations citées ; les dates imprécises sont conservées comme telles.

1. **Avant la période récente :** selon l'intervenant, les défenses et sauvegardes ont progressivement limité la seule extorsion par chiffrement, tandis que le vol de données est devenu un levier supplémentaire (p. 2, 10).
2. **2023, selon le souvenir de l'intervenant :** DragonForce serait apparu ; il précise lui-même l'incertitude de cette date (p. 4).
3. **2025 :** l'entretien situe l'émergence de l'alliance entre Scattered Spider, Lapsus$ et ShinyHunters, la montée en visibilité de DragonForce, son annonce d'alliance en septembre et l'opération Eastwood contre NoName057(16). Le PDF ne donne pas la date exacte d'Eastwood (p. 4-6).
4. **Fin 2025-début 2026 :** De Laet situe une accélération perçue de l'usage de l'IA par les cybercriminels et une durée de vie plus courte des marques de rançongiciels (p. 2-3).
5. **2026 :** l'épisode commente l'IOCTA 2026 et anticipe une poursuite de l'adaptation des méthodes d'attaque (p. 1, 10).

## Thèse principale

Il s'agit d'un **entretien d'appréciation policière**, pas d'une étude expérimentale. De Laet soutient que la rentabilité du rançongiciel repose sur la capacité des acteurs à changer de technique et d'organisation dès qu'une défense ou une opération policière réduit leur marge. Les plateformes de services abaissent la barrière d'entrée, tandis que les alliances et les groupes fermés compliquent le travail d'enquête (p. 2-5, 9-10).

Cette thèse associe deux adaptations distinctes. La première concerne **l'extorsion** : passer du chiffrement au chantage sur les données quand la restauration devient possible. La seconde concerne **l'organisation criminelle** : changer de marque, combiner des compétences ou réserver l'accès à un cercle de confiance. L'intervenant ne prétend pas que tous les groupes évoluent vers le modèle fermé ; il dit explicitement que les trois modèles coexistent (p. 2-4, 8-10).

## Informations et arguments importants

### Du chiffrement au chantage sur les données

De Laet attribue le développement de l'exfiltration à l'amélioration des sauvegardes et de la détection du chiffrement. Dans certains cas récents, dit-il, les attaquants chercheraient les données sans même lancer de chiffrement. Il évoque aussi le recours à des *infostealers* pour voler des identifiants sans demander à l'utilisateur de les saisir, ainsi que des offres d'argent à des employés pour obtenir un accès. Ces mécanismes sont décrits oralement ; aucun taux de prévalence ni échantillon d'incidents n'est donné (p. 2, 7-8, 10).

Le chiffre de **120 marques** correspond, d'après lui, aux marques citées dans des messages reçus par Europol au cours de l'année précédente. Ce n'est ni un décompte des familles de logiciels, ni celui des groupes distincts, ni un total européen de victimes. De Laet propose le changement de marque après des succès policiers comme une explication partielle, qu'il présente avec prudence (p. 2-3).

### Trois formes de coopération criminelle

La typologie de l'entretien porte sur l'accès aux opérateurs et sur la confiance, plus que sur une sophistication technique linéaire. **Ouvert**, un RaaS comme LockBit dans le passé, ou selon l'intervenant RansomHub et Inc Ransomware, accepte largement des affiliés. **Semi-fermé**, un service tel que Qilin sélectionne ses partenaires par recommandation, forum réservé ou test de compétence. **Fermé**, un petit groupe travaille entre personnes déjà connues et garde ses outils pour lui, ce qui peut réduire la visibilité des enquêteurs. Le chiffre d'environ **20 %** pour la part de l'opérateur dans une rançon est présenté comme une valeur courante illustrative, pas comme une moyenne calculée (p. 3-4, 9-10).

De Laet insiste sur la diversité des affiliés : certains font très peu de victimes, d'autres plusieurs dizaines. Il ne voit **pas de tendance démontrée vers les groupes fermés** ; tous les modèles demeurent viables à ses yeux. Les offres ouvertes peuvent donner aux enquêteurs ou aux entreprises de sécurité une visibilité sur un panneau et une infrastructure en devenant clients ; les cercles fermés exigent un investissement d'enquête supérieur (p. 3-4, 9-10).

### Alliances, services et identités mouvantes

L'entretien attribue à **Scattered Spider** des compétences de manipulation sociale et de recrutement d'initiés, à **Lapsus$** le mouvement latéral, et à **ShinyHunters** l'exfiltration et l'extorsion. Il présente leur rapprochement en 2025 comme fluide, via des communautés telles que BreachForums et *The Com*. Cette dernière est décrite comme liée aussi à la fraude en ligne, à l'échange de cartes SIM, à des infractions touchant des mineurs et à des violences. De Laet précise qu'une personne peut revendiquer une appartenance sans adhésion formelle, ce qui rend les étiquettes fragiles pour l'attribution (p. 4).

**DragonForce** illustre la montée en gamme d'une offre criminelle : diffusion d'outils compatibles avec plusieurs plateformes, puis service d'analyse des données volées afin de trouver un moyen de pression sur des cibles à forte valeur. L'intervenant rapporte une annonce d'alliance avec Qilin et un acteur se réclamant de LockBit ; la continuité de LockBit après l'opération policière est donc une **revendication rapportée**, non une identité établie par le PDF (p. 4-5).

### DDoS, coopération et détection

À propos de **NoName057(16)** et d'Eastwood, De Laet distingue l'indisponibilité technique, parfois courte selon lui, de l'effet politique recherché par les revendications et leur reprise médiatique. Il décrit **DDoSia** comme un outil installé volontairement par des sympathisants, dont certains résidaient en Europe. L'action policière aurait combiné perturbation d'infrastructure, perquisitions, arrestations et prises de contact avec des participants. Il dit que la réponse doit dépendre du rôle de chacun, sans suggérer que toute participation donne lieu à une arrestation (p. 5-6).

Pour les rançongiciels, il ne fournit **aucun indicateur de compromission précis**. Il évoque les traces possibles à chaque étape de l'intrusion, les transferts anormaux de données, le vol d'identifiants et la nécessité de sensibiliser les employés aux offres de corruption. Europol reçoit des demandes de recoupement des États, produit des analyses plus approfondies et coordonne des enquêtes ; l'apport de partenaires privés doit, selon l'intervenant, être accepté par les États dont les données seraient partagées (p. 2, 7, 11).

### Intelligence artificielle et prévention

De Laet estime que l'IA accélère l'écriture de code et les intrusions, mais dit également voir des outils prometteurs du côté défensif. Il cite des modèles de plusieurs fournisseurs sans test comparatif et souhaite raccourcir les délais d'autorisation des usages policiers, tout en maintenant contrôle et gouvernance. Son pronostic d'attaques plus rapides « pour le reste de 2026 » est une **anticipation**, pas une mesure tirée de la transcription (p. 3, 8, 10).

En fin d'épisode, il conseille aux particuliers mises à jour, mots de passe uniques via gestionnaire et prudence devant les sollicitations. Il estime que les entreprises sont devenues des cibles plus rémunératrices que les particuliers. Ces conseils généraux ne constituent ni une stratégie complète de sécurité d'entreprise ni une preuve que les particuliers ne sont plus exposés (p. 12).

## Points particulièrement intéressants pour la veille

L'entretien donne surtout des **pistes de suivi**. Elles demandent de relier plusieurs indices avant de conclure à une évolution du marché ou à l'effet d'une opération.

- **Marques contre opérateurs.** Europol rapporte 120 noms cités dans ses messages, tout en signalant le changement de marque. *Inférence pour la veille :* suivre les personnes, infrastructures, outils et affiliés derrière plusieurs noms plutôt que compter chaque nom comme un nouvel acteur (p. 2-3).
- **Extorsion sans chiffrement.** Le vol de données peut suffire à la demande de paiement. *Inférence pour la veille :* suivre les exfiltrations et l'exposition des données même lorsque les sauvegardes restaurent les systèmes (p. 2, 8, 10).
- **Services spécialisés.** DragonForce aurait ajouté l'analyse des données volées à son offre. *Inférence pour la veille :* documenter les fonctions vendues autour de l'attaque, et pas seulement les familles de logiciels malveillants (p. 4-5).
- **Accès par les employés.** Les offres de corruption complètent le phishing et le vol automatisé d'identifiants. *Inférence pour la veille :* intégrer les sollicitations d'initiés aux signaux de risque et aux dispositifs d'alerte interne (p. 2, 4, 7).
- **DDoS et effet informationnel.** L'intervenant distingue l'indisponibilité mesurée de la visibilité politique d'une revendication. *Inférence pour la veille :* relever séparément durée réelle, services touchés, revendications et diffusion médiatique (p. 5-6).

## Faits, opinions et interprétations

### Faits rapportés par la source

Europol publie une transcription officielle d'un échange avec Michaël De Laet, consacré à l'IOCTA 2026, au rançongiciel et au DDoS. L'intervenant rapporte **120 marques** dans des messages reçus par Europol sur la période qu'il nomme « l'année dernière », présente trois modèles d'organisation des groupes et décrit Eastwood ainsi que le travail de coordination d'EC3. Ce sont des **déclarations de la source** : le PDF ne donne pas accès aux messages, aux dossiers d'enquête, aux données de victimes ou aux protocoles de comptage (p. 1-7, 9-11).

### Opinions ou positions de l'auteur

De Laet juge le modèle du rançongiciel encore rentable, considère le DDoS souvent moins grave sur le plan technique que des intrusions avec vol de données et veut que la police signale aux participants d'Eastwood le caractère pénal de leurs actes. Il est optimiste sur les usages défensifs de l'IA, tout en plaidant pour des autorisations policières plus rapides sous contrôle. Ses appréciations sur la gravité relative, la rentabilité, l'effet dissuasif et la vitesse d'adoption de l'IA ne sont pas des mesures indépendantes produites dans l'entretien (p. 2, 5-6, 8-10).

### Interprétations et inférences

La lecture d'ensemble suggère une **substitution partielle du levier d'extorsion** et une **recomposition des relations entre acteurs**, plutôt qu'un remplacement uniforme d'une famille de rançongiciels par une autre. L'absence de tendance vers les groupes fermés, explicitement affirmée par l'intervenant, empêche d'en faire une loi générale. Pour évaluer l'action publique, il faudrait mesurer la persistance des mêmes opérateurs après changement de nom et la réduction durable des victimes après démantèlement ; ces deux mesures sont absentes du PDF (p. 2-5, 9-10).

## Limites et points à vérifier

1. **Transcription et contexte oral.** Le PDF prévient que la transcription automatisée a été éditée et peut comporter des erreurs. Les noms de groupes, les dates approximatives et les formulations techniques devraient être recoupés avant une citation littérale (p. 4-5, 12).
2. **Population des 120 marques inconnue.** Le comptage concerne des messages reçus par Europol, sans volume total, période calendaire exacte ni méthode de dédoublonnage. Il ne mesure pas directement le nombre d'équipes ou de victimes en Europe (p. 2-3).
3. **Économie du RaaS peu quantifiée.** La part de **20 %** est illustrative ; l'entretien ne fournit pas de distribution des commissions, de paiements ni de taux de réussite. La rentabilité globale ne peut pas en être calculée (p. 3, 9).
4. **Alliances et attribution sans pièces jointes.** Les rôles attribués aux groupes et les liens au sein de *The Com* sont exposés oralement, sans preuves techniques ou judiciaires présentées. Les revendications d'appartenance peuvent être opportunistes (p. 4-5).
5. **Effet d'Eastwood non mesuré dans le temps.** L'entretien rapporte des mesures policières et une perturbation d'infrastructure, mais ne donne ni série avant/après ni trajectoire de reconstitution du réseau (p. 5-6).
6. **Impact DDoS dépendant du contexte.** La faible durée ou gravité technique évoquée par l'intervenant n'est pas assortie d'un échantillon et ne vaut pas pour tout service essentiel ou toute campagne (p. 5-6).
7. **IA et détection sans évaluation.** Aucun indicateur de performance d'outil défensif, de gain d'efficacité criminelle ou de taux d'usage de l'IA n'est communiqué ; aucun indicateur de compromission concret n'est livré (p. 3, 7-10).
8. **Paiement des rançons et sécurité des individus.** Les effets d'une interdiction de payer et l'idée d'un moindre ciblage des particuliers sont discutés sans étude d'impact ni mesure d'exposition ; ils ne doivent pas servir seuls de base à une décision (p. 9, 12).

## Sources et références mentionnées

L'entretien cite l'**IOCTA 2026**, l'opération **Eastwood** contre **NoName057(16)**, la perturbation de **LockBit**, l'exemple d'**Emotet**, plusieurs groupes de rançongiciels et une alerte des pays **Five Eyes** sur l'IA sans en fournir la référence précise. Il mentionne aussi un guide de prévention d'Europol, *The Cyber Aware Mindset*, et renvoie aux notes de l'épisode pour les ressources ; ces notes ne figurent pas dans le PDF. Il s'agit donc d'un entretien riche en exemples, sans bibliographie ni annexes probantes (p. 1-5, 10, 12).

## Cinq éléments essentiels à retenir

1. **Le levier d'extorsion se déplace** vers la menace de divulguer des données, parfois sans chiffrement (p. 2, 8, 10).
2. **Les 120 marques citées** dans des messages reçus par Europol ne sont pas 120 groupes distincts démontrés (p. 2-3).
3. **RaaS ouvert, groupes semi-fermés et groupes fermés** coexistent ; l'intervenant ne constate pas de bascule générale vers les derniers (p. 3-4, 9-10).
4. **Alliances et services spécialisés** complètent les outils de rançongiciel, mais leur attribution exige plus que des noms revendiqués (p. 4-5).
5. **La réponse doit regarder l'accès initial, l'exfiltration et les personnes**, tout en distinguant impact technique et effet politique des DDoS (p. 5-8, 11).

## État de l'art et regards extérieurs

Recherches effectuées le **2026-10-11**. Les publications ci-dessous ont été consultées après la lecture de la transcription ; elles servent à la situer et à tester ses affirmations, sans changer ce que le PDF prouve à lui seul.

### Travaux de référence

- **Cadre policier européen.** La [page de l'IOCTA d'Europol, édition 2026 datée du 28 avril 2026](https://www.europol.europa.eu/publications-events/main-reports/internet-organised-crime-threat-assessment) situe l'entretien dans les évaluations de l'EC3 sur les cyberattaques, l'exploitation sexuelle d'enfants, la fraude et les facilitateurs du cybercrime. Elle confirme le cadre institutionnel, sans rendre publiques les données opérationnelles évoquées oralement.
- **Mesure indépendante et périmètre.** L'[ENISA, *Threat Landscape 2025*, 1er octobre 2025, version corrigée en 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) décrit la fragmentation du marché et **82 variantes** de rançongiciels rapportées contre des organisations des États membres sur sa période **juillet 2024-juin 2025**. Cette catégorie, cette fenêtre et cette méthode diffèrent des **120 marques citées dans des messages reçus par Europol** ; les deux chiffres ne sont pas additionnables ni contradictoires.

### Compléments sur le sujet

Le podcast met l'accent sur l'organisation des délinquants. Quatre sources extérieures précisent ce que cela implique pour les victimes, les enquêteurs et la mesure de la menace.

1. **Sauvegarder ne suffit pas contre le vol.** Le [guide conjoint CISA/FBI/NSA/MS-ISAC, *#StopRansomware Guide*, révision du 19 octobre 2023](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) distingue explicitement chiffrement avec fuite de données et extorsion fondée seulement sur la fuite. Il recommande des sauvegardes hors ligne **testées**, mais aussi la surveillance des transferts sortants, le contrôle des accès, la segmentation et un plan de réponse. L'argument de De Laet sur l'exfiltration est donc compatible avec la doctrine de réponse ; il ne rend pas les sauvegardes inutiles.
2. **L'écosystème n'est pas une seule famille.** L'[ENISA, *Threat Landscape 2025*, 1er octobre 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) décrit la multiplication des variantes et des programmes RaaS après actions policières et concurrence interne. Ses **82 variantes** dans un ensemble d'incidents observés ne disent rien, à elles seules, du nombre de personnes derrière les marques. Cela renforce l'intérêt de suivre les infrastructures et affiliés, tout en rappelant les biais de chaque dispositif de collecte.
3. **DDoS : fréquence et gravité sont deux axes.** L'[ENISA, *Threat Landscape 2026*, 22 septembre 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) et sa [présentation des résultats du 22 septembre 2026](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape) indiquent que les DDoS idéologiques représentent **82 % des événements enregistrés contre les administrations publiques** dans leur jeu de données, alors que le rançongiciel reste le type d'incident au plus fort impact à court terme. Le **82 %** porte sur les événements observés dans ce secteur, pas sur toutes les attaques en Europe ; il aide à séparer fréquence et effet réel.
4. **Un cas concret d'extorsion.** Dans un [avis sur Play mis à jour le 4 juin 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a), CISA, le FBI et l'ACSC australien décrivent une chaîne comprenant vol de données, chiffrement et menace de publication, ainsi qu'un groupe présumé fermé. Il donne un exemple technique du modèle décrit par De Laet, sans confirmer la structure ou la pratique de tous les groupes qu'il nomme.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| Il s'agit d'une transcription officielle d'un épisode Europol sur le rançongiciel. | **Confirmé.** L'épisode est publié le **31 juillet 2026**, mis à jour le **13 août 2026** ; ces dates n'apparaissent pas dans le PDF. | [Europol — page officielle de l'épisode 25, saison 4 épisode 3](https://www.europol.europa.eu/media-press/europol-podcast/episode-25-how-ransomware-is-evolving). |
| « 120 marques » sont citées dans des messages reçus par Europol sur la période évoquée. | **Non établi indépendamment.** Aucun jeu de messages ni protocole de comptage public n'accompagne la transcription ; les **82 variantes** d'ENISA portent sur une autre unité et une autre période. | [ENISA — *Threat Landscape 2025*](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025), 1er octobre 2025. |
| Eastwood a perturbé NoName057(16) et mobilisé plusieurs pays. | **Confirmé et précisé.** Europol date l'opération des **14-17 juillet 2025** et annonce plus de **100 systèmes** perturbés, **deux arrestations** et plus de **1 000 sympathisants** avertis ; ce sont les résultats annoncés, pas une mesure de l'extinction durable du réseau. | [Europol — bilan d'Eastwood, 16 juillet 2025](https://www.europol.europa.eu/media-press/newsroom/news/global-operation-targets-noname05716-pro-russian-cybercrime-network). |
| Les attaquants peuvent extorquer sans chiffrer après une exfiltration. | **Confirmé comme mode opératoire documenté.** Sa fréquence européenne actuelle n'est pas mesurée par ce seul guide. | [CISA et partenaires — *#StopRansomware Guide*, 19 octobre 2023](https://www.cisa.gov/resources-tools/resources/stopransomware-guide). |
| La commission de l'opérateur RaaS est « souvent » de 20 %. | **Non établi comme moyenne générale.** Le PDF présente une valeur illustrative et les sources primaires consultées ici ne publient pas de distribution représentative des commissions. | [Europol — entretien officiel, 31 juillet 2026](https://www.europol.europa.eu/media-press/europol-podcast/episode-25-how-ransomware-is-evolving) ; [ENISA — *Threat Landscape 2025*](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025). |
| L'IA accélère effectivement les attaques par rançongiciel. | **Nuancé.** ENISA juge l'usage malveillant des modèles émergents probable ; le PDF n'apporte ni comparaison contrôlée ni gain mesuré. Un cas ultérieur est décrit ci-dessous, sans prouver une accélération générale. | [ENISA — présentation du *Threat Landscape 2026*, 22 septembre 2026](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape) ; [Europol — KillSwitch, 1er octobre 2026](https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site). |

### Contrepoints et critiques

- **Le DDoS ne se réduit pas à une capture d'écran.** La distinction de De Laet entre bruit politique et dommage technique est utile, mais l'[ENISA (22 septembre 2026)](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape) montre la fréquence des attaques contre les administrations. Le risque concret doit être apprécié service par service, avec sa durée, son rôle et les perturbations en aval ; l'entretien n'en fournit pas la mesure.
- **Arrêter un flux financier n'épuise pas le débat.** De Laet évoque des initiatives d'interdiction du paiement comme voie possible pour réduire la rentabilité. Le [guide CISA (19 octobre 2023)](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) privilégie préparation, confinement, enquête et restauration, sans prétendre qu'une règle de paiement suffirait. L'effet d'une interdiction sur la sécurité des victimes ou les formes d'extorsion n'est pas évalué dans le podcast.

### Évolutions depuis la publication

Depuis la mise en ligne de l'épisode le **31 juillet 2026**, l'[ENISA a publié son *Threat Landscape 2026* le 22 septembre 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026), confirmant que le rançongiciel demeure, dans son analyse, le type d'incident au plus fort impact à court terme. Le [1er octobre 2026, Europol a annoncé l'opération KillSwitch contre KillSec](https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site) : contrôle du site de fuite le **30 septembre**, **trois arrestations provisoires**, huit perquisitions et au moins **110 téraoctets** de données soustraits à un accès ultérieur non autorisé, selon son communiqué. Europol dit que les enquêteurs ont relevé un usage de l'IA pour maintenir l'infrastructure et trouver des cibles. Ce cas appuie l'existence de certains usages, sans établir le gain de vitesse global anticipé dans l'entretien ni la disparition durable du groupe.

### Cadre juridique et éthique

- **Notification des incidents dans l'UE.** La [directive (UE) 2022/2555, dite NIS2, article 23](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32022L2555), prévoit pour les entités essentielles et importantes concernées une **alerte précoce sous 24 heures** et une **notification sous 72 heures** après connaissance d'un incident significatif, selon les conditions du texte et sa transposition nationale. Cela concerne la gestion et le partage de l'information sur l'incident ; le podcast ne détaille pas ces obligations.
- **Coopération et données.** Les échanges opérationnels avec des partenaires privés que décrit De Laet supposent l'accord des États concernés selon ses propos (p. 7, 11). La [réglementation d'Europol (UE) 2016/794, version consolidée au 11 janvier 2026](https://eur-lex.europa.eu/eli/reg/2016/794/2026-01-11/eng) encadre les finalités, les catégories de données et leur traitement ; l'entretien ne précise ni la base de chaque partage ni les garanties appliquées à un usage policier de l'IA.

### Pour aller plus loin

- [Europol — page et transcription officielles de l'épisode (31 juillet 2026)](https://www.europol.europa.eu/media-press/europol-podcast/episode-25-how-ransomware-is-evolving) : revenir à la version institutionnelle de l'entretien.
- [Europol — IOCTA 2026 (28 avril 2026)](https://www.europol.europa.eu/publications-events/main-reports/internet-organised-crime-threat-assessment) : replacer les propos dans l'évaluation stratégique annuelle.
- [ENISA — *Threat Landscape 2026* (22 septembre 2026)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) : comparer les types d'incidents avec un périmètre et une méthode distincts.
- [CISA et partenaires — *#StopRansomware Guide* (19 octobre 2023)](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) : préparer détection, réponse et restauration, y compris en cas de vol de données.
- [Europol — bilan d'Eastwood (16 juillet 2025)](https://www.europol.europa.eu/media-press/newsroom/news/global-operation-targets-noname05716-pro-russian-cybercrime-network) : vérifier le nombre et la nature des actions annoncées contre NoName057(16).
