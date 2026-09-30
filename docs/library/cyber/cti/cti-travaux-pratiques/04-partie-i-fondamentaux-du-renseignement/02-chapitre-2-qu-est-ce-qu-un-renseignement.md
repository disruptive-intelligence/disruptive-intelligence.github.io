---
title: Chapitre 2 — Qu'est-ce qu'un renseignement
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE I — Fondamentaux du renseignement
  - index.md
---

> **La pierre angulaire du cours.** Les cinq objets décrits ici sont réutilisés dans les trente-huit chapitres suivants. Si un seul chapitre devait être lu deux fois, c'est celui-ci.

## 2.1 Cinq objets, un seul événement

La plupart des cours donnent des définitions séparées. Nous allons faire l'inverse : suivre **un même fait** depuis son apparition brute jusqu'au jugement qu'il permet de formuler. C'est en le voyant se transformer qu'on comprend ce que chaque étape ajoute.

**L'événement.** Le 3 novembre, à 03 h 12, le pare-feu d'HELIOMED enregistre une connexion entrante en provenance de l'adresse `198.51.100.47` vers le port 443 de la passerelle d'accès distant.

### Étape 1 — La donnée

```
2029-11-03 03:12:47  198.51.100.47 -> gw-vpn.heliomed.fr:443  ACCEPT
```


**Ce que c'est** : un fait brut, sans contexte, sans interprétation. Il est vrai ou faux — ici, il est vrai, le journal l'atteste.

**Ce qu'on peut en faire** : rien. Une organisation de cette taille produit plusieurs millions de lignes de ce type par jour. Prise isolément, cette ligne ne signifie rien du tout.

⚠️ **Le piège de la donnée** : elle est **vérifiable**, donc rassurante. Beaucoup d'organisations accumulent des données et pensent progresser parce que ce qu'elles collectent est indiscutable. La solidité de la donnée ne compense jamais son absence de sens.

### Étape 2 — L'information

> *L'adresse `198.51.100.47` a établi douze connexions vers la passerelle d'accès distant entre 02 h 50 et 03 h 40, toutes avec des tentatives d'authentification échouées sur des comptes qui n'existent pas dans l'annuaire.*

**Ce qu'on a ajouté** : du **contexte**. Une agrégation temporelle, une mise en relation avec l'annuaire, la caractérisation du comportement.

**Ce que ça permet** : formuler une première question. Ce n'est pas encore une décision, c'est une hypothèse naissante — quelqu'un teste des identifiants.

**Ce que ça coûte** : les premiers choix subjectifs apparaissent. Pourquoi une fenêtre de cinquante minutes et pas de deux heures ? Pourquoi rapprocher de l'annuaire et pas des journaux applicatifs ? Chaque choix d'agrégation est une décision d'analyste, et elle oriente déjà la suite.

### Étape 3 — La connaissance

> *Cette adresse appartient à un bloc hébergé chez un fournisseur d'infrastructure à la demande. Elle apparaît dans deux publications de chercheurs des trois dernières semaines, décrivant une activité de test d'identifiants contre des passerelles d'accès distant du même constructeur que celle d'HELIOMED. Le mode opératoire décrit correspond au comportement observé.*

**Ce qu'on a ajouté** : l'**intégration à un ensemble**. L'information isolée rejoint un corpus existant. On sort du périmètre de l'organisation.

**Ce que ça permet** : sortir du cas particulier. Ce n'est plus un incident local, c'est une instance d'un phénomène plus large.

⚠️ **Le piège de la connaissance** : c'est ici qu'apparaît la circularité. Les *deux* publications sont-elles indépendantes, ou la seconde cite-t-elle la première ? Cette vérification prend cinq minutes et n'est presque jamais faite. Nous y reviendrons longuement au §10.4.

### Étape 4 — Le renseignement

