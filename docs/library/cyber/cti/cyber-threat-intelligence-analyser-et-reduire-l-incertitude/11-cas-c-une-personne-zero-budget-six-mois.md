---
title: Cas C — Une personne, zéro budget, six mois
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - index.md
---

> **Format** — Cas de construction. Durée : **2 h**.
> **Livrables** : diagnostic · besoins formulés · plan de collecte · premier produit · mesure à six mois.
> **Prérequis** : chapitres 14, 21, 23, 29, 39, 40.

## C.1 Le dossier

**Vous êtes responsable informatique** d'une organisation de 210 personnes — un opérateur de services de santé à domicile, 4 agences régionales. Vous n'avez pas de fonction de sécurité dédiée.

**Le déclencheur** : un donneur d'ordre public a introduit en janvier une exigence nouvelle dans ses marchés — *« démontrer une capacité de suivi des menaces pertinentes pour l'activité »*. Le renouvellement du marché est en septembre.

**Ce dont vous disposez** :

```
Temps                : 3 h par semaine, prises sur votre poste actuel
Budget               : 0 € en investissement. Adhésions possibles si < 2 k€
Équipe               : vous, plus un technicien
Inventaire           : à jour pour les serveurs, partiel pour les postes
Détection            : antivirus et pare-feu, pas de centre opérationnel
Incidents 18 mois    : 2 — un rançongiciel évité (poste isolé, sauvegarde),
                       une fuite d'identifiants via un service tiers
Produits utilisés    : suite bureautique en ligne · logiciel métier
                       (éditeur unique) · outil de télégestion · VPN
Clients              : 1 donneur d'ordre public, 3 mutuelles
```


## C.2 Les questions

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous les dix premiers jours ? | Diagnostic |
| 2 | Formulez les besoins. Combien ? | Registre |
| 3 | Construisez le plan de collecte. | Matrice |
| 4 | Que refusez-vous de faire, et comment l'écrivez-vous ? | Liste de renoncements |
| 5 | Rédigez le premier produit mensuel. | Une page |
| 6 | Comment démontrez-vous la capacité en septembre ? | Dossier |
| 7 | Que mesurez-vous à six mois ? | Trois indicateurs |

## C.3 Corrigé — les dix premiers jours

**Ce qu'il ne faut pas faire** : chercher des sources, comparer des offres, ou produire une première lettre d'information.

**Ce qu'il faut faire** :

| Jour | Action | Durée |
|---|---|---|
| 1-2 | **Trois entretiens** : le directeur général, le responsable des opérations, vous-même. Deux questions : *quelles décisions vous manquent ?* et *qu'est-ce qui vous a surpris cette année ?* | 2 h |
| 3-4 | **Relire les deux incidents** des dix-huit derniers mois : vecteur, ce qui a fonctionné, ce qui n'a pas détecté | 3 h |
| 5 | Inventorier ce qui est **déjà reçu** : bulletins, avis d'éditeurs, notifications de services | 1 h |
| 6-7 | Lire l'exigence du donneur d'ordre **mot à mot** : que demande-t-elle exactement ? | 1 h |
| 8-10 | Formuler 2 à 3 besoins | 2 h |

**Ce que les entretiens produisent typiquement** :

| Interlocuteur | Réponse type | Besoin sous-jacent |
|---|---|---|
| Directeur général | *« Qu'on ne se retrouve pas à l'arrêt comme [concurrent] l'an dernier »* | Ce qui frappe les organisations comparables |
| Responsable des opérations | *« Savoir si nos logiciels ont des problèmes avant que ça casse »* | Vulnérabilités des produits utilisés |
| Vous-même | *« Savoir quoi corriger en premier »* | Priorisation |

**Ce que la relecture des incidents produit** : les deux incidents impliquaient un tiers — un service externe pour la fuite, et un poste isolé mal inventorié pour le rançongiciel. **Votre angle mort est la périphérie**, pas le cœur.

## C.4 Corrigé — les besoins

**Deux besoins, pas plus.** C'est le §39.1 : trois heures par semaine ne servent pas quatre besoins.

