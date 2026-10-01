---
title: Partie V — Puissances cyber occidentales et alliées
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

*Cette partie complète la cartographie des acteurs étatiques. L'objectif n'est pas de symétriser les menaces mais d'éviter un angle mort analytique : les cyberopérations sont un instrument de puissance utilisé par tous les États dotés. Comprendre les différences doctrinales entre blocs est une compétence analytique fondamentale.*

---


## Chapitre 16 — États-Unis : doctrine, agences et cyber power

L'appareil cyber américain est le plus puissant et le plus structuré au monde. **USCYBERCOM** (commandement militaire cyber — Cyber Mission Force, ~6 000 opérateurs, articulation avec les combatant commands) conduit les opérations offensives et défensives militaires. La **NSA** (National Security Agency — TAO/Tailored Access Operations) collecte du renseignement d'origine électromagnétique et cyber avec des capacités offensives majeures. La **CIA** (Central Intelligence Agency) dispose de capacités cyber clandestines intégrées au renseignement humain. Le **FBI** conduit les investigations cyber, les démantèlements d'infrastructure, et les poursuites judiciaires (indictments). **CISA** (Cybersecurity and Infrastructure Security Agency) coordonne la protection des infrastructures critiques et publie des advisories de référence.

La distinction fondamentale : le renseignement (NSA/CIA — collecte clandestine, pas d'attribution publique) est séparé de l'offensive militaire (USCYBERCOM — defend forward, disruption) et du law enforcement (FBI/DOJ — indictments publics, sanctions, naming and shaming).

**La doctrine du defend forward / persistent engagement** (Gen. Paul Nakasone, 2018) est un changement de paradigme : ne pas attendre l'attaque mais agir en continu dans les réseaux adverses pour dégrader leurs capacités. Le concept de « contestation permanente » signifie que USCYBERCOM opère quotidiennement dans les réseaux adverses, pas uniquement en réponse à une attaque.

**Opérations documentées :** Stuxnet (co-attribution US/Israël — sabotage du programme nucléaire iranien, traité au Ch.18 et Ch.21), démantèlement de botnets (Emotet 2021, Qakbot 2023 — coordination FBI/Europol), neutralisation de Snake/Turla (opération Medusa 2023 — FBI), advisories conjoints NSA/CISA/FBI attribuant des APT avec IoC et TTP (un outil de défense collective unique dans l'écosystème mondial), et opérations de « hunt forward » (USCYBERCOM déploie des équipes dans les réseaux de pays alliés pour détecter les menaces — Ukraine depuis 2018).

**L'utilisation du droit comme instrument :** indictments DOJ contre des opérateurs APT chinois (PLA Unit 61398 en 2014, MSS en 2018 et 2024), russes (GRU Unit 26165 en 2018 pour l'ingérence électorale), iraniens, et nord-coréens. L'effet dissuasif est débattu (les inculpés ne seront probablement jamais arrêtés) mais l'effet de naming and shaming est réel (il réduit la marge de déni plausible). Les sanctions ciblées OFAC complètent le dispositif.

---


## Chapitre 17 — Royaume-Uni et Five Eyes

**GCHQ** (Government Communications Headquarters) est l'agence de renseignement d'origine électromagnétique et cyber, partenaire étroit de la NSA. Le **NCSC** (National Cyber Security Centre, branche du GCHQ) est l'organisme de protection nationale — son modèle (publication d'advisories de haute qualité, collaboration directe avec le secteur privé, communication accessible) est une référence en Europe. La **National Cyber Force** (NCF, créée 2020) conduit les opérations offensives dédiées — capacités de disruption ciblée. **MI5** (sécurité intérieure, contre-espionnage) et **MI6/SIS** (renseignement extérieur) complètent l'écosystème.

L'alliance **Five Eyes** (US, UK, Canada, Australie, Nouvelle-Zélande) est le partage de renseignement cyber le plus intégré au monde : advisories conjoints, partage d'IoC et de TTP en quasi temps réel, coordination des attributions publiques. Le Royaume-Uni est souvent parmi les premiers à attribuer publiquement une opération étatique (NotPetya, SolarWinds, Volt Typhoon). Les opérations documentées incluent la disruption de botnets, les opérations d'influence contre Daesh (JTRIG), et le modèle de « disruption by design ».

