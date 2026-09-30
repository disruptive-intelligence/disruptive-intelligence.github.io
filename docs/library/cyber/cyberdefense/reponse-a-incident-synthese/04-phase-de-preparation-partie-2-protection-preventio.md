---
title: 'Phase de préparation — Partie 2 : Protection & prévention'
source: Cyber/05_Cyberdefense/HTB_Réponse à incidents.md
note: Réponse à incident — synthèse
up:
- - Réponse à incident — synthèse
  - index.md
---

- La phase **Preparation** ne consiste pas uniquement à préparer l’équipe Incident Response.
- Elle comprend aussi la mise en place de contrôles capables de :
    - prévenir les incidents ;
    - limiter leur impact ;
    - améliorer leur détection ;
    - fournir des artefacts utiles à l’investigation.

```
Preparation
├─ Incident Response Readiness
└─ Preventive / Detective Controls
```

## Protection des e-mails
### DMARC

- **DMARC — Domain-based Message Authentication, Reporting & Conformance** protège principalement contre l’**usurpation directe d’un domaine**.
- L'idée est de rejeter les e-mails qui "prétendent" provenir d'une organisation.
- Il s’appuie sur :
    - **SPF** ;
    - **DKIM** ;
    - leur alignement avec le domaine visible dans le champ `From:`.

```
SPF
+
DKIM
+
Domain Alignment
→ DMARC
```

#### SPF

- Définit quels serveurs sont autorisés à envoyer des e-mails pour un domaine.
#### DKIM

- Ajoute une **signature cryptographique** permettant de vérifier :
    - l’origine du message ;
    - son intégrité.
#### DMARC

- Définit la politique à appliquer lorsque les contrôles échouent.

Politiques principales :

```
p=none
→ monitor

p=quarantine
→ considérer le message comme suspect

p=reject
→ refuser le message
```

> DMARC ne bloque pas **tout le phishing**. Il protège surtout contre le spoofing du domaine ; un attaquant peut toujours utiliser un domaine ressemblant au domaine légitime.
Exemple :

```
company.com
vs
cornpany.com
```

#### Déploiement

- Tester avant d’appliquer une politique stricte.
- Vérifier notamment :
    - services SaaS envoyant des e-mails ;
    - plateformes marketing ;
    - systèmes de ticketing ;
    - prestataires envoyant « au nom de » l’entreprise.

```
Monitor
→ Fix legitimate senders
→ Quarantine
→ Reject
```

-> Un mauvais déploiement peut bloquer des messages légitimes.
## Endpoint Hardening & EDR

- Les endpoints représentent une surface d’attaque importante car les utilisateurs :
    - naviguent sur Internet ;
    - ouvrent des documents ;
    - téléchargent des fichiers ;
    - exécutent des applications.
- Les baselines de hardening peuvent notamment s’appuyer sur :
    - **CIS Benchmarks** ;
    - recommandations Microsoft. Markdown collé
### Désactivation de LLMNR / NetBIOS

- Désactiver lorsque ces protocoles ne sont pas nécessaires.

Pourquoi ?

```
Name Resolution Failure
→ LLMNR / NBT-NS
→ Attacker Spoofing
→ Credential Capture
```

Ils peuvent faciliter des attaques de type :

- poisoning ;
- NTLM credential capture ;
- relay selon le contexte.
### Windows LAPS

- Utiliser **Windows LAPS** pour gérer les mots de passe des comptes administrateurs locaux.

```
Machine A → Unique Password
Machine B → Unique Password
Machine C → Unique Password
```

Objectifs :

- éviter un mot de passe local partagé ;
- rotation automatique ;
- limiter le lateral movement.
### Retrait des privilèges administrateur

- Les utilisateurs standards ne doivent pas être **Local Administrator** sans besoin réel.

```
Standard User
→ Least Privilege

Admin Rights
→ uniquement lorsque nécessaire
```

Une compromission d’un utilisateur administrateur augmente fortement l’impact potentiel.
### PowerShell
Le cours recommande notamment de restreindre PowerShell avec :

```
Constrained Language Mode
```

- **ConstrainedLanguage** limite certaines fonctionnalités puissantes de PowerShell.
- Peut faire partie d’une stratégie de hardening, mais ne doit pas être considéré comme une protection autonome.

Contrôles complémentaires :

- Script Block Logging ;
- Module Logging ;
- AMSI ;
- WDAC / AppLocker ;
- EDR.
### Attack Surface Reduction — ASR

- Les **Microsoft Defender ASR Rules** permettent de bloquer certains comportements couramment utilisés par les attaquants.

Exemples :

