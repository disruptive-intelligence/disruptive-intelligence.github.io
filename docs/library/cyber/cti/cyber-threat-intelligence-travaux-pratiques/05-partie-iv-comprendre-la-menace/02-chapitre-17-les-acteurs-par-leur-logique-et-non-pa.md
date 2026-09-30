---
title: Chapitre 17 — Les acteurs, par leur logique et non par leur nom
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE IV — Comprendre la menace
  - index.md
---

## 17.1 Une typologie par motivation et contrainte

**Le principe de ce chapitre** : ce qui est utile chez un acteur n'est pas son identité mais **ce qui le contraint** — son objectif, ses moyens, son horizon, et ce qu'il ne peut pas se permettre.

Ces quatre paramètres se déduisent de l'observation, sans jamais nommer personne. Et ils sont stables sur des années, là où les noms se périment.

| Paramètre | Question | Ce qu'il permet de prévoir |
|---|---|---|
| **Objectif** | Que cherche-t-il à obtenir ? | Ce qu'il fera une fois entré |
| **Moyens** | Que peut-il se payer ? | Le niveau de sophistication attendu |
| **Horizon** | Combien de temps peut-il attendre ? | Discrétion ou rapidité |
| **Contrainte** | Que ne peut-il pas se permettre ? | Ce qui le fera renoncer |

## 17.2 Les criminels

| Paramètre | Valeur typique |
|---|---|
| Objectif | Un gain financier, le plus rapidement possible |
| Moyens | Variables, souvent achetés plutôt que développés |
| Horizon | **Court** — quelques jours à quelques semaines dans le réseau |
| Contrainte | **La rentabilité.** Une opération non rentable est abandonnée |

**Ce que cela permet de prévoir** : un comportement opportuniste, une préférence pour le volume, une progression rapide et bruyante, un abandon face à la résistance, et une monétisation directe — chiffrement, extorsion, revente, fraude.

**La conséquence défensive la plus utile** : contre un acteur contraint par la rentabilité, **augmenter le coût suffit**. Il ne s'agit pas de rendre l'attaque impossible, mais de la rendre moins rentable que la cible suivante.

## 17.3 Les acteurs étatiques

| Paramètre | Valeur typique |
|---|---|
| Objectif | Renseignement, positionnement, parfois sabotage — **non financier** |
| Moyens | Élevés, développement propre possible |
| Horizon | **Long** — des mois, parfois des années |
| Contrainte | **La discrétion.** Être découvert a un coût politique |

**Ce que cela permet de prévoir** : une progression lente, un souci de persistance, un évitement des actions bruyantes, un ciblage sélectif, et une absence de monétisation directe.

⚠️ **PIÈGE — l'attribution étatique par sophistication**
« C'était sophistiqué, donc c'est étatique » est un raisonnement circulaire et faux. Des acteurs criminels emploient des techniques avancées ; des acteurs étatiques emploient régulièrement des techniques banales, précisément parce qu'elles fonctionnent et qu'elles ne les distinguent pas. **La sophistication n'est pas un marqueur d'origine.**

## 17.4 Les hacktivistes

| Paramètre | Valeur typique |
|---|---|
| Objectif | La visibilité d'un message |
| Moyens | Souvent limités |
| Horizon | Court, souvent aligné sur un événement |
| Contrainte | **Ils ont besoin d'être vus** |

**Ce que cela permet de prévoir** : des actions à effet visible — indisponibilité, défiguration, divulgation — plutôt qu'une persistance discrète, et une revendication.

**Le point d'attention** : la revendication est facile à usurper. Une action revendiquée par un collectif n'a pas nécessairement été conduite par lui, et une revendication peut couvrir une opération d'une autre nature.

## 17.5 La menace interne

Deux cas distincts, qu'il faut séparer.

| | **Intentionnelle** | **Accidentelle** |
|---|---|---|
| Objectif | Gain, vengeance, conviction | Aucun |
| Contrainte | Ne pas être identifié — or il l'est presque toujours | — |
| Fréquence | Rare | **Très fréquente** |
| Détectabilité | Difficile : usage d'accès légitimes | Souvent invisible |

**Le rapport de fréquence est le point à retenir.** L'erreur — configuration exposée, envoi au mauvais destinataire, service ouvert par commodité — produit bien plus d'incidents que la malveillance interne. Une fonction CTI qui consacre son attention à la seconde en négligeant la première se trompe de priorité.

