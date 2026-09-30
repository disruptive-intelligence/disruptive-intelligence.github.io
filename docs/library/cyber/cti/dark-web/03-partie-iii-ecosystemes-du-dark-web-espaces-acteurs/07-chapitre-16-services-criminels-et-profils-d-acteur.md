---
title: Chapitre 16 — Services criminels et profils d'acteurs
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

Au-delà des produits (données, credentials), le dark web est un marché de **services** — crime-as-a-service sous toutes ses formes. Ce chapitre cartographie les services majeurs et les profils d'acteurs.

## 16.1 Les services majeurs

**Ransomware-as-a-Service (RaaS)**. Modèle dominant de l'écosystème ransomware. L'opérateur développe et maintient le malware + l'infrastructure (leak site, portail de négociation). Les **affiliés** déploient le ransomware chez des victimes, moyennant partage des gains (typiquement 70/30 affilié/opérateur, parfois 80/20). Ce modèle a industrialisé le ransomware : LockBit, ALPHV, Conti historique, Black Basta, Play, RansomHub actuels.

**Initial Access-as-a-Service (IAaaS)**. Les IAB compromettent et **vendent l'accès** préqualifié. Modèle spécialisé : l'IAB ne ransomware pas lui-même, il vend à un opérateur ransomware (ou autre acheteur) un accès déjà installé. Prix : 500-50 000 USD selon la cible (CA, secteur, niveau de privilèges). Délai de monétisation : plus rapide que développer une intrusion soi-même.

**Phishing-as-a-Service (PhaaS)**. Kits de phishing prêts à l'emploi, avec interface de gestion, templates, hosting. LabHost (démantelé avril 2024), EvilProxy, Evilginx (open source mais utilisé massivement). PhaaS a popularisé l'**AiTM** (Adversary-in-the-Middle) qui contourne le MFA en capturant cookies de session.

**Malware-as-a-Service (MaaS)**. Location de malware — infostealers (Lumma, RedLine mensuel), loaders, RAT, cryptominers.

**DDoS-as-a-Service**. Booters et stressers. De quelques dollars par attaque à plusieurs centaines pour attaques soutenues.

**Hosting bulletproof**. Infrastructure pour héberger contenu illicite (Ch.9).

**Cryptage / Obfuscation-as-a-Service**. Crypters et obfuscateurs pour rendre malware FUD. Service essentiel pour les opérateurs malware.

**Money laundering-as-a-Service**. Services de blanchiment crypto. Commissions 10-30% (Ch.21).

**Account checker / cracking services**. Vérification en masse de combo lists contre des services cibles (valider quels credentials marchent réellement).

**Spam / SMS bombing services**. Services commerciaux d'envoi massif.

## 16.2 Profils d'acteurs typiques

**L'opérateur RaaS**. Figure centrale. Développe le malware, opère l'infrastructure, gère les affiliés, négocie les rançons. Équipe typique : 5-20 personnes. Revenu : plusieurs millions à dizaines de millions USD/an pour les groupes dominants. Exemple public : Dmitry Khoroshev / LockBitSupp (LockBit), autres en grande partie anonymes.

**L'affilié RaaS**. Exécutant opérationnel. Achète l'accès (via IAB ou compromet lui-même), déploie le ransomware, reçoit sa part des gains. Peut être indépendant ou partie d'une équipe. Skills : persistance, lateral movement, AD domination, parfois exfiltration. Turnover élevé — les affiliés changent de groupe selon conditions et opportunités.

**L'Initial Access Broker (IAB)**. Spécialisé dans la compromission initiale. Sources d'accès : exploitation d'edge devices (VPN, RDP exposés, vulnérabilités publiques), phishing, achat de logs, social engineering. Vend l'accès après qualification (confirmation des privilèges, cartographie minimale). Actifs connus : marées de posts sur XSS, Exploit, parfois accès de premier plan sur BreachForums.

**Le developer malware**. Écrit le code. Profil technique pur. Peut travailler pour un groupe, en freelance, ou vendre son malware comme produit. Certains devs sont très réputés dans l'écosystème pour des familles de malware spécifiques.

**Le courtier (broker) de données**. Collecte des données (achat, récupération de breaches publiés) et revend en les repackageant. Spécialisation par type (fullz, credentials bancaires, dossiers médicaux).

**Le money mule et le launderer**. Deux profils distincts. Le **mule** prête son compte bancaire ou son wallet crypto pour faire transiter des fonds — souvent recruté sous prétexte d'un emploi légitime, parfois consentant. Le **launderer** est professionnel, structure des opérations de blanchiment sophistiquées (multi-hop crypto, mixers, conversions off-chain).

**Le carder**. Spécialisé fraude cartes bancaires. Achète des dumps, les teste, les monétise (achats de biens revendables, cash advance, autres).

**Le script kiddie**. Amateur avec skills limités, utilise outils achetés. Majoritaire en nombre, minoritaire en impact. Dans les forums sérieux, traités avec condescendance.

**Le hacktiviste**. Motivation idéologique plus que financière. Opère souvent via canaux Telegram publics, moins sur forums .onion fermés. Anonymous historique, KillNet, Cyber Av3ngers, IT Army of Ukraine, etc. (Ch.38).

**L'agent étatique**. Opérateur qui utilise le dark web comme cover ou comme canal d'acquisition. APT29 a historiquement acheté des accès sur forums. La DPRK utilise le dark web pour vendre des données volées (Lazarus). Ces acteurs n'ont pas de « profil » simple — ils adaptent à chaque opération.

