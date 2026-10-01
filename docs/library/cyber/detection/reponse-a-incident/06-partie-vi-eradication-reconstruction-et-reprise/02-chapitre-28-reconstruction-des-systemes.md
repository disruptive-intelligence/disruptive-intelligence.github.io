---
title: Chapitre 28 — Reconstruction des systèmes
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction et reprise
  - index.md
---

## 28.1 Reconstruire plutôt que nettoyer

Le principe fondamental de la reconstruction post-incident : un système compromis ne peut jamais être « nettoyé » avec certitude absolue. Le nettoyage (suppression du malware visible, patchs, reset des configurations) laisse un doute résiduel — l'attaquant a pu installer un mécanisme de persistance non détecté par l'investigation (rootkit, firmware implant, backdoor dans un fichier système légitime). Le seul moyen fiable de garantir l'éradication est la reconstruction à partir de sources propres : images gold (images système de référence, maintenues à jour), sauvegardes vérifiées antérieures à la compromission, ou installation fraîche depuis les médias d'origine.

En pratique, la reconstruction complète de tout le parc est rarement réalisable (trop long, trop coûteux). L'approche courante est un mix : reconstruction des systèmes critiques (DC, serveurs d'infrastructure, serveurs sensibles), nettoyage vérifié des systèmes moins critiques (postes de travail — réinstallation du poste si compromission confirmée, scan EDR approfondi sinon), et surveillance renforcée post-éradication (Ch.29) pour détecter une persistance non identifiée.

## 28.2 Reconstruction par cercles de confiance

L'infrastructure est reconstruite en 3 cercles concentriques. Le **cercle 1 (noyau de confiance)** comprend les DC, le DNS interne, la PKI, l'infrastructure de sécurité (EDR console, SIEM, serveur de logs). Ces systèmes sont reconstruits en premier, à partir d'images gold, sur un réseau isolé. Ils forment le « noyau dur » à partir duquel le reste est déployé. Le **cercle 2 (services critiques)** comprend les serveurs de fichiers, la messagerie, les applications métier essentielles, le VPN, les portails clients. Ils sont reconstruits ou restaurés une fois le cercle 1 validé. Le **cercle 3 (reste du parc)** comprend les postes de travail, les services secondaires, les applications non critiques. Chaque cercle n'est reconnecté au réseau de production qu'après vérification complète du cercle précédent.

## 28.3 Restauration des données

La restauration des données (à distinguer de la reconstruction des systèmes) pose des questions spécifiques. Les sauvegardes sont-elles intactes ? (si elles sont chiffrées par le ransomware, elles sont inutilisables). Sont-elles antérieures à la compromission ? (attention au dwell time — si la compromission a commencé il y a 5 semaines et que les sauvegardes ont 4 semaines, elles contiennent potentiellement le malware ou des backdoors). Contiennent-elles des données exploitables ? (une sauvegarde de données utilisateur est différente d'une sauvegarde d'image système — restaurer les données sur un système reconstruit proprement est la bonne approche, restaurer une image système potentiellement compromise est la mauvaise).

Stratégie recommandée : restaurer les DONNÉES sur des SYSTÈMES reconstruits proprement (pas les images système depuis des sauvegardes qui pourraient être compromises). Vérifier l'intégrité des données restaurées (scan EDR, recherche d'artefacts malveillants).

## 28.4 Fil rouge — BLACKTIDE : la reconstruction

> **🔍 BLACKTIDE — Épisode 28**
>
> La reconstruction suit le modèle par cercles de confiance.
>
> **Cercle 1 (J+5 à J+7) :** 3 DC reconstruits à partir d'images gold Windows Server 2022, durcis selon les recommandations CIS Benchmark. L'AD est nettoyé en profondeur (option a du Ch.28 — pas de reconstruction complète, car la compromission est bien délimitée après le double reset krbtgt et la suppression des comptes/GPO/ACL). SIEM Splunk vérifié. Console EDR CrowdStrike vérifiée.
>
> **Cercle 2 (J+7 à J+10) :** Serveurs de fichiers reconstruits (installation fraîche Windows Server 2022). Données restaurées depuis les sauvegardes hebdomadaires sur bandes offline — intactes, mais avec 6 jours de perte de données (les sauvegardes quotidiennes sur NAS réseau sont partiellement chiffrées — inutilisables). Messagerie Microsoft 365 : tokens révoqués, conditional access policies renforcées, règles de forwarding malveillantes supprimées.
>
> **Cercle 3 (J+10 à J+12) :** Postes de travail des 3 sites impactés : les postes confirmés compromis (12 machines) sont réinstallés. Les autres subissent un scan EDR approfondi et un reset de l'utilisateur local admin (LAPS activé à cette occasion).

---
