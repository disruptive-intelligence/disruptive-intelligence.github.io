---
title: PARTIE V — PUISSANCES CYBER OCCIDENTALES ET ALLIÉES
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 5
chapters: 8
---

> **Ce que cette partie apprend.** Comprendre les doctrines cyber des puissances occidentales majeures (US, UK/Five Eyes, Israël, Ukraine en miroir), cartographier les agences qui les exécutent, connaître les opérations documentées publiquement, et saisir comment ces acteurs utilisent le droit et l’attribution publique comme instruments de dissuasion.
> 
> **Ce qu’elle ne couvre pas.** Les cadres juridiques détaillés (Annexe G), l’analyse comparée des doctrines comme grille d’analyse (Ch.25), les mercenaires cyber d’origine israélienne en tant qu’entreprises (Ch.15).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer defend forward américain, disruption britannique et préemption israélienne, situer une opération offensive alliée dans son cadre doctrinal, et comprendre pourquoi l’Ukraine est le laboratoire de référence de la cyberdéfense moderne.
> 
> **Une précaution méthodologique.** Cette partie n’est pas une symétrisation morale entre blocs. Les acteurs présentés ici ont des doctrines, des cadres juridiques, des contrôles démocratiques, et des pratiques de responsabilité publique qui diffèrent substantiellement de ceux de la Russie, de la Chine, de la DPRK ou de l’Iran. Les présenter au même titre (cartographie des acteurs étatiques cyber) est une exigence analytique ; le faire sans discernement doctrinal ni contextuel serait trompeur.

-----

## Chapitre 16 — États-Unis : doctrine, agences et cyber power

### 16.1 Vue d’ensemble de l’appareil cyber américain

L’appareil cyber américain est le plus puissant et le plus structuré au monde. Sa caractéristique distinctive est la **séparation institutionnelle** entre plusieurs fonctions qui, dans d’autres pays, sont confondues : le renseignement (NSA, CIA) est séparé de l’action militaire offensive (USCYBERCOM), elle-même séparée du law enforcement (FBI), elle-même séparée de la protection des infrastructures civiles (CISA).

Cette séparation n’est pas parfaite — les fonctions se chevauchent (USCYBERCOM et la NSA partagent un même directeur, le « dual-hat » arrangement), et la coordination est permanente — mais elle structure les missions, les responsabilités, et les cadres juridiques. Elle contraste avec les modèles russe (GRU conduit simultanément espionnage et destruction), chinois (MSS et PLA avec fragmentation et contractors), et iranien (IRGC intègre action et renseignement).

Les quatre piliers de l’appareil cyber américain sont : **USCYBERCOM** (commandement militaire), **NSA** (renseignement SIGINT/cyber), **FBI** (law enforcement cyber), **CISA** (protection des infrastructures critiques). La CIA dispose également de capacités cyber intégrées à ses opérations clandestines, et d’autres agences (DIA, Treasury/OFAC, DOJ) interviennent dans leurs domaines respectifs.

### 16.2 USCYBERCOM : le commandement militaire cyber

**US Cyber Command** (USCYBERCOM) est le combatant command unifié du Département de la Défense chargé des opérations cyber. Créé en 2009 comme sous-commandement de STRATCOM, élevé en combatant command unifié en 2018.

**Mission** : défendre les réseaux du Département de la Défense, soutenir les commandements militaires régionaux et fonctionnels par des opérations cyber, et conduire les opérations cyber militaires offensives autorisées.

**Structure** : USCYBERCOM comprend les **Cyber Mission Forces (CMF)**, environ **6 200 opérateurs** répartis en **133 équipes** :

- **Cyber National Mission Teams (CNMT)** : défendent le pays contre les cybermenaces majeures, coordonnent avec les agences civiles.
- **Cyber Combat Mission Teams (CCMT)** : soutiennent les commandements militaires régionaux dans leurs opérations (supporting CENTCOM, INDOPACOM, EUCOM, etc.).
- **Cyber Protection Teams (CPT)** : défendent les réseaux DoD spécifiques.
- **Cyber Support Teams (CST)** : soutien analytique et planning.

**Dual-hat arrangement** : le directeur de la NSA est simultanément commandant d’USCYBERCOM. Cet arrangement, critiqué périodiquement pour les risques de confusion de missions (renseignement vs action militaire), a été maintenu parce qu’il optimise l’usage des ressources (NSA fournit l’accès technique, USCYBERCOM fournit les autorités d’action).

### 16.3 La NSA : renseignement SIGINT et capacités cyber offensives

La **National Security Agency** (NSA) est l’agence de renseignement d’origine électromagnétique des États-Unis. Elle collecte le SIGINT mondial et développe des capacités cyber offensives majeures.

**Tailored Access Operations (TAO)** — renommé en 2017 **Computer Network Operations** (CNO) puis **Computer Network Exploitation** — est la branche historique de la NSA pour les opérations cyber offensives. TAO développait et déployait des outils d’intrusion pour la collecte de renseignement. Les capacités TAO ont été partiellement révélées par les fuites **Shadow Brokers** (2016-2017), qui ont publié des outils internes dont **EternalBlue** (exploit SMB utilisé ensuite par WannaCry et NotPetya), **DoublePulsar**, **Fuzzbunch**, et d’autres. Ces fuites ont été l’un des événements les plus graves de l’histoire du renseignement américain — des outils offensifs étatiques passés dans le domaine public ont été exploités massivement par des acteurs criminels et étatiques.

**Threat Operations Center (NTOC)** : coordination défensive, détection de menaces, partage avec les alliés.

**Opérations documentées** :

- **Co-attribution Stuxnet** (avec Israël, 2010) : sabotage du programme nucléaire iranien. Attribution solide via le livre *Confront and Conceal* de David Sanger et investigations ultérieures.
- **Collecte SIGINT mondiale** : révélée par les fuites Snowden (2013) qui ont documenté des programmes comme PRISM, XKeyscore, la collecte massive de métadonnées téléphoniques.

La NSA est également l’une des agences qui publient le plus d’**advisories techniques** de haute qualité en coordination avec CISA et le FBI — une transformation majeure depuis les années 2010, où la NSA partageait peu publiquement ses analyses.

### 16.4 La CIA et ses capacités cyber clandestines

La **Central Intelligence Agency** dispose de capacités cyber intégrées à ses opérations de renseignement humain et clandestines. Le **Center for Cyber Intelligence** (CCI) a été révélé partiellement par les fuites **Vault 7** (2017), où WikiLeaks a publié des documents internes de la CIA documentant des outils d’intrusion pour Windows, macOS, iOS, Android, systèmes IoT, et voitures connectées.

Contrairement à la NSA (collecte SIGINT massive) et USCYBERCOM (opérations militaires), la CIA cible des cas très spécifiques dans le cadre d’opérations clandestines plus larges. Son empreinte publique cyber est volontairement limitée — les capacités révélées par Vault 7 ont conduit à des enquêtes internes et à des arrestations (un ancien employé CIA a été condamné en 2022 pour les fuites).

