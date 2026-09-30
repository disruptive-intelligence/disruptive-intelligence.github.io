---
title: Chapitre 26 — Bases de données, middlewares et runtimes
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 26.1 La couche intermédiaire

à jour côté système, vulnérable côté applicatif

C'est le cas le plus fréquent d'obsolescence invisible : le système d'exploitation est parfaitement à jour, les correctifs sont appliqués chaque mois, les indicateurs sont au vert — et l'application s'exécute sur un environnement dont le support a pris fin il y a deux ans.

**Pourquoi cette couche échappe au dispositif**, pour quatre raisons cumulées :

1. Elle est souvent **installée hors gestionnaire de paquets**, par l'éditeur métier ou par l'équipe applicative.
2. Elle est **embarquée dans l'application** : une même machine peut porter trois versions différentes d'un même environnement d'exécution.
3. Ses **cycles de support sont courts** — souvent deux à quatre ans, contre cinq à dix pour un système d'exploitation.
4. Elle n'appartient à personne : trop applicative pour l'exploitation, trop technique pour le métier.

## 26.2 Bases de données

| Objet | Ce qui se dégrade | Point d'attention |
|---|---|---|
| Version majeure | Fin de support, souvent 5 à 8 ans | Migration lourde : compatibilité applicative, tests |
| Version mineure | Correctifs de sécurité réguliers | Souvent différée par crainte d'indisponibilité |
| Moteur et extensions | Modules additionnels avec leur propre cycle | Rarement inventoriés |
| Configuration | Comptes par défaut, chiffrement, journalisation | Souvent la vulnérabilité réelle (ch. 22) |

**La spécificité opérationnelle** : une base de données est un composant **à état**. Les stratégies du §6.4 ne s'y appliquent pas directement, et le point de non-retour du §6.7 y est central. Trois configurations de correction, par ordre de préférence :

| Configuration | Interruption | Condition |
|---|---|---|
| Réplication avec bascule | Quelques secondes à minutes | Compatibilité entre versions pendant la transition (§2.7) |
| Fenêtre planifiée | Durée de l'opération | Standard, mais impose la fenêtre |
| Migration avec bascule applicative | Variable | Réservée aux montées de version majeures |

## 26.3 Compatibilité applicative et schémas

Ce qui bloque réellement une montée de version de base de données n'est presque jamais la base : c'est l'**application** qui s'appuie dessus.

| Blocage | Manifestation |
|---|---|
| Certification de l'éditeur métier | L'application n'est supportée que sur une version précise |
| Fonctionnalité dépréciée utilisée | Le code applicatif emploie une syntaxe supprimée |
| Comportement modifié | Tri, encodage, gestion des valeurs nulles : l'application fonctionne différemment |
| Pilote d'accès | Le connecteur ne supporte pas la nouvelle version |

**La conséquence pour le MCS** : la montée de version de base de données est un **projet applicatif**, pas une opération d'infrastructure. Elle se planifie avec l'équipe applicative et l'éditeur, avec le délai correspondant — souvent six à douze mois. D'où l'importance de l'anticipation du chapitre 12.

## 26.4 Serveurs web, mandataires et serveurs d'applications

Ces composants sont **exposés par nature** et traitent des entrées non fiables. Ils appartiennent presque toujours à la classe C1.

**Trois points spécifiques :**

- **Les modules et extensions** ont leur propre cycle : un serveur web à jour peut charger un module vulnérable non maintenu.
- **La configuration prime souvent sur la version** : en-têtes, méthodes autorisées, gestion des erreurs, limites de taille. Un serveur à jour mal configuré expose davantage qu'un serveur légèrement en retard bien configuré.
- **Le mandataire inverse est un point de contrôle privilégié** : c'est là que se placent les mesures compensatoires du §20.3, ce qui en fait aussi un actif critique.

## 26.5 Brokers, caches, moteurs de recherche, ordonnanceurs

Composants d'infrastructure applicative, souvent installés pour un besoin technique et jamais revus.

⚠️ **PIÈGE — le composant installé sans authentification**
Beaucoup de ces produits s'installent par défaut **sans authentification**, sur le principe qu'ils ne seront joignables que depuis un réseau de confiance. Cette hypothèse est fausse dès qu'un poste du réseau est compromis (§11.4). Ce sont des cibles de choix : ils contiennent souvent des données applicatives complètes, et parfois des secrets.

