---
title: Annexe F — Tableau d'outils de référence IR
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|-----------|-------|---------------|-------|---------|
| **EDR** | CrowdStrike Falcon | Payant | Détection, containment, telemetry | Coût élevé, nécessite agent |
| **EDR** | Microsoft Defender for Endpoint | Payant (inclus E5) | Détection, containment, intégration M365 | Nécessite licence E5 pour full feature |
| **EDR** | SentinelOne | Payant | Détection, containment, rollback ransomware | Coût élevé |
| **SIEM** | Splunk Enterprise | Payant | Corrélation logs, investigation, dashboards | Coût de licence basé sur le volume |
| **SIEM** | Microsoft Sentinel | Payant (cloud) | Corrélation, intégration Azure/M365 | Coût variable selon ingestion |
| **SIEM** | Elastic Security (ELK) | Gratuit (OSS) / Payant (cloud) | Corrélation, flexible, extensible | Expertise nécessaire pour déploiement |
| **NDR** | Vectra AI | Payant | Détection réseau, beaconing, mouvement latéral | Coût élevé |
| **NDR** | Zeek (ex-Bro) | Gratuit (OSS) | Analyse de trafic réseau, génération de logs | Nécessite expertise, pas de GUI |
| **Forensic** | KAPE | Gratuit | Collecte automatisée d'artefacts Windows | Windows uniquement |
| **Forensic** | Velociraptor | Gratuit (OSS) | Collecte à grande échelle, hunting | Courbe d'apprentissage |
| **Forensic** | FTK Imager | Gratuit | Image disque bit-à-bit | Interface vieillissante |
| **Forensic** | Autopsy | Gratuit (OSS) | Analyse forensic complète | Performances variables |
| **Mémoire** | Volatility 3 | Gratuit (OSS) | Analyse de dumps mémoire | Nécessite expertise, plugins limités |
| **Mémoire** | DumpIt (Comae) | Gratuit | Acquisition mémoire Windows rapide | Windows uniquement |
| **Timeline** | Plaso (log2timeline) | Gratuit (OSS) | Super Timeline à partir d'artefacts multiples | Lent sur gros volumes |
| **Timeline** | Timesketch | Gratuit (OSS) | Visualisation collaborative de timelines | Nécessite infrastructure |
| **Malware** | ANY.RUN | Freemium | Sandbox interactive en ligne | Échantillons publics en version gratuite |
| **Malware** | Joe Sandbox | Payant | Sandbox automatisée, analyse approfondie | Coût |
| **Malware** | VirusTotal | Freemium | Multi-scanner, intelligence, relations | Échantillons partagés avec la communauté |
| **AD Audit** | PingCastle | Gratuit (usage interne) | Score de sécurité AD, recommandations | Ne couvre pas tout ATT&CK |
| **AD Audit** | Purple Knight (Semperis) | Gratuit | Audit AD automatisé, détection faiblesses | Rapport parfois verbeux |
| **AD Audit** | BloodHound | Gratuit (OSS) | Cartographie des chemins d'attaque AD | Nécessite collecte SharpHound |
| **SOAR** | Cortex XSOAR (Palo Alto) | Payant | Orchestration, playbooks automatisés | Coût, complexité |
| **SOAR** | Shuffle | Gratuit (OSS) | Orchestration, playbooks | Moins mature que XSOAR |
| **Cloud** | Hawk (PowerShell) | Gratuit (OSS) | Investigation M365 / Entra ID | Limité à l'écosystème Microsoft |

---
