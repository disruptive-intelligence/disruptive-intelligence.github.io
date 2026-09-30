---
title: PARTIE VI — MENACES OT ET PRÉ-POSITIONNEMENT
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 6
chapters: 8
---

> **Ce que cette partie apprend.** Comprendre ce qui rend l’environnement OT radicalement différent de l’IT (protocoles sans authentification, systèmes hérités, impact physique), connaître les campagnes OT emblématiques qui ont défini le domaine (Stuxnet, Industroyer, Triton), maîtriser le concept de pré-positionnement comme menace structurelle de la prochaine décennie, et comprendre les principes de protection des infrastructures critiques.
> 
> **Ce qu’elle ne couvre pas.** Le détail technique d’ingénierie des systèmes industriels (domaine distinct), la doctrine complète de SOC OT (cours dédié OT security), les cadres réglementaires détaillés (Annexe G pour NIS 2 et OIV).
> 
> **Ce que vous saurez faire après cette partie.** Lire une architecture OT et identifier ses points d’exposition, reconnaître une campagne OT via ses TTP caractéristiques, formuler le dilemme du pré-positionnement (éradiquer vs surveiller), et participer à la construction d’une posture de protection d’infrastructure critique.

-----

## Chapitre 20 — Architecture OT/ICS et protocoles industriels

### 20.1 Qu’est-ce que l’OT : SCADA, DCS, PLC, HMI, historians, SIS

L’**OT** (Operational Technology) désigne l’ensemble des systèmes informatiques qui contrôlent ou supervisent des processus physiques — électricité, eau, gaz, pétrole, transport, fabrication, bâtiments. Par opposition à l’IT (Information Technology) qui traite de l’information, l’OT agit sur le monde physique.

Le vocabulaire technique est dense et mérite d’être maîtrisé.

**PLC** (Programmable Logic Controller — automate programmable industriel) : le composant de terrain qui exécute les fonctions de contrôle. Un PLC lit des capteurs (température, pression, débit), exécute une logique de contrôle programmée, et commande des actionneurs (vannes, moteurs, disjoncteurs). Exemples : Siemens S7-300/400/1500, Schneider Modicon M340/M580, Rockwell ControlLogix, Allen-Bradley SLC/MicroLogix. Les PLC ciblés par Stuxnet étaient des Siemens S7-315 et S7-417.

**DCS** (Distributed Control System — système de contrôle distribué) : architecture de contrôle pour les processus industriels continus (raffineries, centrales électriques, usines chimiques). Le DCS distribue les fonctions de contrôle entre plusieurs unités. Exemples : Honeywell Experion, Yokogawa CENTUM, ABB 800xA, Emerson DeltaV. Le DCS est typiquement plus intégré et plus propriétaire qu’un assemblage de PLC.

**SCADA** (Supervisory Control and Data Acquisition) : système de supervision qui collecte les données des PLC/DCS et permet aux opérateurs d’agir à distance. SCADA est plus distribué géographiquement que DCS (utile pour des infrastructures étalées — réseau électrique, réseau d’eau, oléoducs). Exemples : Siemens SIMATIC WinCC, GE iFIX, Schneider Citect, Wonderware/AVEVA System Platform.

**HMI** (Human-Machine Interface) : les écrans et interfaces par lesquels les opérateurs interagissent avec le SCADA/DCS. Peuvent être des applications Windows dédiées, des web clients, ou des panneaux industriels.

**Historian** : base de données spécialisée qui stocke les valeurs historiques des capteurs et des commandes — utilisée pour l’analyse, le reporting, la conformité réglementaire. Exemples : OSIsoft PI System (racheté par AVEVA), GE Proficy Historian, Wonderware Historian.

**SIS** (Safety Instrumented System — systèmes de sécurité industrielle) : systèmes **indépendants** du contrôle opérationnel, dont la **seule fonction** est d’arrêter le processus en cas de conditions dangereuses pour prévenir les accidents. Les SIS sont l’ultime filet de sécurité — si les contrôles classiques échouent, le SIS déclenche un arrêt d’urgence (shutdown). Exemples : Schneider Triconex, Rockwell/Allen-Bradley GuardLogix, Siemens SIMATIC S7-400F/FH, Honeywell Safety Manager. Les SIS font l’objet d’une norme spécifique (**IEC 61511**) et d’un niveau d’exigence (SIL — Safety Integrity Level) calibré selon le risque.

**RTU** (Remote Terminal Unit) : variante de PLC adaptée aux installations distantes et isolées (puits de pétrole, postes électriques, stations de pompage d’eau), souvent avec des communications longue distance.

**Engineering workstation** : poste de travail d’ingénieur utilisé pour programmer et configurer les PLC/DCS. Typiquement Windows, avec le logiciel de l’éditeur (Siemens TIA Portal, Rockwell Studio 5000, etc.). **Les engineering workstations sont des cibles de très haute valeur** — elles ont les credentials et les outils pour modifier la logique de contrôle.

### 20.2 Le modèle Purdue et la segmentation par niveau

Le **modèle Purdue** (Purdue Enterprise Reference Architecture — PERA, étendu en ISA-95) structure l’architecture OT en **niveaux** qui reflètent une hiérarchie fonctionnelle et justifient une segmentation réseau.

**Niveau 0 — Processus physique** : le processus physique lui-même (turbine, four, tuyauterie, chaîne de production).

**Niveau 1 — Contrôle de base** : les PLC et les capteurs/actionneurs qui agissent directement sur le niveau 0.

**Niveau 2 — Contrôle de supervision** : SCADA, DCS, HMI, historian locaux. C’est le niveau où les opérateurs supervisent et interviennent.

**Niveau 3 — Opérations de site** : MES (Manufacturing Execution System), gestion de production, historian globaux, systèmes de planification opérationnelle.

**DMZ industrielle (entre niveaux 3 et 4)** : zone démilitarisée qui filtre les flux entre l’OT (niveaux 0-3) et l’IT (niveaux 4-5). Devrait être obligatoire dans toute architecture sécurisée.

**Niveau 4 — Réseau bureautique** : systèmes IT classiques de l’organisation (ERP, messagerie, collaboration).

**Niveau 5 — Internet / Cloud** : connectivité externe.

**Niveaux SIS (parallèles)** : les SIS sont architecturalement **indépendants** des niveaux 1-3 du contrôle normal — ils ont leurs propres capteurs, leur propre logique, leurs propres actionneurs. Cette indépendance est la raison pour laquelle ils peuvent intervenir quand le contrôle normal échoue.

**Le principe** : les flux doivent être **contrôlés strictement entre niveaux**, notamment entre les niveaux IT (4-5) et OT (3 et moins). Un accès au niveau 4 ne devrait jamais donner un accès direct au niveau 2 — il doit passer par la DMZ industrielle avec authentification et inspection.

**En pratique** : cette segmentation idéale est souvent imparfaite. Les mises à jour des équipements OT nécessitent des accès depuis le niveau 4 (éditeurs, MSP distants), les postes d’ingénierie sont souvent double-connectés, les prestataires externes ont des accès VPN qui contournent partiellement l’architecture. **Ces imperfections sont les chemins d’attaque utilisés par les APT** pour compromettre l’OT via l’IT.

### 20.3 Protocoles industriels : Modbus, DNP3, IEC 60870-5-104, IEC 61850, OPC, PROFINET

Les protocoles industriels transportent les commandes et les mesures entre les composants OT. Leur connaissance est essentielle pour comprendre à la fois les opérations légitimes et les attaques.

**Modbus** (Modicon, 1979) : protocole historique, encore très largement déployé. Existe en Modbus RTU (série) et Modbus TCP (sur Ethernet). Extrêmement simple : lecture et écriture de registres. **Aucune authentification native**, aucun chiffrement, aucune intégrité. Un attaquant sur le réseau OT peut écrire dans n’importe quel registre d’un équipement accessible. Modbus est critiqué depuis des décennies pour son insécurité mais reste dominant dans l’industrie (inertie, coût de remplacement).

**DNP3** (Distributed Network Protocol, développé dans les années 1990 pour le secteur électrique, RTU vers control center) : largement utilisé dans le secteur électrique nord-américain. Version « DNP3 Secure Authentication » offre une authentification mais est rarement déployée.

**IEC 60870-5-104 (IEC 104)** : protocole de télécontrôle standardisé en Europe pour le secteur électrique (équivalent européen de DNP3). Transport sur TCP/IP. **Utilisé par Industroyer** pour commander directement les disjoncteurs et produire le blackout de Kiev 2016. Pas d’authentification native.

