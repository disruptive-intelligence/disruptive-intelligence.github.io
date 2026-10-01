---
title: Chapitre 9 — Hébergement, infrastructure et résilience
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie II — Infrastructures techniques et anonymat
  - index.md
---

Les services illicites du dark web ne sont pas hébergés par magie. Un serveur physique existe quelque part, avec un opérateur, une facture d'hébergement, et une exposition juridique — même masqués par Tor. Comprendre les mécanismes d'hébergement permet de comprendre où sont les points de défaillance.

## 9.1 Les choix d'hébergement d'un service .onion

L'opérateur d'un service .onion a plusieurs options.

**Hébergement classique dans un pays « coopératif »** : un VPS chez OVH, Hetzner, Digital Ocean, AWS. Facile, bon marché, mais **totalement exposé à une saisie** si l'opérateur est identifié. La plupart des grandes saisies de marchés dark web ont concerné des infrastructures hébergées dans des clouds classiques — Silk Road chez des hébergeurs américains et islandais, AlphaBay chez des hébergeurs lituaniens, etc.

**Bulletproof hosting** : hébergeurs situés dans des juridictions où la coopération avec les forces de l'ordre est limitée (historiquement Russie, quelques pays d'Europe de l'Est, certaines zones asiatiques), ou hébergeurs qui se spécialisent explicitement dans l'hébergement de contenus « contestés ». Prix 5 à 10 fois plus élevés qu'un hébergement classique, mais résistance accrue. Bulletproof **ne signifie pas invulnérable** — plusieurs grands bulletproof hosts ont été saisis (Atrivo/Intercage 2008, McColo 2008, Russian Business Network, Hostinger/Cyberbunker 2019).

