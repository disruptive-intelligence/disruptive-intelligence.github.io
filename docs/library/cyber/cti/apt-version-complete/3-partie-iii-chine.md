---
title: PARTIE III — CHINE
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 3
chapters: 8
---

> **Ce que cette partie apprend.** Comprendre la doctrine cyber chinoise (long game, espionnage économique systémique, pré-positionnement stratégique), cartographier l’appareil cyber chinois (MSS civil, PLA militaire, contractors), identifier les groupes APT chinois majeurs, et analyser les campagnes et tendances récentes — y compris la rupture que constitue Volt Typhoon.
> 
> **Ce qu’elle ne couvre pas.** Le traitement approfondi de Volt Typhoon comme cas de pré-positionnement (Ch.22 et Ch.31), les aspects spécifiques OT industriels (Ch.20-21).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître un tradecraft chinois (volumétrie, DLL sideloading, long dwell time), distinguer une opération MSS d’une opération PLA, situer une compromission chinoise dans la stratégie de rattrapage technologique, et anticiper les zones de ciblage prioritaires.

-----

## Chapitre 8 — Chine : contexte, doctrine et appareil cyber

### 8.1 Priorités géopolitiques et principes doctrinaux

La stratégie cyber chinoise ne peut pas se comprendre sans la stratégie globale de la RPC. Quatre priorités structurent l’ensemble.

**Dominance technologique et rattrapage industriel** : depuis les plans Made in China 2025 (2015) et les successeurs (China Standards 2035, stratégie IA 2030), la Chine s’est fixé comme objectif stratégique de devenir leader technologique dans une série de secteurs — semiconducteurs, IA, énergie verte, biotechnologies, aérospatial, télécommunications 5G/6G. Le cyber est un instrument central de ce rattrapage : vol de propriété intellectuelle à très grande échelle, ciblage des centres de R&D, compromission de la supply chain technologique occidentale. Les estimations américaines du préjudice cumulé du vol de propriété intellectuelle par la Chine sont contestées mais situent l’ordre de grandeur en centaines de milliards de dollars par an.

**Question Taïwan** : la réunification avec Taïwan est une priorité stratégique fondamentale du PCC. Le cyber sert la préparation à plusieurs niveaux : collecte de renseignement sur les positions américaines et alliées dans le Pacifique (pré-positionnement dans les infrastructures US de Guam et du Pacifique — documenté par Volt Typhoon), ciblage des institutions taïwanaises (gouvernement, défense, partis politiques), influence sur l’opinion taïwanaise (opérations sur les réseaux sociaux).

**Route de la Soie numérique** : extension géo-économique de la Belt and Road Initiative dans l’espace numérique. Fourniture d’infrastructures télécoms et de surveillance à des partenaires internationaux (Huawei, ZTE, Dahua, Hikvision), exportation de modèles de gouvernance numérique, accès privilégié aux données des partenaires. Le cyber alimente cette stratégie par la collecte sur les concurrents et la présence dans les nouvelles infrastructures.

**Contrôle politique interne et répression étendue** : surveillance des Ouïghours, Tibétains, dissidents, défenseurs des droits humains, médias indépendants, communautés religieuses non-autorisées. Le ciblage de la diaspora (surveillance à l’étranger, pressions sur les familles restées en Chine) est documenté dans de nombreux cas. Le cyber est intégré à cette architecture de contrôle.

**Doctrine de la « guerre sans limites »** : formulée par les colonels Qiao Liang et Wang Xiangsui dans *Unrestricted Warfare* (1999), elle postule que la guerre ne se limite pas aux moyens militaires et peut se mener sur tous les terrains (économique, financier, informationnel, cyber, juridique). Cette formulation informe la vision intégrée du cyber comme instrument de puissance.

**Integrated Deterrence et long game** : contrairement à la doctrine russe qui accepte l’escalade destructive ouverte, la doctrine chinoise privilégie le long terme, la patience, et l’intégration multi-instruments. L’activation publique destructive est rare ; l’espionnage massif et le pré-positionnement sont la norme. Le **dwell time** des opérations chinoises est souvent parmi les plus longs observés — des intrusions documentées ont été maintenues 5 à 10 ans avant découverte.

### 8.2 Le MSS : renseignement civil et décentralisation opérationnelle

Le **MSS** (Ministry of State Security, 国家安全部) est le principal service de renseignement civil chinois. Successeur de plusieurs organes historiques (réorganisé en 1983), il conduit à la fois le renseignement extérieur, le contre-espionnage intérieur, et une partie de la répression politique.

Une spécificité structurante du MSS : la **décentralisation opérationnelle**. Contrairement à une agence centralisée type NSA, le MSS fonctionne via un **réseau de bureaux régionaux** (au niveau des provinces et de certaines grandes villes) qui disposent d’une autonomie opérationnelle significative. Plusieurs bureaux régionaux ont été publiquement identifiés comme conduisant des cyberopérations :

