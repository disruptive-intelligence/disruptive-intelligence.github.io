---
title: PARTIE III — ANALYSE FONDAMENTALE ET RAISONNEMENT FORENSIC
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 4
chapters: 9
---

*Cette partie couvre les fondamentaux transversaux de l'analyse : la compréhension des systèmes de fichiers (le substrat de toute analyse disque), la construction de la timeline (le livrable central), et le raisonnement analytique (la compétence intellectuelle qui distingue l'analyste du simple opérateur d'outils).*

---

### Chapitre 9 — Systèmes de fichiers : comprendre ce qu'on analyse

#### 9.1 Pourquoi comprendre le système de fichiers

Le système de fichiers est la couche d'organisation entre le stockage brut (secteurs du disque) et les fichiers tels que l'utilisateur les voit. Sans comprendre cette couche, l'analyste ne peut pas interpréter les métadonnées, récupérer les fichiers supprimés, ni détecter les manipulations de timestamps. Chaque système de fichiers a sa propre logique de stockage, ses propres métadonnées, et ses propres artefacts forensic.

#### 9.2 NTFS — le système de fichiers le plus riche en artefacts

NTFS (New Technology File System) est le système de fichiers standard de Windows et le plus riche en artefacts forensic.

La **MFT** (Master File Table) est le cœur de NTFS : chaque fichier et dossier du volume possède une entrée dans la MFT (enregistrement de 1 024 octets) qui contient ses attributs. Les attributs clés pour le forensic :

**$STANDARD_INFORMATION ($SI)** contient les timestamps MACB (Modified, Accessed, Changed, Born/Created) du fichier. Ces timestamps sont modifiés par le système d'exploitation lors des opérations normales, mais AUSSI par les outils de timestomping (l'attaquant modifie délibérément les dates pour brouiller la timeline). C'est pourquoi $SI seul ne suffit pas pour dater fiablement un fichier.

**$FILE_NAME ($FN)** contient un second jeu de timestamps MACB, mis à jour uniquement lors du renommage ou du déplacement du fichier — ils sont beaucoup plus difficiles à falsifier (les outils de timestomping standard ne les modifient pas). La comparaison $SI vs $FN est l'outil fondamental de détection du timestomping : si $SI indique « créé en 2022 » mais $FN indique « créé le 3 mars 2026 », il y a eu manipulation.

**$DATA** contient le contenu du fichier lui-même. Pour les petits fichiers (< environ 700 octets), le contenu est stocké directement dans l'entrée MFT (resident data). Pour les fichiers plus grands, $DATA pointe vers les clusters du disque qui contiennent les données.

Les **ADS** (Alternate Data Streams) sont des flux de données secondaires attachés à un fichier, invisibles dans l'explorateur Windows et dans la plupart des commandes (`dir`). Un fichier `rapport.docx` peut avoir un ADS `rapport.docx:hidden_data` contenant des données cachées. Les ADS sont utilisés par Windows lui-même (le flux `Zone.Identifier` indique d'où un fichier a été téléchargé) et par les attaquants pour cacher des données ou du code.

Le journal **$UsnJrnl** (Update Sequence Number Journal) enregistre toutes les modifications de fichiers sur le volume : création, modification, suppression, renommage. Même si un fichier a été supprimé, le $UsnJrnl conserve la trace (avec le nom, la date, et l'opération). C'est une source forensic de première importance, parseable avec MFTECmd.

Le journal **$LogFile** enregistre les transactions NTFS pour la récupération après crash — il contient des informations sur les opérations récentes du système de fichiers.

#### 9.3 ext4, FAT32/exFAT et APFS

**ext4** (Linux) utilise des inodes au lieu de la MFT. Les timestamps incluent crtime (creation time, introduit en ext4), mtime, atime, ctime. Le journal ext4 enregistre les transactions pour la cohérence. La récupération de fichiers supprimés est possible (extundelete, ext4magic) mais moins fiable qu'avec NTFS car ext4 réinitialise les pointeurs d'inode lors de la suppression.

**FAT32/exFAT** (USB, cartes SD) : structure simple, peu de métadonnées, pas de journalisation, pas d'ADS. Les fichiers supprimés sont souvent récupérables car FAT marque l'entrée de répertoire comme supprimée sans effacer les données.

**APFS** (macOS/iOS) : chiffrement natif (FileVault intégré), snapshots (instantanés récupérables contenant des états antérieurs du volume — source forensic précieuse), et clones. Le chiffrement natif rend l'acquisition physique sans clé inutile.

#### 9.4 Fichiers supprimés et carving

Comprendre ce qui se passe lors de la suppression est fondamental. Sur NTFS, supprimer un fichier marque l'entrée MFT comme inactive et libère les clusters — les données restent physiquement sur le disque tant que les clusters ne sont pas réécrits. Le **carving** est la technique de récupération par signature : l'outil (Scalpel, PhotoRec, foremost) parcourt l'espace non alloué en cherchant les en-têtes et pieds de page des formats de fichiers connus (JPEG commence par `FF D8 FF`, PDF par `%PDF-`, DOCX par `PK` car c'est un ZIP). Le carving fonctionne même quand l'entrée MFT est perdue — il retrouve les données brutes par leur structure interne. Mais sur SSD avec TRIM, les données supprimées sont souvent effacées physiquement par le contrôleur — le carving ne retrouve rien.

