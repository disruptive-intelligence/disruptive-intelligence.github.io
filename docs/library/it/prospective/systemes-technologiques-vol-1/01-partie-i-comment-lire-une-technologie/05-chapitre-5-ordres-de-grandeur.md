---
title: Chapitre 5 — Ordres de grandeur
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

## 5.1 Pourquoi l'intuition quantitative précède l'avis

Vous n'avez pas besoin de mathématiques pour analyser une technologie. Vous avez besoin de savoir compter en ordres de grandeur — c'est-à-dire de savoir si l'on parle de dix, de mille ou d'un million, et de sentir immédiatement quand un facteur mille a été escamoté dans une phrase.

C'est une compétence, elle s'acquiert en quelques heures, et elle a un rendement disproportionné. La plupart des affirmations technologiquement absurdes le deviennent visiblement dès qu'on écrit deux nombres l'un en dessous de l'autre. Inversement, certaines affirmations qui paraissent absurdes se révèlent solides au calcul — et le cas traité en 5.6 en est un exemple.

Ce chapitre introduit le premier des motifs récurrents du cours : ***le facteur ×1000***. Il reviendra dans chaque famille technologique de la Partie II et structurera le chapitre 31.

> **P3 — Sans ordre de grandeur, il n'y a pas d'avis, seulement une impression.**

## 5.2 Le kit minimal

Neuf grandeurs suffisent à couvrir l'essentiel de ce cours. Pour chacune, ce qui compte est moins l'unité que **la confusion à éviter**.

| Grandeur | Unité | La confusion à éviter |
|---|---|---|
| Énergie | joule (J), wattheure (Wh) | une quantité, un stock |
| Puissance | watt (W) | un débit d'énergie — 1 W = 1 J/s |
| Densité d'énergie | Wh/kg, Wh/L | combien on emporte |
| Densité de puissance | W/kg | à quelle vitesse on peut le rendre |
| Débit | bit/s | quantité par unité de temps |
| Latence | seconde | délai avant le premier bit — indépendant du débit |
| Rendement | % | rapport de sortie sur entrée, jamais supérieur à 1 |
| Cadence | unités/an | ce qui décide de l'échelle industrielle |
| Taux de défaut | ppm, % | ce qui décide du coût réel |

### La confusion énergie / puissance

C'est la plus coûteuse de toutes, et elle traverse tout ce cours.

L'énergie est un stock : ce que contient une batterie, ce que consomme un bâtiment sur un an. La puissance est un flux : ce qu'un appareil appelle à l'instant t.

Un exemple qui règle la question définitivement. Une batterie de véhicule électrique contient de l'ordre de 60 kWh. Recharger cette batterie en cinq minutes exige :

```text
   60 kWh ÷ (5 min) = 60 kWh ÷ (1/12 h) = 720 kW
```


Sept cent vingt kilowatts. À titre de comparaison, la puissance souscrite d'un logement français est typiquement de 6 à 9 kW. Une seule borne de recharge en cinq minutes appellerait donc l'équivalent instantané de l'ordre d'une centaine de logements — et une station de dix bornes, plusieurs mégawatts, soit le raccordement d'une petite zone industrielle.

Ce calcul tient en une ligne et il déplace complètement le problème. La recharge ultra-rapide n'est pas d'abord une question de chimie de batterie : c'est une question de **raccordement au réseau électrique**, de transformateur, de génie civil et de tarification de la puissance souscrite. Vous venez de découvrir, avec une division, que le verrou n'est pas là où on le cherche spontanément — exactement ce qu'annonçait la section 3.5.

### La confusion débit / latence

Familière au lecteur venant de l'informatique, et transférable partout. Le débit se négocie en achetant de la capacité ; la latence, en dessous d'un certain seuil, ne s'achète pas, parce qu'elle est bornée par la vitesse de propagation du signal. Nous y revenons en 5.5.

## 5.3 Les préfixes, et pourquoi ils trompent

| Préfixe | Facteur |
|---|---|
| kilo (k) | 10³ |
| méga (M) | 10⁶ |
| giga (G) | 10⁹ |
| téra (T) | 10¹² |
| péta (P) | 10¹⁵ |

