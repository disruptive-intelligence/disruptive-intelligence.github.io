---
title: Chapitre 75 — Surface d'attaque et exposition cyber
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 75.1 De la CTI à la surface d'attaque

L'**analyse de surface d'attaque** (Attack Surface Management — ASM) identifie ce qu'un attaquant verrait d'une organisation : domaines, sous-domaines, services exposés, technologies, fuites.

C'est le pendant **défensif** de la CTI : savoir ce qu'on expose pour le protéger.

Voir Ch.41 pour la vue technique. Ce chapitre approfondit l'angle CTI.

## 75.2 Composantes de la surface d'attaque

**Surface technique.**

- Domaines, sous-domaines (Ch.39-40).
- IPs, ASN (Ch.40).
- Services exposés (Shodan, Censys).
- Technologies (Wappalyzer, BuiltWith).
- Buckets cloud, S3 (Ch.41).
- GitHub leaks (Ch.41).

**Surface humaine.**

- Identités d'employés (LinkedIn, communiqués).
- Emails exposés.
- Présences réseaux sociaux.
- Information publiable sur procédures internes.

**Surface organisationnelle.**

- Sous-traitants, prestataires.
- Supply chain logicielle.
- Partenaires.

## 75.3 Outils ASM

**Commercial.**

- **Bitsight** : standard.
- **SecurityScorecard**.
- **RiskIQ** (Microsoft).
- **Censys Continuous**.
- **Shodan Monitor**.
- **PaloAlto Cortex Xpanse**.

**Open source / gratuit.**

- **Amass** + **subfinder** (Ch.40).
- **GoSpider**, **httpx**.
- Combinaisons custom.

## 75.4 Workflow ASM

1. **Inventaire** : domaines, IPs, services.
2. **Scan passif** : Shodan, Censys.
3. **Identification vulnérabilités connues**.
4. **Cloud assets** : buckets, exposed services.
5. **Code leaks** : GitHub search.
6. **Email exposure** : HIBP, DeHashed.
7. **Stealer logs** : Hudson Rock.
8. **Synthèse risque**.
9. **Recommandations**.

## 75.5 Typosquatting et phishing

**DNSTwist** pour identifier typosquats.

**Monitoring** : alertes nouveaux enregistrements suspects.

**Pour due diligence.** Identifier campagnes de phishing visant une entité.

## 75.6 Maturité sécurité comme signal

L'exposition cyber d'une organisation est un **signal** de maturité sécurité.

**Signaux maturité haute.**

- Bonnes pratiques SPF/DKIM/DMARC.
- Pas de secrets GitHub.
- Buckets cloud sécurisés.
- Patches à jour.

**Signaux maturité basse.**

- Services obsolètes exposés.
- Buckets ouverts.
- Secrets sur GitHub.
- Email patterns prévisibles + breaches massives.

## 75.7 Renvoi CTI

Pour la profondeur (threat hunting, intrusion analysis, attribution avancée, reverse engineering), renvoi vers **cours CTI dédié**.

## 75.8 Synthèse — ASM en pratique

L'ASM OSINT est une compétence de plus en plus demandée : par les RSSI (vue interne), par les acquéreurs (M&A), par les régulateurs (cyber resilience).

-----
