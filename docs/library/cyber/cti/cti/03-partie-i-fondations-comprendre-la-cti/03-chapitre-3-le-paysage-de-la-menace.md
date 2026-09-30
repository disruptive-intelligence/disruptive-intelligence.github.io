---
title: Chapitre 3 — Le paysage de la menace
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - ../index.md
- - 'Partie I — Fondations : comprendre la CTI'
  - index.md
---

grille de lecture de l'analyste CTI

*Ce chapitre fournit un socle complet et autosuffisant sur le paysage de la menace. Il est conçu pour que le lecteur dispose de toutes les clés de compréhension nécessaires sans avoir lu les autres cours de la bibliothèque. Les renvois vers les cours APT, Écosystèmes cybercriminels, et Dark Web enrichissent la lecture mais ne la conditionnent pas.*

## 3.1 Les catégories d'acteurs

Le paysage de la menace cyber est structuré par 5 catégories d'acteurs aux motivations, ressources, et modes opératoires distincts. L'analyste CTI doit savoir dans quelle catégorie se situe l'acteur qu'il étudie, car cette catégorisation oriente toute l'analyse : les objectifs attendus, les TTP probables, la persistance anticipée, et les contre-mesures appropriées.

**Les acteurs étatiques (APT)** sont sponsorisés par un État — service de renseignement, armée, ou contractor mandaté. Leurs motivations : espionnage (politique, militaire, industriel), sabotage (infrastructure critique), influence (opérations informationnelles), et pré-positionnement stratégique (accès maintenu sans action immédiate, pour une utilisation future en cas de conflit). Leurs ressources sont considérables : budget étatique, tradecraft mature, outils custom combinés avec des LOLBins (Living off the Land Binaries — utilisation d'outils légitimes du système d'exploitation pour éviter la détection), renseignement préalable sur la cible, et tolérance au risque faible (furtivité maximale). Le dwell time (temps entre la compromission et la détection) est typiquement de mois à années. L'OPSEC est élevée — l'attaquant cherche à rester indétecté le plus longtemps possible.

Les groupes de référence par pays (résumé structurant — pour les profils détaillés, voir le cours APT) :

**Russie** — services : SVR (APT29/Cozy Bear — espionnage furtif, supply chain, abus de services cloud ; campagne de référence : SolarWinds/SUNBURST 2020), GRU (APT28/Fancy Bear — espionnage + influence, exploitation de vulnérabilités ; Sandworm/Unit 74455 — sabotage d'infrastructures critiques, wipers, campagne de référence : NotPetya 2017, attaques réseau électrique ukrainien), FSB (Gamaredon — ciblage massif de l'Ukraine). Tendance : opérations hybrides combinant cyber, influence, et actions cinétiques, particulièrement depuis l'invasion de l'Ukraine en 2022.

**Chine** — services : MSS (APT41 — double casquette espionnage étatique + cybercriminalité ; APT40 — espionnage maritime et défense ; APT10 — ciblage des MSP via Cloud Hopper), PLA et affiliés (Volt Typhoon — pré-positionnement dans les infrastructures critiques américaines avec living-off-the-land quasi exclusif ; Salt Typhoon — compromission d'opérateurs télécom pour accéder aux systèmes d'interception légale). Tendance : exploitation massive de vulnérabilités d'appliances réseau edge (Ivanti, Fortinet, Citrix, Barracuda), pré-positionnement stratégique sans action immédiate.

**Corée du Nord** — service : RGB (Lazarus Group — vol de cryptomonnaies pour financer le régime — Bybit $1,5 Mrd en 2025, Ronin Network $620M en 2022 ; APT38/BlueNoroff — braquages SWIFT ; Kimsuky — espionnage diplomatique et nucléaire). Tendance : ingénierie sociale sophistiquée sur LinkedIn, ciblage de la supply chain (3CX 2023), vol massif de crypto.

