---
title: Chapitre 10 — Évaluer une source et une information
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 10.1 Fiabilité et crédibilité : deux axes à ne jamais fusionner

C'est la distinction structurante du chapitre, et elle est l'équivalent, côté sources, des trois axes du chapitre 9.

| Axe | Porte sur | Question |
|---|---|---|
| **Fiabilité** | La **source** | Cette source s'est-elle montrée exacte par le passé ? A-t-elle un intérêt dans l'affaire ? Est-elle en position de savoir ? |
| **Crédibilité** | L'**information** | Cette affirmation précise est-elle plausible, cohérente, corroborée ? |

**Pourquoi les séparer** : une source fiable peut transmettre une information fausse — parce qu'elle a été trompée, parce qu'elle rapporte sans vérifier, parce qu'elle se trompe cette fois-ci. Et une source douteuse peut transmettre une information exacte.

**Les quatre combinaisons, avec ce qu'elles impliquent :**

| Fiabilité | Crédibilité | Situation | Traitement |
|---|---|---|---|
| Élevée | Élevée | Le cas confortable | Utilisable, en citant |
| Élevée | **Faible** | Une source sérieuse rapporte quelque chose d'invraisemblable | **Le cas le plus intéressant** : chercher pourquoi. Souvent une reprise non vérifiée |
| **Faible** | Élevée | Une source douteuse dit quelque chose de très plausible | Utilisable **si corroboré** — le danger est que la plausibilité tienne lieu de vérification |
| Faible | Faible | — | Écarter, et le tracer |

⚠️ **PIÈGE — l'auréole de la source**
Une source réputée bénéficie d'un crédit qui s'étend à tout ce qu'elle publie, y compris à ce qu'elle rapporte sans l'avoir établi. Un éditeur excellent sur l'analyse technique n'est pas nécessairement rigoureux sur l'attribution ; une agence fiable sur son propre périmètre peut relayer sans filtre ce qui vient d'ailleurs. **La fiabilité s'évalue par domaine, pas globalement.**

## 10.2 Les grilles de cotation, et leur usage réel

Il existe des grilles classiques croisant un axe de fiabilité de source, noté de A à F, et un axe de crédibilité de l'information, noté de 1 à 6. On obtient des cotations du type `B2` ou `C3`.

**Ce qu'elles apportent** : un vocabulaire commun, une discipline d'évaluation, et une trace.

**Leurs limites pratiques, qu'il faut connaître avant de les adopter :**

| Limite | Manifestation |
|---|---|
| La cotation devient mécanique | On note `B2` par habitude, sans réévaluer |
| L'échelle est trop fine | Six niveaux sur chaque axe donnent 36 combinaisons ; personne ne distingue un `C3` d'un `C4` |
| Elle masque le raisonnement | La cote remplace l'explication, alors qu'elle devrait l'accompagner |
| Elle est rarement lue | Le destinataire voit `B2` et n'en fait rien, faute de connaître l'échelle |

✅ **BONNE PRATIQUE (P1) — la version courte qui fonctionne**
Dans une organisation qui débute, une échelle à trois niveaux par axe suffit, **accompagnée d'une phrase**. Ce qui importe n'est pas la finesse de la cote, c'est que l'évaluation ait été **faite consciemment** et qu'elle soit **explicable**.

> *Source : éditeur spécialisé, fiable sur l'analyse technique, sans exposition connue sur ce sujet — fiabilité **élevée**.*
> *Information : affirmation sur le ciblage sectoriel, non détaillée, sans élément à l'appui — crédibilité **moyenne**.*

## 10.3 La chaîne de provenance

**Le principe** : pour toute affirmation importante, savoir **qui l'a dite le premier**, sur quelle base, et par combien de mains elle est passée avant d'arriver à vous.

**Pourquoi c'est le travail le plus rentable du chapitre** : chaque reprise dégrade l'information selon le mécanisme du §4.6 — perte du mode, perte des réserves, perte de la base factuelle. Après trois reprises, une hypothèse prudente est devenue un fait.

🧪 **EN PRATIQUE — remonter une chaîne en quatre questions**

```
1. Qui affirme ceci dans le document que je lis ?
2. Ce document cite-t-il une source ? Laquelle, précisément ?
3. Cette source dit-elle la même chose, avec le même mode et les mêmes réserves ?
4. Sur quoi la source d'origine fonde-t-elle son affirmation ?
```