## 17.6 Prestataires et chaîne d'approvisionnement

Ce n'est pas un type d'acteur mais un **chemin**, et il mérite une place ici parce qu'il modifie l'application des quatre paramètres.

**Le mécanisme** : l'adversaire n'attaque pas votre organisation, il attaque quelqu'un qui a accès à votre organisation — infogérant, éditeur, partenaire d'échange.

**Ce que cela change** :

| Aspect | Effet |
|---|---|
| Le coût d'accès | **Fortement réduit** — un prestataire donne accès à plusieurs organisations |
| Le ciblage | Vous n'êtes pas ciblé, vous êtes atteignable |
| La détection | L'activité emprunte des accès **légitimes** |
| La défense | Elle ne dépend qu'en partie de vous (le chapitre 31 du cours MCS) |

**C'est le chemin dont le rapport coût/gain est le plus favorable**, ce qui explique sa fréquence croissante — et c'est précisément le raisonnement du §16.1.

## 17.7 ⚠️ Pourquoi ce cours ne contient aucun catalogue d'acteurs

Quatre raisons, dans l'ordre d'importance.

| Raison | Explication |
|---|---|
| **Péremption** | Les acteurs se recomposent, se scindent, changent d'outillage. Un catalogue a dix-huit mois de retard le jour où il est écrit |
| **Inutilité décisionnelle** | Vos mesures ne changent pas selon l'auteur (§13.4) |
| **Illusion de maîtrise** | Connaître des noms donne le sentiment de comprendre la menace, et dispense de comprendre les mécanismes |
| **Dépendance à une source** | Les désignations diffèrent selon les éditeurs ; les adopter revient à adopter leur découpage |

**Ce qui remplace le catalogue** : les quatre paramètres du §17.1, appliqués à ce que vous observez. Ils fonctionnent sur un acteur inconnu, ce qu'un catalogue ne fait jamais.

## 17.8 Raisonner sur un acteur inconnu

C'est la situation normale. Voici la méthode, en quatre questions.

```
1. OBJECTIF    Qu'est-ce qui a été fait une fois l'accès obtenu ?
               → chiffrement, exfiltration, persistance, rien ?

2. HORIZON     Combien de temps entre l'entrée et l'action ?
               → heures = opportuniste · mois = patient

3. MOYENS      L'outillage est-il public, acheté, ou propre ?
               → public = faibles moyens ou volonté de se fondre

4. CONTRAINTE  Qu'est-ce qui a été évité ?
               → bruit évité = discrétion prioritaire
               → rien évité = rapidité prioritaire
```


**Ce que ces quatre réponses produisent** : un profil suffisant pour anticiper la suite, sans aucun nom. Et surtout, **un profil révisable** : chaque nouvelle observation ajuste un paramètre, là qu'un nom, une fois posé, résiste aux éléments contraires (§7.3).

🎯 **ET MAINTENANT ?**
*Un incident est en cours. L'équipe de réponse vous demande : « à qui on a affaire ? ». Que répondez-vous dans l'heure ?*
**Réponse** : jamais un nom. Les quatre paramètres, avec ce que vous observez. *« L'accès date d'au moins six semaines et rien n'a été chiffré : horizon long, objectif probablement non financier. L'outillage est public, ce qui n'indique pas des moyens faibles — cela peut être délibéré. Aucune action bruyante n'a été relevée : la discrétion semble prioritaire. En conséquence, nous recommandons de privilégier la recherche de persistance et l'analyse des accès plutôt que la restauration immédiate. »* Ce profil est opérationnel dans l'heure, et il oriente réellement les opérations — ce qu'un nom n'aurait pas fait.

## 17.9 🔴 FIL ROUGE — mai 2030 : « pourquoi nous ? »

Le 6 mai, HELIOMED subit une tentative d'intrusion. Le vecteur : un compte de prestataire, dont les identifiants figuraient dans une fuite publiée deux mois plus tôt. L'authentification multifacteur, active, bloque la tentative. Aucun accès n'est obtenu.

**La question que Pierre Vasseur, directeur général, pose au comité de crise** :

> *« Pourquoi nous ? Qu'est-ce qu'on a fait pour être visés ? »*

