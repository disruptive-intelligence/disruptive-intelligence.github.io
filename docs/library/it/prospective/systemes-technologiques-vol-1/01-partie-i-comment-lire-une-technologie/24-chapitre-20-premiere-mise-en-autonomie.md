---
title: Chapitre 20 — Première mise en autonomie
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

que comprend-on avec la carte seule ?

Vous venez de traverser onze familles technologiques. Ce chapitre a trois fonctions : vous montrer ce que la carte rend visible, vous faire l'utiliser sur un objet qu'elle ne contient pas, et vous faire constater précisément ce qu'elle ne suffit pas à établir.

Cette dernière fonction est la plus importante. Elle justifie l'existence de la partie suivante.

---

### 20.1 Ce que la grille commune rend visible

Les onze chapitres ont suivi la même structure. Ce n'était pas une commodité de rédaction : c'était le moyen de rendre comparables des domaines qui ne le sont pas spontanément.

Voici ce que cette comparaison fait apparaître.

| Famille | Contrainte dominante | Ce qui gouverne son coût | Sa dépendance la plus critique |
|---|---|---|---|
| Information et calcul | déplacement des données | matériel sous-jacent | semi-conducteurs |
| Semi-conducteurs | rendement × surface | capital d'usine | lithographie, un fournisseur |
| Matière et fabrication | défauts, tolérances | capital d'outillage, matière | énergie, raffinage |
| Énergie | densité, conversion, évacuation | capital, facteur de charge | matériaux, foncier, réseau |
| Réseaux et datacenters | latence physique, évacuation thermique | raccordement, génie civil | électricité, spectre, foncier |
| Capteurs et perception | bruit, dynamique, dérive | volume, étalonnage | semi-conducteurs, optique |
| Intelligence artificielle | bande passante mémoire, données | calcul, énergie par appel | semi-conducteurs, énergie |
| Contrôle et robotique | énergie embarquée, délai de boucle | intégration, maintenance | capteurs, actionneurs, énergie |
| Biologie | variabilité, purification | attrition, cadre réglementaire | chimie, instrumentation, cadre |
| Spatial | fraction de masse utile, irréparabilité | cadence de production | lanceurs, stations sol, attributions |
| Calcul non classique | selon l'approche : bruit, précision, décohérence | écosystème absent | tout l'écosystème du calcul classique |

**Trois observations en découlent, et aucune n'était visible avant.**

**Presque toutes ces familles dépendent des semi-conducteurs et de l'énergie.** Ces deux-là sont en amont de tout le reste. C'est ce que le chapitre 32 appellera des technologies habilitantes — mais vous pouvez le constater ici, avant même qu'on vous donne le nom.

**Le coût est presque partout gouverné par le capital**, et non par la matière ou le travail. Cela explique pourquoi l'analyse par les conditions ④ et ⑥ est si productive, et pourquoi le volume produit est une variable si centrale.

**La dépendance la plus critique n'est presque jamais dans la famille elle-même.** Elle est ailleurs, dans une autre colonne — c'est la version cartographiée du paradoxe de la criticité du chapitre 25.

---

### 20.2 Les mêmes murs sous des noms différents

Voici le principal acquis intellectuel de cette partie.

Une remarque avant de commencer, et elle a son importance.

Le chapitre 8 recensait **trois** familles de contraintes : énergie et matière, information et mesure, espace-temps-échelle. Vous allez en trouver **cinq** ici.

Ce n'est pas une correction du chapitre 8. Les trois premières familles sont bien celles que la physique impose, et elles se retrouvent intactes dans les trois premiers murs. Les deux dernières sont apparues au fil de la traversée des onze familles, et elles ne sont pas physiques : **le rendement de production est une contrainte industrielle et économique ; la défaillance silencieuse est une contrainte informationnelle.**

Aucune des deux ne se déduit du chapitre 8. Elles ont été rencontrées en observant des domaines réels, et c'est précisément ce qu'on attend d'une carte : produire quelque chose que le socle ne contenait pas.

Les onze familles rencontrent un très petit nombre de contraintes fondamentales. Chacune leur donne un nom de métier, si bien qu'elles paraissent poser des problèmes différents. Elles ne le font pas.

