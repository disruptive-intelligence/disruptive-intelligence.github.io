---
title: PARTIE VII — Mise en œuvre
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 8
chapters: 10
---

---

### Chapitre 40 — Construire un programme MCS de zéro à douze mois

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

### Cas de synthèse A — 0-day activement exploitée sur la passerelle d'accès distant

> **Format** — Cas à traiter en situation, annexes ouvertes. Durée estimée : **3 heures** en individuel, une demi-journée en groupe.
> **Livrables attendus** : journal de crise (D.11) · demande de changement urgent (D.5) · critères go/no-go (D.6) · note à la direction · retour d'expérience.
> **Prérequis** : chapitres 11, 14, 16, 18, 20, 21, 27, 34.

---

#### A.1 Le dossier initial

**Vous êtes** Claire Nadeau, RSSI du groupe HELIOMED. Nous sommes le **jeudi 9 juillet 2027, 8 h 40**.

##### Artefact 1 — l'alerte reçue

> **CERT sectoriel — Alerte ALT-2027-0714 — 09/07/2027 07:52 UTC — Niveau : critique**
>
> Une vulnérabilité affectant les passerelles d'accès distant du constructeur `[X]` fait l'objet d'une **exploitation active** confirmée chez plusieurs entités européennes du secteur de la santé. La vulnérabilité permet une exécution de code à distance **sans authentification préalable** sur l'interface d'administration du produit.
>
> Versions affectées : `4.2.x` antérieures à `4.2.19`, `4.4.x` antérieures à `4.4.7`.
> Correctif : publié par le constructeur le 09/07/2027 à 02:10 UTC.
> Contournement : restriction d'accès à l'interface d'administration.
>
> Le CERT recommande une vérification immédiate des équipements exposés et une recherche d'indicateurs de compromission.

##### Artefact 2 — extrait de l'inventaire, `GW-VPN-01` / `GW-VPN-02`

```yaml
id_actif: GW-VPN-01              # couple haute disponibilité avec GW-VPN-02
type: securite
modele: passerelle d'accès distant
version_logicielle: "4.2.11"
mis_en_service: 2022-03-14
derniere_mise_a_jour: 2025-11-08
criticite: C1
exposition: internet
proprietaire_metier: s.weber
proprietaire_technique: m.ferhaoui
fenetre_maintenance: "mardi 22h-02h, urgence pré-autorisée sous 72h"
journalisation: locale, rétention 30 jours, PAS d'export externe
utilisateurs_actifs_30j: 210
outils_couverture: [scan:non — appliance fermée]
```

##### Artefact 3 — configuration réseau publiée

```
# Règles de publication, extraction du 09/07/2027 08:15

ALLOW  0.0.0.0/0        -> gw-vpn.heliomed.fr:443/tcp   "service accès distant"      [active depuis 2022-03-14]
DENY   0.0.0.0/0        -> gw-vpn.heliomed.fr:8443/tcp  "interface administration"   [modifiée le 2026-09-22]
ALLOW  10.0.0.0/8       -> gw-vpn.heliomed.fr:8443/tcp  "administration interne"     [active depuis 2026-09-22]
```

##### Artefact 4 — journal des changements de l'équipement

```
2022-03-14  Mise en service, version 4.2.3
2022-03-14  Publication 443/tcp et 8443/tcp — demande CHG-2022-0341
            motif : "télétravail massif, accès administration depuis l'extérieur"
            durée demandée : "temporaire, le temps de la période"
2023-06-02  Mise à jour 4.2.3 -> 4.2.7
2025-11-08  Mise à jour 4.2.7 -> 4.2.11
2026-09-22  Fermeture 8443/tcp depuis Internet — suite exercice de découverte externe
2027-07-09  [aucune action]
```

##### Artefact 5 — état de la journalisation

| Source | Rétention | Export externe | Contenu |
|---|---|---|---|
| Journaux de la passerelle | **30 jours**, sur l'équipement | **Non** | Connexions, authentifications, actions d'administration |
| Journaux du pare-feu amont | 12 mois, exportés | Oui | Flux, sans contenu applicatif |
| Journaux d'annuaire | 12 mois, exportés | Oui | Authentifications des utilisateurs |

##### Artefact 6 — contraintes du jour

- 210 collaborateurs utilisent l'accès distant, dont **7 en déplacement** ce jour (2 en clientèle hospitalière, 5 sur un salon professionnel).
- L'équipe disponible : Malik Ferhaoui, un ingénieur d'astreinte, vous-même.
- Le comité MCS du mois a lieu le mardi suivant.
- La police d'assurance impose une déclaration conservatoire **sous 72 h** en cas d'incident de sécurité présumé.

---

#### A.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous entre H+0 et H+2 ? Justifiez chaque décision. | Journal D.11, premières lignes |
| 2 | Quelle question devez-vous poser que les artefacts ne posent pas ? | — |
| 3 | Quel niveau de qualification retenez-vous, et pourquoi ? | — |
| 4 | Rédigez la phrase exacte que vous dites à la direction générale. | Note de situation |
| 5 | Que comprimez-vous du processus normal, que conservez-vous ? | D.5 + D.6 |
| 6 | Corriger ou reconstruire ? Sur quel critère ? | Décision tracée |
| 7 | Quatre erreurs sont volontairement présentes dans le dossier. Lesquelles ? | — |
| 8 | Variante : mêmes faits, organisation de 40 personnes sans astreinte. | — |

---

#### A.3 Corrigé — heures 0 à 2

##### H+0 — qualifier à la source

**Ce qu'il ne faut pas faire** : agir sur la foi de l'alerte relayée. **Ce qu'il faut faire** : ouvrir l'avis du constructeur et comparer.

| Vérification | Résultat |
|---|---|
| Version installée `4.2.11` dans la plage affectée `< 4.2.19` ? | **Oui** |
| Correctif disponible ? | Oui, `4.2.19`, publié il y a 6 h |
| Contournement officiel ? | Oui : restreindre l'accès à l'interface d'administration |
| Statut de qualification (§14.7) | **Fait vérifié** |

⚠️ Le second équipement `GW-VPN-02` doit être vérifié **séparément** : rien ne garantit que les deux membres du couple portent la même version. C'est une vérification de trente secondes que la pression fait sauter.

##### H+1 — mesurer l'exposition

Les trois questions du §11.1 appliquées aux artefacts 2 et 3 :

| Question | Réponse | Source |
|---|---|---|
| **Depuis où est-il joignable ?** | Le service d'accès distant `443/tcp` est publié sur Internet. L'interface d'administration `8443/tcp` **ne l'est plus depuis le 22/09/2026** | Artefact 3 |
| **Par qui ?** | Anonyme sur `443`, réseau interne sur `8443` | Artefact 3 |
| **Vers quoi mène-t-il ?** | Réseau interne complet — c'est une passerelle d'accès | Fonction du produit |

**Le point décisif** : la vulnérabilité porte sur **l'interface d'administration**, qui n'est plus publiée. L'exposition directe depuis Internet a donc été fermée dix mois plus tôt.

⚠️ Cela ne clôt rien, pour deux raisons :
1. Il faut **vérifier depuis l'extérieur** que la règle `DENY` est effective — une règle écrite n'est pas une règle appliquée. Un test depuis une adresse externe prend cinq minutes.
2. Un attaquant ayant obtenu un accès au réseau interne par un autre chemin (§11.4) atteint toujours `8443`.

##### H+2 — la décision structurante

Le réflexe est de corriger. La bonne action est de **réduire encore l'exposition**, parce qu'elle prend quelques minutes et n'attend ni test ni fenêtre (§21.6).

| Option | Effet | Coût métier | Délai |
|---|---|---|---|
| Couper `443` — le service entier | Protection totale | **210 personnes sans accès distant**, un jeudi | 2 min |
| **Restreindre `443` aux plages des sites HELIOMED** | Forte : ne reste que le trafic depuis les sites | **7 personnes** en déplacement | 15 min |
| Restreindre `8443` aux seuls postes d'administration | Réduit le chemin interne | Nul | 15 min |
| Ne rien faire jusqu'au correctif | Aucune | Nul | — |

