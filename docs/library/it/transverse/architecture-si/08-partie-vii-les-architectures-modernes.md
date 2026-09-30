---
title: PARTIE VII — Les architectures modernes
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 8
chapters: 10
---

> **Toujours : comment les lire, jamais comment les déployer.** Ces quatre chapitres n'enseignent aucune technologie ; ils enseignent ce que chacune change dans la lecture d'un schéma.

---

## Chapitre 39 — Le cloud

### 39.1 La question qui structure tout le chapitre

> **Qu'est-ce qui disparaît du schéma sans disparaître du système ?**

C'est la seule question utile pour lire une architecture cloud. Le fournisseur masque une partie de l'infrastructure — mais le réseau, les identités, les données, les dépendances, les secrets et la résilience **existent toujours**. Ils ont simplement changé de forme, et souvent de responsable.

### 39.2 Ce qui change et ce qui ne change pas

| Ne change pas | Change |
|---|---|
| Les trois familles de flux | **Qui exploite quoi** |
| Les points de rupture | Leur emplacement et leur visibilité |
| La nécessité d'authentifier | Le composant qui le fait |
| Le fait que la donnée soit quelque part | **Où « quelque part » se trouve** |
| La sédimentation | Elle **s'accélère** — le provisionnement est instantané |

⚠️ **La dernière ligne mérite d'être développée.** Créer une machine prenait des semaines ; cela prend des minutes. **La sédimentation du chapitre 4 s'accélère donc d'un ordre de grandeur** : des ressources créées pour un essai, jamais supprimées, jamais inventoriées. C'est le sujet central du volume Asset Management.

### 39.3 La frontière de responsabilité

🖼 **SCHÉMA 39.1 — Où passe la ligne**

```
                    SUR SITE    INFRA.     PLATE-    LOGICIEL
                                LOUÉE      FORME     EN LIGNE

  Données             VOUS       VOUS       VOUS       VOUS
  Accès et identités  VOUS       VOUS       VOUS       VOUS
  Configuration       VOUS       VOUS       VOUS       VOUS
  Application         VOUS       VOUS       VOUS      fournisseur
  Exécution           VOUS       VOUS     fournisseur fournisseur
  Système             VOUS       VOUS     fournisseur fournisseur
  Virtualisation      VOUS     fournisseur fournisseur fournisseur
  Matériel            VOUS     fournisseur fournisseur fournisseur
```

**Les trois premières lignes restent des responsabilités à gouverner, même lorsque leur mise en œuvre est partagée avec le fournisseur.** Quel que soit le modèle, **vous répondez des données que vous y placez, des identités qui y accèdent et des choix de configuration qui vous sont offerts** — même si les moyens techniques de les mettre en œuvre varient fortement d'un service à l'autre — et ce sont précisément les sujets des volumes Asset Management et Identités de cette collection.

⚠️ **Une nuance qui compte, surtout en logiciel en ligne** : *responsable* ne signifie pas *maître de tous les réglages*. Le fournisseur décide de ce qui est configurable, et une partie de la configuration lui appartient — chiffrement au repos, cloisonnement entre clients, durée de conservation des journaux. **Vous êtes responsable de ce que vous pouvez régler, et vous dépendez de lui pour le reste.**

> **La question de lecture** : *quels réglages ce service m'expose-t-il, et lesquels décide-t-il à ma place ?*

⚠️ **Une erreur de lecture courante** : croire que la ligne descend uniformément. Elle descend **par composant**, et une organisation utilise généralement les quatre modèles simultanément. **Il n'y a pas une frontière, il y en a une par service.**

### 39.4 Six comparaisons, et ce que chacune coûte

**C'est le cœur du chapitre.** Pour chaque transformation : *qu'est-ce que je n'exploite plus ? qu'est-ce que je dois toujours concevoir ? quelle nouvelle dépendance ai-je achetée ?*

#### A — Sur site contre infrastructure louée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Matériel, alimentation, virtualisation | **Système, correctifs, sauvegardes, réseau, identités** | La disponibilité du fournisseur · sa facturation à l'usage |

⚠️ **Ce qui surprend le plus** : les correctifs système restent entièrement à votre charge. **Louer une machine ne la maintient pas.**

#### B — Infrastructure louée contre plateforme managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Système, correctifs, une partie de la disponibilité | **L'application, les données, les accès, l'architecture** | Le calendrier de version du fournisseur · **une réversibilité faible** |

⚠️ **Le coût caché de B** : le fournisseur décide quand la version change. **Vous n'êtes plus maître du calendrier**, ce qui est un gain d'exploitation et une perte de maîtrise.

#### C — Machine virtuelle contre conteneur

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un système par application | **L'image, les dépendances embarquées, l'orchestration** | **Un système distribué complet** — §41 |

⚠️ **Le piège** : le conteneur ne supprime pas le système, **il le déplace dans l'image**. Une image jamais reconstruite embarque des composants jamais corrigés. La maintenance n'a pas disparu, elle a changé de main — et souvent, de personne responsable.

#### D — Base auto-hébergée contre base managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Correctifs, sauvegardes automatiques, réplication | **Le schéma de données, les accès, la performance** | Le calendrier de version · **des limitations sur ce qu'on peut faire** |

⚠️ **Ce qu'on découvre après** : certaines opérations d'administration ne sont plus possibles. **Le confort a un prix qui se paie en flexibilité.**

#### E — Monolithe contre microservices

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un déploiement couplé pour tout | **Les contrats entre services, la cohérence des données** | **Le réseau devient un composant du système** — §42.1 |

⚠️ **Le changement de nature** : entre deux microservices, un appel **traverse le réseau**, et hérite donc de tous ses modes de défaillance — perte, latence, duplication, réponse jamais reçue alors que l'action a eu lieu. Chaque appel devient un point de rupture potentiel, **qui n'existait pas dans le monolithe**.

#### F — Tunnel chiffré contre interconnexion dédiée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Une passerelle et son chiffrement | **Le routage, les identités, la résolution de noms** | Un lien contractuel · un délai de mise en place de plusieurs semaines |

⚠️ **Ce que l'interconnexion ne supprime pas** : elle donne un lien privé et performant. **Elle ne résout ni l'identité, ni la résolution de noms, ni les dépendances applicatives** — c'est le §40.2.

🔭 **À RECONNAÎTRE — SASE, SSE, CASB**

> ⚠️ **Avertissement préalable, et il est important.** Ces trois sigles viennent en partie de **taxonomies de marché**. Leur périmètre varie d'un fournisseur à l'autre, et deux produits portant le même sigle ne font pas nécessairement la même chose.

**① Ce que chacun désigne**

