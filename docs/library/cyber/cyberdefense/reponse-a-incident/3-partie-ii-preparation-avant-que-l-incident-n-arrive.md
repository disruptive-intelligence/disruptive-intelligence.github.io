---
title: 'PARTIE II — PRÉPARATION : AVANT QUE L''INCIDENT N''ARRIVE'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 3
chapters: 9
---

*La qualité de la réponse est déterminée à 80 % par la qualité de la préparation. Cette partie traite ce que la plupart des organisations négligent — et ce qui fait la différence le jour J.*

---

### Chapitre 5 — Pourquoi la préparation détermine tout

#### 5.1 Le constat récurrent des retex

Dans la quasi-totalité des post-mortems d'incidents majeurs, les problèmes les plus graves ne sont pas techniques mais organisationnels. L'IRP existait mais n'avait jamais été testé — le jour J, personne ne savait où le trouver ni comment l'appliquer. Les contacts d'escalade étaient obsolètes — le RSSI avait changé de numéro 6 mois plus tôt. Les logs critiques n'étaient pas collectés — le PowerShell script block logging n'était pas activé, rendant l'investigation sur le mouvement latéral quasi impossible. Les sauvegardes étaient sur le même réseau que les serveurs de production — le ransomware les a chiffrées en même temps. Le canal de communication de crise n'était pas prévu — quand le serveur de messagerie a été chiffré, l'équipe s'est retrouvée sans moyen de communiquer.

Ces défaillances ne sont pas des « malchances » — ce sont des défauts de préparation identifiables et corrigeables avant l'incident. Chaque euro investi dans la préparation en économise dix ou cent en réponse.

#### 5.2 Les trois dimensions de la préparation

La préparation technique couvre les outils, les logs, les sauvegardes, la capacité d'isolation réseau, et les accès d'urgence. La préparation organisationnelle couvre les processus (IRP, playbooks, escalade), les rôles (qui fait quoi), les contrats (prestataire PRIS, assurance, exercices), et les relations (ANSSI, forces de l'ordre, CERT sectoriel). La préparation humaine couvre la formation (les analystes savent-ils utiliser Volatility ?), les réflexes (le SOC sait-il qu'il ne faut pas redémarrer un serveur compromis ?), et la capacité à fonctionner sous stress (l'IR lead a-t-elle déjà géré un incident majeur, même en exercice ?).

Négliger une seule dimension rend les deux autres insuffisantes. Un SIEM parfaitement configuré ne sert à rien si personne ne sait lire les alertes. Un IRP impeccable ne sert à rien si les logs ne sont pas collectés. Une équipe brillante ne sert à rien si elle n'a pas les outils pour investiguer.

#### 5.3 Le plan de réponse à incident (IRP)

L'IRP est le document fondateur de la capacité IR d'une organisation. Il doit contenir le périmètre d'application (quels systèmes, quels sites, quels processus sont couverts), la taxonomie des incidents adoptée (cohérente avec la classification du Ch.1), les critères de classification et de gravité (P1 à P4, avec des critères objectifs et des exemples), les critères de bascule en crise (repris du Ch.3), les rôles et contacts (à jour — c'est le point le plus souvent défaillant), les playbooks par type d'incident (ou pointeurs vers les playbooks séparés — Ch.7), les procédures d'escalade (qui appelle qui, dans quel ordre, avec quels critères), les modèles de communication pré-rédigés (premier message aux employés, premier SitRep à la direction, notification ANSSI, notification CNIL), les listes de diffusion (qui doit être informé à chaque niveau de gravité), et les arbres de décision (couper le réseau ? notifier l'ANSSI ? activer l'assurance ?).

Un IRP opérationnel fait 10 à 20 pages, pas 85. Il est stocké hors du SI principal (version papier, clé USB, cloud personnel du RSSI) car le SI peut être indisponible pendant l'incident. Il est mis à jour au minimum semestriellement et après chaque incident. Et il est testé en exercice au moins une fois par an (Ch.10).

