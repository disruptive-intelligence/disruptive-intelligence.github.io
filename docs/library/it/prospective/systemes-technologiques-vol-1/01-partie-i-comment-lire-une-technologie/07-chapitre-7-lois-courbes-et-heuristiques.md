---
title: Chapitre 7 — Lois, courbes et heuristiques
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

ce qui est vrai, et à quel titre

Le vocabulaire de la technologie est peuplé de « lois ». Loi de Moore, courbe en S, hype cycle, TRL, loi d'Amara. Elles sont utiles. Elles ne sont pas du même type, et les confondre produit des erreurs prévisibles.

## 7.1 Quatre statuts, à ne jamais mélanger

| Statut | Définition | Ce qu'on peut en faire | Exemple |
|---|---|---|---|
| **Loi physique** | contrainte établie, sans exception connue | exclure une possibilité | conservation de l'énergie, vitesse limite de propagation |
| **Régularité empirique** | relation observée sur des données, sans garantie de persistance | extrapoler avec prudence, en surveillant sa validité | loi de Wright |
| **Heuristique** | règle de bon sens, utile et non mesurable | orienter l'attention | loi d'Amara |
| **Modèle narratif** | forme qui organise un récit | communiquer | hype cycle |

Une loi physique interdit. Une régularité empirique décrit tant qu'elle dure. Une heuristique suggère. Un modèle narratif raconte.

**L'erreur type consiste à traiter un modèle narratif comme une régularité empirique**, c'est-à-dire à en tirer une prévision. Nous y venons en 7.5.

## 7.2 Loi de Moore

**Ce que c'était.** En 1965, Gordon Moore observe que le nombre de composants par circuit intégré double à intervalle régulier, et prévoit la poursuite de cette tendance. La formulation est révisée en 1975 à un doublement environ tous les deux ans.

**Ce que ce n'était pas.** Ni une loi physique, ni même une prédiction indépendante des acteurs. C'était une observation devenue **objectif industriel** : l'industrie s'est organisée pour la tenir, avec des feuilles de route communes et des investissements coordonnés. Une régularité qui se réalise parce qu'on la vise n'a pas le même statut épistémique qu'une régularité subie.

**Ce qu'elle est devenue.** Le doublement de la densité de transistors s'est poursuivi longtemps, mais plusieurs corollaires qu'on lui associait ont cessé plus tôt : l'augmentation de la fréquence d'horloge, la baisse du coût par transistor à chaque nœud, et la réduction de la consommation à performance constante. C'est un point capital pour la suite du cours : **quand une régularité cesse, elle cesse rarement d'un coup, et jamais sur toutes ses dimensions en même temps**. On continue à observer la dimension qui tient et on en conclut que rien n'a changé.

## 7.3 Courbes en S de diffusion

**Ce qu'elles décrivent.** L'adoption d'une technologie suit fréquemment une forme en S : démarrage lent, accélération, saturation. La forme se retrouve dans de nombreux cas historiques, ce qui en fait une régularité empirique solide.

**Ce qu'elles ne permettent pas.** Trois abus fréquents.

D'abord, **on ne connaît pas la hauteur du plateau à l'avance**. Une courbe en S ajustée sur les premières années peut saturer à 5 % ou à 95 % ; les données précoces ne distinguent pas les deux.

Ensuite, **une phase de croissance rapide ne prouve pas qu'on est sur une courbe en S**. Beaucoup de croissances rapides s'arrêtent sans plateau.

Enfin, **la courbe décrit et n'explique pas**. Elle ne dit pas quelle condition de diffusion a été franchie ni laquelle bloquera. C'est un résultat, pas un mécanisme — et ce cours porte sur les mécanismes.

## 7.4 TRL : ce que l'échelle mesure et ce qu'elle masque

L'échelle de maturité technologique (*Technology Readiness Level*), issue du domaine spatial puis largement reprise, gradue de 1 à 9 le chemin du principe observé au système qualifié en opération.

**Son utilité est réelle.** Elle fournit un langage commun entre financeurs, ingénieurs et acheteurs, et elle force à situer un objet.

**Ses trois limites.**

**Elle est unidimensionnelle.** Un système peut être TRL 8 sur la performance et TRL 3 sur la fabricabilité, le coût ou la certification. Le chiffre unique écrase précisément l'information dont vous avez besoin. C'est pourquoi ce cours utilise neuf conditions et non une échelle.

**Elle s'applique à un objet, pas à un système.** Un composant qualifié dans un contexte redevient immature dans un autre.

**Elle est déclarative.** Le niveau est le plus souvent annoncé par celui qui a intérêt à ce qu'il soit élevé, sans protocole opposable.

**En pratique :** un TRL est une information sur l'objet et sur celui qui l'annonce. Demandez toujours *TRL sur quelle dimension, dans quel environnement, évalué par qui*.

## 7.5 Le *hype cycle*

pourquoi il est populaire, pourquoi ce n'est pas un instrument de mesure

Le modèle a été introduit par l'analyste Jackie Fenn chez Gartner en 1995, et publié chaque année depuis pour des centaines de catégories technologiques. Il décrit cinq phases — déclencheur, pic des attentes exagérées, creux de la désillusion, pente de l'illumination, plateau de productivité — sur un axe vertical de « visibilité ».

