---
title: Annexes
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - index.md
---

## Annexe M — Registre de sources

> ⏱ **Annexe versionnée — dernière vérification : 1er août 2026.**
> Chaque fait périssable du cours renvoie à une entrée de ce registre. Le **niveau de source** indique la force de la référence : `T` texte juridique · `D` documentation officielle de l'éditeur ou de l'organisme · `N` norme ou standard · `S` source secondaire (presse spécialisée, cabinet, analyse tierce).


### M.1 Comment lire une entrée

```
[S-nn]  Organisme — Titre exact du document ou de la page
        Version ou date de publication · Article, section ou contrôle précis
        Niveau : T / D / N / S · Vérifié le : jj/mm/aaaa
        Utilisé au : §x.y, annexe Z
```



### M.2 Réglementation européenne et française

**[S-01]** — Union européenne — *Directive (UE) 2022/2555 (NIS2)*
Niveau `T` · Vérifié le 30/07/2026 · Utilisé au §8.1, annexe F.
*Point de vigilance* : pour une entreprise privée, les obligations opérationnelles résultent principalement du droit national de transposition. Le statut exact doit être vérifié dans chaque juridiction.

**[S-02]** — République française — *Projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité* — dossier législatif public
Niveau `T` · Vérifié le 30/07/2026 · **Non promulgué à cette date** · Utilisé au §8.1, §8.10, annexe F.
*À revérifier en priorité* : c'est le déclencheur de revue anticipée n° 1 du document.

**[S-03]** — ANSSI — *Référentiel d'exigences de cybersécurité (ReCyF)*
Version de travail du **17/03/2026** · Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §8.2, §8.10, annexe F.
*Point de vigilance* : le document porte explicitement la mention « version de travail ». Il n'est pas opposable en l'état. Les numéros d'objectifs cités dans le cours doivent être revérifiés contre la version définitive.

**[S-04]** — Union européenne — *Règlement (UE) 2024/2847 relatif à des exigences horizontales de cybersécurité pour les produits comportant des éléments numériques (Cyber Resilience Act)*
Niveau `T` · Vérifié le 01/08/2026 · Articles utilisés :

- **art. 13** — exigences de gestion des vulnérabilités, applicable au 11/12/2027 → §33.7
- **art. 14** — obligations de signalement, applicable au 11/09/2026 → §33.5, §8.3
- **art. 16** — plateforme unique de signalement → §33.5
- **art. 69 §2 et §3** — régime transitoire des produits déjà mis sur le marché → §33.9
- annexes relatives à la documentation technique → §33.7

**[S-05]** — Commission européenne — *Cyber Resilience Act — Reporting obligations*, page officielle « Shaping Europe's digital future »
Niveau `D` · Vérifié le 01/08/2026 · Utilisé au §33.5, §33.9, annexe F.
*Contenu retenu* : applicabilité au 11/09/2026 · alerte précoce sous 24 h · notification sous 72 h · rapport final sous 14 jours après disponibilité d'une mesure corrective pour une vulnérabilité activement exploitée, sous un mois pour un incident grave.

**[S-06]** — Analyses juridiques concordantes sur la portée de l'article 14 et du régime transitoire de l'article 69
Niveau `S` · Vérifié le 01/08/2026 · Utilisé au §33.5, §33.6, §33.9.
*Usage* : ces sources secondaires confirment la lecture des articles et précisent que l'article 14 **n'impose pas** en lui-même la publication d'une politique de divulgation coordonnée, ni la tenue d'un inventaire de composants — obligations relevant de l'article 13. **Toute décision engageante doit être prise sur le texte [S-04], pas sur ces analyses.**

**[S-07]** — Union européenne — *Règlement (UE) 2016/679 (RGPD)*, article 32
Niveau `T` · Vérifié le 30/07/2026 · Utilisé au §8.6, annexe F.
*Point de vigilance* : les affirmations du cours sur la pratique des autorités de contrôle doivent être rattachées, dans votre contexte, aux **délibérations publiées** de l'autorité compétente. Le cours ne cite aucune décision particulière et présente une tendance, pas une règle.

