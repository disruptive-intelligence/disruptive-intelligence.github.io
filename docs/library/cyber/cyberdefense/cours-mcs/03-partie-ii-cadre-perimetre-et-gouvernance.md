---
title: PARTIE II — Cadre, périmètre et gouvernance
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 3
chapters: 10
---

La Partie I a installé le socle : ce qu'est le MCS, comment fonctionnent les mécanismes techniques, quel vocabulaire décrit les vulnérabilités, quels processus encadrent le changement, et comment concevoir des systèmes qu'on puisse maintenir.

La Partie II répond à trois questions d'organisation : **sur quoi s'applique le MCS** (périmètre, inventaire, exposition, obsolescence), **qui décide** (doctrine, gouvernance), et **ce que l'extérieur exige** (cadre réglementaire, contrats de délégation).

---

## Chapitre 7 — Doctrine et politique MCS

### 7.1 Ce qui distingue une politique appliquée d'un document mort

La plupart des organisations ont déjà une politique de sécurité qui mentionne les correctifs. La plupart de ces mentions ne sont pas appliquées. La différence entre les deux situations ne tient pas à la qualité rédactionnelle, mais à trois propriétés très concrètes.

**Une politique appliquée est décidable.** Chaque phrase doit permettre de trancher un cas réel. « Les correctifs de sécurité sont appliqués dans les meilleurs délais » ne permet de trancher aucun cas : quel délai, sur quel actif, décidé par qui. À l'inverse, « les correctifs concernant une vulnérabilité exploitée sur un actif exposé à Internet sont appliqués sous 72 heures, y compris hors fenêtre, sur décision du propriétaire technique » se vérifie et s'oppose.

**Une politique appliquée est finançable.** Si elle impose un scan authentifié mensuel du parc alors qu'aucune licence ni aucun temps homme n'y sont affectés, elle organise sa propre violation. Une politique qui dépasse les moyens engagés génère une non-conformité permanente, ce qui est pire que l'absence de politique : cela habitue tout le monde à ce que la règle ne soit pas tenue.

**Une politique appliquée prévoit sa propre transgression.** C'est le point le plus contre-intuitif et le plus important. Il existera toujours des situations où corriger est impossible. Si la politique ne prévoit pas de chemin légitime pour ces cas — la dérogation du §7.4 — les équipes emprunteront un chemin illégitime : le silence.

**Structure recommandée.** Un document court, de huit à douze pages, en sept sections :

| Section | Contenu | Longueur indicative |
|---|---|---|
| 1. Objet et périmètre | Ce qui est couvert, ce qui ne l'est pas et pourquoi | ½ page |
| 2. Définitions | Vocabulaire arrêté, notamment actif, propriétaire, couverture, conformité | 1 page |
| 3. Rôles et responsabilités | Renvoi au RACI, décideurs nommés par catégorie | 1 page |
| 4. Classes de service | Le cœur du document (§7.2) | 2-3 pages |
| 5. Processus | Veille, détection, triage, correction, vérification, preuve | 2-3 pages |
| 6. Dérogations | Procédure, durée, signataires, revue (§7.4) | 1 page |
| 7. Mesure et contrôle | Indicateurs, fréquence, destinataires | 1 page |

⚠️ **PIÈGE — la politique qui liste des outils**
Une politique qui nomme des produits devient obsolète au premier changement d'outillage, et elle transforme un document de doctrine en documentation technique. Les outils vivent dans les procédures d'exploitation, qui se modifient sans passer par le circuit d'approbation de la politique.

### 7.2 Les classes de service : le cœur du dispositif

C'est la section qui rend une politique opérationnelle. L'idée : **on ne traite pas tous les actifs de la même façon**, et cette différenciation doit être écrite, pas improvisée.

**Construire les classes.** Trois à quatre classes suffisent — au-delà, plus personne ne sait dans laquelle ranger un actif. Le critère de classement combine deux dimensions : la **criticité métier** (que se passe-t-il si cet actif tombe ou fuit ?) et l'**exposition** (qui peut l'atteindre ?).

| Classe | Définition | Exemples typiques |
|---|---|---|
| **C1 — Critique exposé** | Actif de niveau 0, ou joignable depuis Internet, ou portant une donnée sensible | Passerelle d'accès distant, annuaire, hyperviseur, console de sauvegarde, service public |
| **C2 — Important** | Actif métier significatif, non exposé directement | Serveurs applicatifs internes, bases de données métier |
| **C3 — Courant** | Actif dont l'indisponibilité est tolérable | Postes de travail standard, serveurs de fichiers secondaires |
| **C4 — Contraint** | Actif que l'on ne peut pas corriger normalement | Systèmes industriels, legacy sous contrat figé, appliances fermées |

La classe C4 est indispensable et souvent oubliée. Sans elle, ces actifs sont classés dans une catégorie dont ils violeront en permanence les règles, ce qui pollue tous les indicateurs. Les nommer explicitement permet de leur appliquer un régime différent — compensation obligatoire plutôt que correction — et de mesurer honnêtement.

**Ce que chaque classe définit.** Pour chaque classe, six paramètres, et pas un de plus :

| Paramètre | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| Délai de correction — vulnérabilité exploitée | 72 h | 7 j | 30 j | Compensation sous 72 h |
| Délai de correction — critique non exploitée | 15 j | 30 j | 60 j | Compensation ou dérogation |
| Délai — reste | 30 j | 90 j | 180 j | Selon fenêtre constructeur |
| Fréquence de vérification | Hebdomadaire | Mensuelle | Mensuelle | Trimestrielle |
| Niveau de test avant déploiement | Recette + témoin | Témoin | Anneau pilote | Validation fournisseur |
| Fenêtre | Récurrente hebdomadaire + urgence autorisée | Mensuelle | Mensuelle | Arrêt planifié |

*Les valeurs ci-dessus sont un point de départ réaliste pour une organisation de taille intermédiaire, pas une norme. Ce qui compte n'est pas le chiffre, c'est qu'il soit **écrit, tenable et mesuré**.*

✅ **BONNE PRATIQUE (P0)** — Calibrez vos délais sur ce que vous pouvez réellement tenir, pas sur ce qui fait bien. Une politique annonçant 48 h que vous tenez trois fois par an vous met en position de non-conformité permanente devant un auditeur, un assureur ou un client. Une politique annonçant 15 jours et tenue à 92 % est infiniment plus solide — et vous pourrez la resserrer ensuite, ce qui est un progrès démontrable.

### 7.3 Le contrat interne entre sécurité et production

Le conflit MCO/MCS du §1.2 ne se résout pas par autorité. Il se résout par un engagement **réciproque**, formalisé dans la politique, et c'est la réciprocité qui le rend applicable.

**Ce que la sécurité s'engage à fournir :**

- un périmètre et une priorisation stables, pas une liste de 4 000 constats à trier soi-même ;
- un volume de demandes compatible avec les moyens de l'exploitation, avec un plafond mensuel assumé ;
- une qualification préalable de chaque demande urgente — exposition mesurée, exploitation vérifiée, pas de fausse alerte ;
- l'acceptation formelle du risque lorsqu'un report est décidé, portée par la sécurité et non par l'exploitant.

**Ce que la production s'engage à fournir :**

- des fenêtres récurrentes garanties, pas renégociées mensuellement ;
- l'application dans les délais définis par classe de service ;
- la remontée d'une preuve exploitable, pas une confirmation verbale ;
- l'alerte immédiate en cas d'impossibilité, plutôt que le silence — c'est la contrepartie de l'existence d'une procédure de dérogation.

Ce dernier point est le pivot. **Le silence est le pire résultat possible** : il produit un écart invisible, donc non compensé, donc non financé. Une organisation qui punit les remontées d'impossibilité fabrique mécaniquement son propre angle mort.

### 7.4 La procédure de dérogation

Une dérogation est une décision formelle de ne pas appliquer la règle, pour un actif, une vulnérabilité et une durée déterminés. Bien conçue, c'est un instrument de pilotage. Mal conçue, c'est une machine à dissimuler.

**Les sept champs obligatoires** — repris de la logique du §5.3 et développés au chapitre 20 :

| Champ | Pourquoi il est indispensable |
|---|---|
| Objet précis | Quel actif, quelle vulnérabilité, quel correctif — jamais « les serveurs de l'usine » |
| Motif | Technique, contractuel, métier, budgétaire — le motif oriente la solution |
| **Date d'expiration** | Une dérogation sans date est une renonciation |
| Mesure compensatoire | Obligatoire ; une dérogation nue n'est pas acceptable |
| Moyen de vérification | Comment saura-t-on que la compensation est toujours en place ? |
| Signataire | Le propriétaire métier, pas la sécurité — celui qui porte le risque le signe |
| Condition de sortie | Quel événement met fin à la dérogation |

⚠️ **PIÈGE — la dérogation renouvelée par défaut**
Le mécanisme de dégradation est toujours le même : la dérogation arrive à échéance, rien n'a changé, on reconduit. Trois ans plus tard, elle est devenue un état permanent que plus personne n'interroge.
**Le garde-fou qui fonctionne** : le renouvellement d'une dérogation exige une signature de **niveau supérieur** à la précédente. Le premier renouvellement remonte au directeur des systèmes d'information, le second à la direction générale. Le coût politique croissant force l'arbitrage — soit on corrige, soit on assume au bon niveau.

✅ **BONNE PRATIQUE (P1)** — Suivez l'**âge moyen des dérogations ouvertes** comme indicateur de premier plan (chapitre 38). C'est la mesure la plus honnête de la dette de sécurité réellement acceptée par l'organisation, et elle est plus parlante en comité que n'importe quel décompte de vulnérabilités.

### 7.5 Obtenir le sponsor : construire l'argumentaire

Un programme de MCS sans soutien explicite de la direction générale échouera sur le premier arbitrage sérieux. Voici les quatre leviers qui fonctionnent, par ordre d'efficacité constatée.

**1. L'exigence externe.** Un assureur, un client, un auditeur ou un régulateur qui demande une preuve crée une obligation que la sécurité seule ne peut pas créer. C'est le levier le plus rapide, et il est souvent déjà disponible — il suffit de le lire.

**2. L'incident sectoriel.** Un concurrent ou un pair touché, publiquement, avec un vecteur d'entrée documenté que vous partagez. La fenêtre d'attention est courte : quelques semaines. Préparez le dossier à l'avance pour pouvoir le sortir au bon moment.

**3. Le coût du non-fait, chiffré.** L'approche du §6.13, appliquée à l'échelle du programme : coût des interventions en urgence, des mesures compensatoires, du support étendu, des heures d'astreinte, comparé au coût de la mise à niveau. Ce levier est le plus solide dans la durée, parce qu'il ne dépend pas de l'émotion.

**4. Le risque, en dernier.** Contre-intuitif, mais l'expérience est constante : l'argument « nous pourrions être attaqués » est le moins efficace des quatre auprès d'une direction générale, parce qu'il est invérifiable et que tout le monde l'a déjà entendu.

📌 **LIMITES** — Aucun de ces leviers ne produit un budget pérenne à lui seul. Ce qui pérennise, c'est la **démonstration de progrès mesuré** : un indicateur de résultat qui s'améliore trimestre après trimestre transforme une dépense en investissement aux yeux d'un directeur financier. C'est pourquoi le chapitre 38 arrive avant le chapitre 40.

### 7.6 ⚠️ Les politiques mort-nées : symptômes, causes, réanimation

| Symptôme observable | Cause profonde | Ce qui la réanime |
|---|---|---|
| Personne ne peut citer un délai de correction | Politique trop générale, non décidable | Réécrire la section classes de service, supprimer le reste |
| Aucune dérogation enregistrée depuis un an | Ce n'est pas que tout est corrigé : c'est que les écarts sont invisibles | Rendre la dérogation facile, rapide et non punitive |
| Les indicateurs sont excellents et personne n'y croit | Dénominateur faux (§2.9) | Publier le périmètre de référence avec le chiffre |
| Le document date de trois ans | Aucun propriétaire ni revue planifiée | Nommer un propriétaire et une date de revue annuelle |
| Elle s'applique à « tous les systèmes » | Aucune classe C4 : les cas contraints violent la règle en permanence | Créer la classe des actifs contraints et l'assumer |

### 7.7 🔴 FIL ROUGE — mai 2026 : la politique MCS v1 et ses trois compromis

Claire Nadeau rédige la première politique MCS d'HELIOMED. Onze pages. Trois compromis y sont assumés explicitement, et c'est ce qui la rend applicable.

**Compromis n° 1 — des délais volontairement modestes.** Le premier projet annonçait 24 h pour une vulnérabilité exploitée en classe C1. Malik Ferhaoui démontre chiffres à l'appui que l'équipe, à deux personnes, ne peut pas le tenir en dehors d'une mobilisation exceptionnelle. Le délai retenu est **72 h**, avec un engagement de révision à 48 h une fois l'outillage d'anneaux en place. Claire préfère un engagement tenu à un affichage flatteur.

**Compromis n° 2 — l'usine sort du régime commun.** Les actifs de Saint-Étienne entrent en classe C4 : régime de compensation et non de correction, fenêtre unique lors de l'arrêt de production d'août, revue trimestrielle. Thomas Berger signe, parce que la règle correspond enfin à ce qu'il peut réellement faire. Les indicateurs les distinguent désormais du reste du parc — le taux de conformité global cesse d'être pollué par des actifs qu'on savait non corrigeables.

**Compromis n° 3 — le parc infogéré reste hors périmètre de mesure, temporairement.** Les 620 postes gérés par le prestataire Numeria ne peuvent pas être mesurés faute d'accès aux données de la console du prestataire. Plutôt que de publier un chiffre inventé, la politique déclare explicitement : *périmètre non mesuré, échéance de mise sous contrôle au 31/12/2026, traité par avenant contractuel.* Ce trou déclaré deviendra l'un des deux leviers de la renégociation du chapitre 13.

**La clause qui déclenche le plus de discussion** est celle du renouvellement de dérogation avec signature de niveau supérieur. Deux responsables y voient une marque de défiance. Pierre Vasseur, directeur général, tranche en trois phrases : si une exception est justifiée, la signer ne coûte rien ; si elle ne l'est pas, il vaut mieux qu'il l'apprenne maintenant.

**Livrable de l'épisode.** La politique MCS v1, plus une annexe d'une page listant les périmètres explicitement non couverts avec leur échéance de mise sous contrôle. Cette annexe, apparemment un aveu de faiblesse, sera l'élément le mieux noté lors de la revue de janvier 2027 (chapitre 39).

→ La suite en 🔴 §8.10, quand un référentiel publié en mars vient confronter cette politique à une grille externe.

→ **Chapitre 8 — Cadre réglementaire et normatif applicable** : ce que l'extérieur exige, et comment lire un référentiel sans s'y perdre.

### Synthèse mentale du chapitre 7

