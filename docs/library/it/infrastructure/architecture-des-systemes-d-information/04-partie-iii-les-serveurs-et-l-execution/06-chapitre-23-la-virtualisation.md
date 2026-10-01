---
title: Chapitre 23 — La virtualisation
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

## 23.1 À quoi ça sert

Faire tourner plusieurs machines logiques sur une machine physique, et les déplacer entre machines physiques.

**Pourquoi ça existe.** Un serveur physique dédié à une application utilise une fraction de sa capacité. La virtualisation densifie — et, accessoirement, elle rend une machine **déplaçable**, ce qui change complètement la gestion des pannes matérielles.

## 23.2 Les quatre objets à distinguer

**C'est la distinction qui manque dans la plupart des schémas.**

| Objet | Ce que c'est | Ce qui se passe s'il tombe |
|---|---|---|
| **L'hôte** | La machine physique | Ses machines s'arrêtent, **ou basculent si le mécanisme existe et fonctionne** |
| **Le stockage partagé** | Où résident les disques des machines | **Tout s'arrête** — c'est le point de rupture réel de la plupart des plateformes |
| **Le réseau de la plateforme** | Ce qui relie hôtes et stockage | Les machines perdent leurs disques — effet identique |
| **Le plan de gestion** | La console qui pilote l'ensemble | Rien immédiatement · **on ne peut plus rien administrer, ni créer, ni basculer** |

⚠️ **Le stockage partagé est un point de rupture rarement dessiné, et aux conséquences très larges.** Dix hôtes redondés, quarante machines réparties, **un seul stockage** : c'est une configuration très répandue, et son point de rupture est l'objet qui ne figure sur aucun schéma logique.

## 23.3 La redondance qui n'en est pas

🖼 **SCHÉMA 23.1 — Ce que le schéma logique cache**

```
   CE QUE LE SCHÉMA MONTRE          LA RÉALITÉ PHYSIQUE

      [web 1] [web 2] [web 3]         ┌──── HÔTE A ────┐
           redondés                   │ web1 web2 web3 │
                                      └────────────────┘
                                      L'hôte tombe : les trois tombent.
```


**Les quatre questions à poser devant toute redondance**, et elles découlent du principe de preuve :

```
1. Les exemplaires sont-ils sur des HÔTES différents ?
2. Ces hôtes utilisent-ils le MÊME STOCKAGE ?
3. Sont-ils dans la même BAIE, sur la même ALIMENTATION ?
4. Sont-ils sur le MÊME SITE ?
```


⚠️ **Une réponse « non » à la question 1 suffit à annuler la redondance.** Une réponse « oui » aux trois suivantes la réduit à une protection contre la seule panne d'hôte — ce qui est déjà utile, mais bien moins que ce que le schéma laisse croire.

📌 **Il existe des mécanismes qui empêchent deux machines d'un même rôle de se retrouver sur le même hôte.** Ils sont efficaces, et **ils doivent être configurés** : par défaut, la plateforme place où elle veut.

🔭 **À RECONNAÎTRE — VDI et publication d'applications**

**① Qu'est-ce que c'est.** *Virtual Desktop Infrastructure* — le poste de travail ne s'exécute plus devant l'utilisateur, mais dans le centre de données. **L'utilisateur n'a plus qu'un écran, un clavier et une session distante.**

**② Quel problème il résout.** Les données ne quittent pas le centre · un poste perdu ne contient rien · les prestataires distants travaillent sans qu'on leur confie quoi que ce soit · un parc hétérogène devient uniforme.

**③ Ce que cela change au raisonnement.**

```
   POSTE CLASSIQUE
      [ utilisateur ] ──► [ son poste ] ──► application

   VDI
      [ terminal ] ──session distante──► [ poste centralisé ] ──► application
           │                                      │
      ne contient rien              c'est ICI que tout s'exécute
```