**Iran** — services : MOIS/IRGC (APT33/Peach Sandstorm — énergie et aérospatial ; APT34/OilRig — gouvernements Moyen-Orient ; APT35/Charming Kitten — social engineering avancé ciblant chercheurs et dissidents ; MuddyWater — PowerShell obfusqué, outils open source). Tendance : opérations destructives ponctuelles (wipers), surveillance des dissidents, social engineering très ciblé.

**Les cybercriminels organisés** sont motivés par le profit financier. Le modèle dominant en 2024-2026 est le **Crime-as-a-Service** : chaque fonction est spécialisée et externalisable. Le Ransomware-as-a-Service (RaaS) — l'opérateur développe et maintient le ransomware, les affiliés le déploient contre des cibles, les deux partagent les revenus (typiquement 70/30 ou 80/20). Les IAB (Initial Access Brokers) vendent des accès réseau compromis (VPN, RDP, Citrix) aux affiliés RaaS. Les infostealers (Lumma, RedLine, Vidar) volent automatiquement les credentials, cookies, et données de navigateur des victimes — les logs sont vendus sur des marchés spécialisés (Russian Market) et alimentent le pipeline vers les compromissions d'entreprise. Les temporalités sont courtes (jours à semaines — smash and grab), l'OPSEC est variable (du script kiddie au groupe structuré comme LockBit).

Exemples structurants : LockBit (RaaS dominant 2022-2024, disruption partielle par Operation Cronos en février 2024, réapparition sous LockBit 4.0), Lumma Stealer (infostealer dominant 2024-2025, infrastructure disruptée en mai 2025 par une opération coordonnée Microsoft/Europol — mais le développeur reste actif). *Pour la cartographie complète de l'économie cybercriminelle : voir le cours Écosystèmes cybercriminels.*

**Les hacktivistes** sont motivés par l'idéologie, la réputation, et l'impact médiatique. Leurs outils sont publics (DDoS, défacement, leaks), leur OPSEC faible à moyen, et leur impact souvent limité techniquement mais significatif médiatiquement. Le paysage hacktiviste post-2022 est fortement polarisé par le conflit russo-ukrainien : groupes pro-russes (KillNet, NoName057(16) — DDoS, parfois des fuites de données), groupes pro-ukrainiens (IT Army of Ukraine — DDoS coordonné via Telegram), et groupes idéologiques divers (Anonymous Sudan — DDoS massif, démantelé en 2024).

**Les mercenaires cyber / PSO** (Private Sector Offensive) sont des entreprises commerciales qui vendent des capacités d'espionnage à des États. NSO Group (Pegasus — spyware mobile ciblant journalistes, dissidents, opposants politiques), Intellexa (Predator), Candiru. Leur pertinence pour la CTI : leurs outils apparaissent dans les campagnes d'espionnage — l'analyste qui identifie un spyware Pegasus sait que le commanditaire est un client étatique de NSO, pas un cybercriminel.

**Les insiders** (employés malveillants ou négligents) opèrent avec des accès légitimes (pas de mouvement latéral classique), des motivations variables (vengeance, profit, négligence, recrutement par un service étranger), et une détection qui relève autant du RH et du juridique que de la cybersécurité. La CTI intervient dans la corrélation comportementale et le croisement avec les indicateurs de recrutement par des services étrangers.

## 3.2 Les vecteurs d'accès initial dominants (2024-2026)

Le **phishing/spearphishing** reste le vecteur n°1 en volume. L'évolution : les kits de phishing AitM (Adversary-in-the-Middle) interceptent les tokens MFA en temps réel, rendant le MFA classique (SMS, push) moins efficace contre les attaques ciblées.

L'**exploitation de vulnérabilités périmétriques** est le vecteur n°1 en impact pour les acteurs étatiques et les affiliés RaaS sophistiqués. Les appliances réseau edge (VPN Ivanti/Pulse Secure, firewalls Fortinet, passerelles Citrix, appliances Barracuda) sont des cibles systématiques — elles sont exposées sur Internet, rarement patchées rapidement, et donnent un accès direct au réseau interne.

