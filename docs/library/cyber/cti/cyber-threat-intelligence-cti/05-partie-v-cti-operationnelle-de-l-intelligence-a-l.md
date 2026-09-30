---
title: 'Partie V — CTI opérationnelle : de L''intelligence à L''action'
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - index.md
---

*Comment le renseignement CTI se traduit concrètement en détections, en hunts, en réponse à incident, et en décisions — y compris le chapitre dédié à la vulnerability intelligence.*

---


## Chapitre 20 — CTI-to-Detection

transformer le renseignement en règles

### 20.1 Le workflow complet

Le processus CTI-to-Detection est le mécanisme qui transforme le renseignement en capacité de détection opérationnelle. Il suit une séquence structurée.

**Étape 1 — Identification du TTP pertinent :** la CTI identifie un TTP utilisé par un acteur qui représente une menace pour l'organisation. Dans MERIDIAN : UNC-VOLT utilise T1574.001 (DLL Search Order Hijacking) avec une procédure spécifique — placement d'une DLL malveillante dans le répertoire d'installation de l'application de supervision SCADA.

**Étape 2 — Vérification de la couverture actuelle :** l'analyste CTI vérifie avec le SOC si une règle de détection existe déjà pour ce TTP et cette procédure spécifique. Si la réponse est « oui, nous avons une règle Sigma pour T1574.001 », la question suivante est : la règle couvre-t-elle la procédure spécifique de UNC-VOLT (DLL dans le répertoire de l'application SCADA, pas juste le DLL hijacking générique) ?

**Étape 3 — Rédaction de la règle :** si la couverture est insuffisante, l'analyste CTI rédige une règle de détection en **Sigma** (format pivot universel) qui cible la procédure spécifique. Sigma est ensuite converti en SPL (Splunk), KQL (Microsoft Sentinel), EQL (Elastic), ou le langage de requête du SIEM utilisé par l'organisation.

**Étape 4 — Test et tuning :** la règle est testée sur les logs historiques (rétro-hunt) pour vérifier les faux positifs et la couverture. Si le volume de FP est trop élevé, la règle est affinée (ajout de conditions d'exclusion, restriction à un périmètre de machines).

**Étape 5 — Déploiement et monitoring :** la règle est déployée en production, les alertes sont monitorées, et les FP résiduels sont documentés.

**Étape 6 — Feedback :** le SOC reporte à la CTI les résultats (vrais positifs détectés, FP, gaps de logs identifiés). Ce feedback alimente le cycle suivant.

### 20.2 Le gap analysis

Le gap analysis est l'exercice le plus productif de la CTI-to-Detection. L'analyste CTI liste les TTP des acteurs pertinents pour l'organisation (à partir des profils d'acteurs et des PIR), les croise avec la couverture de détection actuelle (quelles techniques sont couvertes par des règles SIEM, EDR, ou des hunts réguliers), et identifie les gaps (techniques utilisées par les acteurs pertinents mais non détectées). Les gaps sont priorisés par risque (probabilité que l'acteur utilise cette technique contre l'organisation × impact si non détecté) et le SOC les comble progressivement. ATT&CK Navigator est l'outil qui visualise cette analyse : la matrice colorée en vert (couvert), orange (partiellement couvert), et rouge (non couvert) est un livrable immédiatement actionnable.

---


## Chapitre 21 — Vulnerability Intelligence

### 21.1 Pourquoi la vuln intel est un pilier CTI

L'exploitation de vulnérabilités est le 2ème vecteur d'accès initial derrière le phishing — et le 1er pour les acteurs étatiques sophistiqués (Volt Typhoon, APT40, Sandworm). Savoir quelles vulnérabilités sont activement exploitées in the wild, par quels acteurs, contre quel profil de cible, et avec quelle urgence, est du renseignement critique qui oriente directement la priorisation du patching et la posture défensive.

Le problème du volume : des dizaines de milliers de CVE sont publiées chaque année (plus de 28 000 en 2023, plus de 30 000 en 2024). La grande majorité ne sont jamais exploitées. La CTI filtre le bruit pour concentrer l'attention sur les vulnérabilités qui comptent.

### 21.2 Le flux de vulnerability intelligence

**Publication CVE :** une vulnérabilité est identifiée et publiée (NVD, éditeur, chercheur).