> **La question que le VDI oblige à poser, et qui vaut au-delà de lui** : *où s'exécute réellement l'application ?*

⚠️ **Deux variantes à distinguer** : on peut publier **un poste complet** — l'utilisateur voit un bureau — ou **une application seule**, qui apparaît dans son environnement habituel. **Citrix** est le nom historique et majeur de cet écosystème ; vous l'entendrez employé comme synonyme de la fonction elle-même.

**④ Les dépendances que cela crée.**

| Nouvelle dépendance | Effet |
|---|---|
| **Le réseau** | Une coupure ne ralentit plus le travail : **elle l'arrête** |
| **La plateforme centrale** | Une panne affecte tous les utilisateurs simultanément |
| **Le service de courtage de session** | Composant peu connu, et point de rupture réel |
| L'impression, les périphériques | Chaque redirection est une intégration à maintenir |

⚠️ **Le renversement le plus important** : dans un parc classique, une panne réseau dégrade le travail. **En VDI, elle l'interrompt totalement** — le poste de l'utilisateur n'est plus chez lui.

**⑤ Le coût.** Une infrastructure centrale dimensionnée pour tous les utilisateurs simultanés · une expérience dégradée sur les usages graphiques ou latents · **une concentration du risque** · une compétence spécialisée.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « Ils sont en VDI » | **Poste complet ou application publiée ?** |
| « Les prestas passent par Citrix » | Bon modèle — §6.3, poste non maîtrisé | **Que peuvent-ils faire depuis la session ?** |
| « Le VDI rame » | Réseau · plateforme · stockage · trois causes distinctes |

---

🔭 **À RECONNAÎTRE — hyperconvergence**

**① Qu'est-ce que c'est.** Une architecture où **le calcul et le stockage sont réunis dans des nœuds standardisés**, pilotés comme un ensemble par une couche logicielle.

**② Quel problème elle résout.** L'architecture classique sépare les deux, avec un réseau de stockage dédié entre les deux — §23.4. Cela fonctionne, et cela demande trois compétences distinctes et trois équipes.

**③ Ce que cela change.**

```
   ARCHITECTURE CLASSIQUE
      [ serveurs ] ═══ réseau de stockage ═══ [ baie ]
      → trois éléments · trois compétences · trois contrats

   HYPERCONVERGENCE
      [ nœud : calcul + stockage ]
      [ nœud : calcul + stockage ]   ──► cluster piloté par logiciel
      [ nœud : calcul + stockage ]
      → un seul élément · une seule compétence · on ajoute un nœud pour croître
```


⚠️ **④ Le point qui compte, et il est contre-intuitif** :

> **La simplification physique déplace la complexité dans le logiciel.**

Il n'y a plus de baie à administrer — **il y a une couche de stockage distribuée**, avec ses règles de réplication, son quorum, et ses comportements en cas de perte de nœuds. Le point de rupture n'a pas disparu, **il a changé de nature**.

**⑤ Le coût.** Une croissance par blocs — on ajoute calcul et stockage ensemble, même si l'on n'a besoin que de l'un · une dépendance forte à un fournisseur · **une compétence sur le comportement distribué**, pas sur du matériel.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est en HCI » | **Combien de nœuds ? Combien peut-on en perdre ?** — voir le quorum, §23.6 |
| « On n'a plus de SAN » | Le stockage est distribué sur les nœuds. **Avec quelle réplication ?** |
| « On ajoute un nœud pour du stockage » | On ajoute aussi du calcul, et on le paie |

## 23.4 Le stockage — bloc, fichier, objet

> **Le composant le plus présent sur les schémas d'infrastructure et le moins compris.** Il est aussi le point de rupture caché de la plupart des plateformes de virtualisation — §23.2.

### Les trois familles