#### Mur 1 — La dissipation thermique

| Domaine | Nom du mur | Ce qu'il borne |
|---|---|---|
| Semi-conducteurs | densité de puissance, enveloppe thermique | l'activité simultanée d'une puce |
| Datacenters | capacité d'évacuation, refroidissement | la densité par baie, donc le bâtiment |
| Énergie | pertes de conversion, chaleur fatale | le rendement de toute chaîne |
| Robotique | échauffement d'actionneur | la densité de puissance utilisable |
| Spatial | contrôle thermique par rayonnement seul | la conception entière du satellite |
| Biologie | thermorégulation de culture | la taille du bioréacteur |

**L'origine commune :** chapitre 8. Tout finit en chaleur, et l'évacuation est bornée par une surface tandis que la production croît avec un volume.

#### Mur 2 — Le coût du déplacement

| Domaine | Nom du mur | Ce qu'il borne |
|---|---|---|
| Calcul | mur de la mémoire | l'efficacité réelle, indépendamment de la puissance |
| Intelligence artificielle | bande passante mémoire à l'inférence | le débit utile |
| Énergie | pertes de transport, congestion réseau | l'utilisabilité d'une production distante |
| Robotique et spatial | masse embarquée | l'autonomie, par la boucle masse-énergie |
| Chaînes d'approvisionnement | délai de qualification | la capacité à substituer un fournisseur |
| Biologie | transport et purification | le coût de production |

**L'origine commune :** déplacer coûte, et ce coût baisse plus lentement que celui de traiter.

#### Mur 3 — Le bruit et l'incertitude

| Domaine | Nom du mur | Ce qu'il borne |
|---|---|---|
| Capteurs | rapport signal sur bruit, plancher de détection | ce qui est mesurable |
| Réseaux | limite débit-bruit | le débit maximal sur un canal |
| Intelligence artificielle | qualité et représentativité des données | ce qui est apprenable |
| Calcul analogique | précision non reproductible | l'usage possible |
| Quantique | décohérence | la durée d'un calcul |
| Biologie | variabilité biologique | la reproductibilité |

**L'origine commune :** chapitre 8. Aucune grandeur physique n'est mesurable ni manipulable sans incertitude, et cette incertitude ne s'annule pas — elle se compense au prix de temps, de redondance ou d'énergie.

#### Mur 4 — Le rendement de production

| Domaine | Nom du mur | Ce qu'il gouverne |
|---|---|---|
| Semi-conducteurs | rendement de plaquette | le coût unitaire, violemment |
| Fabrication | non-qualité, rebut | le coût et le délai |
| Énergie | facteur de charge | l'énergie réellement produite |
| Biologie | rendement de lot, attrition clinique | le coût de ce qui aboutit |
| Spatial | cadence de production | l'existence même d'un apprentissage |
| Robotique | disponibilité machine | la valeur réellement délivrée |

**L'origine commune :** ce n'est jamais ce qu'on produit qui compte, c'est ce qui sort conforme.

#### Mur 5 — La défaillance silencieuse

| Domaine | Nom du mur | Pourquoi c'est le pire mode |
|---|---|---|
| Capteurs | dérive, saturation | valeur plausible, aucune alarme |
| Intelligence artificielle | sortie hors distribution | réponse plausible, même assurance |
| Traitement du signal | estimateur trop confiant | trajectoire lisse et fausse |
| Mécanique | jeu, flexion sous charge | position correcte selon les capteurs |
| Positionnement | dérive après perte de signal | position fausse, progressive |
| Biologie | contamination ou dérive de lot | contrôles de routine conformes |
| Calcul | corruption non détectée | résultat exploitable et faux |

**L'origine commune :** un système qui cesse de fonctionner correctement mais continue de produire quelque chose de crédible est plus dangereux qu'un système qui s'arrête. **Ce mur est le seul des cinq qui ne soit pas physique. Il est de nature informationnelle** — et c'est celui qui traverse le plus de familles.

🖼 **SCHÉMA — Les cinq murs et les onze familles.** Reprendre le schéma annoncé au chapitre 8, complété. Cinq colonnes — dissipation, déplacement, incertitude, rendement, défaillance silencieuse — et onze lignes. À chaque intersection significative, le nom de métier du mur dans ce domaine. Faire apparaître visuellement que les colonnes sont peu nombreuses et les noms nombreux. Ce schéma est le résumé graphique de la Partie II.

