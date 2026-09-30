---
title: Partie II — Gestion des risques
source: Cyber/05_Cyberdefense/GRC.md
note: GRC
up:
- - GRC
  - index.md
---

*Prioriser ce qui compte vraiment — l'analyse de risques est l'outil de décision du RSSI.*

---


## Chapitre 6 — Concepts fondamentaux du risque

### 6.1 Vocabulaire

Un **actif** est ce qu'on protège (base de données patients, plateforme SaaS, brevet). Une **menace** est ce qui peut arriver (ransomware, employé malveillant, compromission d'un sous-traitant). Une **vulnérabilité** est la faiblesse exploitable (patch manquant, MFA absent, segmentation inexistante). Un **risque** est la combinaison vraisemblance × impact (une fuite de données via l'exploitation d'une vulnérabilité connue non patchée).

Le **risque inhérent** est le risque avant application des contrôles (risque brut). Le **risque résiduel** est le risque après application des contrôles (ce qui reste — et qui doit être formellement accepté par la direction). L'**appétence au risque** (risk appetite) est le niveau de risque que l'organisation est prête à accepter — défini par la direction, pas par le RSSI.

### 6.2 La formule et la matrice

Risque = Vraisemblance × Impact. L'évaluation peut être **qualitative** (échelles 1-4 : faible/modéré/élevé/critique — la plus courante) ou **quantitative** (en euros via FAIR — la plus convaincante devant le COMEX). La matrice heat map croise les deux axes et visualise les risques en couleurs : rouge (critique — traitement immédiat), orange (élevé — dans les 6 mois), jaune (modéré — surveillance), vert (faible — acceptation possible).

### 6.3 Traitement du risque

