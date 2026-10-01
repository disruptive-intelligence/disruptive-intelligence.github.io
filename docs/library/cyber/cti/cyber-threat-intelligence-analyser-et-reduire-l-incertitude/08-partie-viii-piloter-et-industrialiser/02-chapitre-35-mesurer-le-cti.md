---
title: Chapitre 35 — Mesurer le CTI
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

## 35.1 Le problème : mesurer une réduction d'incertitude

**La difficulté est réelle et il faut la nommer** : le CTI produit de meilleures décisions. Une meilleure décision ne se voit pas — surtout quand elle consiste à ne rien faire.

**Les trois pièges qui en découlent** :

| Piège | Mécanisme |
|---|---|
| **Mesurer ce qui est facile** | Nombre de rapports, volume de flux, indicateurs ingérés |
| **Ne rien mesurer** | La fonction disparaît au premier arbitrage |
| **Sur-attribuer** | « Nous avons évité un incident » — invérifiable, et cela décrédibilise |

**La posture honnête** : mesurer ce qu'on peut mesurer, dire ce qu'on ne peut pas prouver, et assumer la différence.

## 35.2 Trois familles d'indicateurs

| Famille | Question | Facilité | Valeur |
|---|---|---|---|
| **Production** | Qu'avons-nous produit ? | **Facile** | **Faible** |
| **Usage** | Qui l'a lu, qui l'a utilisé ? | Moyenne | Élevée |
| **Impact** | Qu'est-ce qui a été décidé différemment ? | **Difficile** | **Très élevée** |

**La corrélation est inverse entre facilité et valeur**, et c'est ce qui explique que la plupart des fonctions mesurent la production.

## 35.3 ⚠️ Les faux indicateurs

| Indicateur | Pourquoi il ne mesure rien |
|---|---|
| **Nombre de rapports produits** | Mesure l'activité, pas l'utilité. Peut augmenter en dégradant la qualité |
| **Volume d'indicateurs ingérés** | Mesure ce que le fournisseur collecte (§22.4) |
| **Nombre de sources suivies** | Mesure une accumulation (§14.6) |
| **Nombre d'alertes émises** | **Devrait diminuer** avec la maturité (§27.2) |
| Temps de veille quotidien | Mesure une consommation, pas un résultat |
| Nombre de menaces identifiées | Dépend de l'actualité, pas de vous |

⚠️ Le quatrième est le plus pervers : présenté comme un indicateur d'activité, il incite exactement au comportement qui détruit la fonction.

## 35.4 Mesurer l'usage

**C'est le compromis praticable** : plus facile que l'impact, infiniment plus utile que la production.

**Les trois questions**, envoyées deux semaines après chaque produit — celles du §15.7 :

```
1. L'avez-vous lu ?
2. Avez-vous décidé ou fait quelque chose ?
3. Qu'est-ce qui vous a manqué ?
```


**Ce qu'on en tire** :

| Indicateur | Ce qu'il révèle |
|---|---|
| Taux de lecture par destinataire | Qui vous lit, et qui ne vous lit plus |
| Taux de réponse au questionnaire | Un proxy de l'engagement |
| **Récurrence des manques signalés** | La lacune structurelle de vos produits |

**Le troisième est le plus précieux.** Quatre destinataires signalant la même absence — un coût estimé, un délai, une comparaison — désignent une amélioration à faire, invisible autrement.

## 35.5 Mesurer l'impact

**Ce qui est mesurable** :

| Indicateur | Comment |
|---|---|
| **Décisions modifiées** | Registre des décisions, avec ce qui aurait été fait sans le renseignement |
| **Ordre de priorisation changé** | Comparaison avant/après (§31.6) |
| **Délai gagné** | Avance sur la publication publique (§22.3, test 3) |
| **Menaces neutralisées documentées** | Les archivages pour neutralisation (§29.9) |
| **Vérifications ayant évité une mobilisation** | Le cas de §8.9 : une journée au lieu de neuf mille euros |

**Ce qui n'est pas mesurable, et qu'il faut renoncer à mesurer** :

- Les incidents évités — invérifiable ;
- La valeur d'une information qui n'a pas servi cette fois ;
- L'effet dissuasif — inexistant en CTI défensif.

✅ **BONNE PRATIQUE (P0) — le registre des décisions**
Deux lignes par produit diffusé : *quelle décision a été prise, et qu'aurait-on fait sans ?* Cinq minutes par semaine. Au bout d'un an, ce registre est **la seule démonstration solide** de l'utilité de la fonction, et il résiste à un arbitrage budgétaire là où aucun indicateur de production ne résiste.

## 35.6 Le retour d'expérience analytique

**C'est le segment ⑥ de la boucle, et il n'existe presque nulle part.**

**Ce que c'est** : relire ses propres estimations passées et vérifier si elles étaient justes.

**La méthode**, semestrielle, deux heures :

```
1. Reprendre les 10 dernières évaluations calibrées
2. Pour chacune : que s'est-il passé réellement ?
3. L'estimation était-elle juste ? La CONFIANCE était-elle juste ?
4. Quel biais, quelle lacune, quelle méthode a manqué ?
5. Qu'est-ce qui change dans ma pratique ?
```


**La distinction de l'étape 3 est essentielle** : une estimation fausse avec une confiance faible correctement exprimée est un **bon travail**. Une estimation juste avec une confiance excessive est un **mauvais travail** — c'est avoir raison par accident (§7.9).

| | Estimation juste | Estimation fausse |
|---|---|---|
| **Confiance élevée** | ✅ Excellent | ❌ **Le pire cas** — surconfiance |
| **Confiance faible** | ⚠️ Correct, mais la confiance était sous-évaluée | ✅ **Bon travail** — l'incertitude était annoncée |

