---
title: Chapitre 71 — Sanctions, PEP, KYC/KYB et adverse media
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 71.1 Vue d'ensemble

Le **screening** sanctions / PEP / adverse media est l'une des composantes les plus systématiques de l'OSINT corporate moderne. Volume massif (banques screent des millions de clients), discipline mature, outils nombreux.

## 71.2 Sanctions : régimes

Voir Ch.7 et Ch.38. Régimes principaux :

- **OFAC** (US Treasury) : SDN List. Extraterritorialité forte.
- **UE** : liste consolidée par la Commission.
- **UK OFSI** post-Brexit.
- **ONU** : sanctions obligatoires globalement.
- **Sanctions sectorielles** (Iran, Russie, Corée du Nord, etc.).

## 71.3 PEP : politiquement exposées

**Définition.** Personnes occupant ou ayant occupé des fonctions publiques importantes (PEP étrangères, PEP nationales, PEP organisations internationales) + famille et associés proches.

**Obligation AMLD UE.** Vigilance renforcée pour toute relation avec PEP.

## 71.4 KYC / KYB : Know Your Customer / Business

**KYC** : vérification d'identité et de risque sur clients (banque, fintech, courtier).

**KYB** : équivalent sur partenaires commerciaux et fournisseurs.

**CSDDD** UE 2024 (Ch.7) impose vigilance supply chain.

## 71.5 Adverse media

Recherche presse négative sur entité / personne. Voir Ch.38.

## 71.6 Outils intégrés

**OpenSanctions.** Gratuit, agrège sanctions + PEP + adverse media. Standard 2026 pour budget limité.

**WorldCheck (Refinitiv / LSEG).** Standard institutionnel.

**Dow Jones Risk & Compliance.** Équivalent.

**ComplyAdvantage, Sayari, Sigma.** Alternatives modernes.

## 71.7 Méthodologie screening

1. Identification entité.
2. Screening sanctions OFAC / UE / UK / ONU.
3. Screening PEP (entité + dirigeants + UBO).
4. Adverse media multi-langues.
5. Match analysis (faux positifs filtrés).
6. Validation humaine.
7. Documentation pour audit.

## 71.8 Gestion des faux positifs

Les screening produisent souvent des faux positifs (homonymes). **Validation humaine** indispensable.

**Méthode.**

- Cross-vérification (date de naissance, juridiction, profession).
- Investigation de l'homonyme.
- Décision finale documentée.

## 71.9 Évolution réglementaire 2024-2026

- **CSDDD** : nouvel impératif supply chain.
- **Failure to Prevent Fraud UK** (sept 2025) : new offence.
- **MiCA** : régulation crypto VASPs.
- **Refonte AMLD** : 6e AMLD UE.

Conformité dynamique.

## 71.10 Renvois

Pour profondeur : cours FININT et cours Compliance / Due Diligence dédié.

-----
