---
title: Chapitre 27 — Hacks DeFi et compromission de wallets
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie V — Typologies d’abus crypto
  - index.md
---

Les hacks DeFi et compromissions de wallets représentent des **milliards USD/an** depuis 2021 selon Chainalysis. Différent du ransomware (où victime paie volontairement) — ici, fonds sont **volés** sans consentement.

## 27.1 Hacks de protocoles DeFi

**Vecteurs typiques** :

**Vulnérabilités de smart contracts**. Bug dans le code (re-entrancy, overflow, logique faillible). Permet à attaquant de drainer le protocole.

**Compromission de clés admin**. Si un protocole DeFi a des fonctions admin (upgrade, pause, mint), compromission de la clé admin = takeover total.

**Oracles attaques**. Manipulation des oracles de prix utilisés par le protocole. Permet de profiter des conditions favorables artificielles.

**Flash loan attacks**. Combinaison de flash loans (prêts non-collatéralisés sur 1 transaction) avec exploitation de vulnérabilités. Permet à attaquant sans capital initial de drainer un protocole.

**Bridge exploits**. Bridges cross-chain sont particulièrement vulnérables (combinaison de smart contracts complexes et de validateurs externes). Cf Ronin (Ch.43), Wormhole (2022, 326 M USD), Nomad (2022, 190 M USD), Multichain (2023, 130 M USD).

**Cas marquants** :

- **Ronin Network** (mars 2022, 625 M USD) — Lazarus / DPRK.
- **Wormhole** (février 2022, 326 M USD) — restitution partielle suite à exploit reverse.
- **Nomad** (août 2022, 190 M USD) — exploitation chaotique multi-acteurs.
- **Mango Markets** (octobre 2022, 117 M USD) — Avraham Eisenberg, condamné aux US.
- **Curve Finance** (juillet 2023, 70 M USD).
- **Mixin Network** (septembre 2023, 200 M USD).
- **Multiple en 2024-2026** : pertes cumulées en milliards.

**Bilan annuel** : Chainalysis 2024 indique des fonds volés dans crypto en hausse, atteignant des chiffres records. Mid-year update 2025 confirme la tendance.

## 27.2 Compromission de wallets utilisateurs

**Vecteurs** :

**Stealer logs**. Malware (Lumma, RedLine, Vidar, etc.) qui vole credentials, cookies, seed phrases stockées localement. Cf cours Dark Web.

**Phishing de seed phrase**. Sites imitant wallet officiel demandant seed phrase « pour vérification ».

**Compromission email + reset MFA**. Reset password exchange / SMS swap / SIM swap.

**Approval phishing / drainers** (Ch.9). Site faux qui fait signer approval, drainer vide le wallet.

**Compromission physique**. Vol de hardware wallet, contraintes physiques. Plus rare.

**Bilan** : Chainalysis 2024-2025 souligne **augmentation forte** des fonds volés via compromission de wallets personnels. Particulièrement pour adresses high-value (whale wallets).

## 27.3 Reconnaître un hack vs vol vs scam

**Hack DeFi** :

- Exploit technique d’un protocole.
- Smart contract vidé.
- Souvent montant élevé (millions à centaines de millions USD).
- Communauté DeFi alertée immédiatement (twitter, dashboards).

**Compromission wallet individuel** :

- Wallet personnel vidé.
- Drainer ou transfert direct.
- Montants variables (quelques USD à millions USD).
- Souvent identifié par victime via alerte mouvement inattendu.

**Scam** (rug pull, fake token, etc.) :

- Investisseurs ont **volontairement** investi.
- Token déprécié à zéro après dump du créateur (rug pull).
- Différent du hack — pas de vulnérabilité exploitée techniquement, mais escroquerie sur l’intention.

L’enquête diffère selon catégorie.

## 27.4 Méthode d’enquête : hack DeFi

**Étape 1 — Détection / annonce**. Souvent annoncé immédiatement par victime ou observers (Twitter/X, Rekt News, Defi Watch).

**Étape 2 — Identification de la transaction d’exploit**. Le hash de la transaction où l’exploit s’est produit est public (sinon on cherche dans les transactions du protocole).

**Étape 3 — Lecture de la transaction**. Sur Etherscan / Phalcon / Tenderly :

- Comprendre la **logique exploit**.
- Identifier les **smart contracts** appelés.
- Identifier les **adresses attaquant**.

**Étape 4 — Suivi des fonds volés**. Méthode standard. Souvent les attaquants utilisent immédiatement Tornado Cash, bridges, ou d’autres techniques d’obfuscation.

**Étape 5 — Identification de l’attaquant**. Si trace publique (white hat hack annoncé), identification facile. Si exploit anonyme, attribution probable via patterns.

**Étape 6 — Coopération avec protocole victime et exchanges**. Souvent demande de gel à exchanges si fonds y atterrissent. Bounty du protocole pour incitation à restitution.

**Étape 7 — Rapport et action**.

## 27.5 Méthode d’enquête : compromission wallet

**Étape 1 — Indices initiaux**. La victime fournit son adresse, le timestamp du drainage, et idéalement des informations sur le vecteur (« j’ai cliqué sur ce lien… », « je crois que mon ordinateur a un virus… »).

**Étape 2 — Lecture des transactions de drainage**. Sur Etherscan, les **dernières transactions** du wallet de la victime montrent où sont allés les fonds.

**Étape 3 — Identification du drainer**. Si pattern approval phishing : voir les transactions d’`approve` précédentes. Identifier le smart contract du drainer.

**Étape 4 — Suivi des fonds drainés**. Le drainer consolide vers son propre wallet, qui ensuite blanchit.

**Étape 5 — Identification du drainer service**. Beaucoup de drainers sont **services-as-a-service** (Inferno Drainer, Pink Drainer historiquement, autres en 2024-2026). Identification du service permet attribution macro.

**Étape 6 — Coopération**. Si fonds vers exchange régulé : demande de gel.

## 27.6 Limites

**Récupération**. Variable. Hacks DeFi : parfois récupération via négociation (white hat reward) ou pression. Compromissions individuelles : récupération rare.

**Attribution**. Hacks sophistiqués (Lazarus) : attribution publique parfois. Drainers individuels : souvent anonymes.

**Vitesse**. Les hackers sont rapides. Les premières heures sont critiques. Si l’enquête ne démarre pas dans la journée, fonds souvent déjà out.

## 27.7 Tendances 2024-2026

**Hacks DeFi** : continuent à grand échelle. Bridges restent ciblés.

**Drainer-as-a-service** : démocratisation des drainers, baisse de la barrière technique.

**Lazarus** : continue à dominer les hacks majeurs. ~Mrd USD/an attribués.

**Compromission de wallets via stealer logs** : croissance massive.

**Retraits forcés via violence physique** : émergent (« 5 dollar wrench attacks », attaques contre des holders identifiés).

-----
