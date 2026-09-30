---
title: Chapitre 5 — Ce que fait réellement un analyste
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE I — Fondamentaux du renseignement
  - index.md
---

#### 5.1 Une journée type

Le métier est mal connu, y compris de ceux qui recrutent pour ce poste. Voici une journée ordinaire, sans crise, dans une organisation de taille intermédiaire.

| Heure | Activité | Chapitre |
|---|---|---|
| 8 h 45 | **Lecture de la veille.** Bulletins, avis d'éditeurs, publications suivies. Non pas tout lire : trier selon les besoins prioritaires établis | 14, 21 |
| 9 h 30 | **Qualification.** Sept éléments retenus. Pour chacun : de quelle étape s'agit-il, quelle question posée cela touche-t-il, quel destinataire | 2, 14 |
| 10 h 00 | **Vérification d'une source.** Un rapport affirme qu'un acteur cible le secteur. Remonter à l'affirmation d'origine. Quarante minutes. Résultat : la source unique est un article de presse | 10 |
| 10 h 40 | **Un échange avec la détection.** Ils ont vu une activité inhabituelle et demandent si elle correspond à quelque chose de connu | 30 |
| 11 h 15 | **Rédaction.** Une fiche opérationnelle de deux pages sur une technique observée dans le secteur | 25, 26 |
| 14 h 00 | **Réunion avec le responsable produit.** Il prépare une réponse client et veut savoir si ses produits sont mentionnés quelque part | 33 |
| 15 h 00 | **Rédaction, suite.** La fiche est relue par un collègue avec la grille des six axiomes | 12 |
| 15 h 45 | **Une demande de la direction.** « On m'a parlé d'un rapport sur les rançongiciels, ça nous concerne ? » Réponse en une page, pour demain | 26 |
| 16 h 30 | **Mise à jour du registre.** Les sept éléments du matin : quatre archivés avec motif, deux traités, un en attente d'information | 14 |
| 17 h 00 | **Une heure imprévue.** Un signalement urgent, ou rien du tout | 29 |

#### 5.2 La répartition réelle du temps

Sur un mois d'observation, dans une fonction mature :

| Activité | Part du temps | Commentaire |
|---|---|---|
| **Lire et trier** | ~25 % | La majeure partie est écartée — c'est le travail, pas un échec |
| **Vérifier** | ~20 % | Remonter les sources, tester les affirmations, chercher les explications alternatives |
| **Écrire** | ~25 % | **La compétence la plus sous-estimée du métier** |
| **Expliquer et échanger** | ~20 % | Réunions, questions, discussions avec les destinataires |
| **Technique** | ~10 % | Enrichissement, requêtes, outillage |

**Le chiffre qui surprend est le dernier.** Un analyste CTI passe environ un dixième de son temps sur des tâches techniques. Le reste est de la lecture, de la vérification, de la rédaction et de la conversation.

**Deux conséquences pratiques.**

**Pour qui veut exercer ce métier** : travaillez votre écriture. Un analyste qui raisonne bien et écrit mal produit des documents que personne n'utilise ; un analyste qui raisonne correctement et écrit clairement est immédiatement précieux. C'est la raison pour laquelle le chapitre 25 existe.

**Pour qui recrute** : un entretien qui ne teste que la connaissance technique — outils, référentiels, acteurs — évalue 10 % du poste. Faire rédiger une demi-page à partir d'un dossier ambigu est infiniment plus prédictif.

⚠️ **PIÈGE — le poste mal défini**
Beaucoup de fiches de poste « analyste CTI » décrivent en réalité trois métiers différents : ingénieur d'intégration de flux, analyste de détection, et analyste de renseignement. Les trois sont légitimes ; ils ne demandent ni les mêmes compétences, ni le même profil. Une fonction qui les mélange produit soit un ingénieur frustré, soit un analyste qui passe ses journées à maintenir des connecteurs.

#### 5.3 Les cinq livrables du métier

| Livrable | Niveau | Fréquence typique | Destinataire |
|---|---|---|---|
| **La note d'orientation** | Stratégique | 2 à 6 par an | Direction, DSI |
| **La fiche opérationnelle** | Opérationnel | 1 à 4 par mois | RSSI, MCS, produit, détection |
| **Le jeu d'indicateurs** | Tactique | Continu | Détection |
| **L'alerte** | Variable | Rare, et c'est normal | Selon l'objet |
| **La réponse à une question** | Variable | **Le plus fréquent, et le moins formalisé** | Celui qui a demandé |

