---
title: Chapitre 24 — L'industrialisation
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
up:
- - Prospective — systèmes technologiques (vol. 1)
  - ../index.md
- - Partie I — Comment lire une technologie
  - index.md
---

Fabriquer un exemplaire et en fabriquer un million sont deux métiers différents. Ce chapitre traite de la condition ⑥, et il explique pourquoi des entreprises correctement financées, disposant d'une technologie qui fonctionne et d'une demande démontrée, échouent quand même.

## 24.1 Le rendement de production gouverne tout

Le chapitre 10 a introduit la notion sur les semi-conducteurs. Elle est générale.

Le **rendement de production** est la proportion d'unités conformes en sortie de chaîne. Il paraît anodin ; il commande l'économie entière.

Considérons une ligne dont le coût de fonctionnement est fixe — c'est approximativement le cas d'une chaîne fortement capitalistique, où l'essentiel de la dépense est engagé indépendamment du nombre d'unités conformes obtenues.

| Rendement | Coût unitaire relatif |
|---|---|
| 90 % | 1,00 |
| 70 % | 1,29 |
| 50 % | 1,80 |
| 30 % | 3,00 |
| 10 % | 9,00 |

Le rendement ne modifie pas le coût proportionnellement : il le modifie **inversement**, ce qui produit une divergence brutale dans les basses valeurs. Une ligne à 30 % de rendement ne coûte pas « un peu plus » qu'une ligne à 90 % : elle coûte trois fois plus, et chaque unité rebutée a consommé de la matière, de l'énergie et du temps machine.

**Conséquence majeure pour l'analyse.** Le rendement n'apparaît dans aucune fiche technique, dans aucun communiqué, dans aucune démonstration. C'est pourtant, dans un grand nombre d'industries, le paramètre qui décide qui survit. Quand deux acteurs produisent le même objet avec la même technologie et que l'un gagne de l'argent, la différence est souvent là.

**La question à poser :** *quel est le rendement en régime, et depuis combien de temps est-il stable ?*

## 24.2 La montée en cadence

Une usine ne démarre pas : elle **monte**. Cette montée est un processus long, mal compris et systématiquement sous-estimé dans les calendriers.

Ce qu'il faut faire monter simultanément : le rendement, la cadence, la qualité, la disponibilité des machines, la compétence des opérateurs, et l'approvisionnement de tous les composants. Ces six variables interagissent : augmenter la cadence dégrade souvent le rendement, et améliorer le rendement demande de ralentir pour analyser.

**Les ordres de grandeur qui structurent la réflexion.** Construire une usine industrielle de taille significative se compte en années, pas en mois. Atteindre le régime nominal après la mise en service se compte également en années dans les procédés complexes. Un projet industriel annoncé pour dans trois ans a donc, dans le meilleur des cas, une production significative dans cinq à six ans — et cette arithmétique élémentaire suffit à disqualifier un grand nombre de calendriers annoncés.

**Le point critique : la course entre la courbe et la trésorerie.** Une usine qui monte consomme de l'argent sans en produire. Le chapitre 22 a montré que le coût baisse avec la production cumulée ; encore faut-il pouvoir financer les premiers doublements. L'industrialisation est donc une course entre deux courbes : celle de l'apprentissage, qui descend, et celle de la trésorerie, qui s'épuise. La technologie peut être bonne, l'apprentissage réel, et la course perdue quand même.

### Cas documenté — Northvolt

**Le projet.** Fondée en 2015, l'entreprise suédoise Northvolt vise à construire une filière européenne de batteries lithium-ion, avec une usine phare à Skellefteå, en Suède, mise en service en 2021. Elle lève plus de 14 milliards de dollars auprès d'investisseurs incluant Volkswagen, Goldman Sachs et BMW, et accumule un carnet de commandes considérable.

