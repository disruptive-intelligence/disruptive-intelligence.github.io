---
title: Chapitre 8 — Cadre réglementaire et normatif applicable
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

> ⏱ **Chapitre entièrement périssable.** Toutes les données de ce chapitre ont été vérifiées le **30 juillet 2026**. Le raisonnement, la méthode de lecture et la matrice du §8.8 restent valables ; les statuts, dates et échéances doivent être revérifiés à chaque revue du cours. Les déclencheurs de revue anticipée figurent en tête du document.

Ce chapitre n'a pas vocation à faire de vous un juriste. Il répond à trois questions pratiques : **qu'est-ce qui m'oblige, à quoi exactement, et quelle preuve devrai-je produire ?** La grille de lecture exigence / objectif / moyen du §5.4 s'applique de bout en bout.

## 8.1 NIS2 et la transposition française

**Ce dont il s'agit.** La directive européenne dite NIS2 élargit considérablement le périmètre des organisations soumises à des obligations de cybersécurité, par rapport au dispositif précédent. Elle introduit deux catégories — **entités essentielles** et **entités importantes** — définies par secteur d'activité et par taille, avec des régimes de contrôle différents : supervision *a priori* pour les premières, contrôle *a posteriori* sur signalement pour les secondes. Les sanctions prévues sont significatives et la responsabilité des dirigeants est explicitement engagée.

Pour une entreprise privée, les obligations opérationnelles sont principalement mises en œuvre par le droit national de transposition. Le statut exact et les effets d'une directive non transposée dans les délais doivent être vérifiés dans chaque juridiction concernée — ce cours retient la lecture pratique : tant que le texte national n'est pas publié, les obligations opposables restent celles du droit existant.

⏱ **ÉTAT DE L'ART — le statut en France au 30/07/2026**
Le véhicule législatif français de transposition — le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, couramment appelé « loi Résilience » — **n'était pas promulgué** à cette date ; le dossier législatif restait ouvert. Le calendrier de transposition européen était donc largement dépassé.
📎 [S-01] [S-02] — directive et dossier législatif public, consultés le 30/07/2026.

**Ce que cela change pour votre programme de MCS — et c'est le point important du chapitre.** L'absence de texte national applicable ne suspend rien, pour trois raisons :

1. Les délais de mise en conformité, une fois le texte publié, sont courts au regard du temps nécessaire pour construire un inventaire fiable et une propriété d'actif. Une organisation qui attend le texte pour commencer aura déjà perdu.
2. Vos **clients** vous imposeront des exigences avant le régulateur. Une entité soumise doit maîtriser sa chaîne de sous-traitance : les questionnaires arrivent donc en amont de la loi, et ils arrivent déjà.
3. Les mesures attendues sont, dans leur substance, celles que ce cours décrit — inventaire, gestion des vulnérabilités, gestion des correctifs, maîtrise de la chaîne d'approvisionnement, gestion des incidents. Elles sont utiles indépendamment du texte qui les rendra obligatoires.

✅ **BONNE PRATIQUE (P0)** — Traitez l'incertitude réglementaire comme une **donnée de pilotage**, pas comme un motif d'attente. Concrètement : construisez le dispositif sur la base du projet de référentiel disponible (§8.2), documentez vos choix de calibrage, et prévoyez une revue d'écart à la publication du texte définitif. C'est exactement la position tenable devant un comité de direction qui demande « faut-il attendre ? ».

## 8.2 Le ReCyF : le référentiel d'application

**Ce dont il s'agit.** Un texte de loi énonce des exigences générales. Il faut un référentiel intermédiaire pour traduire ces exigences en objectifs de sécurité vérifiables. C'est le rôle du ReCyF — référentiel d'exigences de cybersécurité destiné aux entités françaises concernées — élaboré par l'ANSSI.

**Sa structure, et pourquoi elle est bien conçue.** Le référentiel s'organise en une vingtaine d'**objectifs de sécurité**, chacun décliné en exigences, avec pour chacune :

- une **modulation selon la catégorie** de l'entité (essentielle ou importante) ;
- des **moyens acceptables de conformité**, c'est-à-dire des exemples de mise en œuvre reconnus — sans être les seuls admis ;
- l'application du principe de **proportionnalité** : les mesures attendues tiennent compte de la taille, de l'exposition et de la criticité de l'activité.

Cette structure est exactement la grille du §5.4, et elle vous laisse une liberté de mise en œuvre que beaucoup d'organisations n'exploitent pas — à condition de savoir **justifier** son calibrage, donc de l'avoir écrit.

