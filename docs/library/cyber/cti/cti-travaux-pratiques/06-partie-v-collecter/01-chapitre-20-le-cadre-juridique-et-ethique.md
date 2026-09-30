---
title: Chapitre 20 — Le cadre juridique et éthique
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE V — Collecter
  - index.md
---

> ⏱ **Chapitre partiellement périssable.** Les principes durables sont au §20.1, §20.2 et §20.7. Les éléments datés figurent au §20.4, en bloc identifié. Ce chapitre ne remplace pas un avis juridique : il vous apprend **quelles questions poser, et à qui**.

## 20.1 Ce qui distingue une collecte licite d'une collecte problématique

**Le principe fondateur**, et il vaut dans toutes les juridictions :

> **Consulter ce qui est publiquement accessible n'est pas la même chose qu'accéder à ce qui ne vous est pas destiné.** La frontière n'est pas technique, elle est juridique — et le fait qu'un accès soit techniquement possible ne le rend pas licite.

**Les quatre questions à poser à toute activité de collecte** :

| # | Question | Ce qu'elle détermine |
|---|---|---|
| **1** | L'information est-elle **publiquement accessible**, sans contournement ni identification ? | La licéité de l'accès |
| **2** | Contient-elle des **données à caractère personnel** ? | Le régime applicable à leur traitement |
| **3** | Ai-je une **base légitime** pour la traiter et la conserver ? | La conformité du traitement |
| **4** | Puis-je **documenter** comment je l'ai obtenue ? | La défendabilité, en cas de contestation |

**La quatrième est celle qu'on néglige.** Une information dont vous ne pouvez pas expliquer l'origine est inutilisable dans un dossier, dans un partage, et devant un régulateur.

⚠️ **PIÈGE — la confusion entre accessible et public**
Un document accessible parce qu'un serveur est mal configuré n'est pas un document public. Un espace nécessitant une inscription, même gratuite, n'est pas un espace public. Un forum accessible via un lien non listé n'est pas un espace public. **Le critère n'est pas la difficulté d'accès, c'est l'intention de mise à disposition.**

## 20.2 Sources ouvertes et données à caractère personnel

C'est le sujet le plus mal traité du domaine, et il concerne toutes les organisations.

**Le fait structurant** : une grande partie du renseignement en sources ouvertes porte sur des **personnes physiques** — auteurs de publications, participants à des forums, titulaires de comptes, personnes mentionnées dans des fuites. Ces données restent soumises au régime de protection des données personnelles, **y compris lorsqu'elles sont publiquement accessibles**.

**Les cinq obligations qui s'appliquent en pratique** :

| Obligation | Ce qu'elle implique concrètement |
|---|---|
| **Finalité déterminée** | Écrire pourquoi vous collectez, avant de collecter |
| **Minimisation** | Ne conserver que ce qui sert la finalité — pas « au cas où » |
| **Durée limitée** | Une durée de conservation définie, et appliquée |
| **Information des personnes** | Avec des exceptions à instruire, pas à supposer |
| **Sécurité** | Un référentiel de renseignement est lui-même un actif sensible |

✅ **BONNE PRATIQUE (P0) — associer le délégué à la protection des données dès le début**
Pas au moment du contrôle, pas quand un problème survient : **au moment de construire le plan de collecte**. Trois raisons : il connaît les bases légales mobilisables, il sait ce qui a déjà été déclaré dans l'organisation, et son avis écrit vous protège. Une fonction CTI qui découvre le sujet après dix-huit mois de collecte se retrouve à devoir purger, ce qui est bien plus coûteux que de cadrer au départ.

**Le cas particulier des fuites de données** : disposer d'un jeu de données divulguées contenant des informations personnelles est un traitement, avec toutes ses obligations. Beaucoup d'organisations le font sans l'avoir instruit. La question à poser : *pour quelle finalité, pendant combien de temps, et qui y a accès ?*

## 20.3 Accéder à des espaces criminels : ce qui est possible, pour qui

**La question revient systématiquement**, et la réponse honnête est nuancée.