4 options : **réduire** (mettre un contrôle — déployer le MFA), **transférer** (assurance cyber, sous-traitance à un prestataire certifié), **éviter** (supprimer l'activité — ne pas stocker les données de carte bancaire), **accepter** (décision documentée et signée par la direction — pas un oubli). L'acceptation est la décision la plus importante : un risque accepté n'est pas un risque ignoré — c'est un risque évalué, dont le coût du traitement a été pesé, et dont la direction a décidé, par écrit avec signature, de ne pas traiter.

### 6.4 Le registre des risques

Document vivant, revu trimestriellement minimum : description du risque, vraisemblance (1-4), impact (1-4), niveau (calcul), option de traitement retenue, contrôle(s) associé(s), propriétaire du risque (un membre de la direction, pas le RSSI), statut (ouvert, en traitement, accepté, clos), risque résiduel, et date de prochaine revue.

---


## Chapitre 7 — Méthodologies d'analyse de risques

### 7.1 EBIOS RM — la méthode française

EBIOS RM (Expression des Besoins et Identification des Objectifs de Sécurité — Risk Manager), développée par l'ANSSI, est structurée en 5 ateliers. Sa force : l'approche par les menaces réelles (les sources de risque sont des attaquants concrets — un groupe APT, un affilié ransomware, un insider — pas des catégories abstraites). Les scénarios produits sont exploitables par le SOC et les équipes techniques.

**Atelier 1 — Cadrage et socle :** définir le périmètre (quel système, quelles données, quelles parties prenantes), les valeurs métier (ce qui a de la valeur pour l'organisation — disponibilité du service, confidentialité des données, intégrité des prescriptions), les événements redoutés (ce qu'on ne veut PAS qu'il se passe), et le socle de sécurité existant (les contrôles déjà en place). **Atelier 2 — Sources de risque :** identifier les attaquants plausibles (qui pourrait attaquer, pourquoi, avec quels moyens) — ici la CTI est le fournisseur d'intelligence (cours CTI de la bibliothèque). Chaque couple source/objectif est évalué en pertinence et en potentiel. **Atelier 3 — Scénarios stratégiques :** construire les chemins d'attaque à haut niveau (l'attaquant X cible la valeur Y via le vecteur Z en exploitant la partie prenante W). **Atelier 4 — Scénarios opérationnels :** décliner en technique (quels systèmes, quelles vulnérabilités, quels artefacts) et évaluer la vraisemblance. **Atelier 5 — Traitement :** définir les mesures pour chaque scénario (contrôle, responsable, échéance, coût) et évaluer le risque résiduel.

### 7.2 ISO 27005 et FAIR

**ISO 27005** est le cadre générique d'analyse de risques aligné sur ISO 27001 : contexte → identification → analyse → évaluation → traitement → acceptation → communication → surveillance. Plus flexible qu'EBIOS RM, moins prescriptif — il dit « faites une analyse de risques » mais ne dit pas exactement comment.

**FAIR** (Factor Analysis of Information Risk) est la méthode quantitative : elle exprime le risque en euros/dollars, pas en couleurs. Parfaite pour justifier un budget devant le COMEX (« ce risque coûte entre 500 K€ et 2 M€ en espérance de perte annuelle, le contrôle coûte 80 K€ »). Plus complexe à mettre en œuvre, nécessite des données de calibrage.

En pratique, beaucoup combinent : ISO 27005 pour le cadre global + EBIOS RM pour les scénarios concrets + FAIR pour quantifier les risques critiques devant le COMEX.

---


## Chapitre 8 — Analyse de risques en pratique

walkthrough EBIOS RM complet

*Ce chapitre est un walkthrough concret appliqué au fil rouge — pas une description de méthode mais un exercice complet avec des résultats réels.*

**Atelier 1 — Cadrage Néoforma :** périmètre = plateforme SaaS santé (application web, API, bases de données patients, infrastructure cloud Azure + datacenter Nantes). Valeurs métier identifiées avec les métiers : V1 — disponibilité du service SaaS (impact direct sur le CA — 200 hôpitaux dépendent de Néoforma pour la gestion quotidienne des patients), V2 — confidentialité des données de santé (3 millions de dossiers patients — obligation RGPD art.9, risque de sanction CNIL + perte de confiance clients), V3 — intégrité des prescriptions médicales (une modification non autorisée des prescriptions a un impact potentiel sur la sécurité des patients). Événements redoutés : ER1 — indisponibilité prolongée de la plateforme (>4h), ER2 — fuite de données patients, ER3 — modification non autorisée de données médicales. Socle existant évalué via CIS Controls IG1 : 40 % couvert (firewall, antivirus, sauvegardes non testées, pas de MFA, pas d'EDR, pas de segmentation).

**Atelier 2 — Sources de risque :** SR1 — affilié ransomware ciblant le secteur santé (motivation : profit financier, capacité : élevée, vraisemblance : élevée — le secteur santé est le 3ème secteur le plus ciblé par les ransomwares en Europe). SR2 — acteur APT ciblant les données de santé (motivation : espionnage étatique ou économique, capacité : élevée, vraisemblance : modérée). SR3 — insider négligent (motivation : erreur, capacité : accès légitime, vraisemblance : élevée). SR4 — prestataire compromis (motivation : supply chain, capacité : variable, vraisemblance : modérée — 3 sous-traitants critiques dont l'hébergeur non certifié).

**Atelier 3 — Scénarios stratégiques :** SS1 — un affilié ransomware compromet la plateforme SaaS via un phishing sur un admin, chiffre les bases de données patients, et demande 500 K€ de rançon → indisponibilité pour 200 hôpitaux + double extorsion (fuite des données). SS2 — un attaquant exploite une vulnérabilité sur le portail web, accède aux données patients, et les exfiltre → notification CNIL de 3 millions de personnes. SS3 — l'hébergeur non certifié est compromis, les backups sont accessibles, les données patients sont exfiltrées.

**Atelier 4 — Scénarios opérationnels :** déclinaison technique de SS1 : phishing ciblé sur un admin IT → vol de credentials → accès VPN → escalade de privilèges (pas de PAM, comptes admin partagés) → mouvement latéral vers les serveurs de base de données → chiffrement + exfiltration via rclone. Logs nécessaires : email gateway, proxy, AD auth, Sysmon, EDR. Contrôles existants : antivirus (insuffisant). Gaps identifiés : pas de MFA, pas d'EDR, pas de segmentation, pas de monitoring, comptes admin partagés.

**Atelier 5 — Traitement :** pour SS1 : déployer MFA sur tous les accès admin (P0, M1, 15 K€), déployer EDR (P0, M2, 40 K€/an), segmenter le réseau (P1, M6, 30 K€), mettre en place le PAM (P1, M6, 25 K€), sauvegardes immutables et testées (P0, M2, 20 K€/an), plan de réponse incident (P0, M3, 10 K€). Risque résiduel post-traitement : modéré (réduit de critique à modéré).

> **📊 COMPLIANCE — Épisode 3**
>
> Marine présente le rapport EBIOS RM au COMEX avec la matrice heat map : 3 risques critiques (SS1, SS2, SS3), 2 risques élevés, 4 risques modérés. Le PTR chiffré montre que 160 K€ d'investissement immédiat réduisent les 3 risques critiques à modérés. Le DG signe le PTR et l'acceptation formelle des risques résiduels. Le budget est débloqué.

---


## Chapitre 9 — Indicateurs, tableaux de bord et amélioration continue

### 9.1 Les KPIs sécurité

**Indicateurs opérationnels** (pour le RSSI et l'équipe sécurité, fréquence hebdomadaire) : nombre d'incidents par sévérité, MTTD (temps moyen de détection), MTTR (temps moyen de réponse), taux de patching par criticité (critique < 48h, élevé < 15 jours), nombre de vulnérabilités critiques ouvertes et tendance, couverture EDR (% des endpoints protégés), et backlog d'alertes SOC.

**Indicateurs de conformité** (pour les auditeurs et le suivi interne, fréquence mensuelle) : % de contrôles ISO 27001 implémentés (sur les 78 applicables de la DdA), avancement du PTR (% des actions complétées), nombre de non-conformités ouvertes, échéances des exceptions, et état de la certification.

**Indicateurs humains** (pour la sensibilisation, fréquence continue) : taux de clic phishing simulé (par département et dans le temps), taux de signalement des emails suspects (les utilisateurs qui reportent — aussi important que ceux qui ne cliquent pas), complétion des formations obligatoires, et nombre d'incidents signalés par les utilisateurs.

### 9.2 Les 3 dashboards

Le **dashboard opérationnel** (audience : RSSI et équipe sécurité, fréquence : hebdomadaire) contient les KPIs détaillés, les incidents en cours, les vulnérabilités, le patching, et les alertes. Le **dashboard stratégique** (audience : COMEX, fréquence : trimestriel) contient 3-5 indicateurs clés avec tendances, les risques majeurs en termes business, le budget consommé vs prévu, et les décisions demandées. Règle d'or : pas de jargon — couleurs, scénarios, impact business. Le **dashboard conformité** (audience : auditeurs et régulateurs, fréquence : avant audit) contient le % de contrôles implémentés, les écarts, l'avancement du PTR, et les preuves disponibles.

---
