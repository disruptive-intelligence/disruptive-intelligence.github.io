---
title: "Analyse — Commission européenne (JRC) et Europol : prospective des technologies de confidentialité"
date: 2026-10-08
kind: analysis
document_type: rapport
theme: "tech"
slug: commission-europeenne-jrc-et-europol-prospective-des-technologies-de-confidentialite
author: "Sigita Trainauskiene, João Farinha, Mark Wittfoth, Diederik Don et Alexandra de Maleville"
organization: "Centre commun de recherche de la Commission européenne (JRC) et Europol"
tags:
  - technologies de confidentialité
  - cryptographie
  - prospective technologique
  - police judiciaire
  - protection des données
  - intelligence artificielle
source_file: inbox/Horizon-scanning-emerging-privacy-enhancement-tech.pdf
source_url: https://publications.jrc.ec.europa.eu/repository/handle/JRC143326
---

# Analyse — Commission européenne (JRC) et Europol : prospective des technologies de confidentialité

## Métadonnées

- **Document :** *Horizon scanning on emerging privacy enhancement technologies — A participatory technology foresight exercise developed by the JRC and Europol to support policy makers and law enforcement agencies*, rapport de 2026. L'original de 180 pages PDF est conservé dans `inbox/Horizon-scanning-emerging-privacy-enhancement-tech.pdf` ; le corps du rapport va jusqu'à la p. 69 imprimée, suivi des références et d'une longue annexe de signaux.
- **Auteurs :** Sigita Trainauskiene, João Farinha et Alexandra de Maleville (JRC), Mark Wittfoth et Diederik Don (Europol), selon la couverture et la liste des auteurs (couverture, p. 4).
- **Éditeurs :** Centre commun de recherche (JRC) de la Commission européenne et Europol, avec publication par l'Office des publications de l'Union européenne ; les deux institutions figurent sur la couverture et dans les crédits (couverture, p. de crédits). Le texte précise que ses contenus ne constituent pas nécessairement une position officielle de la Commission (p. de crédits).
- **Date et identifiants :** 2026 ; le jour de parution n'est pas indiqué dans le PDF. Référence JRC143326 ; ISBN PDF 978-92-68-42189-5 ; DOI PDF 10.2760/6084454 (p. de crédits).
- **Périmètre :** technologies de protection de la vie privée, technologies voisines et facteurs qui pourraient aider ou entraver les enquêtes des services répressifs européens à court et long terme (p. 11-16, 26, 38).
- **Méthode de cette analyse :** jusqu'aux « Cinq éléments essentiels », les constats proviennent uniquement du rapport, avec sa pagination **imprimée**. La section finale confronte séparément ces constats à des sources publiques consultées le 8 octobre 2026.

## Repères pour comprendre le document

Le rapport est un **exercice de prospective participative**, et non un essai comparatif de performances ni une enquête représentative sur l'usage criminel des technologies. Le JRC et Europol ont collecté des signaux de changement, demandé à un groupe d'experts de les hiérarchiser, puis approfondi des pistes à plus long terme par entretien. Leur question est double : comment protéger les données des citoyens et des enquêteurs, et comment enquêter lorsque ces protections rendent certains contenus moins accessibles ? Des objets retenus, comme les drones ou les robots humanoïdes, ne sont pas des technologies de confidentialité au sens strict ; les auteurs élargissent explicitement le périmètre aux technologies qui affectent l'identité, la surveillance ou la sécurité des données (p. 5, 14-16, 26-27).

- **PET (*privacy-enhancing technology*)** — Ensemble de techniques destinées à protéger la confidentialité ou la sécurité des données pendant leur collecte, leur traitement ou leur partage. Le rapport emploie une acception large, qui inclut parfois des technologies connexes (p. 17, 26-27).
- **Signal faible et *horizon scanning*** — Indice d'une nouveauté potentiellement importante, puis méthode de collecte et d'interprétation de tels indices ; le signal ne prouve pas qu'une adoption à grande échelle aura lieu (p. 14-15).
- **Confidentialité des entrées et des sorties** — Protection des données introduites dans un calcul, ou protection des résultats contre la reconstruction des données initiales. Le rapport reprend cette distinction de classifications existantes (p. 20).
- **Calcul multipartite sécurisé (MPC ou SMPC)** — Plusieurs parties calculent un résultat commun sans communiquer leurs données brutes les unes aux autres ; cela ne règle pas à lui seul qui peut demander le calcul (p. 20-21, 39-40).
- **Chiffrement homomorphe complet (FHE)** — Calcul sur des données chiffrées sans déchiffrer les données pendant l'opération ; sa portée pratique dépend fortement des coûts de calcul et du type de tâche (p. 7, 39-40).
- **Apprentissage fédéré (FL)** — Entraînement d'un modèle sur des données conservées localement, avec partage d'informations sur le modèle plutôt que des fichiers de données brutes. Cette architecture demande elle aussi des protections contre les fuites possibles (p. 30-31, 43).
- **Environnement d'exécution de confiance (TEE)** — Espace de calcul isolé matériellement et attesté, destiné à protéger code et données pendant leur traitement, y compris vis-à-vis de l'hébergeur (p. 35).
- **Preuve à divulgation nulle de connaissance (ZKP)** — Preuve permettant de vérifier une propriété sans révéler l'ensemble des informations qui la fondent ; exemple pédagogique : attester un âge requis sans donner sa date de naissance (p. 20-21, 39).
- **Cryptographie post-quantique (PQC) et distribution quantique de clés (QKD)** — La première désigne des algorithmes classiques conçus pour résister à de futurs ordinateurs quantiques ; la seconde emploie des propriétés quantiques pour distribuer des clés. Les deux ne sont pas interchangeables (p. 38, 47-49).
- **Métadonnées** — Informations sur les communications, telles qu'adresse IP, localisation ou relations entre correspondants, distinctes du contenu des messages ; elles peuvent révéler des comportements même si le contenu est chiffré (p. 40-41).
- **PESTEL** — Grille de lecture des facteurs politiques, économiques, sociaux, technologiques, environnementaux et juridiques qui influencent une technologie, sans établir à elle seule une causalité (p. 56, 59).

