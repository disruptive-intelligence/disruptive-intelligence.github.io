---
title: Chapitre 16 — Contrôle, actionneurs et robotique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 18
chapters: 53
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * manipuler est structurellement plus difficile que se déplacer, pour quatre raisons distinctes ;
> * sûreté et sécurité sont deux disciplines aux hypothèses opposées, et elles peuvent entrer en conflit.
>
> **À reconnaître :** boucle fermée · marge de stabilité · jeu · enveloppe de fonctionnement · fail-safe / fail-operational
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

Le chapitre précédent traitait de systèmes qui produisent de l'information. Celui-ci traite de systèmes qui **agissent sur le monde physique** — ce qui change tout, y compris la nature des conséquences d'une erreur.

## 16.1 Pourquoi cette famille existe : la boucle

Le modèle structurant tient en trois termes :

```text
   PERCEVOIR  →  DÉCIDER  →  AGIR
        ↑                        |
        └────────────────────────┘
```

Un système qui agit sans percevoir le résultat de son action est en **boucle ouverte** : il applique une commande et espère. Un système qui mesure l'effet et corrige est en **boucle fermée**. Toute la robotique, et une grande partie de l'ingénierie des systèmes, consiste à fermer des boucles.

**Ce que la boucle apporte.** Elle rend le système tolérant à l'imprécision de son modèle et aux perturbations extérieures. Un moteur qui mesure sa vitesse et corrige atteint la consigne même si sa charge varie.

**Ce qu'elle impose.** Trois choses, et chacune renvoie à un chapitre précédent : une **mesure**, avec tous ses défauts (chapitre 14) ; un **délai**, incompressible (chapitre 8) ; et une **règle de correction**, qui est une hypothèse sur le comportement du système.

## 16.2 Contrôle : rétroaction, stabilité, marge

**Le principe de la correction.** On mesure l'écart entre l'état voulu et l'état constaté, et on agit proportionnellement à cet écart. Corriger fort ramène vite à la consigne ; corriger trop fort fait dépasser, ce qui produit un écart en sens inverse, donc une nouvelle correction — et le système oscille.

**La stabilité est le vrai sujet.** Un système de contrôle mal réglé n'est pas simplement imprécis : il peut devenir **instable**, c'est-à-dire amplifier ses propres corrections jusqu'à la destruction. La stabilité n'est donc pas une performance parmi d'autres ; c'est une condition d'existence.

**Le délai est l'ennemi de la stabilité.** Le chapitre 8 l'a annoncé : si l'information sur laquelle on corrige est ancienne, on corrige en fonction d'un état révolu. Plus le délai est long relativement à la dynamique du système, plus la correction doit être douce pour rester stable. **Vouloir corriger plus vite que le délai de boucle ne le permet ne rend pas le système plus réactif : cela le déstabilise.**

**La marge de stabilité.** On ne règle jamais un système à la limite. On conserve une marge, parce que la charge varie, les composants vieillissent, la température change et le délai fluctue. **Cette marge est une performance sacrifiée délibérément contre de la robustesse** — c'est l'un des arbitrages les plus universels de l'ingénierie, et il est structurellement invisible dans une démonstration, où les conditions sont favorables.

## 16.3 Actionneurs : convertir de l'énergie en mouvement

| Type | Densité de puissance | Précision | Rendement | Contrainte |
|---|---|---|---|---|
| Électrique | moyenne | élevée | élevé | couple limité, souvent besoin d'une réduction |
| Hydraulique | très élevée | moyenne | moyen | fluide, étanchéité, encombrement de la centrale |
| Pneumatique | moyenne | faible | faible | compressibilité, difficile à positionner finement |

**Les grandeurs qui comptent :** le couple, la vitesse, la précision de positionnement, la densité de puissance et le rendement.

**La réduction, et ce qu'elle coûte.** Un moteur électrique tourne vite avec peu de couple ; la plupart des applications demandent l'inverse. On interpose donc un réducteur, qui échange de la vitesse contre du couple. Ce réducteur introduit du **jeu**, du frottement, de l'usure et de l'inertie — et il devient souvent le composant qui limite la précision et la durée de vie de l'ensemble. C'est un exemple net du chapitre 32 : résoudre le problème du couple crée le problème du jeu.

