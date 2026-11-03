---
title: Chapitre 13 — Microsoft Edge
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie V — Notre pratique
  - index.md
---

> 🧱 **Les bases**
>
> - **Chromium** est le moteur open source de Google Chrome. Edge est construit dessus depuis 2020 : **une faille Chromium touche en général Chrome et Edge**.
> - Le navigateur est l'application **la plus exposée** du poste : elle traite en permanence du contenu venu d'Internet.

## 13.1 Les canaux et le rythme

| Canal | Rythme | Usage |
|---|---|---|
| **Stable** | nouvelle version majeure **toutes les 4 semaines** ; **correctifs de sécurité dès que nécessaire**, souvent chaque semaine | le canal par défaut en entreprise |
| **Extended Stable** | version majeure **toutes les 8 semaines** (versions paires) ; correctifs de sécurité importants entre-temps | organisations qui veulent moins de changements fonctionnels |
| **Beta** | la version majeure suivante, environ 4 semaines avant Stable | tester la prochaine version (pilote IT) |
| **Dev** / **Canary** | hebdomadaire / quotidien | développeurs, curiosité ; pas en production |

Les failles Chromium **exploitées** (0-day) sont régulières : Google publie un correctif de Chrome, Microsoft publie l'équivalent pour Edge en général dans les jours qui suivent. Pour le MCS, **Edge est donc un cycle à part, beaucoup plus rapide que le Patch Tuesday**.

## 13.2 Le mécanisme de mise à jour

- Edge se met à jour par son propre composant, **Microsoft Edge Update** (`MicrosoftEdgeUpdate.exe`), avec deux services (`edgeupdate`, `edgeupdatem`) et des **tâches planifiées** qui vérifient régulièrement la disponibilité d'une nouvelle version **directement chez Microsoft**.
- Il est **aussi** publié dans **WSUS** (produit *Microsoft Edge*, classification *Updates*), et dans Intune / ConfigMgr.
- Il se pilote par les **modèles d'administration Edge Update** (ADMX à télécharger chez Microsoft, distincts des ADMX du navigateur) :

| Stratégie | Effet |
|---|---|
| *Update policy override* (par canal) / *Update policy override default* | autoriser les mises à jour automatiques, les mises à jour manuelles seulement, ou les désactiver |
| *Target version override* | figer Edge sur une version (préfixe), par exemple pendant un incident |
| *Rollback to target version* | revenir à la version cible si une version plus récente est installée |
| *Auto-update check period override* | fréquence de vérification |

Les valeurs se trouvent sous `HKLM\SOFTWARE\Policies\Microsoft\EdgeUpdate`, avec le GUID du canal Stable `{56EB18F8-B008-4CBD-B6D2-8C97FE7E9062}`.

> ⚠️ **Piège — Deux maîtres pour un seul navigateur**
>
> Si Edge Update reste libre de se mettre à jour **et** que l'équipe approuve Edge dans WSUS, c'est le plus rapide qui gagne : le navigateur se met à jour seul depuis Internet, et le groupe test ne teste rien. **Choisir un seul mécanisme maître** (WSUS ou Edge Update piloté par stratégie), le documenter, et vérifier sur le pilote que l'installation fonctionne avec les stratégies choisies.

## 13.3 La cadence bi-hebdomadaire

Le rythme de l'équipe — **deux passes par semaine, avec un groupe test, principalement pour les mises à jour de sécurité** — est adapté au rythme Chromium. Une organisation possible :

| Jour | Action |
|---|---|
| **Lundi** | synchronisation, approbation de la dernière version Stable sur le **groupe test Edge** |
| **Mardi-mercredi** | retours du groupe test (applications web métier, authentification unique, extensions, PDF, **mode Internet Explorer**) |
| **Jeudi** | approbation en **production** si rien n'est signalé |
| **À tout moment** | **0-day Chromium exploité** : groupe test quelques heures, production **sous 24 à 48 h** |

**Ce que le groupe test doit couvrir** : les applications web critiques (portail de tiers payant, intranet, outils RH), l'authentification (SSO, Entra ID), les extensions autorisées, l'impression depuis le navigateur, et les sites en **mode Internet Explorer** (applications anciennes déclarées dans la liste de sites d'entreprise), qui sont les plus fragiles.

**À suivre aussi** : le **runtime WebView2**, composant Edge utilisé par de nombreuses applications (nouveau Teams, nouvel Outlook, applications métier). Il suit le même cycle et se met à jour par Edge Update ; vérifier comment il est couvert dans votre configuration.

**Vérifier** : `edge://version` sur un poste ; à l'échelle du parc, l'inventaire de la version d'`msedge.exe` ou le rapport WSUS du produit *Microsoft Edge*.

> 🧵 **Fil rouge — Jeudi 2 juillet 2026 (scénario fictif)**
>
> Google annonce une faille Chromium exploitée ; Microsoft publie la version Edge corrigée le lendemain. Inès l'approuve sur le groupe test Edge à 10 h, reçoit deux retours positifs du service Prestations (portail de tiers payant) et un du service RH (mode IE), puis approuve la production à 15 h. Le soir, 91 % des postes ont la nouvelle version (le navigateur se met à jour au redémarrage d'Edge). Elle découvre en vérifiant que 300 postes avaient **déjà** la version, téléchargée seule via Edge Update : la stratégie de désactivation ne s'appliquait pas à l'OU des nomades. Elle corrige la GPO : un seul maître.

> 📌 **À retenir**
>
> - Edge = cycle Chromium : version majeure toutes les 4 semaines, sécurité chaque semaine ou presque.
> - Un seul mécanisme maître (WSUS ou Edge Update piloté), sinon le groupe test ne sert à rien.
> - 0-day Chromium exploité : production sous 24 à 48 h.

---