---

### 🧪 Lab 9 — Où vos modèles cessent de fonctionner
**Objectif.** Éprouver le transfert des modèles mentaux d'origine, et en localiser précisément la frontière.
**Durée.** 45 minutes. **Difficulté.** 2/3. **Prérequis.** Partie II complète.
**Contexte.** Six affirmations vous sont proposées, chacune transposant un raisonnement familier du monde informatique à un autre domaine. Trois transferts sont valides, trois ne le sont pas.

**Travail demandé.**
(a) Classer chaque affirmation en transfert valide, transfert partiel ou transfert invalide.
(b) Pour les transferts partiels, dire exactement à partir de quel point le raisonnement cesse de tenir.
(c) Pour les transferts invalides, identifier la propriété du monde numérique qui n'a pas d'équivalent — coût marginal nul, déploiement instantané, absence de matière, réversibilité.
(d) Proposer un septième transfert, tiré de votre propre expérience, et l'évaluer vous-même.

**Livrable.** Un tableau et un paragraphe pour (d).

**Éléments attendus.** Les transferts partiels sont les plus instructifs : la dépendance transitive se transfère en structure et pas en délai (chapitre 25.6), l'abstraction en couches se transfère jusqu'à la physique qui ne s'abstrait pas, la latence se transfère mais devient bornée par la distance. En (d), une auto-évaluation lucide vaut mieux qu'un exemple brillant : c'est la compétence que le chapitre 42.3 demandera.

---

### 20.3 Exercice dirigé : une technologie que la carte ne contient pas

Vous allez maintenant appliquer la carte à un objet dont aucun chapitre ne traite.

#### L'objet

**La pompe à chaleur.**

Le principe, en une phrase : un dispositif qui prélève de la chaleur dans un milieu froid et la restitue dans un milieu plus chaud, en consommant du travail. Il ne produit pas de chaleur : il la **déplace**. C'est un réfrigérateur utilisé dans l'autre sens.

C'est tout ce que vous recevez. Aucun chapitre de la Partie II ne traite de ce sujet.

#### Étape 1 — De quoi parle-t-on ? (chapitre 2)

Un dispositif intégré, achetable, installable : c'est une **plateforme**. Le fluide et le compresseur sont des **briques**. « Chauffer avec moins d'énergie » est une **capacité**. « Électrification du chauffage » est un **récit** — un cadrage qui recouvre plusieurs technologies.

*Conséquence immédiate :* les questions pertinentes sont celles d'une plateforme — prix, maintenance, performance en conditions réelles, service — et non celles d'une brique.

#### Étape 2 — Quel mécanisme, et quelles contraintes ? (chapitre 8, chapitre 12)

Le chapitre 8 fournit l'essentiel. Déplacer de la chaleur d'un milieu froid vers un milieu chaud demande du travail, et **la quantité de travail nécessaire dépend de l'écart de température** — c'est le même principe qui bornait les moteurs thermiques, appliqué en sens inverse.

**Conséquence, déduite et non apprise :** l'efficacité du dispositif se dégrade quand l'écart augmente. Il est donc d'autant moins performant qu'il fait froid dehors et que l'on veut chaud dedans. **C'est précisément quand on en a le plus besoin qu'il fonctionne le moins bien.**

Vous venez de déduire, de la seule thermodynamique du chapitre 8, la difficulté centrale de cette technologie. Vous ne connaissiez pas le sujet il y a trois paragraphes.

Le chapitre 12 ajoute : c'est un dispositif de conversion, il a un rendement, et il s'insère dans une chaîne. Sa consommation est électrique, donc sa performance globale dépend aussi de la manière dont cette électricité est produite — c'est un raisonnement de coût système au sens du chapitre 22.

#### Étape 3 — Quels ordres de grandeur ? (chapitre 5)

Vous pouvez poser les grandeurs pertinentes sans les connaître :