**IEC 61850** : standard plus récent pour les sous-stations électriques, orienté objet et utilisant Ethernet. Inclut **GOOSE** (Generic Object Oriented Substation Event) pour les communications rapides entre équipements de protection, et **SMV** (Sampled Measured Values) pour la télémétrie. Utilisé également par Industroyer. Sécurité améliorée par rapport aux protocoles plus anciens mais déploiement sécurisé inégal.

**OPC DA** (OLE for Process Control Data Access) : protocole Windows (basé sur DCOM) pour l’intégration SCADA/DCS, historiquement très utilisé mais considéré comme obsolète. Sécurité faible, dépendance Windows. Utilisé par Industroyer également.

**OPC UA** (Unified Architecture) : successeur moderne d’OPC DA, cross-platform, sécurité intégrée (authentification, chiffrement, signature). Adoption progressive mais la migration depuis OPC DA est lente dans les installations existantes.

**PROFINET** (PROcess FIeld NETwork) : standard d’Ethernet industriel pour l’automatisation, développé par Siemens. Dominant dans l’industrie manufacturière européenne.

**EtherNet/IP** (dérivé de CIP — Common Industrial Protocol) : standard américain concurrent de PROFINET, utilisé par Rockwell/Allen-Bradley.

**HART** (Highway Addressable Remote Transducer) : protocole historique pour la communication avec les capteurs intelligents (mesures de procédés chimiques, pétroliers). Existe en version filaire et sans fil (WirelessHART).

**Implications sécurité** : presque tous ces protocoles ont été conçus **avant que la cybersécurité soit une considération**. Leur sécurité native va de faible (Modbus, IEC 104) à moyenne (IEC 61850 avec options sécurisées), rarement à élevée (OPC UA bien configuré). La **sécurité OT repose donc massivement sur la segmentation réseau** plutôt que sur la sécurité intrinsèque des protocoles — si un attaquant atteint le réseau OT, il dispose de leviers considérables.

### 20.4 Absence d’authentification native et risques associés

Reprenons le point central : la plupart des protocoles OT n’exigent **aucune authentification** pour émettre des commandes. Cette caractéristique a des conséquences directes sur la nature des attaques OT.

**Implication n°1 — Accès au réseau = capacité d’action** : si un attaquant pénètre le segment OT, il peut directement commander des équipements. Pas besoin de compromettre des credentials additionnels — la seule question est de connaître la carte du réseau et les adresses des équipements.

**Implication n°2 — Pas de trace forte** : sans authentification, il n’y a pas de log fiable de « qui a envoyé telle commande ». Les investigations post-incident doivent s’appuyer sur des corrélations réseau (quelle IP source, quelle timing), pas sur des logs applicatifs.

**Implication n°3 — Les mitigations sont réseau** : l’ensemble de la sécurité OT dépend massivement de la segmentation (qui peut parler à qui), de la surveillance (qui parle en temps réel), et du durcissement des points de passage (engineering workstations, jump hosts).

**Implication n°4 — Les équipements eux-mêmes ne se défendent pas** : un PLC qui reçoit une commande Modbus « écrire valeur 100 dans registre 40001 » l’exécute, quelle que soit la source. Il n’y a pas d’équivalent d’un antivirus ou d’un EDR sur un PLC historique. Les PLC récents commencent à intégrer des fonctions de sécurité, mais le parc déployé reste largement vulnérable.

### 20.5 Convergence IT/OT : causes, avantages, risques

La **convergence IT/OT** est la tendance structurelle des dernières décennies où les frontières entre IT et OT se brouillent. Causes et conséquences.

**Causes** :

- **Besoin de données** : les directions veulent des tableaux de bord en temps réel consolidant données OT et IT (production, qualité, énergie consommée, maintenance).
- **Maintenance à distance** : les éditeurs d’équipements OT (Siemens, Schneider, Rockwell, ABB) proposent de la télémaintenance, qui nécessite des accès depuis Internet vers le réseau OT.
- **Migration cloud** : certaines fonctions historian et MES basculent vers le cloud.
- **IT des objets (IIoT)** : les nouveaux équipements OT intègrent nativement des fonctions IT (API REST, connexions cloud).
- **Coûts** : un réseau unifié est moins cher qu’un réseau OT isolé maintenu séparément.

**Avantages** : efficacité opérationnelle, visibilité métier, optimisation des processus.

**Risques** : la convergence **crée des chemins d’attaque** du réseau IT (largement exposé) vers le réseau OT. Ces chemins sont précisément ceux qu’exploitent les APT.

**Exemples de chemins exploités** :

- **Engineering workstation à double connexion** : ordinateur d’ingénieur connecté simultanément au réseau IT (pour emails, mises à jour) et au réseau OT (pour programmer les PLC). Compromis côté IT, il devient un pivot vers l’OT. C’est le chemin utilisé dans BLACKOUT et dans beaucoup de compromissions OT réelles.
- **Jump hosts / bastions** : serveurs de rebond entre IT et OT. S’ils sont durcis, ils peuvent être un point de contrôle ; mal configurés, ils sont un chemin direct.
- **Prestataires distants via VPN** : éditeurs de logiciels, intégrateurs, mainteneurs — accès VPN qui contourne la segmentation normale.
- **Supply chain logicielle** : les mises à jour d’applications historian ou HMI peuvent porter du malware (cas de M.E.Doc pour NotPetya — même si M.E.Doc n’était pas strictement OT, le pattern s’applique).
- **Ports USB** : les ingénieurs utilisent des USB pour transférer des configurations, des logs, des mises à jour. Un USB infecté peut franchir la segmentation physique.

**Recommandation générale** : la convergence étant une réalité irréversible, la sécurité doit être **pensée autour des chemins d’exposition**, pas uniquement autour d’une séparation stricte qui n’existe que partiellement dans la pratique.

### 20.6 Systèmes hérités : la problématique du patching et de l’EDR

Une spécificité majeure de l’environnement OT : la **longévité extrême des équipements**. Un PLC ou un DCS déployé a typiquement une durée de vie de **15 à 30 ans**. Les systèmes de contrôle dans les centrales électriques, raffineries, et sites industriels lourds peuvent être encore plus anciens.

**Implications** :

- **Pas de patching** : les équipements anciens ne reçoivent plus de mises à jour de sécurité. Les vulnérabilités connues ne sont pas corrigées. Et même quand des patches existent, l’appliquer nécessite souvent un arrêt du processus industriel — opération coûteuse, risquée, et rarement réalisée.
- **OS obsolètes** : les HMI et engineering workstations tournent souvent sur Windows XP, Windows 7, Windows Server 2003 ou 2008 — systèmes non-supportés qui restent en production parce que les applications industrielles ne sont pas certifiées sur les versions récentes.
- **Pas d’EDR** : les PLC et équipements de terrain ne supportent pas d’agents EDR. Les engineering workstations sur Windows obsolète ne peuvent souvent pas accueillir d’EDR moderne non plus. La détection repose entièrement sur le réseau et les comportements observables en amont.
- **Contraintes temps réel** : les équipements OT ont des contraintes temps réel qui ne tolèrent aucune latence additionnelle. Un EDR qui ralentit un HMI de 50 ms peut déstabiliser la supervision. Cette contrainte limite les options de défense.

**Approches modernes** :

- **Replacement progressif** : remplacer les équipements obsolètes quand c’est possible (mais cycles longs).
- **Compensating controls** : segmentation, monitoring, access control stricts autour des équipements qui ne peuvent pas être sécurisés intrinsèquement.
- **Passive monitoring OT** : capteurs réseau passifs (qui n’injectent aucun trafic) qui surveillent les communications OT et détectent les anomalies. Approche non-intrusive compatible avec les contraintes OT.

### 20.7 Le modèle d’attaque OT classique

L’attaque OT typique suit une séquence prévisible. La connaître permet d’anticiper où placer les détections.

**Étape 1 — Accès initial via IT** : phishing, exploitation edge, supply chain — les vecteurs sont ceux des APT IT classiques. Les attaquants accèdent au réseau bureautique (niveau 4 Purdue).

**Étape 2 — Mouvement latéral dans l’IT** : reconnaissance AD, credential dumping, Kerberoasting, identification des cibles d’intérêt. L’objectif : identifier les comptes et les systèmes qui ont accès au réseau OT.

