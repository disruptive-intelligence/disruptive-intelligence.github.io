---
title: Réponse à incident
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
---

*Préparer • Détecter • Qualifier • Investiguer • Contenir • Éradiquer • Restaurer • Capitaliser*

**Cours complet — 40 chapitres • 8 parties • 7 annexes**

*Méthodologie, investigation, coordination, crise et amélioration continue*

---

### Fil rouge : Opération BLACKTIDE

> **Contexte narratif — ce fil rouge traverse les 38 premiers chapitres du cours.**
>
> **Vendredi 14 mars 2026, 22h17.** Le SOC d'**Arvantis**, groupe industriel français coté au SBF 120 (12 000 collaborateurs, 15 sites de production en Europe, activité chimie fine et matériaux spéciaux, classé OIV sur 2 sites dont le complexe pétrochimique de Fos-sur-Mer), détecte une alerte EDR sur le contrôleur de domaine DC01 : exécution suspecte de `PsExec` couplée à une tentative de désactivation de Windows Defender via modification de GPO.
>
> L'analyste SOC N2 de garde, **Karim Belkacem**, vérifie l'alerte, confirme qu'il ne s'agit pas d'une opération d'administration planifiée, et escalade immédiatement vers l'IR lead.
>
> L'investigation va progressivement révéler une compromission profonde : un infostealer (variant Lumma) déployé 5 semaines plus tôt via un phishing ciblé sur le sous-traitant RH GestPaie, une élévation de privilèges via Kerberoasting sur un compte de service avec droits Domain Admin, un mouvement latéral méthodique via PsExec et RDP, une exfiltration de 380 Go de données R&D vers une instance AWS EC2 louée avec une carte prépayée, et le déploiement en cours d'un ransomware PhantomCrypt (connexion directe avec le cours *Cartographie des Écosystèmes Cybercriminels*) via GPO malveillante. Le chiffrement est partiellement contenu mais 3 sites sur 15 sont impactés, dont le site OIV de Fos-sur-Mer.
>
> L'équipe IR d'Arvantis, menée par **Nadia Moreau** (IR lead), sera confrontée à chaque chapitre à des décisions concrètes sous pression : quand couper le réseau et quand ne PAS le couper, comment préserver les preuves quand un admin a déjà redémarré 2 serveurs, quoi dire au CEO qui veut « redémarrer les usines lundi », comment articuler avec l'ANSSI et le CERT-FR, comment traiter la demande de rançon de 4,2 M€, comment reconstruire un AD dont le compte krbtgt est compromis, et comment s'assurer que l'attaquant n'est plus là avant de relancer la production chimique.
>
> Le coût total de l'incident sera estimé à 8,5 M€. Le retex final (Ch.38) produira 15 recommandations structurées et un plan d'amélioration sur 18 mois.

---

## Sommaire

- [Partie I — Fondations : comprendre la réponse à incident](01-partie-i-fondations-comprendre-la-reponse-a-incide/index.md)
    - [Chapitre 1 — Qu'est-ce qu'un incident de sécurité](01-partie-i-fondations-comprendre-la-reponse-a-incide/01-chapitre-1-qu-est-ce-qu-un-incident-de-securite.md)
    - [Chapitre 2 — L'Incident Response comme discipline d'orchestration](01-partie-i-fondations-comprendre-la-reponse-a-incide/02-chapitre-2-l-incident-response-comme-discipline-d.md)
    - [Chapitre 3 — Incident technique, incident majeur, crise cyber : les seuils de bascule](01-partie-i-fondations-comprendre-la-reponse-a-incide/03-chapitre-3-incident-technique-incident-majeur-cris.md)
    - [Chapitre 4 — Référentiels, modèles et cadres méthodologiques](01-partie-i-fondations-comprendre-la-reponse-a-incide/04-chapitre-4-referentiels-modeles-et-cadres-methodol.md)
