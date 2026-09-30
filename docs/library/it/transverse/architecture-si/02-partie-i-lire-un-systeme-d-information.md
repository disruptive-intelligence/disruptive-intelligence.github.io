---
title: PARTIE I — Lire un système d'information
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 2
chapters: 10
---

Cette partie ne vous apprendra aucun composant. Elle installe **un regard** : quatre questions, six contraintes, trois familles de flux, et l'idée que tout ce que vous verrez est le produit d'arbitrages faits par d'autres, à des époques différentes.

À la fin, vous ne saurez pas encore lire le schéma du chapitre 1. Vous saurez **quoi y chercher**.

---

### Chapitre 1 — Pourquoi un système d'information ressemble à ça

#### 1.1 Le schéma que vous ne comprenez pas encore

Voici le système d'information du groupe HELIOMED, en décembre 2025. C'est le schéma que le cours va éclairer, fragment par fragment.

🖼 **SCHÉMA 1.1 — HELIOMED, vue d'ensemble** · *Version graphique à produire : quatre bandes horizontales colorées par zone, composants iconographiés, flux principaux en trait plein, flux de dépendance en pointillé.*

```
                            I N T E R N E T
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
              [ pare-feu ]                  [ pare-feu ]
                    └──────────────┬──────────────┘
                                   │
   ╔═══════════════════════════════╪═══════════════════════════════╗
   ║  ZONE DÉMILITARISÉE           │                               ║
   ║                    ┌──────────┴──────────┐                    ║
   ║              [ mandataire inverse ]  [ relais messagerie ]    ║
   ║                          │                                    ║
   ║              [ répartiteur de charge ]                        ║
   ╚══════════════════════════╪════════════════════════════════════╝
                              │
   ╔══════════════════════════╪════════════════════════════════════╗
   ║  RÉSEAU INTERNE          │                                    ║
   ║              ┌───────────┴───────────┐                        ║
   ║        [ web 1 ]  [ web 2 ]  [ web 3 ]                        ║
   ║              └───────────┬───────────┘                        ║
   ║                    [ applicatif ]                             ║
   ║                          │                                    ║
   ║                  [ base de données ]                          ║
   ║                                                               ║
   ║   [ annuaire ]   [ fichiers ]   [ sauvegarde ]   [ postes ]   ║
   ╚═══════════════════════════════════════════════════════════════╝
                              │
   ╔══════════════════════════╪════════════════════════════════════╗
   ║  SITE INDUSTRIEL — Saint-Étienne                              ║
   ║        [ supervision ]  ──  [ automates ]                     ║
   ╚═══════════════════════════════════════════════════════════════╝
```

❓ **QUE VOYEZ-VOUS ?**

Ne cherchez pas à comprendre. Répondez seulement à ceci, et notez vos réponses :

1. Combien de zones distinguez-vous ?
2. Par où arrive un utilisateur venu d'Internet ?
3. Où sont les données ?
4. Qu'est-ce qui, sur ce schéma, peut tomber sans que le service s'arrête ?
5. **Qu'est-ce qui manque ?**

**La cinquième question est la plus importante du cours**, et vous ne pouvez pas encore y répondre. À la fin du chapitre 50, vous saurez qu'il manque au moins onze choses sur ce schéma — dont la résolution de noms, la synchronisation d'horloge, les chemins d'administration, et l'ensemble des services en ligne utilisés par les métiers.

👁 **CE QU'IL FALLAIT OBSERVER, dès maintenant**

| Observation | Ce qu'elle indique |
|---|---|
| Deux pare-feu côte à côte | Une redondance : l'un peut tomber |
| Trois serveurs web, un seul applicatif | La redondance s'arrête à mi-parcours — **c'est un choix, pas un oubli** |
| Une seule base de données | Le point de rupture le plus probable du schéma |
| Le site industriel n'a qu'un lien | Il est relié, mais peu |
| L'annuaire est dessiné, sans aucun trait | **Personne ne s'y connecte, sur ce schéma. C'est faux, et c'est normal** |

**La dernière ligne contient déjà tout le cours.** L'annuaire est utilisé par presque tout ce qui figure sur ce schéma, et aucun trait ne le montre. Ce n'est pas une erreur du dessinateur : c'est une convention. Les schémas ne dessinent pas les flux de dépendance — c'est la règle principe des trois flux, et c'est le chapitre 30.

#### 1.2 Ce que ce cours n'est pas

Quatre disciplines voisines sont régulièrement confondues avec celle-ci. Autant le dire en dix lignes.

| Ce n'est pas… | Qui s'en occupe | Ce que ce cours en retient |
|---|---|---|
| **L'architecture d'entreprise** | Urbanistes, référentiels de cadrage | Rien. Ce cours ne produit ni cartographie d'entreprise, ni référentiel de transformation |
| **Le fonctionnement des composants** | Formations produit, documentation éditeur | Uniquement ce qui éclaire une décision — *principe de coupe* |
| **L'administration système et réseau** | Exploitation | Aucune commande, aucune configuration |
| **L'ingénierie et le dimensionnement** | Architectes techniques, ingénieurs | Le raisonnement, pas les calculs |

**Ce que ce cours enseigne, et qu'aucune des quatre ne fait** :

> **Pourquoi les choses sont agencées ainsi, ce que chaque agencement résout, ce qu'il coûte — et comment raisonner un agencement nouveau.**

⚠️ **La confusion à éviter dès maintenant.** Un cours *« comment fonctionne un système d'information »* expliquerait le détail d'un protocole de résolution de noms. Celui-ci explique **pourquoi la résolution de noms est le point de rupture le plus spectaculaire d'une architecture**. Ce n'est pas le même objet, et ce n'est pas le même métier.

#### 1.3 Les quatre questions du lecteur

Le modèle de poche du cours. Devant n'importe quel schéma, quatre questions — et l'ordre compte.

🖼 **SCHÉMA 1.2 — Les quatre questions** · *Quatre bandeaux, le quatrième distinct : il ne décrit pas le système, il décrit ce qu'on peut y faire.*

```
   ┌───────────────────────────────────────────────────┐
   │  ①  QU'EST-CE QUI CIRCULE ?                       │
   │      métier · dépendance · exploitation           │
   ├───────────────────────────────────────────────────┤
   │  ②  PAR OÙ ?                                      │
   │      le chemin, dans l'ordre, sans en sauter      │
   ├───────────────────────────────────────────────────┤
   │  ③  QU'EST-CE QUI S'ARRÊTE SI ÇA TOMBE ?          │
   │      ruptures · redondances · dégradations        │
   ├═══════════════════════════════════════════════════┤
   │  ④  OÙ PEUT-ON AGIR ?                             │
   │      observer · filtrer · authentifier            │
   │      · segmenter · journaliser                    │
   └───────────────────────────────────────────────────┘
```

| Question | Ce qu'elle permet | Chapitres |
|---|---|---|
| ① Qu'est-ce qui circule ? | Distinguer trois familles de flux, dont deux invisibles | 3, 29-35 |
| ② Par où ? | Reconstituer un chemin complet, y compris ce qui n'est pas dessiné | 29-35 |
| ③ Qu'est-ce qui s'arrête ? | Identifier les points de rupture réels, pas les composants qui font peur | 35 |
| ④ **Où peut-on agir ?** | **Le raccordement à toute la collection** | 43-45 |

**La quatrième est la porte de sortie du cours.** Elle ne décrit pas le système : elle décrit ce qu'on peut en faire — et elle est déterminée par des décisions prises avant vous, souvent des années avant.

🧪 **EN PRATIQUE — le test des quatre questions**

Prenez le schéma d'architecture de votre organisation. Posez les quatre questions. Comptez les réponses obtenues sans appeler personne.

| Réponses sur 4 | Ce que cela dit |
|---|---|
| 4 | Vous lisez déjà une architecture |
| 2 à 3 | Vous reconnaissez les composants, pas les flux |
| 0 à 1 | Vous regardez un dessin |

**La question ① est celle qui échoue le plus souvent**, y compris chez des professionnels expérimentés — parce que personne n'enseigne que trois choses différentes circulent.

#### 1.4 Les six contraintes qui produisent toute architecture

**Le principe fondateur du cours** :

> ### Toute architecture est un compromis.

Elle n'a pas été conçue : elle a été **négociée**, entre six contraintes qui se contredisent deux à deux.

| Contrainte | Ce qu'elle demande | Avec quoi elle entre en conflit |
|---|---|---|
| **Disponibilité** | Que le service tienne malgré les pannes | Le **coût** — chaque redondance double quelque chose |
| **Performance** | Que ce soit rapide | La **sécurité** — chaque contrôle ajoute un temps |
| **Coût** | Que ce soit finançable | **Tout le reste** |
| **Sécurité** | Que ce soit cloisonné, contrôlé, tracé | La **performance** et la **simplicité d'exploitation** |
| **Conformité** | Que ce soit démontrable et conforme aux règles | Le **coût** et le **délai** |
| **Histoire** | Que ce qui existe continue de fonctionner | **Tout le reste** |

⚠️ **La sixième est celle qu'on oublie, et c'est souvent la plus puissante.** Une architecture doit composer avec ce qui est déjà là : un progiciel qui exige une version ancienne, une base qu'on ne peut pas migrer, un site racheté avec son propre annuaire. Le chapitre 4 lui est consacré.

##### Ce que la contradiction produit concrètement

🖼 **SCHÉMA 1.3 — Trois arbitrages, trois architectures différentes** · *Trois variantes du même besoin, avec le curseur déplacé.*

```
  BESOIN : publier une application interne pour 200 salariés nomades

  ARBITRAGE A — coût prioritaire
  Internet ──► [ pare-feu ] ──► [ serveur applicatif ]
  → simple · peu cher · une panne = service arrêté · exposition directe

  ARBITRAGE B — disponibilité prioritaire
  Internet ──► [ pare-feu ×2 ] ──► [ répartiteur ×2 ] ──► [ serveurs ×3 ]
  → tient aux pannes · trois fois plus de composants à exploiter

  ARBITRAGE C — sécurité prioritaire
  Internet ──► [ pare-feu ] ──► [ mandataire inverse ] ──► [ authentification ]
            ──► [ serveur applicatif ]  (aucune exposition directe)
  → contrôlé · un composant de plus · une latence · une dépendance forte
    à l'authentification
```

**Aucun des trois n'est meilleur.** Ils répondent à trois arbitrages différents, et chacun serait une erreur dans le contexte des deux autres.

**Ce que le lecteur doit savoir faire à la fin du cours** : regarder une architecture réelle et **reconstituer l'arbitrage** qui l'a produite. C'est la définition de *raisonner*.

#### 1.5 Les trois familles de flux

Première présentation ; le chapitre 3 la développe et la Partie V l'exploite.

| Famille | Question | Sur les schémas |
|---|---|---|
| **Flux métier** | Qu'est-ce que le service transporte ou traite ? | **Dessiné** |
| **Flux de dépendance** | Sans quoi le service ne peut pas s'établir ? | **Rarement dessiné** |
| **Flux d'exploitation** | Ce qui permet de tenir, observer, restaurer | **Presque jamais dessiné** |

**L'exemple qui installe la distinction** — un salarié ouvre une application interne :