| Sigle | Ce qu'il recouvre |
|---|---|
| **SASE** | La **convergence de fonctions réseau et de sécurité distribuées**, délivrées notamment depuis le cloud — le pilotage du réseau étendu et les contrôles de sécurité dans une même offre |
| **SSE** | Le **sous-ensemble orienté sécurité** : les mêmes contrôles, **sans la composante réseau étendu** |
| **CASB** | Les **contrôles et la visibilité appliqués à l'usage des services en ligne** — qui utilise quoi, avec quelles données |

**② Quel problème cela résout.** Le §11.3 l'a posé : quand les applications sont en ligne et les postes nomades, **faire remonter le trafic au siège pour le contrôler n'a plus de sens**. Les contrôles doivent se déplacer là où sont les utilisateurs.

```
   MODÈLE HISTORIQUE
      [ poste ] ──► siège ──► [ contrôles ] ──► Internet
      → tout remonte · latence · le lien du siège porte tout

   MODÈLE DISTRIBUÉ
      [ poste ] ──► [ point de présence du fournisseur ] ──► Internet
                            │
                     les contrôles sont ICI
      → le poste nomade est contrôlé sans passer par le siège
```

**③ Ce que cela change dans les flux.** **Les contrôles quittent votre infrastructure.** Le point où l'on peut agir — chapitre 43 — n'est plus chez vous : il est chez un fournisseur, dans un point de présence que vous ne voyez pas.

**④ Le coût.** Une dépendance de disponibilité majeure — **si le service est indisponible, vos postes n'accèdent plus à rien** · une visibilité qui dépend de ce que le fournisseur expose · une réversibilité faible · **et un contrôle qui voit tout le trafic de vos salariés**, y compris personnel.

⚠️ **⑤ La phrase à retenir** :

> **Ces sigles décrivent des familles de capacités et des modèles d'architecture. Ils ne garantissent pas une implémentation identique d'un fournisseur à l'autre.**

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On passe en SASE » | **Quelles fonctions exactement ?** Le sigle ne le dit pas |
| « Le CASB voit nos SaaS » | **Ceux qu'il connaît.** Et les autres — §38.1 ? |
| « Les postes sortent par le SSE » | **Que se passe-t-il si le service est indisponible ?** |
| « C'est du Zero Trust » | Un modèle, pas un produit. **Quelle décision d'architecture cela recouvre-t-il ici ?** |

📚 **À approfondir ailleurs** : ces sujets relèvent des volumes *Identités et accès* et *Détection* de cette collection.

### 39.5 Ce qui devient invisible

| Élément | Sur site | Dans le cloud |
|---|---|---|
| Le réseau | Segments, équipements | **Des règles logiques**, sans équipement à pointer |
| Les machines | Une baie, un hôte | **Un identifiant, une région** |
| Les frontières | Un pare-feu | Des groupes de règles, **beaucoup plus nombreux** |
| La sauvegarde | Un serveur | Une option de configuration — **activée ou non** |
| La redondance | Des équipements visibles | **Une case cochée** — ou pas |

⚠️ **Les deux dernières lignes produisent le plus de mauvaises surprises.** Une ressource cloud sans sauvegarde configurée n'a **aucune** sauvegarde — il n'existe pas de dispositif central qui rattrape l'oubli. **Sur site, quelqu'un finit par s'apercevoir qu'un serveur n'est pas sauvegardé. Dans le cloud, personne.**

🔥 **SCÉNARIO — la ressource supprimée par erreur n'était pas sauvegardée**

| Question | Réponse |
|---|---|
| Symptôme | Une base est supprimée. Aucune sauvegarde n'existe |
| Hypothèse naïve | « La sauvegarde a échoué » |
| Dépendance réelle | **Elle n'avait jamais été activée.** Ce n'est pas une option par défaut |
| Ce que le schéma aurait dû montrer | Rien — une sauvegarde cloud n'est pas un composant, c'est un paramètre |
| Concevoir différemment | Vérifier la configuration, pas l'existence d'un composant |

### 39.6 Ce qui reste entièrement à votre charge

**La liste que le lecteur doit retenir**, parce qu'elle survivra à tous les modèles :

```
   ☐ Les DONNÉES : où elles sont, qui y accède, combien de copies
   ☐ Les IDENTITÉS : qui peut faire quoi, et qui peut le changer
   ☐ La CONFIGURATION : ce qui est activé, exposé, sauvegardé
   ☐ Les DÉPENDANCES : ce que votre service appelle, et réciproquement
   ☐ Les SECRETS : où ils vivent, qui les voit — §33
   ☐ La RÉSILIENCE : ce qui se passe si une région tombe
   ☐ La RÉVERSIBILITÉ : ce que coûterait un changement de fournisseur
```

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans le cloud » | La ressource est chez un fournisseur | **Quel modèle ?** La frontière de responsabilité change du tout au tout |
| « C'est managé » | Le fournisseur exploite une partie | **Laquelle exactement ?** Les correctifs ? Les sauvegardes ? |
| « On est multi-région » | La ressource existe à deux endroits | **Basculement automatique ou manuel ? Testé ?** — *principe de preuve* |
| « Le cloud est plus sûr » | Le fournisseur sécurise son socle | **Les trois premières lignes du §39.3 restent à vous** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Provisionner en minutes, payer à l'usage | **Des ressources créées sans être déclarées** |
| Déléguer l'exploitation de couches basses | Une dépendance à un tiers, et une visibilité réduite |
| Absorber une charge variable | **Une facture variable**, et des ressources oubliées qui coûtent |
| Bénéficier de services managés | Une réversibilité faible · **un calendrier de version subi** |

---

## Chapitre 40 — L'hybride

> **Un point de fragilité récurrent des architectures modernes**, et l'un des plus fréquents.

### 40.1 Ce qu'est une architecture hybride

Un système dont une partie est sur site et une partie chez un fournisseur, **avec des flux entre les deux**. C'est la situation de la quasi-totalité des organisations, et elle est rarement le résultat d'une décision unique.

⚠️ **C'est presque toujours un état de sédimentation**, pas un choix d'architecture : une application est passée en ligne, puis une autre, puis la messagerie — et personne n'a jamais dessiné l'ensemble.

### 40.2 Les trois liens, et leurs fragilités

🖼 **SCHÉMA 40.1 — Les trois liens d'une architecture hybride**

```
   ┌──────────────┐                        ┌──────────────┐
   │   SUR SITE   │                        │    CLOUD     │
   │              │  ① lien réseau         │              │
   │  [annuaire]──┼───────────────────────►│  [ services ]│
   │              │  ② synchronisation     │              │
   │  [postes]  ──┼───────────────────────►│              │
   │              │     d'identités        │              │
   │  [données] ──┼───────────────────────►│  [ copies ]  │
   └──────────────┘  ③ flux de données     └──────────────┘
```