* le rapport entre chaleur restituée et travail consommé, et **sa variation avec la température extérieure** ;
* la puissance appelée, et son maximum lors des pointes de froid ;
* l'effet d'agrégation : si de nombreux dispositifs appellent leur puissance maximale au même moment, quel est l'effet sur le réseau ?

**Cette dernière question est la plus intéressante**, et elle ne vient pas du dispositif : elle vient du chapitre 12. Le réseau doit équilibrer à chaque instant, et une pointe de demande simultanée est un problème distinct de la consommation annuelle.

#### Étape 4 — Quelles autres familles interviennent ? (Partie II)

* **Énergie** : conversion, chaîne, réseau, pointe de puissance.
* **Matière et fabrication** : échangeurs, compresseur, fluide, procédés de série.
* **Contrôle** : régulation, dégivrage, adaptation aux conditions — une boucle au sens du chapitre 16.
* **Capteurs** : mesures de température, avec dérive possible.
* **Semi-conducteurs** : électronique de puissance pour piloter le compresseur à vitesse variable — chapitre 10.9.

**Ce que la carte vous a permis de faire :** identifier cinq familles impliquées, alors que le sujet paraissait relever d'une seule.

#### Étape 5 — Quels murs ? (section 20.2)

* **Dissipation et conversion** : le rendement dépend de l'écart de température — mur 1.
* **Rendement de production** : coût dominé par la fabrication en série et l'installation — mur 4.
* **Défaillance silencieuse** : un dispositif mal réglé, mal dimensionné ou dont un capteur dérive continue de chauffer, en consommant beaucoup plus que prévu. **Rien n'alerte** : l'occupant a chaud, la facture monte, et l'écart avec la performance annoncée n'est attribué à rien de précis — mur 5.

Ce dernier point est remarquable : vous venez d'identifier, sur une technologie que vous ne connaissiez pas, un mode de défaillance que le chapitre 14 vous a appris à chercher.

---

### 20.4 Ce que vous avez pu établir — et ce que vous n'avez pas pu

Voici le bilan honnête de l'exercice.

#### Ce que la carte a permis

| Question | Réponse obtenue |
|---|---|
| De quel type d'objet s'agit-il ? | oui, par le chapitre 2 |
| Comment cela fonctionne-t-il ? | oui, par le chapitre 8 |
| Quelle est la difficulté physique centrale ? | oui, déduite |
| Quelles grandeurs surveiller ? | oui |
| Quelles familles sont impliquées ? | oui, cinq |
| Quels murs va-t-elle rencontrer ? | oui, trois |
| Quel mode de défaillance craindre ? | oui |

C'est déjà considérable pour un sujet abordé en quelques minutes sans documentation.

#### Ce que la carte n'a pas permis

Et c'est là que ce chapitre gagne son intérêt.

**Le coût baissera-t-il, et par quel mécanisme ?** La carte donne la structure de coût. Elle ne dit rien de la trajectoire — cela suppose de savoir si un apprentissage par production est possible, à quel taux, et si une rampe d'accès existe. **Chapitre 22.**

**Qui achète, et à la place de quoi ?** Le dispositif remplace une installation existante. Il faut donc comparer à l'alternative en place, intégrer le coût de bascule — travaux, adaptation de l'installation, apprentissage — et savoir qui paie. **Chapitre 23.**

**Sait-on en produire et en installer assez ?** La fabrication est une chose ; le nombre d'installateurs qualifiés en est une autre, et c'est souvent lui qui borne le déploiement. **Chapitres 24 et 26.**

**Le réseau électrique suit-il ?** La pointe de puissance simultanée est un problème d'infrastructure, avec les délais du chapitre 26.

**Que fait la base installée ?** Le parc de chauffage existant a une durée de vie longue. Même une part de marché élevée sur le neuf transformerait le parc lentement — **chapitre 30**, exactement comme le facteur sept observé sur l'automobile.

**Qui garantit, qui certifie, qui assure ?** Performance annoncée contre performance réelle, garanties, qualification des installateurs, dispositifs de soutien public. **Chapitre 28.**

**Ce que cette liste démontre.** Sur sept questions déterminantes pour savoir si cette technologie se diffusera, **la carte n'en résout aucune**. Elle a permis de comprendre l'objet ; elle ne permet pas de comprendre sa trajectoire.

