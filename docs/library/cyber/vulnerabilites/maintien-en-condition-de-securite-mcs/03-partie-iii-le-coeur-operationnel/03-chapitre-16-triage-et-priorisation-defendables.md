---
title: Chapitre 16 — Triage et priorisation défendables
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

## 16.1 Pourquoi « tout ce qui dépasse 7 » ne fonctionne pas

Commençons par la démonstration chiffrée, parce que l'argument théorique ne convainc personne tant que les nombres ne sont pas posés.

**Le point de départ.** Un parc de taille intermédiaire produit, lors d'un premier scan authentifié complet, de l'ordre de plusieurs milliers de constats. Reprenons les chiffres du fil rouge : 4 312 constats, dont 1 176 de gravité supérieure ou égale à 7.

**Le calcul de capacité.** Comptez vingt minutes par constat — qualification, recherche du correctif, planification, suivi, vérification. C'est une estimation basse pour un constat non trivial.

```
1 176 constats × 20 min            = 392 heures
392 h / 2 personnes                = 196 h par personne
196 h à ~75 h disponibles par mois ≈ 2,6 mois de traitement
```


Deux mois et demi pour résorber le stock initial : à ce stade, la situation paraît tenable. **C'est le flux qui la rend impossible.**

**Le calcul qui compte est celui du régime permanent.** Un parc de cette taille produit typiquement 250 à 400 nouveaux constats par mois, dont une proportion comparable dépasse le seuil de gravité retenu — soit environ 70 à 110 constats mensuels à traiter selon cette règle.

```
90 nouveaux constats/mois × 20 min   ≈ 30 h/mois
Capacité disponible                   ≈ 150 h/mois pour deux personnes
Reste pour le stock initial           ≈ 120 h/mois
392 h de stock / 120 h                ≈ 3,3 mois
```


**Sur le papier, cela passe.** Dans la réalité, deux hypothèses de ce calcul sont fausses :

- Les 75 heures mensuelles supposent que la moitié du temps est consacrée au MCS. La mesure du §37.9 donne un ordre de grandeur bien plus faible une fois déduits l'exploitation courante, les changements, les incidents et les astreintes.
- Les 20 minutes par constat ne couvrent que le triage. Elles n'incluent ni la planification, ni la fenêtre, ni le déploiement, ni la vérification, ni la preuve — c'est-à-dire l'essentiel de la charge réelle (§37.9).

Avec des hypothèses réalistes, le stock ne se résorbe pas : il se stabilise à un niveau élevé, ou il croît. **Et c'est le meilleur des cas**, celui où le flux est régulier : une campagne d'exploitation sur un produit très déployé peut ajouter plusieurs centaines de constats en une semaine.

**Le second problème, plus grave que le premier.** Cette méthode ne se contente pas de produire trop de travail : elle produit le **mauvais** travail. Elle écarte des constats réellement dangereux — la vulnérabilité de gravité 5,9 activement exploitée sur une interface d'administration exposée du fil rouge — et inclut des milliers de constats qui ne seront jamais exploités. Elle est simultanément trop large et trop étroite.

**La conclusion, qui structure tout le chapitre.** Le seuil de gravité seul échoue parce qu'il utilise **une seule des cinq informations** nécessaires à une décision. Il connaît la gravité technique ; il ignore l'exploitation observée, l'exposition, la criticité métier et l'effort de correction.

## 16.2 Construire une fonction de priorisation

**Les cinq entrées**, et ce que chacune apporte :

| Entrée | Question | Source | Qui la détient |
|---|---|---|---|
| **Gravité technique** | Quels dégâts si c'est exploité ? | Score de gravité (§4.4) | Externe |
| **Exploitation** | Est-ce utilisé par des attaquants ? | Catalogue d'exploitation avérée, renseignement (§4.6) | Externe |
| **Probabilité** | Est-ce susceptible de l'être ? | Modèle de prédiction (§4.5) | Externe |
| **Exposition** | Est-ce atteignable, et par qui ? | Votre cartographie (ch. 11) | **Vous seul** |
| **Criticité** | Que vaut cet actif pour l'organisation ? | Votre inventaire (ch. 10) | **Vous seul** |