**Ce qui s'est passé.** La montée en cadence n'a pas suivi. Les objectifs de production à Skellefteå se comptaient en dizaines de gigawattheures annuels ; la production effective est restée d'un ordre de grandeur en dessous. En juin 2024, BMW annule une commande de l'ordre de deux milliards d'euros. En septembre 2024, environ 1 600 postes sont supprimés. L'entreprise dépose une demande de protection aux États-Unis, puis déclare faillite en Suède le 12 mars 2025 — la plus importante de l'histoire du pays — affectant environ 4 000 salariés. La production à Skellefteå est ensuite arrêtée.

**La nuance décisive, et c'est elle qui fait la valeur pédagogique du cas.** Dans son propre communiqué de faillite, l'entreprise indique que la production issue des lignes série avait doublé et que le rendement s'était amélioré d'environ 50 % depuis septembre. Autrement dit : **la courbe d'apprentissage fonctionnait**. Elle ne fonctionnait simplement pas assez vite au regard d'une consommation de trésorerie de l'ordre de cent millions de dollars par mois.

**Ce que ce cas enseigne.**

D'abord, que **l'industrialisation est une condition à part entière**, et non un détail d'exécution après la technologie et le financement. Ici, la technologie existait, la demande était contractualisée, le capital avait été levé — et la condition ⑥ a suffi à tout arrêter.

Ensuite, que **le savoir-faire de production ne s'achète pas avec le capital**. Il s'acquiert par la production, ce qui prend du temps, et le temps coûte de l'argent.

Enfin, que **la demande et l'industrialisation interagissent**. Le ralentissement du marché européen du véhicule électrique sur la période a réduit la pression des clients à attendre et la disposition des investisseurs à refinancer. Deux conditions qui bloquent partiellement peuvent suffire, ensemble, là où chacune seule aurait été surmontable.

**Ce que ce cas ne permet pas de conclure.** Que l'industrie européenne des batteries est impossible, ni que la technologie était en cause. Un cas unique établit un mécanisme, pas une loi — le chapitre 33 y reviendra.

⏱ *Faits vérifiés en août 2026. Voir Annexe I.*

## 24.3 Qualité, variabilité et non-qualité

**La qualité n'est pas l'absence de défauts** : c'est la maîtrise de la variabilité. Un procédé qui produit toujours la même chose, même imparfaite, est contrôlable. Un procédé qui produit tantôt bien tantôt mal, sans qu'on sache pourquoi, ne l'est pas.

Le coût de la non-qualité croît violemment avec le moment de la détection. Un défaut détecté sur la ligne coûte une pièce. Détecté à l'assemblage final, il coûte le démontage. Détecté chez le client, il coûte l'intervention, la logistique, la réputation et parfois le rappel de tout un lot.

**Point important pour le lecteur venant du logiciel.** Le réflexe « on corrigera en production » n'a pas d'équivalent physique. Un correctif logiciel se déploie en heures ; un rappel matériel implique de localiser des objets dispersés, d'organiser leur retour ou l'intervention sur site, de gérer une immobilisation et d'en assumer le coût sur des exemplaires déjà vendus. Cette asymétrie change complètement l'économie de la qualité, et c'est l'un des transferts de modèle mental les plus importants de ce cours.

## 24.4 Le savoir-faire tacite

Une partie substantielle de la compétence industrielle n'est écrite nulle part. Elle réside dans les gestes, les réglages, les réactions aux anomalies, la connaissance des particularités d'une machine donnée. C'est ce qu'on appelle le **savoir-faire tacite**, et il a trois propriétés qui déterminent des trajectoires entières.

**Il se transmet par la pratique et le contact**, pas par la documentation. On peut copier des plans, pas des gestes.

**Il se perd quand la production s'arrête.** Une filière interrompue pendant quinze ans ne redémarre pas là où elle s'était arrêtée : elle réapprend, plus cher. C'est l'un des mécanismes qui expliquent les apprentissages négatifs évoqués en 22.4.

