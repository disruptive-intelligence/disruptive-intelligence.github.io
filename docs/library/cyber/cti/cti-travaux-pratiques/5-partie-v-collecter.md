---
title: PARTIE V — Collecter
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 5
chapters: 8
---

> **Où nous sommes dans la boucle analytique** : segment ② **COLLECTE**. Nous y arrivons au chapitre 20 sur 40, et ce n'est pas un hasard — vous savez désormais ce que vous cherchez, ce que vous en ferez, et comment vous jugerez ce que vous trouverez.
>
> **L'ordre de cette partie est délibéré** : le cadre juridique d'abord, parce qu'il conditionne ce qui est possible ; les sources ouvertes ensuite, parce qu'elles couvrent la majorité des besoins ; les sources payantes après, quand on sait ce qui manque ; **le renseignement interne en quatrième**, parce que c'est la source la plus pertinente et la moins exploitée ; l'infrastructure adverse en dernier, parce que c'est la plus technique et la plus facile à mal employer.

---

## Chapitre 20 — Le cadre juridique et éthique

> ⏱ **Chapitre partiellement périssable.** Les principes durables sont au §20.1, §20.2 et §20.7. Les éléments datés figurent au §20.4, en bloc identifié. Ce chapitre ne remplace pas un avis juridique : il vous apprend **quelles questions poser, et à qui**.

### 20.1 Ce qui distingue une collecte licite d'une collecte problématique

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

### 20.2 Sources ouvertes et données à caractère personnel

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

### 20.3 Accéder à des espaces criminels : ce qui est possible, pour qui

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

### 20.4 ⏱ Les régimes de partage

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

### 20.5 Protocoles de diffusion et permissions d'action

**Le besoin** : quand vous recevez une information, savoir ce que vous avez le droit d'en faire ; quand vous en transmettez une, le dire.

**Deux mécanismes distincts, souvent confondus** :

| Mécanisme | Répond à | Exemple de niveaux |
|---|---|---|
| **Protocole de diffusion** | *À qui puis-je le transmettre ?* | Diffusion libre · communauté · organisation · destinataire uniquement |
| **Permission d'action** | *Qu'ai-je le droit d'en faire ?* | Agir · agir en interne · analyser seulement · ne rien faire sans accord |

**Pourquoi les deux sont nécessaires** : une information peut être largement diffusable et pourtant non actionnable — parce qu'agir dessus révélerait qu'elle vous a été transmise, ou compromettrait une opération en cours.

⚠️ **PIÈGE — le marquage par défaut le plus restrictif**
Une organisation qui marque tout au niveau le plus fermé rend son renseignement inutilisable, et se coupe des échanges — la réciprocité étant la règle dans les dispositifs de partage. Le marquage se décide **par produit**, en fonction de ce qui est réellement sensible.

### 20.6 Le partage sectoriel : ce qui se partage, et pourquoi si peu

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

### 20.7 ⚖️ Ce qu'une organisation ne doit jamais faire

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

### 20.8 🔴 FIL ROUGE — septembre 2029 : l'obstacle est juridique, pas technique

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

### Synthèse mentale du chapitre 20

Consulter ce qui est publiquement accessible n'est pas accéder à ce qui ne vous est pas destiné, et le critère n'est pas la difficulté d'accès mais l'intention de mise à disposition. Une grande partie du renseignement en sources ouvertes porte sur des personnes physiques, et le régime de protection des données s'applique y compris à ce qui est public : le délégué à la protection des données s'associe au moment de construire le plan de collecte, pas au moment du contrôle. Pour une organisation ordinaire, le rendement de la collecte directe dans les espaces criminels est faible et le risque réel — l'essentiel de ce qui y circule est repris et publié par des tiers dont c'est le métier. Le partage est un acte juridique autant que technique, son cadre varie et peut disparaître. Les dispositifs sectoriels sont sous-utilisés pour cinq raisons dont aucune n'est la mauvaise volonté, et l'asymétrie donné/reçu est normale au début — à condition de produire quelque chose. Enfin, sept interdits ne souffrent pas d'exception, dont la riposte, qui repose sur une attribution que vous ne pouvez pas établir.

**Trois questions de vérification**

1. Un serveur mal configuré expose des documents internes d'une autre organisation. Pouvez-vous les consulter ? Justifiez par le critère pertinent.
2. Pourquoi la discipline de calibrage du chapitre 9 se révèle-t-elle être une protection juridique dans un dispositif de partage ?
3. Vous recevez plus que vous ne donnez dans un dispositif sectoriel. Est-ce un problème ? À quelle condition ?

→ **Chapitre 21 — Les sources ouvertes** : ce qu'elles couvrent réellement, et pourquoi la majorité de vos besoins y trouve réponse.

---

## Chapitre 21 — Les sources ouvertes

### 21.1 Ce que couvrent réellement les sources ouvertes

**Le constat qui structure ce chapitre**, et qui contredit une intuition répandue :

> **Pour une organisation ordinaire, les sources ouvertes couvrent la majorité des besoins de renseignement.** Le manque n'est presque jamais un manque de sources — c'est un manque de rapprochement entre les sources et les questions (§14.4).

**Ce qu'elles couvrent bien** :

| Besoin | Couverture |
|---|---|
| Vulnérabilités affectant vos produits | **Excellente** |
| Vulnérabilités activement exploitées | **Bonne** |
| Modes opératoires documentés | **Bonne**, avec un décalage |
| Tendances sectorielles | Correcte |
| Incidents publics comparables | Correcte, mais partielle |
| Analyse technique approfondie | **Excellente** — souvent meilleure que le payant |

**Ce qu'elles ne couvrent pas** :

| Besoin | Pourquoi |
|---|---|
| Ce qui vous vise **spécifiquement** | Personne ne le publie |
| Ce qui n'est pas encore public | Par définition |
| Ce qui circule dans des espaces fermés | Sauf reprise par un tiers |
| Votre propre exposition | Elle vient de vous (chapitre 23) |

### 21.2 Les familles de sources ouvertes

| Famille | Ce qu'elle apporte | Fraîcheur | Fiabilité | Effort |
|---|---|---|---|---|
| **Autorités nationales et centres de réponse** | Alertes, avis, recommandations, contexte national | Bonne | **Élevée** | Faible |
| **Bases de vulnérabilités** | Identification, description, versions affectées | Bonne | Élevée sur le factuel | Faible |
| **Catalogues d'exploitation avérée** | Le signal le plus fort du domaine | Bonne | Élevée | Très faible |
| **Avis des éditeurs de vos produits** | **La source de vérité** sur ce qui vous affecte | Excellente | Élevée | Faible |
| **Publications de chercheurs et d'éditeurs** | Analyse technique, modes opératoires | Variable | Variable (§10.5) | Moyen |
| **Dispositifs sectoriels** | Ce qui vise votre secteur, parfois avant publication | **Excellente** | Élevée | Adhésion |
| **Communautés et réseaux professionnels** | Signaux faibles, retours d'expérience | Excellente | **Faible** | Élevé — bruit important |
| **Presse spécialisée** | Alerte rapide | Excellente | Faible (§10.5) | Faible |

**Les trois premières lignes, plus la quatrième, couvrent à elles seules le besoin de priorisation de la remédiation** — qui est, dans la plupart des organisations, le besoin le plus productif. Elles sont gratuites et demandent peu d'effort.

