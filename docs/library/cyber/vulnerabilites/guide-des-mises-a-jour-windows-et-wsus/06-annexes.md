---
title: Annexes
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - index.md
---

## Annexe A — Glossaire

| Terme | Définition courte |
|---|---|
| 24H2 / 25H2 / 26H2 | Version annuelle de Windows 11 : année + semestre (*Half*) |
| 26H1 | Version de Windows 11 sur un socle distinct, réservée à certains PC neufs ; pas de passage direct vers 26H2 |
| Amont / aval | WSUS central synchronisé sur Microsoft / WSUS de site synchronisé sur le central |
| Anneau (*ring*) | Groupe de déploiement progressif ; dans WSUS, un groupe d'ordinateurs |
| Approbation | Décision WSUS « ce groupe doit installer cette mise à jour » |
| AUOptions | Valeur de stratégie : 2 notifier, 3 télécharger et notifier, 4 installer selon un planning, 7 télécharger et notifier installation + redémarrage |
| B release | Mise à jour de sécurité du Patch Tuesday |
| Baseline (hotpatch) | Mois avec cumulative classique et redémarrage, sur lequel s'appuient les hotpatchs suivants |
| BITS | Service de téléchargement en arrière-plan |
| Build | Numéro de compilation d'une version (26200 = 25H2) |
| BYOVD | *Bring Your Own Vulnerable Driver* : charger un pilote signé vulnérable pour désactiver des protections |
| CAB | *Change Advisory Board* : comité de validation des changements |
| catroot2 | Base des catalogues de signatures de Windows |
| CBS | *Component-Based Servicing* : moteur d'installation des composants Windows |
| CERT-FR | Centre gouvernemental français de veille, d'alerte et de réponse aux attaques (ANSSI) |
| Checkpoint | Cumulative de référence (24H2+) que les suivantes complètent |
| Ciblage côté client / serveur | La machine annonce son groupe (stratégie) / l'administrateur la place dans la console |
| Classification | Type de mise à jour dans WSUS (Security Updates, Updates…) |
| Co-gestion | Gestion d'un même parc par ConfigMgr et Intune |
| CVE | Identifiant universel d'une vulnérabilité |
| CVSS | Note de gravité technique d'une vulnérabilité (0 à 10) |
| D release | Ancienne appellation de la préversion non sécurité de la 4e semaine |
| Deadline (échéance) | Date d'installation forcée |
| Declined (refusée) | Masquée de WSUS, plus évaluée ; ne désinstalle rien |
| Delivery Optimization | Partage pair à pair des téléchargements (sources cloud) |
| Dérogation | Exception écrite, datée, validée, avec mesures compensatoires |
| DISM | Outil de gestion des paquets et images Windows |
| Dynamic Update | Paquets utilisés pendant une mise à niveau / installation |
| eKB / enablement package | Petit paquet qui active une version annuelle (24H2 → 25H2 → 26H2) |
| EPSS | Score statistique de probabilité d'exploitation d'une CVE |
| ESU | Correctifs de sécurité payants après la fin de support |
| Exploit Wednesday | Le lendemain du Patch Tuesday, quand les correctifs sont analysés pour produire des exploits |
| Express | Fichiers différentiels d'une cumulative (lourds côté WSUS) |
| Feature update | Mise à jour de fonctionnalités : change la version |
| Fenêtre d'exposition | Durée entre publication d'un correctif et son activation sur la machine |
| Hotpatch | Correctif sans redémarrage (Windows 11 Entreprise via Autopatch/Intune, Server 2025 avec Arc) |
| KB | Numéro d'article Microsoft, et par extension la mise à jour |
| KEV | Catalogue CISA des failles exploitées |
| KIR | *Known Issue Rollback* : désactivation à distance d'un changement non sécurité défectueux |
| LCU | *Latest Cumulative Update* : la cumulative mensuelle |
| LTSC | Canal à support long, sans nouvelles fonctions |
| MCO / MCS | Maintien en condition opérationnelle / de sécurité |
| Modern / Fixed Lifecycle | Politiques de cycle de vie : par version (Windows 11) / à date fixe (serveurs, LTSC) |
| MSRC | *Microsoft Security Response Center* : gravités, Security Update Guide |
| MSRT | Outil mensuel de suppression de logiciels malveillants (KB890830) |
| .msu | Paquet autonome du catalogue |
| n-day / 0-day | Faille corrigée mais encore exploitable / faille exploitée avant correctif |
| OOB | *Out-of-band* : correctif hors calendrier |
| Patch diffing | Comparaison avant/après d'un correctif pour en déduire la faille |
| Patch Tuesday | 2e mardi du mois, ~19 h à Paris |
| pending.xml | Liste des opérations CBS à appliquer au redémarrage |
| Préversion non sécurité | *Optional non-security preview* : cumulative facultative de la 4e semaine |
| Quality update | Mise à jour de qualité : correctifs mensuels |
| Remplacée (*superseded*) | Rendue inutile par une plus récente |
| Réplica | WSUS aval qui reprend groupes et approbations de l'amont |
| Révision | Nouvelle version des métadonnées d'une mise à jour WSUS |
| Safeguard hold | Blocage automatique d'une mise à niveau sur les machines à incompatibilité connue (sources cloud) |
| Secure Boot | Vérification de la signature des composants de démarrage par le firmware |
| Socle (*platform release*) | Base de code commune à plusieurs versions (26100 pour 24H2/25H2/26H2) |
| SSU | *Servicing Stack Update* : mise à jour du moteur d'installation |
| SUSDB | Base de données de WSUS |
| SusClientId | Identifiant unique d'un client WSUS |
| TargetGroup | Valeur de stratégie : nom du groupe WSUS de la machine |
| TrustedInstaller | Service qui installe les paquets (*Windows Modules Installer*) |
| UBR | *Update Build Revision* : le numéro après le build, niveau de cumulative |
| UpdateID | GUID d'une mise à jour dans WSUS |
| UsoSvc | *Update Orchestrator* : planification et redémarrages |
| UUP | Plateforme de livraison unifiée de Windows Update |
| WaaSMedicSvc | Service qui répare les composants Windows Update |
| WebView2 | Composant Edge embarqué par de nombreuses applications |
| WID | *Windows Internal Database* : base locale gratuite de WSUS |
| WinSxS | Magasin de composants de Windows |
| WSUS | *Windows Server Update Services* |
| WsusPool | Pool IIS de WSUS (son arrêt = erreur 503 / 0x80244022) |
| WUA | *Windows Update Agent* : l'agent client (`wuauserv`) |
| WUfB | *Windows Update for Business*, aujourd'hui « stratégies client Windows Update » : anneaux et reports depuis le cloud |

