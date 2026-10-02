---
title: 'Partie II — Détection : l''art de voir les menaces'
source: Cyber/06 Détection & réponse/Détection & SOC/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*Comment les menaces deviennent des alertes. Cette partie enseigne les principes de détection, l'utilisation d'ATT&CK pour structurer la couverture, l'écriture de règles Sigma de qualité, et la détection dans les environnements cloud — le tout avec l'objectif de construire une capacité de détection durable, pas juste une collection de règles.*

---


## Chapitre 5 — Principes de la détection

### 5.1 Les approches de détection

La détection par **signature / IoC** matche des indicateurs exacts : un hash, une IP, un domaine, un pattern de fichier. C'est rapide, précis (peu de FP), mais éphémère — l'attaquant change ses IoC en quelques heures. C'est le bas de la Pyramid of Pain.

La détection **comportementale** identifie des patterns d'activité suspects indépendamment des IoC : un process tree anormal (svchost.exe avec explorer.exe comme parent), une séquence d'actions caractéristique (logon réseau + accès LSASS + Kerberos TGS request en rafale = credential access), un volume de données sortantes anormal. Plus résiliente que la signature, mais plus de faux positifs — le comportement « suspect » peut être légitime (un admin IT qui fait un PsExec est identique à un attaquant qui fait un PsExec).

La détection par **anomalie statistique / ML** établit une baseline d'activité normale (le comportement habituel d'un utilisateur, d'une machine, d'un flux réseau) et détecte les écarts significatifs. Utile pour le beaconing (intervalles réguliers de connexion), l'impossible travel (connexion depuis deux pays en 1 heure), et les volumes anormaux. Fragile si la baseline est mal calibrée — un utilisateur qui change de comportement légitime (nouveau projet, voyage) déclenche des alertes.

La détection par **corrélation** croise plusieurs événements faibles qui ensemble forment un signal fort. Un 4624 type 3 isolé n'est rien. Un 4624 type 3 depuis un poste RH vers un DC + un 4769 RC4 + un 4648 avec le compte svc-backup en 10 minutes = une chaîne d'attaque (mouvement latéral → Kerberoasting → utilisation de credentials volées). La corrélation est l'approche la plus puissante et la plus complexe.

### 5.2 Le compromis précision vs couverture

Une règle très spécifique (« certutil.exe avec l'argument -urlcache ET le parent winword.exe ») a peu de FP mais rate les variantes (l'attaquant utilise bitsadmin au lieu de certutil, ou PowerShell IWR au lieu de certutil). Une règle large (« tout processus enfant de winword.exe qui fait une connexion réseau ») couvre plus de variantes mais génère du bruit (les macros légitimes qui font des appels réseau). L'art du detection engineer est de trouver le point d'équilibre — et d'accepter que ce point bouge dans le temps (les attaquants s'adaptent, les faux positifs changent avec l'environnement).

---


## Chapitre 6 — MITRE ATT&CK pour le SOC

### 6.1 ATT&CK comme ossature de la détection

MITRE ATT&CK n'est pas seulement un référentiel pour les rapports CTI — c'est l'ossature opérationnelle de la détection. Chaque règle de détection du SIEM doit être mappée à une ou plusieurs techniques ATT&CK (via les tags Sigma). Cette discipline permet de mesurer la couverture (quelles techniques sont détectées, lesquelles ne le sont pas) et de prioriser le développement.

### 6.2 Les techniques prioritaires pour tout SOC

Toutes les 200+ techniques ne sont pas égales. Les techniques suivantes doivent être couvertes en priorité car elles sont utilisées par la quasi-totalité des acteurs et elles sont détectables avec des logs standard.