**Étape 3 — Identification du chemin vers l’OT** : recherche des engineering workstations, des jump hosts, des serveurs historian ayant des pieds dans les deux mondes. BloodHound peut révéler ces chemins.

**Étape 4 — Pivot vers l’OT** : compromission d’un engineering workstation ou d’un jump host, utilisation pour pénétrer le segment OT. **Cette étape est le point de rupture** — avant, l’attaquant est dans un environnement IT classique ; après, il est dans un environnement où les défenses classiques ne fonctionnent plus.

**Étape 5 — Reconnaissance OT** : identification des équipements présents (PLC, HMI, RTU, SIS), identification des protocoles utilisés, cartographie du processus industriel. **Cette phase est typiquement longue — semaines à mois** — car l’attaquant doit comprendre ce qu’il peut faire. Un PLC Siemens S7 dans une raffinerie contrôle un processus spécifique ; modifier ses paramètres a des effets spécifiques. L’attaquant doit apprendre le processus.

**Étape 6 — Préparation de l’action** : développement ou adaptation du code qui manipulera les équipements. Peut impliquer du reverse engineering de la logique de contrôle, des tests en environnement de staging.

**Étape 7 — Déclenchement** : envoi des commandes malveillantes. Peut être : manipulation directe des automates (Industroyer), modification de la logique de contrôle (Stuxnet), désactivation des SIS (Triton), simple coupure par ouverture de disjoncteurs (Ukraine 2015).

**Durée totale** : de l’accès initial au déclenchement, une opération OT sophistiquée prend **plusieurs mois à plusieurs années**. Cette longue phase de préparation est la raison pour laquelle la détection précoce dans la phase IT est critique — intervenir avant que l’attaquant n’atteigne l’OT est bien plus facile que de contenir une fois le pivot effectué.

### 20.8 Visibilité OT : passive monitoring

La défense OT repose largement sur la **visibilité** des communications dans le segment OT. Les technologies dédiées ont émergé dans les années 2010-2020.

**Passive monitoring** : les capteurs passifs se connectent aux segments OT via des **mirror ports** ou des **network taps** — ils observent tout le trafic sans injecter le moindre paquet. Cette approche est compatible avec les contraintes OT (aucune latence ajoutée, aucun risque de perturber le processus).

**Vendors majeurs** :

- **Claroty** : plateforme OT orientée asset discovery, threat detection, risk management.
- **Dragos** : spécialisé sur les grandes infrastructures industrielles (énergie, eau, pétrole/gaz). Équipe de threat intelligence OT reconnue (Sergio Caltagirone, Joe Slowik historiquement).
- **Nozomi Networks** : plateforme polyvalente.
- **Tenable OT Security** (ex Indegy) : couvert par l’acquisition Tenable.
- **Cisco Cyber Vision** : solution Cisco intégrée.
- **Microsoft Defender for IoT** (ex CyberX) : intégration Microsoft.

Ces outils fournissent :

- **Asset inventory** : découverte automatique des équipements OT et leurs caractéristiques (marque, modèle, firmware).
- **Vulnerability assessment** : identification des CVE applicables aux équipements.
- **Anomaly detection** : détection des communications atypiques (nouveau flux, commandes inhabituelles).
- **Threat intelligence OT** : détection des TTP documentées (patterns d’Industroyer, de Triton, etc.).

**Leçon opérationnelle** : une organisation qui n’a pas de visibilité OT **ne peut pas détecter** une compromission OT sophistiquée avant qu’elle ne produise un effet physique. Investir dans la visibilité OT est la première étape de la maturité.

### 20.9 La protection des SIS : l’enjeu ultime

Les **SIS** (Safety Instrumented Systems) méritent une attention particulière car ils représentent **l’ultime filet de sécurité physique** dans une installation industrielle.

**Principe** : les SIS sont conçus pour arrêter le processus en cas de conditions dangereuses. Si la température d’un réacteur dépasse un seuil critique, si une pression devient incontrôlable, si un capteur révèle une fuite — le SIS déclenche un **shutdown** ordonné qui met l’installation en état sûr.

**Indépendance** : pour garantir cette fonction, les SIS sont **architecturalement indépendants** du contrôle normal. Ils ont leurs propres capteurs, leur propre logique, leurs propres actionneurs. Un défaut du contrôle normal ne doit pas affecter le SIS.

**La menace ultime — désactiver les SIS** : si un attaquant **désactive les SIS AVANT de provoquer une condition dangereuse**, il neutralise l’ultime filet de sécurité. L’installation peut alors atteindre des conditions qui, sans SIS fonctionnel, causent des dommages physiques catastrophiques — explosion, fuite toxique, accident grave.

**C’est ce qu’a tenté Triton/TRISIS** (Arabie Saoudite 2017, Ch.21) contre les Triconex Schneider d’une usine pétrochimique. L’attaque a échoué — mais par chance (un arrêt de sécurité non anticipé a révélé l’intrusion). Si elle avait réussi, le scénario envisageable incluait potentiellement une explosion majeure avec pertes humaines.

**Protection des SIS** :

- **Isolation physique absolue** : idéalement, les SIS ne devraient avoir aucune connexion réseau à quoi que ce soit d’autre. Le strict minimum opérationnel (logs, maintenance) doit être géré via des postes dédiés air-gappés.
- **Air gap** : séparation physique totale entre SIS et autres réseaux, y compris les autres segments OT. Si impossible, diodes unidirectionnelles (hardware qui permet le flux dans un seul sens).
- **Credentials séparés** : les ingénieurs SIS ont des comptes distincts de ceux du contrôle opérationnel.
- **Audits réguliers** : vérification de l’intégrité des programmes SIS.

La protection des SIS n’est pas un « nice to have » — elle est l’enjeu le plus critique de la cybersécurité industrielle, celui où un échec produit des morts.

-----

## Chapitre 21 — Campagnes OT/ICS destructrices

Ce chapitre documente les campagnes OT emblématiques dans un ordre globalement chronologique. Ensemble, elles constituent l’**histoire contemporaine** du cyber appliqué aux infrastructures physiques.

### 21.1 Stuxnet (2010) — la première arme cyber OT

**Acteurs** : États-Unis et Israël (co-attribution). **Cible** : centrifugeuses d’enrichissement d’uranium iraniennes à Natanz.

**Traité aux Ch.14 (impact Iran) et Ch.18 (Israël).** Synthèse pour la dimension OT.

**Architecture technique** :

- Quatre **vulnérabilités 0-day Windows** utilisées pour la propagation initiale (inhabituel — un seul 0-day suffirait en général).
- Ciblage extrêmement précis : **ne s’activait que sur des systèmes Windows spécifiques** exécutant **Siemens WinCC/STEP7** (logiciel de programmation PLC Siemens) **connectés à des PLC S7-315 ou S7-417** contrôlant des **centrifugeuses tournant à certaines vitesses spécifiques**. Ces quatre conditions combinées garantissaient que Stuxnet ne s’activerait que sur les systèmes ciblés.
- **Modification de la logique PLC** : une fois sur le système de contrôle, Stuxnet modifiait la programmation du PLC pour faire osciller la vitesse des centrifugeuses entre limites extrêmes, provoquant des contraintes mécaniques qui les détruisaient progressivement.
- **Masquage** : parallèlement, Stuxnet interceptait les signaux de télémétrie et **affichait des valeurs normales aux opérateurs**. Les ingénieurs voyaient sur leurs HMI que tout fonctionnait normalement pendant que les centrifugeuses s’auto-détruisaient.

**Impact** : environ 1 000 centrifugeuses détruites entre 2008 et 2010, programme iranien retardé de 2-3 ans selon les estimations.

**Leçons OT** :

- **Les PLC peuvent être manipulés avec effet physique** : démonstration fondatrice.
- **Le masquage des opérateurs est possible et dangereux** : les HMI peuvent mentir.
- **Les engineering workstations sont des cibles critiques** : Stuxnet utilisait l’engineering workstation Siemens pour modifier le PLC.
- **La propagation non contrôlée** : Stuxnet s’est échappé des systèmes ciblés via USB, révélant l’opération. Le risque de « blowback » des armes cyber est réel.

### 21.2 BlackEnergy / KillDisk — Ukraine décembre 2015

**Acteur** : Sandworm (GRU Unit 74455). **Cible** : trois distributeurs d’électricité ukrainiens — Prykarpattyaoblenergo, Kyivoblenergo, Chernivtsioblenergo. **Premier blackout cyber confirmé de l’histoire**.

