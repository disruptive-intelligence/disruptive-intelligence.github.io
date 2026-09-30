---
title: PARTIE VII — FINALISATION ET PRODUCTION
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 8
chapters: 9
---

---

### Chapitre 26 — Rapport forensic et expertise judiciaire

#### 26.1 Le rapport comme produit final

Le rapport forensic transforme des centaines d'heures d'analyse technique en conclusions compréhensibles et défendables. C'est le document qui sera lu par le juge, le COMEX, l'assureur, ou le conseil d'administration. Le piège le plus fréquent : écrire un rapport technique brillant que seul un autre analyste forensic peut comprendre.

**Structure type du rapport forensic :**

**Résumé exécutif** (1-2 pages maximum) : résumé non technique des conclusions principales, de l'impact, et des recommandations. C'est souvent la seule section lue par les décideurs — elle doit être autonome et compréhensible.

**Cadre de l'investigation** : mandat (qui a demandé l'investigation, dans quel contexte), périmètre (quels systèmes, quelle période), questions investigatives, et méthodologie utilisée (outils, versions, paramètres — pour la reproductibilité et le contradictoire).

**Faits constatés** : chaque constatation est présentée factuellement, avec sa source (Event Log, artefact, capture réseau), sa date, et son niveau de confiance. La distinction fait/déduction/hypothèse (Ch.11) est explicite à chaque étape. Mauvais exemple : « L'attaquant a volé les données. » Bon exemple : « Le fichier `rclone.exe` a été exécuté sur WKS-RD-047 le 2 mars 2026 à 14h32 UTC (source : Prefetch, confirmé par Amcache — fait vérifié). Les logs proxy montrent des flux HTTPS vers des endpoints AWS S3 totalisant 183 Go depuis cette machine entre le 2 et le 7 mars (source : logs Squid — fait vérifié). Ces éléments indiquent une exfiltration de données de ce volume vers l'infrastructure AWS (déduction logique). »

**Analyse et interprétation** : reconstitution de la timeline complète, mapping ATT&CK, hypothèses concurrentes testées, et conclusions avec niveaux de confiance.

**Recommandations** : mesures correctives (éradication, durcissement, prévention), recommandations pour la procédure judiciaire (éléments de preuve exploitables, réquisitions complémentaires suggérées), et recommandations pour le forensic readiness.

**Annexes techniques** : IoC complets, timeline détaillée, captures d'écran, hash des preuves, et chaîne de custody.

#### 26.2 Écrire pour un juge

Le rapport judiciaire doit être compréhensible par un non-technicien. Les termes techniques sont définis quand ils sont utilisés pour la première fois. Les captures d'écran illustrent les constatations. Le raisonnement est explicite (« J'en déduis que... parce que... »). Les conclusions ne dépassent pas les constatations — l'expert donne un avis technique, pas un verdict.

Le témoignage d'expert (à la barre ou en audience) exige de vulgariser sans simplifier. L'expert doit être capable d'expliquer un timestamp NTFS à un procureur, une injection de processus à un avocat, et une chaîne de custody à un jury — en langage clair, sans condescendance, et en répondant aux questions du contre-interrogatoire avec rigueur.

#### 26.3 Le rapport de triage DFIR

Le rapport de triage est plus court (5-10 pages), orienté action et IoC, destiné au SOC et à l'équipe IR. Il contient les IoC (hash, domaines, IP, artefacts de persistance — immédiatement injectables dans le SIEM/EDR), les TTP observées (mapping ATT&CK — pour orienter le confinement et la remédiation), le périmètre de compromission connu (quelles machines, quels comptes), et les recommandations immédiates (quoi isoler, quoi reseter, quoi surveiller).

---

### Chapitre 27 — Forensic readiness : préparer l'organisation

Le forensic readiness est la capacité de l'organisation à mener une investigation forensic efficace quand un incident survient. C'est l'investissement préventif le plus rentable en forensic.

