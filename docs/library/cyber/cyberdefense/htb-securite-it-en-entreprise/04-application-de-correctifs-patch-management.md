---
title: Application de correctifs — Patch Management
source: Cyber/04_Hardening/HTB_Sécurité IT en entreprise.md
note: HTB — Sécurité IT en entreprise
up:
- - HTB — Sécurité IT en entreprise
  - index.md
---

- Déployer les correctifs de **logiciels, OS et firmware** aussi rapidement que possible, en prenant évidemment en compte les contraintes liés à l'infrastructure, s'assurer qu'une montée de version ne bloque rien.
- Activer les **mises à jour automatiques** lorsqu’elles sont compatibles avec les contraintes de l’environnement.

```
Vulnérabilité connue
→ Correctif disponible
→ Déploiement
→ Réduction de la fenêtre d'exposition
```

## SLA de patching

- Un **SLA — Service-Level Agreement** définit notamment un **délai maximal attendu** pour effectuer une action ou fournir un service.
- Dans le cadre du patch management :

```
Criticité de la vulnérabilité
→ délai maximum de correction
```

- Exemple :

```
Critical → patch ≤ 48h
High     → patch ≤ 7 jours
Medium   → patch ≤ 30 jours
```


> Les délais exacts dépendent de la politique et du niveau de risque de l’organisation.
## Priorisation des correctifs

- Le délai ne doit pas dépendre uniquement du score CVSS.
- Critères importants :

|Critère|Impact sur la priorité|
|---|---|
|**CVSS**|Mesure la sévérité technique de la vulnérabilité|
|**Internet Exposure**|Un serveur exposé publiquement est généralement prioritaire|
|**Known Exploitation**|Vulnérabilité activement exploitée → priorité très élevée|
|**Asset Criticality**|Un système critique doit être traité plus rapidement|
|**Exploit Availability**|Exploit public disponible → risque accru|

```
CVSS élevé
+
Internet-facing
+
Exploit public / exploitation active
→ Patch prioritaire
```

## CVE vs CVSS

```
CVE  → identifiant d'une vulnérabilité
CVSS → score de sévérité de cette vulnérabilité
```

- Exemple :

```
CVE-2026-XXXX
CVSS: 9.8 Critical
```

## Zero-Day

- **Zero-day** : vulnérabilité pour laquelle aucun correctif n’est encore disponible au moment où elle est découverte/exploitée.
- Dès qu’un patch existe, il faut le déployer selon une priorité élevée si le risque le justifie.

> À distinguer de **Known Exploited Vulnerability** : une vulnérabilité peut être activement exploitée sans être un zero-day.
## Bon processus de patching

- connaître les assets/version via l’inventaire ;
- identifier les vulnérabilités ;
- prioriser selon le risque ;
- tester si nécessaire avant production ;
- déployer ;
- vérifier que le patch a réellement été appliqué.
