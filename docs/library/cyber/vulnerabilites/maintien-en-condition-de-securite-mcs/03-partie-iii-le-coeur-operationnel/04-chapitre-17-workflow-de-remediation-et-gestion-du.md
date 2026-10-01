---
title: Chapitre 17 — Workflow de remédiation et gestion du backlog
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

## 17.1 Pourquoi la décision ne suffit pas

Le chapitre 16 a produit une décision pour chaque constat. Entre cette décision et la correction effective, il se passe des semaines — parfois des mois — pendant lesquelles le constat doit **exister quelque part**, avec un propriétaire, une échéance et un état.

C'est ce que la plupart des organisations ne font pas. Le triage est soigné, la correction est bien exécutée, et **entre les deux il n'y a qu'un tableur**. Les symptômes sont toujours les mêmes :

- personne ne sait combien de constats sont réellement en cours de traitement ;
- un même problème est traité deux fois par deux personnes différentes ;
- un constat affecté à quelqu'un qui a quitté l'entreprise n'est jamais réaffecté ;
- une vulnérabilité corrigée réapparaît trois mois plus tard sans que personne ne s'en étonne ;
- on ne peut pas répondre à la question « depuis combien de temps ce constat est-il ouvert ? ».

**Le principe de ce chapitre** : le constat est un **objet de gestion** avec un cycle de vie, pas une ligne dans un rapport. C'est ce cycle de vie qui rend le MCS pilotable, mesurable et démontrable.

## 17.2 De la détection au ticket : agrégation et déduplication

Un scan produit des constats, pas des tickets. Créer un ticket par constat est une erreur qui noie l'organisation : 3 800 constats produiraient 3 800 tickets, dont personne ne ferait rien.

**La structure à adopter — le modèle parent / enfants :**

```
CONSTAT PARENT : « Vulnérabilité X dans le composant Y »
   ├─ Actif A  (version, état, échéance)
   ├─ Actif B
   ├─ … 42 actifs
   └─ Décision de triage, propriétaire, échéance : portés par le PARENT
```


Un ticket par **problème**, avec la liste des actifs concernés en pièces attachées. La décision, l'échéance et le propriétaire s'attachent au parent ; l'état d'avancement se mesure sur les enfants.

**Les quatre règles de déduplication**, qui évitent la majorité du bruit :

| Règle | Effet |
|---|---|
| Un même identifiant de vulnérabilité sur plusieurs actifs → **un** ticket parent | Divise le volume par un facteur important |
| Plusieurs constats corrigés par le **même correctif** → un ticket | Aligne le ticket sur l'unité de travail réelle |
| Constat remonté par deux outils différents → un ticket, deux sources | Évite le double traitement (§15.11, faux positif n° 9) |
| Constat réapparaissant sur un actif redéployé → **réouverture**, pas nouveau ticket | Préserve l'historique et révèle la récurrence (§17.9) |

⚠️ **PIÈGE — la déduplication trop agressive**
Regrouper des constats qui ne se corrigent pas de la même façon crée un ticket impossible à clore : il reste ouvert parce qu'un actif sur quarante-deux résiste. Le critère de regroupement doit être **l'action de correction**, pas la ressemblance du constat.

## 17.3 Campagnes ou traitement à l'unité

Deux modes de travail coexistent, et les confondre coûte cher.

| Mode | Quand l'employer | Unité |
|---|---|---|
| **À l'unité** | Constats urgents, actifs de niveau 0, cas particuliers | Le constat parent |
| **En campagne** | Volume, correctifs cumulatifs, montées de version | Un lot d'actifs, une fenêtre, un objectif d'état |

**La campagne est un objet de gestion distinct**, avec ses propres attributs : périmètre d'actifs, objectif d'état cible, fenêtre, anneaux de déploiement, critères d'arrêt, propriétaire, plan de retour arrière. Elle **absorbe** un ensemble de tickets, qui se ferment collectivement à sa vérification.

