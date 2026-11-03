---
title: Chapitre 4 — Les types de mises à jour
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie II — Comprendre les mises à jour
  - index.md
---

> 🧱 **Les bases**
>
> - Un **paquet** est un fichier qui contient des fichiers à installer et les instructions pour le faire (Ch.7).
> - **Cumulatif** veut dire « qui contient tout ce qui précède ». Une mise à jour cumulative de novembre contient aussi les correctifs d'octobre, de septembre, etc.
> - **Remplacer** (*supersede*) : une mise à jour plus récente rend une ancienne inutile, parce qu'elle fait la même chose et plus.

## 4.1 Les deux grandes familles

| | **Mise à jour de fonctionnalités** (*feature update*) | **Mise à jour de qualité** (*quality update*) |
|---|---|---|
| Change | la **version** (24H2 → 25H2) | le **niveau de correctifs** (UBR) |
| Rythme | annuel | mensuel (+ urgences) |
| Taille / durée | quelques Ko (enablement package) à plusieurs Go (mise à niveau), 30 à 90 min | quelques centaines de Mo, 10 à 30 min |
| Contenu | fonctions nouvelles, nouvelle durée de support | sécurité + corrections |
| Classification WSUS | **Upgrades** | Security Updates, Updates, Critical Updates… |
| Gestion en entreprise | un **projet** (compatibilité applicative, pilote long, communication) | le **cycle mensuel** |

Depuis 25H2, Microsoft livre de plus en plus de nouveautés **au fil des cumulatives mensuelles** (souvent désactivées puis activées progressivement), et la version annuelle sert surtout à **renouveler la durée de support**. La frontière « fonctionnalité / qualité » est donc moins nette qu'avant : une cumulative peut modifier l'interface.

## 4.2 La cumulative mensuelle (LCU)

**LCU** (*Latest Cumulative Update*) : la mise à jour mensuelle de Windows. Elle contient **tous** les correctifs de sécurité et de qualité publiés pour cette version.

- **Une seule à installer** : celle du mois remplace toutes les précédentes. Un poste qui a six mois de retard n'a besoin que de la dernière.
- Elle fait monter l'**UBR**. La correspondance UBR ↔ KB ↔ date est publiée sur la page *Windows 11 release information* de Microsoft.
- Titre type : `2026-11 Cumulative Update for Windows 11, version 25H2 for x64-based Systems (KB50xxxxx)`.
- Elle **inclut la SSU** (§4.4) depuis 2021 sur les systèmes récents.
- On ne la désinstalle qu'avec `DISM /Online /Remove-Package` (la partie SSU, elle, reste toujours).

**Pourquoi le modèle cumulatif ?** Jusqu'en 2016 (Windows 7 / 8.1), chaque correctif était une KB séparée : des centaines de KB par machine, des combinaisons impossibles à tester (« la machine A a les KB 1 à 40 sauf la 17 »). Le modèle cumulatif a rendu les parcs homogènes et testables, mais il a rendu le choix **binaire** : on prend **tout** le mois, ou rien. Si un correctif du mois casse une application, on ne peut pas l'écarter seul ; on suspend toute la cumulative, ou on utilise un mécanisme comme le KIR (§4.6).

> 💡 **Exemple — Lire une cumulative**
>
> `2026-07 Cumulative Update for Windows 11, version 25H2 for x64-based Systems (KB5101650)` → juillet 2026, Windows 11, version 25H2, processeurs x64. Elle a porté 24H2 et 25H2 aux builds 26100.8875 et 26200.8875.

## 4.3 Le checkpoint (Windows 11 24H2+, Server 2025)

Les cumulatives grossissaient chaque mois (elles contiennent tout depuis la sortie de la version). Pour limiter leur taille, Microsoft publie de temps en temps une cumulative **de référence**, le **checkpoint** (le premier : **KB5043080**, septembre 2024). Les cumulatives suivantes ne contiennent que **les différences depuis le dernier checkpoint**.

