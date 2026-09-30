---
title: ANNEXES
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 14
chapters: 15
---

> **Avant-propos aux annexes.** Les annexes constituent la **boîte à outils opérationnelle** du master OSINT. Référentiel à conserver à portée de main pendant les enquêtes, mis à jour avec les évolutions du domaine. Chaque annexe est conçue pour être consultable indépendamment.
>
> ### Convention « État des connaissances : mai 2026 »
>
> L'ensemble du cours et des annexes reflète l'écosystème OSINT à **mai 2026**. La discipline évolue à un rythme **mensuel** sur certains compartiments :
>
> - **Outils OSINT** : disponibilité, accès gratuit / payant, fonctionnalités, API. Les outils gratuits peuvent passer payants, ou être abandonnés. Tester avant usage critique.
> - **Politiques de plateformes** : conditions d'utilisation, restrictions d'accès, suppressions de fonctionnalités. Particulièrement volatiles depuis 2023-2026.
> - **Modèles IA** : générations successives mensuelles. Capacités, prix, restrictions évoluent. Llama, Claude, GPT, Gemini, Mistral en révisions régulières.
> - **Statut des API** : payantes / restreintes / supprimées. X (Twitter) API, Reddit API, Meta Graph API sont en évolution constante depuis 2023.
> - **Doctrine française / alliée** : VIGINUM, ANSSI, ODNI publications régulières. Évolutions doctrinales suivies.
> - **Telegram / Durov** : suite arrestation France août 2024, modération et coopération LEA renforcées progressivement.
> - **Acteurs de désinformation** : Doppelgänger, Spamouflage, Storm-1516 et autres évoluent en continu, démantèlements et re-émergences.
> - **Outils de détection deepfake / contenu IA** : course armement permanente entre générateurs et détecteurs. Scores et fiabilité varient.
> - **Cadres juridiques** : AI Act, DSA, CSDDD, NIS2 en application progressive 2024-2026. Interprétations et décrets continuent.
>
> **Discipline analyste 2026.**
> - **Vérifier la documentation officielle** avant tout usage opérationnel.
> - **Tester l'outil** avant de le mobiliser sur enquête critique.
> - **Cross-référencer** avec sources d'actualité de la communauté OSINT.
> - **Veille trimestrielle minimum** sur outils du parc principal.
> - **Audit annuel** de la méthodologie.
>
> **Niveaux de risque d'obsolescence** mentionnés dans les annexes :
> - **Faible** : outil mature, infrastructure stable (registres officiels, standards ouverts).
> - **Moyen** : outil dépendant de plateformes tierces ou évolutions techniques.
> - **Élevé** : outil dépendant d'une API ou plateforme sujette à restrictions fréquentes.
> - **Très élevé** : outil dont l'existence ou l'accès peut disparaître entre deux enquêtes.
> - **Juridique élevé** : risque légal d'usage (AI Act, RGPD, CFAA, etc.) prépondérant sur risque technique.

-----

## ANNEXE A — Glossaire OSINT 2026

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


## ANNEXE B — Dorks et opérateurs multi-moteurs

> **État des connaissances : mai 2026.** Les opérateurs ci-dessous reflètent les fonctionnalités des moteurs à cette date. Les moteurs **modifient et restreignent régulièrement** leurs opérateurs (Google notamment a déprécié plusieurs opérateurs entre 2020 et 2025). Tester les dorks avant usage critique.

Inventaire pratique des **dorks** (requêtes structurées) pour les principaux moteurs et services OSINT. À utiliser avec discernement : certains dorks peuvent enfreindre CGU ou s'approcher de zones grises légales (recherche de credentials notamment).

### B.1 — Dorks Google

**Opérateurs principaux.**

- `"phrase exacte"` — recherche littérale.
- `-mot` — exclusion.
- `site:domaine.com` — restriction à un domaine.
- `inurl:mot` — mot dans URL.
- `intitle:mot` — mot dans titre.
- `intext:mot` — mot dans corps.
- `filetype:pdf` — type de fichier.
- `before:2024-12-31` / `after:2020-01-01` — date.
- `OR` ou `|` — alternative.
- `AND` ou `+` — conjonction (implicite).
- `*` — wildcard.

**Opérateurs dépréciés ou instables 2026.** `cache:`, `link:`, `info:` ne fonctionnent plus de manière fiable. `+` strict est partiellement réintroduit.

**Documents internes accidentellement exposés.**
```
site:technovert.fr filetype:pdf "confidential"
site:technovert.fr filetype:doc OR filetype:docx
site:technovert.fr filetype:xlsx
site:technovert.fr inurl:internal
"technovert" filetype:pdf "internal use only"
```

**Identités d'employés.**
```
site:linkedin.com/in/ "technovert"
"@technovert.fr" -site:technovert.fr
"works at technovert" site:facebook.com
"employé technovert" OR "salarié technovert"
```

**Credentials et fuites (à utiliser avec EXTRÊME prudence).**
```
"technovert" "password" filetype:txt
"@technovert.fr" "password"
inurl:wp-config.php "technovert"
"technovert" intext:"DB_PASSWORD"
"technovert" filetype:env
```

**Sous-domaines.**
```
site:*.technovert.fr -site:www.technovert.fr
```

**Erreurs révélatrices d'infrastructure.**
```
"technovert" intext:"Apache 2.4" inurl:phpinfo.php
"Index of /" "technovert"
intitle:"index of" "technovert" private
"technovert" intitle:"sql syntax error"
```

**Documents techniques.**
```
"technovert" filetype:log
"technovert" filetype:sql
"technovert" filetype:bak
"technovert" filetype:conf OR filetype:cfg
```

### B.2 — Dorks DuckDuckGo

DuckDuckGo accepte la plupart des opérateurs Google avec quelques spécificités :

- `!bang` redirige vers autres moteurs : `!g technovert` → Google, `!yt` → YouTube, `!w` → Wikipedia, `!gh` → GitHub.
- Plus respectueux privacy.
- Index propre + sources Bing.
- `region:fr-fr` — restriction régionale.

**Utile pour OSINT.** DuckDuckGo n'a pas la personnalisation Google. Résultats plus uniformes, sans bulle de filtre. Utile pour comparaison.

### B.3 — Dorks Bing

Opérateurs proches de Google avec spécificités :

- `contains:type` — pages contenant fichiers de ce type (`contains:pdf`).
- `feed:` — flux RSS.
- `hasfeed:` — pages avec flux RSS.
- `language:fr` — langue.
- `loc:FR` — localisation.
- `ip:192.168.x.x` — pages servies par cette IP (utile OSINT infrastructure).
- `linkfromdomain:domaine.com` — pages liées depuis ce domaine.

**Bing est souvent meilleur pour :** indexation profonde sites US, contenu Microsoft, archives OneDrive / SharePoint.

### B.4 — Dorks Yandex

Yandex utilise des opérateurs proches mais avec syntaxe propre :

- `mime:pdf` au lieu de `filetype:pdf`.
- `lang:fr` (codes ISO).
- `domain:technovert.fr`.
- `url:"path"` — recherche dans URL.
- `title:"phrase"` — dans titre.
- `<<` / `>>` — proximité (deux mots à N positions).
- `& & &` — opérateurs de proximité (mots dans même phrase, paragraphe, document).

**Très utile pour.** Requêtes en russe / CEI, recherches d'images, indexation différente.

### B.5 — Dorks Shodan

Spécifique à infrastructure exposée.

**Opérateurs.**
- `port:22` — port spécifique.
- `country:FR` — pays.
- `city:Paris`.
- `org:"TechnoVert"` — organisation.
- `hostname:technovert.fr` — hostname.
- `ssl.cert.subject.cn:technovert` — CN du certificat.
- `ssl.cert.issuer.cn:"Let's Encrypt"` — émetteur.
- `product:Apache` — produit.
- `version:"2.4"` — version.
- `os:Linux` — OS.
- `before:2024-01-01`, `after:2023-01-01` — date.
- `tag:vpn` / `tag:webcam` / `tag:ics` — tags Shodan.
- `has_screenshot:true` — captures disponibles.
- `vuln:CVE-2021-44228` — vulnérabilité spécifique.

