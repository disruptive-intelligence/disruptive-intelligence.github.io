---
title: Chapitre 8 — Outils, journaux et dépannage de premier niveau
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie III — Ce qui se passe dans la machine
  - index.md
---

> 🧱 **Les bases**
>
> - Un **journal** (*log*) est un fichier où un programme écrit ce qu'il fait. L'**Observateur d'événements** (`eventvwr.msc`) regroupe les journaux de Windows sous forme d'événements numérotés (Event ID).
> - Un **code d'erreur** Windows s'écrit en hexadécimal (`0x8024…`). Il est le point de départ de toute recherche.
> - Méthode générale : **observer** (journaux), **comprendre** (code d'erreur), **agir** (correction ciblée), **vérifier** (UBR, état).

## 8.1 Les outils d'installation

| Outil | Usage | Limites |
|---|---|---|
| **Paramètres > Windows Update** | installation manuelle, historique, mises à jour facultatives | lecture seule des stratégies (« Certains paramètres sont gérés par votre organisation ») |
| `wusa.exe` | installer un .msu (`/quiet /norestart`), désinstaller une KB | ne désinstalle **pas** les cumulatives combinées SSU+LCU |
| `DISM` | ajouter/retirer des paquets, en ligne (`/Online`) ou dans une image hors ligne (`/Image:`), réparer le magasin | syntaxe exigeante ; nécessite les droits administrateur |
| **Catalogue Microsoft Update** | télécharger un .msu/.cab (machines isolées, images, import WSUS) | tout est manuel, y compris l'ordre des checkpoints |
| `setup.exe` (support d'installation) | mise à niveau sur place scriptable (`/auto upgrade /quiet`) | nécessite un ISO à jour |
| Module PowerShell **PSWindowsUpdate** | piloter l'agent en PowerShell (scan, installation à distance) | **module tiers communautaire**, non supporté par Microsoft ; à valider avant usage en production |
| `Get-HotFix` | lister les correctifs installés | ne voit que ce que WMI classe comme « QFE » : **liste incomplète**, ne prouve rien seul |
| `usoclient` | déclencher un scan (`StartScan`) | **non documenté**, comportement variable selon les versions |

## 8.2 Les dossiers et journaux

| Emplacement | Contenu |
|---|---|
| `C:\Windows\SoftwareDistribution\` | base de l'agent (`DataStore`), téléchargements (`Download`), `ReportingEvents.log` (historique lisible des événements de l'agent) |
| `C:\Windows\System32\catroot2\` | base des catalogues de signatures |
| `C:\Windows\WinSxS\` | magasin de composants |
| `C:\Windows\Logs\WindowsUpdate\*.etl` | traces de l'agent ; `Get-WindowsUpdateLog` reconstruit un `WindowsUpdate.log` lisible (sur le Bureau) |
| `C:\Windows\Logs\CBS\CBS.log` | installation des paquets (erreurs de TrustedInstaller) — **le journal à lire quand l'installation échoue** |
| `C:\Windows\Logs\DISM\dism.log` | opérations DISM |
| `C:\$Windows.~BT\Sources\Panther\` puis `C:\Windows\Panther\` | journaux des **mises à niveau** (`setupact.log`, `setuperr.log`) |
| Observateur d'événements → journal *Système* (source *WindowsUpdateClient*) et *Microsoft-Windows-WindowsUpdateClient/Operational* | **19** réussite, **20** échec (avec le code), **43** installation démarrée, **44** téléchargement démarré |
| `HKLM\…\Component Based Servicing\RebootPending`, `…\WindowsUpdate\Auto Update\RebootRequired` | redémarrage en attente (Ch.7) |

```powershell
Get-WindowsUpdateLog                       # reconstruit WindowsUpdate.log sur le Bureau

# Les 20 derniers événements d'installation (réussite 19 / échec 20)
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WindowsUpdateClient'; Id=19,20} -MaxEvents 20 |
    Select-Object TimeCreated, Id, Message

# Chercher les erreurs dans CBS.log
Select-String -Path C:\Windows\Logs\CBS\CBS.log -Pattern 'error|failed' | Select-Object -Last 30
```


## 8.3 Les codes d'erreur fréquents

| Code | Signification | Piste |
|---|---|---|
| **0x80244022** | le serveur répond HTTP 503 (service indisponible) | **pool IIS WsusPool arrêté** (Ch.10) |
| 0x8024401c | délai dépassé en joignant le serveur | WSUS surchargé, réseau, proxy |
| 0x80244017 / 0x80244019 | HTTP 401 (refusé) / 404 (introuvable) | URL WSUS erronée dans la GPO, droits IIS, contenu manquant |
| 0x8024402c / 0x80072ee2 / 0x80072efd | nom introuvable, délai réseau, connexion impossible | DNS, proxy, pare-feu, port 8530/8531 |
| **0x800f0922** | échec d'installation CBS (souvent : espace insuffisant sur une partition système/récupération, ou échec à l'application au démarrage) | `CBS.log`, espace disque, VPN/agent de sécurité qui interfère |
| 0x800f081f / 0x800f0906 | fichiers sources introuvables (réparation, fonctionnalités facultatives) | stratégie de source de réparation (§8.4) |
| 0x80073701 | composant (assembly) manquant dans le magasin | `DISM /RestoreHealth` |
| 0x80070002 | fichier introuvable | téléchargement incomplet, cache corrompu |
| 0x8007000d | données invalides | fichier corrompu, cache à reconstruire |
| **0x80070643** | échec fatal pendant l'installation | cas célèbre de WinRE (KB5034441), ou installeur .msi (.NET, Defender) |
| 0xC1900101 (et variantes) | **mise à niveau** annulée, souvent à cause d'un pilote | `SetupDiag`, mise à jour des pilotes |
| 0xC1900208 | application incompatible bloquant la mise à niveau | identifier et retirer/mettre à jour l'application |

> ✅ **Bonne pratique** — Un même code peut avoir plusieurs causes. Le code oriente ; **le journal (`CBS.log`, `WindowsUpdate.log`, Panther) confirme**. Chercher d'abord le code dans la documentation Microsoft (*Windows Update error codes*) et dans les *known issues* de la KB du mois.

## 8.4 Réparer

```powershell
DISM /Online /Cleanup-Image /ScanHealth          # diagnostic du magasin (long)
DISM /Online /Cleanup-Image /RestoreHealth       # répare le magasin (source : Windows Update ou une image)
DISM /Online /Cleanup-Image /RestoreHealth /Source:wim:D:\sources\install.wim:1 /LimitAccess   # source locale
sfc /scannow                                     # répare les fichiers système depuis le magasin (à lancer APRÈS DISM)
```


- **Ordre logique** : `DISM /RestoreHealth` d'abord (réparer la source), `sfc /scannow` ensuite (réparer les fichiers depuis la source réparée).
- **Avec WSUS**, `/RestoreHealth` ne trouve pas toujours de source : WSUS ne fournit pas les fichiers de réparation. La stratégie *Spécifier les paramètres d'installation des composants facultatifs et de réparation de composants* (*Specify settings for optional component installation and component repair*) permet d'autoriser Windows Update **pour la réparation uniquement**, ou d'indiquer une image locale.

> ⚠️ **Ce qu'on ne fait pas en premier** — Supprimer `SoftwareDistribution` ou `catroot2` (la fameuse « réinitialisation de Windows Update »). Ça efface l'historique, oblige un nouveau scan complet et **masque la cause**. C'est un **dernier recours**, après lecture des journaux, et en sachant pourquoi.

**Méthode de premier niveau**, dans l'ordre :

1. Lire l'état exact (Paramètres, WSUS) et le **code d'erreur** (événement 20).
2. Vérifier les évidences : espace disque, redémarrage en attente, accès réseau au serveur WSUS (`Test-NetConnection wsus.domaine.local -Port 8530`).
3. Lire le journal pertinent (`WindowsUpdate.log` pour la recherche et le téléchargement, `CBS.log` pour l'installation).
4. Chercher le code dans les *known issues* de la KB, Windows release health, puis la communauté.
5. Appliquer une correction **ciblée**, puis vérifier (UBR, événement 19).
6. Si plusieurs machines ont la même erreur : c'est un **problème de parc** (GPO, serveur, mise à jour défectueuse), pas un problème de poste. Remonter au lead.

## 8.5 Encadré : les mises à jour de fonctionnalités

Quand ce n'est pas un enablement package, une mise à jour de fonctionnalités est une **réinstallation sur place** (*in-place upgrade*) :

| Phase | Où | Ce qui se passe |
|---|---|---|
| **Downlevel** | l'ancien Windows, en fonctionnement | préparation : copie des fichiers, vérification de compatibilité, collecte des pilotes et applications à migrer |
| **SafeOS** | environnement minimal (WinPE), après redémarrage | installation de la nouvelle image, application des mises à jour dynamiques |
| **First boot** | nouveau Windows, premier démarrage | migration des pilotes et des paramètres |
| **Second boot** | nouveau Windows | migration des données et applications, finalisation (écran « Bonjour ») |

- En cas d'échec, Windows **revient automatiquement** à l'ancienne version.
- L'ancien système est conservé dans `C:\Windows.old` pendant **10 jours** par défaut (retour arrière possible), puis supprimé.
- **SetupDiag** (outil Microsoft) analyse les journaux Panther et donne la cause probable d'un échec.
- **Blocages de protection** (*safeguard holds*) : Microsoft empêche la mise à niveau des machines ayant une incompatibilité connue (pilote, application). Ils s'appliquent aux machines qui passent par **Windows Update / stratégies cloud** ; une machine gérée par **WSUS** n'en bénéficie pas : c'est à l'équipe de vérifier Windows release health avant de diffuser une mise à niveau.
- Rappel : 23H2 → 24H2 = mise à niveau complète ; 24H2 → 25H2 → 26H2 = enablement package. 26H1 ne se met pas à niveau vers 26H2.

Approfondissement : version complète, Ch.13.

> 🧵 **Fil rouge — Février 2026**
>
> Quarante postes de l'agence de Nantes échouent chaque nuit sur la cumulative de février avec **0x800f0922**. Inès commence par l'événement 20, puis `CBS.log` : échec à l'étape de démarrage, lié à la partition système. Ces postes viennent d'un vieux master dont la partition de récupération fait 300 Mo. Elle ne supprime pas `SoftwareDistribution` : elle documente la cause, Karim fait valider au CAB un script d'agrandissement de la partition testé sur 3 postes, puis la cumulative passe. Le cas devient une fiche dans la base de connaissances de l'équipe.

> 📌 **À retenir**
>
> - Les trois journaux clés : `WindowsUpdate.log` (scan/téléchargement), `CBS.log` (installation), Panther (mise à niveau). Événements 19/20.
> - Le code d'erreur oriente, le journal confirme.
> - Réparer : `DISM /RestoreHealth` puis `sfc /scannow`. Réinitialiser `SoftwareDistribution` = dernier recours.
> - Plusieurs machines avec la même erreur = problème de parc.

---
