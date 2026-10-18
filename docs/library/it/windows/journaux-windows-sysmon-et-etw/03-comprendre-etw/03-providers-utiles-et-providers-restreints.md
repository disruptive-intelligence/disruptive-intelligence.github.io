---
title: Providers utiles et providers restreints
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Comprendre ETW
  - index.md
---

## 6. Providers ETW utiles pour le threat hunting

ETW permet d'exploiter des fournisseurs spécialisés selon les activités recherchées.

### Surveillance des processus, fichiers et registre

| Provider                          | Utilisation                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microsoft-Windows-Kernel-Process  | Analyser les activités de processus et rechercher des indices de Process Injection ou Process Hollowing, utile pour surveiller l'activité liée aux processus dans le noyau Windows                                                                                                                         |
| Microsoft-Windows-Kernel-File     | Examiner les opérations fichiers suspectes, notamment détection impliquant un accès non autorisé à des fichiers, des modifications de fichiers système critiques ou dans les scénarios Ransomware                                                                                                          |
| Microsoft-Windows-Kernel-Registry | Rechercher des modifications du registre liées à la Persistence ou utile pour les scénarios de détection liés aux modifications des clés de registre, souvent associées à des mécanismes de persistance, à l'installation de logiciels malveillants ou à des modifications de la configuration du système. |
| Microsoft-Windows-DotNETRuntime   | Examiner les activités du runtime .NET, identifier les anomalies dans l'exécution des applications .NET, l'exploitation potentielle de vulnérabilités .NET ou le chargement malveillant d'assemblys .NET.                                                                                                  |

### Surveillance du réseau et des accès distants

| Provider                                               | Utilisation                                                                      |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Microsoft-Windows-Kernel-Network                       | Analyser certaines activités réseau et communications suspectes                  |
| Microsoft-Windows-SMBClient / SMBServer                | Rechercher des comportements SMB inhabituels, notamment liés au Lateral Movement |
| Microsoft-Windows-DNS-Client                           | Examiner les requêtes DNS suspectes, C2 ou DNS Tunneling potentiel               |
| Microsoft-Windows-VPN-Client                           | Surveiller certaines activités de connexion VPN                                  |
| OpenSSH                                                | Analyser les activités SSH et tentatives d'authentification                      |
| WinRM                                                  | Rechercher des activités de gestion ou d'exécution à distance suspectes          |
| Microsoft-Windows-TerminalServices-LocalSessionManager | Investiguer les sessions Remote Desktop et Terminal Services                     |

### Surveillance de l'exécution et de la sécurité

| Provider                               | Utilisation                                                                         |
| -------------------------------------- | ----------------------------------------------------------------------------------- |
| Microsoft-Windows-PowerShell           | Examiner les activités PowerShell, notamment les événements de Script Block Logging |
| Microsoft-Windows-CodeIntegrity        | Identifier des anomalies dans les contrôles d'intégrité du code et des pilotes      |
| Microsoft-Windows-Security-Mitigations | Examiner les événements associés aux protections et mesures d'atténuation Windows   |
| Microsoft-Antimalware-Service          | Surveiller certaines activités et modifications concernant l'antimalware            |
| Microsoft-Antimalware-Protection       | Examiner les mécanismes de protection antimalware                                   |

Ces fournisseurs peuvent améliorer la visibilité sur les techniques d'attaque, mais leur simple activation ne garantit pas la détection des comportements cités.

La télémétrie effectivement disponible dépend des événements émis, des filtres, des permissions, de la version Windows et des capacités du consommateur.

## 7. Providers ETW restreints

Certains fournisseurs ETW sont Restricted Providers.

Ils donnent accès à des données sensibles et nécessitent des autorisations particulières.

### Microsoft-Windows-Threat-Intelligence

`Microsoft-Windows-Threat-Intelligence` est un fournisseur restreint particulièrement intéressant pour les opérations de sécurité.

Cependant, pour accéder à ce fournisseur, les processus doivent être privilégiés avec un droit spécifique, connu sous le nom de Protected Process Light (PPL).

Il peut offrir une télémétrie détaillée sur certaines activités système associées aux menaces.

Cette visibilité est pertinente pour :

- Advanced Threat Detection ;
- Threat Hunting ;
- Malware Analysis ;
- Digital Forensics ;
- Incident Response.

### Protected Process Light — PPL

L'accès à ce fournisseur est soumis à des restrictions de sécurité liées notamment au modèle Protected Process Light (PPL).

Les processus PPL disposent de protections Windows particulières, utilisées notamment par certains composants de sécurité.

Pour les solutions antimalware, la mise en place d'un service protégé peut impliquer :

- des exigences de validation et de signature par Microsoft ;
- l'utilisation d'un pilote ELAM (Early Launch Anti-Malware) ;
- des mécanismes de signature spécifiques ;
- l'exécution du service antimalware avec le niveau de protection approprié.

L'accès au fournisseur `Microsoft-Windows-Threat-Intelligence` n'est donc pas équivalent à l'activation d'une session ETW classique depuis un terminal administrateur.

Le support mentionne également l'existence de recherches sur les mécanismes permettant de contourner certaines restrictions d'accès.

Intérêt défensif : ce fournisseur illustre que certaines données de sécurité avancées sont accessibles uniquement à des composants disposant des privilèges et protections nécessaires.
