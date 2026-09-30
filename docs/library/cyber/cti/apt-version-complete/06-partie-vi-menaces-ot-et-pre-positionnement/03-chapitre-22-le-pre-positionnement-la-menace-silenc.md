---
title: 'Chapitre 22 — Le pré-positionnement : la menace silencieuse'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie VI — Menaces OT ET pré-positionnement
  - index.md
---

## 22.1 Définition opérationnelle du pré-positionnement

Le **pré-positionnement** est le maintien d’un **accès dormant** dans des infrastructures critiques, **sans action immédiate**, pour une utilisation future en cas de conflit ou d’escalade politique. C’est le scénario stratégique le plus inquiétant du paysage cyber contemporain.

**Caractéristiques opérationnelles** :

- **Accès maintenu** : l’attaquant a compromis des systèmes critiques et conserve la capacité d’y accéder.
- **Pas d’exfiltration massive** : contrairement à l’espionnage, le pré-positionnement ne collecte pas de renseignement (ou seulement le minimum nécessaire au maintien d’accès).
- **Pas de sabotage** : contrairement à une attaque destructive, aucune action malveillante n’est déclenchée.
- **Pas de ransomware** : aucune monétisation, aucune visibilité.
- **Patience opérationnelle** : l’accès peut être maintenu des mois ou des années avant activation — ou ne jamais être activé.

**Intention stratégique** : disposer d’un **levier activable** en cas de besoin. Le message implicite est : « en cas d’escalade/conflit/décision politique, nous pouvons activer ces accès pour causer des dommages aux infrastructures critiques de notre adversaire ».

C’est une **forme de dissuasion cyber**. Comme la dissuasion nucléaire, elle repose sur l’existence d’une capacité plus que sur son utilisation. Mais contrairement à la dissuasion nucléaire, elle est **silencieuse et ambiguë** — la cible peut ignorer l’existence du pré-positionnement, ce qui affaiblit l’effet dissuasif mais préserve la flexibilité opérationnelle.

## 22.2 Volt Typhoon : le cas d’école

**Volt Typhoon** est l’exemple de pré-positionnement le plus documenté publiquement. Déjà introduit au Ch.9, traité en détail comme étude de cas au Ch.31.

**Synthèse pour ce chapitre** :

- Activité au moins depuis mi-2021, probablement plus tôt.
- Cibles : opérateurs de télécoms, énergie, eau, transport aux US et dans le Pacifique (Guam).
- TTP ultra-furtives : LotL exclusif, credentials légitimes, pas de malware custom, C2 via routeurs SOHO compromis.
- **Aucune exfiltration massive, aucune action destructive, aucune monétisation observées**.
- Attribué par les Five Eyes (advisory mai 2023 et réitérations 2024) à la Chine, probablement PLA ou affilié.

**Signification stratégique** : interprété par la communauté de renseignement américaine comme une **capacité de dissuasion/représailles chinoise** liée au scénario Taïwan. Si un conflit militaire éclate autour de Taïwan, la Chine pourrait activer ces accès pour frapper les infrastructures critiques américaines et alliées, dégradant les capacités de projection militaire US dans la région.

**Démantèlements partiels** : FBI a démantelé en janvier 2024 le **KV Botnet** (routeurs Cisco RV domestiques utilisés comme C2 Volt Typhoon) sous mandat judiciaire. Mais Volt Typhoon dispose probablement d’infrastructures alternatives.

## 22.3 Salt Typhoon : autre dimension du pré-positionnement

**Salt Typhoon** illustre une autre facette : pré-positionnement pour l’espionnage stratégique plutôt que pour le sabotage. Déjà traité au Ch.9 et Ch.10.

**Synthèse** :

- Compromission de multiples opérateurs télécoms US (Verizon, AT&T, Lumen confirmés).
- Accès aux **Lawful Intercept Systems** — compromission ciblée permettant de voir qui les autorités américaines surveillaient.
- Accès aux communications de millions d’Américains, ciblage particulier de personnalités politiques.
- Durée de présence estimée à au moins un an avant détection.

**Pré-positionnement ou espionnage ?** Salt Typhoon se situe à la frontière. L’accès maintenu sur les télécoms **est** un pré-positionnement (levier activable en conflit), mais l’accès était aussi activement utilisé pour du renseignement. Cette combinaison — pré-positionnement + espionnage — est probablement la configuration la plus fréquente dans la réalité, les deux n’étant pas mutuellement exclusifs.

## 22.4 Sandworm et le pré-positionnement énergie européenne

Le pré-positionnement n’est pas l’apanage chinois. **Sandworm (GRU Unit 74455)** conduit depuis plusieurs années des opérations de pré-positionnement dans les infrastructures critiques européennes, dans le contexte du conflit ukrainien.

**Documentation publique** :

- Advisory ANSSI (France), BSI (Allemagne), CERT-UA ont évoqué publiquement (avec parcimonie sur les détails) des tentatives d’intrusion dans des infrastructures critiques européennes.
- Rapports Mandiant, Microsoft, Dragos documentent des compromissions d’opérateurs énergie, eau, transport en Europe (sans nommer les victimes pour raisons opérationnelles).
- **Tentative Industroyer2 (avril 2022)** déjouée — démonstration d’intention et de capacité.

