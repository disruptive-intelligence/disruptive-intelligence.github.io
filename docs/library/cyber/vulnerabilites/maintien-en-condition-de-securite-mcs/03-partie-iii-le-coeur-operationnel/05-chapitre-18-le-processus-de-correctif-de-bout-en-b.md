---
title: Chapitre 18 — Le processus de correctif de bout en bout
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

## 18.1 La chaîne complète

Neuf étapes, dont trois sont systématiquement escamotées : la qualification du correctif, la vérification post-déploiement, et la production de preuve.

```
1. Identification   → le constat existe et est qualifié (ch. 14-16)
2. Qualification    → que contient ce correctif, et qu'est-ce qu'il casse ?
3. Acquisition      → obtenir le correctif par un canal de confiance (§2.3)
4. Validation       → tester sur un environnement représentatif (§6.12)
5. Planification    → fenêtre, anneaux, plan de retour arrière
6. Déploiement      → progressif, avec critères d'arrêt
7. Vérification     → l'état constaté a-t-il changé ? (§2.9)
8. Clôture          → issue et preuve (§17.7)
9. Preuve           → archivage exploitable en audit (ch. 39)
```


**La règle de proportionnalité.** Les neuf étapes ne s'appliquent pas avec la même profondeur à tout. Un correctif de navigateur sur un poste C3 et une montée de version d'hyperviseur C1 suivent le même chemin, avec des exigences très différentes à chaque étape. La classe de service (§7.2) détermine cette profondeur — c'est à cela qu'elle sert.

## 18.2 Qualifier un correctif avant de le déployer

**Les six questions**, dont les réponses se trouvent dans les notes de version, la base de connaissances de l'éditeur et les retours de la communauté :

| Question | Où chercher | Pourquoi |
|---|---|---|
| Que corrige-t-il exactement ? | Notes de version | Vérifier qu'il traite bien votre constat |
| Quels **prérequis** exige-t-il ? | Notes de version | Un correctif qui exige un niveau antérieur non installé échouera silencieusement |
| Quelles **régressions** sont signalées ? | Base de connaissances, forums, retours communautaires | C'est l'information la plus rentable de la liste |
| Nécessite-t-il un **redémarrage** ? | Notes de version | Détermine la fenêtre nécessaire |
| Est-il **désinstallable** ? | Documentation, test | Détermine le plan de retour arrière (§2.5) |
| Y a-t-il un **effet différé** ? | Notes de version | Le correctif à activation différée du §2.8 |

⚠️ **PIÈGE — le correctif déjà connu comme problématique**
Beaucoup de régressions sont signalées publiquement dans les 48 à 72 heures suivant la publication. Une organisation qui déploie systématiquement dans les 24 heures s'expose à des problèmes que d'autres ont déjà documentés. C'est l'argument principal en faveur d'un **délai d'observation** avant le premier anneau — sauf urgence caractérisée (chapitre 21), où le calcul s'inverse.

## 18.3 Valider : environnements et jeux de tests

Le §6.12 a posé le problème de la représentativité. Voici la mise en œuvre.

**Trois niveaux de validation**, selon la classe de service :

| Niveau | Contenu | Pour quelle classe |
|---|---|---|
| **Aucune** | Déploiement direct en anneau pilote | C3, correctifs de sécurité courants |
| **Fonctionnelle** | Tests métier sur environnement de recette | C2 |
| **Complète** | Recette + tests de non-régression + validation métier formelle | C1, montées de version |

**Le délai d'observation** est un outil distinct des tests, et souvent plus efficace : laisser passer un temps défini entre la publication et le déploiement, pendant lequel les régressions apparaissent chez d'autres. Un délai de 3 à 7 jours capte l'essentiel des problèmes signalés publiquement, pour un coût nul.

✅ **BONNE PRATIQUE (P1)** — Formalisez ce délai dans la politique, avec sa dérogation : *délai d'observation de 5 jours, sauf vulnérabilité activement exploitée où il est ramené à zéro*. Cela transforme un comportement implicite en règle explicite, et cela évite la discussion à chaque campagne.

🖼 **SCHÉMA — Anneaux de déploiement et critères de passage.** *Cinq anneaux concentriques ou en cascade, avec la durée d'observation et le critère de passage entre chacun.*

