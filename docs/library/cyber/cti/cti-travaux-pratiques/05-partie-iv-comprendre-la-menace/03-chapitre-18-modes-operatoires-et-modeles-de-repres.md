---
title: Chapitre 18 — Modes opératoires et modèles de représentation
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE IV — Comprendre la menace
  - index.md
---

## 18.1 Pourquoi modéliser

**Le problème que les modèles résolvent** : sans langage commun, une intrusion se décrit en prose, et deux descriptions de la même intrusion ne se ressemblent pas. On ne peut ni comparer, ni agréger, ni mesurer une couverture.

**Ce qu'un modèle apporte**, et c'est tout ce qu'il apporte :

| Apport | Mécanisme |
|---|---|
| **Un langage partagé** | Analyste, détection et exploitation nomment la même chose de la même façon |
| **La comparabilité** | Deux incidents deviennent comparables |
| **La mesurabilité** | On peut dire ce qu'on couvre et ce qu'on ne couvre pas |
| **La complétude** | Une case vide se voit — comme dans la matrice du §8.2 |

📌 **Ce qu'un modèle n'apporte pas** : il ne dit pas ce qui est probable, ni ce qui est grave, ni ce qui vous concerne. C'est une **grille de description**, pas une grille d'évaluation. Confondre les deux produit des cartographies impressionnantes et sans valeur décisionnelle (§18.6).

## 18.2 Les référentiels de tactiques et techniques

**Le principe.** Un référentiel de ce type organise les comportements adverses observés en une hiérarchie à deux ou trois niveaux :

```
TACTIQUE      le but poursuivi à cette étape
   └── TECHNIQUE      la manière de l'atteindre
          └── SOUS-TECHNIQUE      la variante précise
```


**Ce qui fait leur force** : ils décrivent des **comportements observés**, pas des menaces théoriques. Chaque entrée est adossée à des cas documentés.

**Ce qui fait leur limite, et qui découle directement de la force précédente** :

> **Un référentiel décrit le passé observé. Ce qui n'y figure pas n'est pas inexistant — c'est simplement non encore documenté publiquement.**

C'est la formulation durable du §1.8, et elle survivra à toutes les versions.

**Les trois usages réels**, par ordre de valeur :

| Usage | Ce qu'il produit |
|---|---|
| **Décrire un incident** | Une description comparable et transmissible |
| **Mesurer une couverture de détection** | Une analyse d'écart (§30.3) |
| Décrire un acteur | Le moins utile — les acteurs partagent l'essentiel de leurs techniques |

## 18.3 Chaîne d'attaque et modèle du diamant

Deux autres modèles courants, avec leur domaine d'utilité propre.

| Modèle | Ce qu'il représente | Quand il est utile | Sa limite |
|---|---|---|---|
| **Chaîne d'attaque** | Une séquence linéaire d'étapes, de la reconnaissance à l'objectif | **Communiquer** avec des non-spécialistes · raisonner sur les points d'interruption | Les intrusions réelles ne sont ni linéaires ni complètes |
| **Modèle du diamant** | Quatre sommets — adversaire, infrastructure, capacité, victime — et leurs relations | **Pivoter** : d'un sommet connu vers les autres · relier des incidents | Ne dit rien de la chronologie |
| **Référentiel de techniques** | Un catalogue structuré de comportements | Décrire, mesurer, comparer | Volumineux, et sans hiérarchie de gravité |

**La règle de choix**, qui évite l'essentiel des débats stériles :

> **La chaîne pour expliquer. Le diamant pour relier. Le référentiel pour mesurer.**

Ces trois modèles ne sont pas concurrents. Les employer ensemble sur un même incident est le cas normal.

## 18.4 La pyramide de la difficulté

**Le principe** : tous les éléments qu'on peut détecter n'ont pas la même valeur, parce qu'ils ne coûtent pas la même chose à l'adversaire pour être changés.

```
                    ▲  COÛT POUR L'ADVERSAIRE
                    │
      Comportements │  ████████████████  très coûteux à changer
   Outils employés  │  ██████████
      Artefacts     │  ██████
   Noms de domaine  │  ████
        Adresses    │  ██
       Empreintes   │  █  trivial à changer
                    │
```


**Ce que cela implique pour votre travail** :

| Niveau | Durée de vie | Coût de détection | Rendement |
|---|---|---|---|
| Empreinte de fichier | Une variante | Très faible | **Très faible** |
| Adresse | Jours à semaines | Faible | Faible |
| Nom de domaine | Semaines | Faible | Faible |
| Artefact d'hôte | Mois | Moyen | Moyen |
| Outil employé | Mois à années | Élevé | Élevé |
| **Comportement** | **Années** | **Élevé** | **Très élevé** |