Une politique MCS n'est utile que si chacune de ses phrases permet de trancher un cas réel, si les moyens de l'appliquer sont engagés, et si elle prévoit un chemin légitime pour les cas où corriger est impossible — faute de quoi les équipes emprunteront le chemin du silence. Son cœur est la table des classes de service : trois à quatre classes croisant criticité métier et exposition, dont une classe explicite pour les actifs contraints qu'on sait ne pas pouvoir corriger. Les délais doivent être calibrés sur ce qu'on tient réellement, pas sur ce qui impressionne. Le conflit avec la production se résout par un engagement réciproque dont le pivot est la remontée immédiate des impossibilités. Une dérogation comporte sept champs, dont une date d'expiration et une mesure compensatoire, et son renouvellement doit coûter politiquement plus cher que le précédent. Enfin, l'argument qui obtient un sponsor est rarement le risque : c'est l'exigence externe, l'incident sectoriel ou le coût chiffré du non-fait.

**Trois questions de vérification**

1. Votre politique annonce un délai de correction de 48 heures que vous tenez trois fois par an. Pourquoi est-ce plus dangereux que d'annoncer 15 jours, et devant qui ?
2. Aucune dérogation n'a été enregistrée dans votre organisation depuis douze mois. Quelle est l'interprétation optimiste, quelle est l'interprétation réaliste, et comment tranchez-vous ?
3. Pourquoi une classe de service dédiée aux actifs non corrigeables améliore-t-elle la qualité de vos indicateurs plutôt que de la dégrader ?

---

## Chapitre 8 — Cadre réglementaire et normatif applicable

> ⏱ **Chapitre entièrement périssable.** Toutes les données de ce chapitre ont été vérifiées le **30 juillet 2026**. Le raisonnement, la méthode de lecture et la matrice du §8.8 restent valables ; les statuts, dates et échéances doivent être revérifiés à chaque revue du cours. Les déclencheurs de revue anticipée figurent en tête du document.

Ce chapitre n'a pas vocation à faire de vous un juriste. Il répond à trois questions pratiques : **qu'est-ce qui m'oblige, à quoi exactement, et quelle preuve devrai-je produire ?** La grille de lecture exigence / objectif / moyen du §5.4 s'applique de bout en bout.

### 8.1 NIS2 et la transposition française

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

### 8.2 Le ReCyF : le référentiel d'application

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

### 8.3 Le Cyber Resilience Act : la réglementation passe au produit

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

### 8.4 ISO/IEC 27001 et 27002 : les mesures qui portent le MCS

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

### 8.5 Le paysage sectoriel

Selon votre activité, d'autres textes s'ajoutent. Voici ce que chacun exige **spécifiquement** en matière de maintien.

| Cadre | Qui est concerné | Ce qu'il exige en propre pour le MCS |
|---|---|---|
| **Série IEC 62443** | Systèmes d'automatisation industriels : exploitants, intégrateurs, fabricants | Une gestion des correctifs adaptée au contexte industriel, la définition de zones et de conduits, et — côté fabricant — un cycle de développement sécurisé incluant la gestion des mises à jour de sécurité. Chapitre 29 |
| **Hébergement de données de santé** | Hébergeurs de données de santé à caractère personnel, et leurs clients par ricochet | Certification de l'hébergeur, exigences de maintien et de traçabilité, obligations contractuelles vers le client |
| **Qualification SecNumCloud** | Fournisseurs de services cloud visant les usages sensibles | Exigences détaillées de maintien en condition de sécurité, de gestion des vulnérabilités et de transparence vers le client |
| **PCI DSS** | Traitement de données de cartes de paiement | Le plus **prescriptif** de tous : délais chiffrés d'application des correctifs critiques, exigences de scan périodique interne et externe, exigences de gestion des changements |
| **DORA** | Secteur financier européen | Gestion du risque informatique, dont l'identification et le traitement des vulnérabilités, les tests, et la maîtrise renforcée des prestataires tiers critiques |

**L'enseignement transversal.** Ces cadres divergent sur la forme et convergent sur le fond : connaître son parc, détecter les vulnérabilités, les traiter selon des délais définis, tracer les exceptions, et prouver. Si vous construisez un dispositif solide, l'adaptation à un cadre supplémentaire relève surtout de la mise en forme documentaire. C'est le meilleur argument contre la construction d'un dispositif par référentiel.

### 8.6 Le règlement général sur la protection des données

Souvent oublié dans les discussions de MCS, alors qu'il est le texte le plus universellement applicable.

Son article relatif à la sécurité du traitement impose des mesures techniques et organisationnelles appropriées au risque, en tenant compte de l'état de l'art. Les autorités de contrôle ont retenu à plusieurs reprises, dans des décisions publiées, qu'un **défaut de mise à jour d'un composant présentant une vulnérabilité connue et corrigée** pouvait caractériser un manquement, dès lors que ce défaut avait contribué à une violation de données. Chaque décision s'apprécie au cas d'espèce ; il convient de se référer aux délibérations publiées de l'autorité compétente plutôt qu'à une règle générale.

⚖️ **CADRE — ce qu'il faut en retenir opérationnellement**
Trois éléments sont regardés en cas de contrôle après incident : la vulnérabilité était-elle **connue et corrigée** au moment des faits ; l'organisation disposait-elle d'un **processus** permettant de la traiter ; et l'écart était-il **identifié et décidé**, ou simplement ignoré ? Une dérogation formalisée et compensée place l'organisation dans une position radicalement différente d'une absence totale de trace. C'est un argument de plus, et le plus concret, en faveur du §7.4.

### 8.7 Un modèle méthodologique utile — et ses limites d'applicabilité

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — L'agence américaine de cybersécurité a publié le **10 juin 2026** une directive opérationnelle contraignante (référencée BOD 26-04) organisant la priorisation des mises à jour de sécurité **par le risque** plutôt que par la seule gravité technique : prise en compte de l'exploitation observée, de l'exposition à Internet, et application d'une méthode par arbre de décision, avec des délais de remédiation différenciés.

⚠️ **Portée juridique — à ne jamais confondre.** Ce type de directive est **contraignant uniquement pour les agences civiles fédérales américaines**. Elle ne crée **aucune obligation** pour une organisation française ou européenne, publique ou privée.

📎 [S-21]

**Pourquoi elle figure malgré tout dans ce cours.** Parce qu'elle constitue un **modèle méthodologique documenté et public**, produit par une autorité qui gère un parc considérable, et qu'elle valide la même orientation que celle enseignée au chapitre 16 : la gravité technique seule ne suffit plus à prioriser. Vous pouvez vous en inspirer pour calibrer vos propres délais et défendre votre méthode — en citant une référence publique plutôt qu'une intuition. Vous ne pouvez pas vous en réclamer comme d'une obligation.

### 8.8 ⚖️ Matrice « exigence → objectif → preuve attendue »

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

### 8.9 📌 Limites : la conformité n'est pas la sécurité

Trois avertissements, à garder présents chaque fois que ce chapitre sert d'argument.

**Aucun texte ne dit comment faire.** Ils fixent des résultats. Le savoir-faire — quels outils, quelle cadence, quelle méthode de triage, quel anneau de déploiement — est le sujet des chapitres 14 à 23, et il n'est écrit dans aucun référentiel.

**La conformité est un plancher, pas un objectif.** Une organisation peut être parfaitement conforme et se faire compromettre le lendemain par un chemin que le référentiel n'adresse pas.

**La conformité peut détourner les moyens.** Le risque le plus concret est de consacrer l'essentiel du budget à la production documentaire au détriment de la remédiation. Un indicateur simple permet de le suivre : la part du temps de l'équipe consacrée à produire de la preuve, rapportée au temps consacré à corriger. Aucun seuil universel n'existe — mais une croissance continue de ce ratio, sans amélioration des indicateurs de résultat, mérite un examen.

### 8.10 🔴 FIL ROUGE — juin 2026 : l'analyse d'écart

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

### Synthèse mentale du chapitre 8

Une directive européenne doit être transposée pour s'appliquer, et l'attente du texte national n'est jamais une stratégie : les clients exigent avant le régulateur, les délais de mise en conformité sont courts, et les mesures attendues sont utiles indépendamment du texte. Un référentiel d'application traduit les exigences en objectifs assortis de moyens acceptables de conformité et d'un principe de proportionnalité — ce qui vous laisse une liberté de calibrage, à condition de savoir la justifier par écrit. Le règlement sur la cyberrésilience déplace la réglementation de l'exploitant vers le fabricant, avec des délais de signalement qui sont d'abord une exigence de capacité organisationnelle, pas de formulaire, et des exclusions qui s'analysent produit par produit. Les normes et cadres sectoriels divergent sur la forme et convergent sur le fond : connaître, détecter, traiter dans des délais, tracer les exceptions, prouver. Une directive étrangère peut servir de modèle méthodologique sans jamais constituer une obligation. Enfin, la conformité est un plancher, et le temps consacré à produire de la preuve doit rester une fraction du temps consacré à corriger.

**Trois questions de vérification**

1. Votre direction demande s'il faut attendre la publication du texte national avant d'engager le programme. Donnez trois arguments qui ne reposent pas sur la crainte de la sanction.
2. Un client vous oppose une directive publiée par une autorité étrangère et exige que vous vous y conformiez. Comment répondez-vous sans être ni fermé ni juridiquement imprudent ?
3. Vous êtes certifié selon une norme de management de la sécurité et 40 % de votre parc est hors support. Est-ce compatible ? Qu'est-ce que cela vous apprend sur ce qu'une certification atteste ?

---

## Chapitre 9 — Gouvernance, rôles et comitologie

Le chapitre 7 a produit une doctrine, le chapitre 8 a identifié ce que l'extérieur attend. Reste la question qui décide de leur application réelle : **qui arbitre, à quel rythme, et avec quel mandat ?**

Un programme de MCS meurt rarement d'un défaut technique. Il meurt d'un arbitrage jamais rendu.

### 9.1 Trois niveaux, trois horizons, trois types de décision

La gouvernance du MCS se structure sur trois étages. Les confondre est l'erreur la plus fréquente : on remonte des sujets techniques au niveau stratégique, qui ne sait pas les traiter, et on laisse des arbitrages métier au niveau opérationnel, qui n'a pas le mandat pour les rendre.

| Niveau | Qui | Rythme | Décisions typiques |
|---|---|---|---|
| **Stratégique** | Direction générale, direction des systèmes d'information, RSSI | Semestriel ou trimestriel | Budget pluriannuel, acceptation des risques majeurs, sortie d'obsolescence, arbitrage entre projets et maintien |
| **Tactique** | Comité MCS : RSSI, exploitation, représentants métier, prestataires | Mensuel | Priorisation des campagnes, validation des dérogations, revue des indicateurs, escalades |
| **Opérationnel** | Exploitation, propriétaires techniques | Hebdomadaire ou quotidien | Exécution, qualification des constats, planification des fenêtres, traitement des échecs |

**La règle de circulation** qui rend le dispositif fluide : chaque niveau ne traite que ce que le niveau inférieur ne peut pas trancher **avec son mandat**. Un correctif refusé par un métier n'est pas un problème technique : il remonte. Un correctif qui échoue sur douze machines n'est pas un sujet de comité : il reste au niveau opérationnel.

### 9.2 Le RACI de référence

Un RACI attribue quatre rôles à chaque activité : **R**éalise, **A**pprouve (le décideur, unique), **C**onsulté, **I**nformé. Voici la matrice de base du MCS, à adapter mais dont la logique est stable.

| Activité | RSSI | Exploitation | Propriétaire métier | Direction SI | Prestataire |
|---|---|---|---|---|---|
| Définir la politique et les classes de service | R | C | C | **A** | I |
| Tenir l'inventaire et le périmètre de référence | C | **R/A** | C | I | R |
| Veille et qualification des vulnérabilités | **R/A** | C | I | I | C |
| Priorisation et délais | **R** | C | C | **A** | I |
| Planifier et exécuter la correction | I | **R/A** | C | I | R |
| Décider d'une interruption de service | C | C | **A** | I | I |
| Accorder une dérogation | R | C | **A** | C | I |
| Produire la preuve | C | **R** | I | I | R |
| Escalader une impossibilité | C | **R** | C | **A** | R |
| Contrôler l'application | **R/A** | C | I | I | I |

**Trois points structurants dans ce tableau, souvent inversés dans la réalité.**

**Le RSSI n'approuve pas la correction.** Il qualifie, priorise et contrôle. La décision d'arrêter un service appartient à celui qui en porte la valeur métier — sinon, la sécurité devient responsable de l'indisponibilité qu'elle provoque, ce qui la rend structurellement timide.

**Le propriétaire métier approuve la dérogation.** Pas la sécurité. Celui qui accepte le risque le signe. Faire signer la sécurité revient à lui transférer un risque qu'elle n'a pas les moyens de porter, et cela déresponsabilise le métier.

**L'escalade est une obligation de l'exploitation, pas une faveur.** Elle doit être explicitement inscrite comme un livrable attendu, avec un délai. Une impossibilité non escaladée est un écart invisible, et c'est ce que le contrat interne du §7.3 vise à empêcher.

### 9.3 Le comité MCS : format, ordre du jour, décisions

C'est l'instance centrale. Sa qualité détermine celle du programme.

**Format.** Une heure, mensuel, même date chaque mois. Participants : RSSI (animation), responsable exploitation, un représentant par grand domaine métier concerné, représentant du prestataire d'infogérance si le périmètre le justifie, et un invité tournant selon les sujets.

**Ordre du jour type, en cinq points et dans cet ordre :**

| Point | Durée | Contenu | Sortie attendue |
|---|---|---|---|
| 1. Indicateurs | 10 min | Trois à cinq indicateurs de résultat, avec leur dénominateur | Constat partagé, aucune discussion technique |
| 2. Escalades | 15 min | Impossibilités remontées depuis le dernier comité | **Décision** : correction forcée, dérogation, ou report daté |
| 3. Dérogations | 10 min | Nouvelles demandes, et surtout celles arrivant à échéance | **Décision** : clôture, renouvellement au niveau supérieur, ou correction |
| 4. Campagne à venir | 15 min | Périmètre, fenêtres, risques identifiés | Validation ou ajustement |
| 5. Sujets de fond | 10 min | Un seul sujet par comité : obsolescence, outillage, contrat | Orientation, à instruire |

⚠️ **PIÈGE — le comité qui devient une revue technique**
Symptôme : on passe quarante minutes sur le cas particulier d'un serveur. Cause : les décisions attendues ne sont pas préparées, donc on remplit avec du détail. Remède : chaque point d'escalade et de dérogation arrive au comité avec **une décision proposée** et ses conséquences, pas avec une question ouverte. Le comité valide, amende ou refuse — il n'instruit pas.

