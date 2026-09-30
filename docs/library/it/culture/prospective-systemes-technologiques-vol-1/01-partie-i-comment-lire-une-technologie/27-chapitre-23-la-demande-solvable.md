---
title: Chapitre 23 — La demande solvable
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Le chapitre précédent s'est achevé sur une question : que se passe-t-il quand le coût a baissé et que personne n'achète ?

Ce chapitre traite de la condition ⑤, la plus souvent négligée par les ingénieurs et la plus souvent fatale. Elle tue discrètement : une technologie qui échoue faute de demande ne produit ni accident spectaculaire, ni controverse scientifique. Elle disparaît des conversations, et l'on croit rétrospectivement qu'elle n'avait pas fonctionné — alors qu'elle fonctionnait parfaitement.

## 23.1 Un problème n'est pas un marché

Tout le monde a des problèmes. Peu de gens paient pour les résoudre.

Entre l'existence d'un problème et l'existence d'une demande solvable, il y a quatre conditions que l'on peut vérifier séparément :

1. **Le problème est perçu** par celui qui le subit. Un problème qu'on ne remarque pas ne crée aucune demande.
2. **Il coûte assez cher** pour justifier une dépense. La plupart des irritants du quotidien coûtent moins que leur solution.
3. **Celui qui subit le problème est celui qui paie.** Quand ces deux personnes diffèrent — et c'est extrêmement fréquent — le mécanisme se bloque.
4. **Il existe un budget** et quelqu'un ayant autorité pour l'engager.

**La troisième condition mérite un développement**, parce qu'elle explique un grand nombre d'échecs contre-intuitifs. Un dispositif qui améliore le confort d'un locataire doit être payé par un propriétaire. Un équipement qui réduit les accidents du travail bénéficie au salarié et coûte à l'employeur. Un système qui économise de l'énergie pendant quinze ans est acheté par un promoteur qui revendra le bâtiment dans deux ans. Cette dissociation entre celui qui bénéficie et celui qui paie est un verrou aussi réel qu'une contrainte physique, et il ne se résout pas par la technique.

**La question à poser, systématiquement :** *qui a le problème, qui a le budget, et est-ce la même personne ?*

## 23.2 Qui paie, combien, à la place de quoi

Une demande ne se mesure pas dans l'absolu. Elle se mesure **par substitution**.

Un acheteur ne compare jamais votre technologie à rien. Il la compare à ce qu'il fait aujourd'hui : une autre solution, une méthode manuelle, ou l'acceptation du problème. La grandeur pertinente n'est donc pas le prix, mais **l'écart de valeur par rapport à l'alternative en place**, diminué du coût de changer.

```text
   valeur perçue = (bénéfice nouveau − bénéfice actuel) − coût d'acquisition − coût de bascule
```


Le dernier terme est celui qu'on oublie. Changer de solution coûte : apprentissage, réorganisation, migration de données, période de double exploitation, risque, perte temporaire de productivité. Ce coût est souvent supérieur au prix d'achat, et il est presque toujours absent des analyses concurrentielles.

**Conséquence pratique.** Une amélioration de 10 % ne fait rien bouger. Le seuil communément observé dans les décisions d'adoption professionnelle est un facteur, pas un pourcentage : il faut généralement être nettement meilleur, ou nettement moins cher, pour compenser le coût de bascule. Nous retrouverons ce mécanisme au chapitre 27 sous son nom : les coûts de changement.

## 23.3 L'alternative bouge pendant que vous construisez

Voici l'erreur la plus coûteuse de ce chapitre, et elle est spécifique aux technologies à long cycle de développement.

Vous évaluez la demande en comparant votre solution future à l'alternative **d'aujourd'hui**. Mais si votre développement prend dix ans, la comparaison qui compte est celle avec l'alternative **telle qu'elle sera dans dix ans**. Or l'alternative n'attend pas : elle bénéficie elle aussi de courbes d'apprentissage, d'améliorations incrémentales, et parfois d'un effet de réseau qui la rend meilleure sans qu'elle change.