**La conséquence sur la production de renseignement** : un jeu de cent indicateurs techniques vaut moins qu'une description précise de trois comportements. Le premier se périme en semaines et produit des faux positifs ; le second oriente durablement la détection.

⚠️ **PIÈGE — le volume d'indicateurs comme mesure de valeur**
C'est le §3.3, et c'est le mode de facturation de nombreuses offres commerciales. Un flux se vend au volume parce que le volume est mesurable ; sa valeur, elle, se situe en haut de la pyramide, là où le volume est faible.

## 18.5 ⚠️ Quand ne pas utiliser un modèle

Quatre situations, toutes fréquentes.

| Situation | Pourquoi le modèle nuit |
|---|---|
| **Communiquer avec une direction** | Une matrice de techniques est illisible. Le récit vaut mieux |
| **Un incident en cours** | La classification consomme du temps que la réponse exige |
| **Une menace nouvelle** | Elle ne rentre pas dans les cases, et forcer la classification déforme l'observation |
| **Quand la classification devient l'objectif** | On produit une cartographie au lieu de produire une décision |

**La quatrième est la plus insidieuse.** Une organisation peut consacrer des mois à cartographier sa couverture sans qu'aucune règle de détection ne soit écrite. La cartographie est un moyen ; elle devient un livrable auto-justifié avec une facilité déconcertante.

## 18.6 Une cartographie est un actif à maintenir

C'est le point durable de ce chapitre, et il vaut indépendamment de tout référentiel particulier.

**Le mécanisme du vieillissement** :

| Cause | Effet |
|---|---|
| Le référentiel évolue | Techniques ajoutées, renommées, scindées, dépréciées |
| Vos règles évoluent | Ajoutées, modifiées, désactivées sans mise à jour de la cartographie |
| Vos sources de journaux évoluent | Une règle cartographiée devient inopérante si sa source disparaît |
| Votre parc évolue | Une technique non applicable le devient, ou l'inverse |

**Ce qu'une cartographie non maintenue produit** : une image rassurante et fausse — exactement le problème du dénominateur inconnu au cours MCS.

✅ **BONNE PRATIQUE (P0) — les quatre attributs d'une cartographie exploitable**

Pour chaque case cartographiée :

| Attribut | Pourquoi |
|---|---|
| **La source de journaux** dont dépend la couverture | Si elle disparaît, la couverture disparaît |
| **La date du dernier test** | Une règle non testée est une intention |
| **Le niveau de couverture** — totale, partielle, théorique | « Couvert » sans nuance est presque toujours faux |
| **La version du référentiel** utilisée | Pour savoir ce qui devra être remappé |

⏱ **ÉTAT DE L'ART (vérifié le 2 août 2026)** — Le principal référentiel public de tactiques et techniques a connu en avril 2026 une évolution structurelle : l'une de ses tactiques historiques a été **scindée en deux**, l'une conservant l'identifiant d'origine. Une table de correspondance a été publiée. Toute cartographie, règle ou publication antérieure y faisant référence doit être remappée. 📎 [S-01]

**Ce que cet événement illustre**, et c'est l'enseignement à retenir quand la version aura changé : **un remaniement structurel d'un référentiel n'est pas un événement exceptionnel**, c'est un événement périodique. La question n'est pas de savoir s'il se reproduira, mais si votre cartographie porte les attributs qui permettront de la remapper — notamment le quatrième.

## 18.7 🔬 Mini-lab 6 — Lire une cartographie de couverture

**Objectif** — Interpréter une cartographie et identifier ce qu'elle ne dit pas.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §18.4, §18.6 · **Livrable** analyse d'écart priorisée
**Compétences validées** — ✔ distinguer couverture théorique et effective ✔ relier une couverture à sa source de journaux ✔ repérer le biais de facilité ✔ prioriser un développement de détection

**Le dossier fourni** — extrait d'une cartographie d'une organisation de 900 personnes, secteur industriel.

| Tactique | Techniques du référentiel | Déclarées couvertes | Taux affiché |
|---|---|---|---|
| Reconnaissance | 10 | 1 | 10 % |
| Accès initial | 11 | **9** | **82 %** |
| Exécution | 14 | **12** | **86 %** |
| Persistance | 20 | 7 | 35 % |
| Élévation de privilèges | 14 | 6 | 43 % |
| Contournement des défenses | 43 | 8 | 19 % |
| Accès aux identifiants | 17 | 5 | 29 % |
| Découverte | 32 | 3 | 9 % |
| Mouvement latéral | 9 | 4 | 44 % |
| Collecte | 17 | 2 | 12 % |
| Exfiltration | 9 | 2 | 22 % |
| Impact | 14 | **11** | **79 %** |
| **Total** | **210** | **70** | **33 %** |

