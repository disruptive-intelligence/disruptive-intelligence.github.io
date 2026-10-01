---
title: Annexes
source: Cyber/01 CTI & renseignement/Méthodes d'analyse/Red teaming analytique.md
note: Red teaming analytique
up:
- - Red teaming analytique
  - index.md
---

---


## Annexe A — Glossaire du red teaming analytique

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — TAS évaluant des hypothèses concurrentes contre des preuves |
| **Angle mort (blind spot)** | Zone de vulnérabilité non perçue par l'organisation |
| **Anti-pattern** | Pattern récurrent qui fait échouer un programme de red teaming |
| **Biais de confirmation** | Tendance à chercher les informations confirmant une croyance existante |
| **Blue Team** | Participants jouant leur propre rôle (défenseurs / décideurs) |
| **Cold wash** | Débriefing analytique post-exercice, structuré, quelques jours après |
| **Control / White Team** | Équipe de facilitation et d'arbitrage d'un exercice |
| **Crown Jewels Analysis** | Identification des actifs critiques du point de vue adversaire |
| **Devil's Advocacy** | TAS de contradiction méthodique — défendre systématiquement la position contraire |
| **Exercice adversarial** | Terme générique couvrant wargame, tabletop, et exercices hybrides |
| **Groupthink** | Pensée de groupe — convergence qui supprime les opinions divergentes |
| **Hot wash** | Débriefing à chaud immédiatement après un exercice |
| **HIPPO** | Highest Paid Person's Opinion — biais organisationnel |
| **I&W** | Indicators and Warnings — indicateurs signalant un changement de posture |
| **Inject** | Événement scripté injecté dans un exercice |
| **Matrix wargame** | Format de wargame basé sur l'argumentation arbitrée |
| **Normalisation de la déviance** | Signaux anormaux devenus « normaux » par habituation |
| **OODA** | Observe-Orient-Decide-Act (Boyd) — cycle décisionnel |
| **Outside-In Thinking** | TAS analysant un problème depuis l'extérieur de l'organisation |
| **Pre-mortem** | TAS de projection dans un futur d'échec pour en identifier les causes |
| **Quadrant Crunching** | TAS de scénarisation par matrice 2×2 |
| **Red Hat Analysis** | TAS d'empathie adversaire immersive |
| **Red Team** | Équipe simulant l'adversaire dans un exercice |
| **Red teaming analytique** | Discipline structurée de pensée adversaire pour tester hypothèses et décisions |
| **Red teaming technique** | Simulation d'intrusion réelle (pentest offensif) — distinct du red teaming analytique |
| **Seminar wargame** | Format léger de wargame basé sur la discussion |
| **Stress-test** | Démontage systématique des hypothèses d'un plan ou d'une stratégie |
| **Tabletop exercise (TTX)** | Exercice de discussion structurée autour d'un scénario |
| **TAS** | Techniques Analytiques Structurées |
| **Team A / Team B** | TAS de débat contradictoire structuré |
| **Wargame** | Simulation structurée avec dynamique compétitive Red/Blue |
| **What-If Analysis** | TAS d'exploration des conséquences de changements d'hypothèses |

---


## Annexe B — Catalogue des techniques analytiques structurées

| Technique | Catégorie | Participants | Durée | Livrable | Usage principal |
|-----------|-----------|-------------|-------|----------|-----------------|
| Devil's Advocacy | Challenge | 2-5 | 1-2h | Note de contre-argumentation | Tester une hypothèse dominante |
| Team A / Team B | Débat | 6-12 | 4-8h | Deux analyses concurrentes | Arbitrer entre deux options |
| Pre-mortem | Anticipation | 5-15 | 2-3h | Causes d'échec + indicateurs | Avant implémentation d'un plan |
| ACH | Évaluation | 3-8 | 3-6h | Matrice + hypothèse prioritaire | Comparer des scénarios |
| What-If Analysis | Prospective | 3-10 | 2-4h | Matrice I&W + actions | Conditions de rupture |
| Outside-In Thinking | Recadrage | 5-12 | 2-4h | Facteurs externes | Changement de contexte |
| Quadrant Crunching | Scénarisation | 5-15 | 3-5h | 4 scénarios + implications | Futurs possibles |
| Red Hat Analysis | Empathie | 3-8 | 3-6h | Profil adversaire enrichi | Acteur spécifique |
| Crown Jewels | Cartographie | 5-12 | 2-4h | Matrice actifs × risques | Cibles prioritaires adversaires |
| Seminar Wargame | Exercice | 10-20 | 2-4h | Constatations + recommandations | Coordination + décisions light |
| Matrix Wargame | Exercice | 15-30 | 4-8h | Rapport de wargame détaillé | Crise multi-acteurs |
| Tabletop Exercise | Exercice | 8-25 | 2-4h | Rapport + recommandations | Playbooks, gouvernance |

