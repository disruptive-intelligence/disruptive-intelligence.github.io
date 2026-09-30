---
title: Chapitre 36 — La robotique généraliste
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

## ① La capacité recherchée

**Formulation courante, et pourquoi elle ne convient pas.** « Un robot capable de tout faire » n'est pas une capacité analysable : elle n'a pas de seuil, pas de mesure, pas de condition de vérification.

**Formulation retenue.**

> **Manipuler des objets variés, dans des environnements non préparés, sans reprogrammation pour chaque tâche — au point que le seuil de variété au-delà duquel la spécialisation cesse d'être rentable se déplace significativement.**

**Ce que cette formulation change.** Elle rend la question économique et mesurable. Un robot spécialisé et bon marché bat un robot généraliste et cher sur toute tâche répétitive : **la généralité ne devient pertinente que là où la variété rend la spécialisation impossible.** Cette frontière existe aujourd'hui, elle est calculable, et la question est de savoir de combien elle se déplacera.

**Ce que le dossier ne traite pas.** La forme des machines. La question « humanoïde ou morphologie spécialisée » est un moyen, pas la capacité — et la monographie du chapitre 15 traite déjà la plateforme. **Ce dossier considère toutes les morphologies** : bras fixe, robot mobile manipulateur, humanoïde, combinaison de plateformes.

**Le récit associé.** C'est ce que le marché appelle *Physical AI* ou *general-purpose robotics*. Les fiches des chapitres 33 le situent ; ce dossier l'analyse.

---

## ② Les briques nécessaires

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

## ③ Ce qui empêche encore

Quatre verrous, hiérarchisés.

**Premier — la fiabilité de la manipulation en contact.** Une démonstration montre une saisie réussie ; une exploitation exige un taux d'échec assez faible pour que le traitement des échecs coûte moins que le gain. **L'écart se compte en ordres de grandeur**, et il n'est pas visible dans une vidéo. Le chapitre 14 en a donné les quatre causes : le contact change brutalement la dynamique, il faut contrôler des forces et non des positions, les objets diffèrent alors qu'ils se ressemblent, et certaines erreurs sont irréversibles.

**Deuxième — les données d'interaction physique.** L'apprentissage de tâches variées exige des exemples associant observation, instruction et action réelle. Ils s'acquièrent **une démonstration à la fois**, généralement par téléopération. Il n'existe aucun équivalent physique d'un corpus textuel collecté en ligne, et les données recueillies sur une plateforme ne se transposent pas directement sur une autre.

**Troisième — le coût de l'actionnement et de la maintenance.** Les actionneurs dominent le coût d'une machine multi-articulée, et leur baisse dépend de la série. La maintenance croît avec le nombre d'articulations sollicitées, et le jeu qui apparaît avec l'usure rend la machine imprécise **sans que ses capteurs le voient**.

**Quatrième — l'énergie embarquée.** La boucle masse-énergie borne l'autonomie : ajouter de la batterie ajoute de la masse qu'il faut déplacer. Le gain est moins que proportionnel, et il existe un point au-delà duquel ajouter n'apporte plus rien.

---

## ④ Le maillon le plus en retard

**Deux candidats sérieux, et il faut trancher.**

**La fiabilité domine ; la donnée la conditionne.**

Voici l'argument. Si les données étaient abondantes et partagées, la fiabilité progresserait — c'est le pari des architectures du chapitre 13. Mais si la fiabilité atteignait le seuil d'exploitation sans surveillance, le déploiement s'engagerait, et **le déploiement produirait des données**. Les deux se conditionnent mutuellement.

**Ce qui départage : l'ordre d'observabilité.** On peut mesurer un taux de succès ; on ne peut pas mesurer directement « la disponibilité des données ». Et surtout, **c'est la fiabilité qui décide de l'engagement économique** : un exploitant n'accepte pas une machine à 90 % de succès, quelle que soit la quantité de données ayant servi à l'entraîner.

**Conclusion du dossier.** Le maillon le plus en retard est **la fiabilité de la manipulation en environnement varié**, et le facteur qui la conditionne est **la disponibilité de données d'interaction mutualisées**.

**Position par rapport à la thèse du volume.** Le maillon en retard se situe **dans la couche éponyme** — *agir* — avec un conditionnement par *apprendre*. **La thèse est ici partiellement contredite**, et c'était prévu : quand la couche éponyme est celle où se joue le contact physique, le verrou peut y rester.

---

## ⑤ Quel mur domine

**Deux murs, parmi les cinq du volume 1.**

**Le rendement de production**, au sens du taux de succès. Un robot dont le geste échoue une fois sur cent produit, à l'échelle d'une ligne, un flux d'incidents dont le traitement dépasse le gain. **C'est la même arithmétique que le rendement de fabrication au chapitre 8** : la pénalité n'est pas proportionnelle, elle est inverse.

**La défaillance silencieuse**, sous trois formes. Un préhenseur usé continue de saisir, moins bien, sans le signaler. Une articulation avec du jeu positionne mal alors que ses capteurs disent le contraire. Et un modèle hors distribution produit une commande plausible et fausse.

**Ni la dissipation ni le coût du déplacement des données ne dominent** — ce qui écarte deux hypothèses fréquentes.

---

## ⑥ Ce qui est en train de changer

