---
title: 'Chapitre 4 — Socle vulnérabilités : identifiants, scores, écosystème'
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

> ⚠️ **Avant de commencer.** Ce chapitre présente une dizaine de sigles en quelques pages. **N'essayez pas de les mémoriser à la première lecture.** Quatre d'entre eux suffisent au travail quotidien — ils sont identifiés au §4.10 — et les autres se consultent au besoin. Ce qui compte ici n'est pas de retenir les acronymes, c'est de comprendre **quelle question chacun répond, et laquelle il ne répond pas**.

Ce chapitre est le pivot du cours. Il installe le vocabulaire que tout le reste utilise, et il vous apprend surtout à **ne pas croire les chiffres** que produit cet écosystème — non parce qu'ils mentent, mais parce qu'ils ne mesurent presque jamais ce qu'on croit qu'ils mesurent.

Aucune connaissance préalable n'est supposée. Si vous n'avez jamais lu un bulletin de sécurité, vous saurez le faire à la fin.

## 4.1 Vocabulaire : six mots qu'on confond en permanence

| Terme | Définition précise | Ce qu'il n'est pas |
|---|---|---|
| **Faiblesse** | Un type de défaut de conception ou de programmation, décrit indépendamment de tout produit — par exemple « absence de vérification des droits avant une action » | Ce n'est pas une faille dans un logiciel précis |
| **Vulnérabilité** | L'instance concrète d'une faiblesse dans un produit et une version donnés | Ce n'est pas un risque : elle peut être inatteignable chez vous |
| **Exposition** | Le fait qu'un attaquant puisse **atteindre** le composant vulnérable | Une vulnérabilité sans exposition n'est pas exploitable |
| **Exploit** | Le code ou la procédure qui transforme la vulnérabilité en effet concret | Son existence publique ne prouve pas qu'il fonctionne partout |
| **Exploitation active** | L'observation, dans le monde réel, d'attaquants utilisant cette vulnérabilité | Ce n'est pas la simple existence d'un exploit |
| **Risque** | La combinaison vulnérabilité × exposition × exploitation × impact métier | Ce n'est jamais un score technique isolé |

Deux termes de calendrier viennent s'y ajouter, souvent employés à contresens :

- **0-day** : vulnérabilité pour laquelle **aucun correctif n'existe** au moment où elle est connue ou exploitée. L'éditeur a eu « zéro jour » pour corriger. Ce n'est pas synonyme de « très grave ».
- **n-day** : vulnérabilité pour laquelle un correctif existe depuis n jours. C'est **l'écrasante majorité des compromissions réelles** : les attaquants exploitent surtout ce qui est corrigé mais non appliqué. Retenez cette asymétrie, elle justifie à elle seule l'existence de ce cours.

⚠️ **PIÈGE — « c'est une 0-day » comme justification d'inaction**
Beaucoup d'organisations se rassurent en se disant qu'elles ne peuvent rien contre les 0-day. C'est vrai — et hors sujet, parce que ce n'est pas par là qu'elles se font attaquer. Le MCS traite les n-day, c'est-à-dire le cas où **vous aviez le correctif et ne l'avez pas appliqué**.

## 4.2 CVE : comment un identifiant naît, et pourquoi sa qualité varie

**Le besoin.** Sans identifiant commun, votre scanner, votre éditeur, votre prestataire et votre auditeur parlent de la même faille avec quatre noms différents. Le programme CVE (*Common Vulnerabilities and Exposures*) résout ce problème : un identifiant unique, de la forme `CVE-2026-12345`.

**Ce qu'un identifiant CVE est, exactement.** Une **clé de dédoublonnage**. Rien de plus. Il ne dit pas si la faille est grave, ni si elle est exploitée, ni si elle vous concerne.

**Qui les attribue.** Des organisations accréditées appelées **CNA** (*CVE Numbering Authorities*) : éditeurs de logiciels pour leurs propres produits, centres de réponse aux incidents, projets open source, chercheurs. Elles reçoivent un bloc d'identifiants et les attribuent de façon autonome.

