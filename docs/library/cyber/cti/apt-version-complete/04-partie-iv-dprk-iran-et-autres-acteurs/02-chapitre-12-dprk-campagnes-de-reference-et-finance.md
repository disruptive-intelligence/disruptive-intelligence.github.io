---
title: 'Chapitre 12 — DPRK : campagnes de référence et financement du régime'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie IV — DPRK, iran ET autres acteurs
  - index.md
---

Ce chapitre documente les campagnes nord-coréennes les plus emblématiques, en progressant chronologiquement et thématiquement. Le cas complet Lazarus/crypto est traité au Ch.30.

## 12.1 Sony Pictures (2014) — cyber-intimidation

**Acteur** : Lazarus. **Paradigme** : cyber-intimidation politique via vol + publication + destruction.

**Contexte** : Sony Pictures produisait *The Interview*, une comédie satirique représentant un complot fictif pour assassiner Kim Jong-un. La DPRK a publiquement protesté contre le film.

**Attaque** : en novembre 2014, Lazarus compromet Sony Pictures, exfiltre des téraoctets de données (emails internes, scénarios, données personnelles de 47 000 employés, films non sortis), puis déploie un wiper (destruction massive de données). Les données exfiltrées sont progressivement publiées en ligne, créant un scandale pour Sony (emails embarrassants, données de célébrités).

**Message politique** : la diffusion de *The Interview* est annulée dans plusieurs cinémas sous la pression des menaces. Sony envisage initialement d’annuler la sortie complète avant de revenir en arrière.

**Attribution** : FBI, NSA, DHS attribuent publiquement à la DPRK en décembre 2014. Un des premiers cas d’attribution publique rapide d’une cyberattaque étatique.

**Leçons** : la DPRK est prête à conduire des opérations cyber coûteuses pour des motifs politiques/de réputation, pas seulement financiers. Le cyber comme arme de dissuasion culturelle est une spécificité.

## 12.2 Bangladesh Bank (février 2016) — premier braquage SWIFT étatique

**Acteur** : APT38/BlueNoroff. **Paradigme** : cyber-braquage bancaire à grande échelle via le système interbancaire.

**Attaque** : APT38 compromet les systèmes de la banque centrale du Bangladesh et accède au terminal SWIFT. Le 4 février 2016, 35 ordres de virement frauduleux sont émis via SWIFT, totalisant **951 millions de dollars** destinés à des comptes aux Philippines et au Sri Lanka.

**Ce qui a été volé** : 81 millions de dollars ont transité vers les Philippines et y ont été blanchis (casinos).

**Ce qui a été bloqué** : les 870 millions restants ont été arrêtés. L’élément déclencheur de la détection : une **faute de frappe** dans l’un des ordres de virement (« Jupiter Street » écrit « Jupiter Steet », puis « fandation » au lieu de « foundation »). La banque Deutsche Bank, qui traitait les virements comme banque correspondante, a examiné manuellement l’ordre et détecté l’anomalie. Les autres ordres ont ensuite été annulés.

**Impact** : premier braquage bancaire majeur par un acteur étatique via le cyber. A mis en évidence les vulnérabilités des systèmes SWIFT et a déclenché un durcissement des contrôles SWIFT (SWIFT Customer Security Programme).

**Leçons** : les systèmes financiers interbancaires sont des cibles APT majeures. La détection peut dépendre de signaux humains (lecture manuelle) en plus des contrôles automatiques. Une seule faute de frappe a sauvé 870 millions de dollars.

## 12.3 WannaCry (mai 2017)

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

## 12.4 Opération Dream Job — social engineering LinkedIn continu

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

## 12.5 3CX supply chain (mars 2023)

**Acteur** : Lazarus (sous-groupe Labyrinth Chollima, chevauchement avec APT41 noté par certains analystes dans une phase intermédiaire). **Paradigme** : supply chain imbriquée — la compromission initiale de 3CX passait par une autre supply chain compromise.

