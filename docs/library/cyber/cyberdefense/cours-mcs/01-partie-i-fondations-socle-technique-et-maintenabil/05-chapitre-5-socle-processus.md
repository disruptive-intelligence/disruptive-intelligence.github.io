---
title: Chapitre 5 — Socle processus
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

changement, risque, propriété, normes, preuve

Les chapitres 2 à 4 ont installé la technique. Celui-ci installe ce qui, dans la pratique, décide de tout : **qui a le droit de faire quoi, quand, et comment on le prouve**. C'est le chapitre le moins spectaculaire du cours et l'un des plus déterminants — les cinq causes d'échec du §1.4 sont toutes ici.

## 5.1 La gestion du changement, alliée ou frein

**Le principe.** Dans toute organisation structurée, modifier un système en production suppose une autorisation. Cette discipline existe pour une bonne raison : la première cause d'indisponibilité, statistiquement, n'est pas l'attaque, c'est le changement mal maîtrisé.

**Les trois catégories universelles.**

| Catégorie | Définition | Autorisation | Usage en MCS |
|---|---|---|---|
| **Changement standard** | Pré-autorisé, procédure connue, risque évalué une fois pour toutes | Aucune validation au cas par cas | **C'est ici que doit vivre le MCS courant** |
| **Changement normal** | Nouveau ou risqué, examiné individuellement | Comité de validation | Montées de version majeures, changements d'architecture |
| **Changement d'urgence** | Traité hors délai normal, régularisé après | Validation restreinte, souvent a posteriori | Correctif de crise (chapitre 21) |

**L'erreur de conception la plus répandue.** Faire passer chaque campagne de correctifs mensuelle en changement normal. Le résultat est mécanique : le comité devient un goulot d'étranglement, les délais s'allongent, et les équipes finissent par contourner le processus — ce qui détruit à la fois la traçabilité et la confiance.

✅ **BONNE PRATIQUE (P0) — faire du MCS courant un changement standard**
Construisez un dossier de changement standard couvrant votre campagne récurrente : périmètre, procédure, tests, critères d'arrêt, plan de retour arrière, fenêtre. Faites-le valider **une fois**. Ensuite, chaque campagne s'exécute sans repasser en comité, et seuls les cas sortant du cadre y remontent. Vous transformez un frein en accélérateur, sans perdre la traçabilité — au contraire, elle devient homogène.

🏢 **VU EN RÉUNION** — Un comité de changement examine une campagne mensuelle de correctifs. Le représentant métier demande la liste des serveurs concernés, puis : « et si ça casse ? ». L'exploitation répond « on a un instantané ». Le comité valide. Personne n'a demandé combien de temps prend la restauration d'un instantané sur ces serveurs — la réponse était de quarante minutes, et le service avait un engagement de disponibilité de quinze minutes. Le §18.8 existe à cause de ce genre de séance.

⚠️ **PIÈGE — le changement d'urgence qui devient la norme**
Quand le processus standard est trop lourd, tout devient une urgence. Symptôme mesurable : la part des changements d'urgence dans le total. Au-delà de 15 à 20 %, ce n'est plus un indicateur de réactivité, c'est le signe que votre processus normal ne fonctionne pas. Suivez ce ratio (chapitre 38).

## 5.2 Fenêtres, gels et calendriers métier

**La fenêtre de maintenance** est un créneau pendant lequel une interruption est acceptée par les métiers. C'est une ressource rare, et le MCS n'en est pas le seul consommateur : projets, montées de version applicatives, opérations d'infrastructure s'y disputent la place.

**Trois principes de négociation qui fonctionnent.**

1. **Négocier des fenêtres récurrentes, pas des interventions.** Obtenir « le deuxième jeudi de chaque mois, de 22 h à 2 h » une seule fois vaut mieux que douze négociations annuelles. Chaque négociation individuelle a un coût, et ce coût produit du report.
2. **Différencier par criticité.** Un actif de niveau 0 mérite une fenêtre courte et fréquente ; un serveur secondaire peut se contenter d'une fenêtre trimestrielle plus large. Les classes de service du chapitre 7 formalisent ce découpage.
3. **Prévoir la fenêtre d'urgence dès maintenant.** Le jour de la crise, personne n'a le temps de négocier. Faites acter à l'avance : *en cas de vulnérabilité exploitée sur un actif exposé, l'interruption est autorisée sous délai de X heures, par décision de Y.* C'est une décision de gouvernance qui se prend à froid (chapitre 9).

