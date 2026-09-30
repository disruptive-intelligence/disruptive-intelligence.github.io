---
title: Chapitre 11 — Produire un jugement analytique
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 11.1 Décrire et évaluer

Le chapitre 6 a posé l'axiome : une analyse est une hypothèse argumentée, pas une description. Voici comment on en fabrique une.

**La différence, en une comparaison :**

| Description | Évaluation |
|---|---|
| *« Trois publications font état d'un ciblage sectoriel. Une victime a été confirmée. L'infrastructure employée présente des similarités avec une campagne antérieure. »* | *« Nous estimons probable que ces incidents relèvent d'une campagne unique — confiance moyenne, fondée sur la réutilisation d'infrastructure et sur la concentration temporelle, affaiblie par l'absence de vecteur commun identifié. »* |
| Tout est vrai | Tout est vrai **et** quelqu'un s'est engagé |
| Le lecteur doit conclure | Le lecteur peut décider ou contester |

**Ce qui fait la différence n'est pas la quantité d'information.** C'est la présence de quatre éléments que la description ne contient pas : un verbe d'estimation, un mot de probabilité, un niveau de confiance, et une justification de ce niveau.

⚠️ **PIÈGE — la prudence qui n'en est pas une**
Refuser de conclure passe pour de la rigueur. C'en est parfois. Mais le plus souvent, c'est un transfert : l'analyste renvoie au destinataire un travail qu'il aurait dû faire, en se protégeant de l'erreur. Le destinataire, lui, conclura quand même — avec moins d'éléments et moins de méthode.

## 11.2 Construire une évaluation

Cinq blocs, dans cet ordre. C'est le modèle qui figure en annexe D.

```
① LA QUESTION        À quoi répond ce document, et qui l'a posée
② LES FAITS          Ce que nous observons, avec sources et dates
③ LE RAISONNEMENT    Les hypothèses envisagées, ce qui les départage
④ LA CONCLUSION      L'estimation, calibrée, avec la suivante
⑤ LA RÉFUTATION      Ce qui l'invaliderait, et ce qui trancherait
```


**Ce que chaque bloc doit contenir**, et l'erreur qui lui correspond :

| Bloc | Contenu | Erreur fréquente |
|---|---|---|
| ① Question | Une question, formulée comme telle | Un sujet — « la campagne TEMPEST-14 » — qui n'appelle aucune réponse |
| ② Faits | Uniquement des observations, avec source et date | Des verbes d'intention (§4.1) |
| ③ Raisonnement | Les hypothèses concurrentes, et ce qui les discrimine | Une liste d'éléments « à l'appui » (§7.2) |
| ④ Conclusion | Estimation + probabilité + confiance + justification | Une affirmation nue |
| ⑤ Réfutation | Ce qui la renverserait, ce qui trancherait | **Absente huit fois sur dix** |

**Le bloc ⑤ est le marqueur de maturité.** Un produit qui ne dit pas ce qui l'invaliderait ne peut pas être révisé — il ne peut qu'être cru ou rejeté. Le §11.3 lui est consacré.

## 11.3 Ce qui invaliderait votre analyse

**La section que personne n'écrit**, et qui distingue une analyse d'une opinion.

**Ce qu'elle est** : la liste explicite des observations qui, si elles se produisaient, vous conduiraient à changer de conclusion.

**Ce qu'elle n'est pas** : une précaution rhétorique. *« Cette évaluation pourrait évoluer en fonction de nouveaux éléments »* ne dit rien — c'est vrai de toute évaluation.

🧪 **EN PRATIQUE — construire une clause de réfutation**

Trois questions, et une ligne par réponse :

```
1. Quelle observation rendrait mon hypothèse retenue improbable ?
2. Quelle observation rendrait l'hypothèse suivante plus probable que la mienne ?
3. Quel présupposé, s'il était faux, effondrerait le raisonnement ?
```


**Exemple, sur le cas du prestataire (§8.9)** :

> *Cette évaluation serait invalidée si :*
> *— un vecteur d'entrée commun aux trois victimes, indépendant du prestataire, était identifié ;*
> *— le prestataire démontrait l'absence de compromission de son infrastructure d'administration ;*
> *— une quatrième victime, non cliente du prestataire, était constatée.*

