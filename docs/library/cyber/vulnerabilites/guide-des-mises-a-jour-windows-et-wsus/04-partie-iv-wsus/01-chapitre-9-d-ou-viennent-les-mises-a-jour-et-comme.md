---
title: Chapitre 9 — D'où viennent les mises à jour, et comment WSUS fonctionne
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie IV — WSUS
  - index.md
---

> 🧱 **Les bases**
>
> - **IIS** (*Internet Information Services*) est le serveur web de Windows. Un **pool d'applications** est un processus (`w3wp.exe`) qui fait tourner une application web.
> - Une **GPO** (*Group Policy Object*, stratégie de groupe) est un ensemble de réglages appliqué automatiquement par Active Directory aux machines d'une unité d'organisation (OU). Les réglages Windows Update y sont des valeurs de registre sous `HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate`.
> - Un **GUID** est un identifiant unique de 128 bits, écrit sous la forme `{xxxxxxxx-xxxx-…}`.

## 9.1 Les sources possibles

| Source | Pour qui | Contrôle |
|---|---|---|
| **Windows Update** | particuliers, petites structures | aucun (reports de quelques semaines au plus) |
| **Microsoft Update** | idem + autres produits Microsoft (Office MSI, .NET…) | case « Recevoir les mises à jour d'autres produits Microsoft » |
| **Microsoft Update Catalog** | téléchargement manuel (.msu, .cab) : images, machines isolées, import dans WSUS | manuel |
| **WSUS** | organisations, réseaux internes ou isolés | **total** : produits, approbations, groupes, échéances |
| **Configuration Manager (SCCM / MECM)** | grandes organisations | WSUS en dessous (*Software Update Point*) + déploiements, fenêtres de maintenance, rapports, applications tierces |
| **Stratégies client Windows Update / Intune / Autopatch** (ex-*Windows Update for Business*) | parc géré dans le cloud | **anneaux** (*rings*) et **reports** (*deferrals*) : la machine télécharge chez Microsoft, l'administrateur fixe le délai (Ch.14) |
| **Azure Update Manager** | serveurs (Azure, Arc) | évaluations et fenêtres de maintenance |

**Sources mixtes.** Une machine peut avoir **plusieurs** sources selon le type de mise à jour (qualité chez WSUS, pilotes chez Windows Update…) : c'est la stratégie *Specify source service for specific classes of Windows Updates*. Elle est utile dans une migration progressive vers le cloud, mais une **configuration mixte non voulue** (une stratégie de report cloud ajoutée en plus de WSUS, par exemple) est une cause classique de « je n'ai rien approuvé, et pourtant ça s'installe ».

## 9.2 Ce qu'est WSUS

**WSUS** (*Windows Server Update Services*) est un **rôle de Windows Server**, gratuit, qui :

1. **se synchronise** avec Microsoft Update (ou un autre WSUS) pour récupérer le **catalogue** des mises à jour ;
2. permet à l'administrateur d'**approuver** chaque mise à jour pour des **groupes** de machines ;
3. **stocke les fichiers** des mises à jour approuvées et les **distribue** sur le réseau interne ;
4. **collecte l'état** de chaque machine (installée, nécessaire, échec…).

Il évite que 3 400 postes téléchargent chacun chez Microsoft, et surtout il donne **le contrôle du moment** : rien ne s'installe tant que ce n'est pas approuvé.

## 9.3 Les composants

