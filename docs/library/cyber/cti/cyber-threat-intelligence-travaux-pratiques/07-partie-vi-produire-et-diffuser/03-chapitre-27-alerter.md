---
title: Chapitre 27 — Alerter
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VI — Produire et diffuser
  - index.md
---

## 27.1 Ce qui justifie une alerte

**Une alerte est un produit qui interrompt.** C'est sa définition fonctionnelle : elle sort du rythme normal, mobilise de l'attention immédiate, et déclenche potentiellement des actions non planifiées.

**Ce statut a un coût, et ce coût est cumulatif.** Chaque alerte consomme du crédit d'attention. Une fonction qui alerte souvent obtient des réactions rapides les trois premières fois, puis de moins en moins.

**Les quatre conditions d'une alerte justifiée** — cumulatives :

| # | Condition | Question |
|---|---|---|
| **1** | **Applicabilité établie** | Cela nous concerne-t-il **factuellement** ? |
| **2** | **Urgence réelle** | Attendre le prochain point périodique aggrave-t-il la situation ? |
| **3** | **Action possible** | Le destinataire peut-il faire quelque chose maintenant ? |
| **4** | **Action nécessaire** | Ne rien faire est-il déraisonnable ? |

**La troisième est celle qu'on néglige.** Alerter sur une menace contre laquelle rien ne peut être fait immédiatement produit de l'anxiété sans produire d'action. Ce n'est pas une alerte, c'est une information — qui a sa place dans le rythme normal.

⚠️ **PIÈGE — l'alerte de couverture**
Alerter « au cas où », pour ne pas être celui qui n'a pas prévenu, est un réflexe compréhensible et destructeur. Il transfère la charge de la décision au destinataire, il consomme du crédit, et il produit exactement l'effet inverse de celui recherché : au bout de quelques mois, les alertes ne sont plus traitées avec urgence.

## 27.2 Le coût d'une fausse alerte, et celui d'une alerte manquée

**Les deux erreurs ne sont pas symétriques**, et il faut le dire clairement.

| | **Fausse alerte** | **Alerte manquée** |
|---|---|---|
| Coût immédiat | Mobilisation inutile, chiffrable | Potentiellement élevé |
| Coût différé | **Érosion du crédit** — cumulative, durable | Remise en cause de la fonction |
| Visibilité | Immédiate | Souvent invisible, sauf incident |
| Réversibilité | La confiance se reconstruit lentement | — |

**Ce que cette asymétrie implique** : le réflexe naturel est de privilégier la fausse alerte, parce que son coût est visible et paraît acceptable. Mais son coût **différé** — l'érosion du crédit — est ce qui produira, plus tard, l'alerte manquée : celle qu'on aura émise et que personne n'aura traitée avec urgence.

> **Une fonction qui alerte trop finit par ne plus être capable d'alerter.**

**Le repère pratique** : dans une organisation de taille intermédiaire, une fonction CTI mature émet de l'ordre de deux à six alertes par an. Au-delà de dix, le seuil de déclenchement est probablement trop bas — ou les conditions du §27.1 ne sont pas appliquées.

## 27.3 Formuler une alerte

**Le format**, cinq à dix lignes, sans exception.

```
① OBJET          Ce qui se passe, en une phrase calibrée
② APPLICABILITÉ  Pourquoi cela nous concerne — factuel, précis
③ DÉLAI          De quoi disposons-nous
④ ACTION         Ce que nous demandons, à qui, précisément
⑤ SUITE          Quand le prochain point aura lieu
```


**Exemple** :

> **Alerte — exploitation active d'une vulnérabilité affectant nos passerelles d'accès distant**
>
> Une vulnérabilité affectant la version installée sur nos deux passerelles fait l'objet d'une exploitation active confirmée depuis ce matin — confiance élevée, avis constructeur et signalement du centre de réponse national.
>
> **Nous sommes concernés** : version 4.2.11 installée sur GW-VPN-01 et 02, service publié sur Internet, 210 utilisateurs.
>
> **Délai** : le correctif est disponible. Nous recommandons une application cette nuit.
>
> **Ce que nous demandons** : validation par [nom] de l'interruption de service entre 22 h et 23 h.
>
> **Point suivant** : demain 9 h, ou immédiatement en cas d'élément nouveau.

