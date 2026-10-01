---
title: Chapitre 1 — Pourquoi le CTI existe
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE I — Fondamentaux du renseignement
  - index.md
---

## 1.1 Le problème réel

### Le modèle mental d'abord

Une organisation moyenne reçoit chaque jour, sans rien demander à personne : une dizaine de bulletins d'autorités et de centres de réponse, plusieurs centaines de publications de chercheurs et d'éditeurs sur les réseaux professionnels, les notes de version de ses fournisseurs, les alertes de ses propres outils, et la couverture générale de l'actualité cyber.

Appelons cela le flux. Il est gratuit, abondant, souvent de bonne qualité.

**Et il ne produit aucune décision.**

C'est le point de départ de ce cours, et il est contre-intuitif : le problème du renseignement n'est pas la rareté de l'information. C'est son abondance. Une organisation qui ne fait pas de CTI n'est pas une organisation mal informée — c'est une organisation **noyée**, qui reçoit chaque semaine largement de quoi occuper une personne à temps plein, et qui n'en tire rien.

**Le CTI est la discipline qui transforme ce flux en décisions.** Pas en tableaux de bord, pas en rapports, pas en indicateurs à intégrer : en décisions que quelqu'un prend et assume.

### La définition de travail

Retenez celle-ci, elle sera utilisée dans tout le cours :

> **Cyber Threat Intelligence** : activité consistant à collecter, analyser et diffuser des informations sur les menaces, **dans le but de réduire l'incertitude d'un décideur identifié**, sur une question qu'il a posée, dans un délai qui lui est utile.

Quatre éléments de cette définition font tout le travail.

**« réduire l'incertitude ».** Pas la supprimer. Un analyste qui produit des certitudes produit autre chose que du renseignement — souvent des ennuis. Nous y reviendrons au chapitre 9.

**« d'un décideur identifié ».** Nommé, joignable, à qui on peut demander si le produit lui a servi. Un renseignement sans destinataire nommé n'est pas du renseignement.

**« sur une question qu'il a posée ».** C'est le principe 2 de la doctrine, et la première cause d'échec du domaine. On ne collecte pas d'abord pour chercher l'usage ensuite.

**« dans un délai qui lui est utile ».** Une analyse parfaite livrée après la décision vaut zéro. Le renseignement est une discipline sous contrainte de temps, et cette contrainte est souvent ce qui distingue un bon analyste d'un excellent.

## 1.2 La boucle analytique

Un seul schéma décrit le métier. Chaque partie de ce cours travaille un segment de cette boucle, et chaque chapitre indique lequel.

🖼 **SCHÉMA — La boucle analytique.** *Diagramme circulaire à six nœuds. Le nœud ① QUESTION est visuellement dominant : taille supérieure, couleur distincte. Flèche de retour « nouvelle incertitude ».*

```
                    ┌───────────────────────────────────┐
                    │                                   │
                    ▼                                   │
      ╔═══════════════════╗                             │
      ║  ①  QUESTION      ║──► ② COLLECTE ──► ③ ANALYSE │
      ║  de quoi ai-je    ║    où chercher,    hypothèses,
      ║  besoin de savoir ║    jusqu'où        biais,
      ║  pour décider ?   ║                    méthode   │
      ╚═══════════════════╝                        │     │
                                                   ▼     │
      ⑥ RETOUR ◄────── ⑤ DÉCISION ◄────── ④ JUGEMENT    │
      qu'ai-je appris   agir, préparer,    conclusion    │
      sur ma propre     surveiller,        + confiance   │
      analyse ?         ignorer, différer  exprimée      │
             │                                           │
             └──────► nouvelle incertitude ──────────────┘
```


| Segment | Question | Parties du cours |
|---|---|---|
| ① **Question** | De quoi ai-je besoin de savoir pour décider ? | I, III |
| ② **Collecte** | Où chercher, jusqu'où, et à quel prix ? | V |
| ③ **Analyse** | Quelles hypothèses, et laquelle résiste ? | II |
| ④ **Jugement** | Que puis-je conclure, avec quelle confiance ? | II, VI |
| ⑤ **Décision** | Qu'est-ce que cela change ? | VII |
| ⑥ **Retour** | Avais-je raison, et pourquoi ? | VIII |

**Trois observations qui structurent tout le cours.**

**La boucle démarre en ① et jamais en ②.** Une cellule qui commence par collecter produit du volume. Elle accumule des flux, des abonnements, des plateformes — et au bout de dix-huit mois, personne ne peut dire quelle décision a été modifiée. C'est la première cause d'échec, et elle est presque toujours invisible de l'intérieur, parce que l'activité est intense.

