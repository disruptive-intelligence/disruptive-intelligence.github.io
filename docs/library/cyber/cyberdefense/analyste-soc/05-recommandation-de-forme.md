---
title: Recommandation de forme
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

Vu ton cours, je garderais ce chapitre :

- **plus court** que les gros chapitres d’investigation ;
- assez **dense pour être utile** ;
- avec un style très **opérationnel** ;
- idéalement **8 à 10 pages max** si tu rédiges de façon développée.

Je te conseille cette structure finale :

- **11.1 Pourquoi ce vocabulaire compte pour le SOC**
- **11.2 CVE — identifier précisément la vulnérabilité**
- **11.3 CWE — comprendre la faiblesse sous-jacente**
- **11.4 CVSS — mesurer la sévérité technique**
- **11.5 EPSS — estimer la probabilité d’exploitation**
- **11.6 KEV — savoir si la menace est déjà réelle**
- **11.7 Bien lire l’ensemble : ce que chaque référentiel apporte**
- **11.8 Ce que le SOC doit en faire concrètement**
- **11.9 Fil rouge — mise en situation SOC**
- **11.10 Transition vers le chapitre suivant**

---

## Chapitre 12 - Qualification, catégorisation et évaluation de gravité


## 12.1 — Vulnérabilité exploitée

distinguer sévérité CVSS et gravité de l'incident

Lorsqu'un incident trouve son origine dans l'exploitation d'une vulnérabilité identifiée par une CVE, l'analyste SOC ne doit pas confondre deux choses fondamentalement différentes : la **sévérité de la vulnérabilité** (mesurée par CVSS) et la **gravité de l'incident** (évaluée par les critères IR de l'organisation). Les deux se nourrissent mutuellement, mais elles ne répondent pas à la même question.

La **gravité de l'incident** répond à : « à quel point l'incident est grave pour l'organisation ici et maintenant ? ». Elle est évaluée selon les critères IR propres : étendue de la compromission, privilèges obtenus par l'attaquant, propagation observée ou potentielle, exfiltration confirmée ou suspectée, impact métier (production arrêtée ? données critiques touchées ?), criticité des systèmes impactés, et obligations réglementaires (notification CNIL 72h, NIS2). C'est cette gravité qui détermine le niveau P1/P2/P3/P4 et déclenche les escalades.

La **sévérité CVSS de la vulnérabilité** répond à : « à quel point cette vulnérabilité est sévère dans notre environnement ? ». C'est une information qui éclaire la qualification, mais qui ne la remplace pas.

### 12.2 Le problème du score CVSS Base brut

Une CVE publiée par un éditeur ou le NVD est accompagnée d'un score CVSS Base (v3.1 ou v4.0). Ce score est **générique** — il décrit la vulnérabilité dans l'absolu, sans tenir compte du contexte de l'organisation. Un CVSS Base de 9.8 sur un service exposé sur Internet avec un exploit public et des données de santé derrière est effectivement critique. Le même CVSS 9.8 sur un service isolé dans un VLAN de test sans données et avec un WAF devant ne l'est pas du tout.

Le problème opérationnel est que beaucoup d'organisations traitent le score Base comme un score final : le scanner remonte 150 « critiques » par semaine, les équipes sont saturées, et les vraies urgences se noient dans le bruit. La re-qualification contextuelle est ce qui rend le score exploitable.

### 12.3 CVSS v4.0 : la structure qui permet la contextualisation

CVSS v4.0 (FIRST, publié fin 2023, supporté par le NVD) apporte une structure de scoring en quatre groupes de métriques qui améliore significativement la contextualisation par rapport à v3.1 :