### Cas — la téléphonie mobile par satellite de première génération

**Ce qui a été construit.** À la fin des années 1990, un système de communication mobile par satellite en orbite basse est déployé : une constellation de plusieurs dizaines de satellites, avec liaisons intersatellites, offrant une couverture réellement mondiale. Techniquement, c'était une réussite remarquable — le système fonctionnait et faisait ce qu'il promettait.

**Ce qui s'est passé.** Le service commercial a été lancé, puis l'opérateur s'est trouvé en faillite en quelques mois, les actifs étant finalement rachetés pour une fraction de l'investissement consenti.

*Nous ne nommons pas cet opérateur ni ne chiffrons l'opération : le mécanisme — l'alternative se déplace pendant que vous construisez — ne dépend d'aucun des deux, et les montants rapportés varient selon les sources.*

**Pourquoi.** Le concept avait été formé au début de la décennie, quand la couverture cellulaire terrestre était limitée et fragmentée. Pendant les années nécessaires à la conception, au financement, à la construction et au lancement de la constellation, les réseaux terrestres se sont étendus massivement, ont standardisé l'itinérance internationale, et ont vu le prix de leurs terminaux s'effondrer. Au moment du lancement du service, le marché visé — le professionnel mobile international — était largement couvert par une alternative moins chère, avec des terminaux plus petits et fonctionnant en intérieur.

**Ce que ce cas enseigne.** La demande n'a pas été mal estimée au moment de la conception : elle a été estimée contre la bonne alternative, mais à la mauvaise date. Le système est d'ailleurs toujours en service aujourd'hui, sur les segments où l'alternative terrestre n'existe toujours pas — maritime, aérien, zones isolées, usages gouvernementaux. **La technologie n'était pas mauvaise ; le marché visé n'était pas le sien.**

**La question à poser, pour tout projet à cycle long :** *contre quoi cette technologie sera-t-elle comparée à sa date de disponibilité, et cette alternative sera-t-elle meilleure qu'aujourd'hui ?*

## 23.4 Les seuils d'adoption

Beaucoup de technologies ne se diffusent pas progressivement : elles franchissent un seuil, puis se diffusent vite. Identifier le seuil est plus utile que suivre une tendance.

Trois formes de seuils reviennent constamment.

**Le seuil de parité de coût.** Le moment où la nouvelle solution devient moins chère que l'alternative sur le périmètre de décision de l'acheteur. Attention : le périmètre de décision de l'acheteur n'est pas toujours le coût total. Un acheteur contraint par un budget d'investissement annuel ne verra pas les économies d'exploitation des dix années suivantes.

**Le seuil de performance suffisante.** Le moment où la solution devient « assez bonne » pour l'usage — au-delà duquel un supplément de performance n'est plus valorisé. Ce seuil est souvent atteint bien avant que les ingénieurs le pensent, et une fois franchi, la concurrence se déplace vers le prix, la fiabilité ou la commodité. C'est un mécanisme majeur : beaucoup d'entreprises continuent d'améliorer une dimension que le marché a cessé de payer.

**Le seuil de risque acceptable.** Le moment où l'acheteur cesse de considérer l'adoption comme risquée pour lui personnellement. Ce seuil est social autant qu'économique : il dépend de l'existence d'autres adoptants, de références, de garanties et parfois d'une assurance. Nous y revenons au chapitre 28.

## 23.5 Le cimetière discret

Une technologie peut être mature, fiable, abordable et sans demande. Cette catégorie est mal représentée dans les analyses parce qu'elle ne fait pas de bruit.

Quatre configurations récurrentes :

**La solution en quête de problème.** Une capacité impressionnante développée sans qu'un utilisateur ait exprimé le besoin correspondant. Le récit qui l'accompagne est généralement une liste d'applications possibles, aucune n'étant portée par un acheteur identifié.

**Le gain trop petit.** Une amélioration réelle mais inférieure au coût de bascule. Elle sera peut-être intégrée un jour, à l'occasion d'un renouvellement, ce qui peut prendre le temps de vie de l'équipement en place — voir le chapitre 30.

