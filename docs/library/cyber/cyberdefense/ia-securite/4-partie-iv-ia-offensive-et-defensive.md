---
title: PARTIE IV — IA OFFENSIVE ET DÉFENSIVE
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 4
chapters: 7
---

## Ch.16 — L’IA comme outil d’attaque : menaces augmentées par l’IA

### 16.1 Phishing et ingénierie sociale augmentés par l’IA

L’IA générative a transformé le phishing. Les emails de phishing générés par LLM sont grammaticalement parfaits, contextuellement adaptés à la cible (l’attaquant injecte des informations de reconnaissance dans le prompt), et produits à un volume industriel. La barrière historique du phishing — les fautes d’orthographe et les formulations maladroites — a disparu.

Le spear-phishing assisté par IA va plus loin : l’attaquant collecte des informations sur la cible via l’OSINT (profils LinkedIn, publications, organigramme), les injecte dans un LLM avec un prompt de génération d’email contextuel, et produit un message personnalisé indistinguable d’un email légitime. L’ANSSI observe cette tendance et note dans sa synthèse CTI 2026 que des modes opératoires attribués à des groupes chinois, iraniens et nord-coréens utilisent l’IA générative pour la conception de contenus d’ingénierie sociale et la création de faux profils sur les réseaux sociaux.

La conséquence pour la défense est que les filtres historiques basés sur les marqueurs linguistiques deviennent insuffisants. La détection doit évoluer vers l’analyse comportementale (patterns d’envoi, analyse des en-têtes, réputation du domaine), l’authentification renforcée des communications (DMARC strict, SPF, DKIM), et la sensibilisation adaptée (le message n’est plus « méfiez-vous des fautes d’orthographe » mais « vérifiez l’expéditeur et le contexte même si le message est parfaitement rédigé »).

### 16.2 Deepfakes vocaux et vidéo

Le clone vocal est devenu accessible et peu coûteux : quelques secondes d’échantillon vocal suffisent pour produire une imitation convaincante en temps réel. Le vishing (voice phishing) assisté par deepfake vocal permet des arnaques au président d’une efficacité redoutable — la voix du « CEO » au téléphone est indistinguable de l’originale.

Le deepfake vidéo progresse rapidement et a été utilisé dans des cas documentés de fraude au président par visioconférence. Des cas de deepfake dans le recrutement ont également été documentés, notamment dans des opérations attribuées au groupe nord-coréen Lazarus (création de faux profils d’employés avec photos et vidéos générées).

Les défenses incluent la vérification hors-bande (rappeler sur le numéro connu, pas sur le numéro affiché), les protocoles de double validation pour les transactions financières, et les outils de détection de deepfake (encore immatures — les taux de détection varient et les modèles de génération évoluent plus vite que les détecteurs).

### 16.3 Code malveillant généré par IA

Les LLMs peuvent générer du code malveillant — malware, exploits, scripts d’attaque. Les guardrails des fournisseurs freinent les demandes directes mais sont contournables par des techniques de jailbreak. Le premier cas de ransomware assisté par IA a été documenté par ESET en août 2025 : des attaquants avaient utilisé un LLM pour développer et obfusquer leur payload.

Au-delà de la génération directe, l’IA facilite la réécriture et l’obfuscation de malware existant : un malware connu peut être réécrit par un LLM pour contourner les signatures antivirus tout en conservant sa fonctionnalité. Le polymorphisme assisté par IA rend les approches de détection par signature de moins en moins efficaces.

### 16.4 Reconnaissance automatisée et OSINT synthétique

L’IA augmente la reconnaissance (la phase initiale d’une attaque) en permettant la collecte et la corrélation d’informations à grande échelle avec une efficacité humaine réduite. Un attaquant peut utiliser un LLM pour analyser l’organigramme d’une entreprise à partir de LinkedIn, identifier les technologies utilisées à partir des offres d’emploi, corréler les informations provenant de multiples sources, et générer des rapports de reconnaissance structurés.

L’OSINT synthétique — la création de faux profils, de faux sites, de faux contenus pour manipuler la perception — est facilitée par l’IA générative. Des sites web à l’apparence légitime mais entièrement générés par IA ont été observés par l’ANSSI, servant à héberger des charges malveillantes ou à effectuer de la caractérisation de cibles.

### 16.5 Fraude documentaire augmentée par IA

L’IA générative facilite la production de faux documents (attestations, relevés bancaires, certificats) d’une qualité graphique et textuelle qui rend la détection manuelle très difficile. Pour les assurances comme NovaSanté, c’est un risque direct : des fausses déclarations de sinistre avec des pièces justificatives générées par IA.

### 16.6 Implications pour la défense

