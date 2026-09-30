---
title: 'Chapitre 8 — Chine : contexte, doctrine et appareil cyber'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie III — Chine
  - index.md
---

## 8.1 Priorités géopolitiques et principes doctrinaux

La stratégie cyber chinoise ne peut pas se comprendre sans la stratégie globale de la RPC. Quatre priorités structurent l’ensemble.

**Dominance technologique et rattrapage industriel** : depuis les plans Made in China 2025 (2015) et les successeurs (China Standards 2035, stratégie IA 2030), la Chine s’est fixé comme objectif stratégique de devenir leader technologique dans une série de secteurs — semiconducteurs, IA, énergie verte, biotechnologies, aérospatial, télécommunications 5G/6G. Le cyber est un instrument central de ce rattrapage : vol de propriété intellectuelle à très grande échelle, ciblage des centres de R&D, compromission de la supply chain technologique occidentale. Les estimations américaines du préjudice cumulé du vol de propriété intellectuelle par la Chine sont contestées mais situent l’ordre de grandeur en centaines de milliards de dollars par an.

**Question Taïwan** : la réunification avec Taïwan est une priorité stratégique fondamentale du PCC. Le cyber sert la préparation à plusieurs niveaux : collecte de renseignement sur les positions américaines et alliées dans le Pacifique (pré-positionnement dans les infrastructures US de Guam et du Pacifique — documenté par Volt Typhoon), ciblage des institutions taïwanaises (gouvernement, défense, partis politiques), influence sur l’opinion taïwanaise (opérations sur les réseaux sociaux).

**Route de la Soie numérique** : extension géo-économique de la Belt and Road Initiative dans l’espace numérique. Fourniture d’infrastructures télécoms et de surveillance à des partenaires internationaux (Huawei, ZTE, Dahua, Hikvision), exportation de modèles de gouvernance numérique, accès privilégié aux données des partenaires. Le cyber alimente cette stratégie par la collecte sur les concurrents et la présence dans les nouvelles infrastructures.

**Contrôle politique interne et répression étendue** : surveillance des Ouïghours, Tibétains, dissidents, défenseurs des droits humains, médias indépendants, communautés religieuses non-autorisées. Le ciblage de la diaspora (surveillance à l’étranger, pressions sur les familles restées en Chine) est documenté dans de nombreux cas. Le cyber est intégré à cette architecture de contrôle.

**Doctrine de la « guerre sans limites »** : formulée par les colonels Qiao Liang et Wang Xiangsui dans *Unrestricted Warfare* (1999), elle postule que la guerre ne se limite pas aux moyens militaires et peut se mener sur tous les terrains (économique, financier, informationnel, cyber, juridique). Cette formulation informe la vision intégrée du cyber comme instrument de puissance.

**Integrated Deterrence et long game** : contrairement à la doctrine russe qui accepte l’escalade destructive ouverte, la doctrine chinoise privilégie le long terme, la patience, et l’intégration multi-instruments. L’activation publique destructive est rare ; l’espionnage massif et le pré-positionnement sont la norme. Le **dwell time** des opérations chinoises est souvent parmi les plus longs observés — des intrusions documentées ont été maintenues 5 à 10 ans avant découverte.

## 8.2 Le MSS : renseignement civil et décentralisation opérationnelle

Le **MSS** (Ministry of State Security, 国家安全部) est le principal service de renseignement civil chinois. Successeur de plusieurs organes historiques (réorganisé en 1983), il conduit à la fois le renseignement extérieur, le contre-espionnage intérieur, et une partie de la répression politique.

Une spécificité structurante du MSS : la **décentralisation opérationnelle**. Contrairement à une agence centralisée type NSA, le MSS fonctionne via un **réseau de bureaux régionaux** (au niveau des provinces et de certaines grandes villes) qui disposent d’une autonomie opérationnelle significative. Plusieurs bureaux régionaux ont été publiquement identifiés comme conduisant des cyberopérations :

- **MSS Tianjin Bureau** : associé à **APT10** / Stone Panda. Indicté publiquement par le DOJ US en décembre 2018 — noms spécifiques d’opérateurs MSS Tianjin publiés.
- **MSS Hainan State Security Department** : associé à **APT40** / Leviathan. Indicté DOJ en juillet 2021, avec la création d’une société écran (« Hainan Xiandun Technology Development Co. ») pour la couverture opérationnelle.
- **MSS Shanghai Bureau**, **MSS Guangzhou Bureau**, **MSS Jiangsu Bureau** : d’autres bureaux régionaux identifiés dans divers rapports.

