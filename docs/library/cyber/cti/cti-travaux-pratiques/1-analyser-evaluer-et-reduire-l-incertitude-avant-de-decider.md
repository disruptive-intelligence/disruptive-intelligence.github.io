---
title: Analyser, évaluer et réduire l'incertitude avant de décider
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 1
chapters: 8
---

**Tranches T1 à T8 — Cours intégral, chapitres 1 à 40**
*Version 1.0 · données vérifiées au 2 août 2026*

---


## Si vous venez du cours MCS

Ce cours se lit seul. Mais si vous avez suivi le précédent, ce tableau vous situe immédiatement.

| | **MCS** | **CTI** |
|---|---|---|
| Objectif | Réduire l'**exposition** | Réduire l'**incertitude** |
| Modèle mental | La boucle MCS | La boucle analytique |
| Décision centrale | Que corriger, quand | **Que croire, et avec quelle confiance** |
| Objet de travail | Des actifs | Des informations |
| Livrable principal | Un plan de remédiation prouvé | Un jugement analytique calibré |
| Mesure de réussite | Exposition résiduelle, prouvée | Décisions modifiées, confiance justifiée |
| Le piège symétrique | Corriger sans connaître son périmètre | Collecter sans savoir ce qu'on cherche |
| Ce qui ne s'automatise pas | La décision d'accepter un risque | Le jugement |

**Ce que vous retrouverez** : la primauté du besoin sur l'outil · la méfiance envers les chiffres non qualifiés · l'obligation de dire ce qu'on ne sait pas · la preuve comme partie intégrante du travail.

**Ce qui change, et c'est fondamental** :

> **En MCS, le réel est vérifiable.** Un serveur porte une version ou n'en porte pas. On peut aller regarder.
> **En CTI, le réel est inaccessible.** On ne vérifie jamais une hypothèse, on la rend plus ou moins probable.

C'est de cette phrase que découlent toutes les particularités du métier : pourquoi on exprime des niveaux de confiance, pourquoi on calibre son langage, pourquoi on argumente au lieu de démontrer, et pourquoi un bon analyste dit régulièrement « je ne sais pas » sans que ce soit un aveu d'incompétence.

---


## PARTIE I — Fondamentaux du renseignement

Cette partie ne vous apprendra ni à collecter, ni à analyser, ni à produire. Elle vous apprend **un langage** — celui sans lequel les trente-cinq chapitres suivants seraient inutilisables.

Cinq chapitres, et un objectif unique : qu'à la fin, vous puissiez distinguer sans hésiter une donnée d'un renseignement, un fait d'une estimation, une observation d'une conclusion. Ces distinctions paraissent évidentes. Elles sont confondues dans la majorité des produits de renseignement que vous lirez, y compris commerciaux et y compris chers.

---

### Chapitre 1 — Pourquoi le CTI existe

#### 1.1 Le problème réel

##### Le modèle mental d'abord

Une organisation moyenne reçoit chaque jour, sans rien demander à personne : une dizaine de bulletins d'autorités et de centres de réponse, plusieurs centaines de publications de chercheurs et d'éditeurs sur les réseaux professionnels, les notes de version de ses fournisseurs, les alertes de ses propres outils, et la couverture générale de l'actualité cyber.

Appelons cela le flux. Il est gratuit, abondant, souvent de bonne qualité.

**Et il ne produit aucune décision.**

C'est le point de départ de ce cours, et il est contre-intuitif : le problème du renseignement n'est pas la rareté de l'information. C'est son abondance. Une organisation qui ne fait pas de CTI n'est pas une organisation mal informée — c'est une organisation **noyée**, qui reçoit chaque semaine largement de quoi occuper une personne à temps plein, et qui n'en tire rien.

**Le CTI est la discipline qui transforme ce flux en décisions.** Pas en tableaux de bord, pas en rapports, pas en indicateurs à intégrer : en décisions que quelqu'un prend et assume.

##### La définition de travail

Retenez celle-ci, elle sera utilisée dans tout le cours :

> **Cyber Threat Intelligence** : activité consistant à collecter, analyser et diffuser des informations sur les menaces, **dans le but de réduire l'incertitude d'un décideur identifié**, sur une question qu'il a posée, dans un délai qui lui est utile.

Quatre éléments de cette définition font tout le travail.

**« réduire l'incertitude ».** Pas la supprimer. Un analyste qui produit des certitudes produit autre chose que du renseignement — souvent des ennuis. Nous y reviendrons au chapitre 9.

**« d'un décideur identifié ».** Nommé, joignable, à qui on peut demander si le produit lui a servi. Un renseignement sans destinataire nommé n'est pas du renseignement.

**« sur une question qu'il a posée ».** C'est le principe 2 de la doctrine, et la première cause d'échec du domaine. On ne collecte pas d'abord pour chercher l'usage ensuite.

**« dans un délai qui lui est utile ».** Une analyse parfaite livrée après la décision vaut zéro. Le renseignement est une discipline sous contrainte de temps, et cette contrainte est souvent ce qui distingue un bon analyste d'un excellent.

#### 1.2 La boucle analytique

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

#### 1.3 Ce que le renseignement permet de décider, concrètement

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

#### 1.4 Pourquoi suivre l'actualité n'est pas du renseignement

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

#### 1.5 Les six causes d'échec d'une cellule CTI

Comme au MCS, les échecs sont remarquablement répétitifs. Aucun n'est technique.

**1. Collecter sans besoin.** On souscrit des flux, on installe une plateforme, on ingère des millions d'indicateurs. Puis on cherche à qui cela pourrait servir. L'activité est intense et le résultat nul. → Chapitre 14.

**2. Produire sans destinataire.** Le rapport est bon. Personne ne l'a demandé, personne ne le lit, et l'analyste conclut que « les gens ne s'intéressent pas à la sécurité ». Le problème n'est pas leur intérêt : c'est qu'on a répondu à une question qu'ils ne se posaient pas. → Chapitres 14 et 26.

**3. Ne pas calibrer.** Le produit affirme sans nuance, ou nuance sans rien affirmer. Dans les deux cas, le destinataire ne peut pas décider : il ne sait pas ce qui est établi et ce qui est supposé. → Chapitre 9.

**4. Confondre les niveaux.** On envoie des indicateurs techniques à une direction générale, et des tendances géopolitiques à un analyste qui doit écrire une règle ce soir. Chacun conclut que le CTI ne sert à rien, et chacun a raison de son point de vue. → Chapitre 3.

**5. Dépendre d'une source unique.** Un flux, un fournisseur, un compte suivi. Le jour où cette source se trompe, se tarit ou change de politique, la fonction s'arrête. Et entre-temps, personne n'a vu que trois « sources différentes » citaient en réalité la même. → Chapitre 10.

**6. Ne pas mesurer l'impact.** Faute de savoir prouver ce que la fonction apporte, on mesure ce qu'on sait compter : nombre de rapports, volume d'indicateurs, nombre de flux. Ces chiffres augmentent. La fonction est supprimée au premier arbitrage budgétaire. → Chapitre 35.

✅ **BONNE PRATIQUE — l'ordre d'attaque (P0)**
Si vous créez une fonction CTI, traitez ces causes **dans cet ordre**. Souscrire un flux avant d'avoir un destinataire nommé et une question écrite est l'erreur de séquencement la plus coûteuse du domaine : vous financerez pendant deux ans une capacité que personne ne vous demandera de justifier — jusqu'au jour où on vous le demandera. Le chapitre 40 détaille la feuille de route.

#### 1.6 Ce que le CTI ne fait pas

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

#### 1.7 Le périmètre de ce cours

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

#### 1.8 ⏱ État de l'art du domaine au 2 août 2026

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

#### 1.9 Comment lire ce cours

Quarante chapitres, trois cas de synthèse, neuf mini-labs, treize annexes. Le document n'est pas conçu pour être lu d'un trait.