### 16.5 Le FBI : investigation, démantèlement, indictments

Le **Federal Bureau of Investigation** conduit les investigations cyber, les démantèlements d’infrastructure, et les poursuites judiciaires. Son **Cyber Division** coordonne avec les bureaux régionaux qui enquêtent sur les incidents.

Le FBI a acquis un rôle central dans la réponse aux APT via plusieurs fonctions :

- **Investigation des incidents majeurs** : compromission de victimes US, collecte de preuves, coordination avec les cibles.
- **Démantèlements d’infrastructure** : opérations judiciaires de saisie de serveurs, de domaines, de cryptomonnaies. Quelques cas emblématiques : **Emotet** (janvier 2021, coordination Europol), **Hive** (janvier 2023, infiltration et déchiffrement pour les victimes), **Qakbot** (août 2023, « Operation Duck Hunt »), **LockBit** (février 2024, « Operation Cronos » coordonnée NCA/FBI/Europol), **Volt Typhoon KV Botnet** (janvier 2024), **Flax Typhoon Raptor Train** (septembre 2024), **Snake/Turla Medusa** (mai 2023).
- **Indictments** : mise en accusation formelle d’opérateurs APT étrangers. Les indictments DOJ sont devenus un instrument diplomatique central. Exemples emblématiques : Unit 61398/PLA (2014, 5 officiers chinois), APT10/MSS Tianjin (2018), APT28/GRU (2018, 12 officiers), APT41 (2020, 5 ressortissants chinois), APT40/MSS Hainan (2021, 4 ressortissants), APT31/MSS Hubei (2024, 7 ressortissants, avec sanctions coordonnées).

L’effet des indictments est débattu. Les inculpés ne seront probablement jamais jugés (les pays sponsors ne les extradent pas). Mais l’effet de **naming and shaming** est réel — il réduit la marge de déni plausible, impose un coût diplomatique au sponsor, et fournit à la communauté CTI un socle documentaire sur les opérateurs.

### 16.6 CISA : protection des infrastructures critiques

**Cybersecurity and Infrastructure Security Agency** (CISA), créée en 2018 au sein du Département de la Sécurité Intérieure (DHS), est l’agence civile de coordination de la cybersécurité aux États-Unis. Elle protège les infrastructures critiques, publie des advisories, coordonne avec le secteur privé et les gouvernements locaux, et conduit des exercices nationaux.

**Publications CISA** : les advisories CISA (souvent conjoints avec NSA, FBI, et alliés Five Eyes) sont devenus une référence mondiale. Les **Joint Cybersecurity Advisories (JCSA)** documentent les TTP d’acteurs étatiques avec un niveau de détail opérationnel exceptionnel. Exemples : advisories Volt Typhoon (2023, 2024), APT40 (2024), Salt Typhoon (2024-2025), et des dizaines d’autres.

**Known Exploited Vulnerabilities (KEV)** : CISA maintient une liste publique des vulnérabilités activement exploitées par les acteurs menaçants. La **Binding Operational Directive 22-01** impose aux agences fédérales US de patcher les vulnérabilités du KEV dans des délais stricts. Le KEV est utilisé mondialement comme référence de priorisation.

**Shields Up** : posture de vigilance renforcée annoncée par CISA post-invasion ukrainienne (février 2022), recommandations pratiques à toutes les organisations américaines.

**Secure by Design** : initiative CISA pour responsabiliser les éditeurs logiciels (designs sécurisés par défaut, transparence sur les vulnérabilités).

CISA est devenue sous son leadership post-2021 (Jen Easterly puis ses successeurs) l’une des agences cyber les plus visibles et les plus influentes mondialement — un modèle de coordination civile/militaire/privée que plusieurs pays européens cherchent à adapter.

### 16.7 Defend Forward et Persistent Engagement

La **doctrine du defend forward / persistent engagement** est l’innovation doctrinale américaine majeure de la décennie 2010-2020. Formulée publiquement par le général Paul Nakasone (directeur NSA et commandant USCYBERCOM de 2018 à 2024) et codifiée dans la **Cyber Strategy du DoD** (2018), elle marque une rupture avec la posture défensive classique.

**Principe** : ne pas attendre l’attaque pour agir, mais **opérer en continu dans les réseaux adverses** pour dégrader leurs capacités, collecter du renseignement tactique, et démontrer une présence dissuasive.

**Concept de « contestation permanente »** : le cyberespace n’est pas un domaine de paix ponctuée d’incidents, mais un domaine de confrontation continue. USCYBERCOM opère quotidiennement dans les réseaux adverses, pas uniquement en réponse à une attaque identifiée.

**Différence avec les doctrines précédentes** : avant defend forward, la doctrine américaine était largement défensive — réagir après compromission, protéger les réseaux nationaux. Defend forward inverse la logique : l’initiative doit être américaine, pas adverse.

**Débats** : la doctrine est critiquée par certains analystes comme favorisant l’escalade (risque d’incidents non désirés), par d’autres comme insuffisamment agressive. Le fait qu’elle soit publique — une doctrine offensive ouvertement assumée — est lui-même une rupture notable avec la tradition de discrétion autour des capacités offensives.

### 16.8 Hunt Forward : les opérations en territoire allié

Le concept de **Hunt Forward Operations (HFO)** est dérivé de defend forward. Il consiste à déployer des équipes USCYBERCOM **dans les réseaux de pays alliés** pour détecter des menaces que les alliés n’ont pas les moyens de détecter seuls.

**Principe** : l’équipe USCYBERCOM arrive chez l’allié à l’invitation de ce dernier, avec un cadre juridique et opérationnel négocié. Elle opère sur les réseaux de l’allié (sensor placement, chasse aux menaces, analyse), partage les résultats avec l’allié et rentre aux États-Unis avec l’expérience et les IoC collectés. Bénéfice croisé : l’allié gagne en sécurité, les États-Unis gagnent en connaissance des TTP adverses observées dans des environnements variés.

**Opérations documentées** :

- **Ukraine** : hunt forward teams américaines déployées dans les réseaux ukrainiens depuis 2018. Volume massif d’activité depuis 2022. Retour d’expérience direct sur les TTP russes (Sandworm, APT28, Gamaredon, Unit 29155). Pour les Ukrainiens : détection renforcée. Pour les Américains : connaissance de terrain des TTP russes qui alimente ensuite les défenses des autres alliés.
- **Europe de l’Est** : Estonie, Lettonie, Lituanie, Pologne, Roumanie, Monténégro.
- **Autres alliés** : déployments documentés également dans des pays non européens.

Le nombre total d’opérations dépasse 50 déploiements publiquement reconnus au moment des rapports annuels de USCYBERCOM.

### 16.9 Opérations documentées majeures