**Le lien avec le chapitre 10.** Commander finement un moteur électrique suppose de l'électronique de puissance. Chaque point de rendement gagné sur cette conversion se répercute sur l'autonomie du système — le chapitre 8 l'a établi, les rendements se multiplient.

**Le lien avec le chapitre 8.** Un actionneur dissipe ses pertes en chaleur, dans un volume restreint, souvent sans circulation d'air. La densité de puissance réellement utilisable est donc bornée par l'évacuation thermique, non par les caractéristiques électriques.

## 16.4 Structure mécanique

**Les degrés de liberté** définissent ce que le système peut atteindre. Plus il y en a, plus l'espace atteignable est riche, et plus la commande, la masse et le coût augmentent.

**La rigidité gouverne la précision.** Une structure qui fléchit sous charge se positionne moins précisément que ne l'indiquent ses capteurs — lesquels mesurent généralement la position des articulations, pas celle de l'extrémité. **Un système peut donc être précis selon ses capteurs et imprécis en réalité**, ce qui est encore une forme de panne silencieuse, cette fois d'origine mécanique.

**Le jeu et l'usure dérivent dans le temps.** Le chapitre 8 l'a établi : les durées de vie mécaniques se comptent en cycles. Un système précis à la livraison ne l'est plus après quelques années, sauf maintenance — ce qui renvoie au chapitre 24.

> **Résout / coûte.** Ajouter un degré de liberté : *résout* l'accessibilité et la dextérité · *coûte* de la masse, de l'énergie, de la complexité de commande, un composant de plus à user et une rigidité moindre.

## 16.5 Énergie embarquée : le compromis qui borne tout

Le chapitre 12 a fourni les grandeurs ; voici leur conséquence.

Un système mobile emporte son énergie. Trois exigences s'opposent :

* **l'autonomie** demande beaucoup d'énergie embarquée, donc de la masse ;
* **la mobilité** demande peu de masse ;
* **la puissance de pointe** demande une capacité de restitution rapide, qui s'oppose à la densité d'énergie (chapitre 12.2).

**La boucle qui ferme le problème.** Ajouter de la batterie ajoute de la masse ; déplacer cette masse consomme de l'énergie ; il faut donc encore plus de batterie. Le gain d'autonomie est donc **moins que proportionnel** à l'énergie ajoutée, et il existe un point au-delà duquel ajouter de la batterie n'apporte pratiquement plus rien.

C'est le même mécanisme qui borne l'aviation électrique au chapitre 12 — vous le retrouvez ici à l'échelle d'un système mobile terrestre. **Ce n'est pas une limite technologique dépendant des batteries actuelles : c'est une propriété structurelle de tout véhicule qui emporte son énergie**, dont seule l'ampleur dépend de la densité énergétique disponible.

## 16.6 Pourquoi manipuler est plus difficile que se déplacer

Point essentiel, et contre-intuitif pour qui observe des démonstrations.

**Se déplacer** suppose de connaître sa position, d'éviter des obstacles et de contrôler une dynamique. Le problème est largement **géométrique**, l'environnement change lentement, et l'erreur se corrige en continu.

**Manipuler** suppose d'entrer en contact avec un objet dont on ignore la masse exacte, la répartition de matière, la rigidité, l'état de surface et le coefficient de frottement. Quatre difficultés apparaissent, qui n'existent pas dans le déplacement :

**Le contact change brutalement la dynamique.** Tant qu'il n'y a pas contact, le système bouge librement ; au contact, les forces changent instantanément. Un régulateur réglé pour le mouvement libre est inadapté au contact, et réciproquement.

**Les forces doivent être contrôlées, pas seulement les positions.** Serrer trop fort abîme, pas assez fait glisser. Cela suppose de mesurer des forces, ce qui est plus difficile et plus bruité que mesurer des positions.

**Les objets diffèrent.** Deux objets d'apparence identique peuvent avoir des propriétés différentes. La perception visuelle ne renseigne pas sur la masse ni sur le frottement.