**Ce qui touche directement le MCS.** Sans citer un découpage qui évoluera, les familles d'objectifs qui concernent ce cours sont : la connaissance et la maîtrise du patrimoine informationnel (inventaire, cartographie), la gestion des vulnérabilités et des mises à jour, la maîtrise des configurations, la gestion des accès et des comptes à privilèges, la maîtrise de la sous-traitance, la journalisation et la détection, la gestion des incidents, et la continuité.

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — Le ReCyF était diffusé en **version de travail**, la dernière datant du **17 mars 2026**. Un document portant explicitement cette mention n'a pas de valeur opposable : il indique la direction, pas l'obligation.
📎 [S-03] — publication de l'agence, consultée le 30/07/2026. Les numéros d'objectifs cités dans ce cours devront être revérifiés contre la version définitive.

✅ **BONNE PRATIQUE (P1) — l'analyse d'écart anticipée**
Menez dès maintenant une analyse d'écart objectif par objectif, avec trois colonnes : *ce que nous faisons* · *ce que l'objectif attend* · *effort estimé*. Deux bénéfices immédiats, indépendants du calendrier réglementaire : vous obtenez une feuille de route priorisée, et vous disposez d'un document à présenter à un client ou à un assureur qui demande où vous en êtes.

## 8.3 Le Cyber Resilience Act : la réglementation passe au produit

**Le changement de nature.** Toutes les réglementations précédentes s'adressent à l'organisation qui **exploite** un système d'information. Le règlement européen sur la cyberrésilience s'adresse à celui qui **met un produit sur le marché**. C'est un déplacement majeur : il crée des obligations de MCS pour les fabricants et éditeurs, sur des produits installés chez leurs clients.

**Le calendrier par paliers.**

| Étape | Date | Portée |
|---|---|---|
| Entrée en vigueur | 10 décembre 2024 | Le règlement existe, l'essentiel des obligations est différé |
| Chapitre relatif aux organismes d'évaluation de la conformité | 11 juin 2026 | Mise en place du dispositif d'évaluation |
| **Obligations de signalement** | **À compter du 11 septembre 2026** | Vulnérabilités activement exploitées et incidents graves |
| Application générale | 11 décembre 2027 | Exigences essentielles de sécurité, marquage, documentation |

**Les délais de signalement, formulés précisément** — c'est le point le plus souvent mal restitué :

| Échéance | Contenu | Point de départ |
|---|---|---|
| **≤ 24 h** | Alerte précoce | Prise de connaissance |
| **≤ 72 h** | Notification, avec les éléments connus et les mesures correctives ou d'atténuation | Prise de connaissance |
| **≤ 14 jours** | Rapport final, pour une **vulnérabilité activement exploitée** | **La mise à disposition d'une mesure corrective ou d'atténuation** — et non la découverte |
| **≤ 1 mois** | Rapport final, pour un **incident grave** | La notification initiale |

Le signalement s'effectue via une plateforme unique de déclaration au niveau européen, avec routage vers le CSIRT compétent.

⚠️ **PIÈGE — croire qu'il s'agit d'une obligation de paperasse**
Un délai de 24 heures pour l'alerte précoce n'est pas un problème de formulaire : c'est une **exigence de capacité organisationnelle**. Pour le tenir, il faut être capable de détecter qu'une vulnérabilité de son produit est activement exploitée chez des clients, de qualifier le périmètre affecté rapidement, et de disposer d'une chaîne de décision pré-autorisée — y compris un week-end d'août. Cette capacité se construit en mois, pas en jours. Le chapitre 33 en fait un module complet.

**Les exclusions de périmètre, et la méthode.** Certains produits sont exclus parce qu'ils relèvent d'un autre régime européen qui leur est propre : c'est notamment le cas des dispositifs médicaux couverts par la réglementation qui leur est applicable, et de plusieurs autres secteurs réglementés.

⚠️ La conséquence pratique est contre-intuitive et coûte cher aux organisations qui la manquent : **l'exclusion ne s'analyse pas par gamme commerciale, mais produit par produit**. Une même entreprise peut commercialiser un dispositif exclu, une passerelle incluse et une application mobile incluse. Et exclusion ne signifie pas absence d'exigences : le régime alternatif comporte ses propres obligations de cybersécurité. La grille d'analyse figure au §33.8.

## 8.4 ISO/IEC 27001 et 27002 : les mesures qui portent le MCS

**Ce dont il s'agit.** Une norme internationale de management de la sécurité de l'information, certifiable. Elle n'est obligatoire pour personne, mais elle est massivement demandée par les clients — ce qui la rend contraignante en pratique.

**Ce qui compte pour ce cours.** Quatre mesures de l'annexe portent directement le MCS :

