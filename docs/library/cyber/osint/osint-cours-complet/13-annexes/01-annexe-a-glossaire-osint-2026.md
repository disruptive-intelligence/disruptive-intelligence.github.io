---
title: ANNEXE A — Glossaire OSINT 2026
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - Annexes
  - index.md
---

> **État des connaissances : mai 2026.** Les définitions ci-dessous sont calibrées sur l'écosystème OSINT à cette date. Outils, doctrines, cadres légaux et plateformes évoluent rapidement. Vérifier la documentation officielle des outils mentionnés avant tout usage opérationnel critique.

Glossaire des termes essentiels mobilisés dans le cours. Sélection volontairement large : termes méthodologiques, outils, doctrines, cadres juridiques, concepts techniques.

**ACH** — Analysis of Competing Hypotheses. Méthode d'analyse structurée développée par Richards Heuer (CIA, 1999, « Psychology of Intelligence Analysis »). Recense les hypothèses possibles, examine chaque évidence contre chacune, retient l'hypothèse la moins infirmée. Ch.79.

**Admiralty (cotation)** — Grille de cotation des sources et informations héritée du renseignement militaire britannique. Deux dimensions : A-F (fiabilité de la source) et 1-6 (crédibilité de l'information). Standard NATO. Ch.84.

**AdES** — Advanced Electronic Signatures. Signature électronique reconnue eIDAS. Variantes : PAdES (PDF), CAdES (ensemble), XAdES (XML). Niveaux : B (base), T (timestamp), LT (long terme), LTA (avec ré-horodatage). Ch.90.

**ADS-B** — Automatic Dependent Surveillance-Broadcast. Système d'identification aérienne. Émet position, vitesse, altitude, identité. Sources publiques : Flightradar24, ADS-B Exchange. Ch.52.

**Adverse media** — Recherche de mentions négatives dans la presse, blogs, sources publiques sur une cible. Composante systématique de la due diligence moderne. Ch.38.

**Agent autonome / agentic AI** — LLM équipé d'outils (web search, code, APIs) qui peut planifier et exécuter des tâches complexes en autonomie partielle. Maturation 2024-2026. Ch.67.

**AI Act (Règlement UE 2024/1689)** — Règlement européen sur l'intelligence artificielle, entré en vigueur le 1er août 2024. Classification par risque. Restrictions sur reconnaissance biométrique en temps réel. Obligations de transparence pour contenus IA. Ch.7.

**AIS** — Automatic Identification System. Système d'identification maritime obligatoire pour les navires > 300 tonneaux internationaux. Sources publiques : MarineTraffic, VesselFinder. Ch.52.

**Aleph (OCCRP)** — Plateforme journalistique d'agrégation OSINT corporate / leaks / sanctions / documents publics. aleph.occrp.org. Ch.37.

**AMLD** — Anti-Money Laundering Directive. Directives européennes sur lutte contre le blanchiment : 5e AMLD (2018), 6e AMLD (2023), refonte AMLA-AMLR (2024). Ch.7, 38.

**Amass** — Outil open source OWASP pour découverte de sous-domaines en passif et actif. Référence. Ch.40.

**Archive.today** — Service d'archivage web alternatif au Wayback Machine, particulièrement utile pour préserver les contenus sociaux et les pages soumises à suppression rapide. Ch.20.

**ASM** — Attack Surface Management. Discipline de gestion continue de la surface d'attaque (domaines, IPs, services exposés, fuites). Outils : Bitsight, SecurityScorecard, RiskIQ, Censys Continuous. Ch.41, 75.

**ASN** — Autonomous System Number. Identifiant d'organisation propriétaire d'un bloc IP. Sources : bgp.he.net, bgp.tools, RIPEstat. Ch.40.

**Avatar mature** — Compte d'investigation construit progressivement (semaines / mois) avec contenu cohérent pour échapper à la détection comme bot ou compte d'investigation. Ch.11.

**Bellingcat** — Collectif d'investigation OSINT fondé en 2014 par Eliot Higgins. Référence méthodologique mondiale. Méthodologie ouverte et reproductible. Cas emblématiques : MH17, Skripal, Khashoggi, Ukraine.

**Biais cognitifs** — Distorsions systématiques du jugement humain. Confirmation, ancrage, disponibilité, narratif, causalité abusive, etc. Discipline anti-biais centrale en OSINT mature. Ch.80.

**BLUF** — Bottom Line Up Front. Convention de rédaction militaire qui place la conclusion en début de document. Adopté en OSINT pour notes courtes et rapports. Ch.86, 87.

**BODACC** — Bulletin Officiel des Annonces Civiles et Commerciales. Source officielle française pour annonces légales (création, modifications, ventes, procédures collectives). Ch.37.

**Brave Search** — Moteur de recherche basé sur index indépendant, orienté privacy. Alternative aux GAFAM. Ch.19.

**C2PA** — Coalition for Content Provenance and Authenticity. Standard ouvert pour métadonnées signées attestant l'origine d'un contenu numérique. Soutenu par Adobe, Microsoft, BBC, Intel, autres. Standard émergent 2024-2026. Ch.55.

**Captures Hunchly** — Outil de capture web spécialisé OSINT (hunch.ly). Enregistre intégralement chaque page consultée (HTML, ressources, métadonnées, hash) automatiquement. Standard professionnel. Ch.10, 15.

**Censys** — Moteur de recherche d'infrastructure exposée sur Internet. Alternative à Shodan, indexation différente. Ch.21, 40.

**CFAA** — Computer Fraud and Abuse Act. Loi américaine sur l'intrusion informatique. Contour précisé par jurisprudence : Van Buren v. United States (2021), hiQ Labs v. LinkedIn (2022). Ch.7.

**Chain of custody** — Chaîne de conservation. Documentation continue de chaque pièce depuis sa collecte jusqu'à présentation. Crucial pour usage judiciaire. Ch.16, 90.

**Chronolocation** — Détermination de la date / heure de production d'un contenu à partir d'indices visuels (ombres, saison, technologies visibles). Shadow analysis avec SunCalc. Ch.49.

**CIB** — Coordinated Inauthentic Behavior. Terme Meta pour caractériser les activités coordonnées simulant des opinions ou réactions organiques. Concept central pour investigation désinformation. Ch.35, 76.

**Cluster (graphe)** — Sous-groupe densément connecté dans un graphe social. Détection algorithmique (Louvain, Leiden, Infomap). Indicateur de communauté ou coordination. Ch.31, 83.

**Companies House** — Registre des sociétés du Royaume-Uni. Gratuit, exhaustif, standard de transparence mondial. UBO public depuis 2016 (PSC register). Ch.37.

**Compte d'investigation** — Compte sur plateforme (LinkedIn, X, Telegram, Discord, etc.) créé et maintenu spécifiquement pour conduire des investigations OSINT. Doit être mature et cohérent. Ch.11.

**Counter-OSINT** — Pratiques défensives contre OSINT adverse : OPSEC personnelle, monitoring de présence publique, neutralisation de signaux faibles. Ch.10.

**Crt.sh** — Interface publique sur les logs Certificate Transparency. Permet de trouver tous les certificats TLS émis pour un domaine, révélant souvent des sous-domaines cachés. Référence gratuite. Ch.39.

**CSDDD** — Corporate Sustainability Due Diligence Directive (UE 2024). Impose vigilance droits humains et environnement sur supply chain. Mobilise massivement l'OSINT corporate. Ch.7, 77.

**CTI** — Cyber Threat Intelligence. Discipline de renseignement sur menaces cyber : acteurs (APT), infrastructures, TTPs, IOCs. Ch.74.

**DARKINT** — Dark Web Intelligence. Sous-discipline OSINT consacrée aux espaces accessibles via réseaux anonymisés (Tor, I2P, Freenet). Cours dédié Dark Web vFULL. Ch.44.

**Dark fleet** — Flotte maritime opérant en contournement des sanctions. Typiquement pétroliers russes ou iraniens post-2022. AIS éteint, pavillons opaques. Ch.52.

**Deepfake** — Contenu synthétique (image, vidéo, audio) généré par IA, typiquement par face swap, reenactment, voice cloning, ou synthèse complète. Outils 2026 : Sora, Veo, Runway, ElevenLabs, HeyGen. Ch.53.

**DeHashed** — Outil OSINT commercial pour recherche dans breaches et leaks. Plus complet que HIBP. Tarification ~$5/jour. Ch.42.

**Devil's advocate** — Posture méthodologique de contestation systématique des conclusions, pour identifier biais et failles. Variante : red teaming. Ch.81.

**Diamond Model** — Modèle d'analyse CTI (Caltagirone et al. 2013). 4 features : adversary, capability, infrastructure, victim. Ch.74.

**DISARM Framework** — Référentiel communautaire pour catégoriser opérations de désinformation. Équivalent MITRE ATT&CK pour info-ops. Anciennement AMITT. Ch.76.

**DNS** — Domain Name System. Système de résolution des noms en adresses IP. Investigation infrastructure exploite multiples types d'enregistrements : A, AAAA, MX, NS, TXT, CNAME, SOA. Ch.39.

**DNSTwist** — Outil de génération de variantes typosquattées d'un domaine. Identification de domaines potentiellement frauduleux. Ch.41.

**Doppelgänger** — Campagne d'influence russe (2022-2026, en cours). Faux médias imitant Le Monde, Bild, Welt, The Guardian, Fox News. Documentée VIGINUM 2024, EU DisinfoLab, Recorded Future. Attribuée à Structura National Technology et Social Design Agency (Russie). Ch.35, 76.

**Dorks** — Requêtes structurées exploitant les opérateurs avancés des moteurs de recherche (Google, Bing, Shodan, GitHub, etc.). Ch.19, Annexe B.

**DSA** — Digital Services Act (Règlement UE 2022/2065, applicable depuis février 2024). Obligations plateformes sur modération, transparence, accès chercheurs. Ch.7, 24.

**Due diligence** — Vérification approfondie d'une cible (entité, personne) avant engagement commercial, juridique ou financier. KYC, KYB, CSDDD. Ch.38, 77.

**Edge case** — En analyse de graphe : arête (lien entre deux nœuds). Force de l'arête : démontrée / probable / suggérée. Ch.83.

**eIDAS** — Règlement européen 910/2014 sur identification électronique et services de confiance. Encadre horodatages qualifiés et signatures électroniques AdES. Ch.90.

**ELA** — Error Level Analysis. Technique d'analyse forensique d'image qui révèle des zones modifiées par compression locale différente. Outils : FotoForensics, Forensically. Ch.47.

**ENS** — Ethereum Name Service. Permet d'associer un nom humain (`alice.eth`) à une adresse Ethereum. Pivot OSINT possible. Ch.72.

**Entity resolution** — Discipline de fusion correcte des références à la même entité réelle dans différents documents. Outils : RapidFuzz, dedupe.io, Splink. Ch.82.

**EU DisinfoLab** — Organisation européenne dédiée à l'analyse des phénomènes de désinformation. Méthodologie CIB de référence. Cas Indian Chronicles (2019-2020). Ch.58.

**EUvsDisinfo** — Programme EEAS de monitoring de la désinformation russe. Ch.76.

**EXIF** — Exchangeable Image File Format. Métadonnées attachées aux photos (appareil, date, GPS, paramètres techniques). Source OSINT majeure quand préservée. Strippée par la plupart des plateformes sociales à l'upload. Ch.29, 45.

**Failure to Prevent Fraud (UK)** — Offence créée par Economic Crime and Corporate Transparency Act 2023, entrée en vigueur 1er septembre 2025. Responsabilise les organisations sur prévention de la fraude. Ch.7.

**Fact-checking** — Discipline journalistique de vérification d'affirmations publiques. Convergence avec OSINT en 2026. Acteurs : AFP Factuel, FactCheck.org, Snopes, Les Décodeurs, IFCN. Ch.58.

**FININT** — Financial Intelligence. Discipline de renseignement financier : patrimoine, flux, blanchiment, UBO complexes. Cours dédié dans la bibliothèque (FININT vFULL). Ch.70.

**Flightradar24** — Plateforme publique de suivi aérien via ADS-B. Filtre certains aéronefs militaires et privés. Alternative non filtrée : ADS-B Exchange. Ch.52.

**FOFA** — Moteur de recherche d'infrastructure exposée (chinois), concurrent de Shodan. Ch.21.

**Forensically** — Suite d'outils gratuits d'analyse forensique d'image (ELA, clone detection, autres). 29a.ch/photo-forensics. Ch.47.

**GEOINT** — Geospatial Intelligence. Discipline de renseignement géospatial. Inclut géolocalisation OSINT, imagerie satellite, cartographie. Ch.48-51.

**GeoSpy / GeoSeer** — Agents IA spécialisés en géolocalisation à partir de photos. Rupture méthodologique 2024-2026. Ch.51.

**Gephi** — Outil open source de visualisation et analyse de graphes. Standard académique. Algorithmes de communautés (Louvain). Ch.31, 83.

**GitHub leaks** — Secrets accidentellement exposés sur GitHub (API keys, credentials, configurations). Outils : gitleaks, TruffleHog, GitHub Code Search dorks. Ch.41.

**Google Lens** — Outil Google de reconnaissance d'image, particulièrement utile pour objets, monuments, plantes, textes. lens.google.com. Ch.46.

**GreyNoise** — Service de filtrage du « bruit » Internet (IPs qui scannent constamment). Permet de distinguer scan ciblé vs opportuniste. Ch.40.

**Hallucination (LLM)** — Affirmation produite par LLM qui est fausse mais formulée avec autorité. Risque numéro un de l'IA en OSINT. Mitigation : protocole Retrieve-Store-Cite. Ch.64.

**Hamilton 2.0** — Outil de monitoring des opérations d'influence Russie / Chine. Alliance for Securing Democracy / German Marshall Fund. Ch.35.

**HATVP** — Haute Autorité pour la Transparence de la Vie Publique (France). Déclarations d'intérêts élus et hauts fonctionnaires. declaration.hatvp.fr. Ch.37.

**HIBP** — Have I Been Pwned. Service public de Troy Hunt indiquant si un email apparaît dans breaches connues. API freemium. Standard. Ch.42.

**Hive Moderation** — Outil commercial de détection de contenus IA-generated, multi-modèles. Standard professionnel 2026. Ch.30, 56.

**Holehe** — Outil open source qui liste les comptes en ligne associés à un email. 130+ services couverts. Ch.27.

**Hudson Rock** — Service commercial spécialisé stealer logs. Permet de tester si email apparaît dans logs récents. Ch.43.

**Hunchly** — Outil de capture web automatique pour OSINT. Préserve la page complète avec hash et métadonnées d'horodatage. Standard professionnel. Ch.10, 15.

**ICD-203** — Intelligence Community Directive 203 (US IC, 2007 et révisions). Impose vocabulaire calibré WEP dans tous les produits IC US. Ch.85.

**ICIJ** — International Consortium of Investigative Journalists. Producteur des grands leaks : Offshore Leaks (2013), Panama Papers (2016), Paradise Papers (2017), Pandora Papers (2021), Cyprus Confidential (2023). Base publique offshoreleaks.icij.org. Ch.37.

**IMINT** — Image Intelligence. Discipline de renseignement image. Inclut analyse, recherche inversée, géolocalisation, authentification. Ch.45-47.

**Imageboard** — Type de forum image-centric (4chan, 8kun). Sources de mèmes politiques, désinformation, parfois contenus illégaux. Ch.34.

**Information Laundromat** — Outil Stanford Internet Observatory pour cross-référencement de narratifs et campagnes d'influence. Ch.58.

**Information privilégiée (insider information)** — Information non publique susceptible d'affecter le cours d'un titre. Usage illégal est délit boursier (art. L. 465-1 et suivants C. monét. fin.). AMF surveille. Ch.7.

**IOC** — Indicator of Compromise. Élément technique signalant une menace : hash, domaine, IP, URL, email. Standard CTI. Sources : abuse.ch, AlienVault OTX, VirusTotal. Ch.74.

**IR** — Question de renseignement (Intelligence Requirement). Question fermée et vérifiable formulée au cadrage d'une enquête. Ch.12.

**Knowledge graph** — Structure de données RDF ou property graph permettant requêtes complexes sur entités et relations. Maturation 2025-2026 pour OSINT. Outils : Apache Jena, Neo4j. Ch.66.

**Lanceur d'alerte** — Personne signalant des faits susceptibles de qualification pénale. Protégé par directive UE 2019/1937 et loi Sapin 2 modifiée en France (transposition 2022). Ch.7, 95.

**Leak journalistique** — Publication de documents internes par sources anonymes via journalistes. Standard ICIJ. Distinction avec breach (intrusion) et stealer log (malware). Ch.37, 42.

**Llama** — Famille de LLMs open source publiés par Meta. Versions 3.3, 4 en référence 2026. Standard pour déploiement local. Ch.65.

**LLM** — Large Language Model. Modèle de langage de grande taille. ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Mistral, Llama (Meta), Qwen (Alibaba), DeepSeek. Ch.60-65.

**LLM local** — LLM exécuté sur infrastructure souveraine de l'analyste, sans transit cloud. Standard 2026 pour OPSEC stricte. Outils : Ollama, LM Studio, vLLM. Ch.65.

**Maltego** — Outil commercial de visualisation et investigation OSINT par graphes. Standard professionnel. Version Casefile gratuite limitée. Ch.31, 83.

**Mapillary** — Service de Street View collaboratif (racheté Meta). Couverture mondiale. Alternative à Google Street View. Ch.48.

**MarineTraffic** — Plateforme publique de suivi maritime via AIS. Standard pour investigation navires. Freemium. Ch.52.

**MiCA** — Markets in Crypto-Assets Regulation (UE 2023, applicable progressivement 2024-2025). Régulation des actifs crypto et des VASPs en UE. Ch.7.

**MISP** — Malware Information Sharing Platform. Standard open source pour partage CTI. Communautés sectorielles ou nationales (CERT-FR, etc.). Ch.74.

**Mistral** — Famille de LLMs européens (Mistral AI, Paris), open source partial. Standard pour souveraineté EU. Ch.60, 65.

**MITRE ATT&CK** — Framework de catégorisation des TTPs adverses. Référence mondiale en CTI. Mises à jour régulières. attack.mitre.org. Ch.74.

**NIS2** — Directive UE 2022/2555 sur sécurité réseaux et SI. Transposition nationale 2024-2025. Renforce obligations sectorielles. Ch.7.

**Note courte** — Format de communication OSINT standard, 1 page A4, structure stable (en-tête, BLUF, contexte, faits cotés, limites, recommandations). Ch.87.

**OFAC** — Office of Foreign Assets Control (US Treasury). Liste SDN, principal organe de sanctions US. Extraterritorialité forte. Ch.7, 38.

**OFSI** — Office of Financial Sanctions Implementation (HM Treasury, UK). Liste consolidée post-Brexit. Ch.38.

**Ollama** — Outil simple pour exécuter LLMs en local. Standard de déploiement local. Installation curl + commandes minimales. Ch.65.

**OpenCorporates** — Méta-agrégateur de registres corporate (140+ juridictions). Source clé pour cross-juridiction. Freemium. Ch.37.

**OpenSanctions** — Base open source de sanctions, PEP, adverse media agrégée. Standard gratuit, alternative aux outils institutionnels. Ch.38.

**OpenTimestamps** — Service open source d'horodatage via blockchain Bitcoin. Preuve d'antériorité sans tiers de confiance. opentimestamps.org. Ch.16.

**OPSEC** — Operational Security. Discipline de protection des opérations contre détection ou compromission par adversaire. Cinq étapes : identification, analyse menace, analyse vulnérabilité, évaluation risque, application contre-mesures. Ch.10.

**OSINT** — Open Source Intelligence. Renseignement à partir de sources ouvertes et accessibles légalement. Discipline objet du présent cours. Ch.1-2.

**Pappers** — Plateforme française d'accès aux registres officiels (RNE, RBE, BODACC, INPI). Standard FR. Freemium. Ch.37.

**Passive DNS** — Archive historique des résolutions DNS. Permet de voir l'évolution d'un domaine. Sources : SecurityTrails (payant), Farsight DNSDB (industrie), CIRCL Passive DNS. Ch.39.

**PEP** — Politiquement Exposée. Personne occupant ou ayant occupé fonctions publiques importantes. Vigilance renforcée AMLD. Ch.38.

**PimEyes** — Outil de recherche faciale commercial. Sujet à restrictions AI Act / RGPD en UE. Tarification ~$15-300/mois. Ch.30.

**Pivot** — En OSINT, élément qui permet de passer d'une dimension d'enquête à une autre (email → comptes, photo → lieu, nom → société). Compétence centrale d'analyste. Ch.27.

**Playwright** — Bibliothèque moderne pour automatisation navigateur, utilisable pour scraping résilient. Multi-navigateurs. Ch.68.

**Pre-mortem** — Méthode anti-biais consistant à imaginer que l'analyse a échoué et à identifier rétrospectivement pourquoi. Ch.81.

**Protocole Retrieve-Store-Cite** — Protocole opérationnel pour usage rigoureux des LLMs en OSINT. Récupération via LLM, vérification source primaire, citation de la source originale (jamais du LLM). Ch.63.

**Provenance** — Documentation de l'origine et de l'historique d'un contenu numérique. Standard C2PA. Ch.55.

**RBE** — Registre des Bénéficiaires Effectifs (France). Géré par INPI, accès partiel post-CJUE 2022. Ch.37.

**RDAP** — Registration Data Access Protocol. Successeur du WHOIS. JSON, query HTTPS. Ch.39.

**Recherche inversée** — Technique de prendre une image en entrée et trouver ses autres occurrences. Outils : Yandex (référence 2026), Google Lens, TinEye, Bing Visual Search. Ch.46.

**Red team** — Équipe adoptant le rôle de l'adversaire pour tester analyses ou systèmes. Posture méthodologique anti-biais. Ch.81.

**RGPD** — Règlement européen 2016/679 sur la protection des données personnelles. Entré en vigueur 25 mai 2018. Cadre central pour OSINT en UE. Ch.7.

**RNE** — Registre National des Entreprises (France). Depuis 2023, unifie RCS, RM, registre actifs agricoles. Accessible via Pappers, INPI. Ch.37.

**Sayari** — Outil commercial OSINT corporate moderne. Forte couverture Chine, Russie, Iran. Ch.37.

**SATs** — Structured Analytic Techniques. Catalogue de techniques formalisées par l'IC US. Inclut ACH, Key Assumptions Check, Devil's Advocacy, Red Cell, etc. Référence : Heuer & Pherson (2020). Ch.78.

**Sherlock** — Outil open source de recherche d'username cross-plateformes. 300+ sites. Standard. github.com/sherlock-project. Ch.27.

**Shodan** — Moteur de recherche d'infrastructure exposée sur Internet. Standard. shodan.io. Freemium. Ch.21, 40.

**SingleFile** — Extension navigateur pour capture web one-file (HTML + ressources). Alternative gratuite à Hunchly pour usages légers. Ch.15.

**SOCMINT** — Social Media Intelligence. Composante OSINT focalisée sur réseaux sociaux. Ch.31-35.

**SOR** — Statement of Request. Document de cadrage d'une mission OSINT, contenant commanditaire, finalité, périmètre, bornes, IR. Ch.12.

**Sock puppet** — Avatar / compte secondaire utilisé pour investigation. Légalement et déontologiquement encadré. Ch.11.

**Spamouflage / Dragonbridge** — Opération d'influence chinoise documentée depuis 2017, intensifiée 2019-2026. Volume massif de faux comptes sur YouTube, Twitter/X, Facebook, TikTok. Documentée Graphika, Stanford Internet Observatory, Mandiant. Ch.76.

**Stealer log** — Données exfiltrées par malware infostealer (RedLine, Vidar, Raccoon, Lumma, Stealc). Vendues sur Telegram et forums. Ch.43.

**STIX/TAXII** — Standards de format (STIX) et transport (TAXII) pour partage CTI. Ch.74.

**Storm-1516** — Opération d'influence russe identifiée 2024-2026 par Microsoft Threat Intelligence. Usage marqué de deepfakes audio-vidéo. Ch.76.

**SynthID** — Watermark invisible Google DeepMind sur contenus générés par leurs modèles IA. Image, audio, texte, vidéo. Détection progressive. Ch.56.

**Tails** — Système d'exploitation live sur clé USB orienté anonymat (Tor par défaut, traces effacées). Ch.10.

**Tankertrackers** — Service commercial spécialisé suivi pétroliers, particulièrement utile pour sanctions maritime. tankertrackers.com. Ch.52.

**Telegago** — Moteur de recherche public dédié à Telegram (canaux publics, messages). telegago.fr. Ch.33.

**TLP** — Traffic Light Protocol. Classification d'informations sensibles : RED, AMBER+STRICT, AMBER, GREEN, CLEAR. Géré par FIRST. Version 2.0 (2022). Ch.91.

**Tor** — The Onion Router. Réseau de routage anonyme. Standard du dark web. Tor Browser pour usage. Ch.10, 44.

**TruePeopleSearch / FastPeopleSearch / Whitepages** — Bases de données people search américaines. Limites RGPD en UE. Ch.26.

**TTP** — Tactics, Techniques, Procedures. Modes opératoires d'un adversaire. Standard MITRE ATT&CK en CTI. Ch.74.

**UBO** — Ultimate Beneficial Owner. Bénéficiaire effectif d'une entité juridique. Personne physique contrôlant in fine (seuil indicatif 25 %). Sources : RBE France, PSC UK, registres UBO nationaux. Ch.36.

**VASP** — Virtual Asset Service Provider. Plateforme crypto régulée. Soumis au Travel Rule FATF et MiCA UE. Ch.72.

**VeraCrypt** — Outil open source de chiffrement de volumes. Standard pour préservation locale chiffrée. Ch.16.

**Verification Handbook** — Manuel de référence du fact-checking et de la vérification (European Journalism Centre). Plusieurs éditions, dont édition deepfakes 2020+. Ch.57.

**VIGINUM** — Service français (SGDSN) de vigilance contre ingérences numériques étrangères. Référence pour CIB en France. Rapport Doppelgänger 2024. Ch.35, 76.

**Wappalyzer** — Extension navigateur pour identifier technologies utilisées par un site (CMS, frameworks, analytics, CDN). Ch.41.

**Watermarking IA** — Signature invisible insérée dans contenus IA-generated, détectable ultérieurement. SynthID (Google), Stable Signature (Meta). Ch.56.

**Wayback Machine** — Service d'archivage web d'Internet Archive. Accumulation de snapshots historiques depuis 1996. archive.org/web. Ch.20.

**WEP** — Words of Estimative Probability. Vocabulaire calibré pour exprimer niveaux de confiance dans conclusions analytiques. Quasi-certain / Très probable / Probable / Possible / Peu probable / Très peu probable / Hautement improbable. ICD-203 standard. Ch.85.

**WHOIS** — Protocole historique d'accès aux données d'enregistrement de domaine. Restrictions post-RGPD 2018 (REDACTED FOR PRIVACY). WHOIS historique via DomainTools pour pre-2018. Ch.39.

**Whonix** — VM open source orientée anonymat (Tor par défaut, isolation). Alternative à Tails. Ch.10.

**Wolfram Alpha** — Moteur computationnel. Pour OSINT : météo historique précise, calculs astronomiques (cohérent avec SunCalc). Ch.49.

**Yandex Images** — Moteur de recherche d'images russe. Référence pour reverse image search en 2026. Indexation différente de Google. Ch.46.

**yt-dlp** — Outil open source de téléchargement vidéo depuis YouTube et 1000+ autres plateformes. Standard pour préservation. Ch.32.

**ZoomEye** — Moteur de recherche d'infrastructure (chinois). Alternative à Shodan. Ch.21.

-----
