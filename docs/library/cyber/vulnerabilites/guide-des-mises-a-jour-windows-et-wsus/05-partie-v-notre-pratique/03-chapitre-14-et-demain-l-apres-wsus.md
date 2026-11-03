---
title: 'Chapitre 14 — Et demain : l''après-WSUS'
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie V — Notre pratique
  - index.md
---

> 🧱 **Les bases**
>
> - **Intune** est le service cloud de Microsoft pour gérer les appareils (configuration, applications, mises à jour).
> - La **co-gestion** (*co-management*) permet de gérer un même parc à la fois par Configuration Manager (local) et par Intune (cloud), en répartissant les tâches.

WSUS est déprécié mais pas retiré (Ch.9). Ce chapitre ne décrit pas une migration : il donne au nouvel arrivant **les repères** pour comprendre les discussions en cours.

## 14.1 Les options

| Option | Principe | Ce qu'elle apporte par rapport à WSUS | Contraintes |
|---|---|---|---|
| **Stratégies client Windows Update** (ex-*Windows Update for Business*), via GPO ou Intune | la machine télécharge chez Microsoft ; l'administrateur fixe des **reports** (qualité : jusqu'à 30 jours ; fonctionnalités : jusqu'à 365 jours), des anneaux, des échéances | pas de serveur ; **blocages de protection** sur les mises à niveau ; déploiement accéléré (*expedite*) | accès Internet des postes ; contrôle par délais plutôt que par approbation |
| **Windows Autopatch** (Intune) | Microsoft orchestre les anneaux et les déploiements (Windows, Microsoft 365 Apps, Edge, Teams) | **hotpatch** (activé par défaut depuis mai 2026), rapports, pilotes/firmware | licences (Entreprise E3/E5 ou équivalent), Intune, confiance dans l'automatisation |
| **Configuration Manager** + WSUS (point de mise à jour logicielle) | WSUS reste en dessous, ConfigMgr ajoute déploiements, fenêtres, rapports, applications tierces | contrôle fin, publication tierce | infrastructure lourde ; dépend de WSUS |
| **Azure Update Manager** + Azure Arc | évaluation et déploiement des mises à jour des serveurs, y compris locaux (via Arc) | hotpatch pour Server 2025 (payant), fenêtres de maintenance | facturation Arc, connexion à Azure |
| **Microsoft Connected Cache** | cache local du contenu Microsoft pour les sources cloud | réduit la bande passante sans WSUS | à déployer et dimensionner |

## 14.2 Ce que WSUS ne fera jamais

- le **hotpatch** (Windows 11 Entreprise et Server 2025) ;
- les **blocages de protection** automatiques sur les mises à niveau ;
- les **rapports cloud** et les nouvelles fonctions de déploiement ;
- la gestion de **Microsoft 365 Apps** (Click-to-Run) seul.

## 14.3 Ce que WSUS reste seul à bien faire

- les **réseaux sans Internet** ou qui ne doivent pas dépendre du cloud (environnements sensibles, industriels, classifiés) : WSUS déconnecté, avec import par support contrôlé ;
- un **contrôle par approbation explicite**, gratuit, sans licence supplémentaire.

## 14.4 Les questions à poser avant de choisir

1. Les postes ont-ils un accès Internet direct et fiable (y compris nomades) ?
2. Quelles licences avons-nous (Entreprise E3/E5, Microsoft 365) ?
3. Quelles contraintes réglementaires ou contractuelles pèsent sur la dépendance au cloud ?
4. Quels serveurs doivent rester totalement isolés ?
5. Qui fera le travail, et avec quelles compétences ?

La réponse est souvent **hybride** : postes vers Intune/Autopatch, serveurs sensibles et réseaux isolés sur WSUS.

Approfondissement : version complète, Ch.26 et 27.

> 🧵 **Fil rouge — Novembre 2026**
>
> Le comité de direction d'ORIAN valide une trajectoire sur 18 mois : postes nomades en co-gestion vers Intune et Autopatch (avec hotpatch), postes fixes ensuite, serveurs du datacenter maintenus sur WSUS (HTTPS) et étudiés pour Azure Update Manager, réseau de l'imprimerie isolé sur un WSUS déconnecté. Karim et Inès gardent le cycle mensuel en J+n : seule la mécanique change, pas la méthode.

> 📌 **À retenir**
>
> - Après WSUS : stratégies client Windows Update, Autopatch (hotpatch), ConfigMgr, Azure Update Manager.
> - WSUS reste pertinent pour les réseaux isolés et le contrôle par approbation.
> - La méthode (veille, qualification, anneaux, preuve) ne change pas avec l'outil.

---