```
  BLOC       « Voici un disque. Débrouille-toi. »
             Le serveur voit un volume brut, il y installe son système
             de fichiers. Utilisé par : machines virtuelles, bases de données.

  FICHIER    « Voici un dossier partagé. »
             Plusieurs serveurs montent le même partage et y lisent
             et écrivent des fichiers. Utilisé par : partages bureautiques,
             données applicatives partagées.

  OBJET      « Voici une adresse. Dépose ton fichier, récupère-le par son nom. »
             Pas de système de fichiers, pas de montage. On dépose et on lit
             par une interface applicative. Utilisé par : sauvegardes,
             archives, contenus web, données massives.
```


| | **Bloc** | **Fichier** | **Objet** |
|---|---|---|---|
| Ce que le serveur voit | Un disque | Un dossier réseau | **Rien — une adresse à appeler** |
| Plusieurs serveurs simultanément | Difficile | **Oui, c'est son objet** | Oui |
| Modification partielle d'un contenu | Oui | Oui | **Non — on remplace l'objet entier** |
| Sur un schéma | Un lien vers une baie | Un serveur de fichiers | **Souvent un nuage, ou rien** |
| Qui l'utilise typiquement | Virtualisation, bases | Postes, applications partagées | Sauvegardes, archives, web |

⚠️ **La ligne « modification partielle » explique la plupart des choix.** Une base de données réécrit constamment de petits fragments : elle a besoin de **bloc**. Une archive s'écrit une fois et se relit : **objet** convient, et coûte bien moins cher.

### Les architectures de stockage sur un schéma

```
  A — STOCKAGE LOCAL
      [ serveur ] avec ses disques
      → simple · aucune dépendance externe
      → la machine ne peut pas se déplacer — pas de bascule à chaud

  B — STOCKAGE PARTAGÉ EN RÉSEAU (bloc)
      [ hôte 1 ] ──┐
      [ hôte 2 ] ──┼──► [ baie de stockage ]
      [ hôte 3 ] ──┘
      → les machines se déplacent entre hôtes
      → ⚠️ LA BAIE EST LE POINT DE RUPTURE RÉEL — §23.2
      → un réseau de stockage dédié, souvent invisible sur les schémas

  C — SERVEUR DE FICHIERS (fichier)
      [ postes et serveurs ] ──► [ serveur de fichiers ]
      → partage simple · droits par dossier — §21
      → cible de choix pour un rançongiciel

  D — STOCKAGE OBJET
      [ applications ] ──interface──► [ stockage objet ]
      → capacité quasi illimitée · souvent chez un tiers
      → ⚠️ accessible par une clé, pas par le réseau : un filtrage
        réseau ne le protège pas
```


⚠️ **Le mode D mérite une attention particulière en lecture.** Un stockage objet n'est pas atteint par le réseau interne mais **par une interface applicative avec une clé**. Cela signifie que :

- il peut être joignable **depuis n'importe où**, si la clé fuit ;
- un pare-feu ne le protège pas ;
- **il n'apparaît sur aucun schéma réseau**, parce qu'il n'y a pas de lien à dessiner.

C'est l'un des composants les plus fréquemment oubliés des inventaires — volume Asset Management.

### Réplication, instantané, sauvegarde — les trois qu'on confond

> **La confusion la plus lourde de conséquences du chapitre.**

| | **Réplication** | **Instantané** | **Sauvegarde** |
|---|---|---|---|
| Ce que c'est | Une copie **continue** vers un autre stockage | Un **état figé** à un instant, sur le même stockage | Une copie **indépendante**, ailleurs |
| Protège contre | La panne d'un stockage | Une **erreur récente** — suppression, mise à jour ratée | **Tout**, y compris la perte du site |
| Ne protège **pas** contre | **Une suppression** — elle est répliquée aussitôt | **La perte du stockage** — l'instantané est dessus | Rien, si elle n'a jamais été testée |
| Délai de restauration | Immédiat, par bascule | Minutes | **Heures à jours** |
| Coût | Élevé — un second stockage complet | Faible | Moyen |