> *Une activité de test d'identifiants visant les passerelles d'accès distant de notre constructeur est en cours depuis au moins trois semaines. Notre passerelle en fait l'objet. Nous exposons ce service par nécessité fonctionnelle ; 210 collaborateurs l'utilisent. L'authentification multifacteur y est active depuis 2027, ce qui rend un test d'identifiants seul insuffisant pour obtenir un accès.*

**Ce qu'on a ajouté** : la **pertinence pour une décision**. Le corpus est rapporté à **votre** contexte : votre exposition, vos mesures existantes, vos utilisateurs.

**Ce que ça permet** : décider. Et remarquez ce que la dernière phrase change : sans elle, la conclusion naturelle serait d'agir en urgence. Avec elle, la situation devient sérieuse mais maîtrisée.

**C'est ici que la plupart des organisations n'arrivent jamais.** Elles produisent des étapes 2 et 3 en abondance — des informations et de la connaissance générale — et les diffusent en croyant faire du renseignement. Le destinataire reçoit alors une description du monde, sans savoir ce qu'elle implique pour lui.

### Étape 5 — Le jugement analytique

> *Nous estimons **probable** que cette activité relève d'une campagne opportuniste visant l'ensemble des passerelles de ce constructeur exposées sur Internet, et non d'un ciblage spécifique d'HELIOMED — **confiance moyenne**, fondée sur deux sources dont l'indépendance reste à confirmer, sur l'absence de sélection apparente de nos comptes réels, et sur l'ampleur du phénomène décrit publiquement.*
>
> *Nous estimons **peu probable** qu'un accès ait été obtenu, l'authentification multifacteur étant active — **confiance élevée**, cette mesure étant vérifiée et journalisée.*
>
> *Cette évaluation serait remise en cause si : des comptes réellement existants étaient ciblés · une authentification aboutissait · l'activité persistait au-delà de la campagne décrite publiquement.*

**Ce qu'on a ajouté** : une **conclusion assumée, calibrée, et réfutable**.

Trois éléments distinguent un jugement analytique de tout ce qui précède :

| Élément | Rôle |
|---|---|
| Un **verbe d'estimation** | *Nous estimons* — l'analyste s'engage, sans prétendre à la certitude |
| Un **niveau de confiance explicite**, distinct de la gravité | Le lecteur sait sur quoi il s'appuie |
| **Ce qui l'invaliderait** | La section que presque personne n'écrit, et qui transforme une opinion en analyse |

### Le tableau récapitulatif

| Objet | Définition | Sur notre événement | Vérifiable ? |
|---|---|---|---|
| **Donnée** | Fait brut, sans contexte | Une ligne de journal | Oui |
| **Information** | Donnée mise en contexte | Douze tentatives échouées en cinquante minutes | Oui |
| **Connaissance** | Information intégrée à un ensemble | L'adresse figure dans deux publications décrivant un mode opératoire | Partiellement |
| **Renseignement** | Connaissance répondant à un besoin de décision | Notre passerelle est visée ; voici notre exposition réelle | Non — il contient une appréciation |
| **Jugement analytique** | Évaluation argumentée, calibrée, réfutable | *Probable, campagne opportuniste, confiance moyenne* | **Non, par nature** |

## 2.2 Ce que chaque étape ajoute, et ce qu'elle coûte

La colonne « vérifiable » du tableau précédent contient l'enseignement central du chapitre.

> **À mesure qu'on progresse vers le renseignement, on gagne en utilité et on perd en vérifiabilité.**

C'est un échange, et il faut l'assumer. Une donnée est incontestable et inutile. Un jugement analytique est utile et contestable. Il n'existe pas d'objet qui soit les deux à la fois — et chercher à en produire un est l'origine de deux dérives symétriques :

| Dérive | Manifestation | Conséquence |
|---|---|---|
| **Refuser de juger** | Le produit décrit longuement sans jamais conclure | Le destinataire doit faire l'analyse lui-même — donc la fonction ne sert à rien |
| **Juger sans le dire** | Le produit affirme sur le ton du fait ce qui est une appréciation | Le destinataire décide sur une base plus solide qu'elle ne l'est |