**Stuxnet (co-attribution 2010)** : sabotage du programme nucléaire iranien à Natanz, en coopération avec Israël. Détaillé au Ch.14, Ch.18, Ch.21.

**Démantèlement d’Emotet (janvier 2021)** : opération coordonnée FBI/Europol/Eurojust qui a saisi l’infrastructure d’Emotet (l’un des plus grands botnets et loaders criminels du monde). Emotet s’est partiellement reconstitué en 2021-2022 mais n’a jamais retrouvé son niveau précédent.

**Démantèlement de Qakbot (août 2023)** : « Operation Duck Hunt », FBI et partenaires internationaux. Le FBI a exploité le protocole de contrôle de Qakbot pour désinstaller le malware des 700 000+ machines infectées — opération offensive law enforcement sur le modèle de Medusa/Snake.

**Opération Medusa / Snake (mai 2023)** : neutralisation de l’implant Snake (Turla) sur les machines infectées via un outil développé par le FBI, exploitant des fonctionnalités du malware lui-même. Détaillé au Ch.6.

**Démantèlement LockBit (février 2024)** : Operation Cronos, NCA britannique en lead avec FBI et Europol. Saisie de l’infrastructure, publication de contenus moqueurs sur le site .onion de LockBit (ironie retournée — les forces de l’ordre ont utilisé l’interface du groupe pour afficher des messages à leur encontre), arrestations, offre gratuite de déchiffreur.

**Démantèlement KV Botnet Volt Typhoon (janvier 2024)** : neutralisation du botnet de routeurs Cisco RV/NetGear compromis utilisé par Volt Typhoon comme infrastructure C2.

**Démantèlement Raptor Train Flax Typhoon (septembre 2024)** : neutralisation du botnet de 260 000+ dispositifs IoT compromis opéré par Flax Typhoon.

### 16.10 Le droit et les sanctions comme instruments

Les États-Unis ont **instrumentalisé le droit** comme réponse aux cybermenaces étatiques d’une manière qu’aucun autre pays n’a égalée en ampleur.

**Indictments DOJ** (section 16.5) : mise en accusation formelle d’opérateurs APT étrangers, effet de naming and shaming.

**Sanctions OFAC** : le Département du Trésor peut désigner des personnes, entités, et adresses crypto comme « Specially Designated Nationals » (SDN), interdisant aux entités américaines tout commerce avec elles. La sanction de **Tornado Cash** (août 2022) a été un précédent majeur — première sanction d’un smart contract dans l’histoire. Les sanctions OFAC ont ciblé des opérateurs APT nommés, des contractors (Integrity Technology Group — chinois, sanctionné janvier 2025), des entités PSO (NSO, Candiru sanctionnés Entity List 2021 ; Intellexa sanctionnée 2023-2024), et des adresses crypto utilisées pour le blanchiment nord-coréen.

**Entity List du Commerce** : liste d’entités interdites d’accès aux technologies américaines. Usage étendu contre Huawei (2019), ZTE, plusieurs fournisseurs de surveillance chinois (Hikvision, Dahua), NSO, Candiru, Intellexa.

**Executive Orders** : **EO 14028** (mai 2021, Biden — « Improving the Nation’s Cybersecurity ») a restructuré la réponse fédérale au cyber suite à SolarWinds. **EO sur les spywares commerciaux** (mars 2023) restreint l’acquisition de spywares commerciaux par le gouvernement fédéral américain.

### 16.11 Particularités doctrinales vs les autres blocs

Synthèse comparative des spécificités américaines :

- **Séparation institutionnelle** : renseignement (NSA, CIA), militaire (USCYBERCOM), law enforcement (FBI), protection civile (CISA) sont distincts. Modèle atypique — la Russie, la Chine, l’Iran intègrent davantage ces fonctions.
- **Usage massif du droit** : indictments, sanctions, Entity List, Executive Orders. Les États-Unis sont le seul pays qui utilise le droit comme instrument diplomatique cyber à cette échelle.
- **Publicité des attributions** : les États-Unis communiquent publiquement sur les attributions avec un niveau de détail sans équivalent. Advisory techniques (NSA/CISA/FBI), rapports annuels, déclarations officielles.
- **Defend forward / hunt forward** : doctrine d’initiative plutôt que de réaction, opérations ouvertement assumées dans les réseaux adverses et alliés.
- **Coordination Five Eyes** : partage de renseignement et d’attribution avec UK, Canada, Australie, Nouvelle-Zélande (Ch.17).
- **Contrôle démocratique et judiciaire** : les opérations cyber américaines sont encadrées par des autorités légales (Title 10 pour le militaire, Title 50 pour le renseignement), des supervisions congressionnelles (Senate Intelligence Committee, House Intelligence Committee), et des contrôles judiciaires (FISA Court pour certaines collectes). Ces mécanismes ne sont pas parfaits mais distinguent le modèle américain de celui d’autres grandes puissances cyber.

Pour l’analyste : face à une activité attribuée aux États-Unis, les considérations différent de celles sur les autres acteurs — question de l’autorité légale invoquée, cadre de commandement (Title 10 vs Title 50), probabilité d’attribution publique à terme, possibilité de réponse diplomatique publique.

-----

## Chapitre 17 — Royaume-Uni et Five Eyes

### 17.1 GCHQ : agence SIGINT et partenaire NSA

**Government Communications Headquarters** (GCHQ) est l’agence britannique d’origine électromagnétique et cyber. Héritière de Bletchley Park (déchiffrement Enigma pendant la Seconde Guerre mondiale), GCHQ est un partenaire étroit de la NSA — la relation US-UK en matière de SIGINT est la plus intégrée au monde, formalisée par l’**UKUSA Agreement** (1946) qui a évolué vers les Five Eyes.

**Mission** : collecte SIGINT mondiale, analyse cyber, soutien aux opérations militaires britanniques, protection de la sécurité nationale.

**Structure** : GCHQ dispose d’une branche cyber offensive intégrée au **National Cyber Force** (voir 17.3) et d’une branche défensive dans le **NCSC** (voir 17.2). La Joint Forces Intelligence Group et d’autres structures complètent le dispositif.

**Publications** : GCHQ publie occasionnellement des analyses techniques, en coordination avec le NCSC. Les attributions GCHQ-NCSC sont parmi les premières dans les attributions coordonnées Five Eyes (NotPetya, SolarWinds, Volt Typhoon).

### 17.2 NCSC : le modèle de protection nationale

**National Cyber Security Centre** (NCSC), créé en 2016 comme branche publique du GCHQ, est l’organisme britannique de protection cyber nationale. Le modèle NCSC est largement considéré comme **une référence internationale** et a inspiré plusieurs agences européennes (ANSSI en partie, BSI en Allemagne).

**Caractéristiques du modèle NCSC** :

