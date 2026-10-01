---
title: Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

## 7.1 Deux métiers, deux temporalités

| | **L'architecte** | **Le lecteur** |
|---|---|---|
| Quand | **Avant** — au moment de décider | **Après** — sur ce qui existe |
| Son objet | Un système qui n'existe pas encore | Un système qui existe et qu'il n'a pas conçu |
| Sa contrainte | Choisir sous incertitude | Comprendre sans documentation |
| Son livrable | Une décision et ses justifications | Une compréhension, et des questions |
| Son erreur type | Optimiser une contrainte au détriment des autres | **Juger sans connaître l'histoire** |

**Ce cours forme d'abord le second, puis le premier.** L'ordre n'est pas négociable : on ne peut concevoir que ce qu'on sait lire.

## 7.2 Ce qu'un lecteur peut décider

Contrairement à une idée répandue, **lire une architecture permet de décider beaucoup**, sans être architecte.

| Décision | Ce que la lecture apporte |
|---|---|
| Où placer un dispositif de sécurité | Les points de passage réels — chapitre 44 |
| Si une vulnérabilité nous concerne | L'exposition du composant affecté |
| Ce qu'on peut isoler pendant un incident | Les dépendances — chapitre 35 |
| Ce qu'on peut arrêter pour une maintenance | Ce qui tombe avec |
| Ce qu'il faut inventorier en priorité | Les points de rupture |
| Si une demande de flux est légitime | Ce qu'elle traverse |
| Ce qu'il faut journaliser | Les points de passage |

**Sept décisions, aucune ne nécessite d'être architecte.** C'est la valeur pratique de ce cours pour la majorité de ses lecteurs.

## 7.3 Ce que ce cours ne rendra pas capable de faire

Par honnêteté, et pour que la Partie IX soit lue avec les bonnes attentes.

| Hors de portée | Pourquoi |
|---|---|
| Dimensionner une infrastructure | Exige des mesures, des essais, une expérience produit |
| Choisir entre deux produits | Dépend du contexte, des contrats, des compétences |
| Concevoir un système à forte contrainte | Haute disponibilité stricte, temps réel, très grande échelle |
| Garantir qu'une architecture fonctionnera | Seul l'essai le démontre |

**Ce que la Partie IX apporte réellement** :

> Poser les bonnes questions, proposer une architecture justifiée pour un besoin courant, énoncer ses compromis — et identifier ce qu'il reste à vérifier.

⚠️ **Le lecteur qui terminera ce cours en pensant *« je sais concevoir une architecture »* l'aura mal lu.** Celui qui le terminera en pensant *« je sais quoi demander, quoi proposer, et quoi vérifier »* en aura tiré l'essentiel.

## 7.4 Comment progresser après ce cours

| Étape | Comment |
|---|---|
| **Lire des architectures réelles** | Demander les schémas de votre organisation, et poser les questions du chapitre 36 |
| **Suivre un flux de bout en bout** | Une fois, en vrai, avec l'exploitation. C'est irremplaçable |
| **Assister à une revue d'architecture** | Écouter les arbitrages se faire |
| **Reconstituer une histoire** | Demander à quelqu'un d'ancien pourquoi un composant est là |
| **Dessiner** | Le chapitre 50 en fait un exercice |

**La deuxième ligne est celle qui fait la différence.** Suivre une requête réelle, de la frappe au clavier jusqu'à l'écriture en base, en observant chaque étape, enseigne en une journée ce qu'aucun cours ne transmet.

## 7.5 🔴 FIL ROUGE — décembre 2025 : la question d'Amélie

Le 19 décembre, Amélie rend compte à Claire Nadeau de ses deux semaines. Elle n'a rien inventorié.

**Ce qu'elle a produit** : une liste de vingt-trois questions, et une observation.

**L'observation** :

> *Le schéma qu'on m'a donné date de mars 2023, il ne mentionne pas le site de Nantes, il ne montre ni les postes, ni la zone d'administration, ni les services en ligne, ni les prestataires. Il n'est pas faux. Il a été fait pour montrer à un client que nous avons une zone démilitarisée.*

**La question qu'elle pose à Claire** :

> *« Est-ce que tu veux que je compte ce qui est sur le schéma, ou que je découvre ce qui existe ? »*

**La réponse de Claire**, qui ouvre le volume suivant :

> *« Les deux. Mais dans cet ordre-là : d'abord comprendre, ensuite compter. Sinon tu vas compter des choses dont tu ne sauras pas si elles comptent. »*

**Ce qui est décidé le 19 décembre** : Amélie consacre janvier à comprendre le système avant de l'inventorier. Sa mission d'inventaire démarre officiellement le 5 janvier 2026.

**Le 11 décembre, Sonia Weber avait demandé** : *« Bon. Combien on en a, alors ? »* — et Claire avait répondu qu'elle ne pouvait pas encore le dire.

**Le 19 décembre, la raison est claire.** Ce n'est pas un problème de comptage. C'est un problème de compréhension, puis de définition.

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> ✓ que **toute architecture est un compromis** entre six contraintes qui se contredisent — et que la sixième, l'histoire, est souvent la plus puissante ;
> ✓ distinguer **trois familles de flux** — métier, dépendance, exploitation — et savoir que la confusion entre les deux dernières fait surdimensionner ce qui n'en a pas besoin ;
> ✓ poser les **quatre questions du lecteur** devant n'importe quel schéma ;
> ✓ que **trois mots** — serveur, application, service — désignent chacun au moins trois choses, et quelle question les désambiguïse ;
> ✓ qu'une **boîte** peut représenter cinq choses et un **trait** cinq autres, et quelles questions poser à chacun ;
> ✓ que quatre **vues** sont nécessaires, et qu'aucune ne ment ;
> ✓ **onze éléments qui ne sont jamais dessinés**, et l'effet de leur absence ;
> ✓ qu'une architecture est un **empilement daté**, et que chaque anomalie a une histoire qu'il faut demander avant de critiquer ;
> ✓ que la **taille ne justifie jamais une brique** — la contrainte, oui ;
> ✓ qu'une **zone** se définit par ce qu'il faut traverser, pas par un trait ;
> ✓ que le **poste utilisateur** est le point de départ de la plupart des flux et le grand absent des schémas ;
> ✓ qu'un schéma est toujours **fait pour quelqu'un**, et qu'il faut savoir pour qui avant de le lire.
>
> **Ce que vous ne savez pas encore** : à quoi servent les composants que vous avez appris à repérer, ce qui se passe quand ils disparaissent, et à partir de quelle contrainte ils deviennent nécessaires. C'est l'objet de la Partie II.

---