**Ce que cette section produit concrètement**, et ce sont trois effets distincts :

| Effet | Mécanisme |
|---|---|
| **Elle oriente la collecte** | Chaque ligne est une question à poser (§14.4) |
| **Elle protège l'analyste** | Le jour où l'alternative se vérifie, il l'avait envisagée et dit pourquoi il l'écartait |
| **Elle discipline le raisonnement** | Une hypothèse qu'on ne sait pas réfuter n'est pas une hypothèse forte : elle est irréfutable, donc vide (§6.3) |

**Le troisième effet est le plus important**, et il agit **pendant** la rédaction : chercher ce qui invaliderait sa propre conclusion oblige à l'examiner. C'est le même mécanisme que l'échelle de calibrage du §9.8 — l'outil sert d'abord à celui qui l'emploie.

## 11.4 Les indicateurs de changement

**Le principe** : à côté de ce qui invaliderait l'analyse, on précise ce qui la **ferait évoluer**, sans nécessairement la renverser.

| | Réfutation | Indicateur de changement |
|---|---|---|
| Effet | La conclusion tombe | La conclusion se déplace |
| Exemple | « Une quatrième victime hors clientèle du prestataire » | « Une revendication publique » — cela ne change pas l'origine, cela change la nature de la menace |
| Ce qu'on en fait | On réécrit | On révise la confiance ou la portée |

**La grille de signaux du §8.4 alimente directement cette section.** Et sa vertu opérationnelle est double : elle permet de **conclure en attendant**, et elle constitue une liste de requêtes exploitables par la détection (chapitre 30).

## 11.5 Distinguer évaluation et recommandation

**Deux registres distincts, deux responsabilités distinctes.**

| | **Évaluation** | **Recommandation** |
|---|---|---|
| Répond à | *Qu'est-ce qui se passe ?* | *Que faut-il faire ?* |
| Relève de | L'analyste | **Le décideur** — l'analyste peut proposer |
| Dépend de | Les faits et le raisonnement | L'évaluation **plus** le contexte, les moyens, les priorités |
| Peut être juste alors que l'autre est fausse | Oui, dans les deux sens | Oui |

**Pourquoi les séparer physiquement dans le document** : parce qu'un désaccord sur la recommandation ne doit pas contaminer l'évaluation. Un RSSI peut accepter votre analyse et refuser votre recommandation — pour des raisons de moyens ou de calendrier qui ne vous concernent pas. Si les deux sont mêlées, le refus de l'une emporte le rejet de l'autre.

⚠️ **PIÈGE — la recommandation déguisée en évaluation**
*« La menace est critique et impose un renforcement immédiat de la surveillance »* mélange les deux. La première partie est une évaluation mal calibrée, la seconde une recommandation présentée comme une conséquence nécessaire. Le destinataire n'a plus d'espace de décision — et c'est exactement ce qu'il faut lui laisser.

✅ **BONNE PRATIQUE (P0)** — Deux sections séparées, avec un titre chacune. Et dans la recommandation, indiquez **le coût estimé** : une recommandation sans ordre de grandeur de coût est une recommandation que le décideur ne peut pas arbitrer.

## 11.6 ⚠️ L'analyse qui n'engage à rien

Quatre formes, toutes fréquentes, toutes reconnaissables.

| Forme | Exemple | Ce qui manque |
|---|---|---|
| **Le conditionnel en cascade** | « Cela pourrait indiquer que l'acteur chercherait à… » | Toute prise de position |
| **L'inventaire d'hypothèses sans hiérarchie** | « Plusieurs explications sont envisageables : A, B, C. » | Laquelle vous retenez, et pourquoi |
| **La conclusion tautologique** | « La vigilance reste de mise. » | Une information |
| **L'évaluation sans calibrage** | « Le risque est significatif. » | Probabilité, confiance, et une définition de « significatif » |

**Le test qui les détecte tous** : *si je supprimais cette phrase, le lecteur perdrait-il quelque chose ?* Appliqué à une conclusion, il élimine l'essentiel du remplissage.

