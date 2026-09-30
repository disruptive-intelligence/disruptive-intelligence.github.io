---
title: 'Ch.16 — L’IA comme outil d’attaque : menaces augmentées par l’IA'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
up:
- - IA & sécurité
  - ../index.md
- - Partie IV — IA offensive et défensive
  - index.md
---

## 16.1 Phishing et ingénierie sociale augmentés par l’IA

L’IA générative a transformé le phishing. Les emails de phishing générés par LLM sont grammaticalement parfaits, contextuellement adaptés à la cible (l’attaquant injecte des informations de reconnaissance dans le prompt), et produits à un volume industriel. La barrière historique du phishing — les fautes d’orthographe et les formulations maladroites — a disparu.

Le spear-phishing assisté par IA va plus loin : l’attaquant collecte des informations sur la cible via l’OSINT (profils LinkedIn, publications, organigramme), les injecte dans un LLM avec un prompt de génération d’email contextuel, et produit un message personnalisé indistinguable d’un email légitime. L’ANSSI observe cette tendance et note dans sa synthèse CTI 2026 que des modes opératoires attribués à des groupes chinois, iraniens et nord-coréens utilisent l’IA générative pour la conception de contenus d’ingénierie sociale et la création de faux profils sur les réseaux sociaux.

La conséquence pour la défense est que les filtres historiques basés sur les marqueurs linguistiques deviennent insuffisants. La détection doit évoluer vers l’analyse comportementale (patterns d’envoi, analyse des en-têtes, réputation du domaine), l’authentification renforcée des communications (DMARC strict, SPF, DKIM), et la sensibilisation adaptée (le message n’est plus « méfiez-vous des fautes d’orthographe » mais « vérifiez l’expéditeur et le contexte même si le message est parfaitement rédigé »).

## 16.2 Deepfakes vocaux et vidéo

Le clone vocal est devenu accessible et peu coûteux : quelques secondes d’échantillon vocal suffisent pour produire une imitation convaincante en temps réel. Le vishing (voice phishing) assisté par deepfake vocal permet des arnaques au président d’une efficacité redoutable — la voix du « CEO » au téléphone est indistinguable de l’originale.

Le deepfake vidéo progresse rapidement et a été utilisé dans des cas documentés de fraude au président par visioconférence. Des cas de deepfake dans le recrutement ont également été documentés, notamment dans des opérations attribuées au groupe nord-coréen Lazarus (création de faux profils d’employés avec photos et vidéos générées).

Les défenses incluent la vérification hors-bande (rappeler sur le numéro connu, pas sur le numéro affiché), les protocoles de double validation pour les transactions financières, et les outils de détection de deepfake (encore immatures — les taux de détection varient et les modèles de génération évoluent plus vite que les détecteurs).

## 16.3 Code malveillant généré par IA

Les LLMs peuvent générer du code malveillant — malware, exploits, scripts d’attaque. Les guardrails des fournisseurs freinent les demandes directes mais sont contournables par des techniques de jailbreak. Le premier cas de ransomware assisté par IA a été documenté par ESET en août 2025 : des attaquants avaient utilisé un LLM pour développer et obfusquer leur payload.

Au-delà de la génération directe, l’IA facilite la réécriture et l’obfuscation de malware existant : un malware connu peut être réécrit par un LLM pour contourner les signatures antivirus tout en conservant sa fonctionnalité. Le polymorphisme assisté par IA rend les approches de détection par signature de moins en moins efficaces.

## 16.4 Reconnaissance automatisée et OSINT synthétique

L’IA augmente la reconnaissance (la phase initiale d’une attaque) en permettant la collecte et la corrélation d’informations à grande échelle avec une efficacité humaine réduite. Un attaquant peut utiliser un LLM pour analyser l’organigramme d’une entreprise à partir de LinkedIn, identifier les technologies utilisées à partir des offres d’emploi, corréler les informations provenant de multiples sources, et générer des rapports de reconnaissance structurés.

L’OSINT synthétique — la création de faux profils, de faux sites, de faux contenus pour manipuler la perception — est facilitée par l’IA générative. Des sites web à l’apparence légitime mais entièrement générés par IA ont été observés par l’ANSSI, servant à héberger des charges malveillantes ou à effectuer de la caractérisation de cibles.

## 16.5 Fraude documentaire augmentée par IA

L’IA générative facilite la production de faux documents (attestations, relevés bancaires, certificats) d’une qualité graphique et textuelle qui rend la détection manuelle très difficile. Pour les assurances comme NovaSanté, c’est un risque direct : des fausses déclarations de sinistre avec des pièces justificatives générées par IA.

## 16.6 Implications pour la défense

L’accélération des capacités offensives par l’IA impose une évolution des défenses. Les filtres basés sur des marqueurs statiques (fautes, patterns connus) sont insuffisants. La détection doit intégrer l’analyse comportementale, l’authentification forte des communications, la vérification multi-canal des transactions critiques, et la sensibilisation continue des collaborateurs aux nouvelles formes de menaces. L’ANSSI note cependant que, malgré l’augmentation qualitative, l’IA n’a pas encore permis de réaliser de manière autonome l’intégralité des étapes d’une attaque informatique — l’humain reste dans la boucle d’attaque.

-----
