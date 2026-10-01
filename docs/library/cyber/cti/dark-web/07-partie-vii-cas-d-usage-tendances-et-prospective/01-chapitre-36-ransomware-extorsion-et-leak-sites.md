---
title: Chapitre 36 — Ransomware, extorsion et leak sites
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VII — Cas d'usage, tendances et prospective
  - index.md
---

Le ransomware est le phénomène cyber le plus structurant des années 2020. Ce chapitre complète les Ch.11-12 (leak sites) avec une vision d'ensemble du phénomène, ses évolutions, ses impacts.

## 36.1 L'évolution du modèle ransomware

**Génération 1 (2013-2018) — Ransomware de masse**. CryptoLocker (2013), Locky (2016), WannaCry (2017 — DPRK). Distribution massive non-ciblée, rançons faibles (300-5 000 USD typiquement), chiffrement local. Modèle : volume × petit paiement.

**Génération 2 (2019-2021) — Big game hunting**. Ryuk, Sodinokibi/REvil, Conti. Ciblage d'organisations spécifiques, reconnaissance approfondie avant déploiement, rançons 100 k - 10 M USD. Modèle : ciblage × gros paiements.

**Génération 3 (2020-présent) — Double extorsion**. Maze a popularisé le modèle : exfiltration **avant** chiffrement, leak site pour pressure, publication si non-paiement. Aujourd'hui standard pour tout ransomware sérieux.

**Génération 4 (2023-présent) — Multi-extorsion**. Au-delà du chiffrement + publication, pressions additionnelles :