Une sixième entrée intervient à l'arbitrage, sans entrer dans l'évaluation du risque : l'**effort de correction**. Elle ne change pas la priorité d'un constat, elle change l'ordre dans lequel on traite des constats de priorité comparable — et elle justifie de regrouper (§16.7).

⚠️ **PIÈGE — la formule pondérée**
La tentation est forte de construire un score unique en pondérant les cinq entrées. C'est une mauvaise idée pour trois raisons : les pondérations sont arbitraires et indéfendables en audit ; un score composite masque le raisonnement au lieu de l'expliciter ; et une entrée manquante — cas fréquent depuis la fragmentation de l'écosystème (§4.9) — rend le score incalculable au lieu de simplement dégrader la décision. **Préférez un arbre de décision** : il produit une action, il se lit, il se discute, et il fonctionne même avec une information incomplète.

🖼 **SCHÉMA — Arbre de décision de triage.** *Arbre à six nœuds de décision et cinq feuilles colorées par urgence. C'est le visuel le plus utilisé du cours : à soigner particulièrement.*

## 16.3 L'arbre de décision opérationnel

Voici un arbre utilisable tel quel, à calibrer sur vos classes de service (§7.2).

```
① La vulnérabilité est-elle activement exploitée ?
   ├─ OUI ─→ ② L'actif est-il joignable depuis Internet ?
   │          ├─ OUI ─→ ████ AGIR EN URGENCE  (72 h, hors fenêtre autorisée)
   │          └─ NON ─→ ③ L'actif est-il de niveau 0 ou critique métier ?
   │                     ├─ OUI ─→ ███ TRAITER EN PRIORITÉ  (7 j)
   │                     └─ NON ─→ ██ TRAITER  (30 j)
   └─ NON ─→ ④ Probabilité d'exploitation élevée OU gravité critique ?
              ├─ OUI ─→ ⑤ Exposé ou actif critique ?
              │          ├─ OUI ─→ ██ TRAITER  (30 j)
              │          └─ NON ─→ █ PLANIFIER  (prochaine campagne)
              └─ NON ─→ ⑥ Corrigeable dans une campagne groupée ?
                         ├─ OUI ─→ █ PLANIFIER  (campagne trimestrielle)
                         └─ NON ─→ ░ SURVEILLER  (revue semestrielle)
```


**Les quatre propriétés qui en font un bon outil**, et qu'un score composite n'a pas :

1. **Il produit une action**, pas un nombre : chaque feuille correspond à un délai et à un mode de traitement.
2. **Il est auditable.** En cas de contestation, on ne discute pas d'une pondération, on relit le chemin parcouru : « exploitation non observée, non exposé, actif non critique ». C'est vérifiable.
3. **Il tolère l'information manquante.** Si la probabilité d'exploitation n'est pas disponible pour ce constat, la question ④ se résout sur la gravité seule. La décision est dégradée, pas bloquée.
4. **Il place les deux informations que vous seul détenez au cœur du raisonnement** : l'exposition et la criticité apparaissent à trois nœuds sur six.

✅ **BONNE PRATIQUE (P0)** — Écrivez votre arbre, faites-le valider en comité MCS, et **datez-le**. C'est le document que vous produirez le jour où l'on vous demandera pourquoi tel constat n'a pas été traité en priorité. Un arbre validé et appliqué est une défense solide ; une décision au cas par cas ne l'est pas.

## 16.4 Exploitabilité contextuelle

Le §11.6 a posé la notion. Trois vérifications rapides, à faire avant d'engager toute campagne, retirent une part significative du volume :

| Vérification | Durée | Question |
|---|---|---|
| **Activation** | 1 minute | Le service ou module vulnérable est-il actif sur cet actif ? |
| **Configuration requise** | 5 minutes | L'avis mentionne-t-il une condition — option activée, mode particulier — que vous n'avez pas ? |
| **Atteignabilité du code** | Variable | La fonction vulnérable est-elle appelable ? (déclaration du fournisseur, analyse) |

