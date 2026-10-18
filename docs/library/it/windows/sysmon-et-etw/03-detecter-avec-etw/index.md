---
title: Détecter avec ETW
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - ../index.md
---

Event Tracing for Windows (ETW) permet d'obtenir une télémétrie plus détaillée que certains événements Sysmon afin d'investiguer des techniques d'attaque avancées.

Cette section présente deux scénarios de Threat Hunting :

- Détecter les relations parent-enfant étranges : détecter des relations anormales entre processus et le Parent PID Spoofing.
    
- Malicious .NET Assembly Loading : identifier le chargement et l'exécution d'assemblages .NET suspects.
    

L'objectif est de compléter les observations de Sysmon avec des informations provenant de fournisseurs ETW spécialisés.

## Dans cette partie

- [Repérer une relation parent-enfant anormale](01-reperer-une-relation-parent-enfant-anormale.md)
- [Démasquer un faux processus parent (PPID spoofing)](02-demasquer-un-faux-processus-parent-ppid-spoofing.md)
- [Repérer le chargement d'assemblies .NET](03-reperer-le-chargement-d-assemblies-net.md)
- [Aller plus loin avec le provider DotNETRuntime](04-aller-plus-loin-avec-le-provider-dotnetruntime.md)