## 18.4 Le déploiement par anneaux

**Le principe.** Découper le parc en populations successives, avec un critère de passage entre chacune.

| Anneau | Population | Taille indicative | Durée d'observation |
|---|---|---|---|
| 0 — Laboratoire | Machines de test | Quelques unités | 1 à 3 jours |
| 1 — Pilote | Volontaires, équipe informatique | 2 à 5 % | 3 à 5 jours |
| 2 — Représentatif | Échantillon couvrant tous les profils métier | 10 à 20 % | 3 à 7 jours |
| 3 — Général | Le reste | 75 à 85 % | — |
| 4 — Sensibles | Actifs critiques, cas particuliers | Quelques unités | Traitement unitaire |

**Les deux erreurs de conception des anneaux :**

1. **L'anneau pilote non représentatif.** Composé uniquement de machines de l'équipe informatique, il ne teste ni les applications métier, ni les configurations réelles, ni les usages. Il valide qu'un correctif s'installe, pas qu'il ne casse rien.
2. **L'absence de critère de passage.** On passe à l'anneau suivant « parce que ça semble aller ». Le critère doit être écrit, mesurable et vérifié : taux d'installation réussie, absence d'incident déclaré, indicateurs fonctionnels stables (§6.8).

**Les critères d'arrêt automatiques**, définis avant le déploiement :

```
Arrêt de la campagne si l'une de ces conditions est atteinte :
  · taux d'échec d'installation      > 5 %
  · incidents déclarés liés          ≥ 3 sur l'anneau
  · indicateur fonctionnel           baisse > 10 % sur 30 min
  · redémarrages inattendus          ≥ 2 machines
```


## 18.5 Ordre des opérations et dépendances

**Redémarrer quoi ?** Trois niveaux, du moins au plus coûteux : le **processus** (rechargement du binaire), le **service** (arrêt et relance du démon), le **système** (redémarrage complet). Le §2.6 fournit les commandes pour savoir lequel est nécessaire. Choisir le niveau minimal suffisant divise le coût d'une campagne.

**L'ordre entre composants.** Une chaîne applicative se met à jour dans un ordre déterminé par les dépendances : en général, du plus profond au plus superficiel — base de données, puis services applicatifs, puis frontaux — sauf indication contraire de l'éditeur. Un ordre inversé produit des erreurs de compatibilité pendant la transition.

**Les quatre opérations connexes** systématiquement oubliées dans les plans de campagne :

| Opération | Pourquoi elle compte |
|---|---|
| **Drainage des connexions** | Arrêter un service avec des sessions actives produit des erreurs visibles côté utilisateur |
| **Invalidation de cache** | Un cache contenant l'ancien comportement peut annuler l'effet du correctif ou produire des incohérences |
| **Bascule de cluster** | Ordre, temporisation, vérification de la synchronisation avant de basculer le second membre (§2.7) |
| **Réindexation ou migration de données** | Peut prendre des heures et n'est pas interruptible |

## 18.6 Contraintes d'infrastructure

Trois contraintes physiques qui font échouer des campagnes correctement conçues :

- **La bande passante.** Un correctif cumulatif de plusieurs centaines de mégaoctets multiplié par le nombre de postes d'un site distant saturera la liaison. Remède : cache local, distribution entre pairs, ou déploiement échelonné par site.
- **Le démarrage massif simultané.** Programmer le redémarrage de centaines de machines virtuelles à la même minute sature le stockage et allonge le démarrage de plusieurs dizaines de minutes. Remède : échelonnement aléatoire sur une plage.
- **La capacité en mode dégradé.** Corriger un cluster suppose de fonctionner temporairement avec un membre en moins (§6.3). Si la capacité restante ne suffit pas, la campagne provoque une dégradation de service.

## 18.7 Migrations et correctifs non réversibles

Le §6.7 a traité les migrations de schéma. Deux règles opérationnelles en découlent :

1. **Identifier le point de non-retour avant de commencer**, et l'écrire dans la demande de changement. La question exacte : *à partir de quel instant un retour arrière exigera-t-il une restauration de données ?*
2. **Vérifier la réversibilité réelle du correctif** (§2.5) sur une machine représentative, avant la campagne — pas pendant l'incident.

## 18.8 Le plan de retour arrière