```
  FLUX MÉTIER          poste ──► mandataire ──► web ──► applicatif ──► base
                       (le chemin dessiné)

  FLUX DE DÉPENDANCE   poste ──► résolution de noms      ← sans elle : rien
                       poste ──► annuaire                ← sans lui : pas d'accès
                       poste ──► validation certificat   ← sans elle : avertissement
                       serveurs ──► serveur de temps     ← sans lui : rejets

  FLUX D'EXPLOITATION  serveurs ──► collecte de journaux ← sans elle : on est aveugle
                       serveurs ──► supervision          ← sans elle : on ne sait pas
                       serveurs ──► sauvegarde           ← sans elle : pas de reprise
```

**Trois observations essentielles.**

**Les flux de dépendance ne sont presque jamais sur le schéma**, et pourtant leur rupture **arrête le service**. C'est l'explication structurelle du *« tout est vert et pourtant ça ne marche pas »*.

**Les flux d'exploitation ne conditionnent pas le service.** Si la collecte de journaux tombe, l'application continue de fonctionner — vous devenez aveugle, ce qui est grave autrement. **Ne pas confondre les deux est une compétence.**

**Les trois empruntent des chemins différents**, traversent des zones différentes, et échouent pour des raisons différentes.

⚠️ **PIÈGE — l'erreur de catégorie**
Ranger la sauvegarde ou la journalisation parmi les dépendances conduit à surdimensionner ce qui n'a pas besoin de l'être, et à sous-estimer ce qui compte vraiment. Le test tient en une question : **si ce flux s'arrête, le service continue-t-il de rendre son objet ?** Si oui, c'est de l'exploitation.

#### 1.6 Les trois architectures de référence

Trois organisations accompagneront tout le cours, à côté d'HELIOMED. Elles servent une seule chose : montrer **à partir de quelle contrainte un composant apparaît**.

| | **ATELIER MARTIN** | **HELIOMED** | **GROUPE NOVARIS** |
|---|---|---|---|
| Effectif | 40 | 1 380 | 12 000 |
| Sites | 1 | 3 | 40, 6 pays |
| Informatique | 1 personne à mi-temps | 14 personnes | 180 personnes |
| Activité | Menuiserie industrielle | Dispositifs médicaux connectés | Distribution |

⚠️ **Le principe de la contrainte s'applique à chaque comparaison** :

> **La taille ne justifie jamais seule une brique d'architecture. C'est la contrainte qui la justifie.**

**Ce que cela interdit d'écrire**, et ce qui sera systématiquement reformulé :

| Formulation interdite | Formulation retenue |
|---|---|
| « Une organisation de 12 000 personnes a plusieurs forêts d'annuaire » | « Novaris a plusieurs forêts **parce qu'elle a absorbé quatre sociétés en huit ans et n'a jamais fusionné les annuaires** » |
| « Une PME n'a pas de zone démilitarisée » | « Atelier Martin n'en a pas **parce qu'elle ne publie aucun service : la contrainte n'existe pas** » |
| « À partir de 1 000 salariés, il faut une infrastructure de clés interne » | « HELIOMED en a une **parce qu'elle doit émettre des certificats pour des équipements médicaux qu'aucune autorité publique ne signera** » |

**La question posée à chaque composant, dans les cinquante chapitres** :

> ### À partir de quelle contrainte ce composant devient-il nécessaire ?

#### 1.7 La doctrine — neuf principes

> **1. Toute architecture est un compromis.** Elle n'a pas été conçue, elle a été négociée.

> **2. Aucune architecture n'a été construite d'un bloc.** Le legacy est l'état normal.

> **3. Un composant s'explique par ce qui se passe s'il disparaît.**

> **4. Le service compte, pas le serveur.**

> **5. Suivre un flux vaut mieux que lire une boîte.**

> **6. Le système d'information n'existe que pour traiter de la donnée.**

> **7. Concevoir, c'est choisir ce qu'on accepte de perdre.**

> **8. La taille ne justifie jamais une brique. La contrainte, oui.**

> **9. Ajouter n'est jamais gratuit.** Avant d'ajouter un composant, savoir énoncer la contrainte qu'il résout **et** le coût qu'il introduit.

> **10. Un schéma révèle une *intention* de redondance ; seul un test établit une *capacité* de basculement.**

> **11. Un composant qu'on ne sait pas exploiter dégrade l'architecture au lieu de l'améliorer.**

> **12. Une architecture dessinée n'est pas une architecture réelle.** *(chapitre 50)*

#### 1.8 La phrase fondatrice

> ### Apprendre à raisonner une architecture, c'est savoir reconstituer les arbitrages qui l'ont produite — et énoncer ceux qu'on propose.

Elle explique pourquoi ce cours consacre un chapitre à la sédimentation avant tout composant, pourquoi chaque brique porte son coût, et pourquoi il se termine sur ce qu'un schéma ne dira jamais.

**Ce que le lecteur saura faire au chapitre 50**, et qui est différent de savoir concevoir :

> *Poser les bonnes questions, proposer une architecture justifiée, et identifier ce qu'il lui reste à vérifier.*

🔴 **FIL ROUGE — décembre 2025 : Amélie regarde un schéma**

*Le fil rouge de ce cours suit six semaines. Il se termine exactement là où commence le volume Asset Management de cette collection — à la même réunion, à la même phrase.*

Amélie Roux est administratrice système à Nantes depuis quatre ans. Elle connaît bien la vingtaine de serveurs de la recherche et développement, la chaîne de construction logicielle, et le réseau du bâtiment.

**Le 15 décembre 2025**, Claire Nadeau, responsable de la sécurité du groupe, lui propose une mission d'un an : établir l'inventaire du système d'information d'HELIOMED. Trois sources donnent trois chiffres différents — 96, 71 et 118 serveurs — et personne ne sait lequel est vrai.

**Amélie accepte, et demande le schéma d'architecture du groupe.**

Ce qu'elle reçoit est le schéma 1.1. Il date de mars 2023, il fait une page, et il porte la mention *« version de travail »*.

**Voici ce qu'elle comprend en le lisant**, et voici ce qu'elle ne comprend pas.

| Ce qu'elle comprend | Ce qu'elle ne comprend pas |
|---|---|
| Il y a des zones séparées | Pourquoi la zone du milieu s'appelle « démilitarisée » |
| Les serveurs web sont en trois exemplaires | Pourquoi trois, et pourquoi l'applicatif est seul |
| Il y a un « mandataire inverse » | À quoi il sert — elle croit que c'est un pare-feu |
| Le site industriel est à part | Pourquoi il n'a qu'un seul lien |
| La base de données est en bas | S'il y en a une seule, et ce qui se passe si elle tombe |

**Les cinq questions qu'elle pose à Malik Ferhaoui, responsable de l'exploitation**, et qui structurent le cours :

1. *« Le mandataire inverse, c'est un pare-feu ? »* → chapitre 12
2. *« Pourquoi trois serveurs web et un seul applicatif ? »* → chapitres 13 et 35
3. *« Si la base tombe, qu'est-ce qui s'arrête ? »* → chapitre 35
4. *« Où sont les postes de travail ? Ils ne sont pas dessinés. »* → chapitre 6
5. *« Et l'annuaire, personne ne s'y connecte ? »* → chapitre 30

**La réponse de Malik à la cinquième question** est celle qu'Amélie retiendra, et elle contient le cours entier :

> *« Tout le monde s'y connecte. On ne le dessine jamais, sinon le schéma serait illisible. »*

**Ce qu'Amélie note dans son carnet, le 15 décembre** :

> *Je ne pourrai pas inventorier ce système tant que je ne saurai pas ce que je regarde. Avant de compter, il faut comprendre.*

**Livrable de l'épisode.** Le schéma de mars 2023, et la liste de ses cinq questions — qui deviendra, au fil du cours, la liste de ce que le schéma ne dit pas.

→ La suite en 🔴 §2.6, quand un mot employé par trois personnes désignera trois choses différentes.

#### Synthèse mentale du chapitre 1

Toute architecture est un compromis : elle n'a pas été conçue, elle a été négociée entre six contraintes qui se contredisent deux à deux — disponibilité, performance, coût, sécurité, conformité, et l'histoire, qu'on oublie et qui est souvent la plus puissante. Trois arbitrages différents produisent trois architectures différentes pour un même besoin, et aucune n'est meilleure : chacune serait une erreur dans le contexte des deux autres. Quatre questions structurent la lecture, et la première échoue le plus souvent parce que personne n'enseigne que trois choses différentes circulent : le flux métier, dessiné · le flux de dépendance, rarement dessiné et dont la rupture arrête le service · le flux d'exploitation, presque jamais dessiné et dont la rupture rend aveugle sans arrêter le service. Confondre les deux derniers conduit à surdimensionner ce qui n'en a pas besoin. Enfin, la taille d'une organisation ne justifie jamais un composant : la contrainte, oui — et ajouter n'est jamais gratuit.

**Trois questions de vérification**

1. Un même besoin peut produire trois architectures différentes. Qu'est-ce qui les distingue, et laquelle est la meilleure ?
2. La collecte de journaux s'interrompt. Le service s'arrête-t-il ? À quelle famille de flux appartient-elle, et pourquoi la distinction compte-t-elle ?
3. Sur un schéma, un annuaire est dessiné sans aucun trait de connexion. Est-ce une erreur ? Que cela vous apprend-il sur les schémas en général ?

→ **Chapitre 2 — Le vocabulaire** : trois personnes emploient le mot « serveur », et désignent trois choses différentes.

---

### Chapitre 2 — Le vocabulaire

> Ce chapitre est court et il n'est pas facultatif. La moitié des malentendus d'architecture viennent de mots que trois personnes emploient en désignant trois choses.

#### 2.1 Les mots qui désignent trois choses

##### « Serveur »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | **Une machine** — physique ou virtuelle |
| Le développeur | **Un logiciel qui écoute** — un serveur web, un serveur de base de données |
| Le métier | **Un service** — « le serveur de paie est tombé » |

**Une même machine peut donc porter trois serveurs**, et un même serveur peut être réparti sur trois machines. Quand quelqu'un dit *« on a 96 serveurs »*, la première question utile est : *machines, logiciels ou services ?*

##### « Application »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | Un processus installé sur une machine |
| Le développeur | Un ensemble de code déployé |
| Le métier | **Ce qu'il ouvre le matin** — qui peut mobiliser huit composants |
| L'achat | Une licence, un contrat |

##### « Service »

Le mot le plus polysémique du domaine, et le plus important.

| Sens | Exemple | Chapitre |
|---|---|---|
| **Service technique** | Un processus qui tourne en arrière-plan | 18-23 |
| **Service réseau** | Ce qui écoute sur un port | 8-17 |
| **Service métier** | Ce qui produit une valeur pour l'organisation | **35** |
| Service au sens contractuel | Ce qui est facturé, avec un engagement | 38 |

⚠️ **Ce cours emploie « service » au sens métier** — chapitre 35 — sauf mention explicite. C'est le sens qui permet de décider.

##### Les autres pièges