- **Partie I (ch. 1-5)** : à lire dans l'ordre, sans exception. Elle installe le langage.
- **Partie II (ch. 6-13)** : le cœur. À lire dans l'ordre également.
- **Parties III à VII** : consultables par thème.
- **Partie VIII** : à traiter en dernier, en situation.
- **Annexes** : outils de travail, pas compléments.

Une matrice de parcours par profil figure en tête du document.

#### 1.10 La phrase fondatrice

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

#### Synthèse mentale du chapitre 1

Le problème du renseignement n'est pas la rareté de l'information mais son abondance : une organisation qui ne fait pas de CTI n'est pas mal informée, elle est noyée. Le CTI transforme ce flux en décisions, pour un décideur nommé, sur une question qu'il a posée, dans un délai qui lui est utile. La boucle analytique commence par la question et jamais par la collecte ; son étape de retour — avais-je raison ? — n'existe presque nulle part, et c'est ce qui empêche les fonctions CTI de progresser. La veille n'est pas du renseignement : trois questions suffisent à trancher — qui l'a demandé, quelle décision, décidée différemment ? Six causes expliquent la plupart des échecs, et aucune n'est technique. Enfin, la décision la plus fréquente est de ne rien faire : ce n'est pas un échec, c'est le produit normal du tri — l'échec est de ne pas la tracer.

**Trois questions de vérification**

1. Votre organisation reçoit chaque jour des dizaines de bulletins de qualité et se déclare bien informée. Quelles trois questions posez-vous pour savoir si elle fait du renseignement ?
2. Pourquoi une cellule CTI qui commence par souscrire des flux échoue-t-elle presque toujours, alors que son activité est intense et visible ?
3. Un bulletin signale une vulnérabilité exploitée sur un produit que vous n'utilisez pas. Que faites-vous, et pourquoi cette réponse compte-t-elle malgré son apparente inutilité ?

→ **Chapitre 2 — Qu'est-ce qu'un renseignement** : les cinq objets que presque tout le monde confond, suivis sur un même événement de bout en bout.

---

### Chapitre 2 — Qu'est-ce qu'un renseignement

> **La pierre angulaire du cours.** Les cinq objets décrits ici sont réutilisés dans les trente-huit chapitres suivants. Si un seul chapitre devait être lu deux fois, c'est celui-ci.

#### 2.1 Cinq objets, un seul événement

La plupart des cours donnent des définitions séparées. Nous allons faire l'inverse : suivre **un même fait** depuis son apparition brute jusqu'au jugement qu'il permet de formuler. C'est en le voyant se transformer qu'on comprend ce que chaque étape ajoute.

**L'événement.** Le 3 novembre, à 03 h 12, le pare-feu d'HELIOMED enregistre une connexion entrante en provenance de l'adresse `198.51.100.47` vers le port 443 de la passerelle d'accès distant.

##### Étape 1 — La donnée

```
2029-11-03 03:12:47  198.51.100.47 -> gw-vpn.heliomed.fr:443  ACCEPT
```

**Ce que c'est** : un fait brut, sans contexte, sans interprétation. Il est vrai ou faux — ici, il est vrai, le journal l'atteste.

**Ce qu'on peut en faire** : rien. Une organisation de cette taille produit plusieurs millions de lignes de ce type par jour. Prise isolément, cette ligne ne signifie rien du tout.

⚠️ **Le piège de la donnée** : elle est **vérifiable**, donc rassurante. Beaucoup d'organisations accumulent des données et pensent progresser parce que ce qu'elles collectent est indiscutable. La solidité de la donnée ne compense jamais son absence de sens.

##### Étape 2 — L'information

> *L'adresse `198.51.100.47` a établi douze connexions vers la passerelle d'accès distant entre 02 h 50 et 03 h 40, toutes avec des tentatives d'authentification échouées sur des comptes qui n'existent pas dans l'annuaire.*

**Ce qu'on a ajouté** : du **contexte**. Une agrégation temporelle, une mise en relation avec l'annuaire, la caractérisation du comportement.

**Ce que ça permet** : formuler une première question. Ce n'est pas encore une décision, c'est une hypothèse naissante — quelqu'un teste des identifiants.

**Ce que ça coûte** : les premiers choix subjectifs apparaissent. Pourquoi une fenêtre de cinquante minutes et pas de deux heures ? Pourquoi rapprocher de l'annuaire et pas des journaux applicatifs ? Chaque choix d'agrégation est une décision d'analyste, et elle oriente déjà la suite.

##### Étape 3 — La connaissance

> *Cette adresse appartient à un bloc hébergé chez un fournisseur d'infrastructure à la demande. Elle apparaît dans deux publications de chercheurs des trois dernières semaines, décrivant une activité de test d'identifiants contre des passerelles d'accès distant du même constructeur que celle d'HELIOMED. Le mode opératoire décrit correspond au comportement observé.*

**Ce qu'on a ajouté** : l'**intégration à un ensemble**. L'information isolée rejoint un corpus existant. On sort du périmètre de l'organisation.

**Ce que ça permet** : sortir du cas particulier. Ce n'est plus un incident local, c'est une instance d'un phénomène plus large.

⚠️ **Le piège de la connaissance** : c'est ici qu'apparaît la circularité. Les *deux* publications sont-elles indépendantes, ou la seconde cite-t-elle la première ? Cette vérification prend cinq minutes et n'est presque jamais faite. Nous y reviendrons longuement au §10.4.

##### Étape 4 — Le renseignement

> *Une activité de test d'identifiants visant les passerelles d'accès distant de notre constructeur est en cours depuis au moins trois semaines. Notre passerelle en fait l'objet. Nous exposons ce service par nécessité fonctionnelle ; 210 collaborateurs l'utilisent. L'authentification multifacteur y est active depuis 2027, ce qui rend un test d'identifiants seul insuffisant pour obtenir un accès.*

**Ce qu'on a ajouté** : la **pertinence pour une décision**. Le corpus est rapporté à **votre** contexte : votre exposition, vos mesures existantes, vos utilisateurs.

**Ce que ça permet** : décider. Et remarquez ce que la dernière phrase change : sans elle, la conclusion naturelle serait d'agir en urgence. Avec elle, la situation devient sérieuse mais maîtrisée.

**C'est ici que la plupart des organisations n'arrivent jamais.** Elles produisent des étapes 2 et 3 en abondance — des informations et de la connaissance générale — et les diffusent en croyant faire du renseignement. Le destinataire reçoit alors une description du monde, sans savoir ce qu'elle implique pour lui.

##### Étape 5 — Le jugement analytique

> *Nous estimons **probable** que cette activité relève d'une campagne opportuniste visant l'ensemble des passerelles de ce constructeur exposées sur Internet, et non d'un ciblage spécifique d'HELIOMED — **confiance moyenne**, fondée sur deux sources dont l'indépendance reste à confirmer, sur l'absence de sélection apparente de nos comptes réels, et sur l'ampleur du phénomène décrit publiquement.*
>
> *Nous estimons **peu probable** qu'un accès ait été obtenu, l'authentification multifacteur étant active — **confiance élevée**, cette mesure étant vérifiée et journalisée.*
>
> *Cette évaluation serait remise en cause si : des comptes réellement existants étaient ciblés · une authentification aboutissait · l'activité persistait au-delà de la campagne décrite publiquement.*

**Ce qu'on a ajouté** : une **conclusion assumée, calibrée, et réfutable**.

Trois éléments distinguent un jugement analytique de tout ce qui précède :

| Élément | Rôle |
|---|---|
| Un **verbe d'estimation** | *Nous estimons* — l'analyste s'engage, sans prétendre à la certitude |
| Un **niveau de confiance explicite**, distinct de la gravité | Le lecteur sait sur quoi il s'appuie |
| **Ce qui l'invaliderait** | La section que presque personne n'écrit, et qui transforme une opinion en analyse |

##### Le tableau récapitulatif