**Les architectures.** Le passage de chaînes modulaires — perception, puis planification, puis contrôle — à des architectures apprenant la correspondance de bout en bout supprime les interfaces où l'information se perdait. C'est un déplacement réel et récent.

**La collecte.** Des efforts de mutualisation de données d'interaction entre laboratoires et industriels sont engagés. **C'est le développement le plus significatif du domaine**, et il porte sur ce que le dossier identifie comme le facteur conditionnant.

**Le transfert depuis la simulation.** Il fonctionne bien pour la locomotion, où la physique est dominée par des effets bien modélisés. Il fonctionne mal pour la manipulation fine, où le contact est mal simulé. **Cet écart indique exactement où le progrès compte.**

**Le coût des plateformes**, en baisse, notamment sur les architectures d'actionnement à réduction faible.

**Ce qui n'a pas changé.** La densité de puissance des actionneurs. Le compromis entre couple, vitesse et précision. Le jeu qui apparaît avec l'usure. Et l'écart entre démonstration et fiabilité exploitable.

---

## ⑦ Ce que la convergence débloquerait

**Le déplacement du seuil de variété.** Aujourd'hui, automatiser une tâche physique suppose une série suffisante pour amortir l'intégration — préhenseur spécifique, adaptation du poste, programmation. Si une machine peut exécuter des tâches variées sans réintégration, **le seuil de série rentable baisse**, et des segments aujourd'hui manuels deviennent accessibles.

**Les usages qui deviendraient possibles**, par ordre de proximité. La manutention en environnement non préparé — chargement, transfert, préparation de commandes variées. L'assemblage en petite série. L'inspection et la maintenance en milieu encombré. Les services à faible valeur unitaire mais forte variété.

**Ce qui resterait hors de portée.** Les tâches exigeant une dextérité fine soutenue, celles où l'erreur est inacceptable, et celles où une machine spécialisée reste moins chère — c'est-à-dire toute production de masse répétitive.

**L'échelle.** Le déploiement serait borné par le nombre de techniciens formés bien avant par la capacité de production — mécanisme établi au volume 1.

---

## ⑧ Le verrou suivant

**La maintenance et les compétences de terrain.**

Si la fiabilité franchit le seuil, le goulet devient l'exploitation d'une flotte : pièces de rechange, interventions, étalonnages, mises à jour, diagnostic. **Le nombre de personnes capables d'entretenir ces machines borne le déploiement**, et former un technicien qualifié se compte en années.

**Une conséquence économique, souvent omise.** Le coût total de possession d'une flotte robotique est dominé par la maintenance et non par l'acquisition. **Un exploitant qui raisonne sur le prix d'achat se trompe de poste.**

**Et un verrou de second ordre.** Si les machines deviennent nombreuses et partagent des modèles appris, une défaillance de modèle affecte simultanément toute la flotte — c'est une défaillance de mode commun, et elle n'existe pas avec des machines programmées individuellement.

---

## ⑨ La chronologie conditionnelle

```text
① si des données d'interaction physique mutualisées atteignent une taille
   permettant un transfert mesurable entre plateformes différentes
        → alors la fiabilité en environnement varié devient le maillon limitant

② si la fiabilité franchit le seuil d'exploitation sans surveillance continue
   sur une famille de tâches
        → alors le coût de l'actionnement et de la maintenance devient limitant

③ si ce coût baisse par la série et si les compétences de maintenance
   se constituent
        → la généralité s'étend aux environnements à variété moyenne

④ si le coût ne baisse pas ou si les compétences manquent
        → la généralité reste confinée aux environnements à forte variété
          et forte valeur, où le coût est absorbable
```


**Lecture.** L'étape ④ n'est pas un échec : c'est une trajectoire, et c'est celle qui décrit l'état actuel. Une convergence qui reste confinée à un segment de valeur n'a pas échoué — elle a trouvé son domaine.

---

## ⑩ Signaux et réfutation

**Signaux de progression, par ordre d'informativité.**

**Un jeu de données d'interaction partagé** dont la taille et la diversité de plateformes sont publiées, et dont on démontre le transfert.

**Des données d'exploitation publiées par un tiers** : taux d'intervention humaine, disponibilité, coût de maintenance sur une flotte en production pendant plusieurs mois. **C'est le signal le plus difficile à obtenir et le plus décisif.**

**Une baisse du coût des actionneurs à couple élevé**, observable sur les catalogues.

**Une offre d'assurance** couvrant l'exploitation de machines de manipulation en environnement partagé.

**Signaux qui ne sont pas informatifs.** Une démonstration, quelle que soit son impressionnante variété. Une annonce de production en série, qui est un objectif. Un nombre de plateformes livrées, qui ne dit rien de leur usage.

**Ce qui réfuterait l'analyse.**

**Le taux de succès plafonne** malgré l'augmentation des données mutualisées — ce qui indiquerait que la donnée n'était pas le facteur conditionnant.

**Le coût de maintenance par unité ne baisse pas** avec la taille de la flotte, ce qui invaliderait l'étape ③.

**Les déploiements annoncés se révèlent être des environnements structurés déguisés** — objets présentés en position connue, scène préparée. Ce serait le signe que le seuil de variété n'a pas bougé.

**Et une réfutation de la formulation elle-même** : si des machines spécialisées et bon marché captaient les segments visés avant que la généralité n'arrive, la question deviendrait sans objet. **C'est une trajectoire possible et elle n'est pas dans les récits.**

---