| Mot | Ambiguïté |
|---|---|
| **Plateforme** | Un ensemble matériel · un socle logiciel · un produit commercial |
| **Instance** | Une machine · un processus · un locataire chez un fournisseur |
| **Cluster** | Un groupe de machines redondantes · un groupe qui répartit la charge · un orchestrateur — **trois choses différentes** |
| **Nœud** | Une machine · un point du réseau · un membre d'un cluster |
| **Environnement** | Production, recette, développement · ou le contexte technique d'exécution |

#### 2.2 Le vocabulaire minimal

Douze mots suffisent pour lire un schéma. Les voici, définis pour la lecture — pas pour l'exactitude protocolaire *(principe de coupe)*.

| Terme | Ce qu'il faut en savoir pour lire |
|---|---|
| **Client** | Ce qui demande. Un poste, mais aussi un serveur qui en appelle un autre |
| **Serveur** | Ce qui répond. Le rôle, pas la machine |
| **Protocole** | La convention de dialogue. Sur un schéma, il indique **la nature du flux** |
| **Port** | Le numéro qui identifie le service sur une machine. Il dit **quoi**, pas **où** |
| **Adresse** | Où se trouve une machine sur le réseau. Elle change |
| **Nom** | Ce qu'on retient. Il faut le traduire en adresse — chapitre 14 |
| **Segment** | Un morceau de réseau, isolé des autres par un équipement |
| **Zone** | Un regroupement de segments partageant un même niveau de confiance |
| **Flux** | Ce qui circule entre deux points, dans une direction |
| **Session** | Une conversation en cours, avec un état — chapitre 31 |
| **Redondance** | Deux exemplaires d'un même rôle, dont un peut tomber |
| **Point de rupture** | Ce qui, en tombant, arrête un service. **La notion la plus utile du cours** |

**Ce qui ne figure pas dans cette liste, volontairement** : les couches d'un modèle en sept niveaux, les classes d'adresses, les mécanismes de contrôle de congestion. Ils ne servent pas à lire un schéma — *principe de coupe*.

#### 2.3 Le vocabulaire du terrain

Comme dans les autres volumes de la collection : ce que dit le cours, et ce que vous entendrez.

| Terme du cours | Ce que vous entendrez | Nuance à ne pas perdre |
|---|---|---|
| Mandataire inverse | « **le reverse** », « le proxy », « le frontal » | On l'appelle « proxy » alors qu'il fait l'inverse — chapitre 12 |
| Mandataire sortant | « **le proxy** » | Même mot, fonction opposée |
| Répartiteur de charge | « **le load balancer** », « le LB », « la VIP » | La « VIP » désigne l'adresse virtuelle, pas l'équipement |
| Zone démilitarisée | « **la DMZ** » | Le mot est militaire et trompeur — chapitre 25 |
| Point de rupture unique | « **le SPOF** » | — |
| Résolution de noms | « **le DNS** » | Souvent employé pour désigner le service **et** le serveur |
| Annuaire | « **l'AD** », « le LDAP », « le domaine » | Trois choses différentes, souvent confondues |
| Infrastructure de clés | « **la PKI** », « les certifs » | — |
| Poste d'administration | « **le bastion** », « le jump », « le rebond » | — |
| Segment réseau | « **le VLAN** », « le subnet » | Deux notions distinctes, souvent alignées mais pas toujours |
| Flux de dépendance | *(aucun terme courant)* | **L'absence de mot est le problème** — règle principe des trois flux |
| Orchestrateur | « **le cluster** », « K8s », « la plateforme » | — |

⚠️ **La ligne « flux de dépendance » est la plus significative du tableau.** Il n'existe pas de terme courant pour désigner ce sans quoi un service ne peut pas s'établir. C'est l'une des raisons pour lesquelles ces flux sont invisibles sur les schémas : **on ne dessine pas ce qu'on ne nomme pas.**

#### 2.4 Lire un protocole sur un schéma

Sans entrer dans leur fonctionnement, six protocoles suffisent à identifier la nature d'un flux.

| Ce qui est écrit | Ce que ça vous dit du flux |
|---|---|
| `443`, `HTTPS` | Une consultation web chiffrée — flux **métier**, le plus courant |
| `80`, `HTTP` | Idem, non chiffré. Sur un schéma récent, c'est une **question à poser** |
| `53`, `DNS` | Résolution de noms — flux de **dépendance** |
| `389`, `636`, `LDAP` | Annuaire — flux de **dépendance** |
| `123`, `NTP` | Synchronisation d'horloge — flux de **dépendance**, presque jamais dessiné |
| `514`, `syslog` | Journaux — flux d'**exploitation** |
| `3389`, `22` | Administration à distance — flux d'**exploitation**, **le plus sensible** |
| `1433`, `3306`, `5432` | Bases de données — flux **métier**, entre serveurs |

**Ce que ce tableau permet immédiatement** : classer un flux dans l'une des trois familles sans rien connaître du protocole. C'est le principe de coupe appliqué — juste ce qu'il faut pour décider.

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. Aucun numéro de port n'y figure. Vous ne pouvez donc pas savoir quels flux le traversent réellement. **C'est le cas de la majorité des schémas d'architecture**, et c'est la première chose qui manque quand on veut raisonner.

#### 2.5 🔬 Mini-lab 1 — Quatre phrases, quatre malentendus

**Objectif** — Repérer une ambiguïté de vocabulaire et poser la question qui la lève.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §2.1 à §2.3
**Compétences validées** — ✔ identifier un mot polysémique ✔ formuler la question qui désambiguïse ✔ reconnaître les conséquences d'un malentendu

**Les phrases** :

```
① « On a 96 serveurs. »
② « L'application de paie est tombée ce matin. »
③ « Il faut mettre l'application derrière le proxy. »
④ « On a un cluster de trois nœuds. »
```

**Consigne** : pour chacune, dites quelles interprétations sont possibles, la question à poser, et ce que coûte le malentendu.

---

**Corrigé**

| # | Interprétations possibles | Question à poser | Ce que coûte le malentendu |
|---|---|---|---|
| **①** | 96 machines · 96 systèmes · 96 services · 96 lignes dans un référentiel | *« Machines physiques, machines virtuelles, ou services ? »* | Un dénominateur faux pour tout le reste — c'est le volume Asset Management |
| **②** | Un processus · un serveur · **un service métier composé de six composants** | *« Qu'est-ce qui ne marche plus, du point de vue de l'utilisateur ? »* | On redémarre une machine alors que le problème est ailleurs |
| **③** | Mandataire **sortant** — pour que l'application accède à Internet · mandataire **inverse** — pour qu'on y accède depuis Internet. **Fonctions opposées** | *« Pour sortir, ou pour entrer ? »* | On ouvre un flux dans le mauvais sens, ou on expose ce qui ne devait pas l'être |
| **④** | Trois machines redondantes · trois machines qui se répartissent la charge · trois nœuds d'un orchestrateur | *« Si un nœud tombe, que se passe-t-il ? »* | On croit avoir une redondance qu'on n'a pas |

**La phrase ③ est celle qui produit les erreurs les plus coûteuses**, parce que le même mot désigne deux fonctions opposées et que personne ne pense à demander.

**L'erreur attendue** : traiter ① comme une question de comptage. C'est une question de **définition** — et c'est exactement le chapitre 2 du volume Asset Management.

#### 2.6 🔴 FIL ROUGE — décembre 2025 : trois personnes, trois « serveurs »

Amélie reprend les trois chiffres de décembre — 96, 71, 118 — et pose à chacun une seule question : *« quand tu dis serveur, tu comptes quoi ? »*

| Interlocuteur | Ce qu'il compte | Chiffre |
|---|---|---|
| Malik Ferhaoui, exploitation | Des **machines** — physiques et virtuelles — qu'il administre | 96 |
| La comptabilité | Des **immobilisations** — du matériel acheté et non amorti | 71 |
| L'outil de scan | Des **adresses ayant répondu** — donc ni les machines éteintes, ni celles hors du segment balayé | 118 |

**Trois définitions, trois périmètres, aucune intersection complète.** Et une découverte : le scan compte **118 adresses**, pas 118 machines — deux serveurs à deux interfaces réseau y comptent quatre fois.

**Ce qu'Amélie note** :

> *Personne ne s'est trompé. Nous avons trois réponses à trois questions différentes, et nous n'avons posé aucune des trois.*

**Ce qui est décidé** : avant tout comptage, écrire ce que le mot désigne. Cette décision sera formalisée en janvier — c'est le chapitre 2 du volume Asset Management, et c'est la réunion de deux heures qui y est racontée.

→ La suite en 🔴 §3.7, quand Amélie apprendra à lire un schéma — et surtout ce qu'il ne dit pas.

#### Synthèse mentale du chapitre 2

Trois mots portent l'essentiel des malentendus d'architecture — serveur, application, service — et chacun désigne au moins trois choses selon qui parle. Une même machine peut porter trois serveurs, et un même serveur être réparti sur trois machines : la question utile devant un chiffre est toujours *machines, logiciels ou services ?* Douze termes suffisent pour lire un schéma, et le plus utile d'entre eux est le point de rupture. Six protocoles suffisent à classer un flux dans l'une des trois familles sans rien connaître de leur fonctionnement. Enfin, il n'existe pas de terme courant pour désigner un flux de dépendance — et cette absence de mot est l'une des raisons pour lesquelles ces flux ne sont jamais dessinés : on ne dessine pas ce qu'on ne nomme pas.

**Trois questions de vérification**

1. Quelqu'un vous annonce un nombre de serveurs. Quelle question posez-vous, et pourquoi ce n'est pas une question de comptage ?
2. « Mets l'application derrière le proxy. » Pourquoi cette phrase est-elle dangereuse, et que demandez-vous ?
3. Pourquoi l'absence de terme courant pour « flux de dépendance » a-t-elle un effet concret sur les schémas ?

→ **Chapitre 3 — Comment lire un schéma** : les conventions, et surtout ce qu'un schéma choisit de ne pas montrer.

---

### Chapitre 3 — Comment lire un schéma

> Chapitre méta, et l'un des plus utiles du cours. Personne n'enseigne à lire un schéma ; on suppose que c'est évident. Ce ne l'est pas.

#### 3.1 Ce qu'une boîte représente

**Le problème** : une boîte sur un schéma peut représenter cinq choses différentes, et rien ne l'indique.

| Ce que la boîte peut être | Comment le deviner |
|---|---|
| Une **machine** physique ou virtuelle | Nom d'hôte, mention d'un système |
| Un **rôle** — « serveur web » sans dire combien | Nom générique, absence de nom d'hôte |
| Un **groupe** — trois machines dessinées en une | Mention d'un nombre, boîtes empilées |
| Un **service** — un ensemble de composants | Nom métier, positionnement isolé |
| Un **fournisseur externe** — une boîte noire | Nom commercial, position en bordure |

⚠️ **Une confusion fréquente, et coûteuse** : lire un **rôle** comme une **machine**. « Serveur web » sur un schéma ne dit pas s'il y en a un ou douze — donc ne dit pas si c'est un point de rupture.

**La question à poser devant toute boîte** : *combien y en a-t-il réellement, et que se passe-t-il si l'un tombe ?*

#### 3.2 Ce qu'un trait représente

Un trait est encore plus ambigu qu'une boîte.