---


## Annexe B — Cheat sheet

**Identifier une machine**

```powershell
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object ProductName, EditionID, DisplayVersion, CurrentBuild, UBR
winver
```


**État des mises à jour**

```powershell
Get-WindowsPackage -Online | Where-Object PackageName -match 'ServicingStack|RollupFix' | Select-Object PackageName, InstallTime
DISM /Online /Get-Packages /Format:Table
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending'
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
```


**Installer / retirer**

```powershell
wusa C:\Temp\<fichier>.msu /quiet /norestart
DISM /Online /Add-Package /PackagePath:C:\Temp\<fichier>.msu
DISM /Online /Remove-Package /PackageName:<Package_for_RollupFix~…>
```


**Journaux**

```powershell
Get-WindowsUpdateLog
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WindowsUpdateClient'; Id=19,20} -MaxEvents 20
Select-String -Path C:\Windows\Logs\CBS\CBS.log -Pattern 'error|failed' | Select-Object -Last 30
```


**Réparer**

```powershell
DISM /Online /Cleanup-Image /AnalyzeComponentStore
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```


**Client WSUS**

```powershell
Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'
Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU'
gpresult /r /scope computer
Test-NetConnection <serveur-wsus> -Port 8531
(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()
```


**Serveur WSUS**

```powershell
Get-WsusUpdate -Classification Security -Approval Unapproved -Status FailedOrNeeded
Get-WsusUpdate -UpdateId '<GUID>' | Approve-WsusUpdate -Action Install -TargetGroupName '<groupe>'
Get-WsusComputer -All | Where-Object { $_.LastReportedStatusTime -lt (Get-Date).AddDays(-14) }
(Get-WsusServer).GetComputerTargets() | Group-Object OSDescription | Select-Object Count, Name
Invoke-WsusServerCleanup -DeclineSupersededUpdates -DeclineExpiredUpdates -CleanupObsoleteUpdates -CleanupUnneededContentFiles -CompressUpdates -CleanupObsoleteComputers
```


