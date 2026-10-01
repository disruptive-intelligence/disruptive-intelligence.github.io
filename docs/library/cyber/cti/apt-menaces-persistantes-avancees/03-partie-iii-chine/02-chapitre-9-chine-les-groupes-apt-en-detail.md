---
title: 'Chapitre 9 — Chine : les groupes APT en détail'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie III — Chine
  - index.md
---

Ce chapitre approfondit le profil des neuf groupes APT chinois les plus importants. Chaque profil couvre mission, TTP signature, OPSEC, campagnes emblématiques.

## 9.1 APT41 / Winnti / Barium / Brass Typhoon

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

## 9.2 APT40 / Leviathan / TA423 (MSS Hainan)

**Attribution** : MSS Hainan State Security Department, publiquement établie par l’indictment DOJ de juillet 2021 (4 ressortissants chinois nommés, société écran Hainan Xiandun Technology Development).

**Mission** : ciblage maritime, naval, et Five Eyes. Priorités : domaine maritime (ports, chantiers navals, industrie maritime), universités spécialisées en technologies navales, recherche sous-marine, équipementiers militaires alliés.

**TTP signature** :

- **Exploitation d’appliances réseau** : APT40 est un exploiteur massif de vulnérabilités sur les appliances edge. Advisory international de juillet 2024 (AUKUS + Canada + Allemagne + Japon + Corée du Sud + Nouvelle-Zélande) détaille l’exploitation par APT40 de plusieurs CVE en days (voire heures) suivant leur publication — Ivanti, Fortinet, Citrix, SonicWall.
- **Web shells** : déploiement systématique (China Chopper notamment) pour la persistance.
- **Scripts PowerShell et LotL**.
- **Mouvement latéral** : Impacket, WMI, PsExec.
- **Exfiltration via cloud storage** (MEGA, OneDrive).

**Campagnes majeures** : ciblage maritime et naval (2013-présent) sur universités australiennes, canadiennes, américaines spécialisées maritime ; opérations contre les élections cambodgiennes (2018) ; exploitation massive Ivanti Connect Secure (2024).

## 9.3 APT10 / Stone Panda / Red Apollo (MSS Tianjin)

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

## 9.4 APT31 / Judgment Panda / Zirconium

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

## 9.5 Volt Typhoon

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

## 9.6 Salt Typhoon

**Attribution** : PRC state-sponsored, advisory CISA et partenaires (fin 2024). Attribution fine (MSS ou PLA) non publiquement précisée à date.

**Mission** : **espionnage via compromission des opérateurs télécoms**. Cibles principales : grands opérateurs télécoms américains (Verizon, AT&T, Lumen, et d’autres). Objectif : accès aux systèmes d’interception légale et aux communications de personnalités et cibles de haute valeur.

**Révélation publique** (octobre-décembre 2024) : le gouvernement américain a confirmé que Salt Typhoon avait compromis de multiples opérateurs télécoms US et maintenu l’accès pendant potentiellement plus d’un an. Les systèmes compromis incluaient les **Lawful Intercept Systems** — ceux utilisés par les opérateurs pour se conformer aux demandes légales d’interception des autorités américaines. La compromission de ces systèmes signifie que les attaquants pouvaient potentiellement voir **qui les autorités américaines surveillaient** — information stratégique majeure.

**Impact additionnel** : accès aux communications (appels, SMS, métadonnées) de millions d’Américains, incluant potentiellement des personnalités politiques (campagnes présidentielles Trump et Harris sont citées parmi les cibles confirmées). La gravité a conduit à des auditions au Congrès US et à des directives CISA obligeant les opérateurs à durcir leur infrastructure.

**TTP** : exploitation d’appliances edge, LotL, persistence via modifications de configurations légitimes des équipements télécoms. Sophistication comparable à Volt Typhoon mais avec un objectif différent (espionnage ciblé plutôt que pré-positionnement).

## 9.7 Flax Typhoon et Raptor Train

**Attribution** : PRC state-sponsored, liens avec la société **Integrity Technology Group** (basée à Pékin) — entreprise sanctionnée par l’OFAC en janvier 2025.

**Mission** : construction et opération d’un **botnet massif de dispositifs IoT compromis** (routeurs, caméras, NAS) pour servir d’infrastructure d’attaque à d’autres acteurs chinois. Modèle de « cyber-logistique » offensive.

**Opération Raptor Train** : le FBI, coordonné avec des partenaires internationaux, a démantelé en septembre 2024 le botnet **Raptor Train** opéré par Flax Typhoon. Le botnet comprenait **plus de 260 000 dispositifs compromis** dans le monde — dont une majorité aux États-Unis et en Europe. Les dispositifs compromis étaient utilisés comme nœuds relais pour d’autres opérations APT chinoises, masquant l’origine réelle des attaques.

**Leçon** : l’écosystème cyber chinois a industrialisé la production d’infrastructure offensive via des contractors spécialisés. Ce modèle rappelle certaines pratiques de cybercriminalité organisée (Infrastructure-as-a-Service) mais appliqué aux opérations étatiques.

## 9.8 Mustang Panda / Bronze President / HoneyMyte

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

## 9.9 APT27 / Emissary Panda / Bronze Union

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
