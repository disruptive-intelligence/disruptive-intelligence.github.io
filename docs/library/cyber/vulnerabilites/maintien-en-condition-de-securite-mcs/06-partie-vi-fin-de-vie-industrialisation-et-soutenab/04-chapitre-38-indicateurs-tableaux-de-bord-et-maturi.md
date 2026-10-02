---
title: Chapitre 38 — Indicateurs, tableaux de bord et maturité
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE VI — Fin de vie, industrialisation et soutenabilité
  - index.md
---

## 38.1 Ce qu'un indicateur doit permettre de décider

Un indicateur qui ne change aucune décision n'a pas d'utilité, quel que soit son intérêt apparent. Trois questions à poser avant d'en créer un :

1. **Quelle décision** cet indicateur permet-il de prendre, et par qui ?
2. **Quel seuil** déclenche une action ?
3. **Que fait-on** exactement quand ce seuil est franchi ?

Sans réponse aux trois, l'indicateur est décoratif — et il consommera du temps de production chaque mois.

## 38.2 Le dictionnaire d'indicateurs

C'est le livrable central du chapitre. **Chaque indicateur doit être défini par huit attributs**, faute de quoi deux personnes calculeront deux valeurs différentes.

| Attribut | Rôle |
|---|---|
| Formule | Le calcul exact |
| Numérateur | Ce qui est compté |
| **Dénominateur** | Sur quoi c'est rapporté — l'attribut le plus important |
| Périmètre | Quels actifs, quelles classes |
| Période | Sur quel intervalle |
| **Exclusions** | Ce qui est retiré, et pourquoi |
| Source | D'où viennent les données |
| Propriétaire | Qui le produit et en répond |

**Les dix indicateurs de référence** — la fiche complète de chacun figure en **Annexe K** :

| # | Indicateur | Formule | Ce qu'il mesure |
|---|---|---|---|
| 1 | **Couverture d'inventaire** | actifs identifiés / actifs estimés du périmètre | La fiabilité de tout le reste |
| 2 | **Couverture de scan** | actifs scannés avec succès / périmètre de référence | Ce que l'on voit réellement |
| 3 | **Conformité de correctifs** | actifs conformes / actifs éligibles | L'état du parc |
| 4 | **Respect des délais** | constats clos dans le délai / constats arrivés à échéance | La tenue des engagements |
| 5 | **Âge moyen du *backlog*** | moyenne des durées depuis la première détection | La vitesse réelle |
| 6 | **Dette critique échue** | constats critiques dont le délai est dépassé | Le retard qui compte |
| 7 | **Âge des dérogations** | ancienneté moyenne des dérogations ouvertes | La dette formellement acceptée |
| 8 | **Taux de récurrence** | constats réapparus / constats clos | Un problème de source (§17.9) |
| 9 | **Taux de retour arrière** | déploiements annulés / déploiements réalisés | La qualité de la validation |
| 10 | **Taux d'échec de déploiement** | actifs en échec / actifs ciblés | La santé de la chaîne |

**Les indicateurs 1 et 2 conditionnent tous les autres**, et leur combinaison appelle une précaution de vocabulaire.

Le produit *conformité × couverture* — 95 % × 60 % = 57 % — est le **ratio conservateur d'actifs confirmés conformes sur le périmètre**. Il suppose implicitement que **tout actif non mesuré est non conforme**. C'est une hypothèse de prudence, pas une mesure : il ne décrit pas la conformité réelle, qui reste **inconnue** sur les 40 % non mesurés.

✅ **Publier quatre valeurs, jamais une seule** :

| Valeur | Exemple |
|---|---|
| Couverture | 60 % |
| Conformité **dans la population mesurée** | 95 % |
| **Ratio confirmé conforme sur périmètre** | 57 % |
| **Non mesuré** | 40 % |

La dernière ligne est celle qui appelle une décision. Les trois premières décrivent ce que vous savez ; la quatrième décrit ce que vous ignorez.

## 38.3 Les pièges de calcul