**Évaluation de criticité technique :** le CVSS (Common Vulnerability Scoring System) mesure la sévérité technique (vecteur d'attaque, complexité, impact). Mais le CVSS seul est insuffisant pour la priorisation : un CVSS de 9.8 sur une technologie que l'organisation n'utilise pas a un risque réel de zéro.

**Détection d'exploitation in the wild :** c'est la donnée la plus critique. Le **CISA KEV** (Known Exploited Vulnerabilities catalog) est le catalogue de référence des vulnérabilités confirmées exploitées activement — mis à jour en continu, avec des dates de correction obligatoires pour les agences fédérales US (référence de fait mondiale). L'**EPSS** (Exploit Prediction Scoring System) calcule la probabilité qu'une CVE soit exploitée dans les 30 prochains jours, basée sur des signaux multiples. Les **sources communautaires** complètent : tweets de chercheurs signalant une exploitation, GreyNoise (détection de mass scanning exploitant une CVE), Shadowserver (monitoring d'Internet à grande échelle).

**Corrélation avec les acteurs :** la donnée de plus haute valeur — quelle vulnérabilité est exploitée par quel groupe. « CVE-2024-21887 (Ivanti Connect Secure) est activement exploitée par au moins 3 clusters d'activité incluant Volt Typhoon et UNC-VOLT » → cette corrélation est du renseignement qui oriente directement le patching prioritaire ET les détections post-exploitation.

**Évaluation de l'exposition :** la CTI apporte le contexte de menace (qui exploite quoi), le vuln management apporte le contexte interne (quels systèmes sont affectés, quels patchs sont disponibles). L'intersection produit une priorisation basée sur le risque réel : vulnérabilité exploitée ITW par un acteur qui cible notre secteur + nous avons les systèmes affectés exposés sur Internet = priorité critique immédiate.

**Production :** flash alert « CVE-2024-21887 activement exploitée — nos appliances Ivanti sont exposées → patch immédiat ou mitigation (disable SAML) » — livré au SOC, au vuln management, et au RSSI dans les heures suivant la détection d'exploitation ITW.

### 21.3 Fil rouge — MERIDIAN : la piste Ivanti

> **🔎 MERIDIAN — Épisode 7**
>
> L'analyse des artefacts IR confirme que UNC-VOLT a exploité CVE-2024-21887 (Ivanti Connect Secure, RCE via commande d'injection dans le composant SAML) comme vecteur d'accès initial chez EDE. Élise vérifie le CISA KEV : la CVE est listée depuis le 10 janvier 2024. L'EPSS au moment de l'incident indiquait une probabilité d'exploitation de 97 %. Mandiant a publié un rapport liant l'exploitation de cette CVE à des clusters étatiques chinois (UNC5221) — mais aussi à des acteurs indépendants opportunistes.
>
> La corrélation est riche mais ambiguë : l'exploitation d'Ivanti est un indice faible pour l'attribution (trop d'acteurs l'exploitent — c'est une technique « commodity »). En revanche, c'est un renseignement critique pour la défense d'EDE : toutes les appliances Ivanti doivent être patchées, et des détections post-exploitation spécifiques doivent être déployées (recherche de webshells LIGHTWIRE/WIREFIRE dans les répertoires Ivanti).

---


## Chapitre 22 — CTI et Threat Hunting

Le threat hunting est la traduction opérationnelle des hypothèses CTI. Le processus : la CTI formule une hypothèse basée sur le renseignement (« UNC-VOLT utilise le DLL sideloading sur les postes d'ingénieurs OT — si nos postes d'ingénieurs OT sont compromis, on devrait trouver des DLL non signées dans les répertoires d'applications de supervision »). Le hunter traduit l'hypothèse en requête technique (recherche via Velociraptor ou le SIEM de DLL non signées dans des chemins spécifiques, corrélation avec les processus chargés). Les résultats alimentent le cycle : si le hunt est positif (compromission découverte) → escalade IR + mise à jour du profil d'acteur + nouvelles hypothèses. Si le hunt est négatif → renforcement de la confiance dans l'éradication + enrichissement de la baseline (les « normaux » découverts pendant le hunt sont documentés pour réduire les futurs FP).

La boucle vertueuse **CTI → Hunt → IR → CTI** est le mécanisme le plus mature de la sécurité opérationnelle : la CTI oriente le hunting, le hunting découvre des compromissions, l'IR investigue, et les artefacts IR enrichissent la CTI — qui formule de nouvelles hypothèses de hunting. Renvoi vers le cours SOC pour les techniques de hunting détaillées.

---


## Chapitre 23 — CTI et Incident Response

Le flux bidirectionnel CTI ↔ IR est le mécanisme qui rend les deux disciplines plus efficaces ensemble qu'isolément.

**En amont de l'incident :** la CTI fournit le contexte de menace que l'IR utilise pour préparer ses playbooks. « Les acteurs qui ciblent les opérateurs d'énergie utilisent typiquement T1190 (exploitation d'appliances VPN), T1574 (DLL hijacking), et T1003.006 (DCSync) — les playbooks IR doivent couvrir ces scénarios. » La CTI identifie aussi les acteurs les plus probables et leurs motivations — ce qui aide l'IR lead à cadrer la réponse (un acteur de pré-positionnement étatique nécessite une réponse différente d'un affilié RaaS).