**Chronologie** :

- **Printemps-été 2015** : phase de reconnaissance et compromission initiale via spear-phishing (documents Office avec macro, envoyés à des ingénieurs des distributeurs).
- **Plusieurs mois** : mouvement latéral, compromission des systèmes de supervision, pivot vers les segments OT.
- **23 décembre 2015, 15h30** : déclenchement. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA.

**Mécanisme de l’attaque** :

- **Prise de contrôle manuelle** des HMI via des outils d’administration à distance. Les opérateurs ukrainiens ont vu, sur leurs propres écrans, leurs souris bouger et leur clavier taper sans leur action.
- **Ouverture manuelle de 30+ disjoncteurs** dans les postes de transformation.
- **230 000 foyers** privés d’électricité pendant ~6 heures.
- **KillDisk** déployé en parallèle : wiper effaçant les systèmes de supervision pour compliquer la récupération et prolonger l’indisponibilité.

**Particularité** : l’attaque a été **largement manuelle** — des opérateurs humains cliquant sur des HMI à distance. Pas de malware automatisé qui commande les équipements. Cette approche indique une compréhension fine du système mais aussi une prise de risque (l’opération prenait du temps, les défenseurs pouvaient réagir).

**Restoration** : les opérateurs ukrainiens, entraînés à basculer en mode manuel, ont rétabli l’alimentation en parcourant physiquement les postes et en refermant les disjoncteurs manuellement.

**Attribution** : CERT-UA, SBU, puis Mandiant et d’autres — attribution à Sandworm publiée en 2016-2017.

**Leçons** :

- **Un blackout cyber est possible** : démonstration empirique.
- **Les opérateurs entraînés peuvent récupérer rapidement** : la capacité de basculer en manuel est un élément de résilience majeur.
- **KillDisk en complément** : pattern Sandworm de combiner attaque et wiper pour maximiser l’indisponibilité.

### 21.3 Industroyer / CrashOverride — Ukraine décembre 2016

**Acteur** : Sandworm. **Cible** : poste de transformation électrique de la banlieue de Kiev.

**Rupture par rapport à 2015** : Industroyer est le **premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles industriels natifs**. Contrairement à 2015 où l’attaque était manuelle, Industroyer **automatise** la manipulation des équipements.

**Architecture Industroyer** :

- **Module IEC 60870-5-101** : protocole série électrique.
- **Module IEC 60870-5-104** : version TCP/IP du précédent, protocole dominant en Europe. Le module peut énumérer les équipements et **commander l’ouverture/fermeture des disjoncteurs**.
- **Module IEC 61850** : protocole des sous-stations modernes. Peut émettre des commandes GOOSE.
- **Module OPC DA** : intégration SCADA/DCS.
- **Module de wiping** : destruction des configurations et des systèmes de supervision.
- **Backdoor** pour la persistence et l’accès ultérieur.

**Déclenchement** : 17 décembre 2016, minuit. Le module IEC 104 ouvre les disjoncteurs. Blackout dans une partie de Kiev pendant ~1 heure.

**Sophistication** : Industroyer démontre que Sandworm a investi dans des capacités OT sur mesure. Chaque module représente une compréhension approfondie du protocole correspondant et des systèmes qui l’implémentent.

**Attribution** : attribution à Sandworm confirmée par ESET (qui a analysé le malware en profondeur — rapport fondateur de juin 2017) et par les agences Five Eyes.

**Leçons** :

- **Le cyber OT est industrialisable** : pas seulement des attaques ponctuelles manuelles, mais des outils sophistiqués réutilisables.
- **Les protocoles sans authentification sont des leviers d’attaque directs** : IEC 104, IEC 61850 — pas d’authentification, commandes exécutées sans challenge.
- **L’investissement OT des acteurs étatiques est sérieux** : développer Industroyer a pris probablement 1-2 ans d’effort.

### 21.4 Triton / TRISIS — Arabie Saoudite 2017

**Acteur** : attribué à la Russie, plus précisément au **Central Scientific Research Institute of Chemistry and Mechanics (TsNIIKhM)** — institut de recherche militaire russe, sanctionné par OFAC en 2020. **Cible** : usine pétrochimique saoudienne (non nommée publiquement, mais largement identifiée comme Petro Rabigh).

**Rupture** : Triton est le premier malware à avoir ciblé explicitement des **SIS** (Safety Instrumented Systems) — les systèmes de sécurité ultimes.

**Cible spécifique** : **Schneider Triconex** — marque emblématique de SIS, largement déployée dans l’industrie pétrochimique et nucléaire. Triton était conçu pour reprogrammer les Triconex, désactivant potentiellement leurs fonctions de sécurité.

**Scénario envisagé** : si Triton avait réussi pleinement, l’attaquant aurait pu, à un moment choisi, **désactiver les SIS puis provoquer une condition dangereuse** dans le processus industriel. Sans SIS pour déclencher le shutdown, l’installation atteint potentiellement des conditions d’**explosion ou de fuite toxique**. Les dommages envisageables incluaient des pertes humaines significatives.

**Comment Triton a été découvert** : par **accident**. Lors d’une intervention Triton sur un Triconex, le malware a provoqué un **arrêt de sécurité non anticipé** — le Triconex a détecté une anomalie dans sa propre programmation et s’est mis en mode sûr (shutdown). Les ingénieurs saoudiens, cherchant à comprendre pourquoi leur SIS s’était arrêté, ont découvert la compromission.

**Attribution** : Dragos a attribué Triton à un acteur qu’il a nommé **XENOTIME**. L’attribution plus précise au TsNIIKhM russe a été établie par le FBI et publiée via sanctions OFAC en 2020.

**Implication stratégique** : Triton est **le wake-up call** sur les risques OT. Un État avait investi dans une capacité visant à pouvoir, à un moment politique choisi, causer des morts via cyber. La ligne entre cyber et terrorisme d’État est franchie, ou près de l’être.

**Leçons OT** :

- **Les SIS sont des cibles APT** : ne plus considérer les SIS comme « naturellement protégés » parce que « critiques ».
- **L’air gap SIS est indispensable** : isolation totale.
- **Des capacités SIS sont en développement** : au-delà de Triton, d’autres acteurs étatiques ont probablement des capacités similaires. XENOTIME est suivi comme groupe actif.

### 21.5 Industroyer2 — Ukraine avril 2022

**Acteur** : Sandworm. **Cible** : un opérateur électrique ukrainien (non nommé publiquement mais situé dans la région de Kiev).

**Contexte** : dans les semaines suivant l’invasion russe de l’Ukraine (24 février 2022), Sandworm tente de reproduire son succès de 2016 en développant **Industroyer2** — évolution du malware de 2016.

**Améliorations Industroyer2** :

- Modules protocoles OT conservés.
- Ciblage plus précis (adapté à la victime spécifique).
- Pattern de déclenchement synchronisé avec d’autres opérations (wiper CaddyWiper prévu en parallèle pour complexifier la réponse).

**Échec grâce à la défense** : **Industroyer2 a été déjoué**. L’équipe CERT-UA, en collaboration avec **ESET**, a détecté le déploiement avant le déclenchement prévu. Une analyse rapide a permis la neutralisation en quelques heures. Le déclenchement prévu n’a pas eu lieu, ou seulement avec des effets très limités.

**Signification** : succès défensif majeur. Démonstration que la coopération CERT-UA/vendor CTI peut neutraliser une attaque OT étatique avant impact. C’est un modèle opérationnel étudié par toutes les agences cyber occidentales.

**Publication** : rapport conjoint CERT-UA et ESET (avril 2022) documente le malware et la réponse défensive. Lecture importante pour comprendre l’état de l’art OT défensif.

### 21.6 Colonial Pipeline (mai 2021) — ransomware IT avec impact OT

**Acteur** : **DarkSide** (groupe RaaS russophone). **Cible** : **Colonial Pipeline**, opérateur d’un oléoduc majeur transportant ~45% de l’essence consommée sur la côte est américaine.

**Particularité** : Colonial Pipeline illustre un pattern où **le cyber IT produit un impact OT indirect**, sans que l’OT soit directement compromis.

**Chronologie** :

