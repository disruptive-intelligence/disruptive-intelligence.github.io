---
title: Chapitre 27 — Standards, effets de réseau et dépendance de sentier
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Ce chapitre répond à une question posée dès le chapitre 1 et laissée ouverte depuis : **pourquoi une meilleure technologie perd-elle ?**

## 27.1 Trois façons dont un standard existe

Un standard est une convention partagée qui permet à des objets conçus indépendamment de fonctionner ensemble. Il existe trois voies, aux propriétés très différentes.

**Le standard de droit.** Établi par un organisme de normalisation, par consensus entre parties prenantes, publié et parfois rendu obligatoire. Lent — plusieurs années —, mais stable, documenté et généralement libre de mise en œuvre. C'est le mode dominant dans les infrastructures physiques, les télécommunications et la sécurité.

**Le standard de fait.** S'impose par l'usage, sans décision formelle. Rapide, souvent contrôlé par un acteur, potentiellement instable — celui qui le contrôle peut le modifier. C'est le mode dominant dans le logiciel et les plateformes.

**Le standard imposé.** Une autorité publique rend une interface obligatoire. Rare, mais spectaculairement efficace quand la coordination volontaire a échoué — l'unification des connecteurs de charge d'appareils portables dans l'Union européenne en est un exemple récent. ⏱

**Ce que le mode de création change.** Un standard de droit se déplace lentement mais prévisiblement. Un standard de fait peut disparaître en quelques années, ou se durcir si son propriétaire y a intérêt. Savoir de quel type on parle change complètement l'analyse du risque de dépendance — question directement pertinente pour un lecteur venant du SI.

## 27.2 Effets de réseau

Un bien présente un **effet de réseau** quand sa valeur pour chaque utilisateur croît avec le nombre d'utilisateurs.

**Effets directs.** La valeur vient des autres utilisateurs eux-mêmes : un réseau de communication, un format d'échange, une langue.

**Effets indirects.** La valeur vient de ce que l'écosystème produit autour : applications disponibles pour une plateforme, pièces détachées pour un véhicule, ingénieurs formés à un outil, littérature technique. Ces effets sont plus lents et bien plus difficiles à renverser que les effets directs, parce qu'ils sont incarnés dans des investissements durables faits par des tiers.

**Conséquence.** Un marché à forts effets de réseau ne tend pas vers un équilibre entre concurrents : il tend vers la concentration. Ce n'est pas un jugement, c'est une propriété structurelle, et elle explique pourquoi la question « qui est le meilleur ? » y est souvent moins prédictive que « qui est arrivé assez tôt avec quelque chose d'assez bon ? ».

## 27.3 Base installée et coûts de changement

Le chapitre 23 a introduit le coût de bascule du point de vue de l'acheteur. Vu du côté du système, il porte un autre nom : la **base installée**.

Tout ce qui est déjà déployé constitue un actif dont la valeur dépend du maintien du standard existant : équipements, formats de données, formations suivies, contrats, procédures, pièces en stock, compétences des équipes. Cette masse n'a aucune raison de changer, et elle est généralement bien plus importante que le flux annuel de nouveaux équipements.

**Le calcul que fait implicitement tout acheteur :**

```text
   changer si :  gain × durée d'usage  >  coût de bascule + risque
```


Trois observations découlent de cette inégalité.

**La durée d'usage est décisive.** Plus l'équipement en place dure, plus le changement est repoussé — non parce qu'il est mauvais, mais parce que l'occasion ne se présente pas. Nous verrons au chapitre 30 que le renouvellement du parc est la contrainte temporelle que rien n'accélère.

**Le risque personnel compte autant que le coût.** Celui qui décide du changement en supporte les conséquences en cas d'échec, et n'en récupère qu'une part des bénéfices en cas de succès. Cette asymétrie explique une grande part du conservatisme des grandes organisations, et elle n'est pas irrationnelle.

**Le verrouillage n'est pas nécessairement voulu.** Il peut résulter d'un enchaînement de décisions individuellement raisonnables. Il n'y a pas toujours quelqu'un à blâmer.

## 27.4 Interopérabilité

un choix stratégique, pas une propriété technique

L'interopérabilité paraît être une qualité technique. Elle est d'abord une décision économique.

**Ouvrir** élargit le marché total, accélère l'adoption, attire des compléments, réduit la crainte du verrouillage chez l'acheteur — et abandonne une partie de la capture de valeur.

**Fermer** protège la marge et le contrôle de l'écosystème — et ralentit l'adoption, encourage les alternatives et attire l'attention du régulateur.

**Le schéma classique** consiste à ouvrir pendant la phase de conquête, quand l'enjeu est de devenir le standard, puis à refermer progressivement une fois la base installée acquise. Reconnaître à quel moment de ce cycle se trouve une technologie est une compétence d'analyse directement utile : elle dit ce qui va probablement se passer au renouvellement de contrat.

## 27.5 La dépendance de sentier

Nous y sommes.

