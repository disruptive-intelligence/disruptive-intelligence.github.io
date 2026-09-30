---
title: Windows
source: IT/02_Windows/Windows.md
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

- [Partie I — Architecture fondamentale](01-partie-i-architecture-fondamentale.md)
- [Partie II — Processus, exécution et code](02-partie-ii-processus-execution-et-code.md)
- [Partie III — Credentials et authentification](03-partie-iii-credentials-et-authentification.md)
- [Partie IV — Réseau et communication](04-partie-iv-reseau-et-communication.md)
- [Partie V — Modèle de sécurité et protections](05-partie-v-modele-de-securite-et-protections.md)
- [Partie VI — Event logs, artefacts et forensic](06-partie-vi-event-logs-artefacts-et-forensic.md)
- [Partie VII — Hardening, cas de synthèse et référence](07-partie-vii-hardening-cas-de-synthese-et-reference.md)
- [Annexes](08-annexes.md)
- [Questions essentielles](09-questions-essentielles.md)
- [Questions complémentaires](10-questions-complementaires.md)
- [Réponses flash](11-reponses-flash.md)
