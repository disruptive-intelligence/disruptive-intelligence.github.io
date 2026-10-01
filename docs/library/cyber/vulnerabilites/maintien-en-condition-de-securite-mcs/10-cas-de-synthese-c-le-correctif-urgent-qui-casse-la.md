---
title: Cas de synthèse C — Le correctif urgent qui casse la production
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - index.md
---

> **Format** — Cas d'arbitrage, à traiter en deux temps : la décision *avant*, puis l'analyse *après*. Durée estimée : **2 h 30**.
> **Livrables attendus** : instruction des deux risques · demande de changement (D.5) · critères go/no-go (D.6) · plan de retour arrière (D.7) · chronologie · compte rendu d'incident · plan d'amélioration.
> **Prérequis** : chapitres 6, 16, 18, 20, 26.

---

## C.1 Le dossier initial

**Nous sommes le vendredi 12 novembre 2027, 14 h 00.**

### Artefact 1 — l'avis reçu

> **Avis de sécurité éditeur — moteur de base de données — 12/11/2027 08:00 UTC**
>
> Une vulnérabilité affectant le traitement des connexions authentifiées permet à un utilisateur disposant de droits limités d'exécuter du code avec les privilèges du service.
> Gravité : **élevée**. Exploitation observée : **aucune à ce jour**.
> Versions affectées : `15.x` antérieures à `15.4.2`.
> Correctif : `15.4.2`, publié le 12/11/2027 à 06:00 UTC.
>
> *Notes de version — extrait, page 4, section « Modifications internes » :*
> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. Une mise à jour simultanée de tous les membres d'un groupe de réplication est requise. »*

### Artefact 2 — le cluster concerné

```yaml
id_actif: CLU-HELIOLINK-BDD
type: base_de_donnees
role: stockage principal de la plateforme de télésuivi HelioLink
version: "15.3.1"
topologie: 3 nœuds — 1 primaire, 2 réplicas synchrones
criticite: C1
exposition: administration        # non publié sur Internet
joignable_depuis: serveurs applicatifs HelioLink (eux-mêmes exposés)
fenetre_maintenance: "samedi 22h-02h"
proprietaire_metier: y.prigent
proprietaire_technique: m.ferhaoui
utilisateurs_finaux: 34 établissements de santé, ~4 200 patients suivis
```


### Artefact 3 — l'environnement de recette

```yaml
id_actif: REC-HELIOLINK-BDD
version: "15.3.1"
topologie: 1 nœud unique — PAS de réplication
volumetrie: 2 % de la production
integrations: 3 sur 7 simulées
configuration: dérive non mesurée depuis 2026
derniere_synchronisation_donnees: 2027-04-15
```


### Artefact 4 — la politique applicable

| Classe | Délai — critique non exploitée |
|---|---|
| **C1** | **15 jours** |

### Artefact 5 — la proposition de l'équipe

> *Courriel de M. Ferhaoui, 12/11/2027 14 h 12 :*
> « Vulnérabilité élevée sur le cluster HelioLink, correctif dispo. Je propose de l'appliquer demain soir dans la fenêtre habituelle, pour ne pas laisser traîner. C'est une version mineure, ça devrait bien se passer. »

### Artefact 6 — antécédents

- Le correctif a été publié il y a **6 heures**. Aucun retour communautaire n'est encore disponible.
- Le dernier retour arrière testé sur ce cluster date de **mars 2026**, sur un nœud isolé.
- La plateforme HelioLink dispose de deux indicateurs fonctionnels : *remontées de télésuivi abouties par minute* et *sessions établissement actives*.

---

## C.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | Instruisez les deux risques **en parallèle**. | Tableau à deux colonnes |
| 2 | Quelle décision prenez-vous le vendredi 12 à 17 h ? | Décision tracée |
| 3 | Le scénario applique le correctif le samedi. Reconstituez ce qui se passe. | Chronologie |
| 4 | Identifiez les causes racines, et ce qui a bien fonctionné. | Compte rendu |
| 5 | Rédigez le plan d'amélioration. | Plan daté |
| 6 | Distinguez erreur humaine, erreur de conception, erreur de processus. | Analyse |

---

## C.3 Corrigé — instruire les deux risques en parallèle

C'est la méthode centrale du cas. On n'instruit pas « faut-il corriger ? », mais **deux questions symétriques**, dans deux colonnes, avec les mêmes exigences de preuve.

