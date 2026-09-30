---
title: Chapitre 30 — Le métier d'expert en social engineering
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie VII — Synthèse ET cas pratiques
  - index.md
---

## 30.1 Les métiers

Le social engineering professionnel couvre plusieurs métiers distincts.

**Red teamer SE / pentester spécialisé.** Exécution de tests d'intrusion social engineering (phishing, vishing, intrusion physique, élicitation) pour des organisations clientes. Travail en cabinet de conseil en cybersécurité ou en équipe interne de sécurité offensive.

**Consultant en sensibilisation.** Conception et délivrance de programmes de formation adaptés aux profils de risque. Développement de simulations réalistes (campagnes de phishing, exercices de vishing, tabletop exercises).

**Analyste en contre-ingénierie sociale.** Détection et analyse des tentatives de social engineering ciblant l'organisation. Veille sur les menaces, coordination avec les services de renseignement (DGSI pour l'ingérence étrangère), investigation sur les incidents.

**Formateur.** Enseignement des techniques de social engineering et de contre-ingénierie sociale dans un contexte académique ou professionnel.

**Enquêteur spécialisé.** Investigation post-incident, analyse forensique de campagnes de phishing, expertise judiciaire.

## 30.2 Les compétences

Le profil du praticien en social engineering est par nature transversal : psychologie appliquée (compréhension des biais, des leviers d'influence, des dynamiques interpersonnelles), communication (aisance orale, capacité d'adaptation, gestion du stress en situation d'imposture), OSINT (maîtrise des techniques de reconnaissance en sources ouvertes), technique (compréhension des systèmes email, des protocoles d'authentification, des technologies de contrôle d'accès, des outils d'infrastructure), rédaction (capacité à produire des rapports clairs, factuels et actionnables), et éthique (discernement, intégrité, capacité à tracer et respecter des limites).

## 30.3 Les certifications

Plusieurs certifications couvrent le social engineering, avec des niveaux de profondeur variables.

**SANS SEC567 — Social Engineering for Penetration Testers.** La formation de référence pour le red team social engineering (phishing, vishing, impersonation, pretexting). Coûteuse (formation SANS) mais reconnue.

**OSCP (Offensive Security Certified Professional).** L'OSCP couvre le pentesting global avec un volet social engineering limité — c'est une certification de pentesting technique plus que de social engineering.

**GPEN (GIAC Penetration Tester).** Couvre le pentesting incluant les aspects de social engineering dans une perspective globale.

**Certified Social Engineer (Social-Engineer.org).** Certification spécialisée en social engineering développée par Christopher Hadnagy. Pertinente mais moins largement reconnue que les certifications SANS/GIAC.

L'état du marché des certifications SE en 2025 est en évolution : la demande de compétences en social engineering augmente, mais les certifications spécialisées restent rares comparées aux certifications de pentesting technique. L'expérience pratique (campagnes réelles, rapports de red team, portfolio de missions) reste le critère de différenciation principal pour les recruteurs.

## 30.4 L'éthique comme compétence fondamentale

Le praticien de social engineering possède un savoir-faire de manipulation interpersonnelle. Cette compétence confère un pouvoir — et la responsabilité qui l'accompagne est non négociable. L'éthique n'est pas une contrainte externe imposée au praticien : c'est une compétence interne qui guide chaque décision opérationnelle.

Les questions éthiques récurrentes incluent : jusqu'où aller dans la manipulation pendant un test autorisé ? Comment gérer la découverte de vulnérabilités personnelles d'un employé (addiction, problèmes financiers) pendant la reconnaissance ? Comment rédiger un rapport qui améliore les défenses sans humilier les individus ? Comment gérer la pression d'un commanditaire qui demande des résultats individuels nominatifs pour sanctionner des employés ?

La réponse à ces questions n'est pas dans un code de conduite abstrait — elle est dans le discernement professionnel du praticien, formé par l'expérience, la réflexion et le dialogue avec ses pairs.