✅ **BONNE PRATIQUE (P1)** — Un tableau de bord de MCS mature affiche **deux compteurs distincts** : les constats en traitement unitaire, et les campagnes en cours avec leur avancement. Mélanger les deux dans un unique décompte de vulnérabilités ouvertes produit un chiffre qui n'a aucun sens opérationnel.

## 17.4 Propriétaires, refus d'affectation et constats orphelins

**L'affectation** relie le ticket au propriétaire technique de l'actif, issu de l'inventaire (§5.5 et §10.4). Si l'inventaire porte cette information, l'affectation est automatique — c'est l'un des bénéfices les plus concrets du travail des chapitres 5 et 10.

**Trois situations à traiter explicitement**, faute de quoi elles bloquent silencieusement la file :

| Situation | Traitement |
|---|---|
| **Aucun propriétaire** | Le constat porte sur un actif orphelin. Ce n'est pas un problème de remédiation, c'est un problème d'inventaire : il remonte au processus de désignation (§5.5), avec la procédure d'extinction programmée en dernier recours |
| **Refus d'affectation** | Le propriétaire estime que l'actif ne relève pas de lui. Délai de contestation borné — par exemple 5 jours ouvrés — puis arbitrage au comité. **Sans délai, le ticket reste en suspens indéfiniment** |
| **Propriétaire indisponible** | Départ, congé long, réorganisation. Règle de suppléance automatique, sinon le ticket vieillit sans que personne ne le sache |

🏢 **VU EN RÉUNION** — Un constat critique traîne depuis onze semaines. En comité, chacun explique de bonne foi pourquoi il ne s'agit pas de son périmètre : l'exploitation dit que c'est applicatif, l'équipe applicative dit que c'est système, le métier dit qu'il n'a pas été saisi. Tous ont raison. Ce qui manquait n'était pas de la bonne volonté, c'était un **délai de contestation borné** et une escalade automatique.

⚠️ **PIÈGE — le ticket affecté à une équipe**
Affecter à « l'équipe infrastructure » revient à n'affecter à personne : c'est la version outillée du problème du §5.5. L'affectation nominative est un prérequis, et le suivi de l'âge du *backlog* par personne révèle très vite les affectations fictives.

## 17.5 Échéances : départ du compteur et suspensions légitimes

**La question qui doit être tranchée une fois pour toutes** : à partir de quand court le délai ?

| Point de départ possible | Avantage | Inconvénient |
|---|---|---|
| Publication du correctif par l'éditeur | Reflète le risque réel | Vous pénalise pour un scan tardif |
| **Détection par votre outil** | Mesurable, sous votre contrôle | Récompense un scan peu fréquent |
| Création du ticket | Simple | Décale artificiellement le délai |

**La recommandation** : mesurer **les deux premiers**, et les présenter séparément. Le délai depuis la publication mesure le temps écoulé **depuis qu'une correction était disponible** ; le délai depuis la détection mesure votre **réactivité**. L'écart entre les deux mesure la fraîcheur de votre détection (§15.5) — un troisième indicateur, gratuit, et souvent le plus instructif.

⚠️ **Aucun des deux ne mesure la durée d'exposition réelle**, qui commence à l'introduction de la vulnérabilité dans votre parc — souvent des années plus tôt, comme le montre le cas de synthèse A. Ne présentez jamais le délai depuis la publication comme « l'exposition » : c'est une borne inférieure.

### Les deux horloges

C'est la distinction qui empêche de rendre le retard invisible.

| Horloge | Départ | Se suspend ? | Ce qu'elle mesure |
|---|---|---|---|
| **Horloge de risque** | Connaissance pertinente, ou disponibilité d'une correction ou d'une mesure d'atténuation | **Jamais** | Le temps pendant lequel le risque est porté |
| **Horloge de traitement (SLA)** | Idem | Oui, dans des cas limitativement définis | Le respect de l'engagement opérationnel |