⚠️ **PIÈGE — les réseaux professionnels comme source principale**
Ils sont excellents pour repérer un signal faible et détestables comme source de renseignement : pas de vérification, pas de provenance, amplification des affirmations spectaculaires, et forte circularité (§10.4). Ils servent à **repérer**, jamais à **établir**.

### 21.3 Construire une veille tenable

**Le problème n'est pas de trouver des sources.** C'est de tenir dans la durée sans y consacrer trois heures par jour ni passer à côté de ce qui compte.

**Les quatre principes d'une veille tenable** :

| Principe | Application |
|---|---|
| **Le filtrage vient du plan de collecte, pas des sources** | On suit une source parce qu'elle répond à une question, pas parce qu'elle est réputée |
| **La cadence est différenciée** | Quotidienne pour trois sources, hebdomadaire pour cinq, mensuelle pour le reste |
| **Le temps est borné** | Vingt minutes le matin, pas « quand j'aurai le temps » |
| **Ce qui n'est pas traité est archivé, pas reporté** | Une file de veille en retard ne se rattrape jamais |

🧪 **EN PRATIQUE — la veille en vingt minutes**

```
5 min   Catalogue d'exploitation avérée + avis des éditeurs de vos produits C1
        → rapprochement immédiat avec l'inventaire
        → tout ce qui matche entre en file avec une priorité

7 min   Bulletins des autorités et centres de réponse
        → lecture des titres, ouverture de ce qui touche un besoin actif

5 min   Dispositif sectoriel
        → tout est lu, le volume est faible et la pertinence élevée

3 min   Le reste — publications, réseaux, presse
        → repérage uniquement, aucune lecture approfondie
```

**Ce que cette répartition traduit** : l'essentiel du temps va aux sources de **haute fiabilité et haute pertinence**, et le reste est du repérage. C'est l'inverse de ce que fait spontanément une personne qui découvre le domaine.

### 21.4 La fatigue de veille

**Un phénomène réel**, qu'il faut nommer parce qu'il détruit des fonctions CTI.

**Le mécanisme** : le volume est infini, la pertinence est faible, la gratification est différée. Au bout de quelques mois, l'analyste lit en diagonale, puis lit moins, puis ne rattrape plus — et le jour où l'information importante passe, elle passe.

**Les quatre signes** :

| Signe | Ce qu'il indique |
|---|---|
| La file de veille a plus de trois jours de retard | Le volume dépasse la capacité |
| On ne lit plus que les titres | Le filtrage a cessé d'être conscient |
| On ne se souvient pas de ce qu'on a lu hier | La lecture n'est plus reliée à un besoin |
| On ajoute des sources pour se rassurer | §14.6 |

**Les trois remèdes** :

1. **Réduire le nombre de sources**, en repartant du plan de collecte. C'est contre-intuitif et c'est le seul qui fonctionne durablement.
2. **Archiver sans culpabilité.** Ce qui n'est pas traité en trois jours ne le sera jamais : on archive, avec motif, et on passe.
3. **Relier chaque lecture à un besoin.** Une lecture sans destination est une lecture qui fatigue sans produire.

### 21.5 📌 Les limites des sources ouvertes

- **Le décalage.** Ce qui est public a été observé plus tôt, parfois de plusieurs mois. Vous travaillez toujours avec du retard (§19.3).
- **Le biais de publication.** On publie ce qui est spectaculaire, nouveau, ou commercialement intéressant. Le banal et le récurrent — qui produisent la majorité des incidents — sont sous-représentés.
- **La couverture inégale.** Certains secteurs, certaines géographies et certains types de produits sont bien couverts ; d'autres ne le sont pas du tout.
- **La circularité** (§10.4), particulièrement forte en sources ouvertes.
- **Rien sur vous.** C'est la limite fondamentale, et elle justifie le chapitre 23.

🎯 **ET MAINTENANT ?**
*Vous démarrez une fonction CTI et disposez de deux heures par semaine. Quelles sources retenez-vous ?*
**Réponse** : quatre, pas davantage. *Le catalogue d'exploitation avérée* — cinq minutes par jour, et c'est le signal le plus fort du domaine. *Les avis des éditeurs de vos trois ou quatre produits les plus critiques* — c'est la source de vérité sur ce qui vous affecte. *Les bulletins de votre centre de réponse national* — contexte, alertes, et gratuité. *Un dispositif sectoriel* si votre secteur en a un — c'est le seul qui vous dira ce qui vise vos pairs. Tout le reste attend que vous ayez du temps, et vous n'en aurez pas la première année. Cette liste couvre les besoins de priorisation et d'alerte, qui sont les deux plus productifs.

### 21.6 🔴 FIL ROUGE — juin 2029 : ce qui était déjà là

En juin 2029, Nour instruit une demande de souscription à un flux commercial. Le fournisseur propose un abonnement à 38 k€ par an, avec une couverture décrite comme complète sur le secteur de la santé.

**Avant de comparer les offres, elle applique le §14.4** : que couvre déjà ce qu'HELIOMED reçoit gratuitement ?

**Le résultat, établi en trois jours** :

| Besoin | Couvert par le payant ? | Couvert par le gratuit ? |
|---|---|---|
| Vulnérabilités exploitées sur nos produits | Oui | **Oui — catalogue public, déjà reçu** |
| Vulnérabilités visant notre secteur | Oui | **Partiellement** — dispositif sectoriel, non adhérent |
| Modes opératoires documentés | Oui | **Oui** — publications, non exploitées |
| Analyse technique approfondie | Oui | **Oui, et souvent meilleure** |
| Indicateurs techniques en volume | **Oui** | Partiellement |
| Ce qui vise HELIOMED spécifiquement | **Non** | Non |
| Mentions de nos produits | **Non** | Non |

**Le constat** : sur sept besoins, cinq sont couverts ou couvrables gratuitement. Les deux qui ne le sont pas — ce qui vise HELIOMED spécifiquement et les mentions de ses produits — **ne sont pas couverts par l'offre payante non plus**.

**Ce qui est décidé** :

| Décision | Coût |
|---|---|
| Exploiter réellement le flux gratuit déjà ingéré | 0 € |
| Adhérer au dispositif sectoriel | Cotisation annuelle modeste |
| Reporter la souscription commerciale | 0 € |
| Instruire séparément une surveillance des mentions de produits | À évaluer |

**Ce qui frappe Claire**, et qu'elle relève au comité : le flux d'indicateurs livré avec la solution de protection des postes — celui qui figurait dans l'inventaire de mars 2029 (§1.10) comme *« ingéré automatiquement, personne ne l'a jamais examiné »* — contenait, sur les six mois écoulés, **onze indicateurs correspondant à des actifs d'HELIOMED**.

Aucun n'avait produit d'alerte, parce que personne n'avait relié le flux à l'inventaire.

> *« Nous allions payer 38 000 € pour recevoir mieux ce que nous ne lisions pas », note-t-elle au compte rendu.*

**L'épilogue, dix mois plus tard.** En avril 2030, une souscription commerciale est finalement engagée — pour un besoin précis, non couvert autrement, et après un test comparatif (§22.3). Le montant est nettement inférieur à l'offre de 2029, parce que le périmètre est nettement plus étroit.

**Livrable de l'épisode.** La matrice de couverture besoin par besoin, gratuit contre payant — annexe C. Et l'exploitation effective du flux existant, qui devient le besoin B-01 opérationnel.

