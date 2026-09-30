---
title: Chapitre 2 — L'échelle d'abstraction
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 2.1 Six niveaux, six natures d'objet

Le vocabulaire technologique mélange en permanence des objets qui n'ont pas le même statut. Le premier instrument de ce cours consiste à les séparer.

> **Brique → Capacité → Plateforme → Système → Doctrine → Récit**

| Niveau | Nature | Question qui lui convient |
|---|---|---|
| **Brique** | un composant, un matériau, un procédé | comment ça marche, combien ça coûte, qui sait le fabriquer |
| **Capacité** | quelque chose qu'on sait faire | dans quelles conditions, avec quelle fiabilité, à quel coût |
| **Plateforme** | un objet intégré, déployable, achetable | quelles performances réelles, quelle maintenance, quel prix |
| **Système** | plusieurs plateformes reliées, avec organisation et logistique | quelle disponibilité d'ensemble, quels points de rupture |
| **Doctrine** | une manière organisée d'employer le système | quel gain opérationnel, quelles compétences, quelle organisation |
| **Récit** | un cadrage, une catégorie médiatique ou commerciale | ce mot désigne-t-il quelque chose de vérifiable ? |

### Un exemple physique

* Un capteur infrarouge non refroidi est une **brique**.
* La perception nocturne est une **capacité** — elle peut être obtenue par ce capteur, ou autrement.
* Un drone équipé de ce capteur est une **plateforme**.
* Une flotte de drones, avec liaisons de données, station de contrôle, chaîne de maintenance et opérateurs formés, est un **système**.
* L'emploi coordonné et distribué de cette flotte est une **doctrine**.
* « Physical AI » est, selon l'usage qu'on en fait, un **récit** — un cadrage transversal utile pour désigner un mouvement, mais qui ne désigne aucun objet précis.

### Le même exemple, dans votre monde

* Un transistor est une **brique**. Un serveur est une **plateforme**.
* L'élasticité — pouvoir doubler la capacité en quelques minutes — est une **capacité**.
* Un datacenter avec son alimentation, son refroidissement, son réseau et ses équipes est un **système**.
* L'infrastructure immuable, le déploiement continu, l'astreinte organisée : autant de **doctrines**.
* « Cloud native » et « zero trust » sont des **récits**. Ce qui ne veut pas dire qu'ils sont vides : ils désignent des ensembles cohérents de doctrines. Mais on ne peut pas acheter « zero trust », on ne peut pas mesurer sa performance, et deux fournisseurs qui l'invoquent ne vendent pas la même chose.

## 2.2 Pourquoi le vocabulaire mélange les niveaux

Cette confusion n'est pas un accident. Elle a des causes identifiables, et savoir les nommer aide à repérer le glissement.

**Le glissement commercial.** Vendre une brique est difficile : le client compare les caractéristiques et négocie le prix. Vendre une capacité est plus confortable. Vendre une doctrine l'est encore plus, parce qu'on ne peut pas la comparer. Un vendeur de composants qui parle de « transformation » monte volontairement de trois niveaux.

**Le besoin de catégories.** Les analystes, les journalistes et les financiers ont besoin de regrouper. Un regroupement est utile s'il rassemble des objets qui partagent des contraintes. Il est trompeur s'il rassemble des objets qui ne partagent qu'un mot.

**L'ambiguïté légitime.** Certains termes désignent réellement plusieurs niveaux selon le contexte. « Radar » peut désigner un principe physique, un composant, un équipement ou un système complet. Ce n'est pas de la confusion : c'est une polysémie normale, à condition de savoir de quel niveau on parle dans la phrase en cours.

**L'inflation de la nouveauté.** Requalifier une brique en récit permet de présenter une amélioration incrémentale comme une rupture. C'est le mécanisme qui produit les vagues de vocabulaire successives autour de choses parfois très stables.

## 2.3 Le cas du récit

Le niveau « récit » mérite un traitement à part, car il attire naturellement le mépris, ce qui serait une erreur.

Un récit est un **cadrage** : une manière de découper le réel qui met en avant certaines relations. Certains cadrages sont excellents et ont produit des progrès réels : parler de « chaîne d'approvisionnement » plutôt que de fournisseurs isolés a permis de voir des dépendances qu'on ne voyait pas. Parler de « surface d'attaque » a changé la manière de concevoir des systèmes.

Un récit devient trompeur quand il commence à être traité comme un objet. On peut analyser une brique, mesurer une capacité, acheter une plateforme, exploiter un système, appliquer une doctrine. On ne peut rien faire de tout cela avec un récit — sauf y adhérer.

### Test du cadrage

Trois questions suffisent :

1. **Ce terme regroupe-t-il des objets qui partagent des contraintes réelles ?** Si oui, c'est un cadrage analytique. Sinon, c'est une catégorie de marché.
2. **Peut-on énoncer ce qui n'entre pas dans la catégorie ?** Une catégorie qui contient tout ne dit rien.
3. **Le terme prédit-il quelque chose ?** Un bon cadrage vous fait anticiper un problème que vous n'auriez pas vu.

Appliquez ce test à trois termes que vous avez entendus cette semaine. En général, l'un des trois passe, un autre échoue nettement, et le troisième dépend de qui l'emploie — ce qui est déjà une information utile.

## 2.4 Ce que le niveau change à la question à poser

C'est l'usage principal de l'échelle : elle vous dit **quelle question est pertinente** et **quelle preuve vous devez exiger**.