**Pourquoi les deux sont nécessaires.** Un gel de production, une attente de correctif éditeur ou une demande d'information suspendent légitimement l'**engagement opérationnel** — l'équipe n'est pas en faute. Mais **le risque, lui, continue de courir**. Une organisation qui ne publie que l'horloge de traitement affiche des délais tenus tout en portant une exposition croissante qu'aucun indicateur ne montre.

✅ **BONNE PRATIQUE (P0)** — Publiez les deux. L'horloge de traitement pilote l'équipe ; l'horloge de risque pilote la direction. Un écart croissant entre les deux est le signal le plus honnête d'un problème structurel — capacité, dépendance fournisseur ou gels trop nombreux.

**Les suspensions légitimes de l'horloge de traitement**, à définir limitativement :

| Motif | Condition |
|---|---|
| Attente d'un correctif éditeur | Le correctif n'existe pas encore — documenté, relance périodique, **et mesure compensatoire engagée** (ch. 20) |
| Attente d'une information demandée à un tiers | Demande écrite et horodatée (§14.10), avec date de relance |
| Fenêtre de gel de production | Prévue par la politique, avec sa clause de levée (§9.4) |

⚠️ **Une suspension ne suspend jamais le risque.** Toute suspension de plus de quelques jours doit s'accompagner d'une mesure compensatoire ou d'une acceptation formelle — sinon vous avez seulement rendu le retard invisible.

⚠️ **PIÈGE — la suspension comme échappatoire**
Sans liste limitative, la suspension devient le moyen de faire disparaître les retards des indicateurs. **Deux garde-fous** : le temps passé en suspension est mesuré et affiché séparément, et une suspension de plus de N jours déclenche une escalade automatique.

🖼 **SCHÉMA — Cycle de vie d'un constat.** *Machine à états, sept états principaux, transitions fléchées, états terminaux distingués des états ouverts (dérogation, dépriorisé).*

## 17.6 Le modèle d'états

Un cycle de vie en sept états, avec des transitions contrôlées. C'est le **livrable de référence** du chapitre, détaillé en Annexe J.

```
   NOUVEAU
      │  qualification (statut §14.7, vérifications §16.4)
      ▼
   QUALIFIÉ ──────────────────► FAUX POSITIF (clos, avec preuve)
      │  décision de triage (§16.3)
      ▼
   AFFECTÉ ───────────────────► DÉPRIORISÉ (ouvert, date de revue)
      │  propriétaire accepte
      ▼
   PLANIFIÉ ──────────────────► DÉROGATION (ouvert, §7.4)
      │  fenêtre, campagne
      ▼
   EN CORRECTION
      │  action réalisée
      ▼
   À VÉRIFIER ────────────────► ÉCHEC → retour à PLANIFIÉ
      │  preuve obtenue
      ▼
   CLOS ◄───────────────────── RÉOUVERTURE si réapparition
```


**Les champs obligatoires par état** — c'est ce qui empêche un ticket d'avancer sans le travail correspondant :

| État | Champs exigés pour y entrer |
|---|---|
| Qualifié | Statut de qualification, actifs confirmés, vérification d'activation |
| Affecté | Propriétaire nominatif, échéance, décision de triage |
| Planifié | Fenêtre ou campagne de rattachement, plan de retour arrière |
| À vérifier | Date d'action, méthode de vérification prévue |
| Clos | **Preuve** conforme au §2.9 |
| Déprioritisé | Motif parmi les quatre du §16.6, **date de revue** |
| Dérogation | Les sept champs du §7.4 |

## 17.7 Les issues possibles, et la preuve attendue pour chacune