**L'analyste défensif / force de l'ordre / journaliste**. Observateur légitime (avec mandat). Se présente généralement comme lurker, parfois sous couverture avec persona active (Ch.22, Ch.23, Ch.30).

## 16.3 La chaîne de valeur d'une compromission moderne

Comprendre les acteurs permet de reconstituer la chaîne typique d'une attaque enterprise 2024-2026.

**Étape 1 — Vol initial de credentials**. Un utilisateur télécharge un logiciel crack piégé, son poste personnel est infecté par un infostealer (Lumma), ses credentials (y compris son compte pro utilisé sur le poste perso) sont exfiltrés.

**Étape 2 — Vente en bulk**. L'opérateur de stealer vend les logs en lot sur Russian Market. Log basique : 15 USD.

**Étape 3 — Achat par IAB**. Un IAB achète des logs en volume, les trie pour identifier ceux avec accès corporate intéressants (VPN, Citrix, tokens cloud).

**Étape 4 — Qualification par IAB**. L'IAB utilise les credentials pour entrer dans le SI cible, vérifier les privilèges, cartographier l'environnement, identifier les cibles de valeur (DC, fileservers, backups).

**Étape 5 — Vente à affilié RaaS**. L'IAB poste l'accès sur un forum : « Access RDP + AD domain admin, EU manufacturing company, CA 500M USD, 2 000 endpoints, backup Veeam visible ». Prix : 25 000 USD.

**Étape 6 — Déploiement ransomware**. L'affilié achète l'accès, déploie le ransomware du groupe (Black Basta, par exemple). Exfiltre d'abord 800 Go de données sensibles (double extorsion), puis chiffre.

**Étape 7 — Négociation et rançon**. La victime est contactée via portail de négociation. Rançon demandée : 3 M USD. Négociation éventuelle. Paiement en Bitcoin.

**Étape 8 — Partage des gains**. Affilié reçoit 70% (2,1 M USD), opérateur RaaS 30% (0,9 M USD). Transferts crypto vers wallets opérationnels.

**Étape 9 — Blanchiment**. Les fonds passent par mixers, swaps Monero, exchanges non-KYC, OTC desks. Après 3-6 mois de chaînes, partie des fonds est convertie en fiat utilisable.

**Étape 10 — Publication partielle ou totale si non-paiement**. Si la victime ne paie pas, le groupe RaaS publie tout ou partie des données sur son leak site. Certaines données valorisables peuvent être revendues en parallèle.

Toute cette chaîne — de l'infection initiale au blanchiment — peut prendre **3 à 6 mois**. Chaque étape est opérée par un acteur spécialisé, avec ses skills et ses marchés. La cybercriminalité est une **industrie structurée**, pas une activité individuelle.

Pour le défenseur, chaque étape de cette chaîne est une **opportunité d'interruption** : détecter le stealer avant l'exfiltration, le log avant l'achat par IAB, l'accès IAB avant la vente, l'affilié avant le déploiement, l'exfiltration avant le chiffrement, la rançon avant le paiement. Plus la détection est précoce, plus l'impact est limité.

## 16.4 Fil rouge — DARKSTREAM : la chaîne reconstituée

> **🌐 DARKSTREAM — Épisode 10 : cartographie de la chaîne**
>
> Au terme de 2 semaines d'investigation, Lucas reconstitue la chaîne probable de compromission Vectris.
>
> **Étape 1** — Infection initiale : un ingénieur R&D (VECTRIS-RD-112) a téléchargé un outil CAD crackéé depuis un site de warez. Infostealer Lumma déployé. Log exfiltré fin 2025.
>
> **Étape 2** — Vente du log sur Russian Market fin 2025, ~120 USD (tier « corporate VPN + tokens actifs », premium).
>
> **Étape 3** — Achat par un IAB russophone (pseudonyme identifié partiellement : **magnit_ru**, actif sur XSS Forum). Qualification : vérification que les credentials VPN fonctionnent, exploration réseau, identification que Vectris est un groupe industriel aerospace.
>
> **Étape 4** — Revente. magnit_ru poste l'accès sur XSS début 2026 : « Access aerospace EU, R&D network, defense programs ». Prix demandé : ~35 000 USD.
>
> **Étape 5** — Achat par aero_source (ou un commanditaire derrière lui). Hypothèse Lucas : aero_source est soit (a) un opérateur individuel qui a acheté l'accès et a exfiltré les 420 Go lui-même, soit (b) le front d'une équipe plus grande, soit (c) un revendeur qui a acheté le dump à un acteur qui lui a fait l'exfiltration.
>
> **Étape 6** — Exfiltration : ~12 semaines d'activité sur le réseau Vectris (traces cohérentes avec les logs Mandiant), 420 Go extraits, focus sur R&D propulsion et dossiers fournisseurs défense.
>
> **Étape 7** — Vente sur IndustrialLeaks : post public il y a 11 jours à 65 000 USDT.
>
> La chaîne implique donc **au moins 3 acteurs distincts** : opérateur Lumma (infection initiale, revente bulk), magnit_ru (IAB), aero_source (exfiltration ou revente finale). Complexifie l'attribution mais multiplie les angles d'investigation. Identifier un seul de ces acteurs précisément pourrait suffire à remonter la chaîne.

---