✅ **BONNE PRATIQUE (P0) — le relevé de décisions**
Le compte rendu ne relate pas les discussions : il liste les décisions, avec pour chacune l'objet, la décision, le décideur nommé, la date et l'échéance de revue. Une page. C'est ce document qui aura valeur de preuve (§5.6 et chapitre 39), et c'est aussi ce qui protège l'équipe le jour où une décision de report est contestée après incident.

**Ce qui remonte au niveau stratégique.** Quatre choses seulement, et il faut résister à la tentation d'en remonter davantage :

1. les risques dont l'acceptation dépasse le mandat du comité — typiquement une exposition majeure non corrigeable ;
2. les besoins budgétaires, notamment de sortie d'obsolescence ;
3. les arbitrages entre projets et maintien, quand les mêmes équipes sont mobilisées ;
4. la tendance des indicateurs de risque, sur plusieurs trimestres — pas le détail du mois.

### 9.4 Articuler sécurité, exploitation et métiers sans arbitrage permanent

Le conflit d'objectifs du §1.2 est structurel. Une bonne gouvernance ne le supprime pas : elle en **réduit la fréquence**, en pré-arbitrant à froid ce qui sinon devrait être tranché à chaud, à chaque fois.

**Les quatre pré-arbitrages qui suppriment l'essentiel des conflits :**

| Pré-arbitrage | Formulation type | Ce qu'il évite |
|---|---|---|
| Fenêtres récurrentes acquises | « Deuxième jeudi, 22 h - 2 h, sans redemander » | Douze négociations par an |
| Seuil d'urgence pré-autorisé | « Vulnérabilité exploitée sur actif exposé : interruption autorisée sous 72 h, décision du propriétaire technique » | Une négociation en pleine crise |
| Plafond de charge mensuel | « Au plus N heures d'intervention MCS par mois ; au-delà, arbitrage en comité » | Le conflit permanent sur la charge |
| Règle de levée de gel | « Les gels de production comportent une clause de levée pour vulnérabilité exploitée, décidée par X » | Le blocage total pendant six semaines |

**Le principe général**, valable bien au-delà du MCS : *tout arbitrage récurrent doit être transformé en règle une fois pour toutes*. Si vous tranchez trois fois la même question, c'est qu'elle appelle une règle, pas un quatrième arbitrage.

### 9.5 Organisations décentralisées, filiales et entités acquises

Le modèle ci-dessus suppose une organisation unifiée. Beaucoup ne le sont pas.

**Le principe applicable** : la gouvernance du MCS suit la gouvernance générale de l'organisation. Tenter d'imposer un modèle centralisé à un groupe décentralisé produit un dispositif de façade — des règles écrites au siège que personne n'applique en local.

**Le modèle qui fonctionne le plus souvent** est mixte, avec une répartition explicite :

| Défini centralement | Décidé localement |
|---|---|
| Les classes de service et les délais associés | Les fenêtres et les modalités d'exécution |
| Le format de la preuve et des indicateurs | L'outillage, quand une raison locale le justifie |
| La procédure de dérogation et les niveaux de signature | Les dérogations elles-mêmes, dans le cadre défini |
| Le périmètre minimal à inventorier | La conduite de l'inventaire |

⚠️ **PIÈGE — l'entité acquise**
Une société rachetée arrive avec son propre parc, ses propres pratiques, souvent son propre annuaire, et une interconnexion réalisée en urgence pour les besoins de l'intégration. C'est statistiquement l'un des chemins d'entrée les plus fréquents dans les groupes. Deux règles : **l'inventaire de l'entité acquise fait partie de la diligence d'acquisition**, pas de l'intégration à venir ; et **l'interconnexion est traitée comme une exposition** (chapitre 11) tant que le niveau de maintien n'est pas connu et mesuré.

### 9.6 ⚠️ Le RSSI propriétaire du MCS : pourquoi c'est un anti-pattern

C'est une configuration extrêmement répandue, et elle échoue de manière prévisible.

**La configuration.** Le RSSI détecte les vulnérabilités, décide des priorités, demande les corrections, relance, et se voit reprocher les retards. Il est de fait responsable d'un résultat dont il ne contrôle aucun des moyens.

**Pourquoi cela ne peut pas fonctionner.**

- Le RSSI ne dispose ni des accès, ni des compétences d'exploitation, ni des fenêtres, ni du budget d'infrastructure.
- Sa position devient adversariale : il demande, l'exploitation subit. L'information circule mal, les impossibilités sont dissimulées.
- La responsabilité et l'autorité sont dissociées, ce qui est la définition même d'une position intenable.
- Effet secondaire fréquent : le RSSI, faute de pouvoir corriger, finit par mesurer moins — parce que chaque constat supplémentaire aggrave un retard dont on le tient pour responsable.

**La configuration qui fonctionne** est celle du RACI du §9.2 : le MCS est une **activité d'exploitation**, dont la sécurité définit les exigences, qualifie les priorités et contrôle l'application. Autrement dit, la sécurité est **prescriptrice et contrôleuse**, l'exploitation est **réalisatrice**, le métier est **décideur** sur l'interruption et le risque.

📌 **LIMITES — le cas des petites organisations**
Dans une structure de trente personnes, les trois rôles sont parfois tenus par la même personne. La séparation reste utile, mais elle devient une discipline mentale : *quand j'écris cette dérogation, j'agis comme propriétaire métier, et je la signe en tant que tel.* Le formalisme allégé ne dispense pas de la traçabilité, il en réduit seulement le volume — une ligne dans un tableau tenu à jour suffit à la place d'un formulaire.

### 9.7 🔴 FIL ROUGE — juillet 2026 : le premier comité MCS et le désaccord Berger / Ferhaoui

Le comité MCS d'HELIOMED se réunit pour la première fois le premier mardi de juillet. Présents : Claire Nadeau, Sonia Weber, Malik Ferhaoui, Thomas Berger, un représentant du service commercial, et un chargé de compte de l'infogérant Numeria.

**Les indicateurs, en dix minutes.** Le taux de conformité global sur le périmètre de référence est passé de 72 % en décembre à 84 %. Personne ne conteste le chiffre, parce que son dénominateur est affiché — c'est le bénéfice direct de la décision de §2.9.

**L'escalade qui occupe le comité.** Malik demande l'autorisation de mettre à jour le micrologiciel de deux commutateurs cœur de réseau de l'usine, sur lesquels une vulnérabilité exploitée a été identifiée. L'opération suppose une coupure réseau de quinze minutes. Thomas Berger refuse : une coupure réseau non planifiée pendant un cycle de production peut mettre une ligne à l'arrêt pour trois heures, avec des lots à rebuter.

Le désaccord n'est pas un conflit de personnes : chacun défend correctement son mandat. Les deux ont raison, et c'est exactement la situation que le comité existe pour trancher.

**Le déroulement de l'arbitrage.**

1. Claire qualifie : vulnérabilité au catalogue d'exploitation avérée, mais équipements **non joignables depuis Internet**. L'exploitation supposerait un accès préalable au réseau interne. Le risque est réel mais pas immédiat.
2. Malik propose une alternative : réaliser l'opération pendant la relève d'équipe du samedi matin, créneau de quarante minutes sans production, avec Thomas présent.
3. Thomas accepte, sous deux conditions écrites : validation préalable du constructeur sur la version cible, et retour arrière préparé et testé sur un commutateur de rechange avant l'intervention.
4. Sonia Weber valide la mobilisation des deux personnes le samedi.

**Ce que le comité produit vraiment**, au-delà de la décision du jour : deux règles générales, qui n'existaient pas avant.

- *Toute intervention sur le réseau industriel se réalise pendant une relève d'équipe, créneau désormais identifié comme fenêtre récurrente de classe C4.* Le pré-arbitrage du §9.4 est né d'un cas concret.
- *Un correctif de micrologiciel sur équipement industriel exige une validation constructeur écrite et un matériel de secours préparé.* La condition devient une règle, applicable sans repasser en comité.

**Le point de friction non résolu.** Le représentant de Numeria ne peut fournir aucune donnée sur l'état des 620 postes. Il indique que le contrat ne prévoit pas cette restitution. Claire inscrit le point à l'ordre du jour du comité stratégique : ce n'est pas un sujet technique, c'est un sujet contractuel — traité au chapitre 13.

**Livrable de l'épisode.** Un relevé de décisions d'une page : quatre décisions, deux règles générales créées, un point escaladé au niveau stratégique, chacun avec un nom et une date.

→ La suite en 🔴 §10.11, quand le comité demande sur quoi, exactement, portent les 84 % annoncés.

→ **Chapitre 10 — Inventaire et cartographie** : le socle non négociable : savoir ce qu'on doit maintenir.

### Synthèse mentale du chapitre 9

Un programme de MCS meurt d'un arbitrage jamais rendu, pas d'un défaut technique. La gouvernance se structure sur trois niveaux dont chacun ne traite que ce que le niveau inférieur ne peut trancher avec son mandat. Trois attributions de rôles sont contre-intuitives et décisives : la sécurité n'approuve pas la correction, le propriétaire métier signe la dérogation parce qu'il porte le risque, et l'escalade d'une impossibilité est une obligation de l'exploitation, pas une faveur. Le comité mensuel produit des décisions, pas des discussions : chaque point y arrive avec une décision proposée, et le relevé d'une page vaut preuve. Les conflits récurrents se suppriment par pré-arbitrage à froid — fenêtres acquises, seuil d'urgence pré-autorisé, plafond de charge, clause de levée de gel — selon le principe que tout arbitrage rendu trois fois appelle une règle. Enfin, faire du RSSI le propriétaire du MCS dissocie la responsabilité de l'autorité : c'est une position intenable, dont l'effet secondaire le plus pervers est qu'elle pousse à mesurer moins.

**Trois questions de vérification**

1. Votre comité MCS passe quarante minutes sur le cas d'un serveur particulier. Quel est le symptôme, quelle est la cause réelle, et quelle règle de préparation le corrige ?
2. Pourquoi faire signer les dérogations par la sécurité plutôt que par le métier affaiblit-il l'ensemble du dispositif, y compris du point de vue de la sécurité elle-même ?
3. Votre groupe rachète une société de 80 personnes et l'interconnecte au réseau en six semaines. Citez les deux règles à appliquer avant l'interconnexion, et à quel moment du processus d'acquisition elles auraient dû intervenir.

---

## Chapitre 10 — Inventaire et cartographie

### 10.1 Pourquoi tout programme de MCS échoue d'abord ici

C'est la cause d'échec n° 1 du §1.4, et elle mérite d'être formulée sans détour : **tant que le dénominateur est inconnu, aucun indicateur de MCS n'a de sens.**

Reprenons le raisonnement de bout en bout, parce qu'il est souvent accepté du bout des lèvres puis oublié dès la première présentation :

- vous ne corrigez que ce que vous connaissez ;
- vous ne mesurez que ce que votre outil atteint ;
- vous ne présentez donc, dans le meilleur des cas, qu'un pourcentage calculé sur les actifs connus **et** atteints ;
- or les actifs inconnus ne sont pas répartis au hasard : ce sont statistiquement les plus anciens, les moins gérés, les moins documentés — donc les plus vulnérables.

Autrement dit, votre indicateur est non seulement incomplet, il est **biaisé dans le sens favorable**. Les machines qui manquent sont précisément celles qui feraient chuter le chiffre.

⚠️ **PIÈGE — l'inventaire parfait comme préalable**
La conclusion inverse est tout aussi fausse : attendre un inventaire exhaustif avant de commencer à corriger. L'exhaustivité n'existe pas, elle est asymptotique. Ce qu'il faut atteindre rapidement, c'est un inventaire **suffisant, mesuré et honnête** : un périmètre de référence dont vous connaissez le taux de complétude estimé et les zones d'ombre déclarées. Le §10.9 fournit le chemin en trente jours.

### 10.2 Les sources de découverte et leur complémentarité

Aucune source ne voit tout. Chacune a un angle mort structurel, et c'est leur **croisement** qui produit l'information — pas leur addition.

| Source | Ce qu'elle voit bien | Son angle mort structurel |
|---|---|---|
| Base de gestion de configuration | Ce que l'organisation a déclaré | Tout ce qui a été créé sans déclaration ; les machines éteintes y restent |
| Annuaire d'entreprise | Machines jointes au domaine | Serveurs hors domaine, équipements réseau, systèmes industriels, machines de développement |
| Découverte réseau active | Ce qui répond, sur les plages scannées | Machines éteintes au moment du passage, réseaux non scannés, équipements qui ne répondent pas |
| Inventaire d'hyperviseur | Toutes les machines virtuelles, allumées ou non | Le physique, le cloud, les conteneurs |
| Interfaces des fournisseurs cloud | Les ressources cloud, exhaustivement | Tout ce qui est sur site |
| Agents installés | État détaillé de la machine | Les machines sans agent — c'est-à-dire celles qui posent problème |
| Gestion de flotte mobile | Postes et mobiles enrôlés | Les appareils non enrôlés |
| Résolution de noms et baux d'adresses | Ce qui s'est connecté récemment | Peu structuré, beaucoup de bruit |
| **Comptabilité fournisseurs** | **Les abonnements payés** | Ne dit rien du technique — mais révèle le shadow IT |
| Découverte externe | Ce qui est publié sur Internet à votre nom | Rien de ce qui est interne |

**Le point qui surprend toujours** : la comptabilité fournisseurs est l'une des sources les plus rentables d'un premier inventaire. Une facture correspond à un service réel, utilisé par quelqu'un, contenant probablement des données — et souvent inconnu de la direction des systèmes d'information. Le rapport effort/découverte y est excellent.

✅ **BONNE PRATIQUE (P0)** — Utilisez au minimum **quatre sources de nature différente**, dont une non technique. Trois sources techniques partagent souvent le même angle mort ; une source non technique ne le partage jamais.

### 10.3 La réconciliation : lire les écarts plutôt que les chiffres

C'est la compétence centrale de ce chapitre. Face à plusieurs sources donnant des chiffres différents, la mauvaise question est « lequel est le bon ? ». La bonne question est : **que signifie chaque écart ?**

**La méthode, en quatre étapes.**

**1. Choisir un identifiant pivot.** Le nom d'hôte est instable, l'adresse IP est mouvante, l'adresse matérielle change avec le matériel. En pratique, on utilise une combinaison : nom d'hôte normalisé + identifiant unique de machine + adresse matérielle, avec des règles de rapprochement documentées. L'identifiant pivot doit être **choisi et écrit**, pas improvisé à chaque extraction.

**2. Construire les ensembles.** Pour chaque paire de sources : présent dans les deux, présent seulement dans A, présent seulement dans B.

**3. Interpréter chaque écart.** C'est ici que se trouve toute la valeur, et chaque catégorie appelle une action différente :

