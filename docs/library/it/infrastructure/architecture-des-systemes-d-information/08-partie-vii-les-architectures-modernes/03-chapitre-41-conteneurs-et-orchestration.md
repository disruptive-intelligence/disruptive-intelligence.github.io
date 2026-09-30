---
title: Chapitre 41 — Conteneurs et orchestration
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VII — Les architectures modernes
  - index.md
---

## 41.1 Ce qui change réellement

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

## 41.2 Pourquoi ces schémas sont illisibles

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

## 41.3 Les quatre nouvelles dépendances

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

## 41.4 La découverte de service

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

## 41.5 Trois architectures de cluster

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
