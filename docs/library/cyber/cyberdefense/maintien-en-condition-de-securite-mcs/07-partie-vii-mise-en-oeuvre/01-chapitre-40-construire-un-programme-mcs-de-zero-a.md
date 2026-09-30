---
title: Chapitre 40 — Construire un programme MCS de zéro à douze mois
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE VII — Mise en œuvre
  - index.md
---

#### 40.1 Le diagnostic en quinze jours : six questions

Avant tout plan, situez l'organisation. Six questions suffisent, et les réponses se trouvent en deux semaines.

| # | Question | Ce que la réponse révèle |
|---|---|---|
| 1 | **Combien d'actifs devons-nous maintenir ?** Et quel est l'écart entre vos sources ? | La fiabilité de tout indicateur futur (ch. 10) |
| 2 | **Qui décide qu'on arrête tel actif pour le corriger ?** | L'existence ou non d'une propriété d'actif (§5.5) |
| 3 | **Quels actifs sont joignables depuis Internet ?** | Le risque réel immédiat (ch. 11) |
| 4 | **Quand a-t-on appliqué le dernier correctif, et comment le prouve-t-on ?** | La capacité à produire une preuve (§2.9) |
| 5 | **Que fait-on quand on ne peut pas corriger ?** | L'existence d'un chemin légitime pour les écarts (§7.4) |
| 6 | **Combien d'actifs sont hors support, et qu'a-t-on décidé ?** | La dette et sa reconnaissance (ch. 12) |

**La lecture des réponses.** Si les questions 1 et 2 n'ont pas de réponse, ne commencez rien d'autre. Si la question 3 n'a pas de réponse, c'est votre première action — elle produit des fermetures immédiates (§11.8). Si la question 5 n'a pas de réponse, votre organisation dissimule ses écarts sans le savoir.

#### 40.2 Jours 0-30 : établir le socle

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Croiser 4 sources d'inventaire, dont une non technique | Périmètre de référence avec ses écarts |
| **P0** | Attribuer criticité et exposition, même grossièrement | Base des classes de service |
| **P0** | Lancer la campagne de désignation des propriétaires | Liste nominative, actifs orphelins identifiés |
| **P0** | Exercice de découverte externe | Carte des actifs exposés |
| **P0** | **Fermer les expositions inutiles** | Réduction de risque immédiate, sans correctif |
| **P0** | Publier le périmètre **avec ses zones non couvertes** | Crédibilité de tous les chiffres ultérieurs |
| P1 | Identifier les actifs de niveau 0 | Liste d'une page (§11.7) |
| P1 | Vérifier les cinq configurations du §22.1 sur ces actifs | Gains rapides sans fenêtre |

**Ce qu'on ne fait pas pendant ce mois** : acheter un outil, publier un taux de conformité, lancer une campagne de correctifs massive.

#### 40.3 Jours 30-90 : poser la règle

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Rédiger la politique MCS avec ses classes de service | Politique v1, délais tenables (§7.2) |
| **P0** | Créer la procédure de dérogation | Chemin légitime pour les écarts |
| **P0** | Constituer la matrice de couverture de veille | Trous identifiés (§14.1) |
| **P0** | Écrire l'arbre de décision de triage | Priorisation défendable (§16.3) |
| P1 | Mettre en place le workflow de remédiation | File unique, états, échéances (ch. 17) |
| P1 | Installer la comitologie | Comité MCS mensuel avec relevé de décisions |
| P1 | **Premier cycle complet mesuré** | De la détection à la preuve, sur un périmètre restreint |

**Le premier cycle complet est le livrable clé de cette phase.** Mieux vaut un cycle entier réussi sur 40 actifs qu'un cycle partiel sur 400 : il révèle tous les points de rupture de la chaîne, à faible coût.

#### 40.4 Jours 90-180 : industrialiser

| Prio | Action |
|---|---|
| **P0** | Consolider le reporting **par le périmètre**, pas par les outils (§19.8) |
| **P0** | Traiter le trou des applications tierces du poste de travail (§19.5) |
| P1 | Mettre en place les anneaux de déploiement et les critères d'arrêt |
| P1 | Dériver une *baseline* de configuration et automatiser son contrôle |
| P1 | Constituer le référentiel de fin de support et le plan d'obsolescence |
| P1 | Publier les premiers indicateurs, avec leurs définitions |
| P1 | Revue des comptes de service et des accès à privilèges (ch. 24) |
| P2 | Négocier les clauses MCS avec les prestataires (§13.3) |

