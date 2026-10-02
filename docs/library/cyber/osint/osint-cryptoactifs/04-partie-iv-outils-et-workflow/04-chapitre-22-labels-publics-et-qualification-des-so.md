---
title: Chapitre 22 — Labels publics et qualification des sources
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IV — Outils et workflow
  - index.md
---

Les **labels** sont les étiquettes qui transforment des adresses anonymes en entités identifiables (« exchange Binance », « Tornado Cash », « Lazarus wallet »). Toute l’enquête en dépend. Mais la qualité varie énormément. Ce chapitre apprend à qualifier les sources et à manipuler les labels avec discernement.

## 22.1 Sources de labels

**Labels Etherscan** (et explorateurs publics) :

- Sourcés par : Etherscan eux-mêmes, contributions communautaires, déclarations d’entités.
- Couverture : exchanges majeurs, smart contracts populaires, certaines adresses notables.
- Qualité : variable. Bonne pour exchanges connus, faible pour acteurs criminels (souvent à jour avec délai).

**Labels Tronscan, Solscan, etc.** :

- Moins riches qu’Etherscan.
- Couvrent les services majeurs sur la chaîne.

**Labels Chainalysis (Reactor, KYT)** :

- Sourcés par : recherche interne Chainalysis, partenariats avec exchanges (KYC information dans certains cas), saisies publiques, OSINT.
- Couverture : très étendue. Centaines de milliers d’entités labellisées.
- Qualité : élevée pour exchanges régulés, moyenne pour acteurs criminels (avec délai pour nouveaux acteurs).

**Labels TRM Labs** :

- Logique similaire à Chainalysis. Bases label distinctes.
- Particulièrement fort sur compliance (Know Your VASP) — exchanges et VASPs dans le monde entier.

**Labels Elliptic** :

- Idem.

**Labels OFAC SDN list** :

- **Source officielle US** : adresses sanctionnées.
- Mise à jour régulière.
- **Référence absolue** pour sanctions : si une adresse y est, elle est officiellement sanctionnée.
- URL : `treasury.gov/ofac/downloads/sdnlist.txt` ou format JSON/XML.

**Labels EU sanctions list** :

- Liste UE des sanctions financières.
- Inclut désormais des adresses crypto.

**Labels saisies / press releases** :

- DOJ, FBI, NCA, Europol, ANSSI, etc. publient parfois des adresses crypto liées à saisies / opérations.
- Officielles, vérifiables.
- Mais limitées dans la couverture (seulement les cas annoncés publiquement).

**Labels par chercheurs publics** :

- ZachXBT (twitter.com/zachxbt) : très actif, attributions souvent reconnues.
- Researchers indépendants.
- Qualité variable selon réputation.

**Labels par communautés** :

- Chainabuse (signalement scams).
- OnChainScores.
- Crypto Scam DB.
- Variable.

**Labels par leaks** :

- Parfois, des leaks (Twitter, Pastebin, dump publics) révèlent des adresses associées à des entités.
- À vérifier avec rigueur.

**Labels par recherche académique** :

- Papers académiques publient parfois listes d’adresses.
- Source crédible, mais peut être obsolète.

## 22.2 Qualification des labels

Tous les labels ne se valent pas. Critères de qualité :

**Source** : qui a produit le label ? Vendor pro (Chainalysis), source officielle (OFAC), chercheur réputé (ZachXBT) ou source anonyme/communautaire.

**Méthode** : sur quelle base l’attribution a été faite ? Preuve directe (saisie), partenariat (KYC), inférence (heuristique), recoupement OSINT.

**Date** : quand le label a été créé ? Un label de 2020 peut être obsolète en 2026 (compromission, vente, transfert de wallet).

**Validation indépendante** : d’autres sources convergent-elles ? Validation croisée multiple.

**Spécificité** : le label est-il précis (« hot wallet 3 de Binance ») ou vague (« exchange ») ? Précision = utilisable pour décisions, vague = orientation seulement.

## 22.3 Échelle de confiance des labels

**Référence absolue** :

- Sanctions OFAC SDN list.
- Sanctions UE / ONU.
- Annonce officielle d’une autorité (FBI press release avec adresses).
- Annonce officielle d’un exchange (« voici notre hot wallet »).

**Très fiable** :

- Labels Chainalysis / TRM / Elliptic « high confidence ».
- Multiple convergence multi-vendor.
- Attribution publique par chercheurs reconnus + validation.