| Lien | Ce qui le rend fragile |
|---|---|
| **① Réseau** | Souvent unique, parfois un simple accès Internet. **Sa perte coupe tout l'hybride** |
| **② Identités** | La synchronisation d'annuaire est un flux de dépendance critique. **Une panne bloque les authentifications côté cloud** |
| **③ Données** | Réplications, sauvegardes croisées, exports. **Le plus difficile à cartographier** |

### 40.3 Le lien d'identités, en détail

**Un composant particulièrement fragile, et presque jamais supervisé.**

```
   [ annuaire interne ]
            │
            │  un composant de synchronisation
            │  s'exécute quelque part — souvent sur UNE machine
            ▼
   [ fournisseur d'identité en ligne ]
            │
            ▼
   [ services en ligne ]
```

**Ce qui casse, par ordre de fréquence** :

| Cause | Symptôme | Délai |
|---|---|---|
| Le composant de synchronisation est arrêté | Les créations et suppressions ne remontent plus | **Invisible pendant des jours** |
| Son certificat ou son secret a expiré | Idem | Idem |
| La machine qui l'héberge a été migrée ou supprimée | Idem | Idem |
| Le lien réseau est coupé | Les authentifications échouent, si le mode est direct | Immédiat |

⚠️ **La première ligne produit un incident silencieux et grave** : un salarié qui part est désactivé dans l'annuaire interne, **et reste actif côté cloud**. Personne ne s'en aperçoit — jusqu'à un audit, ou pire.

🔥 **SCÉNARIO — tout fonctionne, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | L'annuaire interne répond. Les services en ligne répondent. **Les nouveaux mots de passe ne fonctionnent pas** |
| Hypothèse naïve | « Les utilisateurs se trompent » |
| Dépendance réelle | **Le composant de synchronisation est arrêté depuis trois jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'est presque jamais dessiné |
| Comment le reconnaître | **Les anciens mots de passe fonctionnent, les nouveaux non.** C'est signé |
| Concevoir différemment | Superviser le composant **et la fraîcheur de la synchronisation**, pas seulement son état |

### 40.4 La question à poser à toute architecture hybride

> **Que peut-on faire si le lien tombe ?**

| Réponse | Ce qu'elle révèle |
|---|---|
| Rien des deux côtés | Une dépendance mutuelle totale — le pire cas |
| Le local fonctionne, le cloud non | Le cas courant |
| Le cloud fonctionne, le local non | **Fréquent et rarement anticipé** : les postes nomades vont bien, le siège est bloqué |
| Les deux fonctionnent en autonomie | Rare, et coûteux à obtenir |

**Comme au §26.1, personne ne connaît la réponse**, parce que personne n'a coupé le lien pour voir.

### 40.5 Trois architectures hybrides

```
  A — EXTENSION SIMPLE
      [ sur site ] ══lien══► [ quelques services en ligne ]
      → identités synchronisées · données majoritairement sur site
      → si le lien tombe : le sur site continue, le cloud est isolé

  B — BASCULE PROGRESSIVE
      [ sur site : legacy ] ◄══lien══► [ cloud : nouveau ]
      → les deux côtés portent du métier · flux dans les deux sens
      → si le lien tombe : LES DEUX sont dégradés
      → ⚠️ un état très répandu, et le plus fragile des trois

  C — CLOUD PRINCIPAL, SUR SITE RÉSIDUEL
      [ cloud : tout ] ◄══lien══ [ sur site : industriel, legacy ]
      → le cloud est autonome · le résiduel dépend du lien
      → si le lien tombe : seul le résiduel est isolé
```

⚠️ **Le mode B est un état de transition qui dure des années.** Il combine les contraintes des deux mondes et les avantages d'aucun — et il n'a été choisi par personne.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est en hybride » | Une partie est en ligne | **Quel mode ? Que se passe-t-il si le lien tombe ?** |
| « Les identités sont synchronisées » | Un composant réplique l'annuaire | **Où s'exécute-t-il ? Est-il supervisé ? Quelle fraîcheur ?** |
| « On a une interco » | Un lien privé existe | Redondé ? Et l'identité passe-t-elle par là ? |
| « Ça marche depuis chez moi » | Le nomade accède au cloud directement | **Il ne teste pas le lien du siège** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Adopter des services en ligne sans tout migrer | **Une architecture à deux mondes, avec les contraintes des deux** |
| Conserver les identités internes | **Un composant de synchronisation critique et invisible** |
| Garder des données sur site | Des flux de données à cartographier — le plus difficile |

---

## Chapitre 41 — Conteneurs et orchestration

### 41.1 Ce qui change réellement

**La transformation en une ligne** :

```
   SERVEUR PHYSIQUE   1 machine · 1 système · 1 application
          ▼
   MACHINE VIRTUELLE  1 machine physique · N systèmes · N applications
          ▼
   CONTENEUR          1 système · N applications isolées
                      → le système n'est plus dupliqué
          ▼
   FONCTION           plus de machine visible du tout
                      → le code s'exécute à la demande
```

⚠️ **Ce que chaque étape supprime, et ce qu'elle déplace** :

| Transformation | Ce qui disparaît | Où cela va |
|---|---|---|
| Physique → virtuel | La dépendance à un matériel précis | **Vers l'hyperviseur et le stockage partagé** — §23.2 |
| Virtuel → conteneur | Un système par application | **Vers l'image**, qui embarque les dépendances |
| Conteneur → orchestration | Le placement manuel | **Vers le plan de contrôle**, qui décide où tourne quoi |
| Orchestration → fonction | La notion de serveur | **Vers la plateforme**, entièrement |

> **Rien ne disparaît du système. Tout se déplace — et souvent vers un composant que le schéma ne montre pas.**

### 41.2 Pourquoi ces schémas sont illisibles

**Le problème** : un schéma de conteneurs représente souvent des dizaines d'objets éphémères, sans hiérarchie apparente, avec un vocabulaire propre.

**La cause** : on tente de représenter des **instances** alors que ce qui compte est la **structure**.

🖼 **SCHÉMA 41.1 — Deux façons de dessiner le même cluster**

