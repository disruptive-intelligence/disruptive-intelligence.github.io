---
title: Chapitre 37 — Quand la promesse revient tous les quinze ans
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 39
chapters: 53
---

*Cas développés : hydrogène pour la mobilité, réalité virtuelle. Mentions courtes : cycles antérieurs de l'IA, robotique généraliste.*

Ce chapitre est le plus utile de la partie pour votre pratique quotidienne, parce que c'est la situation que vous rencontrerez le plus souvent : une technologie dont on vous dit « cette fois, c'est différent ».

## 37.1 Le phénomène

Certaines technologies connaissent des vagues d'enthousiasme successives, séparées par des périodes d'oubli. À chaque vague, les mêmes promesses reviennent, formulées avec le vocabulaire de l'époque.

**Le piège est symétrique**, et le chapitre 6.8 l'a établi :

* traiter la nouvelle vague comme les précédentes conduit à manquer un changement de régime réel ;
* traiter chaque vague comme nouvelle conduit à répéter les erreurs.

**La seule sortie est analytique** : identifier ce qui a réellement changé depuis la vague précédente, et ce qui n'a pas changé.

## 37.2 Hydrogène pour la mobilité — la physique n'a pas changé

Ce cas est le plus instructif du chapitre, parce que **la contrainte centrale est calculable et n'a jamais varié**.

### Le fait invariant

Le chapitre 8.2 l'a établi par une multiplication. Comparons deux chaînes énergétiques pour un même service :

```text
   Électricité → batterie → moteur                        ≈ 80 %
   Électricité → hydrogène → électricité → moteur         ≈ 30 %
```

Un facteur d'environ deux et demi sur l'électricité consommée. ⏱ *Ordres de grandeur ; le rapport est le point.*

**Ce rapport n'a pas changé depuis les années 1970.** Il découle du rendement de l'électrolyse, de la compression ou de la liquéfaction, du transport, et de la conversion inverse. Chacune de ces étapes a progressé ; aucune ne peut dépasser des bornes thermodynamiques, et leur produit reste défavorable.

**C'est un cas rare et précieux : une condition ④ dont on peut démontrer, par le chapitre 8, qu'elle ne se retournera pas par simple progrès incrémental.**

### Les vagues

Plusieurs périodes d'enthousiasme se sont succédé depuis les années 1970, chacune motivée par un contexte différent — chocs pétroliers, préoccupations d'émissions locales, puis objectifs climatiques. À chaque fois, des programmes publics, des démonstrateurs, des annonces industrielles. À chaque fois, un reflux.

**Nous ne datons pas ces vagues précisément ici**, et c'est délibéré : leur découpage varie selon les auteurs et selon les pays, et le raisonnement qui suit n'en dépend pas. Ce qui compte est qu'elles se sont succédé sur un demi-siècle **sans que la contrainte centrale ne bouge**.

### Ce que la méthode dit

**Ce qui n'a pas changé :** le rendement cumulé de la chaîne, et le fait que le complément — production, transport, stockage, distribution — doit être construit intégralement, alors que le réseau électrique existe déjà. Chapitre 26 : *cette technologie peut-elle s'appuyer sur une infrastructure existante ?* La réponse est non, et c'est structurel.

**Ce qui a réellement changé :** le coût de l'électricité renouvelable, la disponibilité de l'électrolyse à plus grande échelle, et surtout **la comparaison avec l'alternative** — chapitre 23.3. Dans les années 1990, l'alternative électrique à batterie n'était pas crédible ; elle l'est devenue. Le concurrent de l'hydrogène s'est donc considérablement renforcé pendant les périodes de reflux.

**La conclusion analytique, et elle est nuancée.** Le raisonnement ci-dessus ne dit pas que l'hydrogène est sans avenir. Il dit que **la comparaison doit se faire usage par usage** : là où la densité énergétique massique prime, où la recharge rapide est déterminante, ou dans les procédés industriels qui utilisent l'hydrogène comme matière première et non comme vecteur énergétique, la conclusion peut être différente. **Le rendement défavorable disqualifie un usage général, pas tous les usages.**

C'est exactement le raisonnement par segments du chapitre 30.6 : la bonne question n'est jamais « cette technologie va-t-elle gagner ? » mais « sur quels segments, et pourquoi pas sur les autres ? ».

## 37.3 Réalité virtuelle — quand le verrou change de nature entre deux vagues