🎯 **ET MAINTENANT ?**
*Vous relisez votre évaluation et la conclusion dit : « la situation appelle une surveillance accrue et une vigilance particulière sur les accès distants ». Que faites-vous ?*
**Réponse** : vous la réécrivez, parce qu'elle ne contient ni évaluation ni recommandation exploitable. La version utilisable sépare les deux : *« Nous estimons probable que les accès distants constituent le vecteur privilégié de cette campagne — confiance moyenne, fondée sur deux victimes documentées. Nous recommandons trois actions : recherche rétrospective sur 90 jours des authentifications depuis des origines inhabituelles (2 jours-homme) · vérification de l'activation de l'authentification multifacteur sur les 4 comptes de service concernés (2 heures) · règle d'alerte sur les authentifications hors plage horaire (1 jour). »* La différence n'est pas la longueur : c'est qu'on peut décider.

## 11.7 ✅ Livrable — Structure d'une évaluation

| Section | Contenu | Longueur |
|---|---|---|
| **En-tête** | Question · demandeur · date · **date de réexamen** · analyste · relecteur | 3 lignes |
| **Réponse en une phrase** | La conclusion, calibrée | 1 phrase |
| **Ce que nous observons** | Faits uniquement, avec source et date | ½ page |
| **Ce que nous en estimons** | Hypothèses envisagées · ce qui les départage · conclusion calibrée · hypothèse suivante | ½ à 1 page |
| **Ce qui invaliderait cette analyse** | 2 à 4 lignes, opérationnelles | 4 lignes |
| **Ce qui trancherait** | Les questions à poser, les données à obtenir | 3 lignes |
| **Ce que nous recommandons** | **Section séparée**, avec coût estimé par action | ½ page |
| **Ce que nous ne savons pas** | Les lacunes, et leur effet sur la conclusion | 3 lignes |
| Annexe | L'échelle de calibrage (§9.7) | 1 page |

**La « réponse en une phrase » en tête est ce qui fait lire le reste.** Elle applique le principe du chapitre 25 : conclusion d'abord, preuve ensuite.

## 11.8 🔴 FIL ROUGE — décembre 2029 : la ligne qui change la décision

Le 6 décembre, Yann Prigent, responsable produit, sollicite Nour. Un client hospitalier a signalé un comportement anormal de la passerelle HelioBox installée chez lui : redémarrages inexpliqués, deux fois en trois semaines.

**L'enjeu est important.** Si HelioBox est compromise chez un client, l'obligation de signalement réglementaire s'applique, avec des délais courts. Yann veut savoir s'il doit déclencher la procédure.

Nour dispose de peu d'éléments : les journaux du client sur 30 jours, la version installée, et le fait que deux autres clients sur les quarante-trois équipés ont signalé des redémarrages au cours du trimestre.

**Son évaluation, structurée selon le §11.7** :

> **Réponse en une phrase.** *Nous estimons peu probable que ces redémarrages résultent d'une compromission — confiance moyenne.*
>
> **Ce que nous observons.** Deux redémarrages non planifiés en trois semaines chez un client · trois clients sur quarante-trois ayant signalé des redémarrages ce trimestre · aucun élément anormal dans les journaux disponibles · la version installée correspond à la version courante · aucun signalement de vulnérabilité affectant ce produit.
>
> **Ce que nous en estimons.** Trois hypothèses ont été envisagées. *Compromission* : aucun élément à l'appui, mais les journaux ne couvrent que 30 jours et ne tracent pas les modifications de configuration. *Défaut logiciel* : compatible avec la répartition sur trois clients distincts, et avec l'absence d'élément dans les journaux. *Cause environnementale locale* — alimentation, réseau, température : compatible chez un client, moins probable sur trois sites différents. Nous retenons le défaut logiciel, **peu probable** pour la compromission, **confiance moyenne**.
>
> **Ce qui invaliderait cette analyse.** *— Un quatrième client signalant des redémarrages avec un profil d'usage différent · une modification de configuration non expliquée sur l'un des équipements · **la découverte que les trois clients concernés partagent une caractéristique que nous n'avons pas identifiée**.*
>
> **Ce qui trancherait.** L'extraction des journaux de configuration des trois équipements, si le produit les conserve · la comparaison des versions de micrologiciel exactes.
>
> **Ce que nous ne savons pas.** Nos journaux clients ne tracent pas les modifications de configuration. Cette lacune est structurelle et concerne les quarante-trois équipements : nous ne pourrions pas détecter une compromission silencieuse.