> **Piège fréquent :** L'IRP « vitrine » — un document de 100 pages, magnifiquement rédigé, validé par la direction, rangé dans un tiroir, et jamais lu par les opérationnels. Le jour de l'incident, personne ne l'ouvre. Un IRP efficace est court, concret, et connu de tous les acteurs.

#### 5.4 Fil rouge — BLACKTIDE : l'état de préparation d'Arvantis

> **🔍 BLACKTIDE — Épisode 5**
>
> L'IRP d'Arvantis existe — un document de 85 pages rédigé 2 ans plus tôt par un consultant externe, validé par la direction, stocké sur SharePoint. Il n'a jamais été testé en conditions réelles. Le numéro du prestataire PRIS est à jour. Celui de l'ANSSI aussi. Le numéro personnel du DPO a changé il y a 3 mois — l'IRP n'a pas été mis à jour. Nadia l'a dans son téléphone — elle le retrouve. Par chance.
>
> L'IRP couvre les grandes lignes (escalade, classification, notification) mais ne contient pas de playbook ransomware détaillé. Il ne mentionne pas la procédure de double reset du krbtgt. Il ne traite pas l'articulation IT/OT. Et surtout : il est stocké sur SharePoint, qui est hébergé sur l'infrastructure Microsoft 365 d'Arvantis — si l'attaquant avait compromis le tenant M365, l'IRP aurait été inaccessible.

---

### Chapitre 6 — Gouvernance et organisation IR

#### 6.1 L'équipe IR : composition et rôles

L'**IR lead** (ou incident commander) coordonne l'ensemble de la réponse. Il maintient la vision d'ensemble, assigne les questions aux analystes, arbitre les priorités, fait l'interface avec la direction et le RSSI, et documente les décisions. Dans une PME, c'est souvent le RSSI lui-même. Dans un grand groupe, c'est un rôle dédié au sein du CSIRT.

Les **analystes forensic** mènent l'investigation technique sur les endpoints : acquisition de preuves (RAM, disques, artefacts), analyse des artefacts système, analyse de malware first-pass, et production des IoC. Compétences requises : maîtrise des outils forensic (KAPE, Velociraptor, Volatility, FTK Imager), connaissance approfondie des artefacts Windows et Linux.

Les **analystes logs/réseau** analysent les logs centralisés (SIEM), les flux réseau (pare-feu, proxy, DNS, NDR), et construisent la timeline par corrélation des sources. Compétences requises : maîtrise du SIEM (requêtes SPL, KQL, ou ELK), compréhension des protocoles réseau, capacité de corrélation multi-sources.

L'**analyste CTI** contextualise la menace : identification de l'adversaire (groupe, plateforme RaaS, TTP connues), enrichissement des IoC (hash, domaines, IP — sont-ils connus ? associés à quelle campagne ?), et anticipation des comportements (si c'est un affilié PhantomCrypt, quels mécanismes de persistance sont typiques ?). Renvoi vers le cours CTI et le cours Cartographie des Écosystèmes.

Le **représentant IT/infra** apporte la connaissance du SI (architecture, systèmes critiques, dépendances), exécute les actions techniques décidées par l'IR lead (isolation réseau, reset de comptes, restauration), et identifie les impacts opérationnels des actions proposées.

Le **RSSI** fait l'interface entre la cellule technique et la direction. Il traduit la situation technique en termes business, valide les décisions à impact stratégique, et porte la responsabilité managériale de la réponse.

Ces rôles peuvent être portés par 3 personnes dans une PME ou 15 dans un grand groupe. Ce qui compte n'est pas le nombre de personnes mais le fait que chaque fonction soit assignée explicitement à quelqu'un qui sait ce qu'on attend de lui.

#### 6.2 CSIRT interne vs prestataire PRIS

La décision entre réponse interne et mobilisation d'un prestataire qualifié PRIS dépend de plusieurs critères. La nature de l'incident (un phishing simple peut être traité en interne ; un ransomware avec compromission de l'AD nécessite presque toujours un PRIS), les compétences disponibles (l'organisation a-t-elle un forensicien capable d'analyser un dump mémoire de DC à 3h du matin un samedi ?), la charge (même si les compétences existent, l'équipe peut être submergée), le besoin d'indépendance (pour la plainte pénale, un rapport d'un tiers qualifié est plus crédible), et les exigences d'assurance (certaines polices imposent le recours à un PRIS de leur liste).