C'est ce point qui explique la variabilité de qualité, et il faut le comprendre pour ne pas s'étonner ensuite :

| Ce qui varie selon la CNA | Conséquence pratique |
|---|---|
| Le niveau de détail de la description | Certaines fiches disent tout, d'autres une ligne vague |
| La présence et la justesse des versions affectées | Sans versions précises, aucune corrélation automatique n'est possible |
| L'attribution ou non d'un score de gravité | Deux CNA peuvent scorer différemment la même classe de défaut |
| La rapidité de publication | Certaines publient avant le correctif, d'autres bien après |
| La granularité | Un éditeur peut regrouper dix défauts sous un identifiant, un autre en créer dix |

**Le cycle de vie d'une fiche.** Réservation d'un identifiant → publication de la fiche → enrichissements successifs (versions, références, scores) → parfois contestation, rejet ou fusion. Une fiche consultée le jour de sa publication et la même fiche trois semaines plus tard peuvent être très différentes.

✅ **BONNE PRATIQUE (P1)** — Ne figez jamais une décision de triage sur la première version d'une fiche publiée dans les 48 heures. Prévoyez explicitement un **rejeu** des constats récents : ce qui semblait mineur lundi peut être requalifié vendredi.

## 4.3 Nommer les produits

CWE, CPE, purl — et pourquoi la corrélation échoue

Trois nomenclatures cohabitent, avec des rôles distincts.

**CWE — la nature du défaut.** Un catalogue de *types* de faiblesses : injection, débordement, mauvaise gestion des droits, condition de course. Une CVE peut être rattachée à une ou plusieurs CWE lorsque la nature de la faiblesse est connue et correctement renseignée — ce qui n'est pas systématique : certaines fiches n'ont pas de rattachement fiable, d'autres portent une catégorie générique, d'autres encore sont enrichies après publication. Utilité pour le MCS : repérer qu'un même type de défaut revient chez le même fournisseur, ce qui est un signal de qualité du produit — et un argument contractuel (chapitre 13).

**CPE — l'identification d'un produit.** Une chaîne normalisée décrivant éditeur, produit, version, édition. C'est ce qui permet à un outil de dire « la CVE affecte ce produit, or ce produit est installé ici ».

📌 **LIMITES — pourquoi la corrélation par CPE produit tant de bruit**

- Le nom du produit dans la fiche CVE et le nom du paquet installé sur votre machine ne se ressemblent pas toujours.
- Les intervalles de versions affectées sont souvent exprimés de manière imprécise, ou pas du tout.
- Le rétroportage (§2.2) rend la comparaison de version fausse par construction sur les systèmes à support long.
- Un même logiciel peut exister sous plusieurs identifiants selon qui l'a déclaré.
- Les composants embarqués dans une application n'ont généralement aucun identifiant produit.

**purl — l'identification d'un paquet logiciel.** Une notation plus récente et beaucoup plus adaptée aux écosystèmes de développement, de la forme `pkg:type/espace-de-noms/nom@version`. Elle décrit sans ambiguïté un paquet dans son écosystème d'origine. Il est largement utilisé dans les inventaires de composants logiciels modernes (§4.8), là où CPE reste le format historique des bases de vulnérabilités — avec une couverture qui varie selon les formats et les outils.

Retenez la conséquence opérationnelle : **une part importante des faux positifs de vos scanners ne vient pas de leur mauvaise qualité, mais de l'impossibilité structurelle de faire correspondre parfaitement deux nomenclatures conçues pour des usages différents.** Le chapitre 15 en fait un chapitre entier.

## 4.4 CVSS : ce que le score mesure, et ce qu'on lui fait dire

**CVSS** (*Common Vulnerability Scoring System*) attribue une note de 0 à 10. C'est le chiffre que tout le monde connaît, et le plus mal utilisé du domaine.

**Ce qu'il mesure.** La **gravité technique intrinsèque** d'une vulnérabilité : à quel point elle est difficile à exploiter, quels privilèges elle exige, quelle interaction utilisateur elle suppose, et quels impacts elle produit sur la confidentialité, l'intégrité et la disponibilité du composant touché.