| Objet | Définition | Sur notre événement | Vérifiable ? |
|---|---|---|---|
| **Donnée** | Fait brut, sans contexte | Une ligne de journal | Oui |
| **Information** | Donnée mise en contexte | Douze tentatives échouées en cinquante minutes | Oui |
| **Connaissance** | Information intégrée à un ensemble | L'adresse figure dans deux publications décrivant un mode opératoire | Partiellement |
| **Renseignement** | Connaissance répondant à un besoin de décision | Notre passerelle est visée ; voici notre exposition réelle | Non — il contient une appréciation |
| **Jugement analytique** | Évaluation argumentée, calibrée, réfutable | *Probable, campagne opportuniste, confiance moyenne* | **Non, par nature** |

#### 2.2 Ce que chaque étape ajoute, et ce qu'elle coûte

La colonne « vérifiable » du tableau précédent contient l'enseignement central du chapitre.

> **À mesure qu'on progresse vers le renseignement, on gagne en utilité et on perd en vérifiabilité.**

C'est un échange, et il faut l'assumer. Une donnée est incontestable et inutile. Un jugement analytique est utile et contestable. Il n'existe pas d'objet qui soit les deux à la fois — et chercher à en produire un est l'origine de deux dérives symétriques :

| Dérive | Manifestation | Conséquence |
|---|---|---|
| **Refuser de juger** | Le produit décrit longuement sans jamais conclure | Le destinataire doit faire l'analyse lui-même — donc la fonction ne sert à rien |
| **Juger sans le dire** | Le produit affirme sur le ton du fait ce qui est une appréciation | Le destinataire décide sur une base plus solide qu'elle ne l'est |

**La seconde est de loin la plus dangereuse**, et de loin la plus fréquente dans les publications commerciales. Elle est traitée en profondeur au chapitre 11.

🎯 **ET MAINTENANT ?**
*Vous recevez un rapport de fournisseur qui affirme : « le groupe X cible activement le secteur de la santé en Europe ». Que faites-vous de cette phrase ?*
**Réponse** : vous la traduisez avant de l'utiliser. « Cible activement » est-il un fait observé — des victimes identifiées, des intrusions constatées — ou un jugement — un faisceau d'indices interprétés ? Le rapport le dit-il ? S'il ne le dit pas, la phrase n'est pas exploitable en l'état : vous ne pouvez pas savoir si vous devez agir ou surveiller. La demande à faire au fournisseur tient en une ligne : *sur quelles observations cette affirmation repose-t-elle, et avec quel niveau de confiance ?*

#### 2.3 Où la plupart des organisations s'arrêtent

Reprenons les cinq étapes, avec ce qu'on observe en pratique.

| Étape | Qui la produit couramment | Fréquence observée |
|---|---|---|
| Donnée | Les outils, automatiquement | Massive |
| Information | Les outils, avec un peu de configuration | Fréquente |
| Connaissance | Les fournisseurs et les publications publiques | Fréquente, et souvent achetée |
| **Renseignement** | **Vous, et personne d'autre** | **Rare** |
| **Jugement analytique** | **Vous, et personne d'autre** | **Très rare** |

**Les deux dernières lignes sont le cœur du métier**, et elles ont une propriété commune que vous devez avoir en tête tout au long du cours : **personne ne peut les produire à votre place**.

Un fournisseur peut vous vendre de la connaissance — d'excellente qualité, parfois. Il ne peut pas vous vendre du renseignement, parce qu'il ne connaît ni votre exposition, ni vos mesures existantes, ni ce que votre direction est en train de décider. Cette asymétrie explique une observation qui surprend souvent : **une organisation qui dépense beaucoup en flux et peu en analyse achète de la connaissance et croit acheter du renseignement.**

⚠️ **PIÈGE — le rapport qui décrit le monde**
Symptôme : votre produit mensuel pourrait être envoyé tel quel à n'importe quelle autre organisation du secteur. S'il ne contient rien qui vous soit propre — votre exposition, vos actifs, vos décisions en cours — ce n'est pas du renseignement, c'est de la connaissance redistribuée. Elle a une valeur, mais pas celle-là.

#### 2.4 Ce qui rend un renseignement exploitable

Quatre conditions. Elles sont cumulatives.

| Condition | Question de contrôle | Si elle manque |
|---|---|---|
| **Il répond à une question posée** | Qui l'a demandé ? | Le produit ne sera pas lu |
| **Il arrive à temps** | La décision est-elle encore ouverte ? | Le produit est un constat historique |
| **Il est calibré** | Que sait-on, que suppose-t-on ? | Le destinataire ne peut pas doser sa réaction |
| **Il indique ce qu'il implique** | Qu'est-ce qui change ? | Le destinataire doit refaire le travail |

🧪 **EN PRATIQUE — le test des quatre questions**

Avant de diffuser un produit, quel qu'il soit, passez ces quatre questions. Le test prend deux minutes et évite l'essentiel des produits inutiles.

```
1. Qui l'a demandé, et pour décider quoi ?
2. Cette décision est-elle encore ouverte au moment où j'envoie ?
3. Ai-je distingué ce que j'observe de ce que j'estime ?
4. Le destinataire saura-t-il quoi faire différemment ?
```

Un produit qui échoue à la question 1 ne doit pas être envoyé — il doit d'abord trouver son destinataire. Un produit qui échoue à la question 4 doit être réécrit.

#### 2.5 Renseignement et vérité

Une clarification nécessaire, parce qu'elle heurte le sens commun.

> **Un renseignement peut être excellent et faux. Un renseignement peut être exact et sans valeur.**

**Excellent et faux** : une évaluation fondée sur les meilleures sources disponibles, calibrée honnêtement, avec une confiance correctement exprimée, peut se révéler erronée. Ce n'est pas un échec analytique si le raisonnement était sain et l'incertitude déclarée. C'est le fonctionnement normal d'une discipline qui travaille sur de l'information incomplète.

**Exact et sans valeur** : une affirmation parfaitement vraie sur une menace qui ne vous concerne pas, ou qui arrive après la décision, ou que vous ne pouvez pas exploiter, ne vaut rien — quelle que soit sa justesse.

**Ce qu'on juge chez un analyste** n'est donc pas son taux d'exactitude brut. C'est :

| Critère | Question |
|---|---|
| La qualité du raisonnement | Les hypothèses ont-elles été envisagées ? Les sources évaluées ? |
| L'honnêteté du calibrage | La confiance annoncée correspondait-elle à la solidité réelle ? |
| L'utilité | La décision a-t-elle été meilleure ? |
| **La capacité à réviser** | Quand l'analyste a eu tort, l'a-t-il vu, dit et compris ? |

⚠️ Le quatrième critère est celui qui distingue un analyste qui progresse d'un analyste qui se contente d'avoir eu raison souvent. C'est l'objet du §35.6.

#### 2.6 🔴 FIL ROUGE — avril 2029 : « nous suivons déjà l'actualité »

La note de Claire Nadeau (§1.10) est examinée au comité de direction du 4 avril. La demande — un poste à temps plein pendant douze mois — rencontre une objection prévisible, formulée par le directeur financier :

> *« Nous suivons déjà l'actualité de la sécurité. Malik lit les publications, nous recevons les bulletins, nous avons un flux d'indicateurs dans notre outil de protection. Qu'est-ce qu'une personne de plus apporterait ? »*

L'objection est de bonne foi, et elle est exactement la confusion du §1.4. Claire ne répond pas en théorie. Elle prend un exemple réel, survenu six semaines plus tôt.

**Ce qui existait** — étape 3, connaissance :

> *Un bulletin d'un centre de réponse national, reçu le 18 février, signalait une vulnérabilité critique activement exploitée sur une famille de passerelles d'accès distant.*

Ce bulletin a été reçu. Il a été lu par deux personnes. Il n'a produit aucune action.

**Ce qui aurait été du renseignement** — étape 4 :

> *Notre passerelle appartient à la famille concernée. Elle est publiée sur Internet par nécessité fonctionnelle et utilisée par 210 collaborateurs. La version installée est affectée. Un correctif est disponible depuis le 17 février.*

**Ce qui aurait été un jugement analytique** — étape 5 :