L’accélération des capacités offensives par l’IA impose une évolution des défenses. Les filtres basés sur des marqueurs statiques (fautes, patterns connus) sont insuffisants. La détection doit intégrer l’analyse comportementale, l’authentification forte des communications, la vérification multi-canal des transactions critiques, et la sensibilisation continue des collaborateurs aux nouvelles formes de menaces. L’ANSSI note cependant que, malgré l’augmentation qualitative, l’IA n’a pas encore permis de réaliser de manière autonome l’intégralité des étapes d’une attaque informatique — l’humain reste dans la boucle d’attaque.

-----

## Ch.17 — L’IA au service de la cybersécurité : potentiel et limites

### 17.1 L’IA dans le SOC

L’IA est de plus en plus intégrée dans les opérations de cybersécurité, principalement dans le SOC. Les cas d’usage matures incluent le tri d’alertes (classification automatique des alertes par criticité et par type — réduit le volume d’alertes à traiter manuellement), la corrélation (identification de liens entre des événements apparemment indépendants), la contextualisation (enrichissement automatique des alertes avec du contexte — CTI, informations sur l’asset, historique), et la détection de phishing par analyse du contenu des emails.

L’IA de type PredAI (ML classique prédictif) est solidement installée dans les SOC pour quatre cas d’usage principaux : le UEBA (User and Entity Behavior Analytics), la détection d’anomalies réseau, la priorisation d’incidents, et la détection de malware. La GenAI (IA générative) s’ajoute comme couche de qualification et de contextualisation des alertes, avec l’émergence de l’Agentic AI (agents IA qui tentent d’automatiser la qualification et, à terme, la remédiation).

L’étude ANSSI de février 2026 sur l’IA au service de la détection recense plus de 50 éditeurs de solutions de cybersécurité intégrant l’IA, et note que la maturité varie considérablement entre les solutions. Les éditeurs pionniers français (Sekoia, HarfangLab, Gatewatcher, Custocy, Sesame IT) développent des approches combinant ML/DL et LLMs.

### 17.2 UEBA et détection d’anomalies

Le UEBA modélise le comportement normal des utilisateurs et des entités (serveurs, endpoints, applications) et alerte quand un comportement dévie significativement. Les forces : capacité à détecter des menaces inconnues (pas besoin de signature), adaptation au contexte spécifique de l’organisation. Les faiblesses : faux positifs fréquents (un comportement inhabituel n’est pas nécessairement malveillant — un collaborateur en déplacement, un changement de poste, une charge de travail exceptionnelle), concept drift (le comportement « normal » évolue), besoin de données d’entraînement propres (un modèle entraîné sur des données déjà compromises est aveugle à la compromission), et temps de calibration initial.

### 17.3 IA pour l’analyse de malware

L’IA facilite la classification automatique des malwares (famille, variante, capacités), l’extraction automatique d’IOC (indicateurs de compromission), et l’analyse statique augmentée (identification de patterns suspects dans le code sans exécution). Les limites : les techniques d’évasion adversariale (modification du malware pour contourner le classifieur IA) sont efficaces, et la classification automatique ne remplace pas l’analyse manuelle pour les menaces nouvelles ou sophistiquées.

### 17.4 Automation bias et overreliance

L’intégration de l’IA dans la cybersécurité introduit un risque humain majeur : l’automation bias (biais d’automatisation) et l’overreliance (surconfiance). L’analyste SOC qui reçoit une qualification automatique d’une alerte par l’IA a tendance à la valider sans vérification approfondie — « l’IA l’a dit, donc c’est vrai ». Ce biais est amplifié par la fatigue d’alerte et la pression de volume.

Les conséquences sont doubles : les faux négatifs de l’IA ne sont pas rattrapés par l’humain (la menace réelle est ignorée parce que l’IA l’a classée comme bénigne), et les faux positifs de l’IA sont confirmés par l’humain (des ressources sont gaspillées à investiguer des non-incidents). Le phénomène d’effondrement de la vigilance humaine quand un système automatisé est en place est bien documenté en ergonomie des systèmes critiques (aviation, médecine).

Les défenses contre l’overreliance incluent la formation explicite des analystes à la faillibilité de l’IA (l’IA est une aide, pas un oracle — ses sorties sont des suggestions à vérifier, pas des verdicts), la rotation des tâches (ne pas laisser un analyste uniquement en mode « validation de l’IA »), les checks croisés (certaines alertes sont volontairement présentées sans la qualification IA pour maintenir la capacité de jugement indépendant), et les métriques de performance individuelle qui mesurent la capacité de détection indépendante, pas seulement le volume traité.

### 17.5 Limites fondamentales de l’IA défensive

L’IA ne comprend pas le contexte métier — elle détecte des patterns statistiques. Une alerte « anomalie de comportement sur le compte du CFO » peut être une compromission ou le CFO qui prépare une acquisition confidentielle. Seul l’humain avec le contexte métier peut discriminer. L’IA est vulnérable aux données adversariales — un attaquant qui connaît (ou devine) les features du modèle de détection peut ajuster son comportement pour rester sous le seuil. Un modèle de détection n’est jamais meilleur que ses données d’entraînement — si les données historiques ne contiennent pas de cas de l’attaque en question, le modèle ne la détectera pas. Et l’explicabilité et la reproductibilité des résultats restent des enjeux majeurs pour l’Agentic AI dans le SOC.

