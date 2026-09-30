---
title: Chapitre 9 — Gouvernance, rôles et comitologie
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

Le chapitre 7 a produit une doctrine, le chapitre 8 a identifié ce que l'extérieur attend. Reste la question qui décide de leur application réelle : **qui arbitre, à quel rythme, et avec quel mandat ?**

Un programme de MCS meurt rarement d'un défaut technique. Il meurt d'un arbitrage jamais rendu.

## 9.1 Trois niveaux, trois horizons, trois types de décision

La gouvernance du MCS se structure sur trois étages. Les confondre est l'erreur la plus fréquente : on remonte des sujets techniques au niveau stratégique, qui ne sait pas les traiter, et on laisse des arbitrages métier au niveau opérationnel, qui n'a pas le mandat pour les rendre.

| Niveau | Qui | Rythme | Décisions typiques |
|---|---|---|---|
| **Stratégique** | Direction générale, direction des systèmes d'information, RSSI | Semestriel ou trimestriel | Budget pluriannuel, acceptation des risques majeurs, sortie d'obsolescence, arbitrage entre projets et maintien |
| **Tactique** | Comité MCS : RSSI, exploitation, représentants métier, prestataires | Mensuel | Priorisation des campagnes, validation des dérogations, revue des indicateurs, escalades |
| **Opérationnel** | Exploitation, propriétaires techniques | Hebdomadaire ou quotidien | Exécution, qualification des constats, planification des fenêtres, traitement des échecs |

**La règle de circulation** qui rend le dispositif fluide : chaque niveau ne traite que ce que le niveau inférieur ne peut pas trancher **avec son mandat**. Un correctif refusé par un métier n'est pas un problème technique : il remonte. Un correctif qui échoue sur douze machines n'est pas un sujet de comité : il reste au niveau opérationnel.

## 9.2 Le RACI de référence

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

## 9.3 Le comité MCS : format, ordre du jour, décisions

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

## 9.4 Articuler sécurité, exploitation et métiers sans arbitrage permanent

Le conflit d'objectifs du §1.2 est structurel. Une bonne gouvernance ne le supprime pas : elle en **réduit la fréquence**, en pré-arbitrant à froid ce qui sinon devrait être tranché à chaud, à chaque fois.

**Les quatre pré-arbitrages qui suppriment l'essentiel des conflits :**

| Pré-arbitrage | Formulation type | Ce qu'il évite |
|---|---|---|
| Fenêtres récurrentes acquises | « Deuxième jeudi, 22 h - 2 h, sans redemander » | Douze négociations par an |
| Seuil d'urgence pré-autorisé | « Vulnérabilité exploitée sur actif exposé : interruption autorisée sous 72 h, décision du propriétaire technique » | Une négociation en pleine crise |
| Plafond de charge mensuel | « Au plus N heures d'intervention MCS par mois ; au-delà, arbitrage en comité » | Le conflit permanent sur la charge |
| Règle de levée de gel | « Les gels de production comportent une clause de levée pour vulnérabilité exploitée, décidée par X » | Le blocage total pendant six semaines |

**Le principe général**, valable bien au-delà du MCS : *tout arbitrage récurrent doit être transformé en règle une fois pour toutes*. Si vous tranchez trois fois la même question, c'est qu'elle appelle une règle, pas un quatrième arbitrage.

## 9.5 Organisations décentralisées, filiales et entités acquises

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

## 9.6 ⚠️ Le RSSI propriétaire du MCS : pourquoi c'est un anti-pattern

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

## 9.7 🔴 FIL ROUGE — juillet 2026

le premier comité MCS et le désaccord Berger / Ferhaoui

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

## Synthèse mentale du chapitre 9

Un programme de MCS meurt d'un arbitrage jamais rendu, pas d'un défaut technique. La gouvernance se structure sur trois niveaux dont chacun ne traite que ce que le niveau inférieur ne peut trancher avec son mandat. Trois attributions de rôles sont contre-intuitives et décisives : la sécurité n'approuve pas la correction, le propriétaire métier signe la dérogation parce qu'il porte le risque, et l'escalade d'une impossibilité est une obligation de l'exploitation, pas une faveur. Le comité mensuel produit des décisions, pas des discussions : chaque point y arrive avec une décision proposée, et le relevé d'une page vaut preuve. Les conflits récurrents se suppriment par pré-arbitrage à froid — fenêtres acquises, seuil d'urgence pré-autorisé, plafond de charge, clause de levée de gel — selon le principe que tout arbitrage rendu trois fois appelle une règle. Enfin, faire du RSSI le propriétaire du MCS dissocie la responsabilité de l'autorité : c'est une position intenable, dont l'effet secondaire le plus pervers est qu'elle pousse à mesurer moins.

**Trois questions de vérification**

1. Votre comité MCS passe quarante minutes sur le cas d'un serveur particulier. Quel est le symptôme, quelle est la cause réelle, et quelle règle de préparation le corrige ?
2. Pourquoi faire signer les dérogations par la sécurité plutôt que par le métier affaiblit-il l'ensemble du dispositif, y compris du point de vue de la sécurité elle-même ?
3. Votre groupe rachète une société de 80 personnes et l'interconnecte au réseau en six semaines. Citez les deux règles à appliquer avant l'interconnexion, et à quel moment du processus d'acquisition elles auraient dû intervenir.

---
