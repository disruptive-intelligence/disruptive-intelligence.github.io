---
title: Annexe G — Cadres juridiques et réglementaires par juridiction
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Annexes
  - index.md
---

Cette annexe consolide les cadres juridiques, institutions, et qualifications mentionnés dans le cours. L’objectif est d’offrir un référentiel pour l’analyste confronté à un incident APT et devant naviguer dans les obligations et les points de contact pertinents.

## G.1 France

**ANSSI** — Agence nationale de la sécurité des systèmes d’information. Créée en 2009, rattachée au SGDSN (Secrétariat général de la défense et de la sécurité nationale). Mission : défense et sécurité des SI de l’État et des OIV, qualification de produits et prestataires, pilotage CERT-FR, coopération internationale. **N’a pas de mandat offensif** — pure posture défensive et d’accompagnement.

**COMCYBER** — Commandement de la cyberdéfense, créé en 2017 au sein du ministère des Armées. Mission : défense des systèmes militaires, **conduite des opérations cyber offensives (LIO)** pour le compte de l’État. Le COMCYBER intègre les capacités des trois armées et de la DGSE sur le volet cyber militaire.

**DGSE** — Direction générale de la sécurité extérieure. Service de renseignement extérieur rattaché au ministère des Armées. Dispose de capacités cyber intégrées à ses opérations, notamment pour le renseignement technique à l’étranger.

**DGSI** — Direction générale de la sécurité intérieure. Service de renseignement intérieur rattaché au ministère de l’Intérieur. Mission cyber : contre-espionnage cyber, contre-ingérence, investigation des menaces cyber contre la France.

**DRSD** — Direction du renseignement et de la sécurité de la défense. Service de contre-espionnage militaire, ministère des Armées.

**Coordinateur national pour le renseignement et la lutte contre le terrorisme (CNRLT)** : coordonne la communauté française du renseignement à l’Élysée.

**C4** — Centre de Coordination des Crises Cyber. Créé en 2021. Réunit ANSSI, COMCYBER, DGSE, DGSI, Police/Gendarmerie pour la coordination opérationnelle lors des crises cyber majeures.

**Doctrine cyber française** (publiée 2019) :

- **LID** (Lutte Informatique Défensive) : ANSSI.
- **LIO** (Lutte Informatique Offensive) : COMCYBER + DGSE.
- **L2I** (Lutte Informatique d’Influence) : contre-ingérence informationnelle.

**OIV** — Opérateurs d’Importance Vitale. Cadre juridique : Code de la défense, articles **L.1332-1 et suivants**. Créé par la loi de programmation militaire (LPM) de 2013.

- **12 secteurs d’activité d’importance vitale (SAIV)** : alimentation, communications électroniques/audiovisuel, eau, énergie, espace, finances, industrie, santé, transport, auxiliaires de l’État, services judiciaires, activités économiques et sociales de l’État.
- **~300 OIV** désignés en France (liste classifiée).
- Obligations : notification des incidents à l’ANSSI, règles de sécurité spécifiques selon secteur, audits ANSSI, homologation des systèmes d’information d’importance vitale (SIIV).

**Qualifications ANSSI** — label de confiance pour les prestataires :

- **PASSI** — Prestataire d’Audit SSI. Qualifie les prestataires réalisant des audits de sécurité pour les OIV et administrations.
- **PDIS** — Prestataire de Détection d’Incidents de Sécurité. Qualifie les SOC/CSIRT externes.
- **PRIS** — Prestataire de Réponse aux Incidents de Sécurité. Qualifie les prestataires d’investigation et de réponse.
- **PACS** — Prestataire d’Accompagnement et de Conseil en Sécurité.
- **SecNumCloud** — Qualification des services cloud de confiance. Exige un ancrage européen (propriété, législation applicable) et des niveaux de sécurité stricts. Durcie en version 3.2 en 2022.

**Textes additionnels** :

- **Code pénal** : infractions d’atteinte aux STAD (systèmes de traitement automatisé de données) — articles **323-1 à 323-8**.
- **Loi informatique et libertés** + **RGPD** : notification CNIL des violations de données personnelles sous 72h.
- **LPM 2024-2030** : renforcement des pouvoirs cyber offensifs français, capacités nouvelles.

**Contacts opérationnels** :

- **CERT-FR** : cert.ssi.gouv.fr — publication d’advisories, alerte et accompagnement.
- **Plateforme de signalement** : signalements.ssi.gouv.fr pour les OIV et administrations.
- **Cybermalveillance.gouv.fr** : plateforme grand public et PME.

## G.2 Union européenne