**Initial Access :** T1566.001/.002 (Phishing — Attachment / Link), T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts). **Execution :** T1059.001/.003/.005 (PowerShell / Windows Command Shell / Visual Basic), T1204 (User Execution), T1047 (WMI). **Persistence :** T1053.005 (Scheduled Task), T1543.003 (Windows Service), T1547.001 (Registry Run Keys). **Privilege Escalation :** T1558.003 (Kerberoasting), T1003 (OS Credential Dumping). **Defense Evasion :** T1218 (Signed Binary Proxy Execution — rundll32, mshta, regsvr32), T1055 (Process Injection), T1070.001 (Clear Windows Event Logs). **Lateral Movement :** T1021.002 (SMB/Admin Shares — PsExec), T1021.001 (RDP). **Exfiltration :** T1041 (Exfiltration Over C2 Channel), T1567 (Exfiltration Over Web Service). **Command and Control :** T1071.001 (Web Protocols — HTTPS C2), T1105 (Ingress Tool Transfer).

### 6.3 Le gap analysis en pratique

Le gap analysis croise deux informations : les TTP des acteurs qui menacent l'organisation (fournies par la CTI — cours CTI Ch.20) et la couverture de détection actuelle du SOC (quelles techniques sont couvertes par des règles). L'outil est **ATT&CK Navigator** : on colore la matrice en vert (technique couverte par au moins une règle testée), orange (technique partiellement couverte — la règle existe mais n'a pas été testée ou a un taux de FP élevé), et rouge (technique non couverte). Le résultat est un plan de développement priorisé : les techniques rouges utilisées par les acteurs pertinents sont les premières à couvrir.

---


## Chapitre 7 — Detection Engineering : écrire des règles de qualité

### 7.1 Le cycle de vie d'une règle

Le detection engineering suit un cycle structuré. **Besoin :** quelle menace détecter, quel TTP, quel scénario d'attaque. **Données :** quel log source contient les traces (Event ID 1 Sysmon pour l'exécution, Event ID 4769 pour le Kerberoasting, logs proxy pour le C2 web). Le log est-il disponible et correctement parsé dans le SIEM ? **Logique :** quelle condition, quel seuil, quelle fenêtre temporelle. La logique doit cibler la procédure spécifique (pas juste la technique générique). **Rédaction Sigma :** le format pivot universel — la règle est écrite une fois en Sigma et convertie en SPL/KQL/EQL selon le SIEM de chaque client. **Conversion :** pySigma ou sigma-cli convertit la règle Sigma en requête native du SIEM. **Test :** la règle est exécutée sur les logs historiques (rétro-hunt) pour vérifier la détection et les FP. **Déploiement :** mise en production, monitoring du volume d'alertes. **Tuning :** ajustement des conditions et des exceptions basé sur les FP observés en production. **Revue :** revalidation périodique (la règle est-elle toujours pertinente ? l'environnement a-t-il changé ? les FP sont-ils maîtrisés ?).

### 7.2 Sigma en profondeur

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

### 7.3 La gestion des faux positifs

Le FP est l'ennemi n°1 du SOC : trop de FP → fatigue d'alerte → les analystes ne regardent plus → les vrais positifs sont noyés → les FN augmentent. Le paradoxe : réduire les FP en ajoutant des exceptions crée des angles morts (un attaquant qui compromet un compte exclu passe sous le radar).

Les bonnes pratiques : chaque exception est documentée (qui, pourquoi, quand, condition exacte), chaque exception est revue périodiquement (l'exception est-elle toujours justifiée ?), les exceptions ne suppriment pas l'événement — elles réduisent la sévérité ou le routent vers une file d'attente de vérification (l'événement reste visible pour le hunting), et le taux de FP est mesuré par règle (les règles à > 50 % de FP sont re-développées, pas juste supprimées).

---


## Chapitre 8 — YARA, Suricata et détection complémentaire

### 8.1 YARA pour le SOC

