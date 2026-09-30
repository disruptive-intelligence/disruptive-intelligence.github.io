---
title: PARTIE IV — DPRK, IRAN ET AUTRES ACTEURS
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 4
chapters: 8
---

> **Ce que cette partie apprend.** Comprendre le modèle DPRK unique au monde (cyber comme instrument économique du régime), maîtriser les profils des groupes nord-coréens (Lazarus et sous-groupes, Kimsuky, APT43), situer l’Iran dans ses rivalités régionales (MOIS vs IRGC, social engineering extrême), identifier les autres acteurs régionaux et mercenaires cyber, et comprendre les zones grises crime-État.
> 
> **Ce qu’elle ne couvre pas.** Le cas détaillé Lazarus/crypto (Ch.30), les outils techniques de détection spécifiques aux infostealers et au dark web (cours Écosystèmes cybercriminels et Dark Web), les aspects doctrinaux français et européens (Ch.26 et Annexe G).
> 
> **Ce que vous saurez faire après cette partie.** Distinguer un ciblage financier DPRK d’un espionnage classique, reconnaître le social engineering iranien, situer les mercenaires cyber commerciaux (Pegasus, Predator) dans le paysage, et analyser les zones grises entre cybercrime et action étatique.

-----

## Chapitre 11 — DPRK : contexte, groupes et modèle unique

### 11.1 Le cyber comme instrument économique du régime

La République Populaire Démocratique de Corée (DPRK) présente un cas **unique au monde** : c’est le seul État qui utilise le cyber **principalement comme source de revenus** pour contourner les sanctions internationales et financer le régime et son programme d’armement nucléaire et balistique.

Cette particularité découle de la configuration stratégique nord-coréenne. Sous sanctions internationales sévères depuis les années 2000 (renforcées par les résolutions ONU 2006, 2009, 2013, 2016, 2017), coupée des circuits financiers légaux, la DPRK doit financer son régime et surtout son programme nucléaire/balistique par des canaux alternatifs : commerce illégal (charbon, pêche), trafic d’êtres humains, contrefaçon de devises, et depuis les années 2010, **cybervol**.

Les estimations de revenus générés par le cyber nord-coréen varient selon les sources mais s’accordent sur des ordres de grandeur massifs :

- **Rapport ONU** (Panel of Experts) : plusieurs milliards de dollars cumulés depuis 2017.
- **Chainalysis** (rapport annuel) : en 2022, la DPRK a volé environ 1,7 milliard de dollars en crypto-actifs. En 2023, ~1 milliard. En 2024, les volumes sont repartis à la hausse. Le vol Bybit de février 2025 (~1,5 milliard de dollars) est à lui seul le plus gros vol crypto de l’histoire.
- **US Treasury / UN** : cumulé entre 3 et 6+ milliards de dollars sur la décennie 2014-2024.

Pour contextualiser : le PIB total de la DPRK est estimé à environ 30 milliards de dollars par an (difficile à mesurer précisément). Le cybervol annuel représente donc plusieurs pourcents du PIB — équivalent, en proportion, à ce qu’un État comme la France générerait s’il dégageait 80-100 milliards d’euros par an de cybervol. L’ordre de grandeur est macroéconomique.

### 11.2 Le RGB : Reconnaissance General Bureau

Le **RGB** (정찰총국 — Reconnaissance General Bureau) est le service de renseignement militaire nord-coréen. Il supervise l’ensemble des opérations cyber offensives de la DPRK. Les opérateurs cyber sont formés dans des programmes militaires dédiés (Kim Il-sung Military University, autres institutions spécialisées) et intègrent ensuite les bureaux opérationnels du RGB.

Le RGB est structuré en plusieurs bureaux, dont les principaux pour le cyber sont :

- **Bureau 121** : cyberopérations.
- **Lab 110** : développement de malware (certaines sources indiquent une structure fluctuante).

Une caractéristique opérationnelle unique : les **opérateurs cyber nord-coréens sont souvent stationnés à l’étranger**. Principalement en Chine (Shenyang, Dandong — proches de la frontière DPRK), mais aussi en Russie, Malaisie, Singapour, et dans plusieurs pays d’Asie du Sud-Est. Raisons : meilleure connectivité Internet (la Corée du Nord a une bande passante limitée et surveillée), OPSEC (rendre le ciblage plus difficile), et évite la détection automatique par origine IP coréenne du Nord.

Cette configuration produit des artefacts d’attribution parfois trompeurs : certaines opérations Lazarus apparaissent initialement comme provenant de Chine ou de Russie, avant que l’analyse approfondie (comportement, TTP, liens avec d’autres opérations DPRK) ne confirme l’origine nord-coréenne.

### 11.3 Lazarus Group / Diamond Sleet — vue d’ensemble

**Lazarus Group** est le nom générique sous lequel l’écosystème cyber nord-coréen est souvent regroupé. En réalité, **Lazarus est un ensemble de sous-groupes** avec des missions distinctes, tous rattachés au RGB mais avec des spécialisations fonctionnelles.

**Mission globale** : espionnage, cybervol (crypto et traditionnel), opérations ciblées politiques, et depuis 2017 opérations de dégâts collatéraux massifs (WannaCry).

**Particularités opérationnelles** :

- **Multi-plateforme** : Lazarus développe des implants Windows, macOS, Linux — l’un des rares écosystèmes APT à couvrir les trois systèmes avec la même profondeur.
- **Sophistication variable selon les opérations** : des opérations ultra-sophistiquées (3CX supply chain) côtoient des opérations plus standards.
- **Réutilisation d’infrastructure et de code** : les liens entre opérations Lazarus sont souvent détectables par des réutilisations d’outils, ce qui a facilité la consolidation du cluster.

Les principales sous-structures dans l’écosystème Lazarus :

### 11.4 APT38 / BlueNoroff / Sapphire Sleet

**Spécialisation** : cyber-braquages financiers. Ciblage : banques, institutions financières, exchanges de crypto, plateformes DeFi.

**Campagnes historiques** :

- **Bangladesh Bank (février 2016)** : compromission du terminal SWIFT de la banque centrale du Bangladesh, transfert de 81 millions de dollars vers des comptes aux Philippines. Un 951 millions de dollars supplémentaires ont été bloqués grâce à une faute de frappe dans un ordre de virement (« fandation » au lieu de « foundation » ayant déclenché un examen manuel). **Premier cyber-braquage bancaire majeur par un acteur étatique**.
- **Ciblage continu SWIFT** : tentatives multiples contre d’autres banques (Vietnam TPBank, Équateur, plusieurs en Asie) avec des succès variables.

**Pivot crypto (2018+)** : BlueNoroff/APT38 a ensuite tourné massivement son attention vers les crypto-actifs, plus faciles à monétiser que les virements bancaires traditionnels. Ciblage d’exchanges, de services DeFi, de bridges cross-chain. Les campagnes emblématiques sont détaillées au Ch.12.

**TTP signature** :

- **Social engineering ciblé** sur employés d’institutions financières et d’exchanges crypto.
- **Malware custom multi-plateforme** : FALLCHILL, BADCALL, HOPLIGHT, DTrack, AppleJeus (macOS, ciblage spécifique crypto).
- **Supply chain** pour atteindre les clients finaux (3CX 2023 notamment, géré en cas au Ch.30).

### 11.5 Kimsuky / Emerald Sleet