- **MSS Tianjin Bureau** : associé à **APT10** / Stone Panda. Indicté publiquement par le DOJ US en décembre 2018 — noms spécifiques d’opérateurs MSS Tianjin publiés.
- **MSS Hainan State Security Department** : associé à **APT40** / Leviathan. Indicté DOJ en juillet 2021, avec la création d’une société écran (« Hainan Xiandun Technology Development Co. ») pour la couverture opérationnelle.
- **MSS Shanghai Bureau**, **MSS Guangzhou Bureau**, **MSS Jiangsu Bureau** : d’autres bureaux régionaux identifiés dans divers rapports.

Cette décentralisation a des conséquences pour l’analyse : différents bureaux régionaux ont des tradecrafts légèrement différents, des priorités sectorielles distinctes, et parfois des chevauchements qui suggèrent une coordination imparfaite entre bureaux. Le MSS central fournit l’orientation stratégique, mais l’exécution opérationnelle peut varier.

### 8.3 Le PLA : réorganisation post-2015 et SSF

L’appareil cyber militaire chinois a connu une **réorganisation majeure en 2015-2016**. L’emblématique **Unit 61398** (Shanghai, département 3 du PLA — identifiée publiquement par Mandiant en 2013, inculpée par le DOJ en 2014) a été dissoute dans sa forme initiale. Les capacités cyber militaires ont été regroupées dans la **Strategic Support Force (SSF)** créée en décembre 2015, qui rassemble cyber, espace, guerre électronique et opérations d’information dans une structure unifiée.

La SSF comprend un **Network Systems Department** (NSD) qui est la branche cyber principale du PLA. Des rapports récents suggèrent que la SSF a été elle-même réorganisée en 2024 dans une nouvelle structure (Information Support Force), mais les informations publiques sur ces évolutions restent partielles.

Des unités spécifiques du PLA continuent d’être associées à des opérations cyber : unités successeurs de l’ancienne Unit 61398, **Unit 78020** (Chengdu Region Technical Reconnaissance Bureau) associée à plusieurs opérations de ciblage de l’Inde et de l’Asie du Sud-Est, **Unit 61486** et autres TRB (Technical Reconnaissance Bureaux).

La distinction MSS/PLA pour l’attribution des opérations : **le MSS tend à mener l’espionnage stratégique et économique, le PLA tend à mener les opérations de reconnaissance militaire et le pré-positionnement**. Mais les frontières sont perméables et plusieurs groupes APT ont des liens mixtes ou suspectés avec les deux.

### 8.4 Le modèle des contractors civils

Une caractéristique unique de l’écosystème cyber chinois est l’**utilisation massive de contractors civils** pour les opérations offensives. Des entreprises privées chinoises sont mandatées par le MSS ou le PLA pour conduire des opérations cyber — soit pour la conception d’outils, soit pour l’opération directe.

Ce modèle offre plusieurs avantages pour l’État chinois : déni plausible (les opérateurs ne sont pas formellement des employés de l’État), flexibilité des ressources (monter en capacité sans créer d’emplois publics), accès à des talents (attirer des profils qui ne travailleraient pas dans le secteur public), compartimentation (limiter la visibilité interne sur les opérations).

### 8.5 Le leak i-Soon de février 2024

**i-Soon (Anxun Information Technology)** est une société basée à Shanghai, spécialisée en outils de surveillance et en opérations cyber pour le compte de multiples clients gouvernementaux chinois (MSS, PLA, polices provinciales). **En février 2024, un leak massif de données internes d’i-Soon** a révélé le fonctionnement de cet écosystème de contractors.

Plus de 500 fichiers ont été publiés sur GitHub par un contributeur anonyme (probablement un mécontent interne). Le leak comprend : échanges internes (WeChat, emails), documentation technique d’outils offensifs, listings de victimes, listings de clients gouvernementaux, négociations commerciales, plaintes d’employés.

**Outils documentés** :

- Implants Windows avec capacités keylogging, capture d’écran, exfiltration.
- Implants Android avec capacités SMS, géolocalisation, microphone.
- Plateforme de Twitter/X monitoring et manipulation (faux comptes, amplification).
- Outils de bruteforce Outlook et de phishing.
- Plateforme de surveillance mobile vendue à des bureaux de sécurité publique chinois pour la surveillance de dissidents et de minorités.
- Outils de ciblage de routeurs et NAS.

**Clients identifiés** : MSS (central et bureaux régionaux), bureaux de sécurité publique de nombreuses provinces, PLA.

**Victimes documentées** : ciblage de gouvernements asiatiques (Mongolie, Népal, Pakistan, Malaisie, Thaïlande, Vietnam, Cambodge, Laos), d’organisations des droits humains, de médias, de militants Hong Kong, et de la diaspora ouïghoure.

**Impact analytique** : confirmation directe de l’écosystème contractor, des relations client-fournisseur entre entités étatiques chinoises et entreprises privées, et de l’ampleur du ciblage de dissidents et de minorités. L’analyse détaillée du leak a été publiée par SentinelOne, Sekoia, Harfang Lab, et plusieurs chercheurs indépendants. Elle reste une lecture essentielle pour comprendre l’écosystème cyber chinois contemporain.

### 8.6 Ciblage sectoriel : les priorités chinoises

Les priorités de ciblage chinoises révèlent les priorités stratégiques.

