---
title: Chapitre 5 — Le métier d’analyste crypto-forensique
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie I — Comprendre L’écosystème crypto SANS fantasme
  - index.md
---

Avant les techniques, la **posture professionnelle**. Ce chapitre couvre les compétences, l’OPSEC, l’éthique, et l’organisation du métier.

## 5.1 Le profil d’analyste crypto-forensique

**Compétences techniques** :

- Lecture fluide des blockchains majeures (Bitcoin, Ethereum, TRON minimum).
- Maîtrise des explorateurs publics (Mempool, Etherscan, Tronscan).
- Maîtrise d’au moins un outil professionnel (Chainalysis, TRM, ou Elliptic) si budget disponible.
- Capacité à lire et interpréter du code de smart contract basique (Solidity).
- Compréhension des techniques d’obfuscation (mixers, bridges, swaps).
- Fluence avec un environnement Python pour scripts d’analyse personnalisés.

**Compétences analytiques** :

- Méthodologie d’enquête structurée.
- Vocabulaire calibré (WEP).
- Capacité de discernement (distinguer observation, inférence, attribution).
- Discipline anti-biais.
- Rédaction analytique claire.

**Compétences transverses** :

- Curiosité (l’écosystème évolue, il faut suivre).
- Rigueur (la documentation conditionne la valeur du travail).
- Patience (les enquêtes prennent semaines/mois).
- Communication (rapports adaptés à des audiences variées).
- Éthique (résistance aux dérives, alignement avec mandat).

**Background typique** :

- Parcours **finance/AML** reconverti vers crypto (ex-banquier, ex-analyste TRACFIN, ex-compliance officer).
- Parcours **technique/cyber** étendu vers crypto (ex-SOC, ex-pentester, ex-CTI).
- Parcours **académique** (master Finance, master Cybersécurité, parfois doctorat en cryptographie).
- Parcours **enquêteur** (gendarmerie/police, services de renseignement) reconverti.

Sarah Marin, dans MIXSHADOW, illustre le profil hybride : 3 ans TRACFIN (analyste financière) puis 3 ans Athéna (crypto-forensique pure). Combinaison appréciée.

## 5.2 OPSEC de l’analyste crypto

L’analyste crypto manipule des données sensibles : adresses de criminels actifs, flux en cours, méthodologies. Plusieurs principes OPSEC.

**Séparation des univers**. Ne pas mélanger comptes personnels et infrastructure d’investigation. Une machine dédiée pour les analyses sensibles (comme pour Dark Web — voir cours associé).

**Wallet d’investigation séparé**. Si l’enquête nécessite des transactions de test (rare en OSINT pur, plus fréquent en undercover), wallet dédié, financé par circuit professionnel, jamais lié à l’identité personnelle de l’analyste.

**Pas d’interaction directe avec les wallets cibles**. L’analyste OSINT **observe**, il ne **transacte pas** avec les wallets criminels. Envoyer même 1 satoshi vers un wallet ransomware peut alerter l’opérateur et compromettre l’investigation. C’est aussi potentiellement illégal (financement de groupe sanctionné selon l’acteur).

**Pas de phishing aux acteurs**. Tentation parfois : « contacter le scammer en feignant être une victime ». Cela dépasse souvent le cadre OSINT et peut tomber dans l’enquête sous couverture, réservée aux autorités.

**Documentation immédiate**. Toute observation est captée, horodatée, hachée. Pas de mémoire orale. Voir Ch.23.

**Pas de rediffusion incontrôlée**. Les observations ne sont partagées qu’au cercle justifié (mandant, autorités, ISAC selon TLP). Pas de bavardage entre analystes ou avec journalistes.

**Confidentialité du mandat client**. Sauf accord explicite, l’identité du mandant et la nature exacte de l’enquête restent confidentielles, y compris vis-à-vis de l’écosystème pro.

## 5.3 Cadre éthique

**Principes** :

**Légalité scrupuleuse**. L’OSINT crypto opère dans un cadre légal — RGPD, sanctions, AML, secret professionnel. L’analyste connaît le cadre applicable à son périmètre.

**Mandat respecté**. L’enquête se déroule selon le mandat. Pas d’extension non autorisée vers d’autres cibles, pas de curiosité incontrôlée.

**Minimisation**. Collecter ce qui est nécessaire. Ne pas extraire systématiquement toutes les données accessibles « au cas où ».

**Non-prolifération**. Les données collectées ne fuitent pas hors du cercle justifié.

**Calibration honnête**. Ne pas embellir les conclusions. Ne pas masquer les limites.

**Respect des victimes**. Beaucoup d’enquêtes impliquent des victimes (pig butchering, ransomware). Leurs données et leur dignité sont respectées.

**Coopération avec autorités**. Si l’enquête révèle des infractions graves, signalement obligatoire (article 40 CPP pour fonctionnaires, signalement TRACFIN pour assujettis).

**Refus des dérives**. L’analyste résiste aux pressions pour produire des rapports orientés (« attribuer cet acteur à tel groupe pour des raisons politiques »).

## 5.4 Outils, certifications, formation

**Certifications utiles** :

- **Chainalysis Certified Reactor (CRC)** : référence industrie, formation officielle Chainalysis.
- **TRM Labs Certified Investigator (CTI)** : certification TRM Labs.
- **Certified Cryptocurrency Investigator (CCI)** : certification de la blockchain forensics community.
- **CAMS (Certified Anti-Money Laundering Specialist)** : certification AML transverse, utile pour le contexte.

**Formations courtes** :