⚠️ **Les trois lignes du milieu contiennent l'essentiel** :

**Une réplication n'est pas une sauvegarde.** Elle copie tout, y compris les erreurs. Un fichier supprimé par erreur est supprimé des deux côtés en quelques secondes. **Un rançongiciel est répliqué.**

**Un instantané n'est pas une sauvegarde.** Il vit sur le même stockage que la donnée d'origine. Si la baie tombe, ou si elle est chiffrée, **les instantanés disparaissent avec**.

**Une sauvegarde n'en est une que si elle est indépendante** — autre support, autre système, **idéalement hors ligne ou en écriture unique**. Et si elle n'a jamais été restaurée pour de vrai, c'est une croyance — *principe de preuve*.

🔥 **SCÉNARIO — « on a des snapshots » ne suffit pas**

| Question | Réponse |
|---|---|
| Symptôme | Un rançongiciel a chiffré les partages. L'équipe annonce des instantanés toutes les heures |
| Hypothèse naïve | « On restaure, on perd une heure » |
| Dépendance réelle | **Les instantanés sont sur la même baie**, et le compte compromis pouvait les supprimer |
| Ce que le schéma aurait dû montrer | Où vivent les instantanés, et qui peut les supprimer |
| Concevoir différemment | Une copie **hors du périmètre atteignable** par un compte d'exploitation |

🔥 **SCÉNARIO — la baie tombe, dix hôtes redondés s'arrêtent**

| Question | Réponse |
|---|---|
| Symptôme | Dix hôtes de virtualisation en bonne santé. **Quarante machines arrêtées** |
| Hypothèse naïve | « Un problème d'hyperviseur » |
| Dépendance réelle | **Le stockage partagé** — la dépendance commune que le schéma logique ne montre pas |
| Ce que le schéma aurait dû montrer | La baie, et le fait que tous les hôtes en dépendent |
| Concevoir différemment | Un second stockage, avec réplication **et bascule testée** — ou accepter et le déclarer |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur la baie » | Stockage partagé en bloc | **Une seule baie ? C'est le point de rupture réel** |
| « On a des snapshots » | Des états figés existent | **Sur le même stockage ? Qui peut les supprimer ?** |
| « C'est répliqué » | Une copie continue existe | **Ce n'est pas une sauvegarde** — une suppression est répliquée |
| « C'est dans le bucket » | Stockage objet | **Joignable par clé, pas par le réseau.** Qui a la clé ? |
| « On est en NAS » | Stockage fichier | Partagé par combien de serveurs ? Qui a les droits ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Déplacer une machine entre hôtes | **Un stockage partagé qui devient la dépendance commune** |
| Partager des données entre serveurs | Des droits à tenir · une performance à surveiller |
| Stocker sans limite (objet) | **Un accès par clé, qu'aucun filtrage réseau ne protège** |
| Restaurer rapidement (instantané) | **Aucune protection contre la perte du stockage** |
| Restaurer en toute circonstance (sauvegarde) | Un délai long · un dispositif à exploiter · **un test à faire** |

🔭 **À RECONNAÎTRE — réseau de stockage dédié**

**① Qu'est-ce que c'est.** Un réseau **distinct du réseau de données**, réservé aux échanges entre les serveurs et les baies de stockage. **Fibre Channel** en est la technologie historique et dominante.

**② Quel problème il résout.** Les échanges avec le stockage sont massifs et sensibles à la latence. Les isoler du trafic ordinaire évite qu'une sauvegarde ne ralentisse une application.

**③ Ce que cela change en lecture de schéma.**

```
   [ serveur 1 ] ──┬── réseau Ethernet ──► le reste du SI
                   └── réseau de stockage ──► [ baie ]
                          ▲
             DEUX réseaux, deux cartes, deux jeux d'équipements
             Le second n'apparaît presque jamais sur un schéma logique
```


**Le vocabulaire à reconnaître** :