La **dépendance de sentier** désigne le fait que l'état actuel d'un système dépend de l'histoire de ses choix passés, y compris de choix qui n'avaient rien d'optimal, et que ces choix peuvent se verrouiller de sorte qu'une meilleure solution ne parvienne plus à s'imposer.

> **P7 — Une technologie suffisamment bonne déjà installée bat une technologie meilleure isolée.**

**Le mécanisme est clair et se déduit de ce qui précède** : effets de réseau, base installée, coûts de bascule, compléments existants, compétences acquises, risque perçu. Une nouvelle solution ne concourt pas contre les qualités intrinsèques de l'ancienne : elle concourt contre l'ancienne *plus tout l'écosystème accumulé autour d'elle*.

### Une controverse scientifique qu'il faut connaître

L'exemple le plus cité de dépendance de sentier est la disposition du clavier QWERTY. L'économiste Paul David en a fait en 1985 le cas d'école : une disposition conçue sous des contraintes mécaniques disparues se serait verrouillée par apprentissage et effets de réseau, empêchant l'adoption d'alternatives supérieures.

**Cette thèse a été sérieusement contestée.** Stanley Liebowitz et Stephen Margolis ont publié en 1990 une critique dans laquelle ils examinent les preuves de supériorité de la disposition alternative généralement invoquée et concluent que les études favorables étaient méthodologiquement faibles, certaines conduites par une partie intéressée, et que des essais indépendants n'ont pas retrouvé d'avantage significatif. Leur conclusion est que le cas ne démontre pas le verrouillage d'une solution inférieure, faute d'avoir établi qu'elle était inférieure.

**Comment traiter cette controverse.** Le débat reste ouvert et il ne se tranche pas ici. Ce qu'il faut en retenir est méthodologique, et c'est plus utile que l'anecdote :

* **Le mécanisme de dépendance de sentier est solidement établi** par ailleurs — effets de réseau, base installée et coûts de bascule sont documentés dans de nombreux domaines.
* **L'exemple le plus célèbre de ce mécanisme est empiriquement fragile.** Un mécanisme réel peut être illustré par un mauvais exemple, et la popularité d'un exemple n'est pas une preuve.
* **Établir qu'une technologie « meilleure » a perdu suppose d'établir qu'elle était meilleure**, ce qui exige un critère explicite et une mesure — exactement l'exigence du chapitre 6.

C'est ce que ce cours vous demande de faire systématiquement : distinguer le mécanisme de son illustration, et vérifier l'illustration.

**Des cas moins contestés existent** et seront instruits au chapitre 36 : des filières industrielles évincées malgré des propriétés supérieures sur certaines dimensions, des formats concurrents où le gagnant n'était pas le meilleur sur les critères techniques, des infrastructures dont les caractéristiques héritées contraignent encore aujourd'hui des systèmes entiers.

## 27.6 Comment un standard se déplace quand même

Le verrouillage n'est pas éternel. Quatre voies de sortie sont observables, et elles sont toutes reconnaissables à l'avance.

**Le saut générationnel.** Le renouvellement du parc arrive ; on ne remplace pas, on installe la génération suivante. La fenêtre est étroite et périodique — d'où l'importance de savoir quand elle s'ouvre.

**Le nouveau segment.** L'alternative s'impose d'abord là où il n'y a pas de base installée : nouveau marché, nouvelle géographie, nouvel usage. Elle y accumule volume et compléments, puis revient. C'est de loin la voie la plus fréquente.

**La contrainte externe.** Une réglementation, une pénurie, une rupture d'approvisionnement rend l'ancien standard impraticable, et le coût de bascule cesse d'être le critère.

**Le changement d'ordre de grandeur.** L'alternative devient meilleure d'un facteur, pas de quelques pourcents. Le coût de bascule est alors absorbé.

**Signal analytique.** Devant une technologie supérieure qui ne perce pas, la question utile n'est pas « pourquoi le marché est-il irrationnel ? » — il ne l'est pas. C'est : **« laquelle de ces quatre portes est susceptible de s'ouvrir, et quand ? »**

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « C'est le standard du marché » | standard de fait, contrôlé par quelqu'un | de droit ou de fait ? qui peut le modifier ? |
| « C'est ouvert » | une spécification est publiée | qui décide des évolutions, et à quelles conditions ? |
| « On est enfermés chez ce fournisseur » | coûts de bascule élevés | quel est le coût réel, et quelle fenêtre de renouvellement approche ? |
| « Leur techno est meilleure mais ils ne perceront pas » | intuition souvent juste | meilleure selon quel critère mesuré, et quelle porte de sortie existe ? |
| « Il faut être compatible avec l'existant » | contrainte de base installée | jusqu'à quand, et à quel coût de complexité ? |

🎓 **À ce stade, vous savez…** distinguer standard de droit, de fait et imposé ; identifier des effets de réseau directs et indirects ; poser l'inégalité de bascule du point de vue de l'acheteur ; expliquer la dépendance de sentier et distinguer le mécanisme de son illustration la plus célèbre ; reconnaître les quatre portes par lesquelles un standard se déplace.

---
