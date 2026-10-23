---
title: "Repérer une attaque"
---

# Repérer une attaque

Une fiche par attaque : les traces qu'elle laisse, les requêtes pour les retrouver, les faux positifs. Les étapes vont du plus large au plus précis : chacune se teste, puis s'affine.

Pour partir de ce qu'on a devant soi (un `.evtx`, une trace ETW, rien qui remonte) : [Journaux et événements › Par situation](../fondamentaux/logs/index.md#par-situation).
{ .kw-cs-top }

| Fiche | Événement | Indice clé |
|---|---|---|
| [**Repérer un DLL hijacking**](reperer-un-dll-hijacking.md) | Sysmon `7` — chargement d'image (Image Loaded) | DLL système chargée hors de `System32`, non signée, par un exécutable lui aussi hors de sa place |
| [**Repérer du PowerShell non managé**](reperer-du-powershell-non-manage.md) | Sysmon `7` — chargement d'image (Image Loaded) ; Sysmon `8` — CreateRemoteThread (l'injecteur) | `clr.dll` / `clrjit.dll` chargées par un processus natif qui n'utilise pas .NET |
| [**Repérer le chargement d'assemblies .NET**](reperer-le-chargement-d-assemblies-net.md) | Sysmon `7` (chargement de `clr.dll`, `mscoree.dll`) ; ETW : assemblies chargées, méthodes compilées | Un exécutable inconnu ou lancé depuis un dossier inhabituel initialise .NET |
| [**Repérer une relation parent-enfant anormale**](reperer-une-relation-parent-enfant-anormale.md) | Sysmon `1` — création de processus | Un parent qui n'a pas vocation à lancer cet enfant |
| [**Démasquer un faux processus parent (PPID spoofing)**](demasquer-un-faux-processus-parent-ppid-spoofing.md) | Sysmon `1` (parent apparent) ; ETW Kernel-Process (processus créateur réel) | Le parent affiché par Sysmon n'est pas le processus qui a créé l'enfant |
| [**Repérer un accès à LSASS**](reperer-un-acces-a-lsass.md) | Sysmon `10` — accès à un processus (ProcessAccess) | Un exécutable inhabituel, lancé depuis un dossier utilisateur, qui ouvre `lsass.exe` |

Les fiches viennent de mes notes (`IT/02 Windows/Repérer une attaque/`) ; les commandes de lecture et de filtrage sont dans [Journaux et événements](../fondamentaux/logs/index.md), les mécanismes dans le cours [Sysmon et ETW](../../../library/it/windows/sysmon-et-etw/index.md).
{ .kw-cs-meta }
