---
title: 'Chapitre 6 — Architecture maintenable : le MCS by design'
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

## 6.1 La thèse du chapitre

Les chapitres précédents décrivaient comment maintenir ce qui existe. Celui-ci change de moment : il traite des décisions prises **avant** la mise en service, et qui déterminent le coût de tout le reste.

> **Un système mal conçu pour être mis à jour produira de la dette de sécurité, quelle que soit la qualité du processus de MCS qui s'y applique.**

Ce n'est pas une opinion, c'est une conséquence mécanique. Si arrêter un système coûte 40 000 € de production perdue, aucune politique de correctifs ne convaincra qui que ce soit de l'arrêter chaque mois. Si une application est couplée à une version précise de son environnement d'exécution, aucun outil ne permettra de faire évoluer cet environnement. Si aucun retour arrière n'existe, chaque correctif restera une prise de risque non couverte, et sera reporté.

Le corollaire est encourageant : **les gains les plus importants du MCS ne s'obtiennent pas en exploitation, ils s'obtiennent en conception** — et ils ne coûtent presque rien s'ils sont décidés au bon moment.

Ce chapitre s'adresse à trois publics : ceux qui conçoivent des systèmes, ceux qui les achètent ou les font réaliser, et ceux qui les exploitent et doivent expliquer pourquoi ils n'y arrivent pas.

## 6.2 La maintenabilité comme exigence opposable

Le problème pratique : la maintenabilité de sécurité n'apparaît dans aucun cahier des charges, donc personne n'y répond, donc elle n'existe pas.

La solution consiste à la formuler comme une exigence explicite, vérifiable en revue de conception et opposable à un fournisseur. Sept exigences suffisent à couvrir l'essentiel.

| # | Exigence | Formulation opposable |
|---|---|---|
| 1 | Interruptibilité | « Le système supporte l'arrêt d'un composant sans interruption de service pour l'utilisateur » |
| 2 | Découplage de version | « Le système n'impose pas une version figée de son système d'exploitation, de son environnement d'exécution ou de sa base de données » |
| 3 | Réversibilité | « Toute mise à jour dispose d'une procédure de retour arrière documentée et testée » |
| 4 | Observabilité du changement | « Le système expose des indicateurs permettant de constater un effet de bord dans les minutes suivant une mise à jour » |
| 5 | Cadence supportée | « Le système supporte l'application de correctifs de sécurité à une cadence mensuelle » |
| 6 | Inventoriabilité | « Le système déclare ses composants et leurs versions de manière lisible par une machine » |
| 7 | Fin de vie | « Le fournisseur s'engage sur une durée de support et un préavis de fin de support » |

✅ **BONNE PRATIQUE (P0)** — Insérez ces sept exigences dans vos cahiers des charges et vos grilles de revue d'architecture. Elles ne coûtent rien à écrire, elles se négocient au moment où vous avez encore un levier — avant la signature — et elles vous éviteront des années de dérogations. Les exigences 2, 3 et 7 sont celles qui produisent le plus d'effet.

## 6.3 Redondance et haute disponibilité réellement compatibles avec la mise à jour

**L'idée de base.** Si un service tourne sur deux instances au lieu d'une, vous pouvez en arrêter une pour la corriger pendant que l'autre continue de servir. La redondance transforme une interruption de service en simple réduction de capacité. C'est le levier le plus direct entre architecture et MCS.

**Ce qui la rend inopérante en pratique.** Il existe beaucoup de redondances de façade.

⚠️ **PIÈGE — les cinq faux clusters**

| Configuration | Pourquoi ça ne tient pas |
|---|---|
| Deux instances, mais capacité dimensionnée pour deux | En arrêter une sature l'autre : vous ne pouvez plus jamais patcher aux heures ouvrées |
| Deux instances, une base de données unique | La base reste un point unique de panne — et c'est elle qu'il faut corriger |
| Redondance active/passive jamais basculée | La bascule n'a pas été testée depuis 2021 ; personne n'ose |
| Instances redondées, session utilisateur non partagée | Chaque bascule déconnecte les utilisateurs : les métiers refusent |
| Redondance sur le service, pas sur ses dépendances | Le service est doublé, l'annuaire ou le stockage ne l'est pas |