**Le dernier mérite une attention particulière.** L'essentiel du travail d'un analyste ne prend pas la forme d'un document publié, mais d'une réponse à une question posée par un collègue — souvent en quelques lignes, souvent oralement. C'est là que la fonction produit le plus de valeur, et c'est aussi ce qui n'apparaît dans aucun indicateur d'activité.

✅ **BONNE PRATIQUE (P1)** — Tracez ces réponses, même sommairement : question, demandeur, date, réponse en trois lignes. Cinq minutes par semaine. C'est ce registre qui, au bout d'un an, permettra de démontrer ce que la fonction a réellement apporté — et c'est exactement l'exercice du chapitre 35.

#### 5.4 Les interlocuteurs, et ce qu'ils attendent

| Interlocuteur | Ce qu'il attend vraiment | L'erreur fréquente à son égard |
|---|---|---|
| **Direction** | Une orientation, courte, assumée | Lui envoyer du détail technique |
| **RSSI** | De quoi arbitrer ses priorités | Lui envoyer ce qu'il a déjà lu |
| **MCS / exploitation** | *Que corriger en premier* | Lui donner du contexte sans conclusion actionnable |
| **Détection** | Des éléments exploitables, datés et qualifiés | Lui livrer des indicateurs sans contexte ni fraîcheur |
| **Réponse à incident** | Vite, et pendant la crise | Arriver après |
| **Produit / PSIRT** | Ce qui vise ses produits, précisément | Lui parler du secteur en général |
| **Achats, juridique, DPO** | Une réponse à une question précise | Les ignorer jusqu'à ce qu'ils bloquent quelque chose |

**Le dernier point n'est pas anecdotique.** Une fonction CTI qui n'a pas construit de relation avec le juridique et la protection des données découvrira, au moment où elle en aura besoin, que sa collecte pose des questions qu'elle n'a pas anticipées. C'est le chapitre 20.

#### 5.5 Ce qui distingue un analyste d'un veilleur

Le tableau du §1.4 opposait les activités. Voici la version côté personne.

| | **Veilleur** | **Analyste** |
|---|---|---|
| Devant une information nouvelle | *Est-ce intéressant ?* | *Est-ce que cela répond à une question posée ?* |
| Devant une affirmation | La relaie | **Remonte à la source** |
| Devant plusieurs sources concordantes | Y voit une confirmation | **Vérifie leur indépendance** |
| Devant l'incertitude | L'évite ou la masque | **L'exprime et la calibre** |
| Devant une demande floue | Produit quelque chose | **Reformule la question** |
| Devant son propre travail passé | Passe à la suite | **Relit ses estimations pour vérifier** |

**Aucune de ces six lignes n'est technique.** Ce sont des habitudes de travail — ce qui signifie deux choses encourageantes : elles s'acquièrent, et elles ne dépendent d'aucun outil.

#### 5.6 Les qualités qui comptent, et celles qu'on croit à tort nécessaires

**Ce qui compte réellement :**

| Qualité | Pourquoi |
|---|---|
| **Écrire clairement** | Un raisonnement juste et mal exprimé ne produit aucune décision |
| **Tolérer l'incertitude** | Le métier consiste à conclure sans savoir. Qui ne le supporte pas produira de fausses certitudes |
| **Accepter d'avoir tort publiquement** | Sans cela, pas de révision, donc pas de progression |
| **Curiosité disciplinée** | Suivre une piste **et** savoir s'arrêter quand elle ne sert pas la question posée |
| **Comprendre son organisation** | C'est ce qui transforme la connaissance en renseignement (§2.3) |

**Ce qu'on croit à tort nécessaire :**

| Croyance | Réalité |
|---|---|
| Connaître les acteurs par cœur | Périmé en dix-huit mois, et rarement utile (chapitre 17) |
| Maîtriser les outils du domaine | Un dixième du temps, et ça s'apprend en quelques semaines |
| Savoir analyser des maliciels | Compétence voisine et précieuse, mais c'est un autre métier |
| Avoir une culture géopolitique poussée | Utile au niveau stratégique uniquement, donc pour une minorité de postes |
| Être rapide | Être **juste et à temps**. Ce n'est pas la même chose |