| **Risque de NE PAS corriger** | **Risque de corriger maintenant** |
|---|---|
| Exploitation observée ? **Non** (artefact 1) | Correctif publié depuis **6 h** — retours communautaires ? **Aucun** |
| Exposition directe ? **Non** — cluster non publié | Recette représentative ? **Non** : 1 nœud contre 3, **pas de réplication** |
| Exposition indirecte ? **Oui** — via les serveurs applicatifs exposés | Volumétrie de recette : **2 %** de la production |
| Privilèges requis ? **Compte authentifié à droits limités** | Intégrations : **3 sur 7 simulées** |
| Actif critique ? **Oui** — C1, données de santé, 34 établissements | Retour arrière testé sur cette topologie ? **Non** — dernier test en 2026, sur un nœud isolé |
| Délai politique disponible ? **15 jours** | Notes de version lues intégralement ? **À faire** |
| Que se passe-t-il si on attend 10 jours ? Risque marginal supplémentaire **faible** | Que se passe-t-il si ça casse ? **Indisponibilité d'un service de télésuivi médical** |

### La lecture

Le déséquilibre est net. La colonne de gauche ne présente **aucune urgence caractérisée** : pas d'exploitation, pas d'exposition directe, privilèges préalables requis. La colonne de droite présente **quatre inconnues et une lacune avérée** — la recette ne représente pas la production sur la dimension exacte que le correctif touche.

**La décision correcte est d'utiliser le délai disponible.**

⚠️ **Le biais à nommer explicitement.** L'artefact 5 dit *« pour ne pas laisser traîner »*. C'est une préférence psychologique, pas une analyse de risque. Elle est l'erreur symétrique du report perpétuel du §12.7 — et elle est bien moins souvent dénoncée, parce qu'elle a l'apparence de la diligence.

**La formulation à retenir** : *un délai accordé par la politique est une ressource, pas un retard. Il existe précisément pour permettre de tester. L'utiliser n'est pas de la négligence.*

### Ce qui aurait renversé la décision

Il est important de savoir ce qui aurait justifié d'agir samedi :

| Élément | Effet |
|---|---|
| Exploitation observée dans le monde | Bascule vers la feuille « traiter » à 7 jours |
| Exploitation observée dans le secteur santé | Bascule vers l'urgence |
| Cluster directement exposé | Bascule vers l'urgence |
| Recette représentative disponible | Le risque de changement chute — samedi devient raisonnable |

---

## C.4 Corrigé — la lecture des notes de version

L'information décisive est à la **page 4, section « Modifications internes »** de l'artefact 1 :

> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. »*

**Ce que cela signifie concrètement** : la mise à jour nœud par nœud — la méthode standard sur un cluster — **est impossible** sur ce correctif. Elle produit un cluster dont les membres ne peuvent plus se synchroniser.

C'est exactement la question n° 2 de la qualification en six questions du §18.2 : *quels prérequis exige-t-il ?* La réponse était disponible dès 8 h du matin, dans un document de quatre pages.

⚠️ **Pourquoi cette ligne se rate.** Elle ne figure ni dans le résumé, ni dans la section sécurité, ni dans les correctifs listés : elle est dans une rubrique « modifications internes » que rien ne signale comme critique. C'est le cas général — **la qualification consiste à lire les notes de version en entier, pas à les parcourir**.

---

## C.5 Corrigé — la chronologie du samedi

Le scénario applique le correctif malgré tout. Voici ce qui se produit.

| Heure | Événement | Ce qui manquait |
|---|---|---|
| 22:00 | Début de la fenêtre. Instantanés des trois machines virtuelles pris | — |
| 22:40 | Nœud réplica 2 mis à jour en `15.4.2`, redémarre normalement | — |
| **22:55** | **La réplication ne repart pas.** Le nœud en v3 refuse de se synchroniser depuis le primaire en v2 | La ligne de la page 4 |
| 23:00 | Diagnostic : recherche dans les journaux, puis dans les notes de version | Qualification préalable |
| **23:10** | **Décision de retour arrière — après 15 minutes de discussion** | Critères d'arrêt écrits, décideur nommé |
| 23:25 | Instantané restauré sur le réplica 2. Le nœud revient en `15.3.1` | — |
| **23:30** | **La réplication ne repart toujours pas** : le nœud restauré accuse 40 minutes de retard de transactions, au-delà du seuil de rattrapage automatique | Test du retour arrière sur topologie représentative |
| 23:45 | Décision : resynchronisation complète du réplica depuis le primaire | — |
| 00:10 | Resynchronisation en cours. Le cluster fonctionne en mode dégradé — un seul réplica | — |
| 01:20 | Resynchronisation terminée, cluster nominal, service rétabli | — |

**Bilan** : **4 heures d'indisponibilité partielle** de la plateforme de télésuivi, un dimanche matin. **Aucune donnée perdue.** Deux établissements clients ont appelé le support.

### Ce qui aurait pu être pire

Le scénario s'arrête au réplica. Si la séquence avait commencé par le **primaire**, l'indisponibilité aurait été **totale**, et le retour arrière aurait exigé une restauration de sauvegarde avec perte des transactions depuis l'instantané — c'est-à-dire des données de télésuivi de 34 établissements.