| Réf | Besoin | Demandeur | Décision éclairée | Niveau |
|---|---|---|---|---|
| **B-01** | *Parmi les vulnérabilités affectant nos quatre produits, lesquelles sont activement exploitées ?* | Vous | Ordre de correction | Opérationnel |
| **B-02** | *Quelles menaces atteignent des organisations comparables à la nôtre, et par quel chemin ?* | Directeur général | Investissement, préparation | Opérationnel |

**Pourquoi ces deux-là** :

- **B-01** est le plus actionnable et le moins coûteux. Il produit une décision chaque mois.
- **B-02** répond à la question du dirigeant **et** à l'exigence du donneur d'ordre. Il est le plus difficile, mais c'est celui qui est demandé.

**Ce qu'on écarte, et qu'on écrit** : le suivi d'acteurs, le renseignement stratégique, la surveillance de marque, l'infrastructure adverse.

## C.5 Corrigé — le plan de collecte

| Question | Source | Type | Fréquence | Coût | Couverte ? |
|---|---|---|---|---|---|
| B-01/1 — vulnérabilités exploitées | Catalogue d'exploitation avérée | Ouverte | 5 min/jour | 0 € | ✅ |
| B-01/2 — avis de nos 4 éditeurs | Portails éditeurs, listes de diffusion | Ouverte | 10 min/jour | 0 € | ⚠️ reçus, non exploités |
| B-01/3 — applicabilité | **Inventaire interne** | Interne | Continu | 0 € | ⚠️ partiel sur les postes |
| B-02/1 — incidents comparables | Bulletins du centre de réponse national | Ouverte | 15 min/sem | 0 € | ⚠️ non exploités |
| B-02/2 — ce qui vise notre secteur | Dispositif de partage sectoriel santé | Communautaire | 20 min/sem | Adhésion | ❌ |
| B-02/3 — ce qui est testé contre nous | **Journaux du pare-feu** | Interne | 30 min/mois | 0 € | ❌ jamais regardé |

**Le total** : environ 2 h 40 par semaine. **Une seule dépense** : l'adhésion sectorielle.

**Les deux lignes internes** — B-01/3 et B-02/3 — sont gratuites et non exploitées. La seconde, les tentatives d'exploitation bloquées par le pare-feu (§23.3), est celle qui produira le plus vite un résultat visible.

**L'action la plus urgente qui n'est pas du CTI** : compléter l'inventaire des postes. Sans lui, B-01/3 ne fonctionne pas, et l'un des deux incidents provenait précisément d'un poste mal inventorié.

## C.6 Corrigé — les renoncements écrits

> **Ce que notre dispositif ne couvre pas**
>
> **1. Le renseignement stratégique.** Nous ne produisons pas d'analyse prospective sur l'évolution des menaces. En cas de besoin, nous nous appuierons sur les publications de notre centre de réponse national et de notre dispositif sectoriel.
>
> **2. Le suivi d'acteurs.** Nous ne suivons pas d'acteurs nominativement. Nos décisions ne dépendent pas de l'identité des attaquants.
>
> **3. L'infrastructure adverse.** Nous vérifions la fraîcheur et la colocation avant tout blocage. Nous ne conduisons pas de travail d'investigation d'infrastructure.
>
> **4. La surveillance de marque et des espaces criminels.** Nous n'en avons ni le besoin exprimé, ni les moyens, ni le cadre juridique instruit.
>
> **5. La production tactique en volume.** Nous n'ingérons pas de flux d'indicateurs. Notre détection repose sur les mesures en place et sur les recherches ponctuelles.
>
> *Ces renoncements sont réexaminés annuellement.*

**Pourquoi ce document est le plus important du dossier de septembre** : il démontre qu'un choix a été fait. Un donneur d'ordre distingue immédiatement une organisation qui a arbitré d'une organisation qui n'a rien fait.

## C.7 Corrigé — le premier produit mensuel