**Semiconducteurs et high-tech** : priorité absolue. Ciblage de TSMC, ASML, Applied Materials, Tokyo Electron, Samsung — et de toute la supply chain. Objectif : rattraper le retard technologique dans un secteur où les sanctions américaines (CHIPS Act 2022) ont durci les restrictions d’exportation.

**Aéronautique et défense** : Lockheed Martin, Boeing, BAE Systems, Airbus, Dassault, Thales. Le programme F-35 est documenté comme largement compromis par des acteurs chinois depuis les années 2000, ce qui aurait contribué au développement accéléré du chasseur J-20 chinois.

**Énergie** : pétrole/gaz, nucléaire, énergies renouvelables. Pré-positionnement documenté dans les infrastructures électriques US et du Pacifique (Volt Typhoon).

**Biotechnologies et pharmaceutique** : vol de recherche (vaccins COVID en 2020, thérapies oncologiques, biotechnologies d’avant-garde). Ciblage particulièrement intense depuis 2020.

**Maritime et logistique** : APT40 a été massivement actif contre les entreprises maritimes, les ports, et les chantiers navals. Reflète l’intérêt chinois pour la domination maritime.

**Télécommunications** : infrastructure télécom, équipementiers, opérateurs. **Salt Typhoon** (2024) a compromis des systèmes d’interception légale de multiples opérateurs télécoms US — accès potentiel aux communications de millions d’Américains.

**Diaspora et minorités** : Ouïghours, Tibétains, Hongkongais, dissidents. Utilisation du cyber pour la surveillance à l’étranger, la collecte sur les familles restées en Chine, et parfois le harcèlement.

**Think tanks et académique** : producteurs d’analyses sur la Chine (CSIS, Atlantic Council, Chatham House, IFRI, etc.), universités spécialisées en études chinoises, chercheurs individuels.

**Politique** : ciblage de parlementaires (APT31 contre le UK et le US), partis politiques, membres de la société civile engagés dans les politiques Chine.

### 8.7 Fil rouge — BLACKOUT Épisode 4

> **⚡ BLACKOUT — Épisode 4 : la compatibilité avec le profil chinois**
> 
> Le CERT examine si les TTP observées sur BLACKOUT sont compatibles avec les acteurs chinois documentés, notamment Volt Typhoon et clusters similaires.
> 
> **Cohérences** :
> 
> - **Exploitation d’appliance edge (Ivanti CVE-2024-21887)** : Volt Typhoon et plusieurs autres acteurs chinois ont massivement exploité Ivanti fin 2023 / début 2024 (advisory CISA de février 2024). **Forte cohérence avec le profil chinois**.
> - **Living off the Land** : Volt Typhoon se caractérise par un LotL quasi exclusif, avec peu ou pas de malware custom. BLACKOUT montre un PsExec, du Kerberoasting, du DLL sideloading — beaucoup de LotL, et pas de malware custom identifié à ce stade. **Cohérence forte**.
> - **Pré-positionnement OT sans action** : signature exacte de Volt Typhoon, qui maintient des accès dans les infrastructures critiques US sans action observable. **Cohérence très forte**.
> - **Patience opérationnelle** : l’attaquant est présent depuis au moins 42 jours sans action visible. Long dwell time cohérent avec le profil chinois.
> 
> **Décalages** :
> 
> - **Géographie** : Volt Typhoon a été principalement documenté aux US et dans le Pacifique (Guam). Un opérateur énergie européen est une cible inhabituelle pour ce cluster spécifique, même si des cibles européennes ne sont pas exclues et que des clusters chinois similaires peuvent être actifs en Europe.
> - **Beaconing régulier (27 min ± 3 min)** : Volt Typhoon a plutôt des patterns d’activité très irréguliers (accès ponctuels via les routeurs SOHO compromis). Un beaconing régulier serait plus atypique. Mais d’autres clusters chinois utilisent bien du beaconing classique.
> - **Contexte géopolitique immédiat** : pas de tension Taïwan aiguë à la date de l’incident, ce qui rend un déclenchement de pré-positionnement chinois à ce moment précis moins « naturel » que le pré-positionnement russe (conflit ukrainien actif).
> 
> **Diagnostic CERT** : profil **également compatible avec un acteur chinois** — peut-être pas Volt Typhoon spécifiquement, mais un cluster chinois lié. **H2 Chine** reste plausible, avec une confiance à ce stade entre faible et modérée.
> 
> L’incertitude demeure. Le CERT continue l’investigation — notamment pour identifier des artefacts techniques additionnels qui pourraient trancher entre profil russe et profil chinois.

-----

## Chapitre 9 — Chine : les groupes APT en détail

Ce chapitre approfondit le profil des neuf groupes APT chinois les plus importants. Chaque profil couvre mission, TTP signature, OPSEC, campagnes emblématiques.

### 9.1 APT41 / Winnti / Barium / Brass Typhoon

**Attribution** : services d’État chinois, probablement MSS. Indicté par le DOJ US en août 2020 — 5 ressortissants chinois nommés, associés au MSS.

**Particularité historique** : **le double casquette espionnage étatique + cybercrime personnel**. APT41 mène des opérations d’espionnage validées par l’État chinois **et simultanément** des opérations cybercriminelles personnelles (ciblage de l’industrie du jeu vidéo pour voler de la monnaie virtuelle, ransomware opportuniste, fraude). Cette double activité est unique dans l’écosystème APT mondial et reflète probablement une tolérance étatique.

