---
title: 'Chapitre 10 — Chine : campagnes de référence et tendances 2023-2026'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie III — Chine
  - index.md
---

Ce chapitre présente les campagnes chinoises les plus emblématiques, et analyse les tendances récentes qui dessinent l’évolution de la menace.

## 10.1 Opération Cloud Hopper (APT10, 2014-2018)

**Acteur** : APT10 (MSS Tianjin). **Paradigme** : compromission des **MSP** (Managed Service Providers) comme multiplicateur de scope.

**Synthèse** : entre 2014 et 2018, APT10 a compromis un ensemble de grands **MSP internationaux** — entreprises qui gèrent l’infrastructure IT de centaines ou milliers de clients finaux. Parmi les MSP compromis (documentés publiquement) : IBM, HPE, et plusieurs autres. Une fois dans le MSP, APT10 utilisait les accès privilégiés légitimes du MSP vers ses clients pour pénétrer leurs environnements — pivot silencieux, protégé par la confiance implicite qui existe entre un MSP et ses clients.

**Scope victimes** : estimations entre des dizaines et des centaines de clients finaux touchés à travers le monde, dans des secteurs variés (aérospatial, ingénierie, énergie, télécoms, pharma, médias).

**Découverte et publication** : l’opération a été découverte et documentée publiquement en 2017-2018 par **PwC** et **BAE Systems** dans un rapport conjoint. L’indictment DOJ de décembre 2018 a consolidé l’attribution à APT10 / MSS Tianjin et nommé deux ressortissants chinois.

**Leçons** :

- La supply chain IT (MSP, fournisseurs de services managés) est un vecteur APT majeur. Un MSP compromis expose des dizaines à des milliers de clients.
- La confiance implicite entre prestataire et client doit être réévaluée (Zero Trust appliqué aux prestataires internes).
- Les prestataires doivent être considérés comme faisant partie du périmètre de sécurité — d’où les obligations de sécurité renforcées imposées aux MSP par NIS 2.

## 10.2 Hafnium / ProxyLogon (2021)

**Acteur** : Hafnium (MSS, probablement Hubei). **Paradigme** : exploitation massive d’une vulnérabilité 0-day Exchange pour compromettre des dizaines de milliers d’organisations en quelques jours.

**Synthèse** : début mars 2021, Microsoft publie des correctifs d’urgence pour quatre vulnérabilités Exchange (CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065 — collectivement nommées **ProxyLogon**). L’exploitation avait commencé début janvier 2021 par un acteur étatique (Hafnium) de manière ciblée. À partir de fin février / début mars 2021, l’exploitation s’est massifiée — des dizaines de groupes ont commencé à exploiter la vulnérabilité, souvent pour déposer des web shells pour un accès futur.

**Impact** : estimations entre **30 000 et 250 000 organisations compromises mondialement** en l’espace de quelques semaines. Impact massif sur les organisations européennes notamment, beaucoup utilisant Exchange on-premises. Le MOIE français (Ministère de l’Intérieur) et de nombreuses administrations européennes ont été affectés.

**Attribution publique** : en juillet 2021, les États-Unis, le Royaume-Uni, l’Union européenne, l’OTAN et plusieurs autres pays ont conjointement attribué ProxyLogon au MSS chinois — une attribution publique coordonnée sans précédent dans sa portée.

**Leçons** :

- Les vulnérabilités 0-day sur les services exposés massivement (Exchange, VPN, passerelles) produisent des compromissions industrielles.
- La prolifération post-publication est massive : une fois une CVE connue, elle est exploitée par des dizaines d’acteurs en quelques jours.
- Le patching d’urgence des services exposés est un impératif.

## 10.3 Microsoft 2023 / Storm-0558

**Acteur** : Storm-0558 (nomenclature Microsoft, acteur chinois sous investigation). **Paradigme** : compromission d’une clé de signature cloud permettant l’accès aux emails gouvernementaux.

**Synthèse** : en juillet 2023, Microsoft révèle publiquement que Storm-0558 a compromis une **clé privée de signature MSA** (Microsoft Account) en 2021 et l’a utilisée pour forger des tokens d’authentification permettant d’accéder aux emails Outlook.com et à certaines ressources Exchange Online. Le groupe a utilisé ces tokens pour accéder aux emails d’**environ 25 organisations gouvernementales**, dont le Département d’État américain et des gouvernements européens.

L’enquête ultérieure, notamment par la **Cyber Safety Review Board** (CSRB — institution fédérale américaine), a produit un **rapport public** en 2024 qui est une lecture fondatrice pour comprendre les défaillances dans la sécurité du cloud Microsoft. Le rapport identifie une série de défaillances : gestion inadéquate des clés cryptographiques, visibilité insuffisante des anomalies, culture de sécurité critiquée.

**Impact** :

- Accès à des communications gouvernementales sensibles américaines et européennes pendant plusieurs mois.
- Érosion de la confiance dans la sécurité cloud de Microsoft — directe conséquence commerciale et politique.
- Déclenchement d’investigations réglementaires et de durcissements imposés.

**Distinction avec le breach Microsoft 2023-2024 par APT29** : ce sont **deux incidents distincts**. Storm-0558 (MSS chinois) en juillet 2023 via compromission de clé de signature ; APT29 (SVR russe) en novembre 2023 - janvier 2024 via password spray et OAuth abuse.

## 10.4 Salt Typhoon 2024 — le breach télécoms US

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

## 10.5 Mustang Panda contre l’Europe 2023-2025

