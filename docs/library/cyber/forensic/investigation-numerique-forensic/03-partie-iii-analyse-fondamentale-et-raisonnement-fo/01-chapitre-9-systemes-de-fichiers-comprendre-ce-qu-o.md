---
title: 'Chapitre 9 — Systèmes de fichiers : comprendre ce qu''on analyse'
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie III — Analyse fondamentale et raisonnement forensic
  - index.md
---

## 9.1 Pourquoi comprendre le système de fichiers

Le système de fichiers est la couche d'organisation entre le stockage brut (secteurs du disque) et les fichiers tels que l'utilisateur les voit. Sans comprendre cette couche, l'analyste ne peut pas interpréter les métadonnées, récupérer les fichiers supprimés, ni détecter les manipulations de timestamps. Chaque système de fichiers a sa propre logique de stockage, ses propres métadonnées, et ses propres artefacts forensic.

## 9.2 NTFS — le système de fichiers le plus riche en artefacts

NTFS (New Technology File System) est le système de fichiers standard de Windows et le plus riche en artefacts forensic.

La **MFT** (Master File Table) est le cœur de NTFS : chaque fichier et dossier du volume possède une entrée dans la MFT (enregistrement de 1 024 octets) qui contient ses attributs. Les attributs clés pour le forensic :

**$STANDARD_INFORMATION ($SI)** contient les timestamps MACB (Modified, Accessed, Changed, Born/Created) du fichier. Ces timestamps sont modifiés par le système d'exploitation lors des opérations normales, mais AUSSI par les outils de timestomping (l'attaquant modifie délibérément les dates pour brouiller la timeline). C'est pourquoi $SI seul ne suffit pas pour dater fiablement un fichier.

**$FILE_NAME ($FN)** contient un second jeu de timestamps MACB, mis à jour uniquement lors du renommage ou du déplacement du fichier — ils sont beaucoup plus difficiles à falsifier (les outils de timestomping standard ne les modifient pas). La comparaison $SI vs $FN est l'outil fondamental de détection du timestomping : si $SI indique « créé en 2022 » mais $FN indique « créé le 3 mars 2026 », il y a eu manipulation.

**$DATA** contient le contenu du fichier lui-même. Pour les petits fichiers (< environ 700 octets), le contenu est stocké directement dans l'entrée MFT (resident data). Pour les fichiers plus grands, $DATA pointe vers les clusters du disque qui contiennent les données.

Les **ADS** (Alternate Data Streams) sont des flux de données secondaires attachés à un fichier, invisibles dans l'explorateur Windows et dans la plupart des commandes (`dir`). Un fichier `rapport.docx` peut avoir un ADS `rapport.docx:hidden_data` contenant des données cachées. Les ADS sont utilisés par Windows lui-même (le flux `Zone.Identifier` indique d'où un fichier a été téléchargé) et par les attaquants pour cacher des données ou du code.

Le journal **$UsnJrnl** (Update Sequence Number Journal) enregistre toutes les modifications de fichiers sur le volume : création, modification, suppression, renommage. Même si un fichier a été supprimé, le $UsnJrnl conserve la trace (avec le nom, la date, et l'opération). C'est une source forensic de première importance, parseable avec MFTECmd.

Le journal **$LogFile** enregistre les transactions NTFS pour la récupération après crash — il contient des informations sur les opérations récentes du système de fichiers.

## 9.3 ext4, FAT32/exFAT et APFS

**ext4** (Linux) utilise des inodes au lieu de la MFT. Les timestamps incluent crtime (creation time, introduit en ext4), mtime, atime, ctime. Le journal ext4 enregistre les transactions pour la cohérence. La récupération de fichiers supprimés est possible (extundelete, ext4magic) mais moins fiable qu'avec NTFS car ext4 réinitialise les pointeurs d'inode lors de la suppression.

**FAT32/exFAT** (USB, cartes SD) : structure simple, peu de métadonnées, pas de journalisation, pas d'ADS. Les fichiers supprimés sont souvent récupérables car FAT marque l'entrée de répertoire comme supprimée sans effacer les données.

**APFS** (macOS/iOS) : chiffrement natif (FileVault intégré), snapshots (instantanés récupérables contenant des états antérieurs du volume — source forensic précieuse), et clones. Le chiffrement natif rend l'acquisition physique sans clé inutile.

## 9.4 Fichiers supprimés et carving

Comprendre ce qui se passe lors de la suppression est fondamental. Sur NTFS, supprimer un fichier marque l'entrée MFT comme inactive et libère les clusters — les données restent physiquement sur le disque tant que les clusters ne sont pas réécrits. Le **carving** est la technique de récupération par signature : l'outil (Scalpel, PhotoRec, foremost) parcourt l'espace non alloué en cherchant les en-têtes et pieds de page des formats de fichiers connus (JPEG commence par `FF D8 FF`, PDF par `%PDF-`, DOCX par `PK` car c'est un ZIP). Le carving fonctionne même quand l'entrée MFT est perdue — il retrouve les données brutes par leur structure interne. Mais sur SSD avec TRIM, les données supprimées sont souvent effacées physiquement par le contrôleur — le carving ne retrouve rien.

## 9.5 Timestamps MACB et détection du timestomping

Les timestamps MACB sont les artefacts temporels fondamentaux de l'analyse forensic. En NTFS, chaque fichier possède deux jeux de timestamps (dans $SI et dans $FN). La comparaison entre les deux est l'outil principal de détection du timestomping.

Méthode concrète avec MFTECmd : parser la $MFT avec `MFTECmd.exe -f '$MFT' --csv output/ --csvf mft_results.csv`, puis ouvrir le CSV dans Timeline Explorer et comparer les colonnes `SI_Created` et `FN_Created`. Si `SI_Created` est antérieur à `FN_Created` (le fichier aurait été « créé » avant que son nom n'existe), c'est un indicateur de timestomping.

Les **fuseaux horaires** sont un piège récurrent. Les timestamps NTFS sont stockés en UTC, mais les outils d'affichage (Event Viewer, explorateur Windows) les convertissent en heure locale. Si deux machines dans des fuseaux horaires différents sont corrélées sans conversion en UTC, la timeline est incohérente. Règle : toujours travailler en UTC dans l'analyse forensic, convertir en heure locale uniquement pour la présentation au rapport.

## 9.6 Slack space et unallocated space

Le **slack space** est l'espace résiduel entre la fin d'un fichier et la fin du cluster alloué (les systèmes de fichiers allouent par clusters de 4 Ko typiquement — un fichier de 2 Ko occupe un cluster entier, les 2 Ko restants contiennent des fragments du fichier précédemment stocké à cet emplacement). L'**unallocated space** est l'ensemble des clusters non affectés à un fichier actif — c'est là que se trouvent les données des fichiers supprimés. L'analyse de ces espaces par carving peut révéler des données que l'attaquant croyait avoir détruites.

---