```
Office
→ Child Process
→ Block

Office Macro
→ Win32 API
→ Block

Credential Stealing
→ LSASS
→ Block / Restrict
```

Objectif :

```
Reduce exploitable behaviors
→ Attack Surface ↓
```

## Application Allowlisting

- Autoriser uniquement les applications ou comportements nécessaires.
- Technologies possibles :
    - AppLocker ;
    - Windows Defender Application Control — WDAC.

Le cours recommande au minimum de contrôler l’exécution depuis des emplacements inscriptibles par l’utilisateur comme :

```
Downloads
Desktop
AppData
Temp
```

et certains types de scripts :

```
.hta
.vbs
.js
.cmd
.bat
```

Markdown collé
### LOLBins

- **LOLBins — Living Off The Land Binaries** :
    - binaires légitimes présents sur le système ;
    - détournés pour réaliser des actions malveillantes.

Exemples classiques :

```
powershell.exe
mshta.exe
rundll32.exe
regsvr32.exe
certutil.exe
```

```
Trusted Binary
→ Abused Functionality
→ Malicious Action
```

> ⚠️ Le cours parle de « bloquer le trafic sortant vers les LOLBins ». Techniquement, les LOLBins sont des **binaires**, pas des destinations réseau. Leur usage est plutôt contrôlé via **WDAC/AppLocker/ASR/EDR**, tandis que le firewall limite les communications réseau qu’ils pourraient initier.
## Host-Based Firewall

- Utiliser un firewall sur les endpoints.
- Contrôler :
    - inbound ;
    - outbound ;
    - communications inter-workstations.

Exemple :

```
Workstation A
   X
Workstation B
```

Bloquer les communications poste-à-poste inutiles peut réduire :

- lateral movement ;
- SMB abuse ;
- propagation de malware.
## EDR — Endpoint Detection & Response

- Déployer un **EDR** pour obtenir :
    - telemetry ;
    - behavioral detection ;
    - investigation ;
    - containment ;
    - response.
### AMSI

- **AMSI — Antimalware Scan Interface** permet aux produits de sécurité d’inspecter notamment certains contenus scriptés avant ou pendant leur exécution.

Particulièrement utile pour :

- PowerShell ;
- scripts ;
- contenu obfusqué.

```
Script
→ AMSI
→ Security Product
→ Inspect
→ Allow / Detect
```

## Protection réseau
### Segmentation

- Segmenter le réseau pour empêcher qu’une compromission locale devienne une compromission globale.
- Les systèmes critiques doivent être isolés.
- N’autoriser que les communications réellement nécessaires. Markdown collé

```
User Network
   ↓ limited
Application Network
   ↓ limited
Database Network
```

Principe :

```
Compromise
→ Segmentation
→ Blast Radius ↓
```

### DMZ

- Les services qui doivent être exposés à Internet peuvent être placés dans une **DMZ**.

```
Internet
   ↓
Firewall
   ↓
DMZ
   ↓ restricted
Internal Network
```

- Les ressources internes ne devraient pas être directement exposées lorsque cela n’est pas nécessaire. Markdown collé
### IDS / IPS
#### IDS

```
Traffic
→ Detection
→ Alert
```

#### IPS

```
Traffic
→ Detection
→ Block / Prevent
```

- Ils peuvent détecter :
    - signatures ;
    - protocol anomalies ;
    - comportements suspects ;
    - certains patterns d’exploitation.
#### TLS Inspection

- Le trafic HTTPS étant chiffré, son contenu n’est normalement pas directement visible par les équipements réseau.
- Une organisation peut utiliser une **TLS inspection / interception** pour inspecter certains flux. Markdown collé

```
Client
→ TLS Inspection
→ Security Analysis
→ TLS
→ Server
```

> Cela nécessite une conception rigoureuse : gestion des certificats, confidentialité, conformité, performance et exclusion éventuelle de certaines catégories de trafic sensible.
### Network Access Control
#### 802.1X

- **802.1X** permet de contrôler quels utilisateurs/appareils peuvent accéder au réseau.

```
Device
→ Authentication
→ Network Access
```

Peut réduire les risques liés aux :

- équipements inconnus ;
- appareils personnels ;
- dispositifs malveillants.

Markdown collé
#### Conditional Access
Dans les environnements cloud / Microsoft Entra ID :

```
User
+
Device State
+
Location
+
Risk
→ Access Decision
```

Exemple :

```
Managed Device
+
MFA
→ Allow

Unmanaged Device
→ Block / Restrict
```

### Gestion des identités à privilèges / MFA / Mots de passe
#### Privileged Identity Management

- Les comptes privilégiés sont des cibles particulièrement importantes.
- Éviter :
    - mots de passe faibles ;
    - passwords réutilisés ;
    - même password entre compte standard et compte admin. Markdown collé