| Élément | Exigence |
|---|---|
| Mécanisme | Nommé explicitement : instantané, sauvegarde, redéploiement, désinstallation vérifiée |
| **Durée mesurée** | Chronométrée lors du test. C'est cette durée qui décide si vous osez déployer |
| Point de non-retour | Identifié et daté |
| Décideur | Qui décide du retour arrière, et sur quel critère |
| Vérification post-retour | Comment s'assurer que l'état antérieur est bien restauré |

⚠️ **PIÈGE — le plan de retour arrière jamais testé**
Un plan non testé n'est pas un plan. Le test doit être fait au moins une fois par type d'actif et par mécanisme, et refait après tout changement significatif de l'environnement.

## 18.9 Vérification post-déploiement

Trois vérifications distinctes, souvent confondues :

| Vérification | Question | Méthode |
|---|---|---|
| **Technique** | Le correctif est-il appliqué ? | État constaté (§2.9) |
| **Effectivité** | Le code corrigé s'exécute-t-il ? | Redémarrage confirmé (§2.6) |
| **Fonctionnelle** | Le service fait-il toujours son travail ? | Indicateur fonctionnel (§6.8) |

La troisième est celle qui manque presque toujours, et c'est celle qui détecte les régressions silencieuses.

## 18.10 La traîne longue

Toute campagne laisse un résidu : machines éteintes, nomades absents, actifs en échec, cas particuliers. Ce résidu représente typiquement 2 à 5 % du parc, et il concentre une part disproportionnée des risques.

**Le traitement à trois niveaux :**

1. **Relance automatique** pendant une période définie — la majorité du résidu se résorbe seule.
2. **Traitement manuel** du reste, actif par actif, avec identification de la cause.
3. **Qualification formelle** de ce qui résiste : dérogation (§7.4) ou décommissionnement (chapitre 35).

**La règle** : une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée. Une campagne « terminée à 97 % » avec 3 % non qualifiés est une campagne dont la partie la plus risquée n'a pas été traitée.

## 18.11 ⚠️ Quand le correctif casse

Les mises à jour défectueuses existent, y compris chez les éditeurs majeurs, et y compris sur des correctifs de sécurité. La doctrine à tenir n'est ni la naïveté ni l'immobilisme.

| Ce qui ne marche pas | Ce qui marche |
|---|---|
| Déployer immédiatement partout | Anneaux + délai d'observation + critères d'arrêt |
| Ne jamais déployer avant plusieurs mois | Délai borné et différencié par classe |
| Décider au cas par cas dans l'urgence | Doctrine écrite, avec dérogation prévue pour l'urgence |

**Le calcul à faire dans chaque cas**, et il est explicite : comparer le risque du correctif (probabilité de régression × impact de l'indisponibilité) et le risque du non-correctif (probabilité d'exploitation × impact de la compromission). Ce calcul est le sujet entier du cas de synthèse C.

## 18.12 🔬 Mini-lab 5 — Concevoir des anneaux de déploiement

**Objectif** — Découper un parc en anneaux réellement représentatifs et définir des critères de passage vérifiables.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §18.4, §6.8 · **Livrable** tableau d'anneaux + grille de critères (D.6).
**Compétences validées** — ✔ composer un anneau pilote représentatif ✔ écrire des critères de passage vérifiables ✔ traiter une population intermittente ✔ arbitrer une échéance intenable plutôt que la subir

**Données fournies — parc de 340 postes**

| Population | Nb | Particularités | Applications métier critiques | Connexion réseau interne |
|---|---|---|---|---|
| Siège — bureautique | 180 | Poste standard, droits utilisateur | Gestion commerciale, paie (RH only) | Permanente |
| Siège — direction et RH | 22 | Données sensibles | Paie, gestion documentaire | Permanente |
| R&D Nantes | 90 | Droits d'administration locaux, environnements de développement, machines puissantes | Chaîne de développement, outils de build | Permanente |
| Commerciaux nomades | 40 | Se connectent 2 à 6 fois/mois | Gestion commerciale, hors ligne partiel | **Intermittente** |
| Site industriel — bureautique | 19 | Horaires 3×8, arrêts de ligne à éviter | Suivi de production (lecture) | Permanente |
| Site industriel — supervision | 11 | **Classe C4**, validation constructeur requise | Conduite de ligne | Réseau industriel |

