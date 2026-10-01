---
title: Chapitre 3 — Les trois niveaux
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE I — Fondamentaux du renseignement
  - index.md
---

## 3.1 Le schéma structurant

Le renseignement se produit à trois niveaux. Cette distinction n'est pas académique : elle détermine **le destinataire, la question, le format, la durée de vie, la méthode et l'incertitude tolérable**. La confondre est la deuxième cause d'inutilité du domaine, après l'absence de besoin exprimé.

🖼 **SCHÉMA — Les trois niveaux du CTI.** *Trois bandeaux horizontaux superposés, du stratégique en haut au tactique en bas, avec sur l'axe vertical l'horizon temporel et sur l'axe horizontal le degré d'incertitude tolérable. Faire apparaître que les deux varient en sens inverse.*

| | **Stratégique** | **Opérationnel** | **Tactique** |
|---|---|---|---|
| **Qui décide** | Direction générale, comité de direction | RSSI, responsable MCS, responsable produit | Détection, réponse à incident |
| **Question type** | Où investir ? Quels risques portons-nous à trois ans ? | Que prioriser ce trimestre ? Contre quoi nous préparer ? | Que bloquer ? Que chercher dans nos journaux ? |
| **Horizon** | 1 à 3 ans | 3 à 12 mois | 3 à 30 jours |
| **Livrable** | Évaluation, note d'orientation | Priorités, fiches de modes opératoires | Indicateurs, règles, actions |
| **Durée de vie du produit** | Années | Mois | **Jours** |
| **Conséquence d'une erreur** | Un budget mal orienté pendant des années | Un effort de remédiation mal placé | Une alerte manquée, ou du bruit |
| **Incertitude tolérable** | **Élevée** | Moyenne | **Faible** |
| **Volume produit** | 2 à 6 par an | 1 à 4 par mois | Continu |

## 3.2 Pourquoi l'incertitude tolérable varie en sens inverse de l'horizon

C'est la ligne la plus contre-intuitive du tableau, et celle qui explique le plus de malentendus. Prenons-la de face.

**Au niveau stratégique, une incertitude élevée est acceptable — et même normale.** Quand une direction décide d'investir sur trois ans dans une capacité de détection plutôt que dans la segmentation, elle ne dispose d'aucune certitude sur les menaces de 2032. Elle décide sur des tendances. Un analyste qui refuserait de se prononcer faute de preuves serait inutile à ce niveau : ce qu'on lui demande, c'est une **orientation argumentée**, assumée comme incertaine.

**Au niveau tactique, une incertitude élevée est disqualifiante.** Une règle de détection fondée sur une hypothèse fragile produit du bruit, épuise l'équipe et finit désactivée. Un indicateur bloqué à tort coupe un service légitime. Ici, on n'agit que sur ce qui est solide — quitte à ne pas agir.

**La conséquence pratique** est un renversement complet de la posture selon le destinataire :

| Niveau | Ce qu'on reproche à un analyste |
|---|---|
| Stratégique | De ne pas se prononcer |
| Tactique | De se prononcer trop vite |

**Un analyste qui n'a pas intégré cette asymétrie sera jugé mauvais aux deux niveaux** : trop prudent pour la direction, trop affirmatif pour la détection. C'est l'une des raisons pour lesquelles un même produit ne peut jamais servir les trois publics.

## 3.3 Le niveau tactique

**Ce qu'il produit** : des indicateurs techniques, des règles de détection, des actions de blocage, des requêtes de recherche rétrospective.

**Sa caractéristique dominante** : la **péremption rapide**. Une infrastructure adverse change ; une empreinte de fichier ne vaut que pour ce fichier ; un nom de domaine est abandonné. Un indicateur conservé indéfiniment devient un faux positif en puissance, et le chapitre 30 traite son cycle de vie complet.

**L'erreur classique à ce niveau** : confondre volume et valeur. Un flux de deux millions d'indicateurs n'est pas cent fois meilleur qu'un flux de vingt mille — il est surtout cent fois plus coûteux à trier. La question n'est pas *combien* mais *quelle proportion me concerne, et à quel taux d'erreur*.

⚠️ **PIÈGE — l'indicateur sans contexte**
Un indicateur livré seul — une adresse, une empreinte — ne dit ni ce qu'il représente, ni depuis quand il est valide, ni quelle confiance lui accorder, ni ce qu'il faut faire si on le voit. Il est presque inexploitable. Un indicateur utile porte au minimum : sa source, sa date de première et de dernière observation, ce à quoi il est associé, et l'action attendue.

## 3.4 Le niveau opérationnel

**Ce qu'il produit** : des fiches de modes opératoires, des évaluations de campagnes, des priorités de remédiation, des scénarios de préparation.

**C'est le niveau le plus utile et le moins produit.** Cette phrase mérite d'être expliquée, parce qu'elle décrit une anomalie durable du domaine.

| Niveau | Pourquoi il est produit ou non |
|---|---|
| Tactique | Facile à produire, automatisable, vendable au volume — **surproduit** |
| Stratégique | Visible, valorisant, demandé par les directions — **produit, souvent mal** |
| **Opérationnel** | Exige de connaître à la fois la menace **et** votre organisation — **sous-produit** |