**Spécialisation** : espionnage diplomatique et nucléaire. Ciblage : chercheurs spécialisés sur la péninsule coréenne, diplomates, ministères des affaires étrangères, think tanks d’études coréennes, universités, décideurs impliqués dans les négociations sur le programme nucléaire nord-coréen.

**TTP signature** :

- **Spear-phishing extrêmement ciblé** : emails personnalisés adressés à des chercheurs et fonctionnaires nommés, avec contexte précis (invitations à des conférences, demandes d’entretien, thèmes de recherche).
- **Credential harvesting** : fausses pages de login (Gmail, ProtonMail, services académiques coréens, services gouvernementaux sud-coréens).
- **Malware** : **BabyShark** (backdoor légère), **AppleSeed**, **FlowerPower**, plusieurs RAT custom.
- **Ciblage géographique** : Corée du Sud massivement, US (think tanks et universités travaillant sur la DPRK), Europe (centres de recherche sur la non-prolifération), Japon.

**Activité continue** : Kimsuky est l’un des groupes les plus actifs en volume dans l’écosystème DPRK. Volumes élevés de phishing, campagnes quasi permanentes. Sophistication modérée mais efficacité par persistance.

### 11.6 APT43 / Velvet Chollima / Kimsuky-adjacent

**Distinction avec Kimsuky** : les profils se recoupent et certains analystes les considèrent comme très proches ou partiellement fusionnés. Mandiant promeut APT43 comme cluster distinct depuis 2023.

**Spécialisation** : ciblage **académique, think tanks, médias, ONG** travaillant sur la DPRK. Collecte de renseignement sur les positions externes et les narratifs médiatiques.

**TTP signature** : similaire à Kimsuky (spear-phishing, credential harvesting, RAT légers). APT43 est également documenté pour utiliser des **crypto-vols ponctuels** comme source de financement opérationnel — ce qui en fait un croisement entre les missions d’espionnage (Kimsuky) et financières (APT38).

### 11.7 Andariel / Onyx Sleet

**Spécialisation** : mix ransomware / cyber-espionnage. Moins connu que Lazarus ou APT38, mais significatif.

**Particularité** : Andariel a déployé des opérations de **ransomware ciblé** dans le passé (notamment contre des institutions de santé américaines), en plus de ses missions d’espionnage. Cette mixité rend son classement difficile.

**Cibles** : secteur de la santé (ciblage ransomware Maui), défense sud-coréenne, ATM et banques (braquages divers).

### 11.8 Les opérateurs IT DPRK : phénomène unique

Un phénomène entièrement distinct des APT traditionnelles mérite une section dédiée : les **opérateurs IT DPRK**.

**Modus operandi** : des **milliers de ressortissants nord-coréens**, envoyés à l’étranger par le régime, travaillent sous **de fausses identités** comme développeurs freelance ou salariés à distance dans des entreprises occidentales. Ils génèrent un revenu en dollars qui est en grande partie reversé au régime.

**Revenu estimé** : le gouvernement américain estime à **300 millions de dollars par an et plus** les revenus générés par ce programme. L’ordre de grandeur, tout comme les vols crypto, est macroéconomique pour la DPRK.

**Techniques d’infiltration** :

- **Fausses identités** : achat de documents d’identité volés (américains, sud-coréens, autres), construction de profils LinkedIn complets avec CV, recommandations, photos (parfois générées par IA ou volées).
- **VPN et proxies** : connexions via IP occidentales (US, Europe) pour masquer l’origine coréenne.
- **Intermédiaires (facilitators)** : complices locaux qui prêtent leur identité, leur adresse, leurs comptes bancaires. Plusieurs facilitators ont été arrêtés aux US (notamment « l’opération laptop farm » — l’affaire Christina Chapman en 2024 qui hébergeait 90 ordinateurs connectés via VPN pour permettre à des travailleurs DPRK d’apparaître comme basés aux US).
- **Entretiens via vidéoconférence** : les opérateurs DPRK passent les entretiens en se faisant passer pour des asiatiques basés aux US, parfois avec modifications vidéo ou voice transformation.

**Détection** : indices comportementaux (réticence à allumer la caméra, horaires décalés, anomalies linguistiques, accès depuis IP incompatibles avec la localisation déclarée), vérification approfondie d’identité, background checks renforcés. Le FBI a émis des advisories détaillés en 2023-2024 pour aider les employeurs à détecter ces infiltrations.

**Risques au-delà du financement** : une fois à l’intérieur d’une entreprise, un opérateur IT DPRK peut potentiellement introduire du code malveillant, exfiltrer de la propriété intellectuelle, ou préparer des accès pour d’autres opérations APT nord-coréennes. Plusieurs cas documentés de tentatives d’exfiltration.

### 11.9 Formation, stationnement à l’étranger, OPSEC

La formation des opérateurs cyber DPRK combine formation militaire (discipline, hiérarchie, sécurité opérationnelle) et formation technique (informatique, langues étrangères, compréhension des plateformes occidentales). Les opérateurs les plus doués sont identifiés très tôt et formés dans des programmes d’élite.

**Stationnement à l’étranger** : comme mentionné (11.2), une grande partie des opérations cyber DPRK est conduite depuis l’étranger — Chine principalement, mais aussi Russie, Asie du Sud-Est. Les opérateurs vivent dans des communautés fermées sous surveillance, avec des contrôles stricts (familles restées en DPRK comme « assurance » contre la défection, rotation régulière des postes).

**OPSEC** : globalement moyenne. Les opérateurs DPRK sont formés à l’OPSEC mais l’ampleur du volume d’opérations et les pressions de résultats (le régime attend des revenus) produisent des erreurs régulières qui ont facilité plusieurs attributions. Parmi les artefacts récurrents : réutilisation d’infrastructure, overlaps de TTP entre opérations différentes, quelques cas d’opérateurs identifiés nominativement par les indictments DOJ.

-----

## Chapitre 12 — DPRK : campagnes de référence et financement du régime

Ce chapitre documente les campagnes nord-coréennes les plus emblématiques, en progressant chronologiquement et thématiquement. Le cas complet Lazarus/crypto est traité au Ch.30.

### 12.1 Sony Pictures (2014) — cyber-intimidation

**Acteur** : Lazarus. **Paradigme** : cyber-intimidation politique via vol + publication + destruction.

**Contexte** : Sony Pictures produisait *The Interview*, une comédie satirique représentant un complot fictif pour assassiner Kim Jong-un. La DPRK a publiquement protesté contre le film.

**Attaque** : en novembre 2014, Lazarus compromet Sony Pictures, exfiltre des téraoctets de données (emails internes, scénarios, données personnelles de 47 000 employés, films non sortis), puis déploie un wiper (destruction massive de données). Les données exfiltrées sont progressivement publiées en ligne, créant un scandale pour Sony (emails embarrassants, données de célébrités).

**Message politique** : la diffusion de *The Interview* est annulée dans plusieurs cinémas sous la pression des menaces. Sony envisage initialement d’annuler la sortie complète avant de revenir en arrière.

**Attribution** : FBI, NSA, DHS attribuent publiquement à la DPRK en décembre 2014. Un des premiers cas d’attribution publique rapide d’une cyberattaque étatique.

**Leçons** : la DPRK est prête à conduire des opérations cyber coûteuses pour des motifs politiques/de réputation, pas seulement financiers. Le cyber comme arme de dissuasion culturelle est une spécificité.

### 12.2 Bangladesh Bank (février 2016) — premier braquage SWIFT étatique

**Acteur** : APT38/BlueNoroff. **Paradigme** : cyber-braquage bancaire à grande échelle via le système interbancaire.