**Mission étatique** : espionnage industriel (santé, télécoms, high-tech, défense), ciblage politique, reconnaissance géopolitique.

**TTP signature** :

- **Supply chain compromise** massif : **CCleaner** (2017, 2,27 millions de machines infectées), **ASUS LiveUpdate** (opération ShadowHammer, 2018-2019), divers sites.
- **Exploitation rapide de vulnérabilités** : APT41 exploite des CVE dans les heures ou jours suivant publication, notamment sur Citrix, Microsoft Exchange, Pulse Secure, F5.
- **Rootkits et bootkits** : MoonBounce (bootkit UEFI), famille Winnti (implant Windows/Linux, la signature), PipeMon, Crosswalk.
- **Mouvement latéral** : RDP, SMB, Impacket, Mimikatz.

**Campagnes majeures** :

- **Opérations supply chain CCleaner et ASUS** : infection massive initiale, ciblage sélectif en phase 2.
- **Ciblage sanitaire COVID-19** (2020) : exfiltration de recherche vaccin.
- **Opérations contre l’industrie du jeu vidéo** : ciblage d’éditeurs asiatiques.
- **Indictment 2020** : 5 ressortissants nommés, responsables d’opérations contre 100+ victimes dans multiple pays.

### 9.2 APT40 / Leviathan / TA423 (MSS Hainan)

**Attribution** : MSS Hainan State Security Department, publiquement établie par l’indictment DOJ de juillet 2021 (4 ressortissants chinois nommés, société écran Hainan Xiandun Technology Development).

**Mission** : ciblage maritime, naval, et Five Eyes. Priorités : domaine maritime (ports, chantiers navals, industrie maritime), universités spécialisées en technologies navales, recherche sous-marine, équipementiers militaires alliés.

**TTP signature** :

- **Exploitation d’appliances réseau** : APT40 est un exploiteur massif de vulnérabilités sur les appliances edge. Advisory international de juillet 2024 (AUKUS + Canada + Allemagne + Japon + Corée du Sud + Nouvelle-Zélande) détaille l’exploitation par APT40 de plusieurs CVE en days (voire heures) suivant leur publication — Ivanti, Fortinet, Citrix, SonicWall.
- **Web shells** : déploiement systématique (China Chopper notamment) pour la persistance.
- **Scripts PowerShell et LotL**.
- **Mouvement latéral** : Impacket, WMI, PsExec.
- **Exfiltration via cloud storage** (MEGA, OneDrive).

**Campagnes majeures** : ciblage maritime et naval (2013-présent) sur universités australiennes, canadiennes, américaines spécialisées maritime ; opérations contre les élections cambodgiennes (2018) ; exploitation massive Ivanti Connect Secure (2024).

### 9.3 APT10 / Stone Panda / Red Apollo (MSS Tianjin)

**Attribution** : MSS Tianjin Bureau, établie publiquement par l’indictment DOJ de décembre 2018 (2 ressortissants chinois nommés).

**Mission** : espionnage industriel massif, avec ciblage particulier des **MSP** (Managed Service Providers) pour atteindre leurs clients finaux.

**TTP signature** :

- **Opération Cloud Hopper** (2014-2018, détaillée au Ch.10) : compromission de grands MSP mondiaux pour pivoter vers leurs clients — multiplication du scope d’une seule compromission par des centaines de clients accessibles.
- **Spear-phishing** ciblé avec macros Office.
- **Malware custom** : HAYMAKER, PlugX (partagé avec d’autres APT chinoises), Redleaves, ChChes, UPPERCUT.
- **Living off the Land** et web shells.

**Campagnes majeures** :

- **Opération Cloud Hopper** : compromission de plusieurs grands MSP internationaux (IBM, HPE notamment) entre 2014 et 2018, pivot vers les clients des MSP. Un des cas emblématiques de compromission supply chain via prestataire. Documenté par PwC et BAE Systems (2017).
- **Ciblage industriel** : aéronautique, ingénierie, pharmaceutique, énergie dans de multiples pays.

**Évolution** : APT10 moins visible post-indictment 2018 — probablement réorganisation ou fragmentation, mais plusieurs opérations récentes suggèrent que des opérateurs anciens d’APT10 sont toujours actifs sous d’autres clusters.

### 9.4 APT31 / Judgment Panda / Zirconium

**Attribution** : MSS, établie par indictments DOJ (mars 2024) et actions UK (mars 2024). 7 ressortissants chinois nommés, association explicite au MSS Hubei State Security Department.

**Mission** : espionnage politique ciblé. Cibles particulières : parlementaires, opposants politiques, journalistes critiques, entreprises de défense et aérospatiales.

**TTP signature** :

- **Spear-phishing** très ciblé avec emails de suivi et escalade sociale.
- **Exploitation de vulnérabilités Exchange** (notamment lors de la vague ProxyLogon 2021).
- **Ciblage d’infrastructure electorale** : APT31 a été identifié comme ciblant des infrastructures associées à des campagnes politiques.

**Campagnes majeures** :