> *Nous estimons élevée la probabilité que cette passerelle soit sondée dans les jours qui viennent, l'exploitation étant automatisée et notre service étant découvrable publiquement — confiance élevée, l'exploitation étant confirmée par la source d'origine et notre exposition étant vérifiée.*

**Le fait qui emporte la décision.** Claire vérifie l'inventaire : le correctif a été appliqué le 3 mars, treize jours après la publication du bulletin, dans le cadre de la campagne mensuelle ordinaire de maintien en condition de sécurité. Pas parce que quelqu'un avait rapproché le bulletin de l'inventaire — **personne ne l'avait fait** — mais parce que le processus de correctifs a fini par y arriver.

> *« Nous avons eu de la chance pendant treize jours, dit-elle. Ce n'est pas une capacité, c'est un délai. »*

**La décision prise.** Le poste est validé pour douze mois, avec une condition posée par Karim Lebrun : à l'issue de la période, la fonction devra démontrer **quelles décisions ont été prises différemment**. Claire accepte — c'est exactement la mesure qu'elle aurait proposée, et elle le dit.

**Livrable de l'épisode.** Une fiche de poste, et un engagement écrit sur le critère d'évaluation à douze mois. Ce critère structurera tout le fil rouge, jusqu'au chapitre 35.

**Le recrutement.** Nour Belkacem prend ses fonctions le 2 mai 2029. Analyste, cinq ans d'expérience dans un centre opérationnel de sécurité, jamais occupé un poste de CTI. Sa première semaine est décrite au chapitre 5.

→ La suite en 🔴 §3.6, quand Nour découvrira qu'elle produit pour trois publics qui n'attendent pas la même chose.

#### 2.7 ✅ Livrable — Grille de qualification d'un produit reçu

À appliquer à tout produit de renseignement que vous recevez : bulletin, rapport de fournisseur, publication de chercheur, note d'un partenaire.

| Question | Réponse | Ce qu'elle détermine |
|---|---|---|
| À quelle étape se situe ce produit ? | ☐ donnée ☐ information ☐ connaissance ☐ renseignement ☐ jugement | Le travail qu'il vous reste à faire |
| Contient-il quelque chose qui m'est propre ? | ☐ oui ☐ non | Si non : c'est de la connaissance, pas du renseignement |
| Les faits sont-ils distingués des appréciations ? | ☐ oui ☐ non ☐ partiellement | La confiance que je peux lui accorder |
| Un niveau de confiance est-il exprimé ? | ☐ oui ☐ non | S'il faut le demander ou l'estimer moi-même |
| Le produit dit-il ce qui l'invaliderait ? | ☐ oui ☐ non | La maturité de la source |
| Quelle décision cela devrait-il éclairer chez nous ? | *(à écrire)* | Si aucune : archiver, et le tracer |
| Que dois-je ajouter pour en faire du renseignement ? | *(à écrire)* | **Votre valeur ajoutée** |

**La dernière ligne est celle qui compte.** Elle vous rappelle qu'un produit reçu, aussi bon soit-il, s'arrête à l'étape 3. Le passage à l'étape 4 est votre travail, et personne d'autre ne peut le faire.

#### Synthèse mentale du chapitre 2

Cinq objets se succèdent sur un même fait : la donnée est brute et vérifiable, l'information la met en contexte, la connaissance l'intègre à un ensemble extérieur, le renseignement la rapporte à votre situation et à une décision, le jugement analytique conclut avec une confiance exprimée et dit ce qui l'invaliderait. À mesure qu'on progresse, on gagne en utilité et on perd en vérifiabilité — c'est un échange qu'il faut assumer, et deux dérives symétriques en découlent : refuser de juger, ou juger sans le dire, la seconde étant la plus dangereuse. Les deux dernières étapes sont le cœur du métier, et personne ne peut les produire à votre place : un fournisseur vend de la connaissance, jamais du renseignement, parce qu'il ignore votre exposition et vos décisions en cours. Enfin, un renseignement peut être excellent et faux, ou exact et sans valeur : ce qu'on juge chez un analyste n'est pas son taux d'exactitude mais la qualité de son raisonnement, l'honnêteté de son calibrage et sa capacité à réviser.

**Trois questions de vérification**

1. Un fournisseur vous livre un rapport de trente pages sur une campagne. À quelle étape des cinq se situe-t-il, et que devez-vous y ajouter ?
2. Pourquoi une organisation qui dépense beaucoup en flux et peu en analyse achète-t-elle de la connaissance en croyant acheter du renseignement ?
3. Une évaluation s'est révélée fausse six mois plus tard. Comment jugez-vous le travail de l'analyste, et sur quels critères ?

→ **Chapitre 3 — Les trois niveaux** : pourquoi un indicateur technique n'intéresse pas une direction générale, et pourquoi une tendance géopolitique n'aide pas à écrire une règle de détection.

---

### Chapitre 3 — Les trois niveaux

#### 3.1 Le schéma structurant

Le renseignement se produit à trois niveaux. Cette distinction n'est pas académique : elle détermine **le destinataire, la question, le format, la durée de vie, la méthode et l'incertitude tolérable**. La confondre est la deuxième cause d'inutilité du domaine, après l'absence de besoin exprimé.

🖼 **SCHÉMA — Les trois niveaux du CTI.** *Trois bandeaux horizontaux superposés, du stratégique en haut au tactique en bas, avec sur l'axe vertical l'horizon temporel et sur l'axe horizontal le degré d'incertitude tolérable. Faire apparaître que les deux varient en sens inverse.*

| | **Stratégique** | **Opérationnel** | **Tactique** |
|---|---|---|---|
| **Qui décide** | Direction générale, comité de direction | RSSI, responsable MCS, responsable produit | Détection, réponse à incident |
| **Question type** | Où investir ? Quels risques portons-nous à trois ans ? | Que prioriser ce trimestre ? Contre quoi nous préparer ? | Que bloquer ? Que chercher dans nos journaux ? |
| **Horizon** | 1 à 3 ans | 3 à 12 mois | 3 à 30 jours |
| **Livrable** | Évaluation, note d'orientation | Priorités, fiches de modes opératoires | Indicateurs, règles, actions |
| **Durée de vie du produit** | Années | Mois | **Jours** |
| **Conséquence d'une erreur** | Un budget mal orienté pendant des années | Un effort de remédiation mal placé | Une alerte manquée, ou du bruit |
| **Incertitude tolérable** | **Élevée** | Moyenne | **Faible** |
| **Volume produit** | 2 à 6 par an | 1 à 4 par mois | Continu |

#### 3.2 Pourquoi l'incertitude tolérable varie en sens inverse de l'horizon

C'est la ligne la plus contre-intuitive du tableau, et celle qui explique le plus de malentendus. Prenons-la de face.

**Au niveau stratégique, une incertitude élevée est acceptable — et même normale.** Quand une direction décide d'investir sur trois ans dans une capacité de détection plutôt que dans la segmentation, elle ne dispose d'aucune certitude sur les menaces de 2032. Elle décide sur des tendances. Un analyste qui refuserait de se prononcer faute de preuves serait inutile à ce niveau : ce qu'on lui demande, c'est une **orientation argumentée**, assumée comme incertaine.

**Au niveau tactique, une incertitude élevée est disqualifiante.** Une règle de détection fondée sur une hypothèse fragile produit du bruit, épuise l'équipe et finit désactivée. Un indicateur bloqué à tort coupe un service légitime. Ici, on n'agit que sur ce qui est solide — quitte à ne pas agir.

**La conséquence pratique** est un renversement complet de la posture selon le destinataire :

| Niveau | Ce qu'on reproche à un analyste |
|---|---|
| Stratégique | De ne pas se prononcer |
| Tactique | De se prononcer trop vite |

**Un analyste qui n'a pas intégré cette asymétrie sera jugé mauvais aux deux niveaux** : trop prudent pour la direction, trop affirmatif pour la détection. C'est l'une des raisons pour lesquelles un même produit ne peut jamais servir les trois publics.

