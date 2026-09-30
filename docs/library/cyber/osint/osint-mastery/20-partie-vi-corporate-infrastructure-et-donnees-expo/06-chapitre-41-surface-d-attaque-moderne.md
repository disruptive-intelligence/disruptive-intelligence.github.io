---
title: Chapitre 41 — Surface d'attaque moderne
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 41.1 De l'infrastructure à la surface d'attaque

Au-delà de l'inventaire, l'**analyse de surface d'attaque** identifie les **points d'exposition** d'une organisation : services mal configurés, secrets exposés, données fuitées, technologies vulnérables.

Cette analyse intéresse l'OSINT pour :

- **Due diligence** : évaluer la maturité sécurité d'un partenaire/cible.
- **CTI** : comprendre ce qu'un attaquant verrait.
- **Investigation** : identifier l'origine d'un incident.
- **Bug bounty** : recherche éthique de vulnérabilités.

## 41.2 Cloud et SaaS exposés

**Buckets S3 / Azure Blob / GCS.** Stockage cloud souvent mal configuré.

**Outils.**

- **Bucket finders** (S3Scanner, etc.).
- **GrayhatWarfare** : index public de buckets ouverts.
- **Cloud Storage Finder**.

**Cas d'usage.** Vérifier si TechnoVert a des buckets S3 publics potentiellement exposant des données.

**Précaution juridique.** Identifier un bucket ouvert ≠ y accéder. Consulter peut basculer en Bluetouff. En cas de découverte, signaler à l'organisation.

## 41.3 GitHub leaks et secrets exposés

**GitHub** est une mine de secrets accidentellement exposés : API keys, credentials, configurations internes.

**Outils.**

- **GitHub Code Search** (avec opérateurs).
- **gitleaks** : scan local de repos.
- **TruffleHog** : détection de secrets.
- **GitGraber**.

**Dorks GitHub.**

```
"technovert" "password"
"@technovert.fr" extension:env
"DB_PASSWORD" "technovert"
filename:.env "technovert"
```


**Pour due diligence.** Identifier l'exposition GitHub d'une cible révèle :

- Maturité sécurité interne.
- Secrets actuellement valides (risque).
- Identités d'employés (via commits).

**Déontologie.** Si découverte de secrets actifs, signaler à l'organisation. Ne pas exploiter.

## 41.4 Technologies web et empreinte applicative

Identifier les **technologies utilisées** par un site révèle :

- Stack technique (Apache, Nginx, PHP, Python, Node.js).
- Frameworks (Laravel, Django, React, Vue).
- CMS (WordPress, Drupal, Joomla).
- Plugins, librairies.
- Outils analytics (GA, Mixpanel, Hotjar).
- CDN, hébergement.

**Outils.**

- **Wappalyzer** (extension navigateur, gratuit).
- **BuiltWith** (builtwith.com) : profile complet, payant pour fonctions avancées.
- **WhatRuns** : alternative.

**Cas d'usage OSINT.** Identifier les technologies vieilles ou vulnérables. Identifier les correspondants tiers (révèle écosystème).

## 41.5 Typosquatting et domaines frauduleux

Le **typosquatting** est l'enregistrement de domaines proches d'un domaine légitime pour piéger les utilisateurs (`technovrt.fr`, `technowert.fr`, `technovert-rh.com`).

**Outils.**

- **DNSTwist** : génère et vérifie les variantes.
- **URLCrazy**.
- **dnstwister.report**.

**Cas d'usage.**

- Identifier les domaines suspects autour de la cible.
- Détection précoce de campagnes de phishing visant la cible.
- Cluster de domaines frauduleux (un même attaquant enregistre plusieurs typosquats).

## 41.6 Email exposure et compromissions

Voir Ch.42 et Ch.43 pour le détail. L'exposition d'emails dans des breaches est un volet majeur de la surface d'attaque.

## 41.7 Surface d'attaque continue (ASM)

**ASM** (Attack Surface Management) : monitoring continu de la surface d'attaque.

**Outils commerciaux.**

- **Bitsight**.
- **SecurityScorecard**.
- **RiskIQ** (Microsoft).
- **Censys Continuous**.
- **Shodan Monitor**.

**Pour OSINT.** Souvent réservé aux usages CTI / cybersécurité, mais certains éléments accessibles en consultation ponctuelle.

## 41.8 Audit de surface d'attaque OSINT : workflow

1. **Inventaire domaines + sous-domaines** (Ch.39-40).
2. **Inventaire IPs** + ASN.
3. **Scan passif** (Shodan, Censys) : services exposés.
4. **Cloud assets** : buckets, Azure, GCS via outils dédiés.
5. **GitHub** : secrets exposés.
6. **Technologies** : Wappalyzer, BuiltWith.
7. **Typosquatting** : DNSTwist.
8. **Breaches emails** : HIBP, DeHashed (Ch.42).
9. **Stealer logs** : Hudson Rock, SpyCloud (Ch.43).
10. **Synthèse de risque**.

-----
