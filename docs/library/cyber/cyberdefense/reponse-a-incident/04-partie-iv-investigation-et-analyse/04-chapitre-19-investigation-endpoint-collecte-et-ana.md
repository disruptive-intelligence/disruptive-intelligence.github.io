---
title: 'Chapitre 19 — Investigation endpoint : collecte et analyse concrète'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation ET analyse
  - index.md
---

*Ce chapitre est le volet pratique de l'investigation sur les machines. Là où le Ch.18 cartographie les sources, ce chapitre montre concrètement comment collecter et interpréter les artefacts pour répondre aux questions de l'investigation.*

## 19.1 Acquisition de preuves : triage vs image complète

Le **triage live** collecte les artefacts les plus informatifs d'une machine en 20 à 30 minutes, sans éteindre la machine. L'outil de référence est KAPE (Kroll Artifact Parser and Extractor) qui collecte automatiquement les Event Logs, le Prefetch, l'Amcache, le ShimCache, le registre, le SRUM, les Scheduled Tasks, les services, les fichiers récents, et d'autres artefacts configurables. Velociraptor offre une capacité similaire mais avec la possibilité de déployer la collecte à distance sur des centaines de machines simultanément — essentiel quand le périmètre de compromission est large. Le triage est la méthode par défaut en IR : il donne 80 % de l'information en 20 % du temps.

L'**image complète** (bit-à-bit) capture l'intégralité du disque. Outils : FTK Imager (interface graphique, Windows), dd/dcfldd (ligne de commande, Linux), ou acquisition via EDR pour les environnements cloud. L'image est nécessaire quand la chaîne de custody doit être préservée pour une procédure judiciaire, quand une analyse approfondie est requise (analyse de la MFT complète, carving de fichiers supprimés, analyse du slack space), ou quand le triage n'a pas donné de résultats concluants.

L'**acquisition mémoire** capture la RAM de la machine en cours d'exécution. Outils : DumpIt (Windows, simple et rapide), WinPmem (Windows, plus flexible), ou LiME (Linux). L'acquisition mémoire doit être faite AVANT tout redémarrage — la mémoire est la source la plus volatile. Elle est indispensable pour les malwares fileless (qui n'écrivent rien sur le disque), pour l'extraction de credentials en mémoire (hashes NTLM dans le processus lsass), et pour l'analyse des connexions réseau actives.

**Chaîne de custody :** chaque acquisition est documentée : qui (nom de l'analyste), quoi (machine, artefact), quand (horodatage précis), avec quel outil (nom, version), et hash de vérification (SHA256 calculé immédiatement). Le formulaire de chaîne de custody est en Annexe C.

## 19.2 Analyse mémoire

L'analyse de la mémoire vive avec **Volatility 3** (l'outil de référence open source) permet d'extraire les processus en cours d'exécution (`windows.pslist`, `windows.pstree` — identifier les processus suspects par leur arbre de parenté, leur chemin d'exécution, ou leur nom), les DLL chargées (`windows.dlllist` — identifier les DLL injectées ou suspectes), les connexions réseau actives (`windows.netscan` — les connexions vers le C2 sont directement visibles), les credentials en mémoire (hashes NTLM extraits du processus lsass — si mimikatz ou un outil similaire a été exécuté, les credentials déchiffrées peuvent encore être en mémoire), les commandes exécutées (`windows.cmdline` — les arguments passés aux processus), et le code injecté (`windows.malfind` — détection de zones mémoire suspectes dans les processus, indicatrices d'injection de code).

