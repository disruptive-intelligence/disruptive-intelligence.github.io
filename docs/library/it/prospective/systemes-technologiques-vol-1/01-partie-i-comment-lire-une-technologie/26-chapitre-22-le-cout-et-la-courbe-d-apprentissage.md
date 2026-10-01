---
title: Chapitre 22 — Le coût et la courbe d'apprentissage
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 22.1 Décomposer un coût avant de le discuter

« C'est trop cher » n'est pas une analyse. La question utile est : *cher en quoi, et cette part peut-elle baisser ?*

Six postes suffisent à structurer presque n'importe quel coût industriel.

| Poste | Peut-il baisser ? | Par quel mécanisme |
|---|---|---|
| **Matière** | partiellement | substitution, réduction de quantité, recyclage — mais un plancher existe |
| **Énergie de fabrication** | oui | rendement de procédé, prix de l'énergie |
| **Main-d'œuvre** | oui | automatisation, apprentissage, délocalisation |
| **Capital amorti** | fortement | augmentation du volume sur le même outil |
| **Non-qualité** | fortement | amélioration du rendement de fabrication |
| **Frais fixes hors production** | oui | volume |

Cette décomposition a une vertu immédiate : elle vous dit **si une baisse de coût est plausible**. Un objet dont 70 % du coût est de la matière première ne baissera pas d'un facteur dix. Un objet dont 70 % du coût est du capital amorti et de la non-qualité peut baisser énormément, sans qu'aucune découverte scientifique soit nécessaire.

**Application immédiate.** Devant une promesse de baisse de coût, demandez la décomposition. Si personne ne peut la fournir, la promesse n'a pas de mécanisme, et le chapitre 7 vous a appris ce que vaut une régularité sans mécanisme.

## 22.2 Capital et coût marginal : deux économies opposées

Deux objets peuvent avoir le même coût moyen et se comporter de manière opposée.

**Économie dominée par le coût marginal.** Chaque unité supplémentaire coûte à peu près autant que la précédente. La production est flexible, le risque est faible, mais le volume n'apporte pas grand-chose. Beaucoup d'activités artisanales et de services entrent dans cette catégorie.

**Économie dominée par le capital.** L'essentiel du coût est engagé avant la première unité : usine, outillage, qualification, développement. Le coût unitaire dépend alors presque entièrement du volume sur lequel on amortit. C'est le cas des semi-conducteurs, de l'automobile, de l'aéronautique, du médicament.

Trois conséquences majeures découlent de cette seconde structure, et elles gouvernent une grande partie de ce cours.

**Le volume devient une arme.** Celui qui produit plus amortit mieux, donc vend moins cher, donc produit plus. Nous retrouverons cette boucle en 22.3.

**Le taux d'utilisation devient critique.** Une usine à moitié pleine produit à un coût unitaire très supérieur. C'est pourquoi les industries capitalistiques préfèrent souvent baisser leurs prix plutôt que réduire leur cadence.

**Le risque change de nature.** Il faut engager le capital avant de savoir si la demande existe. C'est la raison pour laquelle la condition ⑤ du chapitre 3 — la demande — n'est pas une préoccupation de commercial mais une condition technique de faisabilité : sans visibilité sur la demande, personne ne construit l'usine, et sans usine, le coût ne baisse jamais.

## 22.3 La loi de Wright

En 1936, l'ingénieur aéronautique Theodore Wright publie une observation faite sur la production d'avions : à chaque doublement du nombre cumulé d'unités produites, le coût unitaire baisse d'un pourcentage à peu près constant — de l'ordre de 15 % dans son cas.

Ce pourcentage s'appelle le **taux d'apprentissage**. La variable explicative n'est pas le temps, ni l'effort de recherche : c'est la **production cumulée**.