Le niveau opérationnel est celui qui demande le plus de travail spécifique et qui s'achète le moins bien. Un fournisseur peut vous vendre des indicateurs et des tendances ; il peut difficilement vous dire quelles trois techniques d'attaque devraient orienter vos six prochains mois, parce que cela suppose de connaître votre architecture, vos angles morts et vos projets en cours.

**C'est donc là que se situe l'essentiel de la valeur ajoutée d'une fonction interne** — et c'est ce qui justifie qu'elle existe.

## 3.5 Le niveau stratégique

**Ce qu'il produit** : des évaluations de tendance, des notes d'orientation, des éléments de décision budgétaire.

**Sa difficulté propre** : il est le plus demandé et le plus mal fait. Deux dérives symétriques :

| Dérive | Manifestation | Ce que le destinataire en fait |
|---|---|---|
| **La revue de presse déguisée** | Une compilation des grandes tendances du secteur, sans lien avec l'organisation | Rien. Il l'avait déjà lue ailleurs |
| **La projection non assumée** | Des affirmations sur trois ans formulées comme des faits | Il décide sur une base plus solide qu'elle ne l'est |

**Ce qu'un bon produit stratégique contient** : peu de faits, beaucoup de raisonnement, une orientation claire, et une déclaration explicite de ce qui pourrait la faire changer. Il tient en deux pages. S'il en fait quinze, il ne sera pas lu par son destinataire — qui n'est pas un spécialiste et n'a pas le temps.

🎯 **ET MAINTENANT ?**
*Votre direction générale vous demande une note sur « la menace cyber pour notre secteur en 2030 ». Par quoi commencez-vous ?*
**Réponse** : par une question de retour, avant d'écrire une ligne. *Quelle décision cette note doit-elle éclairer ?* Selon la réponse — arbitrer un budget, choisir entre deux investissements, répondre à un actionnaire, préparer un conseil d'administration — le produit sera radicalement différent. Écrire la note sans poser cette question, c'est produire quinze pages qui finiront dans une pièce jointe non ouverte. Ce réflexe est développé au chapitre 14.

## 3.6 ⚠️ La confusion des niveaux

C'est la deuxième cause d'inutilité du domaine. Quatre situations, toutes observées en pratique.

| # | Situation | Ce que le destinataire en conclut |
|---|---|---|
| 1 | Une liste d'indicateurs techniques envoyée à un comité de direction | « Le CTI, c'est incompréhensible et ça ne me concerne pas » |
| 2 | Une tendance géopolitique envoyée à un analyste qui doit écrire une règle ce soir | « Le CTI, c'est du vent » |
| 3 | Une évaluation stratégique demandée en urgence pour une décision de blocage | Le produit arrive trop tard et ne répond pas à la question |
| 4 | Un rapport unique de vingt pages envoyé à cinq destinataires différents | Aucun ne le lit entièrement, chacun cherche sa partie et ne la trouve pas |

**Le point commun des quatre** : le producteur a raisonné en termes de **contenu** — *voici ce que je sais* — au lieu de raisonner en termes de **destinataire** — *voici ce dont vous avez besoin pour décider*.

✅ **BONNE PRATIQUE (P0) — la question préalable à toute diffusion**
Avant d'envoyer quoi que ce soit : *à quel niveau se situe mon destinataire, et quelle décision doit-il prendre ?* Si vous avez deux destinataires à deux niveaux différents, vous avez **deux produits à écrire**, pas un produit à envoyer deux fois. Le chapitre 26 en fait un exercice complet.

## 3.7 Quel niveau pour quelle organisation

Toutes les organisations n'ont pas besoin des trois niveaux, et prétendre le contraire conduit à des fonctions CTI sous-dimensionnées qui font mal les trois.

| Contexte | Niveau prioritaire | Pourquoi |
|---|---|---|
| Petite organisation, pas de centre opérationnel | **Opérationnel**, exclusivement | Le tactique suppose une capacité de détection à alimenter ; le stratégique suppose des arbitrages d'investissement qui n'existent pas à cette échelle |
| Organisation avec détection interne | Tactique + opérationnel | Le tactique alimente la détection, l'opérationnel oriente les priorités |
| Organisation régulée ou exposée | Les trois | La direction porte des obligations et arbitre des investissements |
| Éditeur ou fabricant | Opérationnel + un tactique spécifique sur ses propres produits | Ce qui vise ses produits est un sujet à part entière (chapitre 33) |

📌 **LIMITES — l'illusion de complétude**
Une fonction d'une personne qui prétend couvrir les trois niveaux produira trois choses médiocres. Le chapitre 39 traite explicitement ce cas : **choisir un niveau, l'assumer, et déclarer les deux autres non couverts** vaut infiniment mieux qu'une couverture superficielle. C'est la même logique que les périmètres déclarés non couverts du cours MCS.

## 3.8 🔴 FIL ROUGE — mai 2029 : trois publics, un seul rapport

Nour Belkacem a pris ses fonctions le 2 mai. Le 22 mai, elle produit son premier livrable : une note de onze pages sur une campagne de rançongiciel visant des établissements de santé européens depuis février.