| Activité | Pour une organisation ordinaire | Remarque |
|---|---|---|
| Consulter un espace accessible sans inscription | **Possible**, avec précautions techniques | Documenter l'accès |
| S'inscrire sous une identité fictive | **À instruire juridiquement** | Peut constituer une intrusion selon la juridiction |
| Interagir, poser des questions | **Fortement déconseillé** | Sort de la collecte passive |
| Acheter des données ou un accès | **Non** | Financement d'activité criminelle, recel |
| Négocier avec un acteur | **Non** — sauf cadre spécifique de gestion de crise | Relève d'autres métiers |

**Ce qui est réellement accessible sans y aller** : une part importante de ce qui circule dans ces espaces est reprise, analysée et publiée par des chercheurs, des éditeurs et des dispositifs sectoriels. **Le rendement de la collecte directe est faible pour une organisation ordinaire**, et le risque juridique et opérationnel est réel.

📌 **La recommandation de ce cours** : sauf besoin explicitement formulé, périmètre borné et avis juridique écrit, une organisation ordinaire n'a pas à conduire cette collecte elle-même. Elle peut la consommer via des tiers dont c'est le métier.

## 20.4 ⏱ Les régimes de partage

*Bloc daté, vérifié le 2 août 2026. Le principe du §20.5 lui survit.*

**Le fait structurant** : le partage d'informations sur les menaces entre organisations soulève des questions juridiques — divulgation d'informations, responsabilité, données personnelles, concurrence — et plusieurs juridictions ont créé des régimes de protection pour l'encourager.

**Ce qui est vérifié à la date de rédaction** : un régime de protection majeur, en vigueur depuis dix ans dans une juridiction de référence, a expiré fin septembre 2025, a fait l'objet de deux prolongations successives sans modification de fond, et arrive à échéance à la fin du mois de septembre 2026 — soit huit semaines après la rédaction de ce chapitre. 📎 [S-03]

**L'effet observé pendant la période de vacance** : le partage a continué, mais les organisations ont réévalué leur exposition, certaines réduisant ce qu'elles transmettaient.

**L'enseignement durable, indépendant de l'issue** :

> **Le partage de renseignement est un acte juridique autant que technique. Son cadre varie selon la juridiction, la nature de l'information et le destinataire — et ce cadre peut disparaître.**

**Les trois questions à instruire avant de partager quoi que ce soit** :

1. **Quel régime s'applique** à ce partage, dans ma juridiction et celle du destinataire ?
2. **Que puis-je transmettre** sans engager ma responsabilité ni divulguer ce qui ne doit pas l'être ?
3. **Que se passe-t-il si le cadre change** ? Ai-je une clause de réexamen ?

## 20.5 Protocoles de diffusion et permissions d'action

**Le besoin** : quand vous recevez une information, savoir ce que vous avez le droit d'en faire ; quand vous en transmettez une, le dire.

**Deux mécanismes distincts, souvent confondus** :

| Mécanisme | Répond à | Exemple de niveaux |
|---|---|---|
| **Protocole de diffusion** | *À qui puis-je le transmettre ?* | Diffusion libre · communauté · organisation · destinataire uniquement |
| **Permission d'action** | *Qu'ai-je le droit d'en faire ?* | Agir · agir en interne · analyser seulement · ne rien faire sans accord |

**Pourquoi les deux sont nécessaires** : une information peut être largement diffusable et pourtant non actionnable — parce qu'agir dessus révélerait qu'elle vous a été transmise, ou compromettrait une opération en cours.

⚠️ **PIÈGE — le marquage par défaut le plus restrictif**
Une organisation qui marque tout au niveau le plus fermé rend son renseignement inutilisable, et se coupe des échanges — la réciprocité étant la règle dans les dispositifs de partage. Le marquage se décide **par produit**, en fonction de ce qui est réellement sensible.

## 20.6 Le partage sectoriel : ce qui se partage, et pourquoi si peu

**Le constat** : les dispositifs de partage sectoriel existent, fonctionnent, et sont sous-utilisés par leurs membres. Ce n'est pas de la mauvaise volonté.

**Les cinq freins réels** :

| Frein | Mécanisme | Ce qui le lève |
|---|---|---|
| **Juridique** | Incertitude sur ce qui peut être transmis | Un cadre écrit, validé une fois (§20.4) |
| **Réputationnel** | Partager un incident revient à révéler qu'on en a eu | L'anonymisation, et l'usage établi |
| **Concurrentiel** | Les membres sont parfois concurrents | Le périmètre limité à la sécurité |
| **Capacitaire** | Partager demande du temps qu'on n'a pas | Des formats légers |
| **Asymétrie** | On reçoit plus qu'on ne donne, et on le sait | **C'est normal au début** |