| Type d'écart | Signification probable | Action |
|---|---|---|
| Déclaré mais ne répond pas | Machine éteinte, décommissionnée à moitié, ou nom obsolète | Vérifier, puis décommissionner en règle (ch. 35) |
| Répond mais non déclaré | Création hors processus, appliance livrée, entité rattachée | Trouver un propriétaire ou éteindre (§5.5) |
| Déclaré, actif, mais hors outil de gestion | **N'a jamais reçu de correctif** | Priorité maximale : c'est le plus dangereux des trois |
| Présent dans deux sources avec des attributs contradictoires | Données obsolètes dans l'une | Définir laquelle fait foi, par attribut |

**4. Publier le résultat avec ses trous.** Le livrable n'est pas un nombre, c'est un tableau d'ensembles avec les causes identifiées. C'est cela qui donne de la crédibilité au chiffre annoncé ensuite.

⚠️ **PIÈGE — le troisième type d'écart**
La ligne « déclaré, actif, mais absent de l'outil de gestion » est la plus grave et la moins visible. Ces machines apparaissent dans tous les documents officiels, sont considérées comme gérées par tout le monde, et n'ont jamais reçu un seul correctif par le canal prévu. Elles sont invisibles à la fois pour l'inventaire *et* pour les indicateurs de conformité, puisqu'elles ne figurent pas dans le dénominateur de l'outil.

### 10.4 Les attributs minimaux d'un actif maintenable

Un inventaire qui ne contient que des noms de machines ne sert à rien pour le MCS. Voici le jeu minimal — le modèle complet figure en **Annexe I**.

| Attribut | Pourquoi il est indispensable au MCS |
|---|---|
| Identifiant unique et stable | Sans lui, aucune réconciliation ni aucun historique |
| Type et rôle | Détermine la méthode de correction |
| **Propriétaire métier** | Qui décide de l'interruption (§5.5) |
| **Propriétaire technique** | Qui exécute et produit la preuve |
| **Criticité** | Détermine la classe de service (§7.2) |
| **Exposition** | Internet, réseau interne, isolé — détermine la priorité réelle (ch. 11) |
| Environnement | Production, recette, développement, laboratoire (ch. 28) |
| Système et version | Base de la corrélation avec les vulnérabilités |
| **Statut et date de fin de support** | Base du plan d'obsolescence (ch. 12) |
| Fournisseur et contrat | Qui doit corriger, et sous quel délai contractuel (ch. 13) |
| Fenêtre de maintenance | Quand on peut intervenir |
| Outils de gestion et de scan | Permet de calculer la couverture réelle |
| Dépendances | Qui casse si on l'arrête |
| Dérogations en cours | Dette formalisée attachée à l'actif |
| Dernière preuve de conformité | Date et nature |

**Le test de qualité de votre inventaire** tient en une question : pouvez-vous produire, en moins de dix minutes, la liste des actifs **exposés à Internet, hors support, sans propriétaire nommé** ? Si oui, votre inventaire est exploitable. Sinon, il est documentaire.

### 10.5 Dépendances applicatives et effets de bord

Connaître les actifs ne suffit pas : il faut savoir **ce qui casse quand on en arrête un**. C'est ce qui transforme une intervention planifiée en incident.

**Trois niveaux de cartographie, par effort croissant.**

| Niveau | Méthode | Effort | Ce que ça donne |
|---|---|---|---|
| Déclaratif | Demander aux propriétaires | Faible | Incomplet mais immédiat ; révèle surtout ce que les gens croient |
| Observé | Analyse des flux réseau réels sur une période représentative | Moyen | Fiable sur ce qui a effectivement communiqué |
| Modélisé | Cartographie applicative maintenue | Élevé | Complet, mais se dégrade vite sans propriétaire |

✅ **BONNE PRATIQUE (P1)** — Ne visez pas la cartographie complète. Cartographiez d'abord les **dépendances des actifs de niveau 0** (annuaire, résolution de noms, hyperviseur, sauvegarde, authentification, temps) : ce sont eux dont l'arrêt produit des effets en cascade imprévus, et ils représentent moins de 5 % du parc.

⚠️ **PIÈGE — la dépendance temporelle**
Certaines dépendances ne se manifestent qu'à des moments précis : traitement de nuit, clôture mensuelle, sauvegarde hebdomadaire, échange avec un partenaire. Une analyse de flux menée sur trois jours ouvrés les manquera. Observez sur au moins un cycle métier complet — un mois, si votre activité a une clôture mensuelle.

### 10.6 Shadow IT et services en ligne non déclarés

Les services souscrits hors du circuit de la direction des systèmes d'information sont une part significative du périmètre réel, et ils sont particulièrement pertinents pour le MCS : ils contiennent des données, ils disposent souvent d'accès à d'autres systèmes via des connecteurs, et personne ne suit leur configuration.

**Les quatre méthodes de détection, par rentabilité décroissante :**

1. **La comptabilité.** Extraire les lignes de dépense correspondant à des abonnements logiciels. Simple, non technique, extrêmement productif.
2. **Le fournisseur d'identité.** Lister les applications ayant reçu une autorisation de connexion via l'authentification unique, et les autorisations déléguées accordées à des applications tierces. C'est aussi ce qui révèle les connecteurs disposant d'accès à la messagerie ou aux fichiers (chapitre 31).
3. **Les journaux de navigation ou de proxy.** Détectent l'usage, pas le contrat.
4. **L'enquête directe.** Demander aux équipes ce qu'elles utilisent, sans posture punitive. Le rendement dépend entièrement du climat : une organisation qui sanctionne le shadow IT ne le découvre jamais.

📌 **LIMITES** — Aucune de ces méthodes ne détecte un service gratuit, souscrit avec une adresse personnelle, utilisé par une seule personne. Ce cas relève de la sensibilisation et de la politique d'usage, pas de l'inventaire technique.

### 10.7 Maintenir l'inventaire vivant

Un inventaire est un actif périssable : il se dégrade dès le jour de sa constitution. Quatre mécanismes le maintiennent.

| Mécanisme | Principe | Effet |
|---|---|---|
| **Intégration au cycle de vie** | Aucune mise en production sans déclaration ; aucun décommissionnement sans retrait | Empêche la dégradation à la source |
| **Réconciliation périodique automatisée** | Rejouer le croisement de sources chaque mois | Détecte les écarts qui réapparaissent |
| **Contrôles de complétude** | Règles de qualité : actif sans propriétaire, sans criticité, sans date de fin de support | Mesure la qualité de la donnée, pas seulement sa quantité |
| **Indicateur de dérive** | Nombre de nouveaux écarts par mois | Mesure si le processus tient ou se dégrade |

✅ **BONNE PRATIQUE (P0)** — L'intégration au cycle de vie est la seule mesure structurelle ; les trois autres sont des rattrapages. Concrètement : la déclaration d'un actif, avec ses deux propriétaires, devient une **condition de mise en production**, au même titre que la sauvegarde. C'est une décision de gouvernance, pas un projet d'outillage.

### 10.8 📌 Ce qu'aucun outil de découverte ne verra

Soyons explicites sur les limites, parce que les ignorer produit une fausse assurance.

- **Les systèmes industriels muets**, qui ne répondent pas à une sollicitation réseau, et qu'il ne faut de toute façon pas interroger activement (§3.7).
- **Les environnements séparés physiquement**, par construction.
- **Les composants embarqués** dans les applications, qui n'ont pas d'existence réseau propre (chapitre 26).
- **Les actifs éphémères** — conteneurs, agents de construction, instances à mise à l'échelle automatique — qui n'existent pas au moment où l'inventaire passe. Pour eux, l'inventaire doit interroger l'orchestrateur, pas le réseau.
- **Les actifs détenus par un prestataire** pour votre compte, qui ne sont pas sur vos réseaux (chapitre 13).
- **Les micrologiciels**, qui ne sont presque jamais remontés par les outils d'inventaire standard (§3.8).

Pour chacune de ces catégories, la seule réponse honnête est de la **déclarer non couverte**, avec un propriétaire et une échéance de première mesure — exactement comme dans la politique du §7.7.

### 10.9 ✅ Inventaire minimal viable en trente jours

| Prio | Action | Résultat attendu |
|---|---|---|
| **P0** | Croiser quatre sources dont une non technique | Périmètre de référence, avec ses écarts identifiés |
| **P0** | Attribuer criticité et exposition à chaque actif, même grossièrement | Base du classement en classes de service |
| **P0** | Lancer la campagne de désignation des propriétaires (§5.5) | Actifs orphelins identifiés |
| **P0** | Publier le périmètre **avec ses zones non couvertes déclarées** | Crédibilité de tous les indicateurs ultérieurs |
| P1 | Calculer et publier la couverture de chaque outil sur ce périmètre | Vision honnête de ce qui est réellement géré |
| P1 | Cartographier les dépendances des actifs de niveau 0 | Prévention des effets en cascade |
| P1 | Extraire les abonnements en ligne depuis la comptabilité | Détection du shadow IT |
| P2 | Automatiser la réconciliation mensuelle | Maintien dans la durée |
| P2 | Intégrer la déclaration au processus de mise en production | Arrêt de la dégradation à la source |

### 10.10 🔬 Mini-lab 2 — Réconciliation d'inventaire

**Objectif** — Construire un périmètre de référence à partir de sources contradictoires, en déduire les indicateurs corrects, et repérer le piège de vocabulaire.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §10.3, §10.4, annexe I.4 · **Livrable** table de réconciliation + quatre indicateurs.
**Compétences validées** — ✔ construire un périmètre maître à partir de sources divergentes ✔ interpréter un écart selon son type ✔ choisir le bon dénominateur par indicateur ✔ distinguer couverture, conformité et ratio conservateur

**Données fournies.** Une filiale de 3 sites. Quatre sources ont été extraites le même jour.

| Source | Effectif |
|---|---|
| **C** — Base de gestion de configuration | 96 |
| **K** — Console de déploiement des correctifs | 71 |
| **D** — Découverte (réseau + hyperviseur + interface cloud) | 118 |
| **F** — Extraction comptable des abonnements en ligne | 14 abonnements |

Éléments de recoupement communiqués par l'équipe :

- toutes les machines de la console figurent dans la base de gestion ;
- 9 machines de la base de gestion ne répondent plus depuis plus de 60 jours ;
- 31 machines découvertes ne figurent pas dans la base de gestion ;
- la console rapporte 68 machines conformes sur les 71 qu'elle gère ;
- parmi les 14 abonnements en ligne, 5 ne sont connus d'aucune équipe technique.

**Questions.**

1. Construisez la table de réconciliation complète des ensembles.
2. Quel est le périmètre de référence ?
3. Calculez : conformité interne à la console · couverture de la console · conformité globale sur les actifs en service · conformité globale sur le périmètre de référence.
4. Quel sous-ensemble représente le risque le plus élevé, et pourquoi ?
5. Le responsable d'exploitation propose d'annoncer « 96 % de conformité » au comité. Que lui répondez-vous ?
6. Comment traitez-vous les 5 abonnements inconnus ?

**Corrigé commenté**

**1 et 2 — Table de réconciliation**

| Ensemble | Calcul | Effectif |
|---|---|---|
| Gérées par la console (K ⊆ C) | donné | 71 |
| Déclarées, actives, hors console (C ∩ D, hors K) | 96 − 71 − 9 | 16 |
| Déclarées mais ne répondant plus (C \ D) | donné | 9 |
| **Total base de gestion (C)** | 71 + 16 + 9 | **96** |
| Déclarées et actives (C ∩ D) | 71 + 16 | 87 |
| Actives non déclarées (D \ C) | donné | 31 |
| **Total découvert actif (D)** | 87 + 31 | **118** |
| **Périmètre de référence (C ∪ D)** | 87 + 9 + 31 | **127** |

Les 14 abonnements en ligne s'ajoutent au périmètre en tant qu'actifs de service — ils ne se comptent pas avec les machines, mais ils ne s'en excluent pas non plus. Le périmètre complet comporte donc **127 actifs techniques et 14 actifs de service**.

**3 — Indicateurs**

| Indicateur | Calcul | Valeur |
|---|---|---|
| Conformité interne à la console | 68 / 71 | **96 %** |
| Couverture de la console | 71 / 118 | **60 %** |
| **Ratio confirmé conforme**, actifs en service | 68 / 118 | **58 %** |
| **Ratio confirmé conforme**, périmètre maître | 68 / 127 | **54 %** |
| **Non mesuré** | 47 actifs en service | **40 %** |

**4 — Le sous-ensemble le plus risqué.** Les **16 machines déclarées, actives, mais hors console**. Ce ne sont pas les 31 non déclarées — celles-là, tout le monde sait qu'on ne les connaît pas. Les 16 sont pires : elles figurent dans tous les documents officiels, chacun les croit gérées, et elles n'ont **jamais** reçu de correctif par le canal prévu. C'est l'écart de type 3 du §10.3.

**5 — La réponse à faire.** Le chiffre de 96 % est exact et il décrit **la conformité interne d'un outil qui couvre 60 % du parc actif**. L'annoncer sans son dénominateur n'est pas une erreur de calcul, c'est une erreur de vocabulaire aux conséquences durables : le comité prendra ses décisions sur une base fausse, et le jour où le chiffre réel apparaîtra — audit, incident, changement d'équipe — la crédibilité de toute la fonction sera atteinte. La formulation correcte tient en une phrase : *« 96 % de conformité sur 60 % de couverture, soit 58 % de conformité réelle sur les actifs en service »*.

**6 — Les cinq abonnements inconnus.** Ils ne relèvent pas d'un traitement technique en première intention. La séquence est : identifier le payeur via la comptabilité → identifier l'utilisateur → déterminer les données traitées → déterminer les connecteurs et autorisations accordés (chapitre 31) → décider de régulariser ou de résilier. Aucune de ces étapes n'est technique, et c'est le point du chapitre.

**Les trois erreurs attendues.** Additionner les sources (96 + 118 = 214), ce qui compte deux fois les machines communes. Exclure les 9 machines éteintes du périmètre, alors qu'elles portent des comptes de service et des enregistrements réseau actifs et relèvent d'un décommissionnement en règle. Et écarter les abonnements en ligne au motif qu'il ne s'agit pas de machines.

### 10.11 🔴 FIL ROUGE — août 2026 : sur quoi portent les 84 % ?

Au comité de juillet (§9.7), Claire Nadeau a annoncé 84 % de conformité. Le représentant commercial pose au comité suivant une question simple : *84 % de quoi ?*

Claire l'attendait. La réponse tient en un tableau de quatre lignes, projeté en séance.

| Population | Effectif | Conformes | Taux |
|---|---|---|---|
| Serveurs et postes gérés par la console interne | 176 | 158 | 90 % |
| Actifs de classe C4 — usine, régime de compensation | 14 | *sans objet* | *compensation vérifiée : 12/14* |
| Postes gérés par l'infogérant | 620 | **non mesuré** | **—** |
| Actifs orphelins en cours d'extinction | 10 | 0 | 0 % |

Les 84 % portaient sur la première ligne uniquement. Rapportés à l'ensemble du périmètre connu, postes infogérés compris, ils tomberaient sous 25 % — non parce que ces postes seraient mal maintenus, mais parce que **personne n'en sait rien**.

