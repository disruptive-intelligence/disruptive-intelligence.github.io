---
title: Chapitre 25 — Écrire pour être lu
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE VI — Produire et diffuser
  - index.md
---

## 25.1 La règle : conclusion d'abord

**Le principe** : votre destinataire lit dans un contexte de rareté d'attention. Il donnera à votre produit entre trente secondes et deux minutes avant de décider s'il continue.

**Ce que cela impose** : la conclusion en premier, la preuve ensuite.

| Structure académique | Structure de renseignement |
|---|---|
| Contexte → méthode → éléments → analyse → conclusion | **Conclusion → ce qui la fonde → détail** |
| Le lecteur doit tout lire pour savoir | Le lecteur sait après une phrase |
| Adaptée à un pair qui évalue le raisonnement | Adaptée à un décideur qui doit agir |

⚠️ **PIÈGE — le suspense**
Réserver la conclusion pour la fin est un réflexe scolaire profondément ancré. Il produit des documents où l'information la plus importante est à la page huit, et il est la première cause de non-lecture.

🧪 **EN PRATIQUE — la première phrase**

Elle contient quatre éléments, et rien d'autre :

```
[Nous estimons] [mot de probabilité] [l'affirmation] — [confiance], [en une ligne pourquoi]
```


> *Nous estimons **probable** que la vulnérabilité signalée le 11 juillet soit exploitée contre trois de nos clients — **confiance élevée**, fondée sur la correspondance exacte des versions et sur la cohérence des symptômes observés.*

Un lecteur qui s'arrête là a l'essentiel. C'est l'objectif.

## 25.2 La structure d'un produit

Reprise du §11.7, avec l'ordre de lecture en tête.

| Rang | Section | Qui la lit |
|---|---|---|
| 1 | **La conclusion**, en une phrase calibrée | Tout le monde |
| 2 | **Ce que cela implique** — 3 à 5 lignes | Tout le monde |
| 3 | **Ce que nous observons** | Ceux qui doivent vérifier |
| 4 | **Ce que nous en estimons** — le raisonnement | Ceux qui doivent contester |
| 5 | **Ce qui invaliderait** | Les rigoureux, et vous dans six mois |
| 6 | **Recommandations**, section séparée, avec coûts | Le décideur |
| 7 | Détail technique, indicateurs, annexes | Les opérationnels |

**Le rang 2 est celui qu'on oublie**, et c'est celui qui produit les décisions. Une conclusion sans implication laisse le lecteur devant un fait dont il ne sait que faire.

## 25.3 Séparer fait, évaluation et recommandation

Le §4.1 et le §11.5 ont posé le principe. Voici la mise en œuvre typographique, qui est ce qui le rend effectif.

**Trois sections, avec trois titres explicites** :

```
CE QUE NOUS OBSERVONS
    — uniquement des faits, avec source et date
    — aucun verbe d'intention

CE QUE NOUS EN ESTIMONS
    — hypothèses envisagées, ce qui les départage
    — conclusion calibrée
    — ce qui l'invaliderait

CE QUE NOUS RECOMMANDONS
    — actions, avec ordre de grandeur de coût
    — la décision appartient au destinataire
```


**Pourquoi la typographie compte** : un lecteur pressé lit les titres. Si vos titres sont « Contexte », « Analyse », « Conclusion », il ne sait pas où trouver ce dont il a besoin. S'ils sont ceux ci-dessus, il va directement à la section qui le concerne.

✅ **BONNE PRATIQUE (P0)** — Ces trois titres, tels quels, sur tous vos produits. Ils imposent la discipline à l'auteur autant qu'ils orientent le lecteur : il devient très difficile d'écrire un verbe d'intention sous un titre qui dit « ce que nous observons ».

## 25.4 ⚠️ Les défauts qui font qu'un produit n'est pas lu

Par fréquence décroissante, tous observés.

| Défaut | Effet |
|---|---|
| **La conclusion n'est pas en tête** | Le lecteur abandonne avant |
| **La longueur** | Au-delà de deux pages, le taux de lecture intégrale s'effondre |
| **Le jargon non défini** | Chaque terme opaque est une occasion d'abandonner |
| **L'absence d'implication** | Le lecteur ne sait pas ce qu'on attend de lui |
| **Le mélange des niveaux** | §3.6 — chacun cherche sa partie et ne la trouve pas |
| **Le ton alarmiste** | Fonctionne une fois, décrédibilise ensuite |
| **L'absence de date de validité** | §4.4 |
| **Les précautions en cascade** | Le lecteur ne sait plus ce qui est affirmé |

**Le deuxième mérite un chiffre** : dans les organisations où le taux de lecture est mesuré, la lecture intégrale décroche nettement au-delà de deux pages pour un produit non sollicité. Un rapport de onze pages a une audience réelle proche de zéro — c'est le §3.8 du fil rouge.

## 25.5 Longueur, format, canal

