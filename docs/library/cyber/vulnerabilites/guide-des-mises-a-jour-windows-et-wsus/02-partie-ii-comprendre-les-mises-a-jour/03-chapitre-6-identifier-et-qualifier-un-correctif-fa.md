---
title: Chapitre 6 — Identifier et qualifier un correctif, faire sa veille
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie II — Comprendre les mises à jour
  - index.md
---

> 🧱 **Les bases**
>
> - **Qualifier** un correctif, c'est décider **quelle urgence** il mérite chez *nous* : pas sa gravité dans l'absolu, mais le risque réel pour *notre* parc.
> - La **veille** consiste à surveiller régulièrement des sources fiables pour apprendre au plus tôt ce qui change : nouvelles failles, régressions, fins de support.

## 6.1 Les identifiants

| Terme | Exemple | Ce que c'est |
|---|---|---|
| **KB** (*Knowledge Base*) | KB5043080 | Numéro de l'**article de support** Microsoft qui décrit un paquet de mise à jour. Par extension : la mise à jour elle-même (« la KB du mois »). La même KB peut exister pour plusieurs architectures (x64, ARM64) |
| **CVE** (*Common Vulnerabilities and Exposures*) | CVE-2025-59287 | Identifiant **universel** d'une vulnérabilité. Une cumulative corrige des dizaines de CVE ; une CVE peut être corrigée par plusieurs KB (une par produit/version) |
| **CVSS** | 9.8 | Note de gravité **technique** (0 à 10) d'une CVE, calculée selon un standard public |
| **Gravité MSRC** | Critique, Important, Modéré, Faible | Note de Microsoft ; visible dans WSUS (*MsrcSeverity*) |
| **Exploited / Publicly disclosed** | *Yes* | La faille est-elle déjà **exploitée**, ou ses détails **publics** ? **Le critère n°1 pour accélérer** |
| **Exploitability Index** | *Exploitation More Likely* | Estimation Microsoft de la probabilité d'exploitation prochaine |
| **Security Update Guide** | msrc.microsoft.com/update-guide | Base officielle : CVE ↔ produits ↔ KB |
| **Release notes** du mois | « November 2026 Security Updates » | Récapitulatif du Patch Tuesday |
| **KEV** (CISA) | *Known Exploited Vulnerabilities* | Catalogue américain des failles **exploitées** : référence mondiale pour prioriser |
| **EPSS** | 0,94 | Score statistique (FIRST) de probabilité d'exploitation dans les 30 jours : un **signal**, pas un verdict |
| **Avis CERT-FR** | CERTFR-2026-AVI-xxxx | Avis français publié le soir du Patch Tuesday ; les **alertes** CERT-FR signalent les cas les plus graves |
| **Bulletin MSxx-yyy** | MS17-010 | **Ancien** format Microsoft, abandonné en 2017 au profit du Security Update Guide. On le croise encore dans les scanners et les vieilles documentations |

