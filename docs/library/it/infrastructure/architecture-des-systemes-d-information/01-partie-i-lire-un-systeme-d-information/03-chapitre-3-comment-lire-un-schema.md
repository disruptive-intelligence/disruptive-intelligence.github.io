---
title: Chapitre 3 — Comment lire un schéma
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

> Chapitre méta, et l'un des plus utiles du cours. Personne n'enseigne à lire un schéma ; on suppose que c'est évident. Ce ne l'est pas.

## 3.1 Ce qu'une boîte représente

**Le problème** : une boîte sur un schéma peut représenter cinq choses différentes, et rien ne l'indique.

| Ce que la boîte peut être | Comment le deviner |
|---|---|
| Une **machine** physique ou virtuelle | Nom d'hôte, mention d'un système |
| Un **rôle** — « serveur web » sans dire combien | Nom générique, absence de nom d'hôte |
| Un **groupe** — trois machines dessinées en une | Mention d'un nombre, boîtes empilées |
| Un **service** — un ensemble de composants | Nom métier, positionnement isolé |
| Un **fournisseur externe** — une boîte noire | Nom commercial, position en bordure |

⚠️ **Une confusion fréquente, et coûteuse** : lire un **rôle** comme une **machine**. « Serveur web » sur un schéma ne dit pas s'il y en a un ou douze — donc ne dit pas si c'est un point de rupture.

**La question à poser devant toute boîte** : *combien y en a-t-il réellement, et que se passe-t-il si l'un tombe ?*

## 3.2 Ce qu'un trait représente

Un trait est encore plus ambigu qu'une boîte.

| Ce que le trait peut être | Fréquence |
|---|---|
| Un **câble** — une liaison physique | Sur les schémas physiques |
| Un **flux** — quelque chose circule | Sur les schémas de flux |
| Une **relation logique** — « dépend de », « appartient à » | Sur les schémas logiques |
| Une **adjacence réseau** — « peut joindre » | Fréquent, et rarement explicité |
| **Rien de précis** — le dessinateur reliait deux choses proches | **Plus fréquent qu'on ne croit** |

**Trois questions devant tout trait** :

```
1. Qui initie ? (le sens compte, et il est rarement fléché)
2. Qu'est-ce qui circule ? (quelle famille de flux)
3. Est-ce permis, ou seulement possible ?
```


⚠️ **La troisième est la plus importante en sécurité.** Un trait indique souvent une **possibilité technique**, pas une autorisation. Deux machines dans le même segment sont reliées, que ce soit voulu ou non.

## 3.3 Les quatre vues d'un même système

**Une architecture ne se représente pas d'un seul schéma.** Il en faut au moins quatre, et confondre les vues est une source d'erreur permanente.

🖼 **SCHÉMA 3.1 — Le même système, quatre vues** · *Quatre panneaux côte à côte, mêmes composants, représentations différentes.*

| Vue | Ce qu'elle montre | Ce qu'elle cache | Qui la produit |
|---|---|---|---|
| **Physique** | Machines, câbles, baies, sites | Ce qui s'exécute dessus | Infrastructure |
| **Logique** | Rôles, zones, relations | Le nombre réel de machines | Architecture |
| **Flux** | Ce qui circule, dans quel sens, sur quel protocole | La topologie physique | Sécurité, réseau |
| **Service** | Ce qui produit une valeur métier | **Presque toute la technique** | Métier, continuité |

**Exemple, sur le même objet** :

```
VUE PHYSIQUE      3 machines dans la baie B12, site de Lyon

VUE LOGIQUE       [ serveurs web ] ──► [ applicatif ] ──► [ base ]

VUE FLUX          poste ──443──► mandataire ──8080──► web
                  web ──1433──► base
                  web ──389──► annuaire        ← dépendance

VUE SERVICE       « Télésuivi HelioLink » — disponible 24/7,
                  dépend de : authentification, base, réseau Lyon
```


**Ce que la comparaison enseigne** : la vue service ne mentionne aucune machine, et la vue physique ne mentionne aucun service. **Aucune des deux ne ment ; elles répondent à deux questions différentes.**

👁 **CE QU'IL FALLAIT OBSERVER** — la vue flux est la seule qui fasse apparaître l'annuaire. C'est pour cela qu'elle est la plus utile en sécurité, et la plus rare dans les organisations.