---


## Annexe C — Templates d'exercices et fiches de facilitation

**C.1 — Template de scénario d'exercice :** objectifs (principal, secondaires, hors périmètre), contexte (organisation, secteur, réglementation, géopolitique), participants (Blue, Red, White), format et timing (type, durée, tours, temps simulé), scénario initial, injects par tour, branches conditionnelles, critères d'observation, grille de RETEX.

**C.2 — Fiche de rôle Red Team :** profil adversaire (acteur, motivation, capacités, contraintes, objectif), règles d'engagement (rester dans le profil, adapter aux réponses Blue, signaler les décisions clés, ne pas chercher à gagner), actions prévues par tour + alternatives.

**C.3 — Template de rapport d'exercice :** synthèse exécutive (1-2 pages), déroulé chronologique, constats détaillés par catégorie, forces identifiées, vulnérabilités classées par criticité, recommandations priorisées avec responsable et échéance, matrice de suivi, annexes.

**C.4 — Template de rapport de stress-test :** objet analysé (document, version, date), hypothèses identifiées (explicites + implicites), classification (vérifiées / plausibles / fragiles), pour chaque hypothèse fragile : impact potentiel si fausse + recommandation + indicateur de dérive, plan d'implémentation.

---


## Annexe D — Banque de scénarios et d'injects

### D.1 — Scénarios types par catégorie de menace

| Catégorie | Scénario | Adversaire | Durée simulée | Dimensions testées |
|-----------|----------|-----------|---------------|-------------------|
| Ransomware | RaaS avec exfiltration et leak site | Cybercriminel | 72h-7j | IR, crise, communication, réglementaire |
| APT / Espionnage | Intrusion longue avec pivot OT | Acteur étatique | 6-18 mois | CTI, détection, coordination, géopolitique |
| Supply chain | Compromission éditeur logiciel | Variable | 2-4 semaines | IR, supply chain, multi-organisations |
| Insider | Exfiltration par employé mécontent | Insider | 1-3 mois | DRH, juridique, forensic, éthique |
| Hybride | Cyber + désinformation + hack-and-leak | Acteur étatique | 3-6 mois | CTI, IE, L2I, communication |
| BEC | Fraude au président | Cybercriminel | 48-72h | Finance, validation, sensibilisation |
| Cloud | Compromission du tenant cloud | Variable | 1-2 semaines | Cloud security, PRA, dépendance |
| DDoS + extorsion | DDoS massif avec rançon | Cybercriminel | 24-72h | SOC, ISP, communication, continuité |

### D.2 — Injects universels

| Type | Inject | Dimension testée |
|------|--------|-----------------|
| Technique | « L'EDR détecte Mimikatz sur DC02 à 03h17 » | Détection, qualification, escalade |
| Opérationnel | « Le VPN est indisponible — 200 collaborateurs bloqués » | Continuité, priorisation |
| Médiatique | « Un journaliste appelle en citant des documents internes » | Communication de crise |
| Réglementaire | « L'ANSSI appelle pour un point de situation dans 2h » | Notification, coordination |
| Adversaire | « Le groupe publie 10 Go et un ultimatum de 48h » | Décision stratégique |
| RH | « L'analyste SOC senior d'astreinte est injoignable » | Résilience, plans B |
| Juridique | « L'avocat déconseille de communiquer, le DPO recommande de notifier » | Arbitrage, autorité |
| Fournisseur | « Le prestataire IR annonce 48h de délai » | Dépendance, alternatives |
| Financier | « L'assureur exige un rapport sous 5 jours » | Coordination juridique/financière |
| Interne | « Un collaborateur poste sur LinkedIn : notre boîte a été hackée » | Communication interne, réseaux sociaux |