| Ce que le trait peut être | Fréquence |
|---|---|
| Un **câble** — une liaison physique | Sur les schémas physiques |
| Un **flux** — quelque chose circule | Sur les schémas de flux |
| Une **relation logique** — « dépend de », « appartient à » | Sur les schémas logiques |
| Une **adjacence réseau** — « peut joindre » | Fréquent, et rarement explicité |
| **Rien de précis** — le dessinateur reliait deux choses proches | **Plus fréquent qu'on ne croit** |

**Trois questions devant tout trait** :

```
1. Qui initie ? (le sens compte, et il est rarement fléché)
2. Qu'est-ce qui circule ? (quelle famille de flux)
3. Est-ce permis, ou seulement possible ?
```

⚠️ **La troisième est la plus importante en sécurité.** Un trait indique souvent une **possibilité technique**, pas une autorisation. Deux machines dans le même segment sont reliées, que ce soit voulu ou non.

#### 3.3 Les quatre vues d'un même système

**Une architecture ne se représente pas d'un seul schéma.** Il en faut au moins quatre, et confondre les vues est une source d'erreur permanente.

🖼 **SCHÉMA 3.1 — Le même système, quatre vues** · *Quatre panneaux côte à côte, mêmes composants, représentations différentes.*

| Vue | Ce qu'elle montre | Ce qu'elle cache | Qui la produit |
|---|---|---|---|
| **Physique** | Machines, câbles, baies, sites | Ce qui s'exécute dessus | Infrastructure |
| **Logique** | Rôles, zones, relations | Le nombre réel de machines | Architecture |
| **Flux** | Ce qui circule, dans quel sens, sur quel protocole | La topologie physique | Sécurité, réseau |
| **Service** | Ce qui produit une valeur métier | **Presque toute la technique** | Métier, continuité |

**Exemple, sur le même objet** :

```
VUE PHYSIQUE      3 machines dans la baie B12, site de Lyon

VUE LOGIQUE       [ serveurs web ] ──► [ applicatif ] ──► [ base ]

VUE FLUX          poste ──443──► mandataire ──8080──► web
                  web ──1433──► base
                  web ──389──► annuaire        ← dépendance

VUE SERVICE       « Télésuivi HelioLink » — disponible 24/7,
                  dépend de : authentification, base, réseau Lyon
```

**Ce que la comparaison enseigne** : la vue service ne mentionne aucune machine, et la vue physique ne mentionne aucun service. **Aucune des deux ne ment ; elles répondent à deux questions différentes.**

👁 **CE QU'IL FALLAIT OBSERVER** — la vue flux est la seule qui fasse apparaître l'annuaire. C'est pour cela qu'elle est la plus utile en sécurité, et la plus rare dans les organisations.

#### 3.4 Ce qui n'est jamais dessiné

**La liste la plus utile du chapitre.** Elle sera complétée au chapitre 50.

| Ce qui manque presque toujours | Pourquoi | Conséquence |
|---|---|---|
| **La résolution de noms** | Tout le monde s'y connecte, le schéma serait illisible | Sa panne paraît inexplicable |
| **L'annuaire** | Idem | On sous-estime son caractère critique |
| **La synchronisation d'horloge** | Considérée comme acquise | Une dérive produit des rejets d'authentification incompréhensibles |
| **Les chemins d'administration** | Ils ne servent pas le métier | **Ce sont souvent les plus sensibles** — chapitre 27 |
| **Les sauvegardes** | Elles ne participent pas au service nominal | On découvre en incident qu'elles passent par un chemin non protégé |
| **Les postes de travail** | Trop nombreux | **La majorité des incidents commence là** — chapitre 6 |
| **Les services en ligne** | Pas chez nous, donc pas dessinés | Chapitre 38 |
| **Les liens partenaires** | Anciens, oubliés | Chapitre 38 |
| **Les certificats et leur autorité** | Invisibles quand ça marche | Une expiration arrête un service sans prévenir |
| **Le temps** | Un schéma est instantané | On ne voit ni l'historique, ni ce qui est en cours de migration |
| **Les versions** | Ça alourdirait | On ne peut pas raisonner l'obsolescence |

🎯 **L'exercice à faire une fois dans sa carrière** : prenez le schéma de votre organisation et **dessinez au crayon les onze éléments ci-dessus**. La page devient illisible en quatre minutes. C'est exactement pour cela qu'ils ne sont pas dessinés — et c'est exactement pour cela qu'il faut savoir qu'ils existent.

#### 3.5 Les conventions courantes

Elles ne sont pas normalisées, mais elles reviennent.

| Convention | Signification habituelle |
|---|---|
| Position **haute** = extérieur | Internet en haut, données en bas |
| Position **basse** = données | La base est presque toujours au fond — chapitre 20 |
| Un **nuage** | Quelque chose qu'on ne maîtrise pas ou qu'on ne détaille pas |
| Des boîtes **empilées** | Plusieurs exemplaires du même rôle |
| Un trait **pointillé** | Un flux logique, une relation, ou un lien non permanent |
| Une **double ligne** | Une redondance, ou un lien à haut débit |
| Un composant **à cheval sur deux zones** | Il traverse une frontière — **toujours un point d'attention** |

⚠️ **Aucune de ces conventions n'est garantie.** Sur un schéma inconnu, la première question est : *y a-t-il une légende ?* S'il n'y en a pas — cas majoritaire — les conventions ci-dessus sont des hypothèses à vérifier, pas des certitudes.

#### 3.6 🔬 Mini-lab 2 — Un schéma à cinq boîtes

**Objectif** — Lire un schéma minimal et formuler ce qu'il ne dit pas.
**Durée** 25 min · **Difficulté** 🟢 débutant · **Prérequis** §3.1 à §3.5
**Compétences validées** — ✔ interroger une boîte ✔ interroger un trait ✔ identifier la vue employée ✔ lister l'invisible

**Le schéma** :

```
        Internet
            │
      [ pare-feu ]
            │
      [ serveur web ]
            │
      [ base de données ]
            │
      [ sauvegarde ]
```

❓ **QUE VOYEZ-VOUS ?**

1. Combien de machines ce schéma représente-t-il ?
2. Quelle vue est-ce ?
3. Que se passe-t-il si le serveur web tombe ?
4. Citez cinq choses qui manquent.
5. Le trait entre la base et la sauvegarde : qui initie ?

---

**Corrigé**

**1. On ne sait pas.** Chaque boîte peut être une machine, un rôle ou un groupe. Rien ne l'indique. **C'est la bonne réponse** — et c'est la première question à poser à l'auteur du schéma.

**2. Une vue logique**, probablement. Aucun protocole, aucune adresse, aucun site : ce n'est ni une vue physique, ni une vue de flux. Ce n'est pas non plus une vue service — aucun nom métier.

**3. On ne sait pas non plus.** S'il est unique, le service s'arrête. S'il représente un groupe, il ne se passe rien. **Le schéma ne permet pas de répondre à la question la plus importante qu'on puisse lui poser.**

**4. Ce qui manque** — au moins :

| Manquant | Effet |
|---|---|
| Résolution de noms | Sans elle, personne n'atteint le serveur |
| Authentification | Où prouve-t-on son identité ? |
| Chemins d'administration | Comment ces machines sont-elles administrées ? |
| Postes de travail | Les utilisateurs internes n'apparaissent pas |
| Protocoles et sens des flux | On ne sait pas ce qui circule |
| Journalisation, supervision | Aucun flux d'exploitation |
| Certificats | Le flux est-il chiffré ? |
| Le nombre d'exemplaires | Voir question 3 |

**5. La sauvegarde initie presque toujours.** C'est contre-intuitif au vu du sens de lecture du schéma, qui suggère un flux descendant. **Et c'est un point de sécurité majeur** : si la sauvegarde initie, elle possède un accès à la base — donc à toutes les données. Le trait ne dit rien du sens, et le sens change tout.

**Les deux erreurs attendues**

1. **Répondre « cinq machines ».** Le schéma ne le dit pas, et l'admettre est la compétence visée.
2. **Répondre « le service s'arrête » à la question 3.** C'est probable, ce n'est pas établi — et la différence entre les deux est ce que ce cours enseigne.

#### 3.7 🔴 FIL ROUGE — décembre 2025 : ce que le schéma ne dit pas

Amélie applique au schéma 1.1 les questions du §3.4. Elle liste ce qui n'y figure pas, et demande à Malik de confirmer.

| Élément absent | Existe-t-il ? | Réponse de Malik |
|---|---|---|
| Résolution de noms | **Oui**, deux serveurs | *« On ne les dessine jamais »* |
| Synchronisation d'horloge | **Oui** | *« Je n'y avais jamais pensé »* |
| Chemins d'administration | **Oui** | *« On passe par le réseau d'admin, il n'est pas sur ce schéma »* |
| Postes de travail | **620** | *« Ils sont partout, ça n'aurait pas de sens de les dessiner »* |
| Services en ligne | **« Une trentaine ? »** | *« Là, je ne sais pas. Ce n'est pas moi qui les gère »* |
| Sauvegarde | Oui | *« Elle est dessinée, mais son chemin ne l'est pas »* |
| Site de Nantes | **Oui** | *« Il n'est pas sur ce schéma. C'est un oubli »* |

**Deux réponses comptent plus que les autres.**

La cinquième — *« je ne sais pas »* — désigne un périmètre entier que personne ne suit. Ce sera le point le plus coûteux du volume Asset Management.

La septième — *« c'est un oubli »* — révèle que le schéma officiel du groupe **ne mentionne pas l'un de ses trois sites**. Depuis mars 2023.

**Ce qu'Amélie note** :

> *Le schéma n'est pas faux. Il est incomplet, et personne ne sait de combien. C'est exactement le problème que je suis censée résoudre.*

→ La suite en 🔴 §4.6, quand elle comprendra pourquoi l'architecture est « bizarre ».

#### Synthèse mentale du chapitre 3

Une boîte peut représenter cinq choses — machine, rôle, groupe, service ou fournisseur — et rien ne l'indique : la confusion coûteuse est de lire un rôle comme une machine, parce qu'elle empêche de savoir si c'est un point de rupture. Un trait est plus ambigu encore, et trois questions le désambiguïsent : qui initie, qu'est-ce qui circule, est-ce permis ou seulement possible. Quatre vues sont nécessaires pour représenter un système, et confondre les vues est une erreur permanente : la vue service ne mentionne aucune machine, la vue physique aucun service, et aucune ne ment. La vue de flux est la seule qui fasse apparaître les dépendances, ce qui la rend la plus utile en sécurité et la plus rare en pratique. Enfin, onze éléments ne sont presque jamais dessinés, dont la résolution de noms, l'annuaire, les chemins d'administration et les postes de travail — et si l'on tentait de les dessiner, la page deviendrait illisible en quatre minutes.

**Trois questions de vérification**

1. Un schéma porte une boîte « serveur web ». Quelles questions posez-vous avant d'en tirer une conclusion sur la disponibilité ?
2. Un trait relie une base de données à une sauvegarde. Pourquoi le sens compte-t-il, et qu'implique chaque réponse ?
3. Citez cinq éléments qui ne figurent sur aucun schéma d'architecture, et l'effet de leur absence.

