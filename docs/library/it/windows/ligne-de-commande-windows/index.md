---
title: Ligne de commande Windows
source: IT/02 Windows/Ligne de commande Windows.md
format: cours
revue: '2026-05-10'
---

*CMD et PowerShell pour naviguer, diagnostiquer et administrer Windows*

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais ouvert un terminal de sa vie.
> Tout ce dont tu as besoin, c’est un ordinateur sous Windows 10 ou 11.

-----

### Ce que ce cours est — et ce qu’il n’est pas

Ce cours t’apprend à **utiliser** la ligne de commande Windows au quotidien :

- naviguer dans le système de fichiers
- manipuler des fichiers et dossiers
- récupérer des informations système
- diagnostiquer le réseau
- comprendre les processus, services, utilisateurs et groupes
- consulter les journaux Windows
- découvrir le registre et les tâches planifiées
- faire une première collecte d’informations utile en administration ou cybersécurité

Ce cours **n’est pas** un cours de programmation PowerShell. Les variables, boucles, fonctions, scripts avancés, `param()`, pipeline d’objets en profondeur — tout ça est couvert dans le **cours PowerShell** de la bibliothèque, qui prend le relais une fois que tu es à l’aise avec la ligne de commande.

**L’analogie :** c’est la différence entre “apprendre à utiliser le terminal Linux” et “apprendre à écrire des scripts Bash”. Les deux se complètent, mais l’angle n’est pas le même.

-----

### Guide de lecture

|Section                   |Niveau           |Objectif                                          |
|--------------------------|-----------------|--------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel      |Ce qu’il faut retenir pour ne pas être perdu      |
|**Très utile en pratique**|🟡 Bon à connaître|Ce qui te rend opérationnel au quotidien          |
|**Bonus**                 |🔴 Avancé         |Pour aller plus loin — tu peux y revenir plus tard|

#### Parcours recommandés

|Parcours                    |Chapitres                |Objectif                                                        |
|----------------------------|-------------------------|----------------------------------------------------------------|
|**🎯 Découverte / entretien**|Ch.1-8, 10-11, 17, 25    |Comprendre la CLI Windows, être crédible en entretien           |
|**🔧 Administration**        |Tous sauf Ch.23-24       |Être autonome pour diagnostiquer et administrer un poste Windows|
|**🛡️ Cyber / blue team**     |Tout, focus Ch.16, 21, 24|Triage, collecte d’informations, investigation de base          |

-----

### Glossaire — Les mots à connaître