**Contraintes** : la campagne doit être terminée en 21 jours · l'équipe dispose de 2 personnes · le correctif exige un redémarrage · deux régressions sur la gestion commerciale ont été signalées publiquement dans les 48 h suivant la publication.

**Questions**
(a) Proposez un découpage en anneaux, avec effectifs et justification.
(b) Écrivez les critères de passage entre anneaux.
(c) Traitez les nomades.
(d) Traitez les 11 postes de supervision.
(e) La contrainte de 21 jours est-elle tenable ? Que faites-vous si elle ne l'est pas ?

---

**Corrigé commenté**

**(a) Découpage proposé**

| Anneau | Composition | Nb | Durée d'observation | Justification |
|---|---|---|---|---|
| **0 — Laboratoire** | 4 machines de test, dont 1 image R&D | 4 | 1 j | Valide l'installation, pas l'usage |
| **1 — Pilote représentatif** | 6 siège bureautique · 4 R&D · **2 commerciaux** · 1 industriel bureautique | 13 | 3 j | **Les quatre profils dès le pilote** |
| **2 — Élargi** | 40 siège · 20 R&D · 10 commerciaux · 6 industriel | 76 | 5 j | Couvre les applications métier en usage réel |
| **3 — Général** | Reste siège (134) + reste R&D (66) | 200 | — | Volume |
| **4 — Sensibles et contraints** | 22 direction/RH · 12 industriel bureautique restant | 34 | Unitaire | Données sensibles, horaires 3×8 |
| **Hors anneaux** | 11 supervision C4 | 11 | — | Régime distinct |
| **Population séparée** | 28 nomades restants | 28 | Suivi propre | Voir (c) |

**Pourquoi la direction et les RH en anneau 4 et non en anneau 1** : ils portent les données les plus sensibles, et une régression sur la paie a un coût politique disproportionné. Ils bénéficient de l'observation faite sur les 289 postes précédents.

**(b) Critères de passage — formulaire D.6 rempli**

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre |
|---|---|---|---|
| Taux d'échec d'installation | `> 5 %` | Console de déploiement | Continu |
| Incidents déclarés liés | `≥ 3 sur l'anneau` | Support N1 | 24 h |
| **Transactions abouties — gestion commerciale** | `baisse > 10 % sur 30 min` | Supervision applicative | Continu |
| **Éditions de paie abouties** | `tout échec` | Supervision applicative | Continu (anneau 4) |
| Redémarrages inattendus | `≥ 2 machines` | Supervision poste | Continu |

**Critère de passage** : tous les seuils respectés pendant la durée d'observation **et** aucun incident bloquant ouvert **et** validation explicite du référent métier de la gestion commerciale pour le passage à l'anneau 3.

Le dernier point est ajouté à cause des deux régressions signalées publiquement : il est justifié ici, et ne le serait pas sur un correctif sans antécédent.

**(c) Les nomades — trois mesures**

1. **Deux d'entre eux dès l'anneau 1.** C'est là que se révèlent les problèmes de déploiement hors réseau interne : téléchargement sur liaison lente, échec de reprise, interruption pendant l'installation.
2. **Mécanisme fonctionnant sur Internet**, sans passage obligatoire par le réseau interne.
3. **Population suivie séparément**, avec une échéance plus longue (`J+45` au lieu de `J+21`) mais **mesurée**. Ils ne sont ni fondus dans le taux global, ni exclus silencieusement (§15.6).

⚠️ Une erreur fréquente consiste à leur appliquer l'échéance générale et à constater un taux de conformité dégradé chaque mois, sans jamais traiter la cause.

**(d) Les 11 postes de supervision**

Régime C4 : hors campagne. Correctif soumis à validation constructeur, application lors de la fenêtre de relève d'équipe ou de l'arrêt de production. Dans l'intervalle, compensation selon le §20.2. Ils figurent au tableau de bord comme **population distincte**, avec leur propre indicateur de compensation vérifiée — jamais fondus dans le taux général (§10.11).

**(e) La contrainte de 21 jours**

Elle n'est **pas tenable** telle quelle : 1 + 3 + 5 jours d'observation = 9 jours avant l'anneau 3, auxquels s'ajoutent le déploiement sur 200 postes, l'anneau 4 unitaire, et la traîne longue. Le calendrier réaliste est de 28 à 32 jours pour l'ensemble, hors nomades.