**Le test de vérité**, à poser en revue d'architecture : *pouvez-vous arrêter un membre de ce cluster, maintenant, en pleine journée, sans prévenir personne ?* Si la réponse n'est pas un oui franc, la redondance existe pour la panne, pas pour la maintenance — et c'est une distinction que beaucoup d'organisations découvrent trop tard.

## 6.4 Trois stratégies de déploiement, et quand chacune vaut son coût

| Stratégie | Principe | Coût | Retour arrière | Adaptée à |
|---|---|---|---|---|
| **Progressive** (*rolling*) | Remplacement instance par instance | Faible | Lent (repasser en sens inverse) | Services sans état, nombreuses instances |
| **Bleu / vert** | Deux environnements complets, bascule du trafic | Élevé (double infrastructure) | **Immédiat** | Systèmes critiques, fenêtres impossibles |
| **Témoin** (*canary*) | Une petite fraction du trafic sur la nouvelle version | Moyen | Rapide | Tout ce dont on veut mesurer l'effet réel |

**Ce qu'il faut vraiment retenir.** Ces stratégies ne servent pas seulement à déployer des fonctionnalités : elles sont l'outil qui permet d'appliquer un correctif **sans pari**. Le déploiement témoin en particulier répond exactement au dilemme du chapitre 18 — corriger vite tout en limitant l'impact d'une régression.

📌 **LIMITES** — Aucune de ces stratégies ne s'applique telle quelle à un composant à état : une base de données, un annuaire, un automate industriel. Elles supposent que l'on peut faire coexister deux versions, ce qui nous amène au point suivant.

## 6.5 Découpler le déploiement de l'activation

Un mécanisme simple change profondément la gestion du risque : séparer **installer le code** de **activer le comportement**.

Un interrupteur de fonctionnalité (*feature flag*) est un paramètre qui active ou désactive un comportement sans redéployer. Le bénéfice pour le MCS est direct et sous-estimé :

- vous déployez la nouvelle version avec le nouveau comportement désactivé, donc sans risque fonctionnel ;
- vous activez ensuite progressivement, sur une population réduite ;
- en cas de problème, vous **désactivez en quelques secondes** au lieu de redéployer l'ancienne version.

C'est aussi le mécanisme qui rend possible une mesure compensatoire propre : désactiver une fonctionnalité vulnérable en attendant le correctif, sans arrêter le service (chapitre 20).

⚠️ **PIÈGE** — Les interrupteurs s'accumulent. Un système comptant 400 interrupteurs dont personne ne connaît l'état est devenu impossible à raisonner, et les combinaisons non testées deviennent la norme. Fixez une durée de vie : un interrupteur temporaire qui dépasse six mois est soit supprimé, soit promu en paramètre de configuration documenté.

## 6.6 Compatibilité entre versions et contrats d'interface

Pour qu'un déploiement progressif fonctionne, deux versions doivent **coexister** — au moins quelques minutes, parfois plusieurs jours. Cela impose une discipline.

**La compatibilité descendante** : la nouvelle version doit continuer à comprendre ce que produit l'ancienne. **La compatibilité ascendante**, plus rarement pensée : l'ancienne version ne doit pas se casser en recevant ce que produit la nouvelle.

**Les règles pratiques qui suffisent dans 90 % des cas :**

- ajouter un champ, jamais en supprimer ni en renommer dans la même version ;
- ne jamais changer le sens d'un champ existant ;
- déprécier avant de supprimer, avec un délai annoncé et mesuré ;
- versionner explicitement les interfaces exposées à d'autres équipes ou à des clients ;
- traiter un point d'accès déprécié comme un actif à décommissionner (chapitre 35), avec une date.

**Le lien avec le MCS est direct** : une interface sans compatibilité impose un déploiement synchronisé de tous les composants, donc une interruption globale, donc une fenêtre rare, donc du report.

## 6.7 Migrations de schéma : le point de non-retour

C'est le cas le plus dangereux du chapitre, parce qu'il annule silencieusement votre plan de retour arrière.

**Le mécanisme.** Une mise à jour applicative modifie la structure de la base de données. Le code applicatif, lui, se réinstalle facilement en version antérieure. Les **données**, non : elles ont été transformées. Vous pouvez redéployer l'ancienne version du code, elle ne saura plus lire la base.

**Ce que ça implique.** Le retour arrière cesse d'être une opération technique de quelques minutes pour devenir une **restauration de sauvegarde**, avec perte de toutes les transactions depuis la migration. La différence, en durée d'indisponibilité, est d'un facteur cent.