Le groupe **Base** (la sévérité intrinsèque de la vulnérabilité — vecteur d'attaque, complexité, privilèges requis, interaction utilisateur, impacts CIA — ce qui existait déjà en v3.1). Le groupe **Threat** (remplace le « Temporal » de v3.1 — intègre l'état d'exploitation actif via Exploit Maturity : Unreported, PoC, Attacked — est-ce que cette vulnérabilité est exploitée in-the-wild ? si oui, la priorité monte). Le groupe **Environmental** (existait en v3.1 mais est mieux structuré en v4 — les Modified Base Metrics permettent de refléter les contrôles compensatoires et l'exposition réelle : Modified Attack Vector si le service n'est pas exposé sur Internet, Modified Privileges Required si un contrôle d'accès compense, les exigences de sécurité CIA adaptées à la criticité métier de l'actif). Le groupe **Supplemental** (nouveau en v4 — Safety, Automatable, Recovery, Value Density, Provider Urgency — des métriques qui enrichissent la contextualisation sans modifier le score numérique, mais en informant la décision opérationnelle).

CVSS v4 produit des scores différenciés selon le niveau de contextualisation appliqué : **CVSS-B** (Base seul — le score générique), **CVSS-BT** (Base + Threat — intègre l'état d'exploitation), **CVSS-BE** (Base + Environmental — intègre le contexte de l'organisation), **CVSS-BTE** (Base + Threat + Environmental — le score le plus contextualisé). Cette nomenclature force à expliciter quel niveau de contextualisation est appliqué — un progrès par rapport au v3.1 où la distinction était souvent floue.

### 12.4 Le workflow de rescoring contextuel

En pratique, quand un incident est déclenché par l'exploitation d'une CVE connue :

(1) **Documenter le score externe** : le score CVSS-B publié par l'éditeur ou le NVD est la référence de départ. Il est conservé tel quel dans la fiche d'incident pour traçabilité.

(2) **Appliquer les métriques Threat** : l'exploit est-il public (PoC sur GitHub, Exploit-DB) ? Est-il observé in-the-wild (KEV — Known Exploited Vulnerabilities de la CISA, bulletins CTI, signalements internes) ? → Exploit Maturity = Attacked si exploitation confirmée. Le score passe de CVSS-B à CVSS-BT.

(3) **Appliquer les métriques Environmental** : le service vulnérable est-il exposé sur Internet ou uniquement en interne ? (Modified Attack Vector). Des contrôles compensatoires sont-ils en place — WAF, segmentation, MFA, EDR ? (Modified Privileges Required, Modified User Interaction). Les données derrière le service sont-elles critiques pour le métier ? (Security Requirements CIA : High/Medium/Low). → Le score passe de CVSS-BT à CVSS-BTE.

(4) **Comparer les trois lectures** : le score externe (ce que dit l'éditeur), le score contextuel interne (ce que dit la réalité de l'environnement), et la gravité IR de l'incident (ce que dit l'impact opérationnel). Les trois sont documentés dans la fiche d'incident.

### 12.5 Ce que le rescoring contextuel NE fait PAS

Le rescoring contextuel CVSS ne remplace pas la qualification de gravité IR (P1/P2/P3/P4), qui reste une évaluation business et opérationnelle. Le FAQ FIRST rappelle que le score numérique seul ne porte pas tout le contexte — les métriques Environmental concernent le système vulnérable dans son environnement, pas la vulnérabilité « dans l'absolu ».

Un incident peut être P1 (gravité maximale) même si la CVE exploitée a un CVSS-BTE de 6.5 — parce que l'attaquant a pivoté vers des systèmes critiques après l'exploitation initiale. Inversement, un incident peut être P3 même si la CVE a un CVSS-B de 9.8 — parce que l'exploitation a été détectée et contenue immédiatement, sur un système non critique, sans propagation.

### 12.6 Ce que le rescoring contextuel SERT à faire

Il sert à **éclairer les décisions** pendant et après l'incident : priorisation du patching (quelle instance de la même vulnérabilité patcher en premier — celle avec le CVSS-BTE le plus élevé), extension du hunting (chercher l'exploitation de la même CVE sur d'autres systèmes — en priorisant les systèmes avec le CVSS-BE le plus élevé), périmètre de remédiation (les systèmes où la vulnérabilité est fortement compensée peuvent attendre ; ceux où elle est pleinement exposée sont P0), et plan de durcissement post-incident (le rescoring du backlog de vulnérabilités révèle les autres expositions critiques dans l'environnement réel).

En résumé : trois informations distinctes, trois usages distincts, documentées ensemble dans la fiche d'incident.

| Information | Question | Usage |
|-------------|----------|-------|
| Score CVSS-B externe (éditeur/NVD) | La vulnérabilité est-elle sévère en général ? | Référence, communication, comparaison |
| Score CVSS-BTE contextuel interne | La vulnérabilité est-elle sévère CHEZ NOUS ? | Priorisation patching, hunting, remédiation |
| Gravité IR de l'incident (P1-P4) | L'incident est-il grave pour l'organisation ? | Escalade, mobilisation, SLA, communication de crise |

