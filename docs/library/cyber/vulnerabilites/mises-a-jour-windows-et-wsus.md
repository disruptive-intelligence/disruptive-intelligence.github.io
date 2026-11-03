---
title: Mises à jour Windows et WSUS
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Mises à jour Windows et WSUS.md
format: cours
revue: '2026-11-03'
---

Tous les termes qu'on croise en gestion des correctifs Microsoft, ce qu'ils désignent, comment les pièces
s'emboîtent, et comment WSUS fonctionne de l'intérieur : des versions de Windows (24H2, 25H2…) jusqu'à la
maintenance d'un serveur WSUS, avec un glossaire en fin de page.

---

## 1. Les versions de Windows

### Édition, version, build : trois choses différentes

| Terme | Exemple | Ce que ça désigne |
|---|---|---|
| **Produit** | Windows 11, Windows Server 2025 | la famille |
| **Édition** | Famille, Professionnel, **Entreprise**, Éducation, LTSC ; Server Standard / Datacenter | les fonctions et la licence |
| **Version** | **24H2**, **25H2** | la « mouture » annuelle, qui reçoit des fonctions nouvelles |
| **Build** | 26200 | le numéro de compilation de cette version |
| **Révision (UBR)** | 26200.**7019** | le niveau de correctifs : augmente à chaque cumulative |

Numéro complet : `10.0.26200.7019`. Le « 10.0 » est resté depuis Windows 10, même sous Windows 11 (compatibilité des applications) ; c'est le **build** qui distingue les versions.

La version de Windows s'affiche généralement sous la forme `Majeure.Mineure.Build.UBR` (par exemple : `10.0.22631.3447` où `3447` est l'UBR)

```powershell
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object ProductName, DisplayVersion, CurrentBuild, UBR
winver          # la fenêtre « À propos de Windows »
```


> Piège connu : `ProductName` affiche encore « Windows 10 » sur beaucoup de Windows 11. Le build fait foi :
> **≥ 22000 = Windows 11**.

### Que veut dire « 25H2 » ?

**AA H n** = année + semestre (*half*) : **25H2** = version du **second semestre 2025**. Le « H » vient de
*Half*. Microsoft a adopté ce format en 2020 ; avant, c'était **AAMM** (année + mois prévu) :

| Époque | Versions | Rythme |
|---|---|---|
| Windows 10, 2015-2020 | 1507, 1511, 1607, 1703, 1709, 1803, 1809, 1903, 1909, 2004 | deux par an |
| Windows 10, 2020-2022 | 20H2, 21H1, 21H2, **22H2** (dernière) | deux puis une par an |
| Windows 11 | 21H2, 22H2, 23H2, **24H2**, **25H2**, 26H2 | **une par an**, au second semestre |

### Les builds de Windows 11

| Version | Build | Note |
|---|---|---|
| 21H2 | 22000 | première version |
| 22H2 | 22621 | |
| 23H2 | 22631 | 22H2 + enablement package |
| **24H2** | **26100** | nouveau socle (« Germanium »), le même que Windows Server 2025 |
| **25H2** | **26200** | 24H2 + enablement package : **mêmes cumulatives** |
| 26H1 | 28000 | réservée aux nouveaux PC (puces Arm récentes), pas une mise à jour des PC existants |
| 26H2 | 26300 | en *Release Preview* depuis fin août 2026, par enablement package depuis 24H2 / 25H2 : vérifie son statut sur *Windows release health* |

**Enablement package** (*eKB*) : tout petit paquet (quelques centaines de Ko) qui **active** des fonctions déjà
présentes, en sommeil, dans les cumulatives de la version précédente. Un seul redémarrage, et la version change
(24H2 → 25H2). Possible seulement quand les deux versions partagent le même socle. Sinon il faut une **mise à
niveau complète** (réinstallation sur place, 1 h, plusieurs Go) : 23H2 → 24H2 par exemple.

### Windows Server

| Version | Build | Canal |
|---|---|---|
| Windows Server 2016 | 14393 | LTSC (SSU encore séparées) |
| Windows Server 2019 | 17763 | LTSC |
| Windows Server 2022 | 20348 | LTSC |
| **Windows Server 2025** | **26100** | LTSC ; dans WSUS : produit **« Microsoft Server Operating System-24H2 »** |

Server 2025 et Windows 11 24H2 partagent le socle 26100 : des cumulatives distinctes, mais publiées le même jour,
avec des correctifs très proches.