**Attaque** : APT38 compromet les systèmes de la banque centrale du Bangladesh et accède au terminal SWIFT. Le 4 février 2016, 35 ordres de virement frauduleux sont émis via SWIFT, totalisant **951 millions de dollars** destinés à des comptes aux Philippines et au Sri Lanka.

**Ce qui a été volé** : 81 millions de dollars ont transité vers les Philippines et y ont été blanchis (casinos).

**Ce qui a été bloqué** : les 870 millions restants ont été arrêtés. L’élément déclencheur de la détection : une **faute de frappe** dans l’un des ordres de virement (« Jupiter Street » écrit « Jupiter Steet », puis « fandation » au lieu de « foundation »). La banque Deutsche Bank, qui traitait les virements comme banque correspondante, a examiné manuellement l’ordre et détecté l’anomalie. Les autres ordres ont ensuite été annulés.

**Impact** : premier braquage bancaire majeur par un acteur étatique via le cyber. A mis en évidence les vulnérabilités des systèmes SWIFT et a déclenché un durcissement des contrôles SWIFT (SWIFT Customer Security Programme).

**Leçons** : les systèmes financiers interbancaires sont des cibles APT majeures. La détection peut dépendre de signaux humains (lecture manuelle) en plus des contrôles automatiques. Une seule faute de frappe a sauvé 870 millions de dollars.

### 12.3 WannaCry (mai 2017)

**Acteur** : Lazarus. **Paradigme** : ransomware worm avec propagation mondiale.

**Mécanisme** : WannaCry combinait un ransomware et l’exploit **EternalBlue** (vulnérabilité SMB de la NSA leakée par Shadow Brokers en avril 2017). L’exploit permettait la propagation vermineuse de machine à machine sur les réseaux, infectant toutes les machines Windows non patchées.

**Impact mondial** (mai 2017) :

- **200 000+ systèmes infectés dans 150 pays** en 24-48 heures.
- **NHS britannique** partiellement paralysé, avec des hôpitaux qui ont dû reporter des opérations non urgentes et rediriger des patients.
- **Telefónica** (Espagne), **Renault-Nissan**, **FedEx**, **Deutsche Bahn** (panneaux d’affichage) sévèrement touchés.
- Dommages mondiaux estimés en milliards de dollars (sur des périmètres variables d’estimation).

**Particularité** : un chercheur britannique (**Marcus Hutchins**, pseudonyme MalwareTech) a découvert un **kill switch** dans le code — une requête vers un domaine spécifique non enregistré. En enregistrant le domaine, Hutchins a activé le kill switch, arrêtant la propagation pour la première vague. Les variants ultérieurs sans kill switch ont causé des dommages supplémentaires mais à moindre échelle.

**Paradoxe** : WannaCry a généré peu de revenus directs (~140 000 dollars en Bitcoin avant saisie). Le mécanisme de paiement/déchiffrement était mal conçu — les victimes qui payaient ne recevaient souvent pas la clé. Soit c’était une opération de test qui a échappé au contrôle, soit un wiper déguisé. L’interprétation privilégiée : opération Lazarus qui s’est partiellement mal déroulée mais a révélé la capacité à causer des dommages mondiaux massifs.

**Attribution** : décembre 2017 — attribution publique par les US, UK, Australie, Canada, Nouvelle-Zélande, Japon à la DPRK/Lazarus.

**Leçons** : la DPRK assume des dommages collatéraux mondiaux massifs. Les vulnérabilités leakées par les services d’État (EternalBlue) produisent des effets de second ordre catastrophiques une fois dans les mains d’acteurs prêts à les utiliser sans discrimination.

### 12.4 Opération Dream Job — social engineering LinkedIn continu

**Acteur** : Lazarus. **Paradigme** : social engineering extrêmement ciblé via faux recruteurs.

**Modus operandi** : Lazarus opère en continu depuis au moins 2019 une opération de social engineering sur LinkedIn. Des faux profils de recruteurs (parfois usurpant des recruteurs réels d’entreprises légitimes) approchent des employés de cibles stratégiques — développeurs dans des entreprises tech, ingénieurs dans l’aérospatial et la défense, employés d’exchanges crypto — avec des propositions d’emploi attractives.

**Chaîne de compromission typique** :

1. Approche initiale sur LinkedIn avec une offre attractive.
1. Transition vers un canal de communication privé (WhatsApp, Telegram, Skype).
1. Envoi d’un « test technique » sous forme de projet à exécuter.
1. Le projet contient du malware qui s’exécute lors de la compilation ou de l’ouverture.
1. Foothold établi sur la machine professionnelle du développeur (souvent avec accès à des réseaux internes et des secrets développement de son employeur).

**Campagnes documentées** : opérations contre des employés d’aerospatial (dont une qui a touché plusieurs entreprises européennes documentées par ESET en 2023), contre des développeurs crypto (ciblage qui a permis plusieurs des grands vols crypto), contre des chercheurs en sécurité.

**Pourquoi ça marche** : l’approche est personnalisée, l’offre est attractive, le « test technique » est contextuel au rôle prétendu. Les développeurs, habitués à exécuter du code inconnu dans le cadre de leur travail, baissent leur garde.

**Défense** : sensibilisation, séparation stricte entre machine professionnelle et exécution de code non vérifié (sandboxes, machines dédiées), vérification par canaux alternatifs de l’identité des recruteurs.

### 12.5 3CX supply chain (mars 2023)

**Acteur** : Lazarus (sous-groupe Labyrinth Chollima, chevauchement avec APT41 noté par certains analystes dans une phase intermédiaire). **Paradigme** : supply chain imbriquée — la compromission initiale de 3CX passait par une autre supply chain compromise.

**Synthèse** : **3CX** est un logiciel de communication VoIP utilisé par plus de 600 000 organisations dans le monde. En mars 2023, il est découvert que l’application desktop 3CX distribuée via les canaux officiels a été **trojanisée** — les binaires signés contiennent une backdoor.

**Mécanisme de la compromission initiale** : l’enquête post-incident a révélé que 3CX lui-même a été compromis via **X_Trader**, un logiciel de trading financier de Trading Technologies, lui-même compromis précédemment par Lazarus. Un employé de 3CX avait installé X_Trader sur sa machine professionnelle ; l’infection de cette machine a donné à Lazarus un accès au réseau 3CX, puis au pipeline de build de leur produit desktop.

**Cascade** : X_Trader compromis → employé 3CX infecté → environnement build 3CX compromis → logiciel 3CX trojanisé → clients 3CX compromis (600 000+ potentiels, avec ciblage sélectif en phase 2). **Le supply chain d’un supply chain** — un niveau d’imbrication nouveau dans les opérations supply chain documentées.

**Impact** : ciblage en phase 2 de clients 3CX spécifiques (entreprises crypto, organisations d’intérêt). Les victimes confirmées publiquement ont été limitées par rapport au pool de 600 000 clients potentiels, confirmant un ciblage sélectif.

**Leçons** : les supply chains peuvent être compromises en cascade — le vecteur peut être éloigné de plusieurs « couches » de la cible finale. La confiance dans un logiciel signé par un éditeur ne suffit plus ; le monitoring comportemental des processus, même légitimes, devient essentiel.

### 12.6 JumpCloud breach (juin 2023) — ciblage crypto via MSP

**Acteur** : Lazarus/Labyrinth Chollima. **Paradigme** : compromission d’un fournisseur de gestion d’identité pour atteindre ses clients crypto.