#### 9.5 Timestamps MACB et détection du timestomping

Les timestamps MACB sont les artefacts temporels fondamentaux de l'analyse forensic. En NTFS, chaque fichier possède deux jeux de timestamps (dans $SI et dans $FN). La comparaison entre les deux est l'outil principal de détection du timestomping.

Méthode concrète avec MFTECmd : parser la $MFT avec `MFTECmd.exe -f '$MFT' --csv output/ --csvf mft_results.csv`, puis ouvrir le CSV dans Timeline Explorer et comparer les colonnes `SI_Created` et `FN_Created`. Si `SI_Created` est antérieur à `FN_Created` (le fichier aurait été « créé » avant que son nom n'existe), c'est un indicateur de timestomping.

Les **fuseaux horaires** sont un piège récurrent. Les timestamps NTFS sont stockés en UTC, mais les outils d'affichage (Event Viewer, explorateur Windows) les convertissent en heure locale. Si deux machines dans des fuseaux horaires différents sont corrélées sans conversion en UTC, la timeline est incohérente. Règle : toujours travailler en UTC dans l'analyse forensic, convertir en heure locale uniquement pour la présentation au rapport.

#### 9.6 Slack space et unallocated space

Le **slack space** est l'espace résiduel entre la fin d'un fichier et la fin du cluster alloué (les systèmes de fichiers allouent par clusters de 4 Ko typiquement — un fichier de 2 Ko occupe un cluster entier, les 2 Ko restants contiennent des fragments du fichier précédemment stocké à cet emplacement). L'**unallocated space** est l'ensemble des clusters non affectés à un fichier actif — c'est là que se trouvent les données des fichiers supprimés. L'analyse de ces espaces par carving peut révéler des données que l'attaquant croyait avoir détruites.

---

### Chapitre 10 — Timeline analysis et corrélation temporelle

#### 10.1 Pourquoi la timeline est le livrable central

La timeline (chronologie d'investigation) est la reconstruction ordonnée dans le temps de tous les événements pertinents de l'incident. C'est le livrable qui répond à la question fondamentale du forensic : que s'est-il passé, dans quel ordre ? C'est aussi le support de raisonnement principal de l'analyste : en examinant la séquence des événements, il identifie les patterns, les corrélations, et les lacunes.

Une timeline forensic complète peut contenir des millions d'événements (sur une machine Windows, la MFT seule produit des centaines de milliers d'entrées, les Event Logs en ajoutent des dizaines de milliers, le Prefetch, l'Amcache, le registre, le navigateur en ajoutent encore). L'enjeu n'est pas de tout voir — c'est de filtrer, de prioriser, et de corréler.

#### 10.2 Construction d'une Super Timeline avec Plaso

**Plaso** (anciennement log2timeline) est l'outil de référence pour la construction de Super Timelines. Il prend en entrée une image disque (ou un ensemble d'artefacts collectés par KAPE) et produit en sortie un fichier contenant TOUS les événements temporels de toutes les sources, fusionnés et triés chronologiquement.

Workflow concret :

```bash
# Étape 1 : extraction des événements (long — heures sur une image de 500 Go)
log2timeline.py --storage-file timeline.plaso image.E01

# Étape 2 : filtrage et export en CSV
psort.py -o l2tcsv timeline.plaso -w timeline.csv "date > '2026-01-01' AND date < '2026-03-08'"
```

Le résultat est un CSV contenant potentiellement des millions de lignes, chaque ligne étant un événement avec sa date/heure, sa source (MFT, Event Log, Prefetch, navigateur...), sa description, et des métadonnées contextuelles.

Les **parsers Plaso** sont les modules qui extraient les événements de chaque type de source. Les parsers les plus importants pour le forensic Windows : `filestat` (timestamps du système de fichiers), `winevtx` (Event Logs), `prefetch` (Prefetch), `winreg` (registre), `chrome_history` / `firefox_history` (navigateurs), et `mft` (MFT NTFS). Pour Linux : `syslog`, `bash_history`, `wtmp`.

Les pièges de Plaso : le temps de traitement est long (plusieurs heures pour une image de 500 Go), le volume de données produit est massif (il faut filtrer agressivement), et les parsers peuvent produire des faux positifs (événements mal interprétés ou dupliqués entre parsers).

#### 10.3 Visualisation et analyse avec Timeline Explorer et Timesketch

**Timeline Explorer** (Eric Zimmerman) est l'outil de visualisation le plus utilisé pour analyser les CSV produits par Plaso ou par les autres outils de la suite Zimmerman. Il permet le filtrage par colonne (filtrer par source, par chemin de fichier, par mots-clés), le tri chronologique, le marquage d'événements (bookmarks), et l'export des résultats filtrés.

**Timesketch** (open source, développé par Google) est une plateforme web collaborative de visualisation de timelines. Il permet l'import de timelines Plaso, le partage entre analystes, l'annotation collaborative, et l'application de « sketches » (filtres prédéfinis pour identifier des patterns courants — beaconing, mouvement latéral, exfiltration).

#### 10.4 Corrélation multi-sources

Le défi de la corrélation est de fusionner des événements provenant de sources hétérogènes (endpoint + réseau + AD + cloud) dans une timeline cohérente. Un exemple concret : à 14h32:15 UTC, le Prefetch montre l'exécution de `psexec.exe` sur la machine A ; à 14h32:18 UTC, le Security Event Log de la machine B montre une authentification réussie (4624 type 3) depuis l'IP de la machine A avec le compte `svc_deploy` ; à 14h32:22 UTC, le log pare-feu montre un flux autorisé de A vers B sur le port 445 (SMB). Ces trois événements, provenant de trois sources différentes, racontent la même histoire : mouvement latéral de A vers B via PsExec.

La corrélation multi-sources exige une synchronisation horaire fiable (NTP — si les horloges ne sont pas synchronisées, les événements ne peuvent pas être alignés), une normalisation des fuseaux horaires (tout en UTC), et une normalisation des identifiants (le même compte peut apparaître sous différentes formes selon la source : `DOMAIN\user`, `user@domain.com`, SID).

#### 10.5 Pièges de la corrélation temporelle

**Fuseaux horaires incohérents :** les timestamps NTFS sont en UTC, les Event Logs Windows sont en UTC, les logs proxy peuvent être en heure locale, les logs applicatifs peuvent être dans le fuseau du serveur, et les captures réseau (PCAP) sont en UTC. Si un analyste mélange des sources sans normaliser en UTC, sa timeline est fausse.

**Précision des timestamps :** les timestamps NTFS ont une précision de 100 nanosecondes, les Event Logs ont une précision de 100 nanosecondes (format FILETIME), mais les logs proxy ou applicatifs peuvent n'avoir qu'une précision à la seconde. Ordonner des événements à la seconde près quand certaines sources n'ont qu'une précision à la seconde est un exercice de prudence.

**Timestamps falsifiés :** le timestomping modifie les timestamps $SI des fichiers (Ch.9, Ch.24). La corrélation avec d'autres sources (Event Logs, $UsnJrnl, $FN) permet de détecter les incohérences.

#### 10.6 Fil rouge — MUSIC BOX : la timeline de 60 jours

> **🔬 MUSIC BOX — Épisode 9**
>
> Dimanche. Claire construit la Super Timeline de WKS-RD-047 avec Plaso : 2,4 millions d'événements sur 60 jours. Elle filtre sur les événements les plus pertinents (exécution de programmes, accès réseau, modifications de fichiers dans les répertoires sensibles) et réduit à environ 15 000 événements exploitables. La corrélation avec les logs proxy (beaconing C2), les logs AD (authentifications), et les logs AWS (accès aux buckets S3) produit une timeline unifiée qui reconstitue les 60 jours de présence de l'attaquant.

---

### Chapitre 11 — Corrélation, raisonnement analytique et gestion des biais

#### 11.1 Le forensic n'est pas juste extraire des artefacts

La compétence technique — savoir parser une MFT, analyser un dump mémoire, interpréter un Event Log — est nécessaire mais pas suffisante. Ce qui distingue un analyste compétent d'un opérateur d'outils, c'est la capacité à raisonner sur les données : formuler des hypothèses, les tester, gérer l'incertitude, et distinguer ce que les données montrent de ce que l'analyste infère.

#### 11.2 Raisonnement par hypothèse

L'investigateur forensic ne cherche pas « la vérité » — il formule des hypothèses et les teste contre les données disponibles. Pour chaque question investigative, au moins deux hypothèses doivent être formulées.

Exemple dans MUSIC BOX : le compte `svc-backup` a été utilisé pour supprimer des fichiers de recherche. Hypothèse 1 : le compte a été compromis par un attaquant externe et utilisé pour l'exfiltration et la destruction de données. Hypothèse 2 : le titulaire légitime du compte (un administrateur système) a supprimé les fichiers pour une raison légitime ou malveillante (insider threat). L'investigation doit collecter des données qui permettent de discriminer entre ces hypothèses : l'IP source des connexions (interne vs externe), la présence d'un malware sur la machine, les logs de keylogging ou de credential dumping, et le profil comportemental de l'administrateur.

#### 11.3 Le biais de confirmation

Le biais de confirmation est le piège le plus dangereux de l'investigation forensic. Il consiste à chercher sélectivement les données qui confirment l'hypothèse initiale et à ignorer ou minimiser celles qui la contredisent. Ce biais est inconscient et universel — même les analystes expérimentés y sont vulnérables.

Exemple : l'analyste suspecte un insider (un employé sur le départ). Il trouve des fichiers copiés sur une clé USB. Il interprète immédiatement : « voilà la preuve du vol de données ». Mais il ne cherche pas si le malware présent sur la machine a pu copier les fichiers automatiquement vers la clé USB. Il ne vérifie pas si l'employé copiait régulièrement des fichiers sur USB dans le cadre de son travail normal. Le biais de confirmation l'a conduit à s'enfermer dans sa première hypothèse sans tester les alternatives.

Contremesure : pour chaque conclusion, l'analyste se pose la question « qu'est-ce qui pourrait contredire cette interprétation ? » et recherche activement ces données contradictoires. La discipline de l'hypothèse alternative (formuler au moins 2 hypothèses et les tester toutes) est le garde-fou principal.

#### 11.4 Niveaux de confiance dans les conclusions

Chaque conclusion forensic doit être accompagnée d'un niveau de confiance explicite.

**Fait vérifié :** observable directement dans les données, reproductible. « Le fichier `rclone.exe` a été exécuté sur WKS-RD-047 le 2 mars 2026 à 14h32 UTC » (constaté dans le Prefetch ET l'Amcache ET les Event Logs — triple confirmation).

**Déduction logique :** conclusion tirée par raisonnement à partir de faits vérifiés. « L'exfiltration a été réalisée via rclone, car le SRUM montre que `rclone.exe` a transféré 180 Go de données réseau entre le 2 et le 7 mars, et les logs proxy confirment des flux HTTPS vers des endpoints S3 AWS depuis cette machine pendant la même période. » (déduction forte, basée sur la convergence de 3 sources indépendantes).

**Hypothèse plausible :** interprétation cohérente mais non confirmée de manière certaine. « L'attaquant est probablement d'origine russophone, car les metadata du document Word piégé contiennent un auteur avec un nom cyrillique et le RAT utilise un C2 dans un ASN associé à un hébergeur d'Asie du Sud-Est couramment utilisé par des groupes russophones » (indices convergents mais non conclusifs — l'attaquant pourrait avoir falsifié ces éléments).

**Inconnue :** ce que l'investigation n'a pas pu déterminer. « L'identité réelle de l'attaquant n'a pas pu être établie dans le cadre de cette investigation. » Documenter les inconnues est aussi important que documenter les conclusions.

#### 11.5 Corrélation vs causalité

Deux événements proches dans le temps ne sont pas nécessairement liés. Un reboot de serveur à 03h00 et une connexion C2 à 03h02 ne sont pas forcément le même incident — le reboot peut être une maintenance planifiée, et la connexion C2 un beaconing régulier qui a coïncidé temporellement. La corrélation temporelle est un indice, pas une preuve de causalité. L'analyste doit chercher des liens causaux (le reboot a été déclenché par un script déposé par l'attaquant — vérifiable dans les Event Logs et le registre) et ne pas se contenter de la proximité temporelle.