| Terme | Ce que c'est |
|---|---|
| **SAN** | Le réseau de stockage lui-même |
| **Fibre Channel** | La technologie dominante de ces réseaux |
| **Commutateur FC** | L'équipement qui les relie — l'équivalent du commutateur Ethernet |
| **Zoning** | Qui a le droit de parler à quoi — l'équivalent d'un filtrage |
| **LUN** | Le volume présenté à un serveur |

**④ Ce que cela change.** Une infrastructure entière, avec ses équipements, ses règles et ses pannes, **qui ne figure sur aucun schéma applicatif** — et qui est pourtant le chemin par lequel toutes les données transitent.

**⑤ Le coût.** Une compétence rare · des équipements dédiés · une évolution coûteuse. **C'est ce qui explique en partie l'attrait de l'hyperconvergence.**

**⑥ En réunion** : *« c'est sur le SAN »* → **combien de baies ? les serveurs voient-ils tous les mêmes volumes ?** · *« il y a un problème de zoning »* → un serveur ne voit plus son volume, **sans qu'aucune panne matérielle ne soit en cause**.

---

🔭 **À RECONNAÎTRE — immutabilité du stockage**

**① Qu'est-ce que c'est.** Un mécanisme qui **empêche la modification ou la suppression d'un objet pendant une durée déterminée**, y compris par un compte administrateur. On l'appelle couramment *Object Lock* sur les stockages objet.

**② Quel problème il résout.** Celui du §23.4 : une sauvegarde atteignable par un compte compromis est chiffrée ou supprimée avec le reste. **L'immutabilité rend cette suppression impossible, même avec les droits nécessaires.**

**③ Où on le rencontre.** Sur les stockages objet servant de destination de sauvegarde, et comme argument commercial majeur des solutions de protection contre les rançongiciels.

**④ Ce que cela change.**

```
   SAUVEGARDE ORDINAIRE
      compte compromis ──► peut supprimer ──► plus de sauvegarde

   SAUVEGARDE IMMUABLE
      compte compromis ──► ne peut pas supprimer avant la fin du délai
      ⚠️ MAIS : peut cesser d'en créer de nouvelles
```


⚠️ **Les deux réserves à connaître, et elles sont importantes** :

> **L'immutabilité n'est pas une sauvegarde à elle seule.** Elle protège une copie existante ; elle ne garantit ni que cette copie soit complète, ni qu'elle soit exploitable.

> **Une sauvegarde non modifiable reste inutile si elle n'a jamais été restaurée.** C'est le principe de preuve appliqué au stockage.

**⑤ Le coût.** Un volume qui ne peut plus être réduit avant l'échéance — **une erreur de configuration de durée coûte cher** · une gestion du cycle de vie plus rigide.

**⑥ En réunion** : *« nos sauvegardes sont immuables »* → **pour combien de temps ? l'administrateur du stockage peut-il modifier ce délai ? et quand a-t-on restauré pour la dernière fois ?**

---

🔭 **À RECONNAÎTRE — quorum**

> **Plus fondamental que son apparence**, et c'est le concept qui explique pourquoi trois nœuds ne signifient pas trois fois plus de sécurité.

**① Qu'est-ce que c'est.** Le mécanisme par lequel **un ensemble distribué décide quelle partie a le droit de continuer** lorsque ses membres ne peuvent plus communiquer entre eux.

**② Quel problème il résout.** Le lecteur voit trois nœuds et pense *« redondant »*. Mais que se passe-t-il si le réseau se coupe **entre** les nœuds ?

```
   AVANT              [ A ] ── [ B ] ── [ C ]     tout va bien

   COUPURE            [ A ] ──X── [ B ] ── [ C ]

   SANS QUORUM        A pense être seul survivant → il continue
                      B et C pensent que A est mort → ils continuent
                      ⚠️ DEUX systèmes actifs, deux vérités divergentes
                         → c'est le « split-brain »

   AVEC QUORUM        A est en minorité (1 sur 3) → IL S'ARRÊTE
                      B et C sont majoritaires (2 sur 3) → ils continuent
                      → une seule vérité subsiste
```


