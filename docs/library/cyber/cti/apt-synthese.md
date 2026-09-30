---
title: APT — synthèse
source: Cyber/01_CTI/APT_Synthese.md
---

*Advanced Persistent Threats — Acteurs étatiques, campagnes et géopolitique cyber*

**Cours complet — 32 chapitres • 8 parties • 7 annexes**

*Russie • Chine • DPRK • Iran • Puissances occidentales • OT/ICS • Attribution • Défense APT-ready*

---

## Table des matières

- [Fil rouge : Opération BLACKOUT](#fil-rouge-operation-blackout)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - [Ch.1 — Qu'est-ce qu'une APT](#chapitre-1-quest-ce-quune-apt)
  - [Ch.2 — Cycle de vie d'une intrusion APT](#chapitre-2-cycle-de-vie-dune-intrusion-apt)
  - [Ch.3 — Tradecraft et TTP](#chapitre-3-tradecraft-et-ttp-comment-une-apt-opere)
  - [Ch.4 — Le cyber comme instrument de puissance étatique](#chapitre-4-le-cyber-comme-instrument-de-puissance-etatique)
- **PARTIE II — RUSSIE (Ch.5-7)**
  - [Ch.5 — Russie : contexte, doctrine et appareil cyber](#chapitre-5-russie-contexte-doctrine-et-appareil-cyber)
  - [Ch.6 — Russie : les groupes APT en détail](#chapitre-6-russie-les-groupes-apt-en-detail)
  - [Ch.7 — Russie : campagnes de référence et influence](#chapitre-7-russie-campagnes-de-reference-et-influence)
- **PARTIE III — CHINE (Ch.8-10)**
  - [Ch.8 — Chine : contexte, doctrine et appareil cyber](#chapitre-8-chine-contexte-doctrine-et-appareil-cyber)
  - [Ch.9 — Chine : les groupes APT en détail](#chapitre-9-chine-les-groupes-apt-en-detail)
  - [Ch.10 — Chine : campagnes de référence et tendances](#chapitre-10-chine-campagnes-de-reference-et-tendances)
- **PARTIE IV — DPRK, IRAN ET AUTRES ACTEURS (Ch.11-15)**
  - [Ch.11 — DPRK : contexte, groupes et modèle unique](#chapitre-11-dprk-contexte-groupes-et-modele-unique)
  - [Ch.12 — DPRK : campagnes de référence](#chapitre-12-dprk-campagnes-de-reference)
  - [Ch.13 — Iran : contexte et groupes APT](#chapitre-13-iran-contexte-et-groupes-apt)
  - [Ch.14 — Iran : campagnes de référence](#chapitre-14-iran-campagnes-de-reference)
  - [Ch.15 — Autres acteurs étatiques et zones grises](#chapitre-15-autres-acteurs-etatiques-et-zones-grises)
- **PARTIE V — PUISSANCES CYBER OCCIDENTALES ET ALLIÉES (Ch.16-19)**
  - [Ch.16 — États-Unis : doctrine, agences et cyber power](#chapitre-16-etats-unis-doctrine-agences-et-cyber-power)
  - [Ch.17 — Royaume-Uni et Five Eyes](#chapitre-17-royaume-uni-et-five-eyes)
  - [Ch.18 — Israël : cyber, renseignement et supériorité technologique](#chapitre-18-israel-cyber-renseignement-et-superiorite-technologique)
  - [Ch.19 — Ukraine : cyberdéfense et guerre en temps réel](#chapitre-19-ukraine-cyberdefense-et-guerre-en-temps-reel)
- **PARTIE VI — MENACES OT ET PRÉ-POSITIONNEMENT (Ch.20-22)**
  - [Ch.20 — APT et OT/ICS : pourquoi c'est différent](#chapitre-20-apt-et-otics-pourquoi-cest-different)
  - [Ch.21 — Campagnes OT/ICS de référence](#chapitre-21-campagnes-otics-de-reference)
  - [Ch.22 — Le pré-positionnement : la menace silencieuse](#chapitre-22-le-pre-positionnement-la-menace-silencieuse)
- **PARTIE VII — GÉOPOLITIQUE, ATTRIBUTION ET PROSPECTIVE (Ch.23-28)**
  - [Ch.23 — Attribution : méthodes, limites et enjeux](#chapitre-23-attribution-methodes-limites-et-enjeux)
  - [Ch.24 — L'écosystème cyber offensif mondial](#chapitre-24-lecosysteme-cyber-offensif-mondial)
  - [Ch.25 — Géopolitique des normes cyber, droit international et cadre français](#chapitre-25-geopolitique-des-normes-cyber-droit-international-et-cadre-francais)
  - [Ch.26 — Tendances 2024-2026 et signaux d'anticipation](#chapitre-26-tendances-2024-2026-et-signaux-danticipation)
  - [Ch.27 — Construire une défense APT-ready](#chapitre-27-construire-une-defense-apt-ready)
  - [Ch.28 — Exercices de simulation](#chapitre-28-exercices-de-simulation)
- **PARTIE VIII — ÉTUDES DE CAS INTÉGRÉES (Ch.29-32)**
  - [Ch.29 — SolarWinds/SUNBURST : la supply chain comme vecteur d'espionnage](#chapitre-29-solarwindssunburst-la-supply-chain-comme-vecteur-despionnage)
  - [Ch.30 — Lazarus et l'empire crypto de la DPRK](#chapitre-30-lazarus-et-lempire-crypto-de-la-dprk)
  - [Ch.31 — Volt Typhoon : le pré-positionnement stratégique](#chapitre-31-volt-typhoon-le-pre-positionnement-strategique)
  - [Ch.32 — Synthèse BLACKOUT : attribution face à l'incertitude](#chapitre-32-synthese-blackout-attribution-et-reponse-face-a-lincertitude)
- **ANNEXES**
  - [Annexe A — Glossaire APT/CTI](#annexe-a-glossaire-aptcti)
  - [Annexe B — Groupes APT majeurs par pays](#annexe-b-groupes-apt-majeurs-par-pays)
  - [Annexe C — Conventions de nommage](#annexe-c-conventions-de-nommage-comparees)
  - [Annexe D — Timeline des cyberattaques étatiques (2007-2026)](#annexe-d-timeline-des-cyberattaques-etatiques-majeures-2007-2026)
  - [Annexe E — Mapping ATT&CK par acteur](#annexe-e-mapping-attck-par-acteur)
  - [Annexe F — Mapping de la bibliothèque](#annexe-f-mapping-de-la-bibliotheque)
  - [Annexe G — Ressources et formation](#annexe-g-ressources-et-formation)

---

## Fil rouge : Opération BLACKOUT

> **Contexte narratif — ce fil rouge traverse les 28 premiers chapitres et se conclut au Ch.32.**
>
> Un **opérateur de distribution d'énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
>
> **L'intrusion :** l'attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d'une application de supervision, se déplacé latéralement via PsExec et Kerberoasting, puis pivoté vers le réseau de supervision SCADA via un poste d'ingénierie à double connexion. Il a été détecté et éjecté avant d'atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
>
> **Le mystère :** aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L'attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d'appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
>
> L'investigation va traverser les 8 parties du cours : identification des TTP (Partie I), comparaison avec les profils par pays (Parties II-V), analyse du ciblage OT (Partie VI), processus d'attribution et calibration de la réponse (Partie VII), et synthèse complète (Partie VIII, Ch.32).

---

## PARTIE I — FONDATIONS : COMPRENDRE LES APT

*Avant d'étudier les acteurs : comprendre ce qu'est une APT, comment elle opère, et pourquoi les États utilisent le cyberespace comme instrument de puissance.*

---

### Chapitre 1 — Qu'est-ce qu'une APT

#### 1.1 Définition opérationnelle

Le terme APT (Advanced Persistent Threat) désigne un adversaire généralement state-sponsored ou state-aligned qui mène des cyberopérations sophistiquées, durables et ciblées. Chaque mot compte.

**Advanced** : l'adversaire dispose d'une capacité d'adaptation élevée, d'un tradecraft mature (OPSEC, évasion, persistence), de ressources conséquentes, et d'un renseignement préalable sur la cible. « Advanced » ne signifie pas forcément zero-day : beaucoup d'APT réussissent avec des credentials volés, des vulnérabilités connues non patchées, ou du Living off the Land. C'est la combinaison adaptation + OPSEC + ressources + mandat qui fait la différence.

**Persistent** : l'objectif n'est pas un coup unique mais un accès durable. L'adversaire investit dans la persistence (backdoors multiples, accès redondants, réinfection si éjecté). Le dwell time moyen (temps entre la compromission et la détection) se mesure en semaines à mois — et pour certaines opérations de pré-positionnement, en années.

**Threat** : c'est une menace intentionnelle, dirigée par des humains. Des opérateurs prennent des décisions en temps réel, adaptent leur approche, et ont des objectifs stratégiques définis par un commanditaire — un service de renseignement, un état-major militaire, ou un appareil gouvernemental.

#### 1.2 APT vs cybercriminalité vs hacktivisme vs insider

| Critère | APT (étatique) | Cybercriminel | Hacktiviste | Insider |
|---------|:---:|:---:|:---:|:---:|
| Motivation | Espionnage, sabotage, influence, pré-positionnement | Profit financier | Idéologie, réputation | Vengeance, profit, négligence |
| Sponsor | État, proxy, contractor | Autonome ou groupe organisé | Groupe idéologique | Employé/contractant |
| Temporalité | Mois à années | Jours à semaines | Ponctuel | Variable |
| Sélection cibles | Très ciblé (secteur, organisation) | Opportuniste ou semi-ciblé | Symboles politiques | Leur propre organisation |
| OPSEC | Très élevé (furtivité maximale) | Variable | Faible à moyen | Variable |
| Tolérance au bruit | Très faible | Moyenne (smash & grab) | Haute (cherche la visibilité) | Variable |
| Critère de succès | Accès maintenu, données exfiltrées, effet stratégique | Monétisation | Impact médiatique | Dommage ou gain personnel |

Les frontières sont floues : APT41 mène à la fois de l'espionnage étatique et du cybercrime personnel. Les groupes ransomware russophones opèrent sous la tolérance tacite de l'État. La DPRK utilise le cybervol comme source de financement étatique. Ces zones grises sont traitées au Ch.15 et analysées au Ch.24.

#### 1.3 Typologie d'objectifs APT

Le **cyberespionnage** est l'objectif le plus courant : vol de données stratégiques (propriété intellectuelle, plans militaires, communications diplomatiques, secrets commerciaux). Le **pré-positionnement** est l'objectif le plus inquiétant : maintenir un accès dormant dans des infrastructures critiques pour une activation future en cas de conflit (Volt Typhoon — Ch.22 et Ch.31). Le **sabotage** vise à endommager ou détruire des systèmes (NotPetya — $10 Mrd, Industroyer — blackouts Ukraine). L'**influence/désinformation** manipule l'opinion et déstabilise politiquement (ingérence électorale 2016, hack-and-leak). Et le **financement** génère des revenus pour contourner les sanctions (Lazarus — milliards volés en crypto — Ch.30).

#### 1.4 Le vocabulaire terrain

Un **intrusion set** est un ensemble d'activités malveillantes regroupées par TTP, infrastructure et victimologie communes — c'est ce que les vendors appellent un « groupe APT », mais c'est un regroupement analytique, pas forcément une seule équipe physique. Un **cluster** (UNC chez Mandiant, DEV chez Microsoft historiquement) est un regroupement préliminaire pas encore attribué. Une **campaign** est une série d'intrusions liées par un objectif commun sur une période donnée. Les **TTP** (Tactics, Techniques, Procedures) décrivent le « comment » de l'attaquant — plus durables que les IoC. Le **tradecraft** est le savoir-faire opérationnel global de l'attaquant (OPSEC + TTP + habitudes).

#### 1.5 Le naming chaos

Chaque éditeur CTI nomme les acteurs selon sa propre convention. CrowdStrike utilise des animaux par pays (Bear = Russie, Panda = Chine, Kitten = Iran, Chollima = DPRK, Spider = cybercrime). Microsoft utilise des phénomènes météo (Blizzard = Russie, Typhoon = Chine, Sandstorm = Iran, Sleet = DPRK, Tempest = cybercrime). Mandiant utilise APT/UNC/FIN. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit — le même acteur avec 5+ noms. La navigation utilise Malpedia (base de données de référence avec les mappings croisés) et MITRE ATT&CK Groups. L'Annexe C fournit le tableau comparatif complet.

#### 1.6 Fil rouge — BLACKOUT : le contexte

> **⚡ BLACKOUT — Épisode 1**
>
> L'alerte initiale vient du CERT mandaté : l'EDR a détecté un comportement anormal sur un poste d'ingénierie OT — un processus `rundll32.exe` chargeant une DLL non signée, avec un beaconing HTTPS régulier vers une IP aux Pays-Bas. Le parent process est un service légitime de l'application de supervision — la DLL a été placée dans son répertoire (DLL sideloading). Le CERT remonte la chaîne : l'infection initiale date de 6 semaines, via l'exploitation d'une vulnérabilité Ivanti. 6 semaines de présence non détectée. L'analyste CTI en charge doit répondre à la question : « qui est derrière ? ».

---

### Chapitre 2 — Cycle de vie d'une intrusion APT

#### 2.1 Le modèle d'intrusion moderne en 7 phases

En pratique, les équipes SOC/IR/CTI utilisent un modèle plus granulaire que la Kill Chain classique de Lockheed Martin.

**Phase 1 — Reconnaissance (J-60 à J-1) :** l'attaquant collecte des informations sur la cible. OSINT (LinkedIn — identifier les employés, les technologies utilisées via les offres d'emploi, les sous-traitants), scanning (Shodan, Censys — identifier les services exposés : VPN, portails web, appliances), et social engineering préliminaire (création de faux profils, préparation de lures de phishing personnalisés). Les APT les plus sophistiqués (APT29, Volt Typhoon) peuvent passer des semaines en reconnaissance avant l'accès initial.

**Phase 2 — Accès initial (J0) :** la première compromission. Le vecteur varie selon l'acteur : phishing ciblé (APT28, APT35), exploitation de vulnérabilité sur un service exposé (Volt Typhoon — Ivanti/Fortinet, APT40 — appliances réseau), supply chain (APT29 — SolarWinds, Lazarus — 3CX), credentials volés (APT29 — password spraying Azure AD), ou social engineering avancé (Lazarus — faux recruteurs LinkedIn).

**Phase 3 — Foothold (J0-J2) :** installation d'une persistence initiale. Dépôt d'un web shell, création d'une tâche planifiée, modification du registre, ou DLL sideloading. L'objectif est de survivre à un reboot et de disposer d'un point de retour si l'accès initial est fermé.

**Phase 4 — Escalade de privilèges (J3-J5) :** obtenir des droits admin/SYSTEM/root. Credential dumping (Mimikatz ou équivalent custom), Kerberoasting, exploitation de vulnérabilités locales, ou abus de configurations AD (ACL permissives, comptes de service surprivilégiés). L'obtention d'un compte Domain Admin est le tournant de l'intrusion.

**Phase 5 — Mouvement latéral (J5-J20+) :** l'attaquant se déplace vers les systèmes de valeur — Domain Controllers, serveurs de fichiers, boîtes mail des dirigeants, systèmes OT. Les techniques dépendent de l'acteur : PsExec (Sandworm), WMI (APT41), RDP (divers), ou uniquement des LOLBins (Volt Typhoon).

**Phase 6 — Collection et staging (J20-J45+) :** identification et rassemblement des données de valeur. Les fichiers sont copiés vers un serveur de staging, compressés et chiffrés. L'attaquant sélectionne — il ne copie pas tout, il cible ce qui correspond à son mandat.

**Phase 7 — Exfiltration / Impact (J45+) :** sortir les données (via HTTPS, DNS, services cloud) ou réaliser l'action finale (déployer un wiper, manipuler un automate OT, publier des données volées). Certaines APT ne réalisent jamais cette phase — elles se pré-positionnent et attendent (Volt Typhoon).

#### 2.2 Dwell time

Le dwell time médian global était de 10 jours en 2023 selon Mandiant M-Trends (vs 16 jours en 2022). Mais cette moyenne masque une dispersion massive : les incidents détectés par un tiers (notification externe) ont un dwell time beaucoup plus long que ceux détectés en interne. Et pour les APT étatiques ciblant des organisations peu matures, le dwell time peut dépasser 200 jours.

Les gaps de détection typiques par phase : pas de logs DNS (C2 invisible), pas d'EDR sur les serveurs (mouvement latéral invisible), pas de monitoring cloud/identity (token theft invisible), pas de DLP (exfiltration invisible).

#### 2.3 Fil rouge — BLACKOUT : la timeline

> **⚡ BLACKOUT — Épisode 2**
>
> Le CERT reconstitue la timeline : exploitation Ivanti à J0, web shell déposé à J+1, DLL sideloading pour la persistence à J+3, Kerberoasting ciblant les comptes de service à J+5, mouvement latéral via PsExec à J+8, pivot vers le poste d'ingénierie OT à J+15, tentative de reconnaissance du réseau SCADA à J+20-30, et inactivité de J+30 à la détection J+42. L'attaquant s'est pré-positionné et a cessé toute activité visible — comme s'il attendait un signal.

---

### Chapitre 3 — Tradecraft et TTP : comment une APT opère

#### 3.1 Vecteurs d'accès initial

Le **spear-phishing** reste le vecteur le plus courant en volume (APT28 — macros Word, APT35 — fausses pages de login). L'**exploitation de vulnérabilités sur les services exposés** est le vecteur n°1 en impact pour les acteurs sophistiqués : les appliances réseau edge (VPN Ivanti/Pulse Secure, firewalls Fortinet, passerelles Citrix, appliances Barracuda) sont des cibles systématiques car elles sont exposées sur Internet, rarement patchées rapidement, et donnent un accès direct au réseau interne. La **supply chain** (SolarWinds par APT29, 3CX par Lazarus, CCleaner par APT41) exploite la confiance dans un fournisseur. Les **credentials volés** (password spraying, infostealers, achat sur les marchés dark web) permettent l'accès avec des identifiants légitimes. Le **social engineering** avancé (Lazarus — faux recruteurs LinkedIn, APT35 — faux profils académiques, Kimsuky — impersonation) cible le facteur humain. Le **watering hole** (APT32 — sites d'actualité régionaux) compromet un site fréquenté par la cible. Et les **trusted relationships** (APT10 — Cloud Hopper via MSP) abusent de la confiance dans un partenaire.

#### 3.2 Persistence

Les APT installent des mécanismes de persistence pour survivre au reboot, au patch, et à la réinitialisation de mot de passe. Les techniques principales : tâches planifiées/cron (exécution régulière), services/démons malveillants, DLL sideloading (placer une DLL malveillante dans le répertoire d'un exécutable légitime), web shells (backdoor sur un serveur web), modification du registre (clés Run/RunOnce, IFEO), bootkits/firmware (persistence en dessous de l'OS — rare mais existant), comptes backdoor (comptes admin cachés), et tokens/certificats (vol ou création de tokens OAuth, certificats SAML — GoldenSAML par APT29).

Le concept clé est l'**accès redondant** : une APT mature ne dépend jamais d'un seul mécanisme. Si un web shell est détecté et supprimé, l'attaquant revient via une tâche planifiée ou un compte backdoor. C'est pourquoi le containment APT doit identifier TOUS les accès avant d'agir (Ch.27).

#### 3.3 Living off the Land

Les APT modernes évitent de déposer des malwares détectables et utilisent les outils déjà présents sur le système. PowerShell (téléchargement, exécution en mémoire, C2), WMI (exécution distante, persistence, reconnaissance), certutil (téléchargement de fichiers), mshta/msiexec (exécution de scripts/packages), rundll32 (chargement de DLL), bitsadmin (téléchargement en arrière-plan), et net.exe/nltest (énumération AD). Volt Typhoon est l'exemple extrême : quasi aucun outil custom, uniquement des LOLBins — le tradecraft qui rend la détection la plus difficile.

La conséquence pour la défense : bloquer ces outils n'est souvent pas possible (ils sont nécessaires au fonctionnement du système). Il faut monitorer leur usage anormal — PowerShell avec -EncodedCommand, certutil qui télécharge un .exe, WMI depuis un poste utilisateur vers un serveur.

#### 3.4 Command & Control et exfiltration

Les techniques C2 par difficulté de détection croissante : HTTPS beaconing (trafic chiffré, se fond dans le trafic légitime), DNS tunneling (données encodées dans les requêtes DNS), domain fronting (utilise un CDN légitime pour masquer le vrai C2), fast flux DNS (rotation rapide des IP), dead drops (messages sur des services légitimes — Pastebin, GitHub), et stéganographie (données cachées dans des images). L'exfiltration suit les mêmes canaux : HTTPS, DNS, email, ou services cloud (OneDrive, Google Drive, S3).

---

### Chapitre 4 — Le cyber comme instrument de puissance étatique

#### 4.1 Les 3 types de cyberopérations étatiques

Le **cyberespionnage** (continu, discret, long terme — APT1 vol de PI, APT29 SolarWinds) vole des informations stratégiques. La **cyberattaque destructrice** (ponctuelle, déclenchée par le contexte géopolitique — NotPetya, Shamoon, Stuxnet) endommage ou détruit des systèmes. La **cyberinfluence** (continue ou en pics électoraux — IRA/GRU 2016, hack-and-leak) manipule l'opinion. Ces types ne sont pas mutuellement exclusifs : une opération peut combiner espionnage (voler des emails) et influence (les publier). L'espionnage peut aussi être la phase préparatoire du sabotage.

#### 4.2 Le framework DIMEFIL

DIMEFIL (Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement) est le cadre utilisé par le DoD américain pour décrire les instruments de puissance d'un État. Le cyber est transversal à tous : attribution publique (Diplomatic), désinformation (Information), sabotage OT (Military), vol de PI (Economic), vol SWIFT/crypto (Financial), espionnage (Intelligence), et indictments (Law Enforcement).

#### 4.3 Le cyber comme 5ème domaine

Depuis le sommet OTAN de Varsovie (2016), le cyberespace est reconnu comme le 5ème domaine d'opérations. Ses particularités : **asymétrie** (un petit État peut infliger des dommages significatifs — DPRK, Iran), **déni plausible** (l'attribution est difficile), **zone grise** (en dessous du seuil de conflit armé), **vitesse** (action en minutes, réponse diplomatique en mois), et **continuum** (espionnage → pré-positionnement → sabotage → guerre, avec des frontières floues).

#### 4.4 Point fondamental : le cyber est un instrument universel

Les cyberopérations ne sont pas l'apanage d'un bloc. Tous les États dotés les utilisent — avec des doctrines, des cadres juridiques, des niveaux de publicité et des finalités différentes. La Russie fait de la guerre hybride et du destructif. La Chine fait de l'espionnage massif et du pré-positionnement. La DPRK vole des cryptomonnaies. L'Iran cible la région et les dissidents. Les États-Unis pratiquent le defend forward et le law enforcement. Israël fait de la préemption. Le Royaume-Uni fait de la disruption coordonnée. Comprendre ces différences doctrinales est une compétence analytique fondamentale — c'est l'objet des Parties II à V.

---

## PARTIE II — RUSSIE

*La Russie est l'acteur étatique le plus prolifique sur le plan destructif et le mieux documenté publiquement. Elle mérite 3 chapitres car elle déploie simultanément de l'espionnage stratégique furtif (SVR), des opérations destructrices et d'influence (GRU), et de la surveillance de l'étranger proche (FSB).*

---

### Chapitre 5 — Russie : contexte, doctrine et appareil cyber

#### 5.1 Priorités géopolitiques et doctrine

Les priorités nationales russes qui structurent les cyberopérations : maintien du statut de grande puissance, contrôle de l'« étranger proche » (ex-URSS), confrontation avec l'OTAN, préservation du régime interne. La doctrine cyber russe est intégrée à la « guerre hybride » (gibridnaya voyna) : information warfare + cyber + désinformation + opérations militaires + pression économique. Il n'y a pas de séparation nette entre espionnage et action — le renseignement collecté est utilisé pour des opérations d'influence (hack-and-leak) ou de sabotage (wipers).

#### 5.2 Structure organisationnelle

Le **SVR** (Service de renseignement extérieur) conduit l'espionnage stratégique de haut niveau — gouvernements, diplomatie, think tanks, grandes entreprises tech. Son style est la furtivité maximale, les opérations de long terme, et le tradecraft sophistiqué (supply chain, abus de services cloud). Groupes associés : APT29 / Cozy Bear / Midnight Blizzard.

Le **GRU** (Direction du renseignement militaire) conduit les opérations militaires cyber, le sabotage, et l'influence. Plus agressif et plus bruyant que le SVR. Trois unités identifiées : **Unit 26165** (APT28 / Fancy Bear — espionnage militaire et politique + influence), **Unit 74455** (Sandworm — opérations destructrices, sabotage OT/ICS, supply chain), et **Unit 29155** (identifiée en 2024 — WhisperGate, opérations déstabilisatrices en Ukraine).

Le **FSB** (Service fédéral de sécurité) conduit la sécurité intérieure, le contre-espionnage, et la surveillance des voisins proches. **Centre 16** : Turla / Snake — espionnage long terme ultra-sophistiqué contre des cibles gouvernementales. **Centre 18** : Gamaredon — ciblage massif de l'Ukraine avec un volume élevé et une sophistication moindre.

#### 5.3 L'écosystème cybercriminel comme zone grise

Les groupes ransomware russophones (LockBit, Conti, BlackBasta) opèrent sous une tolérance tacite de l'État tant qu'ils ne ciblent pas la CEI (Communauté des États Indépendants). La frontière entre tolérance et connivence est floue : certains opérateurs RaaS ont des liens documentés avec les services. Cette zone grise complique l'attribution (un ransomware qui touche un secteur stratégique est-il du cybercrime ou un acte étatique déguisé ?).

---

### Chapitre 6 — Russie : les groupes APT en détail

#### 6.1 APT29 / Cozy Bear / Midnight Blizzard (SVR)

**Mission :** espionnage stratégique de haut niveau — gouvernements occidentaux, diplomatie, think tanks, grandes entreprises technologiques. **TTP dominants :** supply chain (SolarWinds/SUNBURST — backdoor dans le build process), phishing OAuth ciblé (emails imitant des invitations de collaboration Microsoft Teams), abus Azure AD/M365 (manipulation de tokens SAML — GoldenSAML, exploitation OAuth), credential spray (Azure AD à grande échelle), malware custom sophistiqué (EnvyScout — dropper HTML, BoomBox — downloader, NativeZone — loader, FoggyWeb — backdoor ADFS). **OPSEC :** très élevé. Infrastructure compartimentée (chaque cible a sa propre infrastructure C2), C2 via services légitimes (Azure, AWS, Slack), minimal footprint (peu de fichiers déposés, exécution en mémoire). **Campagnes majeures :** SolarWinds (2020 — supply chain, ~18 000 organisations touchées, ~100 cibles activement exploitées), Microsoft corporate breach (2023-2024 — password spray → compromission des emails de dirigeants Microsoft), campagnes de phishing diplomatiques continues (ciblant les ambassades, les ministères des affaires étrangères en Europe).

#### 6.2 APT28 / Fancy Bear / Forest Blizzard (GRU Unit 26165)

**Mission :** espionnage militaire et politique + opérations d'influence. **TTP dominants :** spear-phishing (macros Word, faux portails de login OAuth), exploitation de vulnérabilités (0-days Outlook — CVE-2023-23397, exploitation de serveurs Exchange), credential harvesting (fausses pages de login, password spraying), outils custom (X-Tunnel, XAgent, Zebrocy), et Mimikatz pour le credential dumping. **OPSEC :** moyen à élevé — plus bruyant que le SVR. **Campagnes majeures :** DNC hack 2016 (vol et publication des emails → ingérence électorale), WADA 2016 (vol et publication de données anti-dopage), Bundestag 2015 (compromission du réseau du parlement allemand), campagnes anti-OTAN continues, exploitation CVE-2023-23397 Outlook (2023 — ciblage systématique des organisations européennes).

#### 6.3 Sandworm / Seashell Blizzard (GRU Unit 74455)

**Mission :** opérations destructrices et sabotage — le bras armé du cyber russe. **TTP dominants :** wipers (NotPetya, CaddyWiper, HermeticWiper, IsaacWiper), attaques OT/ICS (Industroyer/CrashOverride — manipulation directe des protocoles industriels IEC 104/IEC 61850), supply chain (M.E.Doc pour NotPetya), exploitation d'edge devices (Cyclops Blink — botnet sur routeurs ASUS/WatchGuard). **Particularité :** Sandworm est le seul groupe APT à avoir causé des pannes d'électricité confirmées par cyberattaque — Ukraine 2015 (BlackEnergy/KillDisk, 230 000 foyers, 6h) et 2016 (Industroyer, Kiev, 1h). En 2022, la tentative Industroyer2 a été déjouée par le CERT-UA et ESET. **Note :** WhisperGate (2022) est attribué à GRU Unit 29155, pas à Sandworm/Unit 74455. **Campagnes majeures :** NotPetya (2017 — wiper mondial, $10+ Mrd), Olympic Destroyer (2018 — false flags Lazarus), Ukraine 2022-présent (multiple wipers, tentative Industroyer2).

#### 6.4 Turla / Snake / Secret Blizzard (FSB Centre 16)

**Mission :** espionnage long terme contre des cibles gouvernementales et diplomatiques de haute valeur. **TTP :** malware ultra-sophistiqué (Snake — rootkit multi-plateforme actif depuis 2003, LightNeuron — backdoor Exchange, Kazuar — backdoor modulaire), infrastructure complexe (réseau de proxys par satellite pour masquer le C2), et technique unique de détournement d'infrastructure d'autres groupes APT (Turla a été observé en train de « pirater les pirates » — utiliser l'infrastructure de groupes iraniens pour mener ses propres opérations). Considéré comme l'un des groupes les plus techniquement avancés au monde. **Snake a été démantelé par le FBI en 2023** (opération Medusa — injection de commandes dans le malware pour le désactiver sur les machines infectées).

#### 6.5 Gamaredon / Aqua Blizzard (FSB Centre 18)

**Mission :** ciblage massif de l'Ukraine. **TTP :** volume élevé, sophistication moindre que les autres groupes russes — phishing de masse, templates VBA, infrastructure Telegram pour le C2, persistence agressive (réinfection rapide après éradication). Gamaredon est le « marteau » là où Turla est le « scalpel ».

---

### Chapitre 7 — Russie : campagnes de référence et influence

#### 7.1 SolarWinds / SUNBURST (2020)

La campagne de supply chain la plus sophistiquée documentée. L'APT29/SVR a compromis le processus de build de SolarWinds Orion, injecté la backdoor SUNBURST dans les mises à jour légitimes (versions 2019.4 HF 5 à 2020.2.1 HF 1), et touché ~18 000 organisations. Environ 100 cibles de haute valeur ont été activement exploitées (Trésor US, Département d'État, Commerce, Microsoft). Les TTP post-compromission incluaient le forgeage de tokens SAML (GoldenSAML) pour accéder à Azure AD/O365 sans credentials, et l'accès massif aux boîtes mail via Graph API. Signaux observables : requêtes DNS vers avsvmcloud[.]com avec sous-domaines encodés, processus fils inhabituels de SolarWinds.BusinessLayerHost.exe, événements ADFS anormaux. Leçons : la confiance dans un fournisseur ne dispense pas de monitorer son comportement réseau, le monitoring du plan de contrôle identity (SAML, OAuth) est devenu indispensable.

#### 7.2 NotPetya (2017)

Le wiper le plus destructeur de l'histoire. Distribué via une mise à jour piégée du logiciel comptable ukrainien M.E.Doc (supply chain). Se propageait via EternalBlue + Mimikatz. Ressemblait à un ransomware (demande de rançon affichée) mais était un wiper (la clé n'existait pas — false flag). Impact mondial non anticipé : Maersk (reconstruction complète du SI en 10 jours, 45 000 postes), Merck ($870M de pertes), FedEx/TNT ($400M), Saint-Gobain ($220M). Total : $10+ Mrd de dégâts mondiaux. Attribution à Sandworm/GRU par les Five Eyes en 2018. Contexte DIMEFIL : Military (appui au conflit Ukraine), Economic (déstabilisation économique).

#### 7.3 Industroyer (2016) — sabotage du réseau électrique

Industroyer/CrashOverride est le malware le plus avancé conçu pour cibler les systèmes de contrôle industriel (ICS). Il manipule directement les protocoles industriels (IEC 104, IEC 61850, OPC DA) pour envoyer des commandes aux automates de distribution électrique. Déployé par Sandworm contre le réseau électrique ukrainien le 17 décembre 2016, il a causé un blackout d'environ 1 heure dans la région de Kiev. L'analyse de ce malware et le traitement approfondi des attaques OT sont développés dans la Partie VI.

#### 7.4 Opérations d'influence russes

L'**Internet Research Agency** (IRA), basée à Saint-Pétersbourg, est la ferme à trolls qui a manipulé les réseaux sociaux US/UE avec des faux comptes, de la polarisation, et de la désinformation — active depuis au moins 2013. Le modèle russe combine cyberespionnage (le GRU vole les données — emails DNC), publication via des intermédiaires (DCLeaks, Guccifer 2.0, WikiLeaks), et amplification par l'IRA (faux comptes qui relaient et commentent). C'est l'approche intégrée espionnage + influence + désinformation la plus documentée au monde. L'ingérence dans les élections US 2016 reste le cas d'école : APT28/GRU a volé et publié les emails du DNC, l'IRA a amplifié les narratifs polarisants, et l'effet combiné a eu un impact mesurable sur le débat public.

#### 7.5 Fil rouge — BLACKOUT : comparaison avec les profils russes

> **⚡ BLACKOUT — Épisode 3**
>
> Camille (l'analyste CTI en charge) compare les TTP de BLACKOUT avec les profils russes. Les patterns de beaconing (intervalles de 32 minutes avec jitter de 10 %) sont similaires à ceux documentés par ESET sur Sandworm/CaddyWiper (2022). La victimologie (opérateur d'énergie européen) est cohérente avec le ciblage Sandworm. Le pivot vers l'OT est une signature Sandworm. Mais l'exploitation d'Ivanti et l'absence de malware custom sont atypiques pour Sandworm (qui utilise typiquement des outils custom — Industroyer, CaddyWiper). L'hypothèse Sandworm/GRU est posée comme H1 avec confiance modérée.

---

## PARTIE III — CHINE

*La Chine est l'acteur étatique le plus prolifique en volume d'espionnage et le plus stratégique dans son ciblage — avec une réorganisation majeure post-2015 qui a significativement augmenté sa sophistication.*

---

### Chapitre 8 — Chine : contexte, doctrine et appareil cyber

#### 8.1 Priorités géopolitiques

Le cyber est un instrument de la stratégie de puissance globale chinoise. Les priorités : rattrapage technologique (Made in China 2025 — atteindre l'autosuffisance dans les technologies clés : semi-conducteurs, IA, aérospatiale, biotechnologie), unification (Taïwan — le scénario géopolitique le plus déterminant pour les cyberopérations chinoises), contrôle interne (surveillance des dissidents, du Tibet, du Xinjiang, de Hong Kong), puissance régionale Indo-Pacifique (projection de puissance en mer de Chine, Routes de la Soie), et accumulation de données (collecte massive via le cyber-espionnage, les JV, et les programmes académiques).

#### 8.2 Structure

Le **MSS** (Ministère de la Sécurité d'État) est le service de renseignement civil — espionnage économique et technologique, avec des bureaux régionaux (le MSS Hainan est derrière APT40). Le **PLA** (Armée populaire de libération) a historiquement conduit le cyber-espionnage (Unit 61398 / APT1 exposé par Mandiant en 2013) mais a été réorganisé après 2015 (PLA Strategic Support Force — SSF). Les **contractors** et universités mandatés par le MSS ou le PLA conduisent des opérations pour le compte de l'État (le modèle chinois brouille la frontière public/privé).

La **réorganisation post-2015** est un tournant : après l'exposition publique d'APT1 (2013) et l'accord Obama-Xi de 2015 (engagement à ne plus mener d'espionnage économique — largement violé), la Chine a transféré la majorité des opérations du PLA vers le MSS, avec une montée en sophistication significative (meilleur OPSEC, tradecraft plus furtif, exploitation d'appliances edge plutôt que phishing basique).

---

### Chapitre 9 — Chine : les groupes APT en détail

**APT41 / Wicked Panda / Brass Typhoon (MSS)** — le groupe à double casquette : espionnage étatique (ciblage tech, santé, télécoms) + cybercrime personnel (gaming, ransomware). Les deux activités utilisent les mêmes outils et la même infrastructure. Indictments DOJ en 2020. TTP : supply chain (CCleaner), exploitation de vulnérabilités web, rootkits, backdoors sophistiquées.

**APT40 / Gingham Typhoon (MSS Hainan)** — espionnage maritime, défense, aérospatial, Asie-Pacifique. TTP signature : exploitation systématique et rapide des vulnérabilités sur les appliances réseau (VPN, firewalls) — souvent dans les 48h suivant la publication d'un advisory. Ciblage cohérent avec les intérêts maritimes chinois en mer de Chine.

**Volt Typhoon (PRC state-sponsored)** — le cas le plus inquiétant. Pré-positionnement dans les infrastructures critiques américaines (télécoms, énergie, eau, transport) avec LotL quasi exclusif. Pas d'exfiltration, pas de sabotage — un accès dormant maintenu pendant des mois/années. Signification stratégique : capacité de dissuasion/représailles en cas de conflit autour de Taïwan. Traité en profondeur au Ch.22 et Ch.31.

**Salt Typhoon (PRC state-sponsored)** — compromission d'opérateurs télécoms mondiaux (AT&T, Verizon, d'autres) pour accéder aux systèmes d'interception légale (wiretapping systems). Révélé fin 2024. Impact : accès potentiel aux communications ciblées par les autorités américaines elles-mêmes.

**APT10 / Stone Panda (MSS)** — ciblage des MSP (Managed Service Providers) via l'opération Cloud Hopper, donnant accès aux réseaux de centaines de clients dans des dizaines de pays. Indictments DOJ en 2018.

**APT31 / Zirconium (MSS)** — ciblage gouvernemental large (parlementaires, think tanks, dissidents). Indictments DOJ en 2024 ciblant 7 opérateurs MSS.

Acteurs associés : **Mustang Panda** (ciblage des ONG, think tanks, et gouvernements en Asie du Sud-Est), **Gallium** (télécoms), et le **Winnti umbrella** (écosystème de groupes utilisant des outils partagés, frontière floue entre espionnage étatique et cybercrime).

---

### Chapitre 10 — Chine : campagnes de référence et tendances

**Cloud Hopper (2016-2018)** : APT10 a compromis des MSP pour accéder aux réseaux de leurs clients — des centaines d'entreprises dans des dizaines de pays. L'attribution repose sur la victimologie (les données volées correspondent aux priorités stratégiques chinoises). Leçon : la supply chain de services (MSP, infogérants) est un vecteur de compromission massive.

**Microsoft Exchange / Hafnium (2021)** : exploitation de 4 vulnérabilités zero-day dans Exchange on-premise, touchant ~250 000 serveurs mondialement. L'exploitation a commencé de manière ciblée puis s'est massifiée — transition inhabituelle vers l'exploitation opportuniste.

**Volt Typhoon (2023-présent)** et **Salt Typhoon (2024)** sont traités respectivement au Ch.22/Ch.31 et dans ce chapitre. Salt Typhoon illustre une évolution : cibler non plus les données elles-mêmes mais les systèmes qui les collectent (les systèmes d'interception légale des opérateurs télécom).

**Tendances structurelles chinoises :** exploitation massive des appliances edge (Ivanti, Fortinet, Citrix, Barracuda — souvent dans les heures suivant la publication d'une CVE), LotL systématique (sophistication croissante de l'OPSEC post-réorganisation MSS), pré-positionnement stratégique dans les infras critiques, ciblage de la supply chain logicielle, et volume d'espionnage inchangé malgré les accords diplomatiques.

> **⚡ BLACKOUT — Épisode 4**
>
> L'exploitation Ivanti dans BLACKOUT est un TTP signature chinois (APT40, Volt Typhoon). Le LotL (pas de malware custom identifié, utilisation de certutil, PowerShell, et PsExec) est compatible avec le tradecraft Volt Typhoon. Le pré-positionnement OT sans action est compatible avec le modèle de « capacité dormante ». L'hypothèse chinoise (H2) est posée avec confiance faible à modérée — mais les patterns de beaconing ne correspondent pas aux profils chinois documentés.

---

## PARTIE IV — CORÉE DU NORD, IRAN ET AUTRES ACTEURS

---

### Chapitre 11 — DPRK : contexte, groupes et modèle unique

#### 11.1 Le cyber comme source de revenus

La DPRK est un cas unique : c'est le seul État qui utilise le cyber principalement comme source de revenus pour contourner les sanctions internationales. Le RGB (Reconnaissance General Bureau) est le service de renseignement militaire qui supervise les opérations cyber. Les opérateurs sont formés dans des programmes dédiés et souvent stationnés à l'étranger (Chine, Russie, Asie du Sud-Est) pour des raisons de connectivité et d'OPSEC.

**Lazarus Group / Diamond Sleet** : le plus polyvalent — vol de cryptomonnaies (Ronin Network $620M, Bybit ~$1,5 Mrd), supply chain (3CX 2023), social engineering sophistiqué sur LinkedIn (Opération Dream Job — fausses offres d'emploi ciblant les développeurs), et malware multi-plateforme (Windows, macOS, Linux). **APT38 / BlueNoroff / Sapphire Sleet** : spécialisation finance — braquages SWIFT (Bangladesh Bank 2016 — $81M), ciblage des exchanges de cryptomonnaies, et des protocoles DeFi. **Kimsuky / Emerald Sleet** : espionnage diplomatique et nucléaire — credential harvesting ciblant des chercheurs, diplomates, think tanks spécialisés sur la péninsule coréenne. **APT43 / Velvet Chollima** : ciblage académique et think tanks.

Les **opérateurs IT DPRK** sont un phénomène unique : des milliers de nord-coréens travaillent sous de fausses identités comme développeurs freelance dans des entreprises occidentales, générant des revenus (estimés à $300M+/an par le gouvernement US) qui financent le régime. Ils utilisent des identités volées, des VPN, et des intermédiaires pour masquer leur nationalité.

---

### Chapitre 12 — DPRK : campagnes de référence

**WannaCry (2017)** : ransomware worm exploitant EternalBlue, propagation mondiale (200 000+ systèmes dans 150 pays), NHS britannique paralysé. Attribution à Lazarus par la NSA, le GCHQ, et le FBI. Le ransomware a généré peu de revenus ($140 000 en Bitcoin) mais causé des milliards de dégâts. Leçon : la DPRK est prête à causer des dommages collatéraux massifs.

**Bangladesh Bank (2016)** : APT38 a compromis le terminal SWIFT de la banque centrale du Bangladesh et transféré $81M vers des comptes aux Philippines. $951M supplémentaires ont été bloqués grâce à une faute de frappe dans un ordre de virement (« fandation » au lieu de « foundation »). Premier braquage bancaire majeur par un acteur étatique via le cyber.

**3CX supply chain (2023)** : Lazarus a compromis la chaîne de build du logiciel de communication VoIP 3CX (600 000+ clients) — le supply chain d'un supply chain (la compromission initiale venait d'un logiciel de trading compromis). TTP similaires à SolarWinds mais avec un acteur différent.

**Vols de cryptomonnaies massifs** : Ronin Network $620M (2022), Harmony Bridge $100M (2022), Atomic Wallet $100M (2023), Bybit ~$1,5 Mrd (2025 — le vol de crypto le plus important de l'histoire, attribué par le FBI). Le cumul est estimé entre $3 et $6 Mrd. Ces fonds financent le programme nucléaire et balistique nord-coréen — le cyber comme arme de prolifération. Les mécanismes de blanchiment (mixeurs — Tornado Cash sanctionné par l'OFAC, ponts cross-chain, mules) évoluent en permanence.

---

### Chapitre 13 — Iran : contexte et groupes APT

Priorités : rivalités régionales (Golfe, Israël), surveillance des dissidents, sabotage ponctuel, influence chiite. Structure : MOIS/VAJA (renseignement civil — APT34, MuddyWater) et IRGC (Gardiens de la Révolution — APT33, APT35, APT42).

**APT33 / Peach Sandstorm (IRGC)** : énergie, aérospatial, pétrochimie. Password spraying massif, backdoors custom. **APT34 / OilRig / Hazel Sandstorm (MOIS)** : gouvernements Moyen-Orient, finance, énergie. DNS tunneling, webshells, credential harvesting. **APT35 / Charming Kitten / Mint Sandstorm (IRGC)** : social engineering ultra-ciblé — faux profils LinkedIn, impersonation de journalistes et d'universitaires, ciblage de chercheurs, dissidents, et opposants politiques. Le social engineering d'APT35 est considéré comme le plus sophistiqué au monde dans la catégorie « impersonation individuelle ». **APT42 / Calanque (IRGC-IO)** : surveillance ciblée, credential harvesting, opérations contre des cibles spécifiques de l'IRGC. **MuddyWater / Mango Sandstorm (MOIS)** : gouvernements et télécoms Moyen-Orient/Asie, PowerShell obfusqué, outils open source.

Le cyber iranien est croissant mais moins sophistiqué que la Russie et la Chine. Sa spécificité : les opérations destructives ponctuelles (wipers) comme substitut/complément aux opérations conventionnelles en période de tension régionale.

---

### Chapitre 14 — Iran : campagnes de référence

**Stuxnet (2010)** est traité ici sous l'angle du catalyseur : l'attaque US/Israël contre les centrifugeuses nucléaires iraniennes a détruit ~1 000 centrifugeuses et retardé le programme de 2-3 ans, mais elle a aussi catalysé le développement des capacités cyber iraniennes. L'Iran a répondu en investissant massivement dans son programme cyber offensif — Shamoon, développé 2 ans après Stuxnet, est la réponse iranienne. Stuxnet est aussi traité au Ch.18 (Israël) et au Ch.21 (OT/ICS).

**Shamoon v1/v2/v3 (2012-2018)** : wipers déployés contre Saudi Aramco (30 000 postes détruits en 2012 — l'un des incidents les plus destructeurs de l'histoire) et le secteur pétrolier. Attribution à APT33/Iran. Message : « si vous nous attaquez (Stuxnet), nous pouvons frapper votre industrie ».

**Opérations contre l'Albanie (2022)** : wipers et ransomware déployés contre les systèmes gouvernementaux albanais après que l'Albanie a hébergé un groupe d'opposition iranien (MEK). L'Albanie a rompu les relations diplomatiques avec l'Iran — premier cas de rupture diplomatique pour cause de cyberattaque.

---

### Chapitre 15 — Autres acteurs étatiques et zones grises

#### 15.1 Acteurs régionaux documentés

**Vietnam — OceanLotus / APT32** : espionnage régional (ASEAN, dissidents vietnamiens, entreprises), sophistication croissante, macOS et mobile. **Pakistan — SideCopy, Transparent Tribe** : ciblage quasi exclusif de l'Inde (gouvernement, défense). **Turquie — Sea Turtle** : détournement DNS ciblant le Moyen-Orient et l'Europe (registrars compromis). **Amérique latine — Blind Eagle / APT-C-36** : ciblage régional (Colombie, Équateur).

#### 15.2 Mercenaires cyber / PSO (Private Sector Offensive)

**NSO Group** (Israël — Pegasus) : spyware mobile exploitant des zero-days iOS/Android, vendu à des États pour la surveillance. Révélé par Citizen Lab et le consortium Pegasus Project (2021). Utilisé contre des journalistes, dissidents, opposants politiques, et même des chefs d'État. **Intellexa** (consortium européen — Predator) : concurrent de NSO, spyware similaire. **Candiru** (Israël) : spyware ciblant les navigateurs et les systèmes desktop.

Pourquoi la CTI les documente : leurs outils apparaissent dans les campagnes d'espionnage étatique — l'analyste qui identifie un spyware Pegasus sait que le commanditaire est un client étatique de NSO, pas un cybercriminel. Les régulations émergentes : Pall Mall Process, restrictions d'exportation, moratorium proposé par l'UE.

#### 15.3 Zones grises crime-État

APT41 (double casquette espionnage/cybercrime), groupes ransomware russophones (tolérance étatique), DPRK (le vol de crypto est du cybercrime par la méthode, de l'action étatique par la finalité), et les hacktivistes instrumentalisés (KillNet, NoName057(16) — hacktivisme pro-russe avec des liens possibles avec les services, IT Army of Ukraine — coordination étatique d'un mouvement de volontaires).

---

## PARTIE V — PUISSANCES CYBER OCCIDENTALES ET ALLIÉES

*Cette partie complète la cartographie des acteurs étatiques. L'objectif n'est pas de symétriser les menaces mais d'éviter un angle mort analytique : les cyberopérations sont un instrument de puissance utilisé par tous les États dotés. Comprendre les différences doctrinales entre blocs est une compétence analytique fondamentale.*

---

### Chapitre 16 — États-Unis : doctrine, agences et cyber power

L'appareil cyber américain est le plus puissant et le plus structuré au monde. **USCYBERCOM** (commandement militaire cyber — Cyber Mission Force, ~6 000 opérateurs, articulation avec les combatant commands) conduit les opérations offensives et défensives militaires. La **NSA** (National Security Agency — TAO/Tailored Access Operations) collecte du renseignement d'origine électromagnétique et cyber avec des capacités offensives majeures. La **CIA** (Central Intelligence Agency) dispose de capacités cyber clandestines intégrées au renseignement humain. Le **FBI** conduit les investigations cyber, les démantèlements d'infrastructure, et les poursuites judiciaires (indictments). **CISA** (Cybersecurity and Infrastructure Security Agency) coordonne la protection des infrastructures critiques et publie des advisories de référence.

La distinction fondamentale : le renseignement (NSA/CIA — collecte clandestine, pas d'attribution publique) est séparé de l'offensive militaire (USCYBERCOM — defend forward, disruption) et du law enforcement (FBI/DOJ — indictments publics, sanctions, naming and shaming).

**La doctrine du defend forward / persistent engagement** (Gen. Paul Nakasone, 2018) est un changement de paradigme : ne pas attendre l'attaque mais agir en continu dans les réseaux adverses pour dégrader leurs capacités. Le concept de « contestation permanente » signifie que USCYBERCOM opère quotidiennement dans les réseaux adverses, pas uniquement en réponse à une attaque.

**Opérations documentées :** Stuxnet (co-attribution US/Israël — sabotage du programme nucléaire iranien, traité au Ch.18 et Ch.21), démantèlement de botnets (Emotet 2021, Qakbot 2023 — coordination FBI/Europol), neutralisation de Snake/Turla (opération Medusa 2023 — FBI), advisories conjoints NSA/CISA/FBI attribuant des APT avec IoC et TTP (un outil de défense collective unique dans l'écosystème mondial), et opérations de « hunt forward » (USCYBERCOM déploie des équipes dans les réseaux de pays alliés pour détecter les menaces — Ukraine depuis 2018).

**L'utilisation du droit comme instrument :** indictments DOJ contre des opérateurs APT chinois (PLA Unit 61398 en 2014, MSS en 2018 et 2024), russes (GRU Unit 26165 en 2018 pour l'ingérence électorale), iraniens, et nord-coréens. L'effet dissuasif est débattu (les inculpés ne seront probablement jamais arrêtés) mais l'effet de naming and shaming est réel (il réduit la marge de déni plausible). Les sanctions ciblées OFAC complètent le dispositif.

---

### Chapitre 17 — Royaume-Uni et Five Eyes

**GCHQ** (Government Communications Headquarters) est l'agence de renseignement d'origine électromagnétique et cyber, partenaire étroit de la NSA. Le **NCSC** (National Cyber Security Centre, branche du GCHQ) est l'organisme de protection nationale — son modèle (publication d'advisories de haute qualité, collaboration directe avec le secteur privé, communication accessible) est une référence en Europe. La **National Cyber Force** (NCF, créée 2020) conduit les opérations offensives dédiées — capacités de disruption ciblée. **MI5** (sécurité intérieure, contre-espionnage) et **MI6/SIS** (renseignement extérieur) complètent l'écosystème.

L'alliance **Five Eyes** (US, UK, Canada, Australie, Nouvelle-Zélande) est le partage de renseignement cyber le plus intégré au monde : advisories conjoints, partage d'IoC et de TTP en quasi temps réel, coordination des attributions publiques. Le Royaume-Uni est souvent parmi les premiers à attribuer publiquement une opération étatique (NotPetya, SolarWinds, Volt Typhoon). Les opérations documentées incluent la disruption de botnets, les opérations d'influence contre Daesh (JTRIG), et le modèle de « disruption by design ».

---

### Chapitre 18 — Israël : cyber, renseignement et supériorité technologique

L'écosystème cyber israélien est unique par son intégration militaire-renseignement-privé. L'**Unité 8200** (renseignement d'origine électromagnétique et cyber de l'IDF — la « NSA israélienne ») est la pépinière de talents du secteur cyber israélien. Le **Mossad** conduit les opérations clandestines extérieures. Le **Shin Bet** gère la sécurité intérieure et la surveillance.

La doctrine de **préemption** appliquée au cyber : Israël considère le cyberespace comme un espace d'action permanent, pas une réponse à une agression. Le cas **Stuxnet** (co-attribution US/Israël) est fondateur : la première arme cyber conçue pour causer des dommages physiques — destruction de ~1 000 centrifugeuses nucléaires iraniennes à Natanz via la manipulation des automates Siemens. L'opération a retardé le programme iranien de 2-3 ans mais a aussi catalysé le développement des capacités cyber iraniennes (effet boomerang) et a posé la question de la prolifération des armes cyber (le code de Stuxnet a fuité et a été étudié par tous les acteurs étatiques). Stuxnet est aussi traité au Ch.14 (impact sur l'Iran) et au Ch.21 (OT/ICS).

Le pipeline **Unité 8200 → startups** : les vétérans fondent les entreprises de cybersécurité et de surveillance les plus avancées au monde. NSO Group (Pegasus), Intellexa (Predator), Candiru — le marché de la surveillance offensive comme produit d'exportation stratégique. Les controverses : usage documenté contre des journalistes, dissidents, opposants politiques, et même des chefs d'État (Pegasus Project 2021). Les tentatives de régulation (Pall Mall Process, restrictions d'exportation, inscription sur la Entity List US). La frontière floue entre sécurité nationale légitime et abus commercial est un enjeu de gouvernance mondiale.

---

### Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel

L'Ukraine est le laboratoire mondial de la cyberdéfense en temps de guerre. La transformation sous contrainte depuis 2014 (annexion de la Crimée, premières cyberattaques russes majeures — BlackEnergy 2015) jusqu'à l'invasion de 2022 a produit un retour d'expérience unique.

La **coopération sans précédent** avec les alliés et le secteur privé : Microsoft (Threat Intelligence Center — détection et neutralisation en quasi temps réel des malwares russes déployés en Ukraine), Google (TAG — Project Shield, protection DDoS), ESET (analyse de malware — Industroyer2 déjoué grâce à la collaboration CERT-UA/ESET), Amazon Web Services (migration d'urgence des données gouvernementales vers le cloud), Starlink (connectivité résiliente), et USCYBERCOM (opérations « hunt forward » — déploiement d'équipes américaines dans les réseaux ukrainiens pour détecter les menaces). Ce modèle de défense collaborative public-privé-international est sans précédent dans l'histoire du cyber.

L'usage **offensif/défensif** : le **CERT-UA** (Computer Emergency Response Team) a démontré des capacités de réponse sous le feu remarquables. Les opérations offensives ukrainiennes (cyberattaques documentées contre les systèmes logistiques et de communication russes, piratage de caméras de surveillance) sont partiellement publiques. L'**IT Army of Ukraine** est un mouvement coordonné de volontaires cyber internationaux (lancé via Telegram par le vice-premier ministre Mykhailo Fedorov) conduisant des opérations DDoS et de hacktivisme contre des cibles russes — zone grise entre hacktivisme et opération militaire.

Le **retour d'expérience** : la résilience numérique sous bombardement (migration cloud d'urgence, décentralisation des systèmes, backups distribués), l'efficacité relative des cyberattaques dans un conflit cinétique (le cyber seul ne gagne pas une guerre — les blackouts de 2022 ont été réparés en heures grâce à l'expérience accumulée depuis 2015), et les leçons pour les pays européens (la préparation, la résilience, et la coopération sont plus importantes que la capacité offensive).

---

## PARTIE VI — MENACES SUR LES INFRASTRUCTURES CRITIQUES ET L'OT

*Le ciblage des systèmes industriels est le scénario le plus critique — celui qui peut causer des dommages physiques. Il mérite un traitement dédié.*

---

### Chapitre 20 — APT et OT/ICS : pourquoi c'est différent

L'environnement OT (Operational Technology) a des spécificités qui changent radicalement la donne de la cybersécurité. Les **protocoles industriels** (IEC 104, IEC 61850, Modbus, DNP3, OPC) n'ont pas d'authentification native — si un attaquant atteint le réseau OT, il peut envoyer des commandes aux automates sans credential. La **convergence IT/OT** croissante (les postes d'ingénierie OT sont connectés au réseau IT pour la maintenance, la supervision, et les mises à jour) crée un chemin d'attaque du réseau bureautique vers les systèmes de contrôle. Les **systèmes hérités** (automates et systèmes de supervision avec 15-20 ans d'âge) ne sont souvent pas patchables et ne supportent pas les agents EDR. Et l'**impact physique** est le différenciateur fondamental : une attaque OT réussie peut provoquer des blackouts, des explosions, des contaminations, ou des accidents industriels.

Le modèle d'attaque OT typique : accès initial via IT (phishing, exploitation de VPN) → mouvement latéral dans le réseau IT → pivot vers OT via un poste d'ingénierie à double connexion (le « jump host ») → reconnaissance du réseau OT (identification des automates, des protocoles, de la topologie) → manipulation des automates (envoi de commandes via les protocoles industriels). L'ensemble prend des semaines à des mois — l'attaquant doit comprendre le processus industriel avant de pouvoir le manipuler.

---

### Chapitre 21 — Campagnes OT/ICS de référence

**Stuxnet (2010)** : la première arme cyber conçue pour causer des dommages physiques. Co-attribution US/Israël. Ciblage des centrifugeuses d'enrichissement d'uranium à Natanz (Iran). Le malware manipulait les automates Siemens S7-300 pour modifier la vitesse de rotation des centrifugeuses, causant leur destruction, tout en affichant des valeurs normales aux opérateurs (manipulation de l'affichage). ~1 000 centrifugeuses détruites, programme retardé de 2-3 ans. Stuxnet a démontré que le cyber peut causer des dommages physiques — il a ouvert l'ère des armes cyber OT.

**BlackEnergy / KillDisk — Ukraine 2015** : Sandworm a compromis 3 distributeurs d'électricité ukrainiens, coupant l'alimentation de ~230 000 foyers pendant 6 heures. Premier blackout confirmé causé par une cyberattaque. L'attaque a été conduite manuellement par des opérateurs qui prenaient le contrôle à distance des systèmes SCADA.

**Industroyer / CrashOverride — Ukraine 2016** : Sandworm a déployé un malware qui manipulait directement les protocoles industriels (IEC 104, IEC 61850, OPC DA) pour ouvrir des disjoncteurs dans un poste de transformation électrique à Kiev, causant un blackout d'~1 heure. C'est le premier malware conçu spécifiquement pour attaquer les systèmes de contrôle du réseau électrique via les protocoles natifs.

**Triton / TRISIS — Arabie Saoudite 2017** : le scénario le plus dangereux. Un attaquant (attribué à la Russie, via le Central Scientific Research Institute of Chemistry and Mechanics — TsNIIKhM) a ciblé les systèmes de sécurité SIS (Safety Instrumented Systems) d'une usine pétrochimique saoudienne — les systèmes dont la seule fonction est d'empêcher les accidents en arrêtant le processus en cas de paramètres dangereux. Désactiver les SIS AVANT de provoquer une condition dangereuse = un potentiel de dommages physiques catastrophiques (explosion, fuite toxique). L'attaque a échoué car le malware a provoqué un arrêt de sécurité non anticipé, révélant l'intrusion.

**Industroyer2 — Ukraine 2022** : tentative de blackout pendant l'invasion russe, déjouée par le CERT-UA et ESET grâce à une détection en quelques heures et une réponse coordonnée. Preuve que les capacités OT continuent d'être développées et déployées.

**Colonial Pipeline (2021)** : ransomware DarkSide sur le réseau IT de l'opérateur d'oléoduc. L'OT n'a pas été directement touché, mais l'opérateur a coupé l'OT par précaution — illustrant que la convergence IT/OT signifie qu'un incident IT peut paralyser l'OT même sans compromission directe.

---

### Chapitre 22 — Le pré-positionnement : la menace silencieuse

Le pré-positionnement est le maintien d'un accès dormant dans des infrastructures critiques, sans action immédiate, pour une utilisation future en cas de conflit. C'est le scénario le plus inquiétant pour les États car il transforme le cyberespace en un terrain de pré-conflit permanent.

**Volt Typhoon** est le cas d'école : depuis 2021 au moins (probablement plus tôt), des opérateurs liés à la Chine ont maintenu des accès dans des infrastructures critiques américaines (télécoms, énergie, eau, transport) en utilisant un LotL quasi exclusif (LOLBins, credentials légitimes, pas de malware custom). Aucune exfiltration, aucun sabotage — juste un accès maintenu pendant des mois/années. La signification stratégique est celle d'une **capacité de dissuasion/représailles** : « si vous intervenez militairement à Taïwan, nous pouvons frapper vos infrastructures critiques ».

La difficulté de détection est maximale : pas d'IoC (pas de malware custom à hasher), pas de traffic anormal (les communications utilisent les outils légitimes), et pas de comportement distinctif (les actions ressemblent à de l'administration normale). La détection repose entièrement sur les anomalies comportementales (un compte admin qui se connecte à un serveur inhabituel, un LOLBin exécuté dans un contexte anormal) et la corrélation multi-sources.

Les implications pour l'Europe : les opérateurs d'énergie, de télécom, et de transport européens sont des cibles potentielles de pré-positionnement — pas seulement par la Chine, mais aussi par la Russie (Sandworm a ciblé les infras critiques européennes dans le contexte du conflit ukrainien). La préparation passe par la visibilité (EDR sur les postes OT, monitoring réseau OT, segmentation IT/OT physique), la détection comportementale (pas de signatures), et la coordination avec les agences nationales (ANSSI, BSI, NCSC).

> **⚡ BLACKOUT — Épisode 5**
>
> BLACKOUT est un scénario de pré-positionnement classique : l'attaquant s'est positionné dans le réseau OT sans agir. Si c'est Sandworm, l'objectif est probablement le sabotage en cas d'escalade du conflit ukrainien. Si c'est Volt Typhoon ou un acteur similaire, l'objectif est la capacité de frappe en cas de conflit Indo-Pacifique. Si c'est un nouveau cluster, l'objectif est indéterminé. La réponse doit être immédiate (éradication + sécurisation OT) mais la compréhension de l'acteur oriente la priorisation et le signalement (ANSSI, OTAN, ISAC énergie).

---

## PARTIE VII — GÉOPOLITIQUE, ATTRIBUTION ET PROSPECTIVE

---

### Chapitre 23 — Attribution : méthodes, limites et enjeux

Ce que signifie « attribuer » dans le contexte APT : relier une activité observée à un acteur (technique), un service (opérationnel), et un État (stratégique). Les 3 niveaux ont des seuils de preuve croissants. Les évidences d'attribution (TTP/tradecraft, infrastructure, malware, victimologie, timing géopolitique, renseignement humain/technique). Les pièges (false flags — Olympic Destroyer avec des fragments Lazarus plantés par le GRU ; outils partagés — Cobalt Strike utilisé par tout le monde ; infrastructure louée — VPS partagés ; biais géopolitiques — attribuer à la Russie « par défaut » parce que le contexte le rend plausible). Les niveaux de confiance (high, moderate, low — jamais « certain »). L'attribution publique par les gouvernements (naming and shaming, indictments DOJ — outil diplomatique autant que sécuritaire). Le cours CTI (bibliothèque) enseigne la méthode d'attribution en profondeur ; le cours APT fournit les données sur les acteurs qui la rendent possible.

> **⚡ BLACKOUT — Épisode 6**
>
> Processus d'attribution : matrice ACH avec 4 hypothèses (H1 Sandworm/GRU, H2 Volt Typhoon/Chine, H3 nouveau cluster étatique, H4 acteur non étatique). Évidences : beaconing compatible Sandworm (C pour H1, I pour H2), exploitation Ivanti compatible Chine (C pour H2, C pour H1 — Ivanti est exploité par les deux), LotL (C pour H2, I partiel pour H1 — Sandworm utilise typiquement des outils custom), victimologie énergie Europe (C pour H1, C pour H2), pas de malware custom identifié (I pour H1, C pour H2). Résultat : H1 et H2 restent plausibles, H4 est éliminée. Conclusion : confiance modérée pour H1 (Sandworm/GRU), confiance faible pour H2. Indicateurs de révision : si un outil custom Sandworm est identifié → H1 renforcée ; si un pattern d'infrastructure chinoise est trouvé → H2 renforcée.

---

### Chapitre 24 — L'écosystème cyber offensif mondial

Vision d'ensemble : plusieurs centaines de groupes APT sont suivis par les vendors CTI mondiaux. La **prolifération** des capacités est la tendance la plus préoccupante : les outils et techniques autrefois réservés aux acteurs les plus sophistiqués sont maintenant accessibles (Cobalt Strike cracké, Brute Ratel commercialisé, frameworks C2 open source — Sliver, Havoc, Mythic). L'économie de la surveillance privée (NSO, Intellexa) est un marché d'armement cyber qui vend des capacités étatiques à des États qui n'auraient pas pu les développer seuls.

**Lecture comparative des doctrines :** la Russie pratique la guerre hybride intégrée (espionnage + destruction + influence) ; la Chine pratique l'espionnage de masse et le pré-positionnement stratégique ; la DPRK pratique le financement du régime par le cybervol ; l'Iran pratique le ciblage régional et le destructif ponctuel ; les États-Unis pratiquent le defend forward et le law enforcement ; Israël pratique la préemption et la supériorité technologique ; le Royaume-Uni pratique la disruption coordonnée avec les Five Eyes. Ces doctrines reflètent les priorités stratégiques, les cultures bureaucratiques, et les cadres juridiques de chaque État.

---

### Chapitre 25 — Géopolitique des normes cyber, droit international et cadre français

#### 25.1 Le droit international appliqué au cyberespace

Le processus de **Tallinn** (manuel rédigé par des experts, non contraignant mais référence académique) a posé les bases de l'application du droit international au cyberespace — les États sont responsables des cyberopérations qu'ils conduisent ou tolèrent, et les principes de souveraineté, de non-intervention, et de proportionnalité s'appliquent. Le **GGE** (Group of Governmental Experts) et l'**OEWG** (Open-Ended Working Group) à l'ONU négocient les normes de comportement responsable des États dans le cyberespace — avec des positions divergentes entre le bloc occidental (normes existantes suffisantes, à appliquer) et le bloc Russie/Chine (nouveau traité nécessaire, avec une définition de « sécurité de l'information » qui couvre aussi le contenu — contrôle de l'internet).

#### 25.2 Attributions publiques et sanctions

Les attributions publiques par les Five Eyes, l'UE, et l'OTAN sont devenues un instrument diplomatique régulier (NotPetya 2018, SolarWinds 2021, Volt Typhoon 2024). Leur effet : réduction de la marge de déni plausible, signal de capacité de détection, et pression diplomatique. Les **indictments DOJ** (poursuites criminelles américaines) ont un effet de naming and shaming même si les inculpés ne seront probablement jamais jugés. L'**EU Cyber Sanctions Regime** (depuis 2019) permet des sanctions ciblées (gel des avoirs, interdiction de voyager) contre des personnes et entités impliquées dans des cyberattaques.

#### 25.3 Le cadre français et européen

**La France** dispose d'un appareil cyber structuré et croissant. L'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information, rattachée au SGDSN) protège les OIV et les entités essentielles NIS 2, publie des advisories de référence, qualifie les prestataires (PASSI, PDIS, SecNumCloud), et conduit les investigations sur les incidents d'envergure nationale. Le **COMCYBER** (Commandement de la cyberdéfense, ministère des Armées) conduit les opérations militaires cyber — la France a officialisé sa doctrine de **lutte informatique offensive (LIO)** en 2019 (revue stratégique de cyberdéfense) : la France se réserve le droit de mener des opérations offensives dans le cyberespace en réponse à une agression. La **lutte informatique défensive (LID)** et la **lutte informatique d'influence (L2I)** complètent le dispositif. La **DGSE** et la **DGSI** contribuent au renseignement cyber. Le **C4** (Centre de Coordination des Crises Cyber, créé 2022) coordonne la réponse aux crises cyber majeures.

Au niveau européen, l'**ENISA** coordonne la cybersécurité entre les États membres. La directive **NIS 2** (2024) étend les obligations de cybersécurité à un périmètre beaucoup plus large d'entités. L'**EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d'urgence. Et l'**OTAN** a reconnu le cyberespace comme 5ème domaine d'opérations (Varsovie 2016) et intègre le cyber dans sa planification de défense collective (un cyberattaque peut déclencher l'article 5 — même si le seuil n'a jamais été formellement défini).

---

### Chapitre 26 — Tendances 2024-2026 et signaux d'anticipation

**Exploitation massive des appliances edge** : les VPN, firewalls, et passerelles exposés sont le vecteur n°1 des acteurs étatiques sophistiqués (Ivanti, Fortinet, Citrix, Barracuda — souvent exploités dans les heures suivant la publication d'un advisory). **Ciblage de l'identité cloud** : Azure AD/Entra ID, tokens SAML/OAuth, MFA bypass (AitM), SSO compromise — l'identité est le nouveau périmètre. **Convergence crime-État** : les frontières s'estompent (APT41, ransomware russophones tolérés, DPRK). **LotL comme standard** : Volt Typhoon a démontré qu'une opération étatique sophistiquée peut être conduite sans aucun malware custom. **IA offensive** : phishing amélioré par LLM, deepfakes vocaux pour le social engineering, aide au développement de malware — impact croissant mais pas encore transformatif. **Pré-positionnement dans les infras critiques** : la menace structurelle qui définira la prochaine décennie.

Les signaux géopolitiques à surveiller : tensions Taïwan → pré-positionnement chinois accru, escalade Ukraine → destructif russe contre les alliés, élections → influence, sanctions → espionnage/vol, crise énergétique → ciblage énergie.

---

### Chapitre 27 — Construire une défense APT-ready

Ce chapitre n'est pas un cours de SOC ou d'IR (voir les cours dédiés) — c'est une synthèse des principes de défense spécifiques aux APT. Les **contrôles minimum viables** (MFA résistant au phishing — P0, PAM — P0, EDR partout y compris serveurs — P0, patching edge devices < 48h — P0, segmentation réseau — P1, durcissement AD — P1, monitoring cloud/identity — P1, backup hors ligne testé — P1, plan IR formalisé — P1). La **visibilité minimum viable** : Sysmon, PowerShell ScriptBlock, DNS, auth logs, Azure AD, firewall/proxy, EDR, email gateway — sans ces sources, l'APT est invisible. La **détection TTP-driven** : détecter les comportements, pas les IoC (renvoi cours SOC). Le **containment APT** : scope AVANT de contenir (identifier TOUS les systèmes compromis, sinon l'attaquant active ses accès redondants), containment coordonné et simultané (pas séquentiel), et monitoring renforcé post-éradication (l'attaquant essaiera de revenir). Le **purple team orienté APT** : simuler les TTP des acteurs pertinents avec Atomic Red Team (renvoi cours SOC Ch.30).

---

### Chapitre 28 — Exercices de simulation

**Tabletop 1 — « APT29 a compromis votre Azure AD via phishing OAuth » :** scénario de 2h avec injections progressives (J0 : alerte sign-in suspect → J+1 : règle de forwarding détectée → J+3 : exfiltration SharePoint → J+5 : découverte de tokens SAML forgés). Questions clés : quand escaladez-vous ? qui informez-vous ? contenez-vous immédiatement ou scopez-vous d'abord ?

**Tabletop 2 — « Ransomware BlackBasta avec précurseur APT » :** discrimination APT vs cybercrime — l'investigation révèle que l'accès initial a été vendu par un IAB qui l'avait acheté à un acteur étatique. Implications pour la réponse, la notification, et l'attribution.

**Tabletop 3 — « Pré-positionnement OT détecté sans action destructive » :** l'attaquant est dans le réseau SCADA mais n'a rien fait. Éradiquez-vous immédiatement (risque de perdre le renseignement) ou surveillez-vous pour comprendre ses intentions (risque de laisser une menace active) ? Le dilemme fondamental du pré-positionnement.

---

## PARTIE VIII — ÉTUDES DE CAS INTÉGRÉES

*4 cas complets représentant 4 paradigmes et 3 blocs d'acteurs différents : supply chain (Russie), financement (DPRK), pré-positionnement (Chine), et investigation multi-hypothèses (fil rouge).*

---

### Chapitre 29 — SolarWinds/SUNBURST : la supply chain comme vecteur d'espionnage

Le paradigme de l'espionnage via supply chain — le cas le plus sophistiqué documenté publiquement.

**Acteur :** APT29 / Cozy Bear / Midnight Blizzard (SVR). **Attribution publique :** NSA, FBI, CISA, Five Eyes (janvier 2021). Confiance : élevée.

**Timeline complète :** septembre-octobre 2019 — activité suspecte dans l'environnement SolarWinds, modifications de « test » dans le code Orion. Février-mars 2020 — la backdoor SUNBURST est injectée dans les builds opérationnels. Mars 2020 — la mise à jour trojanisée est distribuée à ~18 000 organisations. Mars-décembre 2020 — APT29 sélectionne ~100 cibles de haute valeur (Trésor US, Commerce, Homeland Security, Microsoft, FireEye) et déploie des outils supplémentaires (TEARDROP, RAINDROP, GoldMax). Décembre 2020 — FireEye/Mandiant détecte l'intrusion en enquêtant sur le vol de ses propres outils Red Team. Divulgation publique.

**TTP détaillées :** Supply Chain Compromise (T1195.002), Signed Binary Proxy Execution (T1218 — le malware exécuté comme composant légitime d'Orion, signé numériquement), Masquerading (T1036 — C2 via DNS camouflé en requêtes Orion Improvement Program), Application Layer Protocol (T1071 — C2 HTTPS), Account Discovery (T1087), Use Alternate Authentication Material (T1550 — GoldenSAML pour forger des tokens SAML et accéder à Azure AD/O365 sans credentials), Email Collection (T1114 — accès aux boîtes mail via Graph API), Exfiltration Over C2 (T1041).

**Leçons :** la supply chain logicielle est un vecteur APT majeur, le monitoring du plan de contrôle identity (SAML, OAuth, tokens) est indispensable, l'intégrité du build pipeline est un enjeu stratégique, et Zero Trust s'impose (la confiance implicite dans un fournisseur ne protège pas).

---

### Chapitre 30 — Lazarus et l'empire crypto de la DPRK

Le paradigme unique du financement étatique par le cybervol — le seul cas dans l'histoire où un État finance sa survie et son programme d'armement par le vol de cryptomonnaies.

**Acteur :** Lazarus Group / Diamond Sleet et sous-groupes (APT38/BlueNoroff). **Attribution publique :** FBI, DOJ, Treasury/OFAC (multiples entre 2018 et 2025). Confiance : élevée.

**Chronologie des vols majeurs :** Bangladesh Bank 2016 ($81M, SWIFT), échanges de crypto 2017-2021 (centaines de millions cumulés), Ronin Network 2022 ($620M, bridge Ethereum), Harmony Bridge 2022 ($100M), Atomic Wallet 2023 ($100M), et Bybit 2025 (~$1,5 Mrd — le vol de crypto le plus important de l'histoire, attribué par le FBI). Le cumul est estimé entre $3 et $6 Mrd.

**Le pipeline complet :** accès initial (social engineering LinkedIn — fausses offres d'emploi ciblant les développeurs et les employés d'exchanges ; supply chain — 3CX ; exploitation de vulnérabilités DeFi) → compromission des clés privées ou des systèmes de signature → transfert des fonds → blanchiment (mixeurs — Tornado Cash sanctionné par l'OFAC en 2022, ponts cross-chain, conversion via des exchanges à KYC faible, mules, et OTC desks en Chine).

**L'impact géopolitique :** ces fonds financent directement le programme nucléaire et balistique nord-coréen — le cyber est une arme de prolifération. Le ROI est extraordinaire : le coût d'une opération de vol de crypto est de quelques centaines de milliers de dollars ; le revenu peut être de centaines de millions à plus d'un milliard. C'est le retour sur investissement le plus élevé de l'histoire du renseignement.

**Contexte DIMEFIL :** Financial (contournement de sanctions, financement du régime), Economic (substitut aux exportations légales bloquées par les sanctions).

---

### Chapitre 31 — Volt Typhoon : le pré-positionnement stratégique

Le paradigme du pré-positionnement sans action — la menace la plus difficile à détecter et la plus lourde de conséquences.

**Acteur :** PRC state-sponsored (évalué comme PLA ou affilié, nommé Volt Typhoon par Microsoft). **Attribution publique :** advisory conjoint NSA/CISA/FBI + Five Eyes (mai 2023, réitéré en 2024). Confiance : élevée.

**Timeline :** au moins depuis mi-2021, probablement plus tôt. Les accès ont été découverts dans des opérateurs de télécoms, des fournisseurs d'énergie, des systèmes d'eau, et des infrastructures de transport aux États-Unis et dans les territoires du Pacifique (Guam).

**TTP :** exploitation d'appliances edge (routeurs SOHO, VPN, firewalls — exploitation de vulnérabilités connues sur des équipements non patchés), LotL quasi exclusif (PowerShell, WMI, net.exe, ntdsutil — aucun malware custom identifié), credentials légitimes (comptes admin compromis via credential dumping), et maintien d'accès long terme sans action visible. Les communications C2 transitent par des routeurs SOHO compromis (botnets de routeurs domestiques) — ce qui rend la détection réseau extrêmement difficile car le trafic semble provenir de localisations résidentielles légitimes.

**Signification stratégique :** Volt Typhoon est interprété par la communauté de renseignement américaine comme une capacité de dissuasion/représailles chinoise liée au scénario Taïwan. Le message : « si vous intervenez militairement, nous pouvons frapper vos infrastructures critiques ». C'est la menace qui définira la prochaine décennie en géopolitique cyber.

**Leçons :** la menace la plus dangereuse est celle qui ne fait rien — comment détecter ce qui ressemble à de l'activité normale (pas d'IoC, pas de malware, des LOLBins et des credentials légitimes). La réponse : monitoring comportemental, baseline des activités admin, corrélation multi-sources, et collaboration avec les agences nationales.

---

### Chapitre 32 — Synthèse BLACKOUT : attribution et réponse face à l'incertitude

Synthèse du fil rouge sous forme de cas autonome — de la détection à la réponse, en passant par l'attribution.

**Détection (J+42) :** l'EDR détecte un comportement anormal sur un poste d'ingénierie OT — rundll32 avec DLL non signée et beaconing HTTPS régulier. Le CERT remonte la chaîne.

**Investigation :** reconstitution de la timeline (exploitation Ivanti J0, persistence J+3, Kerberoasting J+5, mouvement latéral J+8, pivot OT J+15, inactivité J+30 à J+42). Collecte des artefacts (logs Sysmon, Event Logs AD, captures réseau, dump mémoire du poste OT). Analyse des TTP (mapping ATT&CK complet).

**Attribution :** matrice ACH avec 4 hypothèses. H1 : Sandworm/GRU (beaconing compatible, ciblage énergie compatible, contexte géopolitique cohérent — mais pas de malware custom Sandworm, exploitation Ivanti atypique → confiance modérée). H2 : Volt Typhoon ou acteur chinois similaire (exploitation Ivanti signature, LotL, pré-positionnement sans action — mais beaconing non compatible avec les profils chinois documentés → confiance faible). H3 : nouveau cluster étatique non attribué (possible, non réfutable → confiance faible). H4 : acteur non étatique sophistiqué (très peu probable — le ciblage OT sans monétisation élimine le cybecrime → éliminée). Conclusion : confiance modérée pour H1, indicateurs de révision identifiés.

**Réponse :** éradication de tous les accès (persistence, comptes backdoor, modifications AD), sécurisation du réseau OT (segmentation physique IT/OT renforcée, déploiement Sysmon/EDR sur les postes d'ingénierie OT, monitoring réseau OT dédié), signalement ANSSI (l'opérateur est OIV — notification obligatoire NIS 2), partage ISAC énergie européen (TLP:AMBER — IoC et TTP partagés → 2 autres opérateurs confirment des activités similaires), et monitoring renforcé post-éradication (l'attaquant essaiera probablement de revenir).

**La leçon centrale :** comprendre les acteurs est indispensable pour répondre. Sans la connaissance des profils APT par pays, l'analyste face à BLACKOUT ne sait pas interpréter le pré-positionnement OT (sabotage futur ? capacité de dissuasion ? reconnaissance ?), ne sait pas calibrer l'urgence de la réponse (un acteur qui prépare un sabotage nécessite une éradication immédiate ; un acteur en pré-positionnement stratégique peut justifier une phase de surveillance contrôlée), et ne sait pas qui alerter (le signalement ANSSI déclenche des processus différents selon que l'acteur est russe, chinois, ou inconnu). Un SOC ou un IR sans connaissance des APT est aveugle — c'est la raison d'être de ce cours.

---

## ANNEXES

---

### Annexe A — Glossaire APT/CTI

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — technique analytique structurée |
| **APT** | Advanced Persistent Threat — acteur étatique sophistiqué et persistant |
| **ATT&CK** | Framework MITRE des tactiques, techniques et procédures adverses |
| **Attribution** | Processus de liaison d'une activité malveillante à un acteur/État |
| **Beaconing** | Communication périodique entre un implant et son C2 |
| **C2** | Command and Control — infrastructure de commande d'un implant |
| **Campaign** | Série d'intrusions liées par un objectif/période/infrastructure |
| **Cluster** | Regroupement d'activités non attribué à un acteur connu |
| **COMCYBER** | Commandement de la cyberdéfense français |
| **Defend forward** | Doctrine US de contestation permanente dans les réseaux adverses |
| **DIMEFIL** | Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement |
| **DLL sideloading** | Chargement d'une DLL malveillante via un exécutable légitime |
| **Domain fronting** | Masquage du C2 réel via un CDN légitime |
| **Dwell time** | Temps entre compromission et détection |
| **Edge device** | Appliance réseau exposée (VPN, firewall, passerelle) |
| **False flag** | Indices plantés pour brouiller l'attribution |
| **Five Eyes** | Alliance de renseignement US/UK/Canada/Australie/Nouvelle-Zélande |
| **Foothold** | Point d'ancrage initial dans le réseau victime |
| **FSB** | Service fédéral de sécurité russe (sécurité intérieure) |
| **GoldenSAML** | Forgeage de tokens SAML pour accéder à Azure AD sans credentials |
| **GRU** | Direction du renseignement militaire russe |
| **Hacktiviste** | Acteur motivé par l'idéologie, pas par l'État ou le profit |
| **Hunt forward** | Déploiement d'équipes cyber dans les réseaux de pays alliés |
| **ICS** | Industrial Control Systems — systèmes de contrôle industriel |
| **Indictment** | Mise en accusation formelle (DOJ US) d'opérateurs APT |
| **Intrusion set** | Ensemble d'activités regroupées par TTP/infrastructure/victimologie |
| **IoA** | Indicator of Attack — signal comportemental d'attaque en cours |
| **IoC** | Indicator of Compromise — artefact technique d'une compromission |
| **Kill Chain** | Modèle Lockheed Martin des phases d'une intrusion |
| **LID** | Lutte informatique défensive (doctrine française) |
| **LIO** | Lutte informatique offensive (doctrine française) |
| **L2I** | Lutte informatique d'influence (doctrine française) |
| **LOLBin** | Living Off the Land Binary — outil système légitime détourné |
| **LotL** | Living off the Land — utilisation d'outils légitimes pour éviter la détection |
| **MSS** | Ministry of State Security — renseignement chinois |
| **OT** | Operational Technology — systèmes industriels |
| **PLA** | People's Liberation Army — armée chinoise |
| **Pré-positionnement** | Accès dormant dans une infra critique pour usage futur |
| **PSO** | Private Sector Offensive — entreprise de surveillance cyber commerciale |
| **Pyramid of Pain** | Hiérarchie des indicateurs par coût pour l'attaquant |
| **RGB** | Reconnaissance General Bureau — renseignement nord-coréen |
| **SCADA** | Supervisory Control and Data Acquisition — supervision industrielle |
| **SIS** | Safety Instrumented Systems — systèmes de sécurité industrielle |
| **Supply chain** | Compromission via un fournisseur de confiance |
| **SVR** | Service de renseignement extérieur russe |
| **Tabletop** | Exercice de simulation sur table d'un scénario d'incident |
| **Tradecraft** | Savoir-faire opérationnel global de l'attaquant |
| **TTP** | Tactics, Techniques, and Procedures |
| **USCYBERCOM** | United States Cyber Command |
| **Wiper** | Malware destructeur qui efface les données |
| **Zero Trust** | Architecture qui ne fait confiance à aucun flux par défaut |

---

### Annexe B — Groupes APT majeurs par pays

*La colonne « Statut d'attribution » indique le niveau de publicité et de confiance de l'attribution — un rappel que tout n'a pas le même statut probatoire.*

| Pays | Groupe (Mandiant) | CrowdStrike | Microsoft | Service | Cibles | Statut d'attribution |
|------|-------------------|-------------|-----------|---------|--------|---------------------|
| Russie | APT28 | Fancy Bear | Forest Blizzard | GRU Unit 26165 | OTAN, gouvernements, défense, médias | **Publiquement attribué** (indictment DOJ 2018, Five Eyes) |
| Russie | APT29 | Cozy Bear | Midnight Blizzard | SVR | Gouvernements, tech, think tanks | **Publiquement attribué** (Five Eyes, advisory SolarWinds 2021) |
| Russie | Sandworm | Voodoo Bear | Seashell Blizzard | GRU Unit 74455 | Ukraine, énergie, OT/ICS | **Publiquement attribué** (indictment DOJ 2020, Five Eyes) |
| Russie | Turla | Venomous Bear | Secret Blizzard | FSB Centre 16 | Gouvernements, diplomatie | **Publiquement attribué** (DOJ opération Medusa 2023) |
| Russie | Gamaredon | — | Aqua Blizzard | FSB Centre 18 | Ukraine (volume) | **Largement suspecté** (pas d'indictment formel) |
| Chine | APT41 | Wicked Panda | Brass Typhoon | MSS | Tech, santé, gaming + cybercrime | **Publiquement attribué** (indictment DOJ 2020) |
| Chine | APT40 | — | Gingham Typhoon | MSS Hainan | Maritime, défense, Asie-Pacifique | **Publiquement attribué** (advisory Five Eyes 2024) |
| Chine | APT10 | — | — | MSS | MSP (Cloud Hopper), tech | **Publiquement attribué** (indictment DOJ 2018) |
| Chine | Volt Typhoon | — | Volt Typhoon | PRC (évalué PLA) | Infras critiques US, prépositionnement | **Publiquement attribué** (advisory NSA/CISA/FBI + Five Eyes 2023) |
| Chine | Salt Typhoon | — | Salt Typhoon | PRC | Télécoms mondiales | **Attribué par gouvernements alliés** (advisory 2024) |
| Chine | APT31 | — | Violet Typhoon | MSS | Gouvernements, think tanks | **Publiquement attribué** (indictment DOJ 2024) |
| DPRK | Lazarus | Labyrinth Chollima | Diamond Sleet | RGB | Finance, crypto, défense, tech | **Publiquement attribué** (FBI, DOJ, Treasury — multiple) |
| DPRK | APT38 | — | Sapphire Sleet | RGB | Finance (SWIFT, crypto) | **Publiquement attribué** (FBI 2018) |
| DPRK | Kimsuky | Velvet Chollima | Emerald Sleet | RGB | Think tanks, diplomatique, nucléaire | **Largement suspecté** (advisory NSA/FBI 2023) |
| Iran | APT33 | Elfin | Peach Sandstorm | IRGC | Énergie, aérospatial, défense | **Largement suspecté** (attributions vendors, pas d'indictment) |
| Iran | APT34 | Helix Kitten | Hazel Sandstorm | MOIS | Gouvernement, finance MO | **Largement suspecté** (attributions vendors) |
| Iran | APT35 | Charming Kitten | Mint Sandstorm | IRGC | Chercheurs, dissidents, journalistes | **Publiquement attribué** (indictment DOJ 2022) |
| Iran | APT42 | — | Calanque | IRGC-IO | Surveillance ciblée | **Attribué par vendors** (Mandiant 2022) |
| Iran | MuddyWater | — | Mango Sandstorm | MOIS | Gouvernements MO, télécom | **Publiquement attribué** (advisory USCYBERCOM 2022) |

**Légende des statuts d'attribution :**
- **Publiquement attribué** : indictment DOJ, advisory gouvernemental signé (NSA/CISA/FBI, Five Eyes), ou attribution officielle par un État
- **Attribué par gouvernements alliés** : advisory ou déclaration publique de gouvernements sans indictment formel
- **Attribué par vendors** : attribution par un ou plusieurs éditeurs CTI (Mandiant, CrowdStrike, Microsoft) sans confirmation gouvernementale
- **Largement suspecté** : consensus de la communauté CTI sans attribution publique formelle
- **Cluster non attribué** : activité observée regroupée analytiquement sans attribution à un acteur connu

---

### Annexe C — Conventions de nommage comparées

| Vendor | Convention | Exemples |
|--------|-----------|----------|
| **Mandiant** | APT + numéro (attribué), UNC + numéro (non attribué) | APT28, APT41, UNC2452 |
| **CrowdStrike** | Animal par pays : Bear (Russie), Panda (Chine), Chollima (DPRK), Kitten (Iran), Spider (cybercrime), Jackal (hacktivisme) | Fancy Bear, Wicked Panda, Labyrinth Chollima |
| **Microsoft** | Météo : Blizzard (Russie), Typhoon (Chine), Sleet (DPRK), Sandstorm (Iran), Tempest (cybecrime), Storm (non attribué) | Forest Blizzard, Volt Typhoon, Diamond Sleet |
| **Kaspersky** | Noms descriptifs ou de projets | Equation Group, DarkHotel, Turla |
| **ESET** | Noms propres ou code | Sednit (APT28), Turla, Winnti |
| **Secureworks** | Couleur + animal par motivation : Iron (state), Gold (financial), Cobalt (threat) | Iron Twilight, Gold Melody |

---

### Annexe D — Timeline des cyberattaques étatiques majeures (2007-2026)

| Année | Opération | Attaquant | Type | Impact |
|-------|-----------|-----------|------|--------|
| 2007 | Cyberattaques Estonie | Russie (présumé) | DDoS massif | Premier cas massif et médiatisé |
| 2010 | Stuxnet | USA/Israël | Sabotage OT | Destruction centrifugeuses nucléaires Iran |
| 2012 | Shamoon v1 | Iran (APT33) | Wiper | 30 000 postes Saudi Aramco détruits |
| 2013 | Rapport APT1 | Chine (PLA) | Espionnage | Première attribution publique à une unité militaire |
| 2014 | Sony Pictures | DPRK (Lazarus) | Destructif + leak | Représailles pour un film |
| 2015 | BlackEnergy (Ukraine) | Russie (Sandworm) | Sabotage OT | Premier blackout par cyberattaque (230k foyers) |
| 2016 | Industroyer (Ukraine) | Russie (Sandworm) | Sabotage OT | Blackout Kiev (1h) |
| 2016 | Ingérence US 2016 | Russie (GRU + IRA) | Hack-and-leak + influence | Impact électoral |
| 2016 | Bangladesh Bank | DPRK (APT38) | Vol SWIFT | $81M volés |
| 2017 | WannaCry | DPRK (Lazarus) | Ransomware worm | 200 000+ systèmes, 150 pays |
| 2017 | NotPetya | Russie (Sandworm) | Wiper (false flag ransomware) | $10+ Mrd dégâts mondiaux |
| 2017 | Triton/TRISIS | Russie (TsNIIKhM) | Ciblage SIS industriel | Usine pétrochimique Arabie Saoudite |
| 2020 | SolarWinds/SUNBURST | Russie (APT29/SVR) | Supply chain | ~18 000 orgs touchées, ~100 exploitées |
| 2021 | Exchange/Hafnium | Chine | Espionnage | 250 000 serveurs vulnérables |
| 2021 | Colonial Pipeline | Cybecrime (DarkSide) | Ransomware → impact OT | Perturbation approvisionnement fuel US |
| 2022 | Industroyer2 (Ukraine) | Russie (Sandworm) | Tentative sabotage OT | Déjouée par CERT-UA/ESET |
| 2022 | Attaque Albanie | Iran | Wiper | Rupture diplomatique Iran-Albanie |
| 2023 | Volt Typhoon révélé | Chine (PRC) | Pré-positionnement | Infras critiques US |
| 2023 | 3CX supply chain | DPRK (Lazarus) | Supply chain | 600 000+ clients affectés |
| 2024 | Salt Typhoon | Chine (PRC) | Espionnage télécoms | Systèmes d'interception légale compromis |
| 2025 | Bybit crypto vol | DPRK (Lazarus) | Vol crypto | ~$1,5 Mrd (record historique) |

---

### Annexe E — Mapping ATT&CK par acteur

*Techniques ATT&CK les plus caractéristiques des 10 groupes les plus actifs — simplifié. Statut d'attribution entre parenthèses.*

| Acteur | Initial Access | Execution | Persistence | Cred Access | Lateral Move | C2 | Signature |
|--------|---------------|-----------|-------------|-------------|-------------|-----|-----------|
| **APT29** (publiquement attribué) | Supply chain, OAuth phishing | Signed binary proxy | Tokens/certificats SAML | Credential spray | GoldenSAML | HTTPS, services légitimes | Furtivité extrême, cloud |
| **APT28** (publiquement attribué) | Spear-phishing, exploit vuln | PowerShell, scripts | Service, registre | Mimikatz, credential harvest | RDP, SMB | HTTPS, custom | Exploitation 0-day |
| **Sandworm** (publiquement attribué) | Supply chain, exploit edge | Custom malware | Service, tâche planifiée | Mimikatz | PsExec, WMI | HTTPS, custom | Wipers, OT/ICS |
| **APT41** (publiquement attribué) | Supply chain, exploit web | Rootkits | Bootkits, registre | Credential dump | RDP, SMB | HTTPS, custom | Double mission |
| **Volt Typhoon** (publiquement attribué) | Exploit edge devices | LOLBins exclusif | Credentials légitimes | ntdsutil, mimikatz | LOLBins | Routeurs SOHO compromis | Pas de malware custom |
| **APT40** (publiquement attribué) | Exploit appliances réseau | Scripts, web shells | Web shells | Credential dump | SMB, RDP | HTTPS | Exploitation rapide CVE |
| **Lazarus** (publiquement attribué) | Social engineering, supply chain | Custom malware multi-OS | Service, tâche planifiée | Keylogger | RDP | HTTPS, custom | Crypto, LinkedIn |
| **APT35** (publiquement attribué) | Social engineering avancé | Scripts, backdoors | Registre, service | Credential phishing | Minimal | HTTPS | Impersonation individuelle |
| **APT33** (largement suspecté) | Password spraying | PowerShell | Service | Password spray | RDP | HTTPS | Volume, énergie |
| **Turla** (publiquement attribué) | Watering hole, supply chain | Ultra-custom malware | Rootkit, firmware | Custom tools | Réseaux satellite | Satellite, proxys | Sophistication extrême |

---

### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Acteurs APT (profils, campagnes, géopolitique) | **Ce cours (APT)** | — |
| Processus analytique CTI (cycle, ACH, attribution, production) | **Cours CTI** | APT (Ch.23 attribution, Annexe B/E données acteurs) |
| Détection SOC (SIEM, investigation, detection engineering) | **Cours SOC** | APT (Ch.27 défense APT-ready, Ch.3 TTP) |
| Incident Response | **Cours IR** | APT (Ch.27 containment APT, Ch.28 tabletop) |
| Forensic numérique | **Cours Forensic** | APT (Ch.3 artefacts TTP) |
| Intelligence économique | **Cours IE** | APT (Ch.4 cyber comme instrument de puissance, Ch.16-19 doctrines étatiques) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | APT (Ch.15 zones grises crime-État) |
| Dark Web | **Cours Dark Web** | APT (Ch.15 mercenaires, Ch.11 DPRK) |
| OSINT | **Cours OSINT Mastery** | APT (Ch.1 OSINT sur les acteurs) |
| Windows / AD | **Cours Windows / AD** | APT (Ch.3 TTP mouvement latéral, credential access) |

---

### Annexe G — Ressources et formation

#### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| M-Trends | Mandiant/Google | Tendances IR/CTI, TTP observées, métriques dwell time |
| Global Threat Report | CrowdStrike | Panorama menace par pays et par acteur |
| Digital Defense Report | Microsoft | Tendances globales, telemetry massive |
| DBIR | Verizon | Statistiques breaches, vecteurs d'accès |
| IOCTA | Europol | Menaces cyber organisées en Europe |
| Panorama de la cybermenace | ANSSI | Menaces sur la France, OIV, secteurs critiques |
| Threat Landscape | ENISA | Panorama menace européen |

#### Formations SANS

| Code | Titre | Focus |
|------|-------|-------|
| FOR578 | Cyber Threat Intelligence | CTI de référence — processus, acteurs, analyse |
| FOR508 | Advanced IR, Threat Hunting, Digital Forensics | IR + hunting guidé par CTI |
| FOR572 | Advanced Network Forensics | Détection réseau, C2, exfiltration |
| ICS515 | ICS Visibility, Detection, and Response | CTI et détection pour environnements OT |

#### Bases de données et références

| Ressource | Type | Usage |
|-----------|------|-------|
| MITRE ATT&CK Groups | Base de données | Profils d'acteurs avec alias et TTP |
| Malpedia (Fraunhofer) | Base de données | Mappings croisés acteurs/malware |
| MITRE CTI (GitHub) | Dataset | Données STIX des acteurs ATT&CK |
| The DFIR Report | Blog | Intrusions complètes analysées pas à pas |
| Mandiant Blog | Blog | Analyses de campagnes APT |
| Microsoft Threat Intelligence Blog | Blog | Campagnes, TTP, telemetry |
| CISA Advisories | Advisories | CVE exploitées, alertes APT, IoC |
| CERT-FR Bulletins | Advisories | Alertes France, recommandations |

#### Conférences

| Conférence | Focus |
|-----------|-------|
| Black Hat (US/EU/Asia) | Recherche offensive/défensive |
| SSTIC (France) | Recherche technique en sécurité |
| Botconf (France) | Analyse de malware, CTI |
| FIRST Conference | Communauté CERT/CSIRT mondiale |
| CyCon (Tallinn) | Géopolitique cyber, droit international |
| FIC / InCyber (Lille) | Cybersécurité et IE |

---

> **Note de clôture**
>
> Ce cours a été conçu comme l'encyclopédie des acteurs de la menace étatique — les profils, les campagnes, la géopolitique, et le tradecraft qui donnent sens aux alertes du SOC, aux artefacts du forensicien, et aux analyses du CTI.
>
> L'opération BLACKOUT illustre la leçon centrale : face à une intrusion sophistiquée, comprendre les acteurs est indispensable pour répondre. Un SOC sans connaissance des APT détecte un beaconing et isole un poste. Un SOC informé par le cours APT comprend que ce beaconing est compatible avec un pré-positionnement étatique dans une infrastructure critique européenne, calibre l'urgence de la réponse en conséquence, et déclenche les bons processus (signalement ANSSI, partage ISAC, monitoring OT renforcé).
>
> Le cours assume trois convictions. Première : les cyberopérations sont un instrument de puissance utilisé par tous les États dotés — les documenter sans angle mort (adversaires ET alliés) est une exigence de rigueur analytique. Deuxième : le pré-positionnement dans les infrastructures critiques est la menace structurelle de la prochaine décennie — et elle est la plus difficile à détecter. Troisième : l'attribution est un spectre, pas un binaire — et l'honnêteté sur les incertitudes est un signe de maturité, pas de faiblesse.
>
> *Comprendre qui menace • Pourquoi • Avec quels moyens • Dans quel contexte — pour mieux se défendre.*