| Piège | Mécanisme | Contre-mesure |
|---|---|---|
| **Dénominateur mouvant** | Le périmètre change d'un mois à l'autre, la tendance devient illisible | Périmètre de référence figé, avec ses variations documentées |
| **Exclusions non déclarées** | Les actifs difficiles sortent silencieusement (§15.6) | Liste d'exclusions publiée avec l'indicateur |
| **Agrégation trompeuse** | Un taux global masque une population entière | Publication par population (§10.11) |
| **Moyenne qui masque la traîne** | L'âge moyen cache les constats très anciens | Publier aussi la médiane et le maximum |
| **Indicateur récompensant l'inaction** | Le nombre de vulnérabilités détectées baisse si l'on scanne moins | Toujours associer volume et couverture |
| **Remise à zéro d'historique** | Un actif recréé perd son ancienneté (§15.7) | Identifiant pivot stable |

## 38.4 ⚠️ La discontinuité de modèle comme piège de reporting

Un cas particulier qui mérite d'être isolé, car il produit des conclusions entièrement fausses.

Les modèles de score externes évoluent par versions, et **un changement de version déplace tous les scores simultanément** (§4.5). Conséquence : un indicateur fondé sur un seuil de score peut varier fortement sans qu'aucun correctif n'ait été appliqué et sans qu'aucune vulnérabilité n'ait changé.

**La règle** : toute série temporelle traversant un changement de modèle doit être **marquée comme discontinue** sur le graphique, et l'interprétation doit le mentionner. Avant de célébrer une amélioration soudaine, vérifiez d'abord ce qui a changé dans les données d'entrée.

## 38.5 Concevoir un tableau de bord par audience

| Audience | Nombre d'indicateurs | Contenu | Fréquence |
|---|---|---|---|
| **Exploitation** | 8 à 12 | Opérationnels : échecs, traîne, campagnes en cours, échéances proches | Hebdomadaire |
| **Comité MCS** | 5 à 8 | Résultat : conformité par population, respect des délais, dérogations, dette | Mensuelle |
| **Direction générale** | **3 à 5** | Risque : dette critique, actifs hors support, tendance sur 4 à 8 trimestres | Trimestrielle |
| **Auditeur** | Le dossier de preuves | Définitions, périmètres, exclusions, historique (ch. 39) | À la demande |

**La règle de la direction générale** : trois à cinq indicateurs, une tendance, et une décision demandée. Un comité de direction ne réagit pas à un niveau, il réagit à une **pente** — et il ne peut arbitrer que ce qui lui est présenté sous forme d'options (§12.6).

## 38.6 Le modèle de maturité

Un modèle de maturité sert à situer une organisation et à définir la prochaine étape. Il devient cosmétique dès qu'il sert à s'auto-évaluer favorablement.

| Niveau | Nom | Caractéristique |
|---|---|---|
| **0** | Inexistant | Aucun processus ; les correctifs s'appliquent au gré des incidents |
| **1** | Réactif | On corrige quand un problème survient ; pas d'inventaire fiable |
| **2** | Documenté | Politique écrite, inventaire constitué, propriétaires nommés |
| **3** | Piloté | Délais définis et mesurés, dérogations tracées, indicateurs suivis |
| **4** | Industrialisé | Automatisation, campagnes, preuve produite systématiquement |
| **5** | Adaptatif et fondé sur le risque | Priorisation par exposition et exploitation, boucle d'amélioration, MCS *by design* |

**L'usage utile** : identifier le niveau atteint **par domaine** — inventaire, veille, remédiation, configuration, identités, preuve — et non globalement. Une organisation est rarement au même niveau partout, et un domaine critique faible **plafonne** la maturité de tout ce qui en dépend. La grille par domaine figure en Annexe K.

## 38.7 Historisation et conservation

Sans historique, aucun progrès n'est démontrable — et la démonstration de progrès est ce qui pérennise un budget (§7.5).

| Exigence | Contenu |
|---|---|
| Conservation | Valeurs mensuelles conservées plusieurs années, indépendamment des outils |
| **Indépendance des outils** | Export périodique en format ouvert (§15.12) |
| Traçabilité des définitions | Un changement de formule est daté et documenté |
| Marquage des ruptures | Changement de périmètre, d'outil ou de modèle (§38.4) |

## 38.8 🔬 Mini-lab 9 — Construire un tableau de bord MCS