---

## Chapitre 13 — Investigation endpoint

*Le chapitre le plus dense de la partie — investigation complète sur un endpoint compromis, pas à pas, avec les requêtes réelles et les résultats.*

Le workflow d'investigation endpoint appliqué au fil rouge FALCONWATCH.

**Étape 1 — Lecture de l'alerte EDR :** l'alerte CrowdStrike montre le process tree complet. Karim identifie la chaîne `WINWORD.EXE → cmd.exe → certutil.exe → rundll32.exe`. Chaque processus est examiné : PID, arguments de ligne de commande, hash, connexions réseau, fichiers créés.

**Étape 2 — Reconstitution du process tree complet dans le SIEM :** requête SPL sur les logs Sysmon Event 1 pour WKS-PROD-112 sur les dernières 24h :

```
index=sysmon host="WKS-PROD-112" EventCode=1 
| eval parent=ParentImage." (PID:".ParentProcessId.")"
| eval child=Image." (PID:".ProcessId.")"
| table _time parent child CommandLine User
| sort _time
```

Le résultat montre la séquence complète avec les timestamps — et révèle un processus supplémentaire que l'alerte EDR n'avait pas mis en avant : après le rundll32, un `cmd.exe → whoami /all` puis un `cmd.exe → net group "Domain Admins" /domain` — reconnaissance post-exploitation.

**Étape 3 — Analyse des connexions réseau du processus malveillant :** requête Sysmon Event 3 :

```
index=sysmon host="WKS-PROD-112" EventCode=3 
  ProcessId=9284
| table _time DestinationIp DestinationPort Protocol
```

Résultat : connexion HTTPS vers `185.xx.xx.xx:443` toutes les 45 secondes — beaconing C2 confirmé.

**Étape 4 — Scope assessment :** la compromission est-elle limitée à ce poste ? Requête EDR pour le hash de lib.dll sur tout le parc Norexia :

```
index=sysmon EventCode=7 SHA256="a7f3e2d8..." 
| stats count by host
```

Résultat : 0 match sur les autres postes. Requête firewall pour les connexions vers le C2 :

```
index=firewall dest_ip="185.xx.xx.xx" 
| stats count by src_ip
| sort -count
```

Résultat : 2 IP sources — `10.0.5.112` (WKS-PROD-112, connu) et `10.0.3.45` (WKS-IT-045, **nouveau** — mouvement latéral découvert).

---


## Chapitre 14— Investigation identité et Active Directory

Investigation des compromissions d'identité appliquée au fil rouge.

**Détection du mouvement latéral :** Event ID 4624 type 3 sur WKS-IT-045 depuis `10.0.5.112` (WKS-PROD-112) avec le compte `marc.dubois` :

```
index=windows host="WKS-IT-045" EventCode=4624 LogonType=3 
| table _time TargetUserName IpAddress LogonType AuthenticationPackageName
```

Suivi immédiatement d'un Event ID 7045 (service PSEXESVC installé) — confirmation que PsExec a été utilisé pour le mouvement latéral.

**Détection du Kerberoasting :** Event ID 4769 sur DC01 avec encryption type 0x17 depuis WKS-PROD-112 :

```
index=windows host="DC01" EventCode=4769 TicketEncryptionType=0x17 
| stats count values(ServiceName) by IpAddress
| where count > 5
```

Résultat : 8 comptes de service ciblés, dont `svc-scada` (compte avec accès aux systèmes de supervision industrielle). L'attaquant a demandé des tickets Kerberos RC4 pour craquer les mots de passe offline. **C'est le moment pivot** : si `svc-scada` est cracké, l'attaquant a accès au réseau OT. Escalade immédiate.