**Statut de cette relation.** Régularité empirique, au sens du chapitre 7. Ni loi physique, ni heuristique vague. Elle repose sur une base de données publique constituée à l'Institut de Santa Fe couvrant plus de cinquante technologies sur des décennies, et elle a fait l'objet de travaux statistiques sérieux, notamment ceux de Farmer et Lafond (2016) sur sa capacité prédictive. Elle décrit bien, elle prédit correctement en moyenne, et elle comporte une dispersion réelle qu'il ne faut pas masquer.

**Le cas canonique : le photovoltaïque.** Sur plus de quatre décennies, le prix des modules a baissé d'environ 20 % à chaque doublement de la capacité cumulée installée, passant de l'ordre de 100 dollars par watt au milieu des années 1970 à moins d'un dollar par watt, soit une baisse de plus de 99 %. ⏱ C'est ce mécanisme que les projections évoquées au chapitre 1 n'intégraient pas correctement : en supposant un taux d'apprentissage trop faible, on obtient mécaniquement, sur vingt ans, un écart d'un ordre de grandeur.

**Un cas qui apprend la prudence : le lithium-ion.** Ziegler et Trancik ont réexaminé en 2021 les données de coût des batteries lithium-ion et relevé que la littérature antérieure rapportait des taux d'apprentissage allant d'environ 14 % à 30 % selon les sources, leurs propres estimations se situant autour de 20 à 27 % selon le périmètre retenu. Cette dispersion n'est pas anecdotique : appliquée sur plusieurs doublements, elle produit des projections qui diffèrent de plus d'une décennie sur la date d'atteinte d'un seuil de prix donné.

**Ce qu'il faut en retenir.** Le mécanisme est robuste ; le paramètre ne l'est pas. Annoncer « le coût suivra la loi de Wright » est une affirmation utile ; annoncer « donc le prix sera de X en 2035 » masque une incertitude qui se compte en années.

**Pourquoi ça marche.** Trois mécanismes concourent, et ils se distinguent des simples économies d'échelle. L'apprentissage des opérateurs et des ingénieurs de procédé. L'amélioration incrémentale de la conception, guidée par ce qu'on observe en produisant. Et l'amélioration du rendement de fabrication — le paramètre du chapitre 10, qui à lui seul peut transformer l'économie d'un produit.

> **P5 — La production est elle-même un mécanisme d'innovation : l'expérience cumulée fait souvent baisser les coûts plus fortement que la conception seule.**

## 22.4 Où la loi de Wright ne s'applique pas

C'est la partie la plus utile de ce chapitre, parce qu'elle est la moins souvent enseignée.

La loi de Wright suppose une production répétée d'objets similaires en quantité. Elle ne s'applique pas, ou mal, dans plusieurs situations reconnaissables.

**Les objets de très grande taille produits en très petit nombre.** Une centrale, un barrage, un grand ouvrage d'art, un lanceur à l'unité : la production cumulée reste faible, les unités diffèrent, et le site impose ses contraintes. On observe alors peu d'apprentissage, voire l'inverse.

**Les coûts qui ont augmenté avec l'expérience.** Plusieurs analyses relèvent des taux d'apprentissage négatifs sur certaines filières, notamment le nucléaire civil aux États-Unis et en France. **Cette affirmation est débattue** — sa portée générale est contestée par des travaux de périmètre plus large — et le chapitre 38.1 instruit la controverse. Ce qui n'est pas contesté est plus étroit et suffit ici : **dans aucun pays, ce régime de production n'a produit l'effondrement de coût observé sur les objets manufacturés en série.** Les explications avancées se recoupent : durcissement progressif des exigences réglementaires après incidents, conception spécifique à chaque site, perte de savoir-faire entre deux vagues de construction espacées de décennies, allongement des délais qui renchérit le financement. Le chapitre 29 reviendra sur le premier de ces facteurs, et le chapitre 24 sur le troisième.

**Ce que ce contre-exemple enseigne.** L'apprentissage n'est pas une propriété du temps ni de la technologie : c'est une propriété du **régime de production**. La même filière conçue en objets modulaires produits en série et conçue en ouvrages uniques n'a pas la même trajectoire de coût. C'est pourquoi la question « peut-on modulariser ? » est, dans beaucoup de domaines, une question de coût déguisée en question d'ingénierie.

