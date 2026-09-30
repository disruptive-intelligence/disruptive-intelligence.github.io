---
title: Chapitre 42 — Microservices, fonctions et services en ligne
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE VII — Les architectures modernes
  - index.md
---

## 42.1 Pourquoi le schéma explose

**Le mécanisme** : découper une application en dix services indépendants multiplie par dix le nombre de boîtes, et par bien plus le nombre de flux entre elles.

| Architecture | Composants | Flux internes possibles |
|---|---|---|
| Application monolithique | 1 | 0 |
| Trois niveaux | 3 | 2 |
| **Dix microservices** | **10** | **jusqu'à 45** |

**Ce qu'on gagne** : chaque service évolue et se déploie indépendamment. **Ce qu'on perd** : la lisibilité, et la capacité à répondre simplement à *qu'est-ce qui tombe si ceci tombe*.

## 42.2 Le changement de nature qu'on sous-estime

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

## 42.3 Comment on lit malgré tout

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

## 42.4 La communication asynchrone

> **Le modèle que le reste du chapitre n'a pas traité**, et qui change complètement la nature des pannes.

### Le principe

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

### Ce que le découplage fait gagner

**C'est réel, et c'est pourquoi ce modèle existe** :

| Gain | Pourquoi |
|---|---|
| **B peut tomber sans arrêter A** | Le service reste disponible pour l'utilisateur |
| **Absorber une pointe de charge** | La file sert de tampon : A dépose vite, B rattrape ensuite |
| **Plusieurs consommateurs** | On ajoute des instances de B pour traiter plus vite |
| **Plusieurs destinataires** | Un même événement peut intéresser trois services, sans que l'émetteur les connaisse |
| **Découplage des versions** | A et B évoluent séparément |

⚠️ **Le quatrième gain est le plus structurant en architecture** : l'émetteur ne sait pas qui consomme. **Cela signifie qu'on peut ajouter un consommateur sans toucher à l'émetteur** — et aussi qu'**on ne sait plus, en lisant le code de A, ce que son message déclenche**.

### Les sept problèmes qu'on achète

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

### Les trois topologies à reconnaître

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

### Le point de rupture déplacé

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

### Quand choisir l'asynchrone

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

## 42.5 Les fonctions

| | |
|---|---|
| **Ce que c'est** | Du code exécuté à la demande, sans serveur visible |
| **Ce qui change en lecture** | Il n'y a **rien à dessiner** entre les appels |
| **Le point de rupture** | La plateforme qui les exécute, et les services qu'elles appellent |
| **Ce qui devient difficile** | Savoir ce qui existe : une fonction créée n'apparaît nulle part |

⚠️ **Deux propriétés qui surprennent** :

**Le démarrage à froid.** Une fonction qui n'a pas été appelée depuis un moment met plus longtemps à répondre — le temps que la plateforme la charge. **Cela change le comportement observé selon la fréquence d'appel**, et rend le diagnostic déroutant.

**L'absence de limite naturelle.** Une fonction peut être appelée un million de fois sans que rien ne l'empêche — sauf ce qu'elle appelle derrière. **Une base dimensionnée pour cent connexions simultanées ne survit pas à mille fonctions déclenchées ensemble.** La contrainte s'est déplacée, elle n'a pas disparu.

## 42.6 Le service en ligne, boîte noire sur votre schéma

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
