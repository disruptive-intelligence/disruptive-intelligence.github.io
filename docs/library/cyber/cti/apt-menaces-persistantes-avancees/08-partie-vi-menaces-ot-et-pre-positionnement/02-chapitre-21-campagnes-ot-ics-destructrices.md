---
title: Chapitre 21 — Campagnes OT/ICS destructrices
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie VI — Menaces OT ET pré-positionnement
  - index.md
---

Ce chapitre documente les campagnes OT emblématiques dans un ordre globalement chronologique. Ensemble, elles constituent l’**histoire contemporaine** du cyber appliqué aux infrastructures physiques.

## 21.1 Stuxnet (2010) — la première arme cyber OT

**Acteurs** : États-Unis et Israël (co-attribution). **Cible** : centrifugeuses d’enrichissement d’uranium iraniennes à Natanz.

**Traité aux Ch.14 (impact Iran) et Ch.18 (Israël).** Synthèse pour la dimension OT.

**Architecture technique** :

- Quatre **vulnérabilités 0-day Windows** utilisées pour la propagation initiale (inhabituel — un seul 0-day suffirait en général).
- Ciblage extrêmement précis : **ne s’activait que sur des systèmes Windows spécifiques** exécutant **Siemens WinCC/STEP7** (logiciel de programmation PLC Siemens) **connectés à des PLC S7-315 ou S7-417** contrôlant des **centrifugeuses tournant à certaines vitesses spécifiques**. Ces quatre conditions combinées garantissaient que Stuxnet ne s’activerait que sur les systèmes ciblés.
- **Modification de la logique PLC** : une fois sur le système de contrôle, Stuxnet modifiait la programmation du PLC pour faire osciller la vitesse des centrifugeuses entre limites extrêmes, provoquant des contraintes mécaniques qui les détruisaient progressivement.
- **Masquage** : parallèlement, Stuxnet interceptait les signaux de télémétrie et **affichait des valeurs normales aux opérateurs**. Les ingénieurs voyaient sur leurs HMI que tout fonctionnait normalement pendant que les centrifugeuses s’auto-détruisaient.

**Impact** : environ 1 000 centrifugeuses détruites entre 2008 et 2010, programme iranien retardé de 2-3 ans selon les estimations.

**Leçons OT** :

- **Les PLC peuvent être manipulés avec effet physique** : démonstration fondatrice.
- **Le masquage des opérateurs est possible et dangereux** : les HMI peuvent mentir.
- **Les engineering workstations sont des cibles critiques** : Stuxnet utilisait l’engineering workstation Siemens pour modifier le PLC.
- **La propagation non contrôlée** : Stuxnet s’est échappé des systèmes ciblés via USB, révélant l’opération. Le risque de « blowback » des armes cyber est réel.

## 21.2 BlackEnergy / KillDisk — Ukraine décembre 2015

**Acteur** : Sandworm (GRU Unit 74455). **Cible** : trois distributeurs d’électricité ukrainiens — Prykarpattyaoblenergo, Kyivoblenergo, Chernivtsioblenergo. **Premier blackout cyber confirmé de l’histoire**.

**Chronologie** :

- **Printemps-été 2015** : phase de reconnaissance et compromission initiale via spear-phishing (documents Office avec macro, envoyés à des ingénieurs des distributeurs).
- **Plusieurs mois** : mouvement latéral, compromission des systèmes de supervision, pivot vers les segments OT.
- **23 décembre 2015, 15h30** : déclenchement. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA.

**Mécanisme de l’attaque** :

- **Prise de contrôle manuelle** des HMI via des outils d’administration à distance. Les opérateurs ukrainiens ont vu, sur leurs propres écrans, leurs souris bouger et leur clavier taper sans leur action.
- **Ouverture manuelle de 30+ disjoncteurs** dans les postes de transformation.
- **230 000 foyers** privés d’électricité pendant ~6 heures.
- **KillDisk** déployé en parallèle : wiper effaçant les systèmes de supervision pour compliquer la récupération et prolonger l’indisponibilité.