⚠️ **③ Ce que cela impose, et qui surprend** :

> **Un membre en bonne santé peut être contraint de s'arrêter, non parce qu'il est en panne, mais parce qu'il ne peut pas prouver qu'il est du bon côté.**

**Deux conséquences pratiques** :

| Conséquence | Explication |
|---|---|
| **Un nombre impair est préférable** | Avec deux nœuds, une coupure donne 1 contre 1 : **aucun n'est majoritaire, tout s'arrête** |
| **Il faut parfois un arbitre** | Un troisième élément — un témoin, un disque, un service tiers — dont le seul rôle est de départager |

**④ Où on le rencontre.** Clusters de bases de données · plateformes de virtualisation · stockage distribué · orchestrateurs de conteneurs · hyperconvergence. **Partout où plusieurs machines doivent se mettre d'accord.**

**⑤ Le coût.** Un membre ou un arbitre supplémentaire · **un comportement en cas de coupure qu'il faut connaître avant l'incident** · une architecture réseau entre nœuds qui devient critique.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a deux nœuds en cluster » | **Que se passe-t-il si le lien entre eux tombe ?** Y a-t-il un arbitre ? |
| « Le cluster s'est arrêté tout seul » | **Perte de quorum** — les nœuds ont refusé de continuer sans majorité |
| « On a trois nœuds sur deux sites » | **Deux d'un côté, un de l'autre.** Si le site majoritaire tombe, le troisième s'arrête aussi |

⚠️ **La dernière ligne est un piège classique de conception multi-sites** : trois nœuds répartis 2+1 ne protègent pas contre la perte du site qui en porte deux. **Il faut un arbitre sur un troisième emplacement.**

## 23.6 Le plan de gestion

**Le composant le moins dessiné et le plus critique de la partie.**

| | |
|---|---|
| Ce que c'est | La console qui pilote l'ensemble des hôtes et des machines |
| Ce qu'il permet | Créer, supprimer, déplacer, cloner, **accéder à la console d'une machine sans passer par son système** |
| Ce qu'une compromission donne | **L'accès à toutes les machines qu'il pilote** — y compris en copiant leurs disques |
| Sur les schémas | **Jamais** |

⚠️ **La troisième ligne mérite d'être développée.** Qui contrôle le plan de gestion peut **cloner une machine** et en examiner le disque hors ligne — sans jamais s'authentifier sur son système, sans laisser de trace dans ses journaux. **Aucun contrôle placé à l'intérieur d'une machine ne protège contre cela.**

C'est le §3.4 et le chapitre 27 : **le chemin d'administration est plus puissant que ce qu'il administre**, et il n'est pas représenté.

## 23.7 S'il disparaît

🔥 **SCÉNARIO — deux machines redondées tombent ensemble**

| Question | Réponse |
|---|---|
| Symptôme | Les deux exemplaires d'un service s'arrêtent simultanément |
| Hypothèse naïve | « Un problème applicatif commun » |
| Dépendance réelle | **Elles partagent l'hôte** — ou le stockage, ou l'alimentation |
| Ce que le schéma aurait dû montrer | La couche physique sous les machines |
| Concevoir différemment | Une règle d'anti-affinité, configurée **et vérifiée** |

🔥 **SCÉNARIO — le plan de gestion tombe pendant une panne**

| Question | Réponse |
|---|---|
| Symptôme | Un hôte est en panne. **La bascule ne se déclenche pas** |
| Hypothèse naïve | « La bascule ne fonctionne pas » |
| Dépendance réelle | **C'est le plan de gestion qui l'orchestre.** S'il est lui-même hébergé sur la plateforme, il peut être tombé avec |
| Ce que le schéma aurait dû montrer | Où s'exécute le plan de gestion |
| Concevoir différemment | Ne pas héberger le plan de gestion sur la plateforme qu'il pilote — **ou en avoir conscience** |