**Trois réponses possibles, à arbitrer explicitement** :

| Option | Effet | Coût |
|---|---|---|
| Compresser les durées d'observation à 1 j / 3 j | Gain de 4 jours | Augmente le risque de régression massive — inacceptable ici vu les antécédents |
| Paralléliser les anneaux 3 et 4 | Gain de 3 jours | Prive l'anneau 4 du bénéfice de l'observation |
| **Négocier l'échéance à 30 jours** | Calendrier tenable | Documenter le dépassement et sa justification |

La troisième est la bonne réponse dans ce cas : le constat n'est pas exploité, et le §16.5 rappelle qu'un délai qu'on ne tient pas produit une non-conformité permanente. **Un délai renégocié et documenté vaut mieux qu'un délai affiché et manqué.**

**Les trois erreurs attendues**

1. Composer l'anneau 1 uniquement de postes de l'équipe informatique : le correctif s'installera parfaitement, et la régression sur la gestion commerciale apparaîtra en anneau 3, sur 200 postes.
2. Placer la direction et les RH en anneau 1 « parce qu'ils sont peu nombreux ».
3. Accepter les 21 jours sans le dire, et livrer un taux dégradé un mois plus tard sans explication.

## 18.13 🔬 Mini-lab 6 — Produire la preuve d'une campagne

**Objectif** — Constituer un dossier de preuve recevable en audit et distinguer preuve recevable, contestable et irrecevable.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** §2.9, §18.9, §15.6 · **Livrable** dossier de preuve en six pièces (D.13).
**Compétences validées** — ✔ constituer un dossier de preuve recevable ✔ identifier le vrai dénominateur d'une campagne ✔ vérifier un état sur échantillon ✔ classer une preuve en recevable / contestable / irrecevable

**Données fournies**

Campagne `CAMP-2027-04`, correctif système sur serveurs Linux. Extraits bruts fournis :

*Extrait 1 — rapport de la console de déploiement, exporté le 22/04/2027 à 09 h 14*

```
Campagne CAMP-2027-04 — cible : groupe "SRV-LINUX-PROD"
  Succès ................ 168
  Échec ................. 5
  Non joignable ......... 3
  Total ciblé ........... 176
```


*Extrait 2 — périmètre de référence, extraction du 01/04/2027*

```
Serveurs Linux, environnement = production ....... 181
   dont couverts par la console de déploiement ... 176
   dont hors console (motif non renseigné) ....... 5
```


*Extrait 3 — détail des échecs, journal de la console*

```
srv-app-07   ERR_DISK_SPACE      /var 98% plein
srv-app-11   ERR_DISK_SPACE      /var 97% plein
srv-bdd-03   ERR_LOCK            paquet verrouillé par une transaction en cours
srv-web-09   ERR_DEPENDENCY      prérequis manquant
srv-int-02   ERR_TIMEOUT         pas de réponse après 3 tentatives
```


*Extrait 4 — non joignables*

```
srv-lab-04   dernier contact 12/02/2027
srv-old-01   dernier contact 30/11/2026
srv-tst-06   dernier contact 19/04/2027
```


**Questions**
(a) Quelles six pièces produisez-vous ?
(b) Quel est le vrai dénominateur, et que vaut le taux de réussite annoncé ?
(c) Quelle est la faiblesse d'un rapport de console seul, et comment la comblez-vous ?
(d) Traitez les 8 actifs restants **et** les 5 hors console.
(e) Classez trois formulations en preuve recevable, contestable, irrecevable.

---

**Corrigé commenté**

**(a) Le dossier en six pièces**

| # | Pièce | Contenu pour ce cas |
|---|---|---|
| 1 | Périmètre | 181 serveurs éligibles, dont 176 ciblés et **5 hors console — motif à documenter** |
| 2 | Décision | Ticket de triage, chemin dans l'arbre, échéance |
| 3 | Exécution | Extrait 1 daté et non retouché, avec les trois populations |
| 4 | **Vérification indépendante** | État constaté sur 18 serveurs tirés au sort (≈ 10 %), horodaté, méthode décrite |
| 5 | Traîne longue | Les 8 en échec ou non joignables + les 5 hors console, avec cause et échéance |
| 6 | Clôture | Date, responsable, issue, preuve rattachée |