**La seconde est de loin la plus dangereuse**, et de loin la plus fréquente dans les publications commerciales. Elle est traitée en profondeur au chapitre 11.

🎯 **ET MAINTENANT ?**
*Vous recevez un rapport de fournisseur qui affirme : « le groupe X cible activement le secteur de la santé en Europe ». Que faites-vous de cette phrase ?*
**Réponse** : vous la traduisez avant de l'utiliser. « Cible activement » est-il un fait observé — des victimes identifiées, des intrusions constatées — ou un jugement — un faisceau d'indices interprétés ? Le rapport le dit-il ? S'il ne le dit pas, la phrase n'est pas exploitable en l'état : vous ne pouvez pas savoir si vous devez agir ou surveiller. La demande à faire au fournisseur tient en une ligne : *sur quelles observations cette affirmation repose-t-elle, et avec quel niveau de confiance ?*

## 2.3 Où la plupart des organisations s'arrêtent

Reprenons les cinq étapes, avec ce qu'on observe en pratique.

| Étape | Qui la produit couramment | Fréquence observée |
|---|---|---|
| Donnée | Les outils, automatiquement | Massive |
| Information | Les outils, avec un peu de configuration | Fréquente |
| Connaissance | Les fournisseurs et les publications publiques | Fréquente, et souvent achetée |
| **Renseignement** | **Vous, et personne d'autre** | **Rare** |
| **Jugement analytique** | **Vous, et personne d'autre** | **Très rare** |

**Les deux dernières lignes sont le cœur du métier**, et elles ont une propriété commune que vous devez avoir en tête tout au long du cours : **personne ne peut les produire à votre place**.

Un fournisseur peut vous vendre de la connaissance — d'excellente qualité, parfois. Il ne peut pas vous vendre du renseignement, parce qu'il ne connaît ni votre exposition, ni vos mesures existantes, ni ce que votre direction est en train de décider. Cette asymétrie explique une observation qui surprend souvent : **une organisation qui dépense beaucoup en flux et peu en analyse achète de la connaissance et croit acheter du renseignement.**

⚠️ **PIÈGE — le rapport qui décrit le monde**
Symptôme : votre produit mensuel pourrait être envoyé tel quel à n'importe quelle autre organisation du secteur. S'il ne contient rien qui vous soit propre — votre exposition, vos actifs, vos décisions en cours — ce n'est pas du renseignement, c'est de la connaissance redistribuée. Elle a une valeur, mais pas celle-là.

## 2.4 Ce qui rend un renseignement exploitable

Quatre conditions. Elles sont cumulatives.

| Condition | Question de contrôle | Si elle manque |
|---|---|---|
| **Il répond à une question posée** | Qui l'a demandé ? | Le produit ne sera pas lu |
| **Il arrive à temps** | La décision est-elle encore ouverte ? | Le produit est un constat historique |
| **Il est calibré** | Que sait-on, que suppose-t-on ? | Le destinataire ne peut pas doser sa réaction |
| **Il indique ce qu'il implique** | Qu'est-ce qui change ? | Le destinataire doit refaire le travail |

🧪 **EN PRATIQUE — le test des quatre questions**

Avant de diffuser un produit, quel qu'il soit, passez ces quatre questions. Le test prend deux minutes et évite l'essentiel des produits inutiles.

```
1. Qui l'a demandé, et pour décider quoi ?
2. Cette décision est-elle encore ouverte au moment où j'envoie ?
3. Ai-je distingué ce que j'observe de ce que j'estime ?
4. Le destinataire saura-t-il quoi faire différemment ?
```


Un produit qui échoue à la question 1 ne doit pas être envoyé — il doit d'abord trouver son destinataire. Un produit qui échoue à la question 4 doit être réécrit.