**La réaction du comité est celle qu'espérait Claire.** Personne ne conteste le travail réalisé. La discussion se déplace immédiatement là où elle est utile : *comment obtient-on la mesure des 620 postes ?* Le sujet devient contractuel, il est porté au comité stratégique, et il obtient un mandat de négociation — ce que six mois de relances n'avaient pas produit.

**Décision prise.** Tous les indicateurs d'HELIOMED seront désormais publiés en quatre populations distinctes, avec la mention **« non mesuré »** partout où c'est le cas. La règle est explicite : *un périmètre non mesuré s'affiche comme non mesuré, jamais comme conforme, et jamais comme absent du tableau.*

**Livrable de l'épisode.** Le tableau de bord en quatre populations, qui deviendra le format de référence du chapitre 38 — et la fiche de réconciliation d'inventaire figurant en Annexe I.

→ La suite en 🔴 §11.12, quand l'inventaire ne suffira plus et qu'il faudra savoir ce qui est réellement atteignable.

→ **Chapitre 11 — Exposition et chemins d'attaque** : la différence entre ce qui existe et ce qui peut être atteint.

### Synthèse mentale du chapitre 10

Tant que le dénominateur est inconnu, aucun indicateur n'a de sens — et le biais joue toujours dans le sens favorable, puisque les actifs manquants sont statistiquement les moins maintenus. Aucune source de découverte ne voit tout : c'est leur croisement qui produit l'information, et une source non technique comme la comptabilité fournisseurs a le meilleur rapport effort/découverte. La compétence centrale n'est pas de choisir le bon chiffre mais de lire les écarts, dont le plus dangereux est celui des machines déclarées, actives et absentes de l'outil de gestion : tout le monde les croit gérées et elles n'ont jamais reçu de correctif. Un inventaire exploitable se teste en une question — peut-on sortir en dix minutes la liste des actifs exposés, hors support et sans propriétaire ? Il se maintient par intégration au cycle de vie, la seule mesure structurelle ; le reste est du rattrapage. Enfin, tout ce qui n'est pas couvert doit être déclaré non couvert, avec un propriétaire et une échéance.

**Trois questions de vérification**

1. Trois de vos sources d'inventaire donnent trois chiffres différents. Quelle est la mauvaise question, quelle est la bonne, et quel type d'écart traitez-vous en premier ?
2. Pourquoi un taux de conformité calculé sur les seuls actifs connus est-il biaisé dans le sens favorable, et pas simplement incomplet ?
3. Votre inventaire est complet mais ne comporte ni criticité, ni exposition, ni propriétaire. Que pouvez-vous en faire concrètement pour piloter le MCS ?

---

## Chapitre 11 — Exposition et chemins d'attaque

### 11.1 L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint

Le chapitre 10 a produit une liste. Cette liste ne suffit pas, parce qu'elle traite comme équivalents deux actifs qui ne le sont pas du tout : un serveur portant une vulnérabilité critique mais joignable uniquement depuis un réseau d'administration restreint, et le même serveur publié sur Internet.

**La différence est d'un facteur considérable sur le risque réel, et elle n'apparaît dans aucun score de gravité** (§4.10). C'est vous, et personne d'autre, qui apportez cette information.

**Le modèle mental.** Une vulnérabilité est une porte fermée à clé. L'exposition détermine s'il y a un couloir qui mène jusqu'à cette porte, et qui peut l'emprunter. Une porte fragile au fond d'une pièce fermée n'est pas le même problème qu'une porte fragile sur la rue.

**Trois questions définissent l'exposition d'un actif :**

1. **Depuis où est-il joignable ?** Internet, réseau bureautique, réseau d'administration, réseau industriel, nulle part.
2. **Par qui ?** Anonyme, utilisateur authentifié quelconque, utilisateur privilégié, prestataire.
3. **Vers quoi mène-t-il ?** Un actif compromis donne accès à quoi d'autre — c'est la question des chemins d'attaque (§11.4).

Les deux premières questions relèvent de la surface d'exposition. La troisième change la nature de l'exercice : elle transforme une liste d'actifs en **graphe**.

### 11.2 Les familles d'approche, et ce qu'elles apportent réellement

| Approche | Point de vue | Ce qu'elle apporte | Ce qu'elle ne voit pas |
|---|---|---|---|
| **Découverte externe** | Depuis Internet, sans rien savoir de vous | Ce qui est réellement publié à votre nom, y compris ce que vous ignorez | Tout l'interne |
| **Consolidation de la vue des actifs** | Agrégation de vos propres sources | Une vue unifiée exploitable, avec les écarts (ch. 10) | Ce qu'aucune de vos sources ne connaît |
| **Analyse de chemins d'attaque** | Le point de vue de l'attaquant | Les enchaînements entre actifs, identités et droits | Ce qui n'est pas modélisé dans ses sources |
| **Test d'intrusion** | Un attaquant réel, sur un périmètre borné | La démonstration concrète, avec preuve | Le reste du périmètre, et l'instant d'après |

**Le principe fondateur de la découverte externe** mérite d'être compris, parce qu'il explique son rendement : elle part de ce que **l'extérieur** peut savoir de vous — noms de domaine, enregistrements publics, certificats émis à votre nom, blocs d'adresses, mentions publiques — et reconstruit votre surface. Elle trouve donc précisément ce que votre inventaire interne ne connaît pas : le site créé par une équipe marketing chez un hébergeur externe, l'environnement de démonstration monté pour un salon en 2023, la ressource cloud d'un projet abandonné.

⚠️ **PIÈGE — les certificats comme source de découverte**
Les certificats émis publiquement sont enregistrés dans des journaux consultables par tous. Quand vous publiez un service sous un nom, ce nom devient public — y compris pour un environnement de recette ou d'administration que vous pensiez discret. Ce n'est pas une faille, c'est le fonctionnement normal du dispositif, et c'est une des premières sources qu'utilise un attaquant. Nommer un service `admin-preprod.exemple.fr` n'a donc rien de discret.

### 11.3 L'exposition Internet : ce qu'il faut chercher en premier

Par ordre de gravité constatée, voici ce qui se trouve réellement lors d'un premier exercice de découverte externe.

| Découverte | Pourquoi c'est grave | Fréquence constatée |
|---|---|---|
| **Interface d'administration publiée** | Conçue pour un réseau de confiance, souvent sans authentification forte | Très fréquente |
| **Service oublié** | Plus de propriétaire, donc plus de correctifs depuis des années | Très fréquente |
| Environnement de recette exposé | Données parfois réelles, durcissement moindre (ch. 28) | Fréquente |
| Stockage cloud ouvert | Fuite de données sans aucune intrusion | Fréquente |
| Accès distant secondaire | Mis en place en urgence, jamais retiré | Fréquente |
| Équipement réseau avec interface publiée | Cible de premier choix, très recherchée | Moins fréquente, très grave |

**La première tâche d'un programme de MCS**, avant même de corriger quoi que ce soit, consiste à établir cette liste. Elle est courte, elle se constitue en quelques jours, et elle produit presque toujours des fermetures immédiates — c'est-à-dire une réduction de risque sans correctif, sans fenêtre et sans négociation.

🖼 **SCHÉMA — Chemin d'attaque type en six étapes.** *Graphe orienté du poste bureautique jusqu'à la console de sauvegarde, chaque arête annotée par ce qui la rend praticable (mot de passe local partagé, session privilégiée, joignabilité réseau).*

### 11.4 Chemins d'attaque : de la liste au graphe

Une vulnérabilité isolée est rarement l'histoire complète. Une compromission réelle est un **enchaînement** : entrée par un actif exposé, récupération d'identifiants, déplacement vers un actif de plus grande valeur, élévation de privilèges, atteinte de l'objectif.

**Les trois dimensions à croiser** — et c'est le croisement qui fait l'information :

| Dimension | Question |
|---|---|
| **Réseau** | Depuis cet actif, qu'est-ce qui est joignable ? |
| **Identité** | Quels comptes existent ou peuvent être obtenus sur cet actif, et où sont-ils valables ailleurs ? |
| **Vulnérabilité** | Que permet techniquement chaque étape ? |

**L'exemple canonique**, qu'on retrouve dans une grande partie des compromissions documentées :

```
Poste bureautique compromis (hameçonnage — aucune vulnérabilité exploitée)
    → un compte d'administration local partage son mot de passe avec 400 autres postes
    → déplacement vers un serveur de fichiers
    → un compte de service à privilèges élevés y a laissé une session ouverte
    → récupération de ce compte
    → accès à la console de sauvegarde
    → accès à l'ensemble des données, y compris les sauvegardes
```

**Ce que cet exemple enseigne au MCS.** Aucune des étapes ne dépend d'une vulnérabilité au sens du chapitre 4, sauf éventuellement la première. Ce qui rend le chemin praticable, ce sont des **choix de configuration et d'identité** : mot de passe local partagé, compte de service surprivilégié, console de sauvegarde joignable depuis le réseau bureautique. C'est précisément le périmètre des chapitres 22 et 24 — et la démonstration que réduire le MCS aux correctifs laisse ce chemin entièrement ouvert.

### 11.5 Combinaisons toxiques

Une **combinaison toxique** est un ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur.

| Élément 1 | Élément 2 | Élément 3 | Résultat |
|---|---|---|---|
| Vulnérabilité de gravité moyenne | Actif joignable depuis Internet | Compte à privilèges élevés présent sur l'actif | Compromission du domaine |
| Machine hors support | Aucune segmentation | Copie de données de production | Fuite de données par un actif « secondaire » |
| Compte de service | Mot de passe inchangé depuis 2019 | Droits d'administration sur 200 machines | Propagation immédiate |
| Recette exposée | Mêmes identifiants qu'en production | Journalisation absente | Compromission indétectable |

**Le point qui rend ces combinaisons dangereuses en pratique** : chaque élément pris isolément passe sous les seuils. La vulnérabilité moyenne n'est pas prioritaire, l'exposition seule paraît acceptable, le compte à privilèges est justifié par un besoin d'exploitation. Aucun outil raisonnant constat par constat ne les remontera. Il faut **croiser**, et le croisement est un travail d'analyse, pas d'outillage.

✅ **BONNE PRATIQUE (P1)** — Faites une revue trimestrielle des combinaisons, sur une liste courte et fixe de règles écrites : *actif exposé + compte à privilèges*, *hors support + non segmenté*, *recette + données de production*, *compte de service + droits étendus + mot de passe ancien*. Quatre requêtes sur votre inventaire enrichi suffisent, et elles trouvent ce qu'aucun scanner ne remonte.

### 11.6 Atteignabilité : de la présence du composant à l'exécution du code vulnérable

Une nuance qui divise le volume de travail par un facteur important, et qui devient centrale au chapitre 25.

Un outil détecte la **présence** d'un composant vulnérable. Il ne détecte pas si le **code vulnérable est réellement atteignable** dans le contexte d'exécution. Trois niveaux :

| Niveau | Question | Effet sur la priorité |
|---|---|---|
| Présent | Le composant est installé | Signal faible |
| Chargé | Le composant est effectivement utilisé par l'application | Signal moyen |
| **Atteignable** | La fonction vulnérable peut être appelée par une entrée contrôlable par un attaquant | **Signal fort** |

**Deux applications concrètes :**

- Une bibliothèque vulnérable dont la fonction fautive n'est jamais appelée par l'application ne constitue pas un risque exploitable. Le fournisseur peut le déclarer formellement — c'est l'objet des déclarations d'exploitabilité du §4.8.
- Un service vulnérable installé mais **désactivé** n'est pas exposé. Vérifier l'état d'activation avant de traiter un constat évite une part significative du travail — et c'est une vérification de trente secondes.

📌 **LIMITES** — L'analyse d'atteignabilité est coûteuse et imparfaite : elle dépend de la qualité de l'analyse du code, elle traite mal les appels dynamiques, et elle peut donner une fausse assurance. Utilisez-la pour **déprioriser de façon documentée**, jamais pour clore définitivement un constat. La distinction entre déprioriser et clore est traitée au chapitre 17.

### 11.7 Actifs d'entrée et actifs de niveau 0

Deux catégories méritent un traitement distinct de tout le reste du parc.

**Les actifs d'entrée** — tout ce par quoi un attaquant peut arriver : passerelles d'accès distant, portails publiés, serveurs de messagerie, postes de travail, interfaces d'échange avec des partenaires. Leur particularité : ils sont exposés **par conception**, on ne peut pas fermer leur exposition sans supprimer leur fonction. Le seul levier disponible est donc la **vitesse de correction**. Ce sont eux qui justifient la classe C1 du §7.2.

**Les actifs de niveau 0** — ceux dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, autorité de certification, plan de gestion de virtualisation, console de sauvegarde, outil de déploiement de correctifs, coffre-fort de secrets, chaîne de construction logicielle, outillage d'administration.

⚠️ **PIÈGE — le paradoxe du niveau 0**
Ces actifs sont statistiquement parmi les plus en retard du parc, pour trois raisons convergentes : leur mise à jour « n'apporte rien aux métiers », elle interrompt l'outil que les administrateurs utilisent quotidiennement, et ils sont souvent considérés comme protégés parce qu'ils ne sont pas exposés à Internet. Or leur compromission ne nécessite pas d'exposition externe : elle se produit par un chemin interne (§11.4). **Le fait de ne pas être exposé à Internet ne rend pas un actif secondaire.**

✅ **BONNE PRATIQUE (P0)** — Établissez la liste nominative de vos actifs de niveau 0. Elle tient sur une page. Placez-les tous en classe C1, avec fenêtre récurrente et propriétaire nommé. C'est la mesure de MCS ayant le meilleur rapport effort/réduction de risque de tout ce cours.

### 11.8 Fermer l'exposition plutôt que corriger

Voici l'un des enseignements les plus rentables de ce cours, et l'un des moins appliqués.

Face à une vulnérabilité sur un actif exposé, deux actions sont possibles : corriger, ou **retirer l'exposition**. Comparons-les honnêtement.

| Critère | Corriger | Fermer l'exposition |
|---|---|---|
| Délai | Heures à semaines | **Minutes à heures** |
| Risque de régression | Réel | Faible, et immédiatement réversible |
| Fenêtre nécessaire | Souvent | Rarement |
| Effet sur les **futures** vulnérabilités du même actif | Aucun | **Protège aussi contre celles à venir** |
| Effet métier | Nul si tout va bien | Peut supprimer un usage légitime |

La quatrième ligne est décisive et rarement formulée : fermer une exposition inutile protège contre toutes les vulnérabilités futures du service concerné, y compris celles qui ne sont pas encore découvertes. C'est la seule action de ce cours qui produise un effet durable sans effort récurrent.

**Les questions à poser systématiquement** devant un actif exposé :