**Le cinquième frein mérite d'être traité franchement** : dans tout dispositif de partage, une minorité de membres produit la majorité de la valeur. Ce n'est pas un dysfonctionnement — c'est une conséquence des différences de maturité et de moyens. Une organisation qui débute consomme davantage qu'elle ne produit, et c'est acceptable **à condition qu'elle produise quelque chose**.

**Ce qui se partage réellement, par ordre de facilité** :

```
Facile    → indicateurs techniques anonymisés
          → constats d'exploitation de vulnérabilités
          → modes opératoires observés, sans contexte victime
          → alertes sur des campagnes visant le secteur
Difficile → détails d'incidents propres
          → éléments permettant d'identifier une victime
```


## 20.7 ⚖️ Ce qu'une organisation ne doit jamais faire

Sept interdits. Ils sont brefs, et ils ne souffrent pas d'exception dans le cadre de ce cours.

| # | Interdit | Pourquoi |
|---|---|---|
| 1 | **Accéder à un système sans autorisation**, même pour observer | Infraction dans la quasi-totalité des juridictions |
| 2 | **Acheter des données volées** ou un accès | Financement d'activité criminelle, recel |
| 3 | **Conduire une action offensive**, même en riposte | Illégal, et contre-productif |
| 4 | **Usurper une identité** pour obtenir de l'information | Sort du cadre de la collecte, expose pénalement |
| 5 | **Conserver sans finalité** des données personnelles collectées | Manquement au régime de protection |
| 6 | **Transmettre en violation d'un marquage** reçu | Détruit la confiance, et engage la responsabilité |
| 7 | **Attribuer publiquement** sans base solide | §13.6 |

**Le troisième mérite un mot**, parce que la question revient : la « riposte » ou le « hack back » n'est pas une option pour une organisation privée. Elle est illégale, elle repose sur une attribution que vous ne pouvez pas établir (chapitre 13), et elle expose à une escalade que vous ne maîtrisez pas.

🎯 **ET MAINTENANT ?**
*Un collaborateur vous signale qu'il a trouvé, sur un espace criminel accessible sans inscription, un jeu de données contenant des identifiants de votre organisation. Que faites-vous ?*
**Réponse** : quatre choses, dans cet ordre. *Vous ne téléchargez pas le jeu complet* — il contient des données personnelles de tiers, et sa détention est un traitement à instruire. *Vous documentez la découverte* : date, emplacement, ce qui a été vu, par qui. *Vous saisissez le délégué à la protection des données et le juridique* avant toute exploitation. *Vous traitez le risque immédiat* sans attendre : rotation des identifiants concernés, qui ne nécessite pas de détenir la fuite — il suffit de savoir quels comptes figurent dedans. C'est exactement ce qu'HELIOMED a fait au §17.9.

## 20.8 🔴 FIL ROUGE — septembre 2029

l'obstacle est juridique, pas technique

En septembre 2029, Claire Nadeau décide de faire adhérer HELIOMED à un dispositif de partage sectoriel santé. La démarche paraît simple : un formulaire, une cotisation, un accès.

**Elle prend quatre mois.**

**Ce qui bloque, dans l'ordre où les obstacles apparaissent** :

| # | Obstacle | Qui le lève | Délai |
|---|---|---|---|
| 1 | **Que peut-on transmettre ?** La charte du dispositif engage le membre sur la réciprocité, sans préciser les limites | Le juridique, par une note interne définissant trois catégories | 6 semaines |
| 2 | **Les données personnelles.** Les indicateurs échangés peuvent contenir des adresses associables à des personnes | Léa Cassin, déléguée à la protection des données, par une analyse et une mention au registre des traitements | 5 semaines |
| 3 | **La responsabilité en cas d'erreur.** Si HELIOMED transmet une information fausse ayant conduit un membre à agir | Le juridique, par une clause de bonne foi et une mention systématique du niveau de confiance | 3 semaines |
| 4 | **Le marquage.** Qui, en interne, décide du niveau de diffusion d'un produit sortant ? | Décision de gouvernance : Nour propose, Claire valide | 2 semaines |