-----

## Ch.18 — Le code AI-generated : risques et gouvernance

### 18.1 L’état des lieux

Les assistants de code IA (GitHub Copilot, Cursor, Claude Code, ChatGPT) sont massivement adoptés par les développeurs. Les gains de productivité sont réels et documentés. Mais le code généré par IA contient fréquemment des vulnérabilités classiques car les modèles reproduisent les patterns du code d’entraînement — y compris les mauvaises pratiques.

Les vulnérabilités les plus courantes dans le code AI-generated incluent les injections (SQL, XSS, commande) par absence de sanitization des entrées, les IDOR (Insecure Direct Object References) par absence de vérification d’autorisation, les secrets en dur (API keys, mots de passe, tokens dans le code source), la cryptographie faible (algorithmes obsolètes, gestion incorrecte des clés, IV statiques), et la gestion incorrecte des erreurs (exceptions silencieuses, messages d’erreur exposant des détails internes).

L’étude conjointe ANSSI-BSI d’octobre 2024 sur les assistants de programmation basés sur l’IA détaille ces risques et formule des recommandations spécifiques. Le document souligne le risque de faux sentiment de sécurité : « l’IA l’a généré donc c’est correct » pousse les développeurs à réduire leur vigilance sur le code qu’ils n’ont pas écrit eux-mêmes.

### 18.2 Risques spécifiques

Au-delà des vulnérabilités dans le code généré, plusieurs risques spécifiques méritent attention.

**L’injection indirecte via les assistants de code.** Un attaquant peut insérer des instructions malveillantes dans la documentation d’un package ou dans un fichier du dépôt. L’assistant de code, qui ingère le contexte du projet (fichiers ouverts, documentation, dépendances), peut exécuter ces instructions en suggérant du code malveillant ou en exfiltrant des informations via les suggestions de code.

**La fuite de code propriétaire.** L’envoi de code source propriétaire à un LLM cloud (Copilot, ChatGPT) pour obtenir des suggestions expose le code au fournisseur. Les conditions d’utilisation varient (certains fournisseurs garantissent de ne pas utiliser le code pour l’entraînement, d’autres non). En production, la politique doit définir clairement quels assistants de code sont autorisés et quelles données peuvent leur être envoyées.

**Le slopsquatting.** Quand un LLM hallucine un nom de package dans ses suggestions de code, un attaquant peut créer un package malveillant portant ce nom. Le développeur qui installe les dépendances suggérées par l’IA installe alors le malware. Ce vecteur a été identifié comme une nouvelle classe d’attaque de supply chain en 2025.

### 18.3 Provenance des snippets, licences et contamination de dépôt

Un risque souvent négligé du code AI-generated est la provenance des fragments suggérés. Le LLM a été entraîné sur du code sous des licences variées (MIT, GPL, Apache, propriétaire) et peut régurgiter des fragments substantiels de code sous licence copyleft (GPL) dans un projet propriétaire, créant un risque juridique de contamination de licence. Le développeur qui accepte une suggestion Copilot ne sait pas si le fragment provient d’un projet GPL — et le fournisseur ne donne généralement pas cette information.

La contamination de dépôt est un risque connexe : un assistant de code qui a accès au contexte du projet (fichiers ouverts, historique git) peut suggérer du code basé sur des fichiers sensibles du dépôt (fichiers de configuration, secrets, code propriétaire critique) et exposer ces informations au fournisseur cloud. Inversement, un attaquant qui contrôle un fichier dans le dépôt (via une pull request malveillante, un package compromis, ou une modification de documentation) peut injecter des instructions qui influenceront les suggestions de l’assistant.

La confiance excessive des développeurs dans les suggestions IA est bien documentée par l’étude conjointe ANSSI-BSI d’octobre 2024. Les développeurs utilisant des assistants IA ont tendance à produire du code avec davantage de vulnérabilités s’ils ne vérifient pas systématiquement, précisément parce que le code suggéré semble correct et professionnel. Le faux sentiment de sécurité — « l’IA l’a généré, donc c’est correct » — est le risque humain principal associé à ces outils.

### 18.4 Gouvernance du code AI-generated

Le code AI-generated doit passer par les mêmes contrôles que le code humain — et éventuellement des contrôles supplémentaires. La politique doit couvrir quand l’utilisation d’un assistant de code est autorisée (pas sur des projets classifiés ou à haute sensibilité si l’assistant est cloud), quelles vérifications sont obligatoires (revue de code systématique, SAST, SCA, tests de sécurité), quelles données peuvent être envoyées au LLM de code (jamais de code propriétaire critique dans un LLM cloud non contractualisé), et la traçabilité (identifier dans le commit quand du code a été généré par IA, pour cibler les revues de sécurité).

-----