- Compromission initiale via un **compte VPN sans MFA** (credentials probablement issus d’un breach ou d’un infostealer).
- Déploiement de DarkSide sur le réseau IT.
- **7 mai 2021** : Colonial Pipeline **coupe volontairement l’OT** — par mesure de précaution, l’entreprise arrête l’oléoduc parce qu’elle ne peut pas garantir que l’OT n’a pas été compromis et parce que le système de facturation (IT) est inopérant (pas de moyen de facturer les clients).
- **Impact** : pénuries d’essence sur la côte est US pendant plusieurs jours, situation d’urgence déclarée par le gouverneur de plusieurs États.
- Colonial Pipeline paie une rançon d’environ 4,4 millions de dollars en Bitcoin (dont environ 2,3 millions seront **récupérés ultérieurement par le FBI** — première récupération notable de rançon crypto).

**Leçons** :

- **La convergence IT/OT crée des dépendances opérationnelles** : même sans compromission OT directe, un incident IT peut paralyser l’OT (par précaution légitime ou par dépendance business — facturation, logistique).
- **Les credentials VPN sont un vecteur majeur** : MFA sur les accès distants n’est pas optionnel.
- **Le paiement de rançon peut être partiellement récupéré** : coopération FBI/exchanges/blockchain intelligence.
- **Conséquences macroéconomiques** : une cyberattaque sur une infrastructure critique peut produire des effets au niveau sociétal (pénuries, urgence).

### 21.7 CosmicEnergy — malware Sandworm découvert 2023

**Acteur** : Sandworm (probablement). **Découverte** : Mandiant a publié en mai 2023 l’analyse d’un nouveau malware OT nommé **CosmicEnergy**, trouvé sur **VirusTotal** (uploadé par quelqu’un — probablement l’auteur, un chercheur, ou une victime).

**Capacités** : CosmicEnergy cible les **systèmes de protection IEC 60870-5-104** — similaire à Industroyer mais avec des différences techniques suggérant une évolution distincte. Peut envoyer des commandes IEC 104 pour ouvrir/fermer des équipements.

**Incertitude** : l’utilisation opérationnelle de CosmicEnergy n’est pas confirmée publiquement — il peut s’agir d’un malware en développement, d’un outil de red team russe, ou d’un malware qui n’a pas encore été déployé.

**Signification** : démonstration que le **développement d’outils OT offensifs continue**. Sandworm (ou des acteurs apparentés) investit dans une nouvelle génération de capacités OT. La menace reste active et évolutive.

### 21.8 Attaques récentes 2024-2025

**Cyber Av3ngers contre l’eau (fin 2023 - 2024)** : groupe attribué à l’Iran (IRGC) qui a ciblé des **PLC Unitronics exposés sur Internet** dans des systèmes d’eau municipaux américains. Impact limité (message politique sur les écrans HMI, pas de perturbation majeure du processus), mais démonstration symbolique forte. A conduit à une mobilisation CISA et à des advisories aux opérateurs d’eau.

**Tentatives sur les opérateurs électriques européens (2023-2025)** : advisory ANSSI et BSI ont évoqué publiquement (sans nommer de cibles) des tentatives d’intrusion dans des opérateurs électriques européens. Attribution variable entre acteurs russes (Sandworm, Unit 29155) et acteurs chinois.

**Ciblage d’installations oil & gas et pétrochimiques** : depuis 2022, plusieurs incidents non rendus publics, mais des rapports Dragos et Mandiant font état d’une activité croissante. Certaines compagnies pétrolières européennes ont renforcé publiquement leurs équipes OT security.

**Le contexte général 2024-2026** : les attaques OT se multiplient en tentatives, avec relativement peu d’impacts majeurs publics en Europe. Mais la pression est croissante, et le modèle BLACKOUT (pré-positionnement sans action immédiate) est probablement plus fréquent que les incidents publics ne le suggèrent.

### 21.9 Leçons générales des campagnes OT

La synthèse des campagnes OT documentées dessine un **corpus de leçons transversales**.

**Le cyber OT est réel et testé** : Stuxnet, Industroyer, Triton, Industroyer2, CosmicEnergy démontrent qu’au moins trois États (US/Israël, Russie, avec d’autres probablement) ont des capacités OT opérationnelles. Ce n’est pas une menace théorique.

**L’impact potentiel est physique** : blackouts, explosions potentielles (Triton), paralysies opérationnelles (Colonial). Le cyber peut produire des dommages comparables à des frappes militaires conventionnelles dans certains scénarios.

**La sophistication requise est importante** : développer un malware OT fonctionnel est un effort d’années pour des équipes expertes. Ce n’est pas à la portée d’un cybercriminel classique. Mais c’est à la portée de plusieurs États.

**Les défenses sont possibles** : Industroyer2 déjoué démontre qu’une défense OT bien préparée peut neutraliser une attaque étatique. La visibilité, la collaboration, et la rapidité de réponse sont les facteurs clés.

**Le pré-positionnement est la tendance actuelle** : moins d’attaques destructives déclenchées, plus d’opérations qui maintiennent un accès dormant. Ce pattern est l’objet du chapitre suivant.

-----

## Chapitre 22 — Le pré-positionnement : la menace silencieuse

### 22.1 Définition opérationnelle du pré-positionnement

Le **pré-positionnement** est le maintien d’un **accès dormant** dans des infrastructures critiques, **sans action immédiate**, pour une utilisation future en cas de conflit ou d’escalade politique. C’est le scénario stratégique le plus inquiétant du paysage cyber contemporain.

**Caractéristiques opérationnelles** :

- **Accès maintenu** : l’attaquant a compromis des systèmes critiques et conserve la capacité d’y accéder.
- **Pas d’exfiltration massive** : contrairement à l’espionnage, le pré-positionnement ne collecte pas de renseignement (ou seulement le minimum nécessaire au maintien d’accès).
- **Pas de sabotage** : contrairement à une attaque destructive, aucune action malveillante n’est déclenchée.
- **Pas de ransomware** : aucune monétisation, aucune visibilité.
- **Patience opérationnelle** : l’accès peut être maintenu des mois ou des années avant activation — ou ne jamais être activé.

**Intention stratégique** : disposer d’un **levier activable** en cas de besoin. Le message implicite est : « en cas d’escalade/conflit/décision politique, nous pouvons activer ces accès pour causer des dommages aux infrastructures critiques de notre adversaire ».

C’est une **forme de dissuasion cyber**. Comme la dissuasion nucléaire, elle repose sur l’existence d’une capacité plus que sur son utilisation. Mais contrairement à la dissuasion nucléaire, elle est **silencieuse et ambiguë** — la cible peut ignorer l’existence du pré-positionnement, ce qui affaiblit l’effet dissuasif mais préserve la flexibilité opérationnelle.

### 22.2 Volt Typhoon : le cas d’école

**Volt Typhoon** est l’exemple de pré-positionnement le plus documenté publiquement. Déjà introduit au Ch.9, traité en détail comme étude de cas au Ch.31.

**Synthèse pour ce chapitre** :

- Activité au moins depuis mi-2021, probablement plus tôt.
- Cibles : opérateurs de télécoms, énergie, eau, transport aux US et dans le Pacifique (Guam).
- TTP ultra-furtives : LotL exclusif, credentials légitimes, pas de malware custom, C2 via routeurs SOHO compromis.
- **Aucune exfiltration massive, aucune action destructive, aucune monétisation observées**.
- Attribué par les Five Eyes (advisory mai 2023 et réitérations 2024) à la Chine, probablement PLA ou affilié.

**Signification stratégique** : interprété par la communauté de renseignement américaine comme une **capacité de dissuasion/représailles chinoise** liée au scénario Taïwan. Si un conflit militaire éclate autour de Taïwan, la Chine pourrait activer ces accès pour frapper les infrastructures critiques américaines et alliées, dégradant les capacités de projection militaire US dans la région.

**Démantèlements partiels** : FBI a démantelé en janvier 2024 le **KV Botnet** (routeurs Cisco RV domestiques utilisés comme C2 Volt Typhoon) sous mandat judiciaire. Mais Volt Typhoon dispose probablement d’infrastructures alternatives.

### 22.3 Salt Typhoon : autre dimension du pré-positionnement

**Salt Typhoon** illustre une autre facette : pré-positionnement pour l’espionnage stratégique plutôt que pour le sabotage. Déjà traité au Ch.9 et Ch.10.

**Synthèse** :

- Compromission de multiples opérateurs télécoms US (Verizon, AT&T, Lumen confirmés).
- Accès aux **Lawful Intercept Systems** — compromission ciblée permettant de voir qui les autorités américaines surveillaient.
- Accès aux communications de millions d’Américains, ciblage particulier de personnalités politiques.
- Durée de présence estimée à au moins un an avant détection.