**Le résultat de ces vérifications ne clôt pas le constat**, il le **dépriorise avec justification** — nuance essentielle traitée au §16.6 et au chapitre 17. La distinction est ce qui vous protège le jour où la configuration change et où le service désactivé est réactivé par un autre projet.

## 16.5 Fixer des délais tenables

Les délais des classes de service (§7.2) doivent satisfaire trois contraintes simultanées, et c'est leur conjonction qui est difficile.

| Contrainte | Question |
|---|---|
| **Cohérence avec le risque** | Un délai de 30 jours sur un actif exposé portant une vulnérabilité exploitée est indéfendable |
| **Tenabilité** | Un délai que vous ne tenez pas produit une non-conformité permanente (§7.2) |
| **Justifiabilité** | Vous devez pouvoir expliquer d'où viennent ces chiffres |

**Sur le troisième point**, trois sources de justification acceptables : les délais imposés par un référentiel qui vous est applicable (chapitre 8) ; les délais issus d'un modèle méthodologique public reconnu, en le citant comme référence et non comme obligation (§8.7) ; ou votre propre calibrage documenté, fondé sur une mesure de votre capacité réelle. La troisième est parfaitement recevable — à condition d'être écrite.

**La méthode de calibrage par la capacité**, qui produit des chiffres tenables :

```
1. Mesurez le volume mensuel réel de constats atteignant chaque feuille de l'arbre
2. Mesurez le temps réellement consommé par constat, par catégorie
3. Confrontez à la capacité disponible
4. Ajustez soit les délais, soit la capacité — jamais l'affichage seul
```


L'étape 4 est un arbitrage de direction, pas une décision technique. Si la capacité ne permet pas des délais cohérents avec le risque, c'est un **constat à remonter** au comité stratégique (§9.3), avec les trois options du chapitre 12 : plus de moyens, moins de périmètre, ou plus de risque accepté.

## 16.6 La dépriorisation défendable

Décider de ne pas traiter maintenant est une décision normale et fréquente. Ce qui la rend acceptable, c'est sa **traçabilité**.

**Les quatre motifs légitimes**, avec ce qui doit être écrit pour chacun :

| Motif | À documenter | Risque associé |
|---|---|---|
| Non atteignable dans votre contexte | Le fait vérifié qui l'établit, et sa date | La configuration peut changer |
| Faible probabilité et exposition nulle | Les valeurs constatées et la date | Les deux peuvent évoluer |
| Correction groupée à venir | La campagne cible et sa date | La campagne peut glisser |
| Effort disproportionné au risque | La comparaison chiffrée | Jugement contestable |

⚠️ **PIÈGE — la dépriorisation qui devient un oubli**
Un constat déprioritisé sans **date de revue** disparaît. La règle est simple : toute dépriorisation porte une date de réexamen, et le réexamen est automatique — pas dépendant de la mémoire de quelqu'un. Les trois premiers motifs ci-dessus reposent sur un état du monde qui peut changer ; ils sont valables jusqu'à réexamen, pas définitivement.

**Dépriorisation ≠ clôture.** Un constat déprioritisé reste **ouvert** dans la file, avec une échéance repoussée. Un constat clos n'existe plus. Confondre les deux fait disparaître de votre pilotage la dette que vous venez d'accepter — et c'est ce que le chapitre 17 formalise.

## 16.7 Traiter la volumétrie : penser en campagnes

Le triage réduit la file ; il ne la vide pas. Le second levier consiste à changer d'unité de travail.

**Raisonner par constat individuel est la source principale d'inefficacité.** Trois regroupements produisent des gains considérables :

| Regroupement | Principe | Gain typique |
|---|---|---|
| **Par correctif** | Un correctif cumulatif corrige souvent des dizaines de constats sur le même actif | Le travail est celui d'un correctif, pas de trente |
| **Par actif** | Traiter tous les constats d'un actif en une intervention | Une seule fenêtre, un seul test, un seul redémarrage |
| **Par montée de version** | Passer à une version supportée règle simultanément le présent et le futur | Supprime des constats à venir |