**Ce qui se passe.** Yann lit la troisième ligne de la clause de réfutation — *une caractéristique commune que nous n'avons pas identifiée* — et fait une vérification que personne n'avait demandée : les trois clients concernés utilisent-ils quelque chose en commun ?

**Réponse en une demi-journée** : oui. Les trois sont les seuls, sur quarante-trois, à avoir souscrit une option de synchronisation avec un système d'information hospitalier tiers — activée chez eux, inactive chez les quarante autres.

**La conclusion révisée**, le 11 décembre :

> *Nous estimons très probable que ces redémarrages soient liés au module de synchronisation optionnel — confiance élevée, fondée sur la correspondance exacte entre les trois clients concernés et les trois seuls clients ayant activé cette option.*

Le développement identifie une semaine plus tard une fuite de mémoire dans ce module, corrigée en janvier. Aucune compromission, aucune obligation de signalement.

**Ce que Claire souligne au comité** : la clause de réfutation n'a pas servi à protéger l'analyste. **Elle a produit la bonne réponse.** La troisième ligne n'était pas une précaution rhétorique : c'était une question ouverte, écrite parce que le modèle l'exigeait, et quelqu'un est allé y répondre.

**L'autre effet, moins visible et plus durable.** La section *« ce que nous ne savons pas »* a signalé une lacune structurelle : les équipements ne tracent pas les modifications de configuration. Personne ne l'avait formulé jusque-là. Cette phrase devient une exigence de conception pour la version suivante d'HelioBox — et elle est portée par le responsable produit, pas par la sécurité.

> *« Une évaluation utile ne répond pas seulement à la question posée, écrit Nour. Elle montre où on ne voit rien. »*

**Livrable de l'épisode.** Le modèle d'évaluation en neuf sections, adopté comme standard — annexe D.

→ La suite en 🔴 §12.6, quand une seconde paire d'yeux verra ce qu'un analyste seul ne pouvait pas voir.

## Synthèse mentale du chapitre 11

Une évaluation se distingue d'une description par quatre éléments : un verbe d'estimation, un mot de probabilité, un niveau de confiance et sa justification — refuser de conclure n'est pas de la rigueur mais un transfert de travail vers le destinataire, qui conclura de toute façon avec moins de méthode. Cinq blocs la structurent, et le cinquième — ce qui l'invaliderait — est le marqueur de maturité : absent huit fois sur dix, il oriente la collecte, protège l'analyste et discipline le raisonnement pendant la rédaction. Évaluation et recommandation relèvent de deux responsabilités distinctes et se séparent physiquement, faute de quoi un désaccord sur l'une emporte le rejet de l'autre. Quatre formes d'analyse n'engagent à rien — le conditionnel en cascade, l'inventaire sans hiérarchie, la conclusion tautologique, l'évaluation non calibrée — et un test les détecte toutes : si je supprimais cette phrase, le lecteur perdrait-il quelque chose ? Enfin, une évaluation utile ne répond pas seulement à la question posée : elle montre où l'on ne voit rien.

**Trois questions de vérification**

1. Pourquoi « cette évaluation pourrait évoluer en fonction de nouveaux éléments » n'est-elle pas une clause de réfutation ?
2. Votre destinataire accepte votre analyse et rejette votre recommandation. Est-ce un échec ? Qu'est-ce que cela indique sur la structure de votre document ?
3. Construisez une clause de réfutation en trois lignes pour une évaluation concluant à une campagne opportuniste plutôt qu'à un ciblage.

→ **Chapitre 12 — Analyser à plusieurs** : pourquoi l'analyse solitaire dérive, et ce qu'on peut faire quand on est seul.

---
