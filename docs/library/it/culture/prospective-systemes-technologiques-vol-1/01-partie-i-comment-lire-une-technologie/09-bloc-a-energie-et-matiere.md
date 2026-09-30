---
title: Bloc A — Énergie et matière
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 8.1 Ce que la thermodynamique interdit

Deux règles suffisent. Elles sont, avec la vitesse limite de propagation, parmi les rares choses de ce cours qui soient réellement des **lois physiques** au sens du chapitre 7 : sans exception connue, et donc utilisables pour exclure une possibilité.

**Première règle : l'énergie ne se crée pas.** Elle se transforme, se déplace, change de forme. Toute proposition impliquant une production nette d'énergie à partir de rien est disqualifiée immédiatement, sans examen supplémentaire. Cette catégorie est étroite — c'est important de le redire, car le chapitre 3 vous a mis en garde contre la confusion entre « physiquement impossible » et « très difficile ». L'immense majorité des difficultés technologiques appartient à la seconde catégorie.

**Seconde règle, plus riche : toutes les énergies ne se valent pas.** Un joule d'électricité et un joule de chaleur tiède contiennent la même quantité d'énergie et n'ont pas la même **valeur d'usage**. L'électricité peut être convertie presque intégralement en mouvement, en lumière, en chaleur. La chaleur tiède ne peut être convertie qu'en une petite fraction de travail.

Pourquoi ? Parce que **convertir de la chaleur en travail exige un écart de température**, et que la fraction convertible croît avec cet écart. Une source très chaude face à un environnement froid permet d'extraire beaucoup ; une source tiède, presque rien. C'est la raison pour laquelle les moteurs thermiques plafonnent, dans la pratique industrielle, autour de trente à soixante pour cent selon les technologies et les températures — et non parce que les ingénieurs manqueraient d'idées.

**Ce que vous devez en retenir, opérationnellement :**

> Deux quantités exprimées en kWh ne sont pas comparables si elles ne sont pas de même nature. Demandez toujours : de l'électricité, de la chaleur, à quelle température ?

Cette question paraît pédante. Elle permet de démonter en dix secondes un nombre considérable d'affirmations sur l'énergie, la récupération de chaleur ou le stockage.

## 8.2 Les conversions en cascade — et pourquoi tout finit en chaleur

Chaque conversion perd. Et les pertes ne s'additionnent pas : **elles se multiplient**.

C'est un point d'arithmétique élémentaire dont les conséquences sont majeures. Une chaîne de trois conversions à 80 % de rendement chacune ne rend pas 80 %, ni 60 % :

```text
   0,80 × 0,80 × 0,80 = 0,51
```


Un peu plus de la moitié. Avec quatre étapes, on tombe sous 41 %.

**Exemple structurant, à garder en tête pour tout le volume.** Comparons deux façons d'utiliser de l'électricité pour faire avancer un véhicule.

| Chaîne | Étapes | Rendement approximatif |
|---|---|---|
| Électricité → batterie → moteur | charge/décharge ~90 %, moteur et transmission ~90 % | **≈ 80 %** |
| Électricité → hydrogène → électricité → moteur | électrolyse ~70 %, compression/transport ~90 %, pile à combustible ~55 %, moteur ~90 % | **≈ 30 %** |

⏱ *Ordres de grandeur indicatifs, variables selon les technologies et les conditions ; le rapport entre les deux chaînes est le point, pas les valeurs exactes.*

Un facteur d'environ deux et demi sur l'électricité consommée pour le même service rendu. Ce calcul ne tranche pas le débat sur ces filières — chacune a des propriétés que l'autre n'a pas, notamment sur la masse embarquée et la durée de recharge, et nous y reviendrons au chapitre 12. Mais il pose une contrainte que **aucun progrès d'ingénierie n'effacera** : ajouter des étapes de conversion coûte, et ce coût est multiplicatif.

**La règle d'analyse :** devant toute chaîne technologique, comptez les conversions. Chacune est un facteur.

