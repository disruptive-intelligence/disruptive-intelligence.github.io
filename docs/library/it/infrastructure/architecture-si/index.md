---
title: Architecture SI
source: IT/Architecture_SI.md
format: cours
---

*Comprendre, lire et concevoir un système d'information*

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

## Sommaire

- [PARTIE I — Lire un système d'information](01-partie-i-lire-un-systeme-d-information/index.md)
    - [Chapitre 1 — Pourquoi un système d'information ressemble à ça](01-partie-i-lire-un-systeme-d-information/01-chapitre-1-pourquoi-un-systeme-d-information-resse.md)
    - [Chapitre 2 — Le vocabulaire](01-partie-i-lire-un-systeme-d-information/02-chapitre-2-le-vocabulaire.md)
    - [Chapitre 3 — Comment lire un schéma](01-partie-i-lire-un-systeme-d-information/03-chapitre-3-comment-lire-un-schema.md)
    - [Chapitre 4 — La sédimentation](01-partie-i-lire-un-systeme-d-information/04-chapitre-4-la-sedimentation.md)
    - [Chapitre 5 — Les grandes zones](01-partie-i-lire-un-systeme-d-information/05-chapitre-5-les-grandes-zones.md)
    - [Chapitre 6 — Le poste utilisateur](01-partie-i-lire-un-systeme-d-information/06-chapitre-6-le-poste-utilisateur.md)
    - [Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur](01-partie-i-lire-un-systeme-d-information/07-chapitre-7-ce-que-fait-un-architecte-ce-que-fait-u.md)
- [PARTIE II — Les composants d'infrastructure](02-partie-ii-les-composants-d-infrastructure.md)
- [Préambule — Le socle réseau minimal](03-preambule-le-socle-reseau-minimal/index.md)
    - [P.4 Traduction d'adresses](03-preambule-le-socle-reseau-minimal/01-p-4-traduction-d-adresses.md)
    - [Chapitre 8 — Le commutateur](03-preambule-le-socle-reseau-minimal/02-chapitre-8-le-commutateur.md)
    - [Chapitre 9 — Le routeur](03-preambule-le-socle-reseau-minimal/03-chapitre-9-le-routeur.md)
    - [Chapitre 10 — Le pare-feu](03-preambule-le-socle-reseau-minimal/04-chapitre-10-le-pare-feu.md)
    - [Chapitre 11 — Le mandataire sortant](03-preambule-le-socle-reseau-minimal/05-chapitre-11-le-mandataire-sortant.md)
    - [Chapitre 12 — Le mandataire inverse](03-preambule-le-socle-reseau-minimal/06-chapitre-12-le-mandataire-inverse.md)
    - [Chapitre 13 — Le répartiteur de charge](03-preambule-le-socle-reseau-minimal/07-chapitre-13-le-repartiteur-de-charge.md)
    - [Chapitre 14 — La résolution de noms](03-preambule-le-socle-reseau-minimal/08-chapitre-14-la-resolution-de-noms.md)
    - [Chapitre 15 — L'attribution d'adresses](03-preambule-le-socle-reseau-minimal/09-chapitre-15-l-attribution-d-adresses.md)
    - [Chapitre 16 — L'annuaire](03-preambule-le-socle-reseau-minimal/10-chapitre-16-l-annuaire.md)
    - [Chapitre 17 — L'infrastructure de clés](03-preambule-le-socle-reseau-minimal/11-chapitre-17-l-infrastructure-de-cles.md)
- [PARTIE III — Les serveurs et l'exécution](04-partie-iii-les-serveurs-et-l-execution/index.md)
    - [Chapitre 18 — Le serveur web](04-partie-iii-les-serveurs-et-l-execution/01-chapitre-18-le-serveur-web.md)
    - [Chapitre 19 — Le serveur applicatif](04-partie-iii-les-serveurs-et-l-execution/02-chapitre-19-le-serveur-applicatif.md)
    - [Chapitre 20 — La base de données](04-partie-iii-les-serveurs-et-l-execution/03-chapitre-20-la-base-de-donnees.md)
    - [Chapitre 21 — Le serveur de fichiers](04-partie-iii-les-serveurs-et-l-execution/04-chapitre-21-le-serveur-de-fichiers.md)
    - [Chapitre 22 — La messagerie](04-partie-iii-les-serveurs-et-l-execution/05-chapitre-22-la-messagerie.md)
    - [Chapitre 23 — La virtualisation](04-partie-iii-les-serveurs-et-l-execution/06-chapitre-23-la-virtualisation.md)
- [PARTIE IV — Les réseaux et les zones](05-partie-iv-les-reseaux-et-les-zones/index.md)
    - [Chapitre 24 — Le réseau local et la segmentation](05-partie-iv-les-reseaux-et-les-zones/01-chapitre-24-le-reseau-local-et-la-segmentation.md)
    - [Chapitre 25 — La zone démilitarisée](05-partie-iv-les-reseaux-et-les-zones/02-chapitre-25-la-zone-demilitarisee.md)
    - [Chapitre 26 — Le réseau étendu et les sites distants](05-partie-iv-les-reseaux-et-les-zones/03-chapitre-26-le-reseau-etendu-et-les-sites-distants.md)
    - [Chapitre 27 — Le réseau d'administration](05-partie-iv-les-reseaux-et-les-zones/04-chapitre-27-le-reseau-d-administration.md)
    - [Chapitre 28 — Le réseau industriel](05-partie-iv-les-reseaux-et-les-zones/05-chapitre-28-le-reseau-industriel.md)
- [PARTIE V — Les flux](06-partie-v-les-flux/index.md)
    - [Chapitre 29 — Suivre une requête](06-partie-v-les-flux/01-chapitre-29-suivre-une-requete.md)
    - [Chapitre 30 — Suivre une authentification](06-partie-v-les-flux/02-chapitre-30-suivre-une-authentification.md)
    - [Chapitre 31 — Suivre une session](06-partie-v-les-flux/03-chapitre-31-suivre-une-session.md)
    - [Chapitre 32 — Suivre une donnée](06-partie-v-les-flux/04-chapitre-32-suivre-une-donnee.md)
    - [Chapitre 33 — Suivre un secret](06-partie-v-les-flux/05-chapitre-33-suivre-un-secret.md)
    - [Chapitre 34 — Suivre un journal](06-partie-v-les-flux/06-chapitre-34-suivre-un-journal.md)
    - [Chapitre 35 — Du serveur au service](06-partie-v-les-flux/07-chapitre-35-du-serveur-au-service.md)
- [PARTIE VI — Lire une architecture](07-partie-vi-lire-une-architecture/index.md)
    - [Chapitre 36 — La grille de lecture en sept passes](07-partie-vi-lire-une-architecture/01-chapitre-36-la-grille-de-lecture-en-sept-passes.md)
    - [Chapitre 37 — Dix architectures](07-partie-vi-lire-une-architecture/02-chapitre-37-dix-architectures.md)
    - [Chapitre 38 — Les tiers sur un schéma](07-partie-vi-lire-une-architecture/03-chapitre-38-les-tiers-sur-un-schema.md)
- [PARTIE VII — Les architectures modernes](08-partie-vii-les-architectures-modernes/index.md)
    - [Chapitre 39 — Le cloud](08-partie-vii-les-architectures-modernes/01-chapitre-39-le-cloud.md)
    - [Chapitre 40 — L'hybride](08-partie-vii-les-architectures-modernes/02-chapitre-40-l-hybride.md)
    - [Chapitre 41 — Conteneurs et orchestration](08-partie-vii-les-architectures-modernes/03-chapitre-41-conteneurs-et-orchestration.md)
    - [Chapitre 42 — Microservices, fonctions et services en ligne](08-partie-vii-les-architectures-modernes/04-chapitre-42-microservices-fonctions-et-services-en.md)
- [PARTIE VIII — La vue cybersécurité](09-partie-viii-la-vue-cybersecurite/index.md)
    - [Chapitre 43 — Où peut-on agir ?](09-partie-viii-la-vue-cybersecurite/01-chapitre-43-ou-peut-on-agir.md)
    - [Chapitre 44 — Placer les dispositifs](09-partie-viii-la-vue-cybersecurite/02-chapitre-44-placer-les-dispositifs.md)
    - [Chapitre 45 — Ce que l'architecture impose au reste](09-partie-viii-la-vue-cybersecurite/03-chapitre-45-ce-que-l-architecture-impose-au-reste.md)
- [PARTIE IX — Concevoir](10-partie-ix-concevoir/index.md)
    - [Chapitre 46 — Les quatre questions du concepteur](10-partie-ix-concevoir/01-chapitre-46-les-quatre-questions-du-concepteur.md)
    - [Chapitre 47 — Concevoir sous contrainte](10-partie-ix-concevoir/02-chapitre-47-concevoir-sous-contrainte.md)
    - [Chapitre 48 — Quatre conceptions guidées](10-partie-ix-concevoir/03-chapitre-48-quatre-conceptions-guidees.md)
    - [Chapitre 49 — Critiquer une architecture](10-partie-ix-concevoir/04-chapitre-49-critiquer-une-architecture.md)
    - [Chapitre 50 — Ce qu'un schéma ne dira jamais](10-partie-ix-concevoir/05-chapitre-50-ce-qu-un-schema-ne-dira-jamais.md)
- [Cas A — Le schéma qu'on vous donne le premier jour](11-cas-a-le-schema-qu-on-vous-donne-le-premier-jour.md)
- [Cas B — Le service qui tombe](12-cas-b-le-service-qui-tombe.md)
- [Cas C — Concevoir sous contrainte réelle](13-cas-c-concevoir-sous-contrainte-reelle.md)
- [ANNEXES](14-annexes.md)
- [Journal des modifications](15-journal-des-modifications.md)