## Résumé exécutif

Le JRC et Europol proposent une **carte de technologies à surveiller** pour les politiques publiques et les enquêtes. L'exercice part de plus de 200 signaux collectés, en retient 178 pour discussion et demande à environ vingt participants d'identifier dix sujets jugés prioritaires. La sélection couvre aussi bien la détection des deepfakes et les communications difficiles à intercepter que l'apprentissage préservant la confidentialité, les environnements d'exécution de confiance, l'analyse comportementale, les drones et la robotique. Les auteurs savent qu'une partie de cette liste déborde la définition habituelle des PET (p. 5-6, 14-16, 26-37).

Sept entretiens complètent l'atelier sur le calcul chiffré, la cryptographie post-quantique, l'IA, les communications quantiques, la 6G et les registres distribués. Le **calcul sur données protégées** est l'idée directrice la plus féconde : des institutions pourraient partager des résultats ou détecter des fraudes sans centraliser toutes les données brutes. Mais protéger le contenu ne suffit pas à garantir la confidentialité des métadonnées, la sûreté des sorties, la fiabilité d'un modèle ou la légalité d'un accès ciblé (p. 7-8, 38-55).

Le rapport défend simultanément l'adoption des PET par les services répressifs et le développement de leurs capacités d'enquête lorsque des suspects utilisent ces mêmes outils. Il recommande compétences, coopération, recherche et clarification des règles d'accès. Ce sont des **priorités proposées**, pas des effets démontrés : le travail repose sur un atelier et quelques entretiens, sans classement quantitatif reproductible des risques, démonstration opérationnelle commune ni mesure de l'efficacité des solutions préconisées (p. 5, 9-10, 14-16, 65-69).

Pour la veille, la valeur du texte réside dans les croisements entre confidentialité, cybersécurité, preuve numérique et stratégie industrielle. Sa faiblesse principale est de juxtaposer technologies déployées, prototypes, hypothèses et scénarios à horizon incertain. L'analyse doit donc suivre chaque piste avec son **niveau de maturité, son cas d'usage et ses garanties vérifiables**, plutôt que traiter les dix sujets de l'atelier comme dix menaces déjà constatées (p. 26-27, 31-39, 65-69).

## Chronologie

Cette séquence explique l'âge des signaux et la différence entre le moment où les experts ont été consultés et celui où le rapport a été publié.

- **Juillet-novembre 2024 :** le groupe JRC-Europol réalise la recherche documentaire et rassemble plus de 200 signaux technologiques et contextuels ; les documents examinés portent surtout sur 2020-2024 (p. 14-15).
- **13 novembre 2024 :** un atelier en ligne réunit environ vingt spécialistes de la technique, du droit, de la police, des politiques publiques, des entreprises et de la société civile ; ils discutent 178 signaux et hiérarchisent dix sujets (p. 15-16, 26).
- **Janvier-avril 2025 :** sept entretiens semi-directifs étendent la réflexion aux technologies à plus long terme, au-delà de l'horizon d'environ cinq ans traité par l'atelier (p. 16, 38).
- **2026 :** publication du rapport de prospective et de ses recommandations ; cette date ne signifie pas que chaque prototype ou scénario décrit ait été revalidé en 2026 (couverture, p. de crédits, 65-69).

## Thèse principale

Le rapport soutient que les **technologies de confidentialité sont à double usage** : elles peuvent réduire l'exposition des citoyens et sécuriser les échanges de renseignement, tout en compliquant l'accès à certains éléments de preuve. La réponse préconisée est de développer des capacités techniques et juridiques adaptées, notamment le calcul sur données protégées, la cryptographie post-quantique, la formation et la coopération entre institutions. Les auteurs présentent cet arbitrage comme une question de conception des usages et des garanties, davantage que comme une propriété intrinsèquement bonne ou mauvaise d'un outil (p. 5-10, 24-25, 65-69).