```
  ILLISIBLE — les instances
     [c1][c2][c3][c4][c5][c6][c7][c8][c9][c10][c11][c12]...
     Quarante boîtes, sans hiérarchie, qui changent toutes les heures.

  LISIBLE — les classes et les frontières
     ┌─────────── CLUSTER ───────────────────────────┐
     │  ENTRÉE     [ contrôleur d'entrée ]           │
     │                     │                         │
     │  SERVICES    [ front ×n ] [ api ×n ]          │
     │                     │                         │
     │  ÉTAT        [ base ] ← hors du cluster       │
     │                                               │
     │  PLAN DE CONTRÔLE  [ orchestrateur ]          │
     └───────────────────────────────────────────────┘
```

**La règle de lecture** : dans un cluster, on ne lit pas les instances, on lit **quatre choses** :

| Quoi | Question | Pourquoi c'est celle-là |
|---|---|---|
| **L'entrée** | Par où arrive une requête externe ? | C'est le seul point stable du cluster |
| **Les services** | Quels rôles, en combien d'exemplaires *variables* ? | Le nombre change ; le rôle non |
| **L'état** | **Où sont les données ?** | Presque toujours **à l'extérieur** du cluster |
| **Le plan de contrôle** | Qui pilote ? | **Sa compromission donne tout le cluster** |

⚠️ **La troisième ligne est la plus importante en lecture.** Les conteneurs sont conçus pour être jetables ; ce qui ne l'est pas — les données — vit ailleurs. **Un schéma de cluster qui montre une base à l'intérieur est soit une simplification, soit une architecture à interroger.**

### 41.3 Les quatre nouvelles dépendances

**Ce que l'orchestration ajoute, et qui n'existait pas avant** :

| Dépendance | Ce qu'elle fait | Si elle tombe |
|---|---|---|
| **Le plan de contrôle** | Décide où tourne quoi, redémarre ce qui échoue | Ce qui tourne continue · **rien ne peut plus être déployé, redémarré ni réparé** |
| **Le registre d'images** | Fournit les images au démarrage | **Un conteneur qui redémarre ne repart pas** |
| **La découverte de service** | Traduit un nom de service en adresse d'instance | **Les services ne se trouvent plus entre eux** |
| **La configuration distribuée** | Fournit les paramètres et les secrets | Les instances redémarrées échouent |

⚠️ **Les quatre partagent la même propriété** : leur panne **n'arrête pas ce qui tourne**, elle empêche **ce qui redémarre**. C'est le même mécanisme que le coffre à secrets, §33.4, et que l'attribution d'adresses, §15.3 — **une panne différée jusqu'au prochain événement**.

🔥 **SCÉNARIO — le cluster fonctionne, mais plus rien ne peut être réparé**

| Question | Réponse |
|---|---|
| Symptôme | Les applications répondent. Un déploiement échoue. Un conteneur mort ne repart pas |
| Hypothèse naïve | « Un problème avec le déploiement » |
| Dépendance réelle | **Le plan de contrôle est indisponible** — ou le registre d'images |
| Ce que le schéma aurait dû montrer | Que le plan de contrôle est un composant, avec sa propre disponibilité |
| Ce qui aggrave | **Chaque conteneur qui meurt ne revient pas.** La dégradation est progressive et irréversible |

⚠️ **C'est un cas de dégradation lente que rien ne signale.** Le service fonctionne à quatre-vingt-quinze pour cent, puis quatre-vingts, puis soixante — sans qu'aucune alerte ne se déclenche, parce que **le service répond toujours**.

### 41.4 La découverte de service

**Un mécanisme qui mérite d'être compris**, parce qu'il n'apparaît nulle part et qu'il remplace quelque chose de familier.

```
   HORS CLUSTER
      app ──► résolution de noms ──► adresse fixe ──► base

   DANS UN CLUSTER
      app ──► découverte de service ──► adresse d'une instance
                                         qui change fréquemment
```

📌 **Une précision importante** : la découverte de service n'est **pas** un remplacement du mécanisme de résolution de noms. C'est une **fonction** — fournir un nom stable pour un ensemble d'instances qui changent — et elle est **fréquemment implémentée avec la résolution de noms elle-même**, avec des durées de vie très courtes. D'autres implémentations existent : registre dédié, mandataire local, configuration distribuée.

> **Ce qui change n'est pas le protocole. C'est que le nom désigne désormais un *service*, dont les instances apparaissent et disparaissent.**

⚠️ **Ce que cela change en lecture** : dans un cluster, **l'adresse n'a plus aucune signification durable**. Une règle de pare-feu par adresse ne fonctionne pas · un journal contenant une adresse n'identifie rien · un blocage par adresse est inopérant. **Tout doit se raisonner par identité de service, pas par adresse.**

C'est aussi ce qui rend l'inventaire d'un cluster particulièrement difficile — volume Asset Management, chapitre 6.

🔭 **À RECONNAÎTRE — maillage de services**

> **L'exemple parfait du principe du coût** : une brique résout un problème réel **et** en introduit un.

**① Qu'est-ce que c'est.** Une couche qui s'insère entre les services pour prendre en charge ce qu'ils devraient sinon implémenter chacun de leur côté : identité entre services, chiffrement, politiques d'appel, télémétrie, routage.

**② Ce que cela change conceptuellement.**

```
   SANS
      [ service A ] ◄──────────────► [ service B ]
      chaque service gère lui-même : chiffrement, réessais,
      identité, mesure

   AVEC
      [ A ] ◄─► [ couche ] ◄─────► [ couche ] ◄─► [ B ]
      la couche est déployée à côté de chaque service
      et intercepte tout ce qui entre et sort
```

**③ Ce qu'il apporte** : une identité par service, vérifiée à chaque appel · un chiffrement systématique entre services · des politiques centralisées — qui a le droit d'appeler qui · une télémétrie uniforme sans modifier le code · un routage fin pour les déploiements progressifs.

**④ Ce qu'il coûte** : **un composant à côté de chaque service** — donc autant de composants que d'instances · un plan de contrôle supplémentaire, critique · une latence ajoutée à chaque appel · **une compétence rare** · un diagnostic plus difficile, parce qu'un appel traverse maintenant deux intermédiaires.

⚠️ **⑤ Le message principal, et il est doctrinal** :

> **Tous les environnements de microservices n'ont pas besoin d'un maillage de services.**

Avec cinq services et une équipe, il apporte plus de complexité qu'il n'en résout. Avec quatre-vingts services et six équipes, il devient difficile de s'en passer. **La contrainte qui le justifie est le nombre d'interactions à gouverner, pas la modernité** — principe de la contrainte.

**⑥ En réunion** : *« on a un service mesh »* → **combien de services ? quelle contrainte cela résout-il que le code ne pourrait pas ?** · *« le mesh chiffre tout »* → **entre services seulement · et vers l'extérieur du cluster ?**

### 41.5 Trois architectures de cluster

