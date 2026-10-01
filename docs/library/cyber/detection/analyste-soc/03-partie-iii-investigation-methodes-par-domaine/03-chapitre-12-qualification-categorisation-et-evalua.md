---
title: Chapitre 12 - Qualification, catégorisation et évaluation de gravité
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

## 12.1 — Vulnérabilité exploitée

distinguer sévérité CVSS et gravité de l'incident

Lorsqu'un incident trouve son origine dans l'exploitation d'une vulnérabilité identifiée par une CVE, l'analyste SOC ne doit pas confondre deux choses fondamentalement différentes : la **sévérité de la vulnérabilité** (mesurée par CVSS) et la **gravité de l'incident** (évaluée par les critères IR de l'organisation). Les deux se nourrissent mutuellement, mais elles ne répondent pas à la même question.

La **gravité de l'incident** répond à : « à quel point l'incident est grave pour l'organisation ici et maintenant ? ». Elle est évaluée selon les critères IR propres : étendue de la compromission, privilèges obtenus par l'attaquant, propagation observée ou potentielle, exfiltration confirmée ou suspectée, impact métier (production arrêtée ? données critiques touchées ?), criticité des systèmes impactés, et obligations réglementaires (notification CNIL 72h, NIS2). C'est cette gravité qui détermine le niveau P1/P2/P3/P4 et déclenche les escalades.

La **sévérité CVSS de la vulnérabilité** répond à : « à quel point cette vulnérabilité est sévère dans notre environnement ? ». C'est une information qui éclaire la qualification, mais qui ne la remplace pas.

## 12.2 Le problème du score CVSS Base brut

Une CVE publiée par un éditeur ou le NVD est accompagnée d'un score CVSS Base (v3.1 ou v4.0). Ce score est **générique** — il décrit la vulnérabilité dans l'absolu, sans tenir compte du contexte de l'organisation. Un CVSS Base de 9.8 sur un service exposé sur Internet avec un exploit public et des données de santé derrière est effectivement critique. Le même CVSS 9.8 sur un service isolé dans un VLAN de test sans données et avec un WAF devant ne l'est pas du tout.

Le problème opérationnel est que beaucoup d'organisations traitent le score Base comme un score final : le scanner remonte 150 « critiques » par semaine, les équipes sont saturées, et les vraies urgences se noient dans le bruit. La re-qualification contextuelle est ce qui rend le score exploitable.

## 12.3 CVSS v4.0 : la structure qui permet la contextualisation

CVSS v4.0 (FIRST, publié fin 2023, supporté par le NVD) apporte une structure de scoring en quatre groupes de métriques qui améliore significativement la contextualisation par rapport à v3.1 :

