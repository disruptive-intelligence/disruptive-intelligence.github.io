---
title: 'Chapitre 6 — Russie : les groupes APT en détail'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie II — Russie
  - index.md
---

Ce chapitre approfondit le profil des six groupes APT russes les plus importants. Chaque profil couvre : mission, TTP signature, OPSEC, campagnes emblématiques, évolution récente.

## 6.1 APT29 / Cozy Bear / Midnight Blizzard (SVR)

**Mission** : espionnage stratégique de haut niveau — gouvernements occidentaux, diplomatie, grandes entreprises technologiques, think tanks, ONG actives sur la Russie, recherche médicale (ciblage documenté sur les développeurs de vaccins COVID en 2020).

**TTP signature** :

- **Accès initial par compromission supply chain** (SolarWinds 2020 — cas d’école), par **phishing OAuth ciblé** (demandes d’autorisation d’applications malveillantes imitant Microsoft Teams ou des applications Azure légitimes), par **password spray** sur Azure AD (tenants avec faibles politiques), et occasionnellement par **spear-phishing classique** avec macros.
- **Abus Azure AD / Entra ID / M365** : vol de tokens SAML (GoldenSAML), manipulation d’applications OAuth, pivotement entre tenants via des relations de partage, abus de permissions Graph API pour lire les emails.
- **Malware custom sophistiqué** : SUNBURST (backdoor injectée dans les builds Orion de SolarWinds), TEARDROP (loader), GoldMax / SUNSHUTTLE (backdoor Go cross-platform), GoldFinder (HTTP tracer pour reconnaissance d’infrastructure), SIBOT (VBScript), FoggyWeb (backdoor ADFS post-exploitation), MagicWeb (malware ADFS plus récent 2022).
- **C2 via services légitimes** : Azure, AWS, Dropbox, Twitter (pour des canaux secondaires), abus de canaux Slack/Teams dans certaines campagnes récentes.
- **Minimal footprint** : peu de fichiers déposés, exécution en mémoire privilégiée, nettoyage systématique des traces.

**OPSEC** : parmi la plus élevée du monde APT. Infrastructure compartimentée (chaque cible a sa propre chaîne d’infrastructure C2), opérateurs disciplinés (pas d’erreurs d’horaires documentées), adaptation rapide aux mitigations (changement de techniques dès qu’une campagne est publiée).

**Campagnes majeures** :

- **SolarWinds / SUNBURST** (2020-2021) : ~18 000 organisations infectées via la mise à jour trojanisée d’Orion, ~100 cibles de haute valeur activement exploitées (Trésor US, Département du Commerce, Département de la Sécurité Intérieure, Microsoft, FireEye/Mandiant, et autres). Détaillé au Ch.29.
- **Ciblage des développeurs de vaccins COVID** (2020) : attribué par NCSC, NSA, CSE/Canada — APT29 cible les entreprises pharmaceutiques britanniques, américaines et canadiennes développant les vaccins COVID-19 pour exfiltrer la recherche.
- **Microsoft corporate breach** (novembre 2023 - janvier 2024) : APT29 compromet un tenant Azure AD test de Microsoft via password spray, pivote vers une application OAuth permissive, et accède aux emails de dirigeants Microsoft (y compris de la direction exécutive). Microsoft a publiquement reconnu la compromission. Des entités tierces (Hewlett Packard Enterprise notamment) ont subséquemment confirmé des compromissions liées.
- **Campagnes diplomatiques continues 2022-2025** : spear-phishing OAuth contre les ministères des affaires étrangères européens, les ambassades, les missions diplomatiques. Volume élevé, taux de compromission non-public.
- **MagicWeb** (2022) : backdoor ADFS post-exploitation identifiée par Microsoft. Le malware modifie la gestion des certificats ADFS pour permettre à l’attaquant de se faire passer pour n’importe quel utilisateur.

**Évolution récente (2024-2026)** : après SolarWinds, APT29 a évolué vers un usage encore plus prononcé des abus cloud/identity (tokens, OAuth, Primary Refresh Tokens Azure AD). La dépendance aux infrastructures cloud légitimes (Microsoft, AWS, Google) rend la détection plus difficile. Les campagnes de 2024-2025 montrent un ciblage encore plus sophistiqué des ministères européens, avec des emails personnalisés qui passent les filtres anti-phishing majoritairement par leur contexte plausible.