Il s'agit d'une **synthèse prospective orientée vers les besoins de l'enquête**. Le document reconnaît le droit à la vie privée et les avantages des PET, mais ses scénarios d'emploi, ses choix de financement et ses propositions d'accès légal sont formulés depuis la perspective des services répressifs. Ils ne constituent ni une preuve que l'accès exceptionnel au contenu chiffré serait techniquement sûr, ni une évaluation juridique de chaque usage envisagé (p. 5, 12-16, 24-25, 40-42, 65-69).

## Informations et arguments importants

Le rapport articule trois niveaux qu'il faut garder séparés : **méthode de sélection**, **propriétés techniques et scénarios**, puis **choix de politique publique**. Les mêmes mots, notamment « risque » et « prometteur », changent de sens selon qu'ils décrivent une capacité déjà utilisable, une possibilité technique ou une priorité exprimée en atelier (p. 14-16, 26-27, 38, 65-69).

### Une sélection d'experts, non un palmarès de maturité

Le groupe collecte d'abord plus de 200 signaux à partir de publications scientifiques, brevets, projets, actualités et contributions d'experts. Il en soumet **178 à l'atelier : 116 classés comme PET, 71 comme facteurs contextuels et 9 dans les deux catégories**. Ces nombres se recoupent, d'où 116 + 71 − 9 = 178. Les participants, répartis en trois groupes, discutent les signaux avant de choisir dix sujets. Le rapport ne publie pas de score comparable de performance, de coût ou de probabilité d'adoption pour ces dix entrées. Il reconnaît que l'atelier et sept entretiens limitent la portée des recommandations (p. 5-6, 14-16, 26-27).

Les dix sujets sont **détection de deepfakes ; communications résistantes à l'interception ; Internet des comportements ; biométrie multicouche ; apprentissage automatique préservant la confidentialité ; petits drones solaires ; fondements de l'IA ; injection de signaux adversariaux ; TEE ; robots humanoïdes**. Les auteurs les regroupent ensuite en cinq ensembles : IA, identité et biométrie, communications et environnements sûrs, robotique et drones, approches comportementales. Ce regroupement est une interprétation du projet après atelier, non une taxonomie stabilisée des PET. La présence de drones et de robots est justifiée par leurs effets possibles sur l'identité et la vie privée (p. 6-7, 26-37).

### Le calcul sécurisé crée des voies de coopération, avec des limites différentes

Les technologies centrales du rapport ne sont pas interchangeables. **FHE** protège des données pendant certains calculs mais impose un surcoût de calcul ; **MPC** répartit le calcul entre participants qui ne livrent pas leurs données brutes ; **FL** entraîne un modèle sur des données locales ; **TEE** isole matériellement une exécution ; **ZKP** permet de prouver une propriété sans révéler toutes les données sous-jacentes. Les auteurs envisagent des analyses communes de données sensibles, y compris pour détecter des fraudes et partager du renseignement. La protection des entrées ne supprime pourtant ni les fuites par les résultats ou les mises à jour de modèles, ni les erreurs d'implémentation, ni la nécessité d'une base légale et d'un contrôle des requêtes (p. 20-23, 30-31, 35, 39-41).

Les entretiens soulignent qu'un fournisseur de cloud ne peut pas nécessairement livrer un contenu dont seule la personne détient la clé. Ils avancent une autre question pour l'enquête : **quels calculs autoriser sur un jeu protégé, et à qui donner le résultat ?** Un résultat agrégé de fraude peut être utile sans divulguer les dossiers individuels ; une requête apparemment simple visant un enregistrement particulier peut au contraire les révéler. Le rapport évoque aussi la collecte locale, l'analyse des métadonnées et le renseignement humain. Il ne présente pas de protocole démontré qui résoudrait à lui seul les arbitrages entre preuve, contrôle d'accès et droits (p. 39-42).

### Identité, IA et intégrité de la preuve

La **détection des deepfakes** arrive parmi les thèmes jugés les plus urgents par les participants. Le texte évoque des détecteurs fondés sur l'apprentissage, des traces de bruit et des filigranes. Il relie la falsification à l'usurpation d'identité, à la fabrication de pièces apparentes et au discrédit possible de preuves authentiques. La biométrie multimodale peut renforcer l'authentification, mais une donnée biométrique volée n'est pas réinitialisable comme un mot de passe ; les auteurs mentionnent l'attaque des capteurs et des systèmes par leurres ou signaux adversariaux (p. 27, 29-30, 34-35, 67).

L'**IA explicable**, le *machine unlearning* et l'apprentissage préservant la confidentialité sont présentés comme des outils possibles pour l'analyse judiciaire et la protection des données. Le rapport donne des exemples modestes d'assistance, comme l'examen d'images ou le comptage d'objets saisis, et projette des usages plus intrusifs, comme l'identification d'auteurs anonymes à partir de leur style d'écriture. Il reconnaît les risques de biais, d'opacité et de conclusions non vérifiables devant une juridiction. Les possibilités de police prédictive sont évoquées, sans évaluation empirique de leurs erreurs ou de leurs effets distributifs (p. 30-33, 42-46).

### Communications, quantique et réseaux futurs