**L'étape ⑥ n'existe presque nulle part.** Combien d'organisations relisent leurs estimations de l'an dernier pour vérifier si elles étaient justes ? Sans ce retour, un analyste reproduit ses erreurs indéfiniment, avec la même assurance. C'est l'objet du chapitre 35, et c'est ce qui sépare une fonction qui progresse d'une fonction qui vieillit.

**La sortie de la boucle n'est pas une certitude.** C'est une incertitude **mieux cernée** : vous savez désormais ce que vous ignorez, et pourquoi. C'est exactement ce qui distingue le renseignement de la divination — et c'est aussi ce qui le rend inconfortable à vendre en interne.

## 1.3 Ce que le renseignement permet de décider, concrètement

Le CTI paraît abstrait tant qu'on ne liste pas les décisions qu'il modifie. Les voici, avec leur destinataire.

| Décision | Qui la prend | Ce que le CTI y apporte |
|---|---|---|
| Corriger cette vulnérabilité avant celle-là | Exploitation, MCS | L'exploitation observée, le ciblage sectoriel |
| Écrire cette règle de détection plutôt qu'une autre | Détection | Les modes opératoires réellement employés |
| Bloquer ou ne pas bloquer cette infrastructure | Détection, réseau | La durée de vie et le partage de l'infrastructure |
| Déclencher ou non une recherche de compromission | Réponse à incident | Les indicateurs et le mode opératoire d'une campagne |
| Investir dans cette capacité de sécurité | Direction | Les tendances de menace sur trois ans |
| Renforcer la surveillance sur ce périmètre | RSSI | Le ciblage constaté de votre secteur |
| Prévenir ou non un client | Produit, PSIRT | Ce qui vise vos produits déployés |
| Accepter ou refuser un fournisseur | Achats, sécurité | L'exposition connue de ce fournisseur |
| Ne rien faire | Tous | **La décision la plus fréquente, et la moins tracée** |

⚠️ **La dernière ligne est celle qui surprend.** Dans une fonction CTI mature, l'écrasante majorité des informations traitées aboutissent à *ne rien faire*. Ce n'est pas un échec : c'est le produit normal du tri. Ce qui est un échec, c'est de ne pas tracer cette décision — parce qu'alors, six mois plus tard, personne ne sait si l'information avait été vue et écartée, ou simplement manquée. La différence est considérable en cas d'incident.

🎯 **ET MAINTENANT ?**
*Un bulletin d'un centre de réponse national signale une vulnérabilité critique activement exploitée sur un produit que vous n'utilisez pas. Que faites-vous ?*
**Réponse** : rien — et vous l'écrivez. Une ligne dans votre registre : identifiant du bulletin, date, décision *sans objet — produit non présent au périmètre*, vérification faite dans l'inventaire. Trente secondes. Ce qui coûte cher n'est pas la décision de ne rien faire, c'est de ne pas pouvoir dire, plus tard, qu'on l'avait prise.

## 1.4 Pourquoi suivre l'actualité n'est pas du renseignement

C'est la confusion la plus répandue, y compris chez des professionnels expérimentés. Elle mérite d'être disséquée, parce qu'elle explique pourquoi tant de « cellules CTI » ne produisent rien d'utile.

| | **Veille** | **Renseignement** |
|---|---|---|
| Point de départ | Ce que les sources publient | **Une question posée par un décideur** |
| Critère de sélection | Ce qui est intéressant | Ce qui est **pertinent pour la question** |
| Traitement | Résumer, relayer | Analyser, évaluer, calibrer |
| Sortie | Un flux, une lettre d'information | **Un jugement avec un niveau de confiance** |
| Destinataire | Diffus, non identifié | **Nommé** |
| Mesure de réussite | Volume, régularité | **Décisions modifiées** |
| Ce qui se passe si personne ne lit | Rien de visible | La fonction n'a servi à rien |

**La veille est utile.** Elle n'est simplement pas du renseignement, et l'appeler ainsi crée deux problèmes : on croit avoir une capacité qu'on n'a pas, et on mesure la mauvaise chose — le nombre de bulletins produits plutôt que le nombre de décisions changées.

⚠️ **PIÈGE — le test qui tranche**
Prenez le dernier produit sorti par votre fonction. Posez trois questions : *qui l'a demandé ? quelle décision devait-il éclairer ? cette décision a-t-elle été prise différemment grâce à lui ?* Si les trois réponses sont floues, vous faites de la veille. Ce n'est pas grave — mais il faut le savoir, et le dire.