**[S-08]** — Union européenne — *Règlement (UE) 2022/2554 (DORA)* · **[S-09]** — *Règlement (UE) 2017/745 (MDR)* et *2017/746 (IVDR)*
Niveau `T` · Vérifiés le 30/07/2026 · Utilisés au §8.5, §33.8, annexe F.


### M.3 Normes et référentiels

**[S-10]** — ISO/IEC 27001:2022 et ISO/IEC 27002:2022
Niveau `N` · Vérifié le 30/07/2026 · Contrôles utilisés au §8.4 :

- **8.8** — gestion des vulnérabilités techniques
- **8.9** — gestion des configurations
- **8.19** — installation de logiciels sur les systèmes en exploitation
- **8.32** — gestion des changements

**[S-11]** — Série IEC 62443 — sécurité des systèmes d'automatisation et de contrôle industriels
Niveau `N` · Vérifié le 30/07/2026 · Utilisé au §29.2, annexe F.
*Point de vigilance* : la série comporte plusieurs parties aux publics différents (exploitant, intégrateur, fabricant). Le cours en retient la logique de zones, conduits et répartition des rôles, sans citer de partie particulière.

**[S-12]** — PCI DSS, version 4.x · **[S-13]** — Référentiel HDS · **[S-14]** — Référentiel SecNumCloud
Niveau `N` · Vérifiés le 30/07/2026 · Utilisés au §8.5, annexe F.
*Point de vigilance* : pour chacun, la **version applicable** et les exigences précises doivent être identifiées selon votre périmètre. Le cours ne cite aucun numéro d'exigence.

**[S-15]** — ANSSI — référentiel relatif aux **prestataires d'administration et de maintenance sécurisées (PAMS)**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §13.4.
*Point de vigilance* : **le statut du schéma de qualification et la liste des prestataires éventuellement qualifiés doivent être vérifiés directement sur le site de l'agence.** Une information périmée sur ce point peut orienter à tort un choix de prestataire.


### M.4 Écosystème des vulnérabilités

**[S-16]** — NIST — annonce relative à la **priorisation de l'enrichissement du NVD** à compter du **15/04/2026**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §1.8, §4.9, §16.8.
*Formulation exacte à conserver* : toutes les vulnérabilités continuent d'être enregistrées ; c'est l'**enrichissement** — scores, correspondances produit, classification — qui devient sélectif, priorisé sur les vulnérabilités connues comme exploitées, les logiciels utilisés par l'administration fédérale américaine et les logiciels critiques. Les autres fiches peuvent porter la mention *Not Scheduled*.

**[S-17]** — FIRST — **EPSS**, documentation du modèle et calendrier de versions
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §4.5, §38.4, annexe H.
*Fait retenu* : la version 5 du modèle a commencé à publier ses scores le **15/06/2026** — date de **rupture de série** pour tout indicateur fondé sur un seuil de score.

**[S-18]** — FIRST — **CVSS v4.0**, spécification et guide d'utilisation
Niveau `N` · Vérifié le 30/07/2026 · Utilisé au §4.4, annexe C.
*Fait retenu* : la documentation du standard indique explicitement que CVSS mesure une **sévérité**, non un risque.

**[S-19]** — IETF — **RFC 9116**, *A File Format to Aid in Security Vulnerability Disclosure* (`security.txt`)
Niveau `N` · Vérifié le 01/08/2026 · Utilisé au §33.3.

**[S-20]** — CISA — **catalogue des vulnérabilités connues comme exploitées** · **[S-21]** — CISA — **BOD 26-04**, publiée le 10/06/2026
Niveau `D` · Vérifiés le 30/07/2026 · Utilisés au §4.6, §8.7.
*Point de vigilance majeur* : une directive opérationnelle contraignante de cette autorité s'impose **aux seules agences civiles fédérales américaines**. Elle constitue pour une organisation européenne un **modèle méthodologique**, jamais une obligation.

**[S-22]** — ENISA — **base européenne de vulnérabilités (EUVD)**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §4.9, §14.4.

**[S-23]** — Formats d'inventaire et d'exploitabilité : **CycloneDX**, **SPDX**, **CSAF**, **VEX**
Niveau `N` · Vérifiés le 30/07/2026 · Utilisés au §4.8, §25.11, §25.19.


### M.5 Cycles de vie produits