🎯 **ET MAINTENANT ?**
*On vous propose un poste d'analyste CTI. En entretien, on ne vous pose que des questions sur ATT&CK, MISP et les groupes d'attaquants. Que devez-vous en déduire ?*
**Réponse** : que le poste est probablement mal défini, ou qu'il s'agit en réalité d'un poste d'intégration technique. Une question utile à poser en retour : *« quels produits la fonction publie-t-elle aujourd'hui, et qui les lit ? »* La réponse vous dira en trente secondes si vous serez analyste ou administrateur de plateforme. Aucune des deux réponses n'est disqualifiante — mais mieux vaut le savoir avant.

#### 5.7 🔴 FIL ROUGE — mai 2029 : la première semaine de Nour

Nour Belkacem prend ses fonctions le 2 mai. Voici ce qu'elle fait, et ce que ça révèle.

**Jour 1 — elle ne collecte rien.** Elle demande à Claire la liste des personnes qui pourraient avoir besoin de renseignement, et prend rendez-vous avec chacune. Sept rendez-vous en trois jours.

**Jours 2 à 4 — les entretiens.** Une seule question, posée à chaque fois : *« qu'aimeriez-vous savoir que vous ne savez pas, et qu'est-ce que vous feriez différemment si vous le saviez ? »*

Les réponses sont instructives, et aucune n'est celle qu'elle attendait.

| Interlocuteur | Ce qu'il demande | Ce que ça révèle |
|---|---|---|
| Malik Ferhaoui (MCS) | *« Sur quoi corriger en premier quand j'ai trente constats et deux semaines »* | Un besoin **opérationnel**, précis, immédiatement actionnable |
| Yann Prigent (produit) | *« Est-ce que quelqu'un parle de nos produits quelque part »* | Un besoin **tactique** sur un périmètre étroit |
| Claire Nadeau (RSSI) | *« Est-ce que ce qui arrive à nos concurrents va nous arriver »* | Un besoin **opérationnel à stratégique** |
| Sonia Weber (DSI) | *« Est-ce qu'on investit au bon endroit »* | Un besoin **stratégique**, à échéance budgétaire |
| Le référent détection | *« Qu'est-ce que je devrais chercher dans mes journaux et que je ne cherche pas »* | Un besoin **tactique et opérationnel**, formulé parfaitement |
| Dr Hélène Fabre (réglementaire) | *« Rien, je ne vois pas ce que ça m'apporterait »* | **Honnête, et à respecter** |
| Karim Lebrun (DAF) | *« Que ça coûte moins cher que ce que ça évite »* | Ce n'est pas un besoin de renseignement, c'est un critère d'évaluation |

**Jour 5 — elle écrit une page.** Pas un rapport : une liste de six questions, formulées avec les mots de ceux qui les ont posées, avec pour chacune le nom du demandeur et la décision qu'elle éclaire.

**Ce que Claire remarque.** Nour n'a souscrit à rien, n'a installé aucun outil, n'a produit aucun contenu. En cinq jours, elle a fait la seule chose qui conditionne tout le reste : **transformer une intuition — « il nous faut du CTI » — en six questions ayant chacune un demandeur nommé**.

**Les deux réponses les plus utiles sont les deux dernières.** Hélène Fabre dit non : c'est une information précieuse, qui évite de lui envoyer pendant deux ans des produits qu'elle n'ouvrira pas. Et Karim Lebrun ne formule pas un besoin mais un critère — celui-là même qui servira à évaluer la fonction dans douze mois.

**Livrable de l'épisode.** Une page : six questions, six demandeurs, six décisions. C'est l'embryon des besoins prioritaires de renseignement, construits formellement au chapitre 14.

→ **Fin de la Partie I.** La suite en 🔴 §7.9, quand Nour surestimera une menace et découvrira pourquoi.

---