| Composant | Rôle |
|---|---|
| Service **WsusService** | synchronisation, téléchargement des fichiers, tâches de fond |
| **IIS** : site *WSUS Administration*, pool **WsusPool** | les services web appelés par les clients, la console, les serveurs aval |
| **SUSDB** | la base : catalogue, approbations, groupes, états des machines. Sur **WID** (*Windows Internal Database*, gratuite, locale) ou **SQL Server** (gros parcs, haute disponibilité, base partagée) |
| **WsusContent** | fichiers des mises à jour approuvées (par exemple `D:\WSUS\WsusContent`) |
| **Console** (MMC) et module PowerShell **UpdateServices** | administration (API .NET `Microsoft.UpdateServices.Administration`) |
| `wsusutil.exe` | outil en ligne de commande : `postinstall` (finalise l'installation), `reset` (revérifie les fichiers), `export` / `import` (réseau isolé), `checkhealth`, `usecustomwebsite`, `configuressl` |

## 9.4 Les services web : ce que le client appelle

| URL (port 8530 en HTTP / 8531 en HTTPS) | Rôle |
|---|---|
| `/selfupdate/` | mise à jour de l'agent client lui-même |
| `/ClientWebService/client.asmx` | **recherche** : « voici mon état, que dois-je installer ? » |
| `/SimpleAuthWebService/SimpleAuth.asmx` | authentification du client (jeton) |
| `/ReportingWebService/ReportingWebService.asmx` | **rapports** d'état et événements |
| `/Content/` | **fichiers** à télécharger |
| `/ApiRemoting30/WebService.asmx` | console et PowerShell |
| `/ServerSyncWebService/` | serveurs **aval** qui se synchronisent sur celui-ci |

Chaque client est identifié par son **SusClientId** (GUID stocké dans `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate`), **pas par son nom**. Deux machines clonées sans *sysprep* ont le même identifiant et n'apparaissent que comme **une seule** dans la console, qui « clignote » entre les deux noms.

```powershell
# Corriger un SusClientId dupliqué (sur le poste cloné)
Stop-Service wuauserv
Remove-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate' -Name SusClientId, SusClientIdValidation -ErrorAction SilentlyContinue
Start-Service wuauserv
(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()   # nouveau scan, nouvel identifiant
```


## 9.5 Métadonnées et fichiers

- La **synchronisation** ramène le **catalogue** : titres, descriptions, règles d'applicabilité, relations de remplacement et de prérequis. C'est ce qui remplit SUSDB.
- Les **fichiers** ne sont téléchargés que pour les mises à jour **approuvées** (option par défaut).
- Le **client** évalue lui-même l'applicabilité à partir des métadonnées : **WSUS ne « sait » pas ce dont une machine a besoin avant qu'elle l'ait rapporté**. Une machine qui ne contacte plus WSUS garde son dernier état connu, de plus en plus faux.
- Par défaut, un client recherche les mises à jour environ **toutes les 22 heures** (avec un décalage aléatoire pour ne pas saturer le serveur).

## 9.6 Le paramétrage du serveur

| Réglage | Choix recommandé |
|---|---|
| **Source amont** | Microsoft Update, ou un autre WSUS (serveur **aval**) |
| **Produits** | seulement ceux du parc (chaque produit en trop alourdit la base et les recherches des clients) |
| **Classifications** | Security, Critical, Updates, Update Rollups, Definition Updates ; **jamais** *Upgrades* ni *Drivers* par défaut |
| **Langues** | seulement celles du parc |
| **Planification** | synchronisation automatique, 1 à 4 fois par jour, dont une **après 19 h 30 le Patch Tuesday** (heure exprimée en UTC dans l'API) |
| **Ciblage** | côté **client** (GPO : `TargetGroup`) ou côté **serveur** (déplacement dans la console) |
| **Approbations automatiques** | règles : classification + produit → groupe, avec échéance éventuelle. Bien pour Defender, risqué ailleurs |
| **Stockage** | local (recommandé), ou les clients téléchargent chez Microsoft (WSUS ne fait alors que les approbations) |
| **Fichiers express** | désactivés sauf besoin précis (Ch.7) |

## 9.7 La GPO côté client

Chemin : *Configuration ordinateur > Modèles d'administration > Composants Windows > Windows Update*. Sous Windows 11, les réglages sont rangés en sous-dossiers (*Gérer les mises à jour proposées par Windows Server Update Services*, *Gérer l'expérience utilisateur final*).

| Réglage (nom GPO) | Valeur de registre | Effet |
|---|---|---|
| *Specify intranet Microsoft update service location* | `WUServer`, `WUStatusServer` (+ `UseWUServer=1` sous `AU`) | l'URL du WSUS, ex. `https://wsus.orian.local:8531` |
| *Enable client-side targeting* | `TargetGroupEnabled=1`, `TargetGroup` | le groupe WSUS de la machine |
| *Configure Automatic Updates* | `AUOptions` (sous `AU`) | **2** notifier ; **3** télécharger et notifier ; **4** télécharger et installer selon un planning ; **7** télécharger, notifier l'installation, notifier le redémarrage |
| | `ScheduledInstallDay`, `ScheduledInstallTime` | planning (avec AUOptions = 4) |
| *Specify deadlines for automatic updates and restarts* | échéances (jours) et période de grâce | installation et redémarrage forcés après X jours |
| *Turn off auto-restart for updates during active hours* | heures d'activité | pas de redémarrage automatique pendant les heures de travail |
| *Do not connect to any Windows Update Internet locations* | `DoNotConnectToWindowsUpdateInternetLocations=1` | empêche le client d'aller chercher chez Microsoft (sources mixtes, contournements) |
| *Specify source service for specific classes of Windows Updates* | `SetPolicyDrivenUpdateSourceFor…` | choisir WSUS ou Windows Update par type (qualité, fonctionnalités, pilotes, autres) |

```powershell
# Vérifier ce que le poste a réellement reçu
Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'
Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU'
gpresult /r /scope computer        # quelles GPO s'appliquent
```


## 9.8 Les hiérarchies

- **Amont / aval** : un WSUS central (amont, *upstream*) synchronisé sur Microsoft, et des WSUS en site (aval, *downstream*) synchronisés sur lui. L'aval est :
    - **réplica** : mêmes groupes et mêmes approbations, administrés **depuis l'amont** (le cas d'ORIAN) ;
    - **autonome** : il hérite du catalogue mais a ses propres groupes et approbations.