#### 3.3 Le niveau tactique

**Ce qu'il produit** : des indicateurs techniques, des règles de détection, des actions de blocage, des requêtes de recherche rétrospective.

**Sa caractéristique dominante** : la **péremption rapide**. Une infrastructure adverse change ; une empreinte de fichier ne vaut que pour ce fichier ; un nom de domaine est abandonné. Un indicateur conservé indéfiniment devient un faux positif en puissance, et le chapitre 30 traite son cycle de vie complet.

**L'erreur classique à ce niveau** : confondre volume et valeur. Un flux de deux millions d'indicateurs n'est pas cent fois meilleur qu'un flux de vingt mille — il est surtout cent fois plus coûteux à trier. La question n'est pas *combien* mais *quelle proportion me concerne, et à quel taux d'erreur*.

⚠️ **PIÈGE — l'indicateur sans contexte**
Un indicateur livré seul — une adresse, une empreinte — ne dit ni ce qu'il représente, ni depuis quand il est valide, ni quelle confiance lui accorder, ni ce qu'il faut faire si on le voit. Il est presque inexploitable. Un indicateur utile porte au minimum : sa source, sa date de première et de dernière observation, ce à quoi il est associé, et l'action attendue.

#### 3.4 Le niveau opérationnel

**Ce qu'il produit** : des fiches de modes opératoires, des évaluations de campagnes, des priorités de remédiation, des scénarios de préparation.

**C'est le niveau le plus utile et le moins produit.** Cette phrase mérite d'être expliquée, parce qu'elle décrit une anomalie durable du domaine.

| Niveau | Pourquoi il est produit ou non |
|---|---|
| Tactique | Facile à produire, automatisable, vendable au volume — **surproduit** |
| Stratégique | Visible, valorisant, demandé par les directions — **produit, souvent mal** |
| **Opérationnel** | Exige de connaître à la fois la menace **et** votre organisation — **sous-produit** |

Le niveau opérationnel est celui qui demande le plus de travail spécifique et qui s'achète le moins bien. Un fournisseur peut vous vendre des indicateurs et des tendances ; il peut difficilement vous dire quelles trois techniques d'attaque devraient orienter vos six prochains mois, parce que cela suppose de connaître votre architecture, vos angles morts et vos projets en cours.

**C'est donc là que se situe l'essentiel de la valeur ajoutée d'une fonction interne** — et c'est ce qui justifie qu'elle existe.

#### 3.5 Le niveau stratégique

**Ce qu'il produit** : des évaluations de tendance, des notes d'orientation, des éléments de décision budgétaire.

**Sa difficulté propre** : il est le plus demandé et le plus mal fait. Deux dérives symétriques :

| Dérive | Manifestation | Ce que le destinataire en fait |
|---|---|---|
| **La revue de presse déguisée** | Une compilation des grandes tendances du secteur, sans lien avec l'organisation | Rien. Il l'avait déjà lue ailleurs |
| **La projection non assumée** | Des affirmations sur trois ans formulées comme des faits | Il décide sur une base plus solide qu'elle ne l'est |

**Ce qu'un bon produit stratégique contient** : peu de faits, beaucoup de raisonnement, une orientation claire, et une déclaration explicite de ce qui pourrait la faire changer. Il tient en deux pages. S'il en fait quinze, il ne sera pas lu par son destinataire — qui n'est pas un spécialiste et n'a pas le temps.

🎯 **ET MAINTENANT ?**
*Votre direction générale vous demande une note sur « la menace cyber pour notre secteur en 2030 ». Par quoi commencez-vous ?*
**Réponse** : par une question de retour, avant d'écrire une ligne. *Quelle décision cette note doit-elle éclairer ?* Selon la réponse — arbitrer un budget, choisir entre deux investissements, répondre à un actionnaire, préparer un conseil d'administration — le produit sera radicalement différent. Écrire la note sans poser cette question, c'est produire quinze pages qui finiront dans une pièce jointe non ouverte. Ce réflexe est développé au chapitre 14.

#### 3.6 ⚠️ La confusion des niveaux

C'est la deuxième cause d'inutilité du domaine. Quatre situations, toutes observées en pratique.

| # | Situation | Ce que le destinataire en conclut |
|---|---|---|
| 1 | Une liste d'indicateurs techniques envoyée à un comité de direction | « Le CTI, c'est incompréhensible et ça ne me concerne pas » |
| 2 | Une tendance géopolitique envoyée à un analyste qui doit écrire une règle ce soir | « Le CTI, c'est du vent » |
| 3 | Une évaluation stratégique demandée en urgence pour une décision de blocage | Le produit arrive trop tard et ne répond pas à la question |
| 4 | Un rapport unique de vingt pages envoyé à cinq destinataires différents | Aucun ne le lit entièrement, chacun cherche sa partie et ne la trouve pas |

**Le point commun des quatre** : le producteur a raisonné en termes de **contenu** — *voici ce que je sais* — au lieu de raisonner en termes de **destinataire** — *voici ce dont vous avez besoin pour décider*.

✅ **BONNE PRATIQUE (P0) — la question préalable à toute diffusion**
Avant d'envoyer quoi que ce soit : *à quel niveau se situe mon destinataire, et quelle décision doit-il prendre ?* Si vous avez deux destinataires à deux niveaux différents, vous avez **deux produits à écrire**, pas un produit à envoyer deux fois. Le chapitre 26 en fait un exercice complet.

#### 3.7 Quel niveau pour quelle organisation

Toutes les organisations n'ont pas besoin des trois niveaux, et prétendre le contraire conduit à des fonctions CTI sous-dimensionnées qui font mal les trois.

| Contexte | Niveau prioritaire | Pourquoi |
|---|---|---|
| Petite organisation, pas de centre opérationnel | **Opérationnel**, exclusivement | Le tactique suppose une capacité de détection à alimenter ; le stratégique suppose des arbitrages d'investissement qui n'existent pas à cette échelle |
| Organisation avec détection interne | Tactique + opérationnel | Le tactique alimente la détection, l'opérationnel oriente les priorités |
| Organisation régulée ou exposée | Les trois | La direction porte des obligations et arbitre des investissements |
| Éditeur ou fabricant | Opérationnel + un tactique spécifique sur ses propres produits | Ce qui vise ses produits est un sujet à part entière (chapitre 33) |

📌 **LIMITES — l'illusion de complétude**
Une fonction d'une personne qui prétend couvrir les trois niveaux produira trois choses médiocres. Le chapitre 39 traite explicitement ce cas : **choisir un niveau, l'assumer, et déclarer les deux autres non couverts** vaut infiniment mieux qu'une couverture superficielle. C'est la même logique que les périmètres déclarés non couverts du cours MCS.

#### 3.8 🔴 FIL ROUGE — mai 2029 : trois publics, un seul rapport

Nour Belkacem a pris ses fonctions le 2 mai. Le 22 mai, elle produit son premier livrable : une note de onze pages sur une campagne de rançongiciel visant des établissements de santé européens depuis février.

Le travail est bon. Les sources sont vérifiées, le mode opératoire est décrit précisément, les indicateurs sont listés, une section évalue les implications pour HELIOMED.

Elle l'envoie à sept personnes. Voici ce qui se passe.

| Destinataire | Ce qu'il en fait | Pourquoi |
|---|---|---|
| Claire Nadeau (RSSI) | La lit intégralement | C'est son métier, et elle a commandé le travail |
| Malik Ferhaoui (exploitation, MCS) | Cherche la liste des vulnérabilités exploitées, la trouve page 8 | Il voulait une réponse à *que corriger en premier* |
| Yann Prigent (produit) | Cherche si HelioBox est concerné, ne trouve pas de réponse claire | La question n'était pas traitée |
| Sonia Weber (DSI) | Lit le résumé, s'arrête page 2 | Onze pages, agenda plein |
| Le référent détection | Extrait les indicateurs, se demande depuis quand ils sont valides | L'information n'y était pas |
| Dr Hélène Fabre (affaires réglementaires) | Ne l'ouvre pas | Ne comprend pas pourquoi elle l'a reçue |
| Karim Lebrun (DAF) | Ne l'ouvre pas | Idem |