**Décision retenue : options 2 et 3 combinées.** Les 7 collaborateurs en déplacement sont prévenus individuellement et basculés sur un moyen alternatif — pour les 5 du salon, une connexion depuis le poste d'un partenaire est écartée (elle créerait un chemin non maîtrisé), au profit d'un report des tâches concernées.

**Pourquoi pas la coupure totale** : la vulnérabilité porte sur `8443`, pas sur `443`. Couper le service métier ne réduirait pas le risque lié à cette vulnérabilité — c'est une réaction disproportionnée qui coûterait la crédibilité du dispositif pour la prochaine crise.

🧪 **Journal D.11 — premières lignes**

| Heure | Information | Source | Statut | Décision | Décideur |
|---|---|---|---|---|---|
| 08:40 | Alerte CERT ALT-2027-0714 | CERT sectoriel | Piste | Vérifier à la source | C. Nadeau |
| 08:55 | Version `4.2.11` affectée, sur les deux membres | Avis constructeur | **Fait** | Ouvrir la cellule | C. Nadeau |
| 09:20 | `8443` non publié depuis 22/09/2026, confirmé par test externe | Test depuis IP externe | **Fait** | Ne pas couper `443` | C. Nadeau |
| 09:40 | 7 utilisateurs en déplacement identifiés | Annuaire + journaux | Fait | Restreindre `443` aux sites, prévenir individuellement | S. Weber |
| 10:05 | Restriction appliquée et vérifiée | Test externe | Fait | — | M. Ferhaoui |

---

#### A.4 Corrigé — la question que le dossier ne pose pas

**H+3.** Le greffier consigne une remarque de Malik Ferhaoui : *« depuis quand cette version est-elle installée ? »*

Les artefacts 2 et 4 donnent la réponse, et personne ne l'avait rapprochée :

```
2022-03-14  Mise en service, version 4.2.3
2022-03-14  Publication 8443/tcp — "temporaire, le temps de la période"
2026-09-22  Fermeture 8443/tcp
```

**L'interface d'administration a été publiée sur Internet du 14 mars 2022 au 22 septembre 2026 — quatre ans et six mois.** Et la vulnérabilité publiée aujourd'hui existe dans le code depuis la branche `4.2`, soit depuis la mise en service.

**Les trois questions du §21.3 s'imposent alors :**

| Question | Réponse | Source |
|---|---|---|
| Depuis combien de temps l'actif est-il exposé et vulnérable ? | **4 ans et 6 mois** | Artefact 4 |
| Quels journaux couvrent cette période ? | **30 jours**, sur l'équipement lui-même | Artefact 5 |
| Ces journaux permettraient-ils de détecter ce type d'exploitation ? | **Non** — et ceux du pare-feu ne portent pas le contenu applicatif | Artefact 5 |

##### Le niveau de qualification

Sur l'échelle du §21.2, la tentation est de retenir le **niveau 2** — exploitation active observée dans le monde, aucun indice chez nous. C'est faux.

La bonne réponse est le **niveau 5** : *journalisation insuffisante pour conclure*. Non parce qu'il y a des indices de compromission, mais parce qu'il est **impossible d'établir qu'il n'y en a pas** sur 98 % de la période d'exposition.

⚠️ **La distinction que ce cas enseigne** : le niveau 5 ne décrit pas la gravité de la menace, il décrit votre **degré de confiance dans votre propre évaluation**. Ce sont deux axes différents, et les confondre conduit à sous-réagir.

---

#### A.5 Corrigé — ce qu'on dit à la direction

L'exercice le plus difficile du cas. Quatre formulations, une seule correcte.

| Formulation | Évaluation |
|---|---|
| « Nous n'avons pas été compromis. » | **Faux.** Invérifiable, et très difficile à corriger si l'investigation dit l'inverse |
| « Nous avons probablement été compromis. » | **Excessif.** Aucun indice ne l'établit ; produit une panique injustifiée |
| « Nous enquêtons. » | **Insuffisant.** N'informe pas du problème réel et retarde une décision |
| « Nous ne pouvons pas établir que nous n'avons pas été compromis, parce que nos journaux ne couvrent que trente jours sur une exposition de quatre ans et demi. » | **Correcte** |

**Pourquoi chaque mot de la quatrième compte** :

- *« Nous ne pouvons pas établir »* — décrit une limite de connaissance, pas un fait sur le monde.
- *« que nous n'avons pas été compromis »* — la double négation est inconfortable et exacte ; la remplacer par « nous avons peut-être été compromis » déplace l'affirmation sur le terrain factuel.
- *« parce que nos journaux ne couvrent que trente jours »* — donne immédiatement la cause, donc l'action corrective.
- *« sur une exposition de quatre ans et demi »* — donne l'ordre de grandeur, qui rend la décision de porter la rétention à douze mois évidente.

**Note de situation — structure attendue**

```
1. Ce qui s'est passé      : vulnérabilité, exploitation active confirmée
2. Ce que nous avons fait  : restriction d'exposition à 10h05, correctif planifié cette nuit
3. Ce que nous savons      : 8443 non publié depuis septembre 2026
4. CE QUE NOUS NE SAVONS PAS : ce qui a pu se produire entre mars 2022 et septembre 2026
5. Ce que nous engageons   : investigation, reconstruction, rétention portée à 12 mois
6. Ce que nous demandons   : validation de l'interruption de service de cette nuit
```

⚠️ La section 4 est celle qu'on supprime sous pression. C'est celle qui a le plus de valeur.

---

#### A.6 Corrigé — le correctif d'urgence

##### Ce qu'on comprime, ce qu'on conserve

| Étape normale | En urgence | Justification |
|---|---|---|
| Délai d'observation (5 j) | **Supprimé** | Le calcul de risque s'inverse : exploitation active confirmée (§18.11) |
| Validation en recette | **Réduite** à un test fonctionnel sur le membre passif | Pas d'environnement de recette pour une appliance |
| Anneaux | **Conservés, compressés** : membre passif → observation 2 h → membre actif | La haute disponibilité fournit l'anneau naturel |
| **Critères d'arrêt** | **Conservés intégralement** | C'est ce qui rend la compression acceptable |
| **Plan de retour arrière** | **Conservé intégralement** | Double partition d'image (§2.7), testée |
| Demande de changement | **Émise a posteriori sous 48 h**, avec le journal | Traçabilité préservée |
| **Preuve** | **Conservée intégralement** | Relevé de version sur les deux membres |

🧪 **Critères go/no-go (D.6) — remplis avant l'intervention**

| Indicateur | Seuil d'arrêt | Mesuré par |
|---|---|---|
| Le membre passif redémarre en `4.2.19` | Tout échec | Console constructeur |
| Synchronisation du couple rétablie sous 10 min | `> 10 min` | Console |
| Sessions actives après bascule | `perte > 20 %` | Supervision |
| Authentifications abouties | `baisse > 10 % sur 15 min` | Journaux d'annuaire |
| Décideur du retour arrière | **M. Ferhaoui**, sans validation supplémentaire | — |

##### La séquence en haute disponibilité

```
1. Sauvegarde de configuration des deux membres, vérifiée
2. Mise à jour du membre PASSIF -> 4.2.19
3. Vérification : version, démarrage, synchronisation
4. Observation 2 h en état passif
5. Bascule du trafic vers le membre à jour
6. Observation 1 h — critères go/no-go
7. Mise à jour de l'ancien membre actif
8. Rebascule, ou maintien selon la configuration
```

⚠️ **Le piège du §2.7** : les deux membres fonctionnent en versions différentes pendant les étapes 2 à 7. Vérifier dans la documentation constructeur que cette configuration est supportée — **avant** l'intervention, pas pendant.

---

#### A.7 Corrigé — corriger ou reconstruire

##### La recherche de compromission préalable

Les cinq axes du §21.7, appliqués aux deux membres :

| Axe | Résultat |
|---|---|
| Comptes | **Deux comptes locaux non documentés** : `svc_mon` et `admin2`. Date de création non déterminable — l'équipement n'horodate pas la création de comptes locaux |
| Configuration | Écart de deux règles par rapport à la configuration de référence de 2025 ; les deux s'expliquent par des changements tracés |
| Persistance | Aucune tâche planifiée inconnue |
| Journaux d'accès | 30 jours : rien d'anormal |
| Trafic sortant | Analyse des journaux de pare-feu sur 12 mois : aucune destination inhabituelle **détectée** — la granularité ne permet pas d'exclure un canal discret |