La quatrième question est celle qui s'arrête le plus souvent sur du vide. Il est fréquent d'arriver, au bout de la chaîne, à une affirmation sans base explicite — non par malhonnêteté, mais parce que l'auteur d'origine disposait d'éléments qu'il n'a pas publiés, ou qu'il exprimait une appréciation.

**Ce qu'on écrit alors** : *« affirmation d'origine non étayée publiquement ; nous ne pouvons pas évaluer sa base »*. C'est une conclusion parfaitement recevable, et elle est infiniment plus utile que la reprise.

## 10.4 ⚠️ La circularité

Le piège le plus coûteux du métier, parce qu'il produit exactement la sensation qu'on recherche : la confirmation.

**Le mécanisme** :

```
        Une source primaire publie une évaluation prudente
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Éditeur A       Presse B        Chercheur C
   la reprend      la reprend      la reprend
        │               │               │
        └───────────────┼───────────────┘
                        ▼
         Vous lisez trois sources qui "concordent"
                        │
                        ▼
          Vous concluez à une forte corroboration
```


**Ce qui rend le piège efficace** : les trois reprises emploient des formulations différentes, citent parfois d'autres éléments périphériques, et arrivent à des dates différentes. Rien, en surface, ne signale qu'il s'agit d'une source unique.

**Les quatre signaux qui doivent alerter :**

| Signal | Pourquoi il compte |
|---|---|
| Les trois sources publient dans un intervalle court | Une reprise est rapide ; une observation indépendante l'est rarement |
| Aucune n'apporte d'élément factuel propre | Elles reprennent le même corpus d'exemples |
| Les tournures se ressemblent | Y compris les précautions et les chiffres |
| **Aucune ne cite les deux autres** | Elles citent toutes la même quatrième |

**Le test décisif** : *si je retirais la source X, resterait-il quelque chose ?* Si la réponse est non, vous avez une source, pas trois.

**Le cas particulier de la reprise croisée.** Il arrive que A cite B et que B cite A — chacun renforçant l'autre sans qu'aucune observation nouvelle n'existe. C'est plus rare et plus difficile à détecter, et cela suppose de lire les notes de bas de page.

🎯 **ET MAINTENANT ?**
*Trois publications de trois éditeurs différents, parues en dix jours, affirment qu'un acteur cible votre secteur. Que faites-vous avant d'y croire ?*
**Réponse** : vous ouvrez les trois et vous cherchez les références. Quinze minutes. Trois issues possibles : elles citent toutes la même source antérieure — vous avez **une** source, et vous l'écrivez ; chacune apporte des victimes ou des observations distinctes — vous avez une vraie corroboration, et votre confiance monte ; aucune ne cite quoi que ce soit — vous avez **zéro** source évaluable, ce qui est la situation la plus fréquente et la moins reconnue.

## 10.5 Les sources intéressées

Toute source a un intérêt. Le savoir ne disqualifie personne — l'ignorer fausse l'évaluation.

| Type de source | Intérêt structurel | Ce que cela produit | Ce qu'elle apporte malgré tout |
|---|---|---|---|
| **Éditeur de sécurité** | Vendre un produit ou un service | Une menace décrite comme plus large, plus sophistiquée ou plus nouvelle qu'elle ne l'est | La meilleure analyse technique disponible, souvent |
| **Autorité publique** | Alerter, mais aussi protéger ses sources et ses relations | Des informations solides mais partielles, des attributions prudentes ou absentes | Une fiabilité élevée sur ce qu'elle affirme |
| **Victime** | Préserver sa réputation, limiter sa responsabilité | Une minimisation, ou l'insistance sur la sophistication de l'attaque | Le seul témoignage direct |
| **Chercheur indépendant** | Reconnaissance, publication | Parfois une survalorisation d'une découverte mineure | Une profondeur technique rare |
| **Presse** | Audience | Amplification, raccourcis, pertes de nuance | Une alerte rapide |
| **Fournisseur de renseignement** | Justifier son abonnement | Un volume et une couverture mis en avant | Un accès à des sources non publiques |

**Le cas de la victime mérite une remarque** : l'insistance sur la sophistication de l'attaque est un mécanisme bien identifié — une attaque sophistiquée est moins imputable à une négligence. Cela ne signifie pas que le témoignage soit faux ; cela signifie que l'adjectif « sophistiquée » doit être traité comme une appréciation intéressée, et remplacé par une description des techniques employées.