```
Daily Account
≠
Administrative Account
```

### Passwords / Passphrases
Le cours met l’accent sur les **passphrases** :

```
Long
+
Memorable
+
Hard to Guess
```

Un mot de passe comme :

```
Password1!
```

respecte plusieurs règles classiques de complexité mais reste extrêmement prévisible.

> La longueur et la résistance aux mots de passe compromis sont plus importantes qu’une complexité artificielle seule.
## MFA

- Mettre en œuvre le **Multi-Factor Authentication** au minimum pour :
    - comptes administrateurs ;
    - remote access ;
    - applications critiques ;
    - accès privilégiés.

Markdown collé

```
Password
→ Something You Know

Security Key
→ Something You Have

= MFA
```

Lorsque possible, préférer des méthodes **phishing-resistant** comme :

- FIDO2 ;
- WebAuthn ;
- hardware security keys.
## Vulnerability Management

- Réaliser des vulnerability scans régulièrement ou continuellement.
- Identifier :
    - CVE ;
    - versions obsolètes ;
    - mauvaises configurations ;
    - services vulnérables. Markdown collé

```
Scan
→ Identify
→ Prioritize
→ Remediate
→ Verify
```

> Le cours propose de corriger au minimum les vulnérabilités `High` et `Critical`. En pratique, la priorité ne devrait pas dépendre uniquement de la sévérité.
Considérer aussi :

```
CVSS
+
Exploitability
+
Active Exploitation
+
Internet Exposure
+
Asset Criticality
+
Business Impact
```

### Si le patch est impossible
Mettre en place des **compensating controls** :

- segmentation ;
- firewall rules ;
- désactivation du service ;
- restriction d’accès ;
- IPS / virtual patching ;
- monitoring renforcé.

```
Cannot Patch
→ Reduce Exposure
→ Monitor
```

## Security Awareness Training

- Former les utilisateurs à :
    - identifier les comportements suspects ;
    - reconnaître le phishing ;
    - signaler rapidement les incidents. Markdown collé

Des simulations peuvent être organisées :

- phishing simulations ;
- exercices de social engineering ;
- scénarios USB contrôlés.

Objectif principal :

```
User Detects Suspicious Activity
→ Reports Quickly
→ SOC Investigates
```

> Les exercices doivent mesurer et améliorer les comportements de sécurité, pas uniquement « piéger » les utilisateurs.
## Active Directory Security Assessment

- Auditer régulièrement Active Directory depuis une perspective attaquant.
- Objectif :
    - trouver les chemins d’escalade avant un adversaire ;
    - supprimer les « easy wins » ;
    - augmenter le nombre d’étapes nécessaires à la compromission. Markdown collé

```
Compromised Endpoint
        ↓
Can attacker immediately become Domain Admin?
```

Rechercher notamment :

- privilèges excessifs ;
- ACL faibles ;
- comptes privilégiés mal protégés ;
- mauvaises délégations ;
- services mal configurés ;
- chemins d’attaque vers des Tier 0 assets.

Principe défensif :

```
More attacker actions required
→ More telemetry
→ More opportunities for detection
```

## Purple Team Exercises

- Une **Purple Team** rapproche :
    - Red Team / offensive security ;
    - Blue Team / defensive security.
- La Red Team exécute des techniques adverses.
- La Blue Team vérifie :
    - visibilité ;
    - logging ;
    - detection ;
    - alerting ;
    - response. Markdown collé

```
Red Team
→ Execute TTP

Blue Team
→ Detect / Investigate / Respond

        ↓

Purple Team
→ Share Findings
→ Improve Defenses
```

### Objectifs
Tester concrètement :

- EDR ;
- SIEM ;
- detection rules ;
- playbooks ;
- logging ;
- SOC response ;
- incident handling procedures.

```
Attack Simulated
→ Detected?
├─ Yes → Test Response
└─ No  → Detection Gap
```

Une technique non détectée devient une opportunité pour :

```
Improve Logging
→ Create Detection
→ Update Playbook
→ Retest
```

## Défense en profondeur
Les différentes mesures de cette section ne doivent pas être considérées isolément.

```
Email Security
        ↓
Endpoint Hardening
        ↓
EDR
        ↓
Identity / MFA / PAM
        ↓
Network Segmentation
        ↓
IDS / IPS
        ↓
Vulnerability Management
        ↓
Monitoring
        ↓
Incident Response
```

→ l’objectif est qu’une défaillance d’un contrôle ne suffise pas à compromettre entièrement l’environnement.

```
Prevent
+
Detect
+
Contain
+
Respond
→ Defense in Depth
```