**Le choix de commencer par un réplica est la seule décision de la nuit qui relève de la bonne pratique.** Elle mérite d'être nommée dans le retour d'expérience.

---

## C.6 Corrigé — causes racines et ce qui a fonctionné

### Les quatre causes racines

| # | Cause | Ce qui l'aurait évitée | Coût de la prévention |
|---|---|---|---|
| 1 | **Notes de version parcourues, pas lues** | Qualification en six questions du §18.2, avec référence de la section consultée | 20 minutes |
| 2 | **Recette non représentative sur la dimension touchée** | Mesure de l'écart sur les quatre axes du §6.12, **déclarée dans la demande de changement** | 1 h, puis constat bloquant |
| 3 | **Retour arrière testé sur une topologie non représentative** | Test sur cluster, chronométré (§18.8) | 1/2 journée, une fois |
| 4 | **Aucun critère d'arrêt écrit, aucun décideur nommé** | Formulaire D.6 rempli avant l'intervention | 15 minutes |

**La cause 2 est la cause dominante.** Les causes 1, 3 et 4 aggravent, mais c'est l'écart de recette qui rend l'incident inévitable : aucun test sur un nœud unique ne pouvait révéler un problème de réplication.

### Ce qui a bien fonctionné — à nommer explicitement

| Élément | Pourquoi c'est important |
|---|---|
| La fenêtre était correcte | Samedi soir, usage minimal |
| L'astreinte était présente | Deux personnes, jusqu'à 1 h 20 |
| Les instantanés existaient et étaient récents | Sans eux, restauration de sauvegarde |
| **La séquence a commencé par un réplica** | A évité une indisponibilité totale |
| Aucune donnée n'a été perdue | Le pire scénario a été évité |
| La resynchronisation a fonctionné | Le mécanisme de secours était opérationnel |

⚠️ **Un retour d'expérience qui ne liste que les défaillances produit deux effets pervers** : il décourage l'équipe, et il fait disparaître les pratiques à préserver. La prochaine campagne pourrait « optimiser » en commençant par le primaire.

---

## C.7 Corrigé — ce qu'il aurait fallu faire

| Moment | Action | Livrable |
|---|---|---|
| **Ven. 14:00** | Qualification en six questions. **Lire les notes de version en entier** | Fiche de qualification |
| Ven. 15:30 | Constat : mise à jour simultanée requise, pas de mise à jour nœud par nœud | — |
| Ven. 16:00 | Mesure de l'écart recette/production sur les quatre axes. Constat : **bloquant** | Section de D.5 |
| **Ven. 17:00** | **Décision : utiliser le délai de 15 jours.** Tracée, avec justification | Décision datée |
| Ven. 17:15 | Compensation dans l'intervalle : restreindre l'accès au cluster aux seuls serveurs applicatifs · surveillance des connexions authentifiées inhabituelles · destinataire nommé | Fiche §20.7 |
| Sem. 1 | Monter un cluster de recette à **3 nœuds** avec réplication | Environnement |
| Sem. 1 | Tester le correctif **et le retour arrière** sur cette topologie. Chronométrer | D.7 rempli |
| Sem. 2 | Écrire les critères go/no-go, avec les deux indicateurs fonctionnels | D.6 rempli |
| **Sam. sem. 2** | Déploiement en fenêtre, séquence validée par le test | Chronologie |
| Après | Écart de recette inscrit au plan d'amélioration | Plan daté |

### Les livrables remplis

**D.6 — critères go/no-go**

| Indicateur | Seuil d'arrêt | Mesuré par |
|---|---|---|
| Réplication rétablie après mise à jour d'un nœud | `> 5 min` | Console du moteur |
| **Remontées de télésuivi abouties/min** | `baisse > 10 % sur 15 min` | Supervision applicative |
| **Sessions établissement actives** | `baisse > 5 %` | Supervision applicative |
| Erreurs applicatives | `> 20/min` | Journaux |
| **Décideur du retour arrière** | **M. Ferhaoui**, sans validation supplémentaire | — |

**D.7 — plan de retour arrière**

| Champ | Contenu |
|---|---|
| Mécanisme | Instantané des trois machines virtuelles + resynchronisation depuis le primaire |
| **Testé le** | `[date]` — sur cluster 3 nœuds représentatif |
| **Durée mesurée** | `[hh:mm]` — chronométrée lors du test |
| Périmètre couvert | Binaires, configuration, **format de réplication** |
| **Point de non-retour** | **Mise à jour du primaire** : au-delà, tout retour arrière exige une restauration de sauvegarde |
| Ce que le retour arrière ne restaure pas | Transactions depuis l'instantané · état des connexions établissement |

---

## C.8 Corrigé — erreur humaine, de conception, de processus

C'est la question la plus importante du cas, et la plus mal traitée en pratique.