**(b) Le dénominateur**

| Formulation | Valeur | Statut |
|---|---|---|
| « 95 % de réussite » (168/176) | 95 % | **Réussite de la campagne dans sa cible** |
| Sur les serveurs éligibles | 168/181 = **93 %** | Le chiffre à publier |
| Non mesuré | 5 hors console + 3 non joignables = **8 (4,4 %)** | À publier séparément |

Les 5 serveurs hors console sont le point le plus important de l'exercice : ils n'apparaissent **ni** dans le numérateur, **ni** dans le dénominateur de la console. C'est l'écart de type 3 du §10.3 — déclarés, actifs, jamais atteints.

**(c) La faiblesse du rapport de console**

Il rapporte ce que l'outil **croit** avoir fait. Il n'établit ni que le code corrigé s'exécute — un redémarrage a-t-il eu lieu ? — ni que la console couvre bien le périmètre éligible.

Les trois conditions de recevabilité (§2.9) : périmètre défini et rapproché du périmètre de référence · intégrité de l'extraction (datée, non retouchée) · liste des non joignables fournie. L'échantillon vérifié indépendamment est ce qui transforme un rapport en preuve.

🧪 **La vérification à réaliser sur l'échantillon**

```bash
# Sur chacun des 18 serveurs tirés au sort
dnf history info $(dnf history list | awk 'NR==3{print $1}')   # ou dpkg/apt selon la famille
uptime -s                                                       # date du dernier démarrage
needs-restarting -r ; echo "code retour : $?"                   # redémarrage encore requis ?
```


Le troisième contrôle est le plus important : un correctif installé sans redémarrage laisse le code vulnérable en mémoire (§2.6).

**(d) Traitement des 13 actifs**

| Groupe | Cause | Action | Échéance |
|---|---|---|---|
| srv-app-07, srv-app-11 | Espace disque | Libérer `/var`, relancer. **Cause racine** : aucune supervision de l'espace disque sur ces serveurs | 48 h |
| srv-bdd-03 | Transaction verrouillée | Relancer hors fenêtre de traitement | 48 h |
| srv-web-09 | Prérequis manquant | Installer le prérequis puis relancer. Vérifier si d'autres serveurs sont concernés | 5 j |
| srv-int-02 | Pas de réponse | Vérifier l'état de la machine — agent, réseau, ou machine arrêtée | 5 j |
| srv-lab-04, srv-old-01 | Sans contact depuis 2 et 5 mois | **Candidats au décommissionnement** (§10.3) — vérifier l'existence, sinon PV | 15 j |
| srv-tst-06 | Sans contact depuis 3 jours | Probablement éteint temporairement : relance automatique | 15 j |
| **5 serveurs hors console** | **Motif non renseigné** | **Priorité maximale** : les rattacher à la console ou documenter l'exclusion | 10 j |

**(e) Recevable, contestable, irrecevable**

| Formulation | Statut | Pourquoi |
|---|---|---|
| « Rapport de console du 22/04/2027 09 h 14, périmètre 176 serveurs rapproché des 181 éligibles, 3 non joignables listés, complété d'un relevé d'état horodaté sur 18 serveurs tirés au sort » | **Recevable** | Périmètre, intégrité, non joignables, vérification indépendante |
| « Rapport de console : 95 % de réussite » | **Contestable** | Exact, mais sans périmètre ni dénominateur : l'auditeur demandera les 5 % et les 5 serveurs hors console |
| « L'équipe confirme que la campagne s'est bien déroulée » | **Irrecevable** | Déclaration sans donnée (§5.6) |

**Les deux erreurs attendues**

1. Publier 95 % sans mentionner les 5 serveurs hors console — le chiffre est exact et le périmètre est faux.
2. Considérer la campagne close à 95 % : les 4,4 % non traités concentrent l'essentiel du risque résiduel (§18.10).

## 18.14 🔴 FIL ROUGE — avril 2027 : la nuit du déploiement raté

Campagne de montée de version mineure sur le cluster de bases de données d'HelioLink — trois nœuds, classe C1. Correctif de sécurité, vulnérabilité non exploitée mais gravité élevée, échéance à 30 jours.