- **Publications accessibles** : documentation technique de haute qualité, formulée dans un langage accessible aux non-experts.
- **Collaboration directe avec le secteur privé** : « Active Cyber Defence » programme qui offre gratuitement des services aux organisations britanniques (DMARC, protective DNS, takedown de sites de phishing).
- **Early Warning et threat intelligence partagée** : le NCSC partage des alertes avec les organisations inscrites.
- **Cyber Essentials** : certification cybersécurité accessible aux PME britanniques — modèle qui a inspiré d’autres programmes européens.
- **Transparence** : le NCSC communique plus ouvertement que la plupart de ses homologues sur les incidents nationaux et les menaces — tout en respectant les classifications nécessaires.

**Attributions** : le NCSC (avec GCHQ) attribue publiquement des opérations étatiques. Les attributions NotPetya (2018), Volt Typhoon (2023-2024), APT31 (2024), Salt Typhoon (2024) ont été coordonnées avec les partenaires Five Eyes et relayées par le NCSC.

**NCSC Annual Review** : rapport annuel public qui documente les tendances de la menace sur le Royaume-Uni, les opérations de défense, et les points de mobilisation.

### 17.3 National Cyber Force : opérations offensives

**National Cyber Force** (NCF), créée publiquement en 2020, est l’organisation britannique dédiée aux opérations cyber offensives. Elle rassemble des personnels du GCHQ, du Ministry of Defence (notamment 77th Brigade pour les opérations d’information), et du Secret Intelligence Service (MI6/SIS).

**Mission** : conduire des opérations cyber offensives pour soutenir les intérêts britanniques, avec un focus sur la **disruption ciblée** plutôt que sur la destruction massive. Le NCF se positionne doctrinalement sur la « disruption by design » — désorganiser les adversaires sans détruire, contester sans escalader.

**Cas d’usage publics** :

- Opérations contre les infrastructures Daesh (héritage de JTRIG).
- Opérations contre des réseaux pédocriminels.
- Opérations cyber en soutien des opérations militaires britanniques.
- Opérations contre des groupes cybercriminels (contributions aux démantèlements internationaux).

La NCF est moins visible publiquement qu’USCYBERCOM, mais sa création formelle marque un jalon — le Royaume-Uni a ouvertement assumé ses capacités cyber offensives.

### 17.4 JTRIG : opérations d’information et disruption

**Joint Threat Research Intelligence Group** (JTRIG) est une branche historique du GCHQ, révélée publiquement par les fuites Snowden (2014). Ses capacités incluent des opérations d’influence en ligne, des disruptions de forums criminels et extrémistes, et des opérations d’information contre des cibles stratégiques.

Les documents JTRIG révélés par Snowden ont documenté des opérations contre Anonymous, contre des forums djihadistes, et contre des cibles gouvernementales étrangères. L’exposition publique a suscité des débats sur la légitimité démocratique de certaines opérations (ciblage d’acteurs non étatiques, techniques de manipulation psychologique).

Post-Snowden, JTRIG a probablement été restructurée dans d’autres entités (NCF notamment) mais ses capacités et missions ne sont pas publiquement supprimées.

### 17.5 Five Eyes : l’alliance SIGINT intégrée

L’alliance **Five Eyes** (US, UK, Canada, Australie, Nouvelle-Zélande) est le partage de renseignement SIGINT et cyber le plus intégré au monde. Hérité de l’UKUSA Agreement de 1946, elle s’est étendue progressivement aux trois autres signataires du Commonwealth.

**Mécanismes** :

- **Partage de renseignement SIGINT** : les cinq agences (NSA, GCHQ, CSE Canada, ASD Australie, GCSB NZ) partagent leur collecte entre elles, avec des règles de retenue selon la sensibilité.
- **Partage cyber** : advisories conjoints, IoC et TTP partagés en quasi temps réel, coordination des attributions publiques.
- **Division du travail géographique et technique** : historiquement, chaque Eye couvrait des zones géographiques spécifiques ou des capacités techniques complémentaires.

**Autres agences Five Eyes** :

- **Canada — Communications Security Establishment** (CSE) et **Canadian Centre for Cyber Security** (CCCS, branche publique du CSE, créé 2018 sur le modèle NCSC).
- **Australie — Australian Signals Directorate** (ASD) et **Australian Cyber Security Centre** (ACSC).
- **Nouvelle-Zélande — Government Communications Security Bureau** (GCSB).

**Attributions coordonnées** : les grandes attributions cyber récentes ont presque toutes été Five Eyes avec relais dans chaque pays. NotPetya (2018), SolarWinds (2021), Hafnium/ProxyLogon (2021), Volt Typhoon (2023-2024), APT31 (2024), APT40 (2024), Salt Typhoon (2024-2025) ont toutes été attribuées dans des communiqués coordonnés des cinq pays (plus souvent étendus à des alliés européens et asiatiques : France, Allemagne, Japon, Corée du Sud, Pays-Bas, etc.).

**Étendues d’alliés** : au-delà des Five Eyes stricto sensu, les attributions et les partages s’étendent régulièrement à des « alliés +1 » ou « +X » — **AUKUS** (US, UK, Australie, avec dimension nucléaire), **Quad** (US, Japon, Inde, Australie), **UKUSA élargi** (incluant parfois France, Allemagne, Pays-Bas, Japon, Corée du Sud). La géographie du partage cyber s’étend continuellement.

### 17.6 Opérations documentées

**Disruption de botnets** : contribution britannique à de multiples démantèlements (Emotet, Qakbot, LockBit notamment, où la NCA britannique a été en lead).

**Opérations contre Daesh** : GCHQ et le Ministry of Defence ont publiquement reconnu des opérations cyber contre les infrastructures de communication et de propagande de Daesh (2015-2019).

**Attribution Volt Typhoon (2023)** : le NCSC a co-signé l’advisory Five Eyes de mai 2023 qui a publiquement attribué Volt Typhoon à la Chine. Le ciblage des infrastructures critiques britanniques par des acteurs chinois est un thème récurrent des déclarations publiques NCSC.

**Attribution APT31 (mars 2024)** : le UK a attribué APT31 à des ciblages de parlementaires britanniques et de la Commission électorale. Sanctions coordonnées avec les États-Unis.

**Operation Cronos (LockBit, février 2024)** : la NCA (National Crime Agency) a été en lead de l’opération internationale. Premier cas d’opération de démantèlement ransomware majeur avec le Royaume-Uni en tête.

### 17.7 Modèle de disruption by design

La doctrine britannique peut être résumée par le concept de **« disruption by design »** : contester les adversaires cyber en dégradant leurs capacités, sans nécessairement chercher des effets destructeurs majeurs. Le NCF articule des opérations proportionnées — désorganiser une campagne de phishing, rendre inopérants des outils spécifiques, exposer publiquement des opérateurs.

Cette doctrine est cohérente avec la tradition britannique d’intelligence operations — actions clandestines préférées à l’action militaire ouverte, usage stratégique du law enforcement et de la diplomatie, coordination étroite avec les partenaires.

