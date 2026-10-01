---
title: Chapitre 26 — Infrastructures complémentaires et compétences
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Une technologie fonctionne rarement seule. Elle a besoin de choses qui doivent exister **autour** d'elle : un réseau, un raccordement, un format, des pièces, des techniciens, une formation. Ces éléments s'appellent des **compléments**, et ils forment la condition ⑦.

Cette condition a une particularité : elle est ennuyeuse. Elle ne comporte ni découverte, ni prouesse, ni percée. C'est précisément pour cette raison qu'elle est la plus systématiquement absente des prévisions.

## 26.1 Le complément manquant

Un complément est un élément extérieur à la technologie, sans lequel elle ne produit aucune valeur pour son utilisateur.

| Technologie | Complément indispensable |
|---|---|
| Véhicule électrique | recharge accessible, réseau électrique dimensionné |
| Centre de calcul | raccordement électrique de forte puissance |
| Robot industriel | intégrateurs, mainteneurs, pièces |
| Dispositif médical | praticiens formés, remboursement, protocole |
| Capteur connecté | couverture réseau, alimentation, exploitation des données |
| Nouveau matériau | procédés de mise en œuvre, normes, assureurs |

**La propriété qui compte : le complément a son propre calendrier**, généralement plus long que celui de la technologie, et il n'est pas contrôlé par celui qui la développe. C'est ce décalage qui produit la plupart des retards de diffusion.

**Le test de diagnostic.** Devant une technologie prête, demandez : *de quoi a besoin l'utilisateur, en plus de cet objet, pour en tirer une valeur ?* Puis, pour chaque élément de la réponse : *qui le construit, à quel horizon, et cette personne a-t-elle une raison de le faire ?*

## 26.2 Le problème d'amorçage

Beaucoup de compléments présentent une structure circulaire bien identifiée : personne n'a intérêt à construire le complément tant que la technologie n'est pas déployée, et la technologie ne se déploie pas tant que le complément n'existe pas.

```text
   pas d'utilisateurs → pas d'infrastructure → pas d'utilisateurs
```


Cette boucle n'est pas une fatalité — elle se débloque, mais toujours par un mécanisme identifiable, et il vaut la peine de les connaître :

**Par une niche qui n'a pas besoin du complément général.** Une flotte captive qui recharge sur son propre site n'a pas besoin d'un réseau public. Un usage industriel en circuit fermé n'a pas besoin d'un standard universel. C'est la même logique que la rampe d'accès du chapitre 22, appliquée à l'infrastructure.

**Par un acteur qui construit les deux côtés.** Coûteux, mais efficace : celui qui vend la technologie finance lui-même le complément, en pariant sur le fait qu'il sera ensuite repris par d'autres.

**Par une décision publique.** Obligation d'équipement, financement d'infrastructure, norme imposant une interface. C'est la deuxième boucle du chapitre 3, et elle relève du chapitre 28.

**Par un complément préexistant détourné.** Le mécanisme le plus rapide, et le plus sous-estimé : une technologie qui peut utiliser une infrastructure déjà là démarre bien plus vite qu'une technologie qui doit créer la sienne. C'est une question à poser systématiquement : *cette technologie peut-elle s'appuyer sur quelque chose qui existe déjà ?*

## 26.3 Les compétences comme infrastructure

Une compétence se comporte exactement comme une infrastructure : elle se constitue lentement, elle est localisée, elle se déprécie, et elle limite le débit de déploiement.

**Le délai est le point dur.** Former un technicien qualifié se compte en années, un ingénieur expérimenté en une décennie. Aucune décision, aucun financement ne raccourcit substantiellement ce délai. Une filière qui doit multiplier ses effectifs qualifiés par cinq ne le fera pas en trois ans, quelle que soit la demande.

**La densité compte autant que le nombre.** Une compétence isolée est peu productive. Ce qui fonctionne est un **écosystème** : praticiens, formateurs, sous-traitants, communauté professionnelle, retours d'expérience partagés. Le chapitre 24 a montré le même phénomène sous le nom de savoir-faire tacite ; c'en est la version à l'échelle d'un pays ou d'un secteur.

**Conséquence analytique.** Quand un plan de déploiement suppose une multiplication rapide des effectifs qualifiés, la compétence est probablement la condition bloquante — et personne ne l'a inscrite au plan, parce qu'elle n'appartient à aucun fournisseur.

## 26.4 Le raccordement électrique : un complément devenu goulet

Le meilleur cas contemporain de complément limitant est le raccordement au réseau électrique des installations de forte puissance. Il illustre les trois mécanismes de ce chapitre à la fois.

**Les faits.** Construire un centre de données se compte aujourd'hui en dix-huit à vingt-quatre mois environ ; obtenir la puissance électrique nécessaire se compte en années. Selon des analyses de marché de 2026, les délais de raccordement dans les marchés d'Europe occidentale s'établissent couramment autour de **sept à dix ans**, et l'IEA relève que dans plusieurs pôles majeurs — Francfort, Londres, Amsterdam, Paris, Dublin — l'attente peut atteindre une décennie. Une responsable d'un grand fournisseur de cloud a publiquement indiqué début 2026 que la construction d'un centre prend environ deux ans, contre jusqu'à sept ans pour en sécuriser l'alimentation.