- **Ciblage parlementaires UK** : en 2024, le UK a publiquement attribué à APT31 des ciblages de parlementaires britanniques critiques de la Chine (incluant des membres de l’Inter-Parliamentary Alliance on China — IPAC).
- **Ciblage US** : campagnes similaires documentées contre des parlementaires et décideurs US.
- **Infrastructure électorale** : ciblage de la Commission électorale britannique (2021-2022, révélé publiquement en 2024).

**Impact** : les indictments 2024 ont été accompagnés de **sanctions coordonnées** (US, UK, NZ) contre les personnes nommées et l’entreprise écran associée (Wuhan Xiaoruizhi Science and Technology). Démonstration de la coopération diplomatique renforcée dans la réponse aux APT chinois.

### 9.5 Volt Typhoon

**Attribution** : PRC state-sponsored, probablement PLA ou affilié. Advisory conjoint NSA/CISA/FBI + Five Eyes (mai 2023, réitéré 2024). Aucun indictment public à date, contrairement à d’autres groupes.

**Mission** : **pré-positionnement stratégique dans les infrastructures critiques américaines et du Pacifique**. Pas d’espionnage massif, pas d’exfiltration, pas d’action destructive. Uniquement : établir et maintenir un accès dormant.

**Cibles documentées** : opérateurs de télécommunications, fournisseurs d’énergie électrique, systèmes d’eau, infrastructures de transport aux États-Unis et dans les territoires du Pacifique (Guam est particulièrement ciblée — point stratégique en cas de conflit Taïwan).

**TTP signature** — le profil Volt Typhoon est **extrême dans sa pureté opérationnelle** :

- **Exploitation d’appliances edge** : vulnérabilités sur routeurs SOHO, VPN, firewalls non patchés (Fortinet FortiGate, Cisco RV, NetGear, ASUS RT).
- **LotL quasi exclusif** : PowerShell, WMI, net.exe, ntdsutil, ping, tracert, ipconfig, netsh, reg.exe, wmic, certutil. **Aucun malware custom identifié** à date de l’advisory 2023.
- **Credentials légitimes** : vol de credentials admin via credential dumping puis utilisation prolongée. Aucun compte créé par l’attaquant (éviterait la détection).
- **C2 via routeurs SOHO compromis** : les implants utilisent des **routeurs résidentiels compromis** (des clients domestiques US) comme points de sortie. Le trafic C2 semble donc provenir d’IP résidentielles US légitimes — fondement dans le trafic domestique, détection réseau quasi impossible sans inspection approfondie.
- **Activité très intermittente** : pas de beaconing régulier, accès occasionnels, actions limitées au minimum nécessaire pour maintenir la présence.

**Signification stratégique** : Volt Typhoon est interprété par la communauté de renseignement américaine comme une **capacité de dissuasion/représailles chinoise** liée au scénario Taïwan. Le message implicite : « si vous intervenez militairement pour défendre Taïwan, nous pouvons frapper vos infrastructures critiques ». C’est potentiellement la menace cyber stratégique qui définira la prochaine décennie.

**Démantèlement partiel** : le FBI a démantelé en janvier 2024 un botnet de routeurs Cisco RV domestiques qui servait d’infrastructure C2 à Volt Typhoon. Opération **KV Botnet**, conduite sous mandat judiciaire. Le botnet a été neutralisé, mais Volt Typhoon dispose probablement d’infrastructures alternatives.

**Traitement détaillé** : Ch.22 (pré-positionnement comme paradigme) et Ch.31 (cas complet).

### 9.6 Salt Typhoon

**Attribution** : PRC state-sponsored, advisory CISA et partenaires (fin 2024). Attribution fine (MSS ou PLA) non publiquement précisée à date.

**Mission** : **espionnage via compromission des opérateurs télécoms**. Cibles principales : grands opérateurs télécoms américains (Verizon, AT&T, Lumen, et d’autres). Objectif : accès aux systèmes d’interception légale et aux communications de personnalités et cibles de haute valeur.

**Révélation publique** (octobre-décembre 2024) : le gouvernement américain a confirmé que Salt Typhoon avait compromis de multiples opérateurs télécoms US et maintenu l’accès pendant potentiellement plus d’un an. Les systèmes compromis incluaient les **Lawful Intercept Systems** — ceux utilisés par les opérateurs pour se conformer aux demandes légales d’interception des autorités américaines. La compromission de ces systèmes signifie que les attaquants pouvaient potentiellement voir **qui les autorités américaines surveillaient** — information stratégique majeure.

**Impact additionnel** : accès aux communications (appels, SMS, métadonnées) de millions d’Américains, incluant potentiellement des personnalités politiques (campagnes présidentielles Trump et Harris sont citées parmi les cibles confirmées). La gravité a conduit à des auditions au Congrès US et à des directives CISA obligeant les opérateurs à durcir leur infrastructure.

**TTP** : exploitation d’appliances edge, LotL, persistence via modifications de configurations légitimes des équipements télécoms. Sophistication comparable à Volt Typhoon mais avec un objectif différent (espionnage ciblé plutôt que pré-positionnement).

### 9.7 Flax Typhoon et Raptor Train

**Attribution** : PRC state-sponsored, liens avec la société **Integrity Technology Group** (basée à Pékin) — entreprise sanctionnée par l’OFAC en janvier 2025.