-----

## Chapitre 18 — Israël : cyber, renseignement et supériorité technologique

### 18.1 Un écosystème unique : intégration militaire-renseignement-privé

L’écosystème cyber israélien est **unique au monde** par son intégration militaire-renseignement-privé. Un trajectoire typique : formation à l’**Unité 8200** (cyber militaire) pendant le service national, puis carrière mixte militaire/renseignement, souvent suivie de fondations de startups cyber et de surveillance qui vendent leurs capacités au secteur privé mondial.

Cette intégration produit un avantage comparatif majeur : les startups israéliennes de cybersécurité et de surveillance ont accès à des talents formés par l’appareil de défense, et l’appareil de défense bénéficie des innovations civiles. C’est aussi ce qui explique la présence disproportionnée d’entreprises israéliennes dans le marché de la surveillance offensive (NSO, Intellexa, Candiru, Paragon — tous fondés par des vétérans de l’Unité 8200 ou services apparentés).

### 18.2 Unité 8200 : pépinière de talents

**Unité 8200** (Yehida Shmoneh-Matayim — 8200) est l’unité de renseignement SIGINT et cyber de l’**IDF** (Israel Defense Forces). C’est la « NSA israélienne » — avec une différence notable : elle recrute des jeunes (17-18 ans) par le service militaire obligatoire.

**Taille et ressources** : Unité 8200 est l’une des plus grandes unités de l’IDF. Les chiffres exacts sont classifiés mais les estimations la situent entre 5 000 et 10 000 personnes actives. Pour un pays de 9 millions d’habitants, c’est une concentration cyber par capita sans équivalent.

**Sélection et formation** : les candidats à l’Unité 8200 sont identifiés dès le lycée via des tests d’aptitude. Formation technique intensive (mathématiques, cryptographie, informatique, langues). Les meilleurs éléments sont ensuite déployés dans les spécialités opérationnelles (intrusion, analyse, linguistique, etc.).

**Mission** : collecte SIGINT sur les menaces envers Israël (Iran et son axe, Hezbollah, Hamas, groupes palestiniens, autres adversaires régionaux), capacités cyber offensives, contre-espionnage cyber.

**Pipeline vers le privé** : après leur service militaire (3 ans pour les hommes, 2 pour les femmes, avec extensions fréquentes dans les unités techniques), les vétérans de l’Unité 8200 fondent massivement des entreprises cyber. Check Point, Palo Alto Networks (fondateurs), CyberArk, Imperva, Varonis, SentinelOne, Wiz, Claroty — la liste est immense. Et côté offensive : NSO, Intellexa (co-fondateur), Candiru, Paragon, et dizaines d’autres.

### 18.3 Mossad : opérations clandestines extérieures

**Ha’Mossad le’Modi’in ule-Tafkidim Meyuhadim** (Institut pour le Renseignement et les Missions Spéciales) est le service de renseignement extérieur israélien. Équivalent approximatif de la CIA américaine ou du SIS britannique.

**Capacités cyber** : le Mossad dispose de capacités cyber intégrées à ses opérations clandestines. Contrairement à l’Unité 8200 (collecte SIGINT de masse), le Mossad conduit des opérations cyber ciblées — souvent combinées avec du HUMINT, des opérations physiques, des sabotages. Le **Directorate for Cyber** au sein du Mossad coordonne ces capacités.

**Cas emblématiques** :

- **Stuxnet (co-attribution avec la NSA)** : coopération Mossad-NSA/CIA pour l’implémentation du malware. Le rôle israélien incluait le renseignement HUMINT permettant la connaissance fine de Natanz (spécifications des centrifugeuses, configuration des automates Siemens, routines opérationnelles).
- **Opérations contre le programme nucléaire iranien** : série d’opérations coordonnées (assassinats de scientifiques nucléaires, sabotages physiques et cyber, opérations d’exfiltration de renseignement). L’opération de **vol des archives nucléaires iraniennes** en 2018 (exfiltration physique de centaines de kilos de documents classifiés depuis un entrepôt à Téhéran) a été présentée comme une opération Mossad emblématique — partiellement coordonnée avec des moyens cyber.
- **Hizbullah / Hamas** : opérations continues de renseignement et de disruption contre les infrastructures des organisations ennemies d’Israël.

### 18.4 Shin Bet : sécurité intérieure

**Shin Bet / Shabak / ISA** (Israel Security Agency) est le service de sécurité intérieure. Mission : contre-espionnage, contre-terrorisme dans les territoires, surveillance intérieure. Dispose de capacités cyber pour la surveillance des menaces envers la sécurité intérieure d’Israël (infiltration des organisations palestiniennes, surveillance des citoyens israéliens soupçonnés de liens avec des menaces).

L’usage par le Shin Bet de capacités cyber domestiques a fait l’objet de débats juridiques et politiques en Israël, notamment lors de la période COVID-19 (usage de capacités cyber pour le traçage de contacts — jugée disproportionnée par certains tribunaux).

### 18.5 INCD : coordination nationale

**Israel National Cyber Directorate** (INCD), créé 2017, est l’agence civile de coordination de la cybersécurité israélienne. Équivalent approximatif de CISA américaine ou de l’ANSSI française.

**Mission** : protection des infrastructures critiques israéliennes, coordination avec le secteur privé, publication d’advisories, gestion des crises cyber majeures. INCD opère un CERT-IL qui coordonne la réponse aux incidents nationaux.

**Rôle** : l’INCD est l’entité qui coordonne les réponses publiques israéliennes aux incidents cyber — publication d’alertes, collaborations avec les secteurs (santé, énergie, transports). Le directorate a un rôle central particulièrement depuis l’intensification des cyberattaques iraniennes post-octobre 2023.

### 18.6 Doctrine de préemption appliquée au cyber

La doctrine israélienne de sécurité nationale — shaped by l’histoire du pays — inclut traditionnellement un principe de **préemption** : agir avant que les menaces se matérialisent, plutôt que réagir après agression. Le **Begin Doctrine** (1981) — nommée d’après la frappe israélienne sur le réacteur nucléaire d’Osirak en Irak — codifie l’idée que Israël ne tolère pas que des adversaires régionaux acquièrent des capacités d’armes de destruction massive.

Appliquée au cyber, cette doctrine se traduit par :

- **Action continue plutôt que réactive** : Israël considère le cyberespace comme un espace d’action permanent, pas uniquement une réponse à agression.
- **Ciblage des programmes adverses** : les opérations cyber israéliennes visent souvent à dégrader les capacités adverses en amont — programme nucléaire iranien, capacités du Hezbollah, infrastructures de ciblage du Hamas.
- **Préemption sur les menaces asymétriques** : usage du cyber pour préempter des attentats, des frappes de roquettes, des tentatives d’infiltration.

### 18.7 Stuxnet : la première arme cyber OT

