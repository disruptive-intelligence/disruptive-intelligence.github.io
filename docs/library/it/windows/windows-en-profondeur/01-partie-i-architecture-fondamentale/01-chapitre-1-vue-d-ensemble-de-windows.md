---
title: Chapitre 1 — Vue d'ensemble de Windows
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie I — Architecture fondamentale
  - index.md
---

## 1.1 Pourquoi comprendre Windows en profondeur

Windows équipe l'immense majorité des postes d'entreprise, porte Active Directory et reste la cible principale des logiciels malveillants. On ne peut ni analyser un incident, ni durcir un poste, ni comprendre une alerte EDR sans savoir comment le système fonctionne « sous le capot ». Ce cours n'est pas un cours d'administration : chaque mécanisme y est relié à son usage en défense et en investigation. Le principe directeur : **connaître le normal pour reconnaître l'anormal**.

## 1.2 Historique, versions et éditions

Windows repose sur le noyau **NT** (1993). Client et serveur d'une même génération partagent le même noyau.

| Système | Version NT |
|---|---|
| Windows 2000 | 5.0 |
| Windows XP | 5.1 |
| Windows Server 2003 | 5.2 |
| Windows Vista / Server 2008 | 6.0 |
| Windows 7 / Server 2008 R2 | 6.1 |
| Windows 8 / Server 2012 | 6.2 |
| Windows 8.1 / Server 2012 R2 | 6.3 |
| Windows 10, 11 / Server 2016 à 2025 | 10.0 (distingués par le numéro de build) |

Les versions anciennes encore en production concentrent protocoles obsolètes et vulnérabilités connues : leur inventaire est un enjeu de sécurité à part entière.

| Édition | Fonctions de sécurité notables |
|---|---|
| **Home** | Pas de BitLocker complet, pas de GPO, pas de jonction au domaine |
| **Pro** | BitLocker, GPO locales, jonction au domaine, Hyper-V |
| **Enterprise / Education** | Credential Guard, WDAC et AppLocker complets, Defender for Endpoint |
| **Server** | Rôles AD DS, AD CS, DNS, DHCP, IIS… |

Identifier le système : `systeminfo`, `winver`, ou `Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber`.

## 1.3 Mode utilisateur et mode noyau

Le processeur impose deux niveaux d'exécution :

| | **Mode utilisateur** (ring 3) | **Mode noyau** (ring 0) |
|---|---|---|
| Qui | Applications, services, Explorer | Noyau (`ntoskrnl.exe`), pilotes, HAL |
| Accès | Mémoire propre au processus, pas d'accès direct au matériel | Toute la mémoire, tout le matériel |
| En cas de plantage | Seul le processus s'arrête | Écran bleu (BSOD) |

Un programme qui veut lire un fichier ou ouvrir une connexion doit passer par un **appel système** contrôlé par le noyau. Cette séparation est la base de la sécurité de Windows : c'est aussi pourquoi un pilote malveillant, qui tourne en mode noyau, est si dangereux.

## 1.4 Les composants majeurs

| Composant | Mode | Rôle |
|---|---|---|
| `ntoskrnl.exe` | Noyau | Ordonnanceur, mémoire, entrées/sorties, Object Manager, Security Reference Monitor |
| `hal.dll` | Noyau | Couche d'abstraction matérielle |
| `win32k.sys` | Noyau | Sous-système graphique |
| `smss.exe` | Utilisateur | Gestionnaire de sessions, premier processus en mode utilisateur |
| `csrss.exe` | Utilisateur | Sous-système Windows (consoles, sessions) |
| `wininit.exe` | Utilisateur | Lance les services critiques de la session 0 |
| `services.exe` | Utilisateur | Service Control Manager (SCM) |
| `lsass.exe` | Utilisateur | Authentification, jetons, secrets (voir Partie III) |
| `svchost.exe` | Utilisateur | Hôte des services fournis sous forme de DLL |
| `winlogon.exe` | Utilisateur | Ouverture de session, verrouillage |
| `explorer.exe` | Utilisateur | Bureau, barre des tâches, explorateur |

Un processus qui n'a pas sa place dans ce paysage, ou qui s'y comporte autrement que prévu, mérite qu'on s'y arrête (Ch.6 et Ch.31).

## 1.5 Object Manager et Security Reference Monitor

Windows gère ses ressources comme des **objets** : processus, threads, fichiers, clés de registre, mutex, sections de mémoire. Chaque objet a un type, éventuellement un nom, et un **security descriptor**. Un processus qui veut utiliser un objet obtient un **handle** (une référence). À chaque ouverture de handle, le **Security Reference Monitor** compare le **jeton** du processus à la **DACL** de l'objet (Ch.17) : tout accès passe par ce contrôle.

## 1.6 Arborescence du système

| Dossier | Rôle | Intérêt sécurité |
|---|---|---|
| `C:\Windows\System32` | Binaires et DLL système **64 bits** | Emplacement attendu des processus système |
| `C:\Windows\SysWOW64` | Binaires **32 bits** sur un système 64 bits (nom trompeur) | Idem |
| `C:\Windows\System32\config` | Ruches du registre (SAM, SYSTEM, SECURITY, SOFTWARE) | Fichiers les plus sensibles du poste |
| `C:\Windows\WinSxS` | Magasin des composants et mises à jour | — |
| `C:\Program Files` / `(x86)` | Applications 64 / 32 bits | Normalement non modifiables par un utilisateur |
| `C:\ProgramData` (caché) | Données partagées des applications | Configurations, journaux, parfois secrets mal protégés |
| `C:\Users\<user>\AppData` (caché) | Données par utilisateur : `Roaming` (suit le profil), `Local` (machine), `LocalLow` (intégrité faible) | Traces d'exécution, données de navigateurs, persistance utilisateur |
| `C:\Users\Public` | Partagé entre utilisateurs locaux | Peu surveillé |
| `C:\Windows\Temp`, `%TEMP%` | Fichiers temporaires | Inscriptibles : lieux de dépôt fréquents |
| `pagefile.sys`, `hiberfil.sys` | Pagination, hibernation | Fragments de mémoire, artefacts forensic |

> **À retenir.** Un exécutable système lancé depuis un dossier inscriptible par l'utilisateur (`Temp`, `AppData`, `Public`) est un signal fort, quel que soit son nom.

## 1.7 Outils Sysinternals

| Outil | Usage |
|---|---|
| **Process Explorer** | Processus en détail : DLL, handles, jeton, signature, VirusTotal |
| **Process Monitor** | Activité fichiers, registre, réseau, processus en temps réel |
| **Autoruns** | Tous les points de démarrage automatique (services, tâches, clés Run, pilotes…) |
| **TCPView** | Connexions réseau par processus |
| **Sigcheck** | Signatures numériques |
| **Strings** | Chaînes contenues dans un binaire |
| **Sysmon** | Télémétrie détaillée dans les journaux (Ch.22) |

## 1.8 Fil rouge — SHADOW : l'alerte

> **🔍 SHADOW — Épisode 1**
>
> Léa reçoit l'alerte CrowdStrike. Premier réflexe : l'arbre de processus. `winword.exe` (PID 4528) → `rundll32.exe` (PID 6712) — anormal : un document Office n'a aucune raison de lancer rundll32. Le processus contacte une IP externe sur le port 443, toutes les 60 secondes. Léa sait qu'elle regarde un accès initial par document piégé, avec un canal de commande actif.

---
