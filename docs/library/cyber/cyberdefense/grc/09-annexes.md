---
title: Annexes
source: Cyber/05_Cyberdefense/GRC.md
note: GRC
up:
- - GRC
  - index.md
---

---


## Annexe A — Glossaire GRC

| Terme | Définition |
|-------|-----------|
| **AIPD / DPIA** | Analyse d'Impact relative à la Protection des Données (art.35 RGPD) |
| **BIA** | Business Impact Analysis — analyse d'impact sur l'activité |
| **CASB** | Cloud Access Security Broker — contrôle des accès cloud |
| **CIS Controls** | 18 contrôles de sécurité priorisés (Center for Internet Security) |
| **CMDB** | Configuration Management Database — inventaire des actifs |
| **COMEX** | Comité Exécutif — direction générale |
| **DdA / SoA** | Déclaration d'Applicabilité / Statement of Applicability (ISO 27001) |
| **DORA** | Digital Operational Resilience Act — réglementation financière UE |
| **DPO** | Data Protection Officer — délégué à la protection des données |
| **EBIOS RM** | Expression des Besoins et Identification des Objectifs de Sécurité — Risk Manager |
| **FAIR** | Factor Analysis of Information Risk — méthode quantitative de risque |
| **HDS** | Hébergement de Données de Santé — certification française |
| **Homologation** | Décision formelle d'autoriser l'exploitation d'un SI en connaissance des risques |
| **IAM** | Identity and Access Management — gestion des identités et des accès |
| **II 901** | Instruction Interministérielle n°901 — SI sensibles / Diffusion Restreinte |
| **ISO 27001** | Standard international de certification d'un SMSI |
| **ISO 27002** | Catalogue de 93 mesures de sécurité (version 2022) |
| **ISO 27005** | Cadre générique d'analyse de risques aligné ISO 27001 |
| **KPI** | Key Performance Indicator — indicateur clé de performance |
| **MFA** | Multi-Factor Authentication — authentification multi-facteur |
| **MTTD / MTTR** | Mean Time to Detect / Mean Time to Respond |
| **NIS 2** | Network and Information Security Directive v2 (UE 2022/2555) |
| **NIST CSF** | Cybersecurity Framework du NIST (v2.0, 2024) |
| **OIV** | Opérateur d'Importance Vitale (France) |
| **PAM** | Privileged Access Management — gestion des accès privilégiés |
| **PAS** | Plan d'Assurance Sécurité — exigences de sécurité pour un prestataire |
| **PASSI** | Prestataire d'Audit de SSI Qualifié (ANSSI) |
| **PCA / PRA** | Plan de Continuité / Plan de Reprise d'Activité |
| **PDCA** | Plan-Do-Check-Act — cycle d'amélioration continue |
| **PSSI** | Politique de Sécurité des Systèmes d'Information |
| **PTR** | Plan de Traitement des Risques |
| **RACI** | Responsible, Accountable, Consulted, Informed — matrice de responsabilités |
| **RGS** | Référentiel Général de Sécurité (secteur public français) |
| **RGPD** | Règlement Général sur la Protection des Données (UE 2016/679) |
| **RPO / RTO** | Recovery Point Objective / Recovery Time Objective |
| **RSSI / CISO** | Responsable de la Sécurité des Systèmes d'Information |
| **SecNumCloud** | Qualification ANSSI pour les prestataires de cloud sécurisé |
| **Shadow IT** | Applications et services IT non référencés par la DSI |
| **SIIV** | Système d'Information d'Importance Vitale |
| **SMSI / ISMS** | Système de Management de la Sécurité de l'Information |
| **SOC 2** | Service Organization Control Type 2 — rapport d'audit de contrôles |
| **Waiver** | Exception formalisée à un contrôle de sécurité |

---


## Annexe B — Templates de livrables GRC

### Structure type PSSI (sommaire)

```
1. Contexte et périmètre
2. Engagement de la direction (signature DG)
3. Objectifs de sécurité
4. Principes directeurs
5. Organisation et responsabilités (RACI)
6. Classification des données
7. Règles par domaine
   7.1 Gestion des accès
   7.2 Sécurité réseau
   7.3 Sécurité des endpoints
   7.4 Sécurité cloud
   7.5 Protection des données
   7.6 Gestion des tiers
   7.7 Gestion des incidents
   7.8 Continuité d'activité
8. Gestion des exceptions
9. Sanctions
10. Revue et mise à jour
Annexe : glossaire, contacts, références
```


### Registre des risques (colonnes)

```
ID | Description | Actif | Menace | Vulnérabilité | Vraisemblance (1-4) | 
Impact (1-4) | Niveau | Traitement (réduire/transférer/éviter/accepter) | 
Contrôle(s) | Propriétaire | Statut | Risque résiduel | Date revue
```


### Fiche incident (structure)