**ENISA** — European Union Agency for Cybersecurity. Agence de coordination cybersécurité européenne, basée à Athènes/Héraklion. Mission : expertise technique, coordination, publication de rapports (Threat Landscape annuel), organisation d’exercices (Cyber Europe tous les 2 ans), certification cybersécurité européenne.

**CERT-EU** — CSIRT des institutions, organes et agences de l’UE. Couvre Commission, Parlement, Conseil, agences.

**Directive NIS 2** — Directive (UE) 2022/2555, entrée en application octobre 2024. Successeur de NIS 1 (2016).

- **Périmètre** : 18 secteurs (énergie, transport, banque, santé, eau, infrastructures numériques, administration publique, espace, services postaux, gestion des déchets, produits chimiques, alimentation, fabrication, fournisseurs numériques, recherche, etc.).
- **Deux niveaux** : **Entités Essentielles (EE)** et **Entités Importantes (EI)** avec obligations différenciées.
- **Obligations principales** :
  - Mesures techniques, opérationnelles et organisationnelles (art. 21) : gestion des risques, IR, continuité, supply chain, MFA, chiffrement, etc.
  - **Notification d’incidents** : early warning sous 24h, notification détaillée sous 72h, rapport final dans un mois.
  - **Gouvernance** : responsabilité direct au niveau direction (board), formation des dirigeants.
  - **Supply chain** : évaluation des risques fournisseurs.
- **Sanctions** : jusqu’à **10 M€ ou 2% du CA mondial** pour les EE, 7 M€ ou 1,4% pour les EI.
- **Transposition** : États membres, avec variations nationales (en France, transposition en cours au moment de la rédaction, avec l’ANSSI comme autorité compétente).

**EU Cyber Solidarity Act** — adopté 2024 :

- **Réseau européen de SOC** (European Cybersecurity Shield) : coordination de SOC nationaux pour détection et partage.
- **Mécanisme de réponse d’urgence** (Cyber Emergency Mechanism) : activation en crise majeure, assistance aux États membres.
- **Réserve cyber européenne** : experts privés mobilisables par l’UE en crise.

**Cyber Resilience Act** — adopté 2024. Obligations de cybersécurité pour les produits connectés (IoT, logiciels) mis sur le marché européen. Responsabilité des fabricants, gestion des vulnérabilités sur cycle de vie, notification de vulnérabilités exploitées.

**EU Cyber Sanctions Regime** — règlement (UE) 2019/796. Cadre permettant des sanctions ciblées (gel des avoirs, interdictions de voyager) contre des personnes et entités impliquées dans des cyberattaques. Utilisé contre opérateurs GRU, MSS, acteurs biélorusses, etc.

**Digital Operational Resilience Act (DORA)** — règlement 2022/2554, applicable janvier 2025. Cadre spécifique au secteur financier : gestion des risques ICT, tests de résilience, gestion des prestataires ICT critiques.

**eIDAS 2** — règlement sur l’identité numérique européenne.

**Data Act, Digital Services Act (DSA), Digital Markets Act (DMA)** : autres règlements structurants qui touchent indirectement la cybersécurité (gouvernance des données, responsabilités plateformes, concurrence numérique).

## G.3 États-Unis

**Agences cyber fédérales principales** :

- **CISA** — Cybersecurity and Infrastructure Security Agency, DHS. Coordination civile, advisories, KEV, protection des infrastructures critiques.
- **NSA** — National Security Agency. SIGINT mondiale, capacités cyber offensives, advisories conjoints.
- **USCYBERCOM** — US Cyber Command, DoD. Combatant command cyber, opérations militaires.
- **FBI** — Federal Bureau of Investigation. Law enforcement cyber, investigations, démantèlements, indictments.
- **DOJ** — Department of Justice. Poursuites pénales, indictments formels.
- **OFAC** — Office of Foreign Assets Control, Treasury. Sanctions économiques.
- **NSC Cyber Directorate** — Maison Blanche, coordination stratégique.
- **ODNI** — Office of the Director of National Intelligence. Coordination renseignement fédéral.

**Directives et Executive Orders** :

- **Presidential Policy Directive 21 (PPD-21)** — 2013 — définit les 16 **Critical Infrastructure Sectors**.
- **Executive Order 13800** (2017, Trump) : Strengthening Cybersecurity of Federal Networks.
- **Executive Order 14028** (mai 2021, Biden) : Improving the Nation’s Cybersecurity. Réponse à SolarWinds. **SBOM** obligatoire, Zero Trust fédéral, EDR généralisé, partage renforcé.
- **EO sur les spywares commerciaux** (mars 2023) : restreint l’acquisition de spywares commerciaux par le gouvernement fédéral.
- **National Cybersecurity Strategy** (mars 2023) : doctrine consolidée de l’administration Biden.

