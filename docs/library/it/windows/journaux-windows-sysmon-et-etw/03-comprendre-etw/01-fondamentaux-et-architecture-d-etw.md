---
title: Fondamentaux et architecture d'ETW
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Comprendre ETW
  - index.md
---

## 1. Les fondamentaux d'ETW

ETW est un mécanisme de journalisation et de traçage haute performance intégré au système d'exploitation Windows.

Il repose sur une infrastructure de mise en mémoire tampon (buffering) et de journalisation permettant de collecter des événements avec une surcharge généralement limitée.

### Activités observables

Selon les fournisseurs activés, ETW peut fournir des informations sur :

- Process Activity : création, terminaison et activités des processus.
- File Activity : accès et modifications de fichiers.
- Registry Activity : opérations sur le registre Windows.
- Network Activity : communications et événements réseau.
- System Activity : événements du noyau, services et composants Windows.
- Application Activity : événements générés par les applications et logiciels tiers.

Ces données permettent de détecter des comportements suspects et de reconstruire le déroulement d'un incident.

### ETW ou journaux d'événements Windows

| Technologie        | Rôle                                                                                           |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| ETW                | Infrastructure de génération et de collecte d'événements                                       |
| Windows Event Logs | Système de journalisation et de consultation d'événements Windows                              |
| Sysmon             | Outil de collecte spécialisé enregistrant des événements détaillés dans les Windows Event Logs |

Point essentiel : tous les événements ETW ne sont pas automatiquement visibles dans Event Viewer. Certains sont disponibles uniquement dans des sessions de tracing spécifiques.

## 2. Architecture et composants d'ETW

ETW repose sur un modèle Publish / Subscribe, dans lequel les fournisseurs produisent des événements et les sessions organisent leur collecte.

```
ETW Providers
      ↓
ETW Sessions ← Controllers
      ↓
Event Buffers
      ↓
Consumers / ETL Files
      ↓
Threat Hunting / DFIR Analysis
```


![Architecture ETW (Microsoft) : providers, sessions, controller, trace files, consumer](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-35.png)

### Contrôleurs (controllers)

Les Controllers gèrent les sessions de tracing.

Ils permettent notamment de :

- créer et démarrer une session ;
- arrêter une session ;
- activer ou désactiver des fournisseurs ;
- configurer les paramètres de collecte.

Exemple : Un contrôleur largement utilisé est l'utilitaire intégré « logman.exe », qui facilite la gestion des activités ETW.

### Fournisseurs (providers)

Les ETW Providers sont les composants qui génèrent les événements.

Ils peuvent provenir du système d'exploitation, d'applications, de pilotes ou de logiciels tiers.

Quatre types :

| Provider Type            | Fonctionnement                                                                                                                                                                                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MOF Providers            | Ces fournisseurs sont basés sur le format MOF (Managed Object Format) et sont capables de générer des événements selon des schémas MOF prédéfinis. Ils offrent une approche flexible de la génération d'événements et sont largement utilisés dans divers scénarios. |
| WPP Providers            | Tracing basé sur des macros, souvent utilisé pour le diagnostic de composants bas niveau                                                                                                                                                                             |
| Manifest-Based Providers | Événements décrits à l'aide de manifestes XML                                                                                                                                                                                                                        |
| TraceLogging Providers   | Génération d'événements avec une API de journalisation simplifiée                                                                                                                                                                                                    |

ETW peut également être étendu grâce à des Custom Providers développés pour des besoins spécifiques.

### Sessions ETW

Une ETW Session collecte les événements provenant d'un ou plusieurs fournisseurs activés.

Elle détermine notamment les paramètres de collecte, les filtres et le mode de traitement des événements.

Certaines sessions fonctionnent en temps réel, tandis que d'autres enregistrent des traces destinées à une analyse ultérieure.

### Consommateurs (consumers)

Les Consumers récupèrent les événements collectés pour les analyser ou les traiter.

Deux modes importants :

- Real-Time Consumption : traitement des événements au fur et à mesure de leur génération.
- ETL Analysis : consultation des événements enregistrés dans des fichiers `.etl`.

### Canaux (channels)

Les ETW Channels organisent certains événements selon leur destination ou leur finalité.

Ils facilitent l'exploitation des événements par Windows Event Logging.

Tous les providers ou événements ETW ne disposent cependant pas d'un canal exploitable directement depuis Event Viewer.

### Fichiers ETL

Les fichiers `.etl` (Event Trace Log) permettent d'enregistrer des traces ETW sur disque.

Ils sont utiles pour :

- conserver une capture d'événements ;
- analyser une activité a posteriori ;
- réaliser une investigation forensic ;
- archiver une collecte spécifique.

Précision : une session ETW peut également fonctionner sans créer de fichier ETL, notamment en mode temps réel.
