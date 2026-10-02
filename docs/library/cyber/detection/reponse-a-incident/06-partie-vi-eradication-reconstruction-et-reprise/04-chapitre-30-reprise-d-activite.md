---
title: Chapitre 30 — Reprise d'activité
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction et reprise
  - index.md
---

## 30.1 Priorisation des services

La reprise ne se fait pas en « big bang » — elle est progressive et priorisée en fonction de l'impact business. Les services critiques (messagerie, VPN pour le télétravail, systèmes de production industrielle, systèmes de paiement) reprennent en premier. Les services secondaires (applications RH, intranet, outils collaboratifs non essentiels) reprennent ensuite. Chaque service redémarré est validé fonctionnellement (le service fonctionne-t-il ?) et sécuritairement (aucun indicateur de compromission ?) avant le suivant.

## 30.2 Critères de retour nominal

Le SI est considéré comme revenu à un état normal quand tous les systèmes sont opérationnels et les performances normales, les sauvegardes fonctionnent sur la nouvelle architecture immuable, la surveillance est revenue au niveau standard (plus de monitoring renforcé), aucune action résiduelle d'éradication n'est en cours, et les processus métiers fonctionnent sans workaround.

## 30.3 Fil rouge — BLACKTIDE : la reprise progressive

> **🔍 BLACKTIDE — Épisode 30**
>
> La production reprend progressivement sur 12 jours (pas « lundi » comme le CEO le voulait).
> - J+5 : Messagerie M365 et VPN (12 000 utilisateurs retrouvent l'email et l'accès distant).
> - J+7 : Serveurs de fichiers restaurés (avec 6 jours de perte de données sur les bandes).
> - J+8 : Applications métier non critiques (ERP en lecture seule pour vérification).
> - J+10 : Production reprise sur les 12 sites non impactés (qui fonctionnaient en mode dégradé par précaution — interdiction des flux inter-sites levée).
> - J+12 : Production reprise sur les 3 sites impactés (Fos, Lyon, Cologne). Le site OIV de Fos est le dernier — la reprise est conditionnée à la validation conjointe ANSSI/Arvantis de l'intégrité du réseau SCADA.

---