#### 40.5 Jours 180-365 : étendre et prouver

| Prio | Action |
|---|---|
| **P0** | Étendre aux périmètres déclarés non couverts, dans l'ordre de leur risque |
| **P0** | Constituer le dossier de preuves en continu (§39.2) |
| P1 | Traiter l'industriel, avec l'équipe de maintenance (ch. 29) |
| P1 | Traiter le cloud et les services en ligne (ch. 30, 31) |
| P1 | Traiter la non-production et les actifs d'administration (ch. 28) |
| P1 | Mettre en place le décommissionnement avec procès-verbal (ch. 35) |
| P1 | Automatiser collecte, corrélation et vérification (§36.1) |
| P2 | Module produit, si applicable (ch. 33) |
| P2 | Premier audit interne par sondages (§39.4) |

#### 40.6 Adapter au contexte

| Contexte | Ce qui change |
|---|---|
| **PME (< 200 actifs)** | Formalisme allégé : un tableau tenu à jour remplace un outil. Les rôles se cumulent, mais restent distingués mentalement (§9.6). Priorité absolue à l'exposition et aux actifs de niveau 0 |
| **ETI** | Le modèle décrit ici. Le point critique est la propriété d'actif et la comitologie |
| **Groupe multi-sites** | Modèle mixte : classes, délais et format de preuve définis centralement ; exécution locale (§9.5) |
| **Parc entièrement infogéré** | Le programme démarre par le contrat (ch. 13), pas par la technique. Sans clause de restitution, aucune mesure n'est possible |
| **Organisation industrielle** | Deux programmes parallèles, avec des rythmes différents (ch. 29). Ne jamais imposer le rythme bureautique à l'usine |

#### 40.7 Les erreurs de séquencement les plus coûteuses

| Erreur | Conséquence |
|---|---|
| **Acheter un outil avant l'inventaire** | Automatiser un périmètre inconnu, tableaux de bord verts sur dénominateur faux |
| Publier un taux de conformité avant de connaître son dénominateur | Perte de crédibilité irréversible au premier audit |
| Lancer une campagne massive avant d'avoir des propriétaires | Blocage au premier refus, découragement de l'équipe |
| Écrire une politique avant de mesurer sa capacité | Non-conformité permanente (§7.2) |
| Traiter l'industriel avec les méthodes bureautiques | Rejet, et perte durable de l'accès (ch. 29) |
| Négliger les actifs de niveau 0 parce qu'ils ne sont pas exposés | Le chemin le plus court reste ouvert (§34.12) |
| Reporter la preuve à plus tard | Impossible à reconstituer, et budget non pérennisé |

#### 40.8 ✅ Feuille de route consolidée

**P0 — sans quoi rien ne fonctionne**

1. Périmètre de référence, croisé sur plusieurs sources, publié avec ses zones non couvertes.
2. Propriétaires nommés, avec procédure pour les actifs orphelins.
3. Carte des actifs exposés, et fermeture des expositions inutiles.
4. Liste des actifs de niveau 0, tous en classe C1.
5. Politique avec classes de service et délais **tenables**.
6. Procédure de dérogation, avec date d'expiration et compensation.
7. Arbre de décision de triage, écrit et daté.
8. Preuve d'état sur échantillon, indépendante des outils.

**P1 — ce qui rend le dispositif durable**

9. File unique et workflow de remédiation avec escalade automatique.
10. Anneaux de déploiement et critères d'arrêt chiffrés.
11. Matrice de couverture de veille, et traitement des trous.
12. Référentiel de fin de support et plan d'obsolescence financé.
13. *Baseline* de configuration dérivée et contrôlée.
14. Revue des comptes de service, des secrets et des certificats.
15. Clauses contractuelles avec les prestataires, dont la restitution de données.
16. Indicateurs définis, historisés, publiés par population.

**P2 — ce qui fait la différence dans la durée**

17. Automatisation de la collecte, de la corrélation et de la vérification.
18. Décommissionnement avec procès-verbal et vérification à J+90.
19. Exigences de maintenabilité dans les cahiers des charges (§6.2).
20. Audit interne périodique par sondages.

🖼 **SCHÉMA — La chaîne complète du MCS.** *Poster récapitulatif pleine page reprenant les six segments avec leurs chapitres. Destiné à l'impression séparée.*

#### 40.9 La chaîne complète, en une page