**Les gels de production.** Périodes où tout changement est interdit : clôture comptable, campagne commerciale, fin d'année, pic saisonnier. Elles sont légitimes et non négociables sur le principe. Deux points d'attention :

- Un gel n'est **jamais** absolu en sécurité : il doit comporter une clause explicite de levée pour vulnérabilité exploitée, avec le décideur nommé.
- L'accumulation des gels peut réduire l'année à quelques semaines réellement disponibles. Faites le calcul et présentez-le : *« nous disposons de 14 semaines exploitables sur 52 »* est un argument autrement plus efficace qu'une demande de moyens.

## 5.3 Analyse de risque appliquée au MCS

Vous n'avez pas besoin d'être expert en analyse de risque pour faire du MCS. Vous avez besoin de trois notions.

**Le risque résiduel.** Ce qui reste après application des mesures. Il n'est jamais nul, et le reconnaître explicitement est un acte de maturité, pas un aveu de faiblesse. Un programme de MCS qui prétend supprimer le risque est un programme qui ment à sa direction.

**L'acceptation formalisée.** Décider de ne pas corriger est une décision légitime — **à condition** qu'elle soit prise par la bonne personne, écrite, datée, bornée dans le temps, assortie de mesures compensatoires et revue à échéance. Non formalisée, c'est un oubli ; formalisée, c'est une décision de gestion. La différence entre les deux est ce que regarde un auditeur, et ce que regarde un juge.

**La méthode structurée, quand elle est utile.** Les démarches d'analyse de risque par ateliers successifs — cadrage et socle de sécurité, identification des sources de risque, scénarios stratégiques, scénarios opérationnels, traitement — apportent au MCS deux choses précises : elles obligent à nommer **qui** vous attaquerait et **pourquoi**, ce qui oriente la priorisation vers les chemins réellement plausibles ; et elles produisent une échelle de gravité **métier**, indispensable pour transformer une criticité technique en criticité d'actif.

⚠️ **PIÈGE — l'analyse de risque comme préalable bloquant**
N'attendez pas une analyse complète pour démarrer un programme de MCS. Une classification de criticité à trois niveaux, imparfaite mais appliquée, vaut infiniment mieux qu'une analyse exhaustive attendue pendant dix-huit mois. Commencez avec ce que vous avez, affinez ensuite.

## 5.4 Lire une exigence de conformité : la grille en trois niveaux

Vous allez rencontrer des référentiels — normes, réglementations, référentiels sectoriels, questionnaires clients. Une seule grille de lecture suffit à ne jamais s'y perdre.

| Niveau | Question | Exemple générique | Qui le fixe |
|---|---|---|---|
| **Exigence** | Que dois-je obtenir ? | « Les vulnérabilités techniques doivent être identifiées et traitées en temps utile » | Le texte |
| **Objectif de sécurité** | Quel résultat concret cela suppose-t-il ? | « Détecter les vulnérabilités du parc et les corriger selon des délais définis par criticité » | Le référentiel d'application |
| **Moyen de conformité** | Comment je le fais chez moi ? | « Scan authentifié mensuel, arbre de décision, délais de 7/30/90 jours, dérogations tracées » | **Vous** |

**Les deux erreurs symétriques.**

- **Confondre exigence et moyen** : croire qu'un texte impose un outil ou une fréquence précise. C'est presque toujours faux — les textes fixent des résultats, pas des implémentations. Cela vous laisse une liberté que beaucoup n'exploitent pas.
- **Croire que le moyen suffit** : avoir un scanner et une procédure ne démontre rien. Ce qui est évalué, c'est le **résultat** et sa **preuve**.

Le principe de **proportionnalité** figure dans la plupart des référentiels modernes : les mesures attendues sont proportionnées à la taille de l'organisation, à son exposition et à la criticité de ses activités. C'est un levier de négociation légitime, à condition d'être capable de **justifier** votre calibrage — donc de l'avoir écrit.

## 5.5 La propriété d'actif : la question qui débloque tout