```
FICHE INCIDENT #[numéro]
Sévérité : [P1/P2/P3/P4]    Date détection : [date UTC]
Détecté par : [SOC/utilisateur/tiers]

RÉSUMÉ : [2 lignes — quoi, qui, impact]
TIMELINE : [horodaté — chaque événement clé]
ACTIONS PRISES : [confinement, éradication, communication]
NOTIFICATION : [CNIL ? ANSSI ? Clients ?]
IMPACT : [données, services, financier, réglementaire]
CAUSE RACINE : [identifiée / en cours]
ACTIONS CORRECTIVES : [registre risques mis à jour ?]
RETEX : [ce qui a fonctionné / échoué / à améliorer]
```


---


## Annexe C — Evidence pack : preuves par contrôle

| Contrôle | Preuve attendue | Fréquence | Propriétaire |
|----------|----------------|-----------|-------------|
| MFA | Export IAM + config conditional access | Trimestrielle | IT / IAM |
| Patching | Rapport scan + tickets fermés + taux SLA | Mensuelle | SecOps |
| Sauvegardes | PV test restauration + RPO/RTO mesurés | Semestrielle | IT / Infra |
| Revue accès | CR signé + captures avant/après + actions | Trimestrielle | Propriétaires données |
| Sensibilisation | Attestations + résultats phishing + tendance | Annuelle + continue | RSSI / RH |
| Incidents | Fiches traitées + timeline + retex + MTTD/MTTR | Continue | SOC / RSSI |
| Changes | Tickets avec approbation + validation post-change | Continue | Change Manager |
| SIEM | Dashboard sources connectées + règles + alertes | Mensuelle | SOC |
| Scan vulnérabilités | Rapports + tendances + exceptions documentées | Mensuelle | SecOps |
| Segmentation | Schéma réseau + règles FW + tests de flux | Annuelle | Réseau |
| Classification | Registre classifié + politique appliquée | Annuelle | Propriétaires données |
| Tiers | Questionnaires + PAS + revues annuelles | Annuelle | RSSI / Achats |
| Exercice crise | CR + participants + retex + actions correctives | Annuelle | RSSI / DG |
| PSSI | Versionnée + signée + diffusée + formation | Annuelle | RSSI / DG |
| Analyse risques | Registre + PTR + CR revue direction | Annuelle + trimestrielle | RSSI |
| Homologation | Dossier complet + décision signée + suivi réserves | Selon validité (3 ans) | Autorité d'homologation |

---


## Annexe D — Top 20 contrôles à plus fort ROI

| # | Contrôle | Pourquoi prioritaire | Effort |
|---|----------|---------------------|--------|
| 1 | Inventaire actifs | On ne protège pas ce qu'on ne connaît pas | Moyen |
| 2 | MFA admin + accès distants | Bloque >90 % des compromissions de comptes | Faible |
| 3 | Patching automatisé | Vulnérabilités connues = vecteur #1 | Moyen |
| 4 | Sauvegardes 3-2-1 + immutables | Anti-ransomware | Moyen |
| 5 | EDR endpoints + serveurs | Détection et réponse | Moyen |
| 6 | Logs centralisés (SIEM) | Pas de détection sans logs | Élevé |
| 7 | Segmentation réseau | Limite le mouvement latéral | Élevé |
| 8 | Politique MdP + gestionnaire | MdP faibles = porte ouverte | Faible |
| 9 | Sensibilisation continue | Facteur humain = maillon #1 | Faible |
| 10 | Hardening AD (tiering) | AD compromis = tout compromis | Élevé |
| 11 | Plan incident + contacts | Savoir quoi faire AVANT la crise | Faible |
| 12 | Revue accès trimestrielle | Droits cumulés = risque cumulé | Moyen |
| 13 | Gestion tiers + PAS | Supply chain = surface #1 | Moyen |
| 14 | Chiffrement transit + repos | Obligation + protection | Moyen |
| 15 | Désactivation services inutiles | Réduire la surface | Faible |
| 16 | Use cases SIEM (5-10 règles) | Logs sans règles = bruit | Moyen |
| 17 | Scan vuln + SLA remédiation | Identifier avant l'attaquant | Moyen |
| 18 | Exercice crise annuel | Tester avant la vraie crise | Faible |
| 19 | Classification données | Adapter protection à sensibilité | Moyen |
| 20 | Assurance cyber | Transférer le risque financier résiduel | Moyen |

*Les 5 premiers couvrent la majorité du risque — commencer par eux crédibilise le RSSI et débloque le budget.*

---


## Annexe E — Mapping réglementaire