- Une machine doit avoir le checkpoint **avant** de prendre une cumulative plus récente.
- Avec Windows Update et WSUS, l'agent gère cet ordre **tout seul**.
- Avec le **catalogue** (installation manuelle, préparation d'images), c'est à l'administrateur d'installer les checkpoints **dans l'ordre**. Le catalogue liste alors plusieurs fichiers .msu pour une même KB.

> ⚠️ **Piège** — Installer à la main « la dernière KB » sur une image 24H2 sans son checkpoint : échec d'installation. Lire la section *How to get this update* de la page KB, qui indique les prérequis.

## 4.4 La pile de maintenance (SSU)

La **pile de maintenance** (*servicing stack*) est le « moteur » qui installe les mises à jour : le service *Windows Modules Installer* (**TrustedInstaller**) et la **CBS** (*Component-Based Servicing*, Ch.7). La **SSU** (*Servicing Stack Update*) est la mise à jour de ce moteur.

- **Logique historique** : on met à jour le moteur **avant** de lui faire installer une cumulative qui a besoin de ses nouvelles capacités. D'où la règle **« SSU d'abord, cumulative ensuite »**, et beaucoup d'échecs quand la SSU manquait.
- **Depuis 2021** (Windows 10 2004 et ultérieurs, Windows 11, Server 2022, Server 2025) : SSU et cumulative sont **combinées dans un seul paquet**. Plus d'ordre à gérer, mais :
    - la SSU ne se désinstalle **jamais** ;
    - `wusa /uninstall /kb:…` ne fonctionne plus sur ce paquet combiné : on passe par `DISM /Online /Remove-Package` avec le nom du paquet `Package_for_RollupFix…`.
- **Encore séparées** sur Windows Server 2016 (et Windows 10 1607 LTSB) : la SSU est une KB à part, déclarée comme **prérequis** de la cumulative dans WSUS. **On approuve les deux.**

```powershell
# Voir les paquets SSU et cumulatives installés
Get-WindowsPackage -Online |
    Where-Object PackageName -match 'ServicingStack|RollupFix' |
    Select-Object PackageName, InstallTime
```


## 4.5 L'enablement package (eKB)

Rappel du Ch.2 : un petit paquet qui active une version annuelle déjà « contenue » dans les cumulatives (24H2 → 25H2 → 26H2). Pour l'équipe MCS, c'est une **mise à jour de fonctionnalités** au sens de la gestion (classification *Upgrades* ou paquet spécifique, test applicatif, communication), mais avec le coût technique d'une cumulative (un redémarrage, quelques minutes).

> ⚠️ **Piège** — Une machine doit être à un **niveau minimal de cumulative** pour accepter l'enablement package. Une machine très en retard le refuse jusqu'à ce qu'elle ait pris la cumulative du mois.

## 4.6 Tous les autres types

| Type | Ce que c'est | Rythme | Dans WSUS |
|---|---|---|---|
| **.NET Framework** | Cumulative séparée pour .NET Framework 3.5 / 4.8.x (pas .NET 8, 9, 10, qui ont leur propre canal et leur propre cycle de vie) | mensuelle, même jour | produit Windows / Server, classification Security Updates |
| **MSRT** (KB890830) | *Malicious Software Removal Tool* : exécuté une fois, cherche des familles de malwares connues, puis s'efface. Ce n'est pas un antivirus | mensuel | *Update Rollups* |
| **Defender – security intelligence** (KB2267602) | Définitions antivirus | **plusieurs fois par jour** | *Definition Updates*, approbation automatique |
| **Defender – plateforme** (KB4052623) et moteur | Le logiciel antivirus lui-même | mensuel | produit *Microsoft Defender Antivirus* |
| **Edge** | Navigateur Chromium : version majeure toutes les 4 semaines, correctifs de sécurité dès que nécessaire | 1 à 2 par semaine | produit **Microsoft Edge**, classification *Updates* (Ch.13) |
| **Office MSI** (2016, 2019…) | Correctifs d'Office installé en MSI | mensuel | produits Office |
| **Microsoft 365 Apps** | Office « Click-to-Run » : canaux Current / Monthly Enterprise / Semi-Annual Enterprise | selon le canal | **pas** par WSUS seul (CDN Microsoft, Intune, ConfigMgr) |
| **Pilotes** (*Drivers*) | Pilotes publiés par les constructeurs via Microsoft | continu | classification *Drivers* ; volumineuse, **synchronisation dépréciée** (2025) : en entreprise, outils du constructeur |
| **Firmware / BIOS / UEFI** | Microcode, firmware, base Secure Boot (*DB*, *DBX*) | rare | parfois via Windows Update, surtout via le constructeur |
| **Dynamic Update** | Paquets utilisés **pendant** une mise à niveau ou une installation : Setup DU, SSU, LCU, **Safe OS** | mensuel | produit « Windows 11 Dynamic Update » |
| **Safe OS / WinRE** | Mise à jour de l'environnement de récupération (WinRE). Exemple : KB5034441 (janvier 2024), échec 0x80070643 si la partition de récupération était trop petite | rare | Security Updates |
| **KIR** (*Known Issue Rollback*) | Microsoft **désactive à distance** une modification **non sécurité** qui pose problème, sans retirer la cumulative. Sur les machines gérées (WSUS), via une **GPO** fournie par Microsoft | à l'occasion | hors WSUS |
| **Hotpatch** | Correctif de sécurité appliqué **en mémoire, sans redémarrage** (détails ci-dessous) | mensuel | hors WSUS |
| **ESU** | Correctifs de sécurité payants après fin de support (Windows 10, Server 2012) | mensuel | oui, si la licence ESU est activée sur la machine |

**Le hotpatch en bref.** Sur Windows 11 Entreprise/Éducation 24H2 et suivantes (gérées par Intune / Windows Autopatch, avec la sécurité basée sur la virtualisation, VBS, activée) et sur Windows Server 2025 (via Azure Arc, payant), le correctif de sécurité est appliqué **directement dans le code en mémoire**, sans redémarrer. Le rythme :

- un **mois de base** (*baseline*) par trimestre — **janvier, avril, juillet, octobre** — avec une cumulative classique et un redémarrage ;
- deux mois **hotpatch** sans redémarrage entre deux bases ;
- des **bases supplémentaires imprévues** quand un correctif ne peut pas être appliqué à chaud. En 2026, c'est arrivé en **juin** (faille divulguée hors processus coordonné) et en **septembre** (composants non modifiables sans redémarrage).

Depuis **mai 2026**, Windows Autopatch active le hotpatch **par défaut** pour les appareils éligibles. Le hotpatch ne passe **pas** par WSUS : il ne concerne donc pas un parc géré uniquement par WSUS (Ch.14).

**Les certificats Secure Boot de 2011 (échéance 2026).** Secure Boot vérifie, au démarrage, que le chargeur de Windows est signé par une autorité de confiance stockée dans le firmware. Les certificats Microsoft d'origine expirent en 2026 : *Microsoft Corporation KEK CA 2011* et *Microsoft UEFI CA 2011* en **juin 2026**, *Microsoft Windows Production PCA 2011* en **octobre 2026**. Les remplaçants « 2023 » sont déployés **par les mises à jour Windows** (avec une tâche planifiée et des clés de registre de suivi depuis octobre 2025), mais certains firmwares refusent la mise à jour et doivent d'abord être mis à jour par le constructeur. Un poste resté sur les seuls certificats de 2011 ne peut plus recevoir de mises à jour Secure Boot (DBX, gestionnaire de démarrage). C'est un bon exemple de mise à jour **qui touche à la fois l'OS et le firmware** (approfondissement : version complète, Ch.25).

## 4.7 Les classifications WSUS

WSUS (Ch.9) range chaque mise à jour dans une **classification**. Ce sont elles qu'on coche, et sur elles qu'on bâtit les règles d'approbation.

| Classification | Contenu typique | Usage courant |
|---|---|---|
| **Security Updates** | cumulatives, .NET, Office MSI | cycle mensuel |
| **Critical Updates** | correctifs critiques non sécurité | cycle mensuel |
| **Updates** | correctifs non sécurité, **Edge** | cycle mensuel / Edge |
| **Update Rollups** | MSRT, regroupements | cycle mensuel |
| **Definition Updates** | Defender (définitions) | **approbation automatique** |
| **Upgrades** | mises à jour de fonctionnalités (nouvelles versions) | projet dédié, **pas cochée par défaut** |
| **Drivers** | pilotes | **à éviter** (volume, dépréciation) |
| Feature Packs, Service Packs, Tools | rares aujourd'hui | au cas par cas |

> 🧵 **Fil rouge — Mardi 13 janvier 2026, 19 h 30**
>
> Premier Patch Tuesday d'Inès. Dans WSUS, après synchronisation : une cumulative par version de Windows 11 et par version de Windows Server, une SSU séparée pour Server 2016, les cumulatives .NET, le MSRT, une mise à jour Edge, des définitions Defender (déjà approuvées automatiquement). Karim lui fait remarquer qu'il n'y a **qu'une seule** cumulative par version à déployer : « Le temps où on comptait les KB est fini. On compte les *versions* et les *exceptions*. »

> 📌 **À retenir**
>
> - Deux familles : **fonctionnalités** (change la version, projet annuel) et **qualité** (change l'UBR, cycle mensuel).
> - Une seule LCU par version et par mois, qui contient tout ; la SSU y est intégrée (sauf Server 2016).
> - Checkpoint : ordre géré par WU/WSUS, à gérer soi-même en installation manuelle.
> - Hotpatch, KIR, Microsoft 365 Apps, firmware : **hors WSUS**.

---