📌 **Ce qu'il ne faut pas en conclure.** L'existence d'un intérêt ne justifie pas le cynisme. Un éditeur qui vend une solution produit régulièrement l'analyse technique la plus rigoureuse du marché sur un sujet donné. La bonne posture n'est pas la défiance mais **la lecture différenciée** : on retient l'analyse technique, on interroge l'évaluation de portée.

## 10.6 Évaluer une publication commerciale

Sept questions, dans l'ordre. Elles prennent dix minutes et évitent l'essentiel des erreurs.

| # | Question | Ce qu'elle révèle |
|---|---|---|
| 1 | **La méthodologie est-elle décrite ?** | Une publication qui ne dit pas comment elle a obtenu ses données ne peut pas être évaluée |
| 2 | **Les faits sont-ils distingués des évaluations ?** | Le §4.1, appliqué à autrui |
| 3 | **Des niveaux de confiance sont-ils exprimés ?** | Signe de maturité analytique |
| 4 | **Les chiffres ont-ils un dénominateur ?** | « 300 % d'augmentation » sur quelle base, quel périmètre, quelle méthode de comptage ? |
| 5 | **Le périmètre d'observation est-il déclaré ?** | Un éditeur observe **sa** télémétrie : ses clients, ses secteurs, ses géographies |
| 6 | **Y a-t-il une conclusion commerciale ?** | Sa présence ne disqualifie pas ; son absence de séparation, si |
| 7 | **La publication dit-elle ce qu'elle ne sait pas ?** | Le meilleur indicateur de fiabilité, et le plus rare |

⚠️ **PIÈGE — le biais de télémétrie**
Un éditeur constate ce que ses capteurs voient, chez ses clients. Si sa clientèle est majoritairement composée de grandes organisations d'un secteur donné, ses statistiques décriront ce secteur — et pas la menace en général. Ce biais n'est pas une malhonnêteté : c'est une propriété structurelle de toute observation. Ce qui est fautif, c'est de ne pas déclarer son périmètre.

## 10.7 ⏱ Évaluer une affirmation sur une menace nouvelle

*Bloc daté. Vérifié le 2 août 2026.*

Le cas particulier des menaces émergentes mérite un traitement à part, parce que c'est là que l'écart entre la couverture et les faits établis est le plus grand.

**Le mécanisme observé** : une capacité nouvelle apparaît · un premier cas documenté est publié · la couverture s'emballe · des affirmations générales circulent — « les attaquants utilisent désormais X » — sans que le nombre de cas documentés ait augmenté.

**Les quatre questions à poser à toute affirmation sur une menace nouvelle** :

| # | Question | Ce qu'elle établit |
|---|---|---|
| 1 | **Combien de cas documentés ?** | Un cas n'est pas une tendance |
| 2 | **Documentés par qui, et avec quel accès ?** | Une observation directe ou une reprise ? |
| 3 | **Qu'est-ce qui change réellement dans le mode opératoire ?** | Une capacité nouvelle, ou une automatisation de ce qui existait ? |
| 4 | **Qu'est-ce que cela change pour ma défense ?** | Souvent : rien de nouveau |

**La quatrième est la plus importante et la moins posée.** Une nouveauté qui ne modifie ni le vecteur d'entrée, ni les techniques employées, ni les mesures de défense pertinentes est un sujet d'analyse intéressant et une non-information opérationnelle.

⏱ **Illustration au 2 août 2026.** Des entrées documentant l'emploi de modèles de langage par des attaquants ont été intégrées aux référentiels publics de modes opératoires — décrivant à la fois des opérations largement automatisées et un maliciel interrogeant un modèle en cours d'exécution. 📎 [S-02]

> **Note de transparence.** L'un de ces cas documentés concerne un usage détourné de Claude, l'assistant développé par Anthropic — l'organisation qui m'a créé. Je le mentionne pour que vous puissiez en tenir compte dans votre lecture. Ce cours traite ce cas exactement comme les autres, à partir des sources publiques.

**Appliquons les quatre questions à ce sujet**, à titre d'exercice :

| Question | Réponse au 2 août 2026 |
|---|---|
| Combien de cas documentés ? | **Un petit nombre**, individuellement documentés |
| Par qui ? | Par les fournisseurs des modèles concernés, avec un accès direct à leur télémétrie — donc une observation de première main, sur **leur** périmètre |
| Qu'est-ce qui change dans le mode opératoire ? | Principalement une **automatisation et une accélération** d'étapes existantes ; les techniques d'intrusion documentées restent celles des référentiels |
| Qu'est-ce que cela change pour ma défense ? | **Peu de choses à ce stade** : les vecteurs d'entrée et les mesures pertinentes sont inchangés. L'effet principal est une possible réduction des délais |