⚠️ **Ce que l'exemple ne contient pas** : le nom de l'acteur, le mécanisme technique, l'historique de la campagne, les indicateurs. Tout cela suit dans un produit ultérieur. **Une alerte n'informe pas, elle déclenche.**

## 27.4 ⚠️ La fatigue d'alerte, et comment on la fabrique

**Le mécanisme**, en quatre étapes que toute organisation reconnaît :

```
1. La fonction alerte sur un sujet réel mais sans action possible
2. Le destinataire mobilise, constate qu'il n'y avait rien à faire
3. À l'alerte suivante, il attend avant de mobiliser
4. À la troisième, il traite l'alerte comme une information
```


**Les cinq façons de la fabriquer** :

| Façon | Mécanisme |
|---|---|
| Alerter sans applicabilité établie | §7.9 du fil rouge |
| Alerter sans action possible | Le destinataire subit |
| Alerter par prudence | §27.1 |
| Alerter sur une source unique non vérifiée | La rétractation détruit le crédit |
| **Ne pas clore l'alerte** | Le destinataire ne sait pas quand c'est fini |

**La cinquième est la plus négligée.** Une alerte ouverte indéfiniment maintient un état de mobilisation qui s'épuise. La clôture est une obligation : *« l'alerte du 22 juillet est close, le correctif est déployé et vérifié, aucune activité n'a été observée »*.

## 27.5 Le suivi : ce qui s'est passé après

**Trois questions, deux semaines après chaque alerte** — les mêmes que celles du §15.7 :

1. L'alerte a-t-elle été traitée dans le délai demandé ?
2. Quelle action a été engagée ?
3. **L'alerte était-elle justifiée, avec le recul ?**

**La troisième question est celle qui construit le crédit.** Une fonction qui reconnaît elle-même qu'une alerte n'était pas justifiée — comme au §7.9 — préserve sa capacité à alerter. Une fonction qui ne revient jamais dessus la perd progressivement.

✅ **BONNE PRATIQUE (P1)** — Tenez un registre des alertes avec, pour chacune, la justification a posteriori. Deux lignes. Au bout de deux ans, il constitue la meilleure démonstration de la fiabilité de la fonction — et le meilleur argument face à une direction qui demande si les alertes sont bien calibrées.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel diffuse une alerte critique. Vous vérifiez : la vulnérabilité concerne un produit que vous utilisez, mais aucun correctif n'existe et aucune mesure d'atténuation n'est identifiée. Alertez-vous ?*
**Réponse** : non — pas au sens d'une alerte. Les conditions 1 et 2 sont remplies, la 3 ne l'est pas : le destinataire ne peut rien faire maintenant. Ce que vous produisez est une **information avec un engagement** : *« vulnérabilité sans correctif affectant [produit], nous suivons quotidiennement, nous alerterons dès qu'une action sera possible — prochaine mise à jour vendredi »*. Vous avez informé sans mobiliser, et vous avez conservé votre capacité à alerter pour le moment où elle servira. C'est exactement ce que la condition 3 protège.

## 27.6 🔴 FIL ROUGE — octobre 2030 : l'alerte de trop

Entre mai et septembre 2030, Nour émet **sept alertes**. Le rythme s'est accéléré après le succès de juillet (§26.9) — l'alerte de juillet a bien fonctionné, elle a produit une mobilisation efficace, et la fonction a gagné en légitimité.

**L'alerte du 2 octobre** porte sur une campagne visant le secteur, avec une applicabilité incertaine : le vecteur décrit concerne un composant qu'HELIOMED utilise, mais dans une configuration possiblement non affectée. Nour alerte quand même, par prudence.

**Ce qui se passe** : l'exploitation prend six heures. Résultat : la configuration d'HELIOMED n'est pas affectée. Personne n'avait rien à faire.

**Ce que Claire constate deux semaines plus tard**, en préparant le comité :