## 6.2 APT28 / Fancy Bear / Forest Blizzard (GRU Unit 26165)

**Mission** : espionnage militaire et politique + opérations d’influence intégrées. Cibles : ministères de la défense, organisations internationales (OTAN, UE, OSCE), organisations anti-dopage (WADA), partis politiques (DNC 2016), médias, think tanks de défense.

**TTP signature** :

- **Spear-phishing** : macros VBA dans des documents Office (pendant longtemps la technique privilégiée), faux portails de login OAuth ou de services corporate (Microsoft OWA, VPN).
- **Exploitation de vulnérabilités** : APT28 est l’un des acteurs les plus actifs à exploiter rapidement les vulnérabilités Outlook et Exchange. **CVE-2023-23397** (Outlook, vulnérabilité NTLM hash leak via invitation de calendrier malveillante) a été massivement exploitée par APT28 en 2022-2023 avant sa découverte publique.
- **Credential harvesting** : fausses pages de login imitant les services corporate, password spraying massif sur Azure AD.
- **Outils custom** : **X-Tunnel** (proxy interne), **XAgent** (backdoor modulaire Windows/macOS/iOS/Android), **Zebrocy** (backdoor multi-langages — Delphi, Go, Python, C++ — tradecraft inhabituel qui complique l’analyse), **CredoMap** (stealer de credentials), **Cannon** (backdoor), **Seduploader** (implant).
- **Mimikatz** pour le credential dumping.

**OPSEC** : moyen à élevé — nettement moins furtif que le SVR/APT29. APT28 assume un niveau de bruit plus élevé pour l’efficacité opérationnelle. Plusieurs campagnes ont été identifiées par des erreurs d’OPSEC (réutilisation d’infrastructure, horaires compatibles Moscou, artefacts langue russe).

**Campagnes majeures** :

- **DNC hack** (2016) : compromission du Comité National Démocrate américain. Les données (emails, documents internes) sont publiées via DCLeaks et WikiLeaks dans une opération hack-and-leak coordonnée pour impacter l’élection présidentielle. Attribution par FBI, DHS, Office of the Director of National Intelligence (janvier 2017). Indictment DOJ en 2018 qui inculpe nommément 12 officiers du GRU Unit 26165.
- **WADA breach** (2016) : vol et publication de données médicales d’athlètes olympiques, en représailles à l’exclusion d’athlètes russes pour dopage systémique.
- **Bundestag breach** (2015) : compromission du réseau informatique du parlement allemand, accès maintenu plusieurs semaines, exfiltration massive de documents. La réponse allemande a inclus une reconstruction complète du réseau.
- **TV5Monde** (2015) : bien que revendiquée par un groupe présenté comme « CyberCaliphate » affilié à l’État islamique, l’attribution technique a pointé vers APT28 (false flag — tradecraft similaire, infrastructure compromise).
- **Exploitation massive CVE-2023-23397** (2022-2023) : APT28 a exploité cette vulnérabilité Outlook contre des dizaines d’organisations européennes (gouvernements, défense, énergie, transport) pendant près d’un an avant découverte publique.
- **Campagnes 2023-2025** : ciblage continu des organisations ukrainiennes, alliés de l’OTAN, ministères européens. Utilisation accrue de services de stockage cloud (MEGA, pCloud) pour l’exfiltration.

**Évolution récente** : APT28 a maintenu un haut niveau d’activité post-2022. Utilisation croissante d’**infostealers** comme vecteur d’accès initial (achat de logs sur les marchés dark web pour obtenir des credentials initiaux, plutôt que phishing). Campagne **MooBot** (botnet de routeurs Ubiquiti compromis, utilisé comme infrastructure de proxy) démantelée par le FBI en février 2024 — modèle similaire à Volt Typhoon mais côté russe.

## 6.3 Sandworm / Seashell Blizzard (GRU Unit 74455)

**Mission** : opérations destructives et sabotage — le bras armé du cyber russe. Cibles : infrastructures critiques (énergie principalement, télécoms, secteur financier), gouvernements, sous-traitants militaires. Ciblage privilégié : Ukraine, pays OTAN de la première ligne (Pologne, États baltes), occasionnellement infrastructures mondiales (NotPetya a touché le monde entier via la supply chain M.E.Doc).