⚠️ **Ce second scénario est une dépendance circulaire classique**, et on la retrouve partout : l'outil qui répare dépend de ce qu'il répare. **C'est une question à poser systématiquement en conception.**

## 23.8 Ce qu'il fait à la donnée

L'hôte ne la lit pas, mais il **y a accès** : qui contrôle l'hyperviseur contrôle la mémoire et les disques de toutes les machines qu'il porte.

## 23.9 Sur un schéma

Souvent absente. On dessine des serveurs sans dire lesquels sont virtuels ni sur quoi ils reposent.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a deux nœuds mais le stockage est commun » | La redondance porte sur les hôtes seuls | **C'est une phrase précieuse** — elle nomme exactement le point de rupture |
| « On va migrer la VM à chaud » | La déplacer sans l'arrêter | Suppose un stockage partagé — **donc une dépendance commune** |
| « C'est virtualisé » | La machine est logique | **Sur quel hôte ? Avec quoi d'autre ?** |
| « On a du HA sur le cluster » | Un mécanisme de bascule existe | **Testé quand ? Le plan de gestion est-il hors du cluster ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Densifier, déplacer, provisionner rapidement | **Un plan de gestion dont la compromission donne tout** |
| Basculer une machine en cas de panne d'hôte | **Un stockage partagé qui devient le point de rupture réel** |
| Créer une machine en minutes | **Des machines créées sans être déclarées** — volume Asset Management |
| Migrer à chaud | Une dépendance forte au stockage partagé |

🏭 **TROIS TAILLES** — Atelier Martin : deux hôtes, pas de stockage partagé, pas de bascule automatique — **la contrainte de continuité ne le justifie pas**. HELIOMED : six hôtes, stockage partagé, bascule testée deux fois par an. Novaris : plusieurs centaines d'hôtes, **parce qu'elle exploite quatre mille machines** — pas parce qu'elle est grande.

---

## 🔬 Mini-lab 6 — Attribuer un rôle à sept serveurs

**Objectif** — Proposer un rôle probable à partir des seules connexions, et dire ce qui reste à vérifier.
**Durée** 30 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 18 à 23

**Les données** — sept serveurs, et les connexions observées sur une journée :

```
SRV-01  reçoit : 443 depuis la DMZ        émet : 8080 vers SRV-02, 389 vers SRV-06
SRV-02  reçoit : 8080 depuis SRV-01       émet : 1433 vers SRV-03, 389 vers SRV-06
SRV-03  reçoit : 1433 depuis SRV-02       émet : rien (hors sauvegarde)
SRV-04  reçoit : 445 depuis 600 postes    émet : 389 vers SRV-06
SRV-05  reçoit : 25 depuis la DMZ         émet : 443 vers Internet, 389 vers SRV-06
SRV-06  reçoit : 389 et 636 de partout    émet : 389 vers SRV-07
SRV-07  reçoit : 389 depuis SRV-06        émet : 389 vers SRV-06
```


❓ **Questions**

1. Quel est le rôle de chaque serveur ?
2. Lesquels sont des points de rupture ?
3. Qu'est-ce qui manque dans ces données ?

---

**Corrigé**

**1. Les rôles**

| Réf | Rôle | Raisonnement |
|---|---|---|
| **SRV-01** | Serveur web | Reçoit du web depuis la DMZ, relaie vers un applicatif |
| **SRV-02** | Serveur applicatif | Entre le web et la base — position et ports |
| **SRV-03** | Base de données | Reçoit du 1433, **n'émet rien** : le fond de la pile |
| **SRV-04** | Serveur de fichiers | Port 445, six cents postes |
| **SRV-05** | Relais de messagerie | Port 25 entrant, 443 sortant |
| **SRV-06** | Contrôleur d'annuaire | **Reçoit de partout**, ports 389 et 636. ⚠️ Ces ports ne montrent que l'interrogation |
| **SRV-07** | Second contrôleur, **probablement** | Échanges mutuels avec SRV-06 — compatibles avec une réplication, à confirmer |

