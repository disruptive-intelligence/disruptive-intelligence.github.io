---
title: PARTIE II — ACQUISITION DE PREUVES
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 3
chapters: 9
---

*L'acquisition est l'étape la plus critique de toute investigation. Une analyse brillante ne compense jamais une acquisition bâclée : si l'image disque est incomplète, si le dump mémoire est corrompu, si les logs n'ont pas été préservés, les conclusions seront fragiles et potentiellement contestables.*

---

### Chapitre 5 — Acquisition disque et supports de stockage

#### 5.1 Principes fondamentaux

L'acquisition disque produit une copie bit-à-bit du support de stockage : chaque secteur est copié, y compris les espaces non alloués (où se trouvent les fichiers supprimés), le slack space (espace résiduel en fin de cluster), et les zones cachées (HPA, DCO). Ce n'est pas une simple copie de fichiers — c'est un clone exact du support au niveau des secteurs.

Le **write blocker** est le garant de l'intégrité. Un write blocker matériel (Tableau T35es, CRU WiebeTech) est un dispositif physique interposé entre le support source et la station d'acquisition qui empêche électriquement toute écriture sur le support. Un write blocker logiciel (sous Linux : montage avec `mount -o ro`, ou utilisation de udev rules) empêche les écritures au niveau du système d'exploitation. Le write blocker matériel est préféré en contexte judiciaire car il est physiquement vérifiable et indépendant du logiciel. Sans write blocker, le simple fait de connecter un disque à Windows modifie des métadonnées (timestamps d'accès, journaux du système de fichiers) — ce qui peut compromettre l'intégrité de la preuve.

La **vérification d'intégrité par double hash** (MD5 + SHA-256) est obligatoire. Le hash est calculé sur le support source avant l'acquisition, sur l'image produite immédiatement après l'acquisition, et éventuellement sur le support source après l'acquisition (pour vérifier que l'acquisition n'a rien modifié — ce qui serait le cas si le write blocker avait défailli). Si les hash correspondent, l'intégrité est prouvée mathématiquement.

#### 5.2 Acquisition physique vs logique

L'**acquisition physique** copie l'intégralité du support au niveau des secteurs — c'est la méthode privilégiée car elle capture tout, y compris les données supprimées et les zones cachées. Commande type sous Linux avec dc3dd :

```
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/acquisition.log
```

L'**acquisition logique** copie uniquement les fichiers visibles par le système de fichiers. Plus rapide et moins volumineuse, mais elle ne capture ni les fichiers supprimés, ni le slack space, ni les zones non allouées. L'acquisition logique est utilisée quand l'acquisition physique est impossible (VM en production accessible uniquement par réseau, volume chiffré qu'on ne peut pas déchiffrer hors ligne) ou quand le triage rapide suffit (combinée avec KAPE pour une collecte ciblée des artefacts).

#### 5.3 HDD : le support le plus favorable

Les disques durs magnétiques (HDD) sont les plus favorables au forensic. Les données supprimées restent physiquement présentes sur le plateau magnétique tant que les secteurs n'ont pas été réécrits par de nouvelles données — ce qui peut prendre des mois ou des années dans les zones peu utilisées du disque. La récupération de fichiers supprimés sur HDD est souvent possible et productive.

Les zones cachées du disque — **HPA** (Host Protected Area) et **DCO** (Device Configuration Overlay) — sont des zones que le BIOS et le système d'exploitation ne voient pas normalement, mais qui peuvent contenir des données dissimulées. L'outil `hdparm` (Linux) détecte leur présence (`hdparm -N /dev/sdX` affiche la taille réelle vs la taille visible) et permet de les rendre accessibles pour l'acquisition. Les outils forensic commerciaux (EnCase, X-Ways) gèrent cette détection automatiquement.

#### 5.4 SSD : les défis du forensic moderne

Les SSD ont fondamentalement changé le forensic. Trois mécanismes posent problème.