## 2.5 Renseignement et vérité

Une clarification nécessaire, parce qu'elle heurte le sens commun.

> **Un renseignement peut être excellent et faux. Un renseignement peut être exact et sans valeur.**

**Excellent et faux** : une évaluation fondée sur les meilleures sources disponibles, calibrée honnêtement, avec une confiance correctement exprimée, peut se révéler erronée. Ce n'est pas un échec analytique si le raisonnement était sain et l'incertitude déclarée. C'est le fonctionnement normal d'une discipline qui travaille sur de l'information incomplète.

**Exact et sans valeur** : une affirmation parfaitement vraie sur une menace qui ne vous concerne pas, ou qui arrive après la décision, ou que vous ne pouvez pas exploiter, ne vaut rien — quelle que soit sa justesse.

**Ce qu'on juge chez un analyste** n'est donc pas son taux d'exactitude brut. C'est :

| Critère | Question |
|---|---|
| La qualité du raisonnement | Les hypothèses ont-elles été envisagées ? Les sources évaluées ? |
| L'honnêteté du calibrage | La confiance annoncée correspondait-elle à la solidité réelle ? |
| L'utilité | La décision a-t-elle été meilleure ? |
| **La capacité à réviser** | Quand l'analyste a eu tort, l'a-t-il vu, dit et compris ? |

⚠️ Le quatrième critère est celui qui distingue un analyste qui progresse d'un analyste qui se contente d'avoir eu raison souvent. C'est l'objet du §35.6.

## 2.6 🔴 FIL ROUGE — avril 2029 : « nous suivons déjà l'actualité »

La note de Claire Nadeau (§1.10) est examinée au comité de direction du 4 avril. La demande — un poste à temps plein pendant douze mois — rencontre une objection prévisible, formulée par le directeur financier :

> *« Nous suivons déjà l'actualité de la sécurité. Malik lit les publications, nous recevons les bulletins, nous avons un flux d'indicateurs dans notre outil de protection. Qu'est-ce qu'une personne de plus apporterait ? »*

L'objection est de bonne foi, et elle est exactement la confusion du §1.4. Claire ne répond pas en théorie. Elle prend un exemple réel, survenu six semaines plus tôt.

**Ce qui existait** — étape 3, connaissance :

> *Un bulletin d'un centre de réponse national, reçu le 18 février, signalait une vulnérabilité critique activement exploitée sur une famille de passerelles d'accès distant.*

Ce bulletin a été reçu. Il a été lu par deux personnes. Il n'a produit aucune action.

**Ce qui aurait été du renseignement** — étape 4 :

> *Notre passerelle appartient à la famille concernée. Elle est publiée sur Internet par nécessité fonctionnelle et utilisée par 210 collaborateurs. La version installée est affectée. Un correctif est disponible depuis le 17 février.*

**Ce qui aurait été un jugement analytique** — étape 5 :

> *Nous estimons élevée la probabilité que cette passerelle soit sondée dans les jours qui viennent, l'exploitation étant automatisée et notre service étant découvrable publiquement — confiance élevée, l'exploitation étant confirmée par la source d'origine et notre exposition étant vérifiée.*

**Le fait qui emporte la décision.** Claire vérifie l'inventaire : le correctif a été appliqué le 3 mars, treize jours après la publication du bulletin, dans le cadre de la campagne mensuelle ordinaire de maintien en condition de sécurité. Pas parce que quelqu'un avait rapproché le bulletin de l'inventaire — **personne ne l'avait fait** — mais parce que le processus de correctifs a fini par y arriver.

> *« Nous avons eu de la chance pendant treize jours, dit-elle. Ce n'est pas une capacité, c'est un délai. »*

**La décision prise.** Le poste est validé pour douze mois, avec une condition posée par Karim Lebrun : à l'issue de la période, la fonction devra démontrer **quelles décisions ont été prises différemment**. Claire accepte — c'est exactement la mesure qu'elle aurait proposée, et elle le dit.

