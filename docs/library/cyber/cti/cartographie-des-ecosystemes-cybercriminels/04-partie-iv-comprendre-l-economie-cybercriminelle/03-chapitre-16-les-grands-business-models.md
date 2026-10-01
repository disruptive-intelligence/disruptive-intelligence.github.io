---
title: Chapitre 16 — Les grands business models
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre l'économie cybercriminelle
  - index.md
---

## 16.1 Ransomware-as-a-Service (RaaS)

Le modèle dominant de la cybercriminalité en 2025-2026. L'opérateur développe le ransomware, maintient l'infrastructure (builder, panel C2, leak site, serveur de négociation, infrastructure de paiement crypto), recrute des affiliés, et capte une commission de 20 à 30 % de chaque rançon payée. L'affilié compromet les cibles, déploie le ransomware, et gère la négociation (parfois via un service de négociation externalisé).

**Produit vendu :** accès à la plateforme (builder, panel, leak site, support). **Clientèle :** affiliés de niveau technique variable. **Technicité requise :** modérée pour les affiliés (l'outil est fourni), élevée pour l'opérateur. **Monétisation :** commission sur les rançons payées. **Dépendances critiques :** infrastructure centralisée (panel, leak site), réputation de la marque (un opérateur dont les affiliés sont insatisfaits perd ses affiliés). **Points faibles :** l'opérateur est un point de défaillance unique, la marque est vulnérable à la disruption réputationnelle (Conti Leaks), les affiliés peuvent être retournés (coopération avec les forces de l'ordre).

## 16.2 Initial Access Brokerage (IAB)

Le marché des portes d'entrée. Les IAB vendent des accès compromis — credentials VPN, sessions RDP, webshells, accès domain admin, tokens de session — à des affiliés qui ne veulent pas ou ne savent pas mener la phase de compromission initiale.

**Gamme de prix (2025-2026) :** 500-2 000 $ pour un accès RDP basique d'une PME ; 3 000-15 000 $ pour un accès VPN d'une ETI avec élévation de privilèges ; 15 000-50 000 $+ pour un accès domain admin d'une grande entreprise ou d'une infrastructure critique. Les prix varient selon le pays, le secteur, le niveau d'accès, et le chiffre d'affaires estimé de la victime (les IAB font leur propre due diligence sur les cibles).

**Mode opératoire typique :** campagnes de phishing déployant des infostealers (Lumma, ACRStealer, StealC, Vidar — les quatre familles dominantes début 2026 selon AhnLab ASEC), exploitation de vulnérabilités exposées (VPN, pare-feux, RDP), ou achat de credentials sur les marchés de logs pour les enrichir en accès de niveau supérieur.

## 16.3 Infostealers et log markets

L'économie des identifiants volés est le carburant de l'écosystème ransomware. Les infostealers sont des malwares conçus pour collecter automatiquement les credentials de navigateur, les cookies de session, les données d'auto-remplissage, les informations de carte bancaire, et les données de wallets crypto des machines infectées.

**Lumma Stealer (LummaC2)** est l'infostealer dominant en 2025-2026 malgré la disruption de mai 2025 coordonnée par Microsoft et le DOJ. Vendu sous un modèle MaaS avec des tiers de prix allant de 250 $ (accès basique) à 20 000 $ (code source), il comptait environ 400 affiliés actifs fin 2024. L'opérateur, connu sous le pseudo « Shamel », a créé une véritable marque avec logo (un oiseau) et slogan. Après la saisie de 2 300 domaines en mai 2025, l'activité a repris en quelques semaines avec des tactiques de distribution plus discrètes. En début 2026, les quatre familles dominantes sont LummaC2, ACRStealer, StealC, et Vidar.

Les « logs » — les résultats de l'exfiltration — sont vendus sur des marchés spécialisés. Russian Market est le plus actif en 2025-2026. Genesis Market a été saisi en avril 2023 (Operation Cookie Monster) mais des successeurs ont émergé. Le prix d'un log varie de 1 à 50 $ selon la richesse des données (un log contenant un accès VPN d'entreprise vaut plus qu'un log contenant uniquement des credentials de réseaux sociaux personnels).

## 16.4 Phishing-as-a-Service et autres modèles

L'écosystème cybercriminel comprend de nombreux autres modèles économiques. Le **Phishing-as-a-Service (PhaaS)** fournit des kits de phishing pré-construits avec des pages de landing imitant des services légitimes, des panels de récupération de credentials, et parfois des capacités d'interception de MFA (Adversary-in-the-Middle). Le **DDoS-for-hire** (ou « booter/stresser ») offre des attaques par déni de service à la demande pour quelques dizaines de dollars. Les **botnets en location** fournissent un réseau de machines compromises utilisable pour la distribution de malware, le spam, ou le DDoS. La **fraude BEC** (Business Email Compromise) repose sur l'ingénierie sociale pure : compromission d'un compte email d'entreprise (ou usurpation d'identité), puis envoi de faux ordres de virement. Le **SIM swapping** permet de prendre le contrôle du numéro de téléphone d'une victime pour contourner l'authentification à deux facteurs. Le **carding** — l'utilisation frauduleuse de données de cartes bancaires — reste un marché actif mais en déclin relatif face au ransomware.

## 16.5 Fil rouge — NEXUS : le profil de l'IAB

> **🔍 NEXUS — Épisode 15**
>
> Samira approfondit le profil de ghost_access, l'IAB qui a vendu l'accès à Énergis. Sur le canal Telegram, ses 8 mois d'historique montrent 47 annonces de vente d'accès, toutes dans le secteur industriel européen (énergie, chimie, manufacture, transport). C'est un spécialiste sectoriel — pas un opportuniste qui vend tout ce qu'il trouve.
>
> La spécialisation sectorielle de ghost_access soulève une question : est-ce une stratégie commerciale (le secteur industriel paie bien et les affiliés RaaS apprécient ces cibles) ou une instruction (quelqu'un oriente ghost_access vers des cibles industrielles européennes pour des raisons non financières) ? Samira documente la question sans y répondre — les données sont insuffisantes. Mais elle note que cette spécialisation renforce légèrement H2 (instrumentalisation) sans exclure H1 (le secteur industriel est effectivement lucratif et les IAB se spécialisent souvent par secteur ou par géographie).

---
