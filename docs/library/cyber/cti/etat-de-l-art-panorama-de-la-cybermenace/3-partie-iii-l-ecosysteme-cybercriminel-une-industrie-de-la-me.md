---
title: 'PARTIE III — L''écosystème cybercriminel : une industrie de la menace'
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
chapter: 3
chapters: 7
---

## Chapitre 10 — Structure et dynamiques de l'écosystème cybercriminel

### 10.1 — Le modèle Crime-as-a-Service (CaaS)

L'écosystème cybercriminel contemporain fonctionne comme une **économie de services industrialisée**. Le modèle Crime-as-a-Service (CaaS) permet à des acteurs ayant des compétences limitées de mener des attaques sophistiquées en achetant ou louant les capacités nécessaires auprès de fournisseurs spécialisés. Ce modèle, documenté de manière convergente par Europol (IOCTA/SOCTA 2025), l'ASD, le CSE canadien et Microsoft, est le facteur structurant principal de la menace cybercriminelle.

L'ASD détaille les services de l'écosystème CaaS : le **courtage d'accès initial** (vente de credentials et d'accès réseau), le **développement de ransomware** (programmes RaaS avec portail web et service client), le **crypting** (services d'obfuscation de malware pour contourner la détection), l'**hébergement bulletproof** (infrastructure réseau résistante aux takedowns), et le **blanchiment de cryptomonnaies** (services de mixing et de tumbling).

Le CSE canadien évalue que « la popularité continue du RaaS contribue presque certainement à l'augmentation des incidents de ransomware en abaissant les barrières techniques à l'entrée ». En d'autres termes, le CaaS démocratise la cybercriminalité : un acteur sans compétence technique peut acheter un accès initial sur un forum, louer un programme ransomware, et lancer une attaque contre une cible — tout en partageant les revenus avec les fournisseurs de chaque service.

### 10.2 — La chaîne de valeur criminelle

La chaîne de valeur cybercriminelle peut être décomposée en maillons spécialisés, chacun opéré par des acteurs distincts qui interagissent via des marketplaces et des forums.

Les **développeurs de malware** créent les outils — ransomware, infostealers, loaders, backdoors. Ils vendent leurs produits via des programmes RaaS/MaaS (Malware-as-a-Service) ou directement sur des forums. Les **opérateurs d'infrastructure** fournissent les hébergements bulletproof, les domaines résistants aux takedowns et les réseaux de proxy. Les **courtiers en accès initial (IAB)** vendent des accès déjà établis dans les réseaux de victimes. Les **affiliés ransomware** achètent ces accès et déploient le ransomware. Les **services de blanchiment** convertissent les cryptomonnaies extorquées en fonds utilisables.

Europol souligne que l'accès aux systèmes compromis est devenu « une marchandise dans l'économie CaaS, avec des accès vendus en gros ou aux enchères sur des forums du dark web ». Une victime compromise peut être soumise à « plusieurs cyberattaques simultanées ou consécutives » par différents acteurs ayant acheté l'accès au même vendeur.

### 10.3 — Forums, marketplaces et messageries chiffrées

L'infrastructure du marché noir cybercriminel a évolué sous la pression des forces de l'ordre. Les grands forums centralisés (comme les défunts Genesis Market ou BreachForums dans sa première incarnation) ont cédé du terrain aux **messageries chiffrées de bout en bout (E2EE)**. Europol note que les applications de communication chiffrées sont « de plus en plus utilisées pour négocier, faire la promotion et effectuer des transactions commerciales concernant des données piratées ».

Cette migration vers les messageries E2EE pose un défi majeur pour les forces de l'ordre : le chiffrement empêche l'interception des communications, et la nature éphémère des conversations complique la collecte de preuves. Le démantèlement de la plateforme Ghost en septembre 2024 illustre les efforts internationaux pour contrer ces canaux de communication criminels.

Les courtiers en données « font connaître leur activité sur plusieurs plateformes afin de diversifier leurs opérations et d'accroître leur résilience face aux opérations répressives » — une stratégie de multi-plateforme qui complique les takedowns.

### 10.4 — Les données volées comme marchandise centrale

L'IOCTA 2025 d'Europol est titré « Steal, Deal and Repeat » — voler, vendre, recommencer — une formulation qui résume l'économie des données volées. Les données compromises sont « très précieuses pour un vaste éventail d'acteurs criminels, qui les exploitent comme une marchandise à part entière, mais également comme un bien à acquérir à d'autres fins, y compris d'autres activités criminelles ».

Les données volées alimentent l'ensemble de l'écosystème : les credentials volées par les infostealers sont vendues aux IAB, qui les revendent aux affiliés ransomware. Les données personnelles volées lors de data breaches sont utilisées pour des fraudes d'identité, du phishing ciblé, ou de l'extorsion directe des victimes. L'ENISA documente que 68,6% des intrusions enregistrées ont conduit à des data breaches publiées sur des forums cybercriminels.

### 10.5 — Fragmentation post-disruptions

Le paysage cybercriminel a été significativement perturbé par les opérations de law enforcement en 2024-2025. Les takedowns de LockBit (février 2024), ALPHV/BlackCat (décembre 2023) et Hive (janvier 2023) ont éliminé ou dégradé les groupes ransomware les plus prolifiques. L'opération Endgame (mai 2025) a ciblé les botnets et droppers qui servent d'infrastructure commune à de nombreuses opérations.

L'effet net est paradoxal : les grandes opérations de disruption ont **fragmenté** l'écosystème plutôt que de le réduire. L'ENISA observe qu'« une transition dans l'écosystème ransomware a été observée, marquée par une fragmentation continue, conduisant à l'émergence de nouvelles variants et de nouveaux programmes RaaS ». 82 variants de ransomware ont été déployées contre l'UE sur la période de reporting — un nombre significativement plus élevé que lorsque quelques groupes dominants centralisaient le marché.

Europol note que « le paysage de la cybercriminalité est devenu plus fragmenté, avec des durées de vie plus courtes pour les marketplaces et les groupes ransomware, rendant l'attribution des acteurs de la menace plus difficile ».

### 10.6 — Recrutement et rajeunissement

Europol et le CSE documentent un phénomène préoccupant : le recrutement de jeunes adultes et d'adolescents techniquement compétents par les réseaux cybercriminels. La SOCTA 2025 note que « la récession économique, l'instabilité géopolitique et le creusement des inégalités mondiales ont augmenté les incitations pour les individus à s'engager dans la cybercriminalité financièrement motivée. Les adolescents et jeunes adultes techniquement compétents sont particulièrement susceptibles au recrutement par les réseaux criminels. »

Ce rajeunissement a des implications pour la réponse : les outils de disruption conçus pour démanteler des organisations criminelles structurées sont moins efficaces contre des individus isolés ou des petits groupes éphémères.

### 10.7 — 🔴 Fil rouge : credentials en vente sur un forum

> **📌 FIL ROUGE — Épisode 10**
>
> En juin 2025, un analyste de l'équipe de Sophie repère sur un forum underground une annonce vendant des accès VPN à une « entreprise européenne aéronautique ». Le prix demandé : 15 000 dollars en Bitcoin. L'annonce inclut une capture d'écran montrant un portail VPN — et le logo est celui d'un sous-traitant de niveau 2 d'EuroDefense.
>
> Sophie évalue : l'accès a probablement été obtenu via un infostealer (les credentials VPN sont le type d'accès le plus fréquemment vendu par les IAB). Si un affilié ransomware achète cet accès, l'attaque peut se matérialiser en jours. Plus préoccupant : ce sous-traitant a une interconnexion réseau avec le SI d'EuroDefense pour la gestion de projets conjoints.
>
> Elle déclenche une procédure d'urgence : notification du sous-traitant, reset des credentials partagées, audit des connexions entre le sous-traitant et le réseau EuroDefense, et surveillance renforcée des flux entre les deux réseaux. Elle note dans son CTL en cours de rédaction : « La supply chain IT constitue le vecteur de risque principal pour EuroDefense — non pas parce que nos propres défenses sont faibles, mais parce que nos sous-traitants sont le maillon le plus exposé. »

