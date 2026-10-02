---
title: Annexe A — Glossaire
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

| Terme | Définition |
|-------|-----------|
| **ACL/DACL** | Access Control List / Discretionary ACL — permissions d'accès sur les objets Active Directory ou le système de fichiers |
| **Amcache** | Artefact Windows enregistrant l'historique des programmes exécutés avec leur hash SHA1 |
| **ASN** | Autonomous System Number — identifiant d'un réseau autonome, utile pour identifier l'hébergeur |
| **ATT&CK** | Framework MITRE décrivant les tactiques, techniques et procédures des attaquants |
| **Beaconing** | Pattern de communication périodique entre un malware et son serveur C2 |
| **BEC** | Business Email Compromise — fraude par compromission de messagerie professionnelle |
| **Blast radius** | Périmètre d'impact potentiel d'un incident — nombre de systèmes, utilisateurs, données touchés |
| **BloodHound** | Outil de cartographie des chemins d'attaque dans Active Directory |
| **Break glass account** | Compte d'administration d'urgence, non lié à l'AD principal, utilisable quand le SI est compromis |
| **C2** | Command and Control — infrastructure de commande utilisée par l'attaquant pour piloter le malware |
| **Cellule de crise** | Instance de gouvernance exécutive activée lors d'un incident majeur ou d'une crise |
| **CERT-FR** | Computer Emergency Response Team de l'ANSSI — centre de réponse aux incidents pour l'État français |
| **Chain of custody** | Chaîne de traçabilité des preuves, documentant chaque manipulation d'une preuve numérique |
| **Confinement** | Ensemble des mesures visant à stopper la progression de l'attaquant et limiter l'impact |
| **CSIRT** | Computer Security Incident Response Team — équipe de réponse aux incidents de sécurité |
| **DCSync** | Technique d'attaque AD permettant de simuler un DC pour récupérer les hashes NTLM de tous les comptes |
| **DGA** | Domain Generation Algorithm — algorithme générant des noms de domaine pseudo-aléatoires pour le C2 |
| **Dwell time** | Temps de séjour — durée entre la compromission initiale et la détection de l'incident |
| **EDR** | Endpoint Detection and Response — solution de détection et réponse sur les postes et serveurs |
| **Éradication** | Phase de l'IR consistant à supprimer tous les mécanismes de compromission et de persistence |
| **Event ID** | Identifiant numérique des événements dans les Windows Event Logs |
| **Fileless malware** | Malware s'exécutant uniquement en mémoire, sans écrire de fichier sur le disque |
| **FTK Imager** | Outil d'acquisition forensic pour la création d'images disque bit-à-bit |
| **Golden Ticket** | TGT Kerberos forgé avec le hash du compte krbtgt, donnant un accès illimité au domaine AD |
| **GPO** | Group Policy Object — objet de stratégie de groupe dans Active Directory |
| **IAB** | Initial Access Broker — acteur spécialisé dans la vente d'accès initiaux compromis |
| **IRP** | Incident Response Plan — plan de réponse à incident, document cadre de la capacité IR |
| **IoC** | Indicator of Compromise — indicateur technique de compromission (hash, domaine, IP) |
| **IoA** | Indicator of Attack — indicateur comportemental d'attaque (pattern de mouvement latéral, etc.) |
| **JA3/JA4** | Fingerprinting TLS — empreinte du client TLS permettant d'identifier des connexions suspectes |
| **KAPE** | Kroll Artifact Parser and Extractor — outil de collecte automatisée d'artefacts forensic Windows |
| **Kerberoasting** | Technique d'attaque AD consistant à demander des TGS pour craquer les mots de passe des comptes de service |
| **Kill Chain** | Modèle Lockheed Martin décrivant les 7 phases d'une cyber-attaque |
| **krbtgt** | Compte Active Directory utilisé pour le chiffrement des tickets Kerberos — sa compromission permet les Golden Tickets |
| **LAPS** | Local Administrator Password Solution — solution Microsoft de gestion des mots de passe admin locaux |
| **Lateral movement** | Mouvement latéral — progression de l'attaquant d'un système à un autre au sein du réseau |
| **Loader** | Malware de première étape qui télécharge et exécute le payload principal |
| **MFT** | Master File Table — table maîtresse du système de fichiers NTFS, enregistrant tous les fichiers et métadonnées |
| **MTTC** | Mean Time To Contain — délai moyen entre la détection et le confinement effectif |
| **MTTD** | Mean Time To Detect — délai moyen entre la compromission et la détection |
| **MTTR** | Mean Time To Recover — délai moyen entre le confinement et la reprise complète |
| **NDR** | Network Detection and Response — solution de détection et réponse sur le réseau |
| **NIS 2** | Directive européenne sur la sécurité des réseaux et des systèmes d'information, version 2 |
| **OIV** | Opérateur d'Importance Vitale — organisation identifiée par l'État français comme essentielle |
| **OPSEC** | Operational Security — pratiques de sécurité opérationnelle |
| **PAW** | Privileged Access Workstation — poste dédié et durci pour l'administration privilégiée |
| **Patient zéro** | Premier système compromis dans un incident — le point d'entrée initial de l'attaquant |
| **Playbook** | Document opérationnel décrivant les actions à mener pour un type d'incident spécifique |
| **Plaso** | Outil de création de Super Timeline à partir d'artefacts forensic multiples |
| **Prefetch** | Artefact Windows enregistrant l'historique des programmes exécutés |
| **PRIS** | Prestataires de Réponse aux Incidents de Sécurité — qualification ANSSI pour les prestataires IR |
| **PsExec** | Outil Sysinternals d'exécution de processus à distance — fréquemment utilisé pour le mouvement latéral |
| **RACI** | Responsible, Accountable, Consulted, Informed — matrice de responsabilité |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de distribution de ransomware |
| **RETEX** | Retour d'expérience — analyse post-incident structurée |
| **Scoping** | Délimitation du périmètre de compromission d'un incident |
| **ShimCache** | Artefact Windows (AppCompatCache) enregistrant les programmes exécutés |
| **SIEM** | Security Information and Event Management — plateforme de collecte et corrélation des logs |
| **SitRep** | Situation Report — rapport de situation périodique pendant un incident |
| **SPN** | Service Principal Name — identifiant de service dans Active Directory, cible du Kerberoasting |
| **SRUM** | System Resource Usage Monitor — artefact Windows enregistrant la consommation réseau par processus |
| **Tiering** | Modèle de séparation des niveaux d'administration AD (Tier 0/1/2) |
| **Timeline** | Chronologie reconstituée des événements d'un incident |
| **Triage** | Évaluation rapide initiale d'un incident pour déterminer sa nature et sa gravité |
| **TTP** | Tactics, Techniques, and Procedures — méthodes opérationnelles d'un attaquant |
| **UAL** | Unified Audit Log — journal d'audit unifié de Microsoft 365 |
| **USN Journal** | Update Sequence Number Journal — journal des modifications du système de fichiers NTFS |
| **Velociraptor** | Outil de collecte forensic et de threat hunting à grande échelle |
| **Volatility** | Framework open source d'analyse de mémoire vive (RAM) |
| **WORM** | Write Once Read Many — stockage immuable, résistant au ransomware |

---