Le rapport associe **Tor, VPN décentralisés, messageries chiffrées et réseaux de mélange** à une meilleure protection contre l'observation des communications, mais aussi à des enquêtes plus difficiles. Il présente l'analyse des métadonnées comme une voie alternative ; celles-ci restent pourtant des informations sensibles sur les relations, les déplacements et les habitudes. Ses descriptions de « totale anonymité » ou de communications « impossibles à intercepter » doivent se lire comme les caractérisations du rapport, non comme des garanties établies pour toutes les configurations (p. 24-25, 28, 40-42).

La **PQC** répond au risque de conservation de données chiffrées aujourd'hui pour les déchiffrer plus tard ; la **QKD** désigne une autre technique de distribution de clés, avec des exigences d'infrastructure jugées peu accessibles à la plupart des acteurs criminels. Le texte anticipe aussi une **6G** dotée de capacités de détection de l'environnement, d'IA dans le réseau et de connexions satellitaires. Ces dispositifs pourraient créer des sources de preuve, mais aussi de nouveaux moyens de suivi des personnes et des difficultés d'attribution ou de juridiction. Les calendriers avancés pour la cryptographie et la 6G sont des projections rapportées par les experts, non des échéances garanties (p. 38-39, 47-51).

### Facteurs d'adoption et propositions publiques

La dernière partie applique une grille PESTEL et une adaptation du « triangle des futurs » aux **moteurs, facilitateurs et obstacles** : concurrence technologique États-Unis-Chine, coût de l'innovation, réglementation européenne, pénurie de compétences, cybersécurité, matières premières, empreinte énergétique et attitudes sociales envers la confidentialité. Les participants ne s'accordent pas toujours sur le signe de l'effet : un même texte, comme le règlement sur les marchés numériques ou le règlement sur l'IA, peut stimuler la protection des données et accroître les contraintes d'implémentation. Le rapport cite la protection de la vie privée comme droit fondamental tout en demandant une meilleure capacité d'accès judiciaire aux preuves (p. 56-64).

Ses **propositions de financement et de formation** portent sur la cryptographie, l'IA, la criminalistique numérique, l'interopérabilité, les outils communs, l'éthique et les partenariats public-privé. La question concrète laissée ouverte est celle de la gouvernance : quel service peut interroger quelles données, pour quel but, avec quel contrôle et quelle possibilité de contestation ? Le rapport demande de clarifier ces règles, mais ne fournit pas de hiérarchie chiffrée entre investissements ni de démonstration coût-bénéfice (p. 65-69).

## Points particulièrement intéressants pour la veille

La veille utile suit ici des **conditions de déploiement et de contrôle**, plutôt que l'apparition isolée de mots techniques.

- **Du partage de fichiers au partage de calculs.** Le rapport envisage FHE, MPC, FL et TEE pour travailler sur des informations sensibles sans les centraliser. *Inférence pour la veille :* demander, dans chaque pilote, qui voit les données brutes, le modèle, les requêtes et les sorties, ainsi que les résultats des audits de fuite (p. 30-31, 35, 39-41).
- **Métadonnées malgré le chiffrement.** Les entretiens notent que le contenu peut rester secret alors que les relations et déplacements sont encore observables. *Inférence pour la veille :* suivre aussi les protections des métadonnées et les limites juridiques de leur exploitation, pas seulement les méthodes d'accès au contenu (p. 40-42).
- **Preuve face aux contenus synthétiques.** Deepfakes, filigranes et détecteurs affectent l'authenticité des pièces, mais aucun détecteur n'est présenté ici avec une performance généralisable. *Inférence pour la veille :* documenter provenance, chaîne de conservation, faux positifs et contestabilité des résultats (p. 27, 32-33, 67).
- **Préparation post-quantique.** Les auteurs insistent sur les données captées aujourd'hui et susceptibles d'être déchiffrées à l'avenir. *Inférence pour la veille :* suivre les inventaires cryptographiques et les migrations réelles, en séparant PQC et QKD (p. 38-39, 47-49).
- **Réseaux et capteurs à venir.** La 6G et l'Internet des comportements sont étudiés pour leurs usages policiers et leurs capacités de profilage. *Inférence pour la veille :* suivre les standards de détection intégrée, les usages effectifs et les évaluations de vie privée avant de parler de surveillance généralisée (p. 29, 49-51).
- **Décalage des horizons.** L'atelier date de 2024, les entretiens de 2025 et la publication de 2026. *Inférence pour la veille :* requalifier périodiquement chaque signal comme concept, prototype, produit ou déploiement documenté, plutôt que reprendre sa maturité implicite (p. 14-16).

## Faits, opinions et interprétations

### Faits rapportés par la source

Le rapport indique **178 signaux soumis à l'atelier**, **environ vingt participants**, **dix sujets retenus** et **sept entretiens** ultérieurs. Il décrit les dates de collecte et les catégories qui se recoupent. Ces nombres caractérisent la **méthode du projet**, et non le nombre de technologies effectivement adoptées par la police ou par des organisations criminelles. Il présente des cas techniques, prototypes et exemples d'usage dont les degrés de vérification sont inégaux (p. 14-16, 26-39).

### Opinions ou positions de l'auteur