Le prestataire PRIS ne connaît pas le SI de l'organisation. Le temps d'on-boarding (comprendre l'architecture, les accès, les noms des serveurs, les personnes à contacter) est incompressible et peut prendre plusieurs heures, voire une demi-journée. Ce temps doit être anticipé : un document de synthèse du SI (architecture réseau, liste des systèmes critiques, comptes d'administration, outils de sécurité déployés) doit être préparé à l'avance et remis au PRIS dès son arrivée.

Le référentiel PRIS v3.2 de l'ANSSI (octobre 2025) qualifie les prestataires sur cinq activités : recherche d'indicateurs de compromission, investigation numérique, analyse de codes malveillants, pilotage et coordination des investigations, et gestion de crise d'origine cyber.

#### 6.3 Chaîne d'escalade et RACI

La chaîne d'escalade définit qui appelle qui, dans quel ordre, avec quels critères de déclenchement. Elle doit être simple (pas plus de 3 niveaux pour atteindre le décideur), redondante (si le contact principal ne répond pas, qui est le suppléant ?), et testée régulièrement (voir Ch.10).

Le RACI de l'IR (Responsible, Accountable, Consulted, Informed) doit être défini avant l'incident. Qui est responsable de la décision de confinement réseau ? (typiquement : IR lead propose, RSSI valide). Qui est responsable de la notification ANSSI ? (typiquement : RSSI). Qui est responsable de la communication interne ? (typiquement : direction de la communication, validée par le RSSI et le juridique). L'ambiguïté des rôles pendant un incident est une source majeure de paralysie (personne ne décide) ou de décisions contradictoires (deux personnes décident des choses incompatibles). Un RACI type est proposé en Annexe G.

#### 6.4 Modèle de permanence et astreinte