🧪 **EN PRATIQUE — la migration en expansion / contraction**

La méthode qui préserve la réversibilité consiste à découper en trois temps ce qu'on fait habituellement en un seul :

```
Étape 1 — Expansion   : ajouter la nouvelle structure, SANS retirer l'ancienne
                        → les deux versions du code fonctionnent
Étape 2 — Migration   : le nouveau code écrit dans les deux structures
                        → réversible à tout moment
Étape 3 — Contraction : retirer l'ancienne structure, une fois la stabilité confirmée
                        → point de non-retour, franchi consciemment et à froid
```


Entre l'étape 1 et l'étape 3, le retour arrière reste trivial. Le point de non-retour n'est pas supprimé, il est **déplacé** à un moment que vous choisissez, au calme, plutôt que subi en pleine nuit.

✅ **BONNE PRATIQUE (P1)** — Toute demande de changement impliquant une migration de schéma doit indiquer explicitement, dans son plan de retour arrière : *à partir de quel instant précis le retour arrière ne sera plus possible sans restauration de données*. Cette seule ligne change la nature de la discussion en comité.

## 6.8 Observabilité et critères d'arrêt automatiques

Déployer progressivement ne sert à rien si vous ne savez pas détecter que ça se passe mal. C'est pourtant la situation la plus fréquente : on déploie sur 5 % du parc, puis on attend « un peu », puis on continue — sans critère.

**Ce qu'il faut mesurer, avant / pendant / après.** Trois familles suffisent :

| Famille | Exemples | Ce qu'elle détecte |
|---|---|---|
| Santé technique | Taux d'erreur, temps de réponse, redémarrages inattendus, consommation mémoire | Régression franche |
| Santé fonctionnelle | Nombre de transactions métier abouties par minute | Régression silencieuse : le service répond, mais ne fait plus son travail |
| Santé du déploiement | Taux d'échec d'installation, actifs non joignables, écarts de version | Problème de la campagne elle-même |

La deuxième ligne est celle qu'on oublie, et c'est la plus importante. Un service qui répond « 200 OK » à toutes les requêtes tout en ayant cessé d'enregistrer les commandes passe tous les contrôles techniques.

**Le critère d'arrêt automatique.** Un déploiement doit s'interrompre **tout seul** quand un seuil est franchi, sans attendre qu'un humain regarde un écran. Formulez-le à l'avance et de manière chiffrée : *si le taux d'erreur dépasse X sur Y minutes, ou si le volume de transactions abouties baisse de Z %, la campagne s'arrête et alerte.*

⚠️ **PIÈGE — le seuil défini après le déploiement**
Un seuil discuté pendant l'incident sera toujours interprété dans le sens de « on continue » : personne n'aime arrêter une campagne à moitié faite. Le seuil doit être écrit dans la demande de changement, avant.

## 6.9 Le retour arrière : ce qui est réellement réversible

Reprenons le §2.5 et généralisons.

| Objet | Réversibilité réelle | Mécanisme à privilégier |
|---|---|---|
| Application sans état | Élevée | Redéploiement de la version antérieure |
| Conteneur | Très élevée | Redéploiement de l'image précédente |
| Machine virtuelle | Élevée | Instantané pris avant l'intervention |
| Correctif de système d'exploitation | **Variable, à vérifier** | Instantané ou redéploiement, jamais la désinstallation seule |
| Micrologiciel | Faible à nulle | Double partition d'image quand elle existe (§2.7) |
| Migration de schéma | **Nulle après contraction** | Découpage expansion/contraction (§6.7) |
| Modification d'annuaire | Faible | Sauvegarde autorisée + procédure documentée |

**La règle unique** : un plan de retour arrière **non testé** n'est pas un plan, c'est une intention. Testez-le sur un environnement représentatif, chronométrez-le, et notez sa durée dans la demande de changement — parce que c'est cette durée, et non la probabilité de l'incident, qui déterminera si vous osez déployer.

## 6.10 Images immuables : la correction devient un déploiement ordinaire

Le §3.5 a présenté le principe. Voici ce qu'il change concrètement pour le MCS.

Dans un modèle mutable, corriger consiste à intervenir sur un système en fonctionnement : opération d'exception, à risque, difficile à répéter à l'identique, et qui laisse le système dans un état légèrement différent de tous les autres.