**Auto-hébergement physique** : machine chez soi ou dans un local loué, connexion Internet standard, Tor masquant l'IP. Solution la plus résiliente juridiquement (pas de tiers coopératif à contacter pour les autorités) mais la plus risquée pour l'opérateur (saisie physique de son domicile s'il est identifié, pas de redondance).

**Hébergement distribué** : plusieurs serveurs miroirs dans plusieurs pays, avec load balancing. Augmente la résilience, mais chaque miroir est un point de compromission potentiel.

**Hybrides** : opérateurs sophistiqués combinent plusieurs approches. Un frontend bulletproof pour la face publique, un backend chez un hébergeur différent moins exposé, des backups chiffrés distribués.

## 9.2 Les mécanismes de résilience typiques

Les grands services clandestins mettent en place plusieurs mécanismes pour survivre aux tentatives de saisie.

**Multiple onion addresses**. Un même service peut publier plusieurs adresses .onion (v3 le permet), avec load balancing via onion-balance. Si une adresse est compromise, les autres restent fonctionnelles.

**Rotation d'adresse**. Certains services changent d'adresse .onion périodiquement (tous les X mois) et communiquent la nouvelle aux utilisateurs via des canaux out-of-band (Telegram, XMPP, mailing list chiffrée). Complique le monitoring long terme mais cohérent avec une posture défensive.

**Multiple darknets**. Maintenir simultanément un .onion et un .i2p (ou Lokinet, ou Freenet) — si un darknet devient intenable, l'autre reste. IndustrialLeaks (fictif) illustre ce pattern.

**Infrastructure distribuée**. Frontend, backend, base de données, stockage de fichiers sur des machines séparées, dans des juridictions différentes. Saisir le frontend ne suffit pas ; il faut aussi identifier les autres composants.

**Clés hors ligne**. Les clés privées les plus critiques (signature des annonces, wallet principal) sont conservées hors ligne, sur des machines air-gapped. Une saisie du serveur public ne donne pas accès aux fonds principaux.

**Backups chiffrés**. Les données opérationnelles sont régulièrement sauvegardées chiffrées sur des infrastructures tierces (cloud storage avec chiffrement client-side, stockage distribué type IPFS). Permet de relancer le service même après saisie complète du serveur principal.

**Kill switches**. Certains opérateurs implémentent des kill switches qui effacent automatiquement les données en cas de signes de compromission (pas d'accès admin depuis X heures, tentative de boot sans la bonne clé). Destiné à limiter les preuves collectables lors d'une saisie.

## 9.3 Les points d'attaque des forces de l'ordre

Face à cette résilience, les investigateurs visent les points de faiblesse structurels.

**Identification de l'opérateur**. La méthode la plus efficace historiquement. Une fois l'opérateur identifié, son domicile/bureau peut être perquisitionné, ses infrastructures connues saisies simultanément, et ses clés capturées avant qu'il ne puisse les détruire. Ulbricht capturé ordinateur ouvert, Cazes de même en Thaïlande.

**Vulnérabilités applicatives du service**. Une SQL injection, une RCE, une mauvaise configuration CORS peuvent exposer l'IP réelle du serveur. Les services matures font tester régulièrement leur propre sécurité ; les services amateurs sont souvent identifiables ainsi.

**Fuites d'infrastructure**. Headers HTTP qui révèlent le vrai IP, certificats TLS utilisés à la fois sur clearnet et onion, iframes vers des ressources externes qui font un DNS lookup hors Tor, misconfigurations NTP. Le Tor Project publie régulièrement des recommandations pour éviter ces fuites, mais toutes ne sont pas suivies.

**Analyse de trafic**. Pour un adversaire qui peut observer le trafic entrant/sortant d'un hébergeur suspect, corréler avec les patterns d'activité du service .onion peut permettre d'identifier le serveur. Technique coûteuse, mais documentée dans plusieurs investigations.

**Infiltration**. Opérer le service depuis l'intérieur après saisie (Hansa model) ou infiltrer des comptes admin via social engineering, compromission de machines d'opérateurs, ou pivoting via des services tiers qu'ils utilisent.

**Coopération de l'hébergeur**. Pour les services hébergés chez des clouds mainstream, une simple requête légale suffit à obtenir l'identité du client. C'est pourquoi les opérateurs sérieux n'utilisent pas ces hébergeurs — mais beaucoup d'amateurs le font, et les petits services tombent souvent ainsi.

## 9.4 Le cas emblématique des bulletproof hosts

**Cyberbunker** (originellement Pays-Bas, puis Allemagne) : ancien bunker OTAN reconverti en bulletproof host à partir de 2013. Hébergeait des marchés dark web, des CSAM, des infrastructures criminelles. Saisi en septembre 2019 par la police allemande après une opération de surveillance de trois ans. Le fondateur et plusieurs associés condamnés en 2021. Cas souvent cité comme démonstration que même les bulletproof hosts finissent par tomber.

**Russian Business Network (RBN)** : actif dans les années 2000, St Pétersbourg. Hébergeait malware, phishing, botnets. Jamais saisi stricto sensu, mais progressivement neutralisé par pression sur ses opérateurs de paiement et upstream providers. Dissolution de facto vers 2009.

**Atrivo/Intercage** : US, fermé en 2008 suite à une campagne de denaming par les autres hébergeurs (« de-peering ») qui ont refusé de lui faire du transit.

**McColo** : US, fermé en 2008 de la même manière.

Ces cas illustrent un pattern : les bulletproof hosts finissent par être neutralisés, soit par saisie directe, soit par pression sur leur écosystème (upstream providers, moyens de paiement, banquiers). Durée de vie typique : 5 à 15 ans. Rarement plus.

## 9.5 L'émergence des « underground ISPs »

Ces dernières années, certains acteurs ont tenté de construire des **infrastructures d'ISP entièrement sous contrôle** — leurs propres connexions Internet, leurs propres IPs, leur propre transit. L'idée : ne plus dépendre d'un hébergeur tiers saisissable, mais opérer comme un FAI miniature.

Cas observés avec profils divers : hébergeurs ayant leur propre AS (Autonomous System) BGP dans des juridictions permissives, liaisons satellite pour bypass des FAI nationaux, infrastructure mesh dans des zones sans contrôle étatique effectif. Reste marginal — exige des investissements importants et des compétences techniques avancées.

## 9.6 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5 : analyse d'infrastructure**
>
> Lucas documente ce qu'il peut apprendre de l'infrastructure d'IndustrialLeaks. Depuis le forum lui-même, peu d'indices techniques directs — les opérateurs ont suivi les bonnes pratiques OPSEC.
>
> Mais plusieurs signaux indirects :
> - **Trois changements d'adresse .onion** en 18 mois, toujours annoncés à l'avance sur un canal Telegram public associé au forum. Cohérent avec une posture défensive proactive (pas avec une saisie réussie — pas d'interruption longue observable).
> - **Miroir I2P fonctionnel**, avec la même base de données (posts synchronisés). Indique une architecture centralisée avec deux points d'accès plutôt que deux services indépendants.
> - **Disponibilité élevée** : le forum répond en ~800 ms la plupart du temps, quelques pannes de 2-4 heures observables dans les archives communautaires. Cohérent avec un hébergement sérieux, possiblement bulletproof.
> - **Règles internes publiées** : modération active, bannissements documentés, posts de warning aux scammers. Indique un opérateur impliqué, pas un dump-and-forget.
>
> Hypothèse de travail : IndustrialLeaks est probablement hébergé sur un bulletproof host d'Europe de l'Est, avec une équipe de 2-5 opérateurs (un admin principal, des modérateurs russophones), et une infrastructure miroir I2P active. Son modèle économique : droits d'entrée (250 USD × 3 000 membres = ~750 000 USD si on suppose tous payants — irréaliste, plus réaliste quelques centaines de payants), commissions sur ventes (1-3% probablement), peut-être services premium.
>
> Pour Lucas, les implications d'investigation : accès via vouching (privilégier pour la crédibilité de la persona d'investigation), attentes réalistes de durée de vie (1-3 ans avant rotation ou saisie), priorité à la capture d'indices d'authentification des données **avant** que le forum ne disparaisse.

---