**Synthèse** : **JumpCloud** est un fournisseur de gestion d’identité SaaS (directory service, SSO, MDM). Lazarus compromet JumpCloud en juin 2023 et abuse des accès pour cibler spécifiquement des **clients JumpCloud dans l’écosystème crypto** — exchanges et sociétés de services crypto. Environ 5 clients de JumpCloud (sur des milliers) ont été touchés — ciblage extrêmement sélectif.

**Significance** : illustration des pivots supply chain ciblés dans l’écosystème crypto. Lazarus a identifié que JumpCloud servait des clients crypto intéressants, et a exploité cette position.

### 12.7 Vols crypto massifs — chronologie

La liste des grands vols crypto attribués à Lazarus/BlueNoroff constitue une chronologie à elle seule. Ordre chronologique, non exhaustif.

- **DragonEx** (mars 2019) : ~7 M$.
- **Upbit** (novembre 2019) : 342 000 ETH (~49 M$ à l’époque, ~1 Mrd$ aujourd’hui).
- **KuCoin** (septembre 2020) : 281 M$.
- **Cream Finance** (septembre 2021) : 29 M$.
- **Badger DAO** (décembre 2021) : 120 M$.
- **Axie Infinity Ronin Network** (mars 2022) : **624 M$** — pivot : phishing LinkedIn contre un employé de Sky Mavis (studio derrière Axie). L’un des plus grands vols crypto à date.
- **Harmony Bridge** (juin 2022) : 100 M$.
- **DeBridge Finance** (août 2022) : tentative échouée.
- **Atomic Wallet** (juin 2023) : 100 M$ (certains contestent l’attribution).
- **Alphapo** (juillet 2023) : 60 M$.
- **CoinsPaid** (juillet 2023) : 37 M$.
- **Stake.com** (septembre 2023) : 41 M$.
- **CoinEx** (septembre 2023) : 54 M$.
- **HTX/Heco Bridge** (novembre 2023) : ~100 M$.
- **DMM Bitcoin** (mai 2024) : 305 M$.
- **WazirX** (juillet 2024) : 235 M$.
- **Radiant Capital** (octobre 2024) : 50 M$.
- **Bybit** (février 2025) : **~1,5 milliard de dollars** — **le plus gros vol crypto de l’histoire** à date de publication. Attribution FBI à Lazarus confirmée dans les semaines suivantes. Le cas Bybit est traité en détail au Ch.30.

**Cumul** : entre 3 et 6 milliards de dollars sur la période 2017-2025, avec une accélération nette post-2022.

### 12.8 Le pipeline de blanchiment

Une fois les crypto-actifs volés, la DPRK doit les **convertir en devises utilisables** — un processus complexe qui est devenu un sujet d’investigation à part entière.

**Étape 1 — Obfuscation on-chain** :

- **Mixers / tumblers** : **Tornado Cash** (Ethereum, sanctionné par l’OFAC en août 2022 — première sanction d’un smart contract dans l’histoire), **Wasabi Wallet** (Bitcoin), **Samourai Wallet** (Bitcoin, fermé par les autorités en avril 2024).
- **Bridges cross-chain** : transfert entre blockchains (Ethereum → BNB Chain → TRON) pour complexifier le suivi.
- **Privacy coins** : conversion vers Monero (très difficile à tracer).
- **DeFi non-KYC** : swaps via des protocoles décentralisés qui n’exigent pas d’identification.

**Étape 2 — Conversion en stablecoins** : conversion en **USDT** (Tether), principalement sur la blockchain **TRON** (frais faibles, confirmations rapides, volume élevé qui facilite le camouflage). L’USDT sur TRON est devenu le canal dominant pour les flux illicites crypto en général.

**Étape 3 — Cashout** : conversion finale en devises fiat (dollars, euros, yuan). Plusieurs canaux :

- **Exchanges à KYC faible** : certains petits exchanges en Asie, en Russie, dans le Golfe ont historiquement eu des pratiques KYC laxistes. Ces exchanges subissent une pression réglementaire croissante mais certains restent utilisés.
- **OTC desks** (Over-the-Counter) : desks de trading hors-marché, souvent en Chine ou en Russie, qui convertissent les crypto en fiat pour des commissions élevées en échange d’un KYC minimal.
- **Mules** : réseaux de particuliers recrutés (souvent sans connaissance complète de la source des fonds) pour recevoir et transférer les fonds.

**Étape 4 — Rapatriement vers la DPRK** : une fois en fiat, les fonds transitent par des circuits opaques (sociétés écrans chinoises, banques complaisantes) vers le régime. Les mécanismes exacts restent largement classifiés, mais plusieurs investigations ont documenté des réseaux de facilitators dans plusieurs pays.

**Contre-mesures** :

- **Sanctions OFAC ciblées** : sanction de Tornado Cash (2022), sanction d’adresses crypto spécifiques, sanction d’OTC desks impliqués, sanction de ressortissants (incluant des facilitators chinois et russes).
- **Coopération exchanges** : les exchanges majeurs (Binance, Coinbase, Kraken) ont renforcé leur KYC, gelent les fonds sur signalement, collaborent avec le FBI. Binance a gelé plus de 4 milliards de dollars liés à des activités illicites entre 2022 et 2024.
- **Intelligence blockchain** : Chainalysis, TRM Labs, Elliptic fournissent aux autorités des capacités de suivi on-chain. Les attaquants DPRK adaptent leurs techniques en continu.

La **guerre du blanchiment** est un jeu du chat et de la souris permanent. La DPRK est devenue très sophistiquée, les défenseurs aussi — mais l’asymétrie (les attaquants n’ont qu’à trouver une route de blanchiment qui fonctionne, les défenseurs doivent fermer toutes les routes) joue contre les défenseurs.

### 12.9 Impact géopolitique : cyber comme arme de prolifération nucléaire

La conséquence la plus grave des cyberopérations DPRK est leur **financement direct du programme nucléaire et balistique nord-coréen**. Les estimations ONU et US convergent : une part significative du financement du programme d’armement depuis 2016-2017 vient du cybervol.

**Implication stratégique** : les cyberopérations nord-coréennes ne sont pas un « problème cyber » — elles sont un **problème de sécurité internationale** lié directement à la non-prolifération nucléaire. Chaque dollar volé par Lazarus contribue potentiellement au développement d’armes nucléaires et de vecteurs balistiques.

**Conséquence pour la réponse internationale** : le cadre de sanctions et de contre-mesures s’est durci significativement depuis 2022. Les indictments DOJ contre des opérateurs DPRK et des facilitators, les sanctions OFAC sur des adresses et des entités, les opérations de saisies d’actifs (le DOJ a saisi pour plusieurs centaines de millions de dollars de crypto liés à des vols Lazarus entre 2022 et 2025) construisent une pression croissante.

**Leçon analytique** : quand on regarde une opération DPRK, on regarde un maillon dans une chaîne de financement d’armes nucléaires. Cette perspective change la nature de la menace et la proportionnalité des réponses.

-----

## Chapitre 13 — Iran : contexte, doctrine et groupes APT

### 13.1 Priorités iraniennes et doctrine cyber

Les cyberopérations iraniennes s’inscrivent dans une configuration stratégique définie par plusieurs axes.

**Rivalité régionale** : tensions permanentes avec Israël (rivalité existentielle), Arabie saoudite et monarchies du Golfe (rivalité sunnite/chiite + géopolitique). Le cyber est un levier asymétrique pour un pays qui n’égale pas les capacités militaires de ses rivaux.