| Terme                        | Définition simple                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| **Terminal**                 | La fenêtre où tu tapes des commandes texte                                               |
| **Shell**                    | Le programme qui lit et exécute tes commandes (CMD et PowerShell sont des shells)        |
| **Commande**                 | Une instruction que le shell sait exécuter (`dir`, `ping`, `Get-Process`…)               |
| **Argument**                 | Une info que tu donnes à une commande (`ping 8.8.8.8` — `8.8.8.8` est l’argument)        |
| **Option / Flag**            | Un modificateur qui change le comportement d’une commande (`dir /s` — `/s` est l’option) |
| **Prompt**                   | Le texte affiché par le terminal qui attend ta commande (`C:\Users\Lea>`)                |
| **Chemin (path)**            | L’adresse d’un fichier ou dossier dans le système (`C:\Users\Lea\Documents`)             |
| **Variable d’environnement** | Une information système stockée sous un nom (`%USERNAME%`, `$env:COMPUTERNAME`)          |
| **Processus**                | Un programme en cours d’exécution                                                        |
| **Service**                  | Un programme qui tourne en arrière-plan, souvent sans fenêtre visible                    |
| **Registre**                 | La base de données de configuration de Windows                                           |
| **Tâche planifiée**          | Une action programmée pour s’exécuter automatiquement (au démarrage, à une heure…)       |
| **Journal d’événements**     | Les logs de Windows — ce qui s’est passé sur la machine                                  |
| **Event ID**                 | Un numéro qui identifie un type d’événement dans les journaux Windows                    |
| **PID**                      | Process ID — le numéro unique d’un processus en cours d’exécution                        |
| **Port**                     | Un numéro qui identifie un service réseau sur une machine (80 = web, 443 = HTTPS…)       |
| **DNS**                      | Le système qui traduit les noms de domaine en adresses IP (`google.com` → `142.250.x.x`) |
| **Cmdlet**                   | Une commande PowerShell native, nommée `Verbe-Nom` (`Get-Process`, `Set-Location`)       |
| **Pipeline**                 | Le mécanisme qui envoie la sortie d’une commande vers une autre, avec le caractère `     |
| **Redirection**              | Envoyer la sortie d’une commande dans un fichier au lieu de l’écran (`>`, `>>`)          |
| **Batch (.bat)**             | Un fichier contenant des commandes CMD exécutées dans l’ordre                            |
| **Remoting**                 | La capacité d’exécuter des commandes sur une machine distante                            |

-----

### Fil rouge : Léa, technicienne support

> **Contexte narratif**
> 
> **Léa**, 26 ans, technicienne support niveau 2 dans une PME de 200 postes Windows. Un lundi matin, plusieurs problèmes remontent en même temps : un poste ne se connecte plus au réseau, un utilisateur ne retrouve plus certains fichiers, un processus consomme trop de ressources, un service semble arrêté, le responsable demande des informations système, et un comportement suspect doit être vérifié rapidement.
> 
> Léa va utiliser CMD et PowerShell pour diagnostiquer et résoudre chaque problème, chapitre après chapitre.

-----

### Table des matières

**PARTIE I — FONDATIONS (Ch.1-3)**

1. [Comprendre la ligne de commande Windows](01-partie-i-fondations/01-chapitre-1-comprendre-la-ligne-de-commande-windows.md)
1. [Naviguer dans le système de fichiers](01-partie-i-fondations/02-chapitre-2-naviguer-dans-le-systeme-de-fichiers.md)
1. [Obtenir de l’aide et devenir autonome](01-partie-i-fondations/03-chapitre-3-obtenir-de-laide-et-devenir-autonome.md)

**PARTIE II — MANIPULER FICHIERS, TEXTE ET VARIABLES (Ch.4-8)**

1. [Gérer les fichiers et dossiers avec CMD](02-partie-ii-manipuler-fichiers-texte-et-variables.md#chapitre-4-gerer-les-fichiers-et-dossiers-avec-cmd)
1. [Gérer les fichiers et dossiers avec PowerShell](02-partie-ii-manipuler-fichiers-texte-et-variables.md#chapitre-5-gerer-les-fichiers-et-dossiers-avec-powershell)
1. [Rechercher des fichiers et du contenu](02-partie-ii-manipuler-fichiers-texte-et-variables.md#chapitre-6-rechercher-des-fichiers-et-du-contenu)
1. [Variables d’environnement, PATH et repères système](02-partie-ii-manipuler-fichiers-texte-et-variables.md#chapitre-7-variables-denvironnement-path-et-reperes-systeme)
1. [Redirections, pipes et sorties de commandes](02-partie-ii-manipuler-fichiers-texte-et-variables.md#chapitre-8-redirections-pipes-et-sorties-de-commandes)

**PARTIE III — ADMINISTRER ET DIAGNOSTIQUER (Ch.9-18)**

1. [CMD vs PowerShell : comprendre la différence](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-9-cmd-vs-powershell-comprendre-la-difference)
1. [Informations système et diagnostic de base](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-10-informations-systeme-et-diagnostic-de-base)
1. [Processus](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-11-processus)
1. [Services Windows](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-12-services-windows)
1. [Utilisateurs et groupes locaux](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-13-utilisateurs-et-groupes-locaux)
1. [Tâches planifiées](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-14-taches-planifiees)
1. [Le registre Windows](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-15-le-registre-windows)
1. [Journaux Windows (Event Logs)](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-16-journaux-windows-event-logs)
1. [Réseau avec CMD et PowerShell](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-17-reseau-avec-cmd-et-powershell)
1. [Interagir avec le Web depuis la CLI](03-partie-iii-administrer-et-diagnostiquer.md#chapitre-18-interagir-avec-le-web-depuis-la-cli)

**PARTIE IV — AUTOMATISATION ET TRIAGE (Ch.19-22)**

1. [Introduction aux scripts batch (.bat)](04-partie-iv-automatisation-et-triage.md#chapitre-19-introduction-aux-scripts-batch-bat)
1. [Introduction à l’automatisation PowerShell](04-partie-iv-automatisation-et-triage.md#chapitre-20-introduction-a-lautomatisation-powershell)
1. [Sécurité et triage depuis la ligne de commande](04-partie-iv-automatisation-et-triage.md#chapitre-21-securite-et-triage-depuis-la-ligne-de-commande)
1. [PowerShell Remoting : aperçu](04-partie-iv-automatisation-et-triage.md#chapitre-22-powershell-remoting-apercu)

**PARTIE V — LABS, ÉVALUATION ET SYNTHÈSE (Ch.23-25)**

1. [Labs progressifs](05-partie-v-labs-evaluation-et-synthese.md#chapitre-23-labs-progressifs)
1. [Skills Assessment — Évaluation finale](05-partie-v-labs-evaluation-et-synthese.md#chapitre-24-skills-assessment-evaluation-finale)
1. [Synthèse et boîte à outils du praticien](05-partie-v-labs-evaluation-et-synthese.md#chapitre-25-synthese-et-boite-a-outils-du-praticien)

**ANNEXES**

-----

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Comprendre la ligne de commande Windows](01-partie-i-fondations/01-chapitre-1-comprendre-la-ligne-de-commande-windows.md)
    - [Chapitre 2 — Naviguer dans le système de fichiers](01-partie-i-fondations/02-chapitre-2-naviguer-dans-le-systeme-de-fichiers.md)
    - [Chapitre 3 — Obtenir de l’aide et devenir autonome](01-partie-i-fondations/03-chapitre-3-obtenir-de-laide-et-devenir-autonome.md)
- [Partie II — Manipuler fichiers, texte et variables](02-partie-ii-manipuler-fichiers-texte-et-variables.md)
- [Partie III — Administrer et diagnostiquer](03-partie-iii-administrer-et-diagnostiquer.md)
- [Partie IV — Automatisation et triage](04-partie-iv-automatisation-et-triage.md)
- [Partie V — Labs, évaluation et synthèse](05-partie-v-labs-evaluation-et-synthese.md)
- [Annexes](06-annexes.md)