**Pré-positionnement ou espionnage ?** Salt Typhoon se situe à la frontière. L’accès maintenu sur les télécoms **est** un pré-positionnement (levier activable en conflit), mais l’accès était aussi activement utilisé pour du renseignement. Cette combinaison — pré-positionnement + espionnage — est probablement la configuration la plus fréquente dans la réalité, les deux n’étant pas mutuellement exclusifs.

### 22.4 Sandworm et le pré-positionnement énergie européenne

Le pré-positionnement n’est pas l’apanage chinois. **Sandworm (GRU Unit 74455)** conduit depuis plusieurs années des opérations de pré-positionnement dans les infrastructures critiques européennes, dans le contexte du conflit ukrainien.

**Documentation publique** :

- Advisory ANSSI (France), BSI (Allemagne), CERT-UA ont évoqué publiquement (avec parcimonie sur les détails) des tentatives d’intrusion dans des infrastructures critiques européennes.
- Rapports Mandiant, Microsoft, Dragos documentent des compromissions d’opérateurs énergie, eau, transport en Europe (sans nommer les victimes pour raisons opérationnelles).
- **Tentative Industroyer2 (avril 2022)** déjouée — démonstration d’intention et de capacité.

**Implications** : l’Europe est une cible de pré-positionnement russe crédible. Les opérateurs européens OIV (France) et entités essentielles (NIS 2) doivent intégrer ce scénario dans leur planification.

### 22.5 Autres clusters sous observation

Plusieurs clusters sont sous observation pour des activités possibles de pré-positionnement, sans qu’une attribution définitive ait été publiée.

**Flax Typhoon** (Chine, lié à Integrity Technology Group sanctionné en 2025) : construisait un botnet massif (Raptor Train, 260 000+ dispositifs IoT compromis) démantelé en septembre 2024 par le FBI. Utilisé probablement comme infrastructure offensive pour d’autres clusters chinois — peut inclure des fonctions de pré-positionnement.

**Clusters non attribués** : les advisories ANSSI, CISA, et partenaires mentionnent régulièrement des clusters observés dans des infrastructures critiques, sans attribution publique à date. Leur caractérisation comme pré-positionnement dépend de l’observation de leur comportement (absence d’exfiltration, absence de destructif, maintien d’accès long terme).

**Clusters iraniens** : moins documentés comme pré-positionnement structurel, mais les ciblages « Cyber Av3ngers » sur l’eau et sur l’énergie incluent potentiellement des composantes de pré-positionnement (maintien d’accès post-démonstration initiale).

### 22.6 La difficulté de détection maximale

Le pré-positionnement est la menace la plus difficile à détecter, pour des raisons structurelles.

**Pas de malware custom** : Volt Typhoon démontre que le LotL exclusif est possible et efficace. Sans binaire malveillant à hasher, les signatures EDR classiques sont aveugles.

**Pas de traffic anormal** : l’utilisation de LOLBins et de credentials légitimes produit un trafic qui ressemble à de l’administration normale. Les patterns de beaconing réguliers sont évités au profit d’accès intermittents et irréguliers.

**Pas de comportement distinctif** : les actions sont limitées au strict minimum nécessaire. Pas d’exfiltration visible, pas de tentatives de privilege escalation bruyantes, pas de mouvement latéral massif.

**Pas de monétisation** : contrairement au ransomware ou au cryptominer, le pré-positionnement ne génère aucune activité financière détectable.

**Longue durée** : les opérations s’étalent sur des mois à des années. Les anomalies, si détectables individuellement, se fondent dans le bruit de fond opérationnel normal.

**Implications détection** : la détection repose **entièrement** sur les **anomalies comportementales** et la **corrélation multi-sources**.

- **Baseline des activités admin** : un compte admin qui se connecte à un serveur inhabituel, à une heure inhabituelle, depuis un endpoint inhabituel est un signal. Établir la baseline prend du temps, la maintenir exige de la discipline.
- **Corrélation cross-sources** : connexion VPN + activité locale + connexion AD + trafic sortant. Aucun signal seul n’est conclusif ; leur combinaison peut l’être.
- **Threat hunting proactif** : recherche active d’anomalies subtiles, guidée par les TTP documentées des acteurs de pré-positionnement. Chasse au fil de l’eau, pas alerte automatique.
- **Détection réseau OT** : monitoring passif du trafic OT pour détecter les communications inhabituelles vers les équipements.

### 22.7 Le dilemme : éradiquer ou surveiller ?

Une fois un pré-positionnement détecté, les défenseurs font face à un **dilemme opérationnel** sans solution simple.

**Option A — Éradication immédiate** :

- **Avantage** : élimine la menace active, élimine le risque d’activation.
- **Inconvénient** : signal à l’adversaire que la détection a eu lieu. L’adversaire adaptera ses TTP, réinfectera via des vecteurs différents, et sera plus difficile à détecter la prochaine fois. **Perte de visibilité stratégique**.
- **Inconvénient** : si l’éradication est incomplète (accès redondants non identifiés), l’adversaire revient rapidement avec des TTP modifiées.

**Option B — Surveillance contrôlée** :

- **Avantage** : collecte de renseignement sur les TTP, sur les objectifs, sur les capacités. Ce renseignement peut être partagé avec d’autres défenseurs potentiellement ciblés. Possibilité d’identifier d’autres victimes.
- **Avantage** : ne révèle pas la détection à l’adversaire, préservant la capacité de détecter une activation imminente.
- **Inconvénient** : **risque moral et opérationnel majeur**. Si l’adversaire active son pré-positionnement avant que le défenseur puisse intervenir, l’impact peut être catastrophique. **Qui porte la responsabilité** si un blackout survient pendant la phase de surveillance ?
- **Inconvénient** : nécessite une coordination étroite avec les autorités (agences nationales) et un consensus légal/politique souvent difficile à obtenir.

**Option C — Hybride** :

- **Éradication partielle** des accès identifiés tout en maintenant la surveillance sur d’autres vecteurs suspectés.
- **Collaboration avec les agences nationales** : l’agence nationale peut prendre le relais sur la surveillance stratégique pendant que l’opérateur éradique opérationnellement.
- **Partage d’information** : le pré-positionnement découvert est communiqué à la communauté (ISAC sectoriel, CERT) pour alerter d’autres victimes potentielles.

**En pratique** : le dilemme est **résolu au cas par cas** selon la gravité, le contexte géopolitique, les ressources disponibles, et le cadre juridique. Pour un opérateur privé, l’éradication rapide est souvent la réponse par défaut (risque opérationnel non acceptable). Pour les agences nationales sur des cibles stratégiques (télécoms, énergie), la surveillance contrôlée peut être préférée.

Le dilemme n’a pas de réponse universelle. Il est exercé dans les tabletops (Ch.28) et gagne à être pensé à froid, pas dans l’urgence d’un incident réel.

### 22.8 Implications pour l’Europe

Le pré-positionnement est une menace crédible pour l’Europe. Implications opérationnelles.

**Secteurs prioritaires** :

- **Énergie** (électricité, gaz, pétrole) : cible historique de Sandworm, cible plausible de pré-positionnement chinois.
- **Télécoms** : cible démontrée par Salt Typhoon (US), extensible à l’Europe.
- **Eau** : cible de Cyber Av3ngers (Iran) et potentiellement d’acteurs russes.
- **Transport** (aéroportuaire, ferroviaire, maritime) : cible plausible pour des scénarios de disruption majeure.
- **Finance** : cible moins de pré-positionnement que d’espionnage et de fraude, mais à surveiller.
- **Santé** : cible ransomware massive, mais des APT peuvent s’y positionner aussi.

**Capacités à développer** :

- **Visibilité OT** (Ch.20) : passive monitoring sur les segments industriels.
- **Visibilité identité cloud** : monitoring des authentifications, des consentements OAuth, des activités admin (baseline + anomalies).
- **Threat hunting proactif** : équipes dédiées ou prestataires spécialisés qui recherchent activement les pré-positionnements silencieux.
- **Collaboration CERT nationale + sectoriel + international** : le modèle Ukraine est une référence.
- **Préparation à la réponse** : exercices sur les scénarios de pré-positionnement détecté, avec le dilemme éradication/surveillance.