| Issue | Signification | Preuve exigée |
|---|---|---|
| **Corrigé** | Le correctif est appliqué et effectif | État constaté sur l'actif, postérieur à l'action (§2.9) |
| **Atténué** | Le risque est réduit sans correction | Description de la mesure, vérification qu'elle est active, **date d'expiration** |
| **Dérogation** | Décision de ne pas corriger, bornée | Fiche complète signée par le propriétaire métier |
| **Faux positif** | Le constat était erroné | **Démonstration**, pas affirmation : révision vérifiée, capture, avis éditeur |
| **Risque accepté** | Décision définitive de ne pas traiter | Signature au niveau approprié, revue périodique |
| **Sans objet** | L'actif n'existe plus | Preuve de décommissionnement (ch. 35) |

⚠️ **PIÈGE — le faux positif déclaré sans démonstration**
C'est la fuite la plus commune d'un processus de remédiation. Un constat gênant est marqué « faux positif » et disparaît. Sans preuve jointe, cette issue devient un moyen de vider la file sans travailler. **La règle** : un faux positif se clôt avec une démonstration vérifiable par un tiers, et un échantillon de faux positifs est recontrôlé chaque trimestre.

## 17.8 Vérification et clôture

La règle est brutale et sans exception : **on ne clôt pas sur déclaration, on clôt sur preuve**.

| Méthode de vérification | Fiabilité | Usage |
|---|---|---|
| Nouveau scan de l'actif | Bonne | Méthode par défaut |
| Relevé direct de l'état (§2.9) | **Meilleure** | Actifs critiques, campagnes importantes |
| Rapport de l'outil de déploiement | Correcte, sous les trois conditions du §2.9 | Volume |
| Déclaration du propriétaire | **Insuffisante seule** | Jamais comme unique preuve |

**Le délai de vérification** doit être borné : un ticket qui reste en état « à vérifier » plus de X jours est en réalité non clos, et il pollue les indicateurs en donnant l'illusion que le travail est fait. Suivez cet état comme un indicateur à part entière.

## 17.9 Réouverture et récurrence

**Une vulnérabilité corrigée qui réapparaît** est l'un des signaux les plus riches du MCS, et l'un des moins exploités.

**Les cinq causes racines**, avec leur remède :

| Cause | Mécanisme | Remède |
|---|---|---|
| **Image de référence non corrigée** | Chaque nouvelle machine naît vulnérable | Corriger le modèle, pas les instances (ch. 28) |
| **Restauration de sauvegarde** | Retour à un état antérieur au correctif | Contrôle post-restauration systématique |
| **Redéploiement automatique** | La définition déployée pointe une version ancienne | Corriger la définition, pas l'instance |
| **Retour arrière non suivi** | Un retour arrière a annulé le correctif sans que le ticket soit rouvert | Lier retour arrière et réouverture automatique |
| **Réinstallation manuelle** | Procédure d'installation obsolète | Mettre à jour la procédure |

**Le point d'organisation décisif** : une réapparition doit **rouvrir le ticket d'origine**, pas en créer un nouveau. Sinon la récurrence est invisible — chaque occurrence semble être un problème neuf — et la cause racine n'est jamais traitée. Un ticket rouvert trois fois est un signal, un ticket créé trois fois est du bruit.

✅ **BONNE PRATIQUE (P1)** — Suivez le **taux de récurrence** : constats réapparus rapportés aux constats clos sur la période. Un taux élevé n'indique pas une mauvaise exécution de la correction, il indique presque toujours un problème d'image de référence ou de processus de déploiement — donc un gain considérable si vous le traitez.

## 17.10 Piloter le *backlog*

Le *backlog* est l'ensemble des constats ouverts. Trois lectures en donnent l'état réel.

**Le vieillissement.** Répartition des constats ouverts par tranche d'ancienneté :

| Tranche | Lecture |
|---|---|
| < 30 j | Flux normal |
| 30-90 j | Zone d'attention |
| 90-180 j | Difficulté structurelle : dépendance externe, effort sous-estimé, propriétaire absent |
| > 180 j | **Ce ne sont plus des constats, ce sont des dérogations non formalisées** |