**Ce qu'il capture de juste.** Une intuition réelle et utile : la valeur perçue et la valeur réelle divergent, souvent dans les deux sens. Une technologie reçoit d'abord plus d'attention que ses capacités du moment ne le justifient, puis parfois moins d'attention que ses capacités améliorées ne le mériteraient. Cette observation est bonne, et elle explique la popularité du modèle.

**Ce qui pose problème.** La littérature académique sur sa validité prédictive est nettement sceptique. L'examen le plus cité, celui de Martin Steinert et Larry Leifer (Stanford, PICMET 2010), analyse les rapports du secteur énergie de 2003 à 2009, les 46 technologies qu'ils contiennent, puis teste empiriquement trois trajectoires — énergie marémotrice, cycle combiné à gazéification intégrée, photovoltaïque — en mesurant visibilité médiatique et intérêt des utilisateurs. Les auteurs concluent que le modèle manque de fondement théorique et empirique robuste, que la méthodologie de collecte et de traitement doit être questionnée, et que peu de technologies parcourent effectivement la trajectoire complète que le modèle décrit. Des travaux ultérieurs relèvent des technologies apparaissant d'emblée à une phase avancée, ou régressant d'une phase à l'autre d'une édition à la suivante — deux comportements que le modèle n'autorise pas.

**Ce qu'il faut en faire.** Deux usages distincts, à ne pas confondre.

* **Comme vocabulaire partagé** : parfaitement acceptable. Dire « on est dans le creux » se comprend et n'engage rien.
* **Comme instrument de prévision** : non. En particulier, la phase « plateau de productivité » n'a rien d'automatique. Beaucoup de technologies entrent dans le creux et n'en ressortent pas. Le modèle, par sa forme même, suggère que le creux est une étape vers le succès — c'est exactement ce que le chapitre 1 appelait une analyse que rien ne peut réfuter.

**Retenez la formulation exacte :** un positionnement sur un *hype cycle* est une opinion d'analyste informée, pas un fait vérifié. Cela ne le disqualifie pas ; cela indique le poids qu'on peut lui donner.

## 7.6 Amara, Jevons, et l'usage correct d'une heuristique

**Loi d'Amara.** Attribuée à Roy Amara : nous surestimons l'effet d'une technologie à court terme et le sous-estimons à long terme. C'est une heuristique, pas une régularité mesurable — elle n'est ni quantifiée, ni datée, ni réfutable telle quelle. Elle reste utile parce qu'elle nomme un biais réel et qu'elle rappelle que les deux erreurs de ce cours (surestimation et sous-estimation) coexistent souvent sur le même objet, à des horizons différents. Son abus consiste à l'invoquer pour justifier n'importe quelle prédiction en jouant sur l'horizon.

**Paradoxe de Jevons.** Observation historique de William Stanley Jevons : l'amélioration de l'efficacité d'usage d'une ressource peut augmenter sa consommation totale, parce que la baisse du coût d'usage élargit les usages. Ce n'est ni une loi ni une fatalité : l'effet rebond existe, son ampleur varie fortement selon les cas, et il peut être partiel comme total. Sa valeur est de vous imposer une question — *que se passe-t-il si l'usage augmente autant que l'efficacité ?* — plutôt que de vous donner une réponse. Nous le retrouverons au chapitre 31.

**Règle générale d'usage d'une heuristique :** elle sert à **ouvrir une question**, jamais à la clore. Le jour où vous entendez une heuristique servir de conclusion, c'est qu'elle a changé de statut sans prévenir.

## 7.7 Utiliser un modèle dont on connaît les limites

Aucun modèle de ce chapitre n'est à jeter. Trois règles suffisent à les utiliser sans se tromper.

**Déclarer le statut.** Dites toujours de quel type d'objet vous parlez : « c'est une régularité empirique, valable tant que le mécanisme sous-jacent tient » plutôt que « c'est la loi de X ». Cette précision, en réunion, change la nature de la discussion.

**Nommer le mécanisme.** Une régularité sans mécanisme est fragile. La loi de Wright a un mécanisme — l'apprentissage industriel par accumulation de production. La courbe en S en a un — la saturation d'un marché. Le *hype cycle* n'en a pas de démontré. Cherchez toujours le mécanisme derrière la courbe ; c'est lui qui vous dira quand elle cessera.

**Prévoir la fin.** Pour toute régularité que vous mobilisez, écrivez ce qui l'interromprait. C'est la quatrième question, appliquée à vos outils plutôt qu'à votre objet.

🎓 **À ce stade, vous savez…**

* classer une « loi » technologique en loi physique, régularité empirique, heuristique ou modèle narratif ;
* expliquer pourquoi la loi de Moore n'était pas une loi et pourquoi ses corollaires ont cessé avant elle ;
* dire ce qu'une courbe en S décrit et ce qu'elle ne prédit pas ;
* interroger un TRL sur sa dimension, son environnement et son évaluateur ;
* utiliser le *hype cycle* comme vocabulaire sans le prendre pour une mesure ;
* exiger un mécanisme derrière toute régularité que vous mobilisez.

---