**Il est localisé.** Il réside dans un bassin d'emploi, un réseau de sous-traitants, des écoles techniques, des équipes de maintenance. Reproduire une usine ailleurs ne reproduit pas cet environnement — ce qui nous conduit directement au chapitre 25.

**Conséquence analytique.** Quand un pays ou une entreprise annonce reconstituer une capacité industrielle perdue, la question n'est pas « peut-on financer l'usine ? » mais **« où sont les gens qui savent la faire tourner, et combien de temps faut-il pour en former ? »**.

## 24.5 Maintenir, réparer, remplacer

Un objet déployé en grand nombre doit être entretenu. Cette évidence a des conséquences économiques que les analyses de coût d'acquisition ignorent systématiquement.

**Il faut des pièces** — donc un stock, une logistique, une prévision de consommation, et le maintien d'une production de pièces bien après l'arrêt de la production principale.

**Il faut des techniciens** — en nombre proportionnel au parc déployé, formés, répartis géographiquement. Pour beaucoup de technologies, cette contrainte est le vrai plafond de déploiement : on peut fabriquer plus vite qu'on ne peut former les gens qui entretiendront.

**Il faut une conception qui permette la maintenance.** Un objet conçu pour être performant et non pour être réparé coûte, sur son cycle de vie, bien plus que ce que sa fiche technique laisse croire.

**Le lien avec le chapitre 21.** Un système très fiable mais impossible à réparer et un système moins fiable mais réparable en une heure peuvent avoir la même disponibilité effective. La disponibilité dépend autant du temps de réparation que du taux de panne — c'est pourquoi les deux grandeurs doivent toujours être demandées ensemble.

## 24.6 Pourquoi la deuxième usine est plus difficile que prévu

Contre-intuitif, et très fréquent. On s'attend à ce que la deuxième usine soit facile : les plans existent, le procédé est qualifié, les erreurs ont été faites. Elle est pourtant souvent décevante.

Quatre raisons, toutes réductibles à ce qui précède.

**Le savoir-faire tacite n'a pas été transféré**, parce qu'on a transféré des documents et quelques cadres, pas les équipes.

**Les particularités locales diffèrent** : qualité de l'eau, stabilité électrique, humidité, fournisseurs locaux, réglementation, disponibilité de main-d'œuvre qualifiée.

**La première usine a été réglée empiriquement**, et une partie des réglages qui la font fonctionner n'est pas formalisée — parfois même pas connue de ses propres ingénieurs.

**Les meilleures équipes restent sur la première** ou sont diluées entre les deux, ce qui dégrade les deux.

**Signal d'analyse.** Un acteur qui a réussi une usine n'a pas démontré qu'il sait en dupliquer une. Un acteur qui en a réussi trois a démontré autre chose : il possède un procédé de duplication, ce qui est une compétence distincte et plus rare que la première.

🗣 **Vocabulaire de réunion**

| Ce que vous entendez | Ce que cela signifie probablement | La question à poser |
|---|---|---|
| « L'usine est opérationnelle » | elle est construite et démarre | quel rendement, quelle cadence, en régime depuis quand ? |
| « Capacité de X unités par an » | capacité nominale théorique | quelle production effective sur les douze derniers mois ? |
| « On va industrialiser » | verbe qui masque des années de travail | quel est le calendrier de montée, et son financement ? |
| « On a le procédé » | on a un procédé de laboratoire | qui l'a fait tourner en série, et pendant combien de temps ? |
| « On duplique l'usine » | on copie les plans | qui part sur place, et combien de temps y reste-t-il ? |

🎓 **À ce stade, vous savez…** calculer l'effet d'un rendement sur le coût unitaire ; distinguer capacité nominale et production effective ; expliquer pourquoi l'industrialisation est une course entre apprentissage et trésorerie ; reconnaître le rôle du savoir-faire tacite et sa perte ; poser les bonnes questions sur la maintenance et sur la duplication d'une usine.

---
