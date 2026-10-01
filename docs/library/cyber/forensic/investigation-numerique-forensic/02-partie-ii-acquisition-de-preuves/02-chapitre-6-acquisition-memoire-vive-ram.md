---
title: Chapitre 6 — Acquisition mémoire vive (RAM)
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie II — Acquisition de preuves
  - index.md
---

## 6.1 Pourquoi le dump RAM est non négociable

La mémoire vive contient des données qui n'existent nulle part ailleurs et qui disparaissent irrémédiablement à l'extinction de la machine. Les processus en cours d'exécution (y compris les malwares fileless qui ne sont jamais écrits sur le disque), les connexions réseau actives (vers le C2, vers les machines latéralisées), les credentials en clair (les hashes NTLM dans le processus LSASS, les clés de session Kerberos, les mots de passe en clair si l'attaquant a utilisé mimikatz), les clés de chiffrement en mémoire (BitLocker, FileVault, VeraCrypt — récupérables depuis le dump), et les commandes récemment exécutées (historique de la console, arguments des processus).

La règle est simple : si la machine est allumée, on dumpe la RAM en premier. Avant de l'isoler du réseau, avant de la saisir, avant de la déplacer, et surtout avant de l'éteindre. La perte de la RAM est irréversible — c'est l'erreur forensic la plus courante et la plus grave.

## 6.2 Outils d'acquisition mémoire

**DumpIt** (Comae/Magnet Forensics) : outil Windows le plus simple d'utilisation — un exécutable unique, double-clic, dump automatique de la RAM dans un fichier `.dmp` ou `.raw`. Rapide (environ 1-2 Go/minute selon le matériel), minimal en overhead. Recommandé pour les situations d'urgence où la simplicité prime.

**WinPmem** (Velocidex) : outil Windows open source plus flexible que DumpIt. Supporte les formats raw et AFF4. Permet l'acquisition de la mémoire physique ET du pagefile. Plus configurable mais légèrement plus complexe d'utilisation.

**Magnet RAM Capture** : outil gratuit de Magnet Forensics avec interface graphique. Simple, fiable, mais Windows uniquement.

**LiME** (Linux Memory Extractor) : module kernel Linux pour l'acquisition mémoire. Chargé dynamiquement (`insmod lime.ko "path=/path/dump.lime format=lime"`), il capture la mémoire physique avec un impact minimal. C'est la méthode standard pour les serveurs Linux.

**Acquisition mémoire de VM :** les snapshots VMware produisent un fichier `.vmem` qui est le dump mémoire de la VM. Les snapshots Hyper-V produisent un fichier `.bin`. Ces fichiers sont directement analysables avec Volatility sans avoir besoin d'exécuter un outil d'acquisition dans la VM — ce qui est un avantage considérable (pas de modification de la mémoire par l'outil d'acquisition).

**Acquisition à distance :** Velociraptor permet de déclencher un dump mémoire à distance sur n'importe quelle machine équipée de l'agent, sans intervention physique. F-Response offre une capacité similaire via un accès réseau au disque et à la mémoire de machines distantes.

## 6.3 Pagefile et hiberfil : mémoire persistante

Le **pagefile.sys** (Windows) est le fichier d'échange — quand la RAM est pleine, Windows y déplace des pages mémoire. Ces pages peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le pagefile persiste sur le disque même après un reboot — c'est une source de mémoire « fossile » quand le dump RAM n'a pas été fait à temps.

Le **hiberfil.sys** (Windows) est le fichier d'hibernation — quand la machine entre en hibernation, l'intégralité de la RAM est écrite dans ce fichier. Un hiberfil est littéralement un dump mémoire compressé, analysable avec Volatility (plugin `windows.hibernation`). Sur les laptops, l'hibernation est fréquente — c'est une source souvent négligée.

Sous Linux, le **swap** joue un rôle similaire au pagefile (fichier ou partition d'échange), et le suspend-to-disk écrit la RAM dans la partition swap.

## 6.4 Workflow d'arrivée sur une machine allumée

L'ordre des opérations quand l'analyste arrive sur une machine allumée et potentiellement compromise :

1. **Documenter l'état initial** : photographier l'écran (ce qui est affiché), noter l'heure système (pour calibrer les timestamps), identifier les processus visibles.
2. **Dump RAM** : exécuter DumpIt ou WinPmem depuis une clé USB. Ne pas installer d'outil sur le disque de la machine (on contaminerait la preuve). Durée : 10-20 minutes selon la quantité de RAM.
3. **Triage KAPE** (optionnel si le temps le permet) : collecte des artefacts système depuis la clé USB. Durée : 5-10 minutes.
4. **Capturer l'état réseau** : `netstat -ano` (Windows) ou `ss -tunap` (Linux) pour capturer les connexions réseau actives — elles disparaîtront à l'isolation.
5. **Isoler du réseau** : déconnecter le câble réseau ou désactiver le WiFi — l'attaquant ne peut plus communiquer avec la machine, mais la mémoire est préservée.
6. **Acquisition disque** : si nécessaire, avec write blocker.

> **Alerte :** L'exécution de DumpIt ou de KAPE modifie la mémoire de la machine (l'outil lui-même charge du code en mémoire, crée des processus, alloue des pages). C'est inévitable et documenté — l'analyste note dans le journal que le dump a modifié l'état mémoire et que les artefacts de l'outil de collecte seront visibles dans l'analyse. Ce compromis est accepté car l'alternative (ne pas dumper la RAM) est pire.

## 6.5 Fil rouge — MUSIC BOX : le dump RAM critique

> **🔬 MUSIC BOX — Épisode 6**
>
> Vendredi soir, 19h15. Claire arrive devant WKS-RD-047. L'écran affiche le bureau Windows avec plusieurs fenêtres ouvertes. Elle photographie l'écran (capture de l'état visuel), note l'heure système (19h15:23, UTC+1), et insère sa clé USB contenant DumpIt.
>
> Le dump prend 14 minutes (32 Go de RAM). Le hash SHA-256 est calculé immédiatement : `a7f3e2d8...`. Claire note dans le journal : « 19h15 — début dump RAM WKS-RD-047 avec DumpIt v2.1 depuis USB. 19h29 — fin du dump. SHA-256 : a7f3e2d8... Taille : 34 359 738 368 octets. La machine n'a pas été éteinte ni isolée du réseau avant le dump pour préserver les connexions actives. L'outil DumpIt a modifié l'état mémoire (attendu). »
>
> Ce dump sera la pièce maîtresse de l'investigation : c'est grâce à lui que l'équipe identifiera le processus svchost injecté, les connexions vers le C2 en Asie du Sud-Est, et les credentials en clair de 8 comptes dans la mémoire de LSASS.

---