| Type | Ce qui s'est passé | Le bon niveau de traitement |
|---|---|---|
| **Erreur humaine** | Malik Ferhaoui n'a pas lu la page 4 des notes de version | Aucune sanction n'est appropriée : il a suivi une procédure qui ne l'exigeait pas |
| **Erreur de conception** | L'environnement de recette ne reproduit pas la topologie de production | Décision d'investissement — c'est le §6.12 et le §6.13 |
| **Erreur de processus** | La qualification n'était pas un champ obligatoire · les critères d'arrêt n'étaient pas exigés · le retour arrière n'avait pas à être testé sur topologie représentative | **C'est ici que se corrige l'incident** |

### Le principe à retenir

> Un retour d'expérience porte sur le **processus**, jamais sur les personnes. Quand une personne compétente, appliquant la procédure existante, produit un incident, le défaut est dans la procédure.

**Le test qui tranche** : *une autre personne, à la place de Malik, aurait-elle fait autrement ?* Ici, non — rien dans le processus ne l'y obligeait. Le défaut est donc structurel.

⚠️ **Le contre-exemple**, pour ne pas tomber dans l'excès inverse : si la procédure avait exigé la qualification en six questions et qu'elle avait été délibérément contournée pour gagner du temps, ce serait une erreur d'application — qui appelle un traitement différent, mais toujours pas une sanction en première intention : la question devient *pourquoi la procédure a-t-elle paru contournable ?*

---

## C.9 Le plan d'amélioration

| # | Action | Prio | Échéance | Propriétaire |
|---|---|---|---|---|
| 1 | Qualification en six questions rendue **champ obligatoire** du dossier de campagne C1, avec référence de la section des notes de version consultée | **P0** | Immédiat | RSSI |
| 2 | Critères d'arrêt et décideur du retour arrière écrits **avant** toute intervention C1 (D.6) | **P0** | Immédiat | Exploitation |
| 3 | **Écart recette/production mesuré sur les quatre axes** et déclaré dans chaque demande de changement | **P0** | 1 mois | Exploitation |
| 4 | Cluster de recette à 3 nœuds pour HelioLink | P1 | T1 2028 | DSI — budget |
| 5 | Retour arrière testé sur topologie représentative, **chronométré**, une fois par an et après tout changement d'architecture | P1 | T1 2028 | Exploitation |
| 6 | Point de non-retour identifié et écrit dans toute demande de changement touchant un composant à état | P1 | 1 mois | Exploitation |
| 7 | Les deux indicateurs fonctionnels HelioLink intégrés aux critères d'arrêt par défaut | P2 | T1 2028 | Produit |

---

## C.10 Critères d'évaluation

| Critère | Pts | Attendu |
|---|---|---|
| Instruction des **deux** risques en colonnes symétriques | 20 | Ne pas se contenter d'évaluer la vulnérabilité |
| Détection de la ligne des notes de version | 15 | Lire l'artefact 1 en entier |
| Décision d'utiliser le délai, **avec justification écrite** | 20 | Le cœur du cas |
| Compensation posée pendant l'attente | 10 | Attendre n'est pas ne rien faire |
| Identification de l'écart de recette comme cause dominante | 15 | Distinguer cause dominante et facteurs aggravants |
| Ce qui a bien fonctionné, nommé | 10 | Notamment le choix de commencer par un réplica |
| Distinction des trois types d'erreur | 10 | Le défaut est dans la procédure |

**Seuil de réussite** : 70/100. **Élimination** : conclure que l'incident résulte d'une faute individuelle.

---

## C.11 Variante — la même situation avec exploitation active

Mêmes artefacts, sauf l'artefact 1 : *« exploitation active observée dans le secteur de la santé »*.

**Ce qui change, et ce qui ne change pas** :

| Élément | Sans exploitation | Avec exploitation active |
|---|---|---|
| Décision | Utiliser les 15 jours | **Agir sous 72 h** |
| Lecture des notes de version | Obligatoire | **Toujours obligatoire** — c'est ce qui prend 20 minutes et évite l'incident |
| Écart de recette | Motif de report | **Motif de prudence accrue**, pas de report |
| Séquence | Testée d'abord | Réplica d'abord, observation courte, primaire ensuite |
| Critères d'arrêt | Écrits | **Toujours écrits** — leur suppression n'est jamais un gain de temps |
| Compensation | Pendant l'attente | **Pendant l'intervention** : restriction d'accès maintenue jusqu'à vérification |
| Retour arrière | Testé avant | **Non testable faute de temps** — le déclarer explicitement comme risque assumé, et le dire à la direction |

**Le point que cette variante enseigne** : l'urgence comprime le délai d'observation et la validation, **jamais la qualification, les critères d'arrêt ni la preuve** (§21.8). Ces trois éléments coûtent moins d'une heure au total, et ce sont eux qui permettent de se tromper sans catastrophe.

---
