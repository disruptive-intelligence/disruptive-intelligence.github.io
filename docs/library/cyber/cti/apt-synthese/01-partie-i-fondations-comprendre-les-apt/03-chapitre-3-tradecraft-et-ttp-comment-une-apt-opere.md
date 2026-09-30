---
title: 'Chapitre 3 — Tradecraft et TTP : comment une APT opère'
source: Cyber/01_CTI/APT_Synthese.md
note: APT — synthèse
up:
- - APT — synthèse
  - ../index.md
- - 'Partie I — Fondations : comprendre les APT'
  - index.md
---

## 3.1 Vecteurs d'accès initial

Le **spear-phishing** reste le vecteur le plus courant en volume (APT28 — macros Word, APT35 — fausses pages de login). L'**exploitation de vulnérabilités sur les services exposés** est le vecteur n°1 en impact pour les acteurs sophistiqués : les appliances réseau edge (VPN Ivanti/Pulse Secure, firewalls Fortinet, passerelles Citrix, appliances Barracuda) sont des cibles systématiques car elles sont exposées sur Internet, rarement patchées rapidement, et donnent un accès direct au réseau interne. La **supply chain** (SolarWinds par APT29, 3CX par Lazarus, CCleaner par APT41) exploite la confiance dans un fournisseur. Les **credentials volés** (password spraying, infostealers, achat sur les marchés dark web) permettent l'accès avec des identifiants légitimes. Le **social engineering** avancé (Lazarus — faux recruteurs LinkedIn, APT35 — faux profils académiques, Kimsuky — impersonation) cible le facteur humain. Le **watering hole** (APT32 — sites d'actualité régionaux) compromet un site fréquenté par la cible. Et les **trusted relationships** (APT10 — Cloud Hopper via MSP) abusent de la confiance dans un partenaire.

## 3.2 Persistence

Les APT installent des mécanismes de persistence pour survivre au reboot, au patch, et à la réinitialisation de mot de passe. Les techniques principales : tâches planifiées/cron (exécution régulière), services/démons malveillants, DLL sideloading (placer une DLL malveillante dans le répertoire d'un exécutable légitime), web shells (backdoor sur un serveur web), modification du registre (clés Run/RunOnce, IFEO), bootkits/firmware (persistence en dessous de l'OS — rare mais existant), comptes backdoor (comptes admin cachés), et tokens/certificats (vol ou création de tokens OAuth, certificats SAML — GoldenSAML par APT29).

Le concept clé est l'**accès redondant** : une APT mature ne dépend jamais d'un seul mécanisme. Si un web shell est détecté et supprimé, l'attaquant revient via une tâche planifiée ou un compte backdoor. C'est pourquoi le containment APT doit identifier TOUS les accès avant d'agir (Ch.27).

## 3.3 Living off the Land

Les APT modernes évitent de déposer des malwares détectables et utilisent les outils déjà présents sur le système. PowerShell (téléchargement, exécution en mémoire, C2), WMI (exécution distante, persistence, reconnaissance), certutil (téléchargement de fichiers), mshta/msiexec (exécution de scripts/packages), rundll32 (chargement de DLL), bitsadmin (téléchargement en arrière-plan), et net.exe/nltest (énumération AD). Volt Typhoon est l'exemple extrême : quasi aucun outil custom, uniquement des LOLBins — le tradecraft qui rend la détection la plus difficile.

La conséquence pour la défense : bloquer ces outils n'est souvent pas possible (ils sont nécessaires au fonctionnement du système). Il faut monitorer leur usage anormal — PowerShell avec -EncodedCommand, certutil qui télécharge un .exe, WMI depuis un poste utilisateur vers un serveur.

## 3.4 Command & Control et exfiltration

Les techniques C2 par difficulté de détection croissante : HTTPS beaconing (trafic chiffré, se fond dans le trafic légitime), DNS tunneling (données encodées dans les requêtes DNS), domain fronting (utilise un CDN légitime pour masquer le vrai C2), fast flux DNS (rotation rapide des IP), dead drops (messages sur des services légitimes — Pastebin, GitHub), et stéganographie (données cachées dans des images). L'exfiltration suit les mêmes canaux : HTTPS, DNS, email, ou services cloud (OneDrive, Google Drive, S3).

---
