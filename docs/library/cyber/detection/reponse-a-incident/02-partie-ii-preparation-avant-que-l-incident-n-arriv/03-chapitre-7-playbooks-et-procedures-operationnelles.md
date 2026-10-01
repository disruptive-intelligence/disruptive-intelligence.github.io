---
title: Chapitre 7 — Playbooks et procédures opérationnelles
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 7.1 Qu'est-ce qu'un playbook IR

Un playbook IR est un document opérationnel, court (5 à 10 pages maximum), qui décrit les actions concrètes à mener pour un type d'incident spécifique. Ce n'est pas l'IRP (qui est le cadre général de la capacité IR) — c'est la procédure détaillée pour un cas précis, avec des actions numérotées, des responsables identifiés, des seuils de décision, et des pointeurs vers les outils et commandes à utiliser.

Le playbook est le document que l'analyste ouvre à 3h du matin quand il est fatigué et stressé. Il doit être immédiatement actionnable : pas de prose de 3 pages avant la première action, pas de jargon inutile, pas de renvois vers 10 autres documents. L'action 1 doit pouvoir être exécutée dans les 5 premières minutes.

## 7.2 Playbooks essentiels

Chaque organisation doit disposer au minimum des playbooks suivants, adaptés à son contexte.

**Playbook phishing** : trigger (alerte utilisateur ou détection email malveillant), actions immédiates (extraction des IoC : URL, pièce jointe, expéditeur ; recherche dans les boîtes mail de tous les destinataires ; isolation du poste de l'utilisateur qui a cliqué), investigation (le lien a-t-il été cliqué ? les credentials ont-elles été saisies ? le malware a-t-il été exécuté ?), confinement (blocage du domaine/hash au niveau proxy/EDR, reset du mot de passe si credentials compromises), et communication (notification aux utilisateurs touchés).

**Playbook ransomware** : trigger (détection EDR ou découverte de fichiers chiffrés), actions immédiates (isolation réseau des systèmes touchés — NE PAS éteindre avant collecte), évaluation (quel variant ? quel périmètre ? les sauvegardes sont-elles intactes ? le DC est-il compromis ?), confinement réseau (voir Ch.23), collecte forensic (RAM + triage KAPE avant tout reset), notification (ANSSI si OIV, CNIL si données personnelles), et décision sur la rançon (voir Ch.32).

**Playbook compromission de compte** : trigger (alerte SIEM sur comportement anormal, notification de geo-impossible travel, signalement utilisateur), actions (désactivation immédiate du compte, reset mot de passe, révocation des sessions actives et tokens OAuth, recherche d'activité suspecte : règles de forwarding email, accès aux données, création de comptes, modifications de configuration).

**Playbook malware** : trigger (détection EDR/antivirus), actions (isolation du poste via EDR containment, collecte du sample pour analyse, soumission sandbox, recherche de propagation latérale — le même hash est-il détecté sur d'autres machines ?), classification (commodity malware vs ciblé, infostealer vs RAT vs ransomware).

**Playbook exfiltration de données** : trigger (alerte DLP, volume anormal de trafic sortant, notification externe), investigation (quelles données ? quel volume ? vers quelle destination ?), confinement (blocage du canal d'exfiltration), et notification (CNIL si données personnelles, sous 72h).

**Playbook compromission cloud** : trigger (alerte Entra ID / CloudTrail), investigation (Sign-in Logs pour les accès anormaux, Unified Audit Log pour les actions, app registrations suspectes, conditional access policies modifiées), confinement (révocation de tokens, reset MFA, désactivation des app registrations suspectes).

Les playbooks détaillés avec les commandes concrètes sont en Annexe E.

## 7.3 Concevoir un bon playbook

Structure type d'un playbook opérationnel :

**En-tête :** nom du playbook, version, date de dernière mise à jour, auteur, conditions de déclenchement (trigger).

**Actions immédiates** (0-15 minutes) : ce que l'analyste de garde doit faire sans attendre de validation. Chaque action a un responsable et un livrable.

**Actions d'investigation** (15 min - 4 heures) : les vérifications et analyses nécessaires pour qualifier l'incident et décider du confinement. Inclut les commandes concrètes (requêtes SIEM, commandes EDR, scripts de collecte).

**Actions de confinement** : les mesures de limitation de la progression, avec les critères de décision (quand isoler, quand couper, quand observer).

**Critères d'escalade** : à quel moment et vers qui escalader si la gravité s'avère supérieure à la classification initiale.

**Actions de communication** : qui informer, quand, avec quel message type.

**Actions de clôture** : vérifications post-résolution, documentation, et lien vers le RETEX.

## 7.4 Maintenir les playbooks vivants

Un playbook non testé est un playbook mort. Les playbooks doivent être testés en exercice (Ch.10), révisés après chaque incident où ils ont été utilisés (le RETEX identifie les actions manquantes ou inadaptées), et mis à jour quand l'environnement change (nouveau SIEM, nouvel EDR, changement d'architecture, nouveau type de menace).

Fréquence de révision recommandée : après chaque utilisation en incident réel, après chaque exercice, et au minimum une fois par an même sans utilisation.

## 7.5 Fil rouge — BLACKTIDE : le playbook ransomware insuffisant

> **🔍 BLACKTIDE — Épisode 7**
>
> Arvantis a un playbook ransomware — incomplet. Il décrit les actions de confinement réseau (isolation VLAN, coupure Internet) mais ne couvre pas le cas d'un AD compromis en profondeur (pas de procédure de double reset krbtgt, pas de procédure de reconstruction DC). Il ne mentionne pas l'articulation avec l'ANSSI en cas d'OIV impacté. Il ne traite pas le cas spécifique de l'environnement OT (comment confiner le réseau sans arrêter les automates SCADA ?). Et il n'a jamais été testé en exercice.
>
> Nadia l'utilise comme base mais doit improviser sur environ 40 % des actions. Elle note dans le journal : « Playbook ransomware utilisé — lacunes identifiées : pas de procédure AD compromis, pas de volet OT, pas de volet notification OIV. À mettre à jour en RETEX. »

---
