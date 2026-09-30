---
title: 'Partie III — Investigation : méthodes par domaine'
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*Cette partie enseigne les méthodes d'investigation — comment l'analyste navigue dans les données pour comprendre ce qui s'est passé. La Partie IV (Use Cases) enseigne les grands schémas de menace et leur logique de détection/réponse. La Partie VIII applique le tout de bout en bout.*

---

## Chapitre 10 — Principes de l'investigation SOC

### 10.1 Ce que signifie investiguer

Investiguer en SOC ne signifie pas « remplir un ticket ». Cela signifie comprendre ce qui s'est passé, avec quelle certitude, et quoi faire. L'investigation est un raisonnement structuré : l'analyste observe des faits (dans les logs), formule des hypothèses (ce qui pourrait s'être passé), les teste (en cherchant les données qui confirment ou contredisent), et conclut (avec un niveau de confiance explicite et des actions recommandées).

### 10.2 Qualification des alertes : la taxonomie opérationnelle

Chaque alerte reçue par le SOC doit être classifiée. Cette classification est une compétence centrale du métier.

**True Positive (VP) :** l'alerte détecte une menace réelle. Action : investigation approfondie, confinement, escalade si nécessaire. Exemple : l'alerte « certutil download cradle from Office » sur WKS-PROD-112 est un VP — un document malveillant a effectivement exécuté un téléchargement.

**False Positive (FP) :** l'alerte se déclenche sans menace réelle — la logique de détection a matché sur une activité légitime. Action : documenter le FP, évaluer si la règle doit être tunée, clôturer le ticket. Exemple : l'alerte « PowerShell -EncodedCommand » se déclenche sur un script SCCM de déploiement — l'activité est légitime.

**Benign True Positive (BTP) :** l'alerte est techniquement correcte (la détection a bien vu ce qu'elle devait voir) mais l'action est légitime. Ce n'est PAS un faux positif — la règle fonctionne correctement. Action : documenter comme BTP (pas comme FP — la distinction est importante pour les métriques), évaluer si une exception est justifiée. Exemple : l'alerte « PsExec remote service creation » se déclenche quand un admin IT utilise PsExec pour un déploiement planifié — la détection est correcte (PsExec a bien été utilisé), mais l'usage est légitime.

**Inconclusive :** l'analyste ne peut pas déterminer si l'alerte est un VP ou un FP avec les données disponibles. Action : enrichir (chercher des données supplémentaires), escalader si le risque est élevé et le doute persiste. Ne JAMAIS clôturer un ticket en « inconclusive » sans avoir documenté ce qui a été vérifié et pourquoi la conclusion est impossible.

### 10.3 Qualification de sévérité et critères d'escalade

La sévérité d'un incident VP combine la **criticité technique** (quel type de menace — phishing simple vs mouvement latéral vs ransomware) et la **criticité de l'asset** (un poste utilisateur standard vs un DC vs un serveur SCADA OIV).

| Sévérité | Critères | Exemples | Réponse |
|----------|----------|----------|---------|
| **Critique** | Compromission confirmée d'un asset critique, mouvement latéral actif, ransomware en cours, accès aux données sensibles | Kerberoasting sur un DC, ransomware en déploiement, accès SCADA non autorisé | Escalade immédiate, confinement en urgence, cellule de crise |
| **Haute** | Compromission confirmée d'un endpoint standard, exécution de malware, C2 actif | RAT avec beaconing actif, credential dumping sur un poste | Investigation L2 prioritaire, confinement rapide |
| **Moyenne** | Activité suspecte non confirmée comme malveillante, tentative détectée et bloquée | Phishing cliqué sans soumission de credentials, scan interne détecté | Investigation L2 dans les 4h |
| **Basse** | Anomalie mineure, policy violation, activité potentiellement suspecte | Impossible travel résolu par VPN, violation de politique d'usage | Investigation L1, clôture si bénin |

Les **critères d'escalade** (vers l'IR lead, le CERT, ou le RSSI) : mouvement latéral confirmé, compromission d'un compte privilégié (Domain Admin, admin cloud), accès à des données sensibles (R&D, finance, données personnelles), ransomware ou précurseurs (suppression des shadow copies, binaire de chiffrement identifié), compromission d'un asset OIV/critique, et doute sur l'étendue avec risque élevé.

### 10.4 Le pivoting

Le pivoting est la technique qui permet de naviguer entre les entités pour reconstruire l'histoire. À partir d'une IP source dans une alerte firewall, l'analyste pivote vers le hostname (CMDB/DNS/DHCP), puis vers l'utilisateur connecté (logs d'authentification), puis vers l'activité de cet utilisateur (tous ses logs), puis vers les processus exécutés (EDR/Sysmon), puis vers les connexions réseau de ces processus (Sysmon Event 3, firewall), puis vers les fichiers créés (Sysmon Event 11), etc. Chaque pivot ouvre une nouvelle dimension de l'investigation.

--- 

## Chapitre 11

|Référentiel|Question à laquelle il répond|Utilité SOC|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on ?|Corrélation, recherche, suivi|
|**CWE**|Quel type de faiblesse est en cause ?|Compréhension technique, généralisation|
|**CVSS**|À quel point c’est sévère techniquement ?|Priorisation initiale|
|**EPSS**|Quelle probabilité d’exploitation ?|Priorisation menace, hunting|
|**KEV**|Est-ce exploité dans le réel ?|Urgence opérationnelle|
