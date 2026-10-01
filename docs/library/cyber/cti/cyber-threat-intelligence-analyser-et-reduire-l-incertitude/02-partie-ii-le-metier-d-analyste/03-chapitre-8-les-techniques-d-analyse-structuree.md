---
title: Chapitre 8 — Les techniques d'analyse structurée
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 8.1 Pourquoi structurer

La raison n'est pas que les analystes raisonnent mal. C'est que **la mémoire de travail est limitée**, et que le raisonnement non écrit dépasse rapidement sa capacité.

Concrètement : au-delà de trois hypothèses et cinq éléments, personne ne tient mentalement la matrice de qui contredit quoi. On simplifie sans s'en apercevoir — et la simplification retient ce qui est saillant, pas ce qui est discriminant. C'est le §7.4, appliqué à sa propre pensée.

**Ce qu'une technique structurée apporte**, et c'est tout ce qu'elle apporte :

| Apport | Mécanisme |
|---|---|
| **Externaliser** | Le raisonnement est sur la table, plus dans la tête |
| **Rendre visible ce qui manque** | Une case vide dans un tableau se voit ; une absence dans un raisonnement, non |
| **Forcer l'exhaustivité minimale** | On ne peut pas remplir une colonne « hypothèse C » sans en formuler une |
| **Rendre le raisonnement auditable** | Un tiers peut contester une case, pas une intuition |

📌 **Ce qu'une technique n'apporte pas.** Elle ne rend pas une analyse juste. Elle rend une analyse **contestable** — c'est-à-dire vérifiable par autrui. Une matrice remplie avec des éléments faux produit une conclusion fausse, proprement documentée. La structuration discipline le raisonnement ; elle ne remplace ni la qualité des sources ni le jugement.

## 8.2 L'analyse d'hypothèses concurrentes

La technique centrale du métier. Voici la méthode complète, en sept étapes.

**Étape 1 — Énumérer les hypothèses.** Trois minimum, y compris celles qui déplaisent et celle qui est banale. Elles doivent être **mutuellement exclusives** autant que possible, et couvrir l'espace des possibles.

**Étape 2 — Lister les éléments.** Tout ce dont vous disposez : observations, informations de source externe, absences significatives. Chaque élément sur une ligne.

**Étape 3 — Construire la matrice.** Une ligne par élément, une colonne par hypothèse.

**Étape 4 — Remplir, en évaluant la compatibilité.** Pour chaque case, une seule question : *si cette hypothèse était vraie, cet élément serait-il attendu ?*

| Symbole | Signification |
|---|---|
| `++` | Fortement attendu — l'hypothèse le prédit |
| `+` | Compatible |
| `0` | Neutre — n'apporte rien |
| `−` | Peu compatible — l'hypothèse le rend surprenant |
| `−−` | **Fortement contredit** — l'hypothèse le rend très improbable |

**Étape 5 — Lire les colonnes, pas les lignes.** C'est le renversement méthodologique de la technique.

> **On ne retient pas l'hypothèse qui a le plus de `++`. On élimine celles qui ont des `−−`.**

Une hypothèse qui explique tout n'est pas nécessairement forte : elle est peut-être seulement vague. Une hypothèse contredite par un seul élément solide est éliminée, même si dix autres éléments la soutiennent.

**Étape 6 — Identifier ce qui manque.** Quelle information, si vous l'obteniez, produirait un `−−` quelque part ? C'est votre priorité de collecte — et c'est la jonction avec le chapitre 14.

**Étape 7 — Conclure.** L'hypothèse retenue, celle qui vient ensuite, ce qui les départagerait, et le niveau de confiance.

🧪 **EN PRATIQUE — la matrice, format court**

| Élément | H-A | H-B | H-C |
|---|---|---|---|
| ① … | `+` | `+` | `++` |
| ② … | `++` | `−−` | `0` |
| ③ … | `+` | `−` | `−−` |
| **Verdict** | Tient | **Éliminée** (②) | Affaiblie (③) |