## 1.5 Les six causes d'échec d'une cellule CTI

Comme au MCS, les échecs sont remarquablement répétitifs. Aucun n'est technique.

**1. Collecter sans besoin.** On souscrit des flux, on installe une plateforme, on ingère des millions d'indicateurs. Puis on cherche à qui cela pourrait servir. L'activité est intense et le résultat nul. → Chapitre 14.

**2. Produire sans destinataire.** Le rapport est bon. Personne ne l'a demandé, personne ne le lit, et l'analyste conclut que « les gens ne s'intéressent pas à la sécurité ». Le problème n'est pas leur intérêt : c'est qu'on a répondu à une question qu'ils ne se posaient pas. → Chapitres 14 et 26.

**3. Ne pas calibrer.** Le produit affirme sans nuance, ou nuance sans rien affirmer. Dans les deux cas, le destinataire ne peut pas décider : il ne sait pas ce qui est établi et ce qui est supposé. → Chapitre 9.

**4. Confondre les niveaux.** On envoie des indicateurs techniques à une direction générale, et des tendances géopolitiques à un analyste qui doit écrire une règle ce soir. Chacun conclut que le CTI ne sert à rien, et chacun a raison de son point de vue. → Chapitre 3.

**5. Dépendre d'une source unique.** Un flux, un fournisseur, un compte suivi. Le jour où cette source se trompe, se tarit ou change de politique, la fonction s'arrête. Et entre-temps, personne n'a vu que trois « sources différentes » citaient en réalité la même. → Chapitre 10.

**6. Ne pas mesurer l'impact.** Faute de savoir prouver ce que la fonction apporte, on mesure ce qu'on sait compter : nombre de rapports, volume d'indicateurs, nombre de flux. Ces chiffres augmentent. La fonction est supprimée au premier arbitrage budgétaire. → Chapitre 35.

✅ **BONNE PRATIQUE — l'ordre d'attaque (P0)**
Si vous créez une fonction CTI, traitez ces causes **dans cet ordre**. Souscrire un flux avant d'avoir un destinataire nommé et une question écrite est l'erreur de séquencement la plus coûteuse du domaine : vous financerez pendant deux ans une capacité que personne ne vous demandera de justifier — jusqu'au jour où on vous le demandera. Le chapitre 40 détaille la feuille de route.

## 1.6 Ce que le CTI ne fait pas

Un cours honnête énonce les limites de son sujet. Le CTI **ne fait pas** :

- **Prédire une attaque.** Il n'annonce ni la date, ni la cible, ni le vecteur. Il indique ce qui est plausible, contre quoi, et avec quelle probabilité approximative. C'est beaucoup moins spectaculaire et beaucoup plus utile.
- **Remplacer la détection.** Savoir qu'une campagne existe ne la détecte pas sur votre réseau. Le CTI alimente la détection ; il ne s'y substitue pas.
- **Remplacer la sécurité de base.** Un renseignement excellent sur un parc non maintenu ne produit rien. On ne compense pas un défaut d'hygiène par de la connaissance.
- **Résoudre l'attribution.** Et, comme le montrera le chapitre 13, vous en avez rarement besoin.
- **Donner des certitudes.** Jamais. C'est le principe 1 de la doctrine, et c'est le plus difficile à faire accepter en interne.

⚠️ **PIÈGE — les quatre illusions les plus coûteuses**

| Illusion | Ce qui cloche |
|---|---|
| « Nous avons du CTI, nous sommes informés » | Informé de quoi, pour quelle décision, avec quelle couverture de vos besoins réels ? |
| « Ce flux contient deux millions d'indicateurs » | Le volume mesure ce que le fournisseur collecte, pas ce qui vous concerne. Voir §22.4 |
| « Trois sources confirment » | Trois sources qui citent la même source unique n'en font qu'une. Voir §10.4 |
| « Le rapport dit que ce groupe nous cible » | Sur quelle base ? Avec quelle confiance ? Et surtout : qu'est-ce que ça change à ce que vous devez faire ? |

## 1.7 Le périmètre de ce cours

Il faut le dire explicitement, parce que le mot « renseignement » recouvre des métiers très différents.

**Ce cours traite du CTI défensif en organisation** : une entreprise, une administration ou une association qui cherche à mieux se protéger et à mieux décider.

**Il ne traite pas** :

