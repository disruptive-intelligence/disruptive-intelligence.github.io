---
title: Chapitre 2 — Le vocabulaire
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

> Ce chapitre est court et il n'est pas facultatif. La moitié des malentendus d'architecture viennent de mots que trois personnes emploient en désignant trois choses.

## 2.1 Les mots qui désignent trois choses

### « Serveur »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | **Une machine** — physique ou virtuelle |
| Le développeur | **Un logiciel qui écoute** — un serveur web, un serveur de base de données |
| Le métier | **Un service** — « le serveur de paie est tombé » |

**Une même machine peut donc porter trois serveurs**, et un même serveur peut être réparti sur trois machines. Quand quelqu'un dit *« on a 96 serveurs »*, la première question utile est : *machines, logiciels ou services ?*

### « Application »

| Qui parle | Ce qu'il désigne |
|---|---|
| L'exploitation | Un processus installé sur une machine |
| Le développeur | Un ensemble de code déployé |
| Le métier | **Ce qu'il ouvre le matin** — qui peut mobiliser huit composants |
| L'achat | Une licence, un contrat |

### « Service »

Le mot le plus polysémique du domaine, et le plus important.

| Sens | Exemple | Chapitre |
|---|---|---|
| **Service technique** | Un processus qui tourne en arrière-plan | 18-23 |
| **Service réseau** | Ce qui écoute sur un port | 8-17 |
| **Service métier** | Ce qui produit une valeur pour l'organisation | **35** |
| Service au sens contractuel | Ce qui est facturé, avec un engagement | 38 |

⚠️ **Ce cours emploie « service » au sens métier** — chapitre 35 — sauf mention explicite. C'est le sens qui permet de décider.

### Les autres pièges

| Mot | Ambiguïté |
|---|---|
| **Plateforme** | Un ensemble matériel · un socle logiciel · un produit commercial |
| **Instance** | Une machine · un processus · un locataire chez un fournisseur |
| **Cluster** | Un groupe de machines redondantes · un groupe qui répartit la charge · un orchestrateur — **trois choses différentes** |
| **Nœud** | Une machine · un point du réseau · un membre d'un cluster |
| **Environnement** | Production, recette, développement · ou le contexte technique d'exécution |

## 2.2 Le vocabulaire minimal

Douze mots suffisent pour lire un schéma. Les voici, définis pour la lecture — pas pour l'exactitude protocolaire *(principe de coupe)*.

| Terme | Ce qu'il faut en savoir pour lire |
|---|---|
| **Client** | Ce qui demande. Un poste, mais aussi un serveur qui en appelle un autre |
| **Serveur** | Ce qui répond. Le rôle, pas la machine |
| **Protocole** | La convention de dialogue. Sur un schéma, il indique **la nature du flux** |
| **Port** | Le numéro qui identifie le service sur une machine. Il dit **quoi**, pas **où** |
| **Adresse** | Où se trouve une machine sur le réseau. Elle change |
| **Nom** | Ce qu'on retient. Il faut le traduire en adresse — chapitre 14 |
| **Segment** | Un morceau de réseau, isolé des autres par un équipement |
| **Zone** | Un regroupement de segments partageant un même niveau de confiance |
| **Flux** | Ce qui circule entre deux points, dans une direction |
| **Session** | Une conversation en cours, avec un état — chapitre 31 |
| **Redondance** | Deux exemplaires d'un même rôle, dont un peut tomber |
| **Point de rupture** | Ce qui, en tombant, arrête un service. **La notion la plus utile du cours** |

**Ce qui ne figure pas dans cette liste, volontairement** : les couches d'un modèle en sept niveaux, les classes d'adresses, les mécanismes de contrôle de congestion. Ils ne servent pas à lire un schéma — *principe de coupe*.

## 2.3 Le vocabulaire du terrain

Comme dans les autres volumes de la collection : ce que dit le cours, et ce que vous entendrez.