YARA identifie et classifie les fichiers par pattern matching. L'analyste SOC l'utilise pour scanner des fichiers suspects (soumission à une sandbox avec règles YARA), enrichir les alertes EDR (le hash de l'alerte matche-t-il une règle YARA connue ?), et dans les pipelines d'analyse automatisée. La structure (meta, strings, condition) et les types de patterns (textuels, hexadécimaux, regex) avec les conditions avancées (filesize, entropy, combinaisons logiques).

### 8.2 Suricata pour la détection réseau

Suricata (et Snort) applique des règles sur le trafic réseau en temps réel. Le SOC utilise les jeux de règles **Emerging Threats** (ET Open gratuit, ET Pro commercial) qui couvrent les signatures de malware réseau, les C2 connus, et les exploits. Les règles Suricata complètent Sigma (qui opère sur les logs) et YARA (qui opère sur les fichiers) en couvrant le trafic réseau.

---


## Chapitre 9 — Détection cloud, SaaS et identités

*L'identité est le nouveau périmètre. En 2025-2026, compromettre un compte cloud donne accès à plus de ressources que compromettre un endpoint. Ce chapitre place l'identité au centre de la détection.*

### 9.1 L'identité comme terrain SOC principal

Dans un environnement hybride (AD on-premise + Azure AD/Entra ID + M365 + SaaS), l'identité n'est plus un sujet IAM périphérique — c'est devenu le terrain de jeu principal des attaquants et donc du SOC. Un token de session volé donne accès à toutes les ressources cloud de l'utilisateur sans jamais toucher un endpoint. Un mot de passe compromis via un infostealer donne accès au VPN, à M365, et potentiellement à l'AD on-premise. Les conditional access policies (MFA, device compliance, location) sont les nouveaux firewalls — et leurs contournements sont les nouvelles vulnérabilités.

### 9.2 Détection Azure AD / Entra ID

Les scénarios de détection critiques : **impossible travel** (connexion depuis Paris à 09h00 puis depuis São Paulo à 09h30 — requête KQL Sentinel sur les SigninLogs avec calcul de distance géographique et de temps), **connexion sans MFA quand MFA est requis** (le conditional access policy a été contournée ou le token a été replay — signal critique), **token replay** (l'attaquant rejoue un token de session volé via un kit AitM — détectable par l'absence de MFA challenge sur une session qui devrait en avoir un, ou par une IP différente entre l'émission du token et son utilisation), **modification d'app registration** (ajout de credentials sur une application — technique de persistence cloud : l'attaquant crée un secret sur une app avec des permissions, puis l'utilise comme backdoor même après le reset du mot de passe de l'utilisateur), et **modification de conditional access** (désactivation de MFA ou ajout d'une exclusion — red flag immédiat).

### 9.3 Détection M365

**BEC (Business Email Compromise) :** création de règle de forwarding Outlook (UAL : `New-InboxRule` avec `ForwardTo` ou `RedirectTo`), accès mailbox depuis une IP suspecte, envoi d'emails inhabituels (demande de virement, changement de RIB). **Exfiltration SharePoint/OneDrive :** téléchargement massif (`FileDownloaded` en volume anormal dans l'UAL), partage externe non autorisé (`SharingSet` avec un domaine externe), et synchronisation vers un device non géré. **Compromission Teams :** messages de phishing interne via Teams (moins surveillé que l'email, souvent un angle mort).

### 9.4 Détection AWS

**IAM changes :** création d'utilisateurs (`CreateUser`), modification de policies (`AttachUserPolicy`, `PutUserPolicy`), création d'access keys (`CreateAccessKey`) — chaque appel API est dans CloudTrail. **S3 :** modification de bucket policy (rendre un bucket public — `PutBucketPolicy`), accès depuis une IP non autorisée. **CloudTrail tampering :** désactivation du logging (`StopLogging`, `DeleteTrail`) — l'anti-forensics cloud, signal critique immédiat.

### 9.5 Fil rouge — FALCONWATCH : la dimension identité

> **🛡️ FALCONWATCH — Épisode 4**
>
> La compromission de WKS-PROD-112 n'est pas qu'un problème endpoint — c'est un problème identité. L'attaquant a obtenu les credentials de Marc Dubois et les utilise pour s'authentifier en réseau (4624 type 3) vers d'autres machines. Plus grave : le Kerberoasting ciblant `svc-scada` est une attaque identité pure — si le mot de passe est cracké, l'attaquant obtient un accès aux systèmes SCADA sans jamais exploiter de vulnérabilité technique. La détection de ce Kerberoasting (rafale de 4769 RC4 depuis WKS-PROD-112) est le moment pivot de l'investigation — c'est ce qui transforme un incident « phishing classique » en incident « accès OT critique ».

---