**Le bénéficiaire n'est pas le payeur.** Traité en 23.1. Se résout parfois par la réglementation, ce qui déplace le problème vers le chapitre 28.

**Le marché a été absorbé.** Cas de la section 23.3 : la demande existait, elle a été servie ailleurs pendant le développement.

**Application analytique.** Devant une technologie dont on vous vante les capacités, la question la plus efficace n'est pas technique. C'est : **« qui a déjà payé pour cela, combien, et à la place de quoi ? »** Si la réponse est une liste d'usages potentiels plutôt qu'un client, vous connaissez la condition qui bloque.

## 23.6 Un cas de demande absente : le visiophone

Ce cas mérite d'être instruit parce qu'il est le plus pur de la catégorie : une technologie qui a fonctionné, qui a été commercialisée, et pour laquelle il n'existait pas d'acheteur — pendant environ quarante ans.

**Ce qui a été fait.** Un appareil de téléphonie avec image a été présenté au public dès les années 1960 par un opérateur américain, puis commercialisé dans quelques villes. Le service a été retiré faute d'abonnés. Il a été relancé, sous d'autres formes, à plusieurs reprises dans les décennies suivantes, par différents acteurs et sur différents continents. À chaque fois, même issue.

*Comme pour l'hydrogène, nous ne datons pas ces relances : leur nombre dépend de ce qu'on accepte de compter comme une relance. Ce qui compte est la récurrence, et l'invariance de la cause.*

**Le paradoxe.** L'appel vidéo est aujourd'hui universel. La technologie n'a donc pas échoué : c'est le **produit** qui a échoué, six ou sept fois de suite, avant que l'usage n'explose sous une autre forme.

**Ce que l'analyse par les conditions révèle.**

**Condition ⑦ — le complément.** Un visiophone n'a de valeur que si votre interlocuteur en possède un. C'est un effet de réseau direct au sens du chapitre 27.2, avec un problème d'amorçage classique. Tant que le parc était minuscule, l'appareil ne servait à rien — et son prix élevé empêchait le parc de croître.

**Condition ⑤ — la demande.** Plus profondément, il faut se demander *qui* voulait être vu au téléphone, et *à la place de quoi*. L'alternative n'était pas rien : c'était le téléphone, qui fonctionnait très bien pour l'usage principal — parler. Le gain apporté par l'image était réel mais faible au regard du coût de bascule.

**Condition ⑨ — la doctrine.** Personne ne savait quoi en faire, et surtout : personne n'avait envie de ce que cela impliquait. Être joignable en image suppose d'être présentable, dans un lieu présentable. **Le refus n'était pas technique, il était social.**

**Ce qui a fini par débloquer, et c'est le point du cas.** L'appel vidéo s'est généralisé quand quatre choses se sont produites ensemble, aucune n'étant un progrès du visiophone : le terminal est devenu un objet que chacun possédait déjà pour d'autres raisons — le coût marginal de la fonction est tombé à zéro ; le réseau a rendu le débit disponible ; le logiciel a rendu l'usage gratuit ; et le contexte a changé la norme sociale de ce qui est acceptable.

**La leçon générale.** Une demande absente n'est pas une demande latente qui attendrait un meilleur produit. C'est souvent le signe que **le problème résolu n'était pas important pour l'acheteur** — et l'usage finit parfois par apparaître, mais porté par un objet qui n'est pas celui qu'on avait conçu.

**La question à retenir :** *si cette technologie devient gratuite et parfaite, qui l'utilisera, et pour remplacer quoi ?* Si la réponse est faible même dans cette hypothèse généreuse, la condition ⑤ ne se débloquera pas par le progrès technique.

---

🎓 **À ce stade, vous savez…** distinguer un problème d'un marché ; identifier une dissociation entre bénéficiaire et payeur ; raisonner par substitution et intégrer le coût de bascule ; anticiper le déplacement de l'alternative pendant un développement long ; reconnaître les trois seuils d'adoption et les quatre configurations d'absence de demande.

---
