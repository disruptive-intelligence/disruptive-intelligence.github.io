---
title: Chapitre 37 — Économie de la fonction
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

## 37.1 Chiffrer une fonction CTI

**Les cinq postes**, dont deux sont presque toujours omis :

| Poste | Contenu | Omis ? |
|---|---|---|
| Personnel | Le poste, ou la fraction de poste | Non |
| Sources payantes | Abonnements, adhésions | Non |
| Outillage | Plateforme, connecteurs, stockage | Non |
| **Intégration et maintenance** | Le coût récurrent de la chaîne | **Souvent** |
| **Le temps des destinataires** | Lecture, réunions, sollicitations | **Presque toujours** |

**Le cinquième mérite un calcul** : une fonction qui diffuse quatre produits par mois à sept destinataires, chacun y consacrant vingt minutes, consomme environ **quarante-cinq heures par an** de temps de cadres. Ce coût est réel, invisible, et il justifie à lui seul les chapitres 25 et 26 — un produit mal écrit coûte plus cher qu'il ne paraît.

## 37.2 Construire ou acheter

| Critère | Plutôt construire | Plutôt acheter |
|---|---|---|
| Le besoin est **spécifique à votre contexte** | ✅ | |
| Le besoin est **générique** | | ✅ |
| L'information exige un **accès non public** | | ✅ |
| Vous disposez de la **compétence** | ✅ | |
| Le besoin est **durable** | ✅ | |
| Le besoin est **ponctuel** | | ✅ |

**La règle qui découle du chapitre 2** : ce qui relève de la **connaissance** s'achète ; ce qui relève du **renseignement** ne s'achète pas, parce qu'il suppose votre contexte. Une organisation qui achète du renseignement achète en réalité de la connaissance et devra faire le reste elle-même.

## 37.3 Le coût caché de l'attention

**Développement du §37.1, cinquième poste.**

| Ce qui consomme l'attention | Effet |
|---|---|
| Un produit trop long | Multiplié par le nombre de destinataires |
| Un produit envoyé au mauvais destinataire | Coût pur, valeur nulle |
| Une alerte injustifiée | Coût élevé, plus l'érosion du crédit (§27.2) |
| Une question mal formulée | Le destinataire doit deviner ce qu'on attend |

**Ce que cela implique** : réduire la longueur, cibler les destinataires et restreindre les alertes ne sont pas des raffinements de style. Ce sont des **mesures d'économie**, chiffrables.

## 37.4 Défendre un budget sur une fonction à impact difficilement prouvable

**Ce qui ne fonctionne pas** :

| Argument | Pourquoi il échoue |
|---|---|
| « Nous avons évité un incident » | Invérifiable, et cela décrédibilise |
| « Tout le monde en fait » | Ne répond à aucune question |
| « La menace augmente » | Vrai, général, et sans conséquence budgétaire |
| Le volume produit | §35.3 |

**Ce qui fonctionne**, dans cet ordre :

1. **Les décisions modifiées**, avec exemples nommés (§35.5).
2. **Les mobilisations évitées**, chiffrées — c'est l'argument le plus concret, parce qu'il compare un coût évité à un coût réel.
3. **Les menaces neutralisées documentées** — elles démontrent que les investissements passés fonctionnent, ce qui sert au-delà du CTI.
4. **L'avance obtenue**, en jours, sur les sources publiques.

**L'argument le plus solide n'est pas économique.** Il est le suivant : *sans cette fonction, l'organisation ne saurait pas ce qu'elle ignore.* Il ne se chiffre pas, et il se comprend.

## 37.5 📌 Ce qu'une fonction CTI ne fera jamais économiser

Par honnêteté, et parce qu'un argumentaire qui promet trop se retourne :

- Elle ne réduit pas le budget de sécurité : elle en améliore l'allocation ;
- Elle ne remplace ni la détection, ni la remédiation, ni l'architecture ;
- Elle ne diminue pas le nombre d'incidents de façon démontrable ;
- Elle ne se substitue pas à une capacité de réponse.

**Ce qu'elle fait** : elle rend les mêmes moyens plus efficaces, en les orientant. Le §31.6 en est la démonstration la plus nette — même capacité, ordre différent, délai divisé par cinq.

## 37.6 🔴 FIL ROUGE — juin 2031 : ce que ça coûte