Cette décentralisation a des conséquences pour l’analyse : différents bureaux régionaux ont des tradecrafts légèrement différents, des priorités sectorielles distinctes, et parfois des chevauchements qui suggèrent une coordination imparfaite entre bureaux. Le MSS central fournit l’orientation stratégique, mais l’exécution opérationnelle peut varier.

## 8.3 Le PLA : réorganisation post-2015 et SSF

L’appareil cyber militaire chinois a connu une **réorganisation majeure en 2015-2016**. L’emblématique **Unit 61398** (Shanghai, département 3 du PLA — identifiée publiquement par Mandiant en 2013, inculpée par le DOJ en 2014) a été dissoute dans sa forme initiale. Les capacités cyber militaires ont été regroupées dans la **Strategic Support Force (SSF)** créée en décembre 2015, qui rassemble cyber, espace, guerre électronique et opérations d’information dans une structure unifiée.

La SSF comprend un **Network Systems Department** (NSD) qui est la branche cyber principale du PLA. Des rapports récents suggèrent que la SSF a été elle-même réorganisée en 2024 dans une nouvelle structure (Information Support Force), mais les informations publiques sur ces évolutions restent partielles.

Des unités spécifiques du PLA continuent d’être associées à des opérations cyber : unités successeurs de l’ancienne Unit 61398, **Unit 78020** (Chengdu Region Technical Reconnaissance Bureau) associée à plusieurs opérations de ciblage de l’Inde et de l’Asie du Sud-Est, **Unit 61486** et autres TRB (Technical Reconnaissance Bureaux).

La distinction MSS/PLA pour l’attribution des opérations : **le MSS tend à mener l’espionnage stratégique et économique, le PLA tend à mener les opérations de reconnaissance militaire et le pré-positionnement**. Mais les frontières sont perméables et plusieurs groupes APT ont des liens mixtes ou suspectés avec les deux.

## 8.4 Le modèle des contractors civils

Une caractéristique unique de l’écosystème cyber chinois est l’**utilisation massive de contractors civils** pour les opérations offensives. Des entreprises privées chinoises sont mandatées par le MSS ou le PLA pour conduire des opérations cyber — soit pour la conception d’outils, soit pour l’opération directe.

Ce modèle offre plusieurs avantages pour l’État chinois : déni plausible (les opérateurs ne sont pas formellement des employés de l’État), flexibilité des ressources (monter en capacité sans créer d’emplois publics), accès à des talents (attirer des profils qui ne travailleraient pas dans le secteur public), compartimentation (limiter la visibilité interne sur les opérations).

## 8.5 Le leak i-Soon de février 2024

**i-Soon (Anxun Information Technology)** est une société basée à Shanghai, spécialisée en outils de surveillance et en opérations cyber pour le compte de multiples clients gouvernementaux chinois (MSS, PLA, polices provinciales). **En février 2024, un leak massif de données internes d’i-Soon** a révélé le fonctionnement de cet écosystème de contractors.

Plus de 500 fichiers ont été publiés sur GitHub par un contributeur anonyme (probablement un mécontent interne). Le leak comprend : échanges internes (WeChat, emails), documentation technique d’outils offensifs, listings de victimes, listings de clients gouvernementaux, négociations commerciales, plaintes d’employés.

**Outils documentés** :

- Implants Windows avec capacités keylogging, capture d’écran, exfiltration.
- Implants Android avec capacités SMS, géolocalisation, microphone.
- Plateforme de Twitter/X monitoring et manipulation (faux comptes, amplification).
- Outils de bruteforce Outlook et de phishing.
- Plateforme de surveillance mobile vendue à des bureaux de sécurité publique chinois pour la surveillance de dissidents et de minorités.
- Outils de ciblage de routeurs et NAS.

**Clients identifiés** : MSS (central et bureaux régionaux), bureaux de sécurité publique de nombreuses provinces, PLA.

**Victimes documentées** : ciblage de gouvernements asiatiques (Mongolie, Népal, Pakistan, Malaisie, Thaïlande, Vietnam, Cambodge, Laos), d’organisations des droits humains, de médias, de militants Hong Kong, et de la diaspora ouïghoure.

**Impact analytique** : confirmation directe de l’écosystème contractor, des relations client-fournisseur entre entités étatiques chinoises et entreprises privées, et de l’ampleur du ciblage de dissidents et de minorités. L’analyse détaillée du leak a été publiée par SentinelOne, Sekoia, Harfang Lab, et plusieurs chercheurs indépendants. Elle reste une lecture essentielle pour comprendre l’écosystème cyber chinois contemporain.

## 8.6 Ciblage sectoriel : les priorités chinoises

Les priorités de ciblage chinoises révèlent les priorités stratégiques.