**Ce que ce cas ajoute :** contrairement à l'hydrogène, ici **les verrous ont réellement changé**.

**Vague ancienne.** Les verrous étaient techniques et mesurables : latence trop élevée, résolution insuffisante, encombrement, coût. Ce sont des conditions ② et ③, et elles étaient identifiables.

**Vague récente.** Ces verrous techniques ont été largement levés — latence, résolution et poids ont progressé de plusieurs ordres de grandeur. La diffusion reste pourtant limitée.

**Ce que cela signifie, et c'est le point du cas.** Quand un verrou identifié est levé et que la diffusion ne suit pas, **le verrou était ailleurs**. Ici, il se situe dans les conditions ⑤ et ⑨ : quel problème cette technologie résout-elle, pour qui, et les organisations savent-elles quoi en faire ?

**La leçon générale, et elle est importante :** un verrou technique est plus facile à identifier qu'un verrou d'usage, donc on l'identifie préférentiellement — c'est le biais du chapitre 3.5, chercher le goulet dans son domaine de compétence. Le lever révèle alors le verrou réel, qui était masqué. **C'est un déplacement de goulet au sens du chapitre 32, où le nouveau goulet n'est pas technique.**

## 37.4 Mentions courtes

**Cycles antérieurs de l'intelligence artificielle.** Le domaine a connu des périodes d'enthousiasme suivies de reflux, associées à des attentes non tenues et à des réductions de financement. Le mécanisme est analysable : des démonstrations réussies dans des conditions choisies, une extrapolation à des usages généraux, puis la rencontre avec la condition ③ — fiabilité hors laboratoire. **Le chapitre 21.6 a établi pourquoi ce mur est spécifique aux systèmes appris.**

**Robotique généraliste.** Promesse récurrente depuis des décennies. Le chapitre 16.6 en a donné la raison technique principale : manipuler est structurellement plus difficile que se déplacer, et cette difficulté ne se réduit pas au calcul.

## 37.5 La grille des promesses récurrentes

Six questions, applicables à toute technologie dont on vous dit « cette fois, c'est différent ».

| # | Question | Ce qu'elle teste |
|---|---|---|
| 1 | Quelle est la contrainte invariante, et a-t-elle bougé ? | condition ① ou ④ physique |
| 2 | Quel verrou a été levé depuis la vague précédente, et est-ce mesurable ? | conditions ② et ③ |
| 3 | Quel verrou nouveau apparaît une fois celui-là levé ? | chapitre 32 |
| 4 | L'alternative concurrente a-t-elle progressé pendant l'intervalle ? | chapitre 23.3 |
| 5 | Le complément nécessaire existe-t-il maintenant, ou faut-il encore le construire ? | chapitre 26 |
| 6 | Sur quels segments précisément, et pourquoi pas les autres ? | chapitre 30.6 |

**Comment lire les réponses.** Si la question 1 révèle une contrainte physique invariante défavorable, le scepticisme est fondé pour l'usage général — mais la question 6 reste ouverte. Si la question 2 révèle un verrou réellement levé et mesurable, quelque chose a changé — et la question 3 devient la plus importante.

**Ce que cette grille n'est pas.** Elle ne produit pas de verdict. Elle produit une **analyse conditionnelle réfutable**, ce qui est l'objectif énoncé au chapitre 1.6.

## 37.6 Pourquoi le scepticisme systématique échoue aussi

Il faut le redire ici, parce que ce chapitre entraîne au doute.

Le chapitre 1 l'a montré avec le photovoltaïque : des institutions compétentes ont sous-estimé une trajectoire pendant vingt ans. Le chapitre 6.8 en a donné le mécanisme : généralisation depuis les échecs passés, confusion entre difficile et impossible, refus du changement de régime, et confort social du doute.

**Le test, appliqué une dernière fois.** Après avoir formulé un doute sur une promesse récurrente, demandez-vous : *qu'est-ce que j'observerais si j'avais tort ?* Si votre scepticisme ne produit aucun signal observable qui le contredirait, ce n'est pas une analyse.

🎓 **À ce stade, vous savez…** identifier une contrainte invariante et la distinguer d'un verrou temporaire ; reconnaître qu'un verrou levé sans diffusion signale un verrou masqué ailleurs ; appliquer la grille des six questions ; raisonner par segments plutôt que par verdict global ; et soumettre votre propre scepticisme au test de réfutabilité.

---