**Objectif** — Produire un tableau de bord exploitable et repérer les métriques trompeuses.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** §38.2, §38.3, annexes I.4 et K · **Livrable** deux tableaux de bord (comité, direction) + trois métriques trompeuses identifiées.
**Compétences validées** — ✔ définir un indicateur par ses huit attributs ✔ adapter le tableau de bord à son audience ✔ repérer une métrique trompeuse ✔ publier une population non mesurée sans la faire disparaître

**Données fournies.**

| Source | Contenu |
|---|---|
| Inventaire | Périmètre de référence : 340 actifs, dont 28 hors support, 12 sans propriétaire |
| Scans | 268 actifs scannés avec authentification, 31 en échec d'authentification, 41 non scannés (dont 14 exclus documentés) |
| Constats | 1 240 ouverts, dont 38 critiques échus ; âge moyen 74 jours, médiane 21 jours, maximum 610 jours |
| Tickets | 96 ouverts, 14 dépassant leur échéance, 9 sans propriétaire accepté |
| Dérogations | 17 ouvertes, âge moyen 8 mois, dont 4 renouvelées au moins une fois |
| Campagnes | 6 en cours, 2 en retard, taux d'échec moyen 4 % |
| Conformité | 241 actifs conformes sur les 268 scannés avec succès |

**Questions.** (a) Proposez 5 à 8 indicateurs avec leur formule et leur périmètre. (b) Produisez la version comité MCS et la version direction générale. (c) Identifiez trois métriques trompeuses que ces données invitent à produire.

**Corrigé commenté**

**(a) Les indicateurs retenus**

| Indicateur | Formule | Valeur | Commentaire |
|---|---|---|---|
| Couverture de scan | 268 / 340 | **79 %** | Le chiffre qui conditionne tous les autres |
| Conformité interne au scan | 241 / 268 | 90 % | À ne jamais publier seul |
| **Ratio confirmé conforme** | 241 / 340 | **71 %** | Conservateur : traite les 72 non mesurés comme non conformes |
| **Non mesuré** | 72 / 340 | **21 %** | La valeur qui appelle une décision |
| Actifs hors support | 28 / 340 | 8,2 % | Dette structurelle |
| Dette critique échue | 38 constats | 38 | En valeur absolue, pas en taux |
| Âge du *backlog* | médiane / maximum | 21 j / **610 j** | La médiane rassure, le maximum informe |
| Âge des dérogations | moyenne, dont renouvelées | 8 mois, 4 renouvelées | Dette acceptée |
| Actifs sans propriétaire | 12 | 12 | Blocage structurel |

**(b) Les deux versions**

*Comité MCS* — les huit ci-dessus, avec les 41 actifs non scannés détaillés (14 exclus documentés, 27 à traiter) et les 9 tickets sans propriétaire accepté.

*Direction générale* — quatre lignes seulement :

1. Ratio confirmé conforme : **71 %**, avec 21 % non mesuré — tendance sur quatre trimestres.
2. Actifs hors support : **28**, dont X exposés — avec le plan et son coût.
3. Constats critiques échus : **38** — avec la cause principale.
4. Dette acceptée : **17 dérogations**, dont 4 renouvelées — décision demandée sur celles-ci.

**(c) Les trois métriques trompeuses**

| Métrique | Pourquoi elle trompe |
|---|---|
| **« 90 % de conformité »** | C'est la conformité **dans la population mesurée**, sur 79 % de couverture. Le ratio confirmé conforme est de 71 %, et 21 % du périmètre reste **non mesuré** — c'est-à-dire ni conforme ni non conforme (Annexe K.2) |
| **« Âge moyen du *backlog* : 74 jours »** | La moyenne est tirée par un maximum à 610 jours. La médiane à 21 jours décrit le flux normal, le maximum décrit le problème. Publier la seule moyenne ne décrit ni l'un ni l'autre |
| **« 1 240 constats ouverts »** | Volume brut sans priorisation ni couverture. Il baisserait si l'on scannait moins, et il n'indique aucune décision (§5.7) |

**L'erreur attendue** : produire un tableau de bord de quinze indicateurs pour la direction générale. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique.

## 38.9 🔴 FIL ROUGE — octobre 2028 : la question du directeur financier