Dans un modèle immuable, corriger consiste à **reconstruire l'image de référence et à redéployer**. Autrement dit : la correction emprunte exactement le même chemin, les mêmes tests et les mêmes automatismes qu'une livraison applicative ordinaire. Elle cesse d'être un sujet à part.

Quatre bénéfices, tous directement mesurables :

1. la dérive de configuration disparaît par construction (chapitre 23) ;
2. le retour arrière devient trivial : redéployer l'image précédente ;
3. la preuve devient triviale : l'identifiant d'image porte l'information de version ;
4. le nombre de constats individuels s'effondre au profit d'un seul indicateur — l'âge de l'image.

📌 **LIMITES** — Le modèle ne s'applique pas à tout : composants à état, systèmes industriels, matériel physique, appliances fournisseur. Et il déplace la charge vers la chaîne de construction, qui devient elle-même un actif critique à maintenir (chapitre 28).

## 6.11 Concevoir un mécanisme de mise à jour sécurisé

Cette section concerne ceux qui **fabriquent** un produit installé chez des clients — matériel connecté, logiciel embarqué, appliance, application déployée sur site. Elle est reprise et approfondie au chapitre 33.

Un mécanisme de mise à jour est un chemin d'exécution privilégié offert au fournisseur. Mal conçu, il devient un chemin d'exécution privilégié offert à un attaquant. Six propriétés le rendent sûr.

| Propriété | Ce qu'elle empêche |
|---|---|
| **Authenticité** | Le produit vérifie la signature de la mise à jour avant installation — sinon n'importe qui peut livrer du code |
| **Intégrité** | Empreinte vérifiée, transport protégé — contre l'altération en chemin |
| **Protection contre le retour en arrière** | Refus d'installer une version antérieure vulnérable — sinon l'attaquant « rétrograde » pour retrouver une faille |
| **Atomicité** | Installation complète ou nulle, jamais à moitié — une coupure de courant ne doit pas produire un équipement inutilisable |
| **Repli sûr** | En cas d'échec, retour automatique à la version précédente fonctionnelle |
| **Traçabilité** | Le produit sait dire quelle version il exécute, et le fournisseur sait quelles versions sont déployées |

⚠️ **PIÈGE — le mécanisme qui n'existe pas**
Beaucoup de produits industriels et connectés se mettent à jour par intervention manuelle sur site, avec un support amovible. C'est un choix de conception dont la conséquence est mécanique : la cadence de correction sera annuelle au mieux. Si vous **achetez** un tel produit, sachez-le avant, pas après — c'est l'exigence n° 5 du §6.2. Si vous le **fabriquez**, c'est une dette qui deviendra réglementaire (chapitre 33).

## 6.12 Des environnements de test réellement représentatifs

Toutes les stratégies de ce chapitre supposent qu'on puisse tester avant. Or c'est le maillon le plus faible en pratique.

**Les cinq écarts qui font qu'un test ne prouve rien :**

| Écart | Ce qu'il laisse passer |
|---|---|
| Volume de données sans commune mesure | Les régressions de performance, invisibles sur 200 lignes |
| Versions différentes de celles de production | Le test valide autre chose que ce que vous déploierez |
| Intégrations tierces simulées | Tout ce qui casse à la frontière — c'est-à-dire l'essentiel |
| Configuration divergente | Les effets liés au durcissement, aux droits, au réseau |
| Environnement figé depuis des mois | Il ne représente plus rien, y compris sa propre sécurité (chapitre 28) |

✅ **BONNE PRATIQUE (P1)** — Plutôt que de viser un environnement de recette parfait — objectif rarement atteint —, mesurez et affichez l'**écart** entre recette et production sur quatre axes : versions, volumétrie, intégrations, configuration. Un écart connu se compense par un déploiement témoin plus prudent ; un écart ignoré produit de la fausse confiance, ce qui est bien pire que pas de test du tout.

## 6.13 Le coût réel d'un système impossible à arrêter

Voici l'argument à porter en comité, parce qu'il transforme une exigence technique en décision économique.

**La formulation.** Un système non interruptible impose un coût récurrent qui n'apparaît dans aucun budget :

- l'interruption est repoussée jusqu'à une fenêtre annuelle, donc le délai moyen de correction se compte en mois ;
- chaque intervention devient un projet, avec préparation, validation, mobilisation nocturne, astreinte ;
- l'exposition prolongée impose des mesures compensatoires, qui ont leur propre coût de mise en œuvre et de surveillance (chapitre 20) ;
- le risque résiduel est porté par l'organisation pendant toute la période.