→ La suite en 🔴 §22.6, avec le test comparatif d'avril 2030.

### Synthèse mentale du chapitre 21

Pour une organisation ordinaire, les sources ouvertes couvrent la majorité des besoins : le manque n'est presque jamais un manque de sources, c'est un manque de rapprochement entre les sources et les questions. Quatre familles suffisent à couvrir les deux besoins les plus productifs — catalogue d'exploitation avérée, avis des éditeurs de vos produits critiques, bulletins des autorités, dispositif sectoriel — et elles sont gratuites ou peu coûteuses. Les réseaux professionnels servent à repérer, jamais à établir. Une veille tenable filtre depuis le plan de collecte, différencie ses cadences, borne son temps, et archive sans culpabilité ce qui n'a pas été traité en trois jours. La fatigue de veille détruit des fonctions CTI, et son seul remède durable est contre-intuitif : réduire le nombre de sources. Enfin, les sources ouvertes ne disent rien de vous — c'est leur limite fondamentale, et elle justifie que la source la plus pertinente soit interne.

**Trois questions de vérification**

1. Vous disposez de deux heures par semaine. Quelles quatre sources retenez-vous, et quels besoins couvrent-elles ?
2. Votre file de veille a une semaine de retard. Que faites-vous, et pourquoi ajouter du temps est la mauvaise réponse ?
3. Un flux gratuit est ingéré par votre outil depuis deux ans. Quelle vérification faites-vous avant d'envisager une souscription payante ?

---

## Chapitre 22 — Les sources fermées et payantes

### 22.1 Ce qu'un flux commercial apporte réellement

**Trois apports réels**, et il faut les nommer avant de critiquer :

| Apport | Mécanisme |
|---|---|
| **L'agrégation et la normalisation** | Vingt sources deviennent un format unique, exploitable automatiquement |
| **L'accès à des observations non publiques** | Télémétrie du fournisseur, réponse à incident, collecte dans des espaces fermés |
| **Le gain de temps** | Le tri et l'enrichissement sont faits |

**Le deuxième est le seul qui ne soit pas reproductible en interne.** L'agrégation et le gain de temps peuvent s'obtenir autrement ; l'accès à une télémétrie propriétaire, non.

**La question qui doit gouverner toute souscription** : *qu'est-ce que ce fournisseur voit que je ne peux pas voir autrement ?* Si la réponse est vague, l'offre vend de l'agrégation — utile, mais qui doit être payée à son prix.

### 22.2 Typologie des offres

| Type | Contenu | Pertinence typique |
|---|---|---|
| **Flux d'indicateurs** | Volume d'indicateurs techniques, souvent automatisés | **Variable et souvent faible** — §18.4 |
| **Rapports d'analyse** | Modes opératoires, campagnes, acteurs | Bonne, si l'analyse est de qualité |
| **Renseignement sectoriel** | Ciblé sur votre secteur | **Élevée**, quand le secteur est bien couvert |
| **Surveillance de marque et de fuites** | Mentions de votre organisation, données divulguées | **Élevée** — c'est un besoin que rien d'autre ne couvre |
| **Surveillance de surface exposée** | Ce qui est visible de vous depuis l'extérieur | Élevée, et chevauche le MCS |
| **Accès à des espaces fermés** | Ce qui circule dans des espaces criminels | Élevée si votre besoin le justifie ; §20.3 |
| **Renseignement sur mesure** | Réponse à vos questions spécifiques | Très élevée, très coûteuse |

**Les trois types dont le rapport valeur/prix est le plus favorable pour une organisation ordinaire** : surveillance de fuites et de marque · renseignement sectoriel · surveillance de surface exposée. Tous trois répondent à des besoins que les sources ouvertes ne couvrent pas.

**Le type dont le rapport est le moins favorable** : le flux d'indicateurs en volume. Il est le plus vendu et le plus facile à évaluer sur un critère fallacieux — le nombre.

### 22.3 ⚠️ Évaluer un fournisseur avant d'acheter

**La méthode**, en cinq tests. Elle demande deux à quatre semaines et un accès d'évaluation.

| # | Test | Ce qu'il mesure | Comment |
|---|---|---|---|
| **1** | **Recouvrement avec le gratuit** | Ce que vous payez et recevez déjà | Prendre 100 éléments du flux, chercher combien étaient disponibles gratuitement |
| **2** | **Pertinence** | Ce qui vous concerne réellement | Croiser avec votre inventaire : combien touchent vos produits, votre secteur ? |
| **3** | **Fraîcheur** | L'avance sur le public | Pour 20 éléments, comparer la date de publication du fournisseur et la date de publication publique |
| **4** | **Exploitabilité** | Le contexte fourni | Un indicateur sans date, source ni action attendue est inexploitable (§3.3) |
| **5** | **Taux de faux positifs** | Le coût caché | Appliquer 50 indicateurs en observation, mesurer le bruit |

**Le test 1 est celui qui élimine le plus d'offres.** Il est fréquent qu'une majorité substantielle d'un flux commercial soit constituée d'éléments disponibles publiquement — ce qui n'est pas malhonnête, l'agrégation ayant une valeur, mais qui doit être connu pour négocier.

**Le test 3 est celui qui justifie le plus une souscription.** Une avance moyenne de quelques jours sur la publication publique a une valeur réelle et mesurable (§19.3). Une avance nulle signifie que vous payez de l'agrégation.

✅ **BONNE PRATIQUE (P0) — la période d'évaluation contradictoire**
Exigez un accès d'évaluation d'au moins un mois, et conduisez les cinq tests **avant** toute négociation de prix. Un fournisseur qui refuse l'évaluation, ou qui ne fournit pas les données brutes permettant de la conduire, vous dit quelque chose sur son offre.

### 22.4 ⚠️ Le piège du volume

**Le mécanisme commercial** : le volume est le seul attribut d'un flux qui soit facile à mesurer, à comparer et à mettre en avant. Il devient donc l'argument principal — et le critère de choix de l'acheteur.

**Pourquoi c'est fallacieux**, en trois points :

| Point | Explication |
|---|---|
| Le volume mesure ce que le fournisseur collecte | Pas ce qui vous concerne |
| Un indicateur de bas de pyramide se périme en jours | Un flux de deux millions d'indicateurs contient surtout du périmé (§18.4) |
| Le coût de traitement croît avec le volume | Faux positifs, temps d'analyse, saturation des outils |

**La question à substituer** : *combien d'éléments de ce flux ont produit une action utile chez nous au cours des trois derniers mois ?* Ce chiffre est presque toujours de deux à trois ordres de grandeur inférieur au volume annoncé, et c'est lui qui mesure la valeur.

### 22.5 📌 Coût, dépendance, réversibilité

| Dimension | Ce à quoi s'attendre |
|---|---|
| **Coût affiché** | Abonnement annuel, souvent par utilisateur ou par volume |
| **Coût caché n° 1 — l'intégration** | Connecteurs, normalisation, maintenance : souvent supérieur à la licence |
| **Coût caché n° 2 — le traitement** | Le temps d'analyse du flux reçu |
| **Coût caché n° 3 — les faux positifs** | Alertes générées, temps de qualification |
| **Dépendance** | Un processus construit autour d'un fournisseur devient difficile à en séparer |
| **Réversibilité** | Les données historiques sont rarement exportables — vous perdez l'antériorité |