**Dans WSUS**, une mise à jour est identifiée par un **UpdateID** (GUID) et un **numéro de révision** : Microsoft peut republier une mise à jour (métadonnées corrigées, règle d'applicabilité modifiée) **sans changer de KB**. Les anciennes révisions sont supprimées par l'assistant de nettoyage (Ch.10).

## 6.2 Lire une page KB

Une page KB se lit **avant chaque déploiement**, pas après l'incident.

| Section | Ce qu'on y cherche |
|---|---|
| *Summary* / *Highlights* | ce qui est corrigé, les nouveautés éventuelles |
| *Improvements* | les changements non sécurité (souvent repris de la préversion) |
| **Known issues** | **les problèmes connus** : à lire systématiquement, avec les contournements proposés |
| *How to get this update* | par où elle passe (Windows Update, WSUS, catalogue), **prérequis** (SSU, checkpoint) |
| *File information* | liste des fichiers et versions (utile pour vérifier une installation) |

Compléments indispensables : **Windows release health** (problèmes connus par version, état des déploiements, fins de support) et, pour un administrateur Microsoft 365, le **Message Center** (annonces de changements).

## 6.3 Remplacement, expiration, KIR

- **Remplacée** (*superseded*) : une mise à jour plus récente fait la même chose et plus. Dans WSUS, on la **refuse** quand plus aucune machine n'en a besoin (Ch.10).
- **Expirée** : retirée par Microsoft (défaut grave). À refuser.
- **KIR** (*Known Issue Rollback*) : quand un changement **non sécurité** d'une cumulative pose problème, Microsoft le désactive à distance sur les machines non gérées. Sur un parc géré par WSUS, Microsoft publie un **fichier .msi** qui installe un modèle de GPO ; on applique cette GPO aux machines concernées, puis on redémarre. Le correctif de sécurité, lui, reste installé.

## 6.4 La grille de qualification

La gravité Microsoft ou le CVSS ne suffisent pas. Une faille « critique » dans un composant absent du parc ne vaut rien ; une faille « importante » exploitée, sur des postes exposés, vaut une urgence. On croise **quatre questions** :

1. **Est-elle exploitée ?** (*Exploited: Yes*, présence au KEV, alerte CERT-FR)
2. **Sommes-nous concernés ?** (produit, version, rôle ou fonction activée : WSUS, RDP, Hyper-V, spouleur…)
3. **Sommes-nous exposés ?** (accessible depuis Internet ? depuis les postes utilisateurs ? seulement en local ?)
4. **Quelle est la criticité métier** des machines touchées ? (contrôleurs de domaine, serveurs exposés, postes de la direction…)

| Priorité | Critère typique | Délai cible indicatif | Circuit |
|---|---|---|---|
| **P0 — Urgence** | exploitée (ou PoC public) **et** concerne un actif exposé ou critique | **24 à 72 h** | voie d'urgence (Ch.12) |
| **P1 — Accélérée** | exploitée sur un composant présent mais peu exposé, ou critique non exploitée sur un actif exposé | **7 jours** | pilote raccourci |
| **P2 — Standard** | le reste du Patch Tuesday | **cycle mensuel** (≈ 15 jours) | cycle normal |
| **P3 — Différée** | non applicable de fait, ou risque de régression avéré avec mesure compensatoire | dérogation datée | CAB + RSSI |

Les délais sont **indicatifs** : chaque organisation les fixe dans sa politique de mise à jour, validée par la RSSI. Le guide d'hygiène de l'ANSSI demande de définir et d'appliquer une telle politique ; certains référentiels ou contrats imposent des délais précis.

> ⚠️ **Pièges de qualification**
>
> - Un **CVSS 9.8 n'est pas une urgence** si le composant est absent ; un **CVSS 7.8 exploité** (élévation de privilèges locale) peut l'être, car c'est l'étape qui suit souvent un hameçonnage.
> - Un **scanner de vulnérabilités** qui signale une KB manquante peut se tromper : KB remplacée (la cumulative suivante est installée), redémarrage en attente, détection par version de fichier mal mise à jour. Un scanner est un **signal**, à confirmer par l'UBR (Annexe D).
> - Le score **EPSS** est statistique : il aide à trier, il ne remplace pas la question « sommes-nous exposés ? ».

## 6.5 La veille

| Catégorie | Source | Ce qu'on y trouve |
|---|---|---|
| Microsoft officiel | **Security Update Guide** (MSRC) | toutes les CVE, KB, gravités, mentions *Exploited* |
| | **Windows release health** | problèmes connus, fins de support, état des versions |
| | **Windows IT Pro Blog** (Tech Community) | annonces de changements (hotpatch, WSUS, calendrier) |
| | **Message Center** (centre d'administration Microsoft 365) | changements planifiés, rappels de fin de service |
| | Notes de version **Microsoft Edge** | versions Stable et correctifs de sécurité |
| Institutionnel | **CERT-FR** (avis, alertes, bulletin d'actualité) | lecture française, gravité, recommandations |
| | **CISA KEV** | failles exploitées, avec flux RSS et fichier JSON |
| Communauté | mégafil *Patch Tuesday* de r/sysadmin, liste **patchmanagement.org** | **retours de terrain** sur les régressions, dans les heures qui suivent |
| | Analyses mensuelles ZDI, Tenable, Rapid7, Qualys | lecture commentée et priorisée du Patch Tuesday |
| | BleepingComputer, Born's Tech and Windows World | actualité des régressions et des OOB |

✅ **Organiser sa veille**

- **Un agrégateur RSS** (ou un canal Teams/Slack alimenté par flux) avec les sources ci-dessus, plutôt que des visites au hasard.
- **Une routine** : mardi soir lecture rapide (gravités, *Exploited*) ; mercredi matin qualification ; lecture quotidienne des retours communautaires pendant la semaine pilote.
- **Une fiche de veille mensuelle** (modèle en Annexe C) : CVE exploitées, KB par produit, *known issues*, décision, date. C'est aussi une **preuve** en audit.
- **Automatiser** ce qui peut l'être : l'API du Security Update Guide (format CVRF/CSAF) permet de récupérer chaque mois la liste des CVE et KB par produit (approfondissement : version complète, Ch.7).

> ⚠️ **Fiabilité** — Une régression signalée sur Reddit le mercredi matin peut être un cas isolé (pilote tiers, configuration exotique). Avant de suspendre un déploiement, chercher **la confirmation** : plusieurs témoignages indépendants, entrée dans les *known issues* Microsoft, reproduction sur votre groupe pilote.

> 🧵 **Fil rouge — Mercredi 10 juin 2026 (scénario fictif bâti sur un cas réel)**
>
> Le Patch Tuesday de juin corrige une faille divulguée publiquement hors du processus coordonné : Microsoft la livre exceptionnellement en « base » pour les appareils en hotpatch. Inès remplit la grille : faille d'élévation de privilèges, *Publicly disclosed: Yes*, présente sur tous les postes Windows 11, exploitable après une simple infection par hameçonnage. Elle propose un **P1** : pilote de 48 h au lieu de 7 jours, puis déploiement général à J+3. La RSSI valide, le CAB est informé *a posteriori* selon la procédure d'urgence.

> 📌 **À retenir**
>
> - KB = paquet ; CVE = faille ; une cumulative = des dizaines de CVE.
> - Lire **toujours** la section *Known issues* de la KB et Windows release health avant de déployer.
> - Qualifier = croiser **exploitation**, **présence**, **exposition**, **criticité métier** ; pas seulement le CVSS.
> - Veille : sources officielles + CERT-FR + KEV + retours communautaires, avec une routine et une trace écrite.

---