**Exemples.**
```
hostname:technovert.fr port:443
org:"TechnoVert" country:FR
ssl.cert.subject.cn:technovert
"webcam" country:FR
port:3389 has_screenshot:true   # RDP exposés (très sensible)
product:"Apache" version:"2.2"  # versions obsolètes
"Apache/2.4.49" "X-Powered-By"  # vulnérables CVE-2021-41773
vuln:CVE-2021-44228             # Log4Shell exposés
```

### B.6 — Dorks Censys

Syntaxe différente mais capacités similaires.

```
services.tls.certificates.leaf_data.subject.common_name:technovert
services.banner:"server: apache"
services.port:443
location.country_code:FR
autonomous_system.organization:"OVH SAS"
labels:`expired-cert`
last_updated_at:[2024-01-01 TO 2024-12-31]
```

Censys propose **Censys Search** (web) et **Censys ASM** (continu).

### B.7 — Dorks GitHub

Recherche de code et de secrets.

**Opérateurs.**
- `user:username` — utilisateur.
- `org:org-name` — organisation.
- `repo:user/repo` — dépôt spécifique.
- `filename:.env` — nom de fichier.
- `extension:py` — extension.
- `language:python`.
- `path:src/` — chemin.
- `created:>2024-01-01` — créé après.
- `pushed:>2024-01-01` — pushed après.
- `stars:>100` — étoiles.

**Dorks pour secrets exposés (déontologie attentive).**
```
"technovert" "password"
"@technovert.fr" extension:env
filename:.env "technovert"
"DB_PASSWORD" "technovert"
"api_key" "technovert"
"AWS_SECRET_ACCESS_KEY" "technovert"
filename:credentials "technovert"
"BEGIN RSA PRIVATE KEY" "technovert"
```

**Détection d'employés.**
```
"@technovert.fr" extension:py
user:* email:@technovert.fr
```

### B.8 — Dorks Telegram (via Telegago, Lyzem)

Telegram n'a pas d'opérateurs natifs riches en search public. Mais Telegago / Lyzem indexent canaux publics.

**Telegago.fr.**
- Recherche par mots-clés simples.
- Filtres par type de canal, taille.
- Tri par activité.

**Lyzem.com.**
- Recherche dans messages historiques.
- Filtres date, canal.
- Indexation plus large.

**Recherches typiques.**
- Nom de cible + secteur.
- Domaines suspects.
- Stealer logs (« cloud accounts », « combo list », etc.).
- Vente de données.

### B.9 — Dorks LinkedIn

LinkedIn restreint fortement. Quelques techniques :

**Recherche externe via Google.**
```
site:linkedin.com/in/ "technovert"
site:linkedin.com/in/ "ingénieur" "technovert"
site:linkedin.com/in/ inurl:"marc-delaunay"
site:linkedin.com/company "technovert"
```

**Filtres internes (Sales Navigator ou compte invest).**
- Industrie.
- Localisation.
- Ancienneté (« years of experience »).
- Postes actuels et passés.
- Écoles fréquentées.
- Compétences.
- Boolean : `("DAF" OR "CFO") AND "technovert" AND "Paris"`.

**Pour identifier transfuges.** Recherche par « previously at Technovert » via Sales Navigator.

### B.10 — Dorks Twitter / X

**X search avancée.** twitter.com/search-advanced (encore actif partiellement en 2026 selon évolutions).

**Opérateurs.**
- `from:username`.
- `to:username`.
- `since:2024-01-01`.
- `until:2024-12-31`.
- `near:"Paris" within:10km` (souvent désactivé).
- `lang:fr`.
- `filter:images`, `filter:videos`, `filter:links`.
- `min_retweets:50`.
- `min_likes:100`.
- `-filter:replies` — exclure réponses.

**Exemples.**
```
from:mdelaunay76 since:2024-01-01
"technovert" filter:images since:2025-09-01
"@mdelaunay76" -from:mdelaunay76   # mentions de
"technovert" lang:fr min_retweets:10
```

### B.11 — Dorks Wayback Machine

**Recherches Wayback.**
- `web.archive.org/web/*/technovert.fr` — toutes les versions.
- `web.archive.org/web/2020*/technovert.fr` — versions 2020.
- `archive.org/wayback/available?url=technovert.fr&timestamp=20200101` — API.

**Astuce.** Wayback indexe parfois des pages depuis longtemps supprimées de l'original. Très utile pour archives.

### B.12 — Dorks WHOIS / DomainTools

Via DomainTools (payant) :
- Recherche WHOIS historique par email.
- Recherche par nom du registrant (pre-RGPD).
- Recherche par adresse postale.
- Recherche par téléphone.
- Reverse IP, reverse NS.

**Outils gratuits.**
- ViewDNS.info : reverse IP, reverse WHOIS basique.
- crt.sh : Certificate Transparency (couvre indirectement).

### B.13 — Dorks moteurs académiques

**Google Scholar.**
- `author:"X. Smith"` — auteur.
- `intitle:"climate"` — dans titre.
- `source:"Nature"` — journal source.
- `year:2024..2026` — plage années.

**Semantic Scholar.** Recherche par auteur, sujet, citations.

**Sci-Hub** (controversé, copyright) : archive massive d'articles.

### B.14 — Discipline d'usage

**Bonne pratique.**
- Variations multiples sur même requête.
- Comparer résultats entre moteurs.
- Documenter les dorks ayant produit résultats utiles dans le journal d'enquête.
- Captures Hunchly systématiques.

**Limites éthiques et légales.**
- Dorks de recherche de credentials = zone grise (passage à exploitation = pénal).
- Reverse engineering de configurations privées = passage à zone Bluetouff.
- Respect CGU des moteurs (généralement larges pour recherche).

**Ressources.**
- **GHDB** (Google Hacking Database, exploit-db.com) : catalogue communautaire.
- **OSINT Combine Cheat Sheets** : références par sujet.
- **Awesome OSINT** (GitHub) : compilation.

-----


## ANNEXE C — Atlas plateformes, registres et sources par pays

> **État des connaissances : mai 2026.** Les sources OSINT par pays évoluent : nouveaux registres ouverts, restrictions d'accès, modifications réglementaires (notamment registres UBO post-CJUE 2022, refonte AMLD UE 2024). Vérifier l'accessibilité actuelle avant usage opérationnel.

Inventaire géographique des sources OSINT principales par pays / région. Sélection non exhaustive : couverture des cas les plus fréquents.

### C.1 — France

**Identités personnes.**
- Pages Jaunes / Annuaire.
- Société.com (croisement personnes-sociétés).
- Avis de naissance / mariage / décès dans presse régionale (archives partiellement payantes).
- Généalogie : Geneanet, FamilySearch.

**Sociétés.**
- **Pappers** (pappers.fr) : standard, agrège tout (RNE, RBE, BODACC, INPI). Freemium.
- **Infogreffe** : registre officiel des greffes.
- **RNE** (Registre National des Entreprises, post-2023, unifiant RCS, RM, etc.).
- **RBE** (Registre Bénéficiaires Effectifs) via INPI (accès partiel).
- **BODACC** (bodacc.fr) : annonces légales.
- **societe.com**, **manageo.fr**, **verif.com** : agrégateurs gratuits.

**Patrimoine immobilier.**
- **Cadastre.gouv.fr** : visualisation parcelles (pas accès direct propriétaire).
- **DVF (Demandes de Valeurs Foncières)** sur data.gouv.fr : transactions immobilières historiques 2014+.
- **Géoportail** (IGN) : cartographie complète France.
- SCI propriétaires : via Pappers (dirigeants + UBO révèlent).
- Notaires : annonces ventes immobilières publiques.

**Justice et contentieux.**
- **Légifrance** (legifrance.gouv.fr) : jurisprudence officielle, lois, codes.
- **Doctrine.fr** : jurisprudence enrichie (payant institutionnel).
- **JuriCA** : Cour de cassation.
- **Conseil d'État** : décisions administratives.

**PEP et transparence.**
- **HATVP** (declaration.hatvp.fr) : Haute Autorité Transparence Vie Publique. Déclarations d'intérêts élus, hauts fonctionnaires.
- **declaration.deputes.fr** : déclarations députés.
- **Quintetto** : agrégateur transparence parlementaire (associatif).