##### La décision

| Critère | Évaluation |
|---|---|
| Exposition prolongée avérée | **Oui — 4,5 ans** |
| Journalisation permettant de conclure | **Non** |
| Anomalies non explicables | **Oui — 2 comptes locaux** |
| État de confiance démontrable autrement | **Non** |

→ **Reconstruction**, pas correction.

**Pourquoi.** Le correctif ferme la porte ; il ne fait pas sortir celui qui serait entré avant. Sur un équipement de bordure, la persistance est fréquente et difficile à détecter — comptes créés, configuration modifiée, dans certains cas implant au niveau du micrologiciel (§27.2). Les deux comptes non documentés suffisent à basculer la décision, **même sans preuve de malveillance** : c'est le principe du §34.8, on reconstruit quand l'état de confiance ne peut pas être démontré.

**Ordre des opérations** :
1. **Préserver** : export de la configuration, des journaux disponibles, image de l'équipement si le constructeur le permet.
2. Reconstruire à partir de la **configuration de référence**, pas de la configuration courante.
3. Appliquer `4.2.19` sur l'équipement reconstruit.
4. **Rotation de tous les secrets** ayant transité : comptes de service, certificats, secrets d'authentification.
5. Rétablir la surveillance avant remise en service.

⚠️ **Le conflit à arbitrer consciemment** : préserver les preuves ralentit la remise en service. La décision appartient au pilote de cellule, elle est tracée, et elle n'est pas subie par réflexe.

##### Jours 3 à 30

Recherche des mêmes indicateurs sur les actifs joignables depuis la passerelle · rotation complète des secrets · revue des accès distants · surveillance renforcée 90 jours.

**Résultat** : aucune activité malveillante établie. Ce qui **ne prouve rien** sur la période non journalisée — et cette phrase figure telle quelle dans le retour d'expérience.

---

#### A.8 Corrigé — les quatre erreurs volontairement insérées

| # | Erreur | Où | Ce qu'elle produit |
|---|---|---|---|
| 1 | **Journalisation stockée sur l'équipement lui-même, sans export** | Artefact 5 | Un attaquant ayant compromis l'équipement efface les traces. Même sur 30 jours, la preuve n'est pas fiable |
| 2 | **Ouverture « temporaire » sans date de fin** | Artefact 4, ligne 2022-03-14 | 4,5 ans d'exposition. C'est le §11.9 : toute ouverture temporaire porte une date de fermeture dans la demande de changement |
| 3 | **Fermeture de 2026 sans requalification rétrospective** | Artefact 4, ligne 2026-09-22 | L'exposition a été fermée sans que la question « qu'a-t-il pu se passer pendant ces 4 ans ? » ne soit posée. Elle se pose aujourd'hui, dans l'urgence |
| 4 | **Aucune configuration de référence exploitable** | Implicite — la reconstruction s'appuie sur une configuration de 2025 partiellement obsolète | La reconstruction prend 6 h au lieu de 2 h |

**Une cinquième faiblesse, non fautive mais coûteuse** : l'appliance n'est couverte par aucun outil de scan (artefact 2). Le suivi de version repose entièrement sur un relevé manuel. C'est normal pour ce type d'équipement (§27.4), et cela impose un contrôle périodique explicite plutôt qu'une confiance dans l'outillage.

---

#### A.9 Livrables et décisions structurelles

| Livrable | Contenu |
|---|---|
| Journal de crise D.11 | Horodaté, avec sources et décideurs, encadré « état de la connaissance » rempli |
| Demande de changement urgent D.5 | Émise à J+2, avec D.6 et D.7 joints |
| Note à la direction | Six sections, dont « ce que nous ne savons pas » |
| Déclaration à l'assureur | Conservatoire, sous 72 h |
| Retour d'expérience | Les cinq questions du §21.10 |

**Les cinq décisions structurelles issues du retour d'expérience** :

1. **Journalisation** portée à 12 mois sur les actifs de bordure et de niveau 0, **exportée hors de l'équipement**.
2. **Doctrine de version** écrite et datée pour les équipements de bordure, revue trimestriellement (§2.7).
3. **Reconstruction plutôt que correction** après exploitation potentielle sur un équipement de bordure, avec configuration de référence maintenue et testée.
4. **Pré-arbitrage complété** : le seuil d'urgence distingue désormais *restreindre* et *couper*, avec un décideur pour chacun.
5. **Toute ouverture temporaire porte une date de fermeture** dans la demande de changement, avec contrôle automatique à cette date.

---

#### A.10 Critères d'évaluation

| Critère | Pts | Attendu |
|---|---|---|
| Qualification à la source, et des **deux** membres | 10 | Ne pas agir sur l'alerte relayée |
| Distinction `443` / `8443` dans l'analyse d'exposition | 15 | La vulnérabilité porte sur l'administration, pas sur le service |
| Réduction d'exposition **avant** correction | 15 | Restreindre plutôt que couper, avec justification |
| **Question sur la durée d'exposition** | 20 | Le cœur du cas : rapprocher les artefacts 2 et 4 |
| Qualification en niveau 5 | 10 | Confiance dans l'évaluation, pas gravité de la menace |
| Formulation à la direction | 15 | Les quatre nuances du §A.5 |
| Décision de reconstruire, avec critère explicite | 10 | Et préservation des preuves avant action |
| Identification d'au moins 3 des 4 erreurs | 5 | — |

**Seuil de réussite** : 70/100. **Élimination** : annoncer à la direction l'absence de compromission.

---

#### A.11 Variantes

##### Variante 1 — aucun correctif disponible

L'avis constructeur annonce un correctif « sous 10 jours ». Ce qui change :

| Élément | Traitement |
|---|---|
| Réduction d'exposition | **Identique**, et devient la mesure principale |
| Contournement officiel | Appliquer, et **vérifier** qu'il est effectif |
| Compensation | Les sept attributs du §20.7, avec date d'expiration = date du correctif attendu |
| Surveillance | Renforcée sur `8443`, avec destinataire nommé |
| Relance constructeur | Écrite, hebdomadaire, tracée |
| Direction | Informée que l'exposition résiduelle est portée pendant 10 jours, avec compensation |

**Le piège** : traiter les 10 jours comme une attente passive. Ils doivent être un **régime de compensation formalisé**, révocable si l'exploitation s'intensifie.

##### Variante 2 — organisation de 40 personnes, sans SOC ni astreinte

| Ce qui reste faisable | Ce qui ne l'est pas |
|---|---|
| Restreindre l'exposition — 15 min | La recherche de compromission approfondie |
| Vérifier la version à la source | L'analyse des journaux de pare-feu sur 12 mois |
| Appliquer le correctif dans la journée | La surveillance renforcée sur 90 jours |
| **Poser les trois questions du §21.3** | La reconstruction sans configuration de référence |
| **Documenter honnêtement l'incertitude** | — |

**Les deux investissements préalables qui changent réellement l'issue**, et qui sont accessibles à une petite structure :

1. Une **configuration de référence exportée et testée** — trente minutes par an, et elle transforme une reconstruction impossible en opération de deux heures.
2. Un **export des journaux hors de l'équipement**, même vers un simple espace de stockage — quelques euros par mois, et il rend la question du §21.3 traitable.

**Ce que le cas enseigne aux petites structures** : les deux actions les plus rentables — restreindre l'exposition, et écrire ce qu'on ne peut pas savoir — ne coûtent presque rien et ne dépendent d'aucun outil.

---

### Cas de synthèse B — Sortie d'obsolescence sous contrainte et préparation d'un contrôle

> **Format** — Cas de pilotage, à traiter avec un tableur ouvert. Durée estimée : **3 heures**.
> **Livrables attendus** : trois options chiffrées (D.8) · plan de lots · fiche de sanctuarisation (D.4) · note d'arbitrage au comité de direction · préparation d'entretien de contrôle.
> **Prérequis** : chapitres 7, 8, 12, 13, 32, 39.

---

#### B.1 Le dossier initial

**Nous sommes le lundi 5 octobre 2026.** Vous préparez le comité stratégique du 15 octobre.

##### Artefact 1 — état du parc concerné