**Stuxnet (2010)** est l’opération cyber israélo-américaine emblématique. Déjà traité au Ch.14 (impact sur l’Iran) et abordé au Ch.21 (OT/ICS). Synthèse pour la dimension israélienne.

**Rôle israélien** : Israël a probablement apporté (selon les reconstructions journalistiques les plus solides, notamment *Confront and Conceal* de David Sanger et *Dark Territory* de Fred Kaplan) l’intelligence précise sur le site de Natanz (HUMINT, connaissance des centrifugeuses IR-1, configuration Siemens), co-développé certains composants, et probablement opéré l’exécution finale. Les États-Unis ont apporté les capacités cyber plus larges (NSA/TAO) et l’autorisation stratégique.

**Impact stratégique pour Israël** : retardement du programme iranien de 2-3 ans. Démonstration que le cyber peut produire des effets équivalents à des opérations militaires ciblées, sans les risques politiques d’une frappe conventionnelle sur un pays tiers.

**Conséquences non anticipées** : propagation non contrôlée de Stuxnet, découverte publique (2010), fuite du code et étude par tous les acteurs étatiques — prolifération des capacités OT qui a bénéficié à la Russie (Sandworm), à l’Iran (programme cyber massivement renforcé en réponse), et à d’autres acteurs.

### 18.8 Pipeline Unité 8200 → startups → surveillance commerciale

La trajectoire de beaucoup de vétérans Unité 8200 vers la surveillance commerciale mérite un traitement dédié car elle structure une part majeure du marché mondial des PSO.

**NSO Group** : fondé en 2010 par Niv Carmi, Shalev Hulio et Omri Lavie — vétérans de l’Unité 8200. Pegasus est devenu le spyware commercial le plus sophistiqué au monde. Ventes contrôlées par le **ministère israélien de la Défense** (les exportations de cyber-armes sont considérées comme des exportations d’armement en Israël, nécessitant des licences officielles) — ce qui signifie que le gouvernement israélien approuve la liste des clients étatiques de NSO. Cette structure a des implications géopolitiques : Israël utilise les autorisations NSO comme levier diplomatique (suspension/rétablissement selon les relations).

**Intellexa** : consortium européen avec forte présence israélienne, fondé par Tal Dilian (vétéran du renseignement militaire israélien). Concurrent direct de NSO.

**Candiru** : fondé en 2014 par d’anciens de l’Unité 8200. Spyware desktop.

**Paragon Solutions** : plus récent (2019), fondé par d’anciens de l’Unité 8200. Spyware mobile « Graphite », positionnement plus restrictif que NSO (refus déclaré de vendre à des régimes autoritaires — positionnement éthique contesté).

**Tensions éthiques** : le marché de la surveillance israélienne a fait l’objet de critiques croissantes (Pegasus Project 2021, usage contre des journalistes et dissidents dans des régimes autoritaires). Les réponses gouvernementales israéliennes ont oscillé entre la défense des entreprises (argumentaire économique et d’influence) et la restriction progressive (suspension de licences pour certains pays après scandales).

### 18.9 NSO / Pegasus : enjeux de gouvernance

**Pegasus** mérite une analyse dédiée comme cas emblématique des enjeux contemporains.

**Capacités techniques** : Pegasus exploite des **0-day iOS et Android** (parfois développés à l’interne, parfois achetés à des brokers). Le malware obtient un accès complet au terminal — messages (y compris messageries chiffrées type Signal, WhatsApp, Telegram lues en post-déchiffrement sur le terminal lui-même), géolocalisation, microphone et caméra activables à distance, extraction de données.

**Clients documentés** : gouvernements de dizaines de pays, incluant des démocraties européennes (Espagne, Hongrie, Pologne), des régimes moins démocratiques (Arabie saoudite, Émirats, Azerbaïdjan, Mexique), et plusieurs régimes autoritaires.

**Usages contestés documentés** :

- **Journalistes** : Jamal Khashoggi (journaliste saoudien dissident, assassiné en 2018 au consulat saoudien d’Istanbul — ses proches avaient Pegasus installé, suggérant l’usage pour le tracker avant l’assassinat), Cecilio Pineda (journaliste mexicain assassiné en 2017), des dizaines d’autres documentés par le **Pegasus Project** (consortium de 17 médias coordonnés par Forbidden Stories, 2021).
- **Dissidents** : exilés saoudiens, marocains, azerbaïdjanais, catalans en Espagne, journalistes d’opposition en Pologne.
- **Politiciens** : Emmanuel Macron et plusieurs dirigeants européens listés parmi les cibles potentielles. L’usage par le gouvernement polonais (PiS) contre des opposants a fait scandale en 2022.

**Réponses** :

- **Entity List US** (novembre 2021) : NSO ajouté, restrictions d’accès aux technologies américaines.
- **Apple et Meta ont porté plainte** contre NSO.
- **Enquêtes parlementaires** : enquête européenne PEGA (2022-2023) a produit des recommandations pour limiter l’usage des spywares en UE.
- **Difficultés financières de NSO** : sanctions, contentieux, changements de direction.

### 18.10 Conflit Israël-Hamas post-octobre 2023 : cyber dimension

Le conflit déclenché par l’attaque du Hamas le 7 octobre 2023 a amplifié la dimension cyber des opérations israéliennes et des réponses adverses.

**Cyberopérations israéliennes (peu documentées publiquement pour raisons opérationnelles)** :

- Renseignement cyber sur le Hamas au Liban et dans la bande de Gaza.
- Opérations de disruption contre les infrastructures de communication du Hamas et du Hezbollah.
- Reconnaissance cyber en amont des opérations militaires.

**Cyberopérations adverses** :

- **Iran / Agrius / IRGC** : wipers contre cibles israéliennes, opérations d’influence.
- **Hacktivistes pro-palestiniens / pro-Hamas** : volume massif d’attaques DDoS, défacement, tentatives d’intrusion contre des cibles israéliennes. Sophistication généralement basse.
- **Campagnes d’influence coordonnées** : amplification de narratifs sur les réseaux sociaux, deepfakes ponctuels.

**Cyberespace comme théâtre** : le conflit a illustré comment le cyber est intégré dans un conflit cinétique moderne — pas comme remplaçant du conventionnel, mais comme complément indispensable.

-----

## Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel

### 19.1 Contexte : la transformation 2014-2022

L’Ukraine est le **laboratoire mondial** de la cyberdéfense en temps de guerre. Sa trajectoire depuis 2014 (annexion de la Crimée, premières cyberattaques russes majeures) jusqu’à 2022 (invasion à grande échelle) et ses années de guerre ont produit un retour d’expérience unique — analysé, partagé, et étudié par toutes les agences cyber occidentales.

**Avant 2014** : l’Ukraine n’avait pas d’appareil cyber particulièrement mature. Les services de sécurité (SBU) avaient des capacités limitées. L’écosystème privé était modeste, avec une forte dépendance aux prestataires russes (historique post-soviétique).