```
  A — CLUSTER MANAGÉ, APPLICATIONS SANS ÉTAT
      Le fournisseur exploite le plan de contrôle.
      Les données sont dans une base managée, hors cluster.
      → le modèle le plus simple · le moins d'exploitation
      → une dépendance forte au fournisseur

  B — CLUSTER AUTOGÉRÉ
      Vous exploitez le plan de contrôle, les nœuds, le réseau,
      le stockage, la découverte, le registre.
      → maîtrise complète
      → ⚠️ un système distribué complet · 2 à 4 exploitants minimum

  C — CLUSTER AVEC DONNÉES À L'INTÉRIEUR
      La base est dans le cluster, sur du stockage persistant.
      → une seule plateforme à exploiter
      → ⚠️ le cas le plus difficile : les conteneurs sont jetables,
        les données ne le sont pas. Les deux logiques s'opposent
```

⚠️ **Le mode C n'est pas fautif** — il existe des raisons de le choisir. **Il est simplement celui qui demande le plus de compétence**, et c'est souvent celui qu'on adopte sans le savoir, en installant une base dans le cluster « pour commencer ».

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est sur le cluster » | L'application tourne dans l'orchestrateur | **Et les données ? Dedans ou dehors ?** |
| « Ça scale automatiquement » | Le nombre d'instances varie | **Et la base derrière ? Elle ne scale pas toute seule** |
| « On a trois nœuds » | Trois machines portent le cluster | Le plan de contrôle est-il sur ces mêmes nœuds ? |
| « Le pod a redémarré » | Une instance a été recréée | **Ce qu'elle contenait localement est perdu** |
| « C'est déclaratif » | L'état voulu est décrit, l'orchestrateur l'applique | **Que se passe-t-il si le plan de contrôle ne peut plus l'appliquer ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Déployer de façon reproductible, mettre à l'échelle | **Un système distribué complet à exploiter** |
| Remplacer une instance sans interruption | **Quatre nouvelles dépendances**, toutes à panne différée |
| Densifier l'usage du matériel | Des actifs éphémères invisibles aux inventaires |
| Raisonner par service et non par machine | **Les adresses perdent leur signification** — journaux, filtrage, blocage |

🏭 **TROIS TAILLES** — Atelier Martin : **aucun conteneur**, et aucune contrainte ne le justifierait. HELIOMED : un petit cluster à Nantes pour la chaîne de construction, **parce que les développeurs en avaient besoin** — pas pour la production. Novaris : plusieurs clusters de production, **parce que la variabilité de charge saisonnière l'impose**.

---

## Chapitre 42 — Microservices, fonctions et services en ligne

### 42.1 Pourquoi le schéma explose

**Le mécanisme** : découper une application en dix services indépendants multiplie par dix le nombre de boîtes, et par bien plus le nombre de flux entre elles.

| Architecture | Composants | Flux internes possibles |
|---|---|---|
| Application monolithique | 1 | 0 |
| Trois niveaux | 3 | 2 |
| **Dix microservices** | **10** | **jusqu'à 45** |

**Ce qu'on gagne** : chaque service évolue et se déploie indépendamment. **Ce qu'on perd** : la lisibilité, et la capacité à répondre simplement à *qu'est-ce qui tombe si ceci tombe*.

### 42.2 Le changement de nature qu'on sous-estime

> **Dans un monolithe, un appel entre deux modules peut échouer fonctionnellement — mais il ne peut pas échouer *à cause du réseau*. Entre deux microservices, il le peut.**

**Ce qui apparaît**, ce n'est pas l'échec : c'est **une classe d'échec nouvelle**. L'appel peut être perdu, dupliqué, retardé, ou réussir sans que l'appelant le sache.

**Ce que cela introduit, et qui n'existait pas** :

| Problème nouveau | Ce qu'il faut concevoir |
|---|---|
| L'appel peut échouer | Une politique de réessai — **et le risque de doubler une action** |
| L'appel peut être lent | Un délai maximal — **et que fait-on quand il expire ?** |
| Le service appelé peut être saturé | Un mécanisme qui cesse d'appeler plutôt que d'aggraver |
| La cohérence n'est plus garantie automatiquement | **Une transaction unique ne couvre plus naturellement deux services** — §42.2 |
| L'ordre des appels compte | Une orchestration, explicite ou implicite |

⚠️ **La quatrième ligne est celle qui coûte le plus cher en conception.** Dans un monolithe, une base garantit qu'une opération réussit entièrement ou pas du tout. Entre deux services, **une opération peut réussir d'un côté et échouer de l'autre**.

📌 **Des mécanismes existent pour rétablir cette cohérence**, et il faut les connaître pour ne pas croire à une impossibilité :

| Approche | Principe | Coût |
|---|---|---|
| **Transaction distribuée** | Un coordinateur valide ou annule partout | **Lourde · lente · couplage fort** — souvent évitée |
| **Compensation** | Chaque étape a son action inverse, déclenchée en cas d'échec | Une action inverse à écrire pour chaque étape |
| **Cohérence différée** | On accepte un état incohérent temporaire, réconcilié ensuite | **Le métier doit accepter ce délai** |
| **Idempotence** | Rejouer une action produit le même résultat | À concevoir dans chaque service |

> **Ce n'est donc pas une impossibilité technique. C'est un coût de conception qui n'existait pas dans le monolithe — et une décision métier : qu'accepte-t-on comme état intermédiaire ?**

### 42.3 Comment on lit malgré tout

**On ne lit pas un schéma de microservices comme un schéma classique.** Trois questions remplacent les sept passes :

```
1. QUEL EST LE CHEMIN D'UNE REQUÊTE TYPE ?
   Un seul parcours, pas la carte complète.

2. QUELS SERVICES SONT SUR CE CHEMIN ?
   Ce sont eux qui comptent. Les autres sont annexes.

3. LESQUELS N'ONT PAS D'ALTERNATIVE ?
   Ce sont les points de rupture — et ils sont peu nombreux.
```

**C'est le §35.4 appliqué** : on ne cartographie pas tout, on suit un service et on remonte ses dépendances.

🔥 **SCÉNARIO — un service lent en fait tomber cinq**

| Question | Réponse |
|---|---|
| Symptôme | Cinq services deviennent indisponibles. Un sixième est simplement lent |
| Hypothèse naïve | « Une panne générale » |
| Dépendance réelle | **Le service lent bloque ceux qui l'appellent**, qui bloquent à leur tour leurs appelants |
| Ce que le schéma aurait dû montrer | Les délais maximaux, et ce qui se passe à leur expiration |
| Concevoir différemment | Un mécanisme qui **cesse d'appeler** un service en difficulté plutôt que d'attendre |