**La conclusion analytique honnête** ressemble donc à ceci :

> *Nous estimons **probable** que l'emploi de modèles de langage réduise les délais entre la découverte d'une vulnérabilité et son exploitation à grande échelle — **confiance faible**, le nombre de cas documentés étant restreint et l'observation provenant d'un petit nombre d'acteurs disposant d'un accès privilégié à leur propre télémétrie.*
>
> *Nous n'identifions à ce stade aucune modification des mesures de défense pertinentes. Le sujet appelle une surveillance, pas une réorientation.*

**Ce que cet exemple enseigne**, au-delà de son objet : une menace peut être réelle, correctement documentée, et **sans conséquence opérationnelle immédiate**. Savoir écrire cela est une compétence — et c'est l'inverse de ce que produit la pression médiatique.

## 10.8 ✅ Livrable — Fiche d'évaluation de source

| Champ | Contenu |
|---|---|
| Identification de la source | Nom, type, date de publication |
| **Position pour savoir** | La source est-elle en mesure d'observer ce qu'elle rapporte ? |
| **Intérêt identifié** | Commercial, réputationnel, institutionnel, aucun apparent |
| **Fiabilité** | Élevée / moyenne / faible — **et pourquoi, en une ligne** |
| Historique | Cette source s'est-elle montrée exacte par le passé, sur ce domaine ? |
| **Chaîne de provenance** | Source primaire ou reprise ? Si reprise : de qui, en combien de mains ? |
| **Indépendance** | Cette source est-elle indépendante des autres dont je dispose ? |
| Méthodologie déclarée | Oui / non / partielle |
| Périmètre d'observation déclaré | Oui / non |
| **Crédibilité de l'information** | Élevée / moyenne / faible — **et pourquoi** |
| Éléments propres apportés | Ce que cette source ajoute et qu'aucune autre n'apporte |
| Décision | Utilisable / utilisable si corroboré / à écarter — avec motif |

**La ligne « éléments propres » est le test final.** Une source qui n'apporte aucun élément que vous n'ayez déjà n'augmente pas votre confiance, quelle que soit sa réputation.

## 10.9 🔬 Mini-lab 4 — Trois sources, ou une seule ?

**Objectif** — Reconstituer une chaîne de provenance et détecter une circularité.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §10.3, §10.4, §4.6 · **Livrable** chaîne de provenance + évaluation de confiance révisée
**Compétences validées** — ✔ remonter une chaîne de provenance ✔ détecter une circularité ✔ distinguer corroboration réelle et apparente ✔ requalifier une confiance ✔ écrire une évaluation sur source unique

**Le dossier fourni** — quatre extraits, dans l'ordre où ils vous parviennent.

> **Extrait 1 — Publication d'un éditeur de sécurité, 12 janvier**
> *« Notre équipe évalue avec une confiance modérée que le groupe désigné TEMPEST-14 a étendu son ciblage au secteur des équipements médicaux. Cette évaluation repose sur l'observation, chez un client, d'une infrastructure présentant des similarités avec celle décrite dans notre rapport de septembre. Nous n'avons pas identifié de victime confirmée dans ce secteur. »*

> **Extrait 2 — Article de presse spécialisée, 15 janvier**
> *« Le groupe TEMPEST-14 cible désormais le secteur des équipements médicaux, selon une analyse publiée cette semaine par un éditeur de sécurité. Cette extension du périmètre de ciblage inquiète les acteurs du secteur. »*

> **Extrait 3 — Bulletin d'un dispositif de partage sectoriel, 19 janvier**
> *« Plusieurs sources publiques font état d'un ciblage du secteur des équipements médicaux par le groupe TEMPEST-14. Les membres sont invités à renforcer leur vigilance. »*

> **Extrait 4 — Note d'un cabinet de conseil, 26 janvier**
> *« Il est établi que TEMPEST-14 mène une campagne contre les fabricants d'équipements médicaux. Les organisations du secteur doivent considérer qu'elles figurent parmi les cibles potentielles. »*

**Questions**
(a) Reconstituez la chaîne de provenance.
(b) Combien de sources indépendantes ?
(c) Que devient l'affirmation à chaque étape ?
(d) Quel niveau de confiance retenez-vous ?
(e) Rédigez l'évaluation à destination de votre RSSI.

---

**Corrigé commenté**