**Semiconducteurs et high-tech** : priorité absolue. Ciblage de TSMC, ASML, Applied Materials, Tokyo Electron, Samsung — et de toute la supply chain. Objectif : rattraper le retard technologique dans un secteur où les sanctions américaines (CHIPS Act 2022) ont durci les restrictions d’exportation.

**Aéronautique et défense** : Lockheed Martin, Boeing, BAE Systems, Airbus, Dassault, Thales. Le programme F-35 est documenté comme largement compromis par des acteurs chinois depuis les années 2000, ce qui aurait contribué au développement accéléré du chasseur J-20 chinois.

**Énergie** : pétrole/gaz, nucléaire, énergies renouvelables. Pré-positionnement documenté dans les infrastructures électriques US et du Pacifique (Volt Typhoon).

**Biotechnologies et pharmaceutique** : vol de recherche (vaccins COVID en 2020, thérapies oncologiques, biotechnologies d’avant-garde). Ciblage particulièrement intense depuis 2020.

**Maritime et logistique** : APT40 a été massivement actif contre les entreprises maritimes, les ports, et les chantiers navals. Reflète l’intérêt chinois pour la domination maritime.

**Télécommunications** : infrastructure télécom, équipementiers, opérateurs. **Salt Typhoon** (2024) a compromis des systèmes d’interception légale de multiples opérateurs télécoms US — accès potentiel aux communications de millions d’Américains.

**Diaspora et minorités** : Ouïghours, Tibétains, Hongkongais, dissidents. Utilisation du cyber pour la surveillance à l’étranger, la collecte sur les familles restées en Chine, et parfois le harcèlement.

**Think tanks et académique** : producteurs d’analyses sur la Chine (CSIS, Atlantic Council, Chatham House, IFRI, etc.), universités spécialisées en études chinoises, chercheurs individuels.

**Politique** : ciblage de parlementaires (APT31 contre le UK et le US), partis politiques, membres de la société civile engagés dans les politiques Chine.

## 8.7 Fil rouge — BLACKOUT Épisode 4

> **⚡ BLACKOUT — Épisode 4 : la compatibilité avec le profil chinois**
> 
> Le CERT examine si les TTP observées sur BLACKOUT sont compatibles avec les acteurs chinois documentés, notamment Volt Typhoon et clusters similaires.
> 
> **Cohérences** :
> 
> - **Exploitation d’appliance edge (Ivanti CVE-2024-21887)** : Volt Typhoon et plusieurs autres acteurs chinois ont massivement exploité Ivanti fin 2023 / début 2024 (advisory CISA de février 2024). **Forte cohérence avec le profil chinois**.
> - **Living off the Land** : Volt Typhoon se caractérise par un LotL quasi exclusif, avec peu ou pas de malware custom. BLACKOUT montre un PsExec, du Kerberoasting, du DLL sideloading — beaucoup de LotL, et pas de malware custom identifié à ce stade. **Cohérence forte**.
> - **Pré-positionnement OT sans action** : signature exacte de Volt Typhoon, qui maintient des accès dans les infrastructures critiques US sans action observable. **Cohérence très forte**.
> - **Patience opérationnelle** : l’attaquant est présent depuis au moins 42 jours sans action visible. Long dwell time cohérent avec le profil chinois.
> 
> **Décalages** :
> 
> - **Géographie** : Volt Typhoon a été principalement documenté aux US et dans le Pacifique (Guam). Un opérateur énergie européen est une cible inhabituelle pour ce cluster spécifique, même si des cibles européennes ne sont pas exclues et que des clusters chinois similaires peuvent être actifs en Europe.
> - **Beaconing régulier (27 min ± 3 min)** : Volt Typhoon a plutôt des patterns d’activité très irréguliers (accès ponctuels via les routeurs SOHO compromis). Un beaconing régulier serait plus atypique. Mais d’autres clusters chinois utilisent bien du beaconing classique.
> - **Contexte géopolitique immédiat** : pas de tension Taïwan aiguë à la date de l’incident, ce qui rend un déclenchement de pré-positionnement chinois à ce moment précis moins « naturel » que le pré-positionnement russe (conflit ukrainien actif).
> 
> **Diagnostic CERT** : profil **également compatible avec un acteur chinois** — peut-être pas Volt Typhoon spécifiquement, mais un cluster chinois lié. **H2 Chine** reste plausible, avec une confiance à ce stade entre faible et modérée.
> 
> L’incertitude demeure. Le CERT continue l’investigation — notamment pour identifier des artefacts techniques additionnels qui pourraient trancher entre profil russe et profil chinois.

-----