**Marchés publics.**
- **BOAMP** (Bulletin Officiel des Annonces de Marchés Publics).
- **PLACE** (Plateforme des Achats de l'État).
- **DECP** (Données Essentielles de la Commande Publique) sur data.gouv.fr.

**Brevets et marques.**
- **INPI** : brevets et marques France.
- **Espacenet** (EPO) : brevets Europe.

**Données ouvertes.**
- **data.gouv.fr** : portail open data français.
- **api.gouv.fr** : APIs publiques.

**Régulateurs sectoriels.**
- **AMF** (financier).
- **ACPR** (banque, assurance).
- **ARCEP** (télécom).
- **CRE** (énergie).
- **ARCOM** (audiovisuel et numérique, ex-CSA + Hadopi).
- **CNIL** (protection données).

**Médias et presse.**
- **AFP**, **Reuters France**, **Le Monde**, **Le Figaro**, **Les Échos**, **Libération**.
- **Mediapart**, **Disclose** : investigations.
- **Presse régionale** (Ouest-France, La Voix du Nord, etc.) — précieuse pour mentions locales.
- **Archives presse** : Europresse, Cafeyn (souvent via abonnement bibliothèque).

### C.2 — Royaume-Uni (post-Brexit)

**Sociétés.**
- **Companies House** (gov.uk/government/organisations/companies-house) : standard mondial, **gratuit**, complet. UBO public depuis 2016 (PSC register).
- **GOV.UK companies search**.
- API gratuite mature.

**Justice.**
- **BAILII** (bailii.org) : jurisprudence gratuite.
- **GOV.UK Tribunals**.
- **Courts and Tribunals Judiciary**.

**Sanctions.**
- **OFSI** (HM Treasury) : sanctions consolidées UK post-Brexit.

**Patrimoine.**
- **HM Land Registry** (gov.uk/government/organisations/land-registry).

**Brevets.**
- **UK Intellectual Property Office** (gov.uk/government/organisations/intellectual-property-office).

**PEP.**
- **MPs Register of Members' Financial Interests**.
- **Register of Lords Interests**.

**Médias.**
- BBC, The Guardian, The Times, Financial Times, Telegraph, Daily Mail.
- Reuters UK, Bloomberg UK.

### C.3 — États-Unis

**Sociétés (fragmentation étatique).**
- **Delaware Department of State** : juridiction préférée pour incorporation (corp.delaware.gov).
- **California Secretary of State**, **New York Department of State**, **Texas, Nevada, Florida** : portails dédiés par état.
- **Corporate Transparency Act** (2024) : registre UBO fédéral en cours de déploiement (ralenti par contentieux, statut évolutif 2025-2026).

**Sociétés cotées.**
- **SEC EDGAR** (sec.gov/edgar) : référence absolue. Filings 10-K, 10-Q, 8-K, proxy statements, Form 4 (transactions insider).

**Justice.**
- **PACER** (pacer.uscourts.gov) : standard fédéral, payant par document.
- **CourtListener** (courtlistener.com) : agrégateur gratuit.
- **Justia** (justia.com) : alternative.
- **Caselaw Access Project** (Harvard).

**Sanctions.**
- **OFAC SDN List** (sanctionssearch.ofac.treas.gov).
- **BIS Entity List** (Bureau of Industry and Security).

**Patrimoine immobilier.**
- **Recorder of Deeds** par comté (variable).
- **Zillow, Redfin, Realtor.com** : recherches immobilières.

**Personnes.**
- **TruePeopleSearch**, **FastPeopleSearch**, **Whitepages**, **BeenVerified**, **Spokeo**, **Intelius** (attention RGPD pour cibles UE).

**Marchés publics fédéraux.**
- **SAM.gov** (System for Award Management).
- **USAspending.gov**.

**Médias.**
- New York Times, Washington Post, Wall Street Journal, Reuters US, Bloomberg, AP, NPR.
- ProPublica (investigations), The Intercept.

### C.4 — Union Européenne (États membres principaux)

**Belgique.**
- **Banque-Carrefour des Entreprises (BCE / CBE)** (kbo-bce-ps.economie.fgov.be) — gratuit.
- **Moniteur belge** (annonces légales).
- **NBB** : comptes annuels.

**Pays-Bas.**
- **KvK (Kamer van Koophandel)** (kvk.nl) — payant pour la plupart des données.
- **CBS** : statistiques.

**Allemagne.**
- **Handelsregister** (handelsregister.de) — gratuit base, payant pour comptes détaillés.
- **Bundesanzeiger** : annonces officielles.
- **Unternehmensregister**.

**Italie.**
- **Registro Imprese** (registroimprese.it) — payant.
- **InfoCamere**.

**Espagne.**
- **Registro Mercantil** — payant.
- **Borme** (annonces).

**Irlande.**
- **Companies Registration Office (CRO)** (cro.ie) — gratuit. Pays attractif pour multinationales tech.

**Luxembourg.**
- **RCS** (Registre de Commerce et des Sociétés) (lbr.lu) — gratuit base.
- **RESA** (annonces).

**Malte.**
- **Companies Registry** (mfsa.com.mt) — gratuit recherche.

**Chypre.**
- **Department of Registrar of Companies** (efiling.drcor.mcit.gov.cy) — gratuit base. Registre UBO partiellement accessible post-CJUE 2022.

**Autriche.**
- **Firmenbuch** — payant.

**Portugal.**
- **Portal da Justiça** : registre commercial.

**Pologne.**
- **KRS** (Krajowy Rejestr Sądowy).

**Sanctions UE.**
- **Liste consolidée UE** (eeas.europa.eu).
- **Sanctions Map** (sanctionsmap.eu).

**Registres UBO.** Issus de la 5e AMLD. Accessibilité variable depuis arrêt CJUE 2022 (limitation accès public dans plusieurs États membres).

### C.5 — Suisse

**Sociétés.**
- **Zefix** (zefix.ch) : standard officiel, gratuit.
- **moneyhouse.ch** : agrégateur (freemium).

**Justice.**
- **Tribunal fédéral** (bger.ch).
- **Jurisprudence** par canton.

**Cadastre.** Cantonal, accessibilité variable.

**Sanctions.** SECO (Secrétariat d'État à l'économie) : sanctions suisses.

### C.6 — Paradis fiscaux et juridictions opaques

**Plus accessibles.**
- **Malte** (UE). Companies Registry gratuit recherche.
- **Chypre** (UE). Department of Registrar.
- **Luxembourg** (UE). RCS.
- **Pays-Bas** (UE). KvK.

**Difficiles.**
- **British Virgin Islands (BVI)**. Registre existant, accès très restreint.
- **Cayman Islands**. Idem.
- **Bermuda**. Idem.
- **Liechtenstein**. Idem.
- **Hong Kong**. Companies Registry HK : gratuit base, payant pour détails.
- **Singapour**. ACRA : payant.

**Très difficiles.**
- **Panama**. Avant Panama Papers, opaque ; depuis, registre légèrement plus ouvert.
- **Belize**.
- **Seychelles**.
- **Marshall Islands**.

**Pour ces juridictions opaques.**
- **ICIJ Offshore Leaks Database** (offshoreleaks.icij.org) : principale source publique.
- **OCCRP Aleph** : agrégation journalistique.
- **Sayari** (commercial) : couverture étendue.
- Documents internes leakés (à manier avec déontologie et expertise).

### C.7 — Russie

**Sociétés.**
- **SPARK Interfax** (spark-interfax.com) : payant, standard institutionnel.
- **Kontur.Focus** (focus.kontur.ru) : payant.
- **rusprofile.ru** : freemium.
- **list-org.com** : gratuit basique.
- **EGRUL** (egrul.nalog.ru) : registre officiel des personnes morales.

**Personnes.**
- VK (vk.com), OK.ru (réseaux sociaux russes).
- Outils OSINT spécialisés russes : **220vk** (recherche cross VK).

**Justice.**
- **kad.arbitr.ru** : litiges commerciaux.
- **sudrf.ru** : juridictions générales.

**Sanctions russes.** Liste des « pays hostiles » et autres. Restrictions d'accès à plusieurs ressources russes depuis 2022 selon localisation analyste.

**Accès depuis Europe.** Souvent restreint depuis 2022 (sanctions réciproques, blocage IP). VPN parfois nécessaire.

### C.8 — Chine

**Sociétés.**
- **Tianyancha** (天眼查) : standard, freemium.
- **Qichacha** (企查查) : alternative.
- **National Enterprise Credit Information Publicity System** (gsxt.gov.cn) : officiel.

**Personnes.**
- Weibo, WeChat (limités OSINT externe).
- Baidu (moteur).

**Justice.**
- **Chinese Court Documents** (wenshu.court.gov.cn) : depuis 2014, recherche jurisprudence.

**Restrictions.** Great Firewall. Accès souvent restreint, VPN nécessaire. Langue (mandarin) : LLMs multilingues utiles (Qwen, Claude, GPT). Censure progressive.

### C.9 — Inde

**Sociétés.**
- **MCA21** (Ministry of Corporate Affairs) : portail officiel.
- **Tofler** (tofler.in) : agrégateur freemium.
- **Zauba Corp** (zaubacorp.com) : gratuit basique.

**Justice.**
- **Indian Kanoon** (indiankanoon.org) : jurisprudence gratuite.
- **eCourts** : gov.

**Médias.**
- The Hindu, Times of India, Hindustan Times, NDTV, Indian Express.

### C.10 — Australie

**Sociétés.**
- **ASIC** (Australian Securities and Investments Commission) (asic.gov.au).
- **ABN Lookup** (abr.business.gov.au) : Australian Business Number.

**Justice.**
- **AustLII** (austlii.edu.au) : jurisprudence gratuite.

### C.11 — Canada

**Sociétés.**
- **Corporations Canada** (ic.gc.ca) : fédéral.
- Registries provinciaux (Ontario, Quebec, etc.).

**Justice.**
- **CanLII** (canlii.org) : jurisprudence gratuite.

### C.12 — Brésil

**Sociétés.**
- **Receita Federal** : CNPJ lookup.
- **JUCESP** (São Paulo) et autres juntas comerciais.

**Justice.**
- **JusBrasil** : jurisprudence.

### C.13 — Mexique

**Sociétés.**
- **RPC** (Registro Público de Comercio).
- **SAT** : RFC.

### C.14 — Argentine

**Sociétés.**
- **CUIT** lookup.
- **IGJ** (Inspección General de Justicia).

### C.15 — Israël

**Sociétés.**
- **Israel Companies Registrar**.
- **Ministry of Justice** : commerce.

**Justice.**
- **Nevo** (en hébreu, payant).

### C.16 — Émirats Arabes Unis

**Sociétés.**
- **DMCC** (Dubai Multi Commodities Centre) : free zone, registre.
- **DIFC** (Dubai International Financial Centre) : registre.
- **ADGM** (Abu Dhabi Global Market).
- Free zones diverses, transparence variable.

### C.17 — Pays africains

**Variabilité forte.**

**Afrique du Sud.**
- **CIPC** (Companies and Intellectual Property Commission) (cipc.co.za).
- **SARS** : revenus.

**Nigeria.**
- **Corporate Affairs Commission** (cac.gov.ng).

**Kenya.**
- **eCitizen Business Registration Service**.

**Maroc.**
- **OMPIC** (registre commerce).
- **DGI** : impôts.

**Égypte.**
- **GAFI** (General Authority for Investment).

**Pour la plupart des pays africains.** Recours à OpenCorporates et leaks (Pandora Papers, FinCEN Files ont révélé beaucoup d'Afrique).

### C.18 — Médias internationaux à connaître

**Agences.**
- AFP, Reuters, AP, Bloomberg, EFE, Xinhua, TASS, ANSA, DPA, Kyodo.

**Médias d'investigation transfrontaliers.**
- **OCCRP** (Organized Crime and Corruption Reporting Project) : Europe de l'Est, transversal.
- **ICIJ** : grands leaks.
- **Forbidden Stories** : continuation d'enquêtes interrompues.
- **Bellingcat** : OSINT investigation.
- **Mediapart** (France), **Disclose** (France), **Reporterre**.
- **The Guardian** (UK), **Süddeutsche Zeitung** (DE), **Der Spiegel** (DE), **Le Monde** (FR), **El País** (ES), **La Repubblica** (IT).
- **The New York Times**, **Washington Post**, **ProPublica**, **The Intercept** (US).

### C.19 — Synthèse — stratégie pays

| Cas | Priorité |
|---|---|
| Société France | Pappers + BODACC + RBE |
| Société UK | Companies House (gratuit, complet) |
| Société UE | Registre national + OpenCorporates |
| Société US cotée | SEC EDGAR |
| Société US non cotée | Registre étatique (Delaware en priorité) |
| Paradis fiscal | OpenCorporates + ICIJ leaks + Aleph |
| Société russe | rusprofile + EGRUL + presse |
| Société chinoise | Tianyancha + VPN |
| Société indienne | MCA21 + Tofler |
| Société émirats | Registries free zone + ICIJ |
| Multi-juridictions | OpenCorporates + Sayari (si dispo) |

### C.20 — Discipline d'usage

**Toujours vérifier.**
- Accessibilité actuelle (sites évoluent, certains restreignent).
- Conditions d'usage (CGU, restrictions API).
- Légalité de l'accès depuis votre juridiction.
- Cohérence des sources (un seul registre ≠ vérité absolue).

**Cross-référencement.** Aucun registre n'est exhaustif. La triangulation par 2-3 sources reste la règle.

-----


## ANNEXE D — Cheat sheets : sélecteur → outils

> **État des connaissances : mai 2026.** Les outils mentionnés et leurs accès évoluent. Vérifier disponibilité et conditions avant usage opérationnel.

Tableau de correspondance rapide : à partir d'un sélecteur initial, quels outils mobiliser.

### D.1 — Sélecteur : nom de personne

| Étape | Outils | Risque obsolescence |
|---|---|---|
| Désambiguïsation | Recherches presse, LinkedIn, Pappers (si dirigeant) | Faible |
| Identification corporate | Pappers (dirigeants), Companies House, SEC EDGAR | Faible |
| Patrimoine | Cadastre.gouv.fr, SCI Pappers, DVF | Faible |
| Réseaux sociaux | Sherlock (si username probable), recherches multi-plateformes | Moyen (Sherlock updates fréquentes) |
| Adverse media | Google + Wayback + presse spécialisée | Faible |
| Sanctions / PEP | OpenSanctions, HATVP, WorldCheck (institutionnel) | Faible |
| Photos | Recherche inversée Yandex / Google Lens / TinEye | Faible |
| Généalogie / famille | Geneanet, FamilySearch (déontologie) | Faible |
| Justice | Légifrance, Doctrine.fr, PACER (US) | Faible |
| Académique | Google Scholar, ResearchGate (publications) | Faible |

**Workflow type.**
1. Désambiguïsation par cross-référence multi-sources.
2. Cartographie corporate (Pappers / Companies House).
3. Adverse media multi-langues.
4. Sanctions / PEP screening.
5. Profils réseaux sociaux (compte invest).
6. Synthèse cotée Admiralty.

### D.2 — Sélecteur : email

| Étape | Outils | Risque obsolescence |
|---|---|---|
| Validation format | Bibliothèques (libphonenumber pour téléphones, formats email standards) | Faible |
| Validation existence | Hunter.io, Snov.io (SMTP check) | Moyen (anti-abuse plateformes) |
| Format guessing | Hunter.io (patterns par domaine) | Faible |
| Breaches | HIBP (gratuit lookup), DeHashed (payant), IntelX (payant deep web) | Moyen |
| Comptes liés (plateformes) | Holehe (open source), Epieos (freemium), GHunt (Google spécifique) | **Élevé** (plateformes bloquent régulièrement) |
| Stealer logs | Hudson Rock (payant), SpyCloud (institutionnel) | Moyen |
| Email → personne (Google) | GHunt | **Élevé** (Google restreint) |
| WHOIS historique (pre-2018) | DomainTools (payant) | Faible |
| Forums et code | GitHub search, recherches Google avec email | Faible |
| Pastebins | IntelX, recherches manuelles | Moyen |

**Workflow type.**
1. Validation existence (Hunter.io).
2. Holehe pour cartographier comptes liés.
3. HIBP / DeHashed pour breaches.
4. Hudson Rock pour stealer logs.
5. Cross-recherche WHOIS historique si email pro/perso.

### D.3 — Sélecteur : numéro de téléphone

| Étape | Outils | Risque obsolescence |
|---|---|---|
| Validation format | libphonenumber (Google open source) | Faible |
| Opérateur / pays | Numverify, NumValidate | Faible |
| Identification publique | Truecaller (crowdsourcé, controverse) | Moyen |
| Présence WhatsApp / Telegram | Vérification compte invest (déontologie) | Moyen (plateformes évoluent) |
| Email lié | Epieos (recherche inverse) | Moyen |
| Personne | Recherches presse / réseaux sociaux | Faible |
| Adresse | Très limité légalement, variable par juridiction | Très élevé légal |

**Limites France.** Recherche directe numéro → identité **strictement limitée légalement** hors LEA. RGPD strict.

**Workflow type.**
1. Validation format et opérateur.
2. Truecaller (avec prudence sur fiabilité).
3. Vérification présence WhatsApp / Telegram (sans interaction).
4. Recherche presse / réseaux pour cohérence cible.

### D.4 — Sélecteur : username

| Étape | Outils | Risque obsolescence |
|---|---|---|
| Cross-plateformes (300+ sites) | Sherlock (open source, mises à jour communauté) | **Élevé** (plateformes bloquent) |
| Cross-plateformes alternatif | WhatsMyName (whatsmyname.app) | **Élevé** |
| Cross-plateformes commercial | NameCheckup, Knowem | Moyen |
| Profils existants confirmation | Recherches directes plateforme + Hunchly | Faible |
| GitHub | Recherche directe + Hunter pour email lié | Faible |
| Reddit, X, Telegram | Recherche directe + observation | Moyen |
| Stylométrie | Analyse manuelle ou LLM (avec validation) | Moyen |

**Workflow type.**
1. Sherlock + WhatsMyName en complément.
2. Examen manuel de chaque hit (homonymie possible).
3. Cross-vérification par autres sélecteurs (photo, bio, date création).
4. Cotation prudente.

### D.5 — Sélecteur : photo de personne

| Étape | Outils | Risque obsolescence |
|---|---|---|
| Reverse image search | Yandex (priorité 2026), Google Lens, TinEye, Bing Visual | Faible |
| Reconnaissance faciale | PimEyes, FaceCheck.ID (cadre légal UE attentif) | **Élevé** légal (AI Act, RGPD) |
| Analyse IA / synthétique | Hive Moderation, Optic AI or Not, AI or Not | Moyen (course armement) |
| EXIF | ExifTool (standard universel) | Faible |
| Provenance | TinEye « first seen », recherche source originelle | Faible |
| ELA | Forensically, FotoForensics | Faible |
| C2PA | contentcredentials.org/verify, extensions navigateur | Faible (standard émergent) |

**Workflow type.**
1. Multi-moteurs reverse search (Yandex en priorité).
2. Détection IA (Hive + Optic + Sensity en combinaison).
3. EXIF + C2PA si disponibles.
4. ELA si suspect.
5. Reconnaissance faciale **uniquement** avec base légale documentée.
6. Cotation prudente.

### D.6 — Sélecteur : domaine

| Étape | Outils | Risque obsolescence |
|---|---|---|
| WHOIS / RDAP | `whois` CLI, RDAP query, ICANN Lookup | Faible (RGPD limite info) |
| WHOIS historique (pre-2018) | DomainTools Historical WHOIS (payant ~$95/mois) | Faible |
| DNS records | `dig`, DNSDumpster, ViewDNS.info | Faible |
| Sous-domaines passifs | Amass, subfinder, crt.sh | Faible |
| Sous-domaines actifs | Amass active mode (attention CGU) | Moyen |
| Certificats TLS | crt.sh (référence), Censys | Faible |
| Historique web | Wayback Machine, archive.today | Faible |
| Passive DNS | SecurityTrails (payant), Farsight DNSDB (industriel) | Faible |
| Technologies | Wappalyzer (extension), BuiltWith | Faible |
| Trackers / analytics | DNSlytics (reverse GA, AdSense), SpyOnWeb | Moyen |
| Capture | Hunchly (payant), SingleFile (gratuit), archive.today | Faible |
| Typosquatting | DNSTwist, URLCrazy, dnstwister.report | Faible |
| Services exposés | Shodan, Censys, FOFA, ZoomEye | Faible |

**Workflow type.**
1. WHOIS / RDAP actuel.
2. WHOIS historique si pre-2018.
3. DNS records complets.
4. crt.sh pour sous-domaines via certificats.
5. Amass + subfinder pour sous-domaines complets.
6. Wayback + archive.today pour historique contenu.
7. Wappalyzer + BuiltWith pour stack technique.
8. DNSlytics pour pivots GA / AdSense.
9. Shodan + Censys pour services exposés.
10. Capture Hunchly de chaque page critique.

### D.7 — Sélecteur : adresse IP

| Étape | Outils |
|---|---|
| Géolocalisation | ipinfo.io, MaxMind |
| ASN | bgp.he.net, bgp.tools, RIPEstat |
| Reverse hostname | DNSDumpster, ViewDNS |
| Services exposés | Shodan, Censys, FOFA, ZoomEye |
| Réputation | AbuseIPDB, GreyNoise, VirusTotal |
| Reverse IP (autres sites hébergés) | DomainTools, ViewDNS, hackertarget.com |
| Historique | Passive DNS (SecurityTrails) |

### D.8 — Sélecteur : société

| Étape | Outils |
|---|---|
| Identification | Pappers (FR), Companies House (UK), OpenCorporates (cross) |
| UBO | RBE FR, PSC UK, registres UBO nationaux, ICIJ leaks |
| Comptes annuels | Pappers, registres officiels |
| Dirigeants | Pappers + LinkedIn cross-référence |
| Groupe / filiales | Pappers graphe, Orbis (payant) |
| Sanctions | OpenSanctions, WorldCheck |
| Adverse media | Google, Brandwatch, LexisNexis |
| Infrastructure web | (voir D.6 sur domaine principal) |
| Contentieux | Légifrance, Doctrine.fr, PACER (US) |

### D.9 — Sélecteur : document (PDF, Office)

| Étape | Outils |
|---|---|
| Métadonnées | ExifTool, pdfinfo |
| OCR si scanné | Tesseract, Adobe Acrobat, ABBYY |
| Recherche full-text | grep / ripgrep, indexation Recoll |
| Provenance | C2PA viewer, recherche source originelle |
| Chemins absolus révélateurs | Analyse manuelle métadonnées |
| Auteur révélé | Champ Author EXIF / properties Office |

### D.10 — Sélecteur : image (à vérifier)

| Étape | Outils |
|---|---|
| Métadonnées | ExifTool |
| Provenance | crt.sh / C2PA viewer |
| Reverse image | Yandex, Google Lens, TinEye, Bing |
| Authentification IA | Hive Moderation, Optic AI or Not, Sensity |
| ELA | Forensically, FotoForensics |
| Géolocalisation | Manuelle Bellingcat + GeoSpy (assistance IA) |
| Chronolocation | SunCalc (shadow analysis), Wolfram Alpha (météo) |

### D.11 — Sélecteur : vidéo

| Étape | Outils |
|---|---|
| Téléchargement | yt-dlp (universel) |
| Métadonnées | ExifTool, ffprobe |
| Hash | sha256sum |
| Extraction frames | ffmpeg |
| Recherche inversée frames clés | Yandex, Google Lens |
| Détection deepfake | Sensity AI, Intel FakeCatcher, Deepware |
| Géolocalisation | Méthodes IMINT |
| Voice cloning | Resemble Detect |

### D.12 — Sélecteur : wallet crypto

| Étape | Outils |
|---|---|
| Lookup | Etherscan (ETH), Blockstream.info / Mempool (BTC), Tronscan (TRX) |
| Labellisation | Walletexplorer.com, OXT |
| Sanctions | OFAC SDN, Chainalysis Sanctions |
| Multi-chain | DeBank, Zerion |
| Approfondissement | Renvoi OSINT Crypto vFULL |

### D.13 — Sélecteur : navire (nom ou IMO)

| Étape | Outils |
|---|---|
| Position actuelle | MarineTraffic, VesselFinder |
| Historique | MarineTraffic (premium), Lloyd's List |
| Détails | Equasis (propriétaire, IMO, pavillon) |
| Photos | shipspotting.com |
| Cargaisons | Panjiva, ImportGenius (B/L publics partiel) |
| Sanctions maritimes | Tankertrackers, Windward AI |

### D.14 — Sélecteur : aéronef (immatriculation ou ICAO)

| Étape | Outils |
|---|---|
| Position actuelle | Flightradar24 (filtre), ADS-B Exchange (non filtré) |
| Photos | planespotters.net, JetPhotos |
| Registres | FAA (US), DGAC (FR), CAA (UK) |
| Historique | Aviation Safety Network |

### D.15 — Synthèse — workflow type par sélecteur

L'analyste OSINT mature développe un **réflexe** : à partir d'un sélecteur, il sait immédiatement quels outils mobiliser, dans quel ordre. Les cheat sheets ci-dessus permettent d'automatiser ce réflexe lors de la prise en main d'un nouvel outil ou d'un type de sélecteur moins fréquent.

-----


## ANNEXE E — Catalogue d'outils OSINT par usage

> **État des connaissances : mai 2026.** Catalogue à vérifier trimestriellement. Les outils marqués « risque élevé » sont susceptibles d'évolutions rapides (changement de tarification, restrictions, abandon). Pour chaque outil utilisé en enquête critique, consulter la documentation officielle au moment de l'usage. Les colonnes « Dernière vérification » et « Risque obsolescence » sont indicatives à mai 2026.

Catalogue structuré des outils essentiels mobilisés dans le cours, classés par usage. Pour chaque outil : description courte, accès (gratuit / freemium / payant), chapitre principal, dernière vérification, niveau de risque d'obsolescence.

### E.1 — Captures et préservation

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Hunchly | Payant (~130 $/an) | Capture web auto avec hash | 10, 15 | 2026-05 | Faible |
| SingleFile | Gratuit (extension) | Capture one-file HTML+resources | 15 | 2026-05 | Faible |
| Wayback Machine | Gratuit | Archive web Internet Archive | 20 | 2026-05 | Faible |
| archive.today | Gratuit | Archive web alternatif | 20 | 2026-05 | Moyen (financement) |
| FreezePage | Gratuit | Capture page web horodatée | 15 | 2026-05 | Moyen |
| ExifTool | Gratuit | Métadonnées multi-formats | 29, 45 | 2026-05 | Faible (standard) |
| OpenTimestamps | Gratuit | Horodatage blockchain | 16, 90 | 2026-05 | Faible |
| VeraCrypt | Gratuit | Chiffrement volumes | 16 | 2026-05 | Faible |

### E.2 — Moteurs et recherche

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Google | Gratuit | Standard, dorks puissants | 19 | 2026-05 | Moyen (opérateurs évolutifs) |
| DuckDuckGo | Gratuit | Privacy, !bangs | 19 | 2026-05 | Faible |
| Yandex | Gratuit | Reverse image excellent | 19, 46 | 2026-05 | Moyen (géopolitique) |
| Bing | Gratuit | Indexation différente | 19 | 2026-05 | Faible |
| Brave Search | Gratuit | Index indépendant | 19 | 2026-05 | Faible |
| Marginalia / Mojeek | Gratuit | Index alternatif | 19 | 2026-05 | Moyen |
| Internet Archive Search | Gratuit | Texte historique | 20 | 2026-05 | Faible |

### E.3 — Sociétés et corporate

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Pappers | Freemium | Standard FR | 37 | 2026-05 | Faible |
| Infogreffe | Mixte | Greffes FR officiel | 37 | 2026-05 | Faible |
| Companies House | Gratuit | Standard UK | 37 | 2026-05 | Faible |
| OpenCorporates | Freemium | Multi-juridictions (140+) | 37 | 2026-05 | Faible |
| SEC EDGAR | Gratuit | Cotées US | 37 | 2026-05 | Faible |
| ICIJ Offshore Leaks | Gratuit | Leaks consolidés | 37 | 2026-05 | Faible |
| OCCRP Aleph | Gratuit (registration) | Plateforme journalistique | 37 | 2026-05 | Faible |
| Sayari | Payant | OSINT corporate moderne | 37 | 2026-05 | Faible |
| Orbis (Bureau van Dijk) | Payant lourd | 400M sociétés mondial | 37 | 2026-05 | Faible |
| Dun & Bradstreet | Payant | Credit reporting | 37 | 2026-05 | Faible |

### E.4 — Sanctions et risque

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| OpenSanctions | Gratuit / API freemium | Standard gratuit | 38 | 2026-05 | Faible |
| OFAC SDN | Gratuit | US Treasury | 38 | 2026-05 | Faible |
| EU Sanctions Map | Gratuit | UE Commission | 38 | 2026-05 | Faible |
| OFSI consolidated list | Gratuit | UK | 38 | 2026-05 | Faible |
| WorldCheck (Refinitiv/LSEG) | Payant | Institutionnel | 38 | 2026-05 | Faible |
| Dow Jones Risk | Payant | Équivalent | 38 | 2026-05 | Faible |
| ComplyAdvantage | Payant | Moderne | 38 | 2026-05 | Faible |
| Sigma Ratings | Payant | Alternative | 38 | 2026-05 | Faible |

### E.5 — Identités et personnes

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Sherlock | Gratuit | Username cross-plateformes | 27 | 2026-05 | **Élevé** (plateformes bloquent) |
| WhatsMyName | Gratuit | Alternative Sherlock | 27 | 2026-05 | **Élevé** |
| Hunter.io | Freemium | Validation email | 27 | 2026-05 | Moyen |
| Holehe | Gratuit | Comptes liés à email | 27 | 2026-05 | **Élevé** (plateformes bloquent) |
| Epieos | Freemium | Pivots email | 27 | 2026-05 | Moyen |
| GHunt | Gratuit | Google account info | 27 | 2026-05 | **Élevé** (Google restreint) |
| HIBP | Gratuit (API payante) | Breaches | 42 | 2026-05 | Faible |
| DeHashed | Payant | Breaches profond | 42 | 2026-05 | Moyen |
| IntelX | Payant | Deep web, leaks | 42 | 2026-05 | Moyen |
| Hudson Rock | Payant | Stealer logs | 43 | 2026-05 | Moyen |
| SpyCloud | Payant institutionnel | CTI/breaches | 43 | 2026-05 | Faible |
| PimEyes | Payant | Reconnaissance faciale | 30 | 2026-05 | **Juridique élevé** (AI Act, RGPD) |
| FaceCheck.ID | Payant | Alternative | 30 | 2026-05 | **Juridique élevé** |

### E.6 — Réseaux sociaux

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| X API | Payant ($100-5000/mois) | Volume limité | 32 | 2026-05 | **Très élevé** (changements tarifaires) |
| LinkedIn Sales Navigator | Payant | Filtres avancés | 32 | 2026-05 | Moyen |
| InstaLoader | Gratuit | Instagram download | 32 | 2026-05 | **Élevé** (CGU Meta) |
| yt-dlp | Gratuit | YouTube et + | 32 | 2026-05 | Moyen (mises à jour fréquentes) |
| Telegago | Gratuit | Telegram search | 33 | 2026-05 | **Élevé** (financement) |
| TGStat | Gratuit | Stats Telegram | 33 | 2026-05 | Moyen |
| DiscordChatExporter | Gratuit | Discord export | 34 | 2026-05 | **Élevé** (CGU Discord) |
| Maltego (Casefile, free) | Gratuit / Payant | Graphes | 31 | 2026-05 | Faible |
| Gephi | Gratuit | Graphes académique | 31 | 2026-05 | Faible |
| NodeXL | Gratuit | Réseaux Excel | 31 | 2026-05 | Moyen |

### E.7 — Infrastructure et CTI

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Amass | Gratuit | Sous-domaines OWASP | 40 | 2026-05 | Faible |
| subfinder | Gratuit | Sous-domaines passifs | 40 | 2026-05 | Faible |
| crt.sh | Gratuit | Certificate Transparency | 39 | 2026-05 | Faible |
| Shodan | Freemium | Infrastructure exposée | 21, 40 | 2026-05 | Faible |
| Censys | Freemium | Alternative Shodan | 21, 40 | 2026-05 | Faible |
| FOFA / ZoomEye | Mixte | Chinois | 21 | 2026-05 | Moyen (géopolitique) |
| GreyNoise | Freemium | Bruit Internet | 40 | 2026-05 | Faible |
| DNSDumpster | Gratuit | DNS analyse | 39 | 2026-05 | Faible |
| SecurityTrails | Payant | Passive DNS historique | 39 | 2026-05 | Faible |
| DomainTools | Payant | WHOIS historique | 39 | 2026-05 | Faible |
| ViewDNS.info | Gratuit | Outils DNS | 39 | 2026-05 | Faible |
| Wappalyzer | Gratuit (extension) | Technologies | 41 | 2026-05 | Faible |
| BuiltWith | Freemium | Technologies profil | 41 | 2026-05 | Faible |
| DNSlytics | Freemium | Reverse trackers | 39 | 2026-05 | Moyen |
| DNSTwist | Gratuit | Typosquatting | 41 | 2026-05 | Faible |
| VirusTotal | Freemium | Malware analyse | 74 | 2026-05 | Faible |
| AbuseIPDB | Gratuit | IPs malveillantes | 74 | 2026-05 | Faible |
| URLhaus (abuse.ch) | Gratuit | URLs malveillantes | 74 | 2026-05 | Faible |
| MISP | Gratuit | Partage CTI | 74 | 2026-05 | Faible |

### E.8 — IMINT et GEOINT

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| ExifTool | Gratuit | Métadonnées | 45 | 2026-05 | Faible |
| Yandex Images | Gratuit | Reverse image excellent | 46 | 2026-05 | Moyen (géopolitique) |
| Google Lens | Gratuit | Reconnaissance | 46 | 2026-05 | Faible |
| TinEye | Freemium | First seen | 46 | 2026-05 | Faible |
| Bing Visual | Gratuit | Alternative | 46 | 2026-05 | Faible |
| Forensically | Gratuit | ELA, clone detection | 47 | 2026-05 | Faible |
| FotoForensics | Gratuit | ELA simple | 47 | 2026-05 | Faible |
| Hive Moderation | Freemium | IA detection | 47, 56 | 2026-05 | Moyen (course armement) |
| Optic AI or Not | Freemium | IA detection | 47, 56 | 2026-05 | Moyen |
| Sensity AI | Payant | Deepfake detection | 53, 56 | 2026-05 | Moyen |
| Intel FakeCatcher | Pro | Physiologique | 53, 56 | 2026-05 | Moyen |
| Google Maps | Gratuit | Cartographie | 48 | 2026-05 | Faible |
| Google Earth Pro | Gratuit | Satellite historique | 50 | 2026-05 | Faible |
| OpenStreetMap | Gratuit | Cartographie OSM | 48 | 2026-05 | Faible |
| Overpass Turbo | Gratuit | OSM queries | 48 | 2026-05 | Faible |
| Mapillary | Gratuit | Street View communautaire | 48 | 2026-05 | Faible |
| KartaView | Gratuit | Alternative OSM | 48 | 2026-05 | Faible |
| Sentinel Hub | Gratuit (limité) | Imagerie satellite | 50 | 2026-05 | Faible |
| Planet Labs | Payant | Imagerie quotidienne | 50 | 2026-05 | Faible |
| Maxar | Payant lourd | Très haute résolution | 50 | 2026-05 | Faible |
| SunCalc | Gratuit | Position solaire | 49 | 2026-05 | Faible |
| ShadowMap | Gratuit | Visualisation 3D ombres | 49 | 2026-05 | Faible |
| Wolfram Alpha | Freemium | Météo historique | 49 | 2026-05 | Faible |
| GeoSpy | Freemium | Géolocalisation IA | 51 | 2026-05 | Moyen (rapide évolution) |
| GeoSeer / PicArta | Freemium | Alternatives | 51 | 2026-05 | Moyen |

### E.9 — Transport

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| MarineTraffic | Freemium | AIS maritime | 52 | 2026-05 | Faible |
| VesselFinder | Freemium | Alternative | 52 | 2026-05 | Faible |
| FleetMon | Freemium | Maritime | 52 | 2026-05 | Faible |
| Equasis | Gratuit | Multi-sources navires | 52 | 2026-05 | Faible |
| Tankertrackers | Payant | Pétroliers sanctions | 52 | 2026-05 | Faible |
| Flightradar24 | Freemium | ADS-B (filtré) | 52 | 2026-05 | Faible |
| ADS-B Exchange | Gratuit | ADS-B non filtré | 52 | 2026-05 | Moyen (financement community) |
| planespotters.net | Gratuit | Photos | 52 | 2026-05 | Faible |
| Aviation Safety Network | Gratuit | Sécurité aérienne | 52 | 2026-05 | Faible |

### E.10 — Vérification et provenance

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| contentcredentials.org | Gratuit | Verify C2PA | 55 | 2026-05 | Faible |
| C2PA viewer | Gratuit (extension) | Inspecteur | 55 | 2026-05 | Faible |
| SynthID detector | Limité Google | Watermark IA | 56 | 2026-05 | Moyen (déploiement progressif) |
| GPTZero | Freemium | Détection texte IA | 56 | 2026-05 | **Élevé** (faible fiabilité reconnue) |
| Originality.AI | Payant | Détection texte IA | 56 | 2026-05 | **Élevé** (idem) |
| Copyleaks | Payant | Détection texte IA | 56 | 2026-05 | **Élevé** (idem) |
| Resemble Detect | Payant | Voix clonée | 56 | 2026-05 | Moyen |
| Information Laundromat | Gratuit | Cross-narratifs SIO | 58 | 2026-05 | Faible |
| Hamilton 2.0 | Gratuit | Monitoring RU/CN | 35 | 2026-05 | Faible |

### E.11 — IA et automatisation

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Claude (Anthropic) | Freemium / Payant | LLM analyste | 60 | 2026-05 | Moyen (générations successives) |
| ChatGPT / GPT-4 (OpenAI) | Freemium / Payant | LLM | 60 | 2026-05 | Moyen |
| Gemini (Google) | Freemium / Payant | LLM | 60 | 2026-05 | Moyen |
| Mistral | Freemium / Payant | LLM européen | 60, 65 | 2026-05 | Moyen |
| Llama 3.3 / 4 (Meta) | Open source local | LLM local | 65 | 2026-05 | Moyen (générations) |
| Qwen 2.5 / 3 (Alibaba) | Open source | LLM multilingue | 65 | 2026-05 | Moyen |
| Ollama | Gratuit | Serveur LLMs locaux | 65 | 2026-05 | Faible |
| LM Studio | Gratuit | Interface LLMs locaux | 65 | 2026-05 | Faible |
| Perplexity | Freemium | RAG search avec citations | 63 | 2026-05 | Moyen |
| LangChain | Open source | Framework agents | 67 | 2026-05 | Moyen (évolutions API) |
| CrewAI | Open source | Multi-agents | 67 | 2026-05 | Moyen |
| AutoGen (Microsoft) | Open source | Multi-agents | 67 | 2026-05 | Moyen |
| Whisper (OpenAI) | Open source | Transcription audio | 61 | 2026-05 | Faible |

### E.12 — Knowledge graphs et données

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Apache Jena | Open source | RDF/SPARQL stack | 66 | 2026-05 | Faible |
| Neo4j Community | Open source | Property graph | 66 | 2026-05 | Faible |
| Stardog | Freemium | RDF moderne | 66 | 2026-05 | Faible |
| RapidFuzz | Open source | Fuzzy matching | 68, 82 | 2026-05 | Faible |
| dedupe.io | Open source | Entity resolution | 82 | 2026-05 | Faible |
| Splink (UK gov) | Open source | Entity resolution volume | 82 | 2026-05 | Faible |
| Obsidian | Freemium | Vault markdown + graphe | 17 | 2026-05 | Faible |

### E.13 — Visualisation et timeline

| Outil | Accès | Description | Ch. | Vérif. | Risque |
|---|---|---|---|---|---|
| Gephi | Open source | Graphes | 31, 83 | 2026-05 | Faible |
| Cytoscape | Open source | Graphes biologiques | 31 | 2026-05 | Faible |
| Maltego | Freemium / Payant | OSINT graphes | 31, 83 | 2026-05 | Faible |
| Timeline Explorer (Zimmerman) | Gratuit | Timeline | 83 | 2026-05 | Faible |
| Aeon Timeline | Payant | Timeline pro | 83 | 2026-05 | Faible |
| TimelineJS (Knightlab) | Gratuit | Timeline web publish | 83 | 2026-05 | Faible |

### E.14 — Outils à risque obsolescence Très Élevé (vigilance)

Liste des outils dont l'accès / l'existence est particulièrement volatile en 2026, à surveiller au moment de l'enquête :

| Outil | Usage typique | Statut mai 2026 | Alternative |
|---|---|---|---|
| **Nitter** | Miroir X/Twitter | Quasi tous instances down | yt-dlp pour vidéos, archive.today, X API payante |
| **Pushshift** | Reddit archive | Restreint à modérateurs/chercheurs | API Reddit officielle (payante), undelete.pullpush (mirror partiel) |
| **Holehe** | Comptes liés email | Fonctionne partiellement, plateformes bloquent | Combinaisons manuelles, Epieos |
| **GHunt** | Google account info | Restreint régulièrement par Google | Pivots indirects, recherche manuelle |
| **InstaLoader** | Instagram download | Risque CGU Meta, blocages fréquents | Compte invest + Hunchly |
| **Sherlock** | Username cross-plateformes | Mises à jour communauté nécessaires | WhatsMyName en complément |
| **Diverses instances Searx, Whoogle** | Privacy search | Instances ouvrent/ferment | Self-host, multi-instances |
| **CrowdTangle (Meta)** | Recherche réseau social | **Fermé août 2024** | Meta Content Library (chercheurs), Brandwatch |
| **Plus de 50 % des outils crypto on-chain gratuits 2021-2023** | Clustering, attribution | Payants ou abandonnés | Etherscan, Walletexplorer, services payants |

**Discipline.** Tester tout outil sensible **avant** d'en dépendre dans une enquête critique. Documenter l'état au moment de l'usage. Identifier au moins une alternative pour chaque outil critique du parc.

### E.15 — Politique de mise à jour

L'écosystème OSINT évolue **mensuellement**. L'analyste révise son catalogue d'outils **au minimum tous les trimestres** :
- Quels outils n'ont plus de support / sont obsolètes ?
- Quels nouveaux outils sont apparus ?
- Quels outils ont changé de modèle (gratuit → payant) ?
- Quelles modifications d'API ou de fonctionnalités ?

Sources de veille : Bellingcat resources, OSINT Framework, OSINT Combine, Trace Labs, communautés Discord et Reddit (/r/OSINT, /r/cybersecurity).

-----


## ANNEXE F — Checklist OPSEC

Checklist opérationnelle d'OPSEC à appliquer pour toute enquête OSINT. À adapter au niveau de menace (cible peu équipée vs cible étatique).

### F.1 — Avant l'enquête : préparation

**Matériel.**
- [ ] Machine d'investigation dédiée (physique ou VM cloisonnée).
- [ ] Disque dur chiffré (VeraCrypt ou équivalent).
- [ ] Sauvegarde chiffrée 3-2-1.
- [ ] Câble réseau ou Wi-Fi dédié (pas Wi-Fi personnel).

**Réseau.**
- [ ] VPN no-log auditésuite, payé via moyens non-traçants si menace élevée.
- [ ] Tor Browser installé sur VM dédiée.
- [ ] Killswitch VPN activé (déconnexion auto si VPN tombe).
- [ ] DNS over HTTPS / DNS chiffrés (NextDNS, Cloudflare 1.1.1.1).

**Navigateurs.**
- [ ] Profils navigateur séparés (Firefox profils, Brave profils).
- [ ] Extensions privacy (uBlock, Privacy Badger, Cookie AutoDelete).
- [ ] Mode privé activé par défaut.
- [ ] Pas d'extension non vérifiée (risque exfiltration).
- [ ] User-Agent réaliste (pas custom révélateur).

**Comptes d'investigation.**
- [ ] Comptes matures (créés 6-12 mois avant usage critique).
- [ ] Email burner dédié (ProtonMail / Tutanota).
- [ ] Numéros virtuels pour SMS confirmation (TextNow, etc.).
- [ ] Photos avatars cohérentes (pas IA détectable au premier coup).
- [ ] Cohérence biographique entre plateformes.

### F.2 — Pendant l'enquête : pratique

**Captures.**
- [ ] Hunchly activé (toutes pages d'enquête capturées).
- [ ] Hashes calculés sur chaque pièce critique.
- [ ] Horodatage qualifié (OpenTimestamps) sur pièces sensibles.
- [ ] Pas d'usage d'outils en SaaS pour pièces sensibles (préférer locaux).

**Requêtes.**
- [ ] Pas d'usage de Google / Bing direct pour cibles sensibles (privilégier Yandex, DuckDuckGo, ou via Tor).
- [ ] Pas d'usage de WHOIS via service sans VPN.
- [ ] Pas d'usage de Shodan / Censys directement depuis IP traçable à l'analyste.
- [ ] LLMs cloud (Claude, GPT) uniquement pour tâches non-sensibles ; sensibles → LLM local.

**Interactions.**
- [ ] Pas d'interaction directe avec cible (likes, comments, follows) — observation passive uniquement.
- [ ] Pas de message direct.
- [ ] Pas de demande d'amitié / connexion.

**Fichiers.**
- [ ] EXIF strippés sur tout fichier transmis hors workspace chiffré.
- [ ] Aucun fichier non chiffré sur cloud public.
- [ ] Hashage avant transmission, vérification à réception.

### F.3 — Communications

**Avec commanditaire.**
- [ ] Email chiffré (PGP/GPG ou S/MIME).
- [ ] Signal (chiffrement bout en bout).
- [ ] Plateforme dédiée (Tresorit Send, OnionShare).
- [ ] Pas de SMS pour information sensible.
- [ ] Confirmation à réception.

**Stockage des communications.**
- [ ] Chiffrement local.
- [ ] Durée de conservation documentée.
- [ ] Purge programmée.

### F.4 — Niveau de menace : adaptations

**Niveau 1 (cible peu équipée).** OPSEC standard suffisante.

**Niveau 2 (cible compétente).** Renforcer : LLMs locaux, VPN multi-saut, Tor pour requêtes sensibles, durcissement comptes invest.

**Niveau 3 (cible étatique).** OPSEC maximale : Tails sur USB, Whonix VM, jamais de cloud, communications PGP, devices air-gapped pour stockage, possibilité d'analyste itinérant.

**Niveau 4 (urgence vie).** Coopération avec services compétents (DGSI, gendarmerie). L'OSINT privée seule est inadéquate.

### F.5 — Après l'enquête : clôture

**Diffusion.**
- [ ] Rapport chiffré (PAdES, AES).
- [ ] Watermark destinataire si pertinent.
- [ ] TLP marqué.
- [ ] Confirmation à destinataire.

**Archivage.**
- [ ] Stockage chiffré 3-2-1.
- [ ] Durée de conservation documentée.
- [ ] Intégrité vérifiée périodiquement (re-hash).

**Purge.**
- [ ] Données personnelles purgées à fin de période (RGPD).
- [ ] Comptes d'investigation maintenus ou archivés selon usage.
- [ ] LLMs locaux : modèles téléchargés peuvent être conservés (pas de risque).
- [ ] Logs d'enquête conservés ou purgés selon mandat.

### F.6 — Erreurs OPSEC fréquentes à éviter

- Mélanger compte personnel et compte d'investigation.
- Liker / follower par erreur depuis compte invest.
- Oublier VPN sur certaines requêtes.
- Conserver fichiers non chiffrés sur disque pour « gagner du temps ».
- Cloud sync (Dropbox, OneDrive, iCloud) sur fichiers d'enquête.
- Mention du nom du commanditaire dans recherches Google.
- Photos perso accidentellement uploadées avec EXIF.
- Captures contenant URL de l'analyste dans la barre d'adresse.
- Métadonnées de fichiers (auteur Word, chemin) révélant identité analyste.

### F.7 — Audit OPSEC régulier

L'analyste / cabinet audite régulièrement (semestriellement) sa propre OPSEC :
- Test d'attaque hypothétique (que verrait un adversaire ?).
- Mise à jour des bonnes pratiques.
- Renouvellement des comptes d'investigation si compromis.
- Veille sur évolutions menaces et contre-mesures.

> **Principe.** L'OPSEC est une discipline continue, pas un état. Une enquête sans OPSEC, c'est une investigation qui se retournera tôt ou tard contre l'analyste ou son commanditaire.

-----