```cmd
"C:\Program Files\Update Services\Tools\wsusutil.exe" checkhealth
"C:\Program Files\Update Services\Tools\wsusutil.exe" reset
sqlcmd -S np:\\.\pipe\MICROSOFT##WID\tsql\query -i C:\Scripts\WsusDBMaintenance.sql
```


**Repères**

| Repère | Valeur |
|---|---|
| Patch Tuesday | 2e mardi, ~19 h Paris |
| Préversion non sécurité | 4e semaine |
| Ports WSUS | 8530 (HTTP), **8531 (HTTPS)** |
| Événements client | 19 réussite, 20 échec, 43 installation, 44 téléchargement |
| Build Windows 11 | ≥ 22000 ; 24H2 = 26100, 25H2 = 26200, 26H2 = 26300, 26H1 = 28000 |
| Server 2016 / 2019 / 2022 / 2025 | 14393 / 17763 / 20348 / 26100 |
| Bases hotpatch | janvier, avril, juillet, octobre (+ imprévues) |

---


## Annexe C — Calendrier type et checklists

**C.1 Calendrier mensuel (J = Patch Tuesday)**

| Jour | Action | Fait |
|---|---|---|
| J soir | synchronisation WSUS ; lecture gravités, *Exploited*, avis CERT-FR | ☐ |
| J+1 | fiche de veille ; qualification ; applicatifs → pilote ; voie d'urgence si P0 | ☐ |
| J+1 à J+8 | suivi des retours (support, communauté, *known issues*) | ☐ |
| J+8 | applicatifs → production ; système → pilote | ☐ |
| J+15 | système → production postes ; serveurs par vagues | ☐ |
| J+22 | nettoyage WSUS ; réindexation SUSDB ; rapport de conformité ; préversion sur pilote IT | ☐ |
| En continu | Edge (2 passes/semaine) ; Defender (automatique) ; OOB | ☐ |
| Janvier | publier le calendrier annuel en tenant compte des jours fériés et congés | ☐ |

**C.2 Fiche de veille mensuelle**

```
Mois : ____________   Patch Tuesday : ___/___/______   Rédigé par : __________

CVE exploitées (Exploited = Yes) ou divulguées :
  CVE              Produit / composant   Présent chez nous ?   Exposé ?   Priorité (P0-P3)
  ______________   ___________________   _________________     ________   ________________

KB du mois par produit :
  Windows 11 24H2/25H2/26H2 : KB________   Windows 10 ESU : KB________
  Server 2016 (SSU + LCU) : KB________ / KB________   Server 2019 : KB________
  Server 2022 : KB________   Server 2025 : KB________   .NET : KB________

Known issues lues (KB + release health) : ☐ oui   Points d'attention : ______________
Décision CAB / RSSI : ___________________________   Date : ___/___/______
```


**C.3 Checklist avant déploiement**

