---
title: 'Chapitre 2 — Identifier un Windows : édition, version, build, UBR'
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie I — Les bases
  - index.md
---

> 🧱 **Les bases**
>
> - Le **registre** Windows est une base de configuration hiérarchique (clés et valeurs). `HKLM` (*HKEY_LOCAL_MACHINE*) contient les réglages de la machine.
> - **PowerShell** est le langage de commande et de script de Windows. Une commande s'appelle une *cmdlet* (`Get-ItemProperty`, `Get-CimInstance`…).
> - **WMI / CIM** est une interface standard pour interroger l'état d'une machine (système, matériel, logiciels).

## 2.1 Produit, édition, version, build, révision

cinq choses différentes

C'est la confusion n°1 des débutants. Ces cinq notions répondent à des questions distinctes.

| Terme | Exemple | Ce que ça désigne | Question à laquelle ça répond |
|---|---|---|---|
| **Produit** | Windows 11, Windows Server 2025 | la famille | « Quel système ? » |
| **Édition** | Famille, Professionnel, **Entreprise**, Éducation, LTSC ; Server Standard / Datacenter | les fonctions disponibles et la licence | « Quels droits, quelle durée de support ? » |
| **Version** | **24H2**, **25H2**, **26H2** | la mouture annuelle | « Quel millésime ? » |
| **Build** | 26200 | le numéro de compilation de cette version | « Quelle base de code ? » |
| **Révision (UBR)** | 26200.**9818** | le niveau de correctifs installé | « Quel mois de correctifs ? » |

Le numéro complet s'écrit `Majeur.Mineur.Build.UBR`, par exemple `10.0.26200.9818` :

- **Majeur.Mineur = 10.0** : resté figé depuis Windows 10, même sous Windows 11, pour des raisons de compatibilité des applications (beaucoup de logiciels testent « version ≥ 10 »). **Ce n'est donc pas lui qui distingue Windows 10 de Windows 11.**
- **Build** : distingue les versions. **Build ≥ 22000 = Windows 11.**
- **UBR** (*Update Build Revision*) : augmente à chaque mise à jour cumulative. C'est **la preuve technique** du niveau de correctifs d'une machine (Ch.4).

## 2.2 Que veut dire « 25H2 » ?

**AA H n** = année + semestre (*Half*). **25H2** = version du second semestre 2025. Microsoft a adopté ce format en 2020 ; avant, c'était **AAMM** (année + mois prévu).

| Époque | Versions | Rythme |
|---|---|---|
| Windows 10, 2015-2020 | 1507, 1511, 1607, 1703, 1709, 1803, 1809, 1903, 1909, 2004 | deux par an |
| Windows 10, 2020-2022 | 20H2, 21H1, 21H2, **22H2** (dernière) | deux puis une par an |
| Windows 11 | 21H2, 22H2, 23H2, **24H2**, **25H2**, **26H2** (+ 26H1, cas à part) | **une par an**, au second semestre |

## 2.3 Les builds de Windows 11 et le principe du « socle »

| Version | Build | Note |
|---|---|---|
| 21H2 | 22000 | première version de Windows 11 |
| 22H2 | 22621 | |
| 23H2 | 22631 | 22H2 + enablement package |
| **24H2** | **26100** | **nouveau socle** (nom de code « Germanium »), le même que Windows Server 2025 |
| **25H2** | **26200** | 24H2 + enablement package : **mêmes cumulatives** |
| **26H2** | **26300** | publiée le 29 septembre 2026, disponible pour tous les PC éligibles depuis le 21 octobre 2026 ; 24H2/25H2 + enablement package |
| 26H1 | 28000 | **autre socle**, réservé à certains PC neufs (puces Arm récentes, Snapdragon X2 notamment) ; pas de passage direct 26H1 → 26H2 |

**Le socle** (*platform release*) est la base de code commune. Quand plusieurs versions partagent le même socle, elles reçoivent **la même mise à jour cumulative**, et seul le build diffère.

> 💡 **Exemple — Même UBR, versions différentes**
>
> La préversion d'octobre 2026 (KB5127936) a porté 26H2 et 25H2 aux builds **26300.9818** et **26200.9818**. Le même UBR (9818) sur deux builds différents : c'est la signature de deux versions sur le même socle. La version 26H1, elle, a reçu un paquet distinct (KB5127653, build 28000.3365).