✅ **BONNE PRATIQUE (P1)** — Exigez contractuellement l'**export des données brutes** dans un format ouvert, et l'accès à l'historique en fin de contrat. C'est la même exigence qu'au cours MCS pour les outils de scan, et pour la même raison : sans elle, vous ne pouvez ni mesurer, ni comparer, ni changer de fournisseur.

### 22.6 ✅ Livrable — Grille d'évaluation d'un flux

| Section | Contenu |
|---|---|
| **Besoin** | Quel besoin du plan de collecte cette offre couvre-t-elle ? Réf : … |
| **Ce que le gratuit couvre déjà** | Résultat du test 1 : … % de recouvrement |
| **Pertinence** | Test 2 : … % des éléments concernent nos produits ou notre secteur |
| **Fraîcheur** | Test 3 : avance moyenne de … jours sur la publication publique |
| **Exploitabilité** | Test 4 : les éléments portent-ils date, source, contexte, action ? |
| **Bruit** | Test 5 : … faux positifs sur 50 indicateurs appliqués |
| **Coût total** | Licence + intégration + traitement estimé |
| **Réversibilité** | Export brut : oui / non · Historique en fin de contrat : oui / non |
| **Décision** | Souscrire / négocier / reporter / renoncer — avec motif écrit |

### 22.7 🔴 FIL ROUGE — avril 2030 : le test comparatif

Dix mois après avoir reporté la souscription de 2029 (§21.6), Nour dispose d'un besoin précis que rien ne couvre : **la surveillance des mentions des produits HELIOMED** — besoin B-02, exprimé par Yann Prigent dès mai 2029.

Trois fournisseurs sont mis en évaluation pendant un mois, sur les cinq tests du §22.3.

| Test | Fournisseur A | Fournisseur B | Fournisseur C |
|---|---|---|---|
| **1 — Recouvrement avec le gratuit** | 71 % | **34 %** | 88 % |
| **2 — Pertinence** | 12 % | **41 %** | 6 % |
| **3 — Fraîcheur** | +1,2 j | **+6,4 j** | 0 j |
| **4 — Exploitabilité** | Partielle | **Bonne** | Faible |
| **5 — Faux positifs sur 50** | 19 | **6** | 27 |
| **Prix annuel** | 34 k€ | **19 k€** | 41 k€ |

**Le fournisseur C est le plus cher, le plus volumineux, et le moins utile.** Son argumentaire commercial portait sur le nombre d'indicateurs — 4,2 millions contre 180 000 pour le fournisseur B. Son taux de recouvrement de 88 % avec des sources gratuites explique ce volume.

**Le fournisseur B est retenu.** Il est le moins cher, le moins volumineux, et le seul dont l'avance moyenne — 6,4 jours — a une valeur opérationnelle démontrable.

**Ce que le test 3 permet de chiffrer**, et c'est ce qui emporte la décision de Karim Lebrun :

> *Six jours d'avance sur trois signalements produits par ce fournisseur en un mois d'évaluation. Sur le cas de décembre 2029 (§11.8), six jours d'avance auraient permis de notifier les clients avant leur propre constatation — ce qui change la nature de la relation client.*

**Ce que Nour écrit dans sa note de recommandation**, et qui est repris tel quel :

> *Nous ne recommandons pas le fournisseur qui livre le plus. Nous recommandons celui qui livre le plus tôt ce qui nous concerne.*

**L'épilogue à douze mois.** Le fournisseur B est reconduit. Le rapport d'évaluation annuel montre 14 signalements exploités, dont 4 ayant produit une action produit. Coût par signalement exploité : environ 1 350 €. Nour le présente ainsi, plutôt qu'en volume — et c'est le chapitre 35.

**Livrable de l'épisode.** La grille d'évaluation à cinq tests, versée au référentiel achats d'HELIOMED — annexe D.

→ La suite en 🔴 §23.6, quand un incident interne produira plus de renseignement que douze mois de flux.

### Synthèse mentale du chapitre 22

Un flux commercial apporte trois choses — agrégation, accès à des observations non publiques, gain de temps — et seule la deuxième n'est pas reproductible en interne : la question qui gouverne toute souscription est donc *qu'est-ce que ce fournisseur voit que je ne peux pas voir autrement ?* Cinq tests s'appliquent avant d'acheter, et le premier — le recouvrement avec le gratuit — élimine le plus d'offres, tandis que le troisième — l'avance sur la publication publique — est celui qui justifie le plus une souscription. Le volume est le seul attribut facile à mesurer, ce qui en fait l'argument commercial principal et le critère de choix le plus fallacieux : la question à lui substituer est le nombre d'éléments ayant produit une action utile. Trois coûts cachés dépassent souvent la licence — intégration, traitement, faux positifs — et l'export des données brutes se négocie au contrat, sans quoi vous perdez votre antériorité en changeant de fournisseur.

**Trois questions de vérification**

1. Un fournisseur met en avant un volume de plusieurs millions d'indicateurs. Quelle question posez-vous, et pourquoi le volume n'y répond pas ?
2. Vous disposez d'un mois d'évaluation. Quel test conduisez-vous en premier, et lequel justifiera la dépense s'il est concluant ?
3. Le fournisseur le moins cher est aussi celui qui livre le moins d'éléments. Comment défendez-vous ce choix devant un directeur financier ?

---

## Chapitre 23 — Le renseignement que votre organisation produit

### 23.1 La source la plus pertinente et la moins exploitée

**Le constat qui ouvre ce chapitre** découle directement du chapitre 2 :

> **Aucun fournisseur ne peut vous vendre du renseignement, parce que le renseignement suppose de connaître votre contexte.** Ce contexte, vous êtes seul à le détenir — et il produit de l'information, en permanence, que presque personne n'exploite.

**Ce que votre organisation observe et que personne d'autre ne voit** :

| Ce que vous voyez | Ce que ça dit |
|---|---|
| Ce qui a été **tenté** contre vous | Le seul renseignement qui vous concerne à coup sûr |
| Ce qui a **échoué**, et pourquoi | Quelles mesures fonctionnent réellement |
| Ce qui a **réussi** | Vos angles morts, précisément localisés |
| Ce que vos utilisateurs **signalent** | Des signaux faibles inaccessibles autrement |
| Ce que vos **outils écartent** | Des tentatives que personne ne regarde |
| Ce que vos **partenaires** vous disent | Une vue élargie de votre chaîne |

**Pourquoi cette source est négligée**, en trois raisons :

| Raison | Mécanisme |
|---|---|
| **Elle ne ressemble pas à du renseignement** | Un ticket d'incident, un faux positif, un refus de connexion : ce sont des données d'exploitation |
| **Elle est dispersée** | Aucune n'est dans un flux ; elles sont dans des outils différents, tenus par des équipes différentes |
| **Elle demande de demander** | Il faut aller la chercher auprès de collègues, ce qui est plus coûteux qu'un abonnement |

⚠️ **PIÈGE — l'asymétrie d'attention**
Une organisation consacre volontiers 40 k€ par an à un flux externe et zéro heure par mois à exploiter ses propres incidents. Le rapport de valeur est pourtant inverse : le flux décrit le monde, l'incident décrit **vous**.

### 23.2 Les incidents, les alertes et les faux positifs

**Ce qu'un incident produit**, et qui est presque toujours perdu :

