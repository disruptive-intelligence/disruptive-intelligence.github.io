---
title: Chapitre 15 — Le cycle du renseignement, et pourquoi il ne décrit pas la réalité
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE III — Du besoin au cycle
  - index.md
---

## 15.1 Le modèle classique

Il figure dans toutes les formations, sous des variantes de cinq à six étapes.

```
① ORIENTATION ──► ② COLLECTE ──► ③ TRAITEMENT ──► ④ ANALYSE
       ▲                                              │
       │                                              ▼
       └───────── ⑥ RETOUR ◄──────── ⑤ DIFFUSION ─────┘
```


| Étape | Contenu |
|---|---|
| ① Orientation | Définition des besoins |
| ② Collecte | Recueil de l'information |
| ③ Traitement | Mise en forme, traduction, dédoublonnage |
| ④ Analyse | Évaluation, production du jugement |
| ⑤ Diffusion | Transmission aux destinataires |
| ⑥ Retour | Évaluation de l'utilité, ajustement des besoins |

**Vous avez remarqué la ressemblance avec la boucle analytique du §1.2.** Elle est réelle, et la différence tient en un mot : le cycle décrit une **organisation**, la boucle décrit un **raisonnement**. Le cycle est un modèle de processus, la boucle est un modèle mental.

## 15.2 Ce que le modèle apporte réellement

Trois choses, et elles justifient qu'on l'enseigne :

| Apport | Mécanisme |
|---|---|
| **Un vocabulaire commun** | Tout le monde sait ce que « orientation » désigne |
| **Il place l'orientation en premier** | C'est le principe 2 de la doctrine, et le modèle le porte |
| **Il ferme la boucle** | L'étape ⑥ existe dans le modèle, ce qui la rend au moins pensable |

**Le troisième apport est le plus important**, et c'est celui qu'on oublie le plus : le cycle est le seul modèle courant du domaine qui prévoit explicitement de revenir vérifier si le travail a servi.

## 15.3 ⚠️ Pourquoi il est faux en pratique

Quatre raisons, et elles sont cumulatives.

**1. Le travail n'est pas séquentiel.** Un analyste collecte pendant qu'il analyse, reformule le besoin pendant qu'il collecte, et diffuse partiellement avant d'avoir conclu. Les étapes se chevauchent en permanence.

**2. Il n'y a pas un cycle, il y en a des dizaines simultanés.** À un instant donné, une fonction CTI porte plusieurs questions à des stades différents : l'une en collecte, l'autre en attente d'une réponse fournisseur, une troisième en relecture, une quatrième diffusée et sans retour. Le modèle en décrit un ; la réalité en gère quinze.

**3. La diffusion n'est pas une étape finale.** Elle est souvent le déclencheur d'une nouvelle collecte : le destinataire pose une question de retour qui rouvre le dossier. La flèche ⑤ → ⑥ → ① sous-estime largement ce qui se passe.

**4. L'étape ⑥ n'existe presque jamais.** Elle figure sur tous les schémas et dans presque aucune organisation. C'est le point du §1.2, et le chapitre 35 lui est consacré.

**La conséquence pédagogique** : présenter le cycle comme une description du travail conduit un débutant à croire qu'il fait mal les choses parce qu'il ne les fait pas dans l'ordre. Il ne les fait pas dans l'ordre parce que **l'ordre n'existe pas**.

## 15.4 Le processus réel

Ce que fait réellement une fonction CTI ressemble davantage à une **file de traitement** qu'à un cycle — et le lecteur venu du cours MCS y reconnaîtra le chapitre 17.