**(a) La chaîne**

```
Extrait 1 (12 janv.) — ÉDITEUR — source primaire
   │  Base : une observation chez un client. Aucune victime confirmée.
   │  Mode : "évalue avec une confiance modérée"
   ▼
Extrait 2 (15 janv.) — PRESSE — reprise, cite l'éditeur
   │  Mode perdu : "cible désormais" (affirmation)
   │  Réserve perdue : la mention "aucune victime confirmée" disparaît
   │  Ajout non factuel : "inquiète les acteurs du secteur"
   ▼
Extrait 3 (19 janv.) — DISPOSITIF SECTORIEL — reprise, ne cite personne
   │  "Plusieurs sources publiques" : formulation qui masque une source unique
   ▼
Extrait 4 (26 janv.) — CABINET — reprise, ne cite personne
      "Il est établi que" : le maximum de certitude, sur la base la plus faible
```


**(b) Une seule source indépendante** : l'éditeur. Les trois autres sont des reprises successives, dont deux ne citent personne.

**Le signal le plus fort** est l'extrait 3 : *« plusieurs sources publiques »*. C'est une formulation qui décrit un nombre de **publications**, pas un nombre d'**observations**. Elle est fréquente, et elle est le principal vecteur de circularité dans les dispositifs de partage — non par malhonnêteté, mais parce que celui qui rédige a effectivement lu plusieurs textes.

**(c) La dégradation, en quatre étapes**

| Extrait | Statut de l'affirmation | Ce qui a été perdu |
|---|---|---|
| 1 | Évaluation, confiance modérée, base déclarée, réserve explicite | — |
| 2 | Affirmation | Le mode · la réserve « aucune victime confirmée » |
| 3 | Affirmation, avec pluralisation des sources | La source unique · toute base factuelle |
| 4 | **Fait établi** | Tout. « Il est établi » sur une observation d'infrastructure similaire chez un client |

C'est le §4.6 en action, sur quatorze jours.

**(d) Le niveau de confiance**

**Faible.** Justification, en une ligne comme le veut le §9.4 : *source unique, évaluation d'origine elle-même modérée, aucune victime confirmée dans le secteur, base factuelle limitée à une similarité d'infrastructure.*

⚠️ **L'erreur à ne pas commettre** : conclure que l'information est fausse. Rien ne permet de le dire. L'éditeur a peut-être raison. Ce que l'exercice établit, ce n'est pas la fausseté de l'affirmation — c'est que **le nombre de publications ne dit rien de sa solidité**.

**(e) L'évaluation attendue**

> *Quatre publications font état d'un ciblage du secteur des équipements médicaux par un acteur désigné TEMPEST-14. **Nous n'identifions qu'une seule source primaire** : l'évaluation d'un éditeur du 12 janvier, elle-même donnée avec une confiance modérée, fondée sur une similarité d'infrastructure observée chez un client, et précisant qu'aucune victime du secteur n'a été confirmée. Les trois autres publications en dérivent.*
>
> *Nous estimons **aussi probable qu'improbable** que ce ciblage soit avéré — **confiance faible**, pour les raisons ci-dessus.*
>
> *Nous ne recommandons pas de mobilisation. Nous recommandons deux vérifications : demander à l'éditeur si des victimes ont été confirmées depuis le 12 janvier · interroger le dispositif sectoriel sur l'existence d'observations propres à ses membres.*
>
> *Cette évaluation serait révisée à la hausse si une victime du secteur était confirmée par une source disposant d'une observation directe.*

**Les trois erreurs attendues**

1. **Compter quatre sources.** C'est l'objet du lab, et c'est ce que fait la majorité des lecteurs en première lecture.
2. **Conclure que l'information est fausse.** L'exercice porte sur la solidité de la base, pas sur la véracité.
3. **Ne pas remarquer la perte de la réserve.** La disparition, entre les extraits 1 et 2, de la mention *« nous n'avons pas identifié de victime confirmée »* est la transformation la plus lourde de conséquence — et c'est une suppression, pas une déformation, donc elle est invisible sans comparaison.

## 10.10 🔴 FIL ROUGE — novembre 2029 : deux sources qui n'en font qu'une

Nour prépare une évaluation pour le comité de sécurité du 21 novembre. Le sujet : une technique d'accès initial signalée comme employée contre des organisations de santé européennes.

Elle dispose de trois publications. Elle applique la procédure du §10.3 — désormais systématique depuis l'épisode de juin (§4.9).

