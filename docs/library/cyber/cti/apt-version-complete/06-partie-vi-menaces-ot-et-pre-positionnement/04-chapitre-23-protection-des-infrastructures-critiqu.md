---
title: Chapitre 23 — Protection des infrastructures critiques
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie VI — Menaces OT ET pré-positionnement
  - index.md
---

## 23.1 Cartographie des infrastructures critiques européennes

Les **infrastructures critiques** (IC) sont les infrastructures dont la disruption aurait des conséquences majeures pour la sécurité, la santé publique, l’économie, ou la continuité des fonctions essentielles de l’État. La définition juridique précise dépend de la juridiction.

**En France** — cadre **OIV** (Opérateurs d’Importance Vitale) : défini par le Code de la défense (articles L.1332-1 et suivants). Les OIV sont désignés par l’État dans **12 secteurs d’activité d’importance vitale** (SAIV) — alimentation, communications électroniques/audiovisuel, eau, énergie, espace, finances, industrie, santé, transport, auxiliaires de l’État, services judiciaires, activités économiques et sociales de l’État. Les OIV ont des obligations de sécurité, notifient les incidents, et peuvent faire l’objet de contrôles ANSSI. Environ 300 OIV en France.

**En Europe — NIS 2** (Directive 2022/2555) : successeur de la directive NIS 1 (2016). Entrée en vigueur en octobre 2024, transposition en cours dans les États membres. Élargit considérablement le périmètre : **entités essentielles** (EE) et **entités importantes** (EI) dans 18 secteurs (énergie, transport, banque, santé, fourniture d’eau, infrastructures numériques, administration publique, espace, services postaux, gestion des déchets, fabrication/distribution de produits chimiques, production/transformation/distribution de denrées alimentaires, fabrication, fournisseurs numériques, recherche). Plusieurs dizaines de milliers d’entités couvertes à l’échelle européenne. Obligations : mesures techniques et organisationnelles, notification d’incidents, gouvernance cybersécurité au niveau direction, évaluations de risques de la supply chain.

**Aux États-Unis** — 16 **Critical Infrastructure Sectors** définis par la **Presidential Policy Directive 21** (PPD-21, 2013) : chemical, commercial facilities, communications, critical manufacturing, dams, defense industrial base, emergency services, energy, financial services, food and agriculture, government facilities, healthcare and public health, information technology, nuclear reactors/materials/waste, transportation systems, water and wastewater systems. CISA coordonne la protection.

**Autres juridictions** : l’**UK** a ses **Critical National Infrastructure** (13 secteurs), l’**Allemagne** ses **KRITIS**, le **Japon** et la **Corée du Sud** ont des cadres équivalents.

Point commun : les infrastructures critiques sont **définies par secteur** et sont soumises à des obligations de cybersécurité **renforcées**.

## 23.2 La visibilité minimum viable en OT

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

## 23.3 Segmentation IT/OT

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

## 23.4 Détection comportementale OT

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

## 23.5 Collaboration avec les agences nationales

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

## 23.6 ISAC sectoriels

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

## 23.7 Exercices cyber-OT

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

## 23.8 Le rôle du RSSI face au pré-positionnement

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
