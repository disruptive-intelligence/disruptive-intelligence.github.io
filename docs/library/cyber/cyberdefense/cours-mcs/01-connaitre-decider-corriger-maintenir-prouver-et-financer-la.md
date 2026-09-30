---
title: Connaître, décider, corriger, maintenir, prouver et financer la sécurité dans la durée
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 1
chapters: 10
---

**Document intégral — 7 parties, 40 chapitres, 3 cas de synthèse, 12 annexes**
*Version 1.1 · données vérifiées au 30 juillet 2026*

---


## En-tête de maintenance

| Champ | Valeur |
|---|---|
| **Version du document** | 1.1 |
| **Dernière vérification factuelle** | 30 juillet 2026 |
| **Prochaine revue recommandée** | 31 janvier 2027, ou à la survenue d'un déclencheur ci-dessous |
| **Déclencheurs de revue anticipée** | Promulgation du texte français de transposition de NIS2 · publication d'une version définitive du ReCyF · nouvelle version majeure d'un modèle de score (EPSS, CVSS) · évolution du fonctionnement ou du financement des bases publiques de vulnérabilités · modification d'un calendrier de support étendu majeur · échéances CRA du 11/09/2026 et du 11/12/2027 |
| **Sources officielles surveillées** | cyber.gouv.fr et CERT-FR · digital-strategy.ec.europa.eu · enisa.europa.eu · legifrance.gouv.fr et dossiers législatifs · nvd.nist.gov · cve.org · first.org/epss · cisa.gov · learn.microsoft.com/lifecycle · pages de cycle de vie des éditeurs cités |
| **Sections périssables** *(à réviser en priorité)* | §4.9 · chapitre 8 (intégralité) · §12.4-12.5 · chapitre 19 · chapitre 30 · §33.5-33.7 · annexes B, E, F et H |
| **Noyau durable** *(révision rare)* | Chapitres 1-3, 5-7, 9-11, 13-18, 20-29, 31-32, 34-40 et cas de synthèse |
| **Journal des modifications** | En fin de document |

> **Règle de lecture.** Tout fait externe et périssable — calendrier réglementaire, version courante, état d'un programme de support, tarification — figure dans un bloc ⏱ **ÉTAT DE L'ART** daté et sourcé, ou dans une annexe versionnée. Les dates du cas fil rouge sont fictives. Le reste du texte est écrit pour rester valable au-delà de ces échéances.

---


## Matrice de parcours par profil

Le document dépasse les cent mille mots : cette matrice le rend navigable. Elle indique les chapitres à lire **en profondeur** ; le reste reste utile en survol.

| Profil | Parcours prioritaire |
|---|---|
| Débutant technique | 1-5, 7, 9-10, 14-21, 38-40 + cas A |
| Administrateur systèmes / sysops | 1-28, 34-40 + cas A et C |
| Responsable exploitation / production | 1-21, 26-28, 34-40 + les trois cas |
| RSSI | 1, 4-17, 20-21, 30-40 + les trois cas |
| Responsable OT / automatismes | 1-21, 27-29, 32, 34-40 + cas B |
| DevSecOps / responsable produit | 1-6, 11, 14-21, 23-26, 28, 30, 33-40 + cas C |
| Auditeur / consultant conformité | 1, 5, 7-17, 20, 35, 38-40 + cas B |
| Contexte PME (< 200 actifs) | Parcours socle + chapitre 40 et variantes PME des cas |

**Niveau visé** : débutant technique vers intermédiaire avancé. Aucun prérequis en gestion des vulnérabilités ni en conformité ; une culture informatique générale est recommandée. La Partie I rend autonome sur le MCS — elle ne remplace pas un cours de systèmes, de réseau, de cloud ou de développement, et le dit explicitement (§2.10).

**Fil rouge** : le cas HELIOMED court d'octobre 2025 à janvier 2029, à raison d'un épisode par chapitre. Tout y est fictif ; rien n'y est irréaliste.

---

### Comment lire les blocs de ce cours

| Bloc | Signification |
|---|---|
| 🖼 **SCHÉMA** | Emplacement d'un visuel à produire en mise en page. Le texte reste autonome sans lui |
| 🏢 **VU EN RÉUNION** | Situation réelle typique, en quelques lignes. Illustre un mécanisme, ne remplace pas son explication |
| 🔴 **FIL ROUGE** | Épisode du cas fil rouge HELIOMED, daté, avec une décision et un livrable |
| 🧪 **EN PRATIQUE** | Commande, procédure, workflow ou extrait de configuration réutilisable |
| ⚠️ **PIÈGE** | Erreur fréquente, faux sentiment de sécurité, faux positif classique |
| 📌 **LIMITES** | Ce qui ne fonctionne pas, ce qui n'est pas couvert, coût réel |
| ✅ **BONNE PRATIQUE** | Recommandation priorisée P0 (vital) / P1 (important) / P2 (confort) |
| ⚖️ **CADRE** | Obligation réglementaire, contractuelle ou normative |
| ⏱ **ÉTAT DE L'ART** | Donnée datée, avec sa source et sa date de vérification. **Périssable.** |

**Règle éditoriale.** Tout **fait externe et périssable** — calendrier réglementaire, version courante d'un produit, état d'un programme de support, tarification, politique d'un éditeur — est placé dans un bloc ⏱ ou dans une annexe versionnée, avec sa source et sa date de vérification. En revanche, les dates du cas fil rouge (fictives), les numéros de version utilisés comme exemples de mécanisme et les repères historiques durables figurent normalement dans le corps du texte.
Si vous relisez ce document dans deux ans : les blocs ⏱ et les annexes versionnées sont à réviser, le reste est écrit pour rester valable.

---