⚠️ **Cette propagation en cascade est spécifique aux architectures distribuées**, et elle est contre-intuitive : **la lenteur se propage plus loin que la panne**. Un service arrêté échoue vite ; un service lent immobilise ses appelants.

🔭 **À RECONNAÎTRE — passerelle d'interfaces applicatives**

**① Qu'est-ce que c'est.** Une **façade contrôlée vers un ensemble d'interfaces applicatives**. C'est la formulation qui compte : ce n'est pas un mandataire inverse moderne, c'est une façade **avec une politique**.

**② Quel problème elle résout.** Quand dix services exposent chacun leur interface, chacun doit gérer l'authentification, les quotas, les versions, la journalisation. **La passerelle centralise ce qui est commun**, et laisse aux services ce qui est métier.

**③ Ce qu'elle centralise** :

| Fonction | Ce que le service n'a plus à faire |
|---|---|
| **Routage** | Savoir quelle version répond à quel appelant |
| **Authentification** | Vérifier un jeton — elle le fait en amont |
| **Quotas et limitation de débit** | Se protéger d'un appelant trop gourmand |
| **Transformations** | Adapter un format entre appelant et service |
| **Observabilité** | Produire une mesure uniforme de tous les appels |
| **Politiques d'interface** | Versions, dépréciation, contrats |

⚠️ **④ Le recouvrement avec le mandataire inverse est réel**, et il faut le nommer plutôt que de l'ignorer :

| | Mandataire inverse | Passerelle d'interfaces |
|---|---|---|
| Ce qu'il expose | **Des applications** | **Des interfaces applicatives** |
| Sa logique | Masquer, terminer, relayer | **Gouverner un contrat d'interface** |
| Ce qu'il connaît | Un chemin, un nom | **Une opération, un appelant, un quota** |

**En pratique, un même produit fait souvent les deux.** La question qui tranche : *existe-t-il parce qu'on publie des applications, ou parce qu'on gouverne des interfaces ?*

**⑤ Le coût.** Un point de passage obligé pour tous les appels — **donc un point de rupture** · une configuration qui grossit avec le nombre d'interfaces · une latence · **et le risque qu'elle devienne un fourre-tout** où l'on place de la logique métier qui n'y a pas sa place.

**⑥ En réunion** : *« ça passe par l'API gateway »* → **est-elle redondée ? qu'authentifie-t-elle exactement ?** · *« on a mis du rate limiting »* → **par appelant ou global ? que se passe-t-il quand la limite est atteinte ?**

---

🔭 **À RECONNAÎTRE — consensus distribué**

> **Conceptuel, et volontairement court.** Vous n'aurez pas à l'implémenter ; vous devez comprendre pourquoi c'est difficile.

**① Le problème.** Plusieurs machines doivent **se mettre d'accord sur un état commun**, malgré les pannes, les délais et les messages perdus.

**② Pourquoi c'est difficile.** Voici la phrase à retenir :

> **Répliquer une donnée est facile à dessiner. Maintenir un état cohérent entre plusieurs nœuds qui ne se font pas confiance sur le timing est un problème d'une tout autre nature.**

Deux nœuds qui reçoivent deux ordres contradictoires au même instant doivent aboutir au **même résultat**. Sans mécanisme, ils divergent — c'est le split-brain du §23.5.

**③ Où cela apparaît.** Dans tout ce qui doit décider collectivement : quel nœud est le maître · quelle configuration est la bonne · quel ordre les écritures ont-elles eu. **Orchestrateurs, bases distribuées, stockage réparti, services de configuration.**

**④ Ce que vous rencontrerez comme noms.** **Raft** et **Paxos** sont les algorithmes que vous verrez cités. Vous n'avez pas à les connaître — vous devez savoir que **c'est de cela qu'on parle**, et que leur présence signale un système distribué avec ses propres modes de défaillance.

**⑤ Ce que cela impose en architecture.** Un nombre de membres qui compte — §23.5, quorum · une latence entre membres qui devient structurante · **et une règle générale** :

> **Un système qui garantit une forte cohérence entre plusieurs nœuds paie ce choix en disponibilité ou en performance. Ce n'est pas un défaut d'implémentation, c'est un arbitrage.**

**⑥ En réunion** : *« c'est du Raft »* → un système distribué avec quorum. **Combien de membres ? Que se passe-t-il si la majorité est perdue ?**

### 42.4 La communication asynchrone

> **Le modèle que le reste du chapitre n'a pas traité**, et qui change complètement la nature des pannes.

#### Le principe

Tout ce qui précède raisonne en **appels synchrones** : A appelle B et attend la réponse. Il existe un second modèle, aussi répandu :

```
   SYNCHRONE
      [ A ] ──appel──► [ B ]
      A attend. Si B est lent, A est lent. Si B tombe, A échoue.

   ASYNCHRONE
      [ A ] ──dépose──► [ FILE ] ──consomme──► [ B ]
      A dépose un message et continue. B le traite quand il peut.
      Si B tombe, A ne s'en aperçoit pas.
```

**Le composant intermédiaire** — file de messages, courtier, bus d'événements — porte les messages entre les deux. Il change trois choses fondamentales :

| | Synchrone | Asynchrone |
|---|---|---|
| A sait si B a traité | **Oui, immédiatement** | **Non** — il sait seulement qu'il a déposé |
| B tombe | A échoue | **A continue** · les messages s'accumulent |
| B est lent | A est lent | A n'est pas affecté · **la file grandit** |
| Ordre du traitement | Garanti par l'appel | **À concevoir** |
| Diagnostic | Le chemin est visible | **Le lien de cause à effet est rompu dans le temps** |

#### Ce que le découplage fait gagner

**C'est réel, et c'est pourquoi ce modèle existe** :

| Gain | Pourquoi |
|---|---|
| **B peut tomber sans arrêter A** | Le service reste disponible pour l'utilisateur |
| **Absorber une pointe de charge** | La file sert de tampon : A dépose vite, B rattrape ensuite |
| **Plusieurs consommateurs** | On ajoute des instances de B pour traiter plus vite |
| **Plusieurs destinataires** | Un même événement peut intéresser trois services, sans que l'émetteur les connaisse |
| **Découplage des versions** | A et B évoluent séparément |

⚠️ **Le quatrième gain est le plus structurant en architecture** : l'émetteur ne sait pas qui consomme. **Cela signifie qu'on peut ajouter un consommateur sans toucher à l'émetteur** — et aussi qu'**on ne sait plus, en lisant le code de A, ce que son message déclenche**.

#### Les sept problèmes qu'on achète