**La structure, en quatre groupes.**

| Groupe | Contenu | Qui le renseigne |
|---|---|---|
| **Base** | Caractéristiques intrinsèques et invariantes de la vulnérabilité | L'éditeur ou la CNA |
| **Menace** | Maturité du code d'exploitation à un instant donné | Rarement renseigné en pratique |
| **Environnement** | Adaptation à **votre** contexte : criticité de l'actif, mesures déjà en place | **Vous** — et presque personne ne le fait |
| **Complémentaire** | Informations qualitatives (sûreté, automatisabilité, récupérabilité) | Optionnel |

La version 4 du standard a notamment clarifié la distinction entre l'impact sur le **système vulnérable** et l'impact sur les **systèmes en aval**, et introduit une notation explicite indiquant quels groupes ont été utilisés — un score « base seule » n'a pas le même statut qu'un score enrichi de la menace et de l'environnement.

⚠️ **PIÈGE — les cinq erreurs d'interprétation les plus coûteuses**

| Erreur | Pourquoi c'est faux |
|---|---|
| « Score 9,8 = à corriger en priorité » | Le score de base ignore totalement votre exposition. Une faille 9,8 sur un service désactivé n'est pas un risque |
| « Score 5,3 = pas urgent » | Certaines failles de gravité moyenne sont massivement exploitées parce qu'elles sont triviales à automatiser |
| « Le score est objectif » | Il est calculé à partir de choix humains dans une grille. Deux analystes peuvent diverger |
| « Le score évolue avec la menace » | Le groupe Base est conçu pour être stable dans le temps : il ne reflète pas l'apparition d'un exploit public. Un vecteur publié peut néanmoins être corrigé ou révisé par son émetteur |
| « C'est la même chose qu'un niveau de risque » | Il manque l'exposition, la criticité métier et l'impact organisationnel |

> ### 🎯 La phrase à retenir de ce chapitre
> **CVSS décrit la gravité technique d'une vulnérabilité. Il ne décrit pas votre priorité opérationnelle.**
> Toute la suite du cours découle de cette distinction.

**Le bon usage.** CVSS mesure une **sévérité**, pas un risque — la documentation du standard le dit explicitement 📎 [S-18]. Il répond à la question « **quelle est la gravité technique si cette faille est exploitée ?** ». C'est une entrée utile parmi d'autres. Il ne répond ni à « est-ce exploité ? », ni à « suis-je atteignable ? », ni à « qu'est-ce que ça me coûte ? ».

## 4.5 EPSS : la probabilité, et ses angles morts

**EPSS** (*Exploit Prediction Scoring System*) répond à une question différente et complémentaire : **quelle est la probabilité que cette vulnérabilité soit exploitée dans les trente prochains jours ?**

Le résultat est un nombre entre 0 et 1, accompagné d'un **percentile** indiquant la position relative de la vulnérabilité par rapport à toutes les autres.

**Ce qui change tout.** La distribution est extrêmement asymétrique : l'immense majorité des vulnérabilités publiées ont une probabilité d'exploitation très faible, et une petite fraction concentre presque tout le risque réel. C'est précisément ce qui rend une priorisation par gravité seule inefficace : elle traite comme équivalentes des milliers de vulnérabilités qui ne seront jamais exploitées et quelques dizaines qui le seront.

🧪 **EN PRATIQUE — lire correctement un couple de valeurs**
Une vulnérabilité à 0,08 de probabilité et 96ᵉ percentile signifie : *il y a environ 8 % de chances qu'elle soit exploitée dans les trente jours, et elle est malgré tout plus menaçante que 96 % des autres.* Les deux informations sont nécessaires : la probabilité pour dimensionner l'effort, le percentile pour arbitrer entre constats.

📌 **LIMITES — ce qu'EPSS ne sait pas**