### Tout finit en chaleur

Les pertes de chaque conversion ne disparaissent pas : elles deviennent de la chaleur. Et cette chaleur doit être évacuée, sans quoi la température monte jusqu'à la destruction.

Une conséquence surprend souvent : **un centre de calcul transforme la quasi-totalité de son électricité en chaleur.** Il n'y a pas d'énergie « consommée par le calcul » qui s'en irait ailleurs — le résultat d'un calcul ne pèse rien et n'emporte aucune énergie. Un bâtiment qui appelle 100 MW électriques est un radiateur de 100 MW. C'est pourquoi le refroidissement n'est pas un accessoire de ces installations mais l'une de leurs contraintes structurantes, et pourquoi il réapparaîtra aux chapitres 10, 13 et 32.

**Évacuer la chaleur suppose trois choses**, et chacune est une limite pratique : un écart de température avec le milieu, une surface d'échange, et un fluide capable d'emporter l'énergie. La quantité de chaleur évacuable par unité de surface est bien plus élevée avec un liquide qu'avec de l'air — l'écart se compte en ordres de grandeur —, ce qui explique le basculement progressif des équipements très denses vers le refroidissement liquide. ⚠️ *Écart donné en ordre de grandeur ; il varie fortement selon les configurations. Le point est le rapport entre les deux modes, non sa valeur exacte.*

**🔥 Cas de panne fondateur — l'emballement thermique.** Un système où la production de chaleur croît avec la température, et où l'évacuation ne suit pas, entre dans une boucle qui s'auto-entretient : plus chaud, donc plus de pertes, donc plus chaud. Ce mécanisme se retrouve, sous des formes différentes, dans les batteries, les composants de puissance, les moteurs et certaines réactions chimiques. Il est la matrice de tous les cas de panne thermique du volume.

## 8.3 La matière n'est pas idéale

Les fiches techniques donnent des propriétés moyennes de matériaux parfaits. Les objets réels sont faits de matière imparfaite, et ce sont les imperfections qui décident.

**Le défaut gouverne, pas la moyenne.** La résistance d'une pièce n'est pas déterminée par la qualité moyenne du matériau mais par son **plus gros défaut**. C'est pourquoi deux pièces issues du même lot peuvent avoir des tenues très différentes, et pourquoi le contrôle industriel s'intéresse à la dispersion autant qu'à la moyenne. Le chapitre 24 en tirera une conséquence économique majeure.

**La fatigue : ce sont les cycles qui tuent.** Une pièce soumise à des sollicitations répétées bien inférieures à sa limite de rupture finit par céder. Ce n'est pas de l'usure au sens courant : c'est l'accumulation de micro-dommages à chaque cycle. La fatigue explique pourquoi la durée de vie de nombreux objets se compte en **nombre de cycles** et non en années : cycles de charge d'une batterie, cycles de vol d'une structure, cycles thermiques d'une soudure électronique.

**La dégradation dépend de l'environnement.** Corrosion, oxydation, rayonnement, humidité, ultraviolets. Un matériau qualifié dans un environnement ne l'est pas dans un autre. C'est une des raisons pour lesquelles la qualification d'un composant pour l'espace, le médical ou l'automobile prend des années — et pourquoi le délai de qualification du chapitre 25 est ce qu'il est.

**La pureté coûte, de façon très non linéaire.** Passer de 99 % à 99,9999 % de pureté ne coûte pas six fois plus : chaque ordre de grandeur supplémentaire exige des procédés différents. C'est une des raisons du coût des matériaux électroniques.

**Ce que ce paragraphe vous permet de faire :** relier trois choses que le chapitre 6 avait laissées séparées. Un record de laboratoire porte sur un exemplaire idéal ; un produit industriel porte sur une population dispersée ; et une durée de vie se mesure en cycles dans un environnement donné. Les trois écarts viennent de la même source — la matière réelle.

---
