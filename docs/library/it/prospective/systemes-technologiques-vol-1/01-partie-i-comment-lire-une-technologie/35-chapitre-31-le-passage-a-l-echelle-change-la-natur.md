---
title: Chapitre 31 — Le passage à l'échelle change la nature du problème
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 31.1 Dérouler les facteurs

Le chapitre 5 a introduit le motif ***le facteur ×1000***. Il est temps de le traiter pour lui-même.

Multiplier le nombre d'unités ne multiplie pas simplement les grandeurs associées. À chaque saut, certaines choses restent proportionnelles, d'autres explosent, d'autres apparaissent, d'autres deviennent impossibles.

| Passage | Ce qui apparaît typiquement |
|---|---|
| 1 → 10 | reproductibilité, documentation, premières pièces de rechange |
| 10 → 1 000 | outillage, contrôle qualité, formation d'opérateurs, logistique |
| 10³ → 10⁶ | approvisionnement en matières, capital d'usine, réseau de maintenance, réglementation, fin de vie |
| 10⁶ → 10⁹ | ressources planétaires, infrastructures, externalités, effets systémiques |

> **P9 — Changer d'échelle peut changer la nature du problème.**

Ce principe n'est pas une métaphore. Il signifie que la liste des conditions bloquantes n'est pas la même à chaque échelle : la condition qui bloque à mille exemplaires n'est presque jamais celle qui bloquait à dix.

## 31.2 Ce qui devient rare

À grande échelle, des ressources qu'on ne comptait pas deviennent contraignantes. Quatre familles, et il faut savoir les inventorier.

**La matière.** Le chapitre 25 l'a établi : l'offre minière ne répond pas avant quinze à vingt ans. Une technologie qui consomme une matière peu produite bute sur ce délai bien avant de buter sur son coût.

**L'énergie.** Une consommation unitaire négligeable multipliée par un milliard cesse de l'être. C'est le calcul le plus simple et le plus souvent omis.

**Les personnes.** Le chapitre 26 : la formation ne s'accélère pas. Techniciens, installateurs, mainteneurs, contrôleurs.

**L'espace et les droits associés.** Foncier, spectre radioélectrique, capacité de raccordement, créneaux, orbites. Ces ressources ont une propriété commune : elles sont **attribuées** par une procédure, et non achetées sur un marché fluide. Leur rareté est donc autant institutionnelle que physique.

**Méthode d'inventaire.** Prenez la consommation unitaire de chaque ressource, multipliez par l'échelle visée, et comparez à la production ou à la disponibilité mondiale actuelle. Si le rapport dépasse quelques pourcents, vous avez trouvé une contrainte. C'est un calcul de chapitre 5, il prend cinq minutes, et il est rarement fait.

## 31.3 Ce qui devient impossible

Certaines pratiques ne survivent pas au changement d'échelle, et leur disparition oblige à changer de méthode.

**La vérification exhaustive.** On peut tester dix exemplaires intégralement. On ne peut pas en tester un million : on échantillonne, on contrôle statistiquement, on surveille en exploitation. C'est un changement de nature du contrôle qualité, pas un ajustement.

**L'intervention individuelle.** Corriger un problème sur dix objets se fait manuellement. Sur un million, il faut une procédure, une logistique, un financement — et le chapitre 24 a montré ce que coûte un rappel.

**La connaissance directe.** À petite échelle, quelques personnes savent tout du système. À grande échelle, personne n'a la vue d'ensemble — c'est exactement la structure des chaînes d'approvisionnement du chapitre 25, et elle est générale.

## 31.4 Ce qui apparaît

Des problèmes absents à petite échelle deviennent structurants.

**La logistique**, qui peut dépasser le coût de production.

**La maintenance**, dont le chapitre 24 a montré qu'elle borne le déploiement par le nombre de techniciens disponibles.

**La fin de vie.** À petite échelle, on ne s'en occupe pas. À grande échelle, le volume de déchets devient un problème réglementaire, économique et parfois un gisement de matières — mais avec le décalage temporel de la durée de vie du produit, soit une à deux décennies.

**Les externalités.** Ce qui était négligeable unitairement devient mesurable : consommation d'eau, occupation des sols, émissions, congestion, bruit. Une externalité devient un enjeu politique dès qu'elle devient mesurable localement, et c'est alors une condition ⑧.

