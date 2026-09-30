---
title: Chapitre 7 — Cadre européen et international 2024-2026
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 7.1 Vue d'ensemble

Le cadre juridique européen et international de l'OSINT a évolué de manière substantielle entre 2024 et 2026. Quatre textes structurent désormais la pratique : le **Digital Services Act** (DSA), l'**AI Act**, la **Corporate Sustainability Due Diligence Directive** (CSDDD), et le renforcement des **sanctions internationales**. Côté UK, la **Failure to Prevent Fraud Offence** entre en vigueur en septembre 2025 et change la donne pour la diligence corporate.

## 7.2 Digital Services Act (DSA)

Le **DSA** (règlement UE 2022/2065, applicable depuis février 2024 pour les très grandes plateformes, août 2024 pour les autres) encadre les plateformes en ligne dans l'UE.

**Apports pour l'OSINT.**

- Obligations de transparence des plateformes (rapports de modération, registres publicitaires).
- Création d'archives publiques (DSA Transparency Database, X Community Notes).
- Désignation des **VLOPs** (Very Large Online Platforms) : Meta, X, TikTok, YouTube, etc., soumises aux obligations les plus strictes.
- Encadrement de la publicité ciblée, traçabilité.
- Possibilité de **dark patterns** restreinte.
- **Accès chercheurs** : les VLOPs doivent fournir un accès aux données aux chercheurs agréés (art. 40), avec des conditions strictes.

**Implication OSINT.** Les archives DSA fournissent une source nouvelle pour l'investigation des opérations d'influence (publicités politiques notamment) et de la modération. L'accès chercheur peut être mobilisé pour des projets académiques agréés.

## 7.3 AI Act (Règlement UE 2024/1689)

Entré en vigueur le **1er août 2024**, applicable progressivement entre 2025 et 2027. C'est le premier cadre réglementaire complet sur l'IA au monde.

**Architecture par risques.**

- **Risque inacceptable** (interdits) : social scoring, manipulation comportementale subliminale, identification biométrique en temps réel dans l'espace public (avec exceptions très encadrées).
- **Risque élevé** : usages en justice, RH, éducation, infrastructures critiques, biométrie. Obligations strictes (conformité, documentation, supervision humaine, robustesse).
- **Risque limité** : transparence (deepfakes étiquetés, chatbots identifiés).
- **Risque minimal** : libre.

**Apports pour l'OSINT.**

- **Identification de contenus IA** (art. 50) : les fournisseurs de modèles d'IA générative doivent permettre de marquer les contenus générés. Standard **C2PA** retenu de facto.
- **Encadrement de la reconnaissance faciale** : usage privé restreint. PimEyes et équivalents naviguent dans une zone grise.
- **Modèles à usage général** (GPAI) : transparence sur l'entraînement, droit d'auteur, sécurité.
- **Sanctions** : jusqu'à 7 % du chiffre d'affaires mondial pour les violations majeures.

**Implication OSINT.** L'AI Act renforce les obligations de transparence des contenus IA et donne un cadre aux outils de détection. Il restreint les usages les plus invasifs de la reconnaissance faciale par les acteurs privés. L'OSINT doit s'adapter : si vous utilisez des outils de reconnaissance faciale, vérifiez leur conformité AI Act.

## 7.4 Corporate Sustainability Due Diligence Directive (CSDDD)

La **CSDDD** (directive UE 2024/1760, entrée en vigueur le 25 juillet 2024, transposition nationale à venir) impose un **devoir de vigilance** aux grandes entreprises sur leur chaîne d'approvisionnement, en matière de droits humains et d'environnement.

**Périmètre.**

- Grandes entreprises UE (>1000 employés, >450 M€ CA mondial).
- Grandes entreprises hors UE actives dans l'UE (seuils similaires).

**Obligations.**

- Identification des risques humains et environnementaux dans la chaîne d'activité.
- Prévention et atténuation.
- Reporting et communication.
- Mesures de remédiation.

**Implication OSINT.** La CSDDD fait de l'OSINT un **outil opérationnel obligatoire** pour les directions juridiques, achats et conformité des grandes entreprises. Cartographie des fournisseurs, due diligence renforcée sur les sous-traitants, monitoring continu deviennent des cas d'usage massifs. Le marché de l'OSINT corporate explose en parallèle.

## 7.5 Sanctions internationales (OFAC, UE, UK, ONU)

Le régime de sanctions s'est considérablement renforcé depuis 2022 (invasion russe de l'Ukraine, sanctions Iran, Corée du Nord, Belarus).

**OFAC** (Office of Foreign Assets Control, US Treasury). Liste **SDN** (Specially Designated Nationals). Extraterritorialité forte (toute transaction touchant le dollar US ou impliquant une entité US peut tomber sous coupe OFAC). Sanctions secondaires : un acteur non-US qui transige avec une entité sanctionnée peut être lui-même sanctionné.

**UE**. Sanctions UE coordonnées via le SEAE. Listes consolidées publiées par la Commission. Effet direct dans tous les États membres.

**UK** post-Brexit. **OFSI** (Office of Financial Sanctions Implementation, HM Treasury). Liste consolidée UK.