```
                 ┌──────────────────────────────────────┐
   ENTRÉES  ───► │  FILE DE SIGNALEMENTS                │
   · veille      │  chacun avec : origine · besoin      │
   · demandes    │  rattaché · statut · échéance        │
   · incidents   └──────────────┬───────────────────────┘
   · retours                    │
                                ▼
                    ┌───────────────────────┐
                    │  QUALIFICATION        │──► ARCHIVÉ (avec motif)
                    │  ça concerne un       │
                    │  besoin actif ?       │
                    └───────────┬───────────┘
                                ▼
                    ┌───────────────────────┐
                    │  TRAITEMENT           │──► EN ATTENTE (source, réponse)
                    │  vérification,        │
                    │  analyse, rédaction   │
                    └───────────┬───────────┘
                                ▼
                    ┌───────────────────────┐
                    │  RELECTURE            │
                    └───────────┬───────────┘
                                ▼
                    ┌───────────────────────┐
                    │  DIFFUSION            │──► SUIVI D'USAGE
                    └───────────────────────┘
```


**Les cinq états d'un signalement**, qui suffisent :

| État | Signification |
|---|---|
| **Nouveau** | Entré, non qualifié |
| **Qualifié** | Rattaché à un besoin actif, ou archivé avec motif |
| **En traitement** | Vérification, analyse, rédaction |
| **En attente** | Bloqué sur une source, une réponse, une information manquante |
| **Diffusé** | Avec date, destinataires, et suivi d'usage |

✅ **BONNE PRATIQUE (P0) — l'archivage avec motif**
C'est la ligne qui compte le plus, et c'est le §1.3 appliqué : la majorité des signalements aboutit à *archivé*. Le motif tient en cinq mots — *produit non présent au périmètre*, *rattaché à aucun besoin actif*, *déjà couvert par B-03*. Sans lui, on ne peut pas dire six mois plus tard si une information avait été vue et écartée, ou manquée.

## 15.5 Où le cycle casse le plus souvent

| Rupture | Symptôme | Traité au |
|---|---|---|
| **Entre ① et ②** | On collecte sans besoin — le cas majoritaire | Ch. 14 |
| **Entre ② et ④** | On accumule sans traiter : la file grossit | §15.4 |
| **Entre ④ et ⑤** | Le produit existe et n'est pas diffusé, ou mal | Ch. 25, 26 |
| **Entre ⑤ et ⑥** | **Aucun retour n'est demandé** | Ch. 35 |
| **Entre ⑥ et ①** | Les besoins ne sont jamais révisés | §14.5 |

**La rupture ⑤ → ⑥ est la plus fréquente et la plus coûteuse**, parce qu'elle est invisible : une fonction qui diffuse régulièrement paraît fonctionner, même si aucun de ses produits n'a jamais changé une décision.

## 15.6 📌 Utiliser le modèle sans y croire

**Ce qu'il faut en garder** :

- l'orientation en premier ;
- l'existence d'une étape de retour ;
- le vocabulaire, pour se comprendre.

**Ce qu'il faut abandonner** :

- l'idée de séquence ;
- l'idée d'un cycle unique ;
- l'idée que la diffusion clôt quelque chose.

**Ce qu'il faut mettre à la place** : la boucle analytique (§1.2) comme modèle mental, et une file de traitement comme organisation.

🎯 **ET MAINTENANT ?**
*Vous démarrez une fonction CTI et on vous demande de « mettre en place le cycle du renseignement ». Que faites-vous ?*
**Réponse** : vous mettez en place trois choses, et aucune ne s'appelle un cycle. Un **registre des besoins** avec leurs demandeurs (§14.7) · une **file de signalements** avec cinq états et un archivage motivé (§15.4) · un **registre des réponses** notant qui a demandé quoi et ce qui en a résulté (§5.3). Ces trois artefacts font vivre le cycle sans jamais l'invoquer, et ils produisent la matière du chapitre 35 — la seule preuve que la fonction sert à quelque chose.

## 15.7 🔴 FIL ROUGE — avril 2030 : ce que Nour fait vraiment

Claire demande à Nour de documenter le processus de la fonction, en vue de l'audit client annuel. Nour commence par dessiner le cycle classique, puis s'arrête : il ne décrit pas ce qu'elle fait.

**Elle relève alors son activité réelle sur trois semaines.** Résultat :

| Constat | Chiffre |
|---|---|
| Signalements entrés | 214 |
| Archivés à la qualification, avec motif | **187 (87 %)** |
| Traités | 27 |
| Ayant abouti à un produit diffusé | 9 |
| Dossiers ouverts simultanément à un instant donné | entre 4 et 11 |
| Dossiers rouverts par une question de retour | 3 |
| Produits diffusés pour lesquels un retour a été demandé | **2 sur 9** |