**Le chiffre qui doit rester en mémoire.** Aux États-Unis, selon les travaux du Lawrence Berkeley National Laboratory, sur l'ensemble des demandes de raccordement déposées entre 2000 et 2019, **environ 13 % seulement avaient atteint l'exploitation commerciale fin 2024, environ 77 % ayant été retirées.** ⏱

**Ce que ce cas enseigne, en trois points.**

**Premier point : le complément est trois à cinq fois plus long que la technologie.** Le rapport des durées est ici de un à quatre environ. Une analyse qui ne raisonne que sur le délai de construction se trompe donc d'un facteur quatre sur le calendrier réel — et c'est exactement le type d'erreur que le chapitre 6 vous a appris à traquer.

**Deuxième point : une file d'attente n'est pas une capacité.** Le stock de projets en file dépasse largement ce qui sera effectivement construit ; la majorité se retire. Confondre un carnet de projets annoncés avec une capacité future est une erreur d'échelon de preuve, au sens du chapitre 6.1.

**Troisième point : le goulet se déplace.** Les analyses récentes indiquent que le point dur n'est plus seulement la file d'attente administrative mais, en aval, la construction de lignes de transport, la capacité des postes et les délais de fabrication des transformateurs de puissance. Réformer la procédure de file d'attente ne résout donc pas le problème : cela le déplace vers une contrainte industrielle. Nous verrons ce mécanisme sous son nom général au chapitre 32.

⏱ *Données vérifiées en août 2026 — domaine à évolution rapide. Voir Annexe I.*

## 26.5 Pourquoi le complément est toujours sous-estimé

Quatre raisons, toutes structurelles.

**Il n'appartient à personne.** Le développeur de la technologie ne le contrôle pas, ne le finance pas et n'a pas de raison d'en parler. Le complément n'a pas de porte-parole.

**Il n'est pas intéressant.** Un transformateur, une file d'attente administrative, un programme de formation : rien de tout cela ne produit d'annonce.

**Il est invisible tant que la technologie n'existe pas à l'échelle.** Un prototype n'a pas besoin d'infrastructure ; mille exemplaires si. Le complément apparaît donc **après** la démonstration, quand les analyses ont déjà été écrites.

**Il obéit à des temporalités de génie civil et de formation**, incompressibles, alors que la technologie obéit à des temporalités d'ingénierie, elles compressibles avec du capital.

**Règle pratique.** Dans une analyse de diffusion, listez les compléments **avant** d'examiner la technologie. S'ils sont absents et que personne n'a de raison de les construire, la trajectoire est bornée par eux, quelle que soit la qualité de l'objet.

## 26.6 Un second complément limitant : les compétences d'installation

Le raccordement électrique est un complément visible, chiffrable, discuté. Celui-ci l'est beaucoup moins, et il borne davantage de trajectoires.

**Le mécanisme.** Beaucoup de technologies ne se vendent pas : elles s'installent. Une pompe à chaleur, un système de recharge, un équipement médical, une ligne robotisée, un raccordement fibre — chacun exige une intervention qualifiée, sur site, par une personne formée à cette technologie précise.

**Trois propriétés en font un goulet particulièrement rigide.**

**Le délai de formation est incompressible.** Former un installateur qualifié se compte en mois pour les gestes, en années pour l'expérience — celle qui permet de traiter les cas non standard, qui sont la majorité en rénovation. Aucun financement n'accélère substantiellement ce délai.

**La qualité varie fortement, et l'écart est invisible à l'achat.** Une installation mal dimensionnée, mal réglée ou mal mise en service dégrade les performances de l'équipement sans qu'aucune alarme ne se déclenche. **C'est une défaillance silencieuse au sens du chapitre 14.8, dont la cause est humaine et organisationnelle.** L'utilisateur attribue la contre-performance à la technologie ; il en résulte une dégradation de la réputation de la filière entière, qui affecte la condition ⑤.

**Le métier n'existe pas encore.** Pour une technologie nouvelle, il n'y a ni référentiel de formation, ni certification, ni corps professionnel constitué. Ces éléments se créent, lentement, et ils relèvent de la condition ⑧.

**L'ordre de grandeur qui rend le problème concret.** Si une filière veut installer un million d'unités par an, et qu'un installateur qualifié en pose de l'ordre d'une centaine par an, il faut de l'ordre de dix mille installateurs. Si le vivier en compte deux mille, la filière est bornée à 200 000 unités par an **quelle que soit la capacité de production, la demande ou le prix.** Ce calcul se fait en trois lignes et il est presque toujours absent des plans de déploiement.

**Le lien avec le chapitre 24.** C'est le savoir-faire tacite, déplacé de l'usine vers le terrain. Il ne se documente pas davantage, il est encore plus localisé, et il se perd de la même façon.

**La question à poser devant tout plan de déploiement :** *qui installe, combien sont-ils, combien en forme-t-on par an, et qui les forme ?*

---

🎓 **À ce stade, vous savez…** identifier les compléments nécessaires à une technologie et leur calendrier propre ; reconnaître un problème d'amorçage et les quatre mécanismes qui le débloquent ; traiter la compétence comme une infrastructure à délai long ; distinguer une file de projets d'une capacité réelle.

---