1. Cette exposition est-elle **nécessaire** aujourd'hui, ou héritée d'un besoin passé ?
2. Peut-elle être **restreinte** — à des plages d'adresses connues, derrière une authentification, via un accès distant maîtrisé ?
3. L'interface d'administration a-t-elle besoin d'être publiée, ou seulement le service métier ?

En pratique, une part significative des expositions constatées lors d'un premier inventaire externe ne correspond plus à aucun besoin actif. Les fermer coûte une demi-journée et retire du périmètre à surveiller des actifs entiers.

### 11.9 Suivre l'exposition dans le temps

L'exposition n'est pas un état, c'est un flux : chaque projet en crée, chaque urgence en ajoute, chaque décommissionnement incomplet en laisse.

**Les trois indicateurs utiles**, définis rigoureusement au chapitre 38 :

- **nombre d'actifs exposés à Internet**, avec son évolution — la tendance importe plus que la valeur absolue ;
- **délai moyen entre l'apparition d'une exposition et sa détection** — mesure la réactivité de votre découverte externe ;
- **nombre de réapparitions** — une exposition fermée qui revient signale un problème de processus, pas de configuration : quelqu'un la recrée, et il faut comprendre pourquoi.

⚠️ **PIÈGE — l'exposition temporaire**
« On ouvre pour la migration, on referme après. » La règle qui fonctionne : **toute ouverture temporaire porte une date de fermeture dans la demande de changement**, et un contrôle automatique vérifie la fermeture à cette date. Sans cela, la statistique est constante : une part importante de ces ouvertures reste en place des années.

### 11.10 📌 Ce que chaque approche ne voit pas

| Approche | Angle mort |
|---|---|
| Inventaire interne | Ce que vous ne savez pas posséder — ressources hébergées ailleurs, environnements montés hors processus |
| Scanner de vulnérabilités | La joignabilité réelle depuis l'extérieur ; il scanne depuis là où il est placé |
| Découverte externe | L'interne ; et elle peut attribuer à tort un actif qui ne vous appartient pas |
| Analyse de chemins d'attaque | Ce qui n'est pas dans ses sources : systèmes industriels, environnements séparés, applications propriétaires |
| Test d'intrusion | Tout ce qui n'était pas dans le périmètre, et tout ce qui a changé depuis |

**La conséquence méthodologique** : ces approches ne se substituent pas, elles se croisent. Un actif remonté par la découverte externe et absent de l'inventaire interne est le constat le plus riche que produise ce chapitre — il signale à la fois une exposition et un trou d'inventaire.

### 11.11 ✅ Livrable — Carte des actifs exposés et matrice des chemins critiques

**Partie 1 — Carte des actifs exposés.** Une ligne par actif joignable depuis l'extérieur.

| Actif | Service publié | Depuis quand | Propriétaire | Nécessité confirmée | Restriction possible | Classe | Décision |
|---|---|---|---|---|---|---|---|

**Partie 2 — Matrice des chemins critiques.** Une ligne par enchaînement plausible, limité aux chemins menant à un actif de niveau 0.

| Point d'entrée | Étape intermédiaire | Cible finale | Élément qui rend le chemin praticable | Rupture la moins coûteuse | Prio |
|---|---|---|---|---|---|

**La colonne décisive est l'avant-dernière.** Pour chaque chemin, on ne cherche pas à tout corriger : on cherche **le maillon le moins cher à rompre**. Souvent, ce n'est pas un correctif — c'est une règle de filtrage, un mot de passe local unique par machine, un compte de service dont on retire des droits, ou une console qu'on retire du réseau bureautique.

**Priorisation recommandée** : **P0** pour tout chemin menant à un actif de niveau 0 en trois étapes ou moins ; **P1** au-delà de trois étapes ; **P2** pour les chemins nécessitant un accès physique ou un privilège initial élevé.

### 11.12 🔴 FIL ROUGE — septembre 2026 : l'interface publiée depuis 2022

Claire Nadeau fait réaliser un premier exercice de découverte externe sur les noms de domaine d'HELIOMED. Trois jours de travail, résultat en une page.

**Ce qui est trouvé.**

| Découverte | Origine | Décision |
|---|---|---|
| Interface d'administration de la passerelle d'accès distant, publiée sur Internet | Ouverture réalisée en mars 2022 pendant une période de télétravail massif, jamais refermée | **Fermeture immédiate**, restriction à deux plages d'adresses |
| Environnement de démonstration d'HelioLink, monté pour un salon en 2023 | Hébergé chez un fournisseur externe, facturé sur la carte du service commercial | Contient une copie de données de test réalistes. Extinction sous 15 jours |
| Deux sous-domaines pointant vers des ressources cloud désallouées | Reliquat d'un projet abandonné | Suppression des enregistrements de noms |
| Trois noms d'environnements internes découverts via les journaux de certificats publics | Nommage explicite : recette, administration, sauvegarde | Aucune exposition réelle, mais information offerte à un attaquant. Politique de nommage revue |

**Le chemin d'attaque qui change la priorisation.** L'interface d'administration de la passerelle porte la vulnérabilité de gravité 5,9 identifiée en février (§4.11) — celle que la méthode initiale, fondée sur la gravité, avait écartée. En croisant avec l'exposition, le constat change de nature : vulnérabilité **présente au catalogue d'exploitation avérée**, sur une interface **d'administration**, **publiée sur Internet**, sur un actif d'**entrée**. Trois des quatre critères de la classe C1 sont réunis.

La fermeture de l'exposition est réalisée le jour même, en quarante minutes, sans fenêtre et sans risque de régression pour les utilisateurs — l'accès métier n'était pas concerné. La correction, elle, est planifiée sous 72 heures.

**Ce que Claire présente au comité.** Non pas « nous avons corrigé une vulnérabilité », mais : *nous avons retiré du périmètre exposé quatre actifs, dont un portait une vulnérabilité activement exploitée, et cette fermeture nous protège également des vulnérabilités futures de ces mêmes services*. La distinction n'est pas rhétorique — c'est celle du §11.8, et c'est ce qui débloque le budget de l'exercice de découverte externe récurrent.

**Livrable de l'épisode.** La carte des actifs exposés, la première matrice de chemins d'attaque d'HELIOMED, et une règle de nommage interdisant les noms explicites sur les enregistrements publics.

**Ce qui se joue sans que personne le sache encore.** La passerelle a été exposée pendant quatre ans et demi. La question de savoir si quelqu'un en a profité pendant cette période n'est pas posée en septembre. Elle le sera brutalement au chapitre 21, et elle constitue le point de départ du cas de synthèse A.

→ La suite en 🔴 §12.8, quand il faudra financer la sortie d'obsolescence de ce que cet inventaire a révélé.

→ **Chapitre 12 — Cycle de vie, obsolescence et dette technique** : l'obsolescence, seule menace dont la date est annoncée à l'avance.

### Synthèse mentale du chapitre 11

L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint — et cette information n'est produite par aucun score, elle vient de vous seul. Trois questions la définissent : depuis où, par qui, et vers quoi cet actif mène-t-il. La troisième transforme la liste en graphe, car une compromission réelle est un enchaînement dont la plupart des étapes ne reposent sur aucune vulnérabilité mais sur des choix de configuration et d'identité. Les combinaisons toxiques échappent à tout outil raisonnant constat par constat : quatre règles écrites et une revue trimestrielle les trouvent. Les actifs de niveau 0 sont statistiquement les plus en retard, précisément parce qu'on les croit protégés par leur absence d'exposition externe. Enfin, fermer une exposition inutile est la seule action qui protège aussi contre les vulnérabilités futures du service : elle coûte des minutes, ne nécessite pas de fenêtre, et une part significative des expositions constatées ne correspond plus à aucun besoin actif.

**Trois questions de vérification**

1. Deux serveurs portent la même vulnérabilité critique ; l'un est publié sur Internet, l'autre joignable uniquement depuis un réseau d'administration. Le score de gravité est identique. Qu'est-ce qui doit différencier votre traitement, et d'où vient cette information ?
2. Reconstruisez un chemin d'attaque en quatre étapes qui ne repose sur aucune vulnérabilité logicielle. Quel est le maillon le moins coûteux à rompre ?
3. Votre équipe demande l'ouverture temporaire d'un accès pour une migration de trois semaines. Quelle condition posez-vous, et pourquoi la formuler au moment de la demande plutôt qu'après ?

---

## Chapitre 12 — Cycle de vie, obsolescence et dette technique

### 12.1 Le vocabulaire des fins de support, et ses pièges contractuels

L'obsolescence est la seule menace de ce cours dont la date est **annoncée à l'avance**. C'est aussi celle qui produit le plus de situations subies. Le décalage s'explique en grande partie par un vocabulaire flou, que les éditeurs n'ont aucun intérêt à clarifier.

| Terme | Ce qu'il signifie réellement | Ce que les gens comprennent |
|---|---|---|
| **Fin de commercialisation** | On ne peut plus l'acheter | Souvent confondu avec la fin de support |
| **Fin de vie fonctionnelle** | Plus de nouvelles fonctionnalités, mais correctifs de sécurité maintenus | « C'est fini » — alors que non |
| **Fin de support** | **Plus aucun correctif, y compris de sécurité.** La seule date qui compte pour le MCS | Souvent découverte après coup |
| **Support étendu** | Correctifs de sécurité uniquement, contre paiement, sous conditions strictes | « On pourra prolonger » — sans vérifier l'éligibilité |
| **Fin de support étendu** | Terme absolu | Rarement anticipée |
| **Support de sécurité prolongé par un tiers** | Un acteur autre que l'éditeur maintient des correctifs | Confondu avec un support officiel |

⚠️ **PIÈGE — les cinq clauses qui se découvrent trop tard**

1. **L'éligibilité conditionnelle.** Un support étendu est presque toujours réservé à certaines éditions, certaines versions minimales, certains modes de gestion, certains types de licence. La vérification doit être faite **actif par actif**, pas au niveau du produit.
2. **La tarification croissante.** Beaucoup de programmes voient leur tarif augmenter à chaque année reconduite, souvent en doublant. Un budget calculé sur la première année sous-estime gravement une prolongation de trois ans.
3. **Le prérequis d'état.** Certaines offres exigent que la machine soit déjà à jour d'un niveau de correctif précis au moment de la souscription. Une machine trop en retard peut être **inéligible**, ce qui supprime l'option de repli.
4. **La couverture partielle.** Le support étendu ne couvre en général que les vulnérabilités jugées critiques par l'éditeur, selon ses propres critères. Ce n'est pas un support normal prolongé.
5. **La date de décision.** Souscrire après la fin de support coûte souvent la rétroactivité complète des périodes écoulées — la procrastination est facturée.

✅ **BONNE PRATIQUE (P0)** — Pour chaque option de support étendu envisagée, produisez une note d'une page avant tout arbitrage budgétaire : périmètre exact d'éligibilité **vérifié sur votre parc**, coût sur toute la durée envisagée, ce qui est couvert et ce qui ne l'est pas, et date limite de décision. Cette note évite l'essentiel des mauvaises surprises du domaine.

### 12.2 Construire et tenir un référentiel de fin de support

**L'objectif** : pouvoir répondre à tout moment à la question *« combien d'actifs sortent du support dans les 24 prochains mois, et lesquels ? »*. Sans cette capacité, aucun plan pluriannuel n'est possible.

**Les sources, par fiabilité décroissante :**

| Source | Fiabilité | Remarque |
|---|---|---|
| Page officielle de cycle de vie de l'éditeur | **Fait vérifié** | Seule source opposable ; à consulter, pas à mémoriser |
| Contrat de support signé | Fait vérifié | Peut différer de la politique publique |
| Bases publiques agrégeant les dates de fin de vie | Hypothèse probable | Très pratiques pour le dégrossissage, à confirmer sur les décisions engageantes |
| Connaissance des équipes | Piste exploratoire | Souvent périmée |

**La méthode, en trois temps :**

1. **Extraire** de l'inventaire la liste des systèmes, versions et modèles matériels distincts. Cette liste est bien plus courte que le parc — souvent quelques dizaines de lignes pour plusieurs centaines d'actifs.
2. **Documenter** pour chaque ligne les trois dates : fin de support, fin de support étendu si applicable, source et date de vérification.
3. **Réinjecter** ces dates dans l'inventaire, au niveau de l'actif, pour pouvoir croiser avec la criticité et l'exposition.

⚠️ **PIÈGE — l'obsolescence par composant plutôt que par machine**
Le raisonnement s'arrête trop souvent au système d'exploitation. Or l'obsolescence frappe aussi les moteurs de bases de données, les environnements d'exécution applicatifs, les bibliothèques embarquées, les versions de clusters, les modèles de matériel, les micrologiciels et les certificats. Une machine dont le système est parfaitement supporté peut porter quatre composants hors support — c'est le sujet du chapitre 26.

### 12.3 Le plan de sortie d'obsolescence

Un plan de sortie d'obsolescence n'est pas une liste : c'est une **trajectoire financée**, avec des jalons et un séquencement.

**Les cinq composants d'un plan crédible :**

| Composant | Contenu | Erreur fréquente |
|---|---|---|
| **Trajectoire** | Quels lots, dans quel ordre, sur quels exercices | Tout traiter la même année |
| **Séquencement technique** | Dépendances : migrer l'annuaire avant les applications qui s'y appuient | Découvrir la dépendance en cours de migration |
| **Financement** | Coût par lot, réparti sur les exercices | Un montant global qui ne passe aucun arbitrage |
| **Jalons de décision** | Dates auxquelles une décision doit être prise, y compris de report | Absence de point de contrôle |
| **Plan de repli** | Que fait-on si le lot n'est pas prêt à l'échéance ? | Aucun — donc report subi |

**Le critère de séquencement qui fonctionne.** Ne triez pas par date de fin de support, triez par **produit criticité × exposition × effort**. Un actif hors support depuis deux ans mais isolé et peu critique passe après un actif exposé qui sortira du support dans six mois. La date n'est qu'une des trois entrées.

✅ **BONNE PRATIQUE (P1) — la règle du lot suivant**
À tout moment, le lot en cours doit être financé **et** le lot suivant doit être chiffré. Sans cette règle, chaque lot se négocie isolément et le plan pluriannuel n'existe que sur le papier.

### 12.4 ⏱ Panorama des échéances structurantes

*Bloc périssable, vérifié le 30/07/2026. Le calendrier complet et actualisé figure en **Annexe H**.*

**Les échéances majeures du poste de travail et du serveur Windows :**

| Objet | Date | Point d'attention |
|---|---|---|
| Windows 10 — fin de support | 14 octobre 2025 | Échéance **passée** |
| Windows 10 Entreprise LTSB 2016 — fin de support | 13 octobre 2026 | À ne pas confondre avec le Windows 10 grand public |
| Windows Server 2016 — fin de support étendu | 12 janvier 2027 | Souvent sous-estimée dans les parcs |

**Les échéances récurrentes à surveiller sans date fixe** — et c'est la partie la plus utile de cette section, parce qu'elle reste vraie quand les dates ci-dessus auront été franchies :