Trois lettres de différence entre le kilowatt et le gigawatt, et un facteur un million. Le langage courant traite ces préfixes comme des degrés d'intensité — « c'est plus gros » — alors qu'ils marquent des changements de nature.

Un exemple structurant pour la suite du cours. Un centre de données de 1 MW est un bâtiment : il se raccorde au réseau de distribution local, il se refroidit avec des équipements standard, il s'installe en zone d'activité. Un centre de données de 1 GW n'est pas mille fois ce bâtiment : c'est un objet dont l'alimentation devient elle-même un problème d'infrastructure nationale, comparable en puissance appelée à un réacteur nucléaire de grande taille. Le raccordement se négocie en années, le refroidissement pose des questions d'eau ou d'air, et l'implantation devient une décision d'aménagement du territoire.

> **Le facteur ×1000 ne multiplie pas le problème : il en change la nature.**

C'est le motif que vous retrouverez partout, et il est démontré en détail au chapitre 31.

## 5.4 Estimer à la volée : méthode en quatre temps

Vous n'avez besoin ni de précision ni de calculatrice. Vous avez besoin d'un résultat juste **à un facteur trois près**, obtenu en moins de deux minutes.

**Temps 1 — Borner.** Trouvez une valeur manifestement trop petite et une manifestement trop grande. Souvent, l'écart entre les deux suffit déjà à répondre.

**Temps 2 — Décomposer.** Coupez la quantité inconnue en facteurs que vous savez estimer. Combien d'unités, chacune de quelle taille, pendant combien de temps.

**Temps 3 — Ancrer.** Rattachez chaque facteur à un repère que vous connaissez (voir 5.5).

**Temps 4 — Vérifier les unités.** Écrivez les unités et simplifiez-les. Si le résultat n'est pas dans l'unité attendue, le raisonnement est faux, et cette vérification attrape la majorité des erreurs.

### Exemple déroulé

*Question : l'électricité consommée par une voiture électrique représente-t-elle une part significative de la consommation d'un foyer ?*

**Décomposition.** Une voiture consomme de l'ordre de 15 à 20 kWh aux 100 km. Un automobiliste parcourt de l'ordre de 12 000 à 15 000 km par an.

```text
   15 000 km × 18 kWh/100 km ≈ 2 700 kWh/an
```


**Ancrage.** Un foyer français consomme de l'ordre de quelques milliers de kWh d'électricité par an hors chauffage électrique.

**Conclusion.** Une voiture électrique est du même ordre de grandeur que la consommation électrique domestique d'un foyer — elle ne la multiplie pas par dix, elle la double approximativement. Cela ne dit rien du dimensionnement du réseau, qui dépend de la **puissance appelée simultanément** et non de l'énergie annuelle. Deux grandeurs, deux problèmes distincts. ⏱ *Valeurs indicatives, ordre de grandeur.*

## 5.5 Cinq repères à mémoriser réellement

Ces cinq repères sont durables — ils reposent sur des propriétés physiques ou des ratios structurels — et ils permettent d'ancrer la plupart des estimations de ce cours.

### ① Un humain fournit environ 100 W

Un adulte au repos dissipe de l'ordre de 100 W ; à l'effort soutenu, il fournit de l'ordre de 100 à 200 W de puissance mécanique. Repère utile pour sentir ce que représente un moteur : une automobile de 100 kW équivaut à plusieurs centaines de personnes fournissant leur puissance maximale.

### ② Le soleil délivre environ 1 kW/m² au sol, en plein ensoleillement

Un panneau photovoltaïque de rendement 20 % produit donc de l'ordre de 200 W par m² **en crête**. Sur une année, en tenant compte de la nuit, de la saison et de la météo, on obtient de l'ordre de 150 kWh/m²/an sous latitude tempérée et jusqu'à 250 kWh/m²/an en zone très ensoleillée. Ce repère, à lui seul, permet d'évaluer n'importe quelle affirmation sur le solaire.

### ③ L'essence contient environ 12 kWh/kg ; une cellule lithium-ion, environ 0,2 kWh/kg

Un facteur d'environ soixante en énergie massique. Mais un moteur thermique convertit environ 25 à 30 % de cette énergie en mouvement, contre environ 90 % pour une chaîne électrique : l'écart **utile** se resserre autour d'un facteur quinze à vingt. C'est le repère qui explique simultanément pourquoi l'électrification de l'automobile est possible et pourquoi celle de l'aviation long-courrier est un problème d'une tout autre difficulté.