| Population | Nb | Système | Statut | Contexte |
|---|---|---|---|---|
| Postes bureautiques siège | 340 | Windows 10 22H2 | Hors support depuis le 14/10/2025 | Joints au domaine, gérés par l'infogérant |
| Postes R&D Nantes | 90 | Windows 10 22H2 | Idem | Idem |
| Postes commerciaux nomades | 40 | Windows 10 22H2 | Idem | Idem |
| Postes site industriel (bureautique) | 19 | Windows 10 22H2 | Idem | Idem |
| Postes de supervision industrielle | 11 | Windows 10 IoT LTSB 2016 | **Fin de support le 13/10/2026** | Classe C4, validation constructeur |
| Banc de test PX-40 | 1 | Windows 10 Entreprise LTSB 2016 | **Fin de support le 13/10/2026** | Validation réglementaire des pompes |
| Serveurs | 11 | Windows Server 2016 | **Fin de support le 12/01/2027** | Dont 3 portant des applications métier |

**Total postes hors support : 620** (340 + 90 + 40 + 19 + 11 + 1 arrondi au périmètre géré) · **11 serveurs**.

##### Artefact 2 — courriel de l'infogérant, 12 juin 2026

> *« Concernant votre question sur Windows 10 : l'éditeur a annoncé la prolongation du programme de mises à jour de sécurité étendues jusqu'en octobre 2027. Votre parc est donc couvert et il n'y a pas d'urgence à planifier une migration cette année. Nous restons à votre disposition. »*

##### Artefact 3 — extrait des conditions d'éligibilité du programme grand public

> Le programme de mises à jour de sécurité étendues destiné aux **appareils personnels** est disponible pour les appareils exécutant Windows 10 version 22H2. **Les appareils joints à un domaine Active Directory ou à Microsoft Entra, ainsi que les appareils gérés par une solution de gestion des appareils mobiles, ne sont pas éligibles à ce programme.** Les organisations doivent souscrire au programme commercial.

##### Artefact 4 — compatibilité applicative

| Application | Postes concernés | Validée sur Windows 11 | Remarque |
|---|---|---|---|
| Suite bureautique | 620 | Oui | — |
| Gestion commerciale | 480 | Oui, depuis v9.2 | Migration applicative requise : v9.0 installée |
| Outil de paie | 22 | **Non** | Éditeur : « validation prévue T2 2027 » |
| Chaîne de développement | 90 | Oui | — |
| Suivi de production (lecture) | 19 | Oui | — |
| Conduite de ligne | 11 | **Non — et jamais** | Constructeur : produit en fin de vie |
| Logiciel de banc de test | 1 | **Non** | **Éditeur disparu en 2019** |

##### Artefact 5 — contraintes financières et matérielles

- Budget d'investissement 2026 : **engagé à 94 %**. Reste disponible : 38 k€.
- Vote du budget 2027 : **mars 2027**.
- Parc matériel : 210 postes de plus de 5 ans, **incompatibles** avec le nouveau système sans remplacement.
- Coût unitaire de remplacement d'un poste : ordre de grandeur `[à renseigner selon votre contexte]`.
- Coût du support étendu commercial : facturation **par poste et par an**, avec un tarif **croissant chaque année** — le principe est stable, les montants doivent être obtenus par devis.

##### Artefact 6 — contexte de contrôle

- Un client hospitalier majeur annonce un **audit de sécurité fournisseur au premier trimestre 2027**, portant sur la chaîne HelioLink.
- La police d'assurance est en renouvellement en février 2027.
- Le référentiel applicable comporte un objectif explicite sur la maîtrise de l'obsolescence.

---

#### B.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | L'affirmation de l'infogérant est-elle exacte ? Comment le vérifiez-vous ? | — |
| 2 | Construisez les trois options chiffrées. | D.8 |
| 3 | Proposez un plan de lots avec dépendances. | Tableau de lots |
| 4 | Traitez les 11 postes de supervision et le banc de test. | D.4 |
| 5 | Rédigez la note d'arbitrage au comité de direction. | Note 1 page |
| 6 | Préparez l'entretien de contrôle : six questions et vos réponses. | Grille |
| 7 | Que faites-vous du courriel du 12 juin ? | — |

---

#### B.3 Corrigé — la vérification qui renverse la situation

**L'affirmation de l'infogérant est inexacte**, et la vérification prend quinze minutes : lire les conditions d'éligibilité du programme invoqué (artefact 3).

| Programme | Public | Éligibilité du parc HELIOMED |
|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | **Non éligible** — parc joint au domaine et géré |
| Support étendu **commercial** | Organisations | Éligible, **payant**, tarif croissant |

**Conséquence** : les 620 postes n'ont **jamais** été couverts et ne reçoivent plus de correctifs de sécurité depuis le **14 octobre 2025**, soit près de **douze mois** au moment du constat.

⚠️ **La leçon du §12.1, piège n° 1** : une option de support ne se budgète jamais avant d'avoir vérifié, **actif par actif**, son périmètre d'éligibilité. Ici, la vérification n'avait pas été faite parce que l'information venait d'un tiers de confiance — ce qui ne dispense de rien.

**Ce que la découverte change** : le sujet cesse d'être un arbitrage de calendrier pour devenir un sujet de **responsabilité contractuelle** et de **documentation d'un écart de douze mois**.

---

#### B.4 Corrigé — les trois options chiffrées

> Les montants ci-dessous sont exprimés en **structure de coût**, non en valeurs absolues : les tarifs de support étendu et de matériel se négocient et se périment. La méthode est ce qui compte.

##### Fiche D.8 remplie

| Champ | Contenu |
|---|---|
| Population | 620 postes + 11 serveurs |
| Composant | Système d'exploitation |
| Date de fin de support | 14/10/2025 (postes) · 13/10/2026 (LTSB) · 12/01/2027 (serveurs) |
| Source et vérification | Pages officielles de cycle de vie, consultées le 05/10/2026 |
| Criticité / exposition | C2-C3 pour les postes · C1 pour 3 serveurs |
| **Éligibilité au support étendu** | ☑ **Vérifiée actif par actif** — programme grand public **non applicable** |

##### Comparaison des options

| | **Option 1 — support étendu 2 ans** | **Option 2 — migration en 3 lots** | **Option 3 — statu quo** |
|---|---|---|---|
| **Coûts directs** | 620 postes × tarif an 1 + 620 × tarif an 2 (**croissant**) | 210 postes à remplacer + migration applicative gestion commerciale + charge projet | 0 |
| **Coûts indirects** | Coût de la migration, **qui reste dû** après les 2 ans | Tests, formation, support renforcé pendant 9 mois | Compensations · surveillance · urgences · astreinte |
| **Couverture** | Correctifs **critiques uniquement**, selon les critères de l'éditeur | Complète et durable | **Nulle** |
| **Risque résiduel** | Vulnérabilités non critiques non corrigées | Élevé pendant la transition, nul ensuite | 620 postes sans correctif |
| **Position en contrôle** | Défendable si daté et borné | Excellente | **Intenable** |
| **Position en assurance** | Acceptable avec plan | Excellente | Risque de refus de garantie |
| **Faisabilité** | Immédiate | 9 mois | Immédiate |

⚠️ **L'option 3 doit figurer au tableau, chiffrée.** Son absence est la première cause de non-décision (§12.6). Ici, elle est **techniquement disponible mais contractuellement indisponible** : l'audit client de T1 2027 et le renouvellement d'assurance de février la rendent inacceptable. Ce point s'écrit, il ne se sous-entend pas.

##### Décision recommandée

**Option 2, avec un pont ciblé** :

- Migration en trois lots sur neuf mois.
- Support étendu commercial limité à **140 postes** — ceux portant l'outil de paie (22) et une partie de la gestion commerciale en attente de validation (118).
- Le pont est **daté, borné et chiffré** : il se termine au T4 2027, à la migration du lot 3.

**Ce qui rend cette option supérieure** : sur deux ans, l'option 1 représente une fraction significative du coût de la migration **sans produire aucun bénéfice durable** — et la migration reste à financer ensuite. L'arbitrage se fait en quinze minutes une fois le tableau posé.

---

#### B.5 Corrigé — le plan de lots

