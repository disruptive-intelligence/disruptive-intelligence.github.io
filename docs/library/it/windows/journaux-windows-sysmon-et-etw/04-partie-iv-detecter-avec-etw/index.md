---
title: Partie IV — Détecter avec ETW
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
---

Event Tracing for Windows (ETW) permet d'obtenir une télémétrie plus détaillée que certains événements Sysmon afin d'investiguer des techniques d'attaque avancées.

Cette section présente deux scénarios de Threat Hunting :

- Détecter les relations parent-enfant étranges : détecter des relations anormales entre processus et le Parent PID Spoofing.
    
- Malicious .NET Assembly Loading : identifier le chargement et l'exécution d'assemblages .NET suspects.
    

L'objectif est de compléter les observations de Sysmon avec des informations provenant de fournisseurs ETW spécialisés.

## Dans cette partie

- [Chapitre 13 — Repérer une relation parent-enfant anormale](01-chapitre-13-reperer-une-relation-parent-enfant-ano.md)
- [Chapitre 14 — Démasquer un faux processus parent (PPID spoofing)](02-chapitre-14-demasquer-un-faux-processus-parent-ppi.md)
- [Chapitre 15 — Repérer le chargement d'assemblies .NET](03-chapitre-15-reperer-le-chargement-d-assemblies-net.md)
- [Chapitre 16 — Aller plus loin avec le provider DotNETRuntime](04-chapitre-16-aller-plus-loin-avec-le-provider-dotne.md)