| Élément | Valeur de renseignement |
|---|---|
| Le **vecteur d'entrée** | Ce qui est ouvert chez vous, factuellement établi |
| La **séquence d'actions** | Un mode opératoire observé, de première main |
| Les **indicateurs** | Datés, contextualisés, et certainement pertinents |
| Ce qui a **arrêté** l'adversaire | La mesure qui fonctionne — information rare |
| Ce qui a **échoué à le détecter** | Un écart de couverture, précisément localisé |
| La **durée** entre entrée et détection | Un indicateur de votre capacité réelle |

**Le mécanisme de la perte** : un incident se clôt par un rapport de réponse à incident, orienté remédiation, archivé. Personne n'en extrait la partie renseignement, et six mois plus tard, plus personne ne sait ce qu'il a appris.

✅ **BONNE PRATIQUE (P0) — la fiche de renseignement post-incident**
Une page, produite systématiquement à la clôture, **par la fonction CTI et non par l'équipe de réponse**. Elle ne remplace pas le rapport d'incident : elle en extrait ce qui servira ailleurs.

**Les faux positifs sont la source la plus négligée du chapitre.** Une règle qui déclenche à tort dit quelque chose : sur votre environnement, sur ce qui y est normal, et parfois sur une activité légitime que vous ne connaissiez pas. Une revue trimestrielle des dix faux positifs les plus fréquents produit régulièrement des découvertes — des flux non documentés, des outils non déclarés, des comportements applicatifs inconnus.

### 23.3 Journaux, télémétrie, tentatives échouées

**Ce qui est écarté avant même de produire une alerte** constitue un gisement.

| Source | Ce qu'elle contient | Ce qu'on en tire |
|---|---|---|
| Authentifications échouées | Volume, origines, comptes visés | Détection de tests d'identifiants, exposition de comptes |
| Connexions refusées par filtrage | Ce qui essaie d'entrer | Balayages, ciblage, évolution dans le temps |
| Requêtes bloquées en frontal | Tentatives d'exploitation | **Quelles vulnérabilités sont testées contre vous** |
| Courriels bloqués | Thématiques, expéditeurs, pièces jointes | Campagnes visant vos collaborateurs |
| Alertes de faible sévérité | Ce qui n'est pas remonté | Signaux faibles agrégés |

**La ligne la plus utile est la troisième.** Les tentatives d'exploitation bloquées en frontal vous disent **quelles vulnérabilités des acteurs cherchent activement chez vous** — c'est-à-dire le renseignement le plus directement actionnable qui soit pour la priorisation de la remédiation (§29). Cette donnée existe dans la quasi-totalité des organisations et n'est presque jamais exploitée.

🧪 **EN PRATIQUE — l'exercice mensuel en trente minutes**

```
1. Extraire le top 20 des tentatives d'exploitation bloquées du mois
2. Croiser avec l'inventaire : ces vulnérabilités existent-elles chez nous ?
3. Croiser avec les correctifs : sont-elles corrigées ?
4. Produire trois lignes : ce qui est testé · ce qui nous concerne · ce qui reste ouvert
```

**Ce que cet exercice produit régulièrement** : la découverte qu'une vulnérabilité activement testée contre l'organisation figure encore au *backlog* de remédiation avec une priorité basse.

### 23.4 Ce que le dispositif de MCS produit

Pour le lecteur venu du cours précédent, cette section est une jonction directe. Pour les autres, elle décrit un gisement qui existe dans toute organisation dotée d'une gestion des vulnérabilités.

| Ce que le MCS produit | Ce que le CTI en fait |
|---|---|
| **L'inventaire** | Le rapprochement entre une menace et votre applicabilité (§19.4) |
| **La cartographie d'exposition** | Le deuxième critère de priorisation, que nul ne fournit |
| **Les constats ouverts** | Ce qui est vulnérable **maintenant**, à croiser avec ce qui est exploité |
| **Les dérogations** | Des risques acceptés, à réévaluer si la menace évolue |
| **Les périmètres non couverts** | Vos angles morts déclarés |

**La ligne des dérogations mérite d'être soulignée.** Une dérogation est une décision de ne pas corriger, prise sur la base d'une évaluation du risque à un instant donné. Si le CTI apprend qu'une vulnérabilité couverte par une dérogation devient activement exploitée, **la base de la décision a changé** — et personne ne le verra si les deux dispositifs ne se parlent pas.

✅ **BONNE PRATIQUE (P0)** — Croisez trimestriellement le registre des dérogations avec les catalogues d'exploitation avérée. L'exercice prend une heure et produit, en moyenne, une à deux réévaluations.

### 23.5 Ce que le support et les métiers savent

**Le gisement le moins technique et le plus négligé.**

| Source | Ce qu'elle sait |
|---|---|
| Le support utilisateurs | Les tentatives d'ingénierie sociale signalées, les comportements anormaux |
| Le service commercial | Ce que les clients demandent, ce qui inquiète le secteur |
| Les achats | Les incidents chez les fournisseurs, les questionnaires reçus |
| Les affaires réglementaires | Les obligations émergentes, les signalements sectoriels |
| Les ressources humaines | Les tentatives d'approche, les faux recrutements |
| La communication | Les usurpations d'identité, les mentions publiques |

**Ce qui bloque** : aucune de ces personnes ne pense détenir du renseignement, et aucune ne sait à qui le dire.

**Ce qui débloque, et ce n'est pas un outil** : une question posée régulièrement. Un point de quinze minutes par trimestre avec chacun de ces interlocuteurs, avec une seule question — *avez-vous vu quelque chose d'inhabituel ?* — produit davantage que la plupart des flux.

🎯 **ET MAINTENANT ?**
*Vous prenez un poste de CTI dans une organisation qui n'en avait pas. Quelle est votre première source ?*
**Réponse** : les incidents des dix-huit derniers mois. Avant tout abonnement, avant toute veille, vous relisez ce qui est réellement arrivé à cette organisation — vecteurs d'entrée, ce qui a fonctionné pour l'adversaire, ce qui l'a arrêté, ce qui n'a pas été détecté. Deux à trois jours de travail. Vous en tirerez trois choses qu'aucune source externe ne vous donnera : les angles morts réels, les mesures qui tiennent, et le profil des menaces qui atteignent effectivement cette organisation. C'est aussi ce qui vous rendra crédible auprès des équipes, parce que vous parlerez de ce qu'elles ont vécu.

### 23.6 Transformer un incident en fiche de renseignement

**Le format**, une page, produit à la clôture de chaque incident significatif.

| Section | Contenu | Destinataire ultérieur |
|---|---|---|
| **Vecteur d'entrée** | Précis, avec la mesure qui aurait dû l'empêcher | MCS, architecture |
| **Séquence observée** | Les étapes, dans l'ordre, avec les techniques employées | Détection |
| **Indicateurs** | Avec dates de première et dernière observation | Détection, partage sectoriel |
| **Ce qui a arrêté l'adversaire** | La mesure efficace, nommée | Direction — argumentaire d'investissement |
| **Ce qui n'a pas détecté** | L'écart de couverture, localisé | Détection |
| **Délai entrée → détection** | En heures ou en jours | Indicateur de capacité (§35) |
| **Ce qui est partageable** | Après anonymisation, selon les catégories du §20.8 | Dispositif sectoriel |
| **Ce que cela change** | Les décisions à réexaminer | Tous |