## 31.5 Ce qui se retourne : les effets rebond

Le chapitre 7 a présenté le paradoxe de Jevons comme une heuristique. Voici son usage rigoureux.

**Le mécanisme.** Améliorer l'efficacité d'usage d'une ressource réduit le coût de son usage, ce qui augmente la quantité d'usage. L'effet net sur la consommation totale dépend de l'ampleur de cette augmentation.

**Trois cas possibles**, et il est essentiel de ne pas les confondre :

* **rebond partiel** — l'usage augmente, mais moins que le gain d'efficacité : la consommation totale baisse quand même. C'est le cas le plus fréquent ;
* **rebond total** — l'augmentation compense exactement le gain ;
* **rebond supérieur** — la consommation totale augmente. C'est le cas Jevons proprement dit, et il est plus rare qu'on ne le dit.

**La règle d'usage.** Le rebond n'est ni une fatalité ni une objection universelle. C'est une **question à poser** : *si le coût d'usage baisse d'un facteur N, de combien l'usage augmente-t-il ?* La réponse dépend de la saturation de la demande. Quand un besoin est proche de la saturation, le rebond est faible. Quand il ne l'est pas, il peut être considérable.

**Application à un cas contemporain.** L'amélioration de l'efficacité énergétique du calcul est réelle et continue. La demande de calcul, elle, n'est manifestement pas saturée. C'est pourquoi les gains d'efficacité par opération n'ont pas fait baisser la consommation totale des infrastructures de calcul. Il n'y a là aucun paradoxe : il y a une demande non saturée rencontrant une baisse du coût unitaire. ⏱

## 31.6 Méthode : dérouler un facteur mille sur le papier

Exercice systématique, applicable à toute technologie, en cinq questions.

1. **Quelles ressources par unité ?** Matière, énergie, eau, surface, temps humain.
2. **Multiplier par l'échelle visée.** Comparer à la disponibilité mondiale actuelle.
3. **Qu'est-ce qui cesse d'être possible ?** Vérification, intervention, connaissance directe.
4. **Qu'est-ce qui apparaît ?** Logistique, maintenance, fin de vie, externalités.
5. **Où l'usage augmente-t-il ?** Effet rebond, saturation ou non de la demande.

Si les cinq réponses sont rassurantes, la technologie passe à l'échelle. En pratique, une ou deux ne le sont jamais, et ce sont elles qui détermineront la trajectoire réelle.

## 31.7 Le facteur mille déroulé : un exemple complet

La méthode de 31.6 mérite d'être vue en fonctionnement. Prenons un objet abstrait, pour que l'exercice reste transférable : un **dispositif électronique autonome déployé sur le terrain**, alimenté par batterie, doté de quelques capteurs et d'une liaison radio. Peu importe ce qu'il mesure.

**Hypothèses de départ**, volontairement rondes : masse 200 g, dont 50 g de batterie ; consommation moyenne 0,1 W ; durée de vie 5 ans ; une intervention de maintenance par an. Déploiement actuel : 1 000 unités. Cible : 1 000 000 d'unités.

### Question 1 — Les ressources par unité, multipliées par l'échelle

| Ressource | Par unité | À 10⁶ unités | Comparaison |
|---|---|---|---|
| Masse totale | 200 g | 200 tonnes | modeste |
| Masse de batteries | 50 g | 50 tonnes | à comparer à la production mondiale des matériaux concernés |
| Puissance moyenne | 0,1 W | 100 kW en continu | modeste : l'ordre de grandeur d'un petit bâtiment |
| Énergie sur 5 ans | 4,4 kWh | 4,4 GWh | modeste |

**Première conclusion, contre-intuitive :** l'énergie n'est pas le problème. Un dispositif qui consomme 0,1 W multiplié par un million reste une charge de 100 kW. **Le calcul de cinq lignes vient d'éliminer l'hypothèse la plus intuitive.**

### Question 2 — Ce qui devient rare

**La maintenance.** Une intervention par unité et par an, à un million d'unités, fait un million d'interventions annuelles. À dix interventions par jour et par technicien, sur 220 jours ouvrés, cela représente environ **450 techniciens à temps plein**. C'est le goulet réel, et il n'était visible dans aucune caractéristique du produit.