Le travail est bon. Les sources sont vérifiées, le mode opératoire est décrit précisément, les indicateurs sont listés, une section évalue les implications pour HELIOMED.

Elle l'envoie à sept personnes. Voici ce qui se passe.

| Destinataire | Ce qu'il en fait | Pourquoi |
|---|---|---|
| Claire Nadeau (RSSI) | La lit intégralement | C'est son métier, et elle a commandé le travail |
| Malik Ferhaoui (exploitation, MCS) | Cherche la liste des vulnérabilités exploitées, la trouve page 8 | Il voulait une réponse à *que corriger en premier* |
| Yann Prigent (produit) | Cherche si HelioBox est concerné, ne trouve pas de réponse claire | La question n'était pas traitée |
| Sonia Weber (DSI) | Lit le résumé, s'arrête page 2 | Onze pages, agenda plein |
| Le référent détection | Extrait les indicateurs, se demande depuis quand ils sont valides | L'information n'y était pas |
| Dr Hélène Fabre (affaires réglementaires) | Ne l'ouvre pas | Ne comprend pas pourquoi elle l'a reçue |
| Karim Lebrun (DAF) | Ne l'ouvre pas | Idem |

**Le bilan, deux semaines plus tard** : une personne sur sept a lu le document en entier, deux en ont tiré quelque chose au prix d'une recherche, quatre l'ont ignoré. Aucune décision n'a été prise.

**Ce que Nour croit d'abord.** Que le document était trop long. C'est vrai, mais accessoire.

**Ce que Claire lui fait voir.** Le document mélangeait trois niveaux et six destinataires. Il contenait du tactique — les indicateurs, sans leur date de validité —, de l'opérationnel — les vulnérabilités à prioriser, enterrées page 8 —, et du stratégique — la tendance sectorielle, en introduction. Chaque lecteur devait traverser le contenu des autres pour trouver le sien.

> *« Ce n'est pas un rapport trop long, lui dit Claire. C'est trois rapports collés. »*

**La décision prise.** Le même travail est redécoupé en trois produits, sans une seule recherche supplémentaire :

| Produit | Destinataire | Format | Contenu |
|---|---|---|---|
| **Note d'orientation** | Direction, DSI | 1 page | La tendance sectorielle, ce qu'elle implique pour nos priorités, ce qui la ferait changer |
| **Fiche opérationnelle** | MCS, produit, RSSI | 2 pages | Le mode opératoire, les techniques employées, les trois vulnérabilités à traiter en priorité, la question HelioBox traitée explicitement |
| **Jeu d'indicateurs** | Détection | Tableau | Les indicateurs, **avec date de première et dernière observation, source, et action attendue** |

Les trois sont diffusés le 5 juin. Malik programme une campagne de correctifs dans la semaine. Yann Prigent obtient sa réponse — HelioBox n'est pas concerné, et il peut le dire à ses clients. La détection intègre onze indicateurs sur les quarante fournis, après avoir écarté ceux dont la dernière observation datait de plus de six mois.

**Ce que Nour retient**, et qu'elle notera dans son carnet : *le même travail, découpé selon les destinataires, a produit trois décisions au lieu de zéro.*

**Livrable de l'épisode.** Trois modèles de produits, un par niveau, qui deviendront le standard d'HELIOMED — ils figurent en annexe D.

→ La suite en 🔴 §4.7, quand Nour relira sa première note et y trouvera quatre affirmations qu'elle ne peut pas justifier.

## Synthèse mentale du chapitre 3

Le renseignement se produit à trois niveaux qui déterminent le destinataire, le format, la durée de vie et la méthode. L'incertitude tolérable varie en sens inverse de l'horizon : au stratégique, refuser de se prononcer faute de preuves rend inutile ; au tactique, se prononcer trop vite produit du bruit et des blocages injustifiés — un analyste qui n'a pas intégré cette asymétrie sera jugé mauvais aux deux niveaux. Le tactique se périme en jours et souffre de la confusion entre volume et valeur. L'opérationnel est le plus utile et le moins produit, parce qu'il exige de connaître à la fois la menace et votre organisation : c'est là que se situe la valeur ajoutée d'une fonction interne. Le stratégique est le plus demandé et le plus mal fait, entre revue de presse déguisée et projection non assumée. Enfin, deux destinataires à deux niveaux différents, ce sont deux produits à écrire — jamais un produit à envoyer deux fois.

**Trois questions de vérification**

1. Pourquoi une incertitude élevée est-elle acceptable dans une note stratégique et disqualifiante dans une règle de détection ?
2. Vous êtes seul, à temps partiel, dans une organisation sans capacité de détection. Quel niveau couvrez-vous, et que faites-vous des deux autres ?
3. Un rapport de vingt pages est envoyé à cinq destinataires et personne ne réagit. Quel est le diagnostic le plus probable, et qu'est-ce qui n'est probablement pas le problème ?

→ **Chapitre 4 — Les axiomes de l'analyste** : six énoncés qui paraissent évidents et qui détruisent, une fois posés, l'essentiel des mauvais raisonnements.

---
