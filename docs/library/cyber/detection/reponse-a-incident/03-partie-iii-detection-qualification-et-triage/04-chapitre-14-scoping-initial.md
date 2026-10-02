---
title: Chapitre 14 — Scoping initial
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie III — Détection, qualification et triage
  - index.md
---

délimiter l'étendue de la compromission

## 14.1 La question la plus critique et la plus difficile

L'attaquant a-t-il compromis un seul poste, un segment réseau, ou le domaine entier ? La réponse conditionne toutes les décisions suivantes : le périmètre du confinement (isoler 3 machines ou 3 sites ?), le dimensionnement de l'équipe IR (3 analystes ou 15 ?), les notifications réglementaires (incident technique interne ou violation de données à déclarer ?), et la durée prévisible de la réponse (2 jours ou 3 semaines ?).

Le scoping est un exercice d'approximation rapide — il sera affiné au fil de l'investigation, mais la première estimation doit être produite dans les premières heures pour guider les décisions de confinement. Sous-estimer le périmètre conduit à un confinement insuffisant. Surestimer conduit à un impact business disproportionné.

## 14.2 Méthode de scoping rapide

Croiser les sources disponibles dans les premières heures pour délimiter le périmètre. Les IoC identifiés (hash du malware, domaine C2, IP C2) sont recherchés sur l'ensemble du parc via l'EDR — quelles machines ont communiqué avec le C2, exécuté le hash, ou présenté les mêmes artefacts ? Les logs d'authentification Active Directory sont analysés — quels comptes ont été utilisés, depuis quelles machines, à quelles heures ? Y a-t-il des authentifications anormales (geo-impossible, horaires inhabituels, comptes de service utilisés manuellement) ? Les logs réseau sont examinés — quels systèmes communiquent avec des destinations suspectes ?

L'intersection de ces sources donne le périmètre initial : les machines confirmées compromises, les machines probablement compromises, et les machines non touchées (à ce stade).

## 14.3 Première timeline

La timeline provisoire est la reconstitution chronologique des événements identifiés à ce stade. Elle sera enrichie et corrigée tout au long de l'investigation (Ch.17), mais la première version oriente le scoping : si le premier signe de compromission remonte à 5 semaines, tout ce qui s'est passé pendant ces 5 semaines doit être investigué.

## 14.4 Fil rouge — BLACKTIDE : le scoping

> **🔍 BLACKTIDE — Épisode 14**
>
> En 3 heures (22h30-01h30), l'équipe établit un périmètre provisoire.
>
> **Confirmé compromis :** DC01, DC02, DC03 (traces de PsExec, GPO malveillante, exécution du ransomware builder). Serveur de fichiers FS01-Lyon, FS01-Fos, FS01-Cologne (chiffrement en cours). Le poste du DRH de GestPaie (sous-traitant — point d'entrée de l'infostealer, confirmé par analyse de l'alerte antivirus de J-30).
>
> **Probablement compromis :** 40+ machines listées dans les logs PsExec. Le serveur SCCM (utilisé comme pivot via le compte svc_deploy). Au moins un serveur du réseau OT de Fos (le poste d'ingénierie a des traces de connexion depuis DC01).
>
> **Volume estimé de l'exfiltration :** 380 Go (identifié par corrélation des logs proxy — flux HTTPS vers des endpoints AWS S3 depuis 3 machines internes, sur 7 jours).
>
> **Timeline provisoire :** Patient zéro estimé à J-35 (phishing sur GestPaie). Compromission de l'AD estimée à J-14 (DCSync). Début d'exfiltration estimé à J-7. Déploiement du ransomware : J-0.

---