Nous arrivons à la cause d'échec n° 2 du §1.4, et sans doute à la phrase la plus utile de ce cours.

> Pour chaque actif, une seule question doit avoir une réponse **nominative** : *qui décide qu'on l'arrête pour le corriger ?*

**Pourquoi cette formulation.** « Qui est responsable de ce serveur ? » obtient des réponses floues et collectives. « Qui décide de l'arrêter ? » n'admet qu'un nom. Et c'est exactement la décision qui bloque en pratique.

**Les cinq rôles à distinguer**, parce que les confondre produit l'essentiel des blocages :

| Rôle | Ce qu'il fait | Ce qu'il ne fait pas |
|---|---|---|
| **Propriétaire métier** | Décide de l'interruption, arbitre le risque, porte le budget | Il n'exécute pas |
| **Propriétaire technique** | Exploite, applique, vérifie, produit la preuve | Il ne décide pas de l'arrêt |
| **Éditeur / constructeur** | Produit le correctif, définit les prérequis | Il ne connaît pas votre contexte |
| **Intégrateur** | A construit le système, connaît ses dépendances | Il n'est souvent plus là |
| **Infogérant** | Exécute selon contrat | **Il ne porte jamais la décision d'accepter un risque** (chapitre 13) |

⚠️ **PIÈGE — la propriété collective**
« C'est l'équipe infrastructure » n'est pas une réponse. Une équipe ne prend pas de décision d'interruption à 3 h du matin ; une personne le fait. Exigez un nom, et un suppléant. Sans cela, votre programme s'arrêtera au premier arbitrage.

✅ **BONNE PRATIQUE (P0) — la campagne de désignation**
Nommer les propriétaires est un exercice de trois à six semaines, pas un projet. Méthode qui fonctionne : extraire la liste des actifs, proposer un propriétaire pressenti pour chacun, envoyer la liste aux responsables concernés avec une règle explicite — *sans retour sous quinze jours, la désignation proposée est réputée acceptée*. Le silence devient une acceptation, et la liste se remplit. Les actifs pour lesquels personne ne se reconnaît sont votre priorité réelle : ce sont les **actifs orphelins**, et ils sont presque toujours ceux qui posent problème.

🔴 **FIL ROUGE — mars 2026 : trois noms et un refus**

Claire Nadeau lance la campagne de désignation sur les 221 actifs du périmètre de référence. Trois retours illustrent tout le chapitre.

**Le cas simple.** Sonia Weber, directrice des systèmes d'information, accepte d'être propriétaire métier des serveurs d'infrastructure centraux et désigne Malik Ferhaoui comme propriétaire technique. Fenêtre récurrente négociée : deuxième jeudi du mois, 22 h - 2 h. Pour ces actifs, le MCS devient un changement standard dès avril.

**Le cas de la négociation.** Thomas Berger refuse d'être désigné propriétaire des onze postes de supervision de l'usine tant qu'aucune fenêtre n'est définie : « je ne peux pas m'engager sur quelque chose que je n'ai pas le droit d'arrêter ». Il a raison, et sa réponse est plus constructive qu'une acceptation de façade. La discussion aboutit à un compromis : il devient propriétaire, avec une fenêtre unique lors de l'arrêt de production d'août, et l'engagement écrit que toute intervention hors de cette fenêtre relève d'une décision de la direction générale, pas de la sécurité.

**Le cas révélateur.** Vingt-neuf actifs ne trouvent aucun propriétaire — l'essentiel des machines de test non déclarées et des appliances virtuelles d'éditeurs. Personne ne les revendique, et personne ne demande non plus leur arrêt. Claire applique une règle qui deviendra structurante : *tout actif orphelin depuis plus de trente jours entre dans une procédure d'extinction programmée, avec préavis de quinze jours diffusé largement.* Sur les vingt-neuf, onze trouvent immédiatement un propriétaire — le préavis a réveillé leurs utilisateurs. Huit sont éteints sans conséquence. Dix relèvent d'un décommissionnement en règle (chapitre 35).

**Décision prise.** La désignation nominative devient un prérequis d'entrée en production : aucun nouvel actif n'est mis en service sans propriétaire métier et propriétaire technique nommés.

