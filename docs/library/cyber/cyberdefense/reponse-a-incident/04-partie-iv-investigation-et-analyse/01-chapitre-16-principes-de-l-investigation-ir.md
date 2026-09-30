---
title: Chapitre 16 — Principes de l'investigation IR
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation ET analyse
  - index.md
---

## 16.1 Agir vite sans détruire la preuve

La tension fondamentale de l'investigation IR : collecter des évidences (rigueur, temps) tout en fournissant des réponses rapides aux décideurs (vitesse, pragmatisme). La méthode de résolution est le triage : collecte rapide des artefacts critiques d'abord (30 minutes par machine avec KAPE ou Velociraptor), image complète ensuite (si le temps et les ressources le permettent). Le triage donne 80 % de l'information en 20 % du temps ; l'image complète donne les 20 % restants mais prend 5 fois plus longtemps.

## 16.2 Investigation orientée décision

Chaque action d'investigation doit répondre à une question opérationnelle concrète. « Ce serveur est-il compromis ? » → pour décider de l'isoler. « L'attaquant a-t-il les privilèges domain admin ? » → pour décider de l'ampleur du confinement et du reset des comptes. « Des données personnelles ont-elles été exfiltrées ? » → pour décider de la notification CNIL. « Le krbtgt est-il compromis ? » → pour décider si un double reset est nécessaire. Si une action d'investigation ne répond à aucune question décisionnelle en cours, elle est dé-priorisée — ce n'est pas qu'elle est inutile, c'est qu'elle n'est pas urgente.

## 16.3 Hypothèses et itérativité

L'investigateur formule des hypothèses (« le point d'entrée est probablement un phishing sur le sous-traitant RH, car le premier compte compromis est un compte VPN du sous-traitant ») et les teste contre les données. Chaque hypothèse confirmée ouvre de nouvelles pistes. L'investigation n'est pas linéaire — elle est itérative, avec des allers-retours constants entre collecte, analyse, et reformulation des hypothèses.

## 16.4 Fil rouge — BLACKTIDE : les priorités d'investigation

> **🔍 BLACKTIDE — Épisode 16**
>
> Samedi 08h30. Nadia établit les 4 questions prioritaires pour les 12 prochaines heures, chacune assignée à un analyste :
>
> **Q1 (Thomas/PRIS) :** Quel est le patient zéro ? Remonter au point d'entrée initial. → Investigation forensic sur le poste du DRH GestPaie et les logs VPN.
>
> **Q2 (Léa/PRIS) :** Le compte krbtgt est-il compromis ? → Investigation AD, analyse des logs de réplication, vérification des tickets Kerberos.
>
> **Q3 (Karim/SOC) :** Quel est le volume exact de données exfiltrées ? Quelles données ? → Analyse des logs proxy, identification des fichiers accédés avant l'exfiltration.
>
> **Q4 (Fatima/SOC) :** L'attaquant est-il toujours actif dans le réseau ? → Surveillance temps réel des communications C2, monitoring des authentifications suspectes.

---