> **Suivi des menaces — mars — page 1/1**
>
> **CE QUI NOUS CONCERNE CE MOIS-CI**
> — Une vulnérabilité activement exploitée affecte notre outil de télégestion, version installée concernée. Correctif disponible. **Application prévue le 18 mars.**
> — Deux comptes de notre domaine figurent dans une fuite publiée le 4 mars. **Mots de passe réinitialisés le 6 mars.**
>
> **CE QUE NOUS AVONS VÉRIFIÉ ET QUI NE NOUS CONCERNE PAS**
> — Une campagne visant les établissements hospitaliers exploite un logiciel de gestion que nous n'utilisons pas.
> — Trois vulnérabilités signalées sur notre suite bureautique en ligne : corrigées par l'éditeur avant notre prise de connaissance, aucune action requise.
> — Une technique d'attaque décrite dans un bulletin exploite un protocole que nous bloquons depuis 2029.
>
> **CE QUE NOUS SURVEILLONS**
> — Une campagne visant les prestataires de santé à domicile, signalée par notre dispositif sectoriel. Vecteur non communiqué. **Nous avons posé la question.** Si le vecteur concerne notre outil de télégestion, nous vous en informerons sous 24 h.
>
> **CE QUE NOUS NE SAVONS PAS**
> — Notre inventaire des postes est incomplet (environ 30 non référencés). Nous ne pouvons pas garantir que les correctifs les couvrent.
>
> **CE QUE NOUS DEMANDONS**
> — Une décision sur la complétion de l'inventaire des postes : 3 jours de travail du technicien, à arbitrer.

**Ce que cette page démontre**, et c'est ce qui compte pour le donneur d'ordre : deux actions engagées, trois vérifications documentées, une surveillance avec critère, une lacune assumée, et une demande de décision.

## C.8 Corrigé — démontrer la capacité en septembre

**Le dossier**, six pièces :

| # | Pièce | Ce qu'elle démontre |
|---|---|---|
| 1 | **Le registre des besoins** — 2 besoins, demandeurs, décisions éclairées | Une capacité orientée, pas une veille |
| 2 | **Le plan de collecte** avec la colonne « couverte » | Un choix de sources argumenté |
| 3 | **Les renoncements écrits** | Un arbitrage assumé |
| 4 | **Les six produits mensuels** | Une production régulière et datée |
| 5 | **Le registre des décisions** — ce qui a été fait grâce à quoi | **La preuve d'utilité** |
| 6 | La preuve d'adhésion sectorielle | Une insertion dans un dispositif reconnu |

**Ce qui fera la différence** : les pièces 3 et 5. La première parce qu'elle montre un arbitrage, la seconde parce qu'elle montre un effet.

⚠️ **Ce qu'il ne faut pas mettre dans le dossier** : le nombre de bulletins lus, le nombre de sources suivies, une description des outils. Aucun ne démontre une capacité.

## C.9 Corrigé — la mesure à six mois

**Trois indicateurs, pas davantage** :

| Indicateur | Valeur attendue à 6 mois | Ce qu'il mesure |
|---|---|---|
| **Décisions documentées** | 4 à 8 | L'impact — le seul qui compte |
| **Menaces vérifiées et écartées** | 15 à 30 | Que le travail a lieu, et ce contre quoi on est protégé |
| **Temps réellement consacré** | ≈ 2 h 30/semaine | Que le dispositif est soutenable |

**Le troisième est souvent omis, et il est décisif dans une petite structure** : un dispositif qui consomme cinq heures par semaine au lieu de trois sera abandonné en un an. Le mesurer permet de le corriger avant l'abandon.

## C.10 Ce que le cas enseigne

| Enseignement | Développement |
|---|---|
| **Deux besoins suffisent** | Et deux besoins servis valent mieux que six besoins effleurés |
| **La majorité des sources est déjà là** | Quatre lignes sur six du plan de collecte sont gratuites ou internes |
| **L'action la plus urgente n'est pas du CTI** | L'inventaire des postes conditionne tout — c'est le §40.1, question 5 |
| **Les renoncements écrits sont un livrable** | Ils démontrent un arbitrage à un donneur d'ordre |
| **La section « ce qui ne nous concerne pas » est la plus lue** | Elle répond à l'inquiétude, et elle prouve le travail |

**Le barème** :

| Critère | Pts |
|---|---|
| Commencer par les entretiens, pas par les sources | 15 |
| Deux besoins seulement, justifiés | 15 |
| Identifier les deux sources internes gratuites | 15 |
| Relever que l'inventaire conditionne tout | 15 |
| Renoncements écrits, avec motifs | 15 |
| Produit mensuel avec les cinq sections | 15 |
| Trois indicateurs dont le temps consommé | 10 |

**Élimination** : proposer une souscription commerciale, ou plus de trois besoins.

---