L'analyse mémoire est indispensable quand le malware est fileless (il s'exécute uniquement en mémoire, sans écrire de fichier sur le disque), quand l'attaquant utilise le process hollowing ou le reflective DLL loading (techniques d'évasion qui injectent du code dans des processus légitimes), et pour capturer les credentials actives (les hashes NTLM dans lsass permettent de comprendre quels comptes l'attaquant a compromis).

## 19.3 Artefacts système Windows — interprétation pour l'IR

Le **Prefetch** (situé dans `C:\Windows\Prefetch\`) enregistre les programmes exécutés, avec le nom du fichier, les 8 dernières dates/heures d'exécution, et le nombre total d'exécutions. En IR, le Prefetch révèle l'exécution d'outils de l'attaquant (PsExec, mimikatz, rclone, ransomware builder) même si les fichiers ont été supprimés depuis.

L'**Amcache** (`C:\Windows\AppCompat\Programs\Amcache.hve`) et le **ShimCache** enregistrent les programmes exécutés avec leur hash SHA1 et leur chemin — permettant de confirmer que le binaire malveillant a bien été exécuté et d'en identifier le hash pour enrichissement CTI.

La **MFT** (Master File Table) et le **USN Journal** sont le journal du système de fichiers NTFS. Ils enregistrent la création, la modification, le renommage, et la suppression de fichiers avec horodatage. En IR, ils révèlent les fichiers créés par l'attaquant (scripts, binaires, fichiers de staging), les fichiers supprimés (l'attaquant nettoie souvent ses traces), et les mouvements de données (fichiers copiés vers un répertoire de staging avant exfiltration).

Le **registre Windows** contient des informations critiques pour l'IR : les clés `Run`/`RunOnce` (persistence via exécution automatique au démarrage), les services (persistence via création de service), les clés `UserAssist` (historique des programmes exécutés via l'interface graphique), les clés `BAM`/`DAM` (programmes exécutés avec horodatage, disponibles sur Windows 10/11 et Server 2016+), et les informations réseau (profils WiFi, historique des connexions).

Le **SRUM** (System Resource Usage Monitor, `C:\Windows\System32\SRU\SRUDB.dat`) enregistre la consommation réseau par processus sur 30 à 60 jours. En IR, il révèle les processus ayant généré du trafic réseau significatif — excellent pour détecter l'exfiltration (un processus rclone ayant transféré 380 Go sera visible dans le SRUM même si le processus n'est plus en cours d'exécution).

## 19.4 Analyse malware first-pass

L'IR n'est pas du reverse engineering approfondi, mais un first-pass rapide sur le malware est essentiel pour extraire les IoC et comprendre le comportement. L'analyse statique rapide (strings — extraire les chaînes de caractères pour identifier les URLs, les IP, les clés de registre, les noms de fichiers ; imports — identifier les API Windows utilisées ; sections PE — identifier les sections suspectes ou packé) et la soumission en sandbox (ANY.RUN, Joe Sandbox, CAPE — exécution contrôlée avec observation du comportement réseau, des modifications système, et des artefacts créés) suffisent généralement pour l'IR. Le reverse engineering approfondi (décompilation, analyse du code assembleur) est délégué aux analystes malware spécialisés ou au prestataire PRIS.

## 19.5 Fil rouge — BLACKTIDE : le forensic sur le DC

> **🔍 BLACKTIDE — Épisode 19**
>
> Samedi 09h00-14h00. Thomas (PRIS) priorise DC01 — le contrôleur de domaine principal, le plus compromis.
>
> **Acquisition mémoire (DumpIt) :** 32 Go, 12 minutes. L'analyse Volatility révèle un processus `lsass.exe` avec des zones mémoire modifiées (malfind positif — injection de code), des credentials en clair de 12 comptes admin dans la mémoire de lsass, et un processus `svchost.exe` suspect avec une connexion active vers le C2 `update-srv-infra[.]xyz` sur le port 443.
>
> **Triage KAPE (DC01, DC02, DC03) :** 20 minutes par machine. Le Prefetch confirme l'exécution de `psexec.exe`, `rclone.exe`, `bc.exe` (le builder PhantomCrypt), et `mimikatz.exe`. L'Amcache fournit les hashes SHA1 de tous ces binaires. Le SRUM de DC01 montre que `rclone.exe` a transféré 147 Go de données réseau sur les 7 derniers jours (une partie des 380 Go totaux). Les Scheduled Tasks révèlent une tâche `WindowsUpdateCheck` créée à J-12, exécutant un script PowerShell obfusqué toutes les 4 heures — mécanisme de persistence.
>
> **Constat :** David, l'admin d'astreinte, a redémarré les serveurs de fichiers FS01-Lyon et FS01-Fos à 23h30 la veille (« pour stopper le chiffrement »). La mémoire de ces serveurs est perdue. Les artefacts Prefetch et Amcache sont préservés (ils sont sur disque), mais les connexions réseau actives et les credentials en mémoire sont irrémédiablement perdus. Nadia documente : « Perte de preuve — RAM de FS01-Lyon et FS01-Fos — cause : redémarrage sans collecte préalable. »

---