**Surveillance interne et diaspora** : répression politique contre la dissidence interne et surveillance des opposants à l’étranger (notamment post-Mahsa Amini 2022 et la vague de protestations « Femme Vie Liberté »).

**Sabotage ponctuel** : l’Iran est l’un des rares États à utiliser occasionnellement le **cyber destructif ouvert** (wipers), en réponse à des événements perçus comme des agressions (Stuxnet 2010 a catalysé cette trajectoire).

**Opérations d’influence** : promotion du récit iranien dans les conflits régionaux (Yémen, Liban, Syrie, Irak), influence sur les communautés chiites internationales.

**Contournement de sanctions** : l’Iran subit des sanctions sévères depuis 1979 (renforcées à plusieurs reprises). Le cyber peut servir à contourner certaines sanctions (vol financier, exfiltration de technologies).

**Doctrine** : le cyber iranien est un **levier asymétrique**. Moins sophistiqué que les acteurs de pointe (US, Israël, Russie, Chine), il compense par une grande activité, une acceptation du destructif, et une capacité à causer des dommages à des cibles plus puissantes.

### 13.2 Structure : MOIS vs IRGC

L’appareil cyber iranien est structuré autour de deux pôles institutionnels distincts qui ont des cultures et des missions différentes.

**MOIS / VAJA** (Ministry of Intelligence and Security — وزارت اطلاعات) est le renseignement civil. Institution relativement classique (comparable à un ministère de l’intérieur étendu), conduit l’espionnage extérieur et le contre-espionnage intérieur. Les groupes APT associés au MOIS tendent à être plus orientés **espionnage classique** (collecte de renseignement, ciblage diplomatique).

**IRGC / Sepah** (Islamic Revolutionary Guard Corps — سپاه پاسداران انقلاب اسلامی) est le corps des Gardiens de la Révolution. Force militaire parallèle à l’armée régulière, avec des missions idéologiques et révolutionnaires. Conduit les opérations à l’étranger (Quds Force), gère une partie de l’économie iranienne, et a des branches cyber importantes. Les groupes APT associés à l’IRGC tendent à être plus **agressifs**, **idéologiques**, avec une forte composante de surveillance des opposants et des personnalités cibles.

La distinction MOIS/IRGC est importante pour l’analyse : une opération IRGC peut refléter une initiative révolutionnaire/militaire (ciblage d’un dissident, représailles), une opération MOIS reflète plus probablement un besoin de renseignement classique.

**L’IRGC a une branche cyber structurée** : IRGC Intelligence Organization (IRGC-IO), qui supervise APT42 notamment. L’IRGC a également des capacités cyber dans d’autres structures (IRGC Electronic Warfare and Cyber Defense Command).

### 13.3 APT33 / Peach Sandstorm (IRGC)

**Mission** : espionnage industriel sur l’énergie, l’aérospatial, la pétrochimie. Cibles privilégiées : entreprises énergétiques du Golfe, sous-traitants aérospatiaux américains et européens, industries pétrochimiques saoudiennes (en cohérence avec la rivalité régionale).

**TTP signature** :

- **Password spraying massif** : APT33 est l’un des acteurs les plus connus pour le password spraying à grande échelle sur Azure AD/M365. Volumes gigantesques, faible taux de succès par tentative mais volume global efficace.
- **Malware custom** : backdoors comme **DropShot** (dropper), **StoneDrill** (wiper apparenté à Shamoon), **TurnedUp** (backdoor).
- **Spear-phishing** sur employés cibles.

**Campagnes** :

- Ciblage de l’industrie aérospatiale US (Boeing, sous-traitants) — documenté par FireEye en 2017.
- Ciblage énergie Golfe (Saudi Aramco, autres) — continu.
- Campagnes 2023-2024 documentées par Microsoft (Peach Sandstorm).

**Lien suspecté avec Shamoon** (Ch.14) : certains analystes ont établi des liens entre APT33 et les opérations Shamoon — ce qui placerait APT33 au croisement de l’espionnage et du destructif. Attribution pas pleinement consolidée.

### 13.4 APT34 / OilRig / Hazel Sandstorm (MOIS)

**Mission** : espionnage régional au service du MOIS. Cibles : gouvernements du Moyen-Orient (Golfe, Liban, Israël), finance régionale, énergie, télécommunications.

**TTP signature** :

- **DNS tunneling** : APT34 a historiquement été l’un des groupes qui ont le plus massivement utilisé le DNS tunneling comme canal C2.
- **Webshells** : déploiement massif sur serveurs web compromis.
- **Credential harvesting** : fausses pages de login, spearphishing avec emails contextualisés.
- **Malware** : **QUADAGENT**, **OopsIE**, **Helminth**, **ISMAgent**.

**Leak 2019** : en mars-avril 2019, un leak anonyme sur Telegram (canal « Lab Dookhtegan » — « labo cousu ») a publié des **outils APT34, des données de victimes, et des noms d’opérateurs**. Le leak a exposé l’infrastructure du groupe et plusieurs de ses techniques. L’origine du leak reste débattue (dissident interne, opération Mossad, opération de services tiers).

**Détournement par Turla** : comme mentionné au Ch.6, Turla a été documenté pour avoir utilisé l’infrastructure APT34 pour ses propres opérations — démonstration de l’instabilité relative de l’OPSEC APT34.

### 13.5 APT35 / Charming Kitten / Mint Sandstorm (IRGC)

**Mission** : **social engineering ultra-ciblé**. Cibles : chercheurs spécialisés sur l’Iran et le Moyen-Orient, dissidents politiques iraniens à l’étranger, journalistes, universitaires, cadres d’ONG, parfois femmes politiques (ciblages personnels de campagnes présidentielles US documentés).

**TTP signature — le social engineering d’APT35 est considéré comme le plus sophistiqué au monde dans sa catégorie** :

- **Faux profils LinkedIn** complets de « collègues » ou « recruteurs » avec des mois d’activité pour construire la crédibilité.
- **Impersonation de journalistes** : création de faux profils imitant des journalistes réels de médias respectés, pour approcher des cibles (« je voudrais vous interviewer pour mon article »).
- **Impersonation d’universitaires** : faux chercheurs invitant la cible à une conférence, un panel, ou une publication.
- **Malware léger** : backdoors minimales, souvent déployés via documents Office après établissement de confiance.
- **Phishing OAuth** : fausses applications OAuth imitant Google, Microsoft pour obtenir des accès persistants.

**Particularité** : APT35 investit massivement dans la **construction relationnelle** avant l’attaque. Certaines campagnes impliquent des **mois de conversation légitime** avec la cible avant le moindre élément malveillant. Cette patience et cette sophistication psychologique distinguent APT35.

**Campagnes documentées** :

- **Ciblage de journalistes et universitaires spécialisés sur l’Iran** : continu depuis 2015+.
- **Ciblage de campagnes présidentielles US 2020** : tentatives documentées de ciblage de la campagne Trump.
- **Opérations post-Mahsa Amini (2022-2023)** : ciblage intensif de dissidents à l’étranger, de journalistes couvrant les protestations.

### 13.6 APT42 / Calanque (IRGC-IO)

**Mission** : surveillance ciblée au service de l’IRGC Intelligence Organization. Cibles : opposants politiques iraniens, membres de la diaspora iranienne, personnalités considérées comme menaces par l’IRGC.

**TTP signature** : similaire à APT35 (social engineering, credential harvesting) avec une orientation plus spécifiquement sécuritaire. Surveillance mobile (Android), capture de communications.