**L'erreur ne se rattrape pas toujours.** Un objet lâché tombe ; un objet cassé est cassé. Contrairement au déplacement, où l'on corrige en continu, la manipulation comporte des instants irréversibles.

**Ce que cela change pour votre lecture des démonstrations.** Le chapitre 6 vous a donné les cinq questions à poser à une vidéo. Ce paragraphe vous dit **où regarder** : le nombre de prises, la variabilité des objets manipulés, et la présence ou non de préparation de la scène. Une démonstration de déplacement et une démonstration de manipulation ne prouvent pas des choses de même difficulté.

## 16.7 Sûreté et sécurité : deux disciplines distinctes

Cette section est particulièrement importante pour un lecteur venant de la cybersécurité, parce que le français emploie souvent un seul mot là où deux notions coexistent.

| | **Sûreté** (*safety*) | **Sécurité** (*security*) |
|---|---|---|
| Contre quoi | les défaillances et les erreurs | les actions intentionnelles hostiles |
| Modèle adverse | aucun : pannes aléatoires, erreurs humaines | un adversaire qui s'adapte |
| Méthode | analyse des modes de défaillance, redondance, marges | modèle de menace, défense en profondeur |
| Preuve | statistique, taux de défaillance | absence de vulnérabilité connue, hypothèses |
| Culture | normes, certification, retour d'expérience | veille, réaction, correctifs |

**Pourquoi la distinction compte.** Les méthodes de la sûreté supposent des défaillances **aléatoires et indépendantes** — hypothèse raisonnable pour des pannes matérielles. Un adversaire viole précisément cette hypothèse : il choisit ses cibles, provoque des défaillances corrélées et attaque les mécanismes de protection eux-mêmes. C'est exactement la défaillance de mode commun du chapitre 21, mais provoquée délibérément.

**L'inverse est vrai aussi.** Les méthodes de la sécurité ne traitent pas les défaillances aléatoires : un système parfaitement protégé contre les intrusions peut être dangereux par simple usure d'un composant.

**Les deux disciplines peuvent s'opposer.** Un correctif de sécurité déployé rapidement peut invalider une qualification de sûreté. Un système certifié figé ne peut pas recevoir de correctifs. **C'est une tension réelle, non résolue, et centrale pour tout système à la fois connecté et physique.** Le chapitre 28 en a montré la traduction institutionnelle.

## 16.8 Enveloppe de fonctionnement et modes dégradés

Voici l'aboutissement de ce chapitre, et l'un des concepts les plus utiles du volume.

**L'enveloppe de fonctionnement** est l'ensemble des conditions dans lesquelles un système a été conçu, testé et validé : plages de vitesse, de température, de charge, types d'environnement, conditions de visibilité. À l'intérieur, le comportement est caractérisé. À l'extérieur, il ne l'est pas — ce qui ne signifie pas qu'il sera mauvais, mais qu'on ne sait rien.

**Trois questions définissent la conception d'un système sûr :**

1. **Le système sait-il quand il sort de son enveloppe ?** C'est le problème le plus difficile, et c'est le même que la détection hors distribution du chapitre 15.
2. **Que fait-il alors ?**
3. **Qui en est informé, et dans quel délai ?**

**Les réponses possibles à la deuxième question**, avec leur coût :

**S'arrêter en sécurité** — le système se met dans un état sûr. Peu coûteux, valable seulement si l'arrêt est effectivement sûr.

**Continuer de fonctionner malgré la défaillance** — nécessaire quand s'arrêter est dangereux. Exige de la redondance sur toute la chaîne, et le chapitre 21 a établi que le saut de coût est considérable.

**Rendre la main** — le système transfère le contrôle à un humain. Cette réponse paraît économique et elle est trompeuse : elle suppose qu'un humain soit disponible, attentif, informé du contexte et capable de reprendre en quelques secondes. **Un opérateur qui surveille un système fiable depuis des heures n'est pas dans cet état.** C'est un problème documenté, et il ne se résout pas par la technique.

**Réduire les capacités** — le système continue avec des performances limitées. Souvent la meilleure réponse, et la plus difficile à concevoir : il faut avoir prévu à l'avance ce qui peut être abandonné.