| Lot | Périmètre | Nb | Échéance | Prérequis | Dépendances |
|---|---|---|---|---|---|
| **0 — Pilote** | 15 postes, 4 profils représentés | 15 | Nov. 2026 | Aucun | Valide le processus et produit le chiffrage réel |
| **1** | Postes bureautiques standards, matériel compatible | 200 | T1 2027 | Lot 0 concluant | Aucune |
| **2** | Postes avec gestion commerciale, matériel compatible | 265 | T2 2027 | **Migration applicative v9.0 → v9.2** | Bloquant : à lancer **immédiatement** |
| **3** | Postes à remplacer + paie | 140 | T4 2027 | Budget 2027 voté · **validation éditeur paie (T2 2027)** | Sous pont de support étendu |
| **Hors lots** | 11 supervision + 1 banc de test | 12 | — | — | Voir §B.6 |

##### Le séquencement, et pourquoi il ne suit pas les dates

La date de fin de support est **identique** pour les 620 postes. Le critère du §12.3 s'applique : **criticité × exposition × effort**.

- Le **lot 0** part en premier pour produire un chiffrage réel — c'est le levier n° 4 du §12.7 contre le report perpétuel : l'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée en interne.
- Le **lot 1** regroupe le plus simple : matériel compatible, aucune dépendance applicative. Il fait chuter le volume rapidement.
- Le **lot 2** est conditionné par une migration applicative de neuf semaines. **Elle doit être lancée dès octobre 2026** — le §26.10 rappelle que la négociation avec un éditeur métier doit démarrer six mois avant l'échéance.
- Le **lot 3** dépend d'un budget non voté et d'une validation éditeur non acquise : c'est lui qui porte le pont.

⚠️ **L'erreur de séquencement à éviter** : commencer par les cas difficiles « parce qu'ils sont les plus risqués ». Le lot 3 en premier bloquerait le programme sur une dépendance externe pendant six mois, sans qu'aucun poste ne soit migré.

---

#### B.6 Corrigé — les deux systèmes contraints

##### Cas 1 — les 11 postes de supervision

| Élément | Décision |
|---|---|
| Décision structurante (§32.1) | **Remplacer** — mais à l'échelle du système de conduite, pas du poste |
| Contrainte | Le constructeur a placé le produit en fin de vie ; aucune version compatible n'existera |
| Horizon | Renouvellement du système de conduite : projet industriel pluriannuel, hors périmètre DSI |
| **Traitement intérimaire** | **Isoler** : régime C4, réseau industriel séparé, compensation selon §20.2, fenêtre lors des arrêts de production |
| Dérogation | Signée par le directeur industriel, revue semestrielle |
| Provision | Inscrite au plan pluriannuel industriel |

##### Cas 2 — le banc de test PX-40 (fiche D.4)

| Champ | Contenu |
|---|---|
| Objet | `BANC-PX40-01` · système hors support au 13/10/2026 · logiciel de pilotage sans version récente |
| Type d'impossibilité | ☑ **Technique** — éditeur disparu en 2019, aucun correctif ne viendra jamais |
| Analyse de risque en termes métier | Le banc valide la conformité réglementaire des pompes PX-40. Sa compromission pourrait altérer des résultats de validation, avec des conséquences sur la conformité des dispositifs mis sur le marché et sur la sécurité des patients. Le poste ne contient pas de données à caractère personnel. |
| Exposition avant compensation | Réseau industriel, joignable depuis 11 postes de supervision |
| **Décision structurante** | **ISOLER** — remplacer le banc complet représente ~300 k€ et 18 mois, requalification comprise |
| Compensations | **1.** Retrait de tout réseau (rang 1, §20.2). **2.** Transferts par support dédié, chaîne du §29.5. **3.** Deux comptes nominatifs, journal papier des interventions. **4.** Contrôle trimestriel de l'absence de connexion. |
| Moyen de vérification | Contrôle physique trimestriel : absence de câble, absence d'interface sans fil active, relevé du journal papier |
| Coût de la solution | ~14 k€ — matériel réseau et deux jours d'ingénierie |
| Signataire | **Directeur général** — la grille C.4 impose ce niveau : impact potentiel sur la conformité de dispositifs médicaux |
| Date d'expiration | 31/12/2028, alignée sur la revue du plan pluriannuel |
| Conditions de révocation anticipée | Panne matérielle du poste · évolution de l'exigence réglementaire de validation · disponibilité d'une solution de remplacement qualifiée |
| Provision | Remplacement du banc inscrit au plan pluriannuel, horizon 2031 |

**Le point à retenir** : deux systèmes également non corrigeables, deux décisions différentes. Ce qui les distingue n'est pas technique — c'est le **rapport entre le coût du remplacement et la valeur de l'usage**, et la disponibilité d'une trajectoire.

---

#### B.7 Corrigé — la note d'arbitrage au comité de direction

> **Note — Sortie d'obsolescence du parc bureautique — 8 octobre 2026 — 1 page**
>
> **1. Situation.** 620 postes de travail ne reçoivent plus de correctifs de sécurité depuis le 14 octobre 2025. Le programme de prolongation évoqué en juin ne s'applique pas aux parcs professionnels gérés : la vérification des conditions d'éligibilité, réalisée le 5 octobre, l'établit sans ambiguïté. L'écart porte donc sur douze mois.
>
> **2. Ce que cela signifie.** Toute vulnérabilité publiée depuis un an sur ce système reste non corrigée sur l'ensemble du parc bureautique. Deux échéances externes rendent cette situation intenable : un audit de sécurité d'un client hospitalier au premier trimestre 2027, et le renouvellement de la police d'assurance en février.
>
> **3. Trois options.** *(tableau du §B.4)*
>
> **4. Recommandation.** Migration en trois lots sur neuf mois, avec un pont de support étendu commercial limité à 140 postes, daté et borné au quatrième trimestre 2027. Sur deux ans, l'option de support étendu seule représente une part significative du coût de la migration sans en produire aucun bénéfice durable, et la migration resterait à financer.
>
> **5. Ce que nous demandons.** L'inscription au budget 2027 du remplacement de 210 postes et du pont de support étendu · le lancement immédiat de la migration applicative de la gestion commerciale, prérequis bloquant du lot 2 · la signature de la dérogation relative au banc de test de validation.
>
> **6. Ce qui reste non résolu.** La validation de l'outil de paie par son éditeur est annoncée pour le deuxième trimestre 2027 sans engagement contractuel. En cas de retard, 22 postes resteront sous pont au-delà du quatrième trimestre 2027. Ce risque est identifié, il n'est pas maîtrisé par nous.

⚠️ **La section 6 est celle qui fait la différence.** Une note qui ne présente que des problèmes résolus n'est pas crédible. Celle-ci nomme ce qui échappe à l'organisation, et elle le nomme **avant** que cela ne se produise.

---

#### B.8 Corrigé — l'entretien de contrôle

| Question du contrôleur | Réponse attendue | Pièce du dossier |
|---|---|---|
| « Combien d'actifs sont hors support ? » | Le chiffre, **avec son dénominateur** et la répartition par population : 620 postes sur 941 actifs du périmètre, 11 serveurs sur 187 | Périmètre daté (D.13, pièce 1) |
| « Depuis quand ? » | 14/10/2025 pour les postes. **Et la cause** : une information d'éligibilité inexacte reçue d'un tiers, non vérifiée à la source jusqu'au 05/10/2026 | Note interne datée |
| « Qu'avez-vous décidé ? » | Les trois options chiffrées, l'option retenue, le décideur, la date de décision | D.8 + note d'arbitrage |
| « Qu'est-ce qui n'est pas couvert ? » | L'annexe des périmètres non couverts, tenue depuis 2026 : banc de test, postes de supervision, avec compensations et échéances | Annexe de D.1 |
| « Comment le prouvez-vous ? » | Périmètre daté, journaux de campagne par lot, échantillon de preuve d'état sur chaque lot | D.13, pièces 1, 5, 6 |
| « Et si le lot 3 glisse ? » | Le risque est identifié dans la note du 08/10/2026, section 6. Le pont de support étendu est prolongeable, avec son coût connu | Note d'arbitrage |

##### Ce qui fait la différence dans cet entretien

L'organisation **ne prétend pas être conforme**. Elle démontre trois choses :

1. Elle **connaît** ses écarts, et les chiffre avec leur dénominateur.
2. Elle les a **décidés au bon niveau**, avec une trace datée.
3. Elle en **suit** l'évolution, avec des échéances et un financement.