La dernière ligne est la plus importante du chapitre. Un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque **de fait**, prise par personne, revue par personne. La bonne action n'est pas de le corriger en urgence : c'est de le **qualifier** — dérogation, dépriorisation, ou correction planifiée avec engagement.

**L'écoulement.** Comparer entrées et sorties par période. Trois régimes possibles : la file se résorbe, elle est stable, elle grossit. Un *backlog* qui grossit malgré un travail intense signale un problème de capacité ou de périmètre, pas d'effort — et c'est un constat pour le comité stratégique.

**L'escalade.** Trois déclencheurs automatiques, sans intervention humaine : dépassement d'échéance, âge supérieur à un seuil, suspension prolongée. L'escalade suit les niveaux du §9.1.

## 17.11 Synchroniser scanner, outil de tickets et inventaire

Trois systèmes, trois référentiels d'actifs, trois vérités possibles. Les ruptures classiques :

| Rupture | Symptôme | Prévention |
|---|---|---|
| Identifiants d'actifs divergents | Le même serveur apparaît sous trois noms | Identifiant pivot commun (§10.3, §15.7) |
| Constat corrigé, ticket toujours ouvert | Le scan a détecté la correction, le ticket ne le sait pas | Synchronisation périodique de l'état |
| Ticket clos, constat toujours présent | Clôture sans vérification (§17.8) | Interdire la clôture sans preuve |
| Actif décommissionné, tickets orphelins | Tickets sur une machine qui n'existe plus | Chaînage avec le processus de décommissionnement (ch. 35) |
| Historique perdu au changement d'outil | Impossible de démontrer un progrès | Export périodique en format ouvert (§15.12) |

✅ **BONNE PRATIQUE (P0)** — **L'inventaire fait autorité.** Le scanner et l'outil de tickets s'y réfèrent, ils ne créent pas d'actifs. Toute divergence est un écart d'inventaire à traiter selon le §10.3, pas une bizarrerie d'outil à contourner.

## 17.12 📌 Ce qu'un outil de gestion ne réglera jamais

- **L'absence de propriétaire.** Un outil qui ne sait pas à qui affecter produit une file d'attente, pas une remédiation.
- **L'insuffisance de capacité.** Un *backlog* qui grossit ne se résout pas par une meilleure gestion du *backlog*.
- **La qualité de la preuve.** Un outil enregistre ce qu'on lui donne ; il ne vérifie rien.
- **Le contournement.** Si le processus est trop lourd, les corrections se feront hors outil, et vous perdrez à la fois la trace et la mesure. Le formalisme doit rester proportionné : dans une petite structure, une ligne dans un tableau tenu à jour vaut mieux qu'un outil que personne ne remplit.

## 17.13 ✅ Livrable — Le workflow de remédiation

**Ce qui doit être écrit et validé**, et qui constitue l'Annexe J :

1. Le **modèle d'états** du §17.6 et ses transitions autorisées.
2. Les **champs obligatoires** par état.
3. Les **règles de déduplication** et le modèle parent / enfants.
4. Les **règles d'échéance** : point de départ, suspensions limitatives, seuils d'escalade.
5. Les **issues possibles** et la preuve exigée pour chacune.
6. Les **règles de réouverture**.
7. Le **contrat de service interne** : délai de contestation d'affectation, délai de réponse, suppléance.

## 17.14 🔴 FIL ROUGE — mars 2027

3 800 constats, 21 campagnes, 187 tickets

Les 3 800 constats du scan de janvier, triés en février (§16.11), doivent maintenant être suivis. Malik Ferhaoui applique le modèle parent / enfants.

**La transformation du volume :**

| Étape | Volume |
|---|---|
| Constats bruts | 3 800 |
| Après déduplication par identifiant de vulnérabilité | 612 |
| Après regroupement par correctif | 244 |
| Après extraction des campagnes | **187 tickets + 21 campagnes** |

