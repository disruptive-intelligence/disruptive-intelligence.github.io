---
title: Chapitre 7 — Ce que fait un architecte, ce que fait un lecteur
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

#### 7.1 Deux métiers, deux temporalités

| | **L'architecte** | **Le lecteur** |
|---|---|---|
| Quand | **Avant** — au moment de décider | **Après** — sur ce qui existe |
| Son objet | Un système qui n'existe pas encore | Un système qui existe et qu'il n'a pas conçu |
| Sa contrainte | Choisir sous incertitude | Comprendre sans documentation |
| Son livrable | Une décision et ses justifications | Une compréhension, et des questions |
| Son erreur type | Optimiser une contrainte au détriment des autres | **Juger sans connaître l'histoire** |

**Ce cours forme d'abord le second, puis le premier.** L'ordre n'est pas négociable : on ne peut concevoir que ce qu'on sait lire.

#### 7.2 Ce qu'un lecteur peut décider

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

#### 7.3 Ce que ce cours ne rendra pas capable de faire

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

#### 7.4 Comment progresser après ce cours

| Étape | Comment |
|---|---|
| **Lire des architectures réelles** | Demander les schémas de votre organisation, et poser les questions du chapitre 36 |
| **Suivre un flux de bout en bout** | Une fois, en vrai, avec l'exploitation. C'est irremplaçable |
| **Assister à une revue d'architecture** | Écouter les arbitrages se faire |
| **Reconstituer une histoire** | Demander à quelqu'un d'ancien pourquoi un composant est là |
| **Dessiner** | Le chapitre 50 en fait un exercice |

**La deuxième ligne est celle qui fait la différence.** Suivre une requête réelle, de la frappe au clavier jusqu'à l'écriture en base, en observant chaque étape, enseigne en une journée ce qu'aucun cours ne transmet.

#### 7.5 🔴 FIL ROUGE — décembre 2025 : la question d'Amélie

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


## Registre de cohérence — fin de T1 (chapitres 1 à 7)


### Règles verrouillées, et leur application

| Règle | Application en T1 |
|---|---|
| **principe des trois flux — trois familles de flux** | Introduite §1.5, tableau des protocoles §2.4, appliquée §6.4 |
| **R2 — la taille ne justifie pas** | Énoncée §1.6 avec trois formulations interdites, appliquée §4.3 et §6.3 |
| **R3 — profondeur limitée** | §2.2 : liste des notions volontairement exclues |
| **R4 — coût d'une brique** | Principe 9, appliqué §5.1 sur la segmentation |
| **R5 — le schéma porte l'information** | 7 schémas ASCII en 7 chapitres, ratio texte/représentation tenu |


### Termes arrêtés

| Terme retenu | Écarté |
|---|---|
| **Flux métier / de dépendance / d'exploitation** | « flux de contrôle » (trop large — voir principe des trois flux) |
| **Mandataire inverse** / **mandataire sortant** | « proxy » seul (ambigu) |
| **Point de rupture** | « SPOF » (sigle, une seule mention) |
| **Zone démilitarisée** | — (terme conservé, avec réserve §5.2) |
| **Résolution de noms** | « DNS » (cité, non employé comme terme du cours) |
| **Poste d'administration** | « bastion » (terme du terrain) |
| **Sédimentation** | « dette technique » (notion voisine, plus étroite) |


### Renvois émis vers des chapitres non rédigés

§1.1→50 · §1.3→43-45 · §1.5→29-35 · §2.1→35 · §2.3→12, 14, 25, 27 · §3.4→6, 27, 38, 50 · §4.5→volume MCS · §5.2→10, 27, 28 · §6.3→38 · §7.2→35, 44


### État du fil rouge

| Élément | Valeur figée |
|---|---|
| Épisodes | §1.8 (15/12/2025) · §2.6 · §3.7 · §4.6 · §5.5 · §6.6 · §7.5 (19/12/2025) |
| Personnages | Amélie Roux (administratrice système, Nantes, 4 ans d'ancienneté) · Claire Nadeau (RSSI) · Malik Ferhaoui (exploitation) · Sonia Weber (DSI) |
| Chiffres figés | 96 / 71 / 118 serveurs · 620 postes dont 180 nomades · schéma daté de mars 2023 · 3 sites · lien bureautique-industriel créé en 2018 · serveur `HERMES` de 2011 · second exemplaire applicatif refusé en 2021 pour cause de licence · 23 questions produites |
| Dates figées | 15/12/2025 proposition · 19/12/2025 point avec Claire · 05/01/2026 démarrage officiel |
| Raccordement | §7.5 se raccorde au §1.10 du volume Asset Management (réunion du 11/12/2025 et démarrage du 05/01/2026) |
| Prochain épisode | Partie II — les composants, un par un |


### Écarts au plan validé

**Aucun écart de structure.** Deux précisions :

1. **Le mini-lab 1 a été placé au chapitre 2** plutôt qu'au chapitre 3, parce que l'ambiguïté de vocabulaire se travaille avant la lecture de schéma. Le lab 2 est au chapitre 3, le lab 3 au chapitre 6. La numérotation des quinze labs reste conforme.
2. **Le §5.5 introduit un principe de lecture non prévu** — *un schéma est fait pour quelqu'un* — qui prolonge le chapitre 3 et annonce le chapitre 50. À réutiliser en Partie VI.

---