| Terme du cours | Ce que vous entendrez | Nuance à ne pas perdre |
|---|---|---|
| Mandataire inverse | « **le reverse** », « le proxy », « le frontal » | On l'appelle « proxy » alors qu'il fait l'inverse — chapitre 12 |
| Mandataire sortant | « **le proxy** » | Même mot, fonction opposée |
| Répartiteur de charge | « **le load balancer** », « le LB », « la VIP » | La « VIP » désigne l'adresse virtuelle, pas l'équipement |
| Zone démilitarisée | « **la DMZ** » | Le mot est militaire et trompeur — chapitre 25 |
| Point de rupture unique | « **le SPOF** » | — |
| Résolution de noms | « **le DNS** » | Souvent employé pour désigner le service **et** le serveur |
| Annuaire | « **l'AD** », « le LDAP », « le domaine » | Trois choses différentes, souvent confondues |
| Infrastructure de clés | « **la PKI** », « les certifs » | — |
| Poste d'administration | « **le bastion** », « le jump », « le rebond » | — |
| Segment réseau | « **le VLAN** », « le subnet » | Deux notions distinctes, souvent alignées mais pas toujours |
| Flux de dépendance | *(aucun terme courant)* | **L'absence de mot est le problème** — règle principe des trois flux |
| Orchestrateur | « **le cluster** », « K8s », « la plateforme » | — |

⚠️ **La ligne « flux de dépendance » est la plus significative du tableau.** Il n'existe pas de terme courant pour désigner ce sans quoi un service ne peut pas s'établir. C'est l'une des raisons pour lesquelles ces flux sont invisibles sur les schémas : **on ne dessine pas ce qu'on ne nomme pas.**

## 2.4 Lire un protocole sur un schéma

Sans entrer dans leur fonctionnement, six protocoles suffisent à identifier la nature d'un flux.

| Ce qui est écrit | Ce que ça vous dit du flux |
|---|---|
| `443`, `HTTPS` | Une consultation web chiffrée — flux **métier**, le plus courant |
| `80`, `HTTP` | Idem, non chiffré. Sur un schéma récent, c'est une **question à poser** |
| `53`, `DNS` | Résolution de noms — flux de **dépendance** |
| `389`, `636`, `LDAP` | Annuaire — flux de **dépendance** |
| `123`, `NTP` | Synchronisation d'horloge — flux de **dépendance**, presque jamais dessiné |
| `514`, `syslog` | Journaux — flux d'**exploitation** |
| `3389`, `22` | Administration à distance — flux d'**exploitation**, **le plus sensible** |
| `1433`, `3306`, `5432` | Bases de données — flux **métier**, entre serveurs |

**Ce que ce tableau permet immédiatement** : classer un flux dans l'une des trois familles sans rien connaître du protocole. C'est le principe de coupe appliqué — juste ce qu'il faut pour décider.

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. Aucun numéro de port n'y figure. Vous ne pouvez donc pas savoir quels flux le traversent réellement. **C'est le cas de la majorité des schémas d'architecture**, et c'est la première chose qui manque quand on veut raisonner.

## 2.5 🔬 Mini-lab 1 — Quatre phrases, quatre malentendus

**Objectif** — Repérer une ambiguïté de vocabulaire et poser la question qui la lève.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §2.1 à §2.3
**Compétences validées** — ✔ identifier un mot polysémique ✔ formuler la question qui désambiguïse ✔ reconnaître les conséquences d'un malentendu

**Les phrases** :

```
① « On a 96 serveurs. »
② « L'application de paie est tombée ce matin. »
③ « Il faut mettre l'application derrière le proxy. »
④ « On a un cluster de trois nœuds. »
```


**Consigne** : pour chacune, dites quelles interprétations sont possibles, la question à poser, et ce que coûte le malentendu.

---

**Corrigé**

