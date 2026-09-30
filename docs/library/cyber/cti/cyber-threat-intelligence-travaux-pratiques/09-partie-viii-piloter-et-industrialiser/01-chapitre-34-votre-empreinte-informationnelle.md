---
title: Chapitre 34 — Votre empreinte informationnelle
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

## 34.1 Ce que votre organisation révèle d'elle-même

**Le renversement de perspective** : jusqu'ici, vous collectiez du renseignement. Ce chapitre pose la question inverse — **que collecte-t-on sur vous, et gratuitement ?**

**Ce n'est pas du contre-renseignement au sens strict**, et il ne s'agit pas de secret. Il s'agit de savoir ce qu'un observateur attentif peut établir sans rien faire d'illicite.

| Ce que vous publiez | Ce qu'on en déduit |
|---|---|
| **Offres d'emploi** | Vos technologies, vos outils, vos projets, vos manques |
| Certificats publics | Vos noms d'hôtes, y compris internes |
| Enregistrements de noms | Votre infrastructure, vos environnements de test |
| Communication commerciale | Vos clients, vos secteurs, vos dépendances |
| Interventions en conférence | Votre architecture, vos difficultés |
| Publications de vos équipes | Vos outils, parfois vos configurations |
| **Signatures de messagerie** | Vos fonctions, vos formats de compte, votre organigramme |
| Documents publiés | Métadonnées : logiciels, chemins, noms d'utilisateurs |

**La première ligne est la plus riche et la plus négligée.** Une annonce recherchant « un ingénieur maîtrisant [produit A], [produit B] et [produit C], pour renforcer notre capacité de détection sur [périmètre] » décrit votre pile technique, votre organisation, et l'endroit où vous vous sentez faible.

## 34.2 Fuites et données divulguées

| Type | Ce qu'il révèle | Ce qu'on peut faire |
|---|---|---|
| Fuite chez un tiers contenant vos identifiants | Vos comptes, vos formats, parfois des mots de passe | Rotation, surveillance (§17.9) |
| Fuite chez un fournisseur | Vos données confiées | Réclamation contractuelle, notification |
| Document interne publié par erreur | Ce qu'il contient, et vos processus | Retrait, évaluation d'impact |
| Dépôt de code exposé | Secrets, architecture, dépendances | **Rotation immédiate des secrets** |

**Le suivi des fuites contenant votre nom de domaine** est l'un des rares besoins que les sources ouvertes ne couvrent pas et que le payant couvre bien (§22.2). C'est aussi celui dont le rapport valeur/prix est le plus favorable.

## 34.3 ⚠️ Ce que vos propres alertes et publications apprennent à l'adversaire

Le point le plus contre-intuitif du chapitre, esquissé au §28.6.

| Ce que vous faites | Ce que cela révèle |
|---|---|
| Vous partagez un indicateur | Que vous l'avez observé — donc que vous êtes touché ou visé |
| Vous publiez une analyse détaillée | Votre niveau de capacité, et vos sources |
| Vous corrigez une vulnérabilité en urgence | Que vous étiez exposé |
| Vous posez une question précise dans un dispositif | Où vous vous sentez vulnérable |
| **Vous ne dites rien pendant six mois** | Que vous n'observez rien, ou que vous ne pouvez rien dire |
| **Vous bloquez une infrastructure** | Que vous l'avez identifiée — un adversaire attentif le voit |

**Ce qu'il ne faut pas en conclure** : le repli. La valeur reçue d'un dispositif de partage dépasse largement ce risque, et une organisation qui ne partage rien s'exclut d'elle-même.

**Ce qu'il faut en faire** : relire ce qu'on publie en se demandant ce qu'un observateur en déduirait, et arbitrer au cas par cas — c'est exactement la grille du §28.7.

**Le cas du blocage mérite un mot** : un adversaire qui constate que son infrastructure ne répond plus chez une cible sait qu'il a été détecté. C'est un arbitrage réel entre protection immédiate et conservation de la visibilité, et il appartient au responsable de l'incident, pas à l'analyste.

## 34.4 Mesures réalistes, et ce qui relève de la paranoïa

| Mesure | Coût | Valeur | Verdict |
|---|---|---|---|
| Revoir les offres d'emploi avant publication | Faible | Moyenne | **À faire** |
| Nettoyer les métadonnées des documents publiés | Faible | Moyenne | **À faire** |
| Surveiller les fuites contenant votre domaine | Moyen | **Élevée** | **À faire** |
| Auditer ce qui est visible de vous depuis l'extérieur | Moyen | Élevée | **À faire** (annuel) |
| Restreindre les interventions en conférence | Moyen | Faible | Non — coût culturel disproportionné |
| Anonymiser vos certificats publics | Élevé | Faible | Non |
| Cesser de partager en sectoriel | Faible | **Négative** | **Non** |

