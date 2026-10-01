---
title: Chapitre 34 — Suivre un journal
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

> Le flux d'exploitation par excellence. **Sa rupture n'arrête aucun service — elle rend aveugle.**

## 34.1 D'où naît un journal, et ce que chacun voit

| Source | Ce qu'elle voit | Ce qu'elle ne voit pas |
|---|---|---|
| **Poste** | L'activité de l'utilisateur, les processus | Ce qui se passe sur le réseau après |
| **Pare-feu** | Ce qui traverse, et ce qui est refusé | Le contenu, sauf inspection |
| **Mandataire** | Les destinations, le contenu si déchiffré | **Ce qui ne passe pas par lui** — §29.3 |
| **Serveur web** | Les requêtes reçues | **L'identité réelle si un mandataire est devant** |
| **Applicatif** | Les actions métier, les autorisations | Ce qui se passe sous lui |
| **Base** | Les requêtes, parfois les données lues | **L'utilisateur final**, si l'applicatif utilise un compte unique |
| **Annuaire** | Les authentifications | Ce qui est fait après |

## 34.2 La perte d'identité en chemin

**Le problème le plus structurant du chapitre.**

```
   Marie ──► [ mandataire ] ──► [ web ] ──► [ app ] ──► [ base ]

   JOURNAL DU MANDATAIRE   « marie.durand a demandé /dossiers/4821 »
   JOURNAL DU WEB          « 10.0.2.15 a demandé /dossiers/4821 »
                             ↑ l'adresse du MANDATAIRE, pas de Marie
   JOURNAL DE L'APPLICATIF « utilisateur marie.durand a consulté
                             le dossier 4821 »   ← le seul complet
   JOURNAL DE LA BASE      « svc_app a exécuté SELECT ... »
                             ↑ le COMPTE DE SERVICE, pas Marie
```


⚠️ **Quatre journaux, deux identités différentes, et un seul qui relie l'utilisateur à l'action métier.** C'est le §43.3 : **l'applicatif est le seul point qui connaisse simultanément l'utilisateur réel et l'action**.

**Ce que cela impose** : corréler un journal de base avec un utilisateur réel exige de traverser trois journaux — et **cela suppose qu'ils partagent une horloge**. C'est pourquoi la synchronisation d'horloge est un flux de dépendance, principe des trois flux.

📌 **Les mécanismes qui atténuent le problème** : un mandataire peut transmettre l'adresse d'origine dans un en-tête · une application peut propager l'identité de l'utilisateur jusqu'à la base. **Les deux existent, les deux se configurent, et ni l'un ni l'autre n'est activé par défaut.**

## 34.3 Le chemin d'un journal

```
  ① PRODUCTION     le composant écrit
  ② STOCKAGE LOCAL avec une rotation qui l'efface après N jours
  ③ TRANSPORT      vers une collecte centrale — souvent en clair
  ④ COLLECTE       normalisation, horodatage
  ⑤ CONSERVATION   pour une durée définie… ou pas
  ⑥ EXPLOITATION   recherche, alerte, corrélation
```


**Les trois points de perte** :

| Point | Ce qui se perd | Pourquoi personne ne le voit |
|---|---|---|
| **② → ③** | Si le transport échoue, la rotation locale efface | **Rien n'alerte sur l'absence de journaux** |
| **⑤** | Une conservation trop courte | On ne s'en aperçoit qu'au moment d'enquêter |
| **④** | Un format non reconnu est ingéré sans être exploitable | Le volume est correct, la recherche ne trouve rien |

⚠️ **Le premier est le plus pernicieux** : une chaîne de collecte cassée ne produit **aucun signal**. L'absence de journaux ressemble exactement à l'absence d'activité. **La seule protection est de superviser le volume reçu par source** — et de s'alerter quand il tombe à zéro.

⚠️ **Le deuxième est le plus coûteux.** Le délai moyen entre une compromission et sa détection dépasse souvent la durée de conservation des journaux. **On enquête alors sur une période dont il ne reste rien.**

🔥 **SCÉNARIO — l'enquête porte sur une période dont il ne reste rien**

| Question | Réponse |
|---|---|
| Symptôme | Une compromission est découverte. Elle date d'il y a quatre mois |
| Hypothèse naïve | « On va regarder les journaux » |
| Dépendance réelle | **La conservation est de 90 jours.** Il ne reste rien |
| Ce que le schéma aurait dû montrer | La durée de conservation, par source |
| Concevoir différemment | **Aligner la conservation sur le délai de détection observé**, pas sur le coût du stockage |

## 34.4 Ce que la journalisation dit de l'architecture

**Une observation qui vaut méthode**, et il faut la formuler précisément :

> **Un composant peut produire un journal s'il est *en position de savoir* quelque chose.**

**Deux façons de l'être** :

| Position | Ce que le composant sait | Exemples |
|---|---|---|
| **Sur un chemin** | Ce qui le traverse | Pare-feu, mandataire, commutateur, routeur |
| **À l'origine d'une décision** | Ce qu'il a décidé, **sans qu'aucun flux ne traverse quoi que ce soit** | Une application qui autorise ou refuse · un poste qui lance un processus · un annuaire qui valide une identité |

⚠️ **La seconde ligne est celle que le modèle du point de passage manque.** Une application qui journalise *« Marie a exporté 4 000 lignes »* produit un événement métier **que rien n'a traversé au sens réseau**. C'est même la seule source capable de le produire — §34.2.

**Ce que cela donne comme méthode de lecture** :

```
   Devant chaque composant, une seule question :
   « Est-il en position de savoir quelque chose que personne d'autre ne sait ? »

   → OUI, et il journalise           ✅
   → OUI, et il ne journalise pas    ⚠️ angle mort — c'est le plus grave
   → NON                             pas de journal à en attendre
```


⚠️ **La deuxième ligne définit un angle mort structurel** : un composant qui sait et qui ne dit rien. C'est le cas de la plupart des applications métier — elles connaissent l'utilisateur et l'action, et elles ne journalisent que les erreurs techniques.

C'est le chapitre 43.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On log tout » | Beaucoup de sources sont collectées | **Combien de temps ? Et l'identité est-elle préservée ?** |
| « On a un SIEM » | Une collecte centrale existe | **Toutes les sources y arrivent-elles réellement ?** |
| « On n'a pas les logs » | La période est hors rétention | Combien de jours ? **Aligné sur quoi ?** |
| « L'IP dans le log est celle du proxy » | La perte d'identité — §34.2 | L'en-tête d'origine est-il transmis ? |

---
