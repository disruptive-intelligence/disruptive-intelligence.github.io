---
title: Chapitre 20 — Architecture OT/ICS et protocoles industriels
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie VI — Menaces OT ET pré-positionnement
  - index.md
---

## 20.1 Qu’est-ce que l’OT : SCADA, DCS, PLC, HMI, historians, SIS

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

## 20.2 Le modèle Purdue et la segmentation par niveau

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

## 20.3 Protocoles industriels

Modbus, DNP3, IEC 60870-5-104, IEC 61850, OPC, PROFINET

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

## 20.4 Absence d’authentification native et risques associés

Reprenons le point central : la plupart des protocoles OT n’exigent **aucune authentification** pour émettre des commandes. Cette caractéristique a des conséquences directes sur la nature des attaques OT.

**Implication n°1 — Accès au réseau = capacité d’action** : si un attaquant pénètre le segment OT, il peut directement commander des équipements. Pas besoin de compromettre des credentials additionnels — la seule question est de connaître la carte du réseau et les adresses des équipements.

**Implication n°2 — Pas de trace forte** : sans authentification, il n’y a pas de log fiable de « qui a envoyé telle commande ». Les investigations post-incident doivent s’appuyer sur des corrélations réseau (quelle IP source, quelle timing), pas sur des logs applicatifs.

**Implication n°3 — Les mitigations sont réseau** : l’ensemble de la sécurité OT dépend massivement de la segmentation (qui peut parler à qui), de la surveillance (qui parle en temps réel), et du durcissement des points de passage (engineering workstations, jump hosts).

**Implication n°4 — Les équipements eux-mêmes ne se défendent pas** : un PLC qui reçoit une commande Modbus « écrire valeur 100 dans registre 40001 » l’exécute, quelle que soit la source. Il n’y a pas d’équivalent d’un antivirus ou d’un EDR sur un PLC historique. Les PLC récents commencent à intégrer des fonctions de sécurité, mais le parc déployé reste largement vulnérable.

## 20.5 Convergence IT/OT : causes, avantages, risques

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

## 20.6 Systèmes hérités : la problématique du patching et de l’EDR

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

## 20.7 Le modèle d’attaque OT classique

L’attaque OT typique suit une séquence prévisible. La connaître permet d’anticiper où placer les détections.

**Étape 1 — Accès initial via IT** : phishing, exploitation edge, supply chain — les vecteurs sont ceux des APT IT classiques. Les attaquants accèdent au réseau bureautique (niveau 4 Purdue).

**Étape 2 — Mouvement latéral dans l’IT** : reconnaissance AD, credential dumping, Kerberoasting, identification des cibles d’intérêt. L’objectif : identifier les comptes et les systèmes qui ont accès au réseau OT.

**Étape 3 — Identification du chemin vers l’OT** : recherche des engineering workstations, des jump hosts, des serveurs historian ayant des pieds dans les deux mondes. BloodHound peut révéler ces chemins.

**Étape 4 — Pivot vers l’OT** : compromission d’un engineering workstation ou d’un jump host, utilisation pour pénétrer le segment OT. **Cette étape est le point de rupture** — avant, l’attaquant est dans un environnement IT classique ; après, il est dans un environnement où les défenses classiques ne fonctionnent plus.

**Étape 5 — Reconnaissance OT** : identification des équipements présents (PLC, HMI, RTU, SIS), identification des protocoles utilisés, cartographie du processus industriel. **Cette phase est typiquement longue — semaines à mois** — car l’attaquant doit comprendre ce qu’il peut faire. Un PLC Siemens S7 dans une raffinerie contrôle un processus spécifique ; modifier ses paramètres a des effets spécifiques. L’attaquant doit apprendre le processus.

**Étape 6 — Préparation de l’action** : développement ou adaptation du code qui manipulera les équipements. Peut impliquer du reverse engineering de la logique de contrôle, des tests en environnement de staging.

**Étape 7 — Déclenchement** : envoi des commandes malveillantes. Peut être : manipulation directe des automates (Industroyer), modification de la logique de contrôle (Stuxnet), désactivation des SIS (Triton), simple coupure par ouverture de disjoncteurs (Ukraine 2015).

**Durée totale** : de l’accès initial au déclenchement, une opération OT sophistiquée prend **plusieurs mois à plusieurs années**. Cette longue phase de préparation est la raison pour laquelle la détection précoce dans la phase IT est critique — intervenir avant que l’attaquant n’atteigne l’OT est bien plus facile que de contenir une fois le pivot effectué.

## 20.8 Visibilité OT : passive monitoring

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

## 20.9 La protection des SIS : l’enjeu ultime

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
