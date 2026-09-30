---
title: Partie VII — SOC avancé ET maturité
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

---


## Chapitre 33 — Automatisation SOC et SOAR

Ce qui doit être automatisé : l'enrichissement des alertes (hash → VirusTotal, IP → réputation/géo, domaine → Whois/PDNS, user → CMDB/criticité — ces actions sont répétitives, à faible valeur analytique, et réalisées des dizaines de fois par shift), la création de tickets (chaque alerte génère automatiquement un ticket avec les informations de contexte), la notification (les parties prenantes sont alertées automatiquement selon la sévérité), et les actions de confinement à faible risque (blocage d'IoC confirmé au proxy, quarantaine de fichier malveillant).

Ce qui ne doit PAS être automatisé : les décisions de confinement à fort impact (isolation réseau d'un segment de production, reset du mot de passe du CEO — un humain décide), les conclusions d'investigation (la qualification VP/FP/BTP — un humain évalue), et l'escalade (un humain décide quand et comment escalader).

Le piège de la sur-automatisation : automatiser sans comprendre crée des incidents (un playbook qui isole automatiquement tout endpoint avec un score de risque > 80 peut isoler le poste du RSSI parce qu'un scan de vulnérabilité légitime a fait monter le score).

---


## Chapitre 34 — Vulnerability Operations

le SOC et la réduction proactive du risque

*Ce chapitre couvre l'extension du périmètre SOC vers la gestion proactive des vulnérabilités — une tendance structurelle des SOC modernes.*

### 34.1 Le VOC comme extension naturelle du SOC

Traditionnellement, le vulnerability management (scan, priorisation, patching) est un processus séparé du SOC. Mais la convergence est en cours : les vulnérabilités activement exploitées in the wild sont du renseignement de menace (CTI), et la réponse à ces vulnérabilités est une action de sécurité opérationnelle (SOC). Le VOC (Vulnerability Operations Center, ou la fonction « vuln ops » intégrée au SOC) fait le pont.

### 34.2 Priorisation basée sur le risque réel

Le CVSS mesure la sévérité technique d'une vulnérabilité — pas le risque réel pour l'organisation. Un CVSS de 9.8 sur une technologie que l'organisation n'utilise pas a un risque réel de zéro. Un CVSS de 7.5 sur le VPN Ivanti exposé sur Internet et activement exploité par Volt Typhoon a un risque réel critique.

La priorisation basée sur le risque réel croise trois dimensions. L'**exploitabilité** : la vulnérabilité est-elle exploitée in the wild ? Le **CISA KEV** (Known Exploited Vulnerabilities catalog) est la référence — si la CVE est dans le KEV, elle est exploitée. L'**EPSS** (Exploit Prediction Scoring System) calcule la probabilité d'exploitation dans les 30 jours. L'**exposition** : l'organisation utilise-t-elle la technologie affectée ? L'asset est-il exposé sur Internet ? Est-il critique (OIV, serveur de production, DC) ? Le **contexte de menace** (fourni par la CTI) : quelle CVE est exploitée par quel acteur, contre quel profil de cible ? « CVE-2024-21887 exploitée par des clusters étatiques ciblant les opérateurs d'énergie européens » → si vous êtes un opérateur d'énergie européen avec des Ivanti exposés, c'est votre priorité n°1.

### 34.3 L'articulation SOC ↔ vuln management ↔ CTI

La CTI identifie les vulnérabilités exploitées ITW et les corrèle avec les acteurs (cours CTI Ch.21). Le vuln management scanne l'environnement et identifie les assets vulnérables. Le SOC reçoit le croisement des deux (vulnérabilité exploitée ITW × asset exposé dans notre environnement) et agit : flash alert au RSSI et à l'IT, monitoring renforcé des assets exposés (détection des tentatives d'exploitation), et vérification que le patch est déployé dans les délais (le SOC ne patche pas — il vérifie que le patching a eu lieu et alerte si ce n'est pas le cas).

Le VOC n'est pas un remplacement du vulnerability management classique — c'est l'ajout d'une dimension opérationnelle (« cette vulnérabilité est exploitée maintenant, par un acteur qui nous cible, et nos systèmes sont exposés — il faut agir dans les heures, pas dans les semaines ») qui transforme un processus de gestion en un processus de réponse.

---


## Chapitre 35 — Métriques SOC, reporting et maturité

Les métriques qui comptent : **MTTD** (Mean Time to Detect — temps entre l'événement malveillant et sa détection par le SOC ; cible : < 1h pour les critiques — dans FALCONWATCH, le MTTD est de ~23h car l'infection initiale samedi 08h12 n'a été détectée que lundi 07h42), **MTTR** (Mean Time to Respond — temps entre la détection et le confinement ; cible : < 4h — dans FALCONWATCH, le MTTR est de ~45 minutes entre la détection et l'isolation des postes), **taux de FP** (% d'alertes faussement positives ; cible : < 15 % — au-dessus de 30 %, le SOC est en surcharge), **backlog** (alertes en attente de triage ; cible : proche de 0 en fin de shift), **couverture ATT&CK** (% de techniques couvertes par des règles testées ; amélioration continue via le purple team), et **taux de détection SOC** (% d'incidents détectés par le SOC vs découverts par d'autres moyens — utilisateur, tiers, médias ; cible : > 80 %).

Les niveaux de maturité : **Niveau 1 (Réactif)** — le SOC traite les alertes mais ne crée pas de détections custom et ne fait pas de hunting. **Niveau 2 (Proactif)** — le SOC a un detection engineer qui crée des règles basées sur la CTI, et fait du hunting régulier (hebdomadaire). **Niveau 3 (Adaptatif)** — purple team régulier, validation continue des détections, gap analysis CTI-driven, automatisation SOAR mature. **Niveau 4 (Intelligence-driven)** — la CTI guide toute la stratégie de détection, le hunting est continu, les détections sont validées par purple team, et les métriques d'impact (incidents prévenus) sont mesurées.

---


## Chapitre 36 — Le SOC en 2026 : tendances et évolutions

Les tendances réelles (pas le marketing). Le **SOC cloud-native** : les logs sont dans le cloud, le SIEM est dans le cloud, les endpoints sont gérés via le cloud — le SOC on-premise disparaît progressivement. L'**IA comme assistant** : les LLM pour résumer les alertes, suggérer des requêtes, aider à la rédaction de tickets — utile et productif ; les LLM pour qualifier automatiquement les alertes — risqué (les hallucinations en sécurité ont des conséquences) ; les modèles ML pour le scoring et la priorisation — mature et productif (risk-based alerting de Splunk ES, fusion rules de Sentinel). La **convergence SOC/CTI** : l'analyste SOC de 2026 consomme du renseignement CTI quotidiennement — les profils d'acteurs, les TTP, et les gap analyses sont intégrés dans son workflow. L'**extension du périmètre** : OT/IoT (les systèmes industriels sont maintenant surveillés par le SOC), cloud multi-provider, SaaS, identité — le SOC ne surveille plus seulement les endpoints et le réseau, il surveille tout.

---