- **Bellingcat OSINT trainings** (volet crypto inclus).
- **SANS FOR578 / FOR589** (CTI / cybercrime intelligence, modules crypto).
- **Webinars vendors** (Chainalysis, TRM, Elliptic — gratuits ou peu coûteux).

**Auto-formation** :

- Lecture des rapports annuels Chainalysis Crypto Crime, TRM Labs reports, Elliptic publications.
- Suivre Twitter/X de chercheurs publics : @zachxbt, @mishasolovyov (Solovyov), @pcaversaccio (smart contract security), @0x_lasagna, @samczsun (security DeFi), @tayvano_ (Tay).
- Outils de pratique : explorateurs publics gratuits, analyse de cas historiques publiés.
- Communautés : OnChain Investigators, OSINT Curious, SEAL ISAC.

**Veille à entretenir** :

- Rapports Chainalysis (annuels + mid-year updates).
- TRM Labs blog et threat reports.
- Elliptic publications.
- Rapports FATF (Virtual Assets, Targeted Financial Sanctions, etc.).
- Bulletins OFAC SDN.
- Travaux ZachXBT (chercheur indépendant prolifique).
- Blogs communautaires (Defillama, DeFiLlama Adapter, Rekt News pour les hacks).

## 5.5 L’organisation du travail

**Outillage informatique** :

- Machine principale propre (Linux ou macOS, Windows acceptable).
- VM dédiée pour analyses sensibles (Whonix ou équivalent si interaction Tor).
- Espace de stockage dédié et sauvegardé pour les preuves.
- Outils de capture (Hunchly ou équivalent).
- Outils blockchain (cf Partie IV).

**Workflow type** :

- Réception du mandat / alerte.
- Cadrage et planification.
- Investigation structurée (Partie III).
- Documentation continue.
- Rédaction du rapport (Ch.46).
- Présentation et coopération.
- Clôture et archivage.

**Gestion des dossiers** :

- Un dossier = un répertoire structuré (notes, captures, exports, rapport final).
- Versioning (Git ou équivalent pour rapports).
- Archivage immutable post-clôture.

**Travail en équipe** :

- Pour les grandes investigations, plusieurs analystes (un lead, des contributeurs).
- Partage via plateforme sécurisée (Mattermost, Element/Matrix self-hosted, etc.).
- Peer review systématique des rapports.

## 5.6 Carrière et évolution

**Trajectoires possibles** :

- **Cabinet de conseil / forensique** : Athéna (fictif), Wavestone, Mandiant, Kroll, etc.
- **Vendor blockchain intelligence** : Chainalysis, TRM Labs, Elliptic recrutent.
- **Forces de l’ordre** : SDLC, OFAC français, gendarmerie nationale (cellule cyber), magistrature spécialisée.
- **TRACFIN, ANSSI, DGSI**.
- **Compliance d’exchange ou banque** : équipes AML internes des VASP régulés.
- **Renseignement** : DGSE, services partenaires.
- **Indépendant** : ZachXBT comme modèle (mais rare).

**Évolution des compétences** :

- Junior (0-2 ans) : maîtrise technique, lecture, outils.
- Senior (3-7 ans) : pilotage d’enquêtes complètes, mentoring, livrables.
- Lead (7+ ans) : direction d’équipe, méthodologie, contribution doctrinale.

**Rémunération** (indicatif France 2025-2026) : junior 45-55 k€, senior 65-90 k€, lead 100-150 k€+. Plus élevé chez vendors (Chainalysis, TRM) et en finance (banques d’investissement, hedge funds).

## 5.7 Fil rouge — MIXSHADOW : préparation de l’analyste

> **🔗 MIXSHADOW — Épisode 2 : setup**
> 
> Sarah prépare son environnement. Protocole Athéna pour MIXSHADOW :
> 
> - **Machine dédiée** : laptop sécurisé, OS Ubuntu LTS hardened, accès limité au sous-réseau d’investigation.
> - **Outils blockchain** : Chainalysis Reactor (licence Athéna), TRM Labs Investigations (validation croisée), Etherscan/Tronscan/Mempool en accès direct, scripts Python pour exports CSV.
> - **Espace de travail** : dossier MIXSHADOW chiffré, accès restreint à l’équipe (Sarah + 1 analyste junior + revue par directeur Athéna), backup quotidien sur stockage immutable.
> - **Documentation** : Hunchly pour captures de pages d’explorateur, journal d’enquête en Markdown, exports CSV horodatés et hashés.
> - **Pas de wallets de test** : MIXSHADOW est OSINT pur, pas d’interaction transactionnelle.
> - **Communication** : Element/Matrix interne Athéna pour discussions équipe, email chiffré avec DGSI, audio sécurisé pour les briefings.
> 
> Avant de démarrer le traçage proprement dit, Sarah complète le **dossier de cadrage** : périmètre, objectifs, livrables attendus, contacts, échéances. Validation directeur Athéna et DGSI. Le cadrage prend 4 heures — temps bien investi.
> 
> Action immédiate : récupérer l’**adresse Bitcoin** où les 35 BTC ont été versés. Le RSSI Aurélien Médical fournit la clé : adresse de paiement BTC fournie par Akira via portail Tor, montant exact 35,00000000 BTC, TXID de la transaction de paiement, timestamp 14 mars 09:12 UTC.
> 
> Sarah valide le TXID sur Mempool.space. Le paiement est bien enregistré, 6 confirmations atteintes. Adresse réceptrice : `bc1q...[adresse fictive de 42 caractères]`. Premier nœud du graphe MIXSHADOW.
> 
> Ch.6 va détailler comment lire cette transaction Bitcoin en profondeur. Ch.13 reprendra MIXSHADOW pour l’investigation proprement dite.

-----