Les auteurs estiment que les PET doivent être promues pour renforcer la sécurité des données, tout en demandant aux autorités d'accroître leur capacité à obtenir légalement des preuves. Ils proposent de financer les compétences, outils communs et coopérations, et parlent de technologies « à double usage ». L'intérêt des forces de l'ordre structure la sélection et l'interprétation des signaux ; les risques criminels des technologies les plus nouvelles sont souvent formulés au conditionnel (p. 5, 9-10, 26, 65-69).

### Interprétations et inférences

La lecture de cette analyse est que **la gouvernance des calculs et des résultats** deviendra aussi importante que le contrôle d'accès aux fichiers. Un dispositif peut cacher les entrées tout en révélant trop d'information par des requêtes répétées, un modèle ou des métadonnées. Cette inférence s'appuie sur les fonctions techniques et les réserves évoquées par le rapport ; celui-ci ne démontre pas que l'on peut déjà déployer une solution unique conciliant tous les cas d'enquête, la confidentialité et les exigences du procès (p. 20-23, 30-31, 39-42).

## Limites et points à vérifier

Ces réserves portent sur **la force des preuves et la portée des recommandations**, sans effacer l'intérêt des pistes de recherche.

1. **Petit exercice qualitatif.** Environ vingt personnes ont participé à un atelier et sept ont été interrogées. Le rapport ne donne pas un échantillon représentatif de tous les usages policiers, criminels ou civils, ni de mesure reproductible de la priorité attribuée à chaque signal (p. 5, 14-16, 65).
2. **Catégorie volontairement élargie.** Drones solaires, robots humanoïdes, 6G et « fondements de l'IA » ne sont pas tous des PET au sens technique courant. Leur inclusion sert la prospective autour de l'identité et de la surveillance, mais brouille une comparaison directe avec les taxonomies de l'OCDE ou de l'ICO (p. 20-21, 26-27, 31-39).
3. **Maturités mélangées.** Le texte rapproche systèmes déployés, recherches, prototypes et scénarios de long terme. Il ne fournit pas pour chacun une démonstration équivalente de faisabilité, de sécurité, de coût ou de diffusion, et ses échéances technologiques demeurent incertaines (p. 23, 31-39, 38-55).
4. **Absence de validation commune.** Les perspectives de détection de deepfakes, de partage sécurisé de données, de police prédictive et de calcul chiffré ne sont pas évaluées sur un même protocole, avec taux d'erreur, cas d'échec et contrôle indépendant (p. 27-35, 39-46).
5. **Scénarios criminels hypothétiques.** L'emploi possible de FHE dans un rançongiciel, de TEE pour cacher des marchés ou de robots humanoïdes pour saboter des opérations n'est pas présenté comme une prévalence constatée. Le suivre exige des incidents documentés, pas seulement la possibilité technique (p. 35-37, 41, 67-68).
6. **Promesses absolues à nuancer.** Certaines formulations sur l'anonymat d'une messagerie ou l'impossibilité d'écouter une liaison quantique dépendent de l'implémentation, du terminal et du modèle de menace. Le rapport ne démontre pas ces garanties de bout en bout (p. 28, 48-49).
7. **Accès légal peu spécifié.** Le texte appelle à améliorer l'accès aux données et parfois à une interception adaptée, sans proposer une architecture complète d'autorisation, de contrôle indépendant, de minimisation, de traçabilité et de recours pour chaque technique (p. 24-25, 40-42, 64-69).
8. **Évaluation des coûts insuffisante.** Le coût de calcul, les compétences, la consommation d'énergie et les matières premières sont évoqués, mais aucune comparaison chiffrée ne permet de classer les investissements publics proposés par gain net ou coût social (p. 23, 39-40, 56-64, 68-69).

## Sources et références mentionnées

Le rapport s'appuie sur des travaux de l'**OCDE** sur les PET, de la **Royal Society** sur la collaboration autour des données, de l'**ONU** sur les statistiques, de l'**ENISA** et de l'**ICO** sur les catégories et usages, ainsi que sur des textes de l'UE relatifs aux données, à l'IA, aux preuves électroniques et à la sécurité. Il cite l'**EU-SOCTA 2025**, l'**IOCTA 2025**, des publications scientifiques, des brevets, des projets et des articles technologiques. Cette bibliographie nourrit le repérage des signaux ; les commentaires des participants et des sept personnes interrogées sont volontairement non attribués individuellement, ce qui limite la possibilité de pondérer chaque avis (p. 4, 14-16, 70 et suiv.).

## Cinq éléments essentiels à retenir

1. **JRC et Europol publient une prospective**, bâtie sur 178 signaux discutés en atelier et sept entretiens, et non un classement statistique des technologies adoptées (p. 14-16).
2. **Le calcul protégé est la piste centrale :** FHE, MPC, FL, ZKP et TEE peuvent permettre des analyses communes avec moins d'exposition des données brutes, selon leurs limites propres (p. 20-23, 30-31, 35, 39-41).
3. **Les dix sujets retenus débordent les PET classiques :** deepfakes, biométrie, drones, robots et comportement sont inclus pour leurs effets possibles sur identité, preuve et surveillance (p. 26-37).
4. **Chiffrer un contenu ne résout pas tout :** métadonnées, sorties de calcul, erreurs de modèles et sécurité des terminaux restent des points décisifs pour la confidentialité et l'enquête (p. 30-31, 40-42).
5. **Les recommandations sont provisoires :** financement, formation et accès légal demandent des cas d'usage, des garanties et des mesures d'efficacité que l'exercice ne fournit pas encore (p. 5, 65-69).