**2014 (annexion Crimée + Donbass)** : les premières cyberattaques russes majeures en marge des opérations militaires — ciblage de la Commission électorale centrale ukrainienne en mai 2014 (tentative de manipulation des résultats de l’élection présidentielle, déjouée), BlackEnergy déployé contre le secteur énergie (avant 2015).

**2015-2021 — construction d’une posture cyber** :

- **Décembre 2015** : premier blackout cyber (BlackEnergy/KillDisk) contre trois distributeurs d’électricité. Prise de conscience nationale. Début de la coopération internationale intensive.
- **Décembre 2016** : Industroyer contre Kiev. Deuxième blackout.
- **2017** : NotPetya (supply chain M.E.Doc) — l’Ukraine absorbe le premier choc d’une cyberattaque qui deviendra mondiale.
- **2015-2022** : création et renforcement du **CERT-UA**, du **SSSCIP** (State Special Communications Service), renforcement des capacités cyber de la SBU. Coopération avec USCYBERCOM (hunt forward depuis 2018), NATO, UE.

**2022+ (invasion à grande échelle)** : l’Ukraine est devenue l’environnement de confrontation cyber le plus intense au monde. Les enseignements tirés de cette période sont étudiés partout.

### 19.2 L’appareil cyber ukrainien

**CERT-UA** (Computer Emergency Response Team of Ukraine) est le CERT national. Rattaché au SSSCIP, il conduit les réponses aux incidents cyber d’envergure nationale, publie des advisories techniques, et coordonne avec les partenaires internationaux. Le CERT-UA publie quotidiennement des alertes pendant la guerre — volume de publication parmi les plus élevés au monde.

**SSSCIP** (State Special Communications Service) est l’agence technique qui supervise la cybersécurité civile ukrainienne. Opère le CERT-UA, gère la sécurité des communications gouvernementales, et coordonne la défense des infrastructures critiques.

**SBU** (Sluzhba Bezpeky Ukrayiny — Service de sécurité d’Ukraine) est le principal service de renseignement et de sécurité. Dispose d’une branche cyber qui conduit des opérations de contre-intelligence, d’investigation cyber, et — selon certains rapports — des opérations cyber offensives ciblées.

**Ministry of Digital Transformation** : ministère dédié créé en 2019, dirigé par **Mykhailo Fedorov**. A joué un rôle central dans la coordination cyber depuis 2022 — publication de l’appel à la mobilisation de l’IT Army, coordination avec les grands fournisseurs cloud pour la migration d’urgence, communication publique internationale sur la guerre cyber.

**HUR** (Holovne Upravlinnia Rozvidky — Direction principale du renseignement, sous Ministry of Defense) conduit les opérations de renseignement militaire, y compris la dimension cyber. Certaines opérations ukrainiennes offensives publiquement revendiquées sont attribuées au HUR.

### 19.3 Coopération sans précédent avec le secteur privé et les alliés

La **coopération public-privé-international** mise en place autour de l’Ukraine est sans précédent dans l’histoire du cyber. Caractéristiques.

**Microsoft** : **Microsoft Threat Intelligence Center** (MSTIC) est en ligne avec l’Ukraine depuis 2022. Publications de dizaines de rapports publics documentant les attaques russes en temps réel, détection et neutralisation en quasi temps réel des malwares russes déployés (Microsoft a poussé des mises à jour de Defender qui ont neutralisé des wipers russes en heures). Microsoft a également migré des volumes considérables de données gouvernementales ukrainiennes vers Azure pour les protéger de frappes physiques (centres de données russes). Les rapports publics de Microsoft sur l’Ukraine sont devenus une référence de la documentation CTI.

**Google / Threat Analysis Group (TAG) et Mandiant** : **Project Shield** (protection DDoS gratuite pour les médias et les gouvernements à risque) a été massivement déployé en Ukraine. Mandiant (acquis par Google en 2022) a fourni un soutien IR continu.

**ESET** (Bratislava, Slovaquie) : ESET a une présence historique en Ukraine. La collaboration CERT-UA/ESET a permis la **détection et neutralisation d’Industroyer2** en avril 2022 — l’une des opérations défensives les plus remarquables de la guerre cyber. ESET publie régulièrement des analyses techniques détaillées des malwares russes déployés en Ukraine.

**Amazon Web Services** : migration d’urgence de données gouvernementales ukrainiennes vers AWS dans les premiers jours de l’invasion. Les datacenters ukrainiens étant des cibles potentielles de frappes physiques, la migration cloud a été une mesure de résilience essentielle.

**Starlink (SpaceX)** : connectivité satellitaire critique. Starlink a été déployé massivement en Ukraine dès février 2022, fournissant une connectivité résiliente aux forces armées, aux services publics, et aux civils dans les zones sans infrastructure télécom. Le rôle de Starlink est à double tranchant : dépendance stratégique envers un opérateur privé (SpaceX/Elon Musk) dont les décisions individuelles (limitation de l’usage au-dessus de la Crimée, par exemple) ont pu affecter les opérations militaires.

**Cloudflare** : protection DDoS, services de sécurité web.

**USCYBERCOM hunt forward** : équipes américaines déployées dans les réseaux ukrainiens depuis 2018, intensifiées massivement depuis 2022. Détection de menaces, partage en temps réel, remontée des TTP russes observées aux défenseurs occidentaux.

**Autres alliés européens** : CERT-EU, ANSSI (France), BSI (Allemagne), NCSC (UK), CERT-LT (Lituanie) — contributions techniques et analytiques. L’Estonie a joué un rôle particulier comme « voix cyber » européenne vis-à-vis de l’Ukraine (mémoire de l’attaque de 2007 contre l’Estonie).

Ce modèle de coopération public-privé-international a produit :

- Une **visibilité sans précédent** sur les TTP d’un acteur étatique (la Russie) dans un conflit réel.
- Une **vitesse de détection et de neutralisation** que l’Ukraine seule n’aurait pas pu atteindre.
- Un **laboratoire** pour les techniques défensives modernes, utilisable par tous les alliés.

### 19.4 Les opérations offensives ukrainiennes

Les opérations cyber offensives ukrainiennes sont documentées publiquement de manière fragmentaire. Plusieurs catégories :

**Opérations du HUR (renseignement militaire)** : cyber-sabotages contre des systèmes logistiques russes, compromission de caméras de surveillance russes (pour exfiltrer des flux vidéo révélant des mouvements militaires), compromission de systèmes de communication militaire russe, ciblage d’officiels russes.

**Opérations revendiquées publiquement** :

- **Compromission de banques russes** : plusieurs fuites de données de grandes banques russes revendiquées par des acteurs proches des services ukrainiens.
- **Hack de Rosaviatsiya** (régulateur aéronautique russe) : fuite de documents en 2022.
- **Opérations contre les médias d’État russes** : défacements ponctuels, interruptions de diffusion.