**Les objets à forte composante de matière première.** Quand la matière domine le coût, l'apprentissage bute sur le prix de la matière, qui obéit à d'autres dynamiques.

**Le test pratique.** Devant une projection de baisse de coût, posez trois questions : *combien d'unités identiques seront produites ? qui les produit, de façon répétée ? et quelle part du coût est réellement soumise à l'apprentissage ?*

## 22.5 La courbe ne s'amorce pas toute seule

Voici le paradoxe central de ce chapitre, et il explique un nombre considérable d'échecs.

Le coût baisse avec le volume cumulé. Mais le volume ne vient que s'il existe des acheteurs. Et au début, le prix est prohibitif pour le marché visé. La technologie est donc **prisonnière de son propre coût** : elle a besoin de production pour devenir abordable, et d'être abordable pour être produite.

```text
   coût élevé → pas de demande → pas de volume → pas d'apprentissage → coût élevé
```


Trois sorties existent, et une seule est passive.

**La niche à haute tolérance au coût.** Un domaine où l'on paie très cher un gain marginal : spatial, défense, médical, recherche, compétition, luxe. Ces clients ne sont pas un marché final, ils sont une **rampe d'accès** : ils financent les premiers doublements. Le photovoltaïque a suivi ce chemin, ses premières applications significatives étant des sites isolés et des usages spatiaux, avant tout marché de masse.

**La demande créée par décision publique.** Norme contraignante, obligation d'achat, tarif garanti, commande publique. Le mécanisme est celui de la deuxième boucle du chapitre 3, et il est traité au chapitre 28. Il fonctionne — c'est un fait observable — et il échoue quand la demande garantie s'interrompt avant que la boucle de coût soit auto-entretenue.

**Le capital patient.** Un investisseur accepte de financer des années de production déficitaire en pariant sur l'atteinte du seuil. C'est la voie la plus risquée et la plus dépendante des conditions de financement.

**Conséquence analytique.** Devant une technologie chère, la question n'est pas « quand sera-t-elle abordable ? » mais **« quelle est sa rampe d'accès ? »**. Si aucune des trois sorties n'est identifiable, la baisse de coût n'a pas de chemin, quelle que soit la qualité de la technologie.

## 22.6 Quand la courbe s'arrête

Une courbe d'apprentissage ne descend pas indéfiniment. Trois planchers apparaissent, et savoir lequel approche est une information de grande valeur.

**Le plancher matière.** Le coût ne peut pas descendre sous celui des matériaux consommés. Quand ce plancher approche, la seule voie restante est de réduire la quantité de matière ou de la remplacer, ce qui est un problème de conception, pas de production.

**Le plancher de composition.** Quand un composant devient très bon marché, il cesse de dominer le coût du système. La baisse du prix du module photovoltaïque a ainsi déplacé le coût vers l'installation, la structure, l'onduleur, le raccordement et le foncier — postes qui suivent des dynamiques bien plus lentes. **Poursuivre la baisse du composant ne change alors presque plus le coût final.** C'est un déplacement de goulet, au sens du chapitre 32.

**Le plancher physique.** Certaines contraintes du chapitre 8 fixent une limite : un rendement ne dépasse pas 100 %, une quantité de matière ne descend pas sous ce qu'exige la fonction.

**Le signal à surveiller.** Quand la part du composant dans le coût système passe sous le tiers, l'attention doit se déplacer. Continuer à suivre le prix du composant devient une erreur d'analyse — vous suivez une variable qui ne commande plus rien.

## 22.7 Coût unitaire, coût total, coût système

Trois niveaux de coût, trois conclusions possibles sur le même objet.

**Le coût d'acquisition** — le prix affiché. C'est celui qui circule et le moins informatif.