**Pendant l'incident :** la CTI contextualise les observations de l'IR en temps réel. « Les TTP observées correspondent au cluster UNC-VOLT / profil Sandworm — anticiper les mécanismes de persistance suivants : DLL sideloading dans les répertoires d'applications, modification des ACL AD, et potentiel wiper pré-positionné. » Cette anticipation oriente l'investigation et évite les mauvaises surprises.

**Après l'incident :** l'IR fournit à la CTI les artefacts, les TTP observées, et les IoC. La CTI les intègre dans le profil d'acteur, met à jour les IoC dans le TIP, produit un rapport de campagne, et enrichit la base de connaissances pour les futurs incidents. Renvoi vers le cours IR de la bibliothèque pour le processus IR complet.

---


## Chapitre 24 — CTI pour le RSSI et la direction

### 24.1 Le briefing stratégique

Le RSSI et la direction ont besoin de renseignement formulé en termes de risque business, pas en termes de techniques ATT&CK. Le briefing stratégique répond aux questions : quelles menaces sont pertinentes pour notre secteur et notre géographie ? Quelle est l'évolution du risque par rapport au trimestre précédent ? Sommes-nous plus ou moins exposés que nos pairs ? Quels investissements sont prioritaires ? Le format est court (2-3 pages ou 15 minutes de présentation orale), visuel (graphiques de tendance, cartes de chaleur), et focalisé sur les implications business (perte financière potentielle, risque réglementaire, risque réputationnel).

### 24.2 L'évaluation de risque basée sur la menace (threat-informed)

L'approche classique de l'évaluation de risque (menace × vulnérabilité × impact) est souvent déconnectée de la réalité de la menace : les menaces sont listées de manière générique (« ransomware », « espionnage ») sans corrélation avec les acteurs réels qui ciblent l'organisation. La CTI enrichit l'évaluation de risque avec des menaces concrètes et contextualisées : « le cluster UNC-VOLT cible activement les opérateurs d'énergie européens avec les TTP X, Y, Z — notre exposition à ces TTP est de X % (gap analysis) — le risque est élevé et les mesures prioritaires sont A, B, C ». Renvoi vers le cours GRC pour la méthodologie d'analyse de risques.

---


## Chapitre 25 — Partage de renseignement et communautés

Le partage est un multiplicateur de force : un renseignement partagé avec 10 pairs protège 11 organisations. Les ISACs sectoriels (EE-ISAC pour l'énergie, FS-ISAC pour la finance, H-ISAC pour la santé) sont les structures formelles de partage sectoriel. Les cercles de confiance (FIRST, TF-CSIRT, InterCERT France, groupes de travail ANSSI) permettent les échanges non publics entre pairs. Les plateformes techniques (instances MISP communautaires, feeds TAXII partagés) automatisent le partage d'IoC et de TTP.

Les **règles du partage** : le TLP encadre la diffusion, la Chatham House Rule protège les discussions orales (on peut rapporter le contenu mais pas identifier la source), et la réciprocité est le contrat social (qui prend sans donner finit par être exclu). Les **freins** au partage : la peur de révéler une compromission (paradoxe — partager protège les pairs, qui partageront à leur tour), les contraintes juridiques (RGPD sur les données personnelles dans les IoC, clauses de confidentialité des contrats clients), et la concurrence (entre entreprises du même secteur — les ISACs sont conçus pour surmonter ce frein via la confiance institutionnelle).

### 25.1 Fil rouge — MERIDIAN : le partage ISAC

> **🔎 MERIDIAN — Épisode 8**
>
> Élise partage les IoC et les TTP de UNC-VOLT avec l'EE-ISAC (European Energy ISAC) via MISP, en TLP:AMBER. En retour, elle reçoit des informations de 3 autres opérateurs d'énergie européens qui ont observé des activités similaires (mêmes patterns de beaconing, mêmes techniques de persistence, ciblage d'appliances Ivanti) dans les 6 derniers mois. L'un d'entre eux a identifié un IoC supplémentaire (un domaine C2 non découvert dans l'incident EDE) qui, analysé via passive DNS, révèle un cluster d'infrastructure plus large. Ce partage est le tournant de l'investigation : la victimologie passe de 1 victime (EDE) à 4 opérateurs d'énergie européens — un programme de ciblage systématique, cohérent avec un acteur étatique.

---