#### 11.6 Fil rouge — MUSIC BOX : les hypothèses concurrentes

> **🔬 MUSIC BOX — Épisode 10**
>
> Lundi. Claire formule ses hypothèses concurrentes pour la question investigative #1 (vecteur d'accès initial).
>
> **H1 :** Spearphishing avec document piégé envoyé au Dr. Mallet. Indices : le RAT est actif sur son poste, les emails suspects sont à vérifier.
> **H2 :** Compromission d'un accès VPN/RDP exposé sur Internet. Indices : vérifier les logs VPN pour des connexions anormales.
> **H3 :** Insider — le Dr. Mallet ou un collègue a intentionnellement installé le RAT. Indices : vérifier le comportement de l'utilisateur, les accès physiques, et les motivations.
>
> L'investigation des emails (export PST de la boîte du Dr. Mallet) révèle un email de spearphishing reçu le 6 janvier 2026 (J-60), prétendant provenir d'un partenaire de recherche (`novapharma-partners.com` — domaine imitant le domaine légitime `novapharma-partner.com`). Le document Word joint contient une macro VBA obfusquée (confirmé par olevba). **H1 est confirmée. H2 et H3 ne sont pas soutenues par les données** (pas de connexion VPN anormale, pas d'accès physique suspect). Mais H3 n'est pas formellement exclue — elle est documentée comme « non soutenue en l'état ».

---