**TTP signature** :

- **Wipers** : Sandworm est le groupe au monde qui a déployé le plus de wipers différents. **NotPetya / ExPetr** (2017, wiper masqué en ransomware, propagation via supply chain M.E.Doc + EternalBlue), **CaddyWiper** (2022, wiper destructif Ukraine), **HermeticWiper / FoxBlade** (février 2022, veille de l’invasion), **IsaacWiper** (février 2022), **AcidRain** (février 2022, contre les terminaux satellites Viasat KA-SAT — impact collatéral sur les éoliennes allemandes qui utilisaient le même opérateur). Plusieurs variants récents non publiquement catalogués.
- **Attaques OT/ICS** : **Industroyer / CrashOverride** (2016, premier malware ciblant les protocoles industriels IEC 60870-5-104 et IEC 61850 pour provoquer un blackout), **Industroyer2** (2022, tentative déjouée par CERT-UA et ESET), **CosmicEnergy** (2023, découvert par Mandiant — malware OT conçu pour attaquer les systèmes de protection IEC 60870-5-104, capacités similaires à Industroyer mais avec des différences techniques suggérant une nouvelle branche de développement). Détaillé au Ch.21.
- **Supply chain** : compromission de M.E.Doc (logiciel comptable ukrainien utilisé par des milliers d’organisations) pour la propagation initiale de NotPetya — paradigme supply chain.
- **Exploitation d’edge devices et routeurs** : **Cyclops Blink** (botnet 2022 sur routeurs ASUS et WatchGuard — démantelé par le FBI).
- **Mouvement latéral classique** : Mimikatz, PsExec, RDP.
- **False flags sophistiqués** : **Olympic Destroyer** (2018, Jeux Olympiques de Pyeongchang) incluait des fragments de code Lazarus plantés délibérément pour brouiller l’attribution. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et confirmé l’attribution Sandworm.

**Particularité historique** : Sandworm est le **seul groupe APT dans le monde à avoir causé publiquement documenté des pannes d’électricité** via cyberattaque. Ukraine 2015 (BlackEnergy/KillDisk, 230 000 foyers, 6 heures) et 2016 (Industroyer, Kiev, 1 heure). Ces événements sont les seuls cas avérés d’impact physique étendu d’une cyberattaque sur un système de distribution d’énergie.

**OPSEC** : variable. Sandworm assume un niveau de bruit élevé pour ses opérations destructives (l’impact est l’objectif, la furtivité post-impact n’est plus nécessaire). Mais les phases de reconnaissance et de déploiement sont menées avec un OPSEC sérieux. Les attributions publiques ont été facilitées par des artefacts (strings, infrastructure) qui suggèrent une discipline OPSEC moindre que celle du SVR.

**Campagnes majeures** :

- **Ukraine 2015-2016** : BlackEnergy et Industroyer (Ch.21).
- **NotPetya** (juin 2017) : déployé initialement via M.E.Doc en Ukraine, propagation mondiale en heures via EternalBlue et credentials Windows. Dommages mondiaux estimés à 10+ milliards de dollars (Maersk, Merck, FedEx/TNT Express, Saint-Gobain, etc.). Attribution publique par CIA (juin 2017), UK NCSC et DoD (février 2018). Reconnaissance formelle comme « la cyberattaque la plus destructrice de l’histoire » par les États-Unis.
- **Olympic Destroyer** (2018) : ciblage des Jeux Olympiques d’hiver de Pyeongchang, en représailles à l’exclusion de la délégation russe pour dopage. Plusieurs composants techniques des JO compromis (site web, système Wi-Fi du stade olympique, systèmes de télévision). False flags multiples (code Lazarus, infrastructure iranienne).
- **Campagne Ukraine 2022-présent** : série continue de wipers, tentatives sur les infrastructures critiques (Industroyer2 déjouée), ciblage des télécoms et des médias, opérations OT sur les réseaux électriques ukrainiens coordonnées avec des frappes militaires.
- **Viasat KA-SAT (février 2022)** : attaque via **AcidRain** contre les terminaux satellite du fournisseur Viasat, timing synchronisé avec l’invasion. Impact principal : communications militaires ukrainiennes. Impact collatéral notable : 5 800 éoliennes allemandes utilisant le même service de connectivité satellite, inopérables pendant plusieurs semaines. Attribution publique par UE, UK, US (mai 2022).