## 30.5 Perspectives de carrière

La demande de compétences en social engineering est en croissance structurelle. Les entreprises réalisent que la technologie seule ne suffit pas à protéger contre une menace qui exploite le facteur humain. Les réglementations (NIS2, DORA pour le secteur financier) renforcent les obligations de test de résilience, y compris les tests de social engineering. La menace IA (deepfakes, phishing personnalisé) renforce le besoin de praticiens capables de tester et de former.

Les trajectoires de carrière incluent : le consulting (missions de red team SE pour des clients variés), le poste en interne (responsable de la sensibilisation, responsable du red team interne, analyste en contre-ingérence), le management (direction d'un service de sécurité offensive, RSSI avec une spécialité en facteur humain), et la formation/recherche (enseignement, publication, conférences — DEF CON SE Village, Black Hat, les conférences SANS).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode final**
>
> **Le rapport.** Après 6 semaines de test, Nathan livre son rapport à Marc Tessier (DG) et Lucie Ferraro (RSSI) lors d'une restitution de 2 heures en comité restreint.
>
> **Résultats :**
> - **Phishing** : taux de clic 28,3 % (34/120), 18 identifiants collectés dont 2 comptes admin
> - **Vishing** : 4 tentatives d'appel au helpdesk pour reset de credentials — 2 réussies (50 %), dont 1 reset MFA sur un compte à privilèges
> - **Intrusion physique** : réussie sur 2 sites sur 3 (Bordeaux et Paris — échec à Toulouse où le gardien a refusé l'accès et appelé le responsable sécurité)
> - **Élicitation** : 4 réussites sur 6 tentatives en contexte informel (cantine, fumoir, café)
> - **Implant réseau** : déployé à Bordeaux, actif 72h avant détection par l'équipe réseau (alerte sur un nouveau device inconnu)
> - **Taux de signalement** : 2,5 % (3 emails signalés au SOC sur 120 envoyés)
>
> **Impact potentiel si exploitation réelle :** les 2 comptes admin compromis auraient permis l'accès au tenant Azure AD, à l'ensemble des emails (Exchange Online), aux fichiers SharePoint (dont les documents du programme de défense) et au VPN. L'implant réseau aurait permis l'exfiltration de données depuis le réseau de production de Bordeaux.
>
> **Cas du « recruteur » étranger :** Nathan intègre le cas de David Chen dans le rapport comme illustration de la menace de niveau étatique. Le rapport souligne que la même vulnérabilité humaine (réceptivité à la flatterie, absence de contre-élicitation) a été exploitée par le red team (exercice contrôlé) et par un acteur de renseignement étranger (menace réelle).
>
> **Recommandations P0 :** (1) Déployer FIDO2 sur tous les comptes à privilèges, (2) Renforcer les procédures de helpdesk (callback obligatoire, interdiction des resets MFA par téléphone seul), (3) Mettre en place une procédure de double validation pour les virements > 5 000 €.
>
> **Recommandations P1 :** (4) Formation ciblée par profil de risque (ingénieurs R&D : contre-élicitation, DAF : BEC, helpdesk : pretexting, réception : intrusion physique), (5) Migration vers DESFire EV2 pour le contrôle d'accès physique, (6) Tourniquets anti-tailgating aux accès principaux.
>
> **Recommandations P2 :** (7) Programme de simulation de phishing mensuel avec retour individualisé, (8) Brief systématique avant les salons professionnels et les voyages, (9) Audit OSINT de la surface d'exposition de l'entreprise (informations accessibles en source ouverte).
>
> Helios lance un programme de remédiation sur 12 mois. Nathan conclut sa restitution : « La meilleure défense technique ne vaut rien si un humain tient la porte. Et la meilleure formation ne vaut rien si la culture d'entreprise punit ceux qui signalent un doute plutôt que de les remercier. »


---