Les 187 tickets se répartissent en 23 en traitement unitaire, 140 déprioritisés avec date de revue, et 24 en attente d'un correctif éditeur — compteur suspendu, relance mensuelle.

**Le vieillissement révèle ce que le triage ne montrait pas.** Onze tickets dépassent 180 jours : ils datent des premiers scans de février 2026 et n'ont jamais été traités ni qualifiés. Ils concernent tous le même progiciel métier, dont l'éditeur exige une montée de version majeure facturée. Personne n'avait pris la décision — le sujet flottait entre l'exploitation, le métier et les achats.

Claire applique la règle du §17.10 : ce ne sont pas des constats en retard, ce sont des **dérogations non formalisées**. Elle les transforme en une dérogation unique, motivée, compensée par une restriction d'accès réseau, signée par le propriétaire métier, avec une date d'expiration alignée sur le budget 2028. Le *backlog* perd onze lignes ; l'organisation gagne une décision.

**Une découverte inattendue.** Le taux de récurrence sur les postes de travail atteint 18 % : près d'un constat clos sur cinq réapparaît dans les trois mois. L'analyse des cinq causes du §17.9 en identifie une seule : le modèle de machine virtuelle de mars 2024 (§3.9), jamais mis à jour. Chaque nouveau serveur créé depuis reproduit mécaniquement les mêmes constats. Corriger le modèle prend une demi-journée et supprime une source permanente de travail — ce que trois campagnes successives n'avaient pas réussi à faire.

**Ce que le comité retient.** Le nombre de « vulnérabilités ouvertes » a cessé d'être l'indicateur de référence. Il est remplacé par trois mesures : campagnes en cours et leur avancement, tickets dépassant leur échéance, et âge du plus ancien constat non qualifié. Ce dernier chiffre, en particulier, ne peut pas être embelli.

**Livrable de l'épisode.** Le workflow de remédiation d'HELIOMED, avec son modèle d'états et ses règles d'escalade — Annexe J.

→ La suite en 🔴 §18.14, lors de la nuit du déploiement raté sur le cluster de bases de données.

→ **Chapitre 18 — Le processus de correctif de bout en bout** : la chaîne complète d'un correctif, de la qualification à la preuve.

## Synthèse mentale du chapitre 17

Entre la décision de triage et la correction effective, le constat doit exister comme objet de gestion, avec un propriétaire, une échéance et un état — faute de quoi le travail se perd, se duplique et ne se démontre pas. Le modèle parent/enfants et quatre règles de déduplication transforment des milliers de constats en dizaines de tickets, à condition de regrouper par action de correction et non par ressemblance. Mesurez deux délais séparément : depuis la publication du correctif, qui donne votre exposition réelle, et depuis la détection, qui donne votre réactivité — leur écart mesure gratuitement la fraîcheur de votre détection. Chaque issue exige sa preuve, et le faux positif déclaré sans démonstration est la fuite la plus commune d'un processus de remédiation. Une réapparition rouvre le ticket d'origine, sinon la récurrence reste invisible et sa cause racine — presque toujours une image de référence — n'est jamais traitée. Enfin, un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque prise par personne : la bonne action est de le qualifier, pas de le corriger en urgence.

**Trois questions de vérification**

1. Votre file contient 3 800 constats. Décrivez les quatre étapes qui la ramènent à un nombre de tickets gérable, et le critère qui doit gouverner tout regroupement.
2. Un constat est clos comme faux positif. Que devez-vous exiger avant d'accepter cette clôture, et quel contrôle périodique mettez-vous en place ?
3. 18 % des constats clos sur les postes réapparaissent dans les trois mois. Quelles causes racines examinez-vous, dans quel ordre, et pourquoi corriger l'instance est-il ici une perte de temps ?

---