Claire Nadeau présente au comité de direction le tableau de bord trimestriel. Quatre indicateurs, une tendance sur huit trimestres.

| Indicateur | T4 2026 | T4 2028 |
|---|---|---|
| Conformité globale, périmètre de référence | 72 % | **94 %** |
| Actifs hors support | 41 | **9** |
| Constats critiques échus | 61 | **7** |
| Dérogations ouvertes | 3 | **19** |

**La question de Karim Lebrun** porte sur la dernière ligne : *« Les trois premiers indicateurs s'améliorent nettement. Le quatrième a été multiplié par six. Comment interprétez-vous cela ? »*

**La réponse de Claire**, et c'est le point de cet épisode : les 3 dérogations de 2026 ne signifiaient pas que l'organisation n'avait que trois exceptions. Elles signifiaient qu'elle n'en formalisait que trois. Les autres existaient — sous forme de constats jamais traités, de systèmes ignorés, de compensations informelles. Les 19 dérogations de 2028 sont la **partie enfin visible** d'une dette qui a en réalité diminué.

Elle le démontre par un chiffre complémentaire : les constats ouverts depuis plus de 180 jours et non qualifiés — les dérogations non formalisées du §17.10 — sont passés de **47 à 2**.

**Ce que Karim Lebrun demande alors**, et qui devient la meilleure question de tout le fil rouge : *« Alors comment saurai-je, l'an prochain, si 19 dérogations est un bon ou un mauvais chiffre ? »*

**La réponse construite en séance**, qui donnera lieu à deux indicateurs supplémentaires : le nombre de dérogations n'est pas interprétable seul. Ce qui compte est leur **âge moyen** — une dette qui vieillit est une dette qui pourrit (§20.9) — et le **nombre de renouvellements**, qui mesure combien d'exceptions ont échoué à se résoudre.

**Les décisions du comité.**

1. Ajout de deux indicateurs au tableau de bord de direction : âge moyen des dérogations, et nombre de dérogations renouvelées au moins une fois.
2. Revue annuelle en comité de direction des dérogations renouvelées deux fois ou plus — application du §7.4.
3. La progression 72 % → 94 % est communiquée à l'assureur, avec le dossier de preuves associé. La surprime de 34 % d'octobre 2025 (§1.9) fait l'objet d'une renégociation.

**Ce que Claire note en conclusion.** *Le meilleur indicateur de maturité d'une organisation n'est pas son taux de conformité. C'est l'écart entre ce qu'elle sait de ses propres écarts et ce qu'elle en montre.*

→ La suite en 🔴 §39.8, avec la revue interne et la constitution du dossier de preuves.

→ **Chapitre 39 — Audit, contrôle et production de preuve** : prouver, c'est-à-dire résister à un contrôle.

## Synthèse mentale du chapitre 38

Un indicateur qui ne change aucune décision est décoratif, et il coûte du temps de production chaque mois. Huit attributs le définissent, dont le dénominateur, sans lequel deux personnes calculeront deux valeurs différentes. La couverture d'inventaire et la couverture de scan conditionnent tous les autres indicateurs : 95 % de conformité sur 60 % de couverture vaut 57 %. Les moyennes masquent la traîne — publiez médiane et maximum —, et un indicateur de volume brut récompense l'inaction puisqu'il baisse quand on scanne moins. Une série traversant un changement de modèle de score doit être marquée discontinue : vérifiez ce qui a changé dans les données avant de célébrer une amélioration soudaine. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique : trois à cinq pour une direction générale, avec une tendance et une décision demandée. Enfin, une hausse du nombre de dérogations peut signaler une amélioration : ce qui compte est leur âge, leur distribution et leur nombre de renouvellements.

**Trois questions de vérification**

1. Votre tableau de bord affiche 90 % de conformité. Quelles deux valeurs devez-vous connaître pour savoir ce que ce chiffre décrit réellement ?
2. Votre indicateur de vulnérabilités à forte probabilité chute de 30 % en une semaine sans aucun déploiement. Que vérifiez-vous avant toute communication ?
3. Le nombre de dérogations de votre organisation a été multiplié par six en deux ans. Est-ce un bon ou un mauvais signe, et quels indicateurs complémentaires permettent de trancher ?

---
