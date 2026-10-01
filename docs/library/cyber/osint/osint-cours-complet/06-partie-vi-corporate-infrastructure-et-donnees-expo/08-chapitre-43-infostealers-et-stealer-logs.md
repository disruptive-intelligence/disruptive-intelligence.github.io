---
title: Chapitre 43 — Infostealers et stealer logs
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 43.1 Le phénomène stealer logs

Les **infostealers** (malwares voleurs d'informations : RedLine, Vidar, Raccoon, Lumma, Stealc, etc.) sont devenus une économie criminelle massive depuis 2020-2021. Ils infectent des PC personnels, exfiltrent les données stockées dans les navigateurs (cookies, mots de passe), wallets crypto, fichiers récents.

Les **stealer logs** (dumps de ces exfiltrations) sont vendus ou publiés sur Telegram, marketplaces dark web, forums. Volume astronomique : des millions de logs par mois.

## 43.2 Anatomie d'un stealer log

Un log typique contient :

- **Credentials browser** : URL + email + password sauvegardés.
- **Cookies session** : peuvent permettre session hijacking.
- **Wallets crypto** : fichiers wallet, seeds (rare en clair).
- **Autofill data** : adresses, cartes (partielles).
- **System info** : machine name, user, IP, OS.
- **Screenshot** parfois.

## 43.3 Marché stealer logs

**Telegram** est la plateforme principale.

**Canaux observables (en consultation passive).**

- Dumps gratuits (logs « publics ») destinés à attirer.
- Channels payants (private logs).
- Marketplaces brokers.

**Tarifs.** Quelques cents par log basique, plusieurs $ pour log avec wallets crypto ou credentials premium.

## 43.4 Outils OSINT pour stealer logs

**Hudson Rock** (hudsonrock.com). Service commercial spécialisé. Permet de tester si un email est dans des logs récents.

**SpyCloud** (spycloud.com). Standard institutionnel CTI. Très complet.

**LeakIX** : alternative.

**Telegram observation directe** : compte d'investigation observe les canaux publics.

## 43.5 Cas d'usage OSINT

**Pour investigation personne.** Tester si l'email perso de la cible apparaît dans des logs → révèle compromission, peut révéler comptes utilisés (Binance, ProtonMail, etc.).

**Pour CTI.** Identifier les machines compromises dans une organisation cible.

**Pour due diligence.** Maturité sécurité.

## 43.6 Cadre légal et déontologique

**Consultation.** Légalement plus risqué que breaches publiques car les logs sont issus d'intrusions illégales. Toléré en cadre d'investigation documenté, à manier avec précaution.

**Pas d'exploitation** des credentials (CFAA, art. 323-1).

**Documentation.** Capture du résultat de recherche (Hudson Rock par exemple), pas téléchargement des logs bruts.

## 43.7 Stealer logs sur Telegram : méthodologie

1. Compte d'investigation Telegram dédié.
2. Identification de canaux publics (Telegago).
3. Observation passive (joindre, ne pas interagir).
4. Recherche par email dans channels gratuits / search bots disponibles.
5. Capture du résultat (sans télécharger le log entier).
6. Documentation rigoureuse.

## 43.8 Limites

- Les logs peuvent contenir des erreurs.
- Date d'infection variable.
- Email peut être valide mais compte de longue date inutilisé.
- Faux logs (fabriqués pour usage marchand).

> **MIRAGE — Épisode 10 : Breaches, leaks et stealer logs**
>
> L'analyste poursuit l'investigation de Delaunay via breaches.
>
> **HIBP sur `marc.delaunay76@gmail.com`** : 6 hits dans breaches (LinkedIn 2012, Adobe 2013, Dropbox 2012, MyFitnessPal 2018, Disqus 2017, Canva 2019). Confirmation que c'est un email actif depuis 2010+.
>
> **DeHashed sur même email** : confirme et ajoute Anti-Public Combo List, Collection #1. Pas de pivots majeurs au-delà de l'identification du compte.
>
> **Hudson Rock** : test sur `marc.delaunay76@gmail.com`. **Hit positif** : machine compromise par RedLine Stealer en septembre 2025, IP française (Paris), 47 credentials capturés. Liste des URLs : LinkedIn, ProtonMail (compte perso), Binance, Apple ID, plusieurs e-commerces, et notamment **Binance** avec credentials.
>
> **Capture sur Telegram (compte invest)** : recherche du dump dans canal `@cloudsec_dumps` (visité au MIRAGE 7). Trouvé : un dump du 15 septembre 2025 incluant `marc.delaunay76@gmail.com`. Capture en lecture seule : 47 credentials, dont compte Binance (URL + email + password en clair partiellement masqué dans la capture).
>
> **Implications majeures.**
> 1. Delaunay utilise un compte Binance personnel. **Pivot crypto majeur** — à explorer dans MIRAGE 14 (renvoi OSINT Crypto vFULL).
> 2. La compromission est récente (septembre 2025) → credentials probablement encore frais à la date du dump.
> 3. Le compte ProtonMail perso révèle une infrastructure email plus complexe que l'email Gmail seul (Delaunay a un compte chiffré pour communications sensibles).
> 4. La compromission étant due à un infostealer, ce n'est pas un signe de compétence de la part des attaquants ciblant Delaunay — c'est une infection opportuniste classique. Mais le **rapport offre des sélecteurs**.
>
> **Précautions OPSEC déontologiques.**
> - Aucun téléchargement du log (consultation visuelle uniquement).
> - Aucune tentative d'usage des credentials.
> - Documentation : capture horodatée + cotation B2 (source secondaire de qualité moyenne).
> - Le rapport mentionnera l'existence du log pour orientation procédure (PNF peut réquisitionner le log s'il devient pertinent).

-----