- [Partie II — Préparation : AVANT que L'incident n'arrive](02-partie-ii-preparation-avant-que-l-incident-n-arriv/index.md)
    - [Chapitre 5 — Pourquoi la préparation détermine tout](02-partie-ii-preparation-avant-que-l-incident-n-arriv/01-chapitre-5-pourquoi-la-preparation-determine-tout.md)
    - [Chapitre 6 — Gouvernance et organisation IR](02-partie-ii-preparation-avant-que-l-incident-n-arriv/02-chapitre-6-gouvernance-et-organisation-ir.md)
    - [Chapitre 7 — Playbooks et procédures opérationnelles](02-partie-ii-preparation-avant-que-l-incident-n-arriv/03-chapitre-7-playbooks-et-procedures-operationnelles.md)
    - [Chapitre 8 — Préparation technique : outillage et télémétrie](02-partie-ii-preparation-avant-que-l-incident-n-arriv/04-chapitre-8-preparation-technique-outillage-et-tele.md)
    - [Chapitre 9 — Préparation juridique, réglementaire et contractuelle](02-partie-ii-preparation-avant-que-l-incident-n-arriv/05-chapitre-9-preparation-juridique-reglementaire-et.md)
    - [Chapitre 10 — Exercices et entraînement](02-partie-ii-preparation-avant-que-l-incident-n-arriv/06-chapitre-10-exercices-et-entrainement.md)
