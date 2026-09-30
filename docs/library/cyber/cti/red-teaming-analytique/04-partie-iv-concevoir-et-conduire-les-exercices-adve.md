---
title: Partie IV — Concevoir ET conduire les exercices adversariaux (ch.16-22)
source: Cyber/Red_Teaming.md
note: Red teaming analytique
up:
- - Red teaming analytique
  - index.md
---

*Deuxième couche du triptyque : transformer la pensée adversaire en exercices. Cette partie traite du **comment exercer**. Elle ne couvre pas encore **quoi tester** — c'est l'objet de la Partie V.*

*Wargame et tabletop sont ici présentés comme deux **modalités complémentaires** d'un même champ : l'exercice adversarial structuré. Leurs promesses sont distinctes :*

- **Wargame** = dynamique compétitive, tours, logique d'adaptation Red/Blue, pression du temps
- **Tabletop** = discussion structurée, coordination, maîtrise des procédures et de la gouvernance

---


## Chapitre 16 — Panorama des formats d'exercice adversarial

### Synopsis

**La promesse de ce chapitre** : donner au lecteur une carte claire des formats d'exercice adversarial et des critères pour choisir entre eux.

Les trois familles : wargame, tabletop, hybride. Pour chaque famille : ce qu'elle permet d'observer, ce qu'elle ne permet pas, durée typique, public, coûts de préparation, logistique.

**Tableau de choix — quel format pour quel objectif ?**

| Objectif | Format recommandé | Pourquoi |
|----------|-------------------|----------|
| Tester la prise de décision sous pression évolutive | Wargame | Dynamique compétitive, adaptation Red/Blue, tours successifs |
| Tester la connaissance et l'application des playbooks | Tabletop technique | Discussion structurée, vérification des procédures |
| Tester la gouvernance de crise et les décisions exécutives | Tabletop stratégique | Focus sur les décisions non techniques, accessible au COMEX |
| Tester la coordination technique/stratégique | Exercice hybride | Deux salles, canal contrôlé, révèle les frictions |
| Anticiper une campagne longue durée | Wargame géopolitique | Horizon 6-18 mois simulés, multi-couches |
| Tester la résilience supply chain | Wargame supply chain | Modélise l'opacité des tiers |
| Évaluer rapidement une hypothèse défensive | Devil's Advocacy / pre-mortem | TAS légère, 1-3h, pas d'infrastructure |

Les trois rôles fondamentaux communs à tous les formats : Blue, Red, White/Control.

**Relation avec les autres formats d'exercices** (compliance NIS 2, TLPT DORA, exercices sectoriels) : un exercice adversarial de qualité peut satisfaire la compliance — mais la compliance seule ne produit pas un exercice adversarial de qualité. Cette distinction est fondamentale.

> **🪞 MIRRORGATE — Épisode 16 :** Diane présente au COMEX. Le DG : « Ce n'est pas un war game style jeu vidéo ? » Diane : « Non. Le Pentagone fait ça depuis 200 ans. Vos concurrents commencent à le faire. Vous n'avez jamais testé vos décisions autrement que dans une diapo PowerPoint. »

---


## Chapitre 17 — Wargame

dynamique compétitive, tours et adaptation Red/Blue

### Synopsis

**La promesse du wargame** : observer comment les décisions Blue évoluent face à un adversaire qui s'adapte en temps réel, tour après tour.

Ce qui est propre au wargame : la dynamique compétitive (Red ne joue pas un script mais adapte ses actions aux réponses Blue), la logique de tours (simulation du temps compressé, chaque tour = X heures ou X jours), l'observation des boucles de rétroaction (Blue fait → Red réagit → Blue adapte → Red pivote).

Formats : seminar wargame (discussion, 2-4h), matrix wargame (argumentation + arbitrage facilitateur, 4-8h), wargame avec règles formelles (résolution mécanique par dés pondérés ou tables, plus immersif).

Applications typiques du wargame : simulation d'incident majeur, anticipation de campagnes APT (wargame géopolitique), simulation d'attaque supply chain, exercice d'escalade de crise.