**Cadre réglementaire** : **NIS 2** (entrée en application 2024) impose aux entités essentielles européennes des obligations de cybersécurité renforcées incluant la gestion des menaces étatiques. L’**EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence. Cadre à consolider dans les années à venir.

### 22.9 Fil rouge — BLACKOUT Épisode 5

> **⚡ BLACKOUT — Épisode 5 : pré-positionnement confirmé**
> 
> Après plusieurs semaines d’investigation, le CERT consolide l’analyse : **BLACKOUT est un cas de pré-positionnement**. Les éléments convergents :
> 
> **Absence d’exfiltration** : l’analyse des flux réseau sortants sur les 42 jours de présence documentée de l’attaquant ne révèle aucune exfiltration massive. Quelques dizaines de mégaoctets transférés, compatibles avec de la reconnaissance interne ou du maintien d’accès, pas avec une extraction de propriété intellectuelle ou de données sensibles.
> 
> **Absence d’action destructive** : aucune modification des automates détectée, aucune tentative d’interaction avec les SIS, aucun wiper déposé, aucun ransomware.
> 
> **Maintenance de l’accès** : l’attaquant a créé **trois mécanismes de persistence indépendants** sur le poste d’ingénierie OT (DLL sideloading initial, tâche planifiée, service modifié). Ce n’est pas une tentative ponctuelle — c’est une présence conçue pour durer.
> 
> **Reconnaissance du processus industriel** : l’analyse des logs révèle que l’attaquant a consulté pendant plusieurs jours les documentations techniques du SCADA, les schémas électriques, les procédures opérationnelles. Il comprenait le processus avant de s’engager plus loin.
> 
> **Positionnement stratégique** : le poste d’ingénierie OT compromis a un accès direct à 12 postes de transformation haute tension desservant environ 400 000 foyers. Un attaquant activant cet accès pourrait, théoriquement, provoquer un blackout d’envergure.
> 
> **Diagnostic CERT** : **BLACKOUT est un pré-positionnement OT** avec capacité potentielle de sabotage. L’acteur est soit Sandworm (Russie, contexte ukrainien), soit un cluster chinois (Volt Typhoon ou similaire, pré-positionnement stratégique), soit un cluster non identifié. L’analyse des TTP et le contexte géopolitique orientent vers une probabilité supérieure pour **H1 Sandworm**, mais **l’incertitude demeure** et sera traitée formellement dans la matrice ACH au Ch.24.
> 
> **Décision opérationnelle** : après concertation entre l’opérateur, le CERT, et l’ANSSI (l’opérateur étant OIV), **option A — éradication** est choisie. Raisons :
> 
> - Risque opérationnel non acceptable de laisser le pré-positionnement actif (potentiel d’activation si escalade géopolitique).
> - Contexte européen actuel tendu (conflit ukrainien, tensions énergétiques).
> - Capacité à déployer une équipe dédiée pour l’éradication complète et simultanée de tous les accès.
> 
> L’éradication est planifiée pour les prochains jours. Le Ch.32 documente comment elle s’est déroulée et quelles leçons ont été tirées.

-----

## Chapitre 23 — Protection des infrastructures critiques

### 23.1 Cartographie des infrastructures critiques européennes

Les **infrastructures critiques** (IC) sont les infrastructures dont la disruption aurait des conséquences majeures pour la sécurité, la santé publique, l’économie, ou la continuité des fonctions essentielles de l’État. La définition juridique précise dépend de la juridiction.

**En France** — cadre **OIV** (Opérateurs d’Importance Vitale) : défini par le Code de la défense (articles L.1332-1 et suivants). Les OIV sont désignés par l’État dans **12 secteurs d’activité d’importance vitale** (SAIV) — alimentation, communications électroniques/audiovisuel, eau, énergie, espace, finances, industrie, santé, transport, auxiliaires de l’État, services judiciaires, activités économiques et sociales de l’État. Les OIV ont des obligations de sécurité, notifient les incidents, et peuvent faire l’objet de contrôles ANSSI. Environ 300 OIV en France.

**En Europe — NIS 2** (Directive 2022/2555) : successeur de la directive NIS 1 (2016). Entrée en vigueur en octobre 2024, transposition en cours dans les États membres. Élargit considérablement le périmètre : **entités essentielles** (EE) et **entités importantes** (EI) dans 18 secteurs (énergie, transport, banque, santé, fourniture d’eau, infrastructures numériques, administration publique, espace, services postaux, gestion des déchets, fabrication/distribution de produits chimiques, production/transformation/distribution de denrées alimentaires, fabrication, fournisseurs numériques, recherche). Plusieurs dizaines de milliers d’entités couvertes à l’échelle européenne. Obligations : mesures techniques et organisationnelles, notification d’incidents, gouvernance cybersécurité au niveau direction, évaluations de risques de la supply chain.

**Aux États-Unis** — 16 **Critical Infrastructure Sectors** définis par la **Presidential Policy Directive 21** (PPD-21, 2013) : chemical, commercial facilities, communications, critical manufacturing, dams, defense industrial base, emergency services, energy, financial services, food and agriculture, government facilities, healthcare and public health, information technology, nuclear reactors/materials/waste, transportation systems, water and wastewater systems. CISA coordonne la protection.

**Autres juridictions** : l’**UK** a ses **Critical National Infrastructure** (13 secteurs), l’**Allemagne** ses **KRITIS**, le **Japon** et la **Corée du Sud** ont des cadres équivalents.

Point commun : les infrastructures critiques sont **définies par secteur** et sont soumises à des obligations de cybersécurité **renforcées**.

### 23.2 La visibilité minimum viable en OT

Pour un opérateur d’infrastructure critique, la visibilité est le prérequis de toute défense. Les sources minimales.

**Sur le segment IT (niveaux 4-5 Purdue)** :

- Sysmon sur les endpoints et serveurs critiques.
- PowerShell ScriptBlock logging.
- Authentification AD (sécurité events).
- DNS (requêtes sortantes, réponses).
- Firewall et proxy (flux sortants).
- EDR déployé sur les endpoints et les serveurs (y compris les servers de production IT).
- Email gateway (pour détecter le phishing).
- Identity / cloud (Azure AD/Entra, applications OAuth, anomalies d’authentification).

**Sur la DMZ industrielle (entre niveaux 3-4)** :

- Logs des firewalls DMZ.
- Trafic autorisé / bloqué.
- Logs des serveurs de jump host si présents.

**Sur le segment OT (niveaux 1-3 Purdue)** :

- **Passive monitoring OT** (Claroty, Dragos, Nozomi, Microsoft Defender for IoT) connecté via mirror ports ou network taps aux segments OT.
- Logs des engineering workstations (Sysmon + PowerShell logging quand l’OS le permet).
- Logs des HMI et historian (quand ils existent et sont accessibles).
- **Audit trails sur les PLC récents** (les PLC modernes permettent de logger les modifications de configuration).

**Centralisation** : l’ensemble devrait remonter vers un **SIEM centralisé** qui corrèle les signaux IT et OT. Les SOC matures ont des **cas d’usage spécifiques OT** dans leur detection engineering.

### 23.3 Segmentation IT/OT

La **segmentation** reste le pilier central de la sécurité OT. Principes.

**Segmentation physique** : idéalement, le réseau OT est physiquement séparé du réseau IT — pas de câbles partagés, pas de switches communs. En pratique, la segmentation physique totale est rare ; la **segmentation logique via VLANs et firewalls** est la norme.

**DMZ industrielle** : zone tampon entre IT et OT qui implémente des contrôles stricts :

- Pas de trafic direct IT → OT ni OT → IT.
- Tous les flux transitent par des **proxies applicatifs** ou des **serveurs de rebond** placés dans la DMZ.
- Les serveurs DMZ sont durcis (pas d’outils admin inutiles, monitoring poussé).
- Authentification forte sur tous les accès DMZ.

**Diodes unidirectionnelles** : pour les flux les plus sensibles (typiquement historian → IT pour le reporting), des **data diodes** (hardware qui physiquement ne laisse passer le trafic que dans un sens) garantissent l’unidirectionnalité. Utilisées notamment dans les centrales nucléaires.

**Micro-segmentation au sein de l’OT** : au-delà de la segmentation IT/OT, segmenter aussi les sous-ensembles OT — les SIS doivent être isolés des autres segments OT. Les sous-stations électriques entre elles peuvent être segmentées.

**Jump hosts durcis** : les postes qui sont forcément double-connectés (engineering workstations, postes de supervision) doivent être **durcis au maximum** — EDR, MFA, monitoring renforcé, séparation des sessions IT et OT (utilisateurs différents pour chaque environnement, pas de copier-coller entre les deux).