**[S-24]** — Microsoft — pages officielles de **cycle de vie** et de **support étendu Windows 10**
Niveau `D` · Vérifiées le 30/07/2026 · Utilisées au §2.4, §12.4, §12.5, cas B, annexe H.
*Faits retenus* : fin de support de Windows 10 le **14/10/2025** · programme de support étendu **grand public** prolongé jusqu'au **12/10/2027**, **excluant explicitement les appareils joints à un annuaire d'entreprise ou gérés par une solution de gestion de flotte** · programme **commercial** distinct, payant, à tarif croissant · Windows 10 Entreprise/IoT LTSB 2016 le **13/10/2026** · Windows Server 2016 le **12/01/2027**.

**[S-25]** — Microsoft — documentation relative à l'**expiration des certificats de démarrage sécurisé** émis en 2011
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §1.3, §3.8, annexe H.
*Faits retenus* : KEK CA 2011 le **24/06/2026** · UEFI CA 2011 le **27/06/2026** · Windows Production PCA 2011 le **19/10/2026** · remplacement par les certificats émis en 2023 · les machines non mises à jour continuent de démarrer mais perdent la capacité de recevoir de futures révocations.

**[S-26]** — Microsoft Learn — **correction à chaud (hotpatching) sur machines rattachées à Azure Arc**
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §2.5.
*Faits retenus* : disponible pour Windows Server 2025 éditions Standard et Datacenter · **sans coût additionnel depuis le 19/05/2026** (facturation par cœur supprimée) · cadence de mise à jour de référence trimestrielle avec redémarrage, suivie de deux mois de correctifs à chaud · prérequis dont la sécurité basée sur la virtualisation et le démarrage sécurisé · pilotes, micrologiciels et certains composants **hors périmètre**.

**[S-27]** — Projet Kubernetes — **politique de support des versions**
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §3.3, §30.4, annexe H.
*Faits retenus* : environ trois versions mineures par an · environ **douze mois de support standard** suivis d'environ **deux mois de maintenance limitée** · les offres managées appliquent leurs propres calendriers.


### M.6 Ce qui n'est pas sourcé, et l'est assumé

Les éléments suivants relèvent d'une **doctrine proposée par ce cours**, et non d'une exigence externe. Ils sont marqués comme tels dans le texte et doivent être adaptés puis approuvés par votre organisation :

| Élément | Où |
|---|---|
| Les sept attributs obligatoires d'une mesure compensatoire | §20.7 |
| La règle de signature au niveau supérieur à chaque renouvellement de dérogation | §7.4 |
| Les délais 72 h / 7 j / 30 j des classes de service | §7.2, annexe C |
| Le délai d'observation de 3 à 7 jours | §18.3 |
| Les alertes certificat à 60/30/7 jours | §24.6 |
| Le délai d'observation de 90 jours après décommissionnement | §35.11 |
| La capacité de sécurité de 10 à 20 % réservée en développement | §25.3 |
| Le délai de 90 jours de divulgation coordonnée | §33.3 — **pratique courante**, non règle |
| Les seuils d'escalade et les tailles d'échantillon d'audit | annexe J, §39.4 |
| Les cycles de support par famille de produits (5-10 ans, 2-4 ans…) | annexe H — **ordres de grandeur indicatifs**, non sourcés |

⚠️ **Le principe** : mieux vaut une doctrine interne explicitement assumée et approuvée qu'une valeur présentée comme une norme externe qu'elle n'est pas. Un auditeur accepte parfaitement une règle interne motivée ; il n'accepte pas une exigence attribuée à tort à un référentiel.


### M.7 Sources à revérifier en priorité

| Priorité | Source | Motif |
|---|---|---|
| **1** | [S-02] | Promulgation attendue — change le statut de toute la Partie II |
| **1** | [S-03] | Version définitive attendue — les objectifs cités peuvent être renumérotés |
| **2** | [S-24] | Calendriers de support étendu susceptibles d'évoluer |
| **2** | [S-16], [S-17] | Évolutions de l'écosystème et des modèles de score |
| **3** | [S-15] | Statut du schéma de qualification |
| **3** | [S-26], [S-27] | Modèles économiques et calendriers de support |

---