**Le bilan, deux semaines plus tard** : une personne sur sept a lu le document en entier, deux en ont tiré quelque chose au prix d'une recherche, quatre l'ont ignoré. Aucune décision n'a été prise.

**Ce que Nour croit d'abord.** Que le document était trop long. C'est vrai, mais accessoire.

**Ce que Claire lui fait voir.** Le document mélangeait trois niveaux et six destinataires. Il contenait du tactique — les indicateurs, sans leur date de validité —, de l'opérationnel — les vulnérabilités à prioriser, enterrées page 8 —, et du stratégique — la tendance sectorielle, en introduction. Chaque lecteur devait traverser le contenu des autres pour trouver le sien.

> *« Ce n'est pas un rapport trop long, lui dit Claire. C'est trois rapports collés. »*

**La décision prise.** Le même travail est redécoupé en trois produits, sans une seule recherche supplémentaire :

| Produit | Destinataire | Format | Contenu |
|---|---|---|---|
| **Note d'orientation** | Direction, DSI | 1 page | La tendance sectorielle, ce qu'elle implique pour nos priorités, ce qui la ferait changer |
| **Fiche opérationnelle** | MCS, produit, RSSI | 2 pages | Le mode opératoire, les techniques employées, les trois vulnérabilités à traiter en priorité, la question HelioBox traitée explicitement |
| **Jeu d'indicateurs** | Détection | Tableau | Les indicateurs, **avec date de première et dernière observation, source, et action attendue** |

Les trois sont diffusés le 5 juin. Malik programme une campagne de correctifs dans la semaine. Yann Prigent obtient sa réponse — HelioBox n'est pas concerné, et il peut le dire à ses clients. La détection intègre onze indicateurs sur les quarante fournis, après avoir écarté ceux dont la dernière observation datait de plus de six mois.

**Ce que Nour retient**, et qu'elle notera dans son carnet : *le même travail, découpé selon les destinataires, a produit trois décisions au lieu de zéro.*

**Livrable de l'épisode.** Trois modèles de produits, un par niveau, qui deviendront le standard d'HELIOMED — ils figurent en annexe D.

→ La suite en 🔴 §4.7, quand Nour relira sa première note et y trouvera quatre affirmations qu'elle ne peut pas justifier.

#### Synthèse mentale du chapitre 3

Le renseignement se produit à trois niveaux qui déterminent le destinataire, le format, la durée de vie et la méthode. L'incertitude tolérable varie en sens inverse de l'horizon : au stratégique, refuser de se prononcer faute de preuves rend inutile ; au tactique, se prononcer trop vite produit du bruit et des blocages injustifiés — un analyste qui n'a pas intégré cette asymétrie sera jugé mauvais aux deux niveaux. Le tactique se périme en jours et souffre de la confusion entre volume et valeur. L'opérationnel est le plus utile et le moins produit, parce qu'il exige de connaître à la fois la menace et votre organisation : c'est là que se situe la valeur ajoutée d'une fonction interne. Le stratégique est le plus demandé et le plus mal fait, entre revue de presse déguisée et projection non assumée. Enfin, deux destinataires à deux niveaux différents, ce sont deux produits à écrire — jamais un produit à envoyer deux fois.

**Trois questions de vérification**

1. Pourquoi une incertitude élevée est-elle acceptable dans une note stratégique et disqualifiante dans une règle de détection ?
2. Vous êtes seul, à temps partiel, dans une organisation sans capacité de détection. Quel niveau couvrez-vous, et que faites-vous des deux autres ?
3. Un rapport de vingt pages est envoyé à cinq destinataires et personne ne réagit. Quel est le diagnostic le plus probable, et qu'est-ce qui n'est probablement pas le problème ?

→ **Chapitre 4 — Les axiomes de l'analyste** : six énoncés qui paraissent évidents et qui détruisent, une fois posés, l'essentiel des mauvais raisonnements.

---

### Chapitre 4 — Les axiomes de l'analyste

> Six énoncés, avant toute théorie de l'analyse. Ils paraissent évidents. Ils sont pourtant violés en permanence, y compris dans des publications professionnelles — et chacun d'eux, une fois posé, élimine une famille entière de mauvais raisonnements.
>
> Ils sont réutilisés dans les trente-six chapitres suivants. Le chapitre 8, sur les techniques d'analyse structurée, n'est au fond qu'un ensemble de méthodes pour les respecter quand l'intuition tire dans l'autre sens.

#### 4.1 Observer n'est pas conclure

**L'énoncé.** Ce que vous constatez et ce que vous en déduisez sont deux affirmations distinctes. Elles ont des statuts différents, des degrés de certitude différents, et elles doivent être écrites séparément.

**Le mécanisme de la violation.** Le cerveau produit l'interprétation *en même temps* que l'observation, pas après. Vous ne voyez pas « douze tentatives d'authentification échouées » puis concluez « quelqu'un teste des identifiants » : vous percevez immédiatement un test d'identifiants. L'interprétation arrive déjà collée au fait, et il faut un effort délibéré pour les décoller.

🧪 **EN PRATIQUE — le test de séparation**

Prenez n'importe quelle phrase de votre dernier produit et demandez : *si je remplace le verbe par « nous observons », la phrase reste-t-elle vraie ?*

| Phrase | Test | Verdict |
|---|---|---|
| « L'attaquant a tenté de compromettre le compte administrateur » | *Nous observons que l'attaquant a tenté…* | ❌ **Faux.** Vous observez des échecs d'authentification sur ce compte. Que ce soit un attaquant, qu'il ait « tenté de compromettre », et qu'il y ait une intention : ce sont trois déductions |
| « Douze tentatives d'authentification ont échoué sur le compte administrateur entre 02 h 50 et 03 h 40 » | *Nous observons que…* | ✅ **Vrai.** C'est une observation |
| « Le groupe X cible le secteur de la santé » | *Nous observons que…* | ❌ **Faux.** Vous observez des victimes du secteur ; « cible » suppose une intention |

**Ce que ça change concrètement** : votre produit devient utilisable par quelqu'un qui n'a pas votre contexte. Il peut distinguer ce sur quoi il peut s'appuyer sans réserve de ce qu'il doit interroger.

⚠️ **PIÈGE — le verbe d'intention**
*Cibler, chercher à, tenter de, viser, s'intéresser à* — tous ces verbes attribuent une intention à un acteur dont vous n'observez que des effets. Ils ne sont pas interdits : ils appartiennent au registre du jugement, pas du fait. Écrivez-les dans la section évaluation, jamais dans la section observation.

#### 4.2 Corrélation n'est pas causalité — et en renseignement, la coïncidence est fréquente

**L'énoncé** est connu. Ce qui l'est moins, c'est **pourquoi il mord particulièrement fort ici**.

Le CTI travaille sur des données massives, faiblement structurées, provenant de sources hétérogènes. Dans ce contexte, les coïncidences sont **abondantes** :

| Coïncidence typique | Interprétation tentante | Explication alternative banale |
|---|---|---|
| Deux organisations du même secteur touchées la même semaine | Campagne ciblée sur le secteur | Elles utilisent le même produit vulnérable, exploité massivement |
| Une adresse apparaît dans deux incidents distincts | Même acteur | Hébergement mutualisé, adresse réattribuée, service légitime détourné |
| Une intrusion suit de peu une publication de vulnérabilité | Exploitation de cette vulnérabilité | Le vecteur réel est ailleurs ; la proximité temporelle est fortuite |
| Un pic d'activité coïncide avec un événement géopolitique | Réaction à l'événement | Le pic correspond à une campagne opportuniste sans rapport |

**Le test à appliquer** : *quelle autre explication produirait exactement la même observation ?* Si vous n'en trouvez aucune, ce n'est pas que l'explication est certaine — c'est que vous n'avez pas assez cherché. Le chapitre 8 en fait une méthode.