> **🪞 MIRRORGATE — Épisode 17 :** Diane explique à l'équipe la différence entre un wargame et un tabletop. « Dans un tabletop, Red est dans le scénario scripté — il fait ce qui est prévu. Dans un wargame, Red est dans la salle d'à côté, il réagit à vos décisions, il change de plan s'il est bloqué. Le wargame est un combat, le tabletop est une répétition. »

---


## Chapitre 18 — Wargame : conception, scénarisation et conduite

### Synopsis

Méthodologie complète de conception.

**Phase 1 — Cadrage :** objectif, participants, format, durée. **Phase 2 — Scénarisation en couches :** couche de fond (contexte géopolitique et sectoriel), couche initiale (situation de départ), injects scriptés, branches conditionnelles (si Blue fait X, Red fait Y). **Phase 3 — Règles du jeu :** déroulement des tours, simulation du temps, évaluation des décisions, arbitrage des résultats. **Phase 4 — Logistique :** salle, supports, rôles, observateurs, enregistrement.

**Variantes thématiques traitées dans ce chapitre :**

- Wargame de crise cyber (incident majeur, 5 phases : alerte, confinement, escalade, éradication, recovery). Les dilemmes : payer/ne pas payer, communiquer/se taire, couper/maintenir l'OT, signaler/attendre.
- Wargame géopolitique (horizon long, multi-couches : géopolitique, informationnelle, cyber, organisationnelle).
- Wargame supply chain (spécificité : le Blue ne contrôle pas les défenses des tiers, doit décider avec une opacité réaliste).

Erreurs courantes : scénario trop complexe, trop facile, Red qui joue pour « gagner » au lieu de jouer avec réalisme, wargame sans objectif clair.

> **🪞 MIRRORGATE — Épisode 18 :** Premier wargame d'Hélio. Scénario ransomware avec exfiltration. Tour 3 : le RSSI veut confiner. Le directeur de production refuse — livraison ESA dans 5 jours. Le DG hésite. Personne ne sait qui a l'autorité de trancher. « Ce conflit d'autorité est exactement ce qu'on cherchait. »

---


## Chapitre 19 — Tabletop

discussion structurée, coordination et procédures

### Synopsis

**La promesse du tabletop** : vérifier que les procédures existent, sont connues, et produisent une coordination fluide quand on les suit — dans un format de discussion structurée où personne n'exécute réellement d'action.

Ce qui est propre au tabletop : la discussion structurée (les participants parlent de ce qu'ils feraient, n'exécutent pas), le focus sur les processus et la coordination (pas sur la prise de décision adversaire dynamique), l'accessibilité (2-4h, 8-20 participants, pas d'infrastructure technique).

**Ce que le tabletop teste :** connaissance des processus, coordination entre les rôles, qualité de la prise de décision sur scénario scripté, identification des angles morts procéduraux.

