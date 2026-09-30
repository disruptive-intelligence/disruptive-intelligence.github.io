---
title: PARTIE VIII — ÉTUDES DE CAS INTÉGRÉES
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 8
chapters: 8
---

> **Ce que cette partie apprend.** Articuler l’ensemble des éléments du cours sur des cas complets réels. Chaque chapitre reconstitue un incident emblématique — acteur, contexte géopolitique, TTP, timeline, impact, attribution, réponse, leçons — dans une vue intégrée.
> 
> **Ce qu’elle ne couvre pas.** De nouveaux concepts ou acteurs — tout ce qui est mobilisé ici a été introduit dans les Parties I à VII. Les cas sont inspirés de faits documentés publiquement ; quelques détails techniques peuvent rester classifiés.
> 
> **Ce que vous saurez faire après cette partie.** Lire un incident complexe avec l’ensemble des grilles analytiques du cours, structurer un rapport d’incident APT, et synthétiser les leçons opérationnelles d’un cas complet.

-----

### Chapitre 29 — SolarWinds / SUNBURST : la supply chain comme vecteur d’espionnage

SolarWinds est le **cas d’école** de la compromission supply chain à très grande échelle menée par un acteur étatique sophistiqué. Il mérite un traitement détaillé — timeline, TTP, attribution, leçons.

#### 29.1 Contexte : APT29, SVR, paradigme supply chain

**Acteur** : APT29 / Cozy Bear / Midnight Blizzard — service de renseignement extérieur russe (SVR).

**Paradigme** : la supply chain logicielle comme vecteur d’espionnage stratégique massif. SolarWinds n’était pas la première compromission supply chain étatique — CCleaner (APT17/APT41, 2017), M.E.Doc (Sandworm, 2017 pour NotPetya) l’ont précédée — mais c’est la plus ambitieuse et sophistiquée documentée publiquement.

**Cible SolarWinds** : éditeur de logiciel de supervision réseau basé au Texas. Son produit phare **Orion** est utilisé par **~33 000 organisations** dans le monde, dont une large part du gouvernement fédéral américain, des entreprises Fortune 500, et des infrastructures critiques. C’est précisément cette base installée privilégiée qui en fait une cible APT idéale.

#### 29.2 Timeline détaillée

**Septembre-octobre 2019** : activité suspecte détectable rétrospectivement dans l’environnement de développement SolarWinds. Modifications de « test » dans le code Orion — vraisemblablement la phase de reconnaissance et de préparation de l’attaquant.

**Février 2020** : la backdoor **SUNBURST** est injectée pour la première fois dans un build opérationnel d’Orion. Le mécanisme d’injection ciblait spécifiquement le **processus de build** de SolarWinds — pas une compromission de développeur individuel, mais la compromission de l’infrastructure qui compile le code source en binaires signés.

**Mars 2020** : la mise à jour Orion trojanisée (versions 2019.4 HF5, 2020.2, 2020.2 HF1) est distribuée via les canaux officiels SolarWinds. Tous les clients qui mettent à jour (~18 000 organisations) reçoivent SUNBURST. Le malware est **signé avec le certificat légitime SolarWinds** — rien ne le distingue d’une mise à jour normale.

**Mars-juin 2020** : SUNBURST se propage lentement dans les environnements des victimes. Une fois exécuté, il **attend 12 à 14 jours** avant de s’activer — technique d’évasion pour échapper aux sandboxes automatisées qui analyseraient le fichier pendant quelques minutes seulement. Puis il contacte son serveur C2 (`avsvmcloud.com`, domaine au nom évocateur de services cloud/antivirus légitimes).

**Juillet-décembre 2020** : APT29 examine les signaux reçus des ~18 000 environnements infectés et sélectionne **environ 100 cibles de haute valeur** pour l’exploitation approfondie. Le ciblage sélectif est une signature de l’opération — APT29 n’a pas intérêt à être partout, seulement dans les cibles stratégiques. Sur les cibles sélectionnées, les opérateurs déploient des **outils de seconde étape** :

- **TEARDROP** : loader en mémoire.
- **RAINDROP** : variant de loader identifié ultérieurement.
- **GoldMax / SUNSHUTTLE** : backdoor Go cross-platform.
- **GoldFinder** : HTTP tracer pour reconnaissance d’infrastructure.
- **SIBOT** : backdoor VBScript.

Les cibles finales incluent : **Département du Trésor**, **Département du Commerce**, **Département de la Sécurité intérieure (DHS)**, **Département d’État**, **Département de l’Énergie** (y compris NNSA — National Nuclear Security Administration), **Pentagone** (partiellement), **Microsoft**, **FireEye/Mandiant**, et plusieurs autres grandes entreprises et agences.

**8 décembre 2020** : **FireEye** annonce publiquement avoir été compromis et avoir eu des outils Red Team volés.

**13 décembre 2020** : FireEye publie ses conclusions — l’intrusion chez FireEye provenait de SolarWinds Orion compromis. Publication simultanée d’un rapport technique détaillé sur SUNBURST. L’ensemble de l’écosystème CTI commence à enquêter.

**14 décembre 2020** : SolarWinds confirme la compromission, publie des indicateurs.

**15-20 décembre 2020** : Microsoft et d’autres entités confirment des compromissions. **CISA** publie une Emergency Directive ordonnant aux agences fédérales US de déconnecter Orion ou de le mettre à jour vers une version saine.

**Janvier 2021** : **attribution officielle** par le gouvernement américain — ODNI, NSA, FBI, CISA attribuent à APT29 / SVR russe. L’attribution est renforcée ultérieurement avec le ralliement de Five Eyes + UE en avril 2021.

#### 29.3 TTP détaillées — mapping ATT&CK

SolarWinds est un cas d’étude très documenté en ATT&CK. Techniques principales observées :

- **T1195.002 — Supply Chain Compromise: Compromise Software Supply Chain** : injection de SUNBURST dans le build pipeline SolarWinds.
- **T1218 — Signed Binary Proxy Execution** : SUNBURST est un composant légitime d’Orion, signé numériquement.
- **T1036 — Masquerading** : domaines C2 (avsvmcloud.com, etc.) au nom évocateur de services cloud légitimes. Sous-domaines construits pour ressembler à des requêtes normales.
- **T1071 — Application Layer Protocol: Web Protocols** : C2 HTTPS avec DNS queries de type DNS-over-HTTPS.
- **T1087 — Account Discovery** : énumération des comptes Active Directory.
- **T1550 — Use Alternate Authentication Material** : **GoldenSAML** — forgeage de tokens SAML via compromission d’ADFS, accès aux ressources Azure AD / O365 sans authentification classique.
- **T1528 — Steal Application Access Token** : vol de tokens OAuth Azure AD.
- **T1114 — Email Collection** : accès aux boîtes mail via Graph API en utilisant les tokens SAML forgés.
- **T1078 — Valid Accounts** : usage de comptes légitimes pour le mouvement latéral.
- **T1041 — Exfiltration Over C2 Channel**.

Le chaînage de ces techniques — supply chain → persistence furtive → forgeage d’identité cloud → accès données — est le paradigme que SolarWinds a établi pour les opérations APT cloud modernes.

#### 29.4 GoldenSAML : l’innovation pivot

Le pivot **GoldenSAML** mérite une explication technique dédiée car il est devenu une référence.

**Principe ADFS** : Active Directory Federation Services (ADFS) est le composant Microsoft qui permet l’authentification fédérée. Quand un utilisateur se connecte à Azure AD / O365, ADFS (si configuré) génère un **token SAML** signé par la clé privée d’ADFS. Ce token est présenté à Azure AD comme preuve d’authentification — Azure AD fait confiance à la signature ADFS et autorise l’accès.

**L’attaque GoldenSAML** : l’attaquant qui compromet le serveur ADFS et vole la **clé privée de signature** peut **forger ses propres tokens SAML** pour n’importe quel utilisateur, avec n’importe quels attributs. Azure AD ne peut pas distinguer un token légitime d’un token forgé — la signature est valide.

**Conséquences** :

- L’attaquant peut **se faire passer pour n’importe quel utilisateur**, y compris des administrateurs globaux.
- Accès à **Exchange Online** (lecture de tous les emails), **SharePoint** (tous les documents), **Teams**, **OneDrive**.
- **Persistence sans malware** : tant que la clé n’est pas renouvelée, l’attaquant garde l’accès, sans aucun code malveillant déposé côté cloud.
- **Très difficile à détecter** : les logs Azure AD montrent des authentifications légitimes (tokens valides, signature correcte).

**Remédiation** : nécessite la **régénération des clés ADFS**, idéalement la **reconstruction complète d’ADFS**, et l’audit de tous les accès effectués depuis la compromission — opération lourde qui peut durer des mois.

GoldenSAML, déjà connu théoriquement avant 2020, est devenu **opérationnellement célèbre** avec SolarWinds. D’autres acteurs (notamment chinois) ont adopté la technique ensuite.

#### 29.5 Découverte par FireEye/Mandiant

La découverte de SolarWinds est elle-même une histoire remarquable. FireEye enquêtait sur une intrusion dans son propre environnement — les attaquants avaient volé des outils Red Team. L’investigation interne a remonté jusqu’au vecteur : Orion compromis. FireEye a alors compris que tous ses clients utilisant Orion étaient potentiellement compromis, et au-delà — que l’ensemble du parc Orion dans le monde était compromis.

**La décision de publication** : FireEye aurait pu traiter l’incident en privé. L’entreprise a choisi la **publication rapide et détaillée** (rapport SUNBURST publié dès le 13 décembre 2020). Cette décision, courageuse commercialement (révéler publiquement une compromission est coûteux en réputation), a permis à l’écosystème entier de réagir. C’est devenu un **cas emblématique de l’importance de la transparence** en cybersécurité.

**Kevin Mandia** (alors PDG de FireEye) a conduit les communications publiques. L’entreprise a été saluée pour son approche — le rapport technique est devenu une référence, et la transparence a renforcé (contre-intuitivement) la confiance des clients.

#### 29.6 L’attribution et ses suites

**Attribution officielle** :

- **Janvier 2021** : ODNI, NSA, FBI, CISA attribuent à un acteur russe, probablement le SVR. Confiance : élevée.
- **Avril 2021** : attribution renforcée, mention explicite du SVR. **Sanctions** — l’administration Biden annonce des sanctions contre la Russie (incluant expulsions de diplomates, sanctions financières ciblées).
- **UE et Five Eyes** se coordonnent sur l’attribution.

**Pas d’indictment DOJ** pour SolarWinds (contrairement à certaines autres opérations russes) — probablement parce que les opérateurs individuels sont protégés par le contexte et que l’attribution au niveau étatique était jugée suffisante.

**Pas de représailles cyber déclarées** — les États-Unis ont choisi de répondre par sanctions et diplomatie, pas par action cyber offensive publique en représailles directes.

#### 29.7 Impact et réponse structurelle

**Impact immédiat** :

- **Dwell time** : APT29 avait maintenu l’accès aux environnements les plus sensibles pendant **6 à 12 mois** (voire plus) avant détection.
- **Renseignement collecté** : quantité et nature classifiées, mais probablement massive — emails gouvernementaux US stratégiques, plans, communications diplomatiques.
- **Impact sur la confiance** : ébranlement de la confiance dans la supply chain logicielle. SolarWinds, grand éditeur respecté, était compromis — la question « qui d’autre ? » s’est imposée.

**Réponse structurelle** :

**Executive Order 14028 (mai 2021)** — « Improving the Nation’s Cybersecurity » : réponse américaine majeure à SolarWinds. Exigences :

- **SBOM** (Software Bill of Materials) obligatoire pour les fournisseurs du gouvernement fédéral.
- **Zero Trust** architecture dans les agences fédérales.
- **Amélioration du partage d’information** entre agences et avec CISA.
- **Critical software definition** et contrôles associés.
- **Endpoint Detection and Response** généralisé sur les endpoints fédéraux.

**Cyber Safety Review Board (CSRB)** : création en 2022 sur le modèle du NTSB (investigation d’accidents aériens). Le CSRB investigue les incidents cyber majeurs et publie des rapports. Son premier rapport (juillet 2022) portait sur Log4j ; d’autres ont suivi (Lapsus$, Storm-0558).

**Changements dans l’industrie** : durcissement des build pipelines (isolation, reproducibility, signatures multi-factorielles), Zero Trust sur les mises à jour, monitoring du plan de contrôle identity cloud.

#### 29.8 Leçons opérationnelles

SolarWinds a produit un **corpus de leçons** qui structurent la pratique cyber contemporaine.

**La supply chain logicielle est un vecteur APT majeur** : tous les éditeurs sont des cibles potentielles. Les acheteurs doivent intégrer ce risque dans leurs évaluations.

**La confiance implicite dans un éditeur ne protège pas** : une mise à jour signée par un éditeur légitime peut contenir une backdoor. Le monitoring comportemental des processus, même légitimes, reste indispensable.

**Le monitoring identity cloud est critique** : GoldenSAML, abus OAuth, tokens SAML forgés — la détection d’anomalies dans le plan de contrôle identity est un domaine à part entière de la défense moderne.

**Zero Trust s’impose** : appliqué aux fournisseurs, aux mises à jour, aux authentifications — la confiance ne peut plus être implicite.

**L’intégrité du build pipeline est un enjeu stratégique** : les éditeurs logiciels doivent investir dans la sécurité de leur processus de build (isolation, signatures, audit, reproducibility).

**La transparence bénéficie à l’écosystème** : la décision FireEye de publier rapidement a permis à tous les défenseurs de réagir. Ce modèle de divulgation coordonnée est devenu une référence.

**L’attribution publique coordonnée impose un coût** : les sanctions et expulsions diplomatiques n’ont pas empêché APT29 de continuer, mais elles ont imposé un coût réel à la Russie. L’effet n’est pas nul.

-----

### Chapitre 30 — Lazarus et l’empire crypto de la DPRK

Le paradigme **unique au monde** du financement d’un État par le cybervol de crypto-actifs. Lazarus Group / RGB nord-coréen est le seul cas dans l’histoire où un État finance sa survie et son programme d’armement par des méthodes cybercriminelles.

#### 30.1 Contexte : RGB et modèle économique unique

**Acteur principal** : **Lazarus Group** et sous-structures (APT38/BlueNoroff pour la finance, Kimsuky pour l’espionnage, autres). Tous rattachés au **RGB** (Reconnaissance General Bureau — renseignement militaire nord-coréen).

**Contexte stratégique** : la DPRK est sous **sanctions ONU et internationales** depuis 2006 (renforcées 2009, 2013, 2016, 2017). Coupée des circuits financiers légaux, elle doit financer son régime, son appareil militaire, et surtout son **programme nucléaire et balistique** par des canaux alternatifs — commerce illégal, contrefaçon, et depuis les années 2010, **cybervol**.

**Attribution publique** : FBI, DOJ, Treasury/OFAC ont consolidé l’attribution à la DPRK via de multiples indictments, sanctions, advisories depuis 2018. Les reconstructions techniques par Mandiant, CrowdStrike, Chainalysis, TRM Labs, Elliptic, et d’autres ont alimenté cette attribution avec haute confiance.

**Impact macroéconomique** : les estimations convergent sur un cumul de **3 à 6+ milliards de dollars** volés en crypto-actifs entre 2017 et 2025, avec une accélération récente. Pour un PIB DPRK estimé à ~30 milliards de dollars annuels, le cybervol représente plusieurs pourcents du PIB — ordre de grandeur macroéconomique.

#### 30.2 Chronologie des vols majeurs

Rappel et synthèse consolidée (détaillée au Ch.12) :

**2014-2017 — phase d’expérimentation** :

- **Sony Pictures** (2014) : opération cyber-politique, pas financière, mais démontre l’ambition de Lazarus.
- **Bangladesh Bank** (février 2016) : 81 M$ transférés via SWIFT. Premier braquage bancaire étatique majeur.
- **WannaCry** (mai 2017) : ransomware mondial, peu lucratif (~140 k$) mais démonstration de capacité.

**2018-2021 — pivot crypto et montée en échelle** :

- Multiples vols d’exchanges asiatiques et européens : DragonEx, Upbit, KuCoin, Cream Finance, Badger DAO.
- Cumul estimé à plusieurs centaines de millions.

**2022-2024 — industrialisation** :

- **Ronin Network / Axie Infinity** (mars 2022) : **624 M$**. Accès initial via phishing LinkedIn contre un employé de Sky Mavis. Compromission des clés privées de bridge.
- **Harmony Bridge** (juin 2022) : 100 M$.
- **Atomic Wallet** (juin 2023) : 100 M$.
- **DMM Bitcoin** (mai 2024) : 305 M$.
- **WazirX** (juillet 2024) : 235 M$.
- **Radiant Capital** (octobre 2024) : 50 M$.