**ONU**. Sanctions ONU obligatoires pour tous les États membres. Liste publique.

**Implication OSINT.** Le screening sanctions est devenu un cas d'usage massif. Outils : **OpenSanctions** (gratuit, multi-listes), WorldCheck (payant), Dow Jones Sanctions, Sayari, **Pappers** intègre une partie. La couverture doit être multi-listes et multi-juridictions.

## 7.6 Failure to Prevent Fraud Offence (UK)

L'**Economic Crime and Corporate Transparency Act 2023** crée une nouvelle infraction au Royaume-Uni : **failure to prevent fraud**, entrée en vigueur le 1er septembre 2025.

**Principe.** Une grande organisation est pénalement responsable si une personne associée (employé, agent, prestataire) commet une fraude pour son bénéfice, sauf si elle peut démontrer qu'elle avait mis en place des **« reasonable prevention procedures »**.

**Périmètre.**

- Organisations >250 employés OU >36 M£ CA OU >18 M£ actifs.
- Couvre fraudes diverses : false accounting, fraud by false representation, fraud by failing to disclose, etc.

**Implication OSINT.** Les entreprises UK et leurs partenaires investissent massivement dans la due diligence préventive. L'OSINT corporate, supply chain, et adverse media devient un outil de mise en conformité.

## 7.7 Régime américain (vue d'ensemble)

**Premier amendement** : protection forte de la liberté d'expression, plus permissif pour l'OSINT que le cadre européen.

**CCPA / CPRA** (Californie). Cadre privacy comparable au RGPD pour les résidents californiens, applicable aux entreprises traitant leurs données.

**State laws diverses** : Virginie, Colorado, Connecticut, Utah, Texas — patchwork de législations état par état.

**Federal**. Pas de loi privacy fédérale équivalente RGPD. **HIPAA** pour la santé, **GLBA** pour le financier, **COPPA** pour les enfants.

**FCRA** (Fair Credit Reporting Act). Encadre les rapports d'enquête commerciaux. Applicable à certaines pratiques OSINT corporate.

**FOIA** (Freedom of Information Act). Levier OSINT majeur côté US : demandes d'accès à l'information publique des agences fédérales.

## 7.8 Régime UK post-Brexit

**UK GDPR** (Data Protection Act 2018 + UK GDPR). Très proche du RGPD européen, avec quelques divergences mineures.

**RIPA** (Regulation of Investigatory Powers Act). Encadre la surveillance.

**ICO** (Information Commissioner's Office). Autorité de contrôle.

**Failure to Prevent Fraud** (supra).

## 7.9 Pays sensibles et juridictions à risque

Certaines juridictions présentent des risques particuliers pour l'OSINT.

**Chine, Russie, Iran, Corée du Nord.** Cadre juridique restrictif. Sanctions occidentales. Investigation depuis l'extérieur reste possible mais sur place quasiment impossible.

**Allemagne.** Forte protection vie privée, jurisprudence stricte sur la photographie de personnes, BDSG. Plus exigeant que le standard RGPD européen sur certains points.

**Suisse**. Hors UE mais cadre privacy équivalent (LPD révisée 2023). Régime spécifique pour les données financières (secret bancaire allégé mais existant).

**Émirats, Singapour, autres hubs financiers.** Régulations en construction, parfois moins strictes que l'UE.

## 7.10 MiCA et Travel Rule (cadre crypto)

Le règlement **MiCA** (Markets in Crypto-Assets, applicable progressivement depuis 2024) impose un cadre prudentiel aux **VASPs** (Virtual Asset Service Providers) dans l'UE. Implications OSINT : meilleure visibilité des exchanges régulés, durcissement KYC, traçabilité accrue.

La **Travel Rule** (FATF Recommendation 16, transposée en UE) impose que les VASPs échangent des informations sur l'émetteur et le destinataire pour les transferts crypto au-dessus de certains seuils. Implications OSINT : exchanges régulés disposent de plus d'informations sur leurs utilisateurs, ce qui peut être mobilisé en réquisition judiciaire.

*(Pour le détail, renvoi vers le cours OSINT Crypto vFULL.)*

## 7.11 Synthèse — boussole juridique 2026

| Texte | Juridiction | Applicable | Implication OSINT principale |
|---|---|---|---|
| RGPD | UE | 2018 | Cadre principal collecte données personnelles |
| DSA | UE | 2024 | Transparence plateformes, accès chercheurs |
| AI Act | UE | 2024-2027 | Encadrement IA, marquage contenus, restriction reconnaissance faciale |
| CSDDD | UE | 2024+ | Due diligence supply chain obligatoire |
| MiCA | UE | 2024 | Cadre VASPs crypto |
| CCPA/CPRA | Californie | 2020+ | Privacy résidents Californie |
| Failure to Prevent Fraud | UK | 09/2025 | Due diligence préventive obligatoire |
| Sanctions OFAC | US extraterritorial | Continu | Screening multi-juridictions |
| FOIA | US | 1966 | Levier d'accès information publique |

L'analyste OSINT travaillant à l'échelle internationale doit maîtriser ces régimes croisés. En cas de doute juridique, consultation avocat spécialisé n'est pas optionnelle.

-----