| Hors périmètre | Pourquoi |
|---|---|
| Le renseignement étatique | Moyens, cadre juridique et finalités sans commune mesure |
| Les équipes d'attribution spécialisées | Métier distinct, exigeant des sources et des durées inaccessibles à une organisation ordinaire |
| La recherche offensive et l'analyse de maliciels | Disciplines voisines et complémentaires, avec leurs propres cours |
| L'investigation numérique | Le CTI l'alimente et s'en nourrit, mais c'est un autre métier |
| Le renseignement d'origine humaine | Hors du champ légal et déontologique d'une organisation privée |

**Ce que cela change concrètement** : quand ce cours dit qu'une pratique est déconseillée ou impossible, cela vaut **pour une organisation ordinaire**. Une agence gouvernementale ou une équipe spécialisée peut faire autrement, avec d'autres moyens et un autre cadre. Le chapitre 13, sur l'attribution, est celui où cette distinction compte le plus.

## 1.8 ⏱ État de l'art du domaine au 2 août 2026

*Bloc périssable. À réviser en priorité lors de la prochaine revue.*

**Ce qui a changé récemment**

- **Les référentiels de modes opératoires évoluent structurellement, et pas seulement par ajout.** La principale base publique de tactiques et techniques a scindé en avril 2026 l'une de ses tactiques historiques en deux tactiques distinctes, dont l'une conserve l'identifiant d'origine. Conséquence directe : toute cartographie de couverture, toute règle et tout rapport y faisant référence doivent être remappés. 📎 [S-01]
- **Les modes opératoires assistés par des modèles de langage sont entrés dans les référentiels publics**, avec des entrées documentant à la fois des campagnes largement automatisées et un maliciel interrogeant un modèle en opération. 📎 [S-02]
- **Le cadre juridique du partage d'indicateurs est instable dans plusieurs juridictions.** Un régime de protection majeur a expiré, été prolongé deux fois, et arrive à échéance sous quelques semaines à la date de rédaction. 📎 [S-03]

**Ce qui émerge**

- La production de renseignement par des outils automatisés augmente le volume disponible sans augmenter proportionnellement sa qualité — ce qui déplace l'effort de la collecte vers **l'évaluation de source** (chapitre 10).
- Les exigences réglementaires de maîtrise de la chaîne d'approvisionnement font entrer le renseignement sur les fournisseurs dans le périmètre d'organisations qui n'en faisaient pas.

**Ce qui reste stable, et le restera**

Le besoin précède la collecte. La confiance s'exprime. Les faits sont observés et les jugements argumentés. Un renseignement sans destinataire ne sert à rien. Ces principes étaient vrais avant l'informatique, ils le seront après les référentiels cités dans ce cours.

**Ce qui devient obsolète**

- Le pilotage d'une fonction CTI par le volume d'indicateurs ingérés.
- Le catalogue d'acteurs appris par cœur, périmé en dix-huit mois.
- L'idée qu'une plateforme technique constitue à elle seule une capacité de renseignement.

## 1.9 Comment lire ce cours

Quarante chapitres, trois cas de synthèse, neuf mini-labs, treize annexes. Le document n'est pas conçu pour être lu d'un trait.

- **Partie I (ch. 1-5)** : à lire dans l'ordre, sans exception. Elle installe le langage.
- **Partie II (ch. 6-13)** : le cœur. À lire dans l'ordre également.
- **Parties III à VII** : consultables par thème.
- **Partie VIII** : à traiter en dernier, en situation.
- **Annexes** : outils de travail, pas compléments.

Une matrice de parcours par profil figure en tête du document.

## 1.10 La phrase fondatrice

Tout ce chapitre tient dans une phrase, et si vous n'en gardez qu'une, gardez celle-ci :

> ### Le CTI n'est pas là pour prédire l'avenir. Il est là pour prendre de meilleures décisions malgré l'incertitude.

Elle explique pourquoi ce cours consacre huit chapitres au raisonnement avant d'aborder les sources, et un seul chapitre aux outils, en trente-sixième position. Elle explique pourquoi on parle de niveaux de confiance plutôt que de vérité. Et elle explique pourquoi la question la plus utile qu'un analyste puisse poser à un décideur n'est pas *« que voulez-vous savoir ? »* mais **« que feriez-vous différemment si vous le saviez ? »**.

🔴 **FIL ROUGE — mars 2029 : trois comptes suivis et un flux inutilisé**

*Le fil rouge de ce cours suit une organisation fictive, le groupe HELIOMED. Tout y est inventé — l'entreprise, les personnes, les événements — mais rien n'y est irréaliste. Si vous avez suivi le cours de maintien en condition de sécurité, vous la connaissez déjà ; sinon, elle est décrite au fur et à mesure et vous n'avez rien à savoir d'avance.*