## État de l'art et regards extérieurs

Recherches effectuées le 2026-10-08. Les éléments ci-dessous situent et vérifient le rapport ; ils ne changent pas rétroactivement les sections fondées sur son seul contenu.

### Travaux de référence

- **Protéger les données sans perdre leur utilité.** L'[OCDE — « Emerging privacy-enhancing technologies » (8 mars 2023)](https://www.oecd.org/en/publications/emerging-privacy-enhancing-technologies_bf121be4-en.html) définit les PET à partir des traitements et partages de données qu'elles rendent possibles avec moins d'exposition. Elle rappelle qu'elles complètent des règles de gouvernance et ne suffisent pas à assurer, seules, la conformité ou l'absence de fuite. C'est un cadre plus resserré que la sélection JRC-Europol incluant drones et robots.
- **Le partenariat, au-delà du chiffrement.** La [Royal Society — « From privacy to partnership » (23 janvier 2023)](https://royalsociety.org/-/media/policy/projects/privacy-enhancing-technologies/from-privacy-to-partnership.pdf) situe les PET dans la conception de collaborations entre détenteurs de données. Son point utile ici est que protéger une entrée ne décide ni de la finalité du traitement, ni de l'usage des sorties, ni de la répartition du pouvoir entre partenaires. Ce texte est un rapport de politique scientifique, pas une validation opérationnelle de chacune des techniques citées par JRC-Europol.
- **Le point de départ institutionnel.** La [notice officielle du JRC — « Horizon scanning on emerging privacy enhancement technologies » (8 septembre 2026)](https://publications.jrc.ec.europa.eu/repository/handle/JRC143326) confirme les cinq auteurs, le DOI **10.2760/6084454** et la date de publication que le PDF ne donne qu'à l'année. La [présentation du JRC (8 septembre 2026)](https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/how-emerging-privacy-technologies-could-reshape-law-enforcement-2026-09-08_en) décrit explicitement des « pistes de réflexion » pour les décideurs.

### Compléments sur le sujet

Quatre questions de mise en œuvre complètent utilement la carte des signaux du rapport : **choisir une architecture, vérifier les fuites, préparer la migration cryptographique et définir qui autorise les analyses**.

**Choisir selon le cas d'usage.** L'[ICO britannique — « Tackling barriers to PETs adoption » (atelier du 20 février 2024)](https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tackling-barriers-to-privacy-enhancing-technologies-adoption/) relève des freins concrets : vocabulaire instable, peu de cas démonstratifs, pénurie de compétences, coûts mal connus et incertitude sur le statut juridique des données traitées. Le [gouvernement britannique et l'ICO — outil de comparaison coûts-bénéfices (7 novembre 2024)](https://www.gov.uk/government/publications/privacy-enhancing-technologies-cost-benefit-awareness-tool/cost-benefit-awareness-tool) prennent l'apprentissage fédéré comme scénario et distinguent protection des entrées, protection des sorties, coûts d'infrastructure et utilité du modèle. Ils soulignent que le calcul économique dépend du cas d'usage et ne donnent pas de rendement universel aux PET.

**Tester les fuites à chaque étape.** Le [Contrôleur européen de la protection des données — *TechDispatch* sur l'apprentissage fédéré (10 juin 2025)](https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-06-10-techdispatch-12025-federated-learning_en) indique que les données restent locales, mais que des informations personnelles peuvent persister dans les mises à jour, les gradients ou le modèle final. La reconstruction est difficile et dépend de l'architecture, donc il faut évaluer le risque dans **chaque configuration**, y compris sur les terminaux participants. L'[avis 28/2024 du Comité européen de la protection des données (18 décembre 2024)](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en) ajoute qu'un modèle d'IA n'est pas présumé anonyme : l'extraction et l'identification indirecte doivent être évaluées. Cela précise la différence entre « ne pas déplacer les données brutes » et « ne divulguer aucune donnée personnelle ».

**Séparer PQC et QKD.** Le [NIST — approbation des normes FIPS 203, 204 et 205 (13 août 2024)](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved) confirme que la **cryptographie post-quantique** dispose déjà de normes finalisées pour l'établissement de clés et les signatures ; le sujet opérationnel est désormais aussi celui de la migration des systèmes. À l'inverse, la [spécification ETSI sur les preuves de sécurité QKD (décembre 2010)](https://www.etsi.org/deliver/etsi_gs/qkd/001_099/005/01.01.01_60/gs_qkd005v010101p.pdf) distingue la sécurité du protocole idéal de celle du système réel : la moindre hypothèse d'implémentation violée peut ruiner la garantie. La QKD requiert donc une évaluation de matériel, d'authentification et de réseau ; elle ne remplace pas automatiquement une migration PQC.

**Régir l'accès et les résultats.** Le [rapport de la Royal Society (23 janvier 2023)](https://royalsociety.org/-/media/policy/projects/privacy-enhancing-technologies/from-privacy-to-partnership.pdf) note qu'une PET peut permettre une analyse sans trancher si cette analyse est souhaitable. Appliqué à la police, cela déplace l'attention vers la finalité, les personnes autorisées, la minimisation des requêtes, la possibilité d'auditer les résultats et les recours. Le [guide britannique coûts-bénéfices (7 novembre 2024)](https://www.gov.uk/government/publications/privacy-enhancing-technologies-cost-benefit-awareness-tool/cost-benefit-awareness-tool) montre précisément pourquoi une combinaison FL + MPC + confidentialité différentielle peut être préférable à un outil unique dans certains cas, au prix de contraintes supplémentaires de calcul et d'utilité.

### Vérification des affirmations de la source

Les vérifications portent aussi sur les **unités et le statut** des affirmations : un constat de méthode, une estimation institutionnelle et une promesse de sécurité ne constituent pas la même preuve.

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| Le rapport est publié en 2026 et rassemble dix sujets jugés importants pour l'enquête (p. 5-6). | **Confirmé.** Date précise : **8 septembre 2026** ; les dix sujets proviennent d'un exercice de prospective. | [Notice JRC (8 septembre 2026)](https://publications.jrc.ec.europa.eu/repository/handle/JRC143326) et [communiqué JRC (8 septembre 2026)](https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/how-emerging-privacy-technologies-could-reshape-law-enforcement-2026-09-08_en). |
| 178 signaux soumis à l'atelier, environ vingt participants et sept entretiens (p. 15-16). | **Non établi indépendamment.** Le communiqué confirme « près de 200 » signaux et dix sujets ; il ne publie pas les données de délibération ni de score pour refaire la sélection. | [JRC (8 septembre 2026)](https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/how-emerging-privacy-technologies-could-reshape-law-enforcement-2026-09-08_en) ; détail interne du [rapport original (2026)](https://publications.jrc.ec.europa.eu/repository/handle/JRC143326). |
| Environ 85 % des enquêtes pénales mobilisent des données numériques (p. 24, 64). | **Nuancé.** Ce chiffre circule dans les textes de l'UE et remonte à une estimation utilisée pour la réforme des preuves électroniques ; il ne mesure ni le taux de demandes refusées ni la situation de 2026 par une nouvelle enquête représentative. | [Commission européenne — évaluation de la réforme (2018)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=SWD%3A2018%3A118%3AFIN) et [synthèse EUR-Lex sur les preuves électroniques (consultée le 8 octobre 2026)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=LEGISSUM%3A4682020). |
| L'apprentissage fédéré protège les données parce qu'elles restent chez leurs détenteurs (p. 30-31, 43). | **Nuancé.** Il réduit le transfert des données brutes ; les mises à jour et le modèle peuvent encore divulguer des informations. | [EDPS — *TechDispatch* (10 juin 2025)](https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-06-10-techdispatch-12025-federated-learning_en). |
| Des normes post-quantiques existent déjà (p. 38, 52). | **Confirmé.** FIPS 203, 204 et 205 ont été finalisées en août 2024 ; leur existence ne signifie pas que tous les systèmes ont migré. | [NIST (13 août 2024)](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved). |
| Une liaison QKD empêcherait « toute » écoute si des criminels l'installaient (p. 49). | **Nuancé.** La sécurité du protocole dépend des hypothèses et de l'implémentation ; l'ETSI exige une évaluation des systèmes réels. | [ETSI — GS QKD 005 (décembre 2010)](https://www.etsi.org/deliver/etsi_gs/qkd/001_099/005/01.01.01_60/gs_qkd005v010101p.pdf). |
| La note 11 renvoie à l'article 26 du RGPD comme à des règles spéciales de coopération policière (p. 45). | **Contredit.** L'article 26 du RGPD règle la **responsabilité conjointe des responsables de traitement** ; le cadre propre aux traitements policiers des États membres est notamment la directive 2016/680. L'article 23 du RGPD, cité dans la même note, traite de restrictions législatives à certains droits sous conditions, pas d'une dérogation générale. | [RGPD — articles 23 et 26 (27 avril 2016)](https://eur-lex.europa.eu/eli/reg/2016/679/ojv) ; [directive 2016/680 (27 avril 2016)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016L0680). |

### Contrepoints et critiques

- **La protection technique ne règle pas la finalité.** L'[OCDE (8 mars 2023)](https://www.oecd.org/en/publications/emerging-privacy-enhancing-technologies_bf121be4-en.html) et la [Royal Society (23 janvier 2023)](https://royalsociety.org/-/media/policy/projects/privacy-enhancing-technologies/from-privacy-to-partnership.pdf) soulignent qu'une PET ne remplace pas la gouvernance des données. Leur point est particulièrement fort pour les scénarios de profilage ou d'identification par IA : un calcul peut protéger les fichiers bruts tout en produisant une conclusion intrusive ou erronée sur une personne.
- **La sécurité ne découle pas de la seule architecture.** L'[EDPS (10 juin 2025)](https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-06-10-techdispatch-12025-federated-learning_en) exige une analyse des fuites des modèles fédérés ; l'[ETSI (décembre 2010)](https://www.etsi.org/deliver/etsi_gs/qkd/001_099/005/01.01.01_60/gs_qkd005v010101p.pdf) distingue preuve théorique et matériel quantique réel. Ces sources invitent à tester des implémentations et modèles de menace précis avant de reprendre les promesses d'« anonymat total » ou d'« impossibilité » d'interception.
- **La perspective policière n'épuise pas le débat.** Le rapport valorise l'accès légal à plus de preuves et reconnaît les droits fondamentaux, sans concevoir un dispositif universellement sûr pour obtenir des contenus chiffrés. La [directive 2016/680 (27 avril 2016)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016L0680) impose un cadre au traitement policier des données personnelles ; l'intérêt d'une analyse chiffrée doit être évalué avec nécessité, proportionnalité et contrôle de la finalité, et non à partir de sa seule faisabilité technique.

### Évolutions depuis la publication

Le rapport a été rendu public le **8 septembre 2026**. Deux publications institutionnelles ultérieures éclairent sa réception sans établir que les solutions envisagées sont maintenant déployées.

- **24 septembre 2026 :** le [compte rendu de la conférence EDEN d'Europol](https://www.europol.europa.eu/media-press/newsroom/news/protecting-citizens-preserving-rights) rapporte des discussions entre policiers, autorités de protection des données et universitaires sur le cloud, l'IA et la preuve numérique. L'accent y est mis sur nécessité, proportionnalité, sécurité et crédibilité des preuves ; il ne s'agit pas d'une évaluation indépendante des dix signaux du rapport.
- **7 octobre 2026 :** [Europol et l'université Carlos III de Madrid — « Harvest now, decrypt later »](https://www.europol.europa.eu/publications-events/publications/harvest-now-decrypt-later) approfondissent le risque de collecte présente de données chiffrées en vue d'un déchiffrement futur. Cette publication renforce la priorité de **préparer la migration post-quantique** ; elle ne date pas avec certitude l'arrivée d'un ordinateur capable de casser les systèmes actuels.

### Cadre juridique et éthique

- **Données utilisées par les services répressifs.** La [directive (UE) 2016/680 du 27 avril 2016](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016L0680) encadre les traitements de données personnelles par les autorités compétentes des États membres à des fins pénales. Une PET peut réduire l'exposition technique, mais elle ne fournit pas automatiquement une base légale au traitement ou à une requête sur des données de tiers.
- **Biométrie et IA.** Le [règlement (UE) 2024/1689 sur l'IA, texte consolidé consulté le 8 octobre 2026](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32024R1689) encadre strictement l'identification biométrique à distance « en temps réel » dans les espaces accessibles au public pour la police : cas limités, nécessité et proportionnalité, conditions nationales, évaluation des droits et autorisation préalable en principe. Ces règles précises ne sont pas une interdiction générale de toute biométrie ni une autorisation générale de surveillance.
- **Modèles et anonymat.** L'[avis 28/2024 du Comité européen de la protection des données (18 décembre 2024)](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en) demande une appréciation au cas par cas avant de qualifier d'anonyme un modèle entraîné sur des données personnelles. Cela s'applique aux sorties et aux risques de reconstruction que le rapport JRC-Europol évoque pour les données synthétiques et l'apprentissage fédéré.
- **Trafic et localisation.** La [CJUE — affaire C-140/20, résumé du 5 avril 2022](https://curia.europa.eu/jcms/upload/docs/application/pdf/2022-04/cp220058en.pdf) exclut une conservation générale et indifférenciée de ces données pour la seule lutte contre la criminalité grave, tout en admettant sous conditions des mesures ciblées et certaines autres catégories de conservation. L'appel du rapport à mieux exploiter les métadonnées doit se lire dans ce cadre, sans présumer que toutes ces données sont librement accessibles.

### Pour aller plus loin

- [JRC — notice officielle du rapport (8 septembre 2026)](https://publications.jrc.ec.europa.eu/repository/handle/JRC143326) : accéder au document institutionnel, à ses auteurs et au DOI.
- [OCDE — « Emerging privacy-enhancing technologies » (8 mars 2023)](https://www.oecd.org/en/publications/emerging-privacy-enhancing-technologies_bf121be4-en.html) : comparer les familles de PET et leurs obstacles réglementaires.
- [EDPS — *TechDispatch* sur l'apprentissage fédéré (10 juin 2025)](https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-06-10-techdispatch-12025-federated-learning_en) : examiner les fuites possibles par gradients et modèles.
- [Gouvernement britannique et ICO — outil coûts-bénéfices (7 novembre 2024)](https://www.gov.uk/government/publications/privacy-enhancing-technologies-cost-benefit-awareness-tool/cost-benefit-awareness-tool) : cadrer un pilote concret en séparant données d'entrée, résultats, coût et utilité.
- [NIST — normes post-quantiques FIPS 203 à 205 (13 août 2024)](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved) : distinguer normalisation cryptographique et migration réelle.