---

## Chapitre 11 — Ransomware : anatomie d'une menace persistante et fragmentée

### 11.1 — État des lieux 2025

Le ransomware reste la menace cybercriminelle la plus directement impactante. L'ENISA documente que 81,1% des activités cybercriminelles ciblant les organisations EU impliquent du ransomware. Le FBI IC3 rapporte que le secteur healthcare/public health a reçu le plus de signalements ransomware (460 incidents), suivi des services financiers critiques (258) et de l'industrie manufacturière (189).

Le paysage est devenu plus fragmenté et compétitif. Là où LockBit dominait avec près d'un quart de toutes les revendications en 2023-2024, l'écosystème 2025 est plus éclaté : **Akira** est le variant le plus fréquemment déployé contre l'UE (11,6%), suivi de **SafePay** (10,1%) et **Qilin** (7,5%). LockBit, après la compromission de son panel d'affiliation en mai 2025 et la fuite de sa base de données interne, semble avoir cessé ses activités — remplacé par un opérateur appelé Syrphid utilisant LockBit4. BlackBasta a cessé de revendiquer des incidents depuis janvier 2025. 8Base a vu ses déploiements diminuer après des fuites d'infrastructure et des arrestations d'administrateurs.

**DragonForce** émerge comme un cas d'étude de la dynamique compétitive : engagé dans une « guerre de territoire » contre d'autres groupes ransomware, DragonForce a ciblé 19 organisations EU depuis le lancement de sa plateforme RaaS en juin 2024.