---

### Chapitre 4 — La sédimentation

> Le chapitre qui explique pourquoi les systèmes d'information sont « bizarres ». Il évite plus de jugements naïfs que tout le reste du cours.

#### 4.1 Aucune architecture n'a été construite d'un bloc

**Le constat**, et il est vérifiable sur n'importe quel système en service depuis plus de cinq ans :

> Ce que vous regardez n'est pas une architecture. C'est un **empilement de décisions** prises à des époques différentes, sous des contraintes différentes, par des gens différents — dont la plupart ne travaillent plus là.

**Ce que le débutant pense** : *ils auraient dû refaire propre.*
**Ce que le praticien sait** : *ils n'en avaient pas la possibilité.*

**Les cinq raisons pour lesquelles on ne refait pas** :

| Raison | Mécanisme |
|---|---|
| **Le coût** | Reconstruire coûte plus cher que maintenir, souvent d'un ordre de grandeur |
| **Le risque** | Un système qui fonctionne mal fonctionne quand même. Une migration peut échouer |
| **La dépendance** | Un composant ancien porte une intégration que plus personne ne sait refaire |
| **L'absence de fenêtre** | Le service ne peut pas s'arrêter assez longtemps |
| **La perte de connaissance** | Personne ne sait plus exactement ce que fait le composant |

⚠️ **La cinquième est rarement avouée, et elle explique beaucoup de situations.** Un système qu'on ne comprend plus ne se remplace pas : on l'entoure.

#### 4.2 Les couches historiques, et comment on les reconnaît

🖼 **SCHÉMA 4.1 — Les strates d'un système d'information** · *Coupe géologique : quatre strates superposées, chacune datée, avec les composants caractéristiques.*

```
  ┌─────────────────────────────────────────────────────────┐
  │  STRATE 4 — 2018 →     Cloud, conteneurs, services      │
  │                        en ligne, interfaces applicatives│
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 3 — 2005-2018  Virtualisation, web interne,     │
  │                        annuaire unifié, mobilité        │
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 2 — 1995-2005  Client-serveur, bases            │
  │                        relationnelles, réseau local     │
  ├─────────────────────────────────────────────────────────┤
  │  STRATE 1 — avant 1995 Applications centralisées,       │
  │                        terminaux, traitements par lots  │
  └─────────────────────────────────────────────────────────┘
       Les quatre coexistent dans la plupart des organisations.
```

**Les signes de reconnaissance sur un schéma** :

| Signe | Strate probable | Ce qu'il implique |
|---|---|---|
| Un traitement nocturne, en lot | 1 ou 2 | Une fenêtre à respecter, un ordre à ne pas casser |
| Un serveur avec un nom de personne ou de planète | 2 | Antérieur aux conventions de nommage |
| Un client lourd installé sur les postes | 2 | Une migration de poste devient un projet applicatif |
| Une base au format ancien | 2 | Souvent le point de blocage d'une modernisation |
| Une machine virtuelle qui n'a jamais redémarré depuis des années | 3 | Personne n'ose |
| Un composant unique sans redondance au milieu d'un ensemble redondé | 2 ou 3 | Il n'a pas été inclus dans la modernisation |
| Une passerelle entre deux zones qui ne devraient pas communiquer | Toutes | **Le résultat d'un besoin urgent, jamais reconsidéré** |
| Une interface applicative « v1 » toujours en service à côté d'une « v3 » | 4 | Des clients n'ont pas migré |

**La dernière ligne du tableau est la plus instructive** : une passerelle inexplicable est presque toujours l'empreinte d'une urgence ancienne. Quelqu'un avait besoin que deux choses communiquent, vite. La solution devait être provisoire. Elle a douze ans.

🔭 **À RECONNAÎTRE — architectures centralisées historiques**

**① Pourquoi ce bloc existe.** Un cours d'architecture ne doit pas laisser croire que tout système d'information réel se compose de machines virtuelles, de conteneurs et de services en ligne. **Ce n'est pas le cas.**

> **Vous rencontrerez encore des architectures centralisées autour de systèmes de type mainframe, particulièrement dans certains grands systèmes d'information historiques et dans les secteurs fortement transactionnels** — banque, assurance, transport, administration.

**② Ce qu'il faut en savoir.** Le modèle est différent de tout ce que ce cours décrit : un système central très puissant, des traitements par lots, une fiabilité et une capacité transactionnelle qui restent difficiles à égaler, et un écosystème logiciel accumulé sur des décennies.

**③ Ce qu'il ne faut surtout pas en conclure.**

| Ce qu'un débutant pense | Ce qu'un praticien sait |
|---|---|
| « C'est ancien, donc dépassé » | **Ancien ne veut dire ni inutile, ni mauvais, ni non critique** |
| « Il faudrait migrer » | Cela a été étudié · le coût, le risque et l'absence de fenêtre l'ont écarté — §4.1 |
| « Personne ne sait plus le faire tourner » | Parfois vrai, et c'est précisément l'argument **contre** une migration précipitée |

**④ Ce que cela change en lecture.** Sur un schéma, il apparaît généralement comme une boîte à part, reliée au reste par un nombre restreint de flux — souvent des échanges de fichiers nocturnes, ou une passerelle applicative. **Ces flux sont exactement le genre de dépendance que le §29.5 apprend à chercher.**

**⑤ En réunion** : *« ça vient du mainframe »* → **par quel flux, à quelle fréquence, et que se passe-t-il si l'échange nocturne échoue ?**

⚠️ **Ce bloc est le prolongement direct de ce chapitre** : une strate ancienne n'est pas une erreur. C'est une décision, prise et reconduite, dont il faut connaître la raison avant de la juger.

#### 4.3 Les quatre événements qui sédimentent

| Événement | Ce qu'il laisse |
|---|---|
| **Une acquisition** | Un second annuaire, un second réseau, des conventions différentes, souvent un lien direct « temporaire » |
| **Une migration inachevée** | Deux systèmes qui font la même chose, dont un qu'on n'ose pas éteindre |
| **Une urgence** | Un contournement qui devient permanent |
| **Un départ** | Un composant que plus personne ne comprend |

**L'acquisition est le plus puissant des quatre.** Elle ajoute d'un coup une architecture entière, conçue ailleurs, avec d'autres arbitrages — et la fusion complète n'est presque jamais menée à son terme.

🏭 **TROIS TAILLES — la sédimentation**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Âge du système | 12 ans | 24 ans | 40 ans, par accumulation |
| Strates coexistantes | 2 | 3 | **4** |
| Acquisitions absorbées | 0 | 1 (2019) | **7** |
| Annuaires | 1 | 1, plus un hérité | **4 forêts** |

⚠️ **Application du principe de la contrainte** : Novaris n'a pas quatre forêts d'annuaire *parce qu'elle compte douze mille salariés*. Elle en a quatre **parce qu'elle a absorbé sept sociétés en quinze ans et que trois fusions d'annuaire ont été arbitrées comme trop risquées**. Une organisation de même taille née d'une croissance interne en aurait une seule.

#### 4.4 Comment on lit une architecture sédimentée

**La méthode**, en trois questions :

```
1. Qu'est-ce qui ne ressemble pas au reste ?
   → conventions de nommage, technologies, positionnement

2. Qu'est-ce qui devrait être là et n'y est pas ?
   → une redondance absente au milieu d'un ensemble redondé

3. Qu'est-ce qui relie deux choses qui ne devraient pas être reliées ?
   → une passerelle, un flux transverse, un compte partagé
```

**Chacune de ces anomalies a une date**, et retrouver cette date explique l'architecture mieux que n'importe quel document.

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous arrivez dans une organisation. Le schéma comporte une passerelle directe entre la zone bureautique et le réseau industriel, ce qui contredit toutes les bonnes pratiques. Que faites-vous ?*
**Vous demandez sa date et son motif avant de la critiquer.** Dans la majorité des cas, elle répond à un besoin réel — un export de données de production vers un outil de gestion — décidé un jour où il fallait aller vite. La mauvaise décision évitée : **proposer sa suppression en réunion sans savoir ce qu'elle porte**, se voir opposer un usage métier qu'on ignorait, et perdre la crédibilité nécessaire pour obtenir la vraie correction — qui est souvent de remplacer le flux, pas de le couper.

#### 4.5 📌 Ce que la sédimentation n'excuse pas

Le chapitre pourrait produire un excès inverse : tout expliquer par l'histoire et ne rien remettre en cause.

| La sédimentation explique | Elle n'excuse pas |
|---|---|
| Qu'un composant ancien existe | Qu'on ne sache pas ce qu'il fait |
| Qu'une passerelle ait été créée en urgence | Qu'elle ne soit pas documentée douze ans après |
| Qu'une migration soit inachevée | Qu'aucune décision n'ait été prise sur son achèvement |
| Qu'un annuaire hérité subsiste | Qu'on ignore qui y a des droits |

**La distinction** : la sédimentation explique **l'existence** d'un état ; elle n'explique jamais **l'absence de décision** à son sujet. C'est exactement la distinction que fait le volume Maintien en condition de sécurité entre un écart connu et décidé, et un écart ignoré.

#### 4.6 🔴 FIL ROUGE — décembre 2025 : pourquoi c'est « bizarre »

Amélie a relevé sur le schéma 1.1 trois éléments qui la gênent :

| Anomalie | Ce qu'elle en pense |
|---|---|
| Trois serveurs web, un seul applicatif | *« C'est incohérent »* |
| Une machine nommée `HERMES` au milieu de noms normalisés | *« Ils ont oublié de la renommer »* |
| Un lien direct entre le réseau bureautique et le site industriel | *« Ça ne devrait pas exister »* |

**Elle demande à Malik.** Les trois réponses sont datées.

| Anomalie | L'histoire | Ce que ça change |
|---|---|---|
| **Un seul applicatif** | En 2021, le passage à deux exemplaires a été chiffré. L'éditeur du progiciel facturait une seconde licence au prix de la première. **Arbitrage assumé, écrit, révisé chaque année** | Ce n'est pas une incohérence : c'est un compromis coût/disponibilité documenté |
| **`HERMES`** | Serveur de 2011, portant l'ancien outil de gestion de production. **Personne ne sait exactement ce qu'il fait encore.** Il reçoit un flux quotidien de l'usine | Ce n'est pas un oubli de nommage : c'est un composant que l'organisation n'a pas su remplacer |
| **Le lien bureautique-industriel** | Créé en 2018 pour un export de données de production vers le contrôle de gestion. Devait durer « le temps du projet » | Ce n'est pas une négligence : c'est une urgence de 2018 devenue permanente |

**Ce qu'Amélie comprend, et qu'elle note** :

> *Aucune des trois choses que je trouvais bizarres n'est une erreur. Deux sont des arbitrages, et une est une dette. Mais je ne pouvais pas faire la différence en regardant le schéma.*

**Le point que Malik ajoute**, et qui est le principe 2 du cours formulé par quelqu'un qui l'a vécu :

> *« Il n'y a jamais eu un moment où on a dessiné tout ça. On a ajouté des morceaux pendant vingt ans, chaque fois pour une bonne raison. Le résultat n'a été décidé par personne. »*