| Si l'objet est… | La bonne question est… | La preuve attendue est… | L'horizon typique est… |
|---|---|---|---|
| une brique | quel coût, quel rendement, quelle disponibilité industrielle | données de production, fiches techniques, rendement de fabrication | court, mesurable |
| une capacité | dans quelles conditions, avec quelle fiabilité | protocole d'essai, taux de succès, conditions d'échec | moyen |
| une plateforme | quel prix, quelle maintenance, quel service | retours d'exploitation, coût total de possession | moyen |
| un système | quels points de rupture, quelle disponibilité d'ensemble | exercices, incidents, modes dégradés | long |
| une doctrine | quel gain organisationnel, quelles compétences | retours d'expérience, comparaison avant/après | long |
| un récit | ce terme désigne-t-il quelque chose ? | aucune preuve n'est possible — reformulez au bon niveau | sans objet |

La dernière ligne est la plus utile en réunion. Face à une affirmation de niveau « récit », la réponse n'est pas de contredire : c'est de demander de quel objet concret on parle. La discussion redescend alors d'elle-même à un niveau où l'on peut vérifier quelque chose.

## 2.5 Trois pièges spécifiques

**Le saut de niveau silencieux.** Une phrase commence à un niveau et se termine à un autre : « ce capteur coûte trois fois moins cher, donc la surveillance autonome devient rentable ». On est passé de la brique au système sans rien démontrer entre les deux. Entre le capteur et la surveillance autonome, il reste l'intégration, le traitement, la communication, la maintenance, l'exploitation et les opérateurs.

**L'attribution au mauvais niveau.** Un progrès réel sur une brique est attribué au récit qui l'englobe. On dit « l'IA a permis X » alors que c'est une baisse du coût du calcul, ou un jeu de données devenu disponible, qui a permis X. La distinction n'est pas académique : elle change complètement la réponse à la question « est-ce que ça va continuer ? »

**Le rabattement.** Symétrique du précédent : réduire un système à sa brique la plus visible. « Le problème du véhicule autonome, c'est le lidar. » Non : le lidar est une brique parmi d'autres, et le verrou est ailleurs. Nous verrons au chapitre 3 que le verrou n'est presque jamais là où on le cherche spontanément.

## 2.6 Cas guidé — classer quinze termes

Voici quinze termes réellement employés. Avant de lire la colonne de droite, attribuez un niveau à chacun. Certains sont ambigus : c'est voulu.

| Terme | Niveau | Commentaire |
|---|---|---|
| Batterie lithium-ion | brique | un composant, avec des variantes chimiques |
| Autonomie énergétique embarquée | capacité | obtenue par des briques diverses |
| Exosquelette | plateforme | objet intégré, achetable |
| Industrie 4.0 | récit | cadrage large, peu de contraintes partagées |
| Fibre optique | brique | support de transmission |
| Très haut débit | capacité | plusieurs briques y mènent |
| Réseau d'accès d'un opérateur | système | plateformes + exploitation + supervision |
| Edge computing | doctrine | choix de répartition d'un traitement |
| GPU | brique | composant |
| Entraînement de grands modèles | capacité | conditionnée par des briques et des données |
| Datacenter | système | énergie, refroidissement, réseau, équipes |
| Souveraineté numérique | récit | objectif politique, pas objet technique |
| Jumeau numérique | ambigu | capacité (simuler) ou doctrine (piloter par la simulation) |
| CRISPR | brique/capacité | outil moléculaire, et capacité d'édition |
| Essaim de drones | système + doctrine | le mot désigne l'ensemble et son emploi |

Les trois dernières lignes sont les plus intéressantes. L'ambiguïté n'est pas une faiblesse de l'échelle : c'est une information. Quand un terme occupe deux niveaux, c'est presque toujours le signe qu'une **capacité technique** et une **manière de l'employer** sont en train de se confondre dans le langage — souvent parce que l'une des deux n'existe pas encore vraiment.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « On fait de l'IA » | une capacité est utilisée quelque part dans un produit | sur quelle tâche précise, avec quelle fiabilité mesurée ? |
| « C'est une technologie de rupture » | affirmation de niveau récit | qu'est-ce qui devient possible qui ne l'était pas ? |
| « Nos concurrents sont déjà dessus » | argument de niveau marché, pas technique | dessus à quel niveau : pilote, produit, ou communiqué ? |
| « Il suffit d'intégrer le composant » | saut de niveau brique → système | qui fait l'intégration, la maintenance, l'exploitation ? |
| « La technologie est mature » | affirmation ambiguë | mature comme brique, comme plateforme, ou comme système ? |

🧪 **Lab 1 — Classement**

**Objectif.** Séparer les niveaux d'abstraction dans un discours réel.
**Durée.** 40 minutes. **Difficulté.** 1/3. **Prérequis.** Chapitre 2.
**Contexte.** Prenez trois communiqués de presse technologiques récents, dans trois secteurs différents dont au moins deux hors informatique.
**Travail demandé.** Pour chacun : (a) relever tous les termes techniques employés ; (b) attribuer un niveau à chacun ; (c) repérer les sauts de niveau à l'intérieur d'une même phrase ; (d) identifier ce que le communiqué affirme réellement une fois les récits mis de côté.
**Livrable.** Un tableau de trois colonnes et un paragraphe par communiqué : « ce qui est effectivement affirmé ».
**Compétences validées.** Classement, détection du saut de niveau, reformulation au niveau vérifiable.
**Éléments attendus.** Les communiqués contiennent presque toujours au moins un saut brique → capacité et un terme de niveau récit employé comme s'il désignait un objet. Un raisonnement acceptable identifie le saut sans en conclure que le communiqué est mensonger : la plupart du temps, il ne l'est pas, il est simplement formulé à un niveau qui interdit la vérification.

🎓 **À ce stade, vous savez…** attribuer un niveau à un objet technologique, repérer un saut de niveau dans une phrase, distinguer un cadrage analytique d'une catégorie de marché, et reformuler une affirmation de niveau récit en question vérifiable.

---