- [Partie III — Détection, qualification ET triage](03-partie-iii-detection-qualification-et-triage/index.md)
    - [Chapitre 11 — Du signal faible à l'incident confirmé](03-partie-iii-detection-qualification-et-triage/01-chapitre-11-du-signal-faible-a-l-incident-confirme.md)
    - [Chapitre 12 — Triage initial et premières mesures conservatoires](03-partie-iii-detection-qualification-et-triage/02-chapitre-12-triage-initial-et-premieres-mesures-co.md)
    - [Chapitre 13 — Qualification, catégorisation et évaluation de gravité](03-partie-iii-detection-qualification-et-triage/03-chapitre-13-qualification-categorisation-et-evalua.md)
    - [Chapitre 14 — Scoping initial](03-partie-iii-detection-qualification-et-triage/04-chapitre-14-scoping-initial.md)
    - [Chapitre 15 — Déclenchement formel et premières notifications](03-partie-iii-detection-qualification-et-triage/05-chapitre-15-declenchement-formel-et-premieres-noti.md)
- [Partie IV — Investigation ET analyse](04-partie-iv-investigation-et-analyse/index.md)
    - [Chapitre 16 — Principes de l'investigation IR](04-partie-iv-investigation-et-analyse/01-chapitre-16-principes-de-l-investigation-ir.md)
    - [Chapitre 17 — Construction de la timeline d'attaque](04-partie-iv-investigation-et-analyse/02-chapitre-17-construction-de-la-timeline-d-attaque.md)
    - [Chapitre 18 — Cartographie des sources de données](04-partie-iv-investigation-et-analyse/03-chapitre-18-cartographie-des-sources-de-donnees.md)
    - [Chapitre 19 — Investigation endpoint : collecte et analyse concrète](04-partie-iv-investigation-et-analyse/04-chapitre-19-investigation-endpoint-collecte-et-ana.md)
    - [Chapitre 20 — Investigation identité et Active Directory](04-partie-iv-investigation-et-analyse/05-chapitre-20-investigation-identite-et-active-direc.md)
    - [Chapitre 21 — Investigation réseau et exfiltration](04-partie-iv-investigation-et-analyse/06-chapitre-21-investigation-reseau-et-exfiltration.md)
    - [Chapitre 22 — Investigation des environnements hybrides, OT et dépendances tierces](04-partie-iv-investigation-et-analyse/07-chapitre-22-investigation-des-environnements-hybri.md)
- [Partie V — Confinement, décision ET préservation de preuve](05-partie-v-confinement-decision-et-preservation-de-p/index.md)
    - [Chapitre 23 — Stratégies de confinement et arbitrages](05-partie-v-confinement-decision-et-preservation-de-p/01-chapitre-23-strategies-de-confinement-et-arbitrage.md)
    - [Chapitre 24 — Confinement par type d'incident](05-partie-v-confinement-decision-et-preservation-de-p/02-chapitre-24-confinement-par-type-d-incident.md)
    - [Chapitre 25 — Préserver les preuves sous pression](05-partie-v-confinement-decision-et-preservation-de-p/03-chapitre-25-preserver-les-preuves-sous-pression.md)
    - [Chapitre 26 — Décider sous incertitude](05-partie-v-confinement-decision-et-preservation-de-p/04-chapitre-26-decider-sous-incertitude.md)
- [Partie VI — Éradication, reconstruction ET reprise](06-partie-vi-eradication-reconstruction-et-reprise/index.md)
    - [Chapitre 27 — Plan d'éradication coordonné](06-partie-vi-eradication-reconstruction-et-reprise/01-chapitre-27-plan-d-eradication-coordonne.md)
    - [Chapitre 28 — Reconstruction des systèmes](06-partie-vi-eradication-reconstruction-et-reprise/02-chapitre-28-reconstruction-des-systemes.md)
    - [Chapitre 29 — Validation d'éradication et surveillance post-nettoyage](06-partie-vi-eradication-reconstruction-et-reprise/03-chapitre-29-validation-d-eradication-et-surveillan.md)
    - [Chapitre 30 — Reprise d'activité](06-partie-vi-eradication-reconstruction-et-reprise/04-chapitre-30-reprise-d-activite.md)
    - [Chapitre 31 — Durcissement post-incident](06-partie-vi-eradication-reconstruction-et-reprise/05-chapitre-31-durcissement-post-incident.md)
    - [Chapitre 32 — Extorsion, rançon et arbitrages stratégiques](06-partie-vi-eradication-reconstruction-et-reprise/06-chapitre-32-extorsion-rancon-et-arbitrages-strateg.md)
- [Partie VII — Gestion de crise, communication ET coordination](07-partie-vii-gestion-de-crise-communication-et-coord.md)
- [Partie VIII — Post-incident, maturité ET capitalisation](08-partie-viii-post-incident-maturite-et-capitalisati/index.md)
    - [Chapitre 38 — Clôture de l'incident et retour d'expérience (RETEX)](08-partie-viii-post-incident-maturite-et-capitalisati/01-chapitre-38-cloture-de-l-incident-et-retour-d-expe.md)
    - [Chapitre 39 — Métriques, maturité et programme IR durable](08-partie-viii-post-incident-maturite-et-capitalisati/02-chapitre-39-metriques-maturite-et-programme-ir-dur.md)
    - [Chapitre 40 — Scénarios d'incident : atelier de synthèse](08-partie-viii-post-incident-maturite-et-capitalisati/03-chapitre-40-scenarios-d-incident-atelier-de-synthe.md)
- [Annexes](09-annexes/index.md)
    - [Annexe A — Glossaire](09-annexes/01-annexe-a-glossaire.md)
    - [Annexe B — Checklists opérationnelles](09-annexes/02-annexe-b-checklists-operationnelles.md)
    - [Annexe C — Templates de documents IR](09-annexes/03-annexe-c-templates-de-documents-ir.md)
    - [Annexe D — Cheat sheets techniques](09-annexes/04-annexe-d-cheat-sheets-techniques.md)
    - [Annexe E — Playbooks types détaillés](09-annexes/05-annexe-e-playbooks-types-detailles.md)
    - [Annexe F — Tableau d'outils de référence IR](09-annexes/06-annexe-f-tableau-d-outils-de-reference-ir.md)
    - [Annexe G — Grilles d'évaluation et RACI](09-annexes/07-annexe-g-grilles-d-evaluation-et-raci.md)
- [Questions essentielles](10-questions-essentielles.md)
- [Questions complémentaires](11-questions-complementaires.md)
- [Réponses flash](12-reponses-flash.md)