**Le changement de perspective à opérer**, et il est plus profond qu'il n'y paraît : *ne mesurez pas votre travail en nombre de vulnérabilités fermées, mesurez-le en nombre d'actifs ramenés à un état de référence.* Un actif à jour ne produit plus de constats. C'est aussi ce qui rend l'approche immuable du §3.5 si efficace : la cadence de reconstruction remplace des centaines de traitements individuels.

## 16.8 ⏱ Reconstruire ce que l'on recevait gratuitement

*Bloc périssable, vérifié le 30/07/2026.*

La fragmentation de l'écosystème (§4.9) a une conséquence directe et concrète sur le triage : une part croissante des constats arrive **sans enrichissement** — sans score, sans correspondance produit fiable, parfois sans description exploitable.

**Les trois stratégies d'adaptation**, par ordre de robustesse :

| Stratégie | Principe | Effort |
|---|---|---|
| **Basculer le poids sur ce que vous détenez** | Faire porter la décision sur l'exposition et la criticité plutôt que sur le score reçu | Faible, et c'est déjà la bonne pratique |
| **Multiplier les sources** | Croiser plusieurs bases, dont une européenne, plus les avis éditeurs (§14.4) | Moyen |
| **Enrichir en interne** | Attribuer soi-même une gravité aux constats non enrichis, selon une grille écrite | Élevé, réservé aux actifs C1 |

**Le point encourageant**, et il vaut d'être souligné : une organisation qui a fait le travail des chapitres 10 et 11 est **beaucoup moins exposée** à cette fragmentation qu'une organisation qui dépendait entièrement d'un score externe. L'exposition et la criticité ne dépendent d'aucun fournisseur. C'est un argument de plus pour l'ordre de séquencement du §1.4.

## 16.9 📌 Limites du triage

- **Le triage ne crée aucune capacité de remédiation.** Il permet de dépenser au bon endroit une capacité qui reste constante. Si votre capacité est structurellement insuffisante, le triage la rend visible, il ne la résout pas.
- **Le risque de sur-ingénierie est réel.** Un dispositif de triage sophistiqué peut consommer plus de temps que la correction elle-même. Si votre arbre nécessite plus de cinq minutes par constat, il est trop complexe.
- **Les entrées externes sont volatiles.** Un constat déprioritisé aujourd'hui peut devenir urgent demain, sans qu'aucune information interne ne change. D'où l'obligation de rejeu périodique (§16.6).
- **Le triage ne remplace pas la correction de fond.** Un parc dont les images de référence sont anciennes reproduira les mêmes constats indéfiniment. Le triage traite le symptôme.

## 16.10 🔬 Mini-lab 4 — Construire une matrice de triage

**Objectif** — Appliquer l'arbre de décision et mesurer l'écart avec un tri par gravité.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §16.3, §11.7, §7.2 · **Livrable** priorisation argumentée des 10 constats.
**Compétences validées** — ✔ appliquer un arbre de décision ✔ intégrer exposition et criticité au triage ✔ reconnaître un actif de niveau 0 ✔ déprioriser avec justification et date de revue

**Données fournies.** Vingt-cinq constats issus d'un scan. Extrait représentatif de dix d'entre eux :

| # | Gravité | Exploitation observée | Probabilité | Actif | Exposition | Criticité |
|---|---|---|---|---|---|---|
| 1 | 9,8 | Non | Faible | Serveur de test | Interne | C3 |
| 2 | 5,9 | **Oui** | Élevée | Passerelle d'accès distant | **Internet** | C1 |
| 3 | 8,1 | Non | Faible | Poste bureautique ×340 | Interne | C3 |
| 4 | 7,5 | Non | Moyenne | Contrôleur de domaine | Interne | **C1 — niveau 0** |
| 5 | 6,1 | **Oui** | Élevée | Automate de production | Réseau industriel isolé | C4 |
| 6 | 9,1 | Non | Faible | Bibliothèque, service désactivé | Interne | C2 |
| 7 | 4,3 | Non | Faible | Serveur de fichiers | Interne | C2 |
| 8 | 8,8 | Non | **Élevée** | Serveur web public | **Internet** | C1 |
| 9 | 7,2 | Non | Faible | Console de sauvegarde | Interne | **C1 — niveau 0** |
| 10 | 9,4 | Non | Moyenne | Hyperviseur | Réseau d'administration | **C1 — niveau 0** |