**Informations complémentaires fournies :**

```
· 52 des 70 règles reposent sur les journaux du poste de travail.
· 9 reposent sur les journaux du pare-feu.
· 6 reposent sur les journaux d'annuaire.
· 3 reposent sur une source applicative.
· Aucune des 70 règles n'a de date de test enregistrée.
· La cartographie a été établie il y a 14 mois.
· Le référentiel a connu une évolution majeure il y a 4 mois.
· Les 3 derniers incidents de l'organisation ont impliqué :
    accès initial via identifiants valides · découverte · mouvement
    latéral · exfiltration.
```


**Questions** : (a) Que vous dit ce tableau, et que ne vous dit-il pas ? (b) Où est le biais ? (c) Quelles trois priorités ? (d) Quelle information manquante est la plus grave ?

---

**Corrigé commenté**

**(a) Ce que le tableau dit, et ne dit pas**

| Il dit | Il ne dit pas |
|---|---|
| 70 techniques sont déclarées couvertes sur 210 | Si ces règles **fonctionnent** — aucune date de test |
| La couverture est très inégale selon les tactiques | Si les techniques couvertes sont **pertinentes pour cette organisation** |
| Un taux global de 33 % | Ce que 33 % signifie — toutes les techniques ne se valent pas |
| — | Si la cartographie est encore **valide** : 14 mois, et une évolution du référentiel il y a 4 mois |

⚠️ **Le taux global de 33 % est le chiffre le moins informatif du tableau.** Il additionne des techniques de poids très différents et suppose que couvrir 210 techniques serait un objectif — ce qui n'a aucun sens.

**(b) Le biais : la couverture suit la facilité, pas le risque**

Le croisement entre les taux et les sources de journaux est sans ambiguïté :

| Tactique | Taux | Source dominante | Difficulté de détection |
|---|---|---|---|
| Accès initial, Exécution, Impact | **79-86 %** | Poste de travail | **Facile** — les journaux existent |
| Découverte, Collecte, Contournement | **9-19 %** | Réseau, annuaire, applicatif | **Difficile** — journaux absents ou bruités |

**52 des 70 règles reposent sur une seule source.** L'organisation ne couvre pas ce qui est risqué : elle couvre **ce qu'elle voit**, et elle ne voit qu'un poste de travail.

**La confirmation vient des incidents réels** : les trois derniers ont impliqué identifiants valides, découverte, mouvement latéral et exfiltration — soit quatre tactiques dont les taux sont respectivement 29 %, 9 %, 44 % et 22 %. **La cartographie est excellente là où rien ne s'est passé.**

**(c) Les trois priorités**

| Priorité | Action | Justification |
|---|---|---|
| **1** | **Obtenir les journaux d'annuaire complets** | Débloque simultanément *accès aux identifiants*, *découverte* et *mouvement latéral* — les trois tactiques présentes dans les incidents réels. Une source, trois tactiques |
| **2** | **Tester les 70 règles existantes** | Une couverture déclarée non testée est une hypothèse. Le taux réel est inconnu, et il est certainement inférieur à 33 % |
| **3** | **Remapper la cartographie** sur la version courante du référentiel | 4 mois après une évolution majeure, une partie des correspondances est fausse |

⚠️ **L'ordre compte.** La priorité 2 est moins visible que la 1 mais plus urgente sur le plan de la sincérité : on ne peut pas prioriser à partir d'un état des lieux dont on ignore s'il est vrai.

**(d) L'information manquante la plus grave**

**L'absence de date de test.** Elle rend l'ensemble du tableau inexploitable : sans test, « couvert » signifie *une règle existe*, pas *elle détecte*. Les autres lacunes — pertinence pour l'organisation, version du référentiel, niveau de couverture partielle ou totale — sont graves ; celle-ci invalide tout le reste.

**Les trois erreurs attendues**

1. **Conclure qu'il faut augmenter le taux global.** L'objectif n'est pas 210 techniques : c'est de couvrir ce qui est plausible dans le contexte.
2. **Prioriser sur les tactiques aux taux les plus bas.** *Reconnaissance* est à 10 % et c'est sans importance : cette activité est majoritairement externe et non détectable depuis l'organisation.
3. **Ignorer les incidents réels.** Ils constituent la seule donnée du dossier qui indique ce qui se passe réellement — et ils contredisent la cartographie.

