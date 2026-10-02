---
title: PowerShell
source: IT/02 Windows/Ligne de commande/PowerShell.md
format: cours
revue: '2026-08-21'
---

*De zéro à l'automatisation, l'Active Directory et la cybersécurité — Guide pour débutant absolu*

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

1. [PowerShell dans l'écosystème Windows](01-partie-i-fondamentaux-powershell-pour-administrer/01-chapitre-1-powershell-dans-l-ecosysteme-windows.md)
2. [Variables, types et informations système](01-partie-i-fondamentaux-powershell-pour-administrer/02-chapitre-2-variables-types-et-informations-systeme.md)
3. [Paramètres et scripts administrables](01-partie-i-fondamentaux-powershell-pour-administrer/03-chapitre-3-parametres-et-scripts-administrables.md)
4. [Le pipeline et les objets : le concept fondamental](01-partie-i-fondamentaux-powershell-pour-administrer/04-chapitre-4-le-pipeline-et-les-objets.md)
5. [Opérateurs et conditions](01-partie-i-fondamentaux-powershell-pour-administrer/05-chapitre-5-operateurs-et-conditions.md)
6. [Collections, hashtables et boucles](01-partie-i-fondamentaux-powershell-pour-administrer/06-chapitre-6-collections-hashtables-et-boucles.md)
7. [Fonctions et scripts structurés](01-partie-i-fondamentaux-powershell-pour-administrer/07-chapitre-7-fonctions-et-scripts-structures.md)
8. [Gestion des erreurs et débogage](01-partie-i-fondamentaux-powershell-pour-administrer/08-chapitre-8-gestion-des-erreurs-et-debogage.md)

**PARTIE II — ADMINISTRATION WINDOWS LOCALE**

9. [Fichiers, dossiers et permissions NTFS](02-partie-ii-administration-windows-locale/01-chapitre-9-fichiers-dossiers-et-permissions-ntfs.md)
10. [Utilisateurs et groupes locaux](02-partie-ii-administration-windows-locale/02-chapitre-10-utilisateurs-et-groupes-locaux.md)
11. [Processus et services](02-partie-ii-administration-windows-locale/03-chapitre-11-processus-et-services.md)
12. [Le registre Windows](02-partie-ii-administration-windows-locale/04-chapitre-12-le-registre-windows.md)
13. [Tâches planifiées](02-partie-ii-administration-windows-locale/05-chapitre-13-taches-planifiees.md)
14. [Disques, volumes et stockage](02-partie-ii-administration-windows-locale/06-chapitre-14-disques-volumes-et-stockage.md) · [Rôles, fonctionnalités et logiciels](02-partie-ii-administration-windows-locale/06-chapitre-14-disques-volumes-et-stockage.md#roles-fonctionnalites-et-logiciels)

**PARTIE III — ADMINISTRATION RÉSEAU WINDOWS**

15. [Interfaces et configuration IP](03-partie-iii-administration-reseau-windows/01-chapitre-15-interfaces-et-configuration-ip.md)
16. [DNS client et résolution](03-partie-iii-administration-reseau-windows/02-chapitre-16-dns-client-et-resolution.md)
17. [Routage et connexions](03-partie-iii-administration-reseau-windows/03-chapitre-17-routage-et-connexions.md)
18. [Pare-feu Windows](03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md)

**PARTIE IV — ADMINISTRATION ACTIVE DIRECTORY**

19. [Comprendre Active Directory](04-partie-iv-administration-active-directory/01-chapitre-19-comprendre-active-directory.md)
20. [Utilisateurs AD](04-partie-iv-administration-active-directory/02-chapitre-20-utilisateurs-ad.md)
21. [Groupes AD](04-partie-iv-administration-active-directory/03-chapitre-21-groupes-ad.md)
22. [Ordinateurs et unités d'organisation](04-partie-iv-administration-active-directory/04-chapitre-22-ordinateurs-et-unites-d-organisation.md)
23. [Recherche et filtrage AD](04-partie-iv-administration-active-directory/05-chapitre-23-recherche-et-filtrage-ad.md)
24. [Administration en masse avec CSV](04-partie-iv-administration-active-directory/06-chapitre-24-administration-en-masse-avec-csv.md)

**PARTIE V — GPO ET SERVICES WINDOWS SERVER**

25. [Group Policy (GPO)](05-partie-v-gpo-et-services-windows-server/01-chapitre-25-group-policy-gpo.md)
26. [DNS Server](05-partie-v-gpo-et-services-windows-server/02-chapitre-26-dns-server.md)
27. [DHCP Server](05-partie-v-gpo-et-services-windows-server/03-chapitre-27-dhcp-server.md)
28. [File Server et partages SMB](05-partie-v-gpo-et-services-windows-server/04-chapitre-28-file-server-et-partages-smb.md)

**PARTIE VI — ADMINISTRATION DISTANTE, API ET AUTOMATISATION**

29. [PowerShell Remoting](06-partie-vi-administration-distante-api-et-automatis/01-chapitre-29-powershell-remoting.md)
30. [Authentification, autorisation et tokens](06-partie-vi-administration-distante-api-et-automatis/02-chapitre-30-authentification-autorisation-et-token.md)
31. [API REST avec PowerShell](06-partie-vi-administration-distante-api-et-automatis/03-chapitre-31-api-rest-avec-powershell.md)
32. [Microsoft Graph et Entra ID](06-partie-vi-administration-distante-api-et-automatis/04-chapitre-32-microsoft-graph-et-entra-id.md)

**PARTIE VII — AUTOMATISATION ET INDUSTRIALISATION**

33. [Industrialiser ses scripts](07-partie-vii-automatisation-et-industrialisation/01-chapitre-33-industrialiser-ses-scripts.md)

**PARTIE VIII — POWERSHELL POUR LA CYBERSÉCURITÉ**

34. [Diagnostic, logs et triage](08-partie-viii-powershell-pour-la-cybersecurite/01-chapitre-34-diagnostic-logs-et-triage.md)
35. [Sécurité de l'exécution et durcissement](08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md)

**ANNEXES**

---

## Sommaire

- [Partie I — Fondamentaux PowerShell pour administrer Windows](01-partie-i-fondamentaux-powershell-pour-administrer/index.md)
    - [Chapitre 1 — PowerShell dans l'écosystème Windows](01-partie-i-fondamentaux-powershell-pour-administrer/01-chapitre-1-powershell-dans-l-ecosysteme-windows.md)
    - [Chapitre 2 — Variables, types et informations système](01-partie-i-fondamentaux-powershell-pour-administrer/02-chapitre-2-variables-types-et-informations-systeme.md)
    - [Chapitre 3 — Paramètres et scripts administrables](01-partie-i-fondamentaux-powershell-pour-administrer/03-chapitre-3-parametres-et-scripts-administrables.md)
    - [Chapitre 4 — Le pipeline et les objets](01-partie-i-fondamentaux-powershell-pour-administrer/04-chapitre-4-le-pipeline-et-les-objets.md)
    - [Chapitre 5 — Opérateurs et conditions](01-partie-i-fondamentaux-powershell-pour-administrer/05-chapitre-5-operateurs-et-conditions.md)
    - [Chapitre 6 — Collections, hashtables et boucles](01-partie-i-fondamentaux-powershell-pour-administrer/06-chapitre-6-collections-hashtables-et-boucles.md)
    - [Chapitre 7 — Fonctions et scripts structurés](01-partie-i-fondamentaux-powershell-pour-administrer/07-chapitre-7-fonctions-et-scripts-structures.md)
    - [Chapitre 8 — Gestion des erreurs et débogage](01-partie-i-fondamentaux-powershell-pour-administrer/08-chapitre-8-gestion-des-erreurs-et-debogage.md)
- [Partie II — Administration Windows locale](02-partie-ii-administration-windows-locale/index.md)
    - [Chapitre 9 — Fichiers, dossiers et permissions NTFS](02-partie-ii-administration-windows-locale/01-chapitre-9-fichiers-dossiers-et-permissions-ntfs.md)
    - [Chapitre 10 — Utilisateurs et groupes locaux](02-partie-ii-administration-windows-locale/02-chapitre-10-utilisateurs-et-groupes-locaux.md)
    - [Chapitre 11 — Processus et services](02-partie-ii-administration-windows-locale/03-chapitre-11-processus-et-services.md)
    - [Chapitre 12 — Le registre Windows](02-partie-ii-administration-windows-locale/04-chapitre-12-le-registre-windows.md)
    - [Chapitre 13 — Tâches planifiées](02-partie-ii-administration-windows-locale/05-chapitre-13-taches-planifiees.md)
    - [Chapitre 14 — Disques, volumes et stockage](02-partie-ii-administration-windows-locale/06-chapitre-14-disques-volumes-et-stockage.md)
- [Partie III — Administration réseau Windows](03-partie-iii-administration-reseau-windows/index.md)
    - [Chapitre 15 — Interfaces et configuration IP](03-partie-iii-administration-reseau-windows/01-chapitre-15-interfaces-et-configuration-ip.md)
    - [Chapitre 16 — DNS client et résolution](03-partie-iii-administration-reseau-windows/02-chapitre-16-dns-client-et-resolution.md)
    - [Chapitre 17 — Routage et connexions](03-partie-iii-administration-reseau-windows/03-chapitre-17-routage-et-connexions.md)
    - [Chapitre 18 — Pare-feu Windows](03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md)
- [Partie IV — Administration active directory](04-partie-iv-administration-active-directory/index.md)
    - [Chapitre 19 — Comprendre Active Directory](04-partie-iv-administration-active-directory/01-chapitre-19-comprendre-active-directory.md)
    - [Chapitre 20 — Utilisateurs AD](04-partie-iv-administration-active-directory/02-chapitre-20-utilisateurs-ad.md)
    - [Chapitre 21 — Groupes AD](04-partie-iv-administration-active-directory/03-chapitre-21-groupes-ad.md)
    - [Chapitre 22 — Ordinateurs et unités d'organisation](04-partie-iv-administration-active-directory/04-chapitre-22-ordinateurs-et-unites-d-organisation.md)
    - [Chapitre 23 — Recherche et filtrage AD](04-partie-iv-administration-active-directory/05-chapitre-23-recherche-et-filtrage-ad.md)
    - [Chapitre 24 — Administration en masse avec CSV](04-partie-iv-administration-active-directory/06-chapitre-24-administration-en-masse-avec-csv.md)
- [Partie V — GPO et services Windows server](05-partie-v-gpo-et-services-windows-server/index.md)
    - [Chapitre 25 — Group Policy (GPO)](05-partie-v-gpo-et-services-windows-server/01-chapitre-25-group-policy-gpo.md)
    - [Chapitre 26 — DNS Server](05-partie-v-gpo-et-services-windows-server/02-chapitre-26-dns-server.md)
    - [Chapitre 27 — DHCP Server](05-partie-v-gpo-et-services-windows-server/03-chapitre-27-dhcp-server.md)
    - [Chapitre 28 — File Server et partages SMB](05-partie-v-gpo-et-services-windows-server/04-chapitre-28-file-server-et-partages-smb.md)
- [Partie VI — Administration distante, API et automatisation](06-partie-vi-administration-distante-api-et-automatis/index.md)
    - [Chapitre 29 — PowerShell Remoting](06-partie-vi-administration-distante-api-et-automatis/01-chapitre-29-powershell-remoting.md)
    - [Chapitre 30 — Authentification, autorisation et tokens](06-partie-vi-administration-distante-api-et-automatis/02-chapitre-30-authentification-autorisation-et-token.md)
    - [Chapitre 31 — API REST avec PowerShell](06-partie-vi-administration-distante-api-et-automatis/03-chapitre-31-api-rest-avec-powershell.md)
    - [Chapitre 32 — Microsoft Graph et Entra ID](06-partie-vi-administration-distante-api-et-automatis/04-chapitre-32-microsoft-graph-et-entra-id.md)
- [Partie VII — Automatisation et industrialisation](07-partie-vii-automatisation-et-industrialisation/index.md)
    - [Chapitre 33 — Industrialiser ses scripts](07-partie-vii-automatisation-et-industrialisation/01-chapitre-33-industrialiser-ses-scripts.md)
- [Partie VIII — PowerShell pour la cybersécurité](08-partie-viii-powershell-pour-la-cybersecurite/index.md)
    - [Chapitre 34 — Diagnostic, logs et triage](08-partie-viii-powershell-pour-la-cybersecurite/01-chapitre-34-diagnostic-logs-et-triage.md)
    - [Chapitre 35 — Sécurité de l'exécution et durcissement](08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md)
- [Annexes](09-annexes.md)
