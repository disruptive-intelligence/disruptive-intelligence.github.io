---
title: Chapitre 1 — Pourquoi un système d'information ressemble à ça
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

## 1.1 Le schéma que vous ne comprenez pas encore

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

## 1.2 Ce que ce cours n'est pas

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

## 1.3 Les quatre questions du lecteur

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

## 1.4 Les six contraintes qui produisent toute architecture

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

### Ce que la contradiction produit concrètement

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

## 1.5 Les trois familles de flux

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

## 1.6 Les trois architectures de référence

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

## 1.7 La doctrine — neuf principes

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

## 1.8 La phrase fondatrice

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

## Synthèse mentale du chapitre 1

Toute architecture est un compromis : elle n'a pas été conçue, elle a été négociée entre six contraintes qui se contredisent deux à deux — disponibilité, performance, coût, sécurité, conformité, et l'histoire, qu'on oublie et qui est souvent la plus puissante. Trois arbitrages différents produisent trois architectures différentes pour un même besoin, et aucune n'est meilleure : chacune serait une erreur dans le contexte des deux autres. Quatre questions structurent la lecture, et la première échoue le plus souvent parce que personne n'enseigne que trois choses différentes circulent : le flux métier, dessiné · le flux de dépendance, rarement dessiné et dont la rupture arrête le service · le flux d'exploitation, presque jamais dessiné et dont la rupture rend aveugle sans arrêter le service. Confondre les deux derniers conduit à surdimensionner ce qui n'en a pas besoin. Enfin, la taille d'une organisation ne justifie jamais un composant : la contrainte, oui — et ajouter n'est jamais gratuit.

**Trois questions de vérification**

1. Un même besoin peut produire trois architectures différentes. Qu'est-ce qui les distingue, et laquelle est la meilleure ?
2. La collecte de journaux s'interrompt. Le service s'arrête-t-il ? À quelle famille de flux appartient-elle, et pourquoi la distinction compte-t-elle ?
3. Sur un schéma, un annuaire est dessiné sans aucun trait de connexion. Est-ce une erreur ? Que cela vous apprend-il sur les schémas en général ?

→ **Chapitre 2 — Le vocabulaire** : trois personnes emploient le mot « serveur », et désignent trois choses différentes.

---
