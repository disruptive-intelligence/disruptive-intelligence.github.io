---
title: PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
chapter: 4
chapters: 7
---

## Chapitre 15 — Vecteurs d'accès initial : cartographie et évolution

### 15.1 — Phishing : vecteur dominant en mutation

Le phishing reste le vecteur d'accès initial le plus répandu. L'ENISA ETL 2025 le confirme comme « primary initial intrusion vector ». L'ANSSI observe que les campagnes de phishing reposent de plus en plus sur des comptes légitimes compromis, des services de création d'adresses de messagerie temporaires, ou de l'usurpation d'adresses légitimes — rendant la détection par les filtres anti-spam traditionnels plus difficile.

L'évolution principale est le passage vers le **phishing multi-canal** : combinaison d'emails, de SMS (smishing), de QR codes (quishing), et d'appels téléphoniques (vishing) dans des attaques coordonnées. Le CERT-EU anticipe pour 2026 une intensification de l'ingénierie sociale multi-canal, où les attaquants utiliseront l'IA pour orchestrer des campagnes cohérentes à travers plusieurs canaux simultanément.

Les kits **Adversary-in-the-Middle (AitM)** représentent l'innovation technique la plus significative : ils capturent les tokens de session en interceptant la communication entre la victime et le service légitime, permettant de contourner l'authentification multi-facteurs. Des kits comme **Sneaky 2FA** ciblent spécifiquement les environnements Microsoft 365 — l'environnement cloud le plus déployé dans les organisations européennes.

### 15.2 — Exploitation de vulnérabilités : le pivot vers l'infrastructure

L'exploitation de vulnérabilités logicielles est devenue le deuxième vecteur d'accès initial principal. Microsoft note que « l'exploitation de vulnérabilités reste l'une des méthodes d'accès initial les plus fiables, scalables et silencieuses pour les acteurs de la menace ».

Le fait structurant est le **pivot vers la compromission d'infrastructure**. Les attaquants ciblent de moins en moins les postes utilisateurs (via le phishing) et de plus en plus les équipements d'infrastructure : VPN (Ivanti Connect Secure, Fortinet FortiOS), firewalls (Palo Alto PAN-OS), passerelles (Citrix), serveurs de gestion (BeyondTrust, SimpleHelp). Ce pivot est stratégique parce qu'il ne dépend pas de l'interaction utilisateur, offre un accès direct au réseau interne, et cible des équipements souvent moins supervisés que les endpoints.

L'ANSSI confirme que, en 2024, « plus de la moitié des opérations de cyberdéfense de l'ANSSI, ont eu pour origine l'exploitation de vulnérabilités sur ces équipements », en 2025, les équipements de bordure restent des cibles privilégiées.

### 15.3 — La gestion des CVE : un défi croissant

Le nombre de CVE (Common Vulnerabilities and Exposures) publiées continue de croître. Le CSE canadien documente cette tendance avec des données montrant une augmentation continue des CVE par sévérité. Le délai d'exploitation diminue parallèlement : les attaques commencent « dans les jours suivant la divulgation » des vulnérabilités.

La priorisation devient un enjeu critique. Le catalogue KEV (Known Exploited Vulnerabilities) de la CISA, l'EUVD européen (Ch. 3.6), et le score EPSS (Exploit Prediction Scoring System) sont les outils de priorisation disponibles. La recommandation convergente de toutes les agences est claire : **patcher les vulnérabilités activement exploitées en priorité**, indépendamment de leur score CVSS théorique.

### 15.4 — Zero-day : marché et utilisation

