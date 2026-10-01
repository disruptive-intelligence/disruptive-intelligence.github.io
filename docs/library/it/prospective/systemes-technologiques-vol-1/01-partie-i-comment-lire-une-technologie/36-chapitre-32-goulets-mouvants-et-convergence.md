---
title: Chapitre 32 — Goulets mouvants et convergence
source: IT/09 Technologies & prospective/Systèmes technologiques (vol. 1).md
note: Systèmes technologiques (vol. 1)
up:
- - Systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Dernier chapitre de cette partie. Il rassemble tout ce qui précède en un seul mouvement d'analyse, et il prépare directement la manière de raisonner sur les technologies dont l'issue n'est pas connue.

## 32.1 Identifier le goulet actif

Dans tout système, à un instant donné, **une contrainte domine**. Améliorer n'importe quoi d'autre ne change rien au résultat d'ensemble.

C'est une idée simple et constamment ignorée, parce que l'on améliore spontanément ce qu'on sait améliorer plutôt que ce qui bloque.

**Comment reconnaître le goulet actif :**

* c'est l'élément dont une amélioration se traduit immédiatement en gain global ;
* c'est celui devant lequel les autres attendent — file d'attente, stock intermédiaire, capacité inutilisée ailleurs ;
* c'est celui qui absorbe l'essentiel du coût ou du délai marginal ;
* c'est celui dont on parle le moins, parce qu'il n'est pas dans le domaine de compétence de celui qui présente.

**L'erreur symétrique**, rencontrée au chapitre 3 : chercher le goulet dans le domaine que l'on maîtrise. Un spécialiste voit un goulet dans sa spécialité. Le parcours des neuf conditions sert précisément à contourner ce biais.

## 32.2 Résoudre un goulet le déplace

🖼 **SCHÉMA — La chaîne de goulets de l'infrastructure de calcul.** Six étages empilés verticalement, du calcul par puce jusqu'aux délais de fabrication des transformateurs. Chaque étage porte le chapitre où il a été établi. Marquer visuellement l'étage actuellement dominant et griser les étages franchis. Le schéma doit rendre évident qu'améliorer l'étage supérieur ne change rien tant qu'un étage inférieur borne.



Voici le principe que ce chapitre a pour but d'installer.

> **P8 — Résoudre un goulet ne supprime pas la contrainte : il la déplace.**

Quand la contrainte dominante est levée, une autre devient dominante. Le système ne devient pas « libre » : il devient limité par autre chose. La performance globale ne progresse donc que jusqu'au niveau permis par la contrainte suivante.

### Une chaîne documentée dans ce volume : l'infrastructure de calcul

Le déplacement suivant a été rencontré chapitre après chapitre, sans être nommé :

```text
   ① capacité de calcul par puce
        ↓  (largement améliorée)
   ② accès mémoire et coût du déplacement des données     [9.4, 10.7]
        ↓  (attaqué par le packaging, la hiérarchie, l'intégration)
   ③ énergie consommée et densité de puissance            [8.2, 10.6]
        ↓
   ④ évacuation de la chaleur                             [8.1, 13.5]
        ↓
   ⑤ raccordement électrique et capacité de transport     [26.4]
        ↓
   ⑥ délais de fabrication des transformateurs et postes  [26.4]
```


Chaque étage a été un goulet dominant, a été partiellement résolu, et a révélé le suivant. Aujourd'hui, sur les grandes installations, le goulet actif ne se situe plus dans la puce : il se situe dans le génie électrique et les délais administratifs. Une amélioration de la performance par puce ne change plus le calendrier d'un projet dont le raccordement est attendu pour dans sept ans.

**Ce que cela vous permet de faire.** Devant une annonce de progrès, poser deux questions : *quel goulet cette amélioration lève-t-elle ?* et *lequel deviendra alors dominant ?* Si la seconde question n'a pas de réponse, le gain annoncé est probablement inférieur à ce qui est promis.

## 32.3 Convergence

Certaines transformations ne viennent pas d'une technologie mais de **plusieurs contraintes levées à peu près en même temps**.

**Définition rigoureuse.** Il y a convergence quand une capacité nouvelle exige que plusieurs conditions franchissent simultanément un seuil, et qu'aucune ne suffit isolément. Tant qu'une seule reste en deçà, la capacité n'apparaît pas — ce qui explique que les convergences soient difficiles à anticiper : chacun des progrès partiels paraît décevant, jusqu'à ce qu'ils cessent de l'être.

**La formulation à retenir :**

> Une rupture provient souvent de plusieurs technologies devenues simultanément suffisamment bonnes, suffisamment fiables et suffisamment abordables.

**Les trois « suffisamment » sont indissociables.** Une capacité excellente mais chère ne converge pas. Une capacité bon marché mais peu fiable non plus. C'est la conjonction qui produit l'effet, et c'est pourquoi le raisonnement doit porter sur **le maillon le plus en retard**, jamais sur le plus avancé.