**Ce que cet épisode change pour la suite** : Amélie cesse de chercher les erreurs et commence à chercher **les dates**. C'est ce qui lui permettra, en février, de distinguer les cinq zones non couvertes de son inventaire — certaines sont des choix, d'autres des oublis, et la différence n'est visible que par l'histoire.

→ La suite en 🔴 §5.6, avec les zones.

#### Synthèse mentale du chapitre 4

Ce que vous regardez n'est pas une architecture mais un empilement de décisions prises à des époques différentes, par des gens différents, dont la plupart ne travaillent plus là. On ne refait pas propre pour cinq raisons, dont la moins avouée pèse lourd : un système qu'on ne comprend plus ne se remplace pas, on l'entoure. Quatre événements sédimentent — acquisition, migration inachevée, urgence, départ — et l'acquisition est le plus puissant, parce qu'elle ajoute d'un coup une architecture entière conçue ailleurs. Trois questions permettent de lire une architecture sédimentée : qu'est-ce qui ne ressemble pas au reste, qu'est-ce qui devrait être là et n'y est pas, qu'est-ce qui relie deux choses qui ne devraient pas l'être — et chaque anomalie a une date qui explique l'architecture mieux que n'importe quel document. Enfin, la sédimentation explique l'existence d'un état ; elle n'excuse jamais l'absence de décision à son sujet.

**Trois questions de vérification**

1. Un schéma comporte une passerelle qui contredit toutes les bonnes pratiques. Quelle est votre première question, et pourquoi pas votre première critique ?
2. Pourquoi « ils auraient dû refaire propre » est-il presque toujours un jugement naïf ?
3. Quelle est la différence entre ce que la sédimentation explique et ce qu'elle n'excuse pas ?

---

### Chapitre 5 — Les grandes zones

#### 5.1 Pourquoi on sépare

**Le principe**, et il est unique :

> **On sépare ce qui n'a pas le même niveau de confiance, ni les mêmes conséquences en cas de compromission.**

Le reste — les noms, les technologies, le nombre de zones — en découle largement.

**Ce qu'une séparation apporte, et ce qu'elle coûte** :

⚖️ **CONTRAINTE ET COÛT — la segmentation**

| Contrainte résolue | Coût introduit |
|---|---|
| Limiter la propagation d'une compromission | Des flux à ouvrir, documenter et maintenir |
| Contrôler ce qui traverse une frontière | Un dépannage plus difficile — « ça ne passe pas, mais où ? » |
| Appliquer des règles différentes par niveau de sensibilité | Une complexité qui croît avec le nombre de zones |
| Démontrer un cloisonnement en audit | **Un risque de contournement si les flux deviennent trop pénibles** |

⚠️ **Le dernier point est le plus mal anticipé** : une segmentation trop stricte produit des contournements — un compte partagé, un flux ouvert « temporairement », une machine à cheval sur deux zones. **Une zone contournée est pire qu'une zone absente**, parce qu'on croit qu'elle protège.

#### 5.2 Les six zones de référence

🖼 **SCHÉMA 5.1 — Les six zones** · *Bandes concentriques ou empilées, du moins fiable au plus sensible, avec les frontières marquées.*

```
   ╔═══════════════════════════════════════════════════════╗
   ║  EXTÉRIEUR — Internet, partenaires, mobilité          ║
   ║  Confiance : aucune                                   ║
   ╠═══════════════════════════════════════════════════════╣
   ║  BORDURE — pare-feu, accès distant, publication       ║
   ║  Rôle : filtrer, contrôler ce qui traverse            ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ZONE DÉMILITARISÉE — ce qui est exposé volontairement ║
   ║  Confiance : faible. Compromettable par conception    ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INTERNE — postes, serveurs métier, données           ║
   ║  Confiance : moyenne. C'est là qu'est la valeur       ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ADMINISTRATION — ce qui pilote tout le reste         ║
   ║  Confiance : maximale requise. **Rarement dessinée**  ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INDUSTRIEL / SPÉCIFIQUE — contraintes inversées      ║
   ║  Confiance : à part. Autres règles — chapitre 28      ║
   ╚═══════════════════════════════════════════════════════╝
```

| Zone | Ce qu'on y trouve | Ce qui la caractérise |
|---|---|---|
| **Extérieur** | Ce qu'on ne maîtrise pas | Aucune confiance, aucune hypothèse |
| **Bordure** | Pare-feu, passerelles d'accès distant | **Exposée par conception** — chapitre 10 |
| **Zone démilitarisée** | Ce qui doit être joignable de l'extérieur | On suppose qu'elle **sera** compromise |
| **Interne** | Postes, serveurs, données | Le plus grand volume, la plus grande valeur |
| **Administration** | Postes d'administration, consoles, orchestration | **Sa compromission donne tout le reste** |
| **Industriel** | Automates, supervision | Priorités inversées — chapitre 28 |

**La zone d'administration est la plus importante et la moins dessinée.** C'est le chapitre 27, et c'est le principal angle mort des schémas.

#### 5.3 Ce qui définit une frontière

Une zone n'est pas définie par un trait sur un schéma, mais par **ce qui doit être traversé pour passer**.

| Type de frontière | Ce qui la matérialise | Force | Ce qui la contourne |
|---|---|---|---|
| **Physique** | Réseaux distincts, sans lien | Maximale — et rare | Un support amovible · un portable branché aux deux |
| **Filtrage** | Un pare-feu entre deux segments | Forte, si les règles sont fines | Une règle trop large · un chemin oublié |
| **Segmentation logique** | Des segments distincts, routés | Moyenne — dépend du routage | Une route ajoutée sans filtrage |
| **Applicative** | Un mandataire inverse, une passerelle | Forte sur un protocole, nulle sur les autres | Tout ce qui n'emprunte pas ce protocole |
| **Déclarative** | *« C'est la DMZ »*, sans mécanisme | **Nulle** | Rien à contourner |

⚠️ **La dernière ligne est le piège de lecture le plus fréquent.** Sur beaucoup de schémas, une zone est dessinée sans qu'aucun mécanisme ne la matérialise réellement. **La question à poser devant toute frontière** : *qu'est-ce qui empêche de passer ?*

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. La zone démilitarisée est matérialisée par des pare-feu en haut, mais **rien n'est dessiné entre elle et le réseau interne**. Soit la frontière existe et n'est pas représentée, soit elle n'existe pas. Le schéma ne permet pas de trancher — et c'est la question la plus importante qu'on puisse lui poser.

#### 5.4 Les composants à cheval

**Le cas le plus intéressant en lecture** : un composant qui appartient à deux zones.

| Exemple | Pourquoi il est à cheval | Ce que ça implique |
|---|---|---|
| Un mandataire inverse | Il reçoit de l'extérieur, appelle l'intérieur | **C'est sa fonction** — chapitre 12 |
| Un serveur de sauvegarde | Il atteint toutes les zones | Sa compromission donne accès à toutes les données |
| Un poste d'administration | Il pilote plusieurs zones | Chapitre 27 |
| Un serveur avec deux interfaces réseau | Souvent un contournement historique | **À interroger systématiquement** |
| Un poste portable d'intervenant | Il se branche successivement sur deux réseaux | **Un pont différé** — §28.5 |

**La règle de lecture** : tout composant à cheval sur deux zones est **soit une frontière assumée, soit une brèche**. Il n'y a pas de troisième possibilité, et la distinction se fait en demandant si c'était voulu.

⚠️ **Le cas de la sauvegarde mérite une remarque.** C'est le composant le plus transverse d'une architecture : il atteint tout, pour tout copier. **Sa compromission donne accès à l'ensemble des données de l'organisation, sans jamais toucher à un seul serveur de production.** Et il n'est presque jamais dans la zone d'administration.

🔭 **À RECONNAÎTRE — architectures de calcul intensif**

**① Ce que c'est.** Des architectures optimisées pour des **calculs massifs, souvent parallèles** : simulation, recherche, modélisation, apprentissage automatique à grande échelle.

**② Ce qui les rend différentes d'un système d'information de gestion** :

| | Système de gestion | Calcul intensif |
|---|---|---|
| Ce qui compte | Disponibilité, cohérence, sécurité | **Débit de calcul, interconnexion entre nœuds, débit de stockage** |
| L'unité de travail | Une transaction | **Un travail soumis, qui dure des heures ou des jours** |
| Le réseau | Relie des services | **Relie des nœuds qui calculent ensemble** — la latence entre eux est structurante |
| L'arrêt | Un incident | **Une file d'attente qui s'allonge** |

**③ Ce qu'il faut en retenir en architecture.** Une zone de calcul intensif obéit à d'autres priorités, comme le réseau industriel du §28.1 — **et pour les mêmes raisons de fond : ses contraintes ne sont pas celles du reste du système d'information.** Y appliquer les règles du système de gestion sans discernement produit les mêmes blocages.

**④ En réunion** : *« c'est sur le cluster de calcul »* → **une zone à part, avec ses propres règles. Qui l'administre ? Quels flux la relient au reste ?**

📚 **À approfondir ailleurs** : c'est un domaine à part entière, avec sa propre ingénierie.

#### 5.5 Combien de zones, et pourquoi

**La question qui revient en conception** : *faut-il six zones ?*

| Nombre de zones | Quand c'est justifié | Ce que ça coûte |
|---|---|---|
| **2** — interne, extérieur | Aucun service publié, aucun actif à part | Presque rien |
| **3** — + DMZ | Un service est publié | Deux jeux de règles |
| **4** — + administration | Il y a des administrateurs distincts des utilisateurs | Des postes dédiés |
| **5** — + industriel ou spécifique | Un environnement aux contraintes inversées | Une autonomie à construire |
| **6 et plus** | Des entités, des sensibilités ou des obligations distinctes | **Une complexité qui croît vite** |

⚠️ **Le principe de la contrainte s'applique intégralement** : le nombre de zones ne se déduit pas de la taille. **Il se déduit du nombre de niveaux de confiance réellement différents.** Une organisation de deux mille personnes avec un seul métier et aucun service publié peut légitimement n'avoir que trois zones.

🔥 **SCÉNARIO — la zone existe sur le schéma, pas sur le réseau**

| Question | Réponse |
|---|---|
| Symptôme | Un audit demande la preuve du cloisonnement. Le schéma montre trois zones |
| Hypothèse naïve | « Le schéma fait foi » |
| Dépendance réelle | **Aucun équipement ne filtre entre deux d'entre elles.** Elles sont routées, pas filtrées |
| Ce que le schéma aurait dû montrer | Ce qui matérialise chaque frontière |
| Comment le vérifier en dix minutes | Depuis une machine de la zone A, tenter de joindre une machine de la zone B |

⚠️ **Ce test est le plus rentable du chapitre**, et il ne demande aucun outil : **une connexion réussie entre deux zones censées être séparées vaut tous les schémas du monde.**

#### 5.6 🔴 FIL ROUGE — décembre 2025 : combien de zones ?

Amélie compte les zones du schéma 1.1 : trois — démilitarisée, interne, industriel.

**Elle vérifie auprès de Malik.** Il y en a **six**.