Les vulnérabilités zero-day (inconnues au moment de l'exploitation) sont le vecteur le plus dangereux parce qu'il n'existe aucun patch disponible. L'ANSSI note que des acteurs chinois ont exploité des zero-day (notamment la CVE-2023-23397 par APT28 côté russe). Le marché des zero-day est un secteur où acteurs étatiques, cyber-mercenaires et cybercriminels coexistent — les États étant les principaux acheteurs via des programmes de renseignement ou des intermédiaires.

### 15.5 — Living-off-the-Land (LotL)

La technique Living-off-the-Land consiste à utiliser les outils natifs du système ciblé (PowerShell, WMI, certutil, bitsadmin sous Windows ; bash, curl, python sous Linux) plutôt que de déployer des malwares personnalisés. Cette technique rend la détection beaucoup plus difficile parce que les outils utilisés sont légitimes et leur exécution est « normale » dans l'environnement.

Volt Typhoon est l'exemple emblématique d'utilisation systématique du LotL à des fins de prépositionnement. La détection des techniques LotL nécessite une analyse comportementale — identifier les séquences d'actions anormales plutôt que la présence de fichiers malveillants — ce qui requiert des capacités de monitoring avancées (EDR, SIEM avec règles comportementales, hunting proactif).

### 15.6 — Nouveaux vecteurs émergents

Le CERT-EU anticipe pour 2026 plusieurs vecteurs émergents. **ClickFix** : fenêtres pop-up imitant des erreurs système qui guident l'utilisateur vers l'exécution d'un script malveillant copié dans le presse-papier. **QR phishing** (quishing) : QR codes malveillants dans des emails professionnels, sur des supports physiques ou dans des documents partagés. **Vishing-to-OAuth** : appels téléphoniques qui guident la victime vers une page d'authentification OAuth légitime mais avec un grant malveillant, accordant à l'attaquant un accès persistant au compte sans mot de passe ni token MFA.

---

## Chapitre 16 — L'intelligence artificielle : multiplicateur de menace et de défense

### 16.1 — L'IA comme amplificateur offensif

Microsoft documente dans son MDDR 2025 une cartographie complète des utilisations de l'IA pour augmenter les cyberattaques traditionnelles. Les domaines d'augmentation incluent : le spearphishing automatisé et personnalisé, la reconnaissance automatisée, la génération et le débogage de code malveillant, le développement d'exploits, la génération de domaines d'usurpation, l'automatisation de bots, la création d'identités synthétiques, la gestion de C2, l'obfuscation de malware, et la traduction linguistique pour des campagnes internationales.

Le CSE canadien évalue que « les technologies d'IA amplifient les menaces dans le cyberespace » — la première des cinq tendances structurantes identifiées pour 2025-2026. L'IA abaisse les barrières à l'entrée pour des acteurs moins compétents tout en augmentant l'efficacité des acteurs sophistiqués.

Le CERT-EU anticipe pour 2026 que l'IA sera utilisée à grande échelle dans les opérations de social engineering, avec des campagnes multi-canal orchestrées par IA combinant email, voix et SMS de manière cohérente et personnalisée.

### 16.2 — LLMs malveillants

L'écosystème cybercriminel a développé ses propres outils d'IA générative. **WormGPT** est un LLM sans les garde-fous des modèles commerciaux, capable de générer des emails de phishing, du code malveillant et des scripts d'arnaque. **FraudGPT** est spécialisé dans la fraude. **Xanthorox AI** est présenté comme un système autonome avec ses propres modèles de langage. Ces outils vont du simple jailbreak (contournement des filtres de sécurité des modèles commerciaux) à des systèmes dédiés.

L'impact réel de ces outils doit être évalué avec prudence. Beaucoup sont des arnaques (vendus à des prix élevés avec des capacités exagérées) ou des jailbreaks simples rapidement patchés par les fournisseurs de LLM. Cependant, la tendance de fond est claire : la mise à disposition d'outils d'IA générative sans contraintes de sécurité pour les cybercriminels.

### 16.3 — AI deepfakes : fraude et influence

Les deepfakes — contenus audio et visuels générés par IA imitant de manière réaliste des personnes réelles — posent des risques dans deux domaines.

En **fraude**, les deepfakes vocaux et visuels permettent l'usurpation d'identité à une échelle sans précédent. Le cas Hong Kong (25M USD de virement après un appel vidéo avec un deepfake du directeur financier) est l'exemple le plus documenté. Microsoft note que des profils LinkedIn avec des photos de portrait générées par IA sont utilisés pour du scraping de données ou de l'ingénierie sociale.

En **influence**, les deepfakes d'ancres de journaux télévisés (AI twinning) permettent de diffuser des narratifs étatiques avec un vernis de crédibilité. Microsoft documente l'émergence d'**acteurs AI-first** — des opérateurs d'influence qui privilégient le contenu généré par IA comme stratégie principale plutôt que comme outil secondaire.

### 16.4 — L'IA comme lure et comme cible

L'intérêt du public pour l'IA est exploité par les cybercriminels comme **lure** : faux sites imitant DeepSeek, Kling AI, Canva Dream Lab distribuent des malwares (infostealers, trojans) sous couvert d'outils d'IA gratuits. Les utilisateurs qui cherchent à accéder à des outils d'IA populaires téléchargent à la place des malwares.

L'IA est aussi une **surface d'attaque** émergente. Le **slopsquatting** exploite les hallucinations des LLMs : lorsqu'un modèle d'IA recommande un package logiciel qui n'existe pas, un attaquant crée ce package avec du code malveillant. Les **Rules File Backdoors** ciblent les assistants de code IA en injectant des instructions cachées dans les fichiers de configuration. L'**empoisonnement de modèles** consiste à injecter des données biaisées ou malveillantes dans les datasets d'entraînement.

Des vulnérabilités spécifiques ont été documentées dans les plateformes IA elles-mêmes : CVE dans Langflow (outil d'orchestration IA), vulnérabilités dans les plugins et fonctions connectées aux LLMs. Microsoft consacre une analyse aux nouvelles surfaces d'attaque créées par l'IA — prompts, données et sources de contexte, orchestration, plugins et fonctions, modèles eux-mêmes.

### 16.5 — L'IA dans les opérations d'influence étatiques

Microsoft documente une croissance significative des contenus générés par IA attribués à des adversaires étatiques. La Chine, l'Iran et la Russie utilisent tous des outils d'IA dans leurs opérations d'influence. Les techniques incluent l'**AI twinning** (création de répliques numériques de présentateurs TV de confiance), l'**empoisonnement de données d'entraînement** (injection de contenu biaisé dans les datasets qui informent les modèles d'IA), et le **clonage vocal** pour l'usurpation d'identité.

Google et Microsoft ont documenté l'utilisation de Gemini et ChatGPT par des acteurs étatiques (Chine, Iran, RPDC) pour des tâches de recherche, de rédaction et de traduction dans le cadre d'opérations cyber et d'influence.

### 16.6 — L'IA comme outil défensif

L'IA est également un multiplicateur défensif. Le CERT-EU note avoir « significativement étendu son utilisation de l'automatisation et de l'intelligence artificielle dans ses processus de monitoring et d'analyse » en 2025, élargissant sa capacité de détection. Les applications défensives incluent : la détection d'anomalies comportementales, l'automatisation du triage des alertes SOC, l'enrichissement automatisé des indicateurs, l'analyse de logs à grande échelle, et l'aide à la rédaction de rapports CTI.

Les limites doivent être explicitement reconnues. La **surreliance à l'IA** crée de nouveaux risques : les analystes qui font confiance aux résultats de l'IA sans vérification humaine introduisent des erreurs systémiques. Les **fuites d'information via prompts** sont un risque réel lorsque des données sensibles sont soumises à des LLMs commerciaux. L'**intégrité des modèles** ne peut être présumée — les modèles sont soumis aux mêmes risques supply chain que tout autre logiciel.

### 16.7 — 🔴 Fil rouge : IA augmentée dans la production CTI

> **📌 FIL ROUGE — Épisode 16**
>
> Sophie intègre un outil de CTI augmentée par IA dans son workflow de production — un LLM fine-tuné pour l'analyse de rapports de menace, capable de résumer les publications, d'extraire les IOCs et de proposer des corrélations. Le gain d'efficacité est réel : le traitement de 20 rapports quotidiens passe de 3 heures à 45 minutes.
>
> Mais les limites apparaissent rapidement. L'outil halluciné un lien entre un IOC et un groupe APT qui n'existe pas dans les sources. Un analyste junior reprend cette hallucination dans un draft de note CTI sans vérifier. Sophie intercepte l'erreur lors de la revue. Elle établit une règle : « L'IA est un assistant, pas un analyste. Tout output IA doit être vérifié par un humain avant intégration dans un produit CTI. Les corrélations proposées par l'IA sont des hypothèses à vérifier, jamais des conclusions. »

---

## Chapitre 17 — Compromission de la chaîne d'approvisionnement

### 17.1 — Anatomie d'une supply chain attack

Les attaques supply chain exploitent les relations de confiance entre une organisation et ses fournisseurs, sous-traitants ou partenaires. Le principe est simple : plutôt que d'attaquer directement une cible bien défendue, compromettre un fournisseur moins protégé qui dispose d'un accès au réseau de la cible. L'ANSSI note que « ces attaques, qui sont en constante expansion depuis la fin des années 2010, illustrent combien la maîtrise du SI, de ses interconnexions et de ses dépendances est un enjeu majeur pour les organisations ».

Les vecteurs de supply chain attack se déclinent en trois catégories principales. La **supply chain logicielle** cible les composants logiciels (bibliothèques, packages, mises à jour). La **supply chain des services** cible les prestataires de services IT (MSP, hébergeurs, éditeurs SaaS). La **supply chain matérielle/physique** cible les composants physiques (COTS embarqués, équipements réseau). Le CSE canadien note l'émergence de **double supply chain attacks** — « une attaque supply chain qui en permet une autre ».

### 17.2 — Supply chain logicielle : empoisonnement de packages

L'empoisonnement de packages dans les registres publics (npm, PyPI, RubyGems) est un vecteur en croissance. Les attaquants publient des packages malveillants portant des noms similaires à des packages légitimes populaires (typosquatting) ou créent des packages dont les noms correspondent aux hallucinations de LLMs (slopsquatting).

Le cas **Shai-Hulud** (2025) illustre la sophistication croissante : un package malveillant distribué via npm avec des mécanismes d'évasion avancés. Les **Rules File Backdoors** ciblent les assistants de code IA en injectant des instructions cachées dans les fichiers de configuration des projets.

### 17.3 — Supply chain des services : le cas des prestataires IT

L'ANSSI documente de manière détaillée les cas de compromission en cascade via les prestataires en 2025. « L'ANSSI a été témoin de nombreuses compromissions d'entités par des attaquants en mesure de se latéraliser depuis les systèmes d'information de prestataires vers des clients. À titre d'exemple, un attaquant a compromis et exfiltré des ressources clientes chez un prestataire de nombreuses entités françaises. En tirant parti des interconnexions existantes avec les systèmes d'information des clients et grâce à des authentifiants volés, l'attaquant est parvenu à se latéraliser sur le système d'information de plusieurs clients. »

L'ANSSI a également été témoin de « plusieurs compromissions par rançongiciel de prestataires causant des impacts forts sur les clients ». Le schéma est récurrent : compromission du prestataire → latéralisation via les interconnexions réseau ou les credentials partagées → compromission des clients.

Les **services SaaS** ajoutent une dimension : les API, extensions de marketplace et grants OAuth cross-platform créent des vecteurs de supply chain spécifiques au cloud. Un grant OAuth malveillant peut donner à un attaquant un accès persistant aux données d'une organisation sans jamais compromettre ses credentials.

### 17.4 — Concentration des fournisseurs comme risque systémique

Le CSE canadien identifie la « concentration des fournisseurs » comme l'une des cinq tendances structurantes. La dépendance d'un grand nombre d'organisations aux mêmes fournisseurs de services cloud, de sécurité ou d'infrastructure crée des **points de défaillance uniques** (single points of failure). L'incident CrowdStrike de juillet 2024 — une mise à jour défectueuse ayant paralysé des millions de systèmes Windows dans le monde — illustre ce risque systémique, même en l'absence de cyberattaque.

### 17.5 — SBOM et hygiène des dépendances

Les Software Bills of Materials (SBOM) — inventaires exhaustifs des composants logiciels d'un produit — sont promus par le CRA européen et les régulateurs américains comme outil de transparence et de gestion des risques supply chain. Les SBOM permettent de savoir, lorsqu'une vulnérabilité est découverte dans un composant, quels produits sont affectés. Leur adoption reste cependant inégale, et la gestion opérationnelle des SBOM (mise à jour, corrélation avec les bases de vulnérabilités, intégration dans les processus de patching) est un défi non trivial.

### 17.6 — 🔴 Fil rouge : la surprise — convergence étatique-criminel

> **📌 FIL ROUGE — Épisode 17**
>
> L'investigation sur l'incident du prestataire (Ch. 11) réserve la surprise annoncée. L'analyse forensique approfondie du SI d'EuroDefense révèle, en plus des traces de l'affilié Qilin (ransomware), la présence d'un implant **ShadowPad** sur un serveur de gestion de contrats OTAN — un outil historiquement associé à l'espionnage chinois. L'implant est différent du ransomware : il est discret, persistent, et configuré pour l'exfiltration de données, pas pour le chiffrement.
>
> Deux hypothèses se forment :
> — Hypothèse A : un acteur étatique chinois a exploité le même accès initial que l'affilié Qilin (les credentials du prestataire), indépendamment de l'attaque ransomware. C'est le scénario de « victimes multiples du même IAB ».
> — Hypothèse B : l'affilié Qilin est lui-même un opérateur hybride mêlant ransomware (gain financier) et espionnage (pour un commanditaire étatique). C'est le scénario NailoLocker/ShadowPad documenté par l'ANSSI et Orange CyberDefense.
>
> Sophie ne peut pas trancher entre les deux hypothèses avec les données disponibles. Elle rédige un assessment à confiance basse distinguant explicitement les deux scénarios et recommande une escalade vers l'ANSSI (qui a l'expertise et les données comparatives nécessaires). Le RSSI Marc Vidal réalise la gravité : « Si c'est le scénario B, on n'est pas face à un simple ransomware — on est face à une opération d'espionnage étatique qui utilise le ransomware comme couverture. »

---

## Chapitre 18 — Hacktivisme, menaces hybrides et opérations d'influence

### 18.1 — La résurgence hacktiviste 2025

L'ENISA ETL 2025 documente que le hacktivisme représente une part très significative des incidents enregistrés contre l'UE. Les attaques DDoS hacktivistes constituent 81,4% des menaces les plus prévalentes tous secteurs confondus. L'administration publique est le secteur le plus ciblé (96,2% des incidents dans ce secteur sont des DDoS hacktivistes).

Cependant, l'impact opérationnel reste généralement limité : les sites web ciblés sont indisponibles pendant quelques heures, les services sont perturbés temporairement, mais les dommages structurels sont rares. La nuance analytique est essentielle : **volume élevé d'incidents ne signifie pas impact élevé**. Un CTL qui compte les incidents DDoS hacktivistes au même niveau que les compromissions d'espionnage étatique produit une image déformée du paysage de menace.

### 18.2 — Les alliances hacktivistes et la montée en capacité OT

L'écosystème hacktiviste a évolué vers des alliances transversales. La **Holy League**, annoncée en juillet 2024, rassemblerait 70 groupes incluant des acteurs pro-russes (NoName057(16)) et pro-palestiniens, ciblant l'Ukraine, Israël et les pays perçus comme les soutenant. L'**Union du 7 octobre** et d'autres alliances bilatérales complètent ce paysage.

La montée en capacité la plus préoccupante est le **ciblage OT** par les hacktivistes. **Z-PENTEST-ALLIANCE** s'est positionné comme le principal groupe hacktiviste ciblant les infrastructures critiques dans l'UE, avec un focus sur les infrastructures énergétiques. Le groupe partage des vidéos montrant des opérateurs manipulant des interfaces de systèmes OT — un acte de communication visant à amplifier l'impact psychologique. L'Italie est documentée comme l'État membre le plus fréquemment ciblé par les attaques OT hacktivistes, suivie de la Tchéquie, la France et l'Espagne.

L'**Infrastructure Destruction Squad (IDS)**, apparu en juin 2025, a développé le malware ICS **VoltRuptor**, décrit comme offrant un support multi-protocole et des capacités avancées de persistance et d'anti-forensique. VoltRuptor est disponible à la vente sur le dark web. L'ENISA note que l'attribution de l'IDS à un ensemble d'intrusion Russia-nexus est une « hypothèse de travail réaliste ».

### 18.3 — Opérations d'influence et interférence numérique

La convergence entre opérations cyber et opérations d'influence est l'un des phénomènes les plus structurants documentés dans le corpus. Cette convergence prend plusieurs formes.

Le **hack-and-leak** combine l'intrusion technique (vol de documents) avec la manipulation informationnelle (diffusion sélective des documents pour créer un narratif). Le **cyber-enabled influence operation** utilise les capacités cyber pour amplifier des campagnes de désinformation — création de faux sites, automatisation de la diffusion, génération de contenu par IA.

Les cas documentés incluent les manipulations ciblant l'élection présidentielle roumaine de 2024 (promotion artificielle de contenus sur TikTok), les DDoS ciblant les sites de partis politiques danois le jour des élections, et les campagnes de désinformation russes utilisant des répliques IA de présentateurs TV.

VIGINUM (France) est l'opérateur étatique chargé de détecter et caractériser les ingérences numériques étrangères. L'ANSSI et VIGINUM travaillent en coordination, l'ANSSI traitant le volet technique (intrusions) et VIGINUM le volet informationnel (manipulation).

### 18.4 — 🔴 Fil rouge : DDoS + désinformation sur un contrat OTAN

> **📌 FIL ROUGE — Épisode 18**
>
> En septembre 2025, EuroDefense annonce l'obtention d'un contrat OTAN majeur pour des systèmes de surveillance aérienne. Le jour de l'annonce, trois événements simultanés :
>
> 1. Une campagne DDoS sous le hashtag #OPDefense rend indisponibles les portails web publics d'EuroDefense pendant 4 heures. Revendiquée par NoName057(16) et relayée par le Telegram de la Holy League.
> 2. Un compte Twitter/X se présentant comme un « lanceur d'alerte interne » publie des documents prétendument confidentiels sur les coûts du contrat — les documents sont des faux, mais suffisamment crédibles pour être repris par des médias marginaux.
> 3. Un article sur un site de « pink slime » (faux site d'information local) allègue que le système de surveillance a des « failles de sécurité connues non corrigées » — information invérifiable mais anxiogène.
>
> Sophie identifie l'opération comme une campagne hybride coordonnée : la composante cyber (DDoS) est le signal visible, la composante informationnelle (faux documents, faux article) est le payload réel. L'objectif n'est pas de paralyser EuroDefense mais de **discréditer le contrat** et d'**éroder la confiance** dans le groupe. Elle coordonne avec VIGINUM pour la caractérisation de l'ingérence informationnelle et recommande au service communication d'EuroDefense de préparer une réponse factuelle ciblée.

---

## Chapitre 19 — Menaces sur le spatial : cybersécurité des systèmes satellitaires

### 19.1 — L'espace comme infrastructure critique

Le secteur spatial est désormais reconnu comme infrastructure critique par NIS2. Les dépendances sont massives : télécommunications (Starlink, constellations commerciales), navigation (GPS, Galileo), observation (imagerie satellite), défense (communications militaires, renseignement), et services financiers (synchronisation temporelle pour le trading haute fréquence). La compromission d'un système satellite peut avoir des effets en cascade sur l'ensemble des secteurs dépendants.

### 19.2 — Taxonomie des menaces spatiales

L'ENISA Space Threat Landscape 2025 fournit la première taxonomie systématique des menaces cyber pesant sur les systèmes satellitaires. La taxonomie distingue les menaces par segment (sol, spatial, utilisateur), par catégorie (activités malveillantes, écoute/interception, attaques physiques, défaillances, legacy), et par impact (confidentialité, intégrité, disponibilité).

Les menaces identifiées incluent : l'injection de code malveillant dans les logiciels embarqués (OBSW), l'exploitation de vulnérabilités dans les systèmes de contrôle au sol, l'interception des communications satellite (TM/TC), le détournement de satellite (hijacking), et les attaques physiques (y compris les armes anti-satellite ASAT). L'utilisation croissante de composants commerciaux (COTS) dans les satellites ajoute les risques classiques de la supply chain logicielle au domaine spatial.

### 19.3 — Scénarios d'attaque documentés

L'ENISA documente deux scénarios d'attaque détaillés.

**Scénario 1 — Compromission du centre de contrôle** : spearphishing ciblant un employé du centre de contrôle → installation d'un malware → reconnaissance réseau → mouvement latéral vers les systèmes de contrôle satellite → vol de credentials → accès aux configurations d'antenne et aux protocoles de communication → exfiltration de données sensibles (protocoles de communication, clés de chiffrement) → capacité de corruption du bus satellite et de la charge utile.

**Scénario 2 — Exploitation OBC/OBSW via code malveillant physique** : accès physique non autorisé à la chaîne d'assemblage ou au conteneur de transport du satellite → implantation de code malveillant via un port IO (USB) → exploitation des misconfiguration du logiciel embarqué → injection de données aléatoires provoquant l'épuisement des ressources du système temps réel (RTOS) → perte de contrôle du segment spatial.

### 19.4 — Cadre de contrôles et régulation

L'ENISA propose un cadre de contrôles de cybersécurité spécifiques au spatial, incluant : la gestion des risques et l'analyse d'impact, la sécurité par conception et par défaut (SDLC), la sécurité physique et environnementale (protection des composants pendant le transport et l'assemblage), la sécurité réseau (segmentation, chiffrement authentifié, désactivation des ports physiques non critiques), et la réponse à incidents adaptée au spatial.

Le cadre normatif inclut : NIS2 (espace comme secteur critique), CRA (sécurité des produits numériques), ECSS (standardisation spatiale européenne), BSI TR-03184 (guide de protection des infrastructures spatiales), NIST IR 8270/8323/8401, et les frameworks SPARTA/SPACE-SHIELD (basés sur MITRE ATT&CK adaptés au domaine spatial).

### 19.5 — 🔴 Fil rouge : audit spatial

> **📌 FIL ROUGE — Épisode 19**
>
> La branche satellite d'EuroDefense développe un composant de charge utile pour un satellite d'observation européen. Le responsable programme demande à Sophie une analyse de risque cyber. En utilisant le Space Threat Landscape ENISA et le framework SPARTA, Sophie identifie trois risques prioritaires : (1) compromission de la supply chain des composants COTS embarqués, (2) attaque sur le centre de contrôle au sol via spearphishing, (3) exploitation de vulnérabilités dans le logiciel de simulation utilisé pendant la phase d'assemblage. Elle recommande un audit de sécurité des fournisseurs COTS, une segmentation réseau stricte entre les systèmes de simulation et le réseau corporate, et un programme de sensibilisation spécifique pour le personnel du centre de contrôle.

---

## Chapitre 20 — Technologies opérationnelles (OT/ICS) et convergence IT-OT

### 20.1 — Le ciblage des systèmes industriels

Les systèmes OT (Operational Technology) et ICS (Industrial Control Systems) contrôlent les processus physiques dans les secteurs énergie, eau, transport, industrie manufacturière et infrastructures critiques. Leur compromission peut avoir des conséquences physiques directes — coupures d'électricité, perturbation de la distribution d'eau, arrêt de lignes de production.

Le ciblage OT émane de trois catégories d'acteurs. Les **acteurs étatiques** (Sandworm/GRU, Volt Typhoon/Chine, Cyber Av3ngers/Iran) ciblent l'OT pour le prépositionnement ou le sabotage. Les **hacktivistes** (Z-PENTEST-ALLIANCE, IDS) ciblent l'OT pour l'impact psychologique et la démonstration de capacité. Les **ransomware** ciblent l'OT comme extension de la compromission IT — le chiffrement de systèmes IT de gestion peut paralyser les opérations OT même sans ciblage direct des contrôleurs.

### 20.2 — L'attaque destructive contre les infrastructures électriques polonaises

L'attaque de fin 2025 contre les infrastructures électriques polonaises est l'événement OT le plus significatif de la période. L'ANSSI la décrit comme « une première pour un État membre de l'Union européenne » — un seuil franchi qui matérialise le scénario de cyberattaque destructive sur les infrastructures critiques européennes. L'objectif était de « provoquer des coupures d'électricité et de chauffage pour un nombre conséquent de citoyens ».

Cet événement place la menace OT dans une catégorie différente du hacktivisme démonstratif : il s'agit d'une tentative de **sabotage à effet physique**, potentiellement attribuable à un acteur étatique. L'ANSSI note que la France se prépare à une « augmentation massive — d'ici 2030 — des attaques hybrides avec des effets concrets voire destructeurs sur nos infrastructures critiques ».

### 20.3 — Convergence IT-OT : risques et remédiation

La convergence IT-OT — l'interconnexion croissante des réseaux industriels avec les réseaux informatiques d'entreprise — crée de nouvelles surfaces d'attaque. Un attaquant qui compromet le réseau IT corporate peut potentiellement pivoter vers le réseau OT si la segmentation est insuffisante. Les cas documentés par l'ANSSI incluent des ransomware déployés sur les réseaux IT de prestataires qui ont impacté les opérations OT de leurs clients.

Les particularités de la sécurité OT compliquent la remédiation : les systèmes ont des cycles de vie longs (15-30 ans), utilisent des protocoles propriétaires ou legacy, ne supportent pas toujours les mises à jour de sécurité, et fonctionnent sous des contraintes de disponibilité extrêmes (24/7, pas de fenêtre de maintenance). L'ASD australien opère des programmes spécifiques de cybersécurité OT — le Critical Infrastructure Uplift Program (CI-UP) — qui fournissent des services d'audit, de durcissement et de formation aux opérateurs d'infrastructures critiques.

### 20.4 — 🔴 Fil rouge : scan OT par Z-PENTEST-ALLIANCE

> **📌 FIL ROUGE — Épisode 20**
>
> En octobre 2025, le SOC d'EuroDefense détecte des scans réseau ciblant les interfaces de gestion d'un système SCADA dans l'usine de production aéronautique du groupe. Les adresses IP source correspondent à un range associé à Z-PENTEST-ALLIANCE dans un feed CTI. Le système SCADA est accessible depuis un segment réseau qui n'aurait pas dû être exposé — une erreur de configuration découverte lors de l'incident.
>
> Sophie évalue : l'impact potentiel est limité (les scans n'ont pas abouti à une intrusion), mais le risque réputationnel est élevé (Z-PENTEST-ALLIANCE publie des vidéos de ses intrusions OT sur Telegram). Elle recommande : correction immédiate de la segmentation réseau, audit complet de la surface OT exposée, et mise en place d'un monitoring spécifique OT (IDS industriel). Elle note dans son CTL : « La menace hacktiviste sur l'OT d'EuroDefense est réelle mais actuellement limitée en impact. Le risque principal n'est pas le hacktivisme lui-même mais les déficiences de segmentation qu'il révèle — déficiences qui pourraient être exploitées par un acteur étatique avec des capacités et des intentions très différentes. »

> **🎯 CAPSTONE Partie IV** : Pour une organisation industrielle multi-sectorielle (défense/spatial/industrie), cartographier les 10 vecteurs d'attaque les plus pertinents, évaluer les 3 tendances émergentes les plus préoccupantes (horizon 18 mois), et formuler 5 recommandations d'anticipation priorisées P0/P1/P2 avec justification fondée sur la menace réelle.

---