**Opérations en coordination avec l’IT Army** : certaines opérations de l’IT Army of Ukraine (voir 19.5) ont été publiquement reconnues par des responsables ukrainiens, suggérant une coordination informelle entre services et volontaires.

### 19.5 IT Army of Ukraine : zone grise hacktivisme/opération militaire

L’**IT Army of Ukraine** est un mouvement de volontaires cyber internationaux lancé publiquement par **Mykhailo Fedorov** (ministre de la Transformation numérique) via Telegram le 26 février 2022, deux jours après l’invasion.

**Modus operandi** : le canal Telegram de l’IT Army publie des listes de cibles russes (sites gouvernementaux, entreprises, médias) et appelle les volontaires à conduire des actions (DDoS principalement, parfois hacking plus sophistiqué). Le nombre de membres a dépassé 300 000 au plus haut. Une variété d’outils automatisés a été mise à disposition (scripts DDoS, plugins navigateur).

**Activités** :

- **DDoS massif** : sites gouvernementaux russes, banques, médias d’État, plateformes de service public.
- **Défacements** : sites russes compromis avec messages pro-ukrainiens.
- **Fuites de données** : publication de données russes exfiltrées par des membres plus sophistiqués.

**Zone grise** : l’IT Army illustre la difficulté contemporaine de classifier les opérations cyber.

- **Coordonnée par l’État** (via Fedorov) ? — oui, publiquement.
- **Composée de volontaires indépendants** ? — oui, majoritairement.
- **Hacktivisme ou opération militaire** ? — la question est juridiquement ouverte. Les membres de l’IT Army ne sont pas des combattants légalement (pas d’uniforme, pas d’incorporation militaire), mais ils conduisent des opérations coordonnées par l’État dans un conflit armé.
- **Cadre juridique** ? — les actions de l’IT Army constituent dans la plupart des juridictions des infractions cyber. Les participants prennent des risques juridiques réels selon leur pays de résidence.

Pour la doctrine internationale, l’IT Army pose des questions nouvelles — que ni le droit humanitaire international, ni le droit de la cybersécurité n’ont pleinement résolues. Voir Ch.26 pour les implications sur la responsabilité étatique.

### 19.6 Retour d’expérience technique : résilience sous feu

Plusieurs enseignements techniques majeurs de la guerre cyber en Ukraine.

**Résilience par la décentralisation** : les infrastructures ukrainiennes critiques ont été décentralisées (géographiquement et architecturalement). Un datacenter bombardé, un point de connectivité détruit n’interrompent pas l’ensemble — la redondance est la norme. Cette leçon est directement applicable à la préparation européenne.

**Migration cloud d’urgence** : la migration vers les clouds publics (AWS, Azure) des données gouvernementales critiques a été une mesure de résilience majeure. Préserve les données face aux frappes physiques, permet l’accès depuis n’importe où.

**Backup hors ligne et récupération rapide** : les multiples wipers russes ont imposé une discipline de backup rigoureuse. Les organisations ukrainiennes qui ont survécu aux wipers sont celles qui avaient des backups hors ligne régulièrement testés. Cette leçon est universelle.

**Détection rapide et réponse coordonnée** : la neutralisation d’Industroyer2 en quelques heures illustre ce qu’une collaboration CERT-UA/ESET bien rodée peut accomplir. La **rapidité** est un paramètre critique en cyberdéfense — la différence entre réponse en heures vs en jours peut être la différence entre incident contenu et catastrophe.

**Connectivité résiliente** : Starlink et les technologies satellitaires sont désormais des éléments stratégiques de la planification de résilience cyber.

### 19.7 Efficacité relative des cyberattaques dans un conflit cinétique

L’observation empirique la plus intéressante de la guerre cyber en Ukraine : le **cyber seul ne gagne pas une guerre**. Malgré l’intensité massive des cyberopérations russes, aucune n’a produit d’effet décisif sur le cours de la guerre conventionnelle.

**Pourquoi** :

- **Les blackouts cyber sont temporaires** : les blackouts de 2022 (réussis partiellement) ont été réparés en **heures à jours**, grâce à l’expérience accumulée depuis 2015 et aux équipes bien rodées. L’impact humain/militaire a été bien inférieur à celui d’une frappe physique équivalente.
- **Les frappes physiques sont plus efficaces pour les effets voulus** : lorsque la Russie a voulu détruire l’infrastructure énergétique ukrainienne de façon durable, elle a utilisé des missiles de croisière (hiver 2022-2023), pas des cyberattaques. Les missiles détruisent physiquement, les cyberattaques produisent des pannes de durée limitée.
- **La résilience peut être construite** : face à la menace cyber anticipée, l’Ukraine a construit une résilience qui a massivement limité l’impact effectif.

**Leçons pour les défenseurs européens** :

- **Anticiper** : le cyber sera un composant des conflits futurs, pas le composant central.
- **Construire la résilience** : backups, décentralisation, cloud, exercices.
- **Investir dans la coopération internationale** : le modèle Ukraine-alliés doit être reproductible.
- **Ne pas sur-investir dans la défense cyber au détriment de la défense conventionnelle** : le cyber complète, il ne remplace pas.

### 19.8 Implications pour l’Europe

L’expérience ukrainienne informe directement la préparation cyber européenne. Plusieurs implications opérationnelles.

**Pour les OIV et entités essentielles NIS 2** :

- Les infrastructures critiques européennes sont des cibles crédibles de pré-positionnement ou d’attaque directe dans un scénario d’escalade.
- La résilience sous bombardement (cinétique) doit être intégrée à la planification cyber — pas seulement la défense contre le cyber isolé.
- Les exercices cyber doivent inclure des scénarios de conflit composé (cyber + cinétique + économique).

**Pour les CERT nationaux et CSIRT sectoriels** :

- Le modèle de partage en temps réel (CERT-UA avec Microsoft, ESET, alliés) est à cultiver.
- Les relations préalables avec les vendors CTI majeurs sont indispensables — ne pas les construire pendant la crise.
- Les advisories CERT-UA sont une ressource permanente à intégrer aux workflows.

**Pour les agences nationales (ANSSI, BSI, NCSC)** :

- La coopération avec les pays de première ligne (États baltes, Pologne, Roumanie) est stratégique.
- Le soutien à l’Ukraine (partage de renseignement, assistance technique) nourrit en retour les capacités européennes.

**Pour l’UE** :

- **EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence — inspiré en partie de l’expérience ukrainienne.
- La coordination continue avec l’Ukraine reste une priorité stratégique.

Pour l’analyste cyber travaillant sur la menace russe contre l’Europe, la référence méthodologique est : « comment les mêmes TTP observées en Ukraine s’appliqueraient-elles à mon organisation si le conflit escaladait ? ». Cette approche traduit les enseignements ukrainiens en préparation concrète.

-----
