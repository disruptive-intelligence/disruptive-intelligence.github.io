---
title: Chapitre 14 — Capteurs, mesure et perception
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 16
chapters: 53
---

> **🎯 Pour lire ce chapitre**
>
> **À retenir :**
> * aucun capteur ne maximise à la fois résolution, cadence et dynamique : demandez lequel a été sacrifié ;
> * un capteur qui dérive continue de produire des valeurs plausibles — c'est la panne silencieuse.
>
> **À reconnaître :** rapport signal sur bruit · émission thermique · actif / passif · recalage · authenticité ≠ véracité
>
> **Le reste se consulte.** Les mécanismes de détail, les chiffres et les variantes ne sont pas à mémoriser : ils sont là pour que vous puissiez y revenir.

C'est le chapitre le plus dense en prérequis du volume. Presque tout ce qui relève de l'autonomie, de l'observation, de l'imagerie et de l'instrumentation en dépend.

## 14.1 Pourquoi cette famille existe : convertir le monde en information

Un capteur convertit une grandeur physique en un signal exploitable. Cette conversion est toujours **imparfaite, partielle et située**.

**Imparfaite** — le chapitre 8 l'a établi : il n'existe pas de mesure sans bruit.
**Partielle** — un capteur mesure une grandeur, dans une plage, avec une résolution.
**Située** — il mesure depuis un endroit, à un instant, dans des conditions.

**Conséquence à installer d'emblée.** Un capteur ne donne pas accès au monde : il donne accès à une **projection** du monde, définie par ses caractéristiques. Toute la difficulté de la perception consiste à remonter de cette projection à quelque chose d'utile — et cette remontée est une inférence, non une mesure, au sens du chapitre 8.

## 14.2 Les cinq caractéristiques d'un capteur

🖼 **SCHÉMA — Le triangle d'arbitrage du capteur.** Triangle dont les sommets sont résolution, cadence et dynamique. Montrer trois profils de capteurs comme trois triangles inscrits de formes différentes. Légende : « aucun capteur ne maximise les trois ; demandez lequel a été sacrifié ».



| Caractéristique | Ce qu'elle mesure | La question à poser |
|---|---|---|
| **Sensibilité** | variation de sortie pour une variation d'entrée | quel est le plus petit changement détectable ? |
| **Bruit** | fluctuation en l'absence de signal | quel est le plancher de détection ? |
| **Résolution** | finesse de discrimination | deux objets proches sont-ils distingués ? |
| **Dynamique** | rapport entre le plus fort et le plus faible mesurables | que se passe-t-il en saturation ? |
| **Cadence** | mesures par seconde | le phénomène varie-t-il plus vite ? |

**Le triangle d'arbitrage du chapitre 8 s'applique intégralement.** Résolution fine, cadence élevée, large dynamique : ces trois qualités se paient les unes contre les autres, en énergie, en coût, en encombrement et en volume de données. Devant tout capteur vanté sur une caractéristique, **demandez laquelle a été sacrifiée**.

**Un point souvent négligé : la dynamique.** Un capteur réglé pour un phénomène faible sature devant un phénomène fort, et un capteur saturé ne renvoie pas d'erreur : il renvoie sa valeur maximale, qui est une valeur plausible. C'est la première forme de panne silencieuse de ce chapitre.

## 14.3 Le spectre en pratique : voir avec ce que les objets émettent ou réfléchissent

Le chapitre 8 a posé le cadre. Voici son application, et c'est ce qui fonde tout le domaine de l'imagerie.

**Deux façons de voir, radicalement différentes.**

**Voir par réflexion.** Une source éclaire la scène, les objets renvoient une partie du rayonnement, le capteur le collecte. C'est la vision humaine, la photographie, le lidar, le radar. Sans source, pas d'image — la source pouvant être extérieure (le soleil) ou embarquée.

**Voir par émission.** Le chapitre 8 l'a établi : tout corps émet un rayonnement du fait de sa température, d'autant plus décalé vers les courtes longueurs d'onde qu'il est chaud. Un capteur sensible à la bonne bande capte donc ce que les objets **émettent eux-mêmes**, sans aucun éclairage.