**Distinction avec APT35** : les frontières sont parfois floues. Certains analystes considèrent APT42 comme un sous-groupe d’APT35. Microsoft les distingue comme Calanque (APT42) vs Mint Sandstorm (APT35).

### 13.7 MuddyWater / Mango Sandstorm (MOIS)

**Mission** : ciblage régional et international — gouvernements, télécoms, énergie. MuddyWater est l’un des groupes iraniens les plus actifs en volume.

**TTP signature** :

- **PowerShell obfusqué massivement** : MuddyWater a fait du PowerShell obfusqué sa marque de fabrique — scripts lourdement encodés, plusieurs couches d’évasion.
- **Outils open source** : utilisation massive d’outils accessibles publiquement (Koadic, Metasploit, PSEmpire) — moins de malware custom que d’autres groupes, plus d’adaptation d’outils existants.
- **Spear-phishing** avec documents Office contenant des macros.

**Cibles** : Moyen-Orient, Asie centrale, Asie du Sud, Europe dans une moindre mesure.

### 13.8 Scarred Manticore (MOIS, Check Point 2023)

**Attribution** : MOIS, identifié publiquement par Check Point en 2023.

**Mission** : espionnage gouvernemental de haut niveau au Moyen-Orient.

**TTP signature** : outillage **plus sophistiqué** que MuddyWater ou OilRig — rootkits custom, persistence avancée, OPSEC élevée. Scarred Manticore représente potentiellement une montée en gamme du MOIS cyber.

**Campagne récente** : compromission de longue durée (18+ mois) d’organisations gouvernementales au Moyen-Orient.

### 13.9 Agrius — wipers sous fausse bannière hacktiviste

**Attribution** : acteur lié à l’Iran, probablement IRGC.

**Particularité** : Agrius déploie des **wipers** (**Apostle**, **DEADWOOD**, **Moneybird**) généralement **masqués en ransomware**. Les victimes reçoivent une demande de rançon, mais il n’y a pas de mécanisme de déchiffrement réel — c’est un destructif pur. Des **fausses bannières hacktivistes** sont souvent utilisées (« Black Shadow », « Moses Staff ») pour brouiller l’attribution publique et créer un narratif de « hacktivisme antisioniste ».

**Cibles** : Israël principalement, avec quelques extensions régionales.

**Implication** : Agrius illustre une caractéristique de l’écosystème iranien — l’acceptation des opérations destructives et l’utilisation de fausses bannières pour maintenir un déni plausible, tout en signalant aux audiences cibles (en Iran, dans l’« axe de la résistance ») la capacité de frapper.

-----

## Chapitre 14 — Iran : campagnes de référence

Ce chapitre présente les campagnes iraniennes emblématiques, organisées chronologiquement et thématiquement.

### 14.1 Stuxnet (2010) — le catalyseur

**Acteurs** : co-attribution **États-Unis et Israël** (publiquement documentée par plusieurs sources journalistiques dont le livre *Confront and Conceal* de David Sanger, 2012). **Paradigme** : première arme cyber OT, catalyseur des capacités cyber iraniennes.

**Cible** : le **programme d’enrichissement d’uranium iranien**, spécifiquement les centrifugeuses IR-1 à Natanz.

**Mécanisme** : Stuxnet est un malware d’une complexité sans précédent à son époque. Il combinait :

- **Quatre vulnérabilités 0-day Windows** (usage exceptionnel — un seul 0-day suffit généralement à compromettre une cible).
- **Ciblage extrêmement précis** : Stuxnet ne s’activait que sur des systèmes très spécifiques — machines Windows configurées avec WinCC/STEP7 de Siemens, contrôlant des automates S7-315 spécifiques, eux-mêmes contrôlant des centrifugeuses tournant à certaines vitesses.
- **Manipulation physique** : une fois sur le système de contrôle, Stuxnet modifiait les commandes envoyées aux centrifugeuses pour provoquer leur destruction (variations de vitesse anormales causant des contraintes mécaniques), **tout en affichant des valeurs normales aux opérateurs**. Cette double manipulation (destruction réelle + masquage) est la signature du malware.

**Impact** : environ **1 000 centrifugeuses détruites**, programme iranien retardé de 2-3 ans selon les estimations. Stuxnet a démontré que le cyber pouvait causer des dommages physiques significatifs à un programme militaro-industriel majeur.

**Propagation non intentionnelle** : Stuxnet s’est propagé au-delà des systèmes ciblés (machines Windows génériques, réseaux industriels non ciblés) via USB, ce qui a conduit à sa découverte en 2010 par des chercheurs en sécurité biélorusses puis internationaux.

**Catalyseur iranien** : Stuxnet a eu un **effet boomerang** majeur. L’Iran, conscient de la capacité cyber offensive déployée contre lui, a investi massivement dans son propre programme cyber offensif. Shamoon, développé environ 2 ans après Stuxnet, est la réponse iranienne — un wiper déployé contre Saudi Aramco (allié américain régional) en 2012. L’Iran est depuis devenu un acteur cyber significatif, étape structurée par Stuxnet.

**Autres traitements** : Stuxnet est abordé au Ch.18 (Israël), au Ch.21 (OT/ICS), et au Ch.25 (prolifération cyber — le code Stuxnet a fuité et a été étudié par tous les acteurs étatiques).

### 14.2 Shamoon v1/v2/v3 (2012-2018)

**Acteur** : attribué à l’Iran, avec liens APT33 pour certaines itérations. **Paradigme** : wiper destructif à grande échelle comme représailles stratégiques.

**Shamoon v1 (août 2012)** : déployé contre **Saudi Aramco**, compagnie pétrolière nationale saoudienne. Le wiper a effacé les disques durs de **30 000 postes de travail** (soit environ 75% du parc de la compagnie). Les systèmes de production pétrolière n’ont pas été touchés, mais les opérations administratives ont été paralysées pendant des semaines. Parallèlement, un wiper similaire a frappé RasGas (Qatar) avec un impact plus limité.

**Message politique** : Shamoon v1 a été interprété comme une **représailles iranienne** pour Stuxnet, dirigée contre un allié majeur des États-Unis dans la région. Le message : « si vous nous attaquez, nous pouvons frapper votre industrie pétrolière ».

**Shamoon v2 (novembre 2016 - janvier 2017)** : réapparition du wiper contre des cibles saoudiennes, dans un contexte de tensions régionales renouvelées.

**Shamoon v3 (décembre 2018)** : nouvelle version, ciblage Saipem (entreprise pétrolière italienne) et autres.

**Analyse** : Shamoon est devenu un outil récurrent iranien signalant les moments de tensions régionales. Son déploiement est souvent associé à des événements politiques (sommet de l’OPEP, sanctions, incidents régionaux).

### 14.3 Campagne contre l’Albanie (juillet 2022)

**Acteur** : Iran (MOIS, attribution publique par les États-Unis en septembre 2022 via sanctions OFAC et par l’Albanie). **Paradigme** : wiper + ransomware déployés pour représailles politiques.

**Contexte** : l’Albanie hébergeait un important camp de l’organisation d’opposition iranienne **MEK** (Mujahideen-e-Khalq — Organisation des Moudjahidin du peuple), à la suite d’un accord avec les États-Unis dans les années 2010 pour leur accueil depuis l’Irak. L’Iran considère le MEK comme un groupe terroriste et a exigé son expulsion.