**Mission** : construction et opération d’un **botnet massif de dispositifs IoT compromis** (routeurs, caméras, NAS) pour servir d’infrastructure d’attaque à d’autres acteurs chinois. Modèle de « cyber-logistique » offensive.

**Opération Raptor Train** : le FBI, coordonné avec des partenaires internationaux, a démantelé en septembre 2024 le botnet **Raptor Train** opéré par Flax Typhoon. Le botnet comprenait **plus de 260 000 dispositifs compromis** dans le monde — dont une majorité aux États-Unis et en Europe. Les dispositifs compromis étaient utilisés comme nœuds relais pour d’autres opérations APT chinoises, masquant l’origine réelle des attaques.

**Leçon** : l’écosystème cyber chinois a industrialisé la production d’infrastructure offensive via des contractors spécialisés. Ce modèle rappelle certaines pratiques de cybercriminalité organisée (Infrastructure-as-a-Service) mais appliqué aux opérations étatiques.

### 9.8 Mustang Panda / Bronze President / HoneyMyte

**Attribution** : PRC state-sponsored, MSS probablement.

**Mission** : ciblage principal de la **diaspora chinoise et des minorités** (Tibétains, Ouïghours, opposants politiques Hong Kong), **ASEAN**, **Europe** (depuis 2022 notamment).

**TTP signature** :

- **Spear-phishing** avec documents leurre très contextualisés (thèmes sur la diaspora, les ONG, les affaires asiatiques, les tensions régionales).
- **Malware signature** : **PlugX** (backdoor historique largement utilisée par les APT chinoises, variantes propres à Mustang Panda), **ToneShell**, **Korplug** (ancêtre PlugX), **Hodur**.
- **USB-based propagation** : Mustang Panda utilise activement les clés USB comme vecteur de propagation vers des réseaux moins connectés (diaspora, ONG en zones de conflit).
- **DLL sideloading** massif : signature technique retrouvée dans quasi toutes les opérations Mustang Panda.

**Campagnes récentes** :

- **Ciblage ONG et diaspora tibétaine/ouïghoure** (continu).
- **Ciblage gouvernements européens** (2022-2025) : notamment autour du conflit ukrainien et des sujets Taïwan. Documenté par ESET, Check Point, Trend Micro.
- **Ciblage ASEAN** : activité continue sur les pays d’Asie du Sud-Est (Philippines, Vietnam, Indonésie, Thaïlande).

### 9.9 APT27 / Emissary Panda / Bronze Union

**Attribution** : PRC state-sponsored.

**Mission** : espionnage industriel (industrie, défense, énergie, aérospatial), avec ciblage historique large (US, Europe, Moyen-Orient).

**TTP signature** :

- **Watering hole attacks** : compromission de sites fréquentés par les cibles.
- **Exploitation de vulnérabilités** sur serveurs exposés.
- **Malware** : **HyperBro** (backdoor signature), **SysUpdate**, **ZxShell**.
- **Web shells** pour persistence.
- **DLL sideloading**.

**Activité récente** : moins documentée que les autres groupes mais persistante. Ciblage observé contre des organisations européennes de défense et d’ingénierie.

-----

## Chapitre 10 — Chine : campagnes de référence et tendances 2023-2026

Ce chapitre présente les campagnes chinoises les plus emblématiques, et analyse les tendances récentes qui dessinent l’évolution de la menace.

### 10.1 Opération Cloud Hopper (APT10, 2014-2018)

**Acteur** : APT10 (MSS Tianjin). **Paradigme** : compromission des **MSP** (Managed Service Providers) comme multiplicateur de scope.

**Synthèse** : entre 2014 et 2018, APT10 a compromis un ensemble de grands **MSP internationaux** — entreprises qui gèrent l’infrastructure IT de centaines ou milliers de clients finaux. Parmi les MSP compromis (documentés publiquement) : IBM, HPE, et plusieurs autres. Une fois dans le MSP, APT10 utilisait les accès privilégiés légitimes du MSP vers ses clients pour pénétrer leurs environnements — pivot silencieux, protégé par la confiance implicite qui existe entre un MSP et ses clients.

**Scope victimes** : estimations entre des dizaines et des centaines de clients finaux touchés à travers le monde, dans des secteurs variés (aérospatial, ingénierie, énergie, télécoms, pharma, médias).

**Découverte et publication** : l’opération a été découverte et documentée publiquement en 2017-2018 par **PwC** et **BAE Systems** dans un rapport conjoint. L’indictment DOJ de décembre 2018 a consolidé l’attribution à APT10 / MSS Tianjin et nommé deux ressortissants chinois.

**Leçons** :

- La supply chain IT (MSP, fournisseurs de services managés) est un vecteur APT majeur. Un MSP compromis expose des dizaines à des milliers de clients.
- La confiance implicite entre prestataire et client doit être réévaluée (Zero Trust appliqué aux prestataires internes).
- Les prestataires doivent être considérés comme faisant partie du périmètre de sécurité — d’où les obligations de sécurité renforcées imposées aux MSP par NIS 2.

### 10.2 Hafnium / ProxyLogon (2021)