**Un exemple déjà instruit dans ce volume.** Le chapitre 22 a montré ce que le photovoltaïque devait à sa courbe d'apprentissage. Mais la baisse du coût des modules seule n'aurait pas produit son déploiement : il a fallu simultanément une électronique de puissance devenue fiable et bon marché [10.8], des cadres institutionnels créant une demande [28.4], une baisse parallèle du coût du stockage [12.5], et des chaînes de production capables de suivre [24.2]. Chacun de ces éléments a sa propre histoire ; c'est leur simultanéité qui a produit l'effet observé.

## 32.4 Technologies habilitantes

Certaines technologies ont une propriété particulière : elles ne créent pas directement de valeur, mais **débloquent la contrainte dominante de plusieurs autres à la fois**.

Ce volume en a rencontré plusieurs sans les nommer ainsi : le transistor, la mesure précise du temps, l'électronique de puissance, le séquençage à bas coût, le conteneur normalisé. Chacune est peu spectaculaire prise isolément et a débloqué simultanément des domaines sans rapport apparent entre eux.

**Comment les reconnaître à l'avance** — deux signatures :

* la technologie apparaît comme goulet actif dans plusieurs domaines indépendants à la fois ;
* son amélioration profite à des acteurs qui ne se connaissent pas et ne se coordonnent pas.

**Pourquoi cela importe.** Suivre les technologies habilitantes est plus informatif que suivre les applications spectaculaires : elles conditionnent plusieurs trajectoires simultanément, et leur progression est généralement mieux mesurable — coût, rendement, densité — que celle des capacités qu'elles rendent possibles.

## 32.5 Convergence réelle ou juxtaposition rhétorique

Le mot « convergence » est abondamment employé pour désigner de simples juxtapositions. Quatre tests permettent de trancher.

**Test de nécessité.** Retirez l'une des technologies invoquées. La capacité disparaît-elle ? Si elle survit, cette technologie n'était pas un constituant mais un accessoire.

**Test du seuil.** Peut-on nommer, pour chaque constituant, le seuil à franchir et sa valeur approximative ? Une convergence réelle se décrit en seuils ; une juxtaposition rhétorique se décrit en adjectifs.

**Test du maillon en retard.** Peut-on désigner celui qui est le plus loin de son seuil ? Si tous sont présentés comme prêts, la capacité devrait déjà exister.

**Test du niveau d'abstraction.** Les éléments listés sont-ils du même niveau au sens du chapitre 2 ? Une liste qui mêle un composant, une capacité et un récit n'est pas une analyse de convergence.

**Application.** Ces quatre tests suffisent à disqualifier la majorité des annonces de convergence, et à identifier les rares qui n'en sont pas.

## 32.6 Chronologie : dans quel ordre les choses doivent devenir vraies

Dernier outil de cette partie, et le plus proche de ce que vous ferez ensuite.

Une analyse de convergence ne produit pas une date. Elle produit une **chronologie conditionnelle** :

```text
   si A franchit son seuil   → alors B devient le maillon limitant
   si B le franchit à son tour → alors C devient limitant
   si C ne le franchit pas    → la capacité n'apparaît pas, quelle que soit A et B
```


Cette forme a trois vertus. Elle est **réfutable** — chaque étape est observable. Elle **hiérarchise** — elle dit quoi surveiller en premier. Et elle **résiste au temps** — si les dates glissent, la structure reste valide.

**C'est exactement la forme que doit prendre une analyse prospective sérieuse**, et c'est la raison pour laquelle ce volume s'est attaché à des trajectoires dont on connaît l'issue : pour vous permettre de vérifier que la méthode fonctionne avant de l'appliquer là où l'issue est inconnue.

🧪 **Lab 15 — Goulet et convergence**

**Objectif.** Identifier un goulet actif, anticiper son déplacement, distinguer convergence et juxtaposition.
**Durée.** 90 minutes. **Difficulté.** 3/3. **Prérequis.** Partie III complète.
**Contexte.** Trois annonces de progrès technologique vous sont fournies, dont deux se présentent comme des convergences.
**Travail demandé.** (a) Pour chaque annonce, identifier le goulet levé et le goulet qui deviendra dominant. (b) Appliquer les quatre tests de 32.5 aux deux annonces de convergence. (c) Pour celle qui passe les tests, écrire la chronologie conditionnelle de 32.6, en trois à cinq étapes. (d) Désigner le maillon le plus en retard et dire quel signal observable indiquerait sa progression. (e) Dire ce qui vous ferait conclure que la convergence n'aura pas lieu.
**Livrable.** Deux pages, dont la chronologie sous forme de chaîne conditionnelle.
**Éléments attendus.** L'une des deux annonces de convergence échoue au test de nécessité : une technologie y est invoquée sans être constitutive. En (e), une réponse acceptable désigne un signal observable et daté ; « si ça ne marche pas » n'en est pas un — c'est le critère du chapitre 1, appliqué une dernière fois.

---
