---
title: Chapitre 42 — Breaches, leaks et pastebins
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 42.1 L'écosystème des données fuitées

Depuis 15 ans, l'écosystème des **breaches** (intrusions menant à exfiltration de données) et **leaks** (publications de données) a explosé. Yahoo, LinkedIn, Adobe, Dropbox, Equifax, T-Mobile, Marriott, plus récemment 23andMe, MOVEit, etc. — des milliards de credentials et informations personnelles circulent.

Pour l'analyste OSINT, ces données représentent une **source riche mais juridiquement et déontologiquement complexe**.

## 42.2 HIBP — Have I Been Pwned

**HIBP** (haveibeenpwned.com) est le standard public.

**Capacités.**

- Recherche par email : « cet email est-il dans des breaches connues ? ».
- Recherche par téléphone (limitée).
- API : Pwned Passwords (vérification password sans le révéler).

**Sources.** Troy Hunt vérifie chaque breach avant inclusion. Pas tous les leaks (filtré).

**Tarification.** Lookup gratuit individuel, API payante ($3.95/mois pour API key).

## 42.3 DeHashed

**DeHashed** (dehashed.com) est plus complet, plus profond, plus controversé.

**Capacités.**

- Recherche par email, username, IP, password hash, name, address, phone.
- Données dans certaines breaches en clair (selon ce que le leak originel contenait).
- Pivots multi-fields.

**Tarification.** ~$5/jour ou abonnement mensuel ~$30/mois.

**Précaution.** Les données peuvent inclure passwords. **Ne jamais utiliser** pour tenter d'accéder à un compte. Usage strictement d'investigation.

## 42.4 Intelligence X (IntelX)

**IntelX** (intelx.io) explore **deep web et leaks**.

**Capacités.**

- Recherche par email, username, domaine, BTC, IP, passport, etc.
- Pastes, dumps, archives Tor.
- Index très large.
- Snapshots historiques.

**Tarification.** Plus chère, orientée institutionnel.

## 42.5 Snusbase, LeakPeek et autres

**Snusbase**, **LeakPeek** : alternatives variées, qualité et légalité variables. Vérification du fournisseur recommandée.

## 42.6 ICIJ leaks — Pandora, Panama, etc.

Les **leaks journalistiques majeurs** sont différents techniquement (documents internes, pas credentials), mais constituent une famille apparentée :

- **Panama Papers** (2016) : 11.5 M docs Mossack Fonseca.
- **Paradise Papers** (2017) : 13.4 M docs Appleby.
- **Pandora Papers** (2021) : 11.9 M docs multi-cabinets.
- **FinCEN Files** (2020) : 2100 Suspicious Activity Reports.
- **Cyprus Confidential** (2023) : leak chypriote majeur.

**Accès.** ICIJ Offshore Leaks Database (extracts + métadonnées). Documents bruts réservés aux journalistes ICIJ partenaires.

## 42.7 Pastebins

**Pastebins** (pastebin.com, paste.ee, ghostbin, etc.) hébergent des bouts de texte, souvent éphémères. Utilisés pour partager du code, mais aussi pour publier des leaks.

**Outils.**

- **PasteHunter** : monitoring de pastes.
- **Searches IntelX** indexent pastes.
- **Pastes archive** sur archive.org parfois.

## 42.8 Cadre légal d'usage

**Pour les LEA.** Largement autorisés à utiliser les leaks pour orientation.

**Pour les journalistes.** Liberté de presse et intérêt public sont des protections fortes (jurisprudence française et européenne).

**Pour les analystes privés non-journalistes.** Zone grise :

- **Consulter** un leak public reste généralement toléré.
- **Exploiter** (intégrer dans rapport commercial, citer comme source) est juridiquement plus risqué, particulièrement si données issues d'un piratage avéré.

**Règle pratique.**

- Documenter l'origine.
- Ne pas reproduire les données brutes.
- Citer les analyses publiées par sources autorisées (ICIJ notamment) plutôt qu'accès aux dumps.
- Consultation avocat en cas de doute.

## 42.9 Pivots OSINT depuis breaches

Une fois un email/username confirmé dans une breach, plusieurs pivots :

- **Password reuse** : si un password leakée pour un compte est testé sur un autre compte de la même personne. **Ne jamais exploiter** (CFAA US, art. 323-1 FR). Mais signal que la personne réutilise → faiblesse OPSEC.
- **Date de breach** : situe la création du compte avant la date de breach.
- **Username dans breach** : ouvre Sherlock pour autres plateformes.
- **Phone dans breach** : pivot téléphone.

## 42.10 Minimisation et déontologie

Le travail avec breaches impose :

- **Minimisation** : utiliser uniquement ce qui sert l'enquête.
- **Non-publication** : pas de diffusion des données brutes.
- **Stockage chiffré** : si conservation nécessaire.
- **Destruction** à fin d'enquête.

> **Principe.** Les breaches sont des sources d'orientation, pas des preuves directes. Une affirmation « Cet email apparaît dans la breach LinkedIn 2012 » est une orientation (cotation prudente). Pas une preuve d'identité.

-----