Le schéma directeur du §1.1, déplié avec ses chapitres. C'est la page à garder sous la main.

```
  ┌─ ① CONNAÎTRE ──────────────────────────────────────────────────┐
  │  Inventaire (10) ─► Propriété (5) ─► Criticité + Exposition (11)│
  │  Obsolescence (12) ─► Délégué (13)                              │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ② OBSERVER ───────────────────────────────────────────────────┐
  │  Veille toutes origines (14) ─► Détection technique (15)        │
  │  Faits / hypothèses / pistes (14.7)                             │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ③ DÉCIDER ────────────────────────────────────────────────────┐
  │  Arbre de décision (16) ─► File unique, 2 horloges (17)         │
  │  Exploitation × Exposition × Criticité                          │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ④ CORRIGER, COMPENSER OU DÉROGER ─────────────────────────────┐
  │  Campagne : qualifier ─► tester ─► anneaux ─► arrêt auto (18-19)│
  │  Impossible ? hiérarchie des compensations (20)                 │
  │  Configuration (22-23) · Identités (24) · Code (25-26)          │
  │  Couches basses (27) · Non-production (28)                      │
  │  Contextes : OT (29) · Cloud (30) · SaaS (31) · Legacy (32)     │
  │  Urgence ? réduire l'exposition d'abord (21)                    │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ⑤ VÉRIFIER ───────────────────────────────────────────────────┐
  │  Technique ─► effectivité (redémarrage) ─► fonctionnelle (18.9) │
  │  Traîne longue qualifiée (18.10)                                │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ⑥ PROUVER ────────────────────────────────────────────────────┐
  │  Preuve d'état (2.9) ─► Indicateurs (38) ─► Dossier (39)        │
  │  Décommissionnement (35) ─► retour au périmètre ①               │
  └──────────────────────────────┬─────────────────────────────────┘
                                 │
      ┌──────────────────────────┴──────────────────────────┐
      │  EN PERMANENCE                                       │
      │  Gouvernance (9) · Économie et soutenabilité (37)     │
      │  Automatisation (36) · MCS by design (6)              │
      └──────────────────────────────────────────────────────┘
```


**Les six règles qui résument tout le cours**

1. On ne maintient pas ce qu'on ne connaît pas — et le dénominateur inconnu rend tous les indicateurs faux, dans le sens favorable.
2. Un actif sans propriétaire nommé n'est pas un actif maintenu ; il reste dans le périmètre.
3. L'exposition et la criticité métier ne sont produites par personne d'autre que vous.
4. Fermer une exposition inutile protège aussi contre les vulnérabilités futures.
5. Un délai accordé par la politique est une ressource, pas un retard.
6. Ce qui n'est pas prouvé ne se pilote pas, ne se finance pas, et ne se défend pas.

#### Synthèse mentale du chapitre 40

Six questions suffisent à situer une organisation en quinze jours, et deux d'entre elles sont bloquantes : combien d'actifs, et qui décide de les arrêter. Le premier mois établit le socle sans acheter d'outil, sans publier de taux et sans lancer de campagne massive — il ferme en revanche les expositions inutiles, ce qui produit une réduction de risque immédiate. Le premier cycle complet, de la détection à la preuve, vaut mieux réussi sur quarante actifs que partiel sur quatre cents : il révèle tous les points de rupture à faible coût. Les erreurs de séquencement les plus coûteuses consistent à outiller avant d'inventorier, à publier un taux avant d'en connaître le dénominateur, et à reporter la preuve — laquelle est impossible à reconstituer après coup. Enfin, dans un parc infogéré, le programme démarre par le contrat et non par la technique.

**Trois questions de vérification**

1. Vous prenez un poste de responsable sécurité dans une organisation sans dispositif de MCS. Quelles sont vos deux premières questions, et pourquoi bloquent-elles tout le reste ?
2. Votre direction veut voir un taux de conformité dès le premier mois. Que répondez-vous, et que proposez-vous à la place ?
3. Pourquoi vaut-il mieux réussir un cycle complet sur quarante actifs qu'un cycle partiel sur quatre cents ?

---


## Cas de synthèse

Les trois cas qui suivent se travaillent en situation, les annexes ouvertes. Chacun reprend le fil rouge HELIOMED à un moment précis, fournit les données disponibles à cet instant, et demande des décisions. Les corrigés commentent aussi les **erreurs volontairement insérées** dans les scénarios.

---