**2025 — pic historique** :

- **Bybit** (février 2025) : **~1,5 milliard de dollars** — **le plus gros vol crypto de l’histoire**. Attribution FBI à Lazarus confirmée dans les semaines suivantes.

#### 30.3 Le vecteur social engineering : Opération Dream Job

Le vecteur d’accès initial le plus documenté chez Lazarus est le **social engineering ciblé sur LinkedIn** — l’Opération Dream Job.

**Modus operandi détaillé** :

**Phase 1 — Approche** : un faux profil de recruteur (souvent usurpant un recruteur réel d’une entreprise légitime, ou créé de toutes pièces avec un profil crédible) approche sur LinkedIn un développeur ou ingénieur senior dans une cible stratégique — crypto exchange, entreprise DeFi, éditeur de logiciel, aérospatial. Message personnalisé : « Nous recrutons pour un poste senior chez [entreprise légitime], votre profil correspond parfaitement, êtes-vous intéressé ? »

**Phase 2 — Transition** : la conversation passe à un canal privé (WhatsApp, Telegram, Skype, parfois email personnel). Échanges sur le poste, l’entreprise, la rémunération. Construction de confiance sur plusieurs jours ou semaines.

**Phase 3 — Test technique** : à un moment, le recruteur envoie un « test technique » sous forme de projet à télécharger et exécuter. Peut prendre plusieurs formes :

- Projet en archive ZIP avec un exécutable à tester.
- Projet en Node.js / Python avec des dépendances à installer (qui portent le malware).
- Image Docker à exécuter localement.
- Document PDF avec des exploits.

**Phase 4 — Exécution** : la cible exécute le projet sur **sa machine professionnelle** (car elle a ses outils de développement). Le malware s’exécute dans le contexte de la machine de développement — qui a souvent accès à des secrets (tokens API, clés privées, accès aux systèmes de production, accès au cloud).

**Phase 5 — Pivot** : depuis la machine de développement, l’attaquant pivote vers les systèmes de l’employeur de la victime. Si la victime est un développeur d’exchange crypto, l’attaquant peut accéder aux systèmes de signature de transactions, aux wallets chauds, ou à la chaîne de build du logiciel.

**Cas Ronin Network** (documenté publiquement) : un développeur senior de **Sky Mavis** (studio derrière Axie Infinity) a été approché via LinkedIn par un faux recruteur. Il a exécuté le « test technique » sur sa machine. L’attaquant a pivoté vers les systèmes Sky Mavis, compromis les nodes validateurs du bridge Ronin, et exécuté les transferts frauduleux de **624 millions de dollars**.

**Pourquoi ça marche** :

- L’approche est personnalisée et plausible.
- Les offres d’emploi dans la tech / crypto sont fréquentes et attractives.
- Les développeurs, habitués à exécuter du code inconnu dans leur travail (review de code, contributions open source), ont une garde moins haute.
- Les vérifications d’identité sur LinkedIn sont faibles.

#### 30.4 Les compromissions supply chain : 3CX, JumpCloud

En parallèle du social engineering direct, Lazarus exploite des **supply chains** pour atteindre des cibles crypto en volume.

**3CX (mars 2023)** : supply chain imbriquée déjà traitée (Ch.12). Cascade X_Trader → 3CX → clients 3CX. Ciblage sélectif en phase 2 sur des entreprises crypto parmi les 600 000 clients 3CX.

**JumpCloud (juin 2023)** : compromission d’un fournisseur de gestion d’identité SaaS (directory service, SSO, MDM). Lazarus a pivoté vers **~5 clients JumpCloud dans l’écosystème crypto** — ciblage extrêmement sélectif. Démontre la sophistication — Lazarus identifie les supply chains qui servent des clients crypto, les compromet, et pivote chirurgicalement.

#### 30.5 L’exploitation DeFi

Les plateformes **DeFi** (Finance Décentralisée) sont une cible privilégiée de Lazarus depuis 2022. Pourquoi : quantités massives de fonds (TVL — Total Value Locked — en milliards), smart contracts parfois mal audités, complexité qui crée des vulnérabilités, équipes souvent petites et moins mûres en sécurité qu’un exchange centralisé.

**Vecteurs d’attaque DeFi** :

- **Compromission des clés privées de validateurs** (cas Ronin — bridge multichain avec 9 validateurs, Lazarus en a compromis 5 sur 9, seuil nécessaire pour autoriser un transfert).
- **Exploitation de vulnérabilités dans les smart contracts** (reentrancy, price oracle manipulation, bridge vulnerabilities).
- **Compromission des interfaces web** (pour rediriger les utilisateurs vers des contrats malveillants).
- **Compromission des équipes de développement** (social engineering comme dans Ronin).

**Le cas Bybit (février 2025)** — le plus gros vol crypto de l’histoire :

- **Mécanisme** : compromission présumée d’un compte administrateur de cold wallet via social engineering + exploitation d’une interface de signature. Les détails techniques précis ont été partiellement publiés par Bybit et analysés par Chainalysis.
- **Montant** : ~1,5 milliard de dollars en ETH et stablecoins.
- **Timing** : février 2025, quelques jours de blanchiment avant identification publique.
- **Attribution** : FBI a confirmé l’attribution à Lazarus / DPRK dans les semaines suivantes.
- **Réponse** : Bybit a maintenu la liquidité via des prêts d’urgence et a racheté/remplacé les fonds perdus — transparence remarquable.

#### 30.6 Le pipeline de blanchiment

Une fois les crypto-actifs volés, Lazarus doit les **convertir en devises utilisables**. Ce processus est un sujet d’investigation à part entière — il oppose les défenseurs (Chainalysis, TRM Labs, Elliptic, FBI, OFAC, exchanges majeurs) aux attaquants dans une course constante d’adaptation.

**Étape 1 — Obfuscation on-chain** :

- **Mixers / tumblers** : services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. **Tornado Cash** (Ethereum) était le principal mixer utilisé par Lazarus. **Sanctionné par l’OFAC en août 2022** — première sanction d’un smart contract dans l’histoire. Post-sanction, Lazarus a migré vers d’autres mixers moins connus et vers des techniques de mixing natives on-chain.
- **Samourai Wallet** (Bitcoin) — fermé par les autorités en avril 2024.
- **Wasabi Wallet** (Bitcoin).
- **Privacy coins** : conversion vers Monero (XMR), difficile à tracer on-chain.

**Étape 2 — Bridges cross-chain** : transferts entre blockchains pour complexifier le suivi. Ethereum → BNB Chain → Avalanche → TRON — chaque saut rend le tracing plus complexe. Les **bridges sont également des cibles de Lazarus** (Ronin, Harmony) — ironie où les outils de blanchiment sont aussi des sources de revenus.

**Étape 3 — Conversion en stablecoins** : conversion en **USDT** (Tether) principalement sur la blockchain **TRON** (frais faibles, confirmations rapides, liquidité élevée). L’USDT sur TRON est devenu le canal dominant des flux illicites crypto en général, DPRK incluse.

**Étape 4 — Cashout en fiat** : conversion finale en dollars, euros, yuan.

- **Exchanges à KYC faible** : certains exchanges en Asie, Russie, Golfe ont historiquement eu des pratiques KYC laxistes. Pression réglementaire croissante.
- **OTC desks** (Over-the-Counter) : traders hors-marché qui convertissent crypto en fiat pour commissions élevées. Certains OTC desks basés en Chine ont été identifiés comme facilitators Lazarus — plusieurs ont été sanctionnés par l’OFAC.
- **P2P marketplaces** : LocalBitcoins (fermé 2023), autres.
- **Mules** : réseaux de particuliers recrutés (souvent sans conscience complète) pour recevoir et transférer les fonds.

**Étape 5 — Rapatriement vers la DPRK** : une fois en fiat, circuits opaques — sociétés écrans chinoises, banques complaisantes, parfois transports physiques de cash. Mécanismes largement classifiés.

**Course défensive** :

- **Sanctions OFAC ciblées** : Tornado Cash (2022), adresses crypto spécifiques, OTC desks, ressortissants.
- **Coopération exchanges majeurs** : Binance, Coinbase, Kraken gèlent les fonds identifiés, collaborent avec le FBI. Binance a gelé plus de 4 milliards de dollars liés à des activités illicites entre 2022 et 2024 (tous types, DPRK et autres).
- **Intelligence blockchain** : Chainalysis, TRM Labs, Elliptic fournissent aux autorités des capacités de suivi on-chain.
- **Saisies** : le DOJ a saisi pour plusieurs centaines de millions de dollars de crypto liés à des vols Lazarus entre 2022 et 2025.

L’asymétrie : **les attaquants n’ont qu’à trouver une route qui fonctionne, les défenseurs doivent fermer toutes les routes**. La guerre du blanchiment est permanente.

#### 30.7 Impact géopolitique : cyber comme arme de prolifération

La conséquence la plus grave des cyberopérations DPRK est le **financement direct du programme nucléaire et balistique nord-coréen**.

**Évidences** :

- **Rapports ONU Panel of Experts** : chaque rapport annuel documente l’ampleur du cybervol DPRK et sa contribution au financement du programme d’armement.
- **Déclarations US Treasury** : les sanctions explicitent le lien entre Lazarus et le financement de la prolifération.
- **Timing** : l’accélération du programme nucléaire/balistique nord-coréen (tests de missiles intercontinentaux 2017, tests nucléaires, missiles hypersoniques annoncés) coïncide avec l’intensification du cybervol crypto.

**Implication stratégique** : les cyberopérations nord-coréennes ne sont pas un « problème cyber » — elles sont un **problème de sécurité internationale** lié directement à la non-prolifération nucléaire. Chaque dollar volé par Lazarus contribue potentiellement au développement d’armes nucléaires et de vecteurs balistiques.

**Conséquence pour la réponse** : les mesures anti-Lazarus ne sont pas seulement de la cybersécurité — elles sont partie intégrante de la politique de non-prolifération. Cette perspective justifie l’intensité de la réponse internationale (sanctions OFAC multiples, coordination Treasury/FBI/exchanges, pression sur les juridictions facilitators).

#### 30.8 Les opérateurs IT DPRK : phénomène parallèle

En complément du cybervol, le **phénomène des opérateurs IT DPRK** (détaillé Ch.11.8) représente un autre volet du modèle économique cyber nord-coréen.

**Rappel synthétique** : milliers de ressortissants nord-coréens travaillent à l’étranger sous fausses identités comme développeurs freelance/salariés, générant ~300 M$ par an pour le régime.

**Risques additionnels au-delà du financement** :

- **Introduction de malware** : un opérateur IT DPRK infiltré peut introduire du code malveillant dans les produits de son employeur.
- **Exfiltration de PI** : accès aux secrets techniques de l’employeur.
- **Préparation d’accès pour Lazarus** : un opérateur IT peut préparer des accès privilégiés qui sont ensuite exploités par les équipes Lazarus (opération à deux temps, difficile à détecter).

**Défense** : vérifications d’identité approfondies, background checks, vigilance sur les anomalies comportementales (réticence caméra, horaires décalés, anomalies linguistiques, IP sources incohérentes avec résidence déclarée).

#### 30.9 Réponses internationales

La réponse internationale à Lazarus a évolué vers une stratégie intégrée.

**Sanctions** : sanctions OFAC multiples (personnes, entités, adresses crypto), sanctions UE, sanctions coordonnées. Tornado Cash (2022) et ensembles d’adresses sanctionnées individuellement.

**Indictments** : DOJ a inculpé plusieurs ressortissants nord-coréens pour des opérations spécifiques, facilitators chinois, et des structures-écrans.

**Coopération public-privé** : alliance entre FBI, Treasury, exchanges majeurs, firms d’intelligence blockchain. Partage d’IoC crypto, gels de fonds en temps réel, saisies coordonnées.

**Engagement diplomatique** : pression sur la Chine (principal facilitateur du blanchiment DPRK), sur la Russie (pays de transit), et sur les pays d’Asie du Sud-Est.

**Démantèlements** : Samourai Wallet (2024), OTC desks identifiés — pression continue sur les infrastructures de blanchiment.

**Bilan** : malgré ces efforts massifs, **le cybervol DPRK continue et s’amplifie** (record Bybit 2025). La DPRK adapte ses TTP plus vite que les défenseurs ne ferment les routes. La réponse reste **partielle** — elle limite, sans éliminer.

#### 30.10 Leçons

SolarWinds établit un paradigme technique ; Lazarus établit un paradigme stratégique **unique**.

**Le cybercrime peut être un instrument étatique à échelle macroéconomique** : aucun autre cas documenté dans l’histoire ne combine cette ampleur financière et cette intégration au financement d’un programme d’armement stratégique.

**Les démocraties font face à un acteur non-dissuadable par les moyens classiques** : la DPRK n’a rien à perdre en cyber, les sanctions ne changent pas fondamentalement ses incitations. La réponse doit être **opérationnelle** (fermer les routes de blanchiment) plus que **dissuasive** (imposer un coût qui change les incitations).

**La frontière cybercrime / action étatique est définitivement brouillée** : Lazarus a rendu cette frontière inapplicable comme grille analytique. L’analyse doit considérer la **méthode** et la **finalité** séparément.

**Le secteur privé crypto est en première ligne** : les exchanges, les plateformes DeFi, les développeurs blockchain sont des cibles directes. Les leçons Lazarus (social engineering LinkedIn, supply chain) sont des impératifs de sécurité pour tout l’écosystème crypto.

**Le monitoring blockchain est indispensable** : Chainalysis, TRM Labs, Elliptic ne sont pas des luxes mais des nécessités pour tout acteur significatif du crypto. Le suivi en temps réel des adresses sanctionnées, des flux suspects, et des patterns de blanchiment est désormais une fonction de sécurité standard.

-----

### Chapitre 31 — Volt Typhoon : le pré-positionnement stratégique

Le paradigme du **pré-positionnement sans action** — la menace la plus difficile à détecter et potentiellement la plus lourde de conséquences stratégiques.

#### 31.1 Contexte : PRC, pré-positionnement, scénario Taïwan

**Acteur** : Volt Typhoon — PRC state-sponsored, probablement PLA ou entité affiliée. Attribution fine (quelle unité spécifique) non publiquement précisée à date.

**Attribution publique** : advisory conjoint **NSA, CISA, FBI + Five Eyes** (mai 2023), réitéré et enrichi (2024). Aucun indictment DOJ à date, contrairement à d’autres groupes APT chinois. L’attribution a été faite publiquement avec un niveau de détail technique inhabituel — signe probable d’une volonté de signalement diplomatique forte.

**Paradigme** : pré-positionnement stratégique dans les infrastructures critiques. Pas d’espionnage massif, pas d’exfiltration, pas d’action destructive. Uniquement établir et maintenir un accès dormant, activable en cas de besoin.

**Signification géopolitique** : la communauté de renseignement américaine interprète Volt Typhoon comme une **capacité de dissuasion / représailles chinoise** dans le scénario Taïwan. Message implicite : si les États-Unis interviennent militairement pour défendre Taïwan, la Chine peut frapper les infrastructures critiques américaines — notamment celles qui soutiennent la projection militaire dans le Pacifique (énergie, télécoms, eau, transport à Guam et sur la côte Ouest).

C’est potentiellement **la menace cyber stratégique qui définira la prochaine décennie** — au moins tant que la tension Taïwan reste un enjeu géopolitique majeur.

#### 31.2 Timeline : activité au moins depuis 2021

**Premières détections** : mi-2023 publiquement, avec des traces rétrospectives identifiées jusqu’à **mi-2021 au moins**. Probablement plus tôt — les premières compromissions peuvent remonter à 2019-2020.

**Mai 2023** : **publication de l’advisory conjoint NSA/CISA/FBI + partenaires Five Eyes**. Premier document public détaillé sur Volt Typhoon. L’advisory documente les TTP et plusieurs secteurs cibles, avec des IoC limités (cohérent avec le caractère LotL du groupe).

**2023-2024** : campagne d’observation et d’éradication par les organisations ciblées américaines, avec support CISA/FBI. Documentation progressive des TTP par Microsoft, Mandiant, CrowdStrike et autres.

**Janvier 2024** : **démantèlement partiel par le FBI** — opération **KV Botnet** sous mandat judiciaire. Le FBI a neutralisé un botnet de routeurs **Cisco RV** domestiques et **NetGear** compromis qui servait d’infrastructure C2 à Volt Typhoon. Opération remarquable sur le plan légal — le FBI a exécuté un mandat pour intervenir sur les routeurs domestiques de citoyens américains afin de neutraliser le malware, sans interagir avec les systèmes au-delà de la neutralisation.