**Évolution récente (2024-2026)** : Sandworm reste actif en Ukraine et étend son ciblage aux alliés. CosmicEnergy (2023) révèle une continuité de R&D sur les malwares OT. Des rapports Mandiant et Microsoft de 2024 suggèrent une professionnalisation croissante et un élargissement géographique (ciblage documenté de l’Europe de l’Ouest, y compris la France et l’Allemagne).

## 6.4 GRU Unit 29155

**Identification publique** : advisory conjoint NSA/FBI/CISA + partenaires internationaux (UK, Pologne, Estonie, Lettonie, Lituanie, Tchéquie, Allemagne, Ukraine, Canada, Australie) en septembre 2024.

**Mission** : opérations déstabilisatrices cyber-physiques au soutien d’objectifs stratégiques plus larges. Unit 29155 était historiquement connue pour des opérations clandestines non-cyber (sabotages physiques, empoisonnements — Salisbury 2018 contre les Skripal, impliquée), mais l’advisory 2024 a confirmé son extension au cyber.

**TTP signature** (telles que documentées par l’advisory) :

- **Accès initial** : exploitation de vulnérabilités publiques (VPN, passerelles web), phishing, bruteforce.
- **Malware custom** : **WhisperGate** (wiper déployé contre l’Ukraine en janvier 2022, attribué initialement à Sandworm puis réattribué à Unit 29155 après l’advisory).
- **Outils communs** : Impacket, Mimikatz, PsExec — tradecraft partagé avec le reste de l’écosystème GRU.
- **Ciblage OT** : l’advisory mentionne des tentatives d’attaques contre des systèmes OT européens, sans détails publics précis.

**Distinction avec Sandworm** : Sandworm (Unit 74455) est une unité cyber dédiée de longue date, avec une sophistication technique importante et des malwares signature. Unit 29155 est une unité historiquement non-cyber qui a développé des capacités cyber plus récemment — sophistication technique moindre que Sandworm, mais intégration plus directe avec des opérations clandestines non-cyber. La distinction importe pour l’analyse : attribuer une opération à l’une ou l’autre unité révèle des intentions différentes.

**Campagnes connues** :

- **WhisperGate** (janvier 2022) : wiper déployé contre des organisations ukrainiennes (gouvernement, ONG, IT) quelques semaines avant l’invasion. Masqué en ransomware (note de rançon incohérente). Impact réel : destructive, non récupérable.
- **Campagnes documentées par l’advisory 2024** : tentatives d’attaques contre des infrastructures européennes, y compris dans des pays ayant soutenu activement l’Ukraine. Détails classifiés.

**Implications opérationnelles** : pour l’analyste, la reconnaissance d’Unit 29155 comme acteur distinct signifie que le GRU dispose d’au moins deux unités capables d’opérations destructives cyber — augmentation de la surface de menace et de la capacité de redondance opérationnelle.

## 6.5 Turla / Snake / Secret Blizzard (FSB Centre 16)

**Mission** : espionnage long terme contre cibles gouvernementales et diplomatiques de haute valeur. Ciblage : ministères des affaires étrangères dans le monde, ambassades, organisations internationales, parfois entreprises de défense et think tanks stratégiques.

**TTP signature** :

- **Watering hole** : compromission de sites web fréquentés par les cibles pour les infecter lors de leur visite. Sites gouvernementaux, académiques, ou institutionnels pertinents pour la cible.
- **Supply chain** : opérations de longue durée impliquant compromission d’éditeurs ou de prestataires pour atteindre les cibles finales.
- **Malware signature** — Turla développe et maintient un arsenal malware remarquable :
  - **Snake / Uroburos** : rootkit multi-plateforme (Windows, Linux, macOS) actif depuis au moins 2003. Persistence kernel, évasion sophistiquée, communications P2P entre instances. Démantelé par le FBI en mai 2023 (opération Medusa) mais les variants post-Snake continuent.
  - **Kazuar** : backdoor modulaire (.NET) utilisée pour des opérations ciblées.
  - **LightNeuron** : backdoor Exchange serveur (transport agent malveillant) — interception d’emails au niveau serveur. Actif depuis au moins 2014, découvert par ESET en 2019.
  - **Crutch** : backdoor Windows utilisée contre des cibles diplomatiques en Europe.
  - **Carbon / Cobra** : framework modulaire historique.