**La comparaison à présenter.** Mettez face à face le coût d'ajout de la redondance — souvent une instance supplémentaire et quelques jours d'ingénierie — et le coût annuel du non-interruptible : heures d'astreinte, mesures compensatoires, surveillance dédiée, temps de négociation, et le montant du risque accepté. Dans la plupart des cas, l'écart est spectaculaire, et il n'a jamais été calculé.

C'est l'un des rares arguments de MCS qui se gagne sur le terrain financier plutôt que sur le terrain du risque. Le chapitre 37 en fait un outil de dossier d'investissement.

## 6.14 ✅ Livrable — Grille d'évaluation de la maintenabilité sécurisée

À utiliser en revue d'architecture, en évaluation d'un progiciel, ou en état des lieux d'un système existant. Notation : **0** absent · **1** partiel · **2** satisfaisant.

| # | Critère | Question de vérification | Prio |
|---|---|---|---|
| 1 | Interruptibilité | Peut-on arrêter un composant en journée sans impact utilisateur ? | **P0** |
| 2 | Redondance effective | La capacité restante suffit-elle avec un membre en moins ? | **P0** |
| 3 | Bascule testée | Quand la dernière bascule a-t-elle été réalisée, et par qui ? | **P0** |
| 4 | Retour arrière | Existe-t-il, est-il documenté, a-t-il été chronométré ? | **P0** |
| 5 | Point de non-retour | Est-il identifié et écrit dans la demande de changement ? | **P0** |
| 6 | Découplage de version | Le système impose-t-il une version figée d'un composant sous-jacent ? | **P0** |
| 7 | Cadence supportée | Le système supporte-t-il une correction mensuelle ? | P1 |
| 8 | Stratégie de déploiement | Progressive, bleu/vert ou témoin — laquelle, et est-elle outillée ? | P1 |
| 9 | Critères d'arrêt | Sont-ils chiffrés et automatiques ? | P1 |
| 10 | Observabilité fonctionnelle | Sait-on détecter un service qui répond mais ne fait plus son travail ? | P1 |
| 11 | Compatibilité d'interface | Deux versions peuvent-elles coexister ? | P1 |
| 12 | Inventaire des composants | Le système déclare-t-il ses composants et versions ? | P1 |
| 13 | Représentativité de la recette | L'écart avec la production est-il mesuré sur quatre axes ? | P1 |
| 14 | Mécanisme de mise à jour | Signé, atomique, avec repli et protection contre le retour en arrière ? | P1 |
| 15 | Engagement de support | Durée et préavis de fin de support contractualisés ? | P2 |
| 16 | Décommissionnement | La procédure de retrait est-elle prévue dès la conception ? | P2 |

**Lecture du résultat.** Un seul critère P0 à 0 suffit à qualifier le système de non maintenable en sécurité — et cette qualification doit figurer dans le dossier, avec ses conséquences chiffrées, plutôt que d'être découverte trois ans plus tard par l'équipe d'exploitation.

## 6.15 🔴 FIL ROUGE — avril 2026 : la revue d'architecture d'HelioLink

La grille du §6.14 est appliquée pour la première fois chez HELIOMED, non pas sur un système existant, mais sur la refonte de la plateforme de télésuivi HelioLink, dont le développement démarre à Nantes.

**Ce que la grille révèle en deux heures de réunion.**

| Critère | Note | Constat |
|---|---|---|
| Interruptibilité | 0 | Une seule instance applicative ; toute mise à jour coupe le service de télésuivi |
| Redondance effective | 0 | Base de données unique, non répliquée |
| Point de non-retour | 0 | Les migrations de schéma sont appliquées en une passe, sans découpage |
| Découplage de version | 1 | L'application impose une version précise d'un environnement d'exécution, déjà en fin de support dans 14 mois |
| Observabilité fonctionnelle | 0 | Supervision technique uniquement ; rien ne mesure les remontées de télésuivi abouties |

Yann Prigent, responsable produit, oppose l'argument habituel et parfaitement recevable : ajouter de la redondance représente quatre semaines d'ingénierie et une instance supplémentaire, alors que la mise sur le marché est déjà tendue.

