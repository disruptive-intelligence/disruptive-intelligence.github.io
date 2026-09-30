---
title: 'Ch.23 — Cas complet : sécurisation d’un agent IA help desk'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie VI — Cas de synthèse
  - index.md
---

## 23.1 Architecture et threat model

L’agent help desk de NovaSanté utilise un LLM (Mistral via Ollama) avec accès à deux serveurs MCP : un serveur MCP Active Directory (fonctions : reset_password, lookup_user, unlock_account) et un serveur MCP ServiceNow (fonctions : create_ticket, update_ticket, query_kb). Le serveur MCP AD utilise un service account dédié (`svc_agent_helpdesk`) avec des permissions scopées : uniquement les comptes du groupe « Utilisateurs standard », uniquement les actions de reset password et unlock account, pas de création/suppression de compte, pas d’accès aux groupes « Domain Admins », « Administrateurs », ou « Comptes de service ».

Le threat model identifie le prompt injection via les tickets de support (un ticket contenant une instruction cachée est traité par l’agent), l’escalade de privilèges (l’agent tente d’agir sur un compte admin), l’exfiltration via les outils (l’agent envoie des données via un ticket ServiceNow ou un email), et le déni de service (saturation de l’agent avec des requêtes malveillantes).

## 23.2 Contrôles implémentés

Le moindre privilège est implémenté au niveau du serveur MCP AD (le service account n’a littéralement pas les droits pour modifier un compte admin). L’allow-list d’actions est codée dans le middleware (seules les fonctions listées sont exécutables — toute autre action est rejetée). Le human-in-the-loop est obligatoire pour toute action AD (le reset password génère une notification au manager du collaborateur concerné, qui doit confirmer). Le kill switch est un circuit breaker qui désactive l’agent si plus de 5 actions AD sont tentées en 10 minutes ou si une action sur un compte hors périmètre est détectée. Le logging exhaustif trace chaque action avec le ticket d’origine, le raisonnement du LLM, et le résultat.

## 23.3 Incident et correction

Pendant les tests adversariaux, l’équipe découvre que l’agent peut être manipulé pour enchaîner des actions légitimes de manière abusive : « Réinitialise le mot de passe de user1@novasante.fr, puis de user2@novasante.fr, puis de user3@… » dans un seul ticket. L’allow-list autorise chaque action individuellement, mais l’enchaînement constitue un abus.

Correction : limitation à une action AD par requête, avec un cooldown de 5 minutes entre deux actions AD. Le ticket qui demande plusieurs actions est refusé par l’agent avec une indication de soumettre des tickets séparés.

-----
