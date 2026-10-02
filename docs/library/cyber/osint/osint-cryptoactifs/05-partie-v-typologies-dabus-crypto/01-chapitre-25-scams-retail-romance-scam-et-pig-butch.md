---
title: 'Chapitre 25 — Scams retail : romance scam et pig butchering'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie V — Typologies d’abus crypto
  - index.md
---

Le **pig butchering** (« 杀猪盘 », *shā zhū pán* — « élevage du cochon avant l’abattage ») est devenu en 2022-2026 l’un des plus gros postes de pertes financières liées au crypto, avec des estimations Chainalysis cumulées en milliards USD/an. Il combine manipulation sentimentale et faux investissement, ciblant des victimes individuelles sur des durées de plusieurs mois.

## 25.1 Le modus operandi

**Phase 1 — Approche**. La victime est contactée :

- Via réseaux sociaux (Instagram, LinkedIn, Facebook).
- Via applications de rencontre (Tinder, Bumble, Hinge).
- Via WhatsApp ou Telegram (« mauvais numéro » prétendu).
- Via groupes d’investissement crypto Telegram / Discord.

L’approche est **généralement chaleureuse**, sans demande financière initiale. Construction d’une relation (amicale, sentimentale, professionnelle).

**Phase 2 — Construction de la confiance**. Sur plusieurs semaines/mois :

- Communications quotidiennes.
- Partage de détails « personnels » (vie, famille, succès).
- Création d’intimité.
- Mention progressive du « succès en investissement crypto ».
- Photos volées d’autres personnes (réelles ou IA-générées).

**Phase 3 — Introduction de l’investissement**. Le scammer mentionne :

- Une « plateforme exclusive » avec « gains garantis ».
- Un « mentor » ou « insider tip ».
- Des « gains incroyables » que le scammer prétend avoir réalisés (captures truquées montrant son « portefeuille »).

**Phase 4 — Premier dépôt et premier retrait**. La victime dépose une **petite somme** (500-5000 USD) sur la plateforme frauduleuse. Le scammer **autorise un petit retrait** initial pour crédibiliser. La victime voit ses fonds revenir, gagne confiance.

**Phase 5 — Escalade**. Encouragée par le « succès initial », la victime augmente progressivement :

- Investissements plus gros.
- Prises de prêts pour investir plus.
- Liquidation d’épargne.
- Demande aux proches.

**Phase 6 — Le « chômage » du retrait**. Quand la victime tente de retirer une somme significative :

- « Frais d’audit fiscal » à payer.
- « Caution de sécurité » exigée.
- « Vérification d’identité supplémentaire » qui débloque un retrait moyennant nouveau paiement.
- Cycle : chaque demande de retrait génère une nouvelle demande de paiement.

**Phase 7 — Disparition**. Quand la victime réalise (ou n’a plus rien à donner), le scammer disparaît. Compte coupé, profil supprimé, plateforme inaccessible.

**Bilans typiques** : pertes individuelles de 50 k à 1 M USD+. Cas documentés dépassant 5 M USD pour victimes uniques.

## 25.2 Le réseau opérateur

**Pig butchering n’est PAS un scam individuel**. C’est une **industrie**.

**Structure typique** :

- **Scam compounds** localisés en Asie du Sud-Est (Cambodge, Laos, Myanmar, Philippines). Bâtiments où des centaines à milliers de **« scammeurs »** (parfois eux-mêmes victimes de trafic humain) opèrent sous coercion.
- **Opérateurs / patrons** : organisations criminelles (souvent liées à des syndicats chinois) qui gèrent les compounds.
- **Réseau de blanchiment** : flux USDT-TRON consolidant les paiements des victimes.
- **Infrastructure** : plateformes web crédibles, sites de phishing, canaux Telegram/WhatsApp.

**Cooperation avec le crime organisé**. ZachXBT, OFAC et plusieurs reports (Chainalysis, TRM, Elliptic) documentent depuis 2022-2024 le rôle de syndicats criminels asiatiques dans le pig butchering. Sanctions contre certains compounds documentées.

**Pour la victime** : dans la grande majorité des cas, le « scammeur » qui lui parle quotidiennement n’est **pas le décideur** — c’est un opérateur de bas niveau sous pression (parfois traffiqué). La structure derrière est ce qui prélève les fonds et organise le blanchiment.

## 25.3 Les flux crypto typiques

**Pattern observable on-chain** :

**Étape 1 — Réception sur adresse de collecte**. La plateforme frauduleuse demande à la victime d’envoyer USDT-TRON (le plus fréquent, ou parfois USDT-Ethereum, plus rarement BTC) vers une adresse spécifique.

**Étape 2 — Adresses de collecte multi-victimes**. Sur Tronscan, on observe l’**adresse de collecte** recevant des USDT depuis plusieurs adresses de victimes différentes. Un cluster typique :

- Adresse de collecte centrale.
- 10-100 adresses de victimes envoyant.
- Montants variables (de 500 à 100 000+ USD chacun).
- Période étalée sur semaines/mois.

**Étape 3 — Consolidation rapide**. L’adresse de collecte transfère rapidement les fonds vers une adresse hub.