**2024-2025** : Volt Typhoon reste actif. Les démantèlements partiels n’ont pas stoppé l’activité — le groupe adapte son infrastructure et continue. Détections continues dans des infrastructures US et alliées.

#### 31.3 Les cibles

**Cibles documentées publiquement** :

- **Opérateurs de télécommunications** aux États-Unis.
- **Fournisseurs d’énergie électrique** dans plusieurs États US.
- **Systèmes d’eau** municipaux.
- **Infrastructures de transport** (portuaires, ferroviaires).
- **Territoires du Pacifique** : **Guam** particulièrement ciblée — importance stratégique majeure en cas de conflit Taïwan (base militaire US, point de projection).

**Cibles non confirmées publiquement mais suspectées** : extension possible à d’autres alliés (Japon, Corée du Sud, Australie, pays européens). Les advisories récents suggèrent une préoccupation au-delà des seuls États-Unis, mais les détails restent partiellement classifiés.

**Profil des cibles** : systématiquement des **infrastructures civiles critiques**, pas des cibles militaires directes. Cohérent avec une stratégie de pré-positionnement qui viserait à **dégrader les capacités de projection et de soutien** en cas de conflit, plutôt qu’à frapper directement les forces militaires.

#### 31.4 TTP : le profil extrême de LotL

Volt Typhoon est **extrême dans sa pureté opérationnelle** — l’archétype de l’APT moderne LotL.

**Accès initial** :

- **Exploitation d’appliances edge** : vulnérabilités sur routeurs SOHO (Cisco RV), VPN, firewalls. **Fortinet FortiGate** documenté. Les appliances ciblées sont souvent des équipements en fin de vie ou non patchés.
- Pas de phishing massif documenté (ce qui distingue Volt Typhoon des APT chinoises plus classiques comme APT10).

**Persistence** :

- **Credentials légitimes** : vol de credentials admin via credential dumping, puis utilisation prolongée. Aucun compte créé par l’attaquant.
- **Pas de malware custom** déposé pour la persistence. La persistence repose sur les credentials volés + scheduled tasks légitimes + services Windows existants.

**Exécution et mouvement latéral** :

- **Living off the Land quasi exclusif** : PowerShell, WMI, net.exe, ntdsutil, ping, tracert, ipconfig, netsh, reg.exe, wmic, certutil. Aucun binaire malveillant identifié à date dans les environnements compromis.
- **Mouvement latéral** : RDP avec credentials admin, WMI, SMB.

**Command and Control** :

- **Routeurs SOHO compromis comme relais C2** : les implants utilisent des routeurs résidentiels compromis (domestiques, clients des FAI US) comme points de sortie. Le trafic C2 semble donc provenir d’**IP résidentielles US légitimes** — fondement dans le trafic domestique, détection réseau extrêmement difficile sans inspection approfondie de contenu.
- **Activité très intermittente** : pas de beaconing régulier, accès occasionnels et limités au minimum nécessaire pour maintenir la présence.

**Collection et exfiltration** :

- **Aucune exfiltration massive** documentée.
- Quelques données collectées (configurations réseau, topologie, credentials) — mais uniquement le minimum nécessaire à maintenir l’accès et comprendre l’environnement.

**Impact** :

- **Aucun** déclenché à ce jour. La capacité est maintenue, pas activée.

Ce profil extrême est **une rupture** par rapport aux APT classiques. Les défenseurs habitués à chercher du malware custom, des signatures, des IoC, sont désarmés.

#### 31.5 Le défi de la détection

La détection de Volt Typhoon et de ses imitateurs est **la question défensive la plus difficile** du paysage cyber contemporain.

**Ce qui ne fonctionne pas** (ou peu) :

- **Antivirus/EDR signature-based** : pas de malware à identifier.
- **Blocklist d’IP/domaines malveillants** : les C2 transitent par des IP résidentielles légitimes.
- **Règles SIEM basées sur IoC** : peu ou pas d’IoC stables.

**Ce qui fonctionne** (partiellement) :

- **Baseline comportementale** : qu’est-ce qui est normal dans cet environnement ? Un `ntdsutil` exécuté depuis un serveur non-DC est anormal. Un compte admin qui se connecte à un système où il ne s’est jamais connecté est anormal. Un flux RDP entre deux machines qui n’ont jamais communiqué est anormal.
- **Détection par corrélation multi-sources** : chaque signal individuel peut sembler normal ; leur combinaison dans un temps court est suspecte. Nécessite un SIEM avec corrélation avancée et des règles soigneusement ajustées.
- **Threat hunting proactif** : recherche active d’indicateurs subtils, pas d’attente d’alertes automatiques. Les hunters qualifiés identifient des patterns (usage inhabituel de LOLBins, activité admin en dehors des heures ouvrées, etc.) que les règles automatiques manquent.
- **Monitoring des appliances edge** : logs exhaustifs, patching rapide, scan de configurations.
- **Détection réseau comportementale** : analyse des flux inhabituels, utilisation anormale de protocoles, patterns de connexions distinctifs.

#### 31.6 Réponse : hardening massive et coordination

**Réponse des organisations ciblées** :

- **Hardening** : renforcement des appliances edge (patching, désactivation des composants inutilisés, restriction des accès admin), durcissement AD, déploiement EDR partout, MFA résistant phishing.
- **Monitoring renforcé** : déploiement de visibilité supplémentaire, règles de détection sur mesure, threat hunting dédié.
- **Réaudit des environnements** : chasse rétrospective d’éventuels pré-positionnements non détectés, sur la base des TTP Volt Typhoon publiées.

**Réponse coordonnée** :

- **Advisory CISA conjoint** : publication des TTP, IoC limités, recommandations. Mise à jour régulière.
- **Partage d’information** : briefings classifiés aux opérateurs d’infrastructures critiques, partage via ISAC (E-ISAC, EE-ISAC, Communications ISAC).
- **Shields Up** (CISA) : posture de vigilance renforcée.
- **Démantèlements FBI** : KV Botnet, Raptor Train (Flax Typhoon, opérateur d’infrastructure similaire).

**Réponse diplomatique** :

- Attributions publiques coordonnées Five Eyes.
- Pas de sanctions spécifiques Volt Typhoon à date — la réponse reste principalement opérationnelle.
- Discussions bilatérales US-Chine évoquent le sujet (sans résultats publics).

#### 31.7 Les démantèlements : KV Botnet et Raptor Train

**KV Botnet (janvier 2024)** : le FBI a démantelé un botnet de routeurs domestiques (Cisco RV110W, RV130, RV130W, RV215W, et NetGear) compromis. Ces routeurs — installés chez des particuliers et petites entreprises américaines — servaient d’infrastructure C2 à Volt Typhoon.

**Mandat judiciaire** : le FBI a obtenu un mandat fédéral pour intervenir sur les routeurs, neutraliser le malware (KV Botnet malware), et bloquer les reconnexions. Opération exécutée sans notification préalable aux propriétaires des routeurs (qui, dans la grande majorité, ignoraient être compromis).

**Raptor Train (septembre 2024)** : démantèlement similaire contre **Flax Typhoon**, autre groupe chinois qui opérait un botnet de plus de **260 000 dispositifs IoT compromis** (routeurs, caméras, NAS) servant potentiellement comme infrastructure offensive pour Volt Typhoon et d’autres clusters chinois.

**Effet** : ces démantèlements imposent un **coût opérationnel réel** — reconstituer l’infrastructure demande du temps et des ressources. Mais ils ne stoppent pas définitivement l’activité — Volt Typhoon adapte son infrastructure, recrée d’autres botnets, et continue.

#### 31.8 Implications stratégiques pour l’Europe

Bien que Volt Typhoon soit principalement documenté aux États-Unis, les implications européennes sont réelles.

**Scénario** : si un conflit majeur éclate (Taïwan, mais aussi par extension Ukraine, Moyen-Orient), la Chine pourrait activer des pré-positionnements dans les pays alliés des États-Unis — y compris en Europe. L’alliance OTAN et les solidarités bilatérales US-Europe font de l’Europe une cible crédible.

**Profil des cibles européennes probables** : similaire à l’expérience US — opérateurs télécoms, énergie, eau, transport. Les **opérateurs d’infrastructures critiques européennes** devraient considérer ce scénario dans leur planification.

**Défense proactive** :

- **Audit des environnements** selon les TTP Volt Typhoon publiées. La plupart des opérateurs n’ont pas fait cet audit en profondeur.
- **Renforcement de la visibilité** sur les appliances edge, identity cloud, OT.
- **Exercices** intégrant le scénario pré-positionnement.
- **Collaboration** avec les agences nationales (ANSSI, BSI, NCSC) et les ISAC sectoriels.

#### 31.9 Leçons : la menace la plus dangereuse est celle qui ne fait rien

Volt Typhoon incarne une leçon stratégique profonde.

**Paradoxe de la visibilité** : les menaces les plus visibles (ransomware massif, wipers, exfiltration documentée) ne sont pas les plus dangereuses stratégiquement. **La menace la plus dangereuse est celle qui maintient un accès silencieux pendant des années, sans produire aucun signal détectable, prête à être activée à un moment politique choisi**.

**Incommensurabilité des détections classiques** : les défenses traditionnelles (signature, IoC, volume anormal, exfiltration détectée) sont aveugles au pré-positionnement LotL. Toute une génération d’outils et de pratiques doit évoluer.

**Le facteur temps joue pour l’attaquant** : plus Volt Typhoon maintient ses accès, plus sa capacité de levier grandit. Les défenseurs sont dans une course contre le temps pour construire la visibilité et les capacités de détection qui permettront l’éradication.

**La dimension géopolitique est centrale** : on ne peut pas comprendre Volt Typhoon sans comprendre le scénario Taïwan. La défense cyber est indissociable de la lecture géopolitique. Un RSSI qui ignore la Taïwan Strategic Ambiguity ne peut pas calibrer sa posture face à un pré-positionnement chinois potentiel.

**La réponse doit être collective** : aucun opérateur ne peut répondre seul. La coopération public-privé (opérateurs, agences nationales, ISAC, vendors CTI) est la condition de l’efficacité. Les organisations qui refusent de partager — par peur de l’exposition — affaiblissent la défense collective y compris la leur.

**L’éradication n’est jamais définitive** : Volt Typhoon ne sera pas « éliminé ». Les démantèlements le réduisent, les hardenings le ralentissent, mais l’acteur étatique sophistiqué s’adapte. La défense est un **processus continu**, pas un état atteint.

-----

### Chapitre 32 — Synthèse BLACKOUT : attribution face à l’incertitude

Synthèse complète du fil rouge du cours — de la détection à la réponse, en passant par l’attribution, en un cas autonome intégré.

#### 32.1 Rappel du contexte et des questions d’investigation

