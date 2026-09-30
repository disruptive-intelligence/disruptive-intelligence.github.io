---
title: Comprendre, lire et concevoir un système d'information
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 1
chapters: 10
---

**Tranches T1 à T8 — Cours intégral, chapitres 1 à 50**
*Version 1.8 · 2 août 2026*

---


## Les huit principes de lecture

*Ces principes s'appliquent aux cinquante chapitres. Ils portent chacun un nom, employé dans tout le cours, et une référence courte pour la production éditoriale.*

| # | Nom du principe | Énoncé |
|---|---|---|
| **R1** | **Principe des trois flux** | Métier, dépendance, exploitation — et ne jamais les confondre |
| **R2** | **Principe de la contrainte** | La taille ne justifie jamais une brique · la contrainte, oui |
| **R3** | **Principe de coupe** | On descend dans un mécanisme jusqu'au niveau nécessaire à la décision |
| **R4** | **Principe du coût** | Ajouter n'est jamais gratuit : contrainte résolue **et** coût introduit |
| **R5** | **Principe du visuel** | Le schéma porte l'information, il ne l'accompagne pas |
| **R6** | **Principe du modèle** | Un modèle pédagogique n'est pas une loi technique |
| **R7** | **Principe d'hypothèse** | Une observation produit une hypothèse, pas une identification |
| **R8** | **Principe de preuve** | Un schéma révèle une intention de redondance · seul un test établit une capacité |

### principe des trois flux — Trois familles de flux, pas deux

| Famille | Définition | Exemples | Effet de sa rupture |
|---|---|---|---|
| **Flux métier** | Ce que le service transporte ou traite | Une page, un fichier, une requête, un enregistrement | Le service ne rend plus son objet |
| **Flux de dépendance** | Ce **sans quoi le service ne peut pas s'établir** | Résolution de noms · authentification · validation de certificat · synchronisation d'horloge · découverte de service | **Le service s'arrête, sans qu'on comprenne pourquoi** |
| **Flux d'exploitation** | Ce qui permet de tenir, observer et restaurer le service | Journaux, métriques, supervision, sauvegarde, administration | Le service continue · **on devient aveugle** |

⚠️ **La correction que cette règle apporte** : une version antérieure de cette structure rangeait la collecte de journaux avec la résolution de noms. C'est faux, et pédagogiquement dangereux : cela enseignerait qu'un service s'arrête quand la collecte tombe, alors qu'il continue — et que le vrai problème est ailleurs. **Tout ce qui n'est pas le contenu utile n'est pas un flux de dépendance.**

### R2 · Principe de la contrainte

> **La taille d'une organisation ne justifie jamais seule un composant. C'est la contrainte qui le justifie.**

Une organisation de douze mille personnes n'a aucun besoin de principe d'une infrastructure d'annuaire complexe. Quand elle en a une, c'est le résultat d'une acquisition, d'une exigence d'isolation ou d'une dette historique — jamais du nombre de salariés.

**Application** : les trois architectures de référence — Atelier Martin, HELIOMED, Novaris — sont toujours présentées avec **la contrainte** qui explique chaque écart, jamais avec la seule taille. La question posée à chaque composant est : *à partir de quelle contrainte devient-il nécessaire ?*

### R3 · Principe de coupe

> **On descend dans le fonctionnement interne d'un mécanisme uniquement jusqu'au niveau nécessaire pour comprendre une décision d'architecture.**

**Le test, appliqué à la résolution de noms** :

| Dans le périmètre | Hors périmètre |
|---|---|
| Client → résolution → adresse → connexion | Le format des messages du protocole |
| Récursif et faisant autorité | Les algorithmes de sélection de serveur |
| Cache, et ce qu'il masque | La configuration d'un logiciel de résolution |
| Redondance, et ce qui tombe sans elle | Les enregistrements exotiques |
| Vue interne et vue externe distinctes | La signature cryptographique des zones, sauf effet architectural |

**La même coupe s'applique partout** : annuaire, certificats, routage, répartition de charge, stockage, orchestration.