**Ce qui était prévu.** Fenêtre samedi 22 h - 2 h. Test préalable en recette : concluant. Retour arrière annoncé par instantané des trois machines virtuelles. Malik Ferhaoui et un ingénieur d'astreinte.

**Ce qui s'est passé.** À 22 h 40, le premier nœud est mis à jour et redémarre normalement. À 22 h 55, la réplication ne repart pas : les deux versions ne se synchronisent pas. Le correctif embarquait une modification du format de réplication, mentionnée en dernière ligne des notes de version, sous une rubrique que personne n'avait lue.

À 23 h 10, décision de retour arrière. L'instantané est restauré : le nœud revient à sa version antérieure. Mais la réplication ne repart toujours pas — le nœud restauré est désormais en retard de quarante minutes de transactions, et le mécanisme de rattrapage automatique refuse de s'engager au-delà d'un certain écart.

À 1 h 20, après une resynchronisation complète manuelle, le service est rétabli. Aucune donnée perdue. Quatre heures d'indisponibilité de la plateforme de télésuivi, un dimanche matin — période de faible usage, mais deux établissements clients ont appelé le support.

**Les quatre causes racines identifiées au retour d'expérience :**

| Cause | Ce qui aurait évité |
|---|---|
| Notes de version lues en diagonale | La qualification en six questions du §18.2, notamment « quels prérequis » |
| Test en recette sur un **nœud unique**, pas sur un cluster | L'écart de représentativité du §6.12, non mesuré |
| Plan de retour arrière testé sur une machine isolée | Le test du §18.8 sur un actif **représentatif**, cluster inclus |
| Aucun critère d'arrêt écrit | La décision de retour arrière a pris 15 minutes de discussion |

**Ce qui n'a pas mal fonctionné**, et que Claire Nadeau tient à souligner au comité : la fenêtre était correcte, l'astreinte était en place, l'instantané existait, et aucune donnée n'a été perdue. L'incident aurait pu être bien pire sans ces éléments.

**Les trois mesures.**

1. La qualification en six questions devient un **champ obligatoire** du dossier de campagne pour toute classe C1 — avec la référence exacte de la section des notes de version consultée.
2. Le test de retour arrière doit être réalisé **sur une topologie représentative**. L'écart entre recette et production est désormais mesuré sur les quatre axes du §6.12 et affiché dans le dossier de campagne.
3. Les critères d'arrêt et le décideur sont écrits **avant** l'intervention, dans la demande de changement.

**Livrable de l'épisode.** Le dossier de campagne standard d'HELIOMED, en Annexe D : qualification, écart de représentativité, anneaux, critères d'arrêt, plan de retour arrière chronométré, décideur nommé.

→ La suite en 🔴 §19.11, quand il faudra choisir l'outillage capable de porter tout cela.

→ **Chapitre 19 — Outillage de déploiement par plateforme** : l'outillage — familles, critères de choix et limites structurelles.

## Synthèse mentale du chapitre 18

Neuf étapes composent la chaîne, dont trois sont systématiquement escamotées : qualifier le correctif, vérifier après déploiement, produire la preuve. La qualification en six questions coûte quinze minutes et évite l'essentiel des incidents — la question des régressions déjà signalées est la plus rentable. Le délai d'observation est un outil distinct des tests, et souvent plus efficace pour un coût nul. Les anneaux échouent pour deux raisons : un pilote non représentatif, qui valide qu'un correctif s'installe et non qu'il ne casse rien, et l'absence de critère de passage écrit. Le plan de retour arrière doit être chronométré, car c'est sa durée mesurée qui décide si vous osez déployer. La vérification fonctionnelle est celle qui manque toujours et qui détecte les régressions silencieuses. Enfin, une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée : ces 3 % concentrent une part disproportionnée du risque.

**Trois questions de vérification**

1. Citez les trois étapes de la chaîne les plus souvent escamotées et, pour chacune, la conséquence concrète de son absence.
2. Votre anneau pilote est composé des postes de l'équipe informatique. Qu'est-ce que cela valide réellement, et qu'est-ce que cela laisse passer ?
3. Une campagne affiche 97 % de réussite. Pourquoi ne pouvez-vous pas la clore, et que devez-vous produire sur les 3 % restants ?

---
