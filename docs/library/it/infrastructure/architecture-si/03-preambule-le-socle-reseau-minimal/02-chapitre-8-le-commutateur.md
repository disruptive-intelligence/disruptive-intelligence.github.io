---
title: Chapitre 8 — Le commutateur
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 8.1 À quoi ça sert

Relier des machines à l'intérieur d'un même segment, et acheminer les échanges de l'une à l'autre **sans les diffuser à toutes**.

**Pourquoi ça existe.** Avant le commutateur, les machines partageaient un même support : chacune voyait tout ce qui passait, et deux machines qui émettaient en même temps se gênaient. Le commutateur résout les deux problèmes d'un coup — il apprend quelle machine est derrière quel port, et n'envoie qu'à la bonne.

**Ce qu'il faut en retenir pour raisonner**, et rien de plus :

> **Un commutateur crée un espace où les machines se joignent directement. Il ne crée aucune frontière de filtrage.**

## 8.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Une trame arrive sur le port 3
   ②  Le commutateur note : « cette machine est derrière le port 3 »
   ③  Il regarde la destination
        ├── il sait où elle est  ──► il envoie sur ce port UNIQUEMENT
        └── il ne sait pas       ──► il envoie sur TOUS les ports
   ④  La réponse lui apprend où se trouve la destination
```


**Trois conséquences en lecture d'architecture** :

| Mécanisme | Conséquence |
|---|---|
| Il **apprend** les emplacements | Une machine déplacée est retrouvée automatiquement |
| Il **diffuse** ce qu'il ne connaît pas | Un segment très large produit du trafic inutile partout |
| Il **ne filtre pas** | Deux machines du même segment se joignent, sauf mécanisme dédié — §24.1 |

## 8.3 Les segments logiques

**Le mécanisme qui change tout, et qu'aucun schéma logique ne montre** : un même commutateur physique peut porter plusieurs segments logiques indépendants. Deux machines branchées côte à côte dans la même baie peuvent être **aussi séparées que si elles étaient dans deux bâtiments**.

```
   UN SEUL COMMUTATEUR PHYSIQUE

   ports 1-8    ─── segment « postes »      ┐
   ports 9-16   ─── segment « serveurs »    ├─ trois segments,
   ports 17-24  ─── segment « supervision » ┘  aucun ne voit les autres

   Pour qu'ils communiquent : il faut un ROUTEUR.
```


⚠️ **Ce que cela impose en lecture** : un schéma physique qui montre un seul commutateur peut décrire une architecture **logiquement segmentée**. Et l'inverse : deux commutateurs dessinés séparément peuvent porter **le même segment**. **La question à poser : combien de segments, et non combien d'équipements.**

## 8.4 Trois architectures, trois usages

```
  A — COMMUTATEUR UNIQUE
      [ commutateur ] ─── 20 machines
      → simple · une panne = tout le site
      → convient quand l'interruption tolérable est large

  B — DEUX COMMUTATEURS EN CASCADE
      [ cœur ] ─── [ étage 1 ]
              └─── [ étage 2 ]
      → une panne d'étage n'affecte qu'un étage
      → une panne du cœur affecte tout · le cœur est le point de rupture

  C — CŒUR REDONDÉ
      [ cœur A ] ══╗
                   ╠═══ [ étage 1 ] [ étage 2 ]
      [ cœur B ] ══╝
      → une panne de cœur est absorbée
      → deux équipements à configurer de façon cohérente
      → ⚠️ **Principe de preuve** : sont-ils sur la même alimentation ?
```


**La contrainte qui fait passer de A à C** n'est pas le nombre de machines : c'est **la durée d'interruption tolérable comparée au délai de remplacement d'un équipement**. Si remplacer prend quatre heures et qu'une journée d'arrêt est acceptable, A suffit.

## 8.5 Ce qu'il fait à la donnée

Il la transporte. Pour accomplir sa fonction, il interprète les informations d'adressage de niveau liaison — **sans avoir besoin d'interpréter le contenu applicatif**. Il voit passer ce qui traverse le segment, ce qui en fait un point d'observation possible — chapitre 43.

## 8.6 S'il disparaît

| Ce qui tombe | Délai | Compréhensible pour l'utilisateur ? |
|---|---|---|
| Tout ce qui y est raccordé | Immédiat | ✅ « plus de réseau ici » |

**C'est la panne la plus localisée et la plus totale du cours** : un segment entier disparaît, et le reste du système ne s'en aperçoit pas — **sauf s'il en dépend**.

🔥 **SCÉNARIO — le commutateur de l'étage tombe**

| Question | Réponse |
|---|---|
| Symptôme observé | Quarante personnes sans réseau, le reste du site fonctionne |
| Hypothèse naïve | « Panne réseau générale » |
| Dépendance réelle | Ces quarante postes · **et tout service hébergé sur ce segment** |
| Ce que le schéma aurait dû montrer | Quels serveurs sont sur ce segment |
| Concevoir différemment | Ne pas mélanger postes et serveurs sur un même segment |

## 8.7 Sur un schéma

Souvent absent. Quand il figure, c'est sur une vue physique. Sur une vue logique, il est **implicite** : deux machines dessinées dans la même zone sont supposées reliées.

⚠️ **Le piège de lecture** : l'absence de commutateur ne signifie pas qu'il n'y en a pas — elle signifie que la vue ne s'y intéresse pas. **La question « qui peut joindre qui à l'intérieur d'une zone » reste ouverte**, et la réponse par défaut est « tout le monde ».

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut probablement dire | À vérifier avant de le croire |
|---|---|---|
| « C'est sur le même switch » | Les machines sont sur le même segment | **Même équipement ≠ même segment.** Combien de segments logiques ? |
| « On a mis un VLAN » | Un segment logique a été créé | Le routage entre segments est-il filtré, ou juste routé ? |
| « Le cœur de réseau » | Le commutateur central | Est-il redondé ? Les deux exemplaires partagent-ils l'alimentation ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Relier des machines proches efficacement | Un équipement à alimenter, corriger, surveiller |
| Segmenter logiquement sans recâbler | **Une configuration à maintenir, souvent non documentée** |
| Redonder le cœur | Deux configurations à tenir cohérentes · un mécanisme de bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : 2, dont un pour l'atelier. HELIOMED : une trentaine, dont deux en cœur redondé. Novaris : plusieurs centaines. **La contrainte qui fait passer de 2 à 30 n'est pas le nombre de salariés, c'est le nombre de bâtiments et de segments à isoler.**

---
