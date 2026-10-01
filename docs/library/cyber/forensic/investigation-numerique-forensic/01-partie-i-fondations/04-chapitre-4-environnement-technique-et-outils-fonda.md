---
title: Chapitre 4 — Environnement technique et outils fondamentaux
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 4.1 Le lab forensic

Un laboratoire forensic est un environnement contrôlé dédié à l'analyse des preuves numériques. Son objectif est double : protéger l'intégrité des preuves et fournir les outils nécessaires à l'analyse.

Le **matériel** comprend des write blockers matériels (Tableau/Guidance T356789iu, CRU WiebeTech — qui empêchent physiquement toute écriture sur le support source, indépendamment du logiciel), des duplicateurs forensic (Logicube Falcon Neo, Atola TaskForce — pour les acquisitions rapides avec hashing intégré), et des stations d'analyse puissantes (minimum 64 Go de RAM pour l'analyse mémoire avec Volatility, stockage rapide NVMe pour les images disque qui font souvent plusieurs centaines de Go, processeurs multi-cœurs pour le traitement de Super Timelines qui peuvent contenir des millions d'événements).

Le **réseau du lab** est isolé du réseau de production (on ne connecte jamais un support potentiellement compromis au réseau d'entreprise). Le stockage des preuves est sécurisé : coffre physique fermé à clé (ou salle avec contrôle d'accès et vidéosurveillance pour les investigations judiciaires), registre d'accès documentant chaque entrée/sortie de support.

## 4.2 Distributions forensic

Plusieurs distributions Linux pré-configurées facilitent le travail forensic. **SIFT Workstation** (SANS Investigative Forensic Toolkit), maintenue par le SANS Institute, est la référence pédagogique et professionnelle — basée sur Ubuntu, elle contient Autopsy, Volatility, Plaso, RegRipper, les outils Eric Zimmerman (via Wine ou natifs), et des centaines d'outils spécialisés. **Tsurugi Linux** est une distribution très complète d'origine japonaise/italienne. **CSI Linux** est orientée investigation et OSINT. **Kali Linux**, connue pour le pentest, inclut un méta-paquet forensic (`kali-tools-forensics`). **REMnux** est spécialisée dans l'analyse de malware.

Le choix de la distribution est moins important que la maîtrise des outils qu'elle contient. Un analyste expert avec un Ubuntu nu et les bons outils installés sera plus efficace qu'un débutant avec la distribution la plus complète.

## 4.3 Outils open source vs commerciaux

Les outils forensic se répartissent en deux catégories. Les **outils open source** (Autopsy/The Sleuth Kit pour le disk forensics, Volatility 3 pour le memory forensics, Wireshark/Zeek pour le network forensics, Plaso pour la Super Timeline, RegRipper pour le registre Windows) sont gratuits, auditables (leur code source est vérifiable — argument important pour le contradictoire), et largement utilisés tant par les forces de l'ordre que par les cabinets privés. Les **outils commerciaux** (EnCase d'OpenText, FTK d'Exterro, X-Ways Forensics, Magnet AXIOM, Cellebrite UFED pour le mobile) offrent des interfaces intégrées, un support commercial, et sont parfois requis ou préférés par certaines juridictions ou certains clients institutionnels.

