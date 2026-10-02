---
title: Chapitre 10 — Inventaire et cartographie
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

## 10.1 Pourquoi tout programme de MCS échoue d'abord ici

C'est la cause d'échec n° 1 du §1.4, et elle mérite d'être formulée sans détour : **tant que le dénominateur est inconnu, aucun indicateur de MCS n'a de sens.**

Reprenons le raisonnement de bout en bout, parce qu'il est souvent accepté du bout des lèvres puis oublié dès la première présentation :

- vous ne corrigez que ce que vous connaissez ;
- vous ne mesurez que ce que votre outil atteint ;
- vous ne présentez donc, dans le meilleur des cas, qu'un pourcentage calculé sur les actifs connus **et** atteints ;
- or les actifs inconnus ne sont pas répartis au hasard : ce sont statistiquement les plus anciens, les moins gérés, les moins documentés — donc les plus vulnérables.

Autrement dit, votre indicateur est non seulement incomplet, il est **biaisé dans le sens favorable**. Les machines qui manquent sont précisément celles qui feraient chuter le chiffre.

⚠️ **PIÈGE — l'inventaire parfait comme préalable**
La conclusion inverse est tout aussi fausse : attendre un inventaire exhaustif avant de commencer à corriger. L'exhaustivité n'existe pas, elle est asymptotique. Ce qu'il faut atteindre rapidement, c'est un inventaire **suffisant, mesuré et honnête** : un périmètre de référence dont vous connaissez le taux de complétude estimé et les zones d'ombre déclarées. Le §10.9 fournit le chemin en trente jours.

## 10.2 Les sources de découverte et leur complémentarité

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

## 10.3 La réconciliation : lire les écarts plutôt que les chiffres

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

## 10.4 Les attributs minimaux d'un actif maintenable

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

## 10.5 Dépendances applicatives et effets de bord

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

## 10.6 Shadow IT et services en ligne non déclarés

Les services souscrits hors du circuit de la direction des systèmes d'information sont une part significative du périmètre réel, et ils sont particulièrement pertinents pour le MCS : ils contiennent des données, ils disposent souvent d'accès à d'autres systèmes via des connecteurs, et personne ne suit leur configuration.

**Les quatre méthodes de détection, par rentabilité décroissante :**

1. **La comptabilité.** Extraire les lignes de dépense correspondant à des abonnements logiciels. Simple, non technique, extrêmement productif.
2. **Le fournisseur d'identité.** Lister les applications ayant reçu une autorisation de connexion via l'authentification unique, et les autorisations déléguées accordées à des applications tierces. C'est aussi ce qui révèle les connecteurs disposant d'accès à la messagerie ou aux fichiers (chapitre 31).
3. **Les journaux de navigation ou de proxy.** Détectent l'usage, pas le contrat.
4. **L'enquête directe.** Demander aux équipes ce qu'elles utilisent, sans posture punitive. Le rendement dépend entièrement du climat : une organisation qui sanctionne le shadow IT ne le découvre jamais.

📌 **LIMITES** — Aucune de ces méthodes ne détecte un service gratuit, souscrit avec une adresse personnelle, utilisé par une seule personne. Ce cas relève de la sensibilisation et de la politique d'usage, pas de l'inventaire technique.

## 10.7 Maintenir l'inventaire vivant

Un inventaire est un actif périssable : il se dégrade dès le jour de sa constitution. Quatre mécanismes le maintiennent.

| Mécanisme | Principe | Effet |
|---|---|---|
| **Intégration au cycle de vie** | Aucune mise en production sans déclaration ; aucun décommissionnement sans retrait | Empêche la dégradation à la source |
| **Réconciliation périodique automatisée** | Rejouer le croisement de sources chaque mois | Détecte les écarts qui réapparaissent |
| **Contrôles de complétude** | Règles de qualité : actif sans propriétaire, sans criticité, sans date de fin de support | Mesure la qualité de la donnée, pas seulement sa quantité |
| **Indicateur de dérive** | Nombre de nouveaux écarts par mois | Mesure si le processus tient ou se dégrade |

✅ **BONNE PRATIQUE (P0)** — L'intégration au cycle de vie est la seule mesure structurelle ; les trois autres sont des rattrapages. Concrètement : la déclaration d'un actif, avec ses deux propriétaires, devient une **condition de mise en production**, au même titre que la sauvegarde. C'est une décision de gouvernance, pas un projet d'outillage.

## 10.8 📌 Ce qu'aucun outil de découverte ne verra

Soyons explicites sur les limites, parce que les ignorer produit une fausse assurance.

- **Les systèmes industriels muets**, qui ne répondent pas à une sollicitation réseau, et qu'il ne faut de toute façon pas interroger activement (§3.7).
- **Les environnements séparés physiquement**, par construction.
- **Les composants embarqués** dans les applications, qui n'ont pas d'existence réseau propre (chapitre 26).
- **Les actifs éphémères** — conteneurs, agents de construction, instances à mise à l'échelle automatique — qui n'existent pas au moment où l'inventaire passe. Pour eux, l'inventaire doit interroger l'orchestrateur, pas le réseau.
- **Les actifs détenus par un prestataire** pour votre compte, qui ne sont pas sur vos réseaux (chapitre 13).
- **Les micrologiciels**, qui ne sont presque jamais remontés par les outils d'inventaire standard (§3.8).

Pour chacune de ces catégories, la seule réponse honnête est de la **déclarer non couverte**, avec un propriétaire et une échéance de première mesure — exactement comme dans la politique du §7.7.

## 10.9 ✅ Inventaire minimal viable en trente jours

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

## 10.10 🔬 Mini-lab 2 — Réconciliation d'inventaire

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

## 10.11 🔴 FIL ROUGE — août 2026 : sur quoi portent les 84 % ?

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

## Synthèse mentale du chapitre 10

Tant que le dénominateur est inconnu, aucun indicateur n'a de sens — et le biais joue toujours dans le sens favorable, puisque les actifs manquants sont statistiquement les moins maintenus. Aucune source de découverte ne voit tout : c'est leur croisement qui produit l'information, et une source non technique comme la comptabilité fournisseurs a le meilleur rapport effort/découverte. La compétence centrale n'est pas de choisir le bon chiffre mais de lire les écarts, dont le plus dangereux est celui des machines déclarées, actives et absentes de l'outil de gestion : tout le monde les croit gérées et elles n'ont jamais reçu de correctif. Un inventaire exploitable se teste en une question — peut-on sortir en dix minutes la liste des actifs exposés, hors support et sans propriétaire ? Il se maintient par intégration au cycle de vie, la seule mesure structurelle ; le reste est du rattrapage. Enfin, tout ce qui n'est pas couvert doit être déclaré non couvert, avec un propriétaire et une échéance.

**Trois questions de vérification**

1. Trois de vos sources d'inventaire donnent trois chiffres différents. Quelle est la mauvaise question, quelle est la bonne, et quel type d'écart traitez-vous en premier ?
2. Pourquoi un taux de conformité calculé sur les seuls actifs connus est-il biaisé dans le sens favorable, et pas simplement incomplet ?
3. Votre inventaire est complet mais ne comporte ni criticité, ni exposition, ni propriétaire. Que pouvez-vous en faire concrètement pour piloter le MCS ?

---