Les **credentials volées via infostealers** constituent le pipeline le plus industrialisé : infostealer déployé sur des milliers de machines (via phishing, publicités malveillantes, logiciels piratés) → logs collectés automatiquement → vendus sur les marchés de logs (Russian Market) → exploités par des affiliés RaaS ou des IAB pour compromettre les réseaux d'entreprise. Ce pipeline est détaillé dans le cours Écosystèmes cybercriminels.

La **supply chain** (logicielle et prestataire) est le vecteur le plus difficile à défendre : l'attaquant compromet un fournisseur de confiance et utilise cette position pour atteindre ses clients (SolarWinds, 3CX, compromission de sous-traitants de maintenance — c'est exactement le cas MERIDIAN).

## 3.3 Dynamiques structurelles et tendances

**La convergence crime-état :** des acteurs opèrent simultanément pour un État et pour leur propre profit (APT41 — espionnage MSS + cybercriminalité personnelle), ou des acteurs criminels sont tolérés ou instrumentalisés par des États (les groupes ransomware russophones opèrent en toute impunité tant qu'ils ne ciblent pas la CEI). Cette convergence rend l'attribution plus complexe.

**Living off the Land (LotL) :** l'utilisation systématique d'outils légitimes du système d'exploitation (PowerShell, WMI, certutil, bitsadmin, mshta) pour éviter la détection. Volt Typhoon est l'exemple extrême : quasi aucun outil custom, uniquement des LOLBins. La conséquence pour la CTI : la détection basée sur les outils ne fonctionne plus — il faut détecter les comportements.

**Le ciblage systématique des appliances edge :** les appliances réseau exposées sur Internet (VPN, firewalls, passerelles) sont devenues le vecteur d'accès privilégié des acteurs étatiques et des affiliés RaaS sophistiqués. La gestion de ces appliances (patching rapide, monitoring dédié) est devenue un enjeu critique.

**Le pré-positionnement stratégique :** certains acteurs étatiques (Volt Typhoon, certains groupes russes) compromettent des infrastructures critiques sans mener d'action immédiate — ils maintiennent un accès dormant, utilisable en cas de conflit. C'est une menace existentielle pour les opérateurs d'énergie, de télécom, et de transport — et c'est exactement le profil de l'incident EDE dans MERIDIAN.

## 3.4 Fil rouge — MERIDIAN : positionner UNC-VOLT dans le paysage

> **🔎 MERIDIAN — Épisode 3**
>
> Élise utilise le panorama de menace pour formuler ses hypothèses initiales sur UNC-VOLT.
>
> Le profil de l'incident (ciblage d'un opérateur d'énergie OIV, pré-positionnement OT sans action immédiate, tradecraft sophistiqué avec DLL sideloading et exploitation Ivanti, pas de ransomware ni d'exfiltration financière) élimine d'emblée les catégories hacktiviste et cybercriminel classique. Il reste trois hypothèses :
>
> **H1 :** Acteur étatique russe (Sandworm/GRU) — ciblage des infras critiques européennes cohérent avec le contexte géopolitique post-2022, TTP compatibles (Sandworm cible les opérateurs d'énergie).
> **H2 :** Acteur étatique chinois (Volt Typhoon ou cluster similaire) — pré-positionnement sans action immédiate, exploitation d'appliance edge (Ivanti), LotL.
> **H3 :** Mercenaire cyber / groupe offensif privé vendant des accès à un État — tradecraft sophistiqué sans signature d'un groupe connu.
> **H4 :** Acteur criminel sophistiqué ayant pivoté vers l'OT — peu probable mais à ne pas exclure sans données.
>
> Ces hypothèses seront testées avec l'ACH au Ch.10.

---