**Vérification des modifications AD :** Event ID 5136 (modifications d'objets LDAP) et 4728/4732 (ajouts à des groupes) sur le DC dans la fenêtre temporelle de l'incident — aucune modification détectée. L'attaquant n'a pas encore utilisé le compte svc-scada — il est encore en phase de cracking offline.

---


## Chapitre 15 — Investigation réseau

Les logs réseau complètent l'investigation endpoint et identité.

**Analyse du beaconing C2 :** les logs proxy montrent les connexions HTTPS vers `185.xx.xx.xx` avec un pattern temporel régulier (intervalle de 45 secondes ± 3 secondes). Le user-agent est `Mozilla/5.0 (Windows NT 10.0; Win64; x64) NorexiaUpdate/1.0` — un user-agent custom qui imite un navigateur légitime mais avec un suffixe inhabituel.

**Recherche d'exfiltration :** les logs proxy montrent qu'à J+1 (dimanche), le poste WKS-IT-045 (le second poste compromis — poste d'un admin IT) a lancé `rclone.exe` qui a uploadé 12 Go de données vers un bucket S3 externe. Le SRUM (System Resource Usage Monitor) sur WKS-IT-045 confirme que `rclone.exe` a consommé 12.3 Go de bande passante réseau en 4 heures.

**Reconstruction de la timeline réseau :** corrélation firewall + proxy + DNS pour reconstituer les communications de l'attaquant heure par heure. Les résolutions DNS montrent que `update-norexia[.]xyz` a été résolu pour la première fois samedi à 08h12 UTC (le moment du phishing initial) — 23 heures avant la détection par l'EDR lundi à 07h42.

---


## Chapitre 16 — Investigation cloud et SaaS

Ce chapitre développe l'investigation dans les environnements M365/Azure et AWS avec des requêtes concrètes. Scénario BEC complet (phishing AitM → token replay → forwarding rule → exfiltration SharePoint → phishing interne) avec les requêtes KQL Sentinel à chaque étape. Scénario AWS (access keys compromises → CloudTrail analysis → modification de security groups → lancement d'instances). Le défi de la corrélation cloud ↔ on-premise quand l'attaquant pivote entre les deux mondes.

---


## Chapitre 17 — Construction de timeline multi-sources

La timeline multi-sources fusionne les événements de toutes les sources (EDR + SIEM + proxy + firewall + AD + email gateway + cloud) en une séquence chronologique unique. C'est le livrable le plus puissant de l'investigation — c'est aussi le plus exigeant à construire.

Les étapes de construction : normalisation des timestamps en UTC, identification des sources pertinentes pour chaque phase de l'attaque, extraction des événements clés par requête SIEM, fusion dans un format tabulaire (heure UTC | source | machine | utilisateur | action | détail), et analyse de la séquence (patterns, corrélations, lacunes). Les lacunes sont aussi informatives que les événements — un trou de 6 heures entre le mouvement latéral et l'exfiltration pose la question : l'attaquant était-il inactif, ou les logs manquent-ils ?

Fil rouge : Karim construit la timeline FALCONWATCH de 48 heures, qui révèle que l'attaquant a agi en 4 phases distinctes : samedi 08h-10h (phishing + infection initiale), samedi 22h-01h (reconnaissance + mouvement latéral), dimanche 06h-10h (Kerberoasting + staging des données R&D), lundi 04h-07h (suppression des shadow copies sur 3 machines + déploiement du binaire ransomware — non exécuté avant la détection EDR à 07h42).

---


## Chapitre 18 — Pièges, faux positifs et erreurs d'investigation

Les erreurs les plus fréquentes et comment les éviter, illustrées par des cas concrets. Timezones (le piège n°1 — un log proxy en heure locale Paris et un log firewall en UTC créent un décalage fantôme de 1-2h). NAT/proxy/VPN (l'IP source dans les logs firewall peut être le proxy, pas le poste — toujours croiser avec les logs d'authentification pour identifier la machine réelle). Comptes de service (bruit massif, logons réseau en continu, horaires atypiques — les baseliner mais surveiller tout changement : un compte de service qui fait du Kerberoasting, c'est anormal). DHCP et rotation d'IP (l'IP 10.0.5.112 était-elle attribuée à WKS-PROD-112 au moment de l'alerte ? vérifier les baux DHCP). Multi-sessions RDP (sur un serveur RDS, plusieurs utilisateurs partagent la même IP — le session ID est nécessaire pour identifier l'auteur). Scanners de vulnérabilité (Nessus, Qualys — exclure les IP sources dans les règles IDS/IPS, documenter l'exclusion). Le biais de confirmation (l'analyste qui pense « phishing » arrête de chercher des alternatives — peut-être que le document était légitime et l'alerte est un FP sur une macro inoffensive). Et le benign true positive (l'admin IT qui utilise PsExec légitime — la détection est correcte, l'action est bénigne, c'est un BTP pas un FP).

---