| Alerte | Délai de première réaction |
|---|---|
| Mai (1ʳᵉ) | 22 minutes |
| Juin | 35 minutes |
| Juillet | 18 minutes |
| Août (2) | 1 h 10 · 2 h 40 |
| Septembre | 3 h 15 |
| **Octobre** | **6 h 20** |

**Le délai de réaction a été multiplié par dix-sept en cinq mois.** Aucun destinataire ne s'en est plaint ; personne n'a dit qu'il ne traitait plus les alertes en urgence. Le comportement a simplement changé.

**L'analyse que Nour conduit**, en reprenant les sept alertes avec les quatre conditions du §27.1 :

| Alerte | Cond. 1 applicabilité | Cond. 2 urgence | Cond. 3 action possible | Cond. 4 nécessaire | Justifiée ? |
|---|---|---|---|---|---|
| Mai | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Juin | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Juillet | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Août-1 | ✅ | ⚠️ | ✅ | ⚠️ | Discutable |
| Août-2 | ⚠️ | ✅ | ❌ | — | **Non** |
| Septembre | ✅ | ❌ | ✅ | ❌ | **Non** |
| Octobre | ❌ | ✅ | ✅ | — | **Non** |

**Trois alertes justifiées sur sept.** Les quatre autres relevaient de l'information, pas de l'alerte.

**Ce que Nour porte au comité**, sans détour :

> *J'ai émis quatre alertes qui n'en étaient pas. Le coût n'est pas les heures mobilisées — c'est que la prochaine alerte réelle mettra six heures à être traitée.*

**Les trois décisions** :

1. **Le seuil est écrit** : les quatre conditions du §27.1 doivent être toutes vérifiées, et la vérification est **tracée** dans le message d'alerte lui-même.
2. **Une catégorie intermédiaire est créée** : *information avec engagement de suivi*, qui n'interrompt pas. Elle absorbe ce qui relevait des alertes non justifiées.
3. **Le registre des alertes** est tenu, avec justification a posteriori à deux semaines.

**L'effet mesuré à six mois** : deux alertes émises entre novembre 2030 et avril 2031. Délais de première réaction : 19 et 24 minutes.

**Ce que Claire écrit au compte rendu**, et qui résume le chapitre :

> *« La capacité d'alerter n'est pas un droit acquis. C'est un crédit, et il se dépense. »*

**Livrable de l'épisode.** Le format d'alerte en cinq blocs, la catégorie « information avec engagement », et le registre avec justification a posteriori — annexe D.

→ La suite en 🔴 §28.6, quand HELIOMED devra décider ce qu'elle partage d'un incident qui la concerne.

## Synthèse mentale du chapitre 27

Une alerte est un produit qui interrompt, et ce statut consomme un crédit d'attention cumulatif : une fonction qui alerte trop finit par ne plus être capable d'alerter. Quatre conditions cumulatives la justifient, et la troisième — l'action est-elle possible maintenant ? — est celle qu'on néglige : alerter sur une menace contre laquelle rien ne peut être fait produit de l'anxiété, pas de l'action. Les deux erreurs ne sont pas symétriques : le coût d'une fausse alerte paraît acceptable parce qu'il est visible, mais son coût différé est l'érosion du crédit, laquelle produira plus tard l'alerte manquée. Une alerte tient en cinq à dix lignes et ne contient ni acteur, ni mécanisme, ni indicateurs — elle ne informe pas, elle déclenche. La clôture explicite est une obligation, faute de quoi la mobilisation s'épuise. Enfin, revenir soi-même sur une alerte injustifiée préserve la capacité à alerter ; ne jamais y revenir la détruit lentement.

**Trois questions de vérification**

1. Une vulnérabilité critique vous concerne, aucun correctif ni contournement n'existe. Alertez-vous ? Justifiez par la condition pertinente.
2. Pourquoi le coût d'une fausse alerte est-il plus élevé qu'il n'y paraît, et à quel moment se manifeste-t-il ?
3. Vos délais de réaction aux alertes s'allongent sans que personne ne se plaigne. Que se passe-t-il, et comment le diagnostiquez-vous ?

---