**Ce que la lecture en colonnes révèle immédiatement** : ici, l'hypothèse B est éliminée par un seul élément, quelle que soit la quantité de soutien qu'elle recueille par ailleurs. C'est exactement ce qui s'est passé au mini-lab 2 avec l'appartenance du poste.

## 8.3 Génération d'hypothèses et test de complétude

L'étape 1 est celle qu'on bâcle, et une matrice construite sur des hypothèses mal choisies produit une conclusion propre et fausse.

**Trois méthodes de génération**, à combiner :

| Méthode | Principe | Ce qu'elle débloque |
|---|---|---|
| **Par acteur** | Qui pourrait produire cette observation ? | Les hypothèses d'origine |
| **Par mécanisme** | Quel enchaînement produirait cela ? | Les hypothèses techniques et **les explications légitimes** |
| **Par inversion** | Que faudrait-il pour que ce ne soit rien ? | L'hypothèse banale, celle qu'on n'écrit jamais |

**Le test de complétude** — trois questions à poser à votre liste :

1. Ai-je une hypothèse **bénigne** ? Erreur de configuration, service légitime, coïncidence.
2. Ai-je une hypothèse **désagréable** ? Celle qui impliquerait que nous avons échoué quelque part.
3. Ai-je une hypothèse **ennuyeuse** ? Celle qui ne produira aucun rapport intéressant.

⚠️ Si les trois manquent, votre matrice est déjà orientée avant d'être remplie. Les hypothèses bénignes et ennuyeuses sont, statistiquement, les plus souvent vraies — et les moins souvent écrites.

## 8.4 Indicateurs et signaux d'alerte

**Le principe** : au lieu d'attendre de savoir laquelle des hypothèses est vraie, on définit **à l'avance** ce qui trancherait, et on surveille.

**Comment on construit une grille de signaux :**

| Hypothèse | Si elle est vraie, on devrait observer… | Ce qui l'infirmerait |
|---|---|---|
| A — compromission externe | Persistance, mouvement latéral, communication sortante inhabituelle | Aucune activité au-delà de l'événement initial |
| B — menace interne | Accès en dehors du périmètre habituel de la personne, sur ses propres identifiants | Les accès proviennent d'un compte qui n'est pas le sien |
| C — changement légitime | Correspondance avec une note de version, un ticket, un déploiement | Aucune trace de changement dans les registres |

**Ce que cette grille change** : elle transforme une analyse figée en **dispositif de veille orienté**. Et surtout, elle permet de conclure honnêtement en attendant : *« nous ne pouvons pas trancher ; voici les trois signaux que nous surveillons et qui trancheraient »*. C'est une conclusion parfaitement acceptable, et infiniment plus utile qu'une conclusion forcée.

✅ **BONNE PRATIQUE (P1)** — Cette grille est aussi ce qui alimente le chapitre 30 : les signaux d'alerte deviennent des requêtes de détection. C'est le lien le plus direct entre l'analyse et l'opérationnel, et il est rarement exploité.

## 8.5 Avocat du diable et équipe rouge analytique

Deux dispositifs contre le consensus prématuré et le biais de confirmation.

| Dispositif | Principe | Quand l'employer | Coût |
|---|---|---|---|
| **Avocat du diable** | Une personne est chargée d'attaquer la conclusion retenue, quelle que soit son opinion réelle | Décision engageante, conclusion consensuelle trop rapide | 30 à 60 min |
| **Équipe rouge analytique** | Un groupe construit l'argumentaire complet de l'hypothèse concurrente | Enjeu majeur, désaccord persistant | Une demi-journée |

**La condition de fonctionnement du premier**, et elle est souvent manquée : le rôle doit être **explicitement attribué**, pas spontané. Une objection spontanée est reçue comme une opposition personnelle ; une objection produite au titre d'un rôle est reçue comme un service. La différence de climat est considérable, et elle décide de l'efficacité du dispositif.

