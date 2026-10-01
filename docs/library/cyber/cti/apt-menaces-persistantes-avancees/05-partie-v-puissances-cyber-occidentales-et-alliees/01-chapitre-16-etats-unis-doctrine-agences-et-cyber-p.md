---
title: 'Chapitre 16 — États-Unis : doctrine, agences et cyber power'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie V — Puissances cyber occidentales et alliées
  - index.md
---

## 16.1 Vue d’ensemble de l’appareil cyber américain

L’appareil cyber américain est le plus puissant et le plus structuré au monde. Sa caractéristique distinctive est la **séparation institutionnelle** entre plusieurs fonctions qui, dans d’autres pays, sont confondues : le renseignement (NSA, CIA) est séparé de l’action militaire offensive (USCYBERCOM), elle-même séparée du law enforcement (FBI), elle-même séparée de la protection des infrastructures civiles (CISA).

Cette séparation n’est pas parfaite — les fonctions se chevauchent (USCYBERCOM et la NSA partagent un même directeur, le « dual-hat » arrangement), et la coordination est permanente — mais elle structure les missions, les responsabilités, et les cadres juridiques. Elle contraste avec les modèles russe (GRU conduit simultanément espionnage et destruction), chinois (MSS et PLA avec fragmentation et contractors), et iranien (IRGC intègre action et renseignement).

Les quatre piliers de l’appareil cyber américain sont : **USCYBERCOM** (commandement militaire), **NSA** (renseignement SIGINT/cyber), **FBI** (law enforcement cyber), **CISA** (protection des infrastructures critiques). La CIA dispose également de capacités cyber intégrées à ses opérations clandestines, et d’autres agences (DIA, Treasury/OFAC, DOJ) interviennent dans leurs domaines respectifs.

## 16.2 USCYBERCOM : le commandement militaire cyber

**US Cyber Command** (USCYBERCOM) est le combatant command unifié du Département de la Défense chargé des opérations cyber. Créé en 2009 comme sous-commandement de STRATCOM, élevé en combatant command unifié en 2018.

**Mission** : défendre les réseaux du Département de la Défense, soutenir les commandements militaires régionaux et fonctionnels par des opérations cyber, et conduire les opérations cyber militaires offensives autorisées.

**Structure** : USCYBERCOM comprend les **Cyber Mission Forces (CMF)**, environ **6 200 opérateurs** répartis en **133 équipes** :

- **Cyber National Mission Teams (CNMT)** : défendent le pays contre les cybermenaces majeures, coordonnent avec les agences civiles.
- **Cyber Combat Mission Teams (CCMT)** : soutiennent les commandements militaires régionaux dans leurs opérations (supporting CENTCOM, INDOPACOM, EUCOM, etc.).
- **Cyber Protection Teams (CPT)** : défendent les réseaux DoD spécifiques.
- **Cyber Support Teams (CST)** : soutien analytique et planning.

**Dual-hat arrangement** : le directeur de la NSA est simultanément commandant d’USCYBERCOM. Cet arrangement, critiqué périodiquement pour les risques de confusion de missions (renseignement vs action militaire), a été maintenu parce qu’il optimise l’usage des ressources (NSA fournit l’accès technique, USCYBERCOM fournit les autorités d’action).

## 16.3 La NSA : renseignement SIGINT et capacités cyber offensives

La **National Security Agency** (NSA) est l’agence de renseignement d’origine électromagnétique des États-Unis. Elle collecte le SIGINT mondial et développe des capacités cyber offensives majeures.

**Tailored Access Operations (TAO)** — renommé en 2017 **Computer Network Operations** (CNO) puis **Computer Network Exploitation** — est la branche historique de la NSA pour les opérations cyber offensives. TAO développait et déployait des outils d’intrusion pour la collecte de renseignement. Les capacités TAO ont été partiellement révélées par les fuites **Shadow Brokers** (2016-2017), qui ont publié des outils internes dont **EternalBlue** (exploit SMB utilisé ensuite par WannaCry et NotPetya), **DoublePulsar**, **Fuzzbunch**, et d’autres. Ces fuites ont été l’un des événements les plus graves de l’histoire du renseignement américain — des outils offensifs étatiques passés dans le domaine public ont été exploités massivement par des acteurs criminels et étatiques.

**Threat Operations Center (NTOC)** : coordination défensive, détection de menaces, partage avec les alliés.

**Opérations documentées** :