- **Chantage direct des clients** de la victime (DarkSide historique, d'autres).
- **Chantage des partenaires et fournisseurs**.
- **DDoS** contre les services de la victime pendant la négociation.
- **Harcèlement téléphonique** des dirigeants.
- **Notification aux régulateurs** (mention explicite de SEC, CNIL, etc.) comme menace.
- **Publication auprès journalistes** pour maximiser impact médiatique.

**Génération 5 (émergente) — Extorsion pure, sans chiffrement**. BianLian depuis 2023 a abandonné le chiffrement et se concentre sur exfiltration + extorsion. Raisons : restauration depuis backups annule le levier de chiffrement, le chiffrement déclenche alertes défensives. L'exfiltration + chantage peut être plus subtile et plus efficace.

## 36.2 Les modèles économiques ransomware contemporains

**RaaS (Ransomware-as-a-Service)**. Dominant. Opérateur fournit malware + infrastructure (leak site, portail négociation), affiliés déploient. Partage typique 70-80% affilié, 20-30% opérateur.

**Affiliés indépendants**. Un opérateur ransomware avec équipe interne (pas d'affiliés externes). Moins scalable mais contrôle qualité supérieur. Certains groupes matures opèrent ainsi (Cl0p partiellement).

**Opérateurs franchisés**. Variant RaaS avec contractual obligations plus strictes (territoires, cibles, comportements).

**Cartels** : coordination entre plusieurs groupes, partage d'infrastructure, coordination d'affiliés. Émergent 2023-2025.

## 36.3 Les grands groupes 2024-2026

**LockBit** — leader historique, affecté par Operation Cronos (février 2024). Infrastructure saisie, Dmitry Khoroshev (LockBitSupp) identifié et sanctionné. Relaunch tenté, crédibilité entamée. Estimation historique : 500 M+ USD cumulé avant disruption.

**ALPHV / BlackCat** — second historique, disparition mars 2024 après suspicion d'exit scam post-paiement Change Healthcare (~22 M USD disparu avec opérateur).

**Cl0p** — modus operandi spécifique : exploitation de vulnérabilités d'edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Campagnes massives par vagues, moins continu que LockBit historique.

**Black Basta** — actif 2022-2025, ciblage enterprise large, rançons élevées. Source probable de plusieurs incidents majeurs.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié, rythme soutenu.

**Akira** — émergent fin 2023, croissance rapide. Ciblage diversifié.

**RansomHub** — émergent mi-2024, semble absorber affiliés ALPHV post-disparition. En forte croissance 2024-2025.

**Qilin** — actif, ciblage notable (Synnovis/NHS juin 2024).

**Groupes émergents** : 8Base, Hunters International, Dragonforce, Medusa, Inc Ransom — à surveiller.

## 36.4 Ampleur et tendances macro

**Rapports Coveware** (trimestriels) donnent les tendances transversales :

- **Paiement moyen** en hausse tendancielle : de ~500 k USD en 2021 à ~2-3 M USD en 2024-2025 sur grandes victimes.
- **Taux de paiement** en baisse : de ~70% en 2018-2019 à ~25-30% en 2024. Moins de victimes paient, mais celles qui paient paient plus.
- **Time to recovery** : moyennes de 20-25 jours pour reprise opérationnelle partielle, plusieurs mois pour reprise complète.
- **Victimes par secteur** : healthcare, manufacturing, finance en tête. Secteur public croissant.
- **Géographie** : US majoritaire, mais EU en forte croissance.

**Rapports Chainalysis** sur crypto flux ransomware :

- **2024** : record ~1,1 Mrd USD (en paiements identifiés), malgré ou à cause de Cronos/ALPHV disappearance.
- Flux vers exchanges dans juridictions permissives, mixers, Monero swaps.

## 36.5 Les leak sites comme théâtre médiatique

Les leak sites ne sont pas que des outils de coercition — ils sont aussi **des théâtres médiatiques** pour les groupes.

**Construction de réputation**. Un groupe avec leak site flashy, design soigné, countdown dramatique construit sa réputation. Attire affiliés, impressionne futurs victimes, domine la presse.

**Concurrence entre groupes**. Leak sites montrent les trophées — cibles prestigieuses compromises. Les groupes se comparent, se défient, se vantent.

**Communication aux victimes**. Message implicite : « regardez ce qu'on peut faire, payez ou voyez votre nom ici ».

**Communication à la communauté cybercriminelle**. Recruter affiliés (top des ransom payout), attirer autres acteurs.

**Communication aux médias**. Certains groupes soignent leur relation presse — portails avec section « media contact », press kits, mises à jour régulières. Stratégies de RP criminelles.

**Narratifs politiques**. Certains groupes se drapent dans des narratifs (« on cible les corrompus », « on cible les gouvernements oppresseurs »), soit sincèrement, soit comme cover. REvil historique jouait sur cette corde ; certains groupes actuels aussi.

Pour l'analyste, le **ton** du leak site informe sur l'acteur. Ton brutal + minimaliste = groupe pragmatique. Ton élaboré + narratif = groupe attentif à l'image. Ton politique = potentiel de hybridation avec hacktivisme.

## 36.6 Les négociations

Une fois une victime compromise et revendiquée, les **négociations** commencent. Écosystème professionnalisé.

**Portails dédiés**. Chaque groupe maintient un portail de négociation (généralement sur .onion), avec chat, possibilité d'envoyer preuves d'exfiltration, compteur de rançon.

**Négociateurs**. Côté criminel, personnel dédié à la négociation. Souvent anglophones (ou utilisant traduction), patients, adoptant un ton « business ». Certains sont formés.

**Négociateurs côté victime**. Profession émergente. Cabinets spécialisés (Coveware, Kroll, GroupSense) maîtrisent les négociations avec groupes connus, connaissent patterns de discount, processus de paiement.

**Patterns de négociation** :

- **Demande initiale** souvent exagérée (facteur 3-5× de ce qui sera accepté).
- **Réduction par négociation** : 40-70% de discount réaliste avec négociateur professionnel.
- **Preuve de déchiffrement** (decryption test) avant paiement.
- **Preuve de destruction des données** exfiltrées (rarement vérifiable).
- **Délais** : 7-14 jours typiquement, extensible.

**Payer ou pas** : débat structurant, Ch.12. Tendance baisse du paiement.

**Sanctions OFAC** : certains groupes sanctionnés. Payer un groupe sanctionné expose à sanctions pour le payeur. Négociateurs doivent vérifier avant de faciliter paiement.

## 36.7 L'impact des disruptions policières

**Operation Cronos contre LockBit (février 2024)**. Coordination NCA, FBI, Europol, 10+ pays. Saisie infrastructure, publication de clés de déchiffrement (permettant restauration gratuite pour certaines victimes), identification et sanction Khoroshev, leak de communications internes.

**Impact** : LockBit a tenté un relaunch mais avec crédibilité sérieusement entamée. Affiliés ont migré vers concurrents (Black Basta, Akira, RansomHub notamment).

**Ransom payments** ont connu une baisse mi-2024 liée à Cronos et disparition ALPHV, mais sont remontés rapidement — l'écosystème a absorbé les chocs.

**Enseignements** :

- Les disruptions ont un impact **temporaire** sur l'écosystème, pas définitif.
- Les affiliés sont **agnostiques** — ils migrent là où les conditions sont les meilleures.
- La **résilience structurelle** du ransomware est élevée — business model rentable, acteurs nombreux, juridictions permissives disponibles.
- Les **disruptions répétées** peuvent cependant augmenter les coûts opérationnels et réduire la confiance des affiliés — stratégie de long terme vs coup unique.

## 36.8 Les contre-mesures défensives émergentes

**Cyber-insurance**. A évolué — certaines polices excluent désormais les paiements à groupes sanctionnés, imposent due diligence pré-paiement, requirement de contrôles défensifs (MFA, EDR, backups testés) pour couverture.

**Plans de continuité** éprouvés par exercices (tabletop, simulations). Objectif : récupérer **sans paiement**.

**Backups offline testés**. Le backup qui n'a jamais été testé ne marche pas. Test régulier de restauration partielle et complète.

**Zero Trust**. Limite la propagation latérale. Segmentation, least privilege, MFA partout.

**EDR/XDR et détection comportementale**. Détecter le ransomware **avant le chiffrement** — indicateurs d'exfiltration, modifications massives de fichiers, connexions C2.

**Threat hunting proactif** sur TTP ransomware connus.

**Coopération sectorielle** via ISAC pour partage rapide d'IoC.

**No-ransom coalitions** : initiatives (Counter Ransomware Initiative CRI, dirigée par US depuis 2021, 50+ pays membres) qui coordonnent la lutte, facilitent partage d'intel, découragent paiements.

---