**Aucun n'existait dans le modèle synchrone.**

| # | Problème | Ce qu'il faut concevoir |
|---|---|---|
| **1** | **Accumulation** | La file grandit si B est plus lent que A. **Que faire quand elle est pleine ?** |
| **2** | **Retard** | Le traitement n'est plus immédiat. **Le métier accepte-t-il ce délai ?** |
| **3** | **Doublons** | Un message peut être livré deux fois. **B doit être idempotent** |
| **4** | **Ordre** | Deux messages peuvent arriver dans le désordre. Souvent garanti seulement partiellement |
| **5** | **Rejeu** | Que fait-on d'un message qui échoue ? Le remettre ? Combien de fois ? |
| **6** | **Message empoisonné** | Un message qui échoue toujours bloque la file — d'où une **file d'échecs** dédiée |
| **7** | **Observabilité** | **Le lien entre la cause et l'effet est rompu** : A a déposé à 10 h, B a échoué à 14 h |

⚠️ **Le troisième est celui qu'on découvre le plus tard et qui coûte le plus cher.** La plupart des systèmes de messagerie garantissent **au moins une livraison**, pas exactement une. **Un message de débit bancaire livré deux fois débite deux fois** — sauf si le consommateur a été conçu pour reconnaître qu'il l'a déjà traité. C'est l'idempotence du §42.2.

⚠️ **Le sixième mérite d'être connu, parce qu'il porte un nom qu'on entendra** : un message que le consommateur n'arrive jamais à traiter est écarté vers une **file d'échecs** — souvent appelée *dead-letter queue*. **Personne ne la regarde**, et c'est là que les messages perdus finissent.

#### Les trois topologies à reconnaître

```
  A — FILE POINT À POINT
      [ A ] ──► [ file ] ──► [ B ]
      Un message, un consommateur. Le message est retiré une fois traité.
      → traitement de travaux, commandes à exécuter

  B — PUBLICATION / ABONNEMENT
      [ A ] ──► [ sujet ] ──┬──► [ B ]
                            ├──► [ C ]
                            └──► [ D ]
      Un message, plusieurs destinataires. Chacun a sa copie.
      → événements métier : « une commande a été passée »
      → ⚠️ l'émetteur ignore combien de services l'écoutent

  C — JOURNAL D'ÉVÉNEMENTS
      [ A ] ──► [ journal ordonné, conservé ] ◄── [ B ] lit à son rythme
      Les messages sont conservés et relisibles.
      → un nouveau consommateur peut REJOUER l'historique
      → ⚠️ le journal devient un actif de données à part entière
```

⚠️ **Le mode C brouille une frontière du cours** : le journal d'événements **est à la fois un flux et un stockage**. Il contient l'historique, il peut être rejoué, et il porte donc des données au sens du §32 — avec les copies, la rétention et les obligations qui vont avec.

#### Le point de rupture déplacé

> **Le courtier devient le composant dont tout dépend.**

| S'il tombe | Effet |
|---|---|
| **Les producteurs** | Ne peuvent plus déposer — **ils échouent, ou accumulent localement** |
| **Les consommateurs** | Ne reçoivent plus rien · **ils ne le signalent pas, ils attendent** |
| **Les messages en attente** | Perdus s'ils n'étaient pas persistés |

⚠️ **La deuxième ligne est celle qui rend le diagnostic difficile.** Un consommateur privé de messages **ressemble exactement à un consommateur qui n'a rien à faire**. Rien n'alerte — c'est le même mécanisme que la collecte de journaux interrompue, §34.3.

📌 **La seule protection est de superviser le débit** : messages déposés, messages consommés, taille de la file. **Une file qui ne bouge plus est un incident silencieux.**

🔥 **SCÉNARIO — les commandes ne partent plus depuis trois jours**

| Question | Réponse |
|---|---|
| Symptôme | Le site de commande fonctionne. Les clients confirment. **Rien n'arrive en logistique** |
| Hypothèse naïve | « Un problème dans le système logistique » |
| Dépendance réelle | **Le consommateur est arrêté.** Les messages s'accumulent dans la file depuis trois jours |
| Ce que le schéma aurait dû montrer | La file, et le fait que le producteur ne sait pas si quelqu'un consomme |
| Comment le reconnaître | **Aucune erreur nulle part** — chaque composant fait exactement ce qu'on lui demande |
| Concevoir différemment | Superviser **la taille de la file et l'âge du plus ancien message**, pas l'état des services |

⚠️ **C'est le scénario le plus caractéristique de l'asynchrone** : le découplage a parfaitement fonctionné. **A n'a jamais été affecté par la panne de B — et c'est exactement le problème.**

🔥 **SCÉNARIO — le rejeu produit des doublons**

| Question | Réponse |
|---|---|
| Symptôme | Après un incident, des opérations métier apparaissent en double |
| Hypothèse naïve | « Un bug applicatif » |
| Dépendance réelle | **Des messages ont été rejoués**, et le consommateur n'était pas idempotent |
| Ce que le schéma aurait dû montrer | Rien — c'est une propriété du consommateur, pas de la topologie |
| Concevoir différemment | **Chaque consommateur doit pouvoir reconnaître un message déjà traité** |

#### Quand choisir l'asynchrone

| Le besoin | Modèle |
|---|---|
| L'utilisateur attend le résultat | **Synchrone** |
| Le traitement est long et l'utilisateur n'a pas à attendre | **Asynchrone** |
| Plusieurs services doivent réagir au même événement | **Asynchrone**, publication/abonnement |
| La charge arrive par pointes | **Asynchrone**, la file amortit |
| Le résultat doit être cohérent immédiatement | **Synchrone** |
| Le service appelé est peu fiable ou lent | **Asynchrone**, pour le découpler |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Découpler la disponibilité de deux services | **Un courtier à exploiter, et dont tout dépend** |
| Absorber les pointes de charge | Une file à surveiller · **une accumulation silencieuse possible** |
| Permettre plusieurs consommateurs | L'émetteur ne sait plus ce qu'il déclenche |
| Réessayer sans perdre | **Des doublons à gérer dans chaque consommateur** |
| Rejouer l'historique | Un stockage de données à part entière, avec ses obligations |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est asynchrone » | Un intermédiaire porte les messages | **Que se passe-t-il si le consommateur est arrêté ?** |
| « Il y a du retard dans la queue » | Accumulation | **Depuis quand ? Quel est l'âge du plus ancien message ?** |
| « On a mis un retry » | Réessai automatique | **Le consommateur est-il idempotent ?** Sinon, doublons |
| « C'est parti dans la DLQ » | File d'échecs | **Qui la regarde ? Depuis combien de temps ?** |
| « On publie un événement » | Publication/abonnement | **Combien de services l'écoutent ? L'émetteur ne le sait pas** |
| « Le broker est down » | Le courtier est indisponible | **Les messages en attente étaient-ils persistés ?** |