**Acteur** : Hafnium (MSS, probablement Hubei). **Paradigme** : exploitation massive d’une vulnérabilité 0-day Exchange pour compromettre des dizaines de milliers d’organisations en quelques jours.

**Synthèse** : début mars 2021, Microsoft publie des correctifs d’urgence pour quatre vulnérabilités Exchange (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065 — collectivement nommées **ProxyLogon**). L’exploitation avait commencé début janvier 2021 par un acteur étatique (Hafnium) de manière ciblée. À partir de fin février / début mars 2021, l’exploitation s’est massifiée — des dizaines de groupes ont commencé à exploiter la vulnérabilité, souvent pour déposer des web shells pour un accès futur.

**Impact** : estimations entre **30 000 et 250 000 organisations compromises mondialement** en l’espace de quelques semaines. Impact massif sur les organisations européennes notamment, beaucoup utilisant Exchange on-premises. Le MOIE français (Ministère de l’Intérieur) et de nombreuses administrations européennes ont été affectés.

**Attribution publique** : en juillet 2021, les États-Unis, le Royaume-Uni, l’Union européenne, l’OTAN et plusieurs autres pays ont conjointement attribué ProxyLogon au MSS chinois — une attribution publique coordonnée sans précédent dans sa portée.

**Leçons** :

- Les vulnérabilités 0-day sur les services exposés massivement (Exchange, VPN, passerelles) produisent des compromissions industrielles.
- La prolifération post-publication est massive : une fois une CVE connue, elle est exploitée par des dizaines d’acteurs en quelques jours.
- Le patching d’urgence des services exposés est un impératif.

### 10.3 Microsoft 2023 / Storm-0558

**Acteur** : Storm-0558 (nomenclature Microsoft, acteur chinois sous investigation). **Paradigme** : compromission d’une clé de signature cloud permettant l’accès aux emails gouvernementaux.

**Synthèse** : en juillet 2023, Microsoft révèle publiquement que Storm-0558 a compromis une **clé privée de signature MSA** (Microsoft Account) en 2021 et l’a utilisée pour forger des tokens d’authentification permettant d’accéder aux emails Outlook.com et à certaines ressources Exchange Online. Le groupe a utilisé ces tokens pour accéder aux emails d’**environ 25 organisations gouvernementales**, dont le Département d’État américain et des gouvernements européens.

L’enquête ultérieure, notamment par la **Cyber Safety Review Board** (CSRB — institution fédérale américaine), a produit un **rapport public** en 2024 qui est une lecture fondatrice pour comprendre les défaillances dans la sécurité du cloud Microsoft. Le rapport identifie une série de défaillances : gestion inadéquate des clés cryptographiques, visibilité insuffisante des anomalies, culture de sécurité critiquée.

**Impact** :

- Accès à des communications gouvernementales sensibles américaines et européennes pendant plusieurs mois.
- Érosion de la confiance dans la sécurité cloud de Microsoft — directe conséquence commerciale et politique.
- Déclenchement d’investigations réglementaires et de durcissements imposés.

**Distinction avec le breach Microsoft 2023-2024 par APT29** : ce sont **deux incidents distincts**. Storm-0558 (MSS chinois) en juillet 2023 via compromission de clé de signature ; APT29 (SVR russe) en novembre 2023 - janvier 2024 via password spray et OAuth abuse.

### 10.4 Salt Typhoon 2024 — le breach télécoms US

**Acteur** : Salt Typhoon (PRC). **Paradigme** : espionnage stratégique via compromission des télécoms.

**Synthèse** : révélé publiquement entre octobre et décembre 2024, Salt Typhoon a compromis de multiples opérateurs télécoms américains majeurs (Verizon, AT&T, Lumen confirmés ; d’autres suspectés ou en investigation). La compromission aurait duré **au moins un an, peut-être davantage**, avant détection.

**Accès obtenu** :

- **Systèmes d’interception légale (CALEA — Communications Assistance for Law Enforcement Act)** : les systèmes utilisés par les opérateurs pour répondre aux demandes d’interception des autorités américaines. Accès à ces systèmes signifie **voir qui les autorités surveillaient** — contre-espionnage d’une valeur stratégique exceptionnelle.
- **Communications** : appels, SMS, métadonnées de millions d’utilisateurs, avec ciblage particulier de personnalités politiques et décideurs (campagnes présidentielles Trump et Harris citées).

**Réponse** :

- Auditions au Congrès.
- Directives CISA obligeant le durcissement de l’infrastructure télécom.
- Recommandation publique d’utiliser le chiffrement de bout en bout (Signal, WhatsApp) pour les communications sensibles — officiels US ont pour la première fois publiquement recommandé des messageries chiffrées plutôt que SMS/appels classiques.

**Leçons** : les infrastructures télécoms sont des cibles APT de premier ordre. Les systèmes d’interception légale sont des cibles extrêmement sensibles — un État adversaire qui les compromet retourne littéralement la capacité de surveillance contre son propriétaire.

### 10.5 Mustang Panda contre l’Europe 2023-2025

**Acteur** : Mustang Panda. **Paradigme** : extension géographique du ciblage chinois vers l’Europe dans le contexte du conflit ukrainien et des tensions Taïwan.