📌 **LIMITES** — L'avocat du diable ritualisé perd son effet. S'il est systématique et que chacun sait que « c'est le rôle », l'exercice devient une formalité. Employez-le sur les décisions qui comptent, pas sur toutes.

## 8.6 L'analyse des hypothèses clés

**Ce que c'est** : identifier les **présupposés** sur lesquels repose votre raisonnement, et les tester un par un.

Une hypothèse clé n'est pas une hypothèse au sens du §6.1. C'est quelque chose que vous tenez pour acquis **sans l'avoir formulé** — et qui, s'il est faux, effondre tout.

**Exemples d'hypothèses clés courantes en CTI** :

| Présupposé implicite | Ce qui se passe s'il est faux |
|---|---|
| « Nos journaux couvrent le périmètre concerné » | L'absence d'observation ne vaut rien (§4.3) |
| « Les deux sources sont indépendantes » | Le recoupement n'existe pas (§10.4) |
| « L'adversaire n'a pas connaissance de nos mesures » | Toute la logique de détection est fragilisée |
| « Ce produit est déployé dans la version que nous croyons » | L'exposition est mal évaluée |
| « Le comportement observé est intentionnel » | On analyse une erreur comme une attaque |

**La méthode** : écrire la conclusion, puis se demander *qu'est-ce que je tiens pour vrai sans l'avoir vérifié ?* Lister trois à cinq présupposés, et pour chacun : *comment le vérifier, et que se passe-t-il s'il est faux ?*

C'est la technique la moins coûteuse du chapitre — quinze minutes — et celle dont le rendement est le plus élevé, parce qu'elle attaque le raisonnement à sa base plutôt qu'à ses conclusions.

## 8.7 📌 Le coût de chaque technique, et quand ne pas l'employer

C'est la section que les cours de méthode omettent, et c'est celle qui décide de l'adoption réelle.

| Technique | Coût | À employer quand | **À ne pas employer quand** |
|---|---|---|---|
| Règle des trois hypothèses (§6.1) | 2 min | **Toujours** | Jamais d'exception |
| Matrice d'hypothèses concurrentes | 1 à 3 h | Dossier ambigu, décision engageante, désaccord | Le fait est établi · l'urgence est réelle · une seule hypothèse est plausible et vérifiable en dix minutes |
| Génération structurée d'hypothèses | 20 min | Dossier complexe, ou quand la première liste paraît courte | Situation routinière |
| Grille de signaux d'alerte | 30 min | Quand on ne peut pas trancher maintenant | Quand la question sera résolue avant que la grille ne serve |
| Avocat du diable | 30-60 min | Décision engageante, consensus rapide | Décisions courantes — l'effet s'use |
| Équipe rouge analytique | 1/2 journée | Enjeu majeur | Le reste du temps |
| Analyse des hypothèses clés | 15 min | **Presque toujours** — meilleur rendement du chapitre | Rarement inutile |

⚠️ **PIÈGE — la méthode qui coûte plus que la décision**
Une matrice complète sur un constat qui sera tranché par une requête de dix minutes est du gaspillage, et pire : elle discrédite la méthode auprès de ceux qui la subissent. **La proportionnalité est une compétence analytique à part entière.** Deux règles simples : si la décision est réversible et peu coûteuse, décidez et corrigez ; si elle est engageante ou irréversible, structurez.

🎯 **ET MAINTENANT ?**
*Il est 17 h, un signalement arrive, une décision de blocage est attendue avant 18 h. Vous n'avez pas le temps d'une matrice. Que faites-vous ?*
**Réponse** : la règle des trois hypothèses — deux minutes — et l'analyse des hypothèses clés — dix minutes, sur les deux ou trois présupposés qui portent la décision. Vous écrivez les trois hypothèses, vous identifiez ce que vous tenez pour acquis, et vous décidez en le disant. La conclusion sera : *« nous recommandons le blocage, sur l'hypothèse A ; cette recommandation repose sur le présupposé que [X], non vérifié à cette heure ; si [X] est faux, la mesure est inutile mais sans effet de bord »*. C'est court, honnête, et cela permet de décider.

