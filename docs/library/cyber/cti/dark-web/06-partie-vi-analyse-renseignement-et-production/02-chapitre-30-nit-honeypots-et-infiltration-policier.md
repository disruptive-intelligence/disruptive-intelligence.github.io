---
title: Chapitre 30 — NIT, honeypots et infiltration policière
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

Ce chapitre couvre les techniques **policières** de dé-anonymisation et d'infiltration. Même si elles ne sont pas accessibles aux analystes privés, les comprendre est essentiel pour deux raisons : elles expliquent comment les grandes saisies ont été possibles, et elles informent la vigilance OPSEC des analystes (qui peuvent eux-mêmes être ciblés par erreur ou par ciblage adversaire).

## 30.1 NIT — Network Investigative Techniques

Les **NIT** sont des techniques techniques utilisées par les forces de l'ordre (principalement FBI historiquement) pour identifier les IPs réelles d'utilisateurs Tor, par exploitation de vulnérabilités.

**Principe général** : le FBI (ou équivalent) prend le contrôle d'un service .onion (via saisie précédente du serveur, ou infiltration de l'opérateur), puis injecte dans les pages servies un **exploit** qui cible le navigateur de la victime. L'exploit fait exécuter du code sur la machine de la victime et provoque une communication hors-Tor vers un serveur FBI, révélant l'IP réelle.

**Opération Playpen (2015)** — référence historique. Le FBI saisit Playpen (site CSAM .onion), continue son opération pendant **deux semaines** depuis ses propres serveurs, et déploie une NIT contre les visiteurs. Résultat : plus de 1 000 IPs identifiées aux US, des centaines d'autres à l'international. **Des centaines d'arrestations** découlent de cette opération.

Controverses Playpen :

- Légalité contestée — le FBI a opéré un site criminel actif pendant deux semaines pour tendre le piège.
- Jurisprudence complexe — plusieurs condamnations ont été annulées en appel sur des motifs procéduraux (warrant unique couvrant multiple juridictions).
- Révélation des techniques — le FBI a fait appel jusqu'à la Cour Suprême pour éviter de divulguer le code exploit utilisé, que les avocats de défense exigeaient pour vérifier son fonctionnement.

**Opération Pacifier (lié à Playpen)**. Suite d'opérations mondiales coordonnées.

**Freedom Hosting saisie (2013)**. Le FBI avait saisi Freedom Hosting (hébergeur de nombreux .onion CSAM) et injecté une NIT dans les pages servies. Exploit ciblait Tor Browser / Firefox ESR de l'époque. Efficace sur les utilisateurs en mode non-Safest.

**Leçon OPSEC**. Tor Browser en **mode Safest** (JavaScript désactivé) neutralise la quasi-totalité des NIT documentées, qui reposent sur exécution de JavaScript pour déployer l'exploit. C'est pourquoi tout analyste investigant le dark web opère en Safest par défaut.

## 30.2 Les honeypots

Un **honeypot** est un service déployé intentionnellement pour attirer et observer les attaquants / visiteurs suspects.

**Honeypot CSAM** (plusieurs cas documentés). Les autorités créent ou prennent le contrôle de services qui attirent les criminels de cette catégorie. Collecte d'IPs, identification, arrestations.

**Honeypot marketplace / forum**. Un marché « trop beau pour être vrai » (prix cassés, vendeurs toujours disponibles, fonctionnalités inhabituelles) peut être un honeypot. Difficile à confirmer pour les participants.

**Honeypot accès corporate**. Défenseurs déploient des systèmes qui ressemblent à des cibles attractives (RDP, VPN, Citrix) pour capturer les tentatives et étudier les TTPs. Côté défensif, moins investigatif offensif.

**Sentinels et watermarks**. Versions des outils ou données avec markers individuels. Un acheteur d'un dump peut recevoir une copie avec un identifiant spécifique — si ce dump apparaît ailleurs, l'identifiant révèle qui l'a revendu.

## 30.3 Les infiltrations coordonnées

Les grandes opérations policières combinent plusieurs techniques sur la durée.

**Operation Bayonet (AlphaBay + Hansa, 2017)** — cas d'école. Ch.2 a décrit la séquence : saisie AlphaBay + prise de contrôle de Hansa + opération silencieuse de 30 jours pour capter les migrants, puis annonce simultanée. L'infiltration a nécessité :