## 3.4 Ce qui n'est jamais dessiné

**La liste la plus utile du chapitre.** Elle sera complétée au chapitre 50.

| Ce qui manque presque toujours | Pourquoi | Conséquence |
|---|---|---|
| **La résolution de noms** | Tout le monde s'y connecte, le schéma serait illisible | Sa panne paraît inexplicable |
| **L'annuaire** | Idem | On sous-estime son caractère critique |
| **La synchronisation d'horloge** | Considérée comme acquise | Une dérive produit des rejets d'authentification incompréhensibles |
| **Les chemins d'administration** | Ils ne servent pas le métier | **Ce sont souvent les plus sensibles** — chapitre 27 |
| **Les sauvegardes** | Elles ne participent pas au service nominal | On découvre en incident qu'elles passent par un chemin non protégé |
| **Les postes de travail** | Trop nombreux | **La majorité des incidents commence là** — chapitre 6 |
| **Les services en ligne** | Pas chez nous, donc pas dessinés | Chapitre 38 |
| **Les liens partenaires** | Anciens, oubliés | Chapitre 38 |
| **Les certificats et leur autorité** | Invisibles quand ça marche | Une expiration arrête un service sans prévenir |
| **Le temps** | Un schéma est instantané | On ne voit ni l'historique, ni ce qui est en cours de migration |
| **Les versions** | Ça alourdirait | On ne peut pas raisonner l'obsolescence |

🎯 **L'exercice à faire une fois dans sa carrière** : prenez le schéma de votre organisation et **dessinez au crayon les onze éléments ci-dessus**. La page devient illisible en quatre minutes. C'est exactement pour cela qu'ils ne sont pas dessinés — et c'est exactement pour cela qu'il faut savoir qu'ils existent.

## 3.5 Les conventions courantes

Elles ne sont pas normalisées, mais elles reviennent.

| Convention | Signification habituelle |
|---|---|
| Position **haute** = extérieur | Internet en haut, données en bas |
| Position **basse** = données | La base est presque toujours au fond — chapitre 20 |
| Un **nuage** | Quelque chose qu'on ne maîtrise pas ou qu'on ne détaille pas |
| Des boîtes **empilées** | Plusieurs exemplaires du même rôle |
| Un trait **pointillé** | Un flux logique, une relation, ou un lien non permanent |
| Une **double ligne** | Une redondance, ou un lien à haut débit |
| Un composant **à cheval sur deux zones** | Il traverse une frontière — **toujours un point d'attention** |

⚠️ **Aucune de ces conventions n'est garantie.** Sur un schéma inconnu, la première question est : *y a-t-il une légende ?* S'il n'y en a pas — cas majoritaire — les conventions ci-dessus sont des hypothèses à vérifier, pas des certitudes.

## 3.6 🔬 Mini-lab 2 — Un schéma à cinq boîtes

**Objectif** — Lire un schéma minimal et formuler ce qu'il ne dit pas.
**Durée** 25 min · **Difficulté** 🟢 débutant · **Prérequis** §3.1 à §3.5
**Compétences validées** — ✔ interroger une boîte ✔ interroger un trait ✔ identifier la vue employée ✔ lister l'invisible

**Le schéma** :

```
        Internet
            │
      [ pare-feu ]
            │
      [ serveur web ]
            │
      [ base de données ]
            │
      [ sauvegarde ]
```


❓ **QUE VOYEZ-VOUS ?**

1. Combien de machines ce schéma représente-t-il ?
2. Quelle vue est-ce ?
3. Que se passe-t-il si le serveur web tombe ?
4. Citez cinq choses qui manquent.
5. Le trait entre la base et la sauvegarde : qui initie ?

---

**Corrigé**

**1. On ne sait pas.** Chaque boîte peut être une machine, un rôle ou un groupe. Rien ne l'indique. **C'est la bonne réponse** — et c'est la première question à poser à l'auteur du schéma.

**2. Une vue logique**, probablement. Aucun protocole, aucune adresse, aucun site : ce n'est ni une vue physique, ni une vue de flux. Ce n'est pas non plus une vue service — aucun nom métier.

**3. On ne sait pas non plus.** S'il est unique, le service s'arrête. S'il représente un groupe, il ne se passe rien. **Le schéma ne permet pas de répondre à la question la plus importante qu'on puisse lui poser.**