**La dernière ligne est celle qui distingue une fiche d'un compte rendu.** Un incident produit des faits ; la fiche dit ce qu'il faut en faire ailleurs.

### 23.7 🔴 FIL ROUGE — février 2030 : plus qu'un an de flux

Le 3 février, HELIOMED subit un incident : un poste de la R&D de Nantes est compromis par une pièce jointe. L'adversaire progresse pendant onze jours avant d'être détecté par une alerte sur un accès inhabituel au dépôt de code. Aucune donnée n'est exfiltrée.

**L'équipe de réponse produit son rapport le 20 février** : chronologie, périmètre, actions de remédiation, recommandations techniques. Vingt-deux pages. Il est archivé.

**Nour produit sa fiche de renseignement le 24 février.** Une page. Voici ce qu'elle contient, et ce qu'elle déclenche.

| Section | Contenu | Effet |
|---|---|---|
| **Vecteur** | Pièce jointe, macro, exécution après avertissement ignoré. La politique de blocage des macros existe mais **exclut le service R&D depuis 2027** | Exclusion réexaminée et supprimée en mars |
| **Séquence** | 6 techniques identifiées, dont 3 non couvertes par la détection | Trois règles écrites en mars |
| **Indicateurs** | 14, dont 9 encore valides à la date de la fiche | Partagés au dispositif sectoriel le 26 février |
| **Ce qui a arrêté** | L'alerte sur accès inhabituel au dépôt de code — **règle écrite six mois plus tôt sur la base du besoin B-05** | **Argumentaire d'investissement en détection** |
| **Ce qui n'a pas détecté** | L'accès initial, la persistance, le mouvement latéral — 11 jours d'invisibilité | Analyse d'écart §18.8 confirmée par le réel |
| **Délai entrée → détection** | **11 jours** | Premier indicateur de capacité chiffré |
| **Ce que cela change** | 4 décisions listées | — |

**Ce que la fiche produit, et que le rapport de vingt-deux pages n'avait pas produit** :

1. **L'exclusion de 2027 est réexaminée.** Elle figurait dans le rapport de réponse comme une observation technique ; la fiche la formule comme une décision à revoir, avec un destinataire.
2. **Trois règles de détection sont écrites.** Le rapport listait les techniques ; la fiche les croise avec la cartographie du §18.8 et identifie lesquelles manquaient.
3. **Les indicateurs sont partagés.** Neuf sur quatorze étaient encore valides — deux membres du dispositif sectoriel signalent une activité correspondante dans les trois semaines suivantes.
4. **L'argument d'investissement change de nature.** Ce n'est plus « il faudrait investir en détection », c'est *« la règle qui nous a sauvés a été écrite en août à partir d'un besoin exprimé en mai ; nous en avons trois autres en attente »*.

**Le chiffre que Claire porte au comité du 12 mars**, et qui frappe :

> *Cet incident a produit plus de renseignement exploitable — quatorze indicateurs contextualisés, six techniques confirmées, un écart de couverture localisé, une décision de configuration à revoir — que douze mois de flux externe.*

**Ce que Karim Lebrun demande alors**, et qui devient un point de méthode : *« est-ce que ça vaut pour tous les incidents, ou seulement pour celui-là ? »*

**Réponse honnête de Nour** : non. Un incident mineur — un poste isolé, sans progression — produit peu. Le critère retenu est écrit : **une fiche est produite pour tout incident ayant impliqué une progression au-delà de l'actif initial, ou une durée de détection supérieure à 48 heures.** Sur l'année 2030, cela représente quatre incidents sur onze.

**L'effet mesuré à douze mois** :

| Source | Éléments exploités en 2030 |
|---|---|
| Flux commercial (fournisseur B) | 14 |
| Sources ouvertes | 61 |
| Dispositif sectoriel | 23 |
| **Incidents internes (4 fiches)** | **38** |

Trente-huit éléments exploités issus de quatre incidents. Le coût de production : environ une journée de travail par fiche.

> *« La source la moins chère est celle qu'on paie déjà »*, écrit Nour.

**Livrable de l'épisode.** La fiche de renseignement post-incident en huit sections, et le critère de déclenchement — annexe D.

→ La suite en 🔴 §24.5, quand un pivot d'infrastructure produira une découverte et deux faux positifs.

### Synthèse mentale du chapitre 23

Aucun fournisseur ne peut vous vendre du renseignement, parce que le renseignement suppose votre contexte — que vous seul détenez, et qui produit de l'information en permanence. Cette source est négligée pour trois raisons : elle ne ressemble pas à du renseignement, elle est dispersée, et elle demande de demander. Un incident produit six éléments de valeur presque toujours perdus, dont le plus rare est *ce qui a arrêté l'adversaire* — la mesure qui fonctionne. Les tentatives d'exploitation bloquées en frontal disent quelles vulnérabilités sont activement testées contre vous : c'est le renseignement le plus directement actionnable qui soit, il existe partout et n'est presque jamais exploité. Le registre des dérogations doit être croisé avec les catalogues d'exploitation, parce qu'une décision de ne pas corriger repose sur une évaluation qui peut avoir changé. Enfin, le gisement le moins technique — support, commercial, achats, ressources humaines — se débloque par une question posée trimestriellement, pas par un outil.

**Trois questions de vérification**

1. Vous prenez un poste de CTI dans une organisation sans dispositif existant. Quelle est votre première source, et pourquoi avant tout abonnement ?
2. Quelle donnée, présente dans presque toutes les organisations, indique quelles vulnérabilités sont activement testées contre vous ?
3. Pourquoi un registre de dérogations est-il une source de renseignement, et que faites-vous de ce croisement ?

---

## Chapitre 24 — L'infrastructure adverse

> ⚠️ **Avertissement de proportionnalité.** Ce chapitre décrit la compétence la plus technique et la plus séduisante du CTI. Elle est aussi celle dont le rapport entre le temps consacré et la valeur produite est le plus défavorable dans une organisation ordinaire. Lisez-le en gardant le §24.6 à l'esprit.

### 24.1 Ce qu'on appelle infrastructure

**Définition** : l'ensemble des ressources techniques employées par un adversaire pour conduire une opération.

| Élément | Ce qu'il permet | Durée de vie typique |
|---|---|---|
| Adresses | Hébergement, commande, exfiltration | Jours à mois |
| Noms de domaine | Résolution, apparence légitime | Semaines à mois |
| Certificats | Chiffrement, crédibilité | Mois |
| Hébergeurs et fournisseurs | Le socle | Longue |
| Empreintes de services exposés | Configuration caractéristique d'un outil | Variable |
| Adresses de messagerie | Enregistrement de domaines, contact | Variable |

**Ce qui rend cette matière analysable** : un adversaire réutilise. Créer une infrastructure coûte du temps et de l'argent (§16.3), et la réutilisation est la norme — ce qui permet de relier des éléments entre eux.

### 24.2 Le pivot

**Le principe** : partir d'un élément connu et découvrir les éléments qui lui sont liés.

```
Un domaine connu
     ├──► adresse de résolution ──► autres domaines résolvant vers elle
     ├──► certificat ──────────────► autres domaines couverts
     ├──► enregistrement ──────────► autres domaines du même déposant
     └──► empreinte de service ────► autres serveurs à configuration identique
```