**2. Les points de rupture**

| Serveur | Rupture ? | Nuance |
|---|---|---|
| SRV-01 | ⚠️ **Indéterminé** | Un seul est listé, mais il peut y en avoir d'autres non observés |
| **SRV-02** | ✅ **Oui** | Seul applicatif, tout le service en dépend |
| **SRV-03** | ✅ **Oui, le plus grave** | Base unique, perte potentiellement définitive |
| **SRV-04** | ✅ Oui | Pour le partage de fichiers uniquement |
| **SRV-05** | ✅ Oui | Pour la messagerie entrante |
| SRV-06 / 07 | ⚠️ **Indéterminé** | Deux contrôleurs suggèrent une redondance. **Principe de preuve : partagent-ils un hôte, un stockage, un site, une alimentation ?** Le dossier ne le dit pas |

**3. Ce qui manque** — et c'est la vraie question du lab :

| Manquant | Pourquoi c'est décisif |
|---|---|
| **La résolution de noms** | Aucun flux port 53 n'apparaît. Elle existe pourtant : sans elle, aucune de ces connexions n'aurait lieu. **Elle est hors du périmètre d'observation** |
| **La synchronisation d'horloge** | Idem. Sans elle, les authentifications 389 échoueraient |
| **Les hôtes de virtualisation** | Ces sept serveurs sont peut-être trois machines physiques |
| **Les chemins d'administration** | Aucun flux 22 ou 3389 : soit ils ne sont pas observés, soit l'administration passe ailleurs |
| **Les sauvegardes** | Mentionnées entre parenthèses, non détaillées |

**Les trois erreurs attendues**

1. **Conclure que SRV-01 n'est pas un point de rupture** parce qu'il « doit y en avoir d'autres ». Les données ne le disent pas — la bonne réponse est *indéterminé*.
2. **Oublier la résolution de noms** parce qu'elle n'apparaît dans aucune ligne. C'est le piège central : **une observation de flux ne montre que ce qu'on a observé**.
3. **Conclure que SRV-06 et SRV-07 forment une redondance établie.** Les échanges mutuels en sont un **indice**, pas une preuve : rien ne dit qu'ils ne partagent pas un hôte, un stockage ou un site. **Principe de preuve** — seul un test établit une capacité de basculement.

---

> ### 🎓 À ce stade de la Partie III, vous savez…
>
> ✓ que l'on sépare des serveurs **parce qu'ils n'ont pas les mêmes contraintes** — disponibilité, cycle, charge, conséquence d'une compromission ;
> ✓ pourquoi un serveur web est **facile à redonder** — il ne garde rien — et pourquoi ce « rien » doit alors vivre ailleurs ;
> ✓ pourquoi la **base se trouve au fond dans le modèle à trois niveaux**, et pourquoi une réplication non testée est une croyance, pas une redondance ;
> ✓ que la **messagerie** est simultanément une voie d'entrée majeure et le moyen de récupération de nombreux comptes ;
> ✓ que trois serveurs **dessinés redondés peuvent tourner sur le même hôte physique** — l'un des écarts les plus fréquents entre schéma et réalité ;
> ✓ que le **plan de gestion de la virtualisation** n'est jamais dessiné et donne accès à tout ce qu'il pilote ;
> ✓ **déduire le rôle d'un serveur de ses seules connexions**, et reconnaître ce qu'une observation de flux ne montre pas.
>
> **Ce que vous ne savez pas encore** : comment ces serveurs sont répartis dans des zones et des segments, et ce que cette répartition permet ou interdit. C'est l'objet de la Partie IV.

---