- Il prédit l'exploitation **dans le monde**, pas chez vous. Il ignore totalement votre exposition et votre criticité métier.
- Il repose sur des signaux observables : une exploitation ciblée, discrète, contre un petit nombre d'organisations est mal captée par construction.
- La **transparence est partielle** : la méthode générale et les principes du modèle sont publics, mais le consommateur ne dispose ni des données d'entraînement, ni des poids, ni des signaux ayant produit un score donné — il ne peut donc ni reproduire ni auditer une valeur particulière.
- La probabilité est **volatile** : elle monte brutalement à la publication d'un exploit, puis redescend. Un score consulté il y a trois semaines n'a pas de valeur.

⚠️ **PIÈGE — la discontinuité entre versions de modèle**
Le modèle évolue par versions successives, et un changement de version **déplace tous les scores en même temps**. Conséquence directe et sous-estimée : une série temporelle qui traverse un changement de version n'est pas comparable. Si votre indicateur « nombre de vulnérabilités à forte probabilité » chute de 30 % en une semaine sans qu'aucun correctif n'ait été appliqué, cherchez d'abord un changement de modèle avant de féliciter vos équipes.

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — La version 5 du modèle a commencé à publier ses scores le **15 juin 2026**. Toute série historique franchissant cette date doit être signalée comme discontinue dans vos tableaux de bord. 📎 [S-17]

## 4.6 Les catalogues d'exploitation avérée

Un troisième signal, de nature complètement différente : non plus une prédiction, mais un **constat**.

L'agence américaine de cybersécurité maintient un catalogue de vulnérabilités **connues comme exploitées** (couramment appelé catalogue KEV). Trois critères d'inscription : un identifiant CVE attribué, une **preuve fiable d'exploitation active**, et une action de remédiation claire disponible.

**Pourquoi c'est un signal très fort.** Il n'y a ni probabilité, ni modèle, ni interprétation : quelqu'un a observé l'exploitation. En pratique, l'appartenance à ce catalogue est l'un des meilleurs déclencheurs d'une procédure d'urgence — mais pas un déclencheur suffisant à lui seul, puisqu'il ne couvre ni immédiatement les campagnes ciblées, ni les vulnérabilités sans identifiant.

📌 **LIMITES — ce que le catalogue ne dit pas**

- **Il est incomplet par construction.** Il recense ce qui a été observé **et** publié. Les attaques ciblées contre un secteur, ou celles détectées sans être divulguées, n'y figurent pas.
- **Il est en retard.** L'inscription suit l'observation, qui suit l'exploitation. Ne pas y figurer ne signifie pas « pas exploité », mais « pas encore observé publiquement ».
- **Il est orienté par son public.** Il sert d'abord les administrations américaines ; les produits dominants dans d'autres marchés peuvent y être sous-représentés.
- **Il ne dit rien de votre exposition.** Une vulnérabilité massivement exploitée sur un produit que vous n'utilisez pas ne vous concerne pas.

⚠️ Ne construisez jamais une doctrine du type « nous ne traitons en urgence que ce qui figure au catalogue ». Vous obtiendriez un processus lisible, défendable — et systématiquement en retard sur les campagnes visant votre secteur.

## 4.7 Décider plutôt que scorer : les approches par arbre de décision

Un score produit un nombre ; il faut ensuite décider quoi en faire. Les approches par **arbre de décision** franchissent directement l'étape suivante : elles produisent une **action**.

Le principe est simple et transposable à n'importe quelle organisation. On pose quelques questions binaires ou ternaires, dans un ordre fixé, et chaque combinaison de réponses mène à une décision explicite.

🧪 **EN PRATIQUE — la structure d'un arbre de décision de remédiation**

```
1. Exploitation observée ?        aucune / démonstration publique / active
2. Automatisable à grande échelle ?              oui / non
3. Impact technique en cas de succès ?      partiel / total
4. Effet sur les missions et les personnes ?  faible / … / critique
                       ↓
       Surveiller · Surveiller de près · Traiter · Agir en urgence
```


L'intérêt majeur de cette forme est qu'elle est **auditable** : on ne discute plus d'un chiffre, on discute des réponses aux questions. Et le jour où vous devez justifier de ne pas avoir corrigé, vous produisez le chemin parcouru dans l'arbre plutôt qu'un seuil arbitraire.