**L'argument qui emporte la décision** n'est pas un argument de sécurité. Claire Nadeau applique le §6.13 et présente deux colonnes : le coût de la redondance, contre le coût annuel prévisionnel d'un système non interruptible sur un service de télésuivi médical — interventions nocturnes obligatoires, astreinte, fenêtres à négocier avec les établissements de santé clients, et surtout **impossibilité de corriger rapidement une vulnérabilité exposée sur un service traitant des données de santé**. La comparaison n'est pas serrée.

**Décisions prises.**

1. Redondance applicative et réplication de base de données ajoutées au périmètre initial — quatre semaines de décalage acceptées par la direction générale.
2. Découpage systématique des migrations de schéma en expansion / contraction, inscrit dans les règles de développement.
3. Deux indicateurs fonctionnels créés avant la mise en production, avec seuils d'arrêt automatique chiffrés.
4. Le point de découplage de l'environnement d'exécution est traité comme une dette datée, avec échéance inscrite au plan d'obsolescence (chapitre 12) — c'est un report assumé et tracé, pas un oubli.

**Livrable de l'épisode.** La grille du §6.14 devient un document de revue obligatoire pour tout nouveau projet chez HELIOMED, avec une règle simple : un critère P0 à zéro ne bloque pas le projet, mais impose une décision explicite de la direction générale, écrite et datée.

→ La suite en 🔴 §7.7, quand ces principes doivent devenir une politique applicable à l'ensemble du parc existant.

→ **Chapitre 7 — Doctrine et politique MCS** : la doctrine : transformer ces principes en une politique réellement applicable.

## Synthèse mentale du chapitre 6

Le coût du MCS se décide en conception, pas en exploitation : un système qu'on ne peut pas arrêter ne sera pas corrigé, quelle que soit la politique. Sept exigences de maintenabilité, écrites dans un cahier des charges, se négocient tant qu'on a encore un levier — avant la signature. La redondance ne sert le MCS que si elle survit au test « peut-on en arrêter un membre maintenant, en pleine journée » : les faux clusters sont nombreux. Les stratégies progressive, bleu/vert et témoin permettent de corriger sans pari, et les interrupteurs de fonctionnalité découplent le déploiement de l'activation, ce qui offre aussi une mesure compensatoire propre. Les migrations de schéma détruisent silencieusement la réversibilité : le découpage expansion/contraction déplace le point de non-retour à un moment choisi. Un déploiement doit s'arrêter tout seul sur des seuils chiffrés à l'avance, dont au moins un indicateur fonctionnel — un service peut répondre parfaitement tout en ayant cessé de faire son travail. Enfin, un plan de retour arrière non testé n'est pas un plan, et le coût d'un système non interruptible se démontre en euros, pas en risque.

**Trois questions de vérification**

1. Votre architecte affirme que le service est redondé et donc corrigeable sans interruption. Quelle question unique posez-vous pour vérifier, et quelles sont les trois réponses évasives typiques ?
2. Une mise à jour applicative comporte une migration de base de données. Que devez-vous obtenir avant d'autoriser le changement, et pourquoi cette information change-t-elle la nature du plan de retour arrière ?
3. Un chef de projet refuse d'ajouter une seconde instance pour cause de budget. Construisez l'argument économique en quatre postes de coût récurrent.

---

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> - **distinguer** le MCS du maintien opérationnel, et nommer les cinq causes récurrentes d'échec — dont aucune n'est exclusivement technique ;
> - **expliquer** pourquoi un numéro de version amont ne dit rien de la présence d'une faille sur un système à support long, et le vérifier en trois commandes ;
> - **situer** une frontière de responsabilité sur n'importe quelle couche d'abstraction : hyperviseur, conteneur, orchestrateur, cloud, industriel, micrologiciel ;
> - **lire** un constat de vulnérabilité sans confondre gravité, probabilité, exploitation avérée et exposition — et savoir laquelle de ces informations personne ne produira à votre place ;
> - **qualifier** une information en fait vérifié, hypothèse probable ou piste exploratoire ;
> - **poser** la question qui débloque le plus de situations : *qui décide qu'on l'arrête pour le corriger ?* ;
> - **évaluer** la maintenabilité d'un système en conception, et chiffrer le coût d'un système impossible à arrêter.
>
> **Ce que vous ne savez pas encore** : sur quoi exactement porte votre dispositif, qui arbitre, et ce que l'extérieur exige. C'est l'objet de la Partie II.