Le **TRIM** est une commande que le système d'exploitation envoie au SSD pour indiquer que des secteurs ne sont plus utilisés — le contrôleur du SSD peut alors effacer physiquement ces secteurs pour optimiser les performances d'écriture futures. Conséquence : les fichiers supprimés sur un SSD avec TRIM actif (c'est le cas par défaut sur tous les OS modernes depuis Windows 7, macOS 10.6, et Linux avec les filesystems récents) sont souvent irrécupérables, contrairement aux HDD. Le TRIM peut s'exécuter en quelques secondes après la suppression d'un fichier.

Le **garbage collection** est un processus interne au contrôleur SSD qui réorganise et nettoie les blocs de données de manière autonome — même sans commande du système d'exploitation. Le SSD peut effacer des données « supprimées » de sa propre initiative, à n'importe quel moment, y compris quand le disque est connecté via un write blocker (le write blocker empêche les écritures venant du système, mais pas les opérations internes du contrôleur).

Le **wear leveling** distribue les écritures sur toutes les cellules NAND pour équilibrer l'usure, ce qui signifie que les données ne sont pas nécessairement stockées à l'emplacement attendu au niveau des secteurs logiques.

Implication pratique : sur un SSD, l'acquisition doit être faite le plus rapidement possible après la détection de l'incident. Chaque minute qui passe est une minute pendant laquelle le garbage collection peut effacer des preuves. Et il ne faut jamais promettre de récupérer des fichiers supprimés sur un SSD — c'est souvent impossible.

#### 5.5 Stockage chiffré

Le chiffrement est un défi majeur. BitLocker (Windows), FileVault (macOS), LUKS (Linux) et VeraCrypt chiffrent le contenu du disque — sans la clé, l'image acquise est un bloc de données inexploitable. Stratégies de récupération :

Si la machine est **allumée et le volume déverrouillé**, la clé de chiffrement est en mémoire — d'où l'importance absolue du dump RAM avant toute extinction (Ch.6). Le dump mémoire, analysé avec Volatility, peut révéler la clé BitLocker, la passphrase FileVault, ou les clés LUKS.

La **recovery key** BitLocker est souvent stockée dans Active Directory (vérifiable par les administrateurs), dans le compte Microsoft de l'utilisateur, ou sur un support physique (papier, clé USB). La recovery key FileVault est stockable dans le compte Apple (iCloud) ou par un administrateur MDM. Les clés LUKS n'ont pas de recovery centralisé — si la passphrase est perdue et que la RAM n'a pas été dumpée, les données sont inaccessibles.

Le **TPM** (Trusted Platform Module) protège la clé BitLocker sur les machines modernes, mais il la libère automatiquement au boot normal — une acquisition à chaud (machine allumée avec le volume déverrouillé) contourne cette protection.

#### 5.6 RAID, NAS et serveurs virtualisés

Les serveurs utilisent généralement des configurations RAID. Deux approches : acquisition disque par disque (acquérir individuellement chaque disque du RAID, puis reconstruire le volume logique avec X-Ways, Autopsy, ou `mdadm` — méthode la plus sûre car elle préserve les données brutes de chaque disque) ou acquisition du volume logique via le contrôleur (capture directe du volume RAID reconstruit — plus rapide, mais perte des données résiduelles au niveau physique).

Les **NAS** et serveurs de fichiers en production posent la question de l'acquisition à chaud. Un NAS ne peut pas toujours être éteint et retiré du rack (impact sur la production). L'acquisition à chaud — via le réseau (FTK Imager en mode réseau, ou `dd` via SSH) ou via un snapshot — est souvent le seul choix, mais elle est moins « propre » qu'une acquisition physique avec write blocker car le système de fichiers peut évoluer pendant la copie.

Les **machines virtuelles** sont un cas favorable : l'image VMDK (VMware), VHDX (Hyper-V), ou QCOW2 (KVM/QEMU) EST le disque. Il suffit de copier le fichier d'image de la VM ou de prendre un snapshot (qui gèle l'état du disque à un instant T). Le snapshot de VM est l'équivalent fonctionnel d'une acquisition à chaud avec write blocker — et il capture simultanément la mémoire si la VM est en cours d'exécution.

#### 5.7 Fil rouge — MUSIC BOX : l'acquisition disque

> **🔬 MUSIC BOX — Épisode 5**
>
> Samedi 9h00. Maître Fournier (experte judiciaire) est sur site. L'acquisition formelle commence.
>
> **WKS-RD-047** (SSD NVMe 512 Go, Windows 11, BitLocker activé) : la machine est encore allumée (le dump RAM a été fait la veille — la clé BitLocker est en mémoire). Acquisition physique via FTK Imager avec write blocker Tableau T35es. Format E01, segmenté en fichiers de 4 Go. Durée : 45 minutes. Hash MD5 + SHA-256 calculés automatiquement : correspondance vérifiée. Documenté dans le formulaire de chaîne de custody, signé par Maître Fournier.
>
> **SRV-RD-01** (serveur Linux Ubuntu 22.04, RAID 5 × 4 disques de 2 To) : le serveur est en production, les expériences en cours ne peuvent pas être interrompues. Décision : acquisition logique via `dc3dd` sur le réseau (accès SSH), ciblée sur les répertoires `/home/`, `/var/log/`, `/tmp/`, et `/opt/research/`. Image physique reportée à l'arrêt de maintenance (J+5). Hash calculé sur chaque acquisition partielle.

---

### Chapitre 6 — Acquisition mémoire vive (RAM)

#### 6.1 Pourquoi le dump RAM est non négociable

La mémoire vive contient des données qui n'existent nulle part ailleurs et qui disparaissent irrémédiablement à l'extinction de la machine. Les processus en cours d'exécution (y compris les malwares fileless qui ne sont jamais écrits sur le disque), les connexions réseau actives (vers le C2, vers les machines latéralisées), les credentials en clair (les hashes NTLM dans le processus LSASS, les clés de session Kerberos, les mots de passe en clair si l'attaquant a utilisé mimikatz), les clés de chiffrement en mémoire (BitLocker, FileVault, VeraCrypt — récupérables depuis le dump), et les commandes récemment exécutées (historique de la console, arguments des processus).

La règle est simple : si la machine est allumée, on dumpe la RAM en premier. Avant de l'isoler du réseau, avant de la saisir, avant de la déplacer, et surtout avant de l'éteindre. La perte de la RAM est irréversible — c'est l'erreur forensic la plus courante et la plus grave.

#### 6.2 Outils d'acquisition mémoire

**DumpIt** (Comae/Magnet Forensics) : outil Windows le plus simple d'utilisation — un exécutable unique, double-clic, dump automatique de la RAM dans un fichier `.dmp` ou `.raw`. Rapide (environ 1-2 Go/minute selon le matériel), minimal en overhead. Recommandé pour les situations d'urgence où la simplicité prime.

**WinPmem** (Velocidex) : outil Windows open source plus flexible que DumpIt. Supporte les formats raw et AFF4. Permet l'acquisition de la mémoire physique ET du pagefile. Plus configurable mais légèrement plus complexe d'utilisation.

**Magnet RAM Capture** : outil gratuit de Magnet Forensics avec interface graphique. Simple, fiable, mais Windows uniquement.

**LiME** (Linux Memory Extractor) : module kernel Linux pour l'acquisition mémoire. Chargé dynamiquement (`insmod lime.ko "path=/path/dump.lime format=lime"`), il capture la mémoire physique avec un impact minimal. C'est la méthode standard pour les serveurs Linux.

**Acquisition mémoire de VM :** les snapshots VMware produisent un fichier `.vmem` qui est le dump mémoire de la VM. Les snapshots Hyper-V produisent un fichier `.bin`. Ces fichiers sont directement analysables avec Volatility sans avoir besoin d'exécuter un outil d'acquisition dans la VM — ce qui est un avantage considérable (pas de modification de la mémoire par l'outil d'acquisition).

**Acquisition à distance :** Velociraptor permet de déclencher un dump mémoire à distance sur n'importe quelle machine équipée de l'agent, sans intervention physique. F-Response offre une capacité similaire via un accès réseau au disque et à la mémoire de machines distantes.

#### 6.3 Pagefile et hiberfil : mémoire persistante

Le **pagefile.sys** (Windows) est le fichier d'échange — quand la RAM est pleine, Windows y déplace des pages mémoire. Ces pages peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le pagefile persiste sur le disque même après un reboot — c'est une source de mémoire « fossile » quand le dump RAM n'a pas été fait à temps.

Le **hiberfil.sys** (Windows) est le fichier d'hibernation — quand la machine entre en hibernation, l'intégralité de la RAM est écrite dans ce fichier. Un hiberfil est littéralement un dump mémoire compressé, analysable avec Volatility (plugin `windows.hibernation`). Sur les laptops, l'hibernation est fréquente — c'est une source souvent négligée.

Sous Linux, le **swap** joue un rôle similaire au pagefile (fichier ou partition d'échange), et le suspend-to-disk écrit la RAM dans la partition swap.

#### 6.4 Workflow d'arrivée sur une machine allumée

L'ordre des opérations quand l'analyste arrive sur une machine allumée et potentiellement compromise :

1. **Documenter l'état initial** : photographier l'écran (ce qui est affiché), noter l'heure système (pour calibrer les timestamps), identifier les processus visibles.
2. **Dump RAM** : exécuter DumpIt ou WinPmem depuis une clé USB. Ne pas installer d'outil sur le disque de la machine (on contaminerait la preuve). Durée : 10-20 minutes selon la quantité de RAM.
3. **Triage KAPE** (optionnel si le temps le permet) : collecte des artefacts système depuis la clé USB. Durée : 5-10 minutes.
4. **Capturer l'état réseau** : `netstat -ano` (Windows) ou `ss -tunap` (Linux) pour capturer les connexions réseau actives — elles disparaîtront à l'isolation.
5. **Isoler du réseau** : déconnecter le câble réseau ou désactiver le WiFi — l'attaquant ne peut plus communiquer avec la machine, mais la mémoire est préservée.
6. **Acquisition disque** : si nécessaire, avec write blocker.

> **Alerte :** L'exécution de DumpIt ou de KAPE modifie la mémoire de la machine (l'outil lui-même charge du code en mémoire, crée des processus, alloue des pages). C'est inévitable et documenté — l'analyste note dans le journal que le dump a modifié l'état mémoire et que les artefacts de l'outil de collecte seront visibles dans l'analyse. Ce compromis est accepté car l'alternative (ne pas dumper la RAM) est pire.

#### 6.5 Fil rouge — MUSIC BOX : le dump RAM critique

> **🔬 MUSIC BOX — Épisode 6**
>
> Vendredi soir, 19h15. Claire arrive devant WKS-RD-047. L'écran affiche le bureau Windows avec plusieurs fenêtres ouvertes. Elle photographie l'écran (capture de l'état visuel), note l'heure système (19h15:23, UTC+1), et insère sa clé USB contenant DumpIt.
>
> Le dump prend 14 minutes (32 Go de RAM). Le hash SHA-256 est calculé immédiatement : `a7f3e2d8...`. Claire note dans le journal : « 19h15 — début dump RAM WKS-RD-047 avec DumpIt v2.1 depuis USB. 19h29 — fin du dump. SHA-256 : a7f3e2d8... Taille : 34 359 738 368 octets. La machine n'a pas été éteinte ni isolée du réseau avant le dump pour préserver les connexions actives. L'outil DumpIt a modifié l'état mémoire (attendu). »
>
> Ce dump sera la pièce maîtresse de l'investigation : c'est grâce à lui que l'équipe identifiera le processus svchost injecté, les connexions vers le C2 en Asie du Sud-Est, et les credentials en clair de 8 comptes dans la mémoire de LSASS.

---

### Chapitre 7 — Acquisition réseau et captures de trafic

#### 7.1 Quand et comment capturer du trafic

La capture de trafic réseau en temps réel n'est possible que si l'infrastructure le permet (port mirroring sur le switch, TAP réseau, ou NDR déployé). En forensic, la capture se fait rarement au moment de l'incident initial (on n'avait pas prévu de capturer) — on travaille plus souvent avec les logs réseau existants (proxy, pare-feu, DNS, VPN) et les captures historiques du NDR si disponible.

Si une capture live est possible, **tcpdump** est l'outil en ligne de commande de référence : `tcpdump -i eth0 -w capture.pcap -c 1000000` capture un million de paquets sur l'interface eth0. **Wireshark** offre une interface graphique pour la capture et l'analyse. **Zeek** (ex-Bro) ne capture pas les paquets bruts mais produit des logs structurés (connexions, requêtes DNS, requêtes HTTP, certificats TLS) beaucoup plus faciles à analyser à grande échelle.

Les captures doivent être filtrées par pertinence : capturer tout le trafic d'un réseau de 10 Gbit/s produit des téraoctets de données en quelques heures — inutilisable. Les filtres utiles : par IP suspecte (connue C2), par port (443 sortant vers des destinations inhabituelles), par machine source (la machine compromise), ou par protocole (DNS pour le tunneling, HTTP/HTTPS pour le C2).

#### 7.2 Logs réseau existants

En pratique, les logs existants sont la source réseau principale. Les **logs proxy** (Squid, Zscaler, Blue Coat) contiennent les URLs visitées, les user-agents, les volumes de données, et les codes de retour HTTP — essentiels pour identifier l'exfiltration et le C2 web. Les **logs pare-feu** (Palo Alto, Fortinet, Check Point) contiennent les flux autorisés et refusés avec IP source, IP destination, port, protocole, et volume — essentiels pour identifier les communications inhabituelles. Les **logs DNS** (Infoblox, BIND, Windows DNS) contiennent les résolutions de domaine — essentiels pour identifier les domaines DGA, le DNS tunneling, et les résolutions vers des C2. Les **logs VPN** contiennent les connexions avec géolocalisation, horodatage, et durée — essentiels pour identifier les accès compromis.

Les **NetFlow** (métadonnées de flux réseau sans le contenu des paquets : source, destination, port, volume, durée) sont une source intermédiaire entre les logs et le PCAP — moins détaillée que le PCAP mais disponible en rétention longue et à grande échelle.

#### 7.3 Fil rouge — MUSIC BOX : les logs réseau

> **🔬 MUSIC BOX — Épisode 7**
>
> NovaPharma n'a pas de NDR ni de capture PCAP historique. Les sources réseau disponibles sont le proxy Squid (6 mois de rétention), le pare-feu Palo Alto (12 mois), le DNS Infoblox (3 mois), et le VPN Fortinet (12 mois). Claire demande à l'IT d'exporter immédiatement ces logs vers le stockage forensic — avant que la rotation ne les efface.
>
> Premier résultat du proxy : le poste WKS-RD-047 a des connexions HTTPS régulières vers `103.xx.xx.xx:443` toutes les 30 minutes (pattern de beaconing) depuis 60 jours. Le user-agent est `Mozilla/5.0 NovaPharma` — l'attaquant a personnalisé le user-agent de son RAT.

---

### Chapitre 8 — Acquisition des logs, des données d'identité et du cloud

#### 8.1 Acquisition des Event Logs Windows

Les Event Logs Windows (format `.evtx`) sont stockés dans `C:\Windows\System32\winevt\Logs\`. Méthodes d'acquisition : copie directe des fichiers `.evtx` (possible sur une machine éteinte ou via un partage réseau), export via PowerShell (`wevtutil epl Security C:\export\Security.evtx`), collecte via KAPE (target `EventLogs` — collecte automatiquement tous les fichiers evtx), ou collecte centralisée depuis le SIEM (si les logs ont été envoyés à un SIEM, ils y sont préservés même si l'attaquant efface les logs locaux — c'est l'une des défenses les plus efficaces contre l'anti-forensics).

Les canaux critiques à collecter : Security (authentification, audit), System (services, pilotes), Application, PowerShell/Operational (script block logging — Event ID 4104), Microsoft-Windows-Sysmon/Operational (si Sysmon est déployé), Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational (RDP), et Microsoft-Windows-TaskScheduler/Operational (tâches planifiées).

#### 8.2 Acquisition des logs Linux

Les logs Linux sont stockés dans `/var/log/` et via systemd-journald. Les fichiers clés : `auth.log` ou `secure` (authentifications, sudo, SSH), `syslog` (événements système), `kern.log` (événements noyau), les logs applicatifs (`/var/log/apache2/`, `/var/log/nginx/`, `/var/log/mysql/`), et les fichiers de session (`wtmp`, `btmp`, `lastlog`).

Pour le journald : `journalctl --since "2026-01-01" --until "2026-03-08" -o json > journal_export.json` exporte les logs systemd au format JSON, exploitable par les outils de timeline.

La collecte des historiques de commandes (`.bash_history`, `.zsh_history`) doit inclure non seulement les fichiers dans les home directories mais aussi la recherche dans la mémoire et les fichiers supprimés — l'attaquant supprime souvent son historique, mais des traces peuvent persister en mémoire, dans le swap, ou dans les secteurs non alloués du disque.

#### 8.3 Acquisition des données Active Directory

L'AD est une source critique souvent sous-exploitée en forensic. Le fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) contient tous les objets AD (utilisateurs, groupes, GPO, ACL) et les hashes NTLM de tous les comptes. Son acquisition se fait via volume shadow copy (`vssadmin create shadow /for=C:`) puis copie du ntds.dit depuis le shadow, ou via `ntdsutil` en mode snapshot. L'analyse avec `secretsdump.py` (Impacket) ou DSInternals (PowerShell) permet d'extraire les hashes et de comprendre la compromission AD (Ch.20).

Les **logs de réplication AD** sont essentiels pour détecter le DCSync (Event ID 4662 avec les GUID de réplication). Les **métadonnées AD** (date de création et de modification des objets, via `repadmin /showmeta` ou ADRecon) révèlent les modifications récentes — comptes créés, groupes modifiés, GPO ajoutées.

**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD.

#### 8.4 Acquisition des données cloud

**Microsoft 365 :** l'Unified Audit Log (UAL) est exportable via PowerShell (`Search-UnifiedAuditLog`) ou via le portail Purview Compliance. La rétention dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5). Le Sign-in Log est exportable via le portail Entra ID ou via l'API Microsoft Graph. L'eDiscovery permet de placer un **legal hold** sur des boîtes mail (préservation contre suppression) et d'exporter des données ciblées.

**AWS :** CloudTrail enregistre chaque appel API (exportable en JSON — `aws cloudtrail lookup-events`). Les VPC Flow Logs capturent les métadonnées réseau. Les S3 Access Logs tracent les accès aux buckets. Les EBS Snapshots permettent de capturer l'état d'un volume sans arrêter l'instance.

Les **limitations de rétention** sont un piège fréquent : si le dwell time dépasse la rétention des logs cloud, les premières actions de l'attaquant sont perdues. La vérification de la rétention effective (pas théorique) doit être faite dès le début de l'investigation.

#### 8.5 Fil rouge — MUSIC BOX : les logs AD et cloud

> **🔬 MUSIC BOX — Épisode 8**
>
> Samedi 10h00. Claire lance la collecte des données d'identité et cloud.
>
> **AD :** Export des Event Logs Security et System de DC01 via PowerShell (wevtutil). Snapshot volume shadow copy de DC01 pour acquisition du ntds.dit. Exécution d'ADTimeline pour reconstituer la chronologie des modifications AD.
>
> **Cloud :** NovaPharma utilise AWS pour le stockage des données R&D (S3) et Microsoft 365 (E3) pour la messagerie. Export du UAL M365 via PowerShell (180 jours disponibles — suffisant pour couvrir la fenêtre J-60 à J). Export de CloudTrail AWS (90 jours par défaut, mais NovaPharma avait configuré un trail vers S3 avec rétention longue — les 12 derniers mois sont disponibles).
>
> Premier résultat CloudTrail : 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours (J-5 à J-1), depuis un rôle IAM légitime (`svc-backup-role`) mais utilisé depuis l'IP externe `103.xx.xx.xx` — le C2. Les access keys ont été exfiltrées du serveur R&D Linux par l'attaquant.

---