> ### 🎓 À ce stade, vous savez distinguer
>
> ✓ une **donnée** d'une **information**
> ✓ une **information** d'un **renseignement**
> ✓ un **fait** d'une **estimation**
> ✓ une **observation** d'une **conclusion**
> ✓ une **hypothèse** d'un **jugement**
> ✓ un **jugement** d'une **recommandation**
> ✓ une **décision** de son **justificatif**
>
> Ces sept distinctions paraissent évidentes. Elles sont pourtant confondues dans la majorité des produits de renseignement que vous lirez — y compris commerciaux, y compris chers, y compris rédigés par des professionnels compétents.
>
> **Vous savez également :**
>
> - situer un besoin sur les trois niveaux, et pourquoi l'incertitude tolérable varie en sens inverse de l'horizon ;
> - reconnaître les six causes d'échec d'une cellule CTI, dont aucune n'est technique ;
> - appliquer les six axiomes, et repérer leurs violations dans un texte ;
> - qualifier un produit reçu, et identifier ce qu'il vous reste à y ajouter ;
> - dire ce que le CTI ne fait pas, et où s'arrête le périmètre de ce cours.
>
> **Ce que vous ne savez pas encore** : comment raisonner quand plusieurs explications sont possibles, comment repérer vos propres biais, comment exprimer une confiance, et comment construire un jugement qui résiste à la contradiction. C'est l'objet de la Partie II — le cœur du cours.

---


## Registre de cohérence — fin de T1 (chapitres 1 à 5)


### Termes arrêtés

