---
title: PowerShell
source: IT/02_Windows/Powershell.md
chapters: 8
---

### De zéro à l'automatisation, l'Active Directory et la cybersécurité — Guide pour débutant absolu

---

> **Prérequis :** Aucun en PowerShell ni en programmation. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une ligne de script.
> Il t'apprend PowerShell **en administrant Windows** : chaque notion du langage est introduite à travers un vrai cas d'administration.

---

### Ce que ce cours est — et ce qu'il n'est pas

Ce cours t'apprend à **piloter et automatiser un environnement Windows avec PowerShell**, du poste local jusqu'à l'Active Directory, les GPO, l'administration distante et les API.

L'idée directrice tient en une phrase :

> **On n'apprend pas PowerShell puis l'administration. On apprend PowerShell EN administrant.**

À la fin, tu ne diras pas seulement « je sais écrire quelques scripts ». Tu diras : « je comprends PowerShell et son pipeline objet ; je sais administrer un poste ou un serveur Windows — services, processus, fichiers, permissions, utilisateurs, tâches, registre, réseau ; automatiser Active Directory ; comprendre et manipuler des GPO ; administrer plusieurs machines à distance ; interroger une API REST et Microsoft Graph ; produire des scripts robustes ; et utiliser tout ça comme base pour le diagnostic et la cybersécurité Windows. »

Ce cours **n'est pas** :

- un cours complet d'Active Directory, de Windows Server, de réseau ou de GPO (ce sont des cours à part entière ; ici, **PowerShell reste le fil rouge** et on apprend à *piloter* ces technologies)
- un cours de développement .NET
- un cours de cybersécurité offensive (la partie sécurité est **défensive** : diagnostic, triage, durcissement)

Le niveau final visé est **junior solide / intermédiaire débutant** en administration Windows PowerShell — pas expert Microsoft. Le cours te donne les fondations pour approfondir ensuite séparément AD, Windows Server, Entra ID, la cybersécurité Windows, etc.

---

### Guide de lecture

Chaque chapitre est organisé en trois niveaux. Tu peux suivre le parcours principal (🟢 + 🟡) et revenir aux 🔴 plus tard.

| Section | Niveau | Objectif |
|---------|--------|----------|
| **🟢 Le minimum à savoir** | Essentiel | Ce qu'il faut absolument comprendre |
| **🟡 Très utile en pratique** | Opérationnel | Ce qui te rend efficace en administration réelle |
| **🔴 Bonus / avancé** | Approfondissement | À connaître, mais tu peux y revenir plus tard |

Deux **réflexes** sont martelés dans tout le cours — ce sont les meilleures habitudes qu'un débutant puisse prendre :

> **Réflexe n°1 — Explorer avec `Get-Member`.** Chaque fois que tu récupères un objet que tu ne connais pas, passe-le dans `Get-Member` pour voir ses propriétés et méthodes. Tu ne mémorises pas PowerShell : tu l'explores.

> **Réflexe n°2 — `Get`/`Test` avant `Set`/`New`/`Remove`.** On regarde toujours avant de modifier. On lit l'état actuel, on teste, *puis* on change — et plus tard, on utilise `-WhatIf`, `-Confirm` et des sauvegardes. C'est la discipline de base de l'administrateur.

#### Parcours recommandés

| Parcours | Chapitres | Objectif |
|----------|-----------|----------|
| **🎯 Fondamentaux & poste local** | Parties I-II (Ch.1-14) | Être autonome sur un poste Windows, comprendre PowerShell |
| **🔧 Administrateur Windows** | Parties I-VI (Ch.1-31) | Administrer postes, serveurs, réseau, AD, GPO, à distance |
| **🚀 Complet** | Tout | + industrialisation et cybersécurité |

---

### Environnement de lab recommandé

PowerShell fonctionne partout, mais **toutes les cmdlets ne sont pas disponibles partout**. Voici ce dont tu as besoin selon la partie du cours.

| Parties | Ce que tu administres | Environnement suffisant |
|---------|----------------------|------------------------|
| **I → III** (Ch.1-18) | Poste local, réseau du poste | **Windows 10 ou 11** (ce que tu as déjà) |
| **IV → V** (Ch.19-28) | Active Directory, GPO, DNS/DHCP/SMB serveur | **Une VM Windows Server** (contrôleur de domaine) |
| **VI** (Ch.29-34) | Machines distantes, API | Idéalement 2 machines (un client + un serveur) |

**Le lab idéal (facultatif mais recommandé pour les parties IV+) :** trois machines virtuelles sur ton PC (avec VirtualBox, VMware Workstation, ou Hyper-V) :

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    DC01     │     │    SRV01    │     │  CLIENT01   │
│ Windows Srv │     │ Windows Srv │     │ Windows 10  │
│ Contrôleur  │     │ Serveur     │     │ Poste       │
│ de domaine  │     │ membre      │     │ client      │
│ AD/DNS/DHCP │     │ Fichiers    │     │ RSAT        │
└─────────────┘     └─────────────┘     └─────────────┘
        └──────── domaine lab.local ────────┘