**Questions.** (a) Classez ces dix constats avec l'arbre du §16.3. (b) Classez-les par gravité décroissante. (c) Comparez les cinq premiers de chaque classement. (d) Quels constats méritent une vérification avant tout traitement ? (e) Le constat n° 5 relève d'une classe particulière : que faites-vous ?

**Corrigé commenté**

**(a) Classement par l'arbre :**

| Rang | # | Chemin dans l'arbre | Décision |
|---|---|---|---|
| 1 | **2** | Exploitée → exposée Internet | **AGIR EN URGENCE — 72 h** |
| 2 | **5** | Exploitée → non exposée → actif critique (C4) | **TRAITER EN PRIORITÉ — mais régime C4 : compensation** |
| 3 | **8** | Non exploitée → probabilité élevée → exposé | **TRAITER — 30 j** |
| 4 | **10** | Non exploitée → gravité critique → actif de niveau 0 | **TRAITER — 30 j** |
| 5 | **4** | Non exploitée → gravité critique → niveau 0 | **TRAITER — 30 j** |
| 6 | **9** | Non exploitée → gravité élevée → niveau 0 | TRAITER — 30 j |
| 7 | **3** | Non exploitée → gravité élevée → non exposé, C3 | PLANIFIER — campagne, mais volume : 340 postes |
| 8 | **1** | Non exploitée → gravité critique → non exposé, C3 | PLANIFIER |
| 9 | **6** | Service désactivé | **DÉPRIORISER avec justification et date de revue** |
| 10 | **7** | Faible partout | SURVEILLER |

**(b) Classement par gravité décroissante :** 1 (9,8) · 10 (9,4) · 6 (9,1) · 8 (8,8) · 3 (8,1) · 4 (7,5) · 9 (7,2) · 5 (6,1) · 2 (5,9) · 7 (4,3).

**(c) La comparaison, et c'est tout l'objet du lab.**

| Méthode | Cinq premiers |
|---|---|
| Arbre de décision | **2, 5, 8, 10, 4** |
| Gravité seule | **1, 10, 6, 8, 3** |

Deux constats seulement sont communs. Surtout : le tri par gravité place en **première position** le constat n° 1 — un serveur de test interne, non exposé, non exploité — et relègue en **avant-dernière** le n° 2, la seule vulnérabilité activement exploitée sur un actif publié sur Internet. Il place également en troisième position le n° 6, dont le service est désactivé.