**Ce que le pivot produit** : à partir d'un indicateur unique, un ensemble de plusieurs dizaines d'éléments potentiellement liés.

**Ce qu'il ne produit pas** : la certitude que ces éléments sont liés à la même opération. Chaque pivot est une **hypothèse de lien**, à évaluer comme telle.

⚠️ **PIÈGE — le pivot en chaîne**
Pivoter depuis un élément découvert par pivot multiplie l'incertitude. Au troisième niveau, on obtient couramment des centaines d'éléments dont la relation avec l'origine est purement hypothétique. **La règle** : un pivot au premier niveau est exploitable, au deuxième il demande une confirmation indépendante, au troisième il n'est plus qu'une piste.

### 24.3 Les sources d'enrichissement et leurs limites

| Source | Ce qu'elle apporte | Limite majeure |
|---|---|---|
| Résolution de noms passive | Historique des associations domaine/adresse | Couverture partielle, variable selon les régions |
| Journaux de certificats | Les noms couverts par un certificat public | Ne voit que le public |
| Registres d'enregistrement | Déposant, dates | **Largement anonymisés** aujourd'hui |
| Balayage d'Internet | Services exposés, configurations, empreintes | Photographie datée, souvent hebdomadaire |
| Bases de réputation | Signalements antérieurs | Faible qualité, forte circularité |
| Analyse de maliciel | Ce que le code contacte | Nécessite l'échantillon et la compétence |

**Le point commun de ces sources** : elles décrivent l'infrastructure **telle qu'elle était au moment de l'observation**. Une adresse associée à une activité malveillante en mars peut être parfaitement légitime en juin.

### 24.4 Durée de vie et conséquence sur vos blocages

**Le fait structurant** : l'infrastructure adverse est **jetable**. Elle est conçue pour être abandonnée.

| Conséquence | Explication |
|---|---|
| Un blocage vieillit mal | Une liste jamais purgée bloque des ressources devenues légitimes |
| Le rendement décroît vite | La majorité de la valeur d'un indicateur est consommée dans ses premiers jours |
| **Les faux positifs s'accumulent** | Adresses réattribuées, hébergement mutualisé, services légitimes compromis puis nettoyés |

✅ **BONNE PRATIQUE (P0) — la date d'expiration**
Tout indicateur d'infrastructure entre en blocage **avec une date de retrait**. Trente à quatre-vingt-dix jours selon le type, sauf réexamen explicite. Une liste de blocage sans mécanisme d'expiration devient, en dix-huit mois, une source majeure d'incidents pour les utilisateurs — et personne ne fait le lien.

⚠️ **Le cas de l'hébergement mutualisé** : bloquer une adresse hébergeant des centaines de sites légitimes pour un site malveillant est une erreur fréquente et coûteuse. Vérifiez ce qui d'autre réside à cette adresse avant tout blocage.

### 24.5 ⚠️ Faux positifs et contre-mesures adverses

| Piège | Mécanisme | Comment l'éviter |
|---|---|---|
| **Infrastructure partagée** | Hébergeur mutualisé, réseau de diffusion, service légitime | Vérifier la colocation avant blocage |
| **Service légitime détourné** | L'adversaire emploie une plateforme grand public | Le blocage casse un usage légitime |
| **Adresse réattribuée** | Le fournisseur a réattribué l'adresse à un autre client | Vérifier la fraîcheur de l'observation |
| **Empoisonnement délibéré** | L'adversaire associe son activité à des ressources légitimes | Ne jamais bloquer sans vérification |
| **Infrastructure de recherche** | Balayeurs académiques, moteurs de recherche, chercheurs | Identifier les acteurs connus |

**Le quatrième mérite un mot** : un adversaire averti sait que ses indicateurs seront collectés et diffusés. Y mêler délibérément des ressources largement utilisées produit des blocages dommageables chez ses cibles — et discrédite les listes qui les diffusent.

### 24.6 📌 Ce qui relève de l'analyse et ce qui relève de l'illusion

**La section la plus importante du chapitre.**

| Activité | Valeur pour une organisation ordinaire |
|---|---|
| Vérifier la colocation avant un blocage | **Élevée** — évite des incidents |
| Vérifier la fraîcheur d'un indicateur reçu | **Élevée** — cinq minutes |
| Pivoter au premier niveau sur un élément d'un incident propre | **Correcte** — peut élargir le périmètre d'une recherche |
| Pivoter au deuxième niveau | Faible, sauf besoin explicite |
| Cartographier l'infrastructure d'un acteur | **Très faible** — c'est le niveau 3 de l'attribution (§13.1) |
| Suivre l'évolution d'une infrastructure dans la durée | **Très faible** sans moyens dédiés |

**Le constat honnête** : cette matière est passionnante, visuellement gratifiante — les graphes de relations sont impressionnants — et elle produit peu de décisions dans une organisation ordinaire.

> **Le test à s'appliquer** : *ce pivot va-t-il changer une décision, ou vais-je produire un graphe ?*

**Ce qui justifie néanmoins d'en maîtriser les bases** : la vérification avant blocage, le contrôle de fraîcheur, et la capacité à élargir la recherche autour d'un incident propre. Ces trois usages ont une valeur réelle et demandent trente minutes de compétence, pas trois mois.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel vous transmet une liste de 200 adresses associées à une campagne active. Que faites-vous avant de les bloquer ?*
**Réponse** : trois vérifications, une heure. *La fraîcheur* — quelle est la date de dernière observation ? Tout élément de plus de 90 jours est écarté par défaut. *La colocation* — combien de ces adresses hébergent également des services légitimes ? Un échantillon de vingt suffit à estimer le risque. *L'applicabilité* — vos actifs communiquent-ils déjà avec certaines d'entre elles ? Si oui, c'est une recherche à mener avant tout blocage, parce que la réponse peut être « oui, légitimement ». Puis vous bloquez ce qui reste, **avec une date de retrait**.

### 24.7 🔬 Mini-lab 7 — Un pivot, une découverte, deux faux positifs

**Objectif** — Conduire un pivot, évaluer la solidité des liens, et éviter deux blocages dommageables.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** §24.2 à §24.5 · **Livrable** liste de blocage argumentée
**Compétences validées** — ✔ évaluer un lien issu d'un pivot ✔ vérifier une colocation ✔ contrôler la fraîcheur ✔ distinguer analyse et illusion ✔ justifier un non-blocage

**Le point de départ** : lors d'un incident, un poste de votre organisation a contacté le domaine `sync-portal-update[.]net`. Ce domaine est confirmé malveillant.

**Les données d'enrichissement fournies** :

```
sync-portal-update[.]net
  └── résout vers 203.0.113.44  (observé du 12/03 au 02/05/2030)

203.0.113.44 — autres domaines ayant résolu vers cette adresse :
   ① sync-portal-update[.]net     12/03 → 02/05/2030
   ② client-sync-eu[.]net         14/03 → 29/04/2030
   ③ mail-portal-secure[.]net     11/03 → 05/05/2030
   ④ boutique-artisanale[.]fr     01/2019 → aujourd'hui
   ⑤ association-locale-92[.]org   06/2021 → aujourd'hui
   ⑥ cdn-assets-delivery[.]com     2017 → aujourd'hui

Certificat couvrant ① : couvre également ② et ③
Enregistrement de ① : déposant anonymisé, créé le 09/03/2030
Enregistrement de ② : déposant anonymisé, créé le 09/03/2030
Enregistrement de ③ : déposant anonymisé, créé le 10/03/2030
Enregistrement de ④ : déposant identifié, créé en 2019
Balayage de 203.0.113.44 : 341 sites hébergés
```

