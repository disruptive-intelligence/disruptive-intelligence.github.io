---
title: Outils et techniques ASM
source: Cyber/99_Concepts/HTB_Attack Surface Management.md
note: HTB — Attack Surface Management
up:
- - HTB — Attack Surface Management
  - index.md
---

### Analyse des systèmes et applications

- Scanner l’ensemble de l’environnement afin d’identifier :
    - assets ;
    - applications ;
    - vulnérabilités ;
    - situations à risque.
- Les scans peuvent être :
    - automatisés ;
    - manuels.
- L’objectif est de ne laisser **aucun segment ou endpoint hors périmètre**.

```
Asset Discovery
+
Vulnerability Scanning
→ Visibility
```

#### Asset Discovery Tools

- Détectent les systèmes, réseaux, applications et services existants.
#### Vulnerability Scanners

- Recherchent automatiquement :
    - CVE ;
    - configurations faibles ;
    - versions vulnérables ;
    - services exposés.

 **Asset Discovery ≠ Vulnerability Scanning**

 - Asset Discovery → _Qu’est-ce qui existe ?_
- Vulnerability Scanning → _Qu’est-ce qui est vulnérable ?_
### Réduction des actifs

- Vous devez identifier et arrêter les actifs au sein de votre organisation qui présentent des risques potentiels, tels que les ordinateurs, serveurs, logiciels ou services inutiles ou non utilisés.
- Cela, en plus de réduire la surface exposée aux cyberattaques, contribuera à diminuer les coûts de maintenance et de sécurité de l'organisation.
- Identifier les systèmes ou logiciels :
    - inutilisés ;
    - obsolètes ;
    - redondants ;
    - non nécessaires.

Puis :

```
Unused Asset
→ Decommission
→ Attack Surface ↓
```

-> Cela peut également réduire les coûts de maintenance et de sécurité.

### Désactivation des services inutiles

- Désactiver :
    - network services inutiles ;
    - ports ouverts sans justification ;
    - fonctions non utilisées.

```
Unused Service
→ Disable

Unused Port
→ Close
```

→ réduit les possibilités d’exploitation à distance.
### Désinstallation des applications inutiles

- Supprimer les applications :
    - inutilisées ;
    - non maintenues ;
    - obsolètes ;
    - non autorisées.

Une application non utilisée reste malgré tout :

```
Installed Software
→ Code
→ Vulnerabilities
→ Attack Surface
```

### Surveillance et évaluation continues

- Revoir régulièrement :
    - assets ;
    - services ;
    - applications ;
    - nouvelles vulnérabilités ;
    - bulletins de sécurité éditeurs.

```
Vendor Advisory
→ New Vulnerability
→ Affected Asset?
→ Prioritize Remediation
```

### Network Analysis & Discovery Tools

- Les outils d’analyse réseau permettent d’observer :
    - trafic ;
    - communications ;
    - anomalies ;
    - comportements suspects ;
    - mouvements d’un attaquant.

Ils complètent les scanners de vulnérabilités :

```
Vulnerability Scanner
→ Known Weaknesses

Network Monitoring
→ Suspicious Behavior
```

- C’est particulièrement important contre des menaces non encore connues, comme une éventuelle **Zero-Day**.

> Un système peut être totalement patché et pourtant être compromis via une vulnérabilité inconnue ou un comportement non prévu.
### Threat Intelligence

- Les outils de **Threat Intelligence** fournissent des informations sur :
    - threat actors ;
    - campagnes ;
    - nouvelles vulnérabilités ;
    - IoC ;
    - TTP ;
    - tendances d’attaque.

```
Global Threat Intelligence
+
Internal Telemetry
→ Better Detection Context
```

Exemples d’utilisation :

- IP connue comme malveillante ;
- domaine C2 ;
- hash malware ;
- vulnérabilité activement exploitée.
### Firewall & Security Tool Logs

- Les logs des firewalls et autres outils de sécurité donnent une visibilité sur :
    - connexions entrantes ;
    - connexions sortantes ;
    - flux bloqués ;
    - communications externes ;
    - tentatives de reconnaissance.

```
Internet
↕
Firewall Logs
↕
Internal Network
```

Ils peuvent aider à détecter :

- scans ;
- brute force ;
- communications C2 ;
- lateral movement ;
- exfiltration.
### Sensibilisation du personnel

- Les employés font eux aussi partie de la surface d’attaque.
- Les enquêtes et formations permettent d’évaluer et améliorer :
    - awareness ;
    - reconnaissance du phishing ;
    - bonnes pratiques ;
    - signalement des incidents.

```
Technology
+
Processes
+
People
→ Attack Surface Management
```


## Outils open-source

- OWASP AMASS
- Nuclei
- GreenBone Community Edition