**Le coût total de possession** — acquisition, énergie, maintenance, pièces, formation, immobilisation, fin de vie. Il inverse fréquemment les classements. Un objet plus cher à l'achat et moins cher à l'usage gagne dans les mains d'un acheteur qui raisonne sur dix ans, et perd face à un acheteur qui raisonne sur son budget annuel — ce qui explique pourquoi la structure de décision de l'acheteur fait partie de l'analyse technologique.

**Le coût système** — ce que l'adoption impose au reste de l'ensemble. Une source d'électricité intermittente et bon marché peut exiger du stockage, du réseau supplémentaire et des moyens de secours, dont le coût n'apparaît pas dans son prix de production. Symétriquement, une technologie plus chère mais qui supprime une infrastructure entière peut être moins coûteuse au niveau système.

**La règle :** ne jamais comparer deux technologies au même niveau de coût sans vérifier que le périmètre est identique. Les comparaisons les plus trompeuses de tout le débat technologique viennent d'un simple décalage de périmètre.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « Les coûts vont s'effondrer » | extrapolation, souvent sans mécanisme | quelle part du coût baisse, et par quel mécanisme ? |
| « On atteindra la parité en 20XX » | projection sensible au taux d'apprentissage retenu | quel taux avez-vous pris, et que donne-t-il à ±5 points ? |
| « C'est moins cher que l'alternative » | comparaison de coûts d'acquisition | à quel périmètre — acquisition, possession, ou système ? |
| « Il suffit d'industrialiser » | suppose la rampe d'accès résolue | qui achète les premières unités, et à quel prix ? |
| « On a des économies d'échelle » | souvent confondu avec l'apprentissage | échelle sur le même outil, ou apprentissage par production cumulée ? |

🧪 **Lab 11 — Trajectoire de coût**

**Objectif.** Évaluer la plausibilité d'une baisse de coût annoncée.
**Durée.** 75 minutes. **Difficulté.** 3/3. **Prérequis.** Chapitres 5, 11, 22.
**Contexte.** Deux technologies vous sont présentées avec une projection de coût à dix ans : l'une est un objet manufacturé produit en série, l'autre un ouvrage de grande taille construit à quelques exemplaires.
**Travail demandé.** (a) Décomposer les deux coûts selon les six postes de 22.1. (b) Dire pour chacune si la loi de Wright s'applique, et justifier par le régime de production. (c) Pour celle où elle s'applique, calculer l'effet de deux taux d'apprentissage distants de 5 points sur dix ans, et commenter l'écart obtenu. (d) Identifier la rampe d'accès de chacune, ou son absence. (e) Identifier le plancher que chacune atteindra en premier.
**Livrable.** Deux pages, calculs apparents.
**Éléments attendus.** En (c), l'écart obtenu doit surprendre : c'est le but de la question. En (b), la réponse attendue pour l'ouvrage est que la loi ne s'applique pas — mais une copie qui argumente qu'elle s'appliquerait en cas de modularisation et de série a parfaitement compris le mécanisme et vaut mieux qu'une copie qui se contente de conclure par la négative. En (d), l'absence de rampe d'accès est une conclusion valide et souvent la bonne.

🎓 **À ce stade, vous savez…**

* décomposer un coût en six postes et dire lesquels peuvent baisser, et par quel mécanisme ;
* distinguer une économie dominée par le capital d'une économie dominée par le coût marginal ;
* énoncer la loi de Wright, son statut de régularité empirique, et la sensibilité des projections au taux retenu ;
* reconnaître les régimes de production où elle ne s'applique pas, et pourquoi ;
* identifier la rampe d'accès d'une technologie chère, ou constater son absence ;
* repérer les trois planchers et savoir quand cesser de suivre le prix d'un composant ;
* refuser une comparaison de coûts dont les périmètres diffèrent.

**Ce que vous ne savez pas encore :** ce qui se passe quand le coût a baissé et que personne n'achète. C'est l'objet du chapitre 23.

---

---

---