| Produit | Longueur cible | Canal |
|---|---|---|
| **Alerte** | 5 à 10 lignes | Le canal le plus rapide disponible |
| **Réponse à une question** | 3 à 15 lignes | Le canal de la question |
| **Fiche opérationnelle** | 1 à 2 pages | Document, avec résumé en corps de message |
| **Note d'orientation** | **1 page**, 2 au maximum | Document, présenté oralement si possible |
| **Jeu d'indicateurs** | Tableau | Format structuré, machine à machine |
| **Dossier de campagne** | Sans limite | Référence, consultée à la demande |

**La règle du corps de message** : ce qui est en pièce jointe n'est pas lu. Le message qui accompagne un produit doit contenir la conclusion et l'implication — la pièce jointe sert à ceux qui veulent vérifier.

🎯 **ET MAINTENANT ?**
*Vous avez produit une analyse de six pages, bien construite, sur une campagne visant votre secteur. Comment la diffusez-vous ?*
**Réponse** : vous ne la diffusez pas telle quelle. Vous écrivez un message de huit lignes contenant la conclusion calibrée, les trois implications, et une phrase — *« le détail et les sources sont en pièce jointe »*. Six pages ne seront lues par personne ; huit lignes le seront par tout le monde. Et si vous avez trois destinataires à des niveaux différents, vous écrivez trois messages de huit lignes, pas un message de six pages.

## 25.6 🔴 FIL ROUGE — juin 2029 : le bon rapport que personne ne lit

*Cet épisode a été présenté au §3.8 sous l'angle des niveaux. Le voici sous l'angle de l'écriture — et ce sont deux problèmes distincts, souvent confondus.*

La note du 22 mai fait onze pages. Elle est bien documentée, correctement raisonnée, et sa section d'implications est page 9.

**Ce que Nour croit d'abord** : elle est trop longue.

**Ce que Claire lui montre**, en lui faisant relire la première page :

> *« La campagne dite [X] a été observée pour la première fois en février 2029 par plusieurs éditeurs. Elle vise principalement des établissements de santé européens. Le mode opératoire décrit comprend un accès initial par courriel, suivi d'une phase de reconnaissance… »*

**Le diagnostic** : ce n'est pas trop long, c'est **mal ordonné**. Aucune des trois premières phrases ne dit ce que le lecteur doit faire. La conclusion — *nous ne sommes probablement pas concernés, pour trois raisons* — est page 9.

**La réécriture, à contenu identique** :

> *Nous estimons **peu probable** qu'HELIOMED soit concernée par la campagne [X] — **confiance moyenne**.*
>
> *Le vecteur d'entrée décrit exploite un progiciel de gestion que nous n'utilisons pas. Les deux victimes documentées sont des distributeurs, non des fabricants. Aucun élément ne suggère un ciblage des fabricants.*
>
> *Ce que cela implique : aucune action immédiate. Nous recommandons de surveiller deux indicateurs de changement, listés page 2.*
>
> *Le détail, les sources et les indicateurs figurent ci-après.*

**Quatre-vingt-dix mots.** Le reste du document est inchangé.

**L'effet** : sur les sept destinataires, six lisent les quatre-vingt-dix mots. Deux ouvrent le détail.

**Ce que Nour retient**, et qui est différent de ce qu'elle avait compris au §3.8 :

> *Le problème du découpage et le problème de l'ordre sont deux problèmes. J'avais réglé le premier en faisant trois produits. Le second, c'est que dans chacun des trois, je commençais toujours par le contexte.*

**Livrable de l'épisode.** Le modèle de première phrase en quatre éléments, et la règle des trois titres explicites — annexe D.

→ La suite en 🔴 §26.7, quand un même événement produira cinq bulletins différents.

## Synthèse mentale du chapitre 25

Votre destinataire accorde entre trente secondes et deux minutes avant de décider s'il continue : la conclusion vient donc en premier, et la structure de renseignement est l'inverse de la structure académique. La première phrase contient quatre éléments — verbe d'estimation, probabilité, affirmation, confiance justifiée — et un lecteur qui s'arrête là a l'essentiel. La section qu'on oublie est la deuxième, *ce que cela implique* : une conclusion sans implication laisse le lecteur devant un fait dont il ne sait que faire. Trois titres explicites — ce que nous observons, ce que nous en estimons, ce que nous recommandons — orientent le lecteur et disciplinent l'auteur, parce qu'il devient difficile d'écrire un verbe d'intention sous un titre qui annonce des observations. Enfin, ce qui est en pièce jointe n'est pas lu : le corps du message porte la conclusion et l'implication.

**Trois questions de vérification**

1. Vous avez produit six pages solides. Comment les diffusez-vous, et pourquoi la longueur n'est-elle pas le problème principal ?
2. Écrivez une première phrase de produit contenant les quatre éléments requis.
3. Pourquoi les titres « Contexte, Analyse, Conclusion » desservent-ils un produit de renseignement ?

---