**Le remplacement.** Sur une durée de vie de cinq ans, un parc d'un million d'unités impose de remplacer 200 000 unités par an en régime permanent — soit une production continue, une logistique de retour et une filière de fin de vie.

**Le spectre.** Un million d'émetteurs radio dans une même bande, sur un territoire donné, pose une question de partage de la ressource. Le chapitre 13.2 l'a établi : le spectre est attribué, non acheté. **C'est une rareté institutionnelle, et elle apparaît à cette échelle seulement.**

### Question 3 — Ce qui cesse d'être possible

La vérification individuelle avant déploiement. Le diagnostic unitaire à distance sans une infrastructure dédiée. Et surtout : **la connaissance de l'état réel du parc.** À mille unités, on sait lesquelles fonctionnent. À un million, on ne le sait qu'à travers un système de supervision — qui devient lui-même un objet critique.

### Question 4 — Ce qui apparaît

La logistique de déploiement et de retour. La gestion des versions logicielles sur un parc hétérogène. Le traitement de 200 tonnes de déchets électroniques par cycle de renouvellement, dont 50 tonnes de batteries — soumises à des règles de transport et de traitement spécifiques. Et une surface d'attaque constituée d'un million de points, dont aucun n'est physiquement protégé.

### Question 5 — L'usage augmente-t-il ?

Si le dispositif devient dix fois moins cher, le déploiement s'arrête-t-il à un million ? Le chapitre 31.5 impose de poser la question. Pour un capteur dont la valeur croît avec la densité de mesure, la demande n'est pas saturée : **la baisse de coût produirait un déploiement plus large, donc davantage de maintenance, donc davantage de techniciens.** Le goulet ne se desserre pas, il s'aggrave.

### Conclusion de l'exercice

**Le goulet est la maintenance, et il n'était visible dans aucune spécification technique.** Ni l'énergie, ni la masse, ni le coût unitaire, ni la performance du capteur ne le laissaient prévoir. Il est apparu en multipliant une hypothèse d'exploitation — une intervention par an — par l'échelle visée.

**Les deux conséquences de conception qui en découlent** sont maintenant évidentes, et elles n'ont rien à voir avec le capteur : réduire le nombre d'interventions par unité et par an, quitte à surdimensionner la batterie ou à accepter une performance moindre ; et rendre le dispositif jetable plutôt que réparable, ce qui déplace le problème vers la fin de vie.

**Ce que cet exercice démontre.** Dérouler un facteur mille prend quinze minutes, ne demande aucune connaissance du domaine, et déplace la conversation de la performance vers l'exploitation. **C'est probablement l'usage le plus rentable de tout ce volume.**

🧪 **Lab 14 — Le facteur mille**

**Objectif.** Identifier les contraintes qui apparaissent au changement d'échelle et distinguer celles qui sont physiques de celles qui sont institutionnelles.
**Durée.** 90 minutes. **Difficulté.** 3/3. **Prérequis.** Chapitres 5, 25, 26, 31.
**Contexte.** Une technologie actuellement déployée à quelques milliers d'exemplaires vous est présentée, avec ses caractéristiques unitaires.
**Travail demandé.** (a) Dérouler les cinq questions de 31.6 pour un déploiement à un million d'unités. (b) Identifier les deux contraintes les plus sévères et dire si elles sont physiques, industrielles ou institutionnelles. (c) Estimer l'effet rebond en justifiant par la saturation ou non de la demande. (d) Reprendre l'exercice à dix millions et dire ce qui change qualitativement. (e) Identifier une contrainte qui, elle, ne change pas avec l'échelle.
**Livrable.** Deux pages, calculs apparents.
**Éléments attendus.** En (d), le point recherché est qu'un nouveau facteur dix ne fait pas apparaître les mêmes contraintes que le précédent — souvent, une contrainte devient dominante alors qu'elle était négligeable. En (e), les bonnes réponses sont généralement des contraintes physiques unitaires : rendement, densité énergétique, latence. Une copie qui n'en trouve aucune n'a pas distingué ce qui s'additionne de ce qui ne s'additionne pas.

🎓 **À ce stade, vous savez…** dérouler un facteur d'échelle sur cinq dimensions ; inventorier les ressources qui deviennent rares et distinguer rareté physique et rareté attribuée ; identifier ce qui cesse d'être possible ; poser correctement la question du rebond en termes de saturation de la demande.

---