- **distributions Linux à support long** : cycles de 5 à 10 ans, avec des options de prolongation par abonnement ;
- **moteurs de bases de données** : cycles de 5 à 8 ans, avec des versions intermédiaires au support beaucoup plus court ;
- **environnements d'exécution applicatifs** : cycles souvent **très courts**, de 2 à 4 ans, et c'est la principale source d'obsolescence invisible (chapitre 26) ;
- **versions de clusters d'orchestration** : de l'ordre de quatorze mois (§3.3) ;
- **équipements réseau et de sécurité** : la fin de support **de sécurité** est souvent antérieure à la fin de vie matérielle — les deux dates doivent être suivies séparément ;
- **matériel serveur** : fin de support des micrologiciels, souvent 5 à 7 ans après la commercialisation.

### 12.5 ⏱ L'économie du support étendu, et un cas d'école

*Bloc périssable, vérifié le 30/07/2026.*

Le cas Windows 10 constitue actuellement l'illustration la plus complète des cinq pièges du §12.1, et il mérite d'être détaillé pour cette raison — le mécanisme vaut bien au-delà de cet éditeur.

**La situation.** Windows 10 est en fin de support depuis le 14 octobre 2025. Deux programmes de prolongation coexistent, et ils n'ont ni le même public, ni le même coût, ni la même échéance.

| Programme | Public | Échéance | Coût |
|---|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | Prolongé jusqu'au 12 octobre 2027 | Gratuit ou faible, selon modalité d'inscription |
| Support étendu **commercial** | Organisations | Jusqu'à trois années après la fin de support | Payant, tarif croissant d'année en année |

⚠️ **LE PIÈGE, et il est majeur.** Le programme grand public **exclut explicitement les machines jointes à un annuaire d'entreprise ou gérées par une solution de gestion de flotte**. Autrement dit : un parc professionnel géré n'est **pas** couvert par la prolongation à octobre 2027, quelle que soit l'édition installée. Une organisation qui lit l'annonce de prolongation et en conclut qu'elle dispose d'un an de plus se trompe de programme — et le découvrira au moment où il sera trop tard pour arbitrer.

📎 [S-24]

**La leçon généralisable, qui survivra à ce cas particulier :**

> Une option de support ne se budgète jamais avant d'avoir vérifié, sur son propre parc et actif par actif, son périmètre d'éligibilité et ses conditions.

**Le calcul à faire systématiquement.** Comparez trois scénarios sur la durée complète, pas sur la première année :

| Scénario | Coûts à intégrer |
|---|---|
| Support étendu sur N années | Coût croissant par actif × N + coût de la migration ensuite, qui reste à payer |
| Migration immédiate | Licences, matériel, tests de compatibilité applicative, formation, charge projet |
| Ne rien faire | Mesures compensatoires, surveillance renforcée, risque accepté, position en cas d'incident ou de contrôle |

Le troisième scénario doit **toujours** figurer dans le tableau, chiffré. C'est en le voyant que les directions arbitrent, et son absence est la raison la plus fréquente pour laquelle un dossier d'obsolescence n'obtient pas de financement.

### 12.6 Mesurer la dette et la présenter à une direction

Le §1.6 a posé le principe. Voici la mise en œuvre.

**Les quatre grandeurs, et leur formulation.**

| Grandeur | Définition | Ce qu'elle démontre |
|---|---|---|
| **Actifs hors support, pondérés par la criticité** | Nombre d'actifs sans correctif disponible, pondéré C1 ×5, C2 ×3, C3 ×1 | L'ampleur structurelle |
| **Vulnérabilités critiques échues** | Constats critiques dont le délai de la classe de service est dépassé | Le retard opérationnel |
| **Dérogations ouvertes et leur âge** | Nombre et ancienneté moyenne | La dette **formellement acceptée** |
| **Âge moyen des constats non traités** | Durée depuis la première détection | La vitesse réelle de l'organisation |

**La présentation qui fonctionne en comité de direction**, en trois diapositives et pas une de plus :

1. **La trajectoire.** L'évolution de la dette sur quatre à huit trimestres. Une direction ne réagit pas à un niveau, elle réagit à une **pente**.
2. **Le point de bascule.** À quelle date, sans décision, la situation se dégrade mécaniquement — typiquement la prochaine échéance de fin de support majeure.
3. **Les trois options chiffrées.** Support étendu, migration, statu quo — avec pour chacune le coût et le risque résiduel.

⚠️ **PIÈGE — présenter la dette sans option**
Une présentation qui expose un problème sans proposer d'options chiffrées produit de l'anxiété, puis de l'évitement. La direction ne peut pas arbitrer ce qu'elle ne peut pas comparer, et l'arbitrage par défaut est le report.

### 12.7 ⚠️ « On migrera l'année prochaine » : mécanique du report perpétuel

Le report est rationnel du point de vue de chaque acteur pris isolément, et c'est pour cela qu'il est si difficile à casser.

| Acteur | Sa logique locale | Pourquoi elle est rationnelle pour lui |
|---|---|---|
| Le métier | « Ça marche, ne touchons à rien » | Il porte le risque d'interruption, pas le risque de sécurité |
| L'exploitation | « Nous n'avons pas la charge disponible » | C'est vrai, et la migration s'ajoute au reste |
| La direction financière | « Décalons d'un exercice » | Un décalage améliore le résultat de l'année en cours |
| L'éditeur métier | « Notre version compatible arrive bientôt » | Il n'a pas d'incitation à accélérer |
| La sécurité | Elle alerte, sans mandat pour trancher | Son alerte n'est pas une décision |

**La somme de comportements localement rationnels produit un résultat collectivement absurde.** Ce n'est pas un problème de personnes, et le traiter comme tel garantit l'échec.

**Les quatre leviers qui cassent réellement le cycle :**

1. **La date de bascule visible.** Rendre publique une date après laquelle le report devient une décision explicite de la direction générale, avec signature. Le report cesse d'être un non-choix.
2. **Le coût du report chiffré chaque année.** Support étendu, mesures compensatoires, heures supplémentaires. Un montant qui réapparaît chaque exercice finit par être comparé au coût de la migration.
3. **L'exigence externe.** Un client, un assureur ou un auditeur qui refuse de valider un système hors support (§7.5).
4. **Le lot pilote.** Migrer un périmètre restreint démontre la faisabilité et produit un chiffrage réel. L'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée ailleurs dans la maison.

### 12.8 🔴 FIL ROUGE — octobre 2026 : 620 postes et une échéance dans quinze jours

Le 13 octobre 2026 approche. HELIOMED est concerné par trois échéances distinctes, et Claire Nadeau commence par les séparer — parce qu'elles ont été confondues pendant six mois.

| Population | Échéance | Situation réelle |
|---|---|---|
| Banc de test de Saint-Étienne, sous Windows 10 Entreprise LTSB 2016 | **13 octobre 2026** | 1 poste, critique pour la validation des pompes PX-40 |
| 620 postes bureautiques Windows 10, joints au domaine, gérés par l'infogérant | Fin de support depuis le 14/10/2025 | **Non éligibles** au programme grand public |
| 11 serveurs Windows Server 2016 | 12 janvier 2027 | Dont 3 portant des applications métier |

**La découverte qui change tout.** Le chargé de compte de l'infogérant Numeria avait indiqué en juin que « la prolongation annoncée par l'éditeur couvre le parc jusqu'en octobre 2027 ». Malik Ferhaoui vérifie ligne à ligne les conditions d'éligibilité, comme le recommande le §12.1 : le programme invoqué est le programme **grand public**, qui exclut les machines jointes au domaine. Les 620 postes n'ont **jamais** été couverts, et ne recevaient plus de correctifs de sécurité depuis douze mois.

Le sujet cesse d'être un sujet de calendrier. Il devient un sujet de responsabilité contractuelle — traité au chapitre suivant.

**Les trois options présentées au comité stratégique.**

| Option | Coût | Risque résiduel |
|---|---|---|
| Support étendu commercial, 2 ans, sur 620 postes | Coût par poste croissant d'une année sur l'autre + coût de la migration ensuite, qui reste dû | Correctifs critiques uniquement, aucun autre bénéfice |
| Migration en trois lots sur 9 mois | Renouvellement partiel du matériel, tests applicatifs, charge projet | Élevé pendant la période de transition, nul ensuite |
| Statu quo | Zéro budget affiché | 620 postes sans correctif, position intenable en cas d'incident ou de contrôle |

Karim Lebrun, directeur financier, tranche en quinze minutes une fois le tableau posé : la première option coûte, sur deux ans, une part significative du coût de la migration — sans en produire aucun bénéfice durable. La deuxième est retenue, avec un support étendu **partiel** limité à 140 postes portant des applications métier non encore validées sur le nouveau système : c'est un pont, chiffré et daté, pas une solution.

**Le cas du banc de test.** Un seul poste, non migrable — l'outil de validation constructeur n'existe pas sur une version plus récente, et le fournisseur a disparu. La décision relève du chapitre 32 : sanctuarisation, retrait du réseau, transferts par support maîtrisé, dérogation signée par le directeur général avec revue semestrielle. Coût de la solution : quelques milliers d'euros de segmentation, contre le coût d'un remplacement complet de la chaîne de validation.

**Livrable de l'épisode.** Un plan de sortie d'obsolescence sur dix-huit mois, en trois lots financés, avec un pont chiffré, une sanctuarisation documentée, et — ce que Claire considère comme le point le plus important — **une note écrite établissant que les 620 postes n'ont pas reçu de correctifs pendant douze mois**, avec sa cause. Cette note sera au cœur de la négociation contractuelle.

→ La suite en 🔴 §13.9, pour la renégociation du contrat d'infogérance.

→ **Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs** : ce qui se passe quand le maintien est confié à un tiers.

### Synthèse mentale du chapitre 12

L'obsolescence est la seule menace dont la date est annoncée à l'avance, et pourtant celle qui produit le plus de situations subies — un vocabulaire flou y contribue, que les éditeurs n'ont pas intérêt à clarifier. Cinq clauses se découvrent trop tard : éligibilité conditionnelle, tarification croissante, prérequis d'état, couverture partielle et rétroactivité. Un référentiel de fin de support se construit sur la liste des versions distinctes, bien plus courte que le parc, et doit couvrir les composants autant que les systèmes. Un plan crédible est une trajectoire financée avec des jalons, séquencée par criticité × exposition × effort plutôt que par date. Le report perpétuel résulte de comportements localement rationnels, ce qui interdit de le traiter comme un problème de personnes : il se casse par une date de bascule visible, un coût de report chiffré chaque année, une exigence externe et un lot pilote. Enfin, tout dossier d'obsolescence doit présenter trois options chiffrées, dont le statu quo — son absence est la première cause de non-financement.

**Trois questions de vérification**

1. Un éditeur annonce la prolongation du support de votre système d'exploitation. Quelles vérifications faites-vous avant d'inscrire cette prolongation dans votre plan, et sur quel niveau de granularité ?
2. Pourquoi trier un plan de sortie d'obsolescence par date de fin de support conduit-il à de mauvaises priorités ? Par quoi remplacez-vous ce critère ?
3. Votre direction a reporté la même migration trois années de suite, chaque fois pour de bonnes raisons. Quels leviers activez-vous, et lequel ne dépend pas d'elle ?

---

## Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs

### 13.1 Ce qui est délégable, et ce qui ne l'est jamais

La délégation est la norme, pas l'exception : parc bureautique confié à un infogérant, applications hébergées chez un éditeur, systèmes industriels maintenus par un constructeur, infrastructure chez un fournisseur cloud. Un programme de MCS qui ne traite que ce que vous exploitez vous-même couvre souvent moins de la moitié du périmètre.

**La distinction fondatrice, à poser une fois pour toutes :**

| Délégable | Jamais délégable |
|---|---|
| L'**exécution** : appliquer les correctifs, tester, redémarrer | La **décision** d'accepter un risque |
| La **détection** : scanner, remonter les constats | La définition des **exigences** : délais, périmètre, criticité |
| La **production de preuve** : rapports, journaux | Le **contrôle** que ces exigences sont tenues |
| L'**expertise** technique sur une plateforme | La **responsabilité** vis-à-vis de vos clients et du régulateur |

**La conséquence pratique**, à énoncer clairement devant toute direction qui pense avoir transféré le sujet avec le contrat : vous pouvez déléguer le travail, vous ne pouvez pas déléguer d'en répondre. Un incident causé par un défaut de mise à jour chez votre prestataire reste votre incident vis-à-vis de vos clients, de vos utilisateurs et de l'autorité de contrôle. Le contrat organise le recours entre vous et lui ; il ne vous exonère pas devant les tiers.

### 13.2 Lire un contrat d'infogérance sous l'angle du MCS

La plupart des contrats d'infogérance sont construits autour de la **disponibilité**. C'est ce que le client demande et ce que le prestataire sait mesurer. La sécurité y figure souvent de manière générale, sans obligation vérifiable.

**Les quatre questions à poser à un contrat existant** — l'exercice prend deux heures et produit systématiquement des surprises :

| Question | Réponse fréquente | Ce qu'elle signifie |
|---|---|---|
| Quel **délai** de correction est engagé, par criticité ? | Aucun, ou « dans les meilleurs délais » | Aucune obligation opposable |
| Quel **périmètre** exact est couvert ? | Flou : « le parc bureautique » | Les exclusions apparaissent au moment du litige |
| Quelles **données** le prestataire doit-il restituer, à quelle fréquence ? | Un rapport de disponibilité mensuel | Vous ne pouvez pas mesurer votre propre conformité |
| Que se passe-t-il en cas de **manquement** ? | Rien de spécifique | L'obligation sans sanction est une intention |

🏢 **VU EN RÉUNION** — Point mensuel avec un infogérant. Le chargé de compte présente 99,94 % de disponibilité, félicitations générales. Le RSSI demande le taux d'application des correctifs. Réponse : « ce n'est pas un indicateur que nous produisons ». Ce n'était pas un refus : personne ne le lui avait jamais demandé, et le contrat ne le prévoyait pas.

⚠️ **PIÈGE — le taux de disponibilité comme indicateur de sécurité**
Un prestataire tenu à 99,9 % de disponibilité a une incitation **contraire** à l'application rapide des correctifs : chaque redémarrage consomme son budget d'indisponibilité, chaque correctif crée un risque de régression dont il porte la pénalité. Sans engagement de sécurité symétrique, le contrat pousse structurellement au report. Ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement.

### 13.3 Les clauses à exiger

Voici le jeu minimal, formulé de manière directement réutilisable. Le modèle complet figure en **Annexe D**.