C'est exactement le §39.1. Un dossier qui prétendrait à 100 % de conformité sur ce parc serait immédiatement suspect.

##### Barème d'évaluation de l'entretien

| Critère | Pts |
|---|---|
| Chiffres donnés avec dénominateur et population | 20 |
| Cause de l'écart assumée, sans dissimulation ni mise en cause | 15 |
| Trois options présentées, dont le statu quo | 20 |
| Périmètres non couverts présentés spontanément | 20 |
| Preuves produites, datées, avec périmètre | 15 |
| Risque non maîtrisé nommé avant d'être découvert | 10 |

**Élimination** : présenter le taux de conformité de la console de l'infogérant sans mentionner les 620 postes.

---

#### B.9 Corrigé — le courriel du 12 juin

Trois usages, dans cet ordre.

1. **Contractuel.** L'information transmise était inexacte et a fondé une décision de report. Le sujet n'est plus « qui devait patcher » — le contrat ne comportait aucun engagement de délai — mais « quelle information avons-nous reçue ». C'est ce déplacement qui rend la renégociation possible (§13.9).
2. **Documentaire.** Le courriel devient une pièce du dossier de preuves : il établit la cause de l'écart de douze mois, ce qui est très différent d'une négligence non expliquée (§39.1).
3. **Préventif.** Il justifie l'ajout au contrat d'une clause de restitution de données et d'une clause d'escalade des impossibilités (D.9, clauses 3 et 8). Sans donnée restituée, l'organisation ne pouvait pas détecter elle-même que le parc n'était pas couvert.

⚠️ **Ce qu'il ne faut pas en faire** : un instrument de mise en cause personnelle. L'objectif est d'obtenir des clauses, pas d'avoir raison.

---

#### B.10 Bilan à douze mois et ce qui n'a pas fonctionné

| Indicateur | Oct. 2026 | Oct. 2027 |
|---|---|---|
| Postes hors support | 620 | **140** (sous pont daté) |
| Serveurs hors support | 11 | **2** |
| Ratio confirmé conforme, parc bureautique | 34 % | **89 %** |
| Contrôle client T1 2027 | — | Passé, deux observations mineures |
| Surprime d'assurance | 34 % | Renégociée |

**Ce qui n'a pas fonctionné**, et qui doit figurer au retour d'expérience :

1. **Le lot 2 a glissé de six semaines.** La migration applicative de la gestion commerciale a démarré en novembre au lieu d'octobre : la commande a attendu une validation d'achat non anticipée. Le §26.10 aurait dû être appliqué six mois plus tôt.
2. **Deux postes du lot 1 ont dû être repris.** Du matériel incompatible n'avait pas été détecté à l'inventaire — les caractéristiques matérielles ne figuraient pas dans les attributs suivis (Annexe I.1).
3. **Le pont a coûté plus que prévu.** Le tarif de la deuxième année n'avait pas été intégré au chiffrage initial, alors que le §12.1 le signale explicitement.

---

### Cas de synthèse C — Le correctif urgent qui casse la production

> **Format** — Cas d'arbitrage, à traiter en deux temps : la décision *avant*, puis l'analyse *après*. Durée estimée : **2 h 30**.
> **Livrables attendus** : instruction des deux risques · demande de changement (D.5) · critères go/no-go (D.6) · plan de retour arrière (D.7) · chronologie · compte rendu d'incident · plan d'amélioration.
> **Prérequis** : chapitres 6, 16, 18, 20, 26.

---

#### C.1 Le dossier initial

**Nous sommes le vendredi 12 novembre 2027, 14 h 00.**

##### Artefact 1 — l'avis reçu

> **Avis de sécurité éditeur — moteur de base de données — 12/11/2027 08:00 UTC**
>
> Une vulnérabilité affectant le traitement des connexions authentifiées permet à un utilisateur disposant de droits limités d'exécuter du code avec les privilèges du service.
> Gravité : **élevée**. Exploitation observée : **aucune à ce jour**.
> Versions affectées : `15.x` antérieures à `15.4.2`.
> Correctif : `15.4.2`, publié le 12/11/2027 à 06:00 UTC.
>
> *Notes de version — extrait, page 4, section « Modifications internes » :*
> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. Une mise à jour simultanée de tous les membres d'un groupe de réplication est requise. »*

##### Artefact 2 — le cluster concerné

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

##### Artefact 3 — l'environnement de recette

```yaml
id_actif: REC-HELIOLINK-BDD
version: "15.3.1"
topologie: 1 nœud unique — PAS de réplication
volumetrie: 2 % de la production
integrations: 3 sur 7 simulées
configuration: dérive non mesurée depuis 2026
derniere_synchronisation_donnees: 2027-04-15
```

##### Artefact 4 — la politique applicable

| Classe | Délai — critique non exploitée |
|---|---|
| **C1** | **15 jours** |

##### Artefact 5 — la proposition de l'équipe

> *Courriel de M. Ferhaoui, 12/11/2027 14 h 12 :*
> « Vulnérabilité élevée sur le cluster HelioLink, correctif dispo. Je propose de l'appliquer demain soir dans la fenêtre habituelle, pour ne pas laisser traîner. C'est une version mineure, ça devrait bien se passer. »

##### Artefact 6 — antécédents

- Le correctif a été publié il y a **6 heures**. Aucun retour communautaire n'est encore disponible.
- Le dernier retour arrière testé sur ce cluster date de **mars 2026**, sur un nœud isolé.
- La plateforme HelioLink dispose de deux indicateurs fonctionnels : *remontées de télésuivi abouties par minute* et *sessions établissement actives*.

---

#### C.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | Instruisez les deux risques **en parallèle**. | Tableau à deux colonnes |
| 2 | Quelle décision prenez-vous le vendredi 12 à 17 h ? | Décision tracée |
| 3 | Le scénario applique le correctif le samedi. Reconstituez ce qui se passe. | Chronologie |
| 4 | Identifiez les causes racines, et ce qui a bien fonctionné. | Compte rendu |
| 5 | Rédigez le plan d'amélioration. | Plan daté |
| 6 | Distinguez erreur humaine, erreur de conception, erreur de processus. | Analyse |

---

#### C.3 Corrigé — instruire les deux risques en parallèle

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

##### La lecture

Le déséquilibre est net. La colonne de gauche ne présente **aucune urgence caractérisée** : pas d'exploitation, pas d'exposition directe, privilèges préalables requis. La colonne de droite présente **quatre inconnues et une lacune avérée** — la recette ne représente pas la production sur la dimension exacte que le correctif touche.

**La décision correcte est d'utiliser le délai disponible.**

⚠️ **Le biais à nommer explicitement.** L'artefact 5 dit *« pour ne pas laisser traîner »*. C'est une préférence psychologique, pas une analyse de risque. Elle est l'erreur symétrique du report perpétuel du §12.7 — et elle est bien moins souvent dénoncée, parce qu'elle a l'apparence de la diligence.

**La formulation à retenir** : *un délai accordé par la politique est une ressource, pas un retard. Il existe précisément pour permettre de tester. L'utiliser n'est pas de la négligence.*

##### Ce qui aurait renversé la décision

Il est important de savoir ce qui aurait justifié d'agir samedi :

| Élément | Effet |
|---|---|
| Exploitation observée dans le monde | Bascule vers la feuille « traiter » à 7 jours |
| Exploitation observée dans le secteur santé | Bascule vers l'urgence |
| Cluster directement exposé | Bascule vers l'urgence |
| Recette représentative disponible | Le risque de changement chute — samedi devient raisonnable |

---

#### C.4 Corrigé — la lecture des notes de version

L'information décisive est à la **page 4, section « Modifications internes »** de l'artefact 1 :

> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. »*

**Ce que cela signifie concrètement** : la mise à jour nœud par nœud — la méthode standard sur un cluster — **est impossible** sur ce correctif. Elle produit un cluster dont les membres ne peuvent plus se synchroniser.

C'est exactement la question n° 2 de la qualification en six questions du §18.2 : *quels prérequis exige-t-il ?* La réponse était disponible dès 8 h du matin, dans un document de quatre pages.