**C'est ce qui fonde l'imagerie thermique.** Une caméra thermique voit dans l'obscurité totale parce qu'elle ne cherche pas de lumière réfléchie. Et cela impose une spécialisation : détecter un corps à température ambiante et détecter une source très chaude ne se font pas dans la même région du spectre, avec les mêmes détecteurs.

| Ce qu'on veut voir | Bande utile | Conséquence |
|---|---|---|
| Objets à température ambiante | infrarouge lointain, autour de 10 µm | détecteurs spécifiques, souvent non refroidis |
| Objets chauds, contrastes thermiques fins | infrarouge moyen | détecteurs souvent refroidis, donc plus coûteux |
| Scène éclairée, faible lumière | proche infrarouge, visible | proche de la photographie |
| À travers nuages, pluie, poussière | micro-ondes (radar) | résolution moindre à ouverture égale |

**Le compromis fondamental, rappelé du chapitre 8 :**

> Longueur d'onde courte → meilleure résolution à ouverture égale, moins bonne pénétration.
> Longueur d'onde longue → traverse mieux les conditions dégradées, exige une ouverture plus grande pour la même finesse.

**Ce compromis explique à lui seul pourquoi les systèmes de perception sérieux combinent plusieurs bandes** : aucune n'est bonne partout. Il fournit également au Volume 2 tout le socle nécessaire à l'optronique.

## 14.4 Capteurs actifs et passifs

**Un capteur passif** collecte ce qui existe : lumière ambiante, rayonnement thermique, ondes émises par d'autres.

**Un capteur actif** émet et observe le retour : radar, lidar, sonar, télémètre.

| | Passif | Actif |
|---|---|---|
| Énergie consommée | faible | élevée |
| Mesure de distance | difficile, indirecte | directe, par temps de retour |
| Dépendance aux conditions | forte | plus faible |
| Discrétion | totale | nulle : il émet |
| Interférences | rares | possibles entre systèmes voisins |

> **Résout / coûte.** Le capteur actif : *résout* la mesure directe de distance et l'indépendance à l'éclairement · *coûte* de l'énergie, de l'encombrement, une signature émise, et une sensibilité aux interférences quand plusieurs systèmes opèrent au même endroit.

**Le principe commun des capteurs actifs à mesure de distance** : émettre une impulsion, mesurer le temps de retour, en déduire la distance en connaissant la vitesse de propagation. La précision dépend donc de la finesse avec laquelle on peut dater l'impulsion — ce qui relie la mesure de distance à la mesure de temps, thème du paragraphe suivant.

**Ce que la résolution exige.** Le chapitre 8 l'a énoncé : la finesse de détail dépend du rapport entre la longueur d'onde et la taille de l'ouverture. Un radar travaillant en micro-ondes a donc, pour une antenne de taille raisonnable, une résolution bien plus grossière qu'un système optique. C'est ce qui rend intéressantes les techniques qui **synthétisent** une grande ouverture en combinant des mesures prises depuis des positions successives — le Volume 2 traitera de leurs applications, notamment spatiales.

## 14.5 Inertiel, positionnement et temps

Trois fonctions liées, dont dépend une part considérable du monde technologique.

**La mesure inertielle** détecte les accélérations et les rotations. En intégrant ces mesures dans le temps, on estime le déplacement. Cette méthode est autonome — elle ne dépend d'aucun signal extérieur — mais elle **dérive** : chaque petite erreur de mesure s'accumule, et l'erreur de position croît continûment. Une centrale inertielle seule ne peut donc pas naviguer indéfiniment ; elle a besoin d'être recalée périodiquement.

**Le positionnement par satellite** fournit ce recalage. Son principe : des satellites émettent des signaux horodatés très précisément ; le récepteur mesure les écarts de temps d'arrivée et en déduit sa position. **Le positionnement est donc, fondamentalement, une mesure de temps.**

**La référence de temps** est elle-même une infrastructure. Les réseaux, les transactions, les protocoles de sécurité et la corrélation d'événements en dépendent — et beaucoup de systèmes tirent leur temps des mêmes satellites. Le chapitre 13 l'a listée parmi les dépendances invisibles ; on voit ici pourquoi.