**Binding Operational Directives (BOD) CISA** — contraintes pour les agences fédérales. Exemples :

- **BOD 22-01** : Known Exploited Vulnerabilities catalogue — obligation de patch dans les délais fixés.
- **BOD 23-01** : Improving Asset Visibility and Vulnerability Detection.
- **BOD 23-02** : Mitigating the Risk from Internet-Exposed Management Interfaces.

**Lois cyber principales** :

- **Computer Fraud and Abuse Act (CFAA)** — loi pénale cyber historique (1986), base des poursuites cyber.
- **Cybersecurity Information Sharing Act (CISA Act)** — 2015, partage public-privé.
- **Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA)** — 2022, obligations de notification pour les infrastructures critiques (règles finales CISA en cours).
- **Executive Order sur les télécoms étrangers** : restrictions Huawei, ZTE.

**Indictments et sanctions — acteurs ciblés** :

- **Indictments DOJ notables** : Unit 61398/PLA (2014), APT10/MSS Tianjin (2018), APT28/GRU (2018), APT41 (2020), APT40/MSS Hainan (2021), APT31/MSS Hubei (2024), multiples opérateurs DPRK et iraniens.
- **Sanctions OFAC notables** : Tornado Cash (2022), Integrity Technology Group (2025), multiples adresses crypto Lazarus, entités NSO Group + Intellexa + Candiru (via Entity List Commerce), multiples ressortissants russes/chinois/iraniens/nord-coréens.
- **Entity List Commerce** : Huawei (2019), Hikvision, Dahua, NSO, Candiru, ZTE, etc.

**Cyber Safety Review Board (CSRB)** — créé 2022. Investigue les incidents cyber majeurs, publie des rapports publics. Rapports publiés : Log4j (2022), Lapsus$ (2023), Storm-0558/Microsoft (2024).

## G.4 Royaume-Uni

**NCSC** — National Cyber Security Centre. Branche publique du GCHQ, créée en 2016. Modèle de référence internationale. Publications (Annual Review, Active Cyber Defence programme, Cyber Essentials), accompagnement, advisories.

**GCHQ** — Government Communications Headquarters. Agence SIGINT historique, Cheltenham. Partenaire central NSA dans Five Eyes.

**NCF** — National Cyber Force. Créée publiquement en 2020. Branche cyber offensive britannique, regroupe personnels GCHQ + MoD + MI6/SIS. Doctrine de « disruption by design ».

**MI5 / Security Service** : contre-espionnage intérieur, incluant dimension cyber.

**MI6 / SIS** : renseignement extérieur, capacités cyber intégrées aux opérations clandestines.

**NCA** — National Crime Agency. Law enforcement, incluant National Cyber Crime Unit. Lead sur des démantèlements comme LockBit (Operation Cronos 2024).

**Textes** :

- **Computer Misuse Act** (1990) : base pénale cyber UK.
- **Investigatory Powers Act** (2016) : cadre des capacités d’interception.
- **National Cyber Strategy 2022-2030**.
- **Network and Information Systems Regulations (NIS Regulations 2018)** : transposition NIS 1, en cours d’actualisation pour refléter NIS 2 (le UK étant post-Brexit, la transposition NIS 2 n’est pas automatique).

**Computer Crime Act** et **Data Protection Act** + **UK GDPR** encadrent également le domaine.

## G.5 Allemagne

**BSI** — Bundesamt für Sicherheit in der Informationstechnik. Agence fédérale cybersécurité, équivalent allemand de l’ANSSI. Bonn.

**BfV** — Bundesamt für Verfassungsschutz. Office fédéral de protection de la Constitution (contre-espionnage intérieur).

**BND** — Bundesnachrichtendienst. Service fédéral de renseignement extérieur.

**BKA** — Bundeskriminalamt. Office fédéral de police criminelle.

**Zentrale Stelle für Informationstechnik im Sicherheitsbereich (ZITiS)** : support technique aux services de sécurité allemands.

**KRITIS** : cadre des infrastructures critiques allemandes. Secteurs définis et obligations de notification.

## G.6 OTAN

**Reconnaissance du cyber comme 5ème domaine d’opérations** — sommet de Varsovie, 2016.

**NATO Cyber Operations Centre (CyOC)** — créé 2018, intègre le cyber dans la planification militaire OTAN.

**CCDCOE** — Cooperative Cyber Defence Centre of Excellence, Tallinn (Estonie). Créé en 2008. Think tank OTAN sur le cyber. Pilote :