La réalité opérationnelle de l'IR est que l'incident n'arrive jamais à un moment pratique. L'alerte tombe le vendredi soir, l'expert AD est en vacances à l'étranger, le RSSI est dans un avion. Le modèle de permanence doit anticiper ces situations : astreinte formalisée (qui est joignable 24/7, avec quel délai de réponse), suppléances (si l'astreinte primaire ne répond pas dans les 15 minutes, qui prend le relais), et procédure de rappel d'effectifs (comment mobiliser l'équipe complète un dimanche matin).

La fatigue est un enjeu sous-estimé. Un incident majeur dure des jours, parfois des semaines. Les premières 24-48 heures sont intenses (adrénaline, urgence), mais au-delà, la fatigue dégrade la qualité des décisions, augmente le risque d'erreur, et peut conduire à des conflits interpersonnels. La rotation des équipes (shifts de 8 à 12 heures maximum, avec passage de relais structuré) est un enjeu de santé ET de qualité de réponse.

#### 6.5 Fil rouge — BLACKTIDE : la mobilisation

> **🔍 BLACKTIDE — Épisode 6**
>
> Nadia (IR lead) est d'astreinte ce week-end — elle répond en 3 minutes. Marc (RSSI) est d'astreinte — il répond en 2 sonneries. Le prestataire PRIS CyberForce est mobilisé à 23h30 — le consultant senior forensic, Thomas Hartmann, et un consultant spécialiste AD, Léa Chen, seront sur site samedi à 08h15 (SLA contractuel : 12h le week-end).
>
> L'expert AD interne d'Arvantis, Youssef Benmoussa, est en congé en Tunisie. Il est injoignable par téléphone (pas de réseau dans la zone). Il sera briefé par visioconférence dimanche matin quand il retrouvera du réseau. En attendant, Léa Chen (PRIS) couvrira l'analyse AD.
>
> L'analyste SOC N2, Karim, est en poste depuis 14h (début de shift à 14h). À 02h, cela fait 12 heures qu'il travaille. Nadia lui demande de rester encore 2 heures pour le passage de relais au N2 suivant, puis de dormir. L'analyste suivant, Fatima Zeroual, prend le relais SOC à 04h.

---

### Chapitre 7 — Playbooks et procédures opérationnelles

#### 7.1 Qu'est-ce qu'un playbook IR

Un playbook IR est un document opérationnel, court (5 à 10 pages maximum), qui décrit les actions concrètes à mener pour un type d'incident spécifique. Ce n'est pas l'IRP (qui est le cadre général de la capacité IR) — c'est la procédure détaillée pour un cas précis, avec des actions numérotées, des responsables identifiés, des seuils de décision, et des pointeurs vers les outils et commandes à utiliser.

Le playbook est le document que l'analyste ouvre à 3h du matin quand il est fatigué et stressé. Il doit être immédiatement actionnable : pas de prose de 3 pages avant la première action, pas de jargon inutile, pas de renvois vers 10 autres documents. L'action 1 doit pouvoir être exécutée dans les 5 premières minutes.

#### 7.2 Playbooks essentiels

Chaque organisation doit disposer au minimum des playbooks suivants, adaptés à son contexte.

**Playbook phishing** : trigger (alerte utilisateur ou détection email malveillant), actions immédiates (extraction des IoC : URL, pièce jointe, expéditeur ; recherche dans les boîtes mail de tous les destinataires ; isolation du poste de l'utilisateur qui a cliqué), investigation (le lien a-t-il été cliqué ? les credentials ont-elles été saisies ? le malware a-t-il été exécuté ?), confinement (blocage du domaine/hash au niveau proxy/EDR, reset du mot de passe si credentials compromises), et communication (notification aux utilisateurs touchés).

**Playbook ransomware** : trigger (détection EDR ou découverte de fichiers chiffrés), actions immédiates (isolation réseau des systèmes touchés — NE PAS éteindre avant collecte), évaluation (quel variant ? quel périmètre ? les sauvegardes sont-elles intactes ? le DC est-il compromis ?), confinement réseau (voir Ch.23), collecte forensic (RAM + triage KAPE avant tout reset), notification (ANSSI si OIV, CNIL si données personnelles), et décision sur la rançon (voir Ch.32).

**Playbook compromission de compte** : trigger (alerte SIEM sur comportement anormal, notification de geo-impossible travel, signalement utilisateur), actions (désactivation immédiate du compte, reset mot de passe, révocation des sessions actives et tokens OAuth, recherche d'activité suspecte : règles de forwarding email, accès aux données, création de comptes, modifications de configuration).

**Playbook malware** : trigger (détection EDR/antivirus), actions (isolation du poste via EDR containment, collecte du sample pour analyse, soumission sandbox, recherche de propagation latérale — le même hash est-il détecté sur d'autres machines ?), classification (commodity malware vs ciblé, infostealer vs RAT vs ransomware).

**Playbook exfiltration de données** : trigger (alerte DLP, volume anormal de trafic sortant, notification externe), investigation (quelles données ? quel volume ? vers quelle destination ?), confinement (blocage du canal d'exfiltration), et notification (CNIL si données personnelles, sous 72h).

**Playbook compromission cloud** : trigger (alerte Entra ID / CloudTrail), investigation (Sign-in Logs pour les accès anormaux, Unified Audit Log pour les actions, app registrations suspectes, conditional access policies modifiées), confinement (révocation de tokens, reset MFA, désactivation des app registrations suspectes).

Les playbooks détaillés avec les commandes concrètes sont en Annexe E.

#### 7.3 Concevoir un bon playbook

Structure type d'un playbook opérationnel :

**En-tête :** nom du playbook, version, date de dernière mise à jour, auteur, conditions de déclenchement (trigger).

**Actions immédiates** (0-15 minutes) : ce que l'analyste de garde doit faire sans attendre de validation. Chaque action a un responsable et un livrable.

**Actions d'investigation** (15 min - 4 heures) : les vérifications et analyses nécessaires pour qualifier l'incident et décider du confinement. Inclut les commandes concrètes (requêtes SIEM, commandes EDR, scripts de collecte).

**Actions de confinement** : les mesures de limitation de la progression, avec les critères de décision (quand isoler, quand couper, quand observer).

**Critères d'escalade** : à quel moment et vers qui escalader si la gravité s'avère supérieure à la classification initiale.

**Actions de communication** : qui informer, quand, avec quel message type.

**Actions de clôture** : vérifications post-résolution, documentation, et lien vers le RETEX.

#### 7.4 Maintenir les playbooks vivants

Un playbook non testé est un playbook mort. Les playbooks doivent être testés en exercice (Ch.10), révisés après chaque incident où ils ont été utilisés (le RETEX identifie les actions manquantes ou inadaptées), et mis à jour quand l'environnement change (nouveau SIEM, nouvel EDR, changement d'architecture, nouveau type de menace).

Fréquence de révision recommandée : après chaque utilisation en incident réel, après chaque exercice, et au minimum une fois par an même sans utilisation.

#### 7.5 Fil rouge — BLACKTIDE : le playbook ransomware insuffisant

> **🔍 BLACKTIDE — Épisode 7**
>
> Arvantis a un playbook ransomware — incomplet. Il décrit les actions de confinement réseau (isolation VLAN, coupure Internet) mais ne couvre pas le cas d'un AD compromis en profondeur (pas de procédure de double reset krbtgt, pas de procédure de reconstruction DC). Il ne mentionne pas l'articulation avec l'ANSSI en cas d'OIV impacté. Il ne traite pas le cas spécifique de l'environnement OT (comment confiner le réseau sans arrêter les automates SCADA ?). Et il n'a jamais été testé en exercice.
>
> Nadia l'utilise comme base mais doit improviser sur environ 40 % des actions. Elle note dans le journal : « Playbook ransomware utilisé — lacunes identifiées : pas de procédure AD compromis, pas de volet OT, pas de volet notification OIV. À mettre à jour en RETEX. »

---

### Chapitre 8 — Préparation technique : outillage et télémétrie

#### 8.1 Les outils qui doivent être en place AVANT l'incident

**EDR (Endpoint Detection and Response)** : déployé sur TOUS les endpoints — pas 85 %, pas 92 %, tous. Chaque machine non couverte est un angle mort dans lequel l'attaquant peut se cacher sans être détecté. L'EDR est le premier capteur de l'investigation (il fournit la telemetry qui reconstitue les actions de l'attaquant) et le premier outil de confinement (network containment, kill process). Les leaders du marché en 2025-2026 incluent CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, et Palo Alto Cortex XDR. Le choix dépend du contexte (environnement, budget, intégration avec le SIEM), mais la couverture à 100 % est non négociable.

**SIEM (Security Information and Event Management)** : collecte centralisée des logs critiques avec capacité de recherche et de corrélation. Les sources minimales à collecter : Windows Event Logs (Security, System, PowerShell, Sysmon si déployé), logs Active Directory (réplication, modifications d'objets), logs pare-feu (flux autorisés et refusés), logs proxy (URLs, user-agents, volumes), logs DNS (résolutions), logs VPN (connexions), et logs des solutions de sécurité (EDR, antivirus). Les plateformes courantes : Splunk, Microsoft Sentinel, Elastic Security (ELK), QRadar, Chronicle (Google). Le choix dépend du volume de logs, du budget, et des compétences disponibles.

**NDR (Network Detection and Response)** : pas obligatoire mais extrêmement précieux. Le NDR capture et analyse le trafic réseau en temps réel, détecte les anomalies (beaconing, exfiltration, mouvement latéral), et fournit une visibilité que les logs endpoint et SIEM ne donnent pas (notamment sur les systèmes sans EDR — serveurs legacy, équipements réseau, systèmes OT).

**Outils de collecte forensic pré-packagés** : clés USB bootables contenant KAPE (collecte automatisée d'artefacts Windows), Velociraptor (collecte et hunting à grande échelle), DumpIt ou WinPmem (acquisition mémoire), et des scripts de triage personnalisés. Ces kits doivent être prêts à l'emploi, testés, et accessibles physiquement (pas sur un partage réseau qui sera chiffré).

#### 8.2 Rétention des logs

La durée de rétention des logs détermine la profondeur de l'investigation. Le dwell time médian (temps entre la compromission et la détection) est de 10 à 15 jours pour les ransomwares, mais peut atteindre des mois pour l'espionnage. Si les logs ne sont conservés que 30 jours et que l'attaquant est dans le réseau depuis 5 semaines, les traces du patient zéro sont perdues.

Minimum recommandé : 6 mois de rétention sur le SIEM chaud (recherche immédiate), 12 mois en stockage froid (archivage consultable). Pour les environnements à risque élevé (OIV, secteur financier, défense) : 12 mois chaud, 24 mois froid.

Le cas critique de Microsoft 365 : la rétention des Unified Audit Logs dépend de la licence. En E3 (la licence la plus courante en entreprise), la rétention est de 180 jours (améliorée par Microsoft en 2023, contre 90 jours auparavant pour certains types de logs). En E5, la rétention peut aller jusqu'à 365 jours. Cette différence est critique pour l'investigation — et elle est souvent découverte trop tard, au moment de l'incident.

#### 8.3 Horodatage, sauvegardes, isolation et accès d'urgence

**Synchronisation NTP :** si les horloges des machines ne sont pas synchronisées, la corrélation des événements entre sources est impossible. La synchronisation NTP sur tous les systèmes est un prérequis trivial mais souvent négligé.

**Sauvegardes :** les sauvegardes doivent être segmentées du réseau principal (pas un NAS sur le même VLAN — le ransomware le chiffrera en même temps que les serveurs), testées régulièrement (une sauvegarde non testée est une promesse non vérifiée), et idéalement immuables (stockage WORM, cloud avec versioning et MFA delete protection) ou offline (bandes magnétiques, rotation hebdomadaire). Le ransomware cible systématiquement les sauvegardes — c'est même souvent sa première cible après la compromission de l'AD, car l'attaquant sait que la volonté de payer la rançon est directement proportionnelle à l'indisponibilité des sauvegardes.

**Capacité d'isolation réseau :** VLAN de quarantaine pré-configuré, ACL pare-feu prêtes à être activées (pas à écrire en urgence à 3h du matin), capacité d'isolation via EDR (network containment à distance), et éventuellement un kill switch réseau (coupure totale de l'accès Internet en un clic — procédure documentée et testée).

**Comptes et accès d'urgence :** comptes d'administration « break glass » (non synchronisés avec l'AD principal, stockés de manière sécurisée — coffre-fort physique, gestionnaire de mots de passe hors SI), accès console aux équipements réseau (si le réseau est compromis, les accès in-band via SSH ou HTTPS peuvent être inaccessibles), et accès physique aux datacenters (badges, clés).

#### 8.4 Fil rouge — BLACKTIDE : forces et faiblesses techniques

> **🔍 BLACKTIDE — Épisode 8**
>
> **Forces :** EDR CrowdStrike Falcon déployé sur 92 % du parc (les 3 DC compromis sont couverts — c'est ce qui a permis la détection). SIEM Splunk avec 9 mois de rétention (suffisant pour remonter au patient zéro à J-35). Horodatage NTP synchronisé sur tout le parc. Logs pare-feu conservés 12 mois.
>
> **Faiblesses :** 8 % du parc sans EDR (postes legacy, serveurs OT, équipements réseau — autant d'angles morts). Pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu). Microsoft 365 en licence E3 (rétention UAL de 180 jours — suffisant pour cet incident, mais pas pour un espionnage long terme). Sauvegardes quotidiennes sur NAS réseau, sur le même VLAN que les serveurs de fichiers (elles seront partiellement chiffrées par le ransomware). Sauvegardes hebdomadaires sur bandes offline (intactes — seule sauvegarde exploitable, mais avec 6 jours de perte de données). Comptes break glass : inexistants. PowerShell script block logging : non activé sur tous les postes (activé uniquement sur les serveurs — lacune sur les postes de travail).

---

### Chapitre 9 — Préparation juridique, réglementaire et contractuelle

#### 9.1 Obligations de notification

Le paysage réglementaire français impose plusieurs obligations de notification en cas d'incident cyber, avec des délais et des destinataires différents.

**ANSSI — OIV :** les Opérateurs d'Importance Vitale doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels (variable selon le secteur, mais typiquement « sans délai » pour les incidents majeurs). La notification est obligatoire, et le non-respect peut entraîner des sanctions. L'ANSSI peut déployer des équipes du CERT-FR en appui.

**NIS 2 — Entités essentielles et importantes :** la directive NIS 2, en cours de transposition en France via la « Loi Résilience » (adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, adoption finale attendue début 2026), imposera une notification initiale sous 24 heures (alerte préliminaire indiquant qu'un incident significatif a été détecté) et une notification complète sous 72 heures (analyse de l'incident, impact, mesures prises). Les entités concernées sont considérablement plus nombreuses qu'avec NIS 1 : environ 15 000 entités en France, réparties en « entités essentielles » et « entités importantes » selon leur secteur et leur taille. Les sanctions prévues sont significatives (amendes administratives pouvant atteindre 10 M€ ou 2 % du CA mondial pour les entités essentielles).

**CNIL — Violations de données personnelles :** notification sous 72 heures après la « prise de connaissance » de la violation (article 33 du RGPD). La « prise de connaissance » n'est pas le moment de la détection de l'incident, mais le moment où l'organisation acquiert une certitude raisonnable que des données personnelles sont compromises. La notification doit décrire la nature de la violation, les catégories de données concernées, le nombre de personnes touchées, les conséquences probables, et les mesures prises. Si la violation présente un risque élevé pour les personnes (données de santé, données bancaires, données permettant l'usurpation d'identité), la notification aux personnes concernées est également obligatoire (article 34 du RGPD).

**Forces de l'ordre :** le dépôt de plainte n'est pas une obligation réglementaire mais une recommandation forte, et il est souvent nécessaire pour activer l'assurance cyber. La plainte se fait auprès du procureur de la République (parquet de Paris, section J3 cybercriminalité pour les affaires complexes). Le dépôt de plainte ne nécessite pas d'avoir terminé l'investigation — il peut être fait dès que l'incident est confirmé, avec les éléments disponibles à ce stade.

La préparation de ces notifications en amont (templates pré-rédigés en Annexe C, contacts identifiés, processus documenté) accélère considérablement la réponse le jour J.

#### 9.2 Cadre contractuel des prestataires et assurance cyber

Le contrat avec le prestataire PRIS doit prévoir les SLA d'intervention (délai maximum entre l'appel et l'arrivée sur site ou la connexion à distance), le périmètre (quelles activités PRIS sont couvertes — toutes les 5 activités du référentiel ANSSI ?), les conditions de remontée d'information (que communique le PRIS au commanditaire, quand, sous quelle forme), les clauses de confidentialité (le PRIS a accès aux données les plus sensibles de l'organisation), et la responsabilité en cas de perte de preuve.

L'assurance cyber est un élément de plus en plus important de la préparation IR. Les points clés à connaître avant l'incident : les conditions d'activation (notification dans les délais — souvent 24 à 48h, préservation des preuves, non-aggravation), la couverture (frais de réponse à incident, perte d'exploitation, frais juridiques, frais de notification, communication de crise — et éventuellement la rançon, sujet controversé et variable selon les polices), les exclusions (actes de guerre, faute intentionnelle, certaines exclusions spécifiques), les plafonds et franchises, et la liste de prestataires agréés par l'assureur (vérifier la compatibilité avec le PRIS sous contrat).

#### 9.3 Conservation de preuve et recevabilité judiciaire

Les preuves collectées pendant l'IR peuvent être utilisées dans une procédure pénale (plainte pour accès frauduleux aux systèmes — art. 323-1 du Code pénal, extorsion — art. 312-1, destruction de données — art. 323-2) ou civile (action contre un prestataire défaillant, contentieux assurance). Pour être recevables, elles doivent respecter la chaîne de custody : documentation de chaque acquisition, calcul et vérification des hash SHA256, stockage sécurisé et intégrité vérifiable. Le détail de la chaîne de custody est traité au Ch.25.

#### 9.4 Fil rouge — BLACKTIDE : les obligations d'Arvantis

> **🔍 BLACKTIDE — Épisode 9**
>
> Arvantis est OIV sur 2 sites (Fos-sur-Mer et Lyon) → notification ANSSI obligatoire, effectuée le samedi 15 mars à 08h00. Données RH de 8 000 employés potentiellement exfiltrées (noms, adresses, RIB, numéros de sécurité sociale) → notification CNIL sous 72h, préparée par le DPO dès le samedi, envoyée le lundi 17 mars. Contrat PRIS en place avec CyberForce (SLA : 12h le week-end, couverture des 5 activités PRIS). Assurance cyber souscrite auprès d'AXA XL (plafond 5 M€, franchise 200 K€, exclusion rançon dans cette police, liste de prestataires agréés incluant CyberForce).

---

### Chapitre 10 — Exercices et entraînement

#### 10.1 Types d'exercices

Les **exercices tabletop** sont des simulations sur papier : un scénario est présenté (« il est 22h, le SOC détecte une alerte EDR sur un DC, que faites-vous ? »), les participants discutent leurs décisions, les processus sont testés sans manipulation technique. Efficace pour tester l'IRP, la chaîne d'escalade, la communication, et la coordination entre équipes. Peu coûteux, rapide à organiser (2 à 4 heures), et adapté à la sensibilisation de la direction.

Les **exercices techniques** sont des simulations en environnement de lab ou en production contrôlée : un malware est déployé (avec l'accord de la direction), un mouvement latéral est simulé, les analystes doivent détecter, investiguer, et confiner. Efficace pour tester les compétences techniques, l'outillage, et les playbooks. Plus coûteux (nécessite un environnement de test et un red team ou purple team), mais irremplaçable pour valider la capacité opérationnelle réelle.

Les **exercices de crise complets** impliquent la direction, la communication, le juridique, et les métiers — en plus de l'équipe technique. Le scénario inclut des éléments de pression réalistes : appel d'un journaliste (simulé), publication sur un faux leak site, pression des « clients » (acteurs de l'exercice). Efficace pour tester la gouvernance, la communication de crise, et la prise de décision stratégique. Lourd à organiser (une journée complète, préparation de plusieurs semaines), mais le seul moyen de tester la chaîne complète de la détection au RETEX.

#### 10.2 Fréquence et progression

Fréquence minimale recommandée : exercice tabletop trimestriel, exercice technique semestriel, exercice de crise complet annuel. Chaque exercice est suivi d'un retex structuré avec plan d'amélioration. La progression va du simple au complexe : d'abord un seul type d'incident avec l'équipe technique seule, puis des scénarios multi-vecteurs avec des parties prenantes multiples.

#### 10.3 Le test le plus simple et le plus révélateur

Appeler les numéros de la chaîne d'escalade un dimanche matin à 7h pour vérifier que quelqu'un répond, que la personne connaît son rôle, et qu'elle sait qui mobiliser ensuite. Résultat habituel : 30 à 50 % d'échec au premier essai (numéro qui ne répond pas, personne qui ne sait pas qu'elle est d'astreinte, personne qui ne connaît pas la procédure). Ce test coûte 30 minutes et révèle plus de failles que n'importe quel audit de 3 semaines.

#### 10.4 Fil rouge — BLACKTIDE : les exercices manqués

> **🔍 BLACKTIDE — Épisode 10**
>
> Arvantis avait prévu un exercice de crise cyber depuis 2 ans. Il a été reporté 4 fois (« pas le bon moment », « trop de projets en cours », « le budget est serré cette année », « on fera ça au prochain trimestre »). Le seul exercice réalisé est un tabletop basique il y a 18 mois, limité à l'équipe IT. La direction n'a jamais participé à un exercice de crise cyber.
>
> Conséquences : le CEO d'Arvantis découvre le fonctionnement d'une cellule de crise le samedi matin à 06h00, en situation réelle. Il ne comprend pas pourquoi « on ne peut pas simplement restaurer les sauvegardes et redémarrer ». Il ne connaît pas les obligations de notification ANSSI. Il est surpris par le coût du prestataire PRIS (« 2 500 € par jour et par consultant ?! »). Toutes ces surprises auraient été évitées par un exercice de crise incluant la direction.

---