**4. Ce qui manque** — au moins :

| Manquant | Effet |
|---|---|
| Résolution de noms | Sans elle, personne n'atteint le serveur |
| Authentification | Où prouve-t-on son identité ? |
| Chemins d'administration | Comment ces machines sont-elles administrées ? |
| Postes de travail | Les utilisateurs internes n'apparaissent pas |
| Protocoles et sens des flux | On ne sait pas ce qui circule |
| Journalisation, supervision | Aucun flux d'exploitation |
| Certificats | Le flux est-il chiffré ? |
| Le nombre d'exemplaires | Voir question 3 |

**5. La sauvegarde initie presque toujours.** C'est contre-intuitif au vu du sens de lecture du schéma, qui suggère un flux descendant. **Et c'est un point de sécurité majeur** : si la sauvegarde initie, elle possède un accès à la base — donc à toutes les données. Le trait ne dit rien du sens, et le sens change tout.

**Les deux erreurs attendues**

1. **Répondre « cinq machines ».** Le schéma ne le dit pas, et l'admettre est la compétence visée.
2. **Répondre « le service s'arrête » à la question 3.** C'est probable, ce n'est pas établi — et la différence entre les deux est ce que ce cours enseigne.

## 3.7 🔴 FIL ROUGE — décembre 2025 : ce que le schéma ne dit pas

Amélie applique au schéma 1.1 les questions du §3.4. Elle liste ce qui n'y figure pas, et demande à Malik de confirmer.

| Élément absent | Existe-t-il ? | Réponse de Malik |
|---|---|---|
| Résolution de noms | **Oui**, deux serveurs | *« On ne les dessine jamais »* |
| Synchronisation d'horloge | **Oui** | *« Je n'y avais jamais pensé »* |
| Chemins d'administration | **Oui** | *« On passe par le réseau d'admin, il n'est pas sur ce schéma »* |
| Postes de travail | **620** | *« Ils sont partout, ça n'aurait pas de sens de les dessiner »* |
| Services en ligne | **« Une trentaine ? »** | *« Là, je ne sais pas. Ce n'est pas moi qui les gère »* |
| Sauvegarde | Oui | *« Elle est dessinée, mais son chemin ne l'est pas »* |
| Site de Nantes | **Oui** | *« Il n'est pas sur ce schéma. C'est un oubli »* |

**Deux réponses comptent plus que les autres.**

La cinquième — *« je ne sais pas »* — désigne un périmètre entier que personne ne suit. Ce sera le point le plus coûteux du volume Asset Management.

La septième — *« c'est un oubli »* — révèle que le schéma officiel du groupe **ne mentionne pas l'un de ses trois sites**. Depuis mars 2023.

**Ce qu'Amélie note** :

> *Le schéma n'est pas faux. Il est incomplet, et personne ne sait de combien. C'est exactement le problème que je suis censée résoudre.*

→ La suite en 🔴 §4.6, quand elle comprendra pourquoi l'architecture est « bizarre ».

## Synthèse mentale du chapitre 3

Une boîte peut représenter cinq choses — machine, rôle, groupe, service ou fournisseur — et rien ne l'indique : la confusion coûteuse est de lire un rôle comme une machine, parce qu'elle empêche de savoir si c'est un point de rupture. Un trait est plus ambigu encore, et trois questions le désambiguïsent : qui initie, qu'est-ce qui circule, est-ce permis ou seulement possible. Quatre vues sont nécessaires pour représenter un système, et confondre les vues est une erreur permanente : la vue service ne mentionne aucune machine, la vue physique aucun service, et aucune ne ment. La vue de flux est la seule qui fasse apparaître les dépendances, ce qui la rend la plus utile en sécurité et la plus rare en pratique. Enfin, onze éléments ne sont presque jamais dessinés, dont la résolution de noms, l'annuaire, les chemins d'administration et les postes de travail — et si l'on tentait de les dessiner, la page deviendrait illisible en quatre minutes.

**Trois questions de vérification**

1. Un schéma porte une boîte « serveur web ». Quelles questions posez-vous avant d'en tirer une conclusion sur la disponibilité ?
2. Un trait relie une base de données à une sauvegarde. Pourquoi le sens compte-t-il, et qu'implique chaque réponse ?
3. Citez cinq éléments qui ne figurent sur aucun schéma d'architecture, et l'effet de leur absence.

---