**Ce que Nour aurait pu répondre en 2029** : chercher un acteur, un ciblage, une explication narrative.

**Ce qu'elle répond**, en appliquant les quatre paramètres et le §16.4 :

> *Nous n'avons probablement pas été visés en particulier — confiance moyenne.*
>
> *Les identifiants employés proviennent d'une fuite publique de mars, contenant environ deux cent mille comptes de nombreuses organisations. La tentative a eu lieu à 04 h 12, dans une série de tentatives séquentielles sur quatorze comptes de notre domaine, tous présents dans cette fuite. Aucun compte absent de la fuite n'a été essayé.*
>
> *Ce profil correspond à une exploitation automatisée de la fuite, sans sélection préalable de cible. **Nous n'étions pas choisis, nous étions présents dans la liste.***
>
> *Ce qui invaliderait cette évaluation : la découverte de tentatives sur des comptes absents de la fuite · une reconnaissance préalable de notre infrastructure · un ciblage d'actifs spécifiques plutôt que du portail générique.*

**La vérification que cette conclusion déclenche.** Puisque l'hypothèse retenue est l'exploitation d'une fuite, la question utile n'est pas « qui nous attaque » mais **« combien de nos comptes figurent dans cette fuite, et lesquels sont encore valides ? »**.

Résultat, en deux jours : **quarante et un comptes** d'HELIOMED figurent dans la fuite. Quatorze ont été essayés. Trente-sept sont encore actifs. Trois n'ont pas d'authentification multifacteur — deux comptes de service et un compte d'un prestataire dont le contrat s'est achevé en 2028.

**C'est ce dernier qui compte.** Il n'avait pas été détecté par les revues d'accès précédentes parce qu'il figurait dans un annuaire secondaire, hérité d'une acquisition.

**Ce que Pierre Vasseur retient**, et qu'il formule en séance :

> *« Donc la bonne question n'était pas "pourquoi nous", c'était "qu'est-ce qui traîne chez nous". »*

**Les trois décisions** : rotation des trente-sept comptes concernés · surveillance systématique des fuites contenant le nom de domaine d'HELIOMED, ajoutée au plan de collecte comme besoin B-07 · revue des annuaires secondaires, portée au dispositif de MCS.

**Ce que Nour note.** L'évaluation n'a nommé personne, et elle a produit trois décisions. Un nom en aurait produit zéro.

> *« "Pourquoi nous" est une question de récit. "Qu'est-ce qui est accessible" est une question de renseignement. »*

**Livrable de l'épisode.** La grille des quatre paramètres (§17.8), intégrée à la procédure de réponse à incident — et le besoin B-07.

→ La suite en 🔴 §18.8, quand une cartographie de couverture se révélera excellente là où c'était facile.

## Synthèse mentale du chapitre 17

Ce qui est utile chez un acteur n'est pas son identité mais ce qui le contraint : objectif, moyens, horizon, et ce qu'il ne peut pas se permettre — quatre paramètres déductibles de l'observation, stables sur des années, et applicables à un acteur inconnu. Un criminel est contraint par la rentabilité, donc augmenter le coût suffit à le déplacer ; un acteur étatique est contraint par la discrétion, donc la sophistication n'est pas un marqueur d'origine — le raisonnement inverse est circulaire et faux. La menace interne accidentelle produit bien plus d'incidents que l'intentionnelle, et une fonction qui privilégie la seconde se trompe de priorité. La chaîne d'approvisionnement n'est pas un acteur mais un chemin, dont le rapport coût/gain est le plus favorable — ce qui explique sa fréquence. Enfin, un catalogue d'acteurs se périme en dix-huit mois, ne change aucune décision, et donne l'illusion de comprendre : les quatre paramètres le remplacent avantageusement, parce qu'ils restent révisables là qu'un nom, une fois posé, résiste aux éléments contraires.

**Trois questions de vérification**

1. Une intrusion emploie un outillage public et progresse lentement sans rien chiffrer. Que déduisez-vous, et qu'est-ce que vous ne déduisez pas ?
2. Pourquoi « c'était sophistiqué, donc c'est étatique » est-il un raisonnement fautif, et dans les deux sens ?
3. Votre direction demande « pourquoi nous ? ». Reformulez la question de manière à ce qu'elle produise des décisions.

---