**Aucun obstacle n'est technique.** Nour l'écrit dans sa note de bilan : *« j'ai passé quatre mois sur un sujet où je n'ai pas ouvert un seul outil. »*

**Ce que l'obstacle n° 3 révèle**, et c'est le plus intéressant. Le juridique ne demande pas à HELIOMED de ne transmettre que des certitudes — ce qui rendrait le partage impossible. Il demande que **chaque transmission porte son niveau de confiance**, ce qui transforme une affirmation en évaluation et change la nature de la responsabilité.

Autrement dit : **la discipline de calibrage du chapitre 9, adoptée pour des raisons analytiques, se révèle être une protection juridique.** Ni Claire ni Nour ne l'avaient anticipé.

**Ce qui est décidé**, et qui tient en une page :

| Catégorie | Ce qu'on transmet | Marquage par défaut |
|---|---|---|
| **A — Indicateurs techniques** | Adresses, domaines, empreintes, sans contexte victime | Diffusion communauté |
| **B — Modes opératoires** | Techniques observées, séquences, sans identification | Diffusion communauté |
| **C — Éléments d'incident propre** | **Décision au cas par cas, par Claire** | Restreint |

Plus une règle transverse : toute transmission porte un niveau de confiance et une date.

**L'effet, mesuré à douze mois** :

| Indicateur | Valeur |
|---|---|
| Éléments transmis par HELIOMED | 34 |
| Éléments reçus et exploités | **91** |
| Rapport donné/reçu | **1 pour 2,7** |
| Alertes reçues avant publication publique | 4 |

**Le rapport de 1 pour 2,7 est présenté sans gêne au comité.** C'est le §20.6 : une organisation qui débute consomme davantage qu'elle ne produit, et c'est acceptable dès lors qu'elle produit. Les 34 transmissions d'HELIOMED sont majoritairement des indicateurs de catégorie A — peu coûteux, et suffisants pour établir la réciprocité.

**Les quatre alertes reçues avant publication publique** sont ce qui justifie l'adhésion à elles seules : quatre fois, HELIOMED a su avant que ce ne soit public. C'est le §19.3 — une information reçue à l'étape ③ vaut beaucoup plus qu'à l'étape ⑥.

**Livrable de l'épisode.** La note de trois catégories, l'inscription au registre des traitements, et la règle du niveau de confiance systématique — annexe F.

→ La suite en 🔴 §21.6, quand Nour découvrira que la moitié de ce qu'elle cherchait à acheter était déjà dans sa boîte de réception.

## Synthèse mentale du chapitre 20

Consulter ce qui est publiquement accessible n'est pas accéder à ce qui ne vous est pas destiné, et le critère n'est pas la difficulté d'accès mais l'intention de mise à disposition. Une grande partie du renseignement en sources ouvertes porte sur des personnes physiques, et le régime de protection des données s'applique y compris à ce qui est public : le délégué à la protection des données s'associe au moment de construire le plan de collecte, pas au moment du contrôle. Pour une organisation ordinaire, le rendement de la collecte directe dans les espaces criminels est faible et le risque réel — l'essentiel de ce qui y circule est repris et publié par des tiers dont c'est le métier. Le partage est un acte juridique autant que technique, son cadre varie et peut disparaître. Les dispositifs sectoriels sont sous-utilisés pour cinq raisons dont aucune n'est la mauvaise volonté, et l'asymétrie donné/reçu est normale au début — à condition de produire quelque chose. Enfin, sept interdits ne souffrent pas d'exception, dont la riposte, qui repose sur une attribution que vous ne pouvez pas établir.

**Trois questions de vérification**

1. Un serveur mal configuré expose des documents internes d'une autre organisation. Pouvez-vous les consulter ? Justifiez par le critère pertinent.
2. Pourquoi la discipline de calibrage du chapitre 9 se révèle-t-elle être une protection juridique dans un dispositif de partage ?
3. Vous recevez plus que vous ne donnez dans un dispositif sectoriel. Est-ce un problème ? À quelle condition ?

→ **Chapitre 21 — Les sources ouvertes** : ce qu'elles couvrent réellement, et pourquoi la majorité de vos besoins y trouve réponse.

---