**Ce que cela prépare.** Ces notions — enveloppe, détection de sortie, mode dégradé, arbitrage entre arrêt sûr et continuité — constituent le vocabulaire de tout ce que le Volume 2 traitera sous l'angle de l'autonomie sûre. Vous en avez ici le socle complet.

## 16.9 Ce que cela implique

**Le passage à l'échelle.** Un robot est un prototype ; mille robots déployés constituent un problème de maintenance, de pièces, de techniciens, de mise à jour logicielle et de responsabilité. Le chapitre 24 a montré que le nombre de techniciens formés borne souvent le déploiement bien avant la capacité de production.

**Dépendances.** Cette famille dépend des capteurs, du calcul embarqué, de l'énergie, de l'électronique de puissance, des matériaux et de la mécanique de précision. Et elle dépend du cadre institutionnel du chapitre 28 plus que la plupart des autres.

**Implication cyber — le point central.** Ici, le logiciel agit directement sur le monde physique. Trois conséquences :

**Une compromission produit un dommage matériel ou corporel**, pas une fuite de données. Le modèle de risque change de nature.

**Les correctifs se heurtent à la qualification**, comme la section 16.7 l'a montré.

**Les modèles de menace du système d'information ne se transposent pas directement.** La confidentialité y est souvent secondaire ; **l'intégrité des commandes et la disponibilité du contrôle** sont primordiales. Un attaquant n'a pas besoin de lire quoi que ce soit : il lui suffit d'altérer une consigne ou de retarder une boucle. C'est probablement l'écart le plus important entre votre domaine d'origine et celui-ci.

## 🧪 Lab 6 — Densité énergétique et autonomie embarquée
**Objectif.** Manier les deux densités et découvrir la boucle masse-énergie par le calcul.
**Durée.** 75 minutes. **Difficulté.** 2/3. **Prérequis.** Chapitres 5, 8, 11, 12, 16.
**Contexte.** Trois systèmes mobiles vous sont présentés avec leur masse, leur puissance moyenne en fonctionnement, leur autonomie visée et leur usage.

**Travail demandé.**
(a) Calculer, pour chacun, l'énergie embarquée nécessaire et la masse de batterie correspondante.
(b) Recalculer en tenant compte du fait que cette masse doit elle-même être déplacée — deux itérations suffisent.
(c) Identifier celui des trois pour lequel la boucle ne converge pas raisonnablement, et dire pourquoi.
(d) Pour celui-là, proposer deux modifications de conception qui changeraient la conclusion, l'une portant sur l'énergie, l'autre non.
(e) Dire ce que changerait un doublement de la densité énergétique des cellules — et pour lequel des trois cela changerait le plus.

**Livrable.** Une page et demie, avec les itérations visibles.

**Éléments attendus.** En (b), l'effet doit surprendre : c'est le but. En (d), la modification « non énergétique » attendue peut être une réduction de la puissance requise, un changement de mission, ou un ravitaillement en cours d'usage — une copie qui ne cherche que du côté de la batterie a manqué le point. En (e), le résultat contre-intuitif est que le doublement aide le moins celui qui est déjà le plus contraint, parce que la boucle amplifie : c'est le mécanisme qui sépare l'automobile de l'aviation au chapitre 12.2.

---

🎓 **À ce stade, vous savez…**

* décrire la boucle percevoir-décider-agir et ce que sa fermeture impose ;
* expliquer pourquoi le délai limite la réactivité et pourquoi la marge de stabilité est invisible en démonstration ;
* comparer les familles d'actionneurs et dire ce que coûte une réduction ;
* expliquer la boucle masse-énergie qui borne l'autonomie d'un système mobile ;
* énoncer les quatre raisons pour lesquelles manipuler est plus difficile que se déplacer ;
* distinguer sûreté et sécurité, et identifier la tension entre correctif et qualification ;
* définir une enveloppe de fonctionnement et évaluer les quatre réponses possibles à sa sortie ;
* dire pourquoi les modèles de menace du SI ne se transposent pas aux systèmes cyber-physiques.

---

---

---