- Identification préalable de Cazes (opérateur AlphaBay) via ses erreurs OPSEC.
- Identification de l'infrastructure Hansa via investigation technique.
- Coordination internationale (FBI US, DEA, Police Nationale néerlandaise, Europol, agences de 7 pays).
- Secrecy opérationnelle pendant des mois.

**Operation Cronos (LockBit, 2024)**. Coordination NCA UK, FBI, Europol, forces de 10+ pays. Saisie d'infrastructure LockBit, identification de Dmitry Khoroshev comme LockBitSupp, publication de clés de déchiffrement. Amorcé par années d'investigation technique et humaine.

**Operation Endgame (2024)**. Opération Europol ciblant multiple botnets et infostealers. Démantèlement simultané de plusieurs infrastructures.

**Operation Cookie Monster (Genesis Market, 2023)**. Coordination FBI, Europol, forces de 17 pays. Saisie du marché de logs, arrestations de 120+ utilisateurs, identification de dizaines de milliers d'acheteurs.

**Kidflix (mars 2025)**. Opération contre plateforme CSAM. Démantèlement et arrestations internationales coordonnées.

**BreachForums (multiple saisies)**. Plusieurs saisies successives (mars 2023 avec Pompompurin arrêté, juillet 2024 avec Baphomet arrêté, reprise par ShinyHunters puis nouvelles actions).

Ces opérations illustrent la **capacité croissante** des autorités à coordonner des actions à échelle mondiale. Pour un acteur du dark web, la marge d'opération se réduit.

## 30.4 L'infiltration humaine

Au-delà des moyens techniques, l'infiltration humaine reste un pilier.

**Agents infiltrés**. Un officier se crée une persona dans l'écosystème et monte progressivement. Rare en pratique (coût et risques élevés), mais pratiqué. Limité aux forces de l'ordre.

**Coopération de sources arrêtées**. Un acteur arrêté peut coopérer en échange de réduction de peine. Fournit informations sur ses contacts, ses méthodes, ses partenaires. Multiplie les arrestations en cascade.

**Informateurs**. Acteurs qui coopèrent préventivement, parfois pour éliminer des concurrents, parfois par repentir, parfois par pression discrète.

**Trolling stratégique**. Semer le doute dans une communauté — faire croire à une infiltration, créer conflits internes, déstabiliser la confiance. Peut provoquer exit scams ou fractures communautaires.

## 30.5 Les hacks et deep leaks

Certaines enquêtes bénéficient de **leaks externes** non-autorisés.

**ContiLeaks (2022)**. Un dissident interne de Conti (possiblement ukrainien, en réaction à l'alignement de Conti avec la position russe sur la guerre en Ukraine) a publié massivement les communications internes du groupe. Des dizaines de milliers de messages, les outils, les discussions opérationnelles. **Révélations** : structure hiérarchique, montants traités, liens présumés avec FSB. Impact investigatif immense — Conti a dû se restructurer (via reformulation en multiple groupes affiliés).

**Leak de chats LockBit post-Cronos**. Communications internes révélées par les autorités dans le cadre d'Operation Cronos.

**Autres leaks**. Babuk (2021), Lapsus$ (2022 via membres arrêtés), et d'autres — chaque leak apporte une richesse investigative considérable.

**Ironie du dark web** : les groupes qui vivent de la fuite des données d'autrui sont eux-mêmes victimes de leaks qui les exposent. L'écosystème est fondamentalement hostile — alliances précaires, dissidents fréquents.

## 30.6 Implications pour l'analyste privé

L'analyste ne mène pas d'opérations offensives ni d'infiltration active. Mais il doit :

**Comprendre ces capacités**. Pour ne pas sur-attribuer à l'analyse privée ce qui relève des services publics. Une investigation privée ne démantèle pas un groupe ransomware — elle documente.

**Collaborer avec les autorités**. Les capacités privées et publiques sont complémentaires. Le privé observe en grand, remonte les signaux, contextualise. Le public peut agir coercitivement.

**Maintenir OPSEC défensive**. Les mêmes techniques (NIT, honeypots, infiltration) peuvent être utilisées par adversaires (APT étatiques, criminels sophistiqués) contre les analystes. Mode Safest, machines isolées, identités cloisonnées — les règles s'appliquent.

**Suivre l'actualité des grandes opérations**. Chaque Operation Cronos, Bayonet, Cookie Monster change la configuration de l'écosystème. Un analyste qui les suit anticipe les migrations d'acteurs.

---