Les composantes : politique de rétention des logs (quelle durée, quelles sources, quel stockage — minimum 6 mois chaud, 12 mois froid), activation des sources critiques (PowerShell script block logging — Event ID 4104, Sysmon, audit AD étendu, processus creation avec ligne de commande — Event ID 4688 avec GPO), déploiement d'outils pré-positionnés (KAPE/Velociraptor/DumpIt sur clé USB sécurisée, accessible en urgence), protection de l'intégrité des logs (centralisation SIEM, stockage WORM — les logs locaux peuvent être effacés par l'attaquant), documentation de l'architecture SI (schéma réseau à jour, inventaire des serveurs et services, listes des comptes à privilèges, documentation des GPO), et formation des équipes (les IT doivent connaître les premiers réflexes : ne pas éteindre, ne pas nettoyer, appeler l'IR lead).

Sysmon est la recommandation de forensic readiness la plus impactante : son déploiement (gratuit, léger, configurable via XML) transforme la visibilité forensic d'une machine Windows en fournissant des Event IDs riches (processus avec hash et parenté, connexions réseau par processus, modifications de registre, chargement de DLL, accès à LSASS).

---

### Chapitre 28 — Forensic et incident response : intégration opérationnelle

Ce chapitre articule le forensic avec le processus IR détaillé dans le cours Incident Response de la bibliothèque. Le forensic s'intègre dans l'IR à trois niveaux : il alimente les décisions de confinement (quels systèmes isoler, quels comptes désactiver — basé sur l'étendue de la compromission révélée par l'investigation), il produit les IoC pour la détection à l'échelle du parc (les hash, domaines C2, et artefacts de persistance identifiés sont injectés dans le SIEM/EDR pour scanner toutes les machines), et il alimente le rapport final et le RETEX (la timeline complète, le mapping ATT&CK, et les causes racines identifiées par le forensic structurent le RETEX de l'incident).

---

### Chapitre 29 — Forensic automation et scripting

#### 29.1 Pourquoi l'automatisation est devenue indispensable

La réalité du forensic opérationnel en 2025-2026 : les volumes de données sont massifs (des téraoctets d'images disque, des millions d'événements dans les logs), les parcs à investiguer sont étendus (vérifier 800 postes pour la présence d'un IoC), et les délais sont serrés. L'analyste qui fait tout manuellement est submergé. L'automatisation ne remplace pas le raisonnement analytique (Ch.11) — elle libère du temps pour le raisonnement en automatisant les tâches répétitives.

#### 29.2 Python pour le forensic

Python est le langage de scripting dominant en forensic. Les librairies essentielles : **python-evtx** (parsing des Event Logs Windows), **python-registry** (parsing du registre Windows), **pefile** (analyse de binaires PE), **yara-python** (matching de règles YARA), **volatility3** comme librairie Python (analyse de dumps mémoire programmable), **pandas** (manipulation de données tabulaires — essentiel pour travailler avec les CSV produits par les outils Zimmerman), et **sqlite3** (accès aux bases de données SQLite des navigateurs, de Teams, de WhatsApp, etc.).

Exemple concret : un script Python qui parse le Prefetch de 800 postes collectés par Velociraptor, filtre les exécutions de `rclone.exe`, `psexec.exe`, et `mimikatz.exe`, et produit un CSV des machines sur lesquelles ces outils ont été exécutés — en 30 secondes au lieu de 30 heures d'analyse manuelle.

#### 29.3 PowerShell pour la collecte et l'analyse Windows

PowerShell est l'outil natif pour la collecte et l'analyse sur Windows. `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624}` interroge les Event Logs. `Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'` lit les clés de registre. PowerShell Remoting (`Invoke-Command -ComputerName`) permet la collecte à distance sur un parc entier.

#### 29.4 Velociraptor VQL et KAPE custom

**Velociraptor** utilise le VQL (Velociraptor Query Language) pour définir des collectes et des hunts personnalisées. Un hunt Velociraptor peut scanner 1 000 machines en quelques minutes pour la présence d'un IoC spécifique (hash de fichier, nom de processus, clé de registre). **KAPE** permet la création de targets et modules custom — l'analyste peut définir exactement quels artefacts collecter et comment les parser, adapté à son environnement.

---