HELIOMED est une entreprise de taille intermédiaire française : 1 380 salariés, 240 M€ de chiffre d'affaires. Elle fabrique des dispositifs médicaux connectés — des pompes à perfusion PX-40 — et édite une plateforme de télésuivi, HelioLink, complétée d'une passerelle hospitalière, HelioBox, et d'une application mobile de bien-être, HelioMove. Trois sites : Lyon (siège et direction des systèmes d'information), Saint-Étienne (usine), Nantes (recherche et développement).

Depuis trois ans, Claire Nadeau, responsable de la sécurité des systèmes d'information, a construit un dispositif de maintien en condition de sécurité mature : inventaire fiable, correctifs pilotés, preuve tenue, équipe de sécurité produit en service. Le dernier audit client s'est bien passé.

**Le 14 mars 2029**, le directeur des systèmes d'information d'un centre hospitalier universitaire — le troisième client d'HELIOMED en volume — envoie un courriel de deux paragraphes. Le second contient une phrase nouvelle :

> *« Notre politique de sécurité fournisseurs, révisée en janvier, demande désormais que nos partenaires critiques démontrent une capacité de suivi des menaces visant notre secteur d'activité. Pourriez-vous nous décrire votre dispositif ? »*

Claire réunit ce qui existe. L'inventaire est vite fait :

| Élément | État réel |
|---|---|
| Comptes suivis sur un réseau social professionnel | 3, par Malik Ferhaoui, à titre personnel |
| Abonnement aux bulletins d'un centre de réponse national | Actif — reçu sur une liste de diffusion technique, **jamais exploité systématiquement** |
| Flux d'indicateurs fourni avec la solution de protection des postes | Actif, ingéré automatiquement, **personne ne l'a jamais examiné** |
| Adhésion à un dispositif de partage sectoriel | Aucune |
| Personne en charge | Aucune |
| Produit écrit sur les menaces au cours des douze derniers mois | **Zéro** |

**Ce qui frappe Claire n'est pas l'absence de moyens.** C'est que trois des cinq lignes existent déjà — les bulletins arrivent, le flux est ingéré, quelqu'un lit des publications. L'information est là. Elle ne produit simplement **aucune décision**, et personne ne pourrait dire ce qu'elle a changé au cours de l'année écoulée.

**La décision prise.** Claire ne souscrit rien. Elle rédige une note d'une page pour la direction générale, qui ne parle ni d'outils ni de flux, et pose une seule question :

> *De quoi devons-nous être informés pour prendre de meilleures décisions ? Et qui, chez nous, prendrait ces décisions ?*

**Livrable de l'épisode.** Une note d'une page, et une demande : un poste à temps plein pendant douze mois, pour répondre à cette question avant d'acheter quoi que ce soit.

→ La suite en 🔴 §2.6, quand il faudra expliquer à la direction pourquoi les trois comptes suivis ne constituent pas une réponse.

## Synthèse mentale du chapitre 1

Le problème du renseignement n'est pas la rareté de l'information mais son abondance : une organisation qui ne fait pas de CTI n'est pas mal informée, elle est noyée. Le CTI transforme ce flux en décisions, pour un décideur nommé, sur une question qu'il a posée, dans un délai qui lui est utile. La boucle analytique commence par la question et jamais par la collecte ; son étape de retour — avais-je raison ? — n'existe presque nulle part, et c'est ce qui empêche les fonctions CTI de progresser. La veille n'est pas du renseignement : trois questions suffisent à trancher — qui l'a demandé, quelle décision, décidée différemment ? Six causes expliquent la plupart des échecs, et aucune n'est technique. Enfin, la décision la plus fréquente est de ne rien faire : ce n'est pas un échec, c'est le produit normal du tri — l'échec est de ne pas la tracer.

**Trois questions de vérification**

1. Votre organisation reçoit chaque jour des dizaines de bulletins de qualité et se déclare bien informée. Quelles trois questions posez-vous pour savoir si elle fait du renseignement ?
2. Pourquoi une cellule CTI qui commence par souscrire des flux échoue-t-elle presque toujours, alors que son activité est intense et visible ?
3. Un bulletin signale une vulnérabilité exploitée sur un produit que vous n'utilisez pas. Que faites-vous, et pourquoi cette réponse compte-t-elle malgré son apparente inutilité ?

→ **Chapitre 2 — Qu'est-ce qu'un renseignement** : les cinq objets que presque tout le monde confond, suivis sur un même événement de bout en bout.

---