**Attaque (juillet 2022)** : wipers et ransomware déployés contre les **systèmes gouvernementaux albanais** — services de police, administration, parlement. Disruption significative des services publics. L’attaque a coïncidé avec un congrès prévu du MEK.

**Réponse albanaise (septembre 2022)** : l’Albanie a **rompu les relations diplomatiques** avec l’Iran et expulsé le personnel diplomatique iranien. **Premier cas d’une rupture diplomatique pour cause de cyberattaque** dans l’histoire.

**Attribution et sanctions** : les États-Unis ont attribué publiquement à l’Iran, imposé des sanctions OFAC contre le MOIS et des opérateurs, et soutenu l’Albanie techniquement (FBI a envoyé des équipes).

**Signification** : l’attaque albanaise illustre la volonté iranienne de conduire des opérations destructives à l’étranger pour des motifs politiques, et la capacité occidentale à y répondre par l’attribution et le soutien diplomatique. C’est aussi un précédent juridique intéressant (rupture diplomatique = signal que le cyber peut déclencher des réponses diplomatiques majeures).

### 14.4 Cyberattaques contre Israël 2023-2025

Le conflit Israël-Hamas déclenché en octobre 2023 a amplifié les cyberopérations iraniennes contre Israël et ses intérêts.

**Campagnes documentées** :

- **Opérations Agrius** : wipers continus contre cibles israéliennes, sous fausses bannières hacktivistes (« Cyber Av3ngers » notamment).
- **Ciblage d’infrastructures civiles** : systèmes de santé israéliens, systèmes municipaux, parfois systèmes d’alerte publique.
- **Opérations contre les sous-traitants de défense israéliens et américains** : espionnage classique.
- **Opérations d’influence** : amplification de narratifs pro-palestiniens sur les réseaux sociaux, deepfakes ponctuels, manipulation de contenus.

**Ciblage US post-octobre 2023** : les opérations iraniennes contre des cibles américaines ont également augmenté, notamment contre des infrastructures eau (« Cyber Av3ngers » a revendiqué plusieurs attaques contre des systèmes d’eau municipaux US via exploitation de PLC Unitronics exposés — démonstration plus symbolique qu’impactante mais message clair).

### 14.5 Surveillance des dissidents et diaspora

Les cyberopérations iraniennes contre les dissidents et la diaspora sont un volet continu et sous-documenté publiquement. Quelques éléments publics :

- **Campagnes APT35/APT42** continues contre les dissidents iraniens à l’étranger.
- Post-Mahsa Amini (septembre 2022, mort en détention de la « police des mœurs » iranienne, déclenchement des protestations « Femme Vie Liberté ») : intensification massive du ciblage des militants féministes iraniens à l’étranger, des journalistes couvrant les protestations, des relais de la diaspora.
- **Harcèlement** : au-delà de la surveillance, certaines cibles reçoivent des harcèlements directs (deepfakes humiliants, campagnes de dénigrement, pressions via les familles en Iran).
- **Opérations physiques** : le cyber est parfois coordonné avec des tentatives d’enlèvement ou d’intimidation physique (plusieurs cas documentés aux US et en Europe).

### 14.6 Analyse : la spécificité iranienne

La synthèse des campagnes iraniennes révèle un profil distinct dans l’écosystème APT.

**Le destructif ponctuel comme substitut/complément conventionnel** : l’Iran est l’un des rares États à utiliser régulièrement le cyber destructif ouvertement. Shamoon et Agrius sont des wipers déployés à des moments de tensions régionales — le cyber remplit un rôle que l’action conventionnelle (frappes militaires) remplirait dans d’autres configurations. Cette caractéristique distingue l’Iran des autres acteurs (la Russie fait du destructif aussi mais majoritairement en contexte de guerre déclarée avec l’Ukraine ; la Chine presque pas ; les US/Israël très rarement et ciblé).

**Social engineering extrêmement sophistiqué** : APT35 représente probablement l’état de l’art mondial en social engineering ciblé. Cette compétence compense une sophistication technique de malware moindre que celle des APT russes ou chinoises.

**Utilisation de fausses bannières hacktivistes** : pratique récurrente (Cyber Av3ngers, Moses Staff, autres). Permet à l’Iran de signaler des capacités à son audience domestique et régionale tout en maintenant un déni plausible.

**Montée en sophistication** : Scarred Manticore (2023) suggère que le MOIS investit dans des capacités plus sophistiquées. La trajectoire est à la hausse, même si l’Iran reste un cran en-dessous des acteurs de pointe.

**Pour l’analyste** : face à une intrusion attribuée à l’Iran, les questions discriminantes sont : MOIS ou IRGC ? Opération de renseignement classique ou opération destructive/représailles ? Lien avec un événement politique/régional récent ? Utilisation d’une fausse bannière hacktiviste ?

-----

## Chapitre 15 — Autres acteurs étatiques, mercenaires cyber et zones grises

Ce chapitre couvre les acteurs étatiques non traités en Parties II-III-IV (acteurs régionaux avec capacités cyber croissantes), les mercenaires cyber commerciaux (NSO, Intellexa, Candiru), et les zones grises crime-État.

### 15.1 Acteurs régionaux documentés

**Vietnam — OceanLotus / APT32** (Cobalt Kitty, BISMUTH) : service de renseignement vietnamien (probablement Ministry of Public Security). Mission : espionnage régional (ASEAN, Chine, Cambodge), dissidents vietnamiens et opposants politiques à l’étranger, entreprises étrangères opérant au Vietnam. TTP : sophistication croissante, ciblage macOS et mobile (distinctif pour un acteur régional), malware custom (SOUNDBITE, PHOREAL). Campagnes contre BMW et Hyundai documentées (2019). Ciblage notable des journalistes vietnamiens à l’étranger.

**Pakistan — SideCopy, Transparent Tribe** : services pakistanais. Mission : ciblage quasi exclusif de l’Inde — gouvernement, défense, télécoms. TTP : malware mobile (Crimson RAT, CapraRAT pour Android, CapraSpy pour iOS), sophistication modérée. Campagne continue depuis les années 2010.

**Inde — SideWinder, Patchwork (Dropping Elephant)** : probablement services indiens. Mission : ciblage du Pakistan, de la Chine, et de l’Asie du Sud-Est dans une moindre mesure. SideWinder est particulièrement actif avec des centaines de campagnes documentées. TTP : spear-phishing, malware custom relativement simple.

**Turquie — Sea Turtle / Teal Kurma** : services turcs probablement. Mission : ciblage régional Moyen-Orient/Europe du Sud. **TTP signature : détournement DNS** — Sea Turtle a documenté une technique de compromission de **registrars DNS** pour détourner les résolutions de domaines de ses cibles (Chypre, Grèce, Kurdistan). Technique inhabituelle et sophistiquée. Ciblage des dissidents kurdes.

**Amérique latine** — **Blind Eagle / APT-C-36** : acteur latino-américain (probablement colombien selon certaines analyses). Mission : ciblage régional (Colombie, Équateur, Pérou, Venezuela). Cibles : gouvernements, finance, entreprises. Sophistication modérée.

**Corée du Sud** : services sud-coréens ont des capacités cyber importantes mais très peu documentées publiquement (l’écosystème sud-coréen publie moins sur ses propres capacités offensives). Quelques mentions de ciblage de la DPRK, en contre-intelligence.

Ces acteurs régionaux se caractérisent généralement par une sophistication modérée, un ciblage géographique concentré, et une visibilité moindre que les grandes puissances cyber. Ils sont néanmoins actifs et peuvent créer des incidents significatifs dans leurs zones d’influence.