**(d) Les vérifications préalables :** le n° 6 (état d'activation — déjà connu ici, à confirmer sur l'ensemble du parc), le n° 3 (340 postes : appliquer le point de contrôle des trois actifs représentatifs du §15.13), et le n° 1 (vérifier qu'il s'agit bien d'un serveur de test, et surtout **ce qu'il contient** — un serveur de test portant une copie de données de production n'est pas un actif C3, voir chapitre 28).

**(e) Le constat n° 5.** Vulnérabilité exploitée sur un automate en classe C4. Le régime applicable n'est pas la correction mais la **compensation sous 72 h** (§7.2) : vérifier l'isolation du réseau industriel, restreindre les accès, renforcer la surveillance, et planifier le correctif validé par le constructeur pour le prochain arrêt de production. La décision est écrite et signée par le propriétaire métier. C'est le chapitre 29.

**Les trois erreurs attendues.** Traiter le n° 5 comme un constat C1 et exiger une correction immédiate, ce qui est irréaliste et détruira la relation avec l'exploitant industriel. **Clore** le n° 6 au lieu de le dépriorer. Et sous-estimer le n° 3 en le voyant comme un constat unique alors qu'il représente 340 actifs, donc une campagne à part entière.

## 16.11 🔴 FIL ROUGE — février 2027 : la refonte du triage, un an après

Un an après la première tentative (§4.11), Claire Nadeau et Malik Ferhaoui formalisent l'arbre de décision d'HELIOMED et mesurent l'effet sur les 3 800 constats du scan de janvier.

**Le résultat, en une page.**

| Feuille de l'arbre | Constats | Charge estimée |
|---|---|---|
| Agir en urgence — 72 h | 4 | 1 jour |
| Traiter en priorité — 7 j | 19 | 4 jours |
| Traiter — 30 j | 143 | 3 semaines |
| Planifier — campagne | 1 890 | **21 campagnes groupées**, dont 6 montées de version |
| Surveiller | 1 604 | Revue semestrielle |
| Déprioritisé avec justification | 140 | Réexamen trimestriel automatique |

**Ce qui change réellement.** Ce ne sont pas les 4 constats urgents — ils auraient été traités de toute façon. C'est la ligne « Planifier » : 1 890 constats deviennent **21 campagnes**, parce que le regroupement par correctif et par actif (§16.7) transforme des milliers de traitements individuels en quelques dizaines d'interventions. Six de ces campagnes sont des montées de version qui supprimeront aussi les constats à venir.

La charge annuelle estimée passe de « impossible » à « tenable avec deux personnes, à condition de ne pas ajouter de périmètre ». Ce dernier point est écrit noir sur blanc dans la note au comité.

**La décision la plus discutée.** Les 1 604 constats en surveillance représentent 42 % du total, et le représentant commercial demande si l'on peut « laisser 1 604 vulnérabilités ouvertes ». Claire répond en trois points : elles ne sont ni exploitées, ni exposées, ni sur des actifs critiques ; elles sont **suivies et réexaminées**, pas oubliées ; et la majorité disparaîtra sans traitement individuel lors des campagnes de montée de version. Le comité valide, et la formulation retenue au compte rendu est celle qui compte : *« 1 604 constats en surveillance active, réexamen semestriel, aucun sur actif exposé ou critique »*.

**Ce qui n'était pas prévu.** En appliquant l'arbre, deux constats atteignent la feuille « urgence » sur des actifs de l'infogérant — les premiers depuis que la restitution mensuelle de données fonctionne (§13.9). Le délai contractuel de 7 jours s'applique. C'est la première fois qu'HELIOMED peut opposer un délai à son prestataire sur une base documentée.

**Livrable de l'épisode.** L'arbre de décision d'HELIOMED, daté et validé en comité, et la matrice de triage figurant en Annexe C.

→ La suite en 🔴 §17.14, quand ces 21 campagnes devront être suivies sans se perdre.

→ **Chapitre 17 — Workflow de remédiation et gestion du *backlog*** : piloter le traitement entre la décision et la correction.

## Synthèse mentale du chapitre 16

Un seuil de gravité échoue pour deux raisons cumulées : il produit un volume arithmétiquement intraitable, et il produit le mauvais travail — simultanément trop large et trop étroit. Cinq entrées sont nécessaires à une décision, dont deux que vous seul détenez : l'exposition et la criticité. Préférez un arbre de décision à un score composite, parce qu'il produit une action, se relit en audit, tolère l'information manquante et place au cœur du raisonnement ce que vous êtes seul à savoir. Trois vérifications de quelques minutes — activation, condition de configuration, atteignabilité — retirent une part importante du volume, mais elles déprioritisent, elles ne closent pas. Les délais se calibrent sur la capacité mesurée, et l'écart entre capacité et risque est un constat à remonter, pas à absorber. Enfin, le levier le plus puissant n'est pas le triage mais le changement d'unité de travail : ne comptez pas les vulnérabilités fermées, comptez les actifs ramenés à un état de référence.

**Trois questions de vérification**

1. Démontrez en quatre lignes de calcul pourquoi une règle « corriger tout ce qui dépasse 7 » est intenable sur un parc de 200 serveurs, puis expliquez pourquoi ce n'est pas le problème principal de cette règle.
2. Pourquoi un score composite pondéré est-il plus fragile qu'un arbre de décision, notamment depuis la fragmentation des sources de données ?
3. Un constat porte sur un service installé mais désactivé. Quelle est la bonne décision, en quoi diffère-t-elle d'une clôture, et que devez-vous prévoir pour que cette décision reste valable dans six mois ?

---