| Zone | Sur le schéma ? | Réalité |
|---|---|---|
| Extérieur | Implicite | — |
| Bordure | Les deux pare-feu | Correct |
| Zone démilitarisée | Oui | Correct |
| Interne | Oui | **En réalité trois segments** : serveurs, postes Lyon, postes Nantes |
| **Administration** | **Non** | Existe : un segment dédié, deux postes, un accès depuis Lyon uniquement |
| Industriel | Oui | Correct, mais **le lien de 2018 le traverse** |

**Deux découvertes.**

La zone interne du schéma en cache trois, dont deux sur des sites différents. Le schéma représente une frontière là où il y en a plusieurs.

La zone d'administration n'est pas dessinée **et elle est la plus sensible**. Amélie demande pourquoi.

> *« Parce que ce schéma, on le montre aux clients »*, répond Malik.

**Ce qu'Amélie note**, et qui est un principe de lecture à part entière :

> *Un schéma est fait pour quelqu'un. Celui-ci est fait pour rassurer un client. Il ne ment pas — il ne montre pas ce qui ne le regarde pas. Je dois savoir pour qui un schéma a été dessiné avant de le lire.*

→ La suite en 🔴 §6.6, avec les 620 postes qui ne sont sur aucun schéma.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans une autre zone » | Une séparation existe sur le schéma | **Qu'est-ce qui la matérialise ?** — §5.3 |
| « C'est cloisonné » | Idem | Testé depuis quand ? |
| « Le serveur a une patte dans les deux » | Deux interfaces réseau | **La frontière n'existe plus à cet endroit** |
| « La sauvegarde accède à tout » | Constat de fait | **C'est le composant le plus transverse — où est-il ?** |

---

### Chapitre 6 — Le poste utilisateur

> Placé ici, en Partie I, parce que c'est là que commence la majorité des flux et la majorité des incidents — et qu'il ne figure sur presque aucun schéma.

#### 6.1 Le grand absent

**Le réflexe de tout débutant** : *Internet → pare-feu → serveur*.

**La réalité, en volume** : dans une organisation ordinaire, la majorité écrasante des connexions part d'un poste **interne**, pas d'Internet. Et la majorité des compromissions y commence.

**Pourquoi il n'est jamais dessiné** :

| Raison | Effet |
|---|---|
| Il y en a des centaines | Les dessiner rendrait le schéma illisible |
| Ils sont considérés comme uniformes | **Ils ne le sont pas** — §6.3 |
| Ils appartiennent à un autre périmètre | Souvent gérés par une autre équipe |
| **Ils ne « produisent » rien** | Erreur : ils consomment tout, et ils accèdent à tout |

⚠️ **La conséquence de lecture** : sur un schéma sans poste, vous ne voyez ni le point de départ de la plupart des flux, ni la surface d'attaque principale. **C'est l'omission la plus lourde des schémas d'architecture.**

#### 6.2 Ce qu'un poste contient et ce qu'il ouvre

🖼 **SCHÉMA 6.1 — Ce qu'un poste atteint**

```
                        [ services en ligne ]
                                  ▲
   [ Internet ] ◄───────────  [ POSTE ]  ───────────► [ serveurs internes ]
                                  │  │                  fichiers · applicatifs
                    stockage      │  └──► [ annuaire ]   messagerie · bases
                    amovible ◄────┘        (dépendance)
```

| Ce qu'il contient | Ce que ça implique |
|---|---|
| Des identifiants en mémoire | Une compromission donne accès à ce que l'utilisateur atteint |
| Des documents locaux | Souvent une copie de données sensibles |
| **Des sessions ouvertes** | Vers des services en ligne, **sans nouvelle authentification** |
| Des accès enregistrés | Mots de passe du navigateur, clés, jetons — §33 |
| Des logiciels non maîtrisés | Extensions, outils installés par l'utilisateur |

**Ce qu'il ouvre** : tout ce que son utilisateur a le droit d'atteindre — et **le poste ne fait aucune distinction entre un accès légitime et un accès détourné**.

⚠️ **La ligne des sessions ouvertes est celle qu'on sous-estime le plus.** Un second facteur d'authentification protège la connexion ; il ne protège pas une session déjà ouverte. **Un poste compromis hérite de toutes les sessions actives**, sans avoir à s'authentifier nulle part.

#### 6.3 Les quatre types de postes

| Type | Où il est | Ce qui change |
|---|---|---|
| **Fixe interne** | Sur le réseau de l'organisation | Le cas de référence |
| **Nomade** | Partout | Il n'est plus derrière le pare-feu. **Il l'est parfois par un tunnel, parfois pas** |
| **Virtualisé** | Le poste est ailleurs, l'écran est ici | Les données ne quittent pas le centre. **Une dépendance forte au réseau** |
| **Non maîtrisé** | Poste personnel, poste de prestataire | **Le cas le plus mal traité** — §38.4 |

**Le poste nomade est celui qui casse le raisonnement en zones du chapitre 5.** Un poste hors des murs n'est plus dans la zone interne — mais il y accède.

🖼 **SCHÉMA 6.2 — Les deux chemins d'un poste nomade**

```
  A — TUNNEL COMPLET
      poste ══tunnel══► réseau interne ──► serveurs
                                       └─► Internet
      → tout le trafic remonte · les contrôles internes s'appliquent
      → le lien du siège porte tout le trafic Internet des nomades

  B — TUNNEL PARTIEL
      poste ══tunnel══► réseau interne ──► serveurs internes
      poste ──────────────────────────────► Internet (direct)
      → moins de charge sur le lien
      → ⚠️ le trafic Internet du poste n'est plus filtré ni journalisé
      → le poste est simultanément dans DEUX réseaux
```

⚠️ **Le mode B crée une situation que le chapitre 5 interdirait sur un serveur** : le poste est simultanément connecté au réseau interne et à Internet, **sans qu'aucun équipement ne s'interpose**. C'est un composant à cheval — §5.4 — et il y en a des centaines.

**La question à poser devant tout schéma** : *les postes nomades passent-ils par le même chemin que les postes internes ?*

🏭 **TROIS TAILLES — les postes**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Nombre | 35 | 620 | ≈ 11 000 |
| Nomades | 3 | 180 | ≈ 4 000 |
| Postes non maîtrisés | **Oui** — le gérant utilise son portable personnel | Prestataires, encadré | Encadré, avec accès dédié |
| Poste virtualisé | Non | Pour les prestataires uniquement | Pour plusieurs métiers |

⚠️ **Principe de la contrainte** : Atelier Martin n'a pas de poste virtualisé *parce qu'elle est petite* — elle n'en a pas **parce qu'aucune contrainte ne le justifie** : pas de prestataire distant, pas de données à confiner, pas de parc hétérogène à uniformiser. Une entreprise de 35 personnes avec des sous-traitants dans trois pays en aurait un.

#### 6.4 Le poste dans les flux

Reprenons les trois familles du principe des trois flux, du point de vue du poste.

| Famille | Ce qui part du poste |
|---|---|
| **Métier** | Requêtes web, ouverture de fichiers, messagerie, impression |
| **Dépendance** | Résolution de noms · authentification à l'ouverture de session · validation de certificats · **obtention d'une adresse au démarrage** |
| **Exploitation** | Remontée d'inventaire · télémétrie de sécurité · télédistribution de logiciels · sauvegarde éventuelle |

**Le flux de dépendance le plus méconnu** : à l'ouverture de session, un poste interne interroge l'annuaire, applique des politiques, monte des lecteurs réseau, synchronise son horloge. **Si l'un de ces éléments manque, l'utilisateur constate un poste « lent » ou « bloqué »** — et le diagnostic est difficile parce qu'aucun de ces flux n'est sur le schéma.

🔥 **SCÉNARIO — l'ouverture de session prend cinq minutes**

| Question | Réponse |
|---|---|
| Symptôme | Les sessions s'ouvrent, très lentement. Uniquement sur un site |
| Hypothèse naïve | « Les postes sont vieux » |
| Dépendance réelle | **Un des flux d'ouverture attend l'expiration d'un délai** : un lecteur réseau injoignable, un contrôleur d'annuaire distant, une politique qui référence un serveur disparu |
| Ce que le schéma aurait dû montrer | Ce que fait un poste au démarrage — **jamais représenté** |
| Comment le reconnaître | **Une lenteur constante, à la seconde près, est un délai d'attente, pas une charge** |

⚠️ **Un indice de diagnostic utile, et rien de plus** : une lenteur **qui varie** oriente vers une question de charge · une lenteur **constante et reproductible, à la seconde près**, oriente vers un délai d'attente sur quelque chose d'injoignable.

📌 **Ce n'est pas une loi.** Une lenteur constante peut aussi venir d'un traitement systématiquement coûteux, d'une résolution de noms lente mais réussie, ou d'un chiffrement mal négocié. **C'est une piste à explorer en premier, pas une conclusion.**

#### 6.5 🔬 Mini-lab 3 — Où commence le flux ?

**Objectif** — Reconstituer le point de départ réel des flux d'une organisation.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §6.1 à §6.4

**La situation** : une organisation de 400 personnes. Un incident est survenu — un rançongiciel a chiffré un serveur de fichiers. Le schéma d'architecture montre : Internet → pare-feu → zone démilitarisée → serveurs internes → serveur de fichiers.

❓ **Questions**
1. En regardant ce schéma, par où l'attaquant est-il entré ?
2. Qu'est-ce que le schéma ne permet pas d'envisager ?
3. Quelle est l'hypothèse la plus probable, statistiquement ?

---

**Corrigé**

**1.** Le schéma suggère une entrée par Internet, via la zone démilitarisée. C'est la seule voie qu'il représente.

**2.** Il ne permet pas d'envisager **le poste utilisateur**, qui n'y figure pas. Ni le poste nomade, ni le prestataire, ni le stockage amovible, ni la messagerie ouverte sur un poste.

**3.** L'hypothèse la plus probable est **le poste** : pièce jointe ouverte, identifiants dérobés, session détournée. Le serveur de fichiers a été atteint **avec des droits légitimes**, depuis l'intérieur.

**La leçon** : *un schéma qui ne montre pas les postes oriente le diagnostic vers la mauvaise hypothèse.* Ce n'est pas un défaut du dessin — c'est un défaut de lecture, si le lecteur oublie ce qui n'est pas dessiné.

#### 6.6 🔴 FIL ROUGE — décembre 2025 : 620 postes invisibles

Amélie demande à Malik où sont les postes sur le schéma 1.1.

> *« Ils ne sont pas dessinés. Il y en a 620, ça n'aurait pas de sens. »*

**Elle pose alors trois questions**, et les réponses la surprennent :

| Question | Réponse |
|---|---|
| Combien de postes nomades ? | **180** — un tiers du parc |
| Comment reviennent-ils sur le réseau interne ? | Par un tunnel, vers la passerelle d'accès distant — **qui n'est pas sur le schéma non plus** |
| Y a-t-il des postes non maîtrisés ? | **Oui** — ceux des prestataires de l'infogérant, qui administrent les serveurs |

**La troisième réponse est celle qui compte.** Des postes qu'HELIOMED ne maîtrise pas ont un accès d'administration à ses serveurs. Ils ne figurent sur aucun schéma, dans aucun inventaire, et personne n'en connaît le nombre.