## 8.8 ✅ Livrable — La matrice d'hypothèses concurrentes

Modèle complet, à reprendre en annexe C.

**En-tête**

| Champ | Contenu |
|---|---|
| Question analytique | *(formulée comme une question, pas comme un sujet)* |
| Demandeur | *(nom)* |
| Date | *(et date de réexamen prévue)* |
| Analyste | *(nom)* · Relecteur : *(nom)* |

**Hypothèses** — trois minimum, dont une bénigne et une ennuyeuse

| Réf | Hypothèse | Origine de la formulation |
|---|---|---|
| H-A | | |
| H-B | | |
| H-C | | |

**Matrice**

| Réf | Élément | Source | Date | H-A | H-B | H-C |
|---|---|---|---|---|---|---|
| ① | | | | | | |

**Lecture**

| Hypothèse | Éliminée par | Verdict |
|---|---|---|

**Hypothèses clés** *(ce que je tiens pour acquis)*

| Présupposé | Vérifié ? | Si faux, alors… |
|---|---|---|

**Conclusion**

- Hypothèse retenue : … — **confiance** : …
- Hypothèse suivante la plus probable : …
- **Ce qui trancherait** : …
- **Ce qui invaliderait cette conclusion** : …
- Réexamen : …

## 8.9 🔴 FIL ROUGE — septembre 2029 : la première matrice

Six semaines après l'épisode de juillet (§7.9), un nouveau signalement arrive : un partenaire industriel d'HELIOMED informe que trois de ses clients — dont deux fournisseurs de dispositifs médicaux — ont subi une intrusion en août. Le vecteur n'est pas précisé.

**Ce que Nour aurait fait en juillet** : conclure au ciblage sectoriel, recommander une mobilisation.

**Ce qu'elle fait cette fois.** Elle bloque deux heures et construit une matrice.

**Les hypothèses**

| Réf | Hypothèse | Origine |
|---|---|---|
| **H-A** | Ciblage sectoriel des fournisseurs de dispositifs médicaux | Par acteur — l'hypothèse spontanée |
| **H-B** | Exploitation opportuniste d'un composant commun au secteur | Par mécanisme — celle qui manquait en juillet |
| **H-C** | Compromission du partenaire lui-même, ses clients étant atteints par ricochet | Par inversion — **l'hypothèse ennuyeuse** |

**La matrice**

| Réf | Élément | H-A | H-B | H-C |
|---|---|---|---|---|
| ① | Trois clients touchés en un mois | `+` | `+` | `++` |
| ② | Deux sur trois sont des fabricants de dispositifs médicaux | `++` | `+` | `0` |
| ③ | **Le troisième est un équipementier automobile** | `−−` | `+` | `+` |
| ④ | Les trois utilisent le même prestataire d'infogérance — le partenaire | `0` | `0` | `++` |
| ⑤ | Aucune revendication publique | `+` | `+` | `+` |
| ⑥ | Le partenaire n'a pas signalé d'incident chez lui | `0` | `0` | `−` |

**La lecture en colonnes**

| Hypothèse | Verdict |
|---|---|
| **H-A** | **Éliminée** par ③. Un équipementier automobile n'entre pas dans un ciblage sectoriel médical |
| H-B | Tient. Aucun élément ne la contredit |
| **H-C** | **La plus soutenue** — ① et ④ la prédisent fortement. Affaiblie par ⑥, mais faiblement : une organisation peut ignorer sa propre compromission |

**L'élément ③ est le pivot**, et il aurait pu passer inaperçu. Nour ne l'avait obtenu qu'en rappelant le partenaire pour demander la liste complète des victimes — dix minutes de téléphone. Sans cette question, sa matrice comportait deux fabricants sur deux, et H-A tenait.

**Les hypothèses clés identifiées**