Après le bilan à vingt-quatre mois (§35.8), Karim Lebrun demande le chiffrage complet — pas seulement le poste, mais tout ce que la fonction consomme.

**Le calcul, sur douze mois** :

| Poste | Montant estimé |
|---|---|
| Poste de Nour, charges comprises | Le principal |
| Adhésion au dispositif sectoriel | Modeste |
| Souscription commerciale (fournisseur B) | 19 k€ |
| Outillage | Néant — un tableur structuré et l'existant |
| Intégration et maintenance | ≈ 4 jours-homme/an |
| **Temps des destinataires** | **≈ 52 heures/an**, soit environ 1,5 semaine cumulée |

**Ce que le poste « temps des destinataires » provoque.** Karim Lebrun ne l'avait jamais vu chiffré. Sa réaction n'est pas celle attendue :

> *« Cinquante-deux heures de cadres pour trente et une décisions, ça me paraît très bon marché. Ce qui m'intéresse, c'est de savoir si ces cinquante-deux heures sont bien réparties. »*

**La question déclenche une analyse** : qui consomme les cinquante-deux heures ?

| Destinataire | Temps annuel estimé | Décisions produites |
|---|---|---|
| Malik Ferhaoui (MCS) | 14 h | **14** |
| Référent détection | 11 h | 4 |
| Yann Prigent (produit) | 9 h | 5 |
| Claire Nadeau (RSSI) | 8 h | 6 |
| Sonia Weber (DSI) | 5 h | 2 |
| **Comité de direction** | **9 h** | **0** |
| Dr Hélène Fabre | 0 h | 0 |

**La ligne du comité de direction** : neuf heures cumulées, zéro décision documentée. Les produits stratégiques — quatre en deux ans — ont été lus, et n'ont modifié aucun arbitrage.

**Ce que Nour en conclut**, sans se défendre :

> *Le besoin B-04, orientation des investissements, est le seul de mes besoins qui n'a jamais produit de décision. J'ai mis vingt-quatre mois à l'admettre. Soit je le sers correctement, soit je l'abandonne — mais je ne peux pas continuer à produire quatre notes par an que personne n'utilise.*

**La décision prise** : le besoin B-04 est **reformulé une dernière fois**, avec une échéance ferme calée sur le calendrier budgétaire et un format différent — une présentation orale de quinze minutes en comité, avec une question explicite, plutôt qu'une note écrite. Si aucune décision n'en résulte en 2032, il est abandonné et l'annexe des besoins non couverts le mentionnera.

**Ce que Claire écrit au compte rendu** :

> *« Nous avons passé deux ans à démontrer ce que la fonction produit. Le chiffrage nous a appris ce qu'elle ne produit pas. C'est aussi utile. »*

**Livrable de l'épisode.** Le chiffrage complet en six postes, dont le temps des destinataires, et son croisement avec les décisions produites — annexe K.

→ La suite en 🔴 §38.5, quand la fonction devra décider où elle se rattache.

## Synthèse mentale du chapitre 37

Cinq postes composent le coût d'une fonction CTI, et deux sont presque toujours omis : la maintenance de la chaîne, et surtout **le temps des destinataires** — quarante à cinquante heures de cadres par an dans une organisation moyenne, ce qui fait de la brièveté et du ciblage des mesures d'économie chiffrables plutôt que des raffinements de style. Ce qui relève de la connaissance s'achète, ce qui relève du renseignement ne s'achète pas, parce qu'il suppose votre contexte. Défendre un budget se fait par les décisions modifiées et les mobilisations évitées chiffrées, jamais par les incidents évités — invérifiables et décrédibilisants. Une fonction CTI ne réduit pas le budget de sécurité, elle en améliore l'allocation : mêmes moyens, ordre différent. Enfin, le chiffrage apprend autant sur ce que la fonction ne produit pas que sur ce qu'elle produit — un besoin qui consomme du temps sans jamais produire de décision doit être servi autrement ou abandonné.

**Trois questions de vérification**

1. Quel poste de coût est presque toujours omis dans le chiffrage d'une fonction CTI, et pourquoi justifie-t-il l'exigence de brièveté ?
2. Pourquoi « nous avons évité un incident » est-il un mauvais argument budgétaire ?
3. Un destinataire consomme neuf heures par an et ne produit aucune décision. Que faites-vous, et en combien de temps devriez-vous l'avoir vu ?

---