**Implications** : l’Europe est une cible de pré-positionnement russe crédible. Les opérateurs européens OIV (France) et entités essentielles (NIS 2) doivent intégrer ce scénario dans leur planification.

## 22.5 Autres clusters sous observation

Plusieurs clusters sont sous observation pour des activités possibles de pré-positionnement, sans qu’une attribution définitive ait été publiée.

**Flax Typhoon** (Chine, lié à Integrity Technology Group sanctionné en 2025) : construisait un botnet massif (Raptor Train, 260 000+ dispositifs IoT compromis) démantelé en septembre 2024 par le FBI. Utilisé probablement comme infrastructure offensive pour d’autres clusters chinois — peut inclure des fonctions de pré-positionnement.

**Clusters non attribués** : les advisories ANSSI, CISA, et partenaires mentionnent régulièrement des clusters observés dans des infrastructures critiques, sans attribution publique à date. Leur caractérisation comme pré-positionnement dépend de l’observation de leur comportement (absence d’exfiltration, absence de destructif, maintien d’accès long terme).

**Clusters iraniens** : moins documentés comme pré-positionnement structurel, mais les ciblages « Cyber Av3ngers » sur l’eau et sur l’énergie incluent potentiellement des composantes de pré-positionnement (maintien d’accès post-démonstration initiale).

## 22.6 La difficulté de détection maximale

Le pré-positionnement est la menace la plus difficile à détecter, pour des raisons structurelles.

**Pas de malware custom** : Volt Typhoon démontre que le LotL exclusif est possible et efficace. Sans binaire malveillant à hasher, les signatures EDR classiques sont aveugles.

**Pas de traffic anormal** : l’utilisation de LOLBins et de credentials légitimes produit un trafic qui ressemble à de l’administration normale. Les patterns de beaconing réguliers sont évités au profit d’accès intermittents et irréguliers.

**Pas de comportement distinctif** : les actions sont limitées au strict minimum nécessaire. Pas d’exfiltration visible, pas de tentatives de privilege escalation bruyantes, pas de mouvement latéral massif.

**Pas de monétisation** : contrairement au ransomware ou au cryptominer, le pré-positionnement ne génère aucune activité financière détectable.

**Longue durée** : les opérations s’étalent sur des mois à des années. Les anomalies, si détectables individuellement, se fondent dans le bruit de fond opérationnel normal.

**Implications détection** : la détection repose **entièrement** sur les **anomalies comportementales** et la **corrélation multi-sources**.

- **Baseline des activités admin** : un compte admin qui se connecte à un serveur inhabituel, à une heure inhabituelle, depuis un endpoint inhabituel est un signal. Établir la baseline prend du temps, la maintenir exige de la discipline.
- **Corrélation cross-sources** : connexion VPN + activité locale + connexion AD + trafic sortant. Aucun signal seul n’est conclusif ; leur combinaison peut l’être.
- **Threat hunting proactif** : recherche active d’anomalies subtiles, guidée par les TTP documentées des acteurs de pré-positionnement. Chasse au fil de l’eau, pas alerte automatique.
- **Détection réseau OT** : monitoring passif du trafic OT pour détecter les communications inhabituelles vers les équipements.

## 22.7 Le dilemme : éradiquer ou surveiller ?

Une fois un pré-positionnement détecté, les défenseurs font face à un **dilemme opérationnel** sans solution simple.

**Option A — Éradication immédiate** :

- **Avantage** : élimine la menace active, élimine le risque d’activation.
- **Inconvénient** : signal à l’adversaire que la détection a eu lieu. L’adversaire adaptera ses TTP, réinfectera via des vecteurs différents, et sera plus difficile à détecter la prochaine fois. **Perte de visibilité stratégique**.
- **Inconvénient** : si l’éradication est incomplète (accès redondants non identifiés), l’adversaire revient rapidement avec des TTP modifiées.

**Option B — Surveillance contrôlée** :

- **Avantage** : collecte de renseignement sur les TTP, sur les objectifs, sur les capacités. Ce renseignement peut être partagé avec d’autres défenseurs potentiellement ciblés. Possibilité d’identifier d’autres victimes.
- **Avantage** : ne révèle pas la détection à l’adversaire, préservant la capacité de détecter une activation imminente.
- **Inconvénient** : **risque moral et opérationnel majeur**. Si l’adversaire active son pré-positionnement avant que le défenseur puisse intervenir, l’impact peut être catastrophique. **Qui porte la responsabilité** si un blackout survient pendant la phase de surveillance ?
- **Inconvénient** : nécessite une coordination étroite avec les autorités (agences nationales) et un consensus légal/politique souvent difficile à obtenir.

**Option C — Hybride** :

- **Éradication partielle** des accès identifiés tout en maintenant la surveillance sur d’autres vecteurs suspectés.
- **Collaboration avec les agences nationales** : l’agence nationale peut prendre le relais sur la surveillance stratégique pendant que l’opérateur éradique opérationnellement.
- **Partage d’information** : le pré-positionnement découvert est communiqué à la communauté (ISAC sectoriel, CERT) pour alerter d’autres victimes potentielles.