| # | Clause | Formulation |
|---|---|---|
| 1 | **Délais par criticité** | « Le prestataire applique les correctifs selon les délais suivants, décomptés à partir de la publication du correctif : [reprendre les classes de service du §7.2] » |
| 2 | **Périmètre nominatif** | « Le périmètre couvert est défini par la liste des actifs annexée, mise à jour trimestriellement et contradictoirement » |
| 3 | **Restitution de données** | « Le prestataire fournit mensuellement, dans un format exploitable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables** » |
| 4 | **Notification de vulnérabilité** | « Le prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre, ainsi que toute impossibilité de correction » |
| 5 | **Transparence des versions** | « Le prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence » |
| 6 | **Droit d'audit** | « Le client peut faire réaliser, à sa charge, un contrôle technique du périmètre, avec un préavis de X jours » |
| 7 | **Sous-traitance en cascade** | « Le prestataire déclare ses propres sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations » |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous 5 jours ouvrés, avec sa cause et une proposition de mesure compensatoire » |
| 9 | **Réversibilité** | « En fin de contrat, le prestataire restitue l'inventaire complet, l'historique de mise à jour et la documentation d'exploitation » |
| 10 | **Sanction** | « Le non-respect des délais donne lieu à [pénalité / plan de retour à la conformité sous contrôle] » |

**Les trois clauses qui produisent le plus d'effet**, si vous ne pouvez en obtenir que trois : la **restitution de données** (3), sans laquelle vous ne pouvez rien mesurer ; l'**escalade des impossibilités** (8), qui transforme le silence en obligation ; et la **transparence sur le périmètre** (2), qui empêche le débat sur ce qui était inclus.

✅ **BONNE PRATIQUE (P0)** — La clause 3 est celle à obtenir en priorité, y compris en la négociant seule et en cours de contrat. Sans donnée restituée, votre indicateur affiche « non mesuré » (§10.11) — ce qui est honnête, mais ne réduit aucun risque. Avec la donnée, vous pouvez piloter, y compris sans les autres clauses.

### 13.4 Les référentiels de prestation d'administration et de maintenance

**Le besoin auquel ils répondent.** Un prestataire d'infogérance dispose des accès les plus privilégiés de votre système d'information : comptes d'administration, outils de déploiement, accès distants permanents. Il constitue à ce titre un actif de niveau 0 externalisé — et un chemin d'attaque de premier ordre. Plusieurs compromissions majeures documentées ont emprunté cette voie : compromettre un prestataire pour atteindre l'ensemble de ses clients.

**Ce que ces référentiels encadrent**, indépendamment du schéma considéré : la sécurisation des postes et des accès d'administration du prestataire, la gestion et la traçabilité des comptes à privilèges, le cloisonnement entre les clients, la journalisation des actions d'administration, et les compétences et l'organisation du prestataire.

⏱ **ÉTAT DE L'ART (à vérifier lors de chaque revue)** — En France, un référentiel dédié aux prestataires d'administration et de maintenance sécurisées a été élaboré par l'ANSSI. **Le statut exact du schéma de qualification et la liste des prestataires éventuellement qualifiés doivent être vérifiés directement sur le site de l'agence** : ce type de dispositif évolue, et une information périmée sur ce point peut orienter à tort un choix de prestataire. 📎 [S-15]

**Ce que vous pouvez en faire même sans qualification formelle.** Le référentiel constitue une **grille d'exigences réutilisable** dans un appel d'offres ou un questionnaire fournisseur, indépendamment de tout schéma de certification. Cinq questions en tirent l'essentiel :

1. Les postes utilisés pour administrer notre parc sont-ils dédiés à l'administration, ou servent-ils aussi à la messagerie et à la navigation ?
2. Comment sont gérés les comptes à privilèges utilisés chez nous, et sont-ils propres à notre organisation ?
3. Comment est assuré le cloisonnement entre vos clients ?
4. Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ?
5. Quel est votre propre niveau de maintien en condition de sécurité, et comment le démontrez-vous ?

La cinquième question est celle qui met le plus souvent mal à l'aise. C'est aussi la plus légitime.

### 13.5 Maîtriser le MCS de l'administrateur externe

Le prestataire, en tant que chemin d'accès, mérite un traitement à part — au même titre que les actifs de niveau 0 du §11.7.

**Les cinq points de contrôle :**

| Point | Ce qu'il faut obtenir | Pourquoi |
|---|---|---|
| **Postes d'administration** | Postes dédiés, durcis, à jour, sans usage bureautique | Un poste d'administration qui lit des courriels est un point d'entrée direct vers vos droits les plus élevés |
| **Comptes** | Comptes nominatifs, propres à votre organisation, avec authentification forte | Un compte partagé entre plusieurs clients propage une compromission |
| **Accès distant** | Accès à la demande, borné dans le temps, journalisé | Un accès permanent est une exposition permanente |
| **Journalisation** | Journaux d'actions d'administration accessibles **de votre côté** | Sans cela, vous ne pouvez rien reconstituer après incident |
| **Retrait** | Procédure de retrait des accès au départ d'un intervenant | Les comptes d'anciens intervenants sont un classique des audits |

⚠️ **PIÈGE — l'accès permanent hérité**
Beaucoup d'organisations découvrent, lors d'un premier inventaire des accès, des comptes de prestataires dont le contrat s'est terminé il y a plusieurs années. Le mécanisme est toujours le même : personne ne détient la procédure de retrait, parce qu'elle n'a jamais été écrite. C'est un sujet du chapitre 24, et c'est aussi un sujet de décommissionnement (chapitre 35).

### 13.6 Éditeurs et fournisseurs de services

La délégation ne s'arrête pas à l'infogérance. Chaque éditeur d'application métier, chaque fournisseur de service en ligne, chaque constructeur d'équipement porte une part de votre MCS.

**Les cinq questions à poser à tout fournisseur**, en évaluation comme en revue périodique :

1. **Quelle est votre politique de publication de correctifs de sécurité ?** Fréquence, canaux, délai entre découverte et publication.
2. **Combien de versions maintenez-vous simultanément, et pendant combien de temps ?** C'est ce qui détermine si vous serez contraint à des montées de version subies.
3. **Quel préavis donnez-vous avant une fin de support ?** Six mois est court pour une application métier critique.
4. **Comment nous notifiez-vous une vulnérabilité affectant votre produit ?** Un fournisseur qui ne notifie pas vous laisse découvrir par la presse.
5. **Quels composants tiers votre produit embarque-t-il ?** C'est la question de l'inventaire de composants (§4.8), et elle deviendra réglementaire pour de nombreux produits.

⚠️ **PIÈGE — le prérequis figé**
Certains éditeurs métier conditionnent leur support à une version précise du système d'exploitation, du moteur de base de données ou de l'environnement d'exécution. Vous héritez alors de **leur** calendrier, et vous ne pouvez plus corriger sans perdre le support. C'est l'exigence n° 2 du §6.2 — et elle se négocie avant la signature, jamais après. Une fois l'application déployée et le métier dépendant, votre pouvoir de négociation est nul.

### 13.7 Ce que la réglementation change dans les deux sens

Un effet notable des évolutions réglementaires est de faire circuler les exigences le long de la chaîne d'approvisionnement, dans les deux sens.

**Vers l'amont — ce que vous devez demander.** Si vous êtes soumis à des obligations de maîtrise de votre chaîne d'approvisionnement, vous devez pouvoir démontrer que vous imposez des exigences à vos fournisseurs et que vous les contrôlez. Les clauses du §13.3 ne sont plus seulement de bonne gestion : elles deviennent un élément de preuve.

**Vers l'aval — ce qu'on va vous demander.** Symétriquement, vos clients vous adresseront les mêmes questionnaires. C'est déjà le cas, souvent avant toute obligation légale (§8.1).

✅ **BONNE PRATIQUE (P1) — le dossier fournisseur réutilisable**
Constituez **une fois** un dossier de réponse standard : votre politique MCS, vos classes de service et délais, votre couverture mesurée, votre traitement des exceptions, votre organisation de gestion des incidents. Vous répondrez à 80 % des questionnaires clients par extraction plutôt que par rédaction. C'est le même dossier de preuves que celui du §8.8 — d'où l'intérêt de le construire dans une structure unique.

### 13.8 📌 Limites : l'asymétrie de pouvoir

Tout ce chapitre suppose une capacité de négociation. Elle n'existe pas toujours, et le nier serait malhonnête.

| Situation | Ce qui est réellement possible |
|---|---|
| Fournisseur dominant, contrat d'adhésion non négociable | Aucune clause spécifique. Reste : documenter le risque accepté, exploiter ce que le fournisseur publie déjà, préparer une alternative |
| Petit client d'un grand infogérant | Peu de pouvoir individuel. Levier : le renouvellement, et le groupement avec d'autres clients |
| Éditeur métier en situation de monopole fonctionnel | Négociation faible. Levier : le contrat de maintenance annuel, et la trace écrite des demandes refusées |
| Prestataire en difficulté financière | Le rapport de force s'inverse contre vous : il faut anticiper la réversibilité |

**Ce qui reste toujours possible, quelle que soit l'asymétrie :**

1. **Écrire.** Une demande formalisée, refusée par écrit, change radicalement votre position juridique et votre position en audit.
2. **Mesurer par vous-même** ce que le prestataire ne restitue pas — un scan authentifié de votre côté, si le contrat le permet.
3. **Déclarer non couvert** ce que vous ne pouvez ni mesurer ni imposer (§7.7). C'est ce qui rend le sujet finançable.
4. **Préparer la réversibilité** : un fournisseur qu'on ne peut pas quitter est un fournisseur avec qui on ne négocie pas.

### 13.9 🔴 FIL ROUGE — novembre 2026 : la renégociation

Munie de la note établissant que 620 postes n'ont reçu aucun correctif de sécurité pendant douze mois (§12.8), Claire Nadeau conduit avec Sonia Weber la renégociation du contrat Numeria, dix mois avant son échéance.

**La position initiale du prestataire.** Le contrat de 2023 ne comporte aucun engagement de délai de correction. Le chargé de compte le rappelle : ce qui n'était pas au contrat n'était pas dû. Juridiquement, il n'a pas tort.

**Le levier qui déplace la discussion.** Claire ne conteste pas ce point. Elle expose deux faits : l'information transmise en juin sur l'éligibilité au programme de support étendu était **inexacte**, et cette inexactitude a fondé une décision de report chez HELIOMED. Le sujet cesse d'être « qui devait patcher » pour devenir « quelle information avons-nous reçue ». La négociation change de terrain.

**Ce qui est obtenu à l'avenant, et ce qui ne l'est pas.**

| Demande | Résultat |
|---|---|
| Restitution mensuelle de l'état de mise à jour, actifs non joignables inclus | **Obtenu**, format exploitable, à compter de janvier 2027 |
| Délais de correction par criticité, alignés sur les classes de service | **Obtenu partiellement** : 7 jours pour les vulnérabilités exploitées, 30 jours pour les critiques. Pas d'engagement sur le reste |
| Notification sous 24 h des vulnérabilités exploitées et des impossibilités | **Obtenu** |
| Périmètre nominatif annexé, révisé trimestriellement | **Obtenu** |
| Droit d'audit technique | **Obtenu**, avec préavis de 30 jours et à la charge d'HELIOMED |
| Pénalités financières | **Refusé.** Remplacé par un plan de retour à la conformité sous contrôle en cas de manquement constaté deux mois consécutifs |
| Déclaration des sous-traitants | **Obtenu** |

**La contrepartie.** Numeria obtient une revalorisation d'environ 6 % du contrat, justifiée par la charge de production des rapports et l'engagement de délais. Karim Lebrun valide sans difficulté : le coût annuel supplémentaire représente une fraction de ce qu'aurait coûté le support étendu sur deux ans (§12.8).

**Ce que Claire retient de la négociation**, et qu'elle formalise en règle interne : *aucun périmètre délégué n'entre en service sans clause de restitution de données*. Sans mesure, il n'y a pas de pilotage — seulement de la confiance, ce qui n'est pas une méthode.

**Livrable de l'épisode.** L'avenant contractuel, et la grille de dix clauses du §13.3 versée au référentiel achats d'HELIOMED pour tout futur contrat d'infogérance ou d'hébergement.

→ La suite en 🔴 §14.11, quand la chaîne de veille devra couvrir un périmètre devenu beaucoup plus large que le parc interne.

→ **Chapitre 14 — Veille et sources de constats** : savoir qu'un problème existe — et distinguer les quinze origines de constats.

### Synthèse mentale du chapitre 13

On délègue l'exécution, la détection et la production de preuve ; on ne délègue jamais la décision d'accepter un risque, la définition des exigences, le contrôle, ni la responsabilité devant les tiers. Un contrat construit sur la seule disponibilité pousse structurellement au report des correctifs, puisque chaque redémarrage consomme le budget d'indisponibilité du prestataire — ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement. Dix clauses couvrent le sujet, dont trois sont décisives : restitution de données, escalade des impossibilités, périmètre nominatif. Le prestataire d'administration est un actif de niveau 0 externalisé : postes dédiés, comptes propres à votre organisation, accès bornés, journaux accessibles de votre côté, procédure de retrait écrite. Un prérequis de version imposé par un éditeur métier se négocie avant la signature, jamais après. Enfin, quand l'asymétrie interdit toute négociation, quatre actions restent toujours possibles : écrire, mesurer soi-même, déclarer non couvert, et préparer la réversibilité.

**Trois questions de vérification**

1. Votre infogérant tient un engagement de disponibilité de 99,9 % et n'a aucun engagement de sécurité. Expliquez pourquoi cette configuration retarde mécaniquement les correctifs, sans mettre en cause sa bonne foi.
2. Vous ne pouvez obtenir qu'une seule clause supplémentaire à votre contrat. Laquelle demandez-vous, et pourquoi celle-là plutôt que des pénalités ?
3. Un fournisseur de service en ligne refuse toute modification contractuelle. Que faites-vous concrètement, en quatre actions ?

---

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> - **rédiger** une politique MCS décidable, finançable, et qui prévoit un chemin légitime pour les cas où corriger est impossible ;
> - **construire** des classes de service avec des délais calibrés sur une capacité mesurée, dont une classe explicite pour les actifs non corrigeables ;
> - **lire** un référentiel réglementaire selon la grille exigence / objectif / moyen, et distinguer ce qui oblige de ce qui inspire ;
> - **répartir** les rôles sans faire du RSSI le propriétaire de l'exécution, et pré-arbitrer les conflits récurrents plutôt que les trancher à chaque fois ;
> - **construire** un périmètre de référence en croisant plusieurs sources, et **lire les écarts** plutôt que choisir un chiffre ;
> - **distinguer** ce qui existe de ce qui est atteignable, et reconnaître qu'une fermeture d'exposition protège aussi contre les vulnérabilités futures ;
> - **bâtir** un plan de sortie d'obsolescence financé, et exiger d'un prestataire les trois clauses qui rendent la mesure possible.
>
> **Ce que vous ne savez pas encore** : comment faire tourner la chaîne au quotidien. C'est l'objet de la Partie III.
