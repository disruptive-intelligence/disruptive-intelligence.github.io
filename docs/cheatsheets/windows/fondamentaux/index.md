---
title: "Fondamentaux"
---
# Fondamentaux

Comprendre et observer un système Windows : identité de la machine, processus, connexions, journaux, droits et registre.

## Carte mentale

<div class="kw-mindmap" markdown>

- **Observer un système Windows**
    - [Système et arborescence](systeme.md)
        - Identifier la machine
            - [Version, build](systeme.md#voir-la-version-et-le-build-de-windows) : `Get-CimInstance Win32_OperatingSystem`
            - [Tout d'un coup](systeme.md#avoir-la-vue-densemble-de-la-machine) : `systeminfo`
            - [Domaine ?](systeme.md#savoir-si-la-machine-est-dans-un-domaine) : `Win32_ComputerSystem`
            - [Correctifs](systeme.md#voir-les-correctifs-installes) : `Get-HotFix`
            - [Allumée depuis](systeme.md#savoir-depuis-quand-la-machine-tourne) : `LastBootUpTime`
        - [Dossiers clés](systeme.md#retrouver-les-dossiers-cles)
            - `System32` : binaires système
            - `System32\config` : ruches du registre
            - `ProgramData` : données partagées (caché)
            - `%APPDATA%`, `%LOCALAPPDATA%` : données de l'utilisateur
            - `%TEMP%`, `C:\Windows\Temp` : temporaires
            - `C:\Users\Public` : partagé
        - Qui est là
            - [Connectés](systeme.md#voir-qui-est-connecte-a-la-machine) : `query user`
            - [Qui je suis](systeme.md#savoir-qui-je-suis) : `whoami /all`
    - [Fichiers et recherche](fichiers-recherche.md)
        - Lire
            - [Contenu](fichiers-recherche.md#afficher-le-contenu-dun-fichier) : `Get-Content`
            - [Suivre en direct](fichiers-recherche.md#lire-la-fin-dun-fichier-ou-la-suivre-en-direct) : `-Tail 20 -Wait`
        - Trouver
            - [Par nom](fichiers-recherche.md#trouver-un-fichier-par-son-nom) : `Get-ChildItem -Recurse -Filter`
            - [Modifiés récemment](fichiers-recherche.md#trouver-les-fichiers-modifies-recemment) : `LastWriteTime -gt`
            - [Plus gros](fichiers-recherche.md#trouver-les-plus-gros-fichiers) : `Sort-Object Length -Descending`
            - [Un mot](fichiers-recherche.md#chercher-un-mot-dans-un-fichier-ou-un-dossier) : `Select-String`
        - Vérifier
            - [Empreinte](fichiers-recherche.md#calculer-lempreinte-dun-fichier) : `Get-FileHash`
            - [Signature](fichiers-recherche.md#verifier-la-signature-dun-executable) : `Get-AuthenticodeSignature`
            - [Flux cachés (ADS)](fichiers-recherche.md#voir-les-flux-de-donnees-alternatifs-ads-dun-fichier) : `Get-Item -Stream *`
    - [Processus et services](processus.md)
        - Processus
            - [Lister](processus.md#lister-les-processus) : `Get-Process`
            - [Ligne de commande, parent](processus.md#voir-la-ligne-de-commande-et-le-parent-de-chaque-processus) : `Win32_Process`
            - [Arbre](processus.md#voir-larbre-des-processus) : Process Explorer
            - [Légitime ?](processus.md#verifier-quun-processus-systeme-est-legitime)
                - `lsass.exe` : 1 seul, parent `wininit.exe`
                - `svchost.exe` : parent `services.exe`, avec `-k`
                - Chemin hors `System32` : suspect
            - [Arrêter](processus.md#arreter-un-processus) : `Stop-Process -Id`
        - Services
            - [Lister](processus.md#lister-les-services-et-leur-etat) : `Get-Service`
            - [Binaire, compte, démarrage](processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service) : `Win32_Service`
            - [Contenu des svchost](processus.md#savoir-ce-quheberge-chaque-svchostexe) : `tasklist /svc`
            - [Mal configuré](processus.md#reperer-un-service-mal-configure) : chemin sans guillemets, dossier modifiable
    - [Réseau](reseau.md)
        - Configuration
            - [IP, passerelle, DNS](reseau.md#voir-ses-adresses-ip-passerelle-et-dns) : `Get-NetIPConfiguration`
            - [Routes](reseau.md#voir-la-table-de-routage) : `Get-NetRoute`
            - [ARP](reseau.md#voir-la-table-arp) : `arp -a`
        - Connexions
            - [Par processus](reseau.md#voir-quel-processus-ecoute-ou-communique) : `Get-NetTCPConnection` → `OwningProcess`
            - [En écoute](reseau.md#voir-les-ports-en-ecoute) : `-State Listen`
        - Tester
            - [Port](reseau.md#tester-quun-port-est-ouvert) : `Test-NetConnection -Port`
            - [Nom](reseau.md#resoudre-un-nom) : `Resolve-DnsName`
            - [Cache DNS](reseau.md#voir-et-vider-le-cache-dns) : `ipconfig /displaydns`
        - Partages et pare-feu
            - [Partages](reseau.md#voir-les-partages-de-la-machine-et-ceux-montes) : `Get-SmbShare` · `Get-SmbMapping`
            - [Pare-feu](reseau.md#voir-le-profil-et-letat-du-pare-feu) : `Get-NetFirewallProfile`
    - [Journaux et événements](logs/index.md)
        - [Lire et filtrer](logs/lire.md)
            - [Par ID et période](logs/lire.md#filtrer-par-identifiant-et-par-periode) : `Get-WinEvent -FilterHashtable`
            - [Exporter](logs/lire.md#exporter-un-journal-pour-lanalyser-ailleurs) : `wevtutil epl`
            - [Politique d'audit](logs/lire.md#voir-la-politique-daudit-active) : `auditpol /get /category:*`
        - [Sessions et RDP](logs/sessions-rdp.md)
            - 4624 / 4625 : session ouverte / échouée
            - 4672 : session admin
            - RDP reçu : 1149, 21, 24, 25
            - RDP émis : 1102 (RDPClient)
        - [Processus et PowerShell](logs/processus-powershell.md)
            - 4688 : processus créé
            - 4104 : bloc de script PowerShell
        - [Persistance](logs/persistance.md)
            - 7045 / 4697 : service installé
            - 4698 : tâche planifiée créée
            - 4720 / 4732 : compte créé / ajouté à un groupe
        - [Pare-feu et Defender](logs/pare-feu-defender.md)
            - 2004 / 2005 : règle de pare-feu
            - 1116 : menace détectée · 5001 : protection coupée
        - [Effacement](logs/effacement.md) : 1102 (Security) · 104 (System)
    - [Droits et identités](droits.md)
        - Identité
            - [SID, groupes, privilèges](droits.md#voir-mon-sid-mes-groupes-et-mes-privileges) : `whoami /user /groups /priv`
            - [Session élevée ?](droits.md#savoir-si-la-session-est-elevee-uac) : intégrité Medium / High
            - [Administrateurs](droits.md#savoir-qui-est-administrateur-de-la-machine) : `Get-LocalGroupMember`
        - Permissions NTFS
            - [Lire](droits.md#lire-les-permissions-dun-fichier-ou-dun-dossier) : `icacls` — `F` · `M` · `RX`
            - [Trop larges](droits.md#reperer-les-permissions-trop-larges) : Everyone, Users en écriture
            - [Accorder, retirer](droits.md#accorder-ou-retirer-un-droit) : `icacls /grant` · `/remove`
            - [Prendre possession](droits.md#prendre-possession-dun-fichier) : `takeown /f`
    - [Registre](registre.md)
        - Lire
            - [Valeurs d'une clé](registre.md#lire-les-valeurs-dune-cle) : `Get-ItemProperty`
            - [Chercher](registre.md#chercher-une-valeur-dans-le-registre) : `reg query /f /s`
        - Ruches
            - `HKLM\SYSTEM` : services, USB, ShimCache, BAM
            - `HKLM\SOFTWARE` : logiciels, `Run` machine
            - `HKLM\SAM` · `SECURITY` : comptes, secrets
            - `HKCU` (`NTUSER.DAT`) : `Run`, `RecentDocs`, `RunMRU`
        - [Ce qui démarre](registre.md#voir-ce-qui-se-lance-a-louverture-de-session) : clés `Run` / `RunOnce`
        - [Modifier](registre.md#exporter-une-cle-avant-de-la-modifier) : `reg export` d'abord

</div>

## Les fiches


- [Système et arborescence](systeme.md) — Identifier la machine, se repérer dans l'arborescence, savoir qui est connecté.
- [Fichiers et recherche](fichiers-recherche.md) — Lire, trouver et comparer des fichiers ; empreintes, signatures et flux alternatifs.
- [Processus et services](processus.md) — Ligne de commande, parent, arbre et DLL d'un processus ; services et svchost.
- [Réseau](reseau.md) — Adresses, connexions par processus, test de port, DNS, partages, pare-feu.
- [Journaux et événements](logs/index.md) — Filtrer les journaux, retrouver une activité, exporter.
- [Droits et identités](droits.md) — SID, groupes, privilèges ; permissions NTFS.
- [Registre](registre.md) — Lire, chercher, voir ce qui démarre, exporter.
