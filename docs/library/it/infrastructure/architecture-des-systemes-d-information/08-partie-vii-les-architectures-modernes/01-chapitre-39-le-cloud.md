---
title: Chapitre 39 — Le cloud
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VII — Les architectures modernes
  - index.md
---

## 39.1 La question qui structure tout le chapitre

> **Qu'est-ce qui disparaît du schéma sans disparaître du système ?**

C'est la seule question utile pour lire une architecture cloud. Le fournisseur masque une partie de l'infrastructure — mais le réseau, les identités, les données, les dépendances, les secrets et la résilience **existent toujours**. Ils ont simplement changé de forme, et souvent de responsable.

## 39.2 Ce qui change et ce qui ne change pas

| Ne change pas | Change |
|---|---|
| Les trois familles de flux | **Qui exploite quoi** |
| Les points de rupture | Leur emplacement et leur visibilité |
| La nécessité d'authentifier | Le composant qui le fait |
| Le fait que la donnée soit quelque part | **Où « quelque part » se trouve** |
| La sédimentation | Elle **s'accélère** — le provisionnement est instantané |

⚠️ **La dernière ligne mérite d'être développée.** Créer une machine prenait des semaines ; cela prend des minutes. **La sédimentation du chapitre 4 s'accélère donc d'un ordre de grandeur** : des ressources créées pour un essai, jamais supprimées, jamais inventoriées. C'est le sujet central du volume Asset Management.

## 39.3 La frontière de responsabilité

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

## 39.4 Six comparaisons, et ce que chacune coûte

**C'est le cœur du chapitre.** Pour chaque transformation : *qu'est-ce que je n'exploite plus ? qu'est-ce que je dois toujours concevoir ? quelle nouvelle dépendance ai-je achetée ?*

### A — Sur site contre infrastructure louée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Matériel, alimentation, virtualisation | **Système, correctifs, sauvegardes, réseau, identités** | La disponibilité du fournisseur · sa facturation à l'usage |

⚠️ **Ce qui surprend le plus** : les correctifs système restent entièrement à votre charge. **Louer une machine ne la maintient pas.**

### B — Infrastructure louée contre plateforme managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Système, correctifs, une partie de la disponibilité | **L'application, les données, les accès, l'architecture** | Le calendrier de version du fournisseur · **une réversibilité faible** |

⚠️ **Le coût caché de B** : le fournisseur décide quand la version change. **Vous n'êtes plus maître du calendrier**, ce qui est un gain d'exploitation et une perte de maîtrise.

### C — Machine virtuelle contre conteneur

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un système par application | **L'image, les dépendances embarquées, l'orchestration** | **Un système distribué complet** — §41 |

⚠️ **Le piège** : le conteneur ne supprime pas le système, **il le déplace dans l'image**. Une image jamais reconstruite embarque des composants jamais corrigés. La maintenance n'a pas disparu, elle a changé de main — et souvent, de personne responsable.

### D — Base auto-hébergée contre base managée

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Correctifs, sauvegardes automatiques, réplication | **Le schéma de données, les accès, la performance** | Le calendrier de version · **des limitations sur ce qu'on peut faire** |

⚠️ **Ce qu'on découvre après** : certaines opérations d'administration ne sont plus possibles. **Le confort a un prix qui se paie en flexibilité.**

### E — Monolithe contre microservices

| | Je n'exploite plus | Je conçois toujours | Nouvelle dépendance |
|---|---|---|---|
| | Un déploiement couplé pour tout | **Les contrats entre services, la cohérence des données** | **Le réseau devient un composant du système** — §42.1 |

⚠️ **Le changement de nature** : entre deux microservices, un appel **traverse le réseau**, et hérite donc de tous ses modes de défaillance — perte, latence, duplication, réponse jamais reçue alors que l'action a eu lieu. Chaque appel devient un point de rupture potentiel, **qui n'existait pas dans le monolithe**.

### F — Tunnel chiffré contre interconnexion dédiée

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

## 39.5 Ce qui devient invisible

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

## 39.6 Ce qui reste entièrement à votre charge

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