- ☐ Page KB lue, *Known issues* et prérequis (SSU, checkpoint) vérifiés
- ☐ Windows release health consulté pour chaque version du parc
- ☐ Retours du pilote collectés (référents métier) ; aucun ticket corrélé ouvert
- ☐ Approbation sur le **bon groupe** (jamais *Tous les ordinateurs* par défaut)
- ☐ Échéance et comportement de redémarrage conformes à la politique
- ☐ Fenêtres de maintenance serveurs confirmées ; sauvegardes/instantanés vérifiés
- ☐ Communication aux utilisateurs si redémarrage forcé

**C.4 Checklist après déploiement**

- ☐ Taux d'installation par groupe (WSUS) à J+1, J+3, J+7
- ☐ Échecs analysés (code, journal) et regroupés par cause
- ☐ Redémarrages en attente > 3 jours relancés
- ☐ UBR vérifié sur un échantillon et par l'inventaire
- ☐ Machines silencieuses (> 14 jours) listées
- ☐ Dérogations mises à jour

**C.5 Modèle de dérogation**

```
Référence : DER-AAAA-NNN          Demandeur : ______________   Date : ___/___/______
Machines concernées : ________________________________________________
Correctif(s) non installé(s) : KB________ (CVE principales : ______________)
Raison : _____________________________________________________________
Mesures compensatoires : ☐ isolement réseau  ☐ service désactivé  ☐ surveillance SOC renforcée
                         ☐ autre : ____________________________________
Date de fin (obligatoire) : ___/___/______    Revue à chaque cycle : ☐
Validation RSSI : ______________   Date : ___/___/______
```


**C.6 Voie d'urgence (mémo)**

1. Qualification P0 écrite (CVE, exposition, actifs) — H+4 au plus.
2. Décision RSSI ; information du CAB.
3. Import si besoin (catalogue), approbation pilote IT, tests de fumée.
4. Production avec échéance courte et redémarrage forcé ; mesures temporaires en parallèle.
5. Vérification (UBR, WSUS, scanner) ; compte rendu.

---


## Annexe D — Erreurs fréquentes et faux positifs

| # | Situation | Pourquoi c'est trompeur | Bonne lecture |
|---|---|---|---|
| 1 | Machine « 100 % conforme » dans WSUS | elle est en version **hors support** : plus rien n'est applicable | croiser conformité et version (Ch.3) |
| 2 | `ProductName` = « Windows 10 » | valeur figée sur beaucoup de Windows 11 | build ≥ 22000 = Windows 11 |
| 3 | « Installée » dans WSUS | **redémarrage en attente** : correctif inactif | suivre l'état *Pending Reboot* (Ch.7) |
| 4 | Scanner : « KB manquante » | KB **remplacée** par la cumulative suivante, déjà installée | vérifier l'UBR |
| 5 | `Get-HotFix` ne montre pas la KB | ne voit qu'une partie des paquets | `Get-WindowsPackage`, UBR |
| 6 | 24H2 et 25H2 ont le même UBR | même socle, même cumulative | lire build **et** UBR |
| 7 | « Je n'ai rien approuvé et ça s'installe » | source mixte (stratégie cloud), Edge Update libre | vérifier les stratégies de source (Ch.9, 13) |
| 8 | Une machine « clignote » entre deux noms | **SusClientId dupliqué** (clone) | réinitialiser l'identifiant (Ch.9) |
| 9 | Échec massif soudain 0x80244022 | ce n'est pas le poste : **WsusPool arrêté** | IIS, maintenance (Ch.10) |
| 10 | « 2e mercredi = lendemain du Patch Tuesday » | faux quand le mois commence un mercredi | raisonner en J+n (Ch.5) |
| 11 | Supprimer `SoftwareDistribution` en premier | efface les traces, masque la cause | lire les journaux d'abord (Ch.8) |
| 12 | Approuver sur *Tous les ordinateurs* | l'héritage approuve **tout le parc** | approuver par groupe |
| 13 | Refuser une mise à jour pour la « retirer » | refuser ne désinstalle rien | retirer l'approbation / approuver pour suppression / KIR |
| 14 | CVSS 9.8 = urgence absolue | le composant peut être absent ou non exposé | grille de qualification (Ch.6) |
| 15 | Régression lue sur un forum = suspendre tout | cas isolé possible | chercher confirmation, reproduire sur le pilote |
| 16 | `/ResetBase` pour gagner de la place | rend les mises à jour non désinstallables | réservé aux images de référence |
| 17 | Machine « Inconnu » depuis des semaines | elle ne contacte plus WSUS : état périmé | liste des silencieux > 14 jours |
| 18 | Mise à niveau via WSUS sans vérifier les incompatibilités | pas de blocages de protection automatiques hors cloud | consulter Windows release health avant |

