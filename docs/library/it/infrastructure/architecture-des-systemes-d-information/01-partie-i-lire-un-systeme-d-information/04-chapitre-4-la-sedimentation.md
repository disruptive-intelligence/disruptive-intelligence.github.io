---
title: Chapitre 4 — La sédimentation
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

> Le chapitre qui explique pourquoi les systèmes d'information sont « bizarres ». Il évite plus de jugements naïfs que tout le reste du cours.

## 4.1 Aucune architecture n'a été construite d'un bloc

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

## 4.2 Les couches historiques, et comment on les reconnaît

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

## 4.3 Les quatre événements qui sédimentent

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

## 4.4 Comment on lit une architecture sédimentée

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

## 4.5 📌 Ce que la sédimentation n'excuse pas

Le chapitre pourrait produire un excès inverse : tout expliquer par l'histoire et ne rien remettre en cause.

| La sédimentation explique | Elle n'excuse pas |
|---|---|
| Qu'un composant ancien existe | Qu'on ne sache pas ce qu'il fait |
| Qu'une passerelle ait été créée en urgence | Qu'elle ne soit pas documentée douze ans après |
| Qu'une migration soit inachevée | Qu'aucune décision n'ait été prise sur son achèvement |
| Qu'un annuaire hérité subsiste | Qu'on ignore qui y a des droits |

**La distinction** : la sédimentation explique **l'existence** d'un état ; elle n'explique jamais **l'absence de décision** à son sujet. C'est exactement la distinction que fait le volume Maintien en condition de sécurité entre un écart connu et décidé, et un écart ignoré.

## 4.6 🔴 FIL ROUGE — décembre 2025 : pourquoi c'est « bizarre »

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

## Synthèse mentale du chapitre 4

Ce que vous regardez n'est pas une architecture mais un empilement de décisions prises à des époques différentes, par des gens différents, dont la plupart ne travaillent plus là. On ne refait pas propre pour cinq raisons, dont la moins avouée pèse lourd : un système qu'on ne comprend plus ne se remplace pas, on l'entoure. Quatre événements sédimentent — acquisition, migration inachevée, urgence, départ — et l'acquisition est le plus puissant, parce qu'elle ajoute d'un coup une architecture entière conçue ailleurs. Trois questions permettent de lire une architecture sédimentée : qu'est-ce qui ne ressemble pas au reste, qu'est-ce qui devrait être là et n'y est pas, qu'est-ce qui relie deux choses qui ne devraient pas l'être — et chaque anomalie a une date qui explique l'architecture mieux que n'importe quel document. Enfin, la sédimentation explique l'existence d'un état ; elle n'excuse jamais l'absence de décision à son sujet.

**Trois questions de vérification**

1. Un schéma comporte une passerelle qui contredit toutes les bonnes pratiques. Quelle est votre première question, et pourquoi pas votre première critique ?
2. Pourquoi « ils auraient dû refaire propre » est-il presque toujours un jugement naïf ?
3. Quelle est la différence entre ce que la sédimentation explique et ce qu'elle n'excuse pas ?

---
