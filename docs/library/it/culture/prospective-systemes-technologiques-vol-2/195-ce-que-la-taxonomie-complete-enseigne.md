---
title: Ce que la taxonomie complète enseigne
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

Quarante-cinq fiches, et quatre observations que seul le décompte fait apparaître.

**Un.** Dans **trente-quatre cas sur quarante-cinq**, ce que la catégorie masque est une contrainte **institutionnelle, économique ou temporelle** — cadre d'autorisation, coût par appel, délai de raccordement, renouvellement du parc, attrition, contrôle à l'exportation, durée contractuelle. Presque jamais une contrainte physique. Le vocabulaire déplace systématiquement l'attention vers la capacité technique, c'est-à-dire vers la partie du problème qui bloque le moins souvent.

**Deux.** Les meilleurs cadrages regroupent des objets qui **partagent une contrainte réelle** : *cyber-physical systems*, *smart grid*, *trust technologies*. Les moins bons regroupent par finalité — *Climate Tech* — ou par mode de financement — *Deep Tech*. Ces derniers sont utiles à l'investisseur et inutiles à l'ingénieur, ce qui n'est pas un défaut tant qu'on sait à qui ils servent.

**Trois.** Plusieurs termes sont **des cycles de vocabulaire plutôt que des générations technologiques**. *Clean Tech* devenu *Climate Tech*, *ubiquitous computing* devenu *ambient computing*, *intelligent robotics* remplacé par une succession de termes. Le renouvellement d'un nom après un reflux indique que le récit a été refait — pas nécessairement la technologie.

**Quatre.** Les catégories les plus employées sont les plus larges, et c'est mécanique : un terme large est adoptable par davantage d'acteurs, donc il circule davantage. **Sa fréquence dans le discours est un indice inverse de sa précision.**

---

---


## Ouverture de la Partie IV

L'atlas répondait à une question : **qu'est-ce que cet objet ?**

Cette partie en pose une autre : **que se passe-t-il lorsque plusieurs de ces objets deviennent simultanément suffisamment bons ?**


### Ce qu'est une convergence

> Une rupture provient rarement d'une technologie isolée. Elle apparaît lorsque plusieurs capacités deviennent **simultanément suffisamment performantes, suffisamment fiables et suffisamment abordables**.

Les trois « suffisamment » sont indissociables. Une capacité excellente mais chère ne converge pas. Une capacité bon marché mais peu fiable non plus. **C'est la conjonction qui produit l'effet** — et c'est pourquoi le raisonnement porte toujours sur **le maillon le plus en retard**, jamais sur le plus avancé.


### Ce que chaque dossier produit

Dix mouvements, dans cet ordre, pour les six dossiers :

**① La capacité recherchée** — formulée précisément, sans terme de récit.
**② Les briques nécessaires** — quelles couches, quelles entrées d'atlas.
**③ Ce qui empêche encore** — verrous hiérarchisés, pas énumérés.
**④ Le maillon le plus en retard** — un seul, désigné et argumenté.
**⑤ Quel mur domine** — parmi les cinq du volume 1.
**⑥ Ce qui est en train de changer** — technologies, coûts, infrastructures.
**⑦ Ce que la convergence débloquerait** — usages, échelles, acteurs.
**⑧ Le verrou suivant** — le problème déplacé.
**⑨ La chronologie conditionnelle** — trois à cinq étapes, aucune date.
**⑩ Signaux et réfutation** — observables, datables.

**Les mouvements ④, ⑤ et ⑧ sont ceux qu'aucun autre ouvrage ne produit.** Ce sont eux qui justifient l'existence de cette partie à côté de l'atlas.


### Une thèse à éprouver

L'atlas et la taxonomie ont produit une thèse, et cette partie va la tester dossier par dossier :

> **Le maillon le plus en retard se situe rarement dans la couche qui donne son nom à la convergence — et le plus souvent dans une contrainte industrielle ou institutionnelle.**

Elle sera vérifiée quatre fois et partiellement contredite deux fois. **Le chapitre 41 fera le bilan de cette confrontation**, sans arrondir le résultat.


### Aucune date

Aucun de ces dossiers ne comporte de calendrier. Le volume 1 a établi pourquoi : quelques points d'écart sur un taux d'apprentissage produisent, sur vingt ans, un ordre de grandeur de différence. **Une méthode qui produirait des dates à partir de paramètres aussi dispersés serait fausse par construction.**

Ce que les dossiers produisent à la place est réfutable, hiérarchisant et résistant au temps.

---


## Chapitre 36 — La robotique généraliste


### ① La capacité recherchée

**Formulation courante, et pourquoi elle ne convient pas.** « Un robot capable de tout faire » n'est pas une capacité analysable : elle n'a pas de seuil, pas de mesure, pas de condition de vérification.

**Formulation retenue.**

> **Manipuler des objets variés, dans des environnements non préparés, sans reprogrammation pour chaque tâche — au point que le seuil de variété au-delà duquel la spécialisation cesse d'être rentable se déplace significativement.**

**Ce que cette formulation change.** Elle rend la question économique et mesurable. Un robot spécialisé et bon marché bat un robot généraliste et cher sur toute tâche répétitive : **la généralité ne devient pertinente que là où la variété rend la spécialisation impossible.** Cette frontière existe aujourd'hui, elle est calculable, et la question est de savoir de combien elle se déplacera.

**Ce que le dossier ne traite pas.** La forme des machines. La question « humanoïde ou morphologie spécialisée » est un moyen, pas la capacité — et la monographie du chapitre 15 traite déjà la plateforme. **Ce dossier considère toutes les morphologies** : bras fixe, robot mobile manipulateur, humanoïde, combinaison de plateformes.

**Le récit associé.** C'est ce que le marché appelle *Physical AI* ou *general-purpose robotics*. Les fiches des chapitres 33 le situent ; ce dossier l'analyse.

---


### ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Percevoir** | perception en contact, estimation de pose incertaine | peau électronique et tactile (7) · fusion de capteurs (7) · lidar (6) · caméras événementielles (6) |
| **Apprendre** | correspondance observation-commande, origine des données | VLA (13) · modèles du monde (13) · apprentissage par imitation (13) · sim-to-real (13) · modèles de fondation robotiques (13) |
| **Agir** | ce qui limite le geste, ce qui s'use | manipulation et préhension (14) · actionneurs (15) · mains et préhenseurs (15) · téléopération (15) |
| **Alimenter** | boucle masse-énergie, autonomie réelle | lithium-ion (21) |
| **Vérifier** | comportement quand le geste rate | dégradation maîtrisée (30) · détection de sortie de domaine (30) |

**Dix-sept entrées mobilisées** — la dépendance la plus large de tous les dossiers.

**Observation immédiate, et elle est contre-intuitive.** La couche *apprendre* fournit cinq entrées, la couche *agir* quatre. **La convergence dite « robotique » dépend plus fortement de l'apprentissage que de la mécanique** — ce qui n'apparaît dans aucun des récits qui la désignent.

---