En 2025-2026, la tendance est clairement à la convergence : Autopsy est devenu une plateforme mature capable de rivaliser avec les outils commerciaux pour le disk forensics, Volatility 3 est la référence incontestée pour le memory forensics (même les éditeurs commerciaux l'utilisent comme moteur), et les outils Eric Zimmerman ont transformé le Windows forensics en fournissant des parsers spécialisés de qualité professionnelle, gratuitement.

## 4.4 La suite Eric Zimmerman — l'outillage Windows forensics de référence

Eric Zimmerman est un ancien agent du FBI devenu formateur SANS, qui a développé une suite d'outils de parsing forensic pour Windows, devenus la référence de facto en 2025-2026. Ces outils parsent les artefacts Windows bruts et produisent des résultats structurés (CSV) exploitables dans Timeline Explorer ou un tableur.

**MFTECmd** parse la $MFT (Master File Table) NTFS et produit une timeline de tous les fichiers avec leurs timestamps $SI et $FN — indispensable pour détecter le timestomping. **PECmd** parse le Prefetch — historique d'exécution des programmes avec dates, nombre d'exécutions, et fichiers chargés. **LECmd** parse les fichiers LNK (raccourcis) — révèlent les fichiers récemment ouverts, les chemins réseau accédés, les volumes USB connectés. **SBECmd** (ShellBags Explorer) parse les ShellBags du registre — historique complet de la navigation dans l'explorateur de fichiers. **JLECmd** parse les Jump Lists — fichiers récemment ouverts par application. **EvtxECmd** parse les Event Logs Windows (format evtx) en CSV structuré — beaucoup plus rapide et flexible que l'Event Viewer natif. **RECmd** parse le registre Windows en ligne de commande avec des batch files prédéfinies. **AmcacheParser** parse l'Amcache — historique des programmes exécutés avec hash SHA1. **AppCompatCacheParser** parse le ShimCache — historique des programmes avec timestamps. **SrumECmd** parse la base SRUM — consommation réseau et CPU par processus. **Timeline Explorer** est l'interface de visualisation qui permet de filtrer, trier, et analyser les CSV produits par tous les outils ci-dessus.

Ces outils sont distribués gratuitement via le site d'Eric Zimmerman (ericzimmerman.github.io) et sont pré-installés dans SIFT Workstation. Ils sont utilisés tout au long de la Partie IV.

## 4.5 Hashing et vérification d'intégrité

Le hashing est le mécanisme fondamental de vérification d'intégrité en forensic. Un hash est une empreinte numérique de taille fixe calculée à partir de l'intégralité des données : si un seul bit change, le hash change complètement. **MD5** (128 bits) est rapide mais théoriquement vulnérable aux collisions (deux fichiers différents produisant le même hash — démontré en 2004). **SHA-256** (256 bits) est plus robuste et considéré comme sûr. La pratique recommandée est le **double hashing** (MD5 + SHA-256) : les deux doivent correspondre. La probabilité que deux fichiers différents produisent le même MD5 ET le même SHA-256 est négligeable.

Les outils standards sont `md5sum` et `sha256sum` (Linux), `Get-FileHash` (PowerShell), et `hashdeep` (multi-hash, récursif — utile pour hasher des répertoires entiers). Chaque acquisition doit être accompagnée de ses hash, notés dans le journal d'investigation et le formulaire de chaîne de custody.

## 4.6 Outils d'acquisition et formats d'images

L'acquisition bit-à-bit d'un disque se fait avec des outils spécifiques. La commande **dd** (Linux) est l'outil historique : `dd if=/dev/sdX of=/path/image.raw bs=4M status=progress` — simple, universel, mais sans hashing intégré ni barre de progression utile. **dc3dd** (développé par le DoD américain) ajoute le hashing intégré, le logging, et la gestion des erreurs. **FTK Imager** (gratuit, Windows et Linux) est l'outil le plus utilisé en entreprise : interface graphique, hashing automatique, support des formats E01 et AFF4, preview du contenu avant acquisition. **Guymager** (Linux, open source) offre une acquisition multi-threadée rapide avec interface graphique.

Les formats d'images : le format **raw** (dd) est une copie exacte, secteur par secteur — simple mais volumineux (taille = taille du disque source) et sans métadonnées intégrées. Le format **E01** (EnCase/Expert Witness Format) compresse les données (réduction de 30-50 % typiquement), intègre les métadonnées (hash, notes, informations de case), et permet la segmentation en fichiers multiples — c'est le format le plus utilisé en forensic. Le format **AFF4** (Advanced Forensic Format 4) est un format ouvert moderne, conteneurisé, qui supporte le stockage de multiples types d'évidences dans un seul conteneur.

## 4.7 Outils de triage rapide

Les outils de triage collectent rapidement les artefacts les plus pertinents sans image complète du disque. **KAPE** (Kroll Artifact Parser and Extractor) utilise des targets (définitions de quels fichiers/artefacts collecter) et des modules (parsers pour analyser les artefacts collectés). La commande `kape.exe --tsource C: --tdest E:\Output --target KapeTriage` collecte en quelques minutes les Event Logs, le registre, le Prefetch, l'Amcache, le ShimCache, la $MFT, le SRUM, les historiques navigateur, et d'autres artefacts clés. **Velociraptor** (open source, développé initialement par Google) est un agent déployable sur tout un parc : il permet de lancer des collectes et des hunts à distance sur des centaines de machines simultanément via des requêtes VQL (Velociraptor Query Language). **DFIR-ORC** (développé par l'ANSSI) est un outil de collecte français optimisé pour les grands déploiements dans les OIV.

## 4.8 Environnement d'analyse

L'analyse se fait toujours sur une machine dédiée, jamais sur la machine source. L'environnement standard est une VM isolée du réseau, avec des snapshots pour pouvoir revenir en arrière si une manipulation corrompt l'état de l'analyse. Les images forensic sont montées en lecture seule dans la VM (sous Linux : `mount -o ro,loop,noexec image.raw /mnt/evidence`). Arsenal Image Mounter (Windows) permet de monter des images E01 comme des disques virtuels accessibles en lecture seule. La configuration de l'environnement (version des outils, options utilisées, paramètres de montage) est documentée pour la reproductibilité.

## 4.9 Fil rouge — MUSIC BOX : le lab et l'acquisition initiale

> **🔬 MUSIC BOX — Épisode 4**
>
> Vendredi soir, 19h00. L'équipe met en place le dispositif d'investigation. Claire utilise sa station forensic portable (laptop avec 64 Go de RAM, 4 To NVMe, SIFT Workstation en VM, write blocker Tableau T35es).
>
> **Acquisition mémoire (priorité absolue) :** DumpIt est exécuté sur WKS-RD-047 (machine allumée, session utilisateur active). Dump RAM : 32 Go, 14 minutes. Hash SHA-256 calculé immédiatement : `a7f3e2...`. Documenté dans le journal d'investigation et le formulaire de chaîne de custody.
>
> **Triage KAPE :** lancé sur WKS-RD-047 en parallèle du dump. Target : KapeTriage. Résultat : tous les artefacts Windows critiques collectés en 8 minutes. Hash calculé sur l'archive.
>
> **Acquisition disque prévue samedi matin** avec l'experte judiciaire — image E01 via FTK Imager avec write blocker matériel.
>
> **Serveur R&D Linux (SRV-RD-01) :** la machine est en production et ne peut pas être éteinte (les expériences en cours seraient perdues). Décision : acquisition logique à chaud — copie des logs (`/var/log/`), de l'historique bash, du crontab, des authorized_keys SSH, et des fichiers récemment modifiés. Image disque reportée à un arrêt de maintenance planifié (dans 5 jours).
>
> Choix du format : E01 pour l'image disque (compression, métadonnées intégrées, compatibilité Autopsy). Raw pour le dump mémoire (compatibilité Volatility 3).

---