- **Déconnecté** (réseau isolé, sans Internet) : export depuis un WSUS connecté (`wsusutil export` pour les métadonnées + copie de WsusContent), transfert par support contrôlé, import sur le serveur isolé (`wsusutil import`). Les approbations se refont sur le serveur isolé.
- **Nettoyage** : toujours **de l'aval vers l'amont** (on nettoie d'abord les serveurs du bas de la hiérarchie).

## 9.9 Le statut de WSUS en 2026

Microsoft a annoncé le **20 septembre 2024** que WSUS est **déprécié** : plus de nouvelles fonctions, plus de demandes d'évolution acceptées. Mais :

- WSUS reste **présent dans Windows Server 2025** et supporté selon le cycle de vie de ce système (support étendu jusqu'en novembre 2034) ;
- Microsoft continue d'y **publier les mises à jour** ;
- Configuration Manager, qui s'appuie sur WSUS, n'est pas affecté.

La **synchronisation des pilotes** dans WSUS est elle aussi dépréciée (fin effective en 2025) : les pilotes restent disponibles dans le catalogue Microsoft Update, à importer manuellement, mais en entreprise on passe plutôt par les outils des constructeurs.

En pratique : WSUS reste très répandu (seul ou sous ConfigMgr), en particulier sur les réseaux qui ne doivent pas dépendre du cloud. Le sujet n'est pas « WSUS va s'arrêter demain », mais « **les nouveautés (hotpatch, rapports cloud…) n'y arriveront pas** » (Ch.14).

> 🧵 **Fil rouge — Janvier 2026**
>
> Karim fait faire à Inès le tour de l'architecture : WSUS amont au datacenter (synchronisé sur Microsoft Update, SUSDB sur SQL Server), trois réplicas sur Lyon, Nantes et Lille. Les postes trouvent leur WSUS par GPO (une par site) et leur groupe par ciblage côté client (`TargetGroup` = « Postes-Pilote », « Postes-Prod », « Serveurs-Pilote »…). Inès note un détail : la GPO de Lille pointe encore en `http://…:8530`. Elle le garde pour le Ch.11.

> 📌 **À retenir**
>
> - WSUS = catalogue (métadonnées) + approbations + fichiers + états. **Le client décide de ce qui lui est applicable.**
> - Clients identifiés par **SusClientId** (attention aux clones).
> - Cocher **uniquement** les produits, classifications et langues du parc.
> - GPO : `WUServer`, `TargetGroup`, `AUOptions`, échéances ; vérifier les sources mixtes.
> - WSUS est déprécié mais supporté ; il ne recevra plus de nouvelles fonctions.

---