**Livrable de l'épisode.** Une fiche de poste, et un engagement écrit sur le critère d'évaluation à douze mois. Ce critère structurera tout le fil rouge, jusqu'au chapitre 35.

**Le recrutement.** Nour Belkacem prend ses fonctions le 2 mai 2029. Analyste, cinq ans d'expérience dans un centre opérationnel de sécurité, jamais occupé un poste de CTI. Sa première semaine est décrite au chapitre 5.

→ La suite en 🔴 §3.6, quand Nour découvrira qu'elle produit pour trois publics qui n'attendent pas la même chose.

## 2.7 ✅ Livrable — Grille de qualification d'un produit reçu

À appliquer à tout produit de renseignement que vous recevez : bulletin, rapport de fournisseur, publication de chercheur, note d'un partenaire.

| Question | Réponse | Ce qu'elle détermine |
|---|---|---|
| À quelle étape se situe ce produit ? | ☐ donnée ☐ information ☐ connaissance ☐ renseignement ☐ jugement | Le travail qu'il vous reste à faire |
| Contient-il quelque chose qui m'est propre ? | ☐ oui ☐ non | Si non : c'est de la connaissance, pas du renseignement |
| Les faits sont-ils distingués des appréciations ? | ☐ oui ☐ non ☐ partiellement | La confiance que je peux lui accorder |
| Un niveau de confiance est-il exprimé ? | ☐ oui ☐ non | S'il faut le demander ou l'estimer moi-même |
| Le produit dit-il ce qui l'invaliderait ? | ☐ oui ☐ non | La maturité de la source |
| Quelle décision cela devrait-il éclairer chez nous ? | *(à écrire)* | Si aucune : archiver, et le tracer |
| Que dois-je ajouter pour en faire du renseignement ? | *(à écrire)* | **Votre valeur ajoutée** |

**La dernière ligne est celle qui compte.** Elle vous rappelle qu'un produit reçu, aussi bon soit-il, s'arrête à l'étape 3. Le passage à l'étape 4 est votre travail, et personne d'autre ne peut le faire.

## Synthèse mentale du chapitre 2

Cinq objets se succèdent sur un même fait : la donnée est brute et vérifiable, l'information la met en contexte, la connaissance l'intègre à un ensemble extérieur, le renseignement la rapporte à votre situation et à une décision, le jugement analytique conclut avec une confiance exprimée et dit ce qui l'invaliderait. À mesure qu'on progresse, on gagne en utilité et on perd en vérifiabilité — c'est un échange qu'il faut assumer, et deux dérives symétriques en découlent : refuser de juger, ou juger sans le dire, la seconde étant la plus dangereuse. Les deux dernières étapes sont le cœur du métier, et personne ne peut les produire à votre place : un fournisseur vend de la connaissance, jamais du renseignement, parce qu'il ignore votre exposition et vos décisions en cours. Enfin, un renseignement peut être excellent et faux, ou exact et sans valeur : ce qu'on juge chez un analyste n'est pas son taux d'exactitude mais la qualité de son raisonnement, l'honnêteté de son calibrage et sa capacité à réviser.

**Trois questions de vérification**

1. Un fournisseur vous livre un rapport de trente pages sur une campagne. À quelle étape des cinq se situe-t-il, et que devez-vous y ajouter ?
2. Pourquoi une organisation qui dépense beaucoup en flux et peu en analyse achète-t-elle de la connaissance en croyant acheter du renseignement ?
3. Une évaluation s'est révélée fausse six mois plus tard. Comment jugez-vous le travail de l'analyste, et sur quels critères ?

→ **Chapitre 3 — Les trois niveaux** : pourquoi un indicateur technique n'intéresse pas une direction générale, et pourquoi une tendance géopolitique n'aide pas à écrire une règle de détection.

---