---


## Chapitre 18 — Israël

cyber, renseignement et supériorité technologique

L'écosystème cyber israélien est unique par son intégration militaire-renseignement-privé. L'**Unité 8200** (renseignement d'origine électromagnétique et cyber de l'IDF — la « NSA israélienne ») est la pépinière de talents du secteur cyber israélien. Le **Mossad** conduit les opérations clandestines extérieures. Le **Shin Bet** gère la sécurité intérieure et la surveillance.

La doctrine de **préemption** appliquée au cyber : Israël considère le cyberespace comme un espace d'action permanent, pas une réponse à une agression. Le cas **Stuxnet** (co-attribution US/Israël) est fondateur : la première arme cyber conçue pour causer des dommages physiques — destruction de ~1 000 centrifugeuses nucléaires iraniennes à Natanz via la manipulation des automates Siemens. L'opération a retardé le programme iranien de 2-3 ans mais a aussi catalysé le développement des capacités cyber iraniennes (effet boomerang) et a posé la question de la prolifération des armes cyber (le code de Stuxnet a fuité et a été étudié par tous les acteurs étatiques). Stuxnet est aussi traité au Ch.14 (impact sur l'Iran) et au Ch.21 (OT/ICS).

Le pipeline **Unité 8200 → startups** : les vétérans fondent les entreprises de cybersécurité et de surveillance les plus avancées au monde. NSO Group (Pegasus), Intellexa (Predator), Candiru — le marché de la surveillance offensive comme produit d'exportation stratégique. Les controverses : usage documenté contre des journalistes, dissidents, opposants politiques, et même des chefs d'État (Pegasus Project 2021). Les tentatives de régulation (Pall Mall Process, restrictions d'exportation, inscription sur la Entity List US). La frontière floue entre sécurité nationale légitime et abus commercial est un enjeu de gouvernance mondiale.

---


## Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel

L'Ukraine est le laboratoire mondial de la cyberdéfense en temps de guerre. La transformation sous contrainte depuis 2014 (annexion de la Crimée, premières cyberattaques russes majeures — BlackEnergy 2015) jusqu'à l'invasion de 2022 a produit un retour d'expérience unique.

La **coopération sans précédent** avec les alliés et le secteur privé : Microsoft (Threat Intelligence Center — détection et neutralisation en quasi temps réel des malwares russes déployés en Ukraine), Google (TAG — Project Shield, protection DDoS), ESET (analyse de malware — Industroyer2 déjoué grâce à la collaboration CERT-UA/ESET), Amazon Web Services (migration d'urgence des données gouvernementales vers le cloud), Starlink (connectivité résiliente), et USCYBERCOM (opérations « hunt forward » — déploiement d'équipes américaines dans les réseaux ukrainiens pour détecter les menaces). Ce modèle de défense collaborative public-privé-international est sans précédent dans l'histoire du cyber.

L'usage **offensif/défensif** : le **CERT-UA** (Computer Emergency Response Team) a démontré des capacités de réponse sous le feu remarquables. Les opérations offensives ukrainiennes (cyberattaques documentées contre les systèmes logistiques et de communication russes, piratage de caméras de surveillance) sont partiellement publiques. L'**IT Army of Ukraine** est un mouvement coordonné de volontaires cyber internationaux (lancé via Telegram par le vice-premier ministre Mykhailo Fedorov) conduisant des opérations DDoS et de hacktivisme contre des cibles russes — zone grise entre hacktivisme et opération militaire.

Le **retour d'expérience** : la résilience numérique sous bombardement (migration cloud d'urgence, décentralisation des systèmes, backups distribués), l'efficacité relative des cyberattaques dans un conflit cinétique (le cyber seul ne gagne pas une guerre — les blackouts de 2022 ont été réparés en heures grâce à l'expérience accumulée depuis 2015), et les leçons pour les pays européens (la préparation, la résilience, et la coopération sont plus importantes que la capacité offensive).

---