- Le **Manuel de Tallinn** (1.0 en 2013, 2.0 en 2017, 3.0 en cours) — interprétation du droit international appliqué au cyber. Non-contraignant mais référence majeure.
- L’exercice **Locked Shields** annuel — plus grand exercice de red/blue team au monde.
- Publications académiques et techniques.

**Article 5 et cyber** : reconnu applicable au cyber depuis 2014. Seuil de déclenchement délibérément non défini (ambiguïté stratégique). Jamais déclenché pour un incident cyber à date.

**NATO Communications and Information Agency (NCIA)** : bras technique cyber OTAN.

## G.7 ONU

**GGE** — Group of Governmental Experts on Developments in the Field of Information and Telecommunications in the Context of International Security. Groupe restreint d’experts gouvernementaux. Rapports consensuels 2013 et 2015 affirmant que le droit international s’applique au cyber.

**OEWG** — Open-Ended Working Group. Créé 2018, plus inclusif (tous États membres). Rapports 2021 et 2024, plus divisifs politiquement.

**Groupes de positions structurants** :

- **Bloc occidental** : normes existantes s’appliquent, focus sur comportements responsables, multistakeholderisme.
- **Bloc Russie-Chine** : nouveau traité nécessaire, concept de « sécurité de l’information » incluant contrôle du contenu, multilatéralisme strict (États seuls).

**UN Convention on Cybercrime** — négociée sous leadership russe, adoptée en 2024. Controversée — critiques des démocraties et de la société civile sur les risques pour les droits humains, la définition large des infractions, les capacités de coopération qui pourraient servir à la répression transfrontalière.

## G.8 Pall Mall Process

Lancé à Londres en février 2024, conjointement par le **Royaume-Uni et la France**. Initiative internationale de régulation des capacités cyber offensives commerciales (spywares, outils offensifs).

**Préoccupation centrale** : l’usage abusif de ces outils contre des journalistes, dissidents, opposants politiques, défenseurs des droits humains.

**Signataires initiaux** (déclaration de Londres, février 2024) : plus de **40 États**. Puis d’autres rounds avec nouveaux signataires.

**Entreprises cosignataires** : Apple, Google, Meta, Microsoft, BAE Systems et plusieurs autres. ONG également partie prenante (Citizen Lab, Access Now, etc.).

**Principes affirmés** :

- Usage des capacités cyber commerciales dans le respect du droit international et des droits humains.
- Responsabilité des États sur les usages de capacités qu’ils acquièrent.
- Transparence relative sur les acquisitions étatiques.
- Sanctions contre les entreprises documentées pour usages abusifs.

**Limites** :

- Non-contraignant juridiquement.
- Plusieurs États majeurs (clients importants de NSO et pairs) non signataires — Israël notamment, ainsi que plusieurs pays du Golfe, d’Asie centrale, d’Afrique.
- Effet dépend de la mise en œuvre nationale.

**Suivis** : rounds réguliers, élaboration de cadres plus opérationnels, extension des signataires.

## G.9 Synthèse pour l’analyste

Face à un incident APT, l’analyste mobilise les cadres pertinents selon plusieurs axes.

**Si l’incident touche un OIV français** :

- Notification ANSSI obligatoire.
- Coordination CERT-FR.
- Éventuelle remontée C4 si gravité élevée.
- Respect des règles de sécurité OIV applicables au secteur.

**Si l’incident touche une entité NIS 2** :

- Notification autorité nationale compétente sous 24h (early warning).
- Notification détaillée sous 72h.
- Rapport final sous un mois.
- Éventuelles sanctions administratives en cas de manquement aux mesures de sécurité.

**Si données personnelles affectées** :

- Notification CNIL (en France) sous 72h, RGPD art. 33.
- Communication aux personnes concernées si risque élevé (art. 34).

**Si attribution à acteur sanctionné** :

- Vérification des obligations OFAC (pour les entités ayant des liens US) — interdiction de paiement de rançon à entité sanctionnée.
- Vérification des sanctions UE équivalentes.

**Si l’incident touche plusieurs juridictions** :

- Coordination ANSSI + autorités des autres pays.
- Éventuelle remontée ENISA pour coordination européenne.
- Partage international selon TLP via FIRST, ISAC international.

**Pour la défense proactive** :

- Suivi des advisories CERT-FR, CISA, NCSC, BSI, ENISA.
- Monitoring KEV CISA et équivalents.
- Participation ISAC sectoriel.
- Qualification des prestataires (PASSI, PDIS, PRIS) pour les missions critiques.
- Conformité NIS 2 / LPM / ISO 27001 / référentiels sectoriels.

-----