**Particularité** : l’attaque a été **largement manuelle** — des opérateurs humains cliquant sur des HMI à distance. Pas de malware automatisé qui commande les équipements. Cette approche indique une compréhension fine du système mais aussi une prise de risque (l’opération prenait du temps, les défenseurs pouvaient réagir).

**Restoration** : les opérateurs ukrainiens, entraînés à basculer en mode manuel, ont rétabli l’alimentation en parcourant physiquement les postes et en refermant les disjoncteurs manuellement.

**Attribution** : CERT-UA, SBU, puis Mandiant et d’autres — attribution à Sandworm publiée en 2016-2017.

**Leçons** :

- **Un blackout cyber est possible** : démonstration empirique.
- **Les opérateurs entraînés peuvent récupérer rapidement** : la capacité de basculer en manuel est un élément de résilience majeur.
- **KillDisk en complément** : pattern Sandworm de combiner attaque et wiper pour maximiser l’indisponibilité.

## 21.3 Industroyer / CrashOverride — Ukraine décembre 2016

**Acteur** : Sandworm. **Cible** : poste de transformation électrique de la banlieue de Kiev.

**Rupture par rapport à 2015** : Industroyer est le **premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles industriels natifs**. Contrairement à 2015 où l’attaque était manuelle, Industroyer **automatise** la manipulation des équipements.

**Architecture Industroyer** :

- **Module IEC 60870-5-101** : protocole série électrique.
- **Module IEC 60870-5-104** : version TCP/IP du précédent, protocole dominant en Europe. Le module peut énumérer les équipements et **commander l’ouverture/fermeture des disjoncteurs**.
- **Module IEC 61850** : protocole des sous-stations modernes. Peut émettre des commandes GOOSE.
- **Module OPC DA** : intégration SCADA/DCS.
- **Module de wiping** : destruction des configurations et des systèmes de supervision.
- **Backdoor** pour la persistence et l’accès ultérieur.

**Déclenchement** : 17 décembre 2016, minuit. Le module IEC 104 ouvre les disjoncteurs. Blackout dans une partie de Kiev pendant ~1 heure.

**Sophistication** : Industroyer démontre que Sandworm a investi dans des capacités OT sur mesure. Chaque module représente une compréhension approfondie du protocole correspondant et des systèmes qui l’implémentent.

**Attribution** : attribution à Sandworm confirmée par ESET (qui a analysé le malware en profondeur — rapport fondateur de juin 2017) et par les agences Five Eyes.

**Leçons** :

- **Le cyber OT est industrialisable** : pas seulement des attaques ponctuelles manuelles, mais des outils sophistiqués réutilisables.
- **Les protocoles sans authentification sont des leviers d’attaque directs** : IEC 104, IEC 61850 — pas d’authentification, commandes exécutées sans challenge.
- **L’investissement OT des acteurs étatiques est sérieux** : développer Industroyer a pris probablement 1-2 ans d’effort.

## 21.4 Triton / TRISIS — Arabie Saoudite 2017

**Acteur** : attribué à la Russie, plus précisément au **Central Scientific Research Institute of Chemistry and Mechanics (TsNIIKhM)** — institut de recherche militaire russe, sanctionné par OFAC en 2020. **Cible** : usine pétrochimique saoudienne (non nommée publiquement, mais largement identifiée comme Petro Rabigh).

**Rupture** : Triton est le premier malware à avoir ciblé explicitement des **SIS** (Safety Instrumented Systems) — les systèmes de sécurité ultimes.

**Cible spécifique** : **Schneider Triconex** — marque emblématique de SIS, largement déployée dans l’industrie pétrochimique et nucléaire. Triton était conçu pour reprogrammer les Triconex, désactivant potentiellement leurs fonctions de sécurité.

**Scénario envisagé** : si Triton avait réussi pleinement, l’attaquant aurait pu, à un moment choisi, **désactiver les SIS puis provoquer une condition dangereuse** dans le processus industriel. Sans SIS pour déclencher le shutdown, l’installation atteint potentiellement des conditions d’**explosion ou de fuite toxique**. Les dommages envisageables incluaient des pertes humaines significatives.

