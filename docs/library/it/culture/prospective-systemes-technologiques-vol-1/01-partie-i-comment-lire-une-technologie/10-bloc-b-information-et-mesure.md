---
title: Bloc B — Information et mesure
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 8.4 Il n'existe pas de mesure sans bruit

Le bruit n'est pas un défaut de conception qu'un meilleur capteur ferait disparaître. C'est une propriété du monde physique.

**D'où il vient.** L'agitation thermique des atomes produit du bruit dans tout circuit à température non nulle. La lumière arrive par paquets discrets, et compter des paquets rares est intrinsèquement incertain. Les composants eux-mêmes fluctuent. Aucun de ces phénomènes ne peut être annulé ; on peut seulement les rendre petits devant le signal.

**Ce qui compte est donc le rapport.** La grandeur pertinente n'est jamais le bruit seul, mais le **rapport entre le signal et le bruit**. Un signal faible dans un environnement calme peut être parfaitement lisible ; un signal fort dans un environnement bruyant peut être inexploitable.

**On peut échanger du temps contre de la précision.** Mesurer plus longtemps, ou moyenner plusieurs mesures, améliore le rapport signal sur bruit. Mais on paie ce gain en **latence** — et parfois en pertinence, si l'objet mesuré a changé pendant la mesure. C'est un arbitrage universel, qui réapparaîtra en imagerie, en radar, en instrumentation biologique et en positionnement.

> **Résout / coûte.** Moyenner : *résout* le bruit · *coûte* du temps, donc de la latence, donc la capacité à suivre un phénomène rapide.

**Conséquence à retenir :** il existe toujours un **plancher de détection**. En dessous, l'information n'est pas dégradée : elle est absente. Aucun traitement ne la reconstituera, et c'est la section suivante qui explique pourquoi.

## 8.5 Mesurer, c'est perdre

Toute mesure convertit une grandeur physique continue en une information discrète et finie. Cette conversion perd de l'information, de trois façons distinctes.

**Par la résolution.** Un capteur découpe la grandeur mesurée en niveaux. Tout ce qui est plus fin que ce découpage est perdu.

**Par l'échantillonnage.** Un capteur mesure à intervalles réguliers. Entre deux mesures, il ne sait rien.

**Par la dynamique.** Un capteur a une plage de mesure. En dessous, il ne voit rien ; au-dessus, il sature. Un capteur bien réglé pour un phénomène faible est aveugle à un phénomène fort, et inversement.

**Le triangle d'arbitrage.** Résolution fine, cadence élevée, large dynamique : ces trois qualités se paient les unes contre les autres, en coût, en énergie et en volume de données. Aucun capteur ne les maximise simultanément. **Quand quelqu'un vous vante un capteur, demandez laquelle des trois a été sacrifiée** — il y en a toujours une.

**Le piège du sous-échantillonnage.** Si l'on mesure un phénomène moins souvent qu'il ne varie, on n'obtient pas une version dégradée du phénomène : on obtient un **motif faux**, souvent lisse, cohérent et parfaitement crédible. C'est ainsi que des roues paraissent tourner à l'envers dans une vidéo.

Ce point mérite d'être souligné parce qu'il annonce un thème majeur du volume : **une mesure insuffisante ne se signale pas comme insuffisante.** Elle produit un résultat qui a l'air normal. C'est la première apparition de ce que le chapitre 14 appellera la panne silencieuse, et le chapitre 15 l'échec silencieux d'un modèle.

## 8.6 Les limites de la représentation

Deux idées, qui portent loin.

**On ne comprime pas indéfiniment.** Une donnée peut être comprimée sans perte tant qu'elle contient de la redondance ou de la structure. Une fois cette structure exploitée, il existe un plancher en dessous duquel toute compression supplémentaire détruit de l'information. Ce plancher dépend du contenu, pas de l'ingéniosité de l'algorithme. C'est pourquoi les gains de compression sont incrémentaux et non exponentiels, et pourquoi une promesse de compression d'un facteur cent sans perte, sur des données déjà comprimées, est disqualifiée sans examen.

**Aucun traitement ne recrée l'information absente.** Un traitement peut révéler de l'information présente mais noyée dans le bruit. Il ne peut pas restituer ce que le capteur n'a jamais acquis. Ce qu'un algorithme produit dans ce cas est une **inférence** : une reconstruction plausible fondée sur ce qu'il a appris d'autres données. Elle peut être utile, et elle n'est pas une mesure.

Cette distinction est fondamentale et deviendra centrale dans plusieurs familles :

| | Mesure | Inférence |
|---|---|---|
| Origine | acquise par un capteur | reconstruite à partir d'un modèle |
| Fiabilité | bornée par le bruit et la résolution | bornée par la représentativité du modèle |
| Comportement en cas d'écart | dégradation visible | production d'un résultat plausible et faux |

**Toute représentation est une perte assumée.** Un modèle, une simulation, un jumeau numérique sont des représentations : ils conservent ce que leur concepteur a jugé pertinent. La question n'est jamais « le modèle est-il exact ? » — il ne l'est pas — mais **« qu'a-t-il été construit pour ignorer, et cet aspect est-il négligeable dans mon cas ? »**

---