**Questions** : (a) Quels éléments retenez-vous, et avec quelle solidité ? (b) Que bloquez-vous ? (c) Quels sont les deux faux positifs, et que se passe-t-il si vous les bloquez ? (d) Quelle date de retrait ?

---

**Corrigé commenté**

**(a) Évaluation des liens**

| Élément | Lien avec ① | Solidité | Justification |
|---|---|---|---|
| ② `client-sync-eu[.]net` | **Fort** | **Élevée** | Trois critères indépendants : même certificat · création le même jour · fenêtre d'activité cohérente |
| ③ `mail-portal-secure[.]net` | **Fort** | **Élevée** | Idem, création à un jour près |
| ④ `boutique-artisanale[.]fr` | **Aucun** | — | Hébergé depuis 2019, déposant identifié |
| ⑤ `association-locale-92[.]org` | **Aucun** | — | Hébergé depuis 2021 |
| ⑥ `cdn-assets-delivery[.]com` | **Aucun** | — | Hébergé depuis 2017 |
| **L'adresse 203.0.113.44** | Partagé | — | **341 sites hébergés** |

**Le critère décisif** est la conjonction de trois éléments indépendants pour ② et ③ : le certificat commun, la date de création, et la fenêtre d'activité. Un seul de ces critères ne suffirait pas ; les trois ensemble constituent un lien solide.

**(b) Ce qu'on bloque**

| Élément | Décision | Motif |
|---|---|---|
| ① `sync-portal-update[.]net` | **Bloquer** | Confirmé malveillant |
| ② `client-sync-eu[.]net` | **Bloquer** | Trois critères indépendants |
| ③ `mail-portal-secure[.]net` | **Bloquer** | Idem |
| **203.0.113.44** | **NE PAS BLOQUER** | 341 sites hébergés |

**(c) Les deux faux positifs, et leurs conséquences**

**Faux positif n° 1 — bloquer l'adresse `203.0.113.44`.** C'est l'erreur principale du dossier, et elle est fréquente. Bloquer cette adresse coupe l'accès à **341 sites**, dont ④, ⑤ et ⑥ manifestement légitimes. L'un d'eux — ⑥ — est un service de diffusion de contenu, ce qui signifie que le blocage peut dégrader des sites tiers sans rapport, y compris des services utilisés par votre organisation.

**Faux positif n° 2 — bloquer ④, ⑤ ou ⑥ par association.** Un analyste pressé peut considérer que tout ce qui réside à cette adresse est suspect. Les dates d'hébergement — 2017, 2019, 2021 — l'excluent : ces domaines précèdent de plusieurs années la création de l'infrastructure malveillante. Ils sont **colocataires**, pas complices.

⚠️ Ce que ces deux faux positifs auraient produit : des tickets utilisateurs, une perte de confiance dans les blocages, et — c'est le plus grave — une pression pour désactiver les listes.

**(d) La date de retrait**

| Élément | Retrait proposé | Motif |
|---|---|---|
| ①, ②, ③ | **90 jours**, réexamen le 15 août | La dernière observation date du 05/05 ; l'infrastructure est probablement déjà abandonnée |

**La justification à écrire** : *« blocage de trois domaines liés par certificat commun et date de création, activité observée du 09/03 au 05/05/2030. Adresse d'hébergement non bloquée : 341 sites colocataires dont plusieurs légitimes antérieurs à 2020. Réexamen le 15/08/2030. »*

**Les trois erreurs attendues**

1. **Bloquer l'adresse.** C'est le réflexe, et c'est l'erreur la plus coûteuse du lab.
2. **Ne retenir que le domaine d'origine.** ② et ③ sont solidement liés ; les écarter perd de la couverture sans raison.
3. **Bloquer sans date de retrait.** Dans dix-huit mois, personne ne saura pourquoi ces trois domaines sont dans la liste, ni s'il faut les y laisser.

### 24.8 🔴 FIL ROUGE — mars 2030 : le graphe qui ne servait à rien

Après l'incident de février (§23.7), Nour dispose de quatorze indicateurs. Elle consacre deux journées à un travail de pivot approfondi.

**Le résultat** : un ensemble de 87 éléments — domaines, adresses, certificats — reliés à l'infrastructure de l'incident avec des degrés de confiance variables. Le graphe est impressionnant, et elle le présente au comité du 12 mars.

**La question de Claire** : *« qu'est-ce qu'on fait avec ça ? »*

**La réponse honnête**, que Nour donne après réflexion :

| Sur les 87 éléments | Usage |
|---|---|
| 9 | **Bloqués** — ceux du premier niveau de pivot, solidement liés |
| 12 | Recherchés rétrospectivement dans les journaux — **aucune correspondance** |
| 4 | Partagés au dispositif sectoriel |
| **62** | **Aucun usage identifié** |

**Le calcul qu'elle fait ensuite** : deux journées de travail pour neuf blocages et quatre partages. Les mêmes neuf blocages auraient été obtenus par un pivot de premier niveau en **quarante minutes**.

**Ce que Claire en tire**, et qui devient une règle :

> *« Le pivot de premier niveau, systématiquement. Au-delà, seulement si une question précise le justifie. »*

**Ce que Nour écrit dans son carnet**, et qui est plus honnête que la règle :

> *J'ai fait ce graphe parce qu'il était intéressant, pas parce qu'il servait. C'est la première fois que je m'en aperçois pendant que je le fais, et pas après.*

**L'exception qui confirme la règle**, six mois plus tard. En septembre 2030, un pivot de deuxième niveau est conduit — cette fois avec une question précise : *l'infrastructure de la campagne de juillet (§19.6) est-elle liée à celle de février ?* La réponse est non, et elle est obtenue en trois heures. **La question a rendu le travail utile ; c'est elle qui manquait en mars.**

**Livrable de l'épisode.** La règle du pivot de premier niveau, et le test à s'appliquer avant tout élargissement : *quelle question ce pivot va-t-il trancher ?*

→ **Fin de la Partie V.** La suite en Partie VI, quand il faudra transformer tout cela en produits que quelqu'un lit.

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> - **poser les quatre questions juridiques** avant toute collecte, et associer le délégué à la protection des données au moment du plan, pas du contrôle ;
> - **reconnaître qu'un accès techniquement possible n'est pas licite**, et connaître les sept interdits ;
> - **construire une veille tenable** en vingt minutes par jour, sur quatre sources ;
> - **reconnaître la fatigue de veille** et savoir que son remède est de réduire, pas d'ajouter ;
> - **évaluer un fournisseur en cinq tests** avant d'acheter, et substituer au volume la question du nombre d'éléments ayant produit une action ;
> - **exploiter la source la plus pertinente et la moins chère** : vos incidents, vos tentatives bloquées, vos dérogations, ce que savent vos métiers ;
> - **conduire un pivot d'infrastructure** au premier niveau, vérifier une colocation, et savoir quand un graphe ne sert à rien.
>
> **Ce que vous ne savez pas encore** : comment écrire tout cela pour que quelqu'un le lise, le comprenne et décide. C'est l'objet de la Partie VI.

---