---

## 2. Le cycle de vie

Une version de Windows reçoit des correctifs pendant une durée **fixée à l'avance**. Après : plus aucun correctif
de sécurité, la machine devient une dette.

| Produit | Durée de support | Remarque |
|---|---|---|
| Windows 11 Famille / Pro (version annuelle) | **24 mois** | il faut changer de version tous les 2 ans au plus |
| Windows 11 **Entreprise** / Éducation | **36 mois** | d'où une mise à niveau annuelle ou tous les deux ans en entreprise |
| Windows 11 Entreprise **LTSC** 2024 | 5 ans (IoT : 10 ans) | pas de nouvelles fonctions, pour les systèmes figés (industrie, santé) |
| Windows Server (LTSC) | 5 ans standard + 5 ans étendu | Server 2016 : fin du support étendu en **janvier 2027** |
| Windows 10 | fin le **14 octobre 2025** | puis **ESU** (*Extended Security Updates*) payantes, jusqu'à 3 ans pour les organisations |

Conséquence pour WSUS : une machine en **version non supportée** ne reçoit plus de cumulative ; elle apparaîtra
« à jour » (rien d'applicable) alors qu'elle est vulnérable. Le rapport de conformité doit donc toujours être
croisé avec la **version** de chaque machine.

```powershell
# dans WSUS : versions présentes dans le parc
(Get-WsusServer).GetComputerTargets() | Group-Object OSDescription, ClientVersion | Select-Object Count, Name
```


---

## 3. KB, CVE, bulletins

| Terme | Exemple | Ce que c'est |
|---|---|---|
| **KB** (*Knowledge Base*) | KB5043080 | Numéro de l'**article de support** Microsoft qui décrit un paquet de mise à jour. Par extension : la mise à jour elle-même (« la KB du mois »). Une KB par paquet ; la même KB peut exister pour plusieurs architectures |
| **CVE** (*Common Vulnerabilities and Exposures*) | CVE-2025-59287 | Identifiant **universel** d'une vulnérabilité. Une cumulative corrige des dizaines de CVE |
| **CVSS** | 9.8 | Note de gravité technique (0 à 10) d'une CVE |
| **Gravité MSRC** | Critique, Important, Modéré, Faible | Note de Microsoft ; visible dans WSUS (*MsrcSeverity*) |
| **Exploited / Publicly disclosed** | *Yes* | La faille est-elle déjà **exploitée**, ou ses détails **publics** ? Le critère n°1 pour accélérer |
| **Security Update Guide** | msrc.microsoft.com/update-guide | Base officielle : CVE ↔ produits ↔ KB |
| **Release notes** du mois | « November 2026 Security Updates » | Récapitulatif du Patch Tuesday |
| **KEV** (CISA) | *Known Exploited Vulnerabilities* | Catalogue américain des failles exploitées : la référence pour prioriser |
| **Avis CERT-FR** | « Multiples vulnérabilités dans les produits Microsoft » | Avis français publié le soir du Patch Tuesday |

Dans WSUS, une mise à jour est identifiée par un **UpdateID** (GUID) et un **numéro de révision** : Microsoft
peut republier une mise à jour (métadonnées corrigées) sans changer de KB. C'est la « révision » que l'assistant de
nettoyage supprime quand elle est obsolète.

**Lire une page KB** : *Summary* (ce qui est corrigé), *Improvements*, **Known issues** (problèmes connus, à lire
avant chaque déploiement), *How to get this update* (WU, WSUS, catalogue), *File information*.

---

## 4. Les deux grandes familles

| | **Mise à jour de fonctionnalités** (*feature update*) | **Mise à jour de qualité** (*quality update*) |
|---|---|---|
| Change | la **version** (24H2 → 25H2) | le **niveau de correctifs** (UBR) |
| Rythme | annuel | mensuel (+ urgences) |
| Taille / durée | quelques Ko (eKB) à plusieurs Go (mise à niveau), 30 à 90 min | quelques centaines de Mo, 10 à 30 min |
| Contenu | fonctions nouvelles | sécurité + corrections |
| Classification WSUS | **Upgrades** | Security Updates, Updates… |
| Gestion | **projet** (compatibilité applicative, pilote long) | **cycle mensuel** |

---

## 5. La cumulative (LCU) et le checkpoint

**LCU** (*Latest Cumulative Update*) : la mise à jour mensuelle de Windows. Elle contient **tous** les correctifs
de sécurité et de qualité publiés depuis la sortie de la version.

- **Une seule à installer** : celle du mois remplace (*supersede*) toutes les précédentes. Un poste qui a six mois de
    retard n'a besoin que de la dernière.
- Elle fait monter l'**UBR** : la correspondance UBR ↔ KB ↔ date est publiée sur *Windows release information*.
- Titre type : `2026-11 Cumulative Update for Windows 11, version 25H2 for x64-based Systems (KB50xxxxx)`.
- Elle **inclut la SSU** (voir §6) depuis 2021.
- Elle ne se « désinstalle » qu'avec `DISM /Online /Remove-Package` (la partie SSU reste).

**Avant la cumulative unique** (jusqu'en 2016 sur Windows 7 / 8.1), chaque correctif était une KB séparée : des
centaines de KB par machine, des combinaisons impossibles à tester. Le modèle cumulatif a simplifié la gestion
mais rendu le choix binaire : on prend **tout** le mois, ou rien.

**Checkpoint cumulative update** (Windows 11 24H2+, Server 2025) : pour réduire la taille des cumulatives,
Microsoft publie de temps en temps une cumulative de **référence** (le premier : KB5043080, septembre 2024). Les
cumulatives suivantes ne contiennent que les **différences depuis le dernier checkpoint**. Une machine doit avoir
le checkpoint avant de prendre une cumulative plus récente. Avec Windows Update et WSUS, l'agent gère cet ordre
seul ; avec le catalogue (installation manuelle, images), c'est à l'administrateur d'installer les checkpoints
dans l'ordre.

**Les « lettres » de la semaine** (vocabulaire Microsoft) :

| Release | Quand | Contenu | En entreprise |
|---|---|---|---|
| **B** | 2e mardi (Patch Tuesday) | sécurité + qualité | **le** déploiement mensuel |
| **D** | 4e semaine | **préversion non sécurité** (*optional non-security preview*) de la B suivante | tester sur quelques machines, jamais en prod |
| **OOB** | n'importe quand | correctif urgent (faille exploitée) ou de régression | procédure accélérée |

---

## 6. La pile de maintenance (SSU)

**Servicing stack** = le « moteur » qui installe les mises à jour : le service *Windows Modules Installer*
(**TrustedInstaller**) et la **CBS** (*Component-Based Servicing*). **SSU** (*Servicing Stack Update*) = la mise à
jour de ce moteur.

- Logique : on met à jour le moteur **avant** de lui faire installer une cumulative qui en a besoin. D'où la règle
    historique **« SSU d'abord, cumulative ensuite »**, et des cumulatives qui échouaient quand la SSU manquait.
- **Depuis 2021** (Windows 10 2004 et ultérieurs, Windows 11, Server 2022, Server 2025) : SSU et cumulative sont
    **combinées dans un seul paquet**. Plus d'ordre à gérer, mais :
    - la SSU ne se désinstalle **jamais** ;
    - `wusa /uninstall /kb:…` ne marche plus sur ce paquet combiné : on passe par `DISM /Remove-Package` avec le nom
        du paquet `Package_for_RollupFix…`.
- **Encore séparées** sur Windows Server 2016 (et Windows 10 1607 LTSB) : la SSU est une KB à part, déclarée comme
    **prérequis** de la cumulative dans WSUS. On approuve les deux.

```powershell
Get-WindowsPackage -Online | Where-Object PackageName -match 'ServicingStack|RollupFix' | Select-Object PackageName, InstallTime
```


---

## 7. Tous les autres types de mises à jour

| Type | Ce que c'est | Rythme | Dans WSUS |
|---|---|---|---|
| **.NET Framework** | Cumulative séparée pour .NET 3.5 / 4.8.x (pas .NET 8/9, qui ont leur propre canal) | mensuelle, même jour | produit Windows 11 / Server, classification Security Updates |
| **MSRT** (KB890830) | Outil de suppression de logiciels malveillants : exécuté une fois, cherche des familles connues, puis s'efface | mensuel | *Update Rollups* |
| **Defender – security intelligence** (KB2267602) | Définitions antivirus | **plusieurs fois par jour** | *Definition Updates*, approbation automatique |
| **Defender – plateforme** (KB4052623) et moteur | Le logiciel antivirus lui-même | mensuel | produit Microsoft Defender Antivirus |
| **Edge** | Navigateur Chromium : version majeure toutes les 4 semaines, correctifs de sécurité dès que nécessaire | 1 à 2 par semaine | produit **Microsoft Edge**, classification *Updates* ; canaux Stable / Extended Stable / Beta / Dev |
| **Office MSI** (2016, 2019…) | Correctifs d'Office installé en MSI | mensuel | produits Office |
| **Microsoft 365 Apps** | Office « Click-to-Run » : canaux Current / Monthly Enterprise / Semi-Annual | selon le canal | **pas** par WSUS seul (CDN Microsoft, Intune, ConfigMgr) |
| **Pilotes** (*Drivers*) | Pilotes publiés par les constructeurs via Microsoft | continu | classification *Drivers* ; énorme, synchronisation dépréciée : en entreprise, outils du constructeur |
| **Firmware / BIOS / UEFI** | Microcode, firmware (dont la base Secure Boot, *DBX*) | rare | parfois via Windows Update, surtout via le constructeur |
| **Dynamic Update** | Paquets utilisés **pendant** une mise à niveau ou une installation : Setup DU, SSU, LCU, **Safe OS** | mensuel | produit « Windows 11 Dynamic Update » (pour les supports et les mises à niveau) |
| **Safe OS / WinRE** | Mise à jour de l'environnement de récupération. Exemple marquant : KB5034441 (janvier 2024), échec 0x80070643 quand la partition de récupération était trop petite | rare | Security Updates |
| **KIR** (*Known Issue Rollback*) | Microsoft **désactive à distance** une modification non sécurité qui pose problème, sans retirer la cumulative. Sur les machines gérées (WSUS), via une **GPO** fournie par Microsoft | à l'occasion | hors WSUS |
| **Hotpatch** | Correctif appliqué **en mémoire, sans redémarrage**, avec un mois « de base » par trimestre qui redémarre (janvier, avril, juillet, octobre). Windows 11 Entreprise 24H2+ (Autopatch / Intune) et Server 2025 (Azure Arc, payant) | mensuel | hors WSUS |
| **ESU** | Correctifs de sécurité payants pour une version arrivée en fin de support (Windows 10, Server 2012) | mensuel | oui, si la licence ESU est activée sur la machine |

---

## 8. Le calendrier de Microsoft

| Moment | Événement |
|---|---|
| **2e mardi du mois**, 10 h à Redmond = **~19 h à Paris** | **Patch Tuesday** : cumulatives Windows, .NET, Office, serveurs… |
| le lendemain | *Exploit Wednesday* : les correctifs sont analysés (*patch diffing*), des exploits apparaissent pour les failles corrigées. D'où l'importance de ne pas traîner |
| 4e semaine | préversions non sécurité (D) |
| n'importe quand | **hors cycle** (OOB) : faille exploitée, régression |
| chaque semaine ou presque | Edge (correctifs Chromium) |
| plusieurs fois par jour | définitions Defender |
| septembre-octobre | nouvelle version annuelle de Windows 11 |

Exemple de cycle d'entreprise : J+1 applicatifs en pilote → J+8 applicatifs en prod
et OS en pilote → J+15 OS en prod → J+22 nettoyage. Le bon repère est **le mercredi qui suit le Patch Tuesday**,
pas « le 2e mercredi du mois » (qui tombe parfois avant).

---

## 9. Formats de paquets et outils d'installation

| Format | Ce que c'est | Outil |
|---|---|---|
| **.msu** (*Microsoft Update Standalone Package*) | Paquet autonome téléchargé du catalogue | double-clic, `wusa.exe`, ou `DISM /Add-Package` |
| **.cab** | Archive du paquet CBS lui-même (dans le .msu, ou fourni seul) | `DISM /Online /Add-Package /PackagePath:…` |
| **.psf** + **.cab** / **.wim** | Formats des cumulatives récentes (fichiers différentiels) | via le .msu |
| **.exe** / **.msi** | Office MSI, Edge, MSRT, Defender | l'installeur du produit |
| **Express** | Variante « différentielle » d'une cumulative : le client ne télécharge que ce qui lui manque. Très lourde côté serveur WSUS (option à éviter) | — |
| **UUP** (*Unified Update Platform*) | Mode de livraison de Windows Update : un seul format pour toutes les sources, téléchargement différentiel | Windows Update, WUfB |

```powershell
wusa C:\Temp\windows11.0-kb50xxxxx-x64.msu /quiet /norestart
DISM /Online /Add-Package /PackagePath:C:\Temp\windows11.0-kb50xxxxx-x64.msu
DISM /Online /Get-Packages /Format:Table
DISM /Online /Remove-Package /PackageName:Package_for_RollupFix~31bf3856ad364e35~amd64~~26100.xxxx.1.x
```


---

## 10. Ce qui se passe dans Windows pendant une mise à jour

### Les services

| Service | Nom | Rôle |
|---|---|---|
| Windows Update | `wuauserv` | l'**agent** : recherche, téléchargement, dialogue avec WSUS |
| Update Orchestrator | `UsoSvc` | **orchestre** : planification, échéances, redémarrages, notifications |
| BITS | `BITS` | téléchargement en arrière-plan, avec reprise |
| Delivery Optimization | `DoSvc` | téléchargement en pair à pair entre machines du réseau (Windows Update, Intune) |
| Windows Modules Installer | `TrustedInstaller` | **installe** les paquets CBS dans le magasin de composants |
| Windows Update Medic | `WaaSMedicSvc` | **répare** les composants Windows Update s'ils ont été désactivés ou abîmés |

### Les étapes

1. **Recherche** (*scan*) : l'agent demande à la source les métadonnées, évalue les **règles d'applicabilité** de
    chaque mise à jour (version, build, fichiers présents, prérequis) → applicable / non applicable / installée.
2. **Téléchargement** (BITS, dans `C:\Windows\SoftwareDistribution\Download`).
3. **Installation** (*staging*) : TrustedInstaller prépare les nouveaux composants dans le **magasin de composants**
    (`C:\Windows\WinSxS`).
4. **Redémarrage** : les fichiers en cours d'utilisation sont remplacés (« Mise à jour en cours, ne pas éteindre »).
    Avant ce redémarrage, la machine **n'est pas protégée**.
5. **Rapport** à la source (WSUS) : état de chaque mise à jour.

### Les dossiers et journaux

| Emplacement | Contenu |
|---|---|
| `C:\Windows\SoftwareDistribution\` | base de l'agent (`DataStore`), téléchargements (`Download`), `ReportingEvents.log` |
| `C:\Windows\System32\catroot2\` | catalogues de signatures |
| `C:\Windows\WinSxS\` | magasin de composants (toutes les versions des composants système) |
| `C:\Windows\Logs\WindowsUpdate\*.etl` | traces de l'agent → `Get-WindowsUpdateLog` reconstruit un `WindowsUpdate.log` lisible |
| `C:\Windows\Logs\CBS\CBS.log` | installation des paquets (erreurs de TrustedInstaller) |
| `C:\Windows\Logs\DISM\dism.log` | opérations DISM |
| Observateur d'événements → *Microsoft-Windows-WindowsUpdateClient/Operational* | 19 réussite, 20 échec, 43 installation démarrée, 44 téléchargement démarré |
| `HKLM\…\Component Based Servicing\RebootPending`, `…\WindowsUpdate\Auto Update\RebootRequired` | redémarrage en attente |

### Entretien et réparation

```powershell
DISM /Online /Cleanup-Image /AnalyzeComponentStore     # taille du magasin, nettoyage recommandé ?
DISM /Online /Cleanup-Image /StartComponentCleanup     # supprime les anciennes versions (fait aussi par une tâche planifiée)
DISM /Online /Cleanup-Image /RestoreHealth             # répare le magasin (source : Windows Update ou une image)
sfc /scannow                                           # répare les fichiers système depuis le magasin
```


`/ResetBase` supprime définitivement les versions remplacées : on ne peut plus désinstaller les mises à jour
installées. Avec WSUS, `/RestoreHealth` ne trouve pas toujours de source : la stratégie *Specify settings for
optional component installation and component repair* permet d'autoriser Windows Update pour la réparation.

**Ce qu'on ne fait pas en premier** : supprimer `SoftwareDistribution` ou `catroot2`. Ça efface l'historique et
masque la cause. C'est un dernier recours, après lecture des journaux.

---

## 11. Les sources

| Source | Pour qui | Contrôle |
|---|---|---|
| **Windows Update** | particuliers, petites structures | aucun (reports de quelques semaines) |
| **Microsoft Update** | idem + autres produits Microsoft (Office MSI, .NET…) | case « Recevoir les mises à jour d'autres produits Microsoft » |
| **Microsoft Update Catalog** | téléchargement manuel (.msu, .cab) : images, machines isolées, import dans WSUS | manuel |
| **WSUS** | organisations, réseaux internes ou isolés | **total** : produits, approbations, groupes, échéances |
| **Configuration Manager (SCCM / MECM)** | grandes organisations | WSUS en dessous (*Software Update Point*) + déploiements, fenêtres, rapports, applications tierces |
| **Windows Update for Business / Intune / Autopatch** | parc géré dans le cloud | **anneaux** (*rings*) et **reports** (*deferrals*) : la machine télécharge chez Microsoft, l'administrateur fixe le délai |
| **Azure Update Manager** | serveurs (Azure, Arc) | évaluations et fenêtres de maintenance |

Une machine peut avoir **plusieurs** sources configurées pour des types différents (qualité chez WSUS, pilotes
chez Windows Update…) : c'est la stratégie *Specify source service for specific classes of Windows Updates*. Une
configuration mixte non voulue est une cause classique de « je n'ai rien approuvé, et pourtant ça s'installe ».

---

## 12. WSUS de l'intérieur

### Les composants

| Composant | Rôle |
|---|---|
| Service **WsusService** | synchronisation, téléchargement des fichiers, tâches de fond |
| **IIS** : site *WSUS Administration*, pool **WsusPool** | les services web : clients, console, serveurs aval |
| **SUSDB** | base : catalogue, approbations, groupes, états des machines. Sur **WID** (*Windows Internal Database*, gratuite, locale) ou **SQL Server** (gros parcs, haute disponibilité) |
| **WsusContent** | fichiers des mises à jour approuvées (`D:\WSUS\WsusContent`) |
| **Console** et module PowerShell **UpdateServices** | administration (API .NET `Microsoft.UpdateServices.Administration`) |
| `wsusutil.exe` | outil en ligne de commande : `postinstall`, `reset`, `export` / `import`, `checkhealth`, `usecustomwebsite` |

### Les services web (ce que le client appelle)

| URL (port 8530 / 8531) | Rôle |
|---|---|
| `/selfupdate/` | mise à jour de l'agent client lui-même |
| `/ClientWebService/client.asmx` | **recherche** : « voici mon état, que dois-je installer ? » |
| `/SimpleAuthWebService/SimpleAuth.asmx` | authentification du client (jeton) |
| `/ReportingWebService/ReportingWebService.asmx` | **rapports** d'état et événements |
| `/Content/` | **fichiers** à télécharger |
| `/ApiRemoting30/WebService.asmx` | console et PowerShell |
| `/ServerSyncWebService/` | serveurs **aval** qui se synchronisent sur celui-ci |

Chaque client est identifié par son **SusClientId** (GUID dans le registre), pas par son nom : deux machines
clonées sans *sysprep* ont le même identifiant et n'apparaissent que comme une seule.

### Métadonnées et fichiers

- La **synchronisation** ramène le **catalogue** : titres, descriptions, règles d'applicabilité, relations de
    remplacement et de prérequis. C'est ce qui remplit SUSDB.
- Les **fichiers** ne sont téléchargés que pour les mises à jour **approuvées** (option par défaut).
- Le **client** évalue lui-même l'applicabilité à partir des métadonnées : WSUS ne « sait » pas ce dont une
    machine a besoin avant qu'elle l'ait rapporté.

### Le paramétrage

| Réglage | Choix |
|---|---|
| **Source amont** | Microsoft Update, ou un autre WSUS (**aval**) |
| **Produits** | seulement ceux du parc (chaque produit en trop alourdit la base et les recherches des clients) |
| **Classifications** | Security, Critical, Updates, Update Rollups, Definition Updates ; jamais *Upgrades* ni *Drivers* par défaut |
| **Langues** | seulement celles du parc |
| **Planification** | synchronisation automatique, 1 à 4 fois par jour (heure en UTC dans l'API) |
| **Ciblage** | côté **client** (stratégie / GPO : `TargetGroup`) ou côté **serveur** (déplacement dans la console) |
| **Approbations automatiques** | règles : classification + produit → groupe, avec échéance éventuelle. Bien pour Defender, risqué ailleurs |
| **Stockage** | local (recommandé), ou les clients téléchargent chez Microsoft (WSUS ne fait que les approbations) |

### Les approbations

| Action | Effet |
|---|---|
| **Approuvée pour installation** | les machines du groupe qui en ont besoin l'installent (selon leur stratégie) |
| avec **échéance** | installation **forcée** à la date, puis redémarrage forcé selon la stratégie |
| **Approuvée pour suppression** | désinstallation, si la mise à jour le permet |
| **Non approuvée** | aucune action pour ce groupe |
| **Refusée** (*declined*) | masquée partout, plus évaluée par les clients ; ne désinstalle rien |

Les approbations s'**héritent** des groupes parents vers les groupes enfants.

### Les états d'une machine pour une mise à jour

| État | Sens |
|---|---|
| Inconnu (*Unknown*) | la machine n'a pas encore rapporté pour cette mise à jour |
| Non applicable | ne la concerne pas (autre version, déjà plus récent…) |
| Nécessaire (*Not installed*) | applicable, pas encore installée |
| Téléchargée | fichiers sur la machine, pas installée |
| Installée, redémarrage en attente | installée mais **pas encore active** |
| Installée | ok |
| Échec | l'installation a échoué (code dans l'événement 20) |

### Remplacement, expiration, révision

- **Remplacée** (*superseded*) : une mise à jour plus récente fait la même chose et plus (cumulative suivante).
    À refuser quand plus aucune machine n'en a besoin.
- **Expirée** : retirée par Microsoft (défaut grave). À refuser.
- **Révision** : nouvelle version des métadonnées d'une même mise à jour.

### Hiérarchies

- **Amont / aval** : un WSUS central et des WSUS en agence. L'aval est **réplica** (mêmes groupes et approbations,
    administré depuis l'amont) ou **autonome** (administration locale).
- **Déconnecté** (réseau isolé) : export de l'amont (`wsusutil export` + copie de WsusContent), import sur le
    serveur isolé.
- Nettoyage : toujours de l'**aval vers l'amont**.

### Maintenance

Un WSUS non entretenu ralentit (recherches clients longues, console qui plante, pool IIS qui s'arrête → erreur
HTTP 503 / 0x80244022). Chaque mois : refus des remplacées et expirées, assistant de nettoyage, réindexation de
SUSDB, surveillance du disque.

### Statut

Microsoft a annoncé en 2024 que WSUS est **déprécié** : plus de nouvelles fonctions, mais toujours présent dans
Windows Server 2025 et supporté selon le cycle de vie de ce système. La synchronisation des pilotes est elle aussi
dépréciée. WSUS reste très répandu (seul ou sous Configuration Manager), en particulier sur les réseaux qui ne
doivent pas dépendre du cloud.

---

## 13. Sécurité de la chaîne de mise à jour

Le système de mises à jour a les droits les plus élevés sur toutes les machines : c'est une cible.

- **WSUS en HTTP** : un attaquant sur le réseau peut s'interposer et proposer de faux « correctifs » (outils
    signés Microsoft détournés). En production, WSUS se configure en **HTTPS (8531)** avec un certificat d'entreprise.
- **Le serveur WSUS lui-même** : CVE-2025-59287 (octobre 2025), exécution de code à distance sur le service WSUS,
    exploitée, corrigée hors cycle. Leçons : patcher le serveur WSUS en priorité, **ne jamais exposer 8530 / 8531 sur
    Internet**, filtrer qui peut joindre le serveur.
- **Signature** : les clients n'installent que des mises à jour signées par Microsoft (ou par un certificat
    explicitement approuvé pour la publication locale d'applications tierces).
- **Comptes** : l'administration WSUS = pouvoir d'installer du code sur tout le parc. Groupe *WSUS Administrators*
    restreint, console sur un poste d'administration.
- **Preuve** : en MCS, ce qui compte n'est pas « WSUS tourne » mais le **délai** entre publication et installation,
    et la **liste** de ce qui manque.

---

## 14. Glossaire

| Terme | Définition courte |
|---|---|
| AUOptions | Valeur de stratégie : 2 notifier, 3 télécharger et notifier, 4 installer selon un planning, 7 télécharger et notifier installation + redémarrage |
| Approbation | Décision WSUS « ce groupe doit installer cette mise à jour » |
| B release | Mise à jour de sécurité du Patch Tuesday |
| BITS | Service de téléchargement en arrière-plan |
| Build | Numéro de compilation d'une version (26200 = 25H2) |
| CBS | *Component-Based Servicing* : moteur d'installation des composants Windows |
| Checkpoint | Cumulative de référence (24H2+) que les suivantes complètent |
| Ciblage côté client / serveur | La machine annonce son groupe (stratégie) / l'admin la place dans la console |
| Classification | Type de mise à jour dans WSUS (Security Updates, Updates…) |
| CVE | Identifiant universel d'une vulnérabilité |
| D release | Préversion non sécurité de la 4e semaine |
| Deadline (échéance) | Date d'installation forcée |
| Declined (refusée) | Masquée de WSUS, ne désinstalle rien |
| Delivery Optimization | Partage pair à pair des téléchargements |
| DISM | Outil de gestion des paquets et images Windows |
| Dynamic Update | Paquets utilisés pendant une mise à niveau / installation |
| eKB / enablement package | Petit paquet qui active une version annuelle (24H2 → 25H2) |
| ESU | Correctifs de sécurité payants après la fin de support |
| Express | Fichiers différentiels d'une cumulative (lourds côté WSUS) |
| Feature update | Mise à jour de fonctionnalités : change la version |
| Hotpatch | Correctif sans redémarrage (Windows 11 Entreprise, Server 2025 avec Arc) |
| KB | Numéro d'article Microsoft, et par extension la mise à jour |
| KEV | Catalogue CISA des failles exploitées |
| KIR | *Known Issue Rollback* : désactivation à distance d'un changement défectueux |
| LCU | *Latest Cumulative Update* : la cumulative mensuelle |
| LTSC | Canal à support long, sans nouvelles fonctions |
| MSRC | *Microsoft Security Response Center* : gravités, Security Update Guide |
| MSRT | Outil mensuel de suppression de logiciels malveillants (KB890830) |
| .msu | Paquet autonome du catalogue |
| OOB | *Out-of-band* : correctif hors calendrier |
| Patch Tuesday | 2e mardi du mois, ~19 h à Paris |
| Quality update | Mise à jour de qualité : correctifs mensuels |
| Remplacée (superseded) | Rendue inutile par une plus récente |
| Révision | Nouvelle version des métadonnées d'une mise à jour WSUS |
| Ring (anneau) | Groupe de déploiement (WUfB / Intune) : l'équivalent des groupes WSUS |
| SSU | *Servicing Stack Update* : mise à jour du moteur d'installation |
| SUSDB | Base de données de WSUS |
| SusClientId | Identifiant unique d'un client WSUS |
| TargetGroup | Valeur de stratégie : nom du groupe WSUS de la machine |
| TrustedInstaller | Service qui installe les paquets (*Windows Modules Installer*) |
| UBR | *Update Build Revision* : le numéro après le point du build, niveau de cumulative |
| UpdateID | GUID d'une mise à jour dans WSUS |
| UsoSvc | *Update Orchestrator* : planification et redémarrages |
| UUP | Plateforme de livraison unifiée de Windows Update |
| WID | *Windows Internal Database* : base locale gratuite de WSUS |
| WinSxS | Magasin de composants de Windows |
| WSUS | *Windows Server Update Services* |
| WsusPool | Pool IIS de WSUS (son arrêt = erreur 503) |
| WUA | *Windows Update Agent* : l'agent client (`wuauserv`) |
| WUfB | *Windows Update for Business* : gestion par anneaux et reports, depuis le cloud |
| 24H2 / 25H2 | Version annuelle : année + semestre (*Half*) |

---

## Sources

- [Présentation de WSUS](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus) et [planification](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/plan/plan-your-wsus-deployment)
- [Types de mises à jour Windows](https://learn.microsoft.com/en-us/windows/deployment/update/get-started-updates-channels-tools)
- [Servicing stack updates](https://learn.microsoft.com/en-us/windows/deployment/update/servicing-stack-updates)
- [Checkpoint cumulative updates](https://learn.microsoft.com/en-us/windows/deployment/update/catalog-checkpoint-cumulative-updates)
- [Windows 11 release information](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information) et [Windows release health](https://learn.microsoft.com/en-us/windows/release-health/)
- [Cycle de vie Windows](https://learn.microsoft.com/en-us/lifecycle/faq/windows)
- [Journaux Windows Update](https://learn.microsoft.com/en-us/windows/deployment/update/windows-update-logs)
- [Guide de maintenance WSUS](https://learn.microsoft.com/en-us/troubleshoot/mem/configmgr/update-management/wsus-maintenance-guide)
- [Security Update Guide](https://msrc.microsoft.com/update-guide/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [CERT-FR](https://www.cert.ssi.gouv.fr/)
- 26H2 en Release Preview (build 26300) : [Eleven Forum](https://www.elevenforum.com/t/windows-11-insider-release-preview-build-26300-9278-26h2-aug-27.49064/)