```

> **Important :** ce cours n'est **pas** un tutoriel d'installation de lab (monter un domaine AD est un sujet à part entière). Mais garde en tête cette distinction : si tu tapes `Get-ADUser` sur ton Windows 11 personnel sans domaine ni RSAT, ça ne marchera pas — et c'est normal. Chaque chapitre te signale l'environnement et les droits nécessaires.

**Windows PowerShell 5.1 vs PowerShell 7 :** les deux coexistent (on détaille au Ch.1). Pour la majorité de ce cours, la version intégrée à Windows (5.1) suffit. Les rares points spécifiques à PowerShell 7 sont signalés par le marqueur `[⚡ PS7+]`. Les opérations nécessitant des droits administrateur sont signalées par `[🔑 Admin]`, et celles spécifiques à Windows Server par `[🖥️ Server]`.

---

### Comment lire une commande PowerShell

Pour chaque cmdlet importante, ce cours répond systématiquement à ces questions — c'est le canevas mental à adopter :

1. **Que fait-elle ?** (son rôle)
2. **Que retourne-t-elle ?** (rien à l'écran ≠ rien du tout — souvent un objet)
3. **Quel type d'objet ?** (pour savoir quoi en faire ensuite — d'où le réflexe `Get-Member`)
4. **Quelles propriétés sont utiles ?**
5. **Pourquoi un admin l'utilise ?**
6. **Quand l'éviter ?**
7. **Quels droits / quelle version / client ou serveur ?**

---

### Glossaire — Les mots à connaître

Reviens ici dès qu'un terme te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **PowerShell** | Le shell moderne de Microsoft : terminal + langage de scripting + outil d'administration Windows |
| **Cmdlet** | Une commande PowerShell native, nommée `Verbe-Nom` (`Get-Service`, `New-ADUser`) |
| **Objet** | Une donnée structurée avec des **propriétés** (informations) et des **méthodes** (actions) |
| **Propriété** | Une information portée par un objet (le nom d'un service, son statut…) |
| **Méthode** | Une action qu'un objet sait faire (`.Stop()` sur un service) |
| **Pipeline** | Le `\|` qui envoie la sortie d'une commande dans la suivante — en PowerShell, ce sont des **objets** qui circulent, pas du texte |
| **Module** | Un ensemble de cmdlets regroupées (module `ActiveDirectory`, `DnsServer`…) |
| **Cmdlet vs commande externe** | Une cmdlet est native PowerShell ; `ping.exe` ou `ipconfig.exe` sont des exécutables externes appelables depuis PowerShell |
| **Variable** | Un conteneur nommé, préfixé par `$` (`$Service`, `$env:COMPUTERNAME`) |
| **Hashtable** | Une collection de paires clé-valeur (`@{ Nom = "SRV01" }`) — comme un dictionnaire Python |
| **PSCustomObject** | Un objet sur mesure que tu fabriques pour structurer des données (idéal pour les rapports) |
| **Script** | Un fichier `.ps1` contenant des commandes PowerShell |
| **Fonction** | Un bloc de code nommé et réutilisable, souvent lui aussi en `Verbe-Nom` |
| **Registre** | La base de données de configuration de Windows |
| **Service** | Un programme qui tourne en arrière-plan (pare-feu, spouleur d'impression…) |
| **Remoting** | L'exécution de commandes PowerShell sur des machines distantes (via WinRM) |
| **WinRM** | Windows Remote Management — le service qui permet le remoting |
| **AD (Active Directory)** | L'annuaire central d'un réseau Windows d'entreprise (utilisateurs, ordinateurs, groupes…) |
| **GPO (Group Policy Object)** | Un objet de stratégie qui applique des réglages à des utilisateurs/ordinateurs |
| **RSAT** | Remote Server Administration Tools — les modules qui ajoutent `Get-ADUser`, `Get-GPO`… sur un poste client |
| **API REST** | Une interface web qui permet à des programmes de dialoguer via HTTP (GET, POST…) et JSON |
| **CIM/WMI** | La couche d'instrumentation de Windows qui expose des centaines de classes d'infos système (`Get-CimInstance`) |

---

### Table des matières

**PARTIE I — FONDAMENTAUX POWERSHELL POUR ADMINISTRER WINDOWS**

1. [PowerShell dans l'écosystème Windows](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-1-powershell-dans-lecosysteme-windows)
2. [Variables, types et informations système](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-2-variables-types-et-informations-systeme)
3. [Paramètres et scripts administrables](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-3-parametres-et-scripts-administrables)
4. [Le pipeline et les objets : le concept fondamental](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-4-le-pipeline-et-les-objets)
5. [Opérateurs et conditions](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-5-operateurs-et-conditions)
6. [Collections, hashtables et boucles](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-6-collections-hashtables-et-boucles)
7. [Fonctions et scripts structurés](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-7-fonctions-et-scripts-structures)
8. [Gestion des erreurs et débogage](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md#chapitre-8-gestion-des-erreurs-et-debogage)

**PARTIE II — ADMINISTRATION WINDOWS LOCALE**

9. [Fichiers, dossiers et permissions NTFS](2-partie-ii-administration-windows-locale.md#chapitre-9-fichiers-dossiers-et-permissions-ntfs)
10. [Utilisateurs et groupes locaux](2-partie-ii-administration-windows-locale.md#chapitre-10-utilisateurs-et-groupes-locaux)
11. [Processus et services](2-partie-ii-administration-windows-locale.md#chapitre-11-processus-et-services)
12. [Le registre Windows](2-partie-ii-administration-windows-locale.md#chapitre-12-le-registre-windows)
13. [Tâches planifiées](2-partie-ii-administration-windows-locale.md#chapitre-13-taches-planifiees)
14. [Disques, volumes et stockage](2-partie-ii-administration-windows-locale.md#chapitre-14-disques-volumes-et-stockage) · [Rôles, fonctionnalités et logiciels](2-partie-ii-administration-windows-locale.md#roles-fonctionnalites-et-logiciels)

**PARTIE III — ADMINISTRATION RÉSEAU WINDOWS**

15. [Interfaces et configuration IP](3-partie-iii-administration-reseau-windows.md#chapitre-15-interfaces-et-configuration-ip)
16. [DNS client et résolution](3-partie-iii-administration-reseau-windows.md#chapitre-16-dns-client-et-resolution)
17. [Routage et connexions](3-partie-iii-administration-reseau-windows.md#chapitre-17-routage-et-connexions)
18. [Pare-feu Windows](3-partie-iii-administration-reseau-windows.md#chapitre-18-pare-feu-windows)

**PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY**

19. [Comprendre Active Directory](4-partie-iv-administration-active-directory.md#chapitre-19-comprendre-active-directory)
20. [Utilisateurs AD](4-partie-iv-administration-active-directory.md#chapitre-20-utilisateurs-ad)
21. [Groupes AD](4-partie-iv-administration-active-directory.md#chapitre-21-groupes-ad)
22. [Ordinateurs et unités d'organisation](4-partie-iv-administration-active-directory.md#chapitre-22-ordinateurs-et-unites-dorganisation)
23. [Recherche et filtrage AD](4-partie-iv-administration-active-directory.md#chapitre-23-recherche-et-filtrage-ad)
24. [Administration en masse avec CSV](4-partie-iv-administration-active-directory.md#chapitre-24-administration-en-masse-avec-csv)

**PARTIE V — GPO ET SERVICES WINDOWS SERVER**

25. [Group Policy (GPO)](5-partie-v-gpo-et-services-windows-server.md#chapitre-25-group-policy-gpo)
26. [DNS Server](5-partie-v-gpo-et-services-windows-server.md#chapitre-26-dns-server)
27. [DHCP Server](5-partie-v-gpo-et-services-windows-server.md#chapitre-27-dhcp-server)
28. [File Server et partages SMB](5-partie-v-gpo-et-services-windows-server.md#chapitre-28-file-server-et-partages-smb)

**PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION**

29. [PowerShell Remoting](6-partie-vi-administration-distante-api-et-automatisation.md#chapitre-29-powershell-remoting)
30. [Authentification, autorisation et tokens](6-partie-vi-administration-distante-api-et-automatisation.md#chapitre-30-authentification-autorisation-et-tokens)
31. [API REST avec PowerShell](6-partie-vi-administration-distante-api-et-automatisation.md#chapitre-31-api-rest-avec-powershell)
32. [Microsoft Graph et Entra ID](6-partie-vi-administration-distante-api-et-automatisation.md#chapitre-32-microsoft-graph-et-entra-id)

**PARTIE VII — AUTOMATISATION ET INDUSTRIALISATION**

33. [Industrialiser ses scripts](7-partie-vii-automatisation-et-industrialisation.md#chapitre-33-industrialiser-ses-scripts)

**PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ**

34. [Diagnostic, logs et triage](8-partie-viii-powershell-pour-la-cybersecurite.md#chapitre-34-diagnostic-logs-et-triage)
35. [Sécurité de l'exécution et durcissement](8-partie-viii-powershell-pour-la-cybersecurite.md#chapitre-35-securite-de-lexecution-et-durcissement)

**ANNEXES**

---

## Sommaire

1. [PARTIE I — FONDAMENTAUX POWERSHELL POUR ADMINISTRER WINDOWS](1-partie-i-fondamentaux-powershell-pour-administrer-windows.md)
2. [PARTIE II — ADMINISTRATION WINDOWS LOCALE](2-partie-ii-administration-windows-locale.md)
3. [PARTIE III — ADMINISTRATION RÉSEAU WINDOWS](3-partie-iii-administration-reseau-windows.md)
4. [PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY](4-partie-iv-administration-active-directory.md)
5. [PARTIE V — GPO ET SERVICES WINDOWS SERVER](5-partie-v-gpo-et-services-windows-server.md)
6. [PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION](6-partie-vi-administration-distante-api-et-automatisation.md)
7. [PARTIE VII — AUTOMATISATION ET INDUSTRIALISATION](7-partie-vii-automatisation-et-industrialisation.md)
8. [PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ](8-partie-viii-powershell-pour-la-cybersecurite.md)
