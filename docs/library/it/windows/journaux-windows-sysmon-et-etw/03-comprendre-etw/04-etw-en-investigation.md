---
title: ETW en investigation
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Comprendre ETW
  - index.md
---

## 8. ETW pour le DFIR — démarche d'investigation

```
Identify Hunting Hypothesis
           ↓
Find Relevant ETW Providers
           ↓
Inspect Existing ETW Sessions
           ↓
Configure Event Collection
           ↓
Capture / Consume ETW Events
           ↓
Filter & Correlate Telemetry
           ↓
Validate Suspicious Behavior
           ↓
DFIR Investigation
```


### Points de vigilance

- Collection Scope : seuls les événements générés et effectivement collectés sont exploitables.
- Performance : certains providers peuvent générer un volume très important de données.
- Buffer Loss : des pertes de buffers peuvent entraîner une télémétrie incomplète.
- Visibility : tous les événements ETW ne sont pas présents dans les Windows Event Logs.
- Provider Configuration : les mots-clés, niveaux et filtres déterminent la couverture.
- Restricted Access : certains fournisseurs nécessitent des autorisations spécifiques.

## 9. Synthèse — ETW ou Sysmon

| Critère       | ETW                                                                   | Sysmon                                                    |
| ------------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| Nature        | Infrastructure native de tracing Windows                              | Outil de surveillance Microsoft Sysinternals              |
| Sources       | Très nombreux fournisseurs système et applicatifs                     | Catégories d'événements prises en charge par Sysmon       |
| Collecte      | Sessions ETW configurables                                            | Règles de configuration Sysmon                            |
| Stockage      | ETL, consommation temps réel ou événements publiés dans des journaux  | Windows Event Logs, principalement Sysmon/Operational     |
| Investigation | Accès à une télémétrie spécialisée et potentiellement très granulaire | Recherche d'activités système courantes en Threat Hunting |
| Limites       | Complexité, volume, restrictions d'accès                              | Visibilité limitée aux événements surveillés par Sysmon   |

L'idée centrale de cette section : ETW constitue une infrastructure de télémétrie Windows beaucoup plus vaste que les seuls événements affichés dans Event Viewer ou enregistrés par Sysmon.

En comprenant les Providers, Controllers, Sessions et Consumers, un analyste peut rechercher de nouvelles sources d'événements, configurer une collecte adaptée et améliorer ses capacités de détection face aux attaques que la télémétrie Sysmon seule pourrait ne pas mettre en évidence.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
