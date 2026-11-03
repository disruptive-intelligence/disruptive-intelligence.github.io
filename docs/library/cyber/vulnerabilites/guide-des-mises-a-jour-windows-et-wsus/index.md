---
title: Guide des mises à jour Windows et WSUS
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
format: cours
revue: '2026-11-04'
---

*Comprendre • Identifier • Qualifier • Déployer • Entretenir • Sécuriser*

**Version condensée — 14 chapitres • 5 parties • 6 annexes**
**État des connaissances : novembre 2026**

---

## Comment lire ce guide

Aucune connaissance préalable n'est supposée : chaque chapitre commence par un encadré **« Les bases »** qui rappelle les notions nécessaires.

Il est conçu pour être lu **une fois en entier** (comptez une à deux journées), puis gardé sous la main : les annexes (glossaire, cheat sheet, calendrier type, erreurs fréquentes) servent au quotidien.

C'est la version condensée d'un cours plus complet. Quand un sujet est seulement esquissé ici, un renvoi l'indique : *« Approfondissement : version complète, Ch.X »* (la correspondance est en annexe F).

### Les encadrés

| Encadré | Rôle |
|---|---|
| 🧱 **Les bases** | Notions préalables expliquées simplement |
| 🧵 **Fil rouge** | L'histoire (fictive) d'Inès chez ORIAN Mutuelle, qui illustre le chapitre |
| 💡 **Exemple** | Un cas concret, une commande, un chiffre réel |
| ⚠️ **Piège** | Erreur fréquente, faux positif, mauvaise interprétation |
| ✅ **Bonne pratique** | Ce qu'il faut faire |
| 📌 **À retenir** | Le résumé du chapitre en quelques lignes |

### Faits, hypothèses, fiction

- Les **dates Microsoft, numéros de KB, CVE et versions** cités dans le corps du texte sont réels et vérifiés à la date du guide. Ils évoluent : vérifiez toujours sur *Windows release health* et le *Security Update Guide* avant une décision.
- Les **encadrés Fil rouge** sont fictifs (entreprise, personnes, incidents), mais construits sur des situations réelles.
- Quand une information est une tendance ou une estimation, elle est signalée comme telle.

---

## Fil rouge : ORIAN Mutuelle

> 🧵 **Fil rouge — Le décor (fictif)**
>
> **ORIAN Mutuelle** est une mutuelle santé-prévoyance basée à Lyon : 2 400 salariés, 4 sites (Lyon siège, Nantes, Lille, et un datacenter). Elle relève du secteur financier, donc du règlement européen **DORA** (résilience opérationnelle numérique), et traite des données de santé (hébergement **HDS**, **RGPD**).
>
> **Le parc :**
> - environ 3 400 postes Windows 11 Entreprise, en 23H2, 24H2 et 25H2 ;
> - 60 postes Windows 10 sous ESU (numériseurs, laboratoire, poste de l'imprimerie) ;
> - 320 serveurs, de Windows Server 2016 à 2025 ;
> - un WSUS central (« amont ») au datacenter et trois WSUS « aval » sur les sites, base SUSDB sur SQL Server ;
> - des GPO Active Directory pour configurer les postes ; un projet Intune démarre.
>
> **Les personnages :**
> - **Inès Moreau**, ingénieure MCS junior, arrive le lundi 5 janvier 2026. C'est vous.
> - **Karim Benali**, lead MCS, référent WSUS depuis huit ans.
> - **Claire Dumont**, RSSI (responsable de la sécurité des systèmes d'information).
> - **Thomas Leroy**, responsable de l'exploitation serveurs.
> - Le **CAB** (*Change Advisory Board*), comité qui valide les changements chaque semaine.
>
> On suit Inès de janvier à novembre 2026 : premier Patch Tuesday, une mise à jour qui casse l'impression, une faille exploitée à traiter en urgence, un WSUS qui sature, la fin de service de Windows 11 23H2 Entreprise le 10 novembre 2026.

---

## Sommaire

- [Partie I — Les bases](01-partie-i-les-bases/index.md)
    - [Chapitre 1 — Pourquoi on met à jour](01-partie-i-les-bases/01-chapitre-1-pourquoi-on-met-a-jour.md)
    - [Chapitre 2 — Identifier un Windows : édition, version, build, UBR](01-partie-i-les-bases/02-chapitre-2-identifier-un-windows-edition-version-b.md)
    - [Chapitre 3 — Le cycle de vie](01-partie-i-les-bases/03-chapitre-3-le-cycle-de-vie.md)
- [Partie II — Comprendre les mises à jour](02-partie-ii-comprendre-les-mises-a-jour/index.md)
    - [Chapitre 4 — Les types de mises à jour](02-partie-ii-comprendre-les-mises-a-jour/01-chapitre-4-les-types-de-mises-a-jour.md)
    - [Chapitre 5 — Le calendrier Microsoft](02-partie-ii-comprendre-les-mises-a-jour/02-chapitre-5-le-calendrier-microsoft.md)
    - [Chapitre 6 — Identifier et qualifier un correctif, faire sa veille](02-partie-ii-comprendre-les-mises-a-jour/03-chapitre-6-identifier-et-qualifier-un-correctif-fa.md)
- [Partie III — Ce qui se passe dans la machine](03-partie-iii-ce-qui-se-passe-dans-la-machine/index.md)
    - [Chapitre 7 — De la mise à jour au redémarrage](03-partie-iii-ce-qui-se-passe-dans-la-machine/01-chapitre-7-de-la-mise-a-jour-au-redemarrage.md)
    - [Chapitre 8 — Outils, journaux et dépannage de premier niveau](03-partie-iii-ce-qui-se-passe-dans-la-machine/02-chapitre-8-outils-journaux-et-depannage-de-premier.md)
- [Partie IV — WSUS](04-partie-iv-wsus/index.md)
    - [Chapitre 9 — D'où viennent les mises à jour, et comment WSUS fonctionne](04-partie-iv-wsus/01-chapitre-9-d-ou-viennent-les-mises-a-jour-et-comme.md)
    - [Chapitre 10 — Le cycle mensuel dans WSUS et son entretien](04-partie-iv-wsus/02-chapitre-10-le-cycle-mensuel-dans-wsus-et-son-entr.md)
    - [Chapitre 11 — Sécuriser WSUS et la chaîne de mise à jour](04-partie-iv-wsus/03-chapitre-11-securiser-wsus-et-la-chaine-de-mise-a.md)
- [Partie V — Notre pratique](05-partie-v-notre-pratique/index.md)
    - [Chapitre 12 — Le cycle mensuel de patch management](05-partie-v-notre-pratique/01-chapitre-12-le-cycle-mensuel-de-patch-management.md)
    - [Chapitre 13 — Microsoft Edge](05-partie-v-notre-pratique/02-chapitre-13-microsoft-edge.md)
    - [Chapitre 14 — Et demain : l'après-WSUS](05-partie-v-notre-pratique/03-chapitre-14-et-demain-l-apres-wsus.md)
- [Annexes](06-annexes.md)