**Livrable de l'épisode.** Le référentiel de propriété, intégré à la base d'inventaire — les champs correspondants figurent en Annexe I.

→ La suite en 🔴 §6.15, quand ces engagements rencontrent une architecture qui ne permet pas de les tenir.

## 5.6 Ce qui a valeur de preuve, et ce qui n'en a pas

Le §2.9 a posé les six champs d'une preuve technique. Élargissons au niveau organisationnel.

| Élément | Valeur probante | Condition |
|---|---|---|
| Politique écrite et validée | Faible seule, indispensable en support | Datée, versionnée, approuvée nominativement |
| Compte rendu de comité | Bonne pour les **décisions** | Décisions explicites, pas un relevé de discussion |
| Extraction d'outil | Bonne pour l'**état** | Datée, périmètre défini, non retouchée, actifs injoignables listés |
| Journal système | Forte | Horodaté, intègre, conservé |
| Fiche de dérogation | Forte pour justifier une **non-action** | Signataire, durée, mesure compensatoire, date de revue |
| Déclaration orale ou courriel | Nulle | — |

**La règle qui résume tout** : une preuve répond à *qui, quoi, quand, sur quel périmètre, et qu'est-ce qui manque*. Le dernier terme est celui qui distingue un professionnel d'un amateur — un rapport qui n'énonce pas ses trous est un rapport qu'on ne peut pas croire.

## 5.7 Trois familles d'indicateurs à ne pas confondre

Dernière notion du socle, et source d'innombrables tableaux de bord inutiles.

| Famille | Question | Exemple | Piège |
|---|---|---|---|
| **Activité** | Qu'avons-nous fait ? | Nombre de correctifs déployés ce mois | Récompense l'agitation ; ne dit rien du résultat |
| **Résultat** | Où en sommes-nous ? | Part des actifs critiques conformes, sur périmètre de référence | Nécessite un dénominateur solide |
| **Risque** | Que craignons-nous ? | Nombre d'actifs exposés portant une vulnérabilité exploitée | Le seul qui parle à une direction générale |

⚠️ **PIÈGE — l'indicateur qui récompense l'inaction**
« Nombre de vulnérabilités détectées » est un indicateur d'activité déguisé en indicateur de risque. Il s'améliore quand vous scannez moins. C'est l'archétype de la métrique qu'il ne faut pas présenter à un comité — le chapitre 38 en recense une dizaine d'autres, et l'Annexe K fournit les définitions rigoureuses.

→ **Chapitre 6 — Architecture maintenable : le MCS *by design*** : la conception — parce que le coût du MCS se décide avant la mise en service.

## Synthèse mentale du chapitre 5

Le MCS courant doit vivre en changement standard, pré-autorisé une fois pour toutes : le faire passer en comité à chaque campagne transforme la gouvernance en goulot d'étranglement et pousse les équipes à contourner le processus. Les fenêtres se négocient de façon récurrente et différenciée par criticité, et la fenêtre d'urgence se décide à froid, jamais pendant la crise. Décider de ne pas corriger est légitime dès lors que la décision est prise par la bonne personne, écrite, bornée, compensée et revue — c'est ce qui sépare un oubli d'une décision de gestion. Face à un référentiel, distinguez l'exigence, l'objectif et le moyen : les textes fixent des résultats, le moyen vous appartient, et c'est le résultat prouvé qui est évalué. La question qui débloque le plus de situations n'est pas « qui est responsable ? » mais « qui décide qu'on l'arrête ? », et elle n'admet qu'un nom. Enfin, une preuve dit qui, quoi, quand, sur quel périmètre — et ce qui manque.

**Trois questions de vérification**

1. Votre campagne mensuelle de correctifs passe en comité de validation à chaque itération et accuse trois semaines de retard moyen. Que changez-vous, et qu'obtenez-vous en échange de cette simplification ?
2. Un référentiel exige que « les vulnérabilités techniques soient traitées en temps utile ». Votre direction vous demande quel outil il faut acheter. Que répondez-vous ?
3. Quinze actifs de votre parc n'ont aucun propriétaire identifié depuis quatre mois. Quelle procédure appliquez-vous, et pourquoi le préavis est-il l'élément clé du dispositif ?

---