**En pratique** : le dilemme est **résolu au cas par cas** selon la gravité, le contexte géopolitique, les ressources disponibles, et le cadre juridique. Pour un opérateur privé, l’éradication rapide est souvent la réponse par défaut (risque opérationnel non acceptable). Pour les agences nationales sur des cibles stratégiques (télécoms, énergie), la surveillance contrôlée peut être préférée.

Le dilemme n’a pas de réponse universelle. Il est exercé dans les tabletops (Ch.28) et gagne à être pensé à froid, pas dans l’urgence d’un incident réel.

## 22.8 Implications pour l’Europe

Le pré-positionnement est une menace crédible pour l’Europe. Implications opérationnelles.

**Secteurs prioritaires** :

- **Énergie** (électricité, gaz, pétrole) : cible historique de Sandworm, cible plausible de pré-positionnement chinois.
- **Télécoms** : cible démontrée par Salt Typhoon (US), extensible à l’Europe.
- **Eau** : cible de Cyber Av3ngers (Iran) et potentiellement d’acteurs russes.
- **Transport** (aéroportuaire, ferroviaire, maritime) : cible plausible pour des scénarios de disruption majeure.
- **Finance** : cible moins de pré-positionnement que d’espionnage et de fraude, mais à surveiller.
- **Santé** : cible ransomware massive, mais des APT peuvent s’y positionner aussi.

**Capacités à développer** :

- **Visibilité OT** (Ch.20) : passive monitoring sur les segments industriels.
- **Visibilité identité cloud** : monitoring des authentifications, des consentements OAuth, des activités admin (baseline + anomalies).
- **Threat hunting proactif** : équipes dédiées ou prestataires spécialisés qui recherchent activement les pré-positionnements silencieux.
- **Collaboration CERT nationale + sectoriel + international** : le modèle Ukraine est une référence.
- **Préparation à la réponse** : exercices sur les scénarios de pré-positionnement détecté, avec le dilemme éradication/surveillance.

**Cadre réglementaire** : **NIS 2** (entrée en application 2024) impose aux entités essentielles européennes des obligations de cybersécurité renforcées incluant la gestion des menaces étatiques. L’**EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d’urgence. Cadre à consolider dans les années à venir.

## 22.9 Fil rouge — BLACKOUT Épisode 5

> **⚡ BLACKOUT — Épisode 5 : pré-positionnement confirmé**
> 
> Après plusieurs semaines d’investigation, le CERT consolide l’analyse : **BLACKOUT est un cas de pré-positionnement**. Les éléments convergents :
> 
> **Absence d’exfiltration** : l’analyse des flux réseau sortants sur les 42 jours de présence documentée de l’attaquant ne révèle aucune exfiltration massive. Quelques dizaines de mégaoctets transférés, compatibles avec de la reconnaissance interne ou du maintien d’accès, pas avec une extraction de propriété intellectuelle ou de données sensibles.
> 
> **Absence d’action destructive** : aucune modification des automates détectée, aucune tentative d’interaction avec les SIS, aucun wiper déposé, aucun ransomware.
> 
> **Maintenance de l’accès** : l’attaquant a créé **trois mécanismes de persistence indépendants** sur le poste d’ingénierie OT (DLL sideloading initial, tâche planifiée, service modifié). Ce n’est pas une tentative ponctuelle — c’est une présence conçue pour durer.
> 
> **Reconnaissance du processus industriel** : l’analyse des logs révèle que l’attaquant a consulté pendant plusieurs jours les documentations techniques du SCADA, les schémas électriques, les procédures opérationnelles. Il comprenait le processus avant de s’engager plus loin.
> 
> **Positionnement stratégique** : le poste d’ingénierie OT compromis a un accès direct à 12 postes de transformation haute tension desservant environ 400 000 foyers. Un attaquant activant cet accès pourrait, théoriquement, provoquer un blackout d’envergure.
> 
> **Diagnostic CERT** : **BLACKOUT est un pré-positionnement OT** avec capacité potentielle de sabotage. L’acteur est soit Sandworm (Russie, contexte ukrainien), soit un cluster chinois (Volt Typhoon ou similaire, pré-positionnement stratégique), soit un cluster non identifié. L’analyse des TTP et le contexte géopolitique orientent vers une probabilité supérieure pour **H1 Sandworm**, mais **l’incertitude demeure** et sera traitée formellement dans la matrice ACH au Ch.24.
> 
> **Décision opérationnelle** : après concertation entre l’opérateur, le CERT, et l’ANSSI (l’opérateur étant OIV), **option A — éradication** est choisie. Raisons :
> 
> - Risque opérationnel non acceptable de laisser le pré-positionnement actif (potentiel d’activation si escalade géopolitique).
> - Contexte européen actuel tendu (conflit ukrainien, tensions énergétiques).
> - Capacité à déployer une équipe dédiée pour l’éradication complète et simultanée de tous les accès.
> 
> L’éradication est planifiée pour les prochains jours. Le Ch.32 documente comment elle s’est déroulée et quelles leçons ont été tirées.

-----
