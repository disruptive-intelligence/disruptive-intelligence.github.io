---
title: Windows en profondeur
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
format: cours
revue: '2026-10-04'
revision: library/revision/windows.md
---

*Architecture • Internals • Sécurité • Investigation*

**Cours complet — 31 chapitres • 7 parties • 7 annexes**

*Boot • Noyau • NTFS • Registre • Processus • Credentials • Réseau • Sécurité • Forensics*

---

### Fil rouge : Opération SHADOW

> **Contexte narratif — ce fil rouge traverse les 26 premiers chapitres et se conclut au Ch.28.**
>
> **Léa Chen**, analyste SOC senior / IR chez **CyberShield** (MSSP, 60 personnes), est appelée pour investiguer un incident sur le SI de **Valtec Industries** — équipementier automobile, 1 800 collaborateurs, 2 sites (siège Toulouse, usine Valenciennes), Windows Server 2022 + postes Windows 11, AD on-prem, EDR CrowdStrike déployé.
>
> **L'alerte :** CrowdStrike détecte un processus `rundll32.exe` exécuté par `winword.exe` avec une commande suspecte, contactant une IP externe. L'arbre de processus est immédiatement anormal : `winword.exe` ne devrait JAMAIS lancer `rundll32.exe` (le parent normal de rundll32 est explorer.exe ou svchost.exe pour les opérations légitimes).
>
> L'investigation de Léa va traverser les 7 parties du cours — de l'architecture Windows (comprendre le normal pour détecter l'anormal) aux artefacts forensic (reconstituer la chronologie complète), en passant par les mécanismes d'exécution, les credentials, le réseau et les protections.

---

## Sommaire

- [Partie I — Architecture fondamentale](01-partie-i-architecture-fondamentale/index.md)
    - [Chapitre 1 — Vue d'ensemble de Windows](01-partie-i-architecture-fondamentale/01-chapitre-1-vue-d-ensemble-de-windows.md)
    - [Chapitre 2 — Le processus de démarrage](01-partie-i-architecture-fondamentale/02-chapitre-2-le-processus-de-demarrage.md)
    - [Chapitre 3 — Noyau, mémoire et pilotes](01-partie-i-architecture-fondamentale/03-chapitre-3-noyau-memoire-et-pilotes.md)
    - [Chapitre 4 — Le système de fichiers NTFS](01-partie-i-architecture-fondamentale/04-chapitre-4-le-systeme-de-fichiers-ntfs.md)
    - [Chapitre 5 — Registre Windows, ruches et persistance](01-partie-i-architecture-fondamentale/05-chapitre-5-registre-windows-ruches-et-persistance.md)
- [Partie II — Processus, exécution et code](02-partie-ii-processus-execution-et-code.md)
- [Partie III — Credentials et authentification](03-partie-iii-credentials-et-authentification.md)
- [Partie IV — Réseau et communication](04-partie-iv-reseau-et-communication.md)
- [Partie V — Modèle de sécurité et protections](05-partie-v-modele-de-securite-et-protections/index.md)
    - [Chapitre 17 — Modèle de sécurité, intégrité et mitigations mémoire](05-partie-v-modele-de-securite-et-protections/01-chapitre-17-modele-de-securite-integrite-et-mitiga.md)
    - [Chapitre 18 — Authentification locale et domaine](05-partie-v-modele-de-securite-et-protections/02-chapitre-18-authentification-locale-et-domaine.md)
    - [Chapitre 19 — Privilèges, élévation et contrôle d'exécution](05-partie-v-modele-de-securite-et-protections/03-chapitre-19-privileges-elevation-et-controle-d-exe.md)
    - [Chapitre 20 — Détection moderne : AMSI, ETW, EDR et BYOVD](05-partie-v-modele-de-securite-et-protections/04-chapitre-20-detection-moderne-amsi-etw-edr-et-byov.md)
- [Partie VI — Event logs, artefacts et forensic](06-partie-vi-event-logs-artefacts-et-forensic.md)
- [Partie VII — Hardening, cas de synthèse et référence](07-partie-vii-hardening-cas-de-synthese-et-reference.md)
- [Annexes](08-annexes.md)