| Présupposé | Vérifié ? | Si faux |
|---|---|---|
| Les trois victimes sont bien clientes du même partenaire | ✅ confirmé | — |
| Le partenaire nous dit tout ce qu'il sait | ❌ non vérifiable | H-C serait renforcée |
| HELIOMED est cliente de ce partenaire pour un périmètre significatif | ✅ vérifié — **poste de travail et support N1** | — |

**La conclusion produite**

> *Nous estimons **probable** que ces trois intrusions procèdent d'une compromission du prestataire commun plutôt que d'un ciblage sectoriel — **confiance moyenne**, fondée sur la présence d'une victime hors secteur et sur le prestataire partagé, affaiblie par l'absence de signalement du prestataire lui-même.*
>
> *L'hypothèse d'un ciblage sectoriel est **écartée** : l'une des trois victimes est un équipementier automobile.*
>
> *HELIOMED est exposée à cette hypothèse : le prestataire concerné administre notre parc bureautique.*
>
> *Ce qui trancherait : le vecteur d'entrée constaté chez les trois victimes · la confirmation ou l'infirmation d'un incident chez le prestataire · l'existence d'une connexion d'administration anormale sur notre propre parc.*
>
> *Ce qui invaliderait : la découverte d'un vecteur commun indépendant du prestataire.*

**Ce que la décision devient.** Pas une mobilisation générale. Trois actions ciblées : une recherche rétrospective sur les connexions d'administration du prestataire depuis juillet · une question écrite au prestataire sur son propre état · une revue des accès dont il dispose. Coût : une journée-homme, contre neuf mille euros en juillet.

**Le résultat, trois semaines plus tard.** Le prestataire confirme une compromission de l'un de ses postes d'administration, détectée fin août, non signalée à ses clients. La recherche rétrospective d'HELIOMED ne trouve rien — les accès du prestataire au parc d'HELIOMED transitaient par un chemin non concerné. Aucune compromission.

**Ce que Nour retient**, et qui est différent de juillet :

> *Cette fois j'ai eu raison, mais ce n'est pas ce qui compte. Ce qui compte est que j'aurais pu avoir tort et qu'on l'aurait vu : la matrice disait exactement ce qui l'aurait renversée.*

**Livrable de l'épisode.** La matrice complète, versée au dossier — et la question de dix minutes au partenaire, devenue un réflexe : *avez-vous la liste complète des victimes ?*

→ La suite en 🔴 §9.7, quand il faudra mettre un mot sur « probable » et « confiance moyenne ».

## Synthèse mentale du chapitre 8

On structure parce que la mémoire de travail est limitée : au-delà de trois hypothèses et cinq éléments, on simplifie sans s'en apercevoir, et la simplification retient le saillant plutôt que le discriminant. Une technique n'apporte pas la justesse, elle apporte la contestabilité — une matrice remplie d'éléments faux produit une conclusion fausse proprement documentée. Le renversement méthodologique de l'analyse d'hypothèses concurrentes tient dans une phrase : on ne retient pas l'hypothèse la plus soutenue, on élimine celles qui sont contredites. La génération d'hypothèses se teste par trois questions — en ai-je une bénigne, une désagréable, une ennuyeuse — et leur absence signale une matrice déjà orientée. L'analyse des hypothèses clés attaque le raisonnement à sa base pour quinze minutes de travail : c'est le meilleur rendement du chapitre. Enfin, la proportionnalité est une compétence analytique : une méthode qui coûte plus que la décision qu'elle éclaire discrédite la méthode.

**Trois questions de vérification**

1. Une hypothèse est soutenue par huit éléments et contredite par un seul. Que faites-vous, et pourquoi ce n'est pas une question de comptage ?
2. Vous avez trois hypothèses et aucune n'est bénigne. Qu'est-ce que cela révèle, et que faites-vous avant de remplir la matrice ?
3. Une décision de blocage est attendue dans une heure. Quelles techniques employez-vous, et laquelle écartez-vous malgré son intérêt ?

→ **Chapitre 9 — Calibrer** : mettre un mot sur « probable », un chiffre derrière « confiance moyenne », et cesser de confondre la solidité d'une conclusion avec la gravité de son objet.

---