**Les trois vérifications** à mener sur chacun : authentification activée ? exposition réelle mesurée ? version supportée ?

## 26.6 Les *runtimes* applicatifs

Machines virtuelles applicatives, plateformes d'exécution, interpréteurs : c'est la source d'obsolescence invisible la plus fréquente.

| Caractéristique | Conséquence |
|---|---|
| Cycles de support courts | Une version sort du support avant que le projet ne soit terminé |
| Plusieurs versions cohabitent sur une même machine | L'inventaire par machine ne suffit pas |
| Souvent embarqué avec l'application | Aucun mécanisme système ne le met à jour |
| Version imposée par l'éditeur métier | Vous héritez de son calendrier (§13.6) |

✅ **BONNE PRATIQUE (P0)** — Inventoriez les environnements d'exécution **par application**, pas par machine, avec leur version et leur date de fin de support. C'est un exercice d'une à deux journées qui révèle presque toujours plusieurs composants hors support ignorés jusque-là.

## 26.7 Les bibliothèques natives embarquées

Le composant que personne ne déclare : bibliothèques de chiffrement, de compression, d'analyse de formats, livrées **à l'intérieur** d'une application, sans passer par le gestionnaire de paquets.

**Pourquoi c'est un angle mort complet** : le scanner système ne les voit pas (elles ne sont pas des paquets), l'analyse de composition ne les voit pas (elles ne sont pas dans les dépendances déclarées), et l'éditeur métier ne les mentionne pas. Elles n'apparaissent que dans un inventaire de composants fourni par l'éditeur — d'où l'importance de l'exiger (§13.6).

## 26.8 Pilotes, agents, extensions et greffons

Toute la surface ajoutée sur une machine par des besoins ponctuels : pilotes matériels, agents de supervision, extensions de navigateur, greffons applicatifs, utilitaires métier.

**Le traitement réaliste** : on n'inventorie pas tout. On inventorie ce qui s'exécute avec des privilèges élevés — pilotes et agents — et ce qui traite des entrées non fiables — extensions de navigateur, greffons de traitement de documents. Le reste relève de la maîtrise de ce qui est installé (§22.1).

## 26.9 Clients lourds et postes utilisateurs

Les postes portent eux aussi des environnements d'exécution et des bibliothèques embarquées, souvent installés par des applications métier et jamais mis à jour. C'est le prolongement du §19.5 : le trou noir du poste de travail ne se limite pas aux applications visibles.

## 26.10 Négocier la montée de version avec un éditeur métier

Situation la plus fréquente : votre environnement d'exécution est hors support, et l'éditeur de l'application refuse de supporter une version plus récente.

**La séquence qui fonctionne :**

1. **Écrire la demande**, avec la date de fin de support du composant et la référence de la source (§13.8).
2. **Demander un engagement daté** : à quelle date une version compatible sera-t-elle disponible ?
3. **En l'absence de réponse ou d'engagement**, formaliser une dérogation (§7.4) dont le signataire est le propriétaire métier, et dont le motif est explicitement *« l'éditeur ne fournit pas de version compatible »*.
4. **Inscrire le sujet au renouvellement contractuel** — c'est le seul moment où vous disposez d'un levier.
5. **Compenser** dans l'intervalle (chapitre 20).

**Ce que produit cette séquence**, au-delà de la protection technique : elle transforme un problème technique subi par l'exploitation en une décision de gestion assumée par le métier, avec une trace. C'est ce qui débloque, tôt ou tard, le budget de migration.

## 26.11 Environnements de développement, recette et préproduction

Ces environnements portent les mêmes composants intermédiaires que la production, et sont traités au chapitre 28. Un point ici : un environnement de recette dont l'environnement d'exécution diverge de la production **invalide les tests** (§6.12). L'écart de version fait partie des quatre axes à mesurer.

## 26.12 📌 Limites

- **Applications non maintenues** : l'éditeur a disparu, le code source n'est pas disponible. La seule voie est la sanctuarisation (chapitre 32).
- **Prérequis figés par contrat** : traité au §26.10, avec une issue souvent budgétaire.
- **Multiplicité des versions** : une organisation peut porter cinq versions d'un même environnement d'exécution pour cinq applications. La rationalisation est un projet en soi, dont le bénéfice de MCS est considérable.
- **Absence de propriétaire** : c'est la cause racine la plus fréquente. Cette couche doit être explicitement rattachée à un propriétaire technique (§10.4).