**Fiable** :

- Labels Chainalysis / TRM / Elliptic « medium confidence ».
- Source unique mais réputée.
- Recoupements OSINT cohérents.

**À vérifier** :

- Labels Etherscan communautaires non vérifiés.
- Mentions sur Twitter de chercheurs moins connus.
- Attributions par seul outil sans validation.

**Faible confiance** :

- Mentions sur forums.
- Attributions par sources anonymes.
- Patterns sans label vendor.

## 22.4 Limites communes

**Labels obsolètes**. Une adresse labellisée « Binance » peut avoir été abandonnée par Binance et reprise par d’autres. Les outils mettent à jour avec délai.

**Labels par contagion erronée**. Si un label est attribué à un cluster entier mais qu’une adresse du cluster est en fait différente, le label se propage par erreur.

**Labels marketing**. Certains vendors peuvent labelliser de manière promotionnelle (« voici nos labels exclusifs »). Critique nécessaire.

**Manque de transparence**. Souvent, l’analyste ne peut pas savoir **comment** un label a été attribué. Confiance par défaut + validation croisée.

**Conflits entre vendors**. Chainalysis et TRM peuvent occasionnellement diverger sur un cluster ou un label. Validation croisée et investigation manuelle requise.

## 22.5 Bonnes pratiques

**Ne jamais reposer sur un seul label**. Pour décisions importantes, recoupement minimum.

**Documenter la source**. Dans la fiche, noter explicitement « Label Chainalysis ‘Binance Hot Wallet’ (confidence: high), confirmé TRM ‘Binance Hot 3’ ».

**Vérifier les sanctions OFAC**. Pour toute adresse importante, vérification SDN. C’est gratuit et rapide.

**Mettre à jour**. Les labels évoluent. Lors des phases de revue, re-vérifier.

**Croiser avec OSINT externe**. Pour adresses notables, recherche Twitter/Google peut révéler attributions complémentaires.

**Marquer le doute**. Si un label semble suspect (incohérence avec le pattern observé), noter et investiguer avant d’utiliser.

## 22.6 Le cas spécial : sanctions OFAC

Les **sanctions OFAC** méritent traitement spécial.

**Liste SDN (Specially Designated Nationals)**. Tenue par OFAC (Office of Foreign Assets Control, US Treasury). Inclut :

- Personnes physiques sanctionnées.
- Entités sanctionnées (entreprises, organisations).
- **Adresses crypto sanctionnées**.

**Mise à jour** : régulière, avec annonces officielles.

**Implications légales** : interagir avec une adresse OFAC depuis un US person ou via un VASP US peut constituer **violation des sanctions**. Sanctions sévères. Pour entités EU, le cadre est aussi strict (sanctions UE).

**Cas notables** :

- **Tornado Cash** : sanctionné août 2022. Adresses des smart contracts incluses.
- **Garantex** (exchange) : sanctionné avril 2022.
- **Suex** (exchange) : sanctionné septembre 2021.
- **Bitzlato** : sanctionné janvier 2023.
- **Multiple wallets Lazarus** : sanctionnés depuis 2018-2024.

**Pour l’analyste** : toute adresse pertinente est cross-checked avec SDN list. Outils pro intègrent cette vérification automatiquement. Outils gratuits : vérification manuelle possible via le site OFAC.

## 22.7 Construire sa propre base label

Pour cabinets ou organisations qui investiguent régulièrement, **base label interne** vaut investissement.

**Format type** :

```
| Adresse | Blockchain | Label | Source | Date | Confiance | Notes |
|---|---|---|---|---|---|---|
| bc1q[...] | BTC | Akira receive Aurélien Médical | MIXSHADOW investigation Athéna | 2026-03-14 | High | Adresse fraîche dédiée victime |
| 0xAk1[...] | ETH | Akira ETH wallet (probable) | MIXSHADOW investigation Athéna | 2026-03-19 | Medium | Reçoit fonds via FixedFloat |
| TR[Akira-TRON][...] | TRX | Akira TRON wallet (probable) | MIXSHADOW investigation Athéna | 2026-03-22 | Medium | Reçoit USDT depuis exchange non-KYC X |
```


**Maintenance** : revue trimestrielle, vérification labels obsolètes, ajout de nouvelles attributions.

**Partage** : avec partenaires sectoriels (ISAC, autorités) selon TLP. Contribution à l’écosystème.

-----