⚠️ **Pourquoi cette ligne se rate.** Elle ne figure ni dans le résumé, ni dans la section sécurité, ni dans les correctifs listés : elle est dans une rubrique « modifications internes » que rien ne signale comme critique. C'est le cas général — **la qualification consiste à lire les notes de version en entier, pas à les parcourir**.

---

#### C.5 Corrigé — la chronologie du samedi

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

##### Ce qui aurait pu être pire

Le scénario s'arrête au réplica. Si la séquence avait commencé par le **primaire**, l'indisponibilité aurait été **totale**, et le retour arrière aurait exigé une restauration de sauvegarde avec perte des transactions depuis l'instantané — c'est-à-dire des données de télésuivi de 34 établissements.

**Le choix de commencer par un réplica est la seule décision de la nuit qui relève de la bonne pratique.** Elle mérite d'être nommée dans le retour d'expérience.

---

#### C.6 Corrigé — causes racines et ce qui a fonctionné

##### Les quatre causes racines

| # | Cause | Ce qui l'aurait évitée | Coût de la prévention |
|---|---|---|---|
| 1 | **Notes de version parcourues, pas lues** | Qualification en six questions du §18.2, avec référence de la section consultée | 20 minutes |
| 2 | **Recette non représentative sur la dimension touchée** | Mesure de l'écart sur les quatre axes du §6.12, **déclarée dans la demande de changement** | 1 h, puis constat bloquant |
| 3 | **Retour arrière testé sur une topologie non représentative** | Test sur cluster, chronométré (§18.8) | 1/2 journée, une fois |
| 4 | **Aucun critère d'arrêt écrit, aucun décideur nommé** | Formulaire D.6 rempli avant l'intervention | 15 minutes |

**La cause 2 est la cause dominante.** Les causes 1, 3 et 4 aggravent, mais c'est l'écart de recette qui rend l'incident inévitable : aucun test sur un nœud unique ne pouvait révéler un problème de réplication.

##### Ce qui a bien fonctionné — à nommer explicitement

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

#### C.7 Corrigé — ce qu'il aurait fallu faire

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

##### Les livrables remplis

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

#### C.8 Corrigé — erreur humaine, de conception, de processus

C'est la question la plus importante du cas, et la plus mal traitée en pratique.

| Type | Ce qui s'est passé | Le bon niveau de traitement |
|---|---|---|
| **Erreur humaine** | Malik Ferhaoui n'a pas lu la page 4 des notes de version | Aucune sanction n'est appropriée : il a suivi une procédure qui ne l'exigeait pas |
| **Erreur de conception** | L'environnement de recette ne reproduit pas la topologie de production | Décision d'investissement — c'est le §6.12 et le §6.13 |
| **Erreur de processus** | La qualification n'était pas un champ obligatoire · les critères d'arrêt n'étaient pas exigés · le retour arrière n'avait pas à être testé sur topologie représentative | **C'est ici que se corrige l'incident** |

##### Le principe à retenir

> Un retour d'expérience porte sur le **processus**, jamais sur les personnes. Quand une personne compétente, appliquant la procédure existante, produit un incident, le défaut est dans la procédure.

**Le test qui tranche** : *une autre personne, à la place de Malik, aurait-elle fait autrement ?* Ici, non — rien dans le processus ne l'y obligeait. Le défaut est donc structurel.

⚠️ **Le contre-exemple**, pour ne pas tomber dans l'excès inverse : si la procédure avait exigé la qualification en six questions et qu'elle avait été délibérément contournée pour gagner du temps, ce serait une erreur d'application — qui appelle un traitement différent, mais toujours pas une sanction en première intention : la question devient *pourquoi la procédure a-t-elle paru contournable ?*

---

#### C.9 Le plan d'amélioration

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

#### C.10 Critères d'évaluation

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

#### C.11 Variante — la même situation avec exploitation active

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


## ANNEXES

### Plan d'accès — trouver la bonne annexe en dix secondes

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme ou un acronyme | **A** — glossaire |
| Savoir quoi vérifier sur une plateforme donnée | **B** — cheat sheets |
| Prioriser un constat, ou fixer un délai | **C** — matrices et arbre de décision |
| Un formulaire à remplir : politique, dérogation, changement, PV | **D** — 14 templates |
| Choisir une famille d'outil, ou comprendre un modèle de licence | **E** — outils *(versionnée)* |
| Savoir ce qu'un texte exige et quelle preuve il attend | **F** — réglementaire *(versionnée)* |
| Vérifier si je suis en train de tomber dans un piège connu | **G** — 53 pièges classés |
| Retrouver une échéance, une source de veille, une formation | **H** — calendrier et ressources *(versionnée)* |
| Concevoir ou corriger un inventaire | **I** — modèle de données |
| Définir un cycle de vie de constat, des états, des escalades | **J** — workflow de remédiation |
| Définir un indicateur, ou m'auto-évaluer | **K** — KPI et maturité |
| Une liste à cocher avant une action | **L** — 9 checklists |
| Vérifier d'où vient une affirmation datée du cours | **M** — registre de sources *(versionnée)* |

**Cours ou documentation ?** Les annexes A, C, G et K servent à **apprendre** et se lisent. Les annexes B, D, I, J et L servent à **consulter** et se remplissent. Les annexes E, F, H et M servent à **vérifier** et se périment — ce sont elles qui portent la maintenance du document.

---

Les annexes de ce cours sont conçues comme une **boîte à outils active**, utilisable sans relire les chapitres. Quatre d'entre elles — E, F, H et M — sont **versionnées et datées** : elles contiennent des données périssables et doivent être révisées à chaque revue du document.

---


## Annexe A — Glossaire