**La complémentarité est structurelle.** L'inertiel est autonome mais dérive ; le satellitaire est stable mais dépend d'un signal extérieur faible et distant. Les deux se recalent mutuellement. Cette architecture — un système précis à court terme couplé à un système stable à long terme — est un motif que l'on retrouve dans de nombreux domaines de la mesure.

**Cas de panne fondateur.** Si le signal de positionnement disparaît ou devient erroné, les systèmes qui en dépendent ne s'arrêtent pas tous : certains basculent sur l'inertiel et **dérivent lentement**, d'autres continuent avec un temps faux. Le chapitre 18 traitera de la dépendance ; retenez ici la forme du problème : **la dégradation est progressive et silencieuse**, ce qui la rend difficile à détecter.

## 14.6 Traitement du signal : ce qu'on peut extraire, et ce qu'on ne peut pas

Section ajoutée parce qu'elle conditionne plusieurs sujets majeurs. Aucun formalisme.

**Filtrer, c'est faire une hypothèse.** Séparer le signal du bruit suppose de savoir en quoi ils diffèrent — en fréquence, en régularité, en statistique. Un filtre est donc toujours l'application d'une hypothèse sur la nature du signal. **Si l'hypothèse est fausse, le filtre supprime du signal ou laisse passer du bruit, sans le signaler.**

**Échantillonner correctement.** Le chapitre 8 l'a montré : mesurer moins souvent qu'un phénomène ne varie produit un motif faux et crédible. La règle pratique est qu'il faut échantillonner nettement plus vite que la plus rapide des variations qu'on veut observer — et filtrer, avant l'échantillonnage, tout ce qui varie plus vite.

**Estimer, c'est combiner mesure et modèle.** Beaucoup de systèmes n'utilisent pas la mesure brute : ils la combinent avec une prédiction issue d'un modèle du comportement attendu, en pondérant selon la confiance accordée à chacune. C'est ce qui permet de suivre une trajectoire malgré des mesures bruitées.

**Le point de vigilance, qui est le plus important du chapitre.** Cette combinaison mesure-modèle produit un résultat **plus lisse et plus plausible** que la mesure brute. Elle est donc plus agréable — et elle peut masquer un désaccord entre la mesure et le modèle. Un estimateur qui accorde trop de confiance à son modèle continue de produire une trajectoire crédible alors que la mesure dit autre chose.

C'est, au niveau du traitement, la distinction mesure/inférence du chapitre 8. **Une chaîne de traitement produit toujours quelque chose ; ce quelque chose n'est pas toujours une mesure.**

## 14.7 Fusion de capteurs : pourquoi combiner est difficile

Combiner plusieurs capteurs paraît une bonne idée : leurs défauts se compensent. En pratique, quatre difficultés apparaissent, et elles sont toutes structurelles.

**Le recalage.** Deux capteurs ne mesurent pas depuis le même endroit ni au même instant. Il faut les ramener à une référence commune, ce qui suppose de connaître leur position relative — laquelle peut varier avec la température ou les vibrations — et de dater leurs mesures avec précision. **Un défaut de datation produit une erreur de fusion qui ressemble à une erreur de mesure.**

**Le désaccord.** Que faire quand deux capteurs disent des choses différentes ? Moyenner est presque toujours faux : si l'un a raison et l'autre tort, la moyenne est fausse. Il faut donc décider lequel croire, ce qui suppose un critère — et ce critère est une hypothèse de plus.

**La corrélation des erreurs.** Le chapitre 21 l'a établi pour la redondance : le gain de la combinaison suppose l'indépendance. Deux capteurs affectés par la même cause — brouillard, vibration, éblouissement, alimentation commune — ne sont pas indépendants, et la fusion n'apporte alors pas le bénéfice attendu.

**La confiance en soi excessive.** Une fusion bien réglée produit une estimation plus précise et une incertitude annoncée plus faible. Si cette incertitude annoncée est sous-estimée, le système devient confiant à tort — et un système confiant à tort est plus dangereux qu'un système incertain.