| Mesure | Objet | Chapitre du cours |
|---|---|---|
| **8.8** — Gestion des vulnérabilités techniques | Obtenir l'information sur les vulnérabilités, évaluer l'exposition, prendre les mesures | Ch. 14 à 18 |
| **8.9** — Gestion des configurations | Définir, documenter, appliquer et surveiller les configurations | Ch. 22 et 23 |
| **8.19** — Installation de logiciels sur les systèmes en exploitation | Encadrer ce qui est installé et par qui | Ch. 22, 26 |
| **8.32** — Gestion des changements | Encadrer les modifications de l'environnement de traitement | Ch. 5, 18 |

📎 [S-10] — ISO/IEC 27001:2022 annexe A et ISO/IEC 27002:2022.

**Ce qu'un auditeur regarde réellement**, sur ces quatre mesures : l'existence d'un processus documenté, la **preuve de son application** sur un échantillon d'actifs, la cohérence entre le périmètre déclaré et le périmètre mesuré, le traitement des exceptions, et la revue de direction. C'est-à-dire, très exactement, les livrables décrits aux chapitres 38 et 39.

📌 **LIMITES** — Une certification atteste qu'un système de management existe et fonctionne. Elle n'atteste pas que votre parc est à jour. Une organisation certifiée peut porter des actifs hors support, dès lors que c'est identifié, tracé, décidé et revu — mais un niveau élevé peut constituer une non-conformité selon le périmètre certifié, le traitement du risque retenu et l'efficacité démontrée des mesures. Ne confondez jamais certification et niveau de sécurité — et ne laissez personne le faire dans votre organisation.

## 8.5 Le paysage sectoriel

Selon votre activité, d'autres textes s'ajoutent. Voici ce que chacun exige **spécifiquement** en matière de maintien.

| Cadre | Qui est concerné | Ce qu'il exige en propre pour le MCS |
|---|---|---|
| **Série IEC 62443** | Systèmes d'automatisation industriels : exploitants, intégrateurs, fabricants | Une gestion des correctifs adaptée au contexte industriel, la définition de zones et de conduits, et — côté fabricant — un cycle de développement sécurisé incluant la gestion des mises à jour de sécurité. Chapitre 29 |
| **Hébergement de données de santé** | Hébergeurs de données de santé à caractère personnel, et leurs clients par ricochet | Certification de l'hébergeur, exigences de maintien et de traçabilité, obligations contractuelles vers le client |
| **Qualification SecNumCloud** | Fournisseurs de services cloud visant les usages sensibles | Exigences détaillées de maintien en condition de sécurité, de gestion des vulnérabilités et de transparence vers le client |
| **PCI DSS** | Traitement de données de cartes de paiement | Le plus **prescriptif** de tous : délais chiffrés d'application des correctifs critiques, exigences de scan périodique interne et externe, exigences de gestion des changements |
| **DORA** | Secteur financier européen | Gestion du risque informatique, dont l'identification et le traitement des vulnérabilités, les tests, et la maîtrise renforcée des prestataires tiers critiques |

**L'enseignement transversal.** Ces cadres divergent sur la forme et convergent sur le fond : connaître son parc, détecter les vulnérabilités, les traiter selon des délais définis, tracer les exceptions, et prouver. Si vous construisez un dispositif solide, l'adaptation à un cadre supplémentaire relève surtout de la mise en forme documentaire. C'est le meilleur argument contre la construction d'un dispositif par référentiel.

## 8.6 Le règlement général sur la protection des données

Souvent oublié dans les discussions de MCS, alors qu'il est le texte le plus universellement applicable.

Son article relatif à la sécurité du traitement impose des mesures techniques et organisationnelles appropriées au risque, en tenant compte de l'état de l'art. Les autorités de contrôle ont retenu à plusieurs reprises, dans des décisions publiées, qu'un **défaut de mise à jour d'un composant présentant une vulnérabilité connue et corrigée** pouvait caractériser un manquement, dès lors que ce défaut avait contribué à une violation de données. Chaque décision s'apprécie au cas d'espèce ; il convient de se référer aux délibérations publiées de l'autorité compétente plutôt qu'à une règle générale.

⚖️ **CADRE — ce qu'il faut en retenir opérationnellement**
Trois éléments sont regardés en cas de contrôle après incident : la vulnérabilité était-elle **connue et corrigée** au moment des faits ; l'organisation disposait-elle d'un **processus** permettant de la traiter ; et l'écart était-il **identifié et décidé**, ou simplement ignoré ? Une dérogation formalisée et compensée place l'organisation dans une position radicalement différente d'une absence totale de trace. C'est un argument de plus, et le plus concret, en faveur du §7.4.