### 11.2 — Le modèle RaaS : économie des affiliés

Le modèle Ransomware-as-a-Service reste le modèle économique dominant. Un groupe central (core team) développe le ransomware, maintient l'infrastructure (portail de négociation, site de leak) et recrute des affiliés. Les affiliés mènent les attaques et partagent les revenus avec le core team — typiquement 75% pour l'affilié, 25% pour le développeur.

L'ENISA observe un phénomène de recomposition post-disruption : les affiliés des groupes démantelés migrent vers d'autres programmes ou créent leurs propres variants. Le CSE canadien évalue que « dans les deux prochaines années, l'écosystème ransomware deviendra presque certainement de plus en plus fragmenté. Les affiliés commenceront presque certainement à agir indépendamment et à créer leurs propres variants pour réduire leur vulnérabilité aux disruptions des forces de l'ordre. »

### 11.3 — La chaîne d'attaque complète

La chaîne d'attaque ransomware typique en 2025 suit un modèle multi-acteurs. Un infostealer (Lumma, RedLine, Vidar) collecte des credentials sur un poste utilisateur via malvertising ou logiciel craqué. Les credentials sont vendues sur un forum par un IAB. Un affilié ransomware achète l'accès, se connecte via VPN ou RDP, conduit une reconnaissance interne, se latéralise vers les systèmes critiques, exfiltre les données sensibles (pour l'extorsion double), puis déploie le ransomware. Microsoft documente cette chaîne dans son flux d'infostealer, montrant comment une infection par un infostealer se transforme en accès réseau complet en quelques étapes.

Le **délai entre compromission initiale et déploiement du ransomware** s'est raccourci. Historiquement mesuré en semaines ou mois, il peut désormais être de quelques jours — le temps pour l'affilié de conduire sa reconnaissance et d'identifier les actifs de valeur.

### 11.4 — L'évolution des techniques d'extorsion

Les techniques d'extorsion se sont considérablement sophistiquées. La **double extorsion** (chiffrement + menace de publication des données) est devenue standard. La **triple extorsion** ajoute des attaques DDoS comme pression supplémentaire. Certains groupes pratiquent la **quadruple extorsion** : chiffrement, leak, DDoS, et contact direct des clients/partenaires de la victime.

Le CSE documente des innovations coercitives croissantes : publication de comptes à rebours sur les sites de leak, appels téléphoniques directs aux victimes et à leurs clients, critique publique des organisations victimes pour endommager leur réputation, encouragement des clients des victimes à engager des poursuites judiciaires, et exploitation de nouvelles réglementations de notification d'incidents — un groupe ALPHV a déposé une plainte auprès de la SEC américaine contre sa propre victime pour défaut de signalement de l'incident.

### 11.5 — Statistiques croisées

Les données quantitatives croisées donnent une image plus complète. Le FBI IC3 rapporte 20,877 milliards de dollars de pertes totales liées au cybercrime en 2025, avec le ransomware et les data breaches représentant une part significative des plaintes liées aux infrastructures critiques. L'ENISA documente 82 variants de ransomware déployées contre l'UE. L'ANSSI rapporte avoir traité de multiples incidents de ransomware impactant des prestataires et causant des effets en cascade sur leurs clients.

Ces chiffres sous-estiment systématiquement la réalité : le sous-signalement est structurel (beaucoup de victimes ne déclarent pas), les pertes indirectes (interruption d'activité, atteinte réputationnelle, coûts de remédiation) ne sont pas incluses, et les incidents dans certaines juridictions ne sont pas comptabilisés.

### 11.6 — Résilience de l'écosystème

Malgré les disruptions, l'écosystème ransomware fait preuve d'une résilience structurelle. Le CSE canadien évalue que « les disruptions n'auront presque certainement pas d'impact durable sur l'environnement ransomware parce que, à moins que les membres du noyau des groupes RaaS soient arrêtés, les acteurs trouvent souvent des moyens de s'adapter, se renommer et reprendre leurs opérations ».

Le modèle CaaS lui-même est un facteur de résilience : « le réseau complexe de services habilitants et de cybercriminels interagissant dans des espaces en ligne sans frontières rend l'enquête sur la cybercriminalité difficile. Si les forces de l'ordre perturbent un fournisseur CaaS populaire, l'acteur derrière lui va souvent renommer et relancer son service, ou un autre service va rapidement prendre sa place. »

### 11.7 — 🔴 Fil rouge : attaque Qilin sur un prestataire

> **📌 FIL ROUGE — Épisode 11**
>
> En juillet 2025, le pire scénario se matérialise. Le sous-traitant IT dont les credentials étaient en vente est victime d'une attaque Qilin. Le ransomware chiffre l'ensemble de l'infrastructure du prestataire — y compris les serveurs de gestion de projet partagés avec EuroDefense. L'accès initial confirme l'hypothèse de Sophie : les credentials VPN vendues sur le forum avaient été achetées par un affilié Qilin.
>
> L'impact cascade est immédiat : EuroDefense perd l'accès aux outils de gestion de projet partagés, et l'investigation révèle que l'attaquant a traversé la connexion réseau vers le SI d'EuroDefense pendant 48 heures avant le déclenchement du ransomware. Sophie reconstitue la timeline : infostealer Lumma → vente de credentials sur forum → achat par affilié Qilin → intrusion via VPN → mouvement latéral → pivot vers EuroDefense → exfiltration de données de projet → déploiement ransomware.
>
> Mais l'enquête réserve une surprise que Sophie n'anticipe pas — elle sera révélée au Chapitre 17.

---

## Chapitre 12 — Infostealers et Initial Access Brokers : les fondations de la chaîne d'attaque

### 12.1 — Les infostealers comme pilier de l'écosystème

Microsoft identifie dans son MDDR 2025 l'une des tendances les plus préoccupantes de la période : « la montée rapide de l'utilisation des infostealers ». Traditionnellement considérés comme des outils de post-exploitation, des familles comme Lumma Stealer, RedLine, Vidar et Raccoon Stealer sont désormais déployés comme **payloads de première étape** — le premier malware exécuté sur un poste compromis.

Ce changement est structurant pour l'écosystème. Les infostealers permettent une « division du travail à travers l'écosystème cybercriminel : les opérateurs initiaux déploient le malware, les courtiers en accès monétisent les données volées, et des utilisateurs comme les groupes ransomware les utilisent pour prendre pied dans les environnements d'entreprise ». En conséquence, « les infections par infostealer représentent plus que de simples compromissions locales — elles posent un risque stratégique d'intrusions d'entreprise plus larges ».

### 12.2 — Mécanismes et vecteurs de distribution

Les infostealers sont typiquement distribués via **malvertising** (publicités malveillantes sur les moteurs de recherche), **SEO poisoning** (sites malveillants positionnés en haut des résultats de recherche), **logiciels craqués** (installateurs piégés de logiciels populaires), et techniques de tromperie comme **ClickFix** (fenêtres pop-up imitant des erreurs système qui incitent l'utilisateur à exécuter un script malveillant).

Les données collectées incluent : les credentials stockées dans les navigateurs (mots de passe, auto-complete), les cookies de session (permettant de contourner le MFA en réutilisant une session déjà authentifiée), les tokens d'authentification, les données de formulaire, les informations système, et les wallets de cryptomonnaies.

### 12.3 — IAB : passerelle vers le ransomware

Les Initial Access Brokers (IAB) constituent le maillon intermédiaire entre les infostealers et le ransomware. L'ASD documente leur modèle économique : « Les IAB profitent de la vente d'accès aux réseaux de victimes (y compris les credentials). L'accès est vendu sur le dark web, avec des annonces listant un prix demandé et des détails sur la victime, comme le type d'entreprise, le pays d'origine et le chiffre d'affaires. Typiquement, le prix de l'accès est relativement bas, permettant à des cybercriminels qui n'auraient autrement pas pu obtenir un point d'entrée dans un système victime. »

L'Europol note que les IAB « font de plus en plus de publicité pour ces services, ainsi que pour les matières premières qui y sont liées, sur des plateformes criminelles spécialisées utilisées par un ensemble très divers de cybercriminels ». La commoditisation de l'accès initial transforme le ransomware d'une opération technique complexe en une opération essentiellement logistique et financière.

### 12.4 — Opérations de démantèlement et résilience

Les forces de l'ordre ont ciblé l'infrastructure infostealer et IAB. L'opération Magnus (2024) a visé des infostealers. Le démantèlement de LummaC2 en 2025 a temporairement perturbé l'un des infostealers les plus prolifiques. Mais la résilience structurelle de l'écosystème reste élevée : les opérateurs de services démantelés relancent sous un nouveau nom, et les clients migrent vers des alternatives.

### 12.5 — 🔴 Fil rouge : reconstruction de la timeline

> **📌 FIL ROUGE — Épisode 12**
>
> L'analyse forensique de l'incident du prestataire permet à Sophie de reconstituer la timeline complète. L'infection initiale par Lumma Stealer remonte à janvier 2025 — six mois avant l'attaque ransomware. Un employé du prestataire a téléchargé un logiciel craqué contenant Lumma. Le stealer a collecté les credentials VPN et les a exfiltrées vers un serveur C2. En mars, les credentials apparaissent sur un forum underground. En juin, Sophie les repère. En juillet, un affilié Qilin les achète et lance l'attaque.
>
> La leçon clé : la chaîne infostealer → IAB → ransomware peut s'étaler sur des mois. La détection à n'importe quel maillon de la chaîne aurait pu prévenir l'attaque finale. La fenêtre d'intervention existait — elle n'a pas été exploitée parce que personne ne surveillait les forums pour les credentials du prestataire.

---

## Chapitre 13 — Fraude en ligne, ingénierie sociale et flux financiers illicites

### 13.1 — Panorama des fraudes

Le FBI IC3 documente un paysage de fraude en ligne massif. L'**investment fraud** (arnaques à l'investissement, principalement liées aux cryptomonnaies) représente les pertes les plus élevées. Le **BEC/CEO fraud** (compromission de messagerie professionnelle pour détourner des virements) reste l'une des fraudes les plus rentables par incident. Les **romance scams** et le **pig butchering** (arnaques sentimentales à long terme culminant dans une arnaque d'investissement) sont en forte croissance, exploitant les plateformes de rencontres et les réseaux sociaux.

Les pertes totales déclarées au FBI IC3 est de **20,877 milliards de dollars** en 2025 — un chiffre qui ne représente qu'une fraction de la réalité mondiale, le FBI ne couvrant que les plaintes américaines.

### 13.2 — Phishing industrialisé et contournement MFA

Le phishing s'est industrialisé via le modèle **Phishing-as-a-Service (PhaaS)**. Les kits PhaaS fournissent des templates de pages de phishing, l'infrastructure d'hébergement, et des mécanismes de collecte de credentials — le tout accessible via un abonnement ou un paiement unique. L'innovation la plus significative est les kits **Adversary-in-the-Middle (AitM)** qui capturent non seulement les credentials mais aussi les tokens de session, permettant de contourner l'authentification multi-facteurs. Des kits comme **Sneaky 2FA** automatisent ce processus pour cibler spécifiquement les environnements Microsoft 365.

Le **vishing** (voice phishing) augmenté par IA représente une escalade qualitative. Les deepfakes vocaux permettent de cloner la voix d'un dirigeant à partir de quelques minutes d'enregistrement audio (disponibles sur YouTube, les podcasts, les conférences). Le cas documenté d'une fraude de 25 millions USD à Hong Kong — où un employé financier a effectué un virement après un appel vidéo avec un deepfake de son directeur financier — illustre le potentiel de cette technique.

### 13.3 — LLMs malveillants et IA offensive

L'écosystème cybercriminel a développé ses propres outils d'IA générative. **WormGPT**, **FraudGPT** et **Xanthorox AI** sont des LLMs modifiés ou créés pour assister les cybercriminels — générer des emails de phishing convaincants, créer des malwares, rédiger des scripts d'arnaque. Ces outils vont du simple jailbreak de modèles légitimes à des systèmes autonomes avec leurs propres modèles de langage.

Le FBI note que les cybercriminels « utilisent de plus en plus l'IA pour augmenter la qualité et l'efficacité de leurs attaques ». Le CERT-EU anticipe pour 2026 une augmentation de l'ingénierie sociale multi-canal assistée par IA — combinant email, voix et SMS dans des attaques coordonnées.

### 13.4 — Cryptomonnaies et blanchiment

Les cryptomonnaies sont le système circulatoire de l'écosystème cybercriminel. Le Bitcoin reste le medium principal pour les paiements de rançon, mais les monnaies à confidentialité renforcée (Monero) sont de plus en plus demandées. Les mécanismes de blanchiment incluent les **mixers** (services qui mélangent les transactions pour obscurcir la traçabilité), les **services de swap** (échange entre cryptomonnaies), et les **underground banking services** qui convertissent les cryptomonnaies en fiat.

Les outils d'analyse blockchain (Chainalysis, TRM Labs) ont considérablement amélioré les capacités de traçage. Cependant, leurs capacités ont des limites : les techniques de mixing avancées, les ponts cross-chain et les échanges décentralisés (DEX) compliquent le traçage. Le cadre réglementaire évolue : le règlement MiCA en Europe et la Travel Rule imposent des obligations de transparence aux échanges de cryptomonnaies.

Le modèle nord-coréen illustre le financement étatique par la cybercriminalité : les vols de cryptomonnaies attribués à Lazarus représentent certaines des plus grosses pertes individuelles de l'histoire de la crypto, les fonds étant utilisés pour financer les programmes d'armement de la RPDC en contournement des sanctions internationales.

### 13.5 — 🔴 Fil rouge : campagne de spearphishing augmenté IA

> **📌 FIL ROUGE — Épisode 13**
>
> En août 2025, trois cadres C-level d'EuroDefense reçoivent des appels téléphoniques apparemment du directeur financier du groupe, leur demandant de valider d'urgence un virement lié à une acquisition confidentielle. La voix est convaincante — mais le directeur financier est en vacances et n'a passé aucun appel.
>
> L'analyse révèle un deepfake vocal généré à partir d'enregistrements de conférences publiques du directeur financier. Le numéro d'appel est spoofé. Le scénario est soigneusement construit : acquisition confidentielle = urgence + confidentialité = pression à ne pas vérifier.
>
> Un seul des trois cadres a commencé le processus de validation avant de vérifier par un canal alternatif. Aucun virement n'a été effectué. Sophie rédige un bulletin d'alerte interne et recommande l'implémentation d'un protocole de vérification systématique pour tout virement supérieur à un seuil défini — y compris un callback sur un numéro pré-enregistré, jamais sur le numéro entrant.

---

## Chapitre 14 — Coopération opérationnelle et réponse judiciaire au cybercrime

> **Note de frontière** : Ce chapitre traite de la coopération **opérationnelle** entre les forces de l'ordre et les agences de cybersécurité dans la lutte contre le cybercrime : opérations de disruption, coordination d'enquêtes, démantèlements, procédures judiciaires. Les cadres **stratégiques** — doctrines nationales, coopération diplomatique, normes internationales, attribution publique — sont traités au Chapitre 22.

### 14.1 — Architecture institutionnelle de la réponse opérationnelle

La lutte opérationnelle contre le cybercrime repose sur un écosystème institutionnel dense. **Europol** (et son centre EC3) est le hub de coordination européen, fournissant un appui analytique et opérationnel aux enquêtes des États membres. **INTERPOL** coordonne les opérations à l'échelle mondiale entre ses 195 pays membres, avec des bureaux régionaux (Regional Cybercrime Operations Desks). Le **FBI/IC3** est la principale agence d'investigation américaine. Les agences nationales (ANSSI/CERT-FR, NCSC UK, BKA Allemagne, etc.) gèrent la réponse au niveau national.

Le **cycle EMPACT** (European Multidisciplinary Platform Against Criminal Threats) définit les priorités opérationnelles européennes, avec des objectifs spécifiques pour la cybercriminalité incluant le ciblage des groupes ransomware, les IAB, et les infrastructures de facilitation.

La **stratégie globale INTERPOL** contre le cybercrime s'articule autour de quatre objectifs : (1) cadres et recommandations stratégiques, (2) renseignement et analyse, (3) coordination opérationnelle, et (4) renforcement des capacités des pays membres.

### 14.2 — Les grandes opérations de disruption 2024-2025

La période 2024-2025 a vu une intensification sans précédent des opérations de disruption.

L'**opération Endgame** (mai 2025) est décrite par l'ANSSI et Europol comme l'une des plus ambitieuses : elle a ciblé les botnets et droppers qui servent d'infrastructure commune à de nombreuses opérations cybercriminelles. En ciblant la couche d'infrastructure plutôt que les groupes individuels, Endgame visait à perturber l'ensemble de la chaîne CaaS.

Le **takedown de LockBit** (février 2024) impliquant 10 pays a permis de saisir l'infrastructure du groupe, de fournir des outils de déchiffrement aux victimes, et de geler des comptes de cryptomonnaies. Des membres du noyau ont été arrêtés. Cependant, LockBit a tenté de reprendre ses activités avant d'être finalement compromis en mai 2025.

Le **démantèlement de LummaC2** en 2025 a ciblé l'un des infostealers les plus prolifiques, perturbant temporairement la supply chain criminelle en amont du ransomware.

D'autres opérations significatives incluent le takedown de la plateforme de communication chiffrée Ghost (septembre 2024), le démantèlement de forums cybercriminels (Cracked), et des opérations ciblant les réseaux de phishing ayant fait plus de 480 000 victimes dans le monde.

### 14.3 — Impact réel des disruptions : efficacité et limites

L'efficacité des opérations de disruption est réelle mais limitée dans le temps. Le CSE canadien évalue que « ces disruptions n'auront presque certainement pas d'impact durable sur l'environnement ransomware parce que, à moins que les membres du noyau des groupes RaaS soient arrêtés, les acteurs trouvent souvent des moyens de s'adapter, se renommer et reprendre leurs opérations ».

Plusieurs facteurs limitent l'impact durable. Les **safe haven states** — pays qui ne coopèrent pas avec les forces de l'ordre occidentales et où les cybercriminels peuvent opérer en impunité — permettent aux acteurs arrêtés nulle part d'être remplacés immédiatement. Le modèle CaaS lui-même est un facteur de résilience : si un service est perturbé, des alternatives existent. Et la flexibilité du modèle « permet aux cybercriminels d'utiliser simultanément plusieurs fournisseurs de services pour pouvoir pivoter vers de nouveaux fournisseurs si l'un d'eux est perturbé ».

Microsoft plaide pour des approches complémentaires : la désignation d'États sponsors de ransomware (similaire aux États sponsors du terrorisme), des partenariats public-privé renforcés (Counter Ransomware Initiative, IST Ransomware Task Force), et des conséquences graduées et diversifiées pas limitées au domaine cyber.

### 14.4 — Convention de Budapest et évolutions juridiques

La Convention de Budapest sur la cybercriminalité (2001) reste le principal instrument juridique international. Ses limitations — adoption inégale, dispositions datées, absence de mécanismes de coopération rapide — ont conduit à des efforts de modernisation. Les négociations pour un traité onusien sur la cybercriminalité se poursuivent, avec des tensions entre pays favorables à un cadre large (Russie, Chine) et pays préférant un instrument ciblé sur la cybercriminalité stricto sensu (UE, États-Unis, sociétés civiles).

### 14.5 — 🔴 Fil rouge : exploitation des IOCs Endgame

> **📌 FIL ROUGE — Épisode 14**
>
> Suite à l'opération Endgame en mai 2025, Europol et le CERT-FR publient des IOCs (indicateurs de compromission) liés aux botnets et droppers démantelés. Sophie croise ces indicateurs avec les données forensiques de l'incident EuroDefense et identifie une correspondance : un loader utilisé dans l'attaque contre le prestataire est lié à un botnet ciblé par Endgame.
>
> Cette corrélation enrichit son analyse de la chaîne d'attaque et confirme la connexion entre l'écosystème CaaS (botnet → loader → ransomware) et l'incident spécifique EuroDefense. Sophie intègre cette corrélation dans son CTL comme exemple concret de la convergence CaaS documentée dans le corpus.

> **🎯 CAPSTONE Partie III** : Analyser une chaîne d'attaque cybercriminelle complète : infostealer → IAB → ransomware. Pour chaque maillon, identifier : l'acteur, le mécanisme, la timeline, les IOCs, les points de détection manqués, et formuler des recommandations défensives priorisées P0 (critique — sous 72h), P1 (important — sous 30 jours), P2 (structurant — sous 6 mois).

---