| Publication | Date | Ce qu'elle cite | Éléments propres |
|---|---|---|---|
| Éditeur A | 4 nov. | Rien | **Trois victimes, avec dates et pays** |
| Éditeur B | 9 nov. | « des observations récentes » | Aucun |
| Chercheur C | 12 nov. | Éditeur A, explicitement | **Une analyse technique du mécanisme** |

**Le cas de l'éditeur B** est le plus instructif. Il ne cite personne, emploie une formulation vague, et n'apporte aucune victime, aucune date, aucun élément technique. Nour lui écrit — deux lignes, une question : *votre publication du 9 novembre repose-t-elle sur des observations propres ?*

**La réponse, reçue en trois jours** : non. Elle repose sur la publication de l'éditeur A, qui n'est pas citée parce que « l'usage ne l'impose pas dans ce format ».

**Le résultat de l'évaluation** :

| | Avant vérification | Après |
|---|---|---|
| Sources apparentes | 3 | 3 |
| **Sources indépendantes** | 3 | **2** |
| Éléments factuels distincts | ? | 3 victimes (A) + 1 analyse technique (C) |
| Confiance retenue | *aurait été* élevée | **moyenne** |

**Ce qui change concrètement.** L'éditeur C est une corroboration réelle — il apporte une analyse technique indépendante du mécanisme, qu'il a produite lui-même. L'éditeur B n'ajoute rien. La confiance passe d'élevée à moyenne, et l'évaluation le dit explicitement.

**La question posée en comité par Claire** : *« si tu n'avais pas écrit à l'éditeur B, qu'aurais-tu conclu ? »*

Réponse de Nour : confiance élevée, sur trois sources. Coût de la vérification : deux lignes de courriel et trois jours d'attente.

**La décision prise.** Une règle est ajoutée au processus : **toute source qui n'apporte aucun élément factuel propre est traitée comme une reprise jusqu'à preuve du contraire**, et cette qualification figure dans l'évaluation. Si l'origine peut être vérifiée à peu de frais, on vérifie ; sinon, on écrit le doute.

**L'effet secondaire, observé sur six mois.** Nour prend l'habitude d'écrire aux éditeurs. Sur onze demandes, elle obtient neuf réponses. Deux d'entre elles conduisent à des échanges réguliers, et l'un des éditeurs finit par lui transmettre des éléments avant publication. **La vérification de source est devenue une source.**

> *« Je pensais que vérifier m'isolerait, écrit-elle. En pratique, c'est ce qui m'a fait connaître. »*

**Livrable de l'épisode.** La fiche d'évaluation de source du §10.8, intégrée au processus, avec la règle de la reprise présumée.

→ La suite en 🔴 §11.7, quand une évaluation devra dire ce qui l'invaliderait — et que cette ligne changera la décision.

## Synthèse mentale du chapitre 10

Fiabilité et crédibilité sont deux axes distincts : une source fiable peut transmettre une information fausse, et la fiabilité s'évalue par domaine, jamais globalement. Les grilles de cotation apportent un vocabulaire commun mais deviennent mécaniques ; ce qui compte n'est pas la finesse de la cote mais que l'évaluation ait été faite consciemment et soit explicable en une phrase. Remonter une chaîne de provenance est le travail le plus rentable du chapitre, et la question qui s'arrête le plus souvent sur du vide est la quatrième : sur quoi la source d'origine fonde-t-elle son affirmation ? La circularité produit exactement la sensation qu'on recherche — la confirmation — et le test décisif tient en une question : si je retirais cette source, resterait-il quelque chose ? Toute source a un intérêt, ce qui n'autorise pas le cynisme mais impose une lecture différenciée : retenir l'analyse technique, interroger l'évaluation de portée. Enfin, une menace peut être réelle, correctement documentée, et sans conséquence opérationnelle immédiate — savoir l'écrire est une compétence.

**Trois questions de vérification**

1. Un bulletin sectoriel affirme que « plusieurs sources publiques font état de… ». Pourquoi cette formulation doit-elle déclencher une vérification, et laquelle ?
2. Un éditeur publie des statistiques montrant une hausse de 300 % d'un type d'attaque. Quelles deux questions posez-vous avant d'utiliser ce chiffre ?
3. Une source réputée affirme quelque chose d'invraisemblable. Est-ce le cas le plus embarrassant ou le plus intéressant, et pourquoi ?

→ **Chapitre 11 — Produire un jugement analytique** : construire une évaluation qui s'engage, se conteste et se révise.

---