Le groupe **Base** (la sévérité intrinsèque de la vulnérabilité — vecteur d'attaque, complexité, privilèges requis, interaction utilisateur, impacts CIA — ce qui existait déjà en v3.1). Le groupe **Threat** (remplace le « Temporal » de v3.1 — intègre l'état d'exploitation actif via Exploit Maturity : Unreported, PoC, Attacked — est-ce que cette vulnérabilité est exploitée in-the-wild ? si oui, la priorité monte). Le groupe **Environmental** (existait en v3.1 mais est mieux structuré en v4 — les Modified Base Metrics permettent de refléter les contrôles compensatoires et l'exposition réelle : Modified Attack Vector si le service n'est pas exposé sur Internet, Modified Privileges Required si un contrôle d'accès compense, les exigences de sécurité CIA adaptées à la criticité métier de l'actif). Le groupe **Supplemental** (nouveau en v4 — Safety, Automatable, Recovery, Value Density, Provider Urgency — des métriques qui enrichissent la contextualisation sans modifier le score numérique, mais en informant la décision opérationnelle).

CVSS v4 produit des scores différenciés selon le niveau de contextualisation appliqué : **CVSS-B** (Base seul — le score générique), **CVSS-BT** (Base + Threat — intègre l'état d'exploitation), **CVSS-BE** (Base + Environmental — intègre le contexte de l'organisation), **CVSS-BTE** (Base + Threat + Environmental — le score le plus contextualisé). Cette nomenclature force à expliciter quel niveau de contextualisation est appliqué — un progrès par rapport au v3.1 où la distinction était souvent floue.

## 12.4 Le workflow de rescoring contextuel

En pratique, quand un incident est déclenché par l'exploitation d'une CVE connue :

(1) **Documenter le score externe** : le score CVSS-B publié par l'éditeur ou le NVD est la référence de départ. Il est conservé tel quel dans la fiche d'incident pour traçabilité.

(2) **Appliquer les métriques Threat** : l'exploit est-il public (PoC sur GitHub, Exploit-DB) ? Est-il observé in-the-wild (KEV — Known Exploited Vulnerabilities de la CISA, bulletins CTI, signalements internes) ? → Exploit Maturity = Attacked si exploitation confirmée. Le score passe de CVSS-B à CVSS-BT.

(3) **Appliquer les métriques Environmental** : le service vulnérable est-il exposé sur Internet ou uniquement en interne ? (Modified Attack Vector). Des contrôles compensatoires sont-ils en place — WAF, segmentation, MFA, EDR ? (Modified Privileges Required, Modified User Interaction). Les données derrière le service sont-elles critiques pour le métier ? (Security Requirements CIA : High/Medium/Low). → Le score passe de CVSS-BT à CVSS-BTE.

(4) **Comparer les trois lectures** : le score externe (ce que dit l'éditeur), le score contextuel interne (ce que dit la réalité de l'environnement), et la gravité IR de l'incident (ce que dit l'impact opérationnel). Les trois sont documentés dans la fiche d'incident.

## 12.5 Ce que le rescoring contextuel NE fait PAS

Le rescoring contextuel CVSS ne remplace pas la qualification de gravité IR (P1/P2/P3/P4), qui reste une évaluation business et opérationnelle. Le FAQ FIRST rappelle que le score numérique seul ne porte pas tout le contexte — les métriques Environmental concernent le système vulnérable dans son environnement, pas la vulnérabilité « dans l'absolu ».

Un incident peut être P1 (gravité maximale) même si la CVE exploitée a un CVSS-BTE de 6.5 — parce que l'attaquant a pivoté vers des systèmes critiques après l'exploitation initiale. Inversement, un incident peut être P3 même si la CVE a un CVSS-B de 9.8 — parce que l'exploitation a été détectée et contenue immédiatement, sur un système non critique, sans propagation.

## 12.6 Ce que le rescoring contextuel SERT à faire

Il sert à **éclairer les décisions** pendant et après l'incident : priorisation du patching (quelle instance de la même vulnérabilité patcher en premier — celle avec le CVSS-BTE le plus élevé), extension du hunting (chercher l'exploitation de la même CVE sur d'autres systèmes — en priorisant les systèmes avec le CVSS-BE le plus élevé), périmètre de remédiation (les systèmes où la vulnérabilité est fortement compensée peuvent attendre ; ceux où elle est pleinement exposée sont P0), et plan de durcissement post-incident (le rescoring du backlog de vulnérabilités révèle les autres expositions critiques dans l'environnement réel).

En résumé : trois informations distinctes, trois usages distincts, documentées ensemble dans la fiche d'incident.

| Information | Question | Usage |
|-------------|----------|-------|
| Score CVSS-B externe (éditeur/NVD) | La vulnérabilité est-elle sévère en général ? | Référence, communication, comparaison |
| Score CVSS-BTE contextuel interne | La vulnérabilité est-elle sévère CHEZ NOUS ? | Priorisation patching, hunting, remédiation |
| Gravité IR de l'incident (P1-P4) | L'incident est-il grave pour l'organisation ? | Escalade, mobilisation, SLA, communication de crise |

---