---


## Annexe E — Sources de veille et formation continue

**À suivre en priorité**

| Source | Usage |
|---|---|
| Microsoft **Security Update Guide** (msrc.microsoft.com/update-guide) | CVE, KB, gravités, *Exploited* |
| **Windows release health** (learn.microsoft.com/windows/release-health) | problèmes connus, versions, fins de support, calendrier hotpatch |
| **Windows 11 release information** | correspondance KB ↔ build ↔ date |
| **Windows IT Pro Blog** (Tech Community) | annonces de changements |
| **Message Center** Microsoft 365 | changements planifiés (si tenant Microsoft 365) |
| **CERT-FR** (cert.ssi.gouv.fr) | avis, alertes, bulletin d'actualité |
| **CISA KEV** | failles exploitées (RSS, JSON) |
| Notes de version **Microsoft Edge** (sécurité et Stable) | cycle Edge |
| Mégafil *Patch Tuesday* de r/sysadmin, liste patchmanagement.org | retours de terrain |
| Documentation Microsoft *WSUS maintenance guide* | entretien de WSUS |

**Pour aller plus loin**

- **ANSSI** : *Guide d'hygiène informatique* (mesures sur les mises à jour) et publications sur l'administration sécurisée des systèmes Active Directory.
- **NIST SP 800-40 Rév. 4** : guide de planification de la gestion des correctifs d'entreprise (2022).
- **Microsoft Learn** : parcours sur la gestion des mises à jour Windows, Intune, Windows Autopatch, Azure Update Manager.
- **Certifications Microsoft** liées (à vérifier sur Microsoft Learn, le catalogue évolue) : *Endpoint Administrator* (MD-102) pour Intune et les postes ; *Windows Server Hybrid Administrator* pour les serveurs.
- Cours de la bibliothèque : *Windows en profondeur* (architecture, journaux), *Active Directory* (GPO, tiering), *Réponse à incident* (réagir à une compromission de WSUS), *Infrastructure IT*.

---


## Annexe F — Correspondance avec la version complète

| Guide d'intégration | Version complète |
|---|---|
| Ch.1 — Pourquoi on met à jour | Ch.1 |
| Ch.2 — Identifier un Windows | Ch.2, Ch.3 |
| Ch.3 — Cycle de vie | Ch.4 |
| Ch.4 — Types de mises à jour | Ch.5 (+ Ch.25 pour firmware et Secure Boot) |
| Ch.5 — Calendrier | Ch.6 |
| Ch.6 — Qualifier, veille | Ch.7, Ch.8 |
| Ch.7 — De la mise à jour au redémarrage | Ch.9, Ch.10, Ch.11 |
| Ch.8 — Outils, journaux, dépannage | Ch.12, Ch.13 |
| Ch.9 — Sources et fonctionnement de WSUS | Ch.14, Ch.15 |
| Ch.10 — Cycle mensuel et entretien WSUS | Ch.16, Ch.17 |
| Ch.11 — Sécuriser WSUS | Ch.18 |
| Ch.12 — Cycle de patch management | Ch.19 à Ch.23 |
| Ch.13 — Edge | Ch.24 |
| Ch.14 — Après WSUS | Ch.26, Ch.27 (et Ch.25 pour M365 Apps et applications tierces) |

---

*Fin du guide — version 1.0, novembre 2026. Les dates, numéros de KB et statuts cités sont à revérifier sur les sources officielles avant toute décision.*