> **Comprendre une technologie et comprendre sa diffusion sont deux compétences distinctes.**
> **Vous venez d'acquérir la première.**

C'est la raison d'être de la Partie III.

---

### 20.5 Ce que la carte n'a pas couvert, et pourquoi ce n'est pas grave

Onze familles ne couvrent pas le monde technologique. Manquent, entre autres : la chimie de procédé, l'agronomie, la construction, le traitement de l'eau, la métrologie, l'acoustique, la cryogénie, la logistique, la médecine, le nucléaire dans son détail industriel, la mécanique des fluides.

**Trois raisons pour lesquelles cette incomplétude est assumée.**

**La carte est un moyen.** Son objet n'était pas l'exhaustivité mais de vous fournir assez de matière pour exercer les instruments de la Partie I et pour faire apparaître les cinq murs. Un douzième chapitre n'aurait pas ajouté de mur.

**Les murs, eux, sont peu nombreux.** L'exercice de la section 20.3 l'a montré : un domaine absent de la carte s'analyse avec ce que la carte a établi. C'est exactement ce qu'on attend d'une méthode transférable.

**Une carte exhaustive serait invalidée par sa propre taille.** Elle deviendrait un catalogue, personne ne la retiendrait, et le lecteur croirait devoir tout connaître avant d'analyser quoi que ce soit — ce qui est faux, et l'exercice de ce chapitre en est la démonstration.

**Le vrai test viendra au chapitre 40**, sur un domaine choisi pour être encore plus éloigné de la carte, avec cette fois la totalité de la méthode. Ce que vous venez de faire en était la répétition partielle.

---

### Fin de la Partie II — Bilan

🎓 **Ce que vous savez faire maintenant**

* Décrire le mécanisme de onze familles technologiques au niveau requis pour raisonner, sans formalisme.
* Nommer, pour chacune, sa contrainte dominante, ce qui gouverne son coût et sa dépendance critique.
* Reconnaître cinq murs fondamentaux sous les noms de métier qu'ils portent dans chaque domaine.
* Identifier, dans un domaine que vous ne connaissez pas, quelles familles interviennent et quels murs il rencontrera.
* Déduire une difficulté centrale à partir d'une contrainte physique générale, plutôt que de la mémoriser.
* Repérer où vos modèles mentaux d'origine se transfèrent et où ils cessent de fonctionner.

**Ce que vous ne savez pas encore**

Vous savez comprendre une technologie. Vous ne savez pas encore dire si elle se diffusera.

L'exercice de la section 20.4 a listé sept questions déterminantes auxquelles la carte ne répond pas : trajectoire de coût, demande solvable, capacité industrielle, compléments, base installée, cadre institutionnel, temps de renouvellement. Ce sont les conditions ③ à ⑨ du chapitre 3, que vous n'avez rencontrées que sous forme de grille.

La Partie III les traite comme des mécanismes. C'est là que ce volume produit ce qu'il a de plus spécifique — et c'est là que se trouvent cinq des dix principes directeurs.

---

---

---


## Ouverture de la Partie III

La Partie II vous a donné une carte. Vous savez maintenant comment fonctionnent, suffisamment pour raisonner, onze familles technologiques, et vous avez constaté qu'elles se heurtent aux mêmes murs sous des noms différents.

Cette partie répond à une autre question. Deux technologies peuvent être également matures sur le plan scientifique et connaître des destins opposés. L'une devient une infrastructure mondiale, l'autre reste une curiosité de laboratoire pendant trente ans, une troisième disparaît après avoir été supérieure à ce qui l'a remplacée. Ce qui les sépare n'est presque jamais la physique.

Nous allons déplier, une par une, les neuf conditions de diffusion du chapitre 3. Vous les avez rencontrées comme une grille ; vous allez maintenant les rencontrer comme des mécanismes, avec leurs seuils, leurs boucles et leurs pathologies.

Cette partie contient cinq des dix principes directeurs du cours. Ce n'est pas un hasard : c'est ici que le volume produit ce qu'il a de plus spécifique.

Nous commençons par les deux conditions qui font échouer le plus grand nombre de projets techniquement réussis : la fiabilité et le coût.

---