**L’opérateur** : distributeur d’énergie européen, 4 pays (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2. Infrastructure SCADA reliée à plusieurs dizaines de postes de transformation haute tension.

**L’incident** : détection le J+42 par le SOC d’un comportement anormal sur un poste d’ingénierie OT — rundll32 exécutant une DLL non signée + beaconing HTTPS régulier. Triage CERT rapide : profil APT, pas cybercrime.

**Les questions** :

- **QI-1** : Qui est l’attaquant ?
- **QI-2** : Depuis combien de temps est-il présent, et qu’a-t-il fait ?
- **QI-3** : Quelle est son intention (espionnage, sabotage à venir, pré-positionnement) ?
- **QI-4** : Comment l’éradiquer sans qu’il revienne ?
- **QI-5** : Comment communiquer et coordonner avec les autorités ?

#### 32.2 Reconstitution de la timeline

L’investigation approfondie reconstitue la timeline complète.

**J0 (~42 jours avant détection)** : accès initial via exploitation de **CVE-2024-21887** sur un VPN Ivanti Connect Secure non patché. Le VPN est utilisé par des prestataires externes pour la maintenance des systèmes de supervision — sa compromission donne accès à des zones sensibles sans franchir beaucoup de contrôles internes.

**J+3** : persistence établie. DLL sideloading sur une application de supervision légitime (`SupervisionCenter.exe` charge `plugin_common.dll` — la DLL malveillante remplace la DLL légitime dans un répertoire où l’application regarde avant le répertoire système). Deux mécanismes de persistence additionnels créés : tâche planifiée déguisée en mise à jour système, service Windows modifié.

**J+5** : credential access. Mimikatz déployé en mémoire (sans dépôt sur disque), extraction des credentials LSASS. **Kerberoasting** contre plusieurs comptes de service avec SPN et mots de passe faibles — l’un des comptes crackés est un compte de service privilégié avec droits sur les serveurs de supervision.

**J+8** : mouvement latéral. PsExec utilisé pour pivoter depuis la DMZ vers les serveurs internes de supervision. Compromission d’un serveur historian.

**J+15** : pivot vers l’OT. Identification du poste d’ingénierie OT double-connecté (interface IT + interface SCADA). Compromission du poste via credentials admin locaux obtenus dans la phase précédente. DLL sideloading sur ce poste pour la persistence.

**J+15 à J+30** : reconnaissance OT. Consultation des documentations techniques, des schémas, des procédures. Identification des équipements contrôlés (automates Siemens S7-1500, protocole IEC 104 pour la télécommande des disjoncteurs dans les postes de transformation).

**J+30 à J+42** : dormance. L’attaquant ne fait presque rien pendant 12 jours. Simple maintenance de l’accès via beaconing régulier (27 min ± 3 min) vers un domaine hébergé derrière Cloudflare. Aucune action observable sur les automates.

**J+42 — détection** : l’EDR alerte sur le comportement `rundll32.exe` + DLL non signée + beaconing. Début de l’investigation.

#### 32.3 Collecte des artefacts et mapping ATT&CK

Le CERT collecte méthodiquement les artefacts.

**Collecte** :

- **Logs Sysmon** sur les endpoints compromis (récupération complète depuis la rétention SIEM).
- **Event Logs AD** : authentifications, création de tickets Kerberos, accès aux ressources.
- **Captures réseau** pendant plusieurs jours post-détection (pour observer le beaconing).
- **Dump mémoire** du poste d’ingénierie OT (capture volatile avant redémarrage).
- **Artefacts disque** : persistence, DLL malveillantes, outputs de commandes exécutées.
- **Logs des appliances** : VPN Ivanti, firewalls, proxies.

**Mapping ATT&CK** :

- T1190 — Exploit Public-Facing Application (CVE-2024-21887 Ivanti).
- T1574.002 — DLL Side-Loading (persistence).
- T1003.001 — OS Credential Dumping: LSASS Memory (Mimikatz en mémoire).
- T1558.003 — Kerberoasting.
- T1021.002 — Remote Services: SMB/Windows Admin Shares (PsExec).
- T1071.001 — Application Layer Protocol: Web Protocols (C2 HTTPS).
- T1053.005 — Scheduled Task/Job: Scheduled Task (persistence additionnelle).
- T1543.003 — Create or Modify System Process: Windows Service (persistence).
- T1083 — File and Directory Discovery (reconnaissance OT).

Documentation structurée pour transmission aux autorités et à l’ISAC énergie européen.

#### 32.4 Matrice ACH et attribution

Référence détaillée à l’Épisode 6 (Ch.24). Synthèse.

**H1 Sandworm** : confiance modérée. TTP cohérentes, ciblage énergie, contexte géopolitique. Point faible : absence de malware custom Sandworm identifié.

**H2 cluster chinois (Volt Typhoon ou similaire)** : confiance faible à modérée. TTP LotL s’alignent fortement, mais contexte géopolitique moins aligné, beaconing régulier atypique.

**H3 nouveau cluster étatique non attribué** : confiance faible. Ne peut être écartée.

**H4 acteur non-étatique** : **éliminée** (4 incohérences fortes).

**Conclusion** : pré-positionnement OT par acteur étatique — très probable (>80%). Attribution la plus probable Sandworm/GRU confiance modérée, Chine confiance faible-modérée, cluster non identifié possibility. Documentation des indicateurs de révision.

#### 32.5 La réponse : scope avant contenir

Le CERT applique la règle **scope avant contenir**.

**Scope approfondi** (J+42 à J+48) :

- Threat hunting sur tous les endpoints : recherche d’autres systèmes compromis via les TTP identifiées.
- Identification de **2 autres endpoints compromis** non détectés initialement (un autre poste d’ingénierie, un serveur de supervision).
- Identification de **1 compte admin de domaine compromis** (Kerberoasting réussi — credentials cachés sur les systèmes compromis).
- Identification des mécanismes de persistence sur chaque système.
- Cartographie complète : 3 endpoints, 1 compte admin, 3 mécanismes de persistence par endpoint, plusieurs backdoors secondaires.

**Planification du containment coordonné** (J+48) :

- Équipe dédiée constituée (CERT + IT + OT + direction sécurité).
- Plan de containment simultané documenté : éradication de tous les accès dans une fenêtre de 6 heures.
- Playbook de communication (interne, autorités, potentiellement public).

**Containment exécuté (J+49, nuit de vendredi à samedi)** :

- 22h : réinitialisation de **tous** les comptes compromis (changement de mots de passe, révocation des tickets Kerberos via changement du KRBTGT deux fois).
- 23h : isolation réseau des endpoints compromis.
- 23h30 : neutralisation des mécanismes de persistence (suppression des DLL, des tâches planifiées, des services modifiés).
- 01h : patching du VPN Ivanti (vecteur initial) — patches appliqués depuis plusieurs semaines mais vérification et re-validation.
- 02h-06h : reconstruction des systèmes compromis à partir d’images propres.
- 06h : validation des systèmes reconstruits.
- Ensuite : monitoring renforcé, règles de détection spécifiques déployées pour détecter une tentative de réentrée.

#### 32.6 Sécurisation OT post-incident

Post-éradication, l’opérateur renforce sa posture OT.

**Segmentation physique IT/OT renforcée** : revue complète des points de convergence. Plusieurs accès sont reconfigurés, certains supprimés (simplification de l’architecture).

**Déploiement Sysmon/EDR sur les postes d’ingénierie OT** : quand techniquement possible (OS récents). Les postes sur OS hérités font l’objet de compensating controls (restriction réseau, monitoring renforcé en amont).

**Passive monitoring OT** : déploiement d’une solution OT dédiée (Claroty ou équivalent) sur les segments de supervision. Baseline construite sur 30 jours puis règles de détection activées.

**Durcissement AD** : tiering strict, PAM pour les comptes admin, monitoring des changements critiques.

**Patching edge** : processus accéléré (patch en < 48h sur les vulnérabilités CISA KEV).

**Exercice tabletop programmé** : scénario « pré-positionnement OT à nouveau détecté » pour éprouver la coordination après le vécu de l’incident réel.

#### 32.7 Signalement et coordination

**Signalement ANSSI** : l’opérateur étant OIV, la notification à l’ANSSI est obligatoire dès la qualification de l’incident. Notification initiale sous 24h, détaillée sous 72h, rapport complet ultérieurement.

**Accompagnement ANSSI** : équipe technique mobilisée, revue des éléments techniques, partage d’IoC avec d’autres opérateurs français potentiellement concernés.

**Partage ISAC énergie européen (EE-ISAC)** : diffusion TLP:AMBER des IoC et TTP. Dans les 2 semaines suivantes, **2 autres opérateurs européens confirment avoir observé des TTP identiques** — signe que BLACKOUT n’est pas isolé, mais partie d’une campagne plus large ciblant l’énergie européenne.

**Coordination internationale** : les TTP et le contexte sont partagés avec CISA (via l’ANSSI), NCSC UK, BSI. Coordination croisée pour identifier d’autres victimes.

**Attribution publique** : l’opérateur et l’ANSSI décident de **ne pas communiquer publiquement** à court terme. Raisons : éviter d’exposer les méthodes de détection, préserver la capacité de surveillance d’autres opérations potentielles, contexte diplomatique à gérer par les autorités. Une attribution publique pourrait survenir ultérieurement dans le cadre d’un advisory multilatéral coordonné.

#### 32.8 Monitoring post-éradication et veille

Post-éradication, l’opérateur met en place un **monitoring renforcé** pour détecter une éventuelle tentative de réentrée.

**Règles de détection spécifiques** :

- Alertes sur toute exploitation détectée de CVE Ivanti récentes.
- Monitoring des DLL loading dans les applications de supervision (détection de sideloading).
- Baseline comportementale stricte sur les postes d’ingénierie OT.
- Alertes sur tout Kerberoasting détecté.

**Veille sur les indicateurs** : surveillance des IoC publics liés à Sandworm, Volt Typhoon, et clusters associés. Intégration aux flux CTI.

**Threat hunting trimestriel** : chasse active sur les TTP observées, extension progressive à d’autres TTP Sandworm documentées.

**Exercices réguliers** : tabletop trimestriel sur des scénarios APT dérivés de BLACKOUT.

**Résultat à 6 mois** : **pas de détection d’une nouvelle intrusion** dans l’environnement. L’attaquant n’est pas revenu (ou n’a pas été détecté) via les vecteurs surveillés. L’éradication semble efficace.

#### 32.9 La leçon centrale : comprendre les acteurs pour calibrer la réponse

**La leçon centrale de BLACKOUT — et du cours entier** — peut être formulée ainsi : **face à une intrusion sophistiquée, comprendre les acteurs est indispensable pour répondre correctement**.

Sans la connaissance des acteurs, l’analyste face à BLACKOUT :

- Ne sait pas interpréter le **pré-positionnement OT** — s’agit-il d’un sabotage imminent (réaction immédiate brutale nécessaire) ? d’une capacité de dissuasion (réaction mesurée, surveillance longue possible) ? d’une reconnaissance (exfiltration à craindre) ? Les réponses diffèrent radicalement.
- Ne sait pas **calibrer l’urgence** — un acteur qui prépare un sabotage (profil Sandworm en contexte ukrainien escaladant) nécessite une éradication immédiate. Un acteur en pré-positionnement stratégique (profil Volt Typhoon) peut justifier une phase de surveillance contrôlée.
- Ne sait pas **qui alerter et comment** — le signalement ANSSI déclenche des processus différents selon que l’acteur est russe (contexte ukrainien, information-sensibilité diplomatique), chinois (enjeu Taïwan), ou inconnu (prudence supplémentaire).
- Ne sait pas **anticiper les prochains mouvements** — un Sandworm éradiqué tentera probablement de revenir via des vecteurs différents (adaptation rapide des TTP). Un Volt Typhoon éradiqué pourrait se rétablir via des accès redondants non identifiés. Le monitoring post-incident se calibre sur ces profils.

**Un SOC sans connaissance des APT** détecte un beaconing et isole un poste. Un **SOC informé par le cours APT** comprend que ce beaconing dans un OIV énergétique européen en contexte géopolitique tendu est compatible avec un pré-positionnement étatique, calibre l’urgence de la réponse en conséquence, et déclenche les bons processus (signalement ANSSI, partage ISAC, monitoring OT renforcé, potentiellement coordination diplomatique).

C’est la raison d’être de ce cours.

#### 32.10 Ce qui aurait pu rater, ce qu’on aurait pu mieux faire

Post-mortem blameless sur BLACKOUT, dans l’esprit de l’apprentissage continu.

**Ce qui a marché** :

- La **détection EDR** a fonctionné — le comportement anormal (rundll32 + DLL non signée + beaconing) a produit une alerte traitée.
- La discipline **scope avant contenir** a été respectée, évitant une éradication partielle qui aurait alerté l’attaquant.
- La **coordination ANSSI/ISAC** a produit de la valeur — identification d’autres victimes, enrichissement analytique.

**Ce qui aurait pu rater** :

- **Si l’EDR avait été moins bien configuré**, le rundll32 avec DLL non signée serait passé inaperçu. Beaucoup d’organisations n’ont pas ce niveau de configuration.
- **Si l’opérateur n’avait pas eu de visibilité sur les postes d’ingénierie OT** (beaucoup d’organisations OT n’en ont pas), l’attaquant serait resté indétecté probablement des années.
- **Si l’équipe CERT avait été moins mûre**, l’investigation aurait confondu cybercrime et APT, et la réponse aurait été inadaptée.
- **Si le patching Ivanti avait été plus rapide** (CVE-2024-21887 était disponible plusieurs semaines avant la compromission J0), l’intrusion initiale n’aurait pas eu lieu.

**Ce qu’on aurait pu mieux faire** :

- **Détection plus précoce** : 42 jours de dwell time est long. Des baselines comportementales plus matures, des règles de détection sur les TTP Sandworm/Volt Typhoon déjà publiées, auraient pu détecter plus tôt.
- **Visibilité OT dès le début** : le passive monitoring OT déployé post-incident aurait pu détecter le pivot IT→OT beaucoup plus tôt s’il avait été en place. Investissement qui aurait été priorisé en amont.
- **Durcissement des postes double-connectés** : les engineering workstations double-connectés sont le point de rupture structurel. Un durcissement spécifique (EDR dédié, monitoring renforcé, restrictions strictes, MFA systématique) aurait réduit la surface.
- **Exercices APT plus fréquents** : l’organisation avait fait des tabletops généraux, pas spécifiquement sur des scénarios APT OT. L’expérience aurait été plus fluide avec une préparation spécifique.
- **Contacts ISAC établis plus tôt** : la coordination EE-ISAC s’est construite pendant la crise. Des relations établies en amont auraient accéléré le partage.

**La leçon transversale** : la défense APT-ready est un **investissement continu** qui doit être fait **avant** l’incident. Pendant la crise, il est trop tard pour construire les capacités — on ne peut que mobiliser ce qui existe. L’opérateur BLACKOUT avait assez de capacités pour détecter, scoper, et éradiquer avec succès. Mais la perfection relative de la réponse n’efface pas la question : combien d’autres opérateurs européens ont des pré-positionnements similaires non détectés, faute de capacités ?

La réponse à cette question est le sujet des années à venir. Ce cours a tenté d’y contribuer.

-----


## ANNEXES

-----

### Annexe A — Glossaire APT/CTI

|Terme                 |Définition                                                                               |
|----------------------|-----------------------------------------------------------------------------------------|
|**ACH**               |Analysis of Competing Hypotheses — technique analytique de test d’hypothèses concurrentes|
|**AitM**              |Adversary-in-the-Middle — phishing interceptant credentials et cookies de session        |
|**APT**               |Advanced Persistent Threat — acteur étatique sophistiqué et persistant                   |
|**ASD**               |Australian Signals Directorate — agence australienne Five Eyes                           |
|**ATT&CK**            |Framework MITRE des tactiques, techniques et procédures adverses                         |
|**Attribution**       |Processus de liaison d’une activité malveillante à un acteur/service/État                |
|**Backdoor**          |Accès dissimulé maintenu par un attaquant                                                |
|**Beaconing**         |Communication périodique entre un implant et son C2                                      |
|**BGP hijacking**     |Détournement de routes BGP pour intercepter du trafic                                    |
|**BOD**               |Binding Operational Directive — directive contraignante CISA                             |
|**Bootkit**           |Malware persistant au niveau du bootloader/UEFI                                          |
|**BYOVD**             |Bring Your Own Vulnerable Driver — exploitation d’un driver signé vulnérable             |
|**C2**                |Command and Control — infrastructure de commande d’un implant                            |
|**C4**                |Centre de Coordination des Crises Cyber (France)                                         |
|**Campaign**          |Série d’intrusions liées par objectif/période/infrastructure                             |
|**CALEA**             |Communications Assistance for Law Enforcement Act — interception légale US               |
|**CCDCOE**            |Cooperative Cyber Defence Centre of Excellence OTAN, Tallinn                             |
|**CERT**              |Computer Emergency Response Team                                                         |
|**CISA**              |Cybersecurity and Infrastructure Security Agency (US)                                    |
|**Cluster**           |Regroupement d’activités non attribué à un acteur connu                                  |
|**COMCYBER**          |Commandement de la cyberdéfense français                                                 |
|**CSE**               |Communications Security Establishment (Canada)                                           |
|**CSRB**              |Cyber Safety Review Board (US)                                                           |
|**CTI**               |Cyber Threat Intelligence                                                                |
|**DCS**               |Distributed Control System — système de contrôle distribué industriel                    |
|**DCSync**            |Simulation d’un DC pour récupérer les hashs AD                                           |
|**Defend forward**    |Doctrine US de contestation permanente dans les réseaux adverses                         |
|**DIMEFIL**           |Diplomatic, Information, Military, Economic, Financial, Intelligence, Law Enforcement    |
|**DLL sideloading**   |Chargement d’une DLL malveillante via un exécutable légitime                             |
|**DMZ**               |Zone démilitarisée entre réseaux                                                         |
|**Domain fronting**   |Masquage du C2 réel via un CDN légitime                                                  |
|**Dwell time**        |Temps entre compromission initiale et détection                                          |
|**EDR**               |Endpoint Detection and Response                                                          |
|**Edge device**       |Appliance réseau exposée (VPN, firewall, passerelle)                                     |
|**EE / EI**           |Entité Essentielle / Entité Importante (NIS 2)                                           |
|**ENISA**             |European Union Agency for Cybersecurity                                                  |
|**EternalBlue**       |Exploit SMB NSA leaké, utilisé dans WannaCry/NotPetya                                    |
|**Exfiltration**      |Extraction de données depuis l’environnement compromis                                   |
|**False flag**        |Indices plantés pour brouiller l’attribution                                             |
|**FIRST**             |Forum of Incident Response and Security Teams                                            |
|**Five Eyes**         |Alliance US/UK/Canada/Australie/Nouvelle-Zélande                                         |
|**Foothold**          |Point d’ancrage initial                                                                  |
|**FSB**               |Service fédéral de sécurité russe                                                        |
|**GCHQ**              |Government Communications Headquarters (UK)                                              |
|**Golden Ticket**     |Ticket Kerberos TGT forgé via le hash KRBTGT                                             |
|**GoldenSAML**        |Forgeage de tokens SAML via compromission ADFS                                           |
|**GOOSE**             |Generic Object Oriented Substation Event — protocole IEC 61850                           |
|**GRU**               |Direction du renseignement militaire russe                                               |
|**Hacktiviste**       |Acteur motivé par idéologie                                                              |
|**HMI**               |Human-Machine Interface — interface de supervision industrielle                          |
|**HUMINT**            |Human Intelligence — renseignement d’origine humaine                                     |
|**Hunt forward**      |Déploiement d’équipes USCYBERCOM chez les alliés                                         |
|**IAB**               |Initial Access Broker — courtier vendant des accès compromis                             |
|**ICS**               |Industrial Control Systems                                                               |
|**IEC 60870-5-104**   |Protocole européen de télécommande électrique                                            |
|**IEC 61850**         |Standard pour sous-stations électriques                                                  |
|**IEC 61511**         |Norme pour les SIS                                                                       |
|**Implant**           |Code malveillant persistant                                                              |
|**INCD**              |Israel National Cyber Directorate                                                        |
|**Indictment**        |Mise en accusation formelle (DOJ US)                                                     |
|**Intrusion set**     |Ensemble d’activités regroupées par TTP/infrastructure                                   |
|**IoA / IoC**         |Indicator of Attack / Indicator of Compromise                                            |
|**IRGC**              |Islamic Revolutionary Guard Corps (Iran)                                                 |
|**IRGC-IO**           |IRGC Intelligence Organization                                                           |
|**ISAC**              |Information Sharing and Analysis Center                                                  |
|**JTRIG**             |Joint Threat Research Intelligence Group (GCHQ)                                          |
|**Kerberoasting**     |Extraction de tickets de comptes de service pour cracking hors ligne                     |
|**KEV**               |Known Exploited Vulnerabilities — catalogue CISA                                         |
|**Kill Chain**        |Modèle Lockheed Martin des phases d’intrusion                                            |
|**KRBTGT**            |Compte AD dont le hash permet les Golden Tickets                                         |
|**L2I**               |Lutte Informatique d’Influence (France)                                                  |
|**LID**               |Lutte Informatique Défensive (France)                                                    |
|**LIO**               |Lutte Informatique Offensive (France)                                                    |
|**LOLBin**            |Living Off the Land Binary — outil système légitime détourné                             |
|**LotL**              |Living off the Land                                                                      |
|**LSASS**             |Local Security Authority Subsystem Service — credentials Windows en mémoire              |
|**MES**               |Manufacturing Execution System                                                           |
|**MFA**               |Multi-Factor Authentication                                                              |
|**Mimikatz**          |Outil emblématique d’extraction de credentials Windows                                   |
|**MISP**              |Malware Information Sharing Platform                                                     |
|**MOIS / VAJA**       |Ministry of Intelligence and Security iranien                                            |
|**Mossad**            |Service de renseignement extérieur israélien                                             |
|**MSP**               |Managed Service Provider                                                                 |
|**MSS**               |Ministry of State Security — renseignement civil chinois                                 |
|**NCF**               |National Cyber Force (UK)                                                                |
|**NCSC**              |National Cyber Security Centre (UK + équivalents)                                        |
|**NIS 2**             |Directive UE 2022/2555 sur la cybersécurité                                              |
|**NSA**               |National Security Agency (US)                                                            |
|**OEWG**              |Open-Ended Working Group (ONU)                                                           |
|**OFAC**              |Office of Foreign Assets Control (sanctions US)                                          |
|**OIV**               |Opérateur d’Importance Vitale (France)                                                   |
|**OPC DA/UA**         |OLE for Process Control (Data Access / Unified Architecture)                             |
|**OSINT**             |Open Source Intelligence                                                                 |
|**OT**                |Operational Technology — systèmes industriels                                            |
|**Overpass-the-Hash** |Hash NTLM utilisé pour obtenir un ticket Kerberos                                        |
|**Pall Mall Process** |Initiative internationale de régulation des PSO (2024)                                   |
|**PAM**               |Privileged Access Management                                                             |
|**Pass-the-Hash**     |Authentification avec un hash NTLM                                                       |
|**Pass-the-Ticket**   |Réutilisation d’un ticket Kerberos volé                                                  |
|**PASSI**             |Prestataire d’Audit SSI qualifié ANSSI                                                   |
|**PDIS**              |Prestataire de Détection d’Incidents de Sécurité ANSSI                                   |
|**Pegasus**           |Spyware commercial NSO Group                                                             |
|**PERA**              |Purdue Enterprise Reference Architecture                                                 |
|**PIM**               |Privileged Identity Management                                                           |
|**PLA**               |People’s Liberation Army — armée chinoise                                                |
|**PLC**               |Programmable Logic Controller — automate programmable                                    |
|**Pré-positionnement**|Accès dormant dans infra critique pour usage futur                                       |
|**PSO**               |Private Sector Offensive — fournisseur commercial offensif                               |
|**Purdue (modèle)**   |Architecture en niveaux pour systèmes industriels                                        |
|**Purple team**       |Exercice collaboratif red/blue team                                                      |
|**Pyramid of Pain**   |Hiérarchie des indicateurs par coût pour l’attaquant                                     |
|**Ransomware**        |Malware de rançon par chiffrement                                                        |
|**RAT**               |Remote Access Trojan                                                                     |
|**Red team**          |Équipe de simulation offensive                                                           |
|**RGB**               |Reconnaissance General Bureau — renseignement militaire nord-coréen                      |
|**RSSI**              |Responsable de la Sécurité des Systèmes d’Information                                    |
|**RTU**               |Remote Terminal Unit                                                                     |
|**SAML**              |Security Assertion Markup Language — fédération d’identité                               |
|**Sandbox**           |Environnement isolé d’analyse                                                            |
|**SCADA**             |Supervisory Control and Data Acquisition                                                 |
|**SecNumCloud**       |Qualification ANSSI pour services cloud                                                  |
|**Shadow Brokers**    |Groupe ayant leaké des outils NSA en 2016-2017                                           |
|**SIEM**              |Security Information and Event Management                                                |
|**SIGINT**            |Signal Intelligence                                                                      |
|**Silver Ticket**     |Ticket Kerberos de service forgé                                                         |
|**SIL**               |Safety Integrity Level                                                                   |
|**SIS**               |Safety Instrumented Systems                                                              |
|**SOAR**              |Security Orchestration, Automation and Response                                          |
|**SOC**               |Security Operations Center                                                               |
|**Spear-phishing**    |Phishing hautement ciblé                                                                 |
|**SPN**               |Service Principal Name — identifiant Kerberos                                            |
|**SSF**               |Strategic Support Force (PLA chinois jusqu’en 2024)                                      |
|**SSSCIP**            |State Special Communications Service (Ukraine)                                           |
|**STIX**              |Structured Threat Information Expression — format CTI                                    |
|**Supply chain**      |Compromission via un fournisseur de confiance                                            |
|**SVR**               |Service de renseignement extérieur russe                                                 |
|**Sysmon**            |System Monitor Windows — logging avancé                                                  |
|**Tabletop**          |Exercice de simulation sur table                                                         |
|**TAO**               |Tailored Access Operations (NSA historique)                                              |
|**TAXII**             |Trusted Automated Exchange of Intelligence Information                                   |
|**TLP**               |Traffic Light Protocol (RED/AMBER/GREEN/CLEAR)                                           |
|**Tradecraft**        |Savoir-faire opérationnel global de l’attaquant                                          |
|**TTP**               |Tactics, Techniques, and Procedures                                                      |
|**UBO**               |Ultimate Beneficial Owner                                                                |
|**USCYBERCOM**        |United States Cyber Command                                                              |
|**Watering hole**     |Compromission d’un site fréquenté par les cibles                                         |
|**WEP**               |Words of Estimative Probability                                                          |
|**Wiper**             |Malware destructeur qui efface les données                                               |
|**WMI**               |Windows Management Instrumentation                                                       |
|**Zero day**          |Vulnérabilité inconnue de l’éditeur                                                      |
|**Zero Trust**        |Architecture ne faisant confiance à aucun flux par défaut                                |

-----

### Annexe B — Groupes APT majeurs par pays

*Tableau non exhaustif — focus sur les groupes les plus actifs et documentés. La colonne « Statut d’attribution » indique le niveau de publicité et de confiance.*

|Pays               |Mandiant |CrowdStrike       |Microsoft              |Autres alias                   |Service                    |Cibles principales                  |Statut                   |
|-------------------|---------|------------------|-----------------------|-------------------------------|---------------------------|------------------------------------|-------------------------|
|**Russie**         |APT29    |Cozy Bear         |Midnight Blizzard      |NOBELIUM                       |SVR                        |Gouvernements, diplomatie, tech     |Publique, haute          |
|Russie             |APT28    |Fancy Bear        |Forest Blizzard        |Sofacy, STRONTIUM              |GRU Unit 26165             |Militaire, politique, influence     |Publique, haute          |
|Russie             |Sandworm |Voodoo Bear       |Seashell Blizzard      |BlackEnergy group, IRIDIUM     |GRU Unit 74455             |Sabotage, OT, Ukraine               |Publique, haute          |
|Russie             |—        |—                 |—                      |WhisperGate, UAC-0056          |GRU Unit 29155             |Déstabilisation Ukraine/Europe      |Publique 2024, haute     |
|Russie             |Turla    |Venomous Bear     |Secret Blizzard        |Snake group, Uroburos          |FSB Centre 16              |Espionnage long terme, diplomatie   |Publique, haute          |
|Russie             |Gamaredon|Primitive Bear    |Aqua Blizzard          |Shuckworm                      |FSB Centre 18              |Volumétrie massive Ukraine          |Publique, haute          |
|Russie             |Dragonfly|Energetic Bear    |—                      |Berserk Bear                   |FSB (suspecté)             |Énergie                             |Publique, élevée         |
|**Chine**          |APT41    |Wicked Panda      |Brass Typhoon          |Winnti, BARIUM                 |MSS                        |Tech, santé + cybercrime double     |Publique, haute          |
|Chine              |APT40    |Leviathan         |—                      |TA423, TEMP.Periscope          |MSS Hainan                 |Maritime, Five Eyes                 |Publique 2021, haute     |
|Chine              |APT10    |Stone Panda       |—                      |Red Apollo, MenuPass           |MSS Tianjin                |MSP, industriel (Cloud Hopper)      |Publique 2018, haute     |
|Chine              |APT31    |Judgment Panda    |Zirconium              |RedBravo                       |MSS Hubei                  |Parlementaires, politique           |Publique 2024, haute     |
|Chine              |—        |Vanguard Panda    |Volt Typhoon           |BRONZE SILHOUETTE              |PRC (PLA suspecté)         |Pré-positionnement infras critiques |Publique 2023, haute     |
|Chine              |—        |—                 |Salt Typhoon           |GhostEmperor (partiel)         |PRC                        |Télécoms US                         |Publique 2024, haute     |
|Chine              |—        |Ethereal Panda    |Flax Typhoon           |—                              |Integrity Technology Group |Botnets IoT                         |Publique 2024, sanctionné|
|Chine              |—        |—                 |—                      |Mustang Panda, Bronze President|MSS (suspecté)             |Diaspora, ASEAN, Europe             |Publique, élevée         |
|Chine              |—        |Emissary Panda    |—                      |APT27, Bronze Union            |PRC                        |Industrie, défense                  |Publique, élevée         |
|Chine              |APT30    |—                 |—                      |Naikon                         |PLA                        |ASEAN                               |Publique                 |
|Chine              |Hafnium  |Silk Typhoon      |Hafnium                |—                              |PRC                        |ProxyLogon Exchange 2021            |Publique                 |
|Chine              |—        |—                 |Storm-0558             |—                              |PRC (suspecté)             |Microsoft breach 2023               |Publique                 |
|**DPRK**           |—        |—                 |Diamond Sleet          |Lazarus Group, Hidden Cobra    |RGB                        |Tout usage                          |Publique, haute          |
|DPRK               |APT38    |Stardust Chollima |Sapphire Sleet         |BlueNoroff                     |RGB                        |Finance, crypto                     |Publique, haute          |
|DPRK               |—        |Velvet Chollima   |Emerald Sleet          |Kimsuky, Thallium              |RGB                        |Diplomatie, nucléaire               |Publique, haute          |
|DPRK               |APT43    |—                 |Emerald Sleet (partiel)|—                              |RGB                        |Académique, think tanks             |Publique                 |
|DPRK               |—        |Silent Chollima   |Onyx Sleet             |Andariel                       |RGB                        |Ransomware + espionnage             |Publique                 |
|DPRK               |—        |Labyrinth Chollima|Diamond Sleet          |—                              |RGB                        |Supply chain (3CX, JumpCloud)       |Publique                 |
|**Iran**           |APT33    |Refined Kitten    |Peach Sandstorm        |Elfin                          |IRGC                       |Aérospatial, énergie                |Publique, élevée         |
|Iran               |APT34    |Helix Kitten      |Hazel Sandstorm        |OilRig                         |MOIS                       |Moyen-Orient                        |Publique, élevée         |
|Iran               |APT35    |Charming Kitten   |Mint Sandstorm         |Phosphorus, Magic Hound        |IRGC                       |Dissidents, chercheurs, journalistes|Publique, haute          |
|Iran               |APT42    |—                 |—                      |Calanque                       |IRGC-IO                    |Surveillance ciblée                 |Publique                 |
|Iran               |—        |Static Kitten     |Mango Sandstorm        |MuddyWater                     |MOIS                       |Gouvernements, télécoms             |Publique                 |
|Iran               |—        |—                 |—                      |Scarred Manticore              |MOIS                       |Gouvernements ME                    |Publique 2023            |
|Iran               |—        |—                 |—                      |Agrius, Moses Staff, DEV-0270  |IRGC (suspecté)            |Destructif Israël                   |Publique                 |
|**Vietnam**        |APT32    |OceanBuffalo      |—                      |OceanLotus, Cobalt Kitty       |MPS vietnamien             |ASEAN, dissidents                   |Publique, élevée         |
|**Pakistan**       |—        |Mythic Leopard    |—                      |Transparent Tribe              |Services pakistanais       |Inde                                |Publique                 |
|Pakistan           |—        |—                 |—                      |SideCopy                       |Services pakistanais       |Inde                                |Publique                 |
|**Inde**           |—        |—                 |—                      |SideWinder                     |Services indiens (suspecté)|Pakistan, Chine, ASEAN              |Confiance croissante     |
|Inde               |—        |—                 |—                      |Patchwork                      |Services indiens (suspecté)|Pakistan, Asie du Sud               |Confiance croissante     |
|**Turquie**        |—        |—                 |—                      |Sea Turtle                     |Services turcs (suspecté)  |Moyen-Orient, Europe                |Publique                 |
|**Amérique latine**|—        |—                 |—                      |Blind Eagle, APT-C-36          |Colombie (suspecté)        |Amérique latine                     |Publique                 |

-----

### Annexe C — Conventions de nommage par vendor

Chaque vendor CTI utilise sa propre convention. La correspondance n’est jamais parfaite — deux vendors peuvent regrouper ou fragmenter les clusters différemment.

#### C.1 Mandiant (Google Cloud)

- **APTxx** : groupes étatiques attribués. Ex : APT1, APT28, APT29, APT40, APT41.
- **UNCxxxx** : « Uncategorized » — clusters en analyse, pas encore promus. Ex : UNC2452 (cluster initial SolarWinds, devenu APT29), UNC4841 (Barracuda breach, Chine).
- **FINxx** : groupes financièrement motivés. Ex : FIN7, FIN8, FIN11.
- **TEMP.xxx** : préfixe temporaire historique. Ex : TEMP.Periscope (devenu APT40).

Promotion UNC → APT exige convergence de TTP, d’infrastructure et d’objectifs dans le temps.

#### C.2 CrowdStrike — animaux par origine géographique

- **Bear** : Russie. Fancy Bear (APT28), Cozy Bear (APT29), Voodoo Bear (Sandworm), Venomous Bear (Turla), Energetic Bear (Dragonfly).
- **Panda** : Chine. Wicked Panda (APT41), Stone Panda (APT10), Judgment Panda (APT31), Vanguard Panda (Volt Typhoon).
- **Chollima** : DPRK. Stardust Chollima (APT38), Velvet Chollima (APT43), Silent Chollima (Andariel), Labyrinth Chollima.
- **Kitten** : Iran. Charming Kitten (APT35), Helix Kitten (APT34), Refined Kitten (APT33), Static Kitten (MuddyWater).
- **Buffalo** : Vietnam. OceanBuffalo (APT32).
- **Leopard** : Pakistan. Mythic Leopard (Transparent Tribe).
- **Tiger** : Inde.
- **Crane** : Corée du Sud.
- **Jackal** : hacktivisme.
- **Spider** : cybercrime. Scattered Spider, Wizard Spider.

#### C.3 Microsoft — thèmes météo par origine

Refonte en 2023 — ancienne convention (éléments chimiques : NOBELIUM, STRONTIUM) abandonnée.

- **Blizzard** : Russie. Midnight Blizzard (APT29), Forest Blizzard (APT28), Seashell Blizzard (Sandworm), Aqua Blizzard (Gamaredon), Secret Blizzard (Turla).
- **Typhoon** : Chine. Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon (APT41), Silk Typhoon (Hafnium).
- **Sleet** : DPRK. Diamond Sleet (Lazarus), Sapphire Sleet (APT38), Emerald Sleet (Kimsuky), Onyx Sleet (Andariel).
- **Sandstorm** : Iran. Peach Sandstorm (APT33), Mint Sandstorm (APT35), Hazel Sandstorm (APT34), Mango Sandstorm (MuddyWater).
- **Storm-xxxx** : cybercrime non encore promu. Storm-0558, Storm-1516.
- **Tempest** : acteurs privés / PSO.
- **Flood** : DDoS hacktivisme.
- **Tsunami** : cybercrime sophistiqué.
- **Dust** : non attribué.

#### C.4 Kaspersky

Nommage moins systématisé, souvent créatif : **Turla**, **Equation Group**, **BlueNoroff**, **ProjectSauron**, **Careto/The Mask**, **Sofacy** (APT28). Reflète l’histoire des découvertes.

#### C.5 Secureworks — métaux par origine

- **Bronze** : Chine. Bronze Butler (Tick), Bronze President (Mustang Panda), Bronze Union (APT27).
- **Cobalt** : Russie et autres, parfois Iran. Cobalt Mirage (Iran).
- **Gold** : cybercrime.
- **Iron** : Iran (partiellement).
- **Tin** : DPRK.
- **Nickel** : autres.

#### C.6 Palo Alto Networks / Unit 42

Nommage par nature plus descriptif, parfois par thématique :

- **Stately Taurus** = Mustang Panda.
- **Fighting Ursa** = APT28.
- **Mushroom Leviathan** = en lien avec APT40.
- Nommages plus variables.

#### C.7 ESET

Nommage souvent simple, parfois hérité d’autres vendors. Publications avec focus technique marqué (Industroyer, Industroyer2, CaddyWiper, NightEagle).

#### C.8 Correspondances pratiques pour l’analyste

Quand un rapport mentionne un nom inconnu :

- Rechercher sur **MITRE ATT&CK Groups** (`attack.mitre.org/groups/`) — la page de chaque groupe liste les alias connus.
- Rechercher sur **Malpedia** (`malpedia.caad.fkie.fraunhofer.de`) — base de données allemande qui consolide les correspondances.
- Consulter le **Thaicert APT Groups and Operations** (référence communautaire).
- Croiser 2-3 vendors sérieux (Mandiant, Microsoft, CrowdStrike) pour consolider la correspondance.

**Règle pratique** : noter systématiquement les alias Mandiant (APTxx) et Microsoft dans vos rapports — ce sont les deux conventions les plus largement partagées.

-----

### Annexe D — Timeline des cyberattaques étatiques (2007-2026)

Chronologie non exhaustive des événements majeurs. Sélection privilégiant les cas emblématiques et les ruptures.

|Année    |Événement                                |Acteur attribué            |Type                   |Impact / signification                                                            |
|---------|-----------------------------------------|---------------------------|-----------------------|----------------------------------------------------------------------------------|
|2007     |Cyberattaque contre l’Estonie            |Russie (attribué)          |DDoS massif            |Premier cas d’attaque étatique contre un État — institutions paralysées 3 semaines|
|2008     |Géorgie — cyberattaques pendant la guerre|Russie                     |DDoS + défacement      |Premier cas documenté de cyber + conflit militaire conventionnel                  |
|2009     |Operation Aurora                         |Chine                      |Espionnage             |Google, Adobe, Intel compromis — révélé publiquement par Google janvier 2010      |
|2010     |Stuxnet découvert                        |US + Israël (attribué)     |Sabotage OT            |Première arme cyber OT — ~1000 centrifugeuses iraniennes détruites                |
|2011     |RSA breach                               |Chine (suspecté)           |Espionnage             |Vol de données SecurID — cascade vers Lockheed Martin et autres                   |
|2012     |Shamoon v1 contre Saudi Aramco           |Iran                       |Wiper                  |30 000 postes détruits — représailles pour Stuxnet                                |
|2013     |Mandiant APT1 report                     |—                          |Publication            |Rapport fondateur exposant PLA Unit 61398                                         |
|2014     |Sony Pictures                            |DPRK (Lazarus)             |Cyber-intimidation     |Vol + publication + wiper — représailles pour *The Interview*                     |
|2014     |Annexion Crimée — cyberattaques Ukraine  |Russie                     |Multiples              |Début d’un cycle long contre l’Ukraine                                            |
|2014     |OPM breach                               |Chine                      |Espionnage massif      |21.5M dossiers d’employés fédéraux US exfiltrés                                   |
|2015     |Bundestag compromis                      |Russie (APT28)             |Espionnage             |Parlement allemand compromis plusieurs semaines                                   |
|2015     |Ukraine blackout décembre                |Russie (Sandworm)          |Sabotage OT            |Premier blackout cyber confirmé — 230 000 foyers                                  |
|2016     |Ukraine blackout décembre (Industroyer)  |Russie (Sandworm)          |Sabotage OT            |Premier malware OT dédié aux protocoles industriels                               |
|2016     |Bangladesh Bank                          |DPRK (APT38)               |Cyber-braquage         |81 M$ transférés via SWIFT                                                        |
|2016     |DNC hack                                 |Russie (APT28)             |Ingérence électorale   |Hack-and-leak via DCLeaks/WikiLeaks                                               |
|2017     |WannaCry                                 |DPRK (Lazarus)             |Ransomware worm        |200 000+ systèmes dans 150 pays — NHS affecté                                     |
|2017     |NotPetya                                 |Russie (Sandworm)          |Wiper mondial          |$10+ Mrd de dommages — cyberattaque la plus destructrice de l’histoire            |
|2017     |Triton / TRISIS                          |Russie (TsNIIKhM)          |Sabotage OT/SIS        |Première attaque documentée contre les SIS (Triconex)                             |
|2017     |Shadow Brokers leaks                     |—                          |Fuite d’outils NSA     |EternalBlue, DoublePulsar publiés                                                 |
|2017     |Equifax breach                           |Chine                      |Espionnage             |147M dossiers crédits US exfiltrés                                                |
|2017     |CCleaner supply chain                    |Chine (APT41)              |Supply chain           |2,27M machines infectées                                                          |
|2018     |Olympic Destroyer (Pyeongchang)          |Russie (Sandworm)          |Sabotage + false flags |False flags Lazarus plantés                                                       |
|2018     |Mandiant + DOJ indict APT10              |—                          |Attribution            |2 ressortissants chinois MSS Tianjin inculpés (Cloud Hopper)                      |
|2018     |Indictment 12 officiers GRU              |—                          |Attribution            |Officiers nommés pour DNC hack 2016                                               |
|2019     |Capital One breach                       |—                          |Cybercrime             |100M dossiers exposés                                                             |
|2019     |APT34 (OilRig) leak                      |Anonyme                    |Fuite iranienne        |Outils et victimes OilRig publiés sur Telegram                                    |
|2020     |SolarWinds / SUNBURST                    |Russie (APT29)             |Supply chain           |~18 000 orgs infectées, ~100 cibles actives                                       |
|2020     |Indictment APT41                         |—                          |Attribution            |5 ressortissants chinois MSS inculpés                                             |
|2020     |Ciblage vaccins COVID                    |Russie + Chine + Iran      |Espionnage             |Multiples acteurs ciblent les développeurs de vaccins                             |
|2021     |Attribution publique SolarWinds          |—                          |Attribution            |Five Eyes + UE attribuent à SVR                                                   |
|2021     |ProxyLogon / Hafnium                     |Chine (Hafnium)            |0-day massif           |30-250 000 orgs Exchange compromises mondialement                                 |
|2021     |Colonial Pipeline                        |DarkSide (criminel)        |Ransomware             |Pénuries essence côte est US                                                      |
|2021     |Kaseya supply chain                      |REvil (criminel)           |Supply chain           |Impact massif via MSP                                                             |
|2021     |Pegasus Project                          |—                          |Publication            |17 médias exposent usage NSO Pegasus contre journalistes/dissidents               |
|2021     |NSO + Candiru Entity List                |—                          |Sanctions US           |Entités israéliennes sanctionnées                                                 |
|2021     |Indictment APT40                         |—                          |Attribution            |MSS Hainan inculpé, Hainan Xiandun révélée                                        |
|2021     |Executive Order 14028 (Biden)            |—                          |Réponse structurelle   |Réponse SolarWinds — SBOM, Zero Trust fédéral                                     |
|2022     |Invasion russe Ukraine (février)         |—                          |Contexte               |Intensification massive des cyberopérations                                       |
|2022     |HermeticWiper / WhisperGate / CaddyWiper |Russie                     |Wipers                 |Vagues destructives Ukraine                                                       |
|2022     |Viasat KA-SAT (AcidRain)                 |Russie (Sandworm)          |Sabotage infrastructure|Jour-J invasion — impact collatéral 5800 éoliennes allemandes                     |
|2022     |Industroyer2                             |Russie (Sandworm)          |Tentative OT           |**Déjouée** par CERT-UA + ESET                                                    |
|2022     |Tornado Cash sanctionné OFAC             |—                          |Sanctions              |Premier smart contract sanctionné                                                 |
|2022     |Ronin Network (Axie)                     |DPRK (Lazarus)             |Vol crypto             |624 M$ — phishing LinkedIn                                                        |
|2022     |Albanie attaquée par Iran                |Iran                       |Wipers + ransomware    |Première rupture diplomatique pour cause cyber                                    |
|2022     |ContiLeaks                               |Dissident interne          |Fuite criminelle       |Échanges Conti + liens présumés FSB                                               |
|2023     |3CX supply chain                         |DPRK (Lazarus)             |Supply chain imbriquée |600 000+ clients potentiels, ciblage sélectif                                     |
|2023     |Volt Typhoon advisory                    |—                          |Attribution            |Five Eyes publient sur pré-positionnement chinois                                 |
|2023     |Microsoft Storm-0558                     |Chine                      |Breach cloud           |Emails gouvernementaux US via clé MSA compromise                                  |
|2023     |Barracuda ESG CVE-2023-2868              |Chine (UNC4841)            |Exploitation edge      |8 mois d’exploitation avant découverte                                            |
|2023     |Citrix Bleed (CVE-2023-4966)             |Multiples                  |Exploitation edge      |Vague massive, APT + ransomware                                                   |
|2023     |Operation Medusa (Snake/Turla)           |FBI                        |Démantèlement          |Neutralisation Snake malware mondiale                                             |
|2023     |Qakbot démantelé                         |FBI + Europol              |Démantèlement          |Operation Duck Hunt — 700k machines nettoyées                                     |
|2023     |Opération 7 octobre + cyber Israël       |Hamas + Iran + hacktivistes|Conflit                |Cyber dimension du conflit Israël-Hamas                                           |
|2024     |Leak i-Soon                              |Dissident interne          |Fuite                  |Écosystème contractor chinois documenté                                           |
|2024     |Ivanti CVE-2024-21887                    |Multiples APT              |0-day                  |Vague massive (Volt Typhoon, APT40, APT31)                                        |
|2024     |Microsoft compromis par APT29            |Russie (APT29)             |Identity breach        |Password spray → emails dirigeants Microsoft                                      |
|2024     |KV Botnet démantelé                      |FBI                        |Démantèlement          |Infrastructure C2 Volt Typhoon neutralisée                                        |
|2024     |LockBit démantelé (Cronos)               |NCA + FBI + Europol        |Démantèlement          |Plus grand opérateur RaaS                                                         |
|2024     |Indictment APT31 + sanctions UK/US       |—                          |Attribution coordonnée |Ciblage parlementaires UK/US                                                      |
|2024     |Advisory APT40 (AUKUS+)                  |—                          |Attribution            |AUKUS + Canada + Allemagne + Japon + Corée Sud                                    |
|2024     |NIS 2 entrée en application              |UE                         |Cadre réglementaire    |Périmètre cybersécurité massivement élargi                                        |
|2024     |EU Cyber Solidarity Act                  |UE                         |Cadre                  |Réseau SOC européens, réserve cyber                                               |
|2024     |Pall Mall Process lancé                  |UK + France                |Initiative             |Régulation PSO internationale                                                     |
|2024     |Raptor Train / Flax Typhoon démantelé    |FBI                        |Démantèlement          |260 000 dispositifs IoT compromis                                                 |
|2024     |Salt Typhoon révélé                      |—                          |Attribution            |Télécoms US compromis (Verizon, AT&T, Lumen)                                      |
|2024     |Cyber Av3ngers contre eau US             |Iran                       |Symbolique             |PLC Unitronics exposés ciblés                                                     |
|2024     |Advisory Unit 29155                      |—                          |Attribution            |GRU Unit 29155 publiquement documentée                                            |
|2024     |Salt Typhoon accès interception légale   |Chine                      |Espionnage stratégique |Lawful intercept systems compromis                                                |
|2025     |Bybit hack                               |DPRK (Lazarus)             |Vol crypto             |**~1,5 Mrd$** — plus gros vol crypto de l’histoire                                |
|2025     |Integrity Technology Group sanctionné    |—                          |Sanctions OFAC         |Contractor chinois sanctionné (Flax Typhoon)                                      |
|2025-2026|Vagues edge continues                    |Multiples                  |Exploitation           |Palo Alto, Fortinet, Cisco vulnérabilités exploitées                              |

-----

### Annexe E — Mapping ATT&CK par acteur

*Techniques ATT&CK les plus caractéristiques de 15 groupes majeurs. Les techniques marquées en gras sont les signatures distinctives. Liste simplifiée — la matrice complète pour chaque acteur est sur MITRE ATT&CK Groups.*

|Acteur                         |Initial Access                                             |Execution                                      |Persistence                                       |Cred Access                                       |Lateral Movement            |C2                                                 |Impact / Signature                                        |
|-------------------------------|-----------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|--------------------------------------------------|----------------------------|---------------------------------------------------|----------------------------------------------------------|
|**APT29** (Russie/SVR)         |**T1195.002** Supply chain, **T1566** OAuth phishing, T1078|T1218 Signed binary proxy, T1059.001 PowerShell|**T1550.001** SAML tokens, T1098 Application OAuth|T1003 Credential dumping, T1110.003 Password spray|**GoldenSAML**, T1021       |T1071.001 HTTPS, **T1102** Services cloud légitimes|Furtivité extrême, cloud-focused                          |
|**APT28** (Russie/GRU 26165)   |**T1566.001** Spear-phishing, T1190                        |T1059.001 PowerShell, scripts                  |T1543.003 Services, T1547 Registry                |**T1003.001** Mimikatz, credential harvest        |T1021.001 RDP, T1021.002 SMB|T1071.001 HTTPS, T1102                             |Exploitation 0-day Outlook                                |
|**Sandworm** (Russie/GRU 74455)|**T1195** Supply chain, T1190 Edge exploit                 |T1059, custom malware                          |**T1543.003** Services, T1053 Scheduled tasks     |T1003 Mimikatz                                    |T1021 PsExec, T1047 WMI     |T1071.001 HTTPS, custom                            |**T1485 Data Destruction, T1561 Disk Wipe**, OT protocoles|
|**Unit 29155** (Russie/GRU)    |T1190, T1566                                               |T1059, Impacket                                |T1543, T1053                                      |T1003 Mimikatz                                    |T1021                       |T1071.001                                          |T1485/T1561 Wipers (WhisperGate)                          |
|**Turla** (Russie/FSB)         |**T1189** Watering hole, T1195                             |T1059, **rootkits kernel**                     |**T1542 Firmware**, T1014 Rootkits                |Custom tools                                      |T1090 Proxies satellite     |**T1102** Satellite détournement, piggybacking     |Sophistication extrême                                    |
|**APT41** (Chine/MSS)          |**T1195** Supply chain, T1190                              |Custom malware                                 |**T1542 Bootkits** (MoonBounce), T1014            |T1003                                             |T1021.001 RDP, T1021.002 SMB|T1071.001 HTTPS                                    |**Double mission** espionnage + cybercrime                |
|**APT40** (Chine/MSS Hainan)   |**T1190** Edge appliances                                  |Scripts, web shells                            |**T1505.003** Web shells                          |T1003                                             |T1021 SMB, RDP              |T1071.001                                          |Exploitation rapide CVE                                   |
|**APT10** (Chine/MSS Tianjin)  |**T1199** Trusted relationship (MSP)                       |Custom malware                                 |T1543.003, T1547                                  |T1003                                             |T1021                       |T1071.001                                          |MSP-based supply chain                                    |
|**Volt Typhoon** (Chine)       |**T1190** Edge devices                                     |**T1059 LotL exclusif**                        |T1078 Valid accounts                              |T1003 ntdsutil                                    |T1021.001 RDP avec LoTL     |**Routeurs SOHO compromis** (T1584.008)            |**Pas de malware custom**, pré-positionnement             |
|**Salt Typhoon** (Chine)       |T1190                                                      |T1059                                          |T1542 Firmware télécoms                           |T1003                                             |T1021                       |T1071                                              |**Lawful Intercept Systems**                              |
|**Lazarus** (DPRK)             |**T1566** Social engineering LinkedIn, T1195 Supply chain  |Custom malware multi-OS                        |T1543, T1547                                      |T1003, keyloggers                                 |T1021                       |T1071.001 HTTPS, custom                            |**Vol crypto**, AppleJeus                                 |
|**APT38** (DPRK/BlueNoroff)    |**T1566** Finance social eng                               |Custom malware                                 |T1543                                             |Custom                                            |T1021                       |T1071                                              |**SWIFT**, DeFi exploits                                  |
|**APT35** (Iran/IRGC)          |**T1566 Ultra-social eng**, faux LinkedIn                  |Scripts, backdoors légers                      |T1547 Registry, T1543                             |T1056 Credential phishing                         |Minimal                     |T1071.001                                          |**Impersonation individuelle extrême**                    |
|**APT33** (Iran/IRGC)          |**T1110.003 Password spraying** massif                     |T1059 PowerShell                               |T1543 Services                                    |T1110.003                                         |T1021.001 RDP               |T1071.001                                          |Volume, énergie                                           |
|**MuddyWater** (Iran/MOIS)     |T1566 Phishing                                             |**T1059.001 PowerShell obfusqué**              |T1547                                             |T1003                                             |T1021                       |T1071                                              |Outils open source                                        |

Pour consulter la matrice complète de chaque acteur : **attack.mitre.org/groups/**.

-----

### Annexe F — Malwares et implants emblématiques

Catalogue des malwares les plus significatifs par acteur, avec fonction principale et signification. Non exhaustif.

#### F.1 Russie — APT29 (SVR)

- **SUNBURST** (2020) : backdoor injectée dans SolarWinds Orion. Compilée directement dans les builds légitimes via compromission du pipeline de build. Communications C2 DNS camouflées en requêtes Orion Improvement Program.
- **TEARDROP** / **RAINDROP** : loaders en mémoire déployés en phase 2 après SUNBURST. Minimal footprint, exécution en mémoire.
- **GoldMax / SUNSHUTTLE** : backdoor Go cross-platform. Rare pour sa sophistication et son langage (Go est peu courant dans le malware APT).
- **GoldFinder** : HTTP tracer pour reconnaissance d’infrastructure de victime.
- **FoggyWeb** : backdoor ADFS post-exploitation (2021). Communications via cookies Exchange calibrés.
- **MagicWeb** (2022) : backdoor ADFS évolution de FoggyWeb. Manipulation de la gestion des certificats pour forgeage d’authentification.

#### F.2 Russie — APT28 (GRU 26165)

- **X-Tunnel** : proxy tunneling utilisé pour le mouvement latéral.
- **XAgent** : backdoor modulaire cross-platform (Windows, macOS, iOS, Android — l’une des rares familles APT avec présence mobile).
- **Zebrocy** : famille de backdoors développée en multiples langages (Delphi, Go, Python, C++) — tradecraft inhabituel qui complique l’analyse.
- **Seduploader** : implant léger.
- **CredoMap** : stealer de credentials.
- **Cannon** : backdoor Office.

#### F.3 Russie — Sandworm (GRU 74455)

- **BlackEnergy** : framework utilisé dans les attaques Ukraine 2015 (historique, bien documenté).
- **Industroyer / CrashOverride** (2016) : premier malware OT spécifiquement conçu pour attaquer les protocoles industriels (IEC 60870-5-104, IEC 61850, OPC DA).
- **Industroyer2** (2022) : évolution tentée, déjouée par CERT-UA et ESET.
- **NotPetya / ExPetr** (2017) : wiper masqué en ransomware. Propagation via EternalBlue + credentials.
- **CaddyWiper** (2022) : wiper déployé contre l’Ukraine.
- **HermeticWiper / FoxBlade** (février 2022) : wiper déployé la veille de l’invasion.
- **IsaacWiper** (février 2022) : wiper concurrent.
- **AcidRain** (février 2022) : wiper contre terminaux satellite Viasat KA-SAT.
- **CaddyWiper**, **WhisperKill**, **Double-Zero** (2022) : autres variants de wipers.
- **CosmicEnergy** (2023) : malware OT découvert par Mandiant via VirusTotal, capacités IEC 60870-5-104.
- **Cyclops Blink** (2022) : botnet sur routeurs ASUS et WatchGuard, démantelé par le FBI.

#### F.4 Russie — Unit 29155

- **WhisperGate** (janvier 2022) : wiper déployé contre l’Ukraine quelques semaines avant l’invasion. Masqué en ransomware (note de rançon factice).

#### F.5 Russie — Turla (FSB Centre 16)

- **Snake / Uroburos** : rootkit multi-plateforme (Windows, Linux, macOS). Actif depuis au moins 2003. **Démantelé par le FBI en mai 2023 (opération Medusa)**.
- **Kazuar** : backdoor modulaire .NET.
- **LightNeuron** : backdoor Exchange serveur (transport agent malveillant) — intercepte les emails au niveau serveur.
- **Crutch** : backdoor Windows.
- **Carbon / Cobra** : framework modulaire historique.
- **ComRAT** : backdoor .NET, une des plus anciennes familles Turla.

#### F.6 Chine — APT41

- **Winnti** : famille d’implants Windows/Linux, la signature historique du groupe. Multiples variants depuis les années 2010.
- **ShadowPad** : backdoor modulaire sophistiquée, utilisée par plusieurs APT chinoises.
- **PipeMon** : modulaire.
- **Crosswalk** : RAT.
- **MoonBounce** (découvert par Kaspersky) : **bootkit UEFI**. Persistence au niveau firmware. Sophistication extrême.
- **HyperBro** : backdoor Windows (aussi utilisée par APT27).

#### F.7 Chine — autres APT chinoises

- **PlugX** : famille historique largement partagée entre APT chinoises (APT10, APT27, Mustang Panda, autres). Variants multiples.
- **ChChes** (APT10) : backdoor.
- **Redleaves** (APT10).
- **UPPERCUT** (APT10).
- **HAYMAKER** (APT10).
- **ToneShell** / **Hodur** (Mustang Panda) : évolutions récentes.
- **SysUpdate** (APT27) : backdoor.
- **ZxShell** (APT27) : RAT.

#### F.8 DPRK — Lazarus et sous-groupes

- **FALLCHILL** : backdoor Windows.
- **BADCALL** : backdoor.
- **HOPLIGHT** : backdoor avec proxy.
- **DTrack** : backdoor.
- **AppleJeus** : **malware macOS** ciblant les utilisateurs crypto (l’une des rares familles APT ciblant macOS avec profondeur).
- **Manuscrypt / NukeSped** : backdoors Windows.
- **TAINTEDSCRIBE** : downloader.
- **CROWDEDFLOUNDER** : RAT.
- **VHD Ransomware** : rare — Lazarus a déployé du ransomware ciblé ponctuellement.

#### F.9 Iran

- **Shamoon v1/v2/v3** (APT33) : wipers destructifs. Saudi Aramco 2012 (30 000 postes détruits).
- **ZeroCleare** : wiper proche de Shamoon.
- **Dustman** : wiper.
- **StoneDrill** : wiper apparenté à Shamoon.
- **QUADAGENT** (APT34/OilRig) : backdoor.
- **OopsIE** (APT34) : backdoor.
- **Helminth** (APT34) : backdoor.
- **BabyShark** (Kimsuky — attention, il existe plusieurs malwares appelés ainsi, vérifier le contexte).
- **Liderc** (APT35) : backdoor.
- **Apostle / DEADWOOD / Moneybird** (Agrius) : wipers sous fausses bannières.

#### F.10 Mercenaires cyber

- **Pegasus** (NSO Group) : spyware mobile, iOS et Android. Capacités complètes (messages E2EE lus en post-déchiffrement, micro/caméra, géoloc).
- **Predator** (Intellexa) : spyware mobile concurrent de Pegasus.
- **DevilsTongue** (Candiru) : spyware desktop Windows.
- **Reign** (QuaDream — société fermée en 2023 suite aux révélations Citizen Lab) : spyware mobile.
- **Graphite** (Paragon) : spyware mobile récent.

#### F.11 Outils offensifs commerciaux / open source massivement utilisés

- **Cobalt Strike** : plateforme C2 commerciale, largement « crackée ». Utilisée par la quasi-totalité des APT et groupes ransomware.
- **Brute Ratel C4** : concurrent commercial, cracké également.
- **Sliver** (BishopFox, open source) : framework C2 open source.
- **Havoc** : framework open source récent.
- **Mythic** : plateforme C2 modulaire open source.
- **Metasploit** : pentest framework historique.
- **Empire / PowerShell Empire** : C2 PowerShell historique.
- **Mimikatz** : credential dumping, utilisé universellement.
- **BloodHound / SharpHound** : énumération AD, utilisée par red teams et APT.
- **Impacket** : toolkit Python pour protocoles Windows, utilisation massive.
- **Rubeus** : outil Kerberos.
- **NanoDump, SafetyKatz, SharpKatz** : alternatives furtives à Mimikatz.

**Leçon importante** : la détection d’un de ces outils **ne discrimine rien sur l’acteur** — l’outil est partagé. L’attribution repose sur comment l’outil est utilisé, dans quelle séquence, avec quelles autres techniques, et contre quelle cible.

-----

### Annexe G — Cadres juridiques et réglementaires par juridiction

Cette annexe consolide les cadres juridiques, institutions, et qualifications mentionnés dans le cours. L’objectif est d’offrir un référentiel pour l’analyste confronté à un incident APT et devant naviguer dans les obligations et les points de contact pertinents.

#### G.1 France

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

#### G.2 Union européenne

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

#### G.3 États-Unis

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

#### G.4 Royaume-Uni

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

#### G.5 Allemagne

**BSI** — Bundesamt für Sicherheit in der Informationstechnik. Agence fédérale cybersécurité, équivalent allemand de l’ANSSI. Bonn.

**BfV** — Bundesamt für Verfassungsschutz. Office fédéral de protection de la Constitution (contre-espionnage intérieur).

**BND** — Bundesnachrichtendienst. Service fédéral de renseignement extérieur.

**BKA** — Bundeskriminalamt. Office fédéral de police criminelle.

**Zentrale Stelle für Informationstechnik im Sicherheitsbereich (ZITiS)** : support technique aux services de sécurité allemands.

**KRITIS** : cadre des infrastructures critiques allemandes. Secteurs définis et obligations de notification.

#### G.6 OTAN

**Reconnaissance du cyber comme 5ème domaine d’opérations** — sommet de Varsovie, 2016.

**NATO Cyber Operations Centre (CyOC)** — créé 2018, intègre le cyber dans la planification militaire OTAN.

**CCDCOE** — Cooperative Cyber Defence Centre of Excellence, Tallinn (Estonie). Créé en 2008. Think tank OTAN sur le cyber. Pilote :

- Le **Manuel de Tallinn** (1.0 en 2013, 2.0 en 2017, 3.0 en cours) — interprétation du droit international appliqué au cyber. Non-contraignant mais référence majeure.
- L’exercice **Locked Shields** annuel — plus grand exercice de red/blue team au monde.
- Publications académiques et techniques.

**Article 5 et cyber** : reconnu applicable au cyber depuis 2014. Seuil de déclenchement délibérément non défini (ambiguïté stratégique). Jamais déclenché pour un incident cyber à date.

**NATO Communications and Information Agency (NCIA)** : bras technique cyber OTAN.

#### G.7 ONU

**GGE** — Group of Governmental Experts on Developments in the Field of Information and Telecommunications in the Context of International Security. Groupe restreint d’experts gouvernementaux. Rapports consensuels 2013 et 2015 affirmant que le droit international s’applique au cyber.

**OEWG** — Open-Ended Working Group. Créé 2018, plus inclusif (tous États membres). Rapports 2021 et 2024, plus divisifs politiquement.

**Groupes de positions structurants** :

- **Bloc occidental** : normes existantes s’appliquent, focus sur comportements responsables, multistakeholderisme.
- **Bloc Russie-Chine** : nouveau traité nécessaire, concept de « sécurité de l’information » incluant contrôle du contenu, multilatéralisme strict (États seuls).

**UN Convention on Cybercrime** — négociée sous leadership russe, adoptée en 2024. Controversée — critiques des démocraties et de la société civile sur les risques pour les droits humains, la définition large des infractions, les capacités de coopération qui pourraient servir à la répression transfrontalière.

#### G.8 Pall Mall Process

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

#### G.9 Synthèse pour l’analyste

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

### Annexe H — Ressources et formation

Cette annexe consolide les ressources essentielles pour un analyste CTI/SOC travaillant sur les APT. Sélection non exhaustive — privilégie les sources de qualité établie.

#### H.1 Rapports annuels et périodiques de référence

**Rapports annuels vendors** (tous gratuits et téléchargeables) :

- **Mandiant M-Trends** : publication annuelle depuis 2011. Synthèse des incidents IR traités par Mandiant, tendances des APT, dwell time moyen. Référence centrale.
- **CrowdStrike Global Threat Report (GTR)** : publication annuelle, synthèse des acteurs et tendances.
- **Microsoft Digital Defense Report (DDR)** : publication annuelle depuis 2020. Volume massif, vision cloud (M365, Azure).
- **Verizon Data Breach Investigations Report (DBIR)** : publication annuelle depuis 2008. Données statistiques sur les breaches, vision plus large que les APT stricts.
- **ENISA Threat Landscape** : publication annuelle ENISA, vision européenne.
- **ANSSI Panorama de la cybermenace** : publication annuelle ANSSI, perspective française.
- **NCSC Annual Review** (UK) : publication annuelle NCSC.
- **CISA Year in Review** : publication annuelle CISA.
- **Kaspersky APT Reports** : rapports trimestriels et ad hoc.
- **ESET Threat Report** : publication biannuelle, forte visibilité Europe centrale/orientale.
- **Europol IOCTA** — Internet Organised Crime Threat Assessment, publication annuelle. Focus cybercrime mais avec zones de chevauchement APT.
- **Recorded Future Annual Report** : publication annuelle.
- **Unit 42 (Palo Alto) Incident Response Report** : publication annuelle, données IR.
- **Chainalysis Crypto Crime Report** : publication annuelle, centrale pour le volet crypto/Lazarus.
- **TRM Labs / Elliptic reports** : publications régulières sur les flux illicites crypto.

**Rapports sectoriels** :

- **Dragos Year in Review** : publication annuelle Dragos, focus OT/ICS.
- **Claroty Biannual ICS Risk & Vulnerability Report**.
- **FS-ISAC** : rapports sectoriels finance.
- **H-ISAC** : rapports sectoriels santé.

**Rapports thématiques majeurs** :

- **Pegasus Project** (2021) — Forbidden Stories + 17 médias — usage NSO Pegasus.
- **Leak i-Soon analyses** (2024) — multiple vendors (SentinelOne, Sekoia, Harfang Lab).
- **ContiLeaks analyses** (2022) — multiples chercheurs indépendants.
- **Citizen Lab reports** — University of Toronto — référence internationale sur spywares et surveillance.

#### H.2 Formations certifiantes

**SANS Institute** (gold standard) :

- **FOR578 — Cyber Threat Intelligence** : formation de référence CTI. Enseignants majeurs du domaine (Rebekah Brown, Scott Roberts, Ryan Fetterman). Certification **GCTI**.
- **FOR508 — Advanced Incident Response, Threat Hunting, and Digital Forensics**. Certification **GCFA**.
- **FOR572 — Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response**. Certification **GNFA**.
- **ICS515 — ICS Active Defense and Incident Response** : formation phare OT. Enseignants Dragos (Robert M. Lee). Certification **GRID**.
- **ICS456 — Essentials for NERC Critical Infrastructure Protection** : focus réglementaire NERC CIP (US électricité).
- **FOR528 — Ransomware and Cyber Extortion for Incident Responders**.
- **FOR608 — Enterprise-Class Incident Response & Threat Hunting**.
- **SEC599 — Defeating Advanced Adversaries**.
- **SEC504 — Hacker Tools, Techniques, and Incident Handling**.

**Offensive Security** :

- **OSCP** (Offensive Security Certified Professional) : certification offensive de référence, base du pentest.
- **OSEP** (Offensive Security Experienced Penetration Tester) : niveau plus avancé.
- **OSED** (Offensive Security Exploit Developer).

**EC-Council** :

- **CEH** (Certified Ethical Hacker) — largement reconnu mais considéré comme moins rigoureux que OSCP par les praticiens.
- **CTIA** (Certified Threat Intelligence Analyst).
- **CHFI** (Computer Hacking Forensic Investigator).

**ISC2** :

- **CISSP** (Certified Information Systems Security Professional) — management sécurité.
- **CCSP** (Certified Cloud Security Professional).
- **CCFP** (Certified Cyber Forensics Professional).

**ISACA** :

- **CISM** (Certified Information Security Manager) — management.
- **CISA** (Certified Information Systems Auditor) — audit.
- **CRISC** (Certified in Risk and Information Systems Control).

**Mandiant Academy** : formations spécifiques (CTI, IR, malware analysis).

**CrowdStrike University** : formations internes et ouvertes.

**SECO Institute** (Europe) : certifications cybersécurité européennes.

**Formations françaises** :

- **CNAM** : master cybersécurité.
- **Télécom Paris / Télécom SudParis / INSA** : masters spécialisés.
- **Centrale-Supélec** : formation continue et formations initiales.
- **ESIEA, EPITA, EPITECH** : formations ingénieur avec spécialisations cyber.
- **EC-Conseil** : formations ANSSI orientées.

#### H.3 Bases de données et plateformes techniques

**MITRE — référence absolue** :

- **MITRE ATT&CK** : attack.mitre.org — framework TTP. Sections Enterprise, Mobile, ICS (OT).
- **MITRE ATT&CK Groups** : attack.mitre.org/groups/ — page par groupe avec TTP associées et alias.
- **MITRE CTI GitHub** : github.com/mitre/cti — export STIX des données ATT&CK.
- **MITRE D3FEND** : d3fend.mitre.org — contre-framework défensif aligné sur ATT&CK.
- **MITRE Engage** : cadre pour deception.
- **MITRE Shield** (remplacé par Engage) : cadre historique de defensive cyber operations.
- **CTI Blueprints** : github.com/center-for-threat-informed-defense — méthodologies.

**Malware et samples** :

- **Malpedia** : malpedia.caad.fkie.fraunhofer.de — base consolidée par Fraunhofer FKIE, mapping famille/acteur.
- **VirusTotal** : virustotal.com — Google. Intelligence sur fichiers, URLs, domaines, IPs.
- **Hybrid Analysis** : hybrid-analysis.com — sandboxing public.
- **Any.run** : any.run — sandboxing interactif.
- **Joe Sandbox** : joesandbox.com — analyse dynamique.
- **Triage** : tria.ge — Hatching (Recorded Future).
- **VX-Underground** : vx-underground.org — archives malware historiques.

**Intelligence / reconnaissance** :

- **Shodan** : shodan.io — recherche appliances exposées Internet.
- **Censys** : censys.io — concurrent de Shodan.
- **ZoomEye** : zoomeye.org — équivalent chinois.
- **FOFA, Quake** : équivalents chinois.
- **GreyNoise** : greynoise.io — caractérisation du bruit Internet vs activité ciblée.
- **AlienVault OTX** : otx.alienvault.com — partage communautaire.
- **URLhaus** : urlhaus.abuse.ch — URLs malveillantes.
- **ThreatFox** : threatfox.abuse.ch — IoC partagés.
- **Feodo Tracker** : feodotracker.abuse.ch — botnets bancaires.
- **URLScan** : urlscan.io — scan URLs.

**Threat intelligence platforms** :

- **MISP** : misp-project.org — open source, standard de partage.
- **OpenCTI** : github.com/OpenCTI-Platform — open source.
- **Anomali ThreatStream**, **ThreatConnect**, **EclecticIQ**, **Recorded Future** : commerciaux.

**Vulnerability intelligence** :

- **CISA KEV** : cisa.gov/known-exploited-vulnerabilities-catalog.
- **NVD** : nvd.nist.gov — National Vulnerability Database US.
- **MITRE CVE** : cve.mitre.org.
- **First EPSS** : first.org/epss — scoring prédictif d’exploitation.
- **Patch Tuesday trackers** (divers) : consolidation des patches Microsoft.

#### H.4 Blogs, newsletters, podcasts

**Blogs vendors CTI** (publications techniques de haute qualité) :

- **Mandiant blog** : cloud.google.com/security/resources/threat-intelligence.
- **CrowdStrike blog** : crowdstrike.com/blog.
- **Microsoft Threat Intelligence blog** : microsoft.com/security/blog.
- **Kaspersky Securelist** : securelist.com.
- **ESET WeLiveSecurity** : welivesecurity.com.
- **Unit 42 (Palo Alto)** : unit42.paloaltonetworks.com.
- **Trend Micro Research** : trendmicro.com/research.
- **Proofpoint Threat Insight** : proofpoint.com/us/blog.
- **Check Point Research** : research.checkpoint.com.
- **Sekoia blog** : blog.sekoia.io.
- **Harfang Lab blog** : harfanglab.io/insidethelab.
- **Dragos blog** : dragos.com/blog (OT/ICS).
- **Claroty Team82** : claroty.com/team82/research (OT).
- **Recorded Future Insikt Group** : recordedfuture.com/research.

**Blogs indépendants et communautaires** :

- **The DFIR Report** : thedfirreport.com — analyses d’intrusions détaillées, gratuit et de qualité exceptionnelle.
- **Krebs on Security** : krebsonsecurity.com — Brian Krebs, journalisme cyber.
- **SANS ISC (Internet Storm Center)** : isc.sans.edu — diary quotidien.
- **Bleeping Computer** : bleepingcomputer.com — actualité cyber accessible.
- **The Record** (Recorded Future) : therecord.media.
- **CyberScoop** : cyberscoop.com.
- **Ars Technica — Security** : arstechnica.com/information-technology.
- **The Hacker News** : thehackernews.com.

**Blogs techniques profonds** :

- **Harel Fortinet** / **Securelist** : analyses malware approfondies.
- **Didier Stevens** : didierstevens.com — outils et analyses malware.
- **Objective-See** (Patrick Wardle) : objective-see.org — sécurité macOS.
- **SpecterOps** : posts.specterops.io — red team/AD.
- **Google Project Zero** : googleprojectzero.blogspot.com — recherche vulnérabilités.

**Citizen Lab** : citizenlab.ca — référence sur spywares, surveillance, droits humains numériques.

**Newsletters** :

- **Risky.Biz** (Patrick Gray) : riskybiz.media — podcast et newsletter, référence industrie.
- **The CyberWire** : thecyberwire.com — newsletter quotidienne.
- **This Week in Security** : Matt Tait (@pwnallthethings).
- **TLDR Sec** (Clint Gibler) : tldrsec.com.
- **Return on Security** (Mike Privette) : returnonsecurity.com.

**Podcasts** :

- **Risky.Biz** — Patrick Gray.
- **Darknet Diaries** (Jack Rhysider) : darknetdiaries.com — histoires cyber racontées.
- **SANS Internet Stormcast**.
- **Cyber Weekly**.
- **Hacking Humans** (CyberWire).
- **NoLimitSecu** (français).
- **Le Comptoir Sécu** (français).

#### H.5 Conférences et événements

**Internationales** :

- **Black Hat USA** (Las Vegas, août) — conférence industrielle majeure, briefings techniques.
- **DEF CON** (Las Vegas, août) — conférence hacker historique.
- **RSA Conference** (San Francisco, avril-mai) — plus grande conférence cyber mondiale.
- **Black Hat Europe** (Londres, décembre).
- **Black Hat Asia** (Singapour).
- **FIRST Annual Conference** : conférence du Forum of Incident Response and Security Teams.
- **Virus Bulletin (VB)** : conférence AV/CTI.
- **CyCon** : conférence CCDCOE OTAN, Tallinn. Focus cyber et droit international.
- **REcon** (Montréal) : reverse engineering.
- **ShmooCon** (Washington).
- **Kaspersky SAS (Security Analyst Summit)** : conférence CTI annuelle.

**Européennes / francophones** :

- **SSTIC** (Rennes, juin) : Symposium sur la sécurité des technologies de l’information et des communications. Conférence francophone de référence.
- **FIC** (Lille, puis Marseille, janvier) : Forum International de la Cybersécurité. Dimension institutionnelle forte.
- **Botconf** (Strasbourg/autres, annuel) : focus botnets et malware.
- **NoLimitSecu Days**.
- **ECRIME** (Amsterdam).
- **Troopers** (Heidelberg, Allemagne).
- **hack.lu** (Luxembourg).
- **NDSS** (Network and Distributed System Security) : conférence académique USENIX.
- **USENIX Security** : conférence académique.
- **Hardwear.io** (La Haye) : hardware security.

**Conférences OT spécialisées** :

- **S4** (Miami, janvier) : conférence OT sécurité la plus prestigieuse.
- **SANS ICS Summit** (Orlando).
- **Dragos ICS Cybersecurity Conference**.

**Conférences étatiques / agences** :

- **CSS** (Cyber Security Summit) : événements ANSSI.
- **NCSC One** (UK).
- **RSA Conference Government Track** (US).

#### H.6 OSINT sur APT — sources à cultiver

**Comptes Twitter/X / Mastodon à suivre** (sélection) :

Vendors et chercheurs réputés :

- @TrailofBits, @juanandres_gs, @cyb3rops (Florian Roth), @malwrhunterteam, @vxunderground, @MalwareTechBlog, @bryankb, @wdormann, @gossithedog, @taosecurity (Richard Bejtlich), @jeffreycarr, @MalwareJake, @2sec4u.

Agences et officiels :

- @CISAgov, @NCSC, @ANSSI_FR, @BSI_Bund, @ENISA_EU, @FBI_CYBER, @ODNIgov, @CERT_UA, @WarOnTheRocks.

Journalistes :

- @briankrebs, @lorenzofb, @binaryflash (Kim Zetter), @patrickwardle, @bing_chris, @josephmenn.

Acteurs spécialisés :

- @DragosInc, @mandiant, @CrowdStrike, @Kaspersky, @ESETresearch, @Unit42_Intel, @MsftSecIntel, @citizenlab, @Telecomix, @Recorded_Future.

**Listes et agrégateurs** :

- **Twitter/X lists** sur CTI, APT, threat intelligence par des curateurs reconnus.
- **Mastodon instances** : infosec.exchange (plus focus technique), social.cyber.gay.
- **LinkedIn** : pour les publications plus institutionnelles et les annonces corporatives.

**Plateformes de partage structuré** :

- **CTI league** (formée en 2020) : volontaires COVID, a montré la puissance du partage.
- **InfoSec Handlers Diary** (SANS ISC).
- **Exploit-db.com** : exploits publiés.
- **0day.today** : marketplace (usage à considérer avec prudence).

**Rapports gouvernementaux publics** :

- **US CISA advisories** : cisa.gov/news-events/cybersecurity-advisories.
- **NSA Cybersecurity Advisories** : nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance.
- **UK NCSC advisories** : ncsc.gov.uk/section/advice-guidance/all-topics.
- **CERT-FR** : cert.ssi.gouv.fr.
- **BSI** : bsi.bund.de.
- **CCCS Canada** : cyber.gc.ca.
- **ACSC Australia** : cyber.gov.au.

**Ressources académiques** :

- **arXiv cs.CR** : publications académiques en sécurité.
- **Citizen Lab publications** : citizenlab.ca/category/research/.
- **Atlantic Council Cyber Statecraft Initiative**.
- **CSIS Cyber Policy** : csis.org/programs/strategic-technologies-program.
- **RAND Cyber Policy** : rand.org.

#### H.7 Livres de référence

**Cyber géopolitique et acteurs** :

- *Sandworm* — Andy Greenberg. Référence sur Sandworm/GRU, NotPetya, Ukraine.
- *Dark Territory: The Secret History of Cyber War* — Fred Kaplan.
- *Confront and Conceal* — David Sanger. Stuxnet et Iran.
- *The Perfect Weapon* — David Sanger.
- *This Is How They Tell Me the World Ends* — Nicole Perlroth. Marché 0-day.
- *Countdown to Zero Day* — Kim Zetter. Stuxnet.
- *Cult of the Dead Cow* — Joseph Menn. Histoire du hacking et des enjeux politiques.
- *Active Measures* — Thomas Rid. Histoire de la désinformation.

**CTI et analyse** :

- *Intelligence-Driven Incident Response* — Scott Roberts & Rebekah Brown.
- *The Cuckoo’s Egg* — Cliff Stoll. Premier cas d’APT documenté (1989), encore pertinent.
- *Practical Threat Intelligence and Data-Driven Threat Hunting* — Valentina Palacín.
- *Threat Intelligence and Me* — Robert M. Lee (accessible).
- *The Threat Intelligence Handbook* — Recorded Future.

**Analyse et méthodes** :

- *Psychology of Intelligence Analysis* — Richards Heuer (CIA, ancien mais classique).
- *Structured Analytic Techniques for Intelligence Analysis* — Richards Heuer & Randolph Pherson.

**Technique** :

- *Practical Malware Analysis* — Michael Sikorski & Andrew Honig.
- *The Practice of Network Security Monitoring* — Richard Bejtlich.
- *Applied Incident Response* — Steve Anson.
- *Blue Team Handbook* — Don Murdoch.
- *Red Team Field Manual* — Ben Clark.

**OT / ICS** :

- *Industrial Cybersecurity* — Pascal Ackerman.
- *Hacking Exposed: Industrial Control Systems* — Clint Bodungen et al.

**Ouvrages français** :

- *La cyberdéfense : politique de l’espace numérique* — Stéphane Taillat, Amaël Cattaruzza, Didier Danet.
- *Cyberattaque et cyberdéfense* — Daniel Ventre.
- *La guerre cognitive* — François-Bernard Huyghe.

-----


## CLÔTURE DU COURS

### Ce que ce cours a cherché à apprendre

Ce cours AU CŒUR DES APT s’est donné pour mission de **faire comprendre les acteurs cyber étatiques** — qui ils sont, comment ils opèrent, quelles sont leurs doctrines, leurs ambitions, leurs contraintes. Cette compréhension n’est pas académique : elle est **opérationnellement indispensable**.

Face à une intrusion sophistiquée, un analyste sans connaissance des acteurs peut détecter une compromission mais ne peut pas l’interpréter correctement. Il manipule des IoC sans comprendre les intentions. Il alerte sans calibrer l’urgence. Il répond sans anticiper les mouvements suivants de l’adversaire.

Un analyste qui connaît les acteurs voit différemment. Un beaconing HTTPS sur un poste OT dans un opérateur énergétique européen, pendant un conflit ukrainien actif, n’est pas un artefact technique isolé — c’est le signal possible d’un pré-positionnement stratégique dont les implications s’étendent de la détection technique à la coordination diplomatique internationale. Le cours a cherché à permettre cette lecture.

### Les quatre idées centrales

Quatre idées traversent le cours et méritent d’être retenues.

**Première idée — les APT sont des instruments étatiques intégrés**. Elles ne sont pas des phénomènes cyber isolés mais des extensions des appareils de renseignement, des doctrines de sécurité nationale, des stratégies géopolitiques. Une opération Sandworm est un acte de guerre hybride russe. Une opération APT40 est un vecteur de rattrapage technologique chinois. Un vol Lazarus est un financement du programme nucléaire nord-coréen. Comprendre le cyber exige de comprendre les États qui le conduisent.

**Deuxième idée — l’attribution est une discipline**. Elle ne se contente pas de signatures techniques. Elle croise TTP, infrastructure, victimologie, timing géopolitique, erreurs opérationnelles, et parfois renseignement humain. Elle formalise les niveaux de confiance. Elle teste les hypothèses concurrentes (ACH). Elle accepte l’incertitude et la documente. Elle distingue l’attribution technique (intrusion set), opérationnelle (service), et stratégique (État et intention). Le cours a proposé cette grille parce qu’elle protège contre les erreurs — biais de confirmation, effets de signature, faux drapeaux.

**Troisième idée — le pré-positionnement est la menace structurelle qui vient**. Volt Typhoon a révélé qu’un acteur étatique peut maintenir un accès silencieux des années dans des infrastructures critiques, prêt à être activé à un moment politique choisi. Ce paradigme est ultra-furtif, difficile à détecter, et potentiellement catastrophique en cas d’escalade. Il demande aux défenseurs européens — opérateurs, agences, CERT — de repenser leurs postures défensives. Investir dans la visibilité OT, le monitoring identity cloud, le threat hunting proactif, la coopération internationale. Les années qui viennent nous diront si cette adaptation a été suffisante.

**Quatrième idée — la défense APT-ready est un investissement continu, pas un état atteint**. Les acteurs étatiques s’adaptent en permanence. Aucune organisation n’est totalement invulnérable. L’objectif réaliste est de réduire le dwell time, améliorer la résilience, écourter la récupération, partager l’information avec l’écosystème. La sécurité des infrastructures critiques est un bien commun — un incident qui frappe un opérateur menace tous les autres. La coopération public-privé-international, modèle ukrainien éprouvé sous feu, est la condition de l’efficacité.

### Pour aller plus loin

La bibliothèque dont ce cours fait partie couvre plusieurs dimensions complémentaires. L’OSINT Mastery apprend les techniques de collecte et d’analyse qui alimentent la CTI. Les cours SOC et Incident Response apprennent la conduite opérationnelle de la détection et de la réponse. Le cours Forensics apprend l’investigation technique approfondie. Les cours OT Security et Cloud Security approfondissent les domaines spécialisés. Les cours Écosystèmes cybercriminels et Dark Web documentent la zone grise criminelle adjacente aux APT.

Au-delà de la bibliothèque, l’apprentissage des APT est **un métier de veille permanente**. Les acteurs évoluent. Les TTP se renouvellent. Les outils changent. Les contextes géopolitiques se transforment. Maintenir la compétence exige de lire les rapports annuels, suivre les advisories, pratiquer les exercices, échanger avec la communauté. Le corpus que ce cours a présenté n’est qu’un point de départ.

### Le mot de la fin

Les APT sont des adversaires sérieux. Ils sont bien dotés, patients, sophistiqués, et alignés sur les enjeux stratégiques les plus lourds de notre temps — rivalités géopolitiques, contrôle technologique, dissuasion, surveillance, financement d’armements. Face à eux, la défense est exigeante mais pas hors de portée.

L’histoire du cyber contemporain est celle d’une **course permanente** entre attaquants et défenseurs. Les défenseurs ne gagnent pas définitivement, mais ils peuvent limiter les impacts, raccourcir les compromissions, renforcer la résilience. La différence se fait par la préparation — préparation technique, organisationnelle, humaine, collective. Ce cours a tenté d’y contribuer.

Bonne route.