🏭 **TROIS TAILLES** — Atelier Martin : aucun courtier, **et aucune contrainte ne le justifierait**. HELIOMED : une file pour les remontées de dispositifs médicaux, **parce que les appareils émettent en continu et que le traitement ne doit pas les bloquer**. Novaris : un bus d'événements central, **parce que sept systèmes doivent réagir à une même commande** — et c'est la contrainte, pas la taille.

### 42.5 Les fonctions

| | |
|---|---|
| **Ce que c'est** | Du code exécuté à la demande, sans serveur visible |
| **Ce qui change en lecture** | Il n'y a **rien à dessiner** entre les appels |
| **Le point de rupture** | La plateforme qui les exécute, et les services qu'elles appellent |
| **Ce qui devient difficile** | Savoir ce qui existe : une fonction créée n'apparaît nulle part |

⚠️ **Deux propriétés qui surprennent** :

**Le démarrage à froid.** Une fonction qui n'a pas été appelée depuis un moment met plus longtemps à répondre — le temps que la plateforme la charge. **Cela change le comportement observé selon la fréquence d'appel**, et rend le diagnostic déroutant.

**L'absence de limite naturelle.** Une fonction peut être appelée un million de fois sans que rien ne l'empêche — sauf ce qu'elle appelle derrière. **Une base dimensionnée pour cent connexions simultanées ne survit pas à mille fonctions déclenchées ensemble.** La contrainte s'est déplacée, elle n'a pas disparu.

### 42.6 Le service en ligne, boîte noire sur votre schéma

**Un cas très répandu dans les architectures modernes**, et le §38.2 en donne la représentation : modèle B, la boîte noire avec son interface documentée.

**Les cinq questions, reprises du §38.3 et complétées** :

| Question | Pourquoi elle compte |
|---|---|
| Que peut-il atteindre chez nous ? | Souvent : l'annuaire, par fédération |
| Que faisons-nous s'il tombe ? | **Aucune action possible de votre part** |
| Comment s'authentifie-t-il ? | Fédération, jeton, clé d'interface |
| **Où sont nos données chez lui ?** | La question qu'on ne pose qu'après l'incident |
| **Que se passe-t-il si nous partons ?** | La réversibilité — presque jamais évaluée à la souscription |

⚠️ **La différence fondamentale avec un composant sur site** : **vous ne pouvez agir sur aucune de ses couches internes.** Vous ne le corrigez pas, vous ne le redondez pas, vous n'observez pas son infrastructure.

📌 **Mais les cinq actions du chapitre 43 ne sont pas toutes indisponibles pour autant** — elles se déplacent :

| Action | Dans l'infrastructure du fournisseur | **Ce que vous pouvez malgré tout** |
|---|---|---|
| **Observer** | ❌ | Les journaux d'audit du service, s'il en expose · les appels par interface |
| **Filtrer** | ❌ | Restreindre les origines autorisées · un dispositif intermédiaire d'accès |
| **Authentifier** | ❌ | **Entièrement** : c'est vous qui décidez du fournisseur d'identité et du second facteur |
| **Segmenter** | ❌ | Cloisonner par droits et par espaces, pas par réseau |
| **Journaliser** | ❌ | Récupérer les journaux exposés, et les collecter chez vous |

> **La formulation exacte** : vous perdez le **contrôle de l'infrastructure**, pas toute capacité d'action. Ce qui vous reste est **au niveau de la configuration, des identités et des données** — et c'est loin d'être rien.

⚠️ **Ce qui varie énormément d'un service à l'autre** : la richesse des journaux exposés, la granularité des droits, et la possibilité d'exiger un second facteur. **Ce sont des critères de choix**, et ils s'évaluent avant de souscrire — pas après.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a découpé en microservices » | Plusieurs services indépendants | **Combien d'appels sur le chemin d'une requête ? Que se passe-t-il si l'un est lent ?** |
| « C'est du serverless » | Des fonctions | **Qu'appellent-elles ? La base derrière tient-elle la charge ?** |
| « C'est un SaaS » | Un service en ligne | **Que peut-il atteindre chez nous ?** |
| « L'API est down » | Un service ne répond plus | Le vôtre, ou celui d'un tiers ? La réponse change tout |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Faire évoluer chaque service indépendamment | **Le réseau devient un composant du système** |
| Mettre à l'échelle par service | Des délais, des réessais, une cohérence à concevoir |
| Ne plus exploiter de serveur | **Une dépendance totale à une plateforme** |
| Consommer un service prêt à l'emploi | **Aucune action possible sur son infrastructure** — tout se joue en configuration |

---

> ### 🎓 À ce stade des Parties VI et VII, vous savez…
>
> ✓ appliquer **sept passes dans un ordre non négociable**, et produire une lecture d'une page qui se termine par **trois questions, pas un jugement** ;
> ✓ lire quatre architectures de complexité croissante, et **reconnaître une strate ancienne à trois signes convergents** ;
> ✓ que le prestataire d'infogérance est **au cœur de la zone d'administration** alors qu'il est dessiné en nuage à côté du pare-feu ;
> ✓ que la frontière de responsabilité cloud **descend par composant, pas uniformément** — et que la gouvernance des données et des accès reste vôtre, même quand leur mise en œuvre est partagée ;
> ✓ qu'une **ressource cloud sans sauvegarde configurée n'a aucune sauvegarde** ;
> ✓ que le point de fragilité le plus souvent négligé d'une architecture hybride est le lien des **identités**, et qu'il produit les pannes les plus incompréhensibles ;
> ✓ lire un cluster par ses **quatre éléments** — entrée, services, état, plan de contrôle — et non par ses instances ;
> ✓ qu'un schéma de microservices ne se lit pas en entier : **on suit un chemin, pas une carte** ;
> ✓ que sur un service en ligne, **les cinq actions ne s'appliquent pas à son infrastructure** et se déplacent vers la configuration, les identités et les données ;
> ✓ que la **communication asynchrone découple les disponibilités** — et qu'elle produit en échange accumulation silencieuse, doublons, désordre et perte du lien de cause à effet ;
> ✓ distinguer **bloc, fichier et objet**, et surtout **réplication, instantané et sauvegarde** — les trois qu'on confond constamment.
>
> **Ce que vous ne savez pas encore** : où l'on peut agir sur tout cela. C'est l'objet de la Partie VIII, et c'est le raccordement à toute la collection.

---
