---
title: "Windows"
---
# Windows

[Énumération et audit local](fondamentaux/enumeration.md) — Parcours court : système, comptes, services, logiciels, réseau et protections.

Les commandes en PowerShell (et leur équivalent CMD quand il est courant), avec un exemple qui marche et l'étape suivante. Les blocs `powershell` se tapent dans PowerShell, les blocs `bat` dans l'invite de commandes.

## [Fondamentaux](fondamentaux/index.md)

Comprendre et observer le système.

- [Système et arborescence](fondamentaux/systeme.md) — Identifier la machine (version, build, correctifs, domaine), se repérer dans l'arborescence, savoir qui est connecté.
- [Fichiers et recherche](fondamentaux/fichiers-recherche.md) — Lire, trouver et comparer des fichiers ; chercher dans le contenu ; empreintes, signatures et flux alternatifs.
- [Processus et services](fondamentaux/processus.md) — Ligne de commande et parent d'un processus, arbre, DLL, arrêt ; services, svchost, permissions et mauvaises configurations.
- [Réseau](fondamentaux/reseau.md) — Adresses, routes, connexions par processus, test de port, DNS, partages, pare-feu.
- [Journaux et événements](fondamentaux/logs/index.md) — Filtrer les journaux, retrouver ouvertures de session, processus, services, scripts PowerShell ; exporter.
- [Droits et identités](fondamentaux/droits.md) — SID, groupes, privilèges, niveau d'intégrité ; lire et modifier les permissions NTFS.
- [Registre](fondamentaux/registre.md) — Lire et chercher dans le registre, voir ce qui se lance au démarrage, exporter avant de modifier.

## [🎯 Repérer une attaque](reperer-une-attaque/index.md)

Une fiche par attaque : les traces qu'elle laisse, les requêtes pour les retrouver, les faux positifs.

- [Repérer un DLL hijacking](reperer-une-attaque/reperer-un-dll-hijacking.md) — Sysmon `7`.
- [Repérer du PowerShell non managé](reperer-une-attaque/reperer-du-powershell-non-manage.md) — Sysmon `7` et `8`.
- [Repérer le chargement d'assemblies .NET](reperer-une-attaque/reperer-le-chargement-d-assemblies-net.md) — Sysmon `7` et ETW.
- [Repérer une relation parent-enfant anormale](reperer-une-attaque/reperer-une-relation-parent-enfant-anormale.md) — Sysmon `1`.
- [Démasquer un faux processus parent (PPID spoofing)](reperer-une-attaque/demasquer-un-faux-processus-parent-ppid-spoofing.md) — Sysmon `1` et ETW Kernel-Process.
- [Repérer un accès à LSASS](reperer-une-attaque/reperer-un-acces-a-lsass.md) — Sysmon `10`.

## [Administration](administration/index.md)

Modifier le système.

- [Utilisateurs et groupes](administration/utilisateurs.md) — Comptes et groupes locaux : créer, réinitialiser, désactiver, ajouter à un groupe.
- [Services et démarrage](administration/services.md) — Piloter un service, changer son démarrage, voir tout ce qui démarre avec la machine.
- [Tâches planifiées](administration/taches.md) — Lister, créer, désactiver une tâche ; voir quand elle a tourné.
- [Réseau et pare-feu](administration/reseau.md) — IP, DNS, fichier hosts, règles de pare-feu, désactivation de LLMNR, NetBIOS et SMBv1, bureau à distance.
- [Logiciels et mises à jour](administration/logiciels.md) — winget, correctifs, état et analyses de Defender.
- [Disques, archives et transferts](administration/disques.md) — Espace disque, BitLocker, zip, robocopy, copie vers une autre machine.
- [Active Directory au quotidien](administration/active-directory/index.md) — Comptes, verrouillages, groupes, OU et ordinateurs, LAPS, gMSA, GPO, Kerberos, santé des DC, contrôles d'hygiène.

Pour l'investigation, voir aussi [Artefacts Windows](../forensic/windows/artefacts/index.md).