**Accès conditionnel** — Mécanisme subordonnant l'accès aux ressources à l'état de conformité de l'appareil. §28.8
**Actif** — Élément matériel, logiciel, informationnel, humain ou de service ayant une valeur pour l'organisation ou participant au fonctionnement de son système d'information. Un actif sans propriétaire nommé est un actif *orphelin*, pas un non-actif.
**Actif de niveau 0** — Actif dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, hyperviseur, sauvegarde, coffre-fort, chaîne de construction. §11.7
**Actif d'entrée** — Actif par lequel un attaquant peut arriver, exposé par conception. §11.7
**Actif éphémère** — Actif créé et détruit automatiquement, absent des inventaires réseau. §10.8
**Actif maintenu** — Actif disposant d'un propriétaire nommé, d'une classe de service et d'une preuve de conformité.
**Actif orphelin** — Actif réel du périmètre, sans propriétaire désigné. Jamais exclu du dénominateur.
**Agent** — Programme résident remontant l'état d'une machine à une console centrale. §15.1
**Agilité cryptographique** — Capacité à changer d'algorithme ou de protocole sans reconstruire les applications. §24.8
**Anneau de déploiement** — Population successive recevant un correctif, avec critère de passage. §18.4
**Appliance** — Équipement ou machine virtuelle préconstruite dont le système n'est pas maintenable par le client. §3.1
**Arbre de décision** — Suite de questions ordonnées produisant une action plutôt qu'un score. §16.3
**Atteignabilité** — Possibilité effective d'appeler le code vulnérable dans un contexte donné. §11.6
**Autorisation déléguée** — Accès accordé à une application tierce au nom d'un utilisateur, matérialisé par un jeton, non révoqué par un changement de mot de passe. §31.6
**Backlog** — Ensemble des constats ouverts. §17.10
**Baseline** — Référentiel de configuration dérivé et versionné, propre à l'organisation. §22.3
**Bleu / vert** — Stratégie de déploiement à deux environnements complets, avec bascule du trafic. §6.4
**Chaîne de confiance** — Mécanisme cryptographique garantissant l'origine d'un paquet ou d'un micrologiciel. §2.3
**Chemin d'attaque** — Enchaînement d'étapes menant d'un point d'entrée à une cible. §11.4
**Classe de service** — Regroupement d'actifs partageant délais, fenêtres et niveau de test. §7.2
**CNA** — Organisation accréditée pour attribuer des identifiants de vulnérabilité. §4.2
**Combinaison toxique** — Ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur. §11.5
**Compte de secours** — Compte d'urgence permettant l'accès quand les mécanismes normaux échouent. §24.2
**Conduit** — Chemin de communication entre zones, au sens des normes industrielles. §29.2
**Conformité** — Part des actifs se trouvant dans l'état attendu. Toujours accompagnée de son dénominateur. §38.2
**Constat** — Toute observation appelant une décision de remédiation : vulnérabilité, écart de configuration, résultat d'audit, secret exposé. §14.2
**Contrôleur de gestion à distance** — Composant permettant d'administrer un serveur indépendamment de son système d'exploitation. Actif de niveau 0. §27.1
**Convergence** — Réapplication périodique d'un état désiré par un outil de gestion de configuration. §23.3
**Correctif** — Modification publiée par un éditeur corrigeant un défaut.
**Correction virtuelle** — Blocage de l'exploitation en amont, sans modifier l'actif. §20.3
**Couverture** — Part du périmètre de référence atteinte par un outil ou un processus. §38.2
**CPE** — Nomenclature d'identification de produits, historique des bases de vulnérabilités. §4.3
**Critère d'arrêt** — Seuil chiffré interrompant automatiquement un déploiement. §18.4
**CSAF** — Format d'avis de sécurité lisible par machine. §4.8
**CVE** — Identifiant unique de vulnérabilité ; clé de dédoublonnage, pas jugement de gravité. §4.2
**CVSS** — Système de notation de la gravité technique intrinsèque d'une vulnérabilité. §4.4
**CWE** — Catalogue de types de faiblesses, indépendant des produits. §4.3
**Défaut d'autorisation** — Vulnérabilité applicative permettant d'accéder à des données d'autrui ; invisible à l'analyse automatique. §25.1
**Délai d'observation** — Temps volontairement laissé entre publication et déploiement pour que les régressions apparaissent ailleurs. §18.3
**Dénominateur** — Ensemble sur lequel un indicateur est rapporté ; l'attribut le plus important d'une mesure. §38.2
**Dépendance transitive** — Dépendance d'une dépendance, non choisie directement. §3.6
**Dépriorisation** — Décision documentée de ne pas traiter maintenant, avec date de revue. Un constat déprioritisé reste ouvert. §16.6
**Dérive de configuration** — Écart croissant entre l'état réel et la référence. §23.1
**Dérogation** — Décision formalisée, datée, bornée et compensée de ne pas appliquer la règle. §7.4
**Dette de sécurité** — Somme mesurable des corrections différées et de l'obsolescence. §1.6
**Découverte externe** — Cartographie de la surface exposée, réalisée depuis Internet. §11.2
**Démarrage sécurisé** — Vérification de la signature des composants chargés au démarrage. §3.8
**Effacement sécurisé** — Suppression de données avec preuve, sur tous les supports et copies. §35.4
**Époque** — Préfixe de version prenant le pas sur le reste dans les comparaisons de paquets. §2.6
**EPSS** — Modèle prédisant la probabilité d'exploitation d'une vulnérabilité à court terme. §4.5
**Exclusion** — Retrait volontaire d'un actif ou d'un chemin du périmètre d'un outil. Dérogation déguisée sans motif ni date de revue. §15.6, §34.4
**Exploit** — Code ou procédure transformant une vulnérabilité en effet concret. §4.1
**Exploitation active** — Observation réelle d'attaquants utilisant une vulnérabilité. §4.1
**Exposition** — Possibilité pour un attaquant d'atteindre un composant vulnérable. §11.1
**Faiblesse** — Type de défaut décrit indépendamment de tout produit. §4.1
**Fait vérifié / hypothèse probable / piste exploratoire** — Échelle de qualification d'une information. §14.7
**Fenêtre de maintenance** — Créneau pendant lequel une interruption est acceptée. §5.2
**Fichier de verrouillage** — Fichier figeant les versions exactes des dépendances. §3.6
**Fin de support** — Date après laquelle aucun correctif n'est publié, y compris de sécurité. §12.1
**Fin de support de sécurité** — Sur les équipements réseau, souvent antérieure à la fin de support matériel. §27.3
**Gel de production** — Période d'interdiction de changement, avec clause de levée pour vulnérabilité exploitée. §5.2
**Golden image** — Image de référence servant à créer les instances. §28.5
**Homologation** — Décision formelle autorisant l'usage d'un système, dont le maintien dépend du MCS. §39.5
**Immutabilité** — Principe de ne jamais modifier un système en service : reconstruire et remplacer. §3.5
**Interrupteur de fonctionnalité** — Paramètre activant ou désactivant un comportement sans redéploiement. §6.5
**Inventaire de composants (SBOM)** — Liste des composants d'un logiciel avec leurs versions. §4.8
**KEV (catalogue d'exploitation avérée)** — Recensement des vulnérabilités observées en exploitation. §4.6
**Live patching** — Application de correctifs au noyau sans redémarrage, à périmètre limité. §2.6
**MCO** — Maintien en condition opérationnelle : garantir que le système fonctionne. §1.2
**MCS** — Maintien en condition de sécurité : maintenir le niveau de sécurité sur tout le cycle de vie, preuve incluse. §1.1
**Mesure compensatoire** — Réduction de risque appliquée quand la correction est impossible ; sept attributs obligatoires. §20.7
**Micrologiciel** — Logiciel de bas niveau exécuté avant ou sous le système d'exploitation. §3.8
**Modèle de Purdue** — Découpage en niveaux d'une architecture industrielle. §3.7
**Non détecté / non vulnérable / non scanné** — Trois états distincts apparaissant identiquement dans un rapport. §15.8
**Périmètre de référence (périmètre maître)** — Union des sources d'inventaire, incluant orphelins et actifs à décommissionner. Point de départ du choix de dénominateur, **pas dénominateur universel** : chaque indicateur définit sa population éligible. §10.3, Annexe I.4
**Population éligible** — Sous-ensemble du périmètre maître auquel un contrôle donné s'applique effectivement. Annexe I.4
**Non mesuré** — Actif éligible à un contrôle mais non évalué. Ne devient jamais conforme par défaut. Annexe I.4
**N/A (non applicable)** — Actif hors de la population éligible d'un contrôle, avec motif documenté. Annexe I.4
**Horloge de risque** — Décompte du temps pendant lequel le risque existe ; ne se suspend jamais, contrairement au délai opérationnel de traitement. §17.5
**Ratio conservateur** — Taux calculé en traitant tout actif non mesuré comme non conforme. Hypothèse de prudence, pas mesure. Annexe K.2
**Point de non-retour** — Instant après lequel un retour arrière exige une restauration de données. §6.7
**Preuve d'état** — Version ou révision relevée directement sur l'actif, horodatée. §2.9
**Propriétaire métier** — Personne décidant de l'interruption et portant le risque. §5.5
**Propriétaire technique** — Personne exécutant la correction et produisant la preuve. §5.5
**Protection contre le retour en arrière** — Refus d'installer une version antérieure vulnérable. §6.11
**PSIRT** — Fonction traitant la sécurité des produits mis sur le marché. §33.2
**purl** — Nomenclature d'identification de paquets logiciels dans leur écosystème. §4.3
**Récurrence** — Réapparition d'un constat clos ; signale presque toujours un problème d'image de référence. §17.9
**Rétroportage (backport)** — Application d'un correctif à une version ancienne sans changer son numéro amont. §2.2
**Rolling update** — Déploiement progressif instance par instance. §6.4
**Sanctuarisation** — Réduction d'un système à un périmètre d'usage minimal, strictement contrôlé. §32.2
**Sas de transfert** — Étape contrôlée d'entrée de fichiers dans une zone industrielle. §29.5
**SSVC** — Approche de priorisation par arbre de décision. §4.7
**Support étendu** — Correctifs de sécurité au-delà de la fin de support, payants et conditionnés. §12.1
**Suspension de compteur** — Arrêt légitime et limitativement défini du décompte d'un délai. §17.5
**Témoin (canary)** — Déploiement sur une fraction du trafic ou du parc, avec mesure. §6.4
**Traîne longue** — Résidu d'actifs non traités en fin de campagne ; concentre une part disproportionnée du risque. §18.10
**VEX** — Déclaration d'exploitabilité d'un composant vulnérable dans un produit donné. §4.8
**Zone** — Ensemble d'actifs industriels partageant les mêmes exigences de sécurité. §29.2
**0-day** — Vulnérabilité sans correctif disponible. §4.1
**n-day** — Vulnérabilité corrigée mais non appliquée ; à l'origine de l'écrasante majorité des compromissions. §4.1

---