- **Co-attribution Stuxnet** (avec Israël, 2010) : sabotage du programme nucléaire iranien. Attribution solide via le livre *Confront and Conceal* de David Sanger et investigations ultérieures.
- **Collecte SIGINT mondiale** : révélée par les fuites Snowden (2013) qui ont documenté des programmes comme PRISM, XKeyscore, la collecte massive de métadonnées téléphoniques.

La NSA est également l’une des agences qui publient le plus d’**advisories techniques** de haute qualité en coordination avec CISA et le FBI — une transformation majeure depuis les années 2010, où la NSA partageait peu publiquement ses analyses.

## 16.4 La CIA et ses capacités cyber clandestines

La **Central Intelligence Agency** dispose de capacités cyber intégrées à ses opérations de renseignement humain et clandestines. Le **Center for Cyber Intelligence** (CCI) a été révélé partiellement par les fuites **Vault 7** (2017), où WikiLeaks a publié des documents internes de la CIA documentant des outils d’intrusion pour Windows, macOS, iOS, Android, systèmes IoT, et voitures connectées.

Contrairement à la NSA (collecte SIGINT massive) et USCYBERCOM (opérations militaires), la CIA cible des cas très spécifiques dans le cadre d’opérations clandestines plus larges. Son empreinte publique cyber est volontairement limitée — les capacités révélées par Vault 7 ont conduit à des enquêtes internes et à des arrestations (un ancien employé CIA a été condamné en 2022 pour les fuites).

## 16.5 Le FBI : investigation, démantèlement, indictments

Le **Federal Bureau of Investigation** conduit les investigations cyber, les démantèlements d’infrastructure, et les poursuites judiciaires. Son **Cyber Division** coordonne avec les bureaux régionaux qui enquêtent sur les incidents.

Le FBI a acquis un rôle central dans la réponse aux APT via plusieurs fonctions :

- **Investigation des incidents majeurs** : compromission de victimes US, collecte de preuves, coordination avec les cibles.
- **Démantèlements d’infrastructure** : opérations judiciaires de saisie de serveurs, de domaines, de cryptomonnaies. Quelques cas emblématiques : **Emotet** (janvier 2021, coordination Europol), **Hive** (janvier 2023, infiltration et déchiffrement pour les victimes), **Qakbot** (août 2023, « Operation Duck Hunt »), **LockBit** (février 2024, « Operation Cronos » coordonnée NCA/FBI/Europol), **Volt Typhoon KV Botnet** (janvier 2024), **Flax Typhoon Raptor Train** (septembre 2024), **Snake/Turla Medusa** (mai 2023).
- **Indictments** : mise en accusation formelle d’opérateurs APT étrangers. Les indictments DOJ sont devenus un instrument diplomatique central. Exemples emblématiques : Unit 61398/PLA (2014, 5 officiers chinois), APT10/MSS Tianjin (2018), APT28/GRU (2018, 12 officiers), APT41 (2020, 5 ressortissants chinois), APT40/MSS Hainan (2021, 4 ressortissants), APT31/MSS Hubei (2024, 7 ressortissants, avec sanctions coordonnées).

L’effet des indictments est débattu. Les inculpés ne seront probablement jamais jugés (les pays sponsors ne les extradent pas). Mais l’effet de **naming and shaming** est réel — il réduit la marge de déni plausible, impose un coût diplomatique au sponsor, et fournit à la communauté CTI un socle documentaire sur les opérateurs.

## 16.6 CISA : protection des infrastructures critiques

**Cybersecurity and Infrastructure Security Agency** (CISA), créée en 2018 au sein du Département de la Sécurité Intérieure (DHS), est l’agence civile de coordination de la cybersécurité aux États-Unis. Elle protège les infrastructures critiques, publie des advisories, coordonne avec le secteur privé et les gouvernements locaux, et conduit des exercices nationaux.

**Publications CISA** : les advisories CISA (souvent conjoints avec NSA, FBI, et alliés Five Eyes) sont devenus une référence mondiale. Les **Joint Cybersecurity Advisories (JCSA)** documentent les TTP d’acteurs étatiques avec un niveau de détail opérationnel exceptionnel. Exemples : advisories Volt Typhoon (2023, 2024), APT40 (2024), Salt Typhoon (2024-2025), et des dizaines d’autres.

**Known Exploited Vulnerabilities (KEV)** : CISA maintient une liste publique des vulnérabilités activement exploitées par les acteurs menaçants. La **Binding Operational Directive 22-01** impose aux agences fédérales US de patcher les vulnérabilités du KEV dans des délais stricts. Le KEV est utilisé mondialement comme référence de priorisation.