## 26.13 🔴 FIL ROUGE — novembre 2027

l'application de gestion commerciale

L'inventaire des environnements d'exécution **par application** (§26.6) est mené chez HELIOMED sur les 176 serveurs internes. Une journée et demie de travail.

**Le résultat.**

| Composant | Applications concernées | Statut |
|---|---|---|
| Environnement d'exécution A, version ancienne | 3 applications, dont la gestion commerciale | **Hors support depuis 2023** |
| Environnement d'exécution A, version courante | 9 applications | Supporté |
| Moteur de base de données, version N-2 | 2 applications | Fin de support dans 7 mois |
| Serveur d'applications, version ancienne | 1 application | **Hors support depuis 2024** |
| Bibliothèque de chiffrement embarquée | Inconnue — non déclarée par l'éditeur | **Non mesuré** |

**Le cas central : l'application de gestion commerciale.** Utilisée par 60 personnes, elle porte le fichier clients. Elle s'exécute sur un environnement hors support depuis 2023 — c'est celle du mini-lab 7 (§20.10), dont la dérogation expire le 31 mars 2028.

L'éditeur a été relancé trois fois depuis juin. Réponse obtenue en novembre, par écrit : une version compatible existe, elle est facturée 40 k€, et la version actuelle ne sera plus supportée du tout à compter de septembre 2028.

**Ce que change la réponse écrite.** Le sujet cesse d'être un arbitrage technique. Trois faits sont désormais établis et datés : le composant est hors support depuis quatre ans, une solution existe et son prix est connu, et une seconde échéance arrive en septembre 2028. Karim Lebrun inscrit les 40 k€ au budget 2028 en quinze minutes — ce que dix-huit mois de discussions techniques n'avaient pas obtenu.

**La découverte annexe, plus préoccupante.** Le serveur d'applications hors support depuis 2024 porte une application développée en interne en 2019, dont l'équipe a été dissoute lors d'une réorganisation. Personne ne sait la reconstruire. Le code source existe, mais aucune chaîne de construction fonctionnelle. C'est le cas limite du §26.12, et il est renvoyé au chapitre 32.

**La ligne « non mesuré ».** La bibliothèque de chiffrement embarquée dans le progiciel métier n'est pas déclarée par l'éditeur. La demande d'inventaire des composants est intégrée au courrier de renouvellement contractuel, en application du §13.6 — première application concrète de l'effet de propagation réglementaire du §25.20.

**Livrable de l'épisode.** L'inventaire des composants intermédiaires par application, versé au référentiel d'obsolescence du chapitre 12, avec trois échéances datées et une ligne non mesurée assumée.

→ La suite en 🔴 §27.7, quand la question des micrologiciels reviendra sans avoir jamais eu de propriétaire.

→ **Chapitre 27 — Couches basses et périphéries** : les couches basses, les moins visibles et les plus en retard.

## Synthèse mentale du chapitre 26

La couche intermédiaire — bases de données, serveurs d'applications, environnements d'exécution, bibliothèques embarquées — est la source d'obsolescence invisible la plus fréquente : système parfaitement à jour, indicateurs au vert, et une application qui s'exécute sur un composant hors support depuis deux ans. Quatre raisons se cumulent : installation hors gestionnaire de paquets, embarquement dans l'application, cycles de support courts, et absence de propriétaire. Ce qui bloque une montée de version de base de données n'est presque jamais la base mais l'application : c'est donc un projet applicatif de six à douze mois, pas une opération d'infrastructure. Les brokers, caches et moteurs de recherche s'installent souvent sans authentification, sur l'hypothèse d'un réseau de confiance qui devient fausse au premier poste compromis. Enfin, l'inventaire doit se faire **par application** et non par machine, et la négociation avec un éditeur métier récalcitrant se gagne par une demande écrite, un engagement daté et une dérogation signée par le métier — pas par la persuasion technique.

**Trois questions de vérification**

1. Vos serveurs affichent 98 % de conformité aux correctifs système. Quelle question posez-vous pour savoir si vos applications s'exécutent sur des composants supportés ?
2. Pourquoi une montée de version de base de données se planifie-t-elle sur six à douze mois plutôt que sur une fenêtre de maintenance ?
3. Un éditeur métier refuse de supporter une version récente de l'environnement d'exécution. Décrivez les cinq étapes de la séquence à suivre, et expliquez ce que produit l'étape 3 au-delà de la protection technique.

---