---


## Annexe E — Outils et ressources de référence

| Catégorie | Outil | Type | Usage |
|-----------|-------|------|-------|
| Facilitation | Miro / Mural | SaaS | Tableaux blancs collaboratifs |
| Facilitation | Excalidraw | Gratuit (OSS) | Schémas de situation |
| Scénarisation | MITRE ATT&CK | Base de données | TTP pour le réalisme |
| Scénarisation | The DFIR Report | Blog | Intrusions complètes pour inspiration |
| Profilage | Malpedia | Base de données | Profils d'acteurs |
| Profilage | MITRE ATT&CK Groups | Base de données | Mapping acteurs ↔ TTP |
| Analyse | ACH 2.0 (Palo Alto) | Logiciel gratuit | Matrice ACH informatisée |
| Analyse | PARC ACH | Logiciel gratuit | ACH en ligne |
| Exercice | CISA Tabletop Exercise Packages | Templates | Scénarios pré-construits |
| Exercice | ENISA Cyber Exercises | Guides | Conception d'exercices |
| Wargaming | RAND Corporation | Publications | Méthodologies |
| Documentation | Obsidian | Gratuit | Suivi des recommandations |

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Red teaming analytique, pensée adversaire | **Ce cours** | — |
| Processus analytique CTI | **Cours CTI** | Ce cours (Ch.13 ACH, Ch.5-6 profilage — même rigueur) |
| Acteurs étatiques / APT | **Cours APT** | Ce cours (Ch.5-9, Ch.18 wargame géopolitique, Ch.32) |
| Réponse à incident | **Cours IR** | Ce cours (Ch.20 tabletop technique, Ch.25 stress-test plan IR, Ch.33) |
| Lutte informationnelle / L2I | **Cours L2I** | Ce cours (Ch.18, Ch.34 attaque hybride) |
| Intelligence économique | **Cours IE** | Ce cours (Ch.7 surface d'attaque stratégique, Ch.34) |
| OSINT | **Cours OSINT** | Ce cours (Ch.7 surface d'attaque OSINT sur soi-même) |
| Dark Web | **Cours Dark Web** | Ce cours (Ch.8 scénarios, Ch.33) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | Ce cours (Ch.6 modélisation, Ch.33 RaaS) |
| HUMINT et Social Engineering | **Cours HUMINT & SE** | Ce cours (Ch.7, Ch.20 injects SE) |
| Panorama de la Cybermenace | **Cours Panorama** | Ce cours (Ch.8 portfolio aligné sur CTL sectoriel) |
| FININT | **Cours FININT** | Ce cours (Ch.18 supply chain financière, Ch.33) |
| IA & Sécurité | **Cours IA & Sécurité** | Ce cours (Ch.31 micro-exercices) |
| GRC / Risques | **Cours GRC** | Ce cours (Ch.7, Ch.24-27 stress-tests, Ch.30 métriques) |
| SOC et détection | **Cours SOC** | Ce cours (Ch.20 tabletop technique, Ch.14 I&W) |
| Forensic numérique | **Cours Forensic** | Ce cours (Ch.20 chaîne de preuve dans les exercices) |
| Active Directory | **Cours AD** | Ce cours (Ch.26 reconstruction AD dans le stress-test PRA) |
| Cybersécurité du quotidien | **Cours Cyber Quotidien** | Ce cours (Ch.31 pensée adversaire quotidienne) |

---


## Annexe G — Ressources, formations et communautés

### Ouvrages de référence

| Titre | Auteur(s) | Sujet |
|-------|-----------|-------|
| *Red Team: How to Succeed by Thinking Like the Enemy* | Micah Zenko | Red teaming — principes, cas, méthodologie |
| *Psychology of Intelligence Analysis* | Richards Heuer | Biais cognitifs et TAS — le livre fondateur |
| *Structured Analytic Techniques for Intelligence Analysis* | Heuer & Pherson | Manuel complet des TAS |
| *Thinking in Bets* | Annie Duke | Décision sous incertitude |
| *The Art of the Long View* | Peter Schwartz | Scénarisation et planification stratégique |
| *Superforecasting* | Philip Tetlock | Prévision et jugement calibré |
| *Thinking, Fast and Slow* | Daniel Kahneman | Biais cognitifs — base théorique |
| *Team of Teams* | Stanley McChrystal | Coordination et adaptabilité organisationnelle |
| *The Cyber Wargaming Handbook* | US Naval War College | Méthodologie de wargaming cyber |
| *Wargaming for Leaders* | Mark Herman et al. | Wargaming stratégique appliqué |

### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| Red Team Leader (UFMCS) | US Army — Fort Leavenworth | Red teaming analytique — référence mondiale |
| Applied Critical Thinking | UFMCS | Techniques analytiques structurées |
| FOR578 — Cyber Threat Intelligence | SANS | CTI avec composante analytique |
| MGT514 — IT Security Strategic Planning | SANS | Stratégie cyber et exercices |
| Wargaming courses | King's College London | Wargaming stratégique et cyber |
| ENISA Cyber Exercises | ENISA | Conception et conduite d'exercices |

### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| Connections (Wargaming Conference) | Conférence annuelle | Plus grande conférence de wargaming |
| PAXsims | Blog/communauté | Praticiens du wargaming |
| CISA Exercises | Ressources publiques | Templates et guides |
| FIRST | Communauté CERT | Exercices inter-CERT |
| FIC / InCyber (Lille) | Conférence | Track exercices de crise |
| CyCon (Tallinn) | Conférence | Dimension stratégique du cyber |

### Publications institutionnelles

| Publication | Organisme | Contenu |
|------------|-----------|---------|
| Red Team Handbook | UFMCS / US Army | Manuel de référence |
| Cyber Tabletop Exercise Guide | CISA | Guide de conception de tabletop |
| Good Practice Guide on Exercises | ENISA | Guide européen des exercices cyber |
| Wargaming Handbook | UK MoD DCDC | Méthodologie britannique |
| TIBER-EU Framework | BCE | Cadre red team — secteur financier |
| DORA Testing Requirements (TLPT) | UE | Exigences de tests de résilience |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à la discipline du red teaming analytique — pas à un format d'exercice, pas à une méthodologie d'audit, pas à un cadre de compliance. Il forme à une **posture intellectuelle** : celle qui consiste à penser comme l'adversaire pour mieux défendre.
>
> L'architecture du cours suit un triptyque strict :
> - **Penser comme l'adversaire** (Parties I-III) — la discipline intellectuelle.
> - **Transformer cette pensée en exercices** (Partie IV) — wargame et tabletop comme deux modalités complémentaires.
> - **Utiliser cette pensée et ces exercices pour tester l'organisation** (Partie V) — le stress-test des plans et stratégies existantes.
>
> Les trois dernières parties installent cette capacité dans la durée (Partie VI) et la consolident par des cas complets (Partie VII).
>
> L'opération MIRRORGATE illustre la trajectoire : d'une organisation convaincue d'être préparée à une organisation réellement préparée. Le chemin est inconfortable — le red teaming analytique force à regarder ce qu'on préfère ignorer. Mais l'inconfort d'un exercice est infiniment préférable à l'inconfort d'un incident réel.
>
> Le cours assume quatre convictions.
> - Première : les plans non testés sont des fictions.
> - Deuxième : les biais cognitifs et organisationnels sont les vulnérabilités les plus critiques.
> - Troisième : les programmes de red teaming les plus destructeurs sont ceux qui fonctionnent en apparence — d'où le chapitre dédié aux anti-patterns.
> - Quatrième : le red teaming analytique n'est pas un luxe réservé aux grandes organisations, c'est un état d'esprit applicable à toute échelle.
>
> *Douter avec méthode • Tester avant que le réel ne teste • Regarder ce qu'on ne veut pas voir • Décider en connaissance de cause — et toujours distinguer ce qu'on sait de ce qu'on suppose.*

---

*Fin du cours — Red Teaming Analytique et Simulation Adversaire*
*Version 2025-2026 — v2 (restructuration)*