**Acteur** : Mustang Panda. **Paradigme** : extension géographique du ciblage chinois vers l’Europe dans le contexte du conflit ukrainien et des tensions Taïwan.

**Synthèse** : depuis 2022, Mustang Panda a intensifié ses opérations contre des cibles européennes. Objectifs probables : collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine (et de la Russie), collecte sur les positions Taïwan, ciblage des ONG pro-démocratie, surveillance de la diaspora chinoise en Europe.

**Campagnes documentées** :

- ESET a publié plusieurs rapports (2022-2024) documentant le ciblage européen par Mustang Panda, notamment gouvernements, fournisseurs de défense, ONG spécialisées.
- Check Point a documenté l’exploitation de thèmes géopolitiques (Ukraine, Taïwan, relations UE-Chine) comme leurres de phishing.

**Impact** : pas de compromission massive publiquement revendiquée, mais confirmation d’une présence chinoise significative dans le paysage cyber européen — rappel que l’Europe n’est pas épargnée par les APT chinoises malgré une focalisation historique perçue sur les États-Unis et l’Asie.

## 10.6 Campagnes contre les infrastructures critiques européennes

Plusieurs rapports 2023-2025 documentent des campagnes chinoises contre des infrastructures critiques en Europe :

**Secteur énergie** : ciblage d’opérateurs de distribution d’électricité, d’opérateurs pétroliers et gaziers. Advisory ANSSI et BSI ont mentionné publiquement des tentatives d’intrusion sans détailler les cibles.

**Télécommunications européennes** : ciblage de plusieurs opérateurs télécoms européens dans une extension probable du modèle Salt Typhoon.

**Secteur maritime** : APT40 continue d’être très actif contre les ports européens (Rotterdam, Hambourg, Anvers notamment) et les entreprises maritimes européennes.

**Infrastructures de recherche** : universités techniques européennes, centres R&D.

La tendance : l’Europe est un théâtre APT chinois croissant, moins documenté publiquement que les États-Unis (les pays européens communiquent moins sur les incidents étatiques) mais actif.

## 10.7 Évolution du tradecraft chinois

Le tradecraft chinois a évolué significativement sur la période 2015-2026. Synthèse des évolutions.

**Phase 1 (années 2000 - 2014) : force brute et volumétrie**. L’approche Unit 61398 et APT10 historique : scan massif, exploitation opportuniste, phishing de masse. Beaucoup de cibles, sophistication technique modeste, OPSEC moyen. Le rapport Mandiant APT1 de 2013 a catalysé une prise de conscience et probablement une réorganisation.

**Phase 2 (2015 - 2020) : consolidation et professionnalisation**. Réorganisations post-Unit 61398 et post-accord Xi-Obama (2015, qui a temporairement fait baisser l’espionnage économique chinois aux US). Émergence de groupes plus compartimentés, professionnalisation des TTP, adoption de techniques modernes (DLL sideloading, abus de services légitimes).

**Phase 3 (2020 - présent) : furtivité et pré-positionnement**. L’émergence de Volt Typhoon (2021+) marque une rupture : groupes chinois capables d’opérations ultra-furtives, LotL exclusif, maintenant des accès pendant des années sans signaux détectables. Le ciblage s’oriente vers les appliances edge (cibles sans EDR, privilégiées), les télécoms (pour l’espionnage stratégique), et les infrastructures critiques (pour le pré-positionnement).

**Phase 4 émergente (2024+) : industrialisation via contractors**. Le leak i-Soon a révélé l’étendue de l’écosystème contractor civil. Le modèle se professionnalise : des entreprises développent des outils à destination de multiples clients étatiques, produisent des infrastructures réutilisables (Raptor Train), fournissent des services « clé en main ».

La trajectoire : montée en sophistication continue, fragmentation croissante entre services officiels et contractors multiples, extension géographique (moins concentré US, plus global), et augmentation du volume d’opérations sous-radar qui ne sont identifiées que après plusieurs années de maintien d’accès.

## 10.8 Tendance structurelle : fragmentation de l’attribution

La conséquence analytique majeure de ces évolutions : l’**attribution précise des opérations chinoises est devenue plus difficile**, pas moins. Pourquoi ?

**Prolifération des groupes** : des dizaines de clusters suivis, parfois distinguables seulement par des différences marginales de TTP. Le chevauchement d’outils (PlugX utilisé par plusieurs groupes), d’infrastructure partagée, et de tradecraft similaire rend la discrimination difficile.

**Opacification des liens MSS/PLA/contractors** : qui commandite quelle opération ? Les indictments publics attribuent à des bureaux MSS spécifiques, mais les contractors peuvent travailler simultanément pour plusieurs clients étatiques, et la coordination inter-services est imparfaite.

**Sophistication croissante** : moins d’erreurs opérationnelles, moins d’artefacts d’attribution, usage intensif des abus de services légitimes et du LotL qui produisent moins de signatures.

**Implications pour l’analyste** : face à une intrusion attribuée « à la Chine », préciser **quel groupe** spécifiquement est souvent difficile ou impossible sans accès à du renseignement non-public. La discipline consiste à : (1) tester plusieurs hypothèses (MSS Hainan vs MSS Tianjin vs PLA vs contractor) via ACH, (2) coter la confiance prudemment (« probablement acteur chinois, groupe non déterminé avec confiance »), (3) ne pas laisser le prestige d’une attribution précise forcer une conclusion sous-étayée.

-----