- **Infrastructure par satellite** : Turla est documenté pour avoir utilisé des **liaisons satellite détournées** comme canal C2 — exploitation de liaisons satellite de FAI commerciaux (clients commerciaux des FAI satellites dans des régions où la sécurité est faible) pour masquer l’origine réelle des C2. Technique documentée par Kaspersky en 2015.
- **Piggybacking sur d’autres APT** : Turla a été observé en train d’utiliser l’**infrastructure d’autres groupes APT** pour ses opérations. Le cas le plus documenté : Turla a compromis l’infrastructure d’APT34 (OilRig, Iran) et l’a utilisée pour mener ses propres opérations. Cette technique, documentée publiquement par UK NCSC et NSA en octobre 2019, est unique dans le monde APT par son niveau de sophistication opérationnelle et par l’impact qu’elle a sur l’attribution (une victime peut voir une intrusion qui semble iranienne alors qu’elle est russe).

**OPSEC** : la plus sophistiquée de l’écosystème russe, probablement parmi les plus sophistiquées du monde APT. Opérations de longue durée (certaines compromissions gouvernementales ont duré 5-10 ans). Arsenal malware constamment renouvelé. Peu d’erreurs d’OPSEC documentées.

**Campagnes majeures** :

- **Opérations contre les diplomaties européennes** (depuis au moins les années 2000) : ciblage continu des ministères des affaires étrangères, avec des compromissions parfois longues et silencieuses.
- **RUAG breach (Suisse, 2014-2016)** : la société suisse RUAG (défense, détenue par l’État) a été compromise pendant près de deux ans. Exfiltration massive de données.
- **German Federal Foreign Office** (2017-2018) : compromission du réseau du ministère allemand des affaires étrangères, accès maintenu plusieurs mois.
- **Opération Medusa** (mai 2023, côté défense) : démantèlement du malware Snake par le FBI. Le FBI a développé un outil (PERSEUS) qui exploite des fonctionnalités de Snake lui-même pour rendre le malware inopérant sur les machines infectées, sans interagir avec les systèmes au-delà. Coordination internationale (États affectés notifiés). Opération citée comme un modèle d’action offensive law enforcement contre un malware APT.

**Évolution récente (2024-2026)** : Turla a continué ses opérations avec des outils post-Snake. Un rapport Microsoft de novembre 2023 a détaillé des compromissions continues de ministères ukrainiens et européens par Secret Blizzard, utilisant des techniques post-Snake (détournements d’infrastructure d’Andromeda — un ancien crimeware — pour piggybacker sur les infections existantes). Le modèle opérationnel Turla — sophistication extrême, patience, piggybacking — reste actif.

## 6.6 Gamaredon / Aqua Blizzard (FSB Centre 18)

**Mission** : ciblage massif continu de l’Ukraine. Cibles : institutions ukrainiennes (gouvernement, défense, sécurité, énergie, médias, ONG), diaspora ukrainienne.

**TTP signature** :

- **Phishing de masse** : volume extrêmement élevé, thèmes adaptés à l’actualité ukrainienne. Documents Office avec macros VBA (technique relativement ancienne mais toujours efficace à grande échelle).
- **Templates VBA** : Gamaredon maintient une bibliothèque de templates macros mise à jour régulièrement. Les macros sont relativement simples techniquement mais produites en volume.
- **Scripts VBS et PowerShell** : petits scripts de téléchargement et d’exécution, souvent peu obfusqués.
- **Infrastructure Telegram pour C2** : Gamaredon est l’un des rares acteurs étatiques à utiliser massivement Telegram comme canal de C2. Les implants récupèrent leurs instructions depuis des canaux Telegram contrôlés. Technique inhabituelle pour un acteur étatique, plus proche d’un modèle cybercriminel — mais Gamaredon assume un profil opérationnel différent des autres APT russes.
- **Persistence agressive** : Gamaredon réinfecte rapidement après éradication. Les victimes ukrainiennes rapportent des cycles infection/détection/éradication/réinfection qui se répètent en jours ou semaines.
- **Malwares signature** : **Pterodo** (famille de backdoors légères), **Pteranodon**, **GammaLoad** — moins sophistiqués que les outils SVR ou Sandworm, mais produits et renouvelés en volume.