## 18.8 🔴 FIL ROUGE — juin 2030 : excellents là où c'était facile

Nour et le référent détection conduisent le premier exercice de cartographie de couverture d'HELIOMED, en réponse au besoin B-05 (*ce que je ne détecte pas*).

**Le résultat brut** : 41 % de couverture déclarée. Le référent détection est satisfait — le chiffre est supérieur à ce qu'il attendait.

**Le croisement que Nour ajoute**, en une demi-journée : pour chaque règle, la source de journaux dont elle dépend.

| Source | Règles | Part |
|---|---|---|
| Poste de travail | 61 | **68 %** |
| Pare-feu | 14 | 16 % |
| Annuaire | 9 | 10 % |
| Applicatif métier | 5 | 6 % |
| **Systèmes industriels (Saint-Étienne)** | **0** | **0 %** |

**Le second croisement**, avec les quatre besoins actifs de la fonction : les techniques couvertes correspondent-elles aux menaces identifiées comme pertinentes pour HELIOMED ?

| Menace pertinente identifiée | Couverture |
|---|---|
| Compromission d'un prestataire d'infogérance *(épisode de septembre 2029)* | **Partielle** — 2 règles, aucune testée |
| Exploitation d'identifiants issus de fuites *(épisode de mai 2030)* | **Aucune** au moment de l'exercice |
| Atteinte à la plateforme de télésuivi via les serveurs applicatifs | Partielle |
| Activité sur le réseau industriel | **Aucune source de journaux** |

**Ce que l'exercice établit** : HELIOMED détecte bien ce qui se passe sur les postes de travail — parce que c'est là que les journaux existent — et ne détecte rien de ce qui correspond aux deux incidents réellement survenus en dix-huit mois.

**La réaction du référent détection**, qu'il faut noter parce qu'elle est saine :

> *« Je savais que je manquais de sources. Je ne savais pas que mes 41 % ne couvraient rien de ce qui nous est arrivé. »*

**Les trois décisions**, priorisées par source plutôt que par technique :

| # | Action | Effet attendu |
|---|---|---|
| 1 | Collecte des journaux d'annuaire complets — la source manquait, pas la volonté | Débloque trois tactiques |
| 2 | Test des 89 règles existantes, par lots de dix | Établir la couverture réelle |
| 3 | Écoute passive sur le réseau industriel — projet, échéance 2031 | Couvre une zone entièrement aveugle |

**Le résultat du point 2, trois mois plus tard** : sur 89 règles testées, **17 ne déclenchent pas** — sources modifiées, champs renommés, seuils devenus inopérants. La couverture réelle était de 33 %, pas 41 %.

**Ce que Claire porte au comité** : le chiffre a **baissé** de 41 à 33 %, et c'est un progrès. C'est la première fois qu'il est vrai.

> *« Nous avons perdu huit points et gagné la possibilité de décider »*, écrit-elle au compte rendu.

**Livrable de l'épisode.** La cartographie d'HELIOMED avec ses quatre attributs par case (§18.6), et la règle du test obligatoire avant déclaration de couverture.

→ La suite en 🔴 §19.5, quand plusieurs signalements isolés se révéleront être une seule campagne.

## Synthèse mentale du chapitre 18

Un modèle apporte un langage partagé, la comparabilité, la mesurabilité et la visibilité des manques — et rien d'autre : c'est une grille de description, jamais d'évaluation. Un référentiel décrit le passé observé, donc ce qui n'y figure pas n'est pas inexistant, seulement non documenté. Trois modèles coexistent sans se concurrencer : la chaîne pour expliquer, le diamant pour relier, le référentiel pour mesurer. La pyramide de la difficulté explique qu'un jeu de cent indicateurs techniques vaille moins qu'une description précise de trois comportements — le volume se vend parce qu'il se mesure, la valeur se situe là où le volume est faible. Une cartographie est un actif à maintenir, et sans ses quatre attributs — source de journaux, date de test, niveau réel, version du référentiel — elle produit une image rassurante et fausse. Enfin, une couverture suit presque toujours la facilité plutôt que le risque : on couvre ce qu'on voit, et on ne voit que là où les journaux existent.

**Trois questions de vérification**

1. Une cartographie affiche 33 % de couverture. Quelles trois questions posez-vous avant d'en tirer une priorité ?
2. Pourquoi une source de journaux manquante est-elle une meilleure unité de priorisation qu'une technique non couverte ?
3. Votre taux de couverture passe de 41 à 33 % après tests. Comment le présentez-vous à une direction ?

→ **Chapitre 19 — Les campagnes** : comment plusieurs signalements isolés deviennent un objet unique, et ce que cela change.

---