| Terme retenu | Définition courte | Écarté |
|---|---|---|
| **Renseignement** | Connaissance répondant à un besoin de décision identifié | « intelligence » (anglicisme), « veille » (autre activité) |
| **Jugement analytique** | Évaluation argumentée, calibrée, réfutable | « conclusion », « verdict » |
| **Connaissance** | Information intégrée à un ensemble extérieur | — |
| **Produit** | Tout livrable diffusé par la fonction | « rapport » (un format parmi d'autres), « deliverable » |
| **Destinataire** | Personne nommée à qui un produit est adressé | « client interne », « consommateur » |
| **Besoin prioritaire de renseignement** | Question formalisée émanant d'un décideur | « PIR » (sigle utilisé une fois en glossaire) |
| **Calibrage** | Expression explicite du niveau de confiance | « pondération », « scoring » |
| **Niveau de confiance** | Solidité de la base d'une évaluation. **Indépendant de la gravité** | — |
| **Circularité** | Plusieurs sources apparentes remontant à une source unique | « echo chamber » |
| **Boucle analytique** | Question → collecte → analyse → jugement → décision → retour | « cycle » (réservé au modèle classique, ch. 15) |
| **Axiome** | Énoncé fondateur du chapitre 4, réutilisé dans tout le cours | « principe » (réservé à la doctrine) |


### Renvois émis vers des chapitres non encore rédigés

| Depuis | Vers | Engagement |
|---|---|---|
| §1.3, §1.5 | Ch. 14 | Construction formelle des besoins prioritaires |
| §1.5, §2.2 | Ch. 9, 11 | Calibrage et jugement analytique |
| §1.5, §2.1 | §10.4 | La circularité, traitée en profondeur |
| §1.5, §5.3 | Ch. 35 | Mesure de l'impact et registre des réponses |
| §1.6 | Ch. 13 | Attribution et son utilité limitée en défense |
| §2.2 | Ch. 11 | Juger sans le dire — dérive traitée |
| §3.3 | Ch. 30 | Cycle de vie d'un indicateur |
| §3.6, §5.4 | Ch. 26 | Adaptation au destinataire |
| §3.7 | Ch. 39 | CTI en petite organisation, niveaux non couverts |
| §4.2, §4.5 | Ch. 8 | Techniques d'analyse structurée |
| §4.6 | Cas B | La circularité comme scénario complet |
| §4.9 | Ch. 12 | Relecture croisée et analyse à plusieurs |
| §5.2 | Ch. 25 | Écrire pour être lu |
| §5.4 | Ch. 20 | Cadre juridique et relation avec le juridique |
| §5.7 | Ch. 14 | Formalisation des six questions |


### État du fil rouge

| Élément | Valeur figée |
|---|---|
| Épisodes écrits | §1.10 (mars 2029), §2.6 (avril 2029), §3.8 (mai 2029), §4.9 (juin 2029), §5.7 (mai 2029, première semaine) |
| Personnages engagés | Claire Nadeau (RSSI) · **Nour Belkacem** (analyste CTI, arrivée 02/05/2029, 5 ans en centre opérationnel, jamais fait de CTI) · Malik Ferhaoui (exploitation/MCS) · Yann Prigent (produit) · Sonia Weber (DSI) · Karim Lebrun (DAF) · Dr Hélène Fabre (réglementaire) · le référent détection (non nommé à ce stade) |
| Non encore introduite | Léa Cassin (DPO) |
| Chiffres figés | 3 comptes suivis · 1 flux ingéré jamais examiné · 0 produit en 12 mois · note du 22/05 = 11 pages, 7 destinataires, 1 lecture intégrale, 0 décision · redécoupage en 3 produits = 3 décisions · 40 indicateurs fournis, 11 retenus · relecture des axiomes : 9 verbes d'intention, 4 pertes de mode, 2 conclusions de concomitance, 0 section de réfutation · 2 des 3 publications citaient la même source · 7 entretiens, 6 besoins, 1 refus |
| Dates figées | Courriel client 14/03/2029 · comité 04/04/2029 · prise de poste 02/05/2029 · note 22/05/2029 · rediffusion 05/06/2029 · bulletin non exploité 18/02/2029, correctif appliqué 03/03/2029 (13 jours) |
| Décisions prises | Ne rien souscrire avant d'avoir des questions · poste validé 12 mois avec critère d'évaluation « décisions prises différemment » · un produit par niveau et par destinataire · relecture croisée à partir de juillet · besoins formulés avec les mots du demandeur |
| Prochain épisode | §7.9 — Nour surestime une menace |


### Livrables produits

| Livrable | Section | Réplication |
|---|---|---|
| La boucle analytique | §1.2 | Rappel en tête de chaque partie |
| Les six causes d'échec | §1.5 | Ch. 40, annexe K |
| Le tableau des cinq objets | §2.1 | Annexe A, annexe C |
| Le test des quatre questions | §2.4 | Annexe L |
| Grille de qualification d'un produit reçu | §2.7 | Annexe C |
| Le tableau des trois niveaux | §3.1 | Rappel en tête de partie, annexe C |
| Les six axiomes | Ch. 4 | Grille de relecture, annexe C |
| Trois modèles de produits par niveau | §3.8 | Annexe D |
| Grille de relecture par les axiomes | §4.9 | Annexe C |


### Données périssables introduites

| Donnée | Section | Renvoi |
|---|---|---|
| Scission d'une tactique d'un référentiel majeur, avril 2026 | §1.8 | [S-01] |
| Entrées de modes opératoires assistés par modèles de langage | §1.8 | [S-02] |
| Instabilité d'un régime juridique de partage, échéance proche | §1.8 | [S-03] |

⚠️ **Aucun de ces trois faits ne porte un raisonnement.** Chacun illustre un enseignement formulé indépendamment de lui, conformément à la règle éditoriale de l'en-tête.


### Points marqués [à vérifier]

Aucun. Les trois faits datés du §1.8 sont sourcés en annexe M ; leur formulation dans le corps est volontairement générique — ni version, ni date précise, ni nom de référentiel — pour que le texte survive à leur péremption. Les détails datés figurent au chapitre 18 et en annexe M.


### Écarts au plan validé

Aucun écart de structure. Trois précisions rédactionnelles :

1. **§2.1 est rédigé comme une progression narrative** sur un événement unique plutôt que comme cinq définitions. C'est ce que la structure demandait ; je le signale car cela rend le chapitre plus long que prévu (≈ 2 400 mots) et l'annexe A devra reprendre les définitions sous forme courte.
2. **Le bloc 🎯 ET MAINTENANT ?** est introduit comme bloc récurrent, non prévu au plan. Il répond au risque identifié en revue — *le cours ne doit pas devenir trop intellectuel*. À reproduire dans les 35 chapitres restants, à raison de un à trois par chapitre.
3. **§4.3 traite l'axiome de l'absence en reprenant explicitement la formulation retenue en structure v3** (l'absence appelle une question sur la capacité d'observation), avec une critique nommée de la formule provocatrice concurrente. Cette prise de position doit rester cohérente au chapitre 8 et au cas de synthèse B.

---

---
