---
title: "Artefacts Windows"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
besoin: "Retrouver ce qui s'est passé sur un poste Windows (artefacts)"
---
# Artefacts Windows

Windows garde la trace de ce qu'on y exécute, ouvre, branche et supprime, souvent sans que l'utilisateur le
sache. Pour chaque artefact : où il se trouve, ce qu'il dit, ce qu'il ne prouve pas, et la commande pour le
lire. Les outils cités sont ceux d'Eric Zimmerman (EZ Tools, gratuits) : chacun produit un CSV à ouvrir
dans Timeline Explorer.

Les incontournables : `KAPE` · `PECmd` · `AmcacheParser` · `LECmd` · `SBECmd` · `EvtxECmd` · `Get-WinEvent`
{ .kw-cs-top }

Les incontournables : `KAPE` · `PECmd` · `AmcacheParser` · `LECmd` · `SBECmd` · `EvtxECmd` · `Get-WinEvent`
{ .kw-cs-top }

## Quelle question, quel artefact

| Je veux savoir… | Artefacts à lire | Ce qu'ils ne prouvent pas seuls |
|---|---|---|
| Ce qui a été [**exécuté**](execution.md) | Prefetch, BAM, Amcache, ShimCache, SRUM, événement 4688 | Amcache et ShimCache montrent qu'un exécutable était présent, pas toujours qu'il a tourné |
| Ce qui a été [**ouvert**](fichiers-ouverts.md) | LNK, Jump Lists, RecentDocs, Shellbags | Le contenu du fichier : seulement son nom, son chemin et des dates |
| Quels [**périphériques USB**](usb.md) | USBSTOR, `setupapi.dev.log`, MountedDevices, MountPoints2 | Ce qui a été copié : il faut croiser avec LNK et Shellbags |
| Qui s'est [**connecté**](connexions.md), et comment | Journal Security (4624, 4625, 4672), RDP reçu (1149, 261, 21, 24, 25) et émis (1102, 4648, registre du client RDP) | L'identité réelle derrière un compte partagé ou volé |
| Ce qui a été [**supprimé**](suppressions.md) | Corbeille (`$I`, `$R`), clichés instantanés (VSS) | Un effacement sécurisé, ou une suppression sans passer par la corbeille |
| Ce qui [**se relance**](persistance.md) au démarrage | Clés Run, services (7045), tâches planifiées, abonnements WMI | Une persistance purement en mémoire |
| Qui a **parlé au réseau** | SRUM (octets par application), profils réseau, journaux du pare-feu | Le contenu des échanges |

## Collecter avant d'analyser

### Récupérer les artefacts d'un coup

Les ruches du registre et les journaux sont verrouillés quand Windows tourne : un simple copier-coller
échoue. KAPE (ou FTK Imager) les copie en lecture brute, avec leurs dates.

```powershell title="Commande"
kape.exe --tsource C: --tdest <dossier_collecte> --target KapeTriage   # copie les artefacts courants en lecture brute
```

```powershell title="Exemple"
kape.exe --tsource C: --tdest E:\collecte\PC-COMPTA-07 --target KapeTriage --vhdx PC-COMPTA-07
```

??? example "Sortie"
    ```text
    KAPE version 1.3.0.2 Author: Eric Zimmerman
    Found 312 targets. Found 31 Compound Targets.
    Target 'KapeTriage' with Id '…' found. Executing…
    Copied 1 742 files (1.38 GB) in 94.2 seconds. Total execution time: 101.6 seconds
    ```

```text title="Où sont les ruches du registre"
C:\Windows\System32\config\SYSTEM, SOFTWARE, SAM, SECURITY          # ruches machine
C:\Users\<utilisateur>\NTUSER.DAT                                   # ruche de l'utilisateur
C:\Users\<utilisateur>\AppData\Local\Microsoft\Windows\UsrClass.dat # Shellbags de l'utilisateur
```

!!! warning "Attention"
    Collecter sur un support externe, et noter l'heure UTC de début. Chaque outil lancé sur la machine laisse
    lui-même des traces (Prefetch, événements) : les consigner dans le journal d'intervention.

## Par question

- [Exécution](execution.md) — ce qui a été lancé : Prefetch, BAM, Amcache, ShimCache, SRUM.
- [Fichiers et dossiers ouverts](fichiers-ouverts.md) — LNK, Jump Lists, Shellbags, saisies de l'utilisateur.
- [Périphériques USB](usb.md) — clés branchées, numéros de série, dates.
- [Suppressions](suppressions.md) — corbeille, clichés instantanés.
- [Connexions et RDP](connexions.md) — ouvertures de session, bureau à distance reçu et émis.
- [Persistance](persistance.md) — ce qui se relance tout seul.