## 8.7 Un modèle méthodologique utile — et ses limites d'applicabilité

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — L'agence américaine de cybersécurité a publié le **10 juin 2026** une directive opérationnelle contraignante (référencée BOD 26-04) organisant la priorisation des mises à jour de sécurité **par le risque** plutôt que par la seule gravité technique : prise en compte de l'exploitation observée, de l'exposition à Internet, et application d'une méthode par arbre de décision, avec des délais de remédiation différenciés.

⚠️ **Portée juridique — à ne jamais confondre.** Ce type de directive est **contraignant uniquement pour les agences civiles fédérales américaines**. Elle ne crée **aucune obligation** pour une organisation française ou européenne, publique ou privée.

📎 [S-21]

**Pourquoi elle figure malgré tout dans ce cours.** Parce qu'elle constitue un **modèle méthodologique documenté et public**, produit par une autorité qui gère un parc considérable, et qu'elle valide la même orientation que celle enseignée au chapitre 16 : la gravité technique seule ne suffit plus à prioriser. Vous pouvez vous en inspirer pour calibrer vos propres délais et défendre votre méthode — en citant une référence publique plutôt qu'une intuition. Vous ne pouvez pas vous en réclamer comme d'une obligation.

## 8.8 ⚖️ Matrice « exigence → objectif → preuve attendue »

C'est le livrable de ce chapitre. Il fonctionne quel que soit le référentiel qui vous est opposé.

| Exigence type | Objectif de sécurité correspondant | Preuve à constituer |
|---|---|---|
| Connaître son patrimoine | Inventaire exhaustif, à jour, avec propriétaires | Périmètre de référence daté, sources réconciliées, écarts expliqués, taux de complétude (ch. 10) |
| Identifier les vulnérabilités | Détection périodique sur l'ensemble du périmètre | Rapports datés, couverture calculée et prouvée, liste des actifs non scannés (ch. 15) |
| Traiter en temps utile | Délais définis par criticité et tenus | Politique avec classes de service, mesure du respect des délais, historique (ch. 7, 38) |
| Gérer les exceptions | Décisions formalisées, bornées, compensées | Registre des dérogations avec signataires, dates, compensations, revues (ch. 7, 20) |
| Maîtriser les configurations | Référentiel de configuration appliqué et contrôlé | Baseline versionnée, résultats de contrôle, traitement des écarts (ch. 22) |
| Maîtriser la sous-traitance | Exigences contractuelles et vérification | Clauses, rapports du prestataire, contrôles réalisés (ch. 13) |
| Gérer les incidents | Procédure et capacité de réaction | Journal de crise, chronologies, retours d'expérience (ch. 21) |
| Piloter | Indicateurs suivis et revus par la direction | Tableaux de bord historisés, comptes rendus de comité avec décisions (ch. 38, 39) |

✅ **BONNE PRATIQUE (P0)** — Constituez le dossier de preuves **une fois**, dans cette structure, puis projetez-le sur chaque référentiel qui vous est opposé. L'erreur classique consiste à construire un dossier par certification, par client et par audit : vous multipliez la charge par le nombre d'interlocuteurs, et vous produisez des versions divergentes des mêmes faits.

## 8.9 📌 Limites : la conformité n'est pas la sécurité

Trois avertissements, à garder présents chaque fois que ce chapitre sert d'argument.

**Aucun texte ne dit comment faire.** Ils fixent des résultats. Le savoir-faire — quels outils, quelle cadence, quelle méthode de triage, quel anneau de déploiement — est le sujet des chapitres 14 à 23, et il n'est écrit dans aucun référentiel.

**La conformité est un plancher, pas un objectif.** Une organisation peut être parfaitement conforme et se faire compromettre le lendemain par un chemin que le référentiel n'adresse pas.

**La conformité peut détourner les moyens.** Le risque le plus concret est de consacrer l'essentiel du budget à la production documentaire au détriment de la remédiation. Un indicateur simple permet de le suivre : la part du temps de l'équipe consacrée à produire de la preuve, rapportée au temps consacré à corriger. Aucun seuil universel n'existe — mais une croissance continue de ce ratio, sans amélioration des indicateurs de résultat, mérite un examen.

## 8.10 🔴 FIL ROUGE — juin 2026 : l'analyse d'écart

Claire Nadeau conduit l'analyse d'écart d'HELIOMED contre le référentiel disponible, un mois après la publication de la politique MCS v1. Vingt objectifs passés en revue, quatre demi-journées de travail avec Sonia Weber et Malik Ferhaoui.

