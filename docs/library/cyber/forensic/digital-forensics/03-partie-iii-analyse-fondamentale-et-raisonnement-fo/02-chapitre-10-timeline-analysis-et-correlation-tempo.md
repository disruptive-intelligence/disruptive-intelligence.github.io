---
title: Chapitre 10 — Timeline analysis et corrélation temporelle
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie III — Analyse fondamentale ET raisonnement forensic
  - index.md
---

## 10.1 Pourquoi la timeline est le livrable central

La timeline (chronologie d'investigation) est la reconstruction ordonnée dans le temps de tous les événements pertinents de l'incident. C'est le livrable qui répond à la question fondamentale du forensic : que s'est-il passé, dans quel ordre ? C'est aussi le support de raisonnement principal de l'analyste : en examinant la séquence des événements, il identifie les patterns, les corrélations, et les lacunes.

Une timeline forensic complète peut contenir des millions d'événements (sur une machine Windows, la MFT seule produit des centaines de milliers d'entrées, les Event Logs en ajoutent des dizaines de milliers, le Prefetch, l'Amcache, le registre, le navigateur en ajoutent encore). L'enjeu n'est pas de tout voir — c'est de filtrer, de prioriser, et de corréler.

## 10.2 Construction d'une Super Timeline avec Plaso

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

## 10.3 Visualisation et analyse avec Timeline Explorer et Timesketch

**Timeline Explorer** (Eric Zimmerman) est l'outil de visualisation le plus utilisé pour analyser les CSV produits par Plaso ou par les autres outils de la suite Zimmerman. Il permet le filtrage par colonne (filtrer par source, par chemin de fichier, par mots-clés), le tri chronologique, le marquage d'événements (bookmarks), et l'export des résultats filtrés.

**Timesketch** (open source, développé par Google) est une plateforme web collaborative de visualisation de timelines. Il permet l'import de timelines Plaso, le partage entre analystes, l'annotation collaborative, et l'application de « sketches » (filtres prédéfinis pour identifier des patterns courants — beaconing, mouvement latéral, exfiltration).

## 10.4 Corrélation multi-sources

Le défi de la corrélation est de fusionner des événements provenant de sources hétérogènes (endpoint + réseau + AD + cloud) dans une timeline cohérente. Un exemple concret : à 14h32:15 UTC, le Prefetch montre l'exécution de `psexec.exe` sur la machine A ; à 14h32:18 UTC, le Security Event Log de la machine B montre une authentification réussie (4624 type 3) depuis l'IP de la machine A avec le compte `svc_deploy` ; à 14h32:22 UTC, le log pare-feu montre un flux autorisé de A vers B sur le port 445 (SMB). Ces trois événements, provenant de trois sources différentes, racontent la même histoire : mouvement latéral de A vers B via PsExec.

La corrélation multi-sources exige une synchronisation horaire fiable (NTP — si les horloges ne sont pas synchronisées, les événements ne peuvent pas être alignés), une normalisation des fuseaux horaires (tout en UTC), et une normalisation des identifiants (le même compte peut apparaître sous différentes formes selon la source : `DOMAIN\user`, `user@domain.com`, SID).

## 10.5 Pièges de la corrélation temporelle

**Fuseaux horaires incohérents :** les timestamps NTFS sont en UTC, les Event Logs Windows sont en UTC, les logs proxy peuvent être en heure locale, les logs applicatifs peuvent être dans le fuseau du serveur, et les captures réseau (PCAP) sont en UTC. Si un analyste mélange des sources sans normaliser en UTC, sa timeline est fausse.

**Précision des timestamps :** les timestamps NTFS ont une précision de 100 nanosecondes, les Event Logs ont une précision de 100 nanosecondes (format FILETIME), mais les logs proxy ou applicatifs peuvent n'avoir qu'une précision à la seconde. Ordonner des événements à la seconde près quand certaines sources n'ont qu'une précision à la seconde est un exercice de prudence.

**Timestamps falsifiés :** le timestomping modifie les timestamps $SI des fichiers (Ch.9, Ch.24). La corrélation avec d'autres sources (Event Logs, $UsnJrnl, $FN) permet de détecter les incohérences.

## 10.6 Fil rouge — MUSIC BOX : la timeline de 60 jours

> **🔬 MUSIC BOX — Épisode 9**
>
> Dimanche. Claire construit la Super Timeline de WKS-RD-047 avec Plaso : 2,4 millions d'événements sur 60 jours. Elle filtre sur les événements les plus pertinents (exécution de programmes, accès réseau, modifications de fichiers dans les répertoires sensibles) et réduit à environ 15 000 événements exploitables. La corrélation avec les logs proxy (beaconing C2), les logs AD (authentifications), et les logs AWS (accès aux buckets S3) produit une timeline unifiée qui reconstitue les 60 jours de présence de l'attaquant.

---