### 15.2 Mercenaires cyber / PSO (Private Sector Offensive)

Les **PSO** (Private Sector Offensive) sont des entreprises privées qui développent et vendent des capacités cyber offensives à des États (et parfois à d’autres clients). Le marché est dominé par quelques acteurs majeurs.

**NSO Group** (Israël, fondé 2010) — **Pegasus**. Spyware mobile exploitant des **0-day iOS et Android**, permettant une compromission complète du terminal : accès aux messages (y compris messageries chiffrées type Signal et WhatsApp — lecture en post-déchiffrement sur le terminal lui-même), géolocalisation, microphone et caméra à distance, extraction de données.

NSO vend Pegasus exclusivement à des gouvernements (officiellement), avec un discours « lutte antiterroriste et criminalité grave ». La réalité documentée est beaucoup plus large : usage contre des **journalistes** (Jamal Khashoggi et ses proches avant l’assassinat, Cecilio Pineda au Mexique, des dizaines d’autres documentés par le **Pegasus Project** en 2021 — consortium de 17 médias internationaux coordonné par Forbidden Stories), **dissidents** (membres des familles de dissidents saoudiens, marocains, azerbaïdjanais), **chefs d’État et personnalités politiques** (Emmanuel Macron cité parmi les cibles potentielles, plusieurs dirigeants européens), **avocats des droits humains**, **militants**.

Implications : NSO a été ajouté à l’**Entity List** du Commerce US en novembre 2021. Apple et Meta ont porté plainte contre NSO. L’usage de Pegasus par le gouvernement polonais contre l’opposition (confirmé par Citizen Lab) a fait scandale. L’entreprise a subi des difficultés financières importantes et plusieurs changements de direction, mais reste opérationnelle.

**Intellexa** (consortium européen basé à Chypre/Grèce/Irlande/Macédoine du Nord) — **Predator**. Spyware concurrent de Pegasus, capacités similaires. Documenté par Citizen Lab comme ayant des victimes dans plusieurs pays, notamment des politiciens et journalistes (scandale retentissant en Grèce en 2022-2023, avec ciblage d’un député opposant et de journalistes — affaire **Predatorgate**). Sanctionné par les États-Unis en juillet 2023 et mars 2024.

**Candiru** (Israël, fondée 2014) — spyware ciblant les desktops (Windows principalement) via des 0-day navigateur. Documenté par Citizen Lab et Microsoft (qui a identifié la vulnérabilité CVE-2021-33771 exploitée par Candiru). Sanctionné par les États-Unis en novembre 2021 (Entity List).

**Autres acteurs** : Paragon Solutions (Israël), TrueDialog, et divers acteurs moins documentés. Le marché est en évolution — certains se professionnalisent, d’autres ferment sous la pression réglementaire.

**Pourquoi la CTI documente les mercenaires** : leurs outils apparaissent dans les campagnes d’espionnage étatique. Un analyste qui identifie un spyware Pegasus chez une victime sait que le commanditaire est probablement un **client étatique de NSO**, pas un cybercriminel autonome. La liste des clients NSO/Intellexa/Candiru est partiellement publique (via les révélations Citizen Lab, les enquêtes journalistiques, les sanctions) et inclut de nombreux régimes autoritaires ou illibéraux.

### 15.3 Régulations émergentes sur les PSO

Le marché PSO fait l’objet d’efforts réglementaires croissants.

**Pall Mall Process** : initiative conjointe franco-britannique lancée en février 2024 à Londres. Objectif : établir un cadre international pour la régulation du marché des capacités cyber commerciales. Signataires : une quarantaine d’États, entreprises, et organisations de la société civile (dont les « Big Tech » et des ONG). Le processus est itératif — les discussions se poursuivent dans plusieurs rounds.

**Restrictions d’exportation** : plusieurs pays ont durci les règles d’exportation des technologies de surveillance cyber. L’**Arrangement de Wassenaar** (export control multilatéral) inclut les « intrusion software » depuis 2013. L’UE a un règlement dual-use qui encadre les exportations. Les États-Unis utilisent l’Entity List comme levier.

**Sanctions ciblées** : les Entity List américaines, les sanctions OFAC, et les sanctions UE ont visé NSO, Intellexa, Candiru, et plusieurs individus associés. Ces sanctions ont un effet réel sur la capacité opérationnelle de ces entreprises.

**EU ban on spyware for political surveillance** : des propositions européennes visent à interdire l’usage de spywares commerciaux contre les journalistes, opposants politiques, et défenseurs des droits humains. État législatif en évolution.

**Limitations** : malgré ces efforts, le marché reste actif. De nouveaux acteurs émergent pour remplacer ceux qui sont sanctionnés. La demande étatique (États autoritaires, certaines démocraties aussi) reste forte. L’efficacité des régulations dépendra de leur universalité — les États qui refusent de coopérer peuvent continuer à s’approvisionner.

### 15.4 Zones grises crime-État

Les **zones grises crime-État** sont l’un des phénomènes les plus importants à comprendre dans le paysage cyber contemporain. Elles recouvrent plusieurs configurations.

**APT41 — la double casquette assumée** : déjà traité au Ch.9. Le cas illustre la tolérance étatique (probablement MSS) pour les activités cybercriminelles personnelles des opérateurs, tant que les priorités étatiques sont respectées.

**Ransomware russophone — la tolérance tacite** : déjà traité au Ch.5. Les groupes LockBit, Conti, BlackBasta, ALPHV, Black Suit, Play opèrent sous la tolérance tacite russe. Certains ont des liens documentés avec les services (Conti Leaks 2022 ont révélé des échanges évoquant le FSB). La frontière entre tolérance et connivence est variable selon les groupes.

**DPRK — la méthode criminelle, la finalité étatique** : déjà traité aux Ch.11-12. Lazarus vole des crypto-actifs par des méthodes cybercriminelles, mais la finalité et le commanditaire sont étatiques.

**Hacktivisme instrumentalisé** : déjà traité au Ch.5 (KillNet, NoName057(16), IT Army of Ukraine). Mouvements présentés comme indépendants mais avec un alignement opérationnel systématique sur les priorités d’un État.

**Initial Access Brokers (IAB) — la chaîne fragmentée** : les IAB sont des acteurs cybercriminels qui compromettent des organisations et **vendent l’accès** sur des forums dark web à d’autres acteurs (typiquement des opérateurs ransomware). L’écosystème IAB est massivement russophone. Un accès vendu peut être acheté par un opérateur ransomware classique (finalité criminelle) ou par un acteur étatique qui l’utilise pour un ciblage plus stratégique. La chaîne « IAB → acheteur → usage » brouille l’attribution de l’origine (la compromission initiale) par rapport à l’usage (l’action finale contre la victime).

**Implications pour l’analyse** : face à un incident :

- Ne pas assumer que l’opérateur visible (ransomware, hacktiviste) est l’acteur stratégique réel.
- Identifier si l’accès initial vient d’un IAB — ce qui ajoute une couche analytique.
- Évaluer si le ciblage est cohérent avec une motivation purement financière ou si des signaux étatiques sont présents (choix de cible stratégique, timing politique, absence de monétisation rigoureuse).
- Documenter les incertitudes — dans les zones grises, l’attribution définitive (étatique ou criminel) est souvent impossible sans accès au renseignement non-public.

Le Ch.25 approfondit l’écosystème cyber offensif mondial et ses évolutions.

-----