**Le résultat global est meilleur qu'attendu** — le travail d'inventaire et de propriété des mois précédents couvre à lui seul une part importante des attentes. Trois écarts concentrent l'essentiel de l'effort restant.

**Écart n° 1 — la maîtrise de la sous-traitance.** HELIOMED ne dispose d'aucune donnée sur l'état de mise à jour des 620 postes gérés par son infogérant, ni d'aucune clause lui permettant de l'exiger. C'est le trou déclaré de la politique v1 (§7.7), et le référentiel le range parmi les attentes les plus structurantes. Effort estimé : un avenant contractuel, et une négociation.

**Écart n° 2 — la journalisation.** Les journaux de l'usine de Saint-Étienne ne sont pas centralisés et sont conservés sept jours. En cas de suspicion de compromission d'un poste de supervision, il serait impossible de conclure — ce qui renvoie très exactement à la règle du §21.3 : l'absence de preuve de compromission n'est pas la preuve de l'absence de compromission.

**Écart n° 3 — la qualification produit.** Personne chez HELIOMED n'a encore déterminé lesquels de ses produits relèvent du règlement européen sur la cyberrésilience. L'échéance de signalement du 11 septembre est dans dix semaines.

C'est l'écart le plus urgent des trois, et il est traité comme tel : Yann Prigent et Hélène Fabre conduisent une **qualification de première intention en six semaines**, suffisante pour identifier les produits concernés et mettre en service un dispositif de signalement minimal — point de contact publié, chaîne de décision pré-autorisée, modèles de notification. Ce dispositif est opérationnel le 1er septembre 2026.

Il est **volontairement incomplet** : la qualification retient l'hypothèse la plus contraignante partout où le doute existe, le PSIRT se réduit à deux personnes et une procédure d'astreinte, et l'inventaire des versions déployées chez les clients n'existe pas. C'est un dispositif de conformité minimale assumée, pas un dispositif abouti.

La revue de maturité complète — qualification argumentée produit par produit, exercice à blanc, inventaire des versions clients — est planifiée pour 2028. Elle fait l'objet du **chapitre 33**.

**La décision qui structure la suite.** Plutôt que de traiter les vingt objectifs en parallèle, Claire propose de séquencer sur douze mois en fonction de deux critères : effort d'une part, effet sur le risque réel d'autre part. Trois objectifs sont traités au trimestre suivant, sept sont planifiés, et **deux sont explicitement reportés à 2027 avec une justification écrite**. Ce dernier point est celui que Pierre Vasseur retient : il ne demande pas que tout soit fait, il demande à savoir ce qui ne le sera pas.

**Livrable de l'épisode.** Une analyse d'écart de six pages, une feuille de route à douze mois, et deux reports assumés et datés. Le tout constituera le socle du dossier de preuves de janvier 2027.

→ La suite en 🔴 §9.7, quand il faut désigner qui arbitrera ces priorités mois après mois.

→ **Chapitre 9 — Gouvernance, rôles et comitologie** : qui arbitre, à quel rythme, avec quel mandat.

## Synthèse mentale du chapitre 8

Une directive européenne doit être transposée pour s'appliquer, et l'attente du texte national n'est jamais une stratégie : les clients exigent avant le régulateur, les délais de mise en conformité sont courts, et les mesures attendues sont utiles indépendamment du texte. Un référentiel d'application traduit les exigences en objectifs assortis de moyens acceptables de conformité et d'un principe de proportionnalité — ce qui vous laisse une liberté de calibrage, à condition de savoir la justifier par écrit. Le règlement sur la cyberrésilience déplace la réglementation de l'exploitant vers le fabricant, avec des délais de signalement qui sont d'abord une exigence de capacité organisationnelle, pas de formulaire, et des exclusions qui s'analysent produit par produit. Les normes et cadres sectoriels divergent sur la forme et convergent sur le fond : connaître, détecter, traiter dans des délais, tracer les exceptions, prouver. Une directive étrangère peut servir de modèle méthodologique sans jamais constituer une obligation. Enfin, la conformité est un plancher, et le temps consacré à produire de la preuve doit rester une fraction du temps consacré à corriger.

**Trois questions de vérification**

1. Votre direction demande s'il faut attendre la publication du texte national avant d'engager le programme. Donnez trois arguments qui ne reposent pas sur la crainte de la sanction.
2. Un client vous oppose une directive publiée par une autorité étrangère et exige que vous vous y conformiez. Comment répondez-vous sans être ni fermé ni juridiquement imprudent ?
3. Vous êtes certifié selon une norme de management de la sécurité et 40 % de votre parc est hors support. Est-ce compatible ? Qu'est-ce que cela vous apprend sur ce qu'une certification atteste ?

---