| # | Interprétations possibles | Question à poser | Ce que coûte le malentendu |
|---|---|---|---|
| **①** | 96 machines · 96 systèmes · 96 services · 96 lignes dans un référentiel | *« Machines physiques, machines virtuelles, ou services ? »* | Un dénominateur faux pour tout le reste — c'est le volume Asset Management |
| **②** | Un processus · un serveur · **un service métier composé de six composants** | *« Qu'est-ce qui ne marche plus, du point de vue de l'utilisateur ? »* | On redémarre une machine alors que le problème est ailleurs |
| **③** | Mandataire **sortant** — pour que l'application accède à Internet · mandataire **inverse** — pour qu'on y accède depuis Internet. **Fonctions opposées** | *« Pour sortir, ou pour entrer ? »* | On ouvre un flux dans le mauvais sens, ou on expose ce qui ne devait pas l'être |
| **④** | Trois machines redondantes · trois machines qui se répartissent la charge · trois nœuds d'un orchestrateur | *« Si un nœud tombe, que se passe-t-il ? »* | On croit avoir une redondance qu'on n'a pas |

**La phrase ③ est celle qui produit les erreurs les plus coûteuses**, parce que le même mot désigne deux fonctions opposées et que personne ne pense à demander.

**L'erreur attendue** : traiter ① comme une question de comptage. C'est une question de **définition** — et c'est exactement le chapitre 2 du volume Asset Management.

## 2.6 🔴 FIL ROUGE — décembre 2025 : trois personnes, trois « serveurs »

Amélie reprend les trois chiffres de décembre — 96, 71, 118 — et pose à chacun une seule question : *« quand tu dis serveur, tu comptes quoi ? »*

| Interlocuteur | Ce qu'il compte | Chiffre |
|---|---|---|
| Malik Ferhaoui, exploitation | Des **machines** — physiques et virtuelles — qu'il administre | 96 |
| La comptabilité | Des **immobilisations** — du matériel acheté et non amorti | 71 |
| L'outil de scan | Des **adresses ayant répondu** — donc ni les machines éteintes, ni celles hors du segment balayé | 118 |

**Trois définitions, trois périmètres, aucune intersection complète.** Et une découverte : le scan compte **118 adresses**, pas 118 machines — deux serveurs à deux interfaces réseau y comptent quatre fois.

**Ce qu'Amélie note** :

> *Personne ne s'est trompé. Nous avons trois réponses à trois questions différentes, et nous n'avons posé aucune des trois.*

**Ce qui est décidé** : avant tout comptage, écrire ce que le mot désigne. Cette décision sera formalisée en janvier — c'est le chapitre 2 du volume Asset Management, et c'est la réunion de deux heures qui y est racontée.

→ La suite en 🔴 §3.7, quand Amélie apprendra à lire un schéma — et surtout ce qu'il ne dit pas.

## Synthèse mentale du chapitre 2

Trois mots portent l'essentiel des malentendus d'architecture — serveur, application, service — et chacun désigne au moins trois choses selon qui parle. Une même machine peut porter trois serveurs, et un même serveur être réparti sur trois machines : la question utile devant un chiffre est toujours *machines, logiciels ou services ?* Douze termes suffisent pour lire un schéma, et le plus utile d'entre eux est le point de rupture. Six protocoles suffisent à classer un flux dans l'une des trois familles sans rien connaître de leur fonctionnement. Enfin, il n'existe pas de terme courant pour désigner un flux de dépendance — et cette absence de mot est l'une des raisons pour lesquelles ces flux ne sont jamais dessinés : on ne dessine pas ce qu'on ne nomme pas.

**Trois questions de vérification**

1. Quelqu'un vous annonce un nombre de serveurs. Quelle question posez-vous, et pourquoi ce n'est pas une question de comptage ?
2. « Mets l'application derrière le proxy. » Pourquoi cette phrase est-elle dangereuse, et que demandez-vous ?
3. Pourquoi l'absence de terme courant pour « flux de dépendance » a-t-elle un effet concret sur les schémas ?

→ **Chapitre 3 — Comment lire un schéma** : les conventions, et surtout ce qu'un schéma choisit de ne pas montrer.

---
