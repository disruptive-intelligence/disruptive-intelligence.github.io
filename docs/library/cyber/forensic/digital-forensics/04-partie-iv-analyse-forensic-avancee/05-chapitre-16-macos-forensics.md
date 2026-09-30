---
title: Chapitre 16 — macOS forensics
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

## 16.1 Artefacts spécifiques macOS

macOS possède des artefacts forensic riches et spécifiques qui n'existent pas sur Windows ni Linux.

Le **Unified Logging** (introduit en macOS 10.12) est le système de journalisation le plus riche des OS modernes — il capture des milliards d'événements par jour (processus, réseau, système, applications). L'outil `log show` permet d'interroger les logs avec des filtres : `log show --predicate 'processImagePath contains "ssh"' --start "2026-01-01" --end "2026-03-08"`. L'outil `log collect` exporte les logs pour analyse offline.

Les **FSEvents** (File System Events, stockés dans `.fseventsd/` à la racine de chaque volume) enregistrent toutes les modifications du système de fichiers avec un identifiant d'événement séquentiel. Ils persistent même après suppression des fichiers — c'est l'équivalent fonctionnel du $UsnJrnl de Windows.

**KnowledgeC.db** (`~/Library/Application Support/Knowledge/KnowledgeC.db`) est une base SQLite qui enregistre l'activité utilisateur : applications ouvertes avec durée d'utilisation, activité réseau, période d'éveil de la machine, et interactions utilisateur. C'est une source forensic extrêmement riche, spécifique à macOS.

Les **Spotlight metadata** (index `.Spotlight-V100/`) contiennent les métadonnées de tous les fichiers indexés par Spotlight — même si les fichiers sont supprimés, les métadonnées peuvent persister dans l'index.

**TCC.db** (`~/Library/Application Support/com.apple.TCC/TCC.db`) enregistre les permissions d'accès aux ressources sensibles (caméra, microphone, fichiers, accessibilité). Un malware qui a obtenu l'accès à l'accessibilité ou au Full Disk Access sera visible dans TCC.db.

**LaunchAgents / LaunchDaemons** (`~/Library/LaunchAgents/`, `/Library/LaunchAgents/`, `/Library/LaunchDaemons/`) sont les mécanismes de persistance macOS — des fichiers plist qui définissent des programmes à exécuter automatiquement.

Outils macOS forensics : **mac_apt** (macOS Artifact Parsing Tool — open source, parse les artefacts spécifiques macOS), **APOLLO** (Apple Pattern of Life Lazy Output — parse KnowledgeC.db et d'autres bases de données d'activité), et **Unified Log Parser**.

---