Une approche complémentaire, plus récente, consiste à estimer la probabilité qu'une vulnérabilité **ait déjà été exploitée par le passé**, en agrégeant l'historique des prédictions plutôt qu'en regardant leur valeur du jour. Elle répond à une limite réelle des catalogues d'exploitation avérée — leur incomplétude — sans prétendre la supprimer.

✅ **BONNE PRATIQUE (P0)** — Quelle que soit la méthode retenue, **écrivez-la**. Une règle de priorisation non écrite est une règle qui varie selon la personne, la fatigue et le mois. Le modèle complet est construit au chapitre 16 et formalisé en Annexe C.

## 4.8 De l'inventaire logiciel à l'exploitabilité déclarée

SBOM, VEX, CSAF

Trois briques récentes, souvent confondues, qui répondent à trois questions distinctes.

| Brique | Question à laquelle elle répond | Produite par |
|---|---|---|
| **SBOM** | *Que contient ce logiciel ?* | Le fournisseur, ou vous, à la construction |
| **VEX** | *Ce composant vulnérable rend-il ce produit exploitable ?* | Le fournisseur du produit |
| **CSAF** | *Comment publier un avis de sécurité lisible par une machine ?* | L'éditeur qui publie l'avis |

**SBOM** — l'inventaire des composants d'un logiciel, avec leurs versions et leurs relations de dépendance. Deux formats principaux coexistent, tous deux largement outillés. L'enjeu n'est pas de choisir : c'est de savoir **quoi en faire**. Un inventaire de composants que personne ne rapproche d'une base de vulnérabilités est un document mort.

**VEX** — la réponse à un problème très concret. Votre outil détecte un composant vulnérable dans un produit ; le fournisseur sait, lui, que le code vulnérable n'est jamais appelé dans son produit. Un document VEX transporte cette information sous une forme exploitable, avec quatre états possibles : *non affecté*, *affecté*, *corrigé*, *en cours d'analyse* — et, pour l'état « non affecté », une justification normalisée.

**CSAF** — le format d'avis de sécurité lisible par une machine. Il permet d'automatiser ce qui est aujourd'hui fait à la main : lire un bulletin, en extraire les produits et versions concernés, les rapprocher de l'inventaire.

📌 **LIMITES — l'écart entre la promesse et la réalité de terrain**
La production de ces documents progresse plus vite que leur consommation. Beaucoup d'organisations reçoivent des inventaires de composants qu'elles archivent sans jamais les exploiter, faute d'outillage ou de processus. Un inventaire fourni n'est utile que s'il est **à jour**, **rapproché de l'inventaire d'actifs**, et **rejoué à chaque nouvelle vulnérabilité publiée** — trois conditions rarement réunies. Le chapitre 25 traite la mise en œuvre réelle.

## 4.9 ⏱ L'écosystème des données de vulnérabilités au 30 juillet 2026

*Bloc périssable. Vérifié le 30/07/2026.*

Le point à comprendre est structurel, et il survivra aux détails ci-dessous : **l'écosystème s'est fragmenté**, et la dépendance à une source unique est devenue un risque opérationnel.

**Ce qui a changé.**

- Le NIST a annoncé qu'à compter du **15 avril 2026**, l'enrichissement des fiches de sa base nationale serait **priorisé** : vulnérabilités connues comme exploitées, logiciels utilisés par l'administration fédérale américaine, logiciels critiques. Formulation exacte, importante : **toutes les vulnérabilités continuent d'être enregistrées** ; ce sont les analyses complémentaires — scores, correspondances produit, classification — qui deviennent sélectives, les autres fiches pouvant porter la mention *non programmé*.
- L'agence européenne de cybersécurité a mis en service une **base européenne de vulnérabilités**, alimentée notamment par les CSIRT nationaux, qui constitue désormais une source alternative crédible.
- D'autres initiatives d'attribution d'identifiants, indépendantes du programme historique, ont vu le jour et sont utilisables en complément.