**Synthèse** : **3CX** est un logiciel de communication VoIP utilisé par plus de 600 000 organisations dans le monde. En mars 2023, il est découvert que l’application desktop 3CX distribuée via les canaux officiels a été **trojanisée** — les binaires signés contiennent une backdoor.

**Mécanisme de la compromission initiale** : l’enquête post-incident a révélé que 3CX lui-même a été compromis via **X_Trader**, un logiciel de trading financier de Trading Technologies, lui-même compromis précédemment par Lazarus. Un employé de 3CX avait installé X_Trader sur sa machine professionnelle ; l’infection de cette machine a donné à Lazarus un accès au réseau 3CX, puis au pipeline de build de leur produit desktop.

**Cascade** : X_Trader compromis → employé 3CX infecté → environnement build 3CX compromis → logiciel 3CX trojanisé → clients 3CX compromis (600 000+ potentiels, avec ciblage sélectif en phase 2). **Le supply chain d’un supply chain** — un niveau d’imbrication nouveau dans les opérations supply chain documentées.

**Impact** : ciblage en phase 2 de clients 3CX spécifiques (entreprises crypto, organisations d’intérêt). Les victimes confirmées publiquement ont été limitées par rapport au pool de 600 000 clients potentiels, confirmant un ciblage sélectif.

**Leçons** : les supply chains peuvent être compromises en cascade — le vecteur peut être éloigné de plusieurs « couches » de la cible finale. La confiance dans un logiciel signé par un éditeur ne suffit plus ; le monitoring comportemental des processus, même légitimes, devient essentiel.

## 12.6 JumpCloud breach (juin 2023) — ciblage crypto via MSP

**Acteur** : Lazarus/Labyrinth Chollima. **Paradigme** : compromission d’un fournisseur de gestion d’identité pour atteindre ses clients crypto.

**Synthèse** : **JumpCloud** est un fournisseur de gestion d’identité SaaS (directory service, SSO, MDM). Lazarus compromet JumpCloud en juin 2023 et abuse des accès pour cibler spécifiquement des **clients JumpCloud dans l’écosystème crypto** — exchanges et sociétés de services crypto. Environ 5 clients de JumpCloud (sur des milliers) ont été touchés — ciblage extrêmement sélectif.

**Significance** : illustration des pivots supply chain ciblés dans l’écosystème crypto. Lazarus a identifié que JumpCloud servait des clients crypto intéressants, et a exploité cette position.

## 12.7 Vols crypto massifs — chronologie

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

## 12.8 Le pipeline de blanchiment

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

## 12.9 Impact géopolitique : cyber comme arme de prolifération nucléaire

La conséquence la plus grave des cyberopérations DPRK est leur **financement direct du programme nucléaire et balistique nord-coréen**. Les estimations ONU et US convergent : une part significative du financement du programme d’armement depuis 2016-2017 vient du cybervol.

**Implication stratégique** : les cyberopérations nord-coréennes ne sont pas un « problème cyber » — elles sont un **problème de sécurité internationale** lié directement à la non-prolifération nucléaire. Chaque dollar volé par Lazarus contribue potentiellement au développement d’armes nucléaires et de vecteurs balistiques.

**Conséquence pour la réponse internationale** : le cadre de sanctions et de contre-mesures s’est durci significativement depuis 2022. Les indictments DOJ contre des opérateurs DPRK et des facilitators, les sanctions OFAC sur des adresses et des entités, les opérations de saisies d’actifs (le DOJ a saisi pour plusieurs centaines de millions de dollars de crypto liés à des vols Lazarus entre 2022 et 2025) construisent une pression croissante.

**Leçon analytique** : quand on regarde une opération DPRK, on regarde un maillon dans une chaîne de financement d’armes nucléaires. Cette perspective change la nature de la menace et la proportionnalité des réponses.

-----
