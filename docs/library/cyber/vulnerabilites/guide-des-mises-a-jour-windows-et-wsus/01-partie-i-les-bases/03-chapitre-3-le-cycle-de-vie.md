---
title: Chapitre 3 — Le cycle de vie
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie I — Les bases
  - index.md
---

combien de temps une version est corrigée

> 🧱 **Les bases**
>
> - **Fin de service** (*end of servicing*, *end of updates*) : date après laquelle Microsoft ne publie **plus aucun correctif**, même de sécurité, pour cette version. La machine continue de démarrer, mais chaque nouvelle faille découverte reste ouverte pour toujours.
> - **Support standard / étendu** (*mainstream / extended*) : pour les produits à cycle fixe (serveurs, LTSC). Pendant le support standard : correctifs de sécurité + améliorations. Pendant le support étendu : **correctifs de sécurité uniquement**. Après : plus rien.

## 3.1 Les deux politiques de Microsoft

| Politique | Produits | Principe |
|---|---|---|
| **Modern Lifecycle Policy** | Windows 11 (hors LTSC), Microsoft 365 Apps, Edge | chaque **version** a une durée de vie fixe (24 ou 36 mois) ; rester supporté = **changer de version** régulièrement |
| **Fixed Lifecycle Policy** | Windows Server, Windows 11 LTSC, Office en licence perpétuelle | une date de fin annoncée dès la sortie (typiquement 5 ans standard + 5 ans étendu) |

## 3.2 Les durées

| Produit | Durée de support | Remarque |
|---|---|---|
| Windows 11 Famille / Pro (version annuelle) | **24 mois** | changer de version tous les 2 ans au plus |
| Windows 11 **Entreprise / Éducation** | **36 mois** | une mise à niveau annuelle, ou tous les deux ans, en entreprise |
| Windows 11 Entreprise **LTSC** 2024 | 5 ans (IoT LTSC : 10 ans) | pas de nouvelles fonctions ; pour les systèmes figés (industrie, santé, kiosques) |
| Windows Server (LTSC) | 5 ans standard + 5 ans étendu | |
| Windows 10 | fin le **14 octobre 2025** | puis **ESU** payantes (organisations : jusqu'à 3 ans) |

## 3.3 Le calendrier concret (vérifié en novembre 2026)

**Windows 11**

| Version | Famille / Pro | Entreprise / Éducation |
|---|---|---|
| 22H2 | terminée (8 oct. 2024) | terminée (14 oct. 2025) |
| 23H2 | terminée (11 nov. 2025) | **10 novembre 2026** — le Patch Tuesday de novembre 2026 est la dernière mise à jour |
| 24H2 | terminée (**13 oct. 2026**) | 12 octobre 2027 |
| 25H2 | 12 octobre 2027 | 10 octobre 2028 |
| 26H2 | octobre 2028 (24 mois) | 9 octobre 2029 |
| 26H1 (PC neufs) | 14 mars 2028 | 13 mars 2029 |

**Windows Server et Windows 10**

| Produit | Échéance |
|---|---|
| Windows Server 2016 | fin du support étendu : **12 janvier 2027** |
| Windows Server 2019 | fin du support étendu : janvier 2029 |
| Windows Server 2022 | fin du support étendu : octobre 2031 |
| Windows Server 2025 | fin du support étendu : novembre 2034 |
| Windows 10 22H2, ESU commerciales | année 1 terminée le 13 oct. 2026 ; **année 2 du 14 oct. 2026 au 12 oct. 2027** ; année 3 jusqu'au 10 oct. 2028 |
| Windows 10, ESU grand public | prolongées jusqu'au **12 octobre 2027** (annonce de juin 2026) |
| Windows 10 Entreprise LTSB 2016 | fin le 13 octobre 2026 (programme ESU spécifique) |

> ⚠️ **Piège — Les dates bougent**
>
> Microsoft a prolongé les ESU grand public de Windows 10 en juin 2026, par une simple note ajoutée à un billet de blog. Beaucoup de documents citent encore l'ancienne date. **Règle : une date de fin de support se vérifie à la source** (pages *Lifecycle* et *Windows release health* de Microsoft) au moment de la décision.

## 3.4 Les ESU (*Extended Security Updates*)

Les ESU sont des **correctifs de sécurité payants** (critiques et importants uniquement, pas de nouvelles fonctions ni de correctifs non sécurité) pour un produit arrivé en fin de support.

- **Mécanisme** : on achète une licence par machine et par an ; on installe et active une **clé ESU** sur la machine (pour Windows 10 commercial, avec `slmgr /ipk` puis `slmgr /ato` et l'identifiant d'activation de l'année). Une fois activée, la machine voit les mises à jour ESU via Windows Update ou WSUS comme une cumulative normale.
- **Coût** : pour Windows 10 commercial, le prix **double chaque année** (environ 61 $, puis 122 $, puis 244 $ par poste) et les années sont **cumulatives** : on ne peut pas acheter l'année 2 sans l'année 1.
- **Piège** : une machine dont la clé ESU n'est pas activée n'a **aucune** mise à jour applicable. Dans WSUS, elle paraît « à jour ».

> ⚠️ **Piège majeur — « À jour » ne veut pas dire « protégée »**
>
> Une machine en version **non supportée** (23H2 Entreprise après le 10 novembre 2026, Windows 10 sans ESU…) ne reçoit plus de cumulative. Pour WSUS, il n'existe donc **aucune mise à jour applicable** : elle apparaît **verte, conforme, à 100 %**… alors qu'elle accumule chaque mois de nouvelles failles non corrigées. Le rapport de conformité doit **toujours être croisé avec la version** de chaque machine.

```powershell
# Dans WSUS : versions présentes dans le parc (sur le serveur WSUS, module UpdateServices)
(Get-WsusServer).GetComputerTargets() |
    Group-Object OSDescription, ClientVersion |
    Select-Object Count, Name | Sort-Object Count -Descending
```


## 3.5 Piloter un parc par le cycle de vie

Une équipe MCS tient à jour un **tableau d'obsolescence** : pour chaque couple produit/version, le nombre de machines, la date de fin de service, l'action prévue (mise à niveau, remplacement, ESU, isolement) et le responsable. On le revoit chaque mois, et on alerte au plus tard **6 mois** avant une échéance (le temps de tester une mise à niveau, de commander du matériel, de négocier une dérogation).

> 🧵 **Fil rouge — Lundi 2 novembre 2026**
>
> Le tableau d'obsolescence d'Inès indique encore **140 postes en 23H2 Entreprise**, dont 40 dans une agence de Lille où l'application de tiers payant ne fonctionne pas en 25H2. Échéance : **mardi 10 novembre**. La RSSI tranche avec le CAB : mise à niveau en 26H2 des 100 postes compatibles avant le 10 ; pour les 40 postes de Lille, dérogation de 30 jours, isolement réseau renforcé et pression sur l'éditeur. Sans ce tableau, ces 140 postes seraient restés « verts » dans WSUS jusqu'à la prochaine attaque.

> 📌 **À retenir**
>
> - Windows 11 : 24 mois (Famille/Pro), 36 mois (Entreprise/Éducation) par version ; serveurs : 5 + 5 ans.
> - Prochaines échéances : 23H2 Entreprise le 10 novembre 2026, Server 2016 le 12 janvier 2027.
> - Une machine hors support paraît **conforme** dans WSUS : toujours croiser conformité **et** version.

---