**Étape 4 — Layering**. Le hub fait du peeling chain TRON-style ou disperse vers multiples sub-adresses.

**Étape 5 — Off-ramp**. Les fonds finissent vers :

- Exchanges régionaux moins regardants (souvent Asie).
- P2P / OTC.
- Conversion en autres cryptos (BTC, monero, autres).
- Cartes prepaid crypto.

## 25.4 Reconnaître un cluster pig butchering

**Signaux** :

**Adresse de collecte centrale** recevant de **multiples sources** (>5-10 victimes différentes).

**Montants variables** (pas tous identiques) — caractéristique de victimes individuelles vs scam d’identité de masse.

**Pattern temporel étalé** sur des semaines/mois (vs scam ponctuel).

**Consolidation rapide** vers hub après réception.

**Flux vers exchanges régionaux** ou P2P en finale.

**Activité concentrée** sur USDT-TRON.

**Fraîcheur** : les adresses de collecte sont souvent fraîches (créées peu avant l’opération), réutilisées sur quelques semaines, puis abandonnées au profit de nouvelles.

## 25.5 Méthode d’enquête

**Étape 1 — Indice initial**. Souvent : adresse fournie par victime + screenshots conversation + détails plateforme frauduleuse.

**Étape 2 — Validation**. TXID confirmant le dépôt. Lecture sur Tronscan.

**Étape 3 — Expansion vers cluster**. Identifier l’**adresse de collecte** (premier destinataire). Lire son historique : combien d’autres dépôts a-t-elle reçu ? Volume cumulé ? Patterns ?

**Étape 4 — Identification d’autres victimes**. Les autres adresses ayant déposé sur la même collecte sont **probablement d’autres victimes**. Si la victime principale fait plainte, ces co-victimes peuvent être identifiées (et alerter les autorités si plaintes coordonnées).

**Étape 5 — Suivi des flux post-collecte**. Le hub redistribue vers où ? Identification des chemins de blanchiment.

**Étape 6 — Off-ramps**. Identification des exchanges utilisés en finale. Si exchange régulé : possibilité de réquisition KYC.

**Étape 7 — Rapport et action**.

## 25.6 Limites de l’enquête pig butchering

**Récupération rare**. Les fonds sont souvent dispersés rapidement. Le délai entre dépôt victime et cashout est court (jours/semaines). Au moment où la victime réalise et porte plainte, fonds sont souvent déjà out.

**Identification du « scammeur » individuel** : très difficile. C’est rarement un acteur identifiable (compounds Asie du Sud-Est).

**Identification des opérateurs** : possible via patterns à grande échelle, mais judiciairement complexe (juridictions, coopération internationale variable).

**Effet psychologique sur victime**. La victime est souvent **doublement traumatisée** : perte financière + manipulation sentimentale révélée. Approche humaine importante.

**Réponse défensive sectorielle** : sensibilisation grand public, alertes plateformes, partenariats avec banques pour détecter virements suspects.

## 25.7 Coordination

**Signalement aux autorités** :

- **Cybermalveillance.gouv.fr** (France) : pour victimes individuelles.
- **TRACFIN** : pour banque détectant flux suspect.
- **Plainte police / gendarmerie** locale.
- **FBI IC3** (US) si concerné.

**Coopération internationale** :

- **Operation Shamrock** (US, depuis 2024) : coordination LEA contre pig butchering.
- **GLACY+ Council of Europe** : capacity building anti-cybercrime.
- **Europol EC3** : coordination EU.

**Sanctions** : OFAC a sanctionné certains compounds et opérateurs depuis 2024. Suivre les listes pour adresses sanctionnées.

## 25.8 Cas typiques

**Romance scam pure** : intimité construite, demande de fonds pour « urgence familiale » ou « problème médical ». Moins de prétention investissement, plus d’émotionnel.

**Faux investissement plateformes**. Plateforme prétendant être trading bot, AI investment, DeFi proprietary. Captures truquées de gains.

**Faux investissement « insider »**. Le scammer prétend avoir un « tip » d’initié sur une crypto qui va exploser. Transfert vers « sa » plateforme.

**Faux investissement pyramidal**. Combinaison schéma de Ponzi et scam — les premiers déposants peuvent retirer (avec fonds des suivants) jusqu’à effondrement.

**Job scam**. Variation : la victime est « recrutée » pour faire du « trading test », doit déposer pour qualifier, puis bloquée.

## 25.9 Tendances 2024-2026

**Augmentation explosive** depuis 2022.

**IA dans le scam** :

- Génération d’images de profil par IA (StyleGAN, Stable Diffusion, etc.).
- Voice cloning pour appels téléphoniques crédibles.
- Chatbots IA pour gérer multiples victimes simultanément.
- Multi-langue automatique pour cibler globalement.

**Blanchiment via stablecoins** dominant.

**Sophistication accrue** des plateformes frauduleuses (UI proche d’exchanges légitimes).

**Pour l’enquêteur** : la **typologie évolue**. Les patterns 2026 incluent IA et stablecoins multi-chaînes. La méthodologie de base reste mais s’adapte.

-----