📎 [S-16] pour l'évolution du NVD · [S-22] pour la base européenne.

**Ce que ça change pour vous, concrètement.**

| Si votre processus repose sur… | Alors |
|---|---|
| Le score de gravité fourni par une base unique | Une part croissante de vos constats arrivera sans score |
| La correspondance automatique produit fournie par cette base | Cette correspondance sera absente pour une partie des fiches |
| Un seuil du type « traiter au-dessus de 7 » | Ce seuil devient inapplicable sur les fiches non enrichies |

✅ **BONNE PRATIQUE (P0)** — Construisez votre chaîne de veille sur **au moins trois sources de nature différente** : l'avis de l'éditeur du produit concerné (source de vérité sur les versions), une base agrégée (dédoublonnage et couverture), et un signal d'exploitation avérée. Le détail opérationnel est au chapitre 14.

## 4.10 📌 Ce qu'aucun score ne saura jamais : votre exposition

Récapitulons ce que chaque signal apporte, et surtout ce qu'aucun n'apporte.

| Signal | Répond à | Ne répond pas à |
|---|---|---|
| Gravité technique | Si elle est exploitée, quel dégât ? | Est-elle exploitée ? Suis-je atteignable ? |
| Probabilité d'exploitation | Sera-t-elle exploitée dans le monde ? | Chez moi ? Sur cet actif ? |
| Catalogue d'exploitation avérée | A-t-elle été observée en exploitation ? | Suis-je concerné ? Suis-je exposé ? |
| Arbre de décision | Que dois-je faire ? | *(il faut lui fournir l'exposition en entrée)* |

Les trois premiers signaux sont produits **hors de chez vous**. Aucun ne connaît :

- si le service vulnérable est activé sur vos machines ;
- s'il est joignable depuis Internet, depuis le réseau bureautique, ou depuis nulle part ;
- si une mesure de contournement est déjà en place ;
- si l'actif porte une donnée critique ou un procédé industriel ;
- si sa compromission ouvre l'accès à d'autres actifs.

**C'est vous qui apportez la moitié manquante de l'équation, et personne d'autre ne peut le faire à votre place.**

### Ce que vous manipulerez réellement au quotidien

Sur la dizaine de notions présentées dans ce chapitre, quatre seulement interviennent chaque jour :

| Au quotidien | Pourquoi |
|---|---|
| **L'avis de l'éditeur** du produit concerné | La seule source de vérité sur « suis-je affecté, et quelle version corrige » |
| **Le signal d'exploitation avérée** | Le déclencheur d'urgence le plus fiable |
| **Votre cartographie d'exposition** | Elle transforme un constat en priorité |
| **Votre inventaire enrichi de criticité** | Il transforme une priorité en décision |

Les autres — nomenclatures de produits, modèles de probabilité, formats d'inventaire et d'exploitabilité — sont des **outils de soutien** : utiles quand vous en avez besoin, à consulter plutôt qu'à mémoriser. C'est aussi pour cela que les deux dernières lignes du tableau, qui ne dépendent d'aucun fournisseur, sont les plus robustes de tout le dispositif. C'est aussi la raison pour laquelle le chapitre 11 (exposition et chemins d'attaque) est placé avant le chapitre 16 (triage) : sans connaissance de l'exposition, la meilleure méthode de priorisation du monde travaille sur une entrée manquante.

## 4.11 🔬 Mini-lab 1 — Qualifier dix constats hétérogènes

**Objectif** — Typer un constat avant de le prioriser, et reconnaître ceux qui n'ont pas d'identifiant de vulnérabilité.
**Durée** 30 min · **Difficulté** 🟢 débutant · **Prérequis** §4.1 à §4.7, §14.7 · **Livrable** tableau de qualification typée.
**Compétences validées** — ✔ distinguer les origines de constats ✔ identifier la source de vérité d'un constat ✔ qualifier en fait / hypothèse / piste ✔ repérer un constat qui n'a pas d'identifiant de vulnérabilité

**Énoncé.** Voici dix constats arrivés la même semaine dans la boîte de réception d'une équipe de sécurité. Pour chacun : (a) de quel **type de constat** s'agit-il ? (b) quelle est sa **source de vérité** ? (c) quelle **information manque** pour décider ? (d) fait vérifié, hypothèse probable ou piste exploratoire ?

| # | Constat |
|---|---|
| 1 | Le scanner remonte une bibliothèque de chiffrement en version antérieure à la version corrigée en amont, sur 42 serveurs à support long |
| 2 | Un bulletin d'éditeur annonce une « faille critique d'exécution de code », sans identifiant CVE, avec une version corrigée |
| 3 | Un rapport de test d'intrusion signale une interface d'administration accessible sans authentification sur un port non standard |
| 4 | Une vulnérabilité de gravité 5,3 vient d'entrer au catalogue d'exploitation avérée |
| 5 | L'équipe de développement signale qu'une dépendance transitive de l'application métier est marquée vulnérable par l'outil d'analyse de composition |
| 6 | Un fournisseur SaaS annonce qu'un paramètre de sécurité par défaut change à la prochaine mise à jour |
| 7 | Le service comptable a reçu une facture pour un abonnement à un service en ligne inconnu de la DSI |
| 8 | Un chercheur signale par courriel une faille dans votre produit, avec une preuve de concept fonctionnelle et un délai de 90 jours |
| 9 | La supervision remonte que 14 agents de sécurité n'ont pas mis à jour leur base de détection depuis 21 jours |
| 10 | Une vulnérabilité de gravité 9,8 est publiée sur un composant présent dans votre parc, mais uniquement exploitable en accès physique local |

**Corrigé commenté**

| # | Type | Source de vérité | Information manquante | Statut |
|---|---|---|---|---|
| 1 | Vulnérabilité de composant, **probable faux positif de rétroportage** | Avis de sécurité de la distribution + révision du paquet installée | La révision éditeur réelle sur les 42 serveurs (§2.2) | Piste exploratoire tant que la révision n'est pas vérifiée |
| 2 | Vulnérabilité sans identifiant — **le MCS ne se réduit pas aux CVE** | L'avis de l'éditeur lui-même | Versions exactes déployées ; l'absence de CVE n'atténue rien | Fait vérifié sur l'existence, hypothèse sur l'impact |
| 3 | Écart de configuration / **exposition**, pas une vulnérabilité logicielle | Le rapport de test, rejoué et confirmé | Qui possède cet actif ? Depuis quand ? Traces d'accès ? | Fait vérifié — et probablement le constat le plus grave des dix |
| 4 | Vulnérabilité **à exploitation avérée** | Le catalogue + l'avis éditeur | Suis-je exposé ? La gravité modérée est ici sans importance | Fait vérifié — traitement en urgence malgré le 5,3 |
| 5 | Vulnérabilité de **dépendance transitive** | Inventaire de composants + déclaration d'exploitabilité du fournisseur | Le code vulnérable est-il atteignable dans l'application ? (§25.12) | Hypothèse probable |
| 6 | **Changement fournisseur** — activité de MCS à part entière (§3.4) | Les notes de version du fournisseur | Quels paramètres, quel effet sur ma configuration validée ? | Fait vérifié, impact à instruire |
| 7 | **Actif orphelin** découvert par une source non technique | La facture, puis la confirmation métier | Quelles données ? Quel connecteur ? Quel propriétaire ? | Fait vérifié sur l'existence |
| 8 | **Divulgation coordonnée** reçue en tant que fabricant | Le chercheur, puis la reproduction interne | Reproductible ? Quelles versions livrées ? Horloge des 90 jours (ch. 33) | Hypothèse jusqu'à reproduction |
| 9 | **Dégradation du contenu de détection**, pas une vulnérabilité (§1.3, ch. 34) | La console de l'outil, recoupée sur les postes | Pourquoi 21 jours ? Agents muets ou machines éteintes ? | Fait vérifié |
| 10 | Vulnérabilité grave mais **non atteignable à distance** | L'avis éditeur, lu jusqu'au vecteur d'accès | Existe-t-il des accès physiques non maîtrisés ? | Fait vérifié — priorité basse malgré le 9,8 |

**Les trois erreurs attendues.** Trier ces dix constats par gravité technique — cela placerait le n° 10 en tête et le n° 3 en queue, exactement à l'envers. Écarter les constats 6, 7 et 9 comme « hors sujet MCS » — ils en font pleinement partie. Traiter le n° 1 comme un fait avant vérification de la révision éditeur — et engager 42 interventions inutiles.

🔴 **FIL ROUGE — février 2026 : la semaine des 4 300 constats**

Le premier scan authentifié sur le périmètre réconcilié (§2.9) produit 4 312 constats. Malik Ferhaoui applique la règle qu'il connaît : gravité supérieure ou égale à 7. Il obtient 1 176 constats à traiter. À raison de vingt minutes par constat pour deux personnes, cela représente près de deux ans de travail.

Claire Nadeau demande un autre découpage, en trois questions seulement : *est-ce observé en exploitation ? est-ce atteignable depuis l'extérieur ? l'actif est-il critique ?*

| Filtre | Constats restants |
|---|---|
| Total brut | 4 312 |
| Gravité ≥ 7 (méthode initiale) | 1 176 |
| Exploitation avérée, tous niveaux de gravité confondus | 31 |
| … dont sur un actif joignable depuis Internet | **7** |
| … dont sur un actif de niveau 0 ou critique métier | **3** |

Les sept constats exposés incluent une vulnérabilité de gravité 5,9 sur la passerelle d'accès distant, que la méthode initiale écartait. Elle sera au cœur du cas de synthèse A.

**Décision prise.** La priorisation ne sera plus fondée sur la gravité seule. Trois entrées obligatoires : exploitation observée, exposition, criticité de l'actif. Et une règle qui deviendra un principe de la maison : *un constat que l'on choisit de ne pas traiter doit être écrit, daté et signé — pas oublié dans un rapport.*

**Livrable de l'épisode.** Un premier arbre de décision d'une page, imparfait, appliqué dès la semaine suivante. La version aboutie est construite au chapitre 16.

→ La suite en 🔴 §5.5, quand il faudra désigner qui décide d'arrêter une machine.

## Synthèse mentale du chapitre 4

Un identifiant de vulnérabilité est une clé de dédoublonnage, pas un jugement : sa qualité dépend entièrement de l'organisation qui l'a attribué. La gravité technique mesure les dégâts en cas d'exploitation, jamais la probabilité qu'elle survienne ni votre exposition. La probabilité d'exploitation comble une partie du manque mais reste mondiale, volatile et discontinue entre versions de modèle. Les catalogues d'exploitation avérée sont le signal le plus fort et le plus incomplet : ne pas y figurer ne veut pas dire ne pas être exploité. Les approches par arbre de décision produisent directement une action et se défendent en audit, ce qu'un seuil chiffré ne fait pas. Les inventaires de composants, les déclarations d'exploitabilité et les avis lisibles par machine sont produits plus vite qu'ils ne sont consommés. Enfin, l'écosystème s'est fragmenté : dépendre d'une source unique est devenu un risque, et la moitié de l'équation — votre exposition — n'est produite par personne d'autre que vous.

**Trois questions de vérification**

1. Une vulnérabilité de gravité 5,3 vient d'entrer dans un catalogue d'exploitation avérée ; une autre est notée 9,8 mais n'exige aucun privilège et n'est exploitable qu'en accès physique. Laquelle traitez-vous en premier, et avec quel argument devant un comité ?
2. Votre tableau de bord « vulnérabilités à forte probabilité d'exploitation » chute de 30 % en une semaine sans aucun déploiement. Quelles sont les deux causes à vérifier avant de communiquer ce résultat ?
3. Un fournisseur vous transmet un inventaire des composants de son produit. Quelles trois conditions doivent être réunies pour que ce document ait une valeur opérationnelle chez vous ?

---