### R4 · Principe du coût

> **Avant d'ajouter un composant, être capable d'énoncer la contrainte qu'il résout **et** le coût qu'il introduit.**

C'est la conséquence directe du principe 1. Elle devient le **principe 9** de la doctrine, et elle est appliquée à chaque chapitre de la Partie II sous la forme d'une rubrique obligatoire :

| Composant | Contrainte résolue | **Coût introduit** |
|---|---|---|
| Répartiteur de charge | Continuité malgré la panne d'un membre | Un composant de plus à exploiter, à corriger, à surveiller · un point de rupture nouveau s'il n'est pas redondé |
| Infrastructure de clés interne | Maîtrise des certificats internes | Une hiérarchie à maintenir, des expirations à suivre, une révocation à faire fonctionner |
| Segmentation supplémentaire | Limitation de la propagation | Des flux à ouvrir, à documenter, à maintenir · un dépannage plus difficile |
| Second site | Continuité en cas de sinistre | Un basculement à tester régulièrement, sans quoi il ne fonctionnera pas |
| Orchestration de conteneurs | Densité, reproductibilité, mise à l'échelle | **Un système distribué complet à exploiter** |

⚠️ **Le réflexe que cette règle combat** : construire une architecture en collectionnant des briques. *Ajouter n'est jamais gratuit.*

### R6 · Principe du modèle

Ce cours emploie des **modèles simplifiés** pour rendre les mécanismes lisibles. Un modèle est un outil de raisonnement, pas une description exhaustive du réel.

> **Chaque fois qu'une règle est énoncée sous une forme absolue — toujours, jamais, sans exception — elle est un raccourci pédagogique et doit être signalée comme tel.**

**Les trois formulations à employer** :

| Au lieu de | Écrire |
|---|---|
| « X se passe toujours ainsi » | « Dans le modèle employé ici, X se passe ainsi » |
| « Y ne peut jamais » | « Y suppose généralement, et le contourner exige de … » |
| « Z est le plus … » | « Z est une cause fréquente de … » — sauf si c'est une doctrine assumée |

⚠️ **Pourquoi cette règle est critique dans ce volume précisément** : l'architecture est le domaine où les exceptions sont la norme. Un lecteur qui apprend une fausse loi la transportera dans tous les volumes suivants — et il la défendra en réunion.

**Les formulations fortes sont conservées quand elles expriment une doctrine** — *toute architecture est un compromis*, *ajouter n'est jamais gratuit*. Elles sont supprimées quand elles prétendent établir un classement factuel sans données.

### R7 · Principe d'hypothèse

Cohérente avec les volumes Renseignement et Asset Management de la collection.

> **Lire un schéma produit des hypothèses à confirmer, jamais des identifications certaines.**

**Application aux exercices** : la consigne n'est jamais *« identifiez ce composant »* mais **« proposez le rôle le plus probable, et indiquez ce qu'il faudrait vérifier »**. Un port ouvert, une position, un ensemble de connexions constituent un faisceau — pas une preuve.

### R8 · Principe de preuve

> **Un schéma permet d'identifier une *intention* de redondance. Seul un test permet d'établir une *capacité* de basculement.**

**Ce que deux composants dessinés côte à côte peuvent partager sans que rien ne le montre** : une alimentation · un hôte de virtualisation · un stockage · un site · un segment réseau · une dépendance commune à un service tiers.

**Application** : chaque fois que ce cours conclut à une redondance, il précise **ce qu'il faudrait vérifier** pour que la conclusion tienne.

### R5 · Principe du visuel

Les 115 000 mots annoncés étaient une **estimation, pas une cible**. Ce volume est le plus graphique de la collection.

> **Le schéma peut remplacer le texte. Il n'a pas à l'accompagner.**

Certaines explications de topologie doivent tendre vers 30 % de texte et 70 % de représentation. Si quatre-vingt-cinq mille mots et cent bons schémas enseignent mieux que cent vingt mille mots et soixante schémas, c'est le premier qu'il faut produire.

---