**Comment Triton a été découvert** : par **accident**. Lors d’une intervention Triton sur un Triconex, le malware a provoqué un **arrêt de sécurité non anticipé** — le Triconex a détecté une anomalie dans sa propre programmation et s’est mis en mode sûr (shutdown). Les ingénieurs saoudiens, cherchant à comprendre pourquoi leur SIS s’était arrêté, ont découvert la compromission.

**Attribution** : Dragos a attribué Triton à un acteur qu’il a nommé **XENOTIME**. L’attribution plus précise au TsNIIKhM russe a été établie par le FBI et publiée via sanctions OFAC en 2020.

**Implication stratégique** : Triton est **le wake-up call** sur les risques OT. Un État avait investi dans une capacité visant à pouvoir, à un moment politique choisi, causer des morts via cyber. La ligne entre cyber et terrorisme d’État est franchie, ou près de l’être.

**Leçons OT** :

- **Les SIS sont des cibles APT** : ne plus considérer les SIS comme « naturellement protégés » parce que « critiques ».
- **L’air gap SIS est indispensable** : isolation totale.
- **Des capacités SIS sont en développement** : au-delà de Triton, d’autres acteurs étatiques ont probablement des capacités similaires. XENOTIME est suivi comme groupe actif.

## 21.5 Industroyer2 — Ukraine avril 2022

**Acteur** : Sandworm. **Cible** : un opérateur électrique ukrainien (non nommé publiquement mais situé dans la région de Kiev).

**Contexte** : dans les semaines suivant l’invasion russe de l’Ukraine (24 février 2022), Sandworm tente de reproduire son succès de 2016 en développant **Industroyer2** — évolution du malware de 2016.

**Améliorations Industroyer2** :

- Modules protocoles OT conservés.
- Ciblage plus précis (adapté à la victime spécifique).
- Pattern de déclenchement synchronisé avec d’autres opérations (wiper CaddyWiper prévu en parallèle pour complexifier la réponse).

**Échec grâce à la défense** : **Industroyer2 a été déjoué**. L’équipe CERT-UA, en collaboration avec **ESET**, a détecté le déploiement avant le déclenchement prévu. Une analyse rapide a permis la neutralisation en quelques heures. Le déclenchement prévu n’a pas eu lieu, ou seulement avec des effets très limités.

**Signification** : succès défensif majeur. Démonstration que la coopération CERT-UA/vendor CTI peut neutraliser une attaque OT étatique avant impact. C’est un modèle opérationnel étudié par toutes les agences cyber occidentales.

**Publication** : rapport conjoint CERT-UA et ESET (avril 2022) documente le malware et la réponse défensive. Lecture importante pour comprendre l’état de l’art OT défensif.

## 21.6 Colonial Pipeline (mai 2021) — ransomware IT avec impact OT

**Acteur** : **DarkSide** (groupe RaaS russophone). **Cible** : **Colonial Pipeline**, opérateur d’un oléoduc majeur transportant ~45% de l’essence consommée sur la côte est américaine.

**Particularité** : Colonial Pipeline illustre un pattern où **le cyber IT produit un impact OT indirect**, sans que l’OT soit directement compromis.

**Chronologie** :

- Compromission initiale via un **compte VPN sans MFA** (credentials probablement issus d’un breach ou d’un infostealer).
- Déploiement de DarkSide sur le réseau IT.
- **7 mai 2021** : Colonial Pipeline **coupe volontairement l’OT** — par mesure de précaution, l’entreprise arrête l’oléoduc parce qu’elle ne peut pas garantir que l’OT n’a pas été compromis et parce que le système de facturation (IT) est inopérant (pas de moyen de facturer les clients).
- **Impact** : pénuries d’essence sur la côte est US pendant plusieurs jours, situation d’urgence déclarée par le gouverneur de plusieurs États.
- Colonial Pipeline paie une rançon d’environ 4,4 millions de dollars en Bitcoin (dont environ 2,3 millions seront **récupérés ultérieurement par le FBI** — première récupération notable de rançon crypto).

**Leçons** :