**Particularité** : Gamaredon est le « marteau » là où Turla est le « scalpel ». Sophistication technique modeste, mais volume massif, persistance, et impact cumulé important. Le CERT-UA classe Gamaredon comme la menace cyber la plus continue contre l’Ukraine — pas la plus dangereuse individuellement, mais la plus omniprésente.

**OPSEC** : faible à moyenne. Pas d’effort majeur pour cacher l’origine — Gamaredon assume son rôle de « bruit de fond » plutôt que d’opération clandestine sophistiquée. Des artefacts linguistiques russes, des patterns d’horaires Moscou, et des réutilisations d’infrastructure sont fréquents.

**Évolution post-invasion** : volume massivement augmenté depuis février 2022. Gamaredon est l’acteur qui génère le plus grand volume de cyberactivité hostile contre l’Ukraine au quotidien. Adaptations techniques marginales (nouveaux thèmes de phishing, quelques variants de malware), mais continuité générale du modèle opérationnel.

## 6.7 Dragonfly / Energetic Bear / Berserk Bear

**Attribution** : attribué à la Russie avec haute confiance, rattachement spécifique au FSB Centre 16 (selon des analyses US) ou à une entité distincte — la clarté d’attribution inter-services russes est moins nette que pour APT28/APT29.

**Mission** : ciblage énergie historique. Reconnaissance et pré-positionnement dans le secteur énergie (électricité, pétrole, gaz, nucléaire) aux US et en Europe. Pas d’action destructive publiquement documentée, mais patterns cohérents avec une préparation de capacités.

**TTP signature** :

- Watering hole sur des sites de publications industrielles fréquentés par les ingénieurs énergie.
- Compromission supply chain via des éditeurs de logiciels industriels (compromission d’**eWON Talk2M** en 2017).
- Exploitation SMB, Mimikatz.
- Développement de connaissances opérationnelles sur les systèmes ICS des cibles (reconnaissance approfondie, pas d’action destructive).

**Campagnes majeures** :

- **Opérations énergie US 2017-2018** : advisory conjoint US-CERT/FBI en mars 2018 détaille une campagne russe de pré-positionnement dans le secteur énergie US, avec des accès confirmés dans plusieurs organisations. Pas de destructive action.
- **Cibles énergie européenne** : ciblage documenté de sociétés énergie britanniques, allemandes, italiennes (2016-2020).

**Évolution récente** : activité Dragonfly moins documentée publiquement depuis 2020, mais le ciblage énergie par la Russie s’est poursuivi (notamment via Sandworm). Certains analystes considèrent que Dragonfly a été réorganisé ou fusionné dans d’autres structures cyber russes post-2022.

## 6.8 Évolution de l’écosystème russe post-invasion ukrainienne

Post-février 2022, plusieurs évolutions structurantes :

**Intensification opérationnelle** : volume d’attaques historiquement élevé. L’Ukraine est l’environnement de confrontation cyber le plus intense au monde. Les groupes russes sont déployés à plein régime.

**Émergence d’Unit 29155** : publiquement documentée en 2024, suggérant que l’appareil cyber GRU a été élargi ou réorganisé pour accroître les capacités destructives.

**Pression économique sur le cybercrime russophone** : sanctions, restrictions de blanchiment, pression sur les cryptomonnaies ont fragilisé l’écosystème. Certains groupes se sont reconstitués, d’autres ont migré vers d’autres juridictions.

**Professionnalisation continue** : le GRU Units 26165 et 74455 ont adapté leurs TTP, développé de nouveaux malwares (CosmicEnergy, variants de wipers), et sophistiqué leur ciblage. APT29 a renforcé son tradecraft cloud/identity.

**Visibilité accrue côté défense** : la coopération entre les services occidentaux et l’Ukraine (notamment via Microsoft Threat Intelligence, Mandiant, ESET) a produit un volume de documentation sans précédent sur les APT russes. Ce qui permet aux défenseurs occidentaux d’anticiper les tactiques.

L’équilibre offensif/défensif en cyber russe 2025-2026 est caractérisé par un écosystème russe plus actif que jamais, mais face à des défenseurs occidentaux mieux préparés et mieux informés qu’auparavant.

-----