**Ce que le tabletop ne teste PAS :** compétences techniques individuelles, performance sous stress extrême (le stress d'un tabletop n'est pas celui d'un incident réel), capacité réelle à exécuter (dire « je confine le serveur » dans un tabletop ne prouve pas qu'on sait le faire techniquement), adaptation adversaire (le Red ne s'adapte pas dans un tabletop — il déroule le scénario).

Les trois niveaux : technique (SOC/CERT/IT), stratégique (COMEX/juridique/communication), hybride (couvert au Ch.21).

> **🪞 MIRRORGATE — Épisode 19 :** Diane analyse les « exercices » passés d'Hélio — en réalité des présentations PowerPoint. « Ce n'était pas un tabletop. C'était une réunion d'information. Un tabletop fait mal : les participants doivent prendre des décisions, affronter des dilemmes, réaliser qu'ils ne savent pas quelque chose qu'ils auraient dû savoir. »

---


## Chapitre 20 — Tabletop : conception des injects et conduite

### Synopsis

Les injects sont le carburant du tabletop.

**Principes de conception :** réalisme (fondé sur des TTP documentées), escalade progressive, dilemmes intégrés (pas de réponse évidente), multi-dimensionnalité (techniques, opérationnels, communicationnels, réglementaires, humains, adversaires).

**Timing des injects :** trop vite → submergement ; trop lent → enlisement. Le facilitateur adapte en temps réel.

**Tabletop technique** : tester les playbooks IR, la chaîne détection → qualification → escalade, la coordination SOC/CERT, les décisions de confinement, la collecte de preuves, l'utilisation des outils.

**Tabletop stratégique** : tester l'activation de la cellule de crise, les processus de décision exécutive, la communication de crise, les obligations réglementaires (ANSSI, CNIL, NIS 2, DORA), la coordination avec les parties prenantes externes. Les dilemmes classiques : payer/ne pas payer, communiquer/se taire, arrêter/continuer, signaler/attendre.

Banque d'injects réutilisables (voir Annexe D).

> **🪞 MIRRORGATE — Épisode 20 :** Inject conçu par Diane : « Un journaliste de La Tribune appelle en affirmant avoir reçu des documents internes d'Hélio d'un groupe ransomware, dont un rapport d'audit nucléaire classifié. Article prévu demain matin. Que faites-vous ? » Cet inject teste simultanément communication de crise, coordination technique-juridique, et pression temporelle.

---


## Chapitre 21 — L'exercice hybride

### Synopsis

Le format le plus réaliste et le plus complexe : un exercice qui combine la dynamique compétitive du wargame (adaptation Red/Blue) et la discussion structurée du tabletop multi-niveaux (technique + stratégique simultanément).

Mécanique : deux salles (technique et stratégique), deux facilitateurs synchronisés, un canal de communication contrôlé. Le groupe technique reçoit les injects opérationnels, le groupe stratégique reçoit les injects décisionnels. Les deux doivent communiquer — et c'est cette communication que l'exercice teste.

Ce que l'hybride révèle : perte d'information technique → stratégique, traduction technique → décisionnel, décisions nécessitant coordination des deux niveaux, frictions de tempo (le technique trop lent pour le stratégique, ou inversement).

> **🪞 MIRRORGATE — Épisode 21 :** Tabletop hybride. Salle A : SOC+CERT+IT. Salle B : COMEX+juridique+communication. Canal unique : talkie-walkie simulant des appels. Tour 4 : le CERT découvre des données de santé exfiltrées. Le RSSI ne transmet pas l'information au COMEX pendant 45 minutes. Quand le DPO l'apprend enfin, le compteur CNIL a déjà commencé. « Dans un incident réel, le DPO l'aurait appris par un article de presse. »

---


## Chapitre 22 — Facilitation, observation et RETEX

la colonne vertébrale commune

### Synopsis

**Le rôle le plus critique et le plus sous-estimé** : le facilitateur (White Team lead). Un exercice mal facilité est une perte de temps — un exercice bien facilité produit des insights que des mois d'audit ne révèleraient pas.

Compétences : maîtrise du scénario, lecture de la salle, neutralité, gestion du temps.

**Protocole d'observation :** décisions prises (et celles évitées), processus utilisés (ou improvisés), informations demandées (et celles oubliées), conflits de rôle, hypothèses non vérifiées, silences révélateurs.

**Le RETEX en deux temps :**

- **Hot wash** (à chaud, 30-60 min) : émotions encore vives, impressions brutes, premiers constats.
- **Cold wash** (structuré, quelques jours après) : analyse consolidée avec les observations documentées.

**Le livrable final :** rapport calibré selon l'audience — synthèse COMEX (2 pages) et détail opérationnel RSSI. Matrice de suivi des recommandations avec responsable et échéance.

**Ce chapitre s'applique à tous les formats** (wargame, tabletop, hybride) — c'est la colonne vertébrale commune de la partie IV.

> **🪞 MIRRORGATE — Épisode 22 :** Diane rédige le rapport du premier cycle d'exercices. Constatations : aucun processus d'escalade SOC→COMEX, conflit d'autorité RSSI/production, notification ANSSI non maîtrisée, communication de crise inexistante. Le RSSI : « C'est brutal. Mais si on avait vécu ça en vrai, ça aurait été pire. »

---