### ④ Un grand réacteur nucléaire produit environ 1 GW électrique

Repère d'échelle pour toute discussion sur l'énergie. Une grande éolienne terrestre est de l'ordre de quelques MW en puissance nominale, avec un facteur de charge de l'ordre de 25 %. Comparer des puissances installées sans comparer les facteurs de charge est l'une des erreurs les plus répandues du débat énergétique.

### ⑤ La lumière parcourt environ 300 000 km/s dans le vide, environ 200 000 km/s dans une fibre

Soit environ 200 km par milliseconde. Paris–New York fait environ 5 800 km : le trajet aller ne peut pas prendre moins d'une trentaine de millisecondes, et un aller-retour moins d'une soixantaine, quel que soit l'équipement. C'est une borne physique, pas une limite d'ingénierie. Elle explique pourquoi certaines architectures distribuées ne peuvent pas fonctionner, pourquoi le calcul est parfois rapproché de la donnée, et pourquoi la latence d'un satellite en orbite basse diffère structurellement de celle d'un satellite géostationnaire.

⚠️ *Ces cinq repères sont donnés en ordre de grandeur et non comme données de référence. Ils servent à ancrer une estimation, jamais à fonder un calcul précis.*

## 5.6 Trois affirmations passées au calcul

L'exercice qui suit est le cœur du chapitre. Notez que les trois verdicts sont différents — c'est précisément l'intérêt.

### Affirmation 1 — « Il suffirait de couvrir une petite partie du Sahara pour produire l'électricité mondiale »

**Calcul.** La production mondiale d'électricité est de l'ordre de 30 000 TWh par an, soit 3 × 10¹³ kWh. Avec un rendement surfacique de l'ordre de 250 kWh/m²/an en zone désertique :

```text
   3 × 10¹³ kWh ÷ 250 kWh/m² ≈ 1,2 × 10¹¹ m² ≈ 120 000 km²
```


Le Sahara couvre environ 9 000 000 km². Le calcul donne donc de l'ordre de 1 à 2 % de sa surface.

**Verdict : l'affirmation est arithmétiquement correcte.** Et c'est exactement là que le raisonnement devient intéressant. Le calcul valide la partie de l'affirmation qui semblait douteuse, et il déplace la difficulté vers ce dont l'affirmation ne parle pas : le transport de l'électricité sur des milliers de kilomètres, le stockage pour la nuit, l'eau de nettoyage en milieu désertique, la maintenance, les matériaux nécessaires — et le fait que l'électricité ne représente aujourd'hui qu'environ un cinquième de la consommation énergétique finale mondiale.

**Leçon.** Un ordre de grandeur ne sert pas seulement à démolir. Il sert à **localiser la difficulté réelle**, ce qui est souvent plus utile.

⏱ *Production électrique mondiale et part de l'électricité dans l'énergie finale : ordres de grandeur, à réactualiser.*

### Affirmation 2 — « Nous alimenterons ce centre de données avec des panneaux solaires sur site »

**Calcul.** Prenons un centre de données de 100 MW, ce qui est un objet réaliste. Il consomme cette puissance en continu, soit environ 876 GWh par an. Avec 200 kWh/m²/an :

```text
   8,76 × 10⁸ kWh ÷ 200 kWh/m² ≈ 4,4 × 10⁶ m² ≈ 4,4 km²
```


Quatre virgule quatre kilomètres carrés de panneaux, sans compter le stockage nécessaire pour les heures sans soleil, alors que le bâtiment lui-même occupe quelques hectares.

**Verdict : l'affirmation est fausse telle qu'énoncée.** « Sur site » est impossible d'un facteur cent en surface. L'affirmation devient défendable si on la reformule en « alimenté par un parc solaire dédié situé ailleurs, avec raccordement et stockage » — ce qui est un tout autre projet, avec un tout autre coût.

**Leçon.** Le calcul n'a pas invalidé l'intention ; il a invalidé **deux mots**, « sur site ». C'est la forme la plus fréquente et la plus utile de la réfutation quantitative.