**Synthèse** : depuis 2022, Mustang Panda a intensifié ses opérations contre des cibles européennes. Objectifs probables : collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine (et de la Russie), collecte sur les positions Taïwan, ciblage des ONG pro-démocratie, surveillance de la diaspora chinoise en Europe.

**Campagnes documentées** :

- ESET a publié plusieurs rapports (2022-2024) documentant le ciblage européen par Mustang Panda, notamment gouvernements, fournisseurs de défense, ONG spécialisées.
- Check Point a documenté l’exploitation de thèmes géopolitiques (Ukraine, Taïwan, relations UE-Chine) comme leurres de phishing.

**Impact** : pas de compromission massive publiquement revendiquée, mais confirmation d’une présence chinoise significative dans le paysage cyber européen — rappel que l’Europe n’est pas épargnée par les APT chinoises malgré une focalisation historique perçue sur les États-Unis et l’Asie.

### 10.6 Campagnes contre les infrastructures critiques européennes

Plusieurs rapports 2023-2025 documentent des campagnes chinoises contre des infrastructures critiques en Europe :

**Secteur énergie** : ciblage d’opérateurs de distribution d’électricité, d’opérateurs pétroliers et gaziers. Advisory ANSSI et BSI ont mentionné publiquement des tentatives d’intrusion sans détailler les cibles.

**Télécommunications européennes** : ciblage de plusieurs opérateurs télécoms européens dans une extension probable du modèle Salt Typhoon.

**Secteur maritime** : APT40 continue d’être très actif contre les ports européens (Rotterdam, Hambourg, Anvers notamment) et les entreprises maritimes européennes.

**Infrastructures de recherche** : universités techniques européennes, centres R&D.

La tendance : l’Europe est un théâtre APT chinois croissant, moins documenté publiquement que les États-Unis (les pays européens communiquent moins sur les incidents étatiques) mais actif.

### 10.7 Évolution du tradecraft chinois

Le tradecraft chinois a évolué significativement sur la période 2015-2026. Synthèse des évolutions.

**Phase 1 (années 2000 - 2014) : force brute et volumétrie**. L’approche Unit 61398 et APT10 historique : scan massif, exploitation opportuniste, phishing de masse. Beaucoup de cibles, sophistication technique modeste, OPSEC moyen. Le rapport Mandiant APT1 de 2013 a catalysé une prise de conscience et probablement une réorganisation.

**Phase 2 (2015 - 2020) : consolidation et professionnalisation**. Réorganisations post-Unit 61398 et post-accord Xi-Obama (2015, qui a temporairement fait baisser l’espionnage économique chinois aux US). Émergence de groupes plus compartimentés, professionnalisation des TTP, adoption de techniques modernes (DLL sideloading, abus de services légitimes).

**Phase 3 (2020 - présent) : furtivité et pré-positionnement**. L’émergence de Volt Typhoon (2021+) marque une rupture : groupes chinois capables d’opérations ultra-furtives, LotL exclusif, maintenant des accès pendant des années sans signaux détectables. Le ciblage s’oriente vers les appliances edge (cibles sans EDR, privilégiées), les télécoms (pour l’espionnage stratégique), et les infrastructures critiques (pour le pré-positionnement).

**Phase 4 émergente (2024+) : industrialisation via contractors**. Le leak i-Soon a révélé l’étendue de l’écosystème contractor civil. Le modèle se professionnalise : des entreprises développent des outils à destination de multiples clients étatiques, produisent des infrastructures réutilisables (Raptor Train), fournissent des services « clé en main ».

La trajectoire : montée en sophistication continue, fragmentation croissante entre services officiels et contractors multiples, extension géographique (moins concentré US, plus global), et augmentation du volume d’opérations sous-radar qui ne sont identifiées que après plusieurs années de maintien d’accès.

### 10.8 Tendance structurelle : fragmentation de l’attribution

La conséquence analytique majeure de ces évolutions : l’**attribution précise des opérations chinoises est devenue plus difficile**, pas moins. Pourquoi ?

**Prolifération des groupes** : des dizaines de clusters suivis, parfois distinguables seulement par des différences marginales de TTP. Le chevauchement d’outils (PlugX utilisé par plusieurs groupes), d’infrastructure partagée, et de tradecraft similaire rend la discrimination difficile.

**Opacification des liens MSS/PLA/contractors** : qui commandite quelle opération ? Les indictments publics attribuent à des bureaux MSS spécifiques, mais les contractors peuvent travailler simultanément pour plusieurs clients étatiques, et la coordination inter-services est imparfaite.

**Sophistication croissante** : moins d’erreurs opérationnelles, moins d’artefacts d’attribution, usage intensif des abus de services légitimes et du LotL qui produisent moins de signatures.

**Implications pour l’analyste** : face à une intrusion attribuée « à la Chine », préciser **quel groupe** spécifiquement est souvent difficile ou impossible sans accès à du renseignement non-public. La discipline consiste à : (1) tester plusieurs hypothèses (MSS Hainan vs MSS Tianjin vs PLA vs contractor) via ACH, (2) coter la confiance prudemment (« probablement acteur chinois, groupe non déterminé avec confiance »), (3) ne pas laisser le prestige d’une attribution précise forcer une conclusion sous-étayée.

-----