| Exigence | RGPD | NIS 2 | ISO 27001 | DORA | HDS |
|----------|:---:|:---:|:---:|:---:|:---:|
| Analyse de risques | Art.32 (implicite) | Art.21 | Clause 6.1 | Art.6 | Oui |
| Politique de sécurité | Art.32 | Art.21 | Clause 5.2 | Art.6 | Oui |
| Gestion des incidents | Art.33-34 | Art.23 | A.5.24-28 | Art.17 | Oui |
| Continuité / PCA | Art.32 (restauration) | Art.21 | A.5.29-30 | Art.11-12 | Oui |
| Supply chain / tiers | Art.28 (sous-traitant) | Art.21 | A.5.19-23 | Art.28-30 | Oui |
| Chiffrement | Art.32 (mesure) | Art.21 | A.8.24 | Art.6 | Oui |
| Contrôle d'accès | Art.32 (mesure) | Art.21 | A.8.1-5 | Art.6 | Oui |
| Sensibilisation | Art.39 (DPO) | Art.21 | A.6.3 | Art.13 | Oui |
| Notification incident | 72h CNIL | 24h/72h/1m ANSSI | Interne | Selon classif. | Oui |
| Responsabilité dirigeants | — | Art.20 | Clause 5.1 | Art.5 | — |
| Sanctions | 20M€ / 4% CA | 10M€ / 2% (EE) | Retrait certif. | Variables | Retrait certif. |

---


## Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Gouvernance, risques, conformité | **Ce cours (GRC)** | — |
| Threat intelligence (menaces, acteurs) | **Cours CTI** | GRC (Ch.8 EBIOS RM atelier 2 — sources de risque alimentées par la CTI) |
| Acteurs APT (profils, campagnes) | **Cours APT** | GRC (Ch.8 — les sources de risque sont les acteurs du cours APT) |
| Détection SOC (SIEM, investigation) | **Cours SOC** | GRC (Ch.9 — indicateurs SOC dans le dashboard COMEX, Ch.28 convergence) |
| Incident Response (technique) | **Cours IR** | GRC (Ch.20 gestion incidents vue GRC, Ch.22 gestion de crise) |
| Forensic numérique | **Cours Forensic** | GRC (Ch.20 — préservation des preuves) |
| Intelligence économique | **Cours IE** | GRC (Ch.19 sécurité contractuelle, Ch.24 tiers) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | GRC (Ch.8 — scénarios ransomware dans l'EBIOS RM) |
| OSINT | **Cours OSINT** | GRC (Ch.17 — sensibilisation, social engineering) |
| Windows / AD | **Cours Windows / AD** | GRC (Ch.16 IAM, Ch.18 patching) |

---


## Annexe G — Ressources et formation

### Certifications

| Certification | Organisme | Focus | Niveau |
|--------------|-----------|-------|--------|
| ISO 27001 Lead Implementer | PECB / BSI | Mettre en place un SMSI | Intermédiaire |
| ISO 27001 Lead Auditor | PECB / BSI | Auditer un SMSI | Intermédiaire |
| CISSP | (ISC)² | Sécurité globale (8 domaines) | Avancé |
| CISM | ISACA | Management de la sécurité | Avancé |
| CRISC | ISACA | Gestion des risques IT | Avancé |
| CISA | ISACA | Audit des SI | Avancé |
| EBIOS RM | ANSSI / Club EBIOS | Analyse de risques | Intermédiaire |
| DPO / RGPD | CNIL / organismes agréés | Protection des données | Intermédiaire |
| CompTIA Security+ | CompTIA | Fondamentaux sécurité | Débutant |

### Organismes et ressources

| Organisme | Ressource | URL |
|-----------|----------|-----|
| **ANSSI** | Guides, EBIOS RM, hygiène, SecNumCloud, PASSI | cyber.gouv.fr |
| **CNIL** | Guides RGPD, AIPD, registre, outils PIA | cnil.fr |
| **ENISA** | Guides NIS 2, threat landscape, bonnes pratiques | enisa.europa.eu |
| **NIST** | CSF v2.0, SP 800-53, SP 800-61, FAIR | nist.gov |
| **ISO** | 27001, 27002, 27005, 22301 | iso.org |
| **CIS** | CIS Controls v8, CIS Benchmarks | cisecurity.org |
| **MITRE** | ATT&CK, D3FEND | attack.mitre.org |
| **Club EBIOS** | Communauté EBIOS RM, retours d'expérience | club-ebios.org |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former au pilotage de la sécurité par la gouvernance, le risque, et la conformité — le cadre qui donne sens à la technique et qui permet au RSSI de parler le langage de la direction.
>
> L'opération COMPLIANCE illustre cette ambition : Marine ne déploie pas des outils — elle construit un programme. Elle ne coche pas des cases — elle réduit des risques. Elle ne rédige pas des documents — elle produit des décisions. La PSSI n'est pas un fichier Word — c'est un engagement signé par le DG. L'analyse de risques n'est pas un exercice académique — c'est l'outil qui débloque le budget. L'homologation n'est pas un tampon — c'est la décision formelle d'accepter de vivre avec les risques résiduels.
>
> Le cours assume trois convictions. Première : la conformité sans sécurité est un leurre — cocher les cases d'un référentiel ne protège pas. Deuxième : la sécurité sans gouvernance est fragile — les contrôles techniques sans politique, sans budget, et sans arbitrage se dégradent. Troisième : le risque sans décision formelle est de la négligence — accepter un risque est un acte de management, pas un oubli.
>
> *Gouverner • Évaluer • Se conformer • Protéger • Décider — avec rigueur et pragmatisme.*