**Shields Up** : posture de vigilance renforcée annoncée par CISA post-invasion ukrainienne (février 2022), recommandations pratiques à toutes les organisations américaines.

**Secure by Design** : initiative CISA pour responsabiliser les éditeurs logiciels (designs sécurisés par défaut, transparence sur les vulnérabilités).

CISA est devenue sous son leadership post-2021 (Jen Easterly puis ses successeurs) l’une des agences cyber les plus visibles et les plus influentes mondialement — un modèle de coordination civile/militaire/privée que plusieurs pays européens cherchent à adapter.

## 16.7 Defend Forward et Persistent Engagement

La **doctrine du defend forward / persistent engagement** est l’innovation doctrinale américaine majeure de la décennie 2010-2020. Formulée publiquement par le général Paul Nakasone (directeur NSA et commandant USCYBERCOM de 2018 à 2024) et codifiée dans la **Cyber Strategy du DoD** (2018), elle marque une rupture avec la posture défensive classique.

**Principe** : ne pas attendre l’attaque pour agir, mais **opérer en continu dans les réseaux adverses** pour dégrader leurs capacités, collecter du renseignement tactique, et démontrer une présence dissuasive.

**Concept de « contestation permanente »** : le cyberespace n’est pas un domaine de paix ponctuée d’incidents, mais un domaine de confrontation continue. USCYBERCOM opère quotidiennement dans les réseaux adverses, pas uniquement en réponse à une attaque identifiée.

**Différence avec les doctrines précédentes** : avant defend forward, la doctrine américaine était largement défensive — réagir après compromission, protéger les réseaux nationaux. Defend forward inverse la logique : l’initiative doit être américaine, pas adverse.

**Débats** : la doctrine est critiquée par certains analystes comme favorisant l’escalade (risque d’incidents non désirés), par d’autres comme insuffisamment agressive. Le fait qu’elle soit publique — une doctrine offensive ouvertement assumée — est lui-même une rupture notable avec la tradition de discrétion autour des capacités offensives.

## 16.8 Hunt Forward : les opérations en territoire allié

Le concept de **Hunt Forward Operations (HFO)** est dérivé de defend forward. Il consiste à déployer des équipes USCYBERCOM **dans les réseaux de pays alliés** pour détecter des menaces que les alliés n’ont pas les moyens de détecter seuls.

**Principe** : l’équipe USCYBERCOM arrive chez l’allié à l’invitation de ce dernier, avec un cadre juridique et opérationnel négocié. Elle opère sur les réseaux de l’allié (sensor placement, chasse aux menaces, analyse), partage les résultats avec l’allié et rentre aux États-Unis avec l’expérience et les IoC collectés. Bénéfice croisé : l’allié gagne en sécurité, les États-Unis gagnent en connaissance des TTP adverses observées dans des environnements variés.

**Opérations documentées** :

- **Ukraine** : hunt forward teams américaines déployées dans les réseaux ukrainiens depuis 2018. Volume massif d’activité depuis 2022. Retour d’expérience direct sur les TTP russes (Sandworm, APT28, Gamaredon, Unit 29155). Pour les Ukrainiens : détection renforcée. Pour les Américains : connaissance de terrain des TTP russes qui alimente ensuite les défenses des autres alliés.
- **Europe de l’Est** : Estonie, Lettonie, Lituanie, Pologne, Roumanie, Monténégro.
- **Autres alliés** : déployments documentés également dans des pays non européens.

Le nombre total d’opérations dépasse 50 déploiements publiquement reconnus au moment des rapports annuels de USCYBERCOM.

## 16.9 Opérations documentées majeures

**Stuxnet (co-attribution 2010)** : sabotage du programme nucléaire iranien à Natanz, en coopération avec Israël. Détaillé au Ch.14, Ch.18, Ch.21.

**Démantèlement d’Emotet (janvier 2021)** : opération coordonnée FBI/Europol/Eurojust qui a saisi l’infrastructure d’Emotet (l’un des plus grands botnets et loaders criminels du monde). Emotet s’est partiellement reconstitué en 2021-2022 mais n’a jamais retrouvé son niveau précédent.

**Démantèlement de Qakbot (août 2023)** : « Operation Duck Hunt », FBI et partenaires internationaux. Le FBI a exploité le protocole de contrôle de Qakbot pour désinstaller le malware des 700 000+ machines infectées — opération offensive law enforcement sur le modèle de Medusa/Snake.