🎯 **ET MAINTENANT ?**
*Trois de vos concurrents ont été victimes d'un rançongiciel en six semaines. Un rapport en conclut que le secteur est ciblé. Que faites-vous de cette conclusion ?*
**Réponse** : vous cherchez ce qui les relie **autrement que par le secteur**. Même prestataire informatique ? Même progiciel métier ? Même solution d'accès distant ? Trois victimes d'un même secteur peuvent être trois victimes d'un même fournisseur — et la mesure à prendre n'est alors pas du tout la même. C'est une question à poser avant d'accepter la conclusion, pas après.

#### 4.3 Absence de preuve n'est pas preuve d'absence — et l'inverse est tout aussi faux

**Le premier volet** est classique : ne rien avoir trouvé ne signifie pas qu'il n'y a rien.

**Le second volet l'est beaucoup moins**, et il est tout aussi important : **l'absence n'est pas non plus une preuve de présence**. La formule provocatrice *« l'absence d'information est une information »* circule beaucoup et autorise, mal comprise, exactement le raisonnement qu'on veut éviter :

```
Je n'ai rien trouvé
        ↓
Donc l'adversaire est discret
        ↓
Donc il est sophistiqué
        ↓
Donc c'est grave
```

Chaque flèche est une déduction non fondée. Ce raisonnement est plus fréquent qu'on ne croit, particulièrement après un incident où l'on n'a pas trouvé grand-chose.

**La formulation robuste** est celle-ci :

> **L'absence appelle une question sur votre capacité d'observation, pas une conclusion sur le réel.**

Trois questions, dans cet ordre :

| # | Question | Ce qu'elle vérifie |
|---|---|---|
| 1 | **Ai-je cherché au bon endroit ?** | Le périmètre de la recherche |
| 2 | **Avais-je les bons capteurs ?** | La capacité technique à voir ce type d'activité |
| 3 | **Ai-je cherché assez longtemps ?** | La profondeur d'historique disponible |

Si les trois réponses sont *oui*, l'absence devient un élément d'appréciation — faible, mais réel. Si l'une est *non*, l'absence ne dit **rien du tout**, et le produit doit le dire explicitement.

⚠️ Ceux qui viennent du cours MCS reconnaîtront la formulation du §21.3 : *l'absence de preuve de compromission n'est pas la preuve de l'absence de compromission, a fortiori quand la journalisation est insuffisante*. C'est le même axiome, appliqué à un autre métier.

#### 4.4 Un renseignement est périssable

**L'énoncé.** Toute affirmation de renseignement a une date de péremption. Elle n'est pas toujours connue, mais elle existe toujours.

**Les rythmes**, repris du chapitre 3 :

| Objet | Durée de validité typique | Ce qui la fait expirer |
|---|---|---|
| Une adresse d'infrastructure | Jours à semaines | L'adversaire change d'infrastructure |
| Une empreinte de fichier | Une variante | Une recompilation suffit |
| Un mode opératoire | Mois à années | L'adversaire adapte, ou une défense se généralise |
| Une évaluation de motivation | Années | Un changement de contexte géopolitique ou économique |
| Un rapport lu sans vérifier sa date | **Immédiate** | — |

**La conséquence pratique la plus importante** : un produit de renseignement doit **porter sa date et son horizon de validité**. Pas seulement la date de rédaction — la date jusqu'à laquelle l'analyste estime que la conclusion tient.

🧪 **EN PRATIQUE — la mention à ajouter systématiquement**

```
Évaluation au 14 novembre 2029.
Réexamen prévu : février 2030, ou plus tôt si [événement déclencheur].
```

Cette mention coûte quinze secondes. Elle évite qu'un rapport soit cité deux ans plus tard comme s'il décrivait le présent — situation dont vous serez témoin plus souvent que vous ne le croyez.

#### 4.5 Une analyse est une hypothèse argumentée, pas une description

**L'énoncé.** Décrire n'est pas analyser. Un document qui expose des faits sans conclure n'est pas une analyse prudente : c'est une analyse absente.

**La confusion** est entretenue par une bonne intention. L'analyste veut être rigoureux, il évite d'affirmer, il expose les éléments et laisse le lecteur juger. Le résultat est que **le destinataire doit faire l'analyse lui-même** — c'est-à-dire faire le travail pour lequel la fonction existe.

| Ce que ce n'est pas | Ce que c'est |
|---|---|
| Un résumé de ce qui a été publié | Une position argumentée sur ce qui est le plus probable |
| Une liste d'éléments | Un raisonnement qui les relie |
| « Plusieurs hypothèses sont possibles » | « Nous retenons l'hypothèse B, pour ces trois raisons, avec cette confiance » |
| Une description neutre | **Un engagement révisable** |

**Le mot important est *révisable*.** Une analyse s'engage — et prévoit ce qui la ferait changer d'avis. C'est ce qui la distingue à la fois de la description, qui n'engage rien, et de l'opinion, qui ne prévoit pas de révision. Le chapitre 11 en fait la méthode complète.

#### 4.6 Une source n'est pas un fait

**L'énoncé.** Que quelqu'un l'ait écrit ne le rend pas vrai. Que trois personnes l'aient écrit ne le rend pas trois fois plus vrai.

C'est l'axiome le plus violé du domaine, parce que la violation est **invisible** : elle se produit au moment où l'on recopie une affirmation en changeant simplement de mode grammatical.

| Ce que la source dit | Ce qui est recopié | La transformation opérée |
|---|---|---|
| *« Nous évaluons avec une confiance modérée que… »* | « Le groupe X fait… » | Un jugement calibré devient un fait |
| *« Selon des chercheurs, il est possible que… »* | « Il est établi que… » | Une hypothèse devient une certitude |
| *« Un incident a été rapporté »* | « Une campagne vise… » | Un cas devient une campagne |
| *« Cette activité présente des similarités avec… »* | « Cette activité est attribuée à… » | Une similarité devient une attribution |

**Le mécanisme** est la perte de la chaîne de provenance à chaque reprise. Au bout de trois reprises successives, une hypothèse prudente est devenue un fait établi, et personne ne peut plus remonter à l'affirmation d'origine. C'est ce qui produit la **circularité** du §10.4, et c'est le cas de synthèse B en entier.

✅ **BONNE PRATIQUE (P0)** — Quand vous reprenez une affirmation, **conservez son mode**. Si la source évalue, vous rapportez une évaluation ; si la source observe, vous rapportez une observation. Et citez la source précisément : *« [éditeur] évalue avec une confiance modérée que… »* est infiniment plus utile que *« il apparaît que… »*.

#### 4.7 ⚠️ Comment ces axiomes sont violés en pratique

Les six violations, dans l'ordre où on les rencontre :

| Axiome | Violation typique | Où on la trouve |
|---|---|---|
| Observer ≠ conclure | Verbes d'intention dans une section de faits | Partout, y compris dans des rapports officiels |
| Corrélation ≠ causalité | Trois victimes d'un secteur → « le secteur est ciblé » | Rapports commerciaux, presse spécialisée |
| Absence de preuve | « Nous n'avons rien trouvé, donc l'adversaire est sophistiqué » | Rapports post-incident |
| Périssabilité | Un rapport de 2027 cité en 2029 au présent | Notes internes, présentations |
| Analyse ≠ description | Dix pages de faits, aucune conclusion | Produits internes de fonctions immatures |
| Source ≠ fait | Une évaluation modérée recopiée comme un fait établi | **Toute la chaîne de reprise, du premier au dernier maillon** |

#### 4.8 🔬 Mini-lab 1 — Repérer les six violations

**Objectif** — Identifier les violations d'axiomes dans un produit réel et les corriger.
**Durée** 30 min · **Difficulté** 🟢 débutant · **Prérequis** §4.1 à §4.6 · **Livrable** version corrigée du texte
**Compétences validées** — ✔ séparer observation et déduction ✔ repérer un verbe d'intention ✔ identifier une corrélation prise pour une cause ✔ détecter une perte de mode dans une reprise de source ✔ dater une évaluation