⚠️ **Et le tunnel de la deuxième réponse pose une question qu'Amélie ne sait pas encore formuler** : complet ou partiel ? — §6.3. Personne, chez HELIOMED, ne connaît la réponse en décembre 2025.

**Ce qu'Amélie note** :

> *Le schéma montre ce qui est à nous. Il ne montre ni ce qui vient de l'extérieur, ni ce qui appartient à d'autres — alors que c'est par là que passent les accès les plus puissants.*

**Ce que cet épisode annonce** : la question des postes de prestataires reviendra en septembre 2029 dans le volume Renseignement, quand un prestataire compromis fera l'objet d'une évaluation — et en mai 2030, quand un compte de prestataire de 2028, toujours actif, sera découvert dans une fuite.

→ La suite en 🔴 §7.5, avec la question qu'Amélie finit par poser à Claire.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « L'utilisateur a cliqué » | Un poste est peut-être compromis | **Ce qui compte n'est pas le clic, c'est ce que ce poste atteint** |
| « Ils sont en télétravail » | Postes nomades | **Tunnel complet ou partiel ?** — §6.3 |
| « C'est un poste perso » | Poste non maîtrisé | **Qu'atteint-il ? Avec quels droits ?** |
| « Le poste rame » | Lenteur | **Constante ou variable ?** La réponse oriente la recherche — elle ne la conclut pas |

---

### Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur

#### 7.1 Deux métiers, deux temporalités

| | **L'architecte** | **Le lecteur** |
|---|---|---|
| Quand | **Avant** — au moment de décider | **Après** — sur ce qui existe |
| Son objet | Un système qui n'existe pas encore | Un système qui existe et qu'il n'a pas conçu |
| Sa contrainte | Choisir sous incertitude | Comprendre sans documentation |
| Son livrable | Une décision et ses justifications | Une compréhension, et des questions |
| Son erreur type | Optimiser une contrainte au détriment des autres | **Juger sans connaître l'histoire** |

**Ce cours forme d'abord le second, puis le premier.** L'ordre n'est pas négociable : on ne peut concevoir que ce qu'on sait lire.

#### 7.2 Ce qu'un lecteur peut décider

Contrairement à une idée répandue, **lire une architecture permet de décider beaucoup**, sans être architecte.

| Décision | Ce que la lecture apporte |
|---|---|
| Où placer un dispositif de sécurité | Les points de passage réels — chapitre 44 |
| Si une vulnérabilité nous concerne | L'exposition du composant affecté |
| Ce qu'on peut isoler pendant un incident | Les dépendances — chapitre 35 |
| Ce qu'on peut arrêter pour une maintenance | Ce qui tombe avec |
| Ce qu'il faut inventorier en priorité | Les points de rupture |
| Si une demande de flux est légitime | Ce qu'elle traverse |
| Ce qu'il faut journaliser | Les points de passage |

**Sept décisions, aucune ne nécessite d'être architecte.** C'est la valeur pratique de ce cours pour la majorité de ses lecteurs.

#### 7.3 Ce que ce cours ne rendra pas capable de faire

Par honnêteté, et pour que la Partie IX soit lue avec les bonnes attentes.

| Hors de portée | Pourquoi |
|---|---|
| Dimensionner une infrastructure | Exige des mesures, des essais, une expérience produit |
| Choisir entre deux produits | Dépend du contexte, des contrats, des compétences |
| Concevoir un système à forte contrainte | Haute disponibilité stricte, temps réel, très grande échelle |
| Garantir qu'une architecture fonctionnera | Seul l'essai le démontre |

**Ce que la Partie IX apporte réellement** :

> Poser les bonnes questions, proposer une architecture justifiée pour un besoin courant, énoncer ses compromis — et identifier ce qu'il reste à vérifier.

⚠️ **Le lecteur qui terminera ce cours en pensant *« je sais concevoir une architecture »* l'aura mal lu.** Celui qui le terminera en pensant *« je sais quoi demander, quoi proposer, et quoi vérifier »* en aura tiré l'essentiel.

#### 7.4 Comment progresser après ce cours

| Étape | Comment |
|---|---|
| **Lire des architectures réelles** | Demander les schémas de votre organisation, et poser les questions du chapitre 36 |
| **Suivre un flux de bout en bout** | Une fois, en vrai, avec l'exploitation. C'est irremplaçable |
| **Assister à une revue d'architecture** | Écouter les arbitrages se faire |
| **Reconstituer une histoire** | Demander à quelqu'un d'ancien pourquoi un composant est là |
| **Dessiner** | Le chapitre 50 en fait un exercice |

**La deuxième ligne est celle qui fait la différence.** Suivre une requête réelle, de la frappe au clavier jusqu'à l'écriture en base, en observant chaque étape, enseigne en une journée ce qu'aucun cours ne transmet.

#### 7.5 🔴 FIL ROUGE — décembre 2025 : la question d'Amélie

Le 19 décembre, Amélie rend compte à Claire Nadeau de ses deux semaines. Elle n'a rien inventorié.

**Ce qu'elle a produit** : une liste de vingt-trois questions, et une observation.

**L'observation** :

> *Le schéma qu'on m'a donné date de mars 2023, il ne mentionne pas le site de Nantes, il ne montre ni les postes, ni la zone d'administration, ni les services en ligne, ni les prestataires. Il n'est pas faux. Il a été fait pour montrer à un client que nous avons une zone démilitarisée.*

**La question qu'elle pose à Claire** :

> *« Est-ce que tu veux que je compte ce qui est sur le schéma, ou que je découvre ce qui existe ? »*

**La réponse de Claire**, qui ouvre le volume suivant :

> *« Les deux. Mais dans cet ordre-là : d'abord comprendre, ensuite compter. Sinon tu vas compter des choses dont tu ne sauras pas si elles comptent. »*

**Ce qui est décidé le 19 décembre** : Amélie consacre janvier à comprendre le système avant de l'inventorier. Sa mission d'inventaire démarre officiellement le 5 janvier 2026.

**Le 11 décembre, Sonia Weber avait demandé** : *« Bon. Combien on en a, alors ? »* — et Claire avait répondu qu'elle ne pouvait pas encore le dire.

**Le 19 décembre, la raison est claire.** Ce n'est pas un problème de comptage. C'est un problème de compréhension, puis de définition.

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> ✓ que **toute architecture est un compromis** entre six contraintes qui se contredisent — et que la sixième, l'histoire, est souvent la plus puissante ;
> ✓ distinguer **trois familles de flux** — métier, dépendance, exploitation — et savoir que la confusion entre les deux dernières fait surdimensionner ce qui n'en a pas besoin ;
> ✓ poser les **quatre questions du lecteur** devant n'importe quel schéma ;
> ✓ que **trois mots** — serveur, application, service — désignent chacun au moins trois choses, et quelle question les désambiguïse ;
> ✓ qu'une **boîte** peut représenter cinq choses et un **trait** cinq autres, et quelles questions poser à chacun ;
> ✓ que quatre **vues** sont nécessaires, et qu'aucune ne ment ;
> ✓ **onze éléments qui ne sont jamais dessinés**, et l'effet de leur absence ;
> ✓ qu'une architecture est un **empilement daté**, et que chaque anomalie a une histoire qu'il faut demander avant de critiquer ;
> ✓ que la **taille ne justifie jamais une brique** — la contrainte, oui ;
> ✓ qu'une **zone** se définit par ce qu'il faut traverser, pas par un trait ;
> ✓ que le **poste utilisateur** est le point de départ de la plupart des flux et le grand absent des schémas ;
> ✓ qu'un schéma est toujours **fait pour quelqu'un**, et qu'il faut savoir pour qui avant de le lire.
>
> **Ce que vous ne savez pas encore** : à quoi servent les composants que vous avez appris à repérer, ce qui se passe quand ils disparaissent, et à partir de quelle contrainte ils deviennent nécessaires. C'est l'objet de la Partie II.

---


## Registre de cohérence — fin de T1 (chapitres 1 à 7)

### Règles verrouillées, et leur application

| Règle | Application en T1 |
|---|---|
| **principe des trois flux — trois familles de flux** | Introduite §1.5, tableau des protocoles §2.4, appliquée §6.4 |
| **R2 — la taille ne justifie pas** | Énoncée §1.6 avec trois formulations interdites, appliquée §4.3 et §6.3 |
| **R3 — profondeur limitée** | §2.2 : liste des notions volontairement exclues |
| **R4 — coût d'une brique** | Principe 9, appliqué §5.1 sur la segmentation |
| **R5 — le schéma porte l'information** | 7 schémas ASCII en 7 chapitres, ratio texte/représentation tenu |

### Termes arrêtés

| Terme retenu | Écarté |
|---|---|
| **Flux métier / de dépendance / d'exploitation** | « flux de contrôle » (trop large — voir principe des trois flux) |
| **Mandataire inverse** / **mandataire sortant** | « proxy » seul (ambigu) |
| **Point de rupture** | « SPOF » (sigle, une seule mention) |
| **Zone démilitarisée** | — (terme conservé, avec réserve §5.2) |
| **Résolution de noms** | « DNS » (cité, non employé comme terme du cours) |
| **Poste d'administration** | « bastion » (terme du terrain) |
| **Sédimentation** | « dette technique » (notion voisine, plus étroite) |

### Renvois émis vers des chapitres non rédigés

§1.1→50 · §1.3→43-45 · §1.5→29-35 · §2.1→35 · §2.3→12, 14, 25, 27 · §3.4→6, 27, 38, 50 · §4.5→volume MCS · §5.2→10, 27, 28 · §6.3→38 · §7.2→35, 44

### État du fil rouge

| Élément | Valeur figée |
|---|---|
| Épisodes | §1.8 (15/12/2025) · §2.6 · §3.7 · §4.6 · §5.5 · §6.6 · §7.5 (19/12/2025) |
| Personnages | Amélie Roux (administratrice système, Nantes, 4 ans d'ancienneté) · Claire Nadeau (RSSI) · Malik Ferhaoui (exploitation) · Sonia Weber (DSI) |
| Chiffres figés | 96 / 71 / 118 serveurs · 620 postes dont 180 nomades · schéma daté de mars 2023 · 3 sites · lien bureautique-industriel créé en 2018 · serveur `HERMES` de 2011 · second exemplaire applicatif refusé en 2021 pour cause de licence · 23 questions produites |
| Dates figées | 15/12/2025 proposition · 19/12/2025 point avec Claire · 05/01/2026 démarrage officiel |
| Raccordement | §7.5 se raccorde au §1.10 du volume Asset Management (réunion du 11/12/2025 et démarrage du 05/01/2026) |
| Prochain épisode | Partie II — les composants, un par un |

### Écarts au plan validé

**Aucun écart de structure.** Deux précisions :

1. **Le mini-lab 1 a été placé au chapitre 2** plutôt qu'au chapitre 3, parce que l'ambiguïté de vocabulaire se travaille avant la lecture de schéma. Le lab 2 est au chapitre 3, le lab 3 au chapitre 6. La numérotation des quinze labs reste conforme.
2. **Le §5.5 introduit un principe de lecture non prévu** — *un schéma est fait pour quelqu'un* — qui prolonge le chapitre 3 et annonce le chapitre 50. À réutiliser en Partie VI.

---
