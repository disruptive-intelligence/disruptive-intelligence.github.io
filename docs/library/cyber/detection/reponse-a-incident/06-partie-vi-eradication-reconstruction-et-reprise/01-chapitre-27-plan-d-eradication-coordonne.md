---
title: Chapitre 27 — Plan d'éradication coordonné
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction et reprise
  - index.md
---

## 27.1 Éradication simultanée, pas séquentielle

Si l'éradication est menée machine par machine, l'attaquant réinfecte les machines nettoyées depuis les machines non encore traitées. Le plan d'éradication doit être coordonné : un « jour J » est planifié (typiquement quelques jours après la fin de l'investigation, le temps de préparer toutes les actions), et toutes les mesures d'éradication sont exécutées simultanément dans une fenêtre courte (4 à 8 heures).

Le plan d'éradication liste exhaustivement toutes les actions à mener, l'ordre d'exécution (certaines actions dépendent d'autres — le double reset du krbtgt doit être fait avant le reset massif des comptes), les responsables de chaque action, et les validations post-exécution (comment vérifie-t-on que chaque action a réussi ?).

## 27.2 Suppression des mécanismes de persistance

Pour chaque mécanisme identifié au Ch.20 : suppression des tâches planifiées malveillantes (vérification sur tout le parc via Velociraptor ou GPO de nettoyage), désinstallation des services Windows parasites (identification par nom, chemin, et hash), nettoyage des clés de registre Run/RunOnce, suppression des comptes créés par l'attaquant (après documentation — les comptes sont une preuve), retrait de la GPO malveillante (suppression complète, pas simple désactivation), suppression des règles de forwarding email (vérification de toutes les boîtes mail du domaine, pas seulement celles identifiées), révocation de tous les tokens cloud (M365, Azure, AWS — forcer une réauthentification complète), retrait des clés SSH non autorisées (vérification de tous les serveurs Linux), et correction des ACL/DACL modifiées sur l'AD (retour aux permissions d'origine, documentées).

## 27.3 Le cas du krbtgt compromis

Quand le hash du krbtgt est compromis (DCSync confirmé), l'attaquant peut forger des Golden Tickets — des TGT qui ne seront pas invalidés par un simple reset des mots de passe utilisateurs. Le seul remède est le **double reset du krbtgt** : deux resets du mot de passe du compte krbtgt espacés de 12 heures minimum.

Pourquoi deux resets ? Kerberos retient les 2 derniers mots de passe du krbtgt (pour permettre la transition sans interruption de service). Un seul reset invalide le mot de passe N-1 mais les tickets forgés avec le mot de passe N (celui que l'attaquant connaît) restent valides tant que N est l'un des 2 derniers mots de passe. Le second reset pousse N en position N-2 (plus retenu par Kerberos), invalidant tous les Golden Tickets.

Procédure : premier reset du krbtgt à T0, vérification du fonctionnement de l'authentification Kerberos (les perturbations sont normalement limitées mais possibles — surveiller les tickets de service), second reset à T0+12h minimum (certaines recommandations préconisent T0+24h pour plus de sécurité), re-vérification du fonctionnement.

Le double reset du krbtgt impacte le fonctionnement de Kerberos pendant la transition — tous les TGT en circulation deviennent invalides et doivent être renouvelés. L'impact est généralement transparent (les systèmes renouvellent automatiquement) mais peut causer des dysfonctionnements sur les systèmes legacy ou mal configurés. Le reset doit être planifié dans la fenêtre d'éradication avec une surveillance active des dysfonctionnements.

## 27.4 Fil rouge — BLACKTIDE : le jour J

> **🔍 BLACKTIDE — Épisode 27**
>
> Le « jour J » est planifié pour le mercredi 19 mars, de 22h à 04h (fenêtre de maintenance). L'équipe est constituée de 4 analystes internes + 2 consultants PRIS + 3 admins système.
>
> Séquence d'éradication :
> 1. 22h00 : Premier reset du krbtgt sur DC01.
> 2. 22h15 : Suppression des 3 comptes admin cachés (svc_monitor01, svc_backup_ext, svc_audit_temp).
> 3. 22h30 : Suppression de la GPO « Windows Update Configuration ».
> 4. 22h45 : Nettoyage des scheduled tasks malveillantes sur les 40+ machines (via Velociraptor — exécution centralisée).
> 5. 23h00 : Correction des ACL sur l'OU des serveurs critiques (retrait du GenericAll de svc_deploy).
> 6. 23h15 : Révocation de tous les tokens M365 (forçage de réauthentification).
> 7. 23h30 : Désactivation du compte VPN `admin_rh_ext` (sous-traitant GestPaie).
> 8. 00h00 : Rotation de tous les mots de passe des comptes de service (25 comptes).
> 9. 10h00 (J+1) : Second reset du krbtgt (T0+12h).
> 10. 12h00 : Forçage du changement de mot de passe pour TOUS les comptes utilisateurs du domaine (12 000 comptes — communication préparée, helpdesk renforcé pour le lundi).

---