**Opération Medusa / Snake (mai 2023)** : neutralisation de l’implant Snake (Turla) sur les machines infectées via un outil développé par le FBI, exploitant des fonctionnalités du malware lui-même. Détaillé au Ch.6.

**Démantèlement LockBit (février 2024)** : Operation Cronos, NCA britannique en lead avec FBI et Europol. Saisie de l’infrastructure, publication de contenus moqueurs sur le site .onion de LockBit (ironie retournée — les forces de l’ordre ont utilisé l’interface du groupe pour afficher des messages à leur encontre), arrestations, offre gratuite de déchiffreur.

**Démantèlement KV Botnet Volt Typhoon (janvier 2024)** : neutralisation du botnet de routeurs Cisco RV/NetGear compromis utilisé par Volt Typhoon comme infrastructure C2.

**Démantèlement Raptor Train Flax Typhoon (septembre 2024)** : neutralisation du botnet de 260 000+ dispositifs IoT compromis opéré par Flax Typhoon.

## 16.10 Le droit et les sanctions comme instruments

Les États-Unis ont **instrumentalisé le droit** comme réponse aux cybermenaces étatiques d’une manière qu’aucun autre pays n’a égalée en ampleur.

**Indictments DOJ** (section 16.5) : mise en accusation formelle d’opérateurs APT étrangers, effet de naming and shaming.

**Sanctions OFAC** : le Département du Trésor peut désigner des personnes, entités, et adresses crypto comme « Specially Designated Nationals » (SDN), interdisant aux entités américaines tout commerce avec elles. La sanction de **Tornado Cash** (août 2022) a été un précédent majeur — première sanction d’un smart contract dans l’histoire. Les sanctions OFAC ont ciblé des opérateurs APT nommés, des contractors (Integrity Technology Group — chinois, sanctionné janvier 2025), des entités PSO (NSO, Candiru sanctionnés Entity List 2021 ; Intellexa sanctionnée 2023-2024), et des adresses crypto utilisées pour le blanchiment nord-coréen.

**Entity List du Commerce** : liste d’entités interdites d’accès aux technologies américaines. Usage étendu contre Huawei (2019), ZTE, plusieurs fournisseurs de surveillance chinois (Hikvision, Dahua), NSO, Candiru, Intellexa.

**Executive Orders** : **EO 14028** (mai 2021, Biden — « Improving the Nation’s Cybersecurity ») a restructuré la réponse fédérale au cyber suite à SolarWinds. **EO sur les spywares commerciaux** (mars 2023) restreint l’acquisition de spywares commerciaux par le gouvernement fédéral américain.

## 16.11 Particularités doctrinales vs les autres blocs

Synthèse comparative des spécificités américaines :

- **Séparation institutionnelle** : renseignement (NSA, CIA), militaire (USCYBERCOM), law enforcement (FBI), protection civile (CISA) sont distincts. Modèle atypique — la Russie, la Chine, l’Iran intègrent davantage ces fonctions.
- **Usage massif du droit** : indictments, sanctions, Entity List, Executive Orders. Les États-Unis sont le seul pays qui utilise le droit comme instrument diplomatique cyber à cette échelle.
- **Publicité des attributions** : les États-Unis communiquent publiquement sur les attributions avec un niveau de détail sans équivalent. Advisory techniques (NSA/CISA/FBI), rapports annuels, déclarations officielles.
- **Defend forward / hunt forward** : doctrine d’initiative plutôt que de réaction, opérations ouvertement assumées dans les réseaux adverses et alliés.
- **Coordination Five Eyes** : partage de renseignement et d’attribution avec UK, Canada, Australie, Nouvelle-Zélande (Ch.17).
- **Contrôle démocratique et judiciaire** : les opérations cyber américaines sont encadrées par des autorités légales (Title 10 pour le militaire, Title 50 pour le renseignement), des supervisions congressionnelles (Senate Intelligence Committee, House Intelligence Committee), et des contrôles judiciaires (FISA Court pour certaines collectes). Ces mécanismes ne sont pas parfaits mais distinguent le modèle américain de celui d’autres grandes puissances cyber.

Pour l’analyste : face à une activité attribuée aux États-Unis, les considérations différent de celles sur les autres acteurs — question de l’autorité légale invoquée, cadre de commandement (Title 10 vs Title 50), probabilité d’attribution publique à terme, possibilité de réponse diplomatique publique.

-----