**Ce que ce tableau change** : on ne juge pas un analyste sur son taux d'exactitude, mais sur **l'alignement entre sa confiance annoncée et sa justesse réelle**. C'est le §2.5, rendu mesurable.

## 35.7 ✅ Livrable — Le tableau de bord CTI

Une page, trimestrielle, six indicateurs.

| Indicateur | Famille | Valeur |
|---|---|---|
| Besoins actifs, et leur statut | Production | n actifs, n reportés, n abandonnés |
| Produits diffusés, par niveau | Production | n stratégiques, n opérationnels, n tactiques |
| **Taux de lecture et de réponse** | Usage | n % |
| **Décisions modifiées** | Impact | n, avec 3 exemples |
| **Menaces neutralisées documentées** | Impact | n, avec la mesure qui protège |
| **Alignement confiance / justesse** | Retour | Résultat du dernier retour d'expérience |

**Les trois dernières lignes sont celles qui répondent à la question du financeur.** Les trois premières décrivent l'activité ; elles ne suffisent pas.

## 35.8 🔴 FIL ROUGE — mai 2031 : deux ans après

En avril 2029, Karim Lebrun avait validé le poste de Nour à une condition : *démontrer, à l'issue de la période, quelles décisions ont été prises différemment* (§2.6).

**Le bilan présenté au comité du 14 mai 2031**, à vingt-quatre mois.

**Ce que Nour ne présente pas** : le nombre de produits, le volume d'éléments traités, le nombre de sources suivies.

**Ce qu'elle présente** :

| Indicateur | Valeur sur 24 mois |
|---|---|
| **Décisions documentées comme modifiées par le renseignement** | **31** |
| — dont priorisations de remédiation réordonnées | 14 |
| — dont mobilisations évitées après vérification | 6 |
| — dont actions produit déclenchées | 5 |
| — dont règles de détection écrites | 4 |
| — dont décisions d'investissement éclairées | 2 |
| **Menaces documentées neutralisées par une mesure existante** | 89 |
| **Avance moyenne sur publication publique** *(source sectorielle)* | 4,1 jours |
| Alignement confiance / justesse *(dernier retour d'expérience)* | 8 sur 10 estimations correctement calibrées |

**Les deux chiffres qui emportent la décision**, et ce ne sont pas ceux attendus :

**Les 6 mobilisations évitées.** Chacune est chiffrée. La première — juillet 2029 — a coûté 9 000 € parce qu'elle n'a pas été évitée. Les six suivantes ont été évitées par vérification, pour un coût cumulé estimé de deux journées-homme.

**Les 89 neutralisations documentées.** Elles ne prouvent pas que le CTI a protégé quoi que ce soit — c'est le dispositif de sécurité qui protège. Mais elles **documentent que les mesures en place fonctionnent contre des menaces réelles**, ce qu'aucun autre dispositif ne produisait.

**La question de Karim Lebrun**, plus fine que celle de 2029 :

> *« Sur les 31 décisions, combien auraient été prises correctement sans vous ? »*

**La réponse de Nour**, qu'elle a préparée et qui est honnête :

> *Sur les 31, je peux démontrer que 19 auraient été différentes. Pour 8, je ne peux rien démontrer — elles auraient probablement été prises de la même façon, plus tard. Pour 4, la question n'a pas de réponse.*
>
> *Ce que je peux affirmer avec certitude, c'est que les 89 neutralisations n'auraient été documentées par personne. Et que sans elles, nous ne saurions pas ce qui fonctionne.*

**La décision du comité** : la fonction est pérennisée, et un second poste est ouvert pour 2032 — orienté sur le renseignement produit, qui est le besoin dont la croissance est la plus forte.

**Ce que Claire écrit en conclusion de la note** :

> *Le meilleur indicateur de cette fonction n'est pas dans le tableau. C'est qu'en deux ans, plus personne ne demande « pourquoi nous ? ». On demande « qu'est-ce qui est accessible ». Ce changement de question vaut les trente et une décisions.*

**Livrable de l'épisode.** Le tableau de bord en six indicateurs, et le registre des décisions tenu depuis avril 2029 — annexe K.

→ La suite en 🔴 §37.6, quand il faudra chiffrer ce que tout cela coûte.

## Synthèse mentale du chapitre 35

Le CTI produit de meilleures décisions, et une meilleure décision ne se voit pas — surtout quand elle consiste à ne rien faire. Trois familles d'indicateurs existent, et la corrélation entre facilité et valeur est inverse : la production est facile à mesurer et sans valeur, l'impact est difficile et décisif. Le nombre d'alertes émises est le faux indicateur le plus pervers, parce qu'il devrait diminuer avec la maturité. Mesurer l'usage est le compromis praticable, et sa donnée la plus précieuse est la récurrence des manques signalés — quatre destinataires signalant la même absence désignent une lacune invisible autrement. Le registre des décisions, deux lignes par produit, est la seule démonstration qui résiste à un arbitrage budgétaire. Enfin, le retour d'expérience analytique juge l'alignement entre confiance annoncée et justesse réelle, pas le taux d'exactitude : une estimation fausse avec une confiance faible correctement exprimée est un bon travail ; une estimation juste avec une confiance excessive est le pire cas.

**Trois questions de vérification**

1. Pourquoi le nombre d'alertes émises est-il un indicateur pervers, et que devrait-il faire avec la maturité ?
2. Un financeur vous demande de démontrer l'utilité de la fonction. Que présentez-vous, et que ne présentez-vous surtout pas ?
3. Deux analystes : l'un s'est trompé en annonçant une confiance faible, l'autre a eu raison en annonçant une confiance élevée non justifiée. Lequel a bien travaillé ?

---
