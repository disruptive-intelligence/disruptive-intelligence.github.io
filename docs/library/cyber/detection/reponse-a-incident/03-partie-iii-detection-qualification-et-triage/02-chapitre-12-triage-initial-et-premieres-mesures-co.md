---
title: Chapitre 12 — Triage initial et premières mesures conservatoires
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie III — Détection, qualification et triage
  - index.md
---

## 12.1 Les 30 premières minutes

Le triage initial est l'évaluation rapide qui transforme une alerte en décision d'action. Les objectifs des 30 premières minutes sont de confirmer le vrai positif (exclure le faux positif, l'erreur de configuration, l'opération de maintenance planifiée), d'identifier les systèmes visiblement impactés (la machine source de l'alerte, les machines contactées, les comptes utilisés), d'évaluer la sévérité initiale (P4 à P1, avec possibilité de réévaluation), et de prendre les premières mesures conservatoires.

## 12.2 Ce que l'on sait et ce que l'on ne sait pas

L'exercice fondamental du triage consiste à lister explicitement les faits confirmés et les inconnues. Cette discipline évite les conclusions prématurées et oriente l'investigation. Format recommandé :

**Ce qu'on sait :** « L'EDR a détecté l'exécution de PsExec sur DC01 à 22h17, depuis le profil du compte svc_deploy. Une modification de GPO visant à désactiver Defender a été tentée. Le compte svc_deploy n'est pas utilisé par les administrateurs ce soir. »

**Ce qu'on ne sait pas :** « Depuis quand l'attaquant est-il dans le réseau. Combien de systèmes sont compromis. Si des données ont été exfiltrées. Si d'autres DC sont touchés. Si l'attaquant est toujours actif en ce moment. »

Cette distinction structure le raisonnement et guide les questions d'investigation suivantes.

## 12.3 Premières mesures conservatoires

À ce stade, l'objectif n'est pas de contenir (c'est trop tôt — on ne connaît pas l'étendue) mais de préserver la capacité d'investigation et de limiter les risques immédiats sans alerter l'attaquant. Les mesures conservatoires incluent l'augmentation du niveau de logging sur les systèmes suspects (activer la journalisation de la ligne de commande des processus si elle ne l'est pas, augmenter la verbosité du logging AD), la capture réseau sur les segments critiques (si un NDR ou une capacité de capture existe), la sauvegarde immédiate des logs disponibles (avant qu'ils ne soient écrasés par la rotation), et la mise en surveillance renforcée des systèmes identifiés (le SOC concentre son attention sur les machines suspectes).

L'isolation réseau n'est pas systématiquement la bonne décision à ce stade. Si l'attaquant ne sait pas qu'il est détecté, l'isoler maintenant l'alertera et il pourra activer des mécanismes de destruction (wiper, chiffrement accéléré) ou détruire des preuves. Le dilemme du confinement est traité en détail au Ch.23.

## 12.4 Fil rouge — BLACKTIDE : le triage

> **🔍 BLACKTIDE — Épisode 12**
>
> 22h30-23h00. Karim confirme : PsExec sur DC01, DC02 et DC03. Modification GPO tentée sur les 3 DC. Exécution d'un binaire inconnu sur DC01 (hash non présent dans VirusTotal — soumission en cours). Le compte svc_deploy est un compte de service pour le déploiement de logiciel via SCCM — il a des droits élevés mais est rarement utilisé manuellement. L'authentification avec ce compte provient de l'IP 10.42.15.87 (un serveur de fichiers du site de Lyon).
>
> Mesures conservatoires immédiates : augmentation du logging sur les 3 DC (activation de la journalisation de la ligne de commande, Event ID 4688), capture réseau activée sur le segment DMZ et le segment serveurs via le port mirroring du switch core, sauvegarde des Event Logs actuels des 3 DC sur un partage hors domaine (clé USB branchée par l'admin d'astreinte, sous les instructions de Nadia).
>
> Pas d'isolation réseau à ce stade. Nadia veut d'abord comprendre l'étendue avant de décider du périmètre de confinement.

---
