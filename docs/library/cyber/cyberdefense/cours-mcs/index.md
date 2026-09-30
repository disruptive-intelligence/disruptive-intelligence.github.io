---
title: Cours MCS
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
format: cours
---

*Connaître, décider, corriger, maintenir, prouver et financer la sécurité dans la durée*

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

## Sommaire

- [PARTIE I — Fondations, socle technique et maintenabilité](01-partie-i-fondations-socle-technique-et-maintenabil/index.md)
    - [Chapitre 1 — Ce qu'est réellement le MCS](01-partie-i-fondations-socle-technique-et-maintenabil/01-chapitre-1-ce-qu-est-reellement-le-mcs.md)
    - [Chapitre 2 — Socle technique 1](01-partie-i-fondations-socle-technique-et-maintenabil/02-chapitre-2-socle-technique-1.md)
    - [Chapitre 3 — Socle technique 2](01-partie-i-fondations-socle-technique-et-maintenabil/03-chapitre-3-socle-technique-2.md)
    - [Chapitre 4 — Socle vulnérabilités : identifiants, scores, écosystème](01-partie-i-fondations-socle-technique-et-maintenabil/04-chapitre-4-socle-vulnerabilites-identifiants-score.md)
    - [Chapitre 5 — Socle processus](01-partie-i-fondations-socle-technique-et-maintenabil/05-chapitre-5-socle-processus.md)
    - [Chapitre 6 — Architecture maintenable : le MCS by design](01-partie-i-fondations-socle-technique-et-maintenabil/06-chapitre-6-architecture-maintenable-le-mcs-by-desi.md)
- [PARTIE II — Cadre, périmètre et gouvernance](02-partie-ii-cadre-perimetre-et-gouvernance/index.md)
    - [Chapitre 7 — Doctrine et politique MCS](02-partie-ii-cadre-perimetre-et-gouvernance/01-chapitre-7-doctrine-et-politique-mcs.md)
    - [Chapitre 8 — Cadre réglementaire et normatif applicable](02-partie-ii-cadre-perimetre-et-gouvernance/02-chapitre-8-cadre-reglementaire-et-normatif-applica.md)
    - [Chapitre 9 — Gouvernance, rôles et comitologie](02-partie-ii-cadre-perimetre-et-gouvernance/03-chapitre-9-gouvernance-roles-et-comitologie.md)
    - [Chapitre 10 — Inventaire et cartographie](02-partie-ii-cadre-perimetre-et-gouvernance/04-chapitre-10-inventaire-et-cartographie.md)
    - [Chapitre 11 — Exposition et chemins d'attaque](02-partie-ii-cadre-perimetre-et-gouvernance/05-chapitre-11-exposition-et-chemins-d-attaque.md)
    - [Chapitre 12 — Cycle de vie, obsolescence et dette technique](02-partie-ii-cadre-perimetre-et-gouvernance/06-chapitre-12-cycle-de-vie-obsolescence-et-dette-tec.md)
    - [Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs](02-partie-ii-cadre-perimetre-et-gouvernance/07-chapitre-13-mcs-delegue-infogerance-prestataires-e.md)
- [PARTIE III — Le cœur opérationnel](03-partie-iii-le-coeur-operationnel/index.md)
    - [Chapitre 14 — Veille et sources de constats](03-partie-iii-le-coeur-operationnel/01-chapitre-14-veille-et-sources-de-constats.md)
    - [Chapitre 15 — Détection technique de l'exposition](03-partie-iii-le-coeur-operationnel/02-chapitre-15-detection-technique-de-l-exposition.md)
    - [Chapitre 16 — Triage et priorisation défendables](03-partie-iii-le-coeur-operationnel/03-chapitre-16-triage-et-priorisation-defendables.md)
    - [Chapitre 17 — Workflow de remédiation et gestion du backlog](03-partie-iii-le-coeur-operationnel/04-chapitre-17-workflow-de-remediation-et-gestion-du.md)
    - [Chapitre 18 — Le processus de correctif de bout en bout](03-partie-iii-le-coeur-operationnel/05-chapitre-18-le-processus-de-correctif-de-bout-en-b.md)
    - [Chapitre 19 — Outillage de déploiement par plateforme](03-partie-iii-le-coeur-operationnel/06-chapitre-19-outillage-de-deploiement-par-plateform.md)
    - [Chapitre 20 — Quand on ne peut pas patcher](03-partie-iii-le-coeur-operationnel/07-chapitre-20-quand-on-ne-peut-pas-patcher.md)
    - [Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j](03-partie-iii-le-coeur-operationnel/08-chapitre-21-crise-vulnerabilite-la-cinetique-24-h.md)
- [PARTIE IV — Configuration, dépendances et couches oubliées](04-partie-iv-configuration-dependances-et-couches-oub/index.md)
    - [Chapitre 22 — Durcissement et référentiels de configuration](04-partie-iv-configuration-dependances-et-couches-oub/01-chapitre-22-durcissement-et-referentiels-de-config.md)
    - [Chapitre 23 — Dérive de configuration, IaC et immutabilité](04-partie-iv-configuration-dependances-et-couches-oub/02-chapitre-23-derive-de-configuration-iac-et-immutab.md)
    - [Chapitre 24 — Identités, secrets et cryptographie](04-partie-iv-configuration-dependances-et-couches-oub/03-chapitre-24-identites-secrets-et-cryptographie.md)
    - [Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances](04-partie-iv-configuration-dependances-et-couches-oub/04-chapitre-25-mcs-des-applications-de-la-chaine-logi.md)
    - [Chapitre 26 — Bases de données, middlewares et runtimes](04-partie-iv-configuration-dependances-et-couches-oub/05-chapitre-26-bases-de-donnees-middlewares-et-runtim.md)
    - [Chapitre 27 — Couches basses et périphéries](04-partie-iv-configuration-dependances-et-couches-oub/06-chapitre-27-couches-basses-et-peripheries.md)
    - [Chapitre 28 — Environnements non productifs et actifs d'administration](04-partie-iv-configuration-dependances-et-couches-oub/07-chapitre-28-environnements-non-productifs-et-actif.md)
- [PARTIE V — Contextes spécialisés](05-partie-v-contextes-specialises/index.md)
    - [Chapitre 29 — MCS en environnement industriel (OT / ICS)](05-partie-v-contextes-specialises/01-chapitre-29-mcs-en-environnement-industriel-ot-ics.md)
    - [Chapitre 30 — MCS du cloud](05-partie-v-contextes-specialises/02-chapitre-30-mcs-du-cloud.md)
    - [Chapitre 31 — MCS des services en ligne, extensions et intégrations](05-partie-v-contextes-specialises/03-chapitre-31-mcs-des-services-en-ligne-extensions-e.md)
    - [Chapitre 32 — Systèmes contraints, legacy et sanctuarisation](05-partie-v-contextes-specialises/04-chapitre-32-systemes-contraints-legacy-et-sanctuar.md)
    - [Chapitre 33 — MCS côté produit](05-partie-v-contextes-specialises/05-chapitre-33-mcs-cote-produit.md)
    - [Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes](05-partie-v-contextes-specialises/06-chapitre-34-mcs-des-outils-de-securite-du-contenu.md)
- [PARTIE VI — Fin de vie, industrialisation et soutenabilité](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/index.md)
    - [Chapitre 35 — Décommissionnement sécurisé](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/01-chapitre-35-decommissionnement-securise.md)
    - [Chapitre 36 — Automatisation, orchestration et limites](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/02-chapitre-36-automatisation-orchestration-et-limite.md)
    - [Chapitre 37 — Économie du MCS, charge de travail et facteur humain](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/03-chapitre-37-economie-du-mcs-charge-de-travail-et-f.md)
    - [Chapitre 38 — Indicateurs, tableaux de bord et maturité](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/04-chapitre-38-indicateurs-tableaux-de-bord-et-maturi.md)
    - [Chapitre 39 — Audit, contrôle et production de preuve](06-partie-vi-fin-de-vie-industrialisation-et-soutenab/05-chapitre-39-audit-controle-et-production-de-preuve.md)
- [PARTIE VII — Mise en œuvre](07-partie-vii-mise-en-oeuvre/index.md)
    - [Chapitre 40 — Construire un programme MCS de zéro à douze mois](07-partie-vii-mise-en-oeuvre/01-chapitre-40-construire-un-programme-mcs-de-zero-a.md)
- [Cas de synthèse A — 0-day activement exploitée sur la passerelle d'accès distant](08-cas-de-synthese-a-0-day-activement-exploitee-sur-l.md)
- [Cas de synthèse B — Sortie d'obsolescence sous contrainte et préparation d'un contrôle](09-cas-de-synthese-b-sortie-d-obsolescence-sous-contr.md)
- [Cas de synthèse C — Le correctif urgent qui casse la production](10-cas-de-synthese-c-le-correctif-urgent-qui-casse-la.md)
- [ANNEXES](11-annexes/index.md)
    - [Plan d'accès — trouver la bonne annexe en dix secondes](11-annexes/01-plan-d-acces-trouver-la-bonne-annexe-en-dix-second.md)
    - [Annexe A — Glossaire](11-annexes/02-annexe-a-glossaire.md)
    - [Annexe B — Cheat sheets par plateforme](11-annexes/03-annexe-b-cheat-sheets-par-plateforme.md)
    - [Annexe D — Templates opérationnels](11-annexes/04-annexe-d-templates-operationnels.md)
    - [D.4 — Fiche de dérogation](11-annexes/05-d-4-fiche-de-derogation.md)
    - [D.9 — Clauses contractuelles MCS](11-annexes/06-d-9-clauses-contractuelles-mcs.md)
    - [D.10 — Questionnaire fournisseur](11-annexes/07-d-10-questionnaire-fournisseur.md)
    - [D.14 — Procès-verbal de décommissionnement](11-annexes/08-d-14-proces-verbal-de-decommissionnement.md)
    - [Annexe E — Familles d'outils et exemples de référence](11-annexes/09-annexe-e-familles-d-outils-et-exemples-de-referenc.md)
    - [E.2 Les familles](11-annexes/10-e-2-les-familles.md)
    - [Annexe F — Cadre réglementaire et normatif comparatif](11-annexes/11-annexe-f-cadre-reglementaire-et-normatif-comparati.md)
    - [I.1 Entité ACTIF](11-annexes/12-i-1-entite-actif.md)
    - [K.1 Fiches d'indicateurs](11-annexes/13-k-1-fiches-d-indicateurs.md)
- [Annexes](12-annexes.md)
- [Journal des modifications](13-journal-des-modifications.md)