- **La convergence IT/OT crée des dépendances opérationnelles** : même sans compromission OT directe, un incident IT peut paralyser l’OT (par précaution légitime ou par dépendance business — facturation, logistique).
- **Les credentials VPN sont un vecteur majeur** : MFA sur les accès distants n’est pas optionnel.
- **Le paiement de rançon peut être partiellement récupéré** : coopération FBI/exchanges/blockchain intelligence.
- **Conséquences macroéconomiques** : une cyberattaque sur une infrastructure critique peut produire des effets au niveau sociétal (pénuries, urgence).

## 21.7 CosmicEnergy — malware Sandworm découvert 2023

**Acteur** : Sandworm (probablement). **Découverte** : Mandiant a publié en mai 2023 l’analyse d’un nouveau malware OT nommé **CosmicEnergy**, trouvé sur **VirusTotal** (uploadé par quelqu’un — probablement l’auteur, un chercheur, ou une victime).

**Capacités** : CosmicEnergy cible les **systèmes de protection IEC 60870-5-104** — similaire à Industroyer mais avec des différences techniques suggérant une évolution distincte. Peut envoyer des commandes IEC 104 pour ouvrir/fermer des équipements.

**Incertitude** : l’utilisation opérationnelle de CosmicEnergy n’est pas confirmée publiquement — il peut s’agir d’un malware en développement, d’un outil de red team russe, ou d’un malware qui n’a pas encore été déployé.

**Signification** : démonstration que le **développement d’outils OT offensifs continue**. Sandworm (ou des acteurs apparentés) investit dans une nouvelle génération de capacités OT. La menace reste active et évolutive.

## 21.8 Attaques récentes 2024-2025

**Cyber Av3ngers contre l’eau (fin 2023 - 2024)** : groupe attribué à l’Iran (IRGC) qui a ciblé des **PLC Unitronics exposés sur Internet** dans des systèmes d’eau municipaux américains. Impact limité (message politique sur les écrans HMI, pas de perturbation majeure du processus), mais démonstration symbolique forte. A conduit à une mobilisation CISA et à des advisories aux opérateurs d’eau.

**Tentatives sur les opérateurs électriques européens (2023-2025)** : advisory ANSSI et BSI ont évoqué publiquement (sans nommer de cibles) des tentatives d’intrusion dans des opérateurs électriques européens. Attribution variable entre acteurs russes (Sandworm, Unit 29155) et acteurs chinois.

**Ciblage d’installations oil & gas et pétrochimiques** : depuis 2022, plusieurs incidents non rendus publics, mais des rapports Dragos et Mandiant font état d’une activité croissante. Certaines compagnies pétrolières européennes ont renforcé publiquement leurs équipes OT security.

**Le contexte général 2024-2026** : les attaques OT se multiplient en tentatives, avec relativement peu d’impacts majeurs publics en Europe. Mais la pression est croissante, et le modèle BLACKOUT (pré-positionnement sans action immédiate) est probablement plus fréquent que les incidents publics ne le suggèrent.

## 21.9 Leçons générales des campagnes OT

La synthèse des campagnes OT documentées dessine un **corpus de leçons transversales**.

**Le cyber OT est réel et testé** : Stuxnet, Industroyer, Triton, Industroyer2, CosmicEnergy démontrent qu’au moins trois États (US/Israël, Russie, avec d’autres probablement) ont des capacités OT opérationnelles. Ce n’est pas une menace théorique.

**L’impact potentiel est physique** : blackouts, explosions potentielles (Triton), paralysies opérationnelles (Colonial). Le cyber peut produire des dommages comparables à des frappes militaires conventionnelles dans certains scénarios.

**La sophistication requise est importante** : développer un malware OT fonctionnel est un effort d’années pour des équipes expertes. Ce n’est pas à la portée d’un cybercriminel classique. Mais c’est à la portée de plusieurs États.

**Les défenses sont possibles** : Industroyer2 déjoué démontre qu’une défense OT bien préparée peut neutraliser une attaque étatique. La visibilité, la collaboration, et la rapidité de réponse sont les facteurs clés.

**Le pré-positionnement est la tendance actuelle** : moins d’attaques destructives déclenchées, plus d’opérations qui maintiennent un accès dormant. Ce pattern est l’objet du chapitre suivant.

-----