### 23.4 Détection comportementale OT

La détection OT ne peut pas reposer sur des signatures de malware comme en IT. Elle repose sur la **détection comportementale**.

**Établissement de baselines** :

- Quels équipements communiquent avec quels autres équipements ? (graphe de communication normal).
- Quels protocoles sont utilisés sur quels liens ? (Modbus sur tel segment, IEC 104 sur tel autre).
- Quelles commandes sont typiquement envoyées ? (lecture de registres normale, écriture de configuration exceptionnelle).
- Quelles sont les plages horaires d’activité normale ?

**Détection d’anomalies** :

- Nouveau flux entre équipements qui ne communiquaient pas auparavant.
- Nouveau protocole observé (IEC 104 sur un segment qui n’en utilisait pas).
- Commandes d’écriture vers des registres critiques (modifications de configuration PLC) — devraient être rares et correspondre à des plans de maintenance documentés.
- Activité en dehors des plages horaires.
- Équipement inconnu détecté sur le réseau.

**Détection des TTP documentées** : les vendors OT (Claroty, Dragos, Nozomi) embarquent des détections pour les TTP documentées — patterns d’Industroyer, de Triton, de Stuxnet, des campagnes Sandworm récentes. Ces détections doivent être activées et maintenues à jour.

**Threat hunting OT** : recherche proactive d’indicateurs subtils (modifications mineures de configurations PLC, présence d’outils d’administration inhabituels sur les engineering workstations, patterns de beaconing discret). Ressources dédiées nécessaires.

### 23.5 Collaboration avec les agences nationales

Les opérateurs d’infrastructures critiques sont rarement isolés face aux menaces APT. La collaboration avec les agences nationales est un pilier.

**Agences par pays** :

- **France — ANSSI** : qualifie les prestataires (PASSI, PDIS, PRIS), publie des advisories (CERT-FR), conduit des investigations, accompagne les OIV.
- **Allemagne — BSI** (Bundesamt für Sicherheit in der Informationstechnik) : rôle équivalent.
- **Royaume-Uni — NCSC** : Active Cyber Defence, Early Warning, Cyber Essentials.
- **Pays-Bas — NCSC-NL**.
- **Italie — ACN** (Agenzia per la Cybersicurezza Nazionale).
- **États-Unis — CISA** : advisories, KEV, Secure by Design, ShieldsUp.

**Types de collaboration** :

- **Partage de renseignement** : l’agence transmet des IoC, des TTP, des alertes sur des acteurs pertinents pour le secteur.
- **Support à l’investigation** : en cas d’incident majeur, l’agence peut déployer des experts.
- **Validation des dispositifs** : les qualifications (PASSI, PDIS, SecNumCloud en France) permettent aux opérateurs de faire confiance à des prestataires validés.
- **Exercices nationaux** : les agences conduisent des exercices (Piranet en France, CyberStorm aux US) qui testent les OIV dans des scénarios réalistes.

**Notification d’incidents** : NIS 2 impose des notifications sous 24h (early warning) et 72h (notification détaillée) pour les incidents significatifs. Ces notifications alimentent la vue d’ensemble nationale et permettent la coordination sur des campagnes qui touchent plusieurs acteurs.

### 23.6 ISAC sectoriels

Les **ISAC** (Information Sharing and Analysis Centers) sont des structures de partage d’information **par secteur**. Complètent les CERT nationaux avec un focus métier.

**ISAC européens et internationaux** :

- **E-ISAC** (Electricity ISAC, North America) : secteur électrique.
- **EE-ISAC** (European Energy ISAC) : énergie européenne.
- **FS-ISAC** (Financial Services ISAC) : finance, global.
- **H-ISAC** (Health ISAC) : santé.
- **IT-ISAC** : IT et télécom.
- **ICT-ISAC** : ICT européen.
- **Auto-ISAC** : automobile.
- **Aviation ISAC**, **Maritime ISAC**, etc.

**En France** : **InterCERT France** (coordonne les CERT privés), **CLUSIF**, et plusieurs groupements sectoriels.

**Utilité** : partage rapide d’IoC et de TTP entre acteurs du même secteur, benchmarking des pratiques, exercices sectoriels, dialogue avec les autorités. Un opérateur qui voit une TTP inhabituelle peut la partager avec ses pairs du secteur et découvrir que cinq autres ont vu la même — ce qui change l’interprétation (attaque sectorielle ciblée plutôt qu’incident isolé).

**Règles de partage** : utilisation du **TLP** (Traffic Light Protocol) pour calibrer la diffusion (RED, AMBER, GREEN, CLEAR). Anonymisation des victimes quand nécessaire.

### 23.7 Exercices cyber-OT

Les exercices sont la méthode principale pour **tester la résilience réelle**, pas seulement la résilience sur le papier.

**Niveaux d’exercice** :

- **Tabletop** : scénario discuté autour d’une table, pas d’action technique. Teste la coordination, les procédures, les décisions. Format typique : 2-4 heures, facilité par un animateur, implique les niveaux techniques et direction.
- **Fonctionnel / simulation** : plus approfondi, peut inclure des actions sur des environnements de test. Teste les capacités techniques et organisationnelles.
- **Full-scale / live** : exercice sur les vrais systèmes (en environnement contrôlé), avec injection réelle de scenarios. Teste la détection et la réponse sous conditions opérationnelles.

**Exercices nationaux / européens** :

- **Cyber Europe** (ENISA, tous les 2 ans) : exercice paneuropéen sur des scénarios cyber majeurs.
- **Piranet** (France, ANSSI) : exercice national de crise cyber.
- **CyberStorm** (US, CISA) : équivalent américain.
- **Locked Shields** (CCDCOE OTAN, Tallinn) : exercice technique de red/blue team au niveau OTAN.

**Scénarios OT spécifiques** : un bon exercice OT couvre :

- Le pivot IT → OT et sa détection.
- Le dilemme éradication vs surveillance d’un pré-positionnement.
- L’activation pendant un exercice (attaquant qui tente de manipuler un PLC).
- La communication de crise externe (public, autorités, média).
- La coordination avec les agences et les ISAC.

**Fréquence recommandée** : tabletop annuel, exercice fonctionnel biennal, full-scale tous les 3-5 ans — adapté à la maturité et aux moyens de l’organisation.

### 23.8 Le rôle du RSSI face au pré-positionnement

Pour le **RSSI** (Responsable de la Sécurité des Systèmes d’Information) d’une infrastructure critique, le pré-positionnement change la nature de la mission. Quelques principes opérationnels.

**Communiquer la menace auprès de la direction** : le pré-positionnement est abstrait pour un dirigeant non-cyber. Il faut traduire — « un adversaire étatique peut, à un moment choisi, provoquer un blackout de X jours touchant Y clients, avec Z millions d’euros de pertes opérationnelles + perte de confiance + risque humain ». Le langage de l’impact métier est indispensable.

**Prioriser les investissements** : dans un contexte de ressources limitées, prioriser ce qui compte pour le pré-positionnement :

- **Visibilité IT et OT** : condition nécessaire pour détecter.
- **Durcissement des jump hosts et engineering workstations** : vecteur de pivot principal.
- **Segmentation IT/OT robuste** : limite la surface.
- **Monitoring identity cloud** : vecteur moderne critique.
- **Capacité d’investigation et d’éradication rapide** : soit en interne, soit via un retainer externe.

**Préparer la réponse** : exercices réguliers, plan IR formalisé, procédures de notification, contacts établis avec ANSSI/BSI/etc, retainer IR, relations avec les vendors CTI.

**Intégrer la menace dans la gestion des risques** : la probabilité d’un pré-positionnement par un acteur étatique doit être intégrée dans les évaluations de risque, pas seulement le risque ransomware ou le risque data breach.

**Accepter l’incertitude** : face à des acteurs comme Volt Typhoon ou Sandworm, le RSSI doit accepter qu’il ne sera jamais totalement invulnérable. L’objectif réaliste : rendre la détection rapide et l’éradication efficace, pas viser l’invulnérabilité.

**Collaborer activement** : échanger avec l’ISAC sectoriel, participer aux exercices nationaux, contribuer à la sensibilisation communautaire. La sécurité des infrastructures critiques est un **bien commun** — un incident qui touche un opérateur peut affecter tous les autres via le partage d’information.

-----