**Ce qu'il faut retenir.** La fusion n'est pas une addition de qualités : c'est une opération qui **ajoute ses propres modes de défaillance**. Elle est indispensable et elle n'est jamais gratuite.

## 14.8 Étalonnage, dérive et panne silencieuse

Voici le cas de panne fondateur de ce chapitre, et l'un des plus importants du volume.

**Tout capteur dérive.** Vieillissement, température, contamination de la surface optique, chocs, tassement mécanique. La relation entre la grandeur physique et le signal produit se déforme lentement.

**L'étalonnage corrige cette dérive** en comparant périodiquement à une référence connue. C'est une opération d'exploitation, elle a un coût, et sa périodicité est un arbitrage.

**Le mode de défaillance qui compte.** Un capteur qui tombe en panne franchement est un cas facile : l'absence de signal se détecte. **Un capteur qui dérive continue de produire des valeurs plausibles.** Le système ne voit aucune erreur, aucune alarme ne se déclenche, et les décisions prises sur la base de cette mesure sont fausses sans que rien ne l'indique.

**C'est la panne silencieuse.** Elle a été annoncée trois fois dans ce volume — au chapitre 8 avec le sous-échantillonnage, au chapitre 14.2 avec la saturation, au chapitre 14.6 avec l'estimateur trop confiant. Elle réapparaîtra au chapitre 15 sous une autre forme, et elle est la raison d'être de tout un domaine du Volume 2.

**Les trois parades, et leurs limites :**

* **la redondance dissemblable** — deux capteurs de principes différents, donc peu susceptibles de dériver ensemble ; coûteuse, et suppose de savoir arbitrer leur désaccord ;
* **le contrôle de vraisemblance** — vérifier que les mesures restent cohérentes entre elles et avec un modèle physique ; détecte les dérives importantes, pas les lentes ;
* **l'étalonnage périodique** — efficace, et il ne détecte la dérive qu'au moment du contrôle.

**Le lien avec le chapitre 9.** Une mesure peut être signée cryptographiquement, horodatée, transmise avec une intégrité parfaite — et fausse. La signature atteste l'origine et la non-altération ; elle n'atteste **rien** sur la véracité physique. C'est une distinction que le vocabulaire courant efface, et elle deviendra centrale au Volume 2 pour tout ce qui touche à la confiance dans les données de capteurs.

## 14.9 Ce que cela implique

**Le passage à l'échelle.** Un capteur étalonné à l'unité est une chose ; un million de capteurs déployés sur le terrain, vieillissant dans des environnements différents, en est une autre. **L'étalonnage devient une opération logistique**, et pour beaucoup de déploiements massifs, c'est elle qui borne la qualité de la donnée — pas la qualité du capteur.

**Dépendances.** Cette famille dépend des semi-conducteurs, de l'optique, des matériaux, du calcul embarqué, de l'énergie et du spatial pour le temps. Elle conditionne la robotique, l'autonomie, l'observation, l'industrie et une grande partie de la médecine.

**Implication cyber.** Trois points, tous prolongés au Volume 2 : **l'intégrité de la mesure à la source**, qui ne se règle par aucun moyen cryptographique ; **le leurrage**, c'est-à-dire la production délibérée d'un signal destiné à tromper un capteur, dont il faut comprendre le principe et les conséquences systémiques ; et **la distinction entre authenticité et véracité**, qui est probablement le point le plus important de ce chapitre pour un lecteur venant de la sécurité des systèmes d'information.

🎓 **À ce stade, vous savez…**

* énoncer les cinq caractéristiques d'un capteur et identifier laquelle a été sacrifiée ;
* distinguer voir par réflexion et voir par émission, et dire ce que chaque bande permet ;
* opposer capteurs actifs et passifs avec leurs coûts respectifs ;
* expliquer pourquoi le positionnement est une mesure de temps, et pourquoi inertiel et satellitaire se complètent ;
* dire ce qu'un filtre suppose et ce qu'un estimateur peut masquer ;
* énoncer les quatre difficultés de la fusion et pourquoi elle ajoute ses propres défaillances ;
* reconnaître une panne silencieuse, connaître les trois parades et leurs limites ;
* distinguer authenticité et véracité d'une mesure.

---

---

---