**Le texte à analyser** — extrait d'une note interne fictive, huit phrases numérotées :

> **(1)** Le 3 novembre, notre passerelle d'accès distant a été prise pour cible par un acteur cherchant à obtenir un accès initial. **(2)** Douze tentatives d'authentification ont échoué entre 02 h 50 et 03 h 40 sur des comptes inexistants. **(3)** L'adresse source appartient à un fournisseur d'infrastructure à la demande et apparaît dans deux publications récentes. **(4)** Selon ces publications, il est établi que le groupe TEMPEST-14 mène une campagne contre le secteur de la santé. **(5)** Trois établissements de santé européens ont été victimes de rançongiciels en six semaines, ce qui confirme le ciblage sectoriel. **(6)** Nos recherches dans les journaux n'ont mis en évidence aucune compromission, l'adversaire est donc soit absent, soit particulièrement discret. **(7)** Le mode opératoire correspond à celui décrit dans un rapport de référence sur ce groupe. **(8)** Nous recommandons un renforcement de la surveillance.

**Consigne** : identifiez la violation dans chaque phrase concernée, nommez l'axiome, et proposez une reformulation.

---

**Corrigé commenté**

| # | Violation | Axiome | Reformulation |
|---|---|---|---|
| **(1)** | *Prise pour cible*, *acteur cherchant à obtenir* : trois déductions présentées comme des observations — qu'il y ait un acteur, qu'il cible, qu'il cherche un accès initial | **4.1** | *« Notre passerelle a fait l'objet d'une activité d'authentification anormale. »* La déduction va en section évaluation |
| **(2)** | Aucune. C'est une observation correcte, datée, bornée | — | À conserver telle quelle — c'est le modèle |
| **(3)** | Aucune violation, mais **une information manquante** : ces deux publications sont-elles indépendantes ? | 4.6 *(en germe)* | Ajouter : *« indépendance des deux sources à vérifier »* |
| **(4)** | *Il est établi que* : la source dit « selon ces publications », donc rapporte une évaluation. Le mode a été perdu | **4.6** | *« Ces publications évaluent — avec un niveau de confiance qu'elles ne précisent pas — que… »* |
| **(5)** | *Ce qui confirme* : trois victimes du même secteur ne confirment rien. Elles sont compatibles avec un ciblage sectoriel **et** avec l'exploitation massive d'un produit commun | **4.2** | *« Trois établissements ont été victimes en six semaines. Cette concomitance est compatible avec un ciblage sectoriel comme avec l'exploitation d'un composant commun ; nous n'avons pas d'élément pour trancher. »* |
| **(6)** | *L'adversaire est donc soit absent, soit particulièrement discret* : conclusion tirée du vide. La troisième possibilité — nous n'avons pas les capteurs — est omise | **4.3** | *« Nos recherches n'ont pas mis en évidence de compromission. Nos journaux couvrent 30 jours et ne tracent pas [X] ; cette absence ne permet donc pas de conclure. »* |
| **(7)** | *Correspond à* : une similarité présentée comme une identification. Et *rapport de référence* n'est pas une source citable | **4.6** | *« Le mode opératoire présente des similarités avec celui décrit dans [référence précise, date]. »* Et **aucune** conclusion d'attribution — voir chapitre 13 |
| **(8)** | Recommandation sans évaluation préalable ni horizon | **4.5, 4.4** | La note ne contient aucune évaluation calibrée : elle enchaîne des faits et une recommandation. Ajouter une section d'évaluation, et dater : *« évaluation au 5 novembre 2029, réexamen sous 30 jours »* |

**Le score** : six violations sur huit phrases. Ce n'est pas une note particulièrement mauvaise — c'est une note ordinaire, et vous en lirez beaucoup de ce type.

**Les deux erreurs attendues chez le lecteur**
1. Considérer la phrase (2) comme insuffisante parce qu'elle « ne conclut rien ». C'est au contraire la seule phrase parfaitement écrite : elle est dans la section faits, et son rôle est d'observer.
2. Corriger la phrase (5) en supprimant la conclusion sans proposer d'explication alternative. Le travail d'analyse ne consiste pas à retirer les conclusions, mais à les mettre en concurrence.

#### 4.9 🔴 FIL ROUGE — juin 2029 : Nour relit sa première note

Après l'épisode du redécoupage (§3.8), Claire Nadeau demande à Nour un exercice inhabituel : relire sa note du 22 mai avec les six axiomes en main, et marquer chaque phrase qui n'y résiste pas.

Nour y passe deux heures. Le résultat la surprend.

| Constat | Nombre |
|---|---|
| Phrases contenant un verbe d'intention en section factuelle | 9 |
| Affirmations reprises d'une source en ayant perdu son mode | **4** |
| Conclusions tirées d'une concomitance | 2 |
| Évaluations sans date de réexamen | Toutes |
| Sections indiquant ce qui invaliderait l'analyse | **0** |

**Les quatre affirmations qu'elle ne peut pas justifier** sont les plus instructives. Toutes proviennent de la même mécanique : elle a lu trois publications, formé une image cohérente, et écrit cette image — sans revenir vérifier ce que chaque source disait exactement, ni avec quelle prudence.

En remontant, elle découvre que **deux des trois publications citaient la même source primaire**. Son « recoupement » n'en était pas un.

**Ce qu'elle en tire**, et qu'elle écrit dans son carnet :

> *Je n'ai pas menti et je n'ai pas été négligente. J'ai fait ce que fait tout le monde : j'ai résumé. Le problème est que résumer, c'est perdre le mode. Et perdre le mode, c'est transformer une prudence en certitude sans s'en apercevoir.*

**Ce que Claire décide.** Pas un contrôle supplémentaire — une **relecture croisée** : à partir de juillet, tout produit destiné à sortir d'HELIOMED est relu par une seconde personne, avec une seule consigne, les six axiomes en main. Dix minutes par produit. C'est le chapitre 12.

**Livrable de l'épisode.** Une grille de relecture d'une demi-page — les six axiomes, une case par phrase suspecte. Elle figure en annexe C.

→ La suite en 🔴 §5.6, avec la première semaine de Nour racontée heure par heure — et ce qu'elle révèle de la répartition réelle du temps.

#### Synthèse mentale du chapitre 4

Six énoncés simples éliminent l'essentiel des mauvais raisonnements. Observer n'est pas conclure : l'interprétation arrive collée au fait, et il faut un effort délibéré pour les séparer — le test consiste à remplacer le verbe par « nous observons ». La corrélation mord particulièrement fort en CTI, où les coïncidences sont abondantes : trois victimes d'un secteur peuvent être trois clients d'un même fournisseur. L'absence appelle une question sur votre capacité d'observation, jamais une conclusion sur le réel — ai-je cherché au bon endroit, avec les bons capteurs, assez longtemps. Tout renseignement se périme, et un produit doit porter son horizon de validité, pas seulement sa date. Une analyse est une hypothèse argumentée et révisable : décrire sans conclure n'est pas de la prudence, c'est une analyse absente. Enfin, une source n'est pas un fait, et la violation est invisible : elle se produit au moment où l'on recopie en perdant le mode, transformant une évaluation prudente en certitude établie.

**Trois questions de vérification**

1. « Le groupe X cible le secteur bancaire. » Cette phrase peut-elle figurer dans une section de faits observés ? Justifiez, et proposez la reformulation.
2. Une recherche dans vos journaux ne trouve aucune trace de compromission. Quelles trois questions posez-vous avant d'en tirer la moindre conclusion ?
3. Vous reprenez une affirmation d'un rapport d'éditeur dans votre propre note. Qu'est-ce qui se perd si vous n'y prenez pas garde, et pourquoi cette perte est-elle invisible ?

→ **Chapitre 5 — Ce que fait réellement un analyste** : une journée heure par heure, et la part surprenante du temps consacrée à autre chose que la technique.

---

### Chapitre 5 — Ce que fait réellement un analyste

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