**Trois enseignements**, qu'elle porte au comité :

**1. L'essentiel du travail est le tri.** 87 % des signalements sont archivés, et c'est le fonctionnement normal — pas un défaut. Ce chiffre, présenté brut, inquiète Karim Lebrun jusqu'à ce que Nour retourne la question : *que devrait-on faire des 187 autres, sachant qu'aucun ne se rattache à un besoin actif ?*

**2. Il n'y a jamais un seul cycle.** À tout instant, entre quatre et onze dossiers coexistent à des stades différents. Le schéma linéaire ne décrit aucun d'entre eux.

**3. La boucle n'est pas fermée.** Sept produits sur neuf ont été diffusés sans qu'aucun retour ne soit demandé. C'est le point que Nour n'avait pas vu, et il est le plus important des trois.

**Ce qu'elle produit pour l'audit** : pas un schéma de cycle, mais trois documents — le registre des besoins, la description de la file avec ses cinq états, et un exemple complet de dossier depuis le signalement jusqu'à la diffusion.

**La réaction de l'auditeur client**, en juin :

> *« C'est la première fois qu'un fournisseur me montre son processus réel plutôt qu'un schéma de manuel. Je peux vérifier celui-ci. »*

**La décision prise.** Une case « retour demandé » devient obligatoire au registre de diffusion, avec trois questions envoyées deux semaines après chaque produit : *l'avez-vous lu ? · avez-vous décidé quelque chose ? · qu'est-ce qui vous a manqué ?* Trois questions, trois cases. C'est l'amorce du chapitre 35.

**L'effet mesuré à six mois** : le taux de réponse est de 60 %, ce qui est faible et suffisant. Sur vingt-deux produits, **onze décisions identifiées** — et surtout, quatre retours indiquant qu'il manquait la même chose : une estimation du coût des actions recommandées. Cette lacune était invisible sans le retour.

> *« Le cycle, je l'avais appris. La boucle, je l'ai fermée seulement quand j'ai eu une case à cocher »*, écrit Nour.

**Livrable de l'épisode.** La description du processus réel en cinq états, et les trois questions de retour — annexe J.

→ **Fin de la Partie III.** La suite en 🔴 §17.7, quand il faudra comprendre pourquoi un acteur choisit une cible.

## Synthèse mentale du chapitre 15

Le cycle du renseignement décrit une organisation, la boucle analytique décrit un raisonnement — et le cycle apporte trois choses qui justifient qu'on l'enseigne : un vocabulaire commun, l'orientation en premier, et l'existence d'une étape de retour. Il est faux comme description du travail pour quatre raisons cumulatives : le travail n'est pas séquentiel, il y a des dizaines de cycles simultanés, la diffusion déclenche souvent une nouvelle collecte, et l'étape de retour n'existe presque jamais. Le processus réel ressemble à une file de traitement à cinq états, dont la ligne la plus importante est l'archivage motivé — parce que l'essentiel du travail est le tri, et qu'un signalement écarté sans motif est indiscernable d'un signalement manqué. La rupture la plus coûteuse est celle entre diffusion et retour, parce qu'elle est invisible : une fonction qui diffuse régulièrement paraît fonctionner même si aucun produit n'a jamais changé une décision.

**Trois questions de vérification**

1. On vous demande de « mettre en place le cycle du renseignement ». Quels trois artefacts produisez-vous, et pourquoi aucun ne porte ce nom ?
2. 87 % de vos signalements sont archivés sans traitement. Est-ce un signe de dysfonctionnement ? Que répondez-vous à une direction inquiète ?
3. Pourquoi la rupture entre diffusion et retour est-elle à la fois la plus fréquente et la plus difficile à détecter ?

→ **Chapitre 16 — Pourquoi certaines attaques existent** : les incitations économiques qui expliquent les priorités adverses, en un chapitre volontairement resserré.

---