**La ligne du milieu marque la frontière.** Au-dessus : des mesures peu coûteuses et utiles. En dessous : des mesures qui dégradent le fonctionnement de l'organisation pour un gain marginal.

🎯 **ET MAINTENANT ?**
*Votre direction, alertée par ce sujet, propose de cesser toute publication technique et toute participation aux conférences. Que répondez-vous ?*
**Réponse** : que le calcul est défavorable. Ce que vos équipes publient est observable par un adversaire — mais il l'obtiendrait par d'autres moyens, et le coût est immédiat et certain : perte d'attractivité au recrutement, isolement de vos équipes, perte d'accès aux réseaux d'entraide qui vous alimentent. Ce que vous proposez à la place : une relecture avant publication, portant sur trois points — pas de configuration précise, pas de nom d'hôte interne, pas de description de vos angles morts. Dix minutes par publication. Vous conservez le bénéfice et vous supprimez l'essentiel du risque.

## 34.5 🔴 FIL ROUGE — janvier 2031 : l'audit d'empreinte

Nour conduit le premier audit d'empreinte informationnelle d'HELIOMED, en trois jours, sans autre outil qu'un navigateur et les sources publiques.

**Ce qu'elle établit** :

| Élément | Constat |
|---|---|
| Offres d'emploi actives | 7 — dont une décrivant précisément la pile de sécurité et mentionnant « renforcement de notre capacité de détection sur le périmètre industriel » |
| Certificats publics | 43 noms d'hôtes, dont **11 correspondant à des environnements de recette** |
| Métadonnées de documents publiés | 6 documents commerciaux contenant noms d'utilisateurs et chemins internes |
| Interventions en conférence | 2 sur trois ans, sans information sensible |
| Fuites contenant le domaine | **3 jeux distincts**, dont un non identifié jusque-là |
| Mentions publiques de clients | 19 clients nommés dans la communication commerciale |

**Les trois constats qui produisent une action** :

**1. L'offre d'emploi.** Elle indique explicitement où HELIOMED se sait faible — le périmètre industriel, qui est effectivement sa zone aveugle (§18.8). L'annonce est reformulée : les compétences recherchées sont conservées, la mention du périmètre et de la finalité est retirée.

**2. Les onze noms d'hôtes de recette.** Ils apparaissent dans les journaux de certificats publics, et deux d'entre eux résolvent vers des adresses joignables. C'est transmis au dispositif de gestion des vulnérabilités : deux environnements de recette étaient accessibles depuis Internet, ce qu'aucun scan interne n'avait signalé.

**3. La troisième fuite.** Elle contient 22 comptes, dont 4 encore actifs. Rotation immédiate.

**Ce que l'audit ne produit pas** : aucune recommandation de restreindre la communication ou les interventions publiques. Nour l'écrit explicitement dans sa note, par anticipation :

> *Nous ne recommandons aucune restriction de la communication publique ni de la participation aux conférences. Le bénéfice de ces activités — recrutement, réputation, accès aux réseaux professionnels — dépasse largement le risque, et les informations concernées seraient obtenues autrement. Nous recommandons une relecture avant publication, sur trois points précis.*

**Ce que Claire relève** : l'audit a coûté trois jours et produit deux découvertes de sécurité — les environnements de recette exposés et la fuite non identifiée — qu'aucun autre dispositif n'avait remontées.

> *« Nous nous regardions de l'intérieur depuis trois ans. C'est la première fois que nous nous regardons de l'extérieur. »*

**Livrable de l'épisode.** La grille d'audit d'empreinte en six points, reconduite annuellement — annexe L.

→ La suite en 🔴 §35.8, quand il faudra répondre à la question posée en avril 2029.

## Synthèse mentale du chapitre 34

La question inverse du reste du cours : que collecte-t-on sur vous, gratuitement et licitement ? Les offres d'emploi sont la source la plus riche et la plus négligée — elles décrivent votre pile technique, votre organisation, et l'endroit où vous vous sentez faible. Vos propres actions révèlent aussi : partager un indicateur signale que vous l'avez observé, poser une question précise signale où vous vous sentez vulnérable, et un silence prolongé signale que vous n'observez rien. Il n'en découle pas le repli : la valeur reçue d'un dispositif de partage dépasse largement ce risque, et une organisation qui cesse de publier paie un coût immédiat et certain pour un gain marginal. La frontière des mesures raisonnables passe entre celles qui coûtent peu — relecture, métadonnées, surveillance des fuites, audit annuel — et celles qui dégradent le fonctionnement de l'organisation.

**Trois questions de vérification**

1. Quelle publication de votre organisation décrit le mieux votre pile technique et vos zones de faiblesse ?
2. Votre direction propose de cesser toute publication technique. Que répondez-vous, et que proposez-vous à la place ?
3. Pourquoi le blocage d'une infrastructure adverse est-il un arbitrage, et à qui appartient-il ?

---