**Enablement package** (*eKB*) : un tout petit paquet (quelques centaines de Ko) qui **active** des fonctions déjà présentes, mais en sommeil, dans les cumulatives. Un seul redémarrage, et la version change (24H2 → 25H2 → 26H2). Ce n'est possible **que si les deux versions partagent le même socle**. Sinon, il faut une **mise à niveau complète** (réinstallation sur place, environ une heure, plusieurs Go) : par exemple 23H2 → 24H2.

## 2.4 Windows Server

| Version | Build | Canal | Particularité pour le patching |
|---|---|---|---|
| Windows Server 2016 | 14393 | LTSC | SSU encore séparées (Ch.4) |
| Windows Server 2019 | 17763 | LTSC | |
| Windows Server 2022 | 20348 | LTSC | |
| **Windows Server 2025** | **26100** | LTSC | dans WSUS : produit **« Microsoft Server Operating System-24H2 »** |

Server 2025 et Windows 11 24H2 partagent le socle 26100 : leurs cumulatives sont **distinctes** (KB différentes), publiées le même jour, avec des correctifs très proches. Une faille du socle touche donc souvent les deux.

> ⚠️ **Piège — Le nom de produit dans WSUS**
>
> WSUS ne range pas toujours les mises à jour sous le nom commercial. Server 2025 apparaît comme *Microsoft Server Operating System-24H2* ; Windows 11 a des produits par version. Si le bon produit n'est pas coché, les mises à jour n'arrivent jamais dans WSUS et les machines apparaissent… à jour (rien d'applicable). Voir Ch.9.

## 2.5 Lire l'identité d'une machine

```powershell
# La source la plus fiable : le registre
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' |
    Select-Object ProductName, EditionID, DisplayVersion, CurrentBuild, UBR

# Résultat typique
# ProductName    : Windows 10 Enterprise     <-- piège, voir ci-dessous
# EditionID      : Enterprise
# DisplayVersion : 25H2
# CurrentBuild   : 26200
# UBR            : 9818

winver          # fenêtre « À propos de Windows » : version + build complet

Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object ProductName, DisplayVersion, CurrentBuild, UB

# ProductName    DisplayVersion CurrentBuild  UBR
# -----------    -------------- ------------  ---
# Windows 10 Pro 26H2           26300        9711

# Construire le numéro complet
$cv = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
"10.0.$($cv.CurrentBuild).$($cv.UBR)"
```


| Source | Donne la version (25H2) ? | Donne l'UBR ? | Fiabilité |
|---|---|---|---|
| Registre `CurrentVersion` | oui (`DisplayVersion`) | **oui** (`UBR`) | **la référence** |
| `winver` | oui | oui | bonne, mais manuelle |
| `Get-CimInstance Win32_OperatingSystem` | non (Caption + BuildNumber) | **non** | partielle |
| `[Environment]::OSVersion` | non | **non** | partielle |
| Console WSUS (*OS Version*) | indirectement | oui | dépend du dernier rapport du client |

> ⚠️ **Pièges classiques**
>
> - `ProductName` affiche encore **« Windows 10 »** sur beaucoup de Windows 11. **Le build fait foi : ≥ 22000 = Windows 11.**
> - `ReleaseId` est figé à « 2009 » depuis Windows 10 20H2 : il ne faut plus l'utiliser. Utilisez `DisplayVersion`.
> - 24H2, 25H2 et 26H2 ont **le même UBR** pour un même mois : l'UBR seul ne dit pas la version ; il faut le couple **build + UBR**.
> - Un inventaire qui ne remonte que `Win32_OperatingSystem` ne peut pas prouver le niveau de correctifs (pas d'UBR).

> 🧵 **Fil rouge — Semaine du 5 janvier 2026**
>
> Karim demande à Inès de compter les postes par version. Elle obtient trois chiffres différents : l'outil d'inventaire (basé sur `Win32_OperatingSystem`) voit « 1 200 Windows 10 », la console WSUS en voit 60, l'Active Directory en voit 410 (attribut `operatingSystem` mis à jour irrégulièrement). Le registre, interrogé à distance, tranche : 60 Windows 10 réels, tous les autres sont des Windows 11 dont `ProductName` est trompeur. Première leçon : **toujours savoir d'où vient un chiffre**.

> 📌 **À retenir**
>
> - Édition = droits et durée de support ; version = millésime ; build = base de code ; **UBR = niveau de correctifs**.
> - Build ≥ 22000 = Windows 11 ; 24H2/25H2/26H2 partagent le socle 26100 et les mêmes cumulatives.
> - La source fiable est le registre (`DisplayVersion`, `CurrentBuild`, `UBR`).

---