### Affirmation 3 — « Cette batterie se recharge en cinq minutes »

Reprenons le calcul de 5.2 : 720 kW pour 60 kWh en cinq minutes.

**Verdict : l'affirmation peut être vraie au niveau de la cellule et fausse au niveau du système.** Une chimie peut effectivement accepter cette puissance de charge ; l'infrastructure capable de la délivrer est un autre objet. L'affirmation est donc un cas typique de **saut de niveau d'abstraction** au sens du chapitre 2 : elle est énoncée au niveau de la brique et interprétée au niveau du système.

**Leçon.** Les deux instruments se combinent. L'échelle d'abstraction dit *à quel niveau l'affirmation est vraie* ; l'ordre de grandeur dit *ce que coûterait de la rendre vraie au niveau supérieur*.

## 5.7 Ce qu'un ordre de grandeur ne prouve pas

Quatre limites, à connaître pour ne pas surinvestir cet outil.

**Il ne dit rien de la faisabilité industrielle.** Un calcul peut montrer qu'une quantité est disponible sans montrer qu'on sait la produire, la transporter ou la financer. La surface du Sahara existe ; la chaîne industrielle qui la couvrirait est une autre question.

**Il ne dit rien du coût.** Le coût dépend de mécanismes — apprentissage, capital, rendement de production — qui ne se déduisent d'aucune quantité physique. C'est l'objet du chapitre 22.

**Il est sensible aux hypothèses cachées.** Un facteur de charge, un rendement, une durée de vie mal choisis déplacent le résultat d'un ordre de grandeur. D'où la règle : écrivez toujours vos hypothèses à côté du résultat, et testez la conclusion en faisant varier la plus fragile.

**Il ne remplace pas la question ④.** Un calcul juste peut soutenir une conclusion fausse si l'on n'a pas cherché ce qui l'invaliderait. La quantification est un instrument au service des quatre questions, jamais un substitut.

🧪 **Lab 3 — Estimation**

**Objectif.** Évaluer la plausibilité d'affirmations technologiques sans autre ressource que le kit du chapitre.
**Durée.** 60 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitre 5. **Aucune recherche autorisée pendant les vingt premières minutes.**
**Contexte.** Cinq affirmations vous sont fournies, mêlant des énoncés corrects, des énoncés faux d'un facteur cent, et des énoncés dont la faiblesse n'est pas quantitative.
**Travail demandé.** Pour chacune : (a) estimer sans documentation, en écrivant hypothèses et unités ; (b) classer en *plausible / faux d'un facteur N / non tranchable par le calcul* ; (c) pour celles jugées fausses, identifier les deux ou trois mots à modifier pour les rendre défendables ; (d) après vingt minutes, vérifier deux repères sur source primaire et noter l'écart avec votre estimation.
**Livrable.** Une page de calculs lisibles, hypothèses apparentes.
**Compétences validées.** Décomposition, ancrage, contrôle dimensionnel, reformulation minimale d'un énoncé faux, calibration de sa propre confiance.
**Éléments attendus.** Une estimation à un facteur trois près est un succès complet ; la précision n'est pas l'objectif. L'erreur la plus fréquente est l'oubli du contrôle des unités, qui produit des résultats faux d'un facteur mille sans que l'auteur le remarque. La catégorie *non tranchable par le calcul* est celle qui distingue une bonne copie : au moins une des cinq affirmations est fausse pour une raison institutionnelle ou économique qu'aucun ordre de grandeur ne peut révéler — la repérer vaut mieux que de produire cinq calculs justes.

🎓 **À ce stade, vous savez…**

* distinguer énergie et puissance, débit et latence, et calculer une puissance de charge ;
* manier les préfixes en sachant qu'un facteur mille change la nature d'un problème ;
* estimer une quantité en quatre temps, avec contrôle dimensionnel ;
* mobiliser cinq repères durables pour ancrer une estimation ;
* localiser la difficulté réelle d'une affirmation, y compris quand son arithmétique est correcte ;
* énoncer ce qu'un calcul ne prouve pas.

**Ce que vous ne savez pas encore :** évaluer une affirmation qui ne se calcule pas — une démonstration, un benchmark, un communiqué. C'est l'objet du chapitre 6, qui est le plus important de cette partie.

---

---

---
